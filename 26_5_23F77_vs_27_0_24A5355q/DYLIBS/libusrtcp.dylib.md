## libusrtcp.dylib

> `/usr/lib/libusrtcp.dylib`

```diff

-5812.122.1.0.0
-  __TEXT.__text: 0x5c2a8
-  __TEXT.__auth_stubs: 0x1030
-  __TEXT.__const: 0x240
-  __TEXT.__oslogstring: 0xe6e1
-  __TEXT.__cstring: 0x1a17
-  __TEXT.__unwind_info: 0x460
-  __DATA_CONST.__got: 0xa0
+6681.0.372.502.1
+  __TEXT.__text: 0x5aa0c
+  __TEXT.__const: 0x244
+  __TEXT.__oslogstring: 0xe5ed
+  __TEXT.__cstring: 0x1a4f
+  __TEXT.__unwind_info: 0x450
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x410
-  __AUTH_CONST.__auth_got: 0x818
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x1a8
-  __AUTH.__data: 0x220
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__data: 0x1a0
   __DATA.__data: 0x10
-  __DATA.__bss: 0x6d0
-  __DATA_DIRTY.__data: 0x184
-  __DATA_DIRTY.__bss: 0x170
+  __DATA.__bss: 0x6e0
+  __DATA_DIRTY.__data: 0x1d4
+  __DATA_DIRTY.__bss: 0x160
   - /System/Library/Frameworks/Network.framework/Network
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 598B3907-59F6-3494-BEC4-0FAA5E917E55
+  UUID: 2E063CBD-9456-3B54-9FF9-88853D180C7D
   Functions: 329
   Symbols:   1013
-  CStrings:  1115
+  CStrings:  1114
 
Symbols:
+ _____nw_frame_array_finalize_block_invoke.285
+ _____nw_frame_array_finalize_block_invoke.579
+ _____nw_signpost_is_enabled_block_invoke.91
+ ___block_descriptor_tmp.15.107
+ ___block_descriptor_tmp.286
+ ___block_descriptor_tmp.793
+ ___block_descriptor_tmp.89
+ ___block_literal_global.791
+ ___block_literal_global.86
+ _rbbr_apply_cruise_backoff
+ _tcp_cc_nosack_partial_ack
+ _tcp_cc_rbbr
+ _tcp_prr_update
+ _tcp_rbbr_after_idle
+ _tcp_rbbr_cleanup
+ _tcp_rbbr_data_rcvd
+ _tcp_rbbr_get_rlwin
+ _tcp_rbbr_init
+ _tcp_rbbr_rwnd_init
+ _tcp_rbbr_switch_to
+ _tcp_rcv_cc_rwnd_init
+ _tcp_seg_alloc_init
- _____nw_frame_array_finalize_block_invoke.289
- _____nw_frame_array_finalize_block_invoke.584
- _____nw_signpost_is_enabled_block_invoke.98
- ___block_descriptor_tmp.15.115
- ___block_descriptor_tmp.290
- ___block_descriptor_tmp.798
- ___block_descriptor_tmp.96
- ___block_literal_global.796
- ___block_literal_global.93
- _compute_iaj_meat
- _tcp_cc_newreno
- _tcp_newreno_ack_rcvd
- _tcp_newreno_after_timeout
- _tcp_newreno_cleanup
- _tcp_newreno_congestion_avd
- _tcp_newreno_cwnd_init_or_reset
- _tcp_newreno_delay_ack
- _tcp_newreno_init
- _tcp_newreno_partial_ack
- _tcp_newreno_post_fr
- _tcp_newreno_pre_fr
- _tcp_newreno_switch_cc
CStrings:
+ "%{public}s %{public}s couldn't allocate memory for struct tseg_qent"
+ "tcp_rxtseg_insert"
+ "tcp_sackhole_alloc"
+ "tcp_seg_alloc_init"
- "%{public}s %{public}s couldn't allocate memory for tcp_reass_zone"
- "%{public}s failed allocating tcp_reass_zone"
- "%{public}s failed allocating tcp_reass_zone, backtrace limit exceeded"
- "%{public}s failed allocating tcp_reass_zone, dumping backtrace:%{public}s"
- "%{public}s failed allocating tcp_reass_zone, no backtrace"

```
