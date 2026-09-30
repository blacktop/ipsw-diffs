## mod_actions.so

> `/usr/libexec/apache2/mod_actions.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xb88
+880.0.0.0.0
+  __TEXT.__text: 0xa44
   __TEXT.__auth_stubs: 0xf0
   __TEXT.__cstring: 0x193
-  __TEXT.__unwind_info: 0x48
+  __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0x78
   __DATA_CONST.__const: 0x78
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 9E608C98-5BBA-3B83-B0CA-F7DFBBE975A5
+  UUID: A12FFA8E-3EFB-3250-95CA-0F10EC92C3B1
   Functions: 6
   Symbols:   23
   CStrings:  17
Functions:
~ _create_action_dir_config : 100 -> 96
~ _merge_action_dir_configs : 344 -> 312
~ _add_action : 312 -> 272
~ _set_script : 296 -> 280
~ _action_handler : 1832 -> 1600
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/mappers/mod_actions.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/mappers/mod_actions.c"

```
