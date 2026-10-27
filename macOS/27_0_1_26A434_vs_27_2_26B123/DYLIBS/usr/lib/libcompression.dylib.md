## libcompression.dylib

> `/usr/lib/libcompression.dylib`

```diff

-212.0.1.0.0
-  __TEXT.__text: 0x653cc
-  __TEXT.__const: 0x76e91
+212.40.2.0.0
+  __TEXT.__text: 0x64c34
+  __TEXT.__const: 0x76ec1
   __TEXT.__cstring: 0x2ec
   __TEXT.__unwind_info: 0x700
   __TEXT.__eh_frame: 0x450

   __AUTH_CONST.__const: 0x10a0
   __AUTH_CONST.__auth_got: 0x188
   __AUTH_CONST.__auth_ptr: 0x0
-  __DATA.__data: 0x480
+  __DATA.__data: 0x420
   __DATA.__common: 0x1200
+  __DATA_DIRTY.__data: 0x60
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
~ _lzfseDecode : 5028 -> 5036
~ _lzvnDecode : 1132 -> 1128
~ _lzvn_decode_scratch_size : 32 -> 24
~ _zlibDecodeBuffer : 2352 -> 1580
~ _zlibDecodeBufferSafe : 2596 -> 1824
~ _readHuffmanTable : 2052 -> 1036
~ _msh_decode_buffer : 3656 -> 3756
~ _lz24_decode_buffer : 696 -> 712
~ _lzbitmap_decode : 2212 -> 2344
~ _smb_lznt1_decode_buffer : 520 -> 512
~ _lzfse_decode_buffer_output_size : 504 -> 500
~ _lzfse_decode_buffer_iboot : 2976 -> 2988
~ _lzfse_decode_lzvn_block_iboot : 464 -> 460
~ _smb_lz77h_decode_buffer : 1308 -> 1300
~ _lzbitmap_fast_decode : 1532 -> 1380
~ _lzbitmap_fast_decode_buffer : 52 -> 60
~ _lzbitmap_decode_buffer : 52 -> 60
~ _smb_lz77_decode_buffer : 472 -> 464
+ _getDecoderTable
~ _lzx_decode_buffer : 2292 -> 2300
```
