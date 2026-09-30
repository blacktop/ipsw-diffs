## agx_a000

> `Firmware/agx/armfw_g15d.im4p/agx_a000`

```diff

-  __TEXT.__text: 0x53af0
+  __TEXT.__text: 0x53cc8
   __TEXT.__gxf_code: 0x10cc
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560

   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0xf10
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0xad0
+  __DATA.__const: 0xae8
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xcb8f8
-  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x78000
+  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 522
-  Symbols:   178
+  Symbols:   179
   CStrings:  292
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __DATA.__data : content changed
~ __DATA._rtk_mtab : content changed
~ __DATA.__mod_init_func : content changed
Symbols:
+ _gCrashLog
Functions:
~ sub_fffffc0000003010 : 1420 -> 1428
~ sub_fffffc00000036b4 -> sub_fffffc00000036bc : 8816 -> 8832
~ sub_fffffc000000b13c -> sub_fffffc000000b154 : 19744 -> 19736
~ sub_fffffc000001e9a4 -> sub_fffffc000001e9b4 : 1292 -> 1344
~ sub_fffffc0000022190 -> sub_fffffc00000221d4 : 1068 -> 1104
~ sub_fffffc0000022e2c -> sub_fffffc0000022e94 : 1612 -> 1672
~ sub_fffffc0000023e28 -> sub_fffffc0000023ecc : 1032 -> 1092
~ sub_fffffc000002d8ec -> sub_fffffc000002d9cc : 520 -> 668
~ sub_fffffc000002f6cc -> sub_fffffc000002f840 : 1816 -> 1544
~ sub_fffffc000003511c -> sub_fffffc0000035180 : 544 -> 568
~ sub_fffffc0000037f64 -> sub_fffffc0000037fe0 : 1064 -> 1072
~ sub_fffffc000003838c -> sub_fffffc0000038410 : 132 -> 140
~ sub_fffffc0000039638 -> sub_fffffc00000396c4 : 1772 -> 1784
~ sub_fffffc0000039d24 -> sub_fffffc0000039dbc : 3364 -> 3432
~ sub_fffffc000003aa48 -> sub_fffffc000003ab24 : 6864 -> 6868
~ sub_fffffc000003c518 -> sub_fffffc000003c5f8 : 1684 -> 1860
~ sub_fffffc000003d7bc -> sub_fffffc000003d94c : 1568 -> 1508
~ sub_fffffc000003dddc -> sub_fffffc000003df30 : 400 -> 536
~ sub_fffffc000003df6c -> sub_fffffc000003e148 : 364 -> 384
~ sub_fffffc000003e0d8 -> sub_fffffc000003e2c8 : 808 -> 800
~ sub_fffffc000003e744 -> sub_fffffc000003e92c : 6192 -> 6220
~ sub_fffffc0000042c8c -> sub_fffffc0000042e90 : 748 -> 752
~ sub_fffffc0000042fb4 -> sub_fffffc00000431bc : 432 -> 436
~ sub_fffffc00000432e0 -> sub_fffffc00000434ec : 1880 -> 1832
~ sub_fffffc0000043bc8 -> sub_fffffc0000043da4 : 304 -> 288
~ sub_fffffc00000459c8 -> sub_fffffc0000045b94 : 236 -> 240
~ sub_fffffc0000046bb4 -> sub_fffffc0000046d84 : 820 -> 824
~ sub_fffffc00000477c0 -> sub_fffffc0000047994 : 112 -> 96
~ sub_fffffc0000047830 -> sub_fffffc00000479f4 : 468 -> 452
~ sub_fffffc0000047a04 -> sub_fffffc0000047bb8 : 748 -> 724
~ sub_fffffc0000047cf0 -> sub_fffffc0000047e8c : 96 -> 80
~ sub_fffffc0000047d50 -> sub_fffffc0000047edc : 252 -> 248
~ sub_fffffc000004d334 -> sub_fffffc000004d4bc : 172 -> 168
~ sub_fffffc000004d840 -> sub_fffffc000004d9c4 : 224 -> 228
~ sub_fffffc000004e500 -> sub_fffffc000004e688 : 548 -> 544
~ sub_fffffc00000508d8 -> sub_fffffc0000050a5c : 228 -> 244
~ sub_fffffc0000050a94 -> sub_fffffc0000050c28 : 168 -> 236
~ sub_fffffc0000050b3c -> sub_fffffc0000050d14 : 248 -> 228
~ sub_fffffc0000051370 -> sub_fffffc0000051534 : 3192 -> 3188
~ sub_fffffc0000052ddc -> sub_fffffc0000052f9c : 2608 -> 2632
~ sub_fffffc00000539ac -> sub_fffffc0000053b84 : 324 -> 332
CStrings:
+ "Jun 29 2026 23:32:12"
- "Jun 16 2026 21:33:12"

```
