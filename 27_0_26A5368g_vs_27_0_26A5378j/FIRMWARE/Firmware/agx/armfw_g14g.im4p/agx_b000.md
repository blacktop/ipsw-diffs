## agx_b000

> `Firmware/agx/armfw_g14g.im4p/agx_b000`

```diff

-  __TEXT.__text: 0x520a4
+  __TEXT.__text: 0x523a0
   __TEXT.__gxf_code: 0x10cc
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560

   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0xe20
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0x950
+  __DATA.__const: 0x968
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x40

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0x53238
-  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x78000
+  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 476
-  Symbols:   195
+  Symbols:   196
   CStrings:  236
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __DATA.__data : content changed
~ __DATA._rtk_mtab : content changed
~ __DATA.__mod_init_func : content changed
Symbols:
+ _gCrashLog
Functions:
~ sub_ffffff8000003350 : 852 -> 856
~ sub_ffffff8000008de8 -> sub_ffffff8000008dec : 11720 -> 11712
~ sub_ffffff80000195bc -> sub_ffffff80000195b8 : 1260 -> 1312
~ sub_ffffff800001bed8 -> sub_ffffff800001bf08 : 1164 -> 1200
~ sub_ffffff800001ce88 -> sub_ffffff800001cedc : 1732 -> 1792
~ sub_ffffff800001e008 -> sub_ffffff800001e098 : 1556 -> 1604
~ sub_ffffff800001fdec -> sub_ffffff800001feac : 704 -> 708
~ sub_ffffff8000024f68 -> sub_ffffff800002502c : 520 -> 668
~ sub_ffffff80000260d8 -> sub_ffffff8000026230 : 1600 -> 1596
~ sub_ffffff8000026f7c -> sub_ffffff80000270d0 : 2220 -> 2268
~ sub_ffffff800002ebc8 -> sub_ffffff800002ed4c : 24924 -> 24928
~ sub_ffffff8000036740 -> sub_ffffff80000368c8 : 828 -> 836
~ sub_ffffff8000036a7c -> sub_ffffff8000036c0c : 132 -> 140
~ sub_ffffff8000037e08 -> sub_ffffff8000037fa0 : 1704 -> 1716
~ sub_ffffff80000384b0 -> sub_ffffff8000038654 : 5052 -> 5116
~ sub_ffffff800003c3f0 -> sub_ffffff800003c5d4 : 1804 -> 1996
~ sub_ffffff800003d780 -> sub_ffffff800003da24 : 460 -> 400
~ sub_ffffff800003d94c -> sub_ffffff800003dbb4 : 596 -> 732
~ sub_ffffff800003dba0 -> sub_ffffff800003de90 : 364 -> 384
~ sub_ffffff800003dd0c -> sub_ffffff800003e010 : 716 -> 708
~ sub_ffffff800003e1e0 -> sub_ffffff800003e4dc : 6024 -> 6052
~ sub_ffffff8000042320 -> sub_ffffff8000042638 : 748 -> 752
~ sub_ffffff8000042648 -> sub_ffffff8000042964 : 432 -> 436
~ sub_ffffff8000042974 -> sub_ffffff8000042c94 : 1880 -> 1832
~ sub_ffffff8000044fa4 -> sub_ffffff8000045294 : 236 -> 240
~ sub_ffffff800004619c -> sub_ffffff8000046490 : 820 -> 824
~ sub_ffffff8000046da8 -> sub_ffffff80000470a0 : 112 -> 96
~ sub_ffffff8000046e18 -> sub_ffffff8000047100 : 468 -> 452
~ sub_ffffff8000046fec -> sub_ffffff80000472c4 : 748 -> 724
~ sub_ffffff80000472d8 -> sub_ffffff8000047598 : 96 -> 80
~ sub_ffffff8000047338 -> sub_ffffff80000475e8 : 252 -> 248
~ sub_ffffff800004bf2c -> sub_ffffff800004c1d8 : 172 -> 168
~ sub_ffffff800004c438 -> sub_ffffff800004c6e0 : 224 -> 228
~ sub_ffffff800004d104 -> sub_ffffff800004d3b0 : 548 -> 544
~ sub_ffffff800004f4d8 -> sub_ffffff800004f780 : 228 -> 244
~ sub_ffffff800004f694 -> sub_ffffff800004f94c : 168 -> 236
~ sub_ffffff800004f73c -> sub_ffffff800004fa38 : 248 -> 228
~ sub_ffffff800004fb5c -> sub_ffffff800004fe44 : 3204 -> 3200
~ sub_ffffff8000051484 -> sub_ffffff8000051768 : 2360 -> 2384
CStrings:
+ "Jun 29 2026 23:34:52"
- "Jun 16 2026 21:36:11"

```
