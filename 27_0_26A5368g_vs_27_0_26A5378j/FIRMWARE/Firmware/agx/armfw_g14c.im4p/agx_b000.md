## agx_b000

> `Firmware/agx/armfw_g14c.im4p/agx_b000`

```diff

-  __TEXT.__text: 0x4e530
+  __TEXT.__text: 0x4e828
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
   __DATA.__zerofill: 0x86738
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
~ sub_ffffff80000038cc -> sub_ffffff80000038d8 : 4964 -> 4988
~ sub_ffffff80000099c8 -> sub_ffffff80000099ec : 4188 -> 4180
~ sub_ffffff8000018c70 -> sub_ffffff8000018c8c : 1292 -> 1344
~ sub_ffffff800001c7a8 -> sub_ffffff800001c7f8 : 948 -> 988
~ sub_ffffff800001d38c -> sub_ffffff800001d404 : 1452 -> 1512
~ sub_ffffff800001e24c -> sub_ffffff800001e300 : 1300 -> 1348
~ sub_ffffff8000025204 -> sub_ffffff80000252e8 : 760 -> 860
~ sub_ffffff8000026f1c -> sub_ffffff8000027064 : 18016 -> 18012
~ sub_ffffff800002beec -> sub_ffffff800002c030 : 3352 -> 3380
~ sub_ffffff8000031f54 -> sub_ffffff80000320b4 : 556 -> 580
~ sub_ffffff80000336ac -> sub_ffffff8000033824 : 956 -> 964
~ sub_ffffff8000033a68 -> sub_ffffff8000033be8 : 132 -> 140
~ sub_ffffff8000034c94 -> sub_ffffff8000034e1c : 1964 -> 1976
~ sub_ffffff8000035440 -> sub_ffffff80000355d4 : 3760 -> 3832
~ sub_ffffff80000362f0 -> sub_ffffff80000364cc : 6380 -> 6384
~ sub_ffffff8000037bdc -> sub_ffffff8000037dbc : 2400 -> 2592
~ sub_ffffff8000039098 -> sub_ffffff8000039338 : 600 -> 540
~ sub_ffffff80000392f0 -> sub_ffffff8000039554 : 400 -> 536
~ sub_ffffff8000039480 -> sub_ffffff800003976c : 364 -> 384
~ sub_ffffff80000395ec -> sub_ffffff80000398ec : 776 -> 768
~ sub_ffffff8000039ba8 -> sub_ffffff8000039ea0 : 6812 -> 6856
~ sub_ffffff800003e124 -> sub_ffffff800003e448 : 748 -> 752
~ sub_ffffff800003e44c -> sub_ffffff800003e774 : 432 -> 436
~ sub_ffffff800003e778 -> sub_ffffff800003eaa4 : 1880 -> 1832
~ sub_ffffff800003f060 -> sub_ffffff800003f35c : 308 -> 292
~ sub_ffffff8000040e70 -> sub_ffffff800004115c : 236 -> 240
~ sub_ffffff800004205c -> sub_ffffff800004234c : 820 -> 824
~ sub_ffffff8000042c68 -> sub_ffffff8000042f5c : 112 -> 96
~ sub_ffffff8000042cd8 -> sub_ffffff8000042fbc : 468 -> 452
~ sub_ffffff8000042eac -> sub_ffffff8000043180 : 748 -> 724
~ sub_ffffff8000043198 -> sub_ffffff8000043454 : 96 -> 80
~ sub_ffffff80000431f8 -> sub_ffffff80000434a4 : 252 -> 248
~ sub_ffffff8000047dec -> sub_ffffff8000048094 : 172 -> 168
~ sub_ffffff80000482f8 -> sub_ffffff800004859c : 224 -> 228
~ sub_ffffff8000048fc0 -> sub_ffffff8000049268 : 548 -> 544
~ sub_ffffff800004b39c -> sub_ffffff800004b640 : 228 -> 244
~ sub_ffffff800004b558 -> sub_ffffff800004b80c : 168 -> 236
~ sub_ffffff800004b600 -> sub_ffffff800004b8f8 : 248 -> 228
~ sub_ffffff800004be38 -> sub_ffffff800004c11c : 3196 -> 3192
~ sub_ffffff800004d8b4 -> sub_ffffff800004db94 : 2452 -> 2476
~ sub_ffffff800004e3e8 -> sub_ffffff800004e6e0 : 328 -> 336
CStrings:
+ "Jun 29 2026 23:35:37"
- "Jun 16 2026 21:36:49"

```
