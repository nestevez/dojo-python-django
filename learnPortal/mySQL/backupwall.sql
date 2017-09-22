-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: thewall
-- ------------------------------------------------------
-- Server version	5.7.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message_id` int(11) NOT NULL,
  `comment` text,
  `from_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `modified_at` datetime DEFAULT NULL,
  `to_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comments_messages1_idx` (`message_id`),
  KEY `fk_comments_users1_idx` (`from_id`),
  KEY `fk_comments_users2_idx` (`to_id`),
  CONSTRAINT `fk_comments_messages1` FOREIGN KEY (`message_id`) REFERENCES `messages` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`from_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users2` FOREIGN KEY (`to_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 COMMENT='		';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (1,2,'What it doooo',9,'2017-09-15 00:44:37','2017-09-15 00:44:37',8),(2,3,'bbbrrrrr waaassaaaaaaaaa',9,'2017-09-15 00:47:36','2017-09-15 00:47:36',8),(3,4,'suuup',9,'2017-09-15 13:04:04','2017-09-15 13:04:04',8),(4,2,'huh??',8,'2017-09-15 14:32:29','2017-09-15 14:32:29',8),(5,3,'omg',8,'2017-09-15 14:33:57','2017-09-15 14:33:57',8),(6,4,'does it really work???',8,'2017-09-15 14:34:07','2017-09-15 14:34:07',8),(7,5,'does this work?',8,'2017-09-15 14:53:28','2017-09-15 14:53:28',9),(8,5,'UHOH',10,'2017-09-15 14:55:56','2017-09-15 14:55:56',9),(9,6,'COMMETNdw;gjsef;ag',10,'2017-09-15 14:56:04','2017-09-15 14:56:04',9),(10,3,'GO HOME',10,'2017-09-15 14:56:30','2017-09-15 14:56:30',8),(11,8,'THIS IS ALSO A TEST',11,'2017-09-15 15:05:08','2017-09-15 15:05:08',10),(12,6,'HALLO',11,'2017-09-15 15:05:30','2017-09-15 15:05:30',9),(13,10,'this be cray',8,'2017-09-15 15:23:00','2017-09-15 15:23:00',11),(14,11,'so weird',8,'2017-09-15 15:23:07','2017-09-15 15:23:07',11);
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` text,
  `from_id` int(11) NOT NULL,
  `to_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `modified_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_users_idx` (`from_id`),
  KEY `fk_messages_users1_idx` (`to_id`),
  CONSTRAINT `fk_messages_users` FOREIGN KEY (`from_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_messages_users1` FOREIGN KEY (`to_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (2,'Aloha~',9,8,'2017-09-15 00:00:36','2017-09-15 00:00:36'),(3,'WHATAAA',9,8,'2017-09-15 00:13:17','2017-09-15 00:13:17'),(4,'wassaaaa',9,8,'2017-09-15 13:03:54','2017-09-15 13:03:54'),(5,'aloha to you too',8,9,'2017-09-15 14:53:20','2017-09-15 14:53:20'),(6,'WHAT UP',10,9,'2017-09-15 14:55:48','2017-09-15 14:55:48'),(7,'NO',10,8,'2017-09-15 14:56:21','2017-09-15 14:56:21'),(8,'THIS IS A TEST',11,10,'2017-09-15 15:04:56','2017-09-15 15:04:56'),(9,'NOPE',11,8,'2017-09-15 15:05:43','2017-09-15 15:05:43'),(10,'WUUUUUUUUUUUUUUUUUUUUUT',8,11,'2017-09-15 15:20:25','2017-09-15 15:20:25'),(11,'WUUUUUUUUUUUUUUUUUUUUUT',8,11,'2017-09-15 15:22:52','2017-09-15 15:22:52'),(12,'No\r\n\r\n\r\n\r\n\r\nDid I break it?\r\n\r\n\r\n\r\n\r\n\r\n\r\nHow big a messge can i do\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\nWhat goes here?\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\nHow is the functionality?\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\nhello world\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\nnow what?\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\ndoes this still work?\r\n\r\n\r\n\r\n\r\n\r\n\r\nk\r\n',12,8,'2017-09-15 15:56:23','2017-09-15 15:56:23'),(13,'WASAAAAAAAAAAAAAAAAAAAAAA',8,12,'2017-09-15 15:59:57','2017-09-15 15:59:57');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `salt` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `modified_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (8,'Natalia','Estevez','natalia.estevez3@gmail.com','nestevez','cdcbf533d0f17d4d3abcdb83b29a1684','d62c4dde5fd2a14bc51eea2c996014','2017-09-14 23:11:43','2017-09-14 23:11:43'),(9,'Fulano','Detal','fulano@detal.com','fdetal','d1f8532c217415150940b8630ccd9ddd','f09a2ef823dc35ecee25350c1ba3f5','2017-09-14 23:54:54','2017-09-14 23:54:54'),(10,'Ari','Wolpin','ariwolpin@gmail.com','ariwolpin','962ef77b1d6df5f8639684578d35a89d','4580f17ca9b990c3391f7a41a8f542','2017-09-15 14:55:29','2017-09-15 14:55:29'),(11,'Test','Case','test@case.com','testcase','cb88fbe051156267924e1d3e9fbb13c0','c1285abee7ce195822d2bcd3fcf4e6','2017-09-15 15:04:29','2017-09-15 15:04:29'),(12,'Nathan','Valmonster','valmonten@gmail.com','valmonten','4f1f331af32c9982646bd3308b7b5821','2f5f89b1c7f9cf7c414ff3170529f7','2017-09-15 15:52:34','2017-09-15 15:52:34');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-09-15 17:04:25
