## agx_c000

> `Firmware/agx/armfw_g15g.im4p/agx_c000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x548ec
+  __TEXT.__text: 0x54a6c
   __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x23f4
-  __TEXT.__cstring: 0x25a4
+  __TEXT.__cstring: 0x25c8
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__init_offsets: 0x0

   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0xe10
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0x9f0
+  __DATA.__const: 0xa00
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x697d8
+  __DATA.__zerofill: 0x697f8
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 502
   Symbols:   197
-  CStrings:  264
+  CStrings:  265
 
Functions:
~ sub_fffffc000000381c : 7660 -> 7664
~ sub_fffffc00000121c4 -> sub_fffffc00000121c8 : 4620 -> 4640
~ sub_fffffc0000014424 -> sub_fffffc000001443c : 2392 -> 2420
~ sub_fffffc0000025ccc -> sub_fffffc0000025d00 : 584 -> 600
~ sub_fffffc0000026658 -> sub_fffffc000002669c : 804 -> 820
~ sub_fffffc0000026b20 -> sub_fffffc0000026b74 : 1784 -> 1800
~ sub_fffffc0000029f68 -> sub_fffffc0000029fcc : 1628 -> 1684
~ sub_fffffc000002a5c4 -> sub_fffffc000002a660 : 252 -> 280
~ sub_fffffc0000036020 -> sub_fffffc00000360d8 : 740 -> 764
~ sub_fffffc0000036304 -> sub_fffffc00000363d4 : 2124 -> 2120
~ sub_fffffc0000036cf4 -> sub_fffffc0000036dc0 : 872 -> 856
~ sub_fffffc000003b350 -> sub_fffffc000003b40c : 1480 -> 1600
~ sub_fffffc000003c7c0 -> sub_fffffc000003c8f4 : 7668 -> 7672
~ sub_fffffc000003ec68 -> sub_fffffc000003eda0 : 1116 -> 1188
CStrings:
+ "Aug 11 2026 21:48:47"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:28:03"
```
