## agx_a000

> `Firmware/agx/armfw_g17g.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__TEXT.__chain_starts`
- `__DATA._rtk_mtab`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3d224
+  __TEXT.__text: 0x3d854
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1070
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
-  __TEXT.__cstring: 0x234c
+  __TEXT.__cstring: 0x2370
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
   Functions: 417
   Symbols:   169
-  CStrings:  235
+  CStrings:  236
 
Functions:
~ sub_fffffc000000c30c : 11404 -> 12060
~ sub_fffffc000001035c -> sub_fffffc00000105ec : 10000 -> 10020
~ sub_fffffc0000012c44 -> sub_fffffc0000012ee8 : 4804 -> 4884
~ sub_fffffc0000015814 -> sub_fffffc0000015b08 : 2060 -> 2108
~ sub_fffffc000001d244 -> sub_fffffc000001d568 : 360 -> 352
~ sub_fffffc000001d9a0 -> sub_fffffc000001dcbc : 1688 -> 1704
~ sub_fffffc000001e788 -> sub_fffffc000001eab4 : 756 -> 768
~ sub_fffffc000001edf4 -> sub_fffffc000001f12c : 848 -> 832
~ sub_fffffc000001f844 -> sub_fffffc000001fb6c : 2372 -> 2376
~ sub_fffffc00000241d4 -> sub_fffffc0000024500 : 384 -> 368
~ sub_fffffc0000024b00 -> sub_fffffc0000024e1c : 1368 -> 1380
~ sub_fffffc0000025bdc -> sub_fffffc0000025f04 : 768 -> 772
~ sub_fffffc0000027ecc -> sub_fffffc00000281f8 : 8148 -> 8792
~ sub_fffffc0000029ea0 -> sub_fffffc000002a450 : 2088 -> 2216
CStrings:
+ "Aug 11 2026 21:42:55"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:22:44"
```
