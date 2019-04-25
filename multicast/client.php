<?php

	$len = 80;
	$flags = 0;
	$from = "";
	$port = 14446;
	$grpparms = array("group" => "224.0.0.0", "interface" => "enp0s31f6");
	$sock = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP);
	socket_bind($sock,'0.0.0.0',$port);
	socket_set_option($sock, SOL_SOCKET, SO_REUSEADDR, 1);
	socket_set_option($sock,IPPROTO_IP,MCAST_JOIN_GROUP, $grpparms);
	socket_recvfrom($sock,$recvStr,$len,$flags,$from,$port);
	echo("Received " . $recvStr . " from " . $from); 
	socket_close($sock);

?>
