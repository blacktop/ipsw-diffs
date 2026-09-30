## mod_authz_dbm.so

> `/usr/libexec/apache2/mod_authz_dbm.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xc94
+880.0.0.0.0
+  __TEXT.__text: 0xba0
   __TEXT.__auth_stubs: 0x120
   __TEXT.__cstring: 0x43b
-  __TEXT.__unwind_info: 0x48
+  __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0x90
   __DATA_CONST.__const: 0x98
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 0B300FF1-D535-34A8-9066-82E93BDD2120
+  UUID: 4C69CAF5-ED3E-3B19-B05D-65881CCBC0C1
   Functions: 8
   Symbols:   33
   CStrings:  21
Functions:
~ _register_hooks : 160 -> 168
~ _dbmgroup_check_authorization : 1136 -> 1052
~ _dbm_parse_config : 252 -> 232
~ _get_dbm_grp : 520 -> 452
~ _get_dbm_entry_as_str : 176 -> 160
~ _dbmfilegroup_check_authorization : 852 -> 788
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authz_dbm.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authz_dbm.c"

```
