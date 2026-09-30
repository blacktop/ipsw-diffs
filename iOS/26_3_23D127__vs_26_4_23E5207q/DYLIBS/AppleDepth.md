## AppleDepth

> `/System/Library/PrivateFrameworks/AppleDepth.framework/AppleDepth`

```diff

-150.9.0.0.0
-  __TEXT.__text: 0x107e78
-  __TEXT.__auth_stubs: 0x1490
-  __TEXT.__objc_methlist: 0x7444
-  __TEXT.__const: 0x14c0
-  __TEXT.__gcc_except_tab: 0x12f0c
-  __TEXT.__oslogstring: 0x9249
-  __TEXT.__cstring: 0x7a9b
-  __TEXT.__unwind_info: 0x3bf8
-  __TEXT.__objc_classname: 0x9603
-  __TEXT.__objc_methname: 0x17e09
-  __TEXT.__objc_methtype: 0x8037
-  __TEXT.__objc_stubs: 0xada0
+158.0.0.0.0
+  __TEXT.__text: 0x111e6c
+  __TEXT.__auth_stubs: 0x1440
+  __TEXT.__objc_methlist: 0x7714
+  __TEXT.__const: 0x1460
+  __TEXT.__gcc_except_tab: 0x137c8
+  __TEXT.__oslogstring: 0x95bb
+  __TEXT.__cstring: 0x8c8b
+  __TEXT.__unwind_info: 0x3f40
+  __TEXT.__objc_classname: 0x9673
+  __TEXT.__objc_methname: 0x183c8
+  __TEXT.__objc_methtype: 0x813e
+  __TEXT.__objc_stubs: 0xb020
   __DATA_CONST.__got: 0xa68
-  __DATA_CONST.__const: 0x340
-  __DATA_CONST.__objc_classlist: 0x578
+  __DATA_CONST.__const: 0x358
+  __DATA_CONST.__objc_classlist: 0x598
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3830
-  __DATA_CONST.__objc_superrefs: 0x4a0
-  __DATA_CONST.__objc_arraydata: 0x1e8
-  __AUTH_CONST.__auth_got: 0xa58
-  __AUTH_CONST.__const: 0xaa8
-  __AUTH_CONST.__cfstring: 0x5bc0
-  __AUTH_CONST.__objc_const: 0x12f58
-  __AUTH_CONST.__objc_intobj: 0x480
+  __DATA_CONST.__objc_selrefs: 0x38f8
+  __DATA_CONST.__objc_superrefs: 0x4c8
+  __DATA_CONST.__objc_arraydata: 0x258
+  __AUTH_CONST.__auth_got: 0xa30
+  __AUTH_CONST.__const: 0xae8
+  __AUTH_CONST.__cfstring: 0x5ca0
+  __AUTH_CONST.__objc_const: 0x13688
+  __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH_CONST.__objc_doubleobj: 0x150
-  __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0x1270
-  __DATA.__objc_ivar: 0x1244
-  __DATA.__data: 0xe8618
+  __AUTH_CONST.__objc_doubleobj: 0x190
+  __AUTH_CONST.__objc_arrayobj: 0x138
+  __AUTH_CONST.__objc_dictobj: 0x78
+  __DATA.__objc_ivar: 0x1290
+  __DATA.__data: 0xe8678
   __DATA.__bss: 0x531
-  __DATA_DIRTY.__objc_data: 0x2440
-  __DATA_DIRTY.__bss: 0xd8
+  __DATA_DIRTY.__objc_data: 0x37f0
+  __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/libz.1.dylib
-  UUID: 510214F7-A7D2-3E9F-9F6E-AD5B68886034
-  Functions: 3168
-  Symbols:   11863
-  CStrings:  6632
+  UUID: 543CB0D0-F2BC-31E5-BB7C-17A2CAB39948
+  Functions: 3224
+  Symbols:   12083
+  CStrings:  6724
 
Symbols:
+ +[ADDeviceConfiguration verboseLogs]
+ +[ADLKTOpticalFlow _initializeBaseConfig:]
+ +[ADMonocularVideoPipeline knownNetworksForVariant:]
+ +[ADMonocularVideoPipeline subVariantsForVariant:]
+ +[ADMonocularVideoPipeline supportedDimensionsForParameters:]
+ -[ADFlowFrameInput depth]
+ -[ADFlowFrameInput setDepth:]
+ -[ADJasperColorStillsFlow .cxx_destruct]
+ -[ADJasperColorStillsFlow executor]
+ -[ADJasperColorStillsFlow initMembers:cloudsNumber:]
+ -[ADJasperColorStillsFlow initWithExecutor:]
+ -[ADJasperColorStillsFlow initWithExecutor:andAggregationSize:]
+ -[ADJasperColorStillsFlow preAllocatedOutputBuffer]
+ -[ADJasperColorStillsFlow processIfMatch:]
+ -[ADJasperColorStillsFlow pushColor:pose:calibration:metadata:timestamp:]
+ -[ADJasperColorStillsFlow pushPointCloud:pose:calibration:timestamp:]
+ -[ADJasperColorStillsFlow setPreAllocatedOutputBuffer:]
+ -[ADJasperColorV2Executor createConfidenceBuffer]
+ -[ADJasperColorV2Executor createDepthBuffer]
+ -[ADJasperColorV2Executor executeWithColor:pointCloud:jasperCalibration:colorCalibration:timestamp:outputDepthMap:outputConfidenceMap:]
+ -[ADJasperColorV2Executor pipeline]
+ -[ADJasperColorV2Flow .cxx_destruct]
+ -[ADJasperColorV2Flow executor]
+ -[ADJasperColorV2Flow initWithExecutor:]
+ -[ADJasperColorV2Flow initWithExecutor:andAggregationSize:]
+ -[ADJasperColorV2Flow preAllocatedConfidenceOutputBuffer]
+ -[ADJasperColorV2Flow preAllocatedDepthOutputBuffer]
+ -[ADJasperColorV2Flow processIfMatch:]
+ -[ADJasperColorV2Flow pushColor:pose:calibration:metadata:timestamp:]
+ -[ADJasperColorV2Flow pushPointCloud:pose:calibration:timestamp:]
+ -[ADJasperColorV2Flow setPreAllocatedConfidenceOutputBuffer:]
+ -[ADJasperColorV2Flow setPreAllocatedDepthOutputBuffer:]
+ -[ADMonocularStillsFlow .cxx_destruct]
+ -[ADMonocularStillsFlow executor]
+ -[ADMonocularStillsFlow initWithExecutor:]
+ -[ADMonocularStillsFlow processColor:efl:timestamp:]
+ -[ADMonocularStillsFlow pushColor:efl:timestamp:]
+ -[ADMonocularStillsFlow pushColor:pose:calibration:metadata:timestamp:]
+ -[ADMonocularVideoExecutor executeWithColor:cameraCalibration:outDisparityMap:]
+ -[ADMonocularVideoExecutor executeWithColor:focalLength35mm:outDisparityMap:]
+ -[ADMonocularVideoExecutor executeWithColor:scaleFactor:outDisparityMap:]
+ -[ADMonocularVideoFlow pushColor:focalLength35mm:timestamp:]
+ -[ADMonocularVideoPipeline getMetricScaleFactorFor35mmFocalLength:]
+ -[ADMonocularVideoPipelineParameters initForDevice:]
+ -[ADMonocularVideoPipelineParameters networkVariant]
+ -[ADMonocularVideoPipelineParameters setNetworkVariant:]
+ -[ADPCEDisparityColorExecutor executeWithDisparity:depthMetadata:color:outDisparity:]
+ -[ADPCEDisparityColorFlow .cxx_destruct]
+ -[ADPCEDisparityColorFlow delegate]
+ -[ADPCEDisparityColorFlow executor]
+ -[ADPCEDisparityColorFlow handleMatch:]
+ -[ADPCEDisparityColorFlow initWithExecutor:]
+ -[ADPCEDisparityColorFlow pushColor:pose:calibration:metadata:timestamp:]
+ -[ADPCEDisparityColorFlow pushDepth:pose:metadata:timestamp:]
+ -[ADPCEDisparityColorFlow setDelegate:]
+ GCC_except_table1008
+ GCC_except_table1009
+ GCC_except_table1010
+ GCC_except_table1011
+ GCC_except_table1014
+ GCC_except_table1016
+ GCC_except_table1017
+ GCC_except_table1018
+ GCC_except_table1019
+ GCC_except_table1020
+ GCC_except_table1021
+ GCC_except_table1039
+ GCC_except_table1040
+ GCC_except_table1041
+ GCC_except_table1042
+ GCC_except_table1043
+ GCC_except_table1052
+ GCC_except_table1059
+ GCC_except_table1060
+ GCC_except_table1061
+ GCC_except_table1062
+ GCC_except_table1063
+ GCC_except_table1064
+ GCC_except_table1065
+ GCC_except_table1088
+ GCC_except_table1096
+ GCC_except_table1097
+ GCC_except_table1101
+ GCC_except_table1104
+ GCC_except_table1105
+ GCC_except_table1114
+ GCC_except_table1121
+ GCC_except_table1126
+ GCC_except_table1129
+ GCC_except_table1133
+ GCC_except_table1134
+ GCC_except_table1139
+ GCC_except_table1142
+ GCC_except_table1144
+ GCC_except_table1145
+ GCC_except_table1154
+ GCC_except_table1155
+ GCC_except_table1162
+ GCC_except_table1177
+ GCC_except_table1178
+ GCC_except_table1179
+ GCC_except_table1183
+ GCC_except_table1184
+ GCC_except_table1186
+ GCC_except_table1187
+ GCC_except_table1195
+ GCC_except_table1196
+ GCC_except_table1234
+ GCC_except_table1236
+ GCC_except_table1237
+ GCC_except_table1241
+ GCC_except_table1243
+ GCC_except_table1244
+ GCC_except_table1256
+ GCC_except_table1259
+ GCC_except_table1260
+ GCC_except_table1264
+ GCC_except_table1276
+ GCC_except_table1277
+ GCC_except_table1279
+ GCC_except_table1280
+ GCC_except_table1281
+ GCC_except_table1282
+ GCC_except_table1299
+ GCC_except_table1300
+ GCC_except_table1302
+ GCC_except_table1303
+ GCC_except_table1304
+ GCC_except_table1305
+ GCC_except_table1306
+ GCC_except_table1307
+ GCC_except_table1308
+ GCC_except_table1309
+ GCC_except_table1310
+ GCC_except_table1311
+ GCC_except_table1312
+ GCC_except_table1346
+ GCC_except_table1350
+ GCC_except_table1351
+ GCC_except_table1352
+ GCC_except_table1357
+ GCC_except_table1358
+ GCC_except_table1359
+ GCC_except_table1360
+ GCC_except_table1362
+ GCC_except_table1368
+ GCC_except_table1374
+ GCC_except_table1387
+ GCC_except_table1408
+ GCC_except_table1409
+ GCC_except_table1423
+ GCC_except_table1424
+ GCC_except_table1425
+ GCC_except_table1426
+ GCC_except_table1430
+ GCC_except_table1433
+ GCC_except_table1435
+ GCC_except_table1442
+ GCC_except_table1443
+ GCC_except_table1458
+ GCC_except_table1470
+ GCC_except_table1472
+ GCC_except_table1473
+ GCC_except_table1474
+ GCC_except_table1475
+ GCC_except_table1476
+ GCC_except_table1478
+ GCC_except_table1483
+ GCC_except_table1485
+ GCC_except_table1628
+ GCC_except_table1665
+ GCC_except_table1667
+ GCC_except_table1676
+ GCC_except_table1679
+ GCC_except_table1689
+ GCC_except_table1692
+ GCC_except_table1694
+ GCC_except_table1695
+ GCC_except_table1698
+ GCC_except_table1699
+ GCC_except_table1704
+ GCC_except_table1708
+ GCC_except_table1709
+ GCC_except_table1711
+ GCC_except_table1712
+ GCC_except_table1714
+ GCC_except_table1721
+ GCC_except_table1722
+ GCC_except_table1723
+ GCC_except_table1724
+ GCC_except_table1725
+ GCC_except_table1763
+ GCC_except_table1764
+ GCC_except_table1767
+ GCC_except_table1770
+ GCC_except_table1778
+ GCC_except_table1779
+ GCC_except_table1784
+ GCC_except_table1799
+ GCC_except_table1800
+ GCC_except_table1806
+ GCC_except_table1807
+ GCC_except_table1866
+ GCC_except_table1876
+ GCC_except_table1884
+ GCC_except_table1888
+ GCC_except_table1896
+ GCC_except_table1897
+ GCC_except_table1898
+ GCC_except_table1899
+ GCC_except_table1901
+ GCC_except_table1906
+ GCC_except_table1908
+ GCC_except_table1913
+ GCC_except_table1915
+ GCC_except_table1916
+ GCC_except_table1917
+ GCC_except_table1928
+ GCC_except_table1929
+ GCC_except_table1937
+ GCC_except_table1955
+ GCC_except_table1958
+ GCC_except_table1959
+ GCC_except_table1960
+ GCC_except_table1969
+ GCC_except_table1972
+ GCC_except_table1973
+ GCC_except_table1974
+ GCC_except_table1975
+ GCC_except_table1977
+ GCC_except_table1978
+ GCC_except_table1979
+ GCC_except_table1980
+ GCC_except_table1982
+ GCC_except_table1983
+ GCC_except_table1984
+ GCC_except_table1987
+ GCC_except_table1988
+ GCC_except_table2021
+ GCC_except_table2025
+ GCC_except_table2026
+ GCC_except_table2027
+ GCC_except_table2028
+ GCC_except_table2029
+ GCC_except_table2030
+ GCC_except_table2031
+ GCC_except_table2036
+ GCC_except_table2037
+ GCC_except_table2050
+ GCC_except_table2051
+ GCC_except_table2073
+ GCC_except_table2074
+ GCC_except_table2080
+ GCC_except_table2081
+ GCC_except_table2084
+ GCC_except_table2087
+ GCC_except_table2089
+ GCC_except_table2093
+ GCC_except_table2095
+ GCC_except_table2097
+ GCC_except_table2117
+ GCC_except_table2118
+ GCC_except_table2126
+ GCC_except_table2127
+ GCC_except_table2192
+ GCC_except_table2193
+ GCC_except_table2211
+ GCC_except_table2216
+ GCC_except_table2225
+ GCC_except_table2236
+ GCC_except_table2237
+ GCC_except_table2238
+ GCC_except_table2244
+ GCC_except_table2269
+ GCC_except_table2276
+ GCC_except_table2278
+ GCC_except_table2280
+ GCC_except_table2281
+ GCC_except_table2285
+ GCC_except_table2286
+ GCC_except_table2288
+ GCC_except_table2289
+ GCC_except_table2291
+ GCC_except_table2293
+ GCC_except_table2294
+ GCC_except_table2295
+ GCC_except_table2298
+ GCC_except_table2308
+ GCC_except_table2310
+ GCC_except_table2317
+ GCC_except_table2321
+ GCC_except_table2331
+ GCC_except_table2346
+ GCC_except_table2349
+ GCC_except_table2351
+ GCC_except_table2365
+ GCC_except_table2369
+ GCC_except_table2375
+ GCC_except_table2378
+ GCC_except_table2381
+ GCC_except_table2382
+ GCC_except_table2383
+ GCC_except_table2389
+ GCC_except_table2395
+ GCC_except_table2396
+ GCC_except_table2402
+ GCC_except_table2404
+ GCC_except_table2405
+ GCC_except_table2406
+ GCC_except_table2408
+ GCC_except_table2412
+ GCC_except_table2438
+ GCC_except_table2439
+ GCC_except_table2440
+ GCC_except_table2447
+ GCC_except_table2459
+ GCC_except_table2463
+ GCC_except_table2469
+ GCC_except_table2470
+ GCC_except_table2471
+ GCC_except_table2478
+ GCC_except_table2487
+ GCC_except_table2493
+ GCC_except_table2494
+ GCC_except_table2496
+ GCC_except_table2497
+ GCC_except_table2498
+ GCC_except_table2501
+ GCC_except_table2502
+ GCC_except_table2507
+ GCC_except_table2508
+ GCC_except_table2509
+ GCC_except_table2510
+ GCC_except_table2512
+ GCC_except_table2513
+ GCC_except_table2514
+ GCC_except_table2516
+ GCC_except_table2517
+ GCC_except_table2519
+ GCC_except_table2520
+ GCC_except_table2526
+ GCC_except_table2529
+ GCC_except_table2535
+ GCC_except_table2538
+ GCC_except_table2541
+ GCC_except_table2544
+ GCC_except_table2547
+ GCC_except_table2552
+ GCC_except_table2594
+ GCC_except_table2601
+ GCC_except_table2605
+ GCC_except_table2613
+ GCC_except_table2616
+ GCC_except_table2617
+ GCC_except_table2623
+ GCC_except_table2624
+ GCC_except_table2625
+ GCC_except_table2632
+ GCC_except_table2655
+ GCC_except_table2656
+ GCC_except_table2659
+ GCC_except_table2660
+ GCC_except_table2661
+ GCC_except_table2663
+ GCC_except_table2666
+ GCC_except_table2671
+ GCC_except_table2672
+ GCC_except_table2673
+ GCC_except_table2674
+ GCC_except_table2680
+ GCC_except_table2688
+ GCC_except_table2689
+ GCC_except_table2699
+ GCC_except_table2703
+ GCC_except_table2706
+ GCC_except_table2742
+ GCC_except_table2745
+ GCC_except_table2748
+ GCC_except_table2772
+ GCC_except_table2789
+ GCC_except_table2790
+ GCC_except_table2792
+ GCC_except_table2793
+ GCC_except_table2795
+ GCC_except_table2796
+ GCC_except_table2798
+ GCC_except_table2799
+ GCC_except_table2801
+ GCC_except_table2802
+ GCC_except_table2804
+ GCC_except_table2814
+ GCC_except_table2815
+ GCC_except_table2816
+ GCC_except_table2818
+ GCC_except_table2819
+ GCC_except_table2826
+ GCC_except_table2827
+ GCC_except_table2831
+ GCC_except_table2834
+ GCC_except_table2837
+ GCC_except_table2838
+ GCC_except_table2839
+ GCC_except_table2843
+ GCC_except_table2859
+ GCC_except_table2869
+ GCC_except_table2875
+ GCC_except_table2876
+ GCC_except_table2884
+ GCC_except_table2885
+ GCC_except_table2894
+ GCC_except_table2898
+ GCC_except_table2899
+ GCC_except_table2902
+ GCC_except_table2904
+ GCC_except_table2914
+ GCC_except_table2915
+ GCC_except_table2916
+ GCC_except_table2917
+ GCC_except_table2918
+ GCC_except_table2920
+ GCC_except_table2922
+ GCC_except_table2924
+ GCC_except_table2925
+ GCC_except_table2926
+ GCC_except_table2933
+ GCC_except_table2948
+ GCC_except_table2949
+ GCC_except_table2952
+ GCC_except_table2961
+ GCC_except_table2962
+ GCC_except_table2963
+ GCC_except_table2964
+ GCC_except_table2986
+ GCC_except_table2988
+ GCC_except_table2989
+ GCC_except_table2990
+ GCC_except_table2992
+ GCC_except_table2994
+ GCC_except_table3002
+ GCC_except_table3004
+ GCC_except_table3005
+ GCC_except_table3016
+ GCC_except_table3034
+ GCC_except_table3035
+ GCC_except_table3037
+ GCC_except_table3038
+ GCC_except_table3041
+ GCC_except_table3042
+ GCC_except_table3045
+ GCC_except_table3049
+ GCC_except_table3051
+ GCC_except_table3069
+ GCC_except_table3070
+ GCC_except_table3071
+ GCC_except_table3072
+ GCC_except_table3073
+ GCC_except_table3078
+ GCC_except_table3081
+ GCC_except_table3094
+ GCC_except_table3110
+ GCC_except_table3111
+ GCC_except_table3113
+ GCC_except_table3114
+ GCC_except_table3118
+ GCC_except_table3121
+ GCC_except_table3124
+ GCC_except_table3146
+ GCC_except_table3153
+ GCC_except_table3154
+ GCC_except_table3159
+ GCC_except_table3163
+ GCC_except_table3194
+ GCC_except_table3200
+ GCC_except_table3207
+ GCC_except_table3209
+ GCC_except_table3218
+ GCC_except_table3227
+ GCC_except_table3228
+ GCC_except_table3229
+ GCC_except_table3237
+ GCC_except_table3241
+ GCC_except_table3243
+ GCC_except_table3245
+ GCC_except_table3250
+ GCC_except_table3251
+ GCC_except_table3259
+ GCC_except_table3264
+ GCC_except_table3266
+ GCC_except_table3273
+ GCC_except_table3277
+ GCC_except_table3278
+ GCC_except_table3279
+ GCC_except_table3280
+ GCC_except_table3281
+ GCC_except_table3282
+ GCC_except_table3284
+ GCC_except_table3291
+ GCC_except_table3292
+ GCC_except_table3293
+ GCC_except_table3297
+ GCC_except_table3300
+ GCC_except_table3305
+ GCC_except_table3312
+ GCC_except_table3315
+ GCC_except_table3316
+ GCC_except_table3318
+ GCC_except_table3320
+ GCC_except_table3321
+ GCC_except_table3322
+ GCC_except_table3323
+ GCC_except_table3329
+ GCC_except_table3330
+ GCC_except_table3343
+ GCC_except_table3346
+ GCC_except_table3347
+ GCC_except_table3355
+ GCC_except_table3358
+ GCC_except_table3368
+ GCC_except_table3369
+ GCC_except_table3373
+ GCC_except_table3387
+ GCC_except_table3388
+ GCC_except_table3391
+ GCC_except_table3392
+ GCC_except_table3396
+ GCC_except_table3397
+ GCC_except_table3398
+ GCC_except_table3413
+ GCC_except_table3415
+ GCC_except_table3428
+ GCC_except_table3436
+ GCC_except_table3437
+ GCC_except_table3445
+ GCC_except_table3454
+ GCC_except_table3455
+ GCC_except_table3460
+ GCC_except_table3461
+ GCC_except_table3462
+ GCC_except_table3463
+ GCC_except_table3464
+ GCC_except_table3468
+ GCC_except_table3469
+ GCC_except_table3470
+ GCC_except_table3471
+ GCC_except_table3472
+ GCC_except_table3473
+ GCC_except_table3475
+ GCC_except_table3478
+ GCC_except_table3479
+ GCC_except_table3480
+ GCC_except_table3481
+ GCC_except_table3482
+ GCC_except_table3483
+ GCC_except_table3487
+ GCC_except_table379
+ GCC_except_table384
+ GCC_except_table389
+ GCC_except_table392
+ GCC_except_table393
+ GCC_except_table394
+ GCC_except_table426
+ GCC_except_table430
+ GCC_except_table431
+ GCC_except_table434
+ GCC_except_table445
+ GCC_except_table446
+ GCC_except_table450
+ GCC_except_table453
+ GCC_except_table454
+ GCC_except_table455
+ GCC_except_table472
+ GCC_except_table515
+ GCC_except_table516
+ GCC_except_table517
+ GCC_except_table518
+ GCC_except_table519
+ GCC_except_table538
+ GCC_except_table539
+ GCC_except_table541
+ GCC_except_table542
+ GCC_except_table543
+ GCC_except_table546
+ GCC_except_table564
+ GCC_except_table565
+ GCC_except_table566
+ GCC_except_table567
+ GCC_except_table591
+ GCC_except_table613
+ GCC_except_table614
+ GCC_except_table615
+ GCC_except_table617
+ GCC_except_table618
+ GCC_except_table628
+ GCC_except_table645
+ GCC_except_table646
+ GCC_except_table650
+ GCC_except_table661
+ GCC_except_table662
+ GCC_except_table664
+ GCC_except_table666
+ GCC_except_table683
+ GCC_except_table692
+ GCC_except_table693
+ GCC_except_table696
+ GCC_except_table710
+ GCC_except_table711
+ GCC_except_table712
+ GCC_except_table713
+ GCC_except_table729
+ GCC_except_table730
+ GCC_except_table753
+ GCC_except_table754
+ GCC_except_table755
+ GCC_except_table758
+ GCC_except_table759
+ GCC_except_table760
+ GCC_except_table761
+ GCC_except_table762
+ GCC_except_table763
+ GCC_except_table764
+ GCC_except_table765
+ GCC_except_table784
+ GCC_except_table786
+ GCC_except_table794
+ GCC_except_table797
+ GCC_except_table803
+ GCC_except_table810
+ GCC_except_table827
+ GCC_except_table829
+ GCC_except_table830
+ GCC_except_table831
+ GCC_except_table832
+ GCC_except_table834
+ GCC_except_table835
+ GCC_except_table838
+ GCC_except_table839
+ GCC_except_table847
+ GCC_except_table865
+ GCC_except_table868
+ GCC_except_table869
+ GCC_except_table870
+ GCC_except_table871
+ GCC_except_table872
+ GCC_except_table874
+ GCC_except_table875
+ GCC_except_table876
+ GCC_except_table878
+ GCC_except_table932
+ GCC_except_table940
+ GCC_except_table941
+ GCC_except_table942
+ GCC_except_table943
+ GCC_except_table944
+ GCC_except_table947
+ GCC_except_table948
+ GCC_except_table981
+ GCC_except_table982
+ GCC_except_table998
+ GCC_except_table999
+ _OBJC_CLASS_$_ADJasperColorStillsFlow
+ _OBJC_CLASS_$_ADJasperColorV2Flow
+ _OBJC_CLASS_$_ADMonocularStillsFlow
+ _OBJC_CLASS_$_ADPCEDisparityColorFlow
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_IVAR_$_ADDeviceConfiguration._verboseLogs
+ _OBJC_IVAR_$_ADExecutor._executorName
+ _OBJC_IVAR_$_ADFlowFrameInput._depth
+ _OBJC_IVAR_$_ADJasperColorStillsFlow._executor
+ _OBJC_IVAR_$_ADJasperColorStillsFlow._preAllocatedOutputBuffer
+ _OBJC_IVAR_$_ADJasperColorStillsFlow._streamSync
+ _OBJC_IVAR_$_ADJasperColorV2Flow._aggregationCount
+ _OBJC_IVAR_$_ADJasperColorV2Flow._executor
+ _OBJC_IVAR_$_ADJasperColorV2Flow._preAllocatedConfidenceOutputBuffer
+ _OBJC_IVAR_$_ADJasperColorV2Flow._preAllocatedDepthOutputBuffer
+ _OBJC_IVAR_$_ADJasperColorV2Flow._streamSync
+ _OBJC_IVAR_$_ADMonocularStillsFlow._executor
+ _OBJC_IVAR_$_ADMonocularVideoPipeline._eflScaleFactor
+ _OBJC_IVAR_$_ADMonocularVideoPipeline._nominalResolutionFactor
+ _OBJC_IVAR_$_ADMonocularVideoPipelineParameters._networkVariant
+ _OBJC_IVAR_$_ADPCEDisparityColorFlow._canDelegateFailure
+ _OBJC_IVAR_$_ADPCEDisparityColorFlow._canDelegateProcess
+ _OBJC_IVAR_$_ADPCEDisparityColorFlow._delegate
+ _OBJC_IVAR_$_ADPCEDisparityColorFlow._executor
+ _OBJC_IVAR_$_ADPCEDisparityColorFlow._streamSync
+ _OBJC_METACLASS_$_ADJasperColorStillsFlow
+ _OBJC_METACLASS_$_ADJasperColorV2Flow
+ _OBJC_METACLASS_$_ADMonocularStillsFlow
+ _OBJC_METACLASS_$_ADPCEDisparityColorFlow
+ __OBJC_$_INSTANCE_METHODS_ADJasperColorStillsFlow
+ __OBJC_$_INSTANCE_METHODS_ADJasperColorV2Flow
+ __OBJC_$_INSTANCE_METHODS_ADMonocularStillsFlow
+ __OBJC_$_INSTANCE_METHODS_ADMonocularVideoPipelineParameters
+ __OBJC_$_INSTANCE_METHODS_ADPCEDisparityColorFlow
+ __OBJC_$_INSTANCE_VARIABLES_ADDeviceConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_ADJasperColorStillsFlow
+ __OBJC_$_INSTANCE_VARIABLES_ADJasperColorV2Flow
+ __OBJC_$_INSTANCE_VARIABLES_ADMonocularStillsFlow
+ __OBJC_$_INSTANCE_VARIABLES_ADMonocularVideoPipelineParameters
+ __OBJC_$_INSTANCE_VARIABLES_ADPCEDisparityColorFlow
+ __OBJC_$_PROP_LIST_ADJasperColorStillsFlow
+ __OBJC_$_PROP_LIST_ADJasperColorV2Flow
+ __OBJC_$_PROP_LIST_ADMonocularStillsFlow
+ __OBJC_$_PROP_LIST_ADMonocularVideoPipelineParameters
+ __OBJC_$_PROP_LIST_ADPCEDisparityColorFlow
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ADFlowDepthConsumer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ADFlowDepthConsumer
+ __OBJC_$_PROTOCOL_REFS_ADFlowDepthConsumer
+ __OBJC_CLASS_PROTOCOLS_$_ADJasperColorStillsFlow
+ __OBJC_CLASS_PROTOCOLS_$_ADJasperColorV2Flow
+ __OBJC_CLASS_PROTOCOLS_$_ADMonocularStillsFlow
+ __OBJC_CLASS_PROTOCOLS_$_ADPCEDisparityColorFlow
+ __OBJC_CLASS_RO_$_ADJasperColorStillsFlow
+ __OBJC_CLASS_RO_$_ADJasperColorV2Flow
+ __OBJC_CLASS_RO_$_ADMonocularStillsFlow
+ __OBJC_CLASS_RO_$_ADPCEDisparityColorFlow
+ __OBJC_LABEL_PROTOCOL_$_ADFlowDepthConsumer
+ __OBJC_METACLASS_RO_$_ADJasperColorStillsFlow
+ __OBJC_METACLASS_RO_$_ADJasperColorV2Flow
+ __OBJC_METACLASS_RO_$_ADMonocularStillsFlow
+ __OBJC_METACLASS_RO_$_ADPCEDisparityColorFlow
+ __OBJC_PROTOCOL_$_ADFlowDepthConsumer
+ __PromotedConst.10939
+ __PromotedConst.10940
+ __ZL15INSTRUMENTS_ENDjyyyy.10437
+ __ZL15INSTRUMENTS_ENDjyyyy.10503
+ __ZL15INSTRUMENTS_ENDjyyyy.10686
+ __ZL15INSTRUMENTS_ENDjyyyy.1086
+ __ZL15INSTRUMENTS_ENDjyyyy.10905
+ __ZL15INSTRUMENTS_ENDjyyyy.1219
+ __ZL15INSTRUMENTS_ENDjyyyy.1281
+ __ZL15INSTRUMENTS_ENDjyyyy.1510
+ __ZL15INSTRUMENTS_ENDjyyyy.1617
+ __ZL15INSTRUMENTS_ENDjyyyy.1828
+ __ZL15INSTRUMENTS_ENDjyyyy.1860
+ __ZL15INSTRUMENTS_ENDjyyyy.2027
+ __ZL15INSTRUMENTS_ENDjyyyy.2216
+ __ZL15INSTRUMENTS_ENDjyyyy.245
+ __ZL15INSTRUMENTS_ENDjyyyy.2463
+ __ZL15INSTRUMENTS_ENDjyyyy.251
+ __ZL15INSTRUMENTS_ENDjyyyy.262
+ __ZL15INSTRUMENTS_ENDjyyyy.2675
+ __ZL15INSTRUMENTS_ENDjyyyy.2750
+ __ZL15INSTRUMENTS_ENDjyyyy.2798
+ __ZL15INSTRUMENTS_ENDjyyyy.2885
+ __ZL15INSTRUMENTS_ENDjyyyy.2918
+ __ZL15INSTRUMENTS_ENDjyyyy.2925
+ __ZL15INSTRUMENTS_ENDjyyyy.3125
+ __ZL15INSTRUMENTS_ENDjyyyy.3201
+ __ZL15INSTRUMENTS_ENDjyyyy.332
+ __ZL15INSTRUMENTS_ENDjyyyy.3439
+ __ZL15INSTRUMENTS_ENDjyyyy.3561
+ __ZL15INSTRUMENTS_ENDjyyyy.3577
+ __ZL15INSTRUMENTS_ENDjyyyy.3583
+ __ZL15INSTRUMENTS_ENDjyyyy.3833
+ __ZL15INSTRUMENTS_ENDjyyyy.4032
+ __ZL15INSTRUMENTS_ENDjyyyy.4042
+ __ZL15INSTRUMENTS_ENDjyyyy.4104
+ __ZL15INSTRUMENTS_ENDjyyyy.4293
+ __ZL15INSTRUMENTS_ENDjyyyy.4354
+ __ZL15INSTRUMENTS_ENDjyyyy.4536
+ __ZL15INSTRUMENTS_ENDjyyyy.458
+ __ZL15INSTRUMENTS_ENDjyyyy.4906
+ __ZL15INSTRUMENTS_ENDjyyyy.5121
+ __ZL15INSTRUMENTS_ENDjyyyy.5303
+ __ZL15INSTRUMENTS_ENDjyyyy.544
+ __ZL15INSTRUMENTS_ENDjyyyy.5527
+ __ZL15INSTRUMENTS_ENDjyyyy.6001
+ __ZL15INSTRUMENTS_ENDjyyyy.6149
+ __ZL15INSTRUMENTS_ENDjyyyy.6253
+ __ZL15INSTRUMENTS_ENDjyyyy.6485
+ __ZL15INSTRUMENTS_ENDjyyyy.6824
+ __ZL15INSTRUMENTS_ENDjyyyy.700
+ __ZL15INSTRUMENTS_ENDjyyyy.7100
+ __ZL15INSTRUMENTS_ENDjyyyy.714
+ __ZL15INSTRUMENTS_ENDjyyyy.7286
+ __ZL15INSTRUMENTS_ENDjyyyy.7402
+ __ZL15INSTRUMENTS_ENDjyyyy.7425
+ __ZL15INSTRUMENTS_ENDjyyyy.7613
+ __ZL15INSTRUMENTS_ENDjyyyy.7619
+ __ZL15INSTRUMENTS_ENDjyyyy.7755
+ __ZL15INSTRUMENTS_ENDjyyyy.7778
+ __ZL15INSTRUMENTS_ENDjyyyy.7803
+ __ZL15INSTRUMENTS_ENDjyyyy.8003
+ __ZL15INSTRUMENTS_ENDjyyyy.8261
+ __ZL15INSTRUMENTS_ENDjyyyy.8302
+ __ZL15INSTRUMENTS_ENDjyyyy.8351
+ __ZL15INSTRUMENTS_ENDjyyyy.8462
+ __ZL15INSTRUMENTS_ENDjyyyy.8621
+ __ZL15INSTRUMENTS_ENDjyyyy.8808
+ __ZL15INSTRUMENTS_ENDjyyyy.8814
+ __ZL15INSTRUMENTS_ENDjyyyy.8873
+ __ZL15INSTRUMENTS_ENDjyyyy.8884
+ __ZL15INSTRUMENTS_ENDjyyyy.9036
+ __ZL15INSTRUMENTS_ENDjyyyy.9441
+ __ZL15INSTRUMENTS_ENDjyyyy.9468
+ __ZL15INSTRUMENTS_ENDjyyyy.9640
+ __ZL15INSTRUMENTS_ENDjyyyy.9666
+ __ZL15INSTRUMENTS_ENDjyyyy.968
+ __ZL15INSTRUMENTS_ENDjyyyy.9915
+ __ZL17INSTRUMENTS_EVENTjyyyy.10438
+ __ZL17INSTRUMENTS_EVENTjyyyy.10504
+ __ZL17INSTRUMENTS_EVENTjyyyy.10687
+ __ZL17INSTRUMENTS_EVENTjyyyy.1087
+ __ZL17INSTRUMENTS_EVENTjyyyy.10906
+ __ZL17INSTRUMENTS_EVENTjyyyy.1220
+ __ZL17INSTRUMENTS_EVENTjyyyy.1282
+ __ZL17INSTRUMENTS_EVENTjyyyy.1511
+ __ZL17INSTRUMENTS_EVENTjyyyy.1618
+ __ZL17INSTRUMENTS_EVENTjyyyy.1829
+ __ZL17INSTRUMENTS_EVENTjyyyy.1861
+ __ZL17INSTRUMENTS_EVENTjyyyy.2028
+ __ZL17INSTRUMENTS_EVENTjyyyy.2217
+ __ZL17INSTRUMENTS_EVENTjyyyy.246
+ __ZL17INSTRUMENTS_EVENTjyyyy.2464
+ __ZL17INSTRUMENTS_EVENTjyyyy.252
+ __ZL17INSTRUMENTS_EVENTjyyyy.263
+ __ZL17INSTRUMENTS_EVENTjyyyy.2676
+ __ZL17INSTRUMENTS_EVENTjyyyy.2751
+ __ZL17INSTRUMENTS_EVENTjyyyy.2799
+ __ZL17INSTRUMENTS_EVENTjyyyy.2886
+ __ZL17INSTRUMENTS_EVENTjyyyy.2919
+ __ZL17INSTRUMENTS_EVENTjyyyy.2926
+ __ZL17INSTRUMENTS_EVENTjyyyy.3126
+ __ZL17INSTRUMENTS_EVENTjyyyy.3202
+ __ZL17INSTRUMENTS_EVENTjyyyy.333
+ __ZL17INSTRUMENTS_EVENTjyyyy.3440
+ __ZL17INSTRUMENTS_EVENTjyyyy.3562
+ __ZL17INSTRUMENTS_EVENTjyyyy.3578
+ __ZL17INSTRUMENTS_EVENTjyyyy.3584
+ __ZL17INSTRUMENTS_EVENTjyyyy.3834
+ __ZL17INSTRUMENTS_EVENTjyyyy.4033
+ __ZL17INSTRUMENTS_EVENTjyyyy.4043
+ __ZL17INSTRUMENTS_EVENTjyyyy.4105
+ __ZL17INSTRUMENTS_EVENTjyyyy.4294
+ __ZL17INSTRUMENTS_EVENTjyyyy.4355
+ __ZL17INSTRUMENTS_EVENTjyyyy.4537
+ __ZL17INSTRUMENTS_EVENTjyyyy.459
+ __ZL17INSTRUMENTS_EVENTjyyyy.4907
+ __ZL17INSTRUMENTS_EVENTjyyyy.5122
+ __ZL17INSTRUMENTS_EVENTjyyyy.5304
+ __ZL17INSTRUMENTS_EVENTjyyyy.545
+ __ZL17INSTRUMENTS_EVENTjyyyy.5528
+ __ZL17INSTRUMENTS_EVENTjyyyy.6002
+ __ZL17INSTRUMENTS_EVENTjyyyy.6150
+ __ZL17INSTRUMENTS_EVENTjyyyy.6254
+ __ZL17INSTRUMENTS_EVENTjyyyy.6486
+ __ZL17INSTRUMENTS_EVENTjyyyy.6825
+ __ZL17INSTRUMENTS_EVENTjyyyy.701
+ __ZL17INSTRUMENTS_EVENTjyyyy.7101
+ __ZL17INSTRUMENTS_EVENTjyyyy.715
+ __ZL17INSTRUMENTS_EVENTjyyyy.7287
+ __ZL17INSTRUMENTS_EVENTjyyyy.7403
+ __ZL17INSTRUMENTS_EVENTjyyyy.7426
+ __ZL17INSTRUMENTS_EVENTjyyyy.7614
+ __ZL17INSTRUMENTS_EVENTjyyyy.7620
+ __ZL17INSTRUMENTS_EVENTjyyyy.7756
+ __ZL17INSTRUMENTS_EVENTjyyyy.7779
+ __ZL17INSTRUMENTS_EVENTjyyyy.7804
+ __ZL17INSTRUMENTS_EVENTjyyyy.8004
+ __ZL17INSTRUMENTS_EVENTjyyyy.8262
+ __ZL17INSTRUMENTS_EVENTjyyyy.8303
+ __ZL17INSTRUMENTS_EVENTjyyyy.8352
+ __ZL17INSTRUMENTS_EVENTjyyyy.8463
+ __ZL17INSTRUMENTS_EVENTjyyyy.8622
+ __ZL17INSTRUMENTS_EVENTjyyyy.8809
+ __ZL17INSTRUMENTS_EVENTjyyyy.8815
+ __ZL17INSTRUMENTS_EVENTjyyyy.8874
+ __ZL17INSTRUMENTS_EVENTjyyyy.8885
+ __ZL17INSTRUMENTS_EVENTjyyyy.9037
+ __ZL17INSTRUMENTS_EVENTjyyyy.9442
+ __ZL17INSTRUMENTS_EVENTjyyyy.9469
+ __ZL17INSTRUMENTS_EVENTjyyyy.9641
+ __ZL17INSTRUMENTS_EVENTjyyyy.9667
+ __ZL17INSTRUMENTS_EVENTjyyyy.969
+ __ZL17INSTRUMENTS_EVENTjyyyy.9916
+ __ZL17INSTRUMENTS_STARTjyyyy.10439
+ __ZL17INSTRUMENTS_STARTjyyyy.10505
+ __ZL17INSTRUMENTS_STARTjyyyy.10688
+ __ZL17INSTRUMENTS_STARTjyyyy.1088
+ __ZL17INSTRUMENTS_STARTjyyyy.10907
+ __ZL17INSTRUMENTS_STARTjyyyy.1221
+ __ZL17INSTRUMENTS_STARTjyyyy.1283
+ __ZL17INSTRUMENTS_STARTjyyyy.1512
+ __ZL17INSTRUMENTS_STARTjyyyy.1619
+ __ZL17INSTRUMENTS_STARTjyyyy.1830
+ __ZL17INSTRUMENTS_STARTjyyyy.1862
+ __ZL17INSTRUMENTS_STARTjyyyy.2029
+ __ZL17INSTRUMENTS_STARTjyyyy.2218
+ __ZL17INSTRUMENTS_STARTjyyyy.2465
+ __ZL17INSTRUMENTS_STARTjyyyy.247
+ __ZL17INSTRUMENTS_STARTjyyyy.253
+ __ZL17INSTRUMENTS_STARTjyyyy.264
+ __ZL17INSTRUMENTS_STARTjyyyy.2677
+ __ZL17INSTRUMENTS_STARTjyyyy.2752
+ __ZL17INSTRUMENTS_STARTjyyyy.2800
+ __ZL17INSTRUMENTS_STARTjyyyy.2887
+ __ZL17INSTRUMENTS_STARTjyyyy.2920
+ __ZL17INSTRUMENTS_STARTjyyyy.2927
+ __ZL17INSTRUMENTS_STARTjyyyy.3127
+ __ZL17INSTRUMENTS_STARTjyyyy.3203
+ __ZL17INSTRUMENTS_STARTjyyyy.334
+ __ZL17INSTRUMENTS_STARTjyyyy.3441
+ __ZL17INSTRUMENTS_STARTjyyyy.3563
+ __ZL17INSTRUMENTS_STARTjyyyy.3579
+ __ZL17INSTRUMENTS_STARTjyyyy.3585
+ __ZL17INSTRUMENTS_STARTjyyyy.3835
+ __ZL17INSTRUMENTS_STARTjyyyy.4034
+ __ZL17INSTRUMENTS_STARTjyyyy.4044
+ __ZL17INSTRUMENTS_STARTjyyyy.4106
+ __ZL17INSTRUMENTS_STARTjyyyy.4295
+ __ZL17INSTRUMENTS_STARTjyyyy.4356
+ __ZL17INSTRUMENTS_STARTjyyyy.4538
+ __ZL17INSTRUMENTS_STARTjyyyy.460
+ __ZL17INSTRUMENTS_STARTjyyyy.4908
+ __ZL17INSTRUMENTS_STARTjyyyy.5123
+ __ZL17INSTRUMENTS_STARTjyyyy.5305
+ __ZL17INSTRUMENTS_STARTjyyyy.546
+ __ZL17INSTRUMENTS_STARTjyyyy.5529
+ __ZL17INSTRUMENTS_STARTjyyyy.6003
+ __ZL17INSTRUMENTS_STARTjyyyy.6151
+ __ZL17INSTRUMENTS_STARTjyyyy.6255
+ __ZL17INSTRUMENTS_STARTjyyyy.6487
+ __ZL17INSTRUMENTS_STARTjyyyy.6826
+ __ZL17INSTRUMENTS_STARTjyyyy.702
+ __ZL17INSTRUMENTS_STARTjyyyy.7102
+ __ZL17INSTRUMENTS_STARTjyyyy.716
+ __ZL17INSTRUMENTS_STARTjyyyy.7288
+ __ZL17INSTRUMENTS_STARTjyyyy.7404
+ __ZL17INSTRUMENTS_STARTjyyyy.7427
+ __ZL17INSTRUMENTS_STARTjyyyy.7615
+ __ZL17INSTRUMENTS_STARTjyyyy.7621
+ __ZL17INSTRUMENTS_STARTjyyyy.7757
+ __ZL17INSTRUMENTS_STARTjyyyy.7780
+ __ZL17INSTRUMENTS_STARTjyyyy.7805
+ __ZL17INSTRUMENTS_STARTjyyyy.8005
+ __ZL17INSTRUMENTS_STARTjyyyy.8263
+ __ZL17INSTRUMENTS_STARTjyyyy.8304
+ __ZL17INSTRUMENTS_STARTjyyyy.8353
+ __ZL17INSTRUMENTS_STARTjyyyy.8464
+ __ZL17INSTRUMENTS_STARTjyyyy.8623
+ __ZL17INSTRUMENTS_STARTjyyyy.8810
+ __ZL17INSTRUMENTS_STARTjyyyy.8816
+ __ZL17INSTRUMENTS_STARTjyyyy.8875
+ __ZL17INSTRUMENTS_STARTjyyyy.8886
+ __ZL17INSTRUMENTS_STARTjyyyy.9038
+ __ZL17INSTRUMENTS_STARTjyyyy.9443
+ __ZL17INSTRUMENTS_STARTjyyyy.9470
+ __ZL17INSTRUMENTS_STARTjyyyy.9642
+ __ZL17INSTRUMENTS_STARTjyyyy.9668
+ __ZL17INSTRUMENTS_STARTjyyyy.970
+ __ZL17INSTRUMENTS_STARTjyyyy.9917
+ __ZN13ADCommonUtils12systemUptimeEv
+ __ZN16PixelBufferUtils23pixelBufferFromBMTLFileEPKc
+ __ZN16PixelBufferUtils29pixelFormatFromMTLPixelFormatE14MTLPixelFormat
+ __ZNKSt3__110__function6__funcIZ53-[ADWorldToImageProjection initWithPose:calibration:]E3$_0FNS_6vectorI7CGPointNS_9allocatorIS4_EEEERKNS3_IDv3_fNS5_IS8_EEEEEE7__cloneEPNS0_6__baseISD_EE
+ __ZNKSt3__110__function6__funcIZ53-[ADWorldToImageProjection initWithPose:calibration:]E3$_0FNS_6vectorI7CGPointNS_9allocatorIS4_EEEERKNS3_IDv3_fNS5_IS8_EEEEEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZ92-[ADDispartiyToDepthFitEstimator estimateWithDisparity:calibration:pose:disparityTimestamp:]E3$_0FNS_6vectorI7CGPointNS_9allocatorIS4_EEEERKNS3_IDv3_fNS5_IS8_EEEEEE7__cloneEPNS0_6__baseISD_EE
+ __ZNKSt3__110__function6__funcIZ92-[ADDispartiyToDepthFitEstimator estimateWithDisparity:calibration:pose:disparityTimestamp:]E3$_0FNS_6vectorI7CGPointNS_9allocatorIS4_EEEERKNS3_IDv3_fNS5_IS8_EEEEEE7__cloneEv
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt3__110__function6__funcIZ53-[ADWorldToImageProjection initWithPose:calibration:]E3$_0FNS_6vectorI7CGPointNS_9allocatorIS4_EEEERKNS3_IDv3_fNS5_IS8_EEEEEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZ53-[ADWorldToImageProjection initWithPose:calibration:]E3$_0FNS_6vectorI7CGPointNS_9allocatorIS4_EEEERKNS3_IDv3_fNS5_IS8_EEEEEE7destroyEv
+ __ZNSt3__110__function6__funcIZ53-[ADWorldToImageProjection initWithPose:calibration:]E3$_0FNS_6vectorI7CGPointNS_9allocatorIS4_EEEERKNS3_IDv3_fNS5_IS8_EEEEEED0Ev
+ __ZNSt3__110__function6__funcIZ53-[ADWorldToImageProjection initWithPose:calibration:]E3$_0FNS_6vectorI7CGPointNS_9allocatorIS4_EEEERKNS3_IDv3_fNS5_IS8_EEEEEED1Ev
+ __ZNSt3__110__function6__funcIZ53-[ADWorldToImageProjection initWithPose:calibration:]E3$_0FNS_6vectorI7CGPointNS_9allocatorIS4_EEEERKNS3_IDv3_fNS5_IS8_EEEEEEclESC_
+ __ZNSt3__110__function6__funcIZ92-[ADDispartiyToDepthFitEstimator estimateWithDisparity:calibration:pose:disparityTimestamp:]E3$_0FNS_6vectorI7CGPointNS_9allocatorIS4_EEEERKNS3_IDv3_fNS5_IS8_EEEEEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZ92-[ADDispartiyToDepthFitEstimator estimateWithDisparity:calibration:pose:disparityTimestamp:]E3$_0FNS_6vectorI7CGPointNS_9allocatorIS4_EEEERKNS3_IDv3_fNS5_IS8_EEEEEE7destroyEv
+ __ZNSt3__110__function6__funcIZ92-[ADDispartiyToDepthFitEstimator estimateWithDisparity:calibration:pose:disparityTimestamp:]E3$_0FNS_6vectorI7CGPointNS_9allocatorIS4_EEEERKNS3_IDv3_fNS5_IS8_EEEEEED0Ev
+ __ZNSt3__110__function6__funcIZ92-[ADDispartiyToDepthFitEstimator estimateWithDisparity:calibration:pose:disparityTimestamp:]E3$_0FNS_6vectorI7CGPointNS_9allocatorIS4_EEEERKNS3_IDv3_fNS5_IS8_EEEEEED1Ev
+ __ZNSt3__110__function6__funcIZ92-[ADDispartiyToDepthFitEstimator estimateWithDisparity:calibration:pose:disparityTimestamp:]E3$_0FNS_6vectorI7CGPointNS_9allocatorIS4_EEEERKNS3_IDv3_fNS5_IS8_EEEEEEclESC_
+ __ZNSt3__110shared_ptrIN3jpc9IIFABlock9IFAOutputEED1B9foe210106Ev
+ __ZNSt3__110shared_ptrIN3jpc9IIFABlock9IFAOutputEED2B9foe210106Ev
+ __ZNSt3__110unique_ptrIN3jpc9IIFABlock9IFAOutputENS_14default_deleteIS3_EEED2B9foe210106Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIm20PixelBufferSharedPtrEEPvEENS_22__hash_node_destructorINS_9allocatorIS6_EEEEED1B9foe210106Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIm20PixelBufferSharedPtrEENS_22__unordered_map_hasherImNS_4pairIKmS2_EENS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS7_SB_S9_Lb1EEENS_9allocatorIS7_EEE25__emplace_unique_key_argsImJRKNS_21piecewise_construct_tENS_5tupleIJRS6_EEENSM_IJEEEEEENS5_INS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyNS_4pairIPhiEEEENS_22__unordered_map_hasherIyNS2_IKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS8_SC_SA_Lb1EEENS_9allocatorIS8_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyNS_4pairIPhiEEEENS_22__unordered_map_hasherIyNS2_IKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS8_SC_SA_Lb1EEENS_9allocatorIS8_EEE25__emplace_unique_key_argsIyJRKNS_21piecewise_construct_tENS_5tupleIJOyEEENSN_IJEEEEEENS2_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyNS_4pairIPhiEEEENS_22__unordered_map_hasherIyNS2_IKyS4_EENS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS8_SC_SA_Lb1EEENS_9allocatorIS8_EEED2Ev
+ __ZNSt3__112__tuple_implINS_15__tuple_indicesIJLm0ELm1ELm2ELm3ELm4ELm5EEEEJbffNS_6vectorIfNS_9allocatorIfEEEES6_NS3_I31ADDisparityToDepthFitWorldPointNS4_IS7_EEEEEEC2B9foe210106IJLm0ELm1ELm2ELm3ELm4ELm5EEJbffS6_S6_S9_EJEJEJbiiRS6_SC_RKS9_EEENS1_IJXspT_EEEENS_13__tuple_typesIJDpT0_EEENS1_IJXspT1_EEEENSG_IJDpT2_EEEDpOT3_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__113__nth_elementB9foe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_11__wrap_iterIPfEEEEvT1_S8_S8_T0_
+ __ZNSt3__113unordered_setIiNS_4hashIiEENS_8equal_toIiEENS_9allocatorIiEEED1B9foe210106Ev
+ __ZNSt3__113unordered_setImNS_4hashImEENS_8equal_toImEENS_9allocatorImEEED1B9foe210106Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB9foe210106Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9foe210106Ev
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZNSt3__124__put_character_sequenceB9foe210106IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__125__throw_bad_function_callB9foe210106Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_6vectorI11MatrixNxPtsILj1EdENS_9allocatorIS3_EEE16__destroy_vectorEED2B9foe210106Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_6vectorINS1_IiNS_9allocatorIiEEEENS2_IS4_EEE16__destroy_vectorEED2B9foe210106Ev
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__16vectorI11MatrixNxPtsILj1EdENS_9allocatorIS2_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorI31ADDisparityToDepthFitWorldPointNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorI7CGPointNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIDv3_fNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIN3jpc18IPreprocessorBlock19PearlCorrespondenceENS_9allocatorIS3_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIN3jpc18IPreprocessorBlock25PearlJasperCorrespondenceENS_9allocatorIS3_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIN3jpc9IIFABlock22IFAPearlCorrespondenceENS_9allocatorIS3_EEE18__assign_with_sizeB9foe210106IPS3_S8_EEvT_T0_l
+ __ZNSt3__16vectorIN3jpc9IIFABlock22IFAPearlCorrespondenceENS_9allocatorIS3_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIN3jpc9IIFABlock28IFAPearlJasperCorrespondenceENS_9allocatorIS3_EEE18__assign_with_sizeB9foe210106IPS3_S8_EEvT_T0_l
+ __ZNSt3__16vectorIN3jpc9IIFABlock28IFAPearlJasperCorrespondenceENS_9allocatorIS3_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEED1B9foe210106Ev
+ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEED2B9foe210106Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN3jpc11IIFA_FilterENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN3jpc11IIFA_FilterENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEED2B9foe210106Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN3jpc15IFAPullCriteriaENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN3jpc15IFAPullCriteriaENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEED2B9foe210106Ev
+ __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEED2B9foe210106Ev
+ __ZNSt3__16vectorIbNS_9allocatorIbEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB9foe210106IPfS5_EEvT_T0_l
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE9push_backB9foe210106EOi
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorItNS_9allocatorItEEE20__throw_length_errorB9foe210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ __ZTVNSt3__110__function6__funcIZ53-[ADWorldToImageProjection initWithPose:calibration:]E3$_0FNS_6vectorI7CGPointNS_9allocatorIS4_EEEERKNS3_IDv3_fNS5_IS8_EEEEEEE
+ __ZTVNSt3__110__function6__funcIZ92-[ADDispartiyToDepthFitEstimator estimateWithDisparity:calibration:pose:disparityTimestamp:]E3$_0FNS_6vectorI7CGPointNS_9allocatorIS4_EEEERKNS3_IDv3_fNS5_IS8_EEEEEEE
+ __ZZ33+[ADLKTOpticalFlow defaultConfig]E4once
+ __ZZ37+[ADLKTOpticalFlow highQualityConfig]E4once
+ __ZZ41+[ADLKTOpticalFlow highPerformanceConfig]E4once
+ ___33+[ADLKTOpticalFlow defaultConfig]_block_invoke
+ ___37+[ADLKTOpticalFlow highQualityConfig]_block_invoke
+ ___41+[ADLKTOpticalFlow highPerformanceConfig]_block_invoke
+ ___block_literal_global.10010
+ ___block_literal_global.132
+ ___block_literal_global.134
+ ___block_literal_global.270
+ ___block_literal_global.272
+ ___block_literal_global.274
+ ___block_literal_global.5084
+ ___block_literal_global.7374
+ ___block_literal_global.7994
+ _objc_msgSend$_initializeBaseConfig:
+ _objc_msgSend$createDepthBuffer
+ _objc_msgSend$dataWithContentsOfURL:
+ _objc_msgSend$executeWithColor:cameraCalibration:outDisparityMap:
+ _objc_msgSend$executeWithColor:focalLength35mm:outDisparityMap:
+ _objc_msgSend$executeWithColor:pointCloud:jasperCalibration:colorCalibration:timestamp:outputDepthMap:outputConfidenceMap:
+ _objc_msgSend$executeWithColor:scaleFactor:outDisparityMap:
+ _objc_msgSend$executeWithDisparity:depthMetadata:color:outDisparity:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$getFocalLength35mm
+ _objc_msgSend$getMetricScaleFactorFor35mmFocalLength:
+ _objc_msgSend$initMembers:cloudsNumber:
+ _objc_msgSend$initWithExecutor:andAggregationSize:
+ _objc_msgSend$knownNetworksForVariant:
+ _objc_msgSend$networkVariant
+ _objc_msgSend$pointClouds
+ _objc_msgSend$pushColor:pose:calibration:metadata:timestamp:
+ _objc_msgSend$setNetworkVariant:
+ _objc_msgSend$subVariantsForVariant:
+ _objc_msgSend$supportedDimensionsForParameters:
+ _objc_msgSend$verboseLogs
+ _objc_retainAutoreleasedReturnValue
- -[ADMonocularVideoFlow processColor:efl:timestamp:]
- -[ADMonocularVideoFlow pushColor:efl:timestamp:]
- GCC_except_table1002
- GCC_except_table1023
- GCC_except_table1024
- GCC_except_table1025
- GCC_except_table1026
- GCC_except_table1027
- GCC_except_table1028
- GCC_except_table1029
- GCC_except_table1031
- GCC_except_table1036
- GCC_except_table1046
- GCC_except_table1047
- GCC_except_table1048
- GCC_except_table1049
- GCC_except_table1073
- GCC_except_table1074
- GCC_except_table1082
- GCC_except_table1083
- GCC_except_table1090
- GCC_except_table1091
- GCC_except_table1099
- GCC_except_table1100
- GCC_except_table1106
- GCC_except_table1107
- GCC_except_table1111
- GCC_except_table1112
- GCC_except_table1115
- GCC_except_table1116
- GCC_except_table1117
- GCC_except_table1119
- GCC_except_table1128
- GCC_except_table1140
- GCC_except_table1148
- GCC_except_table1149
- GCC_except_table1158
- GCC_except_table1164
- GCC_except_table1165
- GCC_except_table1167
- GCC_except_table1168
- GCC_except_table1169
- GCC_except_table1170
- GCC_except_table1173
- GCC_except_table1220
- GCC_except_table1222
- GCC_except_table1223
- GCC_except_table1227
- GCC_except_table1228
- GCC_except_table1229
- GCC_except_table1230
- GCC_except_table1238
- GCC_except_table1245
- GCC_except_table1246
- GCC_except_table1250
- GCC_except_table1251
- GCC_except_table1262
- GCC_except_table1263
- GCC_except_table1267
- GCC_except_table1268
- GCC_except_table1284
- GCC_except_table1285
- GCC_except_table1286
- GCC_except_table1288
- GCC_except_table1289
- GCC_except_table1290
- GCC_except_table1291
- GCC_except_table1292
- GCC_except_table1293
- GCC_except_table1294
- GCC_except_table1295
- GCC_except_table1296
- GCC_except_table1297
- GCC_except_table1319
- GCC_except_table1320
- GCC_except_table1328
- GCC_except_table1332
- GCC_except_table1333
- GCC_except_table1334
- GCC_except_table1336
- GCC_except_table1339
- GCC_except_table1341
- GCC_except_table1347
- GCC_except_table1367
- GCC_except_table1388
- GCC_except_table1389
- GCC_except_table1391
- GCC_except_table1393
- GCC_except_table1403
- GCC_except_table1404
- GCC_except_table1405
- GCC_except_table1406
- GCC_except_table1410
- GCC_except_table1420
- GCC_except_table1421
- GCC_except_table1422
- GCC_except_table1434
- GCC_except_table1436
- GCC_except_table1437
- GCC_except_table1449
- GCC_except_table1451
- GCC_except_table1453
- GCC_except_table1454
- GCC_except_table1464
- GCC_except_table1607
- GCC_except_table1644
- GCC_except_table1645
- GCC_except_table1646
- GCC_except_table1647
- GCC_except_table1651
- GCC_except_table1652
- GCC_except_table1653
- GCC_except_table1655
- GCC_except_table1656
- GCC_except_table1657
- GCC_except_table1658
- GCC_except_table1669
- GCC_except_table1670
- GCC_except_table1671
- GCC_except_table1682
- GCC_except_table1683
- GCC_except_table1688
- GCC_except_table1716
- GCC_except_table1729
- GCC_except_table1730
- GCC_except_table1731
- GCC_except_table1733
- GCC_except_table1744
- GCC_except_table1745
- GCC_except_table1766
- GCC_except_table1772
- GCC_except_table1773
- GCC_except_table1830
- GCC_except_table1831
- GCC_except_table1832
- GCC_except_table1833
- GCC_except_table1842
- GCC_except_table1850
- GCC_except_table1854
- GCC_except_table1860
- GCC_except_table1861
- GCC_except_table1862
- GCC_except_table1863
- GCC_except_table1870
- GCC_except_table1871
- GCC_except_table1872
- GCC_except_table1874
- GCC_except_table1879
- GCC_except_table1880
- GCC_except_table1881
- GCC_except_table1882
- GCC_except_table1883
- GCC_except_table1885
- GCC_except_table1903
- GCC_except_table1907
- GCC_except_table1910
- GCC_except_table1911
- GCC_except_table1912
- GCC_except_table1920
- GCC_except_table1921
- GCC_except_table1924
- GCC_except_table1925
- GCC_except_table1926
- GCC_except_table1935
- GCC_except_table1940
- GCC_except_table1942
- GCC_except_table1943
- GCC_except_table1949
- GCC_except_table1950
- GCC_except_table1952
- GCC_except_table1956
- GCC_except_table1966
- GCC_except_table1981
- GCC_except_table1990
- GCC_except_table1992
- GCC_except_table1993
- GCC_except_table1994
- GCC_except_table1995
- GCC_except_table1996
- GCC_except_table2002
- GCC_except_table2012
- GCC_except_table2015
- GCC_except_table2038
- GCC_except_table2039
- GCC_except_table2045
- GCC_except_table2048
- GCC_except_table2049
- GCC_except_table2052
- GCC_except_table2054
- GCC_except_table2057
- GCC_except_table2058
- GCC_except_table2060
- GCC_except_table2062
- GCC_except_table2091
- GCC_except_table2157
- GCC_except_table2158
- GCC_except_table2175
- GCC_except_table2176
- GCC_except_table2181
- GCC_except_table2190
- GCC_except_table2201
- GCC_except_table2202
- GCC_except_table2203
- GCC_except_table2204
- GCC_except_table2206
- GCC_except_table2209
- GCC_except_table2228
- GCC_except_table2229
- GCC_except_table2234
- GCC_except_table2240
- GCC_except_table2243
- GCC_except_table2246
- GCC_except_table2247
- GCC_except_table2248
- GCC_except_table2250
- GCC_except_table2251
- GCC_except_table2253
- GCC_except_table2254
- GCC_except_table2256
- GCC_except_table2258
- GCC_except_table2259
- GCC_except_table2260
- GCC_except_table2262
- GCC_except_table2265
- GCC_except_table2272
- GCC_except_table2273
- GCC_except_table2302
- GCC_except_table2305
- GCC_except_table2307
- GCC_except_table2312
- GCC_except_table2326
- GCC_except_table2329
- GCC_except_table2334
- GCC_except_table2335
- GCC_except_table2341
- GCC_except_table2343
- GCC_except_table2347
- GCC_except_table2348
- GCC_except_table2357
- GCC_except_table2359
- GCC_except_table2364
- GCC_except_table2390
- GCC_except_table2392
- GCC_except_table2393
- GCC_except_table2394
- GCC_except_table2399
- GCC_except_table2411
- GCC_except_table2414
- GCC_except_table2417
- GCC_except_table2420
- GCC_except_table2421
- GCC_except_table2422
- GCC_except_table2423
- GCC_except_table2429
- GCC_except_table2430
- GCC_except_table2435
- GCC_except_table2443
- GCC_except_table2444
- GCC_except_table2445
- GCC_except_table2448
- GCC_except_table2449
- GCC_except_table2450
- GCC_except_table2456
- GCC_except_table2458
- GCC_except_table2460
- GCC_except_table2461
- GCC_except_table2467
- GCC_except_table2474
- GCC_except_table2489
- GCC_except_table2542
- GCC_except_table2549
- GCC_except_table2553
- GCC_except_table2555
- GCC_except_table2557
- GCC_except_table2559
- GCC_except_table2560
- GCC_except_table2561
- GCC_except_table2564
- GCC_except_table2565
- GCC_except_table2567
- GCC_except_table2571
- GCC_except_table2572
- GCC_except_table2573
- GCC_except_table2580
- GCC_except_table2584
- GCC_except_table2603
- GCC_except_table2604
- GCC_except_table2608
- GCC_except_table2614
- GCC_except_table2620
- GCC_except_table2621
- GCC_except_table2622
- GCC_except_table2628
- GCC_except_table2637
- GCC_except_table2638
- GCC_except_table2639
- GCC_except_table2642
- GCC_except_table2643
- GCC_except_table2644
- GCC_except_table2645
- GCC_except_table2646
- GCC_except_table2647
- GCC_except_table2651
- GCC_except_table2654
- GCC_except_table2658
- GCC_except_table2665
- GCC_except_table2667
- GCC_except_table2668
- GCC_except_table2692
- GCC_except_table2693
- GCC_except_table2700
- GCC_except_table2707
- GCC_except_table2708
- GCC_except_table2709
- GCC_except_table2711
- GCC_except_table2712
- GCC_except_table2713
- GCC_except_table2714
- GCC_except_table2715
- GCC_except_table2727
- GCC_except_table2728
- GCC_except_table2729
- GCC_except_table2733
- GCC_except_table2734
- GCC_except_table2735
- GCC_except_table2737
- GCC_except_table2738
- GCC_except_table2740
- GCC_except_table2741
- GCC_except_table2758
- GCC_except_table2774
- GCC_except_table2775
- GCC_except_table2782
- GCC_except_table2791
- GCC_except_table2807
- GCC_except_table2822
- GCC_except_table2824
- GCC_except_table2829
- GCC_except_table2830
- GCC_except_table2842
- GCC_except_table2845
- GCC_except_table2846
- GCC_except_table2847
- GCC_except_table2848
- GCC_except_table2850
- GCC_except_table2852
- GCC_except_table2860
- GCC_except_table2866
- GCC_except_table2868
- GCC_except_table2870
- GCC_except_table2895
- GCC_except_table2896
- GCC_except_table2909
- GCC_except_table2910
- GCC_except_table2911
- GCC_except_table2931
- GCC_except_table2935
- GCC_except_table2936
- GCC_except_table2937
- GCC_except_table2938
- GCC_except_table2939
- GCC_except_table2940
- GCC_except_table2942
- GCC_except_table2958
- GCC_except_table2976
- GCC_except_table2977
- GCC_except_table2979
- GCC_except_table2980
- GCC_except_table2984
- GCC_except_table2993
- GCC_except_table3011
- GCC_except_table3012
- GCC_except_table3013
- GCC_except_table3014
- GCC_except_table3015
- GCC_except_table3020
- GCC_except_table3023
- GCC_except_table3036
- GCC_except_table3052
- GCC_except_table3055
- GCC_except_table3056
- GCC_except_table3060
- GCC_except_table3063
- GCC_except_table3066
- GCC_except_table3088
- GCC_except_table3095
- GCC_except_table3096
- GCC_except_table3101
- GCC_except_table3102
- GCC_except_table3103
- GCC_except_table3104
- GCC_except_table3105
- GCC_except_table3106
- GCC_except_table3107
- GCC_except_table3135
- GCC_except_table3136
- GCC_except_table3142
- GCC_except_table3149
- GCC_except_table3150
- GCC_except_table3151
- GCC_except_table3166
- GCC_except_table3167
- GCC_except_table3169
- GCC_except_table3170
- GCC_except_table3171
- GCC_except_table3176
- GCC_except_table3179
- GCC_except_table3183
- GCC_except_table3185
- GCC_except_table3187
- GCC_except_table3192
- GCC_except_table3197
- GCC_except_table3201
- GCC_except_table3202
- GCC_except_table3203
- GCC_except_table3206
- GCC_except_table3215
- GCC_except_table3221
- GCC_except_table3226
- GCC_except_table3233
- GCC_except_table3235
- GCC_except_table3239
- GCC_except_table3240
- GCC_except_table3242
- GCC_except_table3247
- GCC_except_table3249
- GCC_except_table3254
- GCC_except_table3257
- GCC_except_table3258
- GCC_except_table3262
- GCC_except_table3263
- GCC_except_table3267
- GCC_except_table3269
- GCC_except_table3270
- GCC_except_table3271
- GCC_except_table3276
- GCC_except_table3286
- GCC_except_table3287
- GCC_except_table3295
- GCC_except_table3308
- GCC_except_table3309
- GCC_except_table3328
- GCC_except_table3332
- GCC_except_table3333
- GCC_except_table3335
- GCC_except_table3337
- GCC_except_table3338
- GCC_except_table3339
- GCC_except_table3340
- GCC_except_table3342
- GCC_except_table3351
- GCC_except_table3352
- GCC_except_table3353
- GCC_except_table3354
- GCC_except_table3375
- GCC_except_table3376
- GCC_except_table3384
- GCC_except_table3402
- GCC_except_table3407
- GCC_except_table3408
- GCC_except_table3409
- GCC_except_table3410
- GCC_except_table3411
- GCC_except_table3417
- GCC_except_table3418
- GCC_except_table3419
- GCC_except_table3420
- GCC_except_table3421
- GCC_except_table3422
- GCC_except_table3429
- GCC_except_table395
- GCC_except_table398
- GCC_except_table403
- GCC_except_table405
- GCC_except_table406
- GCC_except_table408
- GCC_except_table436
- GCC_except_table437
- GCC_except_table440
- GCC_except_table444
- GCC_except_table456
- GCC_except_table457
- GCC_except_table458
- GCC_except_table459
- GCC_except_table460
- GCC_except_table461
- GCC_except_table478
- GCC_except_table533
- GCC_except_table534
- GCC_except_table535
- GCC_except_table536
- GCC_except_table537
- GCC_except_table555
- GCC_except_table556
- GCC_except_table557
- GCC_except_table558
- GCC_except_table559
- GCC_except_table560
- GCC_except_table570
- GCC_except_table571
- GCC_except_table572
- GCC_except_table573
- GCC_except_table597
- GCC_except_table624
- GCC_except_table625
- GCC_except_table629
- GCC_except_table632
- GCC_except_table633
- GCC_except_table634
- GCC_except_table656
- GCC_except_table657
- GCC_except_table658
- GCC_except_table670
- GCC_except_table672
- GCC_except_table673
- GCC_except_table686
- GCC_except_table694
- GCC_except_table699
- GCC_except_table715
- GCC_except_table716
- GCC_except_table721
- GCC_except_table731
- GCC_except_table733
- GCC_except_table734
- GCC_except_table738
- GCC_except_table739
- GCC_except_table740
- GCC_except_table741
- GCC_except_table744
- GCC_except_table746
- GCC_except_table750
- GCC_except_table751
- GCC_except_table770
- GCC_except_table772
- GCC_except_table782
- GCC_except_table783
- GCC_except_table789
- GCC_except_table807
- GCC_except_table813
- GCC_except_table815
- GCC_except_table816
- GCC_except_table817
- GCC_except_table818
- GCC_except_table820
- GCC_except_table824
- GCC_except_table825
- GCC_except_table833
- GCC_except_table842
- GCC_except_table843
- GCC_except_table844
- GCC_except_table851
- GCC_except_table854
- GCC_except_table855
- GCC_except_table860
- GCC_except_table861
- GCC_except_table862
- GCC_except_table864
- GCC_except_table913
- GCC_except_table914
- GCC_except_table915
- GCC_except_table918
- GCC_except_table926
- GCC_except_table930
- GCC_except_table933
- GCC_except_table934
- GCC_except_table967
- GCC_except_table968
- GCC_except_table978
- GCC_except_table980
- GCC_except_table984
- GCC_except_table985
- GCC_except_table986
- GCC_except_table989
- GCC_except_table990
- GCC_except_table991
- GCC_except_table993
- GCC_except_table995
- GCC_except_table996
- GCC_except_table997
- _NSClassFromString
- _NSSelectorFromString
- _OBJC_IVAR_$_ADMonocularVideoPipeline._networkNominalEFL
- __PromotedConst.10423
- __PromotedConst.10424
- __Z31debugQuickLookObjectFromCGImageP7CGImage
- __ZGVZ47+[ADMonocularVideoPipeline supportedDimensions]E6result
- __ZL15INSTRUMENTS_ENDjyyyy.10000
- __ZL15INSTRUMENTS_ENDjyyyy.10184
- __ZL15INSTRUMENTS_ENDjyyyy.10400
- __ZL15INSTRUMENTS_ENDjyyyy.10406
- __ZL15INSTRUMENTS_ENDjyyyy.1114
- __ZL15INSTRUMENTS_ENDjyyyy.1224
- __ZL15INSTRUMENTS_ENDjyyyy.1411
- __ZL15INSTRUMENTS_ENDjyyyy.1515
- __ZL15INSTRUMENTS_ENDjyyyy.1725
- __ZL15INSTRUMENTS_ENDjyyyy.1757
- __ZL15INSTRUMENTS_ENDjyyyy.1930
- __ZL15INSTRUMENTS_ENDjyyyy.2123
- __ZL15INSTRUMENTS_ENDjyyyy.2362
- __ZL15INSTRUMENTS_ENDjyyyy.243
- __ZL15INSTRUMENTS_ENDjyyyy.249
- __ZL15INSTRUMENTS_ENDjyyyy.2569
- __ZL15INSTRUMENTS_ENDjyyyy.260
- __ZL15INSTRUMENTS_ENDjyyyy.2643
- __ZL15INSTRUMENTS_ENDjyyyy.2690
- __ZL15INSTRUMENTS_ENDjyyyy.271
- __ZL15INSTRUMENTS_ENDjyyyy.2775
- __ZL15INSTRUMENTS_ENDjyyyy.2808
- __ZL15INSTRUMENTS_ENDjyyyy.2814
- __ZL15INSTRUMENTS_ENDjyyyy.3009
- __ZL15INSTRUMENTS_ENDjyyyy.3079
- __ZL15INSTRUMENTS_ENDjyyyy.3315
- __ZL15INSTRUMENTS_ENDjyyyy.340
- __ZL15INSTRUMENTS_ENDjyyyy.3435
- __ZL15INSTRUMENTS_ENDjyyyy.3449
- __ZL15INSTRUMENTS_ENDjyyyy.3455
- __ZL15INSTRUMENTS_ENDjyyyy.3702
- __ZL15INSTRUMENTS_ENDjyyyy.3911
- __ZL15INSTRUMENTS_ENDjyyyy.3921
- __ZL15INSTRUMENTS_ENDjyyyy.3984
- __ZL15INSTRUMENTS_ENDjyyyy.4168
- __ZL15INSTRUMENTS_ENDjyyyy.4304
- __ZL15INSTRUMENTS_ENDjyyyy.4656
- __ZL15INSTRUMENTS_ENDjyyyy.472
- __ZL15INSTRUMENTS_ENDjyyyy.4862
- __ZL15INSTRUMENTS_ENDjyyyy.5040
- __ZL15INSTRUMENTS_ENDjyyyy.5260
- __ZL15INSTRUMENTS_ENDjyyyy.558
- __ZL15INSTRUMENTS_ENDjyyyy.5729
- __ZL15INSTRUMENTS_ENDjyyyy.5875
- __ZL15INSTRUMENTS_ENDjyyyy.6102
- __ZL15INSTRUMENTS_ENDjyyyy.6435
- __ZL15INSTRUMENTS_ENDjyyyy.6710
- __ZL15INSTRUMENTS_ENDjyyyy.6888
- __ZL15INSTRUMENTS_ENDjyyyy.7002
- __ZL15INSTRUMENTS_ENDjyyyy.7018
- __ZL15INSTRUMENTS_ENDjyyyy.715
- __ZL15INSTRUMENTS_ENDjyyyy.7204
- __ZL15INSTRUMENTS_ENDjyyyy.7210
- __ZL15INSTRUMENTS_ENDjyyyy.731
- __ZL15INSTRUMENTS_ENDjyyyy.7340
- __ZL15INSTRUMENTS_ENDjyyyy.7363
- __ZL15INSTRUMENTS_ENDjyyyy.7388
- __ZL15INSTRUMENTS_ENDjyyyy.7587
- __ZL15INSTRUMENTS_ENDjyyyy.7836
- __ZL15INSTRUMENTS_ENDjyyyy.7876
- __ZL15INSTRUMENTS_ENDjyyyy.7924
- __ZL15INSTRUMENTS_ENDjyyyy.8035
- __ZL15INSTRUMENTS_ENDjyyyy.8191
- __ZL15INSTRUMENTS_ENDjyyyy.8375
- __ZL15INSTRUMENTS_ENDjyyyy.8381
- __ZL15INSTRUMENTS_ENDjyyyy.8437
- __ZL15INSTRUMENTS_ENDjyyyy.8447
- __ZL15INSTRUMENTS_ENDjyyyy.8599
- __ZL15INSTRUMENTS_ENDjyyyy.8918
- __ZL15INSTRUMENTS_ENDjyyyy.8944
- __ZL15INSTRUMENTS_ENDjyyyy.9117
- __ZL15INSTRUMENTS_ENDjyyyy.9141
- __ZL15INSTRUMENTS_ENDjyyyy.9389
- __ZL15INSTRUMENTS_ENDjyyyy.9934
- __ZL15INSTRUMENTS_ENDjyyyy.997
- __ZL17INSTRUMENTS_EVENTjyyyy.10001
- __ZL17INSTRUMENTS_EVENTjyyyy.10185
- __ZL17INSTRUMENTS_EVENTjyyyy.10401
- __ZL17INSTRUMENTS_EVENTjyyyy.10407
- __ZL17INSTRUMENTS_EVENTjyyyy.1115
- __ZL17INSTRUMENTS_EVENTjyyyy.1225
- __ZL17INSTRUMENTS_EVENTjyyyy.1412
- __ZL17INSTRUMENTS_EVENTjyyyy.1516
- __ZL17INSTRUMENTS_EVENTjyyyy.1726
- __ZL17INSTRUMENTS_EVENTjyyyy.1758
- __ZL17INSTRUMENTS_EVENTjyyyy.1931
- __ZL17INSTRUMENTS_EVENTjyyyy.2124
- __ZL17INSTRUMENTS_EVENTjyyyy.2363
- __ZL17INSTRUMENTS_EVENTjyyyy.244
- __ZL17INSTRUMENTS_EVENTjyyyy.250
- __ZL17INSTRUMENTS_EVENTjyyyy.2570
- __ZL17INSTRUMENTS_EVENTjyyyy.261
- __ZL17INSTRUMENTS_EVENTjyyyy.2644
- __ZL17INSTRUMENTS_EVENTjyyyy.2691
- __ZL17INSTRUMENTS_EVENTjyyyy.272
- __ZL17INSTRUMENTS_EVENTjyyyy.2776
- __ZL17INSTRUMENTS_EVENTjyyyy.2809
- __ZL17INSTRUMENTS_EVENTjyyyy.2815
- __ZL17INSTRUMENTS_EVENTjyyyy.3010
- __ZL17INSTRUMENTS_EVENTjyyyy.3080
- __ZL17INSTRUMENTS_EVENTjyyyy.3316
- __ZL17INSTRUMENTS_EVENTjyyyy.341
- __ZL17INSTRUMENTS_EVENTjyyyy.3436
- __ZL17INSTRUMENTS_EVENTjyyyy.3450
- __ZL17INSTRUMENTS_EVENTjyyyy.3456
- __ZL17INSTRUMENTS_EVENTjyyyy.3703
- __ZL17INSTRUMENTS_EVENTjyyyy.3912
- __ZL17INSTRUMENTS_EVENTjyyyy.3922
- __ZL17INSTRUMENTS_EVENTjyyyy.3985
- __ZL17INSTRUMENTS_EVENTjyyyy.4169
- __ZL17INSTRUMENTS_EVENTjyyyy.4305
- __ZL17INSTRUMENTS_EVENTjyyyy.4657
- __ZL17INSTRUMENTS_EVENTjyyyy.473
- __ZL17INSTRUMENTS_EVENTjyyyy.4863
- __ZL17INSTRUMENTS_EVENTjyyyy.5041
- __ZL17INSTRUMENTS_EVENTjyyyy.5261
- __ZL17INSTRUMENTS_EVENTjyyyy.559
- __ZL17INSTRUMENTS_EVENTjyyyy.5730
- __ZL17INSTRUMENTS_EVENTjyyyy.5876
- __ZL17INSTRUMENTS_EVENTjyyyy.6103
- __ZL17INSTRUMENTS_EVENTjyyyy.6436
- __ZL17INSTRUMENTS_EVENTjyyyy.6711
- __ZL17INSTRUMENTS_EVENTjyyyy.6889
- __ZL17INSTRUMENTS_EVENTjyyyy.7003
- __ZL17INSTRUMENTS_EVENTjyyyy.7019
- __ZL17INSTRUMENTS_EVENTjyyyy.716
- __ZL17INSTRUMENTS_EVENTjyyyy.7205
- __ZL17INSTRUMENTS_EVENTjyyyy.7211
- __ZL17INSTRUMENTS_EVENTjyyyy.732
- __ZL17INSTRUMENTS_EVENTjyyyy.7341
- __ZL17INSTRUMENTS_EVENTjyyyy.7364
- __ZL17INSTRUMENTS_EVENTjyyyy.7389
- __ZL17INSTRUMENTS_EVENTjyyyy.7588
- __ZL17INSTRUMENTS_EVENTjyyyy.7837
- __ZL17INSTRUMENTS_EVENTjyyyy.7877
- __ZL17INSTRUMENTS_EVENTjyyyy.7925
- __ZL17INSTRUMENTS_EVENTjyyyy.8036
- __ZL17INSTRUMENTS_EVENTjyyyy.8192
- __ZL17INSTRUMENTS_EVENTjyyyy.8376
- __ZL17INSTRUMENTS_EVENTjyyyy.8382
- __ZL17INSTRUMENTS_EVENTjyyyy.8438
- __ZL17INSTRUMENTS_EVENTjyyyy.8448
- __ZL17INSTRUMENTS_EVENTjyyyy.8600
- __ZL17INSTRUMENTS_EVENTjyyyy.8919
- __ZL17INSTRUMENTS_EVENTjyyyy.8945
- __ZL17INSTRUMENTS_EVENTjyyyy.9118
- __ZL17INSTRUMENTS_EVENTjyyyy.9142
- __ZL17INSTRUMENTS_EVENTjyyyy.9390
- __ZL17INSTRUMENTS_EVENTjyyyy.9935
- __ZL17INSTRUMENTS_EVENTjyyyy.998
- __ZL17INSTRUMENTS_STARTjyyyy.10002
- __ZL17INSTRUMENTS_STARTjyyyy.10186
- __ZL17INSTRUMENTS_STARTjyyyy.10402
- __ZL17INSTRUMENTS_STARTjyyyy.10408
- __ZL17INSTRUMENTS_STARTjyyyy.1116
- __ZL17INSTRUMENTS_STARTjyyyy.1226
- __ZL17INSTRUMENTS_STARTjyyyy.1413
- __ZL17INSTRUMENTS_STARTjyyyy.1517
- __ZL17INSTRUMENTS_STARTjyyyy.1727
- __ZL17INSTRUMENTS_STARTjyyyy.1759
- __ZL17INSTRUMENTS_STARTjyyyy.1932
- __ZL17INSTRUMENTS_STARTjyyyy.2125
- __ZL17INSTRUMENTS_STARTjyyyy.2364
- __ZL17INSTRUMENTS_STARTjyyyy.245
- __ZL17INSTRUMENTS_STARTjyyyy.251
- __ZL17INSTRUMENTS_STARTjyyyy.2571
- __ZL17INSTRUMENTS_STARTjyyyy.262
- __ZL17INSTRUMENTS_STARTjyyyy.2645
- __ZL17INSTRUMENTS_STARTjyyyy.2692
- __ZL17INSTRUMENTS_STARTjyyyy.273
- __ZL17INSTRUMENTS_STARTjyyyy.2777
- __ZL17INSTRUMENTS_STARTjyyyy.2810
- __ZL17INSTRUMENTS_STARTjyyyy.2816
- __ZL17INSTRUMENTS_STARTjyyyy.3011
- __ZL17INSTRUMENTS_STARTjyyyy.3081
- __ZL17INSTRUMENTS_STARTjyyyy.3317
- __ZL17INSTRUMENTS_STARTjyyyy.342
- __ZL17INSTRUMENTS_STARTjyyyy.3437
- __ZL17INSTRUMENTS_STARTjyyyy.3451
- __ZL17INSTRUMENTS_STARTjyyyy.3457
- __ZL17INSTRUMENTS_STARTjyyyy.3704
- __ZL17INSTRUMENTS_STARTjyyyy.3913
- __ZL17INSTRUMENTS_STARTjyyyy.3923
- __ZL17INSTRUMENTS_STARTjyyyy.3986
- __ZL17INSTRUMENTS_STARTjyyyy.4170
- __ZL17INSTRUMENTS_STARTjyyyy.4306
- __ZL17INSTRUMENTS_STARTjyyyy.4658
- __ZL17INSTRUMENTS_STARTjyyyy.474
- __ZL17INSTRUMENTS_STARTjyyyy.4864
- __ZL17INSTRUMENTS_STARTjyyyy.5042
- __ZL17INSTRUMENTS_STARTjyyyy.5262
- __ZL17INSTRUMENTS_STARTjyyyy.560
- __ZL17INSTRUMENTS_STARTjyyyy.5731
- __ZL17INSTRUMENTS_STARTjyyyy.5877
- __ZL17INSTRUMENTS_STARTjyyyy.6104
- __ZL17INSTRUMENTS_STARTjyyyy.6437
- __ZL17INSTRUMENTS_STARTjyyyy.6712
- __ZL17INSTRUMENTS_STARTjyyyy.6890
- __ZL17INSTRUMENTS_STARTjyyyy.7004
- __ZL17INSTRUMENTS_STARTjyyyy.7020
- __ZL17INSTRUMENTS_STARTjyyyy.717
- __ZL17INSTRUMENTS_STARTjyyyy.7206
- __ZL17INSTRUMENTS_STARTjyyyy.7212
- __ZL17INSTRUMENTS_STARTjyyyy.733
- __ZL17INSTRUMENTS_STARTjyyyy.7342
- __ZL17INSTRUMENTS_STARTjyyyy.7365
- __ZL17INSTRUMENTS_STARTjyyyy.7390
- __ZL17INSTRUMENTS_STARTjyyyy.7589
- __ZL17INSTRUMENTS_STARTjyyyy.7838
- __ZL17INSTRUMENTS_STARTjyyyy.7878
- __ZL17INSTRUMENTS_STARTjyyyy.7926
- __ZL17INSTRUMENTS_STARTjyyyy.8037
- __ZL17INSTRUMENTS_STARTjyyyy.8193
- __ZL17INSTRUMENTS_STARTjyyyy.8377
- __ZL17INSTRUMENTS_STARTjyyyy.8383
- __ZL17INSTRUMENTS_STARTjyyyy.8439
- __ZL17INSTRUMENTS_STARTjyyyy.8449
- __ZL17INSTRUMENTS_STARTjyyyy.8601
- __ZL17INSTRUMENTS_STARTjyyyy.8920
- __ZL17INSTRUMENTS_STARTjyyyy.8946
- __ZL17INSTRUMENTS_STARTjyyyy.9119
- __ZL17INSTRUMENTS_STARTjyyyy.9143
- __ZL17INSTRUMENTS_STARTjyyyy.9391
- __ZL17INSTRUMENTS_STARTjyyyy.9936
- __ZL17INSTRUMENTS_STARTjyyyy.999
- __ZL32ADDebugUtilsADVerboseLogsEnabled
- __ZN12ADDebugUtils20isVerboseLogsEnabledEv
- __ZN12ADDebugUtils21setVerboseLogsEnabledEb
- __ZNKSt3__110__function6__funcIZ53-[ADWorldToImageProjection initWithPose:calibration:]E3$_0NS_9allocatorIS2_EEFNS_6vectorI7CGPointNS3_IS6_EEEERKNS5_IDv3_fNS3_IS9_EEEEEE7__cloneEPNS0_6__baseISE_EE
- __ZNKSt3__110__function6__funcIZ53-[ADWorldToImageProjection initWithPose:calibration:]E3$_0NS_9allocatorIS2_EEFNS_6vectorI7CGPointNS3_IS6_EEEERKNS5_IDv3_fNS3_IS9_EEEEEE7__cloneEv
- __ZNKSt3__110__function6__funcIZ92-[ADDispartiyToDepthFitEstimator estimateWithDisparity:calibration:pose:disparityTimestamp:]E3$_0NS_9allocatorIS2_EEFNS_6vectorI7CGPointNS3_IS6_EEEERKNS5_IDv3_fNS3_IS9_EEEEEE7__cloneEPNS0_6__baseISE_EE
- __ZNKSt3__110__function6__funcIZ92-[ADDispartiyToDepthFitEstimator estimateWithDisparity:calibration:pose:disparityTimestamp:]E3$_0NS_9allocatorIS2_EEFNS_6vectorI7CGPointNS3_IS6_EEEERKNS5_IDv3_fNS3_IS9_EEEEEE7__cloneEv
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt3__110__function6__funcIZ53-[ADWorldToImageProjection initWithPose:calibration:]E3$_0NS_9allocatorIS2_EEFNS_6vectorI7CGPointNS3_IS6_EEEERKNS5_IDv3_fNS3_IS9_EEEEEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZ53-[ADWorldToImageProjection initWithPose:calibration:]E3$_0NS_9allocatorIS2_EEFNS_6vectorI7CGPointNS3_IS6_EEEERKNS5_IDv3_fNS3_IS9_EEEEEE7destroyEv
- __ZNSt3__110__function6__funcIZ53-[ADWorldToImageProjection initWithPose:calibration:]E3$_0NS_9allocatorIS2_EEFNS_6vectorI7CGPointNS3_IS6_EEEERKNS5_IDv3_fNS3_IS9_EEEEEED0Ev
- __ZNSt3__110__function6__funcIZ53-[ADWorldToImageProjection initWithPose:calibration:]E3$_0NS_9allocatorIS2_EEFNS_6vectorI7CGPointNS3_IS6_EEEERKNS5_IDv3_fNS3_IS9_EEEEEED1Ev
- __ZNSt3__110__function6__funcIZ53-[ADWorldToImageProjection initWithPose:calibration:]E3$_0NS_9allocatorIS2_EEFNS_6vectorI7CGPointNS3_IS6_EEEERKNS5_IDv3_fNS3_IS9_EEEEEEclESD_
- __ZNSt3__110__function6__funcIZ92-[ADDispartiyToDepthFitEstimator estimateWithDisparity:calibration:pose:disparityTimestamp:]E3$_0NS_9allocatorIS2_EEFNS_6vectorI7CGPointNS3_IS6_EEEERKNS5_IDv3_fNS3_IS9_EEEEEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZ92-[ADDispartiyToDepthFitEstimator estimateWithDisparity:calibration:pose:disparityTimestamp:]E3$_0NS_9allocatorIS2_EEFNS_6vectorI7CGPointNS3_IS6_EEEERKNS5_IDv3_fNS3_IS9_EEEEEE7destroyEv
- __ZNSt3__110__function6__funcIZ92-[ADDispartiyToDepthFitEstimator estimateWithDisparity:calibration:pose:disparityTimestamp:]E3$_0NS_9allocatorIS2_EEFNS_6vectorI7CGPointNS3_IS6_EEEERKNS5_IDv3_fNS3_IS9_EEEEEED0Ev
- __ZNSt3__110__function6__funcIZ92-[ADDispartiyToDepthFitEstimator estimateWithDisparity:calibration:pose:disparityTimestamp:]E3$_0NS_9allocatorIS2_EEFNS_6vectorI7CGPointNS3_IS6_EEEERKNS5_IDv3_fNS3_IS9_EEEEEED1Ev
- __ZNSt3__110__function6__funcIZ92-[ADDispartiyToDepthFitEstimator estimateWithDisparity:calibration:pose:disparityTimestamp:]E3$_0NS_9allocatorIS2_EEFNS_6vectorI7CGPointNS3_IS6_EEEERKNS5_IDv3_fNS3_IS9_EEEEEEclESD_
- __ZNSt3__110shared_ptrIN3jpc9IIFABlock9IFAOutputEED1B8ne200100Ev
- __ZNSt3__110shared_ptrIN3jpc9IIFABlock9IFAOutputEED2B8ne200100Ev
- __ZNSt3__110unique_ptrIN3jpc9IIFABlock9IFAOutputENS_14default_deleteIS3_EEED2B8ne200100Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIm20PixelBufferSharedPtrEEPvEENS_22__hash_node_destructorINS_9allocatorIS6_EEEEED1B8ne200100Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIm20PixelBufferSharedPtrEENS_22__unordered_map_hasherImS3_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS3_S8_S6_Lb1EEENS_9allocatorIS3_EEE25__emplace_unique_key_argsImJRKNS_21piecewise_construct_tENS_5tupleIJRKmEEENSJ_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyNS_4pairIPhiEEEENS_22__unordered_map_hasherIyS5_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS5_SA_S8_Lb1EEENS_9allocatorIS5_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyNS_4pairIPhiEEEENS_22__unordered_map_hasherIyS5_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS5_SA_S8_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIyJRKNS_21piecewise_construct_tENS_5tupleIJOyEEENSL_IJEEEEEENS2_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyNS_4pairIPhiEEEENS_22__unordered_map_hasherIyS5_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS5_SA_S8_Lb1EEENS_9allocatorIS5_EEED2Ev
- __ZNSt3__112__tuple_implINS_15__tuple_indicesIJLm0ELm1ELm2ELm3ELm4ELm5EEEEJbffNS_6vectorIfNS_9allocatorIfEEEES6_NS3_I31ADDisparityToDepthFitWorldPointNS4_IS7_EEEEEEC2B8ne200100IJLm0ELm1ELm2ELm3ELm4ELm5EEJbffS6_S6_S9_EJEJEJbiiRS6_SC_RKS9_EEENS1_IJXspT_EEEENS_13__tuple_typesIJDpT0_EEENS1_IJXspT1_EEEENSG_IJDpT2_EEEDpOT3_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__113__nth_elementB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_11__wrap_iterIPfEEEEvT1_S8_S8_T0_
- __ZNSt3__113unordered_setIiNS_4hashIiEENS_8equal_toIiEENS_9allocatorIiEEED1B8ne200100Ev
- __ZNSt3__113unordered_setImNS_4hashImEENS_8equal_toImEENS_9allocatorImEEED1B8ne200100Ev
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB8ne200100Ev
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100Ev
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- __ZNSt3__124__put_character_sequenceB8ne200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__125__throw_bad_function_callB8ne200100Ev
- __ZNSt3__128__exception_guard_exceptionsINS_6vectorI11MatrixNxPtsILj1EdENS_9allocatorIS3_EEE16__destroy_vectorEED2B8ne200100Ev
- __ZNSt3__128__exception_guard_exceptionsINS_6vectorINS1_IiNS_9allocatorIiEEEENS2_IS4_EEE16__destroy_vectorEED2B8ne200100Ev
- __ZNSt3__16vectorI11MatrixNxPtsILj1EdENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorI31ADDisparityToDepthFitWorldPointNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorI7CGPointNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIDv3_fNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIN3jpc18IPreprocessorBlock19PearlCorrespondenceENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIN3jpc18IPreprocessorBlock25PearlJasperCorrespondenceENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIN3jpc9IIFABlock22IFAPearlCorrespondenceENS_9allocatorIS3_EEE18__assign_with_sizeB8ne200100IPS3_S8_EEvT_T0_l
- __ZNSt3__16vectorIN3jpc9IIFABlock22IFAPearlCorrespondenceENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIN3jpc9IIFABlock28IFAPearlJasperCorrespondenceENS_9allocatorIS3_EEE18__assign_with_sizeB8ne200100IPS3_S8_EEvT_T0_l
- __ZNSt3__16vectorIN3jpc9IIFABlock28IFAPearlJasperCorrespondenceENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIN3jpc9IIFABlock28IFAPearlJasperCorrespondenceENS_9allocatorIS3_EEE9push_backB8ne200100ERKS3_
- __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEED1B8ne200100Ev
- __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEED2B8ne200100Ev
- __ZNSt3__16vectorINS_10unique_ptrIN3jpc11IIFA_FilterENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorINS_10unique_ptrIN3jpc11IIFA_FilterENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEED2B8ne200100Ev
- __ZNSt3__16vectorINS_10unique_ptrIN3jpc15IFAPullCriteriaENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorINS_10unique_ptrIN3jpc15IFAPullCriteriaENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEED2B8ne200100Ev
- __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEED2B8ne200100Ev
- __ZNSt3__16vectorIbNS_9allocatorIbEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ne200100IPfS5_EEvT_T0_l
- __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIiNS_9allocatorIiEEE9push_backB8ne200100EOi
- __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorItNS_9allocatorItEEE20__throw_length_errorB8ne200100Ev
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
- __ZTVNSt3__110__function6__funcIZ53-[ADWorldToImageProjection initWithPose:calibration:]E3$_0NS_9allocatorIS2_EEFNS_6vectorI7CGPointNS3_IS6_EEEERKNS5_IDv3_fNS3_IS9_EEEEEEE
- __ZTVNSt3__110__function6__funcIZ92-[ADDispartiyToDepthFitEstimator estimateWithDisparity:calibration:pose:disparityTimestamp:]E3$_0NS_9allocatorIS2_EEFNS_6vectorI7CGPointNS3_IS6_EEEERKNS5_IDv3_fNS3_IS9_EEEEEEE
- __ZZ47+[ADMonocularVideoPipeline supportedDimensions]E4once
- __ZZ47+[ADMonocularVideoPipeline supportedDimensions]E6result
- ___47+[ADMonocularVideoPipeline supportedDimensions]_block_invoke
- ___block_literal_global.220
- ___block_literal_global.222
- ___block_literal_global.224
- ___block_literal_global.4827
- ___block_literal_global.6974
- ___block_literal_global.7578
- ___block_literal_global.9499
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$methodForSelector:
- _objc_release_x10
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x6
- _objc_retain_x7
CStrings:
+ "%@ completed frame %zu in %f ms"
+ "%@ starting frame %zu"
+ "%s:%d - ERROR - Failed to create pixel buffer"
+ "%s:%d - ERROR - Failed to fill pixel buffer from BMTL data"
+ "%s:%d - ERROR - Failed to read BMTL file"
+ "%s:%d - ERROR - Invalid header size"
+ "%s:%d - ERROR - Unsupported Metal format %lu"
+ "%s_%d"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD7j7ujyfjOVlVxRGqoF8KIZZ5kSxAhgws/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:122: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD7j7ujyfjOVlVxRGqoF8KIZZ5kSxAhgws/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:127: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD7j7ujyfjOVlVxRGqoF8KIZZ5kSxAhgws/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:158: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD7j7ujyfjOVlVxRGqoF8KIZZ5kSxAhgws/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:164: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD7j7ujyfjOVlVxRGqoF8KIZZ5kSxAhgws/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD7j7ujyfjOVlVxRGqoF8KIZZ5kSxAhgws/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__memory/unique_ptr.h:582: libc++ Hardening assertion __checker_.__in_bounds<deleter_type>(std::__to_address(__ptr_), __i) failed: unique_ptr<T[]>::operator[](index): index out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD7j7ujyfjOVlVxRGqoF8KIZZ5kSxAhgws/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD7j7ujyfjOVlVxRGqoF8KIZZ5kSxAhgws/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD7j7ujyfjOVlVxRGqoF8KIZZ5kSxAhgws/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD7j7ujyfjOVlVxRGqoF8KIZZ5kSxAhgws/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD7j7ujyfjOVlVxRGqoF8KIZZ5kSxAhgws/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "/Library/Caches/com.apple.xbs/82F9C946-042E-4E31-AE21-059D231A648F/TemporaryDirectory.NaZ9ev/Sources/AppleDepth/AppleDepth/Executors/ADJasperPearlInFieldCalibrationExecutor.mm"
+ "/Library/Caches/com.apple.xbs/82F9C946-042E-4E31-AE21-059D231A648F/TemporaryDirectory.NaZ9ev/Sources/AppleDepth/AppleDepth/InFieldCalibrations/JPC/Blocks/GMC_J/JPC_PORGMCJ_Block.mm"
+ "/Library/Caches/com.apple.xbs/82F9C946-042E-4E31-AE21-059D231A648F/TemporaryDirectory.NaZ9ev/Sources/AppleDepth/AppleDepth/InFieldCalibrations/JPC/Blocks/IFA/JPC_PORIFABlock.mm"
+ "/Library/Caches/com.apple.xbs/82F9C946-042E-4E31-AE21-059D231A648F/TemporaryDirectory.NaZ9ev/Sources/AppleDepth/AppleDepth/InFieldCalibrations/JPC/Blocks/OutputValidation/JPC_PORGMCJ_OutputValidation_Block.mm"
+ "/Library/Caches/com.apple.xbs/82F9C946-042E-4E31-AE21-059D231A648F/TemporaryDirectory.NaZ9ev/Sources/AppleDepth/AppleDepth/InFieldCalibrations/JPC/Blocks/Preprocessor/JPC_PORPreprocessorBlock.mm"
+ "/Library/Caches/com.apple.xbs/82F9C946-042E-4E31-AE21-059D231A648F/TemporaryDirectory.NaZ9ev/Sources/AppleDepth/AppleDepth/InFieldCalibrations/JPC/JPC.mm"
+ "/Library/Caches/com.apple.xbs/82F9C946-042E-4E31-AE21-059D231A648F/TemporaryDirectory.NaZ9ev/Sources/AppleDepth/AppleDepth/Utils/ADInFieldCalibrationInterSessionData.mm"
+ "158.0"
+ "@\"ADJasperColorStillsExecutor\""
+ "@\"ADJasperColorV2Executor\""
+ "@\"ADMonocularStillsExecutor\""
+ "@\"ADPCEDisparityColorExecutor\""
+ "A"
+ "ADFlowDepthConsumer"
+ "ADJasperColorInFieldCalibration jasper controller not satisfied: number of good spots is too low (not an error but data quality control)"
+ "ADJasperColorInFieldCalibration jasper controller not satisfied: number of valid spots is too low (not an error but data quality control)"
+ "ADJasperColorInFieldCalibration preprocessInputColorFrameImpl is not satisfied due to high angular velocity (not an error, angular movement is too hard and can be reduced by user movement)"
+ "ADJasperColorInFieldCalibration run results relative to previous [%f, %f, %f]"
+ "ADJasperColorInFieldCalibration run results relative to previous post ISF [%f, %f, %f]"
+ "ADJasperColorStillsFlow"
+ "ADJasperColorV2Flow"
+ "ADMonocularStillsFlow"
+ "ADMonocularVideoExecutorScaleFactor"
+ "ADPCEDisparityColorFlow"
+ "Cannot find supported dimensions for provided pipeline parameters"
+ "Dimensions %@ for network %@ were already found in other network, only first one (%@) will be used"
+ "Failed finding eflScaleFactor for network %@"
+ "Failed finding nominalResolutionFactor for network %@"
+ "Failed finding nominalScaleFactor for network %@"
+ "FocalLenIn35mmFilm"
+ "NOT (SELF ENDSWITH '-none')"
+ "Pearl Color In-Field calibration pipeline init for %@"
+ "Requested dimensions not provided, defaulting to %lux%lu"
+ "Selected flow type %d"
+ "T@\"ADJasperColorStillsExecutor\",R,&,N,V_executor"
+ "T@\"ADJasperColorV2Executor\",R,&,N,V_executor"
+ "T@\"ADJasperColorV2Pipeline\",R,&,N,V_pipeline"
+ "T@\"ADMonocularStillsExecutor\",R,&,N,V_executor"
+ "T@\"ADPCEDisparityColorExecutor\",R,&,N,V_executor"
+ "TQ,N,V_networkVariant"
+ "T^{__CVBuffer=},N,V_preAllocatedConfidenceOutputBuffer"
+ "T^{__CVBuffer=},N,V_preAllocatedDepthOutputBuffer"
+ "T^{__CVBuffer=},N,V_preAllocatedOutputBuffer"
+ "Unknown device frequency for (%@). Will use 24MHz..."
+ "Unsupported network variant #%u"
+ "_aggregationCount"
+ "_eflScaleFactor"
+ "_executorName"
+ "_initializeBaseConfig:"
+ "_networkVariant"
+ "_nominalResolutionFactor"
+ "_preAllocatedConfidenceOutputBuffer"
+ "_preAllocatedDepthOutputBuffer"
+ "_preAllocatedOutputBuffer"
+ "_verboseLogs"
+ "a\"2"
+ "color buffer must not be null"
+ "dataWithContentsOfURL:"
+ "executeForPreprocessed features index %d/%d"
+ "executeWithColor:cameraCalibration:outDisparityMap:"
+ "executeWithColor:focalLength35mm:outDisparityMap:"
+ "executeWithColor:pointCloud:jasperCalibration:colorCalibration:timestamp:outputDepthMap:outputConfidenceMap:"
+ "executeWithColor:scaleFactor:outDisparityMap:"
+ "executeWithDisparity:depthMetadata:color:outDisparity:"
+ "failed ADPCEDisparityColorFlow, missing metadata"
+ "failed executing Monocular Still"
+ "failed preProcessColor Color"
+ "failed preprocessing ADPCEDisparityColorFlow input stage"
+ "getBytes:range:"
+ "getFocalLength35mm"
+ "getMetricScaleFactorFor35mmFocalLength:"
+ "initMembers:cloudsNumber:"
+ "initWithExecutor:andAggregationSize:"
+ "inputDepth"
+ "inputDepthMetadata"
+ "intermediatePointCloudFilteredUncropped"
+ "intermediateProcessedDepth"
+ "knownNetworksForVariant:"
+ "modelInputDepth"
+ "must provide metadata with NormalizationMultiplier"
+ "must provide metadata with NormalizationOffset"
+ "networkVariant"
+ "pixelBufferFromBMTLFile"
+ "pixelFormatFromMTLPixelFormat"
+ "preAllocatedConfidenceOutputBuffer"
+ "preAllocatedDepthOutputBuffer"
+ "preAllocatedOutputBuffer"
+ "pushColor:focalLength35mm:timestamp:"
+ "pushDepth:pose:metadata:timestamp:"
+ "q40@0:8^{__CVBuffer=}16@24^^{__CVBuffer}32"
+ "q48@0:8^{__CVBuffer=}16@24^{__CVBuffer=}32^^{__CVBuffer}40"
+ "q72@0:8^{__CVBuffer=}16@24@32@40d48^^{__CVBuffer}56^^{__CVBuffer}64"
+ "running executeForPreprocessed before preProcessInputColorFrame called"
+ "setNetworkVariant:"
+ "setPreAllocatedConfidenceOutputBuffer:"
+ "setPreAllocatedDepthOutputBuffer:"
+ "setPreAllocatedOutputBuffer:"
+ "subVariantsForVariant:"
+ "supportedDimensionsForParameters:"
+ "update depth map referances of %d points"
+ "v104@0:8^{__CVBuffer=}16{?=[4]}24@\"NSDictionary\"88d96"
+ "v24@0:8^{?=Q@BiifffQIB}16"
+ "{unordered_map<unsigned long, ADCameraCalibration *, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, ADCameraCalibration *>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, ADCameraCalibration *>, std::__unordered_map_hasher<unsigned long, std::pair<const unsigned long, ADCameraCalibration *>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::pair<const unsigned long, ADCameraCalibration *>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::pair<const unsigned long, ADCameraCalibration *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, ADCameraCalibration *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, ADCameraCalibration *>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, ADCameraCalibration *>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, ADCameraCalibration *>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_map<unsigned long, CGSize, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, CGSize>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, CGSize>, std::__unordered_map_hasher<unsigned long, std::pair<const unsigned long, CGSize>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::pair<const unsigned long, CGSize>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::pair<const unsigned long, CGSize>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, CGSize>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, CGSize>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, CGSize>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, CGSize>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_map<unsigned long, PixelBufferSharedPtr, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, PixelBufferSharedPtr>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, PixelBufferSharedPtr>, std::__unordered_map_hasher<unsigned long, std::pair<const unsigned long, PixelBufferSharedPtr>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::pair<const unsigned long, PixelBufferSharedPtr>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::pair<const unsigned long, PixelBufferSharedPtr>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, PixelBufferSharedPtr>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, PixelBufferSharedPtr>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, PixelBufferSharedPtr>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, PixelBufferSharedPtr>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_map<unsigned long, simd_float4x4, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, simd_float4x4>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, simd_float4x4>, std::__unordered_map_hasher<unsigned long, std::pair<const unsigned long, simd_float4x4>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::pair<const unsigned long, simd_float4x4>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::pair<const unsigned long, simd_float4x4>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, simd_float4x4>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, simd_float4x4>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, simd_float4x4>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, simd_float4x4>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_map<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, std::__unordered_map_hasher<unsigned long, std::pair<const unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::pair<const unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::pair<const unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "/Library/Caches/com.apple.xbs/Sources/AppleDepth/AppleDepth/Executors/ADJasperPearlInFieldCalibrationExecutor.mm"
- "/Library/Caches/com.apple.xbs/Sources/AppleDepth/AppleDepth/InFieldCalibrations/JPC/Blocks/GMC_J/JPC_PORGMCJ_Block.mm"
- "/Library/Caches/com.apple.xbs/Sources/AppleDepth/AppleDepth/InFieldCalibrations/JPC/Blocks/IFA/JPC_PORIFABlock.mm"
- "/Library/Caches/com.apple.xbs/Sources/AppleDepth/AppleDepth/InFieldCalibrations/JPC/Blocks/OutputValidation/JPC_PORGMCJ_OutputValidation_Block.mm"
- "/Library/Caches/com.apple.xbs/Sources/AppleDepth/AppleDepth/InFieldCalibrations/JPC/Blocks/Preprocessor/JPC_PORPreprocessorBlock.mm"
- "/Library/Caches/com.apple.xbs/Sources/AppleDepth/AppleDepth/InFieldCalibrations/JPC/JPC.mm"
- "/Library/Caches/com.apple.xbs/Sources/AppleDepth/AppleDepth/Utils/ADInFieldCalibrationInterSessionData.mm"
- "150.9"
- "ADJasperColorInFieldCalibration jasper controller failed: number of good spots is too low"
- "ADJasperColorInFieldCalibration jasper controller failed: number of valid spots is too low"
- "ADJasperColorInFieldCalibration preprocessInputColorFrameImpl fail for to high angular velocity"
- "ADJasperColorInFieldCalibration run results relative to previouse [%f, %f, %f]"
- "ADJasperColorInFieldCalibration run results relative to previouse post ISF [%f, %f, %f]"
- "NetworkTrainingWidth"
- "PCEBias"
- "Pearl Color In-Field calibration pipeline init for"
- "UIImage"
- "Unknown device frequency (%@). Will use 24MHz..."
- "a!2"
- "executeForPreprocesed features index %d/%d"
- "failed preProcessColor jasper"
- "forNetworkColorProcessed"
- "forNetworkPointCloudFilteredUncropped"
- "forNetworkPointCloudProcessed"
- "frameMetadata"
- "imageWithCGImage:"
- "inputColorCameraCalibration"
- "inputDisparity"
- "inputPointCloud2ColorTransform"
- "inputPointCloud_%d"
- "jasper2ColorTransform"
- "methodForSelector:"
- "outputProcessed"
- "outputProcessedScaled"
- "preProcessedDisparity"
- "setting verboseLogs: %d"
- "{unordered_map<unsigned long, ADCameraCalibration *, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, ADCameraCalibration *>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, ADCameraCalibration *>, std::__unordered_map_hasher<unsigned long, std::__hash_value_type<unsigned long, ADCameraCalibration *>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::__hash_value_type<unsigned long, ADCameraCalibration *>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::__hash_value_type<unsigned long, ADCameraCalibration *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, ADCameraCalibration *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, ADCameraCalibration *>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, ADCameraCalibration *>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, ADCameraCalibration *>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{unordered_map<unsigned long, CGSize, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, CGSize>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, CGSize>, std::__unordered_map_hasher<unsigned long, std::__hash_value_type<unsigned long, CGSize>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::__hash_value_type<unsigned long, CGSize>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::__hash_value_type<unsigned long, CGSize>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, CGSize>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, CGSize>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, CGSize>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, CGSize>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{unordered_map<unsigned long, PixelBufferSharedPtr, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, PixelBufferSharedPtr>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, PixelBufferSharedPtr>, std::__unordered_map_hasher<unsigned long, std::__hash_value_type<unsigned long, PixelBufferSharedPtr>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::__hash_value_type<unsigned long, PixelBufferSharedPtr>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::__hash_value_type<unsigned long, PixelBufferSharedPtr>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, PixelBufferSharedPtr>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, PixelBufferSharedPtr>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, PixelBufferSharedPtr>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, PixelBufferSharedPtr>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{unordered_map<unsigned long, simd_float4x4, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, simd_float4x4>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, simd_float4x4>, std::__unordered_map_hasher<unsigned long, std::__hash_value_type<unsigned long, simd_float4x4>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::__hash_value_type<unsigned long, simd_float4x4>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::__hash_value_type<unsigned long, simd_float4x4>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, simd_float4x4>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, simd_float4x4>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, simd_float4x4>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, simd_float4x4>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{unordered_map<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, std::__unordered_map_hasher<unsigned long, std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"

```
