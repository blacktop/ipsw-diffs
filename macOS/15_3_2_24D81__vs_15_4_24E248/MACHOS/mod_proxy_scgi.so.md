## mod_proxy_scgi.so

> `/usr/libexec/apache2/mod_proxy_scgi.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x2acc
+880.0.0.0.0
+  __TEXT.__text: 0x2758
   __TEXT.__auth_stubs: 0x2d0
   __TEXT.__cstring: 0x3c4
-  __TEXT.__unwind_info: 0x68
+  __TEXT.__unwind_info: 0x78
   __DATA_CONST.__auth_got: 0x168
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0xb0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 3530BA86-D657-319B-83D5-13F864CF2D07
+  UUID: 9A84B9EE-D3F3-397C-9BF2-EC084A01F37E
   Functions: 15
   Symbols:   71
   CStrings:  39
Functions:
~ _merge_scgi_config : 224 -> 200
~ _register_hooks : 176 -> 172
~ _scgi_set_send_file : 180 -> 160
~ _scgi_set_internal_redirect : 180 -> 160
~ _scgi_handler : 1620 -> 1464
~ _scgi_canon : 892 -> 804
~ _scgi_request_status : 2344 -> 2152
~ _send_headers : 1200 -> 1140
~ _send_request_body : 384 -> 340
~ _pass_response : 2492 -> 2284
~ _sendall : 360 -> 332
~ _bucket_socket_ex_read : 616 -> 576
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_scgi.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_scgi.c"

```
