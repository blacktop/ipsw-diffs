## mod_autoindex.so

> `/usr/libexec/apache2/mod_autoindex.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x72ac
+880.0.0.0.0
+  __TEXT.__text: 0x656c
   __TEXT.__auth_stubs: 0x4f0
   __TEXT.__cstring: 0xf1d
-  __TEXT.__unwind_info: 0x74
+  __TEXT.__unwind_info: 0x80
   __DATA_CONST.__auth_got: 0x278
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 9B53CD5A-3F40-310D-92BA-8E1C9FE8CBFF
+  UUID: D87429B2-AC3F-38FD-981D-3508ED80557D
   Functions: 29
   Symbols:   119
   CStrings:  198
Functions:
~ _create_autoindex_config : 288 -> 284
~ _merge_autoindex_configs : 1544 -> 1416
~ _add_icon : 420 -> 380
~ _add_alt : 244 -> 224
~ _add_opts : 2748 -> 2372
~ _set_default_order : 404 -> 352
~ _add_desc : 396 -> 348
~ _push_item : 352 -> 320
~ _handle_autoindex : 692 -> 616
~ _index_directory : 3624 -> 3172
~ _emit_head : 1180 -> 1008
~ _make_parent_entry : 680 -> 592
~ _make_autoindex_entry : 1636 -> 1424
~ _dsortf : 1172 -> 1012
~ _output_directories : 8184 -> 7328
~ _emit_tail : 652 -> 532
~ _response_is_html : 140 -> 128
~ _emit_preamble : 404 -> 368
~ _do_emit_plain : 692 -> 628
~ _ap_rputs : 212 -> 200
~ _ignore_entry : 376 -> 320
~ _find_item : 616 -> 520
~ _find_desc : 428 -> 372
~ _find_title : 928 -> 820
~ _emit_link : 416 -> 392
~ _terminate_description : 692 -> 600
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/generators/mod_autoindex.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/generators/mod_autoindex.c"

```
