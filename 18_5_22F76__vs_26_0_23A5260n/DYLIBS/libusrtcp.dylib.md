## libusrtcp.dylib

> `/usr/lib/libusrtcp.dylib`

```diff

-4277.122.6.0.0
-  __TEXT.__text: 0x5e29c
-  __TEXT.__auth_stubs: 0xf80
-  __TEXT.__const: 0x234
-  __TEXT.__oslogstring: 0xe62f
-  __TEXT.__cstring: 0x19a0
-  __TEXT.__unwind_info: 0x460
+5569.0.37.0.12
+  __TEXT.__text: 0x5bf20
+  __TEXT.__auth_stubs: 0x1020
+  __TEXT.__const: 0x244
+  __TEXT.__oslogstring: 0xe485
+  __TEXT.__cstring: 0x19c3
+  __TEXT.__unwind_info: 0x440
   __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x390
-  __AUTH_CONST.__auth_got: 0x7c0
-  __AUTH_CONST.__const: 0x188
+  __DATA_CONST.__const: 0x388
+  __AUTH_CONST.__auth_got: 0x810
+  __AUTH_CONST.__const: 0x1a8
   __AUTH.__data: 0x220
   __DATA.__data: 0x10
-  __DATA.__bss: 0x6c4
-  __DATA_DIRTY.__data: 0x180
-  __DATA_DIRTY.__bss: 0x140
+  __DATA.__bss: 0x6d0
+  __DATA_DIRTY.__data: 0x184
+  __DATA_DIRTY.__bss: 0x170
   - /System/Library/Frameworks/Network.framework/Network
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 88F785FB-0C87-3482-9692-AD7942E0BA34
-  Functions: 329
-  Symbols:   995
-  CStrings:  1108
+  UUID: A71B9B26-55D2-35D7-8B1D-E44D0222C751
+  Functions: 320
+  Symbols:   992
+  CStrings:  1105
 
Symbols:
+ _____nw_signpost_is_enabled_block_invoke.482
+ _____nw_signpost_is_enabled_block_invoke.93
+ ___block_descriptor_tmp.15.110
+ ___block_descriptor_tmp.24.26
+ ___block_descriptor_tmp.474
+ ___block_descriptor_tmp.8.476
+ ___block_descriptor_tmp.9
+ ___block_descriptor_tmp.91
+ ___block_literal_global.11
+ ___block_literal_global.475
+ ___block_literal_global.88
+ ___user_tcp_init_all_block_invoke
+ __os_log_default
+ __os_log_error_impl
+ _g_tcp_nw_assert_context
+ _g_tcp_use_malloc_memory
+ _nw_context_assert_queue
+ _nw_context_get_identifier
+ _nw_interface_get_l4s_mode
+ _nw_link_get_local_congestion_info
+ _nw_mem_buffer_allocate_sized_typed
+ _nw_mem_buffer_manager_get_global
+ _nw_protocol_callbacks_set_notify
+ _nw_protocol_common_notify
+ _nw_protocol_tcp_notify
+ _nw_protocol_tcp_set_max_pacing_rate
+ _nw_setting_tcp_nw_assert_context
+ _nw_tcp_access_context
+ _os_nexus_flow_set_connection_idle
+ _os_variant_has_internal_diagnostics
+ _sbappendstream_rcvdemux
+ _sbrelease
+ _tcp_new_isn.isn_last_reseed
+ _tcp_offset_from_latest_tx
+ _tcp_set_rto
+ _user_tcp_init_all.onceToken
- _____nw_signpost_is_enabled_block_invoke.496
- _____nw_signpost_is_enabled_block_invoke.87
- ___block_descriptor_tmp.15.104
- ___block_descriptor_tmp.20.21
- ___block_descriptor_tmp.227
- ___block_descriptor_tmp.488
- ___block_descriptor_tmp.8.490
- ___block_descriptor_tmp.85
- ___block_literal_global.489
- ___block_literal_global.82
- ___tcp_input_get_aggregate_frames_block_invoke
- _nw_default_tcp_input_max_aggregate
- _nw_frame_is_wake_packet
- _nw_setting_tcp_input_max_aggregate
- _sb_agg_empty_verify
- _sbflush
- _sorflush
- _tcp_detect_bad_rexmt
- _tcp_get_notify_ack_count
- _tcp_heuristic_ecn_aggressive
- _tcp_heuristic_ecn_droprxmt
- _tcp_heuristic_ecn_loss
- _tcp_init
- _tcp_input_aggregate_end
- _tcp_input_get_aggregate_frames
- _tcp_input_sbappendstream
- _tcp_reset_stretch_ack
- _tcp_set_ecn
- _tcp_set_link_heur_rtomin
- _tcp_stretch_ack_enable
CStrings:
+ "%s: pacer rate shouldn't be 0, CCA is %s (cwnd=%u, smoothed rtt=%u ms)"
+ "%{public}s %{public}s append frame count %u length %u sb_cc %u"
+ "%{public}s %{public}s nw_protocol_notification_type_connection_idle is %{bool}d"
+ "%{public}s %{public}s nw_protocol_tcp_set_connection_idle flow_registration is NULL"
+ "%{public}s %{public}s nw_protocol_tcp_set_connection_idle path is NULL"
+ "%{public}s %{public}s os_nexus_flow_set_connection_idle returned %d"
+ "%{public}s %{public}s tcp_set_max_pacing_rate failed %{darwin.errno}d"
+ "%{public}s %{public}s tcp_set_max_pacing_rate failed %{darwin.errno}d, backtrace limit exceeded"
+ "%{public}s %{public}s tcp_set_max_pacing_rate failed %{darwin.errno}d, dumping backtrace:%{public}s"
+ "%{public}s %{public}s tcp_set_max_pacing_rate failed %{darwin.errno}d, no backtrace"
+ "%{public}s Assert SEQ_LEQ(ack, tp->snd_max) failed"
+ "%{public}s called with null (len == sizeof(bool))"
+ "%{public}s called with null (len == sizeof(bool)), backtrace limit exceeded"
+ "%{public}s called with null (len == sizeof(bool)), dumping backtrace:%{public}s"
+ "%{public}s called with null (len == sizeof(bool)), no backtrace"
+ "%{public}s called with null (len == sizeof(struct nw_link_congestion_info))"
+ "%{public}s called with null (len == sizeof(struct nw_link_congestion_info)), backtrace limit exceeded"
+ "%{public}s called with null (len == sizeof(struct nw_link_congestion_info)), dumping backtrace:%{public}s"
+ "%{public}s called with null (len == sizeof(struct nw_link_congestion_info)), no backtrace"
+ "%{public}s called with null (val != nil)"
+ "%{public}s called with null (val != nil), backtrace limit exceeded"
+ "%{public}s called with null (val != nil), dumping backtrace:%{public}s"
+ "%{public}s called with null (val != nil), no backtrace"
+ "%{public}s called with null other_protocol"
+ "%{public}s called with null other_protocol, backtrace limit exceeded"
+ "%{public}s called with null other_protocol, dumping backtrace:%{public}s"
+ "%{public}s called with null other_protocol, no backtrace"
+ "%{public}s g_tcp_nw_assert_context is %s value %lld"
+ "%{public}s globals: %p nw_context: %p identifier: %s"
+ "B16@?0^{nw_frame={os_object_header_s=^vii}{?=^{nw_frame}^^{nw_frame}}{?=^{nw_frame}^^{nw_frame}}IIII{?=^{nw_frame_protocol_metadata}^^{nw_frame_protocol_metadata}}^?^v^{dispatch_data_s}^{nw_mem_buffer_manager}*{nw_frame_protocol_metadata={?=^{nw_frame_protocol_metadata}^^{nw_frame_protocol_metadata}}[16C]QQ^{nw_protocol_metadata}iiCCb2b1b1b1b1b1b1[5C]}ISSCCCCb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b5[1C]}8"
+ "buffer_manager_use_malloc"
+ "com.apple.network.tcp"
+ "false"
+ "nw_protocol_tcp_get_buffer_manager_malloc_frame"
+ "nw_protocol_tcp_notify"
+ "nw_protocol_tcp_set_connection_idle"
+ "nw_protocol_tcp_set_max_pacing_rate"
+ "tcp_cubic_post_fr"
+ "true"
+ "user_tcp_init_all_block_invoke"
- "%{public}s %{public}s %{public}s: aggregate frame length %u not counted sb flags 0x%x cc %d agg_cnt %u agg_bytes %u"
- "%{public}s %{public}s %{public}s: aggregate frame not counted sb flags 0x%x cc %d agg_cnt %u agg_bytes %u"
- "%{public}s %{public}s %{public}s: sb flags 0x%x cc %d agg_cnt %u agg_bytes %u"
- "%{public}s %{public}s %{public}s: sb flags 0x%x cc %d agg_cnt %u agg_bytes %u, backtrace limit exceeded"
- "%{public}s %{public}s %{public}s: sb flags 0x%x cc %d agg_cnt %u agg_bytes %u, dumping backtrace:%{public}s"
- "%{public}s %{public}s %{public}s: sb flags 0x%x cc %d agg_cnt %u agg_bytes %u, no backtrace"
- "%{public}s %{public}s append frame count %u length %u sb_agg_bytes %u sb_cc %u"
- "%{public}s %{public}s append to aggregate frame count %u length %u sb_agg_bytes %u sb_cc %u"
- "%{public}s %{public}s nw_protocol_tcp_copy_frame failed"
- "%{public}s %{public}s removing empty wake packet"
- "%{public}s %{public}s sb_mb_aggregate not empty"
- "%{public}s %{public}s skipping empty input frame (length %u bytes %p)"
- "%{public}s %{public}s tcp_input_aggregate_begin sb_mb_aggregate not empty"
- "%{public}s %{public}s tcp_input_max_aggregate %u"
- "%{public}s %{public}s tlen %d != __nw_frame_array_unclaimed_length() %u"
- "%{public}s %{public}s tlen %d != __nw_frame_array_unclaimed_length() %u, backtrace limit exceeded"
- "%{public}s %{public}s tlen %d != __nw_frame_array_unclaimed_length() %u, dumping backtrace:%{public}s"
- "%{public}s %{public}s tlen %d != __nw_frame_array_unclaimed_length() %u, no backtrace"
- "%{public}s Assert sb->sb_agg_bytes >= len failed"
- "%{public}s Assert sb->sb_agg_cnt > 0 failed"
- "%{public}s Assert so->so_rcv.sb_agg_bytes >= frame_length failed"
- "%{public}s Assert so->so_rcv.sb_agg_bytes >= to_copy failed"
- "%{public}s Assert so->so_rcv.sb_agg_cnt > 0 failed"
- "%{public}s Assert so->so_rcv.sb_cc >= frame_length failed"
- "%{public}s added agg frame to sb_mb sb_agg_bytes %u sb_cc %u"
- "%{public}s aggregate buffer is NULL"
- "%{public}s aggregate frame is NULL from array"
- "%{public}s no frame within the array"
- "%{public}s pacer rate shouldn't be 0, CCA is %s (cwnd=%u, smoothed rtt=%u ms)"
- "%{public}s pacer rate shouldn't be 0, CCA is %s (cwnd=%u, smoothed rtt=%u ms), backtrace limit exceeded"
- "%{public}s pacer rate shouldn't be 0, CCA is %s (cwnd=%u, smoothed rtt=%u ms), dumping backtrace:%{public}s"
- "%{public}s pacer rate shouldn't be 0, CCA is %s (cwnd=%u, smoothed rtt=%u ms), no backtrace"
- "%{public}s start sb_agg_bytes %u sb_cc %u"
- "%{public}s tcp_input_get_aggregate_frame failed, drop %u segments of length %u"
- "B16@?0^{nw_frame={os_object_header_s=^vii}{?=^{nw_frame}^^{nw_frame}}{?=^{nw_frame}^^{nw_frame}}IIII{?=^{nw_frame_protocol_metadata}^^{nw_frame_protocol_metadata}}^?^v^{dispatch_data_s}^{nw_mem_buffer_manager}*{nw_frame_protocol_metadata={?=^{nw_frame_protocol_metadata}^^{nw_frame_protocol_metadata}}[16C]QQ^{nw_protocol_metadata}iiCCb2b1b1b1b1b1b1[5C]}ISSCCCCb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b6[1C]}8"
- "sb_agg_empty_verify"
- "tcp_heuristic_ecn_aggressive"
- "tcp_heuristic_ecn_droprxmt"
- "tcp_heuristic_ecn_loss"
- "tcp_input_aggregate_begin"
- "tcp_input_aggregate_end"
- "tcp_input_get_aggregate_frames_block_invoke"
- "tcp_input_sbappendstream"

```
