## mod_authz_groupfile.so

> `/usr/libexec/apache2/mod_authz_groupfile.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x14f0
+880.0.0.0.0
+  __TEXT.__text: 0x1378
   __TEXT.__auth_stubs: 0x1c0
   __TEXT.__cstring: 0x426
-  __TEXT.__unwind_info: 0x54
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0xe0
   __DATA_CONST.__const: 0x70
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 54F14F03-48B8-39B4-85D8-07193E194A60
+  UUID: B72C1697-0849-3C28-BA07-A0F498DDC569
   Functions: 7
   Symbols:   41
   CStrings:  20
Functions:
~ _register_hooks : 160 -> 168
~ _group_check_authorization : 2604 -> 2412
~ _groupfile_parse_config : 252 -> 232
~ _groups_for_user : 632 -> 576
~ _filegroup_check_authorization : 1604 -> 1488
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authz_groupfile.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authz_groupfile.c"

```
