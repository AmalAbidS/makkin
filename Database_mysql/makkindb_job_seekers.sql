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
-- Table structure for table `job_seekers`
--

DROP TABLE IF EXISTS `job_seekers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_seekers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `education` varchar(255) DEFAULT NULL,
  `experience` int DEFAULT NULL,
  `skills` text,
  `resume_path` varchar(255) DEFAULT NULL,
  `national_id` varchar(10) DEFAULT NULL,
  `birthdate` date DEFAULT NULL,
  `marital_status` varchar(20) DEFAULT NULL,
  `employment_status` varchar(20) DEFAULT NULL,
  `major` varchar(100) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `role` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `national_id` (`national_id`),
  FULLTEXT KEY `education` (`education`,`skills`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_seekers`
--

LOCK TABLES `job_seekers` WRITE;
/*!40000 ALTER TABLE `job_seekers` DISABLE KEYS */;
INSERT INTO `job_seekers` VALUES (10,'Manar Almatrafi','manaralmatrafi@outlook.sa','m','بكالوريوس',1,'مبرمج,برمجة,الادارة',NULL,'1234567899','2002-02-12','single','unemployed','علوم الحاسب','female',NULL),(11,'أمل عبدالله','aml@gmail.com','1','بكالوريوس',1,'الحساب,كاشير,مبرمج,ادارة الوقت,مبيعات',NULL,'1234','2002-07-20','single','unemployed','نظم المعلومات','female',NULL),(12,'جود أحمد','joud@gmail.com','joud','بكالوريوس',3,'Illustrator,InDesign,التصميم',NULL,'1234567811','2002-02-12','single','unemployed','الفنون البصرية','female',NULL),(13,'سميه','so@gmail.com','so','بكالوريوس',1,'تعليم,مبرمج,برمجة,تقنية معلومات',NULL,'1234567890','2002-03-12','single','unemployed','نظم المعلومات','female',NULL),(14,'عبدالله الحربي','abdullah.alharbi@example.sa','pass123','بكالوريوس',3,'Network Administration, CCNA',NULL,'1045781261','1992-04-22','أعزب','يبحث عن عمل','هندسة الشبكات','ذكر',NULL),(15,'نورة السبيعي','nora.alsubaie@example.sa','pass123','ماجستير',4,'Digital Marketing, SEO',NULL,'1045781262','1991-07-15','متزوجة','يبحث عن عمل','التسويق','أنثى',NULL),(16,'محمد الفهيد','mohammad.alfahid@example.sa','pass123','بكالوريوس',2,'Graphic Design, Adobe Photoshop',NULL,'1045781263','1993-09-10','أعزب','يبحث عن عمل','تصميم الجرافيك','ذكر',NULL),(17,'ريم الناصر','reem.alnaser@example.sa','pass123','بكالوريوس',5,'Human Resources, Talent Acquisition',NULL,'1045781264','1990-01-25','متزوجة','يبحث عن عمل','الموارد البشرية','أنثى',NULL),(18,'تركي المالكي','turki.almalki@example.sa','pass123','ماجستير',6,'Financial Analysis, Excel',NULL,'1045781265','1989-12-05','متزوج','يبحث عن عمل','المالية','ذكر',NULL),(19,'سارة الغامدي','sarah.alghamdi@example.sa','pass123','بكالوريوس',3,'Software Development, Java',NULL,'1045781266','1992-03-16','أعزب','يبحث عن عمل','علوم الحاسب','أنثى',NULL),(20,'خالد الجهني','khaled.aljohani@example.sa','pass123','بكالوريوس',4,'Marketing Strategy, Social Media',NULL,'1045781267','1990-11-18','متزوج','يبحث عن عمل','التسويق','ذكر',NULL),(21,'هدى القرني','huda.alqarni@example.sa','pass123','ماجستير',2,'Project Management, Agile',NULL,'1045781268','1991-05-12','متزوجة','يبحث عن عمل','إدارة الأعمال','أنثى',NULL),(22,'فيصل الدوسري','faisal.aldosari@example.sa','pass123','بكالوريوس',3,'Data Analysis, Python',NULL,'1045781269','1990-08-07','متزوج','يبحث عن عمل','علوم البيانات','ذكر',NULL),(23,'نجود الشهراني','nujood.alshahrani@example.sa','pass123','بكالوريوس',2,'Public Relations, Communication',NULL,'1045781270','1992-06-28','أعزب','يبحث عن عمل','العلاقات العامة','أنثى',NULL),(24,'عبدالرحمن العمري','abdulrahman.alomari@example.sa','pass123','بكالوريوس',4,'Supply Chain Management, Logistics',NULL,'1045781271','1989-10-09','متزوج','يبحث عن عمل','إدارة سلسلة الإمداد','ذكر',NULL),(25,'زينب الشهري','zainab.alshahri@example.sa','pass123','ماجستير',3,'Clinical Psychology, Counseling',NULL,'1045781272','1990-05-30','متزوجة','يبحث عن عمل','علم النفس','أنثى',NULL),(26,'فهد البقمي','fahad.albogami@example.sa','pass123','بكالوريوس',2,'Mechanical Engineering, CAD',NULL,'1045781273','1991-12-20','أعزب','يبحث عن عمل','الهندسة الميكانيكية','ذكر',NULL),(27,'سلمى الزهراني','salma.alzahrani@example.sa','pass123','بكالوريوس',3,'Teaching, Curriculum Design',NULL,'1045781274','1992-02-15','متزوجة','يبحث عن عمل','التعليم','أنثى',NULL),(28,'علي الزهراني','ali.alzahrani@example.sa','pass123','ماجستير',5,'Software Engineering, C++',NULL,'1045781275','1989-03-19','متزوج','يبحث عن عمل','هندسة البرمجيات','ذكر',NULL),(29,'نادية المقرن','nadia.almogren@example.sa','pass123','بكالوريوس',2,'Event Management, Coordination',NULL,'1045781276','1993-09-25','أعزب','يبحث عن عمل','إدارة الفعاليات','أنثى',NULL),(30,'ياسر المطيري','yasser.almutairi@example.sa','pass123','بكالوريوس',4,'Cybersecurity, Network Security',NULL,'1045781277','1990-04-14','متزوج','يبحث عن عمل','أمن المعلومات','ذكر',NULL);
/*!40000 ALTER TABLE `job_seekers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-14 18:24:17
