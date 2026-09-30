## agx_a000

> `Firmware/agx/armfw_g15d.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x53cc8
-  __TEXT.__gxf_code: 0x10cc
+  __TEXT.__text: 0x53c74
+  __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x12a8
-  __TEXT.__cstring: 0x2bad
+  __TEXT.__cstring: 0x2bab
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__init_offsets: 0x0
Functions:
~ sub_fffffc0000040c58 : 348 -> 356
~ sub_fffffc0000041298 -> sub_fffffc00000412a0 : 112 -> 116
~ sub_fffffc0000044ecc -> sub_fffffc0000044ed8 : 196 -> 192
~ sub_fffffc00000461b8 -> sub_fffffc00000461c0 : 528 -> 524
~ sub_fffffc0000046d84 -> sub_fffffc0000046d88 : 824 -> 828
~ sub_fffffc0000047bb8 -> sub_fffffc0000047bc0 : 724 -> 720
~ sub_fffffc0000048970 -> sub_fffffc0000048974 : 368 -> 364
~ sub_fffffc0000048b6c : 468 -> 456
~ sub_fffffc0000048da8 -> sub_fffffc0000048d9c : 664 -> 652
~ sub_fffffc0000049040 -> sub_fffffc0000049028 : 1008 -> 992
~ sub_fffffc0000049430 -> sub_fffffc0000049408 : 268 -> 256
~ sub_fffffc00000498f0 -> sub_fffffc00000498bc : 956 -> 988
~ sub_fffffc000004a830 -> sub_fffffc000004a81c : 328 -> 324
~ sub_fffffc000004ac34 -> sub_fffffc000004ac1c : 420 -> 416
~ sub_fffffc000004b8c0 -> sub_fffffc000004b8a4 : 480 -> 492
~ sub_fffffc000004cf0c -> sub_fffffc000004cefc : 668 -> 664
~ sub_fffffc000004d1a8 -> sub_fffffc000004d194 : 788 -> 776
~ sub_fffffc000004d564 -> sub_fffffc000004d544 : 672 -> 668
~ sub_fffffc000004d9c4 -> sub_fffffc000004d9a0 : 228 -> 224
~ sub_fffffc000004e688 -> sub_fffffc000004e660 : 544 -> 532
~ sub_fffffc000004fad0 -> sub_fffffc000004fa9c : 792 -> 808
~ sub_fffffc00000501f4 -> sub_fffffc00000501d0 : 508 -> 504
~ sub_fffffc00000506d8 -> sub_fffffc00000506b0 : 420 -> 412
~ sub_fffffc000005090c -> sub_fffffc00000508dc : 212 -> 200
~ sub_fffffc0000050f04 -> sub_fffffc0000050ec8 : 328 -> 324
~ sub_fffffc000005104c -> sub_fffffc000005100c : 208 -> 204
~ sub_fffffc0000051534 -> sub_fffffc00000514f0 : 3188 -> 3196
~ sub_fffffc0000052f9c -> sub_fffffc0000052f60 : 2632 -> 2612
~ sub_fffffc0000053b84 -> sub_fffffc0000053b34 : 332 -> 320
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:21:35"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:32:12"
```
