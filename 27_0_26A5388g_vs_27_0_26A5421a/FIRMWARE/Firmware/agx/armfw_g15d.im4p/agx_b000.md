## agx_b000

> `Firmware/agx/armfw_g15d.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x53d90
+  __TEXT.__text: 0x53f14
   __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x12a8
-  __TEXT.__cstring: 0x2b8e
+  __TEXT.__cstring: 0x2bb2
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
-  __DATA.__zerofill: 0xcb9f8
+  __DATA.__zerofill: 0xcba18
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 522
   Symbols:   179
-  CStrings:  292
+  CStrings:  293
 
Functions:
~ sub_fffffc00000036bc : 8832 -> 8836
~ sub_fffffc00000116e0 -> sub_fffffc00000116e4 : 4740 -> 4760
~ sub_fffffc0000013bd0 -> sub_fffffc0000013be8 : 2512 -> 2540
~ sub_fffffc0000025cc8 -> sub_fffffc0000025cfc : 584 -> 600
~ sub_fffffc00000265a0 -> sub_fffffc00000265e4 : 804 -> 820
~ sub_fffffc0000026a68 -> sub_fffffc0000026abc : 1784 -> 1800
~ sub_fffffc000002a840 -> sub_fffffc000002a8a4 : 1628 -> 1684
~ sub_fffffc000002ae9c -> sub_fffffc000002af38 : 252 -> 280
~ sub_fffffc0000033120 -> sub_fffffc00000331d8 : 1640 -> 1664
~ sub_fffffc0000033788 -> sub_fffffc0000033858 : 2520 -> 2512
~ sub_fffffc00000397e0 -> sub_fffffc00000398a8 : 1784 -> 1904
~ sub_fffffc000003ac40 -> sub_fffffc000003ad80 : 6868 -> 6872
~ sub_fffffc000003ce58 -> sub_fffffc000003cf9c : 952 -> 1016
CStrings:
+ "Aug 11 2026 21:47:14"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:26:31"
```
