## mod_proxy_hcheck.so

> `/usr/libexec/apache2/mod_proxy_hcheck.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x7494
+880.0.0.0.0
+  __TEXT.__text: 0x6bc0
   __TEXT.__auth_stubs: 0x550
   __TEXT.__cstring: 0xb87
-  __TEXT.__unwind_info: 0x74
+  __TEXT.__unwind_info: 0x80
   __DATA_CONST.__auth_got: 0x2a8
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 69769C7E-6BE9-3787-8242-B2E8012E6ED4
+  UUID: 378A2DAD-C747-3063-A83D-C5489E5B07BD
   Functions: 32
   Symbols:   131
   CStrings:  110
Functions:
~ _hc_create_config : 208 -> 196
~ _hc_register_hooks : 364 -> 348
~ _set_hc_template : 668 -> 620
~ _set_hc_condition : 732 -> 664
~ _set_hc_tpsize : 156 -> 136
~ _set_worker_hc_param : 1948 -> 1724
~ _hc_show_exprs : 436 -> 404
~ _hc_select_exprs : 468 -> 424
~ _hc_valid_expr : 340 -> 300
~ _hc_pre_config : 212 -> 188
~ _hc_post_config : 1732 -> 1648
~ _hc_expr_lookup : 304 -> 276
~ _ap_rputs : 212 -> 200
~ _hc_watchdog_callback : 4184 -> 3972
~ _hc_init_baton : 552 -> 456
~ _hc_check : 2264 -> 2104
~ _hc_get_hcworker : 2396 -> 2276
~ _hc_get_backend : 416 -> 364
~ _create_hcheck_req : 832 -> 752
~ _hc_determine_connection : 632 -> 588
~ _hc_check_tcp : 188 -> 168
~ _hc_check_cping : 1604 -> 1464
~ _hc_check_http : 3108 -> 2904
~ _backend_cleanup : 660 -> 612
~ _create_request_rec : 752 -> 716
~ _hc_send : 800 -> 740
~ _hc_read_headers : 1760 -> 1632
~ _hc_read_body : 1056 -> 960
~ _hc_expr_var_fn : 180 -> 144
~ _hc_expr_func_fn : 184 -> 148
~ _hc_get_body : 320 -> 280
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_hcheck.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_hcheck.c"

```
