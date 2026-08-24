## agx_b000

> `Firmware/agx/armfw_g14d.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x4ef10
+  __TEXT.__text: 0x4f08c
   __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1f28
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
-  __DATA.__zerofill: 0x86938
+  __DATA.__zerofill: 0x86958
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 510
   Symbols:   196
-  CStrings:  247
+  CStrings:  248
 
Functions:
~ sub_ffffff80000039d8 : 4988 -> 4984
~ sub_ffffff800000c4dc -> sub_ffffff800000c4d8 : 4424 -> 4444
~ sub_ffffff800000ee9c -> sub_ffffff800000eeac : 2516 -> 2544
~ sub_ffffff80000203c0 -> sub_ffffff80000203ec : 584 -> 600
~ sub_ffffff8000020dd8 -> sub_ffffff8000020e14 : 804 -> 820
~ sub_ffffff80000212a0 -> sub_ffffff80000212ec : 1784 -> 1800
~ sub_ffffff8000023da8 -> sub_ffffff8000023e04 : 1628 -> 1684
~ sub_ffffff8000024404 -> sub_ffffff8000024498 : 252 -> 280
~ sub_ffffff800002ff54 -> sub_ffffff8000030004 : 1108 -> 1132
~ sub_ffffff80000303a8 -> sub_ffffff8000030470 : 2464 -> 2456
~ sub_ffffff8000035520 -> sub_ffffff80000355e0 : 1976 -> 2096
~ sub_ffffff8000036bd0 -> sub_ffffff8000036d08 : 6384 -> 6388
~ sub_ffffff8000038ee0 -> sub_ffffff800003901c : 936 -> 1000
~ sub_ffffff800004edcc -> sub_ffffff800004ef48 : 324 -> 332
CStrings:
+ "Aug 11 2026 21:45:36"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:24:35"
```
