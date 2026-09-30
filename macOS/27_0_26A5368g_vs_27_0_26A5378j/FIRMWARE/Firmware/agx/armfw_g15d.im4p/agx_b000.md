## agx_b000

> `Firmware/agx/armfw_g15d.im4p/agx_b000`

```diff

-  __TEXT.__text: 0x53c0c
+  __TEXT.__text: 0x53de4
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
   __DATA.__zerofill: 0xcb9f8
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
~ sub_fffffc000000b13c -> sub_fffffc000000b154 : 19892 -> 19884
~ sub_fffffc000001ea38 -> sub_fffffc000001ea48 : 1292 -> 1344
~ sub_fffffc0000022224 -> sub_fffffc0000022268 : 1068 -> 1104
~ sub_fffffc0000022ec0 -> sub_fffffc0000022f28 : 1612 -> 1672
~ sub_fffffc0000023ebc -> sub_fffffc0000023f60 : 1032 -> 1092
~ sub_fffffc000002d978 -> sub_fffffc000002da58 : 520 -> 668
~ sub_fffffc000002f7e8 -> sub_fffffc000002f95c : 1816 -> 1544
~ sub_fffffc0000035238 -> sub_fffffc000003529c : 544 -> 568
~ sub_fffffc0000038080 -> sub_fffffc00000380fc : 1064 -> 1072
~ sub_fffffc00000384a8 -> sub_fffffc000003852c : 132 -> 140
~ sub_fffffc0000039754 -> sub_fffffc00000397e0 : 1772 -> 1784
~ sub_fffffc0000039e40 -> sub_fffffc0000039ed8 : 3364 -> 3432
~ sub_fffffc000003ab64 -> sub_fffffc000003ac40 : 6864 -> 6868
~ sub_fffffc000003c634 -> sub_fffffc000003c714 : 1684 -> 1860
~ sub_fffffc000003d8d8 -> sub_fffffc000003da68 : 1568 -> 1508
~ sub_fffffc000003def8 -> sub_fffffc000003e04c : 400 -> 536
~ sub_fffffc000003e088 -> sub_fffffc000003e264 : 364 -> 384
~ sub_fffffc000003e1f4 -> sub_fffffc000003e3e4 : 808 -> 800
~ sub_fffffc000003e860 -> sub_fffffc000003ea48 : 6192 -> 6220
~ sub_fffffc0000042da8 -> sub_fffffc0000042fac : 748 -> 752
~ sub_fffffc00000430d0 -> sub_fffffc00000432d8 : 432 -> 436
~ sub_fffffc00000433fc -> sub_fffffc0000043608 : 1880 -> 1832
~ sub_fffffc0000043ce4 -> sub_fffffc0000043ec0 : 304 -> 288
~ sub_fffffc0000045ae4 -> sub_fffffc0000045cb0 : 236 -> 240
~ sub_fffffc0000046cd0 -> sub_fffffc0000046ea0 : 820 -> 824
~ sub_fffffc00000478dc -> sub_fffffc0000047ab0 : 112 -> 96
~ sub_fffffc000004794c -> sub_fffffc0000047b10 : 468 -> 452
~ sub_fffffc0000047b20 -> sub_fffffc0000047cd4 : 748 -> 724
~ sub_fffffc0000047e0c -> sub_fffffc0000047fa8 : 96 -> 80
~ sub_fffffc0000047e6c -> sub_fffffc0000047ff8 : 252 -> 248
~ sub_fffffc000004d450 -> sub_fffffc000004d5d8 : 172 -> 168
~ sub_fffffc000004d95c -> sub_fffffc000004dae0 : 224 -> 228
~ sub_fffffc000004e61c -> sub_fffffc000004e7a4 : 548 -> 544
~ sub_fffffc00000509f4 -> sub_fffffc0000050b78 : 228 -> 244
~ sub_fffffc0000050bb0 -> sub_fffffc0000050d44 : 168 -> 236
~ sub_fffffc0000050c58 -> sub_fffffc0000050e30 : 248 -> 228
~ sub_fffffc000005148c -> sub_fffffc0000051650 : 3192 -> 3188
~ sub_fffffc0000052ef8 -> sub_fffffc00000530b8 : 2608 -> 2632
~ sub_fffffc0000053ac8 -> sub_fffffc0000053ca0 : 332 -> 324
CStrings:
+ "Jun 29 2026 23:37:52"
- "Jun 16 2026 21:39:45"

```
