## mod_dir.so

> `/usr/libexec/apache2/mod_dir.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x1154
+880.0.0.0.0
+  __TEXT.__text: 0xf40
   __TEXT.__auth_stubs: 0x160
   __TEXT.__cstring: 0x255
-  __TEXT.__unwind_info: 0x54
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0xb0
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0xf0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: ED84F90E-3B0C-393B-9F3C-5EFE41D35CC8
+  UUID: 1F97599B-2118-3087-9CC3-2FEEF4337524
   Functions: 10
   Symbols:   36
   CStrings:  28
Functions:
~ _create_dir_config : 112 -> 108
~ _merge_dir_configs : 440 -> 400
~ _add_index : 400 -> 340
~ _configure_slash : 76 -> 60
~ _configure_checkhandler : 76 -> 60
~ _configure_redirect : 432 -> 372
~ _dir_fixups : 156 -> 136
~ _fixup_dir : 1960 -> 1732
~ _fixup_dflt : 716 -> 628
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/mappers/mod_dir.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/mappers/mod_dir.c"

```
