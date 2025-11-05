## mod_info.so

> `/usr/libexec/apache2/mod_info.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x2818
+880.0.0.0.0
+  __TEXT.__text: 0x24a4
   __TEXT.__auth_stubs: 0x210
   __TEXT.__cstring: 0x1438
-  __TEXT.__unwind_info: 0x5c
+  __TEXT.__unwind_info: 0x68
   __DATA_CONST.__auth_got: 0x108
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x340

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 52AB6E4F-D41C-3646-B428-91ED945045EB
+  UUID: 355119C9-4835-36C9-A982-8268A68D07A7
   Functions: 29
   Symbols:   116
   CStrings:  160
Functions:
~ _create_info_config : 88 -> 84
~ _merge_info_config : 124 -> 112
~ _add_module_info : 152 -> 128
~ _display_info : 2632 -> 2308
~ _check_config : 128 -> 120
~ _ap_rputs : 212 -> 200
~ _get_sorted_modules : 196 -> 184
~ _show_server_settings : 1200 -> 1172
~ _show_active_hooks : 560 -> 536
~ _show_providers : 604 -> 556
~ _mod_info_module_cmds : 388 -> 344
~ _module_find_hook : 232 -> 208
~ _module_request_hook_participate : 216 -> 196
~ _find_more_info : 252 -> 224
~ _cmp_module_name : 88 -> 80
~ _dump_a_hook : 368 -> 336
~ _cmp_provider_groups : 140 -> 120
~ _cmp_provider_names : 80 -> 72
~ _set_fn_info : 88 -> 80
~ _mod_info_show_close : 352 -> 328
~ _mod_info_has_cmd : 188 -> 164
~ _mod_info_show_parents : 116 -> 112
~ _mod_info_show_cmd : 244 -> 236
~ _mod_info_indent : 684 -> 612
~ _get_fn_info : 88 -> 80
~ _put_int_flush_right : 304 -> 272
~ _mod_info_show_open : 244 -> 236
~ _module_participate : 188 -> 172
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/generators/mod_info.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/generators/mod_info.c"

```
