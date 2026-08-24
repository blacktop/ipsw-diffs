## agx_c000

> `Firmware/agx/armfw_g17g.im4p/agx_c000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__TEXT.__chain_starts`
- `__DATA._rtk_mtab`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3ce50
+  __TEXT.__text: 0x3d4c4
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1070
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
-  __TEXT.__cstring: 0x2402
+  __TEXT.__cstring: 0x2426
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA.__gxf_data: 0x80b8
-  __DATA.__data: 0x17520
+  __DATA.__data: 0x17d40
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0x7b8
+  __DATA.__const: 0x7c8
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x5a758
+  __DATA.__zerofill: 0x5a778
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 416
   Symbols:   169
-  CStrings:  237
+  CStrings:  238
 
Functions:
~ sub_fffffc000000bec8 : 11404 -> 12060
~ sub_fffffc000000ff18 -> sub_fffffc00000101a8 : 10000 -> 10020
~ sub_fffffc0000012800 -> sub_fffffc0000012aa4 : 4804 -> 4884
~ sub_fffffc00000153d0 -> sub_fffffc00000156c4 : 2060 -> 2108
~ sub_fffffc000001ce00 -> sub_fffffc000001d124 : 360 -> 352
~ sub_fffffc000001d55c -> sub_fffffc000001d878 : 1688 -> 1704
~ sub_fffffc000001e344 -> sub_fffffc000001e670 : 756 -> 768
~ sub_fffffc000001e9b0 -> sub_fffffc000001ece8 : 848 -> 832
~ sub_fffffc000001f400 -> sub_fffffc000001f728 : 2372 -> 2376
~ sub_fffffc0000023d90 -> sub_fffffc00000240bc : 384 -> 368
~ sub_fffffc00000246bc -> sub_fffffc00000249d8 : 1368 -> 1380
~ sub_fffffc0000025798 -> sub_fffffc0000025ac0 : 768 -> 772
~ sub_fffffc0000027e08 -> sub_fffffc0000028134 : 7364 -> 8076
~ sub_fffffc0000029acc -> sub_fffffc000002a0c0 : 2088 -> 2216
CStrings:
+ "Aug 11 2026 21:53:01"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:31:44"
```
