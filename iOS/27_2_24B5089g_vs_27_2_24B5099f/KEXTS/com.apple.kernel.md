## com.apple.kernel

> `com.apple.kernel`

```diff

-13432.40.162.0.0
-  __TEXT.__const: 0x372d0
+13432.40.177.0.3
+  __TEXT.__const: 0x372e0
   __TEXT.__copyio_vectors: 0x2c0
-  __TEXT.__cstring: 0x90363
-  __TEXT.__os_log: 0x41edb
+  __TEXT.__cstring: 0x903d7
+  __TEXT.__os_log: 0x41fdc
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__const: 0x121070
+  __DATA_CONST.__const: 0x121048
   __DATA_CONST.__kalloc_type: 0x153c0
-  __DATA_CONST.__assert: 0x161c
+  __DATA_CONST.__assert: 0x1630
   __DATA_CONST.__kalloc_var: 0x8020
   __DATA_CONST.__exclaves_bt: 0xc0
   __DATA_CONST.__kern_brk_desc: 0x78

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_SPTM.__const: 0x4c000
   __TEXT_EXEC.__exc: 0x1000
-  __TEXT_EXEC.__text: 0x90ae18
+  __TEXT_EXEC.__text: 0x90bbe8
   __TEXT_EXEC.__hib_text: 0x10d8
   __TEXT_BOOT_EXEC.__bootcode: 0x6a2c
   __KLD.__text: 0x173c

   __DATA.__common: 0x7b9a8
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__static_if: 0xdd0
-  __BOOTDATA.__init_entry_set: 0x14eb0
+  __BOOTDATA.__init_entry_set: 0x14e98
   __BOOTDATA.__init: 0x17938
   __BOOTDATA.__static_ifinit: 0x18
   __PRELINK_TEXT.__text: 0x0

   __PLK_DATA_CONST.__data: 0x0
   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
-  __LINKINFO.__symbolsets: 0x48d7b
-  Functions: 22042
+  __LINKINFO.__symbolsets: 0x48de8
+  Functions: 22050
   Symbols:   0
-  CStrings:  21331
+  CStrings:  21339
 
CStrings:
+ "11111122"
+ "22111220222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222220222121222221111111222211111112222211111122222111111222221111112222211222211122211112111111111111"
+ "FilterDropBadDirection"
+ "SK[%u]: %-30s dropped packet injected on ring %u whose wrap flag does not match the ring direction: pkt_pflags 0x%llx\n"
+ "SK[%u]: %-30s filter packet is not mbuf-wrapped: pkt_pflags 0x%llx\n"
+ "SK[%u]: %-30s filter packet is not packet-wrapped: pkt_pflags 0x%llx\n"
+ "com.apple.private.vfs.unmunged-access-time"
+ "com.apple.security.cs.debugger"
+ "nx_netif_filter_pkt_to_mbuf"
+ "nx_netif_filter_pkt_to_pkt"
+ "ret == TB_ERROR_SUCCESS"
- "221112202222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121222221111111222211111112222211111122222111111222221111112222211222211122211112111111111111"
- "protect_privileged_from_untrusted"
- "vm_protect_privileged_from_untrusted"
```
