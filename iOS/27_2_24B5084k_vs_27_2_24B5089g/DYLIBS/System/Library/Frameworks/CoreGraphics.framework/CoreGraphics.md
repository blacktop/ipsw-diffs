## CoreGraphics

> `/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics`

```diff

-2050.1.4.0.0
-  __TEXT.__text: 0x55cd50
+2050.1.5.0.0
+  __TEXT.__text: 0x55dd98
   __TEXT.__resolver_help: 0xd8
   __TEXT.__delay_helper: 0x1f4
   __TEXT.__objc_methlist: 0x42a0
-  __TEXT.__const: 0x1e0020
+  __TEXT.__const: 0x1dffa0
   __TEXT.__cstring: 0x4393f
   __TEXT.__dlopen_cstrs: 0xd5
   __TEXT.__constg_swiftt: 0x1918

   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__auth_got: 0x26b0
   __AUTH.__objc_data: 0x17c0
-  __AUTH.__data: 0x330
+  __AUTH.__data: 0x298
   __DATA.__objc_ivar: 0x594
   __DATA.__data: 0x1b0c
   __DATA.__common: 0x245
   __DATA_DIRTY.__la_resolver: 0x10
-  __DATA_DIRTY.__data: 0xfb8
+  __DATA_DIRTY.__data: 0x1050
   __DATA_DIRTY.__crash_info: 0x148
-  __DATA_DIRTY.__bss: 0x2748
+  __DATA_DIRTY.__bss: 0x2770
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
Functions:
~ _ripc_AcquireRIPImageData : 1816 -> 1748
~ _img_data_lock : 10012 -> 10028
~ _initialize_skipping_conditional_var : 272 -> 276
~ _RIPLayerBltImage : 1172 -> 1188
~ __blt_image_initialize : 1980 -> 1992
~ _argb32_sample_argb32 : 1688 -> 1680
~ __ZL18A8_sample_A8_innerPK6_ImgOplli : 1640 -> 1636
~ _A8_sample_ALPHA8 : 1844 -> 1864
~ _ripc_EndLayer : 1320 -> 1264
~ _GRAYA8_sample_GRAYA8 : 2108 -> 2116
~ _build_tile : 4140 -> 4148
~ __ZL26RGBAf16_sample_RGBAf_innerPK6_ImgOplli : 1836 -> 1832
~ _rgba64_sample_CMYK64 : 2248 -> 2288
~ _rgba64_sample_rgb48 : 1308 -> 1328
~ _rgba64_sample_w16 : 1604 -> 1644
~ _rgb555_sample_W8 : 1588 -> 1628
~ _rgb555_sample_RGB555 : 2108 -> 2104
~ _rgb555_sample_rgb555 : 2124 -> 2136
~ _rgb555_sample_RGB24 : 1444 -> 1464
~ _rgb555_sample_RGBA32 : 1276 -> 1296
~ _rgb555_sample_rgba32 : 1252 -> 1272
~ _rgb555_sample_ARGB32 : 1268 -> 1288
~ _rgb555_sample_argb32 : 1244 -> 1264
~ _rgb555_sample_CMYK32 : 1716 -> 1760
~ _rgb555_sample_cmyk32 : 1688 -> 1732
~ _rips_DrawDisplayList : 2660 -> 2604
~ _Wf_sample_W8 : 1632 -> 1672
~ _Wf_sample_W16 : 1744 -> 1784
~ _Wf_sample_w16 : 1660 -> 1700
~ __ZL18Wf_sample_WF_innerPK6_ImgOplli : 2032 -> 2020
~ __ZL18Wf_sample_Wf_innerPK6_ImgOplli : 1908 -> 1924
~ _Wf_sample_RGBF : 1348 -> 1368
~ _Wf_sample_RGBf : 1272 -> 1292
~ _Wf_sample_RGBAF : 1424 -> 1444
~ _Wf_sample_RGBAf : 1328 -> 1348
~ _Wf_sample_CMYKF : 1600 -> 1640
~ _Wf_sample_CMYKf : 1536 -> 1576
~ _cmyk32_sample_W8 : 1616 -> 1656
~ _cmyk32_sample_RGB555 : 1732 -> 1776
~ _cmyk32_sample_rgb555 : 1676 -> 1720
~ _cmyk32_sample_RGB24 : 1448 -> 1468
~ _cmyk32_sample_RGBA32 : 1312 -> 1332
~ _cmyk32_sample_rgba32 : 1288 -> 1308
~ _cmyk32_sample_ARGB32 : 1380 -> 1400
~ _cmyk32_sample_argb32 : 1368 -> 1388
~ _cmyk32_sample_CMYK32 : 2048 -> 2056
~ _cmyk32_sample_cmyk32 : 2100 -> 2116
~ _cmyk32_sample_CMYK64 : 2228 -> 2268
~ _cmyk32_sample_cmyk64 : 1776 -> 1816
~ _cmyk32_sample_CMYKF : 1684 -> 1716
~ _cmyk32_sample_CMYKf : 1620 -> 1652
~ _RGBAf_sample_RGB24 : 1436 -> 1456
~ _RGBAf_sample_RGBA32 : 1304 -> 1324
~ _RGBAf_sample_rgba32 : 1292 -> 1312
~ _RGBAf_sample_ARGB32 : 1304 -> 1316
~ _RGBAf_sample_argb32 : 1280 -> 1292
~ _RGBAf_sample_RGB48 : 1644 -> 1664
~ _RGBAf_sample_rgb48 : 1448 -> 1468
~ _RGBAf_sample_RGBA64 : 1744 -> 1768
~ _RGBAf_sample_rgba64 : 1368 -> 1392
~ _RGBAf_sample_WF : 1532 -> 1568
~ _RGBAf_sample_Wf : 1444 -> 1480
~ _RGBAf_sample_RGBF : 1312 -> 1320
~ _RGBAf_sample_RGBf : 1244 -> 1264
~ __ZL24RGBAf_sample_RGBAF_innerPK6_ImgOplli : 1824 -> 1832
~ __ZL24RGBAf_sample_RGBAf_innerPK6_ImgOplli : 1700 -> 1708
~ _RGBAf_sample_CMYKF : 1648 -> 1700
~ _RGBAf_sample_CMYKf : 1560 -> 1612
~ __ZL26GRAYA8_sample_RGBA32_innerPK6_ImgOplli : 2508 -> 2548
~ __ZL22GRAYA8_sample_W8_innerPK6_ImgOplli : 1720 -> 1760
~ _GRAYA8_sample_RGB24 : 1684 -> 1696
~ __ZL26GRAYA8_sample_CMYK32_innerPK6_ImgOplli : 2372 -> 2412
~ _CMYKf16_sample_Wf16 : 1792 -> 1832
~ __ZL25CMYKf16_sample_RGBf_innerPK6_ImgOplli : 4808 -> 4884
~ __ZL26CMYKf16_sample_RGBAf_innerPK6_ImgOplli : 5704 -> 5780
~ __ZL26CMYKf16_sample_CMYKf_innerPK6_ImgOplli : 2352 -> 2288
~ _w16_sample_W8 : 1600 -> 1640
~ _w16_sample_W16 : 2128 -> 2204
~ _w16_sample_w16 : 2068 -> 2140
~ _w16_sample_RGB48 : 1504 -> 1524
~ _w16_sample_rgb48 : 1308 -> 1328
~ _w16_sample_RGBA64 : 1664 -> 1684
~ _w16_sample_rgba64 : 1252 -> 1272
~ _w16_sample_CMYK64 : 2280 -> 2320
~ _w16_sample_cmyk64 : 1836 -> 1876
~ _w16_sample_WF : 1596 -> 1636
~ _w16_sample_Wf : 1516 -> 1556
~ _cmyk64_sample_CMYK32 : 1680 -> 1700
~ _cmyk64_sample_cmyk32 : 1652 -> 1672
~ _cmyk64_sample_W16 : 1708 -> 1748
~ _cmyk64_sample_w16 : 1624 -> 1664
~ _cmyk64_sample_RGB48 : 1564 -> 1584
~ _cmyk64_sample_rgb48 : 1368 -> 1388
~ _cmyk64_sample_RGBA64 : 1692 -> 1732
~ _cmyk64_sample_rgba64 : 1288 -> 1312
~ _cmyk64_sample_CMYK64 : 2644 -> 2664
~ _cmyk64_sample_cmyk64 : 2176 -> 2216
~ _cmyk64_sample_CMYKF : 1684 -> 1716
~ _cmyk64_sample_CMYKf : 1620 -> 1652
~ _argb32_sample_W8 : 1600 -> 1640
~ _argb32_sample_RGB555 : 1672 -> 1712
~ _argb32_sample_rgb555 : 1616 -> 1656
~ _argb32_sample_RGB24 : 1384 -> 1412
~ _argb32_sample_RGBA32 : 1272 -> 1292
~ _argb32_sample_rgba32 : 1248 -> 1268
~ _argb32_sample_ARGB32 : 1716 -> 1708
~ _argb32_sample_CMYK32 : 1716 -> 1760
~ _argb32_sample_cmyk32 : 1688 -> 1732
~ _argb32_sample_RGB48 : 1504 -> 1524
~ _argb32_sample_rgb48 : 1308 -> 1328
~ _argb32_sample_RGBA64 : 1664 -> 1684
~ _argb32_sample_rgba64 : 1240 -> 1264
~ _argb32_sample_RGBF : 1428 -> 1432
~ _argb32_sample_RGBf : 1360 -> 1364
~ _argb32_sample_RGBAF : 1528 -> 1548
~ _argb32_sample_RGBAf : 1416 -> 1436
~ _rgba64_sample_RGB24 : 1424 -> 1444
~ _rgba64_sample_RGBA32 : 1288 -> 1308
~ _rgba64_sample_rgba32 : 1264 -> 1284
~ _rgba64_sample_ARGB32 : 1288 -> 1312
~ _rgba64_sample_argb32 : 1264 -> 1288
~ _rgba64_sample_W16 : 1696 -> 1736
~ _rgba64_sample_RGB48 : 1496 -> 1516
~ _rgba64_sample_RGBA64 : 2080 -> 2076
~ _rgba64_sample_rgba64 : 1688 -> 1680
~ _rgba64_sample_cmyk64 : 1796 -> 1836
~ _rgba64_sample_RGBF : 1428 -> 1432
~ _rgba64_sample_RGBf : 1360 -> 1364
~ _rgba64_sample_RGBAF : 1528 -> 1548
~ _rgba64_sample_RGBAf : 1416 -> 1436
~ _W8_sample_W8 : 2104 -> 2120
~ _W8_sample_RGB555 : 1676 -> 1716
~ _W8_sample_rgb555 : 1620 -> 1660
~ _W8_sample_RGB24 : 1396 -> 1416
~ _W8_sample_RGBA32 : 1268 -> 1292
~ _W8_sample_rgba32 : 1244 -> 1268
~ _W8_sample_ARGB32 : 1272 -> 1292
~ _W8_sample_argb32 : 1248 -> 1268
~ _W8_sample_CMYK32 : 1716 -> 1760
~ _W8_sample_cmyk32 : 1688 -> 1732
~ _W8_sample_W16 : 1668 -> 1708
~ _W8_sample_w16 : 1584 -> 1624
~ _W8_sample_WF : 1580 -> 1620
~ _W8_sample_Wf : 1496 -> 1536
~ _rips_cm_Draw : 1228 -> 1168
~ _RIPLayerConvertLayer : 540 -> 476
~ _rips_gb_Draw : 1440 -> 1344
~ _CMYKf_sample_CMYK32 : 1720 -> 1760
~ _CMYKf_sample_cmyk32 : 1692 -> 1732
~ _CMYKf_sample_CMYK64 : 2324 -> 2364
~ _CMYKf_sample_cmyk64 : 1900 -> 1940
~ _CMYKf_sample_WF : 1548 -> 1584
~ _CMYKf_sample_Wf : 1452 -> 1484
~ _CMYKf_sample_RGBF : 1324 -> 1344
~ _CMYKf_sample_RGBf : 1260 -> 1280
~ _CMYKf_sample_RGBAF : 1400 -> 1420
~ _CMYKf_sample_RGBAf : 1304 -> 1324
~ __ZL24CMYKf_sample_CMYKf_innerPK6_ImgOplli : 1948 -> 1944
~ _A8_sample_ALPHA16 : 1908 -> 1920
~ _A8_sample_alpha16 : 1852 -> 1872
~ _A8_sample_ALPHAF : 1784 -> 1800
~ _A8_sample_ALPHAf : 1728 -> 1744
~ _A8_sample_ALPHAf16 : 1768 -> 1784
~ _rgba32_sample_W8 : 1616 -> 1656
~ _rgba32_sample_RGB555 : 1668 -> 1708
~ _rgba32_sample_rgb555 : 1612 -> 1652
~ _rgba32_sample_RGB24 : 1384 -> 1404
~ _rgba32_sample_RGBA32 : 1716 -> 1704
~ _rgba32_sample_rgba32 : 1688 -> 1676
~ _rgba32_sample_ARGB32 : 1276 -> 1296
~ _rgba32_sample_argb32 : 1252 -> 1272
~ _rgba32_sample_CMYK32 : 1720 -> 1760
~ _rgba32_sample_cmyk32 : 1692 -> 1732
~ _rgba32_sample_RGB48 : 1504 -> 1524
~ _rgba32_sample_rgb48 : 1308 -> 1328
~ _rgba32_sample_RGBA64 : 1664 -> 1684
~ _rgba32_sample_rgba64 : 1252 -> 1272
~ _rgba32_sample_RGBF : 1428 -> 1432
~ _rgba32_sample_RGBf : 1360 -> 1364
~ _rgba32_sample_RGBAF : 1528 -> 1548
~ _rgba32_sample_RGBAf : 1416 -> 1436
~ _RGBAf16_sample_Wf16 : 1752 -> 1792
~ _RGBAf16_sample_RGBf16 : 1532 -> 1552
~ _RGBAf16_sample_CMYKf16 : 1864 -> 1904
~ __ZL20Wf16_sample_Wf_innerPK6_ImgOplli : 2268 -> 2240
~ __ZL22Wf16_sample_RGBf_innerPK6_ImgOplli : 1596 -> 1616
~ __ZL23Wf16_sample_RGBAf_innerPK6_ImgOplli : 2016 -> 2036
~ _Wf16_sample_CMYKf16 : 1884 -> 1924
~ __Z24CIF10_sample_CIF10_innerPK6_ImgOplli : 1608 -> 1648
~ _CIF10_sample_RGBAf16 : 1464 -> 1484
```
