## kernel.release.t8142

> `System/Library/Kernels/kernel.release.t8142`

### Sections with Same Size but Changed Content

- `__TEXT.__copyio_vectors`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__hib_const`
- `__DATA_CONST.__sdt`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__assert`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__exclaves_bt`
- `__DATA_CONST.__kern_brk_desc`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__auth_ptr`
- `__LASTDATA_CONST.__mod_init_func`
- `__KLDDATA.__const`
- `__KLDDATA.__mod_init_func`
- `__KLDDATA.__mod_term_func`
- `__DATA.__data`
- `__HIBDATA.__data`
- `__BOOTDATA.__init`
- `__BOOTDATA.__static_ifinit`

```diff

 12377.161.15.700.19
-  __TEXT.__const: 0x37d70
+  __TEXT.__const: 0x37ce0
   __TEXT.__copyio_vectors: 0x340
-  __TEXT.__cstring: 0xae11b
+  __TEXT.__cstring: 0xadc99
   __TEXT.__os_log: 0x3e2d8
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x310
   __DATA_CONST.__sdt_cstring: 0x6e9e
   __DATA_CONST.__sdt: 0xe640
   __DATA_CONST.__kalloc_type: 0x17880
-  __DATA_CONST.__const: 0x133070
+  __DATA_CONST.__const: 0x132930
   __DATA_CONST.__assert: 0xd0c
   __DATA_CONST.__kalloc_var: 0x8110
   __DATA_CONST.__exclaves_bt: 0x78

   __DATA_CONST.__auth_ptr: 0x10
   __DATA_SPTM.__const: 0x54000
   __TEXT_EXEC.__hib_text: 0x17c8
-  __TEXT_EXEC.__text: 0x9a7ecc
+  __TEXT_EXEC.__text: 0x9a679c
   __TEXT_EXEC.__commpage_text: 0x334
   __TEXT_BOOT_EXEC.__bootcode: 0x5250
   __KLD.__text: 0xad68

   __HIBDATA.__common: 0x108
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__init: 0x5bf90
-  __BOOTDATA.__init_entry_set: 0x14118
+  __BOOTDATA.__init_entry_set: 0x13f08
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0
   __PRELINK_TEXT.__text: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x4fb78
-  __CTF.__ctf: 0x10b97e
-  Functions: 23210
+  __CTF.__ctf: 0x10b5b5
+  Functions: 23197
   Symbols:   6896
-  CStrings:  26241
+  CStrings:  26218
 
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
- "TB_FATAL: invalid result returned from accessorySensorStart @%s:%d"
- "TB_FATAL: invalid result returned from accessorySensorStatus @%s:%d"
- "TB_FATAL: invalid result returned from accessorySensorStop @%s:%d"
- "TB_FATAL: invalid result returned from copyAccessoryBuffer @%s:%d"
- "perflevel2"
- "unknown sensor type @%s:%d"
- "unsupported eic accessory sensor type @%s:%d"
- "unsupported eic devicetype @%s:%d"
- "v24@?0{exclaveindicatorcontroller_accessorysensorrequest_accessorysensorstart__result_s=C(?={exclaveindicatorcontroller_accessorysensorerror_s=Q}Q)}8"
- "v24@?0{exclaveindicatorcontroller_accessorysensorrequest_accessorysensorstatus__result_s=C(?={exclaveindicatorcontroller_accessorysensorerror_s=Q}Q)}8"
- "v24@?0{exclaveindicatorcontroller_accessorysensorrequest_accessorysensorstop__result_s=C(?={exclaveindicatorcontroller_accessorysensorerror_s=Q})}8"
- "v24@?0{exclaveindicatorcontroller_accessorysensorrequest_copyaccessorybuffer__result_s=C(?={exclaveindicatorcontroller_accessorysensorerror_s=Q}Q)}8"
```
