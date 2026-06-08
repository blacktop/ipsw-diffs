## AudioToolbox

> `/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`

```diff

-1556.604.2.0.0
-  __TEXT.__text: 0x2a868c
-  __TEXT.__auth_stubs: 0x3c00
+1619.4.0.0.0
+  __TEXT.__text: 0x26fb90
+  __TEXT.__realtime: 0x266a4
   __TEXT.__delay_stubs: 0x100
   __TEXT.__delay_helper: 0x148
-  __TEXT.__objc_methlist: 0x203c
-  __TEXT.__const: 0x1314
-  __TEXT.__dlopen_cstrs: 0x71d
-  __TEXT.__gcc_except_tab: 0x28a40
-  __TEXT.__cstring: 0x2026b
-  __TEXT.__oslogstring: 0x3b61e
-  __TEXT.__unwind_info: 0xc988
-  __TEXT.__objc_classname: 0x417
-  __TEXT.__objc_methname: 0x5d13
-  __TEXT.__objc_methtype: 0x395c
-  __TEXT.__objc_stubs: 0x4640
-  __DATA_CONST.__got: 0xe68
-  __DATA_CONST.__const: 0x34f8
-  __DATA_CONST.__objc_classlist: 0xd8
-  __DATA_CONST.__objc_protolist: 0x90
+  __TEXT.__objc_methlist: 0x205c
+  __TEXT.__const: 0x486c
+  __TEXT.__dlopen_cstrs: 0x84f
+  __TEXT.__gcc_except_tab: 0x22f00
+  __TEXT.__cstring: 0x22b1f
+  __TEXT.__oslogstring: 0x37544
+  __TEXT.__unwind_info: 0xca38
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x3580
+  __DATA_CONST.__objc_classlist: 0xd0
+  __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1808
+  __DATA_CONST.__objc_selrefs: 0x16f8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0xc0
-  __DATA_CONST.__objc_arraydata: 0x358
-  __AUTH_CONST.__auth_got: 0x1e38
-  __AUTH_CONST.__const: 0x10fb8
-  __AUTH_CONST.__cfstring: 0x5cc0
-  __AUTH_CONST.__objc_const: 0x3250
-  __AUTH_CONST.__objc_intobj: 0x5d0
-  __AUTH_CONST.__objc_arrayobj: 0x408
-  __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x230
+  __DATA_CONST.__objc_superrefs: 0xb8
+  __DATA_CONST.__objc_arraydata: 0x3a8
+  __DATA_CONST.__got: 0xdc8
+  __AUTH_CONST.__const: 0x116c8
+  __AUTH_CONST.__cfstring: 0x5da0
+  __AUTH_CONST.__objc_const: 0x30f0
+  __AUTH_CONST.__weak_auth_got: 0x38
+  __AUTH_CONST.__objc_intobj: 0x5e8
+  __AUTH_CONST.__objc_arrayobj: 0x510
+  __AUTH_CONST.__auth_got: 0x1bb0
+  __AUTH.__objc_data: 0x280
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x230
-  __DATA.__data: 0x830
-  __DATA.__bss: 0x1ff1
-  __DATA_DIRTY.__objc_data: 0x640
-  __DATA_DIRTY.__data: 0x48
-  __DATA_DIRTY.__bss: 0x2a60
+  __DATA.__objc_ivar: 0x204
+  __DATA.__data: 0x88c
+  __DATA.__bss: 0x24f0
+  __DATA_DIRTY.__objc_data: 0x5a0
+  __DATA_DIRTY.__data: 0x4c
+  __DATA_DIRTY.__bss: 0x308
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/WatchdogClient.framework/WatchdogClient
   - /System/Library/PrivateFrameworks/caulk.framework/caulk
   - /usr/lib/libAudioStatistics.dylib
-  - /usr/lib/libAudioToolboxUtility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 330A22B5-ABFD-3DA7-B819-CAB514B9BEF2
-  Functions: 9543
-  Symbols:   26425
-  CStrings:  9842
+  UUID: 2B0803B7-FD0E-30D5-BD93-AC288B8989C2
+  Functions: 9924
+  Symbols:   26790
+  CStrings:  8077
 
Symbols:
+ -[ATATranslatorClientDelegate .cxx_construct]
+ -[ATATranslatorClientDelegate .cxx_destruct]
+ -[ATATranslatorClientDelegate audioGenerationDidFinishForClient:]
+ -[ATATranslatorClientDelegate client:didGenerateTranslatedAudio:]
+ -[ATATranslatorClientDelegate client:didPauseTranslationWithReason:]
+ -[ATATranslatorClientDelegate client:didReceiveTranscriptionResult:]
+ -[ATATranslatorClientDelegate client:didReceiveTranslationResult:]
+ -[ATATranslatorClientDelegate client:didStopTranslationWithError:]
+ -[ATATranslatorClientDelegate client:willStartTranslatedAudioWithMetadata:]
+ -[ATATranslatorClientDelegate initWithWeakImpl:scope:]
+ -[ATATranslatorClientDelegate serverDidDisconnectForClient:]
+ -[ATATranslatorClientDelegate translationDidResumeForClient:]
+ -[ATATranslatorClientDelegate translationDidStartForClient:]
+ -[ATServerDelegatePriv updateContentMixingMode:forSession:]
+ -[AVHapticServer buildActiveProcessesForPowerLogForAudio:haptics:]
+ -[AVHapticServer buildClientsStringFromEntries:returningLastEntry:]
+ -[AVHapticServer clientTypeForEntry:withClientID:]
+ -[AVHapticServer displayPrewarmedProcessEntriesWithPrewarmTime:]
+ -[AVHapticServer forceStopIdleBackgroundRunningClients]
+ -[AVHapticServer forceStopIdleDaemonClients]
+ -[AVHapticServer forceUnprewarmEligibleClients]
+ -[AVHapticServer getPrewarmedClientEntries]
+ -[AVHapticServer getRunningClientEntries]
+ -[AVHapticServer performAction:forClientsMatchingPredicate:]
+ -[AVHapticServer reportRunningCountToPowerLogForAudio:haptics:entry:]
+ -[AVHapticServerInstance handleSynthOutputNotificationDeviceStoppedFromBelow:]
+ -[AVHapticServerInstance hapticSession]
+ -[AVHapticServerInstance initWithServer:id:connection:outError:]
+ -[AVHapticServerInstance server]
+ -[STTranslatorClientDelegate .cxx_construct]
+ -[STTranslatorClientDelegate .cxx_destruct]
+ -[STTranslatorClientDelegate audioGenerationDidFinishForClient:]
+ -[STTranslatorClientDelegate client:didGenerateTranslatedAudio:]
+ -[STTranslatorClientDelegate client:didPauseTranslationWithReason:]
+ -[STTranslatorClientDelegate client:didReceiveTranscriptionResult:]
+ -[STTranslatorClientDelegate client:didReceiveTranslationResult:]
+ -[STTranslatorClientDelegate client:didStopTranslationWithError:]
+ -[STTranslatorClientDelegate client:willStartTranslatedAudioWithMetadata:]
+ -[STTranslatorClientDelegate initWithWeakImpl:scope:]
+ -[STTranslatorClientDelegate serverDidDisconnectForClient:]
+ -[STTranslatorClientDelegate translationDidResumeForClient:]
+ -[STTranslatorClientDelegate translationDidStartForClient:]
+ GCC_except_table10001
+ GCC_except_table10003
+ GCC_except_table10005
+ GCC_except_table10007
+ GCC_except_table10009
+ GCC_except_table10011
+ GCC_except_table10013
+ GCC_except_table10015
+ GCC_except_table10017
+ GCC_except_table10019
+ GCC_except_table10021
+ GCC_except_table10023
+ GCC_except_table10025
+ GCC_except_table10027
+ GCC_except_table10029
+ GCC_except_table10031
+ GCC_except_table10033
+ GCC_except_table10035
+ GCC_except_table10037
+ GCC_except_table10039
+ GCC_except_table10041
+ GCC_except_table10043
+ GCC_except_table10045
+ GCC_except_table10050
+ GCC_except_table10051
+ GCC_except_table10052
+ GCC_except_table10056
+ GCC_except_table10058
+ GCC_except_table1006
+ GCC_except_table10063
+ GCC_except_table10064
+ GCC_except_table10066
+ GCC_except_table10067
+ GCC_except_table10068
+ GCC_except_table10070
+ GCC_except_table10074
+ GCC_except_table10075
+ GCC_except_table10076
+ GCC_except_table10078
+ GCC_except_table10079
+ GCC_except_table1009
+ GCC_except_table1010
+ GCC_except_table10112
+ GCC_except_table10115
+ GCC_except_table10118
+ GCC_except_table1012
+ GCC_except_table10127
+ GCC_except_table1013
+ GCC_except_table10130
+ GCC_except_table10131
+ GCC_except_table10132
+ GCC_except_table10133
+ GCC_except_table10136
+ GCC_except_table10139
+ GCC_except_table1014
+ GCC_except_table10144
+ GCC_except_table1015
+ GCC_except_table10150
+ GCC_except_table10151
+ GCC_except_table1016
+ GCC_except_table10160
+ GCC_except_table10164
+ GCC_except_table1017
+ GCC_except_table1018
+ GCC_except_table1019
+ GCC_except_table10195
+ GCC_except_table10196
+ GCC_except_table102
+ GCC_except_table1020
+ GCC_except_table1021
+ GCC_except_table1022
+ GCC_except_table10226
+ GCC_except_table10227
+ GCC_except_table10228
+ GCC_except_table1024
+ GCC_except_table1025
+ GCC_except_table1026
+ GCC_except_table1027
+ GCC_except_table1028
+ GCC_except_table1030
+ GCC_except_table1033
+ GCC_except_table105
+ GCC_except_table1081
+ GCC_except_table1083
+ GCC_except_table1101
+ GCC_except_table1103
+ GCC_except_table1109
+ GCC_except_table1117
+ GCC_except_table1121
+ GCC_except_table1122
+ GCC_except_table1129
+ GCC_except_table1136
+ GCC_except_table1139
+ GCC_except_table1140
+ GCC_except_table1144
+ GCC_except_table1145
+ GCC_except_table1149
+ GCC_except_table1156
+ GCC_except_table117
+ GCC_except_table1173
+ GCC_except_table1177
+ GCC_except_table118
+ GCC_except_table1187
+ GCC_except_table1193
+ GCC_except_table1198
+ GCC_except_table1200
+ GCC_except_table1202
+ GCC_except_table1203
+ GCC_except_table1204
+ GCC_except_table1206
+ GCC_except_table1207
+ GCC_except_table1209
+ GCC_except_table1210
+ GCC_except_table1211
+ GCC_except_table1212
+ GCC_except_table1213
+ GCC_except_table1216
+ GCC_except_table1217
+ GCC_except_table1222
+ GCC_except_table1225
+ GCC_except_table1226
+ GCC_except_table1227
+ GCC_except_table1235
+ GCC_except_table125
+ GCC_except_table1259
+ GCC_except_table1265
+ GCC_except_table1266
+ GCC_except_table1267
+ GCC_except_table1275
+ GCC_except_table1276
+ GCC_except_table1277
+ GCC_except_table1278
+ GCC_except_table1280
+ GCC_except_table1284
+ GCC_except_table1287
+ GCC_except_table1289
+ GCC_except_table1290
+ GCC_except_table1291
+ GCC_except_table1297
+ GCC_except_table1299
+ GCC_except_table130
+ GCC_except_table1300
+ GCC_except_table1301
+ GCC_except_table1302
+ GCC_except_table1303
+ GCC_except_table1338
+ GCC_except_table1343
+ GCC_except_table135
+ GCC_except_table1352
+ GCC_except_table1355
+ GCC_except_table1361
+ GCC_except_table1362
+ GCC_except_table1364
+ GCC_except_table1367
+ GCC_except_table1387
+ GCC_except_table1391
+ GCC_except_table1392
+ GCC_except_table1403
+ GCC_except_table1404
+ GCC_except_table1405
+ GCC_except_table1411
+ GCC_except_table1413
+ GCC_except_table1414
+ GCC_except_table1419
+ GCC_except_table1422
+ GCC_except_table1429
+ GCC_except_table1430
+ GCC_except_table1431
+ GCC_except_table1437
+ GCC_except_table1441
+ GCC_except_table145
+ GCC_except_table1454
+ GCC_except_table146
+ GCC_except_table1462
+ GCC_except_table1463
+ GCC_except_table1464
+ GCC_except_table1465
+ GCC_except_table1466
+ GCC_except_table1472
+ GCC_except_table1475
+ GCC_except_table1476
+ GCC_except_table1478
+ GCC_except_table1480
+ GCC_except_table1481
+ GCC_except_table1482
+ GCC_except_table1483
+ GCC_except_table1488
+ GCC_except_table149
+ GCC_except_table1494
+ GCC_except_table1495
+ GCC_except_table1549
+ GCC_except_table1550
+ GCC_except_table1552
+ GCC_except_table1555
+ GCC_except_table1556
+ GCC_except_table1558
+ GCC_except_table1559
+ GCC_except_table156
+ GCC_except_table1563
+ GCC_except_table1568
+ GCC_except_table1569
+ GCC_except_table158
+ GCC_except_table1585
+ GCC_except_table1594
+ GCC_except_table1601
+ GCC_except_table1602
+ GCC_except_table1609
+ GCC_except_table1619
+ GCC_except_table1620
+ GCC_except_table1623
+ GCC_except_table1627
+ GCC_except_table1634
+ GCC_except_table1635
+ GCC_except_table1636
+ GCC_except_table164
+ GCC_except_table1641
+ GCC_except_table1646
+ GCC_except_table1647
+ GCC_except_table1650
+ GCC_except_table1651
+ GCC_except_table1654
+ GCC_except_table1655
+ GCC_except_table1656
+ GCC_except_table1658
+ GCC_except_table1659
+ GCC_except_table1660
+ GCC_except_table1662
+ GCC_except_table1663
+ GCC_except_table1667
+ GCC_except_table167
+ GCC_except_table1670
+ GCC_except_table1671
+ GCC_except_table1672
+ GCC_except_table1675
+ GCC_except_table1676
+ GCC_except_table1677
+ GCC_except_table1679
+ GCC_except_table1683
+ GCC_except_table1685
+ GCC_except_table169
+ GCC_except_table170
+ GCC_except_table1709
+ GCC_except_table171
+ GCC_except_table1711
+ GCC_except_table1713
+ GCC_except_table1718
+ GCC_except_table1723
+ GCC_except_table1725
+ GCC_except_table1730
+ GCC_except_table1732
+ GCC_except_table1733
+ GCC_except_table1734
+ GCC_except_table1735
+ GCC_except_table1740
+ GCC_except_table1741
+ GCC_except_table1742
+ GCC_except_table1743
+ GCC_except_table1772
+ GCC_except_table1773
+ GCC_except_table179
+ GCC_except_table1798
+ GCC_except_table1799
+ GCC_except_table180
+ GCC_except_table1803
+ GCC_except_table1805
+ GCC_except_table1808
+ GCC_except_table1809
+ GCC_except_table1813
+ GCC_except_table1817
+ GCC_except_table182
+ GCC_except_table1824
+ GCC_except_table184
+ GCC_except_table185
+ GCC_except_table1851
+ GCC_except_table1853
+ GCC_except_table1867
+ GCC_except_table1868
+ GCC_except_table1871
+ GCC_except_table1877
+ GCC_except_table1880
+ GCC_except_table1881
+ GCC_except_table1884
+ GCC_except_table1885
+ GCC_except_table1888
+ GCC_except_table1891
+ GCC_except_table1894
+ GCC_except_table1896
+ GCC_except_table1897
+ GCC_except_table1898
+ GCC_except_table1899
+ GCC_except_table1915
+ GCC_except_table1918
+ GCC_except_table1922
+ GCC_except_table1924
+ GCC_except_table196
+ GCC_except_table1990
+ GCC_except_table1991
+ GCC_except_table2007
+ GCC_except_table2008
+ GCC_except_table2009
+ GCC_except_table2012
+ GCC_except_table2018
+ GCC_except_table2019
+ GCC_except_table202
+ GCC_except_table2021
+ GCC_except_table2022
+ GCC_except_table2025
+ GCC_except_table2028
+ GCC_except_table203
+ GCC_except_table2044
+ GCC_except_table2045
+ GCC_except_table2046
+ GCC_except_table2047
+ GCC_except_table2054
+ GCC_except_table2057
+ GCC_except_table2058
+ GCC_except_table2059
+ GCC_except_table2060
+ GCC_except_table2061
+ GCC_except_table2062
+ GCC_except_table2063
+ GCC_except_table2066
+ GCC_except_table2067
+ GCC_except_table2068
+ GCC_except_table2070
+ GCC_except_table2072
+ GCC_except_table2075
+ GCC_except_table2076
+ GCC_except_table2078
+ GCC_except_table2080
+ GCC_except_table2085
+ GCC_except_table2089
+ GCC_except_table2093
+ GCC_except_table2096
+ GCC_except_table2097
+ GCC_except_table2099
+ GCC_except_table2102
+ GCC_except_table2103
+ GCC_except_table2106
+ GCC_except_table2109
+ GCC_except_table2112
+ GCC_except_table2115
+ GCC_except_table2116
+ GCC_except_table2118
+ GCC_except_table2123
+ GCC_except_table2124
+ GCC_except_table2126
+ GCC_except_table2127
+ GCC_except_table2128
+ GCC_except_table2129
+ GCC_except_table2141
+ GCC_except_table2143
+ GCC_except_table2172
+ GCC_except_table2175
+ GCC_except_table2179
+ GCC_except_table2180
+ GCC_except_table2181
+ GCC_except_table2194
+ GCC_except_table2210
+ GCC_except_table2211
+ GCC_except_table2213
+ GCC_except_table2215
+ GCC_except_table2225
+ GCC_except_table2230
+ GCC_except_table2235
+ GCC_except_table2239
+ GCC_except_table224
+ GCC_except_table2248
+ GCC_except_table2250
+ GCC_except_table2268
+ GCC_except_table2269
+ GCC_except_table2271
+ GCC_except_table2278
+ GCC_except_table229
+ GCC_except_table2295
+ GCC_except_table2297
+ GCC_except_table231
+ GCC_except_table2310
+ GCC_except_table2320
+ GCC_except_table2322
+ GCC_except_table2337
+ GCC_except_table234
+ GCC_except_table2341
+ GCC_except_table2343
+ GCC_except_table2345
+ GCC_except_table2350
+ GCC_except_table2352
+ GCC_except_table2354
+ GCC_except_table2355
+ GCC_except_table2357
+ GCC_except_table2358
+ GCC_except_table2366
+ GCC_except_table2368
+ GCC_except_table237
+ GCC_except_table2372
+ GCC_except_table2374
+ GCC_except_table2375
+ GCC_except_table2376
+ GCC_except_table2377
+ GCC_except_table2378
+ GCC_except_table2379
+ GCC_except_table238
+ GCC_except_table2384
+ GCC_except_table239
+ GCC_except_table2391
+ GCC_except_table2392
+ GCC_except_table2393
+ GCC_except_table2394
+ GCC_except_table2396
+ GCC_except_table24
+ GCC_except_table2402
+ GCC_except_table2404
+ GCC_except_table2405
+ GCC_except_table2406
+ GCC_except_table2407
+ GCC_except_table2417
+ GCC_except_table2418
+ GCC_except_table244
+ GCC_except_table2444
+ GCC_except_table2449
+ GCC_except_table2456
+ GCC_except_table2467
+ GCC_except_table2469
+ GCC_except_table2472
+ GCC_except_table2474
+ GCC_except_table2485
+ GCC_except_table2490
+ GCC_except_table250
+ GCC_except_table2524
+ GCC_except_table2532
+ GCC_except_table2534
+ GCC_except_table2539
+ GCC_except_table256
+ GCC_except_table2583
+ GCC_except_table2585
+ GCC_except_table2592
+ GCC_except_table260
+ GCC_except_table2608
+ GCC_except_table2609
+ GCC_except_table261
+ GCC_except_table2610
+ GCC_except_table2611
+ GCC_except_table2612
+ GCC_except_table2614
+ GCC_except_table2616
+ GCC_except_table2624
+ GCC_except_table2625
+ GCC_except_table2626
+ GCC_except_table2627
+ GCC_except_table2631
+ GCC_except_table2636
+ GCC_except_table2645
+ GCC_except_table2646
+ GCC_except_table2647
+ GCC_except_table2648
+ GCC_except_table2653
+ GCC_except_table2655
+ GCC_except_table2656
+ GCC_except_table2667
+ GCC_except_table2674
+ GCC_except_table2676
+ GCC_except_table2680
+ GCC_except_table2681
+ GCC_except_table2688
+ GCC_except_table270
+ GCC_except_table2706
+ GCC_except_table2718
+ GCC_except_table2723
+ GCC_except_table2725
+ GCC_except_table2727
+ GCC_except_table2728
+ GCC_except_table2733
+ GCC_except_table2734
+ GCC_except_table2738
+ GCC_except_table2743
+ GCC_except_table2745
+ GCC_except_table2747
+ GCC_except_table2750
+ GCC_except_table2770
+ GCC_except_table2778
+ GCC_except_table2779
+ GCC_except_table2781
+ GCC_except_table2783
+ GCC_except_table2785
+ GCC_except_table2788
+ GCC_except_table2789
+ GCC_except_table2790
+ GCC_except_table2795
+ GCC_except_table2799
+ GCC_except_table28
+ GCC_except_table280
+ GCC_except_table2805
+ GCC_except_table2807
+ GCC_except_table2809
+ GCC_except_table281
+ GCC_except_table2814
+ GCC_except_table2815
+ GCC_except_table2817
+ GCC_except_table282
+ GCC_except_table2825
+ GCC_except_table2831
+ GCC_except_table2834
+ GCC_except_table2842
+ GCC_except_table2844
+ GCC_except_table2845
+ GCC_except_table2847
+ GCC_except_table2848
+ GCC_except_table2856
+ GCC_except_table2858
+ GCC_except_table2859
+ GCC_except_table2867
+ GCC_except_table2876
+ GCC_except_table2878
+ GCC_except_table2895
+ GCC_except_table290
+ GCC_except_table291
+ GCC_except_table2923
+ GCC_except_table2926
+ GCC_except_table293
+ GCC_except_table294
+ GCC_except_table2942
+ GCC_except_table2966
+ GCC_except_table2967
+ GCC_except_table2968
+ GCC_except_table2969
+ GCC_except_table2970
+ GCC_except_table2971
+ GCC_except_table2977
+ GCC_except_table2978
+ GCC_except_table298
+ GCC_except_table2981
+ GCC_except_table300
+ GCC_except_table3002
+ GCC_except_table3003
+ GCC_except_table3004
+ GCC_except_table3006
+ GCC_except_table3007
+ GCC_except_table3008
+ GCC_except_table3011
+ GCC_except_table3013
+ GCC_except_table3014
+ GCC_except_table302
+ GCC_except_table3023
+ GCC_except_table3026
+ GCC_except_table3027
+ GCC_except_table303
+ GCC_except_table3035
+ GCC_except_table3041
+ GCC_except_table3042
+ GCC_except_table3043
+ GCC_except_table3044
+ GCC_except_table3045
+ GCC_except_table3046
+ GCC_except_table3047
+ GCC_except_table3048
+ GCC_except_table3049
+ GCC_except_table3068
+ GCC_except_table3074
+ GCC_except_table3089
+ GCC_except_table3090
+ GCC_except_table3091
+ GCC_except_table3104
+ GCC_except_table3108
+ GCC_except_table3109
+ GCC_except_table3110
+ GCC_except_table3112
+ GCC_except_table3125
+ GCC_except_table3127
+ GCC_except_table3138
+ GCC_except_table3139
+ GCC_except_table3160
+ GCC_except_table3161
+ GCC_except_table3162
+ GCC_except_table3163
+ GCC_except_table3204
+ GCC_except_table3212
+ GCC_except_table3215
+ GCC_except_table3216
+ GCC_except_table3221
+ GCC_except_table3222
+ GCC_except_table3223
+ GCC_except_table3226
+ GCC_except_table3228
+ GCC_except_table3229
+ GCC_except_table3230
+ GCC_except_table3231
+ GCC_except_table3234
+ GCC_except_table3235
+ GCC_except_table3243
+ GCC_except_table3244
+ GCC_except_table3245
+ GCC_except_table3246
+ GCC_except_table3247
+ GCC_except_table3248
+ GCC_except_table3249
+ GCC_except_table3250
+ GCC_except_table3251
+ GCC_except_table3252
+ GCC_except_table3254
+ GCC_except_table3255
+ GCC_except_table3260
+ GCC_except_table3263
+ GCC_except_table3264
+ GCC_except_table3265
+ GCC_except_table3271
+ GCC_except_table3273
+ GCC_except_table3274
+ GCC_except_table3275
+ GCC_except_table3276
+ GCC_except_table3277
+ GCC_except_table3281
+ GCC_except_table3283
+ GCC_except_table3284
+ GCC_except_table3285
+ GCC_except_table3287
+ GCC_except_table3288
+ GCC_except_table3294
+ GCC_except_table3295
+ GCC_except_table3296
+ GCC_except_table3297
+ GCC_except_table3298
+ GCC_except_table3299
+ GCC_except_table3300
+ GCC_except_table3301
+ GCC_except_table3302
+ GCC_except_table3304
+ GCC_except_table3306
+ GCC_except_table3307
+ GCC_except_table3308
+ GCC_except_table3309
+ GCC_except_table3310
+ GCC_except_table3311
+ GCC_except_table3312
+ GCC_except_table3313
+ GCC_except_table3314
+ GCC_except_table3315
+ GCC_except_table3316
+ GCC_except_table3317
+ GCC_except_table3318
+ GCC_except_table3320
+ GCC_except_table3324
+ GCC_except_table3325
+ GCC_except_table3326
+ GCC_except_table3328
+ GCC_except_table3329
+ GCC_except_table3335
+ GCC_except_table3339
+ GCC_except_table3340
+ GCC_except_table3343
+ GCC_except_table3347
+ GCC_except_table3354
+ GCC_except_table337
+ GCC_except_table3396
+ GCC_except_table3398
+ GCC_except_table3399
+ GCC_except_table341
+ GCC_except_table343
+ GCC_except_table3448
+ GCC_except_table3450
+ GCC_except_table3455
+ GCC_except_table3457
+ GCC_except_table3458
+ GCC_except_table3459
+ GCC_except_table3477
+ GCC_except_table3479
+ GCC_except_table3481
+ GCC_except_table3482
+ GCC_except_table3483
+ GCC_except_table3484
+ GCC_except_table3486
+ GCC_except_table3488
+ GCC_except_table3534
+ GCC_except_table3537
+ GCC_except_table3539
+ GCC_except_table3542
+ GCC_except_table3547
+ GCC_except_table3548
+ GCC_except_table3549
+ GCC_except_table3550
+ GCC_except_table3554
+ GCC_except_table3560
+ GCC_except_table3563
+ GCC_except_table3565
+ GCC_except_table3566
+ GCC_except_table3578
+ GCC_except_table3591
+ GCC_except_table3593
+ GCC_except_table3594
+ GCC_except_table3595
+ GCC_except_table3596
+ GCC_except_table3597
+ GCC_except_table3598
+ GCC_except_table3619
+ GCC_except_table3621
+ GCC_except_table3624
+ GCC_except_table3625
+ GCC_except_table3626
+ GCC_except_table3643
+ GCC_except_table3646
+ GCC_except_table3648
+ GCC_except_table3651
+ GCC_except_table3652
+ GCC_except_table3653
+ GCC_except_table3654
+ GCC_except_table3656
+ GCC_except_table3657
+ GCC_except_table3658
+ GCC_except_table3660
+ GCC_except_table3665
+ GCC_except_table3679
+ GCC_except_table3680
+ GCC_except_table3685
+ GCC_except_table3686
+ GCC_except_table3688
+ GCC_except_table3705
+ GCC_except_table3711
+ GCC_except_table3712
+ GCC_except_table3713
+ GCC_except_table3716
+ GCC_except_table3717
+ GCC_except_table3735
+ GCC_except_table3736
+ GCC_except_table3739
+ GCC_except_table3742
+ GCC_except_table3744
+ GCC_except_table3745
+ GCC_except_table3747
+ GCC_except_table3749
+ GCC_except_table3760
+ GCC_except_table3767
+ GCC_except_table3768
+ GCC_except_table3769
+ GCC_except_table3770
+ GCC_except_table3771
+ GCC_except_table3772
+ GCC_except_table3774
+ GCC_except_table3776
+ GCC_except_table3779
+ GCC_except_table379
+ GCC_except_table3792
+ GCC_except_table3797
+ GCC_except_table3798
+ GCC_except_table38
+ GCC_except_table3800
+ GCC_except_table3807
+ GCC_except_table3808
+ GCC_except_table3811
+ GCC_except_table3813
+ GCC_except_table3814
+ GCC_except_table3819
+ GCC_except_table3820
+ GCC_except_table3822
+ GCC_except_table3826
+ GCC_except_table3828
+ GCC_except_table3829
+ GCC_except_table3830
+ GCC_except_table3831
+ GCC_except_table3833
+ GCC_except_table3850
+ GCC_except_table3854
+ GCC_except_table3858
+ GCC_except_table3860
+ GCC_except_table3865
+ GCC_except_table3870
+ GCC_except_table3871
+ GCC_except_table3874
+ GCC_except_table3883
+ GCC_except_table3892
+ GCC_except_table3894
+ GCC_except_table3895
+ GCC_except_table3896
+ GCC_except_table3897
+ GCC_except_table3898
+ GCC_except_table3901
+ GCC_except_table3907
+ GCC_except_table3918
+ GCC_except_table392
+ GCC_except_table3921
+ GCC_except_table3931
+ GCC_except_table3932
+ GCC_except_table3933
+ GCC_except_table394
+ GCC_except_table3941
+ GCC_except_table3952
+ GCC_except_table3975
+ GCC_except_table3979
+ GCC_except_table3981
+ GCC_except_table3988
+ GCC_except_table3992
+ GCC_except_table3993
+ GCC_except_table3998
+ GCC_except_table3999
+ GCC_except_table4001
+ GCC_except_table401
+ GCC_except_table4033
+ GCC_except_table4038
+ GCC_except_table4039
+ GCC_except_table4040
+ GCC_except_table4046
+ GCC_except_table4048
+ GCC_except_table406
+ GCC_except_table407
+ GCC_except_table408
+ GCC_except_table410
+ GCC_except_table4140
+ GCC_except_table415
+ GCC_except_table4155
+ GCC_except_table4171
+ GCC_except_table4172
+ GCC_except_table4173
+ GCC_except_table4175
+ GCC_except_table4177
+ GCC_except_table4180
+ GCC_except_table4183
+ GCC_except_table4187
+ GCC_except_table4189
+ GCC_except_table4196
+ GCC_except_table4213
+ GCC_except_table4214
+ GCC_except_table4224
+ GCC_except_table4226
+ GCC_except_table4231
+ GCC_except_table4232
+ GCC_except_table4233
+ GCC_except_table4234
+ GCC_except_table4235
+ GCC_except_table4236
+ GCC_except_table4238
+ GCC_except_table4242
+ GCC_except_table4243
+ GCC_except_table4245
+ GCC_except_table4247
+ GCC_except_table4249
+ GCC_except_table4252
+ GCC_except_table4263
+ GCC_except_table4265
+ GCC_except_table4270
+ GCC_except_table4272
+ GCC_except_table4279
+ GCC_except_table4280
+ GCC_except_table4281
+ GCC_except_table4286
+ GCC_except_table4294
+ GCC_except_table4297
+ GCC_except_table4299
+ GCC_except_table43
+ GCC_except_table430
+ GCC_except_table4301
+ GCC_except_table4305
+ GCC_except_table4306
+ GCC_except_table4307
+ GCC_except_table4308
+ GCC_except_table4314
+ GCC_except_table4315
+ GCC_except_table4317
+ GCC_except_table4318
+ GCC_except_table4319
+ GCC_except_table4320
+ GCC_except_table4321
+ GCC_except_table4322
+ GCC_except_table4323
+ GCC_except_table4325
+ GCC_except_table4327
+ GCC_except_table4328
+ GCC_except_table4329
+ GCC_except_table4333
+ GCC_except_table4339
+ GCC_except_table4350
+ GCC_except_table4357
+ GCC_except_table4359
+ GCC_except_table4368
+ GCC_except_table437
+ GCC_except_table4374
+ GCC_except_table4433
+ GCC_except_table4436
+ GCC_except_table4439
+ GCC_except_table444
+ GCC_except_table4446
+ GCC_except_table4447
+ GCC_except_table4458
+ GCC_except_table446
+ GCC_except_table4461
+ GCC_except_table4464
+ GCC_except_table4468
+ GCC_except_table4471
+ GCC_except_table4499
+ GCC_except_table4510
+ GCC_except_table4526
+ GCC_except_table4533
+ GCC_except_table4534
+ GCC_except_table4547
+ GCC_except_table4548
+ GCC_except_table4551
+ GCC_except_table4554
+ GCC_except_table4559
+ GCC_except_table4560
+ GCC_except_table4561
+ GCC_except_table457
+ GCC_except_table4570
+ GCC_except_table4571
+ GCC_except_table4584
+ GCC_except_table4588
+ GCC_except_table4595
+ GCC_except_table4604
+ GCC_except_table4609
+ GCC_except_table4629
+ GCC_except_table4634
+ GCC_except_table4639
+ GCC_except_table4646
+ GCC_except_table4655
+ GCC_except_table4656
+ GCC_except_table4662
+ GCC_except_table4667
+ GCC_except_table4674
+ GCC_except_table4683
+ GCC_except_table4687
+ GCC_except_table470
+ GCC_except_table4706
+ GCC_except_table471
+ GCC_except_table4710
+ GCC_except_table4740
+ GCC_except_table4742
+ GCC_except_table475
+ GCC_except_table4751
+ GCC_except_table4766
+ GCC_except_table4769
+ GCC_except_table4770
+ GCC_except_table4782
+ GCC_except_table4786
+ GCC_except_table4788
+ GCC_except_table4791
+ GCC_except_table4792
+ GCC_except_table4802
+ GCC_except_table4805
+ GCC_except_table4806
+ GCC_except_table4807
+ GCC_except_table4808
+ GCC_except_table481
+ GCC_except_table482
+ GCC_except_table4873
+ GCC_except_table4874
+ GCC_except_table4899
+ GCC_except_table4902
+ GCC_except_table4903
+ GCC_except_table4913
+ GCC_except_table4914
+ GCC_except_table4919
+ GCC_except_table500
+ GCC_except_table501
+ GCC_except_table5042
+ GCC_except_table5044
+ GCC_except_table5045
+ GCC_except_table5046
+ GCC_except_table5047
+ GCC_except_table5051
+ GCC_except_table5052
+ GCC_except_table5053
+ GCC_except_table5064
+ GCC_except_table5065
+ GCC_except_table5067
+ GCC_except_table5069
+ GCC_except_table5071
+ GCC_except_table5075
+ GCC_except_table5077
+ GCC_except_table5092
+ GCC_except_table5095
+ GCC_except_table5106
+ GCC_except_table5107
+ GCC_except_table5113
+ GCC_except_table5124
+ GCC_except_table5127
+ GCC_except_table513
+ GCC_except_table5135
+ GCC_except_table5136
+ GCC_except_table5137
+ GCC_except_table5139
+ GCC_except_table5140
+ GCC_except_table5143
+ GCC_except_table5144
+ GCC_except_table5149
+ GCC_except_table5150
+ GCC_except_table5154
+ GCC_except_table5163
+ GCC_except_table5164
+ GCC_except_table5169
+ GCC_except_table5184
+ GCC_except_table5187
+ GCC_except_table5194
+ GCC_except_table5196
+ GCC_except_table5201
+ GCC_except_table5202
+ GCC_except_table5207
+ GCC_except_table5210
+ GCC_except_table5212
+ GCC_except_table5214
+ GCC_except_table5216
+ GCC_except_table5219
+ GCC_except_table5223
+ GCC_except_table5228
+ GCC_except_table5229
+ GCC_except_table5231
+ GCC_except_table5237
+ GCC_except_table5239
+ GCC_except_table5241
+ GCC_except_table5242
+ GCC_except_table5243
+ GCC_except_table5245
+ GCC_except_table5251
+ GCC_except_table5254
+ GCC_except_table5257
+ GCC_except_table5258
+ GCC_except_table526
+ GCC_except_table5260
+ GCC_except_table5261
+ GCC_except_table5264
+ GCC_except_table5295
+ GCC_except_table5298
+ GCC_except_table5319
+ GCC_except_table532
+ GCC_except_table5321
+ GCC_except_table5324
+ GCC_except_table5325
+ GCC_except_table5326
+ GCC_except_table533
+ GCC_except_table5330
+ GCC_except_table5331
+ GCC_except_table5332
+ GCC_except_table5333
+ GCC_except_table5344
+ GCC_except_table5349
+ GCC_except_table5352
+ GCC_except_table5353
+ GCC_except_table5354
+ GCC_except_table5355
+ GCC_except_table5356
+ GCC_except_table5365
+ GCC_except_table5366
+ GCC_except_table5367
+ GCC_except_table5368
+ GCC_except_table5369
+ GCC_except_table5373
+ GCC_except_table5376
+ GCC_except_table5381
+ GCC_except_table5382
+ GCC_except_table5383
+ GCC_except_table5384
+ GCC_except_table5386
+ GCC_except_table5387
+ GCC_except_table5399
+ GCC_except_table5402
+ GCC_except_table542
+ GCC_except_table543
+ GCC_except_table545
+ GCC_except_table547
+ GCC_except_table548
+ GCC_except_table555
+ GCC_except_table559
+ GCC_except_table560
+ GCC_except_table561
+ GCC_except_table562
+ GCC_except_table563
+ GCC_except_table569
+ GCC_except_table576
+ GCC_except_table577
+ GCC_except_table58
+ GCC_except_table580
+ GCC_except_table583
+ GCC_except_table584
+ GCC_except_table590
+ GCC_except_table591
+ GCC_except_table592
+ GCC_except_table593
+ GCC_except_table594
+ GCC_except_table597
+ GCC_except_table598
+ GCC_except_table600
+ GCC_except_table604
+ GCC_except_table622
+ GCC_except_table628
+ GCC_except_table629
+ GCC_except_table630
+ GCC_except_table6310
+ GCC_except_table6311
+ GCC_except_table6312
+ GCC_except_table632
+ GCC_except_table6337
+ GCC_except_table6338
+ GCC_except_table6339
+ GCC_except_table6345
+ GCC_except_table6346
+ GCC_except_table635
+ GCC_except_table6350
+ GCC_except_table6352
+ GCC_except_table6354
+ GCC_except_table6360
+ GCC_except_table6366
+ GCC_except_table6368
+ GCC_except_table6370
+ GCC_except_table6372
+ GCC_except_table6374
+ GCC_except_table6380
+ GCC_except_table6392
+ GCC_except_table6396
+ GCC_except_table6457
+ GCC_except_table6472
+ GCC_except_table6477
+ GCC_except_table6478
+ GCC_except_table6479
+ GCC_except_table6480
+ GCC_except_table6485
+ GCC_except_table6487
+ GCC_except_table6497
+ GCC_except_table6500
+ GCC_except_table6504
+ GCC_except_table6506
+ GCC_except_table6507
+ GCC_except_table6508
+ GCC_except_table6509
+ GCC_except_table6510
+ GCC_except_table6512
+ GCC_except_table6533
+ GCC_except_table6539
+ GCC_except_table6555
+ GCC_except_table6556
+ GCC_except_table656
+ GCC_except_table657
+ GCC_except_table658
+ GCC_except_table6581
+ GCC_except_table6589
+ GCC_except_table659
+ GCC_except_table6594
+ GCC_except_table6597
+ GCC_except_table660
+ GCC_except_table6602
+ GCC_except_table6603
+ GCC_except_table6604
+ GCC_except_table6607
+ GCC_except_table6608
+ GCC_except_table6609
+ GCC_except_table661
+ GCC_except_table6612
+ GCC_except_table6614
+ GCC_except_table6617
+ GCC_except_table6642
+ GCC_except_table6652
+ GCC_except_table6654
+ GCC_except_table6662
+ GCC_except_table6663
+ GCC_except_table6665
+ GCC_except_table667
+ GCC_except_table6670
+ GCC_except_table6671
+ GCC_except_table6679
+ GCC_except_table668
+ GCC_except_table6686
+ GCC_except_table669
+ GCC_except_table6696
+ GCC_except_table670
+ GCC_except_table6700
+ GCC_except_table6709
+ GCC_except_table6711
+ GCC_except_table672
+ GCC_except_table6721
+ GCC_except_table6723
+ GCC_except_table6727
+ GCC_except_table6728
+ GCC_except_table6729
+ GCC_except_table6741
+ GCC_except_table6744
+ GCC_except_table6745
+ GCC_except_table6747
+ GCC_except_table6748
+ GCC_except_table6753
+ GCC_except_table6755
+ GCC_except_table6757
+ GCC_except_table6759
+ GCC_except_table6763
+ GCC_except_table6765
+ GCC_except_table6770
+ GCC_except_table6772
+ GCC_except_table6773
+ GCC_except_table6777
+ GCC_except_table6785
+ GCC_except_table6788
+ GCC_except_table6789
+ GCC_except_table6791
+ GCC_except_table6796
+ GCC_except_table6798
+ GCC_except_table6799
+ GCC_except_table68
+ GCC_except_table6801
+ GCC_except_table6809
+ GCC_except_table6811
+ GCC_except_table6812
+ GCC_except_table6832
+ GCC_except_table6834
+ GCC_except_table6838
+ GCC_except_table6839
+ GCC_except_table6840
+ GCC_except_table6841
+ GCC_except_table6842
+ GCC_except_table6843
+ GCC_except_table6846
+ GCC_except_table6848
+ GCC_except_table6851
+ GCC_except_table6865
+ GCC_except_table6875
+ GCC_except_table6896
+ GCC_except_table6897
+ GCC_except_table6899
+ GCC_except_table69
+ GCC_except_table692
+ GCC_except_table693
+ GCC_except_table6938
+ GCC_except_table694
+ GCC_except_table695
+ GCC_except_table6955
+ GCC_except_table6966
+ GCC_except_table6969
+ GCC_except_table697
+ GCC_except_table6970
+ GCC_except_table6977
+ GCC_except_table698
+ GCC_except_table6984
+ GCC_except_table6993
+ GCC_except_table6995
+ GCC_except_table6996
+ GCC_except_table6997
+ GCC_except_table6998
+ GCC_except_table6999
+ GCC_except_table7
+ GCC_except_table700
+ GCC_except_table7000
+ GCC_except_table701
+ GCC_except_table7011
+ GCC_except_table7012
+ GCC_except_table7021
+ GCC_except_table7024
+ GCC_except_table704
+ GCC_except_table707
+ GCC_except_table7070
+ GCC_except_table7073
+ GCC_except_table7074
+ GCC_except_table7075
+ GCC_except_table7076
+ GCC_except_table7079
+ GCC_except_table7081
+ GCC_except_table7085
+ GCC_except_table7087
+ GCC_except_table7105
+ GCC_except_table7108
+ GCC_except_table7124
+ GCC_except_table7127
+ GCC_except_table7130
+ GCC_except_table7132
+ GCC_except_table7137
+ GCC_except_table7168
+ GCC_except_table7170
+ GCC_except_table718
+ GCC_except_table7182
+ GCC_except_table7194
+ GCC_except_table7195
+ GCC_except_table7198
+ GCC_except_table7199
+ GCC_except_table72
+ GCC_except_table7200
+ GCC_except_table7201
+ GCC_except_table7202
+ GCC_except_table7211
+ GCC_except_table722
+ GCC_except_table7229
+ GCC_except_table7230
+ GCC_except_table7231
+ GCC_except_table7232
+ GCC_except_table7234
+ GCC_except_table724
+ GCC_except_table7243
+ GCC_except_table725
+ GCC_except_table7260
+ GCC_except_table7261
+ GCC_except_table7265
+ GCC_except_table727
+ GCC_except_table7279
+ GCC_except_table7284
+ GCC_except_table7286
+ GCC_except_table729
+ GCC_except_table730
+ GCC_except_table731
+ GCC_except_table732
+ GCC_except_table733
+ GCC_except_table7330
+ GCC_except_table7334
+ GCC_except_table7337
+ GCC_except_table7340
+ GCC_except_table735
+ GCC_except_table7356
+ GCC_except_table7357
+ GCC_except_table7358
+ GCC_except_table7362
+ GCC_except_table7368
+ GCC_except_table7370
+ GCC_except_table738
+ GCC_except_table740
+ GCC_except_table7401
+ GCC_except_table7415
+ GCC_except_table742
+ GCC_except_table7474
+ GCC_except_table7475
+ GCC_except_table7483
+ GCC_except_table7487
+ GCC_except_table7489
+ GCC_except_table7522
+ GCC_except_table7528
+ GCC_except_table7529
+ GCC_except_table7530
+ GCC_except_table7535
+ GCC_except_table7538
+ GCC_except_table7539
+ GCC_except_table7542
+ GCC_except_table7552
+ GCC_except_table7553
+ GCC_except_table7554
+ GCC_except_table7556
+ GCC_except_table7557
+ GCC_except_table7567
+ GCC_except_table7573
+ GCC_except_table7574
+ GCC_except_table7575
+ GCC_except_table7576
+ GCC_except_table758
+ GCC_except_table7580
+ GCC_except_table7582
+ GCC_except_table7599
+ GCC_except_table7602
+ GCC_except_table7603
+ GCC_except_table7606
+ GCC_except_table7609
+ GCC_except_table7612
+ GCC_except_table7614
+ GCC_except_table7616
+ GCC_except_table7624
+ GCC_except_table7625
+ GCC_except_table7631
+ GCC_except_table7633
+ GCC_except_table7634
+ GCC_except_table7641
+ GCC_except_table7647
+ GCC_except_table7649
+ GCC_except_table7656
+ GCC_except_table766
+ GCC_except_table7662
+ GCC_except_table7663
+ GCC_except_table7665
+ GCC_except_table7676
+ GCC_except_table7685
+ GCC_except_table7688
+ GCC_except_table7691
+ GCC_except_table7697
+ GCC_except_table7699
+ GCC_except_table770
+ GCC_except_table7719
+ GCC_except_table773
+ GCC_except_table7733
+ GCC_except_table7735
+ GCC_except_table7740
+ GCC_except_table7742
+ GCC_except_table7745
+ GCC_except_table7748
+ GCC_except_table7751
+ GCC_except_table7781
+ GCC_except_table7789
+ GCC_except_table7798
+ GCC_except_table7800
+ GCC_except_table7815
+ GCC_except_table7818
+ GCC_except_table7822
+ GCC_except_table7824
+ GCC_except_table7845
+ GCC_except_table7857
+ GCC_except_table7882
+ GCC_except_table7883
+ GCC_except_table7884
+ GCC_except_table7886
+ GCC_except_table7897
+ GCC_except_table7898
+ GCC_except_table790
+ GCC_except_table7902
+ GCC_except_table7904
+ GCC_except_table7908
+ GCC_except_table7910
+ GCC_except_table7911
+ GCC_except_table7913
+ GCC_except_table7922
+ GCC_except_table7923
+ GCC_except_table7925
+ GCC_except_table7935
+ GCC_except_table7937
+ GCC_except_table7948
+ GCC_except_table7952
+ GCC_except_table7954
+ GCC_except_table7960
+ GCC_except_table7962
+ GCC_except_table7973
+ GCC_except_table7976
+ GCC_except_table7977
+ GCC_except_table7981
+ GCC_except_table7983
+ GCC_except_table7985
+ GCC_except_table7989
+ GCC_except_table7990
+ GCC_except_table7995
+ GCC_except_table7997
+ GCC_except_table7998
+ GCC_except_table8000
+ GCC_except_table8004
+ GCC_except_table8006
+ GCC_except_table8010
+ GCC_except_table8011
+ GCC_except_table8013
+ GCC_except_table8015
+ GCC_except_table8025
+ GCC_except_table8043
+ GCC_except_table805
+ GCC_except_table8050
+ GCC_except_table8051
+ GCC_except_table806
+ GCC_except_table8069
+ GCC_except_table8076
+ GCC_except_table8078
+ GCC_except_table808
+ GCC_except_table8088
+ GCC_except_table8089
+ GCC_except_table809
+ GCC_except_table8090
+ GCC_except_table8094
+ GCC_except_table8095
+ GCC_except_table8097
+ GCC_except_table8098
+ GCC_except_table8100
+ GCC_except_table8102
+ GCC_except_table8103
+ GCC_except_table8108
+ GCC_except_table8109
+ GCC_except_table8110
+ GCC_except_table8111
+ GCC_except_table812
+ GCC_except_table8120
+ GCC_except_table8122
+ GCC_except_table8127
+ GCC_except_table8129
+ GCC_except_table8137
+ GCC_except_table8143
+ GCC_except_table8145
+ GCC_except_table8147
+ GCC_except_table8149
+ GCC_except_table815
+ GCC_except_table8156
+ GCC_except_table8157
+ GCC_except_table8165
+ GCC_except_table8184
+ GCC_except_table8185
+ GCC_except_table8186
+ GCC_except_table8188
+ GCC_except_table8189
+ GCC_except_table8190
+ GCC_except_table8195
+ GCC_except_table82
+ GCC_except_table8200
+ GCC_except_table8216
+ GCC_except_table8221
+ GCC_except_table8224
+ GCC_except_table8225
+ GCC_except_table8234
+ GCC_except_table8235
+ GCC_except_table8236
+ GCC_except_table8237
+ GCC_except_table8241
+ GCC_except_table8242
+ GCC_except_table8257
+ GCC_except_table8258
+ GCC_except_table8259
+ GCC_except_table8260
+ GCC_except_table8261
+ GCC_except_table8266
+ GCC_except_table8267
+ GCC_except_table8268
+ GCC_except_table8278
+ GCC_except_table8292
+ GCC_except_table8293
+ GCC_except_table8294
+ GCC_except_table8299
+ GCC_except_table83
+ GCC_except_table8302
+ GCC_except_table8303
+ GCC_except_table8308
+ GCC_except_table8310
+ GCC_except_table8311
+ GCC_except_table8312
+ GCC_except_table8315
+ GCC_except_table8317
+ GCC_except_table8319
+ GCC_except_table8321
+ GCC_except_table8322
+ GCC_except_table8323
+ GCC_except_table8331
+ GCC_except_table8337
+ GCC_except_table8358
+ GCC_except_table8361
+ GCC_except_table8362
+ GCC_except_table8363
+ GCC_except_table8365
+ GCC_except_table8366
+ GCC_except_table8367
+ GCC_except_table8369
+ GCC_except_table8378
+ GCC_except_table839
+ GCC_except_table8397
+ GCC_except_table8400
+ GCC_except_table8403
+ GCC_except_table8405
+ GCC_except_table8406
+ GCC_except_table8407
+ GCC_except_table8414
+ GCC_except_table8417
+ GCC_except_table8421
+ GCC_except_table8436
+ GCC_except_table8437
+ GCC_except_table8438
+ GCC_except_table844
+ GCC_except_table845
+ GCC_except_table8460
+ GCC_except_table8461
+ GCC_except_table8462
+ GCC_except_table8465
+ GCC_except_table847
+ GCC_except_table848
+ GCC_except_table8490
+ GCC_except_table851
+ GCC_except_table853
+ GCC_except_table8532
+ GCC_except_table8533
+ GCC_except_table8549
+ GCC_except_table8556
+ GCC_except_table8557
+ GCC_except_table8558
+ GCC_except_table8590
+ GCC_except_table8591
+ GCC_except_table8592
+ GCC_except_table8595
+ GCC_except_table8597
+ GCC_except_table8598
+ GCC_except_table8601
+ GCC_except_table8616
+ GCC_except_table8624
+ GCC_except_table8625
+ GCC_except_table8629
+ GCC_except_table863
+ GCC_except_table8630
+ GCC_except_table8638
+ GCC_except_table8640
+ GCC_except_table8641
+ GCC_except_table8642
+ GCC_except_table8646
+ GCC_except_table8647
+ GCC_except_table8648
+ GCC_except_table8649
+ GCC_except_table865
+ GCC_except_table8651
+ GCC_except_table8653
+ GCC_except_table866
+ GCC_except_table8670
+ GCC_except_table8671
+ GCC_except_table8672
+ GCC_except_table8673
+ GCC_except_table8675
+ GCC_except_table8676
+ GCC_except_table8683
+ GCC_except_table8686
+ GCC_except_table8687
+ GCC_except_table8688
+ GCC_except_table8691
+ GCC_except_table8692
+ GCC_except_table8693
+ GCC_except_table8694
+ GCC_except_table8701
+ GCC_except_table8702
+ GCC_except_table8703
+ GCC_except_table8704
+ GCC_except_table8705
+ GCC_except_table8709
+ GCC_except_table8712
+ GCC_except_table8714
+ GCC_except_table8717
+ GCC_except_table8753
+ GCC_except_table8758
+ GCC_except_table8759
+ GCC_except_table876
+ GCC_except_table8774
+ GCC_except_table8784
+ GCC_except_table8785
+ GCC_except_table8793
+ GCC_except_table8795
+ GCC_except_table8799
+ GCC_except_table88
+ GCC_except_table8805
+ GCC_except_table8808
+ GCC_except_table8810
+ GCC_except_table882
+ GCC_except_table8826
+ GCC_except_table8827
+ GCC_except_table8837
+ GCC_except_table8838
+ GCC_except_table8839
+ GCC_except_table8841
+ GCC_except_table8842
+ GCC_except_table8843
+ GCC_except_table8844
+ GCC_except_table8845
+ GCC_except_table8846
+ GCC_except_table8847
+ GCC_except_table8848
+ GCC_except_table8851
+ GCC_except_table8852
+ GCC_except_table8860
+ GCC_except_table8876
+ GCC_except_table888
+ GCC_except_table8884
+ GCC_except_table8892
+ GCC_except_table89
+ GCC_except_table8900
+ GCC_except_table891
+ GCC_except_table8916
+ GCC_except_table892
+ GCC_except_table8925
+ GCC_except_table894
+ GCC_except_table8942
+ GCC_except_table8943
+ GCC_except_table8944
+ GCC_except_table8945
+ GCC_except_table8946
+ GCC_except_table8948
+ GCC_except_table8949
+ GCC_except_table896
+ GCC_except_table8962
+ GCC_except_table8972
+ GCC_except_table8974
+ GCC_except_table8980
+ GCC_except_table8984
+ GCC_except_table8986
+ GCC_except_table8991
+ GCC_except_table8992
+ GCC_except_table8993
+ GCC_except_table8994
+ GCC_except_table8995
+ GCC_except_table8996
+ GCC_except_table8997
+ GCC_except_table8998
+ GCC_except_table90
+ GCC_except_table9000
+ GCC_except_table9001
+ GCC_except_table9002
+ GCC_except_table9005
+ GCC_except_table9006
+ GCC_except_table9007
+ GCC_except_table9008
+ GCC_except_table9009
+ GCC_except_table9010
+ GCC_except_table9011
+ GCC_except_table9012
+ GCC_except_table9013
+ GCC_except_table9014
+ GCC_except_table9015
+ GCC_except_table9016
+ GCC_except_table9017
+ GCC_except_table902
+ GCC_except_table9021
+ GCC_except_table9039
+ GCC_except_table904
+ GCC_except_table9041
+ GCC_except_table9043
+ GCC_except_table9044
+ GCC_except_table9047
+ GCC_except_table9049
+ GCC_except_table9051
+ GCC_except_table9054
+ GCC_except_table9059
+ GCC_except_table9070
+ GCC_except_table908
+ GCC_except_table9090
+ GCC_except_table91
+ GCC_except_table914
+ GCC_except_table9179
+ GCC_except_table9182
+ GCC_except_table92
+ GCC_except_table9207
+ GCC_except_table9208
+ GCC_except_table922
+ GCC_except_table9228
+ GCC_except_table9236
+ GCC_except_table9249
+ GCC_except_table9255
+ GCC_except_table9262
+ GCC_except_table9263
+ GCC_except_table9267
+ GCC_except_table9269
+ GCC_except_table9270
+ GCC_except_table9287
+ GCC_except_table9288
+ GCC_except_table9289
+ GCC_except_table9290
+ GCC_except_table93
+ GCC_except_table9300
+ GCC_except_table9307
+ GCC_except_table9308
+ GCC_except_table9355
+ GCC_except_table9364
+ GCC_except_table9372
+ GCC_except_table9373
+ GCC_except_table9374
+ GCC_except_table9375
+ GCC_except_table9376
+ GCC_except_table9377
+ GCC_except_table9379
+ GCC_except_table9380
+ GCC_except_table9382
+ GCC_except_table9383
+ GCC_except_table9384
+ GCC_except_table9385
+ GCC_except_table9387
+ GCC_except_table9391
+ GCC_except_table940
+ GCC_except_table9401
+ GCC_except_table9404
+ GCC_except_table941
+ GCC_except_table9414
+ GCC_except_table9415
+ GCC_except_table9421
+ GCC_except_table9424
+ GCC_except_table9435
+ GCC_except_table9437
+ GCC_except_table9438
+ GCC_except_table9442
+ GCC_except_table9443
+ GCC_except_table9444
+ GCC_except_table9445
+ GCC_except_table9447
+ GCC_except_table9449
+ GCC_except_table945
+ GCC_except_table9452
+ GCC_except_table9457
+ GCC_except_table9460
+ GCC_except_table9461
+ GCC_except_table9468
+ GCC_except_table9475
+ GCC_except_table9478
+ GCC_except_table9479
+ GCC_except_table9481
+ GCC_except_table9482
+ GCC_except_table9484
+ GCC_except_table9486
+ GCC_except_table9488
+ GCC_except_table9490
+ GCC_except_table9491
+ GCC_except_table9493
+ GCC_except_table9495
+ GCC_except_table9497
+ GCC_except_table95
+ GCC_except_table9503
+ GCC_except_table9513
+ GCC_except_table9522
+ GCC_except_table9524
+ GCC_except_table9532
+ GCC_except_table9533
+ GCC_except_table9534
+ GCC_except_table9535
+ GCC_except_table9537
+ GCC_except_table9544
+ GCC_except_table9556
+ GCC_except_table9558
+ GCC_except_table9560
+ GCC_except_table9562
+ GCC_except_table9564
+ GCC_except_table9566
+ GCC_except_table9568
+ GCC_except_table9572
+ GCC_except_table9574
+ GCC_except_table9576
+ GCC_except_table9578
+ GCC_except_table9580
+ GCC_except_table9582
+ GCC_except_table9584
+ GCC_except_table959
+ GCC_except_table9590
+ GCC_except_table9594
+ GCC_except_table9598
+ GCC_except_table9600
+ GCC_except_table9602
+ GCC_except_table961
+ GCC_except_table9610
+ GCC_except_table9613
+ GCC_except_table9621
+ GCC_except_table9628
+ GCC_except_table9636
+ GCC_except_table9637
+ GCC_except_table9638
+ GCC_except_table964
+ GCC_except_table9640
+ GCC_except_table9641
+ GCC_except_table9642
+ GCC_except_table9643
+ GCC_except_table9644
+ GCC_except_table9645
+ GCC_except_table9646
+ GCC_except_table9659
+ GCC_except_table9660
+ GCC_except_table9675
+ GCC_except_table9676
+ GCC_except_table9677
+ GCC_except_table968
+ GCC_except_table969
+ GCC_except_table9691
+ GCC_except_table9693
+ GCC_except_table9694
+ GCC_except_table9698
+ GCC_except_table9702
+ GCC_except_table9704
+ GCC_except_table9705
+ GCC_except_table971
+ GCC_except_table9721
+ GCC_except_table9723
+ GCC_except_table9724
+ GCC_except_table9726
+ GCC_except_table973
+ GCC_except_table9735
+ GCC_except_table9736
+ GCC_except_table9741
+ GCC_except_table9742
+ GCC_except_table9744
+ GCC_except_table9745
+ GCC_except_table975
+ GCC_except_table9774
+ GCC_except_table9777
+ GCC_except_table9791
+ GCC_except_table9797
+ GCC_except_table9799
+ GCC_except_table9804
+ GCC_except_table9820
+ GCC_except_table9830
+ GCC_except_table9831
+ GCC_except_table9832
+ GCC_except_table9838
+ GCC_except_table9840
+ GCC_except_table9841
+ GCC_except_table9848
+ GCC_except_table9850
+ GCC_except_table9863
+ GCC_except_table9864
+ GCC_except_table9867
+ GCC_except_table9869
+ GCC_except_table9871
+ GCC_except_table9872
+ GCC_except_table9873
+ GCC_except_table9874
+ GCC_except_table9890
+ GCC_except_table9895
+ GCC_except_table9897
+ GCC_except_table9899
+ GCC_except_table9902
+ GCC_except_table9903
+ GCC_except_table9906
+ GCC_except_table9907
+ GCC_except_table9908
+ GCC_except_table9909
+ GCC_except_table9910
+ GCC_except_table9911
+ GCC_except_table9913
+ GCC_except_table9914
+ GCC_except_table9915
+ GCC_except_table9916
+ GCC_except_table9917
+ GCC_except_table9918
+ GCC_except_table9920
+ GCC_except_table9924
+ GCC_except_table9927
+ GCC_except_table9929
+ GCC_except_table9931
+ GCC_except_table9933
+ GCC_except_table9936
+ GCC_except_table9938
+ GCC_except_table9940
+ GCC_except_table9942
+ GCC_except_table9943
+ GCC_except_table9944
+ GCC_except_table9945
+ GCC_except_table9946
+ GCC_except_table9948
+ GCC_except_table9950
+ GCC_except_table9951
+ GCC_except_table9952
+ GCC_except_table9953
+ GCC_except_table9954
+ GCC_except_table9955
+ GCC_except_table9956
+ GCC_except_table9958
+ GCC_except_table9960
+ GCC_except_table9962
+ GCC_except_table9964
+ GCC_except_table9965
+ GCC_except_table9967
+ GCC_except_table9969
+ GCC_except_table9970
+ GCC_except_table9971
+ GCC_except_table9972
+ GCC_except_table9973
+ GCC_except_table9974
+ GCC_except_table9975
+ GCC_except_table9980
+ GCC_except_table9982
+ GCC_except_table9984
+ GCC_except_table9985
+ GCC_except_table9987
+ GCC_except_table9989
+ GCC_except_table9991
+ GCC_except_table9993
+ GCC_except_table9995
+ GCC_except_table9997
+ GCC_except_table9999
+ _AudioFileReadPacketData
+ _AudioQueueStartWithInterval
+ _CFArrayAppendValue
+ _CFDataAppendBytes
+ _CFDataCreateMutableCopy
+ _CFDataGetMutableBytePtr
+ _CFDataIncreaseLength
+ _CFDataReplaceBytes
+ _CFMachPortCreate
+ _CFMachPortGetPort
+ _CFNotificationCenterRemoveObserver
+ _CFStringCreateWithCharacters
+ _CFStringGetCharacters
+ _CFURLCreateWithString
+ _OBJC_CLASS_$_ATATranslatorClientDelegate
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_STTranslatorClientDelegate
+ _OBJC_IVAR_$_ATATranslatorClientDelegate.mImpl
+ _OBJC_IVAR_$_ATATranslatorClientDelegate.mScope
+ _OBJC_IVAR_$_AVHapticServer._hapticAudioMetrics
+ _OBJC_IVAR_$_AVHapticServer._hapticMetrics
+ _OBJC_IVAR_$_AVHapticServer._processIndexMutex
+ _OBJC_IVAR_$_AVHapticServerInstance._currentRoute
+ _OBJC_IVAR_$_AVHapticServerInstance._server
+ _OBJC_IVAR_$_STTranslatorClientDelegate.mImpl
+ _OBJC_IVAR_$_STTranslatorClientDelegate.mScope
+ _OBJC_METACLASS_$_ATATranslatorClientDelegate
+ _OBJC_METACLASS_$_STTranslatorClientDelegate
+ __OBJC_$_INSTANCE_METHODS_ATATranslatorClientDelegate
+ __OBJC_$_INSTANCE_METHODS_STTranslatorClientDelegate
+ __OBJC_$_INSTANCE_VARIABLES_ATATranslatorClientDelegate
+ __OBJC_$_INSTANCE_VARIABLES_STTranslatorClientDelegate
+ __OBJC_$_PROP_LIST_ATATranslatorClientDelegate
+ __OBJC_$_PROP_LIST_STTranslatorClientDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ATATranslationClientDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_ATATranslationClientDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ATATranslationClientDelegate
+ __OBJC_$_PROTOCOL_REFS_ATATranslationClientDelegate
+ __OBJC_CLASS_PROTOCOLS_$_ATATranslatorClientDelegate
+ __OBJC_CLASS_PROTOCOLS_$_STTranslatorClientDelegate
+ __OBJC_CLASS_RO_$_ATATranslatorClientDelegate
+ __OBJC_CLASS_RO_$_STTranslatorClientDelegate
+ __OBJC_LABEL_PROTOCOL_$_ATATranslationClientDelegate
+ __OBJC_METACLASS_RO_$_ATATranslatorClientDelegate
+ __OBJC_METACLASS_RO_$_STTranslatorClientDelegate
+ __OBJC_PROTOCOL_$_ATATranslationClientDelegate
+ __Z15MakeCAExceptioni
+ __Z18ParameterFormatterjPKjPKf
+ __Z19CAObjectDescriptionPv
+ __Z21IsPassthroughIOFormatj
+ __Z23gOfflineFOAProcessorLogv
+ __Z27AudioQueueInternalStop_Syncjb
+ __Z37SystemSoundServerKillSoundsForAllPIDsb
+ __Z9to_stringPK14AudioTimeStampj
+ __Z9to_stringPK18AudioChannelLayout
+ __Z9to_stringPKfmm
+ __Z9to_stringRK21AudioClassDescription
+ __Z9to_stringRK25AudioComponentDescription
+ __Z9to_stringRK26AudioObjectPropertyAddress
+ __ZGVZ23gOfflineFOAProcessorLogvE6global
+ __ZGVZ41isAudioTranscriptionAnalysisServerEnabledvE7enabled
+ __ZGVZL13GetAcousticIDvE13optionalValue.5590
+ __ZGVZL22sOrchestratorServerLogvE4sLog
+ __ZGVZN21PlatformUtilities_iOS19ProductIsMuseDeviceEvE12isMuseDevice
+ __ZGVZN5caulk13random_uint64EvE6engine
+ __ZL11CPMSLibraryv.10490
+ __ZL11CPMSLibraryv.3784
+ __ZL11debugSerial
+ __ZL12LogMachErrorPKci
+ __ZL12kStateLabels
+ __ZL13LogPosixErrorPKc
+ __ZL16audit_stringCPMS.10505
+ __ZL16audit_stringCPMS.3801
+ __ZL16audit_stringCPMS.6668
+ __ZL18kTFileBSDSubsystem
+ __ZL19AudioCaptureLibraryv
+ __ZL20CoreMediaLibraryCorePPc.7402
+ __ZL20audit_stringAVFAudio.12867
+ __ZL21audit_stringCoreMedia.5289
+ __ZL21audit_stringCoreMedia.7411
+ __ZL22sOrchestratorServerLogv
+ __ZL23AudioCaptureLibraryCorePPc
+ __ZL23MediaToolboxLibraryCorePPc.7392
+ __ZL24audit_stringAudioCapture
+ __ZL24audit_stringMediaToolbox.7401
+ __ZL28getRBSProcessIdentifierClassv
+ __ZL30SynthOutputNotificationHandlerP22__CFNotificationCenterPvPK10__CFStringPKvPK14__CFDictionary
+ __ZL30audit_stringAudioSessionServer.8659
+ __ZL31SynthOutputNotificationCallbackP22__CFNotificationCenterPvPK10__CFStringPKvPK14__CFDictionary
+ __ZL33CoreAudioOrchestrationLibraryCorePPc
+ __ZL33getCMBaseObjectGetVTableSymbolLocv.7403
+ __ZL34audit_stringCoreAudioOrchestration
+ __ZL35gDeviceSupportsHALSpeakerProtection
+ __ZL38audit_stringAudioTranscriptionAnalysis
+ __ZL39soft_AudioCapturerCreateForPCMAudioData19AudioCaptureOptionsPKcS1_jS1_PK27AudioStreamBasicDescriptionS4_
+ __ZL43soft_AudioCapturerCreateForEncodedAudioData19AudioCaptureOptionsPKcS1_jS1_PK27AudioStreamBasicDescriptionS4_PKvj
+ __ZL46getCreatePasscodeDetectorClientPortalSymbolLocv
+ __ZL58getFigCPECryptorCreateCryptorFromSerializedRecipeSymbolLocv.7393
+ __ZN10AQMEDevice25IO_DeviceStoppedFromBelowEbb
+ __ZN10AQMEIO_DSP25IO_DeviceStoppedFromBelowEbb
+ __ZN10AQMEIO_DSP31routeRequires3PBinauralRendererER25AudioComponentDescriptionRN10applesauce2CF9StringRefE
+ __ZN10AQMEIO_HAL24HandleRunningStateChangeEb
+ __ZN10AQMEIO_HAL31routeRequires3PBinauralRendererER25AudioComponentDescriptionRN10applesauce2CF9StringRefE
+ __ZN10CACFStringaSEPK10__CFString
+ __ZN10ClientInfo9AddPlayerEP19SSSActionPlayerBase
+ __ZN10PowerMeter19ScaleDecayConstantsEi
+ __ZN10PowerMeter9SavePeaksEiii
+ __ZN10XPC_ObjectD0Ev
+ __ZN10XPC_ObjectD1Ev
+ __ZN10applesauce2CF10convert_asINSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEELi0EEENS2_8optionalIT_EEPK10__CFString
+ __ZN10applesauce2CF7details12pretty_printEPK14__CFDictionary
+ __ZN10applesauce4raii2v16detail10ScopeGuardIZZN14DSP_Routing_VP28SetCallTranslationPropertiesEPK14__CFDictionaryRbEUb_E4$_12NS2_15StackExitPolicyEED1Ev
+ __ZN11AQAC3IONode25IO_DeviceStoppedFromBelowEbb
+ __ZN11AQMEIO_Base31routeRequires3PBinauralRendererER25AudioComponentDescriptionRN10applesauce2CF9StringRefE
+ __ZN11AQTapIONode25IO_DeviceStoppedFromBelowEbb
+ __ZN11CACFBooleanD2Ev
+ __ZN11ClientEntry19doForSequenceWithIDEmN5caulk15rt_function_refIFvRKNSt3__110shared_ptrI14HapticSequenceEEEEE
+ __ZN11ClientEntry20releaseSynthChannelsINSt3__19allocatorIjEEEEiRKNS1_6vectorIjT_EE
+ __ZN11ClientEntry21prepareSequenceWithIDEmN5caulk16inplace_functionIFvmELm32ELm8ENS0_23inplace_function_detail6vtableEEE
+ __ZN11ClientEntry22handleSequenceFinishedEm
+ __ZN11ClientEntry5flushEd
+ __ZN11ClientEntryC2Em13audit_token_tP13ServerManagerNS_5StateEj20HapticPlayerPriorityb
+ __ZN11HapticSynth15releaseChannelsINSt3__19allocatorIjEEEEiRKNS1_6vectorIjT_EE
+ __ZN11HapticSynth18setSynthRenderProcEPvN5caulk15rt_function_refIFvS0_RK14AudioTimeStampjEEE
+ __ZN11HapticSynth40handleSystemSoundsAndHapticsVolumeChangeEf
+ __ZN11MetricsBase11prewarmTimeEv
+ __ZN11MetricsBase12markEngineOnEv
+ __ZN11MetricsBase13markEngineOffEi
+ __ZN11MetricsBase18fileAutoBugCaptureEP8NSStringP12NSDictionary
+ __ZN11MetricsBase19markEnginePrewarmOnEv
+ __ZN11MetricsBase20markEnginePrewarmOffEv
+ __ZN11MetricsBase20sAutoBugCaptureTimerE
+ __ZN11MetricsBase20sAutoBugCaptureTokenE
+ __ZN11MetricsBase24sAutoBugCaptureAvailableE.0
+ __ZN11MetricsBase25logPowerLogForceStopEventE25HapticServerStoppedReasonim
+ __ZN11MetricsBase26logPowerLogOnDurationEventEiff
+ __ZN11MetricsBase27handleReporterEngineOnEventEv
+ __ZN11MetricsBase28handleReporterEngineOffEventEd
+ __ZN11MetricsBase6onTimeEv
+ __ZN11MetricsBase9sReporterE
+ __ZN11MetricsBaseC2Ev
+ __ZN11MetricsBaseD0Ev
+ __ZN11MetricsBaseD1Ev
+ __ZN11MuteManager15HapticMuteCount7setMuteENS_16HapticMuteReasonEb
+ __ZN11SynthOutput29IONode_DeviceStoppedFromBelowEb
+ __ZN11SynthOutput9SetVolumeEf
+ __ZN12CADeprecated10CAAutoFreeIcE10allocBytesEmb
+ __ZN12CADeprecated11XMachServerD0Ev
+ __ZN12CADeprecated11XMachServerD1Ev
+ __ZN12CADeprecated16XMachReceivePort11SetMachPortEj
+ __ZN12CADeprecated17XMachPortServicer12DispatchImplD0Ev
+ __ZN12CADeprecated17XMachPortServicer12DispatchImplD1Ev
+ __ZN12CADeprecated17XMachPortServicer12DispatchImplD2Ev
+ __ZN12CADeprecated17XMachPortServicer17SetQueueAndSourceERKN10applesauce8dispatch2v15queueERKNS3_6sourceE
+ __ZN12CADeprecated22XMachPortDeathListener18GetPortDeathCFPortEv
+ __ZN12CADeprecated22XMachPortDeathListener21PortDeathListenerProcEP12__CFMachPortPvlS3_
+ __ZN12CADeprecated22XMachPortDeathListener24DispatchPortDeathMessageEPK29mach_dead_name_notification_t
+ __ZN12CADeprecated22XMachPortDeathListenerD0Ev
+ __ZN12CADeprecated22XMachPortDeathListenerD1Ev
+ __ZN12CADeprecated7CAGuardD0Ev
+ __ZN12CADeprecated7CAMutexC2EPKc
+ __ZN12CADeprecated7CAMutexD0Ev
+ __ZN12CADeprecated7CAMutexD2Ev
+ __ZN12CADeprecated9CAPThread5EntryEPv
+ __ZN12CADeprecated9CAPThreadD0Ev
+ __ZN12CADeprecated9CAPThreadD1Ev
+ __ZN12CASerializer14PrepareToWriteEj
+ __ZN12CAXExceptionD0Ev
+ __ZN12MemoryStream11GetPositionEv
+ __ZN12MemoryStream4ReadEPvm
+ __ZN12MemoryStream4SeekEx
+ __ZN12MemoryStream4SkipEx
+ __ZN12MemoryStream5WriteEPvm
+ __ZN12MemoryStreamD0Ev
+ __ZN12MemoryStreamD2Ev
+ __ZN12SequenceImpl17sendEventInternalIN11SequenceFSM13EnableLoopingEEEvRKT_
+ __ZN12SequenceImpl21setRTFinishedCallbackEN5caulk16inplace_functionIFvmELm32ELm8ENS0_23inplace_function_detail9rt_vtableEEE
+ __ZN12SequenceImpl32initializeRealtimeTrackIteratorsEv
+ __ZN13AQMETapInsert10ResetStateEb
+ __ZN13AudioTapMixer17renderCurrentPushEP9TapSourcePvRK14AudioTimeStampjRK15AudioBufferListjRS6_
+ __ZN13AudioTapMixer18renderToRingBufferEP9TapSourceRK14AudioTimeStampjRK15AudioBufferList
+ __ZN13AudioTapMixer23fetchRingBuffersIntoMixEjR15AudioBufferList
+ __ZN13AudioTapMixer24sendMixAndMarkEndOfCycleERK14AudioTimeStampjR15AudioBufferList
+ __ZN13HapticMetrics21logPowerLogCountEventE22PowerLogCountEventTypemimP8NSString
+ __ZN13HapticMetrics25logPowerLogForceStopEventE25HapticServerStoppedReasonim
+ __ZN13HapticMetrics26logPowerLogOnDurationEventEiff
+ __ZN13HapticMetrics27handleReporterEngineOnEventEv
+ __ZN13HapticMetrics28handleReporterEngineOffEventEd
+ __ZN13HapticMetricsD0Ev
+ __ZN13HapticMetricsD2Ev
+ __ZN13QueueAccessorD2Ev
+ __ZN13ServerManager12stopSequenceERKNSt3__110shared_ptrI11ClientEntryEEmi
+ __ZN13ServerManager25handleRouteChangeForEntryENSt3__110shared_ptrI11ClientEntryEEP8NSStringNS0_8optionalIbEE
+ __ZN13TrackIterator12SetEventTimeEd
+ __ZN14AQIONodeClient21GetOfflineFOAMetadataEv
+ __ZN14AQIONodeClient29IONode_DeviceStoppedFromBelowEb
+ __ZN14AudioUnitGraph12AddLiveEventERK22AUGraphLiveUpdateEvent
+ __ZN14CACFDictionaryaSEPK14__CFDictionary
+ __ZN14DSP_Routing_VP25IO_DeviceStoppedFromBelowEbb
+ __ZN14MEMixerChannel19MCAUProcessingBlockC2ER11MCAudioUnitPK10__CFStringRK25AudioComponentDescription
+ __ZN14MEMixerChannel27Configure3PBinauralRendererERK25AudioComponentDescription
+ __ZN14SSSClientEntry21prepareSequenceWithIDEmN5caulk16inplace_functionIFvmELm32ELm8ENS0_23inplace_function_detail6vtableEEE
+ __ZN14SSSClientEntry22handleSequenceFinishedEm
+ __ZN14XPC_Connection14ProcessMessageEPv
+ __ZN14XPC_ConnectionD0Ev
+ __ZN14XPC_ConnectionD1Ev
+ __ZN14XPC_ConnectionD2Ev
+ __ZN14XPC_DictionaryD0Ev
+ __ZN16AudioQueueObject19ScaleForRateChangesEx
+ __ZN16AudioQueueObject21GetOfflineFOAMetadataEv
+ __ZN16AudioQueueObject22SetMetersInstantaneousEb
+ __ZN16AudioQueueObject24GetIONodeConnection_InitERi
+ __ZN16AudioQueueObject27HandlePauseDueToRouteChangeEv
+ __ZN16AudioQueueObject29IONode_DeviceStoppedFromBelowEb
+ __ZN16AudioQueueObject5StartERK15XAudioTimeStampjNSt3__18optionalIyEES5_
+ __ZN16AudioQueueObject8EndPauseEPK15XAudioTimeStampbjNSt3__18optionalIyEES5_
+ __ZN16TArrayMarshallerI20SplicingRequirementsE11DeserializeER14CADeserializerRPvRj
+ __ZN16TArrayMarshallerI20SplicingRequirementsED0Ev
+ __ZN16TArrayMarshallerI20SplicingRequirementsED1Ev
+ __ZN17LegacyHapticSynth22handleAudioRouteChangeENSt3__18functionIFvbEEEPK10__CFStringNS0_8optionalIbEE
+ __ZN17LegacyHapticSynth25hardwareSampleRateChangedENSt3__110shared_ptrI11SynthOutputEE
+ __ZN17ParameterSchedule15PurgeLinkedListERPNS_5EventE
+ __ZN17ParameterSchedule16PurgeAtomicStackERN12CADeprecated12TAtomicStackINS_5EventEEE
+ __ZN17ParameterSchedule5EventnwEmm
+ __ZN18AQHapticOutputNode25IO_DeviceStoppedFromBelowEbb
+ __ZN18CASmartPreferences16InterpretIntegerEPKv
+ __ZN18HapticAudioMetrics21logPowerLogCountEventE22PowerLogCountEventTypemimP8NSString
+ __ZN18HapticAudioMetricsD0Ev
+ __ZN18HapticAudioMetricsD1Ev
+ __ZN19OfflineFOAProcessor10InitializeEv
+ __ZN19OfflineFOAProcessor12UninitializeEv
+ __ZN19OfflineFOAProcessor13LoadStripFileERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_j
+ __ZN19OfflineFOAProcessorD0Ev
+ __ZN19OfflineFOAProcessorD1Ev
+ __ZN19OfflineFOAProcessorD2Ev
+ __ZN19SharableMemoryBlock14XPCClientTokenD0Ev
+ __ZN19SharableMemoryBlock14XPCClientTokenD2Ev
+ __ZN19SharableMemoryBlock14XPCServerTokenD0Ev
+ __ZN19SharableMemoryBlock14XPCServerTokenD2Ev
+ __ZN19SharableMemoryBlockD0Ev
+ __ZN19SharableMemoryBlockD1Ev
+ __ZN20AHSPowerBudgetServer30getPowerBudgetRangesAndSetOnFWE12CPMSClientIdPU28objcproto17CPMSAgentProtocol11objc_objectP12NSDictionary
+ __ZN20AHSPowerBudgetServer34copyThermalBudgetRangeInMilliWattsE12CPMSClientIdPU28objcproto17CPMSAgentProtocol11objc_object
+ __ZN20AudioCapturerManager15mAQCaptureInputE
+ __ZN20AudioCapturerManager18mAQMECaptureOutputE
+ __ZN20AudioCapturerManager22mAQCaptureOutputDecodeE
+ __ZN20AudioCapturerManager22mAQInputRingBufferModeE
+ __ZN20AudioCapturerManager23mAQCaptureOfflineRenderE
+ __ZN20AudioCapturerManager23mAQCaptureOutputEnqueueE
+ __ZN20AudioCapturerManager25mAQMEOutputRingBufferModeE
+ __ZN20AudioCapturerManager5FlushEv
+ __ZN20AudioCapturerManager9SetCookieEPKvj
+ __ZN20AudioCapturerManager9SetFormatERK27AudioStreamBasicDescription
+ __ZN20AudioCapturerManagerC2EOKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEi
+ __ZN20AudioQueueXPC_Bridge5StartEj19XAudioTimeStampBasejyy
+ __ZN20AudioQueueXPC_Client5StartEj19XAudioTimeStampBasejyy
+ __ZN20AudioQueueXPC_ClientD2Ev
+ __ZN20AudioQueueXPC_Server5StartEj19XAudioTimeStampBasejyy
+ __ZN20CAAudioChannelLayout16RefCountedLayoutD0Ev
+ __ZN20CAAudioChannelLayout16RefCountedLayoutD1Ev
+ __ZN20CA_UISoundClientBase29IONode_DeviceStoppedFromBelowEb
+ __ZN20MEDeviceStreamClient22deviceStoppedFromBelowEb
+ __ZN20VADPowerBudgetServer30getPowerBudgetRangesAndSetOnFWE12CPMSClientIdPU28objcproto17CPMSAgentProtocol11objc_objectP12NSDictionary
+ __ZN20VADPowerBudgetServer34copyThermalBudgetRangeInMilliWattsE12CPMSClientIdPU28objcproto17CPMSAgentProtocol11objc_object
+ __ZN21AudioSessionExceptionC1Ei
+ __ZN21AudioSessionExceptionC2Ei
+ __ZN21ResourcePathUtilitiesL14CFDictFromPathERKN10applesauce2CF9StringRefE.3908
+ __ZN21ResourcePathUtilitiesL19ResolveResourcePathERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_.12745
+ __ZN21ResourcePathUtilitiesL19ResolveResourcePathERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_.3907
+ __ZN21ScheduledSlicePlayer212SetStartTimeERK15XAudioTimeStampxjNSt3__18optionalIyEES5_
+ __ZN21SpatializationManager32GetAUSpatialMixerHeadphonePresetENS_18SpatializationModeEib
+ __ZN22MultiOutputHapticSynth22handleAudioRouteChangeENSt3__18functionIFvbEEEPK10__CFStringNS0_8optionalIbEE
+ __ZN22MultiOutputHapticSynth25hardwareSampleRateChangedENSt3__110shared_ptrI11SynthOutputEE
+ __ZN22MultiOutputHapticSynth37shouldApplyVolumeControlOnSynthOutputEP11SynthOutput
+ __ZN22MultiOutputHapticSynth40handleSystemSoundsAndHapticsVolumeChangeEf
+ __ZN27ScheduledSlicePlayer_Legacy12SetStartTimeERK15XAudioTimeStampxjNSt3__18optionalIyEES5_
+ __ZN2AQ3API14ProcessingNodeD2Ev
+ __ZN2AQ3API5Queue19adoptProcessingNodeENSt3__110unique_ptrINS0_14ProcessingNodeENS2_14default_deleteIS4_EEEE
+ __ZN2AQ3API6V2Impl27AudioQueueStartWithIntervalEP16OpaqueAudioQueueyyy
+ __ZN2AT11Translation16TranslatorClient18serverDisconnectedEv
+ __ZN2AT11Translation16TranslatorClient25didReceiveTranslatedAudioEP16AVAudioPCMBuffer
+ __ZN2AT11Translation16TranslatorClient27didStopTranslationWithErrorEP7NSError
+ __ZN2CA12OpaqueObject10BaseLookupC2Ej
+ __ZN2CA12OpaqueObject10BaseLookupD2Ev
+ __ZN2CA12OpaqueObject3RefIN5Phase13ServerManagerEjED0Ev
+ __ZN2CA12OpaqueObject3RefIN5Phase13ServerManagerEjED1Ev
+ __ZN2CA12OpaqueObject4BaseI10AQMEIO_HALjNS0_4RootEE5sRTTIE
+ __ZN2CA12OpaqueObject4BaseI13SequenceTrackP16OpaqueMusicTrackNS0_4RootEE5sRTTIE
+ __ZN2CA12OpaqueObject4BaseI14AQOfflineMixerjNS0_4RootEE5sRTTIE
+ __ZN2CA12OpaqueObject4BaseI14AudioTapObjectP14OpaqueAudioTapNS0_4RootEE5sRTTIE
+ __ZN2CA12OpaqueObject4BaseI14AudioUnitGraphP13OpaqueAUGraphNS0_4RootEE5sRTTIE
+ __ZN2CA12OpaqueObject4BaseI14RemoteIOClientjN12CADeprecated11XMachServer6ClientEE5sRTTIE
+ __ZN2CA12OpaqueObject4BaseI14SequencePlayerP17OpaqueMusicPlayerNS0_4RootEE5sRTTIE
+ __ZN2CA12OpaqueObject4BaseI15AQProcessingTapjNS0_4RootEE5sRTTIE
+ __ZN2CA12OpaqueObject4BaseI15AudioQueueOwnerjNS0_4RootEE5sRTTIE
+ __ZN2CA12OpaqueObject4BaseI15SubmixTapObjectjNS0_4RootEE5sRTTIE
+ __ZN2CA12OpaqueObject4BaseI16AQProcessingNodejNS0_4RootEE5sRTTIE
+ __ZN2CA12OpaqueObject4BaseI17ZenAQIONodeClientjNS0_4RootEE5sRTTIE
+ __ZN2CA12OpaqueObject4BaseI21ExportedTrackIteratorP24OpaqueMusicEventIteratorNS0_4RootEE5sRTTIE
+ __ZN2CA12OpaqueObject4BaseI8SequenceP19OpaqueMusicSequenceNS0_4RootEE5sRTTIE
+ __ZN2CA12OpaqueObject4BaseIN12CADeprecated11XMachServer6ClientEjNS0_4RootEE5sRTTIE
+ __ZN2CA12OpaqueObject4BaseIN2AQ3API12OfflineMixerEP20OpaqueAQOfflineMixerNS0_4RootEE5sRTTIE
+ __ZN2CA12OpaqueObject4BaseIN2AQ3API13ProcessingTapEP29OpaqueAudioQueueProcessingTapNS0_4RootEE5sRTTIE
+ __ZN2CA12OpaqueObject4BaseIN2AQ3API14ProcessingNodeEP27OpaqueATAudioProcessingNodeNS0_4RootEE5sRTTIE
+ __ZN2CA12OpaqueObject4BaseIN2AQ3API5QueueEP16OpaqueAudioQueueNS0_4RootEE5sRTTIE
+ __ZN2CA12OpaqueObject4BaseIN2AQ3API9SubmixTapEP17OpaqueATSubmixTapNS0_4RootEE5sRTTIE
+ __ZN2CA12OpaqueObject4BaseINS0_3RefIN5Phase13ServerManagerEjEEjNS0_4RootEE5sRTTIE
+ __ZN2CA12OpaqueObject4Root10InvalidateEv
+ __ZN2CA12OpaqueObject4Root9FromTokenERKNS0_4RTTIEj
+ __ZN2CA12OpaqueObject4RootC2Ev
+ __ZN2CA12OpaqueObject4RootD2Ev
+ __ZN2CA12OpaqueObject6LookupI15AudioQueueOwnerEC2Ej
+ __ZN4swix10connection10invalidateEv
+ __ZN4swix13ipc_interface10invalidateEv
+ __ZN4swix8listenerD2Ev
+ __ZN5boost3msm4back13state_machineIN11SequenceFSM10StateFront11ActiveFrontENS_9parameter5void_ES7_S7_S7_E18visitor_fct_helperINS3_9StateBaseEvE6insertINS_3_bi6bind_tIvNS_4_mfi4cmf3IvNS4_12FlushingBaseINS4_13FlushingNamerEEERNS3_25PostRenderFlushingVisitorEP14SequenceActiondEENSD_5list4INS_17reference_wrapperINS0_5front4euml10func_stateISI_NS4_12DefaultEntryENS4_12FlushingExitENS_6fusion6vectorIJEEENS_3mpl6vectorINS3_10IsFlushingEN4mpl_2naES13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_S13_EENSZ_7vector0IS13_EESJ_EEEENS_3argILi1EEENS19_ILi2EEENS19_ILi3EEEEEEEEEviT_
+ __ZN5boost3msm4back13state_machineIN11SequenceFSM10StateFront11ActiveFrontENS_9parameter5void_ES7_S7_S7_E18visitor_fct_helperINS3_9StateBaseEvE6insertINS_3_bi6bind_tIvNS_4_mfi4cmf3IvSA_RNS3_25PostRenderFlushingVisitorEP14SequenceActiondEENSD_5list4INS_17reference_wrapperINS0_5front4euml10func_stateINS4_11LoadedNamerENS4_12DefaultEntryENS4_11DefaultExitENS_6fusion6vectorIJEEENS_3mpl7vector0IN4mpl_2naEEES11_NS3_9NamedBaseISR_EEEEEENS_3argILi1EEENS16_ILi2EEENS16_ILi3EEEEEEEEEviT_
+ __ZN5boost3msm4back13state_machineIN11SequenceFSM10StateFront11ActiveFrontENS_9parameter5void_ES7_S7_S7_E18visitor_fct_helperINS3_9StateBaseEvE6insertINS_3_bi6bind_tIvNS_4_mfi4cmf3IvSA_RNS3_25PostRenderFlushingVisitorEP14SequenceActiondEENSD_5list4INS_17reference_wrapperINS0_5front4euml10func_stateINS4_11PausedNamerENS4_11PausedEntryENS4_10PausedExitENS_6fusion6vectorIJEEENS_3mpl6vectorINS3_9IsRunningEN4mpl_2naES11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_EENSY_INS3_4SeekES11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_EENS3_9NamedBaseISR_EEEEEENS_3argILi1EEENS19_ILi2EEENS19_ILi3EEEEEEEEEviT_
+ __ZN5boost3msm4back13state_machineIN11SequenceFSM10StateFront11ActiveFrontENS_9parameter5void_ES7_S7_S7_E18visitor_fct_helperINS3_9StateBaseEvE6insertINS_3_bi6bind_tIvNS_4_mfi4cmf3IvSA_RNS3_25PostRenderFlushingVisitorEP14SequenceActiondEENSD_5list4INS_17reference_wrapperINS0_5front4euml10func_stateINS4_12PausingNamerENS4_12PausingEntryENS4_11PausingExitENS_6fusion6vectorIJEEENS_3mpl6vectorINS3_9IsRunningENS3_9IsPausingEN4mpl_2naES12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_EENSY_INS3_6ResumeENS3_4PlayENS3_4SeekENS3_4StopENS3_13EnableLoopingES12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_S12_EENS3_9NamedBaseISR_EEEEEENS_3argILi1EEENS1E_ILi2EEENS1E_ILi3EEEEEEEEEviT_
+ __ZN5boost3msm4back13state_machineIN11SequenceFSM10StateFront11ActiveFrontENS_9parameter5void_ES7_S7_S7_E18visitor_fct_helperINS3_9StateBaseEvE6insertINS_3_bi6bind_tIvNS_4_mfi4cmf3IvSA_RNS3_25PostRenderFlushingVisitorEP14SequenceActiondEENSD_5list4INS_17reference_wrapperINS0_5front4euml10func_stateINS4_12RunningNamerENS4_12RunningEntryENS4_11RunningExitENS_6fusion6vectorIJEEENS_3mpl6vectorINS3_9IsRunningEN4mpl_2naES11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_S11_EENSX_7vector0IS11_EENS3_9NamedBaseISR_EEEEEENS_3argILi1EEENS19_ILi2EEENS19_ILi3EEEEEEEEEviT_
+ __ZN5boost3msm4back13state_machineIN11SequenceFSM10StateFront11ActiveFrontENS_9parameter5void_ES7_S7_S7_E18visitor_fct_helperINS3_9StateBaseEvE6insertINS_3_bi6bind_tIvNS_4_mfi4cmf3IvSA_RNS3_25PostRenderFlushingVisitorEP14SequenceActiondEENSD_5list4INS_17reference_wrapperINS0_5front4euml10func_stateINS4_13StoppingNamerENS4_13StoppingEntryENS4_12StoppingExitENS_6fusion6vectorIJEEENS_3mpl7vector0IN4mpl_2naEEES11_NS3_9NamedBaseISR_EEEEEENS_3argILi1EEENS16_ILi2EEENS16_ILi3EEEEEEEEEviT_
+ __ZN5boost3msm4back13state_machineIN11SequenceFSM10StateFront11ActiveFrontENS_9parameter5void_ES7_S7_S7_E18visitor_fct_helperINS3_9StateBaseEvE6insertINS_3_bi6bind_tIvNS_4_mfi4cmf3IvSA_RNS3_25PostRenderFlushingVisitorEP14SequenceActiondEENSD_5list4INS_17reference_wrapperINS8_7exit_ptINS5_10ActiveExitEEEEENS_3argILi1EEENSS_ILi2EEENSS_ILi3EEEEEEEEEviT_
+ __ZN5boost9typeindex6detailL23ctti_skip_until_runtimeE.9747
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__110shared_ptrI16AudioCapturerIfcEEE7mutator5writeES5_
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__110shared_ptrIN2AT11Translation14CallTranslatorEEEE7mutator5writeES7_
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__113unordered_mapImNS2_10shared_ptrI14HapticSequenceEENS2_4hashImEENS2_8equal_toImEENS2_9allocatorINS2_4pairIKmS6_EEEEEEE7mutator13copy_previousEv
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__113unordered_mapImNS2_10shared_ptrI14HapticSequenceEENS2_4hashImEENS2_8equal_toImEENS2_9allocatorINS2_4pairIKmS6_EEEEEEE7mutatorD2Ev
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__113unordered_mapImNS2_10shared_ptrI14HapticSequenceEENS2_4hashImEENS2_8equal_toImEENS2_9allocatorINS2_4pairIKmS6_EEEEEEED2Ev
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__13mapIjjNS2_4lessIjEENS2_9allocatorINS2_4pairIKjjEEEEEEE7mutator13copy_previousEv
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__13mapIjjNS2_4lessIjEENS2_9allocatorINS2_4pairIKjjEEEEEEE7mutatorD2Ev
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__13mapIjjNS2_4lessIjEENS2_9allocatorINS2_4pairIKjjEEEEEEEC2Ev
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__13mapIjjNS2_4lessIjEENS2_9allocatorINS2_4pairIKjjEEEEEEED2Ev
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__13mapImNS2_10shared_ptrI11ClientEntryEENS2_4lessImEENS2_9allocatorINS2_4pairIKmS6_EEEEEEE7mutator13copy_previousEv
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__13mapImNS2_10shared_ptrI11ClientEntryEENS2_4lessImEENS2_9allocatorINS2_4pairIKmS6_EEEEEEE7mutatorD2Ev
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__13mapImNS2_10shared_ptrI11ClientEntryEENS2_4lessImEENS2_9allocatorINS2_4pairIKmS6_EEEEEEED2Ev
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__13mapImjNS2_4lessImEENS2_9allocatorINS2_4pairIKmjEEEEEEE7mutator13copy_previousEv
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__13mapImjNS2_4lessImEENS2_9allocatorINS2_4pairIKmjEEEEEEE7mutatorD2Ev
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__13mapImjNS2_4lessImEENS2_9allocatorINS2_4pairIKmjEEEEEEED2Ev
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__16vectorINS2_4pairINS2_10shared_ptrI11SynthOutputEEbEENS2_9allocatorIS8_EEEEE7mutator13copy_previousEv
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__16vectorINS2_4pairINS2_10shared_ptrI11SynthOutputEEbEENS2_9allocatorIS8_EEEEE7mutatorD2Ev
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__16vectorINS2_4pairINS2_10shared_ptrI11SynthOutputEEbEENS2_9allocatorIS8_EEEEED2Ev
+ __ZN5caulk10concurrent5stackINS_5alloc10free_blockENS0_26intrusive_single_link_nodeIS3_PS3_EEE3popEv
+ __ZN5caulk10concurrent7details12message_callIRZN11ClientEntry16unduckOtherAudioEmE3$_0JEE7performEv
+ __ZN5caulk10concurrent7details12message_callIRZN11ClientEntry16unduckOtherAudioEmE3$_0JEED0Ev
+ __ZN5caulk10concurrent7details12message_callIRZN11ClientEntry16unduckOtherAudioEmE3$_0JEED1Ev
+ __ZN5caulk10concurrent7details12message_callIRZN11ClientEntry22handleSequenceFinishedEmE3$_1JEE7performEv
+ __ZN5caulk10concurrent7details12message_callIRZN11ClientEntry22handleSequenceFinishedEmE3$_1JEED0Ev
+ __ZN5caulk10concurrent7details12message_callIRZN11ClientEntry22handleSequenceFinishedEmE3$_1JEED1Ev
+ __ZN5caulk10concurrent7details14node_allocatorIPvNS_5alloc6detail13tracked_blockELm10ELNS0_16skiplist_optionsE0EE9free_nodeEPNS1_13skiplist_nodeIS3_S6_EE
+ __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry16unduckOtherAudioEmE3$_0JEE10rt_cleanupD1Ev
+ __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry16unduckOtherAudioEmE3$_0JEE7performEv
+ __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry16unduckOtherAudioEmE3$_0JEED0Ev
+ __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry16unduckOtherAudioEmE3$_0JEED1Ev
+ __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry22handleSequenceFinishedEmE3$_1JEE10rt_cleanupD1Ev
+ __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry22handleSequenceFinishedEmE3$_1JEE7performEv
+ __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry22handleSequenceFinishedEmE3$_1JEED0Ev
+ __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry22handleSequenceFinishedEmE3$_1JEED1Ev
+ __ZN5caulk10concurrent7details15rt_message_callIRZZN11ClientEntry18playSequenceWithIDEmddENK3$_0clINSt3__110shared_ptrI14HapticSequenceEEEEDaRKT_EUlvE_JEE10rt_cleanupD1Ev
+ __ZN5caulk10concurrent7details15rt_message_callIRZZN11ClientEntry18playSequenceWithIDEmddENK3$_0clINSt3__110shared_ptrI14HapticSequenceEEEEDaRKT_EUlvE_JEE7performEv
+ __ZN5caulk10concurrent7details15rt_message_callIRZZN11ClientEntry18playSequenceWithIDEmddENK3$_0clINSt3__110shared_ptrI14HapticSequenceEEEEDaRKT_EUlvE_JEED0Ev
+ __ZN5caulk10concurrent7details15rt_message_callIRZZN11ClientEntry18playSequenceWithIDEmddENK3$_0clINSt3__110shared_ptrI14HapticSequenceEEEEDaRKT_EUlvE_JEED1Ev
+ __ZN5caulk10concurrent8skiplistIPvNS_5alloc6detail13tracked_blockELi10ELNS0_16skiplist_optionsE0EE13random_uint32Ev
+ __ZN5caulk12function_refIFbPK22AVHapticServerInstanceRKNSt3__110shared_ptrI11ClientEntryEEEE15functor_invokerIZ44-[AVHapticServer forceStopIdleDaemonClients]E3$_6EEbRKNS_7details15erased_callableISA_EES3_S9_
+ __ZN5caulk12function_refIFbPK22AVHapticServerInstanceRKNSt3__110shared_ptrI11ClientEntryEEEE15functor_invokerIZ47-[AVHapticServer forceUnprewarmEligibleClients]E4$_10EEbRKNS_7details15erased_callableISA_EES3_S9_
+ __ZN5caulk12function_refIFbPK22AVHapticServerInstanceRKNSt3__110shared_ptrI11ClientEntryEEEE15functor_invokerIZ55-[AVHapticServer forceStopIdleBackgroundRunningClients]E3$_8EEbRKNS_7details15erased_callableISA_EES3_S9_
+ __ZN5caulk12function_refIFvPK22AVHapticServerInstanceRKNSt3__110shared_ptrI11ClientEntryEEEE15functor_invokerIZ44-[AVHapticServer forceStopIdleDaemonClients]E3$_5EEvRKNS_7details15erased_callableISA_EES3_S9_
+ __ZN5caulk12function_refIFvPK22AVHapticServerInstanceRKNSt3__110shared_ptrI11ClientEntryEEEE15functor_invokerIZ47-[AVHapticServer forceUnprewarmEligibleClients]E3$_9EEvRKNS_7details15erased_callableISA_EES3_S9_
+ __ZN5caulk12function_refIFvPK22AVHapticServerInstanceRKNSt3__110shared_ptrI11ClientEntryEEEE15functor_invokerIZ55-[AVHapticServer forceStopIdleBackgroundRunningClients]E3$_7EEvRKNS_7details15erased_callableISA_EES3_S9_
+ __ZN5caulk12synchronizedIN2AQ3API5Queue12GuardedStateENS_4mach11unfair_lockENS_22empty_atomic_interfaceIS4_EEED2Ev
+ __ZN5caulk14cf_preferences10get_doubleEPK10__CFStringS3_
+ __ZN5caulk14cf_preferences14interpret_boolEPKv
+ __ZN5caulk14cf_preferences15interpret_int64EPKv
+ __ZN5caulk14cf_preferences16interpret_doubleEPKv
+ __ZN5caulk14cf_preferences19interpret_log_levelEPKv
+ __ZN5caulk14cf_preferences7monitor11add_handlerIxEEbPK10__CFStringS5_PFNSt3__18optionalIT_EEPKvERKNS6_8functionIFvS8_EEE
+ __ZN5caulk14cf_preferences7monitor12_add_handlerEPK10__CFStringS4_ONSt3__18functionIFbPKvEEE
+ __ZN5caulk14cf_preferences7monitor3addEPK10__CFStringS4_Rb
+ __ZN5caulk14cf_preferences7monitor3addEPK10__CFStringS4_Rf
+ __ZN5caulk14cf_preferences7monitor3addEPK10__CFStringS4_Ri
+ __ZN5caulk14cf_preferences7monitor8instanceEv
+ __ZN5caulk14cf_preferences8get_boolEPK10__CFStringS3_
+ __ZN5caulk14cf_preferences9get_int64EPK10__CFStringS3_
+ __ZN5caulk15rt_function_refIFvPvRK14AudioTimeStampjEE13empty_invokerERKNS_7details18erased_callable_rtIFvS1_S4_jEEES1_S4_j
+ __ZN5caulk15rt_function_refIFvPvRK14AudioTimeStampjEE16function_invokerERKNS_7details18erased_callable_rtIFvS1_S4_jEEES1_S4_j
+ __ZN5caulk15rt_function_refIFvRKNSt3__110shared_ptrI14HapticSequenceEEEE15functor_invokerIZN11ClientEntry18playSequenceWithIDEmddE3$_0EEvRKNS_7details18erased_callable_rtIFvS6_EEES6_
+ __ZN5caulk15rt_function_refIFvRKNSt3__110shared_ptrI14HapticSequenceEEEE15functor_invokerIZN11ClientEntry18seekSequenceWithIDEmdE3$_0EEvRKNS_7details18erased_callable_rtIFvS6_EEES6_
+ __ZN5caulk15rt_function_refIFvRKNSt3__110shared_ptrI14HapticSequenceEEEE15functor_invokerIZN11ClientEntry18stopSequenceWithIDEmE3$_0EEvRKNS_7details18erased_callable_rtIFvS6_EEES6_
+ __ZN5caulk15rt_function_refIFvRKNSt3__110shared_ptrI14HapticSequenceEEEE15functor_invokerIZN11ClientEntry19pauseSequenceWithIDEmE3$_0EEvRKNS_7details18erased_callable_rtIFvS6_EEES6_
+ __ZN5caulk15rt_function_refIFvRKNSt3__110shared_ptrI14HapticSequenceEEEE15functor_invokerIZN11ClientEntry19resetSequenceWithIDEmE3$_0EEvRKNS_7details18erased_callable_rtIFvS6_EEES6_
+ __ZN5caulk15rt_function_refIFvRKNSt3__110shared_ptrI14HapticSequenceEEEE15functor_invokerIZN11ClientEntry20resumeSequenceWithIDEmE3$_0EEvRKNS_7details18erased_callable_rtIFvS6_EEES6_
+ __ZN5caulk15rt_function_refIFvRKNSt3__110shared_ptrI14HapticSequenceEEEE15functor_invokerIZN11ClientEntry21handleRealTimeCommandENSA_16QueueCommandTypeEjP11HapticSynthRK14AudioTimeStampjE3$_0EEvRKNS_7details18erased_callable_rtIFvS6_EEES6_
+ __ZN5caulk15rt_function_refIFvRKNSt3__110shared_ptrI14HapticSequenceEEEE15functor_invokerIZN11ClientEntry21handleRealTimeCommandENSA_16QueueCommandTypeEjP11HapticSynthRK14AudioTimeStampjE3$_1EEvRKNS_7details18erased_callable_rtIFvS6_EEES6_
+ __ZN5caulk15rt_function_refIFvRKNSt3__110shared_ptrI14HapticSequenceEEEE15functor_invokerIZN11ClientEntry26getSequenceChannelForIndexEmjE3$_0EEvRKNS_7details18erased_callable_rtIFvS6_EEES6_
+ __ZN5caulk15rt_function_refIFvRKNSt3__110shared_ptrI14HapticSequenceEEEE15functor_invokerIZN11ClientEntry26handleDetachSequenceWithIDEmE3$_0EEvRKNS_7details18erased_callable_rtIFvS6_EEES6_
+ __ZN5caulk15rt_function_refIFvRKNSt3__110shared_ptrI14HapticSequenceEEEE15functor_invokerIZN11ClientEntry29enableLoopingOnSequenceWithIDEmbE3$_0EEvRKNS_7details18erased_callable_rtIFvS6_EEES6_
+ __ZN5caulk15rt_function_refIFvRKNSt3__110shared_ptrI14HapticSequenceEEEE15functor_invokerIZN11ClientEntry29setLoopLengthOnSequenceWithIDEmdE3$_0EEvRKNS_7details18erased_callable_rtIFvS6_EEES6_
+ __ZN5caulk15rt_function_refIFvRKNSt3__110shared_ptrI14HapticSequenceEEEE15functor_invokerIZN11ClientEntry31setPlaybackRateOnSequenceWithIDEmfE3$_0EEvRKNS_7details18erased_callable_rtIFvS6_EEES6_
+ __ZN5caulk15rt_function_refIFvRKNSt3__110shared_ptrI14HapticSequenceEEEE15functor_invokerIZN11ClientEntry4dumpEP7__sFILEE3$_0EEvRKNS_7details18erased_callable_rtIFvS6_EEES6_
+ __ZN5caulk15rt_function_refIFvRKNSt3__110shared_ptrI14HapticSequenceEEEE15functor_invokerIZN11ClientEntry9preRenderEP11HapticSynthRK14AudioTimeStampjE3$_0EEvRKNS_7details18erased_callable_rtIFvS6_EEES6_
+ __ZN5caulk15rt_function_refIFvRKNSt3__110shared_ptrI14HapticSequenceEEEE15functor_invokerIZN14SSSClientEntry21handleRealTimeCommandEN11ClientEntry16QueueCommandTypeEjP11HapticSynthRK14AudioTimeStampjE3$_0EEvRKNS_7details18erased_callable_rtIFvS6_EEES6_
+ __ZN5caulk15rt_function_refIFvRKNSt3__110shared_ptrI14HapticSequenceEEEE15functor_invokerIZN14SSSClientEntry21handleRealTimeCommandEN11ClientEntry16QueueCommandTypeEjP11HapticSynthRK14AudioTimeStampjE3$_1EEvRKNS_7details18erased_callable_rtIFvS6_EEES6_
+ __ZN5caulk15rt_function_refIFvRKNSt3__110shared_ptrI14HapticSequenceEEEE15functor_invokerIZN14SSSClientEntry21handleRealTimeCommandEN11ClientEntry16QueueCommandTypeEjP11HapticSynthRK14AudioTimeStampjE3$_2EEvRKNS_7details18erased_callable_rtIFvS6_EEES6_
+ __ZN5caulk15rt_function_refIFvRKNSt3__110shared_ptrI14HapticSequenceEEEE15functor_invokerIZN14SSSClientEntry22handleSequenceFinishedEmE3$_0EEvRKNS_7details18erased_callable_rtIFvS6_EEES6_
+ __ZN5caulk16inplace_functionIFKN13ServerManager12SynthCommandEvELm32ELm8ENS_23inplace_function_detail9rt_vtableEE16k_wrapper_vtableIZNS1_12DoRenderProcERK14AudioTimeStampjE3$_1EE
+ __ZN5caulk16inplace_functionIFviELm32ELm8ENS_23inplace_function_detail9rt_vtableEE16k_wrapper_vtableIZN12SequenceImpl9sendEventIN11SequenceFSM10BeginPauseEEEiRKT_EUliE_EE
+ __ZN5caulk16inplace_functionIFviELm32ELm8ENS_23inplace_function_detail9rt_vtableEE16k_wrapper_vtableIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI12NSDictionaryEEEEiRKT_EUliE_EE
+ __ZN5caulk16inplace_functionIFviELm32ELm8ENS_23inplace_function_detail9rt_vtableEE16k_wrapper_vtableIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI6NSDataEEEEiRKT_EUliE_EE
+ __ZN5caulk16inplace_functionIFviELm32ELm8ENS_23inplace_function_detail9rt_vtableEE16k_wrapper_vtableIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI7NSArrayEEEEiRKT_EUliE_EE
+ __ZN5caulk16inplace_functionIFviELm32ELm8ENS_23inplace_function_detail9rt_vtableEE16k_wrapper_vtableIZN12SequenceImpl9sendEventIN11SequenceFSM4PlayEEEiRKT_EUliE_EE
+ __ZN5caulk16inplace_functionIFviELm32ELm8ENS_23inplace_function_detail9rt_vtableEE16k_wrapper_vtableIZN12SequenceImpl9sendEventIN11SequenceFSM4SeekEEEiRKT_EUliE_EE
+ __ZN5caulk16inplace_functionIFviELm32ELm8ENS_23inplace_function_detail9rt_vtableEE16k_wrapper_vtableIZN12SequenceImpl9sendEventIN11SequenceFSM4StopEEEiRKT_EUliE_EE
+ __ZN5caulk16inplace_functionIFviELm32ELm8ENS_23inplace_function_detail9rt_vtableEE16k_wrapper_vtableIZN12SequenceImpl9sendEventIN11SequenceFSM5StartEEEiRKT_EUliE_EE
+ __ZN5caulk16inplace_functionIFviELm32ELm8ENS_23inplace_function_detail9rt_vtableEE16k_wrapper_vtableIZN12SequenceImpl9sendEventIN11SequenceFSM6DetachEEEiRKT_EUliE_EE
+ __ZN5caulk16inplace_functionIFviELm32ELm8ENS_23inplace_function_detail9rt_vtableEE16k_wrapper_vtableIZN12SequenceImpl9sendEventIN11SequenceFSM6ResumeEEEiRKT_EUliE_EE
+ __ZN5caulk16inplace_functionIFviELm32ELm8ENS_23inplace_function_detail9rt_vtableEE16k_wrapper_vtableIZN12SequenceImpl9sendEventIN11SequenceFSM7PrepareEEEiRKT_EUliE_EE
+ __ZN5caulk16inplace_functionIFviELm32ELm8ENS_23inplace_function_detail9rt_vtableEE16k_wrapper_vtableIZN12SequenceImpl9sendEventIN11SequenceFSM9ForceStopEEEiRKT_EUliE_EE
+ __ZN5caulk16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail9rt_vtableEE16k_wrapper_vtableIZN11ClientEntry17doPrepareSequenceENSt3__110shared_ptrI14HapticSequenceEENS0_IS1_Lm32ELm8ENS2_6vtableEEEE3$_0EE
+ __ZN5caulk19multi_simple_randomIyLm4ENSt3__124uniform_int_distributionIyEENS_12xoshiro256ssEEC2Eyy
+ __ZN5caulk23inplace_function_detail9rt_vtableIvJiEE5emptyE
+ __ZN5caulk23inplace_function_detail9rt_vtableIvJmEE5emptyE
+ __ZN5caulk7numeric15exceptional_addIjEET_S2_S2_
+ __ZN5caulk7product11_aid_prefixEv
+ __ZN7TStream9ReadAsyncEPviP18TAsyncIoClient_BSDl
+ __ZN7TStream9SeekAsyncEx
+ __ZN8TFileBSD10DeleteFileEv
+ __ZN8TFileBSD11GetPositionEv
+ __ZN8TFileBSD4ReadEPvm
+ __ZN8TFileBSD4SeekEx
+ __ZN8TFileBSD4SkipEx
+ __ZN8TFileBSD5CloseEv
+ __ZN8TFileBSD5WriteEPvm
+ __ZN8TFileBSD9ReadAsyncEPviP18TAsyncIoClient_BSDl
+ __ZN8TFileBSD9SeekAsyncEx
+ __ZN8TFileBSDD0Ev
+ __ZN8TFileBSDD2Ev
+ __ZN9TapSource6renderERK14AudioTimeStampjRK15AudioBufferListRS0_RjRS3_
+ __ZNK10AQMEIO_HAL15GetDeviceUIDStrEv
+ __ZNK11ClientEntry6idlingEv
+ __ZNK11HapticSynth18doForHapticOutputsIZN17LegacyHapticSynth12startRunningEbbjNSt3__18functionIFivEEEjE3$_2EEvOT_
+ __ZNK11HapticSynth18doForHapticOutputsIZN22MultiOutputHapticSynth12startRunningEbbjNSt3__18functionIFivEEEjE3$_2EEvOT_
+ __ZNK12CAXException4whatEv
+ __ZNK12MemoryStream9GetLengthEv
+ __ZNK14AQIONodeClient11descriptionEv
+ __ZNK14AudioUnitGraph14GetNodeByIndexEiRi
+ __ZNK14SSSClientEntry6idlingEv
+ __ZNK15AQProcessingTap11DescriptionEv
+ __ZNK15AudioQueueOwner11DescriptionEv
+ __ZNK16AQProcessingNode11DescriptionEv
+ __ZNK19SharableMemoryBlock14XPCClientToken7IsValidEv
+ __ZNK20AudioCapturerManager11GetFilePathEv
+ __ZNK20AudioCapturerManager11WriteBufferEPKvjx
+ __ZNK20AudioCapturerManager15WriteBufferListEPK15AudioBufferListjx
+ __ZNK2AQ3API12OfflineMixer11DescriptionEv
+ __ZNK2AQ3API5Queue11DescriptionEv
+ __ZNK2AQ3API9SubmixTap11DescriptionEv
+ __ZNK2CA12OpaqueObject4BaseI10AQMEIO_HALjNS0_4RootEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4BaseI13SequenceTrackP16OpaqueMusicTrackNS0_4RootEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4BaseI14AQOfflineMixerjNS0_4RootEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4BaseI14AudioTapObjectP14OpaqueAudioTapNS0_4RootEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4BaseI14AudioUnitGraphP13OpaqueAUGraphNS0_4RootEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4BaseI14RemoteIOClientjN12CADeprecated11XMachServer6ClientEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4BaseI14SequencePlayerP17OpaqueMusicPlayerNS0_4RootEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4BaseI15AQProcessingTapjNS0_4RootEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4BaseI15AudioQueueOwnerjNS0_4RootEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4BaseI15SubmixTapObjectjNS0_4RootEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4BaseI16AQProcessingNodejNS0_4RootEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4BaseI17ZenAQIONodeClientjNS0_4RootEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4BaseI21ExportedTrackIteratorP24OpaqueMusicEventIteratorNS0_4RootEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4BaseI8SequenceP19OpaqueMusicSequenceNS0_4RootEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4BaseIN12CADeprecated11XMachServer6ClientEjNS0_4RootEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4BaseIN2AQ3API12OfflineMixerEP20OpaqueAQOfflineMixerNS0_4RootEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4BaseIN2AQ3API13ProcessingTapEP29OpaqueAudioQueueProcessingTapNS0_4RootEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4BaseIN2AQ3API14ProcessingNodeEP27OpaqueATAudioProcessingNodeNS0_4RootEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4BaseIN2AQ3API5QueueEP16OpaqueAudioQueueNS0_4RootEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4BaseIN2AQ3API9SubmixTapEP17OpaqueATSubmixTapNS0_4RootEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4BaseINS0_3RefIN5Phase13ServerManagerEjEEjNS0_4RootEE4_isaERKNS0_4RTTIE
+ __ZNK2CA12OpaqueObject4Root11DescriptionEv
+ __ZNK2CA12OpaqueObject4Root18GenericDescriptionEPKc
+ __ZNK2CA12OpaqueObject4Root4_isaERKNS0_4RTTIE
+ __ZNK4swix10connection7timeoutEv
+ __ZNK5caulk10concurrent26lf_read_synchronized_writeIN10applesauce8dispatch2v15blockIFv28AUVoiceIOSpeechActivityEventEEEE12begin_accessEv
+ __ZNK5caulk10concurrent26lf_read_synchronized_writeIN16AudioQueueObject19AQRateChangeHistory12RateScheduleEE12begin_accessEv
+ __ZNK5caulk10concurrent26lf_read_synchronized_writeINSt3__110shared_ptrI16AudioCapturerIfcEEE12begin_accessEv
+ __ZNK5caulk10concurrent26lf_read_synchronized_writeINSt3__110shared_ptrIN2AT11Translation14CallTranslatorEEEE12begin_accessEv
+ __ZNK5caulk10concurrent26lf_read_synchronized_writeINSt3__110unique_ptrIN18MixTapToUplinkHost46MixTapToUplinkGroupedByMicrophoneInjectionModeENS2_14default_deleteIS5_EEEEE12begin_accessEv
+ __ZNK5caulk10concurrent26lf_read_synchronized_writeINSt3__113unordered_mapImNS2_10shared_ptrI14HapticSequenceEENS2_4hashImEENS2_8equal_toImEENS2_9allocatorINS2_4pairIKmS6_EEEEEEE12begin_accessEv
+ __ZNK5caulk10concurrent26lf_read_synchronized_writeINSt3__13mapIP9TapSubmixN14MEMixerChannel19TapSubmixConnectionENS2_4lessIS5_EENS2_9allocatorINS2_4pairIKS5_S7_EEEEEEE12begin_accessEv
+ __ZNK5caulk10concurrent26lf_read_synchronized_writeINSt3__13mapImNS2_10shared_ptrI11ClientEntryEENS2_4lessImEENS2_9allocatorINS2_4pairIKmS6_EEEEEEE12begin_accessEv
+ __ZNK5caulk10concurrent26lf_read_synchronized_writeINSt3__13mapImjNS2_4lessImEENS2_9allocatorINS2_4pairIKmjEEEEEEE12begin_accessEv
+ __ZNK5caulk10concurrent26lf_read_synchronized_writeINSt3__16vectorINS2_10shared_ptrI9TapSubmixEENS2_9allocatorIS6_EEEEE12begin_accessEv
+ __ZNK5caulk10concurrent26lf_read_synchronized_writeINSt3__16vectorINS2_4pairINS2_10shared_ptrI11SynthOutputEEbEENS2_9allocatorIS8_EEEEE12begin_accessEv
+ __ZNK5caulk10concurrent26lf_read_synchronized_writeIP13AudioTapMixerE12begin_accessEv
+ __ZNK5caulk10concurrent26lf_read_synchronized_writeIPN2AT11Translation13AudioInjectorEE12begin_accessEv
+ __ZNK8TFileBSD6IsOpenEv
+ __ZNK9CACFArray9GetCFTypeEjRPKv
+ __ZNKSt3__110__function6__funcIZN13ServerManager13setupListenerEvE3$_6FvbEE7__cloneEPNS0_6__baseIS4_EE
+ __ZNKSt3__110__function6__funcIZN13ServerManager13setupListenerEvE3$_6FvbEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN13ServerManager25handleRouteChangeForEntryENS_10shared_ptrI11ClientEntryEEP8NSStringNS_8optionalIbEEE3$_0FvbEE7__cloneEPNS0_6__baseISB_EE
+ __ZNKSt3__110__function6__funcIZN13ServerManager25handleRouteChangeForEntryENS_10shared_ptrI11ClientEntryEEP8NSStringNS_8optionalIbEEE3$_0FvbEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN5CALog5Scope34SetPriorityThresholdFromPreferenceEPK10__CFStringS6_E3$_0FvN5caulk14cf_preferences9log_levelEEE7__cloneEPNS0_6__baseISB_EE
+ __ZNKSt3__110__function6__funcIZN5CALog5Scope34SetPriorityThresholdFromPreferenceEPK10__CFStringS6_E3$_0FvN5caulk14cf_preferences9log_levelEEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerINS3_9log_levelEEEbPK10__CFStringS9_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSB_EEEEUlSE_E_FbSE_EE7__cloneEPNS0_6__baseISN_EE
+ __ZNKSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerINS3_9log_levelEEEbPK10__CFStringS9_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSB_EEEEUlSE_E_FbSE_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIbEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EE7__cloneEPNS0_6__baseISM_EE
+ __ZNKSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIbEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIdEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EE7__cloneEPNS0_6__baseISM_EE
+ __ZNKSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIdEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIxEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EE7__cloneEPNS0_6__baseISM_EE
+ __ZNKSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIxEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RbEUlbE_FvbEE7__cloneEPNS0_6__baseISA_EE
+ __ZNKSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RbEUlbE_FvbEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RfEUldE_FvdEE7__cloneEPNS0_6__baseISA_EE
+ __ZNKSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RfEUldE_FvdEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RiEUlxE_FvxEE7__cloneEPNS0_6__baseISA_EE
+ __ZNKSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RiEUlxE_FvxEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERKNS_10shared_ptrI11SynthOutputEEEUlvE_FvvEE7__cloneEPNS0_6__baseISA_EE
+ __ZNKSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERKNS_10shared_ptrI11SynthOutputEEEUlvE_FvvEE7__cloneEv
+ __ZNKSt3__111__copy_implclB9foe220100IP11AQMESessionS3_S3_Li0EEENS_4pairIT_T1_EES5_T0_S6_
+ __ZNKSt3__111__copy_implclB9foe220100IP15MEVADIdentifierS3_S3_Li0EEENS_4pairIT_T1_EES5_T0_S6_
+ __ZNKSt3__111__copy_implclB9foe220100IPK11AQMESessionS4_PS2_Li0EEENS_4pairIT_T1_EES7_T0_S8_
+ __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB9foe220100IPNS_4pairIN5boost8functionIFNS5_3msm4back11HandledEnumEvEEEbEENS_16__deque_iteratorISC_SD_RSC_PSD_lLl102EEELi0EEENS4_IT_T0_EESI_SI_SJ_
+ __ZNKSt3__112__hash_tableINS_17__hash_value_typeIPK15AudioBufferListNS_4pairINS_6chrono10time_pointINS6_12steady_clockENS6_8durationIxNS_5ratioILl1ELl1000000000EEEEEEEU8__strongP16AVAudioPCMBufferEEEENS_22__unordered_map_hasherIS4_NS5_IKS4_SH_EENS_4hashIS4_EENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_SL_SP_SN_EENS_9allocatorISL_EEE4findIS4_EENS_21__hash_const_iteratorIPNS_11__hash_nodeISI_PvEEEERKT_
+ __ZNKSt3__112__hash_tableINS_17__hash_value_typeIijEENS_22__unordered_map_hasherIiNS_4pairIKijEENS_4hashIiEENS_8equal_toIiEEEENS_21__unordered_map_equalIiS6_SA_S8_EENS_9allocatorIS6_EEE19__equal_range_multiIiEENS4_INS_21__hash_const_iteratorIPNS_11__hash_nodeIS2_PvEEEESN_EERKT_
+ __ZNKSt3__112__hash_tableINS_17__hash_value_typeImNS_10shared_ptrI14HapticSequenceEEEENS_22__unordered_map_hasherImNS_4pairIKmS4_EENS_4hashImEENS_8equal_toImEEEENS_21__unordered_map_equalImS9_SD_SB_EENS_9allocatorIS9_EEE4findImEENS_21__hash_const_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findB9foe220100EPKcm
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareB9foe220100EmmRKS5_
+ __ZNKSt3__113__format_spec8__parserIcE10__validateB9foe220100ENS0_8__fieldsB9foe220100EPKcj
+ __ZNKSt3__113__format_spec8__parserIcE31__get_parsed_std_specificationsB9foe220100INS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENS0_23__parsed_specificationsIcEERT_
+ __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB9foe220100ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
+ __ZNKSt3__114default_deleteI15AudioTapManagerEclB9foe220100EPS1_
+ __ZNKSt3__114default_deleteI20SSSBufferClickFilterEclB9foe220100EPS1_
+ __ZNKSt3__114default_deleteI29AudioSessionPropertyListenersEclB9foe220100EPS1_
+ __ZNKSt3__114default_deleteI8AQBufferEclB9foe220100EPS1_
+ __ZNKSt3__114default_deleteIN12CADeprecated12CABufferListEEclB9foe220100EPS2_
+ __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE4viewB9foe220100Ev
+ __ZNKSt3__118__formatter_stringIcE6formatB9foe220100INS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT_8iteratorENS_17basic_string_viewIcNS_11char_traitsIcEEEERSA_
+ __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB9foe220100IPNS_4pairIN5boost8functionIFNS5_3msm4back11HandledEnumEvEEEbEENS_16__deque_iteratorISC_SD_RSC_PSD_lLl102EEELi0EEENS4_IT_T0_EESI_SI_SJ_
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB9foe220100ERKS6_S9_
+ __ZNSt12length_errorC1B9foe220100EPKc
+ __ZNSt12out_of_rangeC1B9foe220100EPKc
+ __ZNSt14overflow_errorC1B9foe220100EPKc
+ __ZNSt3__110__function12__value_funcIFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink19TappedAudioProducerENS_14default_deleteIS6_EEEEiEERKN2CA17StreamDescriptionERKNSB_13ChannelLayoutEiRKNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEEC2B9foe220100ERKST_
+ __ZNSt3__110__function12__value_funcIFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink19TappedAudioProducerENS_14default_deleteIS6_EEEEiEERKN2CA17StreamDescriptionERKNSB_13ChannelLayoutEiRKNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFN5caulk8expectedINS_10unique_ptrIN2AT11Translation25AsyncAudioStreamProcessorENS_14default_deleteIS7_EEEEiEENS6_14CallTranslator5ScopeERKNS6_24TranslationConfigurationEEEC2B9foe220100ERKSI_
+ __ZNSt3__110__function12__value_funcIFN5caulk8expectedINS_10unique_ptrIN2AT11Translation25AsyncAudioStreamProcessorENS_14default_deleteIS7_EEEEiEENS6_14CallTranslator5ScopeERKNS6_24TranslationConfigurationEEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFN5caulk8expectedIbiEEjEEC2B9foe220100ERKS6_
+ __ZNSt3__110__function12__value_funcIFN5caulk8expectedIbiEEjEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFNS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS3_EEEERK14AQMEIO_BindingRiEEC2B9foe220100ERKSC_
+ __ZNSt3__110__function12__value_funcIFNS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS3_EEEERK14AQMEIO_BindingRiEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEvEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFNS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEvEEC2B9foe220100ERKSE_
+ __ZNSt3__110__function12__value_funcIFNS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEvEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES8_EEN10applesauce2CF7TypeRefESC_EEC2B9foe220100ERKSE_
+ __ZNSt3__110__function12__value_funcIFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES8_EEN10applesauce2CF7TypeRefESC_EED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFP10MarshallervEEC2B9foe220100ERKS5_
+ __ZNSt3__110__function12__value_funcIFP10MarshallervEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFPK10__CFStringS4_EEC2B9foe220100ERKS6_
+ __ZNSt3__110__function12__value_funcIFPK10__CFStringS4_EED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFR26MutedSpeechActivityManagervEEC2B9foe220100ERKS5_
+ __ZNSt3__110__function12__value_funcIFR26MutedSpeechActivityManagervEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFbNS_10shared_ptrI11ClientEntryEEEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFbPKvEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFbR14AQIONodeClientEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFbRK26AudioObjectPropertyAddressEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFbRmbEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFbjRKN15CAListenerProxy15HALNotificationEEEC2B9foe220100ERKS7_
+ __ZNSt3__110__function12__value_funcIFbjRKN15CAListenerProxy15HALNotificationEEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFbjiEEC2B9foe220100ERKS3_
+ __ZNSt3__110__function12__value_funcIFbjiEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFbvEEC2B9foe220100ERKS3_
+ __ZNSt3__110__function12__value_funcIFbvEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFiN10applesauce3xpc6objectEEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFiP7__sFILEEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFivEEC2B9foe220100ERKS3_
+ __ZNSt3__110__function12__value_funcIFivEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFvN2AT11Translation14CallTranslator5ScopeENS3_17AudioInjectorModeEEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFvN5caulk14cf_preferences9log_levelEEEC2B9foe220100ERKS6_
+ __ZNSt3__110__function12__value_funcIFvN5caulk14cf_preferences9log_levelEEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFvNS_6chrono10time_pointINS2_12steady_clockENS2_8durationIxNS_5ratioILl1ELl1000000000EEEEEEERK15AudioBufferListiEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFvPK14MIDIPacketListEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFvR11IAQMEDeviceEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFvbEEC2B9foe220100ERKS3_
+ __ZNSt3__110__function12__value_funcIFvbEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFvdEEC2B9foe220100ERKS3_
+ __ZNSt3__110__function12__value_funcIFvdEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFvvEEC2B9foe220100EOS3_
+ __ZNSt3__110__function12__value_funcIFvvEEC2B9foe220100ERKS3_
+ __ZNSt3__110__function12__value_funcIFvvEED2B9foe220100Ev
+ __ZNSt3__110__function12__value_funcIFvxEEC2B9foe220100ERKS3_
+ __ZNSt3__110__function12__value_funcIFvxEED2B9foe220100Ev
+ __ZNSt3__110__function6__funcIZN13ServerManager13setupListenerEvE3$_6FvbEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN13ServerManager13setupListenerEvE3$_6FvbEE7destroyEv
+ __ZNSt3__110__function6__funcIZN13ServerManager13setupListenerEvE3$_6FvbEED0Ev
+ __ZNSt3__110__function6__funcIZN13ServerManager13setupListenerEvE3$_6FvbEED1Ev
+ __ZNSt3__110__function6__funcIZN13ServerManager13setupListenerEvE3$_6FvbEEclEOb
+ __ZNSt3__110__function6__funcIZN13ServerManager25handleRouteChangeForEntryENS_10shared_ptrI11ClientEntryEEP8NSStringNS_8optionalIbEEE3$_0FvbEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN13ServerManager25handleRouteChangeForEntryENS_10shared_ptrI11ClientEntryEEP8NSStringNS_8optionalIbEEE3$_0FvbEE7destroyEv
+ __ZNSt3__110__function6__funcIZN13ServerManager25handleRouteChangeForEntryENS_10shared_ptrI11ClientEntryEEP8NSStringNS_8optionalIbEEE3$_0FvbEED0Ev
+ __ZNSt3__110__function6__funcIZN13ServerManager25handleRouteChangeForEntryENS_10shared_ptrI11ClientEntryEEP8NSStringNS_8optionalIbEEE3$_0FvbEED1Ev
+ __ZNSt3__110__function6__funcIZN13ServerManager25handleRouteChangeForEntryENS_10shared_ptrI11ClientEntryEEP8NSStringNS_8optionalIbEEE3$_0FvbEEclEOb
+ __ZNSt3__110__function6__funcIZN5CALog5Scope34SetPriorityThresholdFromPreferenceEPK10__CFStringS6_E3$_0FvN5caulk14cf_preferences9log_levelEEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN5CALog5Scope34SetPriorityThresholdFromPreferenceEPK10__CFStringS6_E3$_0FvN5caulk14cf_preferences9log_levelEEE7destroyEv
+ __ZNSt3__110__function6__funcIZN5CALog5Scope34SetPriorityThresholdFromPreferenceEPK10__CFStringS6_E3$_0FvN5caulk14cf_preferences9log_levelEEED0Ev
+ __ZNSt3__110__function6__funcIZN5CALog5Scope34SetPriorityThresholdFromPreferenceEPK10__CFStringS6_E3$_0FvN5caulk14cf_preferences9log_levelEEED1Ev
+ __ZNSt3__110__function6__funcIZN5CALog5Scope34SetPriorityThresholdFromPreferenceEPK10__CFStringS6_E3$_0FvN5caulk14cf_preferences9log_levelEEEclEOSA_
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerINS3_9log_levelEEEbPK10__CFStringS9_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSB_EEEEUlSE_E_FbSE_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerINS3_9log_levelEEEbPK10__CFStringS9_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSB_EEEEUlSE_E_FbSE_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerINS3_9log_levelEEEbPK10__CFStringS9_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSB_EEEEUlSE_E_FbSE_EED0Ev
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerINS3_9log_levelEEEbPK10__CFStringS9_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSB_EEEEUlSE_E_FbSE_EED1Ev
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerINS3_9log_levelEEEbPK10__CFStringS9_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSB_EEEEUlSE_E_FbSE_EEclEOSE_
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIbEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIbEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIbEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EED0Ev
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIbEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EED1Ev
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIbEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EEclEOSD_
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIdEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIdEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIdEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EED0Ev
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIdEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EED1Ev
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIdEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EEclEOSD_
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIxEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIxEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIxEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EED0Ev
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIxEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EED1Ev
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIxEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EEclEOSD_
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RbEUlbE_FvbEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RbEUlbE_FvbEE7destroyEv
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RbEUlbE_FvbEED0Ev
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RbEUlbE_FvbEED1Ev
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RbEUlbE_FvbEEclEOb
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RfEUldE_FvdEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RfEUldE_FvdEE7destroyEv
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RfEUldE_FvdEED0Ev
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RfEUldE_FvdEED1Ev
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RfEUldE_FvdEEclEOd
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RiEUlxE_FvxEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RiEUlxE_FvxEE7destroyEv
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RiEUlxE_FvxEED0Ev
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RiEUlxE_FvxEED1Ev
+ __ZNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RiEUlxE_FvxEEclEOx
+ __ZNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERKNS_10shared_ptrI11SynthOutputEEEUlvE_FvvEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERKNS_10shared_ptrI11SynthOutputEEEUlvE_FvvEE7destroyEv
+ __ZNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERKNS_10shared_ptrI11SynthOutputEEEUlvE_FvvEED0Ev
+ __ZNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERKNS_10shared_ptrI11SynthOutputEEEUlvE_FvvEED1Ev
+ __ZNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERKNS_10shared_ptrI11SynthOutputEEEUlvE_FvvEEclEv
+ __ZNSt3__110__list_impI15SystemSoundInfoNS_9allocatorIS1_EEE13__create_nodeB9foe220100IJRKS1_EEEPNS_11__list_nodeIS1_PvEEPNS_16__list_node_baseIS1_S9_EESE_DpOT_
+ __ZNSt3__110__list_impIN13ServerManager12SynthCommandEN5caulk12rt_allocatorIS2_EEE13__create_nodeB9foe220100IJRKS2_EEEPNS_11__list_nodeIS2_PvEEPNS_16__list_node_baseIS2_SB_EESG_DpOT_
+ __ZNSt3__110shared_ptrI11AQTapIONodeEC2B9foe220100IS1_PFvP8AQIONodeELi0EEEPT_T0_
+ __ZNSt3__110shared_ptrI11SynthOutputE18__enable_weak_thisB9foe220100IS1_S1_Li0EEEvPKNS_23enable_shared_from_thisIT_EEPT0_
+ __ZNSt3__110shared_ptrI18AQMixEngine_SingleEC2B9foe220100IS1_PFvP8AQIONodeELi0EEEPT_T0_
+ __ZNSt3__110shared_ptrI19AQMixEngine_OfflineEC2B9foe220100IS1_PFvP8AQIONodeELi0EEEPT_T0_
+ __ZNSt3__110shared_ptrI21ThreadSafeHeadTrackerE18__enable_weak_thisB9foe220100IS1_S1_Li0EEEvPKNS_23enable_shared_from_thisIT_EEPT0_
+ __ZNSt3__110shared_ptrIN2AQ3API5QueueEEC2B9foe220100IS3_Li0EEERKNS_8weak_ptrIT_EE
+ __ZNSt3__110shared_ptrIN2AQ3API9SubmixTapEEC2B9foe220100IS3_Li0EEERKNS_8weak_ptrIT_EE
+ __ZNSt3__110shared_ptrIN2AT9IOBinding4ImplEE18__enable_weak_thisB9foe220100IS3_S3_Li0EEEvPKNS_23enable_shared_from_thisIT_EEPT0_
+ __ZNSt3__110unique_ptrI12CASerializerNS_14default_deleteIS1_EEE5resetB9foe220100EPS1_
+ __ZNSt3__110unique_ptrI13XOSTransactorNS_14default_deleteIS1_EEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrI14AQClientBufferN2AQ3API13BufferDeleterEE5resetB9foe220100EPS1_
+ __ZNSt3__110unique_ptrI14CADeserializerNS_14default_deleteIS1_EEE5resetB9foe220100EPS1_
+ __ZNSt3__110unique_ptrI14CAMemoryStreamNS_14default_deleteIS1_EEE5resetB9foe220100EPS1_
+ __ZNSt3__110unique_ptrI14InputConverterNS_14default_deleteIS1_EEE5resetB9foe220100EPS1_
+ __ZNSt3__110unique_ptrI14MixTapToUplinkNS_14default_deleteIS1_EEE5resetB9foe220100EPS1_
+ __ZNSt3__110unique_ptrI14__CFReadStreamN10applesauce4raii2v16detail23opaque_deletion_functorIPS1_XadL_Z9CFReleaseEEEEE5resetB9foe220100ES7_
+ __ZNSt3__110unique_ptrI16SSSVibrationDataNS_14default_deleteIS1_EEE5resetB9foe220100EPS1_
+ __ZNSt3__110unique_ptrI16SSSVibrationDataNS_14default_deleteIS1_EEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrI17AudioEventManagerNS_14default_deleteIS1_EEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrI17AudioTapInterfaceNS_14default_deleteIS1_EEE5resetB9foe220100EPS1_
+ __ZNSt3__110unique_ptrI17AudioTapSpecifierNS_14default_deleteIS1_EEE5resetB9foe220100EPS1_
+ __ZNSt3__110unique_ptrI18AudioRingAllocatorNS_14default_deleteIS1_EEE5resetB9foe220100EPS1_
+ __ZNSt3__110unique_ptrI18VADPropertyManagerNS_14default_deleteIS1_EEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrI19MESchedulingVectorsNS_14default_deleteIS1_EEE5resetB9foe220100EPS1_
+ __ZNSt3__110unique_ptrI19OpaqueAudioCapturerN10applesauce4raii2v16detail23opaque_deletion_functorIPS1_XadL_ZL25soft_AudioCapturerDestroyS7_EEEEE5resetB9foe220100ES7_
+ __ZNSt3__110unique_ptrI20AudioCapturerManagerNS_14default_deleteIS1_EEE5resetB9foe220100EPS1_
+ __ZNSt3__110unique_ptrI20AudioImpulseInjectorNS_14default_deleteIS1_EEE5resetB9foe220100EPS1_
+ __ZNSt3__110unique_ptrI26SSClientCompletionProcInfoNS_14default_deleteIS1_EEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrI27SpatialTrackingServiceProxyNS_14default_deleteIS1_EEE5resetB9foe220100EPS1_
+ __ZNSt3__110unique_ptrI28OpaqueAudioComponentInstanceN10applesauce4raii2v16detail23opaque_deletion_functorIPS1_XadL_Z29AudioComponentInstanceDisposeEEEEE5resetB9foe220100ES7_
+ __ZNSt3__110unique_ptrI29ATSecureExternalDeviceManagerNS_14default_deleteIS1_EEE5resetB9foe220100EPS1_
+ __ZNSt3__110unique_ptrI30ProductTuningAdjustmentManagerNS_14default_deleteIS1_EEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrI7__sFILENS_8functionIFiPS1_EEEE5resetB9foe220100ES3_
+ __ZNSt3__110unique_ptrI8XPromiseNS_14default_deleteIS1_EEE5resetB9foe220100EPS1_
+ __ZNSt3__110unique_ptrIKvN10applesauce4raii2v16detail23opaque_deletion_functorIPS1_XadL_Z9CFReleaseEEEEE5resetB9foe220100ES7_
+ __ZNSt3__110unique_ptrIN11AQMEIO_Base12IOSuspensionENS_14default_deleteIS2_EEE5resetB9foe220100EPS2_
+ __ZNSt3__110unique_ptrIN11HeadTracker18HeadTrackerSessionENS_14default_deleteIS2_EEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrIN14MixTapToUplink16AQMETapConnectorENS_14default_deleteIS2_EEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrIN14MixTapToUplink27UplinkSpeechMixerCPPWrapperENS_14default_deleteIS2_EEE5resetB9foe220100EPS2_
+ __ZNSt3__110unique_ptrIN14MixTapToUplink28AQIONodeClientForInternalTapENS_14default_deleteIS2_EEE5resetB9foe220100EPS2_
+ __ZNSt3__110unique_ptrIN14MixTapToUplink41RAIIUnregisterMutedSpeechActivityListenerENS_14default_deleteIS2_EEE5resetB9foe220100EPS2_
+ __ZNSt3__110unique_ptrIN14SpeechDetector18SpeechDetectorImplENS_14default_deleteIS2_EEE5resetB9foe220100EPS2_
+ __ZNSt3__110unique_ptrIN17AudioTapInterface4ImplENS_14default_deleteIS2_EEE5resetB9foe220100EPS2_
+ __ZNSt3__110unique_ptrIN18ATSecureVADManager4ImplENS_14default_deleteIS2_EEE5resetB9foe220100EPS2_
+ __ZNSt3__110unique_ptrIN18MixTapToUplinkHost46MixTapToUplinkGroupedByMicrophoneInjectionModeENS_14default_deleteIS2_EEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrIN18PowerUsageWatchdog23AudioSessionDescriptionENS_14default_deleteIS2_EEE5resetB9foe220100EPS2_
+ __ZNSt3__110unique_ptrIN18PowerUsageWatchdog4ImplENS_14default_deleteIS2_EEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrIN29ATSecureExternalDeviceManager4ImplENS_14default_deleteIS2_EEE5resetB9foe220100EPS2_
+ __ZNSt3__110unique_ptrIN2AQ6Server12RemoteClientENS_14default_deleteIS3_EEE5resetB9foe220100EPS3_
+ __ZNSt3__110unique_ptrIN2AT10RingBufferENS_14default_deleteIS2_EEE5resetB9foe220100EPS2_
+ __ZNSt3__110unique_ptrIN2AT11Translation14CallTranslatorENS_14default_deleteIS3_EEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrIN2AT11Translation19AUAsyncRendererHostENS_14default_deleteIS3_EEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrIN2AT11Translation24AudioTranslationInjectorENS_14default_deleteIS3_EEE5resetB9foe220100EPS3_
+ __ZNSt3__110unique_ptrIN2AT11Translation25BlurringMixerDSPGraphHost20ATBlurMixerInterfaceENS_14default_deleteIS4_EEE5resetB9foe220100EPS4_
+ __ZNSt3__110unique_ptrIN2AT11Translation25BlurringMixerDSPGraphHostENS_14default_deleteIS3_EEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrIN2AT11Translation27TranslationFeedbackInjectorENS_14default_deleteIS3_EEE5resetB9foe220100EPS3_
+ __ZNSt3__110unique_ptrIN2AT14AudioTapClient4ImplENS_14default_deleteIS3_EEE5resetB9foe220100EPS3_
+ __ZNSt3__110unique_ptrIN2CA16AudioBuffersBaseENS_14default_deleteIS2_EEE5resetB9foe220100EPS2_
+ __ZNSt3__110unique_ptrIN2CA22AudioBuffersDeprecatedENS_14default_deleteIS2_EEE5resetB9foe220100EPS2_
+ __ZNSt3__110unique_ptrIN2CA22AudioBuffersDeprecatedENS_14default_deleteIS2_EEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrIN5Phase13ServerManagerENS_14default_deleteIS2_EEE5resetB9foe220100EPS2_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeI27AVHapticPlayerParameterTypeN20HapticEventConverter23CurveConsolidationStateEEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN20AudioImpulseInjector4Impl20NotificationListener17NotificationStateEEEPvEENS_22__hash_node_destructorINS6_ISF_EEEEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIPK15AudioBufferListNS_4pairINS_6chrono10time_pointINS7_12steady_clockENS7_8durationIxNS_5ratioILl1ELl1000000000EEEEEEEU8__strongP16AVAudioPCMBufferEEEEPvEENS_22__hash_node_destructorINS_9allocatorISL_EEEEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS0_I26SSClientCompletionProcInfoNS_14default_deleteIS3_EEEEEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE8LocalityEEPvEENS_22__tree_node_destructorINS6_ISC_EEEEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29NewNotificationCenterObserverEEEEPvEENS_22__tree_node_destructorINS6_ISE_EEEEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29OldNotificationCenterObserverEEEEPvEENS_22__tree_node_destructorINS6_ISE_EEEEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES8_EEPvEENS_22__tree_node_destructorINS6_ISB_EEEEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrINS_15__thread_structENS_14default_deleteIS1_EEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrINS_5tupleIJN5caulk6thread10attributesEZN2AQ3API20ProcessingTapManager7RTStateC1ERKN10applesauce3xpc6objectERNS6_23ProcessingTapAttributesERiE3$_0NS1_IJEEEEEENS_14default_deleteISJ_EEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrINS_5tupleIJNS0_INS_15__thread_structENS_14default_deleteIS2_EEEEZN2AQ3API5Queue7DestroyEvE3$_0EEENS3_ISA_EEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrIZN10applesauce8dispatch2v15asyncI14SystemListenerEEvNS_10shared_ptrIT_EEPU28objcproto17OS_dispatch_queue8NSObjectU13block_pointerFvvEEUlvE_NS_14default_deleteISE_EEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrIZN20CAOrientationManager14UpdateHandlersENS1_11HandlerTypeEE3$_0NS_14default_deleteIS3_EEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrIZN20CAOrientationManager23AddUIOrientationHandlerEPK10__CFStringU13block_pointerFv13CAOrientationEE3$_0NS_14default_deleteIS8_EEED1B9foe220100Ev
+ __ZNSt3__110unique_ptrIZN20CAOrientationManager27AddDeviceOrientationHandlerEPK10__CFStringU13block_pointerFv13CAOrientationEE3$_0NS_14default_deleteIS8_EEED1B9foe220100Ev
+ __ZNSt3__111__formatter14__write_stringB9foe220100IcNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp0_ENS_17basic_string_viewIT_NS_11char_traitsIS9_EEEET0_NS_13__format_spec23__parsed_specificationsIS9_EE
+ __ZNSt3__111__formatter16__format_integerB9foe220100IjPccNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT2_8iteratorET_RSA_NS_13__format_spec23__parsed_specificationsIT1_EEbT0_SI_PKci
+ __ZNSt3__111__formatter16__format_integerB9foe220100IjcNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT1_8iteratorET_RS9_NS_13__format_spec23__parsed_specificationsIT0_EEb
+ __ZNSt3__111__formatter16__format_integerB9foe220100ImPccNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT2_8iteratorET_RSA_NS_13__format_spec23__parsed_specificationsIT1_EEbT0_SI_PKci
+ __ZNSt3__111__formatter16__format_integerB9foe220100IoPccNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT2_8iteratorET_RSA_NS_13__format_spec23__parsed_specificationsIT1_EEbT0_SI_PKci
+ __ZNSt3__111__formatter16__format_integerB9foe220100IocNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT1_8iteratorET_RS9_NS_13__format_spec23__parsed_specificationsIT0_EEb
+ __ZNSt3__111__formatter16__format_integerB9foe220100IyPccNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT2_8iteratorET_RSA_NS_13__format_spec23__parsed_specificationsIT1_EEbT0_SI_PKci
+ __ZNSt3__111__formatter16__format_integerB9foe220100IycNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT1_8iteratorET_RS9_NS_13__format_spec23__parsed_specificationsIT0_EEb
+ __ZNSt3__111__formatter19__write_transformedB9foe220100IPcccPFccENS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp1_ET_SB_T3_NS_13__format_spec23__parsed_specificationsIT1_EET2_
+ __ZNSt3__111__formatter25__write_escaped_code_unitB9foe220100IcEEvRNS_12basic_stringIT_NS_11char_traitsIS3_EENS_9allocatorIS3_EEEEDiPKS3_
+ __ZNSt3__111__formatter27__write_string_no_precisionB9foe220100IcNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp0_ENS_17basic_string_viewIT_NS_11char_traitsIS9_EEEET0_NS_13__format_spec23__parsed_specificationsIS9_EE
+ __ZNSt3__111__formatter28__write_using_trailing_zerosB9foe220100IccNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp1_EPKT_SA_T1_NS_13__format_spec23__parsed_specificationsIT0_EEmSA_m
+ __ZNSt3__111__formatter29__format_locale_specific_formB9foe220100INS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEdcEET_S7_RKNS0_14__float_bufferIT0_EERKNS0_14__float_resultENS_6localeENS_13__format_spec23__parsed_specificationsIT1_EE
+ __ZNSt3__111__formatter32__write_using_decimal_separatorsB9foe220100INS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEPccEET_S8_T0_S9_S9_ONS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEET1_NS_13__format_spec23__parsed_specificationsISH_EE
+ __ZNSt3__111__formatter34__format_buffer_general_lower_caseB9foe220100IddEENS0_14__float_resultERNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter34__format_buffer_general_lower_caseB9foe220100IdeEENS0_14__float_resultERNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter34__format_buffer_general_lower_caseB9foe220100IffEENS0_14__float_resultERNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter34__format_floating_point_non_finiteB9foe220100INS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEET_S7_NS_13__format_spec23__parsed_specificationsIT0_EEbb
+ __ZNSt3__111__formatter37__format_buffer_scientific_lower_caseB9foe220100IddEENS0_14__float_resultERKNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter37__format_buffer_scientific_lower_caseB9foe220100IdeEENS0_14__float_resultERKNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter37__format_buffer_scientific_lower_caseB9foe220100IffEENS0_14__float_resultERKNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter38__format_buffer_hexadecimal_lower_caseB9foe220100IddEENS0_14__float_resultERKNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter38__format_buffer_hexadecimal_lower_caseB9foe220100IdeEENS0_14__float_resultERKNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter38__format_buffer_hexadecimal_lower_caseB9foe220100IffEENS0_14__float_resultERKNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter6__copyB9foe220100IPKcccNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp1_ET_SA_T2_
+ __ZNSt3__111__formatter6__copyB9foe220100IPcccNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp1_ET_S9_T2_
+ __ZNSt3__111__formatter6__copyB9foe220100IPcccNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp1_ET_mT2_
+ __ZNSt3__111__formatter6__fillB9foe220100IcNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEET0_S7_mNS_13__format_spec12__code_pointIT_EE
+ __ZNSt3__111__formatter7__writeB9foe220100IPKccNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp1_ET_SA_T1_NS_13__format_spec23__parsed_specificationsIT0_EEl
+ __ZNSt3__111__formatter7__writeB9foe220100IPccNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp1_ET_S9_T1_NS_13__format_spec23__parsed_specificationsIT0_EE
+ __ZNSt3__111__formatter7__writeB9foe220100IPccNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp1_ET_S9_T1_NS_13__format_spec23__parsed_specificationsIT0_EEl
+ __ZNSt3__111__formatter7__writeB9foe220100IccNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp0_ENS_17basic_string_viewIT_NS_11char_traitsIS9_EEEET1_NS_13__format_spec23__parsed_specificationsIT0_EEl
+ __ZNSt3__111__formatter8__escapeB9foe220100IcEEvRNS_12basic_stringIT_NS_11char_traitsIS3_EENS_9allocatorIS3_EEEENS_17basic_string_viewIS3_S5_EENS0_23__escape_quotation_markE
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZN17AudioTapSpecifierC1ENS_6vectorIjNS_9allocatorIjEEEENS2_12MuteBehaviorEEUlRK11AQMESessionSA_E_PS8_Lb0EEEvT1_SE_T0_NS_15iterator_traitsISE_E15difference_typeEb
+ __ZNSt3__111__sift_downB9foe220100INS_17_ClassicAlgPolicyELb0ERNS_6__lessIvvEEP10MusicEventEEvT2_OT1_NS_15iterator_traitsIS7_E15difference_typeESC_
+ __ZNSt3__111__sift_downB9foe220100INS_17_ClassicAlgPolicyELb0ERNS_6__lessIvvEEP11VolumeEventEEvT2_OT1_NS_15iterator_traitsIS7_E15difference_typeESC_
+ __ZNSt3__111__sift_downB9foe220100INS_17_ClassicAlgPolicyELb0ERNS_6__lessIvvEEP15MEVADIdentifierEEvT2_OT1_NS_15iterator_traitsIS7_E15difference_typeESC_
+ __ZNSt3__111__sift_downB9foe220100INS_17_ClassicAlgPolicyELb0ERNS_6__lessIvvEEPN14NoteOffManager11NoteOffInfoEEEvT2_OT1_NS_15iterator_traitsIS8_E15difference_typeESD_
+ __ZNSt3__111__sift_downB9foe220100INS_17_ClassicAlgPolicyELb0ERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEvT2_OT1_NS_15iterator_traitsISC_E15difference_typeESH_
+ __ZNSt3__111__sift_downB9foe220100INS_17_ClassicAlgPolicyELb0ERZN17AudioTapSpecifierC1ENS_6vectorIjNS_9allocatorIjEEEENS2_12MuteBehaviorEEUlRK11AQMESessionSA_E_PS8_EEvT2_OT1_NS_15iterator_traitsISE_E15difference_typeESJ_
+ __ZNSt3__111make_uniqueB9foe220100I17AudioTapInterfaceJ17AudioTapSpecifierELi0EEENS_10unique_ptrIT_NS_14default_deleteIS4_EEEEDpOT0_
+ __ZNSt3__111make_uniqueB9foe220100I17AudioTapInterfaceJPK8__CFDataELi0EEENS_10unique_ptrIT_NS_14default_deleteIS6_EEEEDpOT0_
+ __ZNSt3__111make_uniqueB9foe220100IN2CA22AudioBuffersDeprecatedEJRNS1_17StreamDescriptionERjELi0EEENS_10unique_ptrIT_NS_14default_deleteIS7_EEEEDpOT0_
+ __ZNSt3__111scoped_lockIJN5caulk4mach21unfair_recursive_lockEN16AudioQueueObject20WorkQueueLockAdapterEEE15__unlock_unpackB9foe220100IJLm0ELm1EEEEvNS_16integer_sequenceImJXspT_EEEERNS_5tupleIJRS3_RS5_EEE
+ __ZNSt3__111scoped_lockIJN5caulk4mach21unfair_recursive_lockENS1_23recursive_mutex_adapterINS1_22pooled_semaphore_mutexEEES3_EE15__unlock_unpackB9foe220100IJLm0ELm1ELm2EEEEvNS_16integer_sequenceImJXspT_EEEERNS_5tupleIJRS3_RS6_SC_EEE
+ __ZNSt3__111scoped_lockIJN5caulk4mach21unfair_recursive_lockENS1_23recursive_mutex_adapterINS1_22pooled_semaphore_mutexEEES3_N16AudioQueueObject20WorkQueueLockAdapterEEE15__unlock_unpackB9foe220100IJLm0ELm1ELm2ELm3EEEEvNS_16integer_sequenceImJXspT_EEEERNS_5tupleIJRS3_RS6_SE_RS8_EEE
+ __ZNSt3__111unique_lockIN5caulk4mach21unfair_recursive_lockEE4lockB9foe220100Ev
+ __ZNSt3__111unique_lockIN5caulk4mach21unfair_recursive_lockEE6unlockB9foe220100Ev
+ __ZNSt3__112__destroy_atB9foe220100I15MEVADIdentifierEEvPT_
+ __ZNSt3__112__destroy_atB9foe220100IN10applesauce2CF7TypeRefEEEvPT_
+ __ZNSt3__112__destroy_atB9foe220100IN10applesauce2CF9NumberRefEEEvPT_
+ __ZNSt3__112__destroy_atB9foe220100IN2AQ6Server12RemoteClient18ProcessingTapStateEEEvPT_
+ __ZNSt3__112__destroy_atB9foe220100IN2AU8Property10Attributes7details15AUPresetWrapperEEEvPT_
+ __ZNSt3__112__destroy_atB9foe220100IN8audioipc18SharedAudioBuffers7ElementEEEvPT_
+ __ZNSt3__112__destroy_atB9foe220100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE8LocalityEEEEvPT_
+ __ZNSt3__112__destroy_atB9foe220100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29NewNotificationCenterObserverEEEEEEvPT_
+ __ZNSt3__112__destroy_atB9foe220100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29OldNotificationCenterObserverEEEEEEvPT_
+ __ZNSt3__112__destroy_atB9foe220100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EEEEvPT_
+ __ZNSt3__112__destroy_atB9foe220100INS_4pairIKP14MEMixerChannelN9TapSubmix10InputStateEEEEEvPT_
+ __ZNSt3__112__destroy_atB9foe220100INS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EEEEvPT_
+ __ZNSt3__112__destroy_atB9foe220100INS_4pairIU8__strongKP22AVHapticServerInstanceNS_10shared_ptrI11ClientEntryEEEEEEvPT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI20HapticPlayerPriorityjEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_jEENS_4hashIS2_EENS_8equal_toIS2_EEEENS_21__unordered_map_equalIS2_S7_SB_S9_EENS_9allocatorIS7_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI20HapticPlayerPriorityjEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_jEENS_4hashIS2_EENS_8equal_toIS2_EEEENS_21__unordered_map_equalIS2_S7_SB_S9_EENS_9allocatorIS7_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI27AVHapticPlayerParameterTypeN20HapticEventConverter23CurveConsolidationStateEEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S4_EENS_4hashIS2_EENS_8equal_toIS2_EEEENS_21__unordered_map_equalIS2_S9_SD_SB_EENS_9allocatorIS9_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE26STSPerLabelControllerStateEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_S8_EENS_4hashIS7_EENS_8equal_toIS7_EEEENS_21__unordered_map_equalIS7_SD_SH_SF_EENS5_ISD_EEE21__construct_node_hashIJRSD_EEENS_10unique_ptrINS_11__hash_nodeIS9_PvEENS_22__hash_node_destructorINS5_ISS_EEEEEEmDpOT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE26STSPerLabelControllerStateEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_S8_EENS_4hashIS7_EENS_8equal_toIS7_EEEENS_21__unordered_map_equalIS7_SD_SH_SF_EENS5_ISD_EEE4findIS7_EENS_15__hash_iteratorIPNS_11__hash_nodeIS9_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE26STSPerLabelControllerStateEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_S8_EENS_4hashIS7_EENS_8equal_toIS7_EEEENS_21__unordered_map_equalIS7_SD_SH_SF_EENS5_ISD_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN20AudioImpulseInjector4Impl20NotificationListener17NotificationStateEEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_SB_EENS_4hashIS7_EENS_8equal_toIS7_EEEENS_21__unordered_map_equalIS7_SG_SK_SI_EENS5_ISG_EEE4findIS7_EENS_15__hash_iteratorIPNS_11__hash_nodeISC_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_bEENS_4hashIS7_EENS_8equal_toIS7_EEEENS_21__unordered_map_equalIS7_SC_SG_SE_EENS5_ISC_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_4pairImN18PowerUsageWatchdog13ClientRunModeEEENS_10shared_ptrINS3_17ClientDescriptionEEEEENS_22__unordered_map_hasherIS5_NS2_IKS5_S8_EENS3_4Impl9pair_hashENS_8equal_toIS5_EEEENS_21__unordered_map_equalIS5_SC_SG_SE_EENS_9allocatorISC_EEE14__assign_valueB9foe220100IRSC_S9_Li0EEEvSO_OT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_4pairImN18PowerUsageWatchdog13ClientRunModeEEENS_10shared_ptrINS3_17ClientDescriptionEEEEENS_22__unordered_map_hasherIS5_NS2_IKS5_S8_EENS3_4Impl9pair_hashENS_8equal_toIS5_EEEENS_21__unordered_map_equalIS5_SC_SG_SE_EENS_9allocatorISC_EEE16__copy_constructB9foe220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS9_PvEEEEST_m
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_4pairImN18PowerUsageWatchdog13ClientRunModeEEENS_10shared_ptrINS3_17ClientDescriptionEEEEENS_22__unordered_map_hasherIS5_NS2_IKS5_S8_EENS3_4Impl9pair_hashENS_8equal_toIS5_EEEENS_21__unordered_map_equalIS5_SC_SG_SE_EENS_9allocatorISC_EEE22__deallocate_node_listB9foe220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS9_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_4pairImN18PowerUsageWatchdog13ClientRunModeEEENS_10shared_ptrINS3_17ClientDescriptionEEEEENS_22__unordered_map_hasherIS5_NS2_IKS5_S8_EENS3_4Impl9pair_hashENS_8equal_toIS5_EEEENS_21__unordered_map_equalIS5_SC_SG_SE_EENS_9allocatorISC_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_4pairImN18PowerUsageWatchdog13ClientRunModeEEENS_10shared_ptrINS3_17ClientDescriptionEEEEENS_22__unordered_map_hasherIS5_NS2_IKS5_S8_EENS3_4Impl9pair_hashENS_8equal_toIS5_EEEENS_21__unordered_map_equalIS5_SC_SG_SE_EENS_9allocatorISC_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPK15AudioBufferListNS_4pairINS_6chrono10time_pointINS6_12steady_clockENS6_8durationIxNS_5ratioILl1ELl1000000000EEEEEEEU8__strongP16AVAudioPCMBufferEEEENS_22__unordered_map_hasherIS4_NS5_IKS4_SH_EENS_4hashIS4_EENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_SL_SP_SN_EENS_9allocatorISL_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPK15AudioBufferListNS_4pairINS_6chrono10time_pointINS6_12steady_clockENS6_8durationIxNS_5ratioILl1ELl1000000000EEEEEEEU8__strongP16AVAudioPCMBufferEEEENS_22__unordered_map_hasherIS4_NS5_IKS4_SH_EENS_4hashIS4_EENS_8equal_toIS4_EEEENS_21__unordered_map_equalIS4_SL_SP_SN_EENS_9allocatorISL_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPvN10applesauce8dispatch2v15blockIFv28AUVoiceIOSpeechActivityEventEEEEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S9_EENS_4hashIS2_EENS_8equal_toIS2_EEEENS_21__unordered_map_equalIS2_SE_SI_SG_EENS_9allocatorISE_EEE17__deallocate_nodeB9foe220100EPNS_11__hash_nodeISA_S2_EE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPvN10applesauce8dispatch2v15blockIFv28AUVoiceIOSpeechActivityEventEEEEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S9_EENS_4hashIS2_EENS_8equal_toIS2_EEEENS_21__unordered_map_equalIS2_SE_SI_SG_EENS_9allocatorISE_EEE4findIS2_EENS_15__hash_iteratorIPNS_11__hash_nodeISA_S2_EEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPvN10applesauce8dispatch2v15blockIFv28AUVoiceIOSpeechActivityEventEEEEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S9_EENS_4hashIS2_EENS_8equal_toIS2_EEEENS_21__unordered_map_equalIS2_SE_SI_SG_EENS_9allocatorISE_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeISA_S2_EEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPvN10applesauce8dispatch2v15blockIFv28AUVoiceIOSpeechActivityEventEEEEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S9_EENS_4hashIS2_EENS_8equal_toIS2_EEEENS_21__unordered_map_equalIS2_SE_SI_SG_EENS_9allocatorISE_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIijEENS_22__unordered_map_hasherIiNS_4pairIKijEENS_4hashIiEENS_8equal_toIiEEEENS_21__unordered_map_equalIiS6_SA_S8_EENS_9allocatorIS6_EEE15__emplace_multiIJNS4_IijEEEEENS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEDpOT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIijEENS_22__unordered_map_hasherIiNS_4pairIKijEENS_4hashIiEENS_8equal_toIiEEEENS_21__unordered_map_equalIiS6_SA_S8_EENS_9allocatorIS6_EEE19__equal_range_multiIiEENS4_INS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEESN_EERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIijEENS_22__unordered_map_hasherIiNS_4pairIKijEENS_4hashIiEENS_8equal_toIiEEEENS_21__unordered_map_equalIiS6_SA_S8_EENS_9allocatorIS6_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_10unique_ptrI26SSClientCompletionProcInfoNS_14default_deleteIS3_EEEEEENS_22__unordered_map_hasherIjNS_4pairIKjS6_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjSB_SF_SD_EENS_9allocatorISB_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_setIPvNS_4hashIS3_EENS_8equal_toIS3_EENS_9allocatorIS3_EEEEEENS_22__unordered_map_hasherIjNS_4pairIKjSA_EENS4_IjEENS6_IjEEEENS_21__unordered_map_equalIjSF_SH_SG_EENS8_ISF_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeISB_S3_EEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_4pairIjxEEEENS_22__unordered_map_hasherIjNS2_IKjS3_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS7_SB_S9_EENS_9allocatorIS7_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_6vectorIhNS_9allocatorIhEEEEEENS_22__unordered_map_hasherIjNS_4pairIKjS5_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjSA_SE_SC_EENS3_ISA_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjP24OpaqueMusicEventIteratorEENS_22__unordered_map_hasherIjNS_4pairIKjS3_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS8_SC_SA_EENS_9allocatorIS8_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjiEENS_22__unordered_map_hasherIjNS_4pairIKjiEENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS6_SA_S8_EENS_9allocatorIS6_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjiEENS_22__unordered_map_hasherIjNS_4pairIKjiEENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS6_SA_S8_EENS_9allocatorIS6_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImNS_10shared_ptrI14HapticSequenceEEEENS_22__unordered_map_hasherImNS_4pairIKmS4_EENS_4hashImEENS_8equal_toImEEEENS_21__unordered_map_equalImS9_SD_SB_EENS_9allocatorIS9_EEE22__deallocate_node_listB9foe220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS5_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImNS_10shared_ptrI14HapticSequenceEEEENS_22__unordered_map_hasherImNS_4pairIKmS4_EENS_4hashImEENS_8equal_toImEEEENS_21__unordered_map_equalImS9_SD_SB_EENS_9allocatorIS9_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImNS_8optionalI28AUVoiceIOSpeechActivityEventEEEENS_22__unordered_map_hasherImNS_4pairIKmS4_EENS_4hashImEENS_8equal_toImEEEENS_21__unordered_map_equalImS9_SD_SB_EENS_9allocatorIS9_EEE4findImEENS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImU13block_pointerFv28AUVoiceIOSpeechActivityEventEEENS_22__unordered_map_hasherImNS_4pairIKmS4_EENS_4hashImEENS_8equal_toImEEEENS_21__unordered_map_equalImS9_SD_SB_EENS_9allocatorIS9_EEE4findImEENS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImbEENS_22__unordered_map_hasherImNS_4pairIKmbEENS_4hashImEENS_8equal_toImEEEENS_21__unordered_map_equalImS6_SA_S8_EEN5caulk12rt_allocatorIS6_EEE22__deallocate_node_listB9foe220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS2_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImbEENS_22__unordered_map_hasherImNS_4pairIKmbEENS_4hashImEENS_8equal_toImEEEENS_21__unordered_map_equalImS6_SA_S8_EEN5caulk12rt_allocatorIS6_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS2_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImbEENS_22__unordered_map_hasherImNS_4pairIKmbEENS_4hashImEENS_8equal_toImEEEENS_21__unordered_map_equalImS6_SA_S8_EEN5caulk12rt_allocatorIS6_EEED2Ev
+ __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEC2ERKS7_
+ __ZNSt3__112__tuple_implINS_18__integer_sequenceImJLm0ELm1ELm2EEEEJN10applesauce3xpc6objectEN4swix6stringEjEEC2EOS8_
+ __ZNSt3__112__tuple_implINS_18__integer_sequenceImJLm0ELm1ELm2ELm3ELm4EEEEJN10applesauce3xpc6objectEjjbNS_6vectorIjNS_9allocatorIjEEEEEEC2EOSA_
+ __ZNSt3__112__tuple_implINS_18__integer_sequenceImJLm0ELm1ELm2ELm3ELm4EEEEJN10applesauce3xpc6objectEjjbNS_6vectorIjNS_9allocatorIjEEEEEEC2ERKSA_
+ __ZNSt3__112__tuple_implINS_18__integer_sequenceImJLm0ELm1ELm2ELm3ELm4ELm5EEEEJjj27AudioStreamBasicDescriptionN10applesauce3xpc6objectES6_N2CA13ChannelLayoutEEEC2EOS9_
+ __ZNSt3__112__tuple_implINS_18__integer_sequenceImJLm0ELm1ELm2ELm3ELm4ELm5EEEEJjj27AudioStreamBasicDescriptionN10applesauce3xpc6objectES6_N2CA13ChannelLayoutEEEC2ERKS9_
+ __ZNSt3__112__tuple_leafILm0EN10applesauce3xpc6objectELb0EEC2B9foe220100ERKS4_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_out_of_rangeB9foe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9foe220100Em
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9foe220100ILi0EEEPKc
+ __ZNSt3__112construct_atB9foe220100I11AQMESessionJS1_EPS1_EEPT_S4_DpOT0_
+ __ZNSt3__112construct_atB9foe220100I15MEVADIdentifierJR14MEDeviceTypeIDRjRN10applesauce2CF9StringRefEEPS1_EEPT_SB_DpOT0_
+ __ZNSt3__112construct_atB9foe220100I15MEVADIdentifierJRS1_EPS1_EEPT_S5_DpOT0_
+ __ZNSt3__112construct_atB9foe220100IN10applesauce2CF9StringRefEJRKS3_EPS3_EEPT_S8_DpOT0_
+ __ZNSt3__112format_errorC1B9foe220100EPKc
+ __ZNSt3__112format_errorD0Ev
+ __ZNSt3__112format_errorD1Ev
+ __ZNSt3__112system_errorC1EiRKNS_14error_categoryE
+ __ZNSt3__112system_errorC2EiRKNS_14error_categoryE
+ __ZNSt3__112system_errorD2Ev
+ __ZNSt3__113__format_spec14__parse_arg_idB9foe220100IPKcNS_26basic_format_parse_contextIcEEEENS_8__format21__parse_number_resultIT_EES8_S8_RT0_
+ __ZNSt3__113__format_spec23__estimate_column_widthB9foe220100IcPKcEENS0_21__column_width_resultIT0_EENS_17basic_string_viewIT_NS_11char_traitsIS8_EEEEmNS0_23__column_width_roundingE
+ __ZNSt3__113__format_spec24__process_parsed_integerB9foe220100IcEEvRNS0_8__parserIT_EEPKc
+ __ZNSt3__113__format_spec33__throw_invalid_type_format_errorB9foe220100EPKc
+ __ZNSt3__113__format_spec35__throw_invalid_option_format_errorB9foe220100EPKcS2_
+ __ZNSt3__113__format_spec8__parserIcE7__parseB9foe220100INS_26basic_format_parse_contextIcEEEENT_8iteratorERS6_NS0_8__fieldsB9foe220100E
+ __ZNSt3__113__tree_removeB9foe220100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__113unordered_mapIPvN10applesauce8dispatch2v15blockIFv28AUVoiceIOSpeechActivityEventEEENS_4hashIS1_EENS_8equal_toIS1_EENS_9allocatorINS_4pairIKS1_S8_EEEEE16insert_or_assignB9foe220100IRU8__strongU13block_pointerS7_EENSE_INS_19__hash_map_iteratorINS_15__hash_iteratorIPNS_11__hash_nodeINS_17__hash_value_typeIS1_S8_EES1_EEEEEEbEERSF_OT_
+ __ZNSt3__114__thread_proxyB9foe220100INS_5tupleIJNS_10unique_ptrINS_15__thread_structENS_14default_deleteIS3_EEEEZN2AQ3API5Queue7DestroyEvE3$_0EEEEEPvSC_
+ __ZNSt3__115allocate_sharedB9foe220100I11SynthOutputNS_9allocatorIS1_EEJR17LegacyHapticSynthbELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9foe220100I14HapticSequenceNS_9allocatorIS1_EEJNS_10shared_ptrI11MuteManagerEEELi0EEENS4_IT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9foe220100I19SSClientPlayOptionsNS_9allocatorIS1_EEJRN10applesauce3xpc6objectEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9foe220100I8TFileBSDNS_9allocatorIS1_EEJRPK7__CFURLELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9foe220100IN2AQ3API9SubmixTapENS_9allocatorIS3_EEJRNS2_7ManagerERjELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9foe220100IN2AT9IOBinding4ImplENS_9allocatorIS3_EEJN10applesauce2CF9StringRefEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9foe220100IN2AT9IOBinding4ImplENS_9allocatorIS3_EEJR24ATIsolatedAudioUseCaseIDELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9foe220100IN5caulk7details19lifetime_guard_baseIN2AQ6Server12RemoteClientEE13control_blockENS_9allocatorIS8_EEJRS7_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B9foe220100Ej
+ __ZNSt3__115system_categoryEv
+ __ZNSt3__116__if_likely_elseB9foe220100IZNS_6vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS4_EEE12emplace_backIJS4_EEERS4_DpOT_EUlvE_ZNS8_IJS4_EEES9_SC_EUlvE0_EEvbT_T0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB9foe220100IOZNS0_6__ctorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEEE19__generic_constructB9foe220100IRKNS0_18__copy_constructorISV_LNS0_6_TraitE1EEEEEvRSW_OT_EUlS15_E_JRKNS0_6__baseILSZ_1EJSE_SM_SS_SU_EEEEEEDcS14_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB9foe220100IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN15AQProcessingTap10DirectImplEEEELNS0_6_TraitE1EE9__destroyB9foe220100EvEUlRT_E_JRNS0_6__baseILSC_1EJS8_SA_EEEEEEDcSE_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB9foe220100IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AQ6Server11XPCListenerENSA_9IPCBypassEEEELNS0_6_TraitE1EE9__destroyB9foe220100EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB9foe220100IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AT13SessionFacade7ManagerENSA_11ManagerBaseEEEELNS0_6_TraitE1EE9__destroyB9foe220100EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB9foe220100IOZNS0_6__dtorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEELNS0_6_TraitE1EE9__destroyB9foe220100EvEUlRT_E_JRNS0_6__baseILSW_1EJSE_SM_SS_SU_EEEEEEDcSY_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB9foe220100IOZNS0_6__ctorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEEE19__generic_constructB9foe220100IRKNS0_18__copy_constructorISV_LNS0_6_TraitE1EEEEEvRSW_OT_EUlS15_E_JRKNS0_6__baseILSZ_1EJSE_SM_SS_SU_EEEEEEDcS14_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB9foe220100IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN15AQProcessingTap10DirectImplEEEELNS0_6_TraitE1EE9__destroyB9foe220100EvEUlRT_E_JRNS0_6__baseILSC_1EJS8_SA_EEEEEEDcSE_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB9foe220100IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AQ6Server11XPCListenerENSA_9IPCBypassEEEELNS0_6_TraitE1EE9__destroyB9foe220100EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB9foe220100IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AT13SessionFacade7ManagerENSA_11ManagerBaseEEEELNS0_6_TraitE1EE9__destroyB9foe220100EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB9foe220100IOZNS0_6__dtorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEELNS0_6_TraitE1EE9__destroyB9foe220100EvEUlRT_E_JRNS0_6__baseILSW_1EJSE_SM_SS_SU_EEEEEEDcSY_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB9foe220100IOZNS0_6__ctorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEEE19__generic_constructB9foe220100IRKNS0_18__copy_constructorISV_LNS0_6_TraitE1EEEEEvRSW_OT_EUlS15_E_JRKNS0_6__baseILSZ_1EJSE_SM_SS_SU_EEEEEEDcS14_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB9foe220100IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AQ6Server11XPCListenerENSA_9IPCBypassEEEELNS0_6_TraitE1EE9__destroyB9foe220100EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB9foe220100IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AT13SessionFacade7ManagerENSA_11ManagerBaseEEEELNS0_6_TraitE1EE9__destroyB9foe220100EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB9foe220100IOZNS0_6__dtorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEELNS0_6_TraitE1EE9__destroyB9foe220100EvEUlRT_E_JRNS0_6__baseILSW_1EJSE_SM_SS_SU_EEEEEEDcSY_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB9foe220100IOZNS0_6__ctorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEEE19__generic_constructB9foe220100IRKNS0_18__copy_constructorISV_LNS0_6_TraitE1EEEEEvRSW_OT_EUlS15_E_JRKNS0_6__baseILSZ_1EJSE_SM_SS_SU_EEEEEEDcS14_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB9foe220100IOZNS0_6__dtorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEELNS0_6_TraitE1EE9__destroyB9foe220100EvEUlRT_E_JRNS0_6__baseILSW_1EJSE_SM_SS_SU_EEEEEEDcSY_DpT0_
+ __ZNSt3__116__variant_detail18__copy_constructorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS3_S5_S7_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvS5_S7_EEENSL_IFvS5_S7_SC_jSF_EEEEEELNS0_6_TraitE1EEC2B9foe220100ERKSS_
+ __ZNSt3__116__variant_detail6__dtorINS0_8__traitsIJNS_9monostateEN15AQProcessingTap10DirectImplEEEELNS0_6_TraitE1EE9__destroyB9foe220100Ev
+ __ZNSt3__116__variant_detail6__dtorINS0_8__traitsIJNS_9monostateEN2AQ6Server11XPCListenerENS5_9IPCBypassEEEELNS0_6_TraitE1EE9__destroyB9foe220100Ev
+ __ZNSt3__116__variant_detail6__dtorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS3_S5_S7_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvS5_S7_EEENSL_IFvS5_S7_SC_jSF_EEEEEELNS0_6_TraitE1EE9__destroyB9foe220100Ev
+ __ZNSt3__116allocator_traitsIN5caulk12rt_allocatorI11VolumeEventEEE17allocate_at_leastB9foe220100IS4_EENS_17allocation_resultIPS3_mEERT_m
+ __ZNSt3__116allocator_traitsIN5caulk12rt_allocatorINS_4pairIPFiPvPjPK14AudioTimeStampjjP15AudioBufferListES4_EEEEE17allocate_at_leastB9foe220100ISE_EENS_17allocation_resultIPSD_mEERT_m
+ __ZNSt3__116allocator_traitsIN5caulk12rt_allocatorINS_4pairIffEEEEE17allocate_at_leastB9foe220100IS5_EENS_17allocation_resultIPS4_mEERT_m
+ __ZNSt3__116allocator_traitsINS_9allocatorI11AQMESessionEEE7destroyB9foe220100IS2_Li0EEEvRS3_PT_
+ __ZNSt3__116allocator_traitsINS_9allocatorI15MEVADIdentifierEEE9constructB9foe220100IS2_J14MEDeviceTypeID3$_1RPK10__CFStringELi0EEEvRS3_PT_DpOT0_
+ __ZNSt3__116allocator_traitsINS_9allocatorI9TapSourceEEE7destroyB9foe220100IS2_Li0EEEvRS3_PT_
+ __ZNSt3__116allocator_traitsINS_9allocatorI9TapSourceEEE9constructB9foe220100IS2_JS2_ELi0EEEvRS3_PT_DpOT0_
+ __ZNSt3__116allocator_traitsINS_9allocatorIN10applesauce2CF11TypeRefPairEEEE7destroyB9foe220100IS4_Li0EEEvRS5_PT_
+ __ZNSt3__116allocator_traitsINS_9allocatorIN10applesauce2CF11TypeRefPairEEEE9constructB9foe220100IS4_JRKNS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEERKNS3_7TypeRefEELi0EEEvRS5_PT_DpOT0_
+ __ZNSt3__116allocator_traitsINS_9allocatorIN10applesauce2CF7TypeRefEEEE9constructB9foe220100IS4_JdELi0EEEvRS5_PT_DpOT0_
+ __ZNSt3__116allocator_traitsINS_9allocatorIN10applesauce2CF9NumberRefEEEE9constructB9foe220100IS4_JjELi0EEEvRS5_PT_DpOT0_
+ __ZNSt3__116allocator_traitsINS_9allocatorIN21IPCAUSharedMemoryBase7ElementEEEE7destroyB9foe220100IS3_Li0EEEvRS4_PT_
+ __ZNSt3__116allocator_traitsINS_9allocatorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEEEEE7destroyB9foe220100ISD_Li0EEEvRSE_PT_
+ __ZNSt3__116allocator_traitsINS_9allocatorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEEEEE9constructB9foe220100ISD_JSD_ELi0EEEvRSE_PT_DpOT0_
+ __ZNSt3__117__call_once_proxyB9foe220100INS_5tupleIJOZ31SetupSystemSoundClientLogScopesvE3$_0EEEEEvPv
+ __ZNSt3__117__call_once_proxyB9foe220100INS_5tupleIJOZN11AQAC3IONodeC1ERK14AQMEIO_Binding14MEStreamTypeIDRidE3$_0EEEEEvPv
+ __ZNSt3__117__call_once_proxyB9foe220100INS_5tupleIJOZN11SSServerIPCC1EvE3$_0EEEEEvPv
+ __ZNSt3__117__call_once_proxyB9foe220100INS_5tupleIJOZN12CADeprecated10TSingletonI11SSClientIPCE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB9foe220100INS_5tupleIJOZN12CADeprecated10TSingletonI14RemoteIOServerE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB9foe220100INS_5tupleIJOZN12CADeprecated10TSingletonI15ActiveSoundListE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB9foe220100INS_5tupleIJOZN12CADeprecated10TSingletonI18SSClientCompletionE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB9foe220100INS_5tupleIJOZN12CADeprecated10TSingletonI19HapticServerManagerE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB9foe220100INS_5tupleIJOZN12CADeprecated10TSingletonI20SSSCallbackMessengerE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB9foe220100INS_5tupleIJOZN12CADeprecated10TSingletonI21CAExternalLockJanitorE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB9foe220100INS_5tupleIJOZN12CADeprecated10TSingletonI8SSServerE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB9foe220100INS_5tupleIJOZN12CADeprecated10TSingletonIN12_GLOBAL__N_118CoreMotionSoftlinkEE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB9foe220100INS_5tupleIJOZN12CADeprecated10TSingletonIN15CAListenerProxy13ZombieJanitorEE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB9foe220100INS_5tupleIJOZN12CADeprecated10TSingletonIN20AudioImpulseInjector4Impl20NotificationListenerEE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB9foe220100INS_5tupleIJOZN18AQOfflineMixerBaseC1ER15AQIONodeManageriRK27AudioStreamBasicDescriptionRKN2CA13ChannelLayoutERiE3$_0EEEEEvPv
+ __ZNSt3__117__call_once_proxyB9foe220100INS_5tupleIJOZN20CA_UISoundClientBaseC1EdjPK14__CFDictionaryjN10applesauce2CF7TypeRefEibE3$_0EEEEEvPv
+ __ZNSt3__117__call_once_proxyB9foe220100INS_5tupleIJOZN2AQ3API9Interface31AudioQueueGetPassThroughFormatsEvE3$_0EEEEEvPv
+ __ZNSt3__118__formatter_stringIcE5parseB9foe220100INS_26basic_format_parse_contextIcEEEENT_8iteratorERS5_
+ __ZNSt3__118__set_intersectionB9foe220100INS_17_ClassicAlgPolicyENS_6__lessIvvEENS_21__hash_const_iteratorIPNS_11__hash_nodeIjPvEEEES9_S9_S9_NS_20back_insert_iteratorINS_6vectorIjNS_9allocatorIjEEEEEEEENS_25__set_intersection_resultIT1_T3_T5_EESH_T2_SI_T4_SJ_OT0_NS_20forward_iterator_tagESP_
+ __ZNSt3__118__visit_format_argB9foe220100IZNS_13__format_spec19__substitute_arg_idB9foe220100INS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEEjNS_16basic_format_argIT_EEEUlSB_E_S9_EEDcOSB_NSA_IT0_EE
+ __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9foe220100Ev
+ __ZNSt3__119__shared_weak_count16__release_sharedB9foe220100Ev
+ __ZNSt3__119__to_chars_integralB9foe220100IyLi0EEENS_17__to_chars_resultEPcS2_T_i
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9foe220100Ev
+ __ZNSt3__120__optional_copy_baseIN2CA13ChannelLayoutELb0EEC2B9foe220100ERKS3_
+ __ZNSt3__120__optional_copy_baseINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEELb0EEC2B9foe220100ERKS7_
+ __ZNSt3__120__shared_ptr_emplaceI13HapticMetricsNS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceI13HapticMetricsNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceI13HapticMetricsNS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceI13HapticMetricsNS_9allocatorIS1_EEED1Ev
+ __ZNSt3__120__shared_ptr_emplaceI18HapticAudioMetricsNS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceI18HapticAudioMetricsNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceI18HapticAudioMetricsNS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceI18HapticAudioMetricsNS_9allocatorIS1_EEED1Ev
+ __ZNSt3__120__shared_ptr_emplaceIN12CADeprecated16XMachReceivePortENS_9allocatorIS2_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceIN12CADeprecated16XMachReceivePortENS_9allocatorIS2_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceIN12CADeprecated16XMachReceivePortENS_9allocatorIS2_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceIN12CADeprecated16XMachReceivePortENS_9allocatorIS2_EEED1Ev
+ __ZNSt3__120__throw_bad_weak_ptrB9foe220100Ev
+ __ZNSt3__120__throw_format_errorB9foe220100EPKc
+ __ZNSt3__120__throw_future_errorB9foe220100ENS_11future_errcE
+ __ZNSt3__120__throw_length_errorB9foe220100EPKc
+ __ZNSt3__120__throw_out_of_rangeB9foe220100EPKc
+ __ZNSt3__120basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcE6localeB9foe220100Ev
+ __ZNSt3__122__escaped_output_table9__entriesB9foe220100E
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPvEEEEEclB9foe220100EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE26STSPerLabelControllerStateEEPvEEEEEclB9foe220100EPSC_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEbEEPvEEEEEclB9foe220100EPSB_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_4pairImN18PowerUsageWatchdog13ClientRunModeEEENS_10shared_ptrINS5_17ClientDescriptionEEEEEPvEEEEEclB9foe220100EPSD_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIPvN10applesauce8dispatch2v15blockIFv28AUVoiceIOSpeechActivityEventEEEEES4_EEEEEclB9foe220100EPSD_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIjNS_10unique_ptrI27SSClientCompletionBlockInfoNS_14default_deleteIS5_EEEEEEPvEEEEEclB9foe220100EPSB_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIjNS_6vectorIhNS1_IhEEEEEEPvEEEEEclB9foe220100EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeImNS_10shared_ptrI14HapticSequenceEEEEPvEEEEEclB9foe220100EPS9_
+ __ZNSt3__122__indic_conjunct_break14__get_propertyB9foe220100EDi
+ __ZNSt3__122__indic_conjunct_break9__entriesB9foe220100E
+ __ZNSt3__122__lower_bound_onesidedB9foe220100INS_17_ClassicAlgPolicyENS_21__hash_const_iteratorIPNS_11__hash_nodeIjPvEEEES7_jKNS_10__identityENS_6__lessIvvEEEET0_SC_T1_RKT2_RT4_RT3_
+ __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEN10applesauce2CF7TypeRefEEEPvEEEEEclB9foe220100EPSE_
+ __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPK14__CFDictionaryEEPvEEEEEclB9foe220100EPSE_
+ __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeImNS_10shared_ptrI11ClientEntryEEEEPvEEEEEclB9foe220100EPS9_
+ __ZNSt3__123__optional_storage_baseI14AQMEIO_BindingLb0EE13__assign_fromB9foe220100IRKNS_27__optional_copy_assign_baseIS1_Lb0EEEEEvOT_
+ __ZNSt3__123__optional_storage_baseIN10applesauce2CF9StringRefELb0EE13__assign_fromB9foe220100INS_27__optional_move_assign_baseIS3_Lb0EEEEEvOT_
+ __ZNSt3__123__optional_storage_baseIN10applesauce2CF9StringRefELb0EE13__assign_fromB9foe220100IRKNS_27__optional_copy_assign_baseIS3_Lb0EEEEEvOT_
+ __ZNSt3__123__optional_storage_baseIN2AT9IOBindingELb0EE13__assign_fromB9foe220100IRKNS_27__optional_copy_assign_baseIS2_Lb0EEEEEvOT_
+ __ZNSt3__123__optional_storage_baseIN2CA13ChannelLayoutELb0EE13__assign_fromB9foe220100INS_27__optional_move_assign_baseIS2_Lb0EEEEEvOT_
+ __ZNSt3__123__specialized_algorithmINS_10_Algorithm8__fill_nEJNS_17__single_iteratorINS_14__bit_iteratorINS_8__bitsetILm1ELm13EEELb0ELm0EEEEEEEclB9foe220100ImbEES7_S7_T_RKT0_
+ __ZNSt3__124__optional_destruct_baseIN10applesauce2CF7DataRefELb0EEC2B9foe220100IJRS3_EEENS_10in_place_tEDpOT_
+ __ZNSt3__124__optional_destruct_baseIN2CA16AudioBuffersBaseELb0EE5resetB9foe220100Ev
+ __ZNSt3__124__optional_destruct_baseIN5caulk5alloc23guarded_edges_allocatorINS2_16tiered_allocatorIJNS2_15size_range_tierILm0ELm409599ENS2_22consolidating_free_mapIN2AQ19SharedPageAllocatorELm10485760EEEEENS2_18tracking_allocatorIS8_EEEEELm2EEELb0EE5resetB9foe220100Ev
+ __ZNSt3__124__optional_destruct_baseIN9TapSubmix10InputState14BufferingStateELb0EE5resetB9foe220100Ev
+ __ZNSt3__124__put_character_sequenceB9foe220100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__124__tree_iterate_from_rootB9foe220100IRNS_4pairIKjP15ActiveSoundInfoEEZNS_23__tree_iterate_subrangeB9foe220100INS_15__tree_iteratorINS_12__value_typeIjS4_EEPNS_11__tree_nodeISA_PvEElEEZN15ActiveSoundList31LogCurrentlyPlayingSystemSoundsEvE3$_0NS_10__identityEEEvT_SJ_RT0_RT1_EUlSE_E_SE_SH_SI_EEbSK_SM_RT2_RT3_
+ __ZNSt3__124__tree_iterate_from_rootB9foe220100IRNS_4pairIKjP15ActiveSoundInfoEEZNS_23__tree_iterate_subrangeB9foe220100INS_15__tree_iteratorINS_12__value_typeIjS4_EEPNS_11__tree_nodeISA_PvEElEEZN15ActiveSoundList31RecordStopRequestForActiveSoundEjiE3$_0NS_10__identityEEEvT_SJ_RT0_RT1_EUlSE_E_SE_SH_SI_EEbSK_SM_RT2_RT3_
+ __ZNSt3__124__tree_iterate_from_rootB9foe220100IRNS_4pairIKjP15ActiveSoundInfoEEZNS_23__tree_iterate_subrangeB9foe220100INS_15__tree_iteratorINS_12__value_typeIjS4_EEPNS_11__tree_nodeISA_PvEElEEZZN15ActiveSoundListC1EvEUb0_E3$_1NS_10__identityEEEvT_SJ_RT0_RT1_EUlSE_E_SE_SH_SI_EEbSK_SM_RT2_RT3_
+ __ZNSt3__124__tree_iterate_from_rootB9foe220100IRNS_4pairIKjP15ActiveSoundInfoEEZNS_23__tree_iterate_subrangeB9foe220100INS_15__tree_iteratorINS_12__value_typeIjS4_EEPNS_11__tree_nodeISA_PvEElEEZZN15ActiveSoundListC1EvEUb_E3$_0NS_10__identityEEEvT_SJ_RT0_RT1_EUlSE_E_SE_SH_SI_EEbSK_SM_RT2_RT3_
+ __ZNSt3__124__width_estimation_table9__entriesB9foe220100E
+ __ZNSt3__125__bucket_list_deallocatorIN5caulk12rt_allocatorIPNS_16__hash_node_baseIPNS_11__hash_nodeINS_17__hash_value_typeImbEEPvEEEEEEEclB9foe220100EPSB_
+ __ZNSt3__125__throw_bad_function_callB9foe220100Ev
+ __ZNSt3__125__to_chars_integral_widthB9foe220100IjEEiT_j
+ __ZNSt3__125__to_chars_integral_widthB9foe220100IoEEiT_j
+ __ZNSt3__125__to_chars_integral_widthB9foe220100IyEEiT_j
+ __ZNSt3__126__throw_bad_variant_accessB9foe220100Ev
+ __ZNSt3__127__insertion_sort_incompleteB9foe220100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP10MusicEventEEbT1_S7_T0_
+ __ZNSt3__127__insertion_sort_incompleteB9foe220100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP11VolumeEventEEbT1_S7_T0_
+ __ZNSt3__127__insertion_sort_incompleteB9foe220100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP15MEVADIdentifierEEbT1_S7_T0_
+ __ZNSt3__127__insertion_sort_incompleteB9foe220100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN14NoteOffManager11NoteOffInfoEEEbT1_S8_T0_
+ __ZNSt3__127__insertion_sort_incompleteB9foe220100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEbT1_SC_T0_
+ __ZNSt3__127__insertion_sort_incompleteB9foe220100INS_17_ClassicAlgPolicyERZN17AudioTapSpecifierC1ENS_6vectorIjNS_9allocatorIjEEEENS2_12MuteBehaviorEEUlRK11AQMESessionSA_E_PS8_EEbT1_SE_T0_
+ __ZNSt3__127__insertion_sort_incompleteB9foe220100INS_17_ClassicAlgPolicyERZZZN2AT11Translation19AUAsyncRendererHost9ConfigureEvENK3$_0clENS_6chrono10time_pointINS6_12steady_clockENS6_8durationIxNS_5ratioILl1ELl1000000000EEEEEEERK15AudioBufferListiENKUlRT_E_clINS_6vectorINS4_34TemporallyOrdereredAudioBufferListENS_9allocatorISM_EEEEEEDaSI_EUlRKSM_SS_E_PSM_EEbT1_SW_T0_
+ __ZNSt3__127__throw_bad_optional_accessB9foe220100Ev
+ __ZNSt3__127__tree_balance_after_insertB9foe220100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__128__exception_guard_exceptionsIZNS_10shared_ptrIxEC1B9foe220100IxZN14MixTapToUplink16AQMETapConnector22getCAReporterIDForCallEvEUlPxE_Li0EEEPT_T0_EUlvE_ED2B9foe220100Ev
+ __ZNSt3__130__default_three_way_comparatorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES6_vEclB9foe220100ERKS6_S9_
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__134__uninitialized_allocator_relocateB9foe220100INS_9allocatorI10MusicEventEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__134__uninitialized_allocator_relocateB9foe220100INS_9allocatorI11AQMESessionEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__134__uninitialized_allocator_relocateB9foe220100INS_9allocatorI9TapSourceEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__134__uninitialized_allocator_relocateB9foe220100INS_9allocatorIN10applesauce2CF11TypeRefPairEEEPS4_EEvRT_T0_S9_S9_
+ __ZNSt3__134__uninitialized_allocator_relocateB9foe220100INS_9allocatorIN8InfoList9InfoEntryEEEPS3_EEvRT_T0_S8_S8_
+ __ZNSt3__134__uninitialized_allocator_relocateB9foe220100INS_9allocatorIN8audioipc18SharedAudioBuffers7ElementEEEPS4_EEvRT_T0_S9_S9_
+ __ZNSt3__134__uninitialized_allocator_relocateB9foe220100INS_9allocatorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEEEEPSD_EEvRT_T0_SI_SI_
+ __ZNSt3__135__uninitialized_allocator_copy_implB9foe220100INS_9allocatorI10MusicEventEEPS2_S4_S4_EET2_RT_T0_T1_S5_
+ __ZNSt3__135__uninitialized_allocator_copy_implB9foe220100INS_9allocatorI11AQMESessionEEPKS2_S5_PS2_EET2_RT_T0_T1_S7_
+ __ZNSt3__135__uninitialized_allocator_copy_implB9foe220100INS_9allocatorI11AQMESessionEEPS2_S4_S4_EET2_RT_T0_T1_S5_
+ __ZNSt3__135__uninitialized_allocator_copy_implB9foe220100INS_9allocatorINS_10shared_ptrI9TapSubmixEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE8LocalityNS_4lessIS6_EENS4_INS_4pairIKS6_S7_EEEEE7emplaceB9foe220100IJRS6_S7_EEENSA_INS_14__map_iteratorINS_15__tree_iteratorINS_12__value_typeIS6_S7_EEPNS_11__tree_nodeISK_PvEElEEEEbEEDpOT_
+ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE8LocalityNS_4lessIS6_EENS4_INS_4pairIKS6_S7_EEEEEixERSB_
+ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN10applesauce2CF7TypeRefENS_4lessIS6_EENS4_INS_4pairIKS6_S9_EEEEEixEOS6_
+ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES6_NS_4lessIS6_EENS4_INS_4pairIKS6_S6_EEEEEixEOS6_
+ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES6_NS_4lessIS6_EENS4_INS_4pairIKS6_S6_EEEEEixERSA_
+ __ZNSt3__13mapIjNS_4pairIN11MuteManager14AudioMuteCountENS2_15HapticMuteCountEEENS_4lessIjEEN5caulk12rt_allocatorINS1_IKjS5_EEEEEixERSA_
+ __ZNSt3__13mapIjNS_6bitsetILm32EEENS_4lessIjEENS_9allocatorINS_4pairIKjS2_EEEEEixERS7_
+ __ZNSt3__13mapIjjNS_4lessIjEENS_9allocatorINS_4pairIKjjEEEEE7emplaceB9foe220100IJS6_EEENS4_INS_14__map_iteratorINS_15__tree_iteratorINS_12__value_typeIjjEEPNS_11__tree_nodeISD_PvEElEEEEbEEDpOT_
+ __ZNSt3__13setIiNS_4lessIiEENS_9allocatorIiEEE6insertB9foe220100ERKi
+ __ZNSt3__144__extended_grapheme_custer_property_boundary14__get_propertyB9foe220100EDi
+ __ZNSt3__144__extended_grapheme_custer_property_boundary9__entriesB9foe220100E
+ __ZNSt3__14__fs10filesystem4pathC2B9foe220100INS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEvEERKT_NS2_6formatE
+ __ZNSt3__14lockB9foe220100IN5caulk4mach21unfair_recursive_lockEN16AudioQueueObject20WorkQueueLockAdapterEEEvRT_RT0_
+ __ZNSt3__14lockB9foe220100IN5caulk4mach21unfair_recursive_lockENS1_23recursive_mutex_adapterINS1_22pooled_semaphore_mutexEEEEEvRT_RT0_
+ __ZNSt3__14pairIN10applesauce2CF9StringRefES3_ED2Ev
+ __ZNSt3__14pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEaSB9foe220100EOSB_
+ __ZNSt3__14pairIU8__strongP22AVHapticServerInstanceNS_10shared_ptrI11ClientEntryEEED2Ev
+ __ZNSt3__14swapB9foe220100I11AQMESessionEENS_9enable_ifIXaasr21is_move_constructibleIT_EE5valuesr18is_move_assignableIS3_EE5valueEvE4typeERS3_S6_
+ __ZNSt3__14swapB9foe220100IU8__strongU13block_pointerFvPK15AudioBufferListjEEENS_9enable_ifIXaasr21is_move_constructibleIT_EE5valuesr18is_move_assignableIS8_EE5valueEvE4typeERS8_SB_
+ __ZNSt3__15dequeIN5boost8functionIFNS1_3msm4back11HandledEnumEvEEENS_9allocatorIS7_EEED2B9foe220100Ev
+ __ZNSt3__15dequeINS_4pairIN5boost8functionIFNS2_3msm4back11HandledEnumEvEEEbEENS_9allocatorIS9_EEE26__maybe_remove_front_spareB9foe220100Eb
+ __ZNSt3__15dequeINS_4pairIN5boost8functionIFNS2_3msm4back11HandledEnumEvEEEbEENS_9allocatorIS9_EEE9pop_frontEv
+ __ZNSt3__15dequeINS_4pairIN5boost8functionIFNS2_3msm4back11HandledEnumEvEEEbEENS_9allocatorIS9_EEED2B9foe220100Ev
+ __ZNSt3__15dequeIjNS_9allocatorIjEEE9pop_frontEv
+ __ZNSt3__15dequeIjNS_9allocatorIjEEED2B9foe220100Ev
+ __ZNSt3__16__itoa10__append10B9foe220100IyEEPcS2_T_
+ __ZNSt3__16__itoa10__integralILj16EE10__to_charsB9foe220100IjEENS_17__to_chars_resultEPcS5_T_
+ __ZNSt3__16__itoa10__integralILj16EE10__to_charsB9foe220100IoEENS_17__to_chars_resultEPcS5_T_
+ __ZNSt3__16__itoa10__integralILj16EE10__to_charsB9foe220100IyEENS_17__to_chars_resultEPcS5_T_
+ __ZNSt3__16__itoa10__integralILj2EE10__to_charsB9foe220100IjEENS_17__to_chars_resultEPcS5_T_
+ __ZNSt3__16__itoa10__integralILj2EE10__to_charsB9foe220100IoEENS_17__to_chars_resultEPcS5_T_
+ __ZNSt3__16__itoa10__integralILj2EE10__to_charsB9foe220100IyEENS_17__to_chars_resultEPcS5_T_
+ __ZNSt3__16__itoa10__integralILj8EE10__to_charsB9foe220100IjEENS_17__to_chars_resultEPcS5_T_
+ __ZNSt3__16__itoa10__integralILj8EE10__to_charsB9foe220100IoEENS_17__to_chars_resultEPcS5_T_
+ __ZNSt3__16__itoa10__integralILj8EE10__to_charsB9foe220100IyEENS_17__to_chars_resultEPcS5_T_
+ __ZNSt3__16__itoa10__pow10_32E
+ __ZNSt3__16__itoa10__pow10_64E
+ __ZNSt3__16__itoa11__pow10_128E
+ __ZNSt3__16__itoa12__base_2_lutE
+ __ZNSt3__16__itoa12__base_8_lutE
+ __ZNSt3__16__itoa13__base_10_u32B9foe220100EPcj
+ __ZNSt3__16__itoa13__base_16_lutE
+ __ZNSt3__16__itoa16__digits_base_10E
+ __ZNSt3__16__lerpB9foe220100IdEET_S1_S1_S1_
+ __ZNSt3__16__treeINS_12__value_typeIN14SystemListener5EventENS_8functionIFvbEEEEENS_19__map_value_compareIS3_NS_4pairIKS3_S6_EENS_4lessIS3_EEEENS_9allocatorISB_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS7_PvEE
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE8LocalityEENS_19__map_value_compareIS7_NS_4pairIKS7_S8_EENS_4lessIS7_EEEENS5_ISD_EEE12__find_equalB9foe220100IS7_EENSB_IPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSO_EERKT_
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE8LocalityEENS_19__map_value_compareIS7_NS_4pairIKS7_S8_EENS_4lessIS7_EEEENS5_ISD_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS9_PvEE
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE8LocalityEENS_19__map_value_compareIS7_NS_4pairIKS7_S8_EENS_4lessIS7_EEEENS5_ISD_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSN_SN_
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN10applesauce2CF7TypeRefEEENS_19__map_value_compareIS7_NS_4pairIKS7_SA_EENS_4lessIS7_EEEENS5_ISF_EEE12__find_equalB9foe220100IS7_EENSD_IPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSQ_EERKT_
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN10applesauce2CF7TypeRefEEENS_19__map_value_compareIS7_NS_4pairIKS7_SA_EENS_4lessIS7_EEEENS5_ISF_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeISB_PvEE
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN10applesauce2CF7TypeRefEEENS_19__map_value_compareIS7_NS_4pairIKS7_SA_EENS_4lessIS7_EEEENS5_ISF_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSP_SP_
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29NewNotificationCenterObserverEEEENS_19__map_value_compareIS7_NS_4pairIKS7_SA_EENS_4lessIS7_EEEENS5_ISF_EEE12__find_equalB9foe220100IS7_EENSD_IPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSQ_EERKT_
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29NewNotificationCenterObserverEEEENS_19__map_value_compareIS7_NS_4pairIKS7_SA_EENS_4lessIS7_EEEENS5_ISF_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeISB_PvEE
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29OldNotificationCenterObserverEEEENS_19__map_value_compareIS7_NS_4pairIKS7_SA_EENS_4lessIS7_EEEENS5_ISF_EEE12__find_equalB9foe220100IS7_EENSD_IPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSQ_EERKT_
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29OldNotificationCenterObserverEEEENS_19__map_value_compareIS7_NS_4pairIKS7_SA_EENS_4lessIS7_EEEENS5_ISF_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeISB_PvEE
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPK14__CFDictionaryEENS_19__map_value_compareIS7_NS_4pairIKS7_SA_EENS_4lessIS7_EEEENS5_ISF_EEE12__find_equalB9foe220100IS7_EENSD_IPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSQ_EERKT_
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS_19__map_value_compareIS7_NS_4pairIKS7_S7_EENS_4lessIS7_EEEENS5_ISC_EEE12__find_equalB9foe220100IS7_EENSA_IPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSN_EERKT_
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS_19__map_value_compareIS7_NS_4pairIKS7_S7_EENS_4lessIS7_EEEENS5_ISC_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS8_PvEE
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS_19__map_value_compareIS7_NS_4pairIKS7_S7_EENS_4lessIS7_EEEENS5_ISC_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSM_SM_
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEyEENS_19__map_value_compareIS7_NS_4pairIKS7_yEENS_4lessIS7_EEEENS5_ISC_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS8_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIP14MEMixerChannelN9TapSubmix10InputStateEEENS_19__map_value_compareIS3_NS_4pairIKS3_S5_EENS_4lessIS3_EEEENS_9allocatorISA_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS6_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIP9TapSubmixN14MEMixerChannel19TapSubmixConnectionEEENS_19__map_value_compareIS3_NS_4pairIKS3_S5_EENS_4lessIS3_EEEENS_9allocatorISA_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS6_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIP9TapSubmixN14MEMixerChannel19TapSubmixConnectionEEENS_19__map_value_compareIS3_NS_4pairIKS3_S5_EENS_4lessIS3_EEEENS_9allocatorISA_EEE21__construct_from_treeB9foe220100IZNSG_21__copy_construct_treeB9foe220100EPNS_11__tree_nodeIS6_PvEEEUlRKSA_E_EESL_SL_T_
+ __ZNSt3__16__treeINS_12__value_typeIPK14AQIONodeClientZN2AT13SessionFacadeL34PopulateSourceFormatInfoDictionaryEP14__CFDictionaryPKvRS3_RN2CA17StreamDescriptionEbbbE16SourceFormatInfoEENS_19__map_value_compareIS4_NS_4pairIKS4_SF_EENS_4lessIS4_EEEENS_9allocatorISK_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeISG_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIU8__strongP22AVHapticServerInstanceNS_10shared_ptrI11ClientEntryEEEENS_19__map_value_compareIS4_NS_4pairIU8__strongKS3_S7_EENS_4lessIS4_EEEENS_9allocatorISC_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS8_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIdjEENS_19__map_value_compareIdNS_4pairIKdjEENS_4lessIdEEEENS_9allocatorIS6_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS2_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIiNS_10unique_ptrI13XOSTransactorNS_14default_deleteIS3_EEEEEENS_19__map_value_compareIiNS_4pairIKiS6_EENS_4lessIiEEEENS_9allocatorISB_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS7_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIiNS_6bitsetILm255EEEEENS_19__map_value_compareIiNS_4pairIKiS3_EENS_4lessIiEEEENS_9allocatorIS8_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS4_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIjNS_4pairIN11MuteManager14AudioMuteCountENS3_15HapticMuteCountEEEEENS_19__map_value_compareIjNS2_IKjS6_EENS_4lessIjEEEEN5caulk12rt_allocatorISA_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS7_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIjNS_6bitsetILm32EEEEENS_19__map_value_compareIjNS_4pairIKjS3_EENS_4lessIjEEEENS_9allocatorIS8_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS4_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIjP15ActiveSoundInfoEENS_19__map_value_compareIjNS_4pairIKjS3_EENS_4lessIjEEEENS_9allocatorIS8_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS4_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIjU8__strongP14NSMutableArrayIP15AVServerWrapperEEENS_19__map_value_compareIjNS_4pairIKjS7_EENS_4lessIjEEEENS_9allocatorISC_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS8_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIjjEENS_19__map_value_compareIjNS_4pairIKjjEENS_4lessIjEEEENS_9allocatorIS6_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS2_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIjjEENS_19__map_value_compareIjNS_4pairIKjjEENS_4lessIjEEEENS_9allocatorIS6_EEE21__construct_from_treeB9foe220100IZNSC_21__copy_construct_treeB9foe220100EPNS_11__tree_nodeIS2_PvEEEUlRKS6_E_EESH_SH_T_
+ __ZNSt3__16__treeINS_12__value_typeIjjEENS_19__map_value_compareIjNS_4pairIKjjEENS_4lessIjEEEENS_9allocatorIS6_EEE21__remove_node_pointerEPNS_11__tree_nodeIS2_PvEE
+ __ZNSt3__16__treeINS_12__value_typeImN5caulk5alloc22consolidating_free_mapIN2AQ19SharedPageAllocatorELm10485760EE14FreelistOfSizeEEENS_19__map_value_compareImNS_4pairIKmS8_EENS_4lessImEEEENS_9allocatorISD_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS9_PvEE
+ __ZNSt3__16__treeINS_12__value_typeImN5caulk5alloc22consolidating_free_mapIN2AQ19SharedPageAllocatorELm10485760EE14FreelistOfSizeEEENS_19__map_value_compareImNS_4pairIKmS8_EENS_4lessImEEEENS_9allocatorISD_EEE21__remove_node_pointerEPNS_11__tree_nodeIS9_PvEE
+ __ZNSt3__16__treeINS_12__value_typeImNS_10shared_ptrI11ClientEntryEEEENS_19__map_value_compareImNS_4pairIKmS4_EENS_4lessImEEEENS_9allocatorIS9_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS5_PvEE
+ __ZNSt3__16__treeINS_12__value_typeImNS_10shared_ptrI11ClientEntryEEEENS_19__map_value_compareImNS_4pairIKmS4_EENS_4lessImEEEENS_9allocatorIS9_EEE21__construct_from_treeB9foe220100IZNSF_21__copy_construct_treeB9foe220100EPNS_11__tree_nodeIS5_PvEEEUlRKS9_E_EESK_SK_T_
+ __ZNSt3__16__treeINS_12__value_typeImjEENS_19__map_value_compareImNS_4pairIKmjEENS_4lessImEEEEN5caulk12rt_allocatorIS6_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS2_PvEE
+ __ZNSt3__16__treeINS_12__value_typeImjEENS_19__map_value_compareImNS_4pairIKmjEENS_4lessImEEEENS_9allocatorIS6_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS2_PvEE
+ __ZNSt3__16__treeINS_12__value_typeImjEENS_19__map_value_compareImNS_4pairIKmjEENS_4lessImEEEENS_9allocatorIS6_EEE21__construct_from_treeB9foe220100IZNSC_21__copy_construct_treeB9foe220100EPNS_11__tree_nodeIS2_PvEEEUlRKS6_E_EESH_SH_T_
+ __ZNSt3__16__treeINS_12__value_typeImjEENS_19__map_value_compareImNS_4pairIKmjEENS_4lessImEEEENS_9allocatorIS6_EEE21__remove_node_pointerEPNS_11__tree_nodeIS2_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIttEENS_19__map_value_compareItNS_4pairIKttEENS_4lessItEEEENS_9allocatorIS6_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS2_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIttEENS_19__map_value_compareItNS_4pairIKttEENS_4lessItEEEENS_9allocatorIS6_EEE5eraseENS_21__tree_const_iteratorIS2_PNS_11__tree_nodeIS2_PvEElEESI_
+ __ZNSt3__16__treeIP10XAudioUnitNS_4lessIS2_EENS_9allocatorIS2_EEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIS2_PvEE
+ __ZNSt3__16__treeIP10XAudioUnitNS_4lessIS2_EENS_9allocatorIS2_EEE18__assign_from_treeB9foe220100IZNS7_18__copy_assign_treeB9foe220100EPNS_11__tree_nodeIS2_PvEESC_EUlRS2_RKS2_E_ZNS7_18__copy_assign_treeB9foe220100ESC_SC_EUlSC_E_EESC_SC_SC_T_T0_
+ __ZNSt3__16__treeIP10XAudioUnitNS_4lessIS2_EENS_9allocatorIS2_EEE21__construct_from_treeB9foe220100IZNS7_21__copy_construct_treeB9foe220100EPNS_11__tree_nodeIS2_PvEEEUlRKS2_E_EESC_SC_T_
+ __ZNSt3__16__treeIP10XAudioUnitNS_4lessIS2_EENS_9allocatorIS2_EEEC2ERKS7_
+ __ZNSt3__16__treeIiNS_4lessIiEENS_9allocatorIiEEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIiPvEE
+ __ZNSt3__16__treeIjNS_4lessIjEENS_9allocatorIjEEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIjPvEE
+ __ZNSt3__16__treeIxNS_4lessIxEENS_9allocatorIxEEE14__tree_deleterclB9foe220100EPNS_11__tree_nodeIxPvEE
+ __ZNSt3__16any_ofB9foe220100INS_11__wrap_iterIPPK10__CFStringEEZN16AudioQueueObject11SetPropertyEjR14CADeserializerE3$_0EEbT_SB_T0_
+ __ZNSt3__16localeC1ERKS0_
+ __ZNSt3__16localeaSERKS0_
+ __ZNSt3__16vectorI10ChaseEventN5caulk12rt_allocatorIS1_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorI10ChaseEventN5caulk12rt_allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI10ChaseEventN5caulk12rt_allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE18__assign_with_sizeB9foe220100INS_17_ClassicAlgPolicyEPS1_S7_EEvT0_T1_l
+ __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE18__insert_with_sizeB9foe220100INS_17_ClassicAlgPolicyENS_11__wrap_iterIPS1_EES9_EES9_NS7_IPKS1_EET0_T1_l
+ __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE9push_backB9foe220100ERKS1_
+ __ZNSt3__16vectorI10PowerMeterNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI11AQMESessionNS_9allocatorIS1_EEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorI11AQMESessionNS_9allocatorIS1_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorI11AQMESessionNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI11AQMESessionNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI11AQMESessionNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI11TrackChaserNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI11TrackChaserNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI11VolumeEventN5caulk12rt_allocatorIS1_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorI11VolumeEventN5caulk12rt_allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI11VolumeEventN5caulk12rt_allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI13ChaseInstInfoNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI13ChaseInstInfoNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI13ChaseInstInfoNS_9allocatorIS1_EEE5eraseENS_11__wrap_iterIPKS1_EES8_
+ __ZNSt3__16vectorI13RootQueueInfoNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI13RootQueueInfoNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI14MEStreamTypeIDNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI14MEStreamTypeIDNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI15MEVADIdentifierNS_9allocatorIS1_EEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorI15MEVADIdentifierNS_9allocatorIS1_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorI15MEVADIdentifierNS_9allocatorIS1_EEE16__init_with_sizeB9foe220100IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI15MEVADIdentifierNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI15MEVADIdentifierNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJR14MEDeviceTypeIDEEEPS1_DpOT_
+ __ZNSt3__16vectorI15MEVADIdentifierNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI15MeterTrackEntryNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI15MeterTrackEntryNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI16AURateRampStructNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI16AURateRampStructNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI18AudioMetadataEventNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI18AudioMetadataEventNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI20AUNodeRenderCallbackNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI20AUNodeRenderCallbackNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI22AUGraphLiveUpdateEventNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI22AUGraphLiveUpdateEventNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI23AudioUnitNodeConnectionNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI23AudioUnitNodeConnectionNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI23AudioUnitParameterEventN5caulk12rt_allocatorIS1_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorI23AudioUnitParameterEventN5caulk12rt_allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI23AudioUnitParameterEventN5caulk12rt_allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI23AudioUnitParameterEventNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI23AudioUnitParameterEventNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI24AudioQueueParameterEventNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI24AudioQueueParameterEventNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI25AudioQueueLevelMeterStateNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI26AQBufferCreateDestroyEventNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI26AQBufferCreateDestroyEventNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI26AQBufferCreateDestroyEventNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI26AudioObjectPropertyAddressNS_9allocatorIS1_EEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorI26AudioObjectPropertyAddressNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI26AudioObjectPropertyAddressNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI27AudioQueueChannelAssignmentNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI28AudioStreamPacketDescriptionNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI30AQProcessingNodeImmediateEventNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI30AQProcessingNodeImmediateEventNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI32AudioSessionPropertyListenerInfoNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI32AudioSessionPropertyListenerInfoNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI9TapSourceNS_9allocatorIS1_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorI9TapSourceNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorI9TapSourceNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKNS_12basic_stringIcNS_11char_traitsIcEENS4_IcEEEERKNS2_7TypeRefEEEEPS3_DpOT_
+ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKNS_12basic_stringIcNS_11char_traitsIcEENS4_IcEEEERKyEEEPS3_DpOT_
+ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKNS_12basic_stringIcNS_11char_traitsIcEENS4_IcEEEESE_EEEPS3_DpOT_
+ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJEEEPS3_DpOT_
+ __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJPKcEEEPS3_DpOT_
+ __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJbEEEPS3_DpOT_
+ __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJdEEEPS3_DpOT_
+ __ZNSt3__16vectorIN10applesauce2CF9NumberRefENS_9allocatorIS3_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorIN10applesauce2CF9NumberRefENS_9allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN10applesauce2CF9NumberRefENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJjEEEPS3_DpOT_
+ __ZNSt3__16vectorIN14AudioUnitGraph14RenderCallbackENS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN14AudioUnitGraph14RenderCallbackENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIN14NoteOffManager11NoteOffInfoENS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN14NoteOffManager11NoteOffInfoENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIN14NoteOffManager14ControlMessageENS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN14NoteOffManager14ControlMessageENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIN16AudioQueueObject12AQRateChangeENS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN16AudioQueueObject12AQRateChangeENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIN18AQOfflineMixerBase10MixerQueueENS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN18AQOfflineMixerBase10MixerQueueENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIN18AQOfflineMixerBase15StartQueueEventENS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN19SequenceDestination14TrackPlayStateENS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN19SequenceDestination14TrackPlayStateENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIN21IPCAUSharedMemoryBase7ElementENS_9allocatorIS2_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorIN21VibeToHapticConverter11SegmentInfoENS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN21VibeToHapticConverter11SegmentInfoENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIN25AUNodeSequenceDestination18RampTrackPlayStateENS_9allocatorIS2_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorIN25AUNodeSequenceDestination18RampTrackPlayStateENS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN25AUNodeSequenceDestination18RampTrackPlayStateENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIN2AQ6Server12RemoteClient18ProcessingTapStateENS_9allocatorIS4_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorIN2AQ6Server12RemoteClient18ProcessingTapStateENS_9allocatorIS4_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN2AQ6Server12RemoteClient18ProcessingTapStateENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJS4_EEEPS4_DpOT_
+ __ZNSt3__16vectorIN2AQ6Server12RemoteClient5QueueENS_9allocatorIS4_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN2AQ6Server12RemoteClient5QueueENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJS4_EEEPS4_DpOT_
+ __ZNSt3__16vectorIN2AT11Translation19AUAsyncRendererHost34TemporallyOrdereredAudioBufferListENS_9allocatorIS4_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN2AT11Translation19AUAsyncRendererHost34TemporallyOrdereredAudioBufferListENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJRKS4_EEEPS4_DpOT_
+ __ZNSt3__16vectorIN2AU8Property10Attributes7details15AUPresetWrapperENS_9allocatorIS5_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorIN2AU8Property10Attributes7details15AUPresetWrapperENS_9allocatorIS5_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN2AU8Property10Attributes7details15AUPresetWrapperENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJS5_EEEPS5_DpOT_
+ __ZNSt3__16vectorIN5boost8functionIFvRN11SequenceFSM25PostRenderFlushingVisitorEP14SequenceActiondEEENS_9allocatorIS9_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorIN8InfoList9InfoEntryENS_9allocatorIS2_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorIN8InfoList9InfoEntryENS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN8InfoList9InfoEntryENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIN8TempoMap10TempoEntryENS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN8TempoMap10TempoEntryENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIN8XAUMixer11EInputStateENS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN8XAUMixer11EInputStateENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIN8audioipc18SharedAudioBuffers7ElementENS_9allocatorIS3_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorIN8audioipc18SharedAudioBuffers7ElementENS_9allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIN8audioipc18SharedAudioBuffers7ElementENS_9allocatorIS3_EEE20__throw_out_of_rangeB9foe220100Ev
+ __ZNSt3__16vectorIN8audioipc18SharedAudioBuffers7ElementENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKNS1_14ExtendedFormatEEEEPS3_DpOT_
+ __ZNSt3__16vectorINS_10shared_ptrI11ClientEntryEENS_9allocatorIS3_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI11ClientEntryEENS_9allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI11ClientEntryEENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorINS_10shared_ptrI11ClientEntryEENS_9allocatorIS3_EEE9push_backB9foe220100ERKS3_
+ __ZNSt3__16vectorINS_10shared_ptrI14HapticSequenceEEN5caulk12rt_allocatorIS3_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI14HapticSequenceEEN5caulk12rt_allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI14HapticSequenceEEN5caulk12rt_allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorINS_10shared_ptrI14HapticSequenceEEN5caulk12rt_allocatorIS3_EEE5clearB9foe220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI14HapticSequenceEEN5caulk12rt_allocatorIS3_EEE9push_backB9foe220100ERKS3_
+ __ZNSt3__16vectorINS_10shared_ptrI16MCProcessingNodeEENS_9allocatorIS3_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI16MCProcessingNodeEENS_9allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI16MCProcessingNodeEENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorINS_10shared_ptrI16MCProcessingNodeEENS_9allocatorIS3_EEE9push_backB9foe220100ERKS3_
+ __ZNSt3__16vectorINS_10shared_ptrI8AQIONodeEENS_9allocatorIS3_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI8AQIONodeEENS_9allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI8AQIONodeEENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE16__init_with_sizeB9foe220100IPS3_S8_EEvT_T0_m
+ __ZNSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE5clearB9foe220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN10AQMEIO_HAL8IOStreamEEENS_9allocatorIS4_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN10AQMEIO_HAL8IOStreamEEENS_9allocatorIS4_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN10AQMEIO_HAL8IOStreamEEENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJRKS4_EEEPS4_DpOT_
+ __ZNSt3__16vectorINS_10shared_ptrIN10AQMEIO_HAL8IOStreamEEENS_9allocatorIS4_EEE5clearB9foe220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN18PowerUsageWatchdog17ClientDescriptionEEENS_9allocatorIS4_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN18PowerUsageWatchdog17ClientDescriptionEEENS_9allocatorIS4_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN18PowerUsageWatchdog17ClientDescriptionEEENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJRKS4_EEEPS4_DpOT_
+ __ZNSt3__16vectorINS_10shared_ptrIN2AQ3API9SubmixTapEEENS_9allocatorIS5_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN2AQ3API9SubmixTapEEENS_9allocatorIS5_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN2AQ3API9SubmixTapEEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJRKS5_EEEPS5_DpOT_
+ __ZNSt3__16vectorINS_10unique_ptrI11IAQMEDeviceNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI11IAQMEDeviceNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI11IAQMEDeviceNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJRPN15AQMixEngine_VAD10MEVADeviceEEEEPS5_DpOT_
+ __ZNSt3__16vectorINS_10unique_ptrI11IAQMEDeviceNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJRPS2_EEEPS5_DpOT_
+ __ZNSt3__16vectorINS_10unique_ptrI11MEConnectorNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI11MEConnectorNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI11MEConnectorNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJS5_EEEPS5_DpOT_
+ __ZNSt3__16vectorINS_10unique_ptrI14AQClientBufferN2AQ3API13BufferDeleterEEENS_9allocatorIS6_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI14AQClientBufferN2AQ3API13BufferDeleterEEENS_9allocatorIS6_EEE24__emplace_back_slow_pathIJS6_EEEPS6_DpOT_
+ __ZNSt3__16vectorINS_10unique_ptrI14AQOfflineMixerNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI14AQOfflineMixerNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI14AQOfflineMixerNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJS5_EEEPS5_DpOT_
+ __ZNSt3__16vectorINS_10unique_ptrI14AQOfflineMixerNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE5clearB9foe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI15SubmixTapObjectNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI15SubmixTapObjectNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI15SubmixTapObjectNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJS5_EEEPS5_DpOT_
+ __ZNSt3__16vectorINS_10unique_ptrI16AQProcessingNodeNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI16AQProcessingNodeNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI16AQProcessingNodeNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJS5_EEEPS5_DpOT_
+ __ZNSt3__16vectorINS_10unique_ptrI16SSSVibrationDataNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI16SSSVibrationDataNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJS5_EEEPS5_DpOT_
+ __ZNSt3__16vectorINS_10unique_ptrIN18PowerUsageWatchdog12ClientLoggerENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN18PowerUsageWatchdog12ClientLoggerENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN18PowerUsageWatchdog12ClientLoggerENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE24__emplace_back_slow_pathIJNS1_IZNS2_4Impl21populateClientLoggersEvE16CAReporterLoggerNS4_ISC_EEEEEEEPS6_DpOT_
+ __ZNSt3__16vectorINS_10unique_ptrIN18PowerUsageWatchdog12ClientLoggerENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE24__emplace_back_slow_pathIJNS1_IZNS2_4Impl21populateClientLoggersEvE20CaulkLogClientLoggerNS4_ISC_EEEEEEEPS6_DpOT_
+ __ZNSt3__16vectorINS_10unique_ptrIN18PowerUsageWatchdog12ClientLoggerENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE24__emplace_back_slow_pathIJNS1_IZNS2_4Impl21populateClientLoggersEvE20PowerLogClientLoggerNS4_ISC_EEEEEEEPS6_DpOT_
+ __ZNSt3__16vectorINS_10unique_ptrIN18PowerUsageWatchdog12ClientLoggerENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE24__emplace_back_slow_pathIJS6_EEEPS6_DpOT_
+ __ZNSt3__16vectorINS_10unique_ptrIN2AQ3API14ProcessingNodeENS_14default_deleteIS4_EEEENS_9allocatorIS7_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN2AQ3API14ProcessingNodeENS_14default_deleteIS4_EEEENS_9allocatorIS7_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN2AQ3API14ProcessingNodeENS_14default_deleteIS4_EEEENS_9allocatorIS7_EEE24__emplace_back_slow_pathIJS7_EEEPS7_DpOT_
+ __ZNSt3__16vectorINS_10unique_ptrIN2AQ6Server12RemoteClientENS_14default_deleteIS4_EEEENS_9allocatorIS7_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN2AQ6Server12RemoteClientENS_14default_deleteIS4_EEEENS_9allocatorIS7_EEE24__emplace_back_slow_pathIJS7_EEEPS7_DpOT_
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJRS6_EEEPS6_DpOT_
+ __ZNSt3__16vectorINS_13unordered_mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbNS_4hashIS7_EENS_8equal_toIS7_EENS5_INS_4pairIKS7_bEEEEEENS5_ISG_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEENS_9allocatorISC_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEENS_9allocatorISC_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_4pairINS_10shared_ptrI11SynthOutputEEbEENS_9allocatorIS5_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_4pairINS_10shared_ptrI11SynthOutputEEbEENS_9allocatorIS5_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_4pairINS_10shared_ptrI11SynthOutputEEbEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJS5_EEEPS5_DpOT_
+ __ZNSt3__16vectorINS_4pairINS_10shared_ptrI11SynthOutputEEbEENS_9allocatorIS5_EEE5clearB9foe220100Ev
+ __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS5_IS8_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS5_IS8_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS5_IS8_EEE24__emplace_back_slow_pathIJS8_EEEPS8_DpOT_
+ __ZNSt3__16vectorINS_4pairIPFiPvPjPK14AudioTimeStampjjP15AudioBufferListES2_EEN5caulk12rt_allocatorISB_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_4pairIPFiPvPjPK14AudioTimeStampjjP15AudioBufferListES2_EEN5caulk12rt_allocatorISB_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_4pairIPFiPvPjPK14AudioTimeStampjjP15AudioBufferListES2_EEN5caulk12rt_allocatorISB_EEE24__emplace_back_slow_pathIJSB_EEEPSB_DpOT_
+ __ZNSt3__16vectorINS_4pairIffEEN5caulk12rt_allocatorIS2_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_4pairIffEEN5caulk12rt_allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_4pairIffEEN5caulk12rt_allocatorIS2_EEE24__emplace_back_slow_pathIJRffEEEPS2_DpOT_
+ __ZNSt3__16vectorINS_4pairIjNS_10shared_ptrIN2AQ3API11BufferOwnerEEEEENS_9allocatorIS7_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_4pairIjNS_10shared_ptrIN2AQ3API11BufferOwnerEEEEENS_9allocatorIS7_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_4pairIjNS_10shared_ptrIN2AQ3API11BufferOwnerEEEEENS_9allocatorIS7_EEE24__emplace_back_slow_pathIJRjKS6_EEEPS7_DpOT_
+ __ZNSt3__16vectorINS_4pairIjNS_10shared_ptrIN2AQ3API11BufferOwnerEEEEENS_9allocatorIS7_EEE5clearB9foe220100Ev
+ __ZNSt3__16vectorINS_4pairIjNS_8optionalIjEEEENS_9allocatorIS4_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_4pairIjNS_8optionalIjEEEENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJS4_EEEPS4_DpOT_
+ __ZNSt3__16vectorINS_5tupleIJjNS_10shared_ptrIN2AQ3API5QueueEEEEEENS_9allocatorIS7_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_5tupleIJjNS_10shared_ptrIN2AQ3API5QueueEEEEEENS_9allocatorIS7_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_5tupleIJjNS_10shared_ptrIN2AQ3API5QueueEEEEEENS_9allocatorIS7_EEE24__emplace_back_slow_pathIJRjRKS6_EEEPS7_DpOT_
+ __ZNSt3__16vectorINS_5tupleIJjNS_10shared_ptrIN2AQ3API9SubmixTapEEEEEENS_9allocatorIS7_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_5tupleIJjNS_10shared_ptrIN2AQ3API9SubmixTapEEEEEENS_9allocatorIS7_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_5tupleIJjNS_10shared_ptrIN2AQ3API9SubmixTapEEEEEENS_9allocatorIS7_EEE24__emplace_back_slow_pathIJRjRKS6_EEEPS7_DpOT_
+ __ZNSt3__16vectorINS_5tupleIJjPFvPvP16OpaqueAudioQueuejES2_EEENS_9allocatorIS7_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_8weak_ptrI25AQMEIO_NotificationClientEENS_9allocatorIS3_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_8weak_ptrI25AQMEIO_NotificationClientEENS_9allocatorIS3_EEE16__init_with_sizeB9foe220100IPS3_S8_EEvT_T0_m
+ __ZNSt3__16vectorINS_8weak_ptrI25AQMEIO_NotificationClientEENS_9allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_8weak_ptrI25AQMEIO_NotificationClientEENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorINS_8weak_ptrI8AQIONodeEENS_9allocatorIS3_EEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorINS_8weak_ptrI8AQIONodeEENS_9allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_8weak_ptrI8AQIONodeEENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorINS_8weak_ptrIN5caulk17lifetime_observedINS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS5_EEEENS2_23shared_instance_managerIS5_E8observerEEEEENS_9allocatorISD_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorINS_8weak_ptrIN5caulk17lifetime_observedINS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS5_EEEENS2_23shared_instance_managerIS5_E8observerEEEEENS_9allocatorISD_EEE24__emplace_back_slow_pathIJRNS_10shared_ptrISC_EEEEEPSD_DpOT_
+ __ZNSt3__16vectorIP10AUNodeInfoNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP10AUNodeInfoNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP10ClientInfoNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP10ClientInfoNS_9allocatorIS2_EEE20__throw_out_of_rangeB9foe220100Ev
+ __ZNSt3__16vectorIP10ClientInfoNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP11MCAudioUnitNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP11MCAudioUnitNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP11MCAudioUnitNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP11MEConnectorNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP11MEConnectorNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP12SSSAudioDataNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP12SSSAudioDataNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP13AudioTapMixerNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP13AudioTapMixerNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP13MESubmixGraphNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP13MESubmixGraphNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP13SequenceTrackNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP13SequenceTrackNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP14AQIONodeClientNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP14AQIONodeClientNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP14AudioTapObjectNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP14AudioTapObjectNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP14CAExternalLockNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP14CAExternalLockNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP14MEMixerChannelNS_9allocatorIS2_EEE16__init_with_sizeB9foe220100IPS2_S7_EEvT_T0_m
+ __ZNSt3__16vectorIP14MEMixerChannelNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP14MEMixerChannelNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP14MEMixerChannelNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP14MixTapToUplinkNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP14MixTapToUplinkNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP14__CFDictionaryNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP15InputDispatcherNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP15InputDispatcherNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP15InputDispatcherNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP15XProcessingBaseNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP15XProcessingBaseNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP15XProcessingBaseNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP16AudioQueueObjectNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP16AudioQueueObjectNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP19MEInputStreamClientNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP19MEInputStreamClientNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP19SSSActionPlayerBaseNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP19SSSActionPlayerBaseNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP20MEOutputStreamClientNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP20MEOutputStreamClientNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP25AUNodeSequenceDestinationNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP25AUNodeSequenceDestinationNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP31MIDIEndpointSequenceDestinationNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP31MIDIEndpointSequenceDestinationNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP8AQIONodeNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP8AQIONodeNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP8UserInfoNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIP8UserInfoNS_9allocatorIS2_EEE20__throw_out_of_rangeB9foe220100Ev
+ __ZNSt3__16vectorIP8UserInfoNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIPK10__CFStringNS_9allocatorIS3_EEE16__init_with_sizeB9foe220100IPKS3_S9_EEvT_T0_m
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEEC2B9foe220100Em
+ __ZNSt3__16vectorIPN11DSP_Routing15PublishedStreamENS_9allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIPN11DSP_Routing15PublishedStreamENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorIPN11DSP_Routing6StreamENS_9allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIPN11DSP_Routing6StreamENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorIPN12CADeprecated11XMachServer6ClientENS_9allocatorIS4_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIPN12CADeprecated11XMachServer6ClientENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJRKS4_EEEPS4_DpOT_
+ __ZNSt3__16vectorIPN15CAListenerProxy8ListenerENS_9allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIPN15CAListenerProxy8ListenerENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorIPN16AudioQueueObject23ScheduledSliceAllocatorENS_9allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIPN16AudioQueueObject23ScheduledSliceAllocatorENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorIPN2AQ3API12OfflineMixerENS_9allocatorIS4_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIPN2AQ3API12OfflineMixerENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJRS4_EEEPS4_DpOT_
+ __ZNSt3__16vectorIPvNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorISt4byteNS_9allocatorIS1_EEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorISt4byteNS_9allocatorIS1_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorISt4byteNS_9allocatorIS1_EEEC2B9foe220100Em
+ __ZNSt3__16vectorIU8__strongP24ATAudioSessionClientImplNS_9allocatorIS3_EEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIU8__strongP24ATAudioSessionClientImplNS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRU8__strongKS2_EEEPS3_DpOT_
+ __ZNSt3__16vectorIU8__strongP24ATAudioSessionClientImplNS_9allocatorIS3_EEE9push_backB9foe220100ERU8__strongKS2_
+ __ZNSt3__16vectorIcN5caulk12rt_allocatorIcEEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorIcN5caulk12rt_allocatorIcEEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIcN5caulk12rt_allocatorIcEEE6resizeEm
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE16__init_with_sizeB9foe220100IPcS5_EEvT_T0_m
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE18__assign_with_sizeB9foe220100INS_17_ClassicAlgPolicyEPcS6_EEvT0_T1_l
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE6resizeEm
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE6resizeEmRKc
+ __ZNSt3__16vectorIcNS_9allocatorIcEEEC2B9foe220100Em
+ __ZNSt3__16vectorIcNS_9allocatorIcEEEC2B9foe220100EmRKc
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE24__emplace_back_slow_pathIJRKfEEEPfDpOT_
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE18__assign_with_sizeB9foe220100INS_17_ClassicAlgPolicyEPhS6_EEvT0_T1_l
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE6resizeEm
+ __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B9foe220100Em
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE16__init_with_sizeB9foe220100IPKiS6_EEvT_T0_m
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE16__init_with_sizeB9foe220100IPiS5_EEvT_T0_m
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE18__assign_with_sizeB9foe220100INS_17_ClassicAlgPolicyEPKiS7_EEvT0_T1_l
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE18__assign_with_sizeB9foe220100INS_17_ClassicAlgPolicyEPiS6_EEvT0_T1_l
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE24__emplace_back_slow_pathIJRKiEEEPiDpOT_
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE24__emplace_back_slow_pathIJiEEEPiDpOT_
+ __ZNSt3__16vectorIjN5caulk12rt_allocatorIjEEE16__destroy_vectorclB9foe220100Ev
+ __ZNSt3__16vectorIjN5caulk12rt_allocatorIjEEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIjN5caulk12rt_allocatorIjEEE24__emplace_back_slow_pathIJRKjEEEPjDpOT_
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE16__init_with_sizeB9foe220100INS_11__wrap_iterIPKjEES8_EEvT_T0_m
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE16__init_with_sizeB9foe220100IPKjS6_EEvT_T0_m
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE16__init_with_sizeB9foe220100IPjS5_EEvT_T0_m
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE18__assign_with_sizeB9foe220100INS_17_ClassicAlgPolicyEPKjS7_EEvT0_T1_l
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE18__assign_with_sizeB9foe220100INS_17_ClassicAlgPolicyEPjS6_EEvT0_T1_l
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE18__insert_with_sizeB9foe220100INS_17_ClassicAlgPolicyENS_11__wrap_iterIPjEES8_EES8_NS6_IPKjEET0_T1_l
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_out_of_rangeB9foe220100Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE24__emplace_back_slow_pathIJRKjEEEPjDpOT_
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE24__emplace_back_slow_pathIJRjEEEPjDpOT_
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE24__emplace_back_slow_pathIJjEEEPjDpOT_
+ __ZNSt3__16vectorIjNS_9allocatorIjEEEC2B9foe220100Em
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEE24__emplace_back_slow_pathIJRKmEEEPmDpOT_
+ __ZNSt3__16vectorImNS_9allocatorImEEE24__emplace_back_slow_pathIJmEEEPmDpOT_
+ __ZNSt3__16vectorIxNS_9allocatorIxEEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorIxNS_9allocatorIxEEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__17__sort3B9foe220100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP15MEVADIdentifierLi0EEEbT1_S7_S7_T0_
+ __ZNSt3__17__sort3B9foe220100INS_17_ClassicAlgPolicyERZN17AudioTapSpecifierC1ENS_6vectorIjNS_9allocatorIjEEEENS2_12MuteBehaviorEEUlRK11AQMESessionSA_E_PS8_Li0EEEbT1_SE_SE_T0_
+ __ZNSt3__17__sort4B9foe220100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP10MusicEventLi0EEEvT1_S7_S7_S7_T0_
+ __ZNSt3__17__sort4B9foe220100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP11VolumeEventLi0EEEvT1_S7_S7_S7_T0_
+ __ZNSt3__17__sort4B9foe220100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEELi0EEEvT1_SC_SC_SC_T0_
+ __ZNSt3__17__sort4B9foe220100INS_17_ClassicAlgPolicyERZN17AudioTapSpecifierC1ENS_6vectorIjNS_9allocatorIjEEEENS2_12MuteBehaviorEEUlRK11AQMESessionSA_E_PS8_Li0EEEvT1_SE_SE_SE_T0_
+ __ZNSt3__17__sort5B9foe220100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP15MEVADIdentifierLi0EEEvT1_S7_S7_S7_S7_T0_
+ __ZNSt3__17__sort5B9foe220100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN14NoteOffManager11NoteOffInfoELi0EEEvT1_S8_S8_S8_S8_T0_
+ __ZNSt3__17__sort5B9foe220100INS_17_ClassicAlgPolicyERZN17AudioTapSpecifierC1ENS_6vectorIjNS_9allocatorIjEEEENS2_12MuteBehaviorEEUlRK11AQMESessionSA_E_PS8_Li0EEEvT1_SE_SE_SE_SE_T0_
+ __ZNSt3__17__sort5B9foe220100INS_17_ClassicAlgPolicyERZZZN2AT11Translation19AUAsyncRendererHost9ConfigureEvENK3$_0clENS_6chrono10time_pointINS6_12steady_clockENS6_8durationIxNS_5ratioILl1ELl1000000000EEEEEEERK15AudioBufferListiENKUlRT_E_clINS_6vectorINS4_34TemporallyOrdereredAudioBufferListENS_9allocatorISM_EEEEEEDaSI_EUlRKSM_SS_E_PSM_Li0EEEvT1_SW_SW_SW_SW_T0_
+ __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB9foe220100IRP10MusicEventS6_EEvOT_OT0_
+ __ZNSt3__18__format14__parse_arg_idB9foe220100IPKcNS_26basic_format_parse_contextIcEEEENS0_21__parse_number_resultIT_EES7_S7_RT0_
+ __ZNSt3__18__format14__parse_numberB9foe220100IPKcEENS0_21__parse_number_resultIT_EES5_S5_
+ __ZNSt3__18__format15__output_bufferIcE11__transformB9foe220100IPcPFccEcEEvT_S7_T0_
+ __ZNSt3__18__format15__output_bufferIcE6__copyB9foe220100IcEEvNS_17basic_string_viewIT_NS_11char_traitsIS5_EEEE
+ __ZNSt3__18__format15__output_bufferIcE6__fillB9foe220100Emc
+ __ZNSt3__18__format15__output_bufferIcE9push_backB9foe220100Ec
+ __ZNSt3__18__format19__allocating_bufferIcE15__prepare_writeB9foe220100ERNS0_15__output_bufferIcEEm
+ __ZNSt3__18__format26__handle_replacement_fieldB9foe220100IPKcNS_26basic_format_parse_contextIcEENS_20basic_format_contextINS_20back_insert_iteratorINS0_15__output_bufferIcEEEEcEEEET_SC_SC_RT0_RT1_
+ __ZNSt3__18__invokeB9foe220100IJRZN15ActiveSoundList31RecordStopRequestForActiveSoundEjiE3$_0RNS_4pairIKjP15ActiveSoundInfoEEEEENS_20__invoke_result_implIvJDpT_EE4typeEDpOSB_
+ __ZNSt3__18__invokeB9foe220100IJRZZN15ActiveSoundListC1EvEUb0_E3$_1RNS_4pairIKjP15ActiveSoundInfoEEEEENS_20__invoke_result_implIvJDpT_EE4typeEDpOSB_
+ __ZNSt3__18__invokeB9foe220100IJRZZN15ActiveSoundListC1EvEUb_E3$_0RNS_4pairIKjP15ActiveSoundInfoEEEEENS_20__invoke_result_implIvJDpT_EE4typeEDpOSB_
+ __ZNSt3__18numpunctIcE2idE
+ __ZNSt3__18optionalI14AQMEIO_BindingE7emplaceB9foe220100IJR15AQIONodeManagerRPK10__CFStringELi0EEERS1_DpOT_
+ __ZNSt3__18optionalI14AQMEIO_BindingEaSB9foe220100IRKS1_Li0EEERS2_OT_
+ __ZNSt3__18optionalIN4swix17connection_configEEC1B9foe220100EOS3_
+ __ZNSt3__18optionalIN4swix6resultIJNS1_4dataEEEEEaSB9foe220100IS4_Li0EEERS5_OT_
+ __ZNSt3__18optionalIN5caulk9semaphoreEE7emplaceB9foe220100IJELi0EEERS2_DpOT_
+ __ZNSt3__18optionalIN8audioipc18SharedAudioBuffersEE7emplaceB9foe220100IJRjNS_4spanIKNS1_14ExtendedFormatELm18446744073709551615EEENS6_IhLm18446744073709551615EEEELi0EEERS2_DpOT_
+ __ZNSt3__18to_charsEPcS0_d
+ __ZNSt3__18to_charsEPcS0_dNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_dNS_12chars_formatEi
+ __ZNSt3__18to_charsEPcS0_e
+ __ZNSt3__18to_charsEPcS0_eNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_eNS_12chars_formatEi
+ __ZNSt3__18to_charsEPcS0_f
+ __ZNSt3__18to_charsEPcS0_fNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_fNS_12chars_formatEi
+ __ZNSt3__18try_lockB9foe220100IN5caulk23recursive_mutex_adapterINS1_22pooled_semaphore_mutexEEENS1_4mach21unfair_recursive_lockEEEiRT_RT0_
+ __ZNSt3__18try_lockB9foe220100IN5caulk4mach21unfair_recursive_lockENS1_23recursive_mutex_adapterINS1_22pooled_semaphore_mutexEEEEEiRT_RT0_
+ __ZNSt3__18try_lockB9foe220100IN5caulk4mach21unfair_recursive_lockES3_EEiRT_RT0_
+ __ZNSt3__19__unicode17__code_point_viewIcE9__consumeB9foe220100Ev
+ __ZNSt3__19__unicode33__extended_grapheme_cluster_break15__evaluate_noneB9foe220100EDiNS_44__extended_grapheme_custer_property_boundary10__propertyE
+ __ZNSt3__19allocatorI10MusicEventE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorI11AQMESessionE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorI14MEStreamTypeIDE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorI15MEVADIdentifierE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorI15MeterTrackEntryE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorI16AURateRampStructE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorI18AudioMetadataEventE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorI24AudioQueueParameterEventE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorI26AQBufferCreateDestroyEventE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorI26AudioObjectPropertyAddressE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorI30AQProcessingNodeImmediateEventE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorI32AudioSessionPropertyListenerInfoE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorI9TapSourceE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIN10applesauce2CF11TypeRefPairEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIN10applesauce2CF7TypeRefEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIN10applesauce2CF9NumberRefEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIN14NoteOffManager14ControlMessageEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIN16AudioQueueObject12AQRateChangeEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIN18AQOfflineMixerBase15StartQueueEventEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIN21VibeToHapticConverter11SegmentInfoEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIN2AQ6Server12RemoteClient5QueueEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIN8TempoMap10TempoEntryEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIN8audioipc18SharedAudioBuffers7ElementEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorINS_10shared_ptrI9TapSubmixEEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorINS_10shared_ptrIN10AQMEIO_HAL8IOStreamEEEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorINS_10unique_ptrI11IAQMEDeviceNS_14default_deleteIS2_EEEEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorINS_10unique_ptrI11MEConnectorNS_14default_deleteIS2_EEEEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorINS_10unique_ptrIN18PowerUsageWatchdog12ClientLoggerENS_14default_deleteIS3_EEEEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorINS_12basic_stringIcNS_11char_traitsIcEENS0_IcEEEEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorINS_4pairINS_10shared_ptrI11SynthOutputEEbEEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS0_IcEEEES6_EEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorINS_5tupleIJjPFvPvP16OpaqueAudioQueuejES2_EEEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorINS_8weak_ptrI25AQMEIO_NotificationClientEEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIP10AUNodeInfoE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIP11MCAudioUnitE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIP14AQIONodeClientE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIP14MEMixerChannelE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIP15InputDispatcherE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIP15XProcessingBaseE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIP19SSSActionPlayerBaseE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIP20MEOutputStreamClientE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIPKvE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIPN5boost8functionIFNS1_3msm4back11HandledEnumEvEEEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIPNS_4pairIN5boost8functionIFNS2_3msm4back11HandledEnumEvEEEbEEE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIPjE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIPmE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIfE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIiE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIjE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorImE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19allocatorIxE17allocate_at_leastB9foe220100Em
+ __ZNSt3__19remove_ifB9foe220100INS_11__wrap_iterIPNS_8weak_ptrIN5caulk17lifetime_observedINS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS6_EEEENS3_23shared_instance_managerIS6_E8observerEEEEEEEZNSB_14remove_expiredEvEUlRKT_E_EESH_SH_SH_T0_
+ __ZNSt3__1plB9foe220100IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEOS9_PKS6_
+ __ZNSt3__1plB9foe220100IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_OS9_
+ __ZNSt3__1plB9foe220100IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_PKS6_
+ __ZNSt3__1ssB9foe220100IcNS_11char_traitsIcEENS_9allocatorIcEEEEDaRKNS_12basic_stringIT_T0_T1_EESC_
+ __ZSt28__throw_bad_array_new_lengthB9foe220100v
+ __ZSt30__make_exception_ptr_via_throwB9foe220100INSt3__112future_errorEESt13exception_ptrRT_
+ __ZTI3$_0
+ __ZTINSt3__112format_errorE
+ __ZTS3$_0
+ __ZTSNSt3__112format_errorE
+ __ZTV10XPC_Object
+ __ZTV11MetricsBase
+ __ZTV12MemoryStream
+ __ZTV13HapticMetrics
+ __ZTV16TArrayMarshallerI20SplicingRequirementsE
+ __ZTV18HapticAudioMetrics
+ __ZTV19OfflineFOAProcessor
+ __ZTV8TFileBSD
+ __ZTVN10__cxxabiv116__enum_type_infoE
+ __ZTVN12CADeprecated17XMachPortServicer12DispatchImplE
+ __ZTVN12CADeprecated22XMachPortDeathListenerE
+ __ZTVN12CADeprecated7CAGuardE
+ __ZTVN12CADeprecated7CAMutexE
+ __ZTVN12CADeprecated9CAPThreadE
+ __ZTVN20CAAudioChannelLayout16RefCountedLayoutE
+ __ZTVN2CA12OpaqueObject3RefIN5Phase13ServerManagerEjEE
+ __ZTVN5caulk10concurrent7details12message_callIRZN11ClientEntry16unduckOtherAudioEmE3$_0JEEE
+ __ZTVN5caulk10concurrent7details12message_callIRZN11ClientEntry22handleSequenceFinishedEmE3$_1JEEE
+ __ZTVN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry16unduckOtherAudioEmE3$_0JEEE
+ __ZTVN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry22handleSequenceFinishedEmE3$_1JEEE
+ __ZTVN5caulk10concurrent7details15rt_message_callIRZZN11ClientEntry18playSequenceWithIDEmddENK3$_0clINSt3__110shared_ptrI14HapticSequenceEEEEDaRKT_EUlvE_JEEE
+ __ZTVNSt3__110__function6__funcIZN13ServerManager13setupListenerEvE3$_6FvbEEE
+ __ZTVNSt3__110__function6__funcIZN13ServerManager25handleRouteChangeForEntryENS_10shared_ptrI11ClientEntryEEP8NSStringNS_8optionalIbEEE3$_0FvbEEE
+ __ZTVNSt3__110__function6__funcIZN5CALog5Scope34SetPriorityThresholdFromPreferenceEPK10__CFStringS6_E3$_0FvN5caulk14cf_preferences9log_levelEEEE
+ __ZTVNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerINS3_9log_levelEEEbPK10__CFStringS9_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSB_EEEEUlSE_E_FbSE_EEE
+ __ZTVNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIbEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EEE
+ __ZTVNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIdEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EEE
+ __ZTVNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor11add_handlerIxEEbPK10__CFStringS8_PFNS_8optionalIT_EEPKvERKNS_8functionIFvSA_EEEEUlSD_E_FbSD_EEE
+ __ZTVNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RbEUlbE_FvbEEE
+ __ZTVNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RfEUldE_FvdEEE
+ __ZTVNSt3__110__function6__funcIZN5caulk14cf_preferences7monitor3addEPK10__CFStringS7_RiEUlxE_FvxEEE
+ __ZTVNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERKNS_10shared_ptrI11SynthOutputEEEUlvE_FvvEEE
+ __ZTVNSt3__112format_errorE
+ __ZTVNSt3__120__shared_ptr_emplaceI13HapticMetricsNS_9allocatorIS1_EEEE
+ __ZTVNSt3__120__shared_ptr_emplaceI18HapticAudioMetricsNS_9allocatorIS1_EEEE
+ __ZTVNSt3__120__shared_ptr_emplaceIN12CADeprecated16XMachReceivePortENS_9allocatorIS2_EEEE
+ __ZThn144_N14DSP_Routing_VP25IO_DeviceStoppedFromBelowEbb
+ __ZThn16_N20AudioQueueXPC_Client5StartEj19XAudioTimeStampBasejyy
+ __ZThn16_N20AudioQueueXPC_Server5StartEj19XAudioTimeStampBasejyy
+ __ZThn288_N16AudioQueueObject18ToAudioQueueObjectEv
+ __ZThn288_N16AudioQueueObjectD0Ev
+ __ZThn288_N16AudioQueueObjectD1Ev
+ __ZThn288_N17ZenAQIONodeClientD0Ev
+ __ZThn288_N17ZenAQIONodeClientD1Ev
+ __ZThn304_N16AudioQueueObject21SSP_StartTimeResolvedEx15XAudioTimeStamp
+ __ZThn304_N16AudioQueueObject30SSP_ScaledToUnscaledSampleTimeEx
+ __ZThn304_N16AudioQueueObjectD0Ev
+ __ZThn304_N16AudioQueueObjectD1Ev
+ __ZThn48_NK15AudioQueueOwner11DescriptionEv
+ __ZThn80_N11AQTapIONode25IO_DeviceStoppedFromBelowEbb
+ __ZThn80_N12CADeprecated11XMachServerD0Ev
+ __ZThn80_N12CADeprecated11XMachServerD1Ev
+ __ZThn88_N11AQAC3IONode25IO_DeviceStoppedFromBelowEbb
+ __ZThn88_N18AQHapticOutputNode25IO_DeviceStoppedFromBelowEbb
+ __ZThn8_N10AQMEIO_DSP25IO_DeviceStoppedFromBelowEbb
+ __ZZ23gOfflineFOAProcessorLogvE6global
+ __ZZ41isAudioTranscriptionAnalysisServerEnabledvE7enabled
+ __ZZ66-[AVHapticServer buildActiveProcessesForPowerLogForAudio:haptics:]ENK4$_11clERKNSt3__13setIiNS0_4lessIiEENS0_9allocatorIiEEEE
+ __ZZL13GetAcousticIDvE13optionalValue.5592
+ __ZZL13GetAcousticIDvENKUlvE_clEv.5591
+ __ZZL15CPMSLibraryCorePPcE16frameworkLibrary.0.10498
+ __ZZL15CPMSLibraryCorePPcE16frameworkLibrary.0.3794
+ __ZZL15CPMSLibraryCorePPcE16frameworkLibrary.0.6653
+ __ZZL17getCPMSAgentClassvE9softClass.0.3764
+ __ZZL17getCPMSAgentClassvE9softClass.0.6651
+ __ZZL19AVFAudioLibraryCorePPcE16frameworkLibrary.0.12858
+ __ZZL20CoreMediaLibraryCorePPcE16frameworkLibrary.0.5286
+ __ZZL20CoreMediaLibraryCorePPcE16frameworkLibrary.0.7407
+ __ZZL21GetSpatialMetadataSPIvE19sSpatialMetadataSPI.11525
+ __ZZL21GetSpatialMetadataSPIvE23sSpatialMetadataSPIOnce.11524
+ __ZZL21getAVAudioFormatClassvE9softClass.0.12001
+ __ZZL22sOrchestratorServerLogvE4sLog
+ __ZZL23AudioCaptureLibraryCorePPcE16frameworkLibrary.0
+ __ZZL23MediaToolboxLibraryCorePPcE16frameworkLibrary.0.7399
+ __ZZL28getATATranslationClientClassvE9softClass.0
+ __ZZL29AudioSessionServerLibraryCorePPcE16frameworkLibrary.0.8646
+ __ZZL29getCPMSClientDescriptionClassvE9softClass.0.3773
+ __ZZL31resolveHapticPatternLibraryPathvENK3$_0clERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZZL32getAudioCapturerDestroySymbolLocvE3ptr.0
+ __ZZL33CoreAudioOrchestrationLibraryCorePPcE16frameworkLibrary.0
+ __ZZL33getAudioCapturerFilePathSymbolLocvE3ptr.0
+ __ZZL33getCMBaseObjectGetVTableSymbolLocvE3ptr.0.5282
+ __ZZL33getCMBaseObjectGetVTableSymbolLocvE3ptr.0.7404
+ __ZZL34getAudioCaptureInitializeSymbolLocvE3ptr.0
+ __ZZL36getAudioCapturerWriteBufferSymbolLocvE3ptr.0
+ __ZZL37AudioTranscriptionAnalysisLibraryCorePPcE16frameworkLibrary.0
+ __ZZL37getAudioCapturerWritePacketsSymbolLocvE3ptr.0
+ __ZZL40getAudioCapturerWriteBufferListSymbolLocvE3ptr.0
+ __ZZL46getAudioCapturerCreateForPCMAudioDataSymbolLocvE3ptr.0
+ __ZZL46getCreatePasscodeDetectorClientPortalSymbolLocvE3ptr.0
+ __ZZL50getAudioCapturerCreateForEncodedAudioDataSymbolLocvE3ptr.0
+ __ZZL58getFigCPECryptorCreateCryptorFromSerializedRecipeSymbolLocvE3ptr.0.7395
+ __ZZN10XAudioUnit6RenderEPjPK14AudioTimeStampjjP15AudioBufferListENKUlvE_clEv
+ __ZZN11MetricsBaseC1EvE14sReporterToken
+ __ZZN12CASerializer14PrepareToWriteEjE3pad
+ __ZZN17LegacyHapticSynth10initializeEvENK3$_0clERKNSt3__110shared_ptrI11SynthOutputEE
+ __ZZN17LegacyHapticSynth11stopRunningEbbjENK3$_1clERKNSt3__110shared_ptrI11SynthOutputEE
+ __ZZN17LegacyHapticSynth11stopRunningEbbjENK3$_3clERKNSt3__110shared_ptrI11SynthOutputEE
+ __ZZN19SharableMemoryBlock10InitServerEmRNS_11ServerTokenEE13gBufSerialNum
+ __ZZN20AudioCapturerManager17RegisterListenersEvE9onceToken
+ __ZZN20AudioCapturerManagerC1EOKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEiE9onceToken
+ __ZZN21PlatformUtilities_iOS14GetProductTypeEvE15sCompletedCheck
+ __ZZN21PlatformUtilities_iOS14GetProductTypeEvE5sType
+ __ZZN21PlatformUtilities_iOS19ProductIsMuseDeviceEvE12isMuseDevice
+ __ZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_2clERKNSt3__110shared_ptrI11SynthOutputEE
+ __ZZN2AQ3API9Interface31AudioQueueGetPassThroughFormatsEvE7formats
+ __ZZN2AQ3API9Interface31AudioQueueGetPassThroughFormatsEvE8onceflag
+ __ZZN5caulk13random_uint64EvE6engine
+ __ZZN5caulk23inplace_function_detail9rt_vtableIKN13ServerManager12SynthCommandEJEEC1IZNS2_12DoRenderProcERK14AudioTimeStampjE3$_1EENS0_7wrapperIT_EEENUlPvE0_8__invokeESE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIKN13ServerManager12SynthCommandEJEEC1IZNS2_12DoRenderProcERK14AudioTimeStampjE3$_1EENS0_7wrapperIT_EEENUlPvE_8__invokeESE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIKN13ServerManager12SynthCommandEJEEC1IZNS2_12DoRenderProcERK14AudioTimeStampjE3$_1EENS0_7wrapperIT_EEENUlPvSE_E0_8__invokeESE_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIKN13ServerManager12SynthCommandEJEEC1IZNS2_12DoRenderProcERK14AudioTimeStampjE3$_1EENS0_7wrapperIT_EEENUlPvSE_E_8__invokeESE_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1EvENUlPvE_8__invokeES3_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1EvENUlPvOiE_8__invokeES3_S4_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1EvENUlPvS3_E0_8__invokeES3_S3_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1EvENUlPvS3_E_8__invokeES3_S3_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM10BeginPauseEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvE_8__invokeESE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM10BeginPauseEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvOiE_8__invokeESE_SF_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM10BeginPauseEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvSE_E0_8__invokeESE_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM10BeginPauseEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvSE_E_8__invokeESE_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI12NSDictionaryEEEEiRKT_EUliE_EENS0_7wrapperISA_EEENUlPvE_8__invokeESG_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI12NSDictionaryEEEEiRKT_EUliE_EENS0_7wrapperISA_EEENUlPvOiE_8__invokeESG_SH_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI12NSDictionaryEEEEiRKT_EUliE_EENS0_7wrapperISA_EEENUlPvSG_E0_8__invokeESG_SG_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI12NSDictionaryEEEEiRKT_EUliE_EENS0_7wrapperISA_EEENUlPvSG_E_8__invokeESG_SG_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI6NSDataEEEEiRKT_EUliE_EENS0_7wrapperISA_EEENUlPvE_8__invokeESG_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI6NSDataEEEEiRKT_EUliE_EENS0_7wrapperISA_EEENUlPvOiE_8__invokeESG_SH_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI6NSDataEEEEiRKT_EUliE_EENS0_7wrapperISA_EEENUlPvSG_E0_8__invokeESG_SG_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI6NSDataEEEEiRKT_EUliE_EENS0_7wrapperISA_EEENUlPvSG_E_8__invokeESG_SG_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI7NSArrayEEEEiRKT_EUliE_EENS0_7wrapperISA_EEENUlPvE_8__invokeESG_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI7NSArrayEEEEiRKT_EUliE_EENS0_7wrapperISA_EEENUlPvOiE_8__invokeESG_SH_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI7NSArrayEEEEiRKT_EUliE_EENS0_7wrapperISA_EEENUlPvSG_E0_8__invokeESG_SG_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI7NSArrayEEEEiRKT_EUliE_EENS0_7wrapperISA_EEENUlPvSG_E_8__invokeESG_SG_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4PlayEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvE_8__invokeESE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4PlayEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvOiE_8__invokeESE_SF_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4PlayEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvSE_E0_8__invokeESE_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4PlayEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvSE_E_8__invokeESE_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4SeekEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvE_8__invokeESE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4SeekEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvOiE_8__invokeESE_SF_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4SeekEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvSE_E0_8__invokeESE_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4SeekEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvSE_E_8__invokeESE_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4StopEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvE_8__invokeESE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4StopEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvOiE_8__invokeESE_SF_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4StopEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvSE_E0_8__invokeESE_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM4StopEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvSE_E_8__invokeESE_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM5StartEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvE_8__invokeESE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM5StartEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvOiE_8__invokeESE_SF_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM5StartEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvSE_E0_8__invokeESE_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM5StartEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvSE_E_8__invokeESE_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM6DetachEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvE_8__invokeESE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM6DetachEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvOiE_8__invokeESE_SF_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM6DetachEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvSE_E0_8__invokeESE_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM6DetachEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvSE_E_8__invokeESE_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM6ResumeEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvE_8__invokeESE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM6ResumeEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvOiE_8__invokeESE_SF_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM6ResumeEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvSE_E0_8__invokeESE_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM6ResumeEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvSE_E_8__invokeESE_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM7PrepareEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvE_8__invokeESE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM7PrepareEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvOiE_8__invokeESE_SF_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM7PrepareEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvSE_E0_8__invokeESE_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM7PrepareEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvSE_E_8__invokeESE_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM9ForceStopEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvE_8__invokeESE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM9ForceStopEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvOiE_8__invokeESE_SF_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM9ForceStopEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvSE_E0_8__invokeESE_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJiEEC1IZN12SequenceImpl9sendEventIN11SequenceFSM9ForceStopEEEiRKT_EUliE_EENS0_7wrapperIS8_EEENUlPvSE_E_8__invokeESE_SE_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJmEEC1EvENUlPvE_8__invokeES3_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJmEEC1EvENUlPvOmE_8__invokeES3_S4_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJmEEC1EvENUlPvS3_E0_8__invokeES3_S3_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJmEEC1EvENUlPvS3_E_8__invokeES3_S3_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJmEEC1IZN11ClientEntry17doPrepareSequenceENSt3__110shared_ptrI14HapticSequenceEENS_16inplace_functionIFvmELm32ELm8ENS0_6vtableEEEE3$_0EENS0_7wrapperIT_EEENUlPvE_8__invokeESH_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJmEEC1IZN11ClientEntry17doPrepareSequenceENSt3__110shared_ptrI14HapticSequenceEENS_16inplace_functionIFvmELm32ELm8ENS0_6vtableEEEE3$_0EENS0_7wrapperIT_EEENUlPvOmE_8__invokeESH_SI_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJmEEC1IZN11ClientEntry17doPrepareSequenceENSt3__110shared_ptrI14HapticSequenceEENS_16inplace_functionIFvmELm32ELm8ENS0_6vtableEEEE3$_0EENS0_7wrapperIT_EEENUlPvSH_E0_8__invokeESH_SH_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJmEEC1IZN11ClientEntry17doPrepareSequenceENSt3__110shared_ptrI14HapticSequenceEENS_16inplace_functionIFvmELm32ELm8ENS0_6vtableEEEE3$_0EENS0_7wrapperIT_EEENUlPvSH_E_8__invokeESH_SH_
+ __ZZN8TFileBSDC1EPK7__CFURLE4once
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeI20HapticPlayerPriorityjEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_jEENS_4hashIS2_EENS_8equal_toIS2_EEEENS_21__unordered_map_equalIS2_S7_SB_S9_EENS_9allocatorIS7_EEE16__emplace_uniqueB9foe220100IJRKNS_21piecewise_construct_tENS_5tupleIJOS2_EEENSM_IJEEEEEENS5_INS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEEDpOT_ENKUlRS6_SL_OSO_OSP_E_clES10_SL_S11_S12_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN20AudioImpulseInjector4Impl20NotificationListener17NotificationStateEEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_SB_EENS_4hashIS7_EENS_8equal_toIS7_EEEENS_21__unordered_map_equalIS7_SG_SK_SI_EENS5_ISG_EEE16__emplace_uniqueB9foe220100IJRKNS_21piecewise_construct_tENS_5tupleIJRSF_EEENSU_IJEEEEEENSE_INS_15__hash_iteratorIPNS_11__hash_nodeISC_PvEEEEbEEDpOT_ENKUlSV_ST_OSW_OSX_E_clESV_ST_S18_S19_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_bEENS_4hashIS7_EENS_8equal_toIS7_EEEENS_21__unordered_map_equalIS7_SC_SG_SE_EENS5_ISC_EEE16__emplace_uniqueB9foe220100IJRKNS_21piecewise_construct_tENS_5tupleIJRSB_EEENSQ_IJEEEEEENSA_INS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEEbEEDpOT_ENKUlSR_SP_OSS_OST_E_clESR_SP_S14_S15_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_6vectorIhNS_9allocatorIhEEEEEENS_22__unordered_map_hasherIjNS_4pairIKjS5_EENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjSA_SE_SC_EENS3_ISA_EEE16__emplace_uniqueB9foe220100IJRKNS_21piecewise_construct_tENS_5tupleIJRS9_EEENSO_IJEEEEEENS8_INS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEEDpOT_ENKUlSP_SN_OSQ_OSR_E_clESP_SN_S12_S13_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIjiEENS_22__unordered_map_hasherIjNS_4pairIKjiEENS_4hashIjEENS_8equal_toIjEEEENS_21__unordered_map_equalIjS6_SA_S8_EENS_9allocatorIS6_EEE16__emplace_uniqueB9foe220100IJRKNS_21piecewise_construct_tENS_5tupleIJRS5_EEENSL_IJEEEEEENS4_INS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEEDpOT_ENKUlSM_SK_OSN_OSO_E_clESM_SK_SZ_S10_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeImU13block_pointerFv28AUVoiceIOSpeechActivityEventEEENS_22__unordered_map_hasherImNS_4pairIKmS4_EENS_4hashImEENS_8equal_toImEEEENS_21__unordered_map_equalImS9_SD_SB_EENS_9allocatorIS9_EEE16__emplace_uniqueB9foe220100IJRKNS_21piecewise_construct_tENS_5tupleIJRS8_EEENSO_IJEEEEEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEEDpOT_ENKUlSP_SN_OSQ_OSR_E_clESP_SN_S12_S13_
+ __ZZNSt3__112__hash_tableIPN20AudioImpulseInjector4ImplENS_4hashIS3_EENS_8equal_toIS3_EENS_9allocatorIS3_EEE16__emplace_uniqueB9foe220100IJRKS3_EEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEEDpOT_ENKUlSD_SD_E_clESD_SD_
+ __ZZNSt3__112__hash_tableIPvNS_4hashIS1_EENS_8equal_toIS1_EENS_9allocatorIS1_EEE16__emplace_uniqueB9foe220100IJRKS1_EEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS1_S1_EEEEbEEDpOT_ENKUlSB_SB_E_clESB_SB_
+ __ZZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEE16__emplace_uniqueB9foe220100IJRKjEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIjPvEEEEbEEDpOT_ENKUlSA_SA_E_clESA_SA_
+ __ZZNSt3__16vectorI15MEVADIdentifierNS_9allocatorIS1_EEE12emplace_backIJ14MEDeviceTypeID3$_1RPK10__CFStringEEERS1_DpOT_ENKUlvE0_clEv
+ __ZZNSt3__16vectorI15MEVADIdentifierNS_9allocatorIS1_EEE12emplace_backIJR14MEDeviceTypeIDRjRN10applesauce2CF9StringRefEEEERS1_DpOT_ENKUlvE0_clEv
+ __ZZNSt3__16vectorINS_5tupleIJjPFvPvP16OpaqueAudioQueuejES2_EEENS_9allocatorIS7_EEE12emplace_backIJRjRS6_RS2_EEERS7_DpOT_ENKUlvE0_clEv
+ __ZZZ47-[AVHapticServer forceUnprewarmEligibleClients]ENK3$_9clEPK22AVHapticServerInstanceRKNSt3__110shared_ptrI11ClientEntryEEENUlvE_D1Ev
+ ___53-[AVHapticServer listener:shouldAcceptNewConnection:]_block_invoke.469
+ ___53-[AVHapticServer listener:shouldAcceptNewConnection:]_block_invoke.473
+ ___53-[AVHapticServer listener:shouldAcceptNewConnection:]_block_invoke.474
+ ___59-[AVVoiceTriggerServer listener:shouldAcceptNewConnection:]_block_invoke.168
+ ___59-[AVVoiceTriggerServer listener:shouldAcceptNewConnection:]_block_invoke_2.170
+ ___65-[AVHapticServerInstance setupAudioSessionFromID:isShared:error:]_block_invoke.34
+ ___Block_byref_object_copy_.100
+ ___Block_byref_object_copy_.106
+ ___Block_byref_object_copy_.112
+ ___Block_byref_object_copy_.119
+ ___Block_byref_object_copy_.12116
+ ___Block_byref_object_copy_.124
+ ___Block_byref_object_copy_.12950
+ ___Block_byref_object_copy_.130
+ ___Block_byref_object_copy_.135
+ ___Block_byref_object_copy_.142
+ ___Block_byref_object_copy_.145
+ ___Block_byref_object_copy_.14719
+ ___Block_byref_object_copy_.149
+ ___Block_byref_object_copy_.1884
+ ___Block_byref_object_copy_.2023
+ ___Block_byref_object_copy_.4524
+ ___Block_byref_object_copy_.5942
+ ___Block_byref_object_copy_.7708
+ ___Block_byref_object_copy_.81
+ ___Block_byref_object_copy_.84
+ ___Block_byref_object_copy_.874
+ ___Block_byref_object_copy_.88
+ ___Block_byref_object_copy_.94
+ ___Block_byref_object_dispose_.101
+ ___Block_byref_object_dispose_.107
+ ___Block_byref_object_dispose_.113
+ ___Block_byref_object_dispose_.120
+ ___Block_byref_object_dispose_.12117
+ ___Block_byref_object_dispose_.125
+ ___Block_byref_object_dispose_.12951
+ ___Block_byref_object_dispose_.131
+ ___Block_byref_object_dispose_.136
+ ___Block_byref_object_dispose_.143
+ ___Block_byref_object_dispose_.146
+ ___Block_byref_object_dispose_.14720
+ ___Block_byref_object_dispose_.150
+ ___Block_byref_object_dispose_.1885
+ ___Block_byref_object_dispose_.2024
+ ___Block_byref_object_dispose_.4525
+ ___Block_byref_object_dispose_.5943
+ ___Block_byref_object_dispose_.7709
+ ___Block_byref_object_dispose_.82
+ ___Block_byref_object_dispose_.85
+ ___Block_byref_object_dispose_.875
+ ___Block_byref_object_dispose_.89
+ ___Block_byref_object_dispose_.95
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.12708
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.12936
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.13098
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.2180
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.2901
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.3958
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.5346
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.6232
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.6686
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.9657
+ ____Z27AudioQueueInternalStop_Syncjb_block_invoke
+ ____Z28AudioStatisticsLibraryLoaderv_block_invoke.12287
+ ____Z28AudioStatisticsLibraryLoaderv_block_invoke.2926
+ ____Z28AudioStatisticsLibraryLoaderv_block_invoke.9100
+ ____Z28CMClientNotificationCallbackP26opaqueCMNotificationCenterPKvPK10__CFStringS2_S2__block_invoke_2
+ ____ZL15CPMSLibraryCorePPc_block_invoke.10499
+ ____ZL15CPMSLibraryCorePPc_block_invoke.3795
+ ____ZL15CPMSLibraryCorePPc_block_invoke.6654
+ ____ZL17getCPMSAgentClassv_block_invoke.3765
+ ____ZL17getCPMSAgentClassv_block_invoke.6652
+ ____ZL19AVFAudioLibraryCorePPc_block_invoke.12859
+ ____ZL20CoreMediaLibraryCorePPc_block_invoke.5287
+ ____ZL20CoreMediaLibraryCorePPc_block_invoke.7408
+ ____ZL21GetSpatialMetadataSPIv_block_invoke.11533
+ ____ZL21getAVAudioFormatClassv_block_invoke.12002
+ ____ZL23AudioCaptureLibraryCorePPc_block_invoke
+ ____ZL23MediaToolboxLibraryCorePPc_block_invoke.7400
+ ____ZL28getATATranslationClientClassv_block_invoke
+ ____ZL29AudioSessionServerLibraryCorePPc_block_invoke.8647
+ ____ZL29getCPMSClientDescriptionClassv_block_invoke.3774
+ ____ZL30SynthOutputNotificationHandlerP22__CFNotificationCenterPvPK10__CFStringPKvPK14__CFDictionary_block_invoke
+ ____ZL31SynthOutputNotificationCallbackP22__CFNotificationCenterPvPK10__CFStringPKvPK14__CFDictionary_block_invoke
+ ____ZL32getAudioCapturerDestroySymbolLocv_block_invoke
+ ____ZL33CoreAudioOrchestrationLibraryCorePPc_block_invoke
+ ____ZL33getAudioCapturerFilePathSymbolLocv_block_invoke
+ ____ZL33getCMBaseObjectGetVTableSymbolLocv_block_invoke.5283
+ ____ZL33getCMBaseObjectGetVTableSymbolLocv_block_invoke.7405
+ ____ZL34getAudioCaptureInitializeSymbolLocv_block_invoke
+ ____ZL36getAudioCapturerWriteBufferSymbolLocv_block_invoke
+ ____ZL37AudioTranscriptionAnalysisLibraryCorePPc_block_invoke
+ ____ZL37getAudioCapturerWritePacketsSymbolLocv_block_invoke
+ ____ZL40getAudioCapturerWriteBufferListSymbolLocv_block_invoke
+ ____ZL46getAudioCapturerCreateForPCMAudioDataSymbolLocv_block_invoke
+ ____ZL46getCreatePasscodeDetectorClientPortalSymbolLocv_block_invoke
+ ____ZL50getAudioCapturerCreateForEncodedAudioDataSymbolLocv_block_invoke
+ ____ZL58getFigCPECryptorCreateCryptorFromSerializedRecipeSymbolLocv_block_invoke.7396
+ ____ZN11MetricsBaseC2Ev_block_invoke
+ ____ZN11MetricsBaseC2Ev_block_invoke.11
+ ____ZN11MetricsBaseC2Ev_block_invoke_2
+ ____ZN11SynthOutput29IONode_DeviceStoppedFromBelowEb_block_invoke
+ ____ZN12CADeprecated15XBasicMIGServer22SetServerDispatchQueueERKN10applesauce8dispatch2v15queueE_block_invoke
+ ____ZN12CADeprecated15XBasicMIGServer22SetServerDispatchQueueERKN10applesauce8dispatch2v15queueE_block_invoke.9
+ ____ZN12CADeprecated17XMachPortServicer12DispatchImplD2Ev_block_invoke
+ ____ZN12CADeprecated22XMachPortDeathListener33SetDeathNotificationDispatchQueueERKN10applesauce8dispatch2v15queueE_block_invoke
+ ____ZN13ServerManager23setClientPlayerBehaviorENSt3__110shared_ptrI11ClientEntryEEmP8NSString_block_invoke
+ ____ZN14SystemListener38getInitialSystemSoundsAndHapticsVolumeEv_block_invoke
+ ____ZN14XPC_Connection10InitializeEv_block_invoke
+ ____ZN16AudioQueueObject27HandlePauseDueToRouteChangeEv_block_invoke
+ ____ZN16AudioQueueObject27HandlePauseDueToRouteChangeEv_block_invoke_2
+ ____ZN16AudioQueueObject29IONode_DeviceStoppedFromBelowEb_block_invoke
+ ____ZN17LegacyHapticSynth25hardwareSampleRateChangedENSt3__110shared_ptrI11SynthOutputEE_block_invoke
+ ____ZN19HapticServerManager26SetupVADRoutingObservationEj_block_invoke.6
+ ____ZN20AudioCapturerManager17RegisterListenersEv_block_invoke
+ ____ZN20AudioCapturerManager17RegisterListenersEv_block_invoke.14338
+ ____ZN20AudioCapturerManagerC2EOKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEi_block_invoke
+ ____ZN20AudioQueueXPC_Bridge5StartEj19XAudioTimeStampBasejyy_block_invoke
+ ____ZN20AudioQueueXPC_Server5StartEj19XAudioTimeStampBasejyy_block_invoke
+ ____ZN21ThreadSafeHeadTracker10InitializeEv_block_invoke.79
+ ____ZN21ThreadSafeHeadTracker10InitializeEv_block_invoke.83
+ ____ZN21ThreadSafeHeadTracker10InitializeEv_block_invoke.89
+ ____ZN22MultiOutputHapticSynth25hardwareSampleRateChangedENSt3__110shared_ptrI11SynthOutputEE_block_invoke
+ ____ZN24AVVoiceTriggerServerImpl10InitializeEv_block_invoke.309
+ ____ZN24AVVoiceTriggerServerImpl10InitializeEv_block_invoke.311
+ ____ZN24AVVoiceTriggerServerImpl10InitializeEv_block_invoke_2.312
+ ____ZN2AT11Translation16TranslatorClient28getPreferredInputAudioFormatEv_block_invoke
+ ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.10788
+ ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.11521
+ ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.13973
+ ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.2206
+ ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.3222
+ ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.3576
+ ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.5141
+ ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.7284
+ ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.8956
+ ____ZN2AT13DispatchBlockEPU28objcproto17OS_dispatch_queue8NSObjectU13block_pointerFvvEbPKcS6_iyy_block_invoke.7359
+ ____ZN5Phase13ServerManager5startEv_block_invoke.29
+ ____ZN8TFileBSDC2EPK7__CFURL_block_invoke
+ ____ZZ44-[AVHapticServer forceStopIdleDaemonClients]ENK3$_5clEPK22AVHapticServerInstanceRKNSt3__110shared_ptrI11ClientEntryEE_block_invoke
+ ____ZZ47-[AVHapticServer forceUnprewarmEligibleClients]ENK3$_9clEPK22AVHapticServerInstanceRKNSt3__110shared_ptrI11ClientEntryEE_block_invoke
+ ____ZZ55-[AVHapticServer forceStopIdleBackgroundRunningClients]ENK3$_7clEPK22AVHapticServerInstanceRKNSt3__110shared_ptrI11ClientEntryEE_block_invoke
+ ____ZZN11ClientEntry16unduckOtherAudioEmENK3$_0clEv_block_invoke
+ ___block_descriptor_40_ea8_32c68_ZTSKZZN19HapticServerManager26SetupVADRoutingObservationEjEUb_E3$_1_e5_v8?0l
+ ___block_descriptor_56_ea8_32c132_ZTSKZZ44-[AVHapticServer forceStopIdleDaemonClients]ENK3$_5clEPK22AVHapticServerInstanceRKNSt3__110shared_ptrI11ClientEntryEEEUlvE__e5_v8?0l
+ ___block_descriptor_56_ea8_32c143_ZTSKZZ55-[AVHapticServer forceStopIdleBackgroundRunningClients]ENK3$_7clEPK22AVHapticServerInstanceRKNSt3__110shared_ptrI11ClientEntryEEEUlvE__e5_v8?0l
+ ___block_descriptor_56_ea8_32c36_ZTSNSt3__18weak_ptrI11ClientEntryEE_e5_v8?0l
+ ___block_descriptor_56_ea8_40c36_ZTSNSt3__18weak_ptrI11SynthOutputEE_e5_v8?0l
+ ___block_descriptor_56_ea8_40c39_ZTSNSt3__110shared_ptrI11SynthOutputEE_e5_v8?0l
+ ___block_descriptor_64_ea8_32c135_ZTSKZZ47-[AVHapticServer forceUnprewarmEligibleClients]ENK3$_9clEPK22AVHapticServerInstanceRKNSt3__110shared_ptrI11ClientEntryEEEUlvE__e5_v8?0l
+ ___block_descriptor_72_ea8_32s40r56c39_ZTSNSt3__110shared_ptrI11ClientEntryEE_e5_v8?0l
+ ___block_descriptor_tmp.1.12978
+ ___block_descriptor_tmp.10.10807
+ ___block_descriptor_tmp.10.13083
+ ___block_descriptor_tmp.10.5203
+ ___block_descriptor_tmp.10.7285
+ ___block_descriptor_tmp.10.7348
+ ___block_descriptor_tmp.103.14726
+ ___block_descriptor_tmp.105
+ ___block_descriptor_tmp.105.14725
+ ___block_descriptor_tmp.10572
+ ___block_descriptor_tmp.10784
+ ___block_descriptor_tmp.11.10808
+ ___block_descriptor_tmp.11.11669
+ ___block_descriptor_tmp.11.5138
+ ___block_descriptor_tmp.11379
+ ___block_descriptor_tmp.117
+ ___block_descriptor_tmp.118
+ ___block_descriptor_tmp.122
+ ___block_descriptor_tmp.123
+ ___block_descriptor_tmp.12490
+ ___block_descriptor_tmp.12638
+ ___block_descriptor_tmp.12706
+ ___block_descriptor_tmp.128
+ ___block_descriptor_tmp.129
+ ___block_descriptor_tmp.129.14717
+ ___block_descriptor_tmp.1293
+ ___block_descriptor_tmp.12967
+ ___block_descriptor_tmp.13115
+ ___block_descriptor_tmp.132.14722
+ ___block_descriptor_tmp.133
+ ___block_descriptor_tmp.134
+ ___block_descriptor_tmp.13570
+ ___block_descriptor_tmp.13970
+ ___block_descriptor_tmp.14.11671
+ ___block_descriptor_tmp.141
+ ___block_descriptor_tmp.143
+ ___block_descriptor_tmp.144
+ ___block_descriptor_tmp.147
+ ___block_descriptor_tmp.14732
+ ___block_descriptor_tmp.148
+ ___block_descriptor_tmp.15.11658
+ ___block_descriptor_tmp.15.5142
+ ___block_descriptor_tmp.1547
+ ___block_descriptor_tmp.158
+ ___block_descriptor_tmp.159
+ ___block_descriptor_tmp.164
+ ___block_descriptor_tmp.168
+ ___block_descriptor_tmp.1692
+ ___block_descriptor_tmp.198
+ ___block_descriptor_tmp.200
+ ___block_descriptor_tmp.2025
+ ___block_descriptor_tmp.203
+ ___block_descriptor_tmp.217
+ ___block_descriptor_tmp.219
+ ___block_descriptor_tmp.2193
+ ___block_descriptor_tmp.220
+ ___block_descriptor_tmp.2203
+ ___block_descriptor_tmp.221
+ ___block_descriptor_tmp.221.9655
+ ___block_descriptor_tmp.222
+ ___block_descriptor_tmp.223
+ ___block_descriptor_tmp.226
+ ___block_descriptor_tmp.227
+ ___block_descriptor_tmp.24.3223
+ ___block_descriptor_tmp.25.3168
+ ___block_descriptor_tmp.254
+ ___block_descriptor_tmp.255
+ ___block_descriptor_tmp.263
+ ___block_descriptor_tmp.27
+ ___block_descriptor_tmp.27.11607
+ ___block_descriptor_tmp.276
+ ___block_descriptor_tmp.28
+ ___block_descriptor_tmp.2853
+ ___block_descriptor_tmp.2875
+ ___block_descriptor_tmp.288
+ ___block_descriptor_tmp.3.10785
+ ___block_descriptor_tmp.3.2019
+ ___block_descriptor_tmp.3.5431
+ ___block_descriptor_tmp.3.6198
+ ___block_descriptor_tmp.3.7234
+ ___block_descriptor_tmp.30.10789
+ ___block_descriptor_tmp.307
+ ___block_descriptor_tmp.321
+ ___block_descriptor_tmp.3220
+ ___block_descriptor_tmp.333
+ ___block_descriptor_tmp.335
+ ___block_descriptor_tmp.343
+ ___block_descriptor_tmp.345
+ ___block_descriptor_tmp.3486
+ ___block_descriptor_tmp.349
+ ___block_descriptor_tmp.3590
+ ___block_descriptor_tmp.4.5168
+ ___block_descriptor_tmp.49
+ ___block_descriptor_tmp.498
+ ___block_descriptor_tmp.5.5378
+ ___block_descriptor_tmp.5.9271
+ ___block_descriptor_tmp.50
+ ___block_descriptor_tmp.50.6231
+ ___block_descriptor_tmp.503
+ ___block_descriptor_tmp.507
+ ___block_descriptor_tmp.511
+ ___block_descriptor_tmp.5148
+ ___block_descriptor_tmp.515
+ ___block_descriptor_tmp.5267
+ ___block_descriptor_tmp.5344
+ ___block_descriptor_tmp.5428
+ ___block_descriptor_tmp.5615
+ ___block_descriptor_tmp.59
+ ___block_descriptor_tmp.6.10802
+ ___block_descriptor_tmp.6.3581
+ ___block_descriptor_tmp.6.5379
+ ___block_descriptor_tmp.6185
+ ___block_descriptor_tmp.6336
+ ___block_descriptor_tmp.6426
+ ___block_descriptor_tmp.66
+ ___block_descriptor_tmp.6684
+ ___block_descriptor_tmp.7.10804
+ ___block_descriptor_tmp.7.11666
+ ___block_descriptor_tmp.7.3574
+ ___block_descriptor_tmp.7.7319
+ ___block_descriptor_tmp.7.8379
+ ___block_descriptor_tmp.7.9273
+ ___block_descriptor_tmp.7034
+ ___block_descriptor_tmp.7182
+ ___block_descriptor_tmp.7230
+ ___block_descriptor_tmp.7281
+ ___block_descriptor_tmp.7325
+ ___block_descriptor_tmp.74
+ ___block_descriptor_tmp.7409
+ ___block_descriptor_tmp.76
+ ___block_descriptor_tmp.7710
+ ___block_descriptor_tmp.8.10805
+ ___block_descriptor_tmp.8.13082
+ ___block_descriptor_tmp.8.3224
+ ___block_descriptor_tmp.8.3593
+ ___block_descriptor_tmp.8.6351
+ ___block_descriptor_tmp.8.7347
+ ___block_descriptor_tmp.8196
+ ___block_descriptor_tmp.83
+ ___block_descriptor_tmp.83.14731
+ ___block_descriptor_tmp.86
+ ___block_descriptor_tmp.867
+ ___block_descriptor_tmp.87
+ ___block_descriptor_tmp.8830
+ ___block_descriptor_tmp.9.10806
+ ___block_descriptor_tmp.90.14730
+ ___block_descriptor_tmp.91.13096
+ ___block_descriptor_tmp.91.14729
+ ___block_descriptor_tmp.92
+ ___block_descriptor_tmp.92.14728
+ ___block_descriptor_tmp.9269
+ ___block_descriptor_tmp.93
+ ___block_descriptor_tmp.93.14727
+ ___block_descriptor_tmp.9717
+ ___block_descriptor_tmp.98
+ ___block_literal_global.10018
+ ___block_literal_global.10125
+ ___block_literal_global.10568
+ ___block_literal_global.10827
+ ___block_literal_global.110
+ ___block_literal_global.11377
+ ___block_literal_global.115
+ ___block_literal_global.12092
+ ___block_literal_global.12209
+ ___block_literal_global.12271
+ ___block_literal_global.12488
+ ___block_literal_global.12702
+ ___block_literal_global.12931
+ ___block_literal_global.12965
+ ___block_literal_global.13
+ ___block_literal_global.13111
+ ___block_literal_global.13563
+ ___block_literal_global.14258
+ ___block_literal_global.15
+ ___block_literal_global.185
+ ___block_literal_global.20
+ ___block_literal_global.205
+ ___block_literal_global.216
+ ___block_literal_global.2190
+ ___block_literal_global.225
+ ___block_literal_global.257
+ ___block_literal_global.2846
+ ___block_literal_global.289
+ ___block_literal_global.290
+ ___block_literal_global.2921
+ ___block_literal_global.3.12976
+ ___block_literal_global.3.6338
+ ___block_literal_global.323
+ ___block_literal_global.3444
+ ___block_literal_global.358
+ ___block_literal_global.3605
+ ___block_literal_global.3693
+ ___block_literal_global.3768
+ ___block_literal_global.3954
+ ___block_literal_global.4009
+ ___block_literal_global.471
+ ___block_literal_global.500
+ ___block_literal_global.505
+ ___block_literal_global.509
+ ___block_literal_global.513
+ ___block_literal_global.5137
+ ___block_literal_global.517
+ ___block_literal_global.5262
+ ___block_literal_global.5309
+ ___block_literal_global.5341
+ ___block_literal_global.5429
+ ___block_literal_global.5519
+ ___block_literal_global.5687
+ ___block_literal_global.5716
+ ___block_literal_global.5753
+ ___block_literal_global.6.9371
+ ___block_literal_global.6227
+ ___block_literal_global.6334
+ ___block_literal_global.636
+ ___block_literal_global.6441
+ ___block_literal_global.6679
+ ___block_literal_global.685
+ ___block_literal_global.70
+ ___block_literal_global.7176
+ ___block_literal_global.7228
+ ___block_literal_global.7317
+ ___block_literal_global.7604
+ ___block_literal_global.774
+ ___block_literal_global.7797
+ ___block_literal_global.803
+ ___block_literal_global.8192
+ ___block_literal_global.8329
+ ___block_literal_global.8985
+ ___block_literal_global.909
+ ___block_literal_global.93
+ ___block_literal_global.9361
+ ___block_literal_global.9646
+ ___block_literal_global.9916
+ ___copy_helper_atomic_property_
+ ___copy_helper_block_e8_32c60_ZTSNSt3__110shared_ptrIN12CADeprecated16XMachReceivePortEEE
+ ___copy_helper_block_e8_40c37_ZTSN10applesauce8dispatch2v16sourceE
+ ___copy_helper_block_ea8_32c132_ZTSKZZ44-[AVHapticServer forceStopIdleDaemonClients]ENK3$_5clEPK22AVHapticServerInstanceRKNSt3__110shared_ptrI11ClientEntryEEEUlvE_
+ ___copy_helper_block_ea8_32c135_ZTSKZZ47-[AVHapticServer forceUnprewarmEligibleClients]ENK3$_9clEPK22AVHapticServerInstanceRKNSt3__110shared_ptrI11ClientEntryEEEUlvE_
+ ___copy_helper_block_ea8_32c143_ZTSKZZ55-[AVHapticServer forceStopIdleBackgroundRunningClients]ENK3$_7clEPK22AVHapticServerInstanceRKNSt3__110shared_ptrI11ClientEntryEEEUlvE_
+ ___copy_helper_block_ea8_32c36_ZTSNSt3__18weak_ptrI11ClientEntryEE
+ ___copy_helper_block_ea8_32c68_ZTSKZZN19HapticServerManager26SetupVADRoutingObservationEjEUb_E3$_1
+ ___copy_helper_block_ea8_40c36_ZTSNSt3__18weak_ptrI11SynthOutputEE
+ ___copy_helper_block_ea8_40c39_ZTSNSt3__110shared_ptrI11SynthOutputEE
+ ___destroy_helper_block_e8_32c60_ZTSNSt3__110shared_ptrIN12CADeprecated16XMachReceivePortEEE
+ ___destroy_helper_block_e8_40c37_ZTSN10applesauce8dispatch2v16sourceE
+ ___destroy_helper_block_ea8_32
+ ___destroy_helper_block_ea8_32.5778
+ ___destroy_helper_block_ea8_32c135_ZTSKZZ47-[AVHapticServer forceUnprewarmEligibleClients]ENK3$_9clEPK22AVHapticServerInstanceRKNSt3__110shared_ptrI11ClientEntryEEEUlvE_
+ ___destroy_helper_block_ea8_32c36_ZTSNSt3__18weak_ptrI11ClientEntryEE
+ ___destroy_helper_block_ea8_40c36_ZTSNSt3__18weak_ptrI11SynthOutputEE
+ ___destroy_helper_block_ea8_40c39_ZTSNSt3__110shared_ptrI11SynthOutputEE
+ ___umodti3
+ __dispatch_source_type_mach_recv
+ __xpc_type_error
+ _access
+ _bootstrap_check_in
+ _dispatch_barrier_sync
+ _dispatch_mig_server
+ _dispatch_source_cancel
+ _dispatch_source_set_cancel_handler
+ _exp
+ _feof
+ _ferror
+ _fileno
+ _fseeko
+ _ftruncate
+ _gCAVectorUnitType
+ _gHCHNDeferredLog
+ _gHMUTDeferredLog
+ _gHSEQDeferredLog
+ _gHSHMDeferredLog
+ _gHSQPDeferredLog
+ _gHSRVDeferredLog
+ _gHSYNDeferredLog
+ _gRSRVDeferredLog
+ _gRSYNDeferredLog
+ _getenv
+ _kHapticEngineNotificationDeviceStoppedFromBelow
+ _kHapticEngineNotificationKeyClientID
+ _kHapticEngineNotificationKeyDeviceIsHaptic
+ _mach_port_insert_right
+ _mach_port_mod_refs
+ _mach_port_request_notification
+ _malloc_type_free
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyCppObjectAtomic
+ _objc_msgSend$buildActiveProcessesForPowerLogForAudio:haptics:
+ _objc_msgSend$buildClientsStringFromEntries:returningLastEntry:
+ _objc_msgSend$clientTypeForEntry:withClientID:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$displayPrewarmedProcessEntriesWithPrewarmTime:
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$forceStopIdleBackgroundRunningClients
+ _objc_msgSend$forceStopIdleDaemonClients
+ _objc_msgSend$forceUnprewarmEligibleClients
+ _objc_msgSend$getClientMinMaxPowerPolicy:error:
+ _objc_msgSend$getPrewarmedClientEntries
+ _objc_msgSend$getRunningClientEntries
+ _objc_msgSend$handleSynthOutputNotificationDeviceStoppedFromBelow:
+ _objc_msgSend$hapticSession
+ _objc_msgSend$initWithServer:id:connection:outError:
+ _objc_msgSend$initWithTranslationIdentifier:delegate:delegateQueue:
+ _objc_msgSend$isDaemon
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$performAction:forClientsMatchingPredicate:
+ _objc_msgSend$performVolumeOperation:volume:category:mode:routeName:routeDeviceIdentifier:routeSubtype:rampUpDuration:rampDownDuration:outVolume:outSequenceNumber:outMuted:outCategoryCopy:outModeCopy:retainFullMute:
+ _objc_msgSend$reportRunningCountToPowerLogForAudio:haptics:entry:
+ _objc_msgSend$server
+ _objc_msgSend$substringToIndex:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x9
+ _os_transaction_create
+ _pow
+ _pthread_attr_setdetachstate
+ _pthread_cond_broadcast
+ _pthread_cond_destroy
+ _pthread_cond_init
+ _pthread_cond_signal
+ _pthread_cond_timedwait_relative_np
+ _pthread_cond_wait
+ _pthread_mutex_destroy
+ _pthread_mutex_init
+ _pthread_mutex_trylock
+ _pthread_setname_np
+ _remove
+ _shm_open
+ _shm_unlink
+ _stat
+ _task_get_special_port
+ _thread_info
+ _vm_map
+ _xpc_connection_set_context
+ _xpc_connection_set_event_handler
- +[SSCoreHapticsInfo instance]
- -[AVHapticServer shouldUnprewarmAllClientsAfterDisplayingPrewarmedProcessEntriesWithPrewarmTime:]
- -[AVHapticServer unprewarmAllClientEntries]
- -[AVHapticServerInstance initWithMaster:id:connection:outError:]
- -[AVHapticServerInstance master]
- -[SSCoreHapticsInfo .cxx_construct]
- -[SSCoreHapticsInfo .cxx_destruct]
- -[SSCoreHapticsInfo disposeSSID:]
- -[SSCoreHapticsInfo generateNewSSIDForPlayer:]
- -[SSCoreHapticsInfo getPlayerForSSID:]
- -[SSCoreHapticsInfo init]
- -[SSCoreHapticsInfo registerSSID:withPlayer:]
- -[SSCoreHapticsInfo unregisterSSID:]
- -[SSCoreHapticsPlayer .cxx_destruct]
- -[SSCoreHapticsPlayer createAudioPlayerAndReturnError:]
- -[SSCoreHapticsPlayer createAudioResource:error:]
- -[SSCoreHapticsPlayer createHapticPlayer:error:]
- -[SSCoreHapticsPlayer dealloc]
- -[SSCoreHapticsPlayer doInit:haptic:error:]
- -[SSCoreHapticsPlayer engine]
- -[SSCoreHapticsPlayer getHapticDictionaryFromURL:]
- -[SSCoreHapticsPlayer handleFinish]
- -[SSCoreHapticsPlayer initWithAudio:haptic:error:]
- -[SSCoreHapticsPlayer initWithAudio:hapticDictionary:error:]
- -[SSCoreHapticsPlayer init]
- -[SSCoreHapticsPlayer playWithOptions:completionCallbackToken:error:]
- -[SSCoreHapticsPlayer prepareHapticPatternFromPlayOptions:]
- -[SSCoreHapticsPlayer prewarm:]
- -[SSCoreHapticsPlayer registerCompletionAndStop]
- -[SSCoreHapticsPlayer registerCompletionPortion:]
- -[SSCoreHapticsPlayer setupDefaultEngineConfigBlock]
- -[SSCoreHapticsPlayer setupLooping]
- -[SSCoreHapticsPlayer ssid]
- -[SSCoreHapticsPlayer startPlayerAtTime:forAudio:error:]
- -[SSCoreHapticsPlayer stop:]
- -[TranslatorClientDelegate .cxx_construct]
- -[TranslatorClientDelegate .cxx_destruct]
- -[TranslatorClientDelegate audioGenerationDidFinishForClient:]
- -[TranslatorClientDelegate client:didGenerateTranslatedAudio:]
- -[TranslatorClientDelegate client:didPauseTranslationWithReason:]
- -[TranslatorClientDelegate client:didReceiveTranscriptionResult:]
- -[TranslatorClientDelegate client:didReceiveTranslationResult:]
- -[TranslatorClientDelegate client:didStopTranslationWithError:]
- -[TranslatorClientDelegate client:willStartTranslatedAudioWithMetadata:]
- -[TranslatorClientDelegate initWithWeakImpl:scope:]
- -[TranslatorClientDelegate serverDidDisconnectForClient:]
- -[TranslatorClientDelegate translationDidResumeForClient:]
- -[TranslatorClientDelegate translationDidStartForClient:]
- GCC_except_table0
- GCC_except_table1
- GCC_except_table100
- GCC_except_table1000
- GCC_except_table1001
- GCC_except_table1002
- GCC_except_table1003
- GCC_except_table1056
- GCC_except_table1057
- GCC_except_table1058
- GCC_except_table1065
- GCC_except_table107
- GCC_except_table1071
- GCC_except_table1072
- GCC_except_table1076
- GCC_except_table1078
- GCC_except_table108
- GCC_except_table1084
- GCC_except_table1085
- GCC_except_table1086
- GCC_except_table1089
- GCC_except_table1092
- GCC_except_table1095
- GCC_except_table1099
- GCC_except_table1104
- GCC_except_table1119
- GCC_except_table1125
- GCC_except_table1126
- GCC_except_table1133
- GCC_except_table115
- GCC_except_table1151
- GCC_except_table1155
- GCC_except_table1164
- GCC_except_table1168
- GCC_except_table1170
- GCC_except_table1174
- GCC_except_table1176
- GCC_except_table1178
- GCC_except_table1179
- GCC_except_table1181
- GCC_except_table1183
- GCC_except_table1184
- GCC_except_table1185
- GCC_except_table1186
- GCC_except_table119
- GCC_except_table1192
- GCC_except_table1195
- GCC_except_table1196
- GCC_except_table1197
- GCC_except_table1205
- GCC_except_table1214
- GCC_except_table1219
- GCC_except_table1229
- GCC_except_table123
- GCC_except_table1230
- GCC_except_table1237
- GCC_except_table1238
- GCC_except_table1239
- GCC_except_table1243
- GCC_except_table1245
- GCC_except_table1246
- GCC_except_table1247
- GCC_except_table1249
- GCC_except_table1251
- GCC_except_table1255
- GCC_except_table1260
- GCC_except_table1261
- GCC_except_table1262
- GCC_except_table1268
- GCC_except_table1270
- GCC_except_table1271
- GCC_except_table128
- GCC_except_table1308
- GCC_except_table1309
- GCC_except_table1310
- GCC_except_table1311
- GCC_except_table1315
- GCC_except_table1319
- GCC_except_table1320
- GCC_except_table1323
- GCC_except_table1326
- GCC_except_table1330
- GCC_except_table1331
- GCC_except_table1333
- GCC_except_table1334
- GCC_except_table1335
- GCC_except_table1336
- GCC_except_table1345
- GCC_except_table1346
- GCC_except_table1347
- GCC_except_table1350
- GCC_except_table1351
- GCC_except_table1354
- GCC_except_table1356
- GCC_except_table1357
- GCC_except_table1363
- GCC_except_table1369
- GCC_except_table1371
- GCC_except_table1372
- GCC_except_table1375
- GCC_except_table1380
- GCC_except_table1394
- GCC_except_table1395
- GCC_except_table1396
- GCC_except_table1397
- GCC_except_table140
- GCC_except_table1400
- GCC_except_table141
- GCC_except_table1424
- GCC_except_table1425
- GCC_except_table1434
- GCC_except_table1436
- GCC_except_table1439
- GCC_except_table144
- GCC_except_table1440
- GCC_except_table1446
- GCC_except_table1447
- GCC_except_table1448
- GCC_except_table1451
- GCC_except_table1468
- GCC_except_table1477
- GCC_except_table148
- GCC_except_table1486
- GCC_except_table1489
- GCC_except_table1504
- GCC_except_table1505
- GCC_except_table1507
- GCC_except_table1508
- GCC_except_table151
- GCC_except_table1510
- GCC_except_table1514
- GCC_except_table1515
- GCC_except_table1521
- GCC_except_table1530
- GCC_except_table1531
- GCC_except_table1536
- GCC_except_table1546
- GCC_except_table1554
- GCC_except_table1564
- GCC_except_table1572
- GCC_except_table1573
- GCC_except_table1574
- GCC_except_table1576
- GCC_except_table1580
- GCC_except_table1581
- GCC_except_table1582
- GCC_except_table1583
- GCC_except_table1586
- GCC_except_table1587
- GCC_except_table1588
- GCC_except_table1589
- GCC_except_table159
- GCC_except_table1596
- GCC_except_table160
- GCC_except_table1603
- GCC_except_table1604
- GCC_except_table1607
- GCC_except_table1608
- GCC_except_table161
- GCC_except_table1613
- GCC_except_table1615
- GCC_except_table1616
- GCC_except_table1618
- GCC_except_table1631
- GCC_except_table1632
- GCC_except_table1637
- GCC_except_table1639
- GCC_except_table1640
- GCC_except_table1642
- GCC_except_table1661
- GCC_except_table1664
- GCC_except_table1666
- GCC_except_table1668
- GCC_except_table168
- GCC_except_table1680
- GCC_except_table1689
- GCC_except_table1690
- GCC_except_table1695
- GCC_except_table1696
- GCC_except_table1697
- GCC_except_table1698
- GCC_except_table17
- GCC_except_table1716
- GCC_except_table1726
- GCC_except_table1727
- GCC_except_table1731
- GCC_except_table174
- GCC_except_table175
- GCC_except_table1751
- GCC_except_table1752
- GCC_except_table1756
- GCC_except_table1757
- GCC_except_table1758
- GCC_except_table1759
- GCC_except_table1761
- GCC_except_table1766
- GCC_except_table177
- GCC_except_table1770
- GCC_except_table18
- GCC_except_table1820
- GCC_except_table1821
- GCC_except_table1823
- GCC_except_table1831
- GCC_except_table1832
- GCC_except_table1835
- GCC_except_table1836
- GCC_except_table1839
- GCC_except_table1841
- GCC_except_table1844
- GCC_except_table1846
- GCC_except_table1847
- GCC_except_table1848
- GCC_except_table1849
- GCC_except_table1856
- GCC_except_table1864
- GCC_except_table1870
- GCC_except_table1872
- GCC_except_table1900
- GCC_except_table192
- GCC_except_table193
- GCC_except_table1931
- GCC_except_table1932
- GCC_except_table1934
- GCC_except_table1935
- GCC_except_table1940
- GCC_except_table1947
- GCC_except_table1949
- GCC_except_table1950
- GCC_except_table1951
- GCC_except_table1952
- GCC_except_table1953
- GCC_except_table1954
- GCC_except_table1956
- GCC_except_table1958
- GCC_except_table1959
- GCC_except_table1960
- GCC_except_table1961
- GCC_except_table1962
- GCC_except_table1963
- GCC_except_table1964
- GCC_except_table1965
- GCC_except_table1967
- GCC_except_table1968
- GCC_except_table1971
- GCC_except_table1979
- GCC_except_table1980
- GCC_except_table1981
- GCC_except_table1983
- GCC_except_table1984
- GCC_except_table1985
- GCC_except_table1988
- GCC_except_table1989
- GCC_except_table1994
- GCC_except_table1995
- GCC_except_table1997
- GCC_except_table1998
- GCC_except_table2
- GCC_except_table2001
- GCC_except_table2002
- GCC_except_table2003
- GCC_except_table2004
- GCC_except_table2006
- GCC_except_table2026
- GCC_except_table2029
- GCC_except_table2030
- GCC_except_table2031
- GCC_except_table2032
- GCC_except_table2033
- GCC_except_table2035
- GCC_except_table2037
- GCC_except_table2043
- GCC_except_table2056
- GCC_except_table2069
- GCC_except_table2082
- GCC_except_table209
- GCC_except_table2090
- GCC_except_table2091
- GCC_except_table2092
- GCC_except_table21
- GCC_except_table210
- GCC_except_table2101
- GCC_except_table211
- GCC_except_table212
- GCC_except_table213
- GCC_except_table2135
- GCC_except_table2146
- GCC_except_table2147
- GCC_except_table2148
- GCC_except_table215
- GCC_except_table2151
- GCC_except_table2153
- GCC_except_table216
- GCC_except_table2164
- GCC_except_table2165
- GCC_except_table217
- GCC_except_table2171
- GCC_except_table2173
- GCC_except_table2178
- GCC_except_table2188
- GCC_except_table2189
- GCC_except_table219
- GCC_except_table2190
- GCC_except_table2195
- GCC_except_table2197
- GCC_except_table2199
- GCC_except_table220
- GCC_except_table2209
- GCC_except_table2218
- GCC_except_table2219
- GCC_except_table2221
- GCC_except_table2236
- GCC_except_table2237
- GCC_except_table2245
- GCC_except_table2249
- GCC_except_table2251
- GCC_except_table2252
- GCC_except_table2253
- GCC_except_table2255
- GCC_except_table2256
- GCC_except_table2263
- GCC_except_table2272
- GCC_except_table2275
- GCC_except_table2276
- GCC_except_table2281
- GCC_except_table2286
- GCC_except_table2288
- GCC_except_table2291
- GCC_except_table2301
- GCC_except_table2302
- GCC_except_table2303
- GCC_except_table2304
- GCC_except_table2313
- GCC_except_table2314
- GCC_except_table2339
- GCC_except_table2347
- GCC_except_table2351
- GCC_except_table236
- GCC_except_table2362
- GCC_except_table2364
- GCC_except_table2369
- GCC_except_table2370
- GCC_except_table2373
- GCC_except_table2381
- GCC_except_table2412
- GCC_except_table2419
- GCC_except_table242
- GCC_except_table2421
- GCC_except_table2426
- GCC_except_table2427
- GCC_except_table2429
- GCC_except_table2434
- GCC_except_table2435
- GCC_except_table246
- GCC_except_table2480
- GCC_except_table2481
- GCC_except_table2482
- GCC_except_table2483
- GCC_except_table2484
- GCC_except_table2486
- GCC_except_table2488
- GCC_except_table2496
- GCC_except_table2497
- GCC_except_table2498
- GCC_except_table2499
- GCC_except_table2503
- GCC_except_table2508
- GCC_except_table2509
- GCC_except_table2517
- GCC_except_table2518
- GCC_except_table2519
- GCC_except_table2520
- GCC_except_table2525
- GCC_except_table2527
- GCC_except_table253
- GCC_except_table2537
- GCC_except_table2541
- GCC_except_table2543
- GCC_except_table2544
- GCC_except_table2545
- GCC_except_table2546
- GCC_except_table2554
- GCC_except_table2555
- GCC_except_table2556
- GCC_except_table2558
- GCC_except_table2559
- GCC_except_table2560
- GCC_except_table2561
- GCC_except_table2562
- GCC_except_table2564
- GCC_except_table2567
- GCC_except_table2568
- GCC_except_table2569
- GCC_except_table2571
- GCC_except_table2572
- GCC_except_table2573
- GCC_except_table2574
- GCC_except_table2576
- GCC_except_table2577
- GCC_except_table2578
- GCC_except_table2584
- GCC_except_table2591
- GCC_except_table2593
- GCC_except_table2597
- GCC_except_table2598
- GCC_except_table2621
- GCC_except_table2622
- GCC_except_table2623
- GCC_except_table2630
- GCC_except_table2634
- GCC_except_table2641
- GCC_except_table2643
- GCC_except_table2649
- GCC_except_table265
- GCC_except_table2650
- GCC_except_table2659
- GCC_except_table266
- GCC_except_table2662
- GCC_except_table2664
- GCC_except_table2665
- GCC_except_table2675
- GCC_except_table2685
- GCC_except_table2686
- GCC_except_table2687
- GCC_except_table2693
- GCC_except_table2694
- GCC_except_table2696
- GCC_except_table2697
- GCC_except_table2698
- GCC_except_table2703
- GCC_except_table2708
- GCC_except_table271
- GCC_except_table2711
- GCC_except_table2722
- GCC_except_table2724
- GCC_except_table2726
- GCC_except_table2729
- GCC_except_table2730
- GCC_except_table2731
- GCC_except_table2740
- GCC_except_table2746
- GCC_except_table2749
- GCC_except_table275
- GCC_except_table2756
- GCC_except_table2759
- GCC_except_table276
- GCC_except_table2762
- GCC_except_table2763
- GCC_except_table2773
- GCC_except_table2774
- GCC_except_table278
- GCC_except_table279
- GCC_except_table2791
- GCC_except_table2792
- GCC_except_table2802
- GCC_except_table2810
- GCC_except_table2826
- GCC_except_table2827
- GCC_except_table2829
- GCC_except_table283
- GCC_except_table2832
- GCC_except_table2835
- GCC_except_table2838
- GCC_except_table2840
- GCC_except_table285
- GCC_except_table2854
- GCC_except_table2855
- GCC_except_table287
- GCC_except_table2879
- GCC_except_table2880
- GCC_except_table2881
- GCC_except_table2882
- GCC_except_table2883
- GCC_except_table2884
- GCC_except_table2885
- GCC_except_table2886
- GCC_except_table2890
- GCC_except_table2891
- GCC_except_table2894
- GCC_except_table2897
- GCC_except_table2898
- GCC_except_table2901
- GCC_except_table2902
- GCC_except_table2903
- GCC_except_table2904
- GCC_except_table2908
- GCC_except_table2909
- GCC_except_table2910
- GCC_except_table2913
- GCC_except_table2915
- GCC_except_table2916
- GCC_except_table2918
- GCC_except_table2919
- GCC_except_table2921
- GCC_except_table2922
- GCC_except_table2927
- GCC_except_table2928
- GCC_except_table2933
- GCC_except_table2934
- GCC_except_table2937
- GCC_except_table2938
- GCC_except_table2947
- GCC_except_table2948
- GCC_except_table2949
- GCC_except_table2950
- GCC_except_table2952
- GCC_except_table2953
- GCC_except_table2954
- GCC_except_table2955
- GCC_except_table2956
- GCC_except_table2957
- GCC_except_table2958
- GCC_except_table2959
- GCC_except_table2960
- GCC_except_table2961
- GCC_except_table2962
- GCC_except_table2963
- GCC_except_table2964
- GCC_except_table2965
- GCC_except_table2975
- GCC_except_table2986
- GCC_except_table2987
- GCC_except_table2994
- GCC_except_table3015
- GCC_except_table3016
- GCC_except_table3017
- GCC_except_table3018
- GCC_except_table3021
- GCC_except_table3022
- GCC_except_table3029
- GCC_except_table3030
- GCC_except_table3031
- GCC_except_table3032
- GCC_except_table3033
- GCC_except_table3034
- GCC_except_table3039
- GCC_except_table3055
- GCC_except_table3056
- GCC_except_table3057
- GCC_except_table3058
- GCC_except_table3059
- GCC_except_table3060
- GCC_except_table3062
- GCC_except_table3064
- GCC_except_table3065
- GCC_except_table3067
- GCC_except_table3072
- GCC_except_table3080
- GCC_except_table3082
- GCC_except_table3083
- GCC_except_table3092
- GCC_except_table3094
- GCC_except_table3099
- GCC_except_table3100
- GCC_except_table3101
- GCC_except_table3106
- GCC_except_table3107
- GCC_except_table3114
- GCC_except_table3115
- GCC_except_table3118
- GCC_except_table3123
- GCC_except_table3124
- GCC_except_table3131
- GCC_except_table3132
- GCC_except_table3135
- GCC_except_table3136
- GCC_except_table3137
- GCC_except_table3145
- GCC_except_table3148
- GCC_except_table3149
- GCC_except_table3152
- GCC_except_table3153
- GCC_except_table3155
- GCC_except_table3156
- GCC_except_table3170
- GCC_except_table3171
- GCC_except_table3172
- GCC_except_table3173
- GCC_except_table3175
- GCC_except_table3176
- GCC_except_table3177
- GCC_except_table3178
- GCC_except_table3179
- GCC_except_table3180
- GCC_except_table3181
- GCC_except_table3182
- GCC_except_table3183
- GCC_except_table3184
- GCC_except_table3185
- GCC_except_table3186
- GCC_except_table3187
- GCC_except_table3188
- GCC_except_table3189
- GCC_except_table3190
- GCC_except_table3191
- GCC_except_table3192
- GCC_except_table3193
- GCC_except_table3194
- GCC_except_table3195
- GCC_except_table3197
- GCC_except_table3199
- GCC_except_table321
- GCC_except_table3210
- GCC_except_table325
- GCC_except_table3267
- GCC_except_table327
- GCC_except_table3334
- GCC_except_table3342
- GCC_except_table3345
- GCC_except_table3349
- GCC_except_table3351
- GCC_except_table3353
- GCC_except_table3355
- GCC_except_table3356
- GCC_except_table3357
- GCC_except_table3358
- GCC_except_table3361
- GCC_except_table3362
- GCC_except_table3363
- GCC_except_table3366
- GCC_except_table3371
- GCC_except_table3403
- GCC_except_table3407
- GCC_except_table3410
- GCC_except_table3411
- GCC_except_table3412
- GCC_except_table3415
- GCC_except_table3419
- GCC_except_table3420
- GCC_except_table3421
- GCC_except_table3422
- GCC_except_table3423
- GCC_except_table3427
- GCC_except_table3431
- GCC_except_table3432
- GCC_except_table3433
- GCC_except_table3434
- GCC_except_table3435
- GCC_except_table3436
- GCC_except_table3437
- GCC_except_table3438
- GCC_except_table3439
- GCC_except_table3441
- GCC_except_table3446
- GCC_except_table3456
- GCC_except_table3461
- GCC_except_table3462
- GCC_except_table3464
- GCC_except_table3466
- GCC_except_table3469
- GCC_except_table3472
- GCC_except_table3494
- GCC_except_table3495
- GCC_except_table3499
- GCC_except_table3500
- GCC_except_table3502
- GCC_except_table3512
- GCC_except_table3514
- GCC_except_table3515
- GCC_except_table3517
- GCC_except_table3520
- GCC_except_table3521
- GCC_except_table3522
- GCC_except_table3524
- GCC_except_table3525
- GCC_except_table3526
- GCC_except_table3527
- GCC_except_table3529
- GCC_except_table353
- GCC_except_table3531
- GCC_except_table3533
- GCC_except_table3541
- GCC_except_table3552
- GCC_except_table3553
- GCC_except_table3556
- GCC_except_table3557
- GCC_except_table3570
- GCC_except_table3577
- GCC_except_table3582
- GCC_except_table3584
- GCC_except_table3585
- GCC_except_table3586
- GCC_except_table3592
- GCC_except_table3604
- GCC_except_table3605
- GCC_except_table3606
- GCC_except_table3607
- GCC_except_table3608
- GCC_except_table361
- GCC_except_table3611
- GCC_except_table3613
- GCC_except_table3614
- GCC_except_table3616
- GCC_except_table3622
- GCC_except_table3635
- GCC_except_table3636
- GCC_except_table3637
- GCC_except_table3639
- GCC_except_table3642
- GCC_except_table3644
- GCC_except_table3659
- GCC_except_table3661
- GCC_except_table3662
- GCC_except_table3667
- GCC_except_table3670
- GCC_except_table3671
- GCC_except_table3672
- GCC_except_table3677
- GCC_except_table3678
- GCC_except_table3681
- GCC_except_table3690
- GCC_except_table3692
- GCC_except_table3693
- GCC_except_table3696
- GCC_except_table3698
- GCC_except_table3699
- GCC_except_table370
- GCC_except_table3700
- GCC_except_table3702
- GCC_except_table3708
- GCC_except_table3719
- GCC_except_table3726
- GCC_except_table3727
- GCC_except_table373
- GCC_except_table3730
- GCC_except_table3734
- GCC_except_table374
- GCC_except_table3748
- GCC_except_table3750
- GCC_except_table3752
- GCC_except_table3753
- GCC_except_table3757
- GCC_except_table376
- GCC_except_table3763
- GCC_except_table3775
- GCC_except_table3781
- GCC_except_table3782
- GCC_except_table3783
- GCC_except_table382
- GCC_except_table3827
- GCC_except_table3834
- GCC_except_table3840
- GCC_except_table3841
- GCC_except_table3843
- GCC_except_table3844
- GCC_except_table3847
- GCC_except_table3849
- GCC_except_table386
- GCC_except_table3879
- GCC_except_table3881
- GCC_except_table3885
- GCC_except_table3887
- GCC_except_table3961
- GCC_except_table3973
- GCC_except_table3976
- GCC_except_table3978
- GCC_except_table3982
- GCC_except_table3983
- GCC_except_table3985
- GCC_except_table40
- GCC_except_table400
- GCC_except_table4011
- GCC_except_table4014
- GCC_except_table4019
- GCC_except_table4026
- GCC_except_table4053
- GCC_except_table4055
- GCC_except_table4060
- GCC_except_table4061
- GCC_except_table4062
- GCC_except_table4063
- GCC_except_table4064
- GCC_except_table4065
- GCC_except_table4067
- GCC_except_table4068
- GCC_except_table4072
- GCC_except_table4073
- GCC_except_table4075
- GCC_except_table4076
- GCC_except_table4077
- GCC_except_table4079
- GCC_except_table4082
- GCC_except_table4088
- GCC_except_table4089
- GCC_except_table4090
- GCC_except_table4092
- GCC_except_table4093
- GCC_except_table4094
- GCC_except_table4095
- GCC_except_table4097
- GCC_except_table4100
- GCC_except_table4102
- GCC_except_table4109
- GCC_except_table4110
- GCC_except_table4111
- GCC_except_table4115
- GCC_except_table4117
- GCC_except_table4119
- GCC_except_table4122
- GCC_except_table4124
- GCC_except_table4126
- GCC_except_table4127
- GCC_except_table4128
- GCC_except_table4129
- GCC_except_table413
- GCC_except_table4131
- GCC_except_table4134
- GCC_except_table4136
- GCC_except_table4137
- GCC_except_table4139
- GCC_except_table414
- GCC_except_table4144
- GCC_except_table4146
- GCC_except_table4148
- GCC_except_table4149
- GCC_except_table4150
- GCC_except_table4156
- GCC_except_table4157
- GCC_except_table4158
- GCC_except_table4163
- GCC_except_table4164
- GCC_except_table4169
- GCC_except_table4181
- GCC_except_table4188
- GCC_except_table4190
- GCC_except_table4192
- GCC_except_table4197
- GCC_except_table4199
- GCC_except_table4205
- GCC_except_table421
- GCC_except_table425
- GCC_except_table4256
- GCC_except_table4261
- GCC_except_table4273
- GCC_except_table4274
- GCC_except_table4275
- GCC_except_table4284
- GCC_except_table4285
- GCC_except_table4287
- GCC_except_table4291
- GCC_except_table4295
- GCC_except_table4330
- GCC_except_table4331
- GCC_except_table4344
- GCC_except_table4345
- GCC_except_table435
- GCC_except_table4360
- GCC_except_table4362
- GCC_except_table4363
- GCC_except_table4376
- GCC_except_table4377
- GCC_except_table4378
- GCC_except_table4380
- GCC_except_table4393
- GCC_except_table4394
- GCC_except_table4395
- GCC_except_table4396
- GCC_except_table4397
- GCC_except_table4399
- GCC_except_table44
- GCC_except_table4401
- GCC_except_table4402
- GCC_except_table4403
- GCC_except_table4404
- GCC_except_table4405
- GCC_except_table4406
- GCC_except_table4407
- GCC_except_table4408
- GCC_except_table4417
- GCC_except_table4418
- GCC_except_table4435
- GCC_except_table4438
- GCC_except_table4459
- GCC_except_table4465
- GCC_except_table4466
- GCC_except_table4486
- GCC_except_table4489
- GCC_except_table449
- GCC_except_table4491
- GCC_except_table4494
- GCC_except_table4497
- GCC_except_table4504
- GCC_except_table4516
- GCC_except_table4517
- GCC_except_table4519
- GCC_except_table4520
- GCC_except_table4524
- GCC_except_table4525
- GCC_except_table4527
- GCC_except_table4528
- GCC_except_table453
- GCC_except_table4530
- GCC_except_table4537
- GCC_except_table4549
- GCC_except_table4553
- GCC_except_table4555
- GCC_except_table4575
- GCC_except_table4577
- GCC_except_table4578
- GCC_except_table4579
- GCC_except_table4586
- GCC_except_table4587
- GCC_except_table4589
- GCC_except_table459
- GCC_except_table46
- GCC_except_table460
- GCC_except_table4619
- GCC_except_table462
- GCC_except_table4621
- GCC_except_table4630
- GCC_except_table464
- GCC_except_table4647
- GCC_except_table4650
- GCC_except_table4651
- GCC_except_table4652
- GCC_except_table4653
- GCC_except_table47
- GCC_except_table4717
- GCC_except_table4718
- GCC_except_table4734
- GCC_except_table4739
- GCC_except_table4743
- GCC_except_table4746
- GCC_except_table4747
- GCC_except_table4755
- GCC_except_table4757
- GCC_except_table4758
- GCC_except_table4763
- GCC_except_table478
- GCC_except_table479
- GCC_except_table480
- GCC_except_table483
- GCC_except_table485
- GCC_except_table487
- GCC_except_table488
- GCC_except_table4880
- GCC_except_table4881
- GCC_except_table4882
- GCC_except_table4883
- GCC_except_table4884
- GCC_except_table4885
- GCC_except_table4886
- GCC_except_table4887
- GCC_except_table4888
- GCC_except_table4889
- GCC_except_table489
- GCC_except_table4891
- GCC_except_table4892
- GCC_except_table4893
- GCC_except_table4894
- GCC_except_table4896
- GCC_except_table4897
- GCC_except_table49
- GCC_except_table490
- GCC_except_table4904
- GCC_except_table4905
- GCC_except_table4906
- GCC_except_table4908
- GCC_except_table491
- GCC_except_table4910
- GCC_except_table4912
- GCC_except_table4916
- GCC_except_table4917
- GCC_except_table4918
- GCC_except_table4924
- GCC_except_table4933
- GCC_except_table4936
- GCC_except_table4939
- GCC_except_table4947
- GCC_except_table4948
- GCC_except_table495
- GCC_except_table4954
- GCC_except_table4967
- GCC_except_table4968
- GCC_except_table4969
- GCC_except_table4970
- GCC_except_table4971
- GCC_except_table4974
- GCC_except_table4975
- GCC_except_table4979
- GCC_except_table498
- GCC_except_table4980
- GCC_except_table4981
- GCC_except_table4986
- GCC_except_table4987
- GCC_except_table4989
- GCC_except_table4991
- GCC_except_table4993
- GCC_except_table4999
- GCC_except_table5001
- GCC_except_table5002
- GCC_except_table5003
- GCC_except_table5007
- GCC_except_table5008
- GCC_except_table5009
- GCC_except_table5010
- GCC_except_table5011
- GCC_except_table5013
- GCC_except_table5014
- GCC_except_table5019
- GCC_except_table5023
- GCC_except_table5024
- GCC_except_table5029
- GCC_except_table5030
- GCC_except_table5034
- GCC_except_table5057
- GCC_except_table5059
- GCC_except_table506
- GCC_except_table5061
- GCC_except_table5066
- GCC_except_table5068
- GCC_except_table5073
- GCC_except_table5074
- GCC_except_table5084
- GCC_except_table5085
- GCC_except_table5087
- GCC_except_table5093
- GCC_except_table5097
- GCC_except_table5100
- GCC_except_table5104
- GCC_except_table5123
- GCC_except_table5126
- GCC_except_table5133
- GCC_except_table5146
- GCC_except_table5151
- GCC_except_table5156
- GCC_except_table5157
- GCC_except_table5158
- GCC_except_table5159
- GCC_except_table516
- GCC_except_table5175
- GCC_except_table5178
- GCC_except_table5179
- GCC_except_table5180
- GCC_except_table519
- GCC_except_table5190
- GCC_except_table5191
- GCC_except_table5197
- GCC_except_table5199
- GCC_except_table52
- GCC_except_table520
- GCC_except_table5204
- GCC_except_table5205
- GCC_except_table5206
- GCC_except_table5224
- GCC_except_table523
- GCC_except_table524
- GCC_except_table53
- GCC_except_table537
- GCC_except_table538
- GCC_except_table539
- GCC_except_table54
- GCC_except_table550
- GCC_except_table551
- GCC_except_table552
- GCC_except_table553
- GCC_except_table554
- GCC_except_table557
- GCC_except_table558
- GCC_except_table565
- GCC_except_table567
- GCC_except_table57
- GCC_except_table572
- GCC_except_table573
- GCC_except_table574
- GCC_except_table575
- GCC_except_table581
- GCC_except_table585
- GCC_except_table60
- GCC_except_table603
- GCC_except_table609
- GCC_except_table610
- GCC_except_table611
- GCC_except_table613
- GCC_except_table6131
- GCC_except_table6132
- GCC_except_table6133
- GCC_except_table6156
- GCC_except_table6157
- GCC_except_table616
- GCC_except_table6162
- GCC_except_table6163
- GCC_except_table6164
- GCC_except_table6168
- GCC_except_table6170
- GCC_except_table6172
- GCC_except_table6174
- GCC_except_table6176
- GCC_except_table6178
- GCC_except_table618
- GCC_except_table6180
- GCC_except_table6182
- GCC_except_table6184
- GCC_except_table6186
- GCC_except_table6187
- GCC_except_table6188
- GCC_except_table619
- GCC_except_table6190
- GCC_except_table6196
- GCC_except_table6208
- GCC_except_table6212
- GCC_except_table6272
- GCC_except_table6282
- GCC_except_table6286
- GCC_except_table6291
- GCC_except_table6292
- GCC_except_table6293
- GCC_except_table6297
- GCC_except_table6300
- GCC_except_table6302
- GCC_except_table6304
- GCC_except_table6305
- GCC_except_table6307
- GCC_except_table6309
- GCC_except_table6316
- GCC_except_table6317
- GCC_except_table6318
- GCC_except_table6319
- GCC_except_table6320
- GCC_except_table6321
- GCC_except_table6327
- GCC_except_table6331
- GCC_except_table6332
- GCC_except_table6340
- GCC_except_table6341
- GCC_except_table6343
- GCC_except_table6348
- GCC_except_table6353
- GCC_except_table6357
- GCC_except_table6361
- GCC_except_table6363
- GCC_except_table6373
- GCC_except_table6376
- GCC_except_table6377
- GCC_except_table6381
- GCC_except_table6385
- GCC_except_table6387
- GCC_except_table639
- GCC_except_table6391
- GCC_except_table6395
- GCC_except_table640
- GCC_except_table6400
- GCC_except_table6401
- GCC_except_table6403
- GCC_except_table6408
- GCC_except_table6409
- GCC_except_table641
- GCC_except_table6412
- GCC_except_table6413
- GCC_except_table6415
- GCC_except_table6418
- GCC_except_table642
- GCC_except_table6426
- GCC_except_table6442
- GCC_except_table645
- GCC_except_table6451
- GCC_except_table6453
- GCC_except_table6455
- GCC_except_table6460
- GCC_except_table6461
- GCC_except_table6463
- GCC_except_table6469
- GCC_except_table6475
- GCC_except_table648
- GCC_except_table6482
- GCC_except_table6488
- GCC_except_table649
- GCC_except_table6490
- GCC_except_table6492
- GCC_except_table650
- GCC_except_table651
- GCC_except_table6515
- GCC_except_table6516
- GCC_except_table6517
- GCC_except_table6518
- GCC_except_table6522
- GCC_except_table6529
- GCC_except_table653
- GCC_except_table6536
- GCC_except_table6537
- GCC_except_table6538
- GCC_except_table654
- GCC_except_table6540
- GCC_except_table6541
- GCC_except_table6545
- GCC_except_table655
- GCC_except_table6551
- GCC_except_table6553
- GCC_except_table6557
- GCC_except_table6559
- GCC_except_table6560
- GCC_except_table6562
- GCC_except_table6563
- GCC_except_table6566
- GCC_except_table6569
- GCC_except_table6572
- GCC_except_table6573
- GCC_except_table6578
- GCC_except_table6582
- GCC_except_table6583
- GCC_except_table6584
- GCC_except_table6587
- GCC_except_table6588
- GCC_except_table6590
- GCC_except_table6596
- GCC_except_table6598
- GCC_except_table6600
- GCC_except_table6601
- GCC_except_table6619
- GCC_except_table6621
- GCC_except_table6626
- GCC_except_table6628
- GCC_except_table6629
- GCC_except_table6630
- GCC_except_table6633
- GCC_except_table6634
- GCC_except_table6635
- GCC_except_table6638
- GCC_except_table6651
- GCC_except_table6658
- GCC_except_table6659
- GCC_except_table6660
- GCC_except_table6661
- GCC_except_table6682
- GCC_except_table6683
- GCC_except_table6685
- GCC_except_table6689
- GCC_except_table6691
- GCC_except_table6693
- GCC_except_table6699
- GCC_except_table67
- GCC_except_table671
- GCC_except_table6724
- GCC_except_table6730
- GCC_except_table6734
- GCC_except_table6735
- GCC_except_table6739
- GCC_except_table6740
- GCC_except_table675
- GCC_except_table6751
- GCC_except_table6754
- GCC_except_table676
- GCC_except_table677
- GCC_except_table6778
- GCC_except_table678
- GCC_except_table679
- GCC_except_table6793
- GCC_except_table680
- GCC_except_table6804
- GCC_except_table681
- GCC_except_table682
- GCC_except_table684
- GCC_except_table685
- GCC_except_table6853
- GCC_except_table6856
- GCC_except_table6857
- GCC_except_table6858
- GCC_except_table686
- GCC_except_table6861
- GCC_except_table6863
- GCC_except_table6867
- GCC_except_table6869
- GCC_except_table687
- GCC_except_table6871
- GCC_except_table6872
- GCC_except_table6874
- GCC_except_table688
- GCC_except_table6883
- GCC_except_table6885
- GCC_except_table6887
- GCC_except_table6888
- GCC_except_table689
- GCC_except_table6890
- GCC_except_table6891
- GCC_except_table690
- GCC_except_table6902
- GCC_except_table6903
- GCC_except_table6910
- GCC_except_table6912
- GCC_except_table6913
- GCC_except_table6914
- GCC_except_table6916
- GCC_except_table6918
- GCC_except_table6919
- GCC_except_table6920
- GCC_except_table6922
- GCC_except_table6923
- GCC_except_table6924
- GCC_except_table6939
- GCC_except_table6941
- GCC_except_table6942
- GCC_except_table6943
- GCC_except_table6944
- GCC_except_table6945
- GCC_except_table6946
- GCC_except_table6947
- GCC_except_table6948
- GCC_except_table6949
- GCC_except_table6952
- GCC_except_table6957
- GCC_except_table6959
- GCC_except_table6964
- GCC_except_table6976
- GCC_except_table6979
- GCC_except_table6980
- GCC_except_table6981
- GCC_except_table6983
- GCC_except_table6986
- GCC_except_table6987
- GCC_except_table6988
- GCC_except_table6989
- GCC_except_table6990
- GCC_except_table7006
- GCC_except_table7007
- GCC_except_table7008
- GCC_except_table7009
- GCC_except_table7015
- GCC_except_table7032
- GCC_except_table7033
- GCC_except_table7037
- GCC_except_table7038
- GCC_except_table7054
- GCC_except_table7059
- GCC_except_table7061
- GCC_except_table7062
- GCC_except_table710
- GCC_except_table7103
- GCC_except_table7104
- GCC_except_table7106
- GCC_except_table7109
- GCC_except_table711
- GCC_except_table7111
- GCC_except_table7112
- GCC_except_table7113
- GCC_except_table7116
- GCC_except_table7118
- GCC_except_table712
- GCC_except_table713
- GCC_except_table7133
- GCC_except_table714
- GCC_except_table7142
- GCC_except_table7143
- GCC_except_table7146
- GCC_except_table7147
- GCC_except_table7149
- GCC_except_table7150
- GCC_except_table7158
- GCC_except_table7159
- GCC_except_table716
- GCC_except_table7160
- GCC_except_table7161
- GCC_except_table7163
- GCC_except_table7165
- GCC_except_table7171
- GCC_except_table7173
- GCC_except_table7179
- GCC_except_table7181
- GCC_except_table7183
- GCC_except_table7186
- GCC_except_table719
- GCC_except_table7192
- GCC_except_table720
- GCC_except_table7205
- GCC_except_table7206
- GCC_except_table7207
- GCC_except_table7208
- GCC_except_table7216
- GCC_except_table7217
- GCC_except_table7218
- GCC_except_table723
- GCC_except_table7253
- GCC_except_table7267
- GCC_except_table7281
- GCC_except_table7282
- GCC_except_table7295
- GCC_except_table7309
- GCC_except_table7312
- GCC_except_table7314
- GCC_except_table7315
- GCC_except_table7316
- GCC_except_table7317
- GCC_except_table7331
- GCC_except_table7333
- GCC_except_table7351
- GCC_except_table7352
- GCC_except_table7369
- GCC_except_table7373
- GCC_except_table7377
- GCC_except_table7382
- GCC_except_table7383
- GCC_except_table7384
- GCC_except_table7385
- GCC_except_table7390
- GCC_except_table7391
- GCC_except_table7392
- GCC_except_table7393
- GCC_except_table7394
- GCC_except_table7396
- GCC_except_table7397
- GCC_except_table74
- GCC_except_table7400
- GCC_except_table7402
- GCC_except_table7407
- GCC_except_table7408
- GCC_except_table7409
- GCC_except_table7410
- GCC_except_table7411
- GCC_except_table7412
- GCC_except_table7422
- GCC_except_table7424
- GCC_except_table7428
- GCC_except_table7430
- GCC_except_table7431
- GCC_except_table7434
- GCC_except_table7435
- GCC_except_table7436
- GCC_except_table7437
- GCC_except_table7441
- GCC_except_table7445
- GCC_except_table7446
- GCC_except_table7447
- GCC_except_table7448
- GCC_except_table7449
- GCC_except_table7450
- GCC_except_table7454
- GCC_except_table7458
- GCC_except_table746
- GCC_except_table7461
- GCC_except_table7464
- GCC_except_table7466
- GCC_except_table7467
- GCC_except_table7469
- GCC_except_table747
- GCC_except_table7470
- GCC_except_table7479
- GCC_except_table7480
- GCC_except_table7482
- GCC_except_table7484
- GCC_except_table7485
- GCC_except_table7486
- GCC_except_table7493
- GCC_except_table7496
- GCC_except_table7497
- GCC_except_table7501
- GCC_except_table7502
- GCC_except_table7503
- GCC_except_table7505
- GCC_except_table7506
- GCC_except_table7508
- GCC_except_table7509
- GCC_except_table751
- GCC_except_table7511
- GCC_except_table7517
- GCC_except_table7523
- GCC_except_table7527
- GCC_except_table754
- GCC_except_table7540
- GCC_except_table7545
- GCC_except_table7548
- GCC_except_table7551
- GCC_except_table7565
- GCC_except_table7587
- GCC_except_table7589
- GCC_except_table7596
- GCC_except_table7597
- GCC_except_table7598
- GCC_except_table7600
- GCC_except_table7611
- GCC_except_table7635
- GCC_except_table7637
- GCC_except_table764
- GCC_except_table7646
- GCC_except_table7664
- GCC_except_table7668
- GCC_except_table7673
- GCC_except_table7689
- GCC_except_table769
- GCC_except_table7690
- GCC_except_table7693
- GCC_except_table7721
- GCC_except_table7722
- GCC_except_table7723
- GCC_except_table7724
- GCC_except_table7725
- GCC_except_table7736
- GCC_except_table7737
- GCC_except_table7739
- GCC_except_table7743
- GCC_except_table7757
- GCC_except_table7759
- GCC_except_table7761
- GCC_except_table7762
- GCC_except_table7764
- GCC_except_table7768
- GCC_except_table7770
- GCC_except_table7772
- GCC_except_table7774
- GCC_except_table7776
- GCC_except_table7778
- GCC_except_table7780
- GCC_except_table7782
- GCC_except_table7784
- GCC_except_table7786
- GCC_except_table7787
- GCC_except_table7793
- GCC_except_table7795
- GCC_except_table7797
- GCC_except_table7801
- GCC_except_table7805
- GCC_except_table7806
- GCC_except_table7808
- GCC_except_table7809
- GCC_except_table7811
- GCC_except_table7813
- GCC_except_table7814
- GCC_except_table7816
- GCC_except_table7817
- GCC_except_table7819
- GCC_except_table782
- GCC_except_table7821
- GCC_except_table7823
- GCC_except_table7829
- GCC_except_table783
- GCC_except_table7830
- GCC_except_table7832
- GCC_except_table7834
- GCC_except_table7835
- GCC_except_table7837
- GCC_except_table7838
- GCC_except_table7840
- GCC_except_table7842
- GCC_except_table7844
- GCC_except_table7849
- GCC_except_table7852
- GCC_except_table7854
- GCC_except_table7858
- GCC_except_table786
- GCC_except_table7863
- GCC_except_table7864
- GCC_except_table7865
- GCC_except_table7866
- GCC_except_table7867
- GCC_except_table7877
- GCC_except_table7880
- GCC_except_table7881
- GCC_except_table7888
- GCC_except_table7889
- GCC_except_table789
- GCC_except_table7899
- GCC_except_table79
- GCC_except_table7915
- GCC_except_table7917
- GCC_except_table7919
- GCC_except_table792
- GCC_except_table7928
- GCC_except_table7930
- GCC_except_table7932
- GCC_except_table7938
- GCC_except_table7942
- GCC_except_table7944
- GCC_except_table7949
- GCC_except_table7950
- GCC_except_table7951
- GCC_except_table7953
- GCC_except_table7957
- GCC_except_table7964
- GCC_except_table7966
- GCC_except_table7967
- GCC_except_table7968
- GCC_except_table7970
- GCC_except_table7972
- GCC_except_table7980
- GCC_except_table7986
- GCC_except_table7988
- GCC_except_table7993
- GCC_except_table8005
- GCC_except_table8018
- GCC_except_table8020
- GCC_except_table8021
- GCC_except_table8022
- GCC_except_table8030
- GCC_except_table8031
- GCC_except_table8032
- GCC_except_table8053
- GCC_except_table8054
- GCC_except_table8055
- GCC_except_table8056
- GCC_except_table8057
- GCC_except_table8058
- GCC_except_table8059
- GCC_except_table8060
- GCC_except_table8066
- GCC_except_table8068
- GCC_except_table8072
- GCC_except_table8073
- GCC_except_table8074
- GCC_except_table8080
- GCC_except_table8081
- GCC_except_table8091
- GCC_except_table8105
- GCC_except_table8106
- GCC_except_table8112
- GCC_except_table8114
- GCC_except_table8115
- GCC_except_table8116
- GCC_except_table8121
- GCC_except_table8124
- GCC_except_table8130
- GCC_except_table8132
- GCC_except_table8134
- GCC_except_table8135
- GCC_except_table8142
- GCC_except_table8158
- GCC_except_table816
- GCC_except_table8172
- GCC_except_table8174
- GCC_except_table8175
- GCC_except_table8176
- GCC_except_table8177
- GCC_except_table8179
- GCC_except_table8180
- GCC_except_table8183
- GCC_except_table819
- GCC_except_table8206
- GCC_except_table8209
- GCC_except_table821
- GCC_except_table8215
- GCC_except_table8217
- GCC_except_table8218
- GCC_except_table822
- GCC_except_table8228
- GCC_except_table8230
- GCC_except_table8233
- GCC_except_table824
- GCC_except_table8248
- GCC_except_table825
- GCC_except_table8252
- GCC_except_table8253
- GCC_except_table8271
- GCC_except_table8272
- GCC_except_table8273
- GCC_except_table8276
- GCC_except_table8277
- GCC_except_table828
- GCC_except_table8297
- GCC_except_table8298
- GCC_except_table830
- GCC_except_table8333
- GCC_except_table8341
- GCC_except_table8343
- GCC_except_table8344
- GCC_except_table8348
- GCC_except_table8357
- GCC_except_table8375
- GCC_except_table8376
- GCC_except_table8377
- GCC_except_table8382
- GCC_except_table840
- GCC_except_table841
- GCC_except_table8410
- GCC_except_table8412
- GCC_except_table8413
- GCC_except_table8419
- GCC_except_table8422
- GCC_except_table8423
- GCC_except_table8425
- GCC_except_table8426
- GCC_except_table8427
- GCC_except_table8428
- GCC_except_table843
- GCC_except_table8431
- GCC_except_table8443
- GCC_except_table8444
- GCC_except_table8448
- GCC_except_table8449
- GCC_except_table8451
- GCC_except_table8452
- GCC_except_table8453
- GCC_except_table8456
- GCC_except_table8467
- GCC_except_table8470
- GCC_except_table8478
- GCC_except_table8479
- GCC_except_table8480
- GCC_except_table8484
- GCC_except_table8489
- GCC_except_table8495
- GCC_except_table8496
- GCC_except_table8510
- GCC_except_table8511
- GCC_except_table8512
- GCC_except_table8519
- GCC_except_table852
- GCC_except_table8521
- GCC_except_table8531
- GCC_except_table8535
- GCC_except_table8536
- GCC_except_table8539
- GCC_except_table8541
- GCC_except_table8544
- GCC_except_table8562
- GCC_except_table8573
- GCC_except_table8574
- GCC_except_table8575
- GCC_except_table8576
- GCC_except_table8577
- GCC_except_table8578
- GCC_except_table8579
- GCC_except_table858
- GCC_except_table8580
- GCC_except_table8581
- GCC_except_table8582
- GCC_except_table8583
- GCC_except_table8588
- GCC_except_table8596
- GCC_except_table86
- GCC_except_table8604
- GCC_except_table8612
- GCC_except_table8620
- GCC_except_table8628
- GCC_except_table8644
- GCC_except_table8652
- GCC_except_table8661
- GCC_except_table8669
- GCC_except_table8677
- GCC_except_table868
- GCC_except_table8680
- GCC_except_table8681
- GCC_except_table8684
- GCC_except_table8698
- GCC_except_table8699
- GCC_except_table870
- GCC_except_table8707
- GCC_except_table871
- GCC_except_table8710
- GCC_except_table8715
- GCC_except_table8719
- GCC_except_table872
- GCC_except_table8721
- GCC_except_table8723
- GCC_except_table8725
- GCC_except_table8726
- GCC_except_table8727
- GCC_except_table8730
- GCC_except_table8731
- GCC_except_table8733
- GCC_except_table8734
- GCC_except_table8735
- GCC_except_table8736
- GCC_except_table8737
- GCC_except_table8738
- GCC_except_table8739
- GCC_except_table8743
- GCC_except_table8745
- GCC_except_table8746
- GCC_except_table8747
- GCC_except_table8749
- GCC_except_table8750
- GCC_except_table8752
- GCC_except_table8756
- GCC_except_table8777
- GCC_except_table8778
- GCC_except_table878
- GCC_except_table8780
- GCC_except_table8781
- GCC_except_table8783
- GCC_except_table8788
- GCC_except_table8790
- GCC_except_table8797
- GCC_except_table880
- GCC_except_table8801
- GCC_except_table8811
- GCC_except_table8814
- GCC_except_table8815
- GCC_except_table8816
- GCC_except_table8821
- GCC_except_table8822
- GCC_except_table883
- GCC_except_table8831
- GCC_except_table8832
- GCC_except_table8859
- GCC_except_table8867
- GCC_except_table8883
- GCC_except_table8885
- GCC_except_table8886
- GCC_except_table8889
- GCC_except_table889
- GCC_except_table8890
- GCC_except_table8891
- GCC_except_table8905
- GCC_except_table8907
- GCC_except_table8930
- GCC_except_table8932
- GCC_except_table8936
- GCC_except_table8937
- GCC_except_table8938
- GCC_except_table8952
- GCC_except_table8964
- GCC_except_table8968
- GCC_except_table8970
- GCC_except_table8971
- GCC_except_table8979
- GCC_except_table8982
- GCC_except_table8987
- GCC_except_table8989
- GCC_except_table9020
- GCC_except_table9022
- GCC_except_table9023
- GCC_except_table9053
- GCC_except_table9055
- GCC_except_table9057
- GCC_except_table9065
- GCC_except_table9068
- GCC_except_table9071
- GCC_except_table9073
- GCC_except_table9074
- GCC_except_table9087
- GCC_except_table9088
- GCC_except_table9089
- GCC_except_table9093
- GCC_except_table9094
- GCC_except_table9095
- GCC_except_table9096
- GCC_except_table9097
- GCC_except_table9098
- GCC_except_table9099
- GCC_except_table9102
- GCC_except_table9104
- GCC_except_table9105
- GCC_except_table9106
- GCC_except_table9107
- GCC_except_table9108
- GCC_except_table9110
- GCC_except_table9112
- GCC_except_table9114
- GCC_except_table9115
- GCC_except_table9116
- GCC_except_table9117
- GCC_except_table9118
- GCC_except_table9119
- GCC_except_table912
- GCC_except_table9123
- GCC_except_table9124
- GCC_except_table9125
- GCC_except_table9126
- GCC_except_table9127
- GCC_except_table9128
- GCC_except_table9129
- GCC_except_table9130
- GCC_except_table9132
- GCC_except_table9133
- GCC_except_table9134
- GCC_except_table9135
- GCC_except_table9136
- GCC_except_table9137
- GCC_except_table9138
- GCC_except_table9142
- GCC_except_table9143
- GCC_except_table9144
- GCC_except_table9145
- GCC_except_table9146
- GCC_except_table9147
- GCC_except_table9148
- GCC_except_table9149
- GCC_except_table915
- GCC_except_table9150
- GCC_except_table9158
- GCC_except_table916
- GCC_except_table9160
- GCC_except_table9161
- GCC_except_table9165
- GCC_except_table9166
- GCC_except_table9167
- GCC_except_table9168
- GCC_except_table9169
- GCC_except_table9170
- GCC_except_table9171
- GCC_except_table9172
- GCC_except_table9173
- GCC_except_table9174
- GCC_except_table9175
- GCC_except_table9177
- GCC_except_table9178
- GCC_except_table918
- GCC_except_table9180
- GCC_except_table919
- GCC_except_table9192
- GCC_except_table9193
- GCC_except_table9194
- GCC_except_table9195
- GCC_except_table9196
- GCC_except_table9197
- GCC_except_table9198
- GCC_except_table9199
- GCC_except_table920
- GCC_except_table9200
- GCC_except_table9201
- GCC_except_table9202
- GCC_except_table9203
- GCC_except_table9204
- GCC_except_table9206
- GCC_except_table9209
- GCC_except_table921
- GCC_except_table9210
- GCC_except_table9214
- GCC_except_table9215
- GCC_except_table9217
- GCC_except_table9218
- GCC_except_table9219
- GCC_except_table9220
- GCC_except_table9221
- GCC_except_table9222
- GCC_except_table9229
- GCC_except_table9237
- GCC_except_table9239
- GCC_except_table9244
- GCC_except_table9251
- GCC_except_table9258
- GCC_except_table9265
- GCC_except_table9272
- GCC_except_table9273
- GCC_except_table9275
- GCC_except_table9277
- GCC_except_table9279
- GCC_except_table9280
- GCC_except_table9283
- GCC_except_table9296
- GCC_except_table9297
- GCC_except_table9311
- GCC_except_table9312
- GCC_except_table9326
- GCC_except_table933
- GCC_except_table9330
- GCC_except_table9333
- GCC_except_table9337
- GCC_except_table9339
- GCC_except_table934
- GCC_except_table9340
- GCC_except_table9356
- GCC_except_table9359
- GCC_except_table936
- GCC_except_table9378
- GCC_except_table938
- GCC_except_table9388
- GCC_except_table939
- GCC_except_table9392
- GCC_except_table9398
- GCC_except_table9405
- GCC_except_table9407
- GCC_except_table9425
- GCC_except_table9428
- GCC_except_table9430
- GCC_except_table9473
- GCC_except_table948
- GCC_except_table950
- GCC_except_table9516
- GCC_except_table9545
- GCC_except_table9547
- GCC_except_table9549
- GCC_except_table9551
- GCC_except_table9553
- GCC_except_table9571
- GCC_except_table9587
- GCC_except_table9591
- GCC_except_table9595
- GCC_except_table9597
- GCC_except_table9599
- GCC_except_table96
- GCC_except_table9601
- GCC_except_table9606
- GCC_except_table9608
- GCC_except_table9612
- GCC_except_table9619
- GCC_except_table9620
- GCC_except_table9622
- GCC_except_table9623
- GCC_except_table9624
- GCC_except_table9626
- GCC_except_table9630
- GCC_except_table9631
- GCC_except_table9632
- GCC_except_table9634
- GCC_except_table966
- GCC_except_table9668
- GCC_except_table9671
- GCC_except_table9674
- GCC_except_table9683
- GCC_except_table9686
- GCC_except_table9687
- GCC_except_table9688
- GCC_except_table9689
- GCC_except_table9692
- GCC_except_table9695
- GCC_except_table9700
- GCC_except_table9706
- GCC_except_table9707
- GCC_except_table9716
- GCC_except_table972
- GCC_except_table9720
- GCC_except_table9751
- GCC_except_table9752
- GCC_except_table9782
- GCC_except_table9783
- GCC_except_table9784
- GCC_except_table980
- GCC_except_table981
- GCC_except_table984
- GCC_except_table986
- GCC_except_table987
- GCC_except_table989
- GCC_except_table990
- GCC_except_table992
- GCC_except_table993
- GCC_except_table994
- GCC_except_table995
- GCC_except_table996
- GCC_except_table999
- _AudioFileReadPackets
- _CFDictionaryApplyFunction
- _CFGetRetainCount
- _CFStringAppend
- _CFStringCreateMutableCopy
- _CFStringCreateWithBytesNoCopy
- _CFStringCreateWithCStringNoCopy
- _CFStringHasPrefix
- _CHHapticAudioResourceKeyUseVolumeEnvelope
- _CHHapticEngineOptionKeyAudioPowerUsage
- _CHHapticEngineOptionKeyHapticPowerUsage
- _CHHapticEngineOptionKeyLocality
- _CHHapticEngineOptionKeyPriority
- _CHHapticLocalityDefault
- _CHHapticPatternKeyPattern
- _CHHapticPowerUsageHigh
- _CHHapticPriorityExclusive
- _CrashIfClientProvidedBogusAudioBufferList
- _OBJC_CLASS_$_CHHapticEvent
- _OBJC_CLASS_$_NSConstantDictionary
- _OBJC_CLASS_$_NSURL
- _OBJC_CLASS_$_SSCoreHapticsInfo
- _OBJC_CLASS_$_SSCoreHapticsPlayer
- _OBJC_CLASS_$_TranslatorClientDelegate
- _OBJC_IVAR_$_AVHapticServerInstance._master
- _OBJC_IVAR_$_AVHapticServerInstance._routeUsesReceiver
- _OBJC_IVAR_$_SSCoreHapticsInfo._SSIDMapQueue
- _OBJC_IVAR_$_SSCoreHapticsInfo._SSIDToPlayerMap
- _OBJC_IVAR_$_SSCoreHapticsPlayer._audioPatternDuration
- _OBJC_IVAR_$_SSCoreHapticsPlayer._audioPlaybackFinished
- _OBJC_IVAR_$_SSCoreHapticsPlayer._audioPlayer
- _OBJC_IVAR_$_SSCoreHapticsPlayer._audioResourceID
- _OBJC_IVAR_$_SSCoreHapticsPlayer._audioURL
- _OBJC_IVAR_$_SSCoreHapticsPlayer._clientCompletionToken
- _OBJC_IVAR_$_SSCoreHapticsPlayer._engine
- _OBJC_IVAR_$_SSCoreHapticsPlayer._hapticPatternDict
- _OBJC_IVAR_$_SSCoreHapticsPlayer._hapticPatternDuration
- _OBJC_IVAR_$_SSCoreHapticsPlayer._hapticPlaybackFinished
- _OBJC_IVAR_$_SSCoreHapticsPlayer._hapticPlayer
- _OBJC_IVAR_$_SSCoreHapticsPlayer._shouldPlayAudioFinal
- _OBJC_IVAR_$_SSCoreHapticsPlayer._shouldPlayHapticsFinal
- _OBJC_IVAR_$_SSCoreHapticsPlayer._ssid
- _OBJC_IVAR_$_TranslatorClientDelegate.mImpl
- _OBJC_IVAR_$_TranslatorClientDelegate.mScope
- _OBJC_METACLASS_$_SSCoreHapticsInfo
- _OBJC_METACLASS_$_SSCoreHapticsPlayer
- _OBJC_METACLASS_$_TranslatorClientDelegate
- _OSAtomicDequeue
- _OSAtomicEnqueue
- _Synchronously
- __OBJC_$_CLASS_METHODS_SSCoreHapticsInfo
- __OBJC_$_INSTANCE_METHODS_SSCoreHapticsInfo
- __OBJC_$_INSTANCE_METHODS_SSCoreHapticsPlayer
- __OBJC_$_INSTANCE_METHODS_TranslatorClientDelegate
- __OBJC_$_INSTANCE_VARIABLES_SSCoreHapticsInfo
- __OBJC_$_INSTANCE_VARIABLES_SSCoreHapticsPlayer
- __OBJC_$_INSTANCE_VARIABLES_TranslatorClientDelegate
- __OBJC_$_PROP_LIST_SSCoreHapticsPlayer
- __OBJC_$_PROP_LIST_TranslatorClientDelegate
- __OBJC_CLASS_PROTOCOLS_$_TranslatorClientDelegate
- __OBJC_CLASS_RO_$_SSCoreHapticsInfo
- __OBJC_CLASS_RO_$_SSCoreHapticsPlayer
- __OBJC_CLASS_RO_$_TranslatorClientDelegate
- __OBJC_METACLASS_RO_$_SSCoreHapticsInfo
- __OBJC_METACLASS_RO_$_SSCoreHapticsPlayer
- __OBJC_METACLASS_RO_$_TranslatorClientDelegate
- __Z18MIDIPacketList_NewymPKh
- __Z27AudioQueueInternalStop_Syncj
- __Z30AudioSessionSetActiveWithFlagsj13audit_token_thj
- __Z31CACFPreferencesGetAppFloatValuePK10__CFStringS1_Pb
- __Z33CACFPreferencesGetAppBooleanValuePK10__CFStringS1_Pb
- __Z33CACFPreferencesGetAppIntegerValuePK10__CFStringS1_Pb
- __Z35getMinimalRampDurationForValueDeltaff
- __Z7DumpHexP7__sFILEiPKh
- __ZGVZL13GetAcousticIDvE13optionalValue.5508
- __ZGVZN5caulk10concurrent8skiplistIPvNS_5alloc6detail13tracked_blockELi10ELNS0_16skiplist_optionsE0EE13random_engineEvE6engine
- __ZL11CPMSLibraryv.10598
- __ZL11CPMSLibraryv.3529
- __ZL15gAQCaptureInput
- __ZL16audit_stringCPMS.10613
- __ZL16audit_stringCPMS.3546
- __ZL16audit_stringCPMS.6513
- __ZL20CoreMediaLibraryCorePPc.7252
- __ZL20audit_stringAVFAudio.12854
- __ZL21audit_stringCoreMedia.5194
- __ZL21audit_stringCoreMedia.7261
- __ZL22gAQCaptureOutputDecode
- __ZL22gOutputCapturesEnabled
- __ZL23MediaToolboxLibraryCorePPc.7242
- __ZL23gAQCaptureOfflineRender
- __ZL23gAQCaptureOutputEnqueue
- __ZL24audit_stringMediaToolbox.7251
- __ZL29gAQCaptureInputRingBufferMode
- __ZL30audit_stringAudioSessionServer.8510
- __ZL32PV_GetAirPodsOffloadModeFromDictRKN10applesauce2CF13DictionaryRefE
- __ZL33getCMBaseObjectGetVTableSymbolLocv.7253
- __ZL58getFigCPECryptorCreateCryptorFromSerializedRecipeSymbolLocv.7243
- __ZN10AQMEIO_HAL11PrintObjectEP7__sFILE
- __ZN10CACFString10GetCStringEPK10__CFStringPcRjj
- __ZN10Marshaller18AddCreatedCFObjectEPKv
- __ZN10Marshaller9CheckDestERPvRjm
- __ZN10PowerMeter13Process_Int16EPKsii
- __ZN10PowerMeter13Process_Int32EPKiii
- __ZN10PowerMeter13SetSampleRateEd
- __ZN10PowerMeter14ProcessSilenceEi
- __ZN10PowerMeter5ResetEv
- __ZN10PowerMeter7ProcessEPKfii
- __ZN10TOpaqueRefIN5Phase13ServerManagerEE11PrintObjectEP7__sFILE
- __ZN10TOpaqueRefIN5Phase13ServerManagerEED0Ev
- __ZN10TOpaqueRefIN5Phase13ServerManagerEED1Ev
- __ZN10applesauce2CF11TypeRefPairC2IRA3_KcjEEOT_OT0_
- __ZN10applesauce4raii2v16detail10ScopeGuardIZZN14DSP_Routing_VP28SetCallTranslationPropertiesEPK14__CFDictionaryRbEUb_E4$_13NS2_15StackExitPolicyEED1Ev
- __ZN11CAExceptionD0Ev
- __ZN11CAExceptionD1Ev
- __ZN11CAExceptionD2Ev
- __ZN11CAFormatter20InitWithMemoryStreamER14CAMemoryStream
- __ZN11CAFormatter4InitERK14AudioTimeStampjb
- __ZN11CAFormatterC1EP20OpaqueAudioConverter
- __ZN11CAFormatterC1EPK14AudioTimeStampjb
- __ZN11CAFormatterC1EPK18AudioChannelLayout
- __ZN11CAFormatterC1EPKfii
- __ZN11CAFormatterC1ERK21AudioClassDescription
- __ZN11CAFormatterC1ERK24CAStreamBasicDescriptionb
- __ZN11CAFormatterC1ERK25AudioComponentDescription
- __ZN11CAFormatterC1ERK26AudioObjectPropertyAddress
- __ZN11CAFormatterC1ERK26AudioObjectPropertyAddressPKvi
- __ZN11CAFormatterC1ERK27AudioStreamBasicDescriptionb
- __ZN11ClientEntry19handleSequenceEndedEmN5caulk16inplace_functionIFvmELm32ELm8ENS0_23inplace_function_detail6vtableEEE
- __ZN11ClientEntry19setFlushRequestTimeEd
- __ZN11ClientEntry20releaseSynthChannelsERKNSt3__16vectorIjNS0_9allocatorIjEEEE
- __ZN11ClientEntry21prepareSequenceWithIDEmNSt3__18functionIFvmEEE
- __ZN11ClientEntry23addSequenceToActiveListERNSt3__110shared_ptrI14HapticSequenceEE
- __ZN11ClientEntry23getActiveSequenceWithIDEmb
- __ZN11ClientEntry27getSequencerChannelForIndexEmj
- __ZN11ClientEntry29handleReleaseCustomAudioEventEj
- __ZN11ClientEntry7doStartEv
- __ZN11ClientEntryC2Em13audit_token_tP13ServerManagerNS_5StateEj20HapticPlayerPriority
- __ZN11HapticSynth15enableRenderingEjb
- __ZN11HapticSynth15releaseChannelsERKNSt3__16vectorIjNS0_9allocatorIjEEEE
- __ZN11HapticSynth18doForHapticOutputsIZN17LegacyHapticSynth12startRunningEbbjNSt3__18functionIFivEEEjE3$_2EEvOT_
- __ZN11HapticSynth18doForHapticOutputsIZN22MultiOutputHapticSynth12startRunningEbbjNSt3__18functionIFivEEEjE3$_2EEvOT_
- __ZN11HapticSynth18enableSubRenderingEjb
- __ZN11HapticSynth18setSynthRenderProcEPvPFvS0_RK14AudioTimeStampjE
- __ZN11HapticSynth19clearSoundingEventsEjj
- __ZN11HapticSynth24getAvailableChannelCountEv
- __ZN11HapticSynth9stopEventEjjj
- __ZN11PListLogger12logDictEntryEPKvS1_Pv
- __ZN11PListLogger12logItemEntryEPKvPKcPv
- __ZN11SequenceFSM10StateFront10PausedExitclINS_9ForceStopEN5boost3msm4back13state_machineINS0_11ActiveFrontENS4_9parameter5void_ESA_SA_SA_EENS5_5front4euml10func_stateINS0_11PausedNamerENS0_11PausedEntryES1_NS4_6fusion6vectorIJEEENS4_3mpl6vectorINS_9IsRunningEN4mpl_2naESO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_EENSL_INS_4SeekESO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_EENS_9NamedBaseISF_EEEEEEvRKT_RT0_RT1_
- __ZN11SequenceFSM10StateFront11RunningExitclINS_9ForceStopEN5boost3msm4back13state_machineINS0_11ActiveFrontENS4_9parameter5void_ESA_SA_SA_EENS5_5front4euml10func_stateINS0_12RunningNamerENS0_12RunningEntryES1_NS4_6fusion6vectorIJEEENS4_3mpl6vectorINS_9IsRunningEN4mpl_2naESO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_EENSK_7vector0ISO_EENS_9NamedBaseISF_EEEEEEvRKT_RT0_RT1_
- __ZN11SequenceFSM10StateFront12DefaultEntryclINS_13SequenceEndedEN5boost3msm4back13state_machineINS0_11ActiveFrontENS4_9parameter5void_ESA_SA_SA_EENS5_5front4euml10func_stateINS0_13FlushingNamerES1_NS0_12FlushingExitENS4_6fusion6vectorIJEEENS4_3mpl6vectorINS_10IsFlushingEN4mpl_2naESO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_EENSK_7vector0ISO_EENS0_12FlushingBaseISF_EEEEEEvRKT_RT0_RT1_
- __ZN11SequenceFSM10StateFront12DefaultEntryclINS_13SequenceEndedEN5boost3msm4back13state_machineIS0_NS4_9parameter5void_ES9_S9_S9_EENS5_5front4euml10func_stateINS0_13FinishedNamerES1_NS0_11DefaultExitENS4_6fusion6vectorIJEEENS4_3mpl6vectorINS_10IsFinishedEN4mpl_2naESN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_EENSJ_7vector0ISN_EENS_9NamedBaseISE_EEEEEEvRKT_RT0_RT1_
- __ZN11SequenceFSM10StateFront12DefaultEntryclINS_4StopEN5boost3msm4back13state_machineIS0_NS4_9parameter5void_ES9_S9_S9_EENS5_5front4euml10func_stateINS0_13FinishedNamerES1_NS0_11DefaultExitENS4_6fusion6vectorIJEEENS4_3mpl6vectorINS_10IsFinishedEN4mpl_2naESN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_EENSJ_7vector0ISN_EENS_9NamedBaseISE_EEEEEEvRKT_RT0_RT1_
- __ZN11SequenceFSM10StateFront12DefaultEntryclINS_7DestroyEN5boost3msm4back13state_machineIS0_NS4_9parameter5void_ES9_S9_S9_EENS5_5front4euml10func_stateINS0_18UninitializedNamerES1_NS0_11DefaultExitENS4_6fusion6vectorIJEEENS4_3mpl7vector0IN4mpl_2naEEESN_NS_9NamedBaseISE_EEEEEEvRKT_RT0_RT1_
- __ZN11SequenceFSM10StateFront12DefaultEntryclINS_7PrepareEN5boost3msm4back13state_machineIS0_NS4_9parameter5void_ES9_S9_S9_EENS5_5front4euml10func_stateINS0_13PreparedNamerES1_NS0_11DefaultExitENS4_6fusion6vectorIJEEENS4_3mpl6vectorINS_10IsFinishedEN4mpl_2naESN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_EENSJ_7vector0ISN_EENS_9NamedBaseISE_EEEEEEvRKT_RT0_RT1_
- __ZN11SequenceFSM10StateFront12DefaultEntryclINS_9ForceStopEN5boost3msm4back13state_machineIS0_NS4_9parameter5void_ES9_S9_S9_EENS5_5front4euml10func_stateINS0_13FinishedNamerES1_NS0_11DefaultExitENS4_6fusion6vectorIJEEENS4_3mpl6vectorINS_10IsFinishedEN4mpl_2naESN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_SN_EENSJ_7vector0ISN_EENS_9NamedBaseISE_EEEEEEvRKT_RT0_RT1_
- __ZN11SequenceFSM10StateFront12FlushingExitclINS_9ForceStopEN5boost3msm4back13state_machineINS0_11ActiveFrontENS4_9parameter5void_ESA_SA_SA_EENS5_5front4euml10func_stateINS0_13FlushingNamerENS0_12DefaultEntryES1_NS4_6fusion6vectorIJEEENS4_3mpl6vectorINS_10IsFlushingEN4mpl_2naESO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_EENSK_7vector0ISO_EENS0_12FlushingBaseISF_EEEEEEvRKT_RT0_RT1_
- __ZN11SequenceFSM10StateFront12PausingEntryclINS_10BeginPauseEN5boost3msm4back13state_machineINS0_11ActiveFrontENS4_9parameter5void_ESA_SA_SA_EENS5_5front4euml10func_stateINS0_12PausingNamerES1_NS0_11PausingExitENS4_6fusion6vectorIJEEENS4_3mpl6vectorINS_9IsRunningENS_9IsPausingEN4mpl_2naESP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_EENSL_INS_6ResumeENS_4PlayENS_4SeekENS_4StopENS_13EnableLoopingESP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_SP_EENS_9NamedBaseISF_EEEEEEvRKT_RT0_RT1_
- __ZN11SequenceFSM10StateFront12RunningEntryclINS_4PlayEN5boost3msm4back13state_machineINS0_11ActiveFrontENS4_9parameter5void_ESA_SA_SA_EENS5_5front4euml10func_stateINS0_12RunningNamerES1_NS0_11RunningExitENS4_6fusion6vectorIJEEENS4_3mpl6vectorINS_9IsRunningEN4mpl_2naESO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_EENSK_7vector0ISO_EENS_9NamedBaseISF_EEEEEEvRKT_RT0_RT1_
- __ZN11SequenceFSM10StateFront12RunningEntryclINS_6ResumeEN5boost3msm4back13state_machineINS0_11ActiveFrontENS4_9parameter5void_ESA_SA_SA_EENS5_5front4euml10func_stateINS0_12RunningNamerES1_NS0_11RunningExitENS4_6fusion6vectorIJEEENS4_3mpl6vectorINS_9IsRunningEN4mpl_2naESO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_SO_EENSK_7vector0ISO_EENS_9NamedBaseISF_EEEEEEvRKT_RT0_RT1_
- __ZN11SequenceFSM10StateFront12StoppingExitclINS_9ForceStopEN5boost3msm4back13state_machineINS0_11ActiveFrontENS4_9parameter5void_ESA_SA_SA_EENS5_5front4euml10func_stateINS0_13StoppingNamerENS0_13StoppingEntryES1_NS4_6fusion6vectorIJEEENS4_3mpl7vector0IN4mpl_2naEEESO_NS_9NamedBaseISF_EEEEEEvRKT_RT0_RT1_
- __ZN11SequenceFSM10StateFront13StoppingEntryclINS_4StopEN5boost3msm4back13state_machineINS0_11ActiveFrontENS4_9parameter5void_ESA_SA_SA_EENS5_5front4euml10func_stateINS0_13StoppingNamerES1_NS0_12StoppingExitENS4_6fusion6vectorIJEEENS4_3mpl7vector0IN4mpl_2naEEESO_NS_9NamedBaseISF_EEEEEEvRKT_RT0_RT1_
- __ZN11TOpaqueRTTII10AQMEIO_HALE5sRTTIE
- __ZN11TOpaqueRTTII10TOpaqueRefIN5Phase13ServerManagerEEE5sRTTIE
- __ZN11TOpaqueRTTII13SequenceTrackE5sRTTIE
- __ZN11TOpaqueRTTII14AQOfflineMixerE5sRTTIE
- __ZN11TOpaqueRTTII14AudioTapObjectE5sRTTIE
- __ZN11TOpaqueRTTII14AudioUnitGraphE5sRTTIE
- __ZN11TOpaqueRTTII14RemoteIOClientE5sRTTIE
- __ZN11TOpaqueRTTII14SequencePlayerE5sRTTIE
- __ZN11TOpaqueRTTII15AQProcessingTapE5sRTTIE
- __ZN11TOpaqueRTTII15AudioQueueOwnerE5sRTTIE
- __ZN11TOpaqueRTTII15SubmixTapObjectE5sRTTIE
- __ZN11TOpaqueRTTII16AQProcessingNodeE5sRTTIE
- __ZN11TOpaqueRTTII17ZenAQIONodeClientE5sRTTIE
- __ZN11TOpaqueRTTII21ExportedTrackIteratorE5sRTTIE
- __ZN11TOpaqueRTTII8SequenceE5sRTTIE
- __ZN11TOpaqueRTTIIN12CADeprecated11XMachServer6ClientEE5sRTTIE
- __ZN11TOpaqueRTTIIN2AQ3API12OfflineMixerEE5sRTTIE
- __ZN11TOpaqueRTTIIN2AQ3API13ProcessingTapEE5sRTTIE
- __ZN11TOpaqueRTTIIN2AQ3API14ProcessingNodeEE5sRTTIE
- __ZN11TOpaqueRTTIIN2AQ3API5QueueEE5sRTTIE
- __ZN11TOpaqueRTTIIN2AQ3API9SubmixTapEE5sRTTIE
- __ZN12CADeprecated10TSingletonI13HapticMetricsE5sOnceE
- __ZN12CADeprecated10TSingletonI13HapticMetricsE9sInstanceE
- __ZN12CADeprecated11XMachServer6Client11PrintObjectEP7__sFILE
- __ZN12CADeprecated11XMachServerC2ERKNS_14XMIGServerInfoEPKci
- __ZN12CADeprecated13TAtomicStack2IN16XAtomicAllocator8FreeNodeEE10pop_atomicEv
- __ZN12CADeprecated13TAtomicStack2IN16XAtomicAllocator8FreeNodeEE11push_atomicEPS2_
- __ZN12CADeprecated15XBasicMIGServer22SetServerDispatchQueueERKN10applesauce8dispatch2v15queueE
- __ZN12CADeprecated22XMachPortDeathListener33SetDeathNotificationDispatchQueueERKN10applesauce8dispatch2v15queueE
- __ZN12CADeprecated4TaskD2Ev
- __ZN12CADeprecated7CAGuardC1EPKc
- __ZN12CADeprecated7CAMutexC1EPKc
- __ZN12CADeprecated7XThread4StopEv
- __ZN12CADeprecated9CAPThread7SetNameEPKc
- __ZN12CADeprecated9CAPThreadD2Ev
- __ZN12CASerializer10WritePlistEPKv
- __ZN12CASerializer5WriteEPKvjj
- __ZN12CASerializerC1EP8__CFData
- __ZN12MemoryStream7GetDataEv
- __ZN12MemoryStreamC1Ev
- __ZN12SequenceImpl13enableLoopingEbj
- __ZN12SequenceImpl19setFinishedCallbackENSt3__18functionIFvmEEE
- __ZN13AQCommandList4ShowEP7__sFILE
- __ZN13AQMETapInsert15AllocateBuffersEv
- __ZN13AudioTapMixer13sendMixToTapsERK14AudioTimeStampjRK15AudioBufferList
- __ZN13CACFFormatterC1EPKv
- __ZN13HapticMetrics13markEngineOffEi
- __ZN13HapticMetrics15sHapticABCTokenE
- __ZN13HapticMetrics16logPowerLogEventE25HapticMetricsPowerLogTypemmm
- __ZN13HapticMetrics26sHapticAutoBugCaptureTimerE
- __ZN13HapticMetrics29markHapticAutoBugCaptureFiledEv
- __ZN13HapticMetrics30sHapticAutoBugCaptureAvailableE.0
- __ZN13HapticMetrics6onTimeEv
- __ZN13HapticMetricsC1Ev
- __ZN13SequenceTrack11PrintObjectEP7__sFILE
- __ZN13ServerManager10flushEntryENSt3__110shared_ptrI11ClientEntryEEf
- __ZN13ServerManager12stopSequenceENSt3__110shared_ptrI11ClientEntryEEmi
- __ZN13ServerManager13handleCommandERKNS_12SynthCommandEiNSt3__18functionIFS1_vEEE
- __ZN13ServerManager25handleRouteChangeForEntryENSt3__110shared_ptrI11ClientEntryEEbNS0_8optionalIbEE
- __ZN13ServerManager35cancelOngoingParameterCurveOfSameIDENSt3__110shared_ptrI11ClientEntryEERK13HapticCommand
- __ZN13XOSTransactor14endTransactionEv
- __ZN14AQIONodeClient11DescriptionC2ERKS_
- __ZN14AQIONodeClient11PrintObjectEP7__sFILE
- __ZN14AQOfflineMixer11PrintObjectEP7__sFILE
- __ZN14AudioTapObject11PrintObjectEP7__sFILE
- __ZN14AudioUnitGraph11PrintObjectEP7__sFILE
- __ZN14CACFDictionary13AddDictionaryEPK10__CFStringPK14__CFDictionary
- __ZN14CACFDictionary7AddDataEPK10__CFStringPK8__CFData
- __ZN14CACFDictionary9AddCFTypeEPK10__CFStringPKv
- __ZN14CACFDictionary9AddSInt32EPK10__CFStringi
- __ZN14CACFDictionary9AddStringEPK10__CFStringS2_
- __ZN14CADeserializer4ReadEPvjj
- __ZN14CADeserializerC1EPKvm
- __ZN14SSSClientEntry19handleSequenceEndedEmN5caulk16inplace_functionIFvmELm32ELm8ENS0_23inplace_function_detail6vtableEEE
- __ZN14SSSClientEntry21prepareSequenceWithIDEmNSt3__18functionIFvmEEE
- __ZN14SequencePlayer11PrintObjectEP7__sFILE
- __ZN14TuningPListMgr20loadTuningInSubdirs_EPPK10CACFStringjNS_15kTuningFileTypeE
- __ZN14TuningPListMgrC2EPKc
- __ZN14TuningPListMgrD1Ev
- __ZN15AQProcessingTap11PrintObjectEP7__sFILE
- __ZN15AudioQueueOwner11PrintObjectEP7__sFILE
- __ZN15OpaqueObjectMgr9sInstanceE
- __ZN15SubmixTapObject11PrintObjectEP7__sFILE
- __ZN16AQProcessingNode11PrintObjectEP7__sFILE
- __ZN16AudioQueueObject11PrintObjectEP7__sFILE
- __ZN16AudioQueueObject31CorrectTimePitchUnflushedFramesEddR8AQIONode
- __ZN16AudioQueueObject31QueryTimePitchPullAheadEstimateExxddR8AQIONode
- __ZN16AudioQueueObject5StartERK15XAudioTimeStampj
- __ZN16AudioQueueObject8EndPauseEPK15XAudioTimeStampbj
- __ZN16BaseOpaqueObject16ResolveOpaqueRefERKNS_4RTTIENS_3RefE
- __ZN16BaseOpaqueObject16destroyOpaqueRefEv
- __ZN16BaseOpaqueObject9checkRTTIERKNS_4RTTIE
- __ZN16BaseOpaqueObject9sBaseRTTIE
- __ZN16BaseOpaqueObjectC2Ev
- __ZN16BaseOpaqueObjectD2Ev
- __ZN16SSSAudioDataList3AddEP12SSSAudioData
- __ZN16SSSAudioDataList6RemoveEP12SSSAudioData
- __ZN16TAtomicAllocatorI15AQBufferCommandED0Ev
- __ZN16TAtomicAllocatorI15AQBufferCommandED1Ev
- __ZN16TCustomAllocatedI16XAtomicAllocator9AQCommandEnwEmRS0_
- __ZN16XAtomicAllocatorD0Ev
- __ZN16XAtomicAllocatorD1Ev
- __ZN16XAtomicAllocatorD2Ev
- __ZN17CACFMutableStringD2Ev
- __ZN17LegacyHapticSynth25hardwareSampleRateChangedER11SynthOutput
- __ZN17ParameterSchedule8AddEventEPNS_5EventE
- __ZN17PlatformUtilities11processNameEi
- __ZN17PlatformUtilities15IsInternalBuildEv
- __ZN17PlatformUtilities26CopyHardwareModelShortNameEv
- __ZN17ResolvedOpaqueRefI10AQMEIO_HALEC2EN16BaseOpaqueObject3RefE
- __ZN17ResolvedOpaqueRefI15AudioQueueOwnerEC2EN16BaseOpaqueObject3RefE
- __ZN17ZenAQIONodeClient11PrintObjectEP7__sFILE
- __ZN18CASmartPreferences10AddHandlerIxEEvPK10__CFStringS3_PFT_PKvRbENSt3__18functionIFvS4_EEE
- __ZN18CASmartPreferences14InterpretFloatEPKvRb
- __ZN18CASmartPreferences16InterpretBooleanEPKvRb
- __ZN18CASmartPreferences16InterpretIntegerEPKvRb
- __ZN18CASmartPreferences21_RegisterFirstHandlerEPK10__CFStringS2_NSt3__18functionIFbPKvEEE
- __ZN18CASmartPreferences4ReadEPK10__CFStringS2_Rb
- __ZN18CASmartPreferences4ReadEPK10__CFStringS2_Rf
- __ZN18CASmartPreferences4ReadEPK10__CFStringS2_Ri
- __ZN18CASmartPreferences8instanceEv
- __ZN18ParameterFormatterC2EjPKjPKf
- __ZN18SSClientCompletion25AddEntryForNewPlayAttemptEjU13block_pointerFvvE
- __ZN19SSClientPlayOptionsC1EjPK14__CFDictionary
- __ZN19SSClientPlayOptionsD1Ev
- __ZN19SharableMemoryBlock10InitClientERNS_11ClientTokenE
- __ZN20AHSPowerBudgetServer34copyThermalBudgetRangeInMilliWattsEv
- __ZN20AudioQueueXPC_Bridge5StartEj19XAudioTimeStampBasej
- __ZN20AudioQueueXPC_Client5StartEj19XAudioTimeStampBasej
- __ZN20AudioQueueXPC_Server5StartEj19XAudioTimeStampBasej
- __ZN20HapticEventConverter11loadPatternEP7NSArrayRbS2_
- __ZN20VADPowerBudgetServer34copyThermalBudgetRangeInMilliWattsEv
- __ZN21ExportedTrackIterator11PrintObjectEP7__sFILE
- __ZN21PlatformUtilities_iOS25CopyProductTypeFilePrefixE14iOSProductType
- __ZN21ResourcePathUtilitiesL14CFDictFromPathERKN10applesauce2CF9StringRefE.3645
- __ZN21ResourcePathUtilitiesL19ResolveResourcePathERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_.3644
- __ZN21ScheduledSlicePlayer212SetStartTimeERK15XAudioTimeStampxj
- __ZN21SpatializationManager32GetAUSpatialMixerHeadphonePresetENS_18SpatializationModeEibj
- __ZN21VibeToHapticConverter11loadPatternEP12NSDictionary
- __ZN22AUGraphLiveUpdateEvent5PrintEP7__sFILE
- __ZN22MultiOutputHapticSynth25hardwareSampleRateChangedER11SynthOutput
- __ZN22SpatializationLoggerV111AddToHeaderENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES6_
- __ZN24AudioServicesCoreHaptics18PrewarmSystemSoundEjb
- __ZN25MEParallelPathSubmixGraph15_addSourceGraphER13MESubmixGraphR24MEEnhanceableSubmixGraphb
- __ZN27ScheduledSlicePlayer_Legacy12SetStartTimeERK15XAudioTimeStampxj
- __ZN2AQ3API12OfflineMixer11PrintObjectEP7__sFILE
- __ZN2AQ3API13ProcessingTap11PrintObjectEP7__sFILE
- __ZN2AQ3API14ProcessingNode11PrintObjectEP7__sFILE
- __ZN2AQ3API5Queue11PrintObjectEP7__sFILE
- __ZN2AQ3API9SubmixTap11PrintObjectEP7__sFILE
- __ZN2AQ6Server12RemoteClient12forEachQueueIRKN5caulk12function_refIFvjEEEEEvbOT_
- __ZN2CA13ChannelLayout28SetNumberChannelDescriptionsEj
- __ZN41AppleHapticsSupportPowerInterfaceResource25clampBudgetToRangeMinimumEP8NSStringj
- __ZN41AppleHapticsSupportPowerInterfaceResource8getValueIiEEKNSt3__18optionalIT_EEPK10__CFString
- __ZN4swix10connection5state17cancel_connectionENS_19CancellationContextE
- __ZN4swix10connectionD2Ev
- __ZN5boost3msm4back13state_machineIN11SequenceFSM10StateFront11ActiveFrontENS_9parameter5void_ES7_S7_S7_E13execute_entryINS8_7exit_ptINS5_10ActiveExitEEENS3_9ForceStopES8_EENS_9enable_ifINS1_14is_pseudo_exitIT_E4typeEvE4typeERSG_RKT0_RT1_NS1_5dummyILi2EEE
- __ZN5boost8functionIFvRN11SequenceFSM25PostRenderFlushingVisitorEP14SequenceActiondEEaSINS_3_bi6bind_tIvNS_4_mfi4cmf3IvNS1_10StateFront12FlushingBaseINSD_13FlushingNamerEEES3_S5_dEENS9_5list4INS_17reference_wrapperINS_3msm5front4euml10func_stateISF_NSD_12DefaultEntryENSD_12FlushingExitENS_6fusion6vectorIJEEENS_3mpl6vectorINS1_10IsFlushingEN4mpl_2naESX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_SX_EENST_7vector0ISX_EESG_EEEENS_3argILi1EEENS13_ILi2EEENS13_ILi3EEEEEEEEENS_10enable_if_IXntsr11is_integralIT_EE5valueERS7_E4typeES1A_
- __ZN5boost8functionIFvRN11SequenceFSM25PostRenderFlushingVisitorEP14SequenceActiondEEaSINS_3_bi6bind_tIvNS_4_mfi4cmf3IvNS1_9StateBaseES3_S5_dEENS9_5list4INS_17reference_wrapperINS_3msm4back13state_machineINS1_10StateFront11ActiveFrontENS_9parameter5void_ESN_SN_SN_E7exit_ptINSL_10ActiveExitEEEEENS_3argILi1EEENST_ILi2EEENST_ILi3EEEEEEEEENS_10enable_if_IXntsr11is_integralIT_EE5valueERS7_E4typeES10_
- __ZN5boost8functionIFvRN11SequenceFSM25PostRenderFlushingVisitorEP14SequenceActiondEEaSINS_3_bi6bind_tIvNS_4_mfi4cmf3IvNS1_9StateBaseES3_S5_dEENS9_5list4INS_17reference_wrapperINS_3msm5front4euml10func_stateINS1_10StateFront11PausedNamerENSL_11PausedEntryENSL_10PausedExitENS_6fusion6vectorIJEEENS_3mpl6vectorINS1_9IsRunningEN4mpl_2naESW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_EENST_INS1_4SeekESW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_EENS1_9NamedBaseISM_EEEEEENS_3argILi1EEENS14_ILi2EEENS14_ILi3EEEEEEEEENS_10enable_if_IXntsr11is_integralIT_EE5valueERS7_E4typeES1B_
- __ZN5boost8functionIFvRN11SequenceFSM25PostRenderFlushingVisitorEP14SequenceActiondEEaSINS_3_bi6bind_tIvNS_4_mfi4cmf3IvNS1_9StateBaseES3_S5_dEENS9_5list4INS_17reference_wrapperINS_3msm5front4euml10func_stateINS1_10StateFront12RunningNamerENSL_12RunningEntryENSL_11RunningExitENS_6fusion6vectorIJEEENS_3mpl6vectorINS1_9IsRunningEN4mpl_2naESW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_SW_EENSS_7vector0ISW_EENS1_9NamedBaseISM_EEEEEENS_3argILi1EEENS14_ILi2EEENS14_ILi3EEEEEEEEENS_10enable_if_IXntsr11is_integralIT_EE5valueERS7_E4typeES1B_
- __ZN5boost8functionIFvRN11SequenceFSM25PostRenderFlushingVisitorEP14SequenceActiondEEaSINS_3_bi6bind_tIvNS_4_mfi4cmf3IvNS1_9StateBaseES3_S5_dEENS9_5list4INS_17reference_wrapperINS_3msm5front4euml10func_stateINS1_10StateFront13StoppingNamerENSL_13StoppingEntryENSL_12StoppingExitENS_6fusion6vectorIJEEENS_3mpl7vector0IN4mpl_2naEEESW_NS1_9NamedBaseISM_EEEEEENS_3argILi1EEENS11_ILi2EEENS11_ILi3EEEEEEEEENS_10enable_if_IXntsr11is_integralIT_EE5valueERS7_E4typeES18_
- __ZN5boost9typeindex6detailL23ctti_skip_until_runtimeE.9574
- __ZN5caulk10concurrent16shared_spin_lock11lock_sharedEv
- __ZN5caulk10concurrent16shared_spin_lock13unlock_sharedEv
- __ZN5caulk10concurrent16shared_spin_lock4lockEv
- __ZN5caulk10concurrent16shared_spin_lock6unlockEv
- __ZN5caulk10concurrent16shared_spin_lockD2Ev
- __ZN5caulk10concurrent5stackINS_5alloc10free_blockENS0_26intrusive_single_link_nodeIS3_EEE3popEv
- __ZN5caulk10concurrent7details12message_callIRZN11ClientEntry19handleSequenceEndedEmNS_16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEEEE3$_0JEE7performEv
- __ZN5caulk10concurrent7details12message_callIRZN11ClientEntry19handleSequenceEndedEmNS_16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEEEE3$_0JEED0Ev
- __ZN5caulk10concurrent7details12message_callIRZN11ClientEntry19handleSequenceEndedEmNS_16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEEEE3$_0JEED1Ev
- __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry18playSequenceWithIDEmddE3$_0JEE10rt_cleanupD1Ev
- __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry18playSequenceWithIDEmddE3$_0JEE7performEv
- __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry18playSequenceWithIDEmddE3$_0JEED0Ev
- __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry18playSequenceWithIDEmddE3$_0JEED1Ev
- __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry19handleSequenceEndedEmNS_16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEEEE3$_0JEE10rt_cleanupD1Ev
- __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry19handleSequenceEndedEmNS_16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEEEE3$_0JEE7performEv
- __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry19handleSequenceEndedEmNS_16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEEEE3$_0JEED0Ev
- __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry19handleSequenceEndedEmNS_16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEEEE3$_0JEED1Ev
- __ZN5caulk10concurrent7details15rt_message_callIRZN17AudioEventManager32disableAndRemoveCustomAudioEventEjE3$_0JEE10rt_cleanupD1Ev
- __ZN5caulk10concurrent7details15rt_message_callIRZN17AudioEventManager32disableAndRemoveCustomAudioEventEjE3$_0JEE7performEv
- __ZN5caulk10concurrent7details15rt_message_callIRZN17AudioEventManager32disableAndRemoveCustomAudioEventEjE3$_0JEED0Ev
- __ZN5caulk10concurrent7details15rt_message_callIRZN17AudioEventManager32disableAndRemoveCustomAudioEventEjE3$_0JEED1Ev
- __ZN5caulk10concurrent8skiplistIPvNS_5alloc6detail13tracked_blockELi10ELNS0_16skiplist_optionsE0EE13random_engineEv
- __ZN5caulk16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEE16k_wrapper_vtableINSt3__18functionIS1_EEEE
- __ZN5caulk19multi_simple_randomIjLm4ENSt3__124uniform_int_distributionIjEENS1_23mersenne_twister_engineIjLm32ELm624ELm397ELm31ELj2567483615ELm11ELj4294967295ELm7ELj2636928640ELm15ELj4022730752ELm18ELj1812433253EEEEC2Ejj
- __ZN5caulk2rt6vectorIcE6resizeEm
- __ZN5caulk5alloc15multi_free_listINS0_19cascading_allocatorINS0_15chunk_allocatorINS0_17global_page_cacheENS0_16serial_allocatorENS0_18embed_block_memoryELm16384EJEEEEENS_10concurrent7details14node_allocatorIPvNS0_6detail13tracked_blockELm10ELNS9_16skiplist_optionsE0EE14size_generatorELm8ELm1ELln1EE10deallocateENS0_5blockEm
- __ZN7TStream10WriteBig16Et
- __ZN7TStream10WriteBig32Ej
- __ZN7TStream12ReadLittle16Ev
- __ZN7TStream12ReadLittle32Ev
- __ZN7TStream14ReadBigFloat32Ev
- __ZN7TStream14ReadBigFloat64Ev
- __ZN7TStream8ReadByteEv
- __ZN7TStream9ReadBig16Ev
- __ZN7TStream9ReadBig32Ev
- __ZN7TStream9WriteByteEh
- __ZN8RTLockedINSt3__13mapEKjJjEEC2EPKc
- __ZN8RTLockedINSt3__13mapEKjJjEED1Ev
- __ZN8RTLockedINSt3__13mapEmJNS0_10shared_ptrI11ClientEntryEEEED1Ev
- __ZN8RTLockedINSt3__13mapEmJjEED1Ev
- __ZN8Sequence11PrintObjectEP7__sFILE
- __ZN8TempoMap13AddTempoEventEdd
- __ZN9CACFArray12AppendStringEPK10__CFString
- __ZN9CACFArray16AppendDictionaryEPK14__CFDictionary
- __ZNK10PowerMeter10LinearToDBEd
- __ZNK11CAException4whatEv
- __ZNK11MultiReaderINSt3__13mapImjNS0_4lessImEENS0_9allocatorINS0_4pairIKmjEEEEEEE4findEm
- __ZNK11PListLogger3logEPKcz
- __ZNK13TOpaqueObjectI10AQMEIO_HALj16BaseOpaqueObjectE3isaERKNS1_4RTTIE
- __ZNK13TOpaqueObjectI10TOpaqueRefIN5Phase13ServerManagerEEj16BaseOpaqueObjectE3isaERKNS4_4RTTIE
- __ZNK13TOpaqueObjectI13SequenceTrackP16OpaqueMusicTrack16BaseOpaqueObjectE3isaERKNS3_4RTTIE
- __ZNK13TOpaqueObjectI14AQOfflineMixerj16BaseOpaqueObjectE3isaERKNS1_4RTTIE
- __ZNK13TOpaqueObjectI14AudioTapObjectP14OpaqueAudioTap16BaseOpaqueObjectE3isaERKNS3_4RTTIE
- __ZNK13TOpaqueObjectI14AudioUnitGraphP13OpaqueAUGraph16BaseOpaqueObjectE3isaERKNS3_4RTTIE
- __ZNK13TOpaqueObjectI14RemoteIOClientjN12CADeprecated11XMachServer6ClientEE3isaERKN16BaseOpaqueObject4RTTIE
- __ZNK13TOpaqueObjectI14SequencePlayerP17OpaqueMusicPlayer16BaseOpaqueObjectE3isaERKNS3_4RTTIE
- __ZNK13TOpaqueObjectI15AQProcessingTapj16BaseOpaqueObjectE3isaERKNS1_4RTTIE
- __ZNK13TOpaqueObjectI15AudioQueueOwnerj16BaseOpaqueObjectE3isaERKNS1_4RTTIE
- __ZNK13TOpaqueObjectI15SubmixTapObjectj16BaseOpaqueObjectE3isaERKNS1_4RTTIE
- __ZNK13TOpaqueObjectI16AQProcessingNodej16BaseOpaqueObjectE3isaERKNS1_4RTTIE
- __ZNK13TOpaqueObjectI17ZenAQIONodeClientj16BaseOpaqueObjectE3isaERKNS1_4RTTIE
- __ZNK13TOpaqueObjectI21ExportedTrackIteratorP24OpaqueMusicEventIterator16BaseOpaqueObjectE3isaERKNS3_4RTTIE
- __ZNK13TOpaqueObjectI8SequenceP19OpaqueMusicSequence16BaseOpaqueObjectE3isaERKNS3_4RTTIE
- __ZNK13TOpaqueObjectIN12CADeprecated11XMachServer6ClientEj16BaseOpaqueObjectE3isaERKNS3_4RTTIE
- __ZNK13TOpaqueObjectIN2AQ3API12OfflineMixerEP20OpaqueAQOfflineMixer16BaseOpaqueObjectE3isaERKNS5_4RTTIE
- __ZNK13TOpaqueObjectIN2AQ3API13ProcessingTapEP29OpaqueAudioQueueProcessingTap16BaseOpaqueObjectE3isaERKNS5_4RTTIE
- __ZNK13TOpaqueObjectIN2AQ3API14ProcessingNodeEP27OpaqueATAudioProcessingNode16BaseOpaqueObjectE3isaERKNS5_4RTTIE
- __ZNK13TOpaqueObjectIN2AQ3API5QueueEP16OpaqueAudioQueue16BaseOpaqueObjectE3isaERKNS5_4RTTIE
- __ZNK13TOpaqueObjectIN2AQ3API9SubmixTapEP17OpaqueATSubmixTap16BaseOpaqueObjectE3isaERKNS5_4RTTIE
- __ZNK14CACFDictionary6GetURLEPK10__CFStringRPK7__CFURL
- __ZNK14CACFDictionary6HasKeyEPK10__CFString
- __ZNK14TuningPListMgr16getAUPListByNameEPKc
- __ZNK17AQIONodeSpecifier11descriptionEv
- __ZNK5caulk10concurrent26lf_read_synchronized_writeIP13AudioTapMixerE4readEv
- __ZNKRSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB9nqe210106Ev
- __ZNKRSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB9nqe210106Ev
- __ZNKSt3__110__function6__funcIN5caulk16inplace_functionIFvmELm32ELm8ENS2_23inplace_function_detail6vtableEEES4_E7__cloneEPNS0_6__baseIS4_EE
- __ZNKSt3__110__function6__funcIN5caulk16inplace_functionIFvmELm32ELm8ENS2_23inplace_function_detail6vtableEEES4_E7__cloneEv
- __ZNKSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEEN5caulk16inplace_functionIFvmELm32ELm8ENS6_23inplace_function_detail6vtableEEEE3$_0S8_E7__cloneEPNS0_6__baseIS8_EE
- __ZNKSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEEN5caulk16inplace_functionIFvmELm32ELm8ENS6_23inplace_function_detail6vtableEEEE3$_0S8_E7__cloneEv
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM10BeginPauseEEEiRKT_EUliE_FviEE7__cloneEPNS0_6__baseISA_EE
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM10BeginPauseEEEiRKT_EUliE_FviEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI12NSDictionaryEEEEiRKT_EUliE_FviEE7__cloneEPNS0_6__baseISC_EE
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI12NSDictionaryEEEEiRKT_EUliE_FviEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI6NSDataEEEEiRKT_EUliE_FviEE7__cloneEPNS0_6__baseISC_EE
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI6NSDataEEEEiRKT_EUliE_FviEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI7NSArrayEEEEiRKT_EUliE_FviEE7__cloneEPNS0_6__baseISC_EE
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI7NSArrayEEEEiRKT_EUliE_FviEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4PlayEEEiRKT_EUliE_FviEE7__cloneEPNS0_6__baseISA_EE
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4PlayEEEiRKT_EUliE_FviEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4SeekEEEiRKT_EUliE_FviEE7__cloneEPNS0_6__baseISA_EE
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4SeekEEEiRKT_EUliE_FviEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4StopEEEiRKT_EUliE_FviEE7__cloneEPNS0_6__baseISA_EE
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4StopEEEiRKT_EUliE_FviEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM5StartEEEiRKT_EUliE_FviEE7__cloneEPNS0_6__baseISA_EE
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM5StartEEEiRKT_EUliE_FviEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM6DetachEEEiRKT_EUliE_FviEE7__cloneEPNS0_6__baseISA_EE
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM6DetachEEEiRKT_EUliE_FviEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM6ResumeEEEiRKT_EUliE_FviEE7__cloneEPNS0_6__baseISA_EE
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM6ResumeEEEiRKT_EUliE_FviEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM7PrepareEEEiRKT_EUliE_FviEE7__cloneEPNS0_6__baseISA_EE
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM7PrepareEEEiRKT_EUliE_FviEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM9ForceStopEEEiRKT_EUliE_FviEE7__cloneEPNS0_6__baseISA_EE
- __ZNKSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM9ForceStopEEEiRKT_EUliE_FviEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_0FKNS2_12SynthCommandEvEE7__cloneEPNS0_6__baseIS9_EE
- __ZNKSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_0FKNS2_12SynthCommandEvEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN13ServerManager25handleRouteChangeForEntryENS_10shared_ptrI11ClientEntryEEbNS_8optionalIbEEE3$_0FvbEE7__cloneEPNS0_6__baseIS9_EE
- __ZNKSt3__110__function6__funcIZN13ServerManager25handleRouteChangeForEntryENS_10shared_ptrI11ClientEntryEEbNS_8optionalIbEEE3$_0FvbEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN14DSP_Routing_VPC1ER10AQMEIO_DSPN11DSP_Routing12ERoutingTypeERKNS_6vectorI14MEStreamTypeIDNS_9allocatorIS8_EEEEbE3$_1FbjRKN15CAListenerProxy15HALNotificationEEE7__cloneEPNS0_6__baseISJ_EE
- __ZNKSt3__110__function6__funcIZN14DSP_Routing_VPC1ER10AQMEIO_DSPN11DSP_Routing12ERoutingTypeERKNS_6vectorI14MEStreamTypeIDNS_9allocatorIS8_EEEEbE3$_1FbjRKN15CAListenerProxy15HALNotificationEEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIbEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EE7__cloneEPNS0_6__baseISH_EE
- __ZNKSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIbEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIdEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EE7__cloneEPNS0_6__baseISH_EE
- __ZNKSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIdEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIxEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EE7__cloneEPNS0_6__baseISH_EE
- __ZNKSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIxEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RbEUlbE_FvbEE7__cloneEPNS0_6__baseIS8_EE
- __ZNKSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RbEUlbE_FvbEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RfEUldE_FvdEE7__cloneEPNS0_6__baseIS8_EE
- __ZNKSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RfEUldE_FvdEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RiEUlxE_FvxEE7__cloneEPNS0_6__baseIS8_EE
- __ZNKSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RiEUlxE_FvxEE7__cloneEv
- __ZNKSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERNS_10shared_ptrI11SynthOutputEEEUlvE_FvvEE7__cloneEPNS0_6__baseIS9_EE
- __ZNKSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERNS_10shared_ptrI11SynthOutputEEEUlvE_FvvEE7__cloneEv
- __ZNKSt3__111__copy_implclB9nqe210106IP11AQMESessionS3_S3_EENS_4pairIT_T1_EES5_T0_S6_
- __ZNKSt3__111__copy_implclB9nqe210106IP15MEVADIdentifierS3_S3_EENS_4pairIT_T1_EES5_T0_S6_
- __ZNKSt3__111__copy_implclB9nqe210106IPK11AQMESessionS4_PS2_EENS_4pairIT_T1_EES7_T0_S8_
- __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB9nqe210106IPNS_4pairIN5boost8functionIFNS5_3msm4back11HandledEnumEvEEEbEENS_16__deque_iteratorISC_SD_RSC_PSD_lLl102EEELi0EEENS4_IT_T0_EESI_SI_SJ_
- __ZNKSt3__112__hash_tableINS_17__hash_value_typeIPK15AudioBufferListNS_4pairINS_6chrono10time_pointINS6_12steady_clockENS6_8durationIxNS_5ratioILl1ELl1000000000EEEEEEEU8__strongP16AVAudioPCMBufferEEEENS_22__unordered_map_hasherIS4_NS5_IKS4_SH_EENS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_SL_SP_SN_Lb1EEENS_9allocatorISL_EEE4findIS4_EENS_21__hash_const_iteratorIPNS_11__hash_nodeISI_PvEEEERKT_
- __ZNKSt3__112__hash_tableINS_17__hash_value_typeIijEENS_22__unordered_map_hasherIiNS_4pairIKijEENS_4hashIiEENS_8equal_toIiEELb1EEENS_21__unordered_map_equalIiS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE19__equal_range_multiIiEENS4_INS_21__hash_const_iteratorIPNS_11__hash_nodeIS2_PvEEEESN_EERKT_
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findB9nqe210106EPKcm
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareB9nqe210106EmmRKS5_
- __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB9nqe210106ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
- __ZNKSt3__114default_deleteI13XOSTransactorEclB9nqe210106EPS1_
- __ZNKSt3__114default_deleteI15AudioTapManagerEclB9nqe210106EPS1_
- __ZNKSt3__114default_deleteI20SSSBufferClickFilterEclB9nqe210106EPS1_
- __ZNKSt3__114default_deleteI29AudioSessionPropertyListenersEclB9nqe210106EPS1_
- __ZNKSt3__114default_deleteI8AQBufferEclB9nqe210106EPS1_
- __ZNKSt3__114default_deleteIN12CADeprecated12CABufferListEEclB9nqe210106EPS2_
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE4viewB9nqe210106Ev
- __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB9nqe210106IPNS_4pairIN5boost8functionIFNS5_3msm4back11HandledEnumEvEEEbEENS_16__deque_iteratorISC_SD_RSC_PSD_lLl102EEELi0EEENS4_IT_T0_EESI_SI_SJ_
- __ZNKSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE8LocalityEENS_19__map_value_compareIS7_NS_4pairIKS7_S8_EENS_4lessIS7_EELb1EEENS5_ISD_EEE14__count_uniqueIS7_EEmRKT_
- __ZNKSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN10applesauce2CF7TypeRefEEENS_19__map_value_compareIS7_NS_4pairIKS7_SA_EENS_4lessIS7_EELb1EEENS5_ISF_EEE14__count_uniqueIS7_EEmRKT_
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB9nqe210106ERKS6_S9_
- __ZNKSt3__18functionIFvmEEclEm
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt12out_of_rangeC1B9nqe210106EPKc
- __ZNSt14overflow_errorC1B9nqe210106EPKc
- __ZNSt3__110__function12__value_funcIFKN13ServerManager12SynthCommandEvEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink19TappedAudioProducerENS_14default_deleteIS6_EEEEiEERKN2CA17StreamDescriptionERKNSB_13ChannelLayoutEiRKNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEEC2B9nqe210106ERKST_
- __ZNSt3__110__function12__value_funcIFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink19TappedAudioProducerENS_14default_deleteIS6_EEEEiEERKN2CA17StreamDescriptionERKNSB_13ChannelLayoutEiRKNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFN5caulk8expectedINS_10unique_ptrIN2AT11Translation25AsyncAudioStreamProcessorENS_14default_deleteIS7_EEEEiEENS6_14CallTranslator5ScopeERKNS6_24TranslationConfigurationEEEC2B9nqe210106ERKSI_
- __ZNSt3__110__function12__value_funcIFN5caulk8expectedINS_10unique_ptrIN2AT11Translation25AsyncAudioStreamProcessorENS_14default_deleteIS7_EEEEiEENS6_14CallTranslator5ScopeERKNS6_24TranslationConfigurationEEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFN5caulk8expectedIbiEEjEEC2B9nqe210106ERKS6_
- __ZNSt3__110__function12__value_funcIFN5caulk8expectedIbiEEjEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFNS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS3_EEEERK14AQMEIO_BindingRiEEC2B9nqe210106ERKSC_
- __ZNSt3__110__function12__value_funcIFNS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS3_EEEERK14AQMEIO_BindingRiEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEvEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFNS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEvEEC2B9nqe210106ERKSE_
- __ZNSt3__110__function12__value_funcIFNS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEvEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES8_EEN10applesauce2CF7TypeRefESC_EEC2B9nqe210106ERKSE_
- __ZNSt3__110__function12__value_funcIFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES8_EEN10applesauce2CF7TypeRefESC_EED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFP10MarshallervEEC2B9nqe210106ERKS5_
- __ZNSt3__110__function12__value_funcIFP10MarshallervEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFPK10__CFStringS4_EEC2B9nqe210106ERKS6_
- __ZNSt3__110__function12__value_funcIFPK10__CFStringS4_EED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFR26MutedSpeechActivityManagervEEC2B9nqe210106ERKS5_
- __ZNSt3__110__function12__value_funcIFR26MutedSpeechActivityManagervEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFbNS_10shared_ptrI11ClientEntryEEEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFbPKvEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFbR14AQIONodeClientEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFbRK26AudioObjectPropertyAddressEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFbRmbEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFbjRKN15CAListenerProxy15HALNotificationEEEC2B9nqe210106ERKS7_
- __ZNSt3__110__function12__value_funcIFbjRKN15CAListenerProxy15HALNotificationEEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFbjiEEC2B9nqe210106ERKS3_
- __ZNSt3__110__function12__value_funcIFbjiEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFbvEEC2B9nqe210106ERKS3_
- __ZNSt3__110__function12__value_funcIFbvEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFiN10applesauce3xpc6objectEEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFiP7__sFILEEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFivEEC2B9nqe210106ERKS3_
- __ZNSt3__110__function12__value_funcIFivEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFvN2AT11Translation14CallTranslator5ScopeENS3_17AudioInjectorModeEEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFvNS_6chrono10time_pointINS2_12steady_clockENS2_8durationIxNS_5ratioILl1ELl1000000000EEEEEEERK15AudioBufferListiEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFvPK14MIDIPacketListEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFvR11IAQMEDeviceEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFvbEEC2B9nqe210106EOS3_
- __ZNSt3__110__function12__value_funcIFvbEEC2B9nqe210106ERKS3_
- __ZNSt3__110__function12__value_funcIFvbEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFvdEEC2B9nqe210106ERKS3_
- __ZNSt3__110__function12__value_funcIFvdEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFviEEC2B9nqe210106ERKS3_
- __ZNSt3__110__function12__value_funcIFviEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFvmEEC2B9nqe210106ERKS3_
- __ZNSt3__110__function12__value_funcIFvmEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFvvEEC2B9nqe210106EOS3_
- __ZNSt3__110__function12__value_funcIFvvEEC2B9nqe210106ERKS3_
- __ZNSt3__110__function12__value_funcIFvvEED2B9nqe210106Ev
- __ZNSt3__110__function12__value_funcIFvxEEC2B9nqe210106ERKS3_
- __ZNSt3__110__function12__value_funcIFvxEED2B9nqe210106Ev
- __ZNSt3__110__function6__funcIN5caulk16inplace_functionIFvmELm32ELm8ENS2_23inplace_function_detail6vtableEEES4_E18destroy_deallocateEv
- __ZNSt3__110__function6__funcIN5caulk16inplace_functionIFvmELm32ELm8ENS2_23inplace_function_detail6vtableEEES4_E7destroyEv
- __ZNSt3__110__function6__funcIN5caulk16inplace_functionIFvmELm32ELm8ENS2_23inplace_function_detail6vtableEEES4_ED0Ev
- __ZNSt3__110__function6__funcIN5caulk16inplace_functionIFvmELm32ELm8ENS2_23inplace_function_detail6vtableEEES4_ED1Ev
- __ZNSt3__110__function6__funcIN5caulk16inplace_functionIFvmELm32ELm8ENS2_23inplace_function_detail6vtableEEES4_EclEOm
- __ZNSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEEN5caulk16inplace_functionIFvmELm32ELm8ENS6_23inplace_function_detail6vtableEEEE3$_0S8_E18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEEN5caulk16inplace_functionIFvmELm32ELm8ENS6_23inplace_function_detail6vtableEEEE3$_0S8_E7destroyEv
- __ZNSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEEN5caulk16inplace_functionIFvmELm32ELm8ENS6_23inplace_function_detail6vtableEEEE3$_0S8_ED0Ev
- __ZNSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEEN5caulk16inplace_functionIFvmELm32ELm8ENS6_23inplace_function_detail6vtableEEEE3$_0S8_ED1Ev
- __ZNSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEEN5caulk16inplace_functionIFvmELm32ELm8ENS6_23inplace_function_detail6vtableEEEE3$_0S8_EclEOm
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM10BeginPauseEEEiRKT_EUliE_FviEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM10BeginPauseEEEiRKT_EUliE_FviEE7destroyEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM10BeginPauseEEEiRKT_EUliE_FviEED0Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM10BeginPauseEEEiRKT_EUliE_FviEED1Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM10BeginPauseEEEiRKT_EUliE_FviEEclEOi
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI12NSDictionaryEEEEiRKT_EUliE_FviEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI12NSDictionaryEEEEiRKT_EUliE_FviEE7destroyEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI12NSDictionaryEEEEiRKT_EUliE_FviEED0Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI12NSDictionaryEEEEiRKT_EUliE_FviEED1Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI12NSDictionaryEEEEiRKT_EUliE_FviEEclEOi
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI6NSDataEEEEiRKT_EUliE_FviEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI6NSDataEEEEiRKT_EUliE_FviEE7destroyEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI6NSDataEEEEiRKT_EUliE_FviEED0Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI6NSDataEEEEiRKT_EUliE_FviEED1Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI6NSDataEEEEiRKT_EUliE_FviEEclEOi
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI7NSArrayEEEEiRKT_EUliE_FviEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI7NSArrayEEEEiRKT_EUliE_FviEE7destroyEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI7NSArrayEEEEiRKT_EUliE_FviEED0Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI7NSArrayEEEEiRKT_EUliE_FviEED1Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI7NSArrayEEEEiRKT_EUliE_FviEEclEOi
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4PlayEEEiRKT_EUliE_FviEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4PlayEEEiRKT_EUliE_FviEE7destroyEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4PlayEEEiRKT_EUliE_FviEED0Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4PlayEEEiRKT_EUliE_FviEED1Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4PlayEEEiRKT_EUliE_FviEEclEOi
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4SeekEEEiRKT_EUliE_FviEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4SeekEEEiRKT_EUliE_FviEE7destroyEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4SeekEEEiRKT_EUliE_FviEED0Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4SeekEEEiRKT_EUliE_FviEED1Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4SeekEEEiRKT_EUliE_FviEEclEOi
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4StopEEEiRKT_EUliE_FviEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4StopEEEiRKT_EUliE_FviEE7destroyEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4StopEEEiRKT_EUliE_FviEED0Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4StopEEEiRKT_EUliE_FviEED1Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4StopEEEiRKT_EUliE_FviEEclEOi
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM5StartEEEiRKT_EUliE_FviEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM5StartEEEiRKT_EUliE_FviEE7destroyEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM5StartEEEiRKT_EUliE_FviEED0Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM5StartEEEiRKT_EUliE_FviEED1Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM5StartEEEiRKT_EUliE_FviEEclEOi
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM6DetachEEEiRKT_EUliE_FviEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM6DetachEEEiRKT_EUliE_FviEE7destroyEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM6DetachEEEiRKT_EUliE_FviEED0Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM6DetachEEEiRKT_EUliE_FviEED1Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM6DetachEEEiRKT_EUliE_FviEEclEOi
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM6ResumeEEEiRKT_EUliE_FviEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM6ResumeEEEiRKT_EUliE_FviEE7destroyEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM6ResumeEEEiRKT_EUliE_FviEED0Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM6ResumeEEEiRKT_EUliE_FviEED1Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM6ResumeEEEiRKT_EUliE_FviEEclEOi
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM7PrepareEEEiRKT_EUliE_FviEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM7PrepareEEEiRKT_EUliE_FviEE7destroyEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM7PrepareEEEiRKT_EUliE_FviEED0Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM7PrepareEEEiRKT_EUliE_FviEED1Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM7PrepareEEEiRKT_EUliE_FviEEclEOi
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM9ForceStopEEEiRKT_EUliE_FviEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM9ForceStopEEEiRKT_EUliE_FviEE7destroyEv
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM9ForceStopEEEiRKT_EUliE_FviEED0Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM9ForceStopEEEiRKT_EUliE_FviEED1Ev
- __ZNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM9ForceStopEEEiRKT_EUliE_FviEEclEOi
- __ZNSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_0FKNS2_12SynthCommandEvEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_0FKNS2_12SynthCommandEvEE7destroyEv
- __ZNSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_0FKNS2_12SynthCommandEvEED0Ev
- __ZNSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_0FKNS2_12SynthCommandEvEED1Ev
- __ZNSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_0FKNS2_12SynthCommandEvEEclEv
- __ZNSt3__110__function6__funcIZN13ServerManager25handleRouteChangeForEntryENS_10shared_ptrI11ClientEntryEEbNS_8optionalIbEEE3$_0FvbEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN13ServerManager25handleRouteChangeForEntryENS_10shared_ptrI11ClientEntryEEbNS_8optionalIbEEE3$_0FvbEE7destroyEv
- __ZNSt3__110__function6__funcIZN13ServerManager25handleRouteChangeForEntryENS_10shared_ptrI11ClientEntryEEbNS_8optionalIbEEE3$_0FvbEED0Ev
- __ZNSt3__110__function6__funcIZN13ServerManager25handleRouteChangeForEntryENS_10shared_ptrI11ClientEntryEEbNS_8optionalIbEEE3$_0FvbEED1Ev
- __ZNSt3__110__function6__funcIZN13ServerManager25handleRouteChangeForEntryENS_10shared_ptrI11ClientEntryEEbNS_8optionalIbEEE3$_0FvbEEclEOb
- __ZNSt3__110__function6__funcIZN14DSP_Routing_VPC1ER10AQMEIO_DSPN11DSP_Routing12ERoutingTypeERKNS_6vectorI14MEStreamTypeIDNS_9allocatorIS8_EEEEbE3$_1FbjRKN15CAListenerProxy15HALNotificationEEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN14DSP_Routing_VPC1ER10AQMEIO_DSPN11DSP_Routing12ERoutingTypeERKNS_6vectorI14MEStreamTypeIDNS_9allocatorIS8_EEEEbE3$_1FbjRKN15CAListenerProxy15HALNotificationEEE7destroyEv
- __ZNSt3__110__function6__funcIZN14DSP_Routing_VPC1ER10AQMEIO_DSPN11DSP_Routing12ERoutingTypeERKNS_6vectorI14MEStreamTypeIDNS_9allocatorIS8_EEEEbE3$_1FbjRKN15CAListenerProxy15HALNotificationEEED0Ev
- __ZNSt3__110__function6__funcIZN14DSP_Routing_VPC1ER10AQMEIO_DSPN11DSP_Routing12ERoutingTypeERKNS_6vectorI14MEStreamTypeIDNS_9allocatorIS8_EEEEbE3$_1FbjRKN15CAListenerProxy15HALNotificationEEED1Ev
- __ZNSt3__110__function6__funcIZN14DSP_Routing_VPC1ER10AQMEIO_DSPN11DSP_Routing12ERoutingTypeERKNS_6vectorI14MEStreamTypeIDNS_9allocatorIS8_EEEEbE3$_1FbjRKN15CAListenerProxy15HALNotificationEEEclEOjSI_
- __ZNSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIbEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIbEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EE7destroyEv
- __ZNSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIbEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EED0Ev
- __ZNSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIbEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EED1Ev
- __ZNSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIbEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EEclEOS9_
- __ZNSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIdEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIdEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EE7destroyEv
- __ZNSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIdEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EED0Ev
- __ZNSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIdEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EED1Ev
- __ZNSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIdEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EEclEOS9_
- __ZNSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIxEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIxEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EE7destroyEv
- __ZNSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIxEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EED0Ev
- __ZNSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIxEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EED1Ev
- __ZNSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIxEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EEclEOS9_
- __ZNSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RbEUlbE_FvbEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RbEUlbE_FvbEE7destroyEv
- __ZNSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RbEUlbE_FvbEED0Ev
- __ZNSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RbEUlbE_FvbEED1Ev
- __ZNSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RbEUlbE_FvbEEclEOb
- __ZNSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RfEUldE_FvdEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RfEUldE_FvdEE7destroyEv
- __ZNSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RfEUldE_FvdEED0Ev
- __ZNSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RfEUldE_FvdEED1Ev
- __ZNSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RfEUldE_FvdEEclEOd
- __ZNSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RiEUlxE_FvxEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RiEUlxE_FvxEE7destroyEv
- __ZNSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RiEUlxE_FvxEED0Ev
- __ZNSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RiEUlxE_FvxEED1Ev
- __ZNSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RiEUlxE_FvxEEclEOx
- __ZNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERNS_10shared_ptrI11SynthOutputEEEUlvE_FvvEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERNS_10shared_ptrI11SynthOutputEEEUlvE_FvvEE7destroyEv
- __ZNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERNS_10shared_ptrI11SynthOutputEEEUlvE_FvvEED0Ev
- __ZNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERNS_10shared_ptrI11SynthOutputEEEUlvE_FvvEED1Ev
- __ZNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERNS_10shared_ptrI11SynthOutputEEEUlvE_FvvEEclEv
- __ZNSt3__110__list_impI15SystemSoundInfoNS_9allocatorIS1_EEE13__create_nodeB9nqe210106IJRKS1_EEEPNS_11__list_nodeIS1_PvEEPNS_16__list_node_baseIS1_S9_EESE_DpOT_
- __ZNSt3__110__list_impIN13ServerManager12SynthCommandEN5caulk12rt_allocatorIS2_EEE13__create_nodeB9nqe210106IJRKS2_EEEPNS_11__list_nodeIS2_PvEEPNS_16__list_node_baseIS2_SB_EESG_DpOT_
- __ZNSt3__110shared_ptrI11AQTapIONodeEC2B9nqe210106IS1_PFvP8AQIONodeELi0EEEPT_T0_
- __ZNSt3__110shared_ptrI11SynthOutputE18__enable_weak_thisB9nqe210106IS1_S1_Li0EEEvPKNS_23enable_shared_from_thisIT_EEPT0_
- __ZNSt3__110shared_ptrI14HapticSequenceEC2B9nqe210106IS1_Li0EEEPT_
- __ZNSt3__110shared_ptrI18AQMixEngine_SingleEC2B9nqe210106IS1_PFvP8AQIONodeELi0EEEPT_T0_
- __ZNSt3__110shared_ptrI19AQMixEngine_OfflineEC2B9nqe210106IS1_PFvP8AQIONodeELi0EEEPT_T0_
- __ZNSt3__110shared_ptrI21ThreadSafeHeadTrackerE18__enable_weak_thisB9nqe210106IS1_S1_Li0EEEvPKNS_23enable_shared_from_thisIT_EEPT0_
- __ZNSt3__110shared_ptrIN2AQ3API5QueueEEC2B9nqe210106IS3_Li0EEERKNS_8weak_ptrIT_EE
- __ZNSt3__110shared_ptrIN2AQ3API9SubmixTapEEC2B9nqe210106IS3_Li0EEERKNS_8weak_ptrIT_EE
- __ZNSt3__110shared_ptrIN2AT9IOBinding4ImplEE18__enable_weak_thisB9nqe210106IS3_S3_Li0EEEvPKNS_23enable_shared_from_thisIT_EEPT0_
- __ZNSt3__110unique_ptrI12CASerializerNS_14default_deleteIS1_EEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI14AQClientBufferN2AQ3API13BufferDeleterEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI14CADeserializerNS_14default_deleteIS1_EEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI14CAMemoryStreamNS_14default_deleteIS1_EEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI14InputConverterNS_14default_deleteIS1_EEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI14MixTapToUplinkNS_14default_deleteIS1_EEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI14__CFReadStreamN10applesauce4raii2v16detail23opaque_deletion_functorIPS1_XadL_Z9CFReleaseEEEEE5resetB9nqe210106ES7_
- __ZNSt3__110unique_ptrI16SSSVibrationDataNS_14default_deleteIS1_EEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI16SSSVibrationDataNS_14default_deleteIS1_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrI17AudioEventManagerNS_14default_deleteIS1_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrI17AudioTapInterfaceNS_14default_deleteIS1_EEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI17AudioTapSpecifierNS_14default_deleteIS1_EEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI18AudioRingAllocatorNS_14default_deleteIS1_EEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI18VADPropertyManagerNS_14default_deleteIS1_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrI19MESchedulingVectorsNS_14default_deleteIS1_EEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI20AudioImpulseInjectorNS_14default_deleteIS1_EEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI26SSClientCompletionProcInfoNS_14default_deleteIS1_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrI27SpatialTrackingServiceProxyNS_14default_deleteIS1_EEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI28OpaqueAudioComponentInstanceN10applesauce4raii2v16detail23opaque_deletion_functorIPS1_XadL_Z29AudioComponentInstanceDisposeEEEEE5resetB9nqe210106ES7_
- __ZNSt3__110unique_ptrI29ATSecureExternalDeviceManagerNS_14default_deleteIS1_EEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrI30ProductTuningAdjustmentManagerNS_14default_deleteIS1_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrI7__sFILENS_8functionIFiPS1_EEEE5resetB9nqe210106ES3_
- __ZNSt3__110unique_ptrI8XPromiseNS_14default_deleteIS1_EEE5resetB9nqe210106EPS1_
- __ZNSt3__110unique_ptrIKvN10applesauce4raii2v16detail23opaque_deletion_functorIPS1_XadL_Z9CFReleaseEEEEE5resetB9nqe210106ES7_
- __ZNSt3__110unique_ptrIN11AQMEIO_Base12IOSuspensionENS_14default_deleteIS2_EEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN11HeadTracker18HeadTrackerSessionENS_14default_deleteIS2_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrIN14MixTapToUplink16AQMETapConnectorENS_14default_deleteIS2_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrIN14MixTapToUplink27UplinkSpeechMixerCPPWrapperENS_14default_deleteIS2_EEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN14MixTapToUplink28AQIONodeClientForInternalTapENS_14default_deleteIS2_EEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN14MixTapToUplink41RAIIUnregisterMutedSpeechActivityListenerENS_14default_deleteIS2_EEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN14SpeechDetector18SpeechDetectorImplENS_14default_deleteIS2_EEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN17AudioTapInterface4ImplENS_14default_deleteIS2_EEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN18ATSecureVADManager4ImplENS_14default_deleteIS2_EEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN18MixTapToUplinkHost46MixTapToUplinkGroupedByMicrophoneInjectionModeENS_14default_deleteIS2_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrIN18PowerUsageWatchdog23AudioSessionDescriptionENS_14default_deleteIS2_EEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN18PowerUsageWatchdog4ImplENS_14default_deleteIS2_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrIN29ATSecureExternalDeviceManager4ImplENS_14default_deleteIS2_EEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN2AQ6Server12RemoteClientENS_14default_deleteIS3_EEE5resetB9nqe210106EPS3_
- __ZNSt3__110unique_ptrIN2AT11Translation14CallTranslatorENS_14default_deleteIS3_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrIN2AT11Translation19AUAsyncRendererHostENS_14default_deleteIS3_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrIN2AT11Translation24AudioTranslationInjectorENS_14default_deleteIS3_EEE5resetB9nqe210106EPS3_
- __ZNSt3__110unique_ptrIN2AT11Translation25BlurringMixerDSPGraphHost20ATBlurMixerInterfaceENS_14default_deleteIS4_EEE5resetB9nqe210106EPS4_
- __ZNSt3__110unique_ptrIN2AT11Translation25BlurringMixerDSPGraphHostENS_14default_deleteIS3_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrIN2AT11Translation27TranslationFeedbackInjectorENS_14default_deleteIS3_EEE5resetB9nqe210106EPS3_
- __ZNSt3__110unique_ptrIN2AT14AudioTapClient4ImplENS_14default_deleteIS3_EEE5resetB9nqe210106EPS3_
- __ZNSt3__110unique_ptrIN2CA16AudioBuffersBaseENS_14default_deleteIS2_EEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN2CA22AudioBuffersDeprecatedENS_14default_deleteIS2_EEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrIN5Phase13ServerManagerENS_14default_deleteIS2_EEE5resetB9nqe210106EPS2_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeI27AVHapticPlayerParameterTypeN20HapticEventConverter23CurveConsolidationStateEEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN20AudioImpulseInjector4Impl20NotificationListener17NotificationStateEEEPvEENS_22__hash_node_destructorINS6_ISF_EEEEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIPK15AudioBufferListNS_4pairINS_6chrono10time_pointINS7_12steady_clockENS7_8durationIxNS_5ratioILl1ELl1000000000EEEEEEEU8__strongP16AVAudioPCMBufferEEEEPvEENS_22__hash_node_destructorINS_9allocatorISL_EEEEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS0_I26SSClientCompletionProcInfoNS_14default_deleteIS3_EEEEEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE8LocalityEEPvEENS_22__tree_node_destructorINS6_ISC_EEEEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29NewNotificationCenterObserverEEEEPvEENS_22__tree_node_destructorINS6_ISE_EEEEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29OldNotificationCenterObserverEEEEPvEENS_22__tree_node_destructorINS6_ISE_EEEEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES8_EEPvEENS_22__tree_node_destructorINS6_ISB_EEEEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrINS_15__thread_structENS_14default_deleteIS1_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrINS_5tupleIJN5caulk6thread10attributesEZN2AQ3API20ProcessingTapManager7RTStateC1ERKN10applesauce3xpc6objectERNS6_23ProcessingTapAttributesERiE3$_0NS1_IJEEEEEENS_14default_deleteISJ_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrINS_5tupleIJNS0_INS_15__thread_structENS_14default_deleteIS2_EEEEZN2AQ3API5Queue7DestroyEvE3$_0EEENS3_ISA_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrIZN10applesauce8dispatch2v15asyncI14SystemListenerEEvNS_10shared_ptrIT_EEPU28objcproto17OS_dispatch_queue8NSObjectU13block_pointerFvvEEUlvE_NS_14default_deleteISE_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrIZN20CAOrientationManager14UpdateHandlersENS1_11HandlerTypeEE3$_0NS_14default_deleteIS3_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrIZN20CAOrientationManager23AddUIOrientationHandlerEPK10__CFStringU13block_pointerFv13CAOrientationEE3$_0NS_14default_deleteIS8_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrIZN20CAOrientationManager27AddDeviceOrientationHandlerEPK10__CFStringU13block_pointerFv13CAOrientationEE3$_0NS_14default_deleteIS8_EEED1B9nqe210106Ev
- __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZN17AudioTapSpecifierC1ENS_6vectorIjNS_9allocatorIjEEEE22ATAudioTapMuteBehaviorEUlRK11AQMESessionSA_E_PS8_Lb0EEEvT1_SE_T0_NS_15iterator_traitsISE_E15difference_typeEb
- __ZNSt3__111make_uniqueB9nqe210106I17AudioTapInterfaceJ17AudioTapSpecifierELi0EEENS_10unique_ptrIT_NS_14default_deleteIS4_EEEEDpOT0_
- __ZNSt3__111make_uniqueB9nqe210106I17AudioTapInterfaceJPK8__CFDataELi0EEENS_10unique_ptrIT_NS_14default_deleteIS6_EEEEDpOT0_
- __ZNSt3__111make_uniqueB9nqe210106IN2CA22AudioBuffersDeprecatedEJRNS1_17StreamDescriptionERjELi0EEENS_10unique_ptrIT_NS_14default_deleteIS7_EEEEDpOT0_
- __ZNSt3__111scoped_lockIJN5caulk4mach21unfair_recursive_lockEN16AudioQueueObject20WorkQueueLockAdapterEEE15__unlock_unpackB9nqe210106IJLm0ELm1EEEEvNS_15__tuple_indicesIJXspT_EEEERNS_5tupleIJRS3_RS5_EEE
- __ZNSt3__111scoped_lockIJN5caulk4mach21unfair_recursive_lockENS1_23recursive_mutex_adapterINS1_22pooled_semaphore_mutexEEES3_EE15__unlock_unpackB9nqe210106IJLm0ELm1ELm2EEEEvNS_15__tuple_indicesIJXspT_EEEERNS_5tupleIJRS3_RS6_SC_EEE
- __ZNSt3__111scoped_lockIJN5caulk4mach21unfair_recursive_lockENS1_23recursive_mutex_adapterINS1_22pooled_semaphore_mutexEEES3_N16AudioQueueObject20WorkQueueLockAdapterEEE15__unlock_unpackB9nqe210106IJLm0ELm1ELm2ELm3EEEEvNS_15__tuple_indicesIJXspT_EEEERNS_5tupleIJRS3_RS6_SE_RS8_EEE
- __ZNSt3__111shared_lockIN5caulk10concurrent16shared_spin_lockEED2B9nqe210106Ev
- __ZNSt3__111shared_lockINS_12shared_mutexEED2B9nqe210106Ev
- __ZNSt3__111unique_lockIN5caulk10concurrent16shared_spin_lockEED2B9nqe210106Ev
- __ZNSt3__111unique_lockIN5caulk4mach21unfair_recursive_lockEE4lockB9nqe210106Ev
- __ZNSt3__111unique_lockIN5caulk4mach21unfair_recursive_lockEE6unlockB9nqe210106Ev
- __ZNSt3__111unique_lockINS_12shared_mutexEED2B9nqe210106Ev
- __ZNSt3__112__destroy_atB9nqe210106I15MEVADIdentifierLi0EEEvPT_
- __ZNSt3__112__destroy_atB9nqe210106IN10applesauce2CF7TypeRefELi0EEEvPT_
- __ZNSt3__112__destroy_atB9nqe210106IN10applesauce2CF9NumberRefELi0EEEvPT_
- __ZNSt3__112__destroy_atB9nqe210106IN2AQ6Server12RemoteClient18ProcessingTapStateELi0EEEvPT_
- __ZNSt3__112__destroy_atB9nqe210106IN2AU8Property10Attributes7details15AUPresetWrapperELi0EEEvPT_
- __ZNSt3__112__destroy_atB9nqe210106IN8audioipc18SharedAudioBuffers7ElementELi0EEEvPT_
- __ZNSt3__112__destroy_atB9nqe210106INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE8LocalityEELi0EEEvPT_
- __ZNSt3__112__destroy_atB9nqe210106INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29NewNotificationCenterObserverEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB9nqe210106INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29OldNotificationCenterObserverEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB9nqe210106INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EELi0EEEvPT_
- __ZNSt3__112__destroy_atB9nqe210106INS_4pairIKP14MEMixerChannelN9TapSubmix10InputStateEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB9nqe210106INS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EELi0EEEvPT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI20HapticPlayerPriorityjEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_jEENS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S7_SB_S9_Lb1EEENS_9allocatorIS7_EEE25__emplace_unique_key_argsIS2_JRKNS_21piecewise_construct_tENS_5tupleIJOS2_EEENSM_IJEEEEEENS5_INS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI20HapticPlayerPriorityjEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_jEENS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S7_SB_S9_Lb1EEENS_9allocatorIS7_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI20HapticPlayerPriorityjEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_jEENS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S7_SB_S9_Lb1EEENS_9allocatorIS7_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI27AVHapticPlayerParameterTypeN20HapticEventConverter23CurveConsolidationStateEEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S4_EENS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S9_SD_SB_Lb1EEENS_9allocatorIS9_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE26STSPerLabelControllerStateEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_S8_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SD_SH_SF_Lb1EEENS5_ISD_EEE4findIS7_EENS_15__hash_iteratorIPNS_11__hash_nodeIS9_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE26STSPerLabelControllerStateEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_S8_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SD_SH_SF_Lb1EEENS5_ISD_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE26STSPerLabelControllerStateEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_S8_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SD_SH_SF_Lb1EEENS5_ISD_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN20AudioImpulseInjector4Impl20NotificationListener17NotificationStateEEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_SB_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SG_SK_SI_Lb1EEENS5_ISG_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJRSF_EEENSU_IJEEEEEENSE_INS_15__hash_iteratorIPNS_11__hash_nodeISC_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN20AudioImpulseInjector4Impl20NotificationListener17NotificationStateEEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_SB_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SG_SK_SI_Lb1EEENS5_ISG_EEE4findIS7_EENS_15__hash_iteratorIPNS_11__hash_nodeISC_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_bEENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SC_SG_SE_Lb1EEENS5_ISC_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJRSB_EEENSQ_IJEEEEEENSA_INS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_bEENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SC_SG_SE_Lb1EEENS5_ISC_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_4pairImN18PowerUsageWatchdog13ClientRunModeEEENS_10shared_ptrINS3_17ClientDescriptionEEEEENS_22__unordered_map_hasherIS5_NS2_IKS5_S8_EENS3_4Impl9pair_hashENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_SC_SG_SE_Lb1EEENS_9allocatorISC_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS9_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_4pairImN18PowerUsageWatchdog13ClientRunModeEEENS_10shared_ptrINS3_17ClientDescriptionEEEEENS_22__unordered_map_hasherIS5_NS2_IKS5_S8_EENS3_4Impl9pair_hashENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_SC_SG_SE_Lb1EEENS_9allocatorISC_EEE19__node_insert_multiEPNS_11__hash_nodeIS9_PvEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_4pairImN18PowerUsageWatchdog13ClientRunModeEEENS_10shared_ptrINS3_17ClientDescriptionEEEEENS_22__unordered_map_hasherIS5_NS2_IKS5_S8_EENS3_4Impl9pair_hashENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_SC_SG_SE_Lb1EEENS_9allocatorISC_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_4pairImN18PowerUsageWatchdog13ClientRunModeEEENS_10shared_ptrINS3_17ClientDescriptionEEEEENS_22__unordered_map_hasherIS5_NS2_IKS5_S8_EENS3_4Impl9pair_hashENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_SC_SG_SE_Lb1EEENS_9allocatorISC_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPK15AudioBufferListNS_4pairINS_6chrono10time_pointINS6_12steady_clockENS6_8durationIxNS_5ratioILl1ELl1000000000EEEEEEEU8__strongP16AVAudioPCMBufferEEEENS_22__unordered_map_hasherIS4_NS5_IKS4_SH_EENS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_SL_SP_SN_Lb1EEENS_9allocatorISL_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPK15AudioBufferListNS_4pairINS_6chrono10time_pointINS6_12steady_clockENS6_8durationIxNS_5ratioILl1ELl1000000000EEEEEEEU8__strongP16AVAudioPCMBufferEEEENS_22__unordered_map_hasherIS4_NS5_IKS4_SH_EENS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_SL_SP_SN_Lb1EEENS_9allocatorISL_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPvN10applesauce8dispatch2v15blockIFv28AUVoiceIOSpeechActivityEventEEEEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S9_EENS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_SE_SI_SG_Lb1EEENS_9allocatorISE_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeISA_S2_EEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPvN10applesauce8dispatch2v15blockIFv28AUVoiceIOSpeechActivityEventEEEEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S9_EENS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_SE_SI_SG_Lb1EEENS_9allocatorISE_EEE4findIS2_EENS_15__hash_iteratorIPNS_11__hash_nodeISA_S2_EEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPvN10applesauce8dispatch2v15blockIFv28AUVoiceIOSpeechActivityEventEEEEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S9_EENS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_SE_SI_SG_Lb1EEENS_9allocatorISE_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeISA_S2_EEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPvN10applesauce8dispatch2v15blockIFv28AUVoiceIOSpeechActivityEventEEEEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S9_EENS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_SE_SI_SG_Lb1EEENS_9allocatorISE_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIijEENS_22__unordered_map_hasherIiNS_4pairIKijEENS_4hashIiEENS_8equal_toIiEELb1EEENS_21__unordered_map_equalIiS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE15__emplace_multiIJNS4_IijEEEEENS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEDpOT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIijEENS_22__unordered_map_hasherIiNS_4pairIKijEENS_4hashIiEENS_8equal_toIiEELb1EEENS_21__unordered_map_equalIiS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE19__equal_range_multiIiEENS4_INS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEESN_EERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIijEENS_22__unordered_map_hasherIiNS_4pairIKijEENS_4hashIiEENS_8equal_toIiEELb1EEENS_21__unordered_map_equalIiS6_SA_S8_Lb1EEENS_9allocatorIS6_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_10unique_ptrI26SSClientCompletionProcInfoNS_14default_deleteIS3_EEEEEENS_22__unordered_map_hasherIjNS_4pairIKjS6_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjSB_SF_SD_Lb1EEENS_9allocatorISB_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_13unordered_setIPvNS_4hashIS3_EENS_8equal_toIS3_EENS_9allocatorIS3_EEEEEENS_22__unordered_map_hasherIjNS_4pairIKjSA_EENS4_IjEENS6_IjEELb1EEENS_21__unordered_map_equalIjSF_SH_SG_Lb1EEENS8_ISF_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeISB_S3_EEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_4pairIjxEEEENS_22__unordered_map_hasherIjNS2_IKjS3_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SB_S9_Lb1EEENS_9allocatorIS7_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_6vectorIhNS_9allocatorIhEEEEEENS_22__unordered_map_hasherIjNS_4pairIKjS5_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjSA_SE_SC_Lb1EEENS3_ISA_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRS9_EEENSO_IJEEEEEENS8_INS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_6vectorIhNS_9allocatorIhEEEEEENS_22__unordered_map_hasherIjNS_4pairIKjS5_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjSA_SE_SC_Lb1EEENS3_ISA_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjP24OpaqueMusicEventIteratorEENS_22__unordered_map_hasherIjNS_4pairIKjS3_EENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS8_SC_SA_Lb1EEENS_9allocatorIS8_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjiEENS_22__unordered_map_hasherIjNS_4pairIKjiEENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRS5_EEENSL_IJEEEEEENS4_INS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjiEENS_22__unordered_map_hasherIjNS_4pairIKjiEENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjiEENS_22__unordered_map_hasherIjNS_4pairIKjiEENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SA_S8_Lb1EEENS_9allocatorIS6_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImNS_10shared_ptrI14HapticSequenceEEEENS_22__unordered_map_hasherImNS_4pairIKmS4_EENS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS5_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImNS_10shared_ptrI14HapticSequenceEEEENS_22__unordered_map_hasherImNS_4pairIKmS4_EENS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE4findImEENS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImNS_10shared_ptrI14HapticSequenceEEEENS_22__unordered_map_hasherImNS_4pairIKmS4_EENS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS9_SD_SB_Lb1EEENS_9allocatorIS9_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImNS_8optionalI28AUVoiceIOSpeechActivityEventEEEENS_22__unordered_map_hasherImNS_4pairIKmS4_EENS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE4findImEENS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImU13block_pointerFv28AUVoiceIOSpeechActivityEventEEENS_22__unordered_map_hasherImNS_4pairIKmS4_EENS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE25__emplace_unique_key_argsImJRKNS_21piecewise_construct_tENS_5tupleIJRS8_EEENSO_IJEEEEEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImU13block_pointerFv28AUVoiceIOSpeechActivityEventEEENS_22__unordered_map_hasherImNS_4pairIKmS4_EENS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE4findImEENS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImbEENS_22__unordered_map_hasherImNS_4pairIKmbEENS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS6_SA_S8_Lb1EEEN5caulk12rt_allocatorIS6_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS2_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImbEENS_22__unordered_map_hasherImNS_4pairIKmbEENS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS6_SA_S8_Lb1EEEN5caulk12rt_allocatorIS6_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS2_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImbEENS_22__unordered_map_hasherImNS_4pairIKmbEENS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS6_SA_S8_Lb1EEEN5caulk12rt_allocatorIS6_EEED2Ev
- __ZNSt3__112__hash_tableIPN20AudioImpulseInjector4ImplENS_4hashIS3_EENS_8equal_toIS3_EENS_9allocatorIS3_EEE25__emplace_unique_key_argsIS3_JRKS3_EEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableIPvNS_4hashIS1_EENS_8equal_toIS1_EENS_9allocatorIS1_EEE25__emplace_unique_key_argsIS1_JRKS1_EEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS1_S1_EEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableIPvNS_4hashIS1_EENS_8equal_toIS1_EENS_9allocatorIS1_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEE25__emplace_unique_key_argsIjJRKjEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIjPvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEE8__rehashILb1EEEvm
- __ZNSt3__112__tuple_implINS_15__tuple_indicesIJLm0ELm1ELm2EEEEJN10applesauce3xpc6objectEN4swix6stringEjEEC2EOS8_
- __ZNSt3__112__tuple_implINS_15__tuple_indicesIJLm0ELm1ELm2ELm3ELm4EEEEJN10applesauce3xpc6objectEjjbNS_6vectorIjNS_9allocatorIjEEEEEEC2EOSA_
- __ZNSt3__112__tuple_implINS_15__tuple_indicesIJLm0ELm1ELm2ELm3ELm4EEEEJN10applesauce3xpc6objectEjjbNS_6vectorIjNS_9allocatorIjEEEEEEC2ERKSA_
- __ZNSt3__112__tuple_implINS_15__tuple_indicesIJLm0ELm1ELm2ELm3ELm4ELm5EEEEJjj27AudioStreamBasicDescriptionN10applesauce3xpc6objectES6_N2CA13ChannelLayoutEEEC2EOS9_
- __ZNSt3__112__tuple_implINS_15__tuple_indicesIJLm0ELm1ELm2ELm3ELm4ELm5EEEEJjj27AudioStreamBasicDescriptionN10applesauce3xpc6objectES6_N2CA13ChannelLayoutEEEC2ERKS9_
- __ZNSt3__112__tuple_leafILm0EN10applesauce3xpc6objectELb0EEC2B9nqe210106ERKS4_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_out_of_rangeB9nqe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106EPKcm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106Emc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106ILi0EEEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106INS_17basic_string_viewIcS2_EELi0EEERKT_
- __ZNSt3__112construct_atB9nqe210106I11AQMESessionJS1_EPS1_EEPT_S4_DpOT0_
- __ZNSt3__112construct_atB9nqe210106I15MEVADIdentifierJR14MEDeviceTypeIDRjRN10applesauce2CF9StringRefEEPS1_EEPT_SB_DpOT0_
- __ZNSt3__112construct_atB9nqe210106I15MEVADIdentifierJRS1_EPS1_EEPT_S5_DpOT0_
- __ZNSt3__112construct_atB9nqe210106IN10applesauce2CF9StringRefEJRKS3_EPS3_EEPT_S8_DpOT0_
- __ZNSt3__113__fill_n_boolB9nqe210106ILb0ENS_8__bitsetILm1ELm13EEEEEvNS_14__bit_iteratorIT0_Lb0EXLi0EEEENS_29__size_difference_type_traitsIS4_vE9size_typeE
- __ZNSt3__113__tree_removeB9nqe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__113unordered_mapIPvN10applesauce8dispatch2v15blockIFv28AUVoiceIOSpeechActivityEventEEENS_4hashIS1_EENS_8equal_toIS1_EENS_9allocatorINS_4pairIKS1_S8_EEEEE16insert_or_assignB9nqe210106IRU8__strongU13block_pointerS7_EENSE_INS_19__hash_map_iteratorINS_15__hash_iteratorIPNS_11__hash_nodeINS_17__hash_value_typeIS1_S8_EES1_EEEEEEbEERSF_OT_
- __ZNSt3__113unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEC2ERKS7_
- __ZNSt3__114__split_bufferINS_8weak_ptrI25AQMEIO_NotificationClientEERNS_9allocatorIS3_EEED2Ev
- __ZNSt3__114__thread_proxyB9nqe210106INS_5tupleIJNS_10unique_ptrINS_15__thread_structENS_14default_deleteIS3_EEEEZN2AQ3API5Queue7DestroyEvE3$_0EEEEEPvSC_
- __ZNSt3__115allocate_sharedB9nqe210106I11SynthOutputNS_9allocatorIS1_EEJR17LegacyHapticSynthbELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB9nqe210106I14HapticSequenceNS_9allocatorIS1_EEJNS_10shared_ptrI11MuteManagerEEELi0EEENS4_IT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB9nqe210106I19SSClientPlayOptionsNS_9allocatorIS1_EEJRN10applesauce3xpc6objectEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB9nqe210106I8TFileBSDNS_9allocatorIS1_EEJRPK7__CFURLELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB9nqe210106IN2AQ3API9SubmixTapENS_9allocatorIS3_EEJRNS2_7ManagerERjELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB9nqe210106IN2AT9IOBinding4ImplENS_9allocatorIS3_EEJN10applesauce2CF9StringRefEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB9nqe210106IN2AT9IOBinding4ImplENS_9allocatorIS3_EEJR24ATIsolatedAudioUseCaseIDELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB9nqe210106IN5caulk7details19lifetime_guard_baseIN2AQ6Server12RemoteClientEE13control_blockENS_9allocatorIS8_EEJRS7_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B9nqe210106Ej
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB9nqe210106IOZNS0_6__ctorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEEE19__generic_constructB9nqe210106IRKNS0_18__copy_constructorISV_LNS0_6_TraitE1EEEEEvRSW_OT_EUlS15_E_JRKNS0_6__baseILSZ_1EJSE_SM_SS_SU_EEEEEEDcS14_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB9nqe210106IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN15AQProcessingTap10DirectImplEEEELNS0_6_TraitE1EE9__destroyB9nqe210106EvEUlRT_E_JRNS0_6__baseILSC_1EJS8_SA_EEEEEEDcSE_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB9nqe210106IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AQ6Server11XPCListenerENSA_9IPCBypassEEEELNS0_6_TraitE1EE9__destroyB9nqe210106EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB9nqe210106IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AT13SessionFacade7ManagerENSA_11ManagerBaseEEEELNS0_6_TraitE1EE9__destroyB9nqe210106EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB9nqe210106IOZNS0_6__dtorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEELNS0_6_TraitE1EE9__destroyB9nqe210106EvEUlRT_E_JRNS0_6__baseILSW_1EJSE_SM_SS_SU_EEEEEEDcSY_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB9nqe210106IOZNS0_6__ctorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEEE19__generic_constructB9nqe210106IRKNS0_18__copy_constructorISV_LNS0_6_TraitE1EEEEEvRSW_OT_EUlS15_E_JRKNS0_6__baseILSZ_1EJSE_SM_SS_SU_EEEEEEDcS14_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB9nqe210106IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN15AQProcessingTap10DirectImplEEEELNS0_6_TraitE1EE9__destroyB9nqe210106EvEUlRT_E_JRNS0_6__baseILSC_1EJS8_SA_EEEEEEDcSE_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB9nqe210106IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AQ6Server11XPCListenerENSA_9IPCBypassEEEELNS0_6_TraitE1EE9__destroyB9nqe210106EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB9nqe210106IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AT13SessionFacade7ManagerENSA_11ManagerBaseEEEELNS0_6_TraitE1EE9__destroyB9nqe210106EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB9nqe210106IOZNS0_6__dtorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEELNS0_6_TraitE1EE9__destroyB9nqe210106EvEUlRT_E_JRNS0_6__baseILSW_1EJSE_SM_SS_SU_EEEEEEDcSY_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB9nqe210106IOZNS0_6__ctorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEEE19__generic_constructB9nqe210106IRKNS0_18__copy_constructorISV_LNS0_6_TraitE1EEEEEvRSW_OT_EUlS15_E_JRKNS0_6__baseILSZ_1EJSE_SM_SS_SU_EEEEEEDcS14_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB9nqe210106IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AQ6Server11XPCListenerENSA_9IPCBypassEEEELNS0_6_TraitE1EE9__destroyB9nqe210106EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB9nqe210106IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AT13SessionFacade7ManagerENSA_11ManagerBaseEEEELNS0_6_TraitE1EE9__destroyB9nqe210106EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB9nqe210106IOZNS0_6__dtorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEELNS0_6_TraitE1EE9__destroyB9nqe210106EvEUlRT_E_JRNS0_6__baseILSW_1EJSE_SM_SS_SU_EEEEEEDcSY_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB9nqe210106IOZNS0_6__ctorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEEE19__generic_constructB9nqe210106IRKNS0_18__copy_constructorISV_LNS0_6_TraitE1EEEEEvRSW_OT_EUlS15_E_JRKNS0_6__baseILSZ_1EJSE_SM_SS_SU_EEEEEEDcS14_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB9nqe210106IOZNS0_6__dtorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEELNS0_6_TraitE1EE9__destroyB9nqe210106EvEUlRT_E_JRNS0_6__baseILSW_1EJSE_SM_SS_SU_EEEEEEDcSY_DpT0_
- __ZNSt3__116__variant_detail18__copy_constructorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS3_S5_S7_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvS5_S7_EEENSL_IFvS5_S7_SC_jSF_EEEEEELNS0_6_TraitE1EEC2B9nqe210106ERKSS_
- __ZNSt3__116__variant_detail6__dtorINS0_8__traitsIJNS_9monostateEN15AQProcessingTap10DirectImplEEEELNS0_6_TraitE1EE9__destroyB9nqe210106Ev
- __ZNSt3__116__variant_detail6__dtorINS0_8__traitsIJNS_9monostateEN2AQ6Server11XPCListenerENS5_9IPCBypassEEEELNS0_6_TraitE1EE9__destroyB9nqe210106Ev
- __ZNSt3__116__variant_detail6__dtorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS3_S5_S7_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvS5_S7_EEENSL_IFvS5_S7_SC_jSF_EEEEEELNS0_6_TraitE1EE9__destroyB9nqe210106Ev
- __ZNSt3__116allocator_traitsIN5caulk12rt_allocatorI11VolumeEventEEE17allocate_at_leastB9nqe210106IS4_EENS_17allocation_resultIPS3_mEERT_m
- __ZNSt3__116allocator_traitsIN5caulk12rt_allocatorINS_4pairIPFiPvPjPK14AudioTimeStampjjP15AudioBufferListES4_EEEEE17allocate_at_leastB9nqe210106ISE_EENS_17allocation_resultIPSD_mEERT_m
- __ZNSt3__116allocator_traitsIN5caulk12rt_allocatorINS_4pairIffEEEEE17allocate_at_leastB9nqe210106IS5_EENS_17allocation_resultIPS4_mEERT_m
- __ZNSt3__116allocator_traitsINS_9allocatorI11AQMESessionEEE7destroyB9nqe210106IS2_Li0EEEvRS3_PT_
- __ZNSt3__116allocator_traitsINS_9allocatorI15MEVADIdentifierEEE9constructB9nqe210106IS2_J14MEDeviceTypeID3$_1RPK10__CFStringELi0EEEvRS3_PT_DpOT0_
- __ZNSt3__116allocator_traitsINS_9allocatorI9TapSourceEEE7destroyB9nqe210106IS2_Li0EEEvRS3_PT_
- __ZNSt3__116allocator_traitsINS_9allocatorI9TapSourceEEE9constructB9nqe210106IS2_JS2_ELi0EEEvRS3_PT_DpOT0_
- __ZNSt3__116allocator_traitsINS_9allocatorIN10applesauce2CF11TypeRefPairEEEE7destroyB9nqe210106IS4_Li0EEEvRS5_PT_
- __ZNSt3__116allocator_traitsINS_9allocatorIN10applesauce2CF11TypeRefPairEEEE9constructB9nqe210106IS4_JRKNS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEERKNS3_7TypeRefEELi0EEEvRS5_PT_DpOT0_
- __ZNSt3__116allocator_traitsINS_9allocatorIN10applesauce2CF7TypeRefEEEE9constructB9nqe210106IS4_JdELi0EEEvRS5_PT_DpOT0_
- __ZNSt3__116allocator_traitsINS_9allocatorIN10applesauce2CF9NumberRefEEEE9constructB9nqe210106IS4_JjELi0EEEvRS5_PT_DpOT0_
- __ZNSt3__116allocator_traitsINS_9allocatorIN21IPCAUSharedMemoryBase7ElementEEEE7destroyB9nqe210106IS3_Li0EEEvRS4_PT_
- __ZNSt3__116allocator_traitsINS_9allocatorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEEEEE7destroyB9nqe210106ISD_Li0EEEvRSE_PT_
- __ZNSt3__116allocator_traitsINS_9allocatorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEEEEE9constructB9nqe210106ISD_JSD_ELi0EEEvRSE_PT_DpOT0_
- __ZNSt3__117__call_once_proxyB9nqe210106INS_5tupleIJOZ31SetupSystemSoundClientLogScopesvE3$_0EEEEEvPv
- __ZNSt3__117__call_once_proxyB9nqe210106INS_5tupleIJOZL12logSubsystemvE3$_0EEEEEvPv
- __ZNSt3__117__call_once_proxyB9nqe210106INS_5tupleIJOZN11AQAC3IONodeC1ERK14AQMEIO_Binding14MEStreamTypeIDRidE3$_0EEEEEvPv
- __ZNSt3__117__call_once_proxyB9nqe210106INS_5tupleIJOZN11SSServerIPCC1EvE3$_0EEEEEvPv
- __ZNSt3__117__call_once_proxyB9nqe210106INS_5tupleIJOZN12CADeprecated10TSingletonI11SSClientIPCE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB9nqe210106INS_5tupleIJOZN12CADeprecated10TSingletonI13HapticMetricsE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB9nqe210106INS_5tupleIJOZN12CADeprecated10TSingletonI14RemoteIOServerE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB9nqe210106INS_5tupleIJOZN12CADeprecated10TSingletonI15ActiveSoundListE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB9nqe210106INS_5tupleIJOZN12CADeprecated10TSingletonI18SSClientCompletionE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB9nqe210106INS_5tupleIJOZN12CADeprecated10TSingletonI19HapticServerManagerE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB9nqe210106INS_5tupleIJOZN12CADeprecated10TSingletonI20SSSCallbackMessengerE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB9nqe210106INS_5tupleIJOZN12CADeprecated10TSingletonI21CAExternalLockJanitorE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB9nqe210106INS_5tupleIJOZN12CADeprecated10TSingletonI8SSServerE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB9nqe210106INS_5tupleIJOZN12CADeprecated10TSingletonIN12_GLOBAL__N_118CoreMotionSoftlinkEE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB9nqe210106INS_5tupleIJOZN12CADeprecated10TSingletonIN15CAListenerProxy13ZombieJanitorEE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB9nqe210106INS_5tupleIJOZN12CADeprecated10TSingletonIN20AudioImpulseInjector4Impl20NotificationListenerEE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB9nqe210106INS_5tupleIJOZN18AQOfflineMixerBaseC1ER15AQIONodeManageriRK27AudioStreamBasicDescriptionRKN2CA13ChannelLayoutERiE3$_0EEEEEvPv
- __ZNSt3__117__call_once_proxyB9nqe210106INS_5tupleIJOZN20CA_UISoundClientBaseC1EdjPK14__CFDictionaryjN10applesauce2CF7TypeRefEibE3$_0EEEEEvPv
- __ZNSt3__118__set_intersectionB9nqe210106INS_17_ClassicAlgPolicyENS_6__lessIvvEENS_21__hash_const_iteratorIPNS_11__hash_nodeIjPvEEEES9_S9_S9_NS_20back_insert_iteratorINS_6vectorIjNS_9allocatorIjEEEEEEEENS_25__set_intersection_resultIT1_T3_T5_EESH_T2_SI_T4_SJ_OT0_NS_20forward_iterator_tagESP_
- __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106Ev
- __ZNSt3__119__shared_mutex_base11lock_sharedEv
- __ZNSt3__119__shared_mutex_base13unlock_sharedEv
- __ZNSt3__119__shared_mutex_base4lockEv
- __ZNSt3__119__shared_mutex_base6unlockEv
- __ZNSt3__119__shared_mutex_base8try_lockEv
- __ZNSt3__119__shared_mutex_baseC1Ev
- __ZNSt3__119__shared_weak_count16__release_sharedB9nqe210106Ev
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106Ev
- __ZNSt3__120__optional_copy_baseIN2CA13ChannelLayoutELb0EEC2B9nqe210106ERKS3_
- __ZNSt3__120__optional_copy_baseIN4swix14timeout_configELb0EEC2B9nqe210106ERKS3_
- __ZNSt3__120__optional_copy_baseINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEELb0EEC2B9nqe210106ERKS7_
- __ZNSt3__120__shared_ptr_pointerIP14HapticSequenceNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_pointerIP14HapticSequenceNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_pointerIP14HapticSequenceNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEED0Ev
- __ZNSt3__120__shared_ptr_pointerIP14HapticSequenceNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEED1Ev
- __ZNSt3__120__throw_bad_weak_ptrB9nqe210106Ev
- __ZNSt3__120__throw_future_errorB9nqe210106ENS_11future_errcE
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- __ZNSt3__120__throw_out_of_rangeB9nqe210106EPKc
- __ZNSt3__121__concatenate_stringsB9nqe210106IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS8_NS_15__type_identityINS_17basic_string_viewIS6_S7_EEE4typeESG_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPvEEEEEclB9nqe210106EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE26STSPerLabelControllerStateEEPvEEEEEclB9nqe210106EPSC_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEbEEPvEEEEEclB9nqe210106EPSB_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_4pairImN18PowerUsageWatchdog13ClientRunModeEEENS_10shared_ptrINS5_17ClientDescriptionEEEEEPvEEEEEclB9nqe210106EPSD_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIPvN10applesauce8dispatch2v15blockIFv28AUVoiceIOSpeechActivityEventEEEEES4_EEEEEclB9nqe210106EPSD_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIjNS_10unique_ptrI27SSClientCompletionBlockInfoNS_14default_deleteIS5_EEEEEEPvEEEEEclB9nqe210106EPSB_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIjNS_6vectorIhNS1_IhEEEEEEPvEEEEEclB9nqe210106EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeImNS_10shared_ptrI14HapticSequenceEEEEPvEEEEEclB9nqe210106EPS9_
- __ZNSt3__122__lower_bound_onesidedB9nqe210106INS_17_ClassicAlgPolicyENS_21__hash_const_iteratorIPNS_11__hash_nodeIjPvEEEES7_jKNS_10__identityENS_6__lessIvvEEEET0_SC_T1_RKT2_RT4_RT3_
- __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEN10applesauce2CF7TypeRefEEEPvEEEEEclB9nqe210106EPSE_
- __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPK14__CFDictionaryEEPvEEEEEclB9nqe210106EPSE_
- __ZNSt3__123__optional_storage_baseI14AQMEIO_BindingLb0EE13__assign_fromB9nqe210106IRKNS_27__optional_copy_assign_baseIS1_Lb0EEEEEvOT_
- __ZNSt3__123__optional_storage_baseIN10applesauce2CF9StringRefELb0EE13__assign_fromB9nqe210106INS_27__optional_move_assign_baseIS3_Lb0EEEEEvOT_
- __ZNSt3__123__optional_storage_baseIN10applesauce2CF9StringRefELb0EE13__assign_fromB9nqe210106IRKNS_27__optional_copy_assign_baseIS3_Lb0EEEEEvOT_
- __ZNSt3__123__optional_storage_baseIN2AT9IOBindingELb0EE13__assign_fromB9nqe210106IRKNS_27__optional_copy_assign_baseIS2_Lb0EEEEEvOT_
- __ZNSt3__123__optional_storage_baseIN2CA13ChannelLayoutELb0EE13__assign_fromB9nqe210106INS_27__optional_move_assign_baseIS2_Lb0EEEEEvOT_
- __ZNSt3__123mersenne_twister_engineIjLm32ELm624ELm397ELm31ELj2567483615ELm11ELj4294967295ELm7ELj2636928640ELm15ELj4022730752ELm18ELj1812433253EEclEv
- __ZNSt3__124__optional_destruct_baseIN2CA16AudioBuffersBaseELb0EE5resetB9nqe210106Ev
- __ZNSt3__124__optional_destruct_baseIN5caulk5alloc23guarded_edges_allocatorINS2_16tiered_allocatorIJNS2_15size_range_tierILm0ELm409599ENS2_22consolidating_free_mapIN2AQ19SharedPageAllocatorELm10485760EEEEENS2_18tracking_allocatorIS8_EEEEELm2EEELb0EE5resetB9nqe210106Ev
- __ZNSt3__124__optional_destruct_baseIN9TapSubmix10InputState14BufferingStateELb0EE5resetB9nqe210106Ev
- __ZNSt3__124__put_character_sequenceB9nqe210106IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__125__bucket_list_deallocatorIN5caulk12rt_allocatorIPNS_16__hash_node_baseIPNS_11__hash_nodeINS_17__hash_value_typeImbEEPvEEEEEEEclB9nqe210106EPSB_
- __ZNSt3__125__throw_bad_function_callB9nqe210106Ev
- __ZNSt3__126__throw_bad_variant_accessB9nqe210106Ev
- __ZNSt3__127__insertion_sort_incompleteB9nqe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP10MusicEventEEbT1_S7_T0_
- __ZNSt3__127__insertion_sort_incompleteB9nqe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP11VolumeEventEEbT1_S7_T0_
- __ZNSt3__127__insertion_sort_incompleteB9nqe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP15MEVADIdentifierEEbT1_S7_T0_
- __ZNSt3__127__insertion_sort_incompleteB9nqe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN14NoteOffManager11NoteOffInfoEEEbT1_S8_T0_
- __ZNSt3__127__insertion_sort_incompleteB9nqe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEbT1_SC_T0_
- __ZNSt3__127__insertion_sort_incompleteB9nqe210106INS_17_ClassicAlgPolicyERZN17AudioTapSpecifierC1ENS_6vectorIjNS_9allocatorIjEEEE22ATAudioTapMuteBehaviorEUlRK11AQMESessionSA_E_PS8_EEbT1_SE_T0_
- __ZNSt3__127__insertion_sort_incompleteB9nqe210106INS_17_ClassicAlgPolicyERZZZN2AT11Translation19AUAsyncRendererHost9ConfigureEvENK3$_0clENS_6chrono10time_pointINS6_12steady_clockENS6_8durationIxNS_5ratioILl1ELl1000000000EEEEEEERK15AudioBufferListiENKUlRT_E_clINS_6vectorINS4_34TemporallyOrdereredAudioBufferListENS_9allocatorISM_EEEEEEDaSI_EUlRKSM_SS_E_PSM_EEbT1_SW_T0_
- __ZNSt3__127__throw_bad_optional_accessB9nqe210106Ev
- __ZNSt3__127__tree_balance_after_insertB9nqe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__134__uninitialized_allocator_relocateB9nqe210106INS_9allocatorI10MusicEventEEPS2_EEvRT_T0_S7_S7_
- __ZNSt3__134__uninitialized_allocator_relocateB9nqe210106INS_9allocatorI11AQMESessionEEPS2_EEvRT_T0_S7_S7_
- __ZNSt3__134__uninitialized_allocator_relocateB9nqe210106INS_9allocatorI9TapSourceEEPS2_EEvRT_T0_S7_S7_
- __ZNSt3__134__uninitialized_allocator_relocateB9nqe210106INS_9allocatorIN10applesauce2CF11TypeRefPairEEEPS4_EEvRT_T0_S9_S9_
- __ZNSt3__134__uninitialized_allocator_relocateB9nqe210106INS_9allocatorIN8InfoList9InfoEntryEEEPS3_EEvRT_T0_S8_S8_
- __ZNSt3__134__uninitialized_allocator_relocateB9nqe210106INS_9allocatorIN8audioipc18SharedAudioBuffers7ElementEEEPS4_EEvRT_T0_S9_S9_
- __ZNSt3__134__uninitialized_allocator_relocateB9nqe210106INS_9allocatorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEEEEPSD_EEvRT_T0_SI_SI_
- __ZNSt3__135__uninitialized_allocator_copy_implB9nqe210106INS_9allocatorI10MusicEventEEPS2_S4_S4_EET2_RT_T0_T1_S5_
- __ZNSt3__135__uninitialized_allocator_copy_implB9nqe210106INS_9allocatorI11AQMESessionEEPKS2_S5_PS2_EET2_RT_T0_T1_S7_
- __ZNSt3__135__uninitialized_allocator_copy_implB9nqe210106INS_9allocatorI11AQMESessionEEPS2_S4_S4_EET2_RT_T0_T1_S5_
- __ZNSt3__135__uninitialized_allocator_copy_implB9nqe210106INS_9allocatorINS_10shared_ptrI9TapSubmixEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__13setIP10XAudioUnitNS_4lessIS2_EENS_9allocatorIS2_EEEC2B9nqe210106ERKS7_
- __ZNSt3__14__fs10filesystem4pathC2B9nqe210106INS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEvEERKT_NS2_6formatE
- __ZNSt3__14lockB9nqe210106IN5caulk4mach21unfair_recursive_lockEN16AudioQueueObject20WorkQueueLockAdapterEEEvRT_RT0_
- __ZNSt3__14lockB9nqe210106IN5caulk4mach21unfair_recursive_lockENS1_23recursive_mutex_adapterINS1_22pooled_semaphore_mutexEEEEEvRT_RT0_
- __ZNSt3__14pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEaSB9nqe210106EOSB_
- __ZNSt3__14swapB9nqe210106I11AQMESessionEENS_9enable_ifIXaasr21is_move_constructibleIT_EE5valuesr18is_move_assignableIS3_EE5valueEvE4typeERS3_S6_
- __ZNSt3__14swapB9nqe210106IU8__strongU13block_pointerFvPK15AudioBufferListjEEENS_9enable_ifIXaasr21is_move_constructibleIT_EE5valuesr18is_move_assignableIS8_EE5valueEvE4typeERS8_SB_
- __ZNSt3__15dequeIN5boost8functionIFNS1_3msm4back11HandledEnumEvEEENS_9allocatorIS7_EEED2B9nqe210106Ev
- __ZNSt3__15dequeINS_4pairIN5boost8functionIFNS2_3msm4back11HandledEnumEvEEEbEENS_9allocatorIS9_EEE26__maybe_remove_front_spareB9nqe210106Eb
- __ZNSt3__15dequeINS_4pairIN5boost8functionIFNS2_3msm4back11HandledEnumEvEEEbEENS_9allocatorIS9_EEED2B9nqe210106Ev
- __ZNSt3__15dequeIjNS_9allocatorIjEEE26__maybe_remove_front_spareB9nqe210106Eb
- __ZNSt3__15dequeIjNS_9allocatorIjEEED2B9nqe210106Ev
- __ZNSt3__16__lerpB9nqe210106IdEET_S1_S1_S1_
- __ZNSt3__16__treeINS_12__value_typeIKjjEENS_19__map_value_compareIS2_NS_4pairIS2_jEENS_4lessIS2_EELb1EEENS_9allocatorIS6_EEE21__emplace_unique_implIJRNS_5tupleIJS2_jEEEEEENS5_INS_15__tree_iteratorIS3_PNS_11__tree_nodeIS3_PvEElEEbEEDpOT_
- __ZNSt3__16__treeINS_12__value_typeIKjjEENS_19__map_value_compareIS2_NS_4pairIS2_jEENS_4lessIS2_EELb1EEENS_9allocatorIS6_EEE21__remove_node_pointerEPNS_11__tree_nodeIS3_PvEE
- __ZNSt3__16__treeINS_12__value_typeIKjjEENS_19__map_value_compareIS2_NS_4pairIS2_jEENS_4lessIS2_EELb1EEENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS3_PvEE
- __ZNSt3__16__treeINS_12__value_typeIN14SystemListener5EventENS_8functionIFvbEEEEENS_19__map_value_compareIS3_NS_4pairIKS3_S6_EENS_4lessIS3_EELb1EEENS_9allocatorISB_EEE7destroyEPNS_11__tree_nodeIS7_PvEE
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE8LocalityEENS_19__map_value_compareIS7_NS_4pairIKS7_S8_EENS_4lessIS7_EELb1EEENS5_ISD_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISN_EERKT_
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE8LocalityEENS_19__map_value_compareIS7_NS_4pairIKS7_S8_EENS_4lessIS7_EELb1EEENS5_ISD_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSN_SN_
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE8LocalityEENS_19__map_value_compareIS7_NS_4pairIKS7_S8_EENS_4lessIS7_EELb1EEENS5_ISD_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJRSC_EEENSN_IJEEEEEENSB_INS_15__tree_iteratorIS9_PNS_11__tree_nodeIS9_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE8LocalityEENS_19__map_value_compareIS7_NS_4pairIKS7_S8_EENS_4lessIS7_EELb1EEENS5_ISD_EEE25__emplace_unique_key_argsIS7_JRS7_S8_EEENSB_INS_15__tree_iteratorIS9_PNS_11__tree_nodeIS9_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE8LocalityEENS_19__map_value_compareIS7_NS_4pairIKS7_S8_EENS_4lessIS7_EELb1EEENS5_ISD_EEE7destroyEPNS_11__tree_nodeIS9_PvEE
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN10applesauce2CF7TypeRefEEENS_19__map_value_compareIS7_NS_4pairIKS7_SA_EENS_4lessIS7_EELb1EEENS5_ISF_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISP_EERKT_
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN10applesauce2CF7TypeRefEEENS_19__map_value_compareIS7_NS_4pairIKS7_SA_EENS_4lessIS7_EELb1EEENS5_ISF_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSP_SP_
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN10applesauce2CF7TypeRefEEENS_19__map_value_compareIS7_NS_4pairIKS7_SA_EENS_4lessIS7_EELb1EEENS5_ISF_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJOS7_EEENSP_IJEEEEEENSD_INS_15__tree_iteratorISB_PNS_11__tree_nodeISB_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN10applesauce2CF7TypeRefEEENS_19__map_value_compareIS7_NS_4pairIKS7_SA_EENS_4lessIS7_EELb1EEENS5_ISF_EEE7destroyEPNS_11__tree_nodeISB_PvEE
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29NewNotificationCenterObserverEEEENS_19__map_value_compareIS7_NS_4pairIKS7_SA_EENS_4lessIS7_EELb1EEENS5_ISF_EEE7destroyEPNS_11__tree_nodeISB_PvEE
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29OldNotificationCenterObserverEEEENS_19__map_value_compareIS7_NS_4pairIKS7_SA_EENS_4lessIS7_EELb1EEENS5_ISF_EEE7destroyEPNS_11__tree_nodeISB_PvEE
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS_19__map_value_compareIS7_NS_4pairIKS7_S7_EENS_4lessIS7_EELb1EEENS5_ISC_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS_19__map_value_compareIS7_NS_4pairIKS7_S7_EENS_4lessIS7_EELb1EEENS5_ISC_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSM_SM_
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS_19__map_value_compareIS7_NS_4pairIKS7_S7_EENS_4lessIS7_EELb1EEENS5_ISC_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJOS7_EEENSM_IJEEEEEENSA_INS_15__tree_iteratorIS8_PNS_11__tree_nodeIS8_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS_19__map_value_compareIS7_NS_4pairIKS7_S7_EENS_4lessIS7_EELb1EEENS5_ISC_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJRSB_EEENSM_IJEEEEEENSA_INS_15__tree_iteratorIS8_PNS_11__tree_nodeIS8_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS_19__map_value_compareIS7_NS_4pairIKS7_S7_EENS_4lessIS7_EELb1EEENS5_ISC_EEE7destroyEPNS_11__tree_nodeIS8_PvEE
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEyEENS_19__map_value_compareIS7_NS_4pairIKS7_yEENS_4lessIS7_EELb1EEENS5_ISC_EEE7destroyEPNS_11__tree_nodeIS8_PvEE
- __ZNSt3__16__treeINS_12__value_typeIP14MEMixerChannelN9TapSubmix10InputStateEEENS_19__map_value_compareIS3_NS_4pairIKS3_S5_EENS_4lessIS3_EELb1EEENS_9allocatorISA_EEE7destroyEPNS_11__tree_nodeIS6_PvEE
- __ZNSt3__16__treeINS_12__value_typeIP9TapSubmixN14MEMixerChannel19TapSubmixConnectionEEENS_19__map_value_compareIS3_NS_4pairIKS3_S5_EENS_4lessIS3_EELb1EEENS_9allocatorISA_EEE12__find_equalIS3_EERPNS_16__tree_node_baseIPvEENS_21__tree_const_iteratorIS6_PNS_11__tree_nodeIS6_SJ_EElEERPNS_15__tree_end_nodeISL_EESM_RKT_
- __ZNSt3__16__treeINS_12__value_typeIP9TapSubmixN14MEMixerChannel19TapSubmixConnectionEEENS_19__map_value_compareIS3_NS_4pairIKS3_S5_EENS_4lessIS3_EELb1EEENS_9allocatorISA_EEE7destroyEPNS_11__tree_nodeIS6_PvEE
- __ZNSt3__16__treeINS_12__value_typeIPK14AQIONodeClientZN2AT13SessionFacadeL34PopulateSourceFormatInfoDictionaryEP14__CFDictionaryPKvRS3_RN2CA17StreamDescriptionEbbbE16SourceFormatInfoEENS_19__map_value_compareIS4_NS_4pairIKS4_SF_EENS_4lessIS4_EELb1EEENS_9allocatorISK_EEE7destroyEPNS_11__tree_nodeISG_PvEE
- __ZNSt3__16__treeINS_12__value_typeIdjEENS_19__map_value_compareIdNS_4pairIKdjEENS_4lessIdEELb1EEENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS2_PvEE
- __ZNSt3__16__treeINS_12__value_typeIiNS_10unique_ptrI13XOSTransactorNS_14default_deleteIS3_EEEEEENS_19__map_value_compareIiNS_4pairIKiS6_EENS_4lessIiEELb1EEENS_9allocatorISB_EEE7destroyEPNS_11__tree_nodeIS7_PvEE
- __ZNSt3__16__treeINS_12__value_typeIiNS_6bitsetILm255EEEEENS_19__map_value_compareIiNS_4pairIKiS3_EENS_4lessIiEELb1EEENS_9allocatorIS8_EEE7destroyEPNS_11__tree_nodeIS4_PvEE
- __ZNSt3__16__treeINS_12__value_typeIjNS_4pairIN11MuteManager14AudioMuteCountENS3_15HapticMuteCountEEEEENS_19__map_value_compareIjNS2_IKjS6_EENS_4lessIjEELb1EEENS_9allocatorISA_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRS9_EEENSL_IJEEEEEENS2_INS_15__tree_iteratorIS7_PNS_11__tree_nodeIS7_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeIjNS_4pairIN11MuteManager14AudioMuteCountENS3_15HapticMuteCountEEEEENS_19__map_value_compareIjNS2_IKjS6_EENS_4lessIjEELb1EEENS_9allocatorISA_EEE7destroyEPNS_11__tree_nodeIS7_PvEE
- __ZNSt3__16__treeINS_12__value_typeIjNS_6bitsetILm32EEEEENS_19__map_value_compareIjNS_4pairIKjS3_EENS_4lessIjEELb1EEENS_9allocatorIS8_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRS7_EEENSJ_IJEEEEEENS6_INS_15__tree_iteratorIS4_PNS_11__tree_nodeIS4_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeIjNS_6bitsetILm32EEEEENS_19__map_value_compareIjNS_4pairIKjS3_EENS_4lessIjEELb1EEENS_9allocatorIS8_EEE7destroyEPNS_11__tree_nodeIS4_PvEE
- __ZNSt3__16__treeINS_12__value_typeIjP15ActiveSoundInfoEENS_19__map_value_compareIjNS_4pairIKjS3_EENS_4lessIjEELb1EEENS_9allocatorIS8_EEE7destroyEPNS_11__tree_nodeIS4_PvEE
- __ZNSt3__16__treeINS_12__value_typeIjU8__strongP14NSMutableArrayIP15AVServerWrapperEEENS_19__map_value_compareIjNS_4pairIKjS7_EENS_4lessIjEELb1EEENS_9allocatorISC_EEE7destroyEPNS_11__tree_nodeIS8_PvEE
- __ZNSt3__16__treeINS_12__value_typeImN5caulk5alloc22consolidating_free_mapIN2AQ19SharedPageAllocatorELm10485760EE14FreelistOfSizeEEENS_19__map_value_compareImNS_4pairIKmS8_EENS_4lessImEELb1EEENS_9allocatorISD_EEE21__remove_node_pointerEPNS_11__tree_nodeIS9_PvEE
- __ZNSt3__16__treeINS_12__value_typeImN5caulk5alloc22consolidating_free_mapIN2AQ19SharedPageAllocatorELm10485760EE14FreelistOfSizeEEENS_19__map_value_compareImNS_4pairIKmS8_EENS_4lessImEELb1EEENS_9allocatorISD_EEE7destroyEPNS_11__tree_nodeIS9_PvEE
- __ZNSt3__16__treeINS_12__value_typeImNS_10shared_ptrI11ClientEntryEEEENS_19__map_value_compareImNS_4pairIKmS4_EENS_4lessImEELb1EEENS_9allocatorIS9_EEE7destroyEPNS_11__tree_nodeIS5_PvEE
- __ZNSt3__16__treeINS_12__value_typeImjEENS_19__map_value_compareImNS_4pairIKmjEENS_4lessImEELb1EEEN5caulk12rt_allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS2_PvEE
- __ZNSt3__16__treeINS_12__value_typeImjEENS_19__map_value_compareImNS_4pairIKmjEENS_4lessImEELb1EEENS_9allocatorIS6_EEE21__remove_node_pointerEPNS_11__tree_nodeIS2_PvEE
- __ZNSt3__16__treeINS_12__value_typeImjEENS_19__map_value_compareImNS_4pairIKmjEENS_4lessImEELb1EEENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS2_PvEE
- __ZNSt3__16__treeINS_12__value_typeIttEENS_19__map_value_compareItNS_4pairIKttEENS_4lessItEELb1EEENS_9allocatorIS6_EEE5eraseENS_21__tree_const_iteratorIS2_PNS_11__tree_nodeIS2_PvEElEESI_
- __ZNSt3__16__treeINS_12__value_typeIttEENS_19__map_value_compareItNS_4pairIKttEENS_4lessItEELb1EEENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS2_PvEE
- __ZNSt3__16__treeIP10XAudioUnitNS_4lessIS2_EENS_9allocatorIS2_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSC_SC_
- __ZNSt3__16__treeIP10XAudioUnitNS_4lessIS2_EENS_9allocatorIS2_EEE18_DetachedTreeCache13__detach_nextEPNS_11__tree_nodeIS2_PvEE
- __ZNSt3__16__treeIP10XAudioUnitNS_4lessIS2_EENS_9allocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE
- __ZNSt3__16__treeIjNS_4lessIjEENS_9allocatorIjEEE7destroyEPNS_11__tree_nodeIjPvEE
- __ZNSt3__16__treeIxNS_4lessIxEENS_9allocatorIxEEE7destroyEPNS_11__tree_nodeIxPvEE
- __ZNSt3__16any_ofB9nqe210106INS_11__wrap_iterIPPK10__CFStringEEZN16AudioQueueObject11SetPropertyEjR14CADeserializerE3$_0EEbT_SB_T0_
- __ZNSt3__16vectorI10ChaseEventN5caulk12rt_allocatorIS1_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorI10ChaseEventN5caulk12rt_allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE18__assign_with_sizeB9nqe210106IPS1_S6_EEvT_T0_l
- __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE18__insert_with_sizeB9nqe210106INS_11__wrap_iterIPS1_EES8_EES8_NS6_IPKS1_EET_T0_l
- __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE27__insert_assign_n_uncheckedB9nqe210106INS_11__wrap_iterIPS1_EELi0EEEvT_lS7_
- __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE9push_backB9nqe210106ERKS1_
- __ZNSt3__16vectorI10PowerMeterNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI11AQMESessionNS_9allocatorIS1_EEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorI11AQMESessionNS_9allocatorIS1_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorI11AQMESessionNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI11TrackChaserNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI11VolumeEventN5caulk12rt_allocatorIS1_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorI11VolumeEventN5caulk12rt_allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI13ChaseInstInfoNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI13RootQueueInfoNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI14MEStreamTypeIDNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI15MEVADIdentifierNS_9allocatorIS1_EEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorI15MEVADIdentifierNS_9allocatorIS1_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorI15MEVADIdentifierNS_9allocatorIS1_EEE16__init_with_sizeB9nqe210106IPS1_S6_EEvT_T0_m
- __ZNSt3__16vectorI15MEVADIdentifierNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI15MeterTrackEntryNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI15MeterTrackEntryNS_9allocatorIS1_EEE9push_backB9nqe210106ERKS1_
- __ZNSt3__16vectorI16AURateRampStructNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI18AudioMetadataEventNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI18AudioMetadataEventNS_9allocatorIS1_EEE9push_backB9nqe210106ERKS1_
- __ZNSt3__16vectorI20AUNodeRenderCallbackNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI22AUGraphLiveUpdateEventNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI22AUGraphLiveUpdateEventNS_9allocatorIS1_EEE9push_backB9nqe210106ERKS1_
- __ZNSt3__16vectorI23AudioUnitNodeConnectionNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI23AudioUnitParameterEventN5caulk12rt_allocatorIS1_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorI23AudioUnitParameterEventN5caulk12rt_allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI23AudioUnitParameterEventNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI24AudioQueueParameterEventNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI25AudioQueueLevelMeterStateNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI26AQBufferCreateDestroyEventNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI26AudioObjectPropertyAddressNS_9allocatorIS1_EEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorI26AudioObjectPropertyAddressNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI27AudioQueueChannelAssignmentNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI28AudioStreamPacketDescriptionNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI30AQProcessingNodeImmediateEventNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI32AudioSessionPropertyListenerInfoNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI9TapSourceNS_9allocatorIS1_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorI9TapSourceNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE9push_backB9nqe210106EOS3_
- __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN10applesauce2CF9NumberRefENS_9allocatorIS3_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorIN10applesauce2CF9NumberRefENS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN14AudioUnitGraph14RenderCallbackENS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN14NoteOffManager14ControlMessageENS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN14NoteOffManager14ControlMessageENS_9allocatorIS2_EEE9push_backB9nqe210106EOS2_
- __ZNSt3__16vectorIN16AudioQueueObject12AQRateChangeENS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN18AQOfflineMixerBase10MixerQueueENS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN18AQOfflineMixerBase15StartQueueEventENS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN19SequenceDestination14TrackPlayStateENS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN19SequenceDestination14TrackPlayStateENS_9allocatorIS2_EEE9push_backB9nqe210106ERKS2_
- __ZNSt3__16vectorIN21IPCAUSharedMemoryBase7ElementENS_9allocatorIS2_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorIN21VibeToHapticConverter11SegmentInfoENS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN21VibeToHapticConverter11SegmentInfoENS_9allocatorIS2_EEE9push_backB9nqe210106EOS2_
- __ZNSt3__16vectorIN25AUNodeSequenceDestination18RampTrackPlayStateENS_9allocatorIS2_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorIN25AUNodeSequenceDestination18RampTrackPlayStateENS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN2AQ6Server12RemoteClient18ProcessingTapStateENS_9allocatorIS4_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorIN2AQ6Server12RemoteClient18ProcessingTapStateENS_9allocatorIS4_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN2AQ6Server12RemoteClient5QueueENS_9allocatorIS4_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN2AT11Translation19AUAsyncRendererHost34TemporallyOrdereredAudioBufferListENS_9allocatorIS4_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN2AU8Property10Attributes7details15AUPresetWrapperENS_9allocatorIS5_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorIN2AU8Property10Attributes7details15AUPresetWrapperENS_9allocatorIS5_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN5boost8functionIFvRN11SequenceFSM25PostRenderFlushingVisitorEP14SequenceActiondEEENS_9allocatorIS9_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorIN8InfoList9InfoEntryENS_9allocatorIS2_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorIN8InfoList9InfoEntryENS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN8TempoMap10TempoEntryENS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN8XAUMixer11EInputStateENS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN8audioipc18SharedAudioBuffers7ElementENS_9allocatorIS3_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorIN8audioipc18SharedAudioBuffers7ElementENS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_10shared_ptrI14HapticSequenceEEN5caulk12rt_allocatorIS3_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_10shared_ptrI14HapticSequenceEEN5caulk12rt_allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_10shared_ptrI14HapticSequenceEEN5caulk12rt_allocatorIS3_EEE5clearB9nqe210106Ev
- __ZNSt3__16vectorINS_10shared_ptrI16MCProcessingNodeEENS_9allocatorIS3_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_10shared_ptrI16MCProcessingNodeEENS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_10shared_ptrI16MCProcessingNodeEENS_9allocatorIS3_EEE9push_backB9nqe210106ERKS3_
- __ZNSt3__16vectorINS_10shared_ptrI8AQIONodeEENS_9allocatorIS3_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_10shared_ptrI8AQIONodeEENS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE16__init_with_sizeB9nqe210106IPS3_S8_EEvT_T0_m
- __ZNSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE5clearB9nqe210106Ev
- __ZNSt3__16vectorINS_10shared_ptrIN10AQMEIO_HAL8IOStreamEEENS_9allocatorIS4_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_10shared_ptrIN10AQMEIO_HAL8IOStreamEEENS_9allocatorIS4_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_10shared_ptrIN10AQMEIO_HAL8IOStreamEEENS_9allocatorIS4_EEE5clearB9nqe210106Ev
- __ZNSt3__16vectorINS_10shared_ptrIN18PowerUsageWatchdog17ClientDescriptionEEENS_9allocatorIS4_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_10shared_ptrIN18PowerUsageWatchdog17ClientDescriptionEEENS_9allocatorIS4_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_10shared_ptrIN2AQ3API9SubmixTapEEENS_9allocatorIS5_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_10shared_ptrIN2AQ3API9SubmixTapEEENS_9allocatorIS5_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrI11IAQMEDeviceNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrI11IAQMEDeviceNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrI11MEConnectorNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrI11MEConnectorNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrI11MEConnectorNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE9push_backB9nqe210106EOS5_
- __ZNSt3__16vectorINS_10unique_ptrI14AQClientBufferN2AQ3API13BufferDeleterEEENS_9allocatorIS6_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrI14AQOfflineMixerNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrI14AQOfflineMixerNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrI14AQOfflineMixerNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE5clearB9nqe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrI15SubmixTapObjectNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrI15SubmixTapObjectNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrI16AQProcessingNodeNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrI16AQProcessingNodeNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrI16SSSVibrationDataNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrIN18PowerUsageWatchdog12ClientLoggerENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrIN18PowerUsageWatchdog12ClientLoggerENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_10unique_ptrIN2AQ6Server12RemoteClientENS_14default_deleteIS4_EEEENS_9allocatorIS7_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_13unordered_mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbNS_4hashIS7_EENS_8equal_toIS7_EENS5_INS_4pairIKS7_bEEEEEENS5_ISG_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEENS_9allocatorISC_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEENS_9allocatorISC_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_4pairINS_10shared_ptrI11SynthOutputEEbEENS_9allocatorIS5_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_4pairINS_10shared_ptrI11SynthOutputEEbEENS_9allocatorIS5_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_4pairINS_10shared_ptrI11SynthOutputEEbEENS_9allocatorIS5_EEE5clearB9nqe210106Ev
- __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS5_IS8_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS5_IS8_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_4pairIPFiPvPjPK14AudioTimeStampjjP15AudioBufferListES2_EEN5caulk12rt_allocatorISB_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_4pairIPFiPvPjPK14AudioTimeStampjjP15AudioBufferListES2_EEN5caulk12rt_allocatorISB_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_4pairIffEEN5caulk12rt_allocatorIS2_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_4pairIffEEN5caulk12rt_allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_4pairIjNS_10shared_ptrIN2AQ3API11BufferOwnerEEEEENS_9allocatorIS7_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_4pairIjNS_10shared_ptrIN2AQ3API11BufferOwnerEEEEENS_9allocatorIS7_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_4pairIjNS_10shared_ptrIN2AQ3API11BufferOwnerEEEEENS_9allocatorIS7_EEE5clearB9nqe210106Ev
- __ZNSt3__16vectorINS_4pairIjNS_8optionalIjEEEENS_9allocatorIS4_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_4pairIjNS_8optionalIjEEEENS_9allocatorIS4_EEE9push_backB9nqe210106EOS4_
- __ZNSt3__16vectorINS_5tupleIJjNS_10shared_ptrIN2AQ3API5QueueEEEEEENS_9allocatorIS7_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_5tupleIJjNS_10shared_ptrIN2AQ3API5QueueEEEEEENS_9allocatorIS7_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_5tupleIJjNS_10shared_ptrIN2AQ3API9SubmixTapEEEEEENS_9allocatorIS7_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_5tupleIJjNS_10shared_ptrIN2AQ3API9SubmixTapEEEEEENS_9allocatorIS7_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_5tupleIJjPFvPvP16OpaqueAudioQueuejES2_EEENS_9allocatorIS7_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_8weak_ptrI25AQMEIO_NotificationClientEENS_9allocatorIS3_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_8weak_ptrI25AQMEIO_NotificationClientEENS_9allocatorIS3_EEE16__init_with_sizeB9nqe210106IPS3_S8_EEvT_T0_m
- __ZNSt3__16vectorINS_8weak_ptrI25AQMEIO_NotificationClientEENS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_8weak_ptrI8AQIONodeEENS_9allocatorIS3_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorINS_8weak_ptrI8AQIONodeEENS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorINS_8weak_ptrIN5caulk17lifetime_observedINS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS5_EEEENS2_23shared_instance_managerIS5_E8observerEEEEENS_9allocatorISD_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP10AUNodeInfoNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP10AUNodeInfoNS_9allocatorIS2_EEE9push_backB9nqe210106ERKS2_
- __ZNSt3__16vectorIP10ClientInfoNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP10ClientInfoNS_9allocatorIS2_EEE20__throw_out_of_rangeB9nqe210106Ev
- __ZNSt3__16vectorIP11MCAudioUnitNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP11MCAudioUnitNS_9allocatorIS2_EEE9push_backB9nqe210106EOS2_
- __ZNSt3__16vectorIP11MEConnectorNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP11MEConnectorNS_9allocatorIS2_EEE9push_backB9nqe210106EOS2_
- __ZNSt3__16vectorIP12SSSAudioDataNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP13AudioTapMixerNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP13AudioTapMixerNS_9allocatorIS2_EEE9push_backB9nqe210106ERKS2_
- __ZNSt3__16vectorIP13MESubmixGraphNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP13SequenceTrackNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP14AQIONodeClientNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP14AudioTapObjectNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP14CAExternalLockNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP14MEMixerChannelNS_9allocatorIS2_EEE16__init_with_sizeB9nqe210106IPS2_S7_EEvT_T0_m
- __ZNSt3__16vectorIP14MEMixerChannelNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP14MEMixerChannelNS_9allocatorIS2_EEE9push_backB9nqe210106ERKS2_
- __ZNSt3__16vectorIP14MixTapToUplinkNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP14__CFDictionaryNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP15InputDispatcherNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP15XProcessingBaseNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP15XProcessingBaseNS_9allocatorIS2_EEE9push_backB9nqe210106EOS2_
- __ZNSt3__16vectorIP16AudioQueueObjectNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP19MEInputStreamClientNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP19SSSActionPlayerBaseNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP19SSSActionPlayerBaseNS_9allocatorIS2_EEE9push_backB9nqe210106ERKS2_
- __ZNSt3__16vectorIP20MEOutputStreamClientNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP20MEOutputStreamClientNS_9allocatorIS2_EEE9push_backB9nqe210106ERKS2_
- __ZNSt3__16vectorIP25AUNodeSequenceDestinationNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP31MIDIEndpointSequenceDestinationNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP8AQIONodeNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP8UserInfoNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP8UserInfoNS_9allocatorIS2_EEE20__throw_out_of_rangeB9nqe210106Ev
- __ZNSt3__16vectorIPK10__CFStringNS_9allocatorIS3_EEE16__init_with_sizeB9nqe210106IPKS3_S9_EEvT_T0_m
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEEC2B9nqe210106Em
- __ZNSt3__16vectorIPN11DSP_Routing15PublishedStreamENS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIPN11DSP_Routing6StreamENS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIPN15CAListenerProxy8ListenerENS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIPN15CAListenerProxy8ListenerENS_9allocatorIS3_EEE9push_backB9nqe210106EOS3_
- __ZNSt3__16vectorIPN16AudioQueueObject23ScheduledSliceAllocatorENS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIPN2AQ3API12OfflineMixerENS_9allocatorIS4_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIPvNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorISt4byteNS_9allocatorIS1_EEEC2B9nqe210106Em
- __ZNSt3__16vectorIU8__strongP24ATAudioSessionClientImplNS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIU8__strongP24ATAudioSessionClientImplNS_9allocatorIS3_EEE9push_backB9nqe210106ERU8__strongKS2_
- __ZNSt3__16vectorIcN5caulk12rt_allocatorIcEEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorIcN5caulk12rt_allocatorIcEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIcNS_9allocatorIcEEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorIcNS_9allocatorIcEEE16__init_with_sizeB9nqe210106IPcS5_EEvT_T0_m
- __ZNSt3__16vectorIcNS_9allocatorIcEEE18__assign_with_sizeB9nqe210106IPcS5_EEvT_T0_l
- __ZNSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIcNS_9allocatorIcEEE8__appendEm
- __ZNSt3__16vectorIcNS_9allocatorIcEEE8__appendEmRKc
- __ZNSt3__16vectorIcNS_9allocatorIcEEEC2B9nqe210106Em
- __ZNSt3__16vectorIcNS_9allocatorIcEEEC2B9nqe210106EmRKc
- __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorIhNS_9allocatorIhEEE18__assign_with_sizeB9nqe210106IPhS5_EEvT_T0_l
- __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIhNS_9allocatorIhEEE8__appendEm
- __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B9nqe210106Em
- __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorIiNS_9allocatorIiEEE16__init_with_sizeB9nqe210106IPKiS6_EEvT_T0_m
- __ZNSt3__16vectorIiNS_9allocatorIiEEE16__init_with_sizeB9nqe210106IPiS5_EEvT_T0_m
- __ZNSt3__16vectorIiNS_9allocatorIiEEE18__assign_with_sizeB9nqe210106IPKiS6_EEvT_T0_l
- __ZNSt3__16vectorIiNS_9allocatorIiEEE18__assign_with_sizeB9nqe210106IPiS5_EEvT_T0_l
- __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIiNS_9allocatorIiEEE9push_backB9nqe210106EOi
- __ZNSt3__16vectorIjNS_9allocatorIjEEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorIjNS_9allocatorIjEEE16__init_with_sizeB9nqe210106INS_11__wrap_iterIPKjEES8_EEvT_T0_m
- __ZNSt3__16vectorIjNS_9allocatorIjEEE16__init_with_sizeB9nqe210106IPKjS6_EEvT_T0_m
- __ZNSt3__16vectorIjNS_9allocatorIjEEE16__init_with_sizeB9nqe210106IPjS5_EEvT_T0_m
- __ZNSt3__16vectorIjNS_9allocatorIjEEE18__assign_with_sizeB9nqe210106IPKjS6_EEvT_T0_l
- __ZNSt3__16vectorIjNS_9allocatorIjEEE18__assign_with_sizeB9nqe210106IPjS5_EEvT_T0_l
- __ZNSt3__16vectorIjNS_9allocatorIjEEE18__insert_with_sizeB9nqe210106INS_11__wrap_iterIPjEES7_EES7_NS5_IPKjEET_T0_l
- __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_out_of_rangeB9nqe210106Ev
- __ZNSt3__16vectorIjNS_9allocatorIjEEE9push_backB9nqe210106EOj
- __ZNSt3__16vectorIjNS_9allocatorIjEEE9push_backB9nqe210106ERKj
- __ZNSt3__16vectorIjNS_9allocatorIjEEEC2B9nqe210106Em
- __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIxNS_9allocatorIxEEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorIxNS_9allocatorIxEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__17__sort3B9nqe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP15MEVADIdentifierLi0EEEbT1_S7_S7_T0_
- __ZNSt3__17__sort3B9nqe210106INS_17_ClassicAlgPolicyERZN17AudioTapSpecifierC1ENS_6vectorIjNS_9allocatorIjEEEE22ATAudioTapMuteBehaviorEUlRK11AQMESessionSA_E_PS8_Li0EEEbT1_SE_SE_T0_
- __ZNSt3__17__sort4B9nqe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP10MusicEventLi0EEEvT1_S7_S7_S7_T0_
- __ZNSt3__17__sort4B9nqe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP11VolumeEventLi0EEEvT1_S7_S7_S7_T0_
- __ZNSt3__17__sort4B9nqe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEELi0EEEvT1_SC_SC_SC_T0_
- __ZNSt3__17__sort4B9nqe210106INS_17_ClassicAlgPolicyERZN17AudioTapSpecifierC1ENS_6vectorIjNS_9allocatorIjEEEE22ATAudioTapMuteBehaviorEUlRK11AQMESessionSA_E_PS8_Li0EEEvT1_SE_SE_SE_T0_
- __ZNSt3__17__sort5B9nqe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP15MEVADIdentifierLi0EEEvT1_S7_S7_S7_S7_T0_
- __ZNSt3__17__sort5B9nqe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN14NoteOffManager11NoteOffInfoELi0EEEvT1_S8_S8_S8_S8_T0_
- __ZNSt3__17__sort5B9nqe210106INS_17_ClassicAlgPolicyERZN17AudioTapSpecifierC1ENS_6vectorIjNS_9allocatorIjEEEE22ATAudioTapMuteBehaviorEUlRK11AQMESessionSA_E_PS8_Li0EEEvT1_SE_SE_SE_SE_T0_
- __ZNSt3__17__sort5B9nqe210106INS_17_ClassicAlgPolicyERZZZN2AT11Translation19AUAsyncRendererHost9ConfigureEvENK3$_0clENS_6chrono10time_pointINS6_12steady_clockENS6_8durationIxNS_5ratioILl1ELl1000000000EEEEEEERK15AudioBufferListiENKUlRT_E_clINS_6vectorINS4_34TemporallyOrdereredAudioBufferListENS_9allocatorISM_EEEEEEDaSI_EUlRKSM_SS_E_PSM_Li0EEEvT1_SW_SW_SW_SW_T0_
- __ZNSt3__17find_ifB9nqe210106INS_11__wrap_iterIP10MusicEventEEZN13TrackIterator4SeekEdE3$_0EET_S7_S7_T0_
- __ZNSt3__17find_ifB9nqe210106INS_16reverse_iteratorINS_11__wrap_iterIP10MusicEventEEEEZN13TrackIterator4SeekEdE3$_0EET_S9_S9_T0_
- __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB9nqe210106IRP10MusicEventS6_EEvOT_OT0_
- __ZNSt3__18functionIFviEEaSERKS2_
- __ZNSt3__18optionalI14AQMEIO_BindingE7emplaceB9nqe210106IJR15AQIONodeManagerRPK10__CFStringELi0EEERS1_DpOT_
- __ZNSt3__18optionalI14AQMEIO_BindingEaSB9nqe210106IRKS1_Li0EEERS2_OT_
- __ZNSt3__18optionalIN4swix17connection_configEEC1B9nqe210106EOS3_
- __ZNSt3__18optionalIN4swix6resultIJNS1_4dataEEEEEaSB9nqe210106IS4_Li0EEERS5_OT_
- __ZNSt3__18optionalIN5caulk10concurrent25guarded_lookup_hash_tableIjP16BaseOpaqueObjectLNS2_33guarded_lookup_hash_table_optionsE0E24OpaqueObjectIdentityHashE13scoped_lookupEE7emplaceB9nqe210106IJRS8_RKjELi0EEERS9_DpOT_
- __ZNSt3__18optionalIN5caulk9semaphoreEE7emplaceB9nqe210106IJELi0EEERS2_DpOT_
- __ZNSt3__18optionalIN8audioipc18SharedAudioBuffersEE7emplaceB9nqe210106IJRjNS_4spanIKNS1_14ExtendedFormatELm18446744073709551615EEENS6_IhLm18446744073709551615EEEELi0EEERS2_DpOT_
- __ZNSt3__18try_lockB9nqe210106IN5caulk23recursive_mutex_adapterINS1_22pooled_semaphore_mutexEEENS1_4mach21unfair_recursive_lockEEEiRT_RT0_
- __ZNSt3__18try_lockB9nqe210106IN5caulk4mach21unfair_recursive_lockENS1_23recursive_mutex_adapterINS1_22pooled_semaphore_mutexEEEEEiRT_RT0_
- __ZNSt3__18try_lockB9nqe210106IN5caulk4mach21unfair_recursive_lockES3_EEiRT_RT0_
- __ZNSt3__19allocatorI10MusicEventE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorI11AQMESessionE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorI13ChaseInstInfoE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorI14MEStreamTypeIDE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorI15MEVADIdentifierE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorI15MeterTrackEntryE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorI16AURateRampStructE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorI18AudioMetadataEventE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorI24AudioQueueParameterEventE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorI26AQBufferCreateDestroyEventE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorI26AudioObjectPropertyAddressE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorI30AQProcessingNodeImmediateEventE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorI32AudioSessionPropertyListenerInfoE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorI9TapSourceE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIN10applesauce2CF11TypeRefPairEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIN10applesauce2CF7TypeRefEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIN10applesauce2CF9NumberRefEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIN14NoteOffManager14ControlMessageEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIN16AudioQueueObject12AQRateChangeEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIN18AQOfflineMixerBase15StartQueueEventEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIN21VibeToHapticConverter11SegmentInfoEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIN2AQ6Server12RemoteClient5QueueEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIN8TempoMap10TempoEntryEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIN8audioipc18SharedAudioBuffers7ElementEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorINS_10shared_ptrI9TapSubmixEEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorINS_10shared_ptrIN10AQMEIO_HAL8IOStreamEEEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorINS_10unique_ptrI11IAQMEDeviceNS_14default_deleteIS2_EEEEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorINS_10unique_ptrI11MEConnectorNS_14default_deleteIS2_EEEEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorINS_10unique_ptrIN18PowerUsageWatchdog12ClientLoggerENS_14default_deleteIS3_EEEEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorINS_12basic_stringIcNS_11char_traitsIcEENS0_IcEEEEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS0_IcEEEES6_EEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorINS_5tupleIJjPFvPvP16OpaqueAudioQueuejES2_EEEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorINS_8weak_ptrI25AQMEIO_NotificationClientEEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIP10AUNodeInfoE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIP11MCAudioUnitE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIP14AQIONodeClientE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIP14MEMixerChannelE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIP15InputDispatcherE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIP15XProcessingBaseE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIP19SSSActionPlayerBaseE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIP20MEOutputStreamClientE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIPKvE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIPN5boost8functionIFNS1_3msm4back11HandledEnumEvEEEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIPNS_4pairIN5boost8functionIFNS2_3msm4back11HandledEnumEvEEEbEEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIPjE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIPmE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIfE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIiE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIjE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorImE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIxE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19remove_ifB9nqe210106INS_11__wrap_iterIPNS_8weak_ptrIN5caulk17lifetime_observedINS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS6_EEEENS3_23shared_instance_managerIS6_E8observerEEEEEEEZNSB_14remove_expiredEvEUlRKT_E_EESH_SH_SH_T0_
- __ZNSt3__1plB9nqe210106IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEOS9_PKS6_
- __ZNSt3__1plB9nqe210106IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_OS9_
- __ZNSt3__1plB9nqe210106IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_PKS6_
- __ZNSt3__1ssB9nqe210106IcNS_11char_traitsIcEENS_9allocatorIcEEEEDaRKNS_12basic_stringIT_T0_T1_EESC_
- __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- __ZSt30__make_exception_ptr_via_throwB9nqe210106INSt3__112future_errorEESt13exception_ptrRT_
- __ZTC21AudioSessionException0_11CAException
- __ZTI11CAException
- __ZTS11CAException
- __ZTT21AudioSessionException
- __ZTV10TOpaqueRefIN5Phase13ServerManagerEE
- __ZTV11CAException
- __ZTV16TAtomicAllocatorI15AQBufferCommandE
- __ZTV16XAtomicAllocator
- __ZTVN5caulk10concurrent7details12message_callIRZN11ClientEntry19handleSequenceEndedEmNS_16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEEEE3$_0JEEE
- __ZTVN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry18playSequenceWithIDEmddE3$_0JEEE
- __ZTVN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry19handleSequenceEndedEmNS_16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEEEE3$_0JEEE
- __ZTVN5caulk10concurrent7details15rt_message_callIRZN17AudioEventManager32disableAndRemoveCustomAudioEventEjE3$_0JEEE
- __ZTVNSt3__110__function6__funcIN5caulk16inplace_functionIFvmELm32ELm8ENS2_23inplace_function_detail6vtableEEES4_EE
- __ZTVNSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEEN5caulk16inplace_functionIFvmELm32ELm8ENS6_23inplace_function_detail6vtableEEEE3$_0S8_EE
- __ZTVNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM10BeginPauseEEEiRKT_EUliE_FviEEE
- __ZTVNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI12NSDictionaryEEEEiRKT_EUliE_FviEEE
- __ZTVNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI6NSDataEEEEiRKT_EUliE_FviEEE
- __ZTVNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4LoadI7NSArrayEEEEiRKT_EUliE_FviEEE
- __ZTVNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4PlayEEEiRKT_EUliE_FviEEE
- __ZTVNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4SeekEEEiRKT_EUliE_FviEEE
- __ZTVNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM4StopEEEiRKT_EUliE_FviEEE
- __ZTVNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM5StartEEEiRKT_EUliE_FviEEE
- __ZTVNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM6DetachEEEiRKT_EUliE_FviEEE
- __ZTVNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM6ResumeEEEiRKT_EUliE_FviEEE
- __ZTVNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM7PrepareEEEiRKT_EUliE_FviEEE
- __ZTVNSt3__110__function6__funcIZN12SequenceImpl9sendEventIN11SequenceFSM9ForceStopEEEiRKT_EUliE_FviEEE
- __ZTVNSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_0FKNS2_12SynthCommandEvEEE
- __ZTVNSt3__110__function6__funcIZN13ServerManager25handleRouteChangeForEntryENS_10shared_ptrI11ClientEntryEEbNS_8optionalIbEEE3$_0FvbEEE
- __ZTVNSt3__110__function6__funcIZN14DSP_Routing_VPC1ER10AQMEIO_DSPN11DSP_Routing12ERoutingTypeERKNS_6vectorI14MEStreamTypeIDNS_9allocatorIS8_EEEEbE3$_1FbjRKN15CAListenerProxy15HALNotificationEEEE
- __ZTVNSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIbEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EEE
- __ZTVNSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIdEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EEE
- __ZTVNSt3__110__function6__funcIZN18CASmartPreferences10AddHandlerIxEEvPK10__CFStringS6_PFT_PKvRbENS_8functionIFvS7_EEEEUlS9_E_FbS9_EEE
- __ZTVNSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RbEUlbE_FvbEEE
- __ZTVNSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RfEUldE_FvdEEE
- __ZTVNSt3__110__function6__funcIZN18CASmartPreferences4ReadEPK10__CFStringS5_RiEUlxE_FvxEEE
- __ZTVNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERNS_10shared_ptrI11SynthOutputEEEUlvE_FvvEEE
- __ZTVNSt3__120__shared_ptr_pointerIP14HapticSequenceNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEEE
- __ZThn16_N20AudioQueueXPC_Client5StartEj19XAudioTimeStampBasej
- __ZThn16_N20AudioQueueXPC_Server5StartEj19XAudioTimeStampBasej
- __ZThn280_N16AudioQueueObject18ToAudioQueueObjectEv
- __ZThn280_N16AudioQueueObjectD0Ev
- __ZThn280_N16AudioQueueObjectD1Ev
- __ZThn280_N17ZenAQIONodeClient11PrintObjectEP7__sFILE
- __ZThn280_N17ZenAQIONodeClientD0Ev
- __ZThn280_N17ZenAQIONodeClientD1Ev
- __ZThn296_N16AudioQueueObject21SSP_StartTimeResolvedEx15XAudioTimeStamp
- __ZThn296_N16AudioQueueObject30SSP_ScaledToUnscaledSampleTimeEx
- __ZThn296_N16AudioQueueObjectD0Ev
- __ZThn296_N16AudioQueueObjectD1Ev
- __ZThn392_N14AQOfflineMixer11PrintObjectEP7__sFILE
- __ZThn48_N15AudioQueueOwner11PrintObjectEP7__sFILE
- __ZThn600_N10AQMEIO_HAL11PrintObjectEP7__sFILE
- __ZThn8_N14AudioUnitGraph11PrintObjectEP7__sFILE
- __ZZ29+[SSCoreHapticsInfo instance]E4inst
- __ZZ29+[SSCoreHapticsInfo instance]E9onceToken
- __ZZ46-[SSCoreHapticsInfo generateNewSSIDForPlayer:]E12currentToken
- __ZZL12logSubsystemvE5scope
- __ZZL12logSubsystemvE8onceflag
- __ZZL13GetAcousticIDvE13optionalValue.5510
- __ZZL13GetAcousticIDvENKUlvE_clEv.5509
- __ZZL15CPMSLibraryCorePPcE16frameworkLibrary.0.10606
- __ZZL15CPMSLibraryCorePPcE16frameworkLibrary.0.3539
- __ZZL15CPMSLibraryCorePPcE16frameworkLibrary.0.6498
- __ZZL17getCPMSAgentClassvE9softClass.0.3509
- __ZZL17getCPMSAgentClassvE9softClass.0.6496
- __ZZL19AVFAudioLibraryCorePPcE16frameworkLibrary.0.12840
- __ZZL20CoreMediaLibraryCorePPcE16frameworkLibrary.0.5191
- __ZZL20CoreMediaLibraryCorePPcE16frameworkLibrary.0.7257
- __ZZL21GetSpatialMetadataSPIvE19sSpatialMetadataSPI.11731
- __ZZL21GetSpatialMetadataSPIvE23sSpatialMetadataSPIOnce.11730
- __ZZL21getAVAudioFormatClassvE9softClass.0.12080
- __ZZL23MediaToolboxLibraryCorePPcE16frameworkLibrary.0.7249
- __ZZL29AudioSessionServerLibraryCorePPcE16frameworkLibrary.0.8497
- __ZZL29getCPMSClientDescriptionClassvE9softClass.0.3518
- __ZZL33getCMBaseObjectGetVTableSymbolLocvE3ptr.0.5187
- __ZZL33getCMBaseObjectGetVTableSymbolLocvE3ptr.0.7254
- __ZZL58getFigCPECryptorCreateCryptorFromSerializedRecipeSymbolLocvE3ptr.0.7245
- __ZZN11ClientEntry8setStateENS_5StateEE6states
- __ZZN16AudioQueueObjectC1ER15AQIONodeManagerbRK27AudioStreamBasicDescriptionjNSt3__110shared_ptrIN2AQ6Server16RemoteClientBaseEEEP15AudioQueueOwnerRK11AQMESession13audit_token_tRiE28aqCaptureInputRingBufferMode
- __ZZN17LegacyHapticSynth10initializeEvENK3$_0clERNSt3__110shared_ptrI11SynthOutputEE
- __ZZN17LegacyHapticSynth11stopRunningEbbjENK3$_1clERNSt3__110shared_ptrI11SynthOutputEE
- __ZZN17LegacyHapticSynth11stopRunningEbbjENK3$_3clERNSt3__110shared_ptrI11SynthOutputEE
- __ZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_2clERNSt3__110shared_ptrI11SynthOutputEE
- __ZZN22MultiOutputHapticSynth21calculateSampleOffsetERK15XAudioTimeStampP11SynthOutputENK3$_1clERNSt3__110shared_ptrIS3_EE
- __ZZN5caulk10concurrent8skiplistIPvNS_5alloc6detail13tracked_blockELi10ELNS0_16skiplist_optionsE0EE13random_engineEvE6engine
- __ZZN5caulk23inplace_function_detail6vtableIvJmEEC1INSt3__18functionIFvmEEEEENS0_7wrapperIT_EEENUlPvE_8__invokeESB_
- __ZZN5caulk23inplace_function_detail6vtableIvJmEEC1INSt3__18functionIFvmEEEEENS0_7wrapperIT_EEENUlPvOmE_8__invokeESB_SC_
- __ZZN5caulk23inplace_function_detail6vtableIvJmEEC1INSt3__18functionIFvmEEEEENS0_7wrapperIT_EEENUlPvSB_E0_8__invokeESB_SB_
- __ZZN5caulk23inplace_function_detail6vtableIvJmEEC1INSt3__18functionIFvmEEEEENS0_7wrapperIT_EEENUlPvSB_E_8__invokeESB_SB_
- __ZlsR12CASerializerRKPK7__CFURL
- __ZrsR14CADeserializerR15AudioValueRange
- __ZrsR14CADeserializerRPK7__CFURL
- ___22-[AVHapticServer init]_block_invoke.377
- ___29+[SSCoreHapticsInfo instance]_block_invoke
- ___35-[SSCoreHapticsPlayer handleFinish]_block_invoke
- ___36-[SSCoreHapticsInfo unregisterSSID:]_block_invoke
- ___38-[SSCoreHapticsInfo getPlayerForSSID:]_block_invoke
- ___43-[SSCoreHapticsPlayer doInit:haptic:error:]_block_invoke
- ___45-[SSCoreHapticsInfo registerSSID:withPlayer:]_block_invoke
- ___53-[AVHapticServer listener:shouldAcceptNewConnection:]_block_invoke.451
- ___53-[AVHapticServer listener:shouldAcceptNewConnection:]_block_invoke.455
- ___53-[AVHapticServer listener:shouldAcceptNewConnection:]_block_invoke.456
- ___59-[AVVoiceTriggerServer listener:shouldAcceptNewConnection:]_block_invoke.170
- ___59-[AVVoiceTriggerServer listener:shouldAcceptNewConnection:]_block_invoke_2.171
- ___65-[AVHapticServerInstance setupAudioSessionFromID:isShared:error:]_block_invoke.40
- ___69-[SSCoreHapticsPlayer playWithOptions:completionCallbackToken:error:]_block_invoke
- ___69-[SSCoreHapticsPlayer playWithOptions:completionCallbackToken:error:]_block_invoke.63
- ___69-[SSCoreHapticsPlayer playWithOptions:completionCallbackToken:error:]_block_invoke.64
- ___Block_byref_object_copy_.104
- ___Block_byref_object_copy_.110
- ___Block_byref_object_copy_.117
- ___Block_byref_object_copy_.12194
- ___Block_byref_object_copy_.122
- ___Block_byref_object_copy_.128
- ___Block_byref_object_copy_.12924
- ___Block_byref_object_copy_.133
- ___Block_byref_object_copy_.140
- ___Block_byref_object_copy_.143
- ___Block_byref_object_copy_.14357
- ___Block_byref_object_copy_.147
- ___Block_byref_object_copy_.1787
- ___Block_byref_object_copy_.1922
- ___Block_byref_object_copy_.3701
- ___Block_byref_object_copy_.4393
- ___Block_byref_object_copy_.5845
- ___Block_byref_object_copy_.7585
- ___Block_byref_object_copy_.79
- ___Block_byref_object_copy_.806
- ___Block_byref_object_copy_.82
- ___Block_byref_object_copy_.86
- ___Block_byref_object_copy_.92
- ___Block_byref_object_copy_.98
- ___Block_byref_object_dispose_.105
- ___Block_byref_object_dispose_.111
- ___Block_byref_object_dispose_.118
- ___Block_byref_object_dispose_.12195
- ___Block_byref_object_dispose_.123
- ___Block_byref_object_dispose_.129
- ___Block_byref_object_dispose_.12925
- ___Block_byref_object_dispose_.134
- ___Block_byref_object_dispose_.141
- ___Block_byref_object_dispose_.14358
- ___Block_byref_object_dispose_.144
- ___Block_byref_object_dispose_.148
- ___Block_byref_object_dispose_.1788
- ___Block_byref_object_dispose_.1923
- ___Block_byref_object_dispose_.3702
- ___Block_byref_object_dispose_.4394
- ___Block_byref_object_dispose_.5846
- ___Block_byref_object_dispose_.7586
- ___Block_byref_object_dispose_.80
- ___Block_byref_object_dispose_.807
- ___Block_byref_object_dispose_.83
- ___Block_byref_object_dispose_.87
- ___Block_byref_object_dispose_.93
- ___Block_byref_object_dispose_.99
- ___Synchronously_block_invoke
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.12772
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.12910
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.13061
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.13987
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.2089
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.2674
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.3838
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.5261
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.6103
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.6531
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.8655
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.9465
- ____Z27AudioQueueInternalStop_Syncj_block_invoke
- ____Z28AudioStatisticsLibraryLoaderv_block_invoke.12362
- ____Z28AudioStatisticsLibraryLoaderv_block_invoke.2697
- ____Z28AudioStatisticsLibraryLoaderv_block_invoke.8956
- ____Z28CMClientNotificationCallbackP26opaqueCMNotificationCenterPKvPK10__CFStringS2_S2__block_invoke.36
- ____ZL15CPMSLibraryCorePPc_block_invoke.10607
- ____ZL15CPMSLibraryCorePPc_block_invoke.3540
- ____ZL15CPMSLibraryCorePPc_block_invoke.6499
- ____ZL17getCPMSAgentClassv_block_invoke.3510
- ____ZL17getCPMSAgentClassv_block_invoke.6497
- ____ZL19AVFAudioLibraryCorePPc_block_invoke.12841
- ____ZL20CoreMediaLibraryCorePPc_block_invoke.5192
- ____ZL20CoreMediaLibraryCorePPc_block_invoke.7258
- ____ZL21GetSpatialMetadataSPIv_block_invoke.11738
- ____ZL21getAVAudioFormatClassv_block_invoke.12081
- ____ZL23MediaToolboxLibraryCorePPc_block_invoke.7250
- ____ZL29AudioSessionServerLibraryCorePPc_block_invoke.8498
- ____ZL29getCPMSClientDescriptionClassv_block_invoke.3519
- ____ZL33getCMBaseObjectGetVTableSymbolLocv_block_invoke.5188
- ____ZL33getCMBaseObjectGetVTableSymbolLocv_block_invoke.7255
- ____ZL58getFigCPECryptorCreateCryptorFromSerializedRecipeSymbolLocv_block_invoke.7246
- ____ZN11ClientEntry16unduckOtherAudioEm_block_invoke
- ____ZN13HapticMetricsC2Ev_block_invoke
- ____ZN13HapticMetricsC2Ev_block_invoke_2
- ____ZN13ServerManager23setClientPlayerBehaviorENSt3__110shared_ptrI11ClientEntryEEmb_block_invoke
- ____ZN16AudioQueueObject26IONode_ConfigAboutToChangeEv_block_invoke
- ____ZN16AudioQueueObject26IONode_ConfigAboutToChangeEv_block_invoke_2
- ____ZN17LegacyHapticSynth25hardwareSampleRateChangedER11SynthOutput_block_invoke
- ____ZN20AudioQueueXPC_Bridge5StartEj19XAudioTimeStampBasej_block_invoke
- ____ZN20AudioQueueXPC_Server5StartEj19XAudioTimeStampBasej_block_invoke
- ____ZN21ThreadSafeHeadTracker10InitializeEv_block_invoke.80
- ____ZN21ThreadSafeHeadTracker10InitializeEv_block_invoke.84
- ____ZN21ThreadSafeHeadTracker10InitializeEv_block_invoke.90
- ____ZN22MultiOutputHapticSynth25hardwareSampleRateChangedER11SynthOutput_block_invoke
- ____ZN24AVVoiceTriggerServerImpl10InitializeEv_block_invoke.310
- ____ZN24AVVoiceTriggerServerImpl10InitializeEv_block_invoke.312
- ____ZN24AVVoiceTriggerServerImpl10InitializeEv_block_invoke_2.313
- ____ZN2AQ3API6V2Impl32ATAudioProcessingNodeInstantiateEP16OpaqueAudioQueuePK25AudioComponentDescriptionjPP27OpaqueATAudioProcessingNode_block_invoke_2
- ____ZN2AT11Translation16TranslatorClient53getSTSpeechTranslatorClientsPreferredInputAudioFormatEv_block_invoke
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.10884
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.11727
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.13707
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.2115
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.2968
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.3321
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.5016
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.7193
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.7716
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.8782
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.9855
- ____ZN2AT13DispatchBlockEPU28objcproto17OS_dispatch_queue8NSObjectU13block_pointerFvvEbPKcS6_iyy_block_invoke.7209
- ____ZN5Phase13ServerManager5startEv_block_invoke.30
- ___block_descriptor_120_ea8_32s40s48s56r64r72c25_ZTS19SSClientPlayOptions_e17_v16?0"NSError"8l
- ___block_descriptor_40_ea8_32s_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_40_ea8_32w_e17_v16?0"NSError"8lw32l8
- ___block_descriptor_48_e5_v8?0l
- ___block_descriptor_48_ea8_32r40w_e5_v8?0lw40l8r32l8
- ___block_descriptor_56_ea8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_65_ea8_32r48c39_ZTSNSt3__110shared_ptrI11ClientEntryEE_e5_v8?0l
- ___block_descriptor_tmp
- ___block_descriptor_tmp.1.12951
- ___block_descriptor_tmp.10.10901
- ___block_descriptor_tmp.10.13047
- ___block_descriptor_tmp.10.5112
- ___block_descriptor_tmp.101
- ___block_descriptor_tmp.102.14366
- ___block_descriptor_tmp.106
- ___block_descriptor_tmp.10690
- ___block_descriptor_tmp.107
- ___block_descriptor_tmp.10880
- ___block_descriptor_tmp.109.14365
- ___block_descriptor_tmp.11.10906
- ___block_descriptor_tmp.11.11885
- ___block_descriptor_tmp.11.3352
- ___block_descriptor_tmp.112
- ___block_descriptor_tmp.112.14364
- ___block_descriptor_tmp.113
- ___block_descriptor_tmp.113.14363
- ___block_descriptor_tmp.114.14362
- ___block_descriptor_tmp.11587
- ___block_descriptor_tmp.119
- ___block_descriptor_tmp.120
- ___block_descriptor_tmp.1209
- ___block_descriptor_tmp.124
- ___block_descriptor_tmp.124.14359
- ___block_descriptor_tmp.125
- ___block_descriptor_tmp.12557
- ___block_descriptor_tmp.12704
- ___block_descriptor_tmp.12770
- ___block_descriptor_tmp.12940
- ___block_descriptor_tmp.130
- ___block_descriptor_tmp.13078
- ___block_descriptor_tmp.13305
- ___block_descriptor_tmp.135
- ___block_descriptor_tmp.136
- ___block_descriptor_tmp.13704
- ___block_descriptor_tmp.142
- ___block_descriptor_tmp.14369
- ___block_descriptor_tmp.1447
- ___block_descriptor_tmp.145
- ___block_descriptor_tmp.146
- ___block_descriptor_tmp.149
- ___block_descriptor_tmp.15.11867
- ___block_descriptor_tmp.150
- ___block_descriptor_tmp.1623
- ___block_descriptor_tmp.179
- ___block_descriptor_tmp.179.9463
- ___block_descriptor_tmp.180
- ___block_descriptor_tmp.181
- ___block_descriptor_tmp.182
- ___block_descriptor_tmp.184
- ___block_descriptor_tmp.184.8745
- ___block_descriptor_tmp.185
- ___block_descriptor_tmp.186
- ___block_descriptor_tmp.189
- ___block_descriptor_tmp.19
- ___block_descriptor_tmp.1924
- ___block_descriptor_tmp.2.10881
- ___block_descriptor_tmp.209
- ___block_descriptor_tmp.210
- ___block_descriptor_tmp.2102
- ___block_descriptor_tmp.2112
- ___block_descriptor_tmp.22
- ___block_descriptor_tmp.23
- ___block_descriptor_tmp.231
- ___block_descriptor_tmp.259
- ___block_descriptor_tmp.26
- ___block_descriptor_tmp.26.5348
- ___block_descriptor_tmp.26.9856
- ___block_descriptor_tmp.2648
- ___block_descriptor_tmp.275
- ___block_descriptor_tmp.29
- ___block_descriptor_tmp.2966
- ___block_descriptor_tmp.3.1918
- ___block_descriptor_tmp.3.5040
- ___block_descriptor_tmp.3.5344
- ___block_descriptor_tmp.3.6070
- ___block_descriptor_tmp.3.7149
- ___block_descriptor_tmp.304
- ___block_descriptor_tmp.308
- ___block_descriptor_tmp.3252
- ___block_descriptor_tmp.3334
- ___block_descriptor_tmp.38.5506
- ___block_descriptor_tmp.3836
- ___block_descriptor_tmp.4.5020
- ___block_descriptor_tmp.40
- ___block_descriptor_tmp.43
- ___block_descriptor_tmp.48
- ___block_descriptor_tmp.492
- ___block_descriptor_tmp.497
- ___block_descriptor_tmp.5.10895
- ___block_descriptor_tmp.5.9110
- ___block_descriptor_tmp.501
- ___block_descriptor_tmp.5022
- ___block_descriptor_tmp.505
- ___block_descriptor_tmp.509
- ___block_descriptor_tmp.5172
- ___block_descriptor_tmp.5259
- ___block_descriptor_tmp.53.11823
- ___block_descriptor_tmp.5341
- ___block_descriptor_tmp.5530
- ___block_descriptor_tmp.57
- ___block_descriptor_tmp.6.10897
- ___block_descriptor_tmp.6.3326
- ___block_descriptor_tmp.6.5013
- ___block_descriptor_tmp.6.5293
- ___block_descriptor_tmp.6057
- ___block_descriptor_tmp.6193
- ___block_descriptor_tmp.64
- ___block_descriptor_tmp.6529
- ___block_descriptor_tmp.67
- ___block_descriptor_tmp.6885
- ___block_descriptor_tmp.7.10898
- ___block_descriptor_tmp.7.11882
- ___block_descriptor_tmp.7.3319
- ___block_descriptor_tmp.7.9112
- ___block_descriptor_tmp.7031
- ___block_descriptor_tmp.7145
- ___block_descriptor_tmp.7190
- ___block_descriptor_tmp.7259
- ___block_descriptor_tmp.73
- ___block_descriptor_tmp.7587
- ___block_descriptor_tmp.7713
- ___block_descriptor_tmp.799
- ___block_descriptor_tmp.8.10899
- ___block_descriptor_tmp.8.13046
- ___block_descriptor_tmp.8.13708
- ___block_descriptor_tmp.8.2969
- ___block_descriptor_tmp.8.3337
- ___block_descriptor_tmp.8.6209
- ___block_descriptor_tmp.8061
- ___block_descriptor_tmp.81.14368
- ___block_descriptor_tmp.8230
- ___block_descriptor_tmp.84
- ___block_descriptor_tmp.85
- ___block_descriptor_tmp.8664
- ___block_descriptor_tmp.88
- ___block_descriptor_tmp.9.10900
- ___block_descriptor_tmp.9.3345
- ___block_descriptor_tmp.9.7194
- ___block_descriptor_tmp.9108
- ___block_descriptor_tmp.94.14367
- ___block_descriptor_tmp.9525
- ___block_descriptor_tmp.9873
- ___block_literal_global.10
- ___block_literal_global.10114
- ___block_literal_global.10242
- ___block_literal_global.10686
- ___block_literal_global.10917
- ___block_literal_global.11585
- ___block_literal_global.116
- ___block_literal_global.12170
- ___block_literal_global.12346
- ___block_literal_global.12555
- ___block_literal_global.12766
- ___block_literal_global.12905
- ___block_literal_global.12938
- ___block_literal_global.13074
- ___block_literal_global.13298
- ___block_literal_global.13983
- ___block_literal_global.175
- ___block_literal_global.186
- ___block_literal_global.188
- ___block_literal_global.2099
- ___block_literal_global.21
- ___block_literal_global.212
- ___block_literal_global.233
- ___block_literal_global.261
- ___block_literal_global.2694
- ___block_literal_global.277
- ___block_literal_global.3.12949
- ___block_literal_global.3.6195
- ___block_literal_global.3212
- ___block_literal_global.3350
- ___block_literal_global.3446
- ___block_literal_global.3513
- ___block_literal_global.359
- ___block_literal_global.3833
- ___block_literal_global.3886
- ___block_literal_global.453
- ___block_literal_global.494
- ___block_literal_global.499
- ___block_literal_global.50
- ___block_literal_global.5012
- ___block_literal_global.503
- ___block_literal_global.507
- ___block_literal_global.511
- ___block_literal_global.5167
- ___block_literal_global.5213
- ___block_literal_global.5256
- ___block_literal_global.5342
- ___block_literal_global.5435
- ___block_literal_global.5604
- ___block_literal_global.561
- ___block_literal_global.5633
- ___block_literal_global.5668
- ___block_literal_global.6.9200
- ___block_literal_global.6099
- ___block_literal_global.6191
- ___block_literal_global.627
- ___block_literal_global.6291
- ___block_literal_global.6524
- ___block_literal_global.7025
- ___block_literal_global.71
- ___block_literal_global.713
- ___block_literal_global.7143
- ___block_literal_global.741
- ___block_literal_global.7480
- ___block_literal_global.7610
- ___block_literal_global.8057
- ___block_literal_global.8194
- ___block_literal_global.846
- ___block_literal_global.8650
- ___block_literal_global.9190
- ___block_literal_global.9456
- ___block_literal_global.96
- ___block_literal_global.9945
- ___copy_helper_block_e8_40c36_ZTSNSt3__18weak_ptrI11SynthOutputEE
- ___copy_helper_block_e8_56c31_ZTSN10applesauce2CF9StringRefE64c31_ZTSN10applesauce3xpc8endpointE
- ___copy_helper_block_ea8_72c25_ZTS19SSClientPlayOptions
- ___destroy_helper_block_e8_40c36_ZTSNSt3__18weak_ptrI11SynthOutputEE
- ___destroy_helper_block_e8_56c31_ZTSN10applesauce2CF9StringRefE64c31_ZTSN10applesauce3xpc8endpointE
- ___destroy_helper_block_ea8_72c25_ZTS19SSClientPlayOptions
- ___kCFBooleanFalse
- __dispatch_queue_attr_concurrent
- _dispatch_barrier_async
- _mach_wait_until
- _objc_msgSend$absoluteString
- _objc_msgSend$createAdvancedPlayerWithPattern:error:
- _objc_msgSend$createAdvancedPlayerWithVibePatternDictionary:error:
- _objc_msgSend$createAudioPlayerAndReturnError:
- _objc_msgSend$createAudioResource:error:
- _objc_msgSend$createHapticPlayer:error:
- _objc_msgSend$currentTime
- _objc_msgSend$dataWithContentsOfFile:
- _objc_msgSend$defaultCStringEncoding
- _objc_msgSend$disposeSSID:
- _objc_msgSend$doInit:haptic:error:
- _objc_msgSend$earlyUnduckAudioAtTime:error:
- _objc_msgSend$generateNewSSIDForPlayer:
- _objc_msgSend$getDurationForResource:
- _objc_msgSend$getHapticDictionaryFromURL:
- _objc_msgSend$getPlayerForSSID:
- _objc_msgSend$handleFinish
- _objc_msgSend$initWithAudio:hapticDictionary:error:
- _objc_msgSend$initWithAudioResourceID:parameters:relativeTime:duration:
- _objc_msgSend$initWithEvents:parameters:error:
- _objc_msgSend$initWithMaster:id:connection:outError:
- _objc_msgSend$instance
- _objc_msgSend$isEqualToDictionary:
- _objc_msgSend$isFileURL
- _objc_msgSend$master
- _objc_msgSend$path
- _objc_msgSend$pathExtension
- _objc_msgSend$playWithOptions:completionCallbackToken:error:
- _objc_msgSend$prepareHapticPatternFromPlayOptions:
- _objc_msgSend$prewarm:
- _objc_msgSend$prewarmWithCompletionHandler:
- _objc_msgSend$registerAudioResource:options:error:
- _objc_msgSend$registerCompletionAndStop
- _objc_msgSend$registerCompletionPortion:
- _objc_msgSend$registerSSID:withPlayer:
- _objc_msgSend$removeObjectForKey:
- _objc_msgSend$sendParameters:atTime:error:
- _objc_msgSend$setCompletionHandler:
- _objc_msgSend$setFollowAudioRoute:
- _objc_msgSend$setLoopEnabled:
- _objc_msgSend$setLoopEnd:
- _objc_msgSend$setResetHandler:
- _objc_msgSend$setupDefaultEngineConfigBlock
- _objc_msgSend$setupLooping
- _objc_msgSend$shouldUnprewarmAllClientsAfterDisplayingPrewarmedProcessEntriesWithPrewarmTime:
- _objc_msgSend$ssid
- _objc_msgSend$startAtTime:error:
- _objc_msgSend$startPlayerAtTime:forAudio:error:
- _objc_msgSend$startWithCompletionHandler:
- _objc_msgSend$stop:
- _objc_msgSend$stopWithCompletionHandler:
- _objc_msgSend$stringWithCString:encoding:
- _objc_msgSend$unprewarmAllClientEntries
- _objc_msgSend$unregisterAudioResource:error:
- _objc_msgSend$unregisterSSID:
- _objc_release_x10
- _vdprintf
CStrings:
+ "\tAudio on-time: %.1f seconds\n"
+ "\tAudio prewarm-time: %.1f seconds\n"
+ "\tHaptics prewarm-time: %.1f seconds\n"
+ " (AllClientEntries)"
+ " does not allow the "
+ " formatting argument"
+ " option"
+ "%25s:%-5d      EnhanceDialogue processor failed to initialize (err = %d), keeping out of chain"
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
+ "%25s:%-5d %s failed: 0x%x (%s)"
+ "%25s:%-5d %s failed: errno %d"
+ "%25s:%-5d %s is deallocating notification port (0x%x) because a new notification port has been registered."
+ "%25s:%-5d %s: %@ but haptic AutoBugCapture has filed within 24 hours"
+ "%25s:%-5d %s: %s device abnormally stopped from below. Stopping client 0x%lx because run mode includes %s"
+ "%25s:%-5d %s: %s format changed for clientID 0x%x%s"
+ "%25s:%-5d %s: %s side for clientID 0x%x%s is already initialized!"
+ "%25s:%-5d %s: %s side for clientID 0x%x%s is already uninitialized!"
+ "%25s:%-5d %s: %s side, for clientID 0x%x%s"
+ "%25s:%-5d %s: %s volume changed for clientID 0x%x%s"
+ "%25s:%-5d %s: <- encountered a fatal error connecting to remote AU (%s): %d"
+ "%25s:%-5d %s: << %@. Filing ABC >>"
+ "%25s:%-5d %s: <RT> <RTMessenger thread callback> Calling notifyFinished(stopped=false) from within client finish callback"
+ "%25s:%-5d %s: <RT> <RTMessenger thread callback> Calling notifyFinished(stopped=true) from within client ID 0x%x finish callback"
+ "%25s:%-5d %s: <RT> <RTMessenger thread callback> Client already destroyed -- noop"
+ "%25s:%-5d %s: <RT> <RTMessenger thread callback> DONE"
+ "%25s:%-5d %s: <RT> Attempting to flush starting or stopped client"
+ "%25s:%-5d %s: <RT> Channel voice count: %u"
+ "%25s:%-5d %s: <RT> ClientEntry for client ID 0x%x is invalid! Num of clients in mClientMap: %u"
+ "%25s:%-5d %s: <RT> CompleteTimestamp failed - bailing out"
+ "%25s:%-5d %s: <RT> ERROR converting param curve points to AU parameter events. result: %d"
+ "%25s:%-5d %s: <RT> ERROR: Real-time component threw exception - treating as fatal error"
+ "%25s:%-5d %s: <RT> ERROR: incoming haptic command has invalid size of %u bytes (expected at most %u bytes), clearing pending commands to recover"
+ "%25s:%-5d %s: <RT> Force-stopping sequence %p"
+ "%25s:%-5d %s: <RT> Found StartParamCurveList outside of event list!"
+ "%25s:%-5d %s: <RT> Illegal HapticCommandType: %u"
+ "%25s:%-5d %s: <RT> Illegal StartEventList within list!"
+ "%25s:%-5d %s: <RT> Illegal StartParamCurveList within list!"
+ "%25s:%-5d %s: <RT> Illegal command type: %u"
+ "%25s:%-5d %s: <RT> Illegal playback rate"
+ "%25s:%-5d %s: <RT> Invalid synth channel ID: %u"
+ "%25s:%-5d %s: <RT> MusicPlayerGetTime returned %d"
+ "%25s:%-5d %s: <RT> MusicPlayerSetPlayRateScalar returned %d"
+ "%25s:%-5d %s: <RT> MusicPlayerSetTime returned %d"
+ "%25s:%-5d %s: <RT> MusicPlayerStart returned %d"
+ "%25s:%-5d %s: <RT> MusicSequenceGetBeatsForSeconds returned %d"
+ "%25s:%-5d %s: <RT> MusicSequenceGetIndTrack returned %d"
+ "%25s:%-5d %s: <RT> MusicSequenceGetMaxTrackLength returned %d"
+ "%25s:%-5d %s: <RT> MusicTrackGetProperty returned %d"
+ "%25s:%-5d %s: <RT> MusicTrackSetProperty returned %d"
+ "%25s:%-5d %s: <RT> No registered channel at index %u"
+ "%25s:%-5d %s: <RT> Playing one haptic with intensity 0 to warm up memory"
+ "%25s:%-5d %s: <RT> SequenceRTAccessor::getEventInfo returned %d"
+ "%25s:%-5d %s: <RT> SequenceRTAccessor::nextEvent returned %d"
+ "%25s:%-5d %s: <RT> SequenceRTAccessor::setEventTime returned %d"
+ "%25s:%-5d %s: <RT> Set automation track %u t=0 point value to %.3f, based on calculated value at t=iterationEndTime (%.2f beats)"
+ "%25s:%-5d %s: <RT> Stopping all sequences in active list"
+ "%25s:%-5d %s: <RT> Unknown parameter: %u"
+ "%25s:%-5d %s: <RT> WARNING: Fetch for %s ring buffer end sample %lld > buffer range [%ld - %ld]"
+ "%25s:%-5d %s: <RT> WARNING: Fetch for %s ring buffer start sample %lld < buffer range [%ld - %ld]"
+ "%25s:%-5d %s: <RT> WARNING: Fetch from %s ring buffer returned err %d"
+ "%25s:%-5d %s: <RT> WARNING: Illegal AddParamCurve (adjusted time %.3lf, type %u) -- has different paramID %u than expected paramID %u! Skipping"
+ "%25s:%-5d %s: <RT> WARNING: Render thread error: %d - File radar with haptics team"
+ "%25s:%-5d %s: <RT> WARNING: Store to %s ring buffer returned err %d"
+ "%25s:%-5d %s: <RT> WARNING: client ID: 0x%x cannot enqueue RT command %u - not running"
+ "%25s:%-5d %s: <RT> WARNING: client ID: 0x%x neither stopping nor !stopped"
+ "%25s:%-5d %s: <RT> WARNING: failed to set parameter on AU: err %d"
+ "%25s:%-5d %s: <RT> WARNING: failed to start event on AU: err %d"
+ "%25s:%-5d %s: <RT> WARNING: frame count (%u) exceeds %u -- returning silence"
+ "%25s:%-5d %s: <RT> WARNING: mRenderLock lock held -- returning silence"
+ "%25s:%-5d %s: <RT> _rtFinishedCallback is NULL"
+ "%25s:%-5d %s: <RT> channel %u, mute=%d - behavior set to not mute - noop"
+ "%25s:%-5d %s: <RT> channel: %u mute: %d ramp: %.3f secs"
+ "%25s:%-5d %s: <RT> client ID 0x%x state: %s => %s"
+ "%25s:%-5d %s: <RT> client ID: 0x%x"
+ "%25s:%-5d %s: <RT> client ID: 0x%x is %s"
+ "%25s:%-5d %s: <RT> client ID: 0x%x, detaching sequence ID %u"
+ "%25s:%-5d %s: <RT> client ID: 0x%x, inRenderTime %.4f"
+ "%25s:%-5d %s: <RT> client ID: 0x%x, sequence ID %u, loop %d"
+ "%25s:%-5d %s: <RT> client ID: 0x%x, sequence ID %u, loop length %f seconds"
+ "%25s:%-5d %s: <RT> client ID: 0x%x, sequence ID %u, rate %f"
+ "%25s:%-5d %s: <RT> client ID: 0x%x, stopping sequence ID %u"
+ "%25s:%-5d %s: <RT> client ID: 0x%x: flush wait time: %.3f seconds"
+ "%25s:%-5d %s: <RT> getAutomationValueAtTime returned %d"
+ "%25s:%-5d %s: <RT> parameter curve has only 1 control point - setting this parameter instead"
+ "%25s:%-5d %s: <RT> preRender: sequence play failed for Sequence ID %u"
+ "%25s:%-5d %s: <RT> preRender::play failed for Sequence ID %u with offset %f seconds"
+ "%25s:%-5d %s: <RT> setEventInfo returned %d"
+ "%25s:%-5d %s: <RT> synchronizer %d is ready to play with offset of %d"
+ "%25s:%-5d %s: <RT> synchronizer %d is ready to play with zero offset"
+ "%25s:%-5d %s: <RT> zero length param curve - ignoring"
+ "%25s:%-5d %s: Average power budget range not found or invalid in CPMS response"
+ "%25s:%-5d %s: Background-running client idle timeout: attempting to force stop client ID 0x%lx (began idling %.0f seconds ago, entered background %.0f seconds ago)"
+ "%25s:%-5d %s: Cannot configure audio output for clientID 0x%x%s. Error %d"
+ "%25s:%-5d %s: Client ID 0x%x from PID %d (%s) is hosted in an external daemon, marked for daemon idle timeout"
+ "%25s:%-5d %s: Client prewarm timeout: attempting to force unprewarm client ID 0x%lx (last started prewarm %.0f seconds ago)"
+ "%25s:%-5d %s: Daemon client idle timeout: attempting to force stop client ID 0x%lx (last started or finished %.0f seconds ago)"
+ "%25s:%-5d %s: Device has no hardware name. Not loading per-product tuning"
+ "%25s:%-5d %s: Device stopped from below. DeviceStoppedAbnormally? %i"
+ "%25s:%-5d %s: ERROR: Allocating mSynthBuffer for %s side clientID 0x%x%s failed!"
+ "%25s:%-5d %s: ERROR: Allocating mSynthRingBuffer for %s side clientID 0x%x%s failed!"
+ "%25s:%-5d %s: ERROR: Failed to determine whether process with PID %d (%s) is a daemon or agent"
+ "%25s:%-5d %s: ERROR: Haptic server is nil - cannot stop!"
+ "%25s:%-5d %s: ERROR: Server instance for client ID 0x%lx identified as running-in-background but client had no onset time recorded"
+ "%25s:%-5d %s: ERROR: Unable to load per-product tuning %@, err %@"
+ "%25s:%-5d %s: ERROR: Unable to load the configuration plist: Product has neither Acoustic ID nor product short name"
+ "%25s:%-5d %s: ERROR: Unable to load the configuration plist: err %@"
+ "%25s:%-5d %s: EngineOnDuration - ApplicationName = %@, EngineOnDuration = %fs"
+ "%25s:%-5d %s: Failed to get power policy from CPMS API, error: %@"
+ "%25s:%-5d %s: Failed to set average power budget range: min=%u, max=%u, error=0x%x"
+ "%25s:%-5d %s: Failed to set peak power budget range: min=%u, max=%u, error=0x%x"
+ "%25s:%-5d %s: Found existing deactivated audio synth output for client ID 0x%x, updating audio session"
+ "%25s:%-5d %s: HapticAudioRunningCount - RunningCount = %lu, pid = %d, ActiveProcesses = \"%@\""
+ "%25s:%-5d %s: HapticForceStop - reason = %d, pid = %d, subsystem = %lu, process = %@"
+ "%25s:%-5d %s: HapticServer AutoBugCapture filed. Starting cooldown of %.1f hours"
+ "%25s:%-5d %s: HapticsPrewarmCount - PrewarmCount = %lu, pid = %d, process = %@"
+ "%25s:%-5d %s: HapticsRunningCount - RunningCount = %lu, pid = %d, ActiveProcesses = \"%@\""
+ "%25s:%-5d %s: IOServiceOpen failed with error: 0x%08X"
+ "%25s:%-5d %s: Interval-based start after pause: mHostTime=%lld interval=%lld intervals=%f"
+ "%25s:%-5d %s: Interval-based start: mHostTime=%lld interval=%lld maxIntervals=%lld"
+ "%25s:%-5d %s: Invalid userInfo or AVServerWrapper instance!"
+ "%25s:%-5d %s: Loading using product short name: '%@'"
+ "%25s:%-5d %s: Missing min/max values for time scale: %@"
+ "%25s:%-5d %s: NULL preset dictionary"
+ "%25s:%-5d %s: No HapticEngine per-product tuning needed for '%@'"
+ "%25s:%-5d %s: No valid power budgets received from CPMS API"
+ "%25s:%-5d %s: Output pointer is null - noop"
+ "%25s:%-5d %s: Peak power budget range not found or invalid in CPMS response"
+ "%25s:%-5d %s: PreflightOfflineRender aq@%p - failed to query InputPullAheadFrameCount."
+ "%25s:%-5d %s: PreflightOfflineRender aq@%p clientSampleRate %f mixerSampleRate %f inCurrentSampleTime: %lld anchor: %lld queueTimeScaled: %lld framesAvailable(scaled): %lld decodedFrames(unscaled): %lld framesRequired(scaled): %lld framesRequired(unscaled): %lld done decoding: %d recentRenderEndTime(unscaled): %lld scaledLastRenderTime: %lld currentEndOfTimeline(unscaled): %lld scaledEndOfTimeline: %lld mOfflineEndOfStreamSampleTime= %lld unscaledInputSampleTime=%lld pullAheadFramesUnscaled=%u pullAheadFramesScaled=%u sspFramesRemaining=%lld unflushedSamplesFromTimePitch: %lld "
+ "%25s:%-5d %s: Product Acoustic ID: '%@'"
+ "%25s:%-5d %s: Received MX SystemVolumeDidChange notification. Actively querying VAD volume now. %@"
+ "%25s:%-5d %s: Set average power budget range: min=%u, max=%u"
+ "%25s:%-5d %s: Set peak power budget range: min=%u, max=%u"
+ "%25s:%-5d %s: Since sequence with ID %u was not in active list, falling back to sequence map query in messenger lambda"
+ "%25s:%-5d %s: StartRunning: this = %p, prewarmed: %d running: %d haptic: %d, sessionID: %u(0x%x), clientID: 0x%x%s synchronizer: %p"
+ "%25s:%-5d %s: StartRunning: this = %p, session category %s, mode %s"
+ "%25s:%-5d %s: StopRunning: this = %p, running: %d haptic: %d, bus: %u, for clientID 0x%x%s"
+ "%25s:%-5d %s: Stopping running %s%s%s for client ID: 0x%lx"
+ "%25s:%-5d %s: Successfully opened IOService connection"
+ "%25s:%-5d %s: SynthOutput(%s) this = %p, sessionID: %u(0x%x), for client ID 0x%x%s, mRoutingBehavior: %s"
+ "%25s:%-5d %s: SystemSoundsAndHaptics volume is now: %.2f"
+ "%25s:%-5d %s: WARNING: Server is already nil - no call to stop prewarm or running possible"
+ "%25s:%-5d %s: XMachServer couldn't cancel port-death notification (0x%x)"
+ "%25s:%-5d %s: XMachServer couldn't request port-death notification (0x%x)"
+ "%25s:%-5d %s: aq@%p Destroying AudioQueueObject with present mIONodeConnection"
+ "%25s:%-5d %s: aq@%p: %d (disposing=%d)"
+ "%25s:%-5d %s: aq@%p: IONode_DeviceStoppedFromBelow"
+ "%25s:%-5d %s: aq@%p: OfflineFOA metadata set (size %ld)"
+ "%25s:%-5d %s: aq@%p: OfflineFOA: %s"
+ "%25s:%-5d %s: found default dictionary for route"
+ "%25s:%-5d %s: looking for hardware platform: %s"
+ "%25s:%-5d %s: looking for late night / soundcheck key: %s"
+ "%25s:%-5d %s: looking for route: %s"
+ "%25s:%-5d %s: no dictionary (or default) for encoder OS version: %s %d.%d"
+ "%25s:%-5d %s: no dictionary for encoder OS type: %s"
+ "%25s:%-5d %s: no dictionary for hw platform: %s"
+ "%25s:%-5d %s: no dictionary for media type: %s"
+ "%25s:%-5d %s: no dictionary for route: %s"
+ "%25s:%-5d %s: protectionStrategy: %u"
+ "%25s:%-5d %s: server side metrics %s"
+ "%25s:%-5d %s: this = %p, haptic: %d, clientID: 0x%x%s, prewarmed: %d"
+ "%25s:%-5d %s: this = %p, setting volume to %.2f"
+ "%25s:%-5d ->%s"
+ "%25s:%-5d ->%s %p"
+ "%25s:%-5d 3rd party spatial AU component description: with type=%s, subType=%s, manufacturer=%s, flags=0x%X, flagsMask=0x%X"
+ "%25s:%-5d <-%s %p"
+ "%25s:%-5d <-%s %p: Swallowed exception from Close()"
+ "%25s:%-5d ================= InterruptionEndedAfterActivationError %s ================="
+ "%25s:%-5d AQAC3IONode::AQAC3IONode() failed to create IO unit (%d)"
+ "%25s:%-5d AQMEDevice: couldn't initialize processor with id: %s err: %d"
+ "%25s:%-5d AQMixEngine_Base::DebugPrintFrom: ForAllDevices threw std::exception: %s"
+ "%25s:%-5d AQMixEngine_Base::DebugPrintFrom: ForAllDevices threw unknown exception"
+ "%25s:%-5d ATATranslationClient@%p: created client for scope %s"
+ "%25s:%-5d ATATranslatorClientDelegate::didGenerateTranslatedAudio; scope: %s"
+ "%25s:%-5d AUSpatializationHost [3PSpatialAU] deviceUID is null"
+ "%25s:%-5d AUSpatializationHost [chain] bypass mode entered"
+ "%25s:%-5d Apple device detected - no external component needed"
+ "%25s:%-5d AudioFileReadPacketData: mDataSize %u, mPacketCount %u, result %d"
+ "%25s:%-5d Bluetooth spatial audio is not enabled for this port"
+ "%25s:%-5d Both frameworks available; using %s based on feature flag"
+ "%25s:%-5d ConfigureStreamFormats (%p): AudioUnit is not valid"
+ "%25s:%-5d ConfigureStreamFormats (%p): Failed to set input element count, error %d"
+ "%25s:%-5d ConfigureStreamFormats (%p): Failed to set input format, error %d"
+ "%25s:%-5d ConfigureStreamFormats (%p): Failed to set output element count, error %d"
+ "%25s:%-5d ConfigureStreamFormats (%p): Failed to set output format, error %d"
+ "%25s:%-5d ConfigureStreamFormats (%p): Invalid input channel count %u (expected %u)"
+ "%25s:%-5d ConfigureStreamFormats (%p): configured (%uch -> %uch)"
+ "%25s:%-5d ConfigureStreamFormats (%p): input format %s"
+ "%25s:%-5d CoreAudioOrchestration framework is not available"
+ "%25s:%-5d CreatePasscodeDetectorClientPortal not found in CoreAudioOrchestration - a newer version of CoreAudioOrchestration may be needed!"
+ "%25s:%-5d Device stopped from below. DeviceStoppedAbnormally? %i"
+ "%25s:%-5d ERROR: Haptics stream stopped abnormally! Stopping all sounding vibes"
+ "%25s:%-5d EXCEPTION (%d): \"\""
+ "%25s:%-5d EnhanceDialogueProcessor() - Product does not have valid tuning at '%s'"
+ "%25s:%-5d EnhanceDialogueProcessor::Initialize: processor not supported (missing or invalid tuning at '%s'), refusing to initialize"
+ "%25s:%-5d Error %d (%s) getting 3rd party spatial AU component description"
+ "%25s:%-5d Error %d creating AQAC3IONode for binding: %s"
+ "%25s:%-5d ExtractAcousticID: AcousticID key not found in metadata"
+ "%25s:%-5d ExtractAcousticID: Failed to parse metadata as dictionary"
+ "%25s:%-5d Failed to create ATATranslationClient from UUID %s"
+ "%25s:%-5d Failed to get active output port, err = %d"
+ "%25s:%-5d Failed to get port UUID, err = %d"
+ "%25s:%-5d Failed to set AUSpatialMixer into external speaker mode: %d"
+ "%25s:%-5d GetTuningDirectory (%p): Failed to extract AcousticID from metadata"
+ "%25s:%-5d GetTuningDirectory (%p): No metadata set"
+ "%25s:%-5d GetTuningDirectory (%p): Tuning directory does not exist: %s"
+ "%25s:%-5d GetTuningDirectory (%p): Using tuning path: %s"
+ "%25s:%-5d Getting kAudioFormatProperty_MatrixMixMap failed, err = %d, using identity matrix"
+ "%25s:%-5d Handling config change"
+ "%25s:%-5d Initialize (%p): Already initialized, skipping"
+ "%25s:%-5d Initialize (%p): AudioUnit is not valid"
+ "%25s:%-5d Initialize (%p): FOA processor initialized successfully"
+ "%25s:%-5d Initialize (%p): XAudioUnit::Initialize() failed, error %d"
+ "%25s:%-5d InputConverter: AudioBufferList sizes don't match: %u != %u"
+ "%25s:%-5d InterruptionEndedAfterActivationError with id %llX"
+ "%25s:%-5d LoadDSPGraph (%p): Failed to load graph, error %d"
+ "%25s:%-5d LoadDSPGraph (%p): Failed to resolve path: %s/%s"
+ "%25s:%-5d LoadDSPGraph (%p): Successfully loaded: %s"
+ "%25s:%-5d LoadStripFile (%p): Failed to parse strip file: %s"
+ "%25s:%-5d LoadStripFile (%p): Failed to set property, error %d"
+ "%25s:%-5d LoadStripFile (%p): Strip file not found: %s/%s"
+ "%25s:%-5d LoadStripFile (%p): Successfully loaded: %s"
+ "%25s:%-5d OfflineFOAProcessor (%p) created"
+ "%25s:%-5d OfflineFOAProcessor (%p) destroyed"
+ "%25s:%-5d Orchestrator portal launched"
+ "%25s:%-5d Port UUID: %s"
+ "%25s:%-5d RemoteIOClient(%p)::~RemoteIOClient exception: %s"
+ "%25s:%-5d RemoteIOClient(%p)::~RemoteIOClient unknown exception"
+ "%25s:%-5d STTranslatorClientDelegate::didGenerateTranslatedAudio; scope: %s"
+ "%25s:%-5d SelectAUStrip (%p): Using %s"
+ "%25s:%-5d SetMetadata (%p): metadata %s (size %ld)"
+ "%25s:%-5d Setting headTracking=%d on third-party head tracking AU"
+ "%25s:%-5d Setting kAudioConverterPropertyChannelMixMap failed, err = %d"
+ "%25s:%-5d Setting kAudioConverterPropertyPerformDownmix failed, err = %d"
+ "%25s:%-5d TranslationClient@%p: Received %d number of samples, abl %lu"
+ "%25s:%-5d TranslationClient@%p: Translate %d number of samples"
+ "%25s:%-5d TranslationClient@%p: lookUpPreferredInputAudioFormatWithCompletionHandler succeeded but format is null!"
+ "%25s:%-5d TranslationClient@%p: lookUpPreferredInputAudioFormatWithCompletionHandler succeeded with format: %s"
+ "%25s:%-5d TranslationClient@%p: lookUpPreferredInputAudioFormatWithCompletionHandler timed out!"
+ "%25s:%-5d TranslationClient@%p: server disconnected"
+ "%25s:%-5d TranslationClient@%p: set state %d"
+ "%25s:%-5d TranslationClient@%p: setting client's produceAudio value to %i for scope %s"
+ "%25s:%-5d TranslationClient@%p: translation did stop with error: %d"
+ "%25s:%-5d Uninitialize (%p): AudioUnit is not valid"
+ "%25s:%-5d Uninitialize (%p): FOA processor uninitialized, error %d"
+ "%25s:%-5d Unrecognized mode: %@"
+ "%25s:%-5d aqmeio@%p * * * * * kAudioDevicePropertyIOStoppedAbnormally fired * * * * * mIOProcStarted: %i"
+ "%25s:%-5d behaviorDict does not contain valid routing information! No-op"
+ "%25s:%-5d bootstrap_check_in(%s) failed: 0x%x; %s"
+ "%25s:%-5d kMETimePitchProperty_InputPullAheadFrameCount: %d, err %d"
+ "%25s:%-5d obj 0x%x, addr %s, qual %d@%p, size %d: %s %s"
+ "%25s:%-5d useCaseID: %s, deviceID: %u"
+ "%25s:%-5d xpc_shmem_map failed"
+ "%@%@"
+ "%@/%@/%@"
+ "%@/%@/%@/%@"
+ "%@/%@/%@/%@/%@"
+ "%c%d%c"
+ "%s %p (%d:%s)"
+ "%s%s:0x%x:%@"
+ "%s/GymKitConnected.caf"
+ "%s/GymKitConnecting.caf"
+ "%s/GymKitDisconnected.caf"
+ "%zu%@"
+ "(notify_register_dispatch(\"com.apple.accessibility.hac.status\", &token, AudioControlQueue(), ^(int token) { AT::ScopedACQBlock scopedACQBlock(\"notify_register_dispatch\", __func__, \"DSP_Routing_VP.cpp\" , 501); do { auto logobj = CALog::LogObjIfEnabled(5, gAQMELogScope); if (logobj) __extension__({ os_log_t _log_tmp = ((logobj)); os_log_type_t _type_tmp = (OS_LOG_TYPE_DEBUG); if (os_log_type_enabled(_log_tmp, _type_tmp)) { __extension__({ _Pragma(\"clang diagnostic push\") _Pragma(\"clang diagnostic ignored \\\"-Wvla\\\"\") _Pragma(\"clang diagnostic error \\\"-Wformat\\\"\") _Static_assert(__builtin_constant_p(\"%25s:%-5d \" \"HACStatusChanged %p\"), \"format/label/description argument must be a string constant\"); __attribute__((section(\"__TEXT,__oslogstring,cstring_literals\"),internal_linkage)) static const char _os_fmt_str[] __asm(\"LOS_LOG895\") = \"%25s:%-5d \" \"HACStatusChanged %p\"; __attribute__((stack_protector_ignore)) uint8_t _Alignas(16) __attribute__((uninitialized)) _os_fmt_buf[__builtin_os_log_format_buffer_size(\"%25s:%-5d \" \"HACStatusChanged %p\", \"DSP_Routing_VP.cpp\", 502, gInstance.load())]; _os_log_impl(&__dso_handle, _log_tmp, _type_tmp, _os_fmt_str, (uint8_t *)__builtin_os_log_format(_os_fmt_buf, \"%25s:%-5d \" \"HACStatusChanged %p\", \"DSP_Routing_VP.cpp\", 502, gInstance.load()), (uint32_t)sizeof(_os_fmt_buf)) _Pragma(\"clang diagnostic pop\"); }); } }); } while (0); std::unique_lock locker1(mgr.GetMutex()); if (gInstance) { gInstance.load()->mParent.TriggerAdaptToDevice(); } })) == 0"
+ "+"
+ "-[AVHapticServer displayPrewarmedProcessEntriesWithPrewarmTime:]"
+ "-[AVHapticServerInstance handleSynthOutputNotificationDeviceStoppedFromBelow:]"
+ "-[AVHapticServerInstance stopRunning:]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:233: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:246: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:260: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__hash_table:1855: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1146: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1156: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:413: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:418: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:441: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:445: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/array:279: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/array:284: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/bitset:696: libc++ Hardening assertion __p < _Size failed: bitset::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:2199: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:2341: libc++ Hardening assertion __f != end() failed: deque::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/list:1394: libc++ Hardening assertion !empty() failed: list::pop_front() called with empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/list:830: libc++ Hardening assertion !empty() failed: list::front called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1112: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1121: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1130: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1139: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1148: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:1371: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:3384: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string_view:331: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
+ "/AppleInternal/Library/BuildRoots/4~CQM0ugBmljniJOFo4ChbeRjW-W0aiq-NalgZrbE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string_view:343: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "/Library/Audio/Tunings/%@/Haptics/SystemSounds/Library/systemsoundhapticpatterns.plist"
+ "/VAD"
+ "/var/mobile/Library/Audio/Tunings"
+ "0"
+ "01"
+ "01234567"
+ "0123456789abcdef"
+ "0123456789abcdefghijklmnopqrstuvwxyz"
+ "0B"
+ "0X"
+ "0b"
+ "AQProcessingNode"
+ "AQProcessingTap"
+ "ATATranslationClient"
+ "ActiveProcesses"
+ "An argument index may not have a negative value"
+ "AppleABL.%x.%x"
+ "AppleHapticsSupportPowerInterfaceResource"
+ "AspenActionPlayer.cpp"
+ "AudioCaptureInitialize"
+ "AudioCapturerCreateForEncodedAudioData"
+ "AudioCapturerCreateForPCMAudioData"
+ "AudioCapturerDestroy"
+ "AudioCapturerFilePath"
+ "AudioCapturerManager.h"
+ "AudioCapturerWriteBuffer"
+ "AudioCapturerWriteBufferList"
+ "AudioCapturerWritePackets"
+ "AudioTranscriptionAnalysis"
+ "CAGuard.cpp"
+ "CAMutex.cpp"
+ "CAPThread.cpp"
+ "CAPThread::SetTimeConstraints: thread_policy_set failed, Error: %d (%s)"
+ "CAPThread::Start: can't start because the thread is already running"
+ "CA_NoVector"
+ "CA_NoVector set; Vector unit optimized routines will be bypassed\n"
+ "Class getATATranslationClientClass()_block_invoke"
+ "Close"
+ "Close::fclose failed"
+ "Create::fclose failed"
+ "Create::fopen failed"
+ "CreatePasscodeDetectorClientPortal"
+ "DISABLED"
+ "DeleteFile"
+ "DeviceIsMuseCapable"
+ "DeviceSupportsClosedLoopHaptics"
+ "Didn't find user event for sequence with ID %u"
+ "ENABLED"
+ "Enable3PSpatialAudioExtension_iOS"
+ "End of input while parsing an argument index"
+ "End of input while parsing format specifier precision"
+ "Event track not found for sequence with ID %u, earlier code should have added one"
+ "Exists"
+ "Expected RT automation track iterator for track %u on sequence ID %u"
+ "Expected RT event track iterator for sequence with ID %u"
+ "ExplicitVolumeChange"
+ "Finished callback for sequence %u was NULL"
+ "GetFreeRequestBlock"
+ "GetLength"
+ "GetLength - file not open"
+ "GetLength::fstat failed"
+ "GetPosition"
+ "GetTimePitchUnflushedFrames"
+ "HandlePauseDueToRouteChange_block_invoke"
+ "Haptic mute reason %u was out of range"
+ "HapticAudioRunningCount"
+ "HapticForceStop"
+ "HapticSupport.cpp"
+ "HapticsPowerControlFeatures"
+ "HostAudioTranscriptionAnalysisServer"
+ "IONode_DeviceStoppedFromBelow"
+ "Integral value outside the range of the char type"
+ "IsOpen()"
+ "MacParrot"
+ "MetricsBase"
+ "MetricsBase_block_invoke"
+ "MetricsBase_block_invoke_2"
+ "MixServer"
+ "MultiOutputHapticSynth.mm"
+ "OfflineFOAProcessor"
+ "OfflineFOAProcessor.cpp"
+ "OfflineMixer"
+ "Open - file open invalid file permission"
+ "Open: Permission denied"
+ "Open::fopen failed"
+ "OrchestratorServer"
+ "OrchestratorService.mm"
+ "POSTCONDITION FAILURE (std::logic_error)"
+ "PRECONDITION FAILURE (std::logic_error)"
+ "Queue"
+ "Read"
+ "Read - file not open"
+ "Read::fread"
+ "ReadAsync"
+ "Replacement argument isn't a standard signed or unsigned integer type"
+ "Requested %u synth channels but received %u"
+ "SSS sequence with ID %u shouldn't be gone!"
+ "Seek - file not open"
+ "Seek::fseeko failed"
+ "SeekAsync"
+ "Sequence with ID %u was NULL in messenger notify-finished lambda"
+ "SetVolume"
+ "SharableMemory.cpp"
+ "Skip"
+ "Skip - file not open"
+ "Skip::fseeko failed"
+ "SpeechTranslation"
+ "Stuck UIFeedback engine encountered"
+ "Stuck haptic/audio prewarm encountered"
+ "SupportsMultiAudioOutput_block_invoke"
+ "SynthOutput.mm"
+ "SynthOutputNotificationCallback"
+ "SystemSoundMaximumVolume.plist"
+ "TFileBSD"
+ "TFileBSD.cpp"
+ "The argument index is invalid"
+ "The argument index should end with a ':' or a '}'"
+ "The argument index starts with an invalid character"
+ "The argument index value is too large for the number of arguments supplied"
+ "The fill option contains an invalid value"
+ "The format specifier contains malformed Unicode characters"
+ "The format specifier for "
+ "The format specifier should consume the input or end with a '}'"
+ "The format string contains an invalid escape sequence"
+ "The format string terminates at a '{'"
+ "The numeric value of the format specifier is too large"
+ "The precision option does not contain a value or an argument index"
+ "The replacement field misses a terminating '}'"
+ "The type does not fit in the mask"
+ "The type option contains an invalid value for "
+ "The type option contains an invalid value for a string formatting argument"
+ "The value of the argument index exceeds its maximum value"
+ "The width option should not have a leading zero"
+ "Using automatic argument numbering in manual argument numbering mode"
+ "Using manual argument numbering in automatic argument numbering mode"
+ "Write"
+ "Write - file not open"
+ "Write::fwrite"
+ "XMachServer init for service %s failed: %s"
+ "XMachServer.cpp"
+ "XMachServer.mLock"
+ "\\'"
+ "\\u{"
+ "\\x{"
+ "a bool"
+ "a character"
+ "a floating-point"
+ "a pointer"
+ "alternate form"
+ "an integer"
+ "aqmeio_captureoutput_ring_buffer_mode"
+ "close"
+ "commandSize != 0"
+ "cpms_maxPwr"
+ "cpms_minPwr"
+ "doCalculateSampleOffset"
+ "failed assertion: goodToCopy"
+ "fileAutoBugCapture"
+ "flexible_video_recording.austrip"
+ "flexible_video_recording.dspg"
+ "flexible_video_recording.propstrip"
+ "getInitialSystemSoundsAndHapticsVolume_block_invoke"
+ "getPowerBudgetRangesAndSetOnFW"
+ "handleReporterEngineOffEvent"
+ "hapticengineconfig.plist"
+ "inSynthOutput != nullptr"
+ "infnanINFNAN"
+ "initializeRealtimeTrackIterators"
+ "interval"
+ "intrusive_single_link_node.h"
+ "ios{}"
+ "logPowerLogCountEvent"
+ "logPowerLogForceStopEvent"
+ "logPowerLogOnDurationEvent"
+ "mach_make_memory_entry_64"
+ "mach_port_deallocate"
+ "maxIntervals"
+ "mmap"
+ "munmap"
+ "precision"
+ "r+b"
+ "shm_open"
+ "shm_unlink"
+ "sign"
+ "softlink:o:path:/AppleInternal/Library/Frameworks/AudioCapture.framework/AudioCapture"
+ "softlink:o:path:/System/Library/PrivateFrameworks/CoreAudioOrchestration.framework/CoreAudioOrchestration"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AudioTranscriptionAnalysis.framework/AudioTranscriptionAnalysis"
+ "t != nullptr"
+ "tfbsd"
+ "vm_allocate"
+ "vm_deallocate"
+ "vm_map"
+ "void *AudioTranscriptionAnalysisLibrary()"
+ "void *CoreAudioOrchestrationLibrary()"
+ "void softCreatePasscodeDetectorClientPortal()"
+ "w+b"
+ "zero-padding"
+ "~TFileBSD"
- "\t\tType='%4.4s', SubType='%4.4s',Manu='%4.4s'\n"
- "\t\tcontrolID = %d, value = %.3f\n"
- "\t\tscope=%d, element=%d\n"
- "\t%6ld:  "
- "\t%s:Chan:%d %d %d\n"
- "\t* * UnknownEvent:%d * *\n"
- "\tAUPreset: @%p\n"
- "\tExNote: ID=%d, Group=%d, Dur=%.3f, pitch = %.3f, velocity = %.3f\n"
- "\tMetaEvent:%02X\n"
- "\tNote:Ch:%d %d %d (%.3f)\n"
- "\tNum Events: %d, Track Length: %.2f beats, Loop Region End: %.2f beats\n"
- "\tParameterEvent:paramID=%d, scope=%d, element=%d, value=%f\n"
- "\tSMPTE Offset [%d:%d:%d:%d.%d]\n"
- "\tSys-Ex:%02X\n"
- "\tTempo:%.3f\n"
- "\tTime Sig:%d/%d, %d clks/qtr, %d 32nds/clk\n"
- "\tUserEvent, length = %d\n"
- "\tclear all connections\n"
- "\tconnect:source=%d,bus=%d,dest=%d,bus=%d\n"
- "\tdisconnect:dest=%d,bus=%d\n"
- "\tinput callback:dest=%d,bus=%d\n"
- "\tmLastUpdateError=%d, eventsToProcess=%c, isInitialized=%c, isRunning=%c"
- "\tnode %3d bus %3d => node %3d bus %3d"
- "\tnode %d: %s %s %s, instance %p %c %c\n"
- "\tremove node=%d\n"
- "\tunknown event\n"
- "\t{%p, %p} => node %3d bus %3d"
- "   "
- "    Volume:                     \t%7.3f\n"
- "    [%3d] : %d bytes (capacity %d) @ %p"
- "    channel layout: %s\n"
- "    magic cookie: %s\n"
- "    maximum output packet size: %d\n"
- "  Buffers:\n"
- "  Commands:\n"
- "  Connections:\n"
- "  CurrentState:\n"
- "  Data format: %s"
- "  Decode buffer: %d frames\n"
- "  Events to be updated:\n"
- "  IO assignment: '%s'%s\n"
- "  Input Callbacks:\n"
- "  Member Nodes:\n"
- "  Parameters:\n"
- "  Problem Events when updated:\n"
- "  [%d ch, %d Hz]"
- "  [%s]"
- "  isInput=%d, isRunning=%d, isStarted=%d, isPaused=%d\n"
- " (%d)\n"
- "#"
- "#16@0:8"
- "%02X "
- "%25s:%-5d %@ SSID %u, SSCoreHapticsPlayer %p"
- "%25s:%-5d %@ completed for SSID %d, SSCoreHapticsPlayer %p"
- "%25s:%-5d %@ for SSID %d, SSCoreHapticsPlayer %p has already finished or never started"
- "%25s:%-5d %s:  ClientEntry for client ID 0x%x is invalid! Num of clients in mClientMap: %u"
- "%25s:%-5d %s: %s format changed for clientID 0x%x"
- "%25s:%-5d %s: %s side for clientID 0x%x is already initialized!"
- "%25s:%-5d %s: %s side for clientID 0x%x is already uninitialized!"
- "%25s:%-5d %s: %s side, for clientID 0x%x"
- "%25s:%-5d %s: %s volume changed for clientID 0x%x"
- "%25s:%-5d %s: %u channels"
- "%25s:%-5d %s: %u synth channels now available"
- "%25s:%-5d %s: << Stuck UIFeedback engine encountered. Filing ABC >>"
- "%25s:%-5d %s: << Stuck haptic prewarm encountered. Filing ABC >> "
- "%25s:%-5d %s: <Bottom of messenger notify-finished lambda (done calling std::function)>"
- "%25s:%-5d %s: <Haptic on time: %.1f seconds>"
- "%25s:%-5d %s: <Haptic prewarm time: %.1f seconds>"
- "%25s:%-5d %s: <RTMessenger thread callback> Calling notifyFinished(stopped=false) from within client finish callback"
- "%25s:%-5d %s: <RTMessenger thread callback> Calling notifyFinished(stopped=true) from within client ID 0x%x finish callback"
- "%25s:%-5d %s: <RTMessenger thread callback> Client already destroyed -- noop"
- "%25s:%-5d %s: <RTMessenger thread callback> DONE"
- "%25s:%-5d %s: <Top of messenger notify-finished lambda for seq ID %u - calling captured std::function 'callback' %p>"
- "%25s:%-5d %s: => remaining coarse tune %d semitones (%.1f cents)"
- "%25s:%-5d %s: Add param curve, client ID 0x%lx, param %u (0x%x)"
- "%25s:%-5d %s: Adding %s layer for key %u"
- "%25s:%-5d %s: Adding audio sample '%@'"
- "%25s:%-5d %s: Adding connections for filter 0x%x: cutoff %f Hz, range %fx that"
- "%25s:%-5d %s: Adding default envelope for layer"
- "%25s:%-5d %s: Adding extra power check: high-power SSS %s existing low-power"
- "%25s:%-5d %s: Adding raw audio sample %p, size %u bytes. Raw audio has %u channels, %u frames, %u Bytes per frame, clientProcessTaskToken: %u"
- "%25s:%-5d %s: Adding zone for sampleID 0x%x with key %u vel %u"
- "%25s:%-5d %s: Adjusted waveform base freq %f Hz"
- "%25s:%-5d %s: After %s wait, client state = %d"
- "%25s:%-5d %s: After seq sema %s wait"
- "%25s:%-5d %s: Already have %d MIDI channels reserved -- nothing to do here"
- "%25s:%-5d %s: Already in '%s' - no-op"
- "%25s:%-5d %s: Anchor timestamp sample time %lld already set on audio side"
- "%25s:%-5d %s: Anchor timestamp sample time %lld already set on haptic side"
- "%25s:%-5d %s: Anchor: hosttime %llu, sample time %.0f, audio latency %u, haptic latency %u"
- "%25s:%-5d %s: App was in background-running - unmute haptics for suspend"
- "%25s:%-5d %s: Asynchronous call to play sequence %u with synchronizer %p"
- "%25s:%-5d %s: Attack time Parameter:"
- "%25s:%-5d %s: Attack: %f"
- "%25s:%-5d %s: Attempting to flush starting or stopped client"
- "%25s:%-5d %s: Audio Filter Cutoff Parameter:"
- "%25s:%-5d %s: Audio-only - just storing anchor"
- "%25s:%-5d %s: Automation track %p for type %u: publishing control point (time %.3f, value %f) from source curve %p"
- "%25s:%-5d %s: Automation track %p for type %u: publishing flat segment extension control point (time %.3f, value %f) for non-overlapping source curve %p"
- "%25s:%-5d %s: Budget granted by CPMS for haptics is %{public}@."
- "%25s:%-5d %s: Called on %s side, runMode = 0x%x"
- "%25s:%-5d %s: Called on %s side. Current run mode: audio: %d, haptics: %d"
- "%25s:%-5d %s: Calling AddRunningClient for %s node client"
- "%25s:%-5d %s: Calling _finishedCallback %p"
- "%25s:%-5d %s: Calling doPrewarm (on ACQ) due to client resume"
- "%25s:%-5d %s: Calling doStopPrewarm (on ACQ) due to client suspend"
- "%25s:%-5d %s: Calling doStopRunning (on ACQ) due to client suspend"
- "%25s:%-5d %s: Calling doStopRunningForInterrupt (async on ACQ) due to client interruption"
- "%25s:%-5d %s: Cannot configure audio output for clientID 0x%x. Error %d"
- "%25s:%-5d %s: Change in mute-on-record state: %d"
- "%25s:%-5d %s: Channel voice count: %u"
- "%25s:%-5d %s: Channel was already released"
- "%25s:%-5d %s: ChannelID %u not found"
- "%25s:%-5d %s: Clear events,  client ID 0x%lx"
- "%25s:%-5d %s: Clear sequence events,  client ID 0x%lx"
- "%25s:%-5d %s: Clearing all events for client ID 0x%lx"
- "%25s:%-5d %s: Client 0x%lx did not stop on interruption (or was not found)"
- "%25s:%-5d %s: Client 0x%lx does not respond to interruptions (or was not found)"
- "%25s:%-5d %s: Client ID: 0x%lx"
- "%25s:%-5d %s: Client ID: 0x%lx with audio: %d cancelCurrent: %d isHighPowerHaptics: %d"
- "%25s:%-5d %s: Client ID: 0x%lx, %s for interrupt, fadeTime: %f, fadeLevel: %f, affectHaptics: %u"
- "%25s:%-5d %s: Client ID: 0x%lx, ringer switch: %d"
- "%25s:%-5d %s: Client behavior suppresses audio session activation"
- "%25s:%-5d %s: Client follows audio route, so mute all non-following clients"
- "%25s:%-5d %s: Client gone - noop"
- "%25s:%-5d %s: Client is in process of flushing"
- "%25s:%-5d %s: Client stopped before wait started.  Going on."
- "%25s:%-5d %s: Client stopping or not running - ignoring command"
- "%25s:%-5d %s: Client was following audio route, so unmute all non-following clients"
- "%25s:%-5d %s: CompleteTimestamp FAILED"
- "%25s:%-5d %s: CompleteTimestamp failed - bailing out"
- "%25s:%-5d %s: Custom audio event found that needs to be offsetted by factor of %.2f at time %.2f"
- "%25s:%-5d %s: Custom audio event found that offset needs to be set back to zero at time %.2f"
- "%25s:%-5d %s: Custom gain curve coefficient A: %f"
- "%25s:%-5d %s: Custom gain curve coefficient B: %f"
- "%25s:%-5d %s: Cutoff: %f"
- "%25s:%-5d %s: DEBUG: Caught boost exception during visit_current_states()"
- "%25s:%-5d %s: DEBUG: WHAT IS THIS STATE?"
- "%25s:%-5d %s: Decay time Parameter:"
- "%25s:%-5d %s: Decay: %f"
- "%25s:%-5d %s: Detaching sequence %u"
- "%25s:%-5d %s: Did not find a layer and/or zone for key: %u, vel: %u"
- "%25s:%-5d %s: Did not find a layer matching this key"
- "%25s:%-5d %s: Did not find a zone matching this velocity"
- "%25s:%-5d %s: Disabling user callback on sequence %p"
- "%25s:%-5d %s: Disabling zone"
- "%25s:%-5d %s: Dispatching app state notification handler async onto ACQ"
- "%25s:%-5d %s: Dispatching doPrewarm on ACQ"
- "%25s:%-5d %s: Dispatching doStopPrewarm and doStopRunning on ACQ"
- "%25s:%-5d %s: Dispatching doStopPrewarm on ACQ"
- "%25s:%-5d %s: Dispatching doStopRunning on ACQ"
- "%25s:%-5d %s: Dispatching route change notification handler async onto ACQ"
- "%25s:%-5d %s: Dispatching startEntry on ACQ"
- "%25s:%-5d %s: Dispatching unmuteClientAfterSessionInterruption on ACQ"
- "%25s:%-5d %s: Done enqueing lambda on RTMessenger"
- "%25s:%-5d %s: Done fading client 0x%lx"
- "%25s:%-5d %s: Done handling charging state change"
- "%25s:%-5d %s: Done handling continuity screen state change"
- "%25s:%-5d %s: Done handling interruption notification for client 0x%lx"
- "%25s:%-5d %s: Done handling microphone activity change"
- "%25s:%-5d %s: Done handling phone call state change.  mPhoneCallActive -> %d"
- "%25s:%-5d %s: Done handling record state change"
- "%25s:%-5d %s: Done handling route change for client 0x%lx"
- "%25s:%-5d %s: Done handling state change for client 0x%lx"
- "%25s:%-5d %s: Done stopping interrupted client 0x%lx"
- "%25s:%-5d %s: Done unmuting client 0x%lx"
- "%25s:%-5d %s: Done waiting"
- "%25s:%-5d %s: Done waiting for force stop"
- "%25s:%-5d %s: ERROR converting param curve points to AU parameter events. result: %d"
- "%25s:%-5d %s: ERROR: Allocating mSynthBuffer for %s side clientID 0x%x failed!"
- "%25s:%-5d %s: ERROR: Allocating mSynthRingBuffer for %s side clientID 0x%x failed!"
- "%25s:%-5d %s: ERROR: Real-time component threw exception - treating as fatal error"
- "%25s:%-5d %s: ERROR: Unable to load per-product tuning %@, err %d"
- "%25s:%-5d %s: ERROR: Unable to load the configuration plist: err %d"
- "%25s:%-5d %s: EndEventList - breaking out"
- "%25s:%-5d %s: EndParamCurveList - breaking out"
- "%25s:%-5d %s: Ending power check due to start error"
- "%25s:%-5d %s: Ending power check: low-power SSS %s existing high-power"
- "%25s:%-5d %s: Entered"
- "%25s:%-5d %s: Entered (on ACQ)"
- "%25s:%-5d %s: Event %d:"
- "%25s:%-5d %s: Event %u local refcount at zero - unreferencing on manager"
- "%25s:%-5d %s: Event is %f seconds before subslice beginning"
- "%25s:%-5d %s: Event not found for key: %u (0x%x)"
- "%25s:%-5d %s: Event started with instanceID %u"
- "%25s:%-5d %s: Exited (on ACQ)"
- "%25s:%-5d %s: Expanding AU channel count from %u to %u"
- "%25s:%-5d %s: Factor %f"
- "%25s:%-5d %s: Filter cutoff factor: %f"
- "%25s:%-5d %s: Final event,  client ID 0x%lx"
- "%25s:%-5d %s: Finish notify callback completed"
- "%25s:%-5d %s: Force-stopping sequence %p"
- "%25s:%-5d %s: Force-stopping sequence %u"
- "%25s:%-5d %s: Found StartParamCurveList outside of event list!"
- "%25s:%-5d %s: Found existing deactivated audio synth output for client ID 0x%x"
- "%25s:%-5d %s: Found it with layer ID %u"
- "%25s:%-5d %s: Found it with zone ID %u"
- "%25s:%-5d %s: Found synth output for valid client ID 0x%x"
- "%25s:%-5d %s: Front command on main queue: time: %.3f (< slice end %.3f) [host time %llu], type: %u count: %u"
- "%25s:%-5d %s: Gain Parameter:"
- "%25s:%-5d %s: Gain envelope:"
- "%25s:%-5d %s: GetSettings(): looking for hardware platform: %s"
- "%25s:%-5d %s: GetSettings(): looking for late night / soundcheck key: %s"
- "%25s:%-5d %s: GetSettings(): looking for route: %s"
- "%25s:%-5d %s: GetSettings(): no dictionary (or default) for encoder OS version: %s %d.%d"
- "%25s:%-5d %s: GetSettings(): no dictionary for encoder OS type: %s"
- "%25s:%-5d %s: GetSettings(): no dictionary for hw platform: %s"
- "%25s:%-5d %s: GetSettings(): no dictionary for media type: %s"
- "%25s:%-5d %s: GetSettings(): no dictionary for route: %s"
- "%25s:%-5d %s: Got %@ notification"
- "%25s:%-5d %s: Got adjusted audio sample time %.0f"
- "%25s:%-5d %s: Got adjusted haptic sample time %.0f"
- "%25s:%-5d %s: Got error %d while writing packets for AQ output enqueue"
- "%25s:%-5d %s: Handling BeginQuietTime"
- "%25s:%-5d %s: Handling EndQuietTime"
- "%25s:%-5d %s: Handling Pause"
- "%25s:%-5d %s: Handling Resume"
- "%25s:%-5d %s: Handling Silent Mute"
- "%25s:%-5d %s: Handling Silent UnMute"
- "%25s:%-5d %s: Handling StopNow"
- "%25s:%-5d %s: Handling client route change for client 0x%lx"
- "%25s:%-5d %s: Haptic AutoBugCapture filed. Starting cooldown of %.1f hours"
- "%25s:%-5d %s: Haptic waveform pitch modulation limits: %.2f cents lower, %.2f cents upper"
- "%25s:%-5d %s: Haptic-only - just storing anchor"
- "%25s:%-5d %s: ID: %u channel: %u offset: %u [=> key %u vel %u]"
- "%25s:%-5d %s: Ignoring %s event: client is %s"
- "%25s:%-5d %s: Ignoring InterruptionEnded"
- "%25s:%-5d %s: Ignoring cmd: 0x%x"
- "%25s:%-5d %s: Illegal HapticCommandType: %u"
- "%25s:%-5d %s: Illegal StartEventList within list!"
- "%25s:%-5d %s: Illegal StartParamCurveList within list!"
- "%25s:%-5d %s: Illegal command type: %u"
- "%25s:%-5d %s: Illegal playback rate"
- "%25s:%-5d %s: Illegal synth channel - ignoring"
- "%25s:%-5d %s: In-process pause done ramping out"
- "%25s:%-5d %s: Including channel event: ID %d value %f time:%.3f"
- "%25s:%-5d %s: Including extended note param: ID %d value %f"
- "%25s:%-5d %s: Invalid haptic channel ID: %u"
- "%25s:%-5d %s: Layer %d:"
- "%25s:%-5d %s: Legacy sequence loops"
- "%25s:%-5d %s: LoopEnable, client ID 0x%lx, sequenceID %u"
- "%25s:%-5d %s: LoopLength, client ID 0x%lx, sequenceID %u"
- "%25s:%-5d %s: Looping %s"
- "%25s:%-5d %s: Making parameter event for curve control point: ID=%d time=%.3f value=%f"
- "%25s:%-5d %s: Min Gain (dB): %f"
- "%25s:%-5d %s: Min: %f Max: %f"
- "%25s:%-5d %s: Modified haptic release: %f"
- "%25s:%-5d %s: MusicEventIteratorGetEventInfo returned %d - doing cleanup"
- "%25s:%-5d %s: MusicEventIteratorSeek returned %d - doing cleanup"
- "%25s:%-5d %s: MusicEventIteratorSetEventTime returned %d - doing cleanup"
- "%25s:%-5d %s: MusicPlayer not reporting playing, so not pausing"
- "%25s:%-5d %s: MusicPlayer not reporting playing, so not stopping"
- "%25s:%-5d %s: MusicPlayerGetTime returned %d"
- "%25s:%-5d %s: MusicPlayerSetPlayRateScalar returned %d"
- "%25s:%-5d %s: MusicPlayerSetTime returned %d"
- "%25s:%-5d %s: MusicPlayerStart returned %d"
- "%25s:%-5d %s: Need to render %u frames to catch up?"
- "%25s:%-5d %s: Negative frame offset - increasing skip time to %.3f to synch"
- "%25s:%-5d %s: New app state %d ignored"
- "%25s:%-5d %s: New route: %@"
- "%25s:%-5d %s: No HapticEngine per-product tuning found for '%@'"
- "%25s:%-5d %s: No change in mute-on-record state"
- "%25s:%-5d %s: No more active sequences - asynch posting to sequence sema"
- "%25s:%-5d %s: No registered channel at index %u"
- "%25s:%-5d %s: No valid RT MusicEventIterator. Skipping"
- "%25s:%-5d %s: Not able to remove it at this time. Will try in the next render cycle"
- "%25s:%-5d %s: Not setting session inactive because it is being interrupted"
- "%25s:%-5d %s: Not stopped, so not posting to client sema"
- "%25s:%-5d %s: Not verified to be removed so don't remove"
- "%25s:%-5d %s: Old mute bits for channel %d: 0x%lx, new mute bits: 0x%lx"
- "%25s:%-5d %s: PLAYER TIME: %f > LOOP LENGTH: %f"
- "%25s:%-5d %s: Pause sequence, client ID 0x%lx, sequenceID %u"
- "%25s:%-5d %s: Pausing sequence %p (ID %u)"
- "%25s:%-5d %s: Pausing sequence %u"
- "%25s:%-5d %s: PlaybackRate, client ID 0x%lx, sequenceID %u"
- "%25s:%-5d %s: Playing one haptic with intensity 0 to warm up memory"
- "%25s:%-5d %s: Playing sequence %u"
- "%25s:%-5d %s: Posting to client sema"
- "%25s:%-5d %s: Posting vibe start notification"
- "%25s:%-5d %s: Posting vibe stop notification"
- "%25s:%-5d %s: PowerTimer calling its block"
- "%25s:%-5d %s: PowerTimer restarting itself"
- "%25s:%-5d %s: PreflightOfflineRender aq@%p  correcting available time-pitch unflushed frames: %d to framecount"
- "%25s:%-5d %s: PreflightOfflineRender aq@%p - Setting available time-pitch unflushed frames: to %d for input block size: %d"
- "%25s:%-5d %s: PreflightOfflineRender aq@%p - failed to query UnflushedSampleCount."
- "%25s:%-5d %s: PreflightOfflineRender aq@%p - failed to query ZeroLatencyPullSize."
- "%25s:%-5d %s: PreflightOfflineRender aq@%p adding available unflushed frames: %d to framecount"
- "%25s:%-5d %s: PreflightOfflineRender aq@%p clientSampleRate %f mixerSampleRate %f inCurrentSampleTime: %lld anchor: %lld queueTimeScaled: %lld framesAvailable(scaled): %lld decodedFrames(unscaled): %lld framesRequired(scaled): %lld framesRequired(unscaled): %lld done decoding: %d recentRenderEndTime(unscaled): %lld scaledLastRenderTime: %lld currentEndOfTimeline(unscaled): %lld scaledEndOfTimeline: %lld mOfflineEndOfStreamSampleTime= %lld unscaledInputSampleTime=%lld unflushedSamplesFromTimePitch: %lld "
- "%25s:%-5d %s: Preparing sequence ID %u with non-RT callback %p"
- "%25s:%-5d %s: Processing haptic/audio event"
- "%25s:%-5d %s: Processing param event"
- "%25s:%-5d %s: Product: '%@'"
- "%25s:%-5d %s: Queueing notify functor on messenger"
- "%25s:%-5d %s: Queueing notify functor on messenger for client ID: 0x%x"
- "%25s:%-5d %s: Queueing removeCustomAudioEvent functor on messenger"
- "%25s:%-5d %s: Ramping controller: relative time %f, level %f"
- "%25s:%-5d %s: Reached end of queued commands"
- "%25s:%-5d %s: Read command from client ID 0x%lx: Relative time: %.3f type: %u chanID: %d"
- "%25s:%-5d %s: Read command from client ID 0x%lx: time: %.3f type: %u chanID: %d"
- "%25s:%-5d %s: Received MX SystemVolumeDidChange notification. Actively querying VAD volume now"
- "%25s:%-5d %s: Release time Parameter:"
- "%25s:%-5d %s: Releasing %u channel(s)"
- "%25s:%-5d %s: Removing zone from layer and unreferencing its audio sample"
- "%25s:%-5d %s: Request to reserve %u more MIDI chans"
- "%25s:%-5d %s: Requested root pitch %f Hz => zone coarse tune %d semitones"
- "%25s:%-5d %s: Requesting %u total channels; %u synth chans already available"
- "%25s:%-5d %s: Requesting copy of event ID %u from synth"
- "%25s:%-5d %s: Requesting new event from synth"
- "%25s:%-5d %s: Requesting power check for high-power client"
- "%25s:%-5d %s: Reset sequence, client ID 0x%lx, sequenceID %u"
- "%25s:%-5d %s: Resetting channel: client ID 0x%lx, channelID %lu"
- "%25s:%-5d %s: Resume sequence, client ID 0x%lx, sequenceID %u"
- "%25s:%-5d %s: Resuming looped playback at offset %.2f - seeking back to %.2f to continue"
- "%25s:%-5d %s: Resuming sequence %p (ID %u)"
- "%25s:%-5d %s: Resuming sequence %u"
- "%25s:%-5d %s: Returning layer ID %u"
- "%25s:%-5d %s: Returning new zone ID %u"
- "%25s:%-5d %s: SSS Sequence ID %u playing at offset %f seconds"
- "%25s:%-5d %s: SSS Sequence ID %u reached loop point"
- "%25s:%-5d %s: SSS pattern completion callback: Returned from external clients completion handler"
- "%25s:%-5d %s: Sample path %@:"
- "%25s:%-5d %s: Searching for layer with key %u"
- "%25s:%-5d %s: Searching for layer with key: %u vel: %u"
- "%25s:%-5d %s: Searching for zone with velocity %u"
- "%25s:%-5d %s: Seek sequence, client ID 0x%lx, sequenceID %u"
- "%25s:%-5d %s: Seeking now-nonlooping player *back* to time %.2f to finish out"
- "%25s:%-5d %s: Seeking sequence %u to %.2f"
- "%25s:%-5d %s: Seeking to beat %.2f in sequence"
- "%25s:%-5d %s: Segment end controller: relative time %f, level %f"
- "%25s:%-5d %s: Sending RT QueuedForForceStop and waiting on sema again..."
- "%25s:%-5d %s: Sequence %u is flushing... inRenderTime = %.4f"
- "%25s:%-5d %s: Sequence ID %lu stopping player"
- "%25s:%-5d %s: Sequence ID %u"
- "%25s:%-5d %s: Sequence ID %u finished playing. Enqueing lambda for non-RT finished callback %p on RTMessenger"
- "%25s:%-5d %s: Sequence ID %u not found"
- "%25s:%-5d %s: Sequence ID %u not in active list"
- "%25s:%-5d %s: Sequence ID %u notifying finish via callback on RT thread"
- "%25s:%-5d %s: Sequence ID %u reached end"
- "%25s:%-5d %s: Sequence cmd, client ID 0x%lx, sequenceID %u"
- "%25s:%-5d %s: SequenceRTAccessor::getEventInfo returned %d"
- "%25s:%-5d %s: SequenceRTAccessor::nextEvent returned %d"
- "%25s:%-5d %s: Sequences stopped before wait started.  Going on."
- "%25s:%-5d %s: Set automation track %u t=0 point value to %.3f, based on calculated value at t=iterationEndTime (%.2f beats)"
- "%25s:%-5d %s: Set sequence channel param, client ID 0x%lx, sequenceID %u, param %u (0x%x), seq channel index %d"
- "%25s:%-5d %s: Set sequence param, client ID 0x%lx, sequenceID %u"
- "%25s:%-5d %s: Setting (private) audio session ID %u play state to Started"
- "%25s:%-5d %s: Setting (private) audio session ID %u play state to Stopped and setting session inactive"
- "%25s:%-5d %s: Setting (private) audio session ID %u to unduck other audio (if applicable)"
- "%25s:%-5d %s: Setting (shared) audio session ID %u play state to Started"
- "%25s:%-5d %s: Setting (shared) audio session ID %u play state to Stopped"
- "%25s:%-5d %s: Setting attack to convex to generate pseudo-linear ramp"
- "%25s:%-5d %s: Setting param %u value %f"
- "%25s:%-5d %s: Setting param %u value %f on synth channel %u"
- "%25s:%-5d %s: Setting track offset to %.2f beats"
- "%25s:%-5d %s: Setting up muting"
- "%25s:%-5d %s: Setting zone %u output to bus %u"
- "%25s:%-5d %s: Specified ramp duration is sub-minimal (provided %.3f, requiring %.3f) - pushing new event forward to time %.3f. Warning: ramp might be too fast for some watches"
- "%25s:%-5d %s: Start event, client ID 0x%lx"
- "%25s:%-5d %s: Start of command list for client ID 0x%lx, list time %f"
- "%25s:%-5d %s: Start of param curve command list for client ID 0x%lx, curve list time %f"
- "%25s:%-5d %s: Start sequence, client ID 0x%lx, sequenceID %u [frame offset %d]"
- "%25s:%-5d %s: StartParamCurveList - adjusted time: %.3f - descending into curve"
- "%25s:%-5d %s: StartRunning: this = %p, prewarmed: %d running: %d haptic: %d, sessionID: %u(0x%x), clientID: 0x%x synchronizer: %p"
- "%25s:%-5d %s: Starting sequence %p (ID %u)"
- "%25s:%-5d %s: Starting sequence %u"
- "%25s:%-5d %s: Stop event, client ID 0x%lx, token %u"
- "%25s:%-5d %s: Stop sequence, client ID 0x%lx, sequenceID %u"
- "%25s:%-5d %s: StopRunning: this = %p, running: %d haptic: %d, bus: %u, for clientID 0x%x"
- "%25s:%-5d %s: Stopping all sequences in active list"
- "%25s:%-5d %s: Stopping running %s for client ID: 0x%lx"
- "%25s:%-5d %s: Stopping sequence %p (ID %u)"
- "%25s:%-5d %s: Stopping sequence %u"
- "%25s:%-5d %s: Stuck UIFeedback engine encountered but haptic AutoBugCapture has filed within 24 hours"
- "%25s:%-5d %s: Stuck haptic prewarm encountered but haptic AutoBugCapture has filed within 24 hours"
- "%25s:%-5d %s: Sustain: %f"
- "%25s:%-5d %s: Synchronizer start offset %lld > I/O frame count %u -- waiting another I/O cycle"
- "%25s:%-5d %s: Synth has been prewarmed beyond threshold time. Unprewarming all clients"
- "%25s:%-5d %s: SynthOutput %s ringbuffer info: %s"
- "%25s:%-5d %s: SynthOutput(%s) this = %p, sessionID: %u(0x%x), for client ID 0x%x, mRoutingBehavior: %s"
- "%25s:%-5d %s: Top of lambda handed to Sequence::prepare() for id %u"
- "%25s:%-5d %s: Transpose Parameter:"
- "%25s:%-5d %s: Treating as one-shot (ignores event-off command)"
- "%25s:%-5d %s: Unduck other audio, client ID 0x%lx"
- "%25s:%-5d %s: Unknown parameter: %u"
- "%25s:%-5d %s: Updating audio session for audio synth output for client ID 0x%x"
- "%25s:%-5d %s: Using MusicPlayer extended note event w/ extparams, dur:%.2f [key:%u vel:%u], time:%.3f"
- "%25s:%-5d %s: Using MusicPlayer extended note event, dur:%.2f [key:%u vel:%u], time:%.3f"
- "%25s:%-5d %s: Value delta %.3f requires a minimal ramp duration of %.3f"
- "%25s:%-5d %s: Verified to be removed. So release ID and channel now"
- "%25s:%-5d %s: WARNING: Fetch for %s ring buffer end sample %lld > buffer range [%ld - %ld]"
- "%25s:%-5d %s: WARNING: Fetch for %s ring buffer start sample %lld < buffer range [%ld - %ld]"
- "%25s:%-5d %s: WARNING: Fetch from %s ring buffer returned err %d"
- "%25s:%-5d %s: WARNING: Illegal AddParamCurve (adjusted time %.3lf, type %u) -- has different paramID %u than expected paramID %u! Skipping"
- "%25s:%-5d %s: WARNING: Render thread error: %d - File radar with haptics team"
- "%25s:%-5d %s: WARNING: Server master is already nil - no call to stop prewarm or running possible"
- "%25s:%-5d %s: WARNING: Store to %s ring buffer returned err %d"
- "%25s:%-5d %s: WARNING: cleanupToBeDetachedChannels: could not get lock - will retry the next render cycle"
- "%25s:%-5d %s: WARNING: client ID: 0x%x cannot enqueue RT command %u - not running"
- "%25s:%-5d %s: WARNING: client ID: 0x%x neither stopping nor !stopped"
- "%25s:%-5d %s: WARNING: failed to set parameter on AU: err %d"
- "%25s:%-5d %s: WARNING: failed to start event on AU: err %d"
- "%25s:%-5d %s: WARNING: frame count (%u) exceeds %u -- returning silence"
- "%25s:%-5d %s: WARNING: mRenderLock lock held -- returning silence"
- "%25s:%-5d %s: Waiting on sema for all sequences to complete..."
- "%25s:%-5d %s: Waiting on sema for client to stop..."
- "%25s:%-5d %s: Zone %d:"
- "%25s:%-5d %s: [end of finishAction]"
- "%25s:%-5d %s: [end of forceStopAction]"
- "%25s:%-5d %s: [end of loadAction]"
- "%25s:%-5d %s: [end of pauseAction]"
- "%25s:%-5d %s: [end of prepareAction]"
- "%25s:%-5d %s: [end of prepareResetAction]"
- "%25s:%-5d %s: [end of preparedPlayAction]"
- "%25s:%-5d %s: [end of rePlayAction]"
- "%25s:%-5d %s: [end of resumeAction]"
- "%25s:%-5d %s: [end of seekAction]"
- "%25s:%-5d %s: [end of seqEndedAction]"
- "%25s:%-5d %s: [end of startAction]"
- "%25s:%-5d %s: [end of startingPlayAction]"
- "%25s:%-5d %s: [end of stopAction]"
- "%25s:%-5d %s: [end of unPauseAction]"
- "%25s:%-5d %s: _finishedCallback %p completed"
- "%25s:%-5d %s: _finishedCallback is NULL"
- "%25s:%-5d %s: _flushRequestTime -> %.4f"
- "%25s:%-5d %s: _flushTime is %.4f, so sending DoneFlushing"
- "%25s:%-5d %s: active: %d someoneIsRecording: %d"
- "%25s:%-5d %s: added event to local map and bumping manager's reference"
- "%25s:%-5d %s: adding callback %p for context %p"
- "%25s:%-5d %s: already flushing - updating request time"
- "%25s:%-5d %s: aq@%p / bcmd@%p: Error from output capture: %d (%u frames, %u bytes, %p data ptr)"
- "%25s:%-5d %s: aq@%p: %d (mDisposalPending=%d)"
- "%25s:%-5d %s: averagePowerBudgetMax not found from user client"
- "%25s:%-5d %s: averagePowerBudgetMin not found found from user client"
- "%25s:%-5d %s: beginPauseAction: %s => %s"
- "%25s:%-5d %s: calling doStart() before internal transition"
- "%25s:%-5d %s: channel %d still active"
- "%25s:%-5d %s: channel %s muted for audio, %s muted for haptics"
- "%25s:%-5d %s: channel %u, mute=%d - behavior set to not mute - noop"
- "%25s:%-5d %s: channel %u, mute=%d, why=%d current state was %s"
- "%25s:%-5d %s: channel ID %u <-> synth channel %u: no pending commands, not active"
- "%25s:%-5d %s: channel ID %u no longer mapped to synth channel"
- "%25s:%-5d %s: channel active during flush"
- "%25s:%-5d %s: channel: %u Enabling rendering %s"
- "%25s:%-5d %s: channel: %u Enabling sub-rendering %s"
- "%25s:%-5d %s: channel: %u audioAlreadyMuted: %d hapticsAlreadyMuted: %d"
- "%25s:%-5d %s: channel: %u mute: %d ramp: %.3f secs"
- "%25s:%-5d %s: clearing events on channel: %u"
- "%25s:%-5d %s: client ID 0x%x not yet calling finish: %s"
- "%25s:%-5d %s: client ID 0x%x state: %s => %s"
- "%25s:%-5d %s: client ID: 0x%x adding sequence %u to active queue"
- "%25s:%-5d %s: client ID: 0x%x is %s"
- "%25s:%-5d %s: client ID: 0x%x isStopped: %d"
- "%25s:%-5d %s: client ID: 0x%x preparing SSS sequence %u"
- "%25s:%-5d %s: client ID: 0x%x preparing sequence %u"
- "%25s:%-5d %s: client ID: 0x%x removing sequence %u from active queue"
- "%25s:%-5d %s: client ID: 0x%x start count == 1, so calling doStart"
- "%25s:%-5d %s: client ID: 0x%x, eventID %u"
- "%25s:%-5d %s: client ID: 0x%x, inRenderTime %.4f"
- "%25s:%-5d %s: client ID: 0x%x, inRenderTime = %.4f"
- "%25s:%-5d %s: client ID: 0x%x, mute all audio on this client: %d"
- "%25s:%-5d %s: client ID: 0x%x, mute all haptics on this client: %d"
- "%25s:%-5d %s: client ID: 0x%x, playing sequence ID %u, offset time %f, skip time %f"
- "%25s:%-5d %s: client ID: 0x%x, resetting sequence ID %u"
- "%25s:%-5d %s: client ID: 0x%x, returning instanceID %u"
- "%25s:%-5d %s: client ID: 0x%x, sequence ID %u, loop %d"
- "%25s:%-5d %s: client ID: 0x%x, sequence ID %u, loop length %f seconds"
- "%25s:%-5d %s: client ID: 0x%x, sequence ID %u, rate %f"
- "%25s:%-5d %s: client ID: 0x%x, stopping sequence ID %u"
- "%25s:%-5d %s: client ID: 0x%x: flush wait time: %.3f seconds"
- "%25s:%-5d %s: client in process of flushing - setting _stoppedDuringFlush"
- "%25s:%-5d %s: client in process of stopping - setting _stoppedDuringFlush"
- "%25s:%-5d %s: continuityScreenOn: %d"
- "%25s:%-5d %s: current state now %s"
- "%25s:%-5d %s: destroyAction: %s => %s"
- "%25s:%-5d %s: device rate check: audio & haptic both %f"
- "%25s:%-5d %s: didNotReachEnd guard: returning %d"
- "%25s:%-5d %s: doMute:%d - why:%d muting for SSS client handled here"
- "%25s:%-5d %s: enableLoopingAction"
- "%25s:%-5d %s: entering state: Active"
- "%25s:%-5d %s: entering: %s"
- "%25s:%-5d %s: entering: Paused"
- "%25s:%-5d %s: entering: Pausing"
- "%25s:%-5d %s: entering: Running"
- "%25s:%-5d %s: entering: Starting"
- "%25s:%-5d %s: entering: StartingForPlay"
- "%25s:%-5d %s: entering: Stopping"
- "%25s:%-5d %s: eventID %u"
- "%25s:%-5d %s: eventID %u (key: %u vel: %u) is in layer %u, zone %u"
- "%25s:%-5d %s: failAction"
- "%25s:%-5d %s: finishAction: %s => %s"
- "%25s:%-5d %s: flushing client ID 0x%x, inRenderTime = %.4f"
- "%25s:%-5d %s: forceStopAction: %s => %s"
- "%25s:%-5d %s: found and local refcount now zero, so unref'ing on evt mgr"
- "%25s:%-5d %s: found but local refcount still > 0"
- "%25s:%-5d %s: found it: refcount will be %u"
- "%25s:%-5d %s: inRenderTime - _flushRequestTime > %.4f, so ready to finish"
- "%25s:%-5d %s: init count -> %u"
- "%25s:%-5d %s: initialized"
- "%25s:%-5d %s: instanceID: %u channel: %u offset: %u"
- "%25s:%-5d %s: invoking callback %p with eventID %u and error %@"
- "%25s:%-5d %s: invoking callback %p with seqID %u, channelCount %u, and error %@"
- "%25s:%-5d %s: invoking callback %p with sharedBufferSize %u and error %@"
- "%25s:%-5d %s: isCharging: %d"
- "%25s:%-5d %s: isLooped guard: returning %d"
- "%25s:%-5d %s: isNotLooped guard: returning %d"
- "%25s:%-5d %s: isRecording: %d"
- "%25s:%-5d %s: key: %@"
- "%25s:%-5d %s: key=%u value=%u"
- "%25s:%-5d %s: leaving state: Active"
- "%25s:%-5d %s: leaving: %s"
- "%25s:%-5d %s: leaving: Flushing - resetting flush time"
- "%25s:%-5d %s: leaving: Paused"
- "%25s:%-5d %s: leaving: Pausing"
- "%25s:%-5d %s: leaving: Running"
- "%25s:%-5d %s: leaving: Starting"
- "%25s:%-5d %s: leaving: StartingForPlay"
- "%25s:%-5d %s: leaving: Stopping"
- "%25s:%-5d %s: loadAction"
- "%25s:%-5d %s: logging engine on duration %f for %@ to PowerLog..."
- "%25s:%-5d %s: mSomeoneIsRecording -> %d"
- "%25s:%-5d %s: micIsActive: %d"
- "%25s:%-5d %s: moving user event to beat %.2f"
- "%25s:%-5d %s: numEnvelopes: %u"
- "%25s:%-5d %s: parameter curve has only 1 control point - setting this parameter instead"
- "%25s:%-5d %s: params ID: %u, param value: %.2f, volumeCompensation: %.2f, final output param value: %.2f"
- "%25s:%-5d %s: pauseAction: %s => %s"
- "%25s:%-5d %s: pausing events on channel: %u"
- "%25s:%-5d %s: peakPowerBudgetMax not found found from user client"
- "%25s:%-5d %s: peakPowerBudgetMin not found found from user client"
- "%25s:%-5d %s: preRender: sequence play failed for Sequence ID %u"
- "%25s:%-5d %s: preRender::play failed for Sequence ID %u with offset %f seconds"
- "%25s:%-5d %s: prepareAction"
- "%25s:%-5d %s: prepareResetAction"
- "%25s:%-5d %s: preparedDestroyAction: %s => %s"
- "%25s:%-5d %s: preparedPlayAction: %s => %s"
- "%25s:%-5d %s: queries: %@"
- "%25s:%-5d %s: rePlayAction: %s => %s"
- "%25s:%-5d %s: refcount zero so disabling and removing"
- "%25s:%-5d %s: removing callback %p for context %p"
- "%25s:%-5d %s: resetAction"
- "%25s:%-5d %s: resetting mute map for channel %u"
- "%25s:%-5d %s: resumeAction: %s => %s"
- "%25s:%-5d %s: resuming events on channel: %u"
- "%25s:%-5d %s: seekAction: %s => %s"
- "%25s:%-5d %s: seqEndedAction: %s => %s"
- "%25s:%-5d %s: seqID: %lu"
- "%25s:%-5d %s: seqID: %lu events %p"
- "%25s:%-5d %s: seqID: %lu flushing: time = %.3f"
- "%25s:%-5d %s: seqID: %lu force-stopped"
- "%25s:%-5d %s: seqID: %lu midiData %p"
- "%25s:%-5d %s: seqID: %lu running - clearing events, disabling loop and seeking to end to force flush"
- "%25s:%-5d %s: seqID: %lu vibe pattern %p"
- "%25s:%-5d %s: seqID: %lu, loop: %d, loopCount: %d"
- "%25s:%-5d %s: seqID: %lu, loopLength: %.2f seconds"
- "%25s:%-5d %s: seqID: %lu, startOffsetTime: %f, startSkipTime: %f"
- "%25s:%-5d %s: seqID: %u pausing"
- "%25s:%-5d %s: seqID: %u ramping in for end of pause"
- "%25s:%-5d %s: seqID: %u ramping out for pause"
- "%25s:%-5d %s: seqID: %u resuming"
- "%25s:%-5d %s: seqID: %u seeking to %lf"
- "%25s:%-5d %s: sequence channel active during flush -- resetting _flushTime"
- "%25s:%-5d %s: server side metrics DISABLED"
- "%25s:%-5d %s: server side metrics ENABLED"
- "%25s:%-5d %s: setEventInfo returned %d"
- "%25s:%-5d %s: setting track %u loop start to %.2f beats and end to %.2f beats"
- "%25s:%-5d %s: setting volume base multiplier to %.2f"
- "%25s:%-5d %s: startAction: %s => %s"
- "%25s:%-5d %s: startingPlayAction: %s => %s"
- "%25s:%-5d %s: startingSeqEndedAction: %s => %s"
- "%25s:%-5d %s: stopAction: %s => %s"
- "%25s:%-5d %s: stopping client ID 0x%x, _hasNoActiveEvents = %d, someSequenceActive = %d, inRenderTime = %.4f"
- "%25s:%-5d %s: synchronizer %d is ready to play with offset of %d"
- "%25s:%-5d %s: synchronizer %d is ready to play with zero offset"
- "%25s:%-5d %s: synchronizer %d offset %lld > frame count (%u) -- returning silence"
- "%25s:%-5d %s: synthFormat info: %s"
- "%25s:%-5d %s: synthParamID: %u (input value: %.4f) AU value: %.4f channel: %u offset: %u"
- "%25s:%-5d %s: synthParamID: %u channel: %u frameOffset: %u points: %u, clientID: %lu"
- "%25s:%-5d %s: this = %p, client ID: 0x%x"
- "%25s:%-5d %s: this = %p, client ID: 0x%x behaviors: 0x%x"
- "%25s:%-5d %s: this = %p, haptic: %d, clientID: 0x%x, prewarmed: %d"
- "%25s:%-5d %s: unPauseAction: %s => %s"
- "%25s:%-5d %s: zero length param curve - ignoring"
- "%25s:%-5d -> Incoming Request : SSID %d, inClientPID %d(%s), behaviorID %d, customHapticsProvided %d, loop %d, loopPeriod %f, inFlags %u, SSCoreHapticsPlayer %p"
- "%25s:%-5d AQMEDevice: couldn't initialize processor (%d)"
- "%25s:%-5d Audio player completion handler called. SSID %d"
- "%25s:%-5d AudioFileReadPackets:result %d"
- "%25s:%-5d Both sound and haptic flags are false for SSID %d, behaviorID: %d, SSCoreHapticsPlayer %p"
- "%25s:%-5d Cannot create haptic dictionary. error: %@"
- "%25s:%-5d Cannot initialize CHHapticEngine. error: %@"
- "%25s:%-5d Cannot start %@ portion for SSID %d, SSCoreHapticsPlayer %p, error %@"
- "%25s:%-5d Cannot start SSCoreHapticsPlayer %p for SSID %d, error %@"
- "%25s:%-5d Creating haptic dictionary from JSON or AHAP..."
- "%25s:%-5d Creating new system sound. Audio: %@"
- "%25s:%-5d DSP_Routing_VP creating mRequestedDSPOffloadListener to listen for kAudioDevicePropertyDSPOffloadRequested changes on deviceID %u"
- "%25s:%-5d Destroying SSCoreHapticsPlayer %p"
- "%25s:%-5d Disabling audio for SSID %d, SSCoreHapticsPlayer %p as suppress audio flag is set"
- "%25s:%-5d Disabling haptics for SSID %d, SSCoreHapticsPlayer %p as suppress haptic flag is set"
- "%25s:%-5d ERROR: Haptic server master is nil - cannot stop!"
- "%25s:%-5d EXCEPTION (%d) [error != noErr is false]: \"\""
- "%25s:%-5d EnhanceDialogueProcessor() - Product does not have valid tuning"
- "%25s:%-5d Error creating AQAC3IONode for binding: %s"
- "%25s:%-5d Error playing SSID %d. status %d"
- "%25s:%-5d Failed to create audio player and continue. error: %@"
- "%25s:%-5d Getting a notification for kAudioDevicePropertyDSPOffloadRequested property change"
- "%25s:%-5d Haptic player completion handler called. SSID %d"
- "%25s:%-5d Incoming ahapURL not a valid file path URL or file type not supported. Not creating haptic portion"
- "%25s:%-5d InputConverter: AudioBufferList sizes don't match: %i != %i"
- "%25s:%-5d Invalid audio pattern. Not creating audio player and continue. error: %@"
- "%25s:%-5d Invalid audio resource. Not creating audio player and continue. error: %@"
- "%25s:%-5d Invalid haptic pattern. Not creating haptic player and continue. error: %@"
- "%25s:%-5d No haptic dictionary passed in"
- "%25s:%-5d No player associated with SSID %ld"
- "%25s:%-5d Requested offload AirPods noise suppression mode is updated to = %s"
- "%25s:%-5d SSCoreHapticsPlayer %p: Lost connection with server. re-creating players"
- "%25s:%-5d SSCoreHapticsPlayer invalid!"
- "%25s:%-5d SSID %d, SSCoreHapticsPlayer %p, shouldPlayAudio %d, shouldPlayHaptics %d, clientVolumeScalar %f, needsUnduckCall %d, interruptCurrentSystemSounds %d"
- "%25s:%-5d STSpeechTranslatorClient@%p: Received %d number of samples, abl %lu"
- "%25s:%-5d STSpeechTranslatorClient@%p: Translate %d number of samples"
- "%25s:%-5d STSpeechTranslatorClient@%p: lookUpPreferredInputAudioFormatWithCompletionHandler succeeded but format is null!"
- "%25s:%-5d STSpeechTranslatorClient@%p: lookUpPreferredInputAudioFormatWithCompletionHandler succeeded with format: %s"
- "%25s:%-5d STSpeechTranslatorClient@%p: lookUpPreferredInputAudioFormatWithCompletionHandler timed out!"
- "%25s:%-5d STSpeechTranslatorClient@%p: server disconnected"
- "%25s:%-5d STSpeechTranslatorClient@%p: set state %d"
- "%25s:%-5d STSpeechTranslatorClient@%p: setting client's produceAudio value to %i for scope %s"
- "%25s:%-5d STSpeechTranslatorClient@%p: translation did stop with error: %d"
- "%25s:%-5d Starting audio: SSID %u, behaviorID %u, SSCoreHapticsPlayer %p, clientVolumeScalar %f"
- "%25s:%-5d Starting haptics: SSID %u, behaviorID %u, SSCoreHapticsPlayer %p"
- "%25s:%-5d Stopping SSID %u, SSCoreHapticsPlayer %p. stopNow: %d"
- "%25s:%-5d System sound finished playing, SSID %d, SSCoreHapticsPlayer %p"
- "%25s:%-5d TranslatorClientDelegate::didGenerateTranslatedAudio; scope: %s"
- "%25s:%-5d Unexpected mode: %@. Please file a radar to Audio - Session | All component"
- "%25s:%-5d aqmeio@%p * * * * * kAudioDevicePropertyIOStoppedAbnormally fired * * * * *"
- "%25s:%-5d audio duration: %.2fs"
- "%25s:%-5d audioURL not valid"
- "%25s:%-5d disposing SSID %ld and its SSCoreHapticsPlayer"
- "%25s:%-5d haptic duration: %.2fs"
- "%25s:%-5d null mixmap from %s | %s"
- "%25s:%-5d obj 0x%x, addr %s, qual %d@%p, size %d: %s"
- "%25s:%-5d playOptions contain haptic pattern identical to the one stored in SSCoreHapticsPlayer %p. NOT recreating haptic player"
- "%25s:%-5d registering SSID %ld <-> SSCoreHapticsPlayer %p"
- "%25s:%-5d return dictionary is null"
- "%25s:%-5d useCaseID: %s, deviceID: %d"
- "%X"
- "%s:0x%x:%s"
- "'%s' | %sData{%d} | %d bytes\n"
- "'%s' | <unknown type id: %d)>\n"
- "'%s' | Array{%d} | %d ordered objects\n"
- "'%s' | Dictionary{%d} | %d key/value pairs\n"
- "'%s' | Number(SInt16){%d} | 0x%04x\n"
- "'%s' | Number(SInt32){%d} | %-6d 0x%08x %c%c%c%c\n"
- "'%s' | Number(SInt8){%d} | 0x%02x\n"
- "'%s' | Number(float){%d} | %f\n"
- "'%s' | String{%d} | \"%s\"\n"
- "(notify_register_dispatch(\"com.apple.accessibility.hac.status\", &token, AudioControlQueue(), ^(int token) { AT::ScopedACQBlock scopedACQBlock(\"notify_register_dispatch\", __func__, \"DSP_Routing_VP.cpp\" , 491); do { auto logobj = CALog::LogObjIfEnabled(5, gAQMELogScope); if (logobj) __extension__({ os_log_t _log_tmp = ((logobj)); os_log_type_t _type_tmp = (OS_LOG_TYPE_DEBUG); if (os_log_type_enabled(_log_tmp, _type_tmp)) { __extension__({ _Pragma(\"clang diagnostic push\") _Pragma(\"clang diagnostic ignored \\\"-Wvla\\\"\") _Pragma(\"clang diagnostic error \\\"-Wformat\\\"\") _Static_assert(__builtin_constant_p(\"%25s:%-5d \" \"HACStatusChanged %p\"), \"format/label/description argument must be a string constant\"); __attribute__((section(\"__TEXT,__oslogstring,cstring_literals\"),internal_linkage)) static const char _os_fmt_str[] __asm(\"LOS_LOG880\") = \"%25s:%-5d \" \"HACStatusChanged %p\"; uint8_t _Alignas(16) __attribute__((uninitialized)) _os_fmt_buf[__builtin_os_log_format_buffer_size(\"%25s:%-5d \" \"HACStatusChanged %p\", \"DSP_Routing_VP.cpp\", 492, gInstance.load())]; _os_log_impl(&__dso_handle, _log_tmp, _type_tmp, _os_fmt_str, (uint8_t *)__builtin_os_log_format(_os_fmt_buf, \"%25s:%-5d \" \"HACStatusChanged %p\", \"DSP_Routing_VP.cpp\", 492, gInstance.load()), (uint32_t)sizeof(_os_fmt_buf)) _Pragma(\"clang diagnostic pop\"); }); } }); } while (0); std::unique_lock locker1(mgr.GetMutex()); if (gInstance) { gInstance.load()->mParent.TriggerAdaptToDevice(); } })) == 0"
- "* * TempoTrack * *\n"
- "* * Track %d * *\n"
- "*** done.\n"
- ", %d channels, sr=%.f Hz"
- "-[AVHapticServer init]_block_invoke"
- "-[AVHapticServer shouldUnprewarmAllClientsAfterDisplayingPrewarmedProcessEntriesWithPrewarmTime:]"
- "-[AVHapticServerInstance dealloc]"
- "-[AVHapticServerInstance handleClientRouteChange:]"
- ".cxx_construct"
- ".cxx_destruct"
- ".plist"
- "/Library/Audio/Tunings/Generic/Haptics/SystemSounds/Library/systemsoundhapticpatterns.plist"
- "1"
- "2"
- "2A$0"
- "; %d packets (capacity %d) @%p"
- "; enqueue count=%d\n"
- "<OfflineMixer@%p>\n"
- "<Queue@%p>\n"
- "<SubmixTap@%p>\n"
- "<empty>"
- "@"
- "@\"<CHHapticAdvancedPatternPlayerExtended>\""
- "@\"<PHASERoomCongruenceInterface>\"16@0:8"
- "@\"<PHASESessionInterface>\"16@0:8"
- "@\"<PHASESessionVolumeInterface>\"16@0:8"
- "@\"<PHASEStreamInfo>\"24@0:8I16C20"
- "@\"<UplinkSpeechMixer>\"16@0:8"
- "@\"ATAudioSessionClientImpl\""
- "@\"ATAudioSessionPropertyManager\""
- "@\"ATAudioTapDescription\""
- "@\"ATPhasePlatform\""
- "@\"AVAudioFormat\""
- "@\"AVAudioFormat\"16@0:8"
- "@\"AVAudioSession\""
- "@\"AVAudioSessionSpatialPreferences\"24@0:8I16I20"
- "@\"AVHapticServer\""
- "@\"AVHapticServerInstance\""
- "@\"AVServerWrapper\""
- "@\"CHHapticEngine\""
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSDictionary\"28@0:8I16@\"NSDictionary\"20"
- "@\"NSError\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\"24@0:8I16B20"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@\"NSXPCInterface\""
- "@\"NSXPCListener\""
- "@\"OS_os_workgroup\"16@0:8"
- "@\"PHASESessionVolume\"24@0:8@\"PHASEVolumeCommand\"16"
- "@\"SWSystemSleepMonitor\""
- "@\"VTStateManager\""
- "@16@0:8"
- "@20@0:8I16"
- "@20@0:8{ATIsolatedAudioUseCaseID=I}16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8I16B20"
- "@24@0:8I16C20"
- "@24@0:8I16I20"
- "@24@0:8Q16"
- "@28@0:8@16B24"
- "@28@0:8@16I24"
- "@28@0:8@16i24"
- "@28@0:8I16@20"
- "@32@0:8:16@24"
- "@32@0:8:16@?24"
- "@32@0:8@16@24"
- "@32@0:8@16q24"
- "@32@0:8^{OpaqueFigSTS=}16^@24"
- "@32@0:8{shared_ptr<const AT::IOBinding::Impl>=^{Impl}^{__shared_weak_count}}16"
- "@36@0:8@16@24i32"
- "@36@0:8@16I24@28"
- "@36@0:8@16i24@28"
- "@36@0:8Q16f24@?28"
- "@36@0:8r^{AudioStreamBasicDescription=dIIIIIIII}16I24^@28"
- "@36@0:8{weak_ptr<AT::Translation::TranslatorClient>=^{TranslatorClient}^{__shared_weak_count}}16i32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24^@32"
- "@40@0:8r^{AudioStreamBasicDescription=dIIIIIIII}16I24B28^@32"
- "@48@0:8@16@24I32I36@40"
- "@48@0:8@16Q24@32^@40"
- "@60@0:8f16B20^v24^?32^?40^?48B56"
- "@?"
- "@?16@0:8"
- "@@ Strips Apr 18 2026 17:45:53"
- "AID0"
- "AQInternalGetOfflineBufferCompletions"
- "AQInternalPreflightOfflineRender"
- "AQInternalScheduledStart"
- "AQProcessingNode@%p\n"
- "AQProcessingTap@%p\n"
- "AQProcessingTapManager"
- "AQServer_CheckStopFromPause"
- "ATAudioSessionClientImpl"
- "ATAudioSessionPropertyManager"
- "ATAudioSessionUtils"
- "ATAudioTap"
- "ATAudioTapDescription"
- "ATBlurMixer"
- "ATIOBinding"
- "ATPhasePlatform"
- "ATServerDelegatePriv"
- "ATSpatialStreamDescriptions"
- "ATSpatialStreamParameters"
- "AUPreset"
- "AVAudioSessionServerDelegate"
- "AVHapticServer"
- "AVHapticServerInstance"
- "AVServerWrapper"
- "AVVoiceTriggerServer"
- "AVVoiceTriggerServerHysteresisNotifier"
- "AVVoiceTriggerServerPortManager"
- "ActiveExit"
- "AddPropertyListener"
- "After"
- "AssignToSubmixTap_block_invoke"
- "AudioDSPGraph"
- "AudioDSPGraphFramework_AudioDSP"
- "AudioQueueCheckSpatializationAfterRouteChange"
- "AudioQueueDeassignFromSubmixTap_block_invoke"
- "AudioQueueInternalDeliverProcessingNodeEvents"
- "AudioQueueInternalNotifyRunning"
- "AudioQueueInternalPause"
- "AudioQueueInternalReleasePlayResources"
- "AudioQueueInternalStop_Sync_block_invoke"
- "AudioQueueNotifyReadyToRestart"
- "AudioQueueSiriListeningPropertyChanged_block_invoke"
- "AudioSessionAddPropertyListenerImpl:userProc:userData:"
- "AudioSessionGetPropertyImpl:size:data:"
- "AudioSessionGetPropertySizeImpl:size:"
- "AudioSessionOnMac"
- "AudioSessionRemovePropertyListenerImpl:"
- "AudioSessionRemovePropertyListenerWithUserDataImpl:userProc:userData:"
- "AudioSessionSetActiveImpl:flags:"
- "AudioSessionSetPropertyImpl:size:data:"
- "AudioUnitGraph 0x%lX:\n"
- "B16@0:8"
- "B20@0:8I16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8@?16"
- "B24@0:8@?<B@?@\"PHASEVolumeCommand\">16"
- "B24@0:8@?<i@?IBf>16"
- "B24@0:8@?<i@?IBff>16"
- "B24@0:8@?<v@?>16"
- "B24@0:8@?<v@?@\"<PHASERouteChangeInfo>\">16"
- "B24@0:8@?<v@?IB>16"
- "B24@0:8@?<v@?^{PHASEIOCycleInfo={AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}Q}Q^{PHASEIOStream={AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}IB^{AudioBufferList}}Q^{PHASEIOStream={AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}IB^{AudioBufferList}}>16"
- "B24@0:8B16C20"
- "B24@0:8Q16"
- "B24@0:8^@16"
- "B28@0:8I16@20"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B32@0:8I16B20^@24"
- "B32@0:8I16^v20B28"
- "B32@0:8Q16Q24"
- "B32@0:8r^{AudioStreamBasicDescription=dIIIIIIII}16^@24"
- "B36@0:8@16@24f32"
- "B36@0:8@16I24^@28"
- "B36@0:8d16B24^@28"
- "B40@0:8@16@24^@32"
- "B40@0:8^{STSGlobalState=Q{?=[4]}}16^B24^@32"
- "B40@0:8r^{STSGlobalState=Q{?=[4]}}16^B24^@32"
- "B40@0:8r^{STSGlobalState=Q{?=[4]}}16r^v24^@32"
- "B44@0:8I16^v20I28I32^{AudioSessionDuckingInfo=Bff}36"
- "B48@0:8^{__CFString=}16^{STSPerLabelState={?=[4]}Iff}24^B32^@40"
- "B48@0:8r^{STSGlobalState=Q{?=[4]}}16r^v24@32^@40"
- "B56@0:8^{__CFString=}16r^{STSPerLabelState={?=[4]}Iff}24^B32@40^@48"
- "Bend"
- "CAException"
- "CHHapticClientInterface"
- "CHHapticServerInterface"
- "ClientEntry"
- "ClientMap"
- "Copy"
- "CorrectTimePitchUnflushedFrames"
- "CreateActiveSoundEntry"
- "CreateTimeline"
- "Ctrl"
- "D23"
- "DebugPrint"
- "Default-"
- "Delete"
- "Device-"
- "DeviceGetCurrentTime"
- "DeviceGetNearestStartTime"
- "DeviceIsRunning"
- "DeviceTranslateTime"
- "DisposeQueue_block_invoke"
- "DisposeTimeline"
- "DoRenderProc"
- "Ending power check for high-power client"
- "Error loading plist file "
- "Event track not found, earlier code should have added one"
- "Failed to construct AQAC3IONode"
- "Flush"
- "GetCurrentTime"
- "GetMaxIOBufferFrameSize"
- "GetNearestStartTime"
- "GetParameter"
- "GetPendingCallbackMessages"
- "GetProperty"
- "GetProperty:size:data:"
- "GetPropertySize"
- "GetSampleRanges"
- "GetSampleRate"
- "GetStreamFormat"
- "GetTotalNumberChannels"
- "HandleAQGetParameter"
- "HandleAQGetProperty"
- "HandleAQScheduledParameters"
- "HandleAQSetParameter"
- "HandleAQSetProperty"
- "HandleInterruptionForSession:command:dictionary:"
- "HapticMetrics"
- "HapticMetrics_block_invoke_2"
- "I16@0:8"
- "I20@0:8C16"
- "I20@0:8I16"
- "I24@0:8@16"
- "ID"
- "IONode_ConfigAboutToChange_block_invoke"
- "JSONObjectWithData:options:error:"
- "KVOProperties"
- "KeyP"
- "LatencySamples"
- "MapSharedBuffers"
- "MaximumSupportedBatteryBudget100ms"
- "MaximumSupportedBatteryBudget1ms"
- "MinimumSupportedBatteryBudget100ms"
- "MinimumSupportedBatteryBudget1ms"
- "MixerConnectQueue_block_invoke"
- "MixerDispose"
- "MixerGetProperty"
- "MixerGetPropertySize"
- "MixerNew"
- "MixerRender"
- "MixerReset"
- "MixerSetProperty"
- "MultiOutputHapticSynth.cpp"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "NSXPCListenerDelegate"
- "NewQueue"
- "No power check change for low-power client"
- "Noise Suppression"
- "Noise Suppression Studio"
- "NotifyMicrophoneInjectionPermissionChanged"
- "NumTracks = %d, Type = %s\n"
- "OffloadActivationOffACQ"
- "PHASEPlatform"
- "PHASERoomCongruenceInterface"
- "PHASERoomCongruenceInterfaceImpl"
- "PHASERouteChangeInfo"
- "PHASERouteChangeInfoImpl"
- "PHASESessionInterface"
- "PHASESessionInterfaceImpl"
- "PHASESessionVolumeImpl"
- "PHASESessionVolumeInterface"
- "PHASEStreamInfo"
- "PHASEStreamInfoImpl"
- "Pause_block_invoke"
- "Paused"
- "Pausing"
- "PowerTimer_block_invoke"
- "Prgm"
- "Prime_block_invoke"
- "PriorityManagerPhone"
- "ProcessingNodeDispose"
- "ProcessingNodeInstantiate"
- "ProcessingTapDispose"
- "ProcessingTapInit"
- "ProcessingTapNew"
- "Q"
- "Q16@0:8"
- "Q20@0:8I16"
- "Q20@0:8i16"
- "Q24@0:8@16"
- "Q32@0:8@16^@24"
- "QueryTimePitchPullAheadEstimate"
- "QueueGetCurrentTime"
- "Recreate"
- "RemovePropertyListener"
- "SSCoreHapticsInfo"
- "SSCoreHapticsPlayer"
- "SSCoreHapticsPlayer.mm"
- "SSIDPlayerDictQueue"
- "STSController"
- "STSpeechTranslatorClientDelegate"
- "SWSystemSleepObserver"
- "ScaleOrUnscaleSampleTime"
- "Sequence @%p\n"
- "SequencePlayer\n"
- "SequenceTrack @%p\n"
- "ServerManager.h"
- "SetAudioQueue_block_invoke"
- "SetOfflineRenderFormat_block_invoke"
- "SetParameter"
- "SetProperty:size:data:"
- "SetRoutingBehavior"
- "SetTopologyFlags"
- "StartIO_Primitive"
- "Start_block_invoke"
- "Stop_block_invoke"
- "SynthOutput.cpp"
- "SystemSound"
- "SystemSoundMaximumVolume"
- "T#,&,N,V_clsVTStateManager"
- "T#,R"
- "T@\"<PHASERoomCongruenceInterface>\",?,R,N"
- "T@\"<PHASESessionInterface>\",?,R,N"
- "T@\"<PHASESessionVolumeInterface>\",?,R,N"
- "T@\"<PHASETapInterface>\",R,N,V_tapInterface"
- "T@\"ATAudioTapDescription\",R,N,V_tapDescription"
- "T@\"AVAudioFormat\",R,N"
- "T@\"AVAudioFormat\",R,N,V_flatFormat"
- "T@\"AVAudioFormat\",R,N,V_format"
- "T@\"AVAudioFormat\",R,N,V_streamFormat"
- "T@\"AVAudioSession\",R"
- "T@\"AVAudioSession\",R,&,N"
- "T@\"AVHapticServer\",R,V_master"
- "T@\"AVHapticServerInstance\",R,W,V_serverInstance"
- "T@\"CHHapticEngine\",R,V_engine"
- "T@\"NSArray\",C,N,V_excludedPIDs"
- "T@\"NSArray\",C,N,V_processIdentifiers"
- "T@\"NSArray\",R,N"
- "T@\"NSDictionary\",?,R,N"
- "T@\"NSDictionary\",?,R,N,V_streamDescription"
- "T@\"NSDictionary\",R,N"
- "T@\"NSMutableArray\",&,N,V_clientConnections"
- "T@\"NSMutableArray\",&,N,V_portsToMonitor"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_notificationQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,&,N"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_name"
- "T@\"NSString\",R,N,V_sceneIdentifier"
- "T@\"NSUUID\",R,N,V_UUID"
- "T@\"NSUUID\",R,N,V_identifier"
- "T@\"NSXPCListener\",&,N,V_serverListener"
- "T@\"OS_os_workgroup\",?,R,N"
- "T@\"VTStateManager\",&,N,V_vtStateManager"
- "T@?,C,N,V_notificationBlock"
- "T@?,R,N"
- "TB,N,GisBlurEnabled"
- "TB,N,GisScreenSharingHost,V_screenSharingHost"
- "TB,N,V_lastStateSent"
- "TB,N,V_listeningEnabled"
- "TB,R"
- "TB,R,N"
- "TB,R,N,GisEnabled"
- "TB,R,N,GisPreSpatial,V_preSpatial"
- "TB,R,N,V_isUplink"
- "TB,V_clientInterrupted"
- "TB,V_clientSuspended"
- "TB,V_isConfigured"
- "TB,V_prewarmIncludesAudio"
- "TB,V_prewarmIncludesHaptics"
- "TB,V_runIncludesAudio"
- "TB,V_runIncludesHaptics"
- "TB,V_runningInBackground"
- "TB,V_wasPrewarmedAndSuspended"
- "TB,V_wasRunningAndSuspended"
- "TI,N"
- "TI,R,N"
- "TI,R,N,V_audioSessionID"
- "TI,R,N,V_latencyInFrames"
- "TI,R,N,V_sessionType"
- "TI,V_interruptionType"
- "TPLM"
- "TQ,N,V_portType"
- "TQ,R"
- "TQ,R,V_clientID"
- "TQ,R,V_initCount"
- "TQ,R,V_ssid"
- "T^?,N,V_afSiriActivationBuiltInMicVoiceFuncPtr"
- "T^?,V_clientInterruptionListenerProc"
- "T^v,N,V_mobileAssistantDylib"
- "T^v,N,V_voiceTriggerDylib"
- "T^v,R,V_manager"
- "T^v,V_clientUserData"
- "Td,R,N"
- "Tf,N"
- "Tf,N,V_hysteresisDurationSeconds"
- "Ti,N"
- "Time %.3f:\n"
- "Tq,N,V_generation"
- "Tq,N,V_muteBehavior"
- "Tq,R"
- "Tq,R,N,V_tapType"
- "Tq,R,N,V_type"
- "TrackIterator\n"
- "TranslateTime"
- "TranslatorClientDelegate"
- "TuningPListMgr.cpp"
- "T{ATIsolatedAudioUseCaseID=I},R,N"
- "T{AudioStreamBasicDescription=dIIIIIIII},N"
- "UTF8String"
- "UUIDString"
- "Unprewarming"
- "UplinkSpeechMixerFactory"
- "UsageCategory"
- "VibeSynthEngine"
- "VoiceTriggerInterface"
- "VoiceTriggerNotificationInterface"
- "Vv16@0:8"
- "[ "
- "[%u]"
- "^?"
- "^?16@0:8"
- "^v"
- "^v16@0:8"
- "^{AVVoiceTriggerServerImpl=^^?I^{HALListener}^{HALListener}^{HALListener}i**BBBBB@@i^{unfair_recursive_lock}@BI@}"
- "^{OpaqueAudioComponentInstance=}16@0:8"
- "^{OpaqueFigSTS=}"
- "^{PowerTimer=@@B}"
- "^{_NSZone=}16@0:8"
- "^{__CFString=}28@0:8@16B24"
- "_InternalDispose_block_invoke"
- "_SSIDMapQueue"
- "_SSIDToPlayerMap"
- "_SSSClientID"
- "_UUID"
- "_activateSessionBlock"
- "_activeIndices"
- "_afSiriActivationBuiltInMicVoiceFuncPtr"
- "_allowAutomaticHeadTracking"
- "_aqmeSession"
- "_audioPatternDuration"
- "_audioPlaybackFinished"
- "_audioPlayer"
- "_audioPrewarmCount"
- "_audioResourceID"
- "_audioRunningCount"
- "_audioSessionID"
- "_audioURL"
- "_availableIndicesWithinSharedStorage"
- "_cachedClientInterface"
- "_cachedServerInterface"
- "_callbackMutex"
- "_clientCompletionToken"
- "_clientConnections"
- "_clientID"
- "_clientInterrupted"
- "_clientInterruptionListenerProc"
- "_clientRunLoop"
- "_clientRunLoopMode"
- "_clientSession"
- "_clientSuspended"
- "_clientUserData"
- "_clsVTStateManager"
- "_conclaveLaunchCondVar"
- "_conclaveLaunchMutex"
- "_conclaveLaunched"
- "_connection"
- "_controlSemaphore"
- "_currentAudioListenerPose:timestamp:"
- "_description"
- "_engine"
- "_excludedPIDs"
- "_fadeSessionOutputBlock"
- "_flatFormat"
- "_format"
- "_generation"
- "_globalGeneration"
- "_globalState"
- "_hapticPatternDict"
- "_hapticPatternDuration"
- "_hapticPlaybackFinished"
- "_hapticPlayer"
- "_hapticSession"
- "_hapticsPrewarmCount"
- "_hapticsRunningCount"
- "_hysteresisDurationSeconds"
- "_identifier"
- "_impl"
- "_initCount"
- "_initWithOptions:"
- "_instanceMap"
- "_instanceMutex"
- "_interruptionType"
- "_isConfigured"
- "_isUplink"
- "_lastStateSent"
- "_latencyInFrames"
- "_listener"
- "_listenerWrapper"
- "_listeningEnabled"
- "_manager"
- "_master"
- "_mobileAssistantDylib"
- "_muteBehavior"
- "_muteSessionInputBlock"
- "_name"
- "_newNotificationCenterObservers"
- "_notificationBlock"
- "_notificationQueue"
- "_oldNotificationCenterObservers"
- "_perLabelState"
- "_phasePlatform"
- "_portType"
- "_portsToMonitor"
- "_powerTimer"
- "_preSpatial"
- "_prewarmIncludesAudio"
- "_prewarmIncludesHaptics"
- "_processIdentifiers"
- "_processIndexMap"
- "_propertyListeners"
- "_propertyManager"
- "_queue"
- "_roomCongruenceInterface"
- "_routeUsesReceiver"
- "_runIncludesAudio"
- "_runIncludesHaptics"
- "_runningChannelIDCount"
- "_runningInBackground"
- "_savedError"
- "_sceneIdentifier"
- "_screenSharingHost"
- "_serverInstance"
- "_serverListener"
- "_serverManager"
- "_sessionInterface"
- "_sessionType"
- "_sessionVolumeImpl"
- "_sharedStorage"
- "_shmemSize"
- "_shouldPlayAudioFinal"
- "_shouldPlayHapticsFinal"
- "_sleepMonitor"
- "_ssid"
- "_start"
- "_stop"
- "_streamDescription"
- "_streamFormat"
- "_streamParameters"
- "_strongSession"
- "_sts"
- "_tapDescription"
- "_tapInterface"
- "_tapType"
- "_type"
- "_updateGlobalState:didChange:error:"
- "_voiceTriggerDylib"
- "_vtStateManager"
- "_wasPrewarmedAndSuspended"
- "_wasRunningAndSuspended"
- "_weakSession"
- "absoluteString"
- "acknowledgePowerBudget:forClientId:error:"
- "activateSecureSession:reply:"
- "activateSession:activate:"
- "active sequence(s)"
- "activeInterfaceOrientationWithCompletion:"
- "addAVAudioSessionKVOObservers:session:"
- "addListener:forAudioSessionID:"
- "addNSNotificationListenerFor:session:block:"
- "addNSNotificationListenerFor:session:selector:"
- "addObject:"
- "addObserver:"
- "addObserver:forKeyPath:options:context:"
- "addObserver:selector:name:object:"
- "addObserverForName:object:queue:usingBlock:"
- "addPortToMonitor:hysteresisDurationSeconds:notificationBlock:"
- "addProcessEntry:"
- "addSequenceToActiveList"
- "afSiriActivationBuiltInMicVoiceFuncPtr"
- "ahap"
- "allKeys"
- "allocateClientResources:"
- "allowEnhanceDialogue:"
- "appendFormat:"
- "appendString:"
- "applyVolumeOnAllSessions"
- "applyVolumeOnSession:"
- "applyVolumeOnVolumeCategory:mode:value:"
- "aq"
- "aq_enq"
- "aq_input"
- "aqtap-"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "arrayByAddingObjectsFromArray:"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "audioBufferList"
- "audioGenerationDidFinishForClient:"
- "audioSessionInputClients"
- "audioUnit"
- "auditToken"
- "aupreset"
- "autorelease"
- "auxiliarySession"
- "avas"
- "bad key"
- "beats"
- "beginStop"
- "bitset test argument out of range"
- "blendTimeMs"
- "bluetoothAlternateTransportMode"
- "bluetoothUserHeadTrackingModeForBundleID"
- "bluetoothUserSpatialModeForBundleID"
- "blurHoldTimeSec"
- "boolValue"
- "boost"
- "bufferFrameSize"
- "bundle"
- "bytes"
- "cStringUsingEncoding:"
- "calculateSampleOffset"
- "calibrationData"
- "callFinishedCallback"
- "callNotificationBlock:"
- "callPropertyListeners:data:"
- "cancelPatternWithOptions:"
- "cancelled"
- "categories"
- "channelCount"
- "checkBooleanEntitlementForSession:entitlementIdentifier:"
- "checkForFinish"
- "checkMicrophoneInjectionPermission"
- "checkRunningCountAndStopSynth"
- "class"
- "classesForSelector:argumentIndex:ofReply:"
- "cleanup"
- "cleanupAllLabels"
- "cleanupDeactivatedSynthOutputs"
- "cleanupLabel:"
- "cleanupToBeDetachedChannels"
- "clearCommandsForClient"
- "clearCustomAudioEvents"
- "clearSequences"
- "clearSoundingEvents"
- "client:didGenerateTranslatedAudio:"
- "client:didPauseTranslationWithReason:"
- "client:didReceiveTranscriptionResult:"
- "client:didReceiveTranslationResult:"
- "client:didStopTranslationWithError:"
- "client:willStartTranslatedAudioWithMetadata:"
- "clientCompletedWithError:"
- "clientConnections"
- "clientDisconnectingForReason:error:"
- "clientID"
- "clientInterrupted"
- "clientInterruptionListenerProc"
- "clientStoppedForReason:error:"
- "clientSuspended"
- "clientUserData"
- "clsVTStateManager"
- "code"
- "com.apple.coreaudio.utility"
- "conclaveLaunched"
- "configurationDictionary"
- "configure"
- "configureWithOptions:reply:"
- "conformsToProtocol:"
- "connectedWiredDeviceIsHeadphone"
- "contains:"
- "containsString:"
- "controlPoints"
- "copy"
- "copyAttributeForKey:withValueOut:"
- "copyCMSession:"
- "copyCustomAudioEvent:options:reply:"
- "copyPowerBudgetForRequest:forClient:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createAdvancedPlayerWithPattern:error:"
- "createAdvancedPlayerWithVibePatternDictionary:error:"
- "createAudioPlayerAndReturnError:"
- "createAudioResource:error:"
- "createCoreMXSession:type:"
- "createCoreMXSessionForPID:"
- "createCustomAudioEvent:format:frames:options:reply:"
- "createHapticPlayer:error:"
- "createServerWithAudioControlQueue:delegate:"
- "createTimestampWriterForDevice:halID:isDecoupledInput:"
- "createUplinkSpeechMixer"
- "currentConnection"
- "currentHandler"
- "currentTime"
- "customEventIDMap"
- "customHRTFMode"
- "d16@0:8"
- "dataWithContentsOfFile:"
- "dataWithContentsOfFile:options:error:"
- "deactivate-SetActiveWithFlags"
- "dealloc"
- "debugDescription"
- "debugExpectNotifyOnFinishAfter:reply:"
- "decodeBoolForKey:"
- "decodeInt32ForKey:"
- "decodeIntForKey:"
- "decodeObjectForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decrementInit"
- "decrementPrewarmCountAndStopAudio:stopHaptics:entry:"
- "decrementRunningCountAndStopAudio:stopHaptics:entry:"
- "defaultCStringEncoding"
- "defaultCenter"
- "defaultFaceToDevicePitchAngle"
- "description"
- "destroyCMSessionForPID:sessionID:"
- "destroySession:auditToken:"
- "destroyTimestampWriterForDevice:"
- "detach"
- "detachSequence:"
- "deviceID"
- "deviceLatencyInFramesForDirection:"
- "deviceOrientationBlocking"
- "dictionary"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "disableAndRemoveCustomAudioEvent"
- "disableStream"
- "disableUserCallback"
- "displayRunningProcessEntriesWithOnTime:"
- "disposeSSID:"
- "doEnableLooping"
- "doFinish"
- "doFlush"
- "doInit:haptic:error:"
- "doPause"
- "doPlay"
- "doPrepare"
- "doPrepareSequence"
- "doPrewarm:"
- "doReleaseClientResources:"
- "doReplay"
- "doResume"
- "doSeek"
- "doStart"
- "doStartRunning:completedBlock:"
- "doStop"
- "doStopPrewarm:audio:haptics:"
- "doStopRunning:audio:haptics:"
- "doStopRunningForInterrupt:audio:haptics:"
- "doesNotRecognizeSelector:"
- "dolbyDigitalEncoderAvailable"
- "doubleValue"
- "dumpProcessEntries:"
- "duration"
- "dynamicLatency"
- "dynamicLatencyForDevice:isInput:"
- "earlyUnduckAudioAtTime:error:"
- "enableBargeInMode:reply:"
- "enableBlur"
- "enableHeadTrackingMode"
- "enableIO:direction:"
- "enableListeningOnPorts:reply:"
- "enableLooping"
- "enableRendering"
- "enableSpeakerStateListening:reply:"
- "enableStreamWithIdentifier:error:"
- "enableSubRendering"
- "enableVoiceTriggerListening:reply:"
- "encodeBool:forKey:"
- "encodeInt32:forKey:"
- "encodeInt:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endPowerCheckForMedia"
- "engine"
- "ensureResourcesAllocatedForLabel:error:"
- "entryForID"
- "entryWithID:"
- "enumerateKeysAndObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "eventCategory"
- "eventListFromEvents:parameters:parameterCurves:engine:privileged:"
- "eventType"
- "events"
- "exportedInterface"
- "exportedObject"
- "f"
- "f16@0:8"
- "f20@0:8f16"
- "fadeClientForSessionInterruption:affectHaptics:fadeTime:fadeLevel:stopAfterFade:"
- "fadeClientsInSession:activating:fadeLevel:fadeTime:"
- "fadeForPause"
- "fadeInForResume"
- "failed"
- "filterUsingPredicate:"
- "filteredArrayUsingPredicate:"
- "firstObject"
- "fixedParamCount"
- "fixedParams"
- "flatFormat"
- "floatValue"
- "flushEntry"
- "forceStop"
- "force_haptification"
- "foundUserEvent == true"
- "frameLength"
- "general"
- "generateIOControllerEvent:forDevice:"
- "generateNewSSIDForPlayer:"
- "generation"
- "getAUStripPath"
- "getAVASCategory:"
- "getAVASMode:"
- "getAVASProperty:"
- "getAssignedChannelWithID"
- "getAsyncDelegateForMethod:errorHandler:"
- "getAudioOutput"
- "getAudioSessionCategory:"
- "getAudioSessionMode:"
- "getAudioSessionPortType:forInput:"
- "getAudioSessionProperty:"
- "getBuiltInAudioEventsDictionary"
- "getBusCountForScope:"
- "getCategoryOptionFromPropertyID:"
- "getChannelID"
- "getDSPGraphPath"
- "getDefaultMXSession:"
- "getDescriptionForSession:"
- "getDurationForResource:"
- "getHapticDictionaryFromURL:"
- "getHapticLatency:"
- "getHeadTracker"
- "getHeadTrackingSupport"
- "getInputChannelInfoCompletion:"
- "getInputMuteStateForSession:fromCallback:"
- "getJSONDescriptionForSession:"
- "getMappedObjectOf:inside:ofType:"
- "getMinimalRampDurationForValueDelta"
- "getPlayerForSSID:"
- "getPort:forInput:"
- "getPortManagerForType:"
- "getPorts:forInput:"
- "getPowerBudgets"
- "getPrimarySession:createIfNecessary:"
- "getPrimarySessionForPID:createIfNecessary:"
- "getPropStripPath"
- "getReturnValue:"
- "getRouteDescriptionFromAVASRouteDescription:"
- "getRouteStringFromAVASRouteDescription:"
- "getSequencerChannelForIndex"
- "getSessionIDsForToken:"
- "getSessionsWithMicrophoneInjectionPreference"
- "getSyncDelegateForMethod:errorHandler:"
- "getUUIDBytes:"
- "gqDnklGQnpv5ilgh5uHckw"
- "handleActiveMicrophoneChange"
- "handleCategoryOrModeChange:"
- "handleChargingStateChange"
- "handleClientApplicationStateChange:"
- "handleClientApplicationStateChangeUsingAppState:"
- "handleClientRouteChange:"
- "handleCommand"
- "handleConnectionError"
- "handleContinuityScreenStateChange"
- "handleFailureInFunction:file:lineNumber:description:"
- "handleFinish"
- "handleForIdentifier:error:"
- "handleForPredicate:error:"
- "handleInterruption:"
- "handleInterruptionForSession:command:dictionary:"
- "handleInterruptionWithID:clientPID:interruptionState:interruptionInfo:"
- "handlePhoneCallStateChange"
- "handleRecordingStateChange"
- "handleReleaseCustomAudioEvent"
- "handleResetChannelCommand"
- "handleRingerSwitchForEntry"
- "handleRouteChange:"
- "handleRouteChangeForEntry"
- "handleSequenceCommand"
- "handleSequenceEnded"
- "handleServerDeath:"
- "handleServerReset:"
- "handleSessionInterruptionForEntry"
- "handleSystemSleepMonitorDidWakeFromSleep"
- "haptic_audio_multi_output"
- "hapticengineconfig"
- "hardwareSupportsVoiceTrigger"
- "has active events"
- "hasDefaultOutputSpeakerPort"
- "hash"
- "hostProcess"
- "hysteresisDurationSeconds"
- "i16@0:8"
- "i20@0:8I16"
- "i24@0:8C16I20"
- "i24@0:8^{__CFDictionary=}16"
- "i24@0:8^{__CFString=}16"
- "i24@0:8r^{?=[8I]}16"
- "i28@0:8I16B20f24"
- "i28@0:8I16^I20"
- "i28@0:8I16i20B24"
- "i28@0:8q16I24"
- "i32@0:8I16B20f24f28"
- "i32@0:8I16I20r^v24"
- "i32@0:8^{__CFDictionary=}16^{__CFDictionary=}24"
- "i32@0:8{shared_ptr<ClientEntry>=^{ClientEntry}^{__shared_weak_count}}16"
- "i36@0:8I16^?20^v28"
- "i36@0:8I16^I20^v28"
- "i36@0:8I16i20I24@\"NSDictionary\"28"
- "i36@0:8I16i20I24@28"
- "i40@0:8{shared_ptr<ClientEntry>=^{ClientEntry}^{__shared_weak_count}}16@?32"
- "i48@0:8^{__CFRunLoop=}16^{__CFString=}24^?32^v40"
- "i56@0:8^v16f24^{SSPlayerSynchronizer=}28I36d40@?48"
- "identifier"
- "identifierWithPid:"
- "incrementChannelID"
- "incrementInit:"
- "incrementPrewarmCountForAudio:haptics:entry:"
- "incrementRunningCountForAudio:haptics:entry:"
- "init"
- "initBaseTapInternalWithFormat:"
- "initCount"
- "initDownlinkWithFormat:maxFrames:error:"
- "initForMode:"
- "initInternalWithFormat:"
- "initInternalWithFormat:maxFrames:isUplink:error:"
- "initPreSpatialAudioSessionTapWithFormat:sessionID:"
- "initPreSpatialProcessTapWithFormat:PID:"
- "initPreSpatialProcessTapWithFormat:PIDs:"
- "initPreSpatialSceneIdentifierTapWithFormat:sceneIdentifier:"
- "initPreSpatialSessionTypeTapWithFormat:sessionType:"
- "initPreSpatialTapInternalWithFormat:PIDs:sessionID:sessionType:sceneID:"
- "initProcessTapWithFormat:PID:"
- "initProcessTapWithFormat:PID:deviceUID:"
- "initProcessTapWithFormat:PIDs:"
- "initScreenSharingTapWithFormat:"
- "initStandardFormatWithSampleRate:channels:"
- "initSystemTapWithFormat:"
- "initSystemTapWithFormat:excludePIDs:"
- "initTapInternalWithFormat:PIDs:"
- "initUplinkWithFormat:maxFrames:error:"
- "initWithATAudioSessionClientImpl:"
- "initWithAudio:haptic:error:"
- "initWithAudio:hapticDictionary:error:"
- "initWithAudioResourceID:parameters:relativeTime:duration:"
- "initWithAudioSession:"
- "initWithAudioSession:sessionIsShared:options:error:"
- "initWithAudioSessionID:"
- "initWithCoder:"
- "initWithDescription:"
- "initWithDeviceID:"
- "initWithDeviceUID:"
- "initWithDictionary:copyItems:"
- "initWithDictionary:error:"
- "initWithDouble:"
- "initWithEvents:parameters:error:"
- "initWithFlatIOFormat:type:"
- "initWithFormat:latencyInFrames:"
- "initWithFormat:latencyInFrames:streamDescription:"
- "initWithIdentifier:queue:"
- "initWithImpl:"
- "initWithInteger:"
- "initWithIsolatedAudioUseCaseID:"
- "initWithLayout:"
- "initWithLayoutTag:"
- "initWithMachServiceName:"
- "initWithMaster:id:connection:outError:"
- "initWithNewReporterID"
- "initWithObjectsAndKeys:"
- "initWithPCMFormat:frameCapacity:"
- "initWithPID:"
- "initWithPhasePlatform:"
- "initWithPortType:hysteresisDurationSeconds:notificationBlock:"
- "initWithProperty:callbackWithMessageAndTimestamp:"
- "initWithRateLimit:detectPredictionAnchor:userContext:factory:execution:finalizer:useSleepWakeDetector:"
- "initWithSTSObject:error:"
- "initWithSerialQueue:"
- "initWithServerInstance:"
- "initWithSession:"
- "initWithSiriEndpointIdentifier:"
- "initWithStreamDescription:channelLayout:"
- "initWithStrongSession:"
- "initWithTapDescription:"
- "initWithTime:value:"
- "initWithTranslatorIdentifier:delegate:delegateQueue:"
- "initWithType:relativeTime:shape:controlPoints:"
- "initWithUUIDBytes:"
- "initWithUUIDString:"
- "initWithUseCaseID:"
- "initWithWeakImpl:scope:"
- "initializeAU"
- "initializeChannels"
- "initializeWithReply:"
- "inputPortTypes"
- "inputs"
- "instance"
- "intValue"
- "interfaceWithProtocol:"
- "interruptDummyPlayersForSession:"
- "interruptionType"
- "invalidate"
- "invocationWithMethodSignature:"
- "invoke"
- "ios%d"
- "isAssistantVoiceTriggerEnabled"
- "isAvailable"
- "isBlurEnabled"
- "isCPMSSupportedForClient:"
- "isConfigured"
- "isEnabled"
- "isEqual:"
- "isEqualToDictionary:"
- "isEqualToNumber:"
- "isEqualToString:"
- "isFileURL"
- "isInterleaved"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPortActive:activePortsToken:"
- "isPreSpatial"
- "isProxy"
- "isScreenSharingHost"
- "isSessionMuted:"
- "isUplink"
- "isValid"
- "isXPCService"
- "isolate"
- "json"
- "keyEnumerator"
- "lastObject"
- "lastStateSent"
- "latencyInFrames"
- "layout"
- "lazyInitRoomCongruenceInterface"
- "lazyInitServerManager"
- "lazyInitSessionInterface"
- "lazyInitSessionVolumeInterface"
- "lengthOfBytesUsingEncoding:"
- "listener:shouldAcceptNewConnection:"
- "listeningEnabled"
- "listeningEnabledReply:"
- "loadHapticEvent:reply:"
- "loadHapticSequenceFromData:reply:"
- "loadHapticSequenceFromEvents:reply:"
- "loadSynthPreset"
- "loadVibePattern:reply:"
- "localTimeZone"
- "localizedDescription"
- "logPowerLogEngineOnDuration"
- "longLongValue"
- "lookUpPreferredInputAudioFormatWithCompletionHandler:"
- "lookupAndClearEvent"
- "mAUDSPGraph"
- "mAsClientImpl"
- "mBlurHoldTimeSec"
- "mCapturer->SetCookie(CFDataGetBytePtr(mMagicCookie), ToUInt32(CFDataGetLength(mMagicCookie))) == noErr"
- "mCapturer->WriteBufferList(framesToRender, &abl) == noErr"
- "mImpl"
- "mIsInitialized"
- "mMaxFrames"
- "mRemoteFeedbackFeatureEnabled"
- "mScope"
- "mStreamDescription"
- "mTuningDirectory"
- "manager"
- "manufacturer"
- "mapSession:isInput:toDevice:"
- "markHapticAutoBugCaptureFiled"
- "master"
- "maxLabelLength"
- "maxNumberOfPerLabelStates"
- "maximumFramesPerSlice"
- "methodSignatureForSelector:"
- "mobileAssistantDylib"
- "modes"
- "mutableAudioBufferList"
- "mutableCopy"
- "muteAudioSessionBidirectional:mute:inputFadeTime:outputFadeTime:"
- "muteChannelAudio"
- "muteClientForRingerSwitch:"
- "muteSessionInput:clientPID:muted:"
- "muteSessionInput:mute:fadeTime:"
- "nextObject"
- "not ready to finish"
- "notificationBlock"
- "notificationQueue"
- "notifyClientOnStopWithReason:error:"
- "notifyStateChanged:onQueue:"
- "numberOfStreamsForDirection:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLong:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observeValueForKeyPath:ofObject:change:context:"
- "offsetCustomAudioEventStartTimeToSeekTime"
- "on_entry"
- "on_exit"
- "opaqueSessionID"
- "orientation"
- "outputPortTypes"
- "outputs"
- "overlapping"
- "paramType"
- "parameterCurve"
- "parameterCurves"
- "parameters"
- "path"
- "pathExtension"
- "pause"
- "pauseEvents"
- "pauseSequenceWithID"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performVolumeOperation:volume:category:mode:routeName:routeDeviceIdentifier:routeSubtype:outVolume:outSequenceNumber:outMuted:outCategoryCopy:outModeCopy:"
- "personalized-"
- "phoneCallExists"
- "playSequenceWithID"
- "playVibePattern:gain:synchronizer:flags:atTime:completionHandler:"
- "playWithOptions:completionCallbackToken:error:"
- "portStateChangedNotification:"
- "portType"
- "portsActiveReply:"
- "portsToMonitor"
- "postRender"
- "preRender"
- "predicateMatchingBundleIdentifier:"
- "predicateWithBlock:"
- "predicateWithFormat:"
- "prepareHapticPatternFromPlayOptions:"
- "prepareHapticSequence:reply:"
- "prewarm:"
- "prewarmEntry"
- "prewarmIncludesAudio"
- "prewarmIncludesHaptics"
- "prewarmWithCompletionHandler:"
- "processBlock"
- "processIdentifier"
- "processState:"
- "produceAudio"
- "propertyListWithData:options:format:error:"
- "q"
- "q16@0:8"
- "queryCapabilities:reply:"
- "referenceCustomAudioEvent:reply:"
- "referenceCustomAudioEventsWhileRunning"
- "refreshInputMuteOnAllSessions:"
- "refreshMicrophoneInjectionPermissions:"
- "refreshRecordPermissions:"
- "registerActivateAudioSessionBlock:"
- "registerAudioResource:options:error:"
- "registerClientWithDescription:error:"
- "registerCompletionAndStop"
- "registerCompletionPortion:"
- "registerFadeClientsInAudioSessionBlock:"
- "registerIOBlock:"
- "registerMuteInputClientsInAudioSessionBlock:"
- "registerOverloadNotification:"
- "registerRouteChangeNotification:"
- "registerSSID:withPlayer:"
- "registerSequencePlayerRenderCallback"
- "registerTapInterface:"
- "registerVolumeChangedNotificationBlock:"
- "release"
- "releaseChannels"
- "releaseClientResources"
- "releaseCustomAudioEvent:reply:"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "removeAVAudioSessionKVOObservers:"
- "removeAllObjects"
- "removeChannel:reply:"
- "removeInputClientToken:fromSessionID:"
- "removeListener:withAudioSessionID:"
- "removeObject:"
- "removeObjectForKey:"
- "removeObserver:"
- "removeObserver:forKeyPath:context:"
- "removeObserver:name:object:"
- "removePortToMonitor:"
- "removeProcessEntry:"
- "removeSessionListeners"
- "requestChannels"
- "requestChannels:reply:"
- "requestRecordPermissionWithCompletionHandler:"
- "resetClientConfiguration"
- "resetMuteMapForChannel"
- "resetMuteParameters"
- "resetSequenceWithID"
- "respondsToSelector:"
- "resume"
- "resumeEvents"
- "resumeListener"
- "resumeListeners"
- "resumeSequenceWithID"
- "retain"
- "retainCount"
- "retrieveSessionWithID:"
- "roomCongruenceInterface"
- "rotationDirection"
- "runIncludesAudio"
- "runIncludesHaptics"
- "runningInBackground"
- "s2qnnwugvb7yAD70+Uho7g"
- "sampleRateChanged:forDevice:"
- "samples"
- "seconds"
- "seek"
- "seekSequenceWithID"
- "self"
- "sendActiveStateChangedNotificationForPort:isActive:"
- "sendMessage:category:type:"
- "sendParameters:atTime:error:"
- "sendSingleMessage:category:type:"
- "sendSpeakerMuteStateChangedNotification:"
- "sendState:"
- "sendVoiceTriggerOccuredNotification:triggerTime:"
- "sequenceFinished:error:"
- "serverDidDisconnectForClient:"
- "serverImpl"
- "serverInstance"
- "serverListener"
- "session"
- "sessionInterface"
- "sessionVolumeInterface"
- "set, %d bytes"
- "setAUStrip:propertyStrip:"
- "setActive:error:"
- "setActive:withOptions:error:"
- "setAfSiriActivationBuiltInMicVoiceFuncPtr:"
- "setAggressiveECMode:reply:"
- "setAlwaysSpatialize:"
- "setArgument:atIndex:"
- "setAttributeForKey:andValue:"
- "setAudioBehaviorMuted"
- "setBlendTimeMs:"
- "setCategory:mode:options:error:"
- "setChannelEventBehavior:behavior:reply:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setClientConfiguration:runLoopMode:listenerProc:userData:"
- "setClientConnections:"
- "setClientId:"
- "setClientInterrupted:"
- "setClientInterruptionListenerProc:"
- "setClientMode:"
- "setClientMuteState:sessionID:playerType:playerRef:"
- "setClientStateFromCallbackOnSession:clientToken:modes:state:outDuckingInfo:"
- "setClientStateOnSession:clientToken:modes:state:outDuckingInfo:"
- "setClientSuspended:"
- "setClientUserData:"
- "setClockDevice"
- "setClsVTStateManager:"
- "setCompletionHandler:"
- "setDSPGraph:"
- "setDateFormat:"
- "setDelegate:"
- "setElementCount:"
- "setEnableBlur:"
- "setExcludedPIDs:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFlushRequestTime"
- "setFollowAudioRoute:"
- "setFormat:"
- "setFrameLength:"
- "setGeneration:"
- "setGetCurrentPower:"
- "setHandler:"
- "setHapticsBehaviorMuted"
- "setHysteresisDurationSeconds:"
- "setIOPropertiesForSession:values:"
- "setInputMuteStateFromCallbackOnSession:clientToken:isMuted:"
- "setInputMuteStateOnSession:clientToken:isMuted:"
- "setIntendedSpatialExperience:reply:"
- "setInterruptionHandler:"
- "setInterruptionType:"
- "setInvalidationHandler:"
- "setIsConfigured:"
- "setIsContinuous:"
- "setLastStateSent:"
- "setListeningEnabled:"
- "setListeningProperty:reply:"
- "setLoopEnabled:"
- "setLoopEnd:"
- "setLoopLength"
- "setMaxConcurrentOperationCount:"
- "setMaxFramesPerSlice"
- "setMaximumFramesPerSlice:"
- "setMaximumSpatializableChannels:"
- "setMicrophoneInjectionCapability:"
- "setMobileAssistantDylib:"
- "setMuteBehavior:"
- "setNotificationBlock:"
- "setNotificationCallback:"
- "setNotificationQueue:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPlayState:sessionID:playerType:playerRef:modes:subsessionRef:"
- "setPlayerBehavior:reply:"
- "setPortType:"
- "setPortsToMonitor:"
- "setPowerBudgetUpdateMinimumPeriod:"
- "setPowerLevels:"
- "setPredictionIntervalMicroseconds:"
- "setPrefersHeadTrackedSpatialization:"
- "setPrefersLossyAudioSources:"
- "setPrewarmIncludesAudio:"
- "setPrewarmIncludesHaptics:"
- "setProcessIdentifier:"
- "setProcessIdentifiers:"
- "setProcessIdentifiersChecked:"
- "setProduceAudio:"
- "setQueue:"
- "setRemoteObjectInterface:"
- "setResetHandler:"
- "setRoomCongruenceParameters:"
- "setRunIncludesAudio:"
- "setRunIncludesHaptics:"
- "setRunningInBackground:"
- "setScreenSharingHost:"
- "setSelector:"
- "setSequenceChannelParam"
- "setSequenceEventBehavior:behavior:channelIndex:reply:"
- "setSequenceParam"
- "setServerListener:"
- "setServiceType:"
- "setSomeoneIsRecording"
- "setSpatialAudioSources:"
- "setSpatialStreamInfo"
- "setState:clientType:clientID:clientDescription:"
- "setStreamDescription:"
- "setTarget:"
- "setTelephonyClientSessionID:"
- "setTime:"
- "setTimeZone:"
- "setValue:forKey:"
- "setVersion:"
- "setVoiceTriggerDylib:"
- "setVolumeScalar"
- "setVtStateManager:"
- "setWasPrewarmedAndSuspended:"
- "setWasRunningAndSuspended:"
- "setWithArray:"
- "setupAU"
- "setupAudioSessionFromID:isShared:error:"
- "setupDefaultEngineConfigBlock"
- "setupLooping"
- "setupSSSClient"
- "sharedCPMSAgent"
- "sharedInstance"
- "sharedInstanceWithPlatform:"
- "shouldUnprewarmAllClientsAfterDisplayingPrewarmedProcessEntriesWithPrewarmTime:"
- "signalChangeWithError:"
- "siriClientRecordStateChanged:"
- "siriClientRecordStateChangedNotification:recordingCount:"
- "siriClientsRecordingReply:"
- "sortedArrayUsingComparator:"
- "spatialAudioEnabled:mode:"
- "spatialPreferencesForSession:contentType:"
- "speakerMuteStateChangedNotification:"
- "speakerStateActiveReply:"
- "speakerStateChangedNotification:"
- "speakerStateMutedReply:"
- "speechDetectionVADCreated"
- "srcCmd->head.mSize != 0"
- "ssid"
- "sssPlayer->Play"
- "sss_use_corehaptics"
- "startAlertSequence"
- "startAtTime:error:"
- "startDeviceOrientationUpdatesToQueue:withHandler:"
- "startPlayerAtTime:forAudio:error:"
- "startRunning:"
- "startSequence"
- "startWithCompletionHandler:"
- "startXPCServer"
- "stateChanged:"
- "stateChanged:forPort:"
- "stop:"
- "stopDeviceOrientationUpdates"
- "stopEntry"
- "stopEvent"
- "stopPrewarmEntry"
- "stopRunning:"
- "stopSequence"
- "stopWithCompletionHandler:"
- "streamDescription"
- "streamFormat"
- "streamInfoForIndex:direction:"
- "streamParameters"
- "stringFromDate:"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subtype"
- "successful"
- "superclass"
- "support_secure_platform_t6050"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "synthChannels"
- "systemSleepMonitor:prepareForSleepWithCompletion:"
- "systemSleepMonitor:sleepRequestedWithResult:"
- "systemSleepMonitorDidWakeFromSleep:"
- "systemSleepMonitorSleepRequestAborted:"
- "systemSleepMonitorWillWakeFromSleep:"
- "t6050"
- "tapInterface"
- "taskTokenDictionary"
- "track != 0"
- "translateAudioSamples:"
- "translationDidResumeForClient:"
- "translationDidStartForClient:"
- "triggerSPENOnAlternateTransportChange"
- "type"
- "unarchivedObjectOfClass:fromData:error:"
- "unduckOtherAudio_block_invoke"
- "uninitializeAU"
- "unmuteClientAfterSessionInterruption:"
- "unprewarmAllClientEntries"
- "unregisterAudioResource:error:"
- "unregisterSSID:"
- "unregisterSequencePlayerRenderCallback"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "unsignedLongValue"
- "updateFormat:error:"
- "updateFormats"
- "updateGlobalState:didChange:error:"
- "updateGlobalState:labelStates:additionalLabelInfo:error:"
- "updateGlobalState:labelStates:error:"
- "updateLabel:state:didChange:additionalInfo:error:"
- "updateLabel:state:didChange:error:"
- "updateMicrophoneInjectionPreference:forSession:"
- "updateVoiceTriggerConfiguration:reply:"
- "userInfo"
- "v16@0:8"
- "v16@?0@?<v@?>8"
- "v2-"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8f16"
- "v20@0:8i16"
- "v24@0:8#16"
- "v24@0:8@\"<PHASETapInterface>\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@\"STSpeechTranslatorClient\"16"
- "v24@0:8@\"SWSystemSleepMonitor\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSObject<OS_xpc_object>\"I@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8@?<v@?I@\"NSError\">16"
- "v24@0:8@?<v@?Q@\"NSError\">16"
- "v24@0:8@?<v@?d@\"NSError\">16"
- "v24@0:8I16B20"
- "v24@0:8Q16"
- "v24@0:8^?16"
- "v24@0:8^v16"
- "v24@0:8^{__CFString=}16"
- "v24@0:8^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}16"
- "v24@0:8q16"
- "v28@0:8@16I24"
- "v28@0:8B16@20"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSError\">20"
- "v28@0:8B16Q20"
- "v28@0:8I16@20"
- "v28@0:8Q16B24"
- "v28@0:8^v16I24"
- "v32@0:8@\"CASpatialAudioExperience\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?QdQ@\"NSError\">24"
- "v32@0:8@\"NSData\"16@?<v@?QdQ@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?Q>24"
- "v32@0:8@\"NSDictionary\"16@?<v@?Q@\"NSError\">24"
- "v32@0:8@\"STSpeechTranslatorClient\"16@\"AVAudioPCMBuffer\"24"
- "v32@0:8@\"STSpeechTranslatorClient\"16@\"NSError\"24"
- "v32@0:8@\"STSpeechTranslatorClient\"16@\"NSString\"24"
- "v32@0:8@\"STSpeechTranslatorClient\"16@\"STGeneratedAudioMetadata\"24"
- "v32@0:8@\"STSpeechTranslatorClient\"16@\"STTranscriptionResult\"24"
- "v32@0:8@\"STSpeechTranslatorClient\"16@\"STTranslationResult\"24"
- "v32@0:8@\"SWSystemSleepMonitor\"16@?<@\"SWPreventSystemSleepAssertion\"@?B@\"NSString\">24"
- "v32@0:8@\"SWSystemSleepMonitor\"16@?<v@?>24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8@16^@24"
- "v32@0:8Q16@\"NSError\"24"
- "v32@0:8Q16@24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8Q16@?<v@?@\"NSError\">24"
- "v32@0:8d16@?24"
- "v32@0:8d16@?<v@?>24"
- "v32@0:8q16@24"
- "v32@0:8{shared_ptr<ClientEntry>=^{ClientEntry}^{__shared_weak_count}}16"
- "v36@0:8B16B20f24f28B32"
- "v36@0:8r^v16I24@28"
- "v36@0:8r^v16I24^{__CFDictionary=}28"
- "v40@0:8@16@24:32"
- "v40@0:8@16@24@?32"
- "v40@0:8B16B20{shared_ptr<ClientEntry>=^{ClientEntry}^{__shared_weak_count}}24"
- "v40@0:8Q16@\"NSDictionary\"24@?<v@?Q@\"NSError\">32"
- "v40@0:8Q16@24@?32"
- "v40@0:8Q16Q24@?32"
- "v40@0:8Q16Q24@?<v@?@\"NSError\">32"
- "v40@0:8{shared_ptr<ClientEntry>=^{ClientEntry}^{__shared_weak_count}}16B32B36"
- "v48@0:8@16@24@32^v40"
- "v48@0:8Q16Q24Q32@?40"
- "v48@0:8Q16Q24Q32@?<v@?@\"NSError\">40"
- "v56@0:8@\"NSData\"16@\"AVAudioFormat\"24Q32@\"NSDictionary\"40@?<v@?Q@\"NSError\">48"
- "v56@0:8@16@24Q32@40@?48"
- "v56@0:8{AudioStreamBasicDescription=dIIIIIIII}16"
- "valueForKey:"
- "valueForKeyPath:"
- "version"
- "voiceTriggerDylib"
- "voiceTriggerNotification:"
- "voiceTriggerPastDataFramesAvailable:"
- "volumeForCommand:"
- "volumeForCommandFromCallback:"
- "volumeScalar"
- "volumeScalarMappedToHWCurve"
- "volumeScalarMappedToHWCurve:"
- "vtStateManager"
- "waitForConclaveLaunch"
- "wasPrewarmedAndSuspended"
- "wasRunningAndSuspended"
- "zone"
- "{AQMESession=\"mProcessID\"i\"mSessionID\"I\"mSourceSessionID\"{optional<unsigned int>=\"\"(?=\"__null_state_\"c\"__val_\"I)\"__engaged_\"B}\"mSubsessionRef\"{ObjectRef<const void *>=\"mCFObject\"^v}\"mSubsessionID\"Q\"mDescription\"{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"\"{?=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}\"mOneWordID\"i\"mBundleID\"{optional<applesauce::CF::StringRef>=\"\"(?=\"__null_state_\"c\"__val_\"{StringRef=\"mObject\"{ObjectRef<const __CFString *>=\"mCFObject\"^{__CFString}}})\"__engaged_\"B}}"
- "{ATIsolatedAudioUseCaseID=I}16@0:8"
- "{AudioStreamBasicDescription=dIIIIIIII}16@0:8"
- "{ObjectRef<__CFRunLoop *>=\"mCFObject\"^{__CFRunLoop}}"
- "{STSActiveIndices=\"m_activeLabels\"Q}"
- "{STSGlobalState=\"hostTime\"Q\"listenerTransform\"{?=\"columns\"[4]}}"
- "{StreamDescription=\"mSampleRate\"d\"mFormatID\"I\"mFormatFlags\"I\"mBytesPerPacket\"I\"mFramesPerPacket\"I\"mBytesPerFrame\"I\"mChannelsPerFrame\"I\"mBitsPerChannel\"I\"mReserved\"I}"
- "{StringRef=\"mObject\"{ObjectRef<const __CFString *>=\"mCFObject\"^{__CFString}}}"
- "{StringRef={ObjectRef<const __CFString *>=^{__CFString}}}16@0:8"
- "{__hash_map_iterator<std::__hash_iterator<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *>>={__hash_iterator<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *>=^v}}32@0:8^{__CFString=}16^@24"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"\"{?=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}"
- "{condition_variable=\"__cv_\"{_opaque_pthread_cond_t=\"__sig\"q\"__opaque\"[40c]}}"
- "{map<int, std::bitset<255>, std::less<int>, std::allocator<std::pair<const int, std::bitset<255>>>>=\"__tree_\"{__tree<std::__value_type<int, std::bitset<255>>, std::__map_value_compare<int, std::pair<const int, std::bitset<255>>, std::less<int>>, std::allocator<std::pair<const int, std::bitset<255>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
- "{map<std::string, std::shared_ptr<NewNotificationCenterObserver>, std::less<std::string>, std::allocator<std::pair<const std::string, std::shared_ptr<NewNotificationCenterObserver>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::shared_ptr<NewNotificationCenterObserver>>, std::__map_value_compare<std::string, std::pair<const std::string, std::shared_ptr<NewNotificationCenterObserver>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::shared_ptr<NewNotificationCenterObserver>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
- "{map<std::string, std::shared_ptr<OldNotificationCenterObserver>, std::less<std::string>, std::allocator<std::pair<const std::string, std::shared_ptr<OldNotificationCenterObserver>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::shared_ptr<OldNotificationCenterObserver>>, std::__map_value_compare<std::string, std::pair<const std::string, std::shared_ptr<OldNotificationCenterObserver>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::shared_ptr<OldNotificationCenterObserver>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
- "{map<unsigned int, NSMutableArray<AVServerWrapper *> *, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, NSMutableArray<AVServerWrapper *> *>>>=\"__tree_\"{__tree<std::__value_type<unsigned int, NSMutableArray<AVServerWrapper *> *>, std::__map_value_compare<unsigned int, std::pair<const unsigned int, NSMutableArray<AVServerWrapper *> *>, std::less<unsigned int>>, std::allocator<std::pair<const unsigned int, NSMutableArray<AVServerWrapper *> *>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
- "{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}"
- "{queue=\"fObj\"{object=\"fObj\"@\"NSObject<OS_dispatch_object>\"}}"
- "{recursive_mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}"
- "{semaphore=\"mMachSem\"I\"mOwned\"B}"
- "{shared_ptr<ClientEntry>=^{ClientEntry}^{__shared_weak_count}}24@0:8Q16"
- "{shared_ptr<HapticSession>=\"__ptr_\"^{HapticSession}\"__cntrl_\"^{__shared_weak_count}}"
- "{shared_ptr<ThreadSafeHeadTracker>=\"__ptr_\"^{ThreadSafeHeadTracker}\"__cntrl_\"^{__shared_weak_count}}"
- "{shared_ptr<const AT::IOBinding::Impl>=\"__ptr_\"^{Impl}\"__cntrl_\"^{__shared_weak_count}}"
- "{shared_ptr<opaqueCMSession>=\"__ptr_\"^{opaqueCMSession}\"__cntrl_\"^{__shared_weak_count}}"
- "{stack<unsigned long, std::deque<unsigned long>>=\"c\"{deque<unsigned long, std::allocator<unsigned long>>=\"__map_\"{__split_buffer<unsigned long *, std::allocator<unsigned long *>>=\"__first_\"^^Q\"__begin_\"^^Q\"__end_\"^^Q\"\"{?=\"__cap_\"^^Q}}\"__start_\"Q\"\"{?=\"__size_\"Q}}}"
- "{unique_ptr<AudioSessionPropertyListeners, std::default_delete<AudioSessionPropertyListeners>>=\"\"{?=\"__ptr_\"^{AudioSessionPropertyListeners}}}"
- "{unique_ptr<OpaqueAudioComponentInstance, applesauce::raii::detail::opaque_deletion_functor<OpaqueAudioComponentInstance *, &AudioComponentInstanceDispose>>=\"\"{?=\"__ptr_\"^{OpaqueAudioComponentInstance}}}"
- "{unique_ptr<Phase::ServerManager, std::default_delete<Phase::ServerManager>>=\"\"{?=\"__ptr_\"^{ServerManager}}}"
- "{unordered_map<std::string, STSPerLabelControllerState, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, STSPerLabelControllerState>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, STSPerLabelControllerState>, std::__unordered_map_hasher<std::string, std::pair<const std::string, STSPerLabelControllerState>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, STSPerLabelControllerState>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, STSPerLabelControllerState>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{unordered_map<unsigned int, std::unordered_set<void *>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, std::unordered_set<void *>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, std::__unordered_map_hasher<unsigned int, std::pair<const unsigned int, std::unordered_set<void *>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::pair<const unsigned int, std::unordered_set<void *>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::pair<const unsigned int, std::unordered_set<void *>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{weak_ptr<AT::Translation::TranslatorClient>=\"__ptr_\"^{TranslatorClient}\"__cntrl_\"^{__shared_weak_count}}"
- "~ClientEntry"
- "~MIDIPacketEmitter"
- "~RemoteClient_block_invoke"

```
