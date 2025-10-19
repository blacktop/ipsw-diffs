## com.apple.kernel

> `com.apple.kernel`

```diff

-12377.40.103.502.2
-  __TEXT.__const: 0x35450
+12377.40.120.502.1
+  __TEXT.__const: 0x35180
   __TEXT.__copyio_vectors: 0x2c0
-  __TEXT.__cstring: 0x7fd06
-  __TEXT.__os_log: 0x3c50a
+  __TEXT.__cstring: 0x80008
+  __TEXT.__os_log: 0x3c58f
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2d8
-  __DATA_CONST.__const: 0x117180
+  __DATA_CONST.__const: 0x117410
   __DATA_CONST.__hib_const: 0x120
   __DATA_CONST.__kalloc_type: 0x14200
   __DATA_CONST.__assert: 0x8fc

   __DATA_CONST.__exclaves_bt: 0x78
   __DATA_CONST.__kern_brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
-  __TEXT_EXEC.__text: 0x8b147c
+  __TEXT_EXEC.__text: 0x8b1a6c
   __TEXT_EXEC.__hib_text: 0xf38
   __TEXT_BOOT_EXEC.__bootcode: 0x51d0
   __KLD.__text: 0x1638

   __KLDDATA.__const: 0x34c0
   __KLDDATA.__bss: 0x1
   __DATA.__data: 0x17f79
-  __DATA.__lock_grp: 0x5b18
+  __DATA.__lock_grp: 0x5bc8
   __DATA.__percpu: 0x6f28
-  __DATA.__common: 0x6ec00
-  __DATA.__bss: 0x971c8
+  __DATA.__common: 0x6ec40
+  __DATA.__bss: 0x97228
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__static_if: 0x4d20
-  __BOOTDATA.__init_entry_set: 0x126d8
-  __BOOTDATA.__init: 0x5b2f0
+  __BOOTDATA.__static_if: 0x4d30
+  __BOOTDATA.__init_entry_set: 0x12810
+  __BOOTDATA.__init: 0x5b3b0
   __BOOTDATA.__static_ifinit: 0x8
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x471ae
-  UUID: ED7299F6-8580-30C4-8E8E-8B6368FB4401
-  Functions: 20743
+  UUID: 2D5AC777-C3A9-3CFD-A271-F79F6D86529F
+  Functions: 20748
   Symbols:   0
-  CStrings:  20237
+  CStrings:  20258
 
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
