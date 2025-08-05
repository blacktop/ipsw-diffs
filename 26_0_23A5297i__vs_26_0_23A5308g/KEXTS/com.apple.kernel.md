## com.apple.kernel

> `com.apple.kernel`

```diff

-12377.0.154.0.2
-  __TEXT.__const: 0x34bc0
+12377.0.187.0.2
+  __TEXT.__const: 0x34be0
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x7d68d
-  __TEXT.__os_log: 0x3c0c4
+  __TEXT.__cstring: 0x7d828
+  __TEXT.__os_log: 0x3c2f3
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2d8
-  __DATA_CONST.__const: 0xacba8
+  __DATA_CONST.__const: 0xacd08
   __DATA_CONST.__hib_const: 0x120
   __DATA_CONST.__kalloc_type: 0x14180
   __DATA_CONST.__assert: 0x5dc

   __DATA_CONST.__exclaves_bt: 0x78
   __DATA_CONST.__kern_brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
-  __TEXT_EXEC.__text: 0x8936d0
+  __TEXT_EXEC.__text: 0x89104c
   __TEXT_EXEC.__hib_text: 0xe38
-  __TEXT_BOOT_EXEC.__bootcode: 0x5218
+  __TEXT_BOOT_EXEC.__bootcode: 0x523c
   __KLD.__text: 0x1818
   __LASTDATA_CONST.__mod_init_func: 0x8
   __LAST.__pinst: 0x8

   __KLDDATA.__cstring: 0x6e1
   __KLDDATA.__const: 0x3168
   __KLDDATA.__bss: 0x1
-  __DATA.__data: 0x17e29
+  __DATA.__data: 0x17ea9
   __DATA.__lock_grp: 0x5b70
   __DATA.__percpu: 0x6f08
-  __DATA.__common: 0x5c100
-  __DATA.__bss: 0x96cd8
+  __DATA.__common: 0x5c140
+  __DATA.__bss: 0x96dc8
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__static_if: 0x4d10
-  __BOOTDATA.__init_entry_set: 0x11838
+  __BOOTDATA.__init_entry_set: 0x11868
   __BOOTDATA.__init: 0x5b288
   __BOOTDATA.__static_ifinit: 0x8
   __PRELINK_TEXT.__text: 0x0

   __PLK_DATA_CONST.__data: 0x0
   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
-  __LINKINFO.__symbolsets: 0x470a7
-  UUID: 7BB60F77-CC2A-381F-AA30-24CF51327874
-  Functions: 20623
+  __LINKINFO.__symbolsets: 0x470d0
+  UUID: 29368CB4-6F41-3C14-88D8-FFF8319F7974
+  Functions: 20636
   Symbols:   0
-  CStrings:  19929
+  CStrings:  19954
 
CStrings:
+ "ARM_BR_MIS_PRED"
+ "ARM_BR_PRED"
+ "ARM_L1D_CACHE"
+ "ARM_L1D_CACHE_LMISS_RD"
+ "ARM_L1D_CACHE_RD"
+ "ARM_L1D_CACHE_REFILL"
+ "ARM_STALL"
+ "ARM_STALL_BACKEND"
+ "ARM_STALL_FRONTEND"
+ "ARM_STALL_SLOT"
+ "ARM_STALL_SLOT_BACKEND"
+ "ARM_STALL_SLOT_FRONTEND"
+ "Attempted I/O wiring of page with executable mapping\n"
+ "Attempted executable mapping of page already wired for I/O\n"
+ "Attempted writable UPL against executable VM region\n"
+ "LDST_UNIT_WAITING_OLD_L1D_CACHE_MISS"
+ "LDST_UNIT_WAITING_SME_ENGINE_INST_QUEUE_FULL"
+ "LD_UNIT_WAITING_YOUNG_L1D_CACHE_MISS"
+ "already notified attributed wake packet"
+ "com.apple.xnu.net.wake_packet"
+ "copied_on_read_kernel_map"
+ "copied_on_read_platform_map"
+ "dp_rx_process_low_power_wake LPW TCP connection idle"
+ "if_is_lpw_enabled %s set LPW to %d"
+ "if_ports_used_match_mbuf: receive interface is NULL"
+ "if_ports_used_match_pkt: receive interface is NULL"
+ "if_set_wake_physical_interface %s last_wake_phy_if_delay_wake_pkt set"
+ "if_set_wake_physical_interface ignored on %s because already set on %s"
+ "ifclassq instance %p created"
+ "ifclassq instance %p freed"
+ "memorystatus: all victims exhausted @%s:%d"
+ "memorystatus: clearing kill errors and retrying\n"
+ "memorystatus: failed to find a process to kill!\n"
+ "memorystatus: fully draining kernel zone allocator\n"
+ "memorystatus: system still unhealthy after cache purge!\n"
+ "net_port_info_match_npi"
+ "pmap_recycle_page"
+ "sysctl_wake_pkt_event_notify attributed_wake_already_notified"
+ "sysctl_wake_pkt_event_notify bad npi_wp_code"
+ "sysctl_wake_pkt_event_notify in vain"
+ "sysctl_wake_pkt_event_notify proc %s:%u val %u last_wake_phy_if_delay_wake_pkt %d last_wake_phy_if_family %u delay_wake_pkt_event %d"
+ "sysctl_wake_pkt_event_notify unattributed_wake_already_notified"
- "  "
- "%s: receive interface is NULL"
- "LD_UNIT_YOUNG_L1D_CACHE_MISS"
- "MMU_VIRTUAL_MEMORY_FAULT_NONSPEC"
- "SME_ENGINE_INST_QUEUE_FULL"
- "add empty AccECN option, optlen=%u"
- "already notified wake packet"
- "dp_rx_process_wake_packet LPW TCP connection idle"
- "if_is_lpw_enabled %s set LPW to 0"
- "if_is_lpw_enabled %s set LPW to 1"
- "if_notify_unattributed_wake_pkt"
- "low-band "
- "memorystatus: attempting full drain of kernel zone allocator\n"
- "memorystatus: ran out of %sprocesses to kill but system is still in critical condition\n"
- "memorystatus_jetsam_thread: no victim! available pages:%llu @%s:%d"
- "sysctl_wake_pkt_event_notify proc %s:%u val %u last_wake_phy_if_delay_wake_pkt %d last_wake_phy_if_family %u"
- "vm_page_validate_no_references"

```
