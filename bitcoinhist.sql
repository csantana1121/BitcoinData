-- MariaDB dump 10.17  Distrib 10.4.8-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: bitcoin
-- ------------------------------------------------------
-- Server version	10.4.8-MariaDB-1:10.4.8+maria~bionic-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Hist_Price_Index`
--

DROP TABLE IF EXISTS `Hist_Price_Index`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Hist_Price_Index` (
  `Day` text DEFAULT NULL,
  `USD` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Hist_Price_Index`
--

LOCK TABLES `Hist_Price_Index` WRITE;
/*!40000 ALTER TABLE `Hist_Price_Index` DISABLE KEYS */;
INSERT INTO `Hist_Price_Index` VALUES ('2021-06-01',36681.7417),('2021-06-02',37583.65),('2021-06-03',39232.6517),('2021-06-04',36851.8417),('2021-06-05',35534.9267),('2021-06-06',35801.1317),('2021-06-07',33580.7767),('2021-06-08',33406.4817),('2021-06-09',37383.66),('2021-06-10',36683.9167),('2021-06-11',37338.0367),('2021-06-12',35545.9817),('2021-06-13',39018.0383),('2021-06-14',40518.6883),('2021-06-15',40160.7267),('2021-06-16',38344.7233),('2021-06-17',38087.2533),('2021-06-18',35814.6417),('2021-06-19',35519.7117),('2021-06-20',35605.68),('2021-06-21',31651.5733),('2021-06-22',32538.255),('2021-06-23',33690.375),('2021-06-24',34657.9733),('2021-06-25',31586.9033),('2021-06-26',32308.725),('2021-06-27',34708.96),('2021-06-28',34497.755),('2021-06-29',35918.88),('2021-06-30',35053.4183),('2021-07-01',33524.9833);
/*!40000 ALTER TABLE `Hist_Price_Index` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Price_Index`
--

DROP TABLE IF EXISTS `Price_Index`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Price_Index` (
  `Date` text DEFAULT NULL,
  `USD` text DEFAULT NULL,
  `EURO` text DEFAULT NULL,
  `GBP` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Price_Index`
--

LOCK TABLES `Price_Index` WRITE;
/*!40000 ALTER TABLE `Price_Index` DISABLE KEYS */;
INSERT INTO `Price_Index` VALUES ('Jul 1, 2021 18:40:00 UTC','33,546.2033','28,315.7129','24,374.5036'),('Jul 1, 2021 18:45:00 UTC','33,550.4033','28,319.2580','24,377.5553'),('Jul 1, 2021 18:54:00 UTC','33,498.1017','28,275.1112','24,339.5532'),('Jul 1, 2021 19:02:00 UTC','33,317.3370','28,122.5311','24,208.2105'),('Jul 1, 2021 19:03:00 UTC','33,266.4927','28,079.6144','24,171.2672'),('Jul 1, 2021 19:24:00 UTC','32,935.2297','27,813.4392','23,943.4509'),('Jul 1, 2021 19:39:00 UTC','32,921.4183','27,801.7756','23,933.4102'),('Jul 1, 2021 19:56:00 UTC','33,076.8529','27,933.0384','24,046.4090'),('Jul 1, 2021 19:57:00 UTC','33,090.9100','27,944.9095','24,056.6283'),('Jul 1, 2021 19:58:00 UTC','33,122.7083','27,971.7628','24,079.7452'),('Jul 1, 2021 20:15:00 UTC','33,193.7160','28,018.1850','24,127.1181'),('Jul 1, 2021 20:19:00 UTC','33,217.2517','28,038.0510','24,144.2251'),('Jul 1, 2021 20:23:00 UTC','33,259.6424','28,073.8322','24,175.0372'),('Jul 1, 2021 20:24:00 UTC','33,269.4461','28,082.1073','24,182.1630'),('Jul 1, 2021 20:27:00 UTC','33,258.4983','28,072.8665','24,174.2056'),('Jul 1, 2021 20:28:00 UTC','33,313.5083','28,119.2994','24,214.1900'),('Jul 1, 2021 20:28:00 UTC','33,323.6030','28,127.8201','24,221.5274'),('Jul 1, 2021 20:29:00 UTC','33,316.9050','28,122.1665','24,216.6589'),('Jul 1, 2021 20:30:00 UTC','33,297.3786','28,105.6846','24,202.4660'),('Jul 1, 2021 20:37:00 UTC','33,405.2144','28,196.7068','24,280.8474'),('Jul 1, 2021 20:38:00 UTC','33,382.4350','28,177.4791','24,264.2899'),('Jul 1, 2021 21:23:00 UTC','33,566.0100','28,325.0803','24,389.5328'),('Jul 2, 2021 16:05:00 UTC','33,625.8583','28,383.4189','24,379.9242');
/*!40000 ALTER TABLE `Price_Index` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-02 16:05:33