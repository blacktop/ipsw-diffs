## mod_allowmethods.so

> `/usr/libexec/apache2/mod_allowmethods.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x4cc
+880.0.0.0.0
+  __TEXT.__text: 0x460
   __TEXT.__auth_stubs: 0x60
   __TEXT.__cstring: 0x163
-  __TEXT.__unwind_info: 0x48
+  __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0x30
   __DATA_CONST.__const: 0x50
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: DD433FC0-A6F3-38F8-9749-5302C6983078
+  UUID: CB689E29-2A63-3901-8BAE-52F61C06FA0C
   Functions: 5
   Symbols:   13
   CStrings:  9
Functions:
~ _am_create_conf : 84 -> 80
~ _am_merge_conf : 184 -> 164
~ _am_allowmethods : 404 -> 372
~ _am_check_access : 488 -> 436
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_allowmethods.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_allowmethods.c"

```
