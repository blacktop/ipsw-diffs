## PhotoLibraryServicesCore

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore`

```diff

-760.6.150.0.0
-  __TEXT.__text: 0xc4e54
-  __TEXT.__auth_stubs: 0x1c80
-  __TEXT.__objc_methlist: 0x7e74
-  __TEXT.__const: 0x249c
-  __TEXT.__cstring: 0x141f9
+800.14.111.0.0
+  __TEXT.__text: 0xc4a48
+  __TEXT.__auth_stubs: 0x1c40
+  __TEXT.__objc_methlist: 0x7d44
+  __TEXT.__const: 0x2404
+  __TEXT.__cstring: 0x14513
   __TEXT.__dlopen_cstrs: 0x19c
-  __TEXT.__gcc_except_tab: 0x71d4
-  __TEXT.__oslogstring: 0x9e09
-  __TEXT.__unwind_info: 0x3078
-  __TEXT.__objc_classname: 0x1100
-  __TEXT.__objc_methname: 0x15499
-  __TEXT.__objc_methtype: 0x4c92
-  __TEXT.__objc_stubs: 0xbb00
-  __DATA_CONST.__got: 0xab0
-  __DATA_CONST.__const: 0x39d0
-  __DATA_CONST.__objc_classlist: 0x418
+  __TEXT.__gcc_except_tab: 0x71f0
+  __TEXT.__oslogstring: 0x9ece
+  __TEXT.__ustring: 0x4
+  __TEXT.__unwind_info: 0x2fd8
+  __TEXT.__objc_classname: 0x10e7
+  __TEXT.__objc_methname: 0x150ff
+  __TEXT.__objc_methtype: 0x4a98
+  __TEXT.__objc_stubs: 0xb920
+  __DATA_CONST.__got: 0xa40
+  __DATA_CONST.__const: 0x3a68
+  __DATA_CONST.__objc_classlist: 0x410
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x49c0
+  __DATA_CONST.__objc_selrefs: 0x4938
   __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x278
+  __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__objc_arraydata: 0x408
-  __AUTH_CONST.__auth_got: 0xe50
-  __AUTH_CONST.__const: 0x3310
-  __AUTH_CONST.__cfstring: 0x10de0
-  __AUTH_CONST.__objc_const: 0xaa40
+  __AUTH_CONST.__auth_got: 0xe30
+  __AUTH_CONST.__const: 0x3238
+  __AUTH_CONST.__cfstring: 0x10f80
+  __AUTH_CONST.__objc_const: 0xa830
   __AUTH_CONST.__objc_intobj: 0x960
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x240
-  __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x678
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0x658
   __DATA.__data: 0x1080
-  __DATA.__bss: 0xba8
+  __DATA.__bss: 0xb98
   __DATA_DIRTY.__objc_data: 0x2580
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x548
+  __DATA_DIRTY.__bss: 0x500
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 0572DA7B-CDE2-353D-80F9-81DFDE683FC9
-  Functions: 3736
-  Symbols:   12877
+  UUID: 6754E7A4-B6D0-3F50-B936-41ED45799EB2
+  Functions: 3717
+  Symbols:   12785
   CStrings:  9311
 
Symbols:
+ +[PLFileUtilities createDirectoryAtURL:error:]
+ +[PLFileUtilities createDirectoryAtURL:error:usingFileManager:]
+ +[PLFileUtilities realPathsFromPaths:includeUnresolved:]
+ +[PLFileUtilities subpathWithLast:pathComponentsFromURL:]
+ +[PLFormatChooser _desiredImageSizeForRequestedViewSizeInPixels:]
+ +[PLSecurity clientIsAllowedToFetchCollectionShares]
+ +[PLValidatedSavedAssetType _maskForCollectionShareMutatingFrom]
+ +[PLValidatedSavedAssetType _maskForCollectionShareMutatingTo]
+ +[PLValidatedSavedAssetType executeBlockForSavedAssetType:unknown:photoBooth:photoStream:camera:cloudShared:cameraConnectionKit:cloudPhotoLibrary:wallpaper_UNUSED:momentShared:placeholder:referenced:alternate:guest:companionSynced:recovered:legacyImport:collectionShare:unrecognized:]
+ +[PLValidatedSavedAssetType mapSavedAssetType:unknown:photoBooth:photoStream:camera:cloudShared:cameraConnectionKit:cloudPhotoLibrary:wallpaper_UNUSED:momentShared:placeholder:referenced:alternate:guest:companionSynced:recovered:legacyImport:collectionShare:unrecognized:]
+ +[PLValidatedSavedAssetType maskForAllowedForSceneAnalysis]
+ +[PLValidatedSavedAssetType maskForAssetsEligibleForCPLSharingScopes]
+ +[PLValidatedSavedAssetType maskForAssetsEligibleForCPLTransportWithoutSharedScopesAndPlaceholders]
+ +[PLValidatedSavedAssetType maskForAssetsEligibleForCollectionShareRelationship]
+ +[PLValidatedSavedAssetType maskForCollectionShareAsset]
+ +[PLValidatedSavedAssetType savedAssetTypeForCollectionShareAsset]
+ +[PLValidatedSavedAssetType validatedSavedAssetTypeMaskUnknown:photoBooth:photoStream:camera:cloudShared:cameraConnectionKit:cloudPhotoLibrary:wallpaper_UNUSED:momentShared:placeholder:referenced:alternate:guest:companionSynced:recovered:collectionShare:legacyImport:]
+ -[PLAssetsdCloudInternalClient declineCollectionShareWithUUID:completionHandler:]
+ -[PLAssetsdCloudInternalClient reportInvitationAsSpamForCollectionShareWithUUID:completionHandler:]
+ -[PLAssetsdCloudInternalClient sendInvitationsForCollectionShareWithUUID:participantUUIDs:completionHandler:]
+ -[PLAssetsdDebugClient clearSensitivityStateForAssetsWithUUIDs:error:]
+ -[PLAssetsdLibraryInternalClient _getLibrarySizesFromDB:completionHandler:]
+ -[PLAssetsdLibraryInternalClient _inProcess_getLibrarySizesFromDB:handler:]
+ -[PLAssetsdLibraryInternalClient _librarySizesQueue]
+ -[PLAssetsdLibraryInternalClient deleteAllInitialSuggestionsWithError:]
+ -[PLAssetsdLibraryInternalClient generateInitialSuggestionsWithStyleType:error:]
+ -[PLAssetsdLibraryInternalClient updateInitialSuggestionsWithIdentifiers:dateLastUsed:error:]
+ -[PLAssetsdNonBindingDebugClient allKnownLibraryPaths:]
+ -[PLAssetsdNonBindingDebugClient getStatus]
+ -[PLAssetsdNonBindingDebugClient libraryServicesStateByBundlePathWithCompletion:]
+ -[PLAssetsdPhotoKitClient cancelReservedCloudIdentifiers:error:]
+ -[PLAssetsdPhotoKitClient forceSyndicationIngestAsyncToDate:withCompletionHandler:]
+ -[PLAssetsdPhotoKitClient forceSyndicationIngestSyncToDate:error:]
+ -[PLAssetsdPhotoKitClient ingestItemWithCoreSpotlightUniqueIdentifier:bundleID:purgeUrgency:error:]
+ -[PLAssetsdPhotoKitClient photoLibraryIdentifierWithError:]
+ -[PLDeviceConfiguration initWithLogicalScreenSize:screenScale:deviceClass:supportsASTC:]
+ -[PLFormatChooser _derivativeFormatThatFitsSize:]
+ -[PLGatekeeperClient _inProcess_getLibrarySizesFromDB:handler:]
+ -[PLImageFormat(ResourceChoosing) _isAcceptableForDesiredImageSize:]
+ -[PLPhotoLibraryFileIdentifier customSuffix]
+ -[PLPhotoLibraryFileIdentifier initWithAssetUuid:bundleScope:uti:resourceVersion:resourceType:recipeID:originalFilename:customSuffix:]
+ -[PLPositionalImageTable readImageDataAtIndex:intoBuffer:bytesRead:imageWidth:imageHeight:imageDataWidth:imageDataHeight:startingOffset:bytesPerRow:uuidBytes:]
+ -[PLPositionalTable readDataAtIndex:intoBuffer:bytesRead:]
+ GCC_except_table1023
+ GCC_except_table1082
+ GCC_except_table1084
+ GCC_except_table1386
+ GCC_except_table1511
+ GCC_except_table1534
+ GCC_except_table1539
+ GCC_except_table1576
+ GCC_except_table1589
+ GCC_except_table1615
+ GCC_except_table1620
+ GCC_except_table1623
+ GCC_except_table1626
+ GCC_except_table1629
+ GCC_except_table1632
+ GCC_except_table1635
+ GCC_except_table1638
+ GCC_except_table1641
+ GCC_except_table1644
+ GCC_except_table1647
+ GCC_except_table1649
+ GCC_except_table1657
+ GCC_except_table1660
+ GCC_except_table1663
+ GCC_except_table1665
+ GCC_except_table1668
+ GCC_except_table1671
+ GCC_except_table1674
+ GCC_except_table1677
+ GCC_except_table1680
+ GCC_except_table1683
+ GCC_except_table1686
+ GCC_except_table1689
+ GCC_except_table1692
+ GCC_except_table1703
+ GCC_except_table1706
+ GCC_except_table1709
+ GCC_except_table1712
+ GCC_except_table1714
+ GCC_except_table1717
+ GCC_except_table1720
+ GCC_except_table1723
+ GCC_except_table1842
+ GCC_except_table1861
+ GCC_except_table1865
+ GCC_except_table2061
+ GCC_except_table2066
+ GCC_except_table2067
+ GCC_except_table2069
+ GCC_except_table2072
+ GCC_except_table2205
+ GCC_except_table2285
+ GCC_except_table2324
+ GCC_except_table2356
+ GCC_except_table2361
+ GCC_except_table2364
+ GCC_except_table2367
+ GCC_except_table2370
+ GCC_except_table2373
+ GCC_except_table2376
+ GCC_except_table2379
+ GCC_except_table2382
+ GCC_except_table2385
+ GCC_except_table2388
+ GCC_except_table2391
+ GCC_except_table2413
+ GCC_except_table2438
+ GCC_except_table2441
+ GCC_except_table2449
+ GCC_except_table2452
+ GCC_except_table2455
+ GCC_except_table2463
+ GCC_except_table2467
+ GCC_except_table2472
+ GCC_except_table2476
+ GCC_except_table2480
+ GCC_except_table2484
+ GCC_except_table2488
+ GCC_except_table2492
+ GCC_except_table2496
+ GCC_except_table2500
+ GCC_except_table2504
+ GCC_except_table2508
+ GCC_except_table2519
+ GCC_except_table2523
+ GCC_except_table2527
+ GCC_except_table2531
+ GCC_except_table2535
+ GCC_except_table2539
+ GCC_except_table2543
+ GCC_except_table2557
+ GCC_except_table2570
+ GCC_except_table2573
+ GCC_except_table2576
+ GCC_except_table2579
+ GCC_except_table2582
+ GCC_except_table2585
+ GCC_except_table2588
+ GCC_except_table2591
+ GCC_except_table2594
+ GCC_except_table2597
+ GCC_except_table2600
+ GCC_except_table2603
+ GCC_except_table2609
+ GCC_except_table2611
+ GCC_except_table2728
+ GCC_except_table2731
+ GCC_except_table2787
+ GCC_except_table2840
+ GCC_except_table2851
+ GCC_except_table2853
+ GCC_except_table2879
+ GCC_except_table3031
+ GCC_except_table3035
+ GCC_except_table3040
+ GCC_except_table3046
+ GCC_except_table3052
+ GCC_except_table3133
+ GCC_except_table3318
+ GCC_except_table3328
+ GCC_except_table3333
+ GCC_except_table3337
+ GCC_except_table3344
+ GCC_except_table3396
+ GCC_except_table3399
+ GCC_except_table3406
+ GCC_except_table3412
+ GCC_except_table3416
+ GCC_except_table3420
+ GCC_except_table3424
+ GCC_except_table3428
+ GCC_except_table3447
+ GCC_except_table3450
+ GCC_except_table3472
+ GCC_except_table3498
+ GCC_except_table3500
+ GCC_except_table3505
+ GCC_except_table3509
+ GCC_except_table3520
+ GCC_except_table3523
+ GCC_except_table3526
+ GCC_except_table3530
+ GCC_except_table3539
+ GCC_except_table3542
+ GCC_except_table3545
+ GCC_except_table3549
+ GCC_except_table3555
+ GCC_except_table3561
+ GCC_except_table3565
+ GCC_except_table3645
+ GCC_except_table3646
+ GCC_except_table3647
+ GCC_except_table3649
+ GCC_except_table3651
+ GCC_except_table3653
+ GCC_except_table3654
+ GCC_except_table3657
+ GCC_except_table3664
+ GCC_except_table3677
+ GCC_except_table3682
+ GCC_except_table3689
+ GCC_except_table3694
+ GCC_except_table491
+ GCC_except_table494
+ GCC_except_table497
+ GCC_except_table500
+ GCC_except_table504
+ GCC_except_table508
+ GCC_except_table511
+ GCC_except_table515
+ GCC_except_table519
+ GCC_except_table525
+ GCC_except_table528
+ GCC_except_table534
+ GCC_except_table537
+ GCC_except_table540
+ GCC_except_table548
+ GCC_except_table602
+ GCC_except_table661
+ GCC_except_table693
+ GCC_except_table698
+ GCC_except_table701
+ GCC_except_table704
+ GCC_except_table710
+ GCC_except_table713
+ GCC_except_table716
+ GCC_except_table719
+ GCC_except_table722
+ GCC_except_table723
+ GCC_except_table761
+ GCC_except_table764
+ GCC_except_table767
+ GCC_except_table770
+ GCC_except_table776
+ GCC_except_table779
+ GCC_except_table788
+ GCC_except_table791
+ GCC_except_table794
+ GCC_except_table797
+ GCC_except_table800
+ GCC_except_table804
+ GCC_except_table808
+ GCC_except_table811
+ GCC_except_table814
+ GCC_except_table817
+ GCC_except_table820
+ GCC_except_table823
+ GCC_except_table826
+ GCC_except_table829
+ GCC_except_table832
+ GCC_except_table835
+ GCC_except_table838
+ GCC_except_table841
+ GCC_except_table844
+ GCC_except_table847
+ GCC_except_table854
+ GCC_except_table857
+ GCC_except_table860
+ GCC_except_table863
+ GCC_except_table866
+ GCC_except_table871
+ GCC_except_table874
+ GCC_except_table877
+ GCC_except_table880
+ GCC_except_table883
+ GCC_except_table887
+ GCC_except_table891
+ GCC_except_table894
+ GCC_except_table897
+ GCC_except_table900
+ GCC_except_table903
+ GCC_except_table906
+ GCC_except_table908
+ GCC_except_table910
+ GCC_except_table940
+ GCC_except_table942
+ GCC_except_table988
+ _OBJC_IVAR_$_PLPhotoLibraryFileIdentifier._customSuffix
+ _OBJC_IVAR_$_PLPhotoLibraryPathManagerUBF._derivativesContextualVideoThumbnailsDirectory
+ _OBJC_IVAR_$_PLPhotoLibraryPathManagerUBF._scopesCollectionShareDirectory
+ _PFIsCamera
+ _PFIsPhotosAppAnyPlatform
+ _PFIsiOSPhotosApp
+ _PLBackendPerfTestGetLog
+ _PLBackendPerfTestGetLog.log
+ _PLBackendPerfTestGetLog.predicate
+ _PLCoreAnalyticsLibraryMigrateEventPersistentHistoryChangeCountKey
+ _PLCoreAnalyticsLibraryMigrateEventPersistentHistoryTransactionCountKey
+ _PLCoreAnalyticsLibrarySummaryIsExceedingiCPLQuotaKey
+ _PLCoreAnalyticsLibrarySummaryManualAlbumsCreatedByAppleCountKey
+ _PLCoreAnalyticsLibrarySummaryManualAlbumsCreatedByThirdPartiesCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLRemainingQuotaBytesKey
+ _PLCoreAnalyticsLibrarySummaryiCPLSyncSessionActivityMotionStateBlockedCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLSyncSessionConsoleModeBlockedCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLSyncSessionDASDoItNowUnBlockedCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLSyncSessionDeviceActivityBlockedCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLSyncSessionDeviceActivityEarlyThermalWarningBlockedCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLSyncSessionSignificantTransferBlockedCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLTotalPhotosStorageBytesKey
+ _PLCoreAnalyticsLibrarySummaryiCPLTotalStorageBytesKey
+ _PLFruitBasketBundleID
+ _PLIsAlchemistAllowed
+ _PLLibraryServicesOperationNamePrefetchSensitiveContentAnalysisPolicy
+ _PLPhotosApplicationSettingsDomain
+ _PLResourceAlchemistV2OneUpFilename
+ _PLResourceAlchemistV2WallpaperFilename
+ _PLResourceAlchemistV2Widget1x1Filename
+ _PLResourceAlchemistV2Widget1x2Filename
+ _PLResourcesDerivativesContextualVideoThumbnailsDirectoryName
+ _PLRunWithIncrementedAtomicInt32
+ _PLSearchBackendPSITokenizerGetLog
+ _PLSearchBackendPSITokenizerGetLog.log
+ _PLSearchBackendPSITokenizerGetLog.predicate
+ _PLSearchBackendThumbnailMapGetLog
+ _PLSearchBackendThumbnailMapGetLog.log
+ _PLSearchBackendThumbnailMapGetLog.predicate
+ _PLSharedCollectionsGetLog
+ _PLSharedCollectionsGetLog.log
+ _PLSharedCollectionsGetLog.predicate
+ _PL_gKTXFileIdentifier.11404
+ _PhotoKitAllowCollectionShareFetchEntitlement
+ _PhotoLibraryServicesEntitlementAllowPhotosMessagesAccess
+ __OBJC_$_PROP_LIST_PLPhotoLibraryPathManagerCore.644
+ ___100-[PLAssetsdCloudInternalClient getLibraryScopeStatusCountsForScopeWithIdentifier:completionHandler:]_block_invoke.122
+ ___100-[PLAssetsdCloudInternalClient getLibraryScopeStatusCountsForScopeWithIdentifier:completionHandler:]_block_invoke.123
+ ___104-[PLAssetsdResourceClient fileDescriptorForAssetURL:withAdjustments:fileExtension:fileDescriptor:error:]_block_invoke.53
+ ___105-[PLAssetsdResourceClient sandboxExtensionForFileSystemBookmark:bookmarkURL:sandboxExtensionToken:error:]_block_invoke.81
+ ___105-[PLAssetsdResourceClient saveAssetWithJobDictionary:imageSurface:previewImageSurface:completionHandler:]_block_invoke.16
+ ___105-[PLAssetsdResourceClient saveAssetWithJobDictionary:imageSurface:previewImageSurface:completionHandler:]_block_invoke.19
+ ___106-[PLAssetsdDebugClient privateDownloadCloudPhotoLibraryAsset:resourceType:highPriority:completionHandler:]_block_invoke.129
+ ___106-[PLAssetsdResourceClient adjustmentDataForAsset:networkAccessAllowed:trackCPLDownload:completionHandler:]_block_invoke.83
+ ___106-[PLAssetsdResourceClient adjustmentDataForAsset:networkAccessAllowed:trackCPLDownload:completionHandler:]_block_invoke.84
+ ___107-[PLAssetsdCloudInternalClient confirmAllRemainingOnboardingPreviewAssetsOnLibraryScope:completionHandler:]_block_invoke.128
+ ___107-[PLAssetsdCloudInternalClient confirmAllRemainingOnboardingPreviewAssetsOnLibraryScope:completionHandler:]_block_invoke.129
+ ___109-[PLAssetsdCloudInternalClient sendInvitationsForCollectionShareWithUUID:participantUUIDs:completionHandler:]_block_invoke
+ ___109-[PLAssetsdCloudInternalClient sendInvitationsForCollectionShareWithUUID:participantUUIDs:completionHandler:]_block_invoke.87
+ ___109-[PLAssetsdCloudInternalClient sendInvitationsForCollectionShareWithUUID:participantUUIDs:completionHandler:]_block_invoke.88
+ ___110-[PLAssetsdCloudInternalClient resetLocalOnlyLibraryScopesAndAllLibraryScopeAssetStatesWithCompletionHandler:]_block_invoke.130
+ ___110-[PLAssetsdCloudInternalClient resetLocalOnlyLibraryScopesAndAllLibraryScopeAssetStatesWithCompletionHandler:]_block_invoke.131
+ ___110-[PLAssetsdCloudInternalClient userViewedSharedLibraryParticipantAssetTrashNotificationWithCompletionHandler:]_block_invoke.114
+ ___110-[PLAssetsdCloudInternalClient userViewedSharedLibraryParticipantAssetTrashNotificationWithCompletionHandler:]_block_invoke.115
+ ___116-[PLAssetsdPhotoKitClient processUniversalSearchJITForCoreSpotlightUniqueIdentifier:bundleID:processingTypes:error:]_block_invoke.29
+ ___117-[PLAssetsdCloudInternalClient startExitFromLibraryScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:]_block_invoke.102
+ ___117-[PLAssetsdCloudInternalClient startExitFromLibraryScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:]_block_invoke.103
+ ___120-[PLAssetsdDebugClient coalesceJournalsForManagerName:payloadClassIDs:withChangeJournalOverThreshold:completionHandler:]_block_invoke.140
+ ___120-[PLAssetsdDebugClient coalesceJournalsForManagerName:payloadClassIDs:withChangeJournalOverThreshold:completionHandler:]_block_invoke.141
+ ___128-[PLAssetsdCloudInternalClient markOnboardingPreviewAssetsByProcessingRulesOnLibraryScope:excludePersonUUIDs:completionHandler:]_block_invoke.127
+ ___130-[PLAssetsdResourceClient downloadCloudSharedAsset:withCloudPlaceholderKind:shouldPrioritize:shouldExtendTimer:completionHandler:]_block_invoke.101
+ ___130-[PLAssetsdResourceClient downloadCloudSharedAsset:withCloudPlaceholderKind:shouldPrioritize:shouldExtendTimer:completionHandler:]_block_invoke.102
+ ___131-[PLAssetsdResourceClient estimatedOutputFileLengthForVideoURL:fallbackFilePath:exportPreset:exportProperties:outFileLength:error:]_block_invoke.99
+ ___137-[PLAssetsdResourceClient imageDataForAsset:format:allowPlaceholder:wantURLOnly:networkAccessAllowed:trackCPLDownload:completionHandler:]_block_invoke.59
+ ___137-[PLAssetsdResourceClient imageDataForAsset:format:allowPlaceholder:wantURLOnly:networkAccessAllowed:trackCPLDownload:completionHandler:]_block_invoke.60
+ ___147-[PLAssetsdCloudInternalClient removeParticipantsWithParticipantUUIDs:fromLibraryScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:]_block_invoke.107
+ ___147-[PLAssetsdCloudInternalClient removeParticipantsWithParticipantUUIDs:fromLibraryScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:]_block_invoke.108
+ ___177-[PLAssetsdResourceClient imageDataForAsset:format:allowPlaceholder:wantURLOnly:networkAccessAllowed:trackCPLDownload:outImageData:outImageDataInfo:outCPLDownloadContext:error:]_block_invoke.57
+ ___40-[PLAssetsdDebugClient rebuildCloudFeed]_block_invoke.47
+ ___42-[PLAssetsdDebugClient rebuildTableThumbs]_block_invoke.58
+ ___43-[PLAssetsdNonBindingDebugClient getStatus]_block_invoke
+ ___43-[PLAssetsdNonBindingDebugClient getStatus]_block_invoke.7
+ ___44-[PLAssetsdDebugClient getCPLStateForDebug:]_block_invoke.69
+ ___46-[PLAssetsdCloudInternalClient getCPLSettings]_block_invoke.145
+ ___46-[PLAssetsdDebugClient momentGenerationStatus]_block_invoke.23
+ ___47-[PLAssetsdDebugClient getTaskConstraintStatus]_block_invoke.66
+ ___47-[PLAssetsdDebugClient getXPCTransactionStatus]_block_invoke.63
+ ___47-[PLAssetsdDebugClient waitForMomentGeneration]_block_invoke.157
+ ___49-[PLAssetsdDebugClient runMaintenanceTask:error:]_block_invoke.174
+ ___50-[PLAssetsdDebugClient prefetchResourcesWithMode:]_block_invoke.106
+ ___50-[PLAssetsdDebugClient pruneAssets:resourceTypes:]_block_invoke.93
+ ___51-[PLAssetsdDebugClient indexAssetsWithUUIDs:error:]_block_invoke.44
+ ___51-[PLAssetsdDebugClient resetComputeCacheWithError:]_block_invoke.150
+ ___52+[PLSecurity clientIsAllowedToFetchCollectionShares]_block_invoke
+ ___52-[PLAssetsdDebugClient computeCacheStatusWithError:]_block_invoke.151
+ ___52-[PLAssetsdDebugClient rebuildSearchIndexWithError:]_block_invoke.39
+ ___52-[PLAssetsdLibraryInternalClient _librarySizesQueue]_block_invoke
+ ___53-[PLAssetsdDebugClient archiveComputeCacheWithError:]_block_invoke.149
+ ___53-[PLAssetsdDebugClient backgroundMigrationWithError:]_block_invoke.162
+ ___53-[PLAssetsdDebugClient prefetchResourcesForMemories:]_block_invoke.98
+ ___53-[PLAssetsdDebugClient restoreComputeCacheWithError:]_block_invoke.148
+ ___54-[PLAssetsdCloudInternalClient setPrefetchMode:error:]_block_invoke.149
+ ___55-[PLAssetsdDebugClient prefetchResourcesForHighlights:]_block_invoke.103
+ ___55-[PLAssetsdDebugClient resetMaintenanceTasksWithError:]_block_invoke.171
+ ___55-[PLAssetsdDebugClient revertToOriginalForAsset:error:]_block_invoke.77
+ ___55-[PLAssetsdDebugClient updateHighlightTitlesWithError:]_block_invoke.114
+ ___55-[PLAssetsdNonBindingDebugClient allKnownLibraryPaths:]_block_invoke
+ ___55-[PLAssetsdNonBindingDebugClient allKnownLibraryPaths:]_block_invoke_2
+ ___55-[PLAssetsdResourceInternalClient cancelAllPrewarming:]_block_invoke.25
+ ___56-[PLAssetsdDebugClient cleanupEmptyHighlightsWithError:]_block_invoke.117
+ ___57-[PLAssetsdDebugClient processRecentHighlightsWithError:]_block_invoke.108
+ ___57-[PLAssetsdLibraryInternalClient getSearchIndexProgress:]_block_invoke.52
+ ___58-[PLAssetsdDebugClient locationOfInterestUpdateWithError:]_block_invoke.123
+ ___59-[PLAssetsdDebugClient removeAllThumbnailsForDryRun:count:]_block_invoke.54
+ ___59-[PLAssetsdPhotoKitClient photoLibraryIdentifierWithError:]_block_invoke
+ ___59-[PLAssetsdPhotoKitClient photoLibraryIdentifierWithError:]_block_invoke.39
+ ___60-[PLAssetsdCloudInternalClient getResetSyncStatusWithError:]_block_invoke.93
+ ___60-[PLAssetsdLibraryInternalClient failAvailabilityWithError:]_block_invoke.105
+ ___61-[PLAssetsdDebugClient dropSearchIndexWithCompletionHandler:]_block_invoke.33
+ ___61-[PLAssetsdDebugClient dropSearchIndexWithCompletionHandler:]_block_invoke.34
+ ___62-[PLAssetsdDebugClient closeSearchIndexWithCompletionHandler:]_block_invoke.37
+ ___62-[PLAssetsdDebugClient closeSearchIndexWithCompletionHandler:]_block_invoke.38
+ ___62-[PLAssetsdResourceClient addGroupWithName:completionHandler:]_block_invoke.23
+ ___62-[PLAssetsdResourceClient addGroupWithName:completionHandler:]_block_invoke.24
+ ___62-[PLAssetsdResourceClient projectExtensionDataForProjectUuid:]_block_invoke.122
+ ___63-[PLAssetsdLibraryInternalClient setKeywords:forAssetWithUUID:]_block_invoke.69
+ ___63-[PLAssetsdResourceClient consolidateAssets:completionHandler:]_block_invoke.110
+ ___63-[PLGatekeeperClient _inProcess_getLibrarySizesFromDB:handler:]_block_invoke
+ ___64-[PLAssetsdDebugClient resetBackgroundMigrationClassName:error:]_block_invoke.165
+ ___64-[PLAssetsdPhotoKitClient cancelReservedCloudIdentifiers:error:]_block_invoke
+ ___64-[PLAssetsdPhotoKitClient cancelReservedCloudIdentifiers:error:]_block_invoke.24
+ ___64-[PLAssetsdPhotoKitClient cancelReservedCloudIdentifiers:error:]_block_invoke_2
+ ___66-[PLAssetsdLibraryInternalClient clearAvailabilityStateWithError:]_block_invoke.104
+ ___66-[PLAssetsdPhotoKitClient forceSyndicationIngestSyncToDate:error:]_block_invoke
+ ___66-[PLAssetsdPhotoKitClient forceSyndicationIngestSyncToDate:error:]_block_invoke.33
+ ___67-[PLAssetsdDebugClient processUnprocessedMomentLocationsWithError:]_block_invoke.111
+ ___68-[PLAssetsdDebugClient rebuildMomentsDeletingExistingMoments:error:]_block_invoke.25
+ ___68-[PLAssetsdDebugClient updateAndSaveAssetPersonEdgesWithCompletion:]_block_invoke.147
+ ___69-[PLAssetsdLibraryInternalClient featureProcessingSnapshotWithError:]_block_invoke.102
+ ___70-[PLAssetsdDebugClient clearSensitivityStateForAssetsWithUUIDs:error:]_block_invoke
+ ___70-[PLAssetsdDebugClient clearSensitivityStateForAssetsWithUUIDs:error:]_block_invoke.126
+ ___70-[PLAssetsdLibraryInternalClient signalAvailabilityWithChanges:error:]_block_invoke.107
+ ___70-[PLAssetsdResourceClient updateInternalResourcePath:objectURI:error:]_block_invoke.118
+ ___71-[PLAssetsdCloudInternalClient activateLibraryScope:completionHandler:]_block_invoke.95
+ ___71-[PLAssetsdCloudInternalClient activateLibraryScope:completionHandler:]_block_invoke.96
+ ___71-[PLAssetsdCloudInternalClient isComputeSyncEnabledForDirection:reply:]_block_invoke.152
+ ___71-[PLAssetsdLibraryInternalClient availabilityStateShouldPersist:error:]_block_invoke.103
+ ___71-[PLAssetsdLibraryInternalClient deleteAllInitialSuggestionsWithError:]_block_invoke
+ ___71-[PLAssetsdLibraryInternalClient deleteAllInitialSuggestionsWithError:]_block_invoke.66
+ ___71-[PLAssetsdLibraryInternalClient waitForSearchIndexExistenceWithError:]_block_invoke.53
+ ___72-[PLAssetsdDebugClient syndicationIngestMutexStateDescriptionWithError:]_block_invoke.153
+ ___72-[PLAssetsdLibraryInternalClient getBackgroundJobServiceStateWithError:]_block_invoke.76
+ ___73-[PLAssetsdCloudInternalClient deactivateLibraryScope:completionHandler:]_block_invoke.100
+ ___73-[PLAssetsdCloudInternalClient deactivateLibraryScope:completionHandler:]_block_invoke.101
+ ___73-[PLAssetsdResourceInternalClient prewarmWithCapturePhotoSettings:error:]_block_invoke.21
+ ___74-[PLAssetsdDebugClient rebuildHighlightsDeletingExistingHighlights:error:]_block_invoke.26
+ ___74-[PLAssetsdLibraryInternalClient getLibrarySizesFromDB:completionHandler:]_block_invoke.5
+ ___74-[PLAssetsdPhotoKitClient analyzeAssets:forFeature:withCompletionHandler:]_block_invoke.36
+ ___74-[PLAssetsdPhotoKitClient analyzeLibraryForFeature:withCompletionHandler:]_block_invoke.37
+ ___75-[PLAssetsdDebugClient runAssetContainmentOnAllSocialGroupsWithCompletion:]_block_invoke.145
+ ___75-[PLAssetsdLibraryInternalClient _getLibrarySizesFromDB:completionHandler:]_block_invoke
+ ___75-[PLAssetsdLibraryInternalClient _getLibrarySizesFromDB:completionHandler:]_block_invoke_2
+ ___75-[PLAssetsdLibraryInternalClient _inProcess_getLibrarySizesFromDB:handler:]_block_invoke
+ ___75-[PLAssetsdLibraryInternalClient pauseSearchIndexingWithCompletionHandler:]_block_invoke.56
+ ___75-[PLAssetsdLibraryInternalClient pauseSearchIndexingWithCompletionHandler:]_block_invoke.57
+ ___76-[PLAssetsdCloudInternalClient sharedLibraryRampCheckWithCompletionHandler:]_block_invoke.112
+ ___76-[PLAssetsdCloudInternalClient sharedLibraryRampCheckWithCompletionHandler:]_block_invoke.113
+ ___76-[PLAssetsdLibraryInternalClient resumeSearchIndexingWithCompletionHandler:]_block_invoke.54
+ ___76-[PLAssetsdLibraryInternalClient resumeSearchIndexingWithCompletionHandler:]_block_invoke.55
+ ___76-[PLAssetsdLibraryInternalClient signalAvailabilityStateDidChangeWithError:]_block_invoke.106
+ ___76-[PLAssetsdResourceClient fileURLForAssetURL:withAdjustments:fileURL:error:]_block_invoke.45
+ ___76-[PLAssetsdResourceInternalClient cancelAllPrewarmingWithCompletionHandler:]_block_invoke.28
+ ___77-[PLAssetsdResourceClient addAssetWithURL:toAlbumWithUUID:completionHandler:]_block_invoke.35
+ ___77-[PLAssetsdResourceClient addAssetWithURL:toAlbumWithUUID:completionHandler:]_block_invoke.36
+ ___80-[PLAssetsdCloudInternalClient getCPLConfigrationValueForKey:completionHandler:]_block_invoke.142
+ ___80-[PLAssetsdDebugClient debugSidecarFileURLsForAsset:debugSidecarFileURLs:error:]_block_invoke.84
+ ___80-[PLAssetsdDebugClient runAssetContainmentOnSocialGroupWithUUID:withCompletion:]_block_invoke.146
+ ___80-[PLAssetsdLibraryInternalClient generateInitialSuggestionsWithStyleType:error:]_block_invoke
+ ___80-[PLAssetsdLibraryInternalClient generateInitialSuggestionsWithStyleType:error:]_block_invoke.60
+ ___81-[PLAssetsdCloudInternalClient declineCollectionShareWithUUID:completionHandler:]_block_invoke
+ ___81-[PLAssetsdCloudInternalClient declineCollectionShareWithUUID:completionHandler:]_block_invoke.83
+ ___81-[PLAssetsdCloudInternalClient declineCollectionShareWithUUID:completionHandler:]_block_invoke.84
+ ___81-[PLAssetsdDebugClient requestSearchDebugInformationForAssetUUID:redacted:error:]_block_invoke.43
+ ___81-[PLAssetsdDebugClient unloadImageFilesForAsset:minimumFormat:completionHandler:]_block_invoke.15
+ ___81-[PLAssetsdLibraryInternalClient deleteiTunesSyncedContentWithCompletionHandler:]_block_invoke.81
+ ___81-[PLAssetsdNonBindingDebugClient libraryServicesStateByBundlePathWithCompletion:]_block_invoke
+ ___81-[PLAssetsdNonBindingDebugClient libraryServicesStateByBundlePathWithCompletion:]_block_invoke.17
+ ___81-[PLAssetsdNonBindingDebugClient libraryServicesStateByBundlePathWithCompletion:]_block_invoke.20
+ ___82-[PLAssetsdDebugClient allMomentsMetadataWithOutputPath:metadataDictionary:error:]_block_invoke.32
+ ___83-[PLAssetsdLibraryInternalClient checkAssetsArePendingForDuplicateMergeProcessing:]_block_invoke.99
+ ___83-[PLAssetsdLibraryInternalClient getBackgroundJobServiceStatusCenterDumpWithError:]_block_invoke.78
+ ___83-[PLAssetsdPhotoKitClient forceSyndicationIngestAsyncToDate:withCompletionHandler:]_block_invoke
+ ___83-[PLAssetsdPhotoKitClient forceSyndicationIngestAsyncToDate:withCompletionHandler:]_block_invoke.35
+ ___83-[PLAssetsdPhotoKitClient getUUIDsForAssetObjectIDs:filterPredicate:context:error:]_block_invoke.25
+ ___83-[PLAssetsdPhotoKitClient getUUIDsForAssetObjectIDs:filterPredicate:context:error:]_block_invoke.27
+ ___84-[PLAssetsdCloudInternalClient refreshLibraryScopeWithIdentifier:completionHandler:]_block_invoke.119
+ ___84-[PLAssetsdCloudInternalClient refreshLibraryScopeWithIdentifier:completionHandler:]_block_invoke.120
+ ___84-[PLAssetsdDebugClient resetDrawAssetPersonEdgesBackgroundMigrationActionWithError:]_block_invoke.168
+ ___84-[PLAssetsdLibraryInternalClient invalidateReverseLocationDataOnAllAssetsWithError:]_block_invoke.71
+ ___85-[PLAssetsdDebugClient dumpMetadataForMomentsWithOutputPath:metadataDirectory:error:]_block_invoke.27
+ ___85-[PLAssetsdLibraryInternalClient processIdenticalDuplicatesWithProcessingType:error:]_block_invoke.96
+ ___85-[PLAssetsdResourceInternalClient prewarmWithCapturePhotoSettings:completionHandler:]_block_invoke.23
+ ___85-[PLAssetsdResourceInternalClient prewarmWithCapturePhotoSettings:completionHandler:]_block_invoke.24
+ ___87-[PLAssetsdPhotoKitClient processUniversalSearchJITForAssetUUID:processingTypes:error:]_block_invoke.31
+ ___88-[PLAssetsdCloudInternalClient forceParticipantAssetTrashNotificationCompletionHandler:]_block_invoke.116
+ ___88-[PLAssetsdCloudInternalClient forceParticipantAssetTrashNotificationCompletionHandler:]_block_invoke.117
+ ___88-[PLAssetsdResourceInternalClient batchSaveAssetsWithJobDictionaries:completionHandler:]_block_invoke.11
+ ___88-[PLAssetsdResourceInternalClient requestMasterThumbnailForAssetUUID:completionHandler:]_block_invoke.16
+ ___90-[PLAssetsdCloudInternalClient requestDeviceLibraryConfigurationChange:completionHandler:]_block_invoke.132
+ ___90-[PLAssetsdCloudInternalClient requestDeviceLibraryConfigurationChange:completionHandler:]_block_invoke.133
+ ___90-[PLAssetsdDebugClient invalidateHighlightSubtitlesAndRegenerateHighlightTitlesWithError:]_block_invoke.120
+ ___90-[PLAssetsdResourceClient sandboxExtensionsForAssetWithUUID:sandboxExtensionTokens:error:]_block_invoke.70
+ ___91-[PLAssetsdCloudInternalClient queryParticipantsWithEmails:phoneNumbers:completionHandler:]_block_invoke.90
+ ___91-[PLAssetsdCloudInternalClient queryParticipantsWithEmails:phoneNumbers:completionHandler:]_block_invoke.91
+ ___91-[PLAssetsdLibraryInternalClient getBackgroundJobServiceBundlesInQueueDictionaryWithError:]_block_invoke.80
+ ___92-[PLAssetsdPhotoKitClient resetStateForMediaProcessingTaskID:assetUUIDs:resetOptions:error:]_block_invoke.38
+ ___92-[PLAssetsdResourceClient sandboxExtensionFileURLForAssetURL:withAdjustments:fileURL:error:]_block_invoke.47
+ ___93-[PLAssetsdDebugClient snapshotJournalsForManagerName:payloadClassIDs:withCompletionHandler:]_block_invoke.135
+ ___93-[PLAssetsdDebugClient snapshotJournalsForManagerName:payloadClassIDs:withCompletionHandler:]_block_invoke.136
+ ___93-[PLAssetsdLibraryInternalClient registerBackgroundJobServiceIfNecessaryOnLibraryPath:error:]_block_invoke.75
+ ___93-[PLAssetsdLibraryInternalClient updateInitialSuggestionsWithIdentifiers:dateLastUsed:error:]_block_invoke
+ ___93-[PLAssetsdLibraryInternalClient updateInitialSuggestionsWithIdentifiers:dateLastUsed:error:]_block_invoke.63
+ ___95-[PLAssetsdCloudInternalClient markResourcesPurgeableWithUrgency:assetUuids:completionHandler:]_block_invoke.138
+ ___99-[PLAssetsdCloudInternalClient reportInvitationAsSpamForCollectionShareWithUUID:completionHandler:]_block_invoke
+ ___99-[PLAssetsdCloudInternalClient reportInvitationAsSpamForCollectionShareWithUUID:completionHandler:]_block_invoke.85
+ ___99-[PLAssetsdCloudInternalClient reportInvitationAsSpamForCollectionShareWithUUID:completionHandler:]_block_invoke.86
+ ___99-[PLAssetsdPhotoKitClient ingestItemWithCoreSpotlightUniqueIdentifier:bundleID:purgeUrgency:error:]_block_invoke
+ ___99-[PLAssetsdPhotoKitClient ingestItemWithCoreSpotlightUniqueIdentifier:bundleID:purgeUrgency:error:]_block_invoke.32
+ ___ALGetLibrarySizes_block_invoke_4
+ ___Block_byref_object_copy_.10934
+ ___Block_byref_object_copy_.11472
+ ___Block_byref_object_copy_.11629
+ ___Block_byref_object_copy_.11681
+ ___Block_byref_object_copy_.11728
+ ___Block_byref_object_copy_.11781
+ ___Block_byref_object_copy_.12005
+ ___Block_byref_object_copy_.12672
+ ___Block_byref_object_copy_.12725
+ ___Block_byref_object_copy_.1519
+ ___Block_byref_object_copy_.1633
+ ___Block_byref_object_copy_.1898
+ ___Block_byref_object_copy_.3184
+ ___Block_byref_object_copy_.3386
+ ___Block_byref_object_copy_.3547
+ ___Block_byref_object_copy_.3753
+ ___Block_byref_object_copy_.4838
+ ___Block_byref_object_copy_.5444
+ ___Block_byref_object_copy_.5706
+ ___Block_byref_object_copy_.6003
+ ___Block_byref_object_copy_.6326
+ ___Block_byref_object_copy_.6518
+ ___Block_byref_object_copy_.7011
+ ___Block_byref_object_copy_.7856
+ ___Block_byref_object_copy_.8884
+ ___Block_byref_object_copy_.982
+ ___Block_byref_object_dispose_.10935
+ ___Block_byref_object_dispose_.11473
+ ___Block_byref_object_dispose_.11630
+ ___Block_byref_object_dispose_.11682
+ ___Block_byref_object_dispose_.11729
+ ___Block_byref_object_dispose_.11782
+ ___Block_byref_object_dispose_.12006
+ ___Block_byref_object_dispose_.12673
+ ___Block_byref_object_dispose_.12726
+ ___Block_byref_object_dispose_.1520
+ ___Block_byref_object_dispose_.1634
+ ___Block_byref_object_dispose_.1899
+ ___Block_byref_object_dispose_.3185
+ ___Block_byref_object_dispose_.3387
+ ___Block_byref_object_dispose_.3548
+ ___Block_byref_object_dispose_.3754
+ ___Block_byref_object_dispose_.4839
+ ___Block_byref_object_dispose_.5445
+ ___Block_byref_object_dispose_.5707
+ ___Block_byref_object_dispose_.6004
+ ___Block_byref_object_dispose_.6327
+ ___Block_byref_object_dispose_.6519
+ ___Block_byref_object_dispose_.7012
+ ___Block_byref_object_dispose_.7857
+ ___Block_byref_object_dispose_.8885
+ ___Block_byref_object_dispose_.983
+ ___PLBackendPerfTestGetLog_block_invoke
+ ___PLSearchBackendPSITokenizerGetLog_block_invoke
+ ___PLSearchBackendThumbnailMapGetLog_block_invoke
+ ___PLSharedCollectionsGetLog_block_invoke
+ ____create5551BGRACGImageFromImageData_block_invoke
+ ___block_descriptor_40_e12_v24?0^v8Q16l
+ ___block_descriptor_48_e8_32r40r_e46_v24?0"PLPhotoLibraryIdentifier"8"NSError"16lr32l8r40l8
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e37_v28?0B8"NSDictionary"12"NSError"20ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e25_v32?0"NSString"8Q16^B24ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40s48r56r_e30_v24?0"NSString"8"NSError"16ls32l8s40l8r48l8r56l8
+ ___block_descriptor_96_e8_32bs40n18_8_8_t0w1_s8_t16w32_e51_v16?0"<PLAssetsdNonBindingDebugServiceProtocol>"8l
+ ___block_literal_global.100.1910
+ ___block_literal_global.102.2591
+ ___block_literal_global.105.2596
+ ___block_literal_global.10643
+ ___block_literal_global.1085
+ ___block_literal_global.10940
+ ___block_literal_global.110
+ ___block_literal_global.111.2600
+ ___block_literal_global.11173
+ ___block_literal_global.11272
+ ___block_literal_global.11384
+ ___block_literal_global.11783
+ ___block_literal_global.119
+ ___block_literal_global.11986
+ ___block_literal_global.12.2547
+ ___block_literal_global.122
+ ___block_literal_global.12371
+ ___block_literal_global.125
+ ___block_literal_global.1251
+ ___block_literal_global.126.6016
+ ___block_literal_global.1266
+ ___block_literal_global.128
+ ___block_literal_global.129.3933
+ ___block_literal_global.13
+ ___block_literal_global.134
+ ___block_literal_global.134.3944
+ ___block_literal_global.139
+ ___block_literal_global.1402
+ ___block_literal_global.144.6007
+ ___block_literal_global.148
+ ___block_literal_global.148.6005
+ ___block_literal_global.151
+ ___block_literal_global.151.5998
+ ___block_literal_global.153.3961
+ ___block_literal_global.156.2618
+ ___block_literal_global.159.2621
+ ___block_literal_global.16.6166
+ ___block_literal_global.161
+ ___block_literal_global.161.3970
+ ___block_literal_global.164
+ ___block_literal_global.164.11844
+ ___block_literal_global.167
+ ___block_literal_global.1685
+ ___block_literal_global.171.3978
+ ___block_literal_global.176
+ ___block_literal_global.18.2553
+ ___block_literal_global.182
+ ___block_literal_global.186.3992
+ ___block_literal_global.191
+ ___block_literal_global.192.6414
+ ___block_literal_global.197
+ ___block_literal_global.1986
+ ___block_literal_global.2.6194
+ ___block_literal_global.20.1980
+ ___block_literal_global.20.6162
+ ___block_literal_global.2005
+ ___block_literal_global.201.6407
+ ___block_literal_global.209
+ ___block_literal_global.219.4013
+ ___block_literal_global.22.1974
+ ___block_literal_global.222.4017
+ ___block_literal_global.230
+ ___block_literal_global.233
+ ___block_literal_global.235
+ ___block_literal_global.237.4028
+ ___block_literal_global.24.6156
+ ___block_literal_global.253
+ ___block_literal_global.2539
+ ___block_literal_global.258.4036
+ ___block_literal_global.27.10929
+ ___block_literal_global.27.6150
+ ___block_literal_global.277
+ ___block_literal_global.279.10614
+ ___block_literal_global.285.4044
+ ___block_literal_global.294.4047
+ ___block_literal_global.297
+ ___block_literal_global.30.6144
+ ___block_literal_global.301
+ ___block_literal_global.305
+ ___block_literal_global.309
+ ___block_literal_global.313
+ ___block_literal_global.317
+ ___block_literal_global.3207
+ ___block_literal_global.3318
+ ___block_literal_global.3400
+ ___block_literal_global.3453
+ ___block_literal_global.3688
+ ___block_literal_global.374
+ ___block_literal_global.379
+ ___block_literal_global.3923
+ ___block_literal_global.396.2703
+ ___block_literal_global.402
+ ___block_literal_global.405
+ ___block_literal_global.408
+ ___block_literal_global.4167
+ ___block_literal_global.42.2565
+ ___block_literal_global.42.6120
+ ___block_literal_global.45.3658
+ ___block_literal_global.46.1933
+ ___block_literal_global.48.6116
+ ___block_literal_global.483
+ ___block_literal_global.49.1934
+ ___block_literal_global.50.6108
+ ___block_literal_global.5014
+ ___block_literal_global.51.2569
+ ___block_literal_global.51.3643
+ ___block_literal_global.531
+ ___block_literal_global.536
+ ___block_literal_global.5652
+ ___block_literal_global.57.2573
+ ___block_literal_global.5700
+ ___block_literal_global.59
+ ___block_literal_global.6.1072
+ ___block_literal_global.6.2543
+ ___block_literal_global.6.6576
+ ___block_literal_global.60.2576
+ ___block_literal_global.62.3626
+ ___block_literal_global.6205
+ ___block_literal_global.6321
+ ___block_literal_global.640
+ ___block_literal_global.6446
+ ___block_literal_global.65.12369
+ ___block_literal_global.65.3623
+ ___block_literal_global.6586
+ ___block_literal_global.666
+ ___block_literal_global.6673
+ ___block_literal_global.68.3619
+ ___block_literal_global.7016
+ ___block_literal_global.73.7616
+ ___block_literal_global.737
+ ___block_literal_global.75.2581
+ ___block_literal_global.7642
+ ___block_literal_global.7851
+ ___block_literal_global.8507
+ ___block_literal_global.8830
+ ___block_literal_global.8886
+ ___block_literal_global.9.11273
+ ___block_literal_global.9.6577
+ ___block_literal_global.92.1912
+ ___block_literal_global.93.3573
+ ___block_literal_global.93.6304
+ ___block_literal_global.95
+ ___block_literal_global.95.3569
+ ___block_literal_global.9514
+ ___block_literal_global.97
+ ___block_literal_global.98
+ ___pl_dispatch_on_main_queue_after_block_invoke
+ __create5551BGRACGImageFromImageData.s_colorSpace
+ __create5551BGRACGImageFromImageData.s_onceToken
+ __dispatch_main_q
+ __librarySizesQueue.onceToken
+ __librarySizesQueue.sLibrarySizesQueue
+ _allPhotosPathsOnThisDevice.bundlePaths.2415
+ _allPhotosPathsOnThisDevice.onceToken.2414
+ _clientIsAllowedToFetchCollectionShares.collectionShareFetchAllowed
+ _clientIsAllowedToFetchCollectionShares.onceToken
+ _kPLImageWriterSharingRestriction
+ _objc_msgSend$_derivativeFormatThatFitsSize:
+ _objc_msgSend$_desiredImageSizeForRequestedViewSizeInPixels:
+ _objc_msgSend$_getLibrarySizesFromDB:completionHandler:
+ _objc_msgSend$_inProcess_getLibrarySizesFromDB:handler:
+ _objc_msgSend$_isAcceptableForDesiredImageSize:
+ _objc_msgSend$_librarySizesQueue
+ _objc_msgSend$_maskForCollectionShareMutatingFrom
+ _objc_msgSend$_maskForCollectionShareMutatingTo
+ _objc_msgSend$_setError
+ _objc_msgSend$cancelReservedCloudIdentifiers:reply:
+ _objc_msgSend$clearSensitivityStateForAssetsWithUUIDs:reply:
+ _objc_msgSend$createDirectoryAtURL:error:usingFileManager:
+ _objc_msgSend$customSuffix
+ _objc_msgSend$declineCollectionShareWithUUID:reply:
+ _objc_msgSend$deleteAllInitialSuggestionsWithReply:
+ _objc_msgSend$forceSyndicationIngestAsyncToDate:reply:
+ _objc_msgSend$generateInitialSuggestionsWithStyleType:reply:
+ _objc_msgSend$getAllKnownLibraryPathsWithReply:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$getLibraryServicesStateByLibraryBundleWithReply:
+ _objc_msgSend$getLibrarySizesFromDB:error:
+ _objc_msgSend$getLibrarySizesFromDB:handler:
+ _objc_msgSend$getPhotoLibraryIdentifierWithReply:
+ _objc_msgSend$hasError
+ _objc_msgSend$ingestItemWithCoreSpotlightUniqueIdentifier:bundleID:purgeUrgency:reply:
+ _objc_msgSend$initWithAssetUuid:bundleScope:uti:resourceVersion:resourceType:recipeID:originalFilename:customSuffix:
+ _objc_msgSend$initWithLogicalScreenSize:screenScale:deviceClass:supportsASTC:
+ _objc_msgSend$openAndWaitWithUpgrade:error:
+ _objc_msgSend$photosMessagesEntitled
+ _objc_msgSend$position
+ _objc_msgSend$readDataAtIndex:intoBuffer:bytesRead:
+ _objc_msgSend$readImageDataAtIndex:intoBuffer:bytesRead:imageWidth:imageHeight:imageDataWidth:imageDataHeight:startingOffset:bytesPerRow:uuidBytes:
+ _objc_msgSend$reportInvitationAsSpamForCollectionShareWithUUID:reply:
+ _objc_msgSend$sendInvitationsForCollectionShareWithUUID:participantUUIDs:reply:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$systemPhotoLibraryURL
+ _objc_msgSend$updateInitialSuggestionsWithIdentifiers:dateLastUsed:reply:
+ _objc_msgSend$validatedSavedAssetTypeMaskUnknown:photoBooth:photoStream:camera:cloudShared:cameraConnectionKit:cloudPhotoLibrary:wallpaper_UNUSED:momentShared:placeholder:referenced:alternate:guest:companionSynced:recovered:collectionShare:legacyImport:
+ _pl_dispatch_on_main_queue
+ _pl_dispatch_on_main_queue_after
+ _sharedInstance.onceToken.8829
- +[NSKeyedUnarchiver(PLKeyedUnarchiverAdditions) pl_safeUnarchiveObjectFromFile:class:]
- +[NSKeyedUnarchiver(PLKeyedUnarchiverAdditions) pl_safeUnarchiveObjectFromFile:classes:]
- +[PLDiskController sharedInstance]
- +[PLFileUtilities hasDiskSpaceToCopyFileAtURL:toVolumeAtURL:error:]
- +[PLFormatChooser _desiredImageSizeForRequestedViewSizeInPixels:isAspectFill:srcAspectRatio:]
- +[PLImportFileManager isCameraDirectoryFolderName:]
- +[PLImportFileManager isImportDirectoryFolderName:]
- +[PLLibraryServicesOperation operationWithName:libraryServicesManager:requiredState:parentProgress:executionBlock:]
- +[PLLibraryServicesOperation setShouldSuppressLogging:]
- +[PLLibraryServicesOperation shouldSuppressLogging]
- +[PLValidatedSavedAssetType executeBlockForSavedAssetType:unknown:photoBooth:photoStream:camera:cloudShared:cameraConnectionKit:cloudPhotoLibrary:wallpaper_UNUSED:momentShared:placeholder:referenced:alternate:guest:companionSynced:recovered:legacyImport:unrecognized:]
- +[PLValidatedSavedAssetType mapSavedAssetType:unknown:photoBooth:photoStream:camera:cloudShared:cameraConnectionKit:cloudPhotoLibrary:wallpaper_UNUSED:momentShared:placeholder:referenced:alternate:guest:companionSynced:recovered:legacyImport:unrecognized:]
- +[PLValidatedSavedAssetType maskForAssetsEligibleForCloudKitTransportWithoutMomentSharesAndPlaceholders]
- +[PLValidatedSavedAssetType maskForMomentShareDeDupe]
- +[PLValidatedSavedAssetType validatedSavedAssetTypeMaskUnknown:photoBooth:photoStream:camera:cloudShared:cameraConnectionKit:cloudPhotoLibrary:wallpaper_UNUSED:momentShared:placeholder:referenced:alternate:guest:companionSynced:recovered:legacyImport:]
- -[PLAssetsdCloudInternalClient runComputeSyncBackfillMigrationSynchronously]
- -[PLAssetsdDebugClient assetContainmentLargeFaceThresholdUserDefaultWithError:]
- -[PLAssetsdDebugClient assetContainmentSmallFaceThresholdUserDefaultWithError:]
- -[PLAssetsdDebugClient assetContainmentSmallTorsoThresholdUserDefaultWithError:]
- -[PLAssetsdDebugClient getStatus]
- -[PLAssetsdDebugClient setAssetContainmentLargeFaceThreshold:error:]
- -[PLAssetsdDebugClient setAssetContainmentSmallFaceThreshold:error:]
- -[PLAssetsdDebugClient setAssetContainmentSmallTorsoThreshold:error:]
- -[PLAssetsdDebugClient synchronouslySetSearchIndexPaused:reason:error:]
- -[PLAssetsdLibraryInternalClient applySearchIndexGraphUpdates:supportingData:completionHandler:]
- -[PLAssetsdLibraryInternalClient deleteEmbeddings:assetUUID:completionHandler:]
- -[PLAssetsdLibraryInternalClient insertEmbeddings:modelType:assetUUID:completionHandler:]
- -[PLAssetsdLibraryInternalClient invalidateBehavioralScoreOnAllAssetsWithError:]
- -[PLAssetsdLibraryInternalClient synchronouslyGetLibrarySizesFromDB:sizes:error:]
- -[PLDeviceConfiguration initWithLogicalScreenSize:screenScale:deviceClass:supportsASTC:isMigrationService:]
- -[PLDeviceConfiguration isMigrationService]
- -[PLDeviceConfiguration setIsMigrationService:]
- -[PLDiskController _actuallyUpdateCookie]
- -[PLDiskController _diskSpaceDidBecomeLow]
- -[PLDiskController _updateCookie]
- -[PLDiskController bytesToAutomaticallyClear]
- -[PLDiskController dealloc]
- -[PLDiskController hasEnoughDiskToTakePicture]
- -[PLDiskController init]
- -[PLDiskController updateAvailableDiskSpace]
- -[PLFormatChooser _bestFormatWithSize:specificVersionType:contentMode:demoteFactor:srcAspectRatio:hasAdjustmentsHandler:desiredImagePixelSize:]
- -[PLFormatChooser _fastestDegradedFormatFallingBackFromFormat:]
- -[PLFormatChooser _nextLargestAcceptableFormatForFormat:]
- -[PLFormatChooser _standardDegradedFormatFallingBackFromFormat:]
- -[PLFormatChooser chooseFormatsForSize:specificVersionType:contentMode:demoteFactor:srcAspectRatio:degradedFormatPolicy:hasAdjustmentsHandler:desiredImagePixelSize:bestFormat:degradedFormat:]
- -[PLFormatChooser derivativeFormatThatFitsSize:contentMode:demoteFactor:srcAspectRatio:desiredImagePixelSize:]
- -[PLImageFormat(ResourceChoosing) _canDegradeToFormat:]
- -[PLImageFormat(ResourceChoosing) _isAcceptableForViewSize:contentMode:sourceAspectRatio:desiredImageSize:demoteFactor:]
- -[PLImportFileManager nextAvailableFilePathInDirectory:withExtension:]
- -[PLLibraryServicesOperation .cxx_destruct]
- -[PLLibraryServicesOperation _runOperationBlock:]
- -[PLLibraryServicesOperation debugDescription]
- -[PLLibraryServicesOperation logPrefix]
- -[PLLibraryServicesOperation progressPercentOfTotal]
- -[PLLibraryServicesOperation progress]
- -[PLLibraryServicesOperation requiredState]
- -[PLLibraryServicesOperation setExecutionBlockFromOperationBlock:]
- -[PLLibraryServicesOperation setLogPrefix:]
- -[PLLibraryServicesOperation setProgress:]
- -[PLLibraryServicesOperation setProgressPercentOfTotal:]
- -[PLLibraryServicesOperation setRequiredState:]
- -[PLLibraryServicesOperation statusDescription]
- -[PLPhotoLibraryFileIdentifier initWithAssetUuid:bundleScope:uti:resourceVersion:resourceType:recipeID:originalFilename:]
- -[PLPhotoLibraryFileIdentifier setOriginalFilename:]
- -[PLPositionalImageTable readImageDataAtIndex:intoPoolNode:bytesRead:imageWidth:imageHeight:imageDataWidth:imageDataHeight:startingOffset:bytesPerRow:uuidBytes:]
- -[PLPositionalTable pool]
- -[PLPositionalTable readDataAtIndex:intoPoolNode:bytesRead:]
- GCC_except_table1087
- GCC_except_table1088
- GCC_except_table1383
- GCC_except_table1530
- GCC_except_table1535
- GCC_except_table1571
- GCC_except_table1580
- GCC_except_table1600
- GCC_except_table1616
- GCC_except_table1621
- GCC_except_table1624
- GCC_except_table1627
- GCC_except_table1630
- GCC_except_table1633
- GCC_except_table1636
- GCC_except_table1639
- GCC_except_table1642
- GCC_except_table1645
- GCC_except_table1648
- GCC_except_table1656
- GCC_except_table1658
- GCC_except_table1661
- GCC_except_table1664
- GCC_except_table1667
- GCC_except_table1670
- GCC_except_table1673
- GCC_except_table1675
- GCC_except_table1678
- GCC_except_table1681
- GCC_except_table1684
- GCC_except_table1687
- GCC_except_table1690
- GCC_except_table1693
- GCC_except_table1704
- GCC_except_table1707
- GCC_except_table1710
- GCC_except_table1713
- GCC_except_table1716
- GCC_except_table1718
- GCC_except_table1721
- GCC_except_table1724
- GCC_except_table1727
- GCC_except_table1730
- GCC_except_table1855
- GCC_except_table1874
- GCC_except_table1878
- GCC_except_table2073
- GCC_except_table2078
- GCC_except_table2079
- GCC_except_table2081
- GCC_except_table2084
- GCC_except_table2211
- GCC_except_table2292
- GCC_except_table2331
- GCC_except_table2363
- GCC_except_table2368
- GCC_except_table2371
- GCC_except_table2374
- GCC_except_table2377
- GCC_except_table2380
- GCC_except_table2383
- GCC_except_table2386
- GCC_except_table2389
- GCC_except_table2392
- GCC_except_table2395
- GCC_except_table2398
- GCC_except_table2420
- GCC_except_table2443
- GCC_except_table2448
- GCC_except_table2453
- GCC_except_table2456
- GCC_except_table2462
- GCC_except_table2466
- GCC_except_table2474
- GCC_except_table2477
- GCC_except_table2479
- GCC_except_table2483
- GCC_except_table2487
- GCC_except_table2491
- GCC_except_table2495
- GCC_except_table2499
- GCC_except_table2503
- GCC_except_table2507
- GCC_except_table2518
- GCC_except_table2522
- GCC_except_table2526
- GCC_except_table2530
- GCC_except_table2534
- GCC_except_table2538
- GCC_except_table2542
- GCC_except_table2545
- GCC_except_table2553
- GCC_except_table2571
- GCC_except_table2574
- GCC_except_table2577
- GCC_except_table2580
- GCC_except_table2583
- GCC_except_table2586
- GCC_except_table2589
- GCC_except_table2592
- GCC_except_table2595
- GCC_except_table2598
- GCC_except_table2601
- GCC_except_table2604
- GCC_except_table2723
- GCC_except_table2726
- GCC_except_table2793
- GCC_except_table2846
- GCC_except_table2863
- GCC_except_table2865
- GCC_except_table2891
- GCC_except_table3038
- GCC_except_table3054
- GCC_except_table3057
- GCC_except_table3060
- GCC_except_table3092
- GCC_except_table3097
- GCC_except_table3158
- GCC_except_table3160
- GCC_except_table3171
- GCC_except_table3356
- GCC_except_table3366
- GCC_except_table3371
- GCC_except_table3375
- GCC_except_table3382
- GCC_except_table3435
- GCC_except_table3438
- GCC_except_table3445
- GCC_except_table3451
- GCC_except_table3455
- GCC_except_table3463
- GCC_except_table3467
- GCC_except_table3493
- GCC_except_table3502
- GCC_except_table3541
- GCC_except_table3543
- GCC_except_table3548
- GCC_except_table3563
- GCC_except_table3566
- GCC_except_table3573
- GCC_except_table3576
- GCC_except_table3588
- GCC_except_table3592
- GCC_except_table3595
- GCC_except_table3598
- GCC_except_table3601
- GCC_except_table3604
- GCC_except_table3608
- GCC_except_table3612
- GCC_except_table3625
- GCC_except_table3673
- GCC_except_table3699
- GCC_except_table3700
- GCC_except_table3701
- GCC_except_table3703
- GCC_except_table3705
- GCC_except_table3707
- GCC_except_table3708
- GCC_except_table3711
- GCC_except_table3718
- GCC_except_table492
- GCC_except_table495
- GCC_except_table499
- GCC_except_table503
- GCC_except_table509
- GCC_except_table512
- GCC_except_table518
- GCC_except_table521
- GCC_except_table524
- GCC_except_table532
- GCC_except_table588
- GCC_except_table647
- GCC_except_table679
- GCC_except_table684
- GCC_except_table687
- GCC_except_table690
- GCC_except_table696
- GCC_except_table699
- GCC_except_table702
- GCC_except_table705
- GCC_except_table708
- GCC_except_table709
- GCC_except_table742
- GCC_except_table747
- GCC_except_table750
- GCC_except_table753
- GCC_except_table762
- GCC_except_table765
- GCC_except_table768
- GCC_except_table771
- GCC_except_table774
- GCC_except_table777
- GCC_except_table780
- GCC_except_table787
- GCC_except_table790
- GCC_except_table792
- GCC_except_table795
- GCC_except_table798
- GCC_except_table801
- GCC_except_table805
- GCC_except_table809
- GCC_except_table812
- GCC_except_table815
- GCC_except_table818
- GCC_except_table821
- GCC_except_table824
- GCC_except_table827
- GCC_except_table830
- GCC_except_table833
- GCC_except_table836
- GCC_except_table839
- GCC_except_table842
- GCC_except_table845
- GCC_except_table848
- GCC_except_table855
- GCC_except_table858
- GCC_except_table861
- GCC_except_table864
- GCC_except_table867
- GCC_except_table872
- GCC_except_table875
- GCC_except_table878
- GCC_except_table881
- GCC_except_table884
- GCC_except_table888
- GCC_except_table892
- GCC_except_table895
- GCC_except_table898
- GCC_except_table901
- GCC_except_table904
- GCC_except_table907
- GCC_except_table909
- GCC_except_table911
- GCC_except_table914
- GCC_except_table944
- GCC_except_table946
- GCC_except_table992
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- OBJC_IVAR_$_PLDiskController._bytesRequiredForPhoto
- OBJC_IVAR_$_PLDiskController._flags
- OBJC_IVAR_$_PLDiskController._lastFSCheck
- _CFNotificationCenterGetDarwinNotifyCenter
- _CFNotificationCenterPostNotification
- _CFNotificationCenterRemoveObserver
- _DiskSpaceDidBecomeLow
- _NSFileSize
- _NSURLVolumeAvailableCapacityForImportantUsageKey
- _OBJC_CLASS_$_AVCapturePhotoOutput
- _OBJC_CLASS_$_NSBlockOperation
- _OBJC_CLASS_$_NSProgress
- _OBJC_CLASS_$_NSRegularExpression
- _OBJC_CLASS_$_PLLibraryServicesOperation
- _OBJC_IVAR_$_PLDeviceConfiguration._isMigrationService
- _OBJC_IVAR_$_PLLibraryServicesOperation._logPrefix
- _OBJC_IVAR_$_PLLibraryServicesOperation._progress
- _OBJC_IVAR_$_PLLibraryServicesOperation._progressPercentOfTotal
- _OBJC_IVAR_$_PLLibraryServicesOperation._requiredState
- _OBJC_IVAR_$_PLPhotoLibraryPathManagerDCIM._lockedDirectory
- _OBJC_IVAR_$_PLPhotoLibraryPathManagerUBF._scopesLockedDirectory
- _OBJC_IVAR_$_PLPositionalTable._pool
- _OBJC_METACLASS_$_NSBlockOperation
- _OBJC_METACLASS_$_PLLibraryServicesOperation
- _OSAtomicDequeue
- _OSAtomicEnqueue
- _PLGridInlinePlaybackGetLog
- _PLGridInlinePlaybackGetLog.log
- _PLGridInlinePlaybackGetLog.predicate
- _PLIsCamera.didCheck
- _PLIsCamera.isCamera
- _PLIsLockScreenCamera
- _PLIsLockScreenCamera.didCheck
- _PLIsLockScreenCamera.isCamera
- _PLIsMacPhotosApp
- _PLIsMobileSlideShow.didCheck
- _PLIsMobileSlideShow.isMobileslideshow
- _PLIsPhotoPicker
- _PLIsPhotoPicker.didCheck
- _PLIsPhotoPicker.isPhotoPicker
- _PLIsPhotosMessagesApp
- _PLIsPhotosMessagesApp.didCheck
- _PLIsPhotosMessagesApp.isPhotosMessagesApp
- _PLIsPreferences
- _PLIsPreferences.didCheck
- _PLIsPreferences.isPreferences
- _PLIsSpotlight
- _PLIsSpotlight.didCheck
- _PLIsSpotlight.isSpotlight
- _PLIsTVPhotosApp
- _PLIsTVPhotosApp.didCheck
- _PLIsTVPhotosApp.isTVPhotosApp
- _PLLibraryServicesOperationNameCrashRecoveryRepairInterruptedLockedResourceTransfer
- _PLLockedDirectoryName
- _PLPositionalTableMemoryPool_Alloc
- _PLPositionalTableMemoryPool_Create
- _PLPositionalTableMemoryPool_Destroy
- _PLPositionalTableMemoryPool_Free
- _PL_gKTXFileIdentifier.11648
- _UTTypePDF
- __OBJC_$_CLASS_METHODS_PLImportFileManager
- __OBJC_$_CLASS_METHODS_PLLibraryServicesOperation
- __OBJC_$_CLASS_PROP_LIST_PLLibraryServicesOperation
- __OBJC_$_INSTANCE_METHODS_PLDiskController
- __OBJC_$_INSTANCE_METHODS_PLLibraryServicesOperation
- __OBJC_$_INSTANCE_VARIABLES_PLDiskController
- __OBJC_$_INSTANCE_VARIABLES_PLLibraryServicesOperation
- __OBJC_$_PROP_LIST_PLLibraryServicesOperation
- __OBJC_$_PROP_LIST_PLPhotoLibraryPathManagerCore.641
- __OBJC_CLASS_RO_$_PLLibraryServicesOperation
- __OBJC_METACLASS_RO_$_PLLibraryServicesOperation
- ___100-[PLAssetsdCloudInternalClient getLibraryScopeStatusCountsForScopeWithIdentifier:completionHandler:]_block_invoke.116
- ___100-[PLAssetsdCloudInternalClient getLibraryScopeStatusCountsForScopeWithIdentifier:completionHandler:]_block_invoke.117
- ___104-[PLAssetsdResourceClient fileDescriptorForAssetURL:withAdjustments:fileExtension:fileDescriptor:error:]_block_invoke.55
- ___105-[PLAssetsdResourceClient sandboxExtensionForFileSystemBookmark:bookmarkURL:sandboxExtensionToken:error:]_block_invoke.83
- ___105-[PLAssetsdResourceClient saveAssetWithJobDictionary:imageSurface:previewImageSurface:completionHandler:]_block_invoke.18
- ___105-[PLAssetsdResourceClient saveAssetWithJobDictionary:imageSurface:previewImageSurface:completionHandler:]_block_invoke.21
- ___106-[PLAssetsdDebugClient privateDownloadCloudPhotoLibraryAsset:resourceType:highPriority:completionHandler:]_block_invoke.139
- ___106-[PLAssetsdResourceClient adjustmentDataForAsset:networkAccessAllowed:trackCPLDownload:completionHandler:]_block_invoke.85
- ___106-[PLAssetsdResourceClient adjustmentDataForAsset:networkAccessAllowed:trackCPLDownload:completionHandler:]_block_invoke.86
- ___107-[PLAssetsdCloudInternalClient confirmAllRemainingOnboardingPreviewAssetsOnLibraryScope:completionHandler:]_block_invoke.122
- ___107-[PLAssetsdCloudInternalClient confirmAllRemainingOnboardingPreviewAssetsOnLibraryScope:completionHandler:]_block_invoke.123
- ___110-[PLAssetsdCloudInternalClient resetLocalOnlyLibraryScopesAndAllLibraryScopeAssetStatesWithCompletionHandler:]_block_invoke.124
- ___110-[PLAssetsdCloudInternalClient resetLocalOnlyLibraryScopesAndAllLibraryScopeAssetStatesWithCompletionHandler:]_block_invoke.125
- ___110-[PLAssetsdCloudInternalClient userViewedSharedLibraryParticipantAssetTrashNotificationWithCompletionHandler:]_block_invoke.108
- ___110-[PLAssetsdCloudInternalClient userViewedSharedLibraryParticipantAssetTrashNotificationWithCompletionHandler:]_block_invoke.109
- ___115+[PLLibraryServicesOperation operationWithName:libraryServicesManager:requiredState:parentProgress:executionBlock:]_block_invoke
- ___116-[PLAssetsdPhotoKitClient processUniversalSearchJITForCoreSpotlightUniqueIdentifier:bundleID:processingTypes:error:]_block_invoke.25
- ___117-[PLAssetsdCloudInternalClient startExitFromLibraryScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:]_block_invoke.96
- ___117-[PLAssetsdCloudInternalClient startExitFromLibraryScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:]_block_invoke.97
- ___120-[PLAssetsdDebugClient coalesceJournalsForManagerName:payloadClassIDs:withChangeJournalOverThreshold:completionHandler:]_block_invoke.150
- ___120-[PLAssetsdDebugClient coalesceJournalsForManagerName:payloadClassIDs:withChangeJournalOverThreshold:completionHandler:]_block_invoke.151
- ___128-[PLAssetsdCloudInternalClient markOnboardingPreviewAssetsByProcessingRulesOnLibraryScope:excludePersonUUIDs:completionHandler:]_block_invoke.121
- ___130-[PLAssetsdResourceClient downloadCloudSharedAsset:withCloudPlaceholderKind:shouldPrioritize:shouldExtendTimer:completionHandler:]_block_invoke.103
- ___130-[PLAssetsdResourceClient downloadCloudSharedAsset:withCloudPlaceholderKind:shouldPrioritize:shouldExtendTimer:completionHandler:]_block_invoke.104
- ___131-[PLAssetsdResourceClient estimatedOutputFileLengthForVideoURL:fallbackFilePath:exportPreset:exportProperties:outFileLength:error:]_block_invoke.101
- ___137-[PLAssetsdResourceClient imageDataForAsset:format:allowPlaceholder:wantURLOnly:networkAccessAllowed:trackCPLDownload:completionHandler:]_block_invoke.61
- ___137-[PLAssetsdResourceClient imageDataForAsset:format:allowPlaceholder:wantURLOnly:networkAccessAllowed:trackCPLDownload:completionHandler:]_block_invoke.62
- ___143-[PLFormatChooser _bestFormatWithSize:specificVersionType:contentMode:demoteFactor:srcAspectRatio:hasAdjustmentsHandler:desiredImagePixelSize:]_block_invoke
- ___147-[PLAssetsdCloudInternalClient removeParticipantsWithParticipantUUIDs:fromLibraryScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:]_block_invoke.101
- ___147-[PLAssetsdCloudInternalClient removeParticipantsWithParticipantUUIDs:fromLibraryScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:]_block_invoke.102
- ___177-[PLAssetsdResourceClient imageDataForAsset:format:allowPlaceholder:wantURLOnly:networkAccessAllowed:trackCPLDownload:outImageData:outImageDataInfo:outCPLDownloadContext:error:]_block_invoke.59
- ___33-[PLAssetsdDebugClient getStatus]_block_invoke
- ___33-[PLAssetsdDebugClient getStatus]_block_invoke.5
- ___34+[PLDiskController sharedInstance]_block_invoke
- ___38-[PLGatekeeperClient getLibrarySizes:]_block_invoke
- ___40-[PLAssetsdDebugClient rebuildCloudFeed]_block_invoke.58
- ___42-[PLAssetsdDebugClient rebuildTableThumbs]_block_invoke.69
- ___44-[PLAssetsdDebugClient getCPLStateForDebug:]_block_invoke.80
- ___46-[PLAssetsdCloudInternalClient getCPLSettings]_block_invoke.139
- ___46-[PLAssetsdDebugClient momentGenerationStatus]_block_invoke.27
- ___47-[PLAssetsdDebugClient getTaskConstraintStatus]_block_invoke.77
- ___47-[PLAssetsdDebugClient getXPCTransactionStatus]_block_invoke.74
- ___47-[PLAssetsdDebugClient waitForMomentGeneration]_block_invoke.171
- ___49-[PLAssetsdDebugClient runMaintenanceTask:error:]_block_invoke.188
- ___50-[PLAssetsdDebugClient prefetchResourcesWithMode:]_block_invoke.117
- ___50-[PLAssetsdDebugClient pruneAssets:resourceTypes:]_block_invoke.104
- ___51+[PLImportFileManager isCameraDirectoryFolderName:]_block_invoke
- ___51-[PLAssetsdDebugClient indexAssetsWithUUIDs:error:]_block_invoke.55
- ___51-[PLAssetsdDebugClient resetComputeCacheWithError:]_block_invoke.164
- ___52-[PLAssetsdDebugClient computeCacheStatusWithError:]_block_invoke.165
- ___52-[PLAssetsdDebugClient rebuildSearchIndexWithError:]_block_invoke.51
- ___53-[PLAssetsdDebugClient archiveComputeCacheWithError:]_block_invoke.163
- ___53-[PLAssetsdDebugClient backgroundMigrationWithError:]_block_invoke.176
- ___53-[PLAssetsdDebugClient prefetchResourcesForMemories:]_block_invoke.109
- ___53-[PLAssetsdDebugClient restoreComputeCacheWithError:]_block_invoke.162
- ___54-[PLAssetsdCloudInternalClient setPrefetchMode:error:]_block_invoke.143
- ___55-[PLAssetsdDebugClient prefetchResourcesForHighlights:]_block_invoke.114
- ___55-[PLAssetsdDebugClient resetMaintenanceTasksWithError:]_block_invoke.185
- ___55-[PLAssetsdDebugClient revertToOriginalForAsset:error:]_block_invoke.88
- ___55-[PLAssetsdDebugClient updateHighlightTitlesWithError:]_block_invoke.125
- ___55-[PLAssetsdResourceInternalClient cancelAllPrewarming:]_block_invoke.27
- ___56-[PLAssetsdDebugClient cleanupEmptyHighlightsWithError:]_block_invoke.128
- ___57-[PLAssetsdDebugClient processRecentHighlightsWithError:]_block_invoke.119
- ___57-[PLAssetsdLibraryInternalClient getSearchIndexProgress:]_block_invoke.36
- ___57-[PLFormatChooser _nextLargestAcceptableFormatForFormat:]_block_invoke
- ___58-[PLAssetsdDebugClient locationOfInterestUpdateWithError:]_block_invoke.134
- ___59-[PLAssetsdDebugClient removeAllThumbnailsForDryRun:count:]_block_invoke.65
- ___60-[PLAssetsdCloudInternalClient getResetSyncStatusWithError:]_block_invoke.87
- ___60-[PLAssetsdLibraryInternalClient failAvailabilityWithError:]_block_invoke.91
- ___61-[PLAssetsdDebugClient dropSearchIndexWithCompletionHandler:]_block_invoke.36
- ___61-[PLAssetsdDebugClient dropSearchIndexWithCompletionHandler:]_block_invoke.37
- ___62-[PLAssetsdDebugClient closeSearchIndexWithCompletionHandler:]_block_invoke.40
- ___62-[PLAssetsdDebugClient closeSearchIndexWithCompletionHandler:]_block_invoke.41
- ___62-[PLAssetsdResourceClient addGroupWithName:completionHandler:]_block_invoke.25
- ___62-[PLAssetsdResourceClient addGroupWithName:completionHandler:]_block_invoke.26
- ___62-[PLAssetsdResourceClient projectExtensionDataForProjectUuid:]_block_invoke.124
- ___63-[PLAssetsdLibraryInternalClient setKeywords:forAssetWithUUID:]_block_invoke.49
- ___63-[PLAssetsdResourceClient consolidateAssets:completionHandler:]_block_invoke.112
- ___64-[PLAssetsdDebugClient resetBackgroundMigrationClassName:error:]_block_invoke.179
- ___66-[PLAssetsdLibraryInternalClient clearAvailabilityStateWithError:]_block_invoke.90
- ___66-[PLLibraryServicesOperation setExecutionBlockFromOperationBlock:]_block_invoke
- ___67-[PLAssetsdDebugClient processUnprocessedMomentLocationsWithError:]_block_invoke.122
- ___68-[PLAssetsdDebugClient rebuildMomentsDeletingExistingMoments:error:]_block_invoke.28
- ___68-[PLAssetsdDebugClient setAssetContainmentLargeFaceThreshold:error:]_block_invoke
- ___68-[PLAssetsdDebugClient setAssetContainmentSmallFaceThreshold:error:]_block_invoke
- ___68-[PLAssetsdDebugClient updateAndSaveAssetPersonEdgesWithCompletion:]_block_invoke.157
- ___69-[PLAssetsdDebugClient setAssetContainmentSmallTorsoThreshold:error:]_block_invoke
- ___69-[PLAssetsdLibraryInternalClient featureProcessingSnapshotWithError:]_block_invoke.88
- ___70-[PLAssetsdLibraryInternalClient signalAvailabilityWithChanges:error:]_block_invoke.93
- ___70-[PLAssetsdResourceClient updateInternalResourcePath:objectURI:error:]_block_invoke.120
- ___71-[PLAssetsdCloudInternalClient activateLibraryScope:completionHandler:]_block_invoke.89
- ___71-[PLAssetsdCloudInternalClient activateLibraryScope:completionHandler:]_block_invoke.90
- ___71-[PLAssetsdCloudInternalClient isComputeSyncEnabledForDirection:reply:]_block_invoke.148
- ___71-[PLAssetsdDebugClient synchronouslySetSearchIndexPaused:reason:error:]_block_invoke
- ___71-[PLAssetsdDebugClient synchronouslySetSearchIndexPaused:reason:error:]_block_invoke.47
- ___71-[PLAssetsdLibraryInternalClient availabilityStateShouldPersist:error:]_block_invoke.89
- ___71-[PLAssetsdLibraryInternalClient waitForSearchIndexExistenceWithError:]_block_invoke.37
- ___72-[PLAssetsdDebugClient syndicationIngestMutexStateDescriptionWithError:]_block_invoke.167
- ___72-[PLAssetsdLibraryInternalClient getBackgroundJobServiceStateWithError:]_block_invoke.56
- ___73-[PLAssetsdCloudInternalClient deactivateLibraryScope:completionHandler:]_block_invoke.94
- ___73-[PLAssetsdCloudInternalClient deactivateLibraryScope:completionHandler:]_block_invoke.95
- ___73-[PLAssetsdResourceInternalClient prewarmWithCapturePhotoSettings:error:]_block_invoke.23
- ___74-[PLAssetsdDebugClient rebuildHighlightsDeletingExistingHighlights:error:]_block_invoke.29
- ___74-[PLAssetsdLibraryInternalClient getLibrarySizesFromDB:completionHandler:]_block_invoke_2
- ___74-[PLAssetsdPhotoKitClient analyzeAssets:forFeature:withCompletionHandler:]_block_invoke.28
- ___74-[PLAssetsdPhotoKitClient analyzeLibraryForFeature:withCompletionHandler:]_block_invoke.30
- ___75-[PLAssetsdDebugClient runAssetContainmentOnAllSocialGroupsWithCompletion:]_block_invoke.155
- ___75-[PLAssetsdLibraryInternalClient pauseSearchIndexingWithCompletionHandler:]_block_invoke.40
- ___75-[PLAssetsdLibraryInternalClient pauseSearchIndexingWithCompletionHandler:]_block_invoke.41
- ___76-[PLAssetsdCloudInternalClient runComputeSyncBackfillMigrationSynchronously]_block_invoke
- ___76-[PLAssetsdCloudInternalClient sharedLibraryRampCheckWithCompletionHandler:]_block_invoke.106
- ___76-[PLAssetsdCloudInternalClient sharedLibraryRampCheckWithCompletionHandler:]_block_invoke.107
- ___76-[PLAssetsdLibraryInternalClient resumeSearchIndexingWithCompletionHandler:]_block_invoke.38
- ___76-[PLAssetsdLibraryInternalClient resumeSearchIndexingWithCompletionHandler:]_block_invoke.39
- ___76-[PLAssetsdLibraryInternalClient signalAvailabilityStateDidChangeWithError:]_block_invoke.92
- ___76-[PLAssetsdResourceClient fileURLForAssetURL:withAdjustments:fileURL:error:]_block_invoke.47
- ___76-[PLAssetsdResourceInternalClient cancelAllPrewarmingWithCompletionHandler:]_block_invoke.30
- ___77-[PLAssetsdResourceClient addAssetWithURL:toAlbumWithUUID:completionHandler:]_block_invoke.37
- ___77-[PLAssetsdResourceClient addAssetWithURL:toAlbumWithUUID:completionHandler:]_block_invoke.38
- ___79-[PLAssetsdDebugClient assetContainmentLargeFaceThresholdUserDefaultWithError:]_block_invoke
- ___79-[PLAssetsdDebugClient assetContainmentLargeFaceThresholdUserDefaultWithError:]_block_invoke.160
- ___79-[PLAssetsdDebugClient assetContainmentSmallFaceThresholdUserDefaultWithError:]_block_invoke
- ___79-[PLAssetsdDebugClient assetContainmentSmallFaceThresholdUserDefaultWithError:]_block_invoke.158
- ___79-[PLAssetsdLibraryInternalClient deleteEmbeddings:assetUUID:completionHandler:]_block_invoke
- ___79-[PLAssetsdLibraryInternalClient deleteEmbeddings:assetUUID:completionHandler:]_block_invoke_2
- ___80-[PLAssetsdCloudInternalClient getCPLConfigrationValueForKey:completionHandler:]_block_invoke.136
- ___80-[PLAssetsdDebugClient assetContainmentSmallTorsoThresholdUserDefaultWithError:]_block_invoke
- ___80-[PLAssetsdDebugClient assetContainmentSmallTorsoThresholdUserDefaultWithError:]_block_invoke.161
- ___80-[PLAssetsdDebugClient debugSidecarFileURLsForAsset:debugSidecarFileURLs:error:]_block_invoke.95
- ___80-[PLAssetsdDebugClient runAssetContainmentOnSocialGroupWithUUID:withCompletion:]_block_invoke.156
- ___80-[PLAssetsdLibraryInternalClient invalidateBehavioralScoreOnAllAssetsWithError:]_block_invoke
- ___80-[PLAssetsdLibraryInternalClient invalidateBehavioralScoreOnAllAssetsWithError:]_block_invoke.62
- ___81-[PLAssetsdDebugClient requestSearchDebugInformationForAssetUUID:redacted:error:]_block_invoke.54
- ___81-[PLAssetsdDebugClient unloadImageFilesForAsset:minimumFormat:completionHandler:]_block_invoke.17
- ___81-[PLAssetsdLibraryInternalClient deleteiTunesSyncedContentWithCompletionHandler:]_block_invoke.61
- ___81-[PLAssetsdLibraryInternalClient synchronouslyGetLibrarySizesFromDB:sizes:error:]_block_invoke
- ___81-[PLAssetsdLibraryInternalClient synchronouslyGetLibrarySizesFromDB:sizes:error:]_block_invoke_2
- ___82-[PLAssetsdDebugClient allMomentsMetadataWithOutputPath:metadataDictionary:error:]_block_invoke.35
- ___83-[PLAssetsdLibraryInternalClient checkAssetsArePendingForDuplicateMergeProcessing:]_block_invoke.82
- ___83-[PLAssetsdLibraryInternalClient getBackgroundJobServiceStatusCenterDumpWithError:]_block_invoke.58
- ___83-[PLAssetsdPhotoKitClient getUUIDsForAssetObjectIDs:filterPredicate:context:error:]_block_invoke.21
- ___83-[PLAssetsdPhotoKitClient getUUIDsForAssetObjectIDs:filterPredicate:context:error:]_block_invoke.23
- ___84-[PLAssetsdCloudInternalClient refreshLibraryScopeWithIdentifier:completionHandler:]_block_invoke.113
- ___84-[PLAssetsdCloudInternalClient refreshLibraryScopeWithIdentifier:completionHandler:]_block_invoke.114
- ___84-[PLAssetsdDebugClient resetDrawAssetPersonEdgesBackgroundMigrationActionWithError:]_block_invoke.182
- ___84-[PLAssetsdLibraryInternalClient invalidateReverseLocationDataOnAllAssetsWithError:]_block_invoke.51
- ___85-[PLAssetsdDebugClient dumpMetadataForMomentsWithOutputPath:metadataDirectory:error:]_block_invoke.30
- ___85-[PLAssetsdLibraryInternalClient processIdenticalDuplicatesWithProcessingType:error:]_block_invoke.79
- ___85-[PLAssetsdResourceInternalClient prewarmWithCapturePhotoSettings:completionHandler:]_block_invoke.25
- ___85-[PLAssetsdResourceInternalClient prewarmWithCapturePhotoSettings:completionHandler:]_block_invoke.26
- ___87-[PLAssetsdPhotoKitClient processUniversalSearchJITForAssetUUID:processingTypes:error:]_block_invoke.27
- ___88-[PLAssetsdCloudInternalClient forceParticipantAssetTrashNotificationCompletionHandler:]_block_invoke.110
- ___88-[PLAssetsdCloudInternalClient forceParticipantAssetTrashNotificationCompletionHandler:]_block_invoke.111
- ___88-[PLAssetsdResourceInternalClient batchSaveAssetsWithJobDictionaries:completionHandler:]_block_invoke.15
- ___88-[PLAssetsdResourceInternalClient requestMasterThumbnailForAssetUUID:completionHandler:]_block_invoke.18
- ___89-[PLAssetsdLibraryInternalClient insertEmbeddings:modelType:assetUUID:completionHandler:]_block_invoke
- ___89-[PLAssetsdLibraryInternalClient insertEmbeddings:modelType:assetUUID:completionHandler:]_block_invoke_2
- ___90-[PLAssetsdCloudInternalClient requestDeviceLibraryConfigurationChange:completionHandler:]_block_invoke.126
- ___90-[PLAssetsdCloudInternalClient requestDeviceLibraryConfigurationChange:completionHandler:]_block_invoke.127
- ___90-[PLAssetsdDebugClient invalidateHighlightSubtitlesAndRegenerateHighlightTitlesWithError:]_block_invoke.131
- ___90-[PLAssetsdResourceClient sandboxExtensionsForAssetWithUUID:sandboxExtensionTokens:error:]_block_invoke.72
- ___91-[PLAssetsdCloudInternalClient queryParticipantsWithEmails:phoneNumbers:completionHandler:]_block_invoke.83
- ___91-[PLAssetsdCloudInternalClient queryParticipantsWithEmails:phoneNumbers:completionHandler:]_block_invoke.84
- ___91-[PLAssetsdLibraryInternalClient getBackgroundJobServiceBundlesInQueueDictionaryWithError:]_block_invoke.60
- ___92-[PLAssetsdPhotoKitClient resetStateForMediaProcessingTaskID:assetUUIDs:resetOptions:error:]_block_invoke.31
- ___92-[PLAssetsdResourceClient sandboxExtensionFileURLForAssetURL:withAdjustments:fileURL:error:]_block_invoke.49
- ___93-[PLAssetsdDebugClient snapshotJournalsForManagerName:payloadClassIDs:withCompletionHandler:]_block_invoke.145
- ___93-[PLAssetsdDebugClient snapshotJournalsForManagerName:payloadClassIDs:withCompletionHandler:]_block_invoke.146
- ___93-[PLAssetsdLibraryInternalClient registerBackgroundJobServiceIfNecessaryOnLibraryPath:error:]_block_invoke.55
- ___95-[PLAssetsdCloudInternalClient markResourcesPurgeableWithUrgency:assetUuids:completionHandler:]_block_invoke.132
- ___96-[PLAssetsdLibraryInternalClient applySearchIndexGraphUpdates:supportingData:completionHandler:]_block_invoke
- ___96-[PLAssetsdLibraryInternalClient applySearchIndexGraphUpdates:supportingData:completionHandler:]_block_invoke_2
- ___Block_byref_object_copy_.11152
- ___Block_byref_object_copy_.11715
- ___Block_byref_object_copy_.11872
- ___Block_byref_object_copy_.11924
- ___Block_byref_object_copy_.11971
- ___Block_byref_object_copy_.12026
- ___Block_byref_object_copy_.12245
- ___Block_byref_object_copy_.1498
- ___Block_byref_object_copy_.1614
- ___Block_byref_object_copy_.1889
- ___Block_byref_object_copy_.3155
- ___Block_byref_object_copy_.3336
- ___Block_byref_object_copy_.3407
- ___Block_byref_object_copy_.3511
- ___Block_byref_object_copy_.3699
- ___Block_byref_object_copy_.4871
- ___Block_byref_object_copy_.5496
- ___Block_byref_object_copy_.5758
- ___Block_byref_object_copy_.6046
- ___Block_byref_object_copy_.6372
- ___Block_byref_object_copy_.6563
- ___Block_byref_object_copy_.7145
- ___Block_byref_object_copy_.7966
- ___Block_byref_object_copy_.8967
- ___Block_byref_object_copy_.9011
- ___Block_byref_object_copy_.9511
- ___Block_byref_object_copy_.973
- ___Block_byref_object_dispose_.11153
- ___Block_byref_object_dispose_.11716
- ___Block_byref_object_dispose_.11873
- ___Block_byref_object_dispose_.11925
- ___Block_byref_object_dispose_.11972
- ___Block_byref_object_dispose_.12027
- ___Block_byref_object_dispose_.12246
- ___Block_byref_object_dispose_.1499
- ___Block_byref_object_dispose_.1615
- ___Block_byref_object_dispose_.1890
- ___Block_byref_object_dispose_.3156
- ___Block_byref_object_dispose_.3337
- ___Block_byref_object_dispose_.3408
- ___Block_byref_object_dispose_.3512
- ___Block_byref_object_dispose_.3700
- ___Block_byref_object_dispose_.4872
- ___Block_byref_object_dispose_.5497
- ___Block_byref_object_dispose_.5759
- ___Block_byref_object_dispose_.6047
- ___Block_byref_object_dispose_.6373
- ___Block_byref_object_dispose_.6564
- ___Block_byref_object_dispose_.7146
- ___Block_byref_object_dispose_.7967
- ___Block_byref_object_dispose_.8968
- ___Block_byref_object_dispose_.9012
- ___Block_byref_object_dispose_.9512
- ___Block_byref_object_dispose_.974
- ___PLGridInlinePlaybackGetLog_block_invoke
- ___PLIsCamera_block_invoke
- ___PLIsLockScreenCamera_block_invoke
- ___PLIsMobileSlideShow_block_invoke
- ___PLIsPhotoPicker_block_invoke
- ___PLIsPhotosMessagesApp_block_invoke
- ___PLIsPreferences_block_invoke
- ___PLIsSpotlight_block_invoke
- ___PLIsTVPhotosApp_block_invoke
- ____create5551BGRACGImageFromTableEntryNode_block_invoke
- ___block_descriptor_112_e8_32s40s48bs56n18_8_8_t0w1_s8_t16w32_e51_v16?0"<PLAssetsdLibraryInternalServiceProtocol>"8l
- ___block_descriptor_120_e8_32s40s48bs56n18_8_8_t0w1_s8_t16w32_e51_v16?0"<PLAssetsdLibraryInternalServiceProtocol>"8l
- ___block_descriptor_40_e8_32r_e20_v24?0d8"NSError"16lr32l8
- ___block_descriptor_40_e8_32r_e30_v32?0"PLImageFormat"8Q16^B24lr32l8
- ___block_descriptor_48_e12_v24?0^v8Q16l
- ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
- ___block_descriptor_57_e8_32r40r48r_e37_v28?0B8"NSDictionary"12"NSError"20lr32l8r40l8r48l8
- ___block_descriptor_64_e8_32s40s48r56r_e30_v24?0"NSString"8"NSError"16lr48l8s32l8s40l8r56l8
- ___block_literal_global.103
- ___block_literal_global.106
- ___block_literal_global.1061
- ___block_literal_global.108.2571
- ___block_literal_global.10861
- ___block_literal_global.111.1902
- ___block_literal_global.111.2574
- ___block_literal_global.11158
- ___block_literal_global.11396
- ___block_literal_global.11497
- ___block_literal_global.11608
- ___block_literal_global.12.2522
- ___block_literal_global.120.6069
- ___block_literal_global.12028
- ___block_literal_global.121
- ___block_literal_global.12226
- ___block_literal_global.1228
- ___block_literal_global.124
- ___block_literal_global.124.3875
- ___block_literal_global.1243
- ___block_literal_global.126.3879
- ___block_literal_global.12612
- ___block_literal_global.12736
- ___block_literal_global.130
- ___block_literal_global.131
- ___block_literal_global.133
- ___block_literal_global.136
- ___block_literal_global.138.2587
- ___block_literal_global.138.6049
- ___block_literal_global.1382
- ___block_literal_global.142
- ___block_literal_global.144.2591
- ___block_literal_global.145
- ___block_literal_global.145.6044
- ___block_literal_global.147.6038
- ___block_literal_global.149
- ___block_literal_global.150.3905
- ___block_literal_global.155
- ___block_literal_global.159.4943
- ___block_literal_global.16.6213
- ___block_literal_global.163
- ___block_literal_global.165.3916
- ___block_literal_global.1666
- ___block_literal_global.170.3921
- ___block_literal_global.175
- ___block_literal_global.175.3926
- ___block_literal_global.178
- ___block_literal_global.179
- ___block_literal_global.18.2528
- ___block_literal_global.180.3928
- ___block_literal_global.181
- ___block_literal_global.187
- ___block_literal_global.188.6457
- ___block_literal_global.192.6458
- ___block_literal_global.193
- ___block_literal_global.1971
- ___block_literal_global.198.3939
- ___block_literal_global.1983
- ___block_literal_global.2.6241
- ___block_literal_global.20.6209
- ___block_literal_global.201.6450
- ___block_literal_global.203
- ___block_literal_global.208
- ___block_literal_global.213.3947
- ___block_literal_global.22.1958
- ___block_literal_global.221
- ___block_literal_global.223
- ___block_literal_global.228.3958
- ___block_literal_global.23
- ___block_literal_global.234.3960
- ___block_literal_global.24.2532
- ___block_literal_global.24.6203
- ___block_literal_global.2514
- ___block_literal_global.256
- ___block_literal_global.259
- ___block_literal_global.26
- ___block_literal_global.267.3982
- ___block_literal_global.27.6197
- ___block_literal_global.270.3984
- ___block_literal_global.272
- ___block_literal_global.274
- ___block_literal_global.276.10834
- ___block_literal_global.288.3996
- ___block_literal_global.29.11147
- ___block_literal_global.290
- ___block_literal_global.295
- ___block_literal_global.298
- ___block_literal_global.30.6191
- ___block_literal_global.302
- ___block_literal_global.306
- ___block_literal_global.310
- ___block_literal_global.314
- ___block_literal_global.314.4011
- ___block_literal_global.3178
- ___block_literal_global.318
- ___block_literal_global.322.4020
- ___block_literal_global.3288
- ___block_literal_global.331
- ___block_literal_global.3350
- ___block_literal_global.3415
- ___block_literal_global.35
- ___block_literal_global.3618
- ___block_literal_global.375.5060
- ___block_literal_global.380
- ___block_literal_global.3867
- ___block_literal_global.398
- ___block_literal_global.42.6169
- ___block_literal_global.4219
- ___block_literal_global.48.3580
- ___block_literal_global.48.6166
- ___block_literal_global.50.1922
- ___block_literal_global.50.6157
- ___block_literal_global.5048
- ___block_literal_global.5241
- ___block_literal_global.557
- ___block_literal_global.568
- ___block_literal_global.57.2546
- ___block_literal_global.5704
- ___block_literal_global.573
- ___block_literal_global.5752
- ___block_literal_global.6.1048
- ___block_literal_global.6.2518
- ___block_literal_global.6.6621
- ___block_literal_global.60.2549
- ___block_literal_global.6252
- ___block_literal_global.6367
- ___block_literal_global.64
- ___block_literal_global.6491
- ___block_literal_global.6631
- ___block_literal_global.668
- ___block_literal_global.677
- ___block_literal_global.6800
- ___block_literal_global.7150
- ___block_literal_global.73.7725
- ___block_literal_global.739
- ___block_literal_global.75.2555
- ___block_literal_global.76
- ___block_literal_global.76.3545
- ___block_literal_global.7755
- ___block_literal_global.78.3541
- ___block_literal_global.79
- ___block_literal_global.7961
- ___block_literal_global.81.3534
- ___block_literal_global.82
- ___block_literal_global.84.2559
- ___block_literal_global.8612
- ___block_literal_global.8933
- ___block_literal_global.9.11498
- ___block_literal_global.9.6622
- ___block_literal_global.93.6350
- ___block_literal_global.9686
- __create5551BGRACGImageFromTableEntryNode.s_colorSpace
- __create5551BGRACGImageFromTableEntryNode.s_onceToken
- __shouldSuppressLogging
- _allPhotosPathsOnThisDevice.bundlePaths.2393
- _allPhotosPathsOnThisDevice.onceToken.2392
- _isCameraDirectoryFolderName:.gCameraDirectoryExpression
- _isCameraDirectoryFolderName:.onceToken
- _kCFBooleanFalse
- _kCGImageSourceRasterizationDPI
- _kMGQDiskUsageAmountDataAvailable
- _objc_msgSend$_actuallyUpdateCookie
- _objc_msgSend$_bestFormatWithSize:specificVersionType:contentMode:demoteFactor:srcAspectRatio:hasAdjustmentsHandler:desiredImagePixelSize:
- _objc_msgSend$_canDegradeToFormat:
- _objc_msgSend$_desiredImageSizeForRequestedViewSizeInPixels:isAspectFill:srcAspectRatio:
- _objc_msgSend$_diskSpaceDidBecomeLow
- _objc_msgSend$_fastestDegradedFormatFallingBackFromFormat:
- _objc_msgSend$_isAcceptableForViewSize:contentMode:sourceAspectRatio:desiredImageSize:demoteFactor:
- _objc_msgSend$_nextLargestAcceptableFormatForFormat:
- _objc_msgSend$_runOperationBlock:
- _objc_msgSend$_standardDegradedFormatFallingBackFromFormat:
- _objc_msgSend$_updateCookie
- _objc_msgSend$accessibleURLOrParentForFileURL:
- _objc_msgSend$addChild:withPendingUnitCount:
- _objc_msgSend$addExecutionBlock:
- _objc_msgSend$applyGraphUpdates:supportingData:reply:
- _objc_msgSend$assetContainmentLargeFaceThresholdUserDefault:
- _objc_msgSend$assetContainmentSmallFaceThresholdUserDefault:
- _objc_msgSend$assetContainmentSmallTorsoThresholdUserDefault:
- _objc_msgSend$becomeCurrentWithPendingUnitCount:
- _objc_msgSend$characterAtIndex:
- _objc_msgSend$deleteEmbeddings:assetUUID:reply:
- _objc_msgSend$derivativeFormatThatFitsSize:contentMode:demoteFactor:srcAspectRatio:desiredImagePixelSize:
- _objc_msgSend$discreteProgressWithTotalUnitCount:
- _objc_msgSend$fractionCompleted
- _objc_msgSend$initWithAssetUuid:bundleScope:uti:resourceVersion:resourceType:recipeID:originalFilename:
- _objc_msgSend$initWithLogicalScreenSize:screenScale:deviceClass:supportsASTC:isMigrationService:
- _objc_msgSend$initWithPattern:options:error:
- _objc_msgSend$insertEmbeddings:modelType:assetUUID:reply:
- _objc_msgSend$invalidateBehavioralScoreOnAllAssetsWithReply:
- _objc_msgSend$maxLivePhotoDataSize
- _objc_msgSend$numberOfMatchesInString:options:range:
- _objc_msgSend$performSelectorOnMainThread:withObject:waitUntilDone:
- _objc_msgSend$pool
- _objc_msgSend$progress
- _objc_msgSend$progressPercentOfTotal
- _objc_msgSend$readDataAtIndex:intoPoolNode:bytesRead:
- _objc_msgSend$readImageDataAtIndex:intoPoolNode:bytesRead:imageWidth:imageHeight:imageDataWidth:imageDataHeight:startingOffset:bytesPerRow:uuidBytes:
- _objc_msgSend$removeObserver:
- _objc_msgSend$requiredState
- _objc_msgSend$resignCurrent
- _objc_msgSend$runComputeSyncBackfillMigrationSynchronously
- _objc_msgSend$setAssetContainmentLargeFaceThreshold:
- _objc_msgSend$setAssetContainmentSmallFaceThreshold:
- _objc_msgSend$setAssetContainmentSmallTorsoThreshold:
- _objc_msgSend$setExecutionBlockFromOperationBlock:
- _objc_msgSend$setProgressPercentOfTotal:
- _objc_msgSend$setRequiredState:
- _objc_msgSend$setSearchIndexPaused:reason:reply:
- _objc_msgSend$shouldSuppressLogging
- _objc_msgSend$synchronouslyGetLibrarySizesFromDB:sizes:error:
- _objc_msgSend$totalUnitCount
- _objc_msgSend$updateAvailableDiskSpace
- _objc_msgSend$validatedSavedAssetTypeMaskUnknown:photoBooth:photoStream:camera:cloudShared:cameraConnectionKit:cloudPhotoLibrary:wallpaper_UNUSED:momentShared:placeholder:referenced:alternate:guest:companionSynced:recovered:legacyImport:
- _sharedInstance.onceToken.8932
- _sharedInstance.pl_once_object_17
- _sharedInstance.pl_once_token_17
- _vm_allocate
- _vm_deallocate
- _vm_page_size
CStrings:
+ "$"
+ "%s Failed to open PHPhotoLibrary for the SPL, sending empty dictionary to handler: %@"
+ "%s%@%s.%s"
+ "-[PLAssetsdDebugClient clearSensitivityStateForAssetsWithUUIDs:error:]_block_invoke"
+ "-[PLAssetsdLibraryInternalClient _inProcess_getLibrarySizesFromDB:handler:]"
+ "-[PLAssetsdLibraryInternalClient deleteAllInitialSuggestionsWithError:]_block_invoke"
+ "-[PLAssetsdLibraryInternalClient generateInitialSuggestionsWithStyleType:error:]_block_invoke"
+ "-[PLAssetsdLibraryInternalClient updateInitialSuggestionsWithIdentifiers:dateLastUsed:error:]_block_invoke"
+ "-[PLAssetsdNonBindingDebugClient getStatus]_block_invoke"
+ "-[PLAssetsdNonBindingDebugClient libraryServicesStateByBundlePathWithCompletion:]_block_invoke"
+ "-[PLAssetsdPhotoKitClient cancelReservedCloudIdentifiers:error:]_block_invoke_2"
+ "-[PLAssetsdPhotoKitClient forceSyndicationIngestAsyncToDate:withCompletionHandler:]_block_invoke"
+ "-[PLAssetsdPhotoKitClient forceSyndicationIngestSyncToDate:error:]_block_invoke"
+ "-[PLAssetsdPhotoKitClient ingestItemWithCoreSpotlightUniqueIdentifier:bundleID:purgeUrgency:error:]_block_invoke"
+ "-[PLAssetsdPhotoKitClient photoLibraryIdentifierWithError:]_block_invoke"
+ "-[PLGatekeeperClient _inProcess_getLibrarySizesFromDB:handler:]"
+ "@\"NSProgress\"32@0:8@\"NSDate\"16@?<v@?@\"NSError\">24"
+ "@32@0:8Q16@24"
+ "@32@0:8{CGSize=dd}16"
+ "@48@0:8@16@24q32^@40"
+ "@52@0:8{CGSize=dd}16d32^v40B48"
+ "@64@0:8@16S24@28I36I40I44@48@56"
+ "ActivityMotionStateBlockedCount"
+ "Alchemist allowed default not set in domain %@. Defaulting to YES"
+ "AlchemistV2OneUp.mxi"
+ "AlchemistV2Wallpaper.mxi"
+ "AlchemistV2Widget1x1.mxi"
+ "AlchemistV2Widget1x2.mxi"
+ "B28@0:8B16@?20"
+ "B32@0:8{CGSize=dd}16"
+ "B40@0:8Q16^v24^Q32"
+ "B96@0:8Q16^v24^Q32^i40^i48^i56^i64^q72^Q80^{?=CCCCCCCCCCCCCCCC}88"
+ "BackendPerfTest"
+ "Calling XPC getLibrarySizesFromDB:%@ at QoS %@"
+ "CollectionShare"
+ "ConsoleModeBlockedCount"
+ "Contextual video thumbnail URL is obtained via PLManagedAsset.fileURLForContextualVideoThumbnailIdentifier"
+ "DASDoItNowUnBlockedCount"
+ "DeviceActivityBlockedCount"
+ "DeviceActivityEarlyThermalWarningBlockedCount"
+ "EnableAlchemizeButton"
+ "Error getting photo library identifier: %@"
+ "Failed to calloc buffer for PLPositionalImageTableNSDataReleaseInfo."
+ "Failed to resolve real path for %@ (%{public}s)."
+ "I84@0:8B16B20B24B28B32B36B40B44B48B52B56B60B64B68B72B76B80"
+ "Ingest failed for %{public}@ : %{public}@ : %@"
+ "Lowering QoS for getLibrarySizes from %@ to UT"
+ "NSString *_pathForResourceProperties(const char *, const char *, PLResourceType, PLResourceVersion, PLResourceRecipeID, BOOL, const char *, const char *, const char *, const char *, const char *, const char *, const char *)"
+ "No error, photoLibrary = %@"
+ "PHPhotoLibrary"
+ "PLAssetsdNonBindingDebugClient.m"
+ "PLPhotoLibraryInternalPathTypePhotosMessagesBackdropDescriptors"
+ "PLPhotosErrorGraphBitsetIndexOutOfBounds"
+ "PLPhotosErrorPreSchemaMigrationFailed"
+ "PLPhotosErrorSyndicationIngestMutexUnavailable"
+ "PLXPC Client: allKnownLibraryPaths:"
+ "PLXPC Client: cancelReservedCloudIdentifiers:error:"
+ "PLXPC Client: clearSensitivityStateForAssetsWithUUIDs:error:"
+ "PLXPC Client: declineCollectionShareWithUUID:completionHandler:"
+ "PLXPC Client: deleteAllInitialSuggestionsWithError:"
+ "PLXPC Client: forceSyndicationIngestAsyncToDate:withCompletionHandler:"
+ "PLXPC Client: forceSyndicationIngestSyncToDate:error:"
+ "PLXPC Client: generateInitialSuggestionsWithStyleType:error:"
+ "PLXPC Client: ingestItemWithCoreSpotlightUniqueIdentifier:bundleID:purgeUrgency:error:"
+ "PLXPC Client: libraryServicesStateByBundlePathWithCompletion:"
+ "PLXPC Client: photoLibraryIdentifierWithError:"
+ "PLXPC Client: reportInvitationAsSpamForCollectionShareWithUUID:completionHandler:"
+ "PLXPC Client: sendInvitationsForCollectionShareWithUUID:participantUUIDs:completionHandler:"
+ "PLXPC Client: updateInitialSuggestionsWithIdentifiers:dateLastUsed:error:"
+ "Prefetch sensitive content analysis policy"
+ "Q164@0:8s16Q20Q28Q36Q44Q52Q60Q68Q76Q84Q92Q100Q108Q116Q124Q132Q140Q148Q156"
+ "SearchBackendPSITokenizer"
+ "SearchBackendThumbnailMap"
+ "SharedCollections"
+ "SignificantTransferBlockedCount"
+ "T@\"NSString\",R,C,N,V_customSuffix"
+ "T@\"NSString\",R,C,N,V_originalFilename"
+ "Unable to decline collection share because XPC service returned an error. (%@)"
+ "Unable to decline collection share with uuid: %@. (%@)"
+ "Unable to fetch share from share url: %@. (%@)"
+ "Unable to report invitation as spam for collection share because XPC service returned an error. (%@)"
+ "Unable to report invitation as spam for collection share with uuid: %@. (%@)"
+ "Unable to resend invitations for participants of collection share because XPC service returned an error. (%@)"
+ "Unable to resend invitations for participants of collection share with uuid: %@. (%@)"
+ "_customSuffix"
+ "_cvt_"
+ "_derivativeFormatThatFitsSize:"
+ "_derivativesContextualVideoThumbnailsDirectory"
+ "_desiredImageSizeForRequestedViewSizeInPixels:"
+ "_getLibrarySizesFromDB:completionHandler:"
+ "_inProcess_getLibrarySizesFromDB:handler:"
+ "_isAcceptableForDesiredImageSize:"
+ "_librarySizesQueue"
+ "_maskForCollectionShareMutatingFrom"
+ "_maskForCollectionShareMutatingTo"
+ "_scopesCollectionShareDirectory"
+ "_setError"
+ "allKnownLibraryPaths:"
+ "cancelReservedCloudIdentifiers:error:"
+ "cancelReservedCloudIdentifiers:reply:"
+ "clearSensitivityStateForAssetsWithUUIDs:error:"
+ "clearSensitivityStateForAssetsWithUUIDs:reply:"
+ "clientIsAllowedToFetchCollectionShares"
+ "collectionshare"
+ "com.apple.FruitBasket"
+ "com.apple.photos.librarySizesFromDB"
+ "com.apple.private.photos.allowcollectionshare"
+ "com.apple.private.photos.messages.access"
+ "createDirectoryAtURL:error:"
+ "createDirectoryAtURL:error:usingFileManager:"
+ "createImageWithIdentifier: cannot allocate."
+ "customSuffix"
+ "cvtBase != NULL"
+ "declineCollectionShareWithUUID:completionHandler:"
+ "declineCollectionShareWithUUID:reply:"
+ "deleteAllInitialSuggestionsWithError:"
+ "deleteAllInitialSuggestionsWithReply:"
+ "executeBlockForSavedAssetType:unknown:photoBooth:photoStream:camera:cloudShared:cameraConnectionKit:cloudPhotoLibrary:wallpaper_UNUSED:momentShared:placeholder:referenced:alternate:guest:companionSynced:recovered:legacyImport:collectionShare:unrecognized:"
+ "forceSyndicationIngestAsyncToDate:reply:"
+ "forceSyndicationIngestAsyncToDate:withCompletionHandler:"
+ "forceSyndicationIngestSyncToDate:error:"
+ "forceSyndicationIngestUpToDate failed with error %@"
+ "generateInitialSuggestionsWithStyleType:error:"
+ "generateInitialSuggestionsWithStyleType:reply:"
+ "getAllKnownLibraryPathsWithReply:"
+ "getBytes:range:"
+ "getLibraryServicesStateByLibraryBundleWithReply:"
+ "getLibrarySizesFromDB:error:"
+ "getPhotoLibraryIdentifierWithReply:"
+ "hasError"
+ "iCPLRemainingQuotaBytes"
+ "iCPLTotalPhotosStorageBytes"
+ "iCPLTotalStorageBytes"
+ "ingestItemWithCoreSpotlightUniqueIdentifier:bundleID:purgeUrgency:error:"
+ "ingestItemWithCoreSpotlightUniqueIdentifier:bundleID:purgeUrgency:reply:"
+ "initWithAssetUuid:bundleScope:uti:resourceVersion:resourceType:recipeID:originalFilename:customSuffix:"
+ "initWithLogicalScreenSize:screenScale:deviceClass:supportsASTC:"
+ "isExceedingiCPLQuota"
+ "kPLImageWriterSharingRestriction"
+ "libraryServicesStateByBundlePathWithCompletion:"
+ "manualAlbumsCreatedByAppleCount"
+ "manualAlbumsCreatedByThirdPartiesCount"
+ "mapSavedAssetType:unknown:photoBooth:photoStream:camera:cloudShared:cameraConnectionKit:cloudPhotoLibrary:wallpaper_UNUSED:momentShared:placeholder:referenced:alternate:guest:companionSynced:recovered:legacyImport:collectionShare:unrecognized:"
+ "maskForAllowedForSceneAnalysis"
+ "maskForAssetsEligibleForCPLSharingScopes"
+ "maskForAssetsEligibleForCPLTransportWithoutSharedScopesAndPlaceholders"
+ "maskForAssetsEligibleForCollectionShareRelationship"
+ "maskForCollectionShareAsset"
+ "openAndWaitWithUpgrade:error:"
+ "persistentHistoryChangeCount"
+ "photoLibraryIdentifierWithError:"
+ "photosMessagesEntitled"
+ "position"
+ "readDataAtIndex:intoBuffer:bytesRead:"
+ "readImageDataAtIndex:intoBuffer:bytesRead:imageWidth:imageHeight:imageDataWidth:imageDataHeight:startingOffset:bytesPerRow:uuidBytes:"
+ "realPathsFromPaths:includeUnresolved:"
+ "reportInvitationAsSpamForCollectionShareWithUUID:completionHandler:"
+ "reportInvitationAsSpamForCollectionShareWithUUID:reply:"
+ "resources/derivatives/cvt"
+ "savedAssetTypeForCollectionShareAsset"
+ "sendInvitationsForCollectionShareWithUUID:participantUUIDs:completionHandler:"
+ "sendInvitationsForCollectionShareWithUUID:participantUUIDs:reply:"
+ "setPosition:"
+ "subpathWithLast:pathComponentsFromURL:"
+ "systemPhotoLibraryURL"
+ "updateInitialSuggestionsWithIdentifiers:dateLastUsed:error:"
+ "updateInitialSuggestionsWithIdentifiers:dateLastUsed:reply:"
+ "v164@0:8s16@?20@?28@?36@?44@?52@?60@?68@?76@?84@?92@?100@?108@?116@?124@?132@?140@?148@?156"
+ "v16@?0@\"<PLAssetsdNonBindingDebugServiceProtocol>\"8"
+ "v24@0:8@?<v@?@\"PLPhotoLibraryIdentifier\"@\"NSError\">16"
+ "v40@0:8@\"NSArray\"16@\"NSDate\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?B@\"NSError\">32"
+ "v48@0:8@\"NSString\"16@\"NSString\"24q32@?<v@?@\"NSString\"@\"NSError\">40"
+ "v48@0:8@16@24q32@?40"
+ "validatedSavedAssetTypeMaskUnknown:photoBooth:photoStream:camera:cloudShared:cameraConnectionKit:cloudPhotoLibrary:wallpaper_UNUSED:momentShared:placeholder:referenced:alternate:guest:companionSynced:recovered:collectionShare:legacyImport:"
- "%@ progressUnits=%ld req=%@ qos=%@"
- "%{public}@: Completed operation %{public}@ in %f seconds with QoS %{public}@"
- "%{public}@: Starting operation %{public}@ with QoS %{public}@"
- "%{public}@: progress becoming current: %@"
- "%{public}@: progress resigned current: %@"
- "'%@' (progress=%1.1f units=%ld req=%@ qos=%@)"
- "*** Not enough space to take a picture. Available space is %lld"
- "-[PLAssetsdCloudInternalClient runComputeSyncBackfillMigrationSynchronously]_block_invoke"
- "-[PLAssetsdDebugClient assetContainmentLargeFaceThresholdUserDefaultWithError:]_block_invoke"
- "-[PLAssetsdDebugClient assetContainmentSmallFaceThresholdUserDefaultWithError:]_block_invoke"
- "-[PLAssetsdDebugClient assetContainmentSmallTorsoThresholdUserDefaultWithError:]_block_invoke"
- "-[PLAssetsdDebugClient getStatus]_block_invoke"
- "-[PLAssetsdDebugClient setAssetContainmentLargeFaceThreshold:error:]_block_invoke"
- "-[PLAssetsdDebugClient setAssetContainmentSmallFaceThreshold:error:]_block_invoke"
- "-[PLAssetsdDebugClient setAssetContainmentSmallTorsoThreshold:error:]_block_invoke"
- "-[PLAssetsdDebugClient synchronouslySetSearchIndexPaused:reason:error:]_block_invoke"
- "-[PLAssetsdLibraryInternalClient invalidateBehavioralScoreOnAllAssetsWithError:]_block_invoke"
- "@\"NSProgress\""
- "@56@0:8@16@24q32@40@?48"
- "@56@0:8@16S24@28I36I40I44@48"
- "@56@0:8{CGSize=dd}16d32^v40B48B52"
- "@64@0:8{CGSize=dd}16q32d40d48^{CGSize=dd}56"
- "@80@0:8{CGSize=dd}16q32q40d48d56@?64^{CGSize=dd}72"
- "B32@0:8d16^@24"
- "B36@0:8B16^@20^@28"
- "B40@0:8Q16^{tagPLPositionalTableMemoryPoolNode=^v^{tagPLPositionalTableMemoryPool}B^{tagPLPositionalTableMemoryPoolNode}}24^Q32"
- "B72@0:8{CGSize=dd}16q32d40{CGSize=dd}48d64"
- "B96@0:8Q16^{tagPLPositionalTableMemoryPoolNode=^v^{tagPLPositionalTableMemoryPool}B^{tagPLPositionalTableMemoryPoolNode}}24^Q32^i40^i48^i56^i64^q72^Q80^{?=CCCCCCCCCCCCCCCC}88"
- "Couldn't archive supportingData dictionary for search graph update with archiver error: %{public}@"
- "CrashRecovery: Repair interrupted locked resource transfer"
- "Data at path %@ was corrupt; forcing +[NSKeyedUnarchiver unarchivedObjectOfClass:fromData:error:] to return nil, error: %@"
- "Data at path %@ was corrupt; forcing +[NSKeyedUnarchiver unarchivedObjectOfClasses:fromData:error:] to return nil, error: %@"
- "DiskSpaceWasLow"
- "EDT_%04ld"
- "EditedVideoLastFileGroupNumber-%@"
- "Error getting library sizes fromDB: %d, error: %@"
- "Expect only pool nodes to be dequeued."
- "Failed to get library sizes with error: %@"
- "Failed to retrieve file attributes for %@, %@"
- "Failed to retrieve volume attributes for %@, %@"
- "GridInlinePlayback"
- "I80@0:8B16B20B24B28B32B36B40B44B48B52B56B60B64B68B72B76"
- "LSM is nil, not executing operation %@"
- "LockScreenCamera"
- "Locked"
- "PLLibraryServicesOperation"
- "PLPositionalTableAllocator.m"
- "PLXPC Client: applySearchIndexGraphUpdates:supportingData:completionHandler:"
- "PLXPC Client: assetContainmentLargeFaceThresholdUserDefaultWithError:"
- "PLXPC Client: assetContainmentSmallFaceThresholdUserDefaultWithError:"
- "PLXPC Client: assetContainmentSmallTorsoThresholdUserDefaultWithError:"
- "PLXPC Client: deleteEmbeddings:assetUUID:completionHandler:"
- "PLXPC Client: insertEmbeddings:modelType:assetUUID:completionHandler:"
- "PLXPC Client: invalidateBehavioralScoreOnAllAssetsWithError:"
- "PLXPC Client: runComputeSyncBackfillMigrationSynchronously"
- "PLXPC Client: setAssetContainmentLargeFaceThreshold:error:"
- "PLXPC Client: setAssetContainmentSmallFaceThreshold:error:"
- "PLXPC Client: setAssetContainmentSmallTorsoThreshold:error:"
- "PLXPC Client: synchronouslyGetLibrarySizesFromDB:sizes:error:"
- "PLXPC Client: synchronouslySetSearchIndexPaused:reason:error:"
- "PathToPhotoKit"
- "Pausing search indexing no longer supported.  To signal that there may be search indexing work that needs to be done, register the background job service using registerBackgroundJobServiceIfNecessaryOnLibraryPath.  To force search indexing, use forceRunBackgroundJobsOnLibraryPath"
- "PhotosMessagesApp"
- "PhotosPicker"
- "PhotosSearchBackgroundJobWorker"
- "Q156@0:8s16Q20Q28Q36Q44Q52Q60Q68Q76Q84Q92Q100Q108Q116Q124Q132Q140Q148"
- "Spotlight"
- "T@\"NSProgress\",&,N,V_progress"
- "T@\"NSString\",&,N,V_originalFilename"
- "T@\"NSString\",C,V_logPrefix"
- "T@\"NSString\",R,C,N"
- "TB,N,V_isMigrationService"
- "TVPhotos"
- "T^{tagPLPositionalTableMemoryPool={?=^vq}Qi^v^vQ},R,N,V_pool"
- "Tq,N,V_progressPercentOfTotal"
- "Tq,N,V_requiredState"
- "Unable to allocate requested PLPositionalTablePool at size: %ld, using standard alloc."
- "Unable to fetch moment share from share url: %@. (%@)"
- "[1-9][0-9][0-9]APPLE"
- "^{tagPLPositionalTableMemoryPool={?=^vq}Qi^v^vQ}"
- "^{tagPLPositionalTableMemoryPool={?=^vq}Qi^v^vQ}16@0:8"
- "_actuallyUpdateCookie"
- "_bestFormatWithSize:specificVersionType:contentMode:demoteFactor:srcAspectRatio:hasAdjustmentsHandler:desiredImagePixelSize:"
- "_bytesRequiredForPhoto"
- "_canDegradeToFormat:"
- "_desiredImageSizeForRequestedViewSizeInPixels:isAspectFill:srcAspectRatio:"
- "_diskSpaceDidBecomeLow"
- "_fastestDegradedFormatFallingBackFromFormat:"
- "_flags"
- "_isAcceptableForViewSize:contentMode:sourceAspectRatio:desiredImageSize:demoteFactor:"
- "_isMigrationService"
- "_lastFSCheck"
- "_lockedDirectory"
- "_nextLargestAcceptableFormatForFormat:"
- "_pool"
- "_progressPercentOfTotal"
- "_requiredState"
- "_runOperationBlock:"
- "_scopesLockedDirectory"
- "_standardDegradedFormatFallingBackFromFormat:"
- "_updateCookie"
- "addChild:withPendingUnitCount:"
- "addExecutionBlock:"
- "applyGraphUpdates:supportingData:reply:"
- "applySearchIndexGraphUpdates:supportingData:completionHandler:"
- "assetContainmentLargeFaceThresholdUserDefault:"
- "assetContainmentLargeFaceThresholdUserDefaultWithError:"
- "assetContainmentSmallFaceThresholdUserDefault:"
- "assetContainmentSmallFaceThresholdUserDefaultWithError:"
- "assetContainmentSmallTorsoThresholdUserDefault:"
- "assetContainmentSmallTorsoThresholdUserDefaultWithError:"
- "becomeCurrentWithPendingUnitCount:"
- "bytesToAutomaticallyClear"
- "chooseFormatsForSize:specificVersionType:contentMode:demoteFactor:srcAspectRatio:degradedFormatPolicy:hasAdjustmentsHandler:desiredImagePixelSize:bestFormat:degradedFormat:"
- "deleteEmbeddings:assetUUID:completionHandler:"
- "deleteEmbeddings:assetUUID:reply:"
- "derivativeFormatThatFitsSize:contentMode:demoteFactor:srcAspectRatio:desiredImagePixelSize:"
- "destinationURL"
- "discreteProgressWithTotalUnitCount:"
- "executeBlockForSavedAssetType:unknown:photoBooth:photoStream:camera:cloudShared:cameraConnectionKit:cloudPhotoLibrary:wallpaper_UNUSED:momentShared:placeholder:referenced:alternate:guest:companionSynced:recovered:legacyImport:unrecognized:"
- "fractionCompleted"
- "graphUpdates"
- "hasDiskSpaceToCopyFileAtURL:toVolumeAtURL:error:"
- "hasEnoughDiskToTakePicture"
- "initWithAssetUuid:bundleScope:uti:resourceVersion:resourceType:recipeID:originalFilename:"
- "initWithLogicalScreenSize:screenScale:deviceClass:supportsASTC:isMigrationService:"
- "initWithPattern:options:error:"
- "insertEmbeddings:modelType:assetUUID:completionHandler:"
- "insertEmbeddings:modelType:assetUUID:reply:"
- "invalidateBehavioralScoreOnAllAssetsWithError:"
- "invalidateBehavioralScoreOnAllAssetsWithReply:"
- "isCameraDirectoryFolderName:"
- "isImportDirectoryFolderName:"
- "isMigrationService"
- "locked"
- "mapSavedAssetType:unknown:photoBooth:photoStream:camera:cloudShared:cameraConnectionKit:cloudPhotoLibrary:wallpaper_UNUSED:momentShared:placeholder:referenced:alternate:guest:companionSynced:recovered:legacyImport:unrecognized:"
- "maskForAssetsEligibleForCloudKitTransportWithoutMomentSharesAndPlaceholders"
- "maskForMomentShareDeDupe"
- "maxLivePhotoDataSize"
- "nextAvailableFilePathInDirectory:withExtension:"
- "no node."
- "numberOfMatchesInString:options:range:"
- "operation %@ progress: %@"
- "operationWithName:libraryServicesManager:requiredState:parentProgress:executionBlock:"
- "pLzf7OiX5nWAPUMj7BfI4Q"
- "performSelectorOnMainThread:withObject:waitUntilDone:"
- "pl_safeUnarchiveObjectFromFile:class:"
- "pl_safeUnarchiveObjectFromFile:classes:"
- "pool"
- "progressPercentOfTotal"
- "readDataAtIndex:intoPoolNode:bytesRead:"
- "readImageDataAtIndex:intoPoolNode:bytesRead:imageWidth:imageHeight:imageDataWidth:imageDataHeight:startingOffset:bytesPerRow:uuidBytes:"
- "removeObserver:"
- "requiredState"
- "resignCurrent"
- "runComputeSyncBackfillMigrationSynchronously"
- "setAssetContainmentLargeFaceThreshold:"
- "setAssetContainmentLargeFaceThreshold:error:"
- "setAssetContainmentSmallFaceThreshold:"
- "setAssetContainmentSmallFaceThreshold:error:"
- "setAssetContainmentSmallTorsoThreshold:"
- "setAssetContainmentSmallTorsoThreshold:error:"
- "setExecutionBlockFromOperationBlock:"
- "setIsMigrationService:"
- "setLogPrefix:"
- "setOriginalFilename:"
- "setProgressPercentOfTotal:"
- "setRequiredState:"
- "setShouldSuppressLogging:"
- "shouldSuppressLogging"
- "sizes"
- "statusDescription"
- "synchronouslyGetLibrarySizesFromDB:sizes:error:"
- "synchronouslySetSearchIndexPaused:reason:error:"
- "totalUnitCount"
- "updateAvailableDiskSpace"
- "v104@0:8{CGSize=dd}16q32q40d48d56q64@?72^{CGSize=dd}80^@88^@96"
- "v156@0:8s16@?20@?28@?36@?44@?52@?60@?68@?76@?84@?92@?100@?108@?116@?124@?132@?140@?148"
- "v24@0:8@?<v@?d@\"NSError\">16"
- "v24@?0d8@\"NSError\"16"
- "v40@0:8@\"NSDictionary\"16@\"NSData\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSIndexSet\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "v48@0:8@\"NSArray\"16Q24@\"NSString\"32@?<v@?B@\"NSError\">40"
- "validatedSavedAssetTypeMaskUnknown:photoBooth:photoStream:camera:cloudShared:cameraConnectionKit:cloudPhotoLibrary:wallpaper_UNUSED:momentShared:placeholder:referenced:alternate:guest:companionSynced:recovered:legacyImport:"
- "void PLPositionalTableMemoryPool_Destroy(PLPositionalTableMemoryPool *)"
- "void PLPositionalTableMemoryPool_Free(PLPositionalTableMemoryPoolNode *)"
- "{?=\"needToCheckDiskSpace\"b1\"probablyLowOnDiskSpace\"b1\"isAssetsd\"b1\"extra\"b28}"
- "{CGSize=dd}44@0:8{CGSize=dd}16B32d36"

```
