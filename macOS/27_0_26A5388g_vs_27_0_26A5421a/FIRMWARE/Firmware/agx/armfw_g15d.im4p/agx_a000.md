## agx_a000

> `Firmware/agx/armfw_g15d.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x53c74
+  __TEXT.__text: 0x53df8
   __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x12a8
-  __TEXT.__cstring: 0x2bab
+  __TEXT.__cstring: 0x2bcf
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__init_offsets: 0x0

   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0xf10
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0xae8
+  __DATA.__const: 0xaf8
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0xcb8f8
+  __DATA.__zerofill: 0xcb918
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 522
   Symbols:   179
-  CStrings:  292
+  CStrings:  293
 
Functions:
~ sub_fffffc00000036bc : 8832 -> 8836
~ sub_fffffc000001164c -> sub_fffffc0000011650 : 4740 -> 4760
~ sub_fffffc0000013b3c -> sub_fffffc0000013b54 : 2512 -> 2540
~ sub_fffffc0000025c3c -> sub_fffffc0000025c70 : 584 -> 600
~ sub_fffffc0000026514 -> sub_fffffc0000026558 : 804 -> 820
~ sub_fffffc00000269dc -> sub_fffffc0000026a30 : 1784 -> 1800
~ sub_fffffc000002a7b4 -> sub_fffffc000002a818 : 1628 -> 1684
~ sub_fffffc000002ae10 -> sub_fffffc000002aeac : 252 -> 280
~ sub_fffffc0000033004 -> sub_fffffc00000330bc : 1640 -> 1664
~ sub_fffffc000003366c -> sub_fffffc000003373c : 2520 -> 2512
~ sub_fffffc00000396c4 -> sub_fffffc000003978c : 1784 -> 1904
~ sub_fffffc000003ab24 -> sub_fffffc000003ac64 : 6868 -> 6872
~ sub_fffffc000003cd3c -> sub_fffffc000003ce80 : 952 -> 1016
~ sub_fffffc0000053b34 -> sub_fffffc0000053cb8 : 320 -> 328
CStrings:
+ "Aug 11 2026 21:41:40"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:21:35"
```
