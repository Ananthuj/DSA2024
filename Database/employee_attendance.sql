CREATE DATABASE  IF NOT EXISTS `employee_attendance` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `employee_attendance`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: employee_attendance
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attendance`
--

DROP TABLE IF EXISTS `attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendance` (
  `attendance_id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int DEFAULT NULL,
  `employee_name` varchar(50) NOT NULL,
  `checkin_time` timestamp NULL DEFAULT NULL,
  `checkout_time` timestamp NULL DEFAULT NULL,
  `attendance_date` date DEFAULT NULL,
  `attendance_status` enum('present','absent','leave') DEFAULT NULL,
  PRIMARY KEY (`attendance_id`),
  KEY `employee_id` (`employee_id`),
  CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendance`
--

LOCK TABLES `attendance` WRITE;
/*!40000 ALTER TABLE `attendance` DISABLE KEYS */;
INSERT INTO `attendance` VALUES (1,1,'John Smith','2024-10-08 03:35:07','2024-10-08 12:45:03','2024-10-08','present'),(2,2,'Sandra Sunil','2024-10-08 04:31:08','2024-10-08 12:15:36','2024-10-08','present'),(3,3,'Malavika Menon','2024-10-08 02:50:45','2024-10-08 12:34:07','2024-10-08','present'),(4,4,'Aswathy Ritu','2024-10-08 03:19:09','2024-10-08 12:39:34','2024-10-08','present'),(5,5,'Arun p','2024-10-08 04:15:00','2024-10-08 12:25:09','2024-10-08','present'),(6,6,'Richu narayanan','2024-10-08 05:00:04','2024-10-08 12:19:01','2024-10-08','present'),(7,7,'Olivia Garcia','2024-10-08 05:17:00','2024-10-08 12:36:36','2024-10-08','present'),(8,8,'Emily Davis',NULL,NULL,'2024-10-08','absent'),(9,9,'Miriya Alexander','2024-10-08 03:40:00','2024-10-08 12:30:00','2024-10-08','present'),(10,10,'Benjamin Lee','2024-10-08 04:08:09','2024-10-08 12:29:08','2024-10-08','present'),(11,11,'Lina Satheesh','2024-10-08 04:09:09','2024-10-08 12:39:10','2024-10-08','present'),(12,12,'Sophia Martinez',NULL,NULL,'2024-10-08','absent'),(13,13,'Michael Johnson','2024-10-08 03:30:00','2024-10-08 12:00:04','2024-10-08','present'),(14,14,'William Brown','2024-10-08 03:27:02','2024-10-08 12:32:00','2024-10-08','present'),(15,15,'James Wilson',NULL,NULL,'2024-10-08','absent'),(16,16,'Isabella Walker',NULL,NULL,'2024-10-08','absent'),(17,17,'Alexander Young','2024-10-08 03:39:49','2024-10-08 12:15:09','2024-10-08','present'),(18,18,'Mia Harris','2024-10-08 03:38:58','2024-10-08 12:47:00','2024-10-08','present'),(19,19,'Daniel Clark','2024-10-08 03:39:08','2024-10-08 12:53:00','2024-10-08','present'),(20,20,'Amelia Lewis','2024-10-08 03:30:06','2024-10-08 12:25:09','2024-10-08','present'),(21,21,'Lucas King',NULL,NULL,'2024-10-08','absent'),(22,22,'Charlotte Wright','2024-10-08 03:33:23','2024-10-08 12:00:09','2024-10-08','present'),(23,23,'Liam Scott','2024-10-08 03:38:00','2024-10-08 12:00:09','2024-10-08','present'),(24,24,'Ava Green','2024-10-08 03:55:00','2024-10-08 12:30:02','2024-10-08','present'),(25,25,'Mason Baker',NULL,NULL,'2024-10-08','absent'),(26,26,'Harper Hill',NULL,NULL,'2024-10-08','absent'),(27,27,'Elijah Adams','2024-10-08 04:15:08','2024-10-08 12:15:09','2024-10-08','present'),(28,28,'Abigail Nelson','2024-10-08 03:33:40','2024-10-08 12:39:36','2024-10-08','present'),(29,29,'Jacob Carter','2024-10-08 03:17:07','2024-10-08 12:36:10','2024-10-08','present'),(30,30,'Emily Mitchell','2024-10-08 03:37:00','2024-10-08 12:31:36','2024-10-08','present'),(31,31,'Ethan Perez',NULL,NULL,'2024-10-08','absent');
/*!40000 ALTER TABLE `attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departments` (
  `department_id` int NOT NULL AUTO_INCREMENT,
  `department_name` varchar(50) NOT NULL,
  PRIMARY KEY (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES (1,'Human Resources'),(2,'Finance'),(3,'Marketing'),(4,'Sales'),(5,'IT'),(6,'Customer Service'),(7,'Research and Development'),(8,'Logistics'),(9,'Legal'),(10,'Bussiness Development'),(11,'Quality Assurance'),(12,'Administration'),(13,'Human Resources'),(14,'Finance'),(15,'Marketing'),(16,'Sales'),(17,'IT'),(18,'Customer Service'),(19,'Research and Development'),(20,'Logistics'),(21,'Legal'),(22,'Bussiness Development'),(23,'Quality Assurance'),(24,'Administration'),(25,'Human Resources'),(26,'Finance'),(27,'Marketing'),(28,'Sales'),(29,'IT'),(30,'Customer Service'),(31,'Research and Development'),(32,'Logistics'),(33,'Legal'),(34,'Business Development'),(35,'Quality Assurance'),(36,'Administration');
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `employee_id` int NOT NULL AUTO_INCREMENT,
  `employee_name` varchar(50) NOT NULL,
  `department_id` int DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `hire_date` date DEFAULT NULL,
  PRIMARY KEY (`employee_id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'John Smith',1,'john.smith@gmail.com','2021-01-15'),(2,'Sandra Sunil',12,'sand23@gmail.com','2023-05-08'),(3,'Malavika Menon',12,'mallu22@gmail.com','2022-02-04'),(4,'Aswathy Ritu',11,'aswao09@gmail.com','2017-06-07'),(5,'Arun p',5,'aru32@gmail.com','2018-09-26'),(6,'Richu narayanan',1,'richub@gmail.com','2024-01-05'),(7,'Olivia Garcia',6,'oliva33@gmail.com','2024-08-04'),(8,'Emily Davis',4,'emilyda54@gmail.com','2023-09-16'),(9,'Miriya Alexander',4,'miriyalexa32e@gmail.com','2023-12-28'),(10,'Benjamin Lee',4,'benjaa4356@gmail.com','2018-06-22'),(11,'Lina Satheesh',8,'linna43@gmail.com','2023-04-10'),(12,'Sophia Martinez',4,'sophiee45@gmail.com','2020-08-19'),(13,'Michael Johnson',3,'michael.johnson@gmail.com','2021-05-10'),(14,'William Brown',5,'william.brown@gmail.com','2022-03-18'),(15,'James Wilson',7,'james.wilson@gmail.com','2020-02-23'),(16,'Isabella Walker',10,'isabella.walker@gmail.com','2017-04-30'),(17,'Alexander Young',1,'alexander.young@gmail.com','2019-10-14'),(18,'Mia Harris',2,'mia.harris@gmail.com','2018-08-19'),(19,'Daniel Clark',3,'daniel.clark@gmail.com','2021-01-08'),(20,'Amelia Lewis',4,'amelia.lewis@gmail.com','2017-03-25'),(21,'Lucas King',5,'lucas.king@gmail.com','2020-07-09'),(22,'Charlotte Wright',6,'charlotte.wright@gmail.com','2021-09-17'),(23,'Liam Scott',7,'liam.scott@gmail.com','2019-12-01'),(24,'Ava Green',8,'ava.green@gmail.com','2022-04-11'),(25,'Mason Baker',9,'mason.baker@gmail.com','2020-06-03'),(26,'Harper Hill',10,'harper.hill@gmail.com','2018-01-30'),(27,'Elijah Adams',1,'elijah.adams@gmail.com','2017-09-21'),(28,'Abigail Nelson',2,'abigail.nelson@gmail.com','2021-11-27'),(29,'Jacob Carter',3,'jacob.carter@gmail.com','2020-03-13'),(30,'Emily Mitchell',4,'emily.mitchell@gmail.com','2019-05-29'),(31,'Ethan Perez',5,'ethan.perez@gmail.com','2018-02-16');
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-10 14:53:51
