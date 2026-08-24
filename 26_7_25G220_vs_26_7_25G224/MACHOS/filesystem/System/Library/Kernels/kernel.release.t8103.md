## kernel.release.t8103

> `System/Library/Kernels/kernel.release.t8103`

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
- `__PPLDATA_CONST.__const`
- `__KLDDATA.__const`
- `__DATA.__data`
- `__BOOTDATA.__static_if`
- `__BOOTDATA.__init`
- `__BOOTDATA.__static_ifinit`

```diff

 12377.161.15.700.19
-  __TEXT.__const: 0x37190
+  __TEXT.__const: 0x37110
   __TEXT.__copyio_vectors: 0x150
-  __TEXT.__cstring: 0xa65a8
+  __TEXT.__cstring: 0xa64f1
   __TEXT.__os_log: 0x3e118
   __TEXT.__thread_starts: 0x0
   __TEXT.__eh_frame: 0x6b0
   __DATA_CONST.__hib_const: 0x6f0
-  __DATA_CONST.__const: 0x1810a0
+  __DATA_CONST.__const: 0x180960
   __DATA_CONST.__sdt_cstring: 0x6e72
   __DATA_CONST.__sdt: 0xe4d8
   __DATA_CONST.__kalloc_type: 0x17240

   __DATA_CONST.__mod_init_func: 0x2d8
   __DATA_CONST.__auth_ptr: 0x10
   __TEXT_EXEC.__hib_text: 0x3fb0
-  __TEXT_EXEC.__text: 0x96c9b8
+  __TEXT_EXEC.__text: 0x96c758
   __TEXT_EXEC.__commpage_text: 0x334
   __KLD.__text: 0xb020
   __PPLTEXT.__text: 0x2d1e8

   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__static_if: 0x140
   __BOOTDATA.__init: 0x5bce8
-  __BOOTDATA.__init_entry_set: 0x13590
+  __BOOTDATA.__init_entry_set: 0x13380
   __BOOTDATA.__static_ifinit: 0x10
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x4fb78
-  __CTF.__ctf: 0xe779d
-  Functions: 22683
+  __CTF.__ctf: 0xe7820
+  Functions: 22682
   Symbols:   6896
-  CStrings:  25805
+  CStrings:  25793
 
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
