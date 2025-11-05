## mod_proxy_connect.so

> `/usr/libexec/apache2/mod_proxy_connect.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x2f10
+880.0.0.0.0
+  __TEXT.__text: 0x2ba4
   __TEXT.__auth_stubs: 0x240
   __TEXT.__cstring: 0x3a8
-  __TEXT.__unwind_info: 0x54
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0x120
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 42FEA220-1171-338B-A81A-B60377F4B97E
+  UUID: 87264492-D827-3B08-B27F-6544440C00C1
   Functions: 7
   Symbols:   48
   CStrings:  27
Functions:
~ _create_config : 88 -> 84
~ _merge_config : 124 -> 112
~ _set_allowed_ports : 400 -> 364
~ _proxy_connect_handler : 10036 -> 9328
~ _proxy_connect_canon : 980 -> 892
~ _allowed_port : 308 -> 280
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_connect.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_connect.c"

```
