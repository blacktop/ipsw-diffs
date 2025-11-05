## mod_alias.so

> `/usr/libexec/apache2/mod_alias.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x2a2c
+880.0.0.0.0
+  __TEXT.__text: 0x254c
   __TEXT.__auth_stubs: 0x1e0
   __TEXT.__cstring: 0x6a7
-  __TEXT.__unwind_info: 0x60
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0xf0
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x1d0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 2A531BB2-5E81-3D23-914E-6C809640C40A
+  UUID: DFC404BA-DB05-38BA-BCFD-0DC89C6AA2EE
   Functions: 18
   Symbols:   54
   CStrings:  48
Functions:
~ _create_alias_dir_config : 128 -> 124
~ _merge_alias_dir_config : 848 -> 724
~ _create_alias_config : 124 -> 120
~ _merge_alias_config : 160 -> 148
~ _add_alias : 472 -> 416
~ _add_alias_internal : 864 -> 740
~ _alias_matches : 388 -> 336
~ _add_redirect_internal : 1512 -> 1248
~ _translate_alias_redir : 1796 -> 1604
~ _fixup_redir : 1592 -> 1440
~ _try_redirect : 636 -> 568
~ _try_alias_list : 1272 -> 1136
~ _try_alias : 596 -> 536
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/mappers/mod_alias.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/mappers/mod_alias.c"

```
