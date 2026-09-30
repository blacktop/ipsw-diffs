## agx_b000

> `Firmware/agx/armfw_g15s.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x50270
-  __TEXT.__gxf_code: 0x10cc
+  __TEXT.__text: 0x50220
+  __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1120
-  __TEXT.__cstring: 0x2782
+  __TEXT.__cstring: 0x2780
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__init_offsets: 0x0
Functions:
~ sub_fffffc000003dc68 : 348 -> 356
~ sub_fffffc000003e2a8 -> sub_fffffc000003e2b0 : 112 -> 116
~ sub_fffffc0000041ee0 -> sub_fffffc0000041eec : 196 -> 192
~ sub_fffffc00000431d8 -> sub_fffffc00000431e0 : 528 -> 524
~ sub_fffffc0000043da4 -> sub_fffffc0000043da8 : 824 -> 828
~ sub_fffffc0000044bd8 -> sub_fffffc0000044be0 : 724 -> 720
~ sub_fffffc0000045990 -> sub_fffffc0000045994 : 368 -> 364
~ sub_fffffc0000045b8c : 468 -> 456
~ sub_fffffc0000045dc8 -> sub_fffffc0000045dbc : 664 -> 652
~ sub_fffffc0000046060 -> sub_fffffc0000046048 : 1008 -> 992
~ sub_fffffc0000046450 -> sub_fffffc0000046428 : 268 -> 256
~ sub_fffffc0000046910 -> sub_fffffc00000468dc : 956 -> 988
~ sub_fffffc0000047850 -> sub_fffffc000004783c : 328 -> 324
~ sub_fffffc0000047ee8 -> sub_fffffc0000047ed0 : 480 -> 492
~ sub_fffffc0000049534 -> sub_fffffc0000049528 : 668 -> 664
~ sub_fffffc00000497d0 -> sub_fffffc00000497c0 : 796 -> 792
~ sub_fffffc0000049b94 -> sub_fffffc0000049b80 : 672 -> 668
~ sub_fffffc0000049ff4 -> sub_fffffc0000049fdc : 228 -> 224
~ sub_fffffc000004acc0 -> sub_fffffc000004aca4 : 544 -> 532
~ sub_fffffc000004c108 -> sub_fffffc000004c0e0 : 800 -> 816
~ sub_fffffc000004c834 -> sub_fffffc000004c81c : 504 -> 500
~ sub_fffffc000004cd14 -> sub_fffffc000004ccf8 : 420 -> 412
~ sub_fffffc000004cf48 -> sub_fffffc000004cf24 : 212 -> 200
~ sub_fffffc000004d68c -> sub_fffffc000004d65c : 208 -> 204
~ sub_fffffc000004db74 -> sub_fffffc000004db40 : 3192 -> 3200
~ sub_fffffc000004f47c -> sub_fffffc000004f450 : 2828 -> 2796
~ sub_fffffc0000050128 -> sub_fffffc00000500dc : 328 -> 324
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:26:15"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:37:33"
```
