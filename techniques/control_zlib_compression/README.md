# control_zlib_compression

## Main
Chức năng của code là tạo ra một đoạn byte mà khi `zlib.compress()` sẽ tạo được một substring chứa `payload` mong muốn. 

`zlib.compress()` được dùng trong file png do đó ta có context sử dụng như sau:
- Upload file ảnh png có payload mong muốn ví dụ như `$_GET[1]($_POST[2])`.
- Local File Include file ảnh đó.

Hoặc là với context PoC của [CVE-2021-25003](https://wpscan.com/vulnerability/5c21ad35-b2fb-4a51-858f-8ffff685de4a), có phần tìm một chuỗi hex khi compress sẽ chứa payload. Trong link thì tác giả không chỉ cách tìm ra chuỗi đó nên mình khá chật vật tìm hiểu để ~~chắp vá~~ viết ra code này.
![Oops](https://user-images.githubusercontent.com/91038460/209658753-5f66c4c3-f8af-4540-9929-31d55a990e85.png)

## Ý tưởng:
Vì zlib compression/decompression là quá trình không làm mất dữ liệu, nên nếu muốn tìm một đoạn byte mà compress ra đoạn code mong muốn thì mình sẽ decompress đoạn code đó để tìm đoạn byte. Do đó mình đi tìm hiểu về zlib compressed data format rồi cả cách implement quá trình decompression để theo ý muốn.

## ~~Chép code~~ Tham khảo:
- https://calmarius.net/index.php?lang=en&page=programming%2Fzlib_deflate_quick_reference: Đây là nơi mình đọc về format của compressed data.
- https://pyokagan.name/blog/2019-10-18-zlibinflate/. Đây là link mình đọc về thuật toán sử dụng trong `zlib.compress()` và cả chép code nữa. 🦫
