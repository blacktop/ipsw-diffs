## com.apple.kernel

> `com.apple.kernel`

```diff

-12377.120.72.0.4
-  __TEXT.__const: 0x36160
+12377.120.91.0.1
+  __TEXT.__const: 0x36170
   __TEXT.__copyio_vectors: 0x2c0
-  __TEXT.__cstring: 0x8864d
-  __TEXT.__os_log: 0x3decf
+  __TEXT.__cstring: 0x884f6
+  __TEXT.__os_log: 0x3dea0
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__const: 0x119ed8
+  __DATA_CONST.__const: 0x119d88
   __DATA_CONST.__kalloc_type: 0x14600
-  __DATA_CONST.__assert: 0xd84
+  __DATA_CONST.__assert: 0xc58
   __DATA_CONST.__kalloc_var: 0x78f0
   __DATA_CONST.__exclaves_bt: 0x78
   __DATA_CONST.__kern_brk_desc: 0x78

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xed8
-  __TEXT_EXEC.__text: 0x8b61e0
+  __TEXT_EXEC.__text: 0x8b563c
   __TEXT_BOOT_EXEC.__bootcode: 0x5250
   __KLD.__text: 0x1460
   __LASTDATA_CONST.__mod_init_func: 0x8
   __LAST.__pinst: 0x8
   __LAST.__last: 0x0
   __KLDDATA.__cstring: 0x6e1
-  __KLDDATA.__const: 0x37e0
+  __KLDDATA.__const: 0x3740
   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
   __DATA.__data: 0x17ff9
   __DATA.__lock_grp: 0x5b18
   __DATA.__percpu: 0x7870
-  __DATA.__common: 0x79878
-  __DATA.__bss: 0xa3788
+  __DATA.__common: 0x77778
+  __DATA.__bss: 0xa3778
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init_entry_set: 0x13710
-  __BOOTDATA.__init: 0x5b588
+  __BOOTDATA.__init_entry_set: 0x135a8
+  __BOOTDATA.__init: 0x5b568
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0
   __PRELINK_TEXT.__text: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x48024
-  UUID: 08A433C2-096A-35E0-B242-53832764ADB7
-  Functions: 21320
+  UUID: D6F662A4-FFA2-3C33-89B2-8074D2C0EC7E
+  Functions: 21327
   Symbols:   0
-  CStrings:  20753
+  CStrings:  20745
 
CStrings:
+ "AP-M"
+ "LPW UDP unicast"
+ "M-core"
+ "node >= 0 && heap->size > node"
+ "recount: cannot map cluster type %d to CPU kind @%s:%d"
+ "udp6_proto_process_lpw_packet"
+ "udp_proto_process_lpw_packet"
+ "v344@?0{exclaveindicatorcontroller_sensorrequestmetrics_s=QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ}8"
- "!os_sub_overflow(*__counter, free_page_count, __counter)"
- "active tag storages with free covered pages intended for kernel-tagged allocations"
- "active_kernel"
- "cpu_kernel_tagged"
- "free kernel-tagged pages in the MTE free queue"
- "free tagged pages for zalloc in CPU lists"
- "heap->size <= node"
- "kernel_tagged"
- "number of active tag storage pages supporting kernel allocators"
- "recount: unexpected topography %d @%s:%d"
- "recount_coalition_plan"
- "recount_task_terminated_plan"
- "tag_storage_active_kernel"
- "tagged pages in use by zalloc"
- "tagged_kernel"
- "v304@?0{exclaveindicatorcontroller_sensorrequestmetrics_s=QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ}8"

```
