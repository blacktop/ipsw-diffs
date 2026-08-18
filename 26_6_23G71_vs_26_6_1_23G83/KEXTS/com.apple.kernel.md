## com.apple.kernel

> `com.apple.kernel`

```diff

-12377.162.13.0.0
+12377.162.14.0.0
   __TEXT.__const: 0x36320
   __TEXT.__copyio_vectors: 0x2c0
-  __TEXT.__cstring: 0x84e16
+  __TEXT.__cstring: 0x85054
   __TEXT.__os_log: 0x3e186
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__const: 0x119e70
+  __DATA_CONST.__const: 0x119fb0
   __DATA_CONST.__kalloc_type: 0x14340
-  __DATA_CONST.__assert: 0xc80
+  __DATA_CONST.__assert: 0xd20
   __DATA_CONST.__kalloc_var: 0x78f0
   __DATA_CONST.__exclaves_bt: 0x78
   __DATA_CONST.__kern_brk_desc: 0x60

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xed8
-  __TEXT_EXEC.__text: 0x8a5f40
+  __TEXT_EXEC.__text: 0x8a6624
   __TEXT_BOOT_EXEC.__bootcode: 0x5250
   __KLD.__text: 0x1460
   __LASTDATA_CONST.__mod_init_func: 0x8

   __DATA.__lock_grp: 0x5ac0
   __DATA.__percpu: 0x7870
   __DATA.__common: 0x77618
-  __DATA.__bss: 0xa4130
+  __DATA.__bss: 0xa4140
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init_entry_set: 0x135d8
+  __BOOTDATA.__init_entry_set: 0x13638
   __BOOTDATA.__init: 0x5b5c8
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x48096
-  Functions: 21143
+  Functions: 21146
   Symbols:   0
-  CStrings:  20320
+  CStrings:  20334
 
CStrings:
+ "VM object is read-only (decmpfs?)\n"
+ "exclaves_memory_pa_page_is_sk_shared_ro(paddr)"
+ "exclaves_memory_pa_page_is_sk_shared_ro(page_paddr)"
+ "exclaves_memory_pa_page_is_sk_shared_ro(trunc_page_64(curr_addr))"
+ "exclaves_memory_pa_page_is_sk_shared_rw(trunc_page_64(ipcb_paddr))"
+ "exclaves_xnuproxy.c"
+ "i < scid_list_count"
+ "idx < page_count"
+ "object_readonly_copy_overwrite"
+ "object_readonly_fault"
+ "object_readonly_fault_page"
+ "object_readonly_iopl_request"
+ "output_length <= EXCLAVES_STACKSHOT_BUFFER_SIZE"
+ "trunc_page_64(ipcb_paddr) == trunc_page_64(ipcb_paddr + sizeof(Exclaves_L4_IpcBuffer_t) - 1)"
```
