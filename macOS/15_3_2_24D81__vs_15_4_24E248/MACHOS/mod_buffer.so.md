## mod_buffer.so

> `/usr/libexec/apache2/mod_buffer.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x1044
+880.0.0.0.0
+  __TEXT.__text: 0xf0c
   __TEXT.__auth_stubs: 0xe0
   __TEXT.__cstring: 0x110
   __TEXT.__const: 0x7
-  __TEXT.__unwind_info: 0x48
+  __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0x70
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__const: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: C967A975-D5B4-316C-B917-9267F168C57C
+  UUID: 5ABAF4F7-4442-3ABE-80CF-187AAF9D47C6
   Functions: 6
   Symbols:   26
   CStrings:  4
Functions:
~ _create_buffer_config : 88 -> 84
~ _merge_buffer_config : 236 -> 208
~ _set_buffer_size : 156 -> 136
~ _buffer_out_filter : 1680 -> 1552
~ _buffer_in_filter : 1888 -> 1756
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_buffer.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_buffer.c"

```
