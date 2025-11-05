## mod_authz_owner.so

> `/usr/libexec/apache2/mod_authz_owner.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xbe8
+880.0.0.0.0
+  __TEXT.__text: 0xb3c
   __TEXT.__auth_stubs: 0xa0
   __TEXT.__cstring: 0x3f2
   __TEXT.__const: 0x28
-  __TEXT.__unwind_info: 0x50
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0x50
   __DATA_CONST.__const: 0x10
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 226E7275-57A2-3FC0-873A-9BA8E0BD8F34
+  UUID: FBBB2605-429E-3F5B-B096-13345C0B4841
   Functions: 3
   Symbols:   16
   CStrings:  22
Functions:
~ _register_hooks : 128 -> 124
~ _authz_owner_get_file_group : 1324 -> 1248
~ _fileowner_check_authorization : 1596 -> 1504
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authz_owner.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authz_owner.c"

```
