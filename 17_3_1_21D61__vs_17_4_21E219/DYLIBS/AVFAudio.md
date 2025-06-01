## AVFAudio

> `/System/Library/Frameworks/AVFAudio.framework/AVFAudio`

```diff

-629.3.5.0.0
-  __TEXT.__text: 0xf672c
-  __TEXT.__auth_stubs: 0x1da0
-  __TEXT.__objc_methlist: 0x4cb8
-  __TEXT.__const: 0x55e
-  __TEXT.__gcc_except_tab: 0xce70
-  __TEXT.__cstring: 0xd845
-  __TEXT.__oslogstring: 0x1467f
-  __TEXT.__dlopen_cstrs: 0x4f
-  __TEXT.__unwind_info: 0x5308
+629.5.30.0.0
+  __TEXT.__text: 0x104fe4
+  __TEXT.__auth_stubs: 0x1e70
+  __TEXT.__objc_methlist: 0x5050
+  __TEXT.__const: 0x596
+  __TEXT.__gcc_except_tab: 0xeb44
+  __TEXT.__cstring: 0xdca9
+  __TEXT.__oslogstring: 0x15946
+  __TEXT.__dlopen_cstrs: 0xa9
+  __TEXT.__unwind_info: 0x5670
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x9bf
-  __TEXT.__objc_methname: 0xabea
-  __TEXT.__objc_methtype: 0x248d
-  __TEXT.__objc_stubs: 0x6620
-  __DATA_CONST.__got: 0x240
-  __DATA_CONST.__const: 0x1758
-  __DATA_CONST.__objc_classlist: 0x2f8
+  __TEXT.__objc_classname: 0xa12
+  __TEXT.__objc_methname: 0xb846
+  __TEXT.__objc_methtype: 0x2655
+  __TEXT.__objc_stubs: 0x7540
+  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__const: 0x1a08
+  __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x0
-  __DATA_CONST.__objc_protolist: 0x80
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6750
-  __DATA_CONST.__objc_selrefs: 0x2dd8
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__const: 0x8d8
-  __AUTH_CONST.__cfstring: 0x2f40
-  __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0xee8
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x318
-  __DATA.__objc_superrefs: 0x2a8
-  __DATA.__objc_ivar: 0x3b4
-  __DATA.__data: 0x820
-  __DATA.__bss: 0xb8
-  __DATA_DIRTY.__const: 0x5b18
+  __DATA_CONST.__objc_const: 0x6c88
+  __DATA_CONST.__objc_selrefs: 0x3088
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x340
+  __DATA_CONST.__objc_superrefs: 0x2b0
+  __AUTH_CONST.__objc_const: 0x90
+  __AUTH_CONST.__const: 0x9a8
+  __AUTH_CONST.__cfstring: 0x3240
+  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0xf50
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x408
+  __DATA.__data: 0x880
+  __DATA.__bss: 0xf0
+  __DATA_DIRTY.__const: 0x5aa8
   __DATA_DIRTY.__objc_const: 0x2130
   __DATA_DIRTY.__objc_data: 0x1db0
   __DATA_DIRTY.__data: 0x90

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AudioSession.framework/AudioSession
   - /System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore
+  - /System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/caulk.framework/caulk

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1FD858A7-AA84-3F1B-8D04-3B9679C9CB52
-  Functions: 3632
-  Symbols:   11614
-  CStrings:  5716
+  UUID: 3C5388B0-5DF6-316B-AAEB-C57E524A0B15
+  Functions: 3760
+  Symbols:   12141
+  CStrings:  6020
 
Symbols:
+ -[AVAudioDeviceTest initInProcess:]
+ -[AVAudioDeviceTest service]
+ -[AVAudioDeviceTest setService:]
+ -[AVAudioDeviceTestService .cxx_construct]
+ -[AVAudioDeviceTestService .cxx_destruct]
+ -[AVAudioDeviceTestService calculateCrossCorrelationPeakRelativeToSource:capture:]
+ -[AVAudioDeviceTestService cancel]
+ -[AVAudioDeviceTestService checkSequenceValidity:completion:]
+ -[AVAudioDeviceTestService cleanUpObservers]
+ -[AVAudioDeviceTestService cleanUp]
+ -[AVAudioDeviceTestService configureDataSources:session:]
+ -[AVAudioDeviceTestService configureMultiChannelMixerForOutputChannel:totalChannels:]
+ -[AVAudioDeviceTestService convertBufferFor:sourceBuffer:]
+ -[AVAudioDeviceTestService createAudioEngineAndProcessingChain:session:sourceNodeBlock:]
+ -[AVAudioDeviceTestService createAudioEngineAndPulseToneHandlerFor:]
+ -[AVAudioDeviceTestService currentSession]
+ -[AVAudioDeviceTestService dealloc]
+ -[AVAudioDeviceTestService engine]
+ -[AVAudioDeviceTestService extensionHandle]
+ -[AVAudioDeviceTestService init]
+ -[AVAudioDeviceTestService inputFilter]
+ -[AVAudioDeviceTestService inputTapFile]
+ -[AVAudioDeviceTestService interruptionObserver]
+ -[AVAudioDeviceTestService isMixerOutputEnabled]
+ -[AVAudioDeviceTestService isOutputRouteBluetooth:session:]
+ -[AVAudioDeviceTestService mediaservicesLostObserver]
+ -[AVAudioDeviceTestService mediaservicesResetObserver]
+ -[AVAudioDeviceTestService multichannelMixer]
+ -[AVAudioDeviceTestService nodeToCaptureData]
+ -[AVAudioDeviceTestService outputFilter]
+ -[AVAudioDeviceTestService passExtensionToken:]
+ -[AVAudioDeviceTestService playback:filePath:completion:]
+ -[AVAudioDeviceTestService playbackTone:completion:]
+ -[AVAudioDeviceTestService player]
+ -[AVAudioDeviceTestService resetVolume:]
+ -[AVAudioDeviceTestService routeChangeObserver]
+ -[AVAudioDeviceTestService setCurrentSession:]
+ -[AVAudioDeviceTestService setEngine:]
+ -[AVAudioDeviceTestService setExtensionHandle:]
+ -[AVAudioDeviceTestService setInputFilter:]
+ -[AVAudioDeviceTestService setInputTapFile:]
+ -[AVAudioDeviceTestService setInterruptionObserver:]
+ -[AVAudioDeviceTestService setMediaservicesLostObserver:]
+ -[AVAudioDeviceTestService setMediaservicesResetObserver:]
+ -[AVAudioDeviceTestService setMultichannelMixer:]
+ -[AVAudioDeviceTestService setNodeToCaptureData:]
+ -[AVAudioDeviceTestService setOutputFilter:]
+ -[AVAudioDeviceTestService setPlayer:]
+ -[AVAudioDeviceTestService setRouteChangeObserver:]
+ -[AVAudioDeviceTestService setSourceNode:]
+ -[AVAudioDeviceTestService setSystemVolumeObserver:]
+ -[AVAudioDeviceTestService setTestServiceSupportedOnHardware:]
+ -[AVAudioDeviceTestService setToneQueue:]
+ -[AVAudioDeviceTestService setTransaction:]
+ -[AVAudioDeviceTestService setUserVolumeBeforeHearingTest:]
+ -[AVAudioDeviceTestService setVolume:]
+ -[AVAudioDeviceTestService setVolume:session:]
+ -[AVAudioDeviceTestService setupAudioEngineFor:sourceNodeBlock:]
+ -[AVAudioDeviceTestService setupAudioSessionFor:playbackOnly:completion:]
+ -[AVAudioDeviceTestService setupMultiChannelMixerForOutputChannel:completion:]
+ -[AVAudioDeviceTestService setupObservers:]
+ -[AVAudioDeviceTestService setupVolumeObserverForVolume:completion:]
+ -[AVAudioDeviceTestService sourceNode]
+ -[AVAudioDeviceTestService startRecording:filePath:completion:]
+ -[AVAudioDeviceTestService startWithSequence:completion:]
+ -[AVAudioDeviceTestService stopPlayback]
+ -[AVAudioDeviceTestService stopRecording:]
+ -[AVAudioDeviceTestService stringForInterruptionReason:]
+ -[AVAudioDeviceTestService stringForRouteChangeReason:]
+ -[AVAudioDeviceTestService systemVolumeObserver]
+ -[AVAudioDeviceTestService testServiceSupportedOnHardware]
+ -[AVAudioDeviceTestService toneQueue]
+ -[AVAudioDeviceTestService transaction]
+ -[AVAudioDeviceTestService userVolumeBeforeHearingTest]
+ -[AVAudioDeviceTestServiceDelegate listener:shouldAcceptNewConnection:]
+ -[AVVCSessionManager getSiriInputSource:withIdentifier:withIsMicrophoneCheck:forActivationMode:]
+ GCC_except_table1003
+ GCC_except_table1011
+ GCC_except_table1016
+ GCC_except_table1034
+ GCC_except_table1042
+ GCC_except_table105
+ GCC_except_table1050
+ GCC_except_table1058
+ GCC_except_table107
+ GCC_except_table1079
+ GCC_except_table109
+ GCC_except_table1102
+ GCC_except_table1107
+ GCC_except_table1108
+ GCC_except_table1109
+ GCC_except_table111
+ GCC_except_table1123
+ GCC_except_table113
+ GCC_except_table115
+ GCC_except_table1152
+ GCC_except_table1163
+ GCC_except_table1171
+ GCC_except_table1172
+ GCC_except_table1173
+ GCC_except_table1185
+ GCC_except_table1193
+ GCC_except_table1195
+ GCC_except_table1196
+ GCC_except_table1199
+ GCC_except_table1203
+ GCC_except_table1206
+ GCC_except_table121
+ GCC_except_table123
+ GCC_except_table1234
+ GCC_except_table1240
+ GCC_except_table1243
+ GCC_except_table1244
+ GCC_except_table1252
+ GCC_except_table1253
+ GCC_except_table1254
+ GCC_except_table126
+ GCC_except_table1285
+ GCC_except_table1286
+ GCC_except_table1300
+ GCC_except_table132
+ GCC_except_table1336
+ GCC_except_table1337
+ GCC_except_table1338
+ GCC_except_table1348
+ GCC_except_table1349
+ GCC_except_table1350
+ GCC_except_table137
+ GCC_except_table1377
+ GCC_except_table1379
+ GCC_except_table1380
+ GCC_except_table1383
+ GCC_except_table1384
+ GCC_except_table1386
+ GCC_except_table1389
+ GCC_except_table1390
+ GCC_except_table1401
+ GCC_except_table1417
+ GCC_except_table1418
+ GCC_except_table142
+ GCC_except_table1421
+ GCC_except_table1433
+ GCC_except_table1434
+ GCC_except_table1435
+ GCC_except_table1445
+ GCC_except_table1446
+ GCC_except_table1448
+ GCC_except_table1449
+ GCC_except_table146
+ GCC_except_table1463
+ GCC_except_table1464
+ GCC_except_table1468
+ GCC_except_table1469
+ GCC_except_table1470
+ GCC_except_table1473
+ GCC_except_table1475
+ GCC_except_table1489
+ GCC_except_table1490
+ GCC_except_table1495
+ GCC_except_table1506
+ GCC_except_table1508
+ GCC_except_table1511
+ GCC_except_table1515
+ GCC_except_table1518
+ GCC_except_table1520
+ GCC_except_table1525
+ GCC_except_table1529
+ GCC_except_table1530
+ GCC_except_table1541
+ GCC_except_table1542
+ GCC_except_table1543
+ GCC_except_table1544
+ GCC_except_table1546
+ GCC_except_table1547
+ GCC_except_table1567
+ GCC_except_table1571
+ GCC_except_table1572
+ GCC_except_table1573
+ GCC_except_table1576
+ GCC_except_table1577
+ GCC_except_table1587
+ GCC_except_table1589
+ GCC_except_table1593
+ GCC_except_table1623
+ GCC_except_table1631
+ GCC_except_table1635
+ GCC_except_table1636
+ GCC_except_table1637
+ GCC_except_table1638
+ GCC_except_table164
+ GCC_except_table1643
+ GCC_except_table1648
+ GCC_except_table1651
+ GCC_except_table166
+ GCC_except_table1679
+ GCC_except_table168
+ GCC_except_table1682
+ GCC_except_table1686
+ GCC_except_table1687
+ GCC_except_table1689
+ GCC_except_table1690
+ GCC_except_table1694
+ GCC_except_table172
+ GCC_except_table1736
+ GCC_except_table1737
+ GCC_except_table1738
+ GCC_except_table1742
+ GCC_except_table1743
+ GCC_except_table1744
+ GCC_except_table1745
+ GCC_except_table1746
+ GCC_except_table175
+ GCC_except_table1760
+ GCC_except_table1762
+ GCC_except_table1769
+ GCC_except_table1770
+ GCC_except_table1771
+ GCC_except_table1772
+ GCC_except_table1773
+ GCC_except_table1774
+ GCC_except_table1775
+ GCC_except_table1777
+ GCC_except_table1778
+ GCC_except_table1779
+ GCC_except_table1780
+ GCC_except_table1783
+ GCC_except_table1784
+ GCC_except_table1785
+ GCC_except_table1786
+ GCC_except_table1790
+ GCC_except_table1791
+ GCC_except_table1793
+ GCC_except_table1796
+ GCC_except_table1797
+ GCC_except_table1798
+ GCC_except_table1799
+ GCC_except_table1800
+ GCC_except_table1801
+ GCC_except_table1803
+ GCC_except_table1804
+ GCC_except_table1818
+ GCC_except_table182
+ GCC_except_table1826
+ GCC_except_table1833
+ GCC_except_table1836
+ GCC_except_table1837
+ GCC_except_table1868
+ GCC_except_table1870
+ GCC_except_table1871
+ GCC_except_table1872
+ GCC_except_table1873
+ GCC_except_table1874
+ GCC_except_table1875
+ GCC_except_table1876
+ GCC_except_table1877
+ GCC_except_table1878
+ GCC_except_table1879
+ GCC_except_table188
+ GCC_except_table1883
+ GCC_except_table1884
+ GCC_except_table1886
+ GCC_except_table1887
+ GCC_except_table1901
+ GCC_except_table191
+ GCC_except_table2025
+ GCC_except_table2027
+ GCC_except_table2028
+ GCC_except_table2029
+ GCC_except_table2032
+ GCC_except_table2037
+ GCC_except_table204
+ GCC_except_table2045
+ GCC_except_table2048
+ GCC_except_table2049
+ GCC_except_table206
+ GCC_except_table2067
+ GCC_except_table2069
+ GCC_except_table2070
+ GCC_except_table2076
+ GCC_except_table2078
+ GCC_except_table2079
+ GCC_except_table208
+ GCC_except_table2080
+ GCC_except_table2082
+ GCC_except_table2084
+ GCC_except_table2086
+ GCC_except_table2094
+ GCC_except_table2101
+ GCC_except_table212
+ GCC_except_table2122
+ GCC_except_table213
+ GCC_except_table2163
+ GCC_except_table2164
+ GCC_except_table2165
+ GCC_except_table2178
+ GCC_except_table218
+ GCC_except_table2193
+ GCC_except_table2194
+ GCC_except_table2235
+ GCC_except_table2237
+ GCC_except_table2243
+ GCC_except_table2245
+ GCC_except_table2248
+ GCC_except_table2251
+ GCC_except_table2256
+ GCC_except_table2262
+ GCC_except_table2271
+ GCC_except_table2272
+ GCC_except_table2273
+ GCC_except_table2274
+ GCC_except_table2291
+ GCC_except_table2292
+ GCC_except_table2293
+ GCC_except_table2298
+ GCC_except_table2299
+ GCC_except_table2302
+ GCC_except_table2304
+ GCC_except_table2305
+ GCC_except_table2311
+ GCC_except_table2312
+ GCC_except_table2317
+ GCC_except_table2321
+ GCC_except_table2322
+ GCC_except_table2323
+ GCC_except_table2324
+ GCC_except_table2327
+ GCC_except_table2335
+ GCC_except_table2336
+ GCC_except_table2337
+ GCC_except_table2338
+ GCC_except_table2342
+ GCC_except_table2347
+ GCC_except_table2350
+ GCC_except_table2352
+ GCC_except_table2353
+ GCC_except_table2354
+ GCC_except_table2355
+ GCC_except_table2368
+ GCC_except_table2371
+ GCC_except_table2372
+ GCC_except_table2374
+ GCC_except_table2375
+ GCC_except_table2377
+ GCC_except_table2401
+ GCC_except_table2406
+ GCC_except_table2408
+ GCC_except_table2409
+ GCC_except_table2416
+ GCC_except_table2428
+ GCC_except_table2429
+ GCC_except_table2435
+ GCC_except_table2452
+ GCC_except_table247
+ GCC_except_table2473
+ GCC_except_table2482
+ GCC_except_table2484
+ GCC_except_table2502
+ GCC_except_table2505
+ GCC_except_table2507
+ GCC_except_table2508
+ GCC_except_table2513
+ GCC_except_table2514
+ GCC_except_table2519
+ GCC_except_table2520
+ GCC_except_table2541
+ GCC_except_table2552
+ GCC_except_table2553
+ GCC_except_table2561
+ GCC_except_table2562
+ GCC_except_table2563
+ GCC_except_table2565
+ GCC_except_table2569
+ GCC_except_table2571
+ GCC_except_table2575
+ GCC_except_table2577
+ GCC_except_table2583
+ GCC_except_table2589
+ GCC_except_table2593
+ GCC_except_table2605
+ GCC_except_table2609
+ GCC_except_table2615
+ GCC_except_table2617
+ GCC_except_table2623
+ GCC_except_table2628
+ GCC_except_table2634
+ GCC_except_table264
+ GCC_except_table2640
+ GCC_except_table2646
+ GCC_except_table2647
+ GCC_except_table2652
+ GCC_except_table2653
+ GCC_except_table2654
+ GCC_except_table2655
+ GCC_except_table2656
+ GCC_except_table2657
+ GCC_except_table266
+ GCC_except_table2660
+ GCC_except_table2666
+ GCC_except_table2667
+ GCC_except_table2668
+ GCC_except_table2669
+ GCC_except_table2670
+ GCC_except_table2671
+ GCC_except_table2672
+ GCC_except_table2673
+ GCC_except_table2676
+ GCC_except_table2677
+ GCC_except_table268
+ GCC_except_table2713
+ GCC_except_table2714
+ GCC_except_table2718
+ GCC_except_table2719
+ GCC_except_table2720
+ GCC_except_table2721
+ GCC_except_table2722
+ GCC_except_table2723
+ GCC_except_table2724
+ GCC_except_table2729
+ GCC_except_table2732
+ GCC_except_table2733
+ GCC_except_table2743
+ GCC_except_table2747
+ GCC_except_table2749
+ GCC_except_table275
+ GCC_except_table2751
+ GCC_except_table2754
+ GCC_except_table2755
+ GCC_except_table2757
+ GCC_except_table2759
+ GCC_except_table2760
+ GCC_except_table2761
+ GCC_except_table2763
+ GCC_except_table2764
+ GCC_except_table2765
+ GCC_except_table2766
+ GCC_except_table2767
+ GCC_except_table2770
+ GCC_except_table2771
+ GCC_except_table2772
+ GCC_except_table2773
+ GCC_except_table2780
+ GCC_except_table2781
+ GCC_except_table2783
+ GCC_except_table2784
+ GCC_except_table2786
+ GCC_except_table2787
+ GCC_except_table279
+ GCC_except_table280
+ GCC_except_table2800
+ GCC_except_table2801
+ GCC_except_table2802
+ GCC_except_table2803
+ GCC_except_table2804
+ GCC_except_table2806
+ GCC_except_table2808
+ GCC_except_table2809
+ GCC_except_table2811
+ GCC_except_table2813
+ GCC_except_table2814
+ GCC_except_table2816
+ GCC_except_table2818
+ GCC_except_table2819
+ GCC_except_table2821
+ GCC_except_table2822
+ GCC_except_table2823
+ GCC_except_table2824
+ GCC_except_table2825
+ GCC_except_table2826
+ GCC_except_table2827
+ GCC_except_table2828
+ GCC_except_table2829
+ GCC_except_table2830
+ GCC_except_table2833
+ GCC_except_table2834
+ GCC_except_table2838
+ GCC_except_table284
+ GCC_except_table2847
+ GCC_except_table2848
+ GCC_except_table285
+ GCC_except_table2853
+ GCC_except_table2856
+ GCC_except_table2857
+ GCC_except_table2858
+ GCC_except_table2860
+ GCC_except_table2861
+ GCC_except_table2862
+ GCC_except_table2863
+ GCC_except_table2864
+ GCC_except_table2866
+ GCC_except_table2870
+ GCC_except_table2874
+ GCC_except_table2875
+ GCC_except_table290
+ GCC_except_table2929
+ GCC_except_table2932
+ GCC_except_table2937
+ GCC_except_table2939
+ GCC_except_table295
+ GCC_except_table2967
+ GCC_except_table2968
+ GCC_except_table2974
+ GCC_except_table2989
+ GCC_except_table2990
+ GCC_except_table2991
+ GCC_except_table2995
+ GCC_except_table300
+ GCC_except_table3002
+ GCC_except_table3004
+ GCC_except_table3006
+ GCC_except_table3007
+ GCC_except_table3008
+ GCC_except_table3009
+ GCC_except_table3010
+ GCC_except_table3011
+ GCC_except_table3012
+ GCC_except_table3013
+ GCC_except_table3014
+ GCC_except_table3015
+ GCC_except_table3016
+ GCC_except_table3017
+ GCC_except_table3018
+ GCC_except_table3019
+ GCC_except_table3020
+ GCC_except_table3021
+ GCC_except_table3022
+ GCC_except_table3023
+ GCC_except_table3029
+ GCC_except_table3031
+ GCC_except_table3032
+ GCC_except_table3033
+ GCC_except_table3034
+ GCC_except_table3035
+ GCC_except_table3036
+ GCC_except_table3038
+ GCC_except_table3039
+ GCC_except_table3040
+ GCC_except_table3041
+ GCC_except_table3042
+ GCC_except_table3045
+ GCC_except_table3046
+ GCC_except_table3049
+ GCC_except_table305
+ GCC_except_table3050
+ GCC_except_table3056
+ GCC_except_table3058
+ GCC_except_table3060
+ GCC_except_table3062
+ GCC_except_table3064
+ GCC_except_table3066
+ GCC_except_table3068
+ GCC_except_table307
+ GCC_except_table3070
+ GCC_except_table3072
+ GCC_except_table3074
+ GCC_except_table3075
+ GCC_except_table3076
+ GCC_except_table3082
+ GCC_except_table3085
+ GCC_except_table3118
+ GCC_except_table3119
+ GCC_except_table312
+ GCC_except_table3121
+ GCC_except_table314
+ GCC_except_table3146
+ GCC_except_table3152
+ GCC_except_table3199
+ GCC_except_table3201
+ GCC_except_table3210
+ GCC_except_table3211
+ GCC_except_table3216
+ GCC_except_table3218
+ GCC_except_table3225
+ GCC_except_table3261
+ GCC_except_table3263
+ GCC_except_table3265
+ GCC_except_table3266
+ GCC_except_table3269
+ GCC_except_table327
+ GCC_except_table3270
+ GCC_except_table3272
+ GCC_except_table3283
+ GCC_except_table3284
+ GCC_except_table3285
+ GCC_except_table3286
+ GCC_except_table3287
+ GCC_except_table3291
+ GCC_except_table3294
+ GCC_except_table3295
+ GCC_except_table3297
+ GCC_except_table3298
+ GCC_except_table3299
+ GCC_except_table3300
+ GCC_except_table3303
+ GCC_except_table3334
+ GCC_except_table3335
+ GCC_except_table3336
+ GCC_except_table3337
+ GCC_except_table3339
+ GCC_except_table3341
+ GCC_except_table336
+ GCC_except_table3361
+ GCC_except_table337
+ GCC_except_table3375
+ GCC_except_table3415
+ GCC_except_table3418
+ GCC_except_table3426
+ GCC_except_table3432
+ GCC_except_table3433
+ GCC_except_table3434
+ GCC_except_table3435
+ GCC_except_table3436
+ GCC_except_table3474
+ GCC_except_table3475
+ GCC_except_table3476
+ GCC_except_table3477
+ GCC_except_table3478
+ GCC_except_table3479
+ GCC_except_table3480
+ GCC_except_table3482
+ GCC_except_table3484
+ GCC_except_table3487
+ GCC_except_table3488
+ GCC_except_table349
+ GCC_except_table3491
+ GCC_except_table3492
+ GCC_except_table3493
+ GCC_except_table3495
+ GCC_except_table3496
+ GCC_except_table3507
+ GCC_except_table3523
+ GCC_except_table3526
+ GCC_except_table3528
+ GCC_except_table3529
+ GCC_except_table3530
+ GCC_except_table3532
+ GCC_except_table3535
+ GCC_except_table3536
+ GCC_except_table3538
+ GCC_except_table3539
+ GCC_except_table3541
+ GCC_except_table3543
+ GCC_except_table3544
+ GCC_except_table3546
+ GCC_except_table3547
+ GCC_except_table3563
+ GCC_except_table3565
+ GCC_except_table3566
+ GCC_except_table3567
+ GCC_except_table3568
+ GCC_except_table3569
+ GCC_except_table3570
+ GCC_except_table3571
+ GCC_except_table3573
+ GCC_except_table3575
+ GCC_except_table3576
+ GCC_except_table3577
+ GCC_except_table3579
+ GCC_except_table3580
+ GCC_except_table3581
+ GCC_except_table3582
+ GCC_except_table3584
+ GCC_except_table3586
+ GCC_except_table3587
+ GCC_except_table3588
+ GCC_except_table3589
+ GCC_except_table3590
+ GCC_except_table3591
+ GCC_except_table3592
+ GCC_except_table3593
+ GCC_except_table3603
+ GCC_except_table3607
+ GCC_except_table3608
+ GCC_except_table3609
+ GCC_except_table3612
+ GCC_except_table3613
+ GCC_except_table3617
+ GCC_except_table3621
+ GCC_except_table3622
+ GCC_except_table3623
+ GCC_except_table3624
+ GCC_except_table3625
+ GCC_except_table3626
+ GCC_except_table3627
+ GCC_except_table3628
+ GCC_except_table3629
+ GCC_except_table3630
+ GCC_except_table3632
+ GCC_except_table3633
+ GCC_except_table3634
+ GCC_except_table3635
+ GCC_except_table3636
+ GCC_except_table3637
+ GCC_except_table3638
+ GCC_except_table3639
+ GCC_except_table3640
+ GCC_except_table3641
+ GCC_except_table3642
+ GCC_except_table3643
+ GCC_except_table3644
+ GCC_except_table3645
+ GCC_except_table3646
+ GCC_except_table3647
+ GCC_except_table3648
+ GCC_except_table3649
+ GCC_except_table3651
+ GCC_except_table3652
+ GCC_except_table3654
+ GCC_except_table3658
+ GCC_except_table3660
+ GCC_except_table3661
+ GCC_except_table3675
+ GCC_except_table3686
+ GCC_except_table3687
+ GCC_except_table3721
+ GCC_except_table3722
+ GCC_except_table3725
+ GCC_except_table387
+ GCC_except_table406
+ GCC_except_table416
+ GCC_except_table417
+ GCC_except_table418
+ GCC_except_table427
+ GCC_except_table445
+ GCC_except_table446
+ GCC_except_table458
+ GCC_except_table477
+ GCC_except_table490
+ GCC_except_table492
+ GCC_except_table510
+ GCC_except_table515
+ GCC_except_table528
+ GCC_except_table529
+ GCC_except_table530
+ GCC_except_table535
+ GCC_except_table539
+ GCC_except_table562
+ GCC_except_table564
+ GCC_except_table573
+ GCC_except_table577
+ GCC_except_table581
+ GCC_except_table582
+ GCC_except_table590
+ GCC_except_table594
+ GCC_except_table596
+ GCC_except_table600
+ GCC_except_table601
+ GCC_except_table602
+ GCC_except_table607
+ GCC_except_table611
+ GCC_except_table615
+ GCC_except_table619
+ GCC_except_table640
+ GCC_except_table647
+ GCC_except_table648
+ GCC_except_table649
+ GCC_except_table654
+ GCC_except_table666
+ GCC_except_table681
+ GCC_except_table685
+ GCC_except_table686
+ GCC_except_table687
+ GCC_except_table724
+ GCC_except_table725
+ GCC_except_table726
+ GCC_except_table735
+ GCC_except_table744
+ GCC_except_table750
+ GCC_except_table751
+ GCC_except_table766
+ GCC_except_table770
+ GCC_except_table772
+ GCC_except_table777
+ GCC_except_table781
+ GCC_except_table785
+ GCC_except_table786
+ GCC_except_table796
+ GCC_except_table809
+ GCC_except_table810
+ GCC_except_table815
+ GCC_except_table816
+ GCC_except_table817
+ GCC_except_table825
+ GCC_except_table826
+ GCC_except_table827
+ GCC_except_table836
+ GCC_except_table837
+ GCC_except_table843
+ GCC_except_table845
+ GCC_except_table857
+ GCC_except_table858
+ GCC_except_table865
+ GCC_except_table866
+ GCC_except_table867
+ GCC_except_table873
+ GCC_except_table874
+ GCC_except_table882
+ GCC_except_table884
+ GCC_except_table888
+ GCC_except_table890
+ GCC_except_table895
+ GCC_except_table897
+ GCC_except_table902
+ GCC_except_table904
+ GCC_except_table906
+ GCC_except_table911
+ GCC_except_table915
+ GCC_except_table920
+ GCC_except_table922
+ GCC_except_table939
+ GCC_except_table958
+ GCC_except_table962
+ GCC_except_table964
+ GCC_except_table972
+ GCC_except_table976
+ GCC_except_table985
+ GCC_except_table995
+ _AVAudioSessionModeEnrollment
+ _AVAudioSessionRouteControlChangeNotification
+ _AVAudioSessionRouteControlChangeOptionsKey
+ _AVSystemController_AudioVolumeNotificationParameter
+ _AVSystemController_SubscribeToNotificationsAttribute
+ _AVSystemController_SystemVolumeDidChangeNotification
+ _CFPreferencesCopyAppValue
+ _OBJC_CLASS_$_AVAudioDeviceTestService
+ _OBJC_CLASS_$_AVAudioDeviceTestServiceDelegate
+ _OBJC_CLASS_$_AVAudioSessionRouteControl
+ _OBJC_CLASS_$_NSThread
+ _OBJC_IVAR_$_AVAudioDeviceTest._service
+ _OBJC_IVAR_$_AVAudioDeviceTestService._currentSession
+ _OBJC_IVAR_$_AVAudioDeviceTestService._engine
+ _OBJC_IVAR_$_AVAudioDeviceTestService._extensionHandle
+ _OBJC_IVAR_$_AVAudioDeviceTestService._inputFilter
+ _OBJC_IVAR_$_AVAudioDeviceTestService._inputTapFile
+ _OBJC_IVAR_$_AVAudioDeviceTestService._interruptionObserver
+ _OBJC_IVAR_$_AVAudioDeviceTestService._mediaservicesLostObserver
+ _OBJC_IVAR_$_AVAudioDeviceTestService._mediaservicesResetObserver
+ _OBJC_IVAR_$_AVAudioDeviceTestService._multichannelMixer
+ _OBJC_IVAR_$_AVAudioDeviceTestService._nodeToCaptureData
+ _OBJC_IVAR_$_AVAudioDeviceTestService._outputFilter
+ _OBJC_IVAR_$_AVAudioDeviceTestService._player
+ _OBJC_IVAR_$_AVAudioDeviceTestService._routeChangeObserver
+ _OBJC_IVAR_$_AVAudioDeviceTestService._sourceNode
+ _OBJC_IVAR_$_AVAudioDeviceTestService._systemVolumeObserver
+ _OBJC_IVAR_$_AVAudioDeviceTestService._testServiceSupportedOnHardware
+ _OBJC_IVAR_$_AVAudioDeviceTestService._toneQueue
+ _OBJC_IVAR_$_AVAudioDeviceTestService._transaction
+ _OBJC_IVAR_$_AVAudioDeviceTestService._userVolumeBeforeHearingTest
+ _OBJC_IVAR_$_AVAudioDeviceTestService.mPulseToneHandler
+ _OBJC_METACLASS_$_AVAudioDeviceTestService
+ _OBJC_METACLASS_$_AVAudioDeviceTestServiceDelegate
+ _OBJC_METACLASS_$_AVAudioSessionRouteControl
+ __OBJC_$_INSTANCE_METHODS_AVAudioDeviceTestService
+ __OBJC_$_INSTANCE_METHODS_AVAudioDeviceTestServiceDelegate
+ __OBJC_$_INSTANCE_VARIABLES_AVAudioDeviceTestService
+ __OBJC_$_PROP_LIST_AVAudioDeviceTestService
+ __OBJC_$_PROP_LIST_AVAudioDeviceTestServiceDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_REFS_NSXPCListenerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_AVAudioDeviceTestService
+ __OBJC_CLASS_PROTOCOLS_$_AVAudioDeviceTestServiceDelegate
+ __OBJC_CLASS_RO_$_AVAudioDeviceTestService
+ __OBJC_CLASS_RO_$_AVAudioDeviceTestServiceDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSXPCListenerDelegate
+ __OBJC_METACLASS_RO_$_AVAudioDeviceTestService
+ __OBJC_METACLASS_RO_$_AVAudioDeviceTestServiceDelegate
+ __OBJC_PROTOCOL_$_NSXPCListenerDelegate
+ __ZL21MediaSafetyNetLibraryv
+ __ZL26audit_stringMediaSafetyNet
+ __ZL26generateAudioSelfTestError26AVAudioDeviceTestErrorCode
+ __ZN11ElapsedTimeC2EPKcS1_b
+ __ZN17AVAudioEngineImpl12UninitializeEPP7NSError
+ __ZN17AVAudioEngineImpl16DisconnectOutputEP11AVAudioNodem
+ __ZN17AVAudioEngineImpl16GraphDescriptionEv
+ __ZN17AVAudioEngineImpl19DisconnectAllInputsEP11AVAudioNode
+ __ZN17AVAudioEngineImpl20DisconnectAllOutputsEP11AVAudioNode
+ __ZN18AVAudioEngineGraph11SetSequenceEP19OpaqueMusicSequence
+ __ZN18AVAudioEngineGraph13RenderOfflineEjP16AVAudioPCMBufferPP7NSError
+ __ZN18AVAudioEngineGraph22ConnectMultipleOutputsEP11AVAudioNodeP7NSArraymP13AVAudioFormat
+ __ZN18AVAudioEngineGraph22SetAutoShutdownEnabledEb
+ __ZN18AVAudioEngineGraph5ResetEv
+ __ZN18AVAudioEngineGraphC1ERK17AVAudioEngineImpl
+ __ZNK18AVAudioEngineGraph11GetSequenceEv
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB8ue170006IS4_EENS_12basic_stringIcS2_T_EERKS8_
+ __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE4viewB8ue170006Ev
+ __ZNKSt3__16vectorI12WorkloopInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorI23EExtAudioGraphNodeStateNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorI30AVAEStreamFormatObserverStructNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIN17AUInterfaceBaseV314RenderObserverENS_9allocatorIS2_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorINS_10unique_ptrIN5caulk17semaphore_mutex_tINS2_9semaphoreEEENS_14default_deleteIS5_EEEENS_9allocatorIS8_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIP11AVAudioNodeNS_9allocatorIS2_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIP17AUGraphNodeBaseV3NS_9allocatorIS2_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIP17AUGraphNodeBaseV3NS_9allocatorIS2_EEE20__throw_out_of_rangeB8ue170006Ev
+ __ZNKSt3__16vectorIP19AVAudioNodeImplBaseNS_9allocatorIS2_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIP22CompletionHandlerTimerNS_9allocatorIS2_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIP8NSNumberNS_9allocatorIS2_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIbNS_9allocatorIbEEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_out_of_rangeB8ue170006Ev
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt12out_of_rangeC1B8ue170006EPKc
+ __ZNSt3__110__function12__value_funcIF16ETraversalStatusR17AUGraphNodeBaseV3P17AUGraphConnectionEED2B8ue170006Ev
+ __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrI19AVVCRecordingEngineEEEEC2B8ue170006ERKS6_
+ __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrI19AVVCRecordingEngineEEEED2B8ue170006Ev
+ __ZNSt3__110__function12__value_funcIFvbEE4swapB8ue170006ERS3_
+ __ZNSt3__110__function12__value_funcIFvbEEC2B8ue170006ERKS3_
+ __ZNSt3__110__function12__value_funcIFvbEED2B8ue170006Ev
+ __ZNSt3__110shared_ptrI14ControllerImplEC2B8ue170006IS1_vEERKNS_8weak_ptrIT_EE
+ __ZNSt3__110shared_ptrI19AVVCRecordingEngineEC2B8ue170006IS1_vEERKNS_8weak_ptrIT_EE
+ __ZNSt3__110unique_ptrI18AVAudioEngineGraphNS_14default_deleteIS1_EEE5resetB8ue170006EPS1_
+ __ZNSt3__110unique_ptrI21AVAEGraphStateTrackerNS_14default_deleteIS1_EEE5resetB8ue170006EPS1_
+ __ZNSt3__110unique_ptrI22AVAEDispatchQueueTimerNS_14default_deleteIS1_EEE5resetB8ue170006EPS1_
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerF34AVAudioEngineManualRenderingStatusjP15AudioBufferListPiEENS_14default_deleteIS8_EEE5resetB8ue170006EPS8_
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFPK15AudioBufferListjEENS_14default_deleteIS7_EEE5resetB8ue170006EPS7_
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFiPjPK14AudioTimeStampjlP15AudioBufferListEENS_14default_deleteISA_EEE5resetB8ue170006EPSA_
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFiPjPK14AudioTimeStampjlP15AudioBufferListU13block_pointerFiS2_S5_jlS7_EEENS_14default_deleteISC_EEE5resetB8ue170006EPSC_
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFixhPK13MIDIEventListEENS_14default_deleteIS7_EEE5resetB8ue170006EPS7_
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFixhlPKhEENS_14default_deleteIS6_EEE5resetB8ue170006EPS6_
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFv39AVAudioPlayerNodeCompletionCallbackTypeEENS_14default_deleteIS5_EEE5resetB8ue170006EPS5_
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFvPjPK14AudioTimeStampjlEENS_14default_deleteIS8_EEE5resetB8ue170006EPS8_
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFvjPK14AudioTimeStampjlEENS_14default_deleteIS7_EEE5resetB8ue170006EPS7_
+ __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFvxhlPKhEENS_14default_deleteIS6_EEE5resetB8ue170006EPS6_
+ __ZNSt3__110unique_ptrIN4MIDI16LegacyPacketListENS1_23LegacyPacketListDeleterEE5resetB8ue170006EPS2_
+ __ZNSt3__110unique_ptrIN5caulk17semaphore_mutex_tINS1_9semaphoreEEENS_14default_deleteIS4_EEE5resetB8ue170006EPS4_
+ __ZNSt3__110unique_ptrINS_3mapINS_4pairIP11AVAudioNodejEEP24AVAudioMixingDestinationNS_4lessIS5_EENS_9allocatorINS2_IKS5_S7_EEEEEENS_14default_deleteISE_EEE5resetB8ue170006EPSE_
+ __ZNSt3__110unique_ptrIZN20AVAudioSequencerImpl4StopEvE3$_1NS_14default_deleteIS2_EEED1B8ue170006Ev
+ __ZNSt3__110unique_ptrIZN20AVAudioSequencerImplD1EvE3$_0NS_14default_deleteIS2_EEED1B8ue170006Ev
+ __ZNSt3__111unique_lockIN5caulk17semaphore_mutex_tINS1_9semaphoreEEEED2B8ue170006Ev
+ __ZNSt3__111unique_lockIN5caulk27recursive_semaphore_mutex_tINS1_9semaphoreEEEED2B8ue170006Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ue170006Emc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ue170006ILi0EEEPKc
+ __ZNSt3__113__tree_removeB8ue170006IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__116__pad_and_outputB8ue170006IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ue170006IONS1_9__variant15__value_visitorIZN17AUGraphNodeBaseV320CreateMIDIConnectionERK21AUGraphMIDIConnectionE3$_1EEJRKNS0_6__baseILNS0_6_TraitE0EJU13block_pointerFixhlPKhEU13block_pointerFixhPK13MIDIEventListEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ue170006IONS1_9__variant15__value_visitorIZN17AUGraphNodeBaseV320CreateMIDIConnectionERK21AUGraphMIDIConnectionE3$_1EEJRKNS0_6__baseILNS0_6_TraitE0EJU13block_pointerFixhlPKhEU13block_pointerFixhPK13MIDIEventListEEEEEEEDcT_DpT0_
+ __ZNSt3__117__call_once_proxyB8ue170006INS_5tupleIJOZN12CADeprecated10TSingletonINS2_19RealtimeDeallocatorEE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ue170006Ev
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorI23EExtAudioGraphNodeStateEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIP17AUGraphNodeBaseV3EEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIP8NSNumberEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ue170006Ev
+ __ZNSt3__120__throw_bad_weak_ptrB8ue170006Ev
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ue170006EPKc
+ __ZNSt3__124__put_character_sequenceB8ue170006IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__125__throw_bad_function_callB8ue170006Ev
+ __ZNSt3__126__throw_bad_variant_accessB8ue170006Ev
+ __ZNSt3__127__tree_balance_after_insertB8ue170006IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__14lockB8ue170006IN5caulk17semaphore_mutex_tINS1_9semaphoreEEES4_EEvRT_RT0_
+ __ZNSt3__14lockB8ue170006INS_15recursive_mutexEN5caulk27recursive_semaphore_mutex_tINS2_9semaphoreEEEEEvRT_RT0_
+ __ZNSt3__16vectorIN17AUInterfaceBaseV314RenderObserverENS_9allocatorIS2_EEE16__destroy_vectorclB8ue170006Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN5caulk17semaphore_mutex_tINS2_9semaphoreEEENS_14default_deleteIS5_EEEENS_9allocatorIS8_EEE16__destroy_vectorclB8ue170006Ev
+ __ZNSt3__16vectorIP17AUGraphNodeBaseV3NS_9allocatorIS2_EEE18__assign_with_sizeB8ue170006IPS2_S7_EEvT_T0_l
+ __ZNSt3__16vectorIP17AUGraphNodeBaseV3NS_9allocatorIS2_EEE9push_backB8ue170006ERKS2_
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE11__vallocateB8ue170006Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2EmRKf
+ __ZNSt3__16vectorIjNS_9allocatorIjEEEC1B8ue170006ESt16initializer_listIjE
+ __ZNSt3__18optionalIN2CA10BufferListEEaSB8ue170006IS2_vEERS3_OT_
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ __ZZ27AVAudioDeviceTestServiceLogvE4once
+ __ZZ27AVAudioDeviceTestServiceLogvE8category
+ __ZZ36AVAudioDeviceTestServicePulseToneLogvE4once
+ __ZZ36AVAudioDeviceTestServicePulseToneLogvE8category
+ __ZZL25MediaSafetyNetLibraryCorePPcE16frameworkLibrary.0
+ __ZZL34getMSNMonitorEndExceptionSymbolLocvE3ptr.0
+ __ZZL36getMSNMonitorBeginExceptionSymbolLocvE3ptr.0
+ ___40-[AVAudioDeviceTestService stopPlayback]_block_invoke
+ ___43-[AVAudioDeviceTestService setupObservers:]_block_invoke
+ ___43-[AVAudioDeviceTestService setupObservers:]_block_invoke.165
+ ___43-[AVAudioDeviceTestService setupObservers:]_block_invoke.166
+ ___43-[AVAudioDeviceTestService setupObservers:]_block_invoke.167
+ ___50-[AVAudioDeviceTest startWithSequence:completion:]_block_invoke.47
+ ___52-[AVAudioDeviceTestService playbackTone:completion:]_block_invoke
+ ___52-[AVAudioDeviceTestService playbackTone:completion:]_block_invoke.127
+ ___52-[AVAudioDeviceTestService playbackTone:completion:]_block_invoke.137
+ ___52-[AVAudioDeviceTestService playbackTone:completion:]_block_invoke_2
+ ___52-[AVAudioDeviceTestService playbackTone:completion:]_block_invoke_2.129
+ ___52-[AVAudioDeviceTestService playbackTone:completion:]_block_invoke_3
+ ___52-[AVAudioDeviceTestService playbackTone:completion:]_block_invoke_3.134
+ ___52-[AVAudioDeviceTestService playbackTone:completion:]_block_invoke_4
+ ___52-[AVAudioDeviceTestService playbackTone:completion:]_block_invoke_5
+ ___52-[AVVoiceTriggerClient voiceTriggerServerConnection]_block_invoke.175
+ ___52-[AVVoiceTriggerClient voiceTriggerServerConnection]_block_invoke.179
+ ___54-[AVVoiceTriggerClient getInputChannelInfoCompletion:]_block_invoke.187
+ ___55-[AVVoiceTriggerClient portStateActiveCompletionBlock:]_block_invoke.219
+ ___56-[AVVoiceTriggerClient listeningEnabledCompletionBlock:]_block_invoke.227
+ ___57-[AVAudioDeviceTestService playback:filePath:completion:]_block_invoke
+ ___57-[AVAudioDeviceTestService playback:filePath:completion:]_block_invoke.139
+ ___57-[AVAudioDeviceTestService startWithSequence:completion:]_block_invoke
+ ___57-[AVAudioDeviceTestService startWithSequence:completion:]_block_invoke.105
+ ___57-[AVAudioDeviceTestService startWithSequence:completion:]_block_invoke.106
+ ___57-[AVAudioDeviceTestService startWithSequence:completion:]_block_invoke.112
+ ___57-[AVAudioDeviceTestService startWithSequence:completion:]_block_invoke.114
+ ___57-[AVAudioDeviceTestService startWithSequence:completion:]_block_invoke.116
+ ___57-[AVAudioDeviceTestService startWithSequence:completion:]_block_invoke.119
+ ___57-[AVAudioDeviceTestService startWithSequence:completion:]_block_invoke.123
+ ___57-[AVVoiceTriggerClient speakerStateMutedCompletionBlock:]_block_invoke.213
+ ___58-[AVAudioDeviceTestService convertBufferFor:sourceBuffer:]_block_invoke
+ ___58-[AVVoiceTriggerClient enableBargeInMode:completionBlock:]_block_invoke.222
+ ___58-[AVVoiceTriggerClient speakerStateActiveCompletionBlock:]_block_invoke.209
+ ___59-[AVVoiceTriggerClient voiceTriggerPastDataFramesAvailable]_block_invoke.193
+ ___60-[AVVoiceTriggerClient setAggressiveECMode:completionBlock:]_block_invoke.233
+ ___60-[AVVoiceTriggerClient siriClientsRecordingCompletionBlock:]_block_invoke.229
+ ___63-[AVAudioDeviceTestService startRecording:filePath:completion:]_block_invoke
+ ___63-[AVVoiceTriggerClient enableListeningOnPorts:completionBlock:]_block_invoke.217
+ ___68-[AVAudioDeviceTestService setupVolumeObserverForVolume:completion:]_block_invoke
+ ___68-[AVVoiceTriggerClient enableSpeakerStateListening:completionBlock:]_block_invoke.206
+ ___68-[AVVoiceTriggerClient enableVoiceTriggerListening:completionBlock:]_block_invoke.200
+ ___70-[AVVoiceTriggerClient voiceTriggerPastDataFramesAvailableCompletion:]_block_invoke.184
+ ___72-[AVVoiceTriggerClient updateVoiceTriggerConfiguration:completionBlock:]_block_invoke.225
+ ___88-[AVAudioDeviceTestService createAudioEngineAndProcessingChain:session:sourceNodeBlock:]_block_invoke
+ ___Block_byref_object_copy_.1214
+ ___Block_byref_object_copy_.146
+ ___Block_byref_object_copy_.3380
+ ___Block_byref_object_copy_.5363
+ ___Block_byref_object_copy_.6150
+ ___Block_byref_object_copy_.681
+ ___Block_byref_object_copy_.7007
+ ___Block_byref_object_copy_.8454
+ ___Block_byref_object_dispose_.1215
+ ___Block_byref_object_dispose_.147
+ ___Block_byref_object_dispose_.3381
+ ___Block_byref_object_dispose_.5364
+ ___Block_byref_object_dispose_.6151
+ ___Block_byref_object_dispose_.682
+ ___Block_byref_object_dispose_.7008
+ ___Block_byref_object_dispose_.8455
+ ____Z27AVAudioDeviceTestServiceLogv_block_invoke
+ ____Z36AVAudioDeviceTestServicePulseToneLogv_block_invoke
+ ____ZL25MediaSafetyNetLibraryCorePPc_block_invoke
+ ____ZL34getMSNMonitorEndExceptionSymbolLocv_block_invoke
+ ____ZL36getMSNMonitorBeginExceptionSymbolLocv_block_invoke
+ ____ZN14ControllerImpl10setContextEP17AVVoiceControllerP19AVVCContextSettingsU13block_pointerFvm14AVVCStreamTypeP7NSErrorE_block_invoke.263
+ ____ZN17AVAudioEngineImpl26IOUnitConfigurationChangedEv_block_invoke.166
+ ___block_descriptor_36_e24_v16?0"NSNotification"8l
+ ___block_descriptor_40_ea8_32bs_e24_v16?0"NSNotification"8ls32l8
+ ___block_descriptor_40_ea8_32r_e103_i36?0^B8r^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}16I24^{AudioBufferList=I[1{AudioBuffer=II^v}]}28lr32l8
+ ___block_descriptor_40_ea8_32s_e24_v16?0"NSNotification"8ls32l8
+ ___block_descriptor_40_ea8_32s_e27_"AVAudioBuffer"20?0I8^q12ls32l8
+ ___block_descriptor_40_ea8_32s_e33_v24?0"AVAudioUnit"8"NSError"16ls32l8
+ ___block_descriptor_40_ea8_32s_e42_v24?0"AVAudioPCMBuffer"8"AVAudioTime"16ls32l8
+ ___block_descriptor_48_ea8_32s40bs_e24_v16?0"NSNotification"8ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e42_v24?0"AVAudioPCMBuffer"8"AVAudioTime"16ls32l8s40l8
+ ___block_descriptor_56_ea8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_56_ea8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_40c44_ZTSNSt3__18weak_ptrI19AVVCRecordingEngineEE_e56_v32?0"AVAudioBuffer"8"AVAudioTime"16"NSDictionary"24l
+ ___block_descriptor_64_ea8_32s40bs48r56r_e42_v24?0"AVAudioPCMBuffer"8"AVAudioTime"16lr48l8s40l8r56l8s32l8
+ ___block_descriptor_72_ea8_32s40s48s56bs64r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_80_ea8_32s40s48s56s64s72r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r72l8
+ ___block_descriptor_tmp.1157
+ ___block_descriptor_tmp.1420
+ ___block_descriptor_tmp.1428
+ ___block_descriptor_tmp.5834
+ ___block_descriptor_tmp.5880
+ ___block_literal_global.118
+ ___block_literal_global.1343
+ ___block_literal_global.143
+ ___block_literal_global.1693
+ ___block_literal_global.178
+ ___block_literal_global.181
+ ___block_literal_global.192
+ ___block_literal_global.196
+ ___block_literal_global.2060
+ ___block_literal_global.210
+ ___block_literal_global.2419
+ ___block_literal_global.2727
+ ___block_literal_global.3032
+ ___block_literal_global.3317
+ ___block_literal_global.38.2094
+ ___block_literal_global.4817
+ ___block_literal_global.5404
+ ___block_literal_global.5797
+ ___block_literal_global.5862
+ ___block_literal_global.5878
+ ___block_literal_global.6284
+ ___block_literal_global.7009
+ ___block_literal_global.758
+ ___block_literal_global.7746
+ ___block_literal_global.8134
+ ___block_literal_global.8326
+ ___error
+ ___exp10f
+ __dispatch_queue_attr_concurrent
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _exit
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_exception_rethrow
+ _objc_msgSend$allowAllBuiltInDataSources
+ _objc_msgSend$appendDataFromBuffer:
+ _objc_msgSend$appendString:
+ _objc_msgSend$availableInputs
+ _objc_msgSend$averagePowerPerChannel
+ _objc_msgSend$bands
+ _objc_msgSend$calculateCrossCorrelationPeak
+ _objc_msgSend$calculateCrossCorrelationPeakRelativeToSource:capture:
+ _objc_msgSend$categoryOptions
+ _objc_msgSend$checkSequenceValidity:completion:
+ _objc_msgSend$cleanUp
+ _objc_msgSend$cleanUpObservers
+ _objc_msgSend$configureDataSources:session:
+ _objc_msgSend$configureMultiChannelMixerForOutputChannel:totalChannels:
+ _objc_msgSend$convertBufferFor:sourceBuffer:
+ _objc_msgSend$convertToBuffer:error:withInputFromBlock:
+ _objc_msgSend$createAudioEngineAndProcessingChain:session:sourceNodeBlock:
+ _objc_msgSend$createAudioEngineAndPulseToneHandlerFor:
+ _objc_msgSend$dataSourceID
+ _objc_msgSend$dataSources
+ _objc_msgSend$duration
+ _objc_msgSend$extensionHandle
+ _objc_msgSend$frequency
+ _objc_msgSend$getActiveCategoryVolume:andName:
+ _objc_msgSend$getSiriInputSource:withIdentifier:withIsMicrophoneCheck:forActivationMode:
+ _objc_msgSend$initForReading:error:
+ _objc_msgSend$initForWriting:settings:error:
+ _objc_msgSend$initFromFormat:toFormat:
+ _objc_msgSend$initWithData:inputID:outputID:sampleRate:correlationValue:
+ _objc_msgSend$initWithFloat:
+ _objc_msgSend$initWithRenderBlock:
+ _objc_msgSend$inputFilter
+ _objc_msgSend$inputProcessingChain
+ _objc_msgSend$inputTapFile
+ _objc_msgSend$installTapOnBus:bufferSize:format:block:
+ _objc_msgSend$instantiateWithComponentDescription:options:completionHandler:
+ _objc_msgSend$interruptionObserver
+ _objc_msgSend$isActive
+ _objc_msgSend$isMixerOutputEnabled
+ _objc_msgSend$isOutputRouteBluetooth:session:
+ _objc_msgSend$mediaservicesLostObserver
+ _objc_msgSend$mediaservicesResetObserver
+ _objc_msgSend$micBufferNumbers
+ _objc_msgSend$microphone
+ _objc_msgSend$multichannelMixer
+ _objc_msgSend$nodeToCaptureData
+ _objc_msgSend$numberOfPulses
+ _objc_msgSend$outputFilter
+ _objc_msgSend$outputMode
+ _objc_msgSend$outputProcessingChain
+ _objc_msgSend$outputSampleRate
+ _objc_msgSend$overrideOutputAudioPort:error:
+ _objc_msgSend$parallelCrossCorrelationCalculation
+ _objc_msgSend$pauseDuration
+ _objc_msgSend$play
+ _objc_msgSend$player
+ _objc_msgSend$preferredIOBufferFrameSize
+ _objc_msgSend$prepare
+ _objc_msgSend$priority
+ _objc_msgSend$processingFormat
+ _objc_msgSend$pulseDuration
+ _objc_msgSend$rampDuration
+ _objc_msgSend$readIntoBuffer:error:
+ _objc_msgSend$removeTapOnBus:
+ _objc_msgSend$requiresBluetoothOutput
+ _objc_msgSend$resetVolume:
+ _objc_msgSend$routeChangeObserver
+ _objc_msgSend$routeForCategory:
+ _objc_msgSend$service
+ _objc_msgSend$setActiveCategoryVolumeTo:
+ _objc_msgSend$setAllowAllBuiltInDataSources:
+ _objc_msgSend$setAttribute:forKey:error:
+ _objc_msgSend$setBandwidth:
+ _objc_msgSend$setBypass:
+ _objc_msgSend$setCategory:error:
+ _objc_msgSend$setEngine:
+ _objc_msgSend$setExtensionHandle:
+ _objc_msgSend$setFilterType:
+ _objc_msgSend$setFrequency:
+ _objc_msgSend$setInputFilter:
+ _objc_msgSend$setInputTapFile:
+ _objc_msgSend$setInterruptionObserver:
+ _objc_msgSend$setInterruptionPriority:error:
+ _objc_msgSend$setMediaservicesLostObserver:
+ _objc_msgSend$setMediaservicesResetObserver:
+ _objc_msgSend$setMode:error:
+ _objc_msgSend$setMultichannelMixer:
+ _objc_msgSend$setNodeToCaptureData:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setOutputFilter:
+ _objc_msgSend$setPlayer:
+ _objc_msgSend$setPreferredDataSource:error:
+ _objc_msgSend$setPreferredInput:error:
+ _objc_msgSend$setRouteChangeObserver:
+ _objc_msgSend$setService:
+ _objc_msgSend$setSourceNode:
+ _objc_msgSend$setSystemVolumeObserver:
+ _objc_msgSend$setTestServiceSupportedOnHardware:
+ _objc_msgSend$setToneQueue:
+ _objc_msgSend$setTransaction:
+ _objc_msgSend$setUserVolumeBeforeHearingTest:
+ _objc_msgSend$setVolume:session:
+ _objc_msgSend$setVolumeTo:forCategory:
+ _objc_msgSend$setupAudioEngineFor:sourceNodeBlock:
+ _objc_msgSend$setupAudioSessionFor:playbackOnly:completion:
+ _objc_msgSend$setupMultiChannelMixerForOutputChannel:completion:
+ _objc_msgSend$setupObservers:
+ _objc_msgSend$setupVolumeObserverForVolume:completion:
+ _objc_msgSend$sleepForTimeInterval:
+ _objc_msgSend$soundLevel
+ _objc_msgSend$sourceNode
+ _objc_msgSend$splitIntoSingleChannelBuffers
+ _objc_msgSend$startDelay
+ _objc_msgSend$stringForInterruptionReason:
+ _objc_msgSend$stringForRouteChangeReason:
+ _objc_msgSend$systemVolumeObserver
+ _objc_msgSend$toneQueue
+ _objc_msgSend$transaction
+ _objc_msgSend$url
+ _objc_msgSend$userVolumeBeforeHearingTest
+ _objc_msgSend$valueForEntitlement:
+ _objc_msgSend$writeFromBuffer:error:
+ _os_transaction_create
+ _sandbox_extension_consume
+ _sandbox_extension_release
+ _sin
+ _usleep
+ _vDSP_conv
- -[AVVCSessionManager getSiriInputSource:withIdentifier:]
- GCC_except_table1006
- GCC_except_table1017
- GCC_except_table1019
- GCC_except_table103
- GCC_except_table1037
- GCC_except_table1045
- GCC_except_table1053
- GCC_except_table106
- GCC_except_table1064
- GCC_except_table108
- GCC_except_table1082
- GCC_except_table110
- GCC_except_table1105
- GCC_except_table1110
- GCC_except_table1111
- GCC_except_table1112
- GCC_except_table112
- GCC_except_table1126
- GCC_except_table114
- GCC_except_table1155
- GCC_except_table116
- GCC_except_table1166
- GCC_except_table1176
- GCC_except_table1177
- GCC_except_table1178
- GCC_except_table1188
- GCC_except_table1197
- GCC_except_table1200
- GCC_except_table1201
- GCC_except_table1208
- GCC_except_table122
- GCC_except_table1236
- GCC_except_table124
- GCC_except_table1242
- GCC_except_table1246
- GCC_except_table1247
- GCC_except_table128
- GCC_except_table1282
- GCC_except_table1296
- GCC_except_table133
- GCC_except_table1332
- GCC_except_table1333
- GCC_except_table1334
- GCC_except_table1344
- GCC_except_table1345
- GCC_except_table1346
- GCC_except_table1367
- GCC_except_table1368
- GCC_except_table1369
- GCC_except_table1371
- GCC_except_table1372
- GCC_except_table1376
- GCC_except_table138
- GCC_except_table1393
- GCC_except_table1409
- GCC_except_table1410
- GCC_except_table1413
- GCC_except_table1425
- GCC_except_table1426
- GCC_except_table1427
- GCC_except_table1437
- GCC_except_table1438
- GCC_except_table1439
- GCC_except_table144
- GCC_except_table1440
- GCC_except_table1441
- GCC_except_table1451
- GCC_except_table1452
- GCC_except_table1453
- GCC_except_table1454
- GCC_except_table1456
- GCC_except_table1457
- GCC_except_table147
- GCC_except_table1481
- GCC_except_table1482
- GCC_except_table1487
- GCC_except_table1498
- GCC_except_table1499
- GCC_except_table1500
- GCC_except_table1502
- GCC_except_table1503
- GCC_except_table1505
- GCC_except_table1509
- GCC_except_table1512
- GCC_except_table1514
- GCC_except_table1533
- GCC_except_table1534
- GCC_except_table1535
- GCC_except_table1536
- GCC_except_table1538
- GCC_except_table1539
- GCC_except_table1553
- GCC_except_table1556
- GCC_except_table1557
- GCC_except_table1559
- GCC_except_table1563
- GCC_except_table1568
- GCC_except_table1579
- GCC_except_table1581
- GCC_except_table1585
- GCC_except_table1609
- GCC_except_table1610
- GCC_except_table1615
- GCC_except_table1616
- GCC_except_table1619
- GCC_except_table1622
- GCC_except_table1628
- GCC_except_table1629
- GCC_except_table1639
- GCC_except_table165
- GCC_except_table1663
- GCC_except_table1664
- GCC_except_table167
- GCC_except_table1670
- GCC_except_table1671
- GCC_except_table1674
- GCC_except_table1677
- GCC_except_table1678
- GCC_except_table1698
- GCC_except_table170
- GCC_except_table1706
- GCC_except_table1713
- GCC_except_table1716
- GCC_except_table1717
- GCC_except_table173
- GCC_except_table1753
- GCC_except_table179
- GCC_except_table186
- GCC_except_table189
- GCC_except_table1905
- GCC_except_table1907
- GCC_except_table1908
- GCC_except_table1909
- GCC_except_table1912
- GCC_except_table1917
- GCC_except_table1921
- GCC_except_table1923
- GCC_except_table1925
- GCC_except_table1926
- GCC_except_table1927
- GCC_except_table1936
- GCC_except_table1939
- GCC_except_table194
- GCC_except_table1940
- GCC_except_table1944
- GCC_except_table1945
- GCC_except_table1947
- GCC_except_table1948
- GCC_except_table1949
- GCC_except_table1950
- GCC_except_table1954
- GCC_except_table1956
- GCC_except_table1957
- GCC_except_table1958
- GCC_except_table1960
- GCC_except_table1962
- GCC_except_table1964
- GCC_except_table1971
- GCC_except_table1972
- GCC_except_table1979
- GCC_except_table1999
- GCC_except_table2000
- GCC_except_table2001
- GCC_except_table2055
- GCC_except_table2056
- GCC_except_table2059
- GCC_except_table2063
- GCC_except_table2064
- GCC_except_table2073
- GCC_except_table209
- GCC_except_table210
- GCC_except_table2110
- GCC_except_table2113
- GCC_except_table2115
- GCC_except_table2125
- GCC_except_table2126
- GCC_except_table2129
- GCC_except_table2131
- GCC_except_table2132
- GCC_except_table2134
- GCC_except_table2136
- GCC_except_table2140
- GCC_except_table2149
- GCC_except_table215
- GCC_except_table2150
- GCC_except_table2151
- GCC_except_table2152
- GCC_except_table2169
- GCC_except_table2170
- GCC_except_table2171
- GCC_except_table2176
- GCC_except_table2182
- GCC_except_table2187
- GCC_except_table2189
- GCC_except_table2190
- GCC_except_table2196
- GCC_except_table2197
- GCC_except_table2198
- GCC_except_table2199
- GCC_except_table2200
- GCC_except_table2201
- GCC_except_table2202
- GCC_except_table2203
- GCC_except_table2205
- GCC_except_table2206
- GCC_except_table2213
- GCC_except_table2214
- GCC_except_table2216
- GCC_except_table2219
- GCC_except_table2220
- GCC_except_table2223
- GCC_except_table2225
- GCC_except_table2226
- GCC_except_table2228
- GCC_except_table2229
- GCC_except_table2230
- GCC_except_table2231
- GCC_except_table2233
- GCC_except_table2238
- GCC_except_table2239
- GCC_except_table2246
- GCC_except_table2249
- GCC_except_table2250
- GCC_except_table2252
- GCC_except_table2255
- GCC_except_table2257
- GCC_except_table2259
- GCC_except_table2260
- GCC_except_table2265
- GCC_except_table2270
- GCC_except_table2279
- GCC_except_table2280
- GCC_except_table2284
- GCC_except_table2286
- GCC_except_table2287
- GCC_except_table2294
- GCC_except_table2301
- GCC_except_table2313
- GCC_except_table2326
- GCC_except_table2329
- GCC_except_table2330
- GCC_except_table2331
- GCC_except_table2344
- GCC_except_table2349
- GCC_except_table2359
- GCC_except_table2362
- GCC_except_table2363
- GCC_except_table2364
- GCC_except_table2365
- GCC_except_table2366
- GCC_except_table2370
- GCC_except_table2373
- GCC_except_table2383
- GCC_except_table2384
- GCC_except_table2385
- GCC_except_table2386
- GCC_except_table2388
- GCC_except_table2389
- GCC_except_table2390
- GCC_except_table2391
- GCC_except_table2393
- GCC_except_table2394
- GCC_except_table2395
- GCC_except_table2396
- GCC_except_table2397
- GCC_except_table2398
- GCC_except_table2404
- GCC_except_table2405
- GCC_except_table2418
- GCC_except_table2419
- GCC_except_table2420
- GCC_except_table2421
- GCC_except_table2422
- GCC_except_table2424
- GCC_except_table2433
- GCC_except_table2436
- GCC_except_table2437
- GCC_except_table2438
- GCC_except_table2439
- GCC_except_table244
- GCC_except_table2443
- GCC_except_table2445
- GCC_except_table2446
- GCC_except_table2449
- GCC_except_table2454
- GCC_except_table2455
- GCC_except_table2456
- GCC_except_table2459
- GCC_except_table2460
- GCC_except_table2461
- GCC_except_table2464
- GCC_except_table2468
- GCC_except_table2469
- GCC_except_table2474
- GCC_except_table2476
- GCC_except_table2477
- GCC_except_table2478
- GCC_except_table2479
- GCC_except_table2480
- GCC_except_table2489
- GCC_except_table2493
- GCC_except_table2494
- GCC_except_table2496
- GCC_except_table2497
- GCC_except_table2499
- GCC_except_table2500
- GCC_except_table2521
- GCC_except_table2522
- GCC_except_table2523
- GCC_except_table2525
- GCC_except_table2528
- GCC_except_table2529
- GCC_except_table2530
- GCC_except_table2531
- GCC_except_table2532
- GCC_except_table2533
- GCC_except_table2534
- GCC_except_table2535
- GCC_except_table2536
- GCC_except_table2537
- GCC_except_table2538
- GCC_except_table2539
- GCC_except_table2548
- GCC_except_table2549
- GCC_except_table2550
- GCC_except_table2551
- GCC_except_table2556
- GCC_except_table2557
- GCC_except_table2566
- GCC_except_table257
- GCC_except_table2574
- GCC_except_table2579
- GCC_except_table258
- GCC_except_table2580
- GCC_except_table2584
- GCC_except_table259
- GCC_except_table2594
- GCC_except_table2597
- GCC_except_table2604
- GCC_except_table2612
- GCC_except_table2624
- GCC_except_table2627
- GCC_except_table2629
- GCC_except_table2635
- GCC_except_table2641
- GCC_except_table2642
- GCC_except_table267
- GCC_except_table2683
- GCC_except_table2684
- GCC_except_table2685
- GCC_except_table2687
- GCC_except_table269
- GCC_except_table2691
- GCC_except_table2693
- GCC_except_table2697
- GCC_except_table2699
- GCC_except_table2705
- GCC_except_table2709
- GCC_except_table2711
- GCC_except_table2731
- GCC_except_table2739
- GCC_except_table2745
- GCC_except_table2752
- GCC_except_table2758
- GCC_except_table277
- GCC_except_table281
- GCC_except_table282
- GCC_except_table2845
- GCC_except_table2846
- GCC_except_table2869
- GCC_except_table287
- GCC_except_table2873
- GCC_except_table2877
- GCC_except_table2882
- GCC_except_table2884
- GCC_except_table2885
- GCC_except_table2886
- GCC_except_table2887
- GCC_except_table2888
- GCC_except_table2889
- GCC_except_table2890
- GCC_except_table2891
- GCC_except_table2892
- GCC_except_table2893
- GCC_except_table2894
- GCC_except_table2895
- GCC_except_table2896
- GCC_except_table2897
- GCC_except_table2898
- GCC_except_table2899
- GCC_except_table2900
- GCC_except_table2901
- GCC_except_table2902
- GCC_except_table2903
- GCC_except_table2906
- GCC_except_table2907
- GCC_except_table2909
- GCC_except_table2910
- GCC_except_table2911
- GCC_except_table2912
- GCC_except_table2913
- GCC_except_table2914
- GCC_except_table2916
- GCC_except_table2917
- GCC_except_table2918
- GCC_except_table2919
- GCC_except_table292
- GCC_except_table2920
- GCC_except_table2923
- GCC_except_table2924
- GCC_except_table2925
- GCC_except_table2926
- GCC_except_table2928
- GCC_except_table2936
- GCC_except_table2938
- GCC_except_table2940
- GCC_except_table2944
- GCC_except_table2946
- GCC_except_table2948
- GCC_except_table2950
- GCC_except_table2952
- GCC_except_table2960
- GCC_except_table2963
- GCC_except_table297
- GCC_except_table2996
- GCC_except_table2997
- GCC_except_table302
- GCC_except_table3027
- GCC_except_table3030
- GCC_except_table304
- GCC_except_table3053
- GCC_except_table306
- GCC_except_table3077
- GCC_except_table3079
- GCC_except_table3088
- GCC_except_table3089
- GCC_except_table3090
- GCC_except_table3092
- GCC_except_table3093
- GCC_except_table3094
- GCC_except_table3095
- GCC_except_table3096
- GCC_except_table3098
- GCC_except_table3103
- GCC_except_table3107
- GCC_except_table311
- GCC_except_table3110
- GCC_except_table3133
- GCC_except_table3139
- GCC_except_table3140
- GCC_except_table3141
- GCC_except_table3143
- GCC_except_table3144
- GCC_except_table3148
- GCC_except_table3161
- GCC_except_table3162
- GCC_except_table3163
- GCC_except_table3164
- GCC_except_table3165
- GCC_except_table3171
- GCC_except_table3172
- GCC_except_table3173
- GCC_except_table3174
- GCC_except_table3176
- GCC_except_table3177
- GCC_except_table3178
- GCC_except_table3181
- GCC_except_table3213
- GCC_except_table3219
- GCC_except_table3222
- GCC_except_table3223
- GCC_except_table3224
- GCC_except_table3226
- GCC_except_table3227
- GCC_except_table3228
- GCC_except_table323
- GCC_except_table3230
- GCC_except_table3233
- GCC_except_table3234
- GCC_except_table3238
- GCC_except_table3239
- GCC_except_table324
- GCC_except_table3253
- GCC_except_table3257
- GCC_except_table3260
- GCC_except_table3279
- GCC_except_table3282
- GCC_except_table3288
- GCC_except_table3289
- GCC_except_table330
- GCC_except_table3304
- GCC_except_table331
- GCC_except_table3310
- GCC_except_table3311
- GCC_except_table3312
- GCC_except_table3313
- GCC_except_table3314
- GCC_except_table3340
- GCC_except_table3343
- GCC_except_table3347
- GCC_except_table3353
- GCC_except_table3357
- GCC_except_table3358
- GCC_except_table3359
- GCC_except_table3362
- GCC_except_table3363
- GCC_except_table3364
- GCC_except_table3365
- GCC_except_table3366
- GCC_except_table3367
- GCC_except_table3368
- GCC_except_table3369
- GCC_except_table3370
- GCC_except_table3371
- GCC_except_table3372
- GCC_except_table3373
- GCC_except_table3374
- GCC_except_table3376
- GCC_except_table3378
- GCC_except_table3380
- GCC_except_table3383
- GCC_except_table3385
- GCC_except_table3386
- GCC_except_table3388
- GCC_except_table3389
- GCC_except_table339
- GCC_except_table3390
- GCC_except_table3391
- GCC_except_table3392
- GCC_except_table3394
- GCC_except_table3395
- GCC_except_table3396
- GCC_except_table3397
- GCC_except_table3399
- GCC_except_table340
- GCC_except_table3400
- GCC_except_table3402
- GCC_except_table3403
- GCC_except_table3405
- GCC_except_table3406
- GCC_except_table3407
- GCC_except_table3408
- GCC_except_table3409
- GCC_except_table3412
- GCC_except_table3413
- GCC_except_table3416
- GCC_except_table3417
- GCC_except_table3419
- GCC_except_table3421
- GCC_except_table3422
- GCC_except_table3424
- GCC_except_table3425
- GCC_except_table3438
- GCC_except_table3441
- GCC_except_table3443
- GCC_except_table3444
- GCC_except_table3445
- GCC_except_table3446
- GCC_except_table3447
- GCC_except_table3448
- GCC_except_table3449
- GCC_except_table3451
- GCC_except_table3453
- GCC_except_table3454
- GCC_except_table3455
- GCC_except_table3457
- GCC_except_table3458
- GCC_except_table3459
- GCC_except_table3460
- GCC_except_table3503
- GCC_except_table3509
- GCC_except_table352
- GCC_except_table3520
- GCC_except_table3548
- GCC_except_table3559
- GCC_except_table390
- GCC_except_table409
- GCC_except_table424
- GCC_except_table442
- GCC_except_table443
- GCC_except_table455
- GCC_except_table457
- GCC_except_table459
- GCC_except_table461
- GCC_except_table480
- GCC_except_table495
- GCC_except_table496
- GCC_except_table518
- GCC_except_table522
- GCC_except_table532
- GCC_except_table536
- GCC_except_table545
- GCC_except_table546
- GCC_except_table547
- GCC_except_table567
- GCC_except_table568
- GCC_except_table576
- GCC_except_table580
- GCC_except_table585
- GCC_except_table587
- GCC_except_table593
- GCC_except_table597
- GCC_except_table599
- GCC_except_table604
- GCC_except_table608
- GCC_except_table610
- GCC_except_table612
- GCC_except_table637
- GCC_except_table642
- GCC_except_table643
- GCC_except_table644
- GCC_except_table651
- GCC_except_table658
- GCC_except_table660
- GCC_except_table662
- GCC_except_table669
- GCC_except_table684
- GCC_except_table688
- GCC_except_table689
- GCC_except_table693
- GCC_except_table731
- GCC_except_table732
- GCC_except_table733
- GCC_except_table738
- GCC_except_table747
- GCC_except_table753
- GCC_except_table754
- GCC_except_table769
- GCC_except_table775
- GCC_except_table776
- GCC_except_table780
- GCC_except_table789
- GCC_except_table790
- GCC_except_table791
- GCC_except_table799
- GCC_except_table812
- GCC_except_table813
- GCC_except_table820
- GCC_except_table821
- GCC_except_table822
- GCC_except_table829
- GCC_except_table830
- GCC_except_table831
- GCC_except_table839
- GCC_except_table840
- GCC_except_table846
- GCC_except_table848
- GCC_except_table860
- GCC_except_table864
- GCC_except_table868
- GCC_except_table869
- GCC_except_table870
- GCC_except_table876
- GCC_except_table877
- GCC_except_table885
- GCC_except_table887
- GCC_except_table891
- GCC_except_table893
- GCC_except_table898
- GCC_except_table903
- GCC_except_table905
- GCC_except_table907
- GCC_except_table909
- GCC_except_table917
- GCC_except_table923
- GCC_except_table924
- GCC_except_table925
- GCC_except_table942
- GCC_except_table961
- GCC_except_table967
- GCC_except_table968
- GCC_except_table975
- GCC_except_table979
- GCC_except_table988
- GCC_except_table998
- _AVAudioSessionModeSpatialCapture
- _AVVoiceControllerHACRoute
- __Z45extractFirstInputPortTypeFromRouteDescriptionP30AVAudioSessionRouteDescriptionPU8__strongP8NSString
- __ZN11ElapsedTimeC2EPKcS1_
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
- __ZNKSt3__16vectorI12WorkloopInfoNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorI23EExtAudioGraphNodeStateNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorI30AVAEStreamFormatObserverStructNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIN17AUInterfaceBaseV314RenderObserverENS_9allocatorIS2_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorINS_10unique_ptrIN5caulk17semaphore_mutex_tINS2_9semaphoreEEENS_14default_deleteIS5_EEEENS_9allocatorIS8_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIP11AVAudioNodeNS_9allocatorIS2_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIP17AUGraphNodeBaseV3NS_9allocatorIS2_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIP17AUGraphNodeBaseV3NS_9allocatorIS2_EEE20__throw_out_of_rangeB7v160006Ev
- __ZNKSt3__16vectorIP19AVAudioNodeImplBaseNS_9allocatorIS2_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIP22CompletionHandlerTimerNS_9allocatorIS2_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIP8NSNumberNS_9allocatorIS2_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIbNS_9allocatorIbEEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_out_of_rangeB7v160006Ev
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt12out_of_rangeC1B7v160006EPKc
- __ZNSt3__110__function12__value_funcIF16ETraversalStatusR17AUGraphNodeBaseV3P17AUGraphConnectionEED2B7v160006Ev
- __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrI19AVVCRecordingEngineEEEEC2B7v160006ERKS6_
- __ZNSt3__110__function12__value_funcIFvNS_10shared_ptrI19AVVCRecordingEngineEEEED2B7v160006Ev
- __ZNSt3__110__function12__value_funcIFvbEE4swapB7v160006ERS3_
- __ZNSt3__110__function12__value_funcIFvbEEC2B7v160006ERKS3_
- __ZNSt3__110__function12__value_funcIFvbEED2B7v160006Ev
- __ZNSt3__110shared_ptrI14ControllerImplEC2B7v160006IS1_vEERKNS_8weak_ptrIT_EE
- __ZNSt3__110shared_ptrI19AVVCRecordingEngineEC2B7v160006IS1_vEERKNS_8weak_ptrIT_EE
- __ZNSt3__110unique_ptrI18AVAudioEngineGraphNS_14default_deleteIS1_EEE5resetB7v160006EPS1_
- __ZNSt3__110unique_ptrI21AVAEGraphStateTrackerNS_14default_deleteIS1_EEE5resetB7v160006EPS1_
- __ZNSt3__110unique_ptrI22AVAEDispatchQueueTimerNS_14default_deleteIS1_EEE5resetB7v160006EPS1_
- __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerF34AVAudioEngineManualRenderingStatusjP15AudioBufferListPiEENS_14default_deleteIS8_EEE5resetB7v160006EPS8_
- __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFPK15AudioBufferListjEENS_14default_deleteIS7_EEE5resetB7v160006EPS7_
- __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFiPjPK14AudioTimeStampjlP15AudioBufferListEENS_14default_deleteISA_EEE5resetB7v160006EPSA_
- __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFiPjPK14AudioTimeStampjlP15AudioBufferListU13block_pointerFiS2_S5_jlS7_EEENS_14default_deleteISC_EEE5resetB7v160006EPSC_
- __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFixhPK13MIDIEventListEENS_14default_deleteIS7_EEE5resetB7v160006EPS7_
- __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFixhlPKhEENS_14default_deleteIS6_EEE5resetB7v160006EPS6_
- __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFv39AVAudioPlayerNodeCompletionCallbackTypeEENS_14default_deleteIS5_EEE5resetB7v160006EPS5_
- __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFvPjPK14AudioTimeStampjlEENS_14default_deleteIS8_EEE5resetB7v160006EPS8_
- __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFvjPK14AudioTimeStampjlEENS_14default_deleteIS7_EEE5resetB7v160006EPS7_
- __ZNSt3__110unique_ptrI9AVAEBlockIU13block_pointerFvxhlPKhEENS_14default_deleteIS6_EEE5resetB7v160006EPS6_
- __ZNSt3__110unique_ptrIN4MIDI16LegacyPacketListENS1_23LegacyPacketListDeleterEE5resetB7v160006EPS2_
- __ZNSt3__110unique_ptrIN5caulk17semaphore_mutex_tINS1_9semaphoreEEENS_14default_deleteIS4_EEE5resetB7v160006EPS4_
- __ZNSt3__110unique_ptrINS_3mapINS_4pairIP11AVAudioNodejEEP24AVAudioMixingDestinationNS_4lessIS5_EENS_9allocatorINS2_IKS5_S7_EEEEEENS_14default_deleteISE_EEE5resetB7v160006EPSE_
- __ZNSt3__110unique_ptrIZN20AVAudioSequencerImpl4StopEvE3$_1NS_14default_deleteIS2_EEED1B7v160006Ev
- __ZNSt3__110unique_ptrIZN20AVAudioSequencerImplD1EvE3$_0NS_14default_deleteIS2_EEED1B7v160006Ev
- __ZNSt3__111unique_lockIN5caulk17semaphore_mutex_tINS1_9semaphoreEEEED2B7v160006Ev
- __ZNSt3__111unique_lockIN5caulk27recursive_semaphore_mutex_tINS1_9semaphoreEEEED2B7v160006Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B7v160006Emc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B7v160006IDnEEPKc
- __ZNSt3__113__tree_removeB7v160006IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__116__pad_and_outputB7v160006IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB7v160006IONS1_9__variant15__value_visitorIZN17AUGraphNodeBaseV320CreateMIDIConnectionERK21AUGraphMIDIConnectionE3$_1EEJRKNS0_6__baseILNS0_6_TraitE0EJU13block_pointerFixhlPKhEU13block_pointerFixhPK13MIDIEventListEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB7v160006IONS1_9__variant15__value_visitorIZN17AUGraphNodeBaseV320CreateMIDIConnectionERK21AUGraphMIDIConnectionE3$_1EEJRKNS0_6__baseILNS0_6_TraitE0EJU13block_pointerFixhlPKhEU13block_pointerFixhPK13MIDIEventListEEEEEEEDcT_DpT0_
- __ZNSt3__117__call_once_proxyB7v160006INS_5tupleIJOZN12CADeprecated10TSingletonINS2_19RealtimeDeallocatorEE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B7v160006Ev
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorI23EExtAudioGraphNodeStateEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIP17AUGraphNodeBaseV3EEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIP8NSNumberEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__shared_weak_count16__release_sharedB7v160006Ev
- __ZNSt3__120__throw_bad_weak_ptrB7v160006Ev
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__120__throw_out_of_rangeB7v160006EPKc
- __ZNSt3__124__put_character_sequenceB7v160006IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__125__throw_bad_function_callB7v160006Ev
- __ZNSt3__126__throw_bad_variant_accessB7v160006Ev
- __ZNSt3__127__tree_balance_after_insertB7v160006IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__14lockB7v160006IN5caulk17semaphore_mutex_tINS1_9semaphoreEEES4_EEvRT_RT0_
- __ZNSt3__14lockB7v160006INS_15recursive_mutexEN5caulk27recursive_semaphore_mutex_tINS2_9semaphoreEEEEEvRT_RT0_
- __ZNSt3__16vectorIN17AUInterfaceBaseV314RenderObserverENS_9allocatorIS2_EEED2B7v160006Ev
- __ZNSt3__16vectorINS_10unique_ptrIN5caulk17semaphore_mutex_tINS2_9semaphoreEEENS_14default_deleteIS5_EEEENS_9allocatorIS8_EEED2B7v160006Ev
- __ZNSt3__16vectorIP17AUGraphNodeBaseV3NS_9allocatorIS2_EEE6assignIPS2_Li0EEEvT_S8_
- __ZNSt3__16vectorIP17AUGraphNodeBaseV3NS_9allocatorIS2_EEE9push_backB7v160006ERKS2_
- __ZNSt3__16vectorIcNS_9allocatorIcEEE11__vallocateB7v160006Em
- __ZNSt3__16vectorIjNS_9allocatorIjEEEC1B7v160006ESt16initializer_listIjE
- __ZNSt3__18optionalIN2CA10BufferListEEaSB7v160006IS2_vEERS3_OT_
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___52-[AVVoiceTriggerClient voiceTriggerServerConnection]_block_invoke.174
- ___52-[AVVoiceTriggerClient voiceTriggerServerConnection]_block_invoke.178
- ___54-[AVVoiceTriggerClient getInputChannelInfoCompletion:]_block_invoke.186
- ___55-[AVVoiceTriggerClient portStateActiveCompletionBlock:]_block_invoke.218
- ___56-[AVVoiceTriggerClient listeningEnabledCompletionBlock:]_block_invoke.226
- ___57-[AVVoiceTriggerClient speakerStateMutedCompletionBlock:]_block_invoke.212
- ___58-[AVVoiceTriggerClient enableBargeInMode:completionBlock:]_block_invoke.220
- ___58-[AVVoiceTriggerClient speakerStateActiveCompletionBlock:]_block_invoke.208
- ___59-[AVVoiceTriggerClient voiceTriggerPastDataFramesAvailable]_block_invoke.192
- ___60-[AVVoiceTriggerClient setAggressiveECMode:completionBlock:]_block_invoke.231
- ___60-[AVVoiceTriggerClient siriClientsRecordingCompletionBlock:]_block_invoke.228
- ___63-[AVVoiceTriggerClient enableListeningOnPorts:completionBlock:]_block_invoke.215
- ___68-[AVVoiceTriggerClient enableSpeakerStateListening:completionBlock:]_block_invoke.204
- ___68-[AVVoiceTriggerClient enableVoiceTriggerListening:completionBlock:]_block_invoke.199
- ___70-[AVVoiceTriggerClient voiceTriggerPastDataFramesAvailableCompletion:]_block_invoke.183
- ___72-[AVVoiceTriggerClient updateVoiceTriggerConfiguration:completionBlock:]_block_invoke.223
- ___Block_byref_object_copy_.1212
- ___Block_byref_object_copy_.145
- ___Block_byref_object_copy_.5084
- ___Block_byref_object_copy_.5789
- ___Block_byref_object_copy_.6643
- ___Block_byref_object_copy_.683
- ___Block_byref_object_copy_.8073
- ___Block_byref_object_dispose_.1213
- ___Block_byref_object_dispose_.146
- ___Block_byref_object_dispose_.5085
- ___Block_byref_object_dispose_.5790
- ___Block_byref_object_dispose_.6644
- ___Block_byref_object_dispose_.684
- ___Block_byref_object_dispose_.8074
- ____ZN14ControllerImpl10setContextEP17AVVoiceControllerP19AVVCContextSettingsU13block_pointerFvm14AVVCStreamTypeP7NSErrorE_block_invoke_2.263
- ____ZN17AVAudioEngineImpl26IOUnitConfigurationChangedEv_block_invoke.162
- ___block_descriptor_48_ea8_32c44_ZTSNSt3__18weak_ptrI19AVVCRecordingEngineEE_e56_v32?0"AVAudioBuffer"8"AVAudioTime"16"NSDictionary"24l
- ___block_descriptor_tmp.1159
- ___block_descriptor_tmp.1416
- ___block_descriptor_tmp.1424
- ___block_descriptor_tmp.5525
- ___block_descriptor_tmp.5571
- ___block_literal_global.1339
- ___block_literal_global.142
- ___block_literal_global.1687
- ___block_literal_global.177
- ___block_literal_global.180
- ___block_literal_global.191
- ___block_literal_global.195
- ___block_literal_global.2046
- ___block_literal_global.209
- ___block_literal_global.2400
- ___block_literal_global.3009
- ___block_literal_global.38.2076
- ___block_literal_global.4543
- ___block_literal_global.5124
- ___block_literal_global.5488
- ___block_literal_global.5553
- ___block_literal_global.5569
- ___block_literal_global.5923
- ___block_literal_global.6645
- ___block_literal_global.7370
- ___block_literal_global.760
- ___block_literal_global.7757
- ___block_literal_global.7949
- _objc_msgSend$getSiriInputSource:withIdentifier:
CStrings:
+ "%25s:%-5d AVVCPluginRecordingEngine::destroyRecordEngine: Calling doneRecording explicitly"
+ "%25s:%-5d Audio session has changed, setting active."
+ "%25s:%-5d AudioUnitSetProperty kAudioUnitProperty_MatrixLevels %i"
+ "%25s:%-5d Bluetooth setting: %d, Output route: %d"
+ "%25s:%-5d Cannot perform tone playback without setting all required parameters (frequency, soundLevel, and duration)"
+ "%25s:%-5d Cannot request speaker output on Bluetooth route"
+ "%25s:%-5d Cannot set playback URL and tone on the same sequence"
+ "%25s:%-5d Current volume is not as expected, updating volume. { current=%f, expected=%f, name=%@ }"
+ "%25s:%-5d Exception caught while trying to set input client format: %s, reached maximum number of tries (%d), rethrowing..."
+ "%25s:%-5d Exception caught while trying to set input client format: %s, retrying (%d/%d)..."
+ "%25s:%-5d Failed to create input tap file %@"
+ "%25s:%-5d Failed to reset audio session %@"
+ "%25s:%-5d Failed to set audio session category. { error=%@ }"
+ "%25s:%-5d Failed to set audio session mode. { error=%@ }"
+ "%25s:%-5d Failed to subscribe to system volume notification. { error=%@ }"
+ "%25s:%-5d Failed to unsubscribe from AVSystemController volume notification. { error=%{public}@ }"
+ "%25s:%-5d Initializing AVAudioDeviceTest for in-process operation."
+ "%25s:%-5d Initializing AVAudioDeviceTest for out-of-process operation."
+ "%25s:%-5d Interruption detected, resetting observers."
+ "%25s:%-5d Invalid mic channel name. { providedName=%{public}@ }"
+ "%25s:%-5d Invalid setup, cannot provide multichannel playback file without specifying mic channel."
+ "%25s:%-5d Multichannel file provided, will split into single channel buffers. { requestedMic=%{public}@ }"
+ "%25s:%-5d Output route is not a bluetooth speaker"
+ "%25s:%-5d Playing tone above amplitude of 1.0. { amplitude=%f }"
+ "%25s:%-5d Pulse tone handler is nil or does not match this tone sequence."
+ "%25s:%-5d Setting up observers"
+ "%25s:%-5d Started recording on server side %@"
+ "%25s:%-5d Stopped recording on server side %@ (%f s)"
+ "%25s:%-5d Unable to set session on engine"
+ "%25s:%-5d Updating current audio session category to playback only."
+ "%25s:%-5d Volume not as expected, updating volume. { current=%f, expected=%f }"
+ "%25s:%-5d calling mStopRecordCompletionBlock(%p)"
+ "%25s:%-5d cleaning up observers"
+ "%25s:%-5d cleaning up observers and invalidating process assertion"
+ "%25s:%-5d collecting input tap data %@"
+ "%25s:%-5d configuring sequence"
+ "%25s:%-5d couldn't release extension %i"
+ "%25s:%-5d db %f"
+ "%25s:%-5d doneRecording: calling mStartRecordCompletionBlock(%p) (notify start before stop). Error: %@"
+ "%25s:%-5d entering sequence"
+ "%25s:%-5d error code %li"
+ "%25s:%-5d error converting stimulus buffer format %@ - %li"
+ "%25s:%-5d error reading stimulus file into buffer %@"
+ "%25s:%-5d error setInterruptionPriority %li"
+ "%25s:%-5d error writing debug file %@"
+ "%25s:%-5d exception (%@) with test error (%li)"
+ "%25s:%-5d extension token is null"
+ "%25s:%-5d failed to consume extension: %i"
+ "%25s:%-5d failed to read in from buffer - test error %li"
+ "%25s:%-5d getDeviceUIDForHomeOrBluetoothButtonActivation: Context is ambiguous"
+ "%25s:%-5d getDeviceUIDForHomeOrBluetoothButtonActivation: Context is not ambiguous"
+ "%25s:%-5d getDeviceUIDForHomeOrBluetoothButtonActivation: siriInputSource(%@), siriRemoteInputIdentifier(%@), isMicrophoneBuiltIn(%d)"
+ "%25s:%-5d interruption (%@) with test error (%li)"
+ "%25s:%-5d interruption (%@) with test error (%li) - %@"
+ "%25s:%-5d invalid stimulus buffer format %li"
+ "%25s:%-5d mediaserverd died (%@) with test error (%li)"
+ "%25s:%-5d mediaserverd/audiomxd died (%@) with test error (%li)"
+ "%25s:%-5d mediaserverd/audiomxd was reset (%@) with test error (%li)"
+ "%25s:%-5d mixer dimension %d x %d"
+ "%25s:%-5d overrideOutputAudioPort %li"
+ "%25s:%-5d player finished"
+ "%25s:%-5d preparing for test"
+ "%25s:%-5d processing xcorr"
+ "%25s:%-5d route change (%@)"
+ "%25s:%-5d route change (%@) - %@"
+ "%25s:%-5d running test on platform with inadequate hardware"
+ "%25s:%-5d scheduling stimulus file"
+ "%25s:%-5d sequence completed"
+ "%25s:%-5d sequence finished"
+ "%25s:%-5d setActive (%li) with test error (%li)"
+ "%25s:%-5d setCategory %li"
+ "%25s:%-5d setContext: Selected engine (%s) for activation mode (%@) with announceCallsEnabled(%d)"
+ "%25s:%-5d setContext:getEngineTypeAndDeviceIDToUse: AQ engine selected"
+ "%25s:%-5d setContext:getEngineTypeAndDeviceIDToUse: ActivationMode (%@) requested with deviceUUID (%@). Selected EngineType (%s)"
+ "%25s:%-5d setMode (%li) with test error (%li)"
+ "%25s:%-5d setPreferredDataSource %li"
+ "%25s:%-5d setPreferredIOBufferFrameSize (%li) with test error (%li)"
+ "%25s:%-5d setPreferredInput %li"
+ "%25s:%-5d setting up observers"
+ "%25s:%-5d setting volume %.2f for AS category %@, AVS category %@"
+ "%25s:%-5d setting volume to %.2f"
+ "%25s:%-5d sharedInstance setActive %li"
+ "%25s:%-5d startAndReturnError (%@) with test error (%li)"
+ "%25s:%-5d starting sequence"
+ "%25s:%-5d test length %i frames"
+ "%25s:%-5d the length of the captured buffer needs to be greater (%li)"
+ "%25s:%-5d the source file or captured buffers aren't signal channel files (%li)"
+ "%25s:%-5d unable to read stimulus file (%@) with test error (%li)"
+ "%25s:%-5d unable to set volume %.2f (%li)"
+ "%25s:%-5d unable to set volume %.2f for category %@ - (%li)"
+ "%25s:%-5d using data source %@"
+ "%25s:%-5d using port %@"
+ "%25s:%-5d waiting for sequence to finish"
+ ", rethrow after %d tries"
+ "-\x14"
+ "-[AVAudioDeviceTestService playbackTone:completion:]_block_invoke_3"
+ "/tmp/multichannel_mixer_out.caf"
+ "@\"AVAudioBuffer\"20@?0I8^q12"
+ "@\"AVAudioDeviceTestService\""
+ "@\"AVAudioEngine\""
+ "@\"AVAudioFile\""
+ "@\"AVAudioPlayerNode\""
+ "@\"AVAudioSourceNode\""
+ "@\"AVAudioUnit\""
+ "@\"AVAudioUnitEQ\""
+ "@\"NSObject<OS_os_transaction>\""
+ "@20@0:8B16"
+ "AVAudioDeviceTestService"
+ "AVAudioDeviceTestService.mm"
+ "AVAudioDeviceTestServiceDelegate"
+ "App Was Suspended"
+ "Audio/Video"
+ "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
+ "B32@0:8@16@24"
+ "B48@0:8^Q16^@24^B32q40"
+ "Back"
+ "Built-In Mic Muted"
+ "Category Change"
+ "Default"
+ "Front"
+ "HeadphonesBT"
+ "LeftBottom"
+ "MSNMonitorBeginException"
+ "MSNMonitorEndException"
+ "NSXPCListenerDelegate"
+ "New Device Available"
+ "No Suitable Route for Category"
+ "Old Device Unavailable"
+ "PlayAndRecord"
+ "PulseTone.mm"
+ "RightBottom"
+ "Route Configuration Change"
+ "T@\"AVAudioDeviceTestService\",&,N,V_service"
+ "T@\"AVAudioEngine\",&,V_engine"
+ "T@\"AVAudioFile\",&,V_inputTapFile"
+ "T@\"AVAudioNode\",&,V_nodeToCaptureData"
+ "T@\"AVAudioPlayerNode\",&,V_player"
+ "T@\"AVAudioSession\",&,V_currentSession"
+ "T@\"AVAudioSourceNode\",&,N,V_sourceNode"
+ "T@\"AVAudioUnit\",&,V_multichannelMixer"
+ "T@\"AVAudioUnitEQ\",&,V_inputFilter"
+ "T@\"AVAudioUnitEQ\",&,V_outputFilter"
+ "T@\"NSNumber\",&,N,V_userVolumeBeforeHearingTest"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_toneQueue"
+ "T@\"NSObject<OS_os_transaction>\",&,N,V_transaction"
+ "T@\"NSString\",?,R,C"
+ "T@,&,V_interruptionObserver"
+ "T@,&,V_mediaservicesLostObserver"
+ "T@,&,V_mediaservicesResetObserver"
+ "T@,&,V_routeChangeObserver"
+ "T@,&,V_systemVolumeObserver"
+ "TB,V_testServiceSupportedOnHardware"
+ "Tq,V_extensionHandle"
+ "Wake From Sleep"
+ "_currentSession"
+ "_engine"
+ "_extensionHandle"
+ "_inputFilter"
+ "_inputTapFile"
+ "_interruptionObserver"
+ "_mediaservicesLostObserver"
+ "_mediaservicesResetObserver"
+ "_multichannelMixer"
+ "_nodeToCaptureData"
+ "_outputFilter"
+ "_player"
+ "_routeChangeObserver"
+ "_service"
+ "_sourceNode"
+ "_systemVolumeObserver"
+ "_testServiceSupportedOnHardware"
+ "_toneQueue"
+ "_transaction"
+ "_userVolumeBeforeHearingTest"
+ "allowAllBuiltInDataSources"
+ "appendString:"
+ "asts"
+ "atpt"
+ "audiotesting"
+ "availableInputs"
+ "calculateCrossCorrelationPeakRelativeToSource:capture:"
+ "categoryOptions"
+ "checkSequenceValidity:completion:"
+ "cleanUp"
+ "cleanUpObservers"
+ "com.apple.avaudiodevietestservice.tones"
+ "com.apple.avfaudio.devicetest"
+ "com.apple.avfaudio.xcorr_queue"
+ "com.apple.coreaudio.avaudiodevicetest"
+ "configureDataSources:session:"
+ "configureMultiChannelMixerForOutputChannel:totalChannels:"
+ "convertBufferFor:sourceBuffer:"
+ "createAudioEngineAndProcessingChain:session:sourceNodeBlock:"
+ "createAudioEngineAndPulseToneHandlerFor:"
+ "currentSession"
+ "d32@0:8@16@24"
+ "dataSourceID"
+ "dataSources"
+ "didWrite"
+ "err == nil"
+ "extensionHandle"
+ "getActiveCategoryVolume:andName:"
+ "getSiriInputSource:withIdentifier:withIsMicrophoneCheck:forActivationMode:"
+ "i36@?0^B8r^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}16I24^{AudioBufferList=I[1{AudioBuffer=II^v}]}28"
+ "initInProcess:"
+ "initWithFloat:"
+ "input format doesn't contain 1 channel"
+ "inputFilter"
+ "inputTapFile"
+ "interruptionObserver"
+ "isActive"
+ "isMixerOutputEnabled"
+ "isOutputRouteBluetooth:session:"
+ "listener:shouldAcceptNewConnection:"
+ "mPulseToneHandler"
+ "mediaservicesLostObserver"
+ "mediaservicesResetObserver"
+ "mixer_output_enable"
+ "multichannelMixer"
+ "nodeToCaptureData"
+ "outputFilter"
+ "outputSampleRate"
+ "overrideOutputAudioPort:error:"
+ "player"
+ "preferredIOBufferFrameSize"
+ "resetVolume:"
+ "routeChangeObserver"
+ "routeForCategory:"
+ "service"
+ "setActiveCategoryVolumeTo:"
+ "setAllowAllBuiltInDataSources:"
+ "setAttribute:forKey:error:"
+ "setCategory:error:"
+ "setCurrentSession:"
+ "setEngine:"
+ "setExtensionHandle:"
+ "setInputFilter:"
+ "setInputTapFile:"
+ "setInterruptionObserver:"
+ "setInterruptionPriority:error:"
+ "setMediaservicesLostObserver:"
+ "setMediaservicesResetObserver:"
+ "setMode:error:"
+ "setMultichannelMixer:"
+ "setNodeToCaptureData:"
+ "setObject:atIndexedSubscript:"
+ "setOutputFilter:"
+ "setPlayer:"
+ "setPreferredDataSource:error:"
+ "setPreferredInput:error:"
+ "setRouteChangeObserver:"
+ "setService:"
+ "setSourceNode:"
+ "setSystemVolumeObserver:"
+ "setTestServiceSupportedOnHardware:"
+ "setToneQueue:"
+ "setTransaction:"
+ "setUserVolumeBeforeHearingTest:"
+ "setVolume:session:"
+ "setVolumeTo:forCategory:"
+ "setupAudioEngineFor:sourceNodeBlock:"
+ "setupAudioSessionFor:playbackOnly:completion:"
+ "setupMultiChannelMixerForOutputChannel:completion:"
+ "setupObservers:"
+ "setupVolumeObserverForVolume:completion:"
+ "sleepForTimeInterval:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/MediaSafetyNet.framework/MediaSafetyNet"
+ "sourceNode"
+ "stringForInterruptionReason:"
+ "stringForRouteChangeReason:"
+ "systemVolumeObserver"
+ "testServiceSupportedOnHardware"
+ "the desired channel must not be greater than the number of channels"
+ "toneQueue"
+ "transaction"
+ "userVolumeBeforeHearingTest"
+ "v24@?0@\"AVAudioPCMBuffer\"8@\"AVAudioTime\"16"
+ "v24@?0@\"AVAudioUnit\"8@\"NSError\"16"
+ "v28@0:8f16@?20"
+ "v32@0:8q16q24"
+ "v36@0:8@16B24@?28"
+ "valueForEntitlement:"
+ "void *MediaSafetyNetLibrary()"
+ "void MSNMonitorBeginException_soft(const char *)"
+ "void MSNMonitorEndException_soft(const char *)"
+ "{unique_ptr<PulseTone, std::default_delete<PulseTone>>=\"__ptr_\"{__compressed_pair<PulseTone *, std::default_delete<PulseTone>>=\"__value_\"^{PulseTone}}}"
- "%25s:%-5d AVVCPluginRecordingEngine::destroyRecordEngine:  calling doneRecording manually"
- "%25s:%-5d doneRecording: calling startRecordCompletionBlock(%p) (notify start before stop). Error: %@"
- "%25s:%-5d getDeviceUIDForHomeOrBluetoothButtonActivation : siriInputSource(%@), siriRemoteID(%@)"
- "%25s:%-5d setContext:getEngineTypeAndDeviceIDToUse: Ambigous activation (%@) requested with deviceUUID - %@. EngineType : %d"
- "B32@0:8^Q16^@24"
- "HACBuiltIn"
- "getSiriInputSource:withIdentifier:"

```
