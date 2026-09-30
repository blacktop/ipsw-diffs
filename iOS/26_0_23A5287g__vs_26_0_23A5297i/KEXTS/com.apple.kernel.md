## com.apple.kernel

> `com.apple.kernel`

```diff

-12377.0.132.0.2
+12377.0.154.0.2
   __TEXT.__const: 0x34bc0
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x7d3bf
-  __TEXT.__os_log: 0x3bf8f
+  __TEXT.__cstring: 0x7d68d
+  __TEXT.__os_log: 0x3c0c4
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2d8
-  __DATA_CONST.__const: 0xac9f8
+  __DATA_CONST.__const: 0xacba8
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__kalloc_type: 0x13f80
+  __DATA_CONST.__kalloc_type: 0x14180
   __DATA_CONST.__assert: 0x5dc
   __DATA_CONST.__kalloc_var: 0x7a80
   __DATA_CONST.__exclaves_bt: 0x78
   __DATA_CONST.__kern_brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
-  __TEXT_EXEC.__text: 0x891728
+  __TEXT_EXEC.__text: 0x8936d0
   __TEXT_EXEC.__hib_text: 0xe38
   __TEXT_BOOT_EXEC.__bootcode: 0x5218
   __KLD.__text: 0x1818

   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__cstring: 0x6e1
-  __KLDDATA.__const: 0x30d0
+  __KLDDATA.__const: 0x3168
   __KLDDATA.__bss: 0x1
-  __DATA.__data: 0x17de9
+  __DATA.__data: 0x17e29
   __DATA.__lock_grp: 0x5b70
   __DATA.__percpu: 0x6f08
-  __DATA.__common: 0x5c120
-  __DATA.__bss: 0x96cc8
+  __DATA.__common: 0x5c100
+  __DATA.__bss: 0x96cd8
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__static_if: 0x4d10
-  __BOOTDATA.__init_entry_set: 0x11778
+  __BOOTDATA.__init_entry_set: 0x11838
   __BOOTDATA.__init: 0x5b288
   __BOOTDATA.__static_ifinit: 0x8
   __PRELINK_TEXT.__text: 0x0

   __PLK_DATA_CONST.__data: 0x0
   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
-  __LINKINFO.__symbolsets: 0x46fda
-  UUID: 90EE574F-F96C-3700-8BDC-4D92BB95FAFF
-  Functions: 20614
+  __LINKINFO.__symbolsets: 0x470a7
+  UUID: 7BB60F77-CC2A-381F-AA30-24CF51327874
+  Functions: 20623
   Symbols:   0
-  CStrings:  19915
+  CStrings:  19929
 
CStrings:
+ "2211111111111112222222112222211222221111112222111111222222222111211112122222222222222222222222222222222222222222222222222222222212222221122122222222222222222222222222222222222222222222222222222211222222212112222222222222222121112222222222222122222211222221222222222222222221111111222222222200"
+ "2211121111111222221112122212222222222222222222222222222222222222222111111111111111111121122222222211222222222222112122212222212222222222222222222222222222112111122222222222222111121221122211222112221122222211222222222222222222222221111221221222222222212212212222111122222222222222222112222222222112122222222211111112112222222222222222222222222222222222221122222122222121111222212111111111111111111"
+ "S,tcp_cache_data"
+ "S,tcp_heuristics_data"
+ "SK[%u]: %-30s %s(%d) failed to add RX steering rule for flow_uuid %s (err %d)\n"
+ "SK[%u]: %-30s Adding RX flow steering rule: fsw=%p, fe=%p, flow_id=%u\n"
+ "SK[%u]: %-30s Device channel not available for RX flow steering\n"
+ "SK[%u]: %-30s Invalid parameters: fsw=%p, fe=%p\n"
+ "SK[%u]: %-30s Nexus not available for RX flow steering\n"
+ "SK[%u]: %-30s RX flow steering rule add failed (err %d)\n"
+ "SK[%u]: %-30s Successfully added RX flow steering rule: flow_id=%u\n"
+ "TCP cache entries from all buckets"
+ "TCP heuristics entries from all buckets"
+ "Which actions to take in response to rising VM pressure"
+ "cache_list"
+ "com.apple.private.tcp.cache_list"
+ "com.apple.private.tcp.heuristics_list"
+ "corrupt so_rcv (%s:%d): sb_mb %p m_len: %d m_type: %u sb_cc %u sb_ctl %u\n @%s:%d"
+ "darwin-init-system"
+ "flow_entry_add_rx_steering_rule"
+ "heuristics_list"
+ "imgsrcdev"
+ "imgsrcinfo"
+ "memorystatus_pressure_config"
+ "site.struct dlil_ifnet"
+ "site.struct tcpstat_local"
+ "site.struct udpstat_local"
+ "tcp_run_timerlist done: processed_count %u > num_entries %u current %u"
+ "tp->tentry.te_index == TCPT_NONE || tp->tentry.te_mode > 0"
+ "unrestricted-subsystem-root"
- "%s disable ECN until %u now %u on %lx for SYN-RST\n"
- "%s disable ECN until %u now %u on %lx for drop-RST\n"
- "%s: Resetting synrst from %u on heur %lx\n"
- "%s: dl_if %p has no debug structure @%s:%d"
- "((intptr_t)base + object_size) <= ((intptr_t)buf + buffer_size)"
- "2211111111111112222222112222211222221111112222111111222222222111211112122222222222222222222222222222222222222222222222222222222212222221122122222222222222222222222222222222222222222222222222222211222222212112222222222222221211122222222222221222222112222212222222222222222211111112222222222000"
- "SK[%u]: %-30s rx flow steering configuration failed (err %d)\n"
- "corrupt so_rcv: sb_mb %p sb_cc %d\n @%s:%d"
- "dlil_ctl.c"
- "dlil_if_trace"
- "ifnet"
- "ifnet_debug"
- "ifnet_tcpstat"
- "ifnet_udpstat"
- "sbdrop - count not zero @%s:%d"
- "tp->tentry.index == TCPT_NONE || tp->tentry.mode > 0"

```
