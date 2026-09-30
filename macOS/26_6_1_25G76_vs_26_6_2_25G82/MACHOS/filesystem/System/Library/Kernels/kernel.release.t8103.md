## kernel.release.t8103

> `/System/Library/Kernels/kernel.release.t8103`

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
- `__BOOTDATA.__static_ifinit`

```diff

-12377.161.13.0.0
+12377.161.14.0.0
   __TEXT.__const: 0x37100
   __TEXT.__copyio_vectors: 0x150
-  __TEXT.__cstring: 0xa6416
+  __TEXT.__cstring: 0xa64a6
   __TEXT.__os_log: 0x3e0d7
   __TEXT.__thread_starts: 0x0
   __TEXT.__eh_frame: 0x6b0
   __DATA_CONST.__hib_const: 0x6f0
-  __DATA_CONST.__const: 0x180820
+  __DATA_CONST.__const: 0x180960
   __DATA_CONST.__sdt_cstring: 0x6e72
-  __DATA_CONST.__sdt: 0xe478
+  __DATA_CONST.__sdt: 0xe4d8
   __DATA_CONST.__kalloc_type: 0x17240
   __DATA_CONST.__assert: 0x960
   __DATA_CONST.__kalloc_var: 0x7d00

   __DATA_CONST.__mod_init_func: 0x2d8
   __DATA_CONST.__auth_ptr: 0x10
   __TEXT_EXEC.__hib_text: 0x3fb0
-  __TEXT_EXEC.__text: 0x969d60
+  __TEXT_EXEC.__text: 0x96a2f4
   __TEXT_EXEC.__commpage_text: 0x334
   __KLD.__text: 0xb020
   __PPLTEXT.__text: 0x2d198

   __DATA.__data: 0x242c9
   __DATA.__lock_grp: 0x16058
   __DATA.__percpu: 0x4390
-  __DATA.__common: 0x8a490
-  __DATA.__bss: 0x3c3f8
+  __DATA.__common: 0x8a4b0
+  __DATA.__bss: 0x3c408
   __HIBDATA.__data: 0x31
   __HIBDATA.__common: 0x120
   __HIBDATA.__bss: 0x670
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__static_if: 0x140
   __BOOTDATA.__init: 0x5bce8
-  __BOOTDATA.__init_entry_set: 0x13320
+  __BOOTDATA.__init_entry_set: 0x13380
   __BOOTDATA.__static_ifinit: 0x10
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x4fb78
-  __CTF.__ctf: 0xe7695
-  Functions: 22675
+  __CTF.__ctf: 0xe7698
+  Functions: 22676
   Symbols:   6896
-  CStrings:  25785
+  CStrings:  25790
 
CStrings:
+ "VM object is read-only (decmpfs?)\n"
+ "object_readonly_copy_overwrite"
+ "object_readonly_fault"
+ "object_readonly_fault_page"
+ "object_readonly_iopl_request"
```
