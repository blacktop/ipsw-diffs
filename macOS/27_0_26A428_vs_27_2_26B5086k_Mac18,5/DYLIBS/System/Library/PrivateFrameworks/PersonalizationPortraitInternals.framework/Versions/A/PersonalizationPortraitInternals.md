## PersonalizationPortraitInternals

> `/System/Library/PrivateFrameworks/PersonalizationPortraitInternals.framework/Versions/A/PersonalizationPortraitInternals`

```diff

-1345.0.3.0.0
-  __TEXT.__text: 0x19f038
-  __TEXT.__objc_methlist: 0x1428c
-  __TEXT.__const: 0xdc6
+1351.0.0.0.0
+  __TEXT.__text: 0x1a0e80
+  __TEXT.__objc_methlist: 0x14404
+  __TEXT.__const: 0xdd6
   __TEXT.__dlopen_cstrs: 0x2c4
   __TEXT.__constg_swiftt: 0x454
   __TEXT.__swift5_typeref: 0x5fa
   __TEXT.__swift5_fieldmd: 0x160
-  __TEXT.__cstring: 0x16868
+  __TEXT.__cstring: 0x168fb
   __TEXT.__swift5_capture: 0x14c
-  __TEXT.__oslogstring: 0x19ddc
+  __TEXT.__oslogstring: 0x1a286
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_reflstr: 0x102
   __TEXT.__swift5_protos: 0x10

   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x4
-  __TEXT.__gcc_except_tab: 0x84f8
+  __TEXT.__gcc_except_tab: 0x8508
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0x7fa8
-  __TEXT.__eh_frame: 0x2a8
+  __TEXT.__unwind_info: 0x8020
+  __TEXT.__eh_frame: 0x2e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x39c0
-  __DATA_CONST.__objc_classlist: 0xa50
+  __DATA_CONST.__objc_classlist: 0xa60
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x210
+  __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xaca8
+  __DATA_CONST.__objc_selrefs: 0xad98
   __DATA_CONST.__objc_protorefs: 0x128
-  __DATA_CONST.__objc_superrefs: 0x708
+  __DATA_CONST.__objc_superrefs: 0x710
   __DATA_CONST.__objc_arraydata: 0x550
-  __DATA_CONST.__got: 0x18f0
-  __AUTH_CONST.__const: 0x9348
+  __DATA_CONST.__got: 0x1910
+  __AUTH_CONST.__const: 0x9388
   __AUTH_CONST.__cfstring: 0xf760
-  __AUTH_CONST.__objc_const: 0x1a980
+  __AUTH_CONST.__objc_const: 0x1ac88
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x1068
   __AUTH_CONST.__objc_arrayobj: 0x408
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__objc_doubleobj: 0xd0
-  __AUTH_CONST.__auth_got: 0xd60
-  __AUTH.__objc_data: 0x1370
-  __DATA.__objc_ivar: 0x1218
-  __DATA.__data: 0x17e0
+  __AUTH_CONST.__auth_got: 0xd68
+  __AUTH.__objc_data: 0x1410
+  __DATA.__objc_ivar: 0x123c
+  __DATA.__data: 0x1840
   __DATA_DIRTY.__objc_data: 0x5a48
   __DATA_DIRTY.__data: 0x398
-  __DATA_DIRTY.__bss: 0x5f8
+  __DATA_DIRTY.__bss: 0x5e0
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8913
-  Symbols:   17222
-  CStrings:  4255
+  Functions: 8965
+  Symbols:   17335
+  CStrings:  4273
 
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
+ GCC_except_table1005
+ GCC_except_table1006
+ GCC_except_table1019
+ GCC_except_table1022
+ GCC_except_table1025
+ GCC_except_table1026
+ GCC_except_table1027
+ GCC_except_table1028
+ GCC_except_table1031
+ GCC_except_table1032
+ GCC_except_table1033
+ GCC_except_table1034
+ GCC_except_table1035
+ GCC_except_table1036
+ GCC_except_table1038
+ GCC_except_table1039
+ GCC_except_table1042
+ GCC_except_table1045
+ GCC_except_table1065
+ GCC_except_table1068
+ GCC_except_table1070
+ GCC_except_table1072
+ GCC_except_table1073
+ GCC_except_table1087
+ GCC_except_table1088
+ GCC_except_table1121
+ GCC_except_table1129
+ GCC_except_table1131
+ GCC_except_table1138
+ GCC_except_table1151
+ GCC_except_table1176
+ GCC_except_table1178
+ GCC_except_table1180
+ GCC_except_table1184
+ GCC_except_table1188
+ GCC_except_table1192
+ GCC_except_table1201
+ GCC_except_table1213
+ GCC_except_table1243
+ GCC_except_table1247
+ GCC_except_table1248
+ GCC_except_table1254
+ GCC_except_table1256
+ GCC_except_table1265
+ GCC_except_table1283
+ GCC_except_table1290
+ GCC_except_table1293
+ GCC_except_table1295
+ GCC_except_table1297
+ GCC_except_table1311
+ GCC_except_table1326
+ GCC_except_table1343
+ GCC_except_table1352
+ GCC_except_table1354
+ GCC_except_table1359
+ GCC_except_table1379
+ GCC_except_table1431
+ GCC_except_table1453
+ GCC_except_table1464
+ GCC_except_table1567
+ GCC_except_table1568
+ GCC_except_table1569
+ GCC_except_table1570
+ GCC_except_table1575
+ GCC_except_table1581
+ GCC_except_table1583
+ GCC_except_table1584
+ GCC_except_table1585
+ GCC_except_table1586
+ GCC_except_table1589
+ GCC_except_table1622
+ GCC_except_table1649
+ GCC_except_table1740
+ GCC_except_table1750
+ GCC_except_table1754
+ GCC_except_table1758
+ GCC_except_table1761
+ GCC_except_table1774
+ GCC_except_table1778
+ GCC_except_table179
+ GCC_except_table1812
+ GCC_except_table1850
+ GCC_except_table1860
+ GCC_except_table1866
+ GCC_except_table1875
+ GCC_except_table1888
+ GCC_except_table1891
+ GCC_except_table1896
+ GCC_except_table191
+ GCC_except_table1996
+ GCC_except_table2015
+ GCC_except_table2017
+ GCC_except_table2039
+ GCC_except_table2043
+ GCC_except_table2046
+ GCC_except_table2070
+ GCC_except_table2072
+ GCC_except_table2077
+ GCC_except_table2079
+ GCC_except_table2097
+ GCC_except_table2107
+ GCC_except_table2114
+ GCC_except_table2160
+ GCC_except_table2205
+ GCC_except_table2209
+ GCC_except_table2230
+ GCC_except_table2236
+ GCC_except_table2243
+ GCC_except_table2250
+ GCC_except_table2323
+ GCC_except_table298
+ GCC_except_table358
+ GCC_except_table360
+ GCC_except_table378
+ GCC_except_table398
+ GCC_except_table4348
+ GCC_except_table4354
+ GCC_except_table4446
+ GCC_except_table4447
+ GCC_except_table4448
+ GCC_except_table4449
+ GCC_except_table4450
+ GCC_except_table4452
+ GCC_except_table4456
+ GCC_except_table4457
+ GCC_except_table4460
+ GCC_except_table4461
+ GCC_except_table4463
+ GCC_except_table4466
+ GCC_except_table4467
+ GCC_except_table4472
+ GCC_except_table4483
+ GCC_except_table4512
+ GCC_except_table4513
+ GCC_except_table4514
+ GCC_except_table452
+ GCC_except_table4520
+ GCC_except_table4523
+ GCC_except_table4527
+ GCC_except_table458
+ GCC_except_table4581
+ GCC_except_table4586
+ GCC_except_table4588
+ GCC_except_table4598
+ GCC_except_table4608
+ GCC_except_table4616
+ GCC_except_table4624
+ GCC_except_table4628
+ GCC_except_table4636
+ GCC_except_table4666
+ GCC_except_table4673
+ GCC_except_table468
+ GCC_except_table4680
+ GCC_except_table4681
+ GCC_except_table4682
+ GCC_except_table4684
+ GCC_except_table4685
+ GCC_except_table4700
+ GCC_except_table4709
+ GCC_except_table4727
+ GCC_except_table4737
+ GCC_except_table4739
+ GCC_except_table4744
+ GCC_except_table4748
+ GCC_except_table4832
+ GCC_except_table4840
+ GCC_except_table4846
+ GCC_except_table4966
+ GCC_except_table501
+ GCC_except_table5089
+ GCC_except_table5102
+ GCC_except_table5105
+ GCC_except_table5117
+ GCC_except_table5131
+ GCC_except_table5210
+ GCC_except_table5220
+ GCC_except_table5223
+ GCC_except_table5266
+ GCC_except_table536
+ GCC_except_table5383
+ GCC_except_table5387
+ GCC_except_table5389
+ GCC_except_table5390
+ GCC_except_table5396
+ GCC_except_table5403
+ GCC_except_table5405
+ GCC_except_table5438
+ GCC_except_table5447
+ GCC_except_table5448
+ GCC_except_table5449
+ GCC_except_table5451
+ GCC_except_table5454
+ GCC_except_table5472
+ GCC_except_table5489
+ GCC_except_table5492
+ GCC_except_table5494
+ GCC_except_table5495
+ GCC_except_table5496
+ GCC_except_table5498
+ GCC_except_table5507
+ GCC_except_table5511
+ GCC_except_table5512
+ GCC_except_table5514
+ GCC_except_table5515
+ GCC_except_table5518
+ GCC_except_table5545
+ GCC_except_table5598
+ GCC_except_table5711
+ GCC_except_table5726
+ GCC_except_table5752
+ GCC_except_table5757
+ GCC_except_table5761
+ GCC_except_table5763
+ GCC_except_table5767
+ GCC_except_table5778
+ GCC_except_table5870
+ GCC_except_table5896
+ GCC_except_table5902
+ GCC_except_table5904
+ GCC_except_table5953
+ GCC_except_table5960
+ GCC_except_table5971
+ GCC_except_table5973
+ GCC_except_table5984
+ GCC_except_table6134
+ GCC_except_table6139
+ GCC_except_table6144
+ GCC_except_table6158
+ GCC_except_table6169
+ GCC_except_table6173
+ GCC_except_table6188
+ GCC_except_table6195
+ GCC_except_table6216
+ GCC_except_table6256
+ GCC_except_table6270
+ GCC_except_table6281
+ GCC_except_table6294
+ GCC_except_table6308
+ GCC_except_table6315
+ GCC_except_table6334
+ GCC_except_table6346
+ GCC_except_table6349
+ GCC_except_table6353
+ GCC_except_table6356
+ GCC_except_table6359
+ GCC_except_table6365
+ GCC_except_table6370
+ GCC_except_table6373
+ GCC_except_table6376
+ GCC_except_table6395
+ GCC_except_table6400
+ GCC_except_table6404
+ GCC_except_table6407
+ GCC_except_table6418
+ GCC_except_table6552
+ GCC_except_table6568
+ GCC_except_table6580
+ GCC_except_table6586
+ GCC_except_table6592
+ GCC_except_table6598
+ GCC_except_table6599
+ GCC_except_table6609
+ GCC_except_table6614
+ GCC_except_table6659
+ GCC_except_table6676
+ GCC_except_table6793
+ GCC_except_table6812
+ GCC_except_table6822
+ GCC_except_table6828
+ GCC_except_table6830
+ GCC_except_table6913
+ GCC_except_table6920
+ GCC_except_table6926
+ GCC_except_table6933
+ GCC_except_table6940
+ GCC_except_table6977
+ GCC_except_table6985
+ GCC_except_table6993
+ GCC_except_table6999
+ GCC_except_table7002
+ GCC_except_table7037
+ GCC_except_table7070
+ GCC_except_table7082
+ GCC_except_table7093
+ GCC_except_table7113
+ GCC_except_table7119
+ GCC_except_table7122
+ GCC_except_table7128
+ GCC_except_table7129
+ GCC_except_table7130
+ GCC_except_table7131
+ GCC_except_table7185
+ GCC_except_table7201
+ GCC_except_table7208
+ GCC_except_table7262
+ GCC_except_table7277
+ GCC_except_table7298
+ GCC_except_table7300
+ GCC_except_table7302
+ GCC_except_table7306
+ GCC_except_table7308
+ GCC_except_table7310
+ GCC_except_table7312
+ GCC_except_table7314
+ GCC_except_table7316
+ GCC_except_table7318
+ GCC_except_table7320
+ GCC_except_table7327
+ GCC_except_table7338
+ GCC_except_table7355
+ GCC_except_table7364
+ GCC_except_table7432
+ GCC_except_table7436
+ GCC_except_table7439
+ GCC_except_table7451
+ GCC_except_table7453
+ GCC_except_table7454
+ GCC_except_table7481
+ GCC_except_table7482
+ GCC_except_table7492
+ GCC_except_table7495
+ GCC_except_table7502
+ GCC_except_table7507
+ GCC_except_table7514
+ GCC_except_table7517
+ GCC_except_table7533
+ GCC_except_table7556
+ GCC_except_table7564
+ GCC_except_table760
+ GCC_except_table7605
+ GCC_except_table761
+ GCC_except_table763
+ GCC_except_table764
+ GCC_except_table768
+ GCC_except_table7686
+ GCC_except_table769
+ GCC_except_table7705
+ GCC_except_table7716
+ GCC_except_table7719
+ GCC_except_table7721
+ GCC_except_table7726
+ GCC_except_table7735
+ GCC_except_table774
+ GCC_except_table7741
+ GCC_except_table7747
+ GCC_except_table7749
+ GCC_except_table7751
+ GCC_except_table7770
+ GCC_except_table7777
+ GCC_except_table7786
+ GCC_except_table7847
+ GCC_except_table7990
+ GCC_except_table7992
+ GCC_except_table7994
+ GCC_except_table7996
+ GCC_except_table8014
+ GCC_except_table8016
+ GCC_except_table8018
+ GCC_except_table8020
+ GCC_except_table8022
+ GCC_except_table8025
+ GCC_except_table8032
+ GCC_except_table8034
+ GCC_except_table8036
+ GCC_except_table8038
+ GCC_except_table8040
+ GCC_except_table8042
+ GCC_except_table8044
+ GCC_except_table8046
+ GCC_except_table8075
+ GCC_except_table8125
+ GCC_except_table8240
+ GCC_except_table8255
+ GCC_except_table8328
+ GCC_except_table8375
+ GCC_except_table8398
+ GCC_except_table8400
+ GCC_except_table8402
+ GCC_except_table8404
+ GCC_except_table8406
+ GCC_except_table8412
+ GCC_except_table8428
+ GCC_except_table8445
+ GCC_except_table953
+ GCC_except_table954
+ GCC_except_table958
+ GCC_except_table959
+ GCC_except_table960
+ GCC_except_table961
+ GCC_except_table966
+ GCC_except_table967
+ GCC_except_table970
+ GCC_except_table996
+ GCC_except_table999
+ OBJC_IVAR_$_PPDefaultBrowserCheck._cachedDefaultBrowserBundleID
+ OBJC_IVAR_$_PPDefaultBrowserCheck._generation
+ OBJC_IVAR_$_PPDefaultBrowserCheck._hasCachedDefaultBrowser
+ OBJC_IVAR_$_PPDefaultBrowserCheck._lock
+ OBJC_IVAR_$_PPDefaultBrowserCheck._workspace
+ OBJC_IVAR_$_PPSocialHighlightServerRequestHandler._accessValue
+ OBJC_IVAR_$_PPSocialHighlightServerRequestHandler._clientBundleID
+ OBJC_IVAR_$_PPSocialHighlightServerRequestHandler._clientIsWebBrowser
+ OBJC_IVAR_$_PPSocialHighlightServerRequestHandler._externalEntitlement
+ OBJC_IVAR_$_PPSocialHighlightServerRequestHandler._internalEntitlement
+ _OBJC_CLASS_$_LSObserver
+ _OBJC_CLASS_$_PPDefaultBrowserCheck
+ _OBJC_CLASS_$_PPSocialHighlightDefaultBrowserObserver
+ _OBJC_METACLASS_$_PPDefaultBrowserCheck
+ _OBJC_METACLASS_$_PPSocialHighlightDefaultBrowserObserver
+ _OUTLINED_FUNCTION_50
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_60
+ _OUTLINED_FUNCTION_61
+ _OUTLINED_FUNCTION_62
+ _PPBuildApplicationIdentifiers
+ _PPCachedDefaultTTLPolicy.cachedPolicy
+ _PPCachedDefaultTTLPolicy.cachedPolicyLock
+ _PPSocialHighlightHandleDefaultBrowserChange
+ _PPSocialHighlightResetDefaultBrowserChangeTrackingForTesting
+ __124-[PPSocialHighlightServerRequestHandler _rankedHighlightsWithLimit:client:variant:queryId:requestQoS:additionalIdentifiers:]_block_invoke
+ __124-[PPSocialHighlightServerRequestHandler _rankedHighlightsWithLimit:client:variant:queryId:requestQoS:additionalIdentifiers:]_block_invoke_2
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
+ ___124-[PPSocialHighlightServerRequestHandler _rankedHighlightsWithLimit:client:variant:queryId:requestQoS:additionalIdentifiers:]_block_invoke
+ ___124-[PPSocialHighlightServerRequestHandler _rankedHighlightsWithLimit:client:variant:queryId:requestQoS:additionalIdentifiers:]_block_invoke_2
+ ___36+[PPDefaultBrowserCheck sharedCheck]_block_invoke
+ ___39-[PPSocialHighlightServerDelegate init]_block_invoke
+ ___block_descriptor_65_e8_32s40s48s_e48_v16?0"PPConnectionsScoredLocationGuardedData"8l
+ __os_feature_enabled_simple_impl
+ _handleCloudStorageDeletedByUser._pasOnceToken14
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
+ _rankedHighlightsWithLimit:client:variant:queryId:requestQoS:additionalIdentifiers:._pasExprOnceResult
+ _rankedHighlightsWithLimit:client:variant:queryId:requestQoS:additionalIdentifiers:._pasOnceToken3
+ _sHasHandledBrowserChange
+ _sLastHandledBrowserBundleID
+ _sLastHandledBrowserLock
+ _triggerDelayedOperationWithCoalescingToken:operation:._pasOnceToken33
+ init.lsObserver
+ init.observer
+ init.onceToken
+ kPPCanLearnFromAppKey_block_invoke._pasOnceToken23
+ sharedCheck.onceToken
+ sharedCheck.sharedCheck
- -[PPSocialHighlightServerRequestHandler applicationIdentifiers]
- -[PPSocialHighlightServerRequestHandler setApplicationIdentifiers:]
- GCC_except_table1001
- GCC_except_table1004
- GCC_except_table1007
- GCC_except_table1008
- GCC_except_table1009
- GCC_except_table1010
- GCC_except_table1011
- GCC_except_table1015
- GCC_except_table1016
- GCC_except_table1018
- GCC_except_table1021
- GCC_except_table1041
- GCC_except_table1044
- GCC_except_table1046
- GCC_except_table1048
- GCC_except_table1049
- GCC_except_table1063
- GCC_except_table1097
- GCC_except_table1103
- GCC_except_table1105
- GCC_except_table1107
- GCC_except_table1114
- GCC_except_table1152
- GCC_except_table1154
- GCC_except_table1156
- GCC_except_table1160
- GCC_except_table1164
- GCC_except_table1168
- GCC_except_table1177
- GCC_except_table1189
- GCC_except_table1208
- GCC_except_table1219
- GCC_except_table1223
- GCC_except_table1224
- GCC_except_table1230
- GCC_except_table1241
- GCC_except_table1259
- GCC_except_table1263
- GCC_except_table1266
- GCC_except_table1269
- GCC_except_table1271
- GCC_except_table1273
- GCC_except_table1301
- GCC_except_table1318
- GCC_except_table1327
- GCC_except_table1329
- GCC_except_table1334
- GCC_except_table1353
- GCC_except_table1405
- GCC_except_table1427
- GCC_except_table1438
- GCC_except_table1541
- GCC_except_table1542
- GCC_except_table1543
- GCC_except_table1544
- GCC_except_table1549
- GCC_except_table1555
- GCC_except_table1557
- GCC_except_table1558
- GCC_except_table1559
- GCC_except_table1560
- GCC_except_table1563
- GCC_except_table1590
- GCC_except_table1617
- GCC_except_table1708
- GCC_except_table171
- GCC_except_table1714
- GCC_except_table1718
- GCC_except_table1722
- GCC_except_table1726
- GCC_except_table1729
- GCC_except_table1742
- GCC_except_table1780
- GCC_except_table1818
- GCC_except_table1824
- GCC_except_table1827
- GCC_except_table1828
- GCC_except_table183
- GCC_except_table1834
- GCC_except_table1843
- GCC_except_table1864
- GCC_except_table1953
- GCC_except_table1964
- GCC_except_table1975
- GCC_except_table1983
- GCC_except_table2011
- GCC_except_table2014
- GCC_except_table2038
- GCC_except_table2040
- GCC_except_table2045
- GCC_except_table2047
- GCC_except_table2065
- GCC_except_table2075
- GCC_except_table2082
- GCC_except_table2128
- GCC_except_table2173
- GCC_except_table2177
- GCC_except_table2198
- GCC_except_table2204
- GCC_except_table2211
- GCC_except_table2218
- GCC_except_table2291
- GCC_except_table274
- GCC_except_table334
- GCC_except_table336
- GCC_except_table354
- GCC_except_table374
- GCC_except_table428
- GCC_except_table4316
- GCC_except_table4322
- GCC_except_table434
- GCC_except_table4414
- GCC_except_table4415
- GCC_except_table4416
- GCC_except_table4417
- GCC_except_table4418
- GCC_except_table4419
- GCC_except_table4420
- GCC_except_table4424
- GCC_except_table4425
- GCC_except_table4428
- GCC_except_table4429
- GCC_except_table4431
- GCC_except_table4434
- GCC_except_table4435
- GCC_except_table444
- GCC_except_table4440
- GCC_except_table4480
- GCC_except_table4481
- GCC_except_table4482
- GCC_except_table4488
- GCC_except_table4491
- GCC_except_table4495
- GCC_except_table4549
- GCC_except_table4554
- GCC_except_table4556
- GCC_except_table4566
- GCC_except_table4572
- GCC_except_table4576
- GCC_except_table4584
- GCC_except_table4592
- GCC_except_table4596
- GCC_except_table4602
- GCC_except_table4621
- GCC_except_table4641
- GCC_except_table4645
- GCC_except_table4648
- GCC_except_table4649
- GCC_except_table4650
- GCC_except_table4652
- GCC_except_table4668
- GCC_except_table4695
- GCC_except_table4705
- GCC_except_table4707
- GCC_except_table4712
- GCC_except_table4716
- GCC_except_table477
- GCC_except_table4800
- GCC_except_table4808
- GCC_except_table4814
- GCC_except_table4934
- GCC_except_table5057
- GCC_except_table5070
- GCC_except_table5073
- GCC_except_table5085
- GCC_except_table5099
- GCC_except_table512
- GCC_except_table5178
- GCC_except_table5188
- GCC_except_table5191
- GCC_except_table5234
- GCC_except_table5351
- GCC_except_table5355
- GCC_except_table5357
- GCC_except_table5358
- GCC_except_table5364
- GCC_except_table5371
- GCC_except_table5373
- GCC_except_table5406
- GCC_except_table5415
- GCC_except_table5416
- GCC_except_table5417
- GCC_except_table5419
- GCC_except_table5422
- GCC_except_table5440
- GCC_except_table5443
- GCC_except_table5457
- GCC_except_table5460
- GCC_except_table5462
- GCC_except_table5463
- GCC_except_table5464
- GCC_except_table5466
- GCC_except_table5479
- GCC_except_table5480
- GCC_except_table5481
- GCC_except_table5482
- GCC_except_table5483
- GCC_except_table5486
- GCC_except_table5566
- GCC_except_table5678
- GCC_except_table5686
- GCC_except_table5693
- GCC_except_table5701
- GCC_except_table5724
- GCC_except_table5728
- GCC_except_table5730
- GCC_except_table5745
- GCC_except_table5830
- GCC_except_table5837
- GCC_except_table5869
- GCC_except_table5871
- GCC_except_table5920
- GCC_except_table5927
- GCC_except_table5938
- GCC_except_table5940
- GCC_except_table5951
- GCC_except_table6101
- GCC_except_table6106
- GCC_except_table6111
- GCC_except_table6125
- GCC_except_table6136
- GCC_except_table6140
- GCC_except_table6155
- GCC_except_table6162
- GCC_except_table6183
- GCC_except_table6223
- GCC_except_table6237
- GCC_except_table6248
- GCC_except_table6261
- GCC_except_table6268
- GCC_except_table6275
- GCC_except_table6282
- GCC_except_table6304
- GCC_except_table6307
- GCC_except_table6310
- GCC_except_table6313
- GCC_except_table6316
- GCC_except_table6320
- GCC_except_table6323
- GCC_except_table6326
- GCC_except_table6329
- GCC_except_table6332
- GCC_except_table6367
- GCC_except_table6371
- GCC_except_table6374
- GCC_except_table6385
- GCC_except_table6486
- GCC_except_table6510
- GCC_except_table6533
- GCC_except_table6535
- GCC_except_table6547
- GCC_except_table6553
- GCC_except_table6559
- GCC_except_table6565
- GCC_except_table6581
- GCC_except_table6625
- GCC_except_table6642
- GCC_except_table6759
- GCC_except_table6778
- GCC_except_table6788
- GCC_except_table6794
- GCC_except_table6796
- GCC_except_table6879
- GCC_except_table6886
- GCC_except_table6892
- GCC_except_table6899
- GCC_except_table6906
- GCC_except_table6943
- GCC_except_table6951
- GCC_except_table6959
- GCC_except_table6965
- GCC_except_table6968
- GCC_except_table7003
- GCC_except_table7036
- GCC_except_table7048
- GCC_except_table7059
- GCC_except_table7063
- GCC_except_table7079
- GCC_except_table7085
- GCC_except_table7088
- GCC_except_table7094
- GCC_except_table7095
- GCC_except_table7096
- GCC_except_table7151
- GCC_except_table7167
- GCC_except_table7174
- GCC_except_table7228
- GCC_except_table7243
- GCC_except_table7264
- GCC_except_table7266
- GCC_except_table7268
- GCC_except_table7270
- GCC_except_table7272
- GCC_except_table7274
- GCC_except_table7276
- GCC_except_table7278
- GCC_except_table7280
- GCC_except_table7282
- GCC_except_table7284
- GCC_except_table7286
- GCC_except_table7293
- GCC_except_table7321
- GCC_except_table7330
- GCC_except_table736
- GCC_except_table737
- GCC_except_table739
- GCC_except_table7398
- GCC_except_table740
- GCC_except_table7402
- GCC_except_table7405
- GCC_except_table7417
- GCC_except_table7419
- GCC_except_table7420
- GCC_except_table744
- GCC_except_table7447
- GCC_except_table7448
- GCC_except_table745
- GCC_except_table7458
- GCC_except_table7461
- GCC_except_table7468
- GCC_except_table7473
- GCC_except_table7480
- GCC_except_table7483
- GCC_except_table7499
- GCC_except_table750
- GCC_except_table7522
- GCC_except_table7530
- GCC_except_table7571
- GCC_except_table7652
- GCC_except_table7671
- GCC_except_table7682
- GCC_except_table7685
- GCC_except_table7687
- GCC_except_table7692
- GCC_except_table7701
- GCC_except_table7707
- GCC_except_table7713
- GCC_except_table7715
- GCC_except_table7717
- GCC_except_table7736
- GCC_except_table7743
- GCC_except_table7752
- GCC_except_table7813
- GCC_except_table7824
- GCC_except_table7828
- GCC_except_table7830
- GCC_except_table7832
- GCC_except_table7834
- GCC_except_table7836
- GCC_except_table7838
- GCC_except_table7840
- GCC_except_table7842
- GCC_except_table7844
- GCC_except_table7846
- GCC_except_table7848
- GCC_except_table7850
- GCC_except_table7852
- GCC_except_table7854
- GCC_except_table7856
- GCC_except_table7860
- GCC_except_table7991
- GCC_except_table8041
- GCC_except_table8091
- GCC_except_table8206
- GCC_except_table8221
- GCC_except_table8294
- GCC_except_table8341
- GCC_except_table8364
- GCC_except_table8366
- GCC_except_table8368
- GCC_except_table8370
- GCC_except_table8372
- GCC_except_table8378
- GCC_except_table8394
- GCC_except_table8411
- GCC_except_table929
- GCC_except_table930
- GCC_except_table934
- GCC_except_table935
- GCC_except_table936
- GCC_except_table937
- GCC_except_table942
- GCC_except_table943
- GCC_except_table946
- GCC_except_table972
- GCC_except_table974
- GCC_except_table975
- GCC_except_table978
- GCC_except_table979
- GCC_except_table981
- GCC_except_table982
- GCC_except_table988
- GCC_except_table990
- GCC_except_table995
- OBJC_IVAR_$_PPSocialHighlightServerRequestHandler._applicationIdentifiers
- __101-[PPSocialHighlightServerRequestHandler rankedHighlightsWithLimit:client:variant:queryId:requestQoS:]_block_invoke
- __101-[PPSocialHighlightServerRequestHandler rankedHighlightsWithLimit:client:variant:queryId:requestQoS:]_block_invoke_2
- ___101-[PPSocialHighlightServerRequestHandler rankedHighlightsWithLimit:client:variant:queryId:requestQoS:]_block_invoke
- ___101-[PPSocialHighlightServerRequestHandler rankedHighlightsWithLimit:client:variant:queryId:requestQoS:]_block_invoke_2
- ___block_descriptor_56_e8_32s40s_e48_v16?0"PPConnectionsScoredLocationGuardedData"8l
- _handleCloudStorageDeletedByUser._pasOnceToken13
- _objc_msgSend$rankedHighlightsWithLimit:client:variant:queryId:requestQoS:
- _triggerDelayedOperationWithCoalescingToken:operation:._pasOnceToken31
- kPPCanLearnFromAppKey_block_invoke._pasOnceToken22
- rankedHighlightsWithLimit:client:variant:queryId:requestQoS:._pasExprOnceResult
- rankedHighlightsWithLimit:client:variant:queryId:requestQoS:._pasOnceToken3
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
