## agx_b000

> `Firmware/agx/armfw_g16s.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__TEXT.__chain_starts`
- `__DATA._rtk_mtab`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x5109c
+  __TEXT.__text: 0x51758
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x12e8
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x6a0
-  __TEXT.__cstring: 0x2ee2
+  __TEXT.__cstring: 0x2f06
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
   Functions: 498
   Symbols:   169
-  CStrings:  303
+  CStrings:  304
 
Functions:
~ sub_fffffc000000389c : 8184 -> 8196
~ sub_fffffc000000df3c -> sub_fffffc000000df48 : 4920 -> 4940
~ sub_fffffc00000101b4 -> sub_fffffc00000101d4 : 2348 -> 2376
~ sub_fffffc0000013784 -> sub_fffffc00000137c0 : 10636 -> 11140
~ sub_fffffc00000178d8 -> sub_fffffc0000017b0c : 10152 -> 10156
~ sub_fffffc000001a258 -> sub_fffffc000001a490 : 5176 -> 5248
~ sub_fffffc000001cf74 -> sub_fffffc000001d1f4 : 2100 -> 2148
~ sub_fffffc0000021270 -> sub_fffffc0000021520 : 584 -> 600
~ sub_fffffc0000021ab8 -> sub_fffffc0000021d78 : 804 -> 820
~ sub_fffffc0000021f80 -> sub_fffffc0000022250 : 1784 -> 1800
~ sub_fffffc0000026554 -> sub_fffffc0000026834 : 1584 -> 1640
~ sub_fffffc0000026b84 -> sub_fffffc0000026e9c : 252 -> 280
~ sub_fffffc0000028b20 -> sub_fffffc0000028e54 : 360 -> 352
~ sub_fffffc0000029288 -> sub_fffffc00000295b4 : 1772 -> 1788
~ sub_fffffc000002a0c0 -> sub_fffffc000002a3fc : 756 -> 768
~ sub_fffffc000002a748 -> sub_fffffc000002aa90 : 848 -> 832
~ sub_fffffc000002b188 -> sub_fffffc000002b4c0 : 2332 -> 2340
~ sub_fffffc000003170c -> sub_fffffc0000031a4c : 1636 -> 1660
~ sub_fffffc0000031d70 -> sub_fffffc00000320c8 : 2192 -> 2204
~ sub_fffffc0000039524 -> sub_fffffc0000039888 : 6928 -> 7664
~ sub_fffffc000003b034 -> sub_fffffc000003b678 : 1944 -> 2064
CStrings:
+ "Aug 11 2026 21:46:56"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:26:16"
```
