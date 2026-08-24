## agx_a000

> `Firmware/agx/armfw_g14c.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x4ec68
+  __TEXT.__text: 0x4ede4
   __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1f08
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
-  __DATA.__zerofill: 0x86778
+  __DATA.__zerofill: 0x86798
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 510
   Symbols:   196
-  CStrings:  247
+  CStrings:  248
 
Functions:
~ sub_ffffff80000038d8 : 4988 -> 4984
~ sub_ffffff800000bfb8 -> sub_ffffff800000bfb4 : 4424 -> 4444
~ sub_ffffff800000e92c -> sub_ffffff800000e93c : 2516 -> 2544
~ sub_ffffff800002004c -> sub_ffffff8000020078 : 584 -> 600
~ sub_ffffff8000020a64 -> sub_ffffff8000020aa0 : 804 -> 820
~ sub_ffffff8000020f2c -> sub_ffffff8000020f78 : 1784 -> 1800
~ sub_ffffff8000023a34 -> sub_ffffff8000023a90 : 1628 -> 1684
~ sub_ffffff8000024090 -> sub_ffffff8000024124 : 252 -> 280
~ sub_ffffff800002fb98 -> sub_ffffff800002fc48 : 996 -> 1020
~ sub_ffffff800002ff7c -> sub_ffffff8000030044 : 2252 -> 2244
~ sub_ffffff8000035224 -> sub_ffffff80000352e4 : 1976 -> 2096
~ sub_ffffff80000368d4 -> sub_ffffff8000036a0c : 6384 -> 6388
~ sub_ffffff8000038be4 -> sub_ffffff8000038d20 : 936 -> 1000
~ sub_ffffff800004eb24 -> sub_ffffff800004eca0 : 332 -> 324
CStrings:
+ "Aug 11 2026 21:40:46"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:20:48"
```
