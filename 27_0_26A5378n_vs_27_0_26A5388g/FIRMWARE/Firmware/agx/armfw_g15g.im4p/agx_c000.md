## agx_c000

> `Firmware/agx/armfw_g15g.im4p/agx_c000`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x5493c
-  __TEXT.__gxf_code: 0x10cc
+  __TEXT.__text: 0x548ec
+  __TEXT.__gxf_code: 0x10c8
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x23f4
-  __TEXT.__cstring: 0x25a6
+  __TEXT.__cstring: 0x25a4
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__init_offsets: 0x0
Functions:
~ sub_fffffc00000429d0 : 348 -> 356
~ sub_fffffc0000043010 -> sub_fffffc0000043018 : 88 -> 92
~ sub_fffffc0000046b4c -> sub_fffffc0000046b58 : 196 -> 192
~ sub_fffffc0000047e64 -> sub_fffffc0000047e6c : 528 -> 524
~ sub_fffffc0000048a34 -> sub_fffffc0000048a38 : 824 -> 828
~ sub_fffffc0000049868 -> sub_fffffc0000049870 : 724 -> 720
~ sub_fffffc000004a620 -> sub_fffffc000004a624 : 368 -> 364
~ sub_fffffc000004a81c : 468 -> 456
~ sub_fffffc000004aa58 -> sub_fffffc000004aa4c : 664 -> 652
~ sub_fffffc000004acf0 -> sub_fffffc000004acd8 : 1008 -> 992
~ sub_fffffc000004b0e0 -> sub_fffffc000004b0b8 : 268 -> 256
~ sub_fffffc000004b5a0 -> sub_fffffc000004b56c : 956 -> 988
~ sub_fffffc000004c4e0 -> sub_fffffc000004c4cc : 328 -> 324
~ sub_fffffc000004cb78 -> sub_fffffc000004cb60 : 480 -> 492
~ sub_fffffc000004e1c4 -> sub_fffffc000004e1b8 : 668 -> 664
~ sub_fffffc000004e460 -> sub_fffffc000004e450 : 796 -> 792
~ sub_fffffc000004e824 -> sub_fffffc000004e810 : 672 -> 668
~ sub_fffffc000004ec84 -> sub_fffffc000004ec6c : 228 -> 224
~ sub_fffffc000004f954 -> sub_fffffc000004f938 : 544 -> 532
~ sub_fffffc0000050d98 -> sub_fffffc0000050d70 : 800 -> 816
~ sub_fffffc00000514c4 -> sub_fffffc00000514ac : 504 -> 500
~ sub_fffffc00000519a0 -> sub_fffffc0000051984 : 420 -> 412
~ sub_fffffc0000051bd4 -> sub_fffffc0000051bb0 : 212 -> 200
~ sub_fffffc0000052318 -> sub_fffffc00000522e8 : 208 -> 204
~ sub_fffffc00000523e8 -> sub_fffffc00000523b4 : 3200 -> 3208
~ sub_fffffc0000053ba0 -> sub_fffffc0000053b74 : 2740 -> 2708
~ sub_fffffc00000547f4 -> sub_fffffc00000547a8 : 336 -> 332
CStrings:
+ "!MIDR: 0x%x"
+ "Jul 14 2026 21:28:03"
- "!MIDR: 0x%llx"
- "Jun 29 2026 23:39:35"
```
