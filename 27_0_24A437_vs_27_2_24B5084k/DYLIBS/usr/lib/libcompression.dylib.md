## libcompression.dylib

> `/usr/lib/libcompression.dylib`

```diff

-212.0.1.0.0
-  __TEXT.__text: 0x63c60
-  __TEXT.__const: 0x76e91
+212.40.2.0.0
+  __TEXT.__text: 0x634dc
+  __TEXT.__const: 0x76ec1
   __TEXT.__cstring: 0x2ec
-  __TEXT.__unwind_info: 0x860
+  __TEXT.__unwind_info: 0x868
   __TEXT.__eh_frame: 0x460
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x280

   __DATA.__common: 0x1200
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblzma.5.dylib
-  Functions: 546
-  Symbols:   719
+  Functions: 547
+  Symbols:   720
   CStrings:  49
 
Symbols:
+ _getDecoderTable
Functions:
~ _lzvnDecode : 1136 -> 1132
~ _lzfseDecode : 4224 -> 4232
~ _zlibDecodeBufferSafe : 2564 -> 1792
~ _zlibDecodeBuffer : 2344 -> 1572
~ _readHuffmanTable : 2024 -> 1020
~ _zlib_stream_get_encode_state_size : 60 -> 44
~ _lzbitmap_decode : 2220 -> 2372
~ _lzbitmap_decode_buffer : 52 -> 60
+ _getDecoderTable
~ _msh_decode_buffer : 3640 -> 3740
~ _lz24_decode_buffer : 696 -> 712
~ _smb_lznt1_decode_buffer : 516 -> 508
~ _lzfse_decode_buffer_output_size : 504 -> 500
~ _lzfse_decode_buffer_iboot : 2956 -> 2968
~ _lzfse_decode_lzvn_block_iboot : 460 -> 456
~ _smb_lz77h_decode_buffer : 1304 -> 1296
~ _lzbitmap_fast_decode : 1492 -> 1340
~ _lzbitmap_fast_decode_buffer : 52 -> 60
~ _smb_lz77_decode_buffer : 468 -> 460
~ _lzx_decode_buffer : 2292 -> 2300
~ _lzma_stream_end : 56 -> 60
```
