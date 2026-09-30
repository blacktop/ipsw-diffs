## agx_a000

> `Firmware/agx/armfw_g14d.im4p/agx_a000`

```diff

-  __TEXT.__text: 0x4f100
+  __TEXT.__text: 0x4f3f8
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
   __DATA.__zerofill: 0x86978
-  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x78000
+  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 511
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
~ sub_ffffff8000003434 : 952 -> 964
~ sub_ffffff80000039cc -> sub_ffffff80000039d8 : 4964 -> 4988
~ sub_ffffff8000009e70 -> sub_ffffff8000009e94 : 4256 -> 4248
~ sub_ffffff80000192cc -> sub_ffffff80000192e8 : 1292 -> 1344
~ sub_ffffff800001ce04 -> sub_ffffff800001ce54 : 948 -> 988
~ sub_ffffff800001d9f4 -> sub_ffffff800001da6c : 1452 -> 1512
~ sub_ffffff800001e8c4 -> sub_ffffff800001e978 : 1300 -> 1348
~ sub_ffffff80000258c0 -> sub_ffffff80000259a4 : 760 -> 860
~ sub_ffffff8000027620 -> sub_ffffff8000027768 : 18016 -> 18012
~ sub_ffffff800002c5f0 -> sub_ffffff800002c734 : 3352 -> 3380
~ sub_ffffff800003279c -> sub_ffffff80000328fc : 648 -> 672
~ sub_ffffff80000340ec -> sub_ffffff8000034264 : 956 -> 964
~ sub_ffffff80000344a8 -> sub_ffffff8000034628 : 132 -> 140
~ sub_ffffff80000357a8 -> sub_ffffff8000035930 : 1964 -> 1976
~ sub_ffffff8000035f54 -> sub_ffffff80000360e8 : 3760 -> 3832
~ sub_ffffff8000036e04 -> sub_ffffff8000036fe0 : 6380 -> 6384
~ sub_ffffff80000386f0 -> sub_ffffff80000388d0 : 2400 -> 2592
~ sub_ffffff8000039bc0 -> sub_ffffff8000039e60 : 600 -> 540
~ sub_ffffff8000039e18 -> sub_ffffff800003a07c : 400 -> 536
~ sub_ffffff8000039fa8 -> sub_ffffff800003a294 : 364 -> 384
~ sub_ffffff800003a114 -> sub_ffffff800003a414 : 776 -> 768
~ sub_ffffff800003a6d0 -> sub_ffffff800003a9c8 : 6980 -> 7024
~ sub_ffffff800003ecf4 -> sub_ffffff800003f018 : 748 -> 752
~ sub_ffffff800003f01c -> sub_ffffff800003f344 : 432 -> 436
~ sub_ffffff800003f348 -> sub_ffffff800003f674 : 1880 -> 1832
~ sub_ffffff800003fc30 -> sub_ffffff800003ff2c : 308 -> 292
~ sub_ffffff8000041a40 -> sub_ffffff8000041d2c : 236 -> 240
~ sub_ffffff8000042c2c -> sub_ffffff8000042f1c : 820 -> 824
~ sub_ffffff8000043838 -> sub_ffffff8000043b2c : 112 -> 96
~ sub_ffffff80000438a8 -> sub_ffffff8000043b8c : 468 -> 452
~ sub_ffffff8000043a7c -> sub_ffffff8000043d50 : 748 -> 724
~ sub_ffffff8000043d68 -> sub_ffffff8000044024 : 96 -> 80
~ sub_ffffff8000043dc8 -> sub_ffffff8000044074 : 252 -> 248
~ sub_ffffff80000489bc -> sub_ffffff8000048c64 : 172 -> 168
~ sub_ffffff8000048ec8 -> sub_ffffff800004916c : 224 -> 228
~ sub_ffffff8000049b90 -> sub_ffffff8000049e38 : 548 -> 544
~ sub_ffffff800004bf6c -> sub_ffffff800004c210 : 228 -> 244
~ sub_ffffff800004c128 -> sub_ffffff800004c3dc : 168 -> 236
~ sub_ffffff800004c1d0 -> sub_ffffff800004c4c8 : 248 -> 228
~ sub_ffffff800004ca08 -> sub_ffffff800004ccec : 3196 -> 3192
~ sub_ffffff800004e484 -> sub_ffffff800004e764 : 2452 -> 2476
~ sub_ffffff800004efb8 -> sub_ffffff800004f2b0 : 328 -> 336
CStrings:
+ "Jun 29 2026 23:31:27"
- "Jun 16 2026 21:32:19"

```
