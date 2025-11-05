## mod_proxy.so

> `/usr/libexec/apache2/mod_proxy.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x2c360
+880.0.0.0.0
+  __TEXT.__text: 0x280d8
   __TEXT.__auth_stubs: 0x1130
-  __TEXT.__const: 0x10
   __TEXT.__cstring: 0x4cd6
-  __TEXT.__unwind_info: 0x1ac
+  __TEXT.__unwind_info: 0x1b8
   __DATA_CONST.__auth_got: 0x898
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: A79F8B8C-8391-389B-9F8E-76D7C49D11A7
+  UUID: F2F2D881-8D1A-3CBE-BA7C-D46898F26EA4
   Functions: 194
   Symbols:   449
   CStrings:  607
Functions:
~ _ap_proxy_trans_match : 6576 -> 5688
~ _alias_match_servlet : 2592 -> 2308
~ _alias_match : 640 -> 568
~ _proxy_run_check_trans : 236 -> 216
~ _ap_proxy_de_socketfy : 276 -> 240
~ _ap_proxy_ssl_enable : 104 -> 92
~ _ap_proxy_ssl_disable : 60 -> 56
~ _ap_proxy_ssl_engine : 112 -> 100
~ _create_proxy_dir_config : 376 -> 372
~ _merge_proxy_dir_config : 1528 -> 1284
~ _create_proxy_config : 792 -> 788
~ _merge_proxy_config : 3152 -> 2760
~ _proxy_hook_scheme_handler : 264 -> 248
~ _proxy_run_scheme_handler : 256 -> 236
~ _proxy_hook_check_trans : 272 -> 256
~ _proxy_hook_canon_handler : 272 -> 256
~ _proxy_run_canon_handler : 236 -> 216
~ _proxy_hook_pre_request : 272 -> 256
~ _proxy_run_pre_request : 260 -> 240
~ _proxy_hook_post_request : 272 -> 256
~ _proxy_run_post_request : 252 -> 232
~ _proxy_run_section_post_config : 288 -> 260
~ _proxy_run_fixups : 256 -> 228
~ _proxy_run_request_status : 264 -> 236
~ _merge_balancers : 1968 -> 1620
~ _proxysection : 2164 -> 1900
~ _set_proxy_req : 96 -> 92
~ _add_pass_reverse : 440 -> 376
~ _cookie_path : 160 -> 144
~ _cookie_domain : 160 -> 144
~ _set_proxy_exclude : 384 -> 332
~ _set_recv_buffer_size : 192 -> 172
~ _set_io_buffer_size : 236 -> 208
~ _set_max_forwards : 140 -> 120
~ _set_proxy_dirconn : 472 -> 412
~ _set_proxy_domain : 124 -> 116
~ _set_via_opt : 324 -> 288
~ _set_proxy_error_override : 656 -> 588
~ _set_preserve_host : 88 -> 84
~ _set_proxy_timeout : 184 -> 176
~ _set_bad_opt : 272 -> 244
~ _add_member : 3116 -> 2904
~ _set_bgrowth : 192 -> 172
~ _set_persist : 92 -> 88
~ _set_inherit : 112 -> 108
~ _set_ppinherit : 112 -> 108
~ _set_status_opt : 272 -> 244
~ _set_proxy_param : 1416 -> 1236
~ _set_source_address : 200 -> 180
~ _add_proxy_http_headers : 88 -> 84
~ _forward_100_continue : 88 -> 84
~ _ap_add_per_proxy_conf : 100 -> 92
~ _set_worker_param : 4388 -> 3824
~ _set_balancer_param : 2356 -> 2096
~ _add_proxy : 956 -> 848
~ _add_pass : 3336 -> 2976
~ _proxy_handler : 7484 -> 6740
~ _proxy_map_location : 200 -> 168
~ _proxy_fixup : 152 -> 128
~ _proxy_detect : 624 -> 532
~ _proxy_pre_config : 344 -> 312
~ _proxy_post_config : 656 -> 588
~ _child_init : 1296 -> 1220
~ _proxy_needsdomain : 1460 -> 1308
~ _proxy_trans : 816 -> 672
~ _proxy_walk : 1000 -> 864
~ _proxy_status_hook : 1988 -> 1884
~ _ap_rputs : 212 -> 200
~ _proxy_run_create_req : 264 -> 236
~ _ap_proxy_strncpy : 204 -> 180
~ _ap_proxy_hex2c : 320 -> 284
~ _ap_proxy_c2hex : 184 -> 176
~ _ap_proxy_canonenc_ex : 1176 -> 1024
~ _ap_proxy_canonenc : 116 -> 104
~ _ap_proxy_canon_netloc : 828 -> 720
~ _proxyerror_core : 372 -> 352
~ _ap_proxy_is_ipaddr : 1696 -> 1552
~ _proxy_match_ipaddr : 596 -> 548
~ _ap_proxy_is_domainname : 436 -> 404
~ _proxy_match_domainname : 416 -> 388
~ _ap_proxy_is_hostname : 496 -> 456
~ _proxy_match_hostname : 424 -> 388
~ _proxy_match_word : 120 -> 108
~ _ap_proxy_checkproxyblock2 : 2588 -> 2388
~ _ap_proxy_location_reverse_map : 1804 -> 1608
~ _ap_proxy_valid_balancer_name : 100 -> 88
~ _ap_proxy_get_balancer : 516 -> 440
~ _ap_proxy_cookie_reverse_map : 1912 -> 1764
~ _ap_proxy_hashfunc : 352 -> 312
~ _ap_proxy_update_balancer : 388 -> 340
~ _ap_proxy_define_balancer : 1060 -> 976
~ _ap_proxy_share_balancer : 1232 -> 1140
~ _ap_proxy_initialize_balancer : 996 -> 936
~ _proxy_balancer_get_best_worker : 2380 -> 2144
~ _ap_proxy_connection_reusable : 196 -> 148
~ _ap_proxy_ssl_connection_cleanup : 1168 -> 1052
~ _ap_proxy_worker_name : 188 -> 172
~ _ap_proxy_worker_can_upgrade : 288 -> 252
~ _ap_proxy_get_worker_ex : 1364 -> 1124
~ _ap_proxy_strcmp_ematch : 648 -> 580
~ _ap_proxy_define_worker_ex : 3852 -> 3500
~ _ap_proxy_port_of_scheme : 228 -> 196
~ _ap_proxy_define_worker : 116 -> 104
~ _ap_proxy_define_match_worker : 116 -> 104
~ _ap_proxy_share_worker : 1288 -> 1188
~ _ap_proxy_initialize_worker : 4688 -> 4384
~ _connection_constructor : 148 -> 144
~ _connection_destructor : 108 -> 92
~ _fixup_uds_filename : 1836 -> 1648
~ _ap_proxy_interpolate : 444 -> 420
~ _ap_proxy_canon_url : 600 -> 528
~ _proxy_vars : 404 -> 372
~ _ap_proxy_pre_request : 3288 -> 3036
~ _ap_proxy_post_request : 132 -> 116
~ _ap_proxy_connect_to_backend : 3800 -> 3496
~ _ap_proxy_acquire_connection : 1288 -> 1208
~ _ap_proxy_retry_worker : 1660 -> 1584
~ _ap_proxy_release_connection : 544 -> 512
~ _connection_cleanup : 760 -> 612
~ _ap_proxy_determine_address : 6008 -> 5432
~ _worker_address_resolve : 4332 -> 4000
~ _proxy_addrs_equal : 320 -> 268
~ _worker_address_set : 116 -> 100
~ _proxy_address_inc : 120 -> 108
~ _conn_cleanup : 120 -> 112
~ _ap_proxy_determine_connection : 5580 -> 4888
~ _ap_proxy_is_socket_connected : 452 -> 400
~ _ap_proxy_connect_uds : 536 -> 484
~ _ap_proxy_check_connection : 2384 -> 2196
~ _ap_proxy_connect_backend : 6284 -> 5836
~ _send_http_connect : 2076 -> 1960
~ _proxy_connection_create : 2580 -> 2432
~ _ap_proxy_lb_workers : 60 -> 52
~ _ap_proxy_should_override : 208 -> 184
~ _error_code_overridden : 264 -> 232
~ _ap_proxy_backend_broke : 336 -> 316
~ _ap_proxy_set_wstatus : 264 -> 232
~ _ap_proxy_parse_wstatus : 352 -> 308
~ _ap_proxy_sync_balancer : 2292 -> 2152
~ _ap_proxy_find_workershm : 284 -> 264
~ _ap_proxy_find_balancershm : 284 -> 264
~ _ap_proxy_create_hdrbrgd : 3540 -> 3168
~ _ap_proxy_clear_connection : 312 -> 280
~ _ap_proxy_prefetch_input : 1240 -> 1144
~ _ap_proxy_read_input : 720 -> 624
~ _ap_proxy_pass_brigade : 652 -> 568
~ _ap_proxy_spool_input : 1704 -> 1560
~ _ap_proxy_buckets_lifetime_transform : 756 -> 700
~ _ap_proxy_transfer_between_connections : 4652 -> 4252
~ _ap_filter_output_pending : 184 -> 152
~ _ap_proxy_tunnel_create : 1668 -> 1576
~ _ap_proxy_tunnel_run : 9808 -> 9064
~ _del_pollset : 232 -> 200
~ _add_pollset : 212 -> 180
~ _proxy_tunnel_forward : 4492 -> 4160
~ _ap_proxy_show_hcmethod : 144 -> 128
~ _proxy_util_register_hooks : 276 -> 252
~ _proxy_get_host_of_request : 452 -> 388
~ _make_conn_subpool : 404 -> 356
~ _proxy_address_dec : 144 -> 132
~ _connection_shutdown : 888 -> 792
~ _find_conn_headers : 392 -> 352
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/proxy_util.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/proxy_util.c"

```
