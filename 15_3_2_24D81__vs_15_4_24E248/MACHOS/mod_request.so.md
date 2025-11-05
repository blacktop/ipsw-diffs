## mod_request.so

> `/usr/libexec/apache2/mod_request.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x1104
+880.0.0.0.0
+  __TEXT.__text: 0xf8c
   __TEXT.__auth_stubs: 0x150
   __TEXT.__cstring: 0x2c8
-  __TEXT.__unwind_info: 0x50
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0xa8
   __DATA_CONST.__const: 0x50
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: E8C342B9-7CD0-32F4-98B1-C09442A9EAEA
+  UUID: 2EBE8BB0-CAC5-3D4A-BCEC-F188F7C2C106
   Functions: 11
   Symbols:   36
   CStrings:  15
Functions:
~ _create_request_dir_config : 84 -> 80
~ _merge_request_dir_config : 236 -> 208
~ _register_hooks : 276 -> 268
~ _set_kept_body_size : 188 -> 152
~ _keep_body_filter : 1444 -> 1332
~ _kept_body_filter : 1052 -> 964
~ _kept_body_filter_init : 184 -> 164
~ _ap_request_insert_filter : 252 -> 216
~ _ap_request_remove_filter : 196 -> 176
~ _bail_out_on_error : 316 -> 308
~ _request_is_filter_present : 128 -> 112
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_request.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_request.c"

```
