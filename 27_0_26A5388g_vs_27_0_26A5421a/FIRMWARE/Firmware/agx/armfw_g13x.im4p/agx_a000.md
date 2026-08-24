## agx_a000

> `Firmware/agx/armfw_g13x.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x448f0
+  __TEXT.__text: 0x44a1c
   __TEXT.__gxf_code: 0x1150
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1f70
-  __TEXT.__cstring: 0x1f33
+  __TEXT.__cstring: 0x1f57
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x1e8
   __TEXT.__init_offsets: 0x0

   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0xd98
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0x988
+  __DATA.__const: 0x998
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x40

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x535b8
+  __DATA.__zerofill: 0x535d8
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 478
   Symbols:   195
-  CStrings:  229
+  CStrings:  230
 
Functions:
~ sub_ffffff800000386c : 4852 -> 4856
~ sub_ffffff800000adf0 -> sub_ffffff800000adf4 : 3724 -> 3752
~ sub_ffffff800000c514 -> sub_ffffff800000c534 : 1968 -> 1996
~ sub_ffffff800001cea4 -> sub_ffffff800001cee0 : 584 -> 600
~ sub_ffffff800001d770 -> sub_ffffff800001d7bc : 804 -> 820
~ sub_ffffff800001dc38 -> sub_ffffff800001dc94 : 1784 -> 1800
~ sub_ffffff8000026914 -> sub_ffffff8000026980 : 2364 -> 2360
~ sub_ffffff800002b374 -> sub_ffffff800002b3dc : 1664 -> 1784
~ sub_ffffff800002cdf0 -> sub_ffffff800002ced0 : 11096 -> 11100
~ sub_ffffff8000030114 -> sub_ffffff80000301f8 : 1088 -> 1160
~ sub_ffffff80000447ac -> sub_ffffff80000448d8 : 324 -> 332
CStrings:
+ "Aug 11 2026 21:39:39"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:19:51"
```
