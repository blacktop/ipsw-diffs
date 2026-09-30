## agx_a000

> `Firmware/agx/armfw_g14d.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x4f3a8
+  __TEXT.__text: 0x4f524
   __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1f48
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
-  __DATA.__zerofill: 0x86978
+  __DATA.__zerofill: 0x86998
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 511
   Symbols:   196
-  CStrings:  247
+  CStrings:  248
 
Functions:
~ sub_ffffff80000039d8 : 4988 -> 4984
~ sub_ffffff800000c4c4 -> sub_ffffff800000c4c0 : 4424 -> 4444
~ sub_ffffff800000ee84 -> sub_ffffff800000ee94 : 2516 -> 2544
~ sub_ffffff8000020568 -> sub_ffffff8000020594 : 584 -> 600
~ sub_ffffff8000020f80 -> sub_ffffff8000020fbc : 804 -> 820
~ sub_ffffff8000021448 -> sub_ffffff8000021494 : 1784 -> 1800
~ sub_ffffff8000023f50 -> sub_ffffff8000023fac : 1628 -> 1684
~ sub_ffffff80000245ac -> sub_ffffff8000024640 : 252 -> 280
~ sub_ffffff80000300fc -> sub_ffffff80000301ac : 1108 -> 1132
~ sub_ffffff8000030550 -> sub_ffffff8000030618 : 2464 -> 2456
~ sub_ffffff8000035930 -> sub_ffffff80000359f0 : 1976 -> 2096
~ sub_ffffff8000036fe0 -> sub_ffffff8000037118 : 6384 -> 6388
~ sub_ffffff80000392f0 -> sub_ffffff800003942c : 936 -> 1000
~ sub_ffffff800004f264 -> sub_ffffff800004f3e0 : 332 -> 324
CStrings:
+ "Aug 11 2026 21:40:49"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:20:49"
```
