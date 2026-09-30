## agx_a000

> `Firmware/agx/armfw_g15c.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x530d4
-  __TEXT.__gxf_code: 0x10cc
+  __TEXT.__text: 0x53080
+  __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x11b8
-  __TEXT.__cstring: 0x2bad
+  __TEXT.__cstring: 0x2bab
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__init_offsets: 0x0
Functions:
~ sub_fffffc0000040064 : 348 -> 356
~ sub_fffffc00000406a4 -> sub_fffffc00000406ac : 112 -> 116
~ sub_fffffc00000442d8 -> sub_fffffc00000442e4 : 196 -> 192
~ sub_fffffc00000455c4 -> sub_fffffc00000455cc : 528 -> 524
~ sub_fffffc0000046190 -> sub_fffffc0000046194 : 824 -> 828
~ sub_fffffc0000046fc4 -> sub_fffffc0000046fcc : 724 -> 720
~ sub_fffffc0000047d7c -> sub_fffffc0000047d80 : 368 -> 364
~ sub_fffffc0000047f78 : 468 -> 456
~ sub_fffffc00000481b4 -> sub_fffffc00000481a8 : 664 -> 652
~ sub_fffffc000004844c -> sub_fffffc0000048434 : 1008 -> 992
~ sub_fffffc000004883c -> sub_fffffc0000048814 : 268 -> 256
~ sub_fffffc0000048cfc -> sub_fffffc0000048cc8 : 956 -> 988
~ sub_fffffc0000049c3c -> sub_fffffc0000049c28 : 328 -> 324
~ sub_fffffc000004a040 -> sub_fffffc000004a028 : 420 -> 416
~ sub_fffffc000004accc -> sub_fffffc000004acb0 : 480 -> 492
~ sub_fffffc000004c318 -> sub_fffffc000004c308 : 668 -> 664
~ sub_fffffc000004c5b4 -> sub_fffffc000004c5a0 : 788 -> 776
~ sub_fffffc000004c970 -> sub_fffffc000004c950 : 672 -> 668
~ sub_fffffc000004cdd0 -> sub_fffffc000004cdac : 228 -> 224
~ sub_fffffc000004da94 -> sub_fffffc000004da6c : 544 -> 532
~ sub_fffffc000004eedc -> sub_fffffc000004eea8 : 792 -> 808
~ sub_fffffc000004f600 -> sub_fffffc000004f5dc : 508 -> 504
~ sub_fffffc000004fae4 -> sub_fffffc000004fabc : 420 -> 412
~ sub_fffffc000004fd18 -> sub_fffffc000004fce8 : 212 -> 200
~ sub_fffffc0000050310 -> sub_fffffc00000502d4 : 328 -> 324
~ sub_fffffc0000050458 -> sub_fffffc0000050418 : 208 -> 204
~ sub_fffffc0000050940 -> sub_fffffc00000508fc : 3188 -> 3196
~ sub_fffffc00000523a8 -> sub_fffffc000005236c : 2632 -> 2612
~ sub_fffffc0000052f90 -> sub_fffffc0000052f40 : 324 -> 320
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:21:35"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:32:11"
```
