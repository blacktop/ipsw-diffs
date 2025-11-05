## mod_remoteip.so

> `/usr/libexec/apache2/mod_remoteip.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x4994
+880.0.0.0.0
+  __TEXT.__text: 0x43f4
   __TEXT.__auth_stubs: 0x2f0
   __TEXT.__cstring: 0xd30
   __TEXT.__const: 0xc
-  __TEXT.__unwind_info: 0x80
+  __TEXT.__unwind_info: 0x90
   __DATA_CONST.__auth_got: 0x178
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: F3D1C0CB-F5F0-3652-B6D0-B054EBC6BD31
+  UUID: 595452E3-DBAE-32E2-8618-7F4492A2239C
   Functions: 24
   Symbols:   79
   CStrings:  68
Functions:
~ _merge_remoteip_server_config : 292 -> 260
~ _header_name_set : 76 -> 72
~ _proxies_header_name_set : 76 -> 72
~ _proxies_set : 704 -> 632
~ _proxylist_read : 564 -> 524
~ _remoteip_enable_proxy_protocol : 628 -> 572
~ _remoteip_disable_networks : 552 -> 496
~ _looks_like_ip : 196 -> 180
~ _remoteip_sockaddr_equal : 112 -> 108
~ _remoteip_warn_enable_conflict : 420 -> 384
~ _remoteip_addr_in_list : 136 -> 120
~ _remoteip_sockaddr_compat : 352 -> 284
~ _remoteip_input_filter : 3276 -> 3080
~ _remoteip_hook_post_config : 584 -> 556
~ _remoteip_hook_pre_connection : 1284 -> 1160
~ _remoteip_modify_request : 5892 -> 5332
~ _remoteip_determine_version : 188 -> 164
~ _remoteip_process_v1_header : 1880 -> 1832
~ _remoteip_process_v2_header : 1040 -> 1004
~ _remoteip_is_server_port : 160 -> 140
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/metadata/mod_remoteip.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/metadata/mod_remoteip.c"

```
