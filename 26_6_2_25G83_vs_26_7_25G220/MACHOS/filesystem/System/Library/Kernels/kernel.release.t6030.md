## kernel.release.t6030

> `System/Library/Kernels/kernel.release.t6030`

### Sections with Same Size but Changed Content

- `__TEXT.__copyio_vectors`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__hib_const`
- `__DATA_CONST.__sdt`
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

-12377.161.14.0.0
-  __TEXT.__const: 0x36e90
+12377.161.15.700.19
+  __TEXT.__const: 0x36f10
   __TEXT.__copyio_vectors: 0x150
-  __TEXT.__cstring: 0xa182f
-  __TEXT.__os_log: 0x3e0d7
+  __TEXT.__cstring: 0xa1931
+  __TEXT.__os_log: 0x3e118
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x310
   __DATA_CONST.__sdt_cstring: 0x6e72
   __DATA_CONST.__sdt: 0xe4d8
   __DATA_CONST.__kalloc_type: 0x17240
-  __DATA_CONST.__const: 0x12cf50
+  __DATA_CONST.__const: 0x12d690
   __DATA_CONST.__assert: 0x938
   __DATA_CONST.__kalloc_var: 0x7d00
   __DATA_CONST.__kern_brk_desc: 0x60

   __DATA_CONST.__auth_ptr: 0x10
   __DATA_SPTM.__const: 0x54000
   __TEXT_EXEC.__hib_text: 0x17e4
-  __TEXT_EXEC.__text: 0x95f1ec
+  __TEXT_EXEC.__text: 0x961170
   __TEXT_EXEC.__commpage_text: 0x334
   __TEXT_BOOT_EXEC.__bootcode: 0x5330
   __KLD.__text: 0xaf48

   __DATA.__lock_grp: 0x16a98
   __DATA.__percpu: 0x7890
   __DATA.__common: 0x8ae80
-  __DATA.__bss: 0x48188
+  __DATA.__bss: 0x48238
   __HIBDATA.__data: 0x31
   __HIBDATA.__bss: 0x670
   __HIBDATA.__common: 0x108
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__init: 0x5be70
-  __BOOTDATA.__init_entry_set: 0x133c8
+  __BOOTDATA.__init_entry_set: 0x135d8
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0
   __PRELINK_TEXT.__text: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x4fb78
-  __CTF.__ctf: 0xe88f0
-  Functions: 22480
+  __CTF.__ctf: 0xe89b0
+  Functions: 22487
   Symbols:   6896
-  CStrings:  25465
+  CStrings:  25480
 
CStrings:
+ "%s: invalid pth_length %u (pkt %zu)"
+ "2211121111111222221112122212222222222222222222222222222222222222222222211111111111111111112112222222221122222222222211212221222221222222222222222222222222222211211112222222222222211112122112221122211222112222221122222222222222222222222111122122122222222221221221222211112222222222222222211222222222222221121222222222111111121122222222222222222222222222222222222211222221222221211112222122111111111111111111"
+ "FEAT_CPA"
+ "FEAT_CPA2"
+ "FEAT_FAMINMAX"
+ "FEAT_FP8"
+ "FEAT_FPMR"
+ "FEAT_LUT"
+ "FEAT_PAuth_LR"
+ "FEAT_SME_F8F16"
+ "FEAT_SME_F8F32"
+ "FEAT_SME_LUTv2"
+ "Perf level 2 topology and cache geometry parameters"
+ "fsw_dev_input_netem_enqueue"
+ "perflevel2"
+ "pf: BAD ICMP %d:%d outer dst != inner src\n"
- "221112111111122222111212221222222222222222222222222222222222222222222221111111111111111111211222222222112222222222221121222122222122222222222222222222222222221121111222222222222221111212211222112221122211222222112222222222222222222222211112212212222222222122122122221111222222222222222221122222222221121222222222111111121122222222222222222222222222222222222211222221222221211112222122111111111111111111"
```
