## AXMediaUtilities

> `/System/Library/PrivateFrameworks/AXMediaUtilities.framework/Versions/A/AXMediaUtilities`

```diff

-184.0.0.0.0
-  __TEXT.__text: 0xbf044
-  __TEXT.__objc_methlist: 0xa2fc
-  __TEXT.__const: 0x13fc
+186.0.0.0.0
+  __TEXT.__text: 0xc0e7c
+  __TEXT.__objc_methlist: 0xa3dc
+  __TEXT.__const: 0x140c
   __TEXT.__dlopen_cstrs: 0x7d0
   __TEXT.__swift5_typeref: 0x2f0
-  __TEXT.__cstring: 0x93f4
+  __TEXT.__cstring: 0x94bc
   __TEXT.__swift5_reflstr: 0x25d
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__constg_swiftt: 0x3f8

   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_proto: 0x8c
   __TEXT.__swift5_types: 0x30
-  __TEXT.__gcc_except_tab: 0x48a0
-  __TEXT.__oslogstring: 0x37d5
+  __TEXT.__gcc_except_tab: 0x48b8
+  __TEXT.__oslogstring: 0x38de
   __TEXT.__ustring: 0x422
-  __TEXT.__unwind_info: 0x3000
+  __TEXT.__unwind_info: 0x3020
   __TEXT.__eh_frame: 0x390
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5790
+  __DATA_CONST.__objc_selrefs: 0x5868
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x3c0
   __DATA_CONST.__objc_arraydata: 0x6b8
-  __DATA_CONST.__got: 0xc38
+  __DATA_CONST.__got: 0xc58
   __AUTH_CONST.__const: 0x2b98
-  __AUTH_CONST.__cfstring: 0xb920
-  __AUTH_CONST.__objc_const: 0x12410
+  __AUTH_CONST.__cfstring: 0xba80
+  __AUTH_CONST.__objc_const: 0x124b0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0xa68
   __AUTH_CONST.__objc_doubleobj: 0x280
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0xcf0
+  __AUTH_CONST.__auth_got: 0xcf8
   __AUTH.__objc_data: 0x3900
   __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0xd0c
-  __DATA.__data: 0xd48
+  __DATA.__objc_ivar: 0xd18
+  __DATA.__data: 0xd50
   __DATA.__bss: 0x1ae8
   __DATA.__common: 0x80
   __DATA_DIRTY.__objc_data: 0x2d0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4294
-  Symbols:   9992
-  CStrings:  2163
+  Functions: 4312
+  Symbols:   10041
+  CStrings:  2176
 
Symbols:
+ -[AXMBrailleEdgeDetectorOptions edgeLuminanceThreshold]
+ -[AXMBrailleEdgeDetectorOptions flatLuminanceThreshold]
+ -[AXMBrailleEdgeDetectorOptions setEdgeLuminanceThreshold:]
+ -[AXMBrailleEdgeDetectorOptions setFlatLuminanceThreshold:]
+ -[AXMBrailleEdgesDetectorNode _analyzeImage:]
+ -[AXMBrailleEdgesDetectorNode _compositedLuminanceOfPixel:overBackground:]
+ -[AXMBrailleEdgesDetectorNode _flatImageNormalizationBoundsForStats:outMin:outMax:]
+ -[AXMBrailleEdgesDetectorNode _flattenTransparency:overWhite:]
+ -[AXMBrailleEdgesDetectorNode _generateResultFromEdgeDetectedImage:canvasDescription:invert:threshold:panOrigin:zoom:]
+ -[AXMBrailleEdgesDetectorNode _generateResultFromFlatImage:canvasDescription:invert:threshold:normalizeMin:normalizeMax:panOrigin:zoom:]
+ -[AXMBrailleEdgesDetectorNode _luminanceRangeInData:canvas:rect:outMin:outMax:]
+ -[AXMBrailleEdgesDetectorNode _pinsFromData:canvas:normalizeMin:normalizeMax:threshold:invert:]
+ -[AXMBrailleEdgesDetectorNode _processImage:analaysisOptions:stats:]
+ -[AXMBrailleEdgesDetectorNode _quantizeLuminance:toPinHeightCount:invert:threshold:]
+ -[AXMBrailleEdgesDetectorNode _renderImage:ontoCanvas:panOrigin:zoom:contentRect:]
+ -[AXMBrailleEdgesDetectorNode debugAnalyzeImage:]
+ -[AXMBrailleEdgesDetectorNode debugProcessedImageForImage:analysisOptions:]
+ -[AXMDisplay isExternal]
+ -[AXMDisplay setIsExternal:]
+ -[AXMPhotoAssetData assetTimeZone]
+ -[AXMPhotoAssetData setAssetTimeZone:]
+ -[AXMPhotoAssetData timeZone]
+ -[AXMScreenGrabber grabScreenWithRect:orientation:displayID:options:metrics:error:]
+ GCC_except_table1027
+ GCC_except_table1028
+ GCC_except_table1105
+ GCC_except_table1106
+ GCC_except_table1107
+ GCC_except_table1108
+ GCC_except_table1127
+ GCC_except_table1153
+ GCC_except_table1155
+ GCC_except_table1158
+ GCC_except_table1163
+ GCC_except_table1172
+ GCC_except_table1174
+ GCC_except_table1175
+ GCC_except_table1177
+ GCC_except_table1182
+ GCC_except_table1193
+ GCC_except_table1200
+ GCC_except_table1208
+ GCC_except_table1224
+ GCC_except_table1297
+ GCC_except_table133
+ GCC_except_table1372
+ GCC_except_table142
+ GCC_except_table1460
+ GCC_except_table1461
+ GCC_except_table1462
+ GCC_except_table1478
+ GCC_except_table1479
+ GCC_except_table1484
+ GCC_except_table149
+ GCC_except_table1491
+ GCC_except_table1513
+ GCC_except_table1526
+ GCC_except_table1531
+ GCC_except_table156
+ GCC_except_table1631
+ GCC_except_table165
+ GCC_except_table1663
+ GCC_except_table1664
+ GCC_except_table1724
+ GCC_except_table174
+ GCC_except_table1788
+ GCC_except_table1790
+ GCC_except_table1791
+ GCC_except_table1796
+ GCC_except_table1797
+ GCC_except_table1798
+ GCC_except_table1799
+ GCC_except_table182
+ GCC_except_table1827
+ GCC_except_table1868
+ GCC_except_table1869
+ GCC_except_table1870
+ GCC_except_table1871
+ GCC_except_table1880
+ GCC_except_table1882
+ GCC_except_table1883
+ GCC_except_table1885
+ GCC_except_table189
+ GCC_except_table193
+ GCC_except_table198
+ GCC_except_table2014
+ GCC_except_table2016
+ GCC_except_table2019
+ GCC_except_table203
+ GCC_except_table2051
+ GCC_except_table2076
+ GCC_except_table208
+ GCC_except_table2104
+ GCC_except_table2106
+ GCC_except_table2125
+ GCC_except_table2126
+ GCC_except_table2134
+ GCC_except_table2135
+ GCC_except_table2143
+ GCC_except_table2144
+ GCC_except_table2145
+ GCC_except_table2146
+ GCC_except_table216
+ GCC_except_table220
+ GCC_except_table2234
+ GCC_except_table2235
+ GCC_except_table2236
+ GCC_except_table224
+ GCC_except_table2243
+ GCC_except_table2246
+ GCC_except_table2249
+ GCC_except_table2252
+ GCC_except_table2258
+ GCC_except_table2264
+ GCC_except_table2265
+ GCC_except_table2266
+ GCC_except_table2275
+ GCC_except_table2276
+ GCC_except_table2277
+ GCC_except_table2282
+ GCC_except_table2283
+ GCC_except_table2284
+ GCC_except_table2285
+ GCC_except_table2290
+ GCC_except_table2297
+ GCC_except_table2299
+ GCC_except_table23
+ GCC_except_table2300
+ GCC_except_table2302
+ GCC_except_table2308
+ GCC_except_table2311
+ GCC_except_table2313
+ GCC_except_table2318
+ GCC_except_table2324
+ GCC_except_table2325
+ GCC_except_table2327
+ GCC_except_table2569
+ GCC_except_table257
+ GCC_except_table2570
+ GCC_except_table2571
+ GCC_except_table2572
+ GCC_except_table2574
+ GCC_except_table2579
+ GCC_except_table2580
+ GCC_except_table2581
+ GCC_except_table2582
+ GCC_except_table2583
+ GCC_except_table2584
+ GCC_except_table263
+ GCC_except_table2788
+ GCC_except_table2789
+ GCC_except_table2796
+ GCC_except_table280
+ GCC_except_table2822
+ GCC_except_table2832
+ GCC_except_table2837
+ GCC_except_table2865
+ GCC_except_table2866
+ GCC_except_table2867
+ GCC_except_table2868
+ GCC_except_table2869
+ GCC_except_table2870
+ GCC_except_table2871
+ GCC_except_table2872
+ GCC_except_table2873
+ GCC_except_table2876
+ GCC_except_table2877
+ GCC_except_table2878
+ GCC_except_table3027
+ GCC_except_table3084
+ GCC_except_table3085
+ GCC_except_table3086
+ GCC_except_table3088
+ GCC_except_table3089
+ GCC_except_table310
+ GCC_except_table3106
+ GCC_except_table3107
+ GCC_except_table3117
+ GCC_except_table3130
+ GCC_except_table315
+ GCC_except_table3152
+ GCC_except_table3166
+ GCC_except_table317
+ GCC_except_table321
+ GCC_except_table326
+ GCC_except_table332
+ GCC_except_table3366
+ GCC_except_table339
+ GCC_except_table344
+ GCC_except_table353
+ GCC_except_table3600
+ GCC_except_table3604
+ GCC_except_table3624
+ GCC_except_table3628
+ GCC_except_table3632
+ GCC_except_table3636
+ GCC_except_table3640
+ GCC_except_table3643
+ GCC_except_table3665
+ GCC_except_table3759
+ GCC_except_table3768
+ GCC_except_table3772
+ GCC_except_table3779
+ GCC_except_table3780
+ GCC_except_table3781
+ GCC_except_table3782
+ GCC_except_table400
+ GCC_except_table406
+ GCC_except_table424
+ GCC_except_table441
+ GCC_except_table446
+ GCC_except_table448
+ GCC_except_table459
+ GCC_except_table461
+ GCC_except_table469
+ GCC_except_table517
+ GCC_except_table597
+ GCC_except_table717
+ GCC_except_table720
+ GCC_except_table731
+ GCC_except_table773
+ GCC_except_table778
+ GCC_except_table844
+ GCC_except_table869
+ GCC_except_table895
+ GCC_except_table916
+ GCC_except_table985
+ GCC_except_table986
+ GCC_except_table995
+ GCC_except_table996
+ OBJC_IVAR_$_AXMBrailleEdgeDetectorOptions._edgeLuminanceThreshold
+ OBJC_IVAR_$_AXMBrailleEdgeDetectorOptions._flatLuminanceThreshold
+ OBJC_IVAR_$_AXMDisplay._isExternal
+ OBJC_IVAR_$_AXMPhotoAssetData._assetTimeZone
+ _AXMPhotoAssetDataCodingKeyTimeZone
+ _CGRectIsInfinite
+ _OBJC_CLASS_$_CIColor
+ _OBJC_CLASS_$_NSTimeZone
+ _kCIInputBackgroundImageKey
+ _kCIInputRadiusKey
+ _objc_msgSend$_analyzeImage:
+ _objc_msgSend$_compositedLuminanceOfPixel:overBackground:
+ _objc_msgSend$_flatImageNormalizationBoundsForStats:outMin:outMax:
+ _objc_msgSend$_flattenTransparency:overWhite:
+ _objc_msgSend$_generateResultFromEdgeDetectedImage:canvasDescription:invert:threshold:panOrigin:zoom:
+ _objc_msgSend$_generateResultFromFlatImage:canvasDescription:invert:threshold:normalizeMin:normalizeMax:panOrigin:zoom:
+ _objc_msgSend$_luminanceRangeInData:canvas:rect:outMin:outMax:
+ _objc_msgSend$_pinsFromData:canvas:normalizeMin:normalizeMax:threshold:invert:
+ _objc_msgSend$_processImage:analaysisOptions:stats:
+ _objc_msgSend$_quantizeLuminance:toPinHeightCount:invert:threshold:
+ _objc_msgSend$_renderImage:ontoCanvas:panOrigin:zoom:contentRect:
+ _objc_msgSend$assetTimeZone
+ _objc_msgSend$bytes
+ _objc_msgSend$colorWithRed:green:blue:alpha:
+ _objc_msgSend$dataWithCapacity:
+ _objc_msgSend$edgeLuminanceThreshold
+ _objc_msgSend$flatLuminanceThreshold
+ _objc_msgSend$grabScreenWithRect:orientation:displayID:options:metrics:error:
+ _objc_msgSend$imageByCompositingOverImage:
+ _objc_msgSend$imageWithColor:
+ _objc_msgSend$isExternal
+ _objc_msgSend$localCreationDate
+ _objc_msgSend$mutableBytes
+ _objc_msgSend$setAssetTimeZone:
+ _objc_msgSend$setIncludeTrashedAssets:
+ _objc_msgSend$timeZoneForSecondsFromGMT:
- -[AXMBrailleEdgeDetectorOptions luminanceThreshold]
- -[AXMBrailleEdgeDetectorOptions setLuminanceThreshold:]
- -[AXMBrailleEdgesDetectorNode _generateResultFromImage:canvasDescription:invert:luminanceThreshold:]
- -[AXMBrailleEdgesDetectorNode _mapLuminance:toDiscreteNumber:invert:threshold:]
- -[AXMBrailleEdgesDetectorNode _processImage:analaysisOptions:]
- GCC_except_table1023
- GCC_except_table1024
- GCC_except_table1097
- GCC_except_table1099
- GCC_except_table1102
- GCC_except_table1104
- GCC_except_table1123
- GCC_except_table1149
- GCC_except_table1150
- GCC_except_table1151
- GCC_except_table1159
- GCC_except_table1168
- GCC_except_table1169
- GCC_except_table1170
- GCC_except_table1171
- GCC_except_table1178
- GCC_except_table1189
- GCC_except_table1192
- GCC_except_table1204
- GCC_except_table1220
- GCC_except_table1293
- GCC_except_table132
- GCC_except_table1368
- GCC_except_table141
- GCC_except_table1456
- GCC_except_table1457
- GCC_except_table1458
- GCC_except_table1474
- GCC_except_table1475
- GCC_except_table148
- GCC_except_table1480
- GCC_except_table1487
- GCC_except_table1505
- GCC_except_table1522
- GCC_except_table1527
- GCC_except_table155
- GCC_except_table1627
- GCC_except_table164
- GCC_except_table1659
- GCC_except_table1660
- GCC_except_table1716
- GCC_except_table173
- GCC_except_table1766
- GCC_except_table1767
- GCC_except_table1768
- GCC_except_table1769
- GCC_except_table1792
- GCC_except_table1794
- GCC_except_table1795
- GCC_except_table181
- GCC_except_table1823
- GCC_except_table1855
- GCC_except_table1856
- GCC_except_table1857
- GCC_except_table1858
- GCC_except_table1874
- GCC_except_table1875
- GCC_except_table1876
- GCC_except_table188
- GCC_except_table1881
- GCC_except_table192
- GCC_except_table197
- GCC_except_table2010
- GCC_except_table2011
- GCC_except_table2012
- GCC_except_table202
- GCC_except_table2047
- GCC_except_table207
- GCC_except_table2072
- GCC_except_table2100
- GCC_except_table2102
- GCC_except_table2117
- GCC_except_table2118
- GCC_except_table2119
- GCC_except_table2120
- GCC_except_table2129
- GCC_except_table2130
- GCC_except_table2138
- GCC_except_table2139
- GCC_except_table215
- GCC_except_table219
- GCC_except_table22
- GCC_except_table2229
- GCC_except_table223
- GCC_except_table2230
- GCC_except_table2231
- GCC_except_table2232
- GCC_except_table2239
- GCC_except_table2240
- GCC_except_table2242
- GCC_except_table2253
- GCC_except_table2254
- GCC_except_table2260
- GCC_except_table2262
- GCC_except_table2263
- GCC_except_table2268
- GCC_except_table2269
- GCC_except_table2270
- GCC_except_table2279
- GCC_except_table2280
- GCC_except_table2281
- GCC_except_table2286
- GCC_except_table2287
- GCC_except_table2289
- GCC_except_table2294
- GCC_except_table2296
- GCC_except_table2301
- GCC_except_table2304
- GCC_except_table2307
- GCC_except_table2312
- GCC_except_table2314
- GCC_except_table2317
- GCC_except_table2319
- GCC_except_table2551
- GCC_except_table2553
- GCC_except_table2554
- GCC_except_table2555
- GCC_except_table2556
- GCC_except_table2558
- GCC_except_table256
- GCC_except_table2563
- GCC_except_table2564
- GCC_except_table2565
- GCC_except_table2566
- GCC_except_table2568
- GCC_except_table262
- GCC_except_table2772
- GCC_except_table2773
- GCC_except_table2780
- GCC_except_table279
- GCC_except_table2805
- GCC_except_table2806
- GCC_except_table2816
- GCC_except_table2849
- GCC_except_table2850
- GCC_except_table2851
- GCC_except_table2852
- GCC_except_table2853
- GCC_except_table2854
- GCC_except_table2855
- GCC_except_table2856
- GCC_except_table2857
- GCC_except_table2860
- GCC_except_table2861
- GCC_except_table2862
- GCC_except_table3011
- GCC_except_table3068
- GCC_except_table3069
- GCC_except_table3070
- GCC_except_table3072
- GCC_except_table3073
- GCC_except_table3074
- GCC_except_table3075
- GCC_except_table309
- GCC_except_table3101
- GCC_except_table311
- GCC_except_table3114
- GCC_except_table3136
- GCC_except_table3150
- GCC_except_table316
- GCC_except_table318
- GCC_except_table324
- GCC_except_table329
- GCC_except_table3348
- GCC_except_table338
- GCC_except_table343
- GCC_except_table351
- GCC_except_table3582
- GCC_except_table3586
- GCC_except_table3592
- GCC_except_table3606
- GCC_except_table3614
- GCC_except_table3618
- GCC_except_table3622
- GCC_except_table3625
- GCC_except_table3647
- GCC_except_table3741
- GCC_except_table3746
- GCC_except_table3750
- GCC_except_table3754
- GCC_except_table3761
- GCC_except_table3762
- GCC_except_table3763
- GCC_except_table398
- GCC_except_table404
- GCC_except_table423
- GCC_except_table439
- GCC_except_table445
- GCC_except_table447
- GCC_except_table458
- GCC_except_table460
- GCC_except_table467
- GCC_except_table516
- GCC_except_table596
- GCC_except_table715
- GCC_except_table718
- GCC_except_table730
- GCC_except_table762
- GCC_except_table777
- GCC_except_table843
- GCC_except_table868
- GCC_except_table894
- GCC_except_table915
- GCC_except_table981
- GCC_except_table982
- GCC_except_table991
- GCC_except_table992
- OBJC_IVAR_$_AXMBrailleEdgeDetectorOptions._luminanceThreshold
- _objc_msgSend$_generateResultFromImage:canvasDescription:invert:luminanceThreshold:
- _objc_msgSend$_mapLuminance:toDiscreteNumber:invert:threshold:
- _objc_msgSend$_processImage:analaysisOptions:
- _objc_msgSend$luminanceThreshold
CStrings:
+ "    edgeLuminanceThreshold: %.2f\n"
+ "    flatLuminanceThreshold: %.2f\n"
+ "AXMDisplay<%p>: Backing:%@ Name:%@ displayID:%@ uniqueID: %@ scale:%@ size:[%.2f %.2f] physicalSize:[%.2f %.2f] orientation:%@ (%s) currentPhysicalOrientation:(%s) refBounds:[%.2f %.2f %.2f %.2f] deepColor:%d isExternal:%d"
+ "AXMPhotoAssetData: No PHAsset resolved for localIdentifier %@ - unable to load image data"
+ "CISourceOverCompositing"
+ "braille classify: success=%d hasTransparency=%d useWhiteBackground=%d isFlat=%d shapeIsDark=%d minLuminance=%.3f maxLuminance=%.3f"
+ "braille: could not analyze source image; producing no pins"
+ "edgeLuminanceThreshold"
+ "flatLuminanceThreshold"
+ "hasTransparency"
+ "isFlat"
+ "maxLuminance"
+ "minLuminance"
+ "shapeIsDark"
+ "success"
+ "timeZone"
+ "useWhiteBackground"
- "    luminanceThreshold: %.2f\n"
- "%@ %@ -- %@ %@"
- "AXMDisplay<%p>: Backing:%@ Name:%@ displayID:%@ uniqueID: %@ scale:%@ size:[%.2f %.2f] physicalSize:[%.2f %.2f] orientation:%@ (%s) currentPhysicalOrientation:(%s) refBounds:[%.2f %.2f %.2f %.2f] deepColor:%d"
- "luminanceThreshold"
```
