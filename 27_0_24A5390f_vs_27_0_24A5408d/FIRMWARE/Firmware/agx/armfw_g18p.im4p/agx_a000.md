## agx_a000

> `Firmware/agx/armfw_g18p.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__TEXT.__chain_starts`
- `__DATA._rtk_mtab`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3ca9c
+  __TEXT.__text: 0x3cfb4
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1068
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
-  __TEXT.__cstring: 0x2322
+  __TEXT.__cstring: 0x2346
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA.__gxf_data: 0x80b8
-  __DATA.__data: 0x17508
+  __DATA.__data: 0x17d28
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0x798
+  __DATA.__const: 0x7a8
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x5a758
+  __DATA.__zerofill: 0x5a778
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 417
   Symbols:   168
-  CStrings:  234
+  CStrings:  235
 
Functions:
~ sub_fffffc000000c27c : 10776 -> 11152
~ sub_fffffc0000010058 -> sub_fffffc00000101d0 : 10000 -> 10020
~ sub_fffffc0000012940 -> sub_fffffc0000012acc : 4764 -> 4844
~ sub_fffffc00000154e8 -> sub_fffffc00000156c4 : 2060 -> 2108
~ sub_fffffc000001cb1c -> sub_fffffc000001cd28 : 360 -> 352
~ sub_fffffc000001d278 -> sub_fffffc000001d47c : 1688 -> 1704
~ sub_fffffc000001e060 -> sub_fffffc000001e274 : 756 -> 768
~ sub_fffffc000001e6cc -> sub_fffffc000001e8ec : 848 -> 832
~ sub_fffffc000001f11c -> sub_fffffc000001f32c : 2372 -> 2376
~ sub_fffffc0000023aac -> sub_fffffc0000023cc0 : 384 -> 368
~ sub_fffffc00000243d8 -> sub_fffffc00000245dc : 1368 -> 1380
~ sub_fffffc00000254b4 -> sub_fffffc00000256c4 : 768 -> 772
~ sub_fffffc00000277a4 -> sub_fffffc00000279b8 : 8148 -> 8792
~ sub_fffffc0000029778 -> sub_fffffc0000029c10 : 2088 -> 2216
~ sub_fffffc000003c958 -> sub_fffffc000003ce70 : 332 -> 324
CStrings:
+ "Aug  5 2026 21:49:15"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:09:00"
```
