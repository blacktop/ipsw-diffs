## mod_authn_file.so

> `/usr/libexec/apache2/mod_authn_file.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x7b8
+880.0.0.0.0
+  __TEXT.__text: 0x710
   __TEXT.__auth_stubs: 0xc0
   __TEXT.__cstring: 0x1b7
-  __TEXT.__unwind_info: 0x50
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0x60
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 07AD37B0-EA30-3A7D-93E0-43D60B82501D
+  UUID: F1812BD6-4D86-3858-9328-D598E1B6DAC7
   Functions: 5
   Symbols:   24
   CStrings:  11
Functions:
~ _register_hooks : 112 -> 120
~ _check_password : 840 -> 760
~ _get_realm_hash : 916 -> 820
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authn_file.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authn_file.c"

```
