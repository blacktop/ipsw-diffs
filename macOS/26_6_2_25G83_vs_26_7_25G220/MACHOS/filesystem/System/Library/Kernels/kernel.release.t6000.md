## kernel.release.t6000

> `System/Library/Kernels/kernel.release.t6000`

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
- `__KLDDATA.__mod_init_func`
- `__KLDDATA.__mod_term_func`
- `__DATA.__data`
- `__HIBDATA.__data`
- `__BOOTDATA.__static_if`
- `__BOOTDATA.__init`
- `__BOOTDATA.__static_ifinit`

```diff

-12377.161.14.0.0
-  __TEXT.__const: 0x36e50
+12377.161.15.700.19
+  __TEXT.__const: 0x36ed0
   __TEXT.__copyio_vectors: 0x150
-  __TEXT.__cstring: 0xa014a
-  __TEXT.__os_log: 0x3e0d7
+  __TEXT.__cstring: 0xa024c
+  __TEXT.__os_log: 0x3e118
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x310
   __DATA_CONST.__sdt_cstring: 0x6e72
   __DATA_CONST.__sdt: 0xe4d8
   __DATA_CONST.__kalloc_type: 0x17240
-  __DATA_CONST.__const: 0x12d398
+  __DATA_CONST.__const: 0x12dad8
   __DATA_CONST.__assert: 0x938
   __DATA_CONST.__kalloc_var: 0x7d00
   __DATA_CONST.__kern_brk_desc: 0x60

   __DATA_CONST.__auth_ptr: 0x10
   __DATA_SPTM.__const: 0x54000
   __TEXT_EXEC.__hib_text: 0x17bc
-  __TEXT_EXEC.__text: 0x977798
+  __TEXT_EXEC.__text: 0x97a128
   __TEXT_EXEC.__commpage_text: 0x334
   __TEXT_BOOT_EXEC.__bootcode: 0x5340
   __KLD.__text: 0xb020

   __DATA.__lock_grp: 0x16808
   __DATA.__percpu: 0x7850
   __DATA.__common: 0x9c650
-  __DATA.__bss: 0x48918
+  __DATA.__bss: 0x48998
   __HIBDATA.__data: 0x41
   __HIBDATA.__bss: 0x670
   __HIBDATA.__common: 0x108
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__static_if: 0x140
   __BOOTDATA.__init: 0x5be08
-  __BOOTDATA.__init_entry_set: 0x13398
+  __BOOTDATA.__init_entry_set: 0x135a8
   __BOOTDATA.__static_ifinit: 0x10
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x4fb78
-  __CTF.__ctf: 0xe46c3
-  Functions: 22451
+  __CTF.__ctf: 0xe4a4a
+  Functions: 22458
   Symbols:   6896
-  CStrings:  25328
+  CStrings:  25343
 
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
