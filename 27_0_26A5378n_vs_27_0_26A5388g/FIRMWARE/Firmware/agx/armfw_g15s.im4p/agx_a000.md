## agx_a000

> `Firmware/agx/armfw_g15s.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x5069c
-  __TEXT.__gxf_code: 0x10cc
+  __TEXT.__text: 0x5064c
+  __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1120
-  __TEXT.__cstring: 0x279f
+  __TEXT.__cstring: 0x279d
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__init_offsets: 0x0
Functions:
~ sub_fffffc000003e094 : 348 -> 356
~ sub_fffffc000003e6d4 -> sub_fffffc000003e6dc : 112 -> 116
~ sub_fffffc000004230c -> sub_fffffc0000042318 : 196 -> 192
~ sub_fffffc0000043604 -> sub_fffffc000004360c : 528 -> 524
~ sub_fffffc00000441d0 -> sub_fffffc00000441d4 : 824 -> 828
~ sub_fffffc0000045004 -> sub_fffffc000004500c : 724 -> 720
~ sub_fffffc0000045dbc -> sub_fffffc0000045dc0 : 368 -> 364
~ sub_fffffc0000045fb8 : 468 -> 456
~ sub_fffffc00000461f4 -> sub_fffffc00000461e8 : 664 -> 652
~ sub_fffffc000004648c -> sub_fffffc0000046474 : 1008 -> 992
~ sub_fffffc000004687c -> sub_fffffc0000046854 : 268 -> 256
~ sub_fffffc0000046d3c -> sub_fffffc0000046d08 : 956 -> 988
~ sub_fffffc0000047c7c -> sub_fffffc0000047c68 : 328 -> 324
~ sub_fffffc0000048314 -> sub_fffffc00000482fc : 480 -> 492
~ sub_fffffc0000049960 -> sub_fffffc0000049954 : 668 -> 664
~ sub_fffffc0000049bfc -> sub_fffffc0000049bec : 796 -> 792
~ sub_fffffc0000049fc0 -> sub_fffffc0000049fac : 672 -> 668
~ sub_fffffc000004a420 -> sub_fffffc000004a408 : 228 -> 224
~ sub_fffffc000004b0ec -> sub_fffffc000004b0d0 : 544 -> 532
~ sub_fffffc000004c534 -> sub_fffffc000004c50c : 800 -> 816
~ sub_fffffc000004cc60 -> sub_fffffc000004cc48 : 504 -> 500
~ sub_fffffc000004d140 -> sub_fffffc000004d124 : 420 -> 412
~ sub_fffffc000004d374 -> sub_fffffc000004d350 : 212 -> 200
~ sub_fffffc000004dab8 -> sub_fffffc000004da88 : 208 -> 204
~ sub_fffffc000004dfa0 -> sub_fffffc000004df6c : 3192 -> 3200
~ sub_fffffc000004f8a8 -> sub_fffffc000004f87c : 2828 -> 2796
~ sub_fffffc0000050554 -> sub_fffffc0000050508 : 336 -> 332
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:21:32"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:32:09"
```
