## mod_authz_dbd.so

> `/usr/libexec/apache2/mod_authz_dbd.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x15f4
+880.0.0.0.0
+  __TEXT.__text: 0x1480
   __TEXT.__auth_stubs: 0x190
   __TEXT.__cstring: 0x525
-  __TEXT.__unwind_info: 0x54
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0xc8
   __DATA_CONST.__const: 0xd0
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 4504AE73-7D12-3DD2-9E8F-2D82FF7DCD58
+  UUID: AEE69F1B-DBA7-3743-A1AE-1A3E3A2C90B5
   Functions: 11
   Symbols:   44
   CStrings:  37
Functions:
~ _authz_dbd_run_client_login : 272 -> 244
~ _authz_dbd_cr_cfg : 84 -> 80
~ _authz_dbd_merge_cfg : 292 -> 260
~ _authz_dbd_prepare : 308 -> 280
~ _dbdgroup_check_authorization : 504 -> 444
~ _dbd_parse_config : 252 -> 232
~ _authz_dbd_group_query : 1272 -> 1220
~ _dbdlogin_check_authorization : 164 -> 140
~ _authz_dbd_login : 2148 -> 2048
~ _dbdlogout_check_authorization : 164 -> 140
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authz_dbd.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authz_dbd.c"

```
