## com.apple.kernel

> `com.apple.kernel`

```diff

-12377.60.50.0.6
-  __TEXT.__const: 0x351a0
+12377.62.9.0.0
+  __TEXT.__const: 0x35450
   __TEXT.__copyio_vectors: 0x2c0
-  __TEXT.__cstring: 0x80137
+  __TEXT.__cstring: 0x80266
   __TEXT.__os_log: 0x3c5cb
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2d8
-  __DATA_CONST.__const: 0x117438
+  __DATA_CONST.__const: 0x1177a8
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__kalloc_type: 0x141c0
+  __DATA_CONST.__kalloc_type: 0x14200
   __DATA_CONST.__assert: 0x8fc
   __DATA_CONST.__kalloc_var: 0x7b20
   __DATA_CONST.__exclaves_bt: 0x78
   __DATA_CONST.__kern_brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
-  __TEXT_EXEC.__text: 0x8b2e30
+  __TEXT_EXEC.__text: 0x8b45c4
   __TEXT_EXEC.__hib_text: 0xf38
   __TEXT_BOOT_EXEC.__bootcode: 0x51d0
   __KLD.__text: 0x1638

   __DATA.__data: 0x17f79
   __DATA.__lock_grp: 0x5bc8
   __DATA.__percpu: 0x6f28
-  __DATA.__common: 0x6ec40
+  __DATA.__common: 0x6ec78
   __DATA.__bss: 0x97228
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__static_if: 0x4d30
-  __BOOTDATA.__init_entry_set: 0x12870
+  __BOOTDATA.__init_entry_set: 0x12990
   __BOOTDATA.__init: 0x5b3c8
   __BOOTDATA.__static_ifinit: 0x8
   __PRELINK_TEXT.__text: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x471ae
-  UUID: A218D4C8-7B74-39FB-B863-E06AF3F1D37D
-  Functions: 20751
+  UUID: 51F5806A-8A8E-362F-959A-A5BE0D80A1A0
+  Functions: 20763
   Symbols:   0
-  CStrings:  20269
+  CStrings:  20283
 
CStrings:
+ "\"TB_FATAL: \" \"Attempt to retrieve reply list in environment without large message support\" @%s:%d"
+ "%s: map %p va 0x%llx obj %p,%llu saved %p,%llu: unexpected CoW @%s:%d"
+ "322222"
+ "Enable RTO deadline"
+ "Expected %u seed bytes from bootloader, but got %u.\n @%s:%d"
+ "J427"
+ "J527"
+ "J700"
+ "RTO deadline sojourn factor (50-100)"
+ "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[41c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
+ "exclaves_sensor_tick_loop"
+ "rto_deadline_sojourn_factor"
+ "use_rto_deadline"
+ "vmwls_bad_addr"
+ "vmwls_bad_cow"
+ "vmwls_bad_file"
+ "vmwls_bad_offset"
+ "vmwls_bad_prot"
+ "vmwls_bad_shadows"
+ "vmwls_overflow"
+ "vmwls_total_fail"
+ "vmwls_total_success"
- "%s: map %p va 0x%llx obj %p,%u saved %p,%u: unexpected CoW @%s:%d"
- "32222"
- "Early boot random cchkdf_expand %s failed with err %d @%s:%d"
- "Expected %u seed bytes from bootloader, but got %u. @%s:%d"
- "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[40c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
- "bootseed_init"
- "entropy_init"
- "prngseed_init"

```
