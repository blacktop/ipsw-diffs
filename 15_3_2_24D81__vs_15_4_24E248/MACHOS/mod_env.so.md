## mod_env.so

> `/usr/libexec/apache2/mod_env.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x614
+880.0.0.0.0
+  __TEXT.__text: 0x598
   __TEXT.__auth_stubs: 0xf0
   __TEXT.__cstring: 0x1df
-  __TEXT.__unwind_info: 0x48
+  __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0x78
   __DATA_CONST.__const: 0xa0
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 70763EF4-357E-3A6A-9FFA-7030559D151B
+  UUID: 3593AFBF-2F87-3C94-ABAE-FF801CC61F29
   Functions: 7
   Symbols:   24
   CStrings:  10
Functions:
~ _merge_env_dir_configs : 432 -> 400
~ _add_env_module_vars_passed : 308 -> 272
~ _add_env_module_vars_set : 396 -> 356
~ _add_env_module_vars_unset : 96 -> 92
~ _fixup_env_module : 152 -> 140
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/metadata/mod_env.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/metadata/mod_env.c"

```
