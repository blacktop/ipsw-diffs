## libapple_nghttp2.dylib

> `/usr/lib/libapple_nghttp2.dylib`

```diff

-37.0.0.0.0
-  __TEXT.__text: 0xfe44
+37.120.1.0.0
+  __TEXT.__text: 0x100ec
   __TEXT.__auth_stubs: 0xd0
   __TEXT.__const: 0x5860
   __TEXT.__cstring: 0x2022

   __DATA.__bss: 0x80
   __DATA_DIRTY.__data: 0x28
   - /usr/lib/libSystem.B.dylib
-  UUID: D5601B78-1165-3122-BE8C-DF904BABCF80
+  UUID: C9560DD2-7DBD-33CE-93FA-041E42B359EB
   Functions: 299
   Symbols:   431
   CStrings:  317
Functions:
~ _session_new : 1440 -> 1472
~ _default_calloc : 12 -> 4
~ _default_malloc : 12 -> 4
~ _buf_chain_new : 212 -> 248
~ _nghttp2_hd_inflate_init : 176 -> 188
~ _default_realloc : 12 -> 4
~ _nghttp2_session_add_settings : 860 -> 924
~ _nghttp2_nv_array_copy : 428 -> 444
~ _submit_headers_shared_nva : 388 -> 404
~ _nghttp2_session_add_window_update : 168 -> 184
~ _nghttp2_session_mem_recv2 : 12692 -> 12704
~ _nghttp2_submit_data_shared : 204 -> 220
~ _nghttp2_pq_push : 160 -> 176
~ _nghttp2_hd_deflate_hd_bufs : 1440 -> 1444
~ _nghttp2_hd_inflate_hd_nv : 1600 -> 1640
~ _nghttp2_session_open_stream : 604 -> 620
~ _add_hd_table_incremental : 732 -> 764
~ _nghttp2_session_add_goaway : 368 -> 400
~ _emit_indname_block : 396 -> 400
~ _emit_string : 740 -> 744
~ _map_resize : 256 -> 272
~ _emit_table_size : 220 -> 224
~ _nghttp2_hd_deflate_hd2 : 260 -> 276
~ _nghttp2_hd_deflate_hd_vec2 : 400 -> 416
~ _nghttp2_hd_deflate_new2 : 216 -> 248
~ _nghttp2_hd_inflate_new2 : 128 -> 144
~ _nghttp2_rcbuf_new2 : 140 -> 156
~ _nghttp2_submit_push_promise : 344 -> 360
~ _nghttp2_submit_altsvc : 412 -> 460
~ _nghttp2_submit_origin : 496 -> 528
~ _nghttp2_submit_priority_update : 348 -> 380
~ _nghttp2_submit_extension : 216 -> 232
~ _nghttp2_session_add_rst_stream_continue : 432 -> 448
~ _nghttp2_session_add_ping : 236 -> 252
~ _session_call_error_callback : 292 -> 308
~ _nghttp2_session_recv : 276 -> 288
~ _nghttp2_session_upgrade_internal : 472 -> 488

```
