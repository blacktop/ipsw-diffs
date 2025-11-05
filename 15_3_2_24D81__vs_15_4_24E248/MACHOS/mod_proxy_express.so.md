## mod_proxy_express.so

> `/usr/libexec/apache2/mod_proxy_express.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x1b74
+880.0.0.0.0
+  __TEXT.__text: 0x197c
   __TEXT.__auth_stubs: 0x110
   __TEXT.__cstring: 0x286
-  __TEXT.__unwind_info: 0x64
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0x88
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0xa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 1D460636-EBD5-3B6B-B1B1-24B826D39B07
+  UUID: 940DB374-FAF9-3F7C-914F-45964828C00A
   Functions: 8
   Symbols:   29
   CStrings:  19
Functions:
~ _server_merge : 304 -> 280
~ _set_dbmfile : 180 -> 168
~ _post_config : 80 -> 76
~ _xlate_name : 6100 -> 5636
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_express.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_express.c"

```
