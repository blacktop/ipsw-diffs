## libarchive.2.dylib

> `/usr/lib/libarchive.2.dylib`

```diff

-182.0.1.0.0
-  __TEXT.__text: 0xe31b4
+182.40.6.0.0
+  __TEXT.__text: 0xe3460
   __TEXT.__const: 0x9334
   __TEXT.__cstring: 0x9e64
   __TEXT.__unwind_info: 0x2228

   __DATA_CONST.__const: 0x1a10
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xd48
-  __AUTH_CONST.__auth_got: 0x8d0
+  __AUTH_CONST.__auth_got: 0x8e0
   __DATA.__data: 0xc
   __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__bss: 0xb9

   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
   Functions: 2249
-  Symbols:   2533
+  Symbols:   2535
   CStrings:  1828
 
Symbols:
+ __qtn_file_init_with_path
+ __qtn_file_to_data
Functions:
~ _lzx_decode_init : 1140 -> 1148
~ _lzx_read_blocks : 3772 -> 3872
~ _lzx_decode_blocks : 3292 -> 3492
~ _restore_entry : 1680 -> 1676
~ _create_filesystem_object_at : 2616 -> 2648
~ _setup_xattrs : 772 -> 1080
~ _build_pathname_utf16be : 448 -> 488
```
