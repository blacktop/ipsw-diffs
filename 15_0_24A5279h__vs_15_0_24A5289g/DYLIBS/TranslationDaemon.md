## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/Versions/A/TranslationDaemon`

```diff

-284.0.0.0.0
-  __TEXT.__text: 0x1a0b94
-  __TEXT.__auth_stubs: 0xae0
-  __TEXT.__objc_methlist: 0x18f5c
-  __TEXT.__const: 0x390
-  __TEXT.__gcc_except_tab: 0x1b994
-  __TEXT.__cstring: 0x539e
-  __TEXT.__oslogstring: 0xa03d
+286.1.0.0.0
+  __TEXT.__text: 0x197e68
+  __TEXT.__auth_stubs: 0xaf0
+  __TEXT.__objc_methlist: 0x1837c
+  __TEXT.__const: 0x380
+  __TEXT.__gcc_except_tab: 0x1addc
+  __TEXT.__cstring: 0x5397
+  __TEXT.__oslogstring: 0x9fac
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0xf800
-  __TEXT.__objc_classname: 0x4950
-  __TEXT.__objc_methname: 0x19b7b
-  __TEXT.__objc_methtype: 0xe486
-  __TEXT.__objc_stubs: 0x11340
-  __DATA_CONST.__got: 0xc58
-  __DATA_CONST.__const: 0x1440
-  __DATA_CONST.__objc_classlist: 0x1208
+  __TEXT.__unwind_info: 0xf0d0
+  __TEXT.__objc_classname: 0x468f
+  __TEXT.__objc_methname: 0x195d1
+  __TEXT.__objc_methtype: 0xdceb
+  __TEXT.__objc_stubs: 0x112a0
+  __DATA_CONST.__got: 0xc08
+  __DATA_CONST.__const: 0x13f8
+  __DATA_CONST.__objc_classlist: 0x1168
   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x60d8
-  __DATA_CONST.__objc_superrefs: 0x1188
+  __DATA_CONST.__objc_selrefs: 0x6058
+  __DATA_CONST.__objc_superrefs: 0x10e8
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x588
+  __AUTH_CONST.__auth_got: 0x590
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x3230
-  __AUTH_CONST.__cfstring: 0x6d20
-  __AUTH_CONST.__objc_const: 0x2dac0
+  __AUTH_CONST.__const: 0x3270
+  __AUTH_CONST.__cfstring: 0x6d60
+  __AUTH_CONST.__objc_const: 0x2c558
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xb450
-  __DATA.__objc_ivar: 0x114c
+  __AUTH.__objc_data: 0xae10
+  __DATA.__objc_ivar: 0x10cc
   __DATA.__data: 0xa08
-  __DATA.__bss: 0x238
+  __DATA.__bss: 0x248
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9942
-  Symbols:   22993
+  Functions: 9698
+  Symbols:   22440
   CStrings:  1023
 
Symbols:
+ +[MTSchemaMTInvocationStarted(LTTranslationAdditions) lt_initWithTask:inputMode:invocationType:explicitLanguageFilterEnabled:onDevice:translateAppContext:]
+ +[_LTDAssetService assetsForLocales:includeTTS:completion:]
+ +[_LTDAssetService assetsForLocales:includeTTS:error:]
+ +[_LTDAssetService assetsForLocales:includeTTS:error:].cold.1
+ +[_LTDLanguageAssetService _languageModelsForLocales:initialState:error:]
+ +[_LTDLanguageAssetService _supportedLocalesWithError:]
+ +[_LTDLanguageAssetService _supportedLocalesWithError:].cold.1
+ +[_LTDLanguageAssetService addLanguages:useCellular:]
+ +[_LTDLanguageAssetService addLanguages:useCellular:].cold.1
+ +[_LTDLanguageAssetService removeLanguages:]
+ +[_LTDLanguageAssetService removeLanguages:].cold.1
+ +[_LTDLanguageAssetService syncInstalledLocales]
+ +[_LTDSELFLoggingProduction startWithTask:inputMode:invocationType:interfaceMode:explicitLanguageFilterEnabled:onDevice:mtId:sessionId:translateAppContext:]
+ -[FTBatchTranslationCacheContainer contains_masked_profanity]
+ -[FTBatchTranslationResponse contains_masked_profanity]
+ -[FTBatchTranslationResponse_TranslatedSentence contains_masked_profanity]
+ -[FTBatchTranslationResponse_TranslationPhrase contains_masked_profanity]
+ -[FTMutableBatchTranslationCacheContainer contains_masked_profanity]
+ -[FTMutableBatchTranslationCacheContainer setContains_masked_profanity:]
+ -[FTMutableBatchTranslationResponse contains_masked_profanity]
+ -[FTMutableBatchTranslationResponse setContains_masked_profanity:]
+ -[FTMutableBatchTranslationResponse_TranslatedSentence contains_masked_profanity]
+ -[FTMutableBatchTranslationResponse_TranslatedSentence setContains_masked_profanity:]
+ -[FTMutableBatchTranslationResponse_TranslationPhrase contains_masked_profanity]
+ -[FTMutableBatchTranslationResponse_TranslationPhrase setContains_masked_profanity:]
+ -[FTMutableSpeechTranslationMtResponse contains_masked_profanity]
+ -[FTMutableSpeechTranslationMtResponse setContains_masked_profanity:]
+ -[FTMutableSpeechTranslationMtResponse_TranslationPhrase contains_masked_profanity]
+ -[FTMutableSpeechTranslationMtResponse_TranslationPhrase setContains_masked_profanity:]
+ -[FTMutableStartSpeechRequest self_session_id]
+ -[FTMutableStartSpeechRequest setSelf_session_id:]
+ -[FTMutableTextToSpeechResponseDevData engine_error_code]
+ -[FTMutableTextToSpeechResponseDevData engine_error_message]
+ -[FTMutableTextToSpeechResponseDevData setEngine_error_code:]
+ -[FTMutableTextToSpeechResponseDevData setEngine_error_message:]
+ -[FTMutableTranslationOptions disable_payload_logging]
+ -[FTMutableTranslationOptions mask_profanity]
+ -[FTMutableTranslationOptions setDisable_payload_logging:]
+ -[FTMutableTranslationOptions setMask_profanity:]
+ -[FTSpeechTranslationMtResponse contains_masked_profanity]
+ -[FTSpeechTranslationMtResponse_TranslationPhrase contains_masked_profanity]
+ -[FTStartSpeechRequest self_session_id]
+ -[FTTextToSpeechResponseDevData engine_error_code]
+ -[FTTextToSpeechResponseDevData engine_error_message]
+ -[FTTranslationOptions disable_payload_logging]
+ -[FTTranslationOptions mask_profanity]
+ -[_LTClientConnection addLanguages:useCellular:]
+ -[_LTClientConnection removeLanguages:]
+ -[_LTDConfigurationCache setObject:forType:]
+ -[_LTDConfigurationCache setObject:forType:].cold.1
+ GCC_except_table1013
+ GCC_except_table1029
+ GCC_except_table1035
+ GCC_except_table1049
+ GCC_except_table1051
+ GCC_except_table1051
+ GCC_except_table1057
+ GCC_except_table1073
+ GCC_except_table1087
+ GCC_except_table1089
+ GCC_except_table1093
+ GCC_except_table1099
+ GCC_except_table1105
+ GCC_except_table1107
+ GCC_except_table1107
+ GCC_except_table1129
+ GCC_except_table1133
+ GCC_except_table1135
+ GCC_except_table1147
+ GCC_except_table1163
+ GCC_except_table1175
+ GCC_except_table1181
+ GCC_except_table1181
+ GCC_except_table1189
+ GCC_except_table1193
+ GCC_except_table1193
+ GCC_except_table1197
+ GCC_except_table1199
+ GCC_except_table1204
+ GCC_except_table1206
+ GCC_except_table1210
+ GCC_except_table1210
+ GCC_except_table1220
+ GCC_except_table1220
+ GCC_except_table1222
+ GCC_except_table1234
+ GCC_except_table1234
+ GCC_except_table1239
+ GCC_except_table1253
+ GCC_except_table1285
+ GCC_except_table1287
+ GCC_except_table1289
+ GCC_except_table1289
+ GCC_except_table1297
+ GCC_except_table1305
+ GCC_except_table1309
+ GCC_except_table1311
+ GCC_except_table1311
+ GCC_except_table1315
+ GCC_except_table1315
+ GCC_except_table1321
+ GCC_except_table1323
+ GCC_except_table1323
+ GCC_except_table1345
+ GCC_except_table1345
+ GCC_except_table1381
+ GCC_except_table1381
+ GCC_except_table1387
+ GCC_except_table1393
+ GCC_except_table1396
+ GCC_except_table1402
+ GCC_except_table1410
+ GCC_except_table1412
+ GCC_except_table1416
+ GCC_except_table1428
+ GCC_except_table1436
+ GCC_except_table1438
+ GCC_except_table1438
+ GCC_except_table1444
+ GCC_except_table1444
+ GCC_except_table1454
+ GCC_except_table1454
+ GCC_except_table1460
+ GCC_except_table1464
+ GCC_except_table1466
+ GCC_except_table1470
+ GCC_except_table1472
+ GCC_except_table1474
+ GCC_except_table1474
+ GCC_except_table1480
+ GCC_except_table1482
+ GCC_except_table1486
+ GCC_except_table1492
+ GCC_except_table1495
+ GCC_except_table1497
+ GCC_except_table1501
+ GCC_except_table1503
+ GCC_except_table1507
+ GCC_except_table1507
+ GCC_except_table1509
+ GCC_except_table1517
+ GCC_except_table1529
+ GCC_except_table1531
+ GCC_except_table1535
+ GCC_except_table1538
+ GCC_except_table1542
+ GCC_except_table1548
+ GCC_except_table1550
+ GCC_except_table1552
+ GCC_except_table1556
+ GCC_except_table1564
+ GCC_except_table1570
+ GCC_except_table1574
+ GCC_except_table1578
+ GCC_except_table1580
+ GCC_except_table1584
+ GCC_except_table1590
+ GCC_except_table1611
+ GCC_except_table1615
+ GCC_except_table1621
+ GCC_except_table1643
+ GCC_except_table1647
+ GCC_except_table1647
+ GCC_except_table1649
+ GCC_except_table1663
+ GCC_except_table1665
+ GCC_except_table1667
+ GCC_except_table1667
+ GCC_except_table1671
+ GCC_except_table1677
+ GCC_except_table1692
+ GCC_except_table1710
+ GCC_except_table1720
+ GCC_except_table1730
+ GCC_except_table1740
+ GCC_except_table1748
+ GCC_except_table1758
+ GCC_except_table1762
+ GCC_except_table1764
+ GCC_except_table1764
+ GCC_except_table1774
+ GCC_except_table1792
+ GCC_except_table1798
+ GCC_except_table1808
+ GCC_except_table1808
+ GCC_except_table1812
+ GCC_except_table1816
+ GCC_except_table1816
+ GCC_except_table1822
+ GCC_except_table1822
+ GCC_except_table1824
+ GCC_except_table1828
+ GCC_except_table1830
+ GCC_except_table1836
+ GCC_except_table1840
+ GCC_except_table1846
+ GCC_except_table1854
+ GCC_except_table1868
+ GCC_except_table1896
+ GCC_except_table1898
+ GCC_except_table1900
+ GCC_except_table1904
+ GCC_except_table1908
+ GCC_except_table1914
+ GCC_except_table1914
+ GCC_except_table1920
+ GCC_except_table1924
+ GCC_except_table1928
+ GCC_except_table1928
+ GCC_except_table1942
+ GCC_except_table1952
+ GCC_except_table1952
+ GCC_except_table1974
+ GCC_except_table1974
+ GCC_except_table1982
+ GCC_except_table1988
+ GCC_except_table1988
+ GCC_except_table1998
+ GCC_except_table2010
+ GCC_except_table2018
+ GCC_except_table2020
+ GCC_except_table2028
+ GCC_except_table2034
+ GCC_except_table2034
+ GCC_except_table2050
+ GCC_except_table2056
+ GCC_except_table2095
+ GCC_except_table2101
+ GCC_except_table2108
+ GCC_except_table2109
+ GCC_except_table2115
+ GCC_except_table2126
+ GCC_except_table2127
+ GCC_except_table2129
+ GCC_except_table2130
+ GCC_except_table2132
+ GCC_except_table2133
+ GCC_except_table2134
+ GCC_except_table2135
+ GCC_except_table2138
+ GCC_except_table2144
+ GCC_except_table2155
+ GCC_except_table2158
+ GCC_except_table2159
+ GCC_except_table2161
+ GCC_except_table2162
+ GCC_except_table2164
+ GCC_except_table2165
+ GCC_except_table2166
+ GCC_except_table2167
+ GCC_except_table2168
+ GCC_except_table2169
+ GCC_except_table2170
+ GCC_except_table2189
+ GCC_except_table2197
+ GCC_except_table2198
+ GCC_except_table2199
+ GCC_except_table2201
+ GCC_except_table2202
+ GCC_except_table2208
+ GCC_except_table222
+ GCC_except_table222
+ GCC_except_table2221
+ GCC_except_table2222
+ GCC_except_table2223
+ GCC_except_table2224
+ GCC_except_table2232
+ GCC_except_table2240
+ GCC_except_table2241
+ GCC_except_table2242
+ GCC_except_table2248
+ GCC_except_table2253
+ GCC_except_table2254
+ GCC_except_table2258
+ GCC_except_table2259
+ GCC_except_table2273
+ GCC_except_table2276
+ GCC_except_table2282
+ GCC_except_table2284
+ GCC_except_table2285
+ GCC_except_table2287
+ GCC_except_table2292
+ GCC_except_table2303
+ GCC_except_table2304
+ GCC_except_table2310
+ GCC_except_table2314
+ GCC_except_table2315
+ GCC_except_table2318
+ GCC_except_table2323
+ GCC_except_table2329
+ GCC_except_table2343
+ GCC_except_table2344
+ GCC_except_table2353
+ GCC_except_table2355
+ GCC_except_table2356
+ GCC_except_table2357
+ GCC_except_table2359
+ GCC_except_table2370
+ GCC_except_table2372
+ GCC_except_table2374
+ GCC_except_table2384
+ GCC_except_table2385
+ GCC_except_table2387
+ GCC_except_table2393
+ GCC_except_table2402
+ GCC_except_table2409
+ GCC_except_table2411
+ GCC_except_table2414
+ GCC_except_table2416
+ GCC_except_table2423
+ GCC_except_table2425
+ GCC_except_table2427
+ GCC_except_table2429
+ GCC_except_table2430
+ GCC_except_table2438
+ GCC_except_table2442
+ GCC_except_table2443
+ GCC_except_table2444
+ GCC_except_table2445
+ GCC_except_table2447
+ GCC_except_table2448
+ GCC_except_table2449
+ GCC_except_table2453
+ GCC_except_table2470
+ GCC_except_table2479
+ GCC_except_table2481
+ GCC_except_table2483
+ GCC_except_table2489
+ GCC_except_table2494
+ GCC_except_table2504
+ GCC_except_table2515
+ GCC_except_table2516
+ GCC_except_table2522
+ GCC_except_table2530
+ GCC_except_table2532
+ GCC_except_table2533
+ GCC_except_table2539
+ GCC_except_table2545
+ GCC_except_table2551
+ GCC_except_table2553
+ GCC_except_table2555
+ GCC_except_table2556
+ GCC_except_table2557
+ GCC_except_table2560
+ GCC_except_table2566
+ GCC_except_table2571
+ GCC_except_table258
+ GCC_except_table258
+ GCC_except_table2583
+ GCC_except_table2584
+ GCC_except_table2585
+ GCC_except_table2586
+ GCC_except_table2588
+ GCC_except_table2592
+ GCC_except_table2597
+ GCC_except_table2598
+ GCC_except_table2607
+ GCC_except_table2611
+ GCC_except_table2612
+ GCC_except_table2616
+ GCC_except_table2617
+ GCC_except_table2620
+ GCC_except_table2622
+ GCC_except_table2623
+ GCC_except_table2624
+ GCC_except_table2626
+ GCC_except_table2642
+ GCC_except_table2643
+ GCC_except_table2657
+ GCC_except_table2658
+ GCC_except_table2675
+ GCC_except_table2676
+ GCC_except_table2678
+ GCC_except_table2681
+ GCC_except_table2682
+ GCC_except_table2684
+ GCC_except_table2686
+ GCC_except_table2692
+ GCC_except_table2698
+ GCC_except_table2700
+ GCC_except_table2701
+ GCC_except_table2712
+ GCC_except_table2714
+ GCC_except_table2725
+ GCC_except_table2727
+ GCC_except_table2735
+ GCC_except_table2736
+ GCC_except_table2738
+ GCC_except_table2740
+ GCC_except_table2749
+ GCC_except_table2755
+ GCC_except_table2761
+ GCC_except_table2762
+ GCC_except_table2763
+ GCC_except_table2764
+ GCC_except_table2770
+ GCC_except_table2775
+ GCC_except_table2776
+ GCC_except_table2777
+ GCC_except_table2787
+ GCC_except_table2791
+ GCC_except_table2792
+ GCC_except_table2798
+ GCC_except_table2803
+ GCC_except_table2812
+ GCC_except_table2813
+ GCC_except_table2815
+ GCC_except_table2817
+ GCC_except_table2818
+ GCC_except_table2820
+ GCC_except_table2826
+ GCC_except_table2832
+ GCC_except_table2839
+ GCC_except_table2842
+ GCC_except_table2845
+ GCC_except_table2846
+ GCC_except_table2847
+ GCC_except_table2855
+ GCC_except_table2860
+ GCC_except_table2874
+ GCC_except_table2875
+ GCC_except_table2876
+ GCC_except_table2881
+ GCC_except_table2883
+ GCC_except_table2897
+ GCC_except_table2898
+ GCC_except_table2899
+ GCC_except_table290
+ GCC_except_table290
+ GCC_except_table2900
+ GCC_except_table2907
+ GCC_except_table2933
+ GCC_except_table2934
+ GCC_except_table2940
+ GCC_except_table2949
+ GCC_except_table2950
+ GCC_except_table2951
+ GCC_except_table2952
+ GCC_except_table2954
+ GCC_except_table2955
+ GCC_except_table2956
+ GCC_except_table2959
+ GCC_except_table2961
+ GCC_except_table2975
+ GCC_except_table2976
+ GCC_except_table2977
+ GCC_except_table2978
+ GCC_except_table2981
+ GCC_except_table2987
+ GCC_except_table2989
+ GCC_except_table2991
+ GCC_except_table2992
+ GCC_except_table2994
+ GCC_except_table2999
+ GCC_except_table3003
+ GCC_except_table3005
+ GCC_except_table3011
+ GCC_except_table3015
+ GCC_except_table3017
+ GCC_except_table3019
+ GCC_except_table3030
+ GCC_except_table3034
+ GCC_except_table3049
+ GCC_except_table3050
+ GCC_except_table3051
+ GCC_except_table3053
+ GCC_except_table3059
+ GCC_except_table3063
+ GCC_except_table3064
+ GCC_except_table3070
+ GCC_except_table3074
+ GCC_except_table3078
+ GCC_except_table3080
+ GCC_except_table3081
+ GCC_except_table3087
+ GCC_except_table3094
+ GCC_except_table3096
+ GCC_except_table3097
+ GCC_except_table3098
+ GCC_except_table3099
+ GCC_except_table3100
+ GCC_except_table3113
+ GCC_except_table402
+ GCC_except_table449
+ GCC_except_table449
+ GCC_except_table553
+ GCC_except_table579
+ GCC_except_table583
+ GCC_except_table589
+ GCC_except_table597
+ GCC_except_table597
+ GCC_except_table601
+ GCC_except_table607
+ GCC_except_table615
+ GCC_except_table627
+ GCC_except_table633
+ GCC_except_table633
+ GCC_except_table641
+ GCC_except_table641
+ GCC_except_table643
+ GCC_except_table643
+ GCC_except_table647
+ GCC_except_table649
+ GCC_except_table651
+ GCC_except_table679
+ GCC_except_table685
+ GCC_except_table687
+ GCC_except_table689
+ GCC_except_table693
+ GCC_except_table717
+ GCC_except_table725
+ GCC_except_table727
+ GCC_except_table727
+ GCC_except_table729
+ GCC_except_table733
+ GCC_except_table735
+ GCC_except_table741
+ GCC_except_table751
+ GCC_except_table751
+ GCC_except_table753
+ GCC_except_table753
+ GCC_except_table755
+ GCC_except_table757
+ GCC_except_table759
+ GCC_except_table759
+ GCC_except_table805
+ GCC_except_table805
+ GCC_except_table817
+ GCC_except_table817
+ GCC_except_table821
+ GCC_except_table827
+ GCC_except_table827
+ GCC_except_table829
+ GCC_except_table831
+ GCC_except_table833
+ GCC_except_table847
+ GCC_except_table847
+ GCC_except_table855
+ GCC_except_table857
+ GCC_except_table863
+ GCC_except_table863
+ GCC_except_table867
+ GCC_except_table867
+ GCC_except_table873
+ GCC_except_table873
+ GCC_except_table881
+ GCC_except_table885
+ GCC_except_table947
+ GCC_except_table951
+ GCC_except_table951
+ GCC_except_table975
+ GCC_except_table975
+ GCC_except_table981
+ GCC_except_table989
+ GCC_except_table989
+ GCC_except_table991
+ _LTDDisablePayloadLogging
+ _LTDeviseHasGMSCapability.deviceSupportsGenerativeModelSystems
+ _LTDeviseHasGMSCapability.once
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_AFPreferences
+ __59+[_LTDAssetService assetsForLocales:includeTTS:completion:]_block_invoke.107
+ __59+[_LTDAssetService assetsForLocales:includeTTS:completion:]_block_invoke.cold.1
+ __59+[_LTDLanguageAssetService _availableAssetsWithCompletion:]_block_invoke_2.cold.1
+ __59+[_LTDLanguageAssetService _installedAssetsWithCompletion:]_block_invoke_2.cold.1
+ __59-[_LTOnlineTranslationEngine speak:withContext:completion:]_block_invoke.197
+ __59-[_LTOnlineTranslationEngine speak:withContext:completion:]_block_invoke.197.cold.1
+ __60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.51
+ __60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.53
+ __60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.54
+ __60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.55
+ __61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.43
+ __61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.43.cold.1
+ __61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.43.cold.2
+ __66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.22
+ __66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.29
+ __66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.29.cold.1
+ __LTDeviseHasGMSCapability
+ ___48+[_LTDLanguageAssetService syncInstalledLocales]_block_invoke
+ ___48+[_LTDLanguageAssetService syncInstalledLocales]_block_invoke_2
+ ___55+[_LTDLanguageAssetService _supportedLocalesWithError:]_block_invoke
+ ___59+[_LTDAssetService assetsForLocales:includeTTS:completion:]_block_invoke
+ ___59+[_LTDLanguageAssetService _availableAssetsWithCompletion:]_block_invoke_2
+ ___59+[_LTDLanguageAssetService _installedAssetsWithCompletion:]_block_invoke_2
+ ___73+[_LTDLanguageAssetService _languageModelsForLocales:initialState:error:]_block_invoke
+ ___73+[_LTDLanguageAssetService _languageModelsForLocales:initialState:error:]_block_invoke_2
+ ____LTDeviseHasGMSCapability_block_invoke
+ ___block_descriptor_40_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_48_e8_32bs_e51_v24?0"_LTDOfflineConfigurationModel"8"NSError"16l
+ ___block_descriptor_48_e8_32s_e41_"_LTLanguageAssetModel"16?0"NSLocale"8l
+ ___block_descriptor_57_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16l
+ __block_literal_global.14
+ __block_literal_global.18
+ __block_literal_global.202
+ __block_literal_global.49
+ __block_literal_global.67
+ __block_literal_global.67
+ _kLTTranslateAppAttributionBundleID
+ _objc_msgSend$_languageModelsForLocales:initialState:error:
+ _objc_msgSend$_supportedLocalesWithError:
+ _objc_msgSend$addLanguages:useCellular:
+ _objc_msgSend$assetsForLocales:includeTTS:completion:
+ _objc_msgSend$assetsForLocales:includeTTS:error:
+ _objc_msgSend$contains_masked_profanity
+ _objc_msgSend$disable_payload_logging
+ _objc_msgSend$engine_error_code
+ _objc_msgSend$engine_error_message
+ _objc_msgSend$languageIdentificationEnabled
+ _objc_msgSend$lt_initWithTask:inputMode:invocationType:explicitLanguageFilterEnabled:onDevice:translateAppContext:
+ _objc_msgSend$lt_unsupportedLanguageError:
+ _objc_msgSend$mask_profanity
+ _objc_msgSend$removeLanguages:
+ _objc_msgSend$self_session_id
+ _objc_msgSend$setDisable_payload_logging:
+ _objc_msgSend$setObject:forType:
+ _objc_msgSend$sharedPreferences
+ _objc_msgSend$siriDataSharingOptInStatus
+ _objc_msgSend$startWithTask:inputMode:invocationType:interfaceMode:explicitLanguageFilterEnabled:onDevice:mtId:sessionId:translateAppContext:
+ _objc_msgSend$syncInstalledLocales
- +[FTApgBatchRecoverMessage session_message_immutableClassForType:]
- +[FTApgBatchRecoverMessage session_message_typeForImmutableObject:]
- +[FTBatchRecoverStreamingRequest content_immutableClassForType:]
- +[FTBatchRecoverStreamingRequest content_typeForImmutableObject:]
- +[FTBatchRecoverStreamingResponse content_immutableClassForType:]
- +[FTBatchRecoverStreamingResponse content_typeForImmutableObject:]
- +[FTMtStreamingTranslationMessage session_message_immutableClassForType:]
- +[FTMtStreamingTranslationMessage session_message_typeForImmutableObject:]
- +[FTMutableApgBatchRecoverMessage session_message_mutableClassForType:]
- +[FTMutableApgBatchRecoverMessage session_message_typeForMutableObject:]
- +[FTMutableApgBatchRecoverMessage session_message_typeForObject:]
- +[FTMutableBatchRecoverStreamingRequest content_mutableClassForType:]
- +[FTMutableBatchRecoverStreamingRequest content_typeForMutableObject:]
- +[FTMutableBatchRecoverStreamingRequest content_typeForObject:]
- +[FTMutableBatchRecoverStreamingResponse content_mutableClassForType:]
- +[FTMutableBatchRecoverStreamingResponse content_typeForMutableObject:]
- +[FTMutableBatchRecoverStreamingResponse content_typeForObject:]
- +[FTMutableMtStreamingTranslationMessage session_message_mutableClassForType:]
- +[FTMutableMtStreamingTranslationMessage session_message_typeForMutableObject:]
- +[FTMutableMtStreamingTranslationMessage session_message_typeForObject:]
- +[FTMutableStreamingTranslationStreamingRequest content_mutableClassForType:]
- +[FTMutableStreamingTranslationStreamingRequest content_typeForMutableObject:]
- +[FTMutableStreamingTranslationStreamingRequest content_typeForObject:]
- +[FTMutableStreamingTranslationStreamingResponse content_mutableClassForType:]
- +[FTMutableStreamingTranslationStreamingResponse content_typeForMutableObject:]
- +[FTMutableStreamingTranslationStreamingResponse content_typeForObject:]
- +[FTStreamingTranslationStreamingRequest content_immutableClassForType:]
- +[FTStreamingTranslationStreamingRequest content_typeForImmutableObject:]
- +[FTStreamingTranslationStreamingResponse content_immutableClassForType:]
- +[FTStreamingTranslationStreamingResponse content_typeForImmutableObject:]
- +[MTSchemaMTInvocationStarted(LTTranslationAdditions) lt_initWithTask:inputMode:invocationType:explicitLanguageFilterEnabled:languageIdentificationEnabled:onDevice:translateAppContext:]
- +[_LTDAssetService assetsForLocales:completion:]
- +[_LTDAssetService assetsForLocales:error:]
- +[_LTDAssetService assetsForLocales:error:].cold.1
- +[_LTDSELFLoggingProduction startWithTask:inputMode:invocationType:interfaceMode:explicitLanguageFilterEnabled:languageIdentificationEnabled:onDevice:mtId:sessionId:translateAppContext:]
- -[FTApgBatchRecoverMessage .cxx_destruct]
- -[FTApgBatchRecoverMessage addObjectToBuffer:]
- -[FTApgBatchRecoverMessage copyWithZone:]
- -[FTApgBatchRecoverMessage flatbuffData]
- -[FTApgBatchRecoverMessage initAndVerifyWithFlatbuffData:]
- -[FTApgBatchRecoverMessage initWithFlatbuffData:]
- -[FTApgBatchRecoverMessage initWithFlatbuffData:root:]
- -[FTApgBatchRecoverMessage initWithFlatbuffData:root:verify:]
- -[FTApgBatchRecoverMessage session_messageAsFTBatchRecoverFinalResponse]
- -[FTApgBatchRecoverMessage session_messageAsFTPronGuessResponse]
- -[FTApgBatchRecoverMessage session_messageAsFTStartBatchRecoverRequest]
- -[FTApgBatchRecoverMessage session_message]
- -[FTApgBatchRecoverMessage session_message_type]
- -[FTApgService performBatchRecoverWithDelegate:requestBuilder:completion:]
- -[FTBatchRecoverFinalResponse .cxx_destruct]
- -[FTBatchRecoverFinalResponse addObjectToBuffer:]
- -[FTBatchRecoverFinalResponse copyWithZone:]
- -[FTBatchRecoverFinalResponse error_code]
- -[FTBatchRecoverFinalResponse error_str]
- -[FTBatchRecoverFinalResponse flatbuffData]
- -[FTBatchRecoverFinalResponse initAndVerifyWithFlatbuffData:]
- -[FTBatchRecoverFinalResponse initWithFlatbuffData:]
- -[FTBatchRecoverFinalResponse initWithFlatbuffData:root:]
- -[FTBatchRecoverFinalResponse initWithFlatbuffData:root:verify:]
- -[FTBatchRecoverFinalResponse num_of_processed]
- -[FTBatchRecoverFinalResponse num_of_requested]
- -[FTBatchRecoverFinalResponse num_of_succeeded]
- -[FTBatchRecoverFinalResponse session_id]
- -[FTBatchRecoverFinalResponse speech_id]
- -[FTBatchRecoverStreamingContext .cxx_destruct]
- -[FTBatchRecoverStreamingContext closeStream]
- -[FTBatchRecoverStreamingContext initWithGRPCStreamingCallContext:]
- -[FTBatchRecoverStreamingContext sendBatchRecoverStreamingRequest:]
- -[FTBatchRecoverStreamingRequest .cxx_destruct]
- -[FTBatchRecoverStreamingRequest addObjectToBuffer:]
- -[FTBatchRecoverStreamingRequest contentAsFTStartBatchRecoverRequest]
- -[FTBatchRecoverStreamingRequest content]
- -[FTBatchRecoverStreamingRequest content_type]
- -[FTBatchRecoverStreamingRequest copyWithZone:]
- -[FTBatchRecoverStreamingRequest flatbuffData]
- -[FTBatchRecoverStreamingRequest initAndVerifyWithFlatbuffData:]
- -[FTBatchRecoverStreamingRequest initWithFlatbuffData:]
- -[FTBatchRecoverStreamingRequest initWithFlatbuffData:root:]
- -[FTBatchRecoverStreamingRequest initWithFlatbuffData:root:verify:]
- -[FTBatchRecoverStreamingResponse .cxx_destruct]
- -[FTBatchRecoverStreamingResponse addObjectToBuffer:]
- -[FTBatchRecoverStreamingResponse contentAsFTBatchRecoverFinalResponse]
- -[FTBatchRecoverStreamingResponse contentAsFTPronGuessResponse]
- -[FTBatchRecoverStreamingResponse content]
- -[FTBatchRecoverStreamingResponse content_type]
- -[FTBatchRecoverStreamingResponse copyWithZone:]
- -[FTBatchRecoverStreamingResponse flatbuffData]
- -[FTBatchRecoverStreamingResponse initAndVerifyWithFlatbuffData:]
- -[FTBatchRecoverStreamingResponse initWithFlatbuffData:]
- -[FTBatchRecoverStreamingResponse initWithFlatbuffData:root:]
- -[FTBatchRecoverStreamingResponse initWithFlatbuffData:root:verify:]
- -[FTMtService performStreamingTranslationWithDelegate:requestBuilder:completion:]
- -[FTMtStreamingTranslationMessage .cxx_destruct]
- -[FTMtStreamingTranslationMessage addObjectToBuffer:]
- -[FTMtStreamingTranslationMessage copyWithZone:]
- -[FTMtStreamingTranslationMessage flatbuffData]
- -[FTMtStreamingTranslationMessage initAndVerifyWithFlatbuffData:]
- -[FTMtStreamingTranslationMessage initWithFlatbuffData:]
- -[FTMtStreamingTranslationMessage initWithFlatbuffData:root:]
- -[FTMtStreamingTranslationMessage initWithFlatbuffData:root:verify:]
- -[FTMtStreamingTranslationMessage session_messageAsFTStreamingTranslationRequest]
- -[FTMtStreamingTranslationMessage session_messageAsFTTranslationResponse]
- -[FTMtStreamingTranslationMessage session_message]
- -[FTMtStreamingTranslationMessage session_message_type]
- -[FTMutableApgBatchRecoverMessage copyWithZone:]
- -[FTMutableApgBatchRecoverMessage init]
- -[FTMutableApgBatchRecoverMessage session_messageAsFTBatchRecoverFinalResponse]
- -[FTMutableApgBatchRecoverMessage session_messageAsFTPronGuessResponse]
- -[FTMutableApgBatchRecoverMessage session_messageAsFTStartBatchRecoverRequest]
- -[FTMutableApgBatchRecoverMessage session_message_type]
- -[FTMutableApgBatchRecoverMessage setSession_message:]
- -[FTMutableApgBatchRecoverMessage setSession_messageAsFTBatchRecoverFinalResponse:]
- -[FTMutableApgBatchRecoverMessage setSession_messageAsFTPronGuessResponse:]
- -[FTMutableApgBatchRecoverMessage setSession_messageAsFTStartBatchRecoverRequest:]
- -[FTMutableApgBatchRecoverMessage setSession_message_type:]
- -[FTMutableBatchRecoverFinalResponse copyWithZone:]
- -[FTMutableBatchRecoverFinalResponse error_code]
- -[FTMutableBatchRecoverFinalResponse error_str]
- -[FTMutableBatchRecoverFinalResponse init]
- -[FTMutableBatchRecoverFinalResponse num_of_processed]
- -[FTMutableBatchRecoverFinalResponse num_of_requested]
- -[FTMutableBatchRecoverFinalResponse num_of_succeeded]
- -[FTMutableBatchRecoverFinalResponse session_id]
- -[FTMutableBatchRecoverFinalResponse setError_code:]
- -[FTMutableBatchRecoverFinalResponse setError_str:]
- -[FTMutableBatchRecoverFinalResponse setNum_of_processed:]
- -[FTMutableBatchRecoverFinalResponse setNum_of_requested:]
- -[FTMutableBatchRecoverFinalResponse setNum_of_succeeded:]
- -[FTMutableBatchRecoverFinalResponse setSession_id:]
- -[FTMutableBatchRecoverFinalResponse setSpeech_id:]
- -[FTMutableBatchRecoverFinalResponse speech_id]
- -[FTMutableBatchRecoverStreamingRequest contentAsFTStartBatchRecoverRequest]
- -[FTMutableBatchRecoverStreamingRequest content_type]
- -[FTMutableBatchRecoverStreamingRequest copyWithZone:]
- -[FTMutableBatchRecoverStreamingRequest init]
- -[FTMutableBatchRecoverStreamingRequest setContent:]
- -[FTMutableBatchRecoverStreamingRequest setContentAsFTStartBatchRecoverRequest:]
- -[FTMutableBatchRecoverStreamingRequest setContent_type:]
- -[FTMutableBatchRecoverStreamingResponse contentAsFTBatchRecoverFinalResponse]
- -[FTMutableBatchRecoverStreamingResponse contentAsFTPronGuessResponse]
- -[FTMutableBatchRecoverStreamingResponse content_type]
- -[FTMutableBatchRecoverStreamingResponse copyWithZone:]
- -[FTMutableBatchRecoverStreamingResponse init]
- -[FTMutableBatchRecoverStreamingResponse setContent:]
- -[FTMutableBatchRecoverStreamingResponse setContentAsFTBatchRecoverFinalResponse:]
- -[FTMutableBatchRecoverStreamingResponse setContentAsFTPronGuessResponse:]
- -[FTMutableBatchRecoverStreamingResponse setContent_type:]
- -[FTMutableMtStreamingTranslationMessage copyWithZone:]
- -[FTMutableMtStreamingTranslationMessage init]
- -[FTMutableMtStreamingTranslationMessage session_messageAsFTStreamingTranslationRequest]
- -[FTMutableMtStreamingTranslationMessage session_messageAsFTTranslationResponse]
- -[FTMutableMtStreamingTranslationMessage session_message_type]
- -[FTMutableMtStreamingTranslationMessage setSession_message:]
- -[FTMutableMtStreamingTranslationMessage setSession_messageAsFTStreamingTranslationRequest:]
- -[FTMutableMtStreamingTranslationMessage setSession_messageAsFTTranslationResponse:]
- -[FTMutableMtStreamingTranslationMessage setSession_message_type:]
- -[FTMutableQssMessage container_messageAsFTApgBatchRecoverMessage]
- -[FTMutableQssMessage container_messageAsFTMtStreamingTranslationMessage]
- -[FTMutableQssMessage setContainer_messageAsFTApgBatchRecoverMessage:]
- -[FTMutableQssMessage setContainer_messageAsFTMtStreamingTranslationMessage:]
- -[FTMutableStartBatchRecoverRequest apg_ids]
- -[FTMutableStartBatchRecoverRequest copyWithZone:]
- -[FTMutableStartBatchRecoverRequest init]
- -[FTMutableStartBatchRecoverRequest language]
- -[FTMutableStartBatchRecoverRequest session_id]
- -[FTMutableStartBatchRecoverRequest setApg_ids:]
- -[FTMutableStartBatchRecoverRequest setLanguage:]
- -[FTMutableStartBatchRecoverRequest setSession_id:]
- -[FTMutableStartBatchRecoverRequest setSpeech_id:]
- -[FTMutableStartBatchRecoverRequest speech_id]
- -[FTMutableStreamingTranslationRequest app_id]
- -[FTMutableStreamingTranslationRequest copyWithZone:]
- -[FTMutableStreamingTranslationRequest disable_log]
- -[FTMutableStreamingTranslationRequest final_message]
- -[FTMutableStreamingTranslationRequest init]
- -[FTMutableStreamingTranslationRequest opt_in_status]
- -[FTMutableStreamingTranslationRequest request_id]
- -[FTMutableStreamingTranslationRequest sequence_id]
- -[FTMutableStreamingTranslationRequest setApp_id:]
- -[FTMutableStreamingTranslationRequest setDisable_log:]
- -[FTMutableStreamingTranslationRequest setFinal_message:]
- -[FTMutableStreamingTranslationRequest setOpt_in_status:]
- -[FTMutableStreamingTranslationRequest setRequest_id:]
- -[FTMutableStreamingTranslationRequest setSequence_id:]
- -[FTMutableStreamingTranslationRequest setSource_language:]
- -[FTMutableStreamingTranslationRequest setSpeech_id:]
- -[FTMutableStreamingTranslationRequest setTarget_language:]
- -[FTMutableStreamingTranslationRequest setTask:]
- -[FTMutableStreamingTranslationRequest setTranslation_text:]
- -[FTMutableStreamingTranslationRequest source_language]
- -[FTMutableStreamingTranslationRequest speech_id]
- -[FTMutableStreamingTranslationRequest target_language]
- -[FTMutableStreamingTranslationRequest task]
- -[FTMutableStreamingTranslationRequest translation_text]
- -[FTMutableStreamingTranslationStreamingRequest contentAsFTStreamingTranslationRequest]
- -[FTMutableStreamingTranslationStreamingRequest content_type]
- -[FTMutableStreamingTranslationStreamingRequest copyWithZone:]
- -[FTMutableStreamingTranslationStreamingRequest init]
- -[FTMutableStreamingTranslationStreamingRequest setContent:]
- -[FTMutableStreamingTranslationStreamingRequest setContentAsFTStreamingTranslationRequest:]
- -[FTMutableStreamingTranslationStreamingRequest setContent_type:]
- -[FTMutableStreamingTranslationStreamingResponse contentAsFTTranslationResponse]
- -[FTMutableStreamingTranslationStreamingResponse content_type]
- -[FTMutableStreamingTranslationStreamingResponse copyWithZone:]
- -[FTMutableStreamingTranslationStreamingResponse init]
- -[FTMutableStreamingTranslationStreamingResponse setContent:]
- -[FTMutableStreamingTranslationStreamingResponse setContentAsFTTranslationResponse:]
- -[FTMutableStreamingTranslationStreamingResponse setContent_type:]
- -[FTQssMessage container_messageAsFTApgBatchRecoverMessage]
- -[FTQssMessage container_messageAsFTMtStreamingTranslationMessage]
- -[FTStartBatchRecoverRequest .cxx_destruct]
- -[FTStartBatchRecoverRequest addObjectToBuffer:]
- -[FTStartBatchRecoverRequest apg_ids]
- -[FTStartBatchRecoverRequest apg_ids_count]
- -[FTStartBatchRecoverRequest apg_ids_enumerateObjectsUsingBlock:]
- -[FTStartBatchRecoverRequest apg_ids_objectAtIndex:]
- -[FTStartBatchRecoverRequest copyWithZone:]
- -[FTStartBatchRecoverRequest flatbuffData]
- -[FTStartBatchRecoverRequest initAndVerifyWithFlatbuffData:]
- -[FTStartBatchRecoverRequest initWithFlatbuffData:]
- -[FTStartBatchRecoverRequest initWithFlatbuffData:root:]
- -[FTStartBatchRecoverRequest initWithFlatbuffData:root:verify:]
- -[FTStartBatchRecoverRequest language]
- -[FTStartBatchRecoverRequest session_id]
- -[FTStartBatchRecoverRequest speech_id]
- -[FTStreamingTranslationRequest .cxx_destruct]
- -[FTStreamingTranslationRequest addObjectToBuffer:]
- -[FTStreamingTranslationRequest app_id]
- -[FTStreamingTranslationRequest copyWithZone:]
- -[FTStreamingTranslationRequest disable_log]
- -[FTStreamingTranslationRequest final_message]
- -[FTStreamingTranslationRequest flatbuffData]
- -[FTStreamingTranslationRequest initAndVerifyWithFlatbuffData:]
- -[FTStreamingTranslationRequest initWithFlatbuffData:]
- -[FTStreamingTranslationRequest initWithFlatbuffData:root:]
- -[FTStreamingTranslationRequest initWithFlatbuffData:root:verify:]
- -[FTStreamingTranslationRequest opt_in_status]
- -[FTStreamingTranslationRequest request_id]
- -[FTStreamingTranslationRequest sequence_id]
- -[FTStreamingTranslationRequest source_language]
- -[FTStreamingTranslationRequest speech_id]
- -[FTStreamingTranslationRequest target_language]
- -[FTStreamingTranslationRequest task]
- -[FTStreamingTranslationRequest translation_text]
- -[FTStreamingTranslationStreamingContext .cxx_destruct]
- -[FTStreamingTranslationStreamingContext closeStream]
- -[FTStreamingTranslationStreamingContext initWithGRPCStreamingCallContext:]
- -[FTStreamingTranslationStreamingContext sendStreamingTranslationStreamingRequest:]
- -[FTStreamingTranslationStreamingRequest .cxx_destruct]
- -[FTStreamingTranslationStreamingRequest addObjectToBuffer:]
- -[FTStreamingTranslationStreamingRequest contentAsFTStreamingTranslationRequest]
- -[FTStreamingTranslationStreamingRequest content]
- -[FTStreamingTranslationStreamingRequest content_type]
- -[FTStreamingTranslationStreamingRequest copyWithZone:]
- -[FTStreamingTranslationStreamingRequest flatbuffData]
- -[FTStreamingTranslationStreamingRequest initAndVerifyWithFlatbuffData:]
- -[FTStreamingTranslationStreamingRequest initWithFlatbuffData:]
- -[FTStreamingTranslationStreamingRequest initWithFlatbuffData:root:]
- -[FTStreamingTranslationStreamingRequest initWithFlatbuffData:root:verify:]
- -[FTStreamingTranslationStreamingResponse .cxx_destruct]
- -[FTStreamingTranslationStreamingResponse addObjectToBuffer:]
- -[FTStreamingTranslationStreamingResponse contentAsFTTranslationResponse]
- -[FTStreamingTranslationStreamingResponse content]
- -[FTStreamingTranslationStreamingResponse content_type]
- -[FTStreamingTranslationStreamingResponse copyWithZone:]
- -[FTStreamingTranslationStreamingResponse flatbuffData]
- -[FTStreamingTranslationStreamingResponse initAndVerifyWithFlatbuffData:]
- -[FTStreamingTranslationStreamingResponse initWithFlatbuffData:]
- -[FTStreamingTranslationStreamingResponse initWithFlatbuffData:root:]
- -[FTStreamingTranslationStreamingResponse initWithFlatbuffData:root:verify:]
- -[_LTDConfigurationCache setObject:forType:ttl:completion:]
- -[_LTDConfigurationCache setObject:forType:ttl:completion:].cold.1
- -[_LTDSELFLoggingManager sendSpeechTranslationFrameworkRequestReceivedWithInvocationId:requestRoute:numberOfSentences:]
- -[_LTDSELFLoggingManager sendSpeechTranslationFrameworkRequestReceivedWithInvocationId:requestRoute:numberOfSentences:].cold.1
- GCC_except_table1009
- GCC_except_table1017
- GCC_except_table1017
- GCC_except_table1033
- GCC_except_table1055
- GCC_except_table1061
- GCC_except_table1063
- GCC_except_table1063
- GCC_except_table1067
- GCC_except_table1067
- GCC_except_table1069
- GCC_except_table1069
- GCC_except_table1085
- GCC_except_table1091
- GCC_except_table1097
- GCC_except_table1101
- GCC_except_table1111
- GCC_except_table1141
- GCC_except_table1155
- GCC_except_table1162
- GCC_except_table1170
- GCC_except_table1170
- GCC_except_table1174
- GCC_except_table1176
- GCC_except_table1178
- GCC_except_table1190
- GCC_except_table1201
- GCC_except_table1203
- GCC_except_table1211
- GCC_except_table1211
- GCC_except_table1215
- GCC_except_table1215
- GCC_except_table1219
- GCC_except_table1241
- GCC_except_table1243
- GCC_except_table1249
- GCC_except_table1255
- GCC_except_table1261
- GCC_except_table1265
- GCC_except_table1271
- GCC_except_table1271
- GCC_except_table1273
- GCC_except_table1273
- GCC_except_table1277
- GCC_except_table1281
- GCC_except_table1301
- GCC_except_table1356
- GCC_except_table1356
- GCC_except_table1360
- GCC_except_table1360
- GCC_except_table1362
- GCC_except_table1362
- GCC_except_table1364
- GCC_except_table1366
- GCC_except_table1370
- GCC_except_table1370
- GCC_except_table1372
- GCC_except_table1376
- GCC_except_table1378
- GCC_except_table1380
- GCC_except_table1386
- GCC_except_table1386
- GCC_except_table1388
- GCC_except_table1392
- GCC_except_table1392
- GCC_except_table1394
- GCC_except_table1398
- GCC_except_table1404
- GCC_except_table1424
- GCC_except_table1424
- GCC_except_table1430
- GCC_except_table1440
- GCC_except_table1446
- GCC_except_table1452
- GCC_except_table1455
- GCC_except_table1457
- GCC_except_table1461
- GCC_except_table1467
- GCC_except_table1477
- GCC_except_table1483
- GCC_except_table1485
- GCC_except_table1491
- GCC_except_table1498
- GCC_except_table1502
- GCC_except_table1504
- GCC_except_table1504
- GCC_except_table1518
- GCC_except_table1520
- GCC_except_table1524
- GCC_except_table1524
- GCC_except_table1530
- GCC_except_table1532
- GCC_except_table1534
- GCC_except_table1534
- GCC_except_table1540
- GCC_except_table1555
- GCC_except_table1555
- GCC_except_table1571
- GCC_except_table1571
- GCC_except_table1583
- GCC_except_table1583
- GCC_except_table1585
- GCC_except_table1589
- GCC_except_table1589
- GCC_except_table1595
- GCC_except_table1597
- GCC_except_table1601
- GCC_except_table1601
- GCC_except_table1609
- GCC_except_table1617
- GCC_except_table1623
- GCC_except_table1627
- GCC_except_table1637
- GCC_except_table1641
- GCC_except_table1650
- GCC_except_table1656
- GCC_except_table1656
- GCC_except_table1658
- GCC_except_table1658
- GCC_except_table1660
- GCC_except_table1660
- GCC_except_table1662
- GCC_except_table1662
- GCC_except_table1666
- GCC_except_table1670
- GCC_except_table1676
- GCC_except_table1676
- GCC_except_table1680
- GCC_except_table1680
- GCC_except_table1682
- GCC_except_table1682
- GCC_except_table1684
- GCC_except_table1688
- GCC_except_table1688
- GCC_except_table1698
- GCC_except_table1708
- GCC_except_table1718
- GCC_except_table1718
- GCC_except_table1724
- GCC_except_table1742
- GCC_except_table1742
- GCC_except_table1746
- GCC_except_table1754
- GCC_except_table1760
- GCC_except_table1770
- GCC_except_table1778
- GCC_except_table1788
- GCC_except_table1790
- GCC_except_table1790
- GCC_except_table1796
- GCC_except_table1800
- GCC_except_table1800
- GCC_except_table1838
- GCC_except_table1848
- GCC_except_table1850
- GCC_except_table1864
- GCC_except_table1866
- GCC_except_table1866
- GCC_except_table1874
- GCC_except_table1878
- GCC_except_table1878
- GCC_except_table1888
- GCC_except_table1892
- GCC_except_table1912
- GCC_except_table1912
- GCC_except_table1926
- GCC_except_table1932
- GCC_except_table1948
- GCC_except_table1950
- GCC_except_table1950
- GCC_except_table1964
- GCC_except_table1964
- GCC_except_table1966
- GCC_except_table1978
- GCC_except_table1978
- GCC_except_table1992
- GCC_except_table1996
- GCC_except_table2002
- GCC_except_table2008
- GCC_except_table2016
- GCC_except_table2038
- GCC_except_table2046
- GCC_except_table2047
- GCC_except_table2048
- GCC_except_table2051
- GCC_except_table2053
- GCC_except_table2054
- GCC_except_table2054
- GCC_except_table2055
- GCC_except_table2057
- GCC_except_table2059
- GCC_except_table2060
- GCC_except_table2061
- GCC_except_table2062
- GCC_except_table2063
- GCC_except_table2067
- GCC_except_table2069
- GCC_except_table2070
- GCC_except_table2072
- GCC_except_table2078
- GCC_except_table2079
- GCC_except_table2080
- GCC_except_table2081
- GCC_except_table2082
- GCC_except_table2084
- GCC_except_table2085
- GCC_except_table2087
- GCC_except_table2093
- GCC_except_table2097
- GCC_except_table2098
- GCC_except_table2104
- GCC_except_table2113
- GCC_except_table2119
- GCC_except_table2121
- GCC_except_table2122
- GCC_except_table2143
- GCC_except_table2149
- GCC_except_table2156
- GCC_except_table2173
- GCC_except_table2174
- GCC_except_table2175
- GCC_except_table2177
- GCC_except_table2179
- GCC_except_table2180
- GCC_except_table2181
- GCC_except_table2186
- GCC_except_table2192
- GCC_except_table2203
- GCC_except_table2205
- GCC_except_table2206
- GCC_except_table2207
- GCC_except_table2209
- GCC_except_table2210
- GCC_except_table2211
- GCC_except_table2212
- GCC_except_table2213
- GCC_except_table2214
- GCC_except_table2215
- GCC_except_table2216
- GCC_except_table2230
- GCC_except_table2231
- GCC_except_table2237
- GCC_except_table2245
- GCC_except_table2246
- GCC_except_table2247
- GCC_except_table2249
- GCC_except_table2256
- GCC_except_table2266
- GCC_except_table2270
- GCC_except_table2280
- GCC_except_table2296
- GCC_except_table2306
- GCC_except_table2307
- GCC_except_table2316
- GCC_except_table2322
- GCC_except_table2324
- GCC_except_table2330
- GCC_except_table2333
- GCC_except_table2335
- GCC_except_table2336
- GCC_except_table2337
- GCC_except_table2340
- GCC_except_table2346
- GCC_except_table2349
- GCC_except_table2351
- GCC_except_table2352
- GCC_except_table2361
- GCC_except_table2362
- GCC_except_table2363
- GCC_except_table2366
- GCC_except_table2368
- GCC_except_table2377
- GCC_except_table2386
- GCC_except_table2391
- GCC_except_table2392
- GCC_except_table2398
- GCC_except_table2401
- GCC_except_table2404
- GCC_except_table2405
- GCC_except_table2406
- GCC_except_table2407
- GCC_except_table2418
- GCC_except_table2419
- GCC_except_table2420
- GCC_except_table2422
- GCC_except_table2433
- GCC_except_table2435
- GCC_except_table2441
- GCC_except_table2450
- GCC_except_table2457
- GCC_except_table2461
- GCC_except_table2465
- GCC_except_table2471
- GCC_except_table2473
- GCC_except_table2475
- GCC_except_table2477
- GCC_except_table2486
- GCC_except_table2490
- GCC_except_table2491
- GCC_except_table2492
- GCC_except_table2493
- GCC_except_table2496
- GCC_except_table2497
- GCC_except_table2499
- GCC_except_table2507
- GCC_except_table2511
- GCC_except_table2512
- GCC_except_table2518
- GCC_except_table2524
- GCC_except_table2526
- GCC_except_table2528
- GCC_except_table2537
- GCC_except_table2549
- GCC_except_table2552
- GCC_except_table2563
- GCC_except_table2564
- GCC_except_table2575
- GCC_except_table2578
- GCC_except_table2579
- GCC_except_table2580
- GCC_except_table2593
- GCC_except_table2599
- GCC_except_table2603
- GCC_except_table2604
- GCC_except_table2605
- GCC_except_table2606
- GCC_except_table2608
- GCC_except_table2619
- GCC_except_table2629
- GCC_except_table2631
- GCC_except_table2633
- GCC_except_table2634
- GCC_except_table2635
- GCC_except_table2636
- GCC_except_table2638
- GCC_except_table2639
- GCC_except_table2640
- GCC_except_table2645
- GCC_except_table2646
- GCC_except_table2655
- GCC_except_table2660
- GCC_except_table2662
- GCC_except_table2664
- GCC_except_table2666
- GCC_except_table2668
- GCC_except_table2670
- GCC_except_table2673
- GCC_except_table2690
- GCC_except_table2691
- GCC_except_table2697
- GCC_except_table2705
- GCC_except_table2706
- GCC_except_table2719
- GCC_except_table2722
- GCC_except_table2723
- GCC_except_table2724
- GCC_except_table2728
- GCC_except_table2729
- GCC_except_table2730
- GCC_except_table2731
- GCC_except_table2745
- GCC_except_table2746
- GCC_except_table2753
- GCC_except_table2759
- GCC_except_table2766
- GCC_except_table2771
- GCC_except_table2772
- GCC_except_table2782
- GCC_except_table2784
- GCC_except_table2785
- GCC_except_table2786
- GCC_except_table2793
- GCC_except_table2795
- GCC_except_table2801
- GCC_except_table2806
- GCC_except_table2807
- GCC_except_table2808
- GCC_except_table2809
- GCC_except_table2819
- GCC_except_table2821
- GCC_except_table2822
- GCC_except_table2823
- GCC_except_table2825
- GCC_except_table2827
- GCC_except_table2837
- GCC_except_table2838
- GCC_except_table2850
- GCC_except_table2856
- GCC_except_table2858
- GCC_except_table2861
- GCC_except_table2862
- GCC_except_table2863
- GCC_except_table2864
- GCC_except_table2878
- GCC_except_table2879
- GCC_except_table2888
- GCC_except_table2890
- GCC_except_table2892
- GCC_except_table2893
- GCC_except_table2905
- GCC_except_table2906
- GCC_except_table2912
- GCC_except_table2918
- GCC_except_table292
- GCC_except_table292
- GCC_except_table2922
- GCC_except_table2929
- GCC_except_table2931
- GCC_except_table2937
- GCC_except_table2941
- GCC_except_table2943
- GCC_except_table2944
- GCC_except_table2945
- GCC_except_table2946
- GCC_except_table2953
- GCC_except_table2966
- GCC_except_table2979
- GCC_except_table2986
- GCC_except_table2993
- GCC_except_table2998
- GCC_except_table3002
- GCC_except_table3004
- GCC_except_table3006
- GCC_except_table3012
- GCC_except_table3020
- GCC_except_table3021
- GCC_except_table3022
- GCC_except_table3025
- GCC_except_table3031
- GCC_except_table3033
- GCC_except_table3036
- GCC_except_table3038
- GCC_except_table3039
- GCC_except_table3040
- GCC_except_table3043
- GCC_except_table3044
- GCC_except_table3045
- GCC_except_table3054
- GCC_except_table3058
- GCC_except_table3060
- GCC_except_table3061
- GCC_except_table3062
- GCC_except_table3065
- GCC_except_table3066
- GCC_except_table3072
- GCC_except_table3083
- GCC_except_table3088
- GCC_except_table3090
- GCC_except_table3091
- GCC_except_table3092
- GCC_except_table3093
- GCC_except_table3095
- GCC_except_table3101
- GCC_except_table3105
- GCC_except_table3116
- GCC_except_table3118
- GCC_except_table3119
- GCC_except_table3120
- GCC_except_table3122
- GCC_except_table3123
- GCC_except_table3129
- GCC_except_table3136
- GCC_except_table3138
- GCC_except_table3139
- GCC_except_table3140
- GCC_except_table3141
- GCC_except_table3142
- GCC_except_table3148
- GCC_except_table3154
- GCC_except_table3155
- GCC_except_table378
- GCC_except_table378
- GCC_except_table378
- GCC_except_table400
- GCC_except_table400
- GCC_except_table412
- GCC_except_table412
- GCC_except_table412
- GCC_except_table420
- GCC_except_table529
- GCC_except_table529
- GCC_except_table531
- GCC_except_table539
- GCC_except_table539
- GCC_except_table545
- GCC_except_table545
- GCC_except_table549
- GCC_except_table549
- GCC_except_table555
- GCC_except_table555
- GCC_except_table559
- GCC_except_table559
- GCC_except_table561
- GCC_except_table577
- GCC_except_table577
- GCC_except_table599
- GCC_except_table605
- GCC_except_table609
- GCC_except_table617
- GCC_except_table619
- GCC_except_table635
- GCC_except_table635
- GCC_except_table645
- GCC_except_table653
- GCC_except_table655
- GCC_except_table661
- GCC_except_table661
- GCC_except_table663
- GCC_except_table665
- GCC_except_table667
- GCC_except_table667
- GCC_except_table673
- GCC_except_table675
- GCC_except_table681
- GCC_except_table683
- GCC_except_table695
- GCC_except_table697
- GCC_except_table709
- GCC_except_table709
- GCC_except_table711
- GCC_except_table723
- GCC_except_table737
- GCC_except_table739
- GCC_except_table739
- GCC_except_table763
- GCC_except_table773
- GCC_except_table779
- GCC_except_table783
- GCC_except_table795
- GCC_except_table799
- GCC_except_table799
- GCC_except_table803
- GCC_except_table813
- GCC_except_table815
- GCC_except_table819
- GCC_except_table825
- GCC_except_table825
- GCC_except_table837
- GCC_except_table837
- GCC_except_table841
- GCC_except_table841
- GCC_except_table859
- GCC_except_table883
- GCC_except_table897
- GCC_except_table897
- GCC_except_table905
- GCC_except_table905
- GCC_except_table915
- GCC_except_table929
- GCC_except_table933
- GCC_except_table937
- GCC_except_table939
- GCC_except_table939
- GCC_except_table945
- GCC_except_table953
- GCC_except_table953
- GCC_except_table955
- GCC_except_table967
- GCC_except_table993
- GCC_except_table993
- GCC_except_table995
- GCC_except_table995
- GCC_except_table997
- OBJC_IVAR_$_FTApgBatchRecoverMessage._data
- OBJC_IVAR_$_FTApgBatchRecoverMessage._root
- OBJC_IVAR_$_FTApgBatchRecoverMessage._storage
- OBJC_IVAR_$_FTBatchRecoverFinalResponse._data
- OBJC_IVAR_$_FTBatchRecoverFinalResponse._root
- OBJC_IVAR_$_FTBatchRecoverFinalResponse._storage
- OBJC_IVAR_$_FTBatchRecoverStreamingContext._grpcContext
- OBJC_IVAR_$_FTBatchRecoverStreamingRequest._data
- OBJC_IVAR_$_FTBatchRecoverStreamingRequest._root
- OBJC_IVAR_$_FTBatchRecoverStreamingRequest._storage
- OBJC_IVAR_$_FTBatchRecoverStreamingResponse._data
- OBJC_IVAR_$_FTBatchRecoverStreamingResponse._root
- OBJC_IVAR_$_FTBatchRecoverStreamingResponse._storage
- OBJC_IVAR_$_FTMtStreamingTranslationMessage._data
- OBJC_IVAR_$_FTMtStreamingTranslationMessage._root
- OBJC_IVAR_$_FTMtStreamingTranslationMessage._storage
- OBJC_IVAR_$_FTStartBatchRecoverRequest._data
- OBJC_IVAR_$_FTStartBatchRecoverRequest._root
- OBJC_IVAR_$_FTStartBatchRecoverRequest._storage
- OBJC_IVAR_$_FTStreamingTranslationRequest._data
- OBJC_IVAR_$_FTStreamingTranslationRequest._root
- OBJC_IVAR_$_FTStreamingTranslationRequest._storage
- OBJC_IVAR_$_FTStreamingTranslationStreamingContext._grpcContext
- OBJC_IVAR_$_FTStreamingTranslationStreamingRequest._data
- OBJC_IVAR_$_FTStreamingTranslationStreamingRequest._root
- OBJC_IVAR_$_FTStreamingTranslationStreamingRequest._storage
- OBJC_IVAR_$_FTStreamingTranslationStreamingResponse._data
- OBJC_IVAR_$_FTStreamingTranslationStreamingResponse._root
- OBJC_IVAR_$_FTStreamingTranslationStreamingResponse._storage
- OBJC_IVAR_$__LTDConfigurationCache._queue
- OBJC_IVAR_$__LTOnlineTranslationEngine._assistantSettingsConnection
- OBJC_IVAR_$__LTOnlineTranslationEngine._dataSharingOptInStatus
- _OBJC_CLASS_$_AFSettingsConnection
- _OBJC_CLASS_$_FTApgBatchRecoverMessage
- _OBJC_CLASS_$_FTBatchRecoverFinalResponse
- _OBJC_CLASS_$_FTBatchRecoverStreamingContext
- _OBJC_CLASS_$_FTBatchRecoverStreamingRequest
- _OBJC_CLASS_$_FTBatchRecoverStreamingResponse
- _OBJC_CLASS_$_FTMtStreamingTranslationMessage
- _OBJC_CLASS_$_FTMutableApgBatchRecoverMessage
- _OBJC_CLASS_$_FTMutableBatchRecoverFinalResponse
- _OBJC_CLASS_$_FTMutableBatchRecoverStreamingRequest
- _OBJC_CLASS_$_FTMutableBatchRecoverStreamingResponse
- _OBJC_CLASS_$_FTMutableMtStreamingTranslationMessage
- _OBJC_CLASS_$_FTMutableStartBatchRecoverRequest
- _OBJC_CLASS_$_FTMutableStreamingTranslationRequest
- _OBJC_CLASS_$_FTMutableStreamingTranslationStreamingRequest
- _OBJC_CLASS_$_FTMutableStreamingTranslationStreamingResponse
- _OBJC_CLASS_$_FTStartBatchRecoverRequest
- _OBJC_CLASS_$_FTStreamingTranslationRequest
- _OBJC_CLASS_$_FTStreamingTranslationStreamingContext
- _OBJC_CLASS_$_FTStreamingTranslationStreamingRequest
- _OBJC_CLASS_$_FTStreamingTranslationStreamingResponse
- _OBJC_METACLASS_$_FTApgBatchRecoverMessage
- _OBJC_METACLASS_$_FTBatchRecoverFinalResponse
- _OBJC_METACLASS_$_FTBatchRecoverStreamingContext
- _OBJC_METACLASS_$_FTBatchRecoverStreamingRequest
- _OBJC_METACLASS_$_FTBatchRecoverStreamingResponse
- _OBJC_METACLASS_$_FTMtStreamingTranslationMessage
- _OBJC_METACLASS_$_FTMutableApgBatchRecoverMessage
- _OBJC_METACLASS_$_FTMutableBatchRecoverFinalResponse
- _OBJC_METACLASS_$_FTMutableBatchRecoverStreamingRequest
- _OBJC_METACLASS_$_FTMutableBatchRecoverStreamingResponse
- _OBJC_METACLASS_$_FTMutableMtStreamingTranslationMessage
- _OBJC_METACLASS_$_FTMutableStartBatchRecoverRequest
- _OBJC_METACLASS_$_FTMutableStreamingTranslationRequest
- _OBJC_METACLASS_$_FTMutableStreamingTranslationStreamingRequest
- _OBJC_METACLASS_$_FTMutableStreamingTranslationStreamingResponse
- _OBJC_METACLASS_$_FTStartBatchRecoverRequest
- _OBJC_METACLASS_$_FTStreamingTranslationRequest
- _OBJC_METACLASS_$_FTStreamingTranslationStreamingContext
- _OBJC_METACLASS_$_FTStreamingTranslationStreamingRequest
- _OBJC_METACLASS_$_FTStreamingTranslationStreamingResponse
- __48+[_LTDAssetService assetsForLocales:completion:]_block_invoke.107
- __48+[_LTDAssetService assetsForLocales:completion:]_block_invoke.cold.1
- __55+[_LTDConfigurationService configurationForType:error:]_block_invoke.35
- __55+[_LTDConfigurationService configurationForType:error:]_block_invoke.35.cold.1
- __57-[_LTOnlineTranslationEngine initWithSelfLoggingManager:]_block_invoke.cold.1
- __59+[_LTDLanguageAssetService _availableAssetsWithCompletion:]_block_invoke.cold.1
- __59+[_LTDLanguageAssetService _installedAssetsWithCompletion:]_block_invoke.cold.1
- __59-[_LTDConfigurationCache setObject:forType:ttl:completion:]_block_invoke.cold.1
- __59-[_LTOnlineTranslationEngine speak:withContext:completion:]_block_invoke.198
- __59-[_LTOnlineTranslationEngine speak:withContext:completion:]_block_invoke.198.cold.1
- __60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.44
- __60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.46
- __60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.47
- __60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.48
- __61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.38
- __61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.38.cold.1
- __61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.38.cold.2
- __66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.25
- __66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.30
- __66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.30.cold.1
- __LTDPreferencesConfigurationCacheTTL
- __OBJC_$_CLASS_METHODS_FTApgBatchRecoverMessage
- __OBJC_$_CLASS_METHODS_FTBatchRecoverStreamingRequest
- __OBJC_$_CLASS_METHODS_FTBatchRecoverStreamingResponse
- __OBJC_$_CLASS_METHODS_FTMtStreamingTranslationMessage
- __OBJC_$_CLASS_METHODS_FTMutableApgBatchRecoverMessage
- __OBJC_$_CLASS_METHODS_FTMutableBatchRecoverStreamingRequest
- __OBJC_$_CLASS_METHODS_FTMutableBatchRecoverStreamingResponse
- __OBJC_$_CLASS_METHODS_FTMutableMtStreamingTranslationMessage
- __OBJC_$_CLASS_METHODS_FTMutableStreamingTranslationStreamingRequest
- __OBJC_$_CLASS_METHODS_FTMutableStreamingTranslationStreamingResponse
- __OBJC_$_CLASS_METHODS_FTStreamingTranslationStreamingRequest
- __OBJC_$_CLASS_METHODS_FTStreamingTranslationStreamingResponse
- __OBJC_$_INSTANCE_METHODS_FTApgBatchRecoverMessage
- __OBJC_$_INSTANCE_METHODS_FTBatchRecoverFinalResponse
- __OBJC_$_INSTANCE_METHODS_FTBatchRecoverStreamingContext
- __OBJC_$_INSTANCE_METHODS_FTBatchRecoverStreamingRequest
- __OBJC_$_INSTANCE_METHODS_FTBatchRecoverStreamingResponse
- __OBJC_$_INSTANCE_METHODS_FTMtStreamingTranslationMessage
- __OBJC_$_INSTANCE_METHODS_FTMutableApgBatchRecoverMessage
- __OBJC_$_INSTANCE_METHODS_FTMutableBatchRecoverFinalResponse
- __OBJC_$_INSTANCE_METHODS_FTMutableBatchRecoverStreamingRequest
- __OBJC_$_INSTANCE_METHODS_FTMutableBatchRecoverStreamingResponse
- __OBJC_$_INSTANCE_METHODS_FTMutableMtStreamingTranslationMessage
- __OBJC_$_INSTANCE_METHODS_FTMutableStartBatchRecoverRequest
- __OBJC_$_INSTANCE_METHODS_FTMutableStreamingTranslationRequest
- __OBJC_$_INSTANCE_METHODS_FTMutableStreamingTranslationStreamingRequest
- __OBJC_$_INSTANCE_METHODS_FTMutableStreamingTranslationStreamingResponse
- __OBJC_$_INSTANCE_METHODS_FTStartBatchRecoverRequest
- __OBJC_$_INSTANCE_METHODS_FTStreamingTranslationRequest
- __OBJC_$_INSTANCE_METHODS_FTStreamingTranslationStreamingContext
- __OBJC_$_INSTANCE_METHODS_FTStreamingTranslationStreamingRequest
- __OBJC_$_INSTANCE_METHODS_FTStreamingTranslationStreamingResponse
- __OBJC_$_INSTANCE_VARIABLES_FTApgBatchRecoverMessage
- __OBJC_$_INSTANCE_VARIABLES_FTBatchRecoverFinalResponse
- __OBJC_$_INSTANCE_VARIABLES_FTBatchRecoverStreamingContext
- __OBJC_$_INSTANCE_VARIABLES_FTBatchRecoverStreamingRequest
- __OBJC_$_INSTANCE_VARIABLES_FTBatchRecoverStreamingResponse
- __OBJC_$_INSTANCE_VARIABLES_FTMtStreamingTranslationMessage
- __OBJC_$_INSTANCE_VARIABLES_FTStartBatchRecoverRequest
- __OBJC_$_INSTANCE_VARIABLES_FTStreamingTranslationRequest
- __OBJC_$_INSTANCE_VARIABLES_FTStreamingTranslationStreamingContext
- __OBJC_$_INSTANCE_VARIABLES_FTStreamingTranslationStreamingRequest
- __OBJC_$_INSTANCE_VARIABLES_FTStreamingTranslationStreamingResponse
- __OBJC_$_PROP_LIST_FTApgBatchRecoverMessage
- __OBJC_$_PROP_LIST_FTBatchRecoverFinalResponse
- __OBJC_$_PROP_LIST_FTBatchRecoverStreamingRequest
- __OBJC_$_PROP_LIST_FTBatchRecoverStreamingResponse
- __OBJC_$_PROP_LIST_FTMtStreamingTranslationMessage
- __OBJC_$_PROP_LIST_FTMutableApgBatchRecoverMessage
- __OBJC_$_PROP_LIST_FTMutableBatchRecoverFinalResponse
- __OBJC_$_PROP_LIST_FTMutableBatchRecoverStreamingRequest
- __OBJC_$_PROP_LIST_FTMutableBatchRecoverStreamingResponse
- __OBJC_$_PROP_LIST_FTMutableMtStreamingTranslationMessage
- __OBJC_$_PROP_LIST_FTMutableStartBatchRecoverRequest
- __OBJC_$_PROP_LIST_FTMutableStreamingTranslationRequest
- __OBJC_$_PROP_LIST_FTMutableStreamingTranslationStreamingRequest
- __OBJC_$_PROP_LIST_FTMutableStreamingTranslationStreamingResponse
- __OBJC_$_PROP_LIST_FTStartBatchRecoverRequest
- __OBJC_$_PROP_LIST_FTStreamingTranslationRequest
- __OBJC_$_PROP_LIST_FTStreamingTranslationStreamingRequest
- __OBJC_$_PROP_LIST_FTStreamingTranslationStreamingResponse
- __OBJC_CLASS_PROTOCOLS_$_FTApgBatchRecoverMessage
- __OBJC_CLASS_PROTOCOLS_$_FTBatchRecoverFinalResponse
- __OBJC_CLASS_PROTOCOLS_$_FTBatchRecoverStreamingRequest
- __OBJC_CLASS_PROTOCOLS_$_FTBatchRecoverStreamingResponse
- __OBJC_CLASS_PROTOCOLS_$_FTMtStreamingTranslationMessage
- __OBJC_CLASS_PROTOCOLS_$_FTStartBatchRecoverRequest
- __OBJC_CLASS_PROTOCOLS_$_FTStreamingTranslationRequest
- __OBJC_CLASS_PROTOCOLS_$_FTStreamingTranslationStreamingRequest
- __OBJC_CLASS_PROTOCOLS_$_FTStreamingTranslationStreamingResponse
- __OBJC_CLASS_RO_$_FTApgBatchRecoverMessage
- __OBJC_CLASS_RO_$_FTBatchRecoverFinalResponse
- __OBJC_CLASS_RO_$_FTBatchRecoverStreamingContext
- __OBJC_CLASS_RO_$_FTBatchRecoverStreamingRequest
- __OBJC_CLASS_RO_$_FTBatchRecoverStreamingResponse
- __OBJC_CLASS_RO_$_FTMtStreamingTranslationMessage
- __OBJC_CLASS_RO_$_FTMutableApgBatchRecoverMessage
- __OBJC_CLASS_RO_$_FTMutableBatchRecoverFinalResponse
- __OBJC_CLASS_RO_$_FTMutableBatchRecoverStreamingRequest
- __OBJC_CLASS_RO_$_FTMutableBatchRecoverStreamingResponse
- __OBJC_CLASS_RO_$_FTMutableMtStreamingTranslationMessage
- __OBJC_CLASS_RO_$_FTMutableStartBatchRecoverRequest
- __OBJC_CLASS_RO_$_FTMutableStreamingTranslationRequest
- __OBJC_CLASS_RO_$_FTMutableStreamingTranslationStreamingRequest
- __OBJC_CLASS_RO_$_FTMutableStreamingTranslationStreamingResponse
- __OBJC_CLASS_RO_$_FTStartBatchRecoverRequest
- __OBJC_CLASS_RO_$_FTStreamingTranslationRequest
- __OBJC_CLASS_RO_$_FTStreamingTranslationStreamingContext
- __OBJC_CLASS_RO_$_FTStreamingTranslationStreamingRequest
- __OBJC_CLASS_RO_$_FTStreamingTranslationStreamingResponse
- __OBJC_METACLASS_RO_$_FTApgBatchRecoverMessage
- __OBJC_METACLASS_RO_$_FTBatchRecoverFinalResponse
- __OBJC_METACLASS_RO_$_FTBatchRecoverStreamingContext
- __OBJC_METACLASS_RO_$_FTBatchRecoverStreamingRequest
- __OBJC_METACLASS_RO_$_FTBatchRecoverStreamingResponse
- __OBJC_METACLASS_RO_$_FTMtStreamingTranslationMessage
- __OBJC_METACLASS_RO_$_FTMutableApgBatchRecoverMessage
- __OBJC_METACLASS_RO_$_FTMutableBatchRecoverFinalResponse
- __OBJC_METACLASS_RO_$_FTMutableBatchRecoverStreamingRequest
- __OBJC_METACLASS_RO_$_FTMutableBatchRecoverStreamingResponse
- __OBJC_METACLASS_RO_$_FTMutableMtStreamingTranslationMessage
- __OBJC_METACLASS_RO_$_FTMutableStartBatchRecoverRequest
- __OBJC_METACLASS_RO_$_FTMutableStreamingTranslationRequest
- __OBJC_METACLASS_RO_$_FTMutableStreamingTranslationStreamingRequest
- __OBJC_METACLASS_RO_$_FTMutableStreamingTranslationStreamingResponse
- __OBJC_METACLASS_RO_$_FTStartBatchRecoverRequest
- __OBJC_METACLASS_RO_$_FTStreamingTranslationRequest
- __OBJC_METACLASS_RO_$_FTStreamingTranslationStreamingContext
- __OBJC_METACLASS_RO_$_FTStreamingTranslationStreamingRequest
- __OBJC_METACLASS_RO_$_FTStreamingTranslationStreamingResponse
- __ZNK4siri6speech6qss_fb22ApgBatchRecoverMessage6VerifyERN5apple4aiml12flatbuffers28VerifierE
- __ZNK4siri6speech6qss_fb28BatchRecoverStreamingRequest6VerifyERN5apple4aiml12flatbuffers28VerifierE
- __ZNK4siri6speech6qss_fb29BatchRecoverStreamingResponse6VerifyERN5apple4aiml12flatbuffers28VerifierE
- __ZNK4siri6speech6qss_fb29MtStreamingTranslationMessage6VerifyERN5apple4aiml12flatbuffers28VerifierE
- __ZNK4siri6speech6qss_fb36StreamingTranslationStreamingRequest6VerifyERN5apple4aiml12flatbuffers28VerifierE
- __ZNK4siri6speech6qss_fb37StreamingTranslationStreamingResponse6VerifyERN5apple4aiml12flatbuffers28VerifierE
- __ZNK4siri6speech9schema_fb24StartBatchRecoverRequest6VerifyERN5apple4aiml12flatbuffers28VerifierE
- __ZNK4siri6speech9schema_fb25BatchRecoverFinalResponse6VerifyERN5apple4aiml12flatbuffers28VerifierE
- __ZNK4siri6speech9schema_fb27StreamingTranslationRequest6VerifyERN5apple4aiml12flatbuffers28VerifierE
- ___37-[FTStartBatchRecoverRequest apg_ids]_block_invoke
- ___40-[FTApgBatchRecoverMessage flatbuffData]_block_invoke
- ___42-[FTStartBatchRecoverRequest flatbuffData]_block_invoke
- ___43-[FTBatchRecoverFinalResponse flatbuffData]_block_invoke
- ___45-[FTStreamingTranslationRequest flatbuffData]_block_invoke
- ___46-[FTBatchRecoverStreamingRequest flatbuffData]_block_invoke
- ___47-[FTBatchRecoverStreamingResponse flatbuffData]_block_invoke
- ___47-[FTMtStreamingTranslationMessage flatbuffData]_block_invoke
- ___48+[_LTDAssetService assetsForLocales:completion:]_block_invoke
- ___54-[FTStreamingTranslationStreamingRequest flatbuffData]_block_invoke
- ___55-[FTStreamingTranslationStreamingResponse flatbuffData]_block_invoke
- ___57-[_LTOnlineTranslationEngine initWithSelfLoggingManager:]_block_invoke
- ___59-[_LTDConfigurationCache setObject:forType:ttl:completion:]_block_invoke
- ___74-[FTApgService performBatchRecoverWithDelegate:requestBuilder:completion:]_block_invoke
- ___74-[FTApgService performBatchRecoverWithDelegate:requestBuilder:completion:]_block_invoke_2
- ___81-[FTMtService performStreamingTranslationWithDelegate:requestBuilder:completion:]_block_invoke
- ___81-[FTMtService performStreamingTranslationWithDelegate:requestBuilder:completion:]_block_invoke_2
- ___88+[_LTDLanguageAssetService _complementaryLocaleIfMissingForAssets:preferredComplements:]_block_invoke
- ___block_descriptor_40_e8_32bs_e51_v24?0"_LTDOfflineConfigurationModel"8"NSError"16l
- ___block_descriptor_40_ea8_32w_e20_v24?0"NSError"8q16l
- ___block_descriptor_48_e20_v24?0q8"NSError"16l
- ___block_descriptor_64_e8_32bs40w_e5_v8?0l
- __block_literal_global.15
- __block_literal_global.205
- __block_literal_global.21
- __block_literal_global.21
- __block_literal_global.42
- __block_literal_global.70
- _objc_msgSend$assetsForLocales:completion:
- _objc_msgSend$assetsForLocales:error:
- _objc_msgSend$container_messageAsFTApgBatchRecoverMessage
- _objc_msgSend$container_messageAsFTMtStreamingTranslationMessage
- _objc_msgSend$contentAsFTBatchRecoverFinalResponse
- _objc_msgSend$contentAsFTStartBatchRecoverRequest
- _objc_msgSend$contentAsFTStreamingTranslationRequest
- _objc_msgSend$contentAsFTTranslationResponse
- _objc_msgSend$getSiriDataSharingOptInStatusWithCompletion:
- _objc_msgSend$lt_initWithTask:inputMode:invocationType:explicitLanguageFilterEnabled:languageIdentificationEnabled:onDevice:translateAppContext:
- _objc_msgSend$num_of_processed
- _objc_msgSend$num_of_requested
- _objc_msgSend$num_of_succeeded
- _objc_msgSend$pair
- _objc_msgSend$session_messageAsFTBatchRecoverFinalResponse
- _objc_msgSend$session_messageAsFTStartBatchRecoverRequest
- _objc_msgSend$session_messageAsFTStreamingTranslationRequest
- _objc_msgSend$setAutoDownloadedAssets:
- _objc_msgSend$setObject:forType:ttl:completion:
- _objc_msgSend$startWithTask:inputMode:invocationType:interfaceMode:explicitLanguageFilterEnabled:languageIdentificationEnabled:onDevice:mtId:sessionId:translateAppContext:
- _objc_msgSend$streamDidReceiveBatchRecoverStreamingResponse:
- _objc_msgSend$streamDidReceiveStreamingTranslationStreamingResponse:
- _objc_msgSend$streamFailVerifyBatchRecoverStreamingResponse:
- _objc_msgSend$streamFailVerifyStreamingTranslationStreamingResponse:
- _objc_msgSend$subscribedVoices
- _objc_msgSend$translation_text
CStrings:
+ " | control-center"
+ "@\"_LTLanguageAssetModel\"16@?0@\"NSLocale\"8"
+ "DeviceSupportsGenerativeModelSystems"
+ "DisableSyncInstalledLocalesOnLaunch"
+ "TTS asset download failed for %!@(MISSING)"
+ "contains_masked_profanity"
+ "disable_payload_logging"
+ "engine_error_code"
+ "engine_error_message"
+ "mask_profanity"
+ "self_session_id"
- "/siri.speech.qss_fb.Apg/BatchRecover"
- "/siri.speech.qss_fb.Mt/StreamingTranslation"
- "ConfigurationCacheTTL"
- "TTS asset download failed for %!@(MISSING) [%!@(MISSING)]"
- "com.apple.translationd.ConfigurationCache"
- "num_of_processed"
- "num_of_requested"
- "num_of_succeeded"
- "translation_text"
- "v24@?0@\"NSError\"8q16"
- "v24@?0q8@\"NSError\"16"

```
