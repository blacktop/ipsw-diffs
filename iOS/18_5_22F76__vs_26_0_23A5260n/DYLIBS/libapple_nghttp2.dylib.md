## libapple_nghttp2.dylib

> `/usr/lib/libapple_nghttp2.dylib`

```diff

-29.0.0.0.0
-  __TEXT.__text: 0x11434
+31.0.0.0.0
+  __TEXT.__text: 0xfb18
   __TEXT.__auth_stubs: 0xd0
-  __TEXT.__const: 0x56f8
-  __TEXT.__cstring: 0x2347
-  __TEXT.__unwind_info: 0x348
+  __TEXT.__const: 0x5860
+  __TEXT.__cstring: 0x201f
+  __TEXT.__unwind_info: 0x2f8
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x1ef0
   __AUTH_CONST.__auth_got: 0x68
   __DATA.__data: 0x18
+  __DATA.__bss: 0x80
   __DATA_DIRTY.__data: 0x28
   - /usr/lib/libSystem.B.dylib
-  UUID: E4DE3AFD-769F-3368-BB3D-EE93F93573CD
-  Functions: 315
-  Symbols:   471
-  CStrings:  341
+  UUID: 66759250-228C-3AE4-BFD9-31BCB4D0F5D0
+  Functions: 290
+  Symbols:   423
+  CStrings:  318
 
Symbols:
+ _VALID_AUTHORITY_CHARS.382
+ _parser_dispstring
+ _root
+ _utf8d
- _VALID_AUTHORITY_CHARS.396
- _insert_link_dep
- _nghttp2_frame_pack_altsvc
- _nghttp2_frame_pack_priority_update
- _nghttp2_hd_deflate_init2
- _nghttp2_session_adjust_closed_stream
- _nghttp2_session_adjust_idle_stream
- _nghttp2_session_destroy_stream
- _nghttp2_session_pack_data
- _nghttp2_session_reprioritize_stream
- _nghttp2_stream_dep_add_subtree
- _nghttp2_stream_dep_remove
- _nghttp2_stream_dep_remove_subtree
- _nghttp2_stream_detach_item
- _nghttp2_stream_reschedule
- _session_detach_stream_item
- _session_predicate_push_response_headers_send
- _session_process_ping_frame
- _session_process_priority_frame
- _session_process_priority_update_frame
- _session_process_push_promise_frame
- _session_process_rst_stream_frame
- _session_process_window_update_frame
- _stream_less.215
- _stream_obq_move
- _stream_obq_push
- _stream_obq_remove
CStrings:
+ "'%' == *sfp->pos"
+ "1.65.0"
+ "initial_state != NGHTTP2_STREAM_IDLE"
+ "parser_dispstring"
+ "parser_skip_inner_list"
+ "parser_skip_params"
+ "sfparse_parser_dict"
+ "sfparse_parser_inner_list"
+ "sfparse_parser_param"
- "!(stream->flags & NGHTTP2_STREAM_FLAG_NO_RFC7540_PRIORITIES)"
- "!session_no_rfc7540_pri_no_fallback(session)"
- "&session->aob.framebufs == bufs"
- "(!session->server && session->pending_no_rfc7540_priorities != 1) || (session->server && !session_no_rfc7540_pri_no_fallback(session))"
- "(stream->flags & NGHTTP2_STREAM_FLAG_NO_RFC7540_PRIORITIES) || nghttp2_stream_in_dep_tree(stream)"
- "1.64.0"
- "PRIORITY: stream_id == 0"
- "dep_stream"
- "depend on itself"
- "head"
- "head_stream"
- "insert_link_dep"
- "nghttp2_session_adjust_closed_stream"
- "nghttp2_session_adjust_idle_stream"
- "nghttp2_session_on_priority_received"
- "nghttp2_session_reprioritize_stream"
- "nghttp2_stream_dep_remove"
- "nghttp2_stream_dep_remove_subtree"
- "nghttp2_stream_reschedule"
- "prev"
- "pri_spec->stream_id != stream->stream_id"
- "session_process_priority_frame"
- "sf_parser_dict"
- "sf_parser_inner_list"
- "sf_parser_param"
- "stream->closed_prev == NULL"
- "stream->dep_prev"
- "stream->flags & NGHTTP2_STREAM_FLAG_NO_RFC7540_PRIORITIES"
- "stream->queued"
- "stream->sib_prev == NULL"
- "stream_obq_remove"
- "unlink_dep"

```
