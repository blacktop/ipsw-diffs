## agx_b000

> `Firmware/agx/armfw_g14s.im4p/agx_b000`

```diff

-  __TEXT.__text: 0x4e17c
+  __TEXT.__text: 0x4e470
   __TEXT.__gxf_code: 0x10cc
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560

   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0xe80
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0xa98
+  __DATA.__const: 0xab0
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x40

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0x86638
-  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x78000
+  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 509
-  Symbols:   195
+  Symbols:   196
   CStrings:  247
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __DATA.__data : content changed
~ __DATA._rtk_mtab : content changed
~ __DATA.__mod_init_func : content changed
Symbols:
+ _gCrashLog
Functions:
~ sub_ffffff8000003350 : 924 -> 936
~ sub_ffffff80000038cc -> sub_ffffff80000038d8 : 4964 -> 4984
~ sub_ffffff8000009770 -> sub_ffffff8000009790 : 4204 -> 4196
~ sub_ffffff8000018a28 -> sub_ffffff8000018a40 : 1292 -> 1344
~ sub_ffffff800001c560 -> sub_ffffff800001c5ac : 948 -> 988
~ sub_ffffff800001d144 -> sub_ffffff800001d1b8 : 1452 -> 1512
~ sub_ffffff800001e004 -> sub_ffffff800001e0b4 : 1300 -> 1348
~ sub_ffffff8000024fbc -> sub_ffffff800002509c : 760 -> 860
~ sub_ffffff8000026bfc -> sub_ffffff8000026d40 : 18016 -> 18012
~ sub_ffffff800002bbcc -> sub_ffffff800002bd0c : 3352 -> 3380
~ sub_ffffff8000031bb8 -> sub_ffffff8000031d14 : 556 -> 580
~ sub_ffffff8000033310 -> sub_ffffff8000033484 : 956 -> 964
~ sub_ffffff80000336cc -> sub_ffffff8000033848 : 132 -> 140
~ sub_ffffff80000348dc -> sub_ffffff8000034a60 : 1964 -> 1976
~ sub_ffffff8000035088 -> sub_ffffff8000035218 : 3760 -> 3832
~ sub_ffffff8000035f38 -> sub_ffffff8000036110 : 6380 -> 6384
~ sub_ffffff8000037824 -> sub_ffffff8000037a00 : 2400 -> 2592
~ sub_ffffff8000038ce0 -> sub_ffffff8000038f7c : 600 -> 540
~ sub_ffffff8000038f38 -> sub_ffffff8000039198 : 400 -> 536
~ sub_ffffff80000390c8 -> sub_ffffff80000393b0 : 364 -> 384
~ sub_ffffff8000039234 -> sub_ffffff8000039530 : 776 -> 768
~ sub_ffffff80000397f0 -> sub_ffffff8000039ae4 : 6816 -> 6860
~ sub_ffffff800003dd70 -> sub_ffffff800003e090 : 748 -> 752
~ sub_ffffff800003e098 -> sub_ffffff800003e3bc : 432 -> 436
~ sub_ffffff800003e3c4 -> sub_ffffff800003e6ec : 1880 -> 1832
~ sub_ffffff800003ecac -> sub_ffffff800003efa4 : 308 -> 292
~ sub_ffffff8000040abc -> sub_ffffff8000040da4 : 236 -> 240
~ sub_ffffff8000041ca8 -> sub_ffffff8000041f94 : 820 -> 824
~ sub_ffffff80000428b4 -> sub_ffffff8000042ba4 : 112 -> 96
~ sub_ffffff8000042924 -> sub_ffffff8000042c04 : 468 -> 452
~ sub_ffffff8000042af8 -> sub_ffffff8000042dc8 : 748 -> 724
~ sub_ffffff8000042de4 -> sub_ffffff800004309c : 96 -> 80
~ sub_ffffff8000042e44 -> sub_ffffff80000430ec : 252 -> 248
~ sub_ffffff8000047a38 -> sub_ffffff8000047cdc : 172 -> 168
~ sub_ffffff8000047f44 -> sub_ffffff80000481e4 : 224 -> 228
~ sub_ffffff8000048c0c -> sub_ffffff8000048eb0 : 548 -> 544
~ sub_ffffff800004afe8 -> sub_ffffff800004b288 : 228 -> 244
~ sub_ffffff800004b1a4 -> sub_ffffff800004b454 : 168 -> 236
~ sub_ffffff800004b24c -> sub_ffffff800004b540 : 248 -> 228
~ sub_ffffff800004ba84 -> sub_ffffff800004bd64 : 3196 -> 3192
~ sub_ffffff800004d500 -> sub_ffffff800004d7dc : 2452 -> 2476
~ sub_ffffff800004e034 -> sub_ffffff800004e328 : 336 -> 328
CStrings:
+ "Jun 29 2026 23:35:57"
- "Jun 16 2026 21:36:51"

```
