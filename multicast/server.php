<?php
	$port = 14446;
	$grpparms = array("group" => "225.0.0.0", "interface" => "enp0s31f6");
	$mesg = "E ai galera do youtube";
	$sock = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP);
	socket_set_option($sock, SOL_SOCKET, SO_REUSEADDR, 1);
	socket_set_option($sock, IPPROTO_IP, MCAST_JOIN_GROUP, $grpparms);
	socket_sendto($sock, $mesg, strlen($mesg), 0, '225.0.0.0', $port);
	socket_close($sock); 
?>
