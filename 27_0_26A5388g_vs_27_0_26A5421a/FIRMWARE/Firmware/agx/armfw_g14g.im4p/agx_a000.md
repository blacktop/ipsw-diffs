## agx_a000

> `Firmware/agx/armfw_g14g.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x52350
+  __TEXT.__text: 0x524f0
   __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1f14
-  __TEXT.__cstring: 0x20ad
+  __TEXT.__cstring: 0x20d1
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__init_offsets: 0x0

   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0xe20
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0x968
+  __DATA.__const: 0x978
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x40

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x53238
+  __DATA.__zerofill: 0x53278
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 476
   Symbols:   196
-  CStrings:  236
+  CStrings:  237
 
Functions:
~ sub_ffffff8000003880 : 5284 -> 5288
~ sub_ffffff800000d3c8 -> sub_ffffff800000d3cc : 3792 -> 3828
~ sub_ffffff800000ed84 -> sub_ffffff800000edac : 1968 -> 1996
~ sub_ffffff800002067c -> sub_ffffff80000206c0 : 584 -> 600
~ sub_ffffff80000210dc -> sub_ffffff8000021130 : 804 -> 820
~ sub_ffffff80000215a4 -> sub_ffffff8000021608 : 1784 -> 1800
~ sub_ffffff8000023920 -> sub_ffffff8000023994 : 1628 -> 1684
~ sub_ffffff8000023f7c -> sub_ffffff8000024028 : 252 -> 280
~ sub_ffffff800002a5f8 -> sub_ffffff800002a6c0 : 740 -> 764
~ sub_ffffff800002a8dc -> sub_ffffff800002a9bc : 2020 -> 2016
~ sub_ffffff8000037fa0 -> sub_ffffff800003807c : 1716 -> 1836
~ sub_ffffff8000039a50 -> sub_ffffff8000039ba4 : 11140 -> 11144
~ sub_ffffff800003cda0 -> sub_ffffff800003cef8 : 1088 -> 1160
CStrings:
+ "Aug 11 2026 21:40:09"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:20:18"
```
