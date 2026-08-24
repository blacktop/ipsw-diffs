## agx_a000

> `Firmware/agx/armfw_g15s.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x5064c
+  __TEXT.__text: 0x507d4
   __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1120
-  __TEXT.__cstring: 0x279d
+  __TEXT.__cstring: 0x27c1
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
-  __DATA.__zerofill: 0xcae98
+  __DATA.__zerofill: 0xcaeb8
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 503
   Symbols:   178
-  CStrings:  276
+  CStrings:  277
 
Functions:
~ sub_fffffc0000003570 : 8740 -> 8744
~ sub_fffffc000001064c -> sub_fffffc0000010650 : 4604 -> 4624
~ sub_fffffc0000012900 -> sub_fffffc0000012918 : 2512 -> 2540
~ sub_fffffc0000024858 -> sub_fffffc000002488c : 584 -> 600
~ sub_fffffc0000025128 -> sub_fffffc000002516c : 804 -> 820
~ sub_fffffc00000255f0 -> sub_fffffc0000025644 : 1784 -> 1800
~ sub_fffffc000002949c -> sub_fffffc0000029500 : 1628 -> 1684
~ sub_fffffc0000029af8 -> sub_fffffc0000029b94 : 252 -> 280
~ sub_fffffc0000031664 -> sub_fffffc000003171c : 740 -> 764
~ sub_fffffc0000031948 -> sub_fffffc0000031a18 : 2180 -> 2176
~ sub_fffffc0000037308 -> sub_fffffc00000373d4 : 1784 -> 1904
~ sub_fffffc0000038768 -> sub_fffffc00000388ac : 6880 -> 6884
~ sub_fffffc000003a98c -> sub_fffffc000003aad4 : 948 -> 1012
~ sub_fffffc0000050508 -> sub_fffffc0000050690 : 332 -> 324
CStrings:
+ "Aug 11 2026 21:41:36"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:21:32"
```
