-- chat_id_list
CREATE TABLE IF NOT EXISTS `Chat_id_List` (
  `id` int(11) NOT NULL,
  `Chat_id` int(11) NOT NULL,
  `Username` text NOT NULL,
  `Nome` int(11) NOT NULL,
  `Cognome` int(11) NOT NULL,
  `E-mail` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `Chat_id_List`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `Chat_id_List`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- stat_list
CREATE TABLE stat_list (
	Type varchar(100),
	chat_id int(100),
	DateCommand DATE
);