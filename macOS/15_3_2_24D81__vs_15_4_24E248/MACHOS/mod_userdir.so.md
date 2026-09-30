## mod_userdir.so

> `/usr/libexec/apache2/mod_userdir.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xb2c
+880.0.0.0.0
+  __TEXT.__text: 0x9d4
   __TEXT.__auth_stubs: 0x130
   __TEXT.__cstring: 0x1a2
-  __TEXT.__unwind_info: 0x54
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0x98
   __DATA_CONST.__const: 0x70
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 024146E1-0EC7-3ACB-8E43-A2D44CC42DE1
+  UUID: 90AFF326-0FD3-3D33-BA96-59D54D885948
   Functions: 6
   Symbols:   29
   CStrings:  14
Functions:
~ _merge_userdir_config : 268 -> 240
~ _register_hooks : 112 -> 120
~ _set_user_dir : 516 -> 440
~ _translate_userdir : 1608 -> 1396
~ _get_suexec_id_doer : 224 -> 188
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/mappers/mod_userdir.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/mappers/mod_userdir.c"

```
