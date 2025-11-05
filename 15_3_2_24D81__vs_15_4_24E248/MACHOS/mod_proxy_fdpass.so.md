## mod_proxy_fdpass.so

> `/usr/libexec/apache2/mod_proxy_fdpass.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xc7c
+880.0.0.0.0
+  __TEXT.__text: 0xba8
   __TEXT.__auth_stubs: 0x140
   __TEXT.__cstring: 0x1a7
-  __TEXT.__unwind_info: 0x48
+  __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0xa0
   __DATA_CONST.__const: 0x18
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: C0FC3BBF-3594-3C5D-BF9A-97E1003BADA4
+  UUID: AC104390-8717-33DB-A817-C56AE13E8148
   Functions: 6
   Symbols:   28
   CStrings:  12
Functions:
~ _register_hooks : 152 -> 156
~ _proxy_fdpass_handler : 972 -> 916
~ _proxy_fdpass_canon : 1084 -> 992
~ _standard_flush : 376 -> 348
~ _get_socket_from_path : 192 -> 176
~ _send_socket : 420 -> 396
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_fdpass.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_fdpass.c"

```
