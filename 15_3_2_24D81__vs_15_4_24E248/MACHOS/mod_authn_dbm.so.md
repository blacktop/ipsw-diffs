## mod_authn_dbm.so

> `/usr/libexec/apache2/mod_authn_dbm.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x584
+880.0.0.0.0
+  __TEXT.__text: 0x514
   __TEXT.__auth_stubs: 0xd0
   __TEXT.__cstring: 0x166
-  __TEXT.__unwind_info: 0x48
+  __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0x68
   __DATA_CONST.__const: 0x88
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 1134FA1A-8F10-38B4-A7EA-38FB54E10D59
+  UUID: 857CD12D-760E-39B6-BBF0-35100F786FB0
   Functions: 6
   Symbols:   25
   CStrings:  12
Functions:
~ _register_hooks : 112 -> 120
~ _check_dbm_pw : 356 -> 312
~ _get_dbm_realm_hash : 408 -> 372
~ _fetch_dbm_value : 412 -> 372
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authn_dbm.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authn_dbm.c"

```
