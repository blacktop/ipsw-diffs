## com.apple.kernel

> `com.apple.kernel`

```diff

-12377.120.91.0.1
-  __TEXT.__const: 0x36170
+12377.120.99.0.7
+  __TEXT.__const: 0x363e0
   __TEXT.__copyio_vectors: 0x2c0
-  __TEXT.__cstring: 0x884f6
-  __TEXT.__os_log: 0x3dea0
+  __TEXT.__cstring: 0x88592
+  __TEXT.__os_log: 0x3df0f
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__const: 0x119d88
-  __DATA_CONST.__kalloc_type: 0x14600
+  __DATA_CONST.__const: 0x119da0
+  __DATA_CONST.__kalloc_type: 0x14640
   __DATA_CONST.__assert: 0xc58
   __DATA_CONST.__kalloc_var: 0x78f0
   __DATA_CONST.__exclaves_bt: 0x78

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xed8
-  __TEXT_EXEC.__text: 0x8b563c
+  __TEXT_EXEC.__text: 0x8b6cdc
   __TEXT_BOOT_EXEC.__bootcode: 0x5250
   __KLD.__text: 0x1460
   __LASTDATA_CONST.__mod_init_func: 0x8

   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
   __DATA.__data: 0x17ff9
-  __DATA.__lock_grp: 0x5b18
+  __DATA.__lock_grp: 0x5b70
   __DATA.__percpu: 0x7870
   __DATA.__common: 0x77778
-  __DATA.__bss: 0xa3778
+  __DATA.__bss: 0xa3dc8
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init_entry_set: 0x135a8
-  __BOOTDATA.__init: 0x5b568
+  __BOOTDATA.__init_entry_set: 0x135f0
+  __BOOTDATA.__init: 0x5b5c8
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0
   __PRELINK_TEXT.__text: 0x0

   __PLK_DATA_CONST.__data: 0x0
   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
-  __LINKINFO.__symbolsets: 0x48024
-  UUID: D6F662A4-FFA2-3C33-89B2-8074D2C0EC7E
-  Functions: 21327
+  __LINKINFO.__symbolsets: 0x4804e
+  UUID: E9066B72-405C-314B-82C9-C674B6CA3355
+  Functions: 21334
   Symbols:   0
-  CStrings:  20745
+  CStrings:  20748
 
CStrings:
+ "(%u): Token contains a signing identifier and HMAC is missing\n"
+ "vm: swapin for segment %d failed with error %d\n"
+ "zalloc_ro_mut failed: source (%p, phys %p) not from RO zone map (%p - %p), current stack (%p - %p), redzone (%p - %p) or const memory (phys %p - %p) @%s:%d"

```
