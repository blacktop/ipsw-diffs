## agx_c000

> `Firmware/agx/armfw_g15g.im4p/agx_c000`

```diff

-  __TEXT.__text: 0x5463c
+  __TEXT.__text: 0x5493c
   __TEXT.__gxf_code: 0x10cc
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560

   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0xe10
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0x9d8
+  __DATA.__const: 0x9f0
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0x697d8
-  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x78000
+  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 502
-  Symbols:   196
+  Symbols:   197
   CStrings:  264
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __DATA.__data : content changed
~ __DATA._rtk_mtab : content changed
~ __DATA.__mod_init_func : content changed
Symbols:
+ _gCrashLog
Functions:
~ sub_fffffc0000003350 : 936 -> 944
~ sub_fffffc0000003814 -> sub_fffffc000000381c : 7644 -> 7660
~ sub_fffffc000000b56c -> sub_fffffc000000b584 : 17812 -> 17804
~ sub_fffffc000001e9bc -> sub_fffffc000001e9cc : 1220 -> 1272
~ sub_fffffc00000223c4 -> sub_fffffc0000022408 : 1068 -> 1104
~ sub_fffffc0000023028 -> sub_fffffc0000023090 : 1544 -> 1596
~ sub_fffffc0000023fac -> sub_fffffc0000024048 : 964 -> 1016
~ sub_fffffc000002cce4 -> sub_fffffc000002cdb4 : 520 -> 668
~ sub_fffffc000002d830 -> sub_fffffc000002d994 : 17328 -> 17324
~ sub_fffffc0000032b4c -> sub_fffffc0000032cac : 2596 -> 2648
~ sub_fffffc0000039ab4 -> sub_fffffc0000039c48 : 932 -> 940
~ sub_fffffc0000039e58 -> sub_fffffc0000039ff4 : 132 -> 140
~ sub_fffffc000003b1ac -> sub_fffffc000003b350 : 1468 -> 1480
~ sub_fffffc000003b768 -> sub_fffffc000003b918 : 3684 -> 3752
~ sub_fffffc000003c5cc -> sub_fffffc000003c7c0 : 7664 -> 7668
~ sub_fffffc000003e3bc -> sub_fffffc000003e5b4 : 1540 -> 1716
~ sub_fffffc000003f958 -> sub_fffffc000003fc00 : 1452 -> 1392
~ sub_fffffc000003ff04 -> sub_fffffc0000040170 : 400 -> 536
~ sub_fffffc0000040094 -> sub_fffffc0000040388 : 364 -> 384
~ sub_fffffc0000040200 -> sub_fffffc0000040508 : 800 -> 792
~ sub_fffffc0000040714 -> sub_fffffc0000040a14 : 5308 -> 5336
~ sub_fffffc00000448c0 -> sub_fffffc0000044bdc : 748 -> 752
~ sub_fffffc0000044be8 -> sub_fffffc0000044f08 : 432 -> 436
~ sub_fffffc0000044f14 -> sub_fffffc0000045238 : 1880 -> 1832
~ sub_fffffc0000047544 -> sub_fffffc0000047838 : 236 -> 240
~ sub_fffffc000004873c -> sub_fffffc0000048a34 : 820 -> 824
~ sub_fffffc0000049348 -> sub_fffffc0000049644 : 112 -> 96
~ sub_fffffc00000493b8 -> sub_fffffc00000496a4 : 468 -> 452
~ sub_fffffc000004958c -> sub_fffffc0000049868 : 748 -> 724
~ sub_fffffc0000049878 -> sub_fffffc0000049b3c : 96 -> 80
~ sub_fffffc00000498d8 -> sub_fffffc0000049b8c : 252 -> 248
~ sub_fffffc000004e4cc -> sub_fffffc000004e77c : 172 -> 168
~ sub_fffffc000004e9d8 -> sub_fffffc000004ec84 : 224 -> 228
~ sub_fffffc000004f6a4 -> sub_fffffc000004f954 : 548 -> 544
~ sub_fffffc0000051a78 -> sub_fffffc0000051d24 : 228 -> 244
~ sub_fffffc0000051c34 -> sub_fffffc0000051ef0 : 168 -> 236
~ sub_fffffc0000051cdc -> sub_fffffc0000051fdc : 248 -> 228
~ sub_fffffc00000520fc -> sub_fffffc00000523e8 : 3204 -> 3200
~ sub_fffffc00000538b8 -> sub_fffffc0000053ba0 : 2716 -> 2740
CStrings:
+ "Jun 29 2026 23:39:35"
- "Jun 16 2026 21:41:36"

```
