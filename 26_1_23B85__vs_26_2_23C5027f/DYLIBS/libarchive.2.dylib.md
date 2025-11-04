## libarchive.2.dylib

> `/usr/lib/libarchive.2.dylib`

```diff

-160.0.0.0.0
-  __TEXT.__text: 0xe1f24
+160.60.2.0.0
+  __TEXT.__text: 0xe2064
   __TEXT.__auth_stubs: 0x1100
-  __TEXT.__const: 0x932c
+  __TEXT.__const: 0x9334
   __TEXT.__cstring: 0x9e31
   __TEXT.__unwind_info: 0xb60
   __DATA_CONST.__got: 0x30

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 1F01B476-B40C-3BA9-B1E9-8AA3E67DA268
+  UUID: 0199614F-F4D0-346F-AED7-1854E98F3410
   Functions: 2241
   Symbols:   4495
   CStrings:  1826
Functions:
~ _archive_read_open_fd : 520 -> 532
~ _file_skip : 320 -> 400
~ _archive_read_open_FILE : 460 -> 472
~ _FILE_skip : 168 -> 292
~ _file_open : 724 -> 736
~ _file_skip_lseek : 400 -> 480

```
