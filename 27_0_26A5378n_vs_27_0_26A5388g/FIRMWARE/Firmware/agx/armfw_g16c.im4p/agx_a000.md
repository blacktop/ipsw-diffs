## agx_a000

> `Firmware/agx/armfw_g16c.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x51554
+  __TEXT.__text: 0x514f8
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x12e7
+  __TEXT.__const: 0x12e8
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x6a0
-  __TEXT.__cstring: 0x2f52
+  __TEXT.__cstring: 0x2f50
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA.__gxf_data: 0x80b8
Functions:
~ sub_fffffc000003ec18 : 112 -> 116
~ sub_fffffc0000040ac8 -> sub_fffffc0000040acc : 832 -> 836
~ sub_fffffc0000041904 -> sub_fffffc000004190c : 724 -> 720
~ sub_fffffc00000426c8 -> sub_fffffc00000426cc : 368 -> 364
~ sub_fffffc00000428c4 : 468 -> 456
~ sub_fffffc0000042b00 -> sub_fffffc0000042af4 : 664 -> 652
~ sub_fffffc0000042d98 -> sub_fffffc0000042d80 : 1008 -> 992
~ sub_fffffc0000043188 -> sub_fffffc0000043160 : 268 -> 256
~ sub_fffffc0000043648 -> sub_fffffc0000043614 : 956 -> 988
~ sub_fffffc0000044588 -> sub_fffffc0000044574 : 328 -> 324
~ sub_fffffc000004498c -> sub_fffffc0000044974 : 420 -> 416
~ sub_fffffc0000045618 -> sub_fffffc00000455fc : 468 -> 480
~ sub_fffffc00000458f8 -> sub_fffffc00000458e8 : 3188 -> 3196
~ sub_fffffc0000048d30 -> sub_fffffc0000048d28 : 196 -> 192
~ sub_fffffc000004a07c -> sub_fffffc000004a070 : 528 -> 524
~ sub_fffffc000004bdac -> sub_fffffc000004bd9c : 668 -> 664
~ sub_fffffc000004c048 -> sub_fffffc000004c034 : 788 -> 776
~ sub_fffffc000004c404 -> sub_fffffc000004c3e4 : 672 -> 668
~ sub_fffffc000004c864 -> sub_fffffc000004c840 : 228 -> 224
~ sub_fffffc000004d528 -> sub_fffffc000004d500 : 544 -> 532
~ sub_fffffc000004e964 -> sub_fffffc000004e930 : 792 -> 808
~ sub_fffffc000004f088 -> sub_fffffc000004f064 : 508 -> 504
~ sub_fffffc000004f56c -> sub_fffffc000004f544 : 420 -> 412
~ sub_fffffc000004f7a0 -> sub_fffffc000004f770 : 212 -> 200
~ sub_fffffc000004fc8c -> sub_fffffc000004fc50 : 328 -> 324
~ sub_fffffc000004fdd4 -> sub_fffffc000004fd94 : 208 -> 204
~ sub_fffffc000005074c -> sub_fffffc0000050708 : 2852 -> 2832
~ sub_fffffc0000051410 -> sub_fffffc00000513b8 : 324 -> 328
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:21:35"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:32:11"
```
