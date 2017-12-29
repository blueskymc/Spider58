DROP DATABASE IF EXISTS `house`;
CREATE DATABASE `house` /*!40100 DEFAULT CHARACTER SET gbk */;
USE `house`;

CREATE TABLE `info` (
  `id` int(11) NOT NULL auto_increment,
  `title` varchar(255) default NULL,
  `mianshui` varchar(255) default NULL,
  `date` varchar(255) default NULL,
  `view_num` varchar(255) default NULL,
  `price` varchar(255) default NULL,
  `avg` varchar(255) default NULL,
  `shitingwei` varchar(255) default NULL,
  `cenggao` varchar(255) default NULL,
  `area` varchar(255) default NULL,
  `zhuangxiu` varchar(255) default NULL,
  `toward` varchar(255) default NULL,
  `age` varchar(255) default NULL,
  `xiaoqu` varchar(255) default NULL,
  `weizhi` varchar(255) default NULL,
  `jingjiren` varchar(255) default NULL,
  `link` varchar(255) default NULL,
  `shiqu` int(11) default 0,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;