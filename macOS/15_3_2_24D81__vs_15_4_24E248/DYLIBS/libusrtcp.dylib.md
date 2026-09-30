## libusrtcp.dylib

> `/usr/lib/libusrtcp.dylib`

```diff

-4277.81.1.0.0
-  __TEXT.__text: 0x5dc7c
-  __TEXT.__auth_stubs: 0xf60
-  __TEXT.__const: 0x224
-  __TEXT.__oslogstring: 0xe771
-  __TEXT.__cstring: 0x1984
-  __TEXT.__unwind_info: 0x468
+4277.101.3.0.0
+  __TEXT.__text: 0x5e478
+  __TEXT.__auth_stubs: 0xf90
+  __TEXT.__const: 0x234
+  __TEXT.__oslogstring: 0xe62f
+  __TEXT.__cstring: 0x19a0
+  __TEXT.__unwind_info: 0x428
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x2f0
-  __AUTH_CONST.__auth_got: 0x7b0
+  __AUTH_CONST.__auth_got: 0x7c8
   __AUTH_CONST.__const: 0x248
   __AUTH.__data: 0xd0
   __DATA.__data: 0x34
-  __DATA.__bss: 0x7d8
+  __DATA.__bss: 0x7d0
   __DATA_DIRTY.__data: 0x2a0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/Network.framework/Versions/A/Network
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3C4137B4-B6EA-3D39-B9CF-B203A3B7F436
-  Functions: 357
-  Symbols:   677
-  CStrings:  1109
+  UUID: 59E0510B-6111-3581-9B72-085E3AC746D3
+  Functions: 335
+  Symbols:   678
+  CStrings:  1108
 
Symbols:
+ __block_descriptor_tmp.20.21
+ __block_descriptor_tmp.227
+ __block_descriptor_tmp.26
+ __block_descriptor_tmp.30
+ __block_descriptor_tmp.31
+ __block_descriptor_tmp.34
+ __block_literal_global.36
+ _getpid
+ _network_config_get_l4s_enabled
+ _nw_path_use_link_heuristics
+ _nw_protocol_establishment_report_set_l4s_enabled
+ _sandbox_check
+ _tcp_developer_l4s
+ _tcp_set_link_heur_rtomin
- __block_descriptor_tmp.19
- __block_descriptor_tmp.20.23
- __block_descriptor_tmp.228
- __block_descriptor_tmp.27
- __block_descriptor_tmp.28
- __block_descriptor_tmp.33
- __block_literal_global.35
- _network_config_get_tcp_accurate_ecn_enabled
- _network_config_get_tcp_l4s_enabled
- _tcp_do_acc_ecn
- _tcp_do_l4s
- _tcp_rack_update_segment_acked
- _update_iaj_state
CStrings:
+ "%{public}s %{public}s Sandbox does not allow __nexus_set_opt"
+ "%{public}s %{public}s link heuristics %s"
+ "%{public}s %{public}s link heuristics %{public}s"
+ "%{public}s %{public}s route is not usable: no checksum offload"
+ "%{public}s strict allocator failed"
+ "nw_tcp_init_globals"
+ "syscall-unix"
+ "tcp_get_heuristics"
+ "tcp_heuristics_cache_init"
+ "v16@?0^{ifnet_stats_per_flow=QQQIIIIIIIIIIIIIIIIIIb1b1b1b1b1b1b1b1b1b1b6SIQQQQ}8"
- "%{public}s %{public}s Spurious inference as eithertsecr (%u) doesn't lie between xmit_ts(%u) and now (%u) ORthe segment was transmitted less than base rtt (%u) ago"
- "%{public}s %{public}s win is smaller than 0: %d"
- "%{public}s TE_SENDIPECT flag is set but TCP_L4S_ENABLED is not"
- "%{public}s TE_SENDIPECT flag is set but TCP_L4S_ENABLED is not, backtrace limit exceeded"
- "%{public}s TE_SENDIPECT flag is set but TCP_L4S_ENABLED is not, dumping backtrace:%{public}s"
- "%{public}s TE_SENDIPECT flag is set but TCP_L4S_ENABLED is not, no backtrace"
- "%{public}s strict_malloc(%zu) failed"
- "strict_calloc"
- "strict_malloc"
- "tcp_rack_update_segment_acked"
- "v16@?0^{ifnet_stats_per_flow=QQQIIIIIIIIIIIIIIIIIIb1b1b1b1b1b1b1b1b1b1}8"

```
