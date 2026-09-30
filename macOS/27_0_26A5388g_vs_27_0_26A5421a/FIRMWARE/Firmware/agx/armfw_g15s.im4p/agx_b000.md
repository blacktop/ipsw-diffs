## agx_b000

> `Firmware/agx/armfw_g15s.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x50220
+  __TEXT.__text: 0x503a8
   __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1120
-  __TEXT.__cstring: 0x2780
+  __TEXT.__cstring: 0x27a4
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__init_offsets: 0x0

   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0xe70
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0xa28
+  __DATA.__const: 0xa38
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0xcae18
+  __DATA.__zerofill: 0xcae38
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 502
   Symbols:   178
-  CStrings:  276
+  CStrings:  277
 
Functions:
~ sub_fffffc0000003570 : 8708 -> 8712
~ sub_fffffc0000010670 -> sub_fffffc0000010674 : 4604 -> 4624
~ sub_fffffc0000012924 -> sub_fffffc000001293c : 2512 -> 2540
~ sub_fffffc00000248a0 -> sub_fffffc00000248d4 : 584 -> 600
~ sub_fffffc0000025170 -> sub_fffffc00000251b4 : 804 -> 820
~ sub_fffffc0000025638 -> sub_fffffc000002568c : 1784 -> 1800
~ sub_fffffc0000029404 -> sub_fffffc0000029468 : 1628 -> 1684
~ sub_fffffc0000029a60 -> sub_fffffc0000029afc : 252 -> 280
~ sub_fffffc00000315cc -> sub_fffffc0000031684 : 740 -> 764
~ sub_fffffc00000318b0 -> sub_fffffc0000031980 : 2180 -> 2176
~ sub_fffffc0000036ec8 -> sub_fffffc0000036f94 : 1784 -> 1904
~ sub_fffffc0000038328 -> sub_fffffc000003846c : 6868 -> 6872
~ sub_fffffc000003a540 -> sub_fffffc000003a688 : 948 -> 1012
~ sub_fffffc00000500dc -> sub_fffffc0000050264 : 324 -> 332
CStrings:
+ "Aug 11 2026 21:46:59"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:26:15"
```
