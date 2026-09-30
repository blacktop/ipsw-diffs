## agx_b000

> `Firmware/agx/armfw_g16g.im4p/agx_b000`

```diff

-  __TEXT.__text: 0x5239c
-  __TEXT.__gxf_code: 0x50b0
+  __TEXT.__text: 0x52614
+  __TEXT.__gxf_code: 0x5080
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1db7

   __DATA.__gxf_data: 0x81b0
   __DATA.__data: 0xeb8
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0xb18
+  __DATA.__const: 0xb30
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0x7a278
-  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x78000
+  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 517
-  Symbols:   188
+  Symbols:   189
   CStrings:  267
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __DATA.__gxf_data : content changed
~ __DATA.__data : content changed
~ __DATA._rtk_mtab : content changed
~ __DATA.__mod_init_func : content changed
Symbols:
+ _gCrashLog
Functions:
~ sub_fffffc0000003350 : 1296 -> 1308
~ sub_fffffc0000003978 -> sub_fffffc0000003984 : 8020 -> 8028
~ sub_fffffc000000b7b4 -> sub_fffffc000000b7c8 : 17784 -> 17776
~ sub_fffffc000001e5fc -> sub_fffffc000001e608 : 1220 -> 1272
~ sub_fffffc0000022340 -> sub_fffffc0000022380 : 1068 -> 1104
~ sub_fffffc0000023498 -> sub_fffffc00000234fc : 1544 -> 1596
~ sub_fffffc000002441c -> sub_fffffc00000244b4 : 1036 -> 1088
~ sub_fffffc000002e008 -> sub_fffffc000002e0d4 : 436 -> 468
~ sub_fffffc0000030270 -> sub_fffffc000003035c : 1520 -> 1568
~ sub_fffffc0000036b64 -> sub_fffffc0000036c80 : 896 -> 904
~ sub_fffffc0000036ee4 -> sub_fffffc0000037008 : 132 -> 140
~ sub_fffffc0000038244 -> sub_fffffc0000038370 : 1444 -> 1456
~ sub_fffffc00000387e8 -> sub_fffffc0000038920 : 3684 -> 3752
~ sub_fffffc000003964c -> sub_fffffc00000397c8 : 7300 -> 7304
~ sub_fffffc000003b2d0 -> sub_fffffc000003b450 : 1540 -> 1716
~ sub_fffffc000003c85c -> sub_fffffc000003ca8c : 1452 -> 1392
~ sub_fffffc000003ce08 -> sub_fffffc000003cffc : 400 -> 536
~ sub_fffffc000003cf98 -> sub_fffffc000003d214 : 364 -> 384
~ sub_fffffc000003d104 -> sub_fffffc000003d394 : 792 -> 784
~ sub_fffffc000003d610 -> sub_fffffc000003d898 : 5264 -> 5292
~ sub_fffffc000004182c -> sub_fffffc0000041ad0 : 828 -> 832
~ sub_fffffc0000042440 -> sub_fffffc00000426e8 : 112 -> 96
~ sub_fffffc00000424b0 -> sub_fffffc0000042748 : 468 -> 452
~ sub_fffffc0000042684 -> sub_fffffc000004290c : 748 -> 724
~ sub_fffffc0000042970 -> sub_fffffc0000042be0 : 96 -> 80
~ sub_fffffc00000429d0 -> sub_fffffc0000042c30 : 252 -> 248
~ sub_fffffc00000466a8 -> sub_fffffc0000046904 : 3192 -> 3188
~ sub_fffffc0000047bcc -> sub_fffffc0000047e24 : 748 -> 752
~ sub_fffffc0000047ef4 -> sub_fffffc0000048150 : 432 -> 436
~ sub_fffffc0000048220 -> sub_fffffc0000048480 : 1880 -> 1832
~ sub_fffffc0000048b08 -> sub_fffffc0000048d38 : 304 -> 288
~ sub_fffffc000004a914 -> sub_fffffc000004ab34 : 236 -> 240
~ sub_fffffc000004d29c -> sub_fffffc000004d4c0 : 172 -> 168
~ sub_fffffc000004d7a0 -> sub_fffffc000004d9c0 : 224 -> 228
~ sub_fffffc000004e464 -> sub_fffffc000004e688 : 548 -> 544
~ sub_fffffc0000050824 -> sub_fffffc0000050a44 : 228 -> 244
~ sub_fffffc00000509e0 -> sub_fffffc0000050c10 : 168 -> 236
~ sub_fffffc0000050a88 -> sub_fffffc0000050cfc : 248 -> 228
~ sub_fffffc000005159c -> sub_fffffc00000517fc : 2844 -> 2868
~ sub_fffffc0000052258 -> sub_fffffc00000524d0 : 332 -> 324
CStrings:
+ "Jun 29 2026 23:36:40"
- "Jun 16 2026 21:38:13"

```
