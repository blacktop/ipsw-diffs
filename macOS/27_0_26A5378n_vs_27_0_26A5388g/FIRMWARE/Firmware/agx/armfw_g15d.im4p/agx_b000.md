## agx_b000

> `Firmware/agx/armfw_g15d.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x53de4
-  __TEXT.__gxf_code: 0x10cc
+  __TEXT.__text: 0x53d90
+  __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x12a8
-  __TEXT.__cstring: 0x2b90
+  __TEXT.__cstring: 0x2b8e
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__init_offsets: 0x0
Functions:
~ sub_fffffc0000040d74 : 348 -> 356
~ sub_fffffc00000413b4 -> sub_fffffc00000413bc : 112 -> 116
~ sub_fffffc0000044fe8 -> sub_fffffc0000044ff4 : 196 -> 192
~ sub_fffffc00000462d4 -> sub_fffffc00000462dc : 528 -> 524
~ sub_fffffc0000046ea0 -> sub_fffffc0000046ea4 : 824 -> 828
~ sub_fffffc0000047cd4 -> sub_fffffc0000047cdc : 724 -> 720
~ sub_fffffc0000048a8c -> sub_fffffc0000048a90 : 368 -> 364
~ sub_fffffc0000048c88 : 468 -> 456
~ sub_fffffc0000048ec4 -> sub_fffffc0000048eb8 : 664 -> 652
~ sub_fffffc000004915c -> sub_fffffc0000049144 : 1008 -> 992
~ sub_fffffc000004954c -> sub_fffffc0000049524 : 268 -> 256
~ sub_fffffc0000049a0c -> sub_fffffc00000499d8 : 956 -> 988
~ sub_fffffc000004a94c -> sub_fffffc000004a938 : 328 -> 324
~ sub_fffffc000004ad50 -> sub_fffffc000004ad38 : 420 -> 416
~ sub_fffffc000004b9dc -> sub_fffffc000004b9c0 : 480 -> 492
~ sub_fffffc000004d028 -> sub_fffffc000004d018 : 668 -> 664
~ sub_fffffc000004d2c4 -> sub_fffffc000004d2b0 : 788 -> 776
~ sub_fffffc000004d680 -> sub_fffffc000004d660 : 672 -> 668
~ sub_fffffc000004dae0 -> sub_fffffc000004dabc : 228 -> 224
~ sub_fffffc000004e7a4 -> sub_fffffc000004e77c : 544 -> 532
~ sub_fffffc000004fbec -> sub_fffffc000004fbb8 : 792 -> 808
~ sub_fffffc0000050310 -> sub_fffffc00000502ec : 508 -> 504
~ sub_fffffc00000507f4 -> sub_fffffc00000507cc : 420 -> 412
~ sub_fffffc0000050a28 -> sub_fffffc00000509f8 : 212 -> 200
~ sub_fffffc0000051020 -> sub_fffffc0000050fe4 : 328 -> 324
~ sub_fffffc0000051168 -> sub_fffffc0000051128 : 208 -> 204
~ sub_fffffc0000051650 -> sub_fffffc000005160c : 3188 -> 3196
~ sub_fffffc00000530b8 -> sub_fffffc000005307c : 2632 -> 2612
~ sub_fffffc0000053ca0 -> sub_fffffc0000053c50 : 324 -> 320
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:26:31"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:37:52"
```
