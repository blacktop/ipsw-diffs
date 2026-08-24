## agx_b000

> `Firmware/agx/armfw_g14s.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x4e420
+  __TEXT.__text: 0x4e5a0
   __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1ef0
-  __TEXT.__cstring: 0x2347
+  __TEXT.__cstring: 0x236b
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__init_offsets: 0x0

   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0xe80
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0xab0
+  __DATA.__const: 0xac0
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x40

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x86638
+  __DATA.__zerofill: 0x86658
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 509
   Symbols:   196
-  CStrings:  247
+  CStrings:  248
 
Functions:
~ sub_ffffff800000bd8c : 4424 -> 4444
~ sub_ffffff800000e700 -> sub_ffffff800000e714 : 2516 -> 2544
~ sub_ffffff800001fc60 -> sub_ffffff800001fc90 : 584 -> 600
~ sub_ffffff8000020678 -> sub_ffffff80000206b8 : 804 -> 820
~ sub_ffffff8000020b40 -> sub_ffffff8000020b90 : 1784 -> 1800
~ sub_ffffff8000023648 -> sub_ffffff80000236a8 : 1628 -> 1684
~ sub_ffffff8000023ca4 -> sub_ffffff8000023d3c : 252 -> 280
~ sub_ffffff800002f6d4 -> sub_ffffff800002f788 : 980 -> 1004
~ sub_ffffff800002faa8 -> sub_ffffff800002fb74 : 2144 -> 2136
~ sub_ffffff8000034a60 -> sub_ffffff8000034b24 : 1976 -> 2096
~ sub_ffffff8000036110 -> sub_ffffff800003624c : 6384 -> 6388
~ sub_ffffff8000038420 -> sub_ffffff8000038560 : 936 -> 1000
CStrings:
+ "Aug 11 2026 21:45:25"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:24:35"
```
