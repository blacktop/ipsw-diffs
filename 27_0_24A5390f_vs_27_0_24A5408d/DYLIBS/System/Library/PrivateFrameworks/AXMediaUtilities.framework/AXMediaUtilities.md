## AXMediaUtilities

> `/System/Library/PrivateFrameworks/AXMediaUtilities.framework/AXMediaUtilities`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-184.0.0.0.0
-  __TEXT.__text: 0xd4554
-  __TEXT.__objc_methlist: 0xb534
-  __TEXT.__const: 0x166c
+186.0.0.0.0
+  __TEXT.__text: 0xd6480
+  __TEXT.__objc_methlist: 0xb61c
+  __TEXT.__const: 0x168c
   __TEXT.__dlopen_cstrs: 0xc72
   __TEXT.__swift5_typeref: 0x2f0
-  __TEXT.__cstring: 0xa6aa
+  __TEXT.__cstring: 0xa772
   __TEXT.__swift5_reflstr: 0x25d
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__constg_swiftt: 0x3f8

   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_proto: 0x8c
   __TEXT.__swift5_types: 0x30
-  __TEXT.__gcc_except_tab: 0x58b8
-  __TEXT.__oslogstring: 0x5420
+  __TEXT.__gcc_except_tab: 0x58d0
+  __TEXT.__oslogstring: 0x5529
   __TEXT.__ustring: 0x422
-  __TEXT.__unwind_info: 0x3578
+  __TEXT.__unwind_info: 0x35a0
   __TEXT.__eh_frame: 0x390
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6238
+  __DATA_CONST.__objc_selrefs: 0x6300
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x418
   __DATA_CONST.__objc_arraydata: 0x6b8
-  __DATA_CONST.__got: 0xe78
+  __DATA_CONST.__got: 0xe90
   __AUTH_CONST.__const: 0x1d28
-  __AUTH_CONST.__cfstring: 0xcc60
-  __AUTH_CONST.__objc_const: 0x143a8
+  __AUTH_CONST.__cfstring: 0xcdc0
+  __AUTH_CONST.__objc_const: 0x14448
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0xab0
   __AUTH_CONST.__objc_doubleobj: 0x290
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0xf00
+  __AUTH_CONST.__auth_got: 0xf08
   __AUTH.__objc_data: 0x3db0
   __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0xec4
-  __DATA.__data: 0xe30
+  __DATA.__objc_ivar: 0xed0
+  __DATA.__data: 0xe38
   __DATA.__bss: 0x1d20
   __DATA.__common: 0x80
   __DATA_DIRTY.__objc_data: 0x2d0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4745
-  Symbols:   11183
-  CStrings:  2500
+  Functions: 4764
+  Symbols:   11231
+  CStrings:  2513
 
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
+ -[AXMScreenGrabber _displayForID:]
+ -[AXMScreenGrabber grabScreenWithRect:orientation:displayID:options:metrics:error:]
+ GCC_except_table1007
+ GCC_except_table1008
+ GCC_except_table1039
+ GCC_except_table1040
+ GCC_except_table1117
+ GCC_except_table1118
+ GCC_except_table1119
+ GCC_except_table1120
+ GCC_except_table1139
+ GCC_except_table1164
+ GCC_except_table1181
+ GCC_except_table1182
+ GCC_except_table1190
+ GCC_except_table1200
+ GCC_except_table1201
+ GCC_except_table1202
+ GCC_except_table1209
+ GCC_except_table1220
+ GCC_except_table1223
+ GCC_except_table1227
+ GCC_except_table1234
+ GCC_except_table1250
+ GCC_except_table1324
+ GCC_except_table1411
+ GCC_except_table144
+ GCC_except_table1499
+ GCC_except_table1500
+ GCC_except_table1501
+ GCC_except_table1517
+ GCC_except_table1523
+ GCC_except_table153
+ GCC_except_table1530
+ GCC_except_table1548
+ GCC_except_table1552
+ GCC_except_table1571
+ GCC_except_table1595
+ GCC_except_table1598
+ GCC_except_table160
+ GCC_except_table1606
+ GCC_except_table1609
+ GCC_except_table1612
+ GCC_except_table1613
+ GCC_except_table1615
+ GCC_except_table167
+ GCC_except_table1710
+ GCC_except_table1742
+ GCC_except_table1743
+ GCC_except_table176
+ GCC_except_table1799
+ GCC_except_table1803
+ GCC_except_table185
+ GCC_except_table1866
+ GCC_except_table1868
+ GCC_except_table1869
+ GCC_except_table1875
+ GCC_except_table1876
+ GCC_except_table1877
+ GCC_except_table1878
+ GCC_except_table1897
+ GCC_except_table193
+ GCC_except_table1939
+ GCC_except_table1979
+ GCC_except_table1980
+ GCC_except_table1981
+ GCC_except_table1982
+ GCC_except_table1983
+ GCC_except_table1991
+ GCC_except_table1994
+ GCC_except_table1995
+ GCC_except_table1997
+ GCC_except_table200
+ GCC_except_table204
+ GCC_except_table209
+ GCC_except_table2127
+ GCC_except_table2128
+ GCC_except_table2131
+ GCC_except_table214
+ GCC_except_table2163
+ GCC_except_table2188
+ GCC_except_table219
+ GCC_except_table2216
+ GCC_except_table2218
+ GCC_except_table2237
+ GCC_except_table2243
+ GCC_except_table2261
+ GCC_except_table2262
+ GCC_except_table227
+ GCC_except_table2270
+ GCC_except_table2271
+ GCC_except_table2279
+ GCC_except_table2280
+ GCC_except_table2281
+ GCC_except_table2282
+ GCC_except_table2283
+ GCC_except_table231
+ GCC_except_table235
+ GCC_except_table2370
+ GCC_except_table2371
+ GCC_except_table2372
+ GCC_except_table2374
+ GCC_except_table2382
+ GCC_except_table2383
+ GCC_except_table2385
+ GCC_except_table2386
+ GCC_except_table2399
+ GCC_except_table2400
+ GCC_except_table2409
+ GCC_except_table2415
+ GCC_except_table2418
+ GCC_except_table2422
+ GCC_except_table2429
+ GCC_except_table2430
+ GCC_except_table2436
+ GCC_except_table2438
+ GCC_except_table2450
+ GCC_except_table2452
+ GCC_except_table2453
+ GCC_except_table2454
+ GCC_except_table2456
+ GCC_except_table2717
+ GCC_except_table2718
+ GCC_except_table2719
+ GCC_except_table2720
+ GCC_except_table2722
+ GCC_except_table2727
+ GCC_except_table2728
+ GCC_except_table2729
+ GCC_except_table273
+ GCC_except_table2731
+ GCC_except_table2732
+ GCC_except_table274
+ GCC_except_table2747
+ GCC_except_table2757
+ GCC_except_table2887
+ GCC_except_table2893
+ GCC_except_table2900
+ GCC_except_table2901
+ GCC_except_table2902
+ GCC_except_table2903
+ GCC_except_table2909
+ GCC_except_table295
+ GCC_except_table2986
+ GCC_except_table2987
+ GCC_except_table2994
+ GCC_except_table3019
+ GCC_except_table3020
+ GCC_except_table3030
+ GCC_except_table3035
+ GCC_except_table3063
+ GCC_except_table3064
+ GCC_except_table3065
+ GCC_except_table3066
+ GCC_except_table3067
+ GCC_except_table3068
+ GCC_except_table3069
+ GCC_except_table3070
+ GCC_except_table3071
+ GCC_except_table3074
+ GCC_except_table3075
+ GCC_except_table3076
+ GCC_except_table3242
+ GCC_except_table329
+ GCC_except_table3299
+ GCC_except_table3300
+ GCC_except_table3301
+ GCC_except_table3303
+ GCC_except_table3306
+ GCC_except_table3321
+ GCC_except_table3322
+ GCC_except_table3335
+ GCC_except_table3348
+ GCC_except_table335
+ GCC_except_table336
+ GCC_except_table3372
+ GCC_except_table3387
+ GCC_except_table3391
+ GCC_except_table3395
+ GCC_except_table3398
+ GCC_except_table340
+ GCC_except_table341
+ GCC_except_table3417
+ GCC_except_table346
+ GCC_except_table347
+ GCC_except_table354
+ GCC_except_table357
+ GCC_except_table36
+ GCC_except_table3611
+ GCC_except_table3614
+ GCC_except_table3625
+ GCC_except_table3629
+ GCC_except_table363
+ GCC_except_table364
+ GCC_except_table3665
+ GCC_except_table3879
+ GCC_except_table3883
+ GCC_except_table3895
+ GCC_except_table3952
+ GCC_except_table3956
+ GCC_except_table3962
+ GCC_except_table3980
+ GCC_except_table3984
+ GCC_except_table3988
+ GCC_except_table3992
+ GCC_except_table3995
+ GCC_except_table4017
+ GCC_except_table412
+ GCC_except_table413
+ GCC_except_table4133
+ GCC_except_table4138
+ GCC_except_table4142
+ GCC_except_table4146
+ GCC_except_table4153
+ GCC_except_table4154
+ GCC_except_table4155
+ GCC_except_table4156
+ GCC_except_table418
+ GCC_except_table419
+ GCC_except_table437
+ GCC_except_table451
+ GCC_except_table452
+ GCC_except_table459
+ GCC_except_table472
+ GCC_except_table479
+ GCC_except_table480
+ GCC_except_table528
+ GCC_except_table610
+ GCC_except_table719
+ GCC_except_table728
+ GCC_except_table729
+ GCC_except_table738
+ GCC_except_table783
+ GCC_except_table784
+ GCC_except_table789
+ GCC_except_table858
+ GCC_except_table883
+ GCC_except_table909
+ GCC_except_table928
+ GCC_except_table997
+ GCC_except_table998
+ _AXMPhotoAssetDataCodingKeyTimeZone
+ _CGRectIsInfinite
+ _OBJC_CLASS_$_NSTimeZone
+ _OBJC_IVAR_$_AXMBrailleEdgeDetectorOptions._edgeLuminanceThreshold
+ _OBJC_IVAR_$_AXMBrailleEdgeDetectorOptions._flatLuminanceThreshold
+ _OBJC_IVAR_$_AXMDisplay._isExternal
+ _OBJC_IVAR_$_AXMPhotoAssetData._assetTimeZone
+ ___83-[AXMScreenGrabber grabScreenWithRect:orientation:displayID:options:metrics:error:]_block_invoke
+ _kCIInputBackgroundImageKey
+ _kCIInputRadiusKey
+ _objc_msgSend$_analyzeImage:
+ _objc_msgSend$_compositedLuminanceOfPixel:overBackground:
+ _objc_msgSend$_displayForID:
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
+ _objc_msgSend$colorWithRed:green:blue:alpha:
+ _objc_msgSend$dataWithCapacity:
+ _objc_msgSend$edgeLuminanceThreshold
+ _objc_msgSend$flatLuminanceThreshold
+ _objc_msgSend$grabScreenWithRect:orientation:displayID:options:metrics:error:
+ _objc_msgSend$imageWithColor:
+ _objc_msgSend$isExternal
+ _objc_msgSend$localCreationDate
+ _objc_msgSend$setAssetTimeZone:
+ _objc_msgSend$setIncludeTrashedAssets:
+ _objc_msgSend$setIsExternal:
+ _objc_msgSend$timeZoneForSecondsFromGMT:
- -[AXMBrailleEdgeDetectorOptions luminanceThreshold]
- -[AXMBrailleEdgeDetectorOptions setLuminanceThreshold:]
- -[AXMBrailleEdgesDetectorNode _generateResultFromImage:canvasDescription:invert:luminanceThreshold:]
- -[AXMBrailleEdgesDetectorNode _mapLuminance:toDiscreteNumber:invert:threshold:]
- -[AXMBrailleEdgesDetectorNode _processImage:analaysisOptions:]
- GCC_except_table1002
- GCC_except_table1003
- GCC_except_table1034
- GCC_except_table1035
- GCC_except_table1108
- GCC_except_table1110
- GCC_except_table1112
- GCC_except_table1114
- GCC_except_table1134
- GCC_except_table1159
- GCC_except_table1175
- GCC_except_table1176
- GCC_except_table1177
- GCC_except_table1194
- GCC_except_table1195
- GCC_except_table1196
- GCC_except_table1197
- GCC_except_table1215
- GCC_except_table1218
- GCC_except_table1222
- GCC_except_table1229
- GCC_except_table1245
- GCC_except_table1319
- GCC_except_table1406
- GCC_except_table142
- GCC_except_table1494
- GCC_except_table1495
- GCC_except_table1496
- GCC_except_table151
- GCC_except_table1512
- GCC_except_table1513
- GCC_except_table1525
- GCC_except_table1543
- GCC_except_table1547
- GCC_except_table1561
- GCC_except_table158
- GCC_except_table1585
- GCC_except_table1593
- GCC_except_table1596
- GCC_except_table1597
- GCC_except_table1599
- GCC_except_table1600
- GCC_except_table1603
- GCC_except_table165
- GCC_except_table1705
- GCC_except_table1737
- GCC_except_table1738
- GCC_except_table174
- GCC_except_table1794
- GCC_except_table1798
- GCC_except_table183
- GCC_except_table1844
- GCC_except_table1845
- GCC_except_table1846
- GCC_except_table1847
- GCC_except_table1848
- GCC_except_table1871
- GCC_except_table1873
- GCC_except_table1892
- GCC_except_table191
- GCC_except_table1934
- GCC_except_table1966
- GCC_except_table1967
- GCC_except_table1968
- GCC_except_table1969
- GCC_except_table1970
- GCC_except_table198
- GCC_except_table1985
- GCC_except_table1986
- GCC_except_table1987
- GCC_except_table1989
- GCC_except_table202
- GCC_except_table207
- GCC_except_table212
- GCC_except_table2121
- GCC_except_table2122
- GCC_except_table2123
- GCC_except_table2158
- GCC_except_table217
- GCC_except_table2183
- GCC_except_table2211
- GCC_except_table2213
- GCC_except_table2232
- GCC_except_table2238
- GCC_except_table225
- GCC_except_table2253
- GCC_except_table2254
- GCC_except_table2255
- GCC_except_table2256
- GCC_except_table2257
- GCC_except_table2266
- GCC_except_table2267
- GCC_except_table2275
- GCC_except_table2276
- GCC_except_table229
- GCC_except_table233
- GCC_except_table2365
- GCC_except_table2366
- GCC_except_table2367
- GCC_except_table2368
- GCC_except_table2369
- GCC_except_table2375
- GCC_except_table2376
- GCC_except_table2377
- GCC_except_table2384
- GCC_except_table2390
- GCC_except_table2391
- GCC_except_table2397
- GCC_except_table2403
- GCC_except_table2404
- GCC_except_table2405
- GCC_except_table2419
- GCC_except_table2423
- GCC_except_table2425
- GCC_except_table2432
- GCC_except_table2435
- GCC_except_table2444
- GCC_except_table2448
- GCC_except_table2451
- GCC_except_table267
- GCC_except_table268
- GCC_except_table2698
- GCC_except_table2700
- GCC_except_table2701
- GCC_except_table2702
- GCC_except_table2703
- GCC_except_table2705
- GCC_except_table2710
- GCC_except_table2711
- GCC_except_table2712
- GCC_except_table2713
- GCC_except_table2714
- GCC_except_table2740
- GCC_except_table2867
- GCC_except_table2870
- GCC_except_table2876
- GCC_except_table2883
- GCC_except_table2885
- GCC_except_table2886
- GCC_except_table2892
- GCC_except_table293
- GCC_except_table2969
- GCC_except_table2970
- GCC_except_table2977
- GCC_except_table3002
- GCC_except_table3003
- GCC_except_table3013
- GCC_except_table3018
- GCC_except_table3046
- GCC_except_table3047
- GCC_except_table3048
- GCC_except_table3049
- GCC_except_table3050
- GCC_except_table3051
- GCC_except_table3052
- GCC_except_table3053
- GCC_except_table3054
- GCC_except_table3057
- GCC_except_table3058
- GCC_except_table3059
- GCC_except_table3225
- GCC_except_table323
- GCC_except_table326
- GCC_except_table3282
- GCC_except_table3283
- GCC_except_table3284
- GCC_except_table3286
- GCC_except_table3287
- GCC_except_table3288
- GCC_except_table3289
- GCC_except_table3318
- GCC_except_table333
- GCC_except_table3331
- GCC_except_table3355
- GCC_except_table3370
- GCC_except_table3374
- GCC_except_table3378
- GCC_except_table338
- GCC_except_table3381
- GCC_except_table339
- GCC_except_table34
- GCC_except_table3400
- GCC_except_table343
- GCC_except_table344
- GCC_except_table352
- GCC_except_table355
- GCC_except_table3592
- GCC_except_table3595
- GCC_except_table3606
- GCC_except_table361
- GCC_except_table3610
- GCC_except_table362
- GCC_except_table3646
- GCC_except_table3860
- GCC_except_table3864
- GCC_except_table3876
- GCC_except_table3933
- GCC_except_table3937
- GCC_except_table3943
- GCC_except_table3957
- GCC_except_table3961
- GCC_except_table3965
- GCC_except_table3969
- GCC_except_table3973
- GCC_except_table3998
- GCC_except_table410
- GCC_except_table411
- GCC_except_table4114
- GCC_except_table4119
- GCC_except_table4123
- GCC_except_table4127
- GCC_except_table4134
- GCC_except_table4135
- GCC_except_table4136
- GCC_except_table4137
- GCC_except_table416
- GCC_except_table417
- GCC_except_table435
- GCC_except_table449
- GCC_except_table450
- GCC_except_table455
- GCC_except_table468
- GCC_except_table477
- GCC_except_table478
- GCC_except_table526
- GCC_except_table608
- GCC_except_table717
- GCC_except_table724
- GCC_except_table727
- GCC_except_table736
- GCC_except_table772
- GCC_except_table773
- GCC_except_table787
- GCC_except_table856
- GCC_except_table881
- GCC_except_table907
- GCC_except_table926
- GCC_except_table992
- GCC_except_table993
- _OBJC_IVAR_$_AXMBrailleEdgeDetectorOptions._luminanceThreshold
- ___73-[AXMScreenGrabber grabScreenWithRect:orientation:options:metrics:error:]_block_invoke
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
