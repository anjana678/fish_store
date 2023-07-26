/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - django_fish_stores
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`django_fish_stores` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `django_fish_stores`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add booking',7,'add_booking'),
(26,'Can change booking',7,'change_booking'),
(27,'Can delete booking',7,'delete_booking'),
(28,'Can view booking',7,'view_booking'),
(29,'Can add category',8,'add_category'),
(30,'Can change category',8,'change_category'),
(31,'Can delete category',8,'delete_category'),
(32,'Can view category',8,'view_category'),
(33,'Can add customerr',9,'add_customerr'),
(34,'Can change customerr',9,'change_customerr'),
(35,'Can delete customerr',9,'delete_customerr'),
(36,'Can view customerr',9,'view_customerr'),
(37,'Can add loginn',10,'add_loginn'),
(38,'Can change loginn',10,'change_loginn'),
(39,'Can delete loginn',10,'delete_loginn'),
(40,'Can view loginn',10,'view_loginn'),
(41,'Can add product',11,'add_product'),
(42,'Can change product',11,'change_product'),
(43,'Can delete product',11,'delete_product'),
(44,'Can view product',11,'view_product'),
(45,'Can add sellerr',12,'add_sellerr'),
(46,'Can change sellerr',12,'change_sellerr'),
(47,'Can delete sellerr',12,'delete_sellerr'),
(48,'Can view sellerr',12,'view_sellerr'),
(49,'Can add services',13,'add_services'),
(50,'Can change services',13,'change_services'),
(51,'Can delete services',13,'delete_services'),
(52,'Can view services',13,'view_services'),
(53,'Can add wishlist',14,'add_wishlist'),
(54,'Can change wishlist',14,'change_wishlist'),
(55,'Can delete wishlist',14,'delete_wishlist'),
(56,'Can view wishlist',14,'view_wishlist'),
(57,'Can add subcategory',15,'add_subcategory'),
(58,'Can change subcategory',15,'change_subcategory'),
(59,'Can delete subcategory',15,'delete_subcategory'),
(60,'Can view subcategory',15,'view_subcategory'),
(61,'Can add staff',16,'add_staff'),
(62,'Can change staff',16,'change_staff'),
(63,'Can delete staff',16,'delete_staff'),
(64,'Can view staff',16,'view_staff'),
(65,'Can add srequest',17,'add_srequest'),
(66,'Can change srequest',17,'change_srequest'),
(67,'Can delete srequest',17,'delete_srequest'),
(68,'Can view srequest',17,'view_srequest'),
(69,'Can add req_payment',18,'add_req_payment'),
(70,'Can change req_payment',18,'change_req_payment'),
(71,'Can delete req_payment',18,'delete_req_payment'),
(72,'Can view req_payment',18,'view_req_payment'),
(73,'Can add payment',19,'add_payment'),
(74,'Can change payment',19,'change_payment'),
(75,'Can delete payment',19,'delete_payment'),
(76,'Can view payment',19,'view_payment'),
(77,'Can add feedback',20,'add_feedback'),
(78,'Can change feedback',20,'change_feedback'),
(79,'Can delete feedback',20,'delete_feedback'),
(80,'Can view feedback',20,'view_feedback'),
(81,'Can add bchild',21,'add_bchild'),
(82,'Can change bchild',21,'change_bchild'),
(83,'Can delete bchild',21,'delete_bchild'),
(84,'Can view bchild',21,'view_bchild'),
(85,'Can add assign_staff_req',22,'add_assign_staff_req'),
(86,'Can change assign_staff_req',22,'change_assign_staff_req'),
(87,'Can delete assign_staff_req',22,'delete_assign_staff_req'),
(88,'Can view assign_staff_req',22,'view_assign_staff_req'),
(89,'Can add assign_staff_book',23,'add_assign_staff_book'),
(90,'Can change assign_staff_book',23,'change_assign_staff_book'),
(91,'Can delete assign_staff_book',23,'delete_assign_staff_book'),
(92,'Can view assign_staff_book',23,'view_assign_staff_book'),
(93,'Can add captcha store',24,'add_captchastore'),
(94,'Can change captcha store',24,'change_captchastore'),
(95,'Can delete captcha store',24,'delete_captchastore'),
(96,'Can view captcha store',24,'view_captchastore'),
(97,'Can add review',25,'add_review'),
(98,'Can change review',25,'change_review'),
(99,'Can delete review',25,'delete_review'),
(100,'Can view review',25,'view_review'),
(101,'Can add feedbacks',20,'add_feedbacks'),
(102,'Can change feedbacks',20,'change_feedbacks'),
(103,'Can delete feedbacks',20,'delete_feedbacks'),
(104,'Can view feedbacks',20,'view_feedbacks'),
(105,'Can add sfeedback',26,'add_sfeedback'),
(106,'Can change sfeedback',26,'change_sfeedback'),
(107,'Can delete sfeedback',26,'delete_sfeedback'),
(108,'Can view sfeedback',26,'view_sfeedback'),
(109,'Can add sreview',27,'add_sreview'),
(110,'Can change sreview',27,'change_sreview'),
(111,'Can delete sreview',27,'delete_sreview'),
(112,'Can view sreview',27,'view_sreview');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `captcha_captchastore` */

DROP TABLE IF EXISTS `captcha_captchastore`;

CREATE TABLE `captcha_captchastore` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `challenge` varchar(32) NOT NULL,
  `response` varchar(32) NOT NULL,
  `hashkey` varchar(40) NOT NULL,
  `expiration` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hashkey` (`hashkey`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `captcha_captchastore` */

insert  into `captcha_captchastore`(`id`,`challenge`,`response`,`hashkey`,`expiration`) values 
(6,'VHQA','vhqa','03b14c9252e71e96217765b31b811fe6816a178e','2023-04-09 05:21:31.214545'),
(7,'ZWWQ','zwwq','b24af07c830765f9de8488bef3f64dadcaf07c15','2023-04-09 05:21:50.003775'),
(8,'FCNT','fcnt','83882278f7682912362d33a54cf22c5477f9cf87','2023-04-09 05:22:18.976210'),
(9,'SUEY','suey','63a7c1f6507ae657d05b516e08e339d170b1a239','2023-04-09 05:22:43.571181');

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(24,'captcha','captchastore'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(23,'store','assign_staff_book'),
(22,'store','assign_staff_req'),
(21,'store','bchild'),
(7,'store','booking'),
(8,'store','category'),
(9,'store','customerr'),
(20,'store','feedbacks'),
(10,'store','loginn'),
(19,'store','payment'),
(11,'store','product'),
(18,'store','req_payment'),
(25,'store','review'),
(12,'store','sellerr'),
(13,'store','services'),
(26,'store','sfeedback'),
(17,'store','srequest'),
(27,'store','sreview'),
(16,'store','staff'),
(15,'store','subcategory'),
(14,'store','wishlist');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-03-11 15:54:28.223323'),
(2,'auth','0001_initial','2023-03-11 15:54:28.803050'),
(3,'admin','0001_initial','2023-03-11 15:54:28.941680'),
(4,'admin','0002_logentry_remove_auto_add','2023-03-11 15:54:28.958722'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-03-11 15:54:28.977591'),
(6,'contenttypes','0002_remove_content_type_name','2023-03-11 15:54:29.091723'),
(7,'auth','0002_alter_permission_name_max_length','2023-03-11 15:54:29.151561'),
(8,'auth','0003_alter_user_email_max_length','2023-03-11 15:54:29.218385'),
(9,'auth','0004_alter_user_username_opts','2023-03-11 15:54:29.250296'),
(10,'auth','0005_alter_user_last_login_null','2023-03-11 15:54:29.369497'),
(11,'auth','0006_require_contenttypes_0002','2023-03-11 15:54:29.375481'),
(12,'auth','0007_alter_validators_add_error_messages','2023-03-11 15:54:29.397423'),
(13,'auth','0008_alter_user_username_max_length','2023-03-11 15:54:29.444881'),
(14,'auth','0009_alter_user_last_name_max_length','2023-03-11 15:54:29.495752'),
(15,'auth','0010_alter_group_name_max_length','2023-03-11 15:54:29.543619'),
(16,'auth','0011_update_proxy_permissions','2023-03-11 15:54:29.568553'),
(17,'auth','0012_alter_user_first_name_max_length','2023-03-11 15:54:29.613947'),
(18,'captcha','0001_initial','2023-03-11 15:54:29.675075'),
(19,'captcha','0002_alter_captchastore_id','2023-03-11 15:54:29.684308'),
(20,'sessions','0001_initial','2023-03-11 15:54:29.806975'),
(21,'store','0001_initial','2023-03-11 15:54:31.836847'),
(22,'store','0002_review','2023-03-13 16:33:19.963227'),
(23,'store','0003_rename_feedback_feedbacks','2023-04-04 15:45:23.798566'),
(24,'store','0003_feedbacks','2023-04-04 16:41:40.321763'),
(25,'store','0004_sfeedback_sreview','2023-04-09 03:19:59.286254');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('1n6kmjgfm1mkkob41ej4mw1itz69txra','eyJsb2dpbl9pZCI6NH0:1pc451:sdCX2GlsAmFRfmg9gBS7gO2RDv1lmqYNXmy-OzbYm-k','2023-03-28 12:48:39.022850'),
('1r88ytll9z0ux2yq7wgpvtqzq6zyah7k','eyJsb2dpbl9pZCI6NH0:1pbci3:euWmlYQfIQdaHp6uhTp0TIaPzOj7h9qShx9NagY4ARE','2023-03-27 07:35:07.247848'),
('2hbquw9dcs7nce7ely76om64zyuv91qb','eyJsb2dpbl9pZCI6MX0:1pkRyl:e6kst-QEQPcwnJbG9Mtnuy4tnmJB_T3hhpnGfv58AGY','2023-04-20 15:56:51.303555'),
('5uokb2xwqinf40lmwzsievednthy129g','eyJsb2dpbl9pZCI6MX0:1pb4KB:s5kOJE517l7TMOIPAbdQKojLBx4lSQqqiGR0KhY3GwI','2023-03-25 18:52:11.279960'),
('774l96odct186ozmacp3fs87z9xslp0k','eyJsb2dpbl9pZCI6MX0:1pb3eJ:gisAOKRFLsZlczI0MfO8ZHCNDrSfDDFV_bqXhgSCgyM','2023-03-25 18:08:55.467627'),
('7bz7m46izwqizyw54vmn8aqscewg1yac','eyJsb2dpbl9pZCI6M30:1pc7EQ:YKF-TFGGHVMqrsxRD5ZfAya9ReNCnKLWu5N6BIQyMn4','2023-03-28 16:10:34.126004'),
('g2denvpmeh5jsw37nsxm9jt9ueufjaw3','eyJsb2dpbl9pZCI6NH0:1pjx5A:2avNA4nXVQbb4FdvKk8XsMdjwGn-rkAVzxrQMlDZxMc','2023-04-19 06:57:24.232166'),
('h1qo65lsdlzuyj6s5qfytxbjscrxo5d1','eyJsb2dpbl9pZCI6MX0:1plNU8:tary400CJqW95vQF8XHH9W-UHOwbBlQQkmkh5kHOBbQ','2023-04-23 05:21:04.388571'),
('hpsfydh5id29t6qjqt8o9waxjjlgybd5','eyJsb2dpbl9pZCI6NH0:1pblcR:a4cejD_Zn0m1VPwTHlDB33S2gtRWU9oV-4ICI6zzxKM','2023-03-27 17:05:55.321124'),
('md7svlhnxzihux3fkn9a060nzyqk8boi','eyJsb2dpbl9pZCI6NH0:1pc7J1:y9RB0xK2T1-4Y5SNFg3oKj50jAgLyM53R8TkJbDkfiM','2023-03-28 16:15:19.450988'),
('ravdbmc9xleu6ogd7cc4813l3n03yx8q','eyJsb2dpbl9pZCI6NH0:1pbJNw:9WlAp3KjDv6uo9f3H9gAAz0NFjNPk-KQNmf5xtmQ4_A','2023-03-26 10:57:04.823743'),
('snxv72p4izg6wguyy54bei4grexhw25b','eyJsb2dpbl9pZCI6NH0:1pbwGd:6qKVEYo8ogfYS3uzr9mcgkHTNpooliOs6_cYIheviHg','2023-03-28 04:28:07.636926'),
('u2ebm4ojp1rzsnubkk79dafe85mvpsjb','eyJsb2dpbl9pZCI6MX0:1pbItH:cnk_oVWkcr8Oh9_ry7rW3RtkmiPTB3NMP1UIYp-TRKk','2023-03-26 10:25:23.028704'),
('wubqd9j4uembtefwkfebfmgz19og7dg8','eyJsb2dpbl9pZCI6NH0:1pbfbK:xx9tvBG659EpRCkxGki6hC4Dbp5TiGSX7aObhQyoRaU','2023-03-27 10:40:22.752120'),
('ydqwo1wp0ji4k446v9nare9u7dp96h6x','eyJsb2dpbl9pZCI6M30:1pblZ7:5jck0a_DandGbpo-Ppbyk2vDCwhSTGxTA_3XvnAGCig','2023-03-27 17:02:29.033740'),
('yx68t95c8oov5pgt739ri6zl5wycf14x','eyJsb2dpbl9pZCI6NH0:1pcfOb:NrbAlfWP-WjsLqiGD6Q6C61rPBSU9WeJctbgYhRCy00','2023-03-30 04:39:21.833551');

/*Table structure for table `store_assign_staff_book` */

DROP TABLE IF EXISTS `store_assign_staff_book`;

CREATE TABLE `store_assign_staff_book` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` varchar(225) NOT NULL,
  `status` varchar(225) NOT NULL,
  `booking_id` bigint(20) NOT NULL,
  `staff_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_assign_staff_book_booking_id_92bcee73_fk_store_booking_id` (`booking_id`),
  KEY `store_assign_staff_book_staff_id_bb646d3d_fk_store_staff_id` (`staff_id`),
  CONSTRAINT `store_assign_staff_book_booking_id_92bcee73_fk_store_booking_id` FOREIGN KEY (`booking_id`) REFERENCES `store_booking` (`id`),
  CONSTRAINT `store_assign_staff_book_staff_id_bb646d3d_fk_store_staff_id` FOREIGN KEY (`staff_id`) REFERENCES `store_staff` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `store_assign_staff_book` */

insert  into `store_assign_staff_book`(`id`,`date`,`status`,`booking_id`,`staff_id`) values 
(1,'2023-03-13','assigned',1,1);

/*Table structure for table `store_assign_staff_req` */

DROP TABLE IF EXISTS `store_assign_staff_req`;

CREATE TABLE `store_assign_staff_req` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` varchar(225) NOT NULL,
  `status` varchar(225) NOT NULL,
  `srequest_id` bigint(20) NOT NULL,
  `staff_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_assign_staff_req_srequest_id_186f5842_fk_store_srequest_id` (`srequest_id`),
  KEY `store_assign_staff_req_staff_id_4dc45942_fk_store_staff_id` (`staff_id`),
  CONSTRAINT `store_assign_staff_req_srequest_id_186f5842_fk_store_srequest_id` FOREIGN KEY (`srequest_id`) REFERENCES `store_srequest` (`id`),
  CONSTRAINT `store_assign_staff_req_staff_id_4dc45942_fk_store_staff_id` FOREIGN KEY (`staff_id`) REFERENCES `store_staff` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `store_assign_staff_req` */

insert  into `store_assign_staff_req`(`id`,`date`,`status`,`srequest_id`,`staff_id`) values 
(1,'2023-03-13','assigned',1,2),
(2,'2023-04-04','assigned',1,1);

/*Table structure for table `store_bchild` */

DROP TABLE IF EXISTS `store_bchild`;

CREATE TABLE `store_bchild` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `qty` varchar(225) NOT NULL,
  `bamt` varchar(225) NOT NULL,
  `booking_id` bigint(20) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_bchild_booking_id_aadaa458_fk_store_booking_id` (`booking_id`),
  KEY `store_bchild_product_id_17642391_fk_store_product_id` (`product_id`),
  CONSTRAINT `store_bchild_booking_id_aadaa458_fk_store_booking_id` FOREIGN KEY (`booking_id`) REFERENCES `store_booking` (`id`),
  CONSTRAINT `store_bchild_product_id_17642391_fk_store_product_id` FOREIGN KEY (`product_id`) REFERENCES `store_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

/*Data for the table `store_bchild` */

insert  into `store_bchild`(`id`,`qty`,`bamt`,`booking_id`,`product_id`) values 
(1,'10','2500',1,4),
(3,'5','1000',2,1),
(4,'6','300',1,3),
(5,'1','500',2,2),
(16,'2','400',8,1),
(22,'3','1500',14,2),
(23,'6','300',15,3),
(24,'10','2000',14,1),
(25,'6','1200',16,1),
(26,'6','3000',15,2);

/*Table structure for table `store_booking` */

DROP TABLE IF EXISTS `store_booking`;

CREATE TABLE `store_booking` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `total` varchar(225) NOT NULL,
  `date` varchar(225) NOT NULL,
  `status` varchar(225) NOT NULL,
  `order_id` varchar(225) NOT NULL,
  `customerr_id` bigint(20) NOT NULL,
  `seller_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_booking_customerr_id_ed7ce0f8_fk_store_customerr_id` (`customerr_id`),
  KEY `store_booking_seller_id_a2e8a30c_fk_store_sellerr_id` (`seller_id`),
  CONSTRAINT `store_booking_customerr_id_ed7ce0f8_fk_store_customerr_id` FOREIGN KEY (`customerr_id`) REFERENCES `store_customerr` (`id`),
  CONSTRAINT `store_booking_seller_id_a2e8a30c_fk_store_sellerr_id` FOREIGN KEY (`seller_id`) REFERENCES `store_sellerr` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `store_booking` */

insert  into `store_booking`(`id`,`total`,`date`,`status`,`order_id`,`customerr_id`,`seller_id`) values 
(1,'2800.0','2023-03-12','delivered','',1,2),
(2,'1500','2023-03-12','delivered','',1,1),
(8,'400','2023-03-13','paid','',1,1),
(14,'3500.0','2023-03-13','paid','',1,1),
(15,'3300.0','2023-03-14','paid','',1,2),
(16,'1200','2023-04-03','pending','',1,1);

/*Table structure for table `store_category` */

DROP TABLE IF EXISTS `store_category`;

CREATE TABLE `store_category` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `category` varchar(225) NOT NULL,
  `castatus` varchar(225) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `store_category` */

insert  into `store_category`(`id`,`category`,`castatus`) values 
(2,'Fishes','active'),
(3,'Plants','active'),
(4,'Accessories','deactive'),
(7,'DDD','deactive'),
(8,'HII','deactive');

/*Table structure for table `store_customerr` */

DROP TABLE IF EXISTS `store_customerr`;

CREATE TABLE `store_customerr` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fname` varchar(225) NOT NULL,
  `lname` varchar(225) NOT NULL,
  `place` varchar(225) NOT NULL,
  `phone` varchar(225) NOT NULL,
  `email` varchar(225) NOT NULL,
  `address` varchar(225) NOT NULL,
  `login_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_customerr_login_id_6bb3bd98_fk_store_loginn_id` (`login_id`),
  CONSTRAINT `store_customerr_login_id_6bb3bd98_fk_store_loginn_id` FOREIGN KEY (`login_id`) REFERENCES `store_loginn` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `store_customerr` */

insert  into `store_customerr`(`id`,`fname`,`lname`,`place`,`phone`,`email`,`address`,`login_id`) values 
(1,'Sherin','Babu','Manimala','6282589076','aleenatresa8@gmail.com','fdfghg',4),
(2,'jisna','antony','Ponkunnam','9812896758','sonumariaantony@mca.ajce.in','gghhgg',6);

/*Table structure for table `store_feedbacks` */

DROP TABLE IF EXISTS `store_feedbacks`;

CREATE TABLE `store_feedbacks` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(225) NOT NULL,
  `date` varchar(225) NOT NULL,
  `customer_id` bigint(20) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_feedbacks_customer_id_08328eed` (`customer_id`),
  KEY `store_feedbacks_product_id_ef5e8df9` (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `store_feedbacks` */

insert  into `store_feedbacks`(`id`,`feedback`,`date`,`customer_id`,`product_id`) values 
(1,'dfg','2023-04-04',1,2),
(2,'GOOD','2023-04-06',1,4);

/*Table structure for table `store_loginn` */

DROP TABLE IF EXISTS `store_loginn`;

CREATE TABLE `store_loginn` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(225) NOT NULL,
  `password` varchar(225) NOT NULL,
  `usertype` varchar(225) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `store_loginn` */

insert  into `store_loginn`(`id`,`username`,`password`,`usertype`) values 
(1,'admin','pbkdf2_sha256$260000$PoBonepLMB5qGPUUXBkKba$lEPYozegTI8v5o34M2t/jqJxRNdD1CA5YgHoNcwWnA4=','admin'),
(2,'sonu','pbkdf2_sha256$260000$PoBonepLMB5qGPUUXBkKba$lEPYozegTI8v5o34M2t/jqJxRNdD1CA5YgHoNcwWnA4=','seller'),
(3,'maria','pbkdf2_sha256$390000$N7VtdfYLiy58vtwMzUbCtz$0th1tThQ+lROTFQe4tOTRHbRbEVdxYJ6VspebXyxZJU=','seller'),
(4,'sherin','pbkdf2_sha256$260000$PoBonepLMB5qGPUUXBkKba$lEPYozegTI8v5o34M2t/jqJxRNdD1CA5YgHoNcwWnA4=','customer'),
(5,'jeff','pbkdf2_sha256$390000$uMYalb6StdoGri8MpkAdhU$jePgJfza9jBm17IkGGzN4vW/wxYnnIbaa1RwilOSKXQ=','staff'),
(6,'jisna','pbkdf2_sha256$390000$CNUvCagCzzc2huswCHxKeM$zxlvxfJgzlSsliFSzqkC5jJcp324rJaUy9jiOn1dplA=','customer'),
(7,'antony','pbkdf2_sha256$390000$kxx7XYPcDgCFOwEMuMxqTr$QzxjLwyuKRVKZk84RFP36DCFLQXop4xrXWVJeUgyVo8=','staff'),
(8,'aa','pbkdf2_sha256$260000$oJlApGlrFVfvjkZ3Suvxcd$p5/0MfjFYCkeQcNTfgTTkjJLx6mDAwAxCFgck+xVOyM=','pending');

/*Table structure for table `store_payment` */

DROP TABLE IF EXISTS `store_payment`;

CREATE TABLE `store_payment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `amount` varchar(225) NOT NULL,
  `date` varchar(225) NOT NULL,
  `booking_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_payment_booking_id_71a6b0fb_fk_store_booking_id` (`booking_id`),
  CONSTRAINT `store_payment_booking_id_71a6b0fb_fk_store_booking_id` FOREIGN KEY (`booking_id`) REFERENCES `store_booking` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `store_payment` */

/*Table structure for table `store_product` */

DROP TABLE IF EXISTS `store_product`;

CREATE TABLE `store_product` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `product` varchar(225) NOT NULL,
  `amt` decimal(10,0) NOT NULL,
  `quantity` varchar(225) NOT NULL,
  `image` varchar(1000) NOT NULL,
  `description` varchar(2000) NOT NULL,
  `pstatus` varchar(225) NOT NULL,
  `seller_id` bigint(20) NOT NULL,
  `subcategory_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_product_seller_id_9cddda9d_fk_store_sellerr_id` (`seller_id`),
  KEY `store_product_subcategory_id_4a875c72_fk_store_subcategory_id` (`subcategory_id`),
  CONSTRAINT `store_product_seller_id_9cddda9d_fk_store_sellerr_id` FOREIGN KEY (`seller_id`) REFERENCES `store_sellerr` (`id`),
  CONSTRAINT `store_product_subcategory_id_4a875c72_fk_store_subcategory_id` FOREIGN KEY (`subcategory_id`) REFERENCES `store_subcategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `store_product` */

insert  into `store_product`(`id`,`product`,`amt`,`quantity`,`image`,`description`,`pstatus`,`seller_id`,`subcategory_id`) values 
(1,'fantail Goldfish',200,'25','Fantail Gold Fish_WLR8wer.jpg','hjgggfdg','active',1,2),
(2,'Java Fern',500,'150','Java Fern_7SU6fXT.jpg','kjhjhhh','active',2,4),
(3,'pingu Guppy',50,'4','Pingu Guppy_j0spGSq.jpg','njhgfxd','active',2,3),
(4,'Java Fern',250,'0','Java Fern_b7nudbn.jpg','jkhgfd','active',1,3),
(5,'ASSS',400,'100','WhatsApp Image 2023-04-01 at 10.25.31 AM.jpeg','SWEDW RVFR FERFED FRFERF EFEDRF R EFRERFE FRFDEX FRDFDE','active',1,2);

/*Table structure for table `store_req_payment` */

DROP TABLE IF EXISTS `store_req_payment`;

CREATE TABLE `store_req_payment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `amount` varchar(225) NOT NULL,
  `date` varchar(225) NOT NULL,
  `srequest_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_req_payment_srequest_id_3beaded0_fk_store_srequest_id` (`srequest_id`),
  CONSTRAINT `store_req_payment_srequest_id_3beaded0_fk_store_srequest_id` FOREIGN KEY (`srequest_id`) REFERENCES `store_srequest` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `store_req_payment` */

/*Table structure for table `store_review` */

DROP TABLE IF EXISTS `store_review`;

CREATE TABLE `store_review` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `rate` varchar(50) NOT NULL,
  `reviews` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `customer_id` bigint(20) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_review_customer_id_8a20ccc2` (`customer_id`),
  KEY `store_review_product_id_abc413b2` (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `store_review` */

insert  into `store_review`(`id`,`rate`,`reviews`,`date`,`customer_id`,`product_id`) values 
(3,'4','good','2023-04-06',1,3),
(2,'5','kkk','2023-04-04',1,2),
(4,'3','not bad','2023-04-06',1,4);

/*Table structure for table `store_sellerr` */

DROP TABLE IF EXISTS `store_sellerr`;

CREATE TABLE `store_sellerr` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(225) NOT NULL,
  `lastname` varchar(225) NOT NULL,
  `place` varchar(225) NOT NULL,
  `phone` varchar(225) NOT NULL,
  `address` varchar(225) NOT NULL,
  `email` varchar(225) NOT NULL,
  `license` varchar(1000) NOT NULL,
  `login_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_sellerr_login_id_dcc22439_fk_store_loginn_id` (`login_id`),
  CONSTRAINT `store_sellerr_login_id_dcc22439_fk_store_loginn_id` FOREIGN KEY (`login_id`) REFERENCES `store_loginn` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `store_sellerr` */

insert  into `store_sellerr`(`id`,`firstname`,`lastname`,`place`,`phone`,`address`,`email`,`license`,`login_id`) values 
(1,'Sonu','Antony','mundakayam','8547524396','HJGHGHGD DJHDG 686513','sonumariaantony@gmail.com','Figma_AquaWorld.pdf',2),
(2,'maria','George','Kanjirappally','9878095987','','sonumariaantony44@gmail.com','Resume.pdf',3),
(3,'cc','ssx','sssssx','9988663322','ammu villa','annababykp@gmail.com','Question_Paper.pdf',8);

/*Table structure for table `store_services` */

DROP TABLE IF EXISTS `store_services`;

CREATE TABLE `store_services` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `service` varchar(225) NOT NULL,
  `rate` varchar(225) NOT NULL,
  `des` varchar(225) NOT NULL,
  `seller_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_services_seller_id_fde041c5_fk_store_sellerr_id` (`seller_id`),
  CONSTRAINT `store_services_seller_id_fde041c5_fk_store_sellerr_id` FOREIGN KEY (`seller_id`) REFERENCES `store_sellerr` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `store_services` */

insert  into `store_services`(`id`,`service`,`rate`,`des`,`seller_id`) values 
(1,'Cleaning','1500','SHBDS JHCFJCV FJVHFUVN FHVNFJGVN',1),
(2,'maintenance','2000','fnhv jmvhbhfv fbvjfvn fjnvjfvn jnvjfvn',2),
(3,'Setting','300',' vnbnb fbvhfgb hjfvuhv hjvbgvjb',1);

/*Table structure for table `store_sfeedback` */

DROP TABLE IF EXISTS `store_sfeedback`;

CREATE TABLE `store_sfeedback` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(225) NOT NULL,
  `date` varchar(225) NOT NULL,
  `customer_id` bigint(20) NOT NULL,
  `service_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_sfeedback_customer_id_b4eba6e4` (`customer_id`),
  KEY `store_sfeedback_service_id_2322d32a` (`service_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `store_sfeedback` */

insert  into `store_sfeedback`(`id`,`feedback`,`date`,`customer_id`,`service_id`) values 
(1,'good','2023-04-09',1,1);

/*Table structure for table `store_srequest` */

DROP TABLE IF EXISTS `store_srequest`;

CREATE TABLE `store_srequest` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `amount` varchar(225) NOT NULL,
  `date` varchar(225) NOT NULL,
  `status` varchar(225) NOT NULL,
  `customer_id` bigint(20) NOT NULL,
  `service_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_srequest_customer_id_88179025_fk_store_customerr_id` (`customer_id`),
  KEY `store_srequest_service_id_f96fd373_fk_store_services_id` (`service_id`),
  CONSTRAINT `store_srequest_customer_id_88179025_fk_store_customerr_id` FOREIGN KEY (`customer_id`) REFERENCES `store_customerr` (`id`),
  CONSTRAINT `store_srequest_service_id_f96fd373_fk_store_services_id` FOREIGN KEY (`service_id`) REFERENCES `store_services` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `store_srequest` */

insert  into `store_srequest`(`id`,`amount`,`date`,`status`,`customer_id`,`service_id`) values 
(1,'2000','2023-03-13','finished',1,1),
(2,'1500','2023-03-13','accept',1,2),
(3,'1500','2023-04-06','pending',1,1);

/*Table structure for table `store_sreview` */

DROP TABLE IF EXISTS `store_sreview`;

CREATE TABLE `store_sreview` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `rate` varchar(50) NOT NULL,
  `reviews` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `customer_id` bigint(20) NOT NULL,
  `service_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_sreview_customer_id_20184bd8` (`customer_id`),
  KEY `store_sreview_service_id_d34c6701` (`service_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `store_sreview` */

insert  into `store_sreview`(`id`,`rate`,`reviews`,`date`,`customer_id`,`service_id`) values 
(1,'4','nice work','2023-04-09',1,1);

/*Table structure for table `store_staff` */

DROP TABLE IF EXISTS `store_staff`;

CREATE TABLE `store_staff` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fn` varchar(225) NOT NULL,
  `ln` varchar(225) NOT NULL,
  `place` varchar(225) NOT NULL,
  `phone` varchar(225) NOT NULL,
  `email` varchar(225) NOT NULL,
  `sstatus` varchar(225) NOT NULL,
  `login_id` bigint(20) NOT NULL,
  `seller_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_staff_login_id_3df93ffa_fk_store_loginn_id` (`login_id`),
  KEY `store_staff_seller_id_2f48bc8d_fk_store_sellerr_id` (`seller_id`),
  CONSTRAINT `store_staff_login_id_3df93ffa_fk_store_loginn_id` FOREIGN KEY (`login_id`) REFERENCES `store_loginn` (`id`),
  CONSTRAINT `store_staff_seller_id_2f48bc8d_fk_store_sellerr_id` FOREIGN KEY (`seller_id`) REFERENCES `store_sellerr` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `store_staff` */

insert  into `store_staff`(`id`,`fn`,`ln`,`place`,`phone`,`email`,`sstatus`,`login_id`,`seller_id`) values 
(1,'jeff','Antony','Kochi','8978095634','sonumariaantony44@gmail.com','active',5,1),
(2,'antony','Kuruvila','Peruvanthanm','9446223354','sonumariaantony44@gmail.com','active',7,2);

/*Table structure for table `store_subcategory` */

DROP TABLE IF EXISTS `store_subcategory`;

CREATE TABLE `store_subcategory` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `subcategory` varchar(225) NOT NULL,
  `cstatus` varchar(225) NOT NULL,
  `category_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_subcategory_category_id_c0eefd44_fk_store_category_id` (`category_id`),
  CONSTRAINT `store_subcategory_category_id_c0eefd44_fk_store_category_id` FOREIGN KEY (`category_id`) REFERENCES `store_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `store_subcategory` */

insert  into `store_subcategory`(`id`,`subcategory`,`cstatus`,`category_id`) values 
(2,'Gold Fish','active',2),
(3,'Guppy','active',2),
(4,'Fern','active',3),
(5,'Moss','active',3);

/*Table structure for table `store_wishlist` */

DROP TABLE IF EXISTS `store_wishlist`;

CREATE TABLE `store_wishlist` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `customerr_id` bigint(20) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_wishlist_customerr_id_89ab0cf6_fk_store_customerr_id` (`customerr_id`),
  KEY `store_wishlist_product_id_8af1333d_fk_store_product_id` (`product_id`),
  CONSTRAINT `store_wishlist_customerr_id_89ab0cf6_fk_store_customerr_id` FOREIGN KEY (`customerr_id`) REFERENCES `store_customerr` (`id`),
  CONSTRAINT `store_wishlist_product_id_8af1333d_fk_store_product_id` FOREIGN KEY (`product_id`) REFERENCES `store_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `store_wishlist` */

insert  into `store_wishlist`(`id`,`customerr_id`,`product_id`) values 
(2,1,1),
(6,1,3),
(7,1,2);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
