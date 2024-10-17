import os
import cv2
import zipfile
from mtcnn import MTCNN

# Directory paths
data_dir = os.path.join(os.getcwd(), "data")
output_dir = os.path.join(
    os.getcwd(), "output"
)  # Path to save cropped images before zipping
zip_output_path = os.path.join(
    os.getcwd(), "databox.zip"
)  # Path to save the final zip file

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize MTCNN face detector
detector = MTCNN()


# Function to detect faces, crop, convert to grayscale, and save the output image
def process_and_save_image(image_path, output_subdir):
    try:
        # Load the image
        img = cv2.imread(image_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Detect faces in the image
        faces = detector.detect_faces(img_rgb)

        # Log the number of faces detected
        print(f"{len(faces)} face(s) detected in {os.path.basename(image_path)}")

        # Process each detected face
        for i, face in enumerate(faces):
            x, y, width, height = face["box"]

            # Crop the image to the bounding box
            cropped_img = img_rgb[y : y + height, x : x + width]

            # Convert cropped image to grayscale
            gray_cropped_img = cv2.cvtColor(cropped_img, cv2.COLOR_RGB2GRAY)

            # Construct output file path
            base_filename = os.path.splitext(os.path.basename(image_path))[0]
            output_filename = (
                f"{base_filename}_face_{i+1}.png"  # Save each face separately
            )
            output_path = os.path.join(output_subdir, output_filename)

            # Save the cropped grayscale image
            cv2.imwrite(output_path, gray_cropped_img)

            print(f"Processed and saved: {output_path}")

    except Exception as e:
        print(f"Error processing {image_path}: {e}")


# Create a zip file to store the processed images
with zipfile.ZipFile(zip_output_path, "w") as zipf:
    # Traverse the directory and detect faces in each image
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):  # Filter image files
                image_path = os.path.join(root, file)

                # Determine user subdirectory for output (based on the input folder structure)
                subdir_name = os.path.relpath(
                    root, data_dir
                )  # Subdirectory relative to the data directory
                output_subdir = os.path.join(output_dir, subdir_name)

                # Create the output subdirectory if it doesn't exist
                if not os.path.exists(output_subdir):
                    os.makedirs(output_subdir)

                # Process and save the image
                process_and_save_image(image_path, output_subdir)

                # Add the processed images to the zip file (maintaining folder structure)
                for subroot, _, subfiles in os.walk(output_subdir):
                    for subfile in subfiles:
                        file_path_in_zip = os.path.relpath(
                            os.path.join(subroot, subfile), output_dir
                        )
                        zipf.write(os.path.join(subroot, subfile), file_path_in_zip)

print(f"Processed images have been saved to {zip_output_path}")
