## mod_proxy_balancer.so

> `/usr/libexec/apache2/mod_proxy_balancer.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xc228
+880.0.0.0.0
+  __TEXT.__text: 0xb1d4
   __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__const: 0x8
   __TEXT.__cstring: 0x25ff
-  __TEXT.__unwind_info: 0x98
+  __TEXT.__unwind_info: 0xa8
   __DATA_CONST.__auth_got: 0x350
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: CC88BCBB-E6DC-31A4-A72D-66CFB98CC357
+  UUID: 488C1564-AC0E-3037-B28B-85A25CFA7D6E
   Functions: 28
   Symbols:   148
   CStrings:  315
Functions:
~ _ap_proxy_balancer_register_hook : 356 -> 352
~ _balancer_manage : 3888 -> 3584
~ _balancer_post_config : 4424 -> 4232
~ _balancer_pre_config : 200 -> 192
~ _balancer_handler : 2848 -> 2568
~ _balancer_child_init : 652 -> 592
~ _proxy_balancer_pre_request : 3600 -> 3312
~ _proxy_balancer_post_request : 2084 -> 1928
~ _proxy_balancer_canon : 1272 -> 1176
~ _balancer_process_balancer_worker : 7776 -> 6900
~ _recalc_factors : 208 -> 200
~ _make_servers_ids : 660 -> 592
~ _lock_remove : 236 -> 212
~ _make_server_id : 780 -> 712
~ _push2table : 424 -> 372
~ _safe_referer : 172 -> 152
~ _balancer_display_page : 10692 -> 9936
~ _ap_rputs : 212 -> 200
~ _create_radio : 320 -> 304
~ _init_balancer_members : 832 -> 764
~ _force_recovery : 956 -> 880
~ _find_session_route : 4176 -> 3820
~ _find_best_worker : 824 -> 716
~ _decrement_busy_count : 84 -> 72
~ _balancer_fixup : 252 -> 236
~ _get_path_param : 320 -> 284
~ _get_cookie_param : 580 -> 496
~ _find_route_worker : 876 -> 740
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_balancer.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_balancer.c"

```
