## agx_a000

> `Firmware/agx/armfw_g17g.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3d270
+  __TEXT.__text: 0x3d224
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x106f
+  __TEXT.__const: 0x1070
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
-  __TEXT.__cstring: 0x234e
+  __TEXT.__cstring: 0x234c
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA.__gxf_data: 0x80b8
Functions:
~ sub_fffffc00000241d4 : 368 -> 384
~ sub_fffffc000002b858 -> sub_fffffc000002b868 : 112 -> 116
~ sub_fffffc000002d71c -> sub_fffffc000002d730 : 832 -> 836
~ sub_fffffc000002e558 -> sub_fffffc000002e570 : 724 -> 720
~ sub_fffffc000002f320 -> sub_fffffc000002f334 : 368 -> 364
~ sub_fffffc000002f51c -> sub_fffffc000002f52c : 468 -> 456
~ sub_fffffc000002f758 -> sub_fffffc000002f75c : 664 -> 652
~ sub_fffffc000002f9f0 -> sub_fffffc000002f9e8 : 1008 -> 992
~ sub_fffffc000002fde0 -> sub_fffffc000002fdc8 : 268 -> 256
~ sub_fffffc00000302a0 -> sub_fffffc000003027c : 956 -> 988
~ sub_fffffc00000311e4 -> sub_fffffc00000311e0 : 328 -> 324
~ sub_fffffc000003187c -> sub_fffffc0000031874 : 468 -> 480
~ sub_fffffc0000031b5c -> sub_fffffc0000031b60 : 2832 -> 2840
~ sub_fffffc0000034dbc -> sub_fffffc0000034dc8 : 196 -> 192
~ sub_fffffc00000362ec -> sub_fffffc00000362f4 : 528 -> 524
~ sub_fffffc0000038074 -> sub_fffffc0000038078 : 656 -> 652
~ sub_fffffc0000038304 : 796 -> 792
~ sub_fffffc00000386c8 -> sub_fffffc00000386c4 : 672 -> 668
~ sub_fffffc0000038b28 -> sub_fffffc0000038b20 : 228 -> 224
~ sub_fffffc00000397f4 -> sub_fffffc00000397e8 : 544 -> 532
~ sub_fffffc000003ab2c -> sub_fffffc000003ab14 : 800 -> 816
~ sub_fffffc000003b258 -> sub_fffffc000003b250 : 508 -> 504
~ sub_fffffc000003b734 -> sub_fffffc000003b728 : 552 -> 540
~ sub_fffffc000003b9ec -> sub_fffffc000003b9d4 : 212 -> 200
~ sub_fffffc000003c024 -> sub_fffffc000003c000 : 208 -> 204
~ sub_fffffc000003c668 -> sub_fffffc000003c640 : 2332 -> 2300
~ sub_fffffc000003d128 -> sub_fffffc000003d0e0 : 328 -> 324
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:22:44"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:33:24"
```
