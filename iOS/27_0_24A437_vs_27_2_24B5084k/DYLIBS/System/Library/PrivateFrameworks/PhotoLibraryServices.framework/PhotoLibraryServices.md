## PhotoLibraryServices

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices`

```diff

-912.0.235.0.0
-  __TEXT.__text: 0x74991c
+916.40.110.0.0
+  __TEXT.__text: 0x73f8b0
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x45d94
-  __TEXT.__const: 0x7670
+  __TEXT.__objc_methlist: 0x4530c
+  __TEXT.__const: 0x74f0
   __TEXT.__dlopen_cstrs: 0xb28
   __TEXT.__swift5_typeref: 0x131a
-  __TEXT.__cstring: 0x6db46
+  __TEXT.__cstring: 0x6d7ad
   __TEXT.__swift5_capture: 0x188c
   __TEXT.__constg_swiftt: 0x400
   __TEXT.__swift5_builtin: 0xc8

   __TEXT.__swift5_assocty: 0xd8
   __TEXT.__swift5_proto: 0xa4
   __TEXT.__swift5_types: 0x54
-  __TEXT.__oslogstring: 0x86d3e
+  __TEXT.__oslogstring: 0x86c6f
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__gcc_except_tab: 0x20844
+  __TEXT.__gcc_except_tab: 0x2065c
   __TEXT.__ustring: 0xa3a
-  __TEXT.__unwind_info: 0x1b088
-  __TEXT.__eh_frame: 0x11c8
+  __TEXT.__unwind_info: 0x1acf0
+  __TEXT.__eh_frame: 0x11a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x16900
-  __DATA_CONST.__objc_classlist: 0x2420
+  __DATA_CONST.__const: 0x16778
+  __DATA_CONST.__objc_classlist: 0x23e8
   __DATA_CONST.__objc_catlist: 0xf8
-  __DATA_CONST.__objc_protolist: 0x760
+  __DATA_CONST.__objc_protolist: 0x768
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x25618
+  __DATA_CONST.__objc_selrefs: 0x250f8
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0x1598
-  __DATA_CONST.__objc_arraydata: 0x1de0
-  __DATA_CONST.__got: 0x52e0
-  __AUTH_CONST.__const: 0xa6d8
-  __AUTH_CONST.__cfstring: 0x53b20
-  __AUTH_CONST.__objc_const: 0x70938
+  __DATA_CONST.__objc_superrefs: 0x1590
+  __DATA_CONST.__objc_arraydata: 0x1dc0
+  __DATA_CONST.__got: 0x5298
+  __AUTH_CONST.__const: 0xa5b8
+  __AUTH_CONST.__cfstring: 0x532c0
+  __AUTH_CONST.__objc_const: 0x70608
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__objc_intobj: 0x5448
-  __AUTH_CONST.__objc_arrayobj: 0x1500
+  __AUTH_CONST.__objc_intobj: 0x5418
+  __AUTH_CONST.__objc_arrayobj: 0x14d0
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x320
   __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH_CONST.__auth_got: 0x2b58
-  __AUTH.__objc_data: 0x136a0
+  __AUTH_CONST.__auth_got: 0x2b38
+  __AUTH.__objc_data: 0x13470
   __AUTH.__data: 0x350
-  __DATA.__objc_ivar: 0x3e58
-  __DATA.__data: 0x7074
+  __DATA.__objc_ivar: 0x3e48
+  __DATA.__data: 0x7084
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0x3520
   __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0x1e0
+  __DATA_DIRTY.__bss: 0x180
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 29549
-  Symbols:   65269
-  CStrings:  22065
+  Functions: 29249
+  Symbols:   64867
+  CStrings:  21974
 
Symbols:
+ +[PLBackgroundJobHighPrioritySearchIndexingWorker _allCriteriaToUse]
+ +[PLBackgroundJobLowPrioritySearchIndexingWorker _allCriteriaToUse]
+ +[PLBackgroundJobLowPrioritySearchIndexingWorker optOutOfPendingWorkCache]
+ +[PLBackgroundJobSearchIndexingWorker _allCriteriaToUse]
+ +[PLBackgroundJobWorkerTypes backgroundJobWorkerTypesMaskGuestAssetSync:personSync:syndicationSync:syndicationResourceSanitization:syndicationResourceDownload:syndicationAssetCleanup:assetStack:duplicateDetector:deferredRenderDerivativesLowPriority:deferredRenderDerivativesHighPriority:resourceAvailability:stableHash:editRenderingImage:editRenderingVideo:highPrioritySearchIndexing:lowPrioritySearchIndexing:sharedAssetContainerUpdate:assetResourceUploadJob:assetResourceUploadExtensionRunner:featureAvailability:optimizeTableThumbs:cascadeDonation:provenanceTimestamp:]
+ +[PLCollectionShare _allAssetsAreSavedToLibraryForCollectionShare:inContext:]
+ +[PLCollectionShare countOfSharesWithUnreadBadgeActivitySinceLastSeenDate:eventLogDate:inManagedObjectContext:]
+ +[PLCollectionShare predicateForMigratedCPLCollectionShares]
+ +[PLFeatureAvailabilityLexemeCriteria featureAnalysisLexemeCategories]
+ +[PLImageWriter copyJobContentsToHoldingDirectoryWithUUID:incomingPath:job:]
+ +[PLManagedAsset(Share) _cloneResourcesForSharePlaceholderAsset:sourceAsset:shouldBakeInAdjustments:shouldFlattenLivePhoto:withPlaceholderResourceURLToSourceResourceURLMap:fileManager:photoLibrary:]
+ +[PLPhotoLibraryBundleController _formatMemoryBytes:]
+ +[PLSearchEntity confidenceForMomentEdge:]
+ +[PLShareParticipant _enumerateUnattributedCPLContributorContentInPhotoLibrary:usingBlock:]
+ +[PLShareParticipant _objectsMatchingPredicate:entityName:inManagedObjectContext:]
+ +[PLShareParticipant linkCPLContributorContentWithUserIdentifiers:inPhotoLibrary:]
+ +[PLShareParticipant orphanedCPLContributorRecordsInPhotoLibrary:]
+ +[PLSharePost predicateForPostsFromOthersCreatedAfterSubscriptionSinceDate:]
+ +[PLSyndicationResourceDataStore _copyProvidedFilesForItemIdentifier:providerURL:primaryDestination:videoComplementDestination:pathManager:materializesDatalessFiles:resultHandler:]
+ +[PLSyndicationResourceDataStore _provideSourceURLsForBundleID:syndicationIdentifier:typeIdentifier:isLivePhoto:options:completionHandler:]
+ +[PLSyndicationResourceDataStore provideFileURLAndUnwrapLivePhotoIfNeededForItemIdentifiersWithBundleIDs:destURLs:pathManager:options:resultHandler:completionHandler:]
+ +[PLSyndicationResourceFileCoordinator _errorForCopyFailure:sourceURL:]
+ +[PLSyndicationResourceFileCoordinator _unpackLivePhotoBundleAtURL:primaryURL:videoComplementURL:error:]
+ -[PLAbstractLibraryServicesManagerService isAuthorizedAssetUUID:inManagedObjectContext:]
+ -[PLAssetsdLibraryInternalService getSearchDonationProgressShouldCompute:shouldReport:reply:]
+ -[PLAssetsdNonBindingDebugService getStateCaptureDictionaryWithReply:]
+ -[PLAssetsdPhotoKitService executeQueryForSyncManager:type:startDate:endDate:itemsHandler:completionHandler:]
+ -[PLBackgroundJobCascadeDonationWorker workItemsNeedingProcessingInLibrary:currentCriteria:]
+ -[PLBackgroundJobDeferredRenderDerivativesBaseWorker workItemsNeedingProcessingInLibrary:currentCriteria:]
+ -[PLBackgroundJobDuplicateDetectorWorker workItemsNeedingProcessingInLibrary:currentCriteria:]
+ -[PLBackgroundJobEditRenderingWorker workItemsNeedingProcessingInLibrary:currentCriteria:]
+ -[PLBackgroundJobFeatureAvailabilityWorker workItemsNeedingProcessingInLibrary:currentCriteria:]
+ -[PLBackgroundJobGuestAssetSyncWorker workItemsNeedingProcessingInLibrary:currentCriteria:]
+ -[PLBackgroundJobLowPrioritySearchIndexingWorker _jobTypes]
+ -[PLBackgroundJobLowPrioritySearchIndexingWorker _supportsIndexRebuild]
+ -[PLBackgroundJobLowPrioritySearchIndexingWorker locrIdentifyingBlock]
+ -[PLBackgroundJobLowPrioritySearchIndexingWorker type]
+ -[PLBackgroundJobOptimizeTableThumbsWorker workItemsNeedingProcessingInLibrary:currentCriteria:]
+ -[PLBackgroundJobPersonSyncWorker workItemsNeedingProcessingInLibrary:currentCriteria:]
+ -[PLBackgroundJobResourceAvailabilityWorker workItemsNeedingProcessingInLibrary:currentCriteria:]
+ -[PLBackgroundJobResourceUploadExtensionRunnerWorker criteriaNeedingProcessingInLibrary:currentCriteria:outSignalAgainDate:]
+ -[PLBackgroundJobResourceUploadExtensionRunnerWorker workItemsNeedingProcessingInLibrary:currentCriteria:]
+ -[PLBackgroundJobSearchIndexingWorker criteriaNeedingProcessingInLibrary:currentCriteria:outSignalAgainDate:]
+ -[PLBackgroundJobSearchIndexingWorker workItemsNeedingProcessingInLibrary:currentCriteria:]
+ -[PLBackgroundJobService _getProcessingSetURL]
+ -[PLBackgroundJobService _inq_pendingJobsForBundle:workerTypes:currentCriteria:]
+ -[PLBackgroundJobService _inq_pendingJobsOnBuffer:currentCriteria:]
+ -[PLBackgroundJobService _inq_pendingJobsOnBundles:currentCriteria:]
+ -[PLBackgroundJobSharedAssetContainerUpdateWorker workItemsNeedingProcessingInLibrary:currentCriteria:]
+ -[PLBackgroundJobStableHashWorker workItemsNeedingProcessingInLibrary:currentCriteria:]
+ -[PLBackgroundJobSyndicationAssetCleanupWorker workItemsNeedingProcessingInLibrary:currentCriteria:]
+ -[PLBackgroundJobSyndicationResourceSanitizationWorker workItemsNeedingProcessingInLibrary:currentCriteria:]
+ -[PLBackgroundJobSyndicationSyncWorker workItemsNeedingProcessingInLibrary:currentCriteria:]
+ -[PLBackgroundJobWorker _forcefullyInvokeCurrentManagedObjectCompletionHandler]
+ -[PLBackgroundJobWorker criteriaNeedingProcessingInLibrary:currentCriteria:outSignalAgainDate:]
+ -[PLBackgroundJobWorker pendingCriteriaInLibrary:currentCriteria:outSignalAgainDate:]
+ -[PLBackgroundJobWorker pendingWorkItemsInLibrary:currentCriteria:]
+ -[PLBackgroundJobWorker workItemsNeedingProcessingInLibrary:currentCriteria:]
+ -[PLBackgroundJobWorkerPendingWorkItems initWithZeroWorkItemsForCurrentCriteria]
+ -[PLBackgroundJobWorkerPendingWorkItems setZeroWorkItemsForCurrentCriteria:]
+ -[PLBackgroundJobWorkerPendingWorkItems zeroWorkItemsForCurrentCriteria]
+ -[PLBackgroundJobWorkerTypesBuffer redactedDescription]
+ -[PLCPLSettings hasPersistedPrefetchMode]
+ -[PLCPLSettings libraryIdentifier]
+ -[PLCPLSettings setPrefetchModeSchedulingResourceUpdate:error:]
+ -[PLCloudPhotoLibraryManager _applyDefaultPrefetchModeIfNeededWithCPLSettings:createOptions:]
+ -[PLCloudPhotoLibraryManager _collectContributorUserIdentifiersForRecords:into:completionHandler:]
+ -[PLCloudPhotoLibraryManager _linkOrphanedCollectionShareContributorsWithCPLSettings:]
+ -[PLCloudSharedComment _updateShareParticipantWithContributorUserIdentifier:collectionShare:inPhotoLibrary:]
+ -[PLCloudSharedComment updateCommentText:]
+ -[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:searchProgressOnly:completionHandler:]
+ -[PLFeatureAvailabilityComputer computeSearchProgressForPhotoLibrary:completionHandler:]
+ -[PLFeatureAvailabilityLexemeCriteria .cxx_destruct]
+ -[PLFeatureAvailabilityLexemeCriteria _defaultResult]
+ -[PLFeatureAvailabilityLexemeCriteria _imageCaptionDefaultsToCurrent]
+ -[PLFeatureAvailabilityLexemeCriteria _imageEmbeddingDefaultsToCurrent]
+ -[PLFeatureAvailabilityLexemeCriteria _mediaAnalysisImageDefaultsToCurrent]
+ -[PLFeatureAvailabilityLexemeCriteria _richImageCaptionDefaultsToCurrent]
+ -[PLFeatureAvailabilityLexemeCriteria evaluateLexemeIDs:]
+ -[PLFeatureAvailabilityLexemeCriteria evaluateLexemeIDsByCategoryDictionary:foundUnrecognizedLexemeID:]
+ -[PLFeatureAvailabilityLexemeCriteria initWithLexemes:versionProvider:]
+ -[PLGraphNode uuidDescription]
+ -[PLIntensiveResourceTask _lock_addResponder:]
+ -[PLIntensiveResourceTask _lock_isRunning]
+ -[PLIntensiveResourceTask transitionToUninterruptible]
+ -[PLIntensiveResourceTask tryPreparingForReplacementWithNewResponder:existingResponders:existingProgress:]
+ -[PLManagedAsset _generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:retryNumber:allowCancellationByService:clientBundleID:shouldSaveMediaConversionResultBlock:completion:]
+ -[PLManagedAsset _setKeywordsFromMetadata:]
+ -[PLManagedAsset _setRatingFromMetadata:]
+ -[PLManagedAsset generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:allowCancellationByService:clientBundleID:shouldSaveMediaConversionResultBlock:completion:]
+ -[PLManagedAsset updateImageExtendedGenerativeAttributesFromMetadata:policy:]
+ -[PLManagedAsset(DeferredPhotoProcessing) installFinalImageOrVideoAndRemoveDeferredFilesWithFinalImageURL:previewImage:thumbnailImage:useExistingAsset:outError:]
+ -[PLManagedAsset(Share) setupPlaceholderAssetWithRequiredPropertiesFromSourceAsset:placeholderAssetUUID:bundleScope:share:importSessionID:bakeInAdjustmentsFromSourceAsset:flattenLivePhoto:copyTitleDescriptionAndKeywords:copyCameraProcessingAdjustmentResources:copyLocationData:copyProvenanceData:isCurrentUser:library:]
+ -[PLManagedObjectPagingIterator countRemainingWithManagedObjectContext:]
+ -[PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing _assetHasOriginalFileOnDisk:]
+ -[PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing _clearDeferredProcessingNeededForAsset:originalWidth:originalHeight:]
+ -[PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing _originalPrimaryImageResourceForAsset:]
+ -[PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing _processCapturePipelineAsset:originalResource:reingested:]
+ -[PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing _processSemanticEnhanceAsset:originalResource:]
+ -[PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing performActionWithManagedObjectContext:error:]
+ -[PLModelMigrationAction_ReevaluateAllowedForAnalysisForUnknownKindAssets performActionWithManagedObjectContext:error:]
+ -[PLModelMigrationAction_SetKeepOriginalsPrefetchModeForVisualIntelligenceLibrary performActionWithManagedObjectContext:error:]
+ -[PLModelMigrationAction_SetRunOnceFlagToLinkOrphanedCollectionShareContributors performActionWithManagedObjectContext:error:]
+ -[PLNotificationManager kvsListenerDidUpdateEventLogLastEnteredDate:]
+ -[PLNotificationManager kvsListenerDidUpdateLastSeenDate:]
+ -[PLNotificationManager kvsListener]
+ -[PLNotificationManager setKvsListener:]
+ -[PLPhotoAnalysisServiceClient(Vision) cancelVisionOperationWithId:]
+ -[PLPhotoLibraryBundleController _updateStateCaptureInfo:libraryID:]
+ -[PLPhotoLibraryBundleController stateCaptureDictionary]
+ -[PLPrimaryResourceDataStoreUniformFileKey representsNonRawImage]
+ -[PLProgressFollower _syncOutputProgress:toSourceProgress:]
+ -[PLRebuildUserNotification initWithMessage:libraryPath:]
+ -[PLRebuildUserNotification libraryPath]
+ -[PLResourceDataStoreKey representsNonRawImage]
+ -[PLSearchIndexingEngine _calculateDonationCountsFromSnapshot:resultHandler:]
+ -[PLSearchIndexingEngine getSearchDonationProgressInLibrary:shouldCompute:shouldReport:completionHandler:]
+ -[PLSearchIndexingEngine supportsSearchProgressReporting]
+ -[PLSearchIndexingEngineLibraryServicesProvider _createLogger]
+ -[PLSearchIndexingEngineLibraryServicesProvider availabilityComputer]
+ -[PLSearchIndexingEngineLibraryServicesProvider logger]
+ -[PLSearchIndexingRebuildEngine _inq_performRebuildForLibrary:completion:]
+ -[PLShare _cplParticipantsWithBlockedIdentitiesLast:]
+ -[PLShareParticipant _objectsMatchingPredicate:entityName:]
+ -[PLShareParticipant reconcileOrphanedRelationshipsWithCPLCollectionShare:]
+ -[PLSharePost updateCaption:]
+ -[PLSharedAlbumsActivityKVSListener .cxx_destruct]
+ -[PLSharedAlbumsActivityKVSListener _keyValueStoreDidChangeExternally:]
+ -[PLSharedAlbumsActivityKVSListener _updateCachedEventLogLastEnteredDate]
+ -[PLSharedAlbumsActivityKVSListener _updateCachedLastSeenDate]
+ -[PLSharedAlbumsActivityKVSListener dealloc]
+ -[PLSharedAlbumsActivityKVSListener delegate]
+ -[PLSharedAlbumsActivityKVSListener eventLogLastEnteredDate]
+ -[PLSharedAlbumsActivityKVSListener init]
+ -[PLSharedAlbumsActivityKVSListener isListening]
+ -[PLSharedAlbumsActivityKVSListener kvStore]
+ -[PLSharedAlbumsActivityKVSListener lastSeenDate]
+ -[PLSharedAlbumsActivityKVSListener setDelegate:]
+ -[PLSharedAlbumsActivityKVSListener setIsListening:]
+ -[PLSharedAlbumsActivityKVSListener setKvStore:]
+ -[PLSharedAlbumsActivityKVSListener startListening]
+ -[PLSharedAlbumsActivityKVSListener stopListening]
+ -[PLSharedStreamsDataStoreKey representsNonRawImage]
+ -[PLSyndicationResourceDataStore _copyAndMarkAsLocallyAvailablePairedLivePhotoResourceForRequestedResource:requestedVideoComplement:fileCoordinator:error:]
+ -[PLSyndicationResourceDataStore _copyProviderFileWantsVideoComplement:fromCoordinator:fileIdentifier:pathManager:copiedURL:inode:error:]
+ -[PLSyndicationResourceFileCoordinator .cxx_destruct]
+ -[PLSyndicationResourceFileCoordinator _coordinateReadingSourcesWithError:accessor:]
+ -[PLSyndicationResourceFileCoordinator _copyFileAtURL:toDestination:error:]
+ -[PLSyndicationResourceFileCoordinator _isDestinationURLInsideSyndicationOriginals:]
+ -[PLSyndicationResourceFileCoordinator _safeCopyItemAtURL:toURLAndReplaceIfNeeded:error:]
+ -[PLSyndicationResourceFileCoordinator copiedPrimaryURL]
+ -[PLSyndicationResourceFileCoordinator copiedVideoComplementURL]
+ -[PLSyndicationResourceFileCoordinator copyToPrimaryDestination:videoComplementDestination:error:]
+ -[PLSyndicationResourceFileCoordinator initWithSourceURL:videoComplementSourceURL:pathManager:materializesDatalessFiles:]
+ -[PLSyndicationResourceFileCoordinator materializesDatalessFiles]
+ -[PLSyndicationResourceFileCoordinator originalFilename]
+ -[PLSyndicationResourceFileCoordinator pathManager]
+ -[PLSyndicationResourceFileCoordinator sourceURL]
+ -[PLSyndicationResourceFileCoordinator videoComplementFilename]
+ -[PLSyndicationResourceFileCoordinator videoComplementSourceURL]
+ -[PLSyndicationSyncServiceWrapper executeQueryForSyncManager:type:startDate:endDate:itemsHandler:completionHandler:]
+ -[PLTaggedPointerDataStoreKey representsNonRawImage]
+ -[PLThumbnailResourceDataStoreKey representsNonRawImage]
+ GCC_except_table10007
+ GCC_except_table10014
+ GCC_except_table10042
+ GCC_except_table10047
+ GCC_except_table10053
+ GCC_except_table10057
+ GCC_except_table1006
+ GCC_except_table10060
+ GCC_except_table10068
+ GCC_except_table1007
+ GCC_except_table10070
+ GCC_except_table10079
+ GCC_except_table10090
+ GCC_except_table10153
+ GCC_except_table10173
+ GCC_except_table10187
+ GCC_except_table10191
+ GCC_except_table10203
+ GCC_except_table10215
+ GCC_except_table10227
+ GCC_except_table10229
+ GCC_except_table10243
+ GCC_except_table10245
+ GCC_except_table10252
+ GCC_except_table10260
+ GCC_except_table10285
+ GCC_except_table10290
+ GCC_except_table10313
+ GCC_except_table10325
+ GCC_except_table10334
+ GCC_except_table10342
+ GCC_except_table10376
+ GCC_except_table10387
+ GCC_except_table10462
+ GCC_except_table10470
+ GCC_except_table10472
+ GCC_except_table10478
+ GCC_except_table10482
+ GCC_except_table10484
+ GCC_except_table10490
+ GCC_except_table10519
+ GCC_except_table10526
+ GCC_except_table10546
+ GCC_except_table10577
+ GCC_except_table10580
+ GCC_except_table106
+ GCC_except_table10632
+ GCC_except_table1064
+ GCC_except_table10683
+ GCC_except_table10695
+ GCC_except_table10697
+ GCC_except_table10717
+ GCC_except_table10719
+ GCC_except_table10730
+ GCC_except_table10735
+ GCC_except_table10738
+ GCC_except_table10742
+ GCC_except_table10761
+ GCC_except_table1085
+ GCC_except_table10891
+ GCC_except_table10935
+ GCC_except_table110
+ GCC_except_table11016
+ GCC_except_table11017
+ GCC_except_table11020
+ GCC_except_table11021
+ GCC_except_table11024
+ GCC_except_table11025
+ GCC_except_table11027
+ GCC_except_table11033
+ GCC_except_table11037
+ GCC_except_table11039
+ GCC_except_table11041
+ GCC_except_table11043
+ GCC_except_table11045
+ GCC_except_table11047
+ GCC_except_table11049
+ GCC_except_table11051
+ GCC_except_table11053
+ GCC_except_table11057
+ GCC_except_table11060
+ GCC_except_table11063
+ GCC_except_table11067
+ GCC_except_table11070
+ GCC_except_table11073
+ GCC_except_table11075
+ GCC_except_table11077
+ GCC_except_table11079
+ GCC_except_table11081
+ GCC_except_table11083
+ GCC_except_table11084
+ GCC_except_table11087
+ GCC_except_table11090
+ GCC_except_table11093
+ GCC_except_table11096
+ GCC_except_table11098
+ GCC_except_table11101
+ GCC_except_table11104
+ GCC_except_table11107
+ GCC_except_table11108
+ GCC_except_table11112
+ GCC_except_table11117
+ GCC_except_table11118
+ GCC_except_table11120
+ GCC_except_table11121
+ GCC_except_table11122
+ GCC_except_table11123
+ GCC_except_table11124
+ GCC_except_table11125
+ GCC_except_table11126
+ GCC_except_table11128
+ GCC_except_table11129
+ GCC_except_table11130
+ GCC_except_table11132
+ GCC_except_table11133
+ GCC_except_table11134
+ GCC_except_table11135
+ GCC_except_table11146
+ GCC_except_table11148
+ GCC_except_table11150
+ GCC_except_table11154
+ GCC_except_table11156
+ GCC_except_table11226
+ GCC_except_table11230
+ GCC_except_table11312
+ GCC_except_table1136
+ GCC_except_table11384
+ GCC_except_table11425
+ GCC_except_table11437
+ GCC_except_table11535
+ GCC_except_table11540
+ GCC_except_table1159
+ GCC_except_table11617
+ GCC_except_table1165
+ GCC_except_table1166
+ GCC_except_table1168
+ GCC_except_table117
+ GCC_except_table11736
+ GCC_except_table1179
+ GCC_except_table1181
+ GCC_except_table11898
+ GCC_except_table11939
+ GCC_except_table1200
+ GCC_except_table1201
+ GCC_except_table1202
+ GCC_except_table1208
+ GCC_except_table1209
+ GCC_except_table1215
+ GCC_except_table12167
+ GCC_except_table12200
+ GCC_except_table12224
+ GCC_except_table12225
+ GCC_except_table12226
+ GCC_except_table12227
+ GCC_except_table12228
+ GCC_except_table12229
+ GCC_except_table12231
+ GCC_except_table12233
+ GCC_except_table12248
+ GCC_except_table12328
+ GCC_except_table12340
+ GCC_except_table12346
+ GCC_except_table12351
+ GCC_except_table12365
+ GCC_except_table12369
+ GCC_except_table1237
+ GCC_except_table12379
+ GCC_except_table12389
+ GCC_except_table12394
+ GCC_except_table12399
+ GCC_except_table12403
+ GCC_except_table12408
+ GCC_except_table12413
+ GCC_except_table12419
+ GCC_except_table12429
+ GCC_except_table12432
+ GCC_except_table12443
+ GCC_except_table12447
+ GCC_except_table12458
+ GCC_except_table12476
+ GCC_except_table12492
+ GCC_except_table12544
+ GCC_except_table12549
+ GCC_except_table1255
+ GCC_except_table12555
+ GCC_except_table12559
+ GCC_except_table12561
+ GCC_except_table12563
+ GCC_except_table12567
+ GCC_except_table12569
+ GCC_except_table12571
+ GCC_except_table12574
+ GCC_except_table12585
+ GCC_except_table12594
+ GCC_except_table12597
+ GCC_except_table12601
+ GCC_except_table12606
+ GCC_except_table12612
+ GCC_except_table12616
+ GCC_except_table12630
+ GCC_except_table12632
+ GCC_except_table12634
+ GCC_except_table12652
+ GCC_except_table12654
+ GCC_except_table12656
+ GCC_except_table12658
+ GCC_except_table12661
+ GCC_except_table12663
+ GCC_except_table12665
+ GCC_except_table12667
+ GCC_except_table12669
+ GCC_except_table12672
+ GCC_except_table12675
+ GCC_except_table12679
+ GCC_except_table12681
+ GCC_except_table12683
+ GCC_except_table12686
+ GCC_except_table12690
+ GCC_except_table12695
+ GCC_except_table12706
+ GCC_except_table12712
+ GCC_except_table12738
+ GCC_except_table12742
+ GCC_except_table12743
+ GCC_except_table12751
+ GCC_except_table12779
+ GCC_except_table12898
+ GCC_except_table12989
+ GCC_except_table1299
+ GCC_except_table13006
+ GCC_except_table13008
+ GCC_except_table13027
+ GCC_except_table13029
+ GCC_except_table13033
+ GCC_except_table13051
+ GCC_except_table13055
+ GCC_except_table13062
+ GCC_except_table13067
+ GCC_except_table13078
+ GCC_except_table13083
+ GCC_except_table1314
+ GCC_except_table13163
+ GCC_except_table13179
+ GCC_except_table13205
+ GCC_except_table13207
+ GCC_except_table1321
+ GCC_except_table13214
+ GCC_except_table13218
+ GCC_except_table13220
+ GCC_except_table13224
+ GCC_except_table13269
+ GCC_except_table13278
+ GCC_except_table1328
+ GCC_except_table13284
+ GCC_except_table13286
+ GCC_except_table13288
+ GCC_except_table1330
+ GCC_except_table13331
+ GCC_except_table13444
+ GCC_except_table1345
+ GCC_except_table13465
+ GCC_except_table13472
+ GCC_except_table13476
+ GCC_except_table13523
+ GCC_except_table13606
+ GCC_except_table13612
+ GCC_except_table13631
+ GCC_except_table13643
+ GCC_except_table13699
+ GCC_except_table13720
+ GCC_except_table13723
+ GCC_except_table13727
+ GCC_except_table13730
+ GCC_except_table13732
+ GCC_except_table13736
+ GCC_except_table13739
+ GCC_except_table13748
+ GCC_except_table13797
+ GCC_except_table13815
+ GCC_except_table13821
+ GCC_except_table13843
+ GCC_except_table1388
+ GCC_except_table13937
+ GCC_except_table13991
+ GCC_except_table14
+ GCC_except_table14002
+ GCC_except_table14006
+ GCC_except_table14021
+ GCC_except_table14029
+ GCC_except_table14049
+ GCC_except_table14059
+ GCC_except_table14061
+ GCC_except_table14063
+ GCC_except_table14081
+ GCC_except_table14172
+ GCC_except_table14177
+ GCC_except_table14200
+ GCC_except_table14213
+ GCC_except_table14215
+ GCC_except_table14217
+ GCC_except_table1428
+ GCC_except_table1430
+ GCC_except_table14325
+ GCC_except_table14326
+ GCC_except_table14330
+ GCC_except_table14362
+ GCC_except_table14383
+ GCC_except_table1439
+ GCC_except_table14394
+ GCC_except_table14395
+ GCC_except_table14396
+ GCC_except_table14397
+ GCC_except_table14398
+ GCC_except_table14399
+ GCC_except_table14400
+ GCC_except_table14401
+ GCC_except_table14402
+ GCC_except_table14403
+ GCC_except_table14404
+ GCC_except_table14405
+ GCC_except_table14406
+ GCC_except_table14407
+ GCC_except_table1441
+ GCC_except_table14411
+ GCC_except_table14415
+ GCC_except_table14470
+ GCC_except_table14476
+ GCC_except_table1449
+ GCC_except_table14491
+ GCC_except_table14499
+ GCC_except_table14502
+ GCC_except_table14507
+ GCC_except_table14511
+ GCC_except_table14560
+ GCC_except_table14564
+ GCC_except_table14575
+ GCC_except_table14611
+ GCC_except_table14664
+ GCC_except_table14667
+ GCC_except_table14671
+ GCC_except_table14745
+ GCC_except_table14768
+ GCC_except_table1479
+ GCC_except_table14791
+ GCC_except_table14934
+ GCC_except_table15015
+ GCC_except_table1507
+ GCC_except_table15075
+ GCC_except_table15092
+ GCC_except_table15099
+ GCC_except_table15102
+ GCC_except_table15103
+ GCC_except_table15122
+ GCC_except_table1518
+ GCC_except_table15211
+ GCC_except_table15218
+ GCC_except_table1522
+ GCC_except_table15220
+ GCC_except_table15221
+ GCC_except_table15224
+ GCC_except_table15233
+ GCC_except_table15409
+ GCC_except_table15439
+ GCC_except_table15495
+ GCC_except_table15577
+ GCC_except_table1563
+ GCC_except_table15676
+ GCC_except_table15686
+ GCC_except_table15694
+ GCC_except_table15696
+ GCC_except_table1571
+ GCC_except_table15722
+ GCC_except_table15741
+ GCC_except_table15752
+ GCC_except_table15777
+ GCC_except_table158
+ GCC_except_table15817
+ GCC_except_table15821
+ GCC_except_table15822
+ GCC_except_table15888
+ GCC_except_table15892
+ GCC_except_table15895
+ GCC_except_table15898
+ GCC_except_table16054
+ GCC_except_table16084
+ GCC_except_table1609
+ GCC_except_table16101
+ GCC_except_table16106
+ GCC_except_table16109
+ GCC_except_table16111
+ GCC_except_table16114
+ GCC_except_table16119
+ GCC_except_table16120
+ GCC_except_table16125
+ GCC_except_table16126
+ GCC_except_table16128
+ GCC_except_table16134
+ GCC_except_table16138
+ GCC_except_table16140
+ GCC_except_table16141
+ GCC_except_table16145
+ GCC_except_table16147
+ GCC_except_table16149
+ GCC_except_table16151
+ GCC_except_table16154
+ GCC_except_table16157
+ GCC_except_table16208
+ GCC_except_table1622
+ GCC_except_table16223
+ GCC_except_table16226
+ GCC_except_table16243
+ GCC_except_table16247
+ GCC_except_table16252
+ GCC_except_table16257
+ GCC_except_table16260
+ GCC_except_table16262
+ GCC_except_table16273
+ GCC_except_table1631
+ GCC_except_table16370
+ GCC_except_table16374
+ GCC_except_table16398
+ GCC_except_table16405
+ GCC_except_table16414
+ GCC_except_table16423
+ GCC_except_table16428
+ GCC_except_table16432
+ GCC_except_table16445
+ GCC_except_table16503
+ GCC_except_table16505
+ GCC_except_table16656
+ GCC_except_table16669
+ GCC_except_table16690
+ GCC_except_table16781
+ GCC_except_table16801
+ GCC_except_table16807
+ GCC_except_table16812
+ GCC_except_table16819
+ GCC_except_table16847
+ GCC_except_table16855
+ GCC_except_table16896
+ GCC_except_table16900
+ GCC_except_table16963
+ GCC_except_table16968
+ GCC_except_table16976
+ GCC_except_table16986
+ GCC_except_table16998
+ GCC_except_table17012
+ GCC_except_table17018
+ GCC_except_table17028
+ GCC_except_table17041
+ GCC_except_table17051
+ GCC_except_table17061
+ GCC_except_table17091
+ GCC_except_table17095
+ GCC_except_table17097
+ GCC_except_table17099
+ GCC_except_table171
+ GCC_except_table17160
+ GCC_except_table17163
+ GCC_except_table17208
+ GCC_except_table17219
+ GCC_except_table17239
+ GCC_except_table17246
+ GCC_except_table17250
+ GCC_except_table17312
+ GCC_except_table17322
+ GCC_except_table17334
+ GCC_except_table17335
+ GCC_except_table17338
+ GCC_except_table17341
+ GCC_except_table17344
+ GCC_except_table17347
+ GCC_except_table17348
+ GCC_except_table17349
+ GCC_except_table17350
+ GCC_except_table17351
+ GCC_except_table17353
+ GCC_except_table17384
+ GCC_except_table17390
+ GCC_except_table17461
+ GCC_except_table17475
+ GCC_except_table17526
+ GCC_except_table17544
+ GCC_except_table17584
+ GCC_except_table17589
+ GCC_except_table17628
+ GCC_except_table17636
+ GCC_except_table17639
+ GCC_except_table17651
+ GCC_except_table17676
+ GCC_except_table17707
+ GCC_except_table17708
+ GCC_except_table17709
+ GCC_except_table17743
+ GCC_except_table17753
+ GCC_except_table1776
+ GCC_except_table17794
+ GCC_except_table17801
+ GCC_except_table17805
+ GCC_except_table1782
+ GCC_except_table17821
+ GCC_except_table17822
+ GCC_except_table17838
+ GCC_except_table17857
+ GCC_except_table17890
+ GCC_except_table17892
+ GCC_except_table17897
+ GCC_except_table17900
+ GCC_except_table17902
+ GCC_except_table17906
+ GCC_except_table17969
+ GCC_except_table17994
+ GCC_except_table17996
+ GCC_except_table17998
+ GCC_except_table18000
+ GCC_except_table18002
+ GCC_except_table18004
+ GCC_except_table18008
+ GCC_except_table18057
+ GCC_except_table18194
+ GCC_except_table18253
+ GCC_except_table18264
+ GCC_except_table18266
+ GCC_except_table18285
+ GCC_except_table18326
+ GCC_except_table18337
+ GCC_except_table18351
+ GCC_except_table18356
+ GCC_except_table18360
+ GCC_except_table18374
+ GCC_except_table18375
+ GCC_except_table18380
+ GCC_except_table18383
+ GCC_except_table18413
+ GCC_except_table18442
+ GCC_except_table18445
+ GCC_except_table18522
+ GCC_except_table18546
+ GCC_except_table18554
+ GCC_except_table18556
+ GCC_except_table18558
+ GCC_except_table18561
+ GCC_except_table18562
+ GCC_except_table18563
+ GCC_except_table18565
+ GCC_except_table18566
+ GCC_except_table18567
+ GCC_except_table18569
+ GCC_except_table18574
+ GCC_except_table18578
+ GCC_except_table18579
+ GCC_except_table18582
+ GCC_except_table18584
+ GCC_except_table18586
+ GCC_except_table18588
+ GCC_except_table18590
+ GCC_except_table18591
+ GCC_except_table18592
+ GCC_except_table18596
+ GCC_except_table18597
+ GCC_except_table18600
+ GCC_except_table18651
+ GCC_except_table18666
+ GCC_except_table18695
+ GCC_except_table18836
+ GCC_except_table18874
+ GCC_except_table18879
+ GCC_except_table18882
+ GCC_except_table18905
+ GCC_except_table18907
+ GCC_except_table18908
+ GCC_except_table18909
+ GCC_except_table18913
+ GCC_except_table18914
+ GCC_except_table18915
+ GCC_except_table18916
+ GCC_except_table18917
+ GCC_except_table18924
+ GCC_except_table18927
+ GCC_except_table18929
+ GCC_except_table18931
+ GCC_except_table18933
+ GCC_except_table18936
+ GCC_except_table18939
+ GCC_except_table18942
+ GCC_except_table18945
+ GCC_except_table18947
+ GCC_except_table18953
+ GCC_except_table18956
+ GCC_except_table18959
+ GCC_except_table18962
+ GCC_except_table18970
+ GCC_except_table18974
+ GCC_except_table18976
+ GCC_except_table18978
+ GCC_except_table18979
+ GCC_except_table18986
+ GCC_except_table18989
+ GCC_except_table18991
+ GCC_except_table18998
+ GCC_except_table19
+ GCC_except_table19000
+ GCC_except_table19002
+ GCC_except_table19004
+ GCC_except_table19006
+ GCC_except_table19013
+ GCC_except_table19017
+ GCC_except_table19021
+ GCC_except_table19023
+ GCC_except_table19025
+ GCC_except_table19027
+ GCC_except_table19029
+ GCC_except_table19033
+ GCC_except_table19034
+ GCC_except_table19035
+ GCC_except_table19037
+ GCC_except_table19038
+ GCC_except_table19042
+ GCC_except_table19044
+ GCC_except_table19045
+ GCC_except_table19046
+ GCC_except_table19049
+ GCC_except_table19051
+ GCC_except_table19053
+ GCC_except_table19054
+ GCC_except_table19055
+ GCC_except_table19058
+ GCC_except_table19061
+ GCC_except_table19064
+ GCC_except_table19066
+ GCC_except_table19068
+ GCC_except_table19070
+ GCC_except_table19071
+ GCC_except_table19082
+ GCC_except_table19086
+ GCC_except_table19090
+ GCC_except_table19188
+ GCC_except_table19194
+ GCC_except_table192
+ GCC_except_table19207
+ GCC_except_table19208
+ GCC_except_table19209
+ GCC_except_table19213
+ GCC_except_table19216
+ GCC_except_table19217
+ GCC_except_table19218
+ GCC_except_table19350
+ GCC_except_table19362
+ GCC_except_table19381
+ GCC_except_table19454
+ GCC_except_table19457
+ GCC_except_table19459
+ GCC_except_table19467
+ GCC_except_table19475
+ GCC_except_table19502
+ GCC_except_table19506
+ GCC_except_table19508
+ GCC_except_table19512
+ GCC_except_table19522
+ GCC_except_table19527
+ GCC_except_table19529
+ GCC_except_table19537
+ GCC_except_table19538
+ GCC_except_table1954
+ GCC_except_table19541
+ GCC_except_table19542
+ GCC_except_table19545
+ GCC_except_table1959
+ GCC_except_table19610
+ GCC_except_table19677
+ GCC_except_table19695
+ GCC_except_table19767
+ GCC_except_table19769
+ GCC_except_table19789
+ GCC_except_table19791
+ GCC_except_table19797
+ GCC_except_table19813
+ GCC_except_table19955
+ GCC_except_table19966
+ GCC_except_table20003
+ GCC_except_table20009
+ GCC_except_table20013
+ GCC_except_table20018
+ GCC_except_table20044
+ GCC_except_table20078
+ GCC_except_table20087
+ GCC_except_table20093
+ GCC_except_table20096
+ GCC_except_table20101
+ GCC_except_table20105
+ GCC_except_table20110
+ GCC_except_table20116
+ GCC_except_table20122
+ GCC_except_table20133
+ GCC_except_table20139
+ GCC_except_table20152
+ GCC_except_table20160
+ GCC_except_table20313
+ GCC_except_table20317
+ GCC_except_table20351
+ GCC_except_table20355
+ GCC_except_table20359
+ GCC_except_table20361
+ GCC_except_table20389
+ GCC_except_table20429
+ GCC_except_table20433
+ GCC_except_table20437
+ GCC_except_table20441
+ GCC_except_table20445
+ GCC_except_table20449
+ GCC_except_table20453
+ GCC_except_table20457
+ GCC_except_table20461
+ GCC_except_table20465
+ GCC_except_table20469
+ GCC_except_table20473
+ GCC_except_table20477
+ GCC_except_table20481
+ GCC_except_table20485
+ GCC_except_table20489
+ GCC_except_table20493
+ GCC_except_table20497
+ GCC_except_table20501
+ GCC_except_table20505
+ GCC_except_table20509
+ GCC_except_table20546
+ GCC_except_table20549
+ GCC_except_table20554
+ GCC_except_table20557
+ GCC_except_table20583
+ GCC_except_table20587
+ GCC_except_table20588
+ GCC_except_table20589
+ GCC_except_table20595
+ GCC_except_table20596
+ GCC_except_table20608
+ GCC_except_table20668
+ GCC_except_table20714
+ GCC_except_table20725
+ GCC_except_table20758
+ GCC_except_table20765
+ GCC_except_table20777
+ GCC_except_table20781
+ GCC_except_table20785
+ GCC_except_table20789
+ GCC_except_table20805
+ GCC_except_table20858
+ GCC_except_table20862
+ GCC_except_table20910
+ GCC_except_table20927
+ GCC_except_table20944
+ GCC_except_table20952
+ GCC_except_table20953
+ GCC_except_table20957
+ GCC_except_table20958
+ GCC_except_table20960
+ GCC_except_table20962
+ GCC_except_table20967
+ GCC_except_table20968
+ GCC_except_table20970
+ GCC_except_table20978
+ GCC_except_table20981
+ GCC_except_table20982
+ GCC_except_table20983
+ GCC_except_table20984
+ GCC_except_table20986
+ GCC_except_table20988
+ GCC_except_table20991
+ GCC_except_table20992
+ GCC_except_table20994
+ GCC_except_table20995
+ GCC_except_table20997
+ GCC_except_table20998
+ GCC_except_table21002
+ GCC_except_table21004
+ GCC_except_table21006
+ GCC_except_table21008
+ GCC_except_table21012
+ GCC_except_table21014
+ GCC_except_table21016
+ GCC_except_table21018
+ GCC_except_table21020
+ GCC_except_table21023
+ GCC_except_table21027
+ GCC_except_table21038
+ GCC_except_table21162
+ GCC_except_table21169
+ GCC_except_table21182
+ GCC_except_table21188
+ GCC_except_table21206
+ GCC_except_table21306
+ GCC_except_table21379
+ GCC_except_table21395
+ GCC_except_table214
+ GCC_except_table21405
+ GCC_except_table21580
+ GCC_except_table21581
+ GCC_except_table21592
+ GCC_except_table21593
+ GCC_except_table21611
+ GCC_except_table21613
+ GCC_except_table21620
+ GCC_except_table21644
+ GCC_except_table21662
+ GCC_except_table21710
+ GCC_except_table21717
+ GCC_except_table21733
+ GCC_except_table21744
+ GCC_except_table21750
+ GCC_except_table21754
+ GCC_except_table21759
+ GCC_except_table21821
+ GCC_except_table21837
+ GCC_except_table21859
+ GCC_except_table2187
+ GCC_except_table21912
+ GCC_except_table21966
+ GCC_except_table21978
+ GCC_except_table22011
+ GCC_except_table22023
+ GCC_except_table22028
+ GCC_except_table22035
+ GCC_except_table22065
+ GCC_except_table22078
+ GCC_except_table22081
+ GCC_except_table22107
+ GCC_except_table2211
+ GCC_except_table2219
+ GCC_except_table2222
+ GCC_except_table22227
+ GCC_except_table22273
+ GCC_except_table22277
+ GCC_except_table22279
+ GCC_except_table22281
+ GCC_except_table22308
+ GCC_except_table22326
+ GCC_except_table22335
+ GCC_except_table22403
+ GCC_except_table22404
+ GCC_except_table2247
+ GCC_except_table22473
+ GCC_except_table22477
+ GCC_except_table22518
+ GCC_except_table2252
+ GCC_except_table22585
+ GCC_except_table2266
+ GCC_except_table2268
+ GCC_except_table2293
+ GCC_except_table2299
+ GCC_except_table22998
+ GCC_except_table2315
+ GCC_except_table2327
+ GCC_except_table23292
+ GCC_except_table23304
+ GCC_except_table23313
+ GCC_except_table23360
+ GCC_except_table23364
+ GCC_except_table23420
+ GCC_except_table23432
+ GCC_except_table23448
+ GCC_except_table23549
+ GCC_except_table23558
+ GCC_except_table23588
+ GCC_except_table23650
+ GCC_except_table23664
+ GCC_except_table23665
+ GCC_except_table23731
+ GCC_except_table23749
+ GCC_except_table23756
+ GCC_except_table23780
+ GCC_except_table23957
+ GCC_except_table23963
+ GCC_except_table23982
+ GCC_except_table23986
+ GCC_except_table24031
+ GCC_except_table24065
+ GCC_except_table24103
+ GCC_except_table24106
+ GCC_except_table2411
+ GCC_except_table24110
+ GCC_except_table24153
+ GCC_except_table24154
+ GCC_except_table24218
+ GCC_except_table24238
+ GCC_except_table24243
+ GCC_except_table24249
+ GCC_except_table24258
+ GCC_except_table24260
+ GCC_except_table24264
+ GCC_except_table24271
+ GCC_except_table24287
+ GCC_except_table24294
+ GCC_except_table24321
+ GCC_except_table24510
+ GCC_except_table24514
+ GCC_except_table24521
+ GCC_except_table24523
+ GCC_except_table24524
+ GCC_except_table24527
+ GCC_except_table24528
+ GCC_except_table24530
+ GCC_except_table24531
+ GCC_except_table24532
+ GCC_except_table24534
+ GCC_except_table24539
+ GCC_except_table24541
+ GCC_except_table24544
+ GCC_except_table24545
+ GCC_except_table24546
+ GCC_except_table24550
+ GCC_except_table24551
+ GCC_except_table24581
+ GCC_except_table24584
+ GCC_except_table24606
+ GCC_except_table24610
+ GCC_except_table24611
+ GCC_except_table24616
+ GCC_except_table24621
+ GCC_except_table24625
+ GCC_except_table2464
+ GCC_except_table24689
+ GCC_except_table24696
+ GCC_except_table24698
+ GCC_except_table24700
+ GCC_except_table24702
+ GCC_except_table24704
+ GCC_except_table24712
+ GCC_except_table24714
+ GCC_except_table24728
+ GCC_except_table24754
+ GCC_except_table24757
+ GCC_except_table24764
+ GCC_except_table24766
+ GCC_except_table24768
+ GCC_except_table24770
+ GCC_except_table24774
+ GCC_except_table24778
+ GCC_except_table24797
+ GCC_except_table24805
+ GCC_except_table24815
+ GCC_except_table24820
+ GCC_except_table24824
+ GCC_except_table24826
+ GCC_except_table24828
+ GCC_except_table24830
+ GCC_except_table24838
+ GCC_except_table2484
+ GCC_except_table24842
+ GCC_except_table24850
+ GCC_except_table24852
+ GCC_except_table24864
+ GCC_except_table24888
+ GCC_except_table24904
+ GCC_except_table24922
+ GCC_except_table24923
+ GCC_except_table24926
+ GCC_except_table2494
+ GCC_except_table24951
+ GCC_except_table24953
+ GCC_except_table24955
+ GCC_except_table24978
+ GCC_except_table24981
+ GCC_except_table24984
+ GCC_except_table24986
+ GCC_except_table2500
+ GCC_except_table25040
+ GCC_except_table25102
+ GCC_except_table25106
+ GCC_except_table25109
+ GCC_except_table25112
+ GCC_except_table25119
+ GCC_except_table25145
+ GCC_except_table25148
+ GCC_except_table25160
+ GCC_except_table25163
+ GCC_except_table25179
+ GCC_except_table25188
+ GCC_except_table25191
+ GCC_except_table25213
+ GCC_except_table25222
+ GCC_except_table25225
+ GCC_except_table25228
+ GCC_except_table25235
+ GCC_except_table25243
+ GCC_except_table25244
+ GCC_except_table25252
+ GCC_except_table25346
+ GCC_except_table25347
+ GCC_except_table25348
+ GCC_except_table25349
+ GCC_except_table25353
+ GCC_except_table25357
+ GCC_except_table25358
+ GCC_except_table25359
+ GCC_except_table25362
+ GCC_except_table25392
+ GCC_except_table25400
+ GCC_except_table25404
+ GCC_except_table25432
+ GCC_except_table25447
+ GCC_except_table25481
+ GCC_except_table25485
+ GCC_except_table25493
+ GCC_except_table25509
+ GCC_except_table25529
+ GCC_except_table25533
+ GCC_except_table25564
+ GCC_except_table25570
+ GCC_except_table2561
+ GCC_except_table25639
+ GCC_except_table2564
+ GCC_except_table25657
+ GCC_except_table25666
+ GCC_except_table25669
+ GCC_except_table25672
+ GCC_except_table25675
+ GCC_except_table25681
+ GCC_except_table25684
+ GCC_except_table25687
+ GCC_except_table25690
+ GCC_except_table25696
+ GCC_except_table25699
+ GCC_except_table25702
+ GCC_except_table25705
+ GCC_except_table25711
+ GCC_except_table25714
+ GCC_except_table25717
+ GCC_except_table25720
+ GCC_except_table25723
+ GCC_except_table25726
+ GCC_except_table25729
+ GCC_except_table25735
+ GCC_except_table25738
+ GCC_except_table25741
+ GCC_except_table25744
+ GCC_except_table25747
+ GCC_except_table25750
+ GCC_except_table25753
+ GCC_except_table25756
+ GCC_except_table25759
+ GCC_except_table25762
+ GCC_except_table25765
+ GCC_except_table25768
+ GCC_except_table25771
+ GCC_except_table25774
+ GCC_except_table25777
+ GCC_except_table25780
+ GCC_except_table25783
+ GCC_except_table25786
+ GCC_except_table25789
+ GCC_except_table25792
+ GCC_except_table25795
+ GCC_except_table25798
+ GCC_except_table25801
+ GCC_except_table25804
+ GCC_except_table25807
+ GCC_except_table25813
+ GCC_except_table25816
+ GCC_except_table25822
+ GCC_except_table25828
+ GCC_except_table25834
+ GCC_except_table25837
+ GCC_except_table25840
+ GCC_except_table25843
+ GCC_except_table25846
+ GCC_except_table25849
+ GCC_except_table25852
+ GCC_except_table25855
+ GCC_except_table25864
+ GCC_except_table25867
+ GCC_except_table25870
+ GCC_except_table25873
+ GCC_except_table25876
+ GCC_except_table25879
+ GCC_except_table25937
+ GCC_except_table25940
+ GCC_except_table25943
+ GCC_except_table26
+ GCC_except_table26045
+ GCC_except_table26052
+ GCC_except_table26054
+ GCC_except_table26100
+ GCC_except_table26144
+ GCC_except_table26152
+ GCC_except_table26156
+ GCC_except_table26167
+ GCC_except_table26195
+ GCC_except_table26197
+ GCC_except_table26219
+ GCC_except_table26221
+ GCC_except_table26342
+ GCC_except_table26348
+ GCC_except_table26370
+ GCC_except_table26409
+ GCC_except_table26412
+ GCC_except_table26418
+ GCC_except_table26423
+ GCC_except_table26427
+ GCC_except_table26435
+ GCC_except_table26462
+ GCC_except_table26468
+ GCC_except_table26470
+ GCC_except_table26511
+ GCC_except_table26633
+ GCC_except_table26637
+ GCC_except_table26640
+ GCC_except_table26642
+ GCC_except_table26755
+ GCC_except_table26947
+ GCC_except_table26950
+ GCC_except_table26958
+ GCC_except_table26964
+ GCC_except_table26975
+ GCC_except_table26985
+ GCC_except_table26987
+ GCC_except_table26989
+ GCC_except_table26994
+ GCC_except_table26996
+ GCC_except_table27010
+ GCC_except_table27015
+ GCC_except_table27019
+ GCC_except_table27039
+ GCC_except_table2713
+ GCC_except_table2715
+ GCC_except_table2724
+ GCC_except_table2728
+ GCC_except_table2751
+ GCC_except_table277
+ GCC_except_table278
+ GCC_except_table2792
+ GCC_except_table2804
+ GCC_except_table2807
+ GCC_except_table2814
+ GCC_except_table2821
+ GCC_except_table283
+ GCC_except_table2865
+ GCC_except_table2866
+ GCC_except_table2872
+ GCC_except_table2924
+ GCC_except_table2964
+ GCC_except_table3072
+ GCC_except_table3080
+ GCC_except_table3102
+ GCC_except_table3299
+ GCC_except_table330
+ GCC_except_table3305
+ GCC_except_table3357
+ GCC_except_table3409
+ GCC_except_table3411
+ GCC_except_table3420
+ GCC_except_table3462
+ GCC_except_table3490
+ GCC_except_table3504
+ GCC_except_table3509
+ GCC_except_table3511
+ GCC_except_table3514
+ GCC_except_table3521
+ GCC_except_table3522
+ GCC_except_table3526
+ GCC_except_table3528
+ GCC_except_table3532
+ GCC_except_table3536
+ GCC_except_table3573
+ GCC_except_table3580
+ GCC_except_table3829
+ GCC_except_table3833
+ GCC_except_table3836
+ GCC_except_table3839
+ GCC_except_table3842
+ GCC_except_table3845
+ GCC_except_table3855
+ GCC_except_table3913
+ GCC_except_table3951
+ GCC_except_table3954
+ GCC_except_table3961
+ GCC_except_table3962
+ GCC_except_table3968
+ GCC_except_table3996
+ GCC_except_table40
+ GCC_except_table4024
+ GCC_except_table4084
+ GCC_except_table4089
+ GCC_except_table4095
+ GCC_except_table4107
+ GCC_except_table4112
+ GCC_except_table4115
+ GCC_except_table414
+ GCC_except_table4140
+ GCC_except_table4142
+ GCC_except_table4151
+ GCC_except_table4152
+ GCC_except_table4154
+ GCC_except_table417
+ GCC_except_table4172
+ GCC_except_table4175
+ GCC_except_table420
+ GCC_except_table4203
+ GCC_except_table4206
+ GCC_except_table4213
+ GCC_except_table4229
+ GCC_except_table423
+ GCC_except_table4234
+ GCC_except_table4238
+ GCC_except_table4246
+ GCC_except_table4253
+ GCC_except_table426
+ GCC_except_table4269
+ GCC_except_table432
+ GCC_except_table4420
+ GCC_except_table4427
+ GCC_except_table4434
+ GCC_except_table4436
+ GCC_except_table4442
+ GCC_except_table4444
+ GCC_except_table4460
+ GCC_except_table4462
+ GCC_except_table4467
+ GCC_except_table4469
+ GCC_except_table4477
+ GCC_except_table4481
+ GCC_except_table4487
+ GCC_except_table4528
+ GCC_except_table4529
+ GCC_except_table4554
+ GCC_except_table4602
+ GCC_except_table4606
+ GCC_except_table464
+ GCC_except_table4807
+ GCC_except_table4814
+ GCC_except_table4873
+ GCC_except_table4895
+ GCC_except_table4899
+ GCC_except_table49
+ GCC_except_table4922
+ GCC_except_table5018
+ GCC_except_table5023
+ GCC_except_table5031
+ GCC_except_table5057
+ GCC_except_table5128
+ GCC_except_table522
+ GCC_except_table5235
+ GCC_except_table5272
+ GCC_except_table5280
+ GCC_except_table5282
+ GCC_except_table5285
+ GCC_except_table53
+ GCC_except_table536
+ GCC_except_table5497
+ GCC_except_table5531
+ GCC_except_table5604
+ GCC_except_table5605
+ GCC_except_table5618
+ GCC_except_table5621
+ GCC_except_table566
+ GCC_except_table5682
+ GCC_except_table5701
+ GCC_except_table5708
+ GCC_except_table571
+ GCC_except_table5712
+ GCC_except_table5722
+ GCC_except_table5725
+ GCC_except_table5785
+ GCC_except_table5790
+ GCC_except_table5800
+ GCC_except_table5810
+ GCC_except_table5838
+ GCC_except_table5841
+ GCC_except_table5852
+ GCC_except_table5867
+ GCC_except_table589
+ GCC_except_table5904
+ GCC_except_table5905
+ GCC_except_table5908
+ GCC_except_table5909
+ GCC_except_table5917
+ GCC_except_table5930
+ GCC_except_table6021
+ GCC_except_table6023
+ GCC_except_table6046
+ GCC_except_table6081
+ GCC_except_table6085
+ GCC_except_table6089
+ GCC_except_table6110
+ GCC_except_table6115
+ GCC_except_table6120
+ GCC_except_table6122
+ GCC_except_table6124
+ GCC_except_table6142
+ GCC_except_table6145
+ GCC_except_table6153
+ GCC_except_table6211
+ GCC_except_table6234
+ GCC_except_table6239
+ GCC_except_table6258
+ GCC_except_table6263
+ GCC_except_table6267
+ GCC_except_table6271
+ GCC_except_table6276
+ GCC_except_table6281
+ GCC_except_table6285
+ GCC_except_table6289
+ GCC_except_table6293
+ GCC_except_table6305
+ GCC_except_table6306
+ GCC_except_table6308
+ GCC_except_table6316
+ GCC_except_table6317
+ GCC_except_table6318
+ GCC_except_table6320
+ GCC_except_table6321
+ GCC_except_table6322
+ GCC_except_table6326
+ GCC_except_table6327
+ GCC_except_table6329
+ GCC_except_table6330
+ GCC_except_table6333
+ GCC_except_table6335
+ GCC_except_table6338
+ GCC_except_table6340
+ GCC_except_table6344
+ GCC_except_table6345
+ GCC_except_table6347
+ GCC_except_table6348
+ GCC_except_table6349
+ GCC_except_table6356
+ GCC_except_table6358
+ GCC_except_table6361
+ GCC_except_table6364
+ GCC_except_table6367
+ GCC_except_table6369
+ GCC_except_table6370
+ GCC_except_table6371
+ GCC_except_table6372
+ GCC_except_table6373
+ GCC_except_table6374
+ GCC_except_table6375
+ GCC_except_table6383
+ GCC_except_table6384
+ GCC_except_table6394
+ GCC_except_table6396
+ GCC_except_table6447
+ GCC_except_table6460
+ GCC_except_table6487
+ GCC_except_table6553
+ GCC_except_table6667
+ GCC_except_table671
+ GCC_except_table6736
+ GCC_except_table676
+ GCC_except_table689
+ GCC_except_table691
+ GCC_except_table6944
+ GCC_except_table695
+ GCC_except_table7003
+ GCC_except_table704
+ GCC_except_table7049
+ GCC_except_table7056
+ GCC_except_table7067
+ GCC_except_table7073
+ GCC_except_table7080
+ GCC_except_table7089
+ GCC_except_table7093
+ GCC_except_table7096
+ GCC_except_table7099
+ GCC_except_table710
+ GCC_except_table7105
+ GCC_except_table7110
+ GCC_except_table7118
+ GCC_except_table7124
+ GCC_except_table7127
+ GCC_except_table7135
+ GCC_except_table7143
+ GCC_except_table7163
+ GCC_except_table7175
+ GCC_except_table7201
+ GCC_except_table7222
+ GCC_except_table7224
+ GCC_except_table7237
+ GCC_except_table724
+ GCC_except_table7241
+ GCC_except_table7246
+ GCC_except_table7248
+ GCC_except_table7251
+ GCC_except_table7256
+ GCC_except_table728
+ GCC_except_table7326
+ GCC_except_table7327
+ GCC_except_table7329
+ GCC_except_table733
+ GCC_except_table7333
+ GCC_except_table7334
+ GCC_except_table7336
+ GCC_except_table7337
+ GCC_except_table7341
+ GCC_except_table7342
+ GCC_except_table7344
+ GCC_except_table7349
+ GCC_except_table7352
+ GCC_except_table7355
+ GCC_except_table7357
+ GCC_except_table7359
+ GCC_except_table7361
+ GCC_except_table7363
+ GCC_except_table7366
+ GCC_except_table7368
+ GCC_except_table7371
+ GCC_except_table7379
+ GCC_except_table7383
+ GCC_except_table7388
+ GCC_except_table7390
+ GCC_except_table7394
+ GCC_except_table7398
+ GCC_except_table7407
+ GCC_except_table7415
+ GCC_except_table7419
+ GCC_except_table7423
+ GCC_except_table7438
+ GCC_except_table7440
+ GCC_except_table7446
+ GCC_except_table7448
+ GCC_except_table7480
+ GCC_except_table7484
+ GCC_except_table7509
+ GCC_except_table7511
+ GCC_except_table7527
+ GCC_except_table759
+ GCC_except_table7763
+ GCC_except_table7768
+ GCC_except_table7781
+ GCC_except_table7782
+ GCC_except_table7795
+ GCC_except_table7827
+ GCC_except_table7856
+ GCC_except_table7873
+ GCC_except_table7875
+ GCC_except_table7888
+ GCC_except_table7889
+ GCC_except_table7896
+ GCC_except_table7899
+ GCC_except_table795
+ GCC_except_table7956
+ GCC_except_table7960
+ GCC_except_table7973
+ GCC_except_table7980
+ GCC_except_table8028
+ GCC_except_table8039
+ GCC_except_table8058
+ GCC_except_table806
+ GCC_except_table8060
+ GCC_except_table8085
+ GCC_except_table8089
+ GCC_except_table8093
+ GCC_except_table8110
+ GCC_except_table8116
+ GCC_except_table8128
+ GCC_except_table8136
+ GCC_except_table8145
+ GCC_except_table8164
+ GCC_except_table8165
+ GCC_except_table8169
+ GCC_except_table8181
+ GCC_except_table8184
+ GCC_except_table8199
+ GCC_except_table8204
+ GCC_except_table8206
+ GCC_except_table8211
+ GCC_except_table8221
+ GCC_except_table8227
+ GCC_except_table8231
+ GCC_except_table8234
+ GCC_except_table8243
+ GCC_except_table8248
+ GCC_except_table827
+ GCC_except_table8276
+ GCC_except_table833
+ GCC_except_table8334
+ GCC_except_table8347
+ GCC_except_table8353
+ GCC_except_table8358
+ GCC_except_table8359
+ GCC_except_table8393
+ GCC_except_table8398
+ GCC_except_table840
+ GCC_except_table8404
+ GCC_except_table8416
+ GCC_except_table8429
+ GCC_except_table8442
+ GCC_except_table845
+ GCC_except_table8466
+ GCC_except_table8496
+ GCC_except_table850
+ GCC_except_table8531
+ GCC_except_table8534
+ GCC_except_table857
+ GCC_except_table8587
+ GCC_except_table8595
+ GCC_except_table8610
+ GCC_except_table8612
+ GCC_except_table864
+ GCC_except_table869
+ GCC_except_table8729
+ GCC_except_table8772
+ GCC_except_table8773
+ GCC_except_table8797
+ GCC_except_table8826
+ GCC_except_table8827
+ GCC_except_table887
+ GCC_except_table8988
+ GCC_except_table9000
+ GCC_except_table9010
+ GCC_except_table9013
+ GCC_except_table9038
+ GCC_except_table9063
+ GCC_except_table9067
+ GCC_except_table9070
+ GCC_except_table9077
+ GCC_except_table9081
+ GCC_except_table9140
+ GCC_except_table916
+ GCC_except_table922
+ GCC_except_table9262
+ GCC_except_table9296
+ GCC_except_table9300
+ GCC_except_table9306
+ GCC_except_table9308
+ GCC_except_table9314
+ GCC_except_table9317
+ GCC_except_table9352
+ GCC_except_table9396
+ GCC_except_table9520
+ GCC_except_table9534
+ GCC_except_table9559
+ GCC_except_table9561
+ GCC_except_table9563
+ GCC_except_table9565
+ GCC_except_table9566
+ GCC_except_table9572
+ GCC_except_table9574
+ GCC_except_table9575
+ GCC_except_table9584
+ GCC_except_table9588
+ GCC_except_table9591
+ GCC_except_table9641
+ GCC_except_table9642
+ GCC_except_table9643
+ GCC_except_table966
+ GCC_except_table9660
+ GCC_except_table9665
+ GCC_except_table9678
+ GCC_except_table9712
+ GCC_except_table9723
+ GCC_except_table9753
+ GCC_except_table9784
+ GCC_except_table9867
+ GCC_except_table9868
+ GCC_except_table9899
+ GCC_except_table9900
+ GCC_except_table9905
+ GCC_except_table9907
+ GCC_except_table9908
+ GCC_except_table9910
+ GCC_except_table9912
+ GCC_except_table9913
+ GCC_except_table9981
+ GCC_except_table9990
+ OBJC_IVAR_$_PLSearchIndexingEngineLibraryServicesProvider._lazyLogger
+ _CPLRecordModificationDatePrecision
+ _LEOLexemeIDInvalid
+ _NSUbiquitousKeyValueStoreChangedKeysKey
+ _NSUbiquitousKeyValueStoreDidChangeExternallyNotification
+ _OBJC_CLASS_$_NSFileCoordinator
+ _OBJC_CLASS_$_PLBackgroundJobLowPrioritySearchIndexingWorker
+ _OBJC_CLASS_$_PLFeatureAvailabilityLexemeCriteria
+ _OBJC_CLASS_$_PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing
+ _OBJC_CLASS_$_PLModelMigrationAction_ReevaluateAllowedForAnalysisForUnknownKindAssets
+ _OBJC_CLASS_$_PLModelMigrationAction_SetKeepOriginalsPrefetchModeForVisualIntelligenceLibrary
+ _OBJC_CLASS_$_PLModelMigrationAction_SetRunOnceFlagToLinkOrphanedCollectionShareContributors
+ _OBJC_CLASS_$_PLSharedAlbumsActivityKVSListener
+ _OBJC_CLASS_$_PLSyndicationResourceFileCoordinator
+ _OBJC_IVAR_$_PLBackgroundJobService._lazyProcessingSetURL
+ _OBJC_IVAR_$_PLBackgroundJobWorkerPendingWorkItems._zeroWorkItemsForCurrentCriteria
+ _OBJC_IVAR_$_PLFeatureAvailabilityLexemeCriteria._notAllowedForAnalysisID
+ _OBJC_IVAR_$_PLFeatureAvailabilityLexemeCriteria._notInHighlightID
+ _OBJC_IVAR_$_PLFeatureAvailabilityLexemeCriteria._savedAssetTypeByLexemeID
+ _OBJC_IVAR_$_PLFeatureAvailabilityLexemeCriteria._validImageCaptionByLexemeID
+ _OBJC_IVAR_$_PLFeatureAvailabilityLexemeCriteria._validImageEmbeddingByLexemeID
+ _OBJC_IVAR_$_PLFeatureAvailabilityLexemeCriteria._validMediaAnalysisByLexemeID
+ _OBJC_IVAR_$_PLFeatureAvailabilityLexemeCriteria._validMediaAnalysisImageByLexemeID
+ _OBJC_IVAR_$_PLFeatureAvailabilityLexemeCriteria._validRichImageCaptionByLexemeID
+ _OBJC_IVAR_$_PLFeatureAvailabilityLexemeCriteria._validSceneAnalysisByLexemeID
+ _OBJC_IVAR_$_PLFeatureAvailabilityLexemeCriteria._versionProvider
+ _OBJC_IVAR_$_PLNotificationManager._kvsListener
+ _OBJC_IVAR_$_PLPhotoLibraryBundleController._stateCaptureHandler
+ _OBJC_IVAR_$_PLPhotoLibraryBundleController._stateLock
+ _OBJC_IVAR_$_PLPhotoLibraryBundleController._stateLock_lastBundleShutdownDate
+ _OBJC_IVAR_$_PLPhotoLibraryBundleController._stateLock_lastBundleShutdownLibraryID
+ _OBJC_IVAR_$_PLPhotoLibraryBundleController._stateLock_lastBundleShutdownReason
+ _OBJC_IVAR_$_PLRebuildUserNotification._libraryPath
+ _OBJC_IVAR_$_PLSearchIndexingEngine._queue_timeOfLastSearchProgressReport
+ _OBJC_IVAR_$_PLSearchIndexingRebuildEngine._libraryServicesProvider
+ _OBJC_IVAR_$_PLSharedAlbumsActivityKVSListener._delegate
+ _OBJC_IVAR_$_PLSharedAlbumsActivityKVSListener._isListening
+ _OBJC_IVAR_$_PLSharedAlbumsActivityKVSListener._kvStore
+ _OBJC_IVAR_$_PLSharedAlbumsActivityKVSListener._lock
+ _OBJC_IVAR_$_PLSharedAlbumsActivityKVSListener._lock_cachedEventLogLastEnteredDate
+ _OBJC_IVAR_$_PLSharedAlbumsActivityKVSListener._lock_cachedLastSeenDate
+ _OBJC_IVAR_$_PLSyndicationResourceFileCoordinator._copiedPrimaryURL
+ _OBJC_IVAR_$_PLSyndicationResourceFileCoordinator._copiedVideoComplementURL
+ _OBJC_IVAR_$_PLSyndicationResourceFileCoordinator._materializesDatalessFiles
+ _OBJC_IVAR_$_PLSyndicationResourceFileCoordinator._originalFilename
+ _OBJC_IVAR_$_PLSyndicationResourceFileCoordinator._pathManager
+ _OBJC_IVAR_$_PLSyndicationResourceFileCoordinator._sourceURL
+ _OBJC_IVAR_$_PLSyndicationResourceFileCoordinator._videoComplementFilename
+ _OBJC_IVAR_$_PLSyndicationResourceFileCoordinator._videoComplementSourceURL
+ _OBJC_METACLASS_$_PLBackgroundJobLowPrioritySearchIndexingWorker
+ _OBJC_METACLASS_$_PLFeatureAvailabilityLexemeCriteria
+ _OBJC_METACLASS_$_PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing
+ _OBJC_METACLASS_$_PLModelMigrationAction_ReevaluateAllowedForAnalysisForUnknownKindAssets
+ _OBJC_METACLASS_$_PLModelMigrationAction_SetKeepOriginalsPrefetchModeForVisualIntelligenceLibrary
+ _OBJC_METACLASS_$_PLModelMigrationAction_SetRunOnceFlagToLinkOrphanedCollectionShareContributors
+ _OBJC_METACLASS_$_PLSharedAlbumsActivityKVSListener
+ _OBJC_METACLASS_$_PLSyndicationResourceFileCoordinator
+ _PLCloudSharedCommentPredicateForCollectionShare
+ _PLFeatureAvailabilityLexemeEvaluationResultCaptionsAreCurrent
+ _PLFileSystemImportCurrentVersion_block_invoke.s_cplAssetDirectoryPrefix
+ _PLFileSystemImportCurrentVersion_block_invoke.s_onceToken
+ _PLIncludeImageEmbeddingVersionInPredicate
+ _PLIsErrorOrUnderlyingErrorDatalessMaterializationPrevented
+ _PLLibraryIdentifierSupportsSearchProgressReporting
+ _PLPlatformVisualIntelligenceSyncSupported
+ _PLSearchIndexProgressAnalyzedAndIndexedCountKey
+ _PLSearchIndexProgressInIndexCountKey
+ _PLSearchIndexProgressNeedingDonationCountKey
+ _PLSearchIndexProgressPartiallyDonatedCountKey
+ _PLSearchIndexProgressTotalAssetCountKey
+ _PLStringFromCoreAnalyticsLibraryID
+ _PLSyndicationCSProvideOptionsAllowDownload
+ __OBJC_$_CLASS_METHODS_PLBackgroundJobLowPrioritySearchIndexingWorker
+ __OBJC_$_CLASS_METHODS_PLFeatureAvailabilityLexemeCriteria
+ __OBJC_$_CLASS_METHODS_PLSyndicationResourceFileCoordinator
+ __OBJC_$_INSTANCE_METHODS_PLBackgroundJobLowPrioritySearchIndexingWorker
+ __OBJC_$_INSTANCE_METHODS_PLFeatureAvailabilityLexemeCriteria
+ __OBJC_$_INSTANCE_METHODS_PLManagedFolder(PLJournalEntryPayload)
+ __OBJC_$_INSTANCE_METHODS_PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing
+ __OBJC_$_INSTANCE_METHODS_PLModelMigrationAction_ReevaluateAllowedForAnalysisForUnknownKindAssets
+ __OBJC_$_INSTANCE_METHODS_PLModelMigrationAction_SetKeepOriginalsPrefetchModeForVisualIntelligenceLibrary
+ __OBJC_$_INSTANCE_METHODS_PLModelMigrationAction_SetRunOnceFlagToLinkOrphanedCollectionShareContributors
+ __OBJC_$_INSTANCE_METHODS_PLSharedAlbumsActivityKVSListener
+ __OBJC_$_INSTANCE_METHODS_PLSyndicationResourceFileCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_PLFeatureAvailabilityLexemeCriteria
+ __OBJC_$_INSTANCE_VARIABLES_PLSharedAlbumsActivityKVSListener
+ __OBJC_$_INSTANCE_VARIABLES_PLSyndicationResourceFileCoordinator
+ __OBJC_$_PROP_LIST_PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing
+ __OBJC_$_PROP_LIST_PLModelMigrationAction_ReevaluateAllowedForAnalysisForUnknownKindAssets
+ __OBJC_$_PROP_LIST_PLModelMigrationAction_SetKeepOriginalsPrefetchModeForVisualIntelligenceLibrary
+ __OBJC_$_PROP_LIST_PLModelMigrationAction_SetRunOnceFlagToLinkOrphanedCollectionShareContributors
+ __OBJC_$_PROP_LIST_PLSharedAlbumsActivityKVSListener
+ __OBJC_$_PROP_LIST_PLSyndicationResourceFileCoordinator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PLPhotoAnalysisServiceClientOperationCancelling
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PLPhotoAnalysisServiceClientVisionCancelling
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PLSharedAlbumsActivityKVSListenerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PLPhotoAnalysisServiceClientOperationCancelling
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PLPhotoAnalysisServiceClientVisionCancelling
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PLSharedAlbumsActivityKVSListenerDelegate
+ __OBJC_$_PROTOCOL_REFS_PLPhotoAnalysisServiceClientOperationCancelling
+ __OBJC_$_PROTOCOL_REFS_PLPhotoAnalysisServiceClientVisionCancelling
+ __OBJC_$_PROTOCOL_REFS_PLSharedAlbumsActivityKVSListenerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing
+ __OBJC_CLASS_PROTOCOLS_$_PLModelMigrationAction_ReevaluateAllowedForAnalysisForUnknownKindAssets
+ __OBJC_CLASS_PROTOCOLS_$_PLModelMigrationAction_SetKeepOriginalsPrefetchModeForVisualIntelligenceLibrary
+ __OBJC_CLASS_PROTOCOLS_$_PLModelMigrationAction_SetRunOnceFlagToLinkOrphanedCollectionShareContributors
+ __OBJC_CLASS_PROTOCOLS_$_PLPhotoLibraryBundleController
+ __OBJC_CLASS_RO_$_PLBackgroundJobLowPrioritySearchIndexingWorker
+ __OBJC_CLASS_RO_$_PLFeatureAvailabilityLexemeCriteria
+ __OBJC_CLASS_RO_$_PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing
+ __OBJC_CLASS_RO_$_PLModelMigrationAction_ReevaluateAllowedForAnalysisForUnknownKindAssets
+ __OBJC_CLASS_RO_$_PLModelMigrationAction_SetKeepOriginalsPrefetchModeForVisualIntelligenceLibrary
+ __OBJC_CLASS_RO_$_PLModelMigrationAction_SetRunOnceFlagToLinkOrphanedCollectionShareContributors
+ __OBJC_CLASS_RO_$_PLSharedAlbumsActivityKVSListener
+ __OBJC_CLASS_RO_$_PLSyndicationResourceFileCoordinator
+ __OBJC_LABEL_PROTOCOL_$_PLPhotoAnalysisServiceClientOperationCancelling
+ __OBJC_LABEL_PROTOCOL_$_PLPhotoAnalysisServiceClientVisionCancelling
+ __OBJC_LABEL_PROTOCOL_$_PLSharedAlbumsActivityKVSListenerDelegate
+ __OBJC_METACLASS_RO_$_PLBackgroundJobLowPrioritySearchIndexingWorker
+ __OBJC_METACLASS_RO_$_PLFeatureAvailabilityLexemeCriteria
+ __OBJC_METACLASS_RO_$_PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing
+ __OBJC_METACLASS_RO_$_PLModelMigrationAction_ReevaluateAllowedForAnalysisForUnknownKindAssets
+ __OBJC_METACLASS_RO_$_PLModelMigrationAction_SetKeepOriginalsPrefetchModeForVisualIntelligenceLibrary
+ __OBJC_METACLASS_RO_$_PLModelMigrationAction_SetRunOnceFlagToLinkOrphanedCollectionShareContributors
+ __OBJC_METACLASS_RO_$_PLSharedAlbumsActivityKVSListener
+ __OBJC_METACLASS_RO_$_PLSyndicationResourceFileCoordinator
+ __OBJC_PROTOCOL_$_PLPhotoAnalysisServiceClientOperationCancelling
+ __OBJC_PROTOCOL_$_PLPhotoAnalysisServiceClientVisionCancelling
+ __OBJC_PROTOCOL_$_PLSharedAlbumsActivityKVSListenerDelegate
+ __PLSafeEntityForNameInManagedObjectContext
+ __PLSyndicationResourceFileCoordinatorError
+ ___100-[PLBackgroundJobSyndicationAssetCleanupWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___101-[PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing _originalPrimaryImageResourceForAsset:]_block_invoke
+ ___103-[PLBackgroundJobSharedAssetContainerUpdateWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___103-[PLBackgroundJobSharedAssetContainerUpdateWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke_2
+ ___103-[PLFeatureAvailabilityLexemeCriteria evaluateLexemeIDsByCategoryDictionary:foundUnrecognizedLexemeID:]_block_invoke
+ ___106-[PLBackgroundJobDeferredRenderDerivativesBaseWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___106-[PLBackgroundJobResourceUploadExtensionRunnerWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___106-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:searchProgressOnly:completionHandler:]_block_invoke
+ ___106-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:searchProgressOnly:completionHandler:]_block_invoke_2
+ ___106-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:searchProgressOnly:completionHandler:]_block_invoke_3
+ ___106-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:searchProgressOnly:completionHandler:]_block_invoke_4
+ ___106-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:searchProgressOnly:completionHandler:]_block_invoke_5
+ ___106-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:searchProgressOnly:completionHandler:]_block_invoke_6
+ ___106-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:searchProgressOnly:completionHandler:]_block_invoke_7
+ ___106-[PLIntensiveResourceTask tryPreparingForReplacementWithNewResponder:existingResponders:existingProgress:]_block_invoke
+ ___106-[PLSearchIndexingEngine getSearchDonationProgressInLibrary:shouldCompute:shouldReport:completionHandler:]_block_invoke
+ ___106-[PLSearchIndexingEngine getSearchDonationProgressInLibrary:shouldCompute:shouldReport:completionHandler:]_block_invoke_2
+ ___106-[PLSearchIndexingEngine getSearchDonationProgressInLibrary:shouldCompute:shouldReport:completionHandler:]_block_invoke_3
+ ___106-[PLSearchIndexingEngine getSearchDonationProgressInLibrary:shouldCompute:shouldReport:completionHandler:]_block_invoke_4
+ ___106-[PLSearchIndexingEngine getSearchDonationProgressInLibrary:shouldCompute:shouldReport:completionHandler:]_block_invoke_5
+ ___107-[PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing performActionWithManagedObjectContext:error:]_block_invoke
+ ___108-[PLBackgroundJobSyndicationResourceSanitizationWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___116-[PLSyndicationSyncServiceWrapper executeQueryForSyncManager:type:startDate:endDate:itemsHandler:completionHandler:]_block_invoke
+ ___119-[PLModelMigrationAction_ReevaluateAllowedForAnalysisForUnknownKindAssets performActionWithManagedObjectContext:error:]_block_invoke
+ ___124-[PLBackgroundJobResourceUploadExtensionRunnerWorker criteriaNeedingProcessingInLibrary:currentCriteria:outSignalAgainDate:]_block_invoke
+ ___137-[PLSyndicationResourceDataStore _copyProviderFileWantsVideoComplement:fromCoordinator:fileIdentifier:pathManager:copiedURL:inode:error:]_block_invoke
+ ___139+[PLSyndicationResourceDataStore _provideSourceURLsForBundleID:syndicationIdentifier:typeIdentifier:isLivePhoto:options:completionHandler:]_block_invoke
+ ___155-[PLSyndicationResourceDataStore _copyAndMarkAsLocallyAvailablePairedLivePhotoResourceForRequestedResource:requestedVideoComplement:fileCoordinator:error:]_block_invoke
+ ___167+[PLSyndicationResourceDataStore provideFileURLAndUnwrapLivePhotoIfNeededForItemIdentifiersWithBundleIDs:destURLs:pathManager:options:resultHandler:completionHandler:]_block_invoke
+ ___197+[PLIntensiveResourceTask(Constructors) taskForGeneratingDeferredAdjustmentForAsset:trackingIdentifier:imageConversionClient:videoConversionClient:reason:clientBundleID:allowCancellationByService:]_block_invoke_3
+ ___202-[PLManagedAsset _generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:retryNumber:allowCancellationByService:clientBundleID:shouldSaveMediaConversionResultBlock:completion:]_block_invoke
+ ___202-[PLManagedAsset _generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:retryNumber:allowCancellationByService:clientBundleID:shouldSaveMediaConversionResultBlock:completion:]_block_invoke_2
+ ___41-[PLCPLSettings hasPersistedPrefetchMode]_block_invoke
+ ___54-[PLIntensiveResourceTask transitionToUninterruptible]_block_invoke
+ ___55-[PLBackgroundJobWorkerTypesBuffer redactedDescription]_block_invoke
+ ___56-[PLPhotoLibraryBundleController stateCaptureDictionary]_block_invoke
+ ___57-[PLFeatureAvailabilityLexemeCriteria evaluateLexemeIDs:]_block_invoke
+ ___61-[PLBackgroundJobService initWithWorkerClasses:statusCenter:]_block_invoke_3
+ ___61-[PLSearchIndexingEngineLibraryServicesProvider initWithLSM:]_block_invoke
+ ___66+[PLShareParticipant orphanedCPLContributorRecordsInPhotoLibrary:]_block_invoke
+ ___67-[PLBackgroundJobWorker pendingWorkItemsInLibrary:currentCriteria:]_block_invoke
+ ___67-[PLBackgroundJobWorker pendingWorkItemsInLibrary:currentCriteria:]_block_invoke_2
+ ___68-[PLPhotoLibraryBundleController _updateStateCaptureInfo:libraryID:]_block_invoke
+ ___70-[PLBackgroundJobLowPrioritySearchIndexingWorker locrIdentifyingBlock]_block_invoke
+ ___72-[PLManagedObjectPagingIterator countRemainingWithManagedObjectContext:]_block_invoke
+ ___72-[PLManagedObjectPagingIterator countRemainingWithManagedObjectContext:]_block_invoke_2
+ ___72-[PLManagedObjectPagingIterator countRemainingWithManagedObjectContext:]_block_invoke_3
+ ___72-[PLManagedObjectPagingIterator countRemainingWithManagedObjectContext:]_block_invoke_4
+ ___74-[PLSearchIndexingRebuildEngine _inq_performRebuildForLibrary:completion:]_block_invoke
+ ___74-[PLSearchIndexingRebuildEngine _inq_performRebuildForLibrary:completion:]_block_invoke_2
+ ___74-[PLSearchIndexingRebuildEngine _inq_performRebuildForLibrary:completion:]_block_invoke_3
+ ___82+[PLShareParticipant linkCPLContributorContentWithUserIdentifiers:inPhotoLibrary:]_block_invoke
+ ___84-[PLSyndicationResourceFileCoordinator _coordinateReadingSourcesWithError:accessor:]_block_invoke
+ ___84-[PLSyndicationResourceFileCoordinator _coordinateReadingSourcesWithError:accessor:]_block_invoke_2
+ ___85-[PLBackgroundJobWorker pendingCriteriaInLibrary:currentCriteria:outSignalAgainDate:]_block_invoke
+ ___85-[PLBackgroundJobWorker pendingCriteriaInLibrary:currentCriteria:outSignalAgainDate:]_block_invoke_2
+ ___86-[PLCloudPhotoLibraryManager _linkOrphanedCollectionShareContributorsWithCPLSettings:]_block_invoke
+ ___86-[PLCloudPhotoLibraryManager _linkOrphanedCollectionShareContributorsWithCPLSettings:]_block_invoke_2
+ ___87-[PLBackgroundJobPersonSyncWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___87-[PLBackgroundJobStableHashWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___90-[PLBackgroundJobEditRenderingWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___91-[PLBackgroundJobSearchIndexingWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___93-[PLAssetsdLibraryInternalService getSearchDonationProgressShouldCompute:shouldReport:reply:]_block_invoke
+ ___94-[PLBackgroundJobDuplicateDetectorWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___97-[PLBackgroundJobResourceAvailabilityWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___98-[PLCloudPhotoLibraryManager _collectContributorUserIdentifiersForRecords:into:completionHandler:]_block_invoke
+ ___98-[PLCloudPhotoLibraryManager _collectContributorUserIdentifiersForRecords:into:completionHandler:]_block_invoke_2
+ ___98-[PLSyndicationResourceFileCoordinator copyToPrimaryDestination:videoComplementDestination:error:]_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64s72bs80r_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8s72l8s56l8r80l8s64l8
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88bs96bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8s88l8s56l8s64l8s72l8s96l8s80l8
+ ___block_descriptor_121_e8_32s40s48s56s64s72s80s88s96s104s112r_e32_v32?0"PLManagedObject"8Q16^B24ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8r112l8s96l8s104l8
+ ___block_descriptor_122_e8_32s40s48s56s64s72s80s88r96r104r_e5_v8?0ls32l8s40l8r88l8s48l8s56l8r96l8r104l8s64l8s72l8s80l8
+ ___block_descriptor_124_e8_32s40s48s56s64s72s80s88s96s104bs112r_e37_v32?0"NSURL"8"NSURL"16"NSError"24ls32l8s104l8s40l8s48l8s56l8r112l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_136_e8_32s40s48s56s64s72s80s88bs96bs104r112r120r_e5_v8?0ls32l8s40l8r104l8s48l8r112l8s56l8s64l8s72l8s80l8s88l8s96l8r120l8
+ ___block_descriptor_137_e8_32s40s48s56s64s72s80s88s96s104s112bs120n11_8_8_s0_t8w8_e5_v8?0l
+ ___block_descriptor_144_e8_32s40s48s56r64r72r80r88r96r104r112r120r128r_e53_v40?0"LEOItem"8"PLLeoLexemeIDSet"16"NSDate"24^B32ls32l8s40l8r56l8r64l8r72l8r80l8r88l8r96l8s48l8r104l8r112l8r120l8r128l8
+ ___block_descriptor_176_e8_32s40s48s56s64s72s80s88s96s104s112s120bs128r136r144r152r160r_e5_v8?0ls32l8s40l8r128l8s48l8r136l8s56l8s64l8s72l8s120l8r144l8s80l8s88l8r152l8s96l8r160l8s104l8s112l8
+ ___block_descriptor_184_e8_32s40s48s56s64s72s80s88s96s104s112s120s128bs136bs144bs152r160r_e63_v60?0B8"NSURL"12"NSURL"20Q28q36"NSDictionary"44"NSError"52ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s128l8r152l8s88l8r160l8s96l8s104l8s112l8s120l8s136l8s144l8
+ ___block_descriptor_40_e8_32bs_e20_v48?0Q8Q16Q24Q32Q40ls32l8
+ ___block_descriptor_40_e8_32r_e24_v16?0"PLPhotoLibrary"8lr32l8
+ ___block_descriptor_40_e8_32s_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e53_v32?0"CPLScopedIdentifier"8"CPLRecordChange"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e71_v32?0"PLManagedObject"8"CPLScopedIdentifier"16"PLCollectionShare"24ls32l8
+ ___block_descriptor_48_e8_32s40bs_e27_v24?0"NSURL"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e31_v16?0"PLFeatureAvailability"8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e12_v20?0I8^B12ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e15_v32?08Q16^B24lr40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e15_v16?0"NSURL"8lr48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e37_v32?0"NSNumber"8"NSIndexSet"16^B24ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v48?0Q8Q16Q24Q32Q40ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e27_v24?0"NSURL"8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e24_v16?0"PLPhotoLibrary"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40r48r56r_e24_v16?0"PLManagedAsset"8ls32l8r40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48r_e71_v32?0"PLManagedObject"8"CPLScopedIdentifier"16"PLCollectionShare"24ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e34_v24?0"NSDictionary"8"NSError"16ls56l8s32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48bs56bs_e31_v16?0"PLFeatureAvailability"8ls48l8s32l8s40l8s56l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e15_v16?0"NSURL"8ls32l8r56l8s48l8s40l8r64l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e24_v16?0"PLPhotoLibrary"8ls32l8s40l8r48l8r56l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e25_v24?0"NSURL"8"NSURL"16ls32l8r56l8s40l8s48l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0lr56l8s32l8s40l8s48l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56r64r72r_e5_v8?0ls32l8s40l8r56l8s48l8r64l8r72l8
+ ___block_descriptor_81_e8_32s40s48s56r64r72r_e27_v24?0"NSURL"8"NSError"16ls32l8r56l8s40l8r64l8s48l8r72l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8s56l8s80l8s64l8s72l8
+ __hasChangesForCloudShared:.pl_once_object_48
+ __hasChangesForCloudShared:.pl_once_token_48
+ _changeNotificationObjectIDKeys.pl_once_object_45
+ _changeNotificationObjectIDKeys.pl_once_token_45
+ _changeNotificationObjectIDMutationKeys.pl_once_object_44
+ _changeNotificationObjectIDMutationKeys.pl_once_token_44
+ _changeNotificationObjectKeys.pl_once_object_43
+ _changeNotificationObjectKeys.pl_once_token_43
+ _objc_msgSend$_allAssetsAreSavedToLibraryForCollectionShare:inContext:
+ _objc_msgSend$_allCriteriaToUse
+ _objc_msgSend$_applyDefaultPrefetchModeIfNeededWithCPLSettings:createOptions:
+ _objc_msgSend$_assetHasOriginalFileOnDisk:
+ _objc_msgSend$_calculateDonationCountsFromSnapshot:resultHandler:
+ _objc_msgSend$_clearDeferredProcessingNeededForAsset:originalWidth:originalHeight:
+ _objc_msgSend$_cloneResourcesForSharePlaceholderAsset:sourceAsset:shouldBakeInAdjustments:shouldFlattenLivePhoto:withPlaceholderResourceURLToSourceResourceURLMap:fileManager:photoLibrary:
+ _objc_msgSend$_collectContributorUserIdentifiersForRecords:into:completionHandler:
+ _objc_msgSend$_coordinateReadingSourcesWithError:accessor:
+ _objc_msgSend$_copyAndMarkAsLocallyAvailablePairedLivePhotoResourceForRequestedResource:requestedVideoComplement:fileCoordinator:error:
+ _objc_msgSend$_copyFileAtURL:toDestination:error:
+ _objc_msgSend$_copyProvidedFilesForItemIdentifier:providerURL:primaryDestination:videoComplementDestination:pathManager:materializesDatalessFiles:resultHandler:
+ _objc_msgSend$_copyProviderFileWantsVideoComplement:fromCoordinator:fileIdentifier:pathManager:copiedURL:inode:error:
+ _objc_msgSend$_cplParticipantsWithBlockedIdentitiesLast:
+ _objc_msgSend$_createLogger
+ _objc_msgSend$_defaultResult
+ _objc_msgSend$_enumerateUnattributedCPLContributorContentInPhotoLibrary:usingBlock:
+ _objc_msgSend$_errorForCopyFailure:sourceURL:
+ _objc_msgSend$_forcefullyInvokeCurrentManagedObjectCompletionHandler
+ _objc_msgSend$_generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:retryNumber:allowCancellationByService:clientBundleID:shouldSaveMediaConversionResultBlock:completion:
+ _objc_msgSend$_getProcessingSetURL
+ _objc_msgSend$_imageCaptionDefaultsToCurrent
+ _objc_msgSend$_imageEmbeddingDefaultsToCurrent
+ _objc_msgSend$_inq_pendingJobsForBundle:workerTypes:currentCriteria:
+ _objc_msgSend$_inq_pendingJobsOnBuffer:currentCriteria:
+ _objc_msgSend$_inq_pendingJobsOnBundles:currentCriteria:
+ _objc_msgSend$_inq_performRebuildForLibrary:completion:
+ _objc_msgSend$_isDestinationURLInsideSyndicationOriginals:
+ _objc_msgSend$_leo_computeSnapshotForPhotoLibrary:searchProgressOnly:completionHandler:
+ _objc_msgSend$_linkOrphanedCollectionShareContributorsWithCPLSettings:
+ _objc_msgSend$_lock_addResponder:
+ _objc_msgSend$_lock_isRunning
+ _objc_msgSend$_mediaAnalysisImageDefaultsToCurrent
+ _objc_msgSend$_objectsMatchingPredicate:entityName:
+ _objc_msgSend$_objectsMatchingPredicate:entityName:inManagedObjectContext:
+ _objc_msgSend$_originalPrimaryImageResourceForAsset:
+ _objc_msgSend$_processCapturePipelineAsset:originalResource:reingested:
+ _objc_msgSend$_processSemanticEnhanceAsset:originalResource:
+ _objc_msgSend$_provideSourceURLsForBundleID:syndicationIdentifier:typeIdentifier:isLivePhoto:options:completionHandler:
+ _objc_msgSend$_richImageCaptionDefaultsToCurrent
+ _objc_msgSend$_setKeywordsFromMetadata:
+ _objc_msgSend$_setRatingFromMetadata:
+ _objc_msgSend$_syncOutputProgress:toSourceProgress:
+ _objc_msgSend$_unpackLivePhotoBundleAtURL:primaryURL:videoComplementURL:error:
+ _objc_msgSend$_updateCachedEventLogLastEnteredDate
+ _objc_msgSend$_updateCachedLastSeenDate
+ _objc_msgSend$_updateShareParticipantWithContributorUserIdentifier:collectionShare:inPhotoLibrary:
+ _objc_msgSend$_updateStateCaptureInfo:libraryID:
+ _objc_msgSend$backgroundJobWorkerTypesMaskGuestAssetSync:personSync:syndicationSync:syndicationResourceSanitization:syndicationResourceDownload:syndicationAssetCleanup:assetStack:duplicateDetector:deferredRenderDerivativesLowPriority:deferredRenderDerivativesHighPriority:resourceAvailability:stableHash:editRenderingImage:editRenderingVideo:highPrioritySearchIndexing:lowPrioritySearchIndexing:sharedAssetContainerUpdate:assetResourceUploadJob:assetResourceUploadExtensionRunner:featureAvailability:optimizeTableThumbs:cascadeDonation:provenanceTimestamp:
+ _objc_msgSend$computeSearchProgressForPhotoLibrary:completionHandler:
+ _objc_msgSend$confidenceForMomentEdge:
+ _objc_msgSend$coordinateReadingItemAtURL:options:error:byAccessor:
+ _objc_msgSend$copiedPrimaryURL
+ _objc_msgSend$copiedVideoComplementURL
+ _objc_msgSend$copyJobContentsToHoldingDirectoryWithUUID:incomingPath:job:
+ _objc_msgSend$copyToPrimaryDestination:videoComplementDestination:error:
+ _objc_msgSend$countOfSharesWithUnreadBadgeActivitySinceLastSeenDate:eventLogDate:inManagedObjectContext:
+ _objc_msgSend$countRemainingWithManagedObjectContext:
+ _objc_msgSend$criteriaNeedingProcessingInLibrary:currentCriteria:outSignalAgainDate:
+ _objc_msgSend$defaultStore
+ _objc_msgSend$evaluateLexemeIDs:
+ _objc_msgSend$eventLogLastEnteredDate
+ _objc_msgSend$executeQueryForSyncManager:type:startDate:endDate:itemsHandler:completionHandler:
+ _objc_msgSend$featureAnalysisLexemeCategories
+ _objc_msgSend$generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:allowCancellationByService:clientBundleID:shouldSaveMediaConversionResultBlock:completion:
+ _objc_msgSend$getCloudCacheRecordsWithLocalScopedIdentifiers:desiredProperties:completionHandler:
+ _objc_msgSend$getSearchDonationProgressInLibrary:shouldCompute:shouldReport:completionHandler:
+ _objc_msgSend$hasPersistedPrefetchMode
+ _objc_msgSend$initWithFilePresenter:
+ _objc_msgSend$initWithLexemes:versionProvider:
+ _objc_msgSend$initWithMessage:libraryPath:
+ _objc_msgSend$initWithSourceURL:videoComplementSourceURL:pathManager:materializesDatalessFiles:
+ _objc_msgSend$initWithZeroWorkItemsForCurrentCriteria
+ _objc_msgSend$installFinalImageOrVideoAndRemoveDeferredFilesWithFinalImageURL:previewImage:thumbnailImage:useExistingAsset:outError:
+ _objc_msgSend$isAuthorizedAssetUUID:inManagedObjectContext:
+ _objc_msgSend$isEntitledForPrivatePhotosTCCForToken:
+ _objc_msgSend$isListening
+ _objc_msgSend$kvsListener
+ _objc_msgSend$kvsListenerDidUpdateEventLogLastEnteredDate:
+ _objc_msgSend$kvsListenerDidUpdateLastSeenDate:
+ _objc_msgSend$lastEditedDate
+ _objc_msgSend$lastSeenDate
+ _objc_msgSend$libraryPath
+ _objc_msgSend$linkCPLContributorContentWithUserIdentifiers:inPhotoLibrary:
+ _objc_msgSend$materializesDatalessFiles
+ _objc_msgSend$notificationPredicateForFilter:
+ _objc_msgSend$orphanedCPLContributorRecordsInPhotoLibrary:
+ _objc_msgSend$path:isSubpathOfPhotoDirectoryWithType:
+ _objc_msgSend$pendingCriteriaInLibrary:currentCriteria:outSignalAgainDate:
+ _objc_msgSend$pendingWorkItemsInLibrary:currentCriteria:
+ _objc_msgSend$performTransaction:withName:
+ _objc_msgSend$predicateForMigratedCPLCollectionShares
+ _objc_msgSend$predicateForPostsFromOthersCreatedAfterSubscriptionSinceDate:
+ _objc_msgSend$provideFileURLAndUnwrapLivePhotoIfNeededForItemIdentifiersWithBundleIDs:destURLs:pathManager:options:resultHandler:completionHandler:
+ _objc_msgSend$reconcileOrphanedRelationshipsWithCPLCollectionShare:
+ _objc_msgSend$setAllowEmbeddedThumbnails:
+ _objc_msgSend$setIsListening:
+ _objc_msgSend$setLastEditedDate:
+ _objc_msgSend$setPrefetchModeSchedulingResourceUpdate:error:
+ _objc_msgSend$setShareContributorUserIdentifier:
+ _objc_msgSend$setZeroWorkItemsForCurrentCriteria:
+ _objc_msgSend$setupPlaceholderAssetWithRequiredPropertiesFromSourceAsset:placeholderAssetUUID:bundleScope:share:importSessionID:bakeInAdjustmentsFromSourceAsset:flattenLivePhoto:copyTitleDescriptionAndKeywords:copyCameraProcessingAdjustmentResources:copyLocationData:copyProvenanceData:isCurrentUser:library:
+ _objc_msgSend$sourceURL
+ _objc_msgSend$starRating
+ _objc_msgSend$stateCaptureDictionariesForAllHandlers
+ _objc_msgSend$supportsSearchProgressReporting
+ _objc_msgSend$transitionToUninterruptible
+ _objc_msgSend$tryPreparingForReplacementWithNewResponder:existingResponders:existingProgress:
+ _objc_msgSend$updateImageExtendedGenerativeAttributesFromMetadata:policy:
+ _objc_msgSend$videoComplementFilename
+ _objc_msgSend$videoComplementSourceURL
+ _objc_msgSend$workItemsNeedingProcessingInLibrary:currentCriteria:
+ _objc_msgSend$zeroWorkItemsForCurrentCriteria
+ _predicateToExcludeAssetsMissingMasterThumbnailsWithThumbnailIndexKeyPath:.pl_once_object_14
+ _predicateToExcludeAssetsMissingMasterThumbnailsWithThumbnailIndexKeyPath:.pl_once_token_14
+ _predicateToExcludeCameraAutoAdjustments.pl_once_object_15
+ _predicateToExcludeCameraAutoAdjustments.pl_once_token_15
+ _predicateToExcludeHiddenAssetsWithHiddenKeyPath:.pl_once_object_10
+ _predicateToExcludeHiddenAssetsWithHiddenKeyPath:.pl_once_token_10
+ _predicateToExcludeNonvisibleBurstAssets.pl_once_object_12
+ _predicateToExcludeNonvisibleBurstAssets.pl_once_token_12
+ _predicateToExcludeNonvisibleBurstAssetsWithAvalanchePickTypeKeyPath:.pl_once_object_13
+ _predicateToExcludeNonvisibleBurstAssetsWithAvalanchePickTypeKeyPath:.pl_once_token_13
+ _predicateToExcludeRestrictedLockedAssets.pl_once_object_11
+ _predicateToExcludeRestrictedLockedAssets.pl_once_token_11
+ _predicateToExcludeTrashedAssets.pl_once_object_8
+ _predicateToExcludeTrashedAssets.pl_once_token_8
+ _predicateToExcludeTrashedAssetsWithTrashedStateKeyPath:.pl_once_object_9
+ _predicateToExcludeTrashedAssetsWithTrashedStateKeyPath:.pl_once_token_9
- +[PFAdjustment(Validation) isValidArchiveDictionary:errors:]
- +[PFAdjustmentSerialization deserializeAdjustmentsFromData:error:]
- +[PFAdjustmentSerialization deserializeDictionaryFromData:error:]
- +[PFAdjustmentSerialization serializeAdjustments:error:]
- +[PFAdjustmentSerialization serializeDictionary:error:]
- +[PFAdjustmentSerialization(Utility) validateArchive:containsEntryWithKey:ofType:errors:]
- +[PFAdjustmentSerialization(Utility) validateValue:isOfType:errors:]
- +[PFAdjustmentStack(Validation) isValidEnvelopeDictionary:errors:]
- +[PLAggregateAlbumListChangeNotification notificationForAggregateAlbumList:fromAlbumListChangeNotification:indexOffset:]
- +[PLAssetSharingUtilities assetForVideoURL:metadata:library:outAudioMix:outVideoComposition:]
- +[PLBackgroundJobHighPrioritySearchIndexingWorker _criteriaToUse]
- +[PLBackgroundJobLowPriorityBatterySearchIndexingWorker _criteriaToUse]
- +[PLBackgroundJobLowPriorityChargerSearchIndexingWorker _criteriaToUse]
- +[PLBackgroundJobSearchIndexingWorker _criteriaToUse]
- +[PLBackgroundJobWorkerTypes backgroundJobWorkerTypesMaskGuestAssetSync:personSync:syndicationSync:syndicationResourceSanitization:syndicationResourceDownload:syndicationAssetCleanup:assetStack:duplicateDetector:deferredRenderDerivativesLowPriority:deferredRenderDerivativesHighPriority:resourceAvailability:stableHash:editRenderingImage:editRenderingVideo:highPrioritySearchIndexing:lowPriorityBatterySearchIndexing:lowPriorityChargerSearchIndexing:sharedAssetContainerUpdate:assetResourceUploadJob:assetResourceUploadExtensionRunner:featureAvailability:optimizeTableThumbs:cascadeDonation:provenanceTimestamp:]
- +[PLCloudCommentsChangeNotification notificationWithAsset:snapshot:]
- +[PLCloudFeedEntriesChangeNotification notificationWithFullReload]
- +[PLCloudFeedEntriesChangeNotification notificationWithInsertedEntries:updatedEntries:deletedEntries:]
- +[PLCloudFeedEntry allEntriesInLibrary:]
- +[PLCloudFeedEntry entryWithURIRepresentation:inLibrary:]
- +[PLCloudFeedEntry recentAssetsEntriesInLibrary:limit:]
- +[PLCloudMaster deleteAllCloudMastersInManagedObjectContext:]
- +[PLCloudMaster resetCloudMastersStateInManagedObjectContext:]
- +[PLCloudResource countOfLocalCloudResourcesOfType:inManagedObjectContext:localCount:unavailableCount:error:]
- +[PLCloudResource countOfMediumOriginalLocalCloudResourcesInManagedObjectContext:localCount:unavailableCount:error:]
- +[PLCloudResource nonLocalResourcesInManagedObjectContext:forAssetUUIDs:cplResourceTypes:]
- +[PLCloudResource resetPrefetchStateForResourcesWithResourceType:itemIdentifiers:inLibrary:]
- +[PLCloudSharedAlbumInvitationRecord cloudSharedAlbumInvitationRecordsWithAlbumGUID:inLibrary:]
- +[PLCloudSharedAlbumInvitationRecord cloudSharedAlbumInvitationRecordsWithGUIDs:inLibrary:]
- +[PLCloudStreamShareJob publishMediaFromSources:toNewSharedAlbumWithName:withCommentText:recipients:]
- +[PLCloudStreamShareJob publishMediaFromSources:toSharedAlbum:withCommentText:completionHandler:]
- +[PLDiagnostics addOSStateHandlerWithTitle:queue:propertyListHandler:]
- +[PLFeatureAvailability availabilityFromInvalidatingSearchIndexInFeatureAvailability:]
- +[PLFeatureAvailabilityComputer _featureAnalysisLexemeCategories]
- +[PLGlobalKeyValue fetchGlobalKeyValuesForKeys:withManagedObjectContext:]
- +[PLGraphEdge fetchEdgesWithExternalIdentifiers:inManagedObjectContext:]
- +[PLGraphNode fetchNodesWithExternalIdentifiers:inManagedObjectContext:]
- +[PLGraphNode fetchObjectIDsForNodesWithExternalIdentifiers:inManagedObjectContext:]
- +[PLInvitationRecordsChangeNotification notificationWithAlbum:snapshot:]
- +[PLJPEGThumbnailDecode decodeSessionOptionsForMaxPixelSize:]
- +[PLKeywordManager keywordsForAssets:]
- +[PLLocalChangeEventBuilder localEventFromTransaction:]
- +[PLManagedAlbumList facesAlbumListInManagedObjectContext:]
- +[PLManagedAlbumList placesAlbumListInManagedObjectContext:]
- +[PLManagedAlbumList placesAlbumListInPhotoLibrary:]
- +[PLManagedAlbumList scenesAlbumListInManagedObjectContext:]
- +[PLManagedAlbumList scenesAlbumListInPhotoLibrary:]
- +[PLManagedAsset assetsWithGroupingUUID:inManagedObjectContext:]
- +[PLManagedAsset cloudMasterMediaMetadataForAssetObjectID:managedObjectContext:error:]
- +[PLManagedAsset extensionForFullsizeThumbnailFile]
- +[PLManagedAsset fileURLFromAssetURL:photoLibrary:]
- +[PLManagedAsset guaranteedFlashOffForAssetAtURL:]
- +[PLManagedAsset pathForMutationsDirectoryWithDirectory:filename:]
- +[PLManagedAsset predicateForReframedAssets]
- +[PLManagedAsset ptpAssetIDForEventAndFilenameKey:]
- +[PLManagedAsset ptpResetEventAndFilenameMapping]
- +[PLManagedAsset ptpSetAssetIDForEventAndFilenameKey:value:]
- +[PLManagedAsset videoAssetsForMediaGroupUUID:moc:]
- +[PLManagedAsset(CPL) failedToPushAssetInLibrary:]
- +[PLManagedAsset(CPL) predicateForLocallyAvailablePrimaryStoreResourcesWithCPLResourceTypes:version:]
- +[PLManagedAsset(CPL) quarantinedAssetsInLibrary:]
- +[PLManagedAsset(CPL) resetAssetsCloudStateInLibrary:]
- +[PLManagedAsset(CPL) toUploadAssetsInLibrary:]
- +[PLManagedAsset(Share) _cloneResourcesForSharePlaceholderAsset:withPlaceholderResourceURLToSourceResourceURLMap:fileManager:photoLibrary:]
- +[PLManagedObjectContext changeNotificationObjectMutationKeys]
- +[PLManagedObjectContext sanitizedErrorFromError:]
- +[PLModelMigrator extractPathToAssetUUIDRecoveryMappingFromDatabasePath:]
- +[PLModelMigrator(Utilities) enumerateObjectsWithIncrementalSaveDefaultBatchSizeFetchRequest:managedObjectContext:count:error:block:]
- +[PLMoment allAssetsIncludedInMomentsInLibrary:]
- +[PLMoment(PLMoment_Private) batchFetchMomentObjectIDsByAssetObjectIDsWithAssetPredicate:inManagedObjectContext:error:]
- +[PLNLP ngramsFromTokens:ofSize:usingSeparator:]
- +[PLNotificationManager filteredAlbumListForContentMode:library:]
- +[PLPersistentContainer _installFTSIndexesInModel:]
- +[PLPersistentHistoryMarker markerWithTransaction:]
- +[PLPersistentHistoryUtilities fetchTransactionCountSinceToken:withContext:error:]
- +[PLPhotoLibrary CloudPhotoLibrarySize]
- +[PLPhotoLibrary setCloudAlbumSharingEnabled:]
- +[PLPhotoLibraryPathManager(conveniences) defaultDeferredRenderFileFormatTypeIdentifier]
- +[PLPhotoSharingHelper acceptPendingInvitationForAlbum:completionHandler:]
- +[PLPhotoSharingHelper declinePendingInvitationForAlbum:]
- +[PLPhotoSharingHelper deleteCloudSharedAssetsFromServer:inSharedAlbum:]
- +[PLPhotoSharingHelper hasPhoneInvitationForAlbum:]
- +[PLPhotoSharingHelper markPendingInvitationAsSpamForAlbum:completionHandler:]
- +[PLPhotoSharingHelper processExportedFileURL:assetUUID:customExportsInfo:]
- +[PLPhotoSharingHelper sendPendingInvitationsForAlbum:resendInvitationGUIDs:]
- +[PLPhotoSharingHelper sharingFirstName]
- +[PLPhotoSharingHelper sharingLastName]
- +[PLPhotoSharingHelper sharingUsername]
- +[PLPhotoSharingHelper updateCloudSharedAlbumMetadataOnServer:]
- +[PLPhotoSharingHelper updateCloudSharedAlbumMultipleContributorsStateOnServer:]
- +[PLPhotoSharingHelper updateCloudSharedAlbumPublicURLStateOnServer:]
- +[PLResourceInstaller onDemand_installOriginalSOCImagePresentForAsset:referencedResourceURLs:]
- +[PLResourceInstaller onDemand_installOriginalSOCVideoComplementPresentForAsset:referencedResourceURLs:]
- +[PLResourceInstaller onDemand_installOriginalSOCVideoPresentForAsset:referencedResourceURLs:]
- +[PLRevGeoLocationInfo isInvalidWithPlistData:]
- +[PLSMetadataUtilities allAlbumsDetailsWriteToPath:inLibrary:]
- +[PLSearchTrackedChangeTypes entityNamesIndexedBySearch]
- +[PLSpotlightQueryUtilities searchQueryForLibrary:queryString:]
- +[PLSyndicationResourceDataStore _provideFileURLAndUnwrapLivePhotoIfNeededForBundleID:syndicationIdentifier:typeIdentifier:isLivePhoto:options:completionHandler:]
- +[PLSyndicationResourceDataStore _safeCopyItemAtURL:toURLAndReplaceIfNeeded:error:]
- +[PLSyndicationResourceDataStore _unpackPVTBundleAtURL:primaryURL:secondaryURL:error:]
- +[PLSyndicationResourceDataStore provideFileURLAndUnwrapLivePhotoIfNeededForItemIdentifiersWithBundleIDs:destURLs:options:resultHandler:completionHandler:]
- +[PLThumbnailIndexes getAvailableVersionedThumbnailIndexesInLibrary:withCount:handler:]
- +[PLUserActivityDaemonJob userDidChangeStatusForMomentShare:]
- +[PLUserActivityDaemonJob userDidNavigateAwayFromAllSharedAlbums]
- +[PLUserActivityDaemonJob userDidNavigateAwayFromSharedAlbum:]
- +[PLUserActivityDaemonJob userDidNavigateIntoImagePickerSharedAlbum:]
- +[PLUserActivityDaemonJob userDidNavigateIntoSharedAlbum:]
- +[PLUserActivityDaemonJob userDidReadCommentOnSharedAsset:]
- -[CNContactStore(PhotoLibraryAdditions) contactsMatchingPhoneNumber:keysToFetch:]
- -[NSArray(PhotoLibraryServices) _pl_groupBy:]
- -[PFAdjustment .cxx_destruct]
- -[PFAdjustment autoIdentifier]
- -[PFAdjustment autoSettings]
- -[PFAdjustment debugDescription]
- -[PFAdjustment description]
- -[PFAdjustment enabled]
- -[PFAdjustment formatVersion]
- -[PFAdjustment identifier]
- -[PFAdjustment initWithIdentifier:settings:autoIdentifier:autoSettings:enabled:]
- -[PFAdjustment initWithIdentifier:settings:autoIdentifier:autoSettings:enabled:maskUUID:]
- -[PFAdjustment initWithIdentifier:settings:enabled:]
- -[PFAdjustment init]
- -[PFAdjustment maskUUID]
- -[PFAdjustment settings]
- -[PFAdjustment(Serialization) archiveDictionary]
- -[PFAdjustment(Serialization) initWithArchiveDictionary:]
- -[PFAdjustmentStack .cxx_destruct]
- -[PFAdjustmentStack adjustmentAtIndex:]
- -[PFAdjustmentStack adjustmentsWithIdentifier:]
- -[PFAdjustmentStack copyWithZone:]
- -[PFAdjustmentStack countByEnumeratingWithState:objects:count:]
- -[PFAdjustmentStack count]
- -[PFAdjustmentStack debugDescription]
- -[PFAdjustmentStack description]
- -[PFAdjustmentStack firstAdjustmentWithIdentifier:]
- -[PFAdjustmentStack initWithAdjustments:]
- -[PFAdjustmentStack init]
- -[PFAdjustmentStack maskUUIDs]
- -[PFAdjustmentStack(Serialization) envelopeDictionary]
- -[PFAdjustmentStack(Serialization) initWithEnvelopeDictionary:]
- -[PLAbstractLibraryServicesManagerService _isAuthorizedAssetUUID:inManagedObjectContext:]
- -[PLAggregateAlbumList .cxx_destruct]
- -[PLAggregateAlbumList _invalidateAllAlbums]
- -[PLAggregateAlbumList _typeDescription]
- -[PLAggregateAlbumList albumHasFixedOrder:]
- -[PLAggregateAlbumList albumListType]
- -[PLAggregateAlbumList albumsCount]
- -[PLAggregateAlbumList albumsSortingComparator]
- -[PLAggregateAlbumList albums]
- -[PLAggregateAlbumList assetContainerListDidChange:]
- -[PLAggregateAlbumList canEditAlbums]
- -[PLAggregateAlbumList canEditContainers]
- -[PLAggregateAlbumList containersCount]
- -[PLAggregateAlbumList containersRelationshipName]
- -[PLAggregateAlbumList containers]
- -[PLAggregateAlbumList dealloc]
- -[PLAggregateAlbumList filter]
- -[PLAggregateAlbumList hasAtLeastOneAlbum]
- -[PLAggregateAlbumList identifier]
- -[PLAggregateAlbumList initWithFilter:inPhotoLibrary:]
- -[PLAggregateAlbumList isEmpty]
- -[PLAggregateAlbumList isFolder]
- -[PLAggregateAlbumList managedObjectContext]
- -[PLAggregateAlbumList needsReordering]
- -[PLAggregateAlbumList photoLibrary]
- -[PLAggregateAlbumList preheatAlbumsAtIndexes:forProperties:relationships:]
- -[PLAggregateAlbumList preheatAlbumsForProperties:relationships:]
- -[PLAggregateAlbumList setFilter:]
- -[PLAggregateAlbumList setNeedsReordering]
- -[PLAggregateAlbumList unreadAlbumsCount]
- -[PLAggregateAlbumList updateAlbumsOrderIfNeeded]
- -[PLAggregateAlbumListChangeNotification .cxx_destruct]
- -[PLAggregateAlbumListChangeNotification _getOldSet:newSet:]
- -[PLAggregateAlbumListChangeNotification albumList]
- -[PLAggregateAlbumListChangeNotification changedIndexesRelativeToSnapshot]
- -[PLAggregateAlbumListChangeNotification changedIndexes]
- -[PLAggregateAlbumListChangeNotification changedObjects]
- -[PLAggregateAlbumListChangeNotification dealloc]
- -[PLAggregateAlbumListChangeNotification deletedIndexes]
- -[PLAggregateAlbumListChangeNotification deletedObjects]
- -[PLAggregateAlbumListChangeNotification enumerateMovesWithBlock:]
- -[PLAggregateAlbumListChangeNotification initWithAggregateAlbumList:fromAlbumListChangeNotification:indexOffset:]
- -[PLAggregateAlbumListChangeNotification insertedIndexes]
- -[PLAggregateAlbumListChangeNotification insertedObjects]
- -[PLAggregateAlbumListChangeNotification object]
- -[PLAggregateAlbumListChangeNotification shouldReload]
- -[PLAggregateAlbumListChangeNotification snapshotIndexForContainedObject:]
- -[PLAssetsdPhotoKitService executeQueryForSyncManager:type:startDate:endDate:batchHandler:completionHandler:]
- -[PLBackgroundJobCascadeDonationWorker workItemsNeedingProcessingInLibrary:validCriterias:]
- -[PLBackgroundJobDeferredRenderDerivativesBaseWorker workItemsNeedingProcessingInLibrary:validCriterias:]
- -[PLBackgroundJobDuplicateDetectorWorker workItemsNeedingProcessingInLibrary:validCriterias:]
- -[PLBackgroundJobEditRenderingWorker workItemsNeedingProcessingInLibrary:validCriterias:]
- -[PLBackgroundJobFeatureAvailabilityWorker workItemsNeedingProcessingInLibrary:validCriterias:]
- -[PLBackgroundJobGuestAssetSyncWorker workItemsNeedingProcessingInLibrary:validCriterias:]
- -[PLBackgroundJobLowPriorityBatterySearchIndexingWorker _jobTypes]
- -[PLBackgroundJobLowPriorityBatterySearchIndexingWorker _supportsIndexRebuild]
- -[PLBackgroundJobLowPriorityBatterySearchIndexingWorker locrIdentifyingBlock]
- -[PLBackgroundJobLowPriorityBatterySearchIndexingWorker type]
- -[PLBackgroundJobLowPriorityChargerSearchIndexingWorker _jobTypes]
- -[PLBackgroundJobLowPriorityChargerSearchIndexingWorker _supportsIndexRebuild]
- -[PLBackgroundJobLowPriorityChargerSearchIndexingWorker locrIdentifyingBlock]
- -[PLBackgroundJobLowPriorityChargerSearchIndexingWorker type]
- -[PLBackgroundJobOptimizeTableThumbsWorker workItemsNeedingProcessingInLibrary:validCriterias:]
- -[PLBackgroundJobPersonSyncWorker workItemsNeedingProcessingInLibrary:validCriterias:]
- -[PLBackgroundJobResourceAvailabilityWorker workItemsNeedingProcessingInLibrary:validCriterias:]
- -[PLBackgroundJobResourceUploadExtensionRunnerWorker criteriaNeedingProcessingInLibrary:validCriterias:outSignalAgainDate:]
- -[PLBackgroundJobResourceUploadExtensionRunnerWorker workItemsNeedingProcessingInLibrary:validCriterias:]
- -[PLBackgroundJobSearchIndexingWorker workItemsNeedingProcessingInLibrary:validCriterias:]
- -[PLBackgroundJobService _inq_pendingJobsForBundle:workerTypes:validCriterias:]
- -[PLBackgroundJobService _inq_pendingJobsOnBuffer:validCriterias:]
- -[PLBackgroundJobService _inq_pendingJobsOnBundles:validCriterias:]
- -[PLBackgroundJobService _processingSetURL]
- -[PLBackgroundJobSharedAssetContainerUpdateWorker workItemsNeedingProcessingInLibrary:validCriterias:]
- -[PLBackgroundJobStableHashWorker workItemsNeedingProcessingInLibrary:validCriterias:]
- -[PLBackgroundJobStatusCenter recordWorkerHasPendingJobs:]
- -[PLBackgroundJobSyndicationAssetCleanupWorker workItemsNeedingProcessingInLibrary:validCriterias:]
- -[PLBackgroundJobSyndicationResourceSanitizationWorker workItemsNeedingProcessingInLibrary:validCriterias:]
- -[PLBackgroundJobSyndicationSyncWorker workItemsNeedingProcessingInLibrary:validCriterias:]
- -[PLBackgroundJobWorker criteriaNeedingProcessingInLibrary:validCriterias:outSignalAgainDate:]
- -[PLBackgroundJobWorker pendingCriteriaInLibrary:validCriterias:outSignalAgainDate:]
- -[PLBackgroundJobWorker pendingWorkItemsInLibrary:validCriterias:]
- -[PLBackgroundJobWorker workItemsNeedingProcessingInLibrary:validCriterias:]
- -[PLBackgroundJobWorkerPendingWorkItems initWithZeroWorkItemsForValidCriteria]
- -[PLBackgroundJobWorkerPendingWorkItems setZeroWorkItemsForValidCriteria:]
- -[PLBackgroundJobWorkerPendingWorkItems zeroWorkItemsForValidCriteria]
- -[PLBackgroundJobWorkerTypesBuffer containsBackgroundJobWorker:forBundle:]
- -[PLBackgroundJobWorkerTypesBuffer containsBackgroundJobWorkerTypes:forBundle:]
- -[PLChangeNotificationCenter _enqueueCloudCommentsNotifications]
- -[PLChangeNotificationCenter _enqueueCloudFeedEntriesChangeNotifications]
- -[PLChangeNotificationCenter _enqueueInvitationRecordsChangeNotification:]
- -[PLChangeNotificationCenter _evaluateUpdatedAssets]
- -[PLChangeNotificationCenter addAssetContainerListChangeObserver:containerList:]
- -[PLChangeNotificationCenter addCloudCommentsChangeObserver:asset:]
- -[PLChangeNotificationCenter addCloudFeedEntriesObserver:]
- -[PLChangeNotificationCenter addShouldReloadObserver:]
- -[PLChangeNotificationCenter postShouldReloadNotificationWithPhotoLibrary:]
- -[PLChangeNotificationCenter removeAssetContainerListChangeObserver:containerList:]
- -[PLChangeNotificationCenter removeCloudCommentsChangeObserver:asset:]
- -[PLChangeNotificationCenter removeCloudFeedEntriesObserver:]
- -[PLChangeNotificationCenter removeShouldReloadObserver:]
- -[PLCloudCommentsChangeNotification .cxx_destruct]
- -[PLCloudCommentsChangeNotification _contentRelationshipName]
- -[PLCloudCommentsChangeNotification asset]
- -[PLCloudCommentsChangeNotification description]
- -[PLCloudCommentsChangeNotification name]
- -[PLCloudCommentsChangeNotification userInfo]
- -[PLCloudFeedEntriesChangeNotification .cxx_destruct]
- -[PLCloudFeedEntriesChangeNotification _initWithFullReload]
- -[PLCloudFeedEntriesChangeNotification _initWithInsertedEntries:updatedEntries:deletedEntries:]
- -[PLCloudFeedEntriesChangeNotification deletedEntries]
- -[PLCloudFeedEntriesChangeNotification insertedEntries]
- -[PLCloudFeedEntriesChangeNotification name]
- -[PLCloudFeedEntriesChangeNotification object]
- -[PLCloudFeedEntriesChangeNotification setDeletedEntries:]
- -[PLCloudFeedEntriesChangeNotification setInsertedEntries:]
- -[PLCloudFeedEntriesChangeNotification setShouldReload:]
- -[PLCloudFeedEntriesChangeNotification setUpdatedEntries:]
- -[PLCloudFeedEntriesChangeNotification shouldReload]
- -[PLCloudFeedEntriesChangeNotification updatedEntries]
- -[PLCloudFeedEntriesChangeNotification userInfo]
- -[PLCloudPhotoLibraryManager _enforcePrefetchModeForVisualIntelligenceLibraryIfNeededWithCPLSettings:]
- -[PLCloudPhotoLibraryManager cplConfigurationWithCompletionHandler:]
- -[PLCloudSharedAlbum persistRecoveryMetadata]
- -[PLConcurrencyLimiterRecordingReader aggregatesSortedByTotalExecTimeForQueue:]
- -[PLDaemonJob(DaemonCommunication) newDictionaryReplyForObject:]
- -[PLDuplicateGroup addManagedObjectID:]
- -[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:completionHandler:]
- -[PLGenericAlbum assetsByObjectIDAtIndexes:]
- -[PLImageWriter _copyJobContentsToHoldingDirectoryWithUUID:incomingPath:job:]
- -[PLIndexMapper indexForBackingIndex:]
- -[PLIndicatorFileCoordinator isStreamsLibraryUpdatingExpired]
- -[PLIndicatorFileCoordinator setStreamsLibraryUpdatingExpired:]
- -[PLIntensiveResourceTask prepareForReplacement]
- -[PLInternalResource(CPL) isCPLJPEGThumbnail]
- -[PLInvitationRecordsChangeNotification .cxx_destruct]
- -[PLInvitationRecordsChangeNotification _calculateDiffs]
- -[PLInvitationRecordsChangeNotification album]
- -[PLInvitationRecordsChangeNotification invitationRecordsDidChange]
- -[PLInvitationRecordsChangeNotification name]
- -[PLInvitationRecordsChangeNotification userInfo]
- -[PLLibraryScopeRule backingPredicateInPhotoLibrary:]
- -[PLManagedAsset _generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:retryNumber:allowCancellationByService:clientBundleID:completion:]
- -[PLManagedAsset _hdrTypeDescription]
- -[PLManagedAsset avalanchePickDescription]
- -[PLManagedAsset collectionShareContributorUserIdentifier]
- -[PLManagedAsset decodedFaceRegions]
- -[PLManagedAsset evaluateWhiteBalanceValueWithOriginalExifProperties:]
- -[PLManagedAsset fileURLForAsyncAdjustedRenderPreviewImage]
- -[PLManagedAsset generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:allowCancellationByService:clientBundleID:completion:]
- -[PLManagedAsset hasJustBeenHidden]
- -[PLManagedAsset hasJustBeenShown]
- -[PLManagedAsset isIncludedInHighlights]
- -[PLManagedAsset legacyFaceWithIdentifier:]
- -[PLManagedAsset reverseGeoDescription]
- -[PLManagedAsset setFaceRegionsFromCGImageProperties:]
- -[PLManagedAsset(Analysis) sceneAnalysisWasPerformedOnLatestAdjustment]
- -[PLManagedAsset(CPL) targetSizeForInputSize:maxPixelSize:]
- -[PLManagedAsset(PLCloudSharedAsset) cloudCommentsStatusForOwnedAsset:]
- -[PLManagedAsset(PLCloudSharedAsset) cloudHasSameOwnerAsAsset:]
- -[PLManagedAsset(RM) allFileBackedResources]
- -[PLManagedAsset(RM) insertTableThumbImageRequestHints]
- -[PLManagedAsset(RM) persistedCombinedProvenanceResource]
- -[PLManagedAsset(RM) resourcesWithVersion:]
- -[PLManagedAsset(RM_CPL) anyInternalResourceIsLocal]
- -[PLManagedAsset(Share) setupPlaceholderAssetWithRequiredPropertiesFromSourceAsset:placeholderAssetUUID:bundleScope:share:importSessionID:bakeInAdjustmentsFromSourceAsset:flattenLivePhoto:copyTitleDescriptionAndKeywords:copyCameraProcessingAdjustmentResources:copyProvenanceData:isCurrentUser:library:]
- -[PLManagedAsset(SidecarAdoption) removeSidecar:]
- -[PLManagedAsset(Syndication) eligibleForGuestAssetPromotion]
- -[PLManagedAsset(Syndication) unsaveSyndicatedAsset]
- -[PLManagedAssetRecoveryManager identifyAssetsWithInconsistentCloudState]
- -[PLManagedFolder removeChildCollectionsObject:]
- -[PLManagedFolder removeObjectFromChildCollectionsAtIndex:]
- -[PLManagedFolder replaceObjectInChildCollectionsAtIndex:withObject:]
- -[PLManagedFolder(Debugging) descriptionOfChildCollectionOrderValues]
- -[PLManagedObject pl_int32ValueForKey:]
- -[PLManagedObject pl_int64ValueForKey:]
- -[PLManagedObjectPagingIterator countRemainingWithManagedObjectContext:logger:]
- -[PLModelMigrator archiveAssetUUIDForPathPlist:]
- -[PLModelMigrator archivedAssetUUIDForURL:]
- -[PLModelMigrator generatePathToAssetUUIDRecoveryMapping]
- -[PLModelMigrator rebuildTargetedMomentsInStore:targetedAssetOIDs:]
- -[PLModelMigrator validateCurrentModelVersion]
- -[PLNotificationManager noteDidChangePlaceholderKindForAsset:fromOldKind:forSharedAlbum:mstreamdInfo:]
- -[PLNotificationManager noteDidReceiveCMMInvitationWithMomentShare:]
- -[PLNotificationManager noteDidReceiveExpiringCMMInvitationsWithMomentShares:]
- -[PLNotificationManager noteDidReceiveInvitationForSharedAlbum:]
- -[PLNotificationManager noteInvitationRecordStatusChanged:fromOldState:mstreamdInfo:]
- -[PLNotificationManager noteMultipleContributorStatusChangedForAlbum:mstreamdInfo:]
- -[PLNotificationManager noteSharedAlbumUnseenStatusDidChange:]
- -[PLNotificationManager noteUserDidNavigateAwayFromSharedAlbum:photoLibrary:]
- -[PLNotificationUNCenter removeNotificationsForNotifications:]
- -[PLPersistentHistoryTransactionModifiers encodeAsTransactionAuthor]
- -[PLPhotoEditRenderer calculateLongExposureFusionParametersWithCompletionHandler:]
- -[PLPhotoLibrary isAlbumSynced:]
- -[PLPhotoLibrary lastImportedPhotosAlbum]
- -[PLPhotoLibrary recreateMemoriesAndPersonsFromMetadata]
- -[PLPhotoLibraryShouldReloadNotification .cxx_destruct]
- -[PLPhotoLibraryShouldReloadNotification initNotificationWithPhotoLibrary:]
- -[PLPhotoLibraryShouldReloadNotification name]
- -[PLPhotoLibraryShouldReloadNotification object]
- -[PLPhotoLibraryShouldReloadNotification userInfo]
- -[PLPhotoStreamAlbum addAssetOrderedByDataTaken:]
- -[PLRebuildJournalManager recreateAllObjectsInManagedObjectContext:options:]
- -[PLRebuildUserNotification initWithMessage:]
- -[PLSearchIndexingEngineLibraryServicesProvider createLogger]
- -[PLSearchIndexingRebuildEngine _startRebuildForLibrary:]
- -[PLSearchTrackedAttributes .cxx_destruct]
- -[PLSearchTrackedAttributes assetAttributesTrackedForSearch]
- -[PLSearchTrackedAttributes detectedFaceAttributesTrackedForSearch]
- -[PLSearchTrackedAttributes fetchingAlbumAttributesTrackedForSearch]
- -[PLSearchTrackedAttributes highlightAttributesTrackedForSearch]
- -[PLSearchTrackedAttributes managedAlbumAttributesTrackedForSearch]
- -[PLSearchTrackedAttributes mediaAnalysisAssetAttributesTrackedForSearch]
- -[PLSearchTrackedAttributes memoryAttributesTrackedForSearch]
- -[PLSearchTrackedAttributes personAttributesTrackedForSearch]
- -[PLSearchTrackedAttributes setAssetAttributesTrackedForSearch:]
- -[PLSearchTrackedAttributes setDetectedFaceAttributesTrackedForSearch:]
- -[PLSearchTrackedAttributes setFetchingAlbumAttributesTrackedForSearch:]
- -[PLSearchTrackedAttributes setHighlightAttributesTrackedForSearch:]
- -[PLSearchTrackedAttributes setManagedAlbumAttributesTrackedForSearch:]
- -[PLSearchTrackedAttributes setMediaAnalysisAssetAttributesTrackedForSearch:]
- -[PLSearchTrackedAttributes setMemoryAttributesTrackedForSearch:]
- -[PLSearchTrackedAttributes setPersonAttributesTrackedForSearch:]
- -[PLSearchTrackedChangeTypes .cxx_destruct]
- -[PLSearchTrackedChangeTypes _changesTrackedBySearchForEntity:]
- -[PLSearchTrackedChangeTypes searchTrackedAttributes]
- -[PLSearchTrackedChangeTypes setSearchTrackedAttributes:]
- -[PLSearchTrackedChangeTypes trackedEntityNameForChange:photoLibrary:]
- -[PLServerPhotoLibraryBundle invalidateClientsReason]
- -[PLSocialGroup runAssetContainmentWithCompletion:]
- -[PLSyndicationResourceDataStore _copyAndMarkAsLocallyAvailablePairedLivePhotoResourceForRequestedResource:requestedVideoComplement:sourceURL:error:]
- -[PLSyndicationResourceDataStore _copyItemAtURL:withPathManager:destFileIdentifier:inode:error:]
- -[PLSyndicationSyncServiceWrapper executeQueryForSyncManager:type:startDate:endDate:batchHandler:completionHandler:]
- -[PLThumbnailManager _tableDescriptions]
- -[PLThumbnailManager discardCachedThumbnailDownscalerContexts]
- -[PLThumbnailResourceDataStoreOptions .cxx_destruct]
- -[PLThumbnailResourceDataStoreOptions overridingThumbnailIndex]
- -[PLThumbnailResourceDataStoreOptions setOverridingThumbnailIndex:]
- -[PLXPCPhotoLibraryStorePolicyNever shouldUseXPCStoreForDatabasePath:auditToken:]
- GCC_except_table10017
- GCC_except_table10018
- GCC_except_table10020
- GCC_except_table10023
- GCC_except_table10025
- GCC_except_table10030
- GCC_except_table10031
- GCC_except_table10099
- GCC_except_table1010
- GCC_except_table10104
- GCC_except_table10108
- GCC_except_table1011
- GCC_except_table10125
- GCC_except_table10132
- GCC_except_table10144
- GCC_except_table10146
- GCC_except_table10160
- GCC_except_table10165
- GCC_except_table10171
- GCC_except_table10175
- GCC_except_table10178
- GCC_except_table10186
- GCC_except_table10188
- GCC_except_table10197
- GCC_except_table10208
- GCC_except_table10271
- GCC_except_table10291
- GCC_except_table10309
- GCC_except_table10321
- GCC_except_table10333
- GCC_except_table10345
- GCC_except_table10347
- GCC_except_table10370
- GCC_except_table10407
- GCC_except_table10412
- GCC_except_table10427
- GCC_except_table10437
- GCC_except_table10449
- GCC_except_table10458
- GCC_except_table10485
- GCC_except_table10487
- GCC_except_table10500
- GCC_except_table10511
- GCC_except_table10590
- GCC_except_table10596
- GCC_except_table10598
- GCC_except_table10602
- GCC_except_table10604
- GCC_except_table10610
- GCC_except_table10614
- GCC_except_table10616
- GCC_except_table10622
- GCC_except_table10651
- GCC_except_table10658
- GCC_except_table10678
- GCC_except_table1068
- GCC_except_table10709
- GCC_except_table10712
- GCC_except_table10765
- GCC_except_table108
- GCC_except_table10816
- GCC_except_table10828
- GCC_except_table10830
- GCC_except_table10850
- GCC_except_table10852
- GCC_except_table10863
- GCC_except_table10868
- GCC_except_table10871
- GCC_except_table10877
- GCC_except_table1089
- GCC_except_table10897
- GCC_except_table11011
- GCC_except_table11145
- GCC_except_table11147
- GCC_except_table11157
- GCC_except_table11159
- GCC_except_table11161
- GCC_except_table11163
- GCC_except_table11165
- GCC_except_table11167
- GCC_except_table11169
- GCC_except_table11171
- GCC_except_table11173
- GCC_except_table11175
- GCC_except_table11177
- GCC_except_table11180
- GCC_except_table11183
- GCC_except_table11187
- GCC_except_table11190
- GCC_except_table11193
- GCC_except_table11195
- GCC_except_table11197
- GCC_except_table11199
- GCC_except_table112
- GCC_except_table11201
- GCC_except_table11203
- GCC_except_table11204
- GCC_except_table11207
- GCC_except_table11210
- GCC_except_table11213
- GCC_except_table11216
- GCC_except_table11218
- GCC_except_table11221
- GCC_except_table11224
- GCC_except_table11227
- GCC_except_table11228
- GCC_except_table11232
- GCC_except_table11237
- GCC_except_table11238
- GCC_except_table11240
- GCC_except_table11242
- GCC_except_table11243
- GCC_except_table11244
- GCC_except_table11245
- GCC_except_table11246
- GCC_except_table11248
- GCC_except_table11249
- GCC_except_table11250
- GCC_except_table11252
- GCC_except_table11253
- GCC_except_table11254
- GCC_except_table11255
- GCC_except_table11256
- GCC_except_table11257
- GCC_except_table11260
- GCC_except_table11261
- GCC_except_table11264
- GCC_except_table11266
- GCC_except_table11268
- GCC_except_table11270
- GCC_except_table11273
- GCC_except_table11274
- GCC_except_table11276
- GCC_except_table11348
- GCC_except_table11352
- GCC_except_table11363
- GCC_except_table1140
- GCC_except_table11434
- GCC_except_table11522
- GCC_except_table11575
- GCC_except_table1163
- GCC_except_table11680
- GCC_except_table1169
- GCC_except_table1170
- GCC_except_table11703
- GCC_except_table11756
- GCC_except_table1176
- GCC_except_table11814
- GCC_except_table1183
- GCC_except_table1185
- GCC_except_table119
- GCC_except_table12032
- GCC_except_table1204
- GCC_except_table1205
- GCC_except_table1206
- GCC_except_table12073
- GCC_except_table1212
- GCC_except_table1213
- GCC_except_table1219
- GCC_except_table12298
- GCC_except_table12331
- GCC_except_table12355
- GCC_except_table12357
- GCC_except_table12358
- GCC_except_table12359
- GCC_except_table12363
- GCC_except_table12378
- GCC_except_table1241
- GCC_except_table12461
- GCC_except_table12473
- GCC_except_table12479
- GCC_except_table12484
- GCC_except_table12489
- GCC_except_table12494
- GCC_except_table12498
- GCC_except_table12502
- GCC_except_table12512
- GCC_except_table12522
- GCC_except_table12527
- GCC_except_table12532
- GCC_except_table12536
- GCC_except_table12541
- GCC_except_table12546
- GCC_except_table12562
- GCC_except_table12580
- GCC_except_table1259
- GCC_except_table12591
- GCC_except_table12609
- GCC_except_table12625
- GCC_except_table12682
- GCC_except_table12685
- GCC_except_table12696
- GCC_except_table12698
- GCC_except_table12700
- GCC_except_table12702
- GCC_except_table12704
- GCC_except_table12707
- GCC_except_table12709
- GCC_except_table12718
- GCC_except_table12727
- GCC_except_table12730
- GCC_except_table12734
- GCC_except_table12739
- GCC_except_table12745
- GCC_except_table12749
- GCC_except_table12763
- GCC_except_table12765
- GCC_except_table12767
- GCC_except_table12785
- GCC_except_table12787
- GCC_except_table12789
- GCC_except_table12791
- GCC_except_table12794
- GCC_except_table12796
- GCC_except_table12798
- GCC_except_table12800
- GCC_except_table12802
- GCC_except_table12805
- GCC_except_table12810
- GCC_except_table12812
- GCC_except_table12814
- GCC_except_table12816
- GCC_except_table12819
- GCC_except_table12821
- GCC_except_table12823
- GCC_except_table12825
- GCC_except_table12827
- GCC_except_table12828
- GCC_except_table12839
- GCC_except_table12845
- GCC_except_table12871
- GCC_except_table12875
- GCC_except_table12876
- GCC_except_table12884
- GCC_except_table12912
- GCC_except_table12941
- GCC_except_table1303
- GCC_except_table13031
- GCC_except_table13122
- GCC_except_table13139
- GCC_except_table13141
- GCC_except_table13160
- GCC_except_table13162
- GCC_except_table13166
- GCC_except_table1319
- GCC_except_table13195
- GCC_except_table13200
- GCC_except_table13211
- GCC_except_table1326
- GCC_except_table13296
- GCC_except_table13312
- GCC_except_table13317
- GCC_except_table13321
- GCC_except_table1333
- GCC_except_table13338
- GCC_except_table13340
- GCC_except_table13347
- GCC_except_table13349
- GCC_except_table1335
- GCC_except_table13351
- GCC_except_table13353
- GCC_except_table13357
- GCC_except_table13402
- GCC_except_table13411
- GCC_except_table13417
- GCC_except_table13419
- GCC_except_table13421
- GCC_except_table13464
- GCC_except_table1350
- GCC_except_table13577
- GCC_except_table13598
- GCC_except_table13605
- GCC_except_table13609
- GCC_except_table13656
- GCC_except_table13738
- GCC_except_table13744
- GCC_except_table13763
- GCC_except_table13775
- GCC_except_table13829
- GCC_except_table13850
- GCC_except_table13853
- GCC_except_table13857
- GCC_except_table13860
- GCC_except_table13862
- GCC_except_table13866
- GCC_except_table13869
- GCC_except_table13878
- GCC_except_table13927
- GCC_except_table13945
- GCC_except_table1395
- GCC_except_table13951
- GCC_except_table13973
- GCC_except_table14068
- GCC_except_table14123
- GCC_except_table14134
- GCC_except_table14138
- GCC_except_table14153
- GCC_except_table14161
- GCC_except_table14185
- GCC_except_table14195
- GCC_except_table14197
- GCC_except_table14199
- GCC_except_table14218
- GCC_except_table14309
- GCC_except_table14314
- GCC_except_table14337
- GCC_except_table1435
- GCC_except_table14350
- GCC_except_table14352
- GCC_except_table14354
- GCC_except_table1437
- GCC_except_table1446
- GCC_except_table14462
- GCC_except_table14463
- GCC_except_table14467
- GCC_except_table1448
- GCC_except_table14500
- GCC_except_table14521
- GCC_except_table14532
- GCC_except_table14533
- GCC_except_table14534
- GCC_except_table14535
- GCC_except_table14536
- GCC_except_table14537
- GCC_except_table14538
- GCC_except_table14539
- GCC_except_table14540
- GCC_except_table14541
- GCC_except_table14542
- GCC_except_table14543
- GCC_except_table14544
- GCC_except_table1456
- GCC_except_table14609
- GCC_except_table14615
- GCC_except_table14630
- GCC_except_table14638
- GCC_except_table14641
- GCC_except_table14646
- GCC_except_table14684
- GCC_except_table14692
- GCC_except_table14699
- GCC_except_table14703
- GCC_except_table14714
- GCC_except_table14750
- GCC_except_table14800
- GCC_except_table14803
- GCC_except_table14807
- GCC_except_table14824
- GCC_except_table14871
- GCC_except_table14894
- GCC_except_table14916
- GCC_except_table1495
- GCC_except_table15059
- GCC_except_table15140
- GCC_except_table1515
- GCC_except_table15202
- GCC_except_table15219
- GCC_except_table15229
- GCC_except_table15230
- GCC_except_table15249
- GCC_except_table1526
- GCC_except_table1531
- GCC_except_table15338
- GCC_except_table15345
- GCC_except_table15347
- GCC_except_table15348
- GCC_except_table15351
- GCC_except_table15353
- GCC_except_table15360
- GCC_except_table15538
- GCC_except_table15568
- GCC_except_table15624
- GCC_except_table15711
- GCC_except_table1572
- GCC_except_table1580
- GCC_except_table15815
- GCC_except_table15825
- GCC_except_table15835
- GCC_except_table15837
- GCC_except_table15863
- GCC_except_table15882
- GCC_except_table15893
- GCC_except_table15920
- GCC_except_table15960
- GCC_except_table15964
- GCC_except_table15965
- GCC_except_table16
- GCC_except_table160
- GCC_except_table16031
- GCC_except_table16035
- GCC_except_table16038
- GCC_except_table16041
- GCC_except_table16198
- GCC_except_table16228
- GCC_except_table16245
- GCC_except_table16250
- GCC_except_table16253
- GCC_except_table16255
- GCC_except_table16258
- GCC_except_table16263
- GCC_except_table16264
- GCC_except_table1627
- GCC_except_table16270
- GCC_except_table16272
- GCC_except_table16278
- GCC_except_table16282
- GCC_except_table16284
- GCC_except_table16285
- GCC_except_table16289
- GCC_except_table16291
- GCC_except_table16293
- GCC_except_table16295
- GCC_except_table16298
- GCC_except_table16301
- GCC_except_table16348
- GCC_except_table16363
- GCC_except_table16366
- GCC_except_table16383
- GCC_except_table16387
- GCC_except_table16392
- GCC_except_table1640
- GCC_except_table16400
- GCC_except_table16402
- GCC_except_table16409
- GCC_except_table16413
- GCC_except_table1649
- GCC_except_table16510
- GCC_except_table16514
- GCC_except_table16516
- GCC_except_table16518
- GCC_except_table16541
- GCC_except_table16542
- GCC_except_table16549
- GCC_except_table16558
- GCC_except_table16567
- GCC_except_table16572
- GCC_except_table16576
- GCC_except_table16589
- GCC_except_table16648
- GCC_except_table16650
- GCC_except_table16744
- GCC_except_table16805
- GCC_except_table16818
- GCC_except_table16839
- GCC_except_table16931
- GCC_except_table16951
- GCC_except_table16957
- GCC_except_table16962
- GCC_except_table16969
- GCC_except_table16997
- GCC_except_table17009
- GCC_except_table17050
- GCC_except_table17054
- GCC_except_table17117
- GCC_except_table17122
- GCC_except_table17130
- GCC_except_table17140
- GCC_except_table17152
- GCC_except_table17166
- GCC_except_table17172
- GCC_except_table17182
- GCC_except_table17195
- GCC_except_table17205
- GCC_except_table17215
- GCC_except_table17245
- GCC_except_table17249
- GCC_except_table17251
- GCC_except_table17253
- GCC_except_table173
- GCC_except_table17314
- GCC_except_table17317
- GCC_except_table17364
- GCC_except_table17375
- GCC_except_table17395
- GCC_except_table17402
- GCC_except_table17406
- GCC_except_table17468
- GCC_except_table17478
- GCC_except_table17490
- GCC_except_table17491
- GCC_except_table17494
- GCC_except_table17497
- GCC_except_table17500
- GCC_except_table17503
- GCC_except_table17504
- GCC_except_table17505
- GCC_except_table17506
- GCC_except_table17507
- GCC_except_table17509
- GCC_except_table17541
- GCC_except_table17547
- GCC_except_table17631
- GCC_except_table17668
- GCC_except_table17682
- GCC_except_table17734
- GCC_except_table17752
- GCC_except_table17792
- GCC_except_table17797
- GCC_except_table17836
- GCC_except_table17844
- GCC_except_table17847
- GCC_except_table17859
- GCC_except_table17884
- GCC_except_table17915
- GCC_except_table17916
- GCC_except_table17917
- GCC_except_table1794
- GCC_except_table17952
- GCC_except_table17962
- GCC_except_table1800
- GCC_except_table18003
- GCC_except_table18010
- GCC_except_table18014
- GCC_except_table18028
- GCC_except_table18044
- GCC_except_table18045
- GCC_except_table18070
- GCC_except_table18089
- GCC_except_table18125
- GCC_except_table18127
- GCC_except_table18132
- GCC_except_table18135
- GCC_except_table18137
- GCC_except_table18141
- GCC_except_table18204
- GCC_except_table18229
- GCC_except_table18231
- GCC_except_table18233
- GCC_except_table18235
- GCC_except_table18237
- GCC_except_table18239
- GCC_except_table18243
- GCC_except_table18292
- GCC_except_table18432
- GCC_except_table18491
- GCC_except_table18502
- GCC_except_table18523
- GCC_except_table18575
- GCC_except_table18589
- GCC_except_table18598
- GCC_except_table18612
- GCC_except_table18613
- GCC_except_table18618
- GCC_except_table18623
- GCC_except_table18653
- GCC_except_table18682
- GCC_except_table18685
- GCC_except_table18744
- GCC_except_table18762
- GCC_except_table18786
- GCC_except_table18794
- GCC_except_table18796
- GCC_except_table18798
- GCC_except_table18801
- GCC_except_table18802
- GCC_except_table18803
- GCC_except_table18804
- GCC_except_table18805
- GCC_except_table18806
- GCC_except_table18807
- GCC_except_table18809
- GCC_except_table18814
- GCC_except_table18818
- GCC_except_table18819
- GCC_except_table18822
- GCC_except_table18824
- GCC_except_table18826
- GCC_except_table18828
- GCC_except_table18829
- GCC_except_table18830
- GCC_except_table18832
- GCC_except_table18835
- GCC_except_table18838
- GCC_except_table18889
- GCC_except_table18906
- GCC_except_table18935
- GCC_except_table19074
- GCC_except_table19076
- GCC_except_table19114
- GCC_except_table19119
- GCC_except_table19122
- GCC_except_table19143
- GCC_except_table19145
- GCC_except_table19146
- GCC_except_table19147
- GCC_except_table19151
- GCC_except_table19152
- GCC_except_table19153
- GCC_except_table19154
- GCC_except_table19155
- GCC_except_table19160
- GCC_except_table19163
- GCC_except_table19165
- GCC_except_table19167
- GCC_except_table19169
- GCC_except_table19172
- GCC_except_table19175
- GCC_except_table19178
- GCC_except_table19181
- GCC_except_table19183
- GCC_except_table19189
- GCC_except_table19192
- GCC_except_table19195
- GCC_except_table19198
- GCC_except_table19206
- GCC_except_table19210
- GCC_except_table19222
- GCC_except_table19227
- GCC_except_table19234
- GCC_except_table19236
- GCC_except_table19242
- GCC_except_table19252
- GCC_except_table19256
- GCC_except_table19260
- GCC_except_table19262
- GCC_except_table19264
- GCC_except_table19268
- GCC_except_table19270
- GCC_except_table19272
- GCC_except_table19274
- GCC_except_table19278
- GCC_except_table19279
- GCC_except_table19280
- GCC_except_table19282
- GCC_except_table19283
- GCC_except_table19288
- GCC_except_table19290
- GCC_except_table19291
- GCC_except_table19292
- GCC_except_table19295
- GCC_except_table19297
- GCC_except_table19299
- GCC_except_table19300
- GCC_except_table19301
- GCC_except_table19304
- GCC_except_table19307
- GCC_except_table19310
- GCC_except_table19313
- GCC_except_table19316
- GCC_except_table19318
- GCC_except_table19320
- GCC_except_table19322
- GCC_except_table19323
- GCC_except_table19325
- GCC_except_table19326
- GCC_except_table19337
- GCC_except_table19341
- GCC_except_table19345
- GCC_except_table194
- GCC_except_table19444
- GCC_except_table19450
- GCC_except_table19463
- GCC_except_table19465
- GCC_except_table19468
- GCC_except_table19469
- GCC_except_table19470
- GCC_except_table19471
- GCC_except_table19472
- GCC_except_table19473
- GCC_except_table19474
- GCC_except_table19481
- GCC_except_table19494
- GCC_except_table19606
- GCC_except_table19618
- GCC_except_table19637
- GCC_except_table19712
- GCC_except_table19715
- GCC_except_table19717
- GCC_except_table19722
- GCC_except_table19725
- GCC_except_table1973
- GCC_except_table19733
- GCC_except_table19754
- GCC_except_table19760
- GCC_except_table19764
- GCC_except_table19766
- GCC_except_table19770
- GCC_except_table1978
- GCC_except_table19785
- GCC_except_table19787
- GCC_except_table19796
- GCC_except_table19800
- GCC_except_table19803
- GCC_except_table19868
- GCC_except_table19934
- GCC_except_table19952
- GCC_except_table20024
- GCC_except_table20026
- GCC_except_table20037
- GCC_except_table20046
- GCC_except_table20048
- GCC_except_table20052
- GCC_except_table20054
- GCC_except_table20056
- GCC_except_table20070
- GCC_except_table20212
- GCC_except_table20223
- GCC_except_table20260
- GCC_except_table20266
- GCC_except_table20270
- GCC_except_table20275
- GCC_except_table20301
- GCC_except_table20335
- GCC_except_table20344
- GCC_except_table20350
- GCC_except_table20353
- GCC_except_table20358
- GCC_except_table20362
- GCC_except_table20367
- GCC_except_table20373
- GCC_except_table20379
- GCC_except_table20390
- GCC_except_table20396
- GCC_except_table20409
- GCC_except_table20558
- GCC_except_table20562
- GCC_except_table20597
- GCC_except_table20601
- GCC_except_table20605
- GCC_except_table20607
- GCC_except_table20635
- GCC_except_table20675
- GCC_except_table20679
- GCC_except_table20683
- GCC_except_table20687
- GCC_except_table20691
- GCC_except_table20695
- GCC_except_table20699
- GCC_except_table20703
- GCC_except_table20707
- GCC_except_table20711
- GCC_except_table20715
- GCC_except_table20723
- GCC_except_table20727
- GCC_except_table20731
- GCC_except_table20735
- GCC_except_table20739
- GCC_except_table20743
- GCC_except_table20747
- GCC_except_table20755
- GCC_except_table20792
- GCC_except_table20795
- GCC_except_table20800
- GCC_except_table20803
- GCC_except_table20829
- GCC_except_table20834
- GCC_except_table20835
- GCC_except_table20841
- GCC_except_table20842
- GCC_except_table20854
- GCC_except_table20920
- GCC_except_table20964
- GCC_except_table20971
- GCC_except_table20977
- GCC_except_table21
- GCC_except_table21003
- GCC_except_table21017
- GCC_except_table21029
- GCC_except_table21033
- GCC_except_table21037
- GCC_except_table21041
- GCC_except_table21057
- GCC_except_table21085
- GCC_except_table21110
- GCC_except_table21114
- GCC_except_table21160
- GCC_except_table21177
- GCC_except_table21195
- GCC_except_table21199
- GCC_except_table21204
- GCC_except_table21205
- GCC_except_table21209
- GCC_except_table21210
- GCC_except_table21212
- GCC_except_table21214
- GCC_except_table21219
- GCC_except_table21220
- GCC_except_table21222
- GCC_except_table21230
- GCC_except_table21233
- GCC_except_table21234
- GCC_except_table21235
- GCC_except_table21236
- GCC_except_table21238
- GCC_except_table21240
- GCC_except_table21243
- GCC_except_table21244
- GCC_except_table21246
- GCC_except_table21247
- GCC_except_table21249
- GCC_except_table21250
- GCC_except_table21254
- GCC_except_table21256
- GCC_except_table21258
- GCC_except_table21260
- GCC_except_table21262
- GCC_except_table21264
- GCC_except_table21266
- GCC_except_table21268
- GCC_except_table21270
- GCC_except_table21272
- GCC_except_table21275
- GCC_except_table21279
- GCC_except_table21290
- GCC_except_table21421
- GCC_except_table21428
- GCC_except_table21441
- GCC_except_table21447
- GCC_except_table21567
- GCC_except_table216
- GCC_except_table21640
- GCC_except_table21656
- GCC_except_table21666
- GCC_except_table21726
- GCC_except_table21842
- GCC_except_table21843
- GCC_except_table21855
- GCC_except_table21882
- GCC_except_table21907
- GCC_except_table21925
- GCC_except_table21973
- GCC_except_table21996
- GCC_except_table22007
- GCC_except_table22013
- GCC_except_table22017
- GCC_except_table22022
- GCC_except_table22084
- GCC_except_table22100
- GCC_except_table22117
- GCC_except_table22122
- GCC_except_table22136
- GCC_except_table22175
- GCC_except_table22235
- GCC_except_table22247
- GCC_except_table22249
- GCC_except_table2225
- GCC_except_table22280
- GCC_except_table22292
- GCC_except_table22297
- GCC_except_table2230
- GCC_except_table22304
- GCC_except_table22334
- GCC_except_table22347
- GCC_except_table22350
- GCC_except_table22376
- GCC_except_table2238
- GCC_except_table22407
- GCC_except_table2241
- GCC_except_table22496
- GCC_except_table22542
- GCC_except_table22546
- GCC_except_table22548
- GCC_except_table22550
- GCC_except_table22577
- GCC_except_table22649
- GCC_except_table22650
- GCC_except_table2267
- GCC_except_table22690
- GCC_except_table2272
- GCC_except_table22723
- GCC_except_table22727
- GCC_except_table22768
- GCC_except_table22835
- GCC_except_table2286
- GCC_except_table2288
- GCC_except_table2313
- GCC_except_table2319
- GCC_except_table23248
- GCC_except_table2335
- GCC_except_table2347
- GCC_except_table23547
- GCC_except_table23559
- GCC_except_table23568
- GCC_except_table23615
- GCC_except_table23619
- GCC_except_table23675
- GCC_except_table23687
- GCC_except_table23703
- GCC_except_table23804
- GCC_except_table23813
- GCC_except_table23843
- GCC_except_table23905
- GCC_except_table23919
- GCC_except_table23920
- GCC_except_table23987
- GCC_except_table24005
- GCC_except_table24012
- GCC_except_table24036
- GCC_except_table24215
- GCC_except_table24240
- GCC_except_table24244
- GCC_except_table24289
- GCC_except_table2430
- GCC_except_table24323
- GCC_except_table24361
- GCC_except_table24364
- GCC_except_table24368
- GCC_except_table24411
- GCC_except_table24412
- GCC_except_table24478
- GCC_except_table24481
- GCC_except_table24498
- GCC_except_table24503
- GCC_except_table24511
- GCC_except_table24520
- GCC_except_table24526
- GCC_except_table24533
- GCC_except_table24556
- GCC_except_table24583
- GCC_except_table24772
- GCC_except_table24776
- GCC_except_table24783
- GCC_except_table24784
- GCC_except_table24785
- GCC_except_table24786
- GCC_except_table24789
- GCC_except_table24790
- GCC_except_table24792
- GCC_except_table24793
- GCC_except_table24796
- GCC_except_table24803
- GCC_except_table24806
- GCC_except_table24807
- GCC_except_table24808
- GCC_except_table24811
- GCC_except_table24812
- GCC_except_table24813
- GCC_except_table2483
- GCC_except_table24843
- GCC_except_table24869
- GCC_except_table24872
- GCC_except_table24873
- GCC_except_table24878
- GCC_except_table24883
- GCC_except_table24887
- GCC_except_table24950
- GCC_except_table24957
- GCC_except_table24959
- GCC_except_table24961
- GCC_except_table24963
- GCC_except_table24965
- GCC_except_table24973
- GCC_except_table24975
- GCC_except_table24989
- GCC_except_table25015
- GCC_except_table25018
- GCC_except_table25025
- GCC_except_table25027
- GCC_except_table25029
- GCC_except_table2503
- GCC_except_table25031
- GCC_except_table25035
- GCC_except_table25039
- GCC_except_table25055
- GCC_except_table25058
- GCC_except_table25062
- GCC_except_table25066
- GCC_except_table25076
- GCC_except_table25081
- GCC_except_table25085
- GCC_except_table25087
- GCC_except_table25089
- GCC_except_table25091
- GCC_except_table25099
- GCC_except_table25103
- GCC_except_table25107
- GCC_except_table25111
- GCC_except_table25113
- GCC_except_table25125
- GCC_except_table2513
- GCC_except_table25149
- GCC_except_table25165
- GCC_except_table25183
- GCC_except_table25187
- GCC_except_table2519
- GCC_except_table25212
- GCC_except_table25214
- GCC_except_table25216
- GCC_except_table25239
- GCC_except_table25242
- GCC_except_table25247
- GCC_except_table25302
- GCC_except_table25364
- GCC_except_table25368
- GCC_except_table25371
- GCC_except_table25374
- GCC_except_table25381
- GCC_except_table25407
- GCC_except_table25410
- GCC_except_table25422
- GCC_except_table25425
- GCC_except_table25441
- GCC_except_table25446
- GCC_except_table25450
- GCC_except_table25453
- GCC_except_table25475
- GCC_except_table25484
- GCC_except_table25487
- GCC_except_table25490
- GCC_except_table25497
- GCC_except_table25505
- GCC_except_table25506
- GCC_except_table25507
- GCC_except_table25514
- GCC_except_table25607
- GCC_except_table25608
- GCC_except_table25609
- GCC_except_table25610
- GCC_except_table25614
- GCC_except_table25618
- GCC_except_table25619
- GCC_except_table25620
- GCC_except_table25623
- GCC_except_table25653
- GCC_except_table25661
- GCC_except_table25665
- GCC_except_table25742
- GCC_except_table25746
- GCC_except_table25754
- GCC_except_table25770
- GCC_except_table25790
- GCC_except_table25794
- GCC_except_table2582
- GCC_except_table2588
- GCC_except_table2589
- GCC_except_table25900
- GCC_except_table25918
- GCC_except_table25927
- GCC_except_table25930
- GCC_except_table25933
- GCC_except_table25936
- GCC_except_table25942
- GCC_except_table25945
- GCC_except_table25948
- GCC_except_table25951
- GCC_except_table25954
- GCC_except_table25957
- GCC_except_table25960
- GCC_except_table25963
- GCC_except_table25966
- GCC_except_table25969
- GCC_except_table25972
- GCC_except_table25975
- GCC_except_table25978
- GCC_except_table25984
- GCC_except_table25990
- GCC_except_table25996
- GCC_except_table25999
- GCC_except_table26002
- GCC_except_table26005
- GCC_except_table26008
- GCC_except_table26011
- GCC_except_table26014
- GCC_except_table26017
- GCC_except_table26020
- GCC_except_table26023
- GCC_except_table26026
- GCC_except_table26029
- GCC_except_table26032
- GCC_except_table26038
- GCC_except_table26041
- GCC_except_table26044
- GCC_except_table26047
- GCC_except_table26053
- GCC_except_table26056
- GCC_except_table26059
- GCC_except_table26062
- GCC_except_table26065
- GCC_except_table26068
- GCC_except_table26074
- GCC_except_table26077
- GCC_except_table26083
- GCC_except_table26086
- GCC_except_table26089
- GCC_except_table26092
- GCC_except_table26095
- GCC_except_table26098
- GCC_except_table26101
- GCC_except_table26104
- GCC_except_table26107
- GCC_except_table26110
- GCC_except_table26113
- GCC_except_table26116
- GCC_except_table26125
- GCC_except_table26128
- GCC_except_table26131
- GCC_except_table26134
- GCC_except_table26137
- GCC_except_table26140
- GCC_except_table26201
- GCC_except_table26204
- GCC_except_table26242
- GCC_except_table26248
- GCC_except_table26296
- GCC_except_table26328
- GCC_except_table26333
- GCC_except_table26335
- GCC_except_table26337
- GCC_except_table26383
- GCC_except_table26432
- GCC_except_table26440
- GCC_except_table26445
- GCC_except_table26456
- GCC_except_table26484
- GCC_except_table26486
- GCC_except_table26487
- GCC_except_table26620
- GCC_except_table26626
- GCC_except_table26648
- GCC_except_table26687
- GCC_except_table26690
- GCC_except_table26696
- GCC_except_table26701
- GCC_except_table26705
- GCC_except_table26713
- GCC_except_table26740
- GCC_except_table26746
- GCC_except_table26748
- GCC_except_table26789
- GCC_except_table26933
- GCC_except_table26937
- GCC_except_table26940
- GCC_except_table26942
- GCC_except_table27054
- GCC_except_table27246
- GCC_except_table27249
- GCC_except_table27256
- GCC_except_table27260
- GCC_except_table27271
- GCC_except_table27279
- GCC_except_table27281
- GCC_except_table27286
- GCC_except_table27288
- GCC_except_table27302
- GCC_except_table27307
- GCC_except_table27311
- GCC_except_table27331
- GCC_except_table2739
- GCC_except_table2741
- GCC_except_table2750
- GCC_except_table2777
- GCC_except_table2780
- GCC_except_table279
- GCC_except_table28
- GCC_except_table280
- GCC_except_table2818
- GCC_except_table2830
- GCC_except_table2833
- GCC_except_table2840
- GCC_except_table2847
- GCC_except_table285
- GCC_except_table2891
- GCC_except_table2892
- GCC_except_table2898
- GCC_except_table2950
- GCC_except_table2990
- GCC_except_table3100
- GCC_except_table3108
- GCC_except_table3130
- GCC_except_table332
- GCC_except_table3327
- GCC_except_table3333
- GCC_except_table3385
- GCC_except_table3439
- GCC_except_table3464
- GCC_except_table3474
- GCC_except_table3489
- GCC_except_table3533
- GCC_except_table3538
- GCC_except_table3540
- GCC_except_table3543
- GCC_except_table3547
- GCC_except_table3550
- GCC_except_table3551
- GCC_except_table3555
- GCC_except_table3557
- GCC_except_table3561
- GCC_except_table3565
- GCC_except_table3605
- GCC_except_table3612
- GCC_except_table3863
- GCC_except_table3867
- GCC_except_table3870
- GCC_except_table3873
- GCC_except_table3876
- GCC_except_table3879
- GCC_except_table3889
- GCC_except_table3949
- GCC_except_table3990
- GCC_except_table3997
- GCC_except_table3998
- GCC_except_table4004
- GCC_except_table4023
- GCC_except_table4032
- GCC_except_table4060
- GCC_except_table4120
- GCC_except_table4125
- GCC_except_table4136
- GCC_except_table4141
- GCC_except_table4144
- GCC_except_table416
- GCC_except_table4169
- GCC_except_table4171
- GCC_except_table4180
- GCC_except_table4183
- GCC_except_table419
- GCC_except_table4201
- GCC_except_table4204
- GCC_except_table422
- GCC_except_table4232
- GCC_except_table4235
- GCC_except_table4239
- GCC_except_table425
- GCC_except_table4258
- GCC_except_table4263
- GCC_except_table4267
- GCC_except_table4271
- GCC_except_table4275
- GCC_except_table428
- GCC_except_table4282
- GCC_except_table4298
- GCC_except_table434
- GCC_except_table44
- GCC_except_table4449
- GCC_except_table4456
- GCC_except_table4463
- GCC_except_table4465
- GCC_except_table4471
- GCC_except_table4473
- GCC_except_table4489
- GCC_except_table4491
- GCC_except_table4496
- GCC_except_table4498
- GCC_except_table4506
- GCC_except_table4516
- GCC_except_table4539
- GCC_except_table4557
- GCC_except_table4558
- GCC_except_table4583
- GCC_except_table4633
- GCC_except_table4637
- GCC_except_table466
- GCC_except_table4842
- GCC_except_table4849
- GCC_except_table4908
- GCC_except_table4930
- GCC_except_table4934
- GCC_except_table4957
- GCC_except_table5054
- GCC_except_table5059
- GCC_except_table5067
- GCC_except_table5093
- GCC_except_table51
- GCC_except_table5167
- GCC_except_table524
- GCC_except_table5274
- GCC_except_table5313
- GCC_except_table5321
- GCC_except_table5323
- GCC_except_table5326
- GCC_except_table538
- GCC_except_table55
- GCC_except_table5546
- GCC_except_table5561
- GCC_except_table5587
- GCC_except_table5664
- GCC_except_table5665
- GCC_except_table5678
- GCC_except_table5681
- GCC_except_table569
- GCC_except_table574
- GCC_except_table5741
- GCC_except_table5760
- GCC_except_table5767
- GCC_except_table5771
- GCC_except_table5781
- GCC_except_table5784
- GCC_except_table5844
- GCC_except_table5849
- GCC_except_table5897
- GCC_except_table5900
- GCC_except_table5911
- GCC_except_table5918
- GCC_except_table592
- GCC_except_table5926
- GCC_except_table5928
- GCC_except_table5963
- GCC_except_table5964
- GCC_except_table5967
- GCC_except_table5968
- GCC_except_table5976
- GCC_except_table5989
- GCC_except_table6080
- GCC_except_table6082
- GCC_except_table6105
- GCC_except_table6143
- GCC_except_table6172
- GCC_except_table6177
- GCC_except_table6182
- GCC_except_table6184
- GCC_except_table6186
- GCC_except_table6204
- GCC_except_table6207
- GCC_except_table6209
- GCC_except_table6213
- GCC_except_table6215
- GCC_except_table6273
- GCC_except_table6296
- GCC_except_table6301
- GCC_except_table6324
- GCC_except_table6365
- GCC_except_table6377
- GCC_except_table6378
- GCC_except_table6380
- GCC_except_table6382
- GCC_except_table6387
- GCC_except_table6393
- GCC_except_table6398
- GCC_except_table6400
- GCC_except_table6402
- GCC_except_table6404
- GCC_except_table6405
- GCC_except_table6406
- GCC_except_table6407
- GCC_except_table6408
- GCC_except_table6409
- GCC_except_table6410
- GCC_except_table6414
- GCC_except_table6416
- GCC_except_table6418
- GCC_except_table6421
- GCC_except_table6424
- GCC_except_table6427
- GCC_except_table6428
- GCC_except_table6429
- GCC_except_table6430
- GCC_except_table6431
- GCC_except_table6432
- GCC_except_table6433
- GCC_except_table6434
- GCC_except_table6435
- GCC_except_table6436
- GCC_except_table6439
- GCC_except_table6441
- GCC_except_table6443
- GCC_except_table6444
- GCC_except_table6446
- GCC_except_table6448
- GCC_except_table6449
- GCC_except_table6450
- GCC_except_table6452
- GCC_except_table6454
- GCC_except_table6455
- GCC_except_table6456
- GCC_except_table6457
- GCC_except_table6486
- GCC_except_table6524
- GCC_except_table6537
- GCC_except_table6564
- GCC_except_table6630
- GCC_except_table674
- GCC_except_table6746
- GCC_except_table679
- GCC_except_table6815
- GCC_except_table692
- GCC_except_table694
- GCC_except_table698
- GCC_except_table7028
- GCC_except_table707
- GCC_except_table7087
- GCC_except_table713
- GCC_except_table7133
- GCC_except_table7140
- GCC_except_table7157
- GCC_except_table7164
- GCC_except_table7173
- GCC_except_table7177
- GCC_except_table7180
- GCC_except_table7183
- GCC_except_table7194
- GCC_except_table7202
- GCC_except_table7208
- GCC_except_table7211
- GCC_except_table7247
- GCC_except_table7259
- GCC_except_table727
- GCC_except_table7273
- GCC_except_table7285
- GCC_except_table7303
- GCC_except_table7306
- GCC_except_table731
- GCC_except_table7311
- GCC_except_table7319
- GCC_except_table7321
- GCC_except_table7325
- GCC_except_table7330
- GCC_except_table7332
- GCC_except_table7335
- GCC_except_table7340
- GCC_except_table736
- GCC_except_table7410
- GCC_except_table7413
- GCC_except_table7418
- GCC_except_table7420
- GCC_except_table7425
- GCC_except_table7426
- GCC_except_table7428
- GCC_except_table7433
- GCC_except_table7436
- GCC_except_table7439
- GCC_except_table7441
- GCC_except_table7443
- GCC_except_table7445
- GCC_except_table7447
- GCC_except_table7450
- GCC_except_table7455
- GCC_except_table7463
- GCC_except_table7467
- GCC_except_table7472
- GCC_except_table7474
- GCC_except_table7476
- GCC_except_table7478
- GCC_except_table7482
- GCC_except_table7491
- GCC_except_table7495
- GCC_except_table7499
- GCC_except_table7501
- GCC_except_table7503
- GCC_except_table7505
- GCC_except_table7507
- GCC_except_table7522
- GCC_except_table7524
- GCC_except_table7530
- GCC_except_table7532
- GCC_except_table7536
- GCC_except_table7564
- GCC_except_table7568
- GCC_except_table7594
- GCC_except_table7596
- GCC_except_table7612
- GCC_except_table762
- GCC_except_table7848
- GCC_except_table7853
- GCC_except_table7866
- GCC_except_table7867
- GCC_except_table7880
- GCC_except_table7903
- GCC_except_table7904
- GCC_except_table7915
- GCC_except_table7944
- GCC_except_table7964
- GCC_except_table7974
- GCC_except_table7978
- GCC_except_table7979
- GCC_except_table7986
- GCC_except_table7989
- GCC_except_table799
- GCC_except_table8050
- GCC_except_table8052
- GCC_except_table8063
- GCC_except_table8070
- GCC_except_table8125
- GCC_except_table8134
- GCC_except_table814
- GCC_except_table8146
- GCC_except_table8148
- GCC_except_table8197
- GCC_except_table8203
- GCC_except_table8215
- GCC_except_table8223
- GCC_except_table8232
- GCC_except_table8251
- GCC_except_table8252
- GCC_except_table8256
- GCC_except_table8257
- GCC_except_table8261
- GCC_except_table8265
- GCC_except_table8268
- GCC_except_table8271
- GCC_except_table8286
- GCC_except_table8291
- GCC_except_table8293
- GCC_except_table8298
- GCC_except_table8308
- GCC_except_table831
- GCC_except_table8314
- GCC_except_table8318
- GCC_except_table8321
- GCC_except_table8330
- GCC_except_table8363
- GCC_except_table837
- GCC_except_table8421
- GCC_except_table8422
- GCC_except_table8434
- GCC_except_table844
- GCC_except_table8440
- GCC_except_table8445
- GCC_except_table8446
- GCC_except_table8480
- GCC_except_table8485
- GCC_except_table849
- GCC_except_table8491
- GCC_except_table8503
- GCC_except_table8516
- GCC_except_table8529
- GCC_except_table854
- GCC_except_table8553
- GCC_except_table8583
- GCC_except_table8618
- GCC_except_table8621
- GCC_except_table865
- GCC_except_table8674
- GCC_except_table868
- GCC_except_table8682
- GCC_except_table8697
- GCC_except_table8699
- GCC_except_table873
- GCC_except_table8819
- GCC_except_table8864
- GCC_except_table8865
- GCC_except_table8889
- GCC_except_table891
- GCC_except_table8918
- GCC_except_table8919
- GCC_except_table9093
- GCC_except_table9105
- GCC_except_table9115
- GCC_except_table9118
- GCC_except_table9123
- GCC_except_table9149
- GCC_except_table9174
- GCC_except_table9178
- GCC_except_table9181
- GCC_except_table9188
- GCC_except_table9192
- GCC_except_table920
- GCC_except_table9234
- GCC_except_table9248
- GCC_except_table926
- GCC_except_table9370
- GCC_except_table9404
- GCC_except_table9408
- GCC_except_table9414
- GCC_except_table9416
- GCC_except_table9422
- GCC_except_table9425
- GCC_except_table9462
- GCC_except_table9509
- GCC_except_table9635
- GCC_except_table9649
- GCC_except_table9652
- GCC_except_table9677
- GCC_except_table9679
- GCC_except_table9681
- GCC_except_table9683
- GCC_except_table9684
- GCC_except_table9690
- GCC_except_table9692
- GCC_except_table9693
- GCC_except_table9702
- GCC_except_table9706
- GCC_except_table9709
- GCC_except_table974
- GCC_except_table9759
- GCC_except_table9760
- GCC_except_table9761
- GCC_except_table9778
- GCC_except_table9783
- GCC_except_table9796
- GCC_except_table9830
- GCC_except_table9841
- GCC_except_table9871
- GCC_except_table9985
- OBJC_IVAR_$_PFAdjustmentStack._adjustments
- OBJC_IVAR_$_PFAdjustmentStack._formatVersion
- OBJC_IVAR_$_PFAdjustmentStack._maskUUIDs
- _AVAppleMakerNote_SpatialOverCaptureGroupIdentifier
- _CGImageCreateByMatchingToColorSpace
- _MCFeaturePhotoStreamAllowed
- _NSStringFromPLCloudFeedEntryFilter
- _OBJC_CLASS_$_NSFetchIndexDescription
- _OBJC_CLASS_$_NSFetchIndexElementDescription
- _OBJC_CLASS_$_PFAdjustment
- _OBJC_CLASS_$_PFAdjustmentSerialization
- _OBJC_CLASS_$_PFAdjustmentStack
- _OBJC_CLASS_$_PLAggregateAlbumList
- _OBJC_CLASS_$_PLAggregateAlbumListChangeNotification
- _OBJC_CLASS_$_PLBackgroundJobLowPriorityBatterySearchIndexingWorker
- _OBJC_CLASS_$_PLBackgroundJobLowPriorityChargerSearchIndexingWorker
- _OBJC_CLASS_$_PLCloudCommentsChangeNotification
- _OBJC_CLASS_$_PLCloudFeedEntriesChangeNotification
- _OBJC_CLASS_$_PLInvitationRecordsChangeNotification
- _OBJC_CLASS_$_PLPhotoLibraryShouldReloadNotification
- _OBJC_CLASS_$_PLSearchTrackedAttributes
- _OBJC_CLASS_$_PLSearchTrackedChangeTypes
- _OBJC_CLASS_$_PLThumbnailResourceDataStoreOptions
- _OBJC_CLASS_$_PLXPCPhotoLibraryStorePolicyNever
- _OBJC_EHTYPE_id
- _OBJC_IVAR_$_PFAdjustment._autoIdentifier
- _OBJC_IVAR_$_PFAdjustment._autoSettings
- _OBJC_IVAR_$_PFAdjustment._enabled
- _OBJC_IVAR_$_PFAdjustment._formatVersion
- _OBJC_IVAR_$_PFAdjustment._identifier
- _OBJC_IVAR_$_PFAdjustment._maskUUID
- _OBJC_IVAR_$_PFAdjustment._settings
- _OBJC_IVAR_$_PLAggregateAlbumList._allAlbums
- _OBJC_IVAR_$_PLAggregateAlbumList._childAlbumLists
- _OBJC_IVAR_$_PLAggregateAlbumList._filter
- _OBJC_IVAR_$_PLAggregateAlbumListChangeNotification._albumList
- _OBJC_IVAR_$_PLAggregateAlbumListChangeNotification._indexOffet
- _OBJC_IVAR_$_PLAggregateAlbumListChangeNotification._note
- _OBJC_IVAR_$_PLBackgroundJobWorkerPendingWorkItems._zeroWorkItemsForValidCriteria
- _OBJC_IVAR_$_PLChangeNotificationCenter._assetsWithCloudCommentChanges
- _OBJC_IVAR_$_PLChangeNotificationCenter._changedCloudFeedEntries
- _OBJC_IVAR_$_PLCloudCommentsChangeNotification._userInfo
- _OBJC_IVAR_$_PLCloudFeedEntriesChangeNotification._deletedEntries
- _OBJC_IVAR_$_PLCloudFeedEntriesChangeNotification._insertedEntries
- _OBJC_IVAR_$_PLCloudFeedEntriesChangeNotification._shouldReload
- _OBJC_IVAR_$_PLCloudFeedEntriesChangeNotification._updatedEntries
- _OBJC_IVAR_$_PLInvitationRecordsChangeNotification._invitationRecordsDidChange
- _OBJC_IVAR_$_PLInvitationRecordsChangeNotification._userInfo
- _OBJC_IVAR_$_PLManagedAsset._height
- _OBJC_IVAR_$_PLManagedAsset._width
- _OBJC_IVAR_$_PLPhotoLibraryShouldReloadNotification._photoLibrary
- _OBJC_IVAR_$_PLSearchIndexingRebuildEngine._logger
- _OBJC_IVAR_$_PLSearchTrackedAttributes._assetAttributesTrackedForSearch
- _OBJC_IVAR_$_PLSearchTrackedAttributes._detectedFaceAttributesTrackedForSearch
- _OBJC_IVAR_$_PLSearchTrackedAttributes._fetchingAlbumAttributesTrackedForSearch
- _OBJC_IVAR_$_PLSearchTrackedAttributes._highlightAttributesTrackedForSearch
- _OBJC_IVAR_$_PLSearchTrackedAttributes._managedAlbumAttributesTrackedForSearch
- _OBJC_IVAR_$_PLSearchTrackedAttributes._mediaAnalysisAssetAttributesTrackedForSearch
- _OBJC_IVAR_$_PLSearchTrackedAttributes._memoryAttributesTrackedForSearch
- _OBJC_IVAR_$_PLSearchTrackedAttributes._personAttributesTrackedForSearch
- _OBJC_IVAR_$_PLSearchTrackedChangeTypes._searchTrackedAttributes
- _OBJC_IVAR_$_PLThumbnailResourceDataStoreOptions._overridingThumbnailIndex
- _OBJC_METACLASS_$_PFAdjustment
- _OBJC_METACLASS_$_PFAdjustmentSerialization
- _OBJC_METACLASS_$_PFAdjustmentStack
- _OBJC_METACLASS_$_PLAggregateAlbumList
- _OBJC_METACLASS_$_PLAggregateAlbumListChangeNotification
- _OBJC_METACLASS_$_PLBackgroundJobLowPriorityBatterySearchIndexingWorker
- _OBJC_METACLASS_$_PLBackgroundJobLowPriorityChargerSearchIndexingWorker
- _OBJC_METACLASS_$_PLCloudCommentsChangeNotification
- _OBJC_METACLASS_$_PLCloudFeedEntriesChangeNotification
- _OBJC_METACLASS_$_PLInvitationRecordsChangeNotification
- _OBJC_METACLASS_$_PLPhotoLibraryShouldReloadNotification
- _OBJC_METACLASS_$_PLSearchTrackedAttributes
- _OBJC_METACLASS_$_PLSearchTrackedChangeTypes
- _OBJC_METACLASS_$_PLThumbnailResourceDataStoreOptions
- _OBJC_METACLASS_$_PLXPCPhotoLibraryStorePolicyNever
- _PFAdjustmentArchivedSettingsKey
- _PFAdjustmentAutoKey
- _PFAdjustmentEnabledKey
- _PFAdjustmentEnvelopeAdjustmentsKey
- _PFAdjustmentEnvelopeEnvelopeVersionKey
- _PFAdjustmentEnvelopeFormatVersionIsValid
- _PFAdjustmentErrorDomain
- _PFAdjustmentFormatVersionIsValid
- _PFAdjustmentFormatVersionKey
- _PFAdjustmentIdentifierKey
- _PFAdjustmentMaskUUIDKey
- _PFAdjustmentSettingsAutoCurrentKey
- _PFAdjustmentSettingsInputValuePrefix
- _PLAccountIsRamped
- _PLAddCPLDeviceLibraryConfigurationChangedObserver
- _PLAlbumFilterFromAlbumListFilter
- _PLAlbumListFilterFromAlbumFilter
- _PLAlbumNotificationAnyPhotoWasAdded
- _PLAlbumNotificationAnyPhotoWasUpdated
- _PLAlbumNotificationMentionsPhoto
- _PLAssetTypeSupportsMasterThumbnail
- _PLBurstUuidFromImageProperties
- _PLCanEnableMediaStreamForAccount
- _PLCloudCommentsDidChangeNotification
- _PLCloudFeedEntriesDidChangeNotification
- _PLCloudPhotoLibraryHasFinishedInitialSync
- _PLColorSpaceNameFromImageProperties
- _PLCreateCroppedImageRefFromImageRef
- _PLCreateSRGBImageIfNecessary
- _PLDescriptionForPhotosHighlightCurationType
- _PLDownloadMissingOriginals
- _PLExifColorSpaceFromImageProperties
- _PLInvitationRecordsDidChangeNotification
- _PLIsCollectionSharesEnabledForPhotoLibraryURL
- _PLIsSharedCollectionsFeatureEnabled
- _PLOrientationFromClockwiseRotationAndFlip
- _PLOrientationFromCounterClockwiseRotation
- _PLOrientationToClockwiseRotation
- _PLPhotoLibraryNotificationAnyAlbumWasAdded
- _PLPhotoLibraryNotificationAnyAlbumWasDeleted
- _PLPhotoLibraryNotificationAnyAlbumWasUpdated
- _PLPhotoLibraryNotificationMentionsAlbum
- _PLPhotoLibraryPhotoNotificationAnyPhotoWasAdded
- _PLPhotoLibraryPhotoNotificationAnyPhotoWasDeleted
- _PLPhotoLibraryShouldReloadNotificationName
- _PLPhotolibraryWellKnownIdentifierDescriptionForPhotoLibrary
- _PLPlatformMediaStreamSupported
- _PLPrimaryDataStoreKeyClassFromData
- _PLPrintSymbolicStackTrace
- _PLRemoveCPLDeviceLibraryConfigurationChangedObserver
- _PLResetLocalPhotos
- _PLResourceTypeSupportsColorSpace
- _PLSOCGroupIdentifierFromImageProperties
- _PLSafeEntityForNameInManagedObjectContext
- _PLSearchAlbumLookupIdentifier
- _PLSearchBackendLibraryChangeTrackingGetLog
- _PLSearchHomeItemTypeName
- _PLSearchIndexCategoryForPLSceneClassificationType
- _PLSearchIndexEnumeratePlacesFromBigToSmall
- _PLSearchIndexEnumeratePlacesFromBigToSmall.PLRevGeoOrderTypes
- _PLShouldCacheIOSurfaces
- _PhotosString
- _SyncedAssetGetIdentifier
- _SyncedAssetGetPartsCount
- _SyncedAssetGetVersion
- _SyncedAssetSyncedGetPartForFormatID
- _SyncedPartGetFaceIndex
- __OBJC_$_CLASS_METHODS_PFAdjustment(Serialization|Validation)
- __OBJC_$_CLASS_METHODS_PFAdjustmentSerialization(Utility)
- __OBJC_$_CLASS_METHODS_PFAdjustmentStack(Serialization|Validation)
- __OBJC_$_CLASS_METHODS_PLAggregateAlbumListChangeNotification
- __OBJC_$_CLASS_METHODS_PLBackgroundJobLowPriorityBatterySearchIndexingWorker
- __OBJC_$_CLASS_METHODS_PLBackgroundJobLowPriorityChargerSearchIndexingWorker
- __OBJC_$_CLASS_METHODS_PLCloudCommentsChangeNotification
- __OBJC_$_CLASS_METHODS_PLCloudFeedEntriesChangeNotification
- __OBJC_$_CLASS_METHODS_PLInvitationRecordsChangeNotification
- __OBJC_$_CLASS_METHODS_PLSearchTrackedChangeTypes
- __OBJC_$_INSTANCE_METHODS_PFAdjustment(Serialization|Validation)
- __OBJC_$_INSTANCE_METHODS_PFAdjustmentStack(Serialization|Validation)
- __OBJC_$_INSTANCE_METHODS_PLAggregateAlbumList
- __OBJC_$_INSTANCE_METHODS_PLAggregateAlbumListChangeNotification
- __OBJC_$_INSTANCE_METHODS_PLBackgroundJobLowPriorityBatterySearchIndexingWorker
- __OBJC_$_INSTANCE_METHODS_PLBackgroundJobLowPriorityChargerSearchIndexingWorker
- __OBJC_$_INSTANCE_METHODS_PLCloudCommentsChangeNotification
- __OBJC_$_INSTANCE_METHODS_PLCloudFeedEntriesChangeNotification
- __OBJC_$_INSTANCE_METHODS_PLInvitationRecordsChangeNotification
- __OBJC_$_INSTANCE_METHODS_PLManagedFolder(PLJournalEntryPayload|Debugging)
- __OBJC_$_INSTANCE_METHODS_PLPhotoLibraryShouldReloadNotification
- __OBJC_$_INSTANCE_METHODS_PLSearchTrackedAttributes
- __OBJC_$_INSTANCE_METHODS_PLSearchTrackedChangeTypes
- __OBJC_$_INSTANCE_METHODS_PLThumbnailResourceDataStoreOptions
- __OBJC_$_INSTANCE_METHODS_PLXPCPhotoLibraryStorePolicyNever
- __OBJC_$_INSTANCE_VARIABLES_PFAdjustment
- __OBJC_$_INSTANCE_VARIABLES_PFAdjustmentStack
- __OBJC_$_INSTANCE_VARIABLES_PLAggregateAlbumList
- __OBJC_$_INSTANCE_VARIABLES_PLAggregateAlbumListChangeNotification
- __OBJC_$_INSTANCE_VARIABLES_PLCloudCommentsChangeNotification
- __OBJC_$_INSTANCE_VARIABLES_PLCloudFeedEntriesChangeNotification
- __OBJC_$_INSTANCE_VARIABLES_PLInvitationRecordsChangeNotification
- __OBJC_$_INSTANCE_VARIABLES_PLPhotoLibraryShouldReloadNotification
- __OBJC_$_INSTANCE_VARIABLES_PLSearchTrackedAttributes
- __OBJC_$_INSTANCE_VARIABLES_PLSearchTrackedChangeTypes
- __OBJC_$_INSTANCE_VARIABLES_PLThumbnailResourceDataStoreOptions
- __OBJC_$_PROP_LIST_PFAdjustment
- __OBJC_$_PROP_LIST_PLAggregateAlbumList
- __OBJC_$_PROP_LIST_PLCloudCommentsChangeNotification
- __OBJC_$_PROP_LIST_PLCloudFeedEntriesChangeNotification
- __OBJC_$_PROP_LIST_PLInvitationRecordsChangeNotification
- __OBJC_$_PROP_LIST_PLPhotoAnalysisServiceClient
- __OBJC_$_PROP_LIST_PLSearchTrackedAttributes
- __OBJC_$_PROP_LIST_PLSearchTrackedChangeTypes
- __OBJC_$_PROP_LIST_PLThumbnailResourceDataStoreOptions
- __OBJC_$_PROP_LIST_PLXPCPhotoLibraryStorePolicyNever
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSFastEnumeration
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PLAssetContainerListChangeObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSFastEnumeration
- __OBJC_$_PROTOCOL_METHOD_TYPES_PLAssetContainerListChangeObserver
- __OBJC_CLASS_PROTOCOLS_$_PFAdjustmentStack
- __OBJC_CLASS_PROTOCOLS_$_PLAggregateAlbumList
- __OBJC_CLASS_PROTOCOLS_$_PLXPCPhotoLibraryStorePolicyNever
- __OBJC_CLASS_RO_$_PFAdjustment
- __OBJC_CLASS_RO_$_PFAdjustmentSerialization
- __OBJC_CLASS_RO_$_PFAdjustmentStack
- __OBJC_CLASS_RO_$_PLAggregateAlbumList
- __OBJC_CLASS_RO_$_PLAggregateAlbumListChangeNotification
- __OBJC_CLASS_RO_$_PLBackgroundJobLowPriorityBatterySearchIndexingWorker
- __OBJC_CLASS_RO_$_PLBackgroundJobLowPriorityChargerSearchIndexingWorker
- __OBJC_CLASS_RO_$_PLCloudCommentsChangeNotification
- __OBJC_CLASS_RO_$_PLCloudFeedEntriesChangeNotification
- __OBJC_CLASS_RO_$_PLInvitationRecordsChangeNotification
- __OBJC_CLASS_RO_$_PLPhotoLibraryShouldReloadNotification
- __OBJC_CLASS_RO_$_PLSearchTrackedAttributes
- __OBJC_CLASS_RO_$_PLSearchTrackedChangeTypes
- __OBJC_CLASS_RO_$_PLThumbnailResourceDataStoreOptions
- __OBJC_CLASS_RO_$_PLXPCPhotoLibraryStorePolicyNever
- __OBJC_LABEL_PROTOCOL_$_NSFastEnumeration
- __OBJC_LABEL_PROTOCOL_$_PLAssetContainerListChangeObserver
- __OBJC_METACLASS_RO_$_PFAdjustment
- __OBJC_METACLASS_RO_$_PFAdjustmentSerialization
- __OBJC_METACLASS_RO_$_PFAdjustmentStack
- __OBJC_METACLASS_RO_$_PLAggregateAlbumList
- __OBJC_METACLASS_RO_$_PLAggregateAlbumListChangeNotification
- __OBJC_METACLASS_RO_$_PLBackgroundJobLowPriorityBatterySearchIndexingWorker
- __OBJC_METACLASS_RO_$_PLBackgroundJobLowPriorityChargerSearchIndexingWorker
- __OBJC_METACLASS_RO_$_PLCloudCommentsChangeNotification
- __OBJC_METACLASS_RO_$_PLCloudFeedEntriesChangeNotification
- __OBJC_METACLASS_RO_$_PLInvitationRecordsChangeNotification
- __OBJC_METACLASS_RO_$_PLPhotoLibraryShouldReloadNotification
- __OBJC_METACLASS_RO_$_PLSearchTrackedAttributes
- __OBJC_METACLASS_RO_$_PLSearchTrackedChangeTypes
- __OBJC_METACLASS_RO_$_PLThumbnailResourceDataStoreOptions
- __OBJC_METACLASS_RO_$_PLXPCPhotoLibraryStorePolicyNever
- __OBJC_PROTOCOL_$_NSFastEnumeration
- __OBJC_PROTOCOL_$_PLAssetContainerListChangeObserver
- ___102-[PLBackgroundJobSharedAssetContainerUpdateWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___102-[PLBackgroundJobSharedAssetContainerUpdateWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke_2
- ___105-[PLBackgroundJobDeferredRenderDerivativesBaseWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___105-[PLBackgroundJobResourceUploadExtensionRunnerWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___105-[PLBackgroundJobResourceUploadExtensionRunnerWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke_2
- ___105-[PLBackgroundJobResourceUploadExtensionRunnerWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke_3
- ___107-[PLBackgroundJobSyndicationResourceSanitizationWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___115-[PLSyndicationResourceDataStore _requestLocalAvailabilityChangeForSyndicationOriginalResource:options:completion:]_block_invoke_2
- ___116-[PLSyndicationSyncServiceWrapper executeQueryForSyncManager:type:startDate:endDate:batchHandler:completionHandler:]_block_invoke
- ___123-[PLBackgroundJobResourceUploadExtensionRunnerWorker criteriaNeedingProcessingInLibrary:validCriterias:outSignalAgainDate:]_block_invoke
- ___123-[PLBackgroundJobResourceUploadExtensionRunnerWorker criteriaNeedingProcessingInLibrary:validCriterias:outSignalAgainDate:]_block_invoke_2
- ___149-[PLSyndicationResourceDataStore _copyAndMarkAsLocallyAvailablePairedLivePhotoResourceForRequestedResource:requestedVideoComplement:sourceURL:error:]_block_invoke
- ___155+[PLSyndicationResourceDataStore provideFileURLAndUnwrapLivePhotoIfNeededForItemIdentifiersWithBundleIDs:destURLs:options:resultHandler:completionHandler:]_block_invoke
- ___162+[PLSyndicationResourceDataStore _provideFileURLAndUnwrapLivePhotoIfNeededForBundleID:syndicationIdentifier:typeIdentifier:isLivePhoto:options:completionHandler:]_block_invoke
- ___165-[PLManagedAsset _generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:retryNumber:allowCancellationByService:clientBundleID:completion:]_block_invoke
- ___165-[PLManagedAsset _generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:retryNumber:allowCancellationByService:clientBundleID:completion:]_block_invoke_2
- ___43-[PLManagedAsset(RM) resourcesWithVersion:]_block_invoke
- ___44+[PLManagedAsset predicateForReframedAssets]_block_invoke
- ___44-[PLGenericAlbum assetsByObjectIDAtIndexes:]_block_invoke
- ___48-[PLIntensiveResourceTask prepareForReplacement]_block_invoke
- ___49+[PLManagedAsset ptpResetEventAndFilenameMapping]_block_invoke
- ___51+[PLManagedAsset ptpAssetIDForEventAndFilenameKey:]_block_invoke
- ___51-[PLSocialGroup runAssetContainmentWithCompletion:]_block_invoke
- ___52-[PLAggregateAlbumList assetContainerListDidChange:]_block_invoke
- ___52-[PLAggregateAlbumList assetContainerListDidChange:]_block_invoke_2
- ___53-[PLServerPhotoLibraryBundle invalidateClientsReason]_block_invoke
- ___55+[PLLocalChangeEventBuilder localEventFromTransaction:]_block_invoke
- ___57-[PLManagedAsset(RM) persistedCombinedProvenanceResource]_block_invoke
- ___57-[PLSearchIndexingRebuildEngine _startRebuildForLibrary:]_block_invoke
- ___57-[PLSearchIndexingRebuildEngine _startRebuildForLibrary:]_block_invoke_2
- ___58-[PLBackgroundJobStatusCenter recordWorkerHasPendingJobs:]_block_invoke
- ___60+[PLManagedAsset ptpSetAssetIDForEventAndFilenameKey:value:]_block_invoke
- ___62+[PLManagedObjectContext changeNotificationObjectMutationKeys]_block_invoke
- ___62+[PLSMetadataUtilities allAlbumsDetailsWriteToPath:inLibrary:]_block_invoke
- ___62+[PLSMetadataUtilities allAlbumsDetailsWriteToPath:inLibrary:]_block_invoke_2
- ___62-[PLNotificationManager noteSharedAlbumUnseenStatusDidChange:]_block_invoke
- ___62-[PLNotificationUNCenter removeNotificationsForNotifications:]_block_invoke
- ___64-[PLNotificationManager noteDidReceiveInvitationForSharedAlbum:]_block_invoke
- ___64-[PLNotificationManager noteDidReceiveInvitationForSharedAlbum:]_block_invoke_2
- ___66-[PLAggregateAlbumListChangeNotification enumerateMovesWithBlock:]_block_invoke
- ___66-[PLBackgroundJobWorker pendingWorkItemsInLibrary:validCriterias:]_block_invoke
- ___66-[PLBackgroundJobWorker pendingWorkItemsInLibrary:validCriterias:]_block_invoke_2
- ___68-[PLCloudPhotoLibraryManager cplConfigurationWithCompletionHandler:]_block_invoke
- ___68-[PLNotificationManager noteDidReceiveCMMInvitationWithMomentShare:]_block_invoke
- ___69+[PLPhotoSharingHelper updateCloudSharedAlbumPublicURLStateOnServer:]_block_invoke
- ___69+[PLPhotoSharingHelper updateCloudSharedAlbumPublicURLStateOnServer:]_block_invoke_2
- ___70+[PLDiagnostics addOSStateHandlerWithTitle:queue:propertyListHandler:]_block_invoke
- ___72+[PLGraphEdge fetchEdgesWithExternalIdentifiers:inManagedObjectContext:]_block_invoke
- ___72+[PLGraphNode fetchNodesWithExternalIdentifiers:inManagedObjectContext:]_block_invoke
- ___73-[PLManagedAssetRecoveryManager identifyAssetsWithInconsistentCloudState]_block_invoke
- ___73-[PLManagedAssetRecoveryManager identifyAssetsWithInconsistentCloudState]_block_invoke_2
- ___73-[PLManagedAssetRecoveryManager identifyAssetsWithInconsistentCloudState]_block_invoke_3
- ___74+[PLPhotoSharingHelper acceptPendingInvitationForAlbum:completionHandler:]_block_invoke
- ___74+[PLPhotoSharingHelper acceptPendingInvitationForAlbum:completionHandler:]_block_invoke_2
- ___76-[PLRebuildJournalManager recreateAllObjectsInManagedObjectContext:options:]_block_invoke
- ___77+[PLPhotoSharingHelper sendPendingInvitationsForAlbum:resendInvitationGUIDs:]_block_invoke
- ___77-[PLBackgroundJobLowPriorityBatterySearchIndexingWorker locrIdentifyingBlock]_block_invoke
- ___77-[PLBackgroundJobLowPriorityChargerSearchIndexingWorker locrIdentifyingBlock]_block_invoke
- ___77-[PLNotificationManager noteUserDidNavigateAwayFromSharedAlbum:photoLibrary:]_block_invoke
- ___77-[PLNotificationManager noteUserDidNavigateAwayFromSharedAlbum:photoLibrary:]_block_invoke_2
- ___78+[PLPhotoSharingHelper markPendingInvitationAsSpamForAlbum:completionHandler:]_block_invoke
- ___78-[PLNotificationManager noteDidReceiveExpiringCMMInvitationsWithMomentShares:]_block_invoke
- ___79-[PLConcurrencyLimiterRecordingReader aggregatesSortedByTotalExecTimeForQueue:]_block_invoke
- ___79-[PLManagedObjectPagingIterator countRemainingWithManagedObjectContext:logger:]_block_invoke
- ___79-[PLManagedObjectPagingIterator countRemainingWithManagedObjectContext:logger:]_block_invoke_2
- ___79-[PLManagedObjectPagingIterator countRemainingWithManagedObjectContext:logger:]_block_invoke_3
- ___79-[PLManagedObjectPagingIterator countRemainingWithManagedObjectContext:logger:]_block_invoke_4
- ___80+[PLPhotoSharingHelper updateCloudSharedAlbumMultipleContributorsStateOnServer:]_block_invoke
- ___80+[PLPhotoSharingHelper updateCloudSharedAlbumMultipleContributorsStateOnServer:]_block_invoke_2
- ___81-[CNContactStore(PhotoLibraryAdditions) contactsMatchingPhoneNumber:keysToFetch:]_block_invoke
- ___82+[PLPersistentHistoryUtilities fetchTransactionCountSinceToken:withContext:error:]_block_invoke
- ___82-[PLPhotoEditRenderer calculateLongExposureFusionParametersWithCompletionHandler:]_block_invoke
- ___83-[PLNotificationManager noteMultipleContributorStatusChangedForAlbum:mstreamdInfo:]_block_invoke
- ___84+[PLGraphNode fetchObjectIDsForNodesWithExternalIdentifiers:inManagedObjectContext:]_block_invoke
- ___84-[PLBackgroundJobWorker pendingCriteriaInLibrary:validCriterias:outSignalAgainDate:]_block_invoke
- ___84-[PLBackgroundJobWorker pendingCriteriaInLibrary:validCriterias:outSignalAgainDate:]_block_invoke_2
- ___85-[PLNotificationManager noteInvitationRecordStatusChanged:fromOldState:mstreamdInfo:]_block_invoke
- ___86-[PLBackgroundJobPersonSyncWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___86-[PLBackgroundJobStableHashWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___87-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:completionHandler:]_block_invoke
- ___87-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:completionHandler:]_block_invoke_2
- ___87-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:completionHandler:]_block_invoke_3
- ___87-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:completionHandler:]_block_invoke_4
- ___87-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:completionHandler:]_block_invoke_5
- ___87-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:completionHandler:]_block_invoke_6
- ___87-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:completionHandler:]_block_invoke_7
- ___89-[PLBackgroundJobEditRenderingWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___90-[PLBackgroundJobSearchIndexingWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___92+[PLCloudResource resetPrefetchStateForResourcesWithResourceType:itemIdentifiers:inLibrary:]_block_invoke
- ___93+[PLAssetSharingUtilities assetForVideoURL:metadata:library:outAudioMix:outVideoComposition:]_block_invoke
- ___93+[PLAssetSharingUtilities assetForVideoURL:metadata:library:outAudioMix:outVideoComposition:]_block_invoke_2
- ___93+[PLAssetSharingUtilities assetForVideoURL:metadata:library:outAudioMix:outVideoComposition:]_block_invoke_3
- ___93-[PLBackgroundJobDuplicateDetectorWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___96-[PLBackgroundJobResourceAvailabilityWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___96-[PLSyndicationResourceDataStore _copyItemAtURL:withPathManager:destFileIdentifier:inode:error:]_block_invoke
- ___98-[PLCollectionShareSharedStreamBackend checkServerForChangesForCollectionShare:completionHandler:]_block_invoke_8
- ___99-[PLBackgroundJobSyndicationAssetCleanupWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___PLDownloadMissingOriginals_block_invoke
- ___PLSearchIndexEnumeratePlacesFromBigToSmall_block_invoke
- ___albumListTypes
- ___block_descriptor_123_e8_32s40s48s56s64s72s80s88s96s104bs112r_e37_v32?0"NSURL"8"NSURL"16"NSError"24ls32l8s40l8s48l8r112l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
- ___block_descriptor_128_e8_32s40s48s56s64s72s80s88bs96r104r112r_e5_v8?0ls32l8s40l8r96l8s48l8r104l8s56l8s64l8s72l8s80l8s88l8r112l8
- ___block_descriptor_129_e8_32s40s48s56s64s72s80s88s96s104s112s120r_e32_v32?0"PLManagedObject"8Q16^B24ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8r120l8s96l8s104l8s112l8
- ___block_descriptor_130_e8_32s40s48s56s64s72s80s88s96r104r112r_e5_v8?0ls32l8s40l8r96l8s48l8s56l8r104l8r112l8s64l8s72l8s80l8s88l8
- ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96s104s112bs120n11_8_8_s0_t8w8_e5_v8?0l
- ___block_descriptor_168_e8_32s40s48s56s64s72s80s88r96r104r112r120r128r136r144r152r_e12_v20?0I8^B12ls32l8r88l8r96l8r104l8s40l8r112l8s48l8r120l8s56l8r128l8s64l8r136l8s72l8r144l8s80l8r152l8
- ___block_descriptor_168_e8_32s40s48s56s64s72s80s88s96s104s112s120r128r136r144r152r_e5_v8?0ls32l8s40l8r120l8s48l8r128l8s56l8s64l8s72l8s80l8s88l8r136l8r144l8s96l8r152l8s104l8s112l8
- ___block_descriptor_176_e8_32s40s48s56s64s72s80s88s96s104s112s120s128bs136bs144r152r_e63_v60?0B8"NSURL"12"NSURL"20Q28q36"NSDictionary"44"NSError"52ls32l8s40l8s48l8s56l8s64l8s72l8s80l8r144l8s88l8r152l8s96l8s104l8s112l8s120l8s128l8s136l8
- ___block_descriptor_208_e8_32s40s48s56s64s72s80s88s96s104s112r120r128r136r144r152r160r168r176r184r_e53_v40?0"LEOItem"8"PLLeoLexemeIDSet"16"NSDate"24^B32ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8r112l8r120l8r128l8r136l8r144l8r152l8s104l8r160l8r168l8r176l8r184l8
- ___block_descriptor_32_e29_q24?0"NSValue"8"NSValue"16l
- ___block_descriptor_32_e33_B16?0"PLBackgroundJobCriteria"8l
- ___block_descriptor_32_e41_B24?0"PLManagedAsset"8"NSDictionary"16l
- ___block_descriptor_40_e8_32bs_e15_v16?0"NSURL"8ls32l8
- ___block_descriptor_40_e8_32r_e11_v24?0Q8Q16lr32l8
- ___block_descriptor_40_e8_32s_e31_v32?0"PLNotification"8Q16^B24ls32l8
- ___block_descriptor_40_e8_32s_e33_B16?0"PLBackgroundJobCriteria"8ls32l8
- ___block_descriptor_42_e8_32s_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_48_e8_32r_e17_v16?0"NSError"8lr32l8
- ___block_descriptor_48_e8_32r_e31_v32?0"PLGenericAlbum"8Q16^B24lr32l8
- ___block_descriptor_48_e8_32s40bs_e103_^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16?0^{os_state_hints_s=I*II}8ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e11_v24?0Q8Q16ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e15_v16?0"NSURL"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40r_e15_v32?08Q16^B24ls32l8r40l8
- ___block_descriptor_48_e8_32s_e33_B16?0"PLBackgroundJobCriteria"8ls32l8
- ___block_descriptor_49_e8_32s40bs_e24_v16?0"PLPhotoLibrary"8ls32l8s40l8
- ___block_descriptor_56_e8_32r40r48r_e67_v40?0"AVAsset"8"AVAudioMix"16"AVVideoComposition"24"NSError"32lr32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40bs48r_e21_v24?0"NSString"8Q16ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48s_e12_v24?0Q8^B16ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs_e27_v24?0"NSURL"8"NSError"16ls48l8s32l8s40l8
- ___block_descriptor_72_e8_32s40s48r56r64r_e27_v24?0"NSURL"8"NSError"16ls32l8r48l8r56l8r64l8s40l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8r56l8s48l8r64l8
- ___block_descriptor_73_e8_32s40s48bs56r_e5_v8?0lr56l8s32l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56r64r72r_e5_v8?0lr56l8s32l8r64l8s40l8s48l8r72l8
- ___block_descriptor_81_e8_32s40s48s56r64r72r_e24_v16?0"PLPhotoLibrary"8ls32l8s40l8s48l8r56l8r64l8r72l8
- ___block_descriptor_88_e8_32s40s48s56s64bs72r_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8s64l8r72l8s56l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8s80l8s56l8s64l8s72l8
- ___cacheIOSurfaces
- ___getPILongExposureFusionAutoCalculatorClass_block_invoke
- __cplDeviceLibraryConfigurationChanged
- __cplPendingDeviceLibraryConfigurationChanged
- __hasChangesForCloudShared:.pl_once_object_49
- __hasChangesForCloudShared:.pl_once_token_49
- _archivedAssetUUIDForPathDictionary
- _archivedAssetUUIDForPathDictionary_block_invoke.s_cplAssetDirectoryPrefix
- _archivedAssetUUIDForPathDictionary_block_invoke.s_onceToken
- _changeNotificationObjectIDKeys.pl_once_object_46
- _changeNotificationObjectIDKeys.pl_once_token_46
- _changeNotificationObjectIDMutationKeys.pl_once_object_45
- _changeNotificationObjectIDMutationKeys.pl_once_token_45
- _changeNotificationObjectKeys.pl_once_object_44
- _changeNotificationObjectKeys.pl_once_token_44
- _changeNotificationObjectMutationKeys.pl_once_object_43
- _changeNotificationObjectMutationKeys.pl_once_token_43
- _evaluateWhiteBalanceValueWithOriginalExifProperties:.canonWhiteBalance
- _getPILongExposureFusionAutoCalculatorClass.softClass
- _kCGImagePropertyCIFFWhiteBalanceIndex
- _kCGImagePropertyExifColorSpace
- _kCGImagePropertyExifFlash
- _kCGImagePropertyExifLightSource
- _kCGImagePropertyExifWhiteBalance
- _kPhotosApplicationURLAlbumID
- _kPhotosApplicationURLEventScheme
- _kPhotosApplicationURLEventShowAlbum
- _kPhotosApplicationURLEventShowImport
- _kPhotosApplicationURLEventUICommandKey
- _objc_msgSend$_assetsWithJPGFilenameAndRawPrimaryImageResourcePredicate
- _objc_msgSend$_cloneResourcesForSharePlaceholderAsset:withPlaceholderResourceURLToSourceResourceURLMap:fileManager:photoLibrary:
- _objc_msgSend$_copyAndMarkAsLocallyAvailablePairedLivePhotoResourceForRequestedResource:requestedVideoComplement:sourceURL:error:
- _objc_msgSend$_copyItemAtURL:withPathManager:destFileIdentifier:inode:error:
- _objc_msgSend$_copyJobContentsToHoldingDirectoryWithUUID:incomingPath:job:
- _objc_msgSend$_countOfLocalCloudResourcesOfType:inManagedObjectContext:forMediumSized:localCount:unavailableCount:error:
- _objc_msgSend$_customSharedAlbumExportsOutputDirectoryForAssetWithUUID:
- _objc_msgSend$_debugDescription
- _objc_msgSend$_detailsForAlbum:
- _objc_msgSend$_enforcePrefetchModeForVisualIntelligenceLibraryIfNeededWithCPLSettings:
- _objc_msgSend$_enqueueCloudCommentsNotifications
- _objc_msgSend$_enqueueCloudFeedEntriesChangeNotifications
- _objc_msgSend$_enqueueInvitationRecordsChangeNotification:
- _objc_msgSend$_evaluateUpdatedAssets
- _objc_msgSend$_featureAnalysisLexemeCategories
- _objc_msgSend$_generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:retryNumber:allowCancellationByService:clientBundleID:completion:
- _objc_msgSend$_getAvailableVersionedThumbnailIndexesWithCount:inLibrary:handler:
- _objc_msgSend$_imagesWithZeroWidthHeightPredicate
- _objc_msgSend$_initWithFullReload
- _objc_msgSend$_initWithInsertedEntries:updatedEntries:deletedEntries:
- _objc_msgSend$_inq_pendingJobsForBundle:workerTypes:validCriterias:
- _objc_msgSend$_inq_pendingJobsOnBuffer:validCriterias:
- _objc_msgSend$_inq_pendingJobsOnBundles:validCriterias:
- _objc_msgSend$_installFTSIndexesInModel:
- _objc_msgSend$_invalidateAllAlbums
- _objc_msgSend$_irisesWithZeroVideoCpDuration
- _objc_msgSend$_isAuthorizedAssetUUID:inManagedObjectContext:
- _objc_msgSend$_leo_computeSnapshotForPhotoLibrary:completionHandler:
- _objc_msgSend$_predicateForAdjustedAssetsWithMissingResources
- _objc_msgSend$_processingSetURL
- _objc_msgSend$_provideFileURLAndUnwrapLivePhotoIfNeededForBundleID:syndicationIdentifier:typeIdentifier:isLivePhoto:options:completionHandler:
- _objc_msgSend$_ptpEventInfoIsolationQueue
- _objc_msgSend$_setDidCalculateDiffs:
- _objc_msgSend$_startRebuildForLibrary:
- _objc_msgSend$_unpackPVTBundleAtURL:primaryURL:secondaryURL:error:
- _objc_msgSend$_userDidDeleteSharedAssets:
- _objc_msgSend$aa_formattedUsername
- _objc_msgSend$addAssetContainerListChangeObserver:containerList:
- _objc_msgSend$addInfosForRecipients:
- _objc_msgSend$archiveAssetUUIDForPathPlist:
- _objc_msgSend$archiveDictionary
- _objc_msgSend$archivedAssetUUIDForURL:
- _objc_msgSend$assetAttributesTrackedForSearch
- _objc_msgSend$assetUUIDRecoveryMappingPath
- _objc_msgSend$backgroundJobWorkerTypesMaskGuestAssetSync:personSync:syndicationSync:syndicationResourceSanitization:syndicationResourceDownload:syndicationAssetCleanup:assetStack:duplicateDetector:deferredRenderDerivativesLowPriority:deferredRenderDerivativesHighPriority:resourceAvailability:stableHash:editRenderingImage:editRenderingVideo:highPrioritySearchIndexing:lowPriorityBatterySearchIndexing:lowPriorityChargerSearchIndexing:sharedAssetContainerUpdate:assetResourceUploadJob:assetResourceUploadExtensionRunner:featureAvailability:optimizeTableThumbs:cascadeDonation:provenanceTimestamp:
- _objc_msgSend$changedIndexesRelativeToSnapshot
- _objc_msgSend$changedObjects
- _objc_msgSend$compressData:error:
- _objc_msgSend$containsTypes:
- _objc_msgSend$countOfIndexesInRange:
- _objc_msgSend$countRemainingWithManagedObjectContext:logger:
- _objc_msgSend$cplDeviceLibraryConfigurationChanged
- _objc_msgSend$cplPendingDeviceLibraryConfigurationChanged
- _objc_msgSend$createLogger
- _objc_msgSend$criteriaNeedingProcessingInLibrary:validCriterias:outSignalAgainDate:
- _objc_msgSend$debugClient
- _objc_msgSend$deleteResourceForSidecarRepresentation:
- _objc_msgSend$descriptionForEventName:
- _objc_msgSend$detectedFaceAttributesTrackedForSearch
- _objc_msgSend$envelopeDictionary
- _objc_msgSend$eventInfoForPTP
- _objc_msgSend$executeQueryForSyncManager:type:startDate:endDate:batchHandler:completionHandler:
- _objc_msgSend$extractPathToAssetUUIDRecoveryMappingFromDatabasePath:
- _objc_msgSend$fetchingAlbumAttributesTrackedForSearch
- _objc_msgSend$fileURLFromAssetURL:photoLibrary:
- _objc_msgSend$filteredAlbumList:filter:
- _objc_msgSend$finishDecoding
- _objc_msgSend$generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:allowCancellationByService:clientBundleID:completion:
- _objc_msgSend$generatePathToAssetUUIDRecoveryMapping
- _objc_msgSend$highlightAttributesTrackedForSearch
- _objc_msgSend$initCMMInvitationWithMomentShare:
- _objc_msgSend$initNotificationWithPhotoLibrary:
- _objc_msgSend$initWithAggregateAlbumList:fromAlbumListChangeNotification:indexOffset:
- _objc_msgSend$initWithArchiveDictionary:
- _objc_msgSend$initWithEnvelopeDictionary:
- _objc_msgSend$initWithExpiringMomentShares:
- _objc_msgSend$initWithIdentifier:settings:autoIdentifier:autoSettings:enabled:
- _objc_msgSend$initWithIdentifier:settings:autoIdentifier:autoSettings:enabled:maskUUID:
- _objc_msgSend$initWithInvitationAlbum:
- _objc_msgSend$initWithInvitationRecordStatusChanged:
- _objc_msgSend$initWithMessage:
- _objc_msgSend$initWithMultipleContributorEnabledForAlbum:
- _objc_msgSend$initWithName:elements:
- _objc_msgSend$initWithProperty:collationType:
- _objc_msgSend$initWithTransaction:
- _objc_msgSend$initWithZeroWorkItemsForValidCriteria
- _objc_msgSend$isLikePhoneNumber:
- _objc_msgSend$isValidArchiveDictionary:errors:
- _objc_msgSend$isValidEnvelopeDictionary:errors:
- _objc_msgSend$isVisualIntelligenceDefaultLibrary
- _objc_msgSend$lastImportedPhotosAlbumCreateIfNeeded:
- _objc_msgSend$localizedFailureReason
- _objc_msgSend$managedAlbumAttributesTrackedForSearch
- _objc_msgSend$maskUUID
- _objc_msgSend$mediaAnalysisAssetAttributesTrackedForSearch
- _objc_msgSend$memoryAttributesTrackedForSearch
- _objc_msgSend$noteUserDidChangeStatusForMomentShare:photoLibrary:
- _objc_msgSend$noteUserDidNavigateAwayFromCollectionShare:photoLibrary:
- _objc_msgSend$noteUserDidReadCommentOnSharedAsset:photoLibrary:
- _objc_msgSend$notificationForAggregateAlbumList:fromAlbumListChangeNotification:indexOffset:
- _objc_msgSend$notificationWithAlbum:snapshot:
- _objc_msgSend$notificationWithAsset:snapshot:
- _objc_msgSend$notificationWithFullReload
- _objc_msgSend$notificationWithInsertedEntries:updatedEntries:deletedEntries:
- _objc_msgSend$pendingCriteriaInLibrary:validCriterias:outSignalAgainDate:
- _objc_msgSend$pendingWorkItemsInLibrary:validCriterias:
- _objc_msgSend$personAttributesTrackedForSearch
- _objc_msgSend$phoneNumbers
- _objc_msgSend$placesAlbumListInPhotoLibrary:
- _objc_msgSend$postShouldReloadNotificationWithPhotoLibrary:
- _objc_msgSend$predicateForUploadableAssetsWithMasterCloudLocalStateNotEqualTo:cplFeatureDataclasses:
- _objc_msgSend$prepareForReplacement
- _objc_msgSend$privateDownloadCloudPhotoLibraryAsset:resourceType:highPriority:completionHandler:
- _objc_msgSend$provideFileURLAndUnwrapLivePhotoIfNeededForItemIdentifiersWithBundleIDs:destURLs:options:resultHandler:completionHandler:
- _objc_msgSend$removeAssetContainerListChangeObserver:containerList:
- _objc_msgSend$requestAVAssetWithResultHandler:
- _objc_msgSend$runWithCompletionHandler:
- _objc_msgSend$scenesAlbumListInPhotoLibrary:
- _objc_msgSend$searchTrackedAttributes
- _objc_msgSend$serializeDictionary:error:
- _objc_msgSend$setCloudRelationshipState:
- _objc_msgSend$setDeletedEntries:
- _objc_msgSend$setDouble:forKey:
- _objc_msgSend$setIndexes:
- _objc_msgSend$setInsertedEntries:
- _objc_msgSend$setShouldReload:
- _objc_msgSend$setUpdatedEntries:
- _objc_msgSend$setZeroWorkItemsForValidCriteria:
- _objc_msgSend$setupPlaceholderAssetWithRequiredPropertiesFromSourceAsset:placeholderAssetUUID:bundleScope:share:importSessionID:bakeInAdjustmentsFromSourceAsset:flattenLivePhoto:copyTitleDescriptionAndKeywords:copyCameraProcessingAdjustmentResources:copyProvenanceData:isCurrentUser:library:
- _objc_msgSend$validateArchive:containsEntryWithKey:ofType:errors:
- _objc_msgSend$validateValue:isOfType:errors:
- _objc_msgSend$workItemsNeedingProcessingInLibrary:validCriterias:
- _objc_msgSend$zeroWorkItemsForValidCriteria
- _predicateForReframedAssets.onceToken
- _predicateForReframedAssets.predicate
- _predicateToExcludeAssetsMissingMasterThumbnailsWithThumbnailIndexKeyPath:.pl_once_object_16
- _predicateToExcludeAssetsMissingMasterThumbnailsWithThumbnailIndexKeyPath:.pl_once_token_16
- _predicateToExcludeCameraAutoAdjustments.pl_once_object_17
- _predicateToExcludeCameraAutoAdjustments.pl_once_token_17
- _predicateToExcludeHiddenAssetsWithHiddenKeyPath:.pl_once_object_12
- _predicateToExcludeHiddenAssetsWithHiddenKeyPath:.pl_once_token_12
- _predicateToExcludeNonvisibleBurstAssets.pl_once_object_14
- _predicateToExcludeNonvisibleBurstAssets.pl_once_token_14
- _predicateToExcludeNonvisibleBurstAssetsWithAvalanchePickTypeKeyPath:.pl_once_object_15
- _predicateToExcludeNonvisibleBurstAssetsWithAvalanchePickTypeKeyPath:.pl_once_token_15
- _predicateToExcludeRestrictedLockedAssets.pl_once_object_13
- _predicateToExcludeRestrictedLockedAssets.pl_once_token_13
- _predicateToExcludeTrashedAssets.pl_once_object_10
- _predicateToExcludeTrashedAssets.pl_once_token_10
- _predicateToExcludeTrashedAssetsWithTrashedStateKeyPath:.pl_once_object_11
- _predicateToExcludeTrashedAssetsWithTrashedStateKeyPath:.pl_once_token_11
- _xpc_dictionary_create_reply
CStrings:
+ "\n\t%@ : %@"
+ "%@ (%llu)"
+ "%K == %@ AND %K == %@ AND %K == nil"
+ "%K == %@ AND %K == %@ AND (%K == nil OR %K == nil)"
+ "%K == nil OR %K >= %K"
+ "%K > %@ AND %K.%K == NO"
+ "%{public}@ requested to stop running remaining work items"
+ "%{public}@ setting _shouldDeferTask to YES due to error: %@"
+ "+[PLManagedAsset countUsedAssetsWithKind:excludeTrashed:excludeInvisible:excludeCloudShared:excludePhotoStream:inManagedObjectContext:]"
+ "+[PLManagedObject entityInManagedObjectContext:]"
+ "-[PLAssetsdLibraryInternalService getSearchDonationProgressShouldCompute:shouldReport:reply:]"
+ "-[PLBackgroundJobGuestAssetSyncWorker workItemsNeedingProcessingInLibrary:currentCriteria:]"
+ "-[PLBackgroundJobPersonSyncWorker workItemsNeedingProcessingInLibrary:currentCriteria:]"
+ "-[PLBackgroundJobService _inq_pendingJobsForBundle:workerTypes:currentCriteria:]"
+ "-[PLCloudPhotoLibraryManager _linkOrphanedCollectionShareContributorsWithCPLSettings:]"
+ "-[PLFeatureAvailabilityComputer _addHighlightStatusToProcessingSnapshot:managedObjectContext:error:]"
+ "-[PLFeatureAvailabilityComputer _assetCountForPredicate:managedObjectContext:error:]"
+ "-[PLFeatureAvailabilityComputer _fetchHighlightStatusInPhotoLibrary:completionBlock:]_block_invoke"
+ "-[PLManagedAsset _generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:retryNumber:allowCancellationByService:clientBundleID:shouldSaveMediaConversionResultBlock:completion:]"
+ "-[PLManagedAsset(Share) setupPlaceholderAssetWithRequiredPropertiesFromSourceAsset:placeholderAssetUUID:bundleScope:share:importSessionID:bakeInAdjustmentsFromSourceAsset:flattenLivePhoto:copyTitleDescriptionAndKeywords:copyCameraProcessingAdjustmentResources:copyLocationData:copyProvenanceData:isCurrentUser:library:]"
+ "-[PLModelMigrationAction_MigrateCloudSharedAlbumToCollectionShare performActionWithManagedObjectContext:error:]_block_invoke_3"
+ "-[PLSharedAlbumsActivityKVSListener _keyValueStoreDidChangeExternally:]"
+ "-[PLSharedManagedObjectContext _mergeChangesFromDidSaveDictionary:usingObjectIDs:]"
+ "<%@ %@> primary label code: %d"
+ "Applying key asset %{public}@ from scope change to CollectionShare %{public}@ (resolved locally %d, incoming thumbnail length %lu)"
+ "Badge: Calculated unread album count: %lu"
+ "Badge: Failed to fetch unread entries: %@"
+ "Badge: Failed to fetch unread posts: %@"
+ "Badge: KVS eventLogLastEnteredDate changed, recalculating badge"
+ "Badge: KVS lastSeenDate changed, recalculating badge"
+ "Badge: sharedAlbumsUnreadCount called outside assetsd, returning 0"
+ "Checking all library bundles for pending jobs on signal buffer %@"
+ "Checking for work on library %@ (%@)"
+ "Clearing key asset %{public}@ on CollectionShare %{public}@ per no-key scope change, discarding thumbnail of length %lu (asset cloudLocalState %d, master cloudLocalState %d)"
+ "Compute snapshot for search progress failed with error: %@"
+ "Creating sqliteErrorIndicatorFile"
+ "Creating sqliteErrorIndicatorFile before lightweight migration"
+ "Creating sqliteErrorIndicatorFile for background Migration failure"
+ "Creating sqliteErrorIndicatorFile for excessive persistent history size"
+ "DefaultToKeepOriginals"
+ "Deleting %tu identifiers from system Leo store"
+ "Donating %tu items to managed Leo store"
+ "Donating %tu items to system Leo store"
+ "Donating search index rebuild batch for entity: %{public}@, count remaining: %@, resume objectID: %{public}@"
+ "Drop Spotlight index finished"
+ "Drop global Spotlight index finished"
+ "Dropping Spotlight index"
+ "Dropping search index, source: %{public}@, reasons: %{public}@, library identifier: %@"
+ "Error accessing CPL settings"
+ "Error setting prefetch mode on CPL settings"
+ "Failed to apply the default keep-originals prefetch mode: %@"
+ "Failed to create sqliteErrorIndicatorFile to guard against lightweight migration crash loop"
+ "Failed to create sqliteErrorIndicatorFile: %@."
+ "Failed to deserialize sqliteErrorIndicatorFile. Error: %@"
+ "Failed to fetch %@ records to link to participant %{public}@: %@"
+ "Failed to fetch %@ records with an unresolved contributor: %@"
+ "Failed to look for migrated CPL collection shares: %@"
+ "Failed to obtain library identifier for library : %{public}@"
+ "Failed to obtain processing set URL"
+ "Filesystem Import took %1.1fs"
+ "Finished donating %tu items and deleting %tu items in managed Leo store"
+ "FixupAssetsStuckInDeferredProcessing: failed to reingest final image for asset %{public}@: %@"
+ "FixupAssetsStuckInDeferredProcessing: reingested %ld, cleared %ld, skipped %ld"
+ "Found sqliteErrorIndicatorFile (force rebuild indicator), will not attempt lightweight migration"
+ "Found work for library %@ (%@) - W: %{public}@ C: %{public}@ Cache hit: NO"
+ "Found work for library %@ (%@) - W: %{public}@ C: %{public}@ Cache hit: YES"
+ "Ignoring blocked identity for participant %{public}@ that is also a member of share %{public}@"
+ "Invalid entity to process for spotlight search indexing: %{public}@"
+ "KVS Listener: Already listening, ignoring startListening call"
+ "KVS Listener: Loaded initial lastSeenDate: %@, eventLogLastEnteredDate: %@"
+ "KVS Listener: Started listening for KVS changes"
+ "KVS Listener: Stopped listening for KVS changes"
+ "KVS Listener: eventLogLastEnteredDate updated to %@"
+ "KVS Listener: lastSeenDate updated to %@"
+ "Library %@ has jobs for %tu criteria"
+ "Library has migrated CPL collection shares; will look for orphaned contributors once CPL is available"
+ "Library identifier for library : [%{public}@ : %{public}@]"
+ "Linked %lu assets, %lu posts and %lu comments in share %{public}@ to participant %{public}@"
+ "LowPrioritySearchIndexing"
+ "MADEmbeddingSearchQueryResult returned nil sortedResults with no error"
+ "NSManagedObjectContext is NULL looking for entity named %{public}@ (caller: %s)"
+ "No CPL settings on CPL library open, skipping the default prefetch mode"
+ "No custom key asset on CollectionShare %{public}@; pushing a scope change that omits keyAssetIdentifier and thumbnailImageData"
+ "No further bundles are registered for work under any criteria, shutting down."
+ "No participant matches contributor user identifier %@ in share %@ for asset %@; the contributor is linked once that participant syncs"
+ "No participant matches contributor user identifier %@ in share %@ for comment %@; the participant is linked once they sync"
+ "No participant matches contributor user identifier %@ in share %@ for post %@; the contributor is linked once that participant syncs"
+ "Not stashing camera job %{public}@, no asset UUID provided"
+ "PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing"
+ "PLRebuildUserNotification snooze for library %@ for %tu hour(s) until %@"
+ "PLRebuildUserNotificationSnoozeState"
+ "PLSearchIndexProgressAnalyzedAndIndexedCountKey"
+ "PLSearchIndexProgressInIndexCountKey"
+ "PLSearchIndexProgressNeedingDonationCountKey"
+ "PLSearchIndexProgressPartiallyDonatedCountKey"
+ "PLSearchIndexProgressTotalAssetCountKey"
+ "PLSyndicationResourceFileCoordinator.m"
+ "PLXPC Service: getSearchDonationProgressShouldCompute:shouldReport:reply:"
+ "PLXPC Service: getStateCaptureDictionaryWithReply:"
+ "PXSharedAlbumsActivityLastSeenDateKey"
+ "PXSharedAlbumsEventLogLastEnteredDateKey"
+ "Photos cannot proceed with the library (%@) in its current state.\n\n%@%@\n\nSelect \"Rebuild\" to allow rebuild of the photo library database (possible data loss) or \"Not now\" to stop now and leave it as-is"
+ "PostCollectionShareExpiringSoonNotification: skipping notification for collection: %@ because all assets are already saved to library"
+ "Preparing search index rebuild, called by %{public}@"
+ "Preserving generative attribution for asset %{public}@; render declares none"
+ "Preserving not-yet-pushed key asset %{public}@ on CollectionShare %{public}@ against no-key scope change (asset cloudLocalState %d, master cloudLocalState %d)"
+ "Progress donation to Spotlight failed because CSSearchableIndex is nil"
+ "Rejecting runDaemonJob from unauthorized client %d: %@"
+ "Removing sqliteErrorIndicatorFile after successful migration"
+ "Reported search indexing progress"
+ "Reporting search progress failed with error: %@"
+ "Resuming search index rebuild from entity: %{public}@, count remaining: %{public}@, resume objectID: %{public}@"
+ "Search index rebuild completed (start date: %@)"
+ "Search index rebuild failed (start date: %@)"
+ "Search index rebuild paused (start date: %@)"
+ "Search index rebuild resumed (type: %{public}@, reasons: %{public}@, called by: %{public}@, start date: %@)"
+ "Search index rebuild started (type: %{public}@, reasons: %{public}@, called by: %{public}@)"
+ "Set the Visual Intelligence library to keep originals"
+ "Shared Albums not enabled"
+ "Should NOT show PLRebuildUserNotification for library %@ because of snooze until %@"
+ "Skipping direct upload for placeholder asset %@ - a master cannot be created until its resources land"
+ "Stashing camera job %{public}@ for replay at %@"
+ "Successfully dropped system leo store"
+ "System Leo delete items failed with error: %@"
+ "System Leo donate items failed with error: %@"
+ "System Leo store is nil, possible force close during indexing"
+ "System Leo update lexemes with entity scores failed with error: %@"
+ "There are still bundles registered for work in the processing set, submitting activities."
+ "Unable to get attributes for sqliteErrorIndicatorFile %@: %@"
+ "Unable to register PLPhotoLibrary with bundle: bundle already shut down (reason: %{public}@ / %ld)"
+ "Unexpected nil CSSearchableIndex"
+ "Updating scores for %tu lexemes in system Leo store"
+ "Using master thumbnail during resource clone of placeholder Asset: %@"
+ "Visual Intelligence library already keeps originals"
+ "Will report search indexing progress"
+ "[RM] %@ Finalized deferred finalization image/video resource exists but proxy is missing, promoting to original. resource: %{public}@, asset: %{public}@, path: %{public}@"
+ "[RM] %{public}@ Deferred finalization resource file exists at %{public}@ (proxy exists: %{bool}d), will attempt to promote existing file"
+ "[RM] Repairing resource - DF resource exists but proxy is missing, promoting to original"
+ "[RTM] %{public}@ task %{public}@ unable to replace existing task %{public}@ that is uninterruptible"
+ "[resource] %{public}@ provider delivered no video complement for live photo asset: %{public}@"
+ "[resource] %{public}@ unable to copy provided file for asset: %{public}@, error: %@"
+ "[resource] failed to copy provided files for identifier: %{public}@, error: %@"
+ "[resource] failed to copy syndication file from url: %@ to url: %@, error: %@"
+ "[resource] provider file at url: %@ is still dataless, so the copy was refused rather than fetching it; reporting as needing network access. error: %@"
+ "[resource] provider response held no %{public}@, source url: %@"
+ "[resource] unable to coordinate reading provider file at url: %@, video complement url: %@, error: %@"
+ "_linkOrphanedCollectionShareContributors"
+ "_linkOrphanedCollectionShareContributors: linked %{public}lu contributors before failing: %{public}@"
+ "_linkOrphanedCollectionShareContributors: linked the contributor of %{public}lu records"
+ "_linkOrphanedCollectionShareContributors: looking for the contributors of %{public}lu collection share records"
+ "_linkOrphanedCollectionShareContributors: no collection share content is missing its contributor"
+ "addAssetWithURLs: unable to find uuid for main URL: %{public}@"
+ "additionalAttributes.destinationAssetCopyState"
+ "album %@ has %lu missing assets and %lu known assets to check for missing comments"
+ "assertion failure: \"node != ((void*)0)\" -> %llu"
+ "assertion failure: Couldn't find container class for node: %@"
+ "assertion failure: _lock_canAcceptResponders returned YES but _lock_addResponder failed"
+ "assertion failure: shouldSaveMediaConversionResultBlock is a required parameter"
+ "com.apple.PhotosViewService"
+ "contributorUserIdentifier"
+ "criteriaNeedingProcessing(in:currentCriteria:outSignalAgainDate:)"
+ "file coordination did not grant a read claim for %@"
+ "fileCoordinator"
+ "lastBundleShutdownDate"
+ "lastBundleShutdownLibraryID"
+ "lastBundleShutdownReason"
+ "leo donatable item: %{public}@ object of entity %{public}@ uuid: %{public}@ "
+ "managed Leo store donate and delete"
+ "no CPL settings"
+ "nodeContainerClass: %{public}@ is not a kind of %{public}@ for node: %{public}@"
+ "persistentURL is nil"
+ "primary file"
+ "provider delivered no video complement for a live photo"
+ "provider file is dataless and was not materialized: %@"
+ "provider response held no %@"
+ "pulling missing comment %@ for known asset %@ in album %@"
+ "recording person info only for owner participant with personID: %@"
+ "runDaemonJob denied, client is missing a required entitlement"
+ "search indexing progress reporting"
+ "shareContributorUserIdentifier"
+ "sl"
+ "snoozeUntilTime"
+ "sourceURL"
+ "spotlight searchable item: %{public}@ object of entity %{public}@ uuid: %{public}@ "
+ "system Leo deleteItems"
+ "system Leo donate and delete"
+ "system Leo donateItems"
+ "system Leo updateLexemesWithEntityScores"
+ "v16@?0@\"PLFeatureAvailability\"8"
+ "v24@?0@\"NSURL\"8@\"NSURL\"16"
+ "v32@?0@\"CPLScopedIdentifier\"8@\"CPLRecordChange\"16^B24"
+ "v32@?0@\"PLManagedObject\"8@\"CPLScopedIdentifier\"16@\"PLCollectionShare\"24"
+ "v48@?0Q8Q16Q24Q32Q40"
+ "workItemsNeedingProcessing(in:currentCriteria:)"
- "\t W: %@ C: %@ Cache hit: NO\n"
- "\t W: %@ C: %@ Cache hit: YES\n"
- "\n  %@ : %@"
- " PLAvalancheTypeAutoPicked"
- " PLAvalancheTypeNotInBurst"
- " PLAvalancheTypeNotPicked"
- " PLAvalancheTypeStack"
- " PLAvalancheTypeUnknown"
- " PLAvalancheTypeUserFavorite"
- " autoIdentifier=%@ autoSettings=%@"
- "%@ %@ cloudAssetGUIDs %@ album %@"
- "%@ %@[%@] -> %@"
- "%@ -- store %@ vs. plist %@"
- "%@ setting _shouldDeferTask to YES"
- "%@-GM"
- "%@: failed to find invitation GUIDs %@ to resend"
- "%K UTI-CONFORMS-TO %@"
- "%{public}@ -- failed to save %ld asset mappings for store %{public}@: %{public}@"
- "%{public}@ -- saved %ld asset mappings for store %{public}@"
- "%{public}@: PLManagedAsset = %{public}@, like count = %tu, PLCloudCommentsChangeNotification = %@"
- "+setCloudAlbumSharingEnabled %@"
- "-[PLBackgroundJobGuestAssetSyncWorker workItemsNeedingProcessingInLibrary:validCriterias:]"
- "-[PLBackgroundJobPersonSyncWorker workItemsNeedingProcessingInLibrary:validCriterias:]"
- "-[PLBackgroundJobService _inq_pendingJobsForBundle:workerTypes:validCriterias:]"
- "-[PLManagedAsset _generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:retryNumber:allowCancellationByService:clientBundleID:completion:]"
- "-[PLManagedAsset(Share) setupPlaceholderAssetWithRequiredPropertiesFromSourceAsset:placeholderAssetUUID:bundleScope:share:importSessionID:bakeInAdjustmentsFromSourceAsset:flattenLivePhoto:copyTitleDescriptionAndKeywords:copyCameraProcessingAdjustmentResources:copyProvenanceData:isCurrentUser:library:]"
- "-[PLManagedAssetRecoveryManager identifyAssetsWithInconsistentCloudState]"
- "-[PLNotificationManager noteDidReceiveCMMInvitationWithMomentShare:]"
- "-[PLNotificationManager noteDidReceiveInvitationForSharedAlbum:]"
- "-[PLNotificationManager noteInvitationRecordStatusChanged:fromOldState:mstreamdInfo:]"
- "-[PLNotificationManager noteMultipleContributorStatusChangedForAlbum:mstreamdInfo:]"
- "-[PLNotificationManager noteSharedAlbumUnseenStatusDidChange:]"
- "-[PLNotificationManager noteUserDidNavigateAwayFromSharedAlbum:photoLibrary:]"
- "-[PLRebuildJournalManager recreateAllObjectsInManagedObjectContext:options:]"
- "-[PLRebuildJournalManager recreateAllObjectsInManagedObjectContext:options:]_block_invoke"
- "-init unsupported, use one of the other initializers"
- "/private"
- "<%@ %p> "
- "<%@: %p> asset: %p, snapshot: %p"
- "<%@:%p adjustments=%@ masks=%@>"
- "<%@:%p identifer=%@ maskUUID=%@ enabled=%d settings=%@"
- "ActivityByOthers"
- "Archiving asset path to uuid mappings"
- "At least one bundle has more work to do, calling _inq_submitPendingJobsIfNecessary"
- "Attempting to initialize adjustment with nil identifier"
- "Attempting to initialize adjustment with nil settings"
- "B16@?0@\"PLBackgroundJobCriteria\"8"
- "B24@?0@\"PLManagedAsset\"8@\"NSDictionary\"16"
- "Bad adjustment data: expected dictionary, but got %{public}@"
- "Badging"
- "Batch deleted %@ cloud masters"
- "Batch updated %@ assets"
- "Batch updated %@ cloud masters"
- "Cannot generate %lu-grams from tokens %@"
- "Changes for entity: %@ are not tracked by Photos Search"
- "Checked all submitted library bundles. Result: %@"
- "Checked workers of library %@ for pending jobs. Result: %@"
- "Checking %@ of library %@ for pending jobs with signaled worker types: %@"
- "Checking all library bundles for pending jobs"
- "Class getPILongExposureFusionAutoCalculatorClass(void)_block_invoke"
- "Clearing key asset %{public}@ on CollectionShare %{public}@ per no-key scope change (local key asset is uploaded)"
- "Could not copy file from exported source: %@ to temporary location: %@, error: %@"
- "Could not create a directory for copying the exported source: %@. Error: %@"
- "Couldn't find container class for node: %@"
- "Creating path to uuid mappings for UUID recovery"
- "Creating sqlite error file before lightweight migration"
- "Creating sqlite error file for background Migration failure"
- "Creating sqlite error file for excessive persistent history size"
- "Creating sqlite error indicator file"
- "Deleting all cloud masters locally"
- "Detected search index rebuild in progress [%{public}@], start %{public}@ prev end %{public}@, entity: %{public}@, resume objectID: %{public}@ [%{public}@]"
- "Donating %tu items to Leo"
- "Donating %tu items to Leo managed store"
- "Dropping search index, source: %{public}@, reasons: %{public}@, for library %@, library identifier: %@"
- "EV0"
- "End index rebuild event: %{public}@"
- "Error fetching Cloud Resources for %@/%ld: %@"
- "EventLog"
- "FOLDER %@ [%d]\n"
- "FOLDER %@ [0 childCollections]\n"
- "Failed to batch  \u00a0\u00a0\u00a0assets: %@"
- "Failed to batch delete cloud masters: Error: %@"
- "Failed to batch update assets: %@"
- "Failed to batch update cloud masters: %@"
- "Failed to create identifier for library with path manager %@ %@."
- "Failed to create sqlite error file %@."
- "Failed to create sqlite error indicator file to guard against lightweight migration crash loop"
- "Failed to deserialize sqliteerror. Error: %@"
- "Failed to enforce the download-originals prefetch mode on the Visual Intelligence library: %@"
- "Failed to fetch nodes with error: %@"
- "Failed to fetch objectIDs of nodes with error: %@"
- "Failed to fetch path to uuid mappings %d %s"
- "Failed to open database for extracting path to uuid mappings"
- "Failed to write recovery metadata %@ to %@: %@"
- "Feed"
- "Fetch for grouped assets failed with error %@"
- "Fetch for media metadata failed: %@"
- "Finished donating %tu items and deleting %tu items in Leo managed store"
- "Found force rebuild indicator file, will not attempt lightweight migration"
- "HDR EV0"
- "HDR-10-bit-video"
- "HDR-high-or-extended-image"
- "HDR-map"
- "Identifying assets in inconsistent cloud state"
- "Ignoring exception %@"
- "Index rebuild paused"
- "Info.plist"
- "Invalid criteria found: %s"
- "Invitations"
- "Lemonade"
- "Library %@ does not have pending jobs"
- "LowPriorityBatterySearchIndexing"
- "LowPriorityChargerSearchIndexing"
- "Migration took %1.1fs"
- "Missing path to persist recovery metadata %@ for cloud shared album"
- "No CPL settings on CPL library open, skipping the Visual Intelligence prefetch mode check"
- "No further work at the current criteria and no other bundle records in processing set. Shutting down..."
- "No further work at the current criteria but processing set contains bundle records at other criteria. Entering Submitted state."
- "Not a dictionary"
- "Not generating CPLAssetChange for CollectionShare asset as FF is disabled %@"
- "Not pushing CollectionShare scope %@ as FF is disabled"
- "Notifications"
- "Notifications: Deleting notifications for multiple contributor status change for album: %@."
- "Notifications: Ignoring invitation status changed because we don't own the album %@."
- "Notifications: Ignoring invitation status changed since we are currently not accepting notification for album %@."
- "Notifications: Ignoring invitatitionRecordStatusChanged notification for album %@ and invitationRecord %@ beause it's not interesting as per mstreamd dictionary."
- "Notifications: Ignoring multiple status changed notification because we are not subscribed to this the album %@."
- "Notifications: Ignoring multipleContributorStatusChanged notification for album %@ beause it's not interesting as per mstreamd dictionary."
- "Notifications: Ignoring multipleContributorStatusChanged notification since we are currently not accepting notification for album %@."
- "Notifications: Ignoring placeholderKindChanged notification for album %@ beause it's not interesting as per mstreamd dictionary."
- "Notifications: Ignoring placeholderKindChanged notification since we are currently not accepting notification for album %@."
- "Notifications: Ignoring placeholderKindChanged notification since we own the album %@."
- "Notifications: MomentShare is inited by myself."
- "Notifications: MomentShare's invitor is NOT in my contacts."
- "Notifications: no sender email address."
- "Notifications: processing albumUnseenStatusDidChange \"%@\" (%@), unseen: %@"
- "PFAdjustmentErrorDomain"
- "PILongExposureFusionAutoCalculator"
- "PL-PILongExposureFusionAutoCalculator"
- "PLCloudCommentsDidChangeNotification"
- "PLCloudFeedEntriesDidChangeNotification"
- "PLGraphNodeContainer.m"
- "PLInvitationRecordsDidChangeNotification"
- "PLPhotoLibraryShouldReload"
- "PLPhotosHighlightCurationTypeExtended"
- "PLPhotosHighlightCurationTypeNone"
- "PLPhotosHighlightCurationTypeSummary"
- "PLRebuildUserNotification snooze for %tu hour(s) until %@"
- "PLRebuildUserNotificationSnoozeLastMessageKey"
- "PLRebuildUserNotificationSnoozeUntilTime"
- "PLSearchHomeItemTypeDate"
- "PLSearchHomeItemTypeHoliday"
- "PLSearchHomeItemTypeHome"
- "PLSearchHomeItemTypeMeaning"
- "PLSearchHomeItemTypePerson"
- "PLSearchHomeItemTypePlace"
- "PLSearchHomeItemTypeScene"
- "PLSearchHomeItemTypeSeason"
- "PLSearchHomeItemTypeSocialGroup"
- "PLSpotlightQueryUtilities.m"
- "Paused search index rebuild"
- "Photos cannot proceed with the library in its current state.\n\n%@\n\nSelect \"Rebuild\" to allow rebuild of the photo library database (possible data loss) or \"Not now\" to stop now and leave it as-is"
- "PhotosIDExtraction"
- "Preparing to rebuild search index for library: %@"
- "Preserving not-yet-pushed key asset %{public}@ on CollectionShare %{public}@ against no-key scope change"
- "Rebuild in progress, but required rebuild type is %{public}@"
- "Rebuild preparation complete, starting reindexing, rebuild type: %{public}@, reasons: %{public}@, called by: %{public}@"
- "Remaining count for search indexing entity %{public}@: %tu"
- "Remaining search indexing work, rebuild: %tu, incremental: %tu isPaused: %{public}@"
- "Removing migration indicator file"
- "Resetting cloudLocalState of assets"
- "Resetting cloudLocalState of cloud masters"
- "Resetting uploadAttempts of assets"
- "Resuming search index rebuild from entity: %{public}@ token: %{public}@ for library %@"
- "Resuming search index rebuild, called by: %{public}@"
- "SELECT zdirectory, zfilename, zuuid FROM zasset;"
- "SUBQUERY(%K, $resource, $resource.%K == %d AND ($resource.%K IN %@) AND $resource.%K >= %d AND $resource.%K == %d).@count > 0"
- "Search index rebuild completed for library %@"
- "SearchUIImprovements"
- "Set prefetch mode requires cloud sync enabled"
- "Should NOT show PLRebuildUserNotification because of snooze until %@"
- "Skipping exported item of unexpected class: %{public}@"
- "Start index rebuild event: %{public}@"
- "System leo delete items failed with error: %@"
- "System leo donate items failed with error: %@"
- "System leo store is nil, possible force close during indexing"
- "System leo update lexemes with entity scores failed with error: %@"
- "Trying to persist path->uuid mapping"
- "Unable to get attributes for %@: %@"
- "Unable to register PLPhotoLibrary with bundle %@"
- "User did change status for moment share: %{public}@"
- "User did navigate away from all shared albums"
- "User did navigate away from shared album: %{public}@"
- "User did navigate into picker shared album: %{public}@"
- "User did navigate into shared album: %{public}@"
- "User did read comments on asset: %{public}@"
- "UtilityIntelligence"
- "Workers that reported pending jobs on well known library identifier %@:\n"
- "[ERROR] Could not create unarchiver for revGeoLocationData with error:%@"
- "[RM] %@ Deferred finalization resource exists but proxy is missing, promoting to original. resource: %{public}@, asset: %{public}@, path: %{public}@"
- "[RM] %{public}@ Proxy file does not exist but deferred finalization resource does exist, will attempt to promote existing file at %{public}@"
- "[Search Logger]: Failed to obtain library identifier for library : %{public}@"
- "[Search Logger]: Library identifier for library : [%{public}@ : %{public}@]"
- "[resource] %{public}@ did not receive video complement file url from provider, error: %@"
- "[resource] error copying file to url: %@, error: %@"
- "[resource] failed to copy primary resource for identifier: %{public}@ from url: %@ to url: %@, error: %@"
- "[resource] failed to copy secondary resource for identifier: %{public}@ from url: %@ to url: %@, error: %@"
- "[resource] file already exists at url: %@"
- "[resource] read inode at url: %@, %lu"
- "_isOverloaded=%i"
- "actual"
- "addAssetWithURLs: forcing uuid: %{public}@ for master URL: %{public}@"
- "addAssetWithURLs: unable to find uuid for master URL: %{public}@"
- "additionalAttributes.cameraCaptureDevice"
- "additionalAttributes.personReferences"
- "album-id"
- "albumGUID == %@"
- "all workers"
- "allAlbumsMetadataDump.plist"
- "asset containment failed: no library"
- "assetUuid in %@"
- "bindToPhotoLibraryURL WILL FAIL for well known library %td because client '%@' (%d) is missing the photos data vault entitlement \"com.apple.private.security.storage.PhotosLibraries\""
- "byContentFTSv2"
- "can't find LeoLexeme entity"
- "can't find content property"
- "cloudGUID in %@"
- "cloudMaster.assets CONTAINS %@"
- "cloudOwnerEmail"
- "cloudOwnerFirstName"
- "cloudOwnerLastName"
- "cloudPublicURLEnabled"
- "cloudRelationshipState"
- "cloudSubscriptionDate"
- "criteriaNeedingProcessing(in:validCriterias:outSignalAgainDate:)"
- "current"
- "deleted=%@"
- "dictionary"
- "envelope must not be nil"
- "errors"
- "exception"
- "expected"
- "found plAlbum %@ with invitationRecords %lu"
- "groupingUUID == %@"
- "input"
- "inserted=%@"
- "invitation record %@"
- "isValid"
- "itemIdentifier IN %@ AND type = %d"
- "leo donate and delete"
- "leo donate and delete in managed photos store"
- "library.libraryServicesManager != nil"
- "locationInfo"
- "maskUUID"
- "mediaGroupUUID = %@ AND noindex:(kind) = %d"
- "momentShares.count"
- "noindex(isLocallyAvailable) == NO"
- "noindex(type) in %@"
- "notifications"
- "parameter"
- "photo-stream"
- "photos-event"
- "placeAnnotation"
- "processingSetUrl"
- "publicURL"
- "sb"
- "search: %{public}@ object of entity %{public}@ uuid: %{public}@ "
- "search: donation for asset %{public}@ with property sets %{public}@ isUpdate: %{public}@"
- "show-album"
- "show-import"
- "skipping updateWithMSASRelationship for owner participant with personID: %@"
- "some workers"
- "state information archive for %@ too large"
- "system leo deleteItems"
- "system leo donateItems"
- "system leo updateLexemesWithEntityScores"
- "uicmd"
- "unable to archive process state information for %@: %@"
- "updateCloudSharedAlbumMultipleContributorsStateOnServer:(%@ guid %@ requestedEnabledValue %i previousEnabledValue %i)"
- "updateCloudSharedAlbumPublicURLStateOnServer:(%@ guid %@ requestedEnabledValue %i previousEnabledValue %i)"
- "updated=%@"
- "v32@?0@\"PLNotification\"8Q16^B24"
- "v40@?0@\"AVAsset\"8@\"AVAudioMix\"16@\"AVVideoComposition\"24@\"NSError\"32"
- "will call -[PLCloudSharedDeleteAlbumsJob deleteLocalAlbumsForMSASAlbumGUIDs:albumGUIDs:] with arguments %@"
- "workItemsNeedingProcessing(in:validCriterias:)"
- "{PLConcurrencyLimiterRecordingAggregateEntry=IIIIQQQQ[8C]}"
```
