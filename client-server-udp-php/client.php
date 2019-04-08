<?php
	$s=socket_create(AF_INET, SOCK_DGRAM, 0);
	socket_sendto($s, "Hello World", 11, 0, "localhost", "8888");
?>