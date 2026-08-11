## kernel.release.t8142

> `/System/Library/Kernels/kernel.release.t8142`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__hib_const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__exclaves_bt`
- `__DATA_CONST.__kern_brk_desc`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__auth_ptr`
- `__KLDDATA.__const`
- `__DATA.__data`
- `__BOOTDATA.__init`

```diff

-12377.161.13.0.0
+12377.161.14.0.0
   __TEXT.__const: 0x37ce0
   __TEXT.__copyio_vectors: 0x340
-  __TEXT.__cstring: 0xada10
+  __TEXT.__cstring: 0xadc4e
   __TEXT.__os_log: 0x3e297
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x310
   __DATA_CONST.__sdt_cstring: 0x6e9e
-  __DATA_CONST.__sdt: 0xe5e0
+  __DATA_CONST.__sdt: 0xe640
   __DATA_CONST.__kalloc_type: 0x17880
-  __DATA_CONST.__const: 0x1327f0
-  __DATA_CONST.__assert: 0xc6c
+  __DATA_CONST.__const: 0x132930
+  __DATA_CONST.__assert: 0xd0c
   __DATA_CONST.__kalloc_var: 0x8110
   __DATA_CONST.__exclaves_bt: 0x78
   __DATA_CONST.__kern_brk_desc: 0x60

   __DATA_CONST.__auth_ptr: 0x10
   __DATA_SPTM.__const: 0x54000
   __TEXT_EXEC.__hib_text: 0x17c8
-  __TEXT_EXEC.__text: 0x9a4220
+  __TEXT_EXEC.__text: 0x9a4a5c
   __TEXT_EXEC.__commpage_text: 0x334
   __TEXT_BOOT_EXEC.__bootcode: 0x5250
   __KLD.__text: 0xad68

   __DATA.__lock_grp: 0x17100
   __DATA.__percpu: 0x7880
   __DATA.__common: 0x9b260
-  __DATA.__bss: 0xaa738
+  __DATA.__bss: 0xaa748
   __HIBDATA.__data: 0x31
   __HIBDATA.__bss: 0x670
   __HIBDATA.__common: 0x108
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__init: 0x5bf90
-  __BOOTDATA.__init_entry_set: 0x13ea8
+  __BOOTDATA.__init_entry_set: 0x13f08
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0
   __PRELINK_TEXT.__text: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x4fb78
-  __CTF.__ctf: 0x10af3d
-  Functions: 23188
+  __CTF.__ctf: 0x10b536
+  Functions: 23191
   Symbols:   6896
-  CStrings:  26201
+  CStrings:  26215
 
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
