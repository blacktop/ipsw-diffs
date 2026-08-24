## agx_a000

> `Firmware/agx/armfw_g16s.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__TEXT.__chain_starts`
- `__DATA._rtk_mtab`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x511fc
+  __TEXT.__text: 0x518b8
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
-  __DATA.__zerofill: 0x5ea58
+  __DATA.__zerofill: 0x5ea78
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 499
   Symbols:   169
-  CStrings:  305
+  CStrings:  306
 
Functions:
~ sub_fffffc000000389c : 8184 -> 8196
~ sub_fffffc000000df3c -> sub_fffffc000000df48 : 4920 -> 4940
~ sub_fffffc00000101b4 -> sub_fffffc00000101d4 : 2348 -> 2376
~ sub_fffffc0000013794 -> sub_fffffc00000137d0 : 10636 -> 11140
~ sub_fffffc0000017974 -> sub_fffffc0000017ba8 : 10152 -> 10156
~ sub_fffffc000001a2f4 -> sub_fffffc000001a52c : 5176 -> 5248
~ sub_fffffc000001d010 -> sub_fffffc000001d290 : 2100 -> 2148
~ sub_fffffc000002130c -> sub_fffffc00000215bc : 584 -> 600
~ sub_fffffc0000021b54 -> sub_fffffc0000021e14 : 804 -> 820
~ sub_fffffc000002201c -> sub_fffffc00000222ec : 1784 -> 1800
~ sub_fffffc00000265f0 -> sub_fffffc00000268d0 : 1584 -> 1640
~ sub_fffffc0000026c20 -> sub_fffffc0000026f38 : 252 -> 280
~ sub_fffffc0000028bbc -> sub_fffffc0000028ef0 : 360 -> 352
~ sub_fffffc0000029324 -> sub_fffffc0000029650 : 1772 -> 1788
~ sub_fffffc000002a15c -> sub_fffffc000002a498 : 756 -> 768
~ sub_fffffc000002a7e4 -> sub_fffffc000002ab2c : 848 -> 832
~ sub_fffffc000002b224 -> sub_fffffc000002b55c : 2332 -> 2340
~ sub_fffffc0000031718 -> sub_fffffc0000031a58 : 1636 -> 1660
~ sub_fffffc0000031d7c -> sub_fffffc00000320d4 : 2192 -> 2204
~ sub_fffffc0000039684 -> sub_fffffc00000399e8 : 6928 -> 7664
~ sub_fffffc000003b194 -> sub_fffffc000003b7d8 : 1944 -> 2064
CStrings:
+ "Aug 11 2026 21:41:38"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:21:34"
```
