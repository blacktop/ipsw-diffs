## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`

```diff

-3762.0.0.0.0
-  __TEXT.__text: 0x9f0f04
-  __TEXT.__auth_stubs: 0x5b90
-  __TEXT.__objc_methlist: 0x994c
-  __TEXT.__const: 0x24280
-  __TEXT.__cstring: 0x4173d
-  __TEXT.__oslogstring: 0x1d542
-  __TEXT.__gcc_except_tab: 0xe314
+3833.0.0.502.1
+  __TEXT.__text: 0x9fd5f8
+  __TEXT.__auth_stubs: 0x5b80
+  __TEXT.__objc_methlist: 0x9964
+  __TEXT.__const: 0x242e0
+  __TEXT.__cstring: 0x4195d
+  __TEXT.__oslogstring: 0x1dab2
+  __TEXT.__gcc_except_tab: 0xe3f8
   __TEXT.__ustring: 0x176e
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__constg_swiftt: 0x11e68
-  __TEXT.__swift5_typeref: 0x11746
+  __TEXT.__constg_swiftt: 0x11f00
+  __TEXT.__swift5_typeref: 0x117c6
   __TEXT.__swift5_builtin: 0x834
   __TEXT.__swift5_mpenum: 0x118
-  __TEXT.__swift5_reflstr: 0xba9d
-  __TEXT.__swift5_fieldmd: 0xa7dc
+  __TEXT.__swift5_reflstr: 0xbb5d
+  __TEXT.__swift5_fieldmd: 0xa83c
   __TEXT.__swift5_assocty: 0x2240
-  __TEXT.__swift5_capture: 0x1b0dc
+  __TEXT.__swift5_capture: 0x1b310
   __TEXT.__swift5_proto: 0x1844
   __TEXT.__swift5_types: 0xa70
   __TEXT.__swift5_types2: 0x4
   __TEXT.__swift5_protos: 0x98
-  __TEXT.__swift_as_entry: 0x94
-  __TEXT.__swift_as_ret: 0x94
-  __TEXT.__unwind_info: 0x14400
-  __TEXT.__eh_frame: 0x25cd0
+  __TEXT.__swift_as_entry: 0xa8
+  __TEXT.__swift_as_ret: 0xa4
+  __TEXT.__unwind_info: 0x14548
+  __TEXT.__eh_frame: 0x26058
   __TEXT.__objc_classname: 0xef2
-  __TEXT.__objc_methname: 0x1d6dd
-  __TEXT.__objc_methtype: 0x6a37
-  __TEXT.__objc_stubs: 0xfd20
-  __DATA_CONST.__got: 0x17e0
-  __DATA_CONST.__const: 0x4d58
+  __TEXT.__objc_methname: 0x1d792
+  __TEXT.__objc_methtype: 0x6a4f
+  __TEXT.__objc_stubs: 0xfd80
+  __DATA_CONST.__got: 0x17f0
+  __DATA_CONST.__const: 0x4d38
   __DATA_CONST.__objc_classlist: 0x558
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x350
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x60c8
+  __DATA_CONST.__objc_selrefs: 0x60f0
   __DATA_CONST.__objc_protorefs: 0x188
   __DATA_CONST.__objc_superrefs: 0x280
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0x2dd8
-  __AUTH_CONST.__const: 0x50438
-  __AUTH_CONST.__cfstring: 0x6b80
-  __AUTH_CONST.__objc_const: 0x29480
+  __AUTH_CONST.__auth_got: 0x2dd0
+  __AUTH_CONST.__const: 0x508a0
+  __AUTH_CONST.__cfstring: 0x6c00
+  __AUTH_CONST.__objc_const: 0x29570
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x1808
   __AUTH.__data: 0x23e0
   __DATA.__objc_ivar: 0xb20
-  __DATA.__data: 0x89b0
+  __DATA.__data: 0x89d0
   __DATA.__bss: 0x24d40
-  __DATA.__common: 0x158
-  __DATA_DIRTY.__objc_data: 0x37b8
-  __DATA_DIRTY.__data: 0xd8c8
+  __DATA.__common: 0x168
+  __DATA_DIRTY.__objc_data: 0x3800
+  __DATA_DIRTY.__data: 0xd8f8
   __DATA_DIRTY.__bss: 0xa770
   __DATA_DIRTY.__common: 0x8e8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C66751BE-4ED7-3107-95ED-FB5A08D99516
-  Functions: 30559
-  Symbols:   28255
-  CStrings:  13385
+  UUID: B085B086-EDD2-3827-AAD5-BE6C98ECB789
+  Functions: 30651
+  Symbols:   28299
+  CStrings:  13433
 
Symbols:
+ +[FPCKTask runFPCKForDomain:domainUserInfo:domainRootURL:databaseBackupPath:urls:volumeRole:options:reason:fpfs:iCDPackageDetection:shouldPause:sendDiagnostics:saveCheckpoint:reingestItems:isInvalidated:contentBarrier:completionHandler:]
+ -[FPCKOnDemandUpdateReceiver reingestItemIDs:]
+ -[FPCKOnDemandUpdateReceiver reingestItemIDs:].cold.1
+ -[FPDDomainDeadEndBackend resolveConflictAtURL:request:completionHandler:]
+ -[FPDDomainExtensionBackend resolveConflictAtURL:request:completionHandler:]
+ -[FPDWrappedSearchEnumeratorObserverProxy initWithTarget:maximumNumberOfResultsPerPage:]
+ -[FPDWrappedSearchEnumeratorObserverProxy maximumNumberOfResultsPerPage]
+ -[FPDWrappedSearchEnumeratorObserverProxy setMaximumNumberOfResultsPerPage:]
+ -[FPDWrappedSearchEnumeratorProxy initWithTarget:maximumNumberOfResultsPerPage:]
+ GCC_except_table458
+ _OBJC_CLASS_$_NSRecursiveLock
+ _OBJC_IVAR_$_FPDDomain._nsDomainLock
+ _OBJC_IVAR_$_FPDWrappedSearchEnumeratorObserverProxy._maximumNumberOfResultsPerPage
+ _OBJC_IVAR_$_FPDWrappedSearchEnumeratorProxy._maximumNumberOfResultsPerPage
+ _SANDBOX_CHECK_NOFOLLOW
+ __IVARS__TtC18FileProviderDaemon8FSRepair
+ __PROTOCOLS__TtC18FileProviderDaemon12PeriodicFPCK.7
+ ___100-[FPDXPCServicer _test_importItemsPendingScanningProviderProgressForDomainWithID:completionHandler:]_block_invoke.458
+ ___100-[FPDXPCServicer uploadLocalVersionOfItemAtURL:bundleID:conflictResolutionPolicy:completionHandler:]_block_invoke.482
+ ___103-[FPDDomainExtensionBackend startProvidingItemAtURL:readerID:readingOptions:request:completionHandler:]_block_invoke.256
+ ___103-[FPDDomainExtensionBackend startProvidingItemAtURL:readerID:readingOptions:request:completionHandler:]_block_invoke.256.cold.1
+ ___103-[FPDDomainExtensionBackend startProvidingItemAtURL:readerID:readingOptions:request:completionHandler:]_block_invoke_2.258
+ ___103-[FPDDomainExtensionBackend startProvidingItemAtURL:readerID:readingOptions:request:completionHandler:]_block_invoke_2.258.cold.1
+ ___103-[FPDDomainExtensionBackend startProvidingItemAtURL:readerID:readingOptions:request:completionHandler:]_block_invoke_2.258.cold.2
+ ___103-[FPDDomainExtensionBackend startProvidingItemAtURL:readerID:readingOptions:request:completionHandler:]_block_invoke_2.258.cold.3
+ ___103-[FPDDomainExtensionBackend startProvidingItemAtURL:readerID:readingOptions:request:completionHandler:]_block_invoke_2.258.cold.4
+ ___103-[FPDDomainExtensionBackend startProvidingItemAtURL:readerID:readingOptions:request:completionHandler:]_block_invoke_2.258.cold.5
+ ___117-[FPDDomain _provideItemAtURL:withReaderID:withProcessID:withAuditToken:kernelInfo:readingOptions:completionHandler:]_block_invoke.178
+ ___125-[FPDDomainExtensionBackend createItemBasedOnTemplate:fields:urlWrapper:options:bounceOnCollision:request:completionHandler:]_block_invoke.263
+ ___125-[FPDDomainExtensionBackend createItemBasedOnTemplate:fields:urlWrapper:options:bounceOnCollision:request:completionHandler:]_block_invoke.263.cold.1
+ ___125-[FPDDomainExtensionBackend createItemBasedOnTemplate:fields:urlWrapper:options:bounceOnCollision:request:completionHandler:]_block_invoke.263.cold.2
+ ___125-[FPDDomainExtensionBackend itemForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:request:completionHandler:]_block_invoke.271
+ ___125-[FPDDomainExtensionBackend itemForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:request:completionHandler:]_block_invoke.271.cold.1
+ ___125-[FPDDomainExtensionBackend itemForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:request:completionHandler:]_block_invoke.271.cold.2
+ ___133-[FPDXPCServicer runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:]_block_invoke.304
+ ___133-[FPDXPCServicer runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:]_block_invoke.304.cold.1
+ ___133-[FPDXPCServicer runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:]_block_invoke.307
+ ___146-[FPDDomainExtensionBackend URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:forBookmarkResolution:request:completionHandler:]_block_invoke.269
+ ___146-[FPDDomainExtensionBackend URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:forBookmarkResolution:request:completionHandler:]_block_invoke.269.cold.1
+ ___146-[FPDDomainExtensionBackend URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:forBookmarkResolution:request:completionHandler:]_block_invoke.269.cold.2
+ ___209-[FPCKTask scheduleFPCKRun:domainUserInfo:domainRootURL:databaseBackupPath:urls:volumeRole:options:reason:fpfs:iCDPackageDetection:launchType:updateReceiver:shouldPause:contentBarrier:proxy:completionHandler:]_block_invoke_4
+ ___237+[FPCKTask runFPCKForDomain:domainUserInfo:domainRootURL:databaseBackupPath:urls:volumeRole:options:reason:fpfs:iCDPackageDetection:shouldPause:sendDiagnostics:saveCheckpoint:reingestItems:isInvalidated:contentBarrier:completionHandler:]_block_invoke
+ ___237+[FPCKTask runFPCKForDomain:domainUserInfo:domainRootURL:databaseBackupPath:urls:volumeRole:options:reason:fpfs:iCDPackageDetection:shouldPause:sendDiagnostics:saveCheckpoint:reingestItems:isInvalidated:contentBarrier:completionHandler:]_block_invoke_2
+ ___35-[FPDDomain cleanupDomainWithMode:]_block_invoke.158
+ ___35-[FPDDomain cleanupDomainWithMode:]_block_invoke.158.cold.1
+ ___50-[FPDDomain _writerWithID:didFinishWritingForURL:]_block_invoke.180
+ ___53-[FPDXPCServicer pauseIndexingFor:completionHandler:]_block_invoke.432
+ ___54-[FPDDomainExtensionBackend itemChangedAtURL:request:]_block_invoke.268
+ ___54-[FPDDomainExtensionBackend itemChangedAtURL:request:]_block_invoke.268.cold.1
+ ___54-[FPDXPCServicer resumeIndexingFor:completionHandler:]_block_invoke.433
+ ___55-[FPDDomain didChangeItemID:request:completionHandler:]_block_invoke.209
+ ___57-[FPDXPCServicer stateForDomainWithID:completionHandler:]_block_invoke.302
+ ___59-[FPDXPCServicer _test_purgerBarrierWithCompletionHandler:]_block_invoke.465
+ ___59-[FPDXPCServicer _test_purgerBarrierWithCompletionHandler:]_block_invoke.465.cold.1
+ ___59-[FPDXPCServicer appHasNonUploadedFiles:completionHandler:]_block_invoke.315
+ ___63-[FPDXPCServicer fetchDaemonOperationIDsWithCompletionHandler:]_block_invoke.390
+ ___64-[FPDDomain downloadVersionThumbnail:version:completionHandler:]_block_invoke.221
+ ___65-[FPDDomain _registerFileCoordinatorAndSpaceForceWithCompletion:]_block_invoke.195
+ ___65-[FPDXPCServicer _test_resetDBQueryStatistics:completionHandler:]_block_invoke.460
+ ___66-[FPDDomainExtensionBackend itemForURL:request:completionHandler:]_block_invoke.247
+ ___66-[FPDDomainExtensionBackend itemForURL:request:completionHandler:]_block_invoke.247.cold.1
+ ___66-[FPDXPCServicer importProgressForDomainWithID:completionHandler:]_block_invoke.300
+ ___67-[FPDXPCServicer _test_disableDBQueryStatistics:completionHandler:]_block_invoke.459
+ ___67-[FPDXPCServicer dumpTelemetryTo:providerFilter:completionHandler:]_block_invoke.367
+ ___68-[FPDXPCServicer dumpDatabaseAt:fullDump:writeTo:completionHandler:]_block_invoke.310
+ ___68-[FPDXPCServicer getDomainsForProviderIdentifier:completionHandler:]_block_invoke.cold.1
+ ___68-[FPDXPCServicer scheduleActionOperationWithInfo:completionHandler:]_block_invoke.388
+ ___70-[FPDXPCServicer _test_triggerDatabaseError:domain:completionHandler:]_block_invoke.464
+ ___70-[FPDXPCServicer copyDatabaseForFPCKStartingAtPath:completionHandler:]_block_invoke.381
+ ___71-[FPDXPCServicer dumpStateTo:providerFilter:options:completionHandler:]_block_invoke.347
+ ___73-[FPDXPCServicer _test_getDBQueryStatistics:queryPlan:completionHandler:]_block_invoke.461
+ ___73-[FPDXPCServicer waitForChangesOnItemsBelowItemWithID:completionHandler:]_block_invoke.384
+ ___74-[FPDXPCServicer startAccessingServiceWithName:itemURL:completionHandler:]_block_invoke.401
+ ___76-[FPDXPCServicer fetchLatestVersionForItemAtURL:bundleID:completionHandler:]_block_invoke.475
+ ___76-[FPDXPCServicer pauseSyncForItemAtURL:behavior:bundleID:completionHandler:]_block_invoke.469
+ ___76-[FPDXPCServicer waitForStabilizationOfDomainWithID:mode:completionHandler:]_block_invoke.385
+ ___77-[FPDXPCServicer _performWithCheckedEnumerationAttributes:completionHandler:]_block_invoke.411
+ ___77-[FPDXPCServicer forceUpdateBlockedProcessNamesFromDomain:completionHandler:]_block_invoke.297
+ ___77-[FPDXPCServicer resumeSyncForItemAtURL:behavior:bundleID:completionHandler:]_block_invoke.472
+ ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.441
+ ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.441.cold.1
+ ___81-[FPDDomain createRootAndObserveIfNeededWithReason:userAllowedDBDrop:completion:]_block_invoke.136
+ ___82-[FPDDomainExtensionBackend valuesForAttributes:forURL:request:completionHandler:]_block_invoke.303
+ ___82-[FPDXPCServicer fetchAndStartEnumeratingWithSettings:observer:completionHandler:]_block_invoke.417
+ ___82-[FPDXPCServicer reimportItemsBelowItemWithID:markItemDataless:completionHandler:]_block_invoke.296
+ ___85-[FPDDomainExtensionBackend evictItemAtURL:evictionReason:request:completionHandler:]_block_invoke.265
+ ___85-[FPDDomainExtensionBackend evictItemAtURL:evictionReason:request:completionHandler:]_block_invoke.265.cold.1
+ ___85-[FPDDomainExtensionBackend evictItemAtURL:evictionReason:request:completionHandler:]_block_invoke.265.cold.2
+ ___85-[FPDXPCServicer enumerateSearchResultForRequest:providerDomainID:completionHandler:]_block_invoke.406
+ ___86-[FPDDomainExtensionBackend evictItemWithID:evictionReason:request:completionHandler:]_block_invoke.266
+ ___86-[FPDXPCServicer setEnabled:forDomainIdentifier:providerIdentifier:completionHandler:]_block_invoke.293
+ ___88-[FPDDomain _startObservingRootAndResumeIndexerWithReason:userAllowedDBDrop:completion:]_block_invoke.132.cold.1
+ ___88-[FPDDomain _startObservingRootAndResumeIndexerWithReason:userAllowedDBDrop:completion:]_block_invoke.132.cold.2
+ ___88-[FPDDomain _startObservingRootAndResumeIndexerWithReason:userAllowedDBDrop:completion:]_block_invoke.133
+ ___88-[FPDXPCServicer spotlightReindexAllItemsForBundleID:protectionClass:completionHandler:]_block_invoke.386
+ ___90-[FPDDomainExtensionBackend itemIDForURL:requireProviderItemID:request:completionHandler:]_block_invoke.250
+ ___90-[FPDDomainExtensionBackend itemIDForURL:requireProviderItemID:request:completionHandler:]_block_invoke.250.cold.1
+ ___90-[FPDDomainExtensionBackend itemIDForURL:requireProviderItemID:request:completionHandler:]_block_invoke.250.cold.2
+ ___91-[FPDXPCServicer setHiddenByUser:forDomainIdentifier:providerIdentifier:completionHandler:]_block_invoke.294
+ ___93-[FPDXPCServicer signalReindexCSIdentifiersByProviderDomainID:indexReason:completionHandler:]_block_invoke.434
+ ___93-[FPDXPCServicer signalReindexCSIdentifiersByProviderDomainID:indexReason:completionHandler:]_block_invoke.434.cold.1
+ ___93-[FPDXPCServicer signalReindexCSIdentifiersByProviderDomainID:indexReason:completionHandler:]_block_invoke.434.cold.2
+ ___94-[FPDXPCServicer setIndexingEnabled:forDomainIdentifier:providerIdentifier:completionHandler:]_block_invoke.295
+ ___96-[FPDXPCServicer _test_importItemsPendingScanningDiskProgressForDomainWithID:completionHandler:]_block_invoke.455
+ ___98-[FPDXPCServicer _test_importItemsPendingReconciliationProgressForDomainWithID:completionHandler:]_block_invoke.452
+ ___98-[FPDXPCServicer spotlightReindexItemsWithIdentifiers:bundleID:protectionClass:completionHandler:]_block_invoke.387
+ ___block_literal_global.119
+ ___block_literal_global.157
+ ___block_literal_global.183
+ ___block_literal_global.198
+ ___block_literal_global.223
+ ___block_literal_global.393
+ ___block_literal_global.707
+ ___block_literal_global.710
+ _block_copy_helper.1006
+ _block_copy_helper.1008
+ _block_copy_helper.1017
+ _block_copy_helper.1019
+ _block_copy_helper.1029
+ _block_copy_helper.1041
+ _block_copy_helper.1074
+ _block_copy_helper.1108
+ _block_copy_helper.1110
+ _block_copy_helper.1122
+ _block_copy_helper.1131
+ _block_copy_helper.1145
+ _block_copy_helper.1148
+ _block_copy_helper.1152
+ _block_copy_helper.1164
+ _block_copy_helper.117
+ _block_copy_helper.1177
+ _block_copy_helper.1186
+ _block_copy_helper.1188
+ _block_copy_helper.1207
+ _block_copy_helper.1208
+ _block_copy_helper.1214
+ _block_copy_helper.1228
+ _block_copy_helper.1235
+ _block_copy_helper.1238
+ _block_copy_helper.1242
+ _block_copy_helper.1254
+ _block_copy_helper.1256
+ _block_copy_helper.1265
+ _block_copy_helper.1271
+ _block_copy_helper.1279
+ _block_copy_helper.1282
+ _block_copy_helper.1306
+ _block_copy_helper.1310
+ _block_copy_helper.1312
+ _block_copy_helper.1323
+ _block_copy_helper.1332
+ _block_copy_helper.1337
+ _block_copy_helper.1357
+ _block_copy_helper.1359
+ _block_copy_helper.1360
+ _block_copy_helper.1369
+ _block_copy_helper.1379
+ _block_copy_helper.1390
+ _block_copy_helper.1407
+ _block_copy_helper.1412
+ _block_copy_helper.1424
+ _block_copy_helper.1426
+ _block_copy_helper.1436
+ _block_copy_helper.1442
+ _block_copy_helper.1447
+ _block_copy_helper.1453
+ _block_copy_helper.1454
+ _block_copy_helper.1459
+ _block_copy_helper.1461
+ _block_copy_helper.1477
+ _block_copy_helper.1482
+ _block_copy_helper.1489
+ _block_copy_helper.1494
+ _block_copy_helper.1507
+ _block_copy_helper.1512
+ _block_copy_helper.1519
+ _block_copy_helper.1526
+ _block_copy_helper.164
+ _block_copy_helper.1718
+ _block_copy_helper.1759
+ _block_copy_helper.1763
+ _block_copy_helper.178
+ _block_copy_helper.1785
+ _block_copy_helper.1834
+ _block_copy_helper.1853
+ _block_copy_helper.1863
+ _block_copy_helper.1873
+ _block_copy_helper.1890
+ _block_copy_helper.1900
+ _block_copy_helper.1910
+ _block_copy_helper.1920
+ _block_copy_helper.1933
+ _block_copy_helper.1943
+ _block_copy_helper.1962
+ _block_copy_helper.1974
+ _block_copy_helper.1990
+ _block_copy_helper.1993
+ _block_copy_helper.2024
+ _block_copy_helper.2043
+ _block_copy_helper.2078
+ _block_copy_helper.2090
+ _block_copy_helper.2100
+ _block_copy_helper.2112
+ _block_copy_helper.2167
+ _block_copy_helper.2170
+ _block_copy_helper.2176
+ _block_copy_helper.2179
+ _block_copy_helper.2205
+ _block_copy_helper.2217
+ _block_copy_helper.2263
+ _block_copy_helper.2266
+ _block_copy_helper.227
+ _block_copy_helper.2338
+ _block_copy_helper.2350
+ _block_copy_helper.2401
+ _block_copy_helper.2404
+ _block_copy_helper.2434
+ _block_copy_helper.2437
+ _block_copy_helper.2446
+ _block_copy_helper.2516
+ _block_copy_helper.2519
+ _block_copy_helper.2543
+ _block_copy_helper.2546
+ _block_copy_helper.2576
+ _block_copy_helper.2579
+ _block_copy_helper.260
+ _block_copy_helper.2609
+ _block_copy_helper.2612
+ _block_copy_helper.2635
+ _block_copy_helper.2638
+ _block_copy_helper.2668
+ _block_copy_helper.2671
+ _block_copy_helper.2687
+ _block_copy_helper.2699
+ _block_copy_helper.275
+ _block_copy_helper.2754
+ _block_copy_helper.2757
+ _block_copy_helper.2821
+ _block_copy_helper.2824
+ _block_copy_helper.2827
+ _block_copy_helper.2886
+ _block_copy_helper.2889
+ _block_copy_helper.2944
+ _block_copy_helper.2947
+ _block_copy_helper.2970
+ _block_copy_helper.2973
+ _block_copy_helper.2993
+ _block_copy_helper.300
+ _block_copy_helper.303
+ _block_copy_helper.3123
+ _block_copy_helper.3126
+ _block_copy_helper.3148
+ _block_copy_helper.3170
+ _block_copy_helper.319
+ _block_copy_helper.3209
+ _block_copy_helper.3235
+ _block_copy_helper.3238
+ _block_copy_helper.3278
+ _block_copy_helper.3292
+ _block_copy_helper.3342
+ _block_copy_helper.3345
+ _block_copy_helper.3359
+ _block_copy_helper.3396
+ _block_copy_helper.3406
+ _block_copy_helper.3416
+ _block_copy_helper.3426
+ _block_copy_helper.3436
+ _block_copy_helper.344
+ _block_copy_helper.3446
+ _block_copy_helper.3462
+ _block_copy_helper.3469
+ _block_copy_helper.3479
+ _block_copy_helper.3490
+ _block_copy_helper.3500
+ _block_copy_helper.3510
+ _block_copy_helper.3520
+ _block_copy_helper.3538
+ _block_copy_helper.354
+ _block_copy_helper.3564
+ _block_copy_helper.3567
+ _block_copy_helper.3577
+ _block_copy_helper.3580
+ _block_copy_helper.359
+ _block_copy_helper.3593
+ _block_copy_helper.3622
+ _block_copy_helper.3625
+ _block_copy_helper.3632
+ _block_copy_helper.3644
+ _block_copy_helper.370
+ _block_copy_helper.3719
+ _block_copy_helper.3749
+ _block_copy_helper.3752
+ _block_copy_helper.3759
+ _block_copy_helper.3771
+ _block_copy_helper.380
+ _block_copy_helper.384
+ _block_copy_helper.3879
+ _block_copy_helper.3882
+ _block_copy_helper.3891
+ _block_copy_helper.3931
+ _block_copy_helper.396
+ _block_copy_helper.3992
+ _block_copy_helper.3995
+ _block_copy_helper.4005
+ _block_copy_helper.4025
+ _block_copy_helper.4028
+ _block_copy_helper.403
+ _block_copy_helper.4040
+ _block_copy_helper.4073
+ _block_copy_helper.4076
+ _block_copy_helper.4079
+ _block_copy_helper.4096
+ _block_copy_helper.410
+ _block_copy_helper.4129
+ _block_copy_helper.4134
+ _block_copy_helper.4139
+ _block_copy_helper.4149
+ _block_copy_helper.4175
+ _block_copy_helper.4187
+ _block_copy_helper.4195
+ _block_copy_helper.421
+ _block_copy_helper.425
+ _block_copy_helper.428
+ _block_copy_helper.4350
+ _block_copy_helper.437
+ _block_copy_helper.440
+ _block_copy_helper.4405
+ _block_copy_helper.4408
+ _block_copy_helper.4498
+ _block_copy_helper.4501
+ _block_copy_helper.4532
+ _block_copy_helper.4535
+ _block_copy_helper.454
+ _block_copy_helper.4597
+ _block_copy_helper.461
+ _block_copy_helper.464
+ _block_copy_helper.4655
+ _block_copy_helper.4658
+ _block_copy_helper.4661
+ _block_copy_helper.4664
+ _block_copy_helper.4685
+ _block_copy_helper.4688
+ _block_copy_helper.471
+ _block_copy_helper.4721
+ _block_copy_helper.4724
+ _block_copy_helper.4744
+ _block_copy_helper.4754
+ _block_copy_helper.4766
+ _block_copy_helper.4778
+ _block_copy_helper.4785
+ _block_copy_helper.4795
+ _block_copy_helper.4806
+ _block_copy_helper.485
+ _block_copy_helper.4863
+ _block_copy_helper.4870
+ _block_copy_helper.4877
+ _block_copy_helper.488
+ _block_copy_helper.4887
+ _block_copy_helper.4897
+ _block_copy_helper.4907
+ _block_copy_helper.4917
+ _block_copy_helper.492
+ _block_copy_helper.4923
+ _block_copy_helper.4930
+ _block_copy_helper.4940
+ _block_copy_helper.4950
+ _block_copy_helper.4957
+ _block_copy_helper.4967
+ _block_copy_helper.4974
+ _block_copy_helper.498
+ _block_copy_helper.4981
+ _block_copy_helper.4988
+ _block_copy_helper.5039
+ _block_copy_helper.508
+ _block_copy_helper.5146
+ _block_copy_helper.5149
+ _block_copy_helper.5197
+ _block_copy_helper.5237
+ _block_copy_helper.5266
+ _block_copy_helper.5269
+ _block_copy_helper.5279
+ _block_copy_helper.528
+ _block_copy_helper.5289
+ _block_copy_helper.5358
+ _block_copy_helper.5370
+ _block_copy_helper.538
+ _block_copy_helper.5382
+ _block_copy_helper.5388
+ _block_copy_helper.5400
+ _block_copy_helper.541
+ _block_copy_helper.5412
+ _block_copy_helper.5424
+ _block_copy_helper.5430
+ _block_copy_helper.5442
+ _block_copy_helper.5469
+ _block_copy_helper.5472
+ _block_copy_helper.5578
+ _block_copy_helper.558
+ _block_copy_helper.5581
+ _block_copy_helper.5592
+ _block_copy_helper.5607
+ _block_copy_helper.5613
+ _block_copy_helper.5630
+ _block_copy_helper.5641
+ _block_copy_helper.5647
+ _block_copy_helper.5659
+ _block_copy_helper.5670
+ _block_copy_helper.568
+ _block_copy_helper.5683
+ _block_copy_helper.5694
+ _block_copy_helper.5705
+ _block_copy_helper.5711
+ _block_copy_helper.5723
+ _block_copy_helper.5818
+ _block_copy_helper.582
+ _block_copy_helper.5821
+ _block_copy_helper.593
+ _block_copy_helper.594
+ _block_copy_helper.5960
+ _block_copy_helper.5963
+ _block_copy_helper.6018
+ _block_copy_helper.6021
+ _block_copy_helper.604
+ _block_copy_helper.6050
+ _block_copy_helper.6076
+ _block_copy_helper.6079
+ _block_copy_helper.610
+ _block_copy_helper.6106
+ _block_copy_helper.6109
+ _block_copy_helper.6142
+ _block_copy_helper.6145
+ _block_copy_helper.6190
+ _block_copy_helper.6200
+ _block_copy_helper.6229
+ _block_copy_helper.623
+ _block_copy_helper.6232
+ _block_copy_helper.624
+ _block_copy_helper.6242
+ _block_copy_helper.6253
+ _block_copy_helper.6264
+ _block_copy_helper.6325
+ _block_copy_helper.6328
+ _block_copy_helper.634
+ _block_copy_helper.6345
+ _block_copy_helper.6363
+ _block_copy_helper.6375
+ _block_copy_helper.6393
+ _block_copy_helper.6405
+ _block_copy_helper.6423
+ _block_copy_helper.6433
+ _block_copy_helper.644
+ _block_copy_helper.6465
+ _block_copy_helper.6477
+ _block_copy_helper.649
+ _block_copy_helper.6511
+ _block_copy_helper.6514
+ _block_copy_helper.654
+ _block_copy_helper.670
+ _block_copy_helper.678
+ _block_copy_helper.684
+ _block_copy_helper.687
+ _block_copy_helper.702
+ _block_copy_helper.708
+ _block_copy_helper.719
+ _block_copy_helper.726
+ _block_copy_helper.736
+ _block_copy_helper.744
+ _block_copy_helper.746
+ _block_copy_helper.756
+ _block_copy_helper.776
+ _block_copy_helper.785
+ _block_copy_helper.786
+ _block_copy_helper.788
+ _block_copy_helper.789
+ _block_copy_helper.796
+ _block_copy_helper.799
+ _block_copy_helper.806
+ _block_copy_helper.811
+ _block_copy_helper.814
+ _block_copy_helper.824
+ _block_copy_helper.829
+ _block_copy_helper.834
+ _block_copy_helper.837
+ _block_copy_helper.844
+ _block_copy_helper.847
+ _block_copy_helper.850
+ _block_copy_helper.856
+ _block_copy_helper.859
+ _block_copy_helper.860
+ _block_copy_helper.866
+ _block_copy_helper.869
+ _block_copy_helper.872
+ _block_copy_helper.877
+ _block_copy_helper.879
+ _block_copy_helper.880
+ _block_copy_helper.894
+ _block_copy_helper.899
+ _block_copy_helper.906
+ _block_copy_helper.919
+ _block_copy_helper.92
+ _block_copy_helper.922
+ _block_copy_helper.930
+ _block_copy_helper.934
+ _block_copy_helper.937
+ _block_copy_helper.945
+ _block_copy_helper.949
+ _block_copy_helper.952
+ _block_copy_helper.962
+ _block_copy_helper.964
+ _block_copy_helper.965
+ _block_copy_helper.978
+ _block_copy_helper.981
+ _block_copy_helper.995
+ _block_copy_helper.998
+ _block_descriptor.1000
+ _block_descriptor.1008
+ _block_descriptor.1010
+ _block_descriptor.1019
+ _block_descriptor.1021
+ _block_descriptor.1031
+ _block_descriptor.1043
+ _block_descriptor.1076
+ _block_descriptor.1110
+ _block_descriptor.1112
+ _block_descriptor.1124
+ _block_descriptor.1133
+ _block_descriptor.1147
+ _block_descriptor.1150
+ _block_descriptor.1154
+ _block_descriptor.1166
+ _block_descriptor.1179
+ _block_descriptor.1188
+ _block_descriptor.119
+ _block_descriptor.1190
+ _block_descriptor.1209
+ _block_descriptor.1210
+ _block_descriptor.1216
+ _block_descriptor.1230
+ _block_descriptor.1237
+ _block_descriptor.1240
+ _block_descriptor.1244
+ _block_descriptor.1256
+ _block_descriptor.1258
+ _block_descriptor.1267
+ _block_descriptor.1273
+ _block_descriptor.1281
+ _block_descriptor.1284
+ _block_descriptor.1308
+ _block_descriptor.1312
+ _block_descriptor.1314
+ _block_descriptor.1325
+ _block_descriptor.1334
+ _block_descriptor.1339
+ _block_descriptor.1359
+ _block_descriptor.1361
+ _block_descriptor.1362
+ _block_descriptor.1371
+ _block_descriptor.1381
+ _block_descriptor.1392
+ _block_descriptor.1409
+ _block_descriptor.1414
+ _block_descriptor.1426
+ _block_descriptor.1428
+ _block_descriptor.1438
+ _block_descriptor.1444
+ _block_descriptor.1449
+ _block_descriptor.1455
+ _block_descriptor.1456
+ _block_descriptor.1461
+ _block_descriptor.1463
+ _block_descriptor.1479
+ _block_descriptor.1484
+ _block_descriptor.1491
+ _block_descriptor.1496
+ _block_descriptor.1509
+ _block_descriptor.1514
+ _block_descriptor.1521
+ _block_descriptor.1528
+ _block_descriptor.166
+ _block_descriptor.1720
+ _block_descriptor.1761
+ _block_descriptor.1765
+ _block_descriptor.1787
+ _block_descriptor.180
+ _block_descriptor.1836
+ _block_descriptor.1855
+ _block_descriptor.1865
+ _block_descriptor.1875
+ _block_descriptor.1892
+ _block_descriptor.1902
+ _block_descriptor.1912
+ _block_descriptor.1922
+ _block_descriptor.1935
+ _block_descriptor.1945
+ _block_descriptor.1964
+ _block_descriptor.1976
+ _block_descriptor.1992
+ _block_descriptor.1995
+ _block_descriptor.2026
+ _block_descriptor.2045
+ _block_descriptor.2080
+ _block_descriptor.2092
+ _block_descriptor.2102
+ _block_descriptor.2114
+ _block_descriptor.2169
+ _block_descriptor.2172
+ _block_descriptor.2178
+ _block_descriptor.2181
+ _block_descriptor.2207
+ _block_descriptor.2219
+ _block_descriptor.2265
+ _block_descriptor.2268
+ _block_descriptor.229
+ _block_descriptor.2340
+ _block_descriptor.2352
+ _block_descriptor.2403
+ _block_descriptor.2406
+ _block_descriptor.2436
+ _block_descriptor.2439
+ _block_descriptor.2448
+ _block_descriptor.2518
+ _block_descriptor.2521
+ _block_descriptor.2545
+ _block_descriptor.2548
+ _block_descriptor.2578
+ _block_descriptor.2581
+ _block_descriptor.2611
+ _block_descriptor.2614
+ _block_descriptor.262
+ _block_descriptor.2637
+ _block_descriptor.2640
+ _block_descriptor.2670
+ _block_descriptor.2673
+ _block_descriptor.2689
+ _block_descriptor.2701
+ _block_descriptor.2756
+ _block_descriptor.2759
+ _block_descriptor.277
+ _block_descriptor.2823
+ _block_descriptor.2826
+ _block_descriptor.2829
+ _block_descriptor.2888
+ _block_descriptor.2891
+ _block_descriptor.2946
+ _block_descriptor.2949
+ _block_descriptor.2972
+ _block_descriptor.2975
+ _block_descriptor.2995
+ _block_descriptor.302
+ _block_descriptor.305
+ _block_descriptor.3125
+ _block_descriptor.3128
+ _block_descriptor.3150
+ _block_descriptor.3172
+ _block_descriptor.321
+ _block_descriptor.3211
+ _block_descriptor.3237
+ _block_descriptor.3240
+ _block_descriptor.3280
+ _block_descriptor.3294
+ _block_descriptor.3344
+ _block_descriptor.3347
+ _block_descriptor.3361
+ _block_descriptor.3398
+ _block_descriptor.3408
+ _block_descriptor.3418
+ _block_descriptor.3428
+ _block_descriptor.3438
+ _block_descriptor.3448
+ _block_descriptor.346
+ _block_descriptor.3464
+ _block_descriptor.3471
+ _block_descriptor.3481
+ _block_descriptor.3492
+ _block_descriptor.3502
+ _block_descriptor.3512
+ _block_descriptor.3522
+ _block_descriptor.3540
+ _block_descriptor.356
+ _block_descriptor.3566
+ _block_descriptor.3569
+ _block_descriptor.3579
+ _block_descriptor.3582
+ _block_descriptor.3595
+ _block_descriptor.361
+ _block_descriptor.3624
+ _block_descriptor.3627
+ _block_descriptor.3634
+ _block_descriptor.3646
+ _block_descriptor.372
+ _block_descriptor.3721
+ _block_descriptor.3751
+ _block_descriptor.3754
+ _block_descriptor.3761
+ _block_descriptor.3773
+ _block_descriptor.382
+ _block_descriptor.386
+ _block_descriptor.3881
+ _block_descriptor.3884
+ _block_descriptor.3893
+ _block_descriptor.3933
+ _block_descriptor.398
+ _block_descriptor.3994
+ _block_descriptor.3997
+ _block_descriptor.4007
+ _block_descriptor.4027
+ _block_descriptor.4030
+ _block_descriptor.4042
+ _block_descriptor.405
+ _block_descriptor.4075
+ _block_descriptor.4078
+ _block_descriptor.4081
+ _block_descriptor.4098
+ _block_descriptor.412
+ _block_descriptor.4131
+ _block_descriptor.4136
+ _block_descriptor.4141
+ _block_descriptor.4151
+ _block_descriptor.4177
+ _block_descriptor.4189
+ _block_descriptor.4197
+ _block_descriptor.423
+ _block_descriptor.427
+ _block_descriptor.430
+ _block_descriptor.4352
+ _block_descriptor.439
+ _block_descriptor.4407
+ _block_descriptor.4410
+ _block_descriptor.442
+ _block_descriptor.4500
+ _block_descriptor.4503
+ _block_descriptor.4534
+ _block_descriptor.4537
+ _block_descriptor.456
+ _block_descriptor.4599
+ _block_descriptor.463
+ _block_descriptor.4657
+ _block_descriptor.466
+ _block_descriptor.4660
+ _block_descriptor.4663
+ _block_descriptor.4666
+ _block_descriptor.4687
+ _block_descriptor.4690
+ _block_descriptor.4723
+ _block_descriptor.4726
+ _block_descriptor.473
+ _block_descriptor.4746
+ _block_descriptor.4756
+ _block_descriptor.4768
+ _block_descriptor.4780
+ _block_descriptor.4787
+ _block_descriptor.4797
+ _block_descriptor.4808
+ _block_descriptor.4865
+ _block_descriptor.487
+ _block_descriptor.4872
+ _block_descriptor.4879
+ _block_descriptor.4889
+ _block_descriptor.4899
+ _block_descriptor.490
+ _block_descriptor.4909
+ _block_descriptor.4919
+ _block_descriptor.4925
+ _block_descriptor.4932
+ _block_descriptor.494
+ _block_descriptor.4942
+ _block_descriptor.4952
+ _block_descriptor.4959
+ _block_descriptor.4969
+ _block_descriptor.4976
+ _block_descriptor.4983
+ _block_descriptor.4990
+ _block_descriptor.500
+ _block_descriptor.5041
+ _block_descriptor.510
+ _block_descriptor.5148
+ _block_descriptor.5151
+ _block_descriptor.5199
+ _block_descriptor.5239
+ _block_descriptor.5268
+ _block_descriptor.5271
+ _block_descriptor.5281
+ _block_descriptor.5291
+ _block_descriptor.530
+ _block_descriptor.5360
+ _block_descriptor.5372
+ _block_descriptor.5384
+ _block_descriptor.5390
+ _block_descriptor.540
+ _block_descriptor.5402
+ _block_descriptor.5414
+ _block_descriptor.5426
+ _block_descriptor.543
+ _block_descriptor.5432
+ _block_descriptor.5444
+ _block_descriptor.5471
+ _block_descriptor.5474
+ _block_descriptor.5580
+ _block_descriptor.5583
+ _block_descriptor.5594
+ _block_descriptor.560
+ _block_descriptor.5609
+ _block_descriptor.5615
+ _block_descriptor.5632
+ _block_descriptor.5643
+ _block_descriptor.5649
+ _block_descriptor.5661
+ _block_descriptor.5672
+ _block_descriptor.5685
+ _block_descriptor.5696
+ _block_descriptor.570
+ _block_descriptor.5707
+ _block_descriptor.5713
+ _block_descriptor.5725
+ _block_descriptor.5820
+ _block_descriptor.5823
+ _block_descriptor.584
+ _block_descriptor.595
+ _block_descriptor.596
+ _block_descriptor.5962
+ _block_descriptor.5965
+ _block_descriptor.6020
+ _block_descriptor.6023
+ _block_descriptor.6052
+ _block_descriptor.606
+ _block_descriptor.6078
+ _block_descriptor.6081
+ _block_descriptor.6108
+ _block_descriptor.6111
+ _block_descriptor.612
+ _block_descriptor.6144
+ _block_descriptor.6147
+ _block_descriptor.6192
+ _block_descriptor.6202
+ _block_descriptor.6231
+ _block_descriptor.6234
+ _block_descriptor.6244
+ _block_descriptor.625
+ _block_descriptor.6255
+ _block_descriptor.626
+ _block_descriptor.6266
+ _block_descriptor.6327
+ _block_descriptor.6330
+ _block_descriptor.6347
+ _block_descriptor.636
+ _block_descriptor.6365
+ _block_descriptor.6377
+ _block_descriptor.6395
+ _block_descriptor.6407
+ _block_descriptor.6425
+ _block_descriptor.6435
+ _block_descriptor.646
+ _block_descriptor.6467
+ _block_descriptor.6479
+ _block_descriptor.651
+ _block_descriptor.6513
+ _block_descriptor.6516
+ _block_descriptor.656
+ _block_descriptor.672
+ _block_descriptor.680
+ _block_descriptor.686
+ _block_descriptor.689
+ _block_descriptor.704
+ _block_descriptor.710
+ _block_descriptor.721
+ _block_descriptor.728
+ _block_descriptor.738
+ _block_descriptor.746
+ _block_descriptor.748
+ _block_descriptor.758
+ _block_descriptor.778
+ _block_descriptor.787
+ _block_descriptor.788
+ _block_descriptor.790
+ _block_descriptor.791
+ _block_descriptor.798
+ _block_descriptor.801
+ _block_descriptor.808
+ _block_descriptor.813
+ _block_descriptor.816
+ _block_descriptor.826
+ _block_descriptor.831
+ _block_descriptor.836
+ _block_descriptor.839
+ _block_descriptor.846
+ _block_descriptor.849
+ _block_descriptor.852
+ _block_descriptor.858
+ _block_descriptor.861
+ _block_descriptor.862
+ _block_descriptor.868
+ _block_descriptor.871
+ _block_descriptor.874
+ _block_descriptor.879
+ _block_descriptor.881
+ _block_descriptor.882
+ _block_descriptor.896
+ _block_descriptor.901
+ _block_descriptor.908
+ _block_descriptor.921
+ _block_descriptor.924
+ _block_descriptor.932
+ _block_descriptor.936
+ _block_descriptor.939
+ _block_descriptor.94
+ _block_descriptor.947
+ _block_descriptor.951
+ _block_descriptor.954
+ _block_descriptor.964
+ _block_descriptor.966
+ _block_descriptor.967
+ _block_descriptor.980
+ _block_descriptor.983
+ _block_descriptor.997
+ _block_destroy_helper.1007
+ _block_destroy_helper.1009
+ _block_destroy_helper.1018
+ _block_destroy_helper.1020
+ _block_destroy_helper.1030
+ _block_destroy_helper.1042
+ _block_destroy_helper.1075
+ _block_destroy_helper.1109
+ _block_destroy_helper.1111
+ _block_destroy_helper.1123
+ _block_destroy_helper.1132
+ _block_destroy_helper.1146
+ _block_destroy_helper.1149
+ _block_destroy_helper.1153
+ _block_destroy_helper.1165
+ _block_destroy_helper.1178
+ _block_destroy_helper.118
+ _block_destroy_helper.1187
+ _block_destroy_helper.1189
+ _block_destroy_helper.1208
+ _block_destroy_helper.1209
+ _block_destroy_helper.1215
+ _block_destroy_helper.1229
+ _block_destroy_helper.1236
+ _block_destroy_helper.1239
+ _block_destroy_helper.1243
+ _block_destroy_helper.1255
+ _block_destroy_helper.1257
+ _block_destroy_helper.1266
+ _block_destroy_helper.1272
+ _block_destroy_helper.1280
+ _block_destroy_helper.1283
+ _block_destroy_helper.1307
+ _block_destroy_helper.1311
+ _block_destroy_helper.1313
+ _block_destroy_helper.1324
+ _block_destroy_helper.1333
+ _block_destroy_helper.1338
+ _block_destroy_helper.1358
+ _block_destroy_helper.1360
+ _block_destroy_helper.1361
+ _block_destroy_helper.1370
+ _block_destroy_helper.1380
+ _block_destroy_helper.1391
+ _block_destroy_helper.1408
+ _block_destroy_helper.1413
+ _block_destroy_helper.1425
+ _block_destroy_helper.1427
+ _block_destroy_helper.1437
+ _block_destroy_helper.1443
+ _block_destroy_helper.1448
+ _block_destroy_helper.1454
+ _block_destroy_helper.1455
+ _block_destroy_helper.1460
+ _block_destroy_helper.1462
+ _block_destroy_helper.1478
+ _block_destroy_helper.1483
+ _block_destroy_helper.1490
+ _block_destroy_helper.1495
+ _block_destroy_helper.1508
+ _block_destroy_helper.1513
+ _block_destroy_helper.1520
+ _block_destroy_helper.1527
+ _block_destroy_helper.165
+ _block_destroy_helper.1719
+ _block_destroy_helper.1760
+ _block_destroy_helper.1764
+ _block_destroy_helper.1786
+ _block_destroy_helper.179
+ _block_destroy_helper.1835
+ _block_destroy_helper.1854
+ _block_destroy_helper.1864
+ _block_destroy_helper.1874
+ _block_destroy_helper.1891
+ _block_destroy_helper.1901
+ _block_destroy_helper.1911
+ _block_destroy_helper.1921
+ _block_destroy_helper.1934
+ _block_destroy_helper.1944
+ _block_destroy_helper.1963
+ _block_destroy_helper.1975
+ _block_destroy_helper.1991
+ _block_destroy_helper.1994
+ _block_destroy_helper.2025
+ _block_destroy_helper.2044
+ _block_destroy_helper.2079
+ _block_destroy_helper.2091
+ _block_destroy_helper.2101
+ _block_destroy_helper.2113
+ _block_destroy_helper.2168
+ _block_destroy_helper.2171
+ _block_destroy_helper.2177
+ _block_destroy_helper.2180
+ _block_destroy_helper.2206
+ _block_destroy_helper.2218
+ _block_destroy_helper.2264
+ _block_destroy_helper.2267
+ _block_destroy_helper.228
+ _block_destroy_helper.2339
+ _block_destroy_helper.2351
+ _block_destroy_helper.2402
+ _block_destroy_helper.2405
+ _block_destroy_helper.2435
+ _block_destroy_helper.2438
+ _block_destroy_helper.2447
+ _block_destroy_helper.2517
+ _block_destroy_helper.2520
+ _block_destroy_helper.2544
+ _block_destroy_helper.2547
+ _block_destroy_helper.2577
+ _block_destroy_helper.2580
+ _block_destroy_helper.261
+ _block_destroy_helper.2610
+ _block_destroy_helper.2613
+ _block_destroy_helper.2636
+ _block_destroy_helper.2639
+ _block_destroy_helper.2669
+ _block_destroy_helper.2672
+ _block_destroy_helper.2688
+ _block_destroy_helper.2700
+ _block_destroy_helper.2755
+ _block_destroy_helper.2758
+ _block_destroy_helper.276
+ _block_destroy_helper.2822
+ _block_destroy_helper.2825
+ _block_destroy_helper.2828
+ _block_destroy_helper.2887
+ _block_destroy_helper.2890
+ _block_destroy_helper.2945
+ _block_destroy_helper.2948
+ _block_destroy_helper.2971
+ _block_destroy_helper.2974
+ _block_destroy_helper.2994
+ _block_destroy_helper.301
+ _block_destroy_helper.304
+ _block_destroy_helper.3124
+ _block_destroy_helper.3127
+ _block_destroy_helper.3149
+ _block_destroy_helper.3171
+ _block_destroy_helper.320
+ _block_destroy_helper.3210
+ _block_destroy_helper.3236
+ _block_destroy_helper.3239
+ _block_destroy_helper.3279
+ _block_destroy_helper.3293
+ _block_destroy_helper.3343
+ _block_destroy_helper.3346
+ _block_destroy_helper.3360
+ _block_destroy_helper.3397
+ _block_destroy_helper.3407
+ _block_destroy_helper.3417
+ _block_destroy_helper.3427
+ _block_destroy_helper.3437
+ _block_destroy_helper.3447
+ _block_destroy_helper.345
+ _block_destroy_helper.3463
+ _block_destroy_helper.3470
+ _block_destroy_helper.3480
+ _block_destroy_helper.3491
+ _block_destroy_helper.3501
+ _block_destroy_helper.3511
+ _block_destroy_helper.3521
+ _block_destroy_helper.3539
+ _block_destroy_helper.355
+ _block_destroy_helper.3565
+ _block_destroy_helper.3568
+ _block_destroy_helper.3578
+ _block_destroy_helper.3581
+ _block_destroy_helper.3594
+ _block_destroy_helper.360
+ _block_destroy_helper.3623
+ _block_destroy_helper.3626
+ _block_destroy_helper.3633
+ _block_destroy_helper.3645
+ _block_destroy_helper.371
+ _block_destroy_helper.3720
+ _block_destroy_helper.3750
+ _block_destroy_helper.3753
+ _block_destroy_helper.3760
+ _block_destroy_helper.3772
+ _block_destroy_helper.381
+ _block_destroy_helper.385
+ _block_destroy_helper.3880
+ _block_destroy_helper.3883
+ _block_destroy_helper.3892
+ _block_destroy_helper.3932
+ _block_destroy_helper.397
+ _block_destroy_helper.3993
+ _block_destroy_helper.3996
+ _block_destroy_helper.4006
+ _block_destroy_helper.4026
+ _block_destroy_helper.4029
+ _block_destroy_helper.404
+ _block_destroy_helper.4041
+ _block_destroy_helper.4074
+ _block_destroy_helper.4077
+ _block_destroy_helper.4080
+ _block_destroy_helper.4097
+ _block_destroy_helper.411
+ _block_destroy_helper.4130
+ _block_destroy_helper.4135
+ _block_destroy_helper.4140
+ _block_destroy_helper.4150
+ _block_destroy_helper.4176
+ _block_destroy_helper.4188
+ _block_destroy_helper.4196
+ _block_destroy_helper.422
+ _block_destroy_helper.426
+ _block_destroy_helper.429
+ _block_destroy_helper.4351
+ _block_destroy_helper.438
+ _block_destroy_helper.4406
+ _block_destroy_helper.4409
+ _block_destroy_helper.441
+ _block_destroy_helper.4499
+ _block_destroy_helper.4502
+ _block_destroy_helper.4533
+ _block_destroy_helper.4536
+ _block_destroy_helper.455
+ _block_destroy_helper.4598
+ _block_destroy_helper.462
+ _block_destroy_helper.465
+ _block_destroy_helper.4656
+ _block_destroy_helper.4659
+ _block_destroy_helper.4662
+ _block_destroy_helper.4665
+ _block_destroy_helper.4686
+ _block_destroy_helper.4689
+ _block_destroy_helper.472
+ _block_destroy_helper.4722
+ _block_destroy_helper.4725
+ _block_destroy_helper.4745
+ _block_destroy_helper.4755
+ _block_destroy_helper.4767
+ _block_destroy_helper.4779
+ _block_destroy_helper.4786
+ _block_destroy_helper.4796
+ _block_destroy_helper.4807
+ _block_destroy_helper.486
+ _block_destroy_helper.4864
+ _block_destroy_helper.4871
+ _block_destroy_helper.4878
+ _block_destroy_helper.4888
+ _block_destroy_helper.489
+ _block_destroy_helper.4898
+ _block_destroy_helper.4908
+ _block_destroy_helper.4918
+ _block_destroy_helper.4924
+ _block_destroy_helper.493
+ _block_destroy_helper.4931
+ _block_destroy_helper.4941
+ _block_destroy_helper.4951
+ _block_destroy_helper.4958
+ _block_destroy_helper.4968
+ _block_destroy_helper.4975
+ _block_destroy_helper.4982
+ _block_destroy_helper.4989
+ _block_destroy_helper.499
+ _block_destroy_helper.5040
+ _block_destroy_helper.509
+ _block_destroy_helper.5147
+ _block_destroy_helper.5150
+ _block_destroy_helper.5198
+ _block_destroy_helper.5238
+ _block_destroy_helper.5267
+ _block_destroy_helper.5270
+ _block_destroy_helper.5280
+ _block_destroy_helper.529
+ _block_destroy_helper.5290
+ _block_destroy_helper.5359
+ _block_destroy_helper.5371
+ _block_destroy_helper.5383
+ _block_destroy_helper.5389
+ _block_destroy_helper.539
+ _block_destroy_helper.5401
+ _block_destroy_helper.5413
+ _block_destroy_helper.542
+ _block_destroy_helper.5425
+ _block_destroy_helper.5431
+ _block_destroy_helper.5443
+ _block_destroy_helper.5470
+ _block_destroy_helper.5473
+ _block_destroy_helper.5579
+ _block_destroy_helper.5582
+ _block_destroy_helper.559
+ _block_destroy_helper.5593
+ _block_destroy_helper.5608
+ _block_destroy_helper.5614
+ _block_destroy_helper.5631
+ _block_destroy_helper.5642
+ _block_destroy_helper.5648
+ _block_destroy_helper.5660
+ _block_destroy_helper.5671
+ _block_destroy_helper.5684
+ _block_destroy_helper.569
+ _block_destroy_helper.5695
+ _block_destroy_helper.5706
+ _block_destroy_helper.5712
+ _block_destroy_helper.5724
+ _block_destroy_helper.5819
+ _block_destroy_helper.5822
+ _block_destroy_helper.583
+ _block_destroy_helper.594
+ _block_destroy_helper.595
+ _block_destroy_helper.5961
+ _block_destroy_helper.5964
+ _block_destroy_helper.6019
+ _block_destroy_helper.6022
+ _block_destroy_helper.605
+ _block_destroy_helper.6051
+ _block_destroy_helper.6077
+ _block_destroy_helper.6080
+ _block_destroy_helper.6107
+ _block_destroy_helper.611
+ _block_destroy_helper.6110
+ _block_destroy_helper.6143
+ _block_destroy_helper.6146
+ _block_destroy_helper.6191
+ _block_destroy_helper.6201
+ _block_destroy_helper.6230
+ _block_destroy_helper.6233
+ _block_destroy_helper.624
+ _block_destroy_helper.6243
+ _block_destroy_helper.625
+ _block_destroy_helper.6254
+ _block_destroy_helper.6265
+ _block_destroy_helper.6326
+ _block_destroy_helper.6329
+ _block_destroy_helper.6346
+ _block_destroy_helper.635
+ _block_destroy_helper.6364
+ _block_destroy_helper.6376
+ _block_destroy_helper.6394
+ _block_destroy_helper.6406
+ _block_destroy_helper.6424
+ _block_destroy_helper.6434
+ _block_destroy_helper.645
+ _block_destroy_helper.6466
+ _block_destroy_helper.6478
+ _block_destroy_helper.650
+ _block_destroy_helper.6512
+ _block_destroy_helper.6515
+ _block_destroy_helper.655
+ _block_destroy_helper.671
+ _block_destroy_helper.679
+ _block_destroy_helper.685
+ _block_destroy_helper.688
+ _block_destroy_helper.703
+ _block_destroy_helper.709
+ _block_destroy_helper.720
+ _block_destroy_helper.727
+ _block_destroy_helper.737
+ _block_destroy_helper.745
+ _block_destroy_helper.747
+ _block_destroy_helper.757
+ _block_destroy_helper.777
+ _block_destroy_helper.786
+ _block_destroy_helper.787
+ _block_destroy_helper.789
+ _block_destroy_helper.790
+ _block_destroy_helper.797
+ _block_destroy_helper.800
+ _block_destroy_helper.807
+ _block_destroy_helper.812
+ _block_destroy_helper.815
+ _block_destroy_helper.825
+ _block_destroy_helper.830
+ _block_destroy_helper.835
+ _block_destroy_helper.838
+ _block_destroy_helper.845
+ _block_destroy_helper.848
+ _block_destroy_helper.851
+ _block_destroy_helper.857
+ _block_destroy_helper.860
+ _block_destroy_helper.861
+ _block_destroy_helper.867
+ _block_destroy_helper.870
+ _block_destroy_helper.873
+ _block_destroy_helper.878
+ _block_destroy_helper.880
+ _block_destroy_helper.881
+ _block_destroy_helper.895
+ _block_destroy_helper.900
+ _block_destroy_helper.907
+ _block_destroy_helper.920
+ _block_destroy_helper.923
+ _block_destroy_helper.93
+ _block_destroy_helper.931
+ _block_destroy_helper.935
+ _block_destroy_helper.938
+ _block_destroy_helper.946
+ _block_destroy_helper.950
+ _block_destroy_helper.953
+ _block_destroy_helper.963
+ _block_destroy_helper.965
+ _block_destroy_helper.966
+ _block_destroy_helper.979
+ _block_destroy_helper.982
+ _block_destroy_helper.996
+ _block_destroy_helper.999
+ _fpfs_unlinkat
+ _get_type_metadata 15Synchronization5MutexVySDySSSiGG.126
+ _objc_msgSend$initWithDatabasesBackupsPaths:volumeRole:providerDomainID:domainUserInfo:reason:usingFPFS:iCDPackageDetection:useShouldPause:shouldPause:sendDiagnostics:saveCheckpoint:reingestItems:isInvalidated:
+ _objc_msgSend$initWithTarget:maximumNumberOfResultsPerPage:
+ _objc_msgSend$lock
+ _objc_msgSend$maximumNumberOfResultsPerPage
+ _objc_msgSend$reingestItemIDs:
+ _objc_msgSend$resolveConflictAtURL:request:completionHandler:
+ _objc_msgSend$runFPCKForDomain:domainUserInfo:domainRootURL:databaseBackupPath:urls:volumeRole:options:reason:fpfs:iCDPackageDetection:shouldPause:sendDiagnostics:saveCheckpoint:reingestItems:isInvalidated:contentBarrier:completionHandler:
+ _objc_msgSend$unlock
+ _objectdestroy.1053Tm
+ _objectdestroy.1074Tm
+ _objectdestroy.1087Tm
+ _objectdestroy.1090Tm
+ _objectdestroy.1246Tm
+ _objectdestroy.124Tm
+ _objectdestroy.1252Tm
+ _objectdestroy.137Tm
+ _objectdestroy.144Tm
+ _objectdestroy.151Tm
+ _objectdestroy.154Tm
+ _objectdestroy.157Tm
+ _objectdestroy.1593Tm
+ _objectdestroy.166Tm
+ _objectdestroy.1769Tm
+ _objectdestroy.1776Tm
+ _objectdestroy.177Tm
+ _objectdestroy.1780Tm
+ _objectdestroy.182Tm
+ _objectdestroy.188Tm
+ _objectdestroy.196Tm
+ _objectdestroy.208Tm
+ _objectdestroy.212Tm
+ _objectdestroy.2193Tm
+ _objectdestroy.2196Tm
+ _objectdestroy.221Tm
+ _objectdestroy.224Tm
+ _objectdestroy.2287Tm
+ _objectdestroy.2296Tm
+ _objectdestroy.2302Tm
+ _objectdestroy.2305Tm
+ _objectdestroy.2383Tm
+ _objectdestroy.2392Tm
+ _objectdestroy.2424Tm
+ _objectdestroy.2533Tm
+ _objectdestroy.25Tm
+ _objectdestroy.2737Tm
+ _objectdestroy.2744Tm
+ _objectdestroy.2764Tm
+ _objectdestroy.2767Tm
+ _objectdestroy.2868Tm
+ _objectdestroy.2980Tm
+ _objectdestroy.300Tm
+ _objectdestroy.3017Tm
+ _objectdestroy.307Tm
+ _objectdestroy.3110Tm
+ _objectdestroy.3134Tm
+ _objectdestroy.3180Tm
+ _objectdestroy.3190Tm
+ _objectdestroy.3193Tm
+ _objectdestroy.3196Tm
+ _objectdestroy.31Tm
+ _objectdestroy.326Tm
+ _objectdestroy.3270Tm
+ _objectdestroy.3276Tm
+ _objectdestroy.3287Tm
+ _objectdestroy.329Tm
+ _objectdestroy.331Tm
+ _objectdestroy.3321Tm
+ _objectdestroy.336Tm
+ _objectdestroy.338Tm
+ _objectdestroy.3420Tm
+ _objectdestroy.351Tm
+ _objectdestroy.358Tm
+ _objectdestroy.3661Tm
+ _objectdestroy.3675Tm
+ _objectdestroy.377Tm
+ _objectdestroy.3797Tm
+ _objectdestroy.3866Tm
+ _objectdestroy.3870Tm
+ _objectdestroy.38Tm
+ _objectdestroy.399Tm
+ _objectdestroy.4106Tm
+ _objectdestroy.414Tm
+ _objectdestroy.417Tm
+ _objectdestroy.41Tm
+ _objectdestroy.420Tm
+ _objectdestroy.4236Tm
+ _objectdestroy.423Tm
+ _objectdestroy.4262Tm
+ _objectdestroy.4282Tm
+ _objectdestroy.431Tm
+ _objectdestroy.435Tm
+ _objectdestroy.444Tm
+ _objectdestroy.447Tm
+ _objectdestroy.4480Tm
+ _objectdestroy.453Tm
+ _objectdestroy.456Tm
+ _objectdestroy.4591Tm
+ _objectdestroy.474Tm
+ _objectdestroy.4816Tm
+ _objectdestroy.495Tm
+ _objectdestroy.5123Tm
+ _objectdestroy.5128Tm
+ _objectdestroy.5166Tm
+ _objectdestroy.517Tm
+ _objectdestroy.5825Tm
+ _objectdestroy.5856Tm
+ _objectdestroy.5911Tm
+ _objectdestroy.5921Tm
+ _objectdestroy.593Tm
+ _objectdestroy.5980Tm
+ _objectdestroy.5987Tm
+ _objectdestroy.6025Tm
+ _objectdestroy.6188Tm
+ _objectdestroy.623Tm
+ _objectdestroy.626Tm
+ _objectdestroy.629Tm
+ _objectdestroy.655Tm
+ _objectdestroy.665Tm
+ _objectdestroy.676Tm
+ _objectdestroy.67Tm
+ _objectdestroy.691Tm
+ _objectdestroy.745Tm
+ _objectdestroy.74Tm
+ _objectdestroy.791Tm
+ _objectdestroy.800Tm
+ _objectdestroy.818Tm
+ _objectdestroy.851Tm
+ _objectdestroy.864Tm
+ _objectdestroy.975Tm
+ _symbolic Say_____G 18FileProviderDaemon9VFSItemIDO
+ _symbolic Shy_____y__________GG 18FileProviderDaemon16ReconciliationIDO AA07VFSItemE0O So06NSFileB14ItemIdentifiera
+ _symbolic _____Sg 18FileProviderDaemon8FSRepairC
+ _symbolic _____ySi______pGIegg_ s6ResultOsRi_zRi0_zrlE s5ErrorP
+ _symbolic _____ySi______pGIegn_ s6ResultOsRi_zRi0_zrlE s5ErrorP
+ _symbolic _____y_____G 18FileProviderDaemon0A12ItemIDObjectC AA9VFSItemIDO
+ _symbolic _____y_____G 18FileProviderDaemon18SnapshotItemObjectC AA7VFSItemV
+ _symbolic ySay_____y__________GGcSg 18FileProviderDaemon16ReconciliationIDO AA07VFSItemE0O So06NSFileB14ItemIdentifiera
- +[FPCKTask runFPCKForDomain:domainUserInfo:domainRootURL:databaseBackupPath:urls:volumeRole:options:reason:fpfs:iCDPackageDetection:shouldPause:sendDiagnostics:saveCheckpoint:isInvalidated:contentBarrier:completionHandler:]
- -[FPDDomainDeadEndBackend resolveConflictAtURL:completionHandler:]
- -[FPDDomainExtensionBackend resolveConflictAtURL:completionHandler:]
- -[FPDWrappedSearchEnumeratorObserverProxy initWithTarget:maxNumberOfResults:]
- -[FPDWrappedSearchEnumeratorObserverProxy maxNumberOfResults]
- -[FPDWrappedSearchEnumeratorObserverProxy setMaxNumberOfResults:]
- -[FPDWrappedSearchEnumeratorProxy initWithTarget:maxNumberOfResults:]
- -[FPDXPCServicer setIndexingEnabled:forDomainIdentifier:providerIdentifier:completionHandler:].cold.1
- _OBJC_IVAR_$_FPDDomain._nsDomainOrNilForDefault
- _OBJC_IVAR_$_FPDWrappedSearchEnumeratorObserverProxy._maxNumberOfResults
- _OBJC_IVAR_$_FPDWrappedSearchEnumeratorProxy._maxNumberOfResults
- __PROTOCOLS__TtC18FileProviderDaemon12PeriodicFPCK.3
- ___100-[FPDXPCServicer _test_importItemsPendingScanningProviderProgressForDomainWithID:completionHandler:]_block_invoke.448
- ___100-[FPDXPCServicer uploadLocalVersionOfItemAtURL:bundleID:conflictResolutionPolicy:completionHandler:]_block_invoke.469
- ___103-[FPDDomainExtensionBackend startProvidingItemAtURL:readerID:readingOptions:request:completionHandler:]_block_invoke.257.cold.1
- ___103-[FPDDomainExtensionBackend startProvidingItemAtURL:readerID:readingOptions:request:completionHandler:]_block_invoke.258
- ___103-[FPDDomainExtensionBackend startProvidingItemAtURL:readerID:readingOptions:request:completionHandler:]_block_invoke_2.259
- ___103-[FPDDomainExtensionBackend startProvidingItemAtURL:readerID:readingOptions:request:completionHandler:]_block_invoke_2.259.cold.1
- ___103-[FPDDomainExtensionBackend startProvidingItemAtURL:readerID:readingOptions:request:completionHandler:]_block_invoke_2.259.cold.2
- ___103-[FPDDomainExtensionBackend startProvidingItemAtURL:readerID:readingOptions:request:completionHandler:]_block_invoke_2.259.cold.3
- ___103-[FPDDomainExtensionBackend startProvidingItemAtURL:readerID:readingOptions:request:completionHandler:]_block_invoke_2.259.cold.4
- ___103-[FPDDomainExtensionBackend startProvidingItemAtURL:readerID:readingOptions:request:completionHandler:]_block_invoke_2.259.cold.5
- ___117-[FPDDomain _provideItemAtURL:withReaderID:withProcessID:withAuditToken:kernelInfo:readingOptions:completionHandler:]_block_invoke.177
- ___125-[FPDDomainExtensionBackend createItemBasedOnTemplate:fields:urlWrapper:options:bounceOnCollision:request:completionHandler:]_block_invoke.264
- ___125-[FPDDomainExtensionBackend createItemBasedOnTemplate:fields:urlWrapper:options:bounceOnCollision:request:completionHandler:]_block_invoke.264.cold.1
- ___125-[FPDDomainExtensionBackend createItemBasedOnTemplate:fields:urlWrapper:options:bounceOnCollision:request:completionHandler:]_block_invoke.264.cold.2
- ___125-[FPDDomainExtensionBackend itemForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:request:completionHandler:]_block_invoke.272
- ___125-[FPDDomainExtensionBackend itemForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:request:completionHandler:]_block_invoke.272.cold.1
- ___125-[FPDDomainExtensionBackend itemForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:request:completionHandler:]_block_invoke.272.cold.2
- ___133-[FPDXPCServicer runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:]_block_invoke.294
- ___133-[FPDXPCServicer runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:]_block_invoke.294.cold.1
- ___133-[FPDXPCServicer runFPCKForDomainWithID:domainRootURL:databaseBackupPath:options:reason:launchType:contentBarrier:completionHandler:]_block_invoke.297
- ___146-[FPDDomainExtensionBackend URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:forBookmarkResolution:request:completionHandler:]_block_invoke.270
- ___146-[FPDDomainExtensionBackend URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:forBookmarkResolution:request:completionHandler:]_block_invoke.270.cold.1
- ___146-[FPDDomainExtensionBackend URLForItemID:creatingPlaceholderIfMissing:ignoreAlternateContentsURL:forBookmarkResolution:request:completionHandler:]_block_invoke.270.cold.2
- ___223+[FPCKTask runFPCKForDomain:domainUserInfo:domainRootURL:databaseBackupPath:urls:volumeRole:options:reason:fpfs:iCDPackageDetection:shouldPause:sendDiagnostics:saveCheckpoint:isInvalidated:contentBarrier:completionHandler:]_block_invoke
- ___223+[FPCKTask runFPCKForDomain:domainUserInfo:domainRootURL:databaseBackupPath:urls:volumeRole:options:reason:fpfs:iCDPackageDetection:shouldPause:sendDiagnostics:saveCheckpoint:isInvalidated:contentBarrier:completionHandler:]_block_invoke_2
- ___35-[FPDDomain cleanupDomainWithMode:]_block_invoke.157
- ___35-[FPDDomain cleanupDomainWithMode:]_block_invoke.157.cold.1
- ___50-[FPDDomain _writerWithID:didFinishWritingForURL:]_block_invoke.179
- ___53-[FPDXPCServicer pauseIndexingFor:completionHandler:]_block_invoke.422
- ___54-[FPDDomainExtensionBackend itemChangedAtURL:request:]_block_invoke.269
- ___54-[FPDDomainExtensionBackend itemChangedAtURL:request:]_block_invoke.269.cold.1
- ___54-[FPDXPCServicer resumeIndexingFor:completionHandler:]_block_invoke.423
- ___55-[FPDDomain didChangeItemID:request:completionHandler:]_block_invoke.208
- ___57-[FPDXPCServicer stateForDomainWithID:completionHandler:]_block_invoke.292
- ___59-[FPDXPCServicer _test_purgerBarrierWithCompletionHandler:]_block_invoke.455
- ___59-[FPDXPCServicer _test_purgerBarrierWithCompletionHandler:]_block_invoke.455.cold.1
- ___59-[FPDXPCServicer appHasNonUploadedFiles:completionHandler:]_block_invoke.305
- ___63-[FPDXPCServicer fetchDaemonOperationIDsWithCompletionHandler:]_block_invoke.380
- ___64-[FPDDomain downloadVersionThumbnail:version:completionHandler:]_block_invoke.220
- ___65-[FPDDomain _registerFileCoordinatorAndSpaceForceWithCompletion:]_block_invoke.192
- ___65-[FPDXPCServicer _test_resetDBQueryStatistics:completionHandler:]_block_invoke.450
- ___66-[FPDDomainExtensionBackend itemForURL:request:completionHandler:]_block_invoke.248
- ___66-[FPDDomainExtensionBackend itemForURL:request:completionHandler:]_block_invoke.248.cold.1
- ___66-[FPDXPCServicer importProgressForDomainWithID:completionHandler:]_block_invoke.290
- ___67-[FPDXPCServicer _test_disableDBQueryStatistics:completionHandler:]_block_invoke.449
- ___67-[FPDXPCServicer dumpTelemetryTo:providerFilter:completionHandler:]_block_invoke.357
- ___68-[FPDXPCServicer dumpDatabaseAt:fullDump:writeTo:completionHandler:]_block_invoke.300
- ___68-[FPDXPCServicer scheduleActionOperationWithInfo:completionHandler:]_block_invoke.378
- ___70-[FPDXPCServicer _test_triggerDatabaseError:domain:completionHandler:]_block_invoke.454
- ___70-[FPDXPCServicer copyDatabaseForFPCKStartingAtPath:completionHandler:]_block_invoke.371
- ___71-[FPDXPCServicer dumpStateTo:providerFilter:options:completionHandler:]_block_invoke.337
- ___73-[FPDXPCServicer _test_getDBQueryStatistics:queryPlan:completionHandler:]_block_invoke.451
- ___73-[FPDXPCServicer waitForChangesOnItemsBelowItemWithID:completionHandler:]_block_invoke.374
- ___74-[FPDXPCServicer startAccessingServiceWithName:itemURL:completionHandler:]_block_invoke.391
- ___76-[FPDXPCServicer fetchLatestVersionForItemAtURL:bundleID:completionHandler:]_block_invoke.465
- ___76-[FPDXPCServicer pauseSyncForItemAtURL:behavior:bundleID:completionHandler:]_block_invoke.459
- ___76-[FPDXPCServicer waitForStabilizationOfDomainWithID:mode:completionHandler:]_block_invoke.375
- ___77-[FPDXPCServicer _performWithCheckedEnumerationAttributes:completionHandler:]_block_invoke.401
- ___77-[FPDXPCServicer forceUpdateBlockedProcessNamesFromDomain:completionHandler:]_block_invoke.287
- ___77-[FPDXPCServicer resumeSyncForItemAtURL:behavior:bundleID:completionHandler:]_block_invoke.462
- ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.431
- ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.431.cold.1
- ___81-[FPDDomain createRootAndObserveIfNeededWithReason:userAllowedDBDrop:completion:]_block_invoke.135
- ___82-[FPDDomainExtensionBackend valuesForAttributes:forURL:request:completionHandler:]_block_invoke.304
- ___82-[FPDXPCServicer fetchAndStartEnumeratingWithSettings:observer:completionHandler:]_block_invoke.407
- ___82-[FPDXPCServicer reimportItemsBelowItemWithID:markItemDataless:completionHandler:]_block_invoke.286
- ___85-[FPDDomainExtensionBackend evictItemAtURL:evictionReason:request:completionHandler:]_block_invoke.266
- ___85-[FPDDomainExtensionBackend evictItemAtURL:evictionReason:request:completionHandler:]_block_invoke.266.cold.1
- ___85-[FPDDomainExtensionBackend evictItemAtURL:evictionReason:request:completionHandler:]_block_invoke.266.cold.2
- ___85-[FPDXPCServicer enumerateSearchResultForRequest:providerDomainID:completionHandler:]_block_invoke.396
- ___86-[FPDDomainExtensionBackend evictItemWithID:evictionReason:request:completionHandler:]_block_invoke.267
- ___86-[FPDXPCServicer setEnabled:forDomainIdentifier:providerIdentifier:completionHandler:]_block_invoke.283
- ___88-[FPDDomain _startObservingRootAndResumeIndexerWithReason:userAllowedDBDrop:completion:]_block_invoke.131
- ___88-[FPDDomain _startObservingRootAndResumeIndexerWithReason:userAllowedDBDrop:completion:]_block_invoke.131.cold.1
- ___88-[FPDDomain _startObservingRootAndResumeIndexerWithReason:userAllowedDBDrop:completion:]_block_invoke.131.cold.2
- ___88-[FPDXPCServicer spotlightReindexAllItemsForBundleID:protectionClass:completionHandler:]_block_invoke.376
- ___90-[FPDDomainExtensionBackend itemIDForURL:requireProviderItemID:request:completionHandler:]_block_invoke.251
- ___90-[FPDDomainExtensionBackend itemIDForURL:requireProviderItemID:request:completionHandler:]_block_invoke.251.cold.1
- ___90-[FPDDomainExtensionBackend itemIDForURL:requireProviderItemID:request:completionHandler:]_block_invoke.251.cold.2
- ___91-[FPDXPCServicer setHiddenByUser:forDomainIdentifier:providerIdentifier:completionHandler:]_block_invoke.284
- ___93-[FPDXPCServicer signalReindexCSIdentifiersByProviderDomainID:indexReason:completionHandler:]_block_invoke.424
- ___93-[FPDXPCServicer signalReindexCSIdentifiersByProviderDomainID:indexReason:completionHandler:]_block_invoke.424.cold.1
- ___93-[FPDXPCServicer signalReindexCSIdentifiersByProviderDomainID:indexReason:completionHandler:]_block_invoke.424.cold.2
- ___94-[FPDXPCServicer setIndexingEnabled:forDomainIdentifier:providerIdentifier:completionHandler:]_block_invoke.285
- ___96-[FPDXPCServicer _test_importItemsPendingScanningDiskProgressForDomainWithID:completionHandler:]_block_invoke.445
- ___98-[FPDXPCServicer _test_importItemsPendingReconciliationProgressForDomainWithID:completionHandler:]_block_invoke.442
- ___98-[FPDXPCServicer spotlightReindexItemsWithIdentifiers:bundleID:protectionClass:completionHandler:]_block_invoke.377
- ___block_literal_global.118
- ___block_literal_global.156
- ___block_literal_global.182
- ___block_literal_global.197
- ___block_literal_global.222
- ___block_literal_global.383
- ___block_literal_global.705
- ___block_literal_global.708
- ___block_literal_global.97
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_FileProviderDaemon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_FileProviderDaemon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_FileProviderDaemon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_FileProviderDaemon
- _block_copy_helper.1007
- _block_copy_helper.1010
- _block_copy_helper.1018
- _block_copy_helper.1022
- _block_copy_helper.1034
- _block_copy_helper.1056
- _block_copy_helper.1067
- _block_copy_helper.1080
- _block_copy_helper.109
- _block_copy_helper.1104
- _block_copy_helper.1115
- _block_copy_helper.1128
- _block_copy_helper.1135
- _block_copy_helper.1141
- _block_copy_helper.1142
- _block_copy_helper.1156
- _block_copy_helper.1157
- _block_copy_helper.1170
- _block_copy_helper.1181
- _block_copy_helper.1187
- _block_copy_helper.1201
- _block_copy_helper.1204
- _block_copy_helper.1218
- _block_copy_helper.1225
- _block_copy_helper.1231
- _block_copy_helper.1239
- _block_copy_helper.1241
- _block_copy_helper.1252
- _block_copy_helper.1255
- _block_copy_helper.1264
- _block_copy_helper.1275
- _block_copy_helper.1299
- _block_copy_helper.1300
- _block_copy_helper.1305
- _block_copy_helper.1313
- _block_copy_helper.1316
- _block_copy_helper.1325
- _block_copy_helper.1327
- _block_copy_helper.1349
- _block_copy_helper.1350
- _block_copy_helper.1353
- _block_copy_helper.1362
- _block_copy_helper.1372
- _block_copy_helper.1377
- _block_copy_helper.1380
- _block_copy_helper.1383
- _block_copy_helper.1401
- _block_copy_helper.1409
- _block_copy_helper.1414
- _block_copy_helper.1427
- _block_copy_helper.1429
- _block_copy_helper.1432
- _block_copy_helper.1435
- _block_copy_helper.1444
- _block_copy_helper.1446
- _block_copy_helper.1449
- _block_copy_helper.1460
- _block_copy_helper.1462
- _block_copy_helper.1467
- _block_copy_helper.1479
- _block_copy_helper.1484
- _block_copy_helper.1497
- _block_copy_helper.1502
- _block_copy_helper.1509
- _block_copy_helper.1516
- _block_copy_helper.1717
- _block_copy_helper.1758
- _block_copy_helper.1762
- _block_copy_helper.1784
- _block_copy_helper.1833
- _block_copy_helper.1852
- _block_copy_helper.1862
- _block_copy_helper.1872
- _block_copy_helper.1889
- _block_copy_helper.1899
- _block_copy_helper.1909
- _block_copy_helper.1919
- _block_copy_helper.1932
- _block_copy_helper.1942
- _block_copy_helper.1961
- _block_copy_helper.1973
- _block_copy_helper.1989
- _block_copy_helper.1992
- _block_copy_helper.2023
- _block_copy_helper.2042
- _block_copy_helper.2077
- _block_copy_helper.2089
- _block_copy_helper.2099
- _block_copy_helper.2111
- _block_copy_helper.2166
- _block_copy_helper.2169
- _block_copy_helper.2175
- _block_copy_helper.2178
- _block_copy_helper.2204
- _block_copy_helper.2216
- _block_copy_helper.2262
- _block_copy_helper.2265
- _block_copy_helper.2337
- _block_copy_helper.2349
- _block_copy_helper.239
- _block_copy_helper.2400
- _block_copy_helper.2403
- _block_copy_helper.2433
- _block_copy_helper.2436
- _block_copy_helper.2445
- _block_copy_helper.2515
- _block_copy_helper.2518
- _block_copy_helper.2542
- _block_copy_helper.2545
- _block_copy_helper.2575
- _block_copy_helper.2578
- _block_copy_helper.2608
- _block_copy_helper.2611
- _block_copy_helper.2634
- _block_copy_helper.2637
- _block_copy_helper.2667
- _block_copy_helper.2670
- _block_copy_helper.2686
- _block_copy_helper.2698
- _block_copy_helper.2753
- _block_copy_helper.2756
- _block_copy_helper.2820
- _block_copy_helper.2823
- _block_copy_helper.2826
- _block_copy_helper.2885
- _block_copy_helper.2888
- _block_copy_helper.292
- _block_copy_helper.2943
- _block_copy_helper.2946
- _block_copy_helper.2969
- _block_copy_helper.2972
- _block_copy_helper.2992
- _block_copy_helper.3122
- _block_copy_helper.3125
- _block_copy_helper.3147
- _block_copy_helper.3169
- _block_copy_helper.32
- _block_copy_helper.3208
- _block_copy_helper.3234
- _block_copy_helper.3237
- _block_copy_helper.3277
- _block_copy_helper.3291
- _block_copy_helper.3341
- _block_copy_helper.3344
- _block_copy_helper.3358
- _block_copy_helper.3395
- _block_copy_helper.3405
- _block_copy_helper.3415
- _block_copy_helper.3425
- _block_copy_helper.3435
- _block_copy_helper.3445
- _block_copy_helper.3461
- _block_copy_helper.3468
- _block_copy_helper.347
- _block_copy_helper.3478
- _block_copy_helper.3489
- _block_copy_helper.3499
- _block_copy_helper.3509
- _block_copy_helper.3519
- _block_copy_helper.3537
- _block_copy_helper.355
- _block_copy_helper.3563
- _block_copy_helper.3566
- _block_copy_helper.3576
- _block_copy_helper.3579
- _block_copy_helper.3592
- _block_copy_helper.3621
- _block_copy_helper.3624
- _block_copy_helper.3631
- _block_copy_helper.3643
- _block_copy_helper.3718
- _block_copy_helper.3748
- _block_copy_helper.3751
- _block_copy_helper.3758
- _block_copy_helper.3770
- _block_copy_helper.379
- _block_copy_helper.3878
- _block_copy_helper.3881
- _block_copy_helper.3890
- _block_copy_helper.393
- _block_copy_helper.3930
- _block_copy_helper.394
- _block_copy_helper.3991
- _block_copy_helper.3994
- _block_copy_helper.400
- _block_copy_helper.4004
- _block_copy_helper.4024
- _block_copy_helper.4027
- _block_copy_helper.4039
- _block_copy_helper.405
- _block_copy_helper.4072
- _block_copy_helper.4075
- _block_copy_helper.4078
- _block_copy_helper.4095
- _block_copy_helper.4128
- _block_copy_helper.4133
- _block_copy_helper.4138
- _block_copy_helper.4148
- _block_copy_helper.415
- _block_copy_helper.4174
- _block_copy_helper.418
- _block_copy_helper.4186
- _block_copy_helper.419
- _block_copy_helper.4194
- _block_copy_helper.422
- _block_copy_helper.4349
- _block_copy_helper.435
- _block_copy_helper.439
- _block_copy_helper.4404
- _block_copy_helper.4407
- _block_copy_helper.443
- _block_copy_helper.4497
- _block_copy_helper.4500
- _block_copy_helper.4531
- _block_copy_helper.4534
- _block_copy_helper.456
- _block_copy_helper.4596
- _block_copy_helper.465
- _block_copy_helper.4654
- _block_copy_helper.4657
- _block_copy_helper.4660
- _block_copy_helper.4663
- _block_copy_helper.4684
- _block_copy_helper.4687
- _block_copy_helper.470
- _block_copy_helper.4720
- _block_copy_helper.4723
- _block_copy_helper.4743
- _block_copy_helper.4753
- _block_copy_helper.4765
- _block_copy_helper.4777
- _block_copy_helper.4787
- _block_copy_helper.479
- _block_copy_helper.4797
- _block_copy_helper.4854
- _block_copy_helper.4861
- _block_copy_helper.4868
- _block_copy_helper.487
- _block_copy_helper.4878
- _block_copy_helper.4888
- _block_copy_helper.4898
- _block_copy_helper.4908
- _block_copy_helper.4914
- _block_copy_helper.4921
- _block_copy_helper.4931
- _block_copy_helper.4941
- _block_copy_helper.4948
- _block_copy_helper.4958
- _block_copy_helper.4965
- _block_copy_helper.4972
- _block_copy_helper.4979
- _block_copy_helper.499
- _block_copy_helper.5030
- _block_copy_helper.507
- _block_copy_helper.510
- _block_copy_helper.5137
- _block_copy_helper.5140
- _block_copy_helper.5188
- _block_copy_helper.519
- _block_copy_helper.521
- _block_copy_helper.5228
- _block_copy_helper.5257
- _block_copy_helper.5260
- _block_copy_helper.527
- _block_copy_helper.5270
- _block_copy_helper.5280
- _block_copy_helper.5349
- _block_copy_helper.5352
- _block_copy_helper.5373
- _block_copy_helper.5379
- _block_copy_helper.5391
- _block_copy_helper.5403
- _block_copy_helper.5415
- _block_copy_helper.5421
- _block_copy_helper.5433
- _block_copy_helper.5460
- _block_copy_helper.5463
- _block_copy_helper.549
- _block_copy_helper.5569
- _block_copy_helper.5572
- _block_copy_helper.5583
- _block_copy_helper.559
- _block_copy_helper.5595
- _block_copy_helper.5598
- _block_copy_helper.5612
- _block_copy_helper.5632
- _block_copy_helper.5638
- _block_copy_helper.5650
- _block_copy_helper.5661
- _block_copy_helper.5674
- _block_copy_helper.5685
- _block_copy_helper.569
- _block_copy_helper.5696
- _block_copy_helper.5702
- _block_copy_helper.5714
- _block_copy_helper.575
- _block_copy_helper.5809
- _block_copy_helper.5812
- _block_copy_helper.585
- _block_copy_helper.588
- _block_copy_helper.5951
- _block_copy_helper.5954
- _block_copy_helper.597
- _block_copy_helper.6009
- _block_copy_helper.6012
- _block_copy_helper.603
- _block_copy_helper.6041
- _block_copy_helper.6067
- _block_copy_helper.6070
- _block_copy_helper.609
- _block_copy_helper.6097
- _block_copy_helper.6100
- _block_copy_helper.6133
- _block_copy_helper.6136
- _block_copy_helper.617
- _block_copy_helper.6181
- _block_copy_helper.6191
- _block_copy_helper.6220
- _block_copy_helper.6223
- _block_copy_helper.6233
- _block_copy_helper.6244
- _block_copy_helper.625
- _block_copy_helper.6255
- _block_copy_helper.628
- _block_copy_helper.6307
- _block_copy_helper.6310
- _block_copy_helper.6336
- _block_copy_helper.635
- _block_copy_helper.6354
- _block_copy_helper.6366
- _block_copy_helper.6384
- _block_copy_helper.639
- _block_copy_helper.6396
- _block_copy_helper.6414
- _block_copy_helper.642
- _block_copy_helper.6424
- _block_copy_helper.645
- _block_copy_helper.6456
- _block_copy_helper.6459
- _block_copy_helper.663
- _block_copy_helper.665
- _block_copy_helper.677
- _block_copy_helper.679
- _block_copy_helper.689
- _block_copy_helper.703
- _block_copy_helper.737
- _block_copy_helper.757
- _block_copy_helper.764
- _block_copy_helper.767
- _block_copy_helper.77
- _block_copy_helper.777
- _block_copy_helper.781
- _block_copy_helper.787
- _block_copy_helper.790
- _block_copy_helper.797
- _block_copy_helper.800
- _block_copy_helper.804
- _block_copy_helper.807
- _block_copy_helper.810
- _block_copy_helper.815
- _block_copy_helper.825
- _block_copy_helper.835
- _block_copy_helper.848
- _block_copy_helper.851
- _block_copy_helper.862
- _block_copy_helper.867
- _block_copy_helper.870
- _block_copy_helper.875
- _block_copy_helper.876
- _block_copy_helper.878
- _block_copy_helper.889
- _block_copy_helper.892
- _block_copy_helper.905
- _block_copy_helper.910
- _block_copy_helper.912
- _block_copy_helper.917
- _block_copy_helper.924
- _block_copy_helper.931
- _block_copy_helper.939
- _block_copy_helper.954
- _block_copy_helper.955
- _block_copy_helper.971
- _block_copy_helper.974
- _block_copy_helper.988
- _block_copy_helper.997
- _block_copy_helper.999
- _block_descriptor.1001
- _block_descriptor.1009
- _block_descriptor.1012
- _block_descriptor.1020
- _block_descriptor.1024
- _block_descriptor.1036
- _block_descriptor.1058
- _block_descriptor.1069
- _block_descriptor.1082
- _block_descriptor.1106
- _block_descriptor.111
- _block_descriptor.1117
- _block_descriptor.1130
- _block_descriptor.1137
- _block_descriptor.1143
- _block_descriptor.1144
- _block_descriptor.1158
- _block_descriptor.1159
- _block_descriptor.1172
- _block_descriptor.1183
- _block_descriptor.1189
- _block_descriptor.1203
- _block_descriptor.1206
- _block_descriptor.1220
- _block_descriptor.1227
- _block_descriptor.1233
- _block_descriptor.1241
- _block_descriptor.1243
- _block_descriptor.1254
- _block_descriptor.1257
- _block_descriptor.1266
- _block_descriptor.1277
- _block_descriptor.1301
- _block_descriptor.1302
- _block_descriptor.1307
- _block_descriptor.1315
- _block_descriptor.1318
- _block_descriptor.1327
- _block_descriptor.1329
- _block_descriptor.1351
- _block_descriptor.1352
- _block_descriptor.1355
- _block_descriptor.1364
- _block_descriptor.1374
- _block_descriptor.1379
- _block_descriptor.1382
- _block_descriptor.1385
- _block_descriptor.1403
- _block_descriptor.1411
- _block_descriptor.1416
- _block_descriptor.1429
- _block_descriptor.1431
- _block_descriptor.1434
- _block_descriptor.1437
- _block_descriptor.1446
- _block_descriptor.1448
- _block_descriptor.1451
- _block_descriptor.1462
- _block_descriptor.1464
- _block_descriptor.1469
- _block_descriptor.1481
- _block_descriptor.1486
- _block_descriptor.1499
- _block_descriptor.1504
- _block_descriptor.1511
- _block_descriptor.1518
- _block_descriptor.1719
- _block_descriptor.1760
- _block_descriptor.1764
- _block_descriptor.1786
- _block_descriptor.1835
- _block_descriptor.1854
- _block_descriptor.1864
- _block_descriptor.1874
- _block_descriptor.1891
- _block_descriptor.1901
- _block_descriptor.1911
- _block_descriptor.1921
- _block_descriptor.1934
- _block_descriptor.1944
- _block_descriptor.1963
- _block_descriptor.1975
- _block_descriptor.1991
- _block_descriptor.1994
- _block_descriptor.2025
- _block_descriptor.2044
- _block_descriptor.2079
- _block_descriptor.2091
- _block_descriptor.2101
- _block_descriptor.2113
- _block_descriptor.2168
- _block_descriptor.2171
- _block_descriptor.2177
- _block_descriptor.2180
- _block_descriptor.2206
- _block_descriptor.2218
- _block_descriptor.2264
- _block_descriptor.2267
- _block_descriptor.2339
- _block_descriptor.2351
- _block_descriptor.2402
- _block_descriptor.2405
- _block_descriptor.241
- _block_descriptor.2435
- _block_descriptor.2438
- _block_descriptor.2447
- _block_descriptor.2517
- _block_descriptor.2520
- _block_descriptor.2544
- _block_descriptor.2547
- _block_descriptor.2577
- _block_descriptor.2580
- _block_descriptor.2610
- _block_descriptor.2613
- _block_descriptor.2636
- _block_descriptor.2639
- _block_descriptor.2669
- _block_descriptor.2672
- _block_descriptor.2688
- _block_descriptor.2700
- _block_descriptor.2755
- _block_descriptor.2758
- _block_descriptor.2822
- _block_descriptor.2825
- _block_descriptor.2828
- _block_descriptor.2887
- _block_descriptor.2890
- _block_descriptor.294
- _block_descriptor.2945
- _block_descriptor.2948
- _block_descriptor.2971
- _block_descriptor.2974
- _block_descriptor.2994
- _block_descriptor.3124
- _block_descriptor.3127
- _block_descriptor.3149
- _block_descriptor.3171
- _block_descriptor.3210
- _block_descriptor.3236
- _block_descriptor.3239
- _block_descriptor.3279
- _block_descriptor.3293
- _block_descriptor.3343
- _block_descriptor.3346
- _block_descriptor.3360
- _block_descriptor.3397
- _block_descriptor.34
- _block_descriptor.3407
- _block_descriptor.3417
- _block_descriptor.3427
- _block_descriptor.3437
- _block_descriptor.3447
- _block_descriptor.3463
- _block_descriptor.3470
- _block_descriptor.3480
- _block_descriptor.349
- _block_descriptor.3491
- _block_descriptor.3501
- _block_descriptor.3511
- _block_descriptor.3521
- _block_descriptor.3539
- _block_descriptor.3565
- _block_descriptor.3568
- _block_descriptor.357
- _block_descriptor.3578
- _block_descriptor.3581
- _block_descriptor.3594
- _block_descriptor.3623
- _block_descriptor.3626
- _block_descriptor.3633
- _block_descriptor.3645
- _block_descriptor.3720
- _block_descriptor.3750
- _block_descriptor.3753
- _block_descriptor.3760
- _block_descriptor.3772
- _block_descriptor.381
- _block_descriptor.3880
- _block_descriptor.3883
- _block_descriptor.3892
- _block_descriptor.3932
- _block_descriptor.395
- _block_descriptor.396
- _block_descriptor.3993
- _block_descriptor.3996
- _block_descriptor.4006
- _block_descriptor.402
- _block_descriptor.4026
- _block_descriptor.4029
- _block_descriptor.4041
- _block_descriptor.407
- _block_descriptor.4074
- _block_descriptor.4077
- _block_descriptor.4080
- _block_descriptor.4097
- _block_descriptor.4130
- _block_descriptor.4135
- _block_descriptor.4140
- _block_descriptor.4150
- _block_descriptor.417
- _block_descriptor.4176
- _block_descriptor.4188
- _block_descriptor.4196
- _block_descriptor.420
- _block_descriptor.421
- _block_descriptor.424
- _block_descriptor.4351
- _block_descriptor.437
- _block_descriptor.4406
- _block_descriptor.4409
- _block_descriptor.441
- _block_descriptor.445
- _block_descriptor.4499
- _block_descriptor.4502
- _block_descriptor.4533
- _block_descriptor.4536
- _block_descriptor.458
- _block_descriptor.4598
- _block_descriptor.4656
- _block_descriptor.4659
- _block_descriptor.4662
- _block_descriptor.4665
- _block_descriptor.467
- _block_descriptor.4686
- _block_descriptor.4689
- _block_descriptor.472
- _block_descriptor.4722
- _block_descriptor.4725
- _block_descriptor.4745
- _block_descriptor.4755
- _block_descriptor.4767
- _block_descriptor.4779
- _block_descriptor.4789
- _block_descriptor.4799
- _block_descriptor.481
- _block_descriptor.4856
- _block_descriptor.4863
- _block_descriptor.4870
- _block_descriptor.4880
- _block_descriptor.489
- _block_descriptor.4890
- _block_descriptor.4900
- _block_descriptor.4910
- _block_descriptor.4916
- _block_descriptor.4923
- _block_descriptor.4933
- _block_descriptor.4943
- _block_descriptor.4950
- _block_descriptor.4960
- _block_descriptor.4967
- _block_descriptor.4974
- _block_descriptor.4981
- _block_descriptor.501
- _block_descriptor.5032
- _block_descriptor.509
- _block_descriptor.512
- _block_descriptor.5139
- _block_descriptor.5142
- _block_descriptor.5190
- _block_descriptor.521
- _block_descriptor.523
- _block_descriptor.5230
- _block_descriptor.5259
- _block_descriptor.5262
- _block_descriptor.5272
- _block_descriptor.5282
- _block_descriptor.529
- _block_descriptor.5351
- _block_descriptor.5354
- _block_descriptor.5375
- _block_descriptor.5381
- _block_descriptor.5393
- _block_descriptor.5405
- _block_descriptor.5417
- _block_descriptor.5423
- _block_descriptor.5435
- _block_descriptor.5462
- _block_descriptor.5465
- _block_descriptor.551
- _block_descriptor.5571
- _block_descriptor.5574
- _block_descriptor.5585
- _block_descriptor.5597
- _block_descriptor.5600
- _block_descriptor.561
- _block_descriptor.5614
- _block_descriptor.5634
- _block_descriptor.5640
- _block_descriptor.5652
- _block_descriptor.5663
- _block_descriptor.5676
- _block_descriptor.5687
- _block_descriptor.5698
- _block_descriptor.5704
- _block_descriptor.571
- _block_descriptor.5716
- _block_descriptor.577
- _block_descriptor.5811
- _block_descriptor.5814
- _block_descriptor.587
- _block_descriptor.590
- _block_descriptor.5953
- _block_descriptor.5956
- _block_descriptor.599
- _block_descriptor.6011
- _block_descriptor.6014
- _block_descriptor.6043
- _block_descriptor.605
- _block_descriptor.6069
- _block_descriptor.6072
- _block_descriptor.6099
- _block_descriptor.6102
- _block_descriptor.611
- _block_descriptor.6135
- _block_descriptor.6138
- _block_descriptor.6183
- _block_descriptor.619
- _block_descriptor.6193
- _block_descriptor.6222
- _block_descriptor.6225
- _block_descriptor.6235
- _block_descriptor.6246
- _block_descriptor.6257
- _block_descriptor.627
- _block_descriptor.630
- _block_descriptor.6309
- _block_descriptor.6312
- _block_descriptor.6338
- _block_descriptor.6356
- _block_descriptor.6368
- _block_descriptor.637
- _block_descriptor.6386
- _block_descriptor.6398
- _block_descriptor.641
- _block_descriptor.6416
- _block_descriptor.6426
- _block_descriptor.644
- _block_descriptor.6458
- _block_descriptor.6461
- _block_descriptor.647
- _block_descriptor.665
- _block_descriptor.667
- _block_descriptor.679
- _block_descriptor.681
- _block_descriptor.691
- _block_descriptor.705
- _block_descriptor.739
- _block_descriptor.759
- _block_descriptor.766
- _block_descriptor.769
- _block_descriptor.779
- _block_descriptor.783
- _block_descriptor.789
- _block_descriptor.79
- _block_descriptor.792
- _block_descriptor.799
- _block_descriptor.802
- _block_descriptor.806
- _block_descriptor.809
- _block_descriptor.812
- _block_descriptor.817
- _block_descriptor.827
- _block_descriptor.837
- _block_descriptor.850
- _block_descriptor.853
- _block_descriptor.864
- _block_descriptor.869
- _block_descriptor.872
- _block_descriptor.877
- _block_descriptor.878
- _block_descriptor.880
- _block_descriptor.891
- _block_descriptor.894
- _block_descriptor.907
- _block_descriptor.912
- _block_descriptor.914
- _block_descriptor.919
- _block_descriptor.926
- _block_descriptor.933
- _block_descriptor.941
- _block_descriptor.956
- _block_descriptor.957
- _block_descriptor.973
- _block_descriptor.976
- _block_descriptor.990
- _block_descriptor.999
- _block_destroy_helper.1000
- _block_destroy_helper.1008
- _block_destroy_helper.1011
- _block_destroy_helper.1019
- _block_destroy_helper.1023
- _block_destroy_helper.1035
- _block_destroy_helper.1057
- _block_destroy_helper.1068
- _block_destroy_helper.1081
- _block_destroy_helper.110
- _block_destroy_helper.1105
- _block_destroy_helper.1116
- _block_destroy_helper.1129
- _block_destroy_helper.1136
- _block_destroy_helper.1142
- _block_destroy_helper.1143
- _block_destroy_helper.1157
- _block_destroy_helper.1158
- _block_destroy_helper.1171
- _block_destroy_helper.1182
- _block_destroy_helper.1188
- _block_destroy_helper.1202
- _block_destroy_helper.1205
- _block_destroy_helper.1219
- _block_destroy_helper.1226
- _block_destroy_helper.1232
- _block_destroy_helper.1240
- _block_destroy_helper.1242
- _block_destroy_helper.1253
- _block_destroy_helper.1256
- _block_destroy_helper.1265
- _block_destroy_helper.1276
- _block_destroy_helper.1300
- _block_destroy_helper.1301
- _block_destroy_helper.1306
- _block_destroy_helper.1314
- _block_destroy_helper.1317
- _block_destroy_helper.1326
- _block_destroy_helper.1328
- _block_destroy_helper.1350
- _block_destroy_helper.1351
- _block_destroy_helper.1354
- _block_destroy_helper.1363
- _block_destroy_helper.1373
- _block_destroy_helper.1378
- _block_destroy_helper.1381
- _block_destroy_helper.1384
- _block_destroy_helper.1402
- _block_destroy_helper.1410
- _block_destroy_helper.1415
- _block_destroy_helper.1428
- _block_destroy_helper.1430
- _block_destroy_helper.1433
- _block_destroy_helper.1436
- _block_destroy_helper.1445
- _block_destroy_helper.1447
- _block_destroy_helper.1450
- _block_destroy_helper.1461
- _block_destroy_helper.1463
- _block_destroy_helper.1468
- _block_destroy_helper.1480
- _block_destroy_helper.1485
- _block_destroy_helper.1498
- _block_destroy_helper.1503
- _block_destroy_helper.1510
- _block_destroy_helper.1517
- _block_destroy_helper.1718
- _block_destroy_helper.1759
- _block_destroy_helper.1763
- _block_destroy_helper.1785
- _block_destroy_helper.1834
- _block_destroy_helper.1853
- _block_destroy_helper.1863
- _block_destroy_helper.1873
- _block_destroy_helper.1890
- _block_destroy_helper.1900
- _block_destroy_helper.1910
- _block_destroy_helper.1920
- _block_destroy_helper.1933
- _block_destroy_helper.1943
- _block_destroy_helper.1962
- _block_destroy_helper.1974
- _block_destroy_helper.1990
- _block_destroy_helper.1993
- _block_destroy_helper.2024
- _block_destroy_helper.2043
- _block_destroy_helper.2078
- _block_destroy_helper.2090
- _block_destroy_helper.2100
- _block_destroy_helper.2112
- _block_destroy_helper.2167
- _block_destroy_helper.2170
- _block_destroy_helper.2176
- _block_destroy_helper.2179
- _block_destroy_helper.2205
- _block_destroy_helper.2217
- _block_destroy_helper.2263
- _block_destroy_helper.2266
- _block_destroy_helper.2338
- _block_destroy_helper.2350
- _block_destroy_helper.240
- _block_destroy_helper.2401
- _block_destroy_helper.2404
- _block_destroy_helper.2434
- _block_destroy_helper.2437
- _block_destroy_helper.2446
- _block_destroy_helper.2516
- _block_destroy_helper.2519
- _block_destroy_helper.2543
- _block_destroy_helper.2546
- _block_destroy_helper.2576
- _block_destroy_helper.2579
- _block_destroy_helper.2609
- _block_destroy_helper.2612
- _block_destroy_helper.2635
- _block_destroy_helper.2638
- _block_destroy_helper.2668
- _block_destroy_helper.2671
- _block_destroy_helper.2687
- _block_destroy_helper.2699
- _block_destroy_helper.2754
- _block_destroy_helper.2757
- _block_destroy_helper.2821
- _block_destroy_helper.2824
- _block_destroy_helper.2827
- _block_destroy_helper.2886
- _block_destroy_helper.2889
- _block_destroy_helper.293
- _block_destroy_helper.2944
- _block_destroy_helper.2947
- _block_destroy_helper.2970
- _block_destroy_helper.2973
- _block_destroy_helper.2993
- _block_destroy_helper.3123
- _block_destroy_helper.3126
- _block_destroy_helper.3148
- _block_destroy_helper.3170
- _block_destroy_helper.3209
- _block_destroy_helper.3235
- _block_destroy_helper.3238
- _block_destroy_helper.3278
- _block_destroy_helper.3292
- _block_destroy_helper.33
- _block_destroy_helper.3342
- _block_destroy_helper.3345
- _block_destroy_helper.3359
- _block_destroy_helper.3396
- _block_destroy_helper.3406
- _block_destroy_helper.3416
- _block_destroy_helper.3426
- _block_destroy_helper.3436
- _block_destroy_helper.3446
- _block_destroy_helper.3462
- _block_destroy_helper.3469
- _block_destroy_helper.3479
- _block_destroy_helper.348
- _block_destroy_helper.3490
- _block_destroy_helper.3500
- _block_destroy_helper.3510
- _block_destroy_helper.3520
- _block_destroy_helper.3538
- _block_destroy_helper.356
- _block_destroy_helper.3564
- _block_destroy_helper.3567
- _block_destroy_helper.3577
- _block_destroy_helper.3580
- _block_destroy_helper.3593
- _block_destroy_helper.3622
- _block_destroy_helper.3625
- _block_destroy_helper.3632
- _block_destroy_helper.3644
- _block_destroy_helper.3719
- _block_destroy_helper.3749
- _block_destroy_helper.3752
- _block_destroy_helper.3759
- _block_destroy_helper.3771
- _block_destroy_helper.380
- _block_destroy_helper.3879
- _block_destroy_helper.3882
- _block_destroy_helper.3891
- _block_destroy_helper.3931
- _block_destroy_helper.394
- _block_destroy_helper.395
- _block_destroy_helper.3992
- _block_destroy_helper.3995
- _block_destroy_helper.4005
- _block_destroy_helper.401
- _block_destroy_helper.4025
- _block_destroy_helper.4028
- _block_destroy_helper.4040
- _block_destroy_helper.406
- _block_destroy_helper.4073
- _block_destroy_helper.4076
- _block_destroy_helper.4079
- _block_destroy_helper.4096
- _block_destroy_helper.4129
- _block_destroy_helper.4134
- _block_destroy_helper.4139
- _block_destroy_helper.4149
- _block_destroy_helper.416
- _block_destroy_helper.4175
- _block_destroy_helper.4187
- _block_destroy_helper.419
- _block_destroy_helper.4195
- _block_destroy_helper.420
- _block_destroy_helper.423
- _block_destroy_helper.4350
- _block_destroy_helper.436
- _block_destroy_helper.440
- _block_destroy_helper.4405
- _block_destroy_helper.4408
- _block_destroy_helper.444
- _block_destroy_helper.4498
- _block_destroy_helper.4501
- _block_destroy_helper.4532
- _block_destroy_helper.4535
- _block_destroy_helper.457
- _block_destroy_helper.4597
- _block_destroy_helper.4655
- _block_destroy_helper.4658
- _block_destroy_helper.466
- _block_destroy_helper.4661
- _block_destroy_helper.4664
- _block_destroy_helper.4685
- _block_destroy_helper.4688
- _block_destroy_helper.471
- _block_destroy_helper.4721
- _block_destroy_helper.4724
- _block_destroy_helper.4744
- _block_destroy_helper.4754
- _block_destroy_helper.4766
- _block_destroy_helper.4778
- _block_destroy_helper.4788
- _block_destroy_helper.4798
- _block_destroy_helper.480
- _block_destroy_helper.4855
- _block_destroy_helper.4862
- _block_destroy_helper.4869
- _block_destroy_helper.4879
- _block_destroy_helper.488
- _block_destroy_helper.4889
- _block_destroy_helper.4899
- _block_destroy_helper.4909
- _block_destroy_helper.4915
- _block_destroy_helper.4922
- _block_destroy_helper.4932
- _block_destroy_helper.4942
- _block_destroy_helper.4949
- _block_destroy_helper.4959
- _block_destroy_helper.4966
- _block_destroy_helper.4973
- _block_destroy_helper.4980
- _block_destroy_helper.500
- _block_destroy_helper.5031
- _block_destroy_helper.508
- _block_destroy_helper.511
- _block_destroy_helper.5138
- _block_destroy_helper.5141
- _block_destroy_helper.5189
- _block_destroy_helper.520
- _block_destroy_helper.522
- _block_destroy_helper.5229
- _block_destroy_helper.5258
- _block_destroy_helper.5261
- _block_destroy_helper.5271
- _block_destroy_helper.528
- _block_destroy_helper.5281
- _block_destroy_helper.5350
- _block_destroy_helper.5353
- _block_destroy_helper.5374
- _block_destroy_helper.5380
- _block_destroy_helper.5392
- _block_destroy_helper.5404
- _block_destroy_helper.5416
- _block_destroy_helper.5422
- _block_destroy_helper.5434
- _block_destroy_helper.5461
- _block_destroy_helper.5464
- _block_destroy_helper.550
- _block_destroy_helper.5570
- _block_destroy_helper.5573
- _block_destroy_helper.5584
- _block_destroy_helper.5596
- _block_destroy_helper.5599
- _block_destroy_helper.560
- _block_destroy_helper.5613
- _block_destroy_helper.5633
- _block_destroy_helper.5639
- _block_destroy_helper.5651
- _block_destroy_helper.5662
- _block_destroy_helper.5675
- _block_destroy_helper.5686
- _block_destroy_helper.5697
- _block_destroy_helper.570
- _block_destroy_helper.5703
- _block_destroy_helper.5715
- _block_destroy_helper.576
- _block_destroy_helper.5810
- _block_destroy_helper.5813
- _block_destroy_helper.586
- _block_destroy_helper.589
- _block_destroy_helper.5952
- _block_destroy_helper.5955
- _block_destroy_helper.598
- _block_destroy_helper.6010
- _block_destroy_helper.6013
- _block_destroy_helper.604
- _block_destroy_helper.6042
- _block_destroy_helper.6068
- _block_destroy_helper.6071
- _block_destroy_helper.6098
- _block_destroy_helper.610
- _block_destroy_helper.6101
- _block_destroy_helper.6134
- _block_destroy_helper.6137
- _block_destroy_helper.618
- _block_destroy_helper.6182
- _block_destroy_helper.6192
- _block_destroy_helper.6221
- _block_destroy_helper.6224
- _block_destroy_helper.6234
- _block_destroy_helper.6245
- _block_destroy_helper.6256
- _block_destroy_helper.626
- _block_destroy_helper.629
- _block_destroy_helper.6308
- _block_destroy_helper.6311
- _block_destroy_helper.6337
- _block_destroy_helper.6355
- _block_destroy_helper.636
- _block_destroy_helper.6367
- _block_destroy_helper.6385
- _block_destroy_helper.6397
- _block_destroy_helper.640
- _block_destroy_helper.6415
- _block_destroy_helper.6425
- _block_destroy_helper.643
- _block_destroy_helper.6457
- _block_destroy_helper.646
- _block_destroy_helper.6460
- _block_destroy_helper.664
- _block_destroy_helper.666
- _block_destroy_helper.678
- _block_destroy_helper.680
- _block_destroy_helper.690
- _block_destroy_helper.704
- _block_destroy_helper.738
- _block_destroy_helper.758
- _block_destroy_helper.765
- _block_destroy_helper.768
- _block_destroy_helper.778
- _block_destroy_helper.78
- _block_destroy_helper.782
- _block_destroy_helper.788
- _block_destroy_helper.791
- _block_destroy_helper.798
- _block_destroy_helper.801
- _block_destroy_helper.805
- _block_destroy_helper.808
- _block_destroy_helper.811
- _block_destroy_helper.816
- _block_destroy_helper.826
- _block_destroy_helper.836
- _block_destroy_helper.849
- _block_destroy_helper.852
- _block_destroy_helper.863
- _block_destroy_helper.868
- _block_destroy_helper.871
- _block_destroy_helper.876
- _block_destroy_helper.877
- _block_destroy_helper.879
- _block_destroy_helper.890
- _block_destroy_helper.893
- _block_destroy_helper.906
- _block_destroy_helper.911
- _block_destroy_helper.913
- _block_destroy_helper.918
- _block_destroy_helper.925
- _block_destroy_helper.932
- _block_destroy_helper.940
- _block_destroy_helper.955
- _block_destroy_helper.956
- _block_destroy_helper.972
- _block_destroy_helper.975
- _block_destroy_helper.989
- _block_destroy_helper.998
- _get_type_metadata 15Synchronization5MutexVySDySSSiGG.124
- _objc_msgSend$initWithDatabasesBackupsPaths:volumeRole:providerDomainID:domainUserInfo:reason:usingFPFS:iCDPackageDetection:useShouldPause:shouldPause:sendDiagnostics:saveCheckpoint:isInvalidated:
- _objc_msgSend$initWithTarget:maxNumberOfResults:
- _objc_msgSend$maxNumberOfResults
- _objc_msgSend$resolveConflictAtURL:completionHandler:
- _objc_msgSend$runFPCKForDomain:domainUserInfo:domainRootURL:databaseBackupPath:urls:volumeRole:options:reason:fpfs:iCDPackageDetection:shouldPause:sendDiagnostics:saveCheckpoint:isInvalidated:contentBarrier:completionHandler:
- _objc_release_x10
- _objectdestroy.1033Tm
- _objectdestroy.104Tm
- _objectdestroy.1064Tm
- _objectdestroy.1080Tm
- _objectdestroy.1083Tm
- _objectdestroy.1239Tm
- _objectdestroy.123Tm
- _objectdestroy.1245Tm
- _objectdestroy.1251Tm
- _objectdestroy.143Tm
- _objectdestroy.152Tm
- _objectdestroy.155Tm
- _objectdestroy.158Tm
- _objectdestroy.1592Tm
- _objectdestroy.164Tm
- _objectdestroy.1768Tm
- _objectdestroy.176Tm
- _objectdestroy.1775Tm
- _objectdestroy.1779Tm
- _objectdestroy.180Tm
- _objectdestroy.194Tm
- _objectdestroy.2192Tm
- _objectdestroy.2195Tm
- _objectdestroy.220Tm
- _objectdestroy.223Tm
- _objectdestroy.226Tm
- _objectdestroy.2286Tm
- _objectdestroy.2295Tm
- _objectdestroy.2301Tm
- _objectdestroy.2304Tm
- _objectdestroy.2382Tm
- _objectdestroy.2391Tm
- _objectdestroy.2423Tm
- _objectdestroy.2532Tm
- _objectdestroy.2736Tm
- _objectdestroy.2743Tm
- _objectdestroy.2763Tm
- _objectdestroy.2766Tm
- _objectdestroy.2867Tm
- _objectdestroy.2979Tm
- _objectdestroy.298Tm
- _objectdestroy.299Tm
- _objectdestroy.3016Tm
- _objectdestroy.3109Tm
- _objectdestroy.3133Tm
- _objectdestroy.3179Tm
- _objectdestroy.3189Tm
- _objectdestroy.3192Tm
- _objectdestroy.3195Tm
- _objectdestroy.325Tm
- _objectdestroy.3269Tm
- _objectdestroy.3275Tm
- _objectdestroy.327Tm
- _objectdestroy.3286Tm
- _objectdestroy.3320Tm
- _objectdestroy.332Tm
- _objectdestroy.335Tm
- _objectdestroy.339Tm
- _objectdestroy.3419Tm
- _objectdestroy.357Tm
- _objectdestroy.3660Tm
- _objectdestroy.3674Tm
- _objectdestroy.367Tm
- _objectdestroy.3796Tm
- _objectdestroy.37Tm
- _objectdestroy.382Tm
- _objectdestroy.3865Tm
- _objectdestroy.3869Tm
- _objectdestroy.398Tm
- _objectdestroy.404Tm
- _objectdestroy.407Tm
- _objectdestroy.4105Tm
- _objectdestroy.410Tm
- _objectdestroy.4235Tm
- _objectdestroy.4261Tm
- _objectdestroy.4281Tm
- _objectdestroy.428Tm
- _objectdestroy.430Tm
- _objectdestroy.433Tm
- _objectdestroy.443Tm
- _objectdestroy.4479Tm
- _objectdestroy.452Tm
- _objectdestroy.455Tm
- _objectdestroy.4590Tm
- _objectdestroy.473Tm
- _objectdestroy.4807Tm
- _objectdestroy.494Tm
- _objectdestroy.5114Tm
- _objectdestroy.5119Tm
- _objectdestroy.5157Tm
- _objectdestroy.5816Tm
- _objectdestroy.5847Tm
- _objectdestroy.5902Tm
- _objectdestroy.5912Tm
- _objectdestroy.592Tm
- _objectdestroy.5971Tm
- _objectdestroy.5978Tm
- _objectdestroy.6016Tm
- _objectdestroy.6179Tm
- _objectdestroy.622Tm
- _objectdestroy.625Tm
- _objectdestroy.628Tm
- _objectdestroy.654Tm
- _objectdestroy.664Tm
- _objectdestroy.675Tm
- _objectdestroy.681Tm
- _objectdestroy.735Tm
- _objectdestroy.739Tm
- _objectdestroy.790Tm
- _objectdestroy.799Tm
- _objectdestroy.817Tm
- _objectdestroy.829Tm
- _objectdestroy.850Tm
- _objectdestroy.858Tm
- _objectdestroy.903Tm
- _objectdestroy.95Tm
- _objectdestroy.965Tm
- _objectdestroy.98Tm
- _objectdestroy.9Tm
- _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
- _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
- _swift_cvw_singlePayloadEnumGeneric_getEnumTag
- _symbolic Say_____y__________GG 18FileProviderDaemon16ReconciliationIDO So06NSFileB14ItemIdentifiera AA07VFSItemE0O
CStrings:
+ "@\"NSRecursiveLock\""
+ "@104@0:8@16I24@28@36Q44B52B56B60@?64@?72@?80@?88@?96"
+ "A call from %@ to getDomainsForProviderIdentifier failed: %@"
+ "Encountered %@ while ingesting items from FPCK"
+ "Failed to fix blockedByParentCreation items: cannot reingest items"
+ "Failed to fix blockedByParentCreation items: no db available"
+ "Failed to fix blockedByParentCreation items: no deviceID"
+ "Failed to fix blockedByParentCreation items: no parentID"
+ "FileProvider API Issue: getDomainsForProviderIdentifier failed"
+ "Provider not found for URL."
+ "Provider upload error"
+ "Reingested %ld items (expected: %ld)"
+ "Repairing %{public}s is is not supported"
+ "T@\"NSFileProviderDomain\",&,D,N"
+ "T@\"NSFileProviderDomain\",R,N,GnsDomain"
+ "TQ,N,V_maximumNumberOfResultsPerPage"
+ "[DEBUG] 🧹 reingestItemIDs not supported for onDemand"
+ "[ERROR] getDomainsForProviderIdentifier(%@) failed: %@"
+ "_maximumNumberOfResultsPerPage"
+ "_nsDomainLock"
+ "a problem gathering domains occured"
+ "canReingestItems"
+ "desiredNumberOfResults"
+ "fixing blockedByParentCreation on %s"
+ "fixing blockedByParentCreation on parent %s"
+ "fsRepair"
+ "indexer is disabled, updating indexing barrier (index dropped: %{bool}d, anchor: %s)"
+ "indexer is enabled, updating indexing barrier (index dropped: %{bool}d, anchor: %s)"
+ "initWithDatabasesBackupsPaths:volumeRole:providerDomainID:domainUserInfo:reason:usingFPFS:iCDPackageDetection:useShouldPause:shouldPause:sendDiagnostics:saveCheckpoint:reingestItems:isInvalidated:"
+ "initWithQuery:desiredNumberOfResults:maximumNumberOfResultsPerPage:"
+ "initWithTarget:maximumNumberOfResultsPerPage:"
+ "itemIDsToReingest"
+ "maximumNumberOfResultsPerPage"
+ "provider upload error"
+ "reingestItemIDs:"
+ "reingestItems"
+ "reingestItems(vfsItemsIDs:order:reason:_:)"
+ "reingestItemsInDomain"
+ "reloadSyncEngine"
+ "reloadSyncEngine failed: %@"
+ "resolveConflict("
+ "resolveConflict(at:request:completionHandler:)"
+ "resolveConflictAtURL:request:completionHandler:"
+ "runFPCKForDomain:domainUserInfo:domainRootURL:databaseBackupPath:urls:volumeRole:options:reason:fpfs:iCDPackageDetection:shouldPause:sendDiagnostics:saveCheckpoint:reingestItems:isInvalidated:contentBarrier:completionHandler:"
+ "setMaximumNumberOfResultsPerPage:"
+ "trial_configuration"
+ "unlock"
+ "v140@0:8@16@24@32@40@48I56Q60Q68B76B80@?84@?92@?100@?108@?116q124@?132"
+ "⚔️  Scheduling conflict resolution for item %{public}s by %{public}s..."
+ "🧹 FPCK %s: cannot send reingestion, the sender is nil"
+ "🧹 FPCK %s: error encoding IDs for reingestion"
+ "🧹 FPCK %s: launching reingestion check"
+ "🧹 FPCK %s: reingestion check took %fs"
+ "🧹 FPCK %s: sending reingestion, we have items"
+ "🧹 FPCK %s: skipping reingestion, no items"
+ "🧹 could not accept items to reingest from FPCK, reingestItemsInDomain is nil"
+ "🧹 failed decoding VFSItemID for reingestion from FPCK"
+ "🧹 reingesting items from Periodic FPCK"
- "@96@0:8@16I24@28@36Q44B52B56B60@?64@?72@?80@?88"
- "T@\"NSFileProviderDomain\",&,N,V_nsDomainOrNilForDefault"
- "T@\"NSFileProviderDomain\",R,N,V_nsDomain"
- "Tq,N,V_maxNumberOfResults"
- "_maxNumberOfResults"
- "_nsDomainOrNilForDefault"
- "initWithDatabasesBackupsPaths:volumeRole:providerDomainID:domainUserInfo:reason:usingFPFS:iCDPackageDetection:useShouldPause:shouldPause:sendDiagnostics:saveCheckpoint:isInvalidated:"
- "initWithQuery:maxNumberOfResults:"
- "initWithTarget:maxNumberOfResults:"
- "maxNumberOfResults"
- "resolveConflict(at:completionHandler:)"
- "runFPCKForDomain:domainUserInfo:domainRootURL:databaseBackupPath:urls:volumeRole:options:reason:fpfs:iCDPackageDetection:shouldPause:sendDiagnostics:saveCheckpoint:isInvalidated:contentBarrier:completionHandler:"
- "setMaxNumberOfResults:"
- "v132@0:8@16@24@32@40@48I56Q60Q68B76B80@?84@?92@?100@?108q116@?124"
- "⚔️  Scheduling conflict resolution for item %s.."

```
