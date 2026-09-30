## agx_b000

> `Firmware/agx/armfw_g13x.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x4484c
+  __TEXT.__text: 0x44978
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
~ sub_ffffff80000038ac : 4852 -> 4856
~ sub_ffffff800000ae60 -> sub_ffffff800000ae64 : 3724 -> 3752
~ sub_ffffff800000c584 -> sub_ffffff800000c5a4 : 1968 -> 1996
~ sub_ffffff800001ce00 -> sub_ffffff800001ce3c : 584 -> 600
~ sub_ffffff800001d6cc -> sub_ffffff800001d718 : 804 -> 820
~ sub_ffffff800001db94 -> sub_ffffff800001dbf0 : 1784 -> 1800
~ sub_ffffff8000026870 -> sub_ffffff80000268dc : 2364 -> 2360
~ sub_ffffff800002b2d0 -> sub_ffffff800002b338 : 1664 -> 1784
~ sub_ffffff800002cd4c -> sub_ffffff800002ce2c : 11096 -> 11100
~ sub_ffffff8000030070 -> sub_ffffff8000030154 : 1088 -> 1160
CStrings:
+ "Aug 11 2026 21:43:14"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:22:59"
```
