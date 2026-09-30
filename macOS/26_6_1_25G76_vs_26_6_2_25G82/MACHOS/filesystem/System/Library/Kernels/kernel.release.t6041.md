## kernel.release.t6041

> `/System/Library/Kernels/kernel.release.t6041`

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
   __TEXT.__const: 0x36ea0
   __TEXT.__copyio_vectors: 0x150
-  __TEXT.__cstring: 0xa2196
+  __TEXT.__cstring: 0xa2226
   __TEXT.__os_log: 0x3e131
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x310
   __DATA_CONST.__sdt_cstring: 0x6e72
-  __DATA_CONST.__sdt: 0xe448
+  __DATA_CONST.__sdt: 0xe4a8
   __DATA_CONST.__kalloc_type: 0x172c0
-  __DATA_CONST.__const: 0x12d540
+  __DATA_CONST.__const: 0x12d680
   __DATA_CONST.__assert: 0x94c
   __DATA_CONST.__kalloc_var: 0x7e40
   __DATA_CONST.__kern_brk_desc: 0x60

   __DATA_CONST.__auth_ptr: 0x10
   __DATA_SPTM.__const: 0x54000
   __TEXT_EXEC.__hib_text: 0x17e8
-  __TEXT_EXEC.__text: 0x96673c
+  __TEXT_EXEC.__text: 0x966c38
   __TEXT_EXEC.__commpage_text: 0x334
   __TEXT_BOOT_EXEC.__bootcode: 0x5330
   __KLD.__text: 0xaf48

   __DATA.__data: 0x24451
   __DATA.__lock_grp: 0x16be0
   __DATA.__percpu: 0x6730
-  __DATA.__common: 0x8f600
-  __DATA.__bss: 0x544b8
+  __DATA.__common: 0x8f620
+  __DATA.__bss: 0x544c8
   __HIBDATA.__data: 0x31
   __HIBDATA.__bss: 0x670
   __HIBDATA.__common: 0x108
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__init: 0x5bee0
-  __BOOTDATA.__init_entry_set: 0x13500
+  __BOOTDATA.__init_entry_set: 0x13560
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0
   __PRELINK_TEXT.__text: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x4fb78
-  __CTF.__ctf: 0xe80ac
-  Functions: 22523
+  __CTF.__ctf: 0xe812a
+  Functions: 22524
   Symbols:   6896
-  CStrings:  25563
+  CStrings:  25568
 
CStrings:
+ "VM object is read-only (decmpfs?)\n"
+ "object_readonly_copy_overwrite"
+ "object_readonly_fault"
+ "object_readonly_fault_page"
+ "object_readonly_iopl_request"
```
