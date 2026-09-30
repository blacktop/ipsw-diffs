## mod_proxy_http.so

> `/usr/libexec/apache2/mod_proxy_http.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xa018
+880.0.0.0.0
+  __TEXT.__text: 0x91b0
   __TEXT.__auth_stubs: 0x600
   __TEXT.__cstring: 0xd68
-  __TEXT.__unwind_info: 0x6c
+  __TEXT.__unwind_info: 0x78
   __DATA_CONST.__auth_got: 0x300
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 54F479E5-F12B-3C95-AD12-1D41162DBBE4
+  UUID: 7E2639CC-04FF-39B1-AAE3-94FDC32A4CEF
   Functions: 23
   Symbols:   131
   CStrings:  129
Functions:
~ _proxy_http_post_config : 268 -> 236
~ _proxy_http_handler : 6020 -> 5356
~ _proxy_http_canon : 2316 -> 2104
~ _get_url_scheme : 564 -> 508
~ _ap_proxy_http_prefetch : 3028 -> 2648
~ _ap_proxy_http_request : 576 -> 512
~ _ap_proxy_http_process_response : 19076 -> 17420
~ _add_te_chunked : 260 -> 252
~ _add_cl : 232 -> 228
~ _terminate_headers : 716 -> 668
~ _stream_reqbody : 1808 -> 1620
~ _ap_proxygetline : 196 -> 180
~ _ap_proxy_read_headers : 3260 -> 3068
~ _ap_proxy_clean_warnings : 224 -> 216
~ _send_continue_body : 504 -> 452
~ _add_trailers : 84 -> 76
~ _process_proxy_header : 412 -> 380
~ _date_canon : 172 -> 152
~ _clean_warning_headers : 472 -> 424
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_http.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_http.c"

```
