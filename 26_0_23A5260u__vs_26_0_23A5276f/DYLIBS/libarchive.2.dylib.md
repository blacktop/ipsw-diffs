## libarchive.2.dylib

> `/usr/lib/libarchive.2.dylib`

```diff

-156.0.0.0.0
-  __TEXT.__text: 0xe1d54
+157.0.0.0.0
+  __TEXT.__text: 0xe1f18
   __TEXT.__auth_stubs: 0x1100
   __TEXT.__const: 0x932c
-  __TEXT.__cstring: 0x9d44
+  __TEXT.__cstring: 0x9e31
   __TEXT.__unwind_info: 0xb58
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x1a10

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 74B60CDB-CDA9-3DFE-BAAA-7BA48CCF9B9E
+  UUID: C2B8C297-EF41-3A4E-B128-4C794AC2B723
   Functions: 2241
   Symbols:   4495
-  CStrings:  1818
+  CStrings:  1826
 
Functions:
~ _archive_read_format_rar_read_header : 1756 -> 1792
~ _read_header : 5940 -> 6288
~ _read_symlink_stored : 300 -> 372
~ _rar_read_ahead : 436 -> 424
~ _expand : 3040 -> 3008
~ _copy_from_lzss_window : 304 -> 312
~ _parse_filter : 1760 -> 1792
CStrings:
+ "Extended header size too large."
+ "Failed to read extended header data."
+ "Failed to read full header content."
+ "Failed to read link."
+ "Failed to read next header."
+ "Unable to read extended header data."
+ "Unable to read link."
+ "Unable to store offsets."

```
