## com.apple.kernel

> `com.apple.kernel`

```diff

-12377.40.103.502.2
-  __TEXT.__const: 0x35230
+12377.40.120.502.1
+  __TEXT.__const: 0x34f60
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x7e4b0
-  __TEXT.__os_log: 0x3c50a
+  __TEXT.__cstring: 0x7e7b2
+  __TEXT.__os_log: 0x3c58f
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2d8
-  __DATA_CONST.__const: 0xadf58
+  __DATA_CONST.__const: 0xae1e8
   __DATA_CONST.__hib_const: 0x120
   __DATA_CONST.__kalloc_type: 0x141c0
   __DATA_CONST.__assert: 0x5dc

   __DATA_CONST.__exclaves_bt: 0x78
   __DATA_CONST.__kern_brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
-  __TEXT_EXEC.__text: 0x8938fc
+  __TEXT_EXEC.__text: 0x894010
   __TEXT_EXEC.__hib_text: 0xe38
   __TEXT_BOOT_EXEC.__bootcode: 0x523c
   __KLD.__text: 0x1818

   __KLDDATA.__const: 0x33f0
   __KLDDATA.__bss: 0x1
   __DATA.__data: 0x17f39
-  __DATA.__lock_grp: 0x5b70
+  __DATA.__lock_grp: 0x5c20
   __DATA.__percpu: 0x6f08
-  __DATA.__common: 0x5c860
-  __DATA.__bss: 0x96fc8
+  __DATA.__common: 0x5c8a0
+  __DATA.__bss: 0x97028
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__static_if: 0x4d20
-  __BOOTDATA.__init_entry_set: 0x11eb0
-  __BOOTDATA.__init: 0x5b288
+  __BOOTDATA.__static_if: 0x4d30
+  __BOOTDATA.__init_entry_set: 0x11fe8
+  __BOOTDATA.__init: 0x5b348
   __BOOTDATA.__static_ifinit: 0x8
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x471ae
-  UUID: 527AAC9C-9AF3-365D-A640-B36EE0EF5B2E
-  Functions: 20660
+  UUID: 11BE8B11-B8F7-3FFC-9294-4412611AD495
+  Functions: 20665
   Symbols:   0
-  CStrings:  20064
+  CStrings:  20085
 
CStrings:
+ "11222212232122222222222222222222222222222222222222222222222"
+ "Duration of RLC bucket in milliseconds for the ICMP port unreachable run-length-compression"
+ "Duration of RLC bucket in milliseconds for the RST run-length-compression"
+ "Early boot random cchkdf_expand %s failed with err %d @%s:%d"
+ "Enable ICMP port unreachable run-length-compression"
+ "Enable RST run-length-compression"
+ "Expected %u seed bytes from bootloader, but got %u. @%s:%d"
+ "Include timestamp in ICMP port unreachable run-length-compression"
+ "Include timestamp in RST run-length-compression"
+ "RST RLC compression: compressed %u RST segments [%hu:%hu]"
+ "UDP port unreachable RLC compression: compressed %u ICMP packets [%hu:%hu]"
+ "Verbose output: 0: no output; 1: log whenever the ICMP port unreachable RLC buffer changes"
+ "Verbose output: 0: no output; 1: log whenever the RST RLC buffer changes"
+ "bootseed_init"
+ "entropy_init"
+ "matrix saved state"
+ "port_unreach_rlc_bucket_ms"
+ "port_unreach_rlc_enable"
+ "port_unreach_rlc_use_ts"
+ "port_unreach_rlc_verbose"
+ "prngseed_init"
+ "rst_rlc_bucket_ms"
+ "rst_rlc_enable"
+ "rst_rlc_use_ts"
+ "rst_rlc_verbose"
- "112222112232122222222222222222222222222222222222222222222222"
- "AMX save state"
- "Expected %u seed bytes from bootloader, but got %u.\n @%s:%d"
- "SME saved state"

```
