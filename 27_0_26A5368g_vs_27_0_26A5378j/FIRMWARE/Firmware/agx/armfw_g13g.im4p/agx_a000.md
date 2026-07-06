## agx_a000

> `Firmware/agx/armfw_g13g.im4p/agx_a000`

```diff

-  __TEXT.__text: 0x40b90
+  __TEXT.__text: 0x40eb8
   __TEXT.__gxf_code: 0x1154
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560

   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0xc60
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0x900
+  __DATA.__const: 0x918
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x40

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x52db8
-  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x78000
+  __DATA.__zerofill: 0x52dd8
+  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 426
-  Symbols:   193
+  Symbols:   194
   CStrings:  206
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __DATA.__data : content changed
~ __DATA._rtk_mtab : content changed
Symbols:
+ _gCrashLog
Functions:
~ sub_ffffff8000003350 : 768 -> 776
~ sub_ffffff80000088bc -> sub_ffffff80000088c4 : 3292 -> 3284
~ sub_ffffff8000015b04 : 1260 -> 1312
~ sub_ffffff8000018420 -> sub_ffffff8000018454 : 1160 -> 1196
~ sub_ffffff80000193c8 -> sub_ffffff8000019420 : 1656 -> 1716
~ sub_ffffff800001a438 -> sub_ffffff800001a4cc : 1480 -> 1528
~ sub_ffffff800001bfe4 -> sub_ffffff800001c0a8 : 704 -> 708
~ sub_ffffff8000020ed0 -> sub_ffffff8000020f98 : 3712 -> 3716
~ sub_ffffff8000022820 -> sub_ffffff80000228ec : 2308 -> 2304
~ sub_ffffff8000023258 -> sub_ffffff8000023320 : 796 -> 828
~ sub_ffffff8000023574 -> sub_ffffff800002365c : 472 -> 620
~ sub_ffffff800002787c -> sub_ffffff80000279f8 : 828 -> 836
~ sub_ffffff8000027bb8 -> sub_ffffff8000027d3c : 132 -> 140
~ sub_ffffff8000029060 -> sub_ffffff80000291ec : 1704 -> 1716
~ sub_ffffff8000029708 -> sub_ffffff80000298a0 : 5052 -> 5116
~ sub_ffffff800002d530 -> sub_ffffff800002d708 : 1800 -> 1992
~ sub_ffffff800002e8bc -> sub_ffffff800002eb54 : 460 -> 400
~ sub_ffffff800002ea88 -> sub_ffffff800002ece4 : 596 -> 732
~ sub_ffffff800002ecdc -> sub_ffffff800002efc0 : 364 -> 384
~ sub_ffffff800002ee48 -> sub_ffffff800002f140 : 692 -> 684
~ sub_ffffff800002f2c8 -> sub_ffffff800002f5b8 : 4684 -> 4720
~ sub_ffffff8000032ecc -> sub_ffffff80000331e0 : 748 -> 752
~ sub_ffffff80000331f4 -> sub_ffffff800003350c : 432 -> 436
~ sub_ffffff8000033520 -> sub_ffffff800003383c : 1880 -> 1832
~ sub_ffffff8000035a38 -> sub_ffffff8000035d24 : 236 -> 240
~ sub_ffffff800003b5c0 -> sub_ffffff800003b8b0 : 220 -> 228
~ sub_ffffff800003e5c8 -> sub_ffffff800003e8c0 : 228 -> 244
~ sub_ffffff800003e784 -> sub_ffffff800003ea8c : 168 -> 236
~ sub_ffffff800003e82c -> sub_ffffff800003eb78 : 248 -> 228
~ sub_ffffff800003ec4c -> sub_ffffff800003ef84 : 3200 -> 3196
~ sub_ffffff8000040050 -> sub_ffffff8000040384 : 2136 -> 2124
~ sub_ffffff8000040a48 -> sub_ffffff8000040d70 : 328 -> 336
CStrings:
+ "Jun 29 2026 23:30:22"
- "Jun 16 2026 21:31:04"

```
