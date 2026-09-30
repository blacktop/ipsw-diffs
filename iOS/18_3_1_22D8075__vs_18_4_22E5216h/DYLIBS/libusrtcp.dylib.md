## libusrtcp.dylib

> `/usr/lib/libusrtcp.dylib`

```diff

-4277.82.1.0.0
-  __TEXT.__text: 0x5daac
-  __TEXT.__auth_stubs: 0xf50
-  __TEXT.__const: 0x224
-  __TEXT.__oslogstring: 0xe771
-  __TEXT.__cstring: 0x1984
-  __TEXT.__unwind_info: 0x488
+4277.100.434.0.0
+  __TEXT.__text: 0x5e2a4
+  __TEXT.__auth_stubs: 0xf80
+  __TEXT.__const: 0x234
+  __TEXT.__oslogstring: 0xe62f
+  __TEXT.__cstring: 0x19a0
+  __TEXT.__unwind_info: 0x458
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x390
-  __AUTH_CONST.__auth_got: 0x7a8
+  __AUTH_CONST.__auth_got: 0x7c0
   __AUTH_CONST.__const: 0x188
   __AUTH.__data: 0x220
   __DATA.__data: 0x10
-  __DATA.__bss: 0x6c0
+  __DATA.__bss: 0x6c4
   __DATA_DIRTY.__data: 0x180
-  __DATA_DIRTY.__bss: 0x150
+  __DATA_DIRTY.__bss: 0x140
   - /System/Library/Frameworks/Network.framework/Network
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 351
-  Symbols:   595
-  CStrings:  1109
+  Functions: 329
+  Symbols:   597
+  CStrings:  1108
 
Symbols:
+ _getpid
+ _network_config_get_l4s_enabled
+ _nw_path_use_link_heuristics
+ _nw_protocol_establishment_report_set_l4s_enabled
+ _sandbox_check
- _network_config_get_tcp_accurate_ecn_enabled
- _network_config_get_tcp_l4s_enabled
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
