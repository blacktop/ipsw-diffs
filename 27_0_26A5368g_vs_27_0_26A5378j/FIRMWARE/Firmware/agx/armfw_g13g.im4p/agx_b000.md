## agx_b000

> `Firmware/agx/armfw_g13g.im4p/agx_b000`

```diff

-  __TEXT.__text: 0x40c00
+  __TEXT.__text: 0x40f28
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
~ sub_ffffff80000088bc -> sub_ffffff80000088c4 : 3380 -> 3372
~ sub_ffffff8000015b5c : 1260 -> 1312
~ sub_ffffff8000018478 -> sub_ffffff80000184ac : 1160 -> 1196
~ sub_ffffff8000019420 -> sub_ffffff8000019478 : 1656 -> 1716
~ sub_ffffff800001a490 -> sub_ffffff800001a524 : 1480 -> 1528
~ sub_ffffff800001c03c -> sub_ffffff800001c100 : 704 -> 708
~ sub_ffffff8000020f28 -> sub_ffffff8000020ff0 : 3736 -> 3740
~ sub_ffffff8000022890 -> sub_ffffff800002295c : 2308 -> 2304
~ sub_ffffff80000232c8 -> sub_ffffff8000023390 : 796 -> 828
~ sub_ffffff80000235e4 -> sub_ffffff80000236cc : 472 -> 620
~ sub_ffffff80000278ec -> sub_ffffff8000027a68 : 828 -> 836
~ sub_ffffff8000027c28 -> sub_ffffff8000027dac : 132 -> 140
~ sub_ffffff80000290d0 -> sub_ffffff800002925c : 1704 -> 1716
~ sub_ffffff8000029778 -> sub_ffffff8000029910 : 5052 -> 5116
~ sub_ffffff800002d5a0 -> sub_ffffff800002d778 : 1800 -> 1992
~ sub_ffffff800002e92c -> sub_ffffff800002ebc4 : 460 -> 400
~ sub_ffffff800002eaf8 -> sub_ffffff800002ed54 : 596 -> 732
~ sub_ffffff800002ed4c -> sub_ffffff800002f030 : 364 -> 384
~ sub_ffffff800002eeb8 -> sub_ffffff800002f1b0 : 692 -> 684
~ sub_ffffff800002f338 -> sub_ffffff800002f628 : 4684 -> 4720
~ sub_ffffff8000032f3c -> sub_ffffff8000033250 : 748 -> 752
~ sub_ffffff8000033264 -> sub_ffffff800003357c : 432 -> 436
~ sub_ffffff8000033590 -> sub_ffffff80000338ac : 1880 -> 1832
~ sub_ffffff8000035aa8 -> sub_ffffff8000035d94 : 236 -> 240
~ sub_ffffff800003b630 -> sub_ffffff800003b920 : 220 -> 228
~ sub_ffffff800003e638 -> sub_ffffff800003e930 : 228 -> 244
~ sub_ffffff800003e7f4 -> sub_ffffff800003eafc : 168 -> 236
~ sub_ffffff800003e89c -> sub_ffffff800003ebe8 : 248 -> 228
~ sub_ffffff800003ecbc -> sub_ffffff800003eff4 : 3200 -> 3196
~ sub_ffffff80000400c0 -> sub_ffffff80000403f4 : 2136 -> 2124
~ sub_ffffff8000040ab8 -> sub_ffffff8000040de0 : 328 -> 336
CStrings:
+ "Jun 29 2026 23:33:42"
- "Jun 16 2026 21:35:08"

```
