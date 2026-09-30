## agx_a000

> `Firmware/agx/armfw_g16c.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__TEXT.__chain_starts`
- `__DATA._rtk_mtab`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x514f8
+  __TEXT.__text: 0x51bb4
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x12e8
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x6a0
-  __TEXT.__cstring: 0x2f50
+  __TEXT.__cstring: 0x2f74
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA.__gxf_data: 0x80b8
-  __DATA.__data: 0x17198
+  __DATA.__data: 0x179b8
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0xba0
+  __DATA.__const: 0xbb0
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x5eb58
+  __DATA.__zerofill: 0x5eb78
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 499
   Symbols:   169
-  CStrings:  305
+  CStrings:  306
 
Functions:
~ sub_fffffc000000389c : 8228 -> 8240
~ sub_fffffc000000e16c -> sub_fffffc000000e178 : 4920 -> 4940
~ sub_fffffc00000103e4 -> sub_fffffc0000010404 : 2348 -> 2376
~ sub_fffffc00000139c4 -> sub_fffffc0000013a00 : 10636 -> 11140
~ sub_fffffc0000017ba4 -> sub_fffffc0000017dd8 : 10152 -> 10156
~ sub_fffffc000001a524 -> sub_fffffc000001a75c : 5176 -> 5248
~ sub_fffffc000001d240 -> sub_fffffc000001d4c0 : 2100 -> 2148
~ sub_fffffc000002153c -> sub_fffffc00000217ec : 584 -> 600
~ sub_fffffc0000021d80 -> sub_fffffc0000022040 : 804 -> 820
~ sub_fffffc0000022248 -> sub_fffffc0000022518 : 1784 -> 1800
~ sub_fffffc000002681c -> sub_fffffc0000026afc : 1584 -> 1640
~ sub_fffffc0000026e4c -> sub_fffffc0000027164 : 252 -> 280
~ sub_fffffc0000028de8 -> sub_fffffc000002911c : 360 -> 352
~ sub_fffffc0000029550 -> sub_fffffc000002987c : 1772 -> 1788
~ sub_fffffc000002a388 -> sub_fffffc000002a6c4 : 756 -> 768
~ sub_fffffc000002aa10 -> sub_fffffc000002ad58 : 848 -> 832
~ sub_fffffc000002b450 -> sub_fffffc000002b788 : 2332 -> 2340
~ sub_fffffc0000031944 -> sub_fffffc0000031c84 : 1636 -> 1660
~ sub_fffffc0000031fa8 -> sub_fffffc0000032300 : 2288 -> 2300
~ sub_fffffc0000039980 -> sub_fffffc0000039ce4 : 6928 -> 7664
~ sub_fffffc000003b490 -> sub_fffffc000003bad4 : 1944 -> 2064
~ sub_fffffc00000513b8 -> sub_fffffc0000051a74 : 328 -> 320
CStrings:
+ "Aug 11 2026 21:41:38"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:21:35"
```
