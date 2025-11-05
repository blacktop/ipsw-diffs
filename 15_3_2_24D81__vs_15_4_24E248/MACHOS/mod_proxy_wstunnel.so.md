## mod_proxy_wstunnel.so

> `/usr/libexec/apache2/mod_proxy_wstunnel.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x4e48
+880.0.0.0.0
+  __TEXT.__text: 0x4838
   __TEXT.__auth_stubs: 0x260
   __TEXT.__cstring: 0x540
-  __TEXT.__unwind_info: 0x64
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0x130
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 392A6F40-D0DC-341D-88FB-11D1FE91DF77
+  UUID: 6D7707F7-8E65-333B-B897-652465BF84BF
   Functions: 9
   Symbols:   52
   CStrings:  56
Functions:
~ _create_proxyws_dir_config : 84 -> 80
~ _merge_proxyws_dir_config : 304 -> 248
~ _proxyws_fallback_to_proxy_http : 100 -> 92
~ _proxy_wstunnel_post_config : 80 -> 76
~ _proxy_wstunnel_handler : 5620 -> 5176
~ _proxy_wstunnel_check_trans : 1152 -> 1028
~ _proxy_wstunnel_canon : 3360 -> 3084
~ _proxy_wstunnel_request : 9144 -> 8508
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_wstunnel.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/proxy/mod_proxy_wstunnel.c"

```
