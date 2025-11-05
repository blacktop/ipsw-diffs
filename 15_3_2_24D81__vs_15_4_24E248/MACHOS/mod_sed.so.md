## mod_sed.so

> `/usr/libexec/apache2/mod_sed.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x9f70
+880.0.0.0.0
+  __TEXT.__text: 0x9130
   __TEXT.__auth_stubs: 0x280
   __TEXT.__cstring: 0x5d3
   __TEXT.__const: 0x5
-  __TEXT.__unwind_info: 0xc8
+  __TEXT.__unwind_info: 0xd8
   __DATA_CONST.__auth_got: 0x140
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x178

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 1A86AA20-44E1-335E-8C55-0669B526A0E8
+  UUID: 557007D3-9669-3B83-B9AF-92E9AB4A51E1
   Functions: 69
   Symbols:   115
   CStrings:  83
Functions:
~ _create_sed_dir_config : 72 -> 68
~ _sed_add_expr : 164 -> 148
~ _compile_sed_expr : 296 -> 268
~ _sed_compile_errf : 48 -> 44
~ _sed_response_filter : 1460 -> 1312
~ _sed_request_filter : 1748 -> 1612
~ _init_context : 440 -> 420
~ _flush_output_buffer : 208 -> 188
~ _log_sed_errf : 180 -> 160
~ _sed_write_output : 564 -> 512
~ _sed_eval_cleanup : 56 -> 52
~ _append_bucket : 604 -> 580
~ _command_errf : 156 -> 140
~ _sed_init_commands : 368 -> 352
~ _alloc_reptr : 272 -> 256
~ _sed_compile_string : 160 -> 140
~ _fcomp : 6880 -> 6320
~ _check_finalized : 192 -> 164
~ _sed_compile_file : 96 -> 72
~ _sed_get_finalize_error : 272 -> 244
~ _rline : 1200 -> 1068
~ _address : 864 -> 828
~ _search : 160 -> 148
~ _dechain : 196 -> 164
~ _text : 448 -> 420
~ _comple : 160 -> 156
~ _compsub : 568 -> 536
~ _ycomp : 996 -> 916
~ _sed_reset_eval : 852 -> 808
~ _eval_errf : 156 -> 140
~ _sed_destroy_eval : 172 -> 160
~ _sed_eval_file : 272 -> 240
~ _sed_eval_buffer : 760 -> 640
~ _sed_finalize_eval : 360 -> 312
~ _execute : 1732 -> 1504
~ _appendmem_to_linebuf : 220 -> 200
~ _append_to_linebuf : 408 -> 352
~ _grow_buffer : 496 -> 440
~ _match : 204 -> 188
~ _command : 4600 -> 4152
~ _wline : 164 -> 152
~ _arout : 640 -> 564
~ _append_to_holdbuf : 240 -> 216
~ _substitute : 344 -> 296
~ _copy_to_genbuf : 204 -> 180
~ _dosub : 872 -> 788
~ _place : 240 -> 212
~ _grow_gen_buffer : 172 -> 152
~ _append_to_genbuf : 248 -> 224
~ _sed_compile : 3300 -> 2964
~ _regerr : 368 -> 364
~ _sed_step : 384 -> 336
~ __advance : 2832 -> 2552
~ _getrnge : 120 -> 116
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_sed.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_sed.c"

```
