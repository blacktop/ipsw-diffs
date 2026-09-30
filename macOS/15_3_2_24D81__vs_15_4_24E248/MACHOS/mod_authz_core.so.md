## mod_authz_core.so

> `/usr/libexec/apache2/mod_authz_core.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x360c
+880.0.0.0.0
+  __TEXT.__text: 0x30dc
   __TEXT.__auth_stubs: 0x250
   __TEXT.__cstring: 0xa3a
-  __TEXT.__unwind_info: 0x80
+  __TEXT.__unwind_info: 0x90
   __DATA_CONST.__auth_got: 0x128
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 0E0F2F21-4767-3CFC-BACA-0A2DD17F93A0
+  UUID: C88100EF-7F69-394C-B12E-6E2C2D620D27
   Functions: 29
   Symbols:   76
   CStrings:  72
Functions:
~ _merge_authz_core_dir_config : 696 -> 624
~ _register_hooks : 412 -> 408
~ _authz_require_alias_section : 1292 -> 1172
~ _add_authz_provider : 916 -> 836
~ _add_authz_section : 1216 -> 1092
~ _authz_merge_sections : 268 -> 240
~ _authz_alias_check_authorization : 496 -> 452
~ _format_authz_command : 456 -> 380
~ _authz_some_auth_required : 144 -> 132
~ _authz_core_check_config : 192 -> 164
~ _authz_core_check_section : 804 -> 680
~ _authorize_user_core : 1916 -> 1772
~ _apply_authz_sections : 2640 -> 2376
~ _format_authz_result : 152 -> 128
~ _env_check_authorization : 204 -> 184
~ _all_check_authorization : 68 -> 60
~ _all_parse_config : 152 -> 136
~ _method_check_authorization : 104 -> 96
~ _method_parse_config : 328 -> 304
~ _expr_check_authorization : 328 -> 276
~ _expr_parse_config : 464 -> 424
~ _expr_lookup_fn : 144 -> 128
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authz_core.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authz_core.c"

```
