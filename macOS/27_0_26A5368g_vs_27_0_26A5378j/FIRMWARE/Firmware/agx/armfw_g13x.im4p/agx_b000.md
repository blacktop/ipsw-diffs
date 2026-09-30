## agx_b000

> `Firmware/agx/armfw_g13x.im4p/agx_b000`

```diff

-  __TEXT.__text: 0x4453c
+  __TEXT.__text: 0x44898
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
~ sub_ffffff80000088d8 -> sub_ffffff80000088dc : 3648 -> 3640
~ sub_ffffff8000016438 -> sub_ffffff8000016434 : 1260 -> 1312
~ sub_ffffff8000018ce8 -> sub_ffffff8000018d18 : 1160 -> 1196
~ sub_ffffff8000019c40 -> sub_ffffff8000019c94 : 1656 -> 1716
~ sub_ffffff800001ac34 -> sub_ffffff800001acc4 : 1480 -> 1528
~ sub_ffffff800001c694 -> sub_ffffff800001c754 : 704 -> 708
~ sub_ffffff8000021668 -> sub_ffffff800002172c : 3648 -> 3652
~ sub_ffffff80000236ac -> sub_ffffff8000023774 : 2312 -> 2308
~ sub_ffffff80000240f0 -> sub_ffffff80000241b4 : 2224 -> 2312
~ sub_ffffff80000249a0 -> sub_ffffff8000024abc : 472 -> 620
~ sub_ffffff8000029c48 -> sub_ffffff8000029df8 : 896 -> 904
~ sub_ffffff8000029fc8 -> sub_ffffff800002a180 : 132 -> 140
~ sub_ffffff800002b110 -> sub_ffffff800002b2d0 : 1652 -> 1664
~ sub_ffffff800002b784 -> sub_ffffff800002b950 : 5052 -> 5116
~ sub_ffffff800002f698 -> sub_ffffff800002f8a4 : 1804 -> 1996
~ sub_ffffff8000030a28 -> sub_ffffff8000030cf4 : 460 -> 400
~ sub_ffffff8000030bf4 -> sub_ffffff8000030e84 : 596 -> 732
~ sub_ffffff8000030e48 -> sub_ffffff8000031160 : 364 -> 384
~ sub_ffffff8000030fb4 -> sub_ffffff80000312e0 : 700 -> 692
~ sub_ffffff8000031480 -> sub_ffffff80000317a4 : 4088 -> 4124
~ sub_ffffff8000034f10 -> sub_ffffff8000035258 : 748 -> 752
~ sub_ffffff8000035238 -> sub_ffffff8000035584 : 432 -> 436
~ sub_ffffff8000035564 -> sub_ffffff80000358b4 : 1880 -> 1832
~ sub_ffffff8000037be0 -> sub_ffffff8000037f00 : 236 -> 240
~ sub_ffffff800003e330 -> sub_ffffff800003e654 : 220 -> 228
~ sub_ffffff80000413d0 -> sub_ffffff80000416fc : 228 -> 244
~ sub_ffffff800004158c -> sub_ffffff80000418c8 : 168 -> 236
~ sub_ffffff8000041634 -> sub_ffffff80000419b4 : 248 -> 228
~ sub_ffffff8000041e6c -> sub_ffffff80000421d8 : 3192 -> 3188
~ sub_ffffff80000438dc -> sub_ffffff8000043c44 : 2424 -> 2412
CStrings:
+ "Jun 29 2026 23:33:34"
- "Jun 16 2026 21:35:28"

```
