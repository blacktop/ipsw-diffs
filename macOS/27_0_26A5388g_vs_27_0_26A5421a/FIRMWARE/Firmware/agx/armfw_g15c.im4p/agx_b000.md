## agx_b000

> `Firmware/agx/armfw_g15c.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x52c3c
+  __TEXT.__text: 0x52dc0
   __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x11b8
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
-  __DATA.__zerofill: 0xcb778
+  __DATA.__zerofill: 0xcb798
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 519
   Symbols:   179
-  CStrings:  292
+  CStrings:  293
 
Functions:
~ sub_fffffc00000035bc : 8876 -> 8880
~ sub_fffffc0000010ba4 -> sub_fffffc0000010ba8 : 4768 -> 4788
~ sub_fffffc0000013058 -> sub_fffffc0000013070 : 2512 -> 2540
~ sub_fffffc00000251d0 -> sub_fffffc0000025204 : 584 -> 600
~ sub_fffffc0000025aa8 -> sub_fffffc0000025aec : 804 -> 820
~ sub_fffffc0000025f70 -> sub_fffffc0000025fc4 : 1784 -> 1800
~ sub_fffffc0000029d48 -> sub_fffffc0000029dac : 1628 -> 1684
~ sub_fffffc000002a3a4 -> sub_fffffc000002a440 : 252 -> 280
~ sub_fffffc0000032348 -> sub_fffffc0000032400 : 1640 -> 1664
~ sub_fffffc00000329b0 -> sub_fffffc0000032a80 : 2320 -> 2312
~ sub_fffffc0000038788 -> sub_fffffc0000038850 : 1784 -> 1904
~ sub_fffffc0000039be8 -> sub_fffffc0000039d28 : 6868 -> 6872
~ sub_fffffc000003be00 -> sub_fffffc000003bf44 : 952 -> 1016
~ sub_fffffc0000052afc -> sub_fffffc0000052c80 : 328 -> 320
CStrings:
+ "Aug 11 2026 21:47:03"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:26:26"
```
