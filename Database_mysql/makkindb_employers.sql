-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: makkindb
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `employers`
--

DROP TABLE IF EXISTS `employers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `contact_number` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employers`
--

LOCK TABLES `employers` WRITE;
/*!40000 ALTER TABLE `employers` DISABLE KEYS */;
INSERT INTO `employers` VALUES (1,'Manar Almatrafi','m3@gmail.com','3','umm al-qura university','0531394647'),(2,'دانيا','d@gmail.com','d','umm al-qura university','0531394643'),(3,'شهد ','shahad@gmail.com','1','شركة شهد ','0501339934'),(4,'محمد ','muhammad@gmail.com','1','السعوديه للخدمات المحدوده','050000111'),(5,'احمد','ahmad@gmail.com','a','شركة أحمد نجيب المحدودة ','0531394642'),(6,'محمود ','m@gmail.com','m','شركة الرؤية الأولى لتقنية المعلومات','0531394642'),(7,'صالح','s@gmail.com','s','صالح للمحاماة','0531394644'),(8,'سارة','sara@gmail.com','s','افاق التربية','0531394645'),(9,'شركة التقنيات المتقدمة','hr@advtech.com.sa','adv123','التقنيات المتقدمة','0123456789'),(10,'المؤسسة السعودية للتطوير','jobs@soudv.sa','soud123','المؤسسة السعودية للتطوير','0123456790'),(11,'مؤسسة الرؤية المستقبلية','contact@futurevision.sa','fv123','الرؤية المستقبلية','0123456791'),(12,'شركة الحلول المتكاملة','recruit@intsol.sa','ints123','الحلول المتكاملة','0123456792'),(13,'مجموعة الأعمال العالمية','apply@giglobal.sa','gig123','الأعمال العالمية','0123456793'),(14,'شركة المشاريع الرائدة','careers@projleaders.sa','proj123','المشاريع الرائدة','0123456794'),(15,'شركة الإبداع والابتكار','joinus@creainnov.sa','ci123','الإبداع والابتكار','0123456795'),(16,'مؤسسة التطور الرقمي','hr@digitalevo.sa','devo123','التطور الرقمي','0123456796'),(17,'شركة تكنولوجيا التعليم','hr@edtech.sa','edtech123','تكنولوجيا التعليم','0123456797'),(18,'شركة الجودة والتميز','jobs@qualityexcellence.sa','qe123','الجودة والتميز','0123456798'),(19,'شركة الاتصالات السعودية','hr@stc.sa','stc123','الاتصالات السعودية','0123456799'),(20,'شركة المياه الوطنية','jobs@ncw.sa','ncw123','المياه الوطنية','0123456700'),(21,'مجموعة الزامل','careers@zamil.com','zamil123','مجموعة الزامل','0123456701'),(22,'شركة معادن','recruit@maaden.com.sa','maaden123','معادن','0123456702'),(23,'شركة الكهرباء السعودية','apply@sec.com.sa','sec123','الكهرباء السعودية','0123456703'),(24,'شركة النفط السعودية','careers@soc.com.sa','soc123','النفط السعودية','0123456704'),(25,'شركة بترو رابغ','jobs@petroRabigh.com','pr123','بترو رابغ','0123456705'),(26,'مجموعة سابك','recruit@sabic.com','sabic123','سابك','0123456706'),(27,'شركة أرامكو السعودية','hr@aramco.com.sa','aramco123','أرامكو السعودية','0123456707'),(28,'شركة الاتصالات المتكاملة','jobs@integratedcom.sa','ic123','الاتصالات المتكاملة','0123456708');
/*!40000 ALTER TABLE `employers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-14 18:24:18
