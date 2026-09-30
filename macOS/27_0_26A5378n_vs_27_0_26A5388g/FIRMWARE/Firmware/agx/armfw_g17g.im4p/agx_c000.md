## agx_c000

> `Firmware/agx/armfw_g17g.im4p/agx_c000`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3ce9c
+  __TEXT.__text: 0x3ce50
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x106f
+  __TEXT.__const: 0x1070
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
-  __TEXT.__cstring: 0x2404
+  __TEXT.__cstring: 0x2402
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA.__gxf_data: 0x80b8
Functions:
~ sub_fffffc0000023d90 : 368 -> 384
~ sub_fffffc000002b484 -> sub_fffffc000002b494 : 112 -> 116
~ sub_fffffc000002d348 -> sub_fffffc000002d35c : 832 -> 836
~ sub_fffffc000002e184 -> sub_fffffc000002e19c : 724 -> 720
~ sub_fffffc000002ef4c -> sub_fffffc000002ef60 : 368 -> 364
~ sub_fffffc000002f148 -> sub_fffffc000002f158 : 468 -> 456
~ sub_fffffc000002f384 -> sub_fffffc000002f388 : 664 -> 652
~ sub_fffffc000002f61c -> sub_fffffc000002f614 : 1008 -> 992
~ sub_fffffc000002fa0c -> sub_fffffc000002f9f4 : 268 -> 256
~ sub_fffffc000002fecc -> sub_fffffc000002fea8 : 956 -> 988
~ sub_fffffc0000030e10 -> sub_fffffc0000030e0c : 328 -> 324
~ sub_fffffc00000314a8 -> sub_fffffc00000314a0 : 468 -> 480
~ sub_fffffc0000031788 -> sub_fffffc000003178c : 2832 -> 2840
~ sub_fffffc00000349e8 -> sub_fffffc00000349f4 : 196 -> 192
~ sub_fffffc0000035f18 -> sub_fffffc0000035f20 : 528 -> 524
~ sub_fffffc0000037ca0 -> sub_fffffc0000037ca4 : 656 -> 652
~ sub_fffffc0000037f30 : 796 -> 792
~ sub_fffffc00000382f4 -> sub_fffffc00000382f0 : 672 -> 668
~ sub_fffffc0000038754 -> sub_fffffc000003874c : 228 -> 224
~ sub_fffffc0000039420 -> sub_fffffc0000039414 : 544 -> 532
~ sub_fffffc000003a758 -> sub_fffffc000003a740 : 800 -> 816
~ sub_fffffc000003ae84 -> sub_fffffc000003ae7c : 508 -> 504
~ sub_fffffc000003b360 -> sub_fffffc000003b354 : 552 -> 540
~ sub_fffffc000003b618 -> sub_fffffc000003b600 : 212 -> 200
~ sub_fffffc000003bc50 -> sub_fffffc000003bc2c : 208 -> 204
~ sub_fffffc000003c294 -> sub_fffffc000003c26c : 2332 -> 2300
~ sub_fffffc000003cd54 -> sub_fffffc000003cd0c : 336 -> 324
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:31:44"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:43:57"
```
