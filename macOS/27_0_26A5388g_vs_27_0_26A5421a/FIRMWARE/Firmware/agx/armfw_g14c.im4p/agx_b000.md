## agx_b000

> `Firmware/agx/armfw_g14c.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x4e7d8
+  __TEXT.__text: 0x4e954
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
-  __DATA.__zerofill: 0x86738
+  __DATA.__zerofill: 0x86758
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 509
   Symbols:   196
-  CStrings:  247
+  CStrings:  248
 
Functions:
~ sub_ffffff80000038d8 : 4988 -> 4984
~ sub_ffffff800000bfd8 -> sub_ffffff800000bfd4 : 4424 -> 4444
~ sub_ffffff800000e94c -> sub_ffffff800000e95c : 2516 -> 2544
~ sub_ffffff800001feac -> sub_ffffff800001fed8 : 584 -> 600
~ sub_ffffff80000208c4 -> sub_ffffff8000020900 : 804 -> 820
~ sub_ffffff8000020d8c -> sub_ffffff8000020dd8 : 1784 -> 1800
~ sub_ffffff8000023894 -> sub_ffffff80000238f0 : 1628 -> 1684
~ sub_ffffff8000023ef0 -> sub_ffffff8000023f84 : 252 -> 280
~ sub_ffffff800002f9f8 -> sub_ffffff800002faa8 : 996 -> 1020
~ sub_ffffff800002fddc -> sub_ffffff800002fea4 : 2252 -> 2244
~ sub_ffffff8000034e1c -> sub_ffffff8000034edc : 1976 -> 2096
~ sub_ffffff80000364cc -> sub_ffffff8000036604 : 6384 -> 6388
~ sub_ffffff80000387dc -> sub_ffffff8000038918 : 936 -> 1000
~ sub_ffffff800004e694 -> sub_ffffff800004e810 : 332 -> 324
CStrings:
+ "Aug 11 2026 21:45:09"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:24:50"
```
