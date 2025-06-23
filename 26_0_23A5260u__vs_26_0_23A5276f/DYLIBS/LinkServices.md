## LinkServices

> `/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices`

```diff

-248.4.0.0.0
-  __TEXT.__text: 0x10681c
+254.0.0.0.0
+  __TEXT.__text: 0x1070a8
   __TEXT.__auth_stubs: 0x23d0
-  __TEXT.__objc_methlist: 0x9090
+  __TEXT.__objc_methlist: 0x9128
   __TEXT.__const: 0x58c8
   __TEXT.__dlopen_cstrs: 0x548
-  __TEXT.__cstring: 0xa4b5
+  __TEXT.__cstring: 0xa6df
   __TEXT.__constg_swiftt: 0x1270
   __TEXT.__swift5_typeref: 0x19aa
   __TEXT.__swift5_builtin: 0x12c

   __TEXT.__swift5_capture: 0x890
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__oslogstring: 0x59c4
-  __TEXT.__gcc_except_tab: 0x1efc
-  __TEXT.__unwind_info: 0x4ab0
-  __TEXT.__eh_frame: 0x4ef0
+  __TEXT.__oslogstring: 0x5af3
+  __TEXT.__gcc_except_tab: 0x1f78
+  __TEXT.__unwind_info: 0x4af0
+  __TEXT.__eh_frame: 0x4ef8
   __TEXT.__objc_classname: 0x1b68
-  __TEXT.__objc_methname: 0x14683
-  __TEXT.__objc_methtype: 0x3df9
-  __TEXT.__objc_stubs: 0xa4c0
-  __DATA_CONST.__got: 0x1448
-  __DATA_CONST.__const: 0x22a8
+  __TEXT.__objc_methname: 0x148ae
+  __TEXT.__objc_methtype: 0x3e94
+  __TEXT.__objc_stubs: 0xa560
+  __DATA_CONST.__got: 0x1450
+  __DATA_CONST.__const: 0x2290
   __DATA_CONST.__objc_classlist: 0x6d8
   __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4228
+  __DATA_CONST.__objc_selrefs: 0x4260
   __DATA_CONST.__objc_protorefs: 0xd0
-  __DATA_CONST.__objc_superrefs: 0x560
+  __DATA_CONST.__objc_superrefs: 0x558
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x11f8
   __AUTH_CONST.__const: 0x42f8
-  __AUTH_CONST.__cfstring: 0x7ae0
-  __AUTH_CONST.__objc_const: 0x12c68
-  __AUTH_CONST.__objc_intobj: 0x198
+  __AUTH_CONST.__cfstring: 0x7b20
+  __AUTH_CONST.__objc_const: 0x12d08
+  __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x2520
   __AUTH.__data: 0x9d0
-  __DATA.__objc_ivar: 0x958
-  __DATA.__data: 0x2248
+  __DATA.__objc_ivar: 0x964
+  __DATA.__data: 0x2288
   __DATA.__bss: 0x28d2
   __DATA.__common: 0x610
   __DATA_DIRTY.__objc_data: 0x2518
-  __DATA_DIRTY.__data: 0x820
+  __DATA_DIRTY.__data: 0x7f8
   __DATA_DIRTY.__bss: 0xf0
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D84E943F-6177-3949-AA3E-375C72E7579D
-  Functions: 7365
-  Symbols:   14240
-  CStrings:  6460
+  UUID: 533D3DE4-86D5-356D-B887-254EF9E70254
+  Functions: 7392
+  Symbols:   14283
+  CStrings:  6489
 
Symbols:
+ -[LNActionExecutor shouldDismissSiriWithDefault:]
+ -[LNActionExecutorOptions assistantDismissalPolicy]
+ -[LNActionExecutorOptions setAssistantDismissalPolicy:]
+ -[LNConnection optionsForAction:interactionMode:source:sourceOverride:assistantDismissalPolicy:]
+ -[LNConnection(FetchAppShortcutParameters) fetchAppShortcutParametersForMangledName:withCompletionHandler:]
+ -[LNConnectionPolicySignals description]
+ -[LNEmbeddedApplicationConnection optionsForAction:interactionMode:source:sourceOverride:assistantDismissalPolicy:]
+ -[LNEmbeddedApplicationConnectionOptions assistantDismissalPolicy]
+ -[LNEmbeddedApplicationConnectionOptions setAssistantDismissalPolicy:]
+ -[LNFetchAppShortcutParametersConnectionOperation appShortcutProviderMangledName]
+ -[LNFetchAppShortcutParametersConnectionOperation initWithConnectionInterface:queue:appShortcutProviderMangledName:completionHandler:]
+ -[LNFetchAppShortcutParametersConnectionOperation setAppShortcutProviderMangledName:]
+ -[LNMetadataProvider entityForBundleIdentifier:withEntityIdentifier:error:]
+ -[_LNMetadataProviderXPC entityForBundleIdentifier:withEntityIdentifier:error:]
+ GCC_except_table1030
+ GCC_except_table1104
+ GCC_except_table1143
+ GCC_except_table1146
+ GCC_except_table1159
+ GCC_except_table1199
+ GCC_except_table1202
+ GCC_except_table1264
+ GCC_except_table1302
+ GCC_except_table1376
+ GCC_except_table1408
+ GCC_except_table1491
+ GCC_except_table1513
+ GCC_except_table1514
+ GCC_except_table1515
+ GCC_except_table1527
+ GCC_except_table1528
+ GCC_except_table1558
+ GCC_except_table1564
+ GCC_except_table1566
+ GCC_except_table1579
+ GCC_except_table1584
+ GCC_except_table1593
+ GCC_except_table1597
+ GCC_except_table1670
+ GCC_except_table1674
+ GCC_except_table1730
+ GCC_except_table1739
+ GCC_except_table1745
+ GCC_except_table1778
+ GCC_except_table1810
+ GCC_except_table1824
+ GCC_except_table1854
+ GCC_except_table1903
+ GCC_except_table1906
+ GCC_except_table1934
+ GCC_except_table1951
+ GCC_except_table1969
+ GCC_except_table2040
+ GCC_except_table2047
+ GCC_except_table2067
+ GCC_except_table2077
+ GCC_except_table2080
+ GCC_except_table2094
+ GCC_except_table2095
+ GCC_except_table2125
+ GCC_except_table2161
+ GCC_except_table2175
+ GCC_except_table2176
+ GCC_except_table2362
+ GCC_except_table2363
+ GCC_except_table2364
+ GCC_except_table2365
+ GCC_except_table240
+ GCC_except_table2438
+ GCC_except_table2448
+ GCC_except_table2503
+ GCC_except_table2524
+ GCC_except_table2533
+ GCC_except_table2557
+ GCC_except_table2559
+ GCC_except_table2561
+ GCC_except_table2589
+ GCC_except_table2591
+ GCC_except_table2593
+ GCC_except_table2601
+ GCC_except_table2602
+ GCC_except_table2611
+ GCC_except_table2646
+ GCC_except_table2648
+ GCC_except_table2649
+ GCC_except_table2650
+ GCC_except_table2790
+ GCC_except_table2794
+ GCC_except_table2828
+ GCC_except_table2832
+ GCC_except_table2834
+ GCC_except_table2844
+ GCC_except_table2895
+ GCC_except_table2907
+ GCC_except_table2912
+ GCC_except_table2942
+ GCC_except_table317
+ GCC_except_table484
+ GCC_except_table489
+ GCC_except_table493
+ GCC_except_table496
+ GCC_except_table501
+ GCC_except_table504
+ GCC_except_table507
+ GCC_except_table510
+ GCC_except_table513
+ GCC_except_table516
+ GCC_except_table519
+ GCC_except_table522
+ GCC_except_table525
+ GCC_except_table528
+ GCC_except_table531
+ GCC_except_table534
+ GCC_except_table537
+ GCC_except_table540
+ GCC_except_table543
+ GCC_except_table546
+ GCC_except_table549
+ GCC_except_table552
+ GCC_except_table555
+ GCC_except_table558
+ GCC_except_table561
+ GCC_except_table564
+ GCC_except_table567
+ GCC_except_table570
+ GCC_except_table573
+ GCC_except_table576
+ GCC_except_table579
+ GCC_except_table582
+ GCC_except_table590
+ GCC_except_table592
+ GCC_except_table596
+ GCC_except_table598
+ GCC_except_table600
+ GCC_except_table602
+ GCC_except_table604
+ GCC_except_table606
+ GCC_except_table608
+ GCC_except_table610
+ GCC_except_table612
+ GCC_except_table632
+ GCC_except_table634
+ GCC_except_table636
+ GCC_except_table640
+ GCC_except_table642
+ GCC_except_table644
+ GCC_except_table646
+ GCC_except_table648
+ GCC_except_table650
+ GCC_except_table652
+ GCC_except_table654
+ GCC_except_table656
+ GCC_except_table658
+ GCC_except_table660
+ GCC_except_table662
+ GCC_except_table713
+ GCC_except_table737
+ GCC_except_table757
+ GCC_except_table820
+ GCC_except_table832
+ GCC_except_table835
+ GCC_except_table873
+ GCC_except_table919
+ GCC_except_table928
+ GCC_except_table931
+ GCC_except_table937
+ GCC_except_table944
+ GCC_except_table949
+ GCC_except_table979
+ GCC_except_table991
+ _DialogEngineLibraryCore.frameworkLibrary.12688
+ _DialogEngineLibraryCore.frameworkLibrary.5397
+ _DialogEngineLibraryCore.frameworkLibrary.5964
+ _DialogEngineLibraryCore.frameworkLibrary.7286
+ _LNAssistantDismissalPolicyAsString
+ _OBJC_IVAR_$_LNActionExecutorOptions._assistantDismissalPolicy
+ _OBJC_IVAR_$_LNEmbeddedApplicationConnectionOptions._assistantDismissalPolicy
+ _OBJC_IVAR_$_LNFetchAppShortcutParametersConnectionOperation._appShortcutProviderMangledName
+ ___107-[LNConnection(FetchAppShortcutParameters) fetchAppShortcutParametersForMangledName:withCompletionHandler:]_block_invoke
+ ___122-[LNEmbeddedApplicationConnection linkConnectionActionWithOpenApplicationIdentifier:connectionAction:connectionOperation:]_block_invoke.65
+ ___122-[LNEmbeddedApplicationConnection linkConnectionActionWithOpenApplicationIdentifier:connectionAction:connectionOperation:]_block_invoke.66
+ ___134-[LNFetchAppShortcutParametersConnectionOperation initWithConnectionInterface:queue:appShortcutProviderMangledName:completionHandler:]_block_invoke
+ ___50-[LNActionExecutor unsubscribeProgressObservation]_block_invoke
+ ___75-[LNMetadataProvider entityForBundleIdentifier:withEntityIdentifier:error:]_block_invoke
+ ___79-[_LNMetadataProviderXPC entityForBundleIdentifier:withEntityIdentifier:error:]_block_invoke
+ ___79-[_LNMetadataProviderXPC entityForBundleIdentifier:withEntityIdentifier:error:]_block_invoke_2
+ ___97-[LNEmbeddedApplicationConnection openApplicationWithOptions:connectionAction:completionHandler:]_block_invoke.55
+ ___97-[LNEmbeddedApplicationConnection openApplicationWithOptions:connectionAction:completionHandler:]_block_invoke.58
+ ___97-[LNEmbeddedApplicationConnection openApplicationWithOptions:connectionAction:completionHandler:]_block_invoke_2.59
+ ___Block_byref_object_copy_.10567
+ ___Block_byref_object_copy_.12765
+ ___Block_byref_object_copy_.14176
+ ___Block_byref_object_copy_.14816
+ ___Block_byref_object_copy_.2035
+ ___Block_byref_object_copy_.2677
+ ___Block_byref_object_copy_.5537
+ ___Block_byref_object_copy_.6811
+ ___Block_byref_object_copy_.7818
+ ___Block_byref_object_copy_.8766
+ ___Block_byref_object_dispose_.10568
+ ___Block_byref_object_dispose_.12766
+ ___Block_byref_object_dispose_.14177
+ ___Block_byref_object_dispose_.14817
+ ___Block_byref_object_dispose_.2036
+ ___Block_byref_object_dispose_.2678
+ ___Block_byref_object_dispose_.5538
+ ___Block_byref_object_dispose_.6812
+ ___Block_byref_object_dispose_.7819
+ ___Block_byref_object_dispose_.8767
+ ___DialogEngineLibraryCore_block_invoke.12689
+ ___DialogEngineLibraryCore_block_invoke.5398
+ ___DialogEngineLibraryCore_block_invoke.5965
+ ___DialogEngineLibraryCore_block_invoke.7287
+ ___block_descriptor_48_e8_32r40r_e38_v24?0"LNEntityMetadata"8"NSError"16lr32l8r40l8
+ ___block_literal_global.10081
+ ___block_literal_global.10556
+ ___block_literal_global.11000
+ ___block_literal_global.11081
+ ___block_literal_global.1133
+ ___block_literal_global.12096
+ ___block_literal_global.12216
+ ___block_literal_global.12287
+ ___block_literal_global.12343
+ ___block_literal_global.12772
+ ___block_literal_global.12808
+ ___block_literal_global.13318
+ ___block_literal_global.13668
+ ___block_literal_global.14147
+ ___block_literal_global.14434
+ ___block_literal_global.1468
+ ___block_literal_global.14767
+ ___block_literal_global.15039
+ ___block_literal_global.1515
+ ___block_literal_global.1654
+ ___block_literal_global.1718
+ ___block_literal_global.2038
+ ___block_literal_global.2532
+ ___block_literal_global.27.9512
+ ___block_literal_global.3112
+ ___block_literal_global.3227
+ ___block_literal_global.3573
+ ___block_literal_global.3631
+ ___block_literal_global.3885
+ ___block_literal_global.4015
+ ___block_literal_global.4122
+ ___block_literal_global.4233
+ ___block_literal_global.4326
+ ___block_literal_global.4512
+ ___block_literal_global.4574
+ ___block_literal_global.4807
+ ___block_literal_global.5173
+ ___block_literal_global.5219
+ ___block_literal_global.5362
+ ___block_literal_global.5392
+ ___block_literal_global.6127
+ ___block_literal_global.6160
+ ___block_literal_global.6545
+ ___block_literal_global.7350
+ ___block_literal_global.7472
+ ___block_literal_global.77
+ ___block_literal_global.79
+ ___block_literal_global.8316
+ ___block_literal_global.8808
+ ___block_literal_global.8959
+ ___block_literal_global.908
+ ___block_literal_global.9188
+ ___block_literal_global.9254
+ ___block_literal_global.9415
+ ___block_literal_global.9511
+ ___block_literal_global.9739
+ ___block_literal_global.9932
+ ___getCATClass_block_invoke.5395
+ ___getCATClass_block_invoke.5963
+ ___getCATClass_block_invoke.7285
+ ___kCFBooleanFalse
+ _audit_stringDialogEngine.12693
+ _audit_stringDialogEngine.5409
+ _audit_stringDialogEngine.5976
+ _audit_stringDialogEngine.7298
+ _getCATClass.softClass.5394
+ _getCATClass.softClass.5962
+ _getCATClass.softClass.7284
+ _objc_msgSend$appShortcutProviderMangledName
+ _objc_msgSend$assistantDismissalPolicy
+ _objc_msgSend$bundleLinkedOnOrAfter2025:
+ _objc_msgSend$entityForBundleIdentifier:withEntityIdentifier:error:
+ _objc_msgSend$entityForBundleIdentifier:withEntityIdentifier:reply:
+ _objc_msgSend$fetchAppShortcutParametersForMangledName:withCompletionHandler:
+ _objc_msgSend$initWithConnectionInterface:queue:appShortcutProviderMangledName:completionHandler:
+ _objc_msgSend$optionsForAction:interactionMode:source:sourceOverride:assistantDismissalPolicy:
+ _objc_msgSend$setAssistantDismissalPolicy:
+ _objc_msgSend$shouldDismissSiriWithDefault:
- +[LNConnection optionsForAction:interactionMode:source:sourceOverride:]
- +[LNConnectionPolicy bundleLinkedOnOrAfter2024:]
- +[LNEmbeddedApplicationConnection optionsForAction:interactionMode:source:sourceOverride:]
- -[LNFetchAppShortcutParametersConnectionOperation initWithConnectionInterface:queue:completionHandler:]
- GCC_except_table1023
- GCC_except_table1094
- GCC_except_table1133
- GCC_except_table1136
- GCC_except_table1149
- GCC_except_table1189
- GCC_except_table1192
- GCC_except_table1254
- GCC_except_table1282
- GCC_except_table1366
- GCC_except_table1398
- GCC_except_table1481
- GCC_except_table1494
- GCC_except_table1503
- GCC_except_table1505
- GCC_except_table1517
- GCC_except_table1518
- GCC_except_table1548
- GCC_except_table1554
- GCC_except_table1556
- GCC_except_table1569
- GCC_except_table1574
- GCC_except_table1583
- GCC_except_table1587
- GCC_except_table1660
- GCC_except_table1664
- GCC_except_table1720
- GCC_except_table1725
- GCC_except_table1729
- GCC_except_table1768
- GCC_except_table1800
- GCC_except_table1814
- GCC_except_table1834
- GCC_except_table1893
- GCC_except_table1896
- GCC_except_table1924
- GCC_except_table1941
- GCC_except_table1959
- GCC_except_table2036
- GCC_except_table2056
- GCC_except_table2065
- GCC_except_table2068
- GCC_except_table2070
- GCC_except_table2083
- GCC_except_table2113
- GCC_except_table2149
- GCC_except_table2163
- GCC_except_table2164
- GCC_except_table2348
- GCC_except_table2349
- GCC_except_table2350
- GCC_except_table2351
- GCC_except_table241
- GCC_except_table2410
- GCC_except_table2434
- GCC_except_table2489
- GCC_except_table2505
- GCC_except_table2510
- GCC_except_table2543
- GCC_except_table2545
- GCC_except_table2547
- GCC_except_table2575
- GCC_except_table2577
- GCC_except_table2579
- GCC_except_table2587
- GCC_except_table2588
- GCC_except_table2597
- GCC_except_table2621
- GCC_except_table2632
- GCC_except_table2634
- GCC_except_table2636
- GCC_except_table2776
- GCC_except_table2780
- GCC_except_table2814
- GCC_except_table2818
- GCC_except_table2820
- GCC_except_table2830
- GCC_except_table2881
- GCC_except_table2893
- GCC_except_table2898
- GCC_except_table2926
- GCC_except_table316
- GCC_except_table482
- GCC_except_table487
- GCC_except_table491
- GCC_except_table494
- GCC_except_table499
- GCC_except_table502
- GCC_except_table505
- GCC_except_table508
- GCC_except_table511
- GCC_except_table514
- GCC_except_table517
- GCC_except_table520
- GCC_except_table523
- GCC_except_table526
- GCC_except_table529
- GCC_except_table532
- GCC_except_table535
- GCC_except_table538
- GCC_except_table541
- GCC_except_table544
- GCC_except_table547
- GCC_except_table550
- GCC_except_table553
- GCC_except_table556
- GCC_except_table559
- GCC_except_table562
- GCC_except_table565
- GCC_except_table568
- GCC_except_table571
- GCC_except_table574
- GCC_except_table577
- GCC_except_table585
- GCC_except_table587
- GCC_except_table589
- GCC_except_table591
- GCC_except_table593
- GCC_except_table595
- GCC_except_table597
- GCC_except_table599
- GCC_except_table601
- GCC_except_table603
- GCC_except_table605
- GCC_except_table618
- GCC_except_table627
- GCC_except_table629
- GCC_except_table633
- GCC_except_table635
- GCC_except_table637
- GCC_except_table639
- GCC_except_table641
- GCC_except_table643
- GCC_except_table645
- GCC_except_table647
- GCC_except_table649
- GCC_except_table651
- GCC_except_table653
- GCC_except_table655
- GCC_except_table706
- GCC_except_table730
- GCC_except_table750
- GCC_except_table813
- GCC_except_table825
- GCC_except_table828
- GCC_except_table866
- GCC_except_table912
- GCC_except_table921
- GCC_except_table923
- GCC_except_table924
- GCC_except_table936
- GCC_except_table941
- GCC_except_table972
- GCC_except_table984
- _DialogEngineLibraryCore.frameworkLibrary.12656
- _DialogEngineLibraryCore.frameworkLibrary.5369
- _DialogEngineLibraryCore.frameworkLibrary.5934
- _DialogEngineLibraryCore.frameworkLibrary.7254
- __LSVersionNumberCompare
- __LSVersionNumberMakeWithString
- ___103-[LNFetchAppShortcutParametersConnectionOperation initWithConnectionInterface:queue:completionHandler:]_block_invoke
- ___122-[LNEmbeddedApplicationConnection linkConnectionActionWithOpenApplicationIdentifier:connectionAction:connectionOperation:]_block_invoke.59
- ___122-[LNEmbeddedApplicationConnection linkConnectionActionWithOpenApplicationIdentifier:connectionAction:connectionOperation:]_block_invoke.60
- ___97-[LNEmbeddedApplicationConnection openApplicationWithOptions:connectionAction:completionHandler:]_block_invoke.49
- ___97-[LNEmbeddedApplicationConnection openApplicationWithOptions:connectionAction:completionHandler:]_block_invoke.52
- ___97-[LNEmbeddedApplicationConnection openApplicationWithOptions:connectionAction:completionHandler:]_block_invoke_2.53
- ___Block_byref_object_copy_.10539
- ___Block_byref_object_copy_.12733
- ___Block_byref_object_copy_.14150
- ___Block_byref_object_copy_.14790
- ___Block_byref_object_copy_.2030
- ___Block_byref_object_copy_.2656
- ___Block_byref_object_copy_.5507
- ___Block_byref_object_copy_.6779
- ___Block_byref_object_copy_.7788
- ___Block_byref_object_copy_.8739
- ___Block_byref_object_dispose_.10540
- ___Block_byref_object_dispose_.12734
- ___Block_byref_object_dispose_.14151
- ___Block_byref_object_dispose_.14791
- ___Block_byref_object_dispose_.2031
- ___Block_byref_object_dispose_.2657
- ___Block_byref_object_dispose_.5508
- ___Block_byref_object_dispose_.6780
- ___Block_byref_object_dispose_.7789
- ___Block_byref_object_dispose_.8740
- ___DialogEngineLibraryCore_block_invoke.12657
- ___DialogEngineLibraryCore_block_invoke.5370
- ___DialogEngineLibraryCore_block_invoke.5935
- ___DialogEngineLibraryCore_block_invoke.7255
- ___block_literal_global.10066
- ___block_literal_global.105
- ___block_literal_global.10525
- ___block_literal_global.107
- ___block_literal_global.10969
- ___block_literal_global.11050
- ___block_literal_global.1136
- ___block_literal_global.12062
- ___block_literal_global.12183
- ___block_literal_global.12254
- ___block_literal_global.12310
- ___block_literal_global.12740
- ___block_literal_global.12776
- ___block_literal_global.13291
- ___block_literal_global.13642
- ___block_literal_global.14121
- ___block_literal_global.14408
- ___block_literal_global.1470
- ___block_literal_global.14741
- ___block_literal_global.15007
- ___block_literal_global.1517
- ___block_literal_global.1657
- ___block_literal_global.1720
- ___block_literal_global.2033
- ___block_literal_global.2512
- ___block_literal_global.27.9497
- ___block_literal_global.3088
- ___block_literal_global.3203
- ___block_literal_global.3548
- ___block_literal_global.3606
- ___block_literal_global.3865
- ___block_literal_global.3996
- ___block_literal_global.4103
- ___block_literal_global.4214
- ___block_literal_global.4303
- ___block_literal_global.4495
- ___block_literal_global.4557
- ___block_literal_global.4789
- ___block_literal_global.5141
- ___block_literal_global.5187
- ___block_literal_global.5334
- ___block_literal_global.5364
- ___block_literal_global.6097
- ___block_literal_global.6130
- ___block_literal_global.6513
- ___block_literal_global.7318
- ___block_literal_global.7441
- ___block_literal_global.8283
- ___block_literal_global.8781
- ___block_literal_global.8944
- ___block_literal_global.9173
- ___block_literal_global.920
- ___block_literal_global.9239
- ___block_literal_global.9400
- ___block_literal_global.9496
- ___block_literal_global.9724
- ___block_literal_global.9917
- ___getCATClass_block_invoke.5367
- ___getCATClass_block_invoke.5933
- ___getCATClass_block_invoke.7253
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_AppIntents_SQLite
- __swift_FORCE_LOAD_$_swiftDarwin_$_LinkServices
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AppIntents_SQLite
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_LinkServices
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AppIntents_SQLite
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_LinkServices
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AppIntents_SQLite
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_LinkServices
- _audit_stringDialogEngine.12661
- _audit_stringDialogEngine.5381
- _audit_stringDialogEngine.5946
- _audit_stringDialogEngine.7266
- _getCATClass.softClass.5366
- _getCATClass.softClass.5932
- _getCATClass.softClass.7252
- _objc_msgSend$SDKVersion
- _objc_msgSend$fetchAppShortcutParametersWithCompletionHandler:
- _objc_msgSend$numberWithUnsignedInt:
- _objc_msgSend$optionsForAction:interactionMode:source:sourceOverride:
- _objc_msgSend$platform
CStrings:
+ "%{public}@ App linked before 2025, sceneless = %{public}@"
+ "%{public}@ App linked on-or-after 2025, always launching sceneless"
+ "<%@: %p, authenticationPolicy: %@, sceneless: %@, activateSuspended: %@, openApplicationPriority: %@, allowsForegroundAppLaunchWhileInCarPlay: %@, initiatesAudioSession: %@, isCameraCapture:%@, actionSource: %@, assistantDismissalPolicy: %@>"
+ "<%@: %p, executionUUID: %@, clientLabel: %@, source: %@, sourceOverride: %@, kind: %@, interactionMode: %@, viewActionIdentifier: %@, donateToTranscript: %@, environment: %@, systemContext: %@, allowsPrepareBeforePerform: %@, requestUnlockIfNeeded: %@, preferNoticePresentation: %@, convertArrayResultToAsyncSequence: %@, useConstraintsEvaluator: %@, priority: %@, assistantDismissalPolicy: %@, allowLiveActivities: %@>"
+ "<%@: %p, preferredBundleIdentifier: %@, processInstanceIdentifier: %@, shouldExecuteActionOnApplicationBasedOnMetadata: %@>"
+ "<not provided>"
+ "@\"LNEntityMetadata\"40@0:8@\"NSString\"16@\"NSString\"24^@32"
+ "@52@0:8@16q24S32@36q44"
+ "B20@0:8B16"
+ "LinkServices/UTType+IntentPerson.swift"
+ "No app intents with identifier: "
+ "No app shortcuts provider mangled type name in bundle: "
+ "No entities with identifier: "
+ "No queries with identifier: "
+ "Requesting policy for entity: %{public}@ using signals: %{public}@"
+ "Requesting policy for intent: %{public}@ using signals: %{public}@"
+ "Requesting policy for query: %{public}@ using signals: %{public}@"
+ "T@\"NSString\",C,N,V_appShortcutProviderMangledName"
+ "Tq,N,V_assistantDismissalPolicy"
+ "Undefined content type for IntentPerson"
+ "_appShortcutProviderMangledName"
+ "_assistantDismissalPolicy"
+ "appintents:fetch specific entity metadata"
+ "assistantDismissalPolicy"
+ "bundleLinkedOnOrAfter2025:"
+ "dismissAssistant"
+ "entityForBundleIdentifier:withEntityIdentifier:error:"
+ "entityForBundleIdentifier:withEntityIdentifier:reply:"
+ "fetchAppShortcutParametersForMangledName:withCompletionHandler:"
+ "initWithConnectionInterface:queue:appShortcutProviderMangledName:completionHandler:"
+ "optionsForAction:interactionMode:source:sourceOverride:assistantDismissalPolicy:"
+ "retainAssistant"
+ "setAppShortcutProviderMangledName:"
+ "setAssistantDismissalPolicy:"
+ "shouldDismissSiriWithDefault:"
+ "v24@?0@\"LNEntityMetadata\"8@\"NSError\"16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSArray\"@\"NSArray\"@\"NSError\">24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"LNEntityMetadata\"@\"NSError\">32"
- "15.0"
- "18.0"
- "2.0"
- "<%@: %p, authenticationPolicy: %@, sceneless: %@, activateSuspended: %@, openApplicationPriority: %@, allowsForegroundAppLaunchWhileInCarPlay: %@, initiatesAudioSession: %@, isCameraCapture:%@, actionSource: %@>"
- "<%@: %p, executionUUID: %@, clientLabel: %@, source: %@, sourceOverride: %@, kind: %@, interactionMode: %@, viewActionIdentifier: %@, donateToTranscript: %@, environment: %@, systemContext: %@, allowsPrepareBeforePerform: %@, requestUnlockIfNeeded: %@, preferNoticePresentation: %@, convertArrayResultToAsyncSequence: %@, useConstraintsEvaluator: %@, priority: %@, allowLiveActivities: %@>"
- "@44@0:8@16q24S32@36"
- "Comparing %{public}@ to %{public}@"
- "No SDKVersion for %{public}@"
- "SDKVersion"
- "numberWithUnsignedInt:"
- "optionsForAction:interactionMode:source:sourceOverride:"
- "platform"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSArray\"@\"NSArray\"@\"NSError\">16"

```
