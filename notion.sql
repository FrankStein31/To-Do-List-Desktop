/*
SQLyog Professional v13.1.1 (64 bit)
MySQL - 8.0.30 : Database - notion
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`notion` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `notion`;

/*Table structure for table `tasks` */

DROP TABLE IF EXISTS `tasks`;

CREATE TABLE `tasks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` text,
  `status` enum('Pending','In Progress','Completed') DEFAULT 'Pending',
  `priority` enum('Low','Medium','High') DEFAULT 'Medium',
  `type` enum('Personal','Team') DEFAULT 'Personal',
  `deadline` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `approval_status` enum('Pending','Approved','Rejected') DEFAULT 'Pending',
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `tasks_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `tasks` */

insert  into `tasks`(`id`,`user_id`,`title`,`description`,`status`,`priority`,`type`,`deadline`,`created_at`,`updated_at`,`approval_status`) values 
(2,1,'coba','tugas','Completed','Low','Team',NULL,'2024-12-09 15:42:24','2024-12-10 14:42:09','Approved'),
(3,1,'gghghg','tututuu','Completed','Medium','Personal',NULL,'2024-12-09 15:59:32','2024-12-10 14:42:34','Rejected'),
(5,1,'lagigii','lagiiii','Completed','Medium','Personal',NULL,'2024-12-09 16:13:08','2024-12-10 14:53:07','Approved'),
(6,1,'rerere','rerere','Completed','High','Personal',NULL,'2024-12-09 18:29:39','2024-12-10 14:53:29','Approved'),
(8,1,'tes','tes','Completed','Low','Personal','2024-12-10','2024-12-09 18:36:59','2024-12-10 15:03:23','Approved'),
(9,1,'tessssssssssssss','tessssssssssssss','In Progress','High','Team','2024-12-10','2024-12-09 19:45:24','2024-12-10 14:53:15','Approved'),
(10,1,'coba coab','coba coab','Completed','High','Personal','2024-12-10','2024-12-09 19:47:30','2024-12-10 14:53:11','Approved'),
(11,1,'aaaaaa','aaaaaaaaaaa','Completed','High','Personal','2024-12-11','2024-12-10 13:37:44','2024-12-10 14:52:41','Approved'),
(13,2,'tes lagi','tes','Pending','Low','Team','2024-12-10','2024-12-10 14:57:23','2024-12-10 14:57:53','Rejected'),
(14,2,'tesssssssssssss','ini lagi progress tentang edit filter','Completed','High','Team','2024-12-10','2024-12-10 15:05:59','2024-12-10 15:12:18','Approved'),
(15,2,'Jokian','Malam ini selesai','Pending','High','Personal','2024-12-10','2024-12-10 15:27:11','2024-12-10 15:27:11','Approved');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `full_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `users` */

insert  into `users`(`id`,`full_name`,`email`,`password`,`role`) values 
(1,'Frankie Steinlie','fs@gmail.com','ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f','Admin'),
(2,'coba','coba@gmail.com','5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5','Personal');

/*Table structure for table `workspace_members` */

DROP TABLE IF EXISTS `workspace_members`;

CREATE TABLE `workspace_members` (
  `workspace_id` int NOT NULL,
  `user_id` int NOT NULL,
  `role` enum('Owner','Admin','Member') DEFAULT 'Member',
  `joined_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`workspace_id`,`user_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `workspace_members_ibfk_1` FOREIGN KEY (`workspace_id`) REFERENCES `workspaces` (`id`) ON DELETE CASCADE,
  CONSTRAINT `workspace_members_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `workspace_members` */

/*Table structure for table `workspaces` */

DROP TABLE IF EXISTS `workspaces`;

CREATE TABLE `workspaces` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text,
  `created_by` int NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `created_by` (`created_by`),
  CONSTRAINT `workspaces_ibfk_1` FOREIGN KEY (`created_by`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `workspaces` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
