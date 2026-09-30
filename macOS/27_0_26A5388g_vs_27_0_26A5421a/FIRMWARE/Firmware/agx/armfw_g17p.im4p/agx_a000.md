## agx_a000

> `Firmware/agx/armfw_g17p.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__TEXT.__chain_starts`
- `__DATA._rtk_mtab`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3bad4
+  __TEXT.__text: 0x3c044
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1cf8
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x6a0
-  __TEXT.__cstring: 0x22df
+  __TEXT.__cstring: 0x2303
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA.__gxf_data: 0x80b8
-  __DATA.__data: 0x17478
+  __DATA.__data: 0x17c98
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0x820
+  __DATA.__const: 0x830
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x5b198
+  __DATA.__zerofill: 0x5b1d8
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 434
   Symbols:   187
-  CStrings:  234
+  CStrings:  235
 
Functions:
~ sub_fffffc0000003ab4 : 7884 -> 7880
~ sub_fffffc000000b2c4 -> sub_fffffc000000b2c0 : 10592 -> 10924
~ sub_fffffc000000f298 -> sub_fffffc000000f3e0 : 10304 -> 10324
~ sub_fffffc0000011cb0 -> sub_fffffc0000011e0c : 4880 -> 4952
~ sub_fffffc00000148a4 -> sub_fffffc0000014a48 : 2044 -> 2092
~ sub_fffffc000001c118 -> sub_fffffc000001c2ec : 360 -> 352
~ sub_fffffc000001c880 -> sub_fffffc000001ca4c : 1676 -> 1692
~ sub_fffffc000001d658 -> sub_fffffc000001d834 : 756 -> 768
~ sub_fffffc000001dce0 -> sub_fffffc000001dec8 : 848 -> 832
~ sub_fffffc000001e720 -> sub_fffffc000001e8f8 : 2332 -> 2340
~ sub_fffffc00000207b0 -> sub_fffffc0000020990 : 2108 -> 2120
~ sub_fffffc0000023350 -> sub_fffffc000002353c : 384 -> 368
~ sub_fffffc0000023be8 -> sub_fffffc0000023dc4 : 1368 -> 1380
~ sub_fffffc0000024cc4 -> sub_fffffc0000024eac : 768 -> 772
~ sub_fffffc0000026eb4 -> sub_fffffc00000270a0 : 6324 -> 7096
~ sub_fffffc0000028768 -> sub_fffffc0000028c58 : 2084 -> 2212
CStrings:
+ "Aug 11 2026 21:41:11"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:21:10"
```
