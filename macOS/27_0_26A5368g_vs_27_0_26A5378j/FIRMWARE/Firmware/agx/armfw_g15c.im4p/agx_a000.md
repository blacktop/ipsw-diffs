## agx_a000

> `Firmware/agx/armfw_g15c.im4p/agx_a000`

```diff

-  __TEXT.__text: 0x52efc
+  __TEXT.__text: 0x530d4
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
   __DATA.__zerofill: 0xcb7f8
-  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x78000
+  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 520
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
~ sub_fffffc00000035b4 -> sub_fffffc00000035bc : 8892 -> 8908
~ sub_fffffc000000ac30 -> sub_fffffc000000ac48 : 17952 -> 17944
~ sub_fffffc000001de78 -> sub_fffffc000001de88 : 1292 -> 1344
~ sub_fffffc0000021664 -> sub_fffffc00000216a8 : 1068 -> 1104
~ sub_fffffc0000022300 -> sub_fffffc0000022368 : 1612 -> 1672
~ sub_fffffc00000232fc -> sub_fffffc00000233a0 : 1032 -> 1092
~ sub_fffffc000002cf30 -> sub_fffffc000002d010 : 520 -> 668
~ sub_fffffc000002eac0 -> sub_fffffc000002ec34 : 1816 -> 1544
~ sub_fffffc0000034448 -> sub_fffffc00000344ac : 500 -> 524
~ sub_fffffc0000037438 -> sub_fffffc00000374b4 : 1064 -> 1072
~ sub_fffffc0000037860 -> sub_fffffc00000378e4 : 132 -> 140
~ sub_fffffc0000038b54 -> sub_fffffc0000038be0 : 1772 -> 1784
~ sub_fffffc0000039240 -> sub_fffffc00000392d8 : 3364 -> 3432
~ sub_fffffc0000039f64 -> sub_fffffc000003a040 : 6876 -> 6880
~ sub_fffffc000003ba40 -> sub_fffffc000003bb20 : 1684 -> 1860
~ sub_fffffc000003cce4 -> sub_fffffc000003ce74 : 1568 -> 1508
~ sub_fffffc000003d304 -> sub_fffffc000003d458 : 400 -> 536
~ sub_fffffc000003d494 -> sub_fffffc000003d670 : 364 -> 384
~ sub_fffffc000003d600 -> sub_fffffc000003d7f0 : 808 -> 800
~ sub_fffffc000003dc08 -> sub_fffffc000003ddf0 : 6040 -> 6068
~ sub_fffffc0000042098 -> sub_fffffc000004229c : 748 -> 752
~ sub_fffffc00000423c0 -> sub_fffffc00000425c8 : 432 -> 436
~ sub_fffffc00000426ec -> sub_fffffc00000428f8 : 1880 -> 1832
~ sub_fffffc0000042fd4 -> sub_fffffc00000431b0 : 304 -> 288
~ sub_fffffc0000044dd4 -> sub_fffffc0000044fa0 : 236 -> 240
~ sub_fffffc0000045fc0 -> sub_fffffc0000046190 : 820 -> 824
~ sub_fffffc0000046bcc -> sub_fffffc0000046da0 : 112 -> 96
~ sub_fffffc0000046c3c -> sub_fffffc0000046e00 : 468 -> 452
~ sub_fffffc0000046e10 -> sub_fffffc0000046fc4 : 748 -> 724
~ sub_fffffc00000470fc -> sub_fffffc0000047298 : 96 -> 80
~ sub_fffffc000004715c -> sub_fffffc00000472e8 : 252 -> 248
~ sub_fffffc000004c740 -> sub_fffffc000004c8c8 : 172 -> 168
~ sub_fffffc000004cc4c -> sub_fffffc000004cdd0 : 224 -> 228
~ sub_fffffc000004d90c -> sub_fffffc000004da94 : 548 -> 544
~ sub_fffffc000004fce4 -> sub_fffffc000004fe68 : 228 -> 244
~ sub_fffffc000004fea0 -> sub_fffffc0000050034 : 168 -> 236
~ sub_fffffc000004ff48 -> sub_fffffc0000050120 : 248 -> 228
~ sub_fffffc000005077c -> sub_fffffc0000050940 : 3192 -> 3188
~ sub_fffffc00000521e8 -> sub_fffffc00000523a8 : 2608 -> 2632
~ sub_fffffc0000052db8 -> sub_fffffc0000052f90 : 332 -> 324
CStrings:
+ "Jun 29 2026 23:32:11"
- "Jun 16 2026 21:33:13"

```
