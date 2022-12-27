# control_zlib_compression

## Main
Chức năng của code là tạo ra một đoạn byte mà khi `zlib.compress()` sẽ tạo được một substring chứa `payload` mong muốn. 

`zlib.compress()` được dùng trong file png do đó ta có context sử dụng như sau:
- Upload file ảnh png có payload mong muốn ví dụ như `<?=$_GET[1]($_POST[2]);?>`.
- Local File Include file ảnh đó.

Ví dụ với context trên:

```python
import zlib

zlib.compress(b'\x03\xa3\x9fgTo,$\x15+!g\x12To\x11.)\x15+\x19g"ko_P') 
# Kết quả: b'x\x9cc^<?=$_GET[1]($_POST[2]);?>\x00\x00hi\x070'. Có chứa '<?=$_GET[1]($_POST[2]);?>'
```

Hoặc là với context PoC của [CVE-2021-25003](https://wpscan.com/vulnerability/5c21ad35-b2fb-4a51-858f-8ffff685de4a), có phần tìm một chuỗi hex khi compress sẽ chứa payload. Trong link thì tác giả không chỉ cách tìm ra chuỗi đó nên mình khá chật vật tìm hiểu để ~~chắp vá~~ viết ra code này.
![Oops](https://user-images.githubusercontent.com/91038460/209658753-5f66c4c3-f8af-4540-9929-31d55a990e85.png)

## Ý tưởng:
Vì zlib compression/decompression là quá trình không làm mất dữ liệu, nên nếu muốn tìm một đoạn byte mà compress ra đoạn code mong muốn thì mình sẽ decompress đoạn code đó để tìm đoạn byte. Do đó mình đi tìm hiểu về zlib compressed data format rồi cả cách implement quá trình decompression để theo ý muốn.

## Cách dùng:
Vào sửa biến `payload` rồi chạy code thôi 😉.
```Ruby
b'\x03\xa3\x9fgTo,$\x15+!g\x12To\x11.)\x15+\x19g"ko_P'

Double check
Yeah 🙂
```

Nếu chương trình bị lỗi hoặc in ra `Constraint may be violated` hoặc `Take a rest 🤕` thì có thể là code đã không cover được hết trường hợp 😭.

Ngược lại, dòng đầu tiên chính là chuỗi byte mà ta cần 😁

## Lưu ý:
Không phải tất cả payload đều hoạt động được, ví dụ ``<?=`$_GET[1]`;?>`` sẽ gây ra lỗi.

Điều kiện để code gặp ít lỗi nhất (nhưng vẫn sẽ có lỗi 🥲), nếu không thì sẽ phải tự sửa lại tùy payload 😿
1. Không dùng quá nhiều loại ký tự khác nhau trong payload.
2. Dùng payload càng ngắn càng tốt.
3. Mỗi substring độ dài 3 sau khi decompress() không xuất hiện quá 1 lần (Để đảm bảo BTYPE luôn bằng 1).
4. Nên để terminate_symbol như vậy.

## ~~Chép code~~ Tham khảo:
- https://calmarius.net/index.php?lang=en&page=programming%2Fzlib_deflate_quick_reference: Đây là nơi mình đọc về format của compressed data.
- https://pyokagan.name/blog/2019-10-18-zlibinflate/. Đây là link mình đọc về thuật toán sử dụng trong `zlib.compress()` và cả chép code nữa. 🦫

## Ghi chú cho sau này:
- Cái cây cần dùng cho debug khi `BTYPE=1` :)
![Oops](https://user-images.githubusercontent.com/91038460/209665780-a1483101-f2f8-4e34-a07e-ac95989c238a.png)
- Các phần được implement nhưng lại không dùng mà được để lại đề phòng sau này sẽ được comment là `# [skip me]`
- Điều kiện 1 được dùng để đảm bảo BTYPE không thể bằng 0.
- Điều kiện 2 được dùng để đảm bảo BTYPE không thể bằng 2.
- Điều kiện 3 được dùng để đảm bảo thuật toán LZ77 được dùng khi compress() không có tác dụng, do đó lúc decompress() cũng không có tác dụng.
- 27/12/2022: chỉ có 3 loại BTYPE 0, 1 và 2. Mình cố gắng để BTYPE = 1, 
      + là một giá trị cho phép hiệu quả về cả độ phức tạp và độ dài của payload và output.
      + mình cố gắng để BTYPE = 1 nhưng đoạn implement decompress() thì có cả code xử lý khi BTYPE = 0 hay 2 dùng để đề phòng cho sau này.
      + tương tự phần xử lý LZ77 ở trên cũng không có tác dụng nhưng sẽ được mình để lại.
