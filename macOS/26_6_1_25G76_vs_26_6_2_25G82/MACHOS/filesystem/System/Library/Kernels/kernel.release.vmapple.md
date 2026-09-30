## kernel.release.vmapple

> `/System/Library/Kernels/kernel.release.vmapple`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__eh_frame`
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
   __TEXT.__const: 0x369b0
   __TEXT.__copyio_vectors: 0x150
-  __TEXT.__cstring: 0x995fc
+  __TEXT.__cstring: 0x9968c
   __TEXT.__os_log: 0x3dd1e
   __TEXT.__thread_starts: 0x0
   __TEXT.__eh_frame: 0x6b0
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__const: 0x17f1d8
+  __DATA_CONST.__const: 0x17f318
   __DATA_CONST.__sdt_cstring: 0x6e10
-  __DATA_CONST.__sdt: 0xe478
+  __DATA_CONST.__sdt: 0xe4d8
   __DATA_CONST.__kalloc_type: 0x16f40
   __DATA_CONST.__assert: 0x924
   __DATA_CONST.__kalloc_var: 0x7bc0

   __DATA_CONST.__mod_init_func: 0x2d0
   __DATA_CONST.__auth_ptr: 0x10
   __TEXT_EXEC.__hib_text: 0xed8
-  __TEXT_EXEC.__text: 0x943d64
+  __TEXT_EXEC.__text: 0x94430c
   __TEXT_EXEC.__commpage_text: 0x334
   __KLD.__text: 0xb020
   __LASTDATA_CONST.__mod_init_func: 0x8

   __DATA.__data: 0x24289
   __DATA.__lock_grp: 0x159f0
   __DATA.__percpu: 0x3990
-  __DATA.__common: 0x87b30
-  __DATA.__bss: 0x3e548
+  __DATA.__common: 0x87b50
+  __DATA.__bss: 0x3e558
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__init: 0x5b9c8
-  __BOOTDATA.__init_entry_set: 0x12ca8
+  __BOOTDATA.__init_entry_set: 0x12d08
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0
   __PRELINK_TEXT.__text: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x4f6cb
-  __CTF.__ctf: 0xecbce
-  Functions: 21781
+  __CTF.__ctf: 0xecc10
+  Functions: 21782
   Symbols:   6874
-  CStrings:  24673
+  CStrings:  24678
 
CStrings:
+ "VM object is read-only (decmpfs?)\n"
+ "object_readonly_copy_overwrite"
+ "object_readonly_fault"
+ "object_readonly_fault_page"
+ "object_readonly_iopl_request"
```
