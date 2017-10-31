<?php
$socket = socket_create( AF_INET, SOCK_DGRAM, SOL_UDP );
if ( $socket === false ) {
    echo "socket_create() failed:reason:" . socket_strerror( socket_last_error() ) . "\n";
}
$ok = socket_bind( $socket, '0.0.0.0', 8888 );
if ( $ok === false ) {
    echo "socket_bind() failed:reason:" . socket_strerror( socket_last_error( $socket ) );
}
while ( true ) {

    $from = "";
    $port = 0;
    socket_recvfrom( $socket, $buf,1024, 0, $from, $port );

    echo $buf;
    if($buf=="on"){
      exec("./on.sh 2 1");
    }else{
      exec("./off.sh 2 0");
    }
}
?>
