## mod_reflector.so

> `/usr/libexec/apache2/mod_reflector.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xb14
+880.0.0.0.0
+  __TEXT.__text: 0xa08
   __TEXT.__auth_stubs: 0x1a0
   __TEXT.__cstring: 0x19d
-  __TEXT.__unwind_info: 0x54
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0xd0
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 1AC5E970-1BBE-3A9E-AD89-3841416B97BE
+  UUID: 7ABE3756-55FE-3759-AE19-C74F0E9B5062
   Functions: 6
   Symbols:   35
   CStrings:  11
Functions:
~ _create_reflector_dir_config : 84 -> 80
~ _merge_reflector_dir_config : 124 -> 112
~ _reflector_header : 140 -> 128
~ _reflector_handler : 2296 -> 2068
~ _header_do : 124 -> 112
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_reflector.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_reflector.c"

```
