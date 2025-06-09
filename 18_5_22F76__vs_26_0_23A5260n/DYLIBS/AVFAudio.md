## AVFAudio

> `/System/Library/Frameworks/AVFAudio.framework/AVFAudio`

```diff

-684.603.0.0.0
-  __TEXT.__text: 0x114d34
-  __TEXT.__auth_stubs: 0x1fd0
-  __TEXT.__objc_methlist: 0x576c
+735.0.0.0.0
+  __TEXT.__text: 0x118e4c
+  __TEXT.__auth_stubs: 0x2160
+  __TEXT.__objc_methlist: 0x589c
   __TEXT.__dlopen_cstrs: 0xa9
-  __TEXT.__const: 0x656
-  __TEXT.__gcc_except_tab: 0x14dc4
-  __TEXT.__cstring: 0xe5b9
-  __TEXT.__oslogstring: 0x177de
-  __TEXT.__unwind_info: 0x5ca0
-  __TEXT.__objc_classname: 0xa13
-  __TEXT.__objc_methname: 0xbc35
-  __TEXT.__objc_methtype: 0x27ca
-  __TEXT.__objc_stubs: 0x7900
-  __DATA_CONST.__got: 0x578
-  __DATA_CONST.__const: 0x1938
-  __DATA_CONST.__objc_classlist: 0x308
+  __TEXT.__const: 0x700
+  __TEXT.__gcc_except_tab: 0x1552c
+  __TEXT.__cstring: 0xed7c
+  __TEXT.__oslogstring: 0x17c43
+  __TEXT.__unwind_info: 0x5f78
+  __TEXT.__objc_classname: 0xa45
+  __TEXT.__objc_methname: 0xbe4a
+  __TEXT.__objc_methtype: 0x284d
+  __TEXT.__objc_stubs: 0x7a80
+  __DATA_CONST.__got: 0x5f0
+  __DATA_CONST.__const: 0x19a8
+  __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3230
+  __DATA_CONST.__objc_selrefs: 0x32c0
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x2b0
-  __AUTH_CONST.__auth_got: 0x1000
-  __AUTH_CONST.__const: 0x67b8
-  __AUTH_CONST.__cfstring: 0x3580
-  __AUTH_CONST.__objc_const: 0x85c8
-  __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x41c
+  __DATA_CONST.__objc_superrefs: 0x2b8
+  __DATA_CONST.__objc_arraydata: 0x20
+  __AUTH_CONST.__auth_got: 0x10c8
+  __AUTH_CONST.__const: 0x6818
+  __AUTH_CONST.__cfstring: 0x3660
+  __AUTH_CONST.__objc_const: 0x8818
+  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x430
   __DATA.__data: 0x820
-  __DATA.__bss: 0x198
+  __DATA.__bss: 0x1d8
   __DATA_DIRTY.__objc_data: 0x1db0
   __DATA_DIRTY.__data: 0x90
-  __DATA_DIRTY.__bss: 0x260
+  __DATA_DIRTY.__bss: 0x258
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMIDI.framework/CoreMIDI
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/PrivateFrameworks/AudioSession.framework/AudioSession
   - /System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore
   - /System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 55A706AB-4390-32D2-8D85-65A954B832C1
-  Functions: 3820
-  Symbols:   12654
-  CStrings:  6270
+  - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: C8331BED-B411-3534-B266-48ADFE6359AC
+  Functions: 3864
+  Symbols:   12948
+  CStrings:  6360
 
Symbols:
+ +[AVAudioSharedBufferToken supportsSecureCoding]
+ -[AVAudioFile init]
+ -[AVAudioFormat .cxx_construct]
+ -[AVAudioFormat .cxx_destruct]
+ -[AVAudioOutputNode intendedSpatialExperience]
+ -[AVAudioOutputNode setIntendedSpatialExperience:]
+ -[AVAudioPlayer intendedSpatialExperience]
+ -[AVAudioPlayer setIntendedSpatialExperience:]
+ -[AVAudioPlayer setUseInjectionDevice:]
+ -[AVAudioPlayer useInjectionDevice]
+ -[AVAudioSharedBufferToken .cxx_construct]
+ -[AVAudioSharedBufferToken .cxx_destruct]
+ -[AVAudioSharedBufferToken encodeWithCoder:]
+ -[AVAudioSharedBufferToken initWithCoder:]
+ -[AVAudioSharedBufferToken initWithSurface:taskToken:]
+ -[AVAudioSharedBufferToken surfaceXPCType]
+ -[AVAudioSharedBufferToken surface]
+ -[AVAudioSharedBufferToken taskTokenXPCType]
+ -[AVAudioSharedBufferToken taskToken]
+ -[AVAudioSharedPCMBuffer backedBySharedMemory]
+ -[AVAudioSharedPCMBuffer initWithPCMFormat:frameCapacity:]
+ -[AVAudioSharedPCMBuffer initWithPCMFormat:sharedBufferToken:]
+ -[AVAudioSharedPCMBuffer sharedBufferToken]
+ GCC_except_table1011
+ GCC_except_table1021
+ GCC_except_table1037
+ GCC_except_table1038
+ GCC_except_table1039
+ GCC_except_table1041
+ GCC_except_table105
+ GCC_except_table1052
+ GCC_except_table106
+ GCC_except_table1083
+ GCC_except_table1086
+ GCC_except_table1104
+ GCC_except_table112
+ GCC_except_table1128
+ GCC_except_table1129
+ GCC_except_table1130
+ GCC_except_table1134
+ GCC_except_table1135
+ GCC_except_table114
+ GCC_except_table1149
+ GCC_except_table1157
+ GCC_except_table1179
+ GCC_except_table1196
+ GCC_except_table1197
+ GCC_except_table1198
+ GCC_except_table1199
+ GCC_except_table1200
+ GCC_except_table1201
+ GCC_except_table121
+ GCC_except_table1220
+ GCC_except_table1221
+ GCC_except_table1225
+ GCC_except_table1226
+ GCC_except_table1227
+ GCC_except_table124
+ GCC_except_table1253
+ GCC_except_table1254
+ GCC_except_table126
+ GCC_except_table1264
+ GCC_except_table1265
+ GCC_except_table1266
+ GCC_except_table1267
+ GCC_except_table1268
+ GCC_except_table1269
+ GCC_except_table1270
+ GCC_except_table1300
+ GCC_except_table131
+ GCC_except_table1314
+ GCC_except_table1316
+ GCC_except_table1318
+ GCC_except_table1358
+ GCC_except_table1359
+ GCC_except_table136
+ GCC_except_table1370
+ GCC_except_table1371
+ GCC_except_table1372
+ GCC_except_table1402
+ GCC_except_table1403
+ GCC_except_table1406
+ GCC_except_table1407
+ GCC_except_table1408
+ GCC_except_table1409
+ GCC_except_table141
+ GCC_except_table1410
+ GCC_except_table1411
+ GCC_except_table1414
+ GCC_except_table1415
+ GCC_except_table1417
+ GCC_except_table1418
+ GCC_except_table1419
+ GCC_except_table1420
+ GCC_except_table1421
+ GCC_except_table1422
+ GCC_except_table1423
+ GCC_except_table1424
+ GCC_except_table1425
+ GCC_except_table1426
+ GCC_except_table1430
+ GCC_except_table1431
+ GCC_except_table1434
+ GCC_except_table1435
+ GCC_except_table1437
+ GCC_except_table1438
+ GCC_except_table1439
+ GCC_except_table1440
+ GCC_except_table1443
+ GCC_except_table1449
+ GCC_except_table1450
+ GCC_except_table1451
+ GCC_except_table1452
+ GCC_except_table1453
+ GCC_except_table1454
+ GCC_except_table1455
+ GCC_except_table1456
+ GCC_except_table1457
+ GCC_except_table1469
+ GCC_except_table1473
+ GCC_except_table1474
+ GCC_except_table1494
+ GCC_except_table1496
+ GCC_except_table1497
+ GCC_except_table1498
+ GCC_except_table1499
+ GCC_except_table1501
+ GCC_except_table1502
+ GCC_except_table1503
+ GCC_except_table1504
+ GCC_except_table1506
+ GCC_except_table1507
+ GCC_except_table1524
+ GCC_except_table1531
+ GCC_except_table1543
+ GCC_except_table1544
+ GCC_except_table1547
+ GCC_except_table1551
+ GCC_except_table1552
+ GCC_except_table1553
+ GCC_except_table1555
+ GCC_except_table1557
+ GCC_except_table1560
+ GCC_except_table1565
+ GCC_except_table1576
+ GCC_except_table1577
+ GCC_except_table1578
+ GCC_except_table1579
+ GCC_except_table1582
+ GCC_except_table1599
+ GCC_except_table1600
+ GCC_except_table1602
+ GCC_except_table1604
+ GCC_except_table1606
+ GCC_except_table1608
+ GCC_except_table161
+ GCC_except_table1610
+ GCC_except_table1611
+ GCC_except_table1612
+ GCC_except_table1620
+ GCC_except_table1622
+ GCC_except_table1624
+ GCC_except_table163
+ GCC_except_table1632
+ GCC_except_table1633
+ GCC_except_table164
+ GCC_except_table1641
+ GCC_except_table1654
+ GCC_except_table1659
+ GCC_except_table166
+ GCC_except_table1666
+ GCC_except_table1667
+ GCC_except_table1668
+ GCC_except_table1673
+ GCC_except_table1676
+ GCC_except_table1677
+ GCC_except_table1679
+ GCC_except_table1680
+ GCC_except_table1684
+ GCC_except_table1685
+ GCC_except_table1689
+ GCC_except_table1692
+ GCC_except_table1694
+ GCC_except_table1719
+ GCC_except_table172
+ GCC_except_table1721
+ GCC_except_table1722
+ GCC_except_table1723
+ GCC_except_table1724
+ GCC_except_table1725
+ GCC_except_table1728
+ GCC_except_table1729
+ GCC_except_table1730
+ GCC_except_table1732
+ GCC_except_table1733
+ GCC_except_table174
+ GCC_except_table175
+ GCC_except_table1778
+ GCC_except_table1782
+ GCC_except_table1791
+ GCC_except_table1799
+ GCC_except_table180
+ GCC_except_table1802
+ GCC_except_table1806
+ GCC_except_table1808
+ GCC_except_table181
+ GCC_except_table1817
+ GCC_except_table182
+ GCC_except_table1824
+ GCC_except_table1829
+ GCC_except_table1834
+ GCC_except_table1835
+ GCC_except_table1845
+ GCC_except_table1847
+ GCC_except_table1850
+ GCC_except_table1851
+ GCC_except_table1852
+ GCC_except_table1853
+ GCC_except_table1854
+ GCC_except_table1855
+ GCC_except_table1856
+ GCC_except_table1857
+ GCC_except_table1872
+ GCC_except_table188
+ GCC_except_table1880
+ GCC_except_table1887
+ GCC_except_table1888
+ GCC_except_table1890
+ GCC_except_table190
+ GCC_except_table1922
+ GCC_except_table1925
+ GCC_except_table1927
+ GCC_except_table1928
+ GCC_except_table1929
+ GCC_except_table1931
+ GCC_except_table1932
+ GCC_except_table1933
+ GCC_except_table1934
+ GCC_except_table1935
+ GCC_except_table1936
+ GCC_except_table1937
+ GCC_except_table1938
+ GCC_except_table1939
+ GCC_except_table1944
+ GCC_except_table1945
+ GCC_except_table1947
+ GCC_except_table1961
+ GCC_except_table1966
+ GCC_except_table1967
+ GCC_except_table1969
+ GCC_except_table1981
+ GCC_except_table1983
+ GCC_except_table1984
+ GCC_except_table1985
+ GCC_except_table1986
+ GCC_except_table1987
+ GCC_except_table1988
+ GCC_except_table1991
+ GCC_except_table1993
+ GCC_except_table1997
+ GCC_except_table201
+ GCC_except_table202
+ GCC_except_table204
+ GCC_except_table2086
+ GCC_except_table2088
+ GCC_except_table2089
+ GCC_except_table2090
+ GCC_except_table2098
+ GCC_except_table2099
+ GCC_except_table2100
+ GCC_except_table211
+ GCC_except_table2118
+ GCC_except_table2119
+ GCC_except_table212
+ GCC_except_table2123
+ GCC_except_table2124
+ GCC_except_table2126
+ GCC_except_table2127
+ GCC_except_table2128
+ GCC_except_table2129
+ GCC_except_table2133
+ GCC_except_table2135
+ GCC_except_table2142
+ GCC_except_table2145
+ GCC_except_table2158
+ GCC_except_table2159
+ GCC_except_table2160
+ GCC_except_table2168
+ GCC_except_table2169
+ GCC_except_table2170
+ GCC_except_table2171
+ GCC_except_table2172
+ GCC_except_table2175
+ GCC_except_table2176
+ GCC_except_table219
+ GCC_except_table2203
+ GCC_except_table2204
+ GCC_except_table2205
+ GCC_except_table2247
+ GCC_except_table2259
+ GCC_except_table2260
+ GCC_except_table2262
+ GCC_except_table2263
+ GCC_except_table2265
+ GCC_except_table2266
+ GCC_except_table2267
+ GCC_except_table2268
+ GCC_except_table2270
+ GCC_except_table2276
+ GCC_except_table2277
+ GCC_except_table2278
+ GCC_except_table2298
+ GCC_except_table2326
+ GCC_except_table2328
+ GCC_except_table2330
+ GCC_except_table2331
+ GCC_except_table2338
+ GCC_except_table2339
+ GCC_except_table2341
+ GCC_except_table2349
+ GCC_except_table2350
+ GCC_except_table2351
+ GCC_except_table2358
+ GCC_except_table2361
+ GCC_except_table2374
+ GCC_except_table2375
+ GCC_except_table2387
+ GCC_except_table2393
+ GCC_except_table2394
+ GCC_except_table2395
+ GCC_except_table2401
+ GCC_except_table2411
+ GCC_except_table2418
+ GCC_except_table2422
+ GCC_except_table2424
+ GCC_except_table2425
+ GCC_except_table2428
+ GCC_except_table2429
+ GCC_except_table2430
+ GCC_except_table2431
+ GCC_except_table2436
+ GCC_except_table2449
+ GCC_except_table2450
+ GCC_except_table2452
+ GCC_except_table2460
+ GCC_except_table2461
+ GCC_except_table2463
+ GCC_except_table2464
+ GCC_except_table2468
+ GCC_except_table2471
+ GCC_except_table2476
+ GCC_except_table2479
+ GCC_except_table248
+ GCC_except_table2488
+ GCC_except_table2518
+ GCC_except_table2519
+ GCC_except_table2520
+ GCC_except_table2521
+ GCC_except_table2523
+ GCC_except_table2525
+ GCC_except_table2535
+ GCC_except_table2536
+ GCC_except_table2537
+ GCC_except_table2538
+ GCC_except_table2539
+ GCC_except_table2549
+ GCC_except_table2565
+ GCC_except_table2593
+ GCC_except_table2598
+ GCC_except_table2599
+ GCC_except_table2600
+ GCC_except_table2601
+ GCC_except_table2602
+ GCC_except_table2603
+ GCC_except_table2604
+ GCC_except_table2605
+ GCC_except_table2606
+ GCC_except_table2607
+ GCC_except_table2608
+ GCC_except_table2609
+ GCC_except_table2610
+ GCC_except_table2611
+ GCC_except_table2612
+ GCC_except_table2613
+ GCC_except_table264
+ GCC_except_table2642
+ GCC_except_table2650
+ GCC_except_table2655
+ GCC_except_table2656
+ GCC_except_table266
+ GCC_except_table2660
+ GCC_except_table2663
+ GCC_except_table2671
+ GCC_except_table2672
+ GCC_except_table2674
+ GCC_except_table2682
+ GCC_except_table2684
+ GCC_except_table2687
+ GCC_except_table271
+ GCC_except_table2716
+ GCC_except_table2722
+ GCC_except_table2723
+ GCC_except_table273
+ GCC_except_table2732
+ GCC_except_table274
+ GCC_except_table2757
+ GCC_except_table2758
+ GCC_except_table2767
+ GCC_except_table2769
+ GCC_except_table2772
+ GCC_except_table2776
+ GCC_except_table2779
+ GCC_except_table2783
+ GCC_except_table2786
+ GCC_except_table2793
+ GCC_except_table2797
+ GCC_except_table280
+ GCC_except_table2800
+ GCC_except_table2804
+ GCC_except_table2807
+ GCC_except_table2819
+ GCC_except_table2826
+ GCC_except_table2829
+ GCC_except_table283
+ GCC_except_table2836
+ GCC_except_table2845
+ GCC_except_table285
+ GCC_except_table2857
+ GCC_except_table2864
+ GCC_except_table2871
+ GCC_except_table2874
+ GCC_except_table2876
+ GCC_except_table2883
+ GCC_except_table2886
+ GCC_except_table2889
+ GCC_except_table2890
+ GCC_except_table2891
+ GCC_except_table2892
+ GCC_except_table2893
+ GCC_except_table2896
+ GCC_except_table291
+ GCC_except_table2940
+ GCC_except_table2941
+ GCC_except_table2942
+ GCC_except_table2944
+ GCC_except_table2945
+ GCC_except_table2946
+ GCC_except_table2947
+ GCC_except_table2948
+ GCC_except_table2949
+ GCC_except_table2954
+ GCC_except_table2955
+ GCC_except_table2956
+ GCC_except_table2959
+ GCC_except_table296
+ GCC_except_table2960
+ GCC_except_table2964
+ GCC_except_table2976
+ GCC_except_table2977
+ GCC_except_table2978
+ GCC_except_table2982
+ GCC_except_table2986
+ GCC_except_table2987
+ GCC_except_table2988
+ GCC_except_table2990
+ GCC_except_table2991
+ GCC_except_table2992
+ GCC_except_table2993
+ GCC_except_table2994
+ GCC_except_table2996
+ GCC_except_table2997
+ GCC_except_table2998
+ GCC_except_table3000
+ GCC_except_table3004
+ GCC_except_table3005
+ GCC_except_table3008
+ GCC_except_table301
+ GCC_except_table3010
+ GCC_except_table3057
+ GCC_except_table3062
+ GCC_except_table3064
+ GCC_except_table3067
+ GCC_except_table3069
+ GCC_except_table308
+ GCC_except_table3083
+ GCC_except_table3084
+ GCC_except_table3097
+ GCC_except_table3098
+ GCC_except_table310
+ GCC_except_table3115
+ GCC_except_table313
+ GCC_except_table3137
+ GCC_except_table3141
+ GCC_except_table3148
+ GCC_except_table315
+ GCC_except_table3154
+ GCC_except_table3155
+ GCC_except_table3162
+ GCC_except_table3163
+ GCC_except_table3164
+ GCC_except_table3168
+ GCC_except_table3170
+ GCC_except_table3172
+ GCC_except_table3174
+ GCC_except_table3178
+ GCC_except_table3180
+ GCC_except_table3184
+ GCC_except_table3188
+ GCC_except_table3189
+ GCC_except_table3195
+ GCC_except_table3197
+ GCC_except_table3199
+ GCC_except_table3201
+ GCC_except_table3203
+ GCC_except_table3205
+ GCC_except_table3207
+ GCC_except_table3209
+ GCC_except_table3211
+ GCC_except_table3213
+ GCC_except_table3214
+ GCC_except_table3215
+ GCC_except_table3221
+ GCC_except_table3224
+ GCC_except_table3250
+ GCC_except_table3257
+ GCC_except_table3260
+ GCC_except_table327
+ GCC_except_table328
+ GCC_except_table3286
+ GCC_except_table3289
+ GCC_except_table3290
+ GCC_except_table3292
+ GCC_except_table3309
+ GCC_except_table3310
+ GCC_except_table3315
+ GCC_except_table3339
+ GCC_except_table3341
+ GCC_except_table3351
+ GCC_except_table3352
+ GCC_except_table3353
+ GCC_except_table3354
+ GCC_except_table3355
+ GCC_except_table3356
+ GCC_except_table3357
+ GCC_except_table3358
+ GCC_except_table3359
+ GCC_except_table336
+ GCC_except_table3360
+ GCC_except_table3361
+ GCC_except_table3366
+ GCC_except_table337
+ GCC_except_table3370
+ GCC_except_table3373
+ GCC_except_table3402
+ GCC_except_table3403
+ GCC_except_table3424
+ GCC_except_table3425
+ GCC_except_table3426
+ GCC_except_table3427
+ GCC_except_table3428
+ GCC_except_table3432
+ GCC_except_table3433
+ GCC_except_table3434
+ GCC_except_table3435
+ GCC_except_table3436
+ GCC_except_table3437
+ GCC_except_table3438
+ GCC_except_table3439
+ GCC_except_table3440
+ GCC_except_table3441
+ GCC_except_table3444
+ GCC_except_table3475
+ GCC_except_table3476
+ GCC_except_table3477
+ GCC_except_table3478
+ GCC_except_table3480
+ GCC_except_table3482
+ GCC_except_table3483
+ GCC_except_table3485
+ GCC_except_table3486
+ GCC_except_table3487
+ GCC_except_table3489
+ GCC_except_table349
+ GCC_except_table3491
+ GCC_except_table3493
+ GCC_except_table3496
+ GCC_except_table3501
+ GCC_except_table3502
+ GCC_except_table3516
+ GCC_except_table3518
+ GCC_except_table3520
+ GCC_except_table3525
+ GCC_except_table3536
+ GCC_except_table3544
+ GCC_except_table3553
+ GCC_except_table3554
+ GCC_except_table3557
+ GCC_except_table3558
+ GCC_except_table3561
+ GCC_except_table3569
+ GCC_except_table3575
+ GCC_except_table3576
+ GCC_except_table3578
+ GCC_except_table3618
+ GCC_except_table3624
+ GCC_except_table3630
+ GCC_except_table3641
+ GCC_except_table3662
+ GCC_except_table3664
+ GCC_except_table3667
+ GCC_except_table3670
+ GCC_except_table3672
+ GCC_except_table3673
+ GCC_except_table3674
+ GCC_except_table3675
+ GCC_except_table3676
+ GCC_except_table3677
+ GCC_except_table3678
+ GCC_except_table3679
+ GCC_except_table3680
+ GCC_except_table3681
+ GCC_except_table3682
+ GCC_except_table3683
+ GCC_except_table3685
+ GCC_except_table3686
+ GCC_except_table3688
+ GCC_except_table3696
+ GCC_except_table3698
+ GCC_except_table3724
+ GCC_except_table3725
+ GCC_except_table3727
+ GCC_except_table3729
+ GCC_except_table3731
+ GCC_except_table3735
+ GCC_except_table3736
+ GCC_except_table3740
+ GCC_except_table3741
+ GCC_except_table3744
+ GCC_except_table3777
+ GCC_except_table3778
+ GCC_except_table3779
+ GCC_except_table3781
+ GCC_except_table3786
+ GCC_except_table3787
+ GCC_except_table3788
+ GCC_except_table3789
+ GCC_except_table3790
+ GCC_except_table3791
+ GCC_except_table3792
+ GCC_except_table3793
+ GCC_except_table3794
+ GCC_except_table3795
+ GCC_except_table3796
+ GCC_except_table3797
+ GCC_except_table3798
+ GCC_except_table3800
+ GCC_except_table3802
+ GCC_except_table3803
+ GCC_except_table3804
+ GCC_except_table3806
+ GCC_except_table3812
+ GCC_except_table3813
+ GCC_except_table3814
+ GCC_except_table3815
+ GCC_except_table3817
+ GCC_except_table3818
+ GCC_except_table3819
+ GCC_except_table3820
+ GCC_except_table3825
+ GCC_except_table3828
+ GCC_except_table3829
+ GCC_except_table3844
+ GCC_except_table3855
+ GCC_except_table3856
+ GCC_except_table387
+ GCC_except_table3890
+ GCC_except_table3891
+ GCC_except_table3894
+ GCC_except_table406
+ GCC_except_table416
+ GCC_except_table417
+ GCC_except_table418
+ GCC_except_table419
+ GCC_except_table428
+ GCC_except_table446
+ GCC_except_table447
+ GCC_except_table479
+ GCC_except_table492
+ GCC_except_table494
+ GCC_except_table495
+ GCC_except_table512
+ GCC_except_table515
+ GCC_except_table517
+ GCC_except_table518
+ GCC_except_table530
+ GCC_except_table531
+ GCC_except_table532
+ GCC_except_table533
+ GCC_except_table542
+ GCC_except_table564
+ GCC_except_table566
+ GCC_except_table567
+ GCC_except_table575
+ GCC_except_table584
+ GCC_except_table585
+ GCC_except_table586
+ GCC_except_table59
+ GCC_except_table592
+ GCC_except_table593
+ GCC_except_table599
+ GCC_except_table604
+ GCC_except_table605
+ GCC_except_table606
+ GCC_except_table611
+ GCC_except_table615
+ GCC_except_table644
+ GCC_except_table652
+ GCC_except_table653
+ GCC_except_table657
+ GCC_except_table662
+ GCC_except_table67
+ GCC_except_table673
+ GCC_except_table68
+ GCC_except_table688
+ GCC_except_table694
+ GCC_except_table701
+ GCC_except_table73
+ GCC_except_table74
+ GCC_except_table741
+ GCC_except_table743
+ GCC_except_table746
+ GCC_except_table755
+ GCC_except_table762
+ GCC_except_table765
+ GCC_except_table766
+ GCC_except_table767
+ GCC_except_table768
+ GCC_except_table789
+ GCC_except_table790
+ GCC_except_table802
+ GCC_except_table803
+ GCC_except_table805
+ GCC_except_table813
+ GCC_except_table815
+ GCC_except_table818
+ GCC_except_table830
+ GCC_except_table831
+ GCC_except_table832
+ GCC_except_table833
+ GCC_except_table834
+ GCC_except_table842
+ GCC_except_table843
+ GCC_except_table844
+ GCC_except_table845
+ GCC_except_table853
+ GCC_except_table861
+ GCC_except_table863
+ GCC_except_table87
+ GCC_except_table876
+ GCC_except_table880
+ GCC_except_table884
+ GCC_except_table889
+ GCC_except_table890
+ GCC_except_table899
+ GCC_except_table901
+ GCC_except_table903
+ GCC_except_table904
+ GCC_except_table909
+ GCC_except_table914
+ GCC_except_table916
+ GCC_except_table917
+ GCC_except_table921
+ GCC_except_table93
+ GCC_except_table933
+ GCC_except_table934
+ GCC_except_table935
+ GCC_except_table936
+ GCC_except_table937
+ GCC_except_table938
+ GCC_except_table939
+ GCC_except_table94
+ GCC_except_table959
+ GCC_except_table982
+ GCC_except_table983
+ GCC_except_table984
+ GCC_except_table985
+ GCC_except_table988
+ GCC_except_table990
+ GCC_except_table995
+ GCC_except_table996
+ GCC_except_table998
+ _AVAudioSessionActivationCallTypeKey
+ _AVAudioSessionAvailableInputsChangeNotification
+ _AVAudioSessionAvailableOutputsChangeNotification
+ _AVAudioSessionConformSessionAudioSessionIDKey
+ _AVAudioSessionConformSessionShadowingOptionsKey
+ _AVAudioSessionInterruptorSessionIDKey
+ _AVAudioSessionModeShortFormVideo
+ _AVAudioSessionMuteStateKey
+ _AVAudioSessionOutputMuteStateChangeNotification
+ _AVAudioSessionUserIntentToUnmuteOutputNotification
+ _AVEncoderASPFrequencyKey
+ _AVEncoderContentSourceKey
+ _AVEncoderDynamicRangeControlConfigurationKey
+ _CAAssertRtn
+ _CAVerboseAbort
+ _CFURLGetFileSystemRepresentation
+ _IOSurfaceCreate
+ _IOSurfaceCreateXPCObject
+ _IOSurfaceGetAllocSize
+ _IOSurfaceGetBaseAddress
+ _IOSurfaceLookupFromXPCObject
+ _IOSurfaceSetOwnershipIdentity
+ _IOSurfaceSetValue
+ _NSFileSize
+ _OBJC_CLASS_$_AVAudioSessionCapability
+ _OBJC_CLASS_$_AVAudioSessionPortExtensionBluetoothMicrophone
+ _OBJC_CLASS_$_AVAudioSharedBufferToken
+ _OBJC_CLASS_$_AVAudioSharedPCMBuffer
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSXPCCoder
+ _OBJC_IVAR_$_AVAudioFormat._magicCookieMutex
+ _OBJC_IVAR_$_AVAudioOutputNode._intendedSpatialExperience
+ _OBJC_IVAR_$_AVAudioPlayer._intendedSpatialExperience
+ _OBJC_IVAR_$_AVAudioSharedBufferToken.surface
+ _OBJC_IVAR_$_AVAudioSharedBufferToken.taskToken
+ _OBJC_METACLASS_$_AVAudioSessionCapability
+ _OBJC_METACLASS_$_AVAudioSessionPortExtensionBluetoothMicrophone
+ _OBJC_METACLASS_$_AVAudioSharedBufferToken
+ _OBJC_METACLASS_$_AVAudioSharedPCMBuffer
+ __OBJC_$_CLASS_METHODS_AVAudioSharedBufferToken
+ __OBJC_$_CLASS_PROP_LIST_AVAudioSharedBufferToken
+ __OBJC_$_INSTANCE_METHODS_AVAudioSharedBufferToken
+ __OBJC_$_INSTANCE_METHODS_AVAudioSharedPCMBuffer
+ __OBJC_$_INSTANCE_VARIABLES_AVAudioOutputNode
+ __OBJC_$_INSTANCE_VARIABLES_AVAudioSharedBufferToken
+ __OBJC_$_PROP_LIST_AVAudioOutputNode
+ __OBJC_$_PROP_LIST_AVAudioSharedPCMBuffer
+ __OBJC_CLASS_PROTOCOLS_$_AVAudioSharedBufferToken
+ __OBJC_CLASS_RO_$_AVAudioSharedBufferToken
+ __OBJC_CLASS_RO_$_AVAudioSharedPCMBuffer
+ __OBJC_METACLASS_RO_$_AVAudioSharedBufferToken
+ __OBJC_METACLASS_RO_$_AVAudioSharedPCMBuffer
+ __Z19IsDSPGraphSupportedv
+ __ZGVZL17gAVAudioBufferLogvE6global.8847
+ __ZL16getFloat64ForKeyP12NSDictionaryP8NSStringRdRi
+ __ZL17AudioSessionClassv
+ __ZL17gAVAudioBufferLogv.8838
+ __ZN10applesauce2CF9ObjectRefIP11__IOSurfaceED1Ev
+ __ZN10applesauce2CF9ObjectRefIP11__IOSurfaceED2Ev
+ __ZN10applesauce2CF9StringRefD2Ev
+ __ZN11ElapsedTimeC1EPKcS1_b
+ __ZN11ElapsedTimeD1Ev
+ __ZN12CADeprecated17RealtimeMessengerD0Ev
+ __ZN12CADeprecated17RealtimeMessengerD1Ev
+ __ZN12CADeprecated17RealtimeMessengerD2Ev
+ __ZN12CADeprecated19RealtimeDeallocatorD0Ev
+ __ZN12CADeprecated19RealtimeDeallocatorD1Ev
+ __ZN12CADeprecated9CAPThread5EntryEPv
+ __ZN12_GLOBAL__N_113SegmentReader11getSizeProcEPv
+ __ZN12_GLOBAL__N_113SegmentReader8readProcEPvxjS1_Pj
+ __ZN16AVAudioClockImplC2EP19AVAudioNodeImplBase
+ __ZN16CAAudioTimeStamp5kZeroE
+ __ZN24CAStreamBasicDescriptionC1EdjNS_15CommonPCMFormatEb
+ __ZN33unilaterally_billed_shared_memoryD1Ev
+ __ZN4MIDIL13_gMessageSizeE
+ __ZN5caulk10concurrent12atomic_valueI14AudioTimeStampLi2ELi6EE5storeERKS2_
+ __ZN5caulk10concurrent7details8spinloop4spinEv
+ __ZN5caulk16inplace_functionIFvPKN4MIDI16LegacyPacketListEELm48ELm8ENS_23inplace_function_detail9rt_vtableEE16k_wrapper_vtableIZZN17AUGraphMIDINodeV332AllocateMIDIOutputEventListBlockEvEUb_E3$_3EE
+ __ZN5caulk23inplace_function_detail9rt_vtableIvJPKN4MIDI16LegacyPacketListEEE5emptyE
+ __ZN5caulk23rt_safe_memory_resource11rt_allocateEmm
+ __ZN5caulk23rt_safe_memory_resource13rt_deallocateEPvmm
+ __ZN5caulk24g_realtime_safe_resourceE
+ __ZN5caulk4mach14error_categoryD0Ev
+ __ZN5caulk4mach14error_categoryD1Ev
+ __ZN5caulk4mach9mach_portD2Ev
+ __ZN5caulk7numeric15exceptional_addImEET_S2_S2_
+ __ZN5caulk7product16get_device_classEv
+ __ZN9AVAEBlockIU13block_pointerFiPjPK14AudioTimeStampjlP15AudioBufferListEED2Ev
+ __ZNK24CAStreamBasicDescription8AsStringEPcm
+ __ZNK5caulk10concurrent12atomic_valueI14AudioTimeStampLi2ELi6EE4loadEv
+ __ZNK5caulk4mach14error_category4nameEv
+ __ZNK5caulk4mach14error_category7messageEi
+ __ZNKSt3__110__function6__funcIZN13AUGraphParser14InitializeNodeERK18AVAudioEngineGraphR17AUGraphNodeBaseV3jbE3$_0NS_9allocatorIS8_EEF16ETraversalStatusS7_P17AUGraphConnectionEE7__cloneEPNS0_6__baseISE_EE
+ __ZNKSt3__110__function6__funcIZN13AUGraphParser14InitializeNodeERK18AVAudioEngineGraphR17AUGraphNodeBaseV3jbE3$_0NS_9allocatorIS8_EEF16ETraversalStatusS7_P17AUGraphConnectionEE7__cloneEv
+ __ZNKSt3__114error_category10equivalentERKNS_10error_codeEi
+ __ZNKSt3__114error_category10equivalentEiRKNS_15error_conditionE
+ __ZNKSt3__114error_category23default_error_conditionEi
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt12out_of_rangeC1B8ne200100EPKc
+ __ZNSt13runtime_errorC1EPKc
+ __ZNSt13runtime_errorC2EPKc
+ __ZNSt13runtime_errorD1Ev
+ __ZNSt14overflow_errorC1B8ne200100EPKc
+ __ZNSt14overflow_errorD1Ev
+ __ZNSt3__110__function12__value_funcIF16ETraversalStatusR17AUGraphNodeBaseV3P17AUGraphConnectionEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrI19AVVCRecordingEngineEEEEC2B8ne200100ERKS6_
+ __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrI19AVVCRecordingEngineEEEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvbEED2B8ne200100Ev
+ __ZNSt3__110__function6__funcIZN13AUGraphParser14InitializeNodeERK18AVAudioEngineGraphR17AUGraphNodeBaseV3jbE3$_0NS_9allocatorIS8_EEF16ETraversalStatusS7_P17AUGraphConnectionEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN13AUGraphParser14InitializeNodeERK18AVAudioEngineGraphR17AUGraphNodeBaseV3jbE3$_0NS_9allocatorIS8_EEF16ETraversalStatusS7_P17AUGraphConnectionEE7destroyEv
+ __ZNSt3__110__function6__funcIZN13AUGraphParser14InitializeNodeERK18AVAudioEngineGraphR17AUGraphNodeBaseV3jbE3$_0NS_9allocatorIS8_EEF16ETraversalStatusS7_P17AUGraphConnectionEED0Ev
+ __ZNSt3__110__function6__funcIZN13AUGraphParser14InitializeNodeERK18AVAudioEngineGraphR17AUGraphNodeBaseV3jbE3$_0NS_9allocatorIS8_EEF16ETraversalStatusS7_P17AUGraphConnectionEED1Ev
+ __ZNSt3__110__function6__funcIZN13AUGraphParser14InitializeNodeERK18AVAudioEngineGraphR17AUGraphNodeBaseV3jbE3$_0NS_9allocatorIS8_EEF16ETraversalStatusS7_P17AUGraphConnectionEEclES7_OSD_
+ __ZNSt3__110shared_ptrI14ControllerImplEC2B8ne200100IS1_Li0EEERKNS_8weak_ptrIT_EE
+ __ZNSt3__110shared_ptrI19AVVCRecordingEngineEC2B8ne200100IS1_Li0EEERKNS_8weak_ptrIT_EE
+ __ZNSt3__110unique_ptrI15AVAudioFileImplNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI17CallbackMessengerNS_14default_deleteIS1_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrI18AVAudioEngineGraphNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI21AVAEGraphStateTrackerNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI22AVAEDispatchQueueTimerNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerF34AVAudioEngineManualRenderingStatusjP15AudioBufferListPiEENS_14default_deleteIS8_EEE5resetB8ne200100EPS8_
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFPK15AudioBufferListjEENS_14default_deleteIS7_EEE5resetB8ne200100EPS7_
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFiPjPK14AudioTimeStampjlP15AudioBufferListEENS_14default_deleteISA_EEE5resetB8ne200100EPSA_
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFiPjPK14AudioTimeStampjlP15AudioBufferListEENS_14default_deleteISA_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFiPjPK14AudioTimeStampjlP15AudioBufferListU13block_pointerFiS2_S5_jlS7_EEENS_14default_deleteISC_EEE5resetB8ne200100EPSC_
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFixhPK13MIDIEventListEENS_14default_deleteIS7_EEE5resetB8ne200100EPS7_
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFixhlPKhEENS_14default_deleteIS6_EEE5resetB8ne200100EPS6_
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFv39AVAudioPlayerNodeCompletionCallbackTypeEENS_14default_deleteIS5_EEE5resetB8ne200100EPS5_
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFvPjPK14AudioTimeStampjlEENS_14default_deleteIS8_EEE5resetB8ne200100EPS8_
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFvjPK14AudioTimeStampjlEENS_14default_deleteIS7_EEE5resetB8ne200100EPS7_
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFvxhlPKhEENS_14default_deleteIS6_EEE5resetB8ne200100EPS6_
+ __ZNSt3__110unique_ptrI9PulseToneNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrIN4MIDI16LegacyPacketListENS1_23LegacyPacketListDeleterEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeI16AVVoiceAlertTypeU8__strongP5NSURLEEPvEENS_22__tree_node_destructorINS_9allocatorIS9_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_3mapINS_4pairIP11AVAudioNodejEEP24AVAudioMixingDestinationNS_4lessIS5_EENS_9allocatorINS2_IKS5_S7_EEEEEENS_14default_deleteISE_EEE5resetB8ne200100EPSE_
+ __ZNSt3__110unique_ptrIZN20AVAudioSequencerImpl4StopEvE3$_0NS_14default_deleteIS2_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIZN20AVAudioSequencerImplD1EvE3$_0NS_14default_deleteIS2_EEED1B8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
+ __ZNSt3__112construct_atB8ne200100I33unilaterally_billed_shared_memoryJS1_EPS1_EEPT_S4_DpOT0_
+ __ZNSt3__112system_errorC1EiRKNS_14error_categoryEPKc
+ __ZNSt3__112system_errorD1Ev
+ __ZNSt3__113__tree_removeB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__114error_categoryD2Ev
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne200100IONS1_9__variant15__value_visitorIZN17AUGraphNodeBaseV320CreateMIDIConnectionERK21AUGraphMIDIConnectionE3$_0EEJRKNS0_6__baseILNS0_6_TraitE0EJU13block_pointerFixhlPKhEU13block_pointerFixhPK13MIDIEventListEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne200100IONS1_9__variant15__value_visitorIZN17AUGraphNodeBaseV320CreateMIDIConnectionERK21AUGraphMIDIConnectionE3$_0EEJRKNS0_6__baseILNS0_6_TraitE0EJU13block_pointerFixhlPKhEU13block_pointerFixhPK13MIDIEventListEEEEEEEDcT_DpT0_
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN12CADeprecated10TSingletonINS2_19RealtimeDeallocatorEE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100Ev
+ __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI23EExtAudioGraphNodeStateEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIP17AUGraphNodeBaseV3EEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPN5caulk22pooled_semaphore_mutexEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIxEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne200100Ev
+ __ZNSt3__120__throw_bad_weak_ptrB8ne200100Ev
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne200100EPKc
+ __ZNSt3__120__throw_system_errorEiPKc
+ __ZNSt3__123__optional_storage_baseI33unilaterally_billed_shared_memoryLb0EE13__assign_fromB8ne200100INS_27__optional_move_assign_baseIS1_Lb0EEEEEvOT_
+ __ZNSt3__124__put_character_sequenceB8ne200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__125__throw_bad_function_callB8ne200100Ev
+ __ZNSt3__126__throw_bad_variant_accessB8ne200100Ev
+ __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__14lockB8ne200100IN5caulk22pooled_semaphore_mutexES2_EEvRT_RT0_
+ __ZNSt3__14lockB8ne200100INS_15recursive_mutexEN5caulk23recursive_mutex_adapterINS2_22pooled_semaphore_mutexEEEEEvRT_RT0_
+ __ZNSt3__14lockB8ne200100INS_15recursive_mutexES1_EEvRT_RT0_
+ __ZNSt3__14pairINS_11unique_lockINS_15recursive_mutexEEES3_ED2Ev
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16vectorI12WorkloopInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI23EExtAudioGraphNodeStateNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI30AVAEStreamFormatObserverStructNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN17AUInterfaceBaseV314RenderObserverENS_9allocatorIS2_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIN17AUInterfaceBaseV314RenderObserverENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP11AVAudioNodeNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP17AUGraphNodeBaseV3NS_9allocatorIS2_EEE18__assign_with_sizeB8ne200100IPS2_S7_EEvT_T0_l
+ __ZNSt3__16vectorIP17AUGraphNodeBaseV3NS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP17AUGraphNodeBaseV3NS_9allocatorIS2_EEE20__throw_out_of_rangeB8ne200100Ev
+ __ZNSt3__16vectorIP17AUGraphNodeBaseV3NS_9allocatorIS2_EEE9push_backB8ne200100EOS2_
+ __ZNSt3__16vectorIP17AUGraphNodeBaseV3NS_9allocatorIS2_EEE9push_backB8ne200100ERKS2_
+ __ZNSt3__16vectorIP19AVAudioNodeImplBaseNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP22CompletionHandlerTimerNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPN5caulk22pooled_semaphore_mutexENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPN5caulk22pooled_semaphore_mutexENS_9allocatorIS3_EEE20__throw_out_of_rangeB8ne200100Ev
+ __ZNSt3__16vectorIU8__strongP8NSNumberNS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIU8__strongP8NSNumberNS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIU8__strongP8NSNumberNS_9allocatorIS3_EEE9push_backB8ne200100ERU8__strongKS2_
+ __ZNSt3__16vectorIbNS_9allocatorIbEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIcNS_9allocatorIcEEEC2B8ne200100Em
+ __ZNSt3__16vectorIcNS_9allocatorIcEEEC2B8ne200100EmRKc
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne200100EmRKf
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE16__init_with_sizeB8ne200100IPKjS6_EEvT_T0_m
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_out_of_rangeB8ne200100Ev
+ __ZNSt3__16vectorIxNS_9allocatorIxEEE16__init_with_sizeB8ne200100IPxS5_EEvT_T0_m
+ __ZNSt3__16vectorIxNS_9allocatorIxEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIxNS_9allocatorIxEEE9push_backB8ne200100ERKx
+ __ZNSt3__18optionalI33unilaterally_billed_shared_memoryEaSB8ne200100IS1_vEERS2_OT_
+ __ZNSt3__18optionalIN2CA10BufferListEEaSB8ne200100IS2_vEERS3_OT_
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZTINSt3__112system_errorE
+ __ZTISt13runtime_error
+ __ZTISt14overflow_error
+ __ZTSNSt3__112system_errorE
+ __ZTSSt13runtime_error
+ __ZTSSt14overflow_error
+ __ZTVN12CADeprecated17RealtimeMessengerE
+ __ZTVN12CADeprecated19RealtimeDeallocatorE
+ __ZTVN5caulk4mach14error_categoryE
+ __ZTVNSt3__110__function6__funcIZN13AUGraphParser14InitializeNodeERK18AVAudioEngineGraphR17AUGraphNodeBaseV3jbE3$_0NS_9allocatorIS8_EEF16ETraversalStatusS7_P17AUGraphConnectionEEE
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZTVSt14overflow_error
+ __ZZ37AudioDataAnalysisManagerLibraryLoadervE6libSym.21
+ __ZZ37AudioDataAnalysisManagerLibraryLoadervE6libSym.22
+ __ZZL17AVSharedMemoryLogvE4once
+ __ZZL17AVSharedMemoryLogvE8category
+ __ZZL17gAVAudioBufferLogvE6global.8850
+ __ZZL24AVAudioPlayerLogCategoryvE4once
+ __ZZL24AVAudioPlayerLogCategoryvE8category
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJPKN4MIDI16LegacyPacketListEEEC1EvENUlPvE_8__invokeES7_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJPKN4MIDI16LegacyPacketListEEEC1EvENUlPvOS5_E_8__invokeES7_S8_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJPKN4MIDI16LegacyPacketListEEEC1EvENUlPvS7_E0_8__invokeES7_S7_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJPKN4MIDI16LegacyPacketListEEEC1EvENUlPvS7_E_8__invokeES7_S7_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJPKN4MIDI16LegacyPacketListEEEC1IZZN17AUGraphMIDINodeV332AllocateMIDIOutputEventListBlockEvEUb_E3$_3EENS0_7wrapperIT_EEENUlPvE_8__invokeESD_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJPKN4MIDI16LegacyPacketListEEEC1IZZN17AUGraphMIDINodeV332AllocateMIDIOutputEventListBlockEvEUb_E3$_3EENS0_7wrapperIT_EEENUlPvOS5_E_8__invokeESD_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJPKN4MIDI16LegacyPacketListEEEC1IZZN17AUGraphMIDINodeV332AllocateMIDIOutputEventListBlockEvEUb_E3$_3EENS0_7wrapperIT_EEENUlPvSD_E0_8__invokeESD_SD_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJPKN4MIDI16LegacyPacketListEEEC1IZZN17AUGraphMIDINodeV332AllocateMIDIOutputEventListBlockEvEUb_E3$_3EENS0_7wrapperIT_EEENUlPvSD_E_8__invokeESD_SD_
+ __ZdlPvSt11align_val_t
+ __ZnwmSt11align_val_t
+ ___Block_byref_object_copy_.1284
+ ___Block_byref_object_copy_.192
+ ___Block_byref_object_copy_.3455
+ ___Block_byref_object_copy_.5583
+ ___Block_byref_object_copy_.6379
+ ___Block_byref_object_copy_.721
+ ___Block_byref_object_copy_.7266
+ ___Block_byref_object_copy_.8254
+ ___Block_byref_object_copy_.8772
+ ___Block_byref_object_dispose_.1285
+ ___Block_byref_object_dispose_.193
+ ___Block_byref_object_dispose_.3456
+ ___Block_byref_object_dispose_.5584
+ ___Block_byref_object_dispose_.6380
+ ___Block_byref_object_dispose_.722
+ ___Block_byref_object_dispose_.7267
+ ___Block_byref_object_dispose_.8255
+ ___Block_byref_object_dispose_.8773
+ ____ZL17AVSharedMemoryLogv_block_invoke
+ ____ZL24AVAudioPlayerLogCategoryv_block_invoke
+ ____ZN14ControllerImpl10setContextEP17AVVoiceControllerP19AVVCContextSettingsU13block_pointerFvm14AVVCStreamTypeP7NSErrorE_block_invoke.272
+ ____ZN14ControllerImpl10setContextEP17AVVoiceControllerP19AVVCContextSettingsU13block_pointerFvm14AVVCStreamTypeP7NSErrorE_block_invoke.273
+ ____ZN14ControllerImpl10setContextEP17AVVoiceControllerP19AVVCContextSettingsU13block_pointerFvm14AVVCStreamTypeP7NSErrorE_block_invoke.274
+ ____ZN14ControllerImpl10setContextEP17AVVoiceControllerP19AVVCContextSettingsU13block_pointerFvm14AVVCStreamTypeP7NSErrorE_block_invoke.278
+ ____ZN14ControllerImpl10setContextEP17AVVoiceControllerP19AVVCContextSettingsU13block_pointerFvm14AVVCStreamTypeP7NSErrorE_block_invoke.287
+ ____ZN14ControllerImpl10setContextEP17AVVoiceControllerP19AVVCContextSettingsU13block_pointerFvm14AVVCStreamTypeP7NSErrorE_block_invoke.288
+ ____ZN14ControllerImpl10setContextEP17AVVoiceControllerP19AVVCContextSettingsU13block_pointerFvm14AVVCStreamTypeP7NSErrorE_block_invoke_2.279
+ ____ZN14ControllerImpl15startAlertQueueEU13block_pointerFviE_block_invoke.232
+ ____ZN14ControllerImpl16checkForEndpointEP17AVVoiceControllerP16AudioQueueBufferPfjd_block_invoke.255
+ ____ZN14ControllerImpl16checkForEndpointEP17AVVoiceControllerP16AudioQueueBufferPfjd_block_invoke.257
+ ____ZN14ControllerImpl17handleRouteChangeEP17AVVoiceControllerP14AVAudioSessionPK12NSDictionary_block_invoke.268
+ ____ZN14ControllerImpl19getAVVCSessionStateEmU13block_pointerFvm16AVVCSessionStateP7NSErrorE_block_invoke.445
+ ____ZN14ControllerImpl19setContextForStreamEP17AVVoiceControllerP19AVVCContextSettingsmU13block_pointerFvmbP7NSErrorE_block_invoke.474
+ ____ZN14ControllerImpl19setContextForStreamEP17AVVoiceControllerP19AVVCContextSettingsmU13block_pointerFvmbP7NSErrorE_block_invoke.475
+ ____ZN14ControllerImpl19setContextForStreamEP17AVVoiceControllerP19AVVCContextSettingsmU13block_pointerFvmbP7NSErrorE_block_invoke.477
+ ____ZN14ControllerImpl19setContextForStreamEP17AVVoiceControllerP19AVVCContextSettingsmU13block_pointerFvmbP7NSErrorE_block_invoke.480
+ ____ZN14ControllerImpl19setContextForStreamEP17AVVoiceControllerP19AVVCContextSettingsmU13block_pointerFvmbP7NSErrorE_block_invoke_2.472
+ ____ZN14ControllerImpl19stopRecordForStreamEP17AVVoiceControllermU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke.419
+ ____ZN14ControllerImpl19stopRecordForStreamEP17AVVoiceControllermU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke.420
+ ____ZN14ControllerImpl19stopRecordForStreamEP17AVVoiceControllermU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke.422
+ ____ZN14ControllerImpl20_removeEngineFromMapEP17AVVoiceControllermP8NSStringU13block_pointerFvvE_block_invoke.362
+ ____ZN14ControllerImpl20handleInterruptStartEP17AVVoiceControllerP14AVAudioSessionP12NSDictionary_block_invoke.261
+ ____ZN14ControllerImpl20safeAllQueuesBarrierEv_block_invoke.368
+ ____ZN14ControllerImpl20safeAllQueuesBarrierEv_block_invoke.369
+ ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorEU13block_pointerFv16AVVoiceAlertType14AVVCAlertStateS6_EU13block_pointerFvmP15AVVCAudioBufferE_block_invoke.384
+ ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorEU13block_pointerFv16AVVoiceAlertType14AVVCAlertStateS6_EU13block_pointerFvmP15AVVCAudioBufferE_block_invoke.389
+ ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke.390
+ ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke.391
+ ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke.393
+ ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke.400
+ ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke.407
+ ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke_2.394
+ ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke_2.401
+ ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke_2.404
+ ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke_3.402
+ ____ZN14ControllerImpl22getRecordModeForStreamEmU13block_pointerFvm27AVVoiceControllerRecordModeP7NSErrorE_block_invoke.546
+ ____ZN14ControllerImpl22prepareRecordForStreamEP17AVVoiceControllerP25AVVCPrepareRecordSettingsU13block_pointerFvmbP7NSErrorE_block_invoke.372
+ ____ZN14ControllerImpl22prepareRecordForStreamEP17AVVoiceControllerP25AVVCPrepareRecordSettingsU13block_pointerFvmbP7NSErrorE_block_invoke.373
+ ____ZN14ControllerImpl22prepareRecordForStreamEP17AVVoiceControllerP25AVVCPrepareRecordSettingsU13block_pointerFvmbP7NSErrorE_block_invoke.374
+ ____ZN14ControllerImpl22prepareRecordForStreamEP17AVVoiceControllerP25AVVCPrepareRecordSettingsU13block_pointerFvmbP7NSErrorE_block_invoke.375
+ ____ZN14ControllerImpl22setDuckOthersForStreamEmP16AVVCDuckSettingsU13block_pointerFvmbP7NSErrorE_block_invoke.557
+ ____ZN14ControllerImpl22setRecordModeForStreamEm27AVVoiceControllerRecordModeU13block_pointerFvmbP7NSErrorE_block_invoke.538
+ ____ZN14ControllerImpl22setRecordModeForStreamEm27AVVoiceControllerRecordModeU13block_pointerFvmbP7NSErrorE_block_invoke.539
+ ____ZN14ControllerImpl23VibeAlertCompletionProcEjP17AVVoiceControllerm_block_invoke.252
+ ____ZN14ControllerImpl23playAlertWithCompletionEP17AVVoiceController16AVVoiceAlertType20AVVoiceAlertOverrideU13block_pointerFvS2_14AVVCAlertStateP7NSErrorE_block_invoke.492
+ ____ZN14ControllerImpl23playAlertWithCompletionEP17AVVoiceController16AVVoiceAlertType20AVVoiceAlertOverrideU13block_pointerFvS2_14AVVCAlertStateP7NSErrorE_block_invoke.493
+ ____ZN14ControllerImpl23playAlertWithCompletionEP17AVVoiceController16AVVoiceAlertType20AVVoiceAlertOverrideU13block_pointerFvS2_14AVVCAlertStateP7NSErrorE_block_invoke.494
+ ____ZN14ControllerImpl23playAlertWithCompletionEP17AVVoiceController16AVVoiceAlertType20AVVoiceAlertOverrideU13block_pointerFvS2_14AVVCAlertStateP7NSErrorE_block_invoke.495
+ ____ZN14ControllerImpl25updateMeterLevelForStreamEmU13block_pointerFvmbP7NSErrorE_block_invoke.516
+ ____ZN14ControllerImpl25updateMeterLevelForStreamEmU13block_pointerFvmbP7NSErrorE_block_invoke.517
+ ____ZN14ControllerImpl26getRecordSettingsForStreamEP17AVVoiceControllermU13block_pointerFvmP12NSDictionaryP7NSErrorE_block_invoke.509
+ ____ZN14ControllerImpl26isMeteringEnabledForStreamEmU13block_pointerFvmbP7NSErrorE_block_invoke.513
+ ____ZN14ControllerImpl27enableTriangleModeForStreamEmbU13block_pointerFvmbP7NSErrorE_block_invoke.569
+ ____ZN14ControllerImpl27stopKeepAliveQueueForStreamEmU13block_pointerFvmbP7NSErrorE_block_invoke.579
+ ____ZN14ControllerImpl28getRecordDeviceInfoForStreamEP17AVVoiceControllermU13block_pointerFvmP20AVVCRecordDeviceInfoP7NSErrorE_block_invoke.503
+ ____ZN14ControllerImpl28getRecordDeviceInfoForStreamEP17AVVoiceControllermU13block_pointerFvmP20AVVCRecordDeviceInfoP7NSErrorE_block_invoke.505
+ ____ZN14ControllerImpl28startKeepAliveQueueForStreamEmU13block_pointerFvmbP7NSErrorE_block_invoke.572
+ ____ZN14ControllerImpl28startKeepAliveQueueForStreamEmU13block_pointerFvmbP7NSErrorE_block_invoke.575
+ ____ZN14ControllerImpl28startKeepAliveQueueForStreamEmU13block_pointerFvmbP7NSErrorE_block_invoke_2.576
+ ____ZN14ControllerImpl29activateAudioSessionForStreamEP17AVVoiceControllermbbU13block_pointerFvmbP7NSErrorE_block_invoke.455
+ ____ZN14ControllerImpl29activateAudioSessionForStreamEP17AVVoiceControllermbbU13block_pointerFvmbP7NSErrorE_block_invoke.456
+ ____ZN14ControllerImpl29activateAudioSessionForStreamEP17AVVoiceControllermbbU13block_pointerFvmbP7NSErrorE_block_invoke.457
+ ____ZN14ControllerImpl29activateAudioSessionForStreamEP17AVVoiceControllermbbU13block_pointerFvmbP7NSErrorE_block_invoke.458
+ ____ZN14ControllerImpl29activateAudioSessionForStreamEP17AVVoiceControllermbbU13block_pointerFvmbP7NSErrorE_block_invoke_2.459
+ ____ZN14ControllerImpl30getCurrentStreamStateForStreamEP17AVVoiceControllermU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke.426
+ ____ZN14ControllerImpl31configureAlertBehaviorForStreamEP17AVVoiceControllerP34AVVCConfigureAlertBehaviorSettingsU13block_pointerFvP7NSErrorE_block_invoke.433
+ ____ZN14ControllerImpl31configureAlertBehaviorForStreamEP17AVVoiceControllerP34AVVCConfigureAlertBehaviorSettingsU13block_pointerFvP7NSErrorE_block_invoke.436
+ ____ZN14ControllerImpl31enableSmartRoutingConsiderationEmbU13block_pointerFvmbP7NSErrorE_block_invoke.532
+ ____ZN14ControllerImpl31getPeakPowerForStreamAndChannelEmiU13block_pointerFvmfP7NSErrorE_block_invoke.520
+ ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.305
+ ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.307
+ ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.312
+ ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.317
+ ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.322
+ ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.323
+ ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.327
+ ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.331
+ ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.333
+ ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.335
+ ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.341
+ ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.342
+ ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.343
+ ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.347
+ ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.348
+ ____ZN14ControllerImpl32getRecordBufferDurationForStreamEmU13block_pointerFvmdP7NSErrorE_block_invoke.429
+ ____ZN14ControllerImpl32setAnnounceCallsEnabledForStreamEmbU13block_pointerFvmbP7NSErrorE_block_invoke.554
+ ____ZN14ControllerImpl34getAveragePowerForStreamAndChannelEmiU13block_pointerFvmfP7NSErrorE_block_invoke.528
+ ____ZN14ControllerImpl36_createRecordingEngineWithParametersENSt3__110shared_ptrIS_EEP17AVVoiceControllerN19AVVCRecordingEngine10EngineTypeEP8NSStringlU13block_pointerFvNS1_IS5_EEE_block_invoke.293
+ ____ZN14ControllerImpl40isDuckingSupportedOnPickedRouteForStreamEmU13block_pointerFvmbP7NSErrorE_block_invoke.566
+ ____ZN25AVVCPluginRecordingEngine13stopRecordingEv_block_invoke.123
+ ____ZN25AVVCPluginRecordingEngine14startRecordingEv_block_invoke.114
+ ____ZN25AVVCPluginRecordingEngine17createRecordQueueEP12NSDictionary_block_invoke.135
+ ____ZN25AVVCPluginRecordingEngine17createRecordQueueEP12NSDictionary_block_invoke.136
+ ____ZN29AVVCAudioQueueRecordingEngine16handleAudioInputEP16OpaqueAudioQueueP16AudioQueueBufferPK14AudioTimeStampjPK28AudioStreamPacketDescription_block_invoke.158
+ ___block_descriptor_tmp.1225
+ ___block_descriptor_tmp.1502
+ ___block_descriptor_tmp.1510
+ ___block_descriptor_tmp.6079
+ ___block_literal_global.1093
+ ___block_literal_global.1422
+ ___block_literal_global.161
+ ___block_literal_global.1643
+ ___block_literal_global.169
+ ___block_literal_global.1775
+ ___block_literal_global.189
+ ___block_literal_global.194
+ ___block_literal_global.206
+ ___block_literal_global.2161
+ ___block_literal_global.222
+ ___block_literal_global.2538
+ ___block_literal_global.2852
+ ___block_literal_global.3151
+ ___block_literal_global.3389
+ ___block_literal_global.355
+ ___block_literal_global.43
+ ___block_literal_global.5022
+ ___block_literal_global.5210
+ ___block_literal_global.5623
+ ___block_literal_global.5988
+ ___block_literal_global.6059
+ ___block_literal_global.6077
+ ___block_literal_global.6515
+ ___block_literal_global.7268
+ ___block_literal_global.7994
+ ___block_literal_global.8410
+ ___block_literal_global.8632
+ ___block_literal_global.954
+ ___kCFBooleanTrue
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_AVFAudio
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_AVFAudio
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_AVFAudio
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftCoreMedia_$_AVFAudio
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_AVFAudio
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_AVFAudio
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_AVFAudio
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_AVFAudio
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_AVFAudio
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_AVFAudio
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_AVFAudio
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AVFAudio
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AVFAudio
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AVFAudio
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_AVFAudio
+ __xpc_type_null
+ _close
+ _dispatch_barrier_sync
+ _kIOSurfaceAllocSize
+ _kIOSurfaceName
+ _kIOSurfacePreallocPages
+ _mach_error_string
+ _objc_msgSend$attributesOfItemAtPath:error:
+ _objc_msgSend$componentsWithURL:resolvingAgainstBaseURL:
+ _objc_msgSend$decodeXPCObjectOfType:forKey:
+ _objc_msgSend$encodeXPCObject:forKey:
+ _objc_msgSend$initWithPCMFormat:bufferListNoCopy:deallocator:
+ _objc_msgSend$initWithSurface:taskToken:
+ _objc_msgSend$queryItems
+ _objc_msgSend$string
+ _objc_msgSend$surface
+ _objc_msgSend$surfaceXPCType
+ _objc_msgSend$taskToken
+ _objc_msgSend$taskTokenXPCType
+ _open
+ _pread
+ _task_create_identity_token
+ _xpc_mach_send_copy_right
+ _xpc_mach_send_create
- GCC_except_table100
- GCC_except_table101
- GCC_except_table1012
- GCC_except_table102
- GCC_except_table1020
- GCC_except_table1028
- GCC_except_table1030
- GCC_except_table1031
- GCC_except_table1033
- GCC_except_table1051
- GCC_except_table1078
- GCC_except_table1096
- GCC_except_table110
- GCC_except_table1119
- GCC_except_table1120
- GCC_except_table1121
- GCC_except_table1124
- GCC_except_table1125
- GCC_except_table1126
- GCC_except_table113
- GCC_except_table1140
- GCC_except_table1148
- GCC_except_table115
- GCC_except_table1169
- GCC_except_table1170
- GCC_except_table1178
- GCC_except_table1186
- GCC_except_table1187
- GCC_except_table1189
- GCC_except_table1190
- GCC_except_table1191
- GCC_except_table1207
- GCC_except_table1208
- GCC_except_table1210
- GCC_except_table1211
- GCC_except_table1215
- GCC_except_table123
- GCC_except_table1244
- GCC_except_table1245
- GCC_except_table1246
- GCC_except_table1247
- GCC_except_table1248
- GCC_except_table125
- GCC_except_table1251
- GCC_except_table1258
- GCC_except_table1259
- GCC_except_table1261
- GCC_except_table1291
- GCC_except_table1305
- GCC_except_table1307
- GCC_except_table1309
- GCC_except_table1327
- GCC_except_table133
- GCC_except_table1348
- GCC_except_table1349
- GCC_except_table1350
- GCC_except_table1361
- GCC_except_table1362
- GCC_except_table138
- GCC_except_table1385
- GCC_except_table1386
- GCC_except_table1387
- GCC_except_table1389
- GCC_except_table1390
- GCC_except_table1391
- GCC_except_table1392
- GCC_except_table1393
- GCC_except_table1394
- GCC_except_table1398
- GCC_except_table144
- GCC_except_table1460
- GCC_except_table1461
- GCC_except_table1462
- GCC_except_table1463
- GCC_except_table1468
- GCC_except_table147
- GCC_except_table1480
- GCC_except_table1482
- GCC_except_table1485
- GCC_except_table1487
- GCC_except_table1488
- GCC_except_table1489
- GCC_except_table1490
- GCC_except_table1492
- GCC_except_table1510
- GCC_except_table1515
- GCC_except_table1517
- GCC_except_table1518
- GCC_except_table1526
- GCC_except_table1527
- GCC_except_table1528
- GCC_except_table1530
- GCC_except_table1532
- GCC_except_table1534
- GCC_except_table1536
- GCC_except_table1537
- GCC_except_table1538
- GCC_except_table1540
- GCC_except_table1542
- GCC_except_table1550
- GCC_except_table1561
- GCC_except_table1562
- GCC_except_table1563
- GCC_except_table1566
- GCC_except_table1567
- GCC_except_table1584
- GCC_except_table1585
- GCC_except_table1587
- GCC_except_table1589
- GCC_except_table1591
- GCC_except_table1592
- GCC_except_table1593
- GCC_except_table1595
- GCC_except_table1597
- GCC_except_table1609
- GCC_except_table1613
- GCC_except_table1614
- GCC_except_table1617
- GCC_except_table1618
- GCC_except_table1626
- GCC_except_table1636
- GCC_except_table1649
- GCC_except_table1650
- GCC_except_table1652
- GCC_except_table1653
- GCC_except_table1660
- GCC_except_table1661
- GCC_except_table1662
- GCC_except_table1663
- GCC_except_table1669
- GCC_except_table167
- GCC_except_table1670
- GCC_except_table168
- GCC_except_table1699
- GCC_except_table170
- GCC_except_table1700
- GCC_except_table1704
- GCC_except_table1706
- GCC_except_table1707
- GCC_except_table1708
- GCC_except_table1709
- GCC_except_table1710
- GCC_except_table1713
- GCC_except_table1717
- GCC_except_table1718
- GCC_except_table176
- GCC_except_table1764
- GCC_except_table1765
- GCC_except_table1766
- GCC_except_table1768
- GCC_except_table177
- GCC_except_table1771
- GCC_except_table1772
- GCC_except_table1773
- GCC_except_table1774
- GCC_except_table1775
- GCC_except_table1777
- GCC_except_table178
- GCC_except_table1781
- GCC_except_table1783
- GCC_except_table1784
- GCC_except_table1796
- GCC_except_table1813
- GCC_except_table1819
- GCC_except_table1820
- GCC_except_table1822
- GCC_except_table183
- GCC_except_table1830
- GCC_except_table1831
- GCC_except_table1838
- GCC_except_table184
- GCC_except_table1843
- GCC_except_table186
- GCC_except_table1873
- GCC_except_table1874
- GCC_except_table1876
- GCC_except_table1877
- GCC_except_table189
- GCC_except_table1908
- GCC_except_table1910
- GCC_except_table1911
- GCC_except_table1912
- GCC_except_table1913
- GCC_except_table1914
- GCC_except_table1915
- GCC_except_table1916
- GCC_except_table1917
- GCC_except_table1918
- GCC_except_table1919
- GCC_except_table194
- GCC_except_table1959
- GCC_except_table196
- GCC_except_table2061
- GCC_except_table2063
- GCC_except_table2064
- GCC_except_table2065
- GCC_except_table2068
- GCC_except_table2073
- GCC_except_table2076
- GCC_except_table2077
- GCC_except_table2078
- GCC_except_table208
- GCC_except_table2080
- GCC_except_table2083
- GCC_except_table2084
- GCC_except_table2096
- GCC_except_table2097
- GCC_except_table2101
- GCC_except_table2104
- GCC_except_table2107
- GCC_except_table2111
- GCC_except_table2113
- GCC_except_table2114
- GCC_except_table2117
- GCC_except_table2120
- GCC_except_table2138
- GCC_except_table2146
- GCC_except_table2147
- GCC_except_table2148
- GCC_except_table2149
- GCC_except_table215
- GCC_except_table2150
- GCC_except_table2153
- GCC_except_table2154
- GCC_except_table2181
- GCC_except_table2182
- GCC_except_table2223
- GCC_except_table2224
- GCC_except_table2225
- GCC_except_table2237
- GCC_except_table2238
- GCC_except_table2240
- GCC_except_table2241
- GCC_except_table2243
- GCC_except_table2244
- GCC_except_table2248
- GCC_except_table2253
- GCC_except_table2254
- GCC_except_table2255
- GCC_except_table2275
- GCC_except_table2292
- GCC_except_table2295
- GCC_except_table2297
- GCC_except_table2303
- GCC_except_table2305
- GCC_except_table2307
- GCC_except_table2308
- GCC_except_table2311
- GCC_except_table2312
- GCC_except_table2313
- GCC_except_table2316
- GCC_except_table2324
- GCC_except_table2337
- GCC_except_table2343
- GCC_except_table2344
- GCC_except_table2345
- GCC_except_table2346
- GCC_except_table2353
- GCC_except_table2354
- GCC_except_table2355
- GCC_except_table2363
- GCC_except_table2364
- GCC_except_table2365
- GCC_except_table2366
- GCC_except_table2371
- GCC_except_table2372
- GCC_except_table2373
- GCC_except_table2389
- GCC_except_table2407
- GCC_except_table2409
- GCC_except_table2410
- GCC_except_table2416
- GCC_except_table2420
- GCC_except_table2421
- GCC_except_table2426
- GCC_except_table2437
- GCC_except_table2438
- GCC_except_table244
- GCC_except_table2440
- GCC_except_table2443
- GCC_except_table2445
- GCC_except_table2446
- GCC_except_table2447
- GCC_except_table2448
- GCC_except_table2456
- GCC_except_table2472
- GCC_except_table2473
- GCC_except_table2480
- GCC_except_table2487
- GCC_except_table2490
- GCC_except_table2494
- GCC_except_table2497
- GCC_except_table2498
- GCC_except_table2500
- GCC_except_table2502
- GCC_except_table2504
- GCC_except_table2509
- GCC_except_table2514
- GCC_except_table2528
- GCC_except_table2529
- GCC_except_table2542
- GCC_except_table2554
- GCC_except_table2557
- GCC_except_table2558
- GCC_except_table2559
- GCC_except_table2560
- GCC_except_table2564
- GCC_except_table2567
- GCC_except_table257
- GCC_except_table2570
- GCC_except_table2576
- GCC_except_table258
- GCC_except_table2584
- GCC_except_table2585
- GCC_except_table2588
- GCC_except_table2589
- GCC_except_table259
- GCC_except_table2591
- GCC_except_table2592
- GCC_except_table260
- GCC_except_table2616
- GCC_except_table2617
- GCC_except_table2618
- GCC_except_table2621
- GCC_except_table2622
- GCC_except_table2626
- GCC_except_table2627
- GCC_except_table2628
- GCC_except_table2629
- GCC_except_table2632
- GCC_except_table2633
- GCC_except_table2634
- GCC_except_table2635
- GCC_except_table2636
- GCC_except_table2646
- GCC_except_table2647
- GCC_except_table2648
- GCC_except_table2653
- GCC_except_table2654
- GCC_except_table2665
- GCC_except_table2673
- GCC_except_table2678
- GCC_except_table2679
- GCC_except_table2686
- GCC_except_table2695
- GCC_except_table2697
- GCC_except_table270
- GCC_except_table2705
- GCC_except_table2706
- GCC_except_table2730
- GCC_except_table2733
- GCC_except_table2739
- GCC_except_table2740
- GCC_except_table2746
- GCC_except_table2755
- GCC_except_table276
- GCC_except_table277
- GCC_except_table2780
- GCC_except_table2781
- GCC_except_table279
- GCC_except_table2790
- GCC_except_table2791
- GCC_except_table2792
- GCC_except_table2795
- GCC_except_table2799
- GCC_except_table2802
- GCC_except_table2806
- GCC_except_table2809
- GCC_except_table2816
- GCC_except_table2820
- GCC_except_table2823
- GCC_except_table2827
- GCC_except_table2830
- GCC_except_table2859
- GCC_except_table2868
- GCC_except_table287
- GCC_except_table2898
- GCC_except_table2901
- GCC_except_table2905
- GCC_except_table2908
- GCC_except_table2911
- GCC_except_table2912
- GCC_except_table2913
- GCC_except_table2914
- GCC_except_table2915
- GCC_except_table2916
- GCC_except_table2917
- GCC_except_table2918
- GCC_except_table2919
- GCC_except_table292
- GCC_except_table2920
- GCC_except_table2921
- GCC_except_table2922
- GCC_except_table2965
- GCC_except_table2966
- GCC_except_table2967
- GCC_except_table2969
- GCC_except_table297
- GCC_except_table2971
- GCC_except_table2972
- GCC_except_table2973
- GCC_except_table2979
- GCC_except_table2980
- GCC_except_table2985
- GCC_except_table302
- GCC_except_table3032
- GCC_except_table3034
- GCC_except_table3037
- GCC_except_table3039
- GCC_except_table304
- GCC_except_table3042
- GCC_except_table3044
- GCC_except_table3047
- GCC_except_table3058
- GCC_except_table3073
- GCC_except_table3079
- GCC_except_table3085
- GCC_except_table309
- GCC_except_table3093
- GCC_except_table3094
- GCC_except_table3095
- GCC_except_table3096
- GCC_except_table3099
- GCC_except_table3100
- GCC_except_table3101
- GCC_except_table3102
- GCC_except_table3103
- GCC_except_table3105
- GCC_except_table3107
- GCC_except_table3109
- GCC_except_table311
- GCC_except_table3117
- GCC_except_table3122
- GCC_except_table3131
- GCC_except_table3133
- GCC_except_table3136
- GCC_except_table3139
- GCC_except_table3140
- GCC_except_table3143
- GCC_except_table3144
- GCC_except_table3169
- GCC_except_table3183
- GCC_except_table3193
- GCC_except_table3194
- GCC_except_table3196
- GCC_except_table3229
- GCC_except_table323
- GCC_except_table3230
- GCC_except_table3232
- GCC_except_table3233
- GCC_except_table324
- GCC_except_table3259
- GCC_except_table326
- GCC_except_table3262
- GCC_except_table3264
- GCC_except_table3281
- GCC_except_table3282
- GCC_except_table329
- GCC_except_table331
- GCC_except_table3311
- GCC_except_table3313
- GCC_except_table332
- GCC_except_table3323
- GCC_except_table3324
- GCC_except_table3325
- GCC_except_table3326
- GCC_except_table3327
- GCC_except_table3328
- GCC_except_table3329
- GCC_except_table3330
- GCC_except_table3331
- GCC_except_table3332
- GCC_except_table3333
- GCC_except_table3338
- GCC_except_table3342
- GCC_except_table3345
- GCC_except_table3368
- GCC_except_table3374
- GCC_except_table3375
- GCC_except_table3376
- GCC_except_table3378
- GCC_except_table3379
- GCC_except_table3382
- GCC_except_table3383
- GCC_except_table3384
- GCC_except_table3385
- GCC_except_table3397
- GCC_except_table3398
- GCC_except_table3399
- GCC_except_table340
- GCC_except_table3400
- GCC_except_table3405
- GCC_except_table3408
- GCC_except_table3409
- GCC_except_table341
- GCC_except_table3416
- GCC_except_table3447
- GCC_except_table3448
- GCC_except_table3449
- GCC_except_table3450
- GCC_except_table3452
- GCC_except_table3454
- GCC_except_table3455
- GCC_except_table3457
- GCC_except_table3458
- GCC_except_table3459
- GCC_except_table3461
- GCC_except_table3462
- GCC_except_table3463
- GCC_except_table3464
- GCC_except_table3465
- GCC_except_table3467
- GCC_except_table3468
- GCC_except_table3469
- GCC_except_table3473
- GCC_except_table3474
- GCC_except_table3488
- GCC_except_table3506
- GCC_except_table3514
- GCC_except_table3517
- GCC_except_table3523
- GCC_except_table3524
- GCC_except_table3528
- GCC_except_table353
- GCC_except_table3531
- GCC_except_table3539
- GCC_except_table3545
- GCC_except_table3546
- GCC_except_table3548
- GCC_except_table3549
- GCC_except_table3580
- GCC_except_table3581
- GCC_except_table3584
- GCC_except_table3585
- GCC_except_table3586
- GCC_except_table3587
- GCC_except_table3588
- GCC_except_table3589
- GCC_except_table3590
- GCC_except_table3591
- GCC_except_table3592
- GCC_except_table3593
- GCC_except_table3594
- GCC_except_table3595
- GCC_except_table3596
- GCC_except_table3597
- GCC_except_table3598
- GCC_except_table3599
- GCC_except_table3600
- GCC_except_table3601
- GCC_except_table3602
- GCC_except_table3603
- GCC_except_table3605
- GCC_except_table3606
- GCC_except_table3608
- GCC_except_table3612
- GCC_except_table3613
- GCC_except_table3634
- GCC_except_table3648
- GCC_except_table3654
- GCC_except_table3690
- GCC_except_table3692
- GCC_except_table3694
- GCC_except_table3697
- GCC_except_table3700
- GCC_except_table3701
- GCC_except_table3703
- GCC_except_table3704
- GCC_except_table3705
- GCC_except_table3706
- GCC_except_table3708
- GCC_except_table3711
- GCC_except_table3712
- GCC_except_table3716
- GCC_except_table3718
- GCC_except_table3726
- GCC_except_table3737
- GCC_except_table3750
- GCC_except_table3754
- GCC_except_table3757
- GCC_except_table3758
- GCC_except_table3759
- GCC_except_table3761
- GCC_except_table3762
- GCC_except_table3765
- GCC_except_table3766
- GCC_except_table3769
- GCC_except_table3770
- GCC_except_table3773
- GCC_except_table3774
- GCC_except_table3785
- GCC_except_table3811
- GCC_except_table3845
- GCC_except_table3846
- GCC_except_table3849
- GCC_except_table391
- GCC_except_table410
- GCC_except_table424
- GCC_except_table442
- GCC_except_table443
- GCC_except_table455
- GCC_except_table461
- GCC_except_table462
- GCC_except_table464
- GCC_except_table483
- GCC_except_table496
- GCC_except_table498
- GCC_except_table499
- GCC_except_table516
- GCC_except_table519
- GCC_except_table522
- GCC_except_table525
- GCC_except_table53
- GCC_except_table534
- GCC_except_table54
- GCC_except_table547
- GCC_except_table548
- GCC_except_table549
- GCC_except_table550
- GCC_except_table568
- GCC_except_table570
- GCC_except_table571
- GCC_except_table588
- GCC_except_table589
- GCC_except_table590
- GCC_except_table591
- GCC_except_table596
- GCC_except_table601
- GCC_except_table607
- GCC_except_table61
- GCC_except_table610
- GCC_except_table612
- GCC_except_table641
- GCC_except_table647
- GCC_except_table648
- GCC_except_table649
- GCC_except_table659
- GCC_except_table666
- GCC_except_table668
- GCC_except_table670
- GCC_except_table676
- GCC_except_table69
- GCC_except_table691
- GCC_except_table697
- GCC_except_table700
- GCC_except_table72
- GCC_except_table734
- GCC_except_table742
- GCC_except_table745
- GCC_except_table754
- GCC_except_table760
- GCC_except_table776
- GCC_except_table780
- GCC_except_table782
- GCC_except_table791
- GCC_except_table795
- GCC_except_table796
- GCC_except_table797
- GCC_except_table806
- GCC_except_table819
- GCC_except_table820
- GCC_except_table822
- GCC_except_table823
- GCC_except_table825
- GCC_except_table828
- GCC_except_table837
- GCC_except_table838
- GCC_except_table846
- GCC_except_table847
- GCC_except_table85
- GCC_except_table856
- GCC_except_table869
- GCC_except_table870
- GCC_except_table873
- GCC_except_table878
- GCC_except_table879
- GCC_except_table88
- GCC_except_table886
- GCC_except_table89
- GCC_except_table892
- GCC_except_table894
- GCC_except_table900
- GCC_except_table902
- GCC_except_table910
- GCC_except_table912
- GCC_except_table913
- GCC_except_table915
- GCC_except_table922
- GCC_except_table924
- GCC_except_table925
- GCC_except_table926
- GCC_except_table928
- GCC_except_table930
- GCC_except_table95
- GCC_except_table950
- GCC_except_table973
- GCC_except_table974
- GCC_except_table975
- GCC_except_table976
- GCC_except_table977
- GCC_except_table979
- GCC_except_table980
- GCC_except_table981
- GCC_except_table987
- GCC_except_table993
- _AVAudioSessionModeEnrollment
- _CFMakeCollectable
- __ZN10applesauce2CF9StringRefD1Ev
- __ZN11ElapsedTimeC2EPKcS1_b
- __ZN11ElapsedTimeD2Ev
- __ZN12CADeprecated9CAPThread5EntryEPS0_
- __ZN16AVAudioClockImpl11CurrentTimeEv
- __ZN19AVVCRecordingEngine25UpdateRecordDeviceOnQueueEP8NSString
- __ZN19AVVCRecordingEngine28removeAudioHALDeviceListenerEv
- __ZN19AVVCRecordingEngine36setupAudioQueueRecordDeviceAndUpdateEP8NSString
- __ZN24CAStreamBasicDescriptionC2EdjNS_15CommonPCMFormatEb
- __ZN29AVVCAudioQueueRecordingEngine25UpdateRecordDeviceOnQueueEP8NSString
- __ZN29AVVCAudioQueueRecordingEngine28removeAudioHALDeviceListenerEv
- __ZN29AVVCAudioQueueRecordingEngine36setupAudioQueueRecordDeviceAndUpdateEP8NSString
- __ZN2CA12AudioBuffers7PrepareEjj
- __ZN5caulk10concurrent7details12message_callIRZN20AVAudioSequencerImpl12UserCallbackEPvP19OpaqueMusicSequenceP16OpaqueMusicTrackdPK18MusicEventUserDataddE3$_0JEE7performEv
- __ZN5caulk10concurrent7details12message_callIRZN20AVAudioSequencerImpl12UserCallbackEPvP19OpaqueMusicSequenceP16OpaqueMusicTrackdPK18MusicEventUserDataddE3$_0JEED0Ev
- __ZN5caulk10concurrent7details12message_callIRZN20AVAudioSequencerImpl12UserCallbackEPvP19OpaqueMusicSequenceP16OpaqueMusicTrackdPK18MusicEventUserDataddE3$_0JEED1Ev
- __ZN5caulk16inplace_functionIFvPKN4MIDI16LegacyPacketListEELm48ELm8ENS_23inplace_function_detail6vtableEE16k_wrapper_vtableIZZN17AUGraphMIDINodeV332AllocateMIDIOutputEventListBlockEvEUb_E3$_3EE
- __ZN5caulk23inplace_function_detail6vtableIvJPKN4MIDI16LegacyPacketListEEE5emptyE
- __ZN5caulk5alloc22realtime_safe_resourceE
- __ZNK24CAStreamBasicDescription8AsStringEPcmb
- __ZNKSt3__110__function6__funcIZN13AUGraphParser14InitializeNodeERK18AVAudioEngineGraphR17AUGraphNodeBaseV3jbE3$_1NS_9allocatorIS8_EEF16ETraversalStatusS7_P17AUGraphConnectionEE7__cloneEPNS0_6__baseISE_EE
- __ZNKSt3__110__function6__funcIZN13AUGraphParser14InitializeNodeERK18AVAudioEngineGraphR17AUGraphNodeBaseV3jbE3$_1NS_9allocatorIS8_EEF16ETraversalStatusS7_P17AUGraphConnectionEE7__cloneEv
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB8ne190102IS4_EENS_12basic_stringIcS2_T_EERKS8_
- __ZNKSt3__16vectorI12WorkloopInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI23EExtAudioGraphNodeStateNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI30AVAEStreamFormatObserverStructNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN17AUInterfaceBaseV314RenderObserverENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP11AVAudioNodeNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP17AUGraphNodeBaseV3NS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP17AUGraphNodeBaseV3NS_9allocatorIS2_EEE20__throw_out_of_rangeB8ne190102Ev
- __ZNKSt3__16vectorIP19AVAudioNodeImplBaseNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP22CompletionHandlerTimerNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP8NSNumberNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPN5caulk22pooled_semaphore_mutexENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPN5caulk22pooled_semaphore_mutexENS_9allocatorIS3_EEE20__throw_out_of_rangeB8ne190102Ev
- __ZNKSt3__16vectorIbNS_9allocatorIbEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_out_of_rangeB8ne190102Ev
- __ZNKSt3__16vectorIxNS_9allocatorIxEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt12out_of_rangeC1B8ne190102EPKc
- __ZNSt3__110__function12__value_funcIF16ETraversalStatusR17AUGraphNodeBaseV3P17AUGraphConnectionEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrI19AVVCRecordingEngineEEEEC2B8ne190102ERKS6_
- __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrI19AVVCRecordingEngineEEEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFvbEED2B8ne190102Ev
- __ZNSt3__110__function6__funcIZN13AUGraphParser14InitializeNodeERK18AVAudioEngineGraphR17AUGraphNodeBaseV3jbE3$_1NS_9allocatorIS8_EEF16ETraversalStatusS7_P17AUGraphConnectionEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN13AUGraphParser14InitializeNodeERK18AVAudioEngineGraphR17AUGraphNodeBaseV3jbE3$_1NS_9allocatorIS8_EEF16ETraversalStatusS7_P17AUGraphConnectionEE7destroyEv
- __ZNSt3__110__function6__funcIZN13AUGraphParser14InitializeNodeERK18AVAudioEngineGraphR17AUGraphNodeBaseV3jbE3$_1NS_9allocatorIS8_EEF16ETraversalStatusS7_P17AUGraphConnectionEED0Ev
- __ZNSt3__110__function6__funcIZN13AUGraphParser14InitializeNodeERK18AVAudioEngineGraphR17AUGraphNodeBaseV3jbE3$_1NS_9allocatorIS8_EEF16ETraversalStatusS7_P17AUGraphConnectionEED1Ev
- __ZNSt3__110__function6__funcIZN13AUGraphParser14InitializeNodeERK18AVAudioEngineGraphR17AUGraphNodeBaseV3jbE3$_1NS_9allocatorIS8_EEF16ETraversalStatusS7_P17AUGraphConnectionEEclES7_OSD_
- __ZNSt3__110shared_ptrI14ControllerImplEC2B8ne190102IS1_Li0EEERKNS_8weak_ptrIT_EE
- __ZNSt3__110shared_ptrI19AVVCRecordingEngineEC2B8ne190102IS1_Li0EEERKNS_8weak_ptrIT_EE
- __ZNSt3__110unique_ptrI15AVAudioFileImplNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI17CallbackMessengerNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI18AVAudioEngineGraphNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI21AVAEGraphStateTrackerNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI22AVAEDispatchQueueTimerNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerF34AVAudioEngineManualRenderingStatusjP15AudioBufferListPiEENS_14default_deleteIS8_EEE5resetB8ne190102EPS8_
- __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFPK15AudioBufferListjEENS_14default_deleteIS7_EEE5resetB8ne190102EPS7_
- __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFiPjPK14AudioTimeStampjlP15AudioBufferListEENS_14default_deleteISA_EEE5resetB8ne190102EPSA_
- __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFiPjPK14AudioTimeStampjlP15AudioBufferListU13block_pointerFiS2_S5_jlS7_EEENS_14default_deleteISC_EEE5resetB8ne190102EPSC_
- __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFixhPK13MIDIEventListEENS_14default_deleteIS7_EEE5resetB8ne190102EPS7_
- __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFixhlPKhEENS_14default_deleteIS6_EEE5resetB8ne190102EPS6_
- __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFv39AVAudioPlayerNodeCompletionCallbackTypeEENS_14default_deleteIS5_EEE5resetB8ne190102EPS5_
- __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFvPjPK14AudioTimeStampjlEENS_14default_deleteIS8_EEE5resetB8ne190102EPS8_
- __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFvjPK14AudioTimeStampjlEENS_14default_deleteIS7_EEE5resetB8ne190102EPS7_
- __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFvxhlPKhEENS_14default_deleteIS6_EEE5resetB8ne190102EPS6_
- __ZNSt3__110unique_ptrI9PulseToneNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrIN4MIDI16LegacyPacketListENS1_23LegacyPacketListDeleterEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeI16AVVoiceAlertTypeU8__strongP5NSURLEEPvEENS_22__tree_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne190102EPS9_
- __ZNSt3__110unique_ptrINS_3mapINS_4pairIP11AVAudioNodejEEP24AVAudioMixingDestinationNS_4lessIS5_EENS_9allocatorINS2_IKS5_S7_EEEEEENS_14default_deleteISE_EEE5resetB8ne190102EPSE_
- __ZNSt3__110unique_ptrIZN20AVAudioSequencerImpl4StopEvE3$_0NS_14default_deleteIS2_EEED1B8ne190102Ev
- __ZNSt3__110unique_ptrIZN20AVAudioSequencerImplD1EvE3$_0NS_14default_deleteIS2_EEED1B8ne190102Ev
- __ZNSt3__111unique_lockIN5caulk22pooled_semaphore_mutexEED2B8ne190102Ev
- __ZNSt3__111unique_lockIN5caulk23recursive_mutex_adapterINS1_22pooled_semaphore_mutexEEEED2B8ne190102Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIZN17AUGraphNodeBaseV320CreateMIDIConnectionERK21AUGraphMIDIConnectionE3$_0EEJRKNS0_6__baseILNS0_6_TraitE0EJU13block_pointerFixhlPKhEU13block_pointerFixhPK13MIDIEventListEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIZN17AUGraphNodeBaseV320CreateMIDIConnectionERK21AUGraphMIDIConnectionE3$_0EEJRKNS0_6__baseILNS0_6_TraitE0EJU13block_pointerFixhlPKhEU13block_pointerFixhPK13MIDIEventListEEEEEEEDcT_DpT0_
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN12CADeprecated10TSingletonINS2_19RealtimeDeallocatorEE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne190102Ev
- __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI23EExtAudioGraphNodeStateEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP17AUGraphNodeBaseV3EEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP8NSNumberEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPN5caulk22pooled_semaphore_mutexEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
- __ZNSt3__120__throw_bad_weak_ptrB8ne190102Ev
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
- __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__125__throw_bad_function_callB8ne190102Ev
- __ZNSt3__126__throw_bad_variant_accessB8ne190102Ev
- __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__14lockB8ne190102IN5caulk22pooled_semaphore_mutexES2_EEvRT_RT0_
- __ZNSt3__14lockB8ne190102INS_15recursive_mutexEN5caulk23recursive_mutex_adapterINS2_22pooled_semaphore_mutexEEEEEvRT_RT0_
- __ZNSt3__14lockB8ne190102INS_15recursive_mutexES1_EEvRT_RT0_
- __ZNSt3__16vectorIN17AUInterfaceBaseV314RenderObserverENS_9allocatorIS2_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorIP17AUGraphNodeBaseV3NS_9allocatorIS2_EEE18__assign_with_sizeB8ne190102IPS2_S7_EEvT_T0_l
- __ZNSt3__16vectorIP17AUGraphNodeBaseV3NS_9allocatorIS2_EEE9push_backB8ne190102ERKS2_
- __ZNSt3__16vectorIcNS_9allocatorIcEEEC2B8ne190102Em
- __ZNSt3__16vectorIcNS_9allocatorIcEEEC2B8ne190102EmRKc
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne190102EmRKf
- __ZNSt3__16vectorIjNS_9allocatorIjEEEC1B8ne190102ESt16initializer_listIjE
- __ZNSt3__16vectorIxNS_9allocatorIxEEE16__init_with_sizeB8ne190102IPxS5_EEvT_T0_m
- __ZNSt3__18optionalIN2CA10BufferListEEaSB8ne190102IS2_vEERS3_OT_
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __ZTVN5caulk10concurrent7details12message_callIRZN20AVAudioSequencerImpl12UserCallbackEPvP19OpaqueMusicSequenceP16OpaqueMusicTrackdPK18MusicEventUserDataddE3$_0JEEE
- __ZTVNSt3__110__function6__funcIZN13AUGraphParser14InitializeNodeERK18AVAudioEngineGraphR17AUGraphNodeBaseV3jbE3$_1NS_9allocatorIS8_EEF16ETraversalStatusS7_P17AUGraphConnectionEEE
- __ZZN13AUGraphParser14InitializeNodeERK18AVAudioEngineGraphR17AUGraphNodeBaseV3jbENK3$_0clES4_
- __ZZN4MIDI19system_message_sizeEjE5sizes
- __ZZN5caulk23inplace_function_detail6vtableIvJPKN4MIDI16LegacyPacketListEEEC1EvENUlPvE_8__invokeES7_
- __ZZN5caulk23inplace_function_detail6vtableIvJPKN4MIDI16LegacyPacketListEEEC1EvENUlPvOS5_E_8__invokeES7_S8_
- __ZZN5caulk23inplace_function_detail6vtableIvJPKN4MIDI16LegacyPacketListEEEC1EvENUlPvS7_E0_8__invokeES7_S7_
- __ZZN5caulk23inplace_function_detail6vtableIvJPKN4MIDI16LegacyPacketListEEEC1EvENUlPvS7_E_8__invokeES7_S7_
- __ZZN5caulk23inplace_function_detail6vtableIvJPKN4MIDI16LegacyPacketListEEEC1IZZN17AUGraphMIDINodeV332AllocateMIDIOutputEventListBlockEvEUb_E3$_3EENS0_7wrapperIT_EEENUlPvE_8__invokeESD_
- __ZZN5caulk23inplace_function_detail6vtableIvJPKN4MIDI16LegacyPacketListEEEC1IZZN17AUGraphMIDINodeV332AllocateMIDIOutputEventListBlockEvEUb_E3$_3EENS0_7wrapperIT_EEENUlPvOS5_E_8__invokeESD_SE_
- __ZZN5caulk23inplace_function_detail6vtableIvJPKN4MIDI16LegacyPacketListEEEC1IZZN17AUGraphMIDINodeV332AllocateMIDIOutputEventListBlockEvEUb_E3$_3EENS0_7wrapperIT_EEENUlPvSD_E0_8__invokeESD_SD_
- __ZZN5caulk23inplace_function_detail6vtableIvJPKN4MIDI16LegacyPacketListEEEC1IZZN17AUGraphMIDINodeV332AllocateMIDIOutputEventListBlockEvEUb_E3$_3EENS0_7wrapperIT_EEENUlPvSD_E_8__invokeESD_SD_
- __Znwm
- ___Block_byref_object_copy_.1243
- ___Block_byref_object_copy_.145
- ___Block_byref_object_copy_.3492
- ___Block_byref_object_copy_.5596
- ___Block_byref_object_copy_.6386
- ___Block_byref_object_copy_.691
- ___Block_byref_object_copy_.7262
- ___Block_byref_object_copy_.8263
- ___Block_byref_object_copy_.8749
- ___Block_byref_object_dispose_.1244
- ___Block_byref_object_dispose_.146
- ___Block_byref_object_dispose_.3493
- ___Block_byref_object_dispose_.5597
- ___Block_byref_object_dispose_.6387
- ___Block_byref_object_dispose_.692
- ___Block_byref_object_dispose_.7263
- ___Block_byref_object_dispose_.8264
- ___Block_byref_object_dispose_.8750
- ____ZN14ControllerImpl10setContextEP17AVVoiceControllerP19AVVCContextSettingsU13block_pointerFvm14AVVCStreamTypeP7NSErrorE_block_invoke.269
- ____ZN14ControllerImpl10setContextEP17AVVoiceControllerP19AVVCContextSettingsU13block_pointerFvm14AVVCStreamTypeP7NSErrorE_block_invoke.270
- ____ZN14ControllerImpl10setContextEP17AVVoiceControllerP19AVVCContextSettingsU13block_pointerFvm14AVVCStreamTypeP7NSErrorE_block_invoke.271
- ____ZN14ControllerImpl10setContextEP17AVVoiceControllerP19AVVCContextSettingsU13block_pointerFvm14AVVCStreamTypeP7NSErrorE_block_invoke.275
- ____ZN14ControllerImpl10setContextEP17AVVoiceControllerP19AVVCContextSettingsU13block_pointerFvm14AVVCStreamTypeP7NSErrorE_block_invoke.284
- ____ZN14ControllerImpl10setContextEP17AVVoiceControllerP19AVVCContextSettingsU13block_pointerFvm14AVVCStreamTypeP7NSErrorE_block_invoke.285
- ____ZN14ControllerImpl10setContextEP17AVVoiceControllerP19AVVCContextSettingsU13block_pointerFvm14AVVCStreamTypeP7NSErrorE_block_invoke_2.276
- ____ZN14ControllerImpl15startAlertQueueEU13block_pointerFviE_block_invoke.230
- ____ZN14ControllerImpl16checkForEndpointEP17AVVoiceControllerP16AudioQueueBufferPfjd_block_invoke.252
- ____ZN14ControllerImpl16checkForEndpointEP17AVVoiceControllerP16AudioQueueBufferPfjd_block_invoke.254
- ____ZN14ControllerImpl17handleRouteChangeEP17AVVoiceControllerP14AVAudioSessionPK12NSDictionary_block_invoke.262
- ____ZN14ControllerImpl19getAVVCSessionStateEmU13block_pointerFvm16AVVCSessionStateP7NSErrorE_block_invoke.441
- ____ZN14ControllerImpl19setContextForStreamEP17AVVoiceControllerP19AVVCContextSettingsmU13block_pointerFvmbP7NSErrorE_block_invoke.465
- ____ZN14ControllerImpl19setContextForStreamEP17AVVoiceControllerP19AVVCContextSettingsmU13block_pointerFvmbP7NSErrorE_block_invoke.466
- ____ZN14ControllerImpl19setContextForStreamEP17AVVoiceControllerP19AVVCContextSettingsmU13block_pointerFvmbP7NSErrorE_block_invoke.467
- ____ZN14ControllerImpl19setContextForStreamEP17AVVoiceControllerP19AVVCContextSettingsmU13block_pointerFvmbP7NSErrorE_block_invoke.472
- ____ZN14ControllerImpl19setContextForStreamEP17AVVoiceControllerP19AVVCContextSettingsmU13block_pointerFvmbP7NSErrorE_block_invoke_2.468
- ____ZN14ControllerImpl19stopRecordForStreamEP17AVVoiceControllermU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke.414
- ____ZN14ControllerImpl19stopRecordForStreamEP17AVVoiceControllermU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke.415
- ____ZN14ControllerImpl19stopRecordForStreamEP17AVVoiceControllermU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke.416
- ____ZN14ControllerImpl20_removeEngineFromMapEP17AVVoiceControllermP8NSStringU13block_pointerFvvE_block_invoke.359
- ____ZN14ControllerImpl20handleInterruptStartEP17AVVoiceControllerP14AVAudioSessionP12NSDictionary_block_invoke.258
- ____ZN14ControllerImpl20safeAllQueuesBarrierEv_block_invoke.365
- ____ZN14ControllerImpl20safeAllQueuesBarrierEv_block_invoke.366
- ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorEU13block_pointerFv16AVVoiceAlertType14AVVCAlertStateS6_EU13block_pointerFvmP15AVVCAudioBufferE_block_invoke.377
- ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorEU13block_pointerFv16AVVoiceAlertType14AVVCAlertStateS6_EU13block_pointerFvmP15AVVCAudioBufferE_block_invoke.380
- ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke.386
- ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke.387
- ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke.388
- ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke.389
- ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke.399
- ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke_2.390
- ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke_2.393
- ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke_2.400
- ____ZN14ControllerImpl20startRecordForStreamEP17AVVoiceControllerP23AVVCStartRecordSettingsU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke_3.398
- ____ZN14ControllerImpl22getRecordModeForStreamEmU13block_pointerFvm27AVVoiceControllerRecordModeP7NSErrorE_block_invoke.542
- ____ZN14ControllerImpl22prepareRecordForStreamEP17AVVoiceControllerP25AVVCPrepareRecordSettingsU13block_pointerFvmbP7NSErrorE_block_invoke.367
- ____ZN14ControllerImpl22prepareRecordForStreamEP17AVVoiceControllerP25AVVCPrepareRecordSettingsU13block_pointerFvmbP7NSErrorE_block_invoke.368
- ____ZN14ControllerImpl22prepareRecordForStreamEP17AVVoiceControllerP25AVVCPrepareRecordSettingsU13block_pointerFvmbP7NSErrorE_block_invoke.369
- ____ZN14ControllerImpl22prepareRecordForStreamEP17AVVoiceControllerP25AVVCPrepareRecordSettingsU13block_pointerFvmbP7NSErrorE_block_invoke.370
- ____ZN14ControllerImpl22setDuckOthersForStreamEmP16AVVCDuckSettingsU13block_pointerFvmbP7NSErrorE_block_invoke.553
- ____ZN14ControllerImpl22setRecordModeForStreamEm27AVVoiceControllerRecordModeU13block_pointerFvmbP7NSErrorE_block_invoke.534
- ____ZN14ControllerImpl22setRecordModeForStreamEm27AVVoiceControllerRecordModeU13block_pointerFvmbP7NSErrorE_block_invoke.535
- ____ZN14ControllerImpl23VibeAlertCompletionProcEjP17AVVoiceControllerm_block_invoke.249
- ____ZN14ControllerImpl23playAlertWithCompletionEP17AVVoiceController16AVVoiceAlertType20AVVoiceAlertOverrideU13block_pointerFvS2_14AVVCAlertStateP7NSErrorE_block_invoke.485
- ____ZN14ControllerImpl23playAlertWithCompletionEP17AVVoiceController16AVVoiceAlertType20AVVoiceAlertOverrideU13block_pointerFvS2_14AVVCAlertStateP7NSErrorE_block_invoke.486
- ____ZN14ControllerImpl23playAlertWithCompletionEP17AVVoiceController16AVVoiceAlertType20AVVoiceAlertOverrideU13block_pointerFvS2_14AVVCAlertStateP7NSErrorE_block_invoke.488
- ____ZN14ControllerImpl23playAlertWithCompletionEP17AVVoiceController16AVVoiceAlertType20AVVoiceAlertOverrideU13block_pointerFvS2_14AVVCAlertStateP7NSErrorE_block_invoke.491
- ____ZN14ControllerImpl25updateMeterLevelForStreamEmU13block_pointerFvmbP7NSErrorE_block_invoke.512
- ____ZN14ControllerImpl25updateMeterLevelForStreamEmU13block_pointerFvmbP7NSErrorE_block_invoke.513
- ____ZN14ControllerImpl26getRecordSettingsForStreamEP17AVVoiceControllermU13block_pointerFvmP12NSDictionaryP7NSErrorE_block_invoke.505
- ____ZN14ControllerImpl26isMeteringEnabledForStreamEmU13block_pointerFvmbP7NSErrorE_block_invoke.509
- ____ZN14ControllerImpl27enableTriangleModeForStreamEmbU13block_pointerFvmbP7NSErrorE_block_invoke.565
- ____ZN14ControllerImpl27stopKeepAliveQueueForStreamEmU13block_pointerFvmbP7NSErrorE_block_invoke.575
- ____ZN14ControllerImpl28getRecordDeviceInfoForStreamEP17AVVoiceControllermU13block_pointerFvmP20AVVCRecordDeviceInfoP7NSErrorE_block_invoke.499
- ____ZN14ControllerImpl28getRecordDeviceInfoForStreamEP17AVVoiceControllermU13block_pointerFvmP20AVVCRecordDeviceInfoP7NSErrorE_block_invoke.501
- ____ZN14ControllerImpl28startKeepAliveQueueForStreamEmU13block_pointerFvmbP7NSErrorE_block_invoke.568
- ____ZN14ControllerImpl28startKeepAliveQueueForStreamEmU13block_pointerFvmbP7NSErrorE_block_invoke.571
- ____ZN14ControllerImpl28startKeepAliveQueueForStreamEmU13block_pointerFvmbP7NSErrorE_block_invoke_2.572
- ____ZN14ControllerImpl29activateAudioSessionForStreamEP17AVVoiceControllermbbU13block_pointerFvmbP7NSErrorE_block_invoke.446
- ____ZN14ControllerImpl29activateAudioSessionForStreamEP17AVVoiceControllermbbU13block_pointerFvmbP7NSErrorE_block_invoke.447
- ____ZN14ControllerImpl29activateAudioSessionForStreamEP17AVVoiceControllermbbU13block_pointerFvmbP7NSErrorE_block_invoke.448
- ____ZN14ControllerImpl29activateAudioSessionForStreamEP17AVVoiceControllermbbU13block_pointerFvmbP7NSErrorE_block_invoke.449
- ____ZN14ControllerImpl29activateAudioSessionForStreamEP17AVVoiceControllermbbU13block_pointerFvmbP7NSErrorE_block_invoke_2.455
- ____ZN14ControllerImpl30getCurrentStreamStateForStreamEP17AVVoiceControllermU13block_pointerFvmb15AVVCStreamStateP7NSErrorE_block_invoke.422
- ____ZN14ControllerImpl31configureAlertBehaviorForStreamEP17AVVoiceControllerP34AVVCConfigureAlertBehaviorSettingsU13block_pointerFvP7NSErrorE_block_invoke.429
- ____ZN14ControllerImpl31configureAlertBehaviorForStreamEP17AVVoiceControllerP34AVVCConfigureAlertBehaviorSettingsU13block_pointerFvP7NSErrorE_block_invoke.432
- ____ZN14ControllerImpl31enableSmartRoutingConsiderationEmbU13block_pointerFvmbP7NSErrorE_block_invoke.528
- ____ZN14ControllerImpl31getPeakPowerForStreamAndChannelEmiU13block_pointerFvmfP7NSErrorE_block_invoke.516
- ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.302
- ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.304
- ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.306
- ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.308
- ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.319
- ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.320
- ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.324
- ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.328
- ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.329
- ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.330
- ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.336
- ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.338
- ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.340
- ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.344
- ____ZN14ControllerImpl32_configureEngineCompletionBlocksEP17AVVoiceControllerNSt3__110shared_ptrI19AVVCRecordingEngineEE_block_invoke.345
- ____ZN14ControllerImpl32getRecordBufferDurationForStreamEmU13block_pointerFvmdP7NSErrorE_block_invoke.425
- ____ZN14ControllerImpl32setAnnounceCallsEnabledForStreamEmbU13block_pointerFvmbP7NSErrorE_block_invoke.550
- ____ZN14ControllerImpl34getAveragePowerForStreamAndChannelEmiU13block_pointerFvmfP7NSErrorE_block_invoke.524
- ____ZN14ControllerImpl36_createRecordingEngineWithParametersENSt3__110shared_ptrIS_EEP17AVVoiceControllerN19AVVCRecordingEngine10EngineTypeEP8NSStringlU13block_pointerFvNS1_IS5_EEE_block_invoke.290
- ____ZN14ControllerImpl40isDuckingSupportedOnPickedRouteForStreamEmU13block_pointerFvmbP7NSErrorE_block_invoke.562
- ____ZN25AVVCPluginRecordingEngine13stopRecordingEv_block_invoke.120
- ____ZN25AVVCPluginRecordingEngine14startRecordingEv_block_invoke.111
- ____ZN25AVVCPluginRecordingEngine17createRecordQueueEP12NSDictionary_block_invoke.132
- ____ZN25AVVCPluginRecordingEngine17createRecordQueueEP12NSDictionary_block_invoke.133
- ____ZN29AVVCAudioQueueRecordingEngine16handleAudioInputEP16OpaqueAudioQueueP16AudioQueueBufferPK14AudioTimeStampjPK28AudioStreamPacketDescription_block_invoke.153
- ___block_descriptor_60_ea8_40c44_ZTSNSt3__18weak_ptrI19AVVCRecordingEngineEE_e5_v8?0l
- ___block_descriptor_tmp.1186
- ___block_descriptor_tmp.1449
- ___block_descriptor_tmp.1457
- ___block_descriptor_tmp.6082
- ___block_descriptor_tmp.7
- ___block_literal_global.1375
- ___block_literal_global.142
- ___block_literal_global.1590
- ___block_literal_global.160
- ___block_literal_global.164
- ___block_literal_global.1730
- ___block_literal_global.193.8353
- ___block_literal_global.205
- ___block_literal_global.2111
- ___block_literal_global.230
- ___block_literal_global.2498
- ___block_literal_global.2816
- ___block_literal_global.3114
- ___block_literal_global.3410
- ___block_literal_global.349
- ___block_literal_global.38
- ___block_literal_global.5041
- ___block_literal_global.5636
- ___block_literal_global.6001
- ___block_literal_global.6064
- ___block_literal_global.6080
- ___block_literal_global.6522
- ___block_literal_global.7264
- ___block_literal_global.8004
- ___block_literal_global.8417
- ___block_literal_global.8612
CStrings:
+ "%25s:%-5d  CAGuard::CAGuard: Could not init the cond var"
+ "%25s:%-5d  CAGuard::Notify: failed"
+ "%25s:%-5d  CAGuard::NotifyAll: failed"
+ "%25s:%-5d  CAGuard::Wait: A thread has to have locked a guard before it can wait"
+ "%25s:%-5d  CAGuard::Wait: Could not wait for a signal"
+ "%25s:%-5d  CAGuard::WaitFor: A thread has to have locked a guard be for it can wait"
+ "%25s:%-5d  CAGuard::WaitFor: Wait got an error"
+ "%25s:%-5d  CAMutex::CAMutex: Could not init the mutex"
+ "%25s:%-5d  CAMutex::Lock: Could not lock the mutex"
+ "%25s:%-5d  CAMutex::Try: call to pthread_mutex_trylock failed, Error: %d (%s)"
+ "%25s:%-5d  CAMutex::Unlock: A thread is attempting to unlock a Mutex it doesn't own"
+ "%25s:%-5d  CAMutex::Unlock: Could not unlock the mutex"
+ "%25s:%-5d  CAPThread::Start: A thread could not be created in the detached state."
+ "%25s:%-5d  CAPThread::Start: Could not create a thread."
+ "%25s:%-5d  CAPThread::Start: Thread attributes could not be created."
+ "%25s:%-5d  ca_verify_noerr: [%s, %d]"
+ "%25s:%-5d AVVC starting (%s) recording at hosttime (%lld) for AQ engine"
+ "%25s:%-5d AVVC starting (%s) recording at hosttime (%lld) for HAC engine"
+ "%25s:%-5d AVVC starting (%s) recording at hosttime (%lld) for Plugin engine on device (%p)"
+ "%25s:%-5d AVVCAudioQueueRecordingEngine::updateMeterLevels: Error! Stream has not been prepared. Error(%d)"
+ "%25s:%-5d AVVCAudioQueueRecordingEngine::updateMeterLevels: Not fetching meter levels because one of them is untrue: mMeteringEnabled(%d), mRecordMeters(%d)"
+ "%25s:%-5d AVVCAudioQueueRecordingEngine::updateMeterLevels: Not fetching meter levels because one of them is untrue: mMeteringEnabled(%d), mRecordQueue(%d), mRecordMeters(%d)"
+ "%25s:%-5d AVVCHACRecordingEngine::handleInput resetting ignoreInputCallback"
+ "%25s:%-5d AVVCPluginRecordingEngine::startRecordingWithCompletionBlock: Recording cancelled by plugin device. Calling didStop recording and setting audioInputBlock to nil."
+ "%25s:%-5d AVVCPluginRecordingEngine::updateMeterLevels: Error! Stream has not been prepared. Error(%d)"
+ "%25s:%-5d AVVCRecordingEngine::getAveragePowerForChannel: Requested channel(%d) of numChannels(%d) from mRecordMeters(%p). Returning default value (%f)"
+ "%25s:%-5d AVVCRecordingEngine::getAveragePowerForChannel: Returning averagePower(%f) for streamID(%llu) for channel(%d) with numChannels(%d) mRecordMeters(%p)"
+ "%25s:%-5d AVVCRecordingEngine::getAveragePowerForChannel: Stream has not been prepared. Returning default value (%f)"
+ "%25s:%-5d AVVCRecordingEngine::getPeakPowerForChannel: Requested channel(%d) of numChannels(%d) from mRecordMeters(%p). Returning default value (%f)"
+ "%25s:%-5d AVVCRecordingEngine::getPeakPowerForChannel: Returning peakPower(%f) for streamID(%llu) for channel(%d) with numChannels(%d) mRecordMeters(%p)"
+ "%25s:%-5d AVVCRecordingEngine::getPeakPowerForChannel: Stream has not been prepared. Returning default value (%f)"
+ "%25s:%-5d AVVCSessionManager::setSessionActivationContext : No change - not setting activationMode and deviceUID. Current: { activationMode(%s), deviceUID(%@) }. Previous: { activationMode(%s), deviceUID(%@) }. No op."
+ "%25s:%-5d AVVCSessionManager::setSessionActivationContext : Setting new activation context. Current: { activationMode(%s), deviceUID(%@) }. Previous: { activationMode(%s), deviceUID(%@) }."
+ "%25s:%-5d Calling StopIsolatedAudio"
+ "%25s:%-5d Engine@%p: No input device available, cannot enable VoiceProcessing."
+ "%25s:%-5d First callback - AQ engine (%p) - Now: ( ht: %llu ), BuffStartTime: ( ht: %llu st: %f ), SiriRequestedStartTime: ( ht: %llu ). Now-SiriRequestedStartTime: %0.6f ms, BuffStartTime-SiriRequestedStartTime: %0.6f ms."
+ "%25s:%-5d First callback - HAC engine (%p) mIgnoreInputCallback (%d) - Now: ( ht: %llu ), BuffStartTime: ( ht: %llu st: %llu ), SiriRequestedStartTime: ( ht: %llu ). Now-SiriRequestedStartTime: %0.6f ms, BuffStartTime-SiriRequestedStartTime: %0.6f ms."
+ "%25s:%-5d First callback - Plugin engine (%p) - Now: ( ht: %llu ), BuffStartTime: ( ht: %llu st: %f ), SiriRequestedStartTime: ( ht: %llu ). Now-SiriRequestedStartTime: %0.6f ms"
+ "%25s:%-5d Remote shared buffer surface creation error"
+ "%25s:%-5d Shared buffer partitioning error"
+ "%25s:%-5d Shared buffer surface creation error. Frame capacity: %d"
+ "%25s:%-5d _removeEngineFromMap: Engine Map does not exist"
+ "%25s:%-5d _removeEngineFromMap: Engine for streamID(%llu) not found."
+ "%25s:%-5d _removeEngineFromMap: Stream state is (%s). Will stop recording before removing the engine."
+ "%25s:%-5d _removeEngineFromMap: engine[%@] engineType(%s) "
+ "%25s:%-5d createAudioConverter: AudioConverter already exists. Disposing old instance."
+ "%25s:%-5d createAudioConverter: AudioConverterDispose error(%d)"
+ "%25s:%-5d destroyRecordEngine: AudioConverterDispose error(%d)"
+ "%25s:%-5d encodeWithCoder called with an incompatible coder"
+ "%25s:%-5d exclaveSupport(%d) corespeechdConclaveEnabled(%d) isHACProduct(%d)"
+ "%25s:%-5d initWithCoder called with an incompatible coder"
+ "%25s:%-5d old config: %d newConfig: %d"
+ "%25s:%-5d player@0x%p failed to set label on audioqueue 0x%p: %d"
+ "%25s:%-5d record internally stopped, so throwing away buffer. ignoreInputCallback(%d), StreamState(%s). RecordCancelled(%d)"
+ "%25s:%-5d unilaterally_billed_shared_memory - bad IOsurface"
+ "%25s:%-5d unilaterally_billed_shared_memory - bad task token"
+ "%25s:%-5d unilaterally_billed_shared_memory - error on IOSurfaceCreate"
+ "%25s:%-5d unilaterally_billed_shared_memory - error on IOSurfaceSetOwnershipIdentity, memory will most likely be billed to both processes: %u"
+ "%25s:%-5d unilaterally_billed_shared_memory - error on task_create_identity_token: %u"
+ "%25s:%-5d unilaterally_billed_shared_memory - incorrect surface size"
+ "-[AVAudioSharedPCMBuffer initWithPCMFormat:frameCapacity:]"
+ "-[AVAudioSharedPCMBuffer initWithPCMFormat:sharedBufferToken:]"
+ "/Library/Caches/com.apple.xbs/Sources/AVFAudio/Source/AVFAudio/AVAudioEngine/AVAEUtility.mm"
+ "@\"CASpatialAudioExperience\""
+ "@28@0:8^{__IOSurface=}16I24"
+ "ASSERTION FAILED: AQ enqueue error while actively recording"
+ "ASSERTION FAILED: Unlocker attempted to unlock a mutex not owned by the current thread!"
+ "ASSERTION FAILED: attempting to prime record queue while queue is running"
+ "ASSERTION FAILED: getStatus called before object was configured!"
+ "ASSERTION FAILED: inPastFrameCount <= mFrameHistoryLength"
+ "ASSERTION FAILED: no alert buffer is enqueued!"
+ "ASSERTION FAILED: packetsRead <= packetsAvailable!"
+ "ASSERTION FAILED: queue was running when destroyed but not asked to stop"
+ "ASSERTION FAILED: re-entrant request for different alert type"
+ "ASSERTION FAILED: some buffers already enqueued!"
+ "ASSERTION FAILED: unregistering a nonexistent object!"
+ "ASSERTION FAILURE: AVVC_TIMEOUT occurred : for_each_engine timed out! Caller: %s"
+ "ASSERTION FAILURE: AVVC_TIMEOUT occurred : safeAllQueuesBarrier timed out!"
+ "ASSERTION FAILURE: mFramesPerPacket cannot be zero!"
+ "AVAEUtility.mm"
+ "AVAE_CheckFormatsValidAndMatching"
+ "AVAudioPlayerCpp.mm"
+ "AVAudioSharedBufferToken"
+ "AVAudioSharedBufferToken.mm"
+ "AVAudioSharedPCMBuffer"
+ "AVEncoderASPFrequencyKey"
+ "AVEncoderContentSourceKey"
+ "AVEncoderDRCConfigurationKey"
+ "AVVC_Log.mm"
+ "Audio Buffer Shared memory"
+ "AudioDataAnalysisManagerCreateNodeMicLevel"
+ "AudioDataAnalysisManagerProcessMicLevel"
+ "CAGuard.cpp"
+ "CAMutex.cpp"
+ "CAPThread.cpp"
+ "CAPThread::SetPriority: failed to set the fixed-priority policy, Error: 0x%X"
+ "CAPThread::SetPriority: failed to set the precedence policy, Error: 0x%X"
+ "CAPThread::SetTimeConstraints: thread_policy_set failed, Error: %d (%s)"
+ "CAPThread::Start: can't start because the thread is already running"
+ "Mach"
+ "SetFormats(format, false, *(fileASBD.streamDescription), avacl)"
+ "T@\"AVAudioSharedBufferToken\",R,N"
+ "T@\"CASpatialAudioExperience\",C,V_intendedSpatialExperience"
+ "XMachServer.cpp"
+ "^{_xpc_type_s=}16@0:8"
+ "_intendedSpatialExperience"
+ "_magicCookieMutex"
+ "_segmentReader->createExtAudioFile(&_extAudioFile)"
+ "arithmetic addition overflow"
+ "atsh"
+ "attributesOfItemAtPath:error:"
+ "avap"
+ "backedBySharedMemory"
+ "bad IOSurface"
+ "bad taskToken"
+ "clientFormat != nil"
+ "componentsWithURL:resolvingAgainstBaseURL:"
+ "decodeXPCObjectOfType:forKey:"
+ "encodeXPCObject:forKey:"
+ "failed to add the send right"
+ "hint"
+ "hwFormat != nil"
+ "initWithPCMFormat:sharedBufferToken:"
+ "initWithSurface:taskToken:"
+ "intendedSpatialExperience"
+ "isAUv2"
+ "queryItems"
+ "setIntendedSpatialExperience:"
+ "setUseInjectionDevice:"
+ "sharedBufferToken"
+ "string"
+ "surface"
+ "surfaceXPCType"
+ "taskToken"
+ "taskTokenXPCType"
+ "token"
+ "unilaterally_billed_shared_memory.mm"
+ "unique_lock::unlock: not locked"
+ "useInjectionDevice"
+ "{ObjectRef<__IOSurface *>=\"mCFObject\"^{__IOSurface}}"
+ "{ObjectRef<__IOSurface *>=^{__IOSurface}}16@0:8"
+ "{mach_port=\"m_mach_port\"I}"
+ "{mach_port=I}16@0:8"
+ "{unfair_lock=\"m_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}}"
+ "{unique_ptr<AVAudioFileImpl, std::default_delete<AVAudioFileImpl>>=\"__ptr_\"^{AVAudioFileImpl}}"
+ "{unique_ptr<PulseTone, std::default_delete<PulseTone>>=\"__ptr_\"^{PulseTone}}"
- " ASSERTION FAILED: AQ enqueue error while actively recording"
- " ASSERTION FAILED: Unlocker attempted to unlock a mutex not owned by the current thread!"
- " ASSERTION FAILED: attempting to prime record queue while queue is running"
- " ASSERTION FAILED: getStatus called before object was configured!"
- " ASSERTION FAILED: inPastFrameCount <= mFrameHistoryLength"
- " ASSERTION FAILED: no alert buffer is enqueued!"
- " ASSERTION FAILED: packetsRead <= packetsAvailable!"
- " ASSERTION FAILED: queue was running when destroyed but not asked to stop"
- " ASSERTION FAILED: re-entrant request for different alert type"
- " ASSERTION FAILED: some buffers already enqueued!"
- " ASSERTION FAILED: unregistering a nonexistent object!"
- " ASSERTION FAILURE: AVVC_TIMEOUT occurred : for_each_engine timed out! Caller: %s"
- " ASSERTION FAILURE: AVVC_TIMEOUT occurred : safeAllQueuesBarrier timed out!"
- " ASSERTION FAILURE: mFramesPerPacket cannot be zero!"
- " CAGuard::CAGuard: Could not init the cond var"
- " CAGuard::Notify: failed"
- " CAGuard::NotifyAll: failed"
- " CAGuard::Wait: A thread has to have locked a guard before it can wait"
- " CAGuard::Wait: Could not wait for a signal"
- " CAGuard::WaitFor: A thread has to have locked a guard be for it can wait"
- " CAGuard::WaitFor: Wait got an error"
- " CAMutex::CAMutex: Could not init the mutex"
- " CAMutex::Lock: Could not lock the mutex"
- " CAMutex::Try: call to pthread_mutex_trylock failed, Error: %d (%s)"
- " CAMutex::Unlock: A thread is attempting to unlock a Mutex it doesn't own"
- " CAMutex::Unlock: Could not unlock the mutex"
- " CAPThread::SetPriority: failed to set the fixed-priority policy, Error: 0x%X"
- " CAPThread::SetPriority: failed to set the precedence policy, Error: 0x%X"
- " CAPThread::SetTimeConstraints: thread_policy_set failed, Error: %d (%s)"
- " CAPThread::Start: A thread could not be created in the detached state."
- " CAPThread::Start: Could not create a thread."
- " CAPThread::Start: Thread attributes could not be created."
- " CAPThread::Start: can't start because the thread is already running"
- " ca_verify_noerr: [%s, %d]"
- "%25s:%-5d #### calling startRecordingWithCompletionBlock on device (%p) ####"
- "%25s:%-5d (%p) - First callback from AQ -  Now: ( ht: %lld ), BuffStartTime: ( ht: %lld st: %lld ), SiriRequestedStartTime: ( ht: %lld ). Now-SiriRequestedStartTime: %0.6f ms, BuffStartTime-SiriRequestedStartTime: %0.6f ms."
- "%25s:%-5d AVVC starting HAC record (%s) hosttime (%lld) "
- "%25s:%-5d AVVC starting record queue%s at (%s) hosttime (%lld) "
- "%25s:%-5d AVVCAudioQueueRecordingEngine::updateMeterLevels: not fetching meter levels because one of them is untrue! mMeteringEnabled(%d), mRecordQueue(%d), mRecordMeters(%d)"
- "%25s:%-5d AVVCSessionManager::setSessionActivationContext : No change - not setting activationMode and deviceUID. Previous: { activationMode(%s), deviceUID(%@) }. Current: { activationMode(%s), deviceUID(%@) }. No op."
- "%25s:%-5d AVVCSessionManager::setSessionActivationContext : Setting new activation context. Previous: { activationMode(%s), deviceUID(%@) }. Current: { activationMode(%s), deviceUID(%@) }."
- "%25s:%-5d ERROR: destroyRecordEngine: AudioConverterDispose err %d"
- "%25s:%-5d ERROR: destroyRecordEngine: AudioConverterDispose err %{audio:4CC}d"
- "%25s:%-5d Engine for streamID(%llu) not found."
- "%25s:%-5d HAC (%p) - First callback -  Now: ( ht: %lld ), BuffStartTime: ( ht: %lld st: %lld ), SiriRequestedStartTime: ( ht: %lld ). Now-SiriRequestedStartTime: %0.6f ms, BuffStartTime-SiriRequestedStartTime: %0.6f ms."
- "%25s:%-5d Stopping recording here, engine's remote device has been disconnected."
- "%25s:%-5d UpdateRecordDeviceOnQueue : AudioQueueSetProperty(kAudioQueueProperty_CurrentDevice) - %@"
- "%25s:%-5d UpdateRecordDeviceOnQueue: AudioQueueSetProperty(kAudioQueueProperty_CurrentDevice - %d)"
- "%25s:%-5d exclaveSupport: %d corespeechdConclaveEnabled: %d isHACProduct: %d"
- "%25s:%-5d forceUpdate: %d, old config: %d newConfig: %d"
- "%25s:%-5d getAveragePowerForChannel on stream(%llu): returning %f for channel %d"
- "%25s:%-5d getPeakPowerForChannel on stream(%llu): returning %f for channel %d"
- "%25s:%-5d getSessionProperties_HWConfig: HW config changed (not in response to client) -- stopping record"
- "%25s:%-5d record internally stopped, so throwing away buffer. StreamState(%s). RecordCancelled(%d)"
- "%25s:%-5d removeEngineFromMapWithStreamID: engine[%@] stream(%llu) "
- "%25s:%-5d startRecordingWithCompletionBlock: Recording cancelled by plugin device. Calling didStop recording and setting audioInputBlock to nil."
- "AVVC_Log.cpp"
- "CoreSpeech"
- "GetNumberBuffers"
- "player@0x%p failed to set label on audioqueue 0x%p: %d"
- "support_secure_platform_t8132"
- "support_secure_platform_t8140"
- "t8132"
- "t8140"
- "{unique_ptr<AVAudioFileImpl, std::default_delete<AVAudioFileImpl>>=\"__ptr_\"{__compressed_pair<AVAudioFileImpl *, std::default_delete<AVAudioFileImpl>>=\"__value_\"^{AVAudioFileImpl}}}"
- "{unique_ptr<PulseTone, std::default_delete<PulseTone>>=\"__ptr_\"{__compressed_pair<PulseTone *, std::default_delete<PulseTone>>=\"__value_\"^{PulseTone}}}"

```
