## libusrtcp.dylib

> `/usr/lib/libusrtcp.dylib`

```diff

-5569.82.5.0.0
-  __TEXT.__text: 0x5ccc8
+5812.100.360.0.2
+  __TEXT.__text: 0x5c2a4
   __TEXT.__auth_stubs: 0x1030
-  __TEXT.__const: 0x244
-  __TEXT.__oslogstring: 0xe713
-  __TEXT.__cstring: 0x1a3b
+  __TEXT.__const: 0x248
+  __TEXT.__oslogstring: 0xe6e1
+  __TEXT.__cstring: 0x1a17
   __TEXT.__unwind_info: 0x460
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x410

   - /System/Library/Frameworks/Network.framework/Network
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 93BC76FB-94A9-3EE8-AE18-0BDFCBB45F2F
-  Functions: 328
+  UUID: 36FE060C-EC16-3DE4-9180-0428E9FD4FAD
+  Functions: 329
   Symbols:   1013
-  CStrings:  1118
+  CStrings:  1115
 
Symbols:
+ _____nw_frame_array_finalize_block_invoke.584
+ _____nw_signpost_is_enabled_block_invoke.493
+ ___block_descriptor_tmp.485
+ ___block_descriptor_tmp.798
+ ___block_descriptor_tmp.8.487
+ ___block_literal_global.486
+ ___block_literal_global.796
- _____nw_frame_array_finalize_block_invoke.586
- _____nw_signpost_is_enabled_block_invoke.495
- ___block_descriptor_tmp.487
- ___block_descriptor_tmp.8.489
- ___block_descriptor_tmp.800
- ___block_literal_global.488
- ___block_literal_global.798
Functions:
~ _tcp_usr_attach : 2012 -> 2008
~ _set_tcp_stream_priority : 624 -> 612
~ _tcp_output : 32780 -> 32892
~ _tcp_ip_output_send : 3396 -> 3400
~ _nw_tcp_init_globals : 2472 -> 2464
~ _nw_protocol_tcp_register_notification : 4852 -> 4812
~ _tcp_ctloutput : 4580 -> 4480
+ sub_18907a1a8
~ _tcp_usr_bind : 336 -> 332
~ _tcp_usr_connect : 1040 -> 1036
~ _nw_proto_tcp_route_init : 3548 -> 3528
~ _tcp_get_heuristics : 884 -> 864
~ _nw_protocol_tcp_get_frames : 8732 -> 7424
~ _tcp_usr_send : 1744 -> 1740
~ _sbappendstream : 800 -> 752
~ _nw_protocol_tcp_copy_frame_to_buffer : 3080 -> 3084
~ _calculate_tcp_clock : 112 -> 108
~ _tcp_input : 38252 -> 37984
~ _tcp_set_lotimer_index : 644 -> 636
~ _tcp_compute_rtt : 520 -> 356
~ _nw_protocol_tcp_input_available : 3636 -> 3584
~ _tcp_bad_rexmt_check : 1096 -> 1080
~ _update_base_rtt : 764 -> 760
~ _tcp_dooptions : 660 -> 656
~ _soisconnected : 444 -> 440
~ ___nw_protocol_tcp_timer_init_block_invoke : 1684 -> 1640
~ _tcp_process_timerlist : 3452 -> 3436
~ _tcp_gc : 304 -> 300
~ _tcp_timers : 5448 -> 5452
~ _tcp_free_sackholes : 176 -> 172
~ _tcp_update_sack_list : 352 -> 348
~ _nw_protocol_tcp_get_input_frames : 4160 -> 4144
~ _tcp_usr_rcvd : 416 -> 412
~ ___nw_protocol_tcp_get_input_frames_block_invoke : 2284 -> 2292
~ _sbdrop : 1256 -> 1244
~ _nw_frame_tcp_finalize : 2408 -> 2388
~ _tcp_compute_rcv_rtt : 416 -> 236
~ _sbappendstream_rcvdemux : 224 -> 220
~ _nw_protocol_tcp_copy_info : 2332 -> 2328
~ _tcp_fill_info : 1688 -> 1700
~ _tcp_close_locked : 4032 -> 4008
~ _sofreelastref : 984 -> 980
~ _tcp_connection_fill_info : 836 -> 832
~ _nw_protocol_tcp_log_summary : 2244 -> 2212
~ _tcp_usr_disconnect : 180 -> 176
~ _tcp_usr_detach : 188 -> 184
~ _tcp_close : 3940 -> 3928
~ ___tcp_publish_necp_if_stats_block_invoke : 416 -> 432
~ _nw_protocol_tcp_unregister_notification : 3144 -> 3108
~ _tcp_sack_doack : 2176 -> 2184
~ _tcp_sackhole_insert : 320 -> 328
~ _tcp6_usr_bind : 516 -> 508
~ _tcp6_usr_connect : 1172 -> 1168
~ _tcp6_connect : 848 -> 844
~ _tcp_usr_shutdown : 240 -> 236
~ _nw_protocol_tcp_get_frame_count : 588 -> 580
~ _nw_protocol_tcp_get_malloc_frame : 3576 -> 3544
~ ___nw_protocol_tcp_get_slab_frame_block_invoke : 420 -> 408
~ ___nw_frame_tcp_finalize_block_invoke : 796 -> 784
~ _tcp_rledbat_switch_to : 188 -> 180
~ _nw_tcp_release_frame_array : 2148 -> 2088
~ _nw_protocol_tcp_output_available : 1284 -> 1280
~ _tcp_drop : 404 -> 408
~ _tcp_seg_sent_tree_head_RB_REMOVE : 1380 -> 1480
~ _tcp_rxtseg_clean : 144 -> 136
~ _tcp_seg_rto_insert_end : 736 -> 716
~ _tcp_seg_delete_acked : 2448 -> 2432
~ _tcp_seg_sent_insert_before : 740 -> 720
~ _tcp_add_notify_ack_marker : 492 -> 504
~ _tcp_get_notify_ack_ids : 192 -> 188
~ _tcp_enter_fast_recovery : 340 -> 328
~ _tcp_input_ip_ecn : 176 -> 180
~ _tcp_tfo_rcv_probe : 584 -> 568
~ _tcp_reass : 9256 -> 9212
~ _tcp_bad_rexmt_restore_state : 700 -> 684
~ _tcp_set_foreground_cc : 72 -> 80
~ _tcp_usr_listen : 336 -> 332
~ _tcp_usr_abort : 404 -> 400
~ _tcp6_usr_listen : 376 -> 368
~ _tcp_setsockopt : 812 -> 756
~ _tcp_set_keepalive : 156 -> 164
~ _tcp_rack_detect_loss : 480 -> 348
~ _tcp_rack_reordering_timeout : 276 -> 304
CStrings:
- "%{public}s Assert to != NULL && th != NULL failed"
- "tcp_compute_rcv_rtt"
- "tcp_compute_rtt"

```
