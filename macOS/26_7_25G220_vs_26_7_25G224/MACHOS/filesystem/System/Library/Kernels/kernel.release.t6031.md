## kernel.release.t6031

> `System/Library/Kernels/kernel.release.t6031`

### Sections with Same Size but Changed Content

- `__TEXT.__copyio_vectors`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__hib_const`
- `__DATA_CONST.__sdt`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__assert`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__auth_ptr`
- `__KLDDATA.__const`
- `__DATA.__data`
- `__BOOTDATA.__init`

```diff

 12377.161.15.700.19
-  __TEXT.__const: 0x36f30
+  __TEXT.__const: 0x36eb0
   __TEXT.__copyio_vectors: 0x150
-  __TEXT.__cstring: 0xa216a
+  __TEXT.__cstring: 0xa20b3
   __TEXT.__os_log: 0x3e172
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x310
   __DATA_CONST.__sdt_cstring: 0x6e72
   __DATA_CONST.__sdt: 0xe4a8
   __DATA_CONST.__kalloc_type: 0x172c0
-  __DATA_CONST.__const: 0x12e520
+  __DATA_CONST.__const: 0x12dde0
   __DATA_CONST.__assert: 0x94c
   __DATA_CONST.__kalloc_var: 0x7ee0
   __DATA_CONST.__kern_brk_desc: 0x60

   __DATA_CONST.__auth_ptr: 0x10
   __DATA_SPTM.__const: 0x54000
   __TEXT_EXEC.__hib_text: 0x17e4
-  __TEXT_EXEC.__text: 0x966468
+  __TEXT_EXEC.__text: 0x966218
   __TEXT_EXEC.__commpage_text: 0x334
   __TEXT_BOOT_EXEC.__bootcode: 0x5330
   __KLD.__text: 0xaf48

   __HIBDATA.__common: 0x108
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__init: 0x5bee8
-  __BOOTDATA.__init_entry_set: 0x137a0
+  __BOOTDATA.__init_entry_set: 0x13590
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0
   __PRELINK_TEXT.__text: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x4fb78
-  __CTF.__ctf: 0xe8098
-  Functions: 22525
+  __CTF.__ctf: 0xe8035
+  Functions: 22524
   Symbols:   6896
-  CStrings:  25550
+  CStrings:  25538
 
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
