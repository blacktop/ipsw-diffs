## libarchive.2.dylib

> `/usr/lib/libarchive.2.dylib`

```diff

-167.120.3.0.0
-  __TEXT.__text: 0xe2170
+167.160.3.0.0
+  __TEXT.__text: 0xe2238
   __TEXT.__auth_stubs: 0x1100
   __TEXT.__const: 0x9334
-  __TEXT.__cstring: 0x9e43
+  __TEXT.__cstring: 0x9e64
   __TEXT.__unwind_info: 0xb68
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x1a10

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0B08D29C-2B19-33CA-A6C6-612AEA8006E6
+  UUID: D977ADE9-B9B6-30DF-92DE-E8E09745DAB4
   Functions: 2247
   Symbols:   4496
-  CStrings:  1827
+  CStrings:  1828
 
Functions:
~ _cab_read_ahead_cfdata_lzx : 1204 -> 1272
~ _hfs_write_decmpfs_block : 1084 -> 1088
~ _parse_codes : 3888 -> 3920
~ _copy_from_lzss_window : 312 -> 380
~ _parse_filter : 1792 -> 1820
CStrings:
+ "Invalid CFDATA uncompressed size"

```
