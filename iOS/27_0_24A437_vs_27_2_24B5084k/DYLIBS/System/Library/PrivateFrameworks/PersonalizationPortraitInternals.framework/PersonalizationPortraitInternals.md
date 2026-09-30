## PersonalizationPortraitInternals

> `/System/Library/PrivateFrameworks/PersonalizationPortraitInternals.framework/PersonalizationPortraitInternals`

```diff

-1346.0.1.0.0
-  __TEXT.__text: 0x18fa88
-  __TEXT.__objc_methlist: 0x143ec
-  __TEXT.__const: 0xdc6
+1351.0.0.0.0
+  __TEXT.__text: 0x191754
+  __TEXT.__objc_methlist: 0x14564
+  __TEXT.__const: 0xdd6
   __TEXT.__dlopen_cstrs: 0x302
   __TEXT.__constg_swiftt: 0x454
   __TEXT.__swift5_typeref: 0x5fa
   __TEXT.__swift5_fieldmd: 0x160
-  __TEXT.__cstring: 0x16d42
+  __TEXT.__cstring: 0x16dd5
   __TEXT.__swift5_capture: 0x14c
-  __TEXT.__oslogstring: 0x1aa6e
+  __TEXT.__oslogstring: 0x1af18
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_reflstr: 0x102
   __TEXT.__swift5_protos: 0x10

   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x4
-  __TEXT.__gcc_except_tab: 0x888c
+  __TEXT.__gcc_except_tab: 0x889c
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0x8028
-  __TEXT.__eh_frame: 0x2c8
+  __TEXT.__unwind_info: 0x8088
+  __TEXT.__eh_frame: 0x300
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x8838
-  __DATA_CONST.__objc_classlist: 0xa60
+  __DATA_CONST.__objc_classlist: 0xa70
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x218
+  __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xae68
+  __DATA_CONST.__objc_selrefs: 0xaf58
   __DATA_CONST.__objc_protorefs: 0x130
-  __DATA_CONST.__objc_superrefs: 0x718
+  __DATA_CONST.__objc_superrefs: 0x720
   __DATA_CONST.__objc_arraydata: 0x870
-  __DATA_CONST.__got: 0x1978
-  __AUTH_CONST.__const: 0x3708
+  __DATA_CONST.__got: 0x1998
+  __AUTH_CONST.__const: 0x3748
   __AUTH_CONST.__cfstring: 0x104a0
-  __AUTH_CONST.__objc_const: 0x1adf8
+  __AUTH_CONST.__objc_const: 0x1b100
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x17a0
   __AUTH_CONST.__objc_arrayobj: 0xb58
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__objc_doubleobj: 0xd0
-  __AUTH_CONST.__auth_got: 0xf20
-  __AUTH.__objc_data: 0x1370
-  __DATA.__objc_ivar: 0x1268
-  __DATA.__data: 0x1780
+  __AUTH_CONST.__auth_got: 0xf28
+  __AUTH.__objc_data: 0x1410
+  __DATA.__objc_ivar: 0x128c
+  __DATA.__data: 0x18a0
   __DATA_DIRTY.__objc_data: 0x5ae8
-  __DATA_DIRTY.__data: 0x4a8
-  __DATA_DIRTY.__bss: 0x740
+  __DATA_DIRTY.__data: 0x3e8
+  __DATA_DIRTY.__bss: 0x648
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8855
-  Symbols:   17276
-  CStrings:  4415
+  Functions: 8906
+  Symbols:   17388
+  CStrings:  4433
 
Symbols:
+ +[PPDefaultBrowserCheck sharedCheck]
+ +[PPHarvestingUtils effectiveRetentionWindowForDataSource:]
+ +[PPHarvestingUtils effectiveRetentionWindowForDataSource:deletionPolicy:]
+ +[PPHarvestingUtils shouldAdmitByAgeForBundleIdentifier:groupIdentifier:date:]
+ +[PPHarvestingUtils shouldAdmitByAgeForBundleIdentifier:groupIdentifier:date:deletionPolicy:]
+ +[PPHarvestingUtils shouldAdmitByAgeForBundleIdentifier:groupIdentifier:date:deletionPolicy:asOfDate:]
+ -[PPDefaultBrowserCheck .cxx_destruct]
+ -[PPDefaultBrowserCheck _currentDefaultBrowserBundleID]
+ -[PPDefaultBrowserCheck currentDefaultBrowserBundleID]
+ -[PPDefaultBrowserCheck initWithApplicationWorkspace:]
+ -[PPDefaultBrowserCheck initWithDefaultApplicationWorkspace]
+ -[PPDefaultBrowserCheck invalidateCachedDefaultBrowser]
+ -[PPDefaultBrowserCheck isBundleIDCurrentDefaultBrowser:]
+ -[PPLocalSocialHighlightStore invalidateSocialHighlightCacheForClient:]
+ -[PPSocialHighlightDefaultBrowserObserver observerDidObserveDatabaseChange:]
+ -[PPSocialHighlightServerRequestHandler _rankedHighlightsWithLimit:client:variant:queryId:requestQoS:additionalIdentifiers:]
+ -[PPSocialHighlightServerRequestHandler accessValue]
+ -[PPSocialHighlightServerRequestHandler applicationIdentifiersForCurrentRequest]
+ -[PPSocialHighlightServerRequestHandler clientBundleID]
+ -[PPSocialHighlightServerRequestHandler clientIsWebBrowser]
+ -[PPSocialHighlightServerRequestHandler externalEntitlement]
+ -[PPSocialHighlightServerRequestHandler internalEntitlement]
+ -[PPSocialHighlightServerRequestHandler setAccessValue:]
+ -[PPSocialHighlightServerRequestHandler setClientBundleID:]
+ -[PPSocialHighlightServerRequestHandler setClientIsWebBrowser:]
+ -[PPSocialHighlightServerRequestHandler setExternalEntitlement:]
+ -[PPSocialHighlightServerRequestHandler setInternalEntitlement:]
+ -[PPTTLDeletionPolicy effectiveMaxAgeForBundleIdentifier:groupIdentifier:]
+ GCC_except_table1000
+ GCC_except_table1001
+ GCC_except_table1027
+ GCC_except_table1028
+ GCC_except_table1029
+ GCC_except_table1031
+ GCC_except_table1033
+ GCC_except_table1034
+ GCC_except_table1047
+ GCC_except_table1048
+ GCC_except_table1081
+ GCC_except_table1087
+ GCC_except_table1089
+ GCC_except_table1096
+ GCC_except_table1109
+ GCC_except_table1128
+ GCC_except_table1130
+ GCC_except_table1132
+ GCC_except_table1134
+ GCC_except_table1136
+ GCC_except_table1138
+ GCC_except_table1147
+ GCC_except_table1159
+ GCC_except_table1176
+ GCC_except_table1185
+ GCC_except_table1189
+ GCC_except_table1190
+ GCC_except_table1196
+ GCC_except_table1198
+ GCC_except_table1206
+ GCC_except_table1224
+ GCC_except_table1231
+ GCC_except_table1234
+ GCC_except_table1236
+ GCC_except_table1238
+ GCC_except_table1252
+ GCC_except_table1267
+ GCC_except_table1284
+ GCC_except_table1293
+ GCC_except_table1295
+ GCC_except_table1300
+ GCC_except_table1318
+ GCC_except_table1370
+ GCC_except_table1392
+ GCC_except_table1402
+ GCC_except_table1505
+ GCC_except_table1506
+ GCC_except_table1507
+ GCC_except_table1508
+ GCC_except_table1513
+ GCC_except_table1519
+ GCC_except_table1521
+ GCC_except_table1522
+ GCC_except_table1523
+ GCC_except_table1524
+ GCC_except_table1527
+ GCC_except_table1560
+ GCC_except_table1587
+ GCC_except_table1684
+ GCC_except_table1688
+ GCC_except_table1692
+ GCC_except_table1696
+ GCC_except_table1699
+ GCC_except_table1710
+ GCC_except_table1714
+ GCC_except_table173
+ GCC_except_table1747
+ GCC_except_table1781
+ GCC_except_table1787
+ GCC_except_table1790
+ GCC_except_table1791
+ GCC_except_table1796
+ GCC_except_table1805
+ GCC_except_table1818
+ GCC_except_table1821
+ GCC_except_table1826
+ GCC_except_table1912
+ GCC_except_table1923
+ GCC_except_table1934
+ GCC_except_table1942
+ GCC_except_table1943
+ GCC_except_table1963
+ GCC_except_table1967
+ GCC_except_table1970
+ GCC_except_table1994
+ GCC_except_table1996
+ GCC_except_table2001
+ GCC_except_table2003
+ GCC_except_table2019
+ GCC_except_table2025
+ GCC_except_table2032
+ GCC_except_table2078
+ GCC_except_table2123
+ GCC_except_table2127
+ GCC_except_table2148
+ GCC_except_table2154
+ GCC_except_table2161
+ GCC_except_table2168
+ GCC_except_table2241
+ GCC_except_table276
+ GCC_except_table336
+ GCC_except_table337
+ GCC_except_table353
+ GCC_except_table371
+ GCC_except_table424
+ GCC_except_table4266
+ GCC_except_table4272
+ GCC_except_table428
+ GCC_except_table4364
+ GCC_except_table4365
+ GCC_except_table4366
+ GCC_except_table4367
+ GCC_except_table4368
+ GCC_except_table4370
+ GCC_except_table4374
+ GCC_except_table4375
+ GCC_except_table4378
+ GCC_except_table4379
+ GCC_except_table438
+ GCC_except_table4381
+ GCC_except_table4384
+ GCC_except_table4385
+ GCC_except_table4390
+ GCC_except_table4401
+ GCC_except_table4430
+ GCC_except_table4431
+ GCC_except_table4432
+ GCC_except_table4436
+ GCC_except_table4439
+ GCC_except_table4443
+ GCC_except_table4497
+ GCC_except_table4502
+ GCC_except_table4504
+ GCC_except_table4514
+ GCC_except_table4524
+ GCC_except_table4532
+ GCC_except_table4540
+ GCC_except_table4544
+ GCC_except_table4552
+ GCC_except_table4582
+ GCC_except_table4589
+ GCC_except_table4596
+ GCC_except_table4597
+ GCC_except_table4598
+ GCC_except_table4600
+ GCC_except_table4601
+ GCC_except_table4616
+ GCC_except_table4625
+ GCC_except_table4643
+ GCC_except_table4653
+ GCC_except_table4655
+ GCC_except_table4660
+ GCC_except_table4664
+ GCC_except_table471
+ GCC_except_table4748
+ GCC_except_table4756
+ GCC_except_table4762
+ GCC_except_table4888
+ GCC_except_table5011
+ GCC_except_table5024
+ GCC_except_table5027
+ GCC_except_table5038
+ GCC_except_table5052
+ GCC_except_table506
+ GCC_except_table5129
+ GCC_except_table5139
+ GCC_except_table5142
+ GCC_except_table5185
+ GCC_except_table5302
+ GCC_except_table5306
+ GCC_except_table5308
+ GCC_except_table5309
+ GCC_except_table5315
+ GCC_except_table5322
+ GCC_except_table5324
+ GCC_except_table5366
+ GCC_except_table5367
+ GCC_except_table5368
+ GCC_except_table5370
+ GCC_except_table5373
+ GCC_except_table5389
+ GCC_except_table5406
+ GCC_except_table5409
+ GCC_except_table5411
+ GCC_except_table5412
+ GCC_except_table5413
+ GCC_except_table5415
+ GCC_except_table5424
+ GCC_except_table5428
+ GCC_except_table5429
+ GCC_except_table5431
+ GCC_except_table5432
+ GCC_except_table5435
+ GCC_except_table5462
+ GCC_except_table5515
+ GCC_except_table5628
+ GCC_except_table5651
+ GCC_except_table5669
+ GCC_except_table5674
+ GCC_except_table5676
+ GCC_except_table5678
+ GCC_except_table5682
+ GCC_except_table5693
+ GCC_except_table5785
+ GCC_except_table5811
+ GCC_except_table5815
+ GCC_except_table5817
+ GCC_except_table5866
+ GCC_except_table5873
+ GCC_except_table5884
+ GCC_except_table5886
+ GCC_except_table5897
+ GCC_except_table6047
+ GCC_except_table6052
+ GCC_except_table6056
+ GCC_except_table6066
+ GCC_except_table6077
+ GCC_except_table6081
+ GCC_except_table6096
+ GCC_except_table6103
+ GCC_except_table6124
+ GCC_except_table6164
+ GCC_except_table6178
+ GCC_except_table6201
+ GCC_except_table6222
+ GCC_except_table6241
+ GCC_except_table6254
+ GCC_except_table6257
+ GCC_except_table6261
+ GCC_except_table6264
+ GCC_except_table6267
+ GCC_except_table6273
+ GCC_except_table6278
+ GCC_except_table6281
+ GCC_except_table6284
+ GCC_except_table6303
+ GCC_except_table6308
+ GCC_except_table6312
+ GCC_except_table6313
+ GCC_except_table6318
+ GCC_except_table6321
+ GCC_except_table6332
+ GCC_except_table6464
+ GCC_except_table6480
+ GCC_except_table6492
+ GCC_except_table6498
+ GCC_except_table6504
+ GCC_except_table6510
+ GCC_except_table6511
+ GCC_except_table6521
+ GCC_except_table6526
+ GCC_except_table6571
+ GCC_except_table6584
+ GCC_except_table6592
+ GCC_except_table6595
+ GCC_except_table6597
+ GCC_except_table6710
+ GCC_except_table6729
+ GCC_except_table6737
+ GCC_except_table6743
+ GCC_except_table6745
+ GCC_except_table6828
+ GCC_except_table6835
+ GCC_except_table6841
+ GCC_except_table6848
+ GCC_except_table6855
+ GCC_except_table6892
+ GCC_except_table6900
+ GCC_except_table6908
+ GCC_except_table6914
+ GCC_except_table6917
+ GCC_except_table6952
+ GCC_except_table6985
+ GCC_except_table6997
+ GCC_except_table7012
+ GCC_except_table7027
+ GCC_except_table7033
+ GCC_except_table7036
+ GCC_except_table7042
+ GCC_except_table7043
+ GCC_except_table7044
+ GCC_except_table7045
+ GCC_except_table7099
+ GCC_except_table7115
+ GCC_except_table7122
+ GCC_except_table7176
+ GCC_except_table7209
+ GCC_except_table7211
+ GCC_except_table7213
+ GCC_except_table7217
+ GCC_except_table7219
+ GCC_except_table7221
+ GCC_except_table7223
+ GCC_except_table7225
+ GCC_except_table7227
+ GCC_except_table7229
+ GCC_except_table7231
+ GCC_except_table7238
+ GCC_except_table7249
+ GCC_except_table7266
+ GCC_except_table7275
+ GCC_except_table730
+ GCC_except_table731
+ GCC_except_table733
+ GCC_except_table734
+ GCC_except_table7343
+ GCC_except_table7347
+ GCC_except_table7350
+ GCC_except_table7353
+ GCC_except_table7356
+ GCC_except_table7361
+ GCC_except_table7367
+ GCC_except_table7376
+ GCC_except_table7378
+ GCC_except_table7379
+ GCC_except_table738
+ GCC_except_table739
+ GCC_except_table7407
+ GCC_except_table7417
+ GCC_except_table7425
+ GCC_except_table7430
+ GCC_except_table7437
+ GCC_except_table744
+ GCC_except_table7440
+ GCC_except_table7454
+ GCC_except_table7477
+ GCC_except_table7485
+ GCC_except_table7526
+ GCC_except_table7558
+ GCC_except_table7640
+ GCC_except_table7659
+ GCC_except_table7670
+ GCC_except_table7673
+ GCC_except_table7675
+ GCC_except_table7680
+ GCC_except_table7689
+ GCC_except_table7695
+ GCC_except_table7701
+ GCC_except_table7703
+ GCC_except_table7705
+ GCC_except_table7724
+ GCC_except_table7731
+ GCC_except_table7740
+ GCC_except_table7801
+ GCC_except_table7944
+ GCC_except_table7946
+ GCC_except_table7948
+ GCC_except_table7950
+ GCC_except_table7968
+ GCC_except_table7970
+ GCC_except_table7972
+ GCC_except_table7974
+ GCC_except_table7976
+ GCC_except_table7979
+ GCC_except_table7986
+ GCC_except_table7988
+ GCC_except_table7990
+ GCC_except_table7992
+ GCC_except_table7994
+ GCC_except_table7996
+ GCC_except_table7998
+ GCC_except_table8000
+ GCC_except_table8029
+ GCC_except_table8079
+ GCC_except_table8194
+ GCC_except_table8279
+ GCC_except_table8326
+ GCC_except_table8349
+ GCC_except_table8351
+ GCC_except_table8353
+ GCC_except_table8355
+ GCC_except_table8357
+ GCC_except_table8362
+ GCC_except_table8377
+ GCC_except_table8394
+ GCC_except_table923
+ GCC_except_table924
+ GCC_except_table928
+ GCC_except_table929
+ GCC_except_table930
+ GCC_except_table931
+ GCC_except_table934
+ GCC_except_table935
+ GCC_except_table938
+ GCC_except_table964
+ GCC_except_table970
+ GCC_except_table971
+ GCC_except_table982
+ GCC_except_table989
+ GCC_except_table990
+ GCC_except_table991
+ GCC_except_table992
+ GCC_except_table993
+ GCC_except_table996
+ GCC_except_table997
+ GCC_except_table998
+ GCC_except_table999
+ _OBJC_CLASS_$_LSObserver
+ _OBJC_CLASS_$_PPDefaultBrowserCheck
+ _OBJC_CLASS_$_PPSocialHighlightDefaultBrowserObserver
+ _OBJC_IVAR_$_PPDefaultBrowserCheck._cachedDefaultBrowserBundleID
+ _OBJC_IVAR_$_PPDefaultBrowserCheck._generation
+ _OBJC_IVAR_$_PPDefaultBrowserCheck._hasCachedDefaultBrowser
+ _OBJC_IVAR_$_PPDefaultBrowserCheck._lock
+ _OBJC_IVAR_$_PPDefaultBrowserCheck._workspace
+ _OBJC_IVAR_$_PPSocialHighlightServerRequestHandler._accessValue
+ _OBJC_IVAR_$_PPSocialHighlightServerRequestHandler._clientBundleID
+ _OBJC_IVAR_$_PPSocialHighlightServerRequestHandler._clientIsWebBrowser
+ _OBJC_IVAR_$_PPSocialHighlightServerRequestHandler._externalEntitlement
+ _OBJC_IVAR_$_PPSocialHighlightServerRequestHandler._internalEntitlement
+ _OBJC_METACLASS_$_PPDefaultBrowserCheck
+ _OBJC_METACLASS_$_PPSocialHighlightDefaultBrowserObserver
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_50
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _PPBuildApplicationIdentifiers
+ _PPSocialHighlightHandleDefaultBrowserChange
+ _PPSocialHighlightResetDefaultBrowserChangeTrackingForTesting
+ __OBJC_$_CLASS_METHODS_PPDefaultBrowserCheck
+ __OBJC_$_INSTANCE_METHODS_PPDefaultBrowserCheck
+ __OBJC_$_INSTANCE_METHODS_PPSocialHighlightDefaultBrowserObserver
+ __OBJC_$_INSTANCE_VARIABLES_PPDefaultBrowserCheck
+ __OBJC_$_PROP_LIST_PPSocialHighlightDefaultBrowserObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LSObserverDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LSObserverDelegate
+ __OBJC_$_PROTOCOL_REFS_LSObserverDelegate
+ __OBJC_CLASS_PROTOCOLS_$_PPSocialHighlightDefaultBrowserObserver
+ __OBJC_CLASS_RO_$_PPDefaultBrowserCheck
+ __OBJC_CLASS_RO_$_PPSocialHighlightDefaultBrowserObserver
+ __OBJC_LABEL_PROTOCOL_$_LSObserverDelegate
+ __OBJC_METACLASS_RO_$_PPDefaultBrowserCheck
+ __OBJC_METACLASS_RO_$_PPSocialHighlightDefaultBrowserObserver
+ __OBJC_PROTOCOL_$_LSObserverDelegate
+ __PPCachedDefaultTTLPolicy
+ __PPCachedDefaultTTLPolicy.cachedPolicy
+ __PPCachedDefaultTTLPolicy.cachedPolicyLock
+ ___124-[PPSocialHighlightServerRequestHandler _rankedHighlightsWithLimit:client:variant:queryId:requestQoS:additionalIdentifiers:]_block_invoke
+ ___124-[PPSocialHighlightServerRequestHandler _rankedHighlightsWithLimit:client:variant:queryId:requestQoS:additionalIdentifiers:]_block_invoke_2
+ ___124-[PPSocialHighlightServerRequestHandler _rankedHighlightsWithLimit:client:variant:queryId:requestQoS:additionalIdentifiers:]_block_invoke_3
+ ___124-[PPSocialHighlightServerRequestHandler _rankedHighlightsWithLimit:client:variant:queryId:requestQoS:additionalIdentifiers:]_block_invoke_4
+ ___124-[PPSocialHighlightServerRequestHandler _rankedHighlightsWithLimit:client:variant:queryId:requestQoS:additionalIdentifiers:]_block_invoke_5
+ ___36+[PPDefaultBrowserCheck sharedCheck]_block_invoke
+ ___39-[PPSocialHighlightServerDelegate init]_block_invoke
+ ___block_descriptor_65_e8_32s40s48s_e48_v16?0"PPConnectionsScoredLocationGuardedData"8ls32l8s40l8s48l8
+ __handleCloudStorageDeletedByUser._pasOnceToken16
+ __os_feature_enabled_simple_impl
+ __rankedHighlightsWithLimit:client:variant:queryId:requestQoS:additionalIdentifiers:._pasExprOnceResult
+ __rankedHighlightsWithLimit:client:variant:queryId:requestQoS:additionalIdentifiers:._pasOnceToken3
+ __triggerDelayedOperationWithCoalescingToken:operation:._pasOnceToken35
+ _init.lsObserver
+ _init.observer
+ _init.onceToken
+ _kPPCanLearnFromAppKey_block_invoke._pasOnceToken25
+ _kTCCServiceSiriAccess
+ _objc_msgSend$_currentDefaultBrowserBundleID
+ _objc_msgSend$_rankedHighlightsWithLimit:client:variant:queryId:requestQoS:additionalIdentifiers:
+ _objc_msgSend$accessValue
+ _objc_msgSend$applicationIdentifiersForCurrentRequest
+ _objc_msgSend$clientBundleID
+ _objc_msgSend$clientIsWebBrowser
+ _objc_msgSend$currentDefaultBrowserBundleID
+ _objc_msgSend$defaultApplicationForCategory:error:
+ _objc_msgSend$effectiveMaxAgeForBundleIdentifier:groupIdentifier:
+ _objc_msgSend$effectiveRetentionWindowForDataSource:
+ _objc_msgSend$effectiveRetentionWindowForDataSource:deletionPolicy:
+ _objc_msgSend$externalEntitlement
+ _objc_msgSend$initWithDefaultApplicationWorkspace
+ _objc_msgSend$internalEntitlement
+ _objc_msgSend$invalidateCachedDefaultBrowser
+ _objc_msgSend$invalidateSocialHighlightCacheForClient:
+ _objc_msgSend$isBundleIDCurrentDefaultBrowser:
+ _objc_msgSend$registerMaxContentAge:oneDataSource:
+ _objc_msgSend$setAccessValue:
+ _objc_msgSend$setClientBundleID:
+ _objc_msgSend$setClientIsWebBrowser:
+ _objc_msgSend$setExternalEntitlement:
+ _objc_msgSend$setInternalEntitlement:
+ _objc_msgSend$sharedCheck
+ _objc_msgSend$shouldAdmitByAgeForBundleIdentifier:groupIdentifier:date:
+ _objc_msgSend$shouldAdmitByAgeForBundleIdentifier:groupIdentifier:date:deletionPolicy:
+ _objc_msgSend$shouldAdmitByAgeForBundleIdentifier:groupIdentifier:date:deletionPolicy:asOfDate:
+ _objc_msgSend$startObserving
+ _sHasHandledBrowserChange
+ _sLastHandledBrowserBundleID
+ _sLastHandledBrowserLock
+ _sharedCheck.onceToken
+ _sharedCheck.sharedCheck
- -[PPSocialHighlightServerRequestHandler applicationIdentifiers]
- -[PPSocialHighlightServerRequestHandler setApplicationIdentifiers:]
- GCC_except_table1009
- GCC_except_table1023
- GCC_except_table1024
- GCC_except_table1057
- GCC_except_table1061
- GCC_except_table1063
- GCC_except_table1065
- GCC_except_table1072
- GCC_except_table1104
- GCC_except_table1106
- GCC_except_table1108
- GCC_except_table1110
- GCC_except_table1112
- GCC_except_table1114
- GCC_except_table1123
- GCC_except_table1135
- GCC_except_table1152
- GCC_except_table1161
- GCC_except_table1165
- GCC_except_table1166
- GCC_except_table1172
- GCC_except_table1174
- GCC_except_table1182
- GCC_except_table1200
- GCC_except_table1204
- GCC_except_table1207
- GCC_except_table1210
- GCC_except_table1212
- GCC_except_table1214
- GCC_except_table1242
- GCC_except_table1259
- GCC_except_table1268
- GCC_except_table1270
- GCC_except_table1275
- GCC_except_table1292
- GCC_except_table1344
- GCC_except_table1366
- GCC_except_table1376
- GCC_except_table1479
- GCC_except_table1480
- GCC_except_table1481
- GCC_except_table1482
- GCC_except_table1487
- GCC_except_table1493
- GCC_except_table1495
- GCC_except_table1496
- GCC_except_table1497
- GCC_except_table1498
- GCC_except_table1501
- GCC_except_table1528
- GCC_except_table1555
- GCC_except_table157
- GCC_except_table1646
- GCC_except_table1652
- GCC_except_table1656
- GCC_except_table1660
- GCC_except_table1664
- GCC_except_table1667
- GCC_except_table1682
- GCC_except_table1715
- GCC_except_table1749
- GCC_except_table1755
- GCC_except_table1758
- GCC_except_table1759
- GCC_except_table1764
- GCC_except_table1773
- GCC_except_table1786
- GCC_except_table1789
- GCC_except_table1794
- GCC_except_table1880
- GCC_except_table1891
- GCC_except_table1902
- GCC_except_table1910
- GCC_except_table1911
- GCC_except_table1931
- GCC_except_table1935
- GCC_except_table1938
- GCC_except_table1962
- GCC_except_table1964
- GCC_except_table1969
- GCC_except_table1971
- GCC_except_table1987
- GCC_except_table1993
- GCC_except_table2000
- GCC_except_table2046
- GCC_except_table2091
- GCC_except_table2095
- GCC_except_table2116
- GCC_except_table2122
- GCC_except_table2129
- GCC_except_table2136
- GCC_except_table2209
- GCC_except_table252
- GCC_except_table312
- GCC_except_table313
- GCC_except_table329
- GCC_except_table347
- GCC_except_table400
- GCC_except_table404
- GCC_except_table414
- GCC_except_table4234
- GCC_except_table4240
- GCC_except_table4332
- GCC_except_table4333
- GCC_except_table4334
- GCC_except_table4335
- GCC_except_table4336
- GCC_except_table4337
- GCC_except_table4338
- GCC_except_table4342
- GCC_except_table4343
- GCC_except_table4346
- GCC_except_table4347
- GCC_except_table4349
- GCC_except_table4352
- GCC_except_table4353
- GCC_except_table4358
- GCC_except_table4398
- GCC_except_table4399
- GCC_except_table4400
- GCC_except_table4404
- GCC_except_table4407
- GCC_except_table4411
- GCC_except_table4465
- GCC_except_table447
- GCC_except_table4470
- GCC_except_table4472
- GCC_except_table4482
- GCC_except_table4488
- GCC_except_table4492
- GCC_except_table4500
- GCC_except_table4508
- GCC_except_table4512
- GCC_except_table4518
- GCC_except_table4537
- GCC_except_table4557
- GCC_except_table4561
- GCC_except_table4564
- GCC_except_table4565
- GCC_except_table4566
- GCC_except_table4568
- GCC_except_table4584
- GCC_except_table4611
- GCC_except_table4621
- GCC_except_table4623
- GCC_except_table4628
- GCC_except_table4632
- GCC_except_table4716
- GCC_except_table4724
- GCC_except_table4730
- GCC_except_table482
- GCC_except_table4856
- GCC_except_table4979
- GCC_except_table4992
- GCC_except_table4995
- GCC_except_table5006
- GCC_except_table5020
- GCC_except_table5097
- GCC_except_table5107
- GCC_except_table5110
- GCC_except_table5153
- GCC_except_table5270
- GCC_except_table5274
- GCC_except_table5276
- GCC_except_table5277
- GCC_except_table5283
- GCC_except_table5290
- GCC_except_table5292
- GCC_except_table5325
- GCC_except_table5334
- GCC_except_table5335
- GCC_except_table5336
- GCC_except_table5338
- GCC_except_table5341
- GCC_except_table5360
- GCC_except_table5374
- GCC_except_table5377
- GCC_except_table5379
- GCC_except_table5380
- GCC_except_table5381
- GCC_except_table5383
- GCC_except_table5396
- GCC_except_table5397
- GCC_except_table5398
- GCC_except_table5399
- GCC_except_table5400
- GCC_except_table5403
- GCC_except_table5483
- GCC_except_table5595
- GCC_except_table5603
- GCC_except_table5610
- GCC_except_table5618
- GCC_except_table5641
- GCC_except_table5645
- GCC_except_table5649
- GCC_except_table5660
- GCC_except_table5745
- GCC_except_table5752
- GCC_except_table5782
- GCC_except_table5784
- GCC_except_table5833
- GCC_except_table5840
- GCC_except_table5851
- GCC_except_table5853
- GCC_except_table5864
- GCC_except_table6014
- GCC_except_table6019
- GCC_except_table6023
- GCC_except_table6033
- GCC_except_table6044
- GCC_except_table6048
- GCC_except_table6063
- GCC_except_table6070
- GCC_except_table6091
- GCC_except_table6131
- GCC_except_table6145
- GCC_except_table6156
- GCC_except_table6168
- GCC_except_table6175
- GCC_except_table6182
- GCC_except_table6207
- GCC_except_table6212
- GCC_except_table6218
- GCC_except_table6221
- GCC_except_table6224
- GCC_except_table6228
- GCC_except_table6231
- GCC_except_table6234
- GCC_except_table6237
- GCC_except_table6275
- GCC_except_table6279
- GCC_except_table6280
- GCC_except_table6285
- GCC_except_table6288
- GCC_except_table6299
- GCC_except_table6398
- GCC_except_table6422
- GCC_except_table6445
- GCC_except_table6447
- GCC_except_table6459
- GCC_except_table6465
- GCC_except_table6471
- GCC_except_table6477
- GCC_except_table6493
- GCC_except_table6537
- GCC_except_table6550
- GCC_except_table6558
- GCC_except_table6561
- GCC_except_table6563
- GCC_except_table6676
- GCC_except_table6695
- GCC_except_table6703
- GCC_except_table6709
- GCC_except_table6711
- GCC_except_table6794
- GCC_except_table6801
- GCC_except_table6807
- GCC_except_table6814
- GCC_except_table6821
- GCC_except_table6858
- GCC_except_table6866
- GCC_except_table6874
- GCC_except_table6880
- GCC_except_table6883
- GCC_except_table6918
- GCC_except_table6951
- GCC_except_table6963
- GCC_except_table6974
- GCC_except_table6978
- GCC_except_table6993
- GCC_except_table6999
- GCC_except_table7002
- GCC_except_table7009
- GCC_except_table7010
- GCC_except_table7011
- GCC_except_table706
- GCC_except_table7065
- GCC_except_table707
- GCC_except_table7081
- GCC_except_table7088
- GCC_except_table709
- GCC_except_table710
- GCC_except_table714
- GCC_except_table7142
- GCC_except_table715
- GCC_except_table7157
- GCC_except_table7175
- GCC_except_table7177
- GCC_except_table7179
- GCC_except_table7181
- GCC_except_table7183
- GCC_except_table7185
- GCC_except_table7187
- GCC_except_table7189
- GCC_except_table7193
- GCC_except_table7195
- GCC_except_table7197
- GCC_except_table720
- GCC_except_table7204
- GCC_except_table7232
- GCC_except_table7241
- GCC_except_table7309
- GCC_except_table7313
- GCC_except_table7316
- GCC_except_table7319
- GCC_except_table7322
- GCC_except_table7327
- GCC_except_table7333
- GCC_except_table7342
- GCC_except_table7344
- GCC_except_table7345
- GCC_except_table7372
- GCC_except_table7373
- GCC_except_table7383
- GCC_except_table7386
- GCC_except_table7391
- GCC_except_table7396
- GCC_except_table7403
- GCC_except_table7443
- GCC_except_table7451
- GCC_except_table7492
- GCC_except_table7524
- GCC_except_table7606
- GCC_except_table7625
- GCC_except_table7636
- GCC_except_table7639
- GCC_except_table7641
- GCC_except_table7646
- GCC_except_table7655
- GCC_except_table7661
- GCC_except_table7667
- GCC_except_table7669
- GCC_except_table7671
- GCC_except_table7690
- GCC_except_table7697
- GCC_except_table7706
- GCC_except_table7767
- GCC_except_table7778
- GCC_except_table7782
- GCC_except_table7784
- GCC_except_table7786
- GCC_except_table7788
- GCC_except_table7790
- GCC_except_table7792
- GCC_except_table7794
- GCC_except_table7796
- GCC_except_table7798
- GCC_except_table7800
- GCC_except_table7802
- GCC_except_table7804
- GCC_except_table7806
- GCC_except_table7808
- GCC_except_table7810
- GCC_except_table7814
- GCC_except_table7945
- GCC_except_table7995
- GCC_except_table8045
- GCC_except_table8160
- GCC_except_table8245
- GCC_except_table8292
- GCC_except_table8315
- GCC_except_table8317
- GCC_except_table8319
- GCC_except_table8321
- GCC_except_table8323
- GCC_except_table8328
- GCC_except_table8343
- GCC_except_table8360
- GCC_except_table899
- GCC_except_table900
- GCC_except_table904
- GCC_except_table905
- GCC_except_table906
- GCC_except_table907
- GCC_except_table910
- GCC_except_table911
- GCC_except_table914
- GCC_except_table940
- GCC_except_table942
- GCC_except_table943
- GCC_except_table946
- GCC_except_table947
- GCC_except_table949
- GCC_except_table950
- GCC_except_table956
- GCC_except_table958
- GCC_except_table962
- GCC_except_table965
- GCC_except_table968
- GCC_except_table969
- GCC_except_table972
- GCC_except_table975
- GCC_except_table976
- GCC_except_table977
- GCC_except_table979
- GCC_except_table981
- GCC_except_table983
- _OBJC_IVAR_$_PPSocialHighlightServerRequestHandler._applicationIdentifiers
- ___101-[PPSocialHighlightServerRequestHandler rankedHighlightsWithLimit:client:variant:queryId:requestQoS:]_block_invoke
- ___101-[PPSocialHighlightServerRequestHandler rankedHighlightsWithLimit:client:variant:queryId:requestQoS:]_block_invoke_2
- ___101-[PPSocialHighlightServerRequestHandler rankedHighlightsWithLimit:client:variant:queryId:requestQoS:]_block_invoke_3
- ___101-[PPSocialHighlightServerRequestHandler rankedHighlightsWithLimit:client:variant:queryId:requestQoS:]_block_invoke_4
- ___101-[PPSocialHighlightServerRequestHandler rankedHighlightsWithLimit:client:variant:queryId:requestQoS:]_block_invoke_5
- ___block_descriptor_56_e8_32s40s_e48_v16?0"PPConnectionsScoredLocationGuardedData"8ls32l8s40l8
- __handleCloudStorageDeletedByUser._pasOnceToken15
- __triggerDelayedOperationWithCoalescingToken:operation:._pasOnceToken33
- _kPPCanLearnFromAppKey_block_invoke._pasOnceToken24
- _objc_msgSend$rankedHighlightsWithLimit:client:variant:queryId:requestQoS:
- _rankedHighlightsWithLimit:client:variant:queryId:requestQoS:._pasExprOnceResult
- _rankedHighlightsWithLimit:client:variant:queryId:requestQoS:._pasOnceToken3
CStrings:
+ "AppExclusions"
+ "IntelligenceFlow"
+ "PPDefaultBrowserCheck: no application workspace; not treating %{public}@ as default browser"
+ "PPDefaultBrowserCheck: no client bundle identifier; not treating client as default browser"
+ "PPDefaultBrowserCheck: no current default browser (%{public}@)"
+ "PPHarvestingUtils: age gate fail-open for bundle %@ group %@ (date=%@)"
+ "PPHarvestingUtils: age gate skip bundle %@ group %@ age=%.0fs window=%.0fs"
+ "PPLocalSocialHighlightStore: invalidateSocialHighlightCacheForClient: %@"
+ "PPSettings failed to register TCC access change handler."
+ "PPSettings failed to register TCC access change purge handler."
+ "PPSocialHighlightServer: default browser changed from %{public}@ to %{public}@, invalidating cache for those clients only"
+ "PPSocialHighlightServer: granting all-links wildcard to current default browser %{public}@"
+ "PPSocialHighlightServer: observed LaunchServices database change"
+ "PPSocialHighlightServer: rankedHighlightsForSyncedItems applicationIdentifiers: %@"
+ "PPSocialHighlightServer: rankedHighlightsWithLimit applicationIdentifiers: %@"
+ "PPSocialHighlightServer: validateConnection clientBundleID: %@ accessValue: %@ internal: %d external: %d webBrowser: %d"
+ "PPSocialHighlightServer: withholding all-links wildcard from browser client %{public}@ (not the current default browser)"
+ "ThirdPartyBrowserSyndication"
+ "com.apple.proactive.PersonalizationPortrait.SocialHighlight.defaultBrowserDidChange"
- "PPSocialHighlightServer: validateConnection applicationIdentifiers: %@"
```
