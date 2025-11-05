## mod_proxy_uwsgi.so

> `/usr/libexec/apache2/mod_proxy_uwsgi.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x2040
+880.0.0.0.0
+  __TEXT.__text: 0x1d50
   __TEXT.__auth_stubs: 0x3a0
   __TEXT.__cstring: 0x2d0
   __TEXT.__const: 0x8
-  __TEXT.__unwind_info: 0x5c
+  __TEXT.__unwind_info: 0x68
   __DATA_CONST.__auth_got: 0x1d0
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: A0B40806-8972-320A-BE2C-98ED72EA6399
+  UUID: 66AA7290-EB9D-3F43-B113-AB0AE79E4B85
   Functions: 8
   Symbols:   72
   CStrings:  28
Functions:
~ _uwsgi_handler : 2084 -> 1832
~ _uwsgi_canon : 1040 -> 928
~ _uwsgi_send_headers : 1448 -> 1360
~ _uwsgi_send_body : 372 -> 336
~ _uwsgi_response : 2396 -> 2152
~ _uwsgi_send : 348 -> 328
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_uwsgi.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_uwsgi.c"

```
