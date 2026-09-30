## agx_a000

> `Firmware/agx/armfw_g16g.im4p/agx_a000`

```diff

-  __TEXT.__text: 0x52890
-  __TEXT.__gxf_code: 0x50b0
+  __TEXT.__text: 0x52b08
+  __TEXT.__gxf_code: 0x5080
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
   __TEXT.__const: 0x1d77

   __DATA.__gxf_data: 0x81b0
   __DATA.__data: 0xeb8
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0xb28
+  __DATA.__const: 0xb40
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0x7a278
-  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x78000
+  __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 518
-  Symbols:   188
+  Symbols:   189
   CStrings:  270
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __DATA.__gxf_data : content changed
~ __DATA.__data : content changed
~ __DATA._rtk_mtab : content changed
~ __DATA.__mod_init_func : content changed
Symbols:
+ _gCrashLog
Functions:
~ sub_fffffc0000003350 : 1296 -> 1308
~ sub_fffffc0000003978 -> sub_fffffc0000003984 : 8020 -> 8028
~ sub_fffffc000000b86c -> sub_fffffc000000b880 : 17612 -> 17604
~ sub_fffffc000001ea3c -> sub_fffffc000001ea48 : 1220 -> 1272
~ sub_fffffc00000227b8 -> sub_fffffc00000227f8 : 1068 -> 1104
~ sub_fffffc0000023910 -> sub_fffffc0000023974 : 1544 -> 1596
~ sub_fffffc0000024894 -> sub_fffffc000002492c : 1036 -> 1088
~ sub_fffffc000002e480 -> sub_fffffc000002e54c : 436 -> 468
~ sub_fffffc00000306b4 -> sub_fffffc00000307a0 : 1520 -> 1568
~ sub_fffffc0000037030 -> sub_fffffc000003714c : 896 -> 904
~ sub_fffffc00000373b0 -> sub_fffffc00000374d4 : 132 -> 140
~ sub_fffffc0000038724 -> sub_fffffc0000038850 : 1444 -> 1456
~ sub_fffffc0000038cc8 -> sub_fffffc0000038e00 : 3684 -> 3752
~ sub_fffffc0000039b2c -> sub_fffffc0000039ca8 : 7300 -> 7304
~ sub_fffffc000003b7b0 -> sub_fffffc000003b930 : 1540 -> 1716
~ sub_fffffc000003cd50 -> sub_fffffc000003cf80 : 1452 -> 1392
~ sub_fffffc000003d2fc -> sub_fffffc000003d4f0 : 400 -> 536
~ sub_fffffc000003d48c -> sub_fffffc000003d708 : 364 -> 384
~ sub_fffffc000003d5f8 -> sub_fffffc000003d888 : 792 -> 784
~ sub_fffffc000003db04 -> sub_fffffc000003dd8c : 5264 -> 5292
~ sub_fffffc0000041d20 -> sub_fffffc0000041fc4 : 828 -> 832
~ sub_fffffc0000042934 -> sub_fffffc0000042bdc : 112 -> 96
~ sub_fffffc00000429a4 -> sub_fffffc0000042c3c : 468 -> 452
~ sub_fffffc0000042b78 -> sub_fffffc0000042e00 : 748 -> 724
~ sub_fffffc0000042e64 -> sub_fffffc00000430d4 : 96 -> 80
~ sub_fffffc0000042ec4 -> sub_fffffc0000043124 : 252 -> 248
~ sub_fffffc0000046b9c -> sub_fffffc0000046df8 : 3192 -> 3188
~ sub_fffffc00000480c0 -> sub_fffffc0000048318 : 748 -> 752
~ sub_fffffc00000483e8 -> sub_fffffc0000048644 : 432 -> 436
~ sub_fffffc0000048714 -> sub_fffffc0000048974 : 1880 -> 1832
~ sub_fffffc0000048ffc -> sub_fffffc000004922c : 304 -> 288
~ sub_fffffc000004ae08 -> sub_fffffc000004b028 : 236 -> 240
~ sub_fffffc000004d790 -> sub_fffffc000004d9b4 : 172 -> 168
~ sub_fffffc000004dc94 -> sub_fffffc000004deb4 : 224 -> 228
~ sub_fffffc000004e958 -> sub_fffffc000004eb7c : 548 -> 544
~ sub_fffffc0000050d18 -> sub_fffffc0000050f38 : 228 -> 244
~ sub_fffffc0000050ed4 -> sub_fffffc0000051104 : 168 -> 236
~ sub_fffffc0000050f7c -> sub_fffffc00000511f0 : 248 -> 228
~ sub_fffffc0000051a90 -> sub_fffffc0000051cf0 : 2844 -> 2868
~ sub_fffffc000005274c -> sub_fffffc00000529c4 : 324 -> 332
CStrings:
+ "Jun 29 2026 23:31:42"
- "Jun 16 2026 21:32:37"

```
