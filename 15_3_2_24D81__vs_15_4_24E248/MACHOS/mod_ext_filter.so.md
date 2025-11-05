## mod_ext_filter.so

> `/usr/libexec/apache2/mod_ext_filter.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x42c8
+880.0.0.0.0
+  __TEXT.__text: 0x3d18
   __TEXT.__auth_stubs: 0x400
   __TEXT.__cstring: 0x643
-  __TEXT.__unwind_info: 0x60
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0x200
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 21B49EB4-19AC-358B-A43F-3903122339D2
+  UUID: A679A8F7-C780-3CE9-AC16-29A0F5527CAF
   Functions: 20
   Symbols:   92
   CStrings:  63
Functions:
~ _create_ef_dir_conf : 84 -> 80
~ _merge_ef_dir_conf : 220 -> 200
~ _add_options : 308 -> 272
~ _define_filter : 1532 -> 1388
~ _parse_cmd : 672 -> 612
~ _ef_output_filter : 1800 -> 1660
~ _ef_input_filter : 796 -> 704
~ _init_filter_instance : 3152 -> 2880
~ _ef_unified_filter : 2704 -> 2488
~ _find_filter_def : 216 -> 204
~ _init_ext_filter_process : 1496 -> 1376
~ _get_cfg_string : 332 -> 276
~ _set_resource_limits : 280 -> 252
~ _child_errfn : 248 -> 244
~ _pass_data_to_filter : 1620 -> 1500
~ _drain_available_output : 1384 -> 1252
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_ext_filter.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_ext_filter.c"

```
