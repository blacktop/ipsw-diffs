## kernel.release.vmapple

> `System/Library/Kernels/kernel.release.vmapple`

### Sections with Same Size but Changed Content

- `__TEXT.__copyio_vectors`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__sdt`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__assert`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__kern_brk_desc`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__auth_ptr`
- `__LASTDATA_CONST.__mod_init_func`
- `__KLDDATA.__const`
- `__KLDDATA.__mod_init_func`
- `__KLDDATA.__mod_term_func`
- `__DATA.__data`
- `__BOOTDATA.__init`
- `__BOOTDATA.__static_ifinit`

```diff

 12377.161.15.700.19
-  __TEXT.__const: 0x36a40
+  __TEXT.__const: 0x369c0
   __TEXT.__copyio_vectors: 0x150
-  __TEXT.__cstring: 0x9978e
+  __TEXT.__cstring: 0x996d7
   __TEXT.__os_log: 0x3dd5f
   __TEXT.__thread_starts: 0x0
   __TEXT.__eh_frame: 0x6b0
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__const: 0x17fa58
+  __DATA_CONST.__const: 0x17f318
   __DATA_CONST.__sdt_cstring: 0x6e10
   __DATA_CONST.__sdt: 0xe4d8
   __DATA_CONST.__kalloc_type: 0x16f40

   __DATA_CONST.__mod_init_func: 0x2d0
   __DATA_CONST.__auth_ptr: 0x10
   __TEXT_EXEC.__hib_text: 0xed8
-  __TEXT_EXEC.__text: 0x946a24
+  __TEXT_EXEC.__text: 0x946768
   __TEXT_EXEC.__commpage_text: 0x334
   __KLD.__text: 0xb020
   __LASTDATA_CONST.__mod_init_func: 0x8

   __DATA.__common: 0x87b50
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__init: 0x5b9c8
-  __BOOTDATA.__init_entry_set: 0x12f18
+  __BOOTDATA.__init_entry_set: 0x12d08
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0
   __PRELINK_TEXT.__text: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x4f6cb
-  __CTF.__ctf: 0xece05
-  Functions: 21789
+  __CTF.__ctf: 0xecd46
+  Functions: 21788
   Symbols:   6874
-  CStrings:  24693
+  CStrings:  24681
 
CStrings:
- "FEAT_CPA"
- "FEAT_CPA2"
- "FEAT_FAMINMAX"
- "FEAT_FP8"
- "FEAT_FPMR"
- "FEAT_LUT"
- "FEAT_PAuth_LR"
- "FEAT_SME_F8F16"
- "FEAT_SME_F8F32"
- "FEAT_SME_LUTv2"
- "Perf level 2 topology and cache geometry parameters"
- "perflevel2"
```
