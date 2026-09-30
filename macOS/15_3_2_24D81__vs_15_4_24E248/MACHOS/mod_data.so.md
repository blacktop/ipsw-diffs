## mod_data.so

> `/usr/libexec/apache2/mod_data.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xa68
+880.0.0.0.0
+  __TEXT.__text: 0x988
   __TEXT.__auth_stubs: 0x150
   __TEXT.__cstring: 0xc6
   __TEXT.__const: 0x28
-  __TEXT.__unwind_info: 0x50
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0xa8
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: DD14F3A2-28AB-3650-91D0-87C85DAB8AB3
+  UUID: 641F40E9-8E64-3D0B-ADE9-205745787E69
   Functions: 2
   Symbols:   29
   CStrings:  5
Functions:
~ _data_out_filter : 2596 -> 2372
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_data.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_data.c"

```
