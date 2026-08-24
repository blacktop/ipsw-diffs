## agx_a000

> `Firmware/agx/armfw_g13g.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`

```diff

-  __TEXT.__text: 0x40e6c
+  __TEXT.__text: 0x40fac
   __TEXT.__gxf_code: 0x1150
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1d3c
-  __TEXT.__cstring: 0x1c55
+  __TEXT.__cstring: 0x1c79
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x1e8
   __TEXT.__init_offsets: 0x0

   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0xc60
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0x918
+  __DATA.__const: 0x928
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x40

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x52dd8
+  __DATA.__zerofill: 0x52df8
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 426
   Symbols:   194
-  CStrings:  206
+  CStrings:  207
 
Functions:
~ sub_ffffff800000381c : 4684 -> 4688
~ sub_ffffff800001c878 -> sub_ffffff800001c87c : 584 -> 600
~ sub_ffffff800001d244 -> sub_ffffff800001d258 : 804 -> 820
~ sub_ffffff800001d70c -> sub_ffffff800001d730 : 1784 -> 1800
~ sub_ffffff800001f8d0 -> sub_ffffff800001f904 : 1624 -> 1680
~ sub_ffffff800001ff28 -> sub_ffffff800001ff94 : 252 -> 280
~ sub_ffffff800002526c -> sub_ffffff80000252f4 : 2016 -> 2004
~ sub_ffffff80000291ec -> sub_ffffff8000029268 : 1716 -> 1836
~ sub_ffffff800002ac9c -> sub_ffffff800002ad90 : 10860 -> 10864
~ sub_ffffff800002ded0 -> sub_ffffff800002dfc8 : 1088 -> 1160
CStrings:
+ "Aug 11 2026 21:39:34"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:19:47"
```
