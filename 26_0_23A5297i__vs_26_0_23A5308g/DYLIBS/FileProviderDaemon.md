## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`

```diff

-3871.0.0.0.2
-  __TEXT.__text: 0xa01ed0
-  __TEXT.__auth_stubs: 0x5b80
-  __TEXT.__objc_methlist: 0x9964
-  __TEXT.__const: 0x24690
-  __TEXT.__cstring: 0x41afd
-  __TEXT.__oslogstring: 0x1dbf2
-  __TEXT.__gcc_except_tab: 0xe404
+3882.0.36.0.0
+  __TEXT.__text: 0xa052ac
+  __TEXT.__auth_stubs: 0x5c10
+  __TEXT.__objc_methlist: 0x99ec
+  __TEXT.__const: 0x24780
+  __TEXT.__cstring: 0x41dcd
+  __TEXT.__oslogstring: 0x1ddd2
+  __TEXT.__gcc_except_tab: 0xe430
   __TEXT.__ustring: 0x176e
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__constg_swiftt: 0x11fd4
-  __TEXT.__swift5_typeref: 0x118b6
+  __TEXT.__constg_swiftt: 0x12054
+  __TEXT.__swift5_typeref: 0x11926
   __TEXT.__swift5_builtin: 0x848
   __TEXT.__swift5_mpenum: 0x118
-  __TEXT.__swift5_reflstr: 0xbbbd
-  __TEXT.__swift5_fieldmd: 0xa8bc
+  __TEXT.__swift5_reflstr: 0xbc1d
+  __TEXT.__swift5_fieldmd: 0xa8e4
   __TEXT.__swift5_assocty: 0x2270
-  __TEXT.__swift5_capture: 0x1b4f4
+  __TEXT.__swift5_capture: 0x1b518
   __TEXT.__swift5_proto: 0x1860
-  __TEXT.__swift5_types: 0xa78
+  __TEXT.__swift5_types: 0xa7c
   __TEXT.__swift5_types2: 0x4
   __TEXT.__swift5_protos: 0x98
   __TEXT.__swift_as_entry: 0xa8
   __TEXT.__swift_as_ret: 0xa4
-  __TEXT.__unwind_info: 0x14b28
-  __TEXT.__eh_frame: 0x26430
-  __TEXT.__objc_classname: 0xef2
-  __TEXT.__objc_methname: 0x1d802
-  __TEXT.__objc_methtype: 0x6a92
-  __TEXT.__objc_stubs: 0xfdc0
-  __DATA_CONST.__got: 0x17e8
-  __DATA_CONST.__const: 0x4d58
-  __DATA_CONST.__objc_classlist: 0x558
+  __TEXT.__unwind_info: 0x14b80
+  __TEXT.__eh_frame: 0x26570
+  __TEXT.__objc_classname: 0xf14
+  __TEXT.__objc_methname: 0x1d8b7
+  __TEXT.__objc_methtype: 0x6a95
+  __TEXT.__objc_stubs: 0xfe60
+  __DATA_CONST.__got: 0x1800
+  __DATA_CONST.__const: 0x4de8
+  __DATA_CONST.__objc_classlist: 0x568
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x350
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6108
+  __DATA_CONST.__objc_selrefs: 0x6138
   __DATA_CONST.__objc_protorefs: 0x188
-  __DATA_CONST.__objc_superrefs: 0x280
-  __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0x2dd0
-  __AUTH_CONST.__const: 0x50e10
-  __AUTH_CONST.__cfstring: 0x6ca0
-  __AUTH_CONST.__objc_const: 0x29570
-  __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH_CONST.__objc_intobj: 0xf0
+  __DATA_CONST.__objc_superrefs: 0x290
+  __DATA_CONST.__objc_arraydata: 0xf0
+  __AUTH_CONST.__auth_got: 0x2e18
+  __AUTH_CONST.__const: 0x50fc8
+  __AUTH_CONST.__cfstring: 0x6e00
+  __AUTH_CONST.__objc_const: 0x297a8
+  __AUTH_CONST.__objc_arrayobj: 0xf0
+  __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x1808
-  __AUTH.__data: 0x23f0
-  __DATA.__objc_ivar: 0xb20
-  __DATA.__data: 0x8a70
-  __DATA.__bss: 0x250c0
-  __DATA.__common: 0x168
-  __DATA_DIRTY.__objc_data: 0x3800
-  __DATA_DIRTY.__data: 0xd908
-  __DATA_DIRTY.__bss: 0xa770
-  __DATA_DIRTY.__common: 0x8e8
+  __AUTH.__objc_data: 0x1858
+  __AUTH.__data: 0x22f0
+  __DATA.__objc_ivar: 0xb38
+  __DATA.__data: 0x8290
+  __DATA.__bss: 0x247d0
+  __DATA.__common: 0x148
+  __DATA_DIRTY.__objc_data: 0x3850
+  __DATA_DIRTY.__data: 0xe298
+  __DATA_DIRTY.__bss: 0xb070
+  __DATA_DIRTY.__common: 0x918
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D63A2EC2-7CBF-3A54-8A05-628E4835243E
-  Functions: 30743
-  Symbols:   28336
-  CStrings:  13461
+  UUID: B4699351-A14E-3122-85CA-FD7E11B60E87
+  Functions: 30780
+  Symbols:   28407
+  CStrings:  13512
 
Symbols:
+ -[FPBoolean initWithBool:]
+ -[FPBoolean isEqual:]
+ -[FPBoolean value]
+ -[FPDCoreAnalyticsReport .cxx_destruct]
+ -[FPDCoreAnalyticsReport addValue:forKey:]
+ -[FPDCoreAnalyticsReport initWithEventName:]
+ -[FPDCoreAnalyticsReport sendReport]
+ -[FPDExtensionManager updating]
+ -[FPDProvider reloadDomain:unableToStartup:startupError:completionHandler:].cold.1
+ -[FPDXPCServicer _canBundleIDTriggerTTRForFailure:]
+ -[FPDXPCServicer _canBundleIDTriggerTTRForFailure:].cold.1
+ -[FPDiagnosticCollector initWithFD:trashURL:isExternalQuery:]
+ GCC_except_table116
+ GCC_except_table165
+ GCC_except_table195
+ GCC_except_table198
+ GCC_except_table213
+ GCC_except_table220
+ GCC_except_table239
+ GCC_except_table242
+ GCC_except_table246
+ GCC_except_table247
+ GCC_except_table253
+ GCC_except_table254
+ GCC_except_table263
+ GCC_except_table267
+ GCC_except_table270
+ GCC_except_table273
+ GCC_except_table278
+ GCC_except_table285
+ GCC_except_table292
+ GCC_except_table295
+ GCC_except_table315
+ GCC_except_table360
+ GCC_except_table363
+ GCC_except_table366
+ GCC_except_table370
+ GCC_except_table379
+ GCC_except_table380
+ GCC_except_table399
+ GCC_except_table402
+ GCC_except_table405
+ GCC_except_table412
+ GCC_except_table413
+ GCC_except_table417
+ GCC_except_table422
+ GCC_except_table427
+ GCC_except_table428
+ GCC_except_table434
+ GCC_except_table435
+ GCC_except_table443
+ GCC_except_table446
+ GCC_except_table450
+ GCC_except_table451
+ GCC_except_table456
+ GCC_except_table465
+ GCC_except_table469
+ GCC_except_table471
+ GCC_except_table473
+ GCC_except_table480
+ GCC_except_table481
+ _AnalyticsIsEventUsed
+ _AnalyticsSendEventLazy
+ _FPFileIsAlreadyPausedError_internal
+ _FPFileNotPausedError_internal
+ _FPTelemetryParsedError
+ _OBJC_CLASS_$_FPBoolean
+ _OBJC_CLASS_$_FPDCoreAnalyticsReport
+ _OBJC_IVAR_$_FPBoolean._value
+ _OBJC_IVAR_$_FPDCoreAnalyticsReport._eventName
+ _OBJC_IVAR_$_FPDCoreAnalyticsReport._isEventEnabled
+ _OBJC_IVAR_$_FPDCoreAnalyticsReport._report
+ _OBJC_IVAR_$_FPDExtensionManager._updating
+ _OBJC_IVAR_$_FPDiagnosticCollector._isExternalQuery
+ _OBJC_METACLASS_$_FPBoolean
+ _OBJC_METACLASS_$_FPDCoreAnalyticsReport
+ __OBJC_$_INSTANCE_METHODS_FPBoolean
+ __OBJC_$_INSTANCE_METHODS_FPDCoreAnalyticsReport
+ __OBJC_$_INSTANCE_VARIABLES_FPBoolean
+ __OBJC_$_INSTANCE_VARIABLES_FPDCoreAnalyticsReport
+ __OBJC_$_PROP_LIST_FPBoolean
+ __OBJC_CLASS_RO_$_FPBoolean
+ __OBJC_CLASS_RO_$_FPDCoreAnalyticsReport
+ __OBJC_METACLASS_RO_$_FPBoolean
+ __OBJC_METACLASS_RO_$_FPDCoreAnalyticsReport
+ ___100-[FPDXPCServicer _test_importItemsPendingScanningProviderProgressForDomainWithID:completionHandler:]_block_invoke.483
+ ___100-[FPDXPCServicer uploadLocalVersionOfItemAtURL:bundleID:conflictResolutionPolicy:completionHandler:]_block_invoke.544
+ ___100-[FPDXPCServicer uploadLocalVersionOfItemAtURL:bundleID:conflictResolutionPolicy:completionHandler:]_block_invoke.544.cold.1
+ ___133-[FPDXPCServicer runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:]_block_invoke.323
+ ___133-[FPDXPCServicer runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:]_block_invoke.323.cold.1
+ ___133-[FPDXPCServicer runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:]_block_invoke.326
+ ___36-[FPDCoreAnalyticsReport sendReport]_block_invoke
+ ___51-[FPDXPCServicer _canBundleIDTriggerTTRForFailure:]_block_invoke
+ ___53-[FPDXPCServicer pauseIndexingFor:completionHandler:]_block_invoke.457
+ ___54-[FPDXPCServicer resumeIndexingFor:completionHandler:]_block_invoke.458
+ ___57-[FPDXPCServicer stateForDomainWithID:completionHandler:]_block_invoke.321
+ ___59-[FPDXPCServicer _test_purgerBarrierWithCompletionHandler:]_block_invoke.490
+ ___59-[FPDXPCServicer _test_purgerBarrierWithCompletionHandler:]_block_invoke.490.cold.1
+ ___59-[FPDXPCServicer appHasNonUploadedFiles:completionHandler:]_block_invoke.334
+ ___63-[FPDXPCServicer fetchDaemonOperationIDsWithCompletionHandler:]_block_invoke.415
+ ___65-[FPDXPCServicer _test_resetDBQueryStatistics:completionHandler:]_block_invoke.485
+ ___66-[FPDXPCServicer importProgressForDomainWithID:completionHandler:]_block_invoke.319
+ ___67-[FPDXPCServicer _test_disableDBQueryStatistics:completionHandler:]_block_invoke.484
+ ___67-[FPDXPCServicer dumpTelemetryTo:providerFilter:completionHandler:]_block_invoke.392
+ ___68-[FPDXPCServicer dumpDatabaseAt:fullDump:writeTo:completionHandler:]_block_invoke.329
+ ___68-[FPDXPCServicer scheduleActionOperationWithInfo:completionHandler:]_block_invoke.413
+ ___70-[FPDXPCServicer _test_triggerDatabaseError:domain:completionHandler:]_block_invoke.489
+ ___70-[FPDXPCServicer copyDatabaseForFPCKStartingAtPath:completionHandler:]_block_invoke.406
+ ___71-[FPDXPCServicer dumpStateTo:providerFilter:options:completionHandler:]_block_invoke.375
+ ___73-[FPDXPCServicer _test_getDBQueryStatistics:queryPlan:completionHandler:]_block_invoke.486
+ ___73-[FPDXPCServicer waitForChangesOnItemsBelowItemWithID:completionHandler:]_block_invoke.409
+ ___74-[FPDXPCServicer startAccessingServiceWithName:itemURL:completionHandler:]_block_invoke.426
+ ___76-[FPDXPCServicer fetchLatestVersionForItemAtURL:bundleID:completionHandler:]_block_invoke.534
+ ___76-[FPDXPCServicer pauseSyncForItemAtURL:behavior:bundleID:completionHandler:]_block_invoke.516
+ ___76-[FPDXPCServicer waitForStabilizationOfDomainWithID:mode:completionHandler:]_block_invoke.410
+ ___77-[FPDXPCServicer _performWithCheckedEnumerationAttributes:completionHandler:]_block_invoke.436
+ ___77-[FPDXPCServicer forceUpdateBlockedProcessNamesFromDomain:completionHandler:]_block_invoke.316
+ ___77-[FPDXPCServicer resumeSyncForItemAtURL:behavior:bundleID:completionHandler:]_block_invoke.528
+ ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.466
+ ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.466.cold.1
+ ___82-[FPDXPCServicer fetchAndStartEnumeratingWithSettings:observer:completionHandler:]_block_invoke.442
+ ___82-[FPDXPCServicer reimportItemsBelowItemWithID:markItemDataless:completionHandler:]_block_invoke.315
+ ___85-[FPDXPCServicer enumerateSearchResultForRequest:providerDomainID:completionHandler:]_block_invoke.431
+ ___86-[FPDXPCServicer setEnabled:forDomainIdentifier:providerIdentifier:completionHandler:]_block_invoke.312
+ ___88-[FPDXPCServicer spotlightReindexAllItemsForBundleID:protectionClass:completionHandler:]_block_invoke.411
+ ___91-[FPDXPCServicer setHiddenByUser:forDomainIdentifier:providerIdentifier:completionHandler:]_block_invoke.313
+ ___93-[FPDXPCServicer signalReindexCSIdentifiersByProviderDomainID:indexReason:completionHandler:]_block_invoke.459
+ ___93-[FPDXPCServicer signalReindexCSIdentifiersByProviderDomainID:indexReason:completionHandler:]_block_invoke.459.cold.1
+ ___93-[FPDXPCServicer signalReindexCSIdentifiersByProviderDomainID:indexReason:completionHandler:]_block_invoke.459.cold.2
+ ___94-[FPDXPCServicer setIndexingEnabled:forDomainIdentifier:providerIdentifier:completionHandler:]_block_invoke.314
+ ___96-[FPDXPCServicer _test_importItemsPendingScanningDiskProgressForDomainWithID:completionHandler:]_block_invoke.480
+ ___98-[FPDXPCServicer _test_importItemsPendingReconciliationProgressForDomainWithID:completionHandler:]_block_invoke.477
+ ___98-[FPDXPCServicer spotlightReindexItemsWithIdentifiers:bundleID:protectionClass:completionHandler:]_block_invoke.412
+ ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e57_v32?0"NSString"8"FPSandboxingURLWrapper"16"NSError"24ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e30_v24?0"FPItemID"8"NSError"16ls32l8s40l8s48l8s64l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s72l8s56l8s64l8
+ ___block_literal_global.266
+ ___block_literal_global.292
+ ___block_literal_global.418
+ ___unnamed_56
+ __canBundleIDTriggerTTRForFailure:.expectedFailures
+ __canBundleIDTriggerTTRForFailure:.onceToken
+ _block_copy_helper.123
+ _block_copy_helper.126
+ _block_copy_helper.17
+ _block_copy_helper.2055
+ _block_copy_helper.2090
+ _block_copy_helper.2102
+ _block_copy_helper.2112
+ _block_copy_helper.2124
+ _block_copy_helper.2179
+ _block_copy_helper.2182
+ _block_copy_helper.2188
+ _block_copy_helper.2191
+ _block_copy_helper.2217
+ _block_copy_helper.2229
+ _block_copy_helper.2275
+ _block_copy_helper.2278
+ _block_copy_helper.2350
+ _block_copy_helper.2362
+ _block_copy_helper.239
+ _block_copy_helper.2413
+ _block_copy_helper.2416
+ _block_copy_helper.2446
+ _block_copy_helper.2449
+ _block_copy_helper.2458
+ _block_copy_helper.2528
+ _block_copy_helper.2531
+ _block_copy_helper.2555
+ _block_copy_helper.2558
+ _block_copy_helper.2588
+ _block_copy_helper.2591
+ _block_copy_helper.2621
+ _block_copy_helper.2624
+ _block_copy_helper.2647
+ _block_copy_helper.2650
+ _block_copy_helper.2680
+ _block_copy_helper.2683
+ _block_copy_helper.2699
+ _block_copy_helper.2711
+ _block_copy_helper.2766
+ _block_copy_helper.2769
+ _block_copy_helper.2833
+ _block_copy_helper.2836
+ _block_copy_helper.2839
+ _block_copy_helper.2898
+ _block_copy_helper.2901
+ _block_copy_helper.292
+ _block_copy_helper.2956
+ _block_copy_helper.2959
+ _block_copy_helper.2982
+ _block_copy_helper.2985
+ _block_copy_helper.3005
+ _block_copy_helper.3135
+ _block_copy_helper.3138
+ _block_copy_helper.3160
+ _block_copy_helper.3182
+ _block_copy_helper.3221
+ _block_copy_helper.3247
+ _block_copy_helper.3250
+ _block_copy_helper.3290
+ _block_copy_helper.330
+ _block_copy_helper.3304
+ _block_copy_helper.3354
+ _block_copy_helper.3357
+ _block_copy_helper.337
+ _block_copy_helper.3371
+ _block_copy_helper.3408
+ _block_copy_helper.3418
+ _block_copy_helper.3428
+ _block_copy_helper.3438
+ _block_copy_helper.3448
+ _block_copy_helper.3458
+ _block_copy_helper.3481
+ _block_copy_helper.3491
+ _block_copy_helper.3502
+ _block_copy_helper.3512
+ _block_copy_helper.3522
+ _block_copy_helper.3532
+ _block_copy_helper.3550
+ _block_copy_helper.3576
+ _block_copy_helper.3579
+ _block_copy_helper.3589
+ _block_copy_helper.3592
+ _block_copy_helper.3605
+ _block_copy_helper.3634
+ _block_copy_helper.3644
+ _block_copy_helper.3656
+ _block_copy_helper.3731
+ _block_copy_helper.3761
+ _block_copy_helper.3771
+ _block_copy_helper.3783
+ _block_copy_helper.3891
+ _block_copy_helper.3894
+ _block_copy_helper.3903
+ _block_copy_helper.3943
+ _block_copy_helper.4004
+ _block_copy_helper.4007
+ _block_copy_helper.4017
+ _block_copy_helper.4037
+ _block_copy_helper.4040
+ _block_copy_helper.4052
+ _block_copy_helper.4085
+ _block_copy_helper.4088
+ _block_copy_helper.4091
+ _block_copy_helper.4108
+ _block_copy_helper.4141
+ _block_copy_helper.4146
+ _block_copy_helper.4151
+ _block_copy_helper.4161
+ _block_copy_helper.4187
+ _block_copy_helper.4199
+ _block_copy_helper.4207
+ _block_copy_helper.4362
+ _block_copy_helper.4415
+ _block_copy_helper.4418
+ _block_copy_helper.4531
+ _block_copy_helper.4534
+ _block_copy_helper.4596
+ _block_copy_helper.4654
+ _block_copy_helper.4657
+ _block_copy_helper.4660
+ _block_copy_helper.4663
+ _block_copy_helper.4684
+ _block_copy_helper.4687
+ _block_copy_helper.4720
+ _block_copy_helper.4723
+ _block_copy_helper.4743
+ _block_copy_helper.4755
+ _block_copy_helper.4767
+ _block_copy_helper.4779
+ _block_copy_helper.4789
+ _block_copy_helper.4801
+ _block_copy_helper.4858
+ _block_copy_helper.4865
+ _block_copy_helper.4872
+ _block_copy_helper.4882
+ _block_copy_helper.4892
+ _block_copy_helper.4902
+ _block_copy_helper.4912
+ _block_copy_helper.4918
+ _block_copy_helper.4925
+ _block_copy_helper.4935
+ _block_copy_helper.4945
+ _block_copy_helper.4952
+ _block_copy_helper.4962
+ _block_copy_helper.4969
+ _block_copy_helper.4976
+ _block_copy_helper.4983
+ _block_copy_helper.5034
+ _block_copy_helper.5144
+ _block_copy_helper.5192
+ _block_copy_helper.5232
+ _block_copy_helper.5264
+ _block_copy_helper.5274
+ _block_copy_helper.5284
+ _block_copy_helper.5356
+ _block_copy_helper.5365
+ _block_copy_helper.5377
+ _block_copy_helper.5383
+ _block_copy_helper.5395
+ _block_copy_helper.5407
+ _block_copy_helper.5419
+ _block_copy_helper.5425
+ _block_copy_helper.5437
+ _block_copy_helper.5467
+ _block_copy_helper.5554
+ _block_copy_helper.5586
+ _block_copy_helper.5589
+ _block_copy_helper.5602
+ _block_copy_helper.5608
+ _block_copy_helper.5616
+ _block_copy_helper.5625
+ _block_copy_helper.5636
+ _block_copy_helper.5642
+ _block_copy_helper.5654
+ _block_copy_helper.5665
+ _block_copy_helper.5678
+ _block_copy_helper.5689
+ _block_copy_helper.5700
+ _block_copy_helper.5706
+ _block_copy_helper.5718
+ _block_copy_helper.5816
+ _block_copy_helper.5958
+ _block_copy_helper.6016
+ _block_copy_helper.6045
+ _block_copy_helper.6074
+ _block_copy_helper.6104
+ _block_copy_helper.6140
+ _block_copy_helper.6185
+ _block_copy_helper.6195
+ _block_copy_helper.6227
+ _block_copy_helper.6237
+ _block_copy_helper.6248
+ _block_copy_helper.6259
+ _block_copy_helper.6314
+ _block_copy_helper.6323
+ _block_copy_helper.6340
+ _block_copy_helper.6358
+ _block_copy_helper.6370
+ _block_copy_helper.6388
+ _block_copy_helper.6400
+ _block_copy_helper.6418
+ _block_copy_helper.6428
+ _block_copy_helper.6463
+ _block_copy_helper.6472
+ _block_copy_helper.6509
+ _block_descriptor.125
+ _block_descriptor.128
+ _block_descriptor.19
+ _block_descriptor.2057
+ _block_descriptor.2092
+ _block_descriptor.2104
+ _block_descriptor.2114
+ _block_descriptor.2126
+ _block_descriptor.2181
+ _block_descriptor.2184
+ _block_descriptor.2190
+ _block_descriptor.2193
+ _block_descriptor.2219
+ _block_descriptor.2231
+ _block_descriptor.2277
+ _block_descriptor.2280
+ _block_descriptor.2352
+ _block_descriptor.2364
+ _block_descriptor.241
+ _block_descriptor.2415
+ _block_descriptor.2418
+ _block_descriptor.2448
+ _block_descriptor.2451
+ _block_descriptor.2460
+ _block_descriptor.2530
+ _block_descriptor.2533
+ _block_descriptor.2557
+ _block_descriptor.2560
+ _block_descriptor.2590
+ _block_descriptor.2593
+ _block_descriptor.2623
+ _block_descriptor.2626
+ _block_descriptor.2649
+ _block_descriptor.2652
+ _block_descriptor.2682
+ _block_descriptor.2685
+ _block_descriptor.2701
+ _block_descriptor.2713
+ _block_descriptor.2768
+ _block_descriptor.2771
+ _block_descriptor.2835
+ _block_descriptor.2838
+ _block_descriptor.2841
+ _block_descriptor.2900
+ _block_descriptor.2903
+ _block_descriptor.294
+ _block_descriptor.2958
+ _block_descriptor.2961
+ _block_descriptor.2984
+ _block_descriptor.2987
+ _block_descriptor.3007
+ _block_descriptor.3137
+ _block_descriptor.3140
+ _block_descriptor.3162
+ _block_descriptor.3184
+ _block_descriptor.3223
+ _block_descriptor.3249
+ _block_descriptor.3252
+ _block_descriptor.3292
+ _block_descriptor.3306
+ _block_descriptor.332
+ _block_descriptor.3356
+ _block_descriptor.3359
+ _block_descriptor.3373
+ _block_descriptor.339
+ _block_descriptor.3410
+ _block_descriptor.3420
+ _block_descriptor.3430
+ _block_descriptor.3440
+ _block_descriptor.3450
+ _block_descriptor.3460
+ _block_descriptor.3483
+ _block_descriptor.3493
+ _block_descriptor.3504
+ _block_descriptor.3514
+ _block_descriptor.3524
+ _block_descriptor.3534
+ _block_descriptor.3552
+ _block_descriptor.3578
+ _block_descriptor.3581
+ _block_descriptor.3591
+ _block_descriptor.3594
+ _block_descriptor.3607
+ _block_descriptor.3636
+ _block_descriptor.3646
+ _block_descriptor.3658
+ _block_descriptor.3733
+ _block_descriptor.3763
+ _block_descriptor.3773
+ _block_descriptor.3785
+ _block_descriptor.3893
+ _block_descriptor.3896
+ _block_descriptor.3905
+ _block_descriptor.3945
+ _block_descriptor.4006
+ _block_descriptor.4009
+ _block_descriptor.4019
+ _block_descriptor.4039
+ _block_descriptor.4042
+ _block_descriptor.4054
+ _block_descriptor.4087
+ _block_descriptor.4090
+ _block_descriptor.4093
+ _block_descriptor.4110
+ _block_descriptor.4143
+ _block_descriptor.4148
+ _block_descriptor.4153
+ _block_descriptor.4163
+ _block_descriptor.4189
+ _block_descriptor.4201
+ _block_descriptor.4209
+ _block_descriptor.4364
+ _block_descriptor.4417
+ _block_descriptor.4420
+ _block_descriptor.4533
+ _block_descriptor.4536
+ _block_descriptor.4598
+ _block_descriptor.4656
+ _block_descriptor.4659
+ _block_descriptor.4662
+ _block_descriptor.4665
+ _block_descriptor.4686
+ _block_descriptor.4689
+ _block_descriptor.4722
+ _block_descriptor.4725
+ _block_descriptor.4745
+ _block_descriptor.4757
+ _block_descriptor.4769
+ _block_descriptor.4781
+ _block_descriptor.4791
+ _block_descriptor.4803
+ _block_descriptor.4860
+ _block_descriptor.4867
+ _block_descriptor.4874
+ _block_descriptor.4884
+ _block_descriptor.4894
+ _block_descriptor.4904
+ _block_descriptor.4914
+ _block_descriptor.4920
+ _block_descriptor.4927
+ _block_descriptor.4937
+ _block_descriptor.4947
+ _block_descriptor.4954
+ _block_descriptor.4964
+ _block_descriptor.4971
+ _block_descriptor.4978
+ _block_descriptor.4985
+ _block_descriptor.5036
+ _block_descriptor.5146
+ _block_descriptor.5194
+ _block_descriptor.5234
+ _block_descriptor.5266
+ _block_descriptor.5276
+ _block_descriptor.5286
+ _block_descriptor.5358
+ _block_descriptor.5367
+ _block_descriptor.5379
+ _block_descriptor.5385
+ _block_descriptor.5397
+ _block_descriptor.5409
+ _block_descriptor.5421
+ _block_descriptor.5427
+ _block_descriptor.5439
+ _block_descriptor.5469
+ _block_descriptor.5556
+ _block_descriptor.5588
+ _block_descriptor.5591
+ _block_descriptor.5604
+ _block_descriptor.5610
+ _block_descriptor.5618
+ _block_descriptor.5627
+ _block_descriptor.5638
+ _block_descriptor.5644
+ _block_descriptor.5656
+ _block_descriptor.5667
+ _block_descriptor.5680
+ _block_descriptor.5691
+ _block_descriptor.5702
+ _block_descriptor.5708
+ _block_descriptor.5720
+ _block_descriptor.5818
+ _block_descriptor.5960
+ _block_descriptor.6018
+ _block_descriptor.6047
+ _block_descriptor.6076
+ _block_descriptor.6106
+ _block_descriptor.6142
+ _block_descriptor.6187
+ _block_descriptor.6197
+ _block_descriptor.6229
+ _block_descriptor.6239
+ _block_descriptor.6250
+ _block_descriptor.6261
+ _block_descriptor.6316
+ _block_descriptor.6325
+ _block_descriptor.6342
+ _block_descriptor.6360
+ _block_descriptor.6372
+ _block_descriptor.6390
+ _block_descriptor.6402
+ _block_descriptor.6420
+ _block_descriptor.6430
+ _block_descriptor.6465
+ _block_descriptor.6474
+ _block_descriptor.6511
+ _block_destroy_helper.124
+ _block_destroy_helper.127
+ _block_destroy_helper.18
+ _block_destroy_helper.2056
+ _block_destroy_helper.2091
+ _block_destroy_helper.2103
+ _block_destroy_helper.2113
+ _block_destroy_helper.2125
+ _block_destroy_helper.2180
+ _block_destroy_helper.2183
+ _block_destroy_helper.2189
+ _block_destroy_helper.2192
+ _block_destroy_helper.2218
+ _block_destroy_helper.2230
+ _block_destroy_helper.2276
+ _block_destroy_helper.2279
+ _block_destroy_helper.2351
+ _block_destroy_helper.2363
+ _block_destroy_helper.240
+ _block_destroy_helper.2414
+ _block_destroy_helper.2417
+ _block_destroy_helper.2447
+ _block_destroy_helper.2450
+ _block_destroy_helper.2459
+ _block_destroy_helper.2529
+ _block_destroy_helper.2532
+ _block_destroy_helper.2556
+ _block_destroy_helper.2559
+ _block_destroy_helper.2589
+ _block_destroy_helper.2592
+ _block_destroy_helper.2622
+ _block_destroy_helper.2625
+ _block_destroy_helper.2648
+ _block_destroy_helper.2651
+ _block_destroy_helper.2681
+ _block_destroy_helper.2684
+ _block_destroy_helper.2700
+ _block_destroy_helper.2712
+ _block_destroy_helper.2767
+ _block_destroy_helper.2770
+ _block_destroy_helper.2834
+ _block_destroy_helper.2837
+ _block_destroy_helper.2840
+ _block_destroy_helper.2899
+ _block_destroy_helper.2902
+ _block_destroy_helper.293
+ _block_destroy_helper.2957
+ _block_destroy_helper.2960
+ _block_destroy_helper.2983
+ _block_destroy_helper.2986
+ _block_destroy_helper.3006
+ _block_destroy_helper.3136
+ _block_destroy_helper.3139
+ _block_destroy_helper.3161
+ _block_destroy_helper.3183
+ _block_destroy_helper.3222
+ _block_destroy_helper.3248
+ _block_destroy_helper.3251
+ _block_destroy_helper.3291
+ _block_destroy_helper.3305
+ _block_destroy_helper.331
+ _block_destroy_helper.3355
+ _block_destroy_helper.3358
+ _block_destroy_helper.3372
+ _block_destroy_helper.338
+ _block_destroy_helper.3409
+ _block_destroy_helper.3419
+ _block_destroy_helper.3429
+ _block_destroy_helper.3439
+ _block_destroy_helper.3449
+ _block_destroy_helper.3459
+ _block_destroy_helper.3482
+ _block_destroy_helper.3492
+ _block_destroy_helper.3503
+ _block_destroy_helper.3513
+ _block_destroy_helper.3523
+ _block_destroy_helper.3533
+ _block_destroy_helper.3551
+ _block_destroy_helper.3577
+ _block_destroy_helper.3580
+ _block_destroy_helper.3590
+ _block_destroy_helper.3593
+ _block_destroy_helper.3606
+ _block_destroy_helper.3635
+ _block_destroy_helper.3645
+ _block_destroy_helper.3657
+ _block_destroy_helper.3732
+ _block_destroy_helper.3762
+ _block_destroy_helper.3772
+ _block_destroy_helper.3784
+ _block_destroy_helper.3892
+ _block_destroy_helper.3895
+ _block_destroy_helper.3904
+ _block_destroy_helper.3944
+ _block_destroy_helper.4005
+ _block_destroy_helper.4008
+ _block_destroy_helper.4018
+ _block_destroy_helper.4038
+ _block_destroy_helper.4041
+ _block_destroy_helper.4053
+ _block_destroy_helper.4086
+ _block_destroy_helper.4089
+ _block_destroy_helper.4092
+ _block_destroy_helper.4109
+ _block_destroy_helper.4142
+ _block_destroy_helper.4147
+ _block_destroy_helper.4152
+ _block_destroy_helper.4162
+ _block_destroy_helper.4188
+ _block_destroy_helper.4200
+ _block_destroy_helper.4208
+ _block_destroy_helper.4363
+ _block_destroy_helper.4416
+ _block_destroy_helper.4419
+ _block_destroy_helper.4532
+ _block_destroy_helper.4535
+ _block_destroy_helper.4597
+ _block_destroy_helper.4655
+ _block_destroy_helper.4658
+ _block_destroy_helper.4661
+ _block_destroy_helper.4664
+ _block_destroy_helper.4685
+ _block_destroy_helper.4688
+ _block_destroy_helper.4721
+ _block_destroy_helper.4724
+ _block_destroy_helper.4744
+ _block_destroy_helper.4756
+ _block_destroy_helper.4768
+ _block_destroy_helper.4780
+ _block_destroy_helper.4790
+ _block_destroy_helper.4802
+ _block_destroy_helper.4859
+ _block_destroy_helper.4866
+ _block_destroy_helper.4873
+ _block_destroy_helper.4883
+ _block_destroy_helper.4893
+ _block_destroy_helper.4903
+ _block_destroy_helper.4913
+ _block_destroy_helper.4919
+ _block_destroy_helper.4926
+ _block_destroy_helper.4936
+ _block_destroy_helper.4946
+ _block_destroy_helper.4953
+ _block_destroy_helper.4963
+ _block_destroy_helper.4970
+ _block_destroy_helper.4977
+ _block_destroy_helper.4984
+ _block_destroy_helper.5035
+ _block_destroy_helper.5145
+ _block_destroy_helper.5193
+ _block_destroy_helper.5233
+ _block_destroy_helper.5265
+ _block_destroy_helper.5275
+ _block_destroy_helper.5285
+ _block_destroy_helper.5357
+ _block_destroy_helper.5366
+ _block_destroy_helper.5378
+ _block_destroy_helper.5384
+ _block_destroy_helper.5396
+ _block_destroy_helper.5408
+ _block_destroy_helper.5420
+ _block_destroy_helper.5426
+ _block_destroy_helper.5438
+ _block_destroy_helper.5468
+ _block_destroy_helper.5555
+ _block_destroy_helper.5587
+ _block_destroy_helper.5590
+ _block_destroy_helper.5603
+ _block_destroy_helper.5609
+ _block_destroy_helper.5617
+ _block_destroy_helper.5626
+ _block_destroy_helper.5637
+ _block_destroy_helper.5643
+ _block_destroy_helper.5655
+ _block_destroy_helper.5666
+ _block_destroy_helper.5679
+ _block_destroy_helper.5690
+ _block_destroy_helper.5701
+ _block_destroy_helper.5707
+ _block_destroy_helper.5719
+ _block_destroy_helper.5817
+ _block_destroy_helper.5959
+ _block_destroy_helper.6017
+ _block_destroy_helper.6046
+ _block_destroy_helper.6075
+ _block_destroy_helper.6105
+ _block_destroy_helper.6141
+ _block_destroy_helper.6186
+ _block_destroy_helper.6196
+ _block_destroy_helper.6228
+ _block_destroy_helper.6238
+ _block_destroy_helper.6249
+ _block_destroy_helper.6260
+ _block_destroy_helper.6315
+ _block_destroy_helper.6324
+ _block_destroy_helper.6341
+ _block_destroy_helper.6359
+ _block_destroy_helper.6371
+ _block_destroy_helper.6389
+ _block_destroy_helper.6401
+ _block_destroy_helper.6419
+ _block_destroy_helper.6429
+ _block_destroy_helper.6464
+ _block_destroy_helper.6473
+ _block_destroy_helper.6510
+ _fpfs_fget_decmpf_info
+ _get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization6AtomicVySbG.2
+ _get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization6AtomicVySo45FPDExclusiveSharedSystemSchedulerWatcherStateVG.3
+ _get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization6AtomicVys5Int64VG.4
+ _objc_msgSend$_canBundleIDTriggerTTRForFailure:
+ _objc_msgSend$addValue:forKey:
+ _objc_msgSend$initWithEventName:
+ _objc_msgSend$sendReport
+ _objc_msgSend$updating
+ _objectdestroy.2205Tm
+ _objectdestroy.2208Tm
+ _objectdestroy.2299Tm
+ _objectdestroy.2308Tm
+ _objectdestroy.2314Tm
+ _objectdestroy.2317Tm
+ _objectdestroy.2395Tm
+ _objectdestroy.2404Tm
+ _objectdestroy.2436Tm
+ _objectdestroy.2545Tm
+ _objectdestroy.2756Tm
+ _objectdestroy.2776Tm
+ _objectdestroy.2779Tm
+ _objectdestroy.2880Tm
+ _objectdestroy.2992Tm
+ _objectdestroy.2995Tm
+ _objectdestroy.3029Tm
+ _objectdestroy.3122Tm
+ _objectdestroy.3146Tm
+ _objectdestroy.3192Tm
+ _objectdestroy.3202Tm
+ _objectdestroy.3205Tm
+ _objectdestroy.3208Tm
+ _objectdestroy.3282Tm
+ _objectdestroy.3288Tm
+ _objectdestroy.3299Tm
+ _objectdestroy.3333Tm
+ _objectdestroy.3432Tm
+ _objectdestroy.3673Tm
+ _objectdestroy.3687Tm
+ _objectdestroy.3809Tm
+ _objectdestroy.3878Tm
+ _objectdestroy.3882Tm
+ _objectdestroy.4118Tm
+ _objectdestroy.4248Tm
+ _objectdestroy.4274Tm
+ _objectdestroy.4294Tm
+ _objectdestroy.4590Tm
+ _objectdestroy.4811Tm
+ _objectdestroy.5118Tm
+ _objectdestroy.5123Tm
+ _objectdestroy.5161Tm
+ _objectdestroy.5820Tm
+ _objectdestroy.5851Tm
+ _objectdestroy.5906Tm
+ _objectdestroy.5916Tm
+ _objectdestroy.5975Tm
+ _objectdestroy.5982Tm
+ _objectdestroy.6020Tm
+ _objectdestroy.6183Tm
+ _symbolic _____ 18FileProviderDaemon11MaintenanceO37FixParentMaterializationStuckOnImportC
+ _symbolic ______p 10Foundation15ContiguousBytesP
+ _symbolic ______pSg 10Foundation15ContiguousBytesP
+ _symbolic _____ySo6FPItemC______G 18FileProviderDaemon11MaintenanceO37FixParentMaterializationStuckOnImportC AA7VFSItemV
+ _symbolic _____y_____AB_G 18FileProviderDaemon11MaintenanceO37FixParentMaterializationStuckOnImportC AA7VFSItemV
+ _symbolic _____y_____So6FPItemCGyt______pIeggIrzo_ 18FileProviderDaemon20StuckDeletionMonitorC AA7VFSItemV s5ErrorP
+ _symbolic _____y_____So6FPItemCGyt______pIggIrzo_ 18FileProviderDaemon20StuckDeletionMonitorC AA7VFSItemV s5ErrorP
+ _symbolic _____y_____So6FPItemC_G 18FileProviderDaemon11MaintenanceO37FixParentMaterializationStuckOnImportC AA7VFSItemV
+ _symbolic _____y_____So6FPItemC_____yAbDG_____yAbDG_____yAbDGGShy_____y__________GG______pIeggIrzo_ 18FileProviderDaemon20FPDiagnosticsManagerC AA7VFSItemV AA0D13DBQueriesImplC AA010FPFeedbackE0C AA012FPTapToRadarE0C AA16ReconciliationIDO AA0fN0O So06NSFileB14ItemIdentifiera s5ErrorP
+ _symbolic _____y_____So6FPItemC_____yAbDG_____yAbDG_____yAbDGGShy_____y__________GG______pIggIrzo_ 18FileProviderDaemon20FPDiagnosticsManagerC AA7VFSItemV AA0D13DBQueriesImplC AA010FPFeedbackE0C AA012FPTapToRadarE0C AA16ReconciliationIDO AA0fN0O So06NSFileB14ItemIdentifiera s5ErrorP
+ _symbolic _____y_____So6FPItemC_____yAbDG_____yAbDG_____yAbDGGyt______pIeggIrzo_ 18FileProviderDaemon20FPDiagnosticsManagerC AA7VFSItemV AA0D13DBQueriesImplC AA010FPFeedbackE0C AA012FPTapToRadarE0C s5ErrorP
+ _symbolic _____y_____So6FPItemC_____yAbDG_____yAbDG_____yAbDGGyt______pIggIrzo_ 18FileProviderDaemon20FPDiagnosticsManagerC AA7VFSItemV AA0D13DBQueriesImplC AA010FPFeedbackE0C AA012FPTapToRadarE0C s5ErrorP
- -[FPDiagnosticCollector initWithFD:trashURL:]
- GCC_except_table164
- GCC_except_table193
- GCC_except_table194
- GCC_except_table197
- GCC_except_table200
- GCC_except_table215
- GCC_except_table224
- GCC_except_table243
- GCC_except_table244
- GCC_except_table249
- GCC_except_table250
- GCC_except_table255
- GCC_except_table256
- GCC_except_table265
- GCC_except_table271
- GCC_except_table274
- GCC_except_table275
- GCC_except_table280
- GCC_except_table287
- GCC_except_table298
- GCC_except_table303
- GCC_except_table317
- GCC_except_table362
- GCC_except_table365
- GCC_except_table368
- GCC_except_table372
- GCC_except_table397
- GCC_except_table398
- GCC_except_table401
- GCC_except_table404
- GCC_except_table411
- GCC_except_table415
- GCC_except_table416
- GCC_except_table421
- GCC_except_table426
- GCC_except_table430
- GCC_except_table431
- GCC_except_table439
- GCC_except_table442
- GCC_except_table448
- GCC_except_table449
- GCC_except_table454
- GCC_except_table462
- GCC_except_table466
- GCC_except_table468
- GCC_except_table470
- GCC_except_table472
- GCC_except_table474
- ___100-[FPDXPCServicer _test_importItemsPendingScanningProviderProgressForDomainWithID:completionHandler:]_block_invoke.475
- ___100-[FPDXPCServicer uploadLocalVersionOfItemAtURL:bundleID:conflictResolutionPolicy:completionHandler:]_block_invoke.499
- ___133-[FPDXPCServicer runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:]_block_invoke.315
- ___133-[FPDXPCServicer runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:]_block_invoke.315.cold.1
- ___133-[FPDXPCServicer runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:]_block_invoke.318
- ___53-[FPDXPCServicer pauseIndexingFor:completionHandler:]_block_invoke.449
- ___54-[FPDXPCServicer resumeIndexingFor:completionHandler:]_block_invoke.450
- ___57-[FPDXPCServicer stateForDomainWithID:completionHandler:]_block_invoke.313
- ___59-[FPDXPCServicer _test_purgerBarrierWithCompletionHandler:]_block_invoke.482
- ___59-[FPDXPCServicer _test_purgerBarrierWithCompletionHandler:]_block_invoke.482.cold.1
- ___59-[FPDXPCServicer appHasNonUploadedFiles:completionHandler:]_block_invoke.326
- ___63-[FPDXPCServicer fetchDaemonOperationIDsWithCompletionHandler:]_block_invoke.407
- ___65-[FPDXPCServicer _test_resetDBQueryStatistics:completionHandler:]_block_invoke.477
- ___66-[FPDXPCServicer importProgressForDomainWithID:completionHandler:]_block_invoke.311
- ___67-[FPDXPCServicer _test_disableDBQueryStatistics:completionHandler:]_block_invoke.476
- ___67-[FPDXPCServicer dumpTelemetryTo:providerFilter:completionHandler:]_block_invoke.384
- ___68-[FPDXPCServicer dumpDatabaseAt:fullDump:writeTo:completionHandler:]_block_invoke.321
- ___68-[FPDXPCServicer scheduleActionOperationWithInfo:completionHandler:]_block_invoke.405
- ___70-[FPDXPCServicer _test_triggerDatabaseError:domain:completionHandler:]_block_invoke.481
- ___70-[FPDXPCServicer copyDatabaseForFPCKStartingAtPath:completionHandler:]_block_invoke.398
- ___71-[FPDXPCServicer dumpStateTo:providerFilter:options:completionHandler:]_block_invoke.367
- ___73-[FPDXPCServicer _test_getDBQueryStatistics:queryPlan:completionHandler:]_block_invoke.478
- ___73-[FPDXPCServicer waitForChangesOnItemsBelowItemWithID:completionHandler:]_block_invoke.401
- ___74-[FPDXPCServicer startAccessingServiceWithName:itemURL:completionHandler:]_block_invoke.418
- ___76-[FPDXPCServicer fetchLatestVersionForItemAtURL:bundleID:completionHandler:]_block_invoke.492
- ___76-[FPDXPCServicer pauseSyncForItemAtURL:behavior:bundleID:completionHandler:]_block_invoke.486
- ___76-[FPDXPCServicer waitForStabilizationOfDomainWithID:mode:completionHandler:]_block_invoke.402
- ___77-[FPDXPCServicer _performWithCheckedEnumerationAttributes:completionHandler:]_block_invoke.428
- ___77-[FPDXPCServicer forceUpdateBlockedProcessNamesFromDomain:completionHandler:]_block_invoke.308
- ___77-[FPDXPCServicer resumeSyncForItemAtURL:behavior:bundleID:completionHandler:]_block_invoke.489
- ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.458
- ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.458.cold.1
- ___82-[FPDXPCServicer fetchAndStartEnumeratingWithSettings:observer:completionHandler:]_block_invoke.434
- ___82-[FPDXPCServicer reimportItemsBelowItemWithID:markItemDataless:completionHandler:]_block_invoke.307
- ___85-[FPDXPCServicer enumerateSearchResultForRequest:providerDomainID:completionHandler:]_block_invoke.423
- ___86-[FPDXPCServicer setEnabled:forDomainIdentifier:providerIdentifier:completionHandler:]_block_invoke.304
- ___88-[FPDXPCServicer spotlightReindexAllItemsForBundleID:protectionClass:completionHandler:]_block_invoke.403
- ___91-[FPDXPCServicer setHiddenByUser:forDomainIdentifier:providerIdentifier:completionHandler:]_block_invoke.305
- ___93-[FPDXPCServicer signalReindexCSIdentifiersByProviderDomainID:indexReason:completionHandler:]_block_invoke.451
- ___93-[FPDXPCServicer signalReindexCSIdentifiersByProviderDomainID:indexReason:completionHandler:]_block_invoke.451.cold.1
- ___93-[FPDXPCServicer signalReindexCSIdentifiersByProviderDomainID:indexReason:completionHandler:]_block_invoke.451.cold.2
- ___94-[FPDXPCServicer setIndexingEnabled:forDomainIdentifier:providerIdentifier:completionHandler:]_block_invoke.306
- ___96-[FPDXPCServicer _test_importItemsPendingScanningDiskProgressForDomainWithID:completionHandler:]_block_invoke.472
- ___98-[FPDXPCServicer _test_importItemsPendingReconciliationProgressForDomainWithID:completionHandler:]_block_invoke.469
- ___98-[FPDXPCServicer spotlightReindexItemsWithIdentifiers:bundleID:protectionClass:completionHandler:]_block_invoke.404
- ___block_descriptor_48_e8_32s40bs_e57_v32?0"NSString"8"FPSandboxingURLWrapper"16"NSError"24ls32l8s40l8
- ___block_literal_global.253
- ___block_literal_global.261
- ___block_literal_global.410
- _block_copy_helper.125
- _block_copy_helper.135
- _block_copy_helper.165
- _block_copy_helper.175
- _block_copy_helper.2083
- _block_copy_helper.2095
- _block_copy_helper.2105
- _block_copy_helper.2117
- _block_copy_helper.2172
- _block_copy_helper.2175
- _block_copy_helper.2181
- _block_copy_helper.2184
- _block_copy_helper.2210
- _block_copy_helper.2222
- _block_copy_helper.2268
- _block_copy_helper.2271
- _block_copy_helper.2343
- _block_copy_helper.2355
- _block_copy_helper.238
- _block_copy_helper.2406
- _block_copy_helper.2409
- _block_copy_helper.2439
- _block_copy_helper.2442
- _block_copy_helper.2451
- _block_copy_helper.251
- _block_copy_helper.2521
- _block_copy_helper.2524
- _block_copy_helper.2548
- _block_copy_helper.2551
- _block_copy_helper.2581
- _block_copy_helper.2584
- _block_copy_helper.2614
- _block_copy_helper.2617
- _block_copy_helper.2640
- _block_copy_helper.2643
- _block_copy_helper.2673
- _block_copy_helper.2676
- _block_copy_helper.2692
- _block_copy_helper.270
- _block_copy_helper.2704
- _block_copy_helper.2759
- _block_copy_helper.2762
- _block_copy_helper.279
- _block_copy_helper.2826
- _block_copy_helper.2829
- _block_copy_helper.2832
- _block_copy_helper.2891
- _block_copy_helper.2894
- _block_copy_helper.291
- _block_copy_helper.2949
- _block_copy_helper.2952
- _block_copy_helper.2975
- _block_copy_helper.2978
- _block_copy_helper.2998
- _block_copy_helper.304
- _block_copy_helper.3128
- _block_copy_helper.3131
- _block_copy_helper.3153
- _block_copy_helper.3175
- _block_copy_helper.3214
- _block_copy_helper.3240
- _block_copy_helper.3243
- _block_copy_helper.3283
- _block_copy_helper.3297
- _block_copy_helper.3347
- _block_copy_helper.3350
- _block_copy_helper.3364
- _block_copy_helper.3401
- _block_copy_helper.3411
- _block_copy_helper.3421
- _block_copy_helper.3431
- _block_copy_helper.3441
- _block_copy_helper.3451
- _block_copy_helper.3467
- _block_copy_helper.3484
- _block_copy_helper.3495
- _block_copy_helper.3505
- _block_copy_helper.3515
- _block_copy_helper.3525
- _block_copy_helper.3543
- _block_copy_helper.3569
- _block_copy_helper.3572
- _block_copy_helper.3582
- _block_copy_helper.3585
- _block_copy_helper.3598
- _block_copy_helper.3627
- _block_copy_helper.3630
- _block_copy_helper.3649
- _block_copy_helper.3724
- _block_copy_helper.3754
- _block_copy_helper.3757
- _block_copy_helper.3776
- _block_copy_helper.3884
- _block_copy_helper.3887
- _block_copy_helper.3896
- _block_copy_helper.3936
- _block_copy_helper.3997
- _block_copy_helper.4000
- _block_copy_helper.4010
- _block_copy_helper.4030
- _block_copy_helper.4033
- _block_copy_helper.4045
- _block_copy_helper.4078
- _block_copy_helper.4081
- _block_copy_helper.4084
- _block_copy_helper.4101
- _block_copy_helper.4134
- _block_copy_helper.4139
- _block_copy_helper.4144
- _block_copy_helper.4154
- _block_copy_helper.4180
- _block_copy_helper.4192
- _block_copy_helper.4200
- _block_copy_helper.4355
- _block_copy_helper.4408
- _block_copy_helper.4411
- _block_copy_helper.4524
- _block_copy_helper.4527
- _block_copy_helper.4589
- _block_copy_helper.4647
- _block_copy_helper.4650
- _block_copy_helper.4653
- _block_copy_helper.4656
- _block_copy_helper.4677
- _block_copy_helper.4680
- _block_copy_helper.4713
- _block_copy_helper.4716
- _block_copy_helper.4736
- _block_copy_helper.4746
- _block_copy_helper.4758
- _block_copy_helper.4770
- _block_copy_helper.4777
- _block_copy_helper.4787
- _block_copy_helper.4798
- _block_copy_helper.4855
- _block_copy_helper.4862
- _block_copy_helper.4869
- _block_copy_helper.4879
- _block_copy_helper.4889
- _block_copy_helper.4899
- _block_copy_helper.4909
- _block_copy_helper.4915
- _block_copy_helper.4922
- _block_copy_helper.4932
- _block_copy_helper.4942
- _block_copy_helper.4949
- _block_copy_helper.4959
- _block_copy_helper.4966
- _block_copy_helper.4973
- _block_copy_helper.4980
- _block_copy_helper.5031
- _block_copy_helper.5138
- _block_copy_helper.5189
- _block_copy_helper.5229
- _block_copy_helper.5258
- _block_copy_helper.5271
- _block_copy_helper.5281
- _block_copy_helper.5350
- _block_copy_helper.5362
- _block_copy_helper.5374
- _block_copy_helper.5380
- _block_copy_helper.5392
- _block_copy_helper.5404
- _block_copy_helper.5416
- _block_copy_helper.5422
- _block_copy_helper.5434
- _block_copy_helper.5461
- _block_copy_helper.5570
- _block_copy_helper.5573
- _block_copy_helper.5584
- _block_copy_helper.5596
- _block_copy_helper.5605
- _block_copy_helper.5613
- _block_copy_helper.5622
- _block_copy_helper.5633
- _block_copy_helper.5639
- _block_copy_helper.5651
- _block_copy_helper.5662
- _block_copy_helper.5675
- _block_copy_helper.5686
- _block_copy_helper.5697
- _block_copy_helper.5703
- _block_copy_helper.5715
- _block_copy_helper.5810
- _block_copy_helper.5952
- _block_copy_helper.6010
- _block_copy_helper.6042
- _block_copy_helper.6068
- _block_copy_helper.6098
- _block_copy_helper.6134
- _block_copy_helper.6182
- _block_copy_helper.6192
- _block_copy_helper.6221
- _block_copy_helper.6234
- _block_copy_helper.6245
- _block_copy_helper.6256
- _block_copy_helper.6308
- _block_copy_helper.6317
- _block_copy_helper.6337
- _block_copy_helper.6355
- _block_copy_helper.6367
- _block_copy_helper.6385
- _block_copy_helper.6397
- _block_copy_helper.6415
- _block_copy_helper.6425
- _block_copy_helper.6457
- _block_copy_helper.6469
- _block_copy_helper.6503
- _block_copy_helper.84
- _block_copy_helper.94
- _block_descriptor.127
- _block_descriptor.137
- _block_descriptor.167
- _block_descriptor.177
- _block_descriptor.2085
- _block_descriptor.2097
- _block_descriptor.2107
- _block_descriptor.2119
- _block_descriptor.2174
- _block_descriptor.2177
- _block_descriptor.2183
- _block_descriptor.2186
- _block_descriptor.2212
- _block_descriptor.2224
- _block_descriptor.2270
- _block_descriptor.2273
- _block_descriptor.2345
- _block_descriptor.2357
- _block_descriptor.240
- _block_descriptor.2408
- _block_descriptor.2411
- _block_descriptor.2441
- _block_descriptor.2444
- _block_descriptor.2453
- _block_descriptor.2523
- _block_descriptor.2526
- _block_descriptor.253
- _block_descriptor.2550
- _block_descriptor.2553
- _block_descriptor.2583
- _block_descriptor.2586
- _block_descriptor.2616
- _block_descriptor.2619
- _block_descriptor.2642
- _block_descriptor.2645
- _block_descriptor.2675
- _block_descriptor.2678
- _block_descriptor.2694
- _block_descriptor.2706
- _block_descriptor.272
- _block_descriptor.2761
- _block_descriptor.2764
- _block_descriptor.281
- _block_descriptor.2828
- _block_descriptor.2831
- _block_descriptor.2834
- _block_descriptor.2893
- _block_descriptor.2896
- _block_descriptor.293
- _block_descriptor.2951
- _block_descriptor.2954
- _block_descriptor.2977
- _block_descriptor.2980
- _block_descriptor.3000
- _block_descriptor.306
- _block_descriptor.3130
- _block_descriptor.3133
- _block_descriptor.3155
- _block_descriptor.3177
- _block_descriptor.3216
- _block_descriptor.3242
- _block_descriptor.3245
- _block_descriptor.3285
- _block_descriptor.3299
- _block_descriptor.3349
- _block_descriptor.3352
- _block_descriptor.3366
- _block_descriptor.3403
- _block_descriptor.3413
- _block_descriptor.3423
- _block_descriptor.3433
- _block_descriptor.3443
- _block_descriptor.3453
- _block_descriptor.3469
- _block_descriptor.3486
- _block_descriptor.3497
- _block_descriptor.3507
- _block_descriptor.3517
- _block_descriptor.3527
- _block_descriptor.3545
- _block_descriptor.3571
- _block_descriptor.3574
- _block_descriptor.3584
- _block_descriptor.3587
- _block_descriptor.3600
- _block_descriptor.3629
- _block_descriptor.3632
- _block_descriptor.3651
- _block_descriptor.3726
- _block_descriptor.3756
- _block_descriptor.3759
- _block_descriptor.3778
- _block_descriptor.3886
- _block_descriptor.3889
- _block_descriptor.3898
- _block_descriptor.3938
- _block_descriptor.3999
- _block_descriptor.4002
- _block_descriptor.4012
- _block_descriptor.4032
- _block_descriptor.4035
- _block_descriptor.4047
- _block_descriptor.4080
- _block_descriptor.4083
- _block_descriptor.4086
- _block_descriptor.4103
- _block_descriptor.4136
- _block_descriptor.4141
- _block_descriptor.4146
- _block_descriptor.4156
- _block_descriptor.4182
- _block_descriptor.4194
- _block_descriptor.4202
- _block_descriptor.4357
- _block_descriptor.4410
- _block_descriptor.4413
- _block_descriptor.4526
- _block_descriptor.4529
- _block_descriptor.4591
- _block_descriptor.4649
- _block_descriptor.4652
- _block_descriptor.4655
- _block_descriptor.4658
- _block_descriptor.4679
- _block_descriptor.4682
- _block_descriptor.4715
- _block_descriptor.4718
- _block_descriptor.4738
- _block_descriptor.4748
- _block_descriptor.4760
- _block_descriptor.4772
- _block_descriptor.4779
- _block_descriptor.4789
- _block_descriptor.4800
- _block_descriptor.4857
- _block_descriptor.4864
- _block_descriptor.4871
- _block_descriptor.4881
- _block_descriptor.4891
- _block_descriptor.4901
- _block_descriptor.4911
- _block_descriptor.4917
- _block_descriptor.4924
- _block_descriptor.4934
- _block_descriptor.4944
- _block_descriptor.4951
- _block_descriptor.4961
- _block_descriptor.4968
- _block_descriptor.4975
- _block_descriptor.4982
- _block_descriptor.5033
- _block_descriptor.5140
- _block_descriptor.5191
- _block_descriptor.5231
- _block_descriptor.5260
- _block_descriptor.5273
- _block_descriptor.5283
- _block_descriptor.5352
- _block_descriptor.5364
- _block_descriptor.5376
- _block_descriptor.5382
- _block_descriptor.5394
- _block_descriptor.5406
- _block_descriptor.5418
- _block_descriptor.5424
- _block_descriptor.5436
- _block_descriptor.5463
- _block_descriptor.5572
- _block_descriptor.5575
- _block_descriptor.5586
- _block_descriptor.5598
- _block_descriptor.5607
- _block_descriptor.5615
- _block_descriptor.5624
- _block_descriptor.5635
- _block_descriptor.5641
- _block_descriptor.5653
- _block_descriptor.5664
- _block_descriptor.5677
- _block_descriptor.5688
- _block_descriptor.5699
- _block_descriptor.5705
- _block_descriptor.5717
- _block_descriptor.5812
- _block_descriptor.5954
- _block_descriptor.6012
- _block_descriptor.6044
- _block_descriptor.6070
- _block_descriptor.6100
- _block_descriptor.6136
- _block_descriptor.6184
- _block_descriptor.6194
- _block_descriptor.6223
- _block_descriptor.6236
- _block_descriptor.6247
- _block_descriptor.6258
- _block_descriptor.6310
- _block_descriptor.6319
- _block_descriptor.6339
- _block_descriptor.6357
- _block_descriptor.6369
- _block_descriptor.6387
- _block_descriptor.6399
- _block_descriptor.6417
- _block_descriptor.6427
- _block_descriptor.6459
- _block_descriptor.6471
- _block_descriptor.6505
- _block_descriptor.86
- _block_descriptor.96
- _block_destroy_helper.126
- _block_destroy_helper.136
- _block_destroy_helper.166
- _block_destroy_helper.176
- _block_destroy_helper.2084
- _block_destroy_helper.2096
- _block_destroy_helper.2106
- _block_destroy_helper.2118
- _block_destroy_helper.2173
- _block_destroy_helper.2176
- _block_destroy_helper.2182
- _block_destroy_helper.2185
- _block_destroy_helper.2211
- _block_destroy_helper.2223
- _block_destroy_helper.2269
- _block_destroy_helper.2272
- _block_destroy_helper.2344
- _block_destroy_helper.2356
- _block_destroy_helper.239
- _block_destroy_helper.2407
- _block_destroy_helper.2410
- _block_destroy_helper.2440
- _block_destroy_helper.2443
- _block_destroy_helper.2452
- _block_destroy_helper.252
- _block_destroy_helper.2522
- _block_destroy_helper.2525
- _block_destroy_helper.2549
- _block_destroy_helper.2552
- _block_destroy_helper.2582
- _block_destroy_helper.2585
- _block_destroy_helper.2615
- _block_destroy_helper.2618
- _block_destroy_helper.2641
- _block_destroy_helper.2644
- _block_destroy_helper.2674
- _block_destroy_helper.2677
- _block_destroy_helper.2693
- _block_destroy_helper.2705
- _block_destroy_helper.271
- _block_destroy_helper.2760
- _block_destroy_helper.2763
- _block_destroy_helper.280
- _block_destroy_helper.2827
- _block_destroy_helper.2830
- _block_destroy_helper.2833
- _block_destroy_helper.2892
- _block_destroy_helper.2895
- _block_destroy_helper.292
- _block_destroy_helper.2950
- _block_destroy_helper.2953
- _block_destroy_helper.2976
- _block_destroy_helper.2979
- _block_destroy_helper.2999
- _block_destroy_helper.305
- _block_destroy_helper.3129
- _block_destroy_helper.3132
- _block_destroy_helper.3154
- _block_destroy_helper.3176
- _block_destroy_helper.3215
- _block_destroy_helper.3241
- _block_destroy_helper.3244
- _block_destroy_helper.3284
- _block_destroy_helper.3298
- _block_destroy_helper.3348
- _block_destroy_helper.3351
- _block_destroy_helper.3365
- _block_destroy_helper.3402
- _block_destroy_helper.3412
- _block_destroy_helper.3422
- _block_destroy_helper.3432
- _block_destroy_helper.3442
- _block_destroy_helper.3452
- _block_destroy_helper.3468
- _block_destroy_helper.3485
- _block_destroy_helper.3496
- _block_destroy_helper.3506
- _block_destroy_helper.3516
- _block_destroy_helper.3526
- _block_destroy_helper.3544
- _block_destroy_helper.3570
- _block_destroy_helper.3573
- _block_destroy_helper.3583
- _block_destroy_helper.3586
- _block_destroy_helper.3599
- _block_destroy_helper.3628
- _block_destroy_helper.3631
- _block_destroy_helper.3650
- _block_destroy_helper.3725
- _block_destroy_helper.3755
- _block_destroy_helper.3758
- _block_destroy_helper.3777
- _block_destroy_helper.3885
- _block_destroy_helper.3888
- _block_destroy_helper.3897
- _block_destroy_helper.3937
- _block_destroy_helper.3998
- _block_destroy_helper.4001
- _block_destroy_helper.4011
- _block_destroy_helper.4031
- _block_destroy_helper.4034
- _block_destroy_helper.4046
- _block_destroy_helper.4079
- _block_destroy_helper.4082
- _block_destroy_helper.4085
- _block_destroy_helper.4102
- _block_destroy_helper.4135
- _block_destroy_helper.4140
- _block_destroy_helper.4145
- _block_destroy_helper.4155
- _block_destroy_helper.4181
- _block_destroy_helper.4193
- _block_destroy_helper.4201
- _block_destroy_helper.4356
- _block_destroy_helper.4409
- _block_destroy_helper.4412
- _block_destroy_helper.4525
- _block_destroy_helper.4528
- _block_destroy_helper.4590
- _block_destroy_helper.4648
- _block_destroy_helper.4651
- _block_destroy_helper.4654
- _block_destroy_helper.4657
- _block_destroy_helper.4678
- _block_destroy_helper.4681
- _block_destroy_helper.4714
- _block_destroy_helper.4717
- _block_destroy_helper.4737
- _block_destroy_helper.4747
- _block_destroy_helper.4759
- _block_destroy_helper.4771
- _block_destroy_helper.4778
- _block_destroy_helper.4788
- _block_destroy_helper.4799
- _block_destroy_helper.4856
- _block_destroy_helper.4863
- _block_destroy_helper.4870
- _block_destroy_helper.4880
- _block_destroy_helper.4890
- _block_destroy_helper.4900
- _block_destroy_helper.4910
- _block_destroy_helper.4916
- _block_destroy_helper.4923
- _block_destroy_helper.4933
- _block_destroy_helper.4943
- _block_destroy_helper.4950
- _block_destroy_helper.4960
- _block_destroy_helper.4967
- _block_destroy_helper.4974
- _block_destroy_helper.4981
- _block_destroy_helper.5032
- _block_destroy_helper.5139
- _block_destroy_helper.5190
- _block_destroy_helper.5230
- _block_destroy_helper.5259
- _block_destroy_helper.5272
- _block_destroy_helper.5282
- _block_destroy_helper.5351
- _block_destroy_helper.5363
- _block_destroy_helper.5375
- _block_destroy_helper.5381
- _block_destroy_helper.5393
- _block_destroy_helper.5405
- _block_destroy_helper.5417
- _block_destroy_helper.5423
- _block_destroy_helper.5435
- _block_destroy_helper.5462
- _block_destroy_helper.5571
- _block_destroy_helper.5574
- _block_destroy_helper.5585
- _block_destroy_helper.5597
- _block_destroy_helper.5606
- _block_destroy_helper.5614
- _block_destroy_helper.5623
- _block_destroy_helper.5634
- _block_destroy_helper.5640
- _block_destroy_helper.5652
- _block_destroy_helper.5663
- _block_destroy_helper.5676
- _block_destroy_helper.5687
- _block_destroy_helper.5698
- _block_destroy_helper.5704
- _block_destroy_helper.5716
- _block_destroy_helper.5811
- _block_destroy_helper.5953
- _block_destroy_helper.6011
- _block_destroy_helper.6043
- _block_destroy_helper.6069
- _block_destroy_helper.6099
- _block_destroy_helper.6135
- _block_destroy_helper.6183
- _block_destroy_helper.6193
- _block_destroy_helper.6222
- _block_destroy_helper.6235
- _block_destroy_helper.6246
- _block_destroy_helper.6257
- _block_destroy_helper.6309
- _block_destroy_helper.6318
- _block_destroy_helper.6338
- _block_destroy_helper.6356
- _block_destroy_helper.6368
- _block_destroy_helper.6386
- _block_destroy_helper.6398
- _block_destroy_helper.6416
- _block_destroy_helper.6426
- _block_destroy_helper.6458
- _block_destroy_helper.6470
- _block_destroy_helper.6504
- _block_destroy_helper.85
- _block_destroy_helper.95
- _get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization6AtomicVySo45FPDExclusiveSharedSystemSchedulerWatcherStateVG.2
- _get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization6AtomicVys5Int64VG.3
- _objectdestroy.2198Tm
- _objectdestroy.2201Tm
- _objectdestroy.2292Tm
- _objectdestroy.2301Tm
- _objectdestroy.2307Tm
- _objectdestroy.2310Tm
- _objectdestroy.2388Tm
- _objectdestroy.2397Tm
- _objectdestroy.2429Tm
- _objectdestroy.2538Tm
- _objectdestroy.2742Tm
- _objectdestroy.2769Tm
- _objectdestroy.2772Tm
- _objectdestroy.2873Tm
- _objectdestroy.2985Tm
- _objectdestroy.3022Tm
- _objectdestroy.3115Tm
- _objectdestroy.3139Tm
- _objectdestroy.3185Tm
- _objectdestroy.3195Tm
- _objectdestroy.3198Tm
- _objectdestroy.3201Tm
- _objectdestroy.3275Tm
- _objectdestroy.3281Tm
- _objectdestroy.3292Tm
- _objectdestroy.3326Tm
- _objectdestroy.3425Tm
- _objectdestroy.3666Tm
- _objectdestroy.3680Tm
- _objectdestroy.3802Tm
- _objectdestroy.3871Tm
- _objectdestroy.3875Tm
- _objectdestroy.4111Tm
- _objectdestroy.4241Tm
- _objectdestroy.4267Tm
- _objectdestroy.4287Tm
- _objectdestroy.4583Tm
- _objectdestroy.4808Tm
- _objectdestroy.5115Tm
- _objectdestroy.5120Tm
- _objectdestroy.5158Tm
- _objectdestroy.5817Tm
- _objectdestroy.5848Tm
- _objectdestroy.5903Tm
- _objectdestroy.5913Tm
- _objectdestroy.5972Tm
- _objectdestroy.5979Tm
- _objectdestroy.6017Tm
- _objectdestroy.6180Tm
- _objectdestroy.78Tm
- _symbolic _____y_____So6FPItemCGyt______pIeggrzo_ 18FileProviderDaemon20StuckDeletionMonitorC AA7VFSItemV s5ErrorP
- _symbolic _____y_____So6FPItemCGyt______pIggrzo_ 18FileProviderDaemon20StuckDeletionMonitorC AA7VFSItemV s5ErrorP
- _symbolic _____y_____So6FPItemC_____yAbDG_____yAbDG_____yAbDGGShy_____y__________GG______pIeggrzo_ 18FileProviderDaemon20FPDiagnosticsManagerC AA7VFSItemV AA0D13DBQueriesImplC AA010FPFeedbackE0C AA012FPTapToRadarE0C AA16ReconciliationIDO AA0fN0O So06NSFileB14ItemIdentifiera s5ErrorP
- _symbolic _____y_____So6FPItemC_____yAbDG_____yAbDG_____yAbDGGShy_____y__________GG______pIggrzo_ 18FileProviderDaemon20FPDiagnosticsManagerC AA7VFSItemV AA0D13DBQueriesImplC AA010FPFeedbackE0C AA012FPTapToRadarE0C AA16ReconciliationIDO AA0fN0O So06NSFileB14ItemIdentifiera s5ErrorP
- _symbolic _____y_____So6FPItemC_____yAbDG_____yAbDG_____yAbDGGyt______pIeggrzo_ 18FileProviderDaemon20FPDiagnosticsManagerC AA7VFSItemV AA0D13DBQueriesImplC AA010FPFeedbackE0C AA012FPTapToRadarE0C s5ErrorP
- _symbolic _____y_____So6FPItemC_____yAbDG_____yAbDG_____yAbDGGyt______pIggrzo_ 18FileProviderDaemon20FPDiagnosticsManagerC AA7VFSItemV AA0D13DBQueriesImplC AA010FPFeedbackE0C AA012FPTapToRadarE0C s5ErrorP
CStrings:
+ "?"
+ "@\"NSDictionary\"8@?0"
+ "@\"NSFileProviderItemVersion\""
+ "@\"OS_dispatch_semaphore\""
+ "@32@0:8i16@20B28"
+ "FPBoolean"
+ "FPCK: FPDRTCReporting backupManifestVsFSSnapshotDiff %{public}s"
+ "FPCK: FPDRTCReporting diskBrokenInvariants %{public}s"
+ "FPCK: FPDRTCReporting diskVersusFSSnapshotDiff %{public}s"
+ "FPCK: FPDRTCReporting fsSnapshotVersusFpSnapshotDiff %{public}s"
+ "FPCK: FPDRTCReporting reconciliationTableBrokenInvariants %{public}s"
+ "FPDCoreAnalyticsReport"
+ "Failed to set dataless bit: %{darwin.errno}d on %s"
+ "Repairing %{public}s"
+ "The item %s decmpfs attribute is not DATALESS_CMPFS_TYPE: %u"
+ "The item %s has a malformed decmpfs attribute. Size: %ld, magic: %u"
+ "The item %s is not a regular file, not attempting to fix the missing dataless flag"
+ "[ERROR] attempt to reactivate a domain that got removed %@"
+ "_canBundleIDTriggerTTRForFailure:"
+ "_eventName"
+ "_isEventEnabled"
+ "_isExternalQuery"
+ "_report"
+ "_updating"
+ "_value"
+ "addValue:forKey:"
+ "alreadyPausedBundleID"
+ "behavior"
+ "cachedGreedyState"
+ "com.apple.syncControls.fetchLatestVersion"
+ "com.apple.syncControls.pauseSync"
+ "com.apple.syncControls.resumeSync"
+ "com.apple.syncControls.uploadLocalVersion"
+ "com.microsoft.SharePoint-mac"
+ "connectionBundleID"
+ "debug"
+ "fix-parent-materialization-stuck-on-import"
+ "handleDatabaseError"
+ "initWithEventName:"
+ "initWithFD:trashURL:isExternalQuery:"
+ "mismatchedPausedBundleID"
+ "performWithDBDiagnosticAttributes(for:isExternalQuery:block:)"
+ "performWithDiskDiagnosticAttributes(by:isExternalQuery:block:)"
+ "performWithDiskDiagnosticAttributes(for:isExternalQuery:block:)"
+ "reimportEverything"
+ "reimportItems(below:markItemDataless:fpfs:completionHandler:)"
+ "sendReport"
+ "updating"
+ "value"
+ "{NSFileProviderTypeAndCreator=II}"
+ "\xc1"
+ "🧹 FPCK %{public}s pausing mid-run because pause checker indicated"
+ "🧹 FPCK %{public}s resuming mid-run"
+ "🧹 FPCK %{public}s skipping mid-run, shouldPause missing semaphore"
+ "🧹 FPCK %{public}s: FS vs FP snapshot check took %fs"
+ "🧹 FPCK %{public}s: FS vs snapshot check took %fs"
+ "🧹 FPCK %{public}s: all checks done."
+ "🧹 FPCK %{public}s: cannot send TTR, the sender is nil"
+ "🧹 FPCK %{public}s: cannot send reingestion, the sender is nil"
+ "🧹 FPCK %{public}s: error encoding IDs for TTR"
+ "🧹 FPCK %{public}s: error encoding IDs for reingestion"
+ "🧹 FPCK %{public}s: launched with options: [%s] - will abort because sync is paused."
+ "🧹 FPCK %{public}s: launching FSSnapshot and FPSnapshot checks."
+ "🧹 FPCK %{public}s: launching backup manifest checks."
+ "🧹 FPCK %{public}s: launching disk and FSSnapshot checks."
+ "🧹 FPCK %{public}s: launching purgePurgatory."
+ "🧹 FPCK %{public}s: launching reconciliation table checks."
+ "🧹 FPCK %{public}s: launching reingestion check"
+ "🧹 FPCK %{public}s: launching with options: [%s]."
+ "🧹 FPCK %{public}s: reconciliation table check took %fs"
+ "🧹 FPCK %{public}s: reingestion check took %fs"
+ "🧹 FPCK %{public}s: sending TTR, we have nil errors"
+ "🧹 FPCK %{public}s: sending reingestion, we have items"
+ "🧹 FPCK %{public}s: skipping TTR, no nil errors"
+ "🧹 FPCK %{public}s: skipping reingestion, no items"
+ "🧹 FPCK finished with duration: %{public}s"
+ "🧹 FPCK initialized with run id %{public}s"
- "\v"
- "@28@0:8i16@20"
- "FPCK: FPDRTCReporting backupManifestVsFSSnapshotDiff %s "
- "FPCK: FPDRTCReporting diskBrokenInvariants %s "
- "FPCK: FPDRTCReporting diskVersusFSSnapshotDiff %s "
- "FPCK: FPDRTCReporting fsSnapshotVersusFpSnapshotDiff %s "
- "FPCK: FPDRTCReporting reconciliationTableBrokenInvariants %s "
- "Failed to set dataless bit: %{darwin.errno}d"
- "The item doesn't have a decmpfs attribute with the DATALESS_CMPFS_TYPE"
- "The item is not a regular file, not attempting to fix the missing dataless flag"
- "initWithFD:trashURL:"
- "performWithDBDiagnosticAttributes(for:block:)"
- "performWithDiskDiagnosticAttributes(by:block:)"
- "performWithDiskDiagnosticAttributes(for:block:)"
- "\xb1"
- "🧹 FPCK %s pausing mid-run because pause checker indicated"
- "🧹 FPCK %s resuming mid-run"
- "🧹 FPCK %s skipping mid-run, shouldPause missing semaphore"
- "🧹 FPCK %s: FS vs FP snapshot check took %fs"
- "🧹 FPCK %s: FS vs snapshot check took %fs"
- "🧹 FPCK %s: all checks done."
- "🧹 FPCK %s: cannot send TTR, the sender is nil"
- "🧹 FPCK %s: cannot send reingestion, the sender is nil"
- "🧹 FPCK %s: error encoding IDs for TTR"
- "🧹 FPCK %s: error encoding IDs for reingestion"
- "🧹 FPCK %s: launched with options: [%s] - will abort because sync is paused."
- "🧹 FPCK %s: launching FSSnapshot and FPSnapshot checks."
- "🧹 FPCK %s: launching backup manifest checks."
- "🧹 FPCK %s: launching disk and FSSnapshot checks."
- "🧹 FPCK %s: launching purgePurgatory."
- "🧹 FPCK %s: launching reconciliation table checks."
- "🧹 FPCK %s: launching reingestion check"
- "🧹 FPCK %s: launching with options: [%s]."
- "🧹 FPCK %s: reconciliation table check took %fs"
- "🧹 FPCK %s: reingestion check took %fs"
- "🧹 FPCK %s: sending TTR, we have nil errors"
- "🧹 FPCK %s: sending reingestion, we have items"
- "🧹 FPCK %s: skipping TTR, no nil errors"
- "🧹 FPCK %s: skipping reingestion, no items"
- "🧹 FPCK finished with duration: %s"
- "🧹 FPCK initialized with run id %s"

```
