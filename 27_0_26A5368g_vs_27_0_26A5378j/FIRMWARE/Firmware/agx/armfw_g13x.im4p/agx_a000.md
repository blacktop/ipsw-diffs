## agx_a000

> `Firmware/agx/armfw_g13x.im4p/agx_a000`

```diff

-  __TEXT.__text: 0x445e0
+  __TEXT.__text: 0x4493c
   __TEXT.__gxf_code: 0x1154
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560

   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0xd98
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0x970
+  __DATA.__const: 0x988
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x40

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x53598
-  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x78000
+  __DATA.__zerofill: 0x535b8
+  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 478
-  Symbols:   194
+  Symbols:   195
   CStrings:  229
 
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
~ sub_ffffff8000008830 -> sub_ffffff8000008834 : 3704 -> 3696
~ sub_ffffff80000164dc -> sub_ffffff80000164d8 : 1260 -> 1312
~ sub_ffffff8000018d8c -> sub_ffffff8000018dbc : 1160 -> 1196
~ sub_ffffff8000019ce4 -> sub_ffffff8000019d38 : 1656 -> 1716
~ sub_ffffff800001acd8 -> sub_ffffff800001ad68 : 1480 -> 1528
~ sub_ffffff800001c738 -> sub_ffffff800001c7f8 : 704 -> 708
~ sub_ffffff800002170c -> sub_ffffff80000217d0 : 3648 -> 3652
~ sub_ffffff8000023750 -> sub_ffffff8000023818 : 2312 -> 2308
~ sub_ffffff8000024194 -> sub_ffffff8000024258 : 2224 -> 2312
~ sub_ffffff8000024a44 -> sub_ffffff8000024b60 : 472 -> 620
~ sub_ffffff8000029cec -> sub_ffffff8000029e9c : 896 -> 904
~ sub_ffffff800002a06c -> sub_ffffff800002a224 : 132 -> 140
~ sub_ffffff800002b1b4 -> sub_ffffff800002b374 : 1652 -> 1664
~ sub_ffffff800002b828 -> sub_ffffff800002b9f4 : 5052 -> 5116
~ sub_ffffff800002f73c -> sub_ffffff800002f948 : 1804 -> 1996
~ sub_ffffff8000030acc -> sub_ffffff8000030d98 : 460 -> 400
~ sub_ffffff8000030c98 -> sub_ffffff8000030f28 : 596 -> 732
~ sub_ffffff8000030eec -> sub_ffffff8000031204 : 364 -> 384
~ sub_ffffff8000031058 -> sub_ffffff8000031384 : 700 -> 692
~ sub_ffffff8000031524 -> sub_ffffff8000031848 : 4088 -> 4124
~ sub_ffffff8000034fb4 -> sub_ffffff80000352fc : 748 -> 752
~ sub_ffffff80000352dc -> sub_ffffff8000035628 : 432 -> 436
~ sub_ffffff8000035608 -> sub_ffffff8000035958 : 1880 -> 1832
~ sub_ffffff8000037c84 -> sub_ffffff8000037fa4 : 236 -> 240
~ sub_ffffff800003e3d4 -> sub_ffffff800003e6f8 : 220 -> 228
~ sub_ffffff8000041474 -> sub_ffffff80000417a0 : 228 -> 244
~ sub_ffffff8000041630 -> sub_ffffff800004196c : 168 -> 236
~ sub_ffffff80000416d8 -> sub_ffffff8000041a58 : 248 -> 228
~ sub_ffffff8000041f10 -> sub_ffffff800004227c : 3192 -> 3188
~ sub_ffffff8000043980 -> sub_ffffff8000043ce8 : 2424 -> 2412
~ sub_ffffff8000044498 -> sub_ffffff80000447f4 : 328 -> 336
CStrings:
+ "Jun 29 2026 23:30:27"
- "Jun 16 2026 21:31:09"

```
