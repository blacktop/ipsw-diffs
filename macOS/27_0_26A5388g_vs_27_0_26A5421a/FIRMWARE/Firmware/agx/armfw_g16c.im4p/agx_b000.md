## agx_b000

> `Firmware/agx/armfw_g16c.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__TEXT.__chain_starts`
- `__DATA._rtk_mtab`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x51398
+  __TEXT.__text: 0x51a54
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
-  __DATA.__zerofill: 0x5eb58
+  __DATA.__zerofill: 0x5eb78
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 498
   Symbols:   169
-  CStrings:  303
+  CStrings:  304
 
Functions:
~ sub_fffffc000000389c : 8228 -> 8240
~ sub_fffffc000000e16c -> sub_fffffc000000e178 : 4920 -> 4940
~ sub_fffffc00000103e4 -> sub_fffffc0000010404 : 2348 -> 2376
~ sub_fffffc00000139b4 -> sub_fffffc00000139f0 : 10636 -> 11140
~ sub_fffffc0000017b08 -> sub_fffffc0000017d3c : 10152 -> 10156
~ sub_fffffc000001a488 -> sub_fffffc000001a6c0 : 5176 -> 5248
~ sub_fffffc000001d1a4 -> sub_fffffc000001d424 : 2100 -> 2148
~ sub_fffffc00000214a0 -> sub_fffffc0000021750 : 584 -> 600
~ sub_fffffc0000021ce4 -> sub_fffffc0000021fa4 : 804 -> 820
~ sub_fffffc00000221ac -> sub_fffffc000002247c : 1784 -> 1800
~ sub_fffffc0000026780 -> sub_fffffc0000026a60 : 1584 -> 1640
~ sub_fffffc0000026db0 -> sub_fffffc00000270c8 : 252 -> 280
~ sub_fffffc0000028d4c -> sub_fffffc0000029080 : 360 -> 352
~ sub_fffffc00000294b4 -> sub_fffffc00000297e0 : 1772 -> 1788
~ sub_fffffc000002a2ec -> sub_fffffc000002a628 : 756 -> 768
~ sub_fffffc000002a974 -> sub_fffffc000002acbc : 848 -> 832
~ sub_fffffc000002b3b4 -> sub_fffffc000002b6ec : 2332 -> 2340
~ sub_fffffc0000031938 -> sub_fffffc0000031c78 : 1636 -> 1660
~ sub_fffffc0000031f9c -> sub_fffffc00000322f4 : 2288 -> 2300
~ sub_fffffc0000039820 -> sub_fffffc0000039b84 : 6928 -> 7664
~ sub_fffffc000003b330 -> sub_fffffc000003b974 : 1944 -> 2064
~ sub_fffffc0000051258 -> sub_fffffc0000051914 : 328 -> 320
CStrings:
+ "Aug 11 2026 21:46:56"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
- "Jul 14 2026 21:26:15"
```
