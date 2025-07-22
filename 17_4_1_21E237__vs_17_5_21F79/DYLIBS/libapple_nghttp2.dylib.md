## libapple_nghttp2.dylib

> `/usr/lib/libapple_nghttp2.dylib`

```diff

-20.0.0.0.0
-  __TEXT.__text: 0x11d94
+20.120.2.0.0
+  __TEXT.__text: 0x12194
   __TEXT.__auth_stubs: 0xd0
-  __TEXT.__const: 0x554c
-  __TEXT.__cstring: 0x22d8
-  __TEXT.__unwind_info: 0x348
+  __TEXT.__const: 0x555c
+  __TEXT.__cstring: 0x2371
+  __TEXT.__unwind_info: 0x388
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x1ef0
   __AUTH_CONST.__auth_got: 0x68
   __DATA.__data: 0x18
   __DATA_DIRTY.__data: 0x28
   - /usr/lib/libSystem.B.dylib
-  UUID: FB340BFE-0AD7-3F1E-B025-CC7F91355C46
-  Functions: 320
-  Symbols:   444
-  CStrings:  341
+  UUID: 25E33D75-B279-3A62-8E81-FD20EF5396DA
+  Functions: 342
+  Symbols:   470
+  CStrings:  345
 
Symbols:
+ _nghttp2_extpri_parse_priority
+ _nghttp2_hd_deflate_hd2
+ _nghttp2_hd_deflate_hd_vec2
+ _nghttp2_hd_inflate_hd3
+ _nghttp2_option_set_max_continuations
+ _nghttp2_pack_settings_payload2
+ _nghttp2_select_alpn
+ _nghttp2_session_callbacks_set_data_source_read_length_callback2
+ _nghttp2_session_callbacks_set_pack_extension_callback2
+ _nghttp2_session_callbacks_set_recv_callback2
+ _nghttp2_session_callbacks_set_select_padding_callback2
+ _nghttp2_session_callbacks_set_send_callback2
+ _nghttp2_session_get_extpri_stream_priority
+ _nghttp2_session_mem_recv2
+ _nghttp2_session_mem_send2
+ _nghttp2_stream_detach_item
+ _nghttp2_submit_data2
+ _nghttp2_submit_data_shared
+ _nghttp2_submit_request2
+ _nghttp2_submit_response2
+ _select_alpn
+ _stream_less.215
+ _submit_request_shared
+ _submit_response_shared
- _select_next_protocol
- _stream_less.204
CStrings:
+ "1.61.0"
+ "Too many CONTINUATION frames following a HEADER frame"
+ "data_prd"
+ "nghttp2_session_mem_recv2"
+ "nghttp2_session_mem_send2"
+ "nghttp2_submit_data"
+ "nghttp2_submit_data2"
+ "session->callbacks.pack_extension_callback2 || session->callbacks.pack_extension_callback"
- "1.58.0"
- "nghttp2_session_mem_recv"
- "nghttp2_session_mem_send"
- "session->callbacks.pack_extension_callback"

```
