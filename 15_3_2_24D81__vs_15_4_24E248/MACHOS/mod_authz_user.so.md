## mod_authz_user.so

> `/usr/libexec/apache2/mod_authz_user.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x730
+880.0.0.0.0
+  __TEXT.__text: 0x69c
   __TEXT.__auth_stubs: 0x80
   __TEXT.__cstring: 0x196
   __TEXT.__const: 0x28
-  __TEXT.__unwind_info: 0x50
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0x40
   __DATA_CONST.__const: 0x20
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 78D04BF5-47B3-3D63-B9B1-04311FA67900
+  UUID: 0E0FCA10-0283-376D-9D79-CC878B36678C
   Functions: 5
   Symbols:   17
   CStrings:  8
Functions:
~ _user_check_authorization : 1328 -> 1208
~ _user_parse_config : 252 -> 232
~ _validuser_check_authorization : 76 -> 68
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authz_user.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authz_user.c"

```
