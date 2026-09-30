## libarchive.2.dylib

> `/usr/lib/libarchive.2.dylib`

```diff

-149.0.0.0.0
-  __TEXT.__text: 0xe1a64
-  __TEXT.__auth_stubs: 0x10c0
-  __TEXT.__const: 0x932c
-  __TEXT.__cstring: 0x9cb0
+151.140.2.0.0
+  __TEXT.__text: 0xe1d3c
+  __TEXT.__auth_stubs: 0x10d0
+  __TEXT.__const: 0x9334
+  __TEXT.__cstring: 0x9dbc
   __TEXT.__unwind_info: 0xba8
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x1a10
-  __AUTH_CONST.__auth_got: 0x860
+  __AUTH_CONST.__auth_got: 0x868
   __AUTH_CONST.__const: 0xd48
   __DATA.__data: 0xc
   __DATA.__bss: 0x1438

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B7C5C2A6-36E1-3490-86A9-E150FEDC168A
-  Functions: 2237
-  Symbols:   4482
-  CStrings:  1814
+  UUID: 83538842-1D49-3659-9AE2-92166CEE3B18
+  Functions: 2238
+  Symbols:   4485
+  CStrings:  1823
 
Symbols:
+ _FILE_close
+ _FILE_read
+ _FILE_seek
+ _FILE_skip
+ _ftello
Functions:
~ __archive_read_data_block : 1320 -> 1336
~ _client_skip_proxy : 484 -> 444
~ _file_seek : 256 -> 272
~ _archive_read_open_FILE : 440 -> 460
+ _FILE_seek
~ _file_seek : 312 -> 328
~ _file_skip_lseek : 384 -> 400
~ __warc_rdhdr : 1464 -> 1484
~ __warc_skip : 88 -> 132
~ _archive_read_format_rar_read_header : 1756 -> 1792
~ _read_header : 5940 -> 6288
~ _read_symlink_stored : 300 -> 372
~ _rar_read_ahead : 436 -> 424
~ _expand : 3040 -> 3008
~ _copy_from_lzss_window : 304 -> 312
~ _parse_filter : 1760 -> 1792
CStrings:
+ "Error seeking in FILE* pointer"
+ "Extended header size too large."
+ "Failed to read extended header data."
+ "Failed to read full header content."
+ "Failed to read link."
+ "Failed to read next header."
+ "Unable to read extended header data."
+ "Unable to read link."
+ "Unable to store offsets."

```
