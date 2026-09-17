## libcompression.dylib

> `/usr/lib/libcompression.dylib`

```diff

-212.0.1.0.0
-  __TEXT.__text: 0x641ec
-  __TEXT.__const: 0x76e91
+212.40.2.0.0
+  __TEXT.__text: 0x63a54
+  __TEXT.__const: 0x76ec1
   __TEXT.__cstring: 0x2ec
   __TEXT.__unwind_info: 0x860
   __TEXT.__eh_frame: 0x460

   __DATA.__common: 0x1200
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblzma.5.dylib
-  Functions: 552
-  Symbols:   723
+  Functions: 553
+  Symbols:   724
   CStrings:  49
 
Symbols:
+ _getDecoderTable
Functions:
~ _lzma_stream_end : 56 -> 60
~ _lzfseDecode : 4220 -> 4228
~ _lzvnDecode : 1132 -> 1128
~ _lzvn_decode_scratch_size : 16 -> 8
~ _zlibDecodeBuffer : 2344 -> 1572
~ _zlibDecodeBufferSafe : 2564 -> 1792
~ _readHuffmanTable : 2024 -> 1020
~ _lz4_decode_buffer : 500 -> 488
~ _msh_decode_buffer : 3636 -> 3736
~ _lz24_decode_buffer : 696 -> 712
~ _lzbitmap_decode : 2208 -> 2344
~ _smb_lznt1_decode_buffer : 512 -> 504
~ _lzfse_decode_buffer_output_size : 504 -> 500
~ _lzfse_decode_buffer_iboot : 2976 -> 2988
~ _lzfse_decode_lzvn_block_iboot : 464 -> 460
~ _smb_lz77h_decode_buffer : 1304 -> 1296
~ _lzbitmap_fast_decode : 1496 -> 1344
~ _lzbitmap_fast_decode_buffer : 52 -> 60
~ _lzbitmap_decode_buffer : 52 -> 60
~ _smb_lz77_decode_buffer : 464 -> 456
+ _getDecoderTable
~ _lzx_decode_buffer : 2292 -> 2300
```
