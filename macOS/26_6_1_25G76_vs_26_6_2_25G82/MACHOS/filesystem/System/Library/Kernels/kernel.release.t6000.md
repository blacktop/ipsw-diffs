## kernel.release.t6000

> `/System/Library/Kernels/kernel.release.t6000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__hib_const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__assert`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__kern_brk_desc`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__auth_ptr`
- `__KLDDATA.__const`
- `__DATA.__data`
- `__BOOTDATA.__init`

```diff

-12377.161.13.0.0
+12377.161.14.0.0
   __TEXT.__const: 0x36e50
   __TEXT.__copyio_vectors: 0x150
-  __TEXT.__cstring: 0xa00ba
+  __TEXT.__cstring: 0xa014a
   __TEXT.__os_log: 0x3e0d7
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x310
   __DATA_CONST.__sdt_cstring: 0x6e72
-  __DATA_CONST.__sdt: 0xe478
+  __DATA_CONST.__sdt: 0xe4d8
   __DATA_CONST.__kalloc_type: 0x17240
-  __DATA_CONST.__const: 0x12d258
+  __DATA_CONST.__const: 0x12d398
   __DATA_CONST.__assert: 0x938
   __DATA_CONST.__kalloc_var: 0x7d00
   __DATA_CONST.__kern_brk_desc: 0x60

   __DATA_CONST.__auth_ptr: 0x10
   __DATA_SPTM.__const: 0x54000
   __TEXT_EXEC.__hib_text: 0x17bc
-  __TEXT_EXEC.__text: 0x9772a4
+  __TEXT_EXEC.__text: 0x977798
   __TEXT_EXEC.__commpage_text: 0x334
   __TEXT_BOOT_EXEC.__bootcode: 0x5340
   __KLD.__text: 0xb020

   __DATA.__data: 0x24491
   __DATA.__lock_grp: 0x16808
   __DATA.__percpu: 0x7850
-  __DATA.__common: 0x9c630
-  __DATA.__bss: 0x48908
+  __DATA.__common: 0x9c650
+  __DATA.__bss: 0x48918
   __HIBDATA.__data: 0x41
   __HIBDATA.__bss: 0x670
   __HIBDATA.__common: 0x108
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__static_if: 0x140
   __BOOTDATA.__init: 0x5be08
-  __BOOTDATA.__init_entry_set: 0x13338
+  __BOOTDATA.__init_entry_set: 0x13398
   __BOOTDATA.__static_ifinit: 0x10
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x4fb78
-  __CTF.__ctf: 0xe4632
-  Functions: 22450
+  __CTF.__ctf: 0xe46c3
+  Functions: 22451
   Symbols:   6896
-  CStrings:  25323
+  CStrings:  25328
 
CStrings:
+ "VM object is read-only (decmpfs?)\n"
+ "object_readonly_copy_overwrite"
+ "object_readonly_fault"
+ "object_readonly_fault_page"
+ "object_readonly_iopl_request"
```
