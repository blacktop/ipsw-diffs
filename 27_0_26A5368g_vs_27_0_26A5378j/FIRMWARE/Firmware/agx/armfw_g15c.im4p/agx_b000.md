## agx_b000

> `Firmware/agx/armfw_g15c.im4p/agx_b000`

```diff

-  __TEXT.__text: 0x52ab8
+  __TEXT.__text: 0x52c90
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
   __DATA.__zerofill: 0xcb778
-  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x78000
+  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 519
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
~ sub_fffffc0000002f2c : 1392 -> 1400
~ sub_fffffc00000035b4 -> sub_fffffc00000035bc : 8860 -> 8876
~ sub_fffffc000000ac10 -> sub_fffffc000000ac28 : 18020 -> 18012
~ sub_fffffc000001dec8 -> sub_fffffc000001ded8 : 1292 -> 1344
~ sub_fffffc00000216b4 -> sub_fffffc00000216f8 : 1068 -> 1104
~ sub_fffffc0000022350 -> sub_fffffc00000223b8 : 1612 -> 1672
~ sub_fffffc000002334c -> sub_fffffc00000233f0 : 1032 -> 1092
~ sub_fffffc000002ce80 -> sub_fffffc000002cf60 : 520 -> 668
~ sub_fffffc000002ea10 -> sub_fffffc000002eb84 : 1816 -> 1544
~ sub_fffffc0000034398 -> sub_fffffc00000343fc : 500 -> 524
~ sub_fffffc0000036fe0 -> sub_fffffc000003705c : 1064 -> 1072
~ sub_fffffc0000037408 -> sub_fffffc000003748c : 132 -> 140
~ sub_fffffc00000386fc -> sub_fffffc0000038788 : 1772 -> 1784
~ sub_fffffc0000038de8 -> sub_fffffc0000038e80 : 3364 -> 3432
~ sub_fffffc0000039b0c -> sub_fffffc0000039be8 : 6864 -> 6868
~ sub_fffffc000003b5dc -> sub_fffffc000003b6bc : 1684 -> 1860
~ sub_fffffc000003c880 -> sub_fffffc000003ca10 : 1568 -> 1508
~ sub_fffffc000003cea0 -> sub_fffffc000003cff4 : 400 -> 536
~ sub_fffffc000003d030 -> sub_fffffc000003d20c : 364 -> 384
~ sub_fffffc000003d19c -> sub_fffffc000003d38c : 808 -> 800
~ sub_fffffc000003d7a4 -> sub_fffffc000003d98c : 6040 -> 6068
~ sub_fffffc0000041c54 -> sub_fffffc0000041e58 : 748 -> 752
~ sub_fffffc0000041f7c -> sub_fffffc0000042184 : 432 -> 436
~ sub_fffffc00000422a8 -> sub_fffffc00000424b4 : 1880 -> 1832
~ sub_fffffc0000042b90 -> sub_fffffc0000042d6c : 304 -> 288
~ sub_fffffc0000044990 -> sub_fffffc0000044b5c : 236 -> 240
~ sub_fffffc0000045b7c -> sub_fffffc0000045d4c : 820 -> 824
~ sub_fffffc0000046788 -> sub_fffffc000004695c : 112 -> 96
~ sub_fffffc00000467f8 -> sub_fffffc00000469bc : 468 -> 452
~ sub_fffffc00000469cc -> sub_fffffc0000046b80 : 748 -> 724
~ sub_fffffc0000046cb8 -> sub_fffffc0000046e54 : 96 -> 80
~ sub_fffffc0000046d18 -> sub_fffffc0000046ea4 : 252 -> 248
~ sub_fffffc000004c2fc -> sub_fffffc000004c484 : 172 -> 168
~ sub_fffffc000004c808 -> sub_fffffc000004c98c : 224 -> 228
~ sub_fffffc000004d4c8 -> sub_fffffc000004d650 : 548 -> 544
~ sub_fffffc000004f8a0 -> sub_fffffc000004fa24 : 228 -> 244
~ sub_fffffc000004fa5c -> sub_fffffc000004fbf0 : 168 -> 236
~ sub_fffffc000004fb04 -> sub_fffffc000004fcdc : 248 -> 228
~ sub_fffffc0000050338 -> sub_fffffc00000504fc : 3192 -> 3188
~ sub_fffffc0000051da4 -> sub_fffffc0000051f64 : 2608 -> 2632
~ sub_fffffc0000052974 -> sub_fffffc0000052b4c : 332 -> 324
CStrings:
+ "Jun 29 2026 23:37:43"
- "Jun 16 2026 21:39:24"

```
