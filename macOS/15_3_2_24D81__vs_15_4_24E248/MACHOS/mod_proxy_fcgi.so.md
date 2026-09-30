## mod_proxy_fcgi.so

> `/usr/libexec/apache2/mod_proxy_fcgi.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x6634
+880.0.0.0.0
+  __TEXT.__text: 0x5d5c
   __TEXT.__auth_stubs: 0x4d0
   __TEXT.__cstring: 0x7e8
-  __TEXT.__unwind_info: 0x6c
+  __TEXT.__unwind_info: 0x78
   __DATA_CONST.__auth_got: 0x268
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: ADAEEACA-86D6-38D1-AE68-DE02A5145FDA
+  UUID: 6D5FA754-6AC9-330A-A017-5A31C583BCB5
   Functions: 16
   Symbols:   99
   CStrings:  71
Functions:
~ _fcgi_merge_dconf : 196 -> 188
~ _cmd_servertype : 180 -> 160
~ _cmd_setenv : 660 -> 600
~ _proxy_fcgi_handler : 4576 -> 4160
~ _proxy_fcgi_canon : 4380 -> 3992
~ _fcgi_do_request : 1964 -> 1808
~ _send_begin_request : 292 -> 272
~ _send_environment : 3260 -> 2944
~ _dispatch : 5904 -> 5412
~ _send_data : 592 -> 536
~ _fix_cgivars : 3204 -> 2944
~ _get_data_full : 192 -> 176
~ _get_data : 128 -> 116
~ _handle_headers : 424 -> 380
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_fcgi.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_fcgi.c"

```
