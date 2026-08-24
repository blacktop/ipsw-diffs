## agx_b000

> `Firmware/agx/armfw_g15g.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x54c94
+  __TEXT.__text: 0x54e14
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
-  __DATA.__zerofill: 0x69958
+  __DATA.__zerofill: 0x69998
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 503
   Symbols:   197
-  CStrings:  264
+  CStrings:  265
 
Functions:
~ sub_fffffc000000381c : 7668 -> 7672
~ sub_fffffc00000121cc -> sub_fffffc00000121d0 : 4620 -> 4640
~ sub_fffffc000001442c -> sub_fffffc0000014444 : 2392 -> 2420
~ sub_fffffc0000025ca8 -> sub_fffffc0000025cdc : 584 -> 600
~ sub_fffffc0000026634 -> sub_fffffc0000026678 : 804 -> 820
~ sub_fffffc0000026afc -> sub_fffffc0000026b50 : 1784 -> 1800
~ sub_fffffc000002a01c -> sub_fffffc000002a080 : 1628 -> 1684
~ sub_fffffc000002a678 -> sub_fffffc000002a714 : 252 -> 280
~ sub_fffffc00000360b0 -> sub_fffffc0000036168 : 740 -> 764
~ sub_fffffc0000036394 -> sub_fffffc0000036464 : 2124 -> 2120
~ sub_fffffc0000036d84 -> sub_fffffc0000036e50 : 872 -> 856
~ sub_fffffc000003b6fc -> sub_fffffc000003b7b8 : 1480 -> 1600
~ sub_fffffc000003cb6c -> sub_fffffc000003cca0 : 7680 -> 7684
~ sub_fffffc000003f020 -> sub_fffffc000003f158 : 1116 -> 1188
CStrings:
+ "Aug 11 2026 21:45:20"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:25:17"
```
