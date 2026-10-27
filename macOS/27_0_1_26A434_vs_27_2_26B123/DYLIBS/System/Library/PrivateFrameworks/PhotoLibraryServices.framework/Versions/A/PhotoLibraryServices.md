## PhotoLibraryServices

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/Versions/A/PhotoLibraryServices`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0x7b700c
-  __TEXT.__objc_methlist: 0x454bc
-  __TEXT.__const: 0x7548
-  __TEXT.__dlopen_cstrs: 0x783
+916.58.114.0.0
+  __TEXT.__text: 0x7af2e8
+  __TEXT.__objc_methlist: 0x44bdc
+  __TEXT.__const: 0x73c8
+  __TEXT.__dlopen_cstrs: 0x716
   __TEXT.__swift5_typeref: 0x131a
-  __TEXT.__cstring: 0x6bfe7
+  __TEXT.__cstring: 0x6be65
   __TEXT.__swift5_capture: 0x188c
   __TEXT.__constg_swiftt: 0x400
   __TEXT.__swift5_builtin: 0xc8

   __TEXT.__swift5_assocty: 0xd8
   __TEXT.__swift5_proto: 0xa4
   __TEXT.__swift5_types: 0x54
-  __TEXT.__oslogstring: 0x8350c
+  __TEXT.__oslogstring: 0x84099
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__gcc_except_tab: 0x1fe3c
+  __TEXT.__gcc_except_tab: 0x1fe38
   __TEXT.__ustring: 0xa3a
-  __TEXT.__unwind_info: 0x16708
-  __TEXT.__eh_frame: 0x11e0
+  __TEXT.__unwind_info: 0x164f8
+  __TEXT.__eh_frame: 0x11c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6820
-  __DATA_CONST.__objc_classlist: 0x23d0
+  __DATA_CONST.__const: 0x6628
+  __DATA_CONST.__objc_classlist: 0x23b0
   __DATA_CONST.__objc_catlist: 0xf8
-  __DATA_CONST.__objc_protolist: 0x730
+  __DATA_CONST.__objc_protolist: 0x738
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x24d48
+  __DATA_CONST.__objc_selrefs: 0x248a0
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0x1540
-  __DATA_CONST.__objc_arraydata: 0x1ea0
-  __DATA_CONST.__got: 0x5158
-  __AUTH_CONST.__const: 0x1d2b0
-  __AUTH_CONST.__cfstring: 0x52da0
-  __AUTH_CONST.__objc_const: 0x6f938
+  __DATA_CONST.__objc_superrefs: 0x1538
+  __DATA_CONST.__objc_arraydata: 0x1ea8
+  __DATA_CONST.__got: 0x5138
+  __AUTH_CONST.__const: 0x1d190
+  __AUTH_CONST.__cfstring: 0x525a0
+  __AUTH_CONST.__objc_const: 0x6f958
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__objc_intobj: 0x5568
-  __AUTH_CONST.__objc_arrayobj: 0x15a8
-  __AUTH_CONST.__objc_doubleobj: 0x180
+  __AUTH_CONST.__objc_intobj: 0x55e0
+  __AUTH_CONST.__objc_arrayobj: 0x1590
+  __AUTH_CONST.__objc_doubleobj: 0x190
   __AUTH_CONST.__objc_dictobj: 0x320
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH_CONST.__auth_got: 0x2868
+  __AUTH_CONST.__auth_got: 0x2898
   __AUTH_CONST.__auth_ptr: 0x2c8
-  __AUTH.__objc_data: 0xc828
+  __AUTH.__objc_data: 0xc648
   __AUTH.__data: 0x300
-  __DATA.__objc_ivar: 0x3da8
-  __DATA.__data: 0x6dc0
-  __DATA.__bss: 0x34c8
+  __DATA.__objc_ivar: 0x3da4
+  __DATA.__data: 0x6dd0
+  __DATA.__bss: 0x34a8
   __DATA.__common: 0x4
-  __DATA_DIRTY.__objc_data: 0xa078
+  __DATA_DIRTY.__objc_data: 0xa118
   __DATA_DIRTY.__data: 0xd8
   __DATA_DIRTY.__crash_info: 0x148
-  __DATA_DIRTY.__bss: 0x690
+  __DATA_DIRTY.__bss: 0x648
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 29443
-  Symbols:   64748
-  CStrings:  21659
+  Functions: 29166
+  Symbols:   64400
+  CStrings:  21596
 
Symbols:
+ +[PLAssetsdResourceService(Testing) pl_openRegularFileForClientAtPath:libraryRootURL:isSystemLibrary:auditToken:]
+ +[PLBackgroundJobHighPrioritySearchIndexingWorker _allCriteriaToUse]
+ +[PLBackgroundJobLowPrioritySearchIndexingWorker _allCriteriaToUse]
+ +[PLBackgroundJobLowPrioritySearchIndexingWorker optOutOfPendingWorkCache]
+ +[PLBackgroundJobSearchIndexingWorker _allCriteriaToUse]
+ +[PLBackgroundJobWorkerTypes backgroundJobWorkerTypesMaskGuestAssetSync:personSync:syndicationSync:syndicationResourceSanitization:syndicationResourceDownload:syndicationAssetCleanup:assetStack:duplicateDetector:deferredRenderDerivativesLowPriority:deferredRenderDerivativesHighPriority:resourceAvailability:stableHash:editRenderingImage:editRenderingVideo:highPrioritySearchIndexing:lowPrioritySearchIndexing:sharedAssetContainerUpdate:assetResourceUploadJob:assetResourceUploadExtensionRunner:featureAvailability:optimizeTableThumbs:cascadeDonation:provenanceTimestamp:]
+ +[PLBackgroundModelMigration skipAllBackgroundActionsForNewlyCreatedLibraryIfNeededWithPathManager:error:]
+ +[PLBiomeDonations donateDeleteEventForAssetCreationDateByAssetUUID:]
+ +[PLCascadeUtilities _handleSuggestionsPreferenceChanged]
+ +[PLCascadeUtilities _siriExclusionNotificationName]
+ +[PLCollectionShare _allAssetsAreSavedToLibraryForCollectionShare:inContext:]
+ +[PLCollectionShare countOfSharesWithUnreadBadgeActivitySinceLastSeenDate:eventLogDate:inManagedObjectContext:]
+ +[PLCollectionShare predicateForMigratedCPLCollectionShares]
+ +[PLFeatureAvailabilityLexemeCriteria featureAnalysisLexemeCategories]
+ +[PLFileBackedThumbnailVirtualResource estimatedMasterThumbnailDataLengthForAssetWidth:height:]
+ +[PLImageWriter copyJobContentsToHoldingDirectoryWithUUID:incomingPath:job:]
+ +[PLLimitedLibraryFetchFilter migrateLimitedLibraryFetchFilterFromApplicationIdentifier:toApplicationIdentifier:inManagedObjectContext:error:]
+ +[PLManagedAsset(Share) _cloneResourcesForSharePlaceholderAsset:sourceAsset:shouldBakeInAdjustments:shouldFlattenLivePhoto:withPlaceholderResourceURLToSourceResourceURLMap:fileManager:photoLibrary:]
+ +[PLPhotoLibraryBundleController _formatMemoryBytes:]
+ +[PLSearchEntity confidenceForMomentEdge:]
+ +[PLSearchOCRUtilities _ocrTextLineCandidatesFromTextBlockObservation:tokenizer:includeLowConfidenceText:confidenceThreshold:]
+ +[PLSearchOCRUtilities _ocrTextLinesFromDocumentObservation:includeLowConfidenceText:confidenceThreshold:]
+ +[PLSearchOCRUtilities ocrTextLinesFromDocumentObservation:confidenceThreshold:]
+ +[PLSearchOCRUtilities ocrTextLinesFromDocumentObservation:includeLowConfidenceText:]
+ +[PLShareParticipant _enumerateUnattributedCPLContributorContentInPhotoLibrary:usingBlock:]
+ +[PLShareParticipant _objectsMatchingPredicate:entityName:inManagedObjectContext:]
+ +[PLShareParticipant linkCPLContributorContentWithUserIdentifiers:inPhotoLibrary:]
+ +[PLShareParticipant orphanedCPLContributorRecordsInPhotoLibrary:]
+ +[PLSharePost identifiersForMissingPostsInPhotoLibrary:]
+ +[PLSharePost predicateForPostsFromOthersCreatedAfterSubscriptionSinceDate:]
+ +[PLSharePost predicateToExcludePostsWithoutAssets]
+ +[PLSharePost restoreMissingPostsWithCPLRecords:inPhotoLibrary:]
+ +[PLSyndicationResourceDataStore _copyProvidedFilesForItemIdentifier:providerURL:primaryDestination:videoComplementDestination:pathManager:materializesDatalessFiles:resultHandler:]
+ +[PLSyndicationResourceDataStore _provideSourceURLsForBundleID:syndicationIdentifier:typeIdentifier:isLivePhoto:options:completionHandler:]
+ +[PLSyndicationResourceDataStore provideFileURLAndUnwrapLivePhotoIfNeededForItemIdentifiersWithBundleIDs:destURLs:pathManager:options:resultHandler:completionHandler:]
+ +[PLSyndicationResourceFileCoordinator _errorForCopyFailure:sourceURL:]
+ +[PLSyndicationResourceFileCoordinator _unpackLivePhotoBundleAtURL:primaryURL:videoComplementURL:error:]
+ +[PLVirtualResource estimatedJPEGThumbnailDataLengthForWidth:height:]
+ -[PLAbstractLibraryServicesManagerService isAuthorizedAssetUUID:inManagedObjectContext:]
+ -[PLAssetsdCloudInternalService updateAccessRequestForParticipantWithUUID:toAcceptanceStatus:inCollectionShareWithIdentifier:reply:]
+ -[PLAssetsdLibraryInternalService getSearchDonationProgressShouldCompute:shouldReport:reply:]
+ -[PLAssetsdLibraryInternalService migrateLimitedLibraryAccessFromApplication:toApplication:completionHandler:]
+ -[PLAssetsdLibraryInternalService transferAssetsWithUuids:fromLibraryURL:transferOptions:reply:]
+ -[PLAssetsdLibraryInternalService transferPersonsWithUuids:fromLibraryURL:transferOptions:reply:]
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
+ -[PLCloudPhotoLibraryManager _deactivateCPLSyncWithResetMode:reason:willBecomeNonSyncable:]
+ -[PLCloudPhotoLibraryManager _disableACPLAfterMainScopeWipedInCloudIfNecessaryWithStatus:transaction:]
+ -[PLCloudPhotoLibraryManager _linkOrphanedCollectionShareContributorsWithCPLSettings:]
+ -[PLCloudPhotoLibraryManager _restoreMissingCollectionSharePostsWithCPLSettings:]
+ -[PLCloudSharedComment _updateShareParticipantWithContributorUserIdentifier:collectionShare:inPhotoLibrary:]
+ -[PLCloudSharedComment updateCommentText:]
+ -[PLCollectionShare updateAccessRequestForShareParticipantUUID:toAcceptanceStatus:photoLibrary:completionHandler:]
+ -[PLCollectionShareCPLBackend _cplParticipantForParticipant:inScopeChange:collectionShare:]
+ -[PLCollectionShareCPLBackend updateAccessRequestForParticipant:toAcceptanceStatus:collectionShare:completionHandler:]
+ -[PLCollectionShareSharedStreamBackend updateAccessRequestForParticipant:toAcceptanceStatus:collectionShare:completionHandler:]
+ -[PLDelayedSaveActions _popBiomeDeletedAssetsIntoDetail:]
+ -[PLDelayedSaveActions recordAssetForBiomeDelete:]
+ -[PLDelayedSaveActionsDetail biomeDeletedAssetCreationDateByAssetUUID]
+ -[PLDelayedSaveActionsDetail setBiomeDeletedAssetCreationDateByAssetUUID:]
+ -[PLDelayedSaveActionsProcessor _processDelayedAssetsForBiomeDelete:]
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
+ -[PLManagedAsset(CPL) scopedIdentifierWithScopeIdentifier:]
+ -[PLManagedAsset(Share) setupPlaceholderAssetWithRequiredPropertiesFromSourceAsset:placeholderAssetUUID:bundleScope:share:importSessionID:bakeInAdjustmentsFromSourceAsset:flattenLivePhoto:copyTitleDescriptionAndKeywords:copyCameraProcessingAdjustmentResources:copyLocationData:copyProvenanceData:isCurrentUser:library:]
+ -[PLManagedObjectPagingIterator countRemainingWithManagedObjectContext:]
+ -[PLMediaMetadataVirtualResource .cxx_destruct]
+ -[PLMediaMetadataVirtualResource data]
+ -[PLMediaMetadataVirtualResource initWithAsset:resourceType:version:recipeID:data:mediaMetadataType:]
+ -[PLMediaMetadataVirtualResource mediaMetadataType]
+ -[PLModelMigrationAction_FixComputeSyncResourceFileExtension _path:isContainedWithinLibraryBundle:]
+ -[PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing performActionWithManagedObjectContext:error:]
+ -[PLModelMigrationAction_ReevaluateAllowedForAnalysisForUnknownKindAssets performActionWithManagedObjectContext:error:]
+ -[PLModelMigrationAction_ResetLocalAvailabilityRetryStateForDeferredProcessingFinalResources performActionWithManagedObjectContext:error:]
+ -[PLModelMigrationAction_SetKeepOriginalsPrefetchModeForVisualIntelligenceLibrary performActionWithManagedObjectContext:error:]
+ -[PLModelMigrationAction_SetRunOnceFlagToLinkOrphanedCollectionShareContributors performActionWithManagedObjectContext:error:]
+ -[PLModelMigrationAction_SetRunOnceFlagToRestoreMissingCollectionSharePosts performActionWithManagedObjectContext:error:]
+ -[PLModelMigrator _participatesInOTARestore]
+ -[PLNotificationManager kvsListenerDidUpdateEventLogLastEnteredDate:]
+ -[PLNotificationManager kvsListenerDidUpdateLastSeenDate:]
+ -[PLNotificationManager kvsListener]
+ -[PLNotificationManager setKvsListener:]
+ -[PLPhotoAnalysisServiceClient(Vision) cancelVisionOperationWithId:]
+ -[PLPhotoLibrary isMomentLibrary]
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
+ -[PLSearchIndexingEngineLibraryServicesProvider availabilityComputer]
+ -[PLSearchIndexingRebuildEngine _inq_performRebuildForLibrary:completion:]
+ -[PLSearchIndexingRebuildEngine logger]
+ -[PLSearchOCRTextLineCandidate initWithLine:words:confidence:isLowConfidence:]
+ -[PLSearchOCRTextLineCandidate isLowConfidence]
+ -[PLShare _cplParticipantsWithBlockedIdentitiesLast:]
+ -[PLShareParticipant _objectsMatchingPredicate:entityName:]
+ -[PLShareParticipant reconcileOrphanedRelationshipsWithCPLCollectionShare:]
+ -[PLSharePost linkAssets:]
+ -[PLSharePost setShare:]
+ -[PLSharePost updateCaption:]
+ -[PLSharePost updatePostAssetsInPhotoLibrary:]
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
+ GCC_except_table10018
+ GCC_except_table10027
+ GCC_except_table10044
+ GCC_except_table10051
+ GCC_except_table10065
+ GCC_except_table10079
+ GCC_except_table10138
+ GCC_except_table10158
+ GCC_except_table10172
+ GCC_except_table10176
+ GCC_except_table10188
+ GCC_except_table10200
+ GCC_except_table10212
+ GCC_except_table10214
+ GCC_except_table10228
+ GCC_except_table10230
+ GCC_except_table10237
+ GCC_except_table10245
+ GCC_except_table10270
+ GCC_except_table10290
+ GCC_except_table10298
+ GCC_except_table10310
+ GCC_except_table10321
+ GCC_except_table10348
+ GCC_except_table1035
+ GCC_except_table10350
+ GCC_except_table10363
+ GCC_except_table10374
+ GCC_except_table10449
+ GCC_except_table10453
+ GCC_except_table10457
+ GCC_except_table10459
+ GCC_except_table10465
+ GCC_except_table10469
+ GCC_except_table10477
+ GCC_except_table10506
+ GCC_except_table10513
+ GCC_except_table10533
+ GCC_except_table10564
+ GCC_except_table10567
+ GCC_except_table1061
+ GCC_except_table10619
+ GCC_except_table1062
+ GCC_except_table10670
+ GCC_except_table10682
+ GCC_except_table10684
+ GCC_except_table10704
+ GCC_except_table10706
+ GCC_except_table10717
+ GCC_except_table10722
+ GCC_except_table10727
+ GCC_except_table10733
+ GCC_except_table10752
+ GCC_except_table10882
+ GCC_except_table10925
+ GCC_except_table11006
+ GCC_except_table11007
+ GCC_except_table11010
+ GCC_except_table11011
+ GCC_except_table11014
+ GCC_except_table11015
+ GCC_except_table11017
+ GCC_except_table11023
+ GCC_except_table11027
+ GCC_except_table11029
+ GCC_except_table11031
+ GCC_except_table11033
+ GCC_except_table11035
+ GCC_except_table11037
+ GCC_except_table11039
+ GCC_except_table11041
+ GCC_except_table11043
+ GCC_except_table11045
+ GCC_except_table11047
+ GCC_except_table11049
+ GCC_except_table11052
+ GCC_except_table11055
+ GCC_except_table11059
+ GCC_except_table11062
+ GCC_except_table11065
+ GCC_except_table11067
+ GCC_except_table11069
+ GCC_except_table11071
+ GCC_except_table11073
+ GCC_except_table11075
+ GCC_except_table11076
+ GCC_except_table11079
+ GCC_except_table11082
+ GCC_except_table11085
+ GCC_except_table11088
+ GCC_except_table11090
+ GCC_except_table11093
+ GCC_except_table11096
+ GCC_except_table11099
+ GCC_except_table11100
+ GCC_except_table11104
+ GCC_except_table11109
+ GCC_except_table11110
+ GCC_except_table11112
+ GCC_except_table11113
+ GCC_except_table11114
+ GCC_except_table11115
+ GCC_except_table11116
+ GCC_except_table11117
+ GCC_except_table11118
+ GCC_except_table11119
+ GCC_except_table11121
+ GCC_except_table11122
+ GCC_except_table11123
+ GCC_except_table11127
+ GCC_except_table11128
+ GCC_except_table11137
+ GCC_except_table11139
+ GCC_except_table11141
+ GCC_except_table11143
+ GCC_except_table11147
+ GCC_except_table11149
+ GCC_except_table1120
+ GCC_except_table11219
+ GCC_except_table11223
+ GCC_except_table11305
+ GCC_except_table11377
+ GCC_except_table1141
+ GCC_except_table11418
+ GCC_except_table11430
+ GCC_except_table11528
+ GCC_except_table11533
+ GCC_except_table11556
+ GCC_except_table11610
+ GCC_except_table11666
+ GCC_except_table11727
+ GCC_except_table11880
+ GCC_except_table11921
+ GCC_except_table1199
+ GCC_except_table120
+ GCC_except_table12152
+ GCC_except_table12185
+ GCC_except_table12209
+ GCC_except_table12210
+ GCC_except_table12211
+ GCC_except_table12212
+ GCC_except_table12213
+ GCC_except_table12214
+ GCC_except_table12216
+ GCC_except_table12218
+ GCC_except_table1222
+ GCC_except_table12233
+ GCC_except_table1228
+ GCC_except_table1229
+ GCC_except_table12313
+ GCC_except_table12325
+ GCC_except_table12331
+ GCC_except_table12341
+ GCC_except_table12346
+ GCC_except_table12350
+ GCC_except_table12354
+ GCC_except_table12364
+ GCC_except_table12374
+ GCC_except_table12379
+ GCC_except_table12384
+ GCC_except_table12389
+ GCC_except_table1239
+ GCC_except_table12394
+ GCC_except_table12399
+ GCC_except_table12405
+ GCC_except_table12415
+ GCC_except_table12418
+ GCC_except_table12429
+ GCC_except_table12433
+ GCC_except_table12444
+ GCC_except_table1246
+ GCC_except_table12462
+ GCC_except_table12478
+ GCC_except_table12530
+ GCC_except_table12535
+ GCC_except_table12538
+ GCC_except_table12541
+ GCC_except_table12545
+ GCC_except_table12547
+ GCC_except_table12549
+ GCC_except_table12551
+ GCC_except_table12553
+ GCC_except_table12555
+ GCC_except_table12560
+ GCC_except_table12562
+ GCC_except_table12571
+ GCC_except_table12580
+ GCC_except_table12583
+ GCC_except_table12587
+ GCC_except_table12592
+ GCC_except_table12598
+ GCC_except_table12602
+ GCC_except_table12616
+ GCC_except_table12618
+ GCC_except_table12620
+ GCC_except_table12638
+ GCC_except_table12640
+ GCC_except_table12642
+ GCC_except_table12644
+ GCC_except_table12647
+ GCC_except_table12649
+ GCC_except_table1265
+ GCC_except_table12651
+ GCC_except_table12653
+ GCC_except_table12655
+ GCC_except_table1266
+ GCC_except_table12661
+ GCC_except_table12665
+ GCC_except_table12667
+ GCC_except_table12672
+ GCC_except_table12674
+ GCC_except_table12676
+ GCC_except_table12678
+ GCC_except_table12680
+ GCC_except_table12692
+ GCC_except_table12698
+ GCC_except_table12724
+ GCC_except_table12728
+ GCC_except_table12729
+ GCC_except_table12737
+ GCC_except_table1274
+ GCC_except_table12767
+ GCC_except_table12796
+ GCC_except_table128
+ GCC_except_table12886
+ GCC_except_table1296
+ GCC_except_table13001
+ GCC_except_table13003
+ GCC_except_table13007
+ GCC_except_table13025
+ GCC_except_table13029
+ GCC_except_table13036
+ GCC_except_table13042
+ GCC_except_table13053
+ GCC_except_table13058
+ GCC_except_table13137
+ GCC_except_table1314
+ GCC_except_table13153
+ GCC_except_table13158
+ GCC_except_table13162
+ GCC_except_table13179
+ GCC_except_table13181
+ GCC_except_table13188
+ GCC_except_table13190
+ GCC_except_table13192
+ GCC_except_table13197
+ GCC_except_table13241
+ GCC_except_table13250
+ GCC_except_table13256
+ GCC_except_table13258
+ GCC_except_table13260
+ GCC_except_table13303
+ GCC_except_table13416
+ GCC_except_table13437
+ GCC_except_table13444
+ GCC_except_table13448
+ GCC_except_table13495
+ GCC_except_table1351
+ GCC_except_table13580
+ GCC_except_table13586
+ GCC_except_table13605
+ GCC_except_table13617
+ GCC_except_table1366
+ GCC_except_table13669
+ GCC_except_table13679
+ GCC_except_table13700
+ GCC_except_table13703
+ GCC_except_table13707
+ GCC_except_table13710
+ GCC_except_table13716
+ GCC_except_table13719
+ GCC_except_table13728
+ GCC_except_table1373
+ GCC_except_table13777
+ GCC_except_table13795
+ GCC_except_table1380
+ GCC_except_table13801
+ GCC_except_table1382
+ GCC_except_table13823
+ GCC_except_table139
+ GCC_except_table13917
+ GCC_except_table1397
+ GCC_except_table13971
+ GCC_except_table13983
+ GCC_except_table13987
+ GCC_except_table14003
+ GCC_except_table14012
+ GCC_except_table14032
+ GCC_except_table14042
+ GCC_except_table14044
+ GCC_except_table14046
+ GCC_except_table14064
+ GCC_except_table14160
+ GCC_except_table14183
+ GCC_except_table14196
+ GCC_except_table14198
+ GCC_except_table14200
+ GCC_except_table14308
+ GCC_except_table14309
+ GCC_except_table14313
+ GCC_except_table14345
+ GCC_except_table14366
+ GCC_except_table14377
+ GCC_except_table14378
+ GCC_except_table14379
+ GCC_except_table14380
+ GCC_except_table14381
+ GCC_except_table14382
+ GCC_except_table14383
+ GCC_except_table14384
+ GCC_except_table14385
+ GCC_except_table14386
+ GCC_except_table14387
+ GCC_except_table14388
+ GCC_except_table14389
+ GCC_except_table14390
+ GCC_except_table14394
+ GCC_except_table14398
+ GCC_except_table1441
+ GCC_except_table14453
+ GCC_except_table14459
+ GCC_except_table14479
+ GCC_except_table14484
+ GCC_except_table14489
+ GCC_except_table14493
+ GCC_except_table14527
+ GCC_except_table14531
+ GCC_except_table14535
+ GCC_except_table14542
+ GCC_except_table14546
+ GCC_except_table14557
+ GCC_except_table14593
+ GCC_except_table14644
+ GCC_except_table14647
+ GCC_except_table14651
+ GCC_except_table14725
+ GCC_except_table14749
+ GCC_except_table1481
+ GCC_except_table1483
+ GCC_except_table14905
+ GCC_except_table1492
+ GCC_except_table1494
+ GCC_except_table14986
+ GCC_except_table1502
+ GCC_except_table15046
+ GCC_except_table15063
+ GCC_except_table15070
+ GCC_except_table15073
+ GCC_except_table15074
+ GCC_except_table15093
+ GCC_except_table15182
+ GCC_except_table15191
+ GCC_except_table15192
+ GCC_except_table15195
+ GCC_except_table15197
+ GCC_except_table15204
+ GCC_except_table1532
+ GCC_except_table15381
+ GCC_except_table1540
+ GCC_except_table15460
+ GCC_except_table15542
+ GCC_except_table1560
+ GCC_except_table15638
+ GCC_except_table15639
+ GCC_except_table15646
+ GCC_except_table15648
+ GCC_except_table15653
+ GCC_except_table15661
+ GCC_except_table15663
+ GCC_except_table15689
+ GCC_except_table1570
+ GCC_except_table15708
+ GCC_except_table15719
+ GCC_except_table1574
+ GCC_except_table15744
+ GCC_except_table15784
+ GCC_except_table15788
+ GCC_except_table15789
+ GCC_except_table15855
+ GCC_except_table15859
+ GCC_except_table15863
+ GCC_except_table15868
+ GCC_except_table16024
+ GCC_except_table16054
+ GCC_except_table16071
+ GCC_except_table16076
+ GCC_except_table16079
+ GCC_except_table16081
+ GCC_except_table16086
+ GCC_except_table16087
+ GCC_except_table16092
+ GCC_except_table16093
+ GCC_except_table16095
+ GCC_except_table16106
+ GCC_except_table16110
+ GCC_except_table16112
+ GCC_except_table16113
+ GCC_except_table16117
+ GCC_except_table16119
+ GCC_except_table16121
+ GCC_except_table16123
+ GCC_except_table16126
+ GCC_except_table16129
+ GCC_except_table1615
+ GCC_except_table16181
+ GCC_except_table16196
+ GCC_except_table16199
+ GCC_except_table16216
+ GCC_except_table16220
+ GCC_except_table16225
+ GCC_except_table16230
+ GCC_except_table16233
+ GCC_except_table16235
+ GCC_except_table16246
+ GCC_except_table16347
+ GCC_except_table16351
+ GCC_except_table16374
+ GCC_except_table16375
+ GCC_except_table16382
+ GCC_except_table16391
+ GCC_except_table16400
+ GCC_except_table16405
+ GCC_except_table16409
+ GCC_except_table16422
+ GCC_except_table16481
+ GCC_except_table16483
+ GCC_except_table1661
+ GCC_except_table16634
+ GCC_except_table16649
+ GCC_except_table1674
+ GCC_except_table16756
+ GCC_except_table16777
+ GCC_except_table16783
+ GCC_except_table16788
+ GCC_except_table16796
+ GCC_except_table16825
+ GCC_except_table16833
+ GCC_except_table1685
+ GCC_except_table16877
+ GCC_except_table16940
+ GCC_except_table16945
+ GCC_except_table16953
+ GCC_except_table16963
+ GCC_except_table16975
+ GCC_except_table16989
+ GCC_except_table16995
+ GCC_except_table17005
+ GCC_except_table17018
+ GCC_except_table17028
+ GCC_except_table17038
+ GCC_except_table17068
+ GCC_except_table17072
+ GCC_except_table17076
+ GCC_except_table17137
+ GCC_except_table17140
+ GCC_except_table17187
+ GCC_except_table17198
+ GCC_except_table17218
+ GCC_except_table17225
+ GCC_except_table17229
+ GCC_except_table17291
+ GCC_except_table17301
+ GCC_except_table17313
+ GCC_except_table17314
+ GCC_except_table17318
+ GCC_except_table17321
+ GCC_except_table17325
+ GCC_except_table17328
+ GCC_except_table17329
+ GCC_except_table17330
+ GCC_except_table17331
+ GCC_except_table17332
+ GCC_except_table17371
+ GCC_except_table17442
+ GCC_except_table17456
+ GCC_except_table17507
+ GCC_except_table17525
+ GCC_except_table17565
+ GCC_except_table17570
+ GCC_except_table17609
+ GCC_except_table17621
+ GCC_except_table17624
+ GCC_except_table17636
+ GCC_except_table17661
+ GCC_except_table17692
+ GCC_except_table17693
+ GCC_except_table17694
+ GCC_except_table17728
+ GCC_except_table17741
+ GCC_except_table17782
+ GCC_except_table17789
+ GCC_except_table17793
+ GCC_except_table17810
+ GCC_except_table17827
+ GCC_except_table17846
+ GCC_except_table17947
+ GCC_except_table17972
+ GCC_except_table17974
+ GCC_except_table17976
+ GCC_except_table17980
+ GCC_except_table17986
+ GCC_except_table18
+ GCC_except_table18035
+ GCC_except_table18168
+ GCC_except_table18227
+ GCC_except_table18238
+ GCC_except_table18240
+ GCC_except_table18297
+ GCC_except_table183
+ GCC_except_table1830
+ GCC_except_table18308
+ GCC_except_table18322
+ GCC_except_table18327
+ GCC_except_table18331
+ GCC_except_table18347
+ GCC_except_table18348
+ GCC_except_table18355
+ GCC_except_table18358
+ GCC_except_table1836
+ GCC_except_table18388
+ GCC_except_table18417
+ GCC_except_table18420
+ GCC_except_table18437
+ GCC_except_table18438
+ GCC_except_table18443
+ GCC_except_table18485
+ GCC_except_table18503
+ GCC_except_table18514
+ GCC_except_table18515
+ GCC_except_table18530
+ GCC_except_table18538
+ GCC_except_table18540
+ GCC_except_table18542
+ GCC_except_table18544
+ GCC_except_table18547
+ GCC_except_table18548
+ GCC_except_table18549
+ GCC_except_table18551
+ GCC_except_table18552
+ GCC_except_table18553
+ GCC_except_table18555
+ GCC_except_table18560
+ GCC_except_table18564
+ GCC_except_table18565
+ GCC_except_table18568
+ GCC_except_table18572
+ GCC_except_table18574
+ GCC_except_table18576
+ GCC_except_table18577
+ GCC_except_table18580
+ GCC_except_table18582
+ GCC_except_table18586
+ GCC_except_table18637
+ GCC_except_table18652
+ GCC_except_table18681
+ GCC_except_table18820
+ GCC_except_table18822
+ GCC_except_table18860
+ GCC_except_table18865
+ GCC_except_table18868
+ GCC_except_table18891
+ GCC_except_table18893
+ GCC_except_table18894
+ GCC_except_table18895
+ GCC_except_table18899
+ GCC_except_table18900
+ GCC_except_table18903
+ GCC_except_table18904
+ GCC_except_table18911
+ GCC_except_table18914
+ GCC_except_table18916
+ GCC_except_table18918
+ GCC_except_table18920
+ GCC_except_table18923
+ GCC_except_table18928
+ GCC_except_table18933
+ GCC_except_table18936
+ GCC_except_table18938
+ GCC_except_table18944
+ GCC_except_table18947
+ GCC_except_table18950
+ GCC_except_table18953
+ GCC_except_table18955
+ GCC_except_table18959
+ GCC_except_table18961
+ GCC_except_table18963
+ GCC_except_table18964
+ GCC_except_table18971
+ GCC_except_table18974
+ GCC_except_table18976
+ GCC_except_table18983
+ GCC_except_table18985
+ GCC_except_table18987
+ GCC_except_table18989
+ GCC_except_table18991
+ GCC_except_table18998
+ GCC_except_table19002
+ GCC_except_table19006
+ GCC_except_table19008
+ GCC_except_table19010
+ GCC_except_table19012
+ GCC_except_table19014
+ GCC_except_table19018
+ GCC_except_table19019
+ GCC_except_table19020
+ GCC_except_table19024
+ GCC_except_table19025
+ GCC_except_table19029
+ GCC_except_table19031
+ GCC_except_table19034
+ GCC_except_table19035
+ GCC_except_table19038
+ GCC_except_table19043
+ GCC_except_table19044
+ GCC_except_table19047
+ GCC_except_table19050
+ GCC_except_table19053
+ GCC_except_table19055
+ GCC_except_table19057
+ GCC_except_table19059
+ GCC_except_table19060
+ GCC_except_table19071
+ GCC_except_table19075
+ GCC_except_table19079
+ GCC_except_table19183
+ GCC_except_table19196
+ GCC_except_table19200
+ GCC_except_table19202
+ GCC_except_table19204
+ GCC_except_table19212
+ GCC_except_table19337
+ GCC_except_table19349
+ GCC_except_table19368
+ GCC_except_table19444
+ GCC_except_table19446
+ GCC_except_table19451
+ GCC_except_table19454
+ GCC_except_table19462
+ GCC_except_table19483
+ GCC_except_table19489
+ GCC_except_table19493
+ GCC_except_table19495
+ GCC_except_table19499
+ GCC_except_table19509
+ GCC_except_table19514
+ GCC_except_table19516
+ GCC_except_table19524
+ GCC_except_table19525
+ GCC_except_table19528
+ GCC_except_table19529
+ GCC_except_table19532
+ GCC_except_table19597
+ GCC_except_table196
+ GCC_except_table19663
+ GCC_except_table19681
+ GCC_except_table19753
+ GCC_except_table19757
+ GCC_except_table19768
+ GCC_except_table19777
+ GCC_except_table19779
+ GCC_except_table19783
+ GCC_except_table19785
+ GCC_except_table19787
+ GCC_except_table19801
+ GCC_except_table19951
+ GCC_except_table19962
+ GCC_except_table19999
+ GCC_except_table20009
+ GCC_except_table20040
+ GCC_except_table20074
+ GCC_except_table2008
+ GCC_except_table20083
+ GCC_except_table20089
+ GCC_except_table20092
+ GCC_except_table20097
+ GCC_except_table20101
+ GCC_except_table20106
+ GCC_except_table20112
+ GCC_except_table20118
+ GCC_except_table20129
+ GCC_except_table20135
+ GCC_except_table2014
+ GCC_except_table20148
+ GCC_except_table20158
+ GCC_except_table20305
+ GCC_except_table20309
+ GCC_except_table20343
+ GCC_except_table20351
+ GCC_except_table20353
+ GCC_except_table20381
+ GCC_except_table20421
+ GCC_except_table20425
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
+ GCC_except_table20538
+ GCC_except_table20541
+ GCC_except_table20546
+ GCC_except_table20549
+ GCC_except_table20577
+ GCC_except_table20581
+ GCC_except_table20582
+ GCC_except_table20583
+ GCC_except_table20589
+ GCC_except_table20590
+ GCC_except_table20602
+ GCC_except_table20664
+ GCC_except_table20710
+ GCC_except_table20721
+ GCC_except_table20764
+ GCC_except_table20784
+ GCC_except_table20837
+ GCC_except_table20841
+ GCC_except_table20889
+ GCC_except_table20906
+ GCC_except_table20923
+ GCC_except_table20935
+ GCC_except_table20940
+ GCC_except_table20941
+ GCC_except_table20945
+ GCC_except_table20947
+ GCC_except_table20952
+ GCC_except_table20953
+ GCC_except_table20955
+ GCC_except_table20963
+ GCC_except_table20968
+ GCC_except_table20969
+ GCC_except_table20970
+ GCC_except_table20971
+ GCC_except_table20977
+ GCC_except_table20979
+ GCC_except_table20982
+ GCC_except_table20983
+ GCC_except_table20986
+ GCC_except_table20987
+ GCC_except_table20990
+ GCC_except_table20991
+ GCC_except_table20997
+ GCC_except_table20999
+ GCC_except_table21001
+ GCC_except_table21003
+ GCC_except_table21005
+ GCC_except_table21007
+ GCC_except_table21009
+ GCC_except_table21011
+ GCC_except_table21013
+ GCC_except_table21015
+ GCC_except_table21020
+ GCC_except_table21024
+ GCC_except_table21035
+ GCC_except_table21154
+ GCC_except_table21161
+ GCC_except_table21174
+ GCC_except_table21180
+ GCC_except_table21298
+ GCC_except_table21371
+ GCC_except_table21401
+ GCC_except_table21461
+ GCC_except_table21577
+ GCC_except_table21578
+ GCC_except_table21589
+ GCC_except_table21590
+ GCC_except_table21611
+ GCC_except_table21613
+ GCC_except_table21620
+ GCC_except_table21638
+ GCC_except_table21647
+ GCC_except_table21665
+ GCC_except_table21713
+ GCC_except_table21720
+ GCC_except_table21736
+ GCC_except_table21790
+ GCC_except_table21806
+ GCC_except_table21823
+ GCC_except_table21828
+ GCC_except_table21840
+ GCC_except_table21842
+ GCC_except_table21871
+ GCC_except_table21921
+ GCC_except_table21933
+ GCC_except_table21935
+ GCC_except_table21966
+ GCC_except_table21978
+ GCC_except_table21983
+ GCC_except_table21990
+ GCC_except_table220
+ GCC_except_table22020
+ GCC_except_table22033
+ GCC_except_table22036
+ GCC_except_table22064
+ GCC_except_table22095
+ GCC_except_table22184
+ GCC_except_table22230
+ GCC_except_table22234
+ GCC_except_table22238
+ GCC_except_table22265
+ GCC_except_table22283
+ GCC_except_table22292
+ GCC_except_table22360
+ GCC_except_table22361
+ GCC_except_table2243
+ GCC_except_table22439
+ GCC_except_table22506
+ GCC_except_table2262
+ GCC_except_table2267
+ GCC_except_table2275
+ GCC_except_table2278
+ GCC_except_table22913
+ GCC_except_table2303
+ GCC_except_table2308
+ GCC_except_table23207
+ GCC_except_table23219
+ GCC_except_table23228
+ GCC_except_table2326
+ GCC_except_table23275
+ GCC_except_table23279
+ GCC_except_table2328
+ GCC_except_table23335
+ GCC_except_table23347
+ GCC_except_table23363
+ GCC_except_table23464
+ GCC_except_table23473
+ GCC_except_table23503
+ GCC_except_table23579
+ GCC_except_table23580
+ GCC_except_table23646
+ GCC_except_table2365
+ GCC_except_table23664
+ GCC_except_table23671
+ GCC_except_table23695
+ GCC_except_table2381
+ GCC_except_table23872
+ GCC_except_table23878
+ GCC_except_table23897
+ GCC_except_table23901
+ GCC_except_table23946
+ GCC_except_table23980
+ GCC_except_table24018
+ GCC_except_table24021
+ GCC_except_table24025
+ GCC_except_table24068
+ GCC_except_table24069
+ GCC_except_table24133
+ GCC_except_table24136
+ GCC_except_table24151
+ GCC_except_table24156
+ GCC_except_table24164
+ GCC_except_table24173
+ GCC_except_table24175
+ GCC_except_table24186
+ GCC_except_table24202
+ GCC_except_table24209
+ GCC_except_table24236
+ GCC_except_table244
+ GCC_except_table24428
+ GCC_except_table24432
+ GCC_except_table24439
+ GCC_except_table24440
+ GCC_except_table24443
+ GCC_except_table24444
+ GCC_except_table24446
+ GCC_except_table24447
+ GCC_except_table24448
+ GCC_except_table24450
+ GCC_except_table24455
+ GCC_except_table24457
+ GCC_except_table24460
+ GCC_except_table24461
+ GCC_except_table24462
+ GCC_except_table24465
+ GCC_except_table24466
+ GCC_except_table24467
+ GCC_except_table24497
+ GCC_except_table24500
+ GCC_except_table24522
+ GCC_except_table24526
+ GCC_except_table24527
+ GCC_except_table24532
+ GCC_except_table24537
+ GCC_except_table24541
+ GCC_except_table24605
+ GCC_except_table24612
+ GCC_except_table24614
+ GCC_except_table24616
+ GCC_except_table24618
+ GCC_except_table24620
+ GCC_except_table24628
+ GCC_except_table24630
+ GCC_except_table24644
+ GCC_except_table2465
+ GCC_except_table24670
+ GCC_except_table24680
+ GCC_except_table24684
+ GCC_except_table24686
+ GCC_except_table24694
+ GCC_except_table24710
+ GCC_except_table24713
+ GCC_except_table24717
+ GCC_except_table24721
+ GCC_except_table24731
+ GCC_except_table24736
+ GCC_except_table24740
+ GCC_except_table24742
+ GCC_except_table24744
+ GCC_except_table24746
+ GCC_except_table24754
+ GCC_except_table24766
+ GCC_except_table24768
+ GCC_except_table24780
+ GCC_except_table24804
+ GCC_except_table24820
+ GCC_except_table24838
+ GCC_except_table24842
+ GCC_except_table24867
+ GCC_except_table24869
+ GCC_except_table24871
+ GCC_except_table24894
+ GCC_except_table24897
+ GCC_except_table24900
+ GCC_except_table24902
+ GCC_except_table24956
+ GCC_except_table25018
+ GCC_except_table25021
+ GCC_except_table25024
+ GCC_except_table25031
+ GCC_except_table25057
+ GCC_except_table25060
+ GCC_except_table25092
+ GCC_except_table25098
+ GCC_except_table25102
+ GCC_except_table25127
+ GCC_except_table25139
+ GCC_except_table25142
+ GCC_except_table25149
+ GCC_except_table25157
+ GCC_except_table25158
+ GCC_except_table25159
+ GCC_except_table25166
+ GCC_except_table2518
+ GCC_except_table25260
+ GCC_except_table25261
+ GCC_except_table25262
+ GCC_except_table25263
+ GCC_except_table25267
+ GCC_except_table25271
+ GCC_except_table25272
+ GCC_except_table25273
+ GCC_except_table25276
+ GCC_except_table25306
+ GCC_except_table25314
+ GCC_except_table25318
+ GCC_except_table25346
+ GCC_except_table25361
+ GCC_except_table2538
+ GCC_except_table25395
+ GCC_except_table25399
+ GCC_except_table25407
+ GCC_except_table25423
+ GCC_except_table25443
+ GCC_except_table25447
+ GCC_except_table25478
+ GCC_except_table2548
+ GCC_except_table25484
+ GCC_except_table2554
+ GCC_except_table25553
+ GCC_except_table25571
+ GCC_except_table25583
+ GCC_except_table25586
+ GCC_except_table25589
+ GCC_except_table25598
+ GCC_except_table25601
+ GCC_except_table25604
+ GCC_except_table25607
+ GCC_except_table25610
+ GCC_except_table25613
+ GCC_except_table25616
+ GCC_except_table25619
+ GCC_except_table25622
+ GCC_except_table25625
+ GCC_except_table25628
+ GCC_except_table25631
+ GCC_except_table25634
+ GCC_except_table25637
+ GCC_except_table25640
+ GCC_except_table25643
+ GCC_except_table25649
+ GCC_except_table25652
+ GCC_except_table25655
+ GCC_except_table25658
+ GCC_except_table25661
+ GCC_except_table25664
+ GCC_except_table25667
+ GCC_except_table25670
+ GCC_except_table25673
+ GCC_except_table25676
+ GCC_except_table25679
+ GCC_except_table25682
+ GCC_except_table25685
+ GCC_except_table25688
+ GCC_except_table25691
+ GCC_except_table25694
+ GCC_except_table25697
+ GCC_except_table25700
+ GCC_except_table25703
+ GCC_except_table25706
+ GCC_except_table25709
+ GCC_except_table25715
+ GCC_except_table25721
+ GCC_except_table25727
+ GCC_except_table25730
+ GCC_except_table25736
+ GCC_except_table25739
+ GCC_except_table25742
+ GCC_except_table25745
+ GCC_except_table25748
+ GCC_except_table25751
+ GCC_except_table25754
+ GCC_except_table25757
+ GCC_except_table25760
+ GCC_except_table25763
+ GCC_except_table25766
+ GCC_except_table25769
+ GCC_except_table25778
+ GCC_except_table25781
+ GCC_except_table25784
+ GCC_except_table25790
+ GCC_except_table25793
+ GCC_except_table25851
+ GCC_except_table25854
+ GCC_except_table25857
+ GCC_except_table25959
+ GCC_except_table25966
+ GCC_except_table25968
+ GCC_except_table26014
+ GCC_except_table26059
+ GCC_except_table26067
+ GCC_except_table26071
+ GCC_except_table26082
+ GCC_except_table26126
+ GCC_except_table26128
+ GCC_except_table2615
+ GCC_except_table2618
+ GCC_except_table26249
+ GCC_except_table26255
+ GCC_except_table26277
+ GCC_except_table26316
+ GCC_except_table26319
+ GCC_except_table26325
+ GCC_except_table26330
+ GCC_except_table26334
+ GCC_except_table26342
+ GCC_except_table26369
+ GCC_except_table26377
+ GCC_except_table26418
+ GCC_except_table26540
+ GCC_except_table26544
+ GCC_except_table26547
+ GCC_except_table26549
+ GCC_except_table26664
+ GCC_except_table26859
+ GCC_except_table26867
+ GCC_except_table26873
+ GCC_except_table26884
+ GCC_except_table26894
+ GCC_except_table26896
+ GCC_except_table26898
+ GCC_except_table26903
+ GCC_except_table26905
+ GCC_except_table26919
+ GCC_except_table26924
+ GCC_except_table26928
+ GCC_except_table26948
+ GCC_except_table27
+ GCC_except_table2769
+ GCC_except_table2771
+ GCC_except_table2782
+ GCC_except_table2786
+ GCC_except_table2814
+ GCC_except_table2854
+ GCC_except_table2863
+ GCC_except_table2866
+ GCC_except_table2873
+ GCC_except_table2882
+ GCC_except_table2926
+ GCC_except_table2927
+ GCC_except_table2933
+ GCC_except_table2989
+ GCC_except_table3029
+ GCC_except_table309
+ GCC_except_table310
+ GCC_except_table3136
+ GCC_except_table3145
+ GCC_except_table3166
+ GCC_except_table317
+ GCC_except_table3363
+ GCC_except_table3369
+ GCC_except_table3463
+ GCC_except_table3465
+ GCC_except_table3474
+ GCC_except_table3494
+ GCC_except_table3505
+ GCC_except_table3521
+ GCC_except_table3549
+ GCC_except_table3563
+ GCC_except_table3568
+ GCC_except_table3570
+ GCC_except_table3577
+ GCC_except_table3580
+ GCC_except_table3581
+ GCC_except_table3585
+ GCC_except_table3587
+ GCC_except_table3591
+ GCC_except_table36
+ GCC_except_table3632
+ GCC_except_table3639
+ GCC_except_table364
+ GCC_except_table3889
+ GCC_except_table3893
+ GCC_except_table3896
+ GCC_except_table3899
+ GCC_except_table3902
+ GCC_except_table3905
+ GCC_except_table3915
+ GCC_except_table3971
+ GCC_except_table4009
+ GCC_except_table4012
+ GCC_except_table4019
+ GCC_except_table4020
+ GCC_except_table4026
+ GCC_except_table4047
+ GCC_except_table4087
+ GCC_except_table4150
+ GCC_except_table4155
+ GCC_except_table4161
+ GCC_except_table4165
+ GCC_except_table4177
+ GCC_except_table4182
+ GCC_except_table4185
+ GCC_except_table4210
+ GCC_except_table4212
+ GCC_except_table4221
+ GCC_except_table4222
+ GCC_except_table4224
+ GCC_except_table4250
+ GCC_except_table4272
+ GCC_except_table4275
+ GCC_except_table4279
+ GCC_except_table4282
+ GCC_except_table4301
+ GCC_except_table4305
+ GCC_except_table4309
+ GCC_except_table4313
+ GCC_except_table4320
+ GCC_except_table4336
+ GCC_except_table4487
+ GCC_except_table4496
+ GCC_except_table450
+ GCC_except_table4504
+ GCC_except_table4506
+ GCC_except_table4512
+ GCC_except_table4514
+ GCC_except_table453
+ GCC_except_table4530
+ GCC_except_table4532
+ GCC_except_table4537
+ GCC_except_table4539
+ GCC_except_table4547
+ GCC_except_table4557
+ GCC_except_table456
+ GCC_except_table4580
+ GCC_except_table459
+ GCC_except_table4613
+ GCC_except_table462
+ GCC_except_table4661
+ GCC_except_table4665
+ GCC_except_table468
+ GCC_except_table4844
+ GCC_except_table4851
+ GCC_except_table4908
+ GCC_except_table4930
+ GCC_except_table4934
+ GCC_except_table4963
+ GCC_except_table500
+ GCC_except_table5058
+ GCC_except_table5063
+ GCC_except_table5071
+ GCC_except_table5097
+ GCC_except_table5166
+ GCC_except_table52
+ GCC_except_table5274
+ GCC_except_table5311
+ GCC_except_table5319
+ GCC_except_table5321
+ GCC_except_table5324
+ GCC_except_table5535
+ GCC_except_table5569
+ GCC_except_table564
+ GCC_except_table5643
+ GCC_except_table5644
+ GCC_except_table5657
+ GCC_except_table5720
+ GCC_except_table5739
+ GCC_except_table5747
+ GCC_except_table5751
+ GCC_except_table5761
+ GCC_except_table5764
+ GCC_except_table580
+ GCC_except_table5824
+ GCC_except_table5829
+ GCC_except_table5839
+ GCC_except_table5849
+ GCC_except_table5877
+ GCC_except_table5891
+ GCC_except_table5898
+ GCC_except_table5906
+ GCC_except_table5908
+ GCC_except_table5943
+ GCC_except_table5944
+ GCC_except_table5947
+ GCC_except_table5948
+ GCC_except_table5956
+ GCC_except_table5969
+ GCC_except_table6054
+ GCC_except_table6056
+ GCC_except_table6079
+ GCC_except_table61
+ GCC_except_table610
+ GCC_except_table6111
+ GCC_except_table6119
+ GCC_except_table6140
+ GCC_except_table6145
+ GCC_except_table6150
+ GCC_except_table6152
+ GCC_except_table6154
+ GCC_except_table617
+ GCC_except_table6173
+ GCC_except_table6178
+ GCC_except_table6182
+ GCC_except_table6243
+ GCC_except_table6270
+ GCC_except_table6275
+ GCC_except_table6279
+ GCC_except_table6283
+ GCC_except_table6288
+ GCC_except_table6293
+ GCC_except_table6297
+ GCC_except_table6301
+ GCC_except_table6305
+ GCC_except_table6317
+ GCC_except_table6318
+ GCC_except_table6320
+ GCC_except_table6328
+ GCC_except_table6330
+ GCC_except_table6331
+ GCC_except_table6332
+ GCC_except_table6333
+ GCC_except_table6335
+ GCC_except_table6340
+ GCC_except_table6341
+ GCC_except_table6342
+ GCC_except_table6345
+ GCC_except_table6346
+ GCC_except_table6348
+ GCC_except_table635
+ GCC_except_table6350
+ GCC_except_table6351
+ GCC_except_table6353
+ GCC_except_table6355
+ GCC_except_table6358
+ GCC_except_table6359
+ GCC_except_table6360
+ GCC_except_table6362
+ GCC_except_table6363
+ GCC_except_table6367
+ GCC_except_table6371
+ GCC_except_table6374
+ GCC_except_table6377
+ GCC_except_table6379
+ GCC_except_table6382
+ GCC_except_table6384
+ GCC_except_table6385
+ GCC_except_table6386
+ GCC_except_table6387
+ GCC_except_table6388
+ GCC_except_table6389
+ GCC_except_table6399
+ GCC_except_table6409
+ GCC_except_table6440
+ GCC_except_table65
+ GCC_except_table6568
+ GCC_except_table6682
+ GCC_except_table6751
+ GCC_except_table6959
+ GCC_except_table7018
+ GCC_except_table7064
+ GCC_except_table7071
+ GCC_except_table7082
+ GCC_except_table7088
+ GCC_except_table7095
+ GCC_except_table7102
+ GCC_except_table7106
+ GCC_except_table7109
+ GCC_except_table7112
+ GCC_except_table7116
+ GCC_except_table7121
+ GCC_except_table7129
+ GCC_except_table7135
+ GCC_except_table7138
+ GCC_except_table7140
+ GCC_except_table7146
+ GCC_except_table7152
+ GCC_except_table7165
+ GCC_except_table7169
+ GCC_except_table717
+ GCC_except_table7173
+ GCC_except_table7183
+ GCC_except_table7186
+ GCC_except_table7193
+ GCC_except_table7200
+ GCC_except_table7222
+ GCC_except_table7236
+ GCC_except_table724
+ GCC_except_table7254
+ GCC_except_table7257
+ GCC_except_table7262
+ GCC_except_table7270
+ GCC_except_table7276
+ GCC_except_table7281
+ GCC_except_table7283
+ GCC_except_table7291
+ GCC_except_table7361
+ GCC_except_table7364
+ GCC_except_table7368
+ GCC_except_table7371
+ GCC_except_table7376
+ GCC_except_table7379
+ GCC_except_table7382
+ GCC_except_table7385
+ GCC_except_table7388
+ GCC_except_table739
+ GCC_except_table7390
+ GCC_except_table7392
+ GCC_except_table7394
+ GCC_except_table7396
+ GCC_except_table7399
+ GCC_except_table7401
+ GCC_except_table7404
+ GCC_except_table741
+ GCC_except_table7412
+ GCC_except_table7416
+ GCC_except_table7421
+ GCC_except_table7423
+ GCC_except_table7425
+ GCC_except_table7427
+ GCC_except_table7431
+ GCC_except_table7440
+ GCC_except_table7444
+ GCC_except_table7452
+ GCC_except_table7456
+ GCC_except_table747
+ GCC_except_table7475
+ GCC_except_table7481
+ GCC_except_table7489
+ GCC_except_table7521
+ GCC_except_table7546
+ GCC_except_table7548
+ GCC_except_table7563
+ GCC_except_table758
+ GCC_except_table764
+ GCC_except_table778
+ GCC_except_table7796
+ GCC_except_table7803
+ GCC_except_table7816
+ GCC_except_table7817
+ GCC_except_table783
+ GCC_except_table7830
+ GCC_except_table7862
+ GCC_except_table788
+ GCC_except_table7891
+ GCC_except_table7908
+ GCC_except_table7910
+ GCC_except_table7916
+ GCC_except_table7920
+ GCC_except_table7932
+ GCC_except_table7935
+ GCC_except_table7992
+ GCC_except_table7996
+ GCC_except_table8009
+ GCC_except_table8064
+ GCC_except_table8075
+ GCC_except_table8082
+ GCC_except_table8094
+ GCC_except_table8096
+ GCC_except_table8121
+ GCC_except_table8127
+ GCC_except_table8131
+ GCC_except_table814
+ GCC_except_table8148
+ GCC_except_table8154
+ GCC_except_table8196
+ GCC_except_table8211
+ GCC_except_table8216
+ GCC_except_table8218
+ GCC_except_table8223
+ GCC_except_table8233
+ GCC_except_table8241
+ GCC_except_table8245
+ GCC_except_table8248
+ GCC_except_table8257
+ GCC_except_table8262
+ GCC_except_table8290
+ GCC_except_table8348
+ GCC_except_table8349
+ GCC_except_table8361
+ GCC_except_table8367
+ GCC_except_table8372
+ GCC_except_table8373
+ GCC_except_table8407
+ GCC_except_table8412
+ GCC_except_table8418
+ GCC_except_table8430
+ GCC_except_table8443
+ GCC_except_table8456
+ GCC_except_table8480
+ GCC_except_table8510
+ GCC_except_table852
+ GCC_except_table8545
+ GCC_except_table8548
+ GCC_except_table8601
+ GCC_except_table8609
+ GCC_except_table8624
+ GCC_except_table8626
+ GCC_except_table863
+ GCC_except_table8743
+ GCC_except_table8786
+ GCC_except_table8787
+ GCC_except_table8811
+ GCC_except_table884
+ GCC_except_table890
+ GCC_except_table8974
+ GCC_except_table8978
+ GCC_except_table899
+ GCC_except_table8991
+ GCC_except_table8995
+ GCC_except_table9055
+ GCC_except_table906
+ GCC_except_table9067
+ GCC_except_table9074
+ GCC_except_table9077
+ GCC_except_table9102
+ GCC_except_table911
+ GCC_except_table9127
+ GCC_except_table9131
+ GCC_except_table9134
+ GCC_except_table9141
+ GCC_except_table9145
+ GCC_except_table918
+ GCC_except_table9206
+ GCC_except_table927
+ GCC_except_table932
+ GCC_except_table9330
+ GCC_except_table9364
+ GCC_except_table9368
+ GCC_except_table9374
+ GCC_except_table9376
+ GCC_except_table9382
+ GCC_except_table9385
+ GCC_except_table9420
+ GCC_except_table9464
+ GCC_except_table950
+ GCC_except_table9682
+ GCC_except_table9683
+ GCC_except_table9684
+ GCC_except_table9701
+ GCC_except_table9706
+ GCC_except_table9719
+ GCC_except_table9754
+ GCC_except_table9765
+ GCC_except_table981
+ GCC_except_table9821
+ GCC_except_table989
+ GCC_except_table9906
+ GCC_except_table9907
+ GCC_except_table9939
+ GCC_except_table9941
+ GCC_except_table9944
+ GCC_except_table9946
+ GCC_except_table9947
+ GCC_except_table9949
+ GCC_except_table9951
+ GCC_except_table9952
+ OBJC_IVAR_$_PLBackgroundJobService._lazyProcessingSetURL
+ OBJC_IVAR_$_PLBackgroundJobWorkerPendingWorkItems._zeroWorkItemsForCurrentCriteria
+ OBJC_IVAR_$_PLDelayedSaveActions._biomeDeletedAssetCreationDateByAssetUUID
+ OBJC_IVAR_$_PLDelayedSaveActionsDetail._biomeDeletedAssetCreationDateByAssetUUID
+ OBJC_IVAR_$_PLFeatureAvailabilityLexemeCriteria._notAllowedForAnalysisID
+ OBJC_IVAR_$_PLFeatureAvailabilityLexemeCriteria._notInHighlightID
+ OBJC_IVAR_$_PLFeatureAvailabilityLexemeCriteria._savedAssetTypeByLexemeID
+ OBJC_IVAR_$_PLFeatureAvailabilityLexemeCriteria._validImageCaptionByLexemeID
+ OBJC_IVAR_$_PLFeatureAvailabilityLexemeCriteria._validImageEmbeddingByLexemeID
+ OBJC_IVAR_$_PLFeatureAvailabilityLexemeCriteria._validMediaAnalysisByLexemeID
+ OBJC_IVAR_$_PLFeatureAvailabilityLexemeCriteria._validMediaAnalysisImageByLexemeID
+ OBJC_IVAR_$_PLFeatureAvailabilityLexemeCriteria._validRichImageCaptionByLexemeID
+ OBJC_IVAR_$_PLFeatureAvailabilityLexemeCriteria._validSceneAnalysisByLexemeID
+ OBJC_IVAR_$_PLFeatureAvailabilityLexemeCriteria._versionProvider
+ OBJC_IVAR_$_PLMediaMetadataVirtualResource._data
+ OBJC_IVAR_$_PLMediaMetadataVirtualResource._mediaMetadataType
+ OBJC_IVAR_$_PLNotificationManager._kvsListener
+ OBJC_IVAR_$_PLPhotoLibraryBundleController._stateCaptureHandler
+ OBJC_IVAR_$_PLPhotoLibraryBundleController._stateLock
+ OBJC_IVAR_$_PLPhotoLibraryBundleController._stateLock_lastBundleShutdownDate
+ OBJC_IVAR_$_PLPhotoLibraryBundleController._stateLock_lastBundleShutdownLibraryID
+ OBJC_IVAR_$_PLPhotoLibraryBundleController._stateLock_lastBundleShutdownReason
+ OBJC_IVAR_$_PLRebuildUserNotification._libraryPath
+ OBJC_IVAR_$_PLSearchIndexingEngine._queue_timeOfLastSearchProgressReport
+ OBJC_IVAR_$_PLSearchIndexingEngineLibraryServicesProvider._didLogLibraryIdentifier
+ OBJC_IVAR_$_PLSearchOCRTextLineCandidate._isLowConfidence
+ OBJC_IVAR_$_PLSharedAlbumsActivityKVSListener._delegate
+ OBJC_IVAR_$_PLSharedAlbumsActivityKVSListener._isListening
+ OBJC_IVAR_$_PLSharedAlbumsActivityKVSListener._kvStore
+ OBJC_IVAR_$_PLSharedAlbumsActivityKVSListener._lock
+ OBJC_IVAR_$_PLSharedAlbumsActivityKVSListener._lock_cachedEventLogLastEnteredDate
+ OBJC_IVAR_$_PLSharedAlbumsActivityKVSListener._lock_cachedLastSeenDate
+ OBJC_IVAR_$_PLSyndicationResourceFileCoordinator._copiedPrimaryURL
+ OBJC_IVAR_$_PLSyndicationResourceFileCoordinator._copiedVideoComplementURL
+ OBJC_IVAR_$_PLSyndicationResourceFileCoordinator._materializesDatalessFiles
+ OBJC_IVAR_$_PLSyndicationResourceFileCoordinator._originalFilename
+ OBJC_IVAR_$_PLSyndicationResourceFileCoordinator._pathManager
+ OBJC_IVAR_$_PLSyndicationResourceFileCoordinator._sourceURL
+ OBJC_IVAR_$_PLSyndicationResourceFileCoordinator._videoComplementFilename
+ OBJC_IVAR_$_PLSyndicationResourceFileCoordinator._videoComplementSourceURL
+ PLFileSystemImportCurrentVersion_block_invoke.s_cplAssetDirectoryPrefix
+ PLFileSystemImportCurrentVersion_block_invoke.s_onceToken
+ PLPhotoAnalysisServiceIgnoredOperationID_block_invoke.mediaStreamDownloadQueue
+ PLPhotoAnalysisServiceIgnoredOperationID_block_invoke.onceToken
+ PLXPCStoreAllowedEntityNames.pl_once_object_15
+ PLXPCStoreAllowedEntityNames.pl_once_token_15
+ PLXPCStoreDeniedEntityNames.pl_once_object_16
+ PLXPCStoreDeniedEntityNames.pl_once_token_16
+ _LEOLexemeIDInvalid
+ _LEOSQLiteErrorDomain
+ _NSUbiquitousKeyValueStoreChangedKeysKey
+ _NSUbiquitousKeyValueStoreDidChangeExternallyNotification
+ _OBJC_CLASS_$_PFRadarComponent
+ _OBJC_CLASS_$_PFTapToRadarDraft
+ _OBJC_CLASS_$_PLBackgroundJobLowPrioritySearchIndexingWorker
+ _OBJC_CLASS_$_PLBiomeDonations
+ _OBJC_CLASS_$_PLFeatureAvailabilityLexemeCriteria
+ _OBJC_CLASS_$_PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing
+ _OBJC_CLASS_$_PLModelMigrationAction_ReevaluateAllowedForAnalysisForUnknownKindAssets
+ _OBJC_CLASS_$_PLModelMigrationAction_ResetLocalAvailabilityRetryStateForDeferredProcessingFinalResources
+ _OBJC_CLASS_$_PLModelMigrationAction_SetKeepOriginalsPrefetchModeForVisualIntelligenceLibrary
+ _OBJC_CLASS_$_PLModelMigrationAction_SetRunOnceFlagToLinkOrphanedCollectionShareContributors
+ _OBJC_CLASS_$_PLModelMigrationAction_SetRunOnceFlagToRestoreMissingCollectionSharePosts
+ _OBJC_CLASS_$_PLSharedAlbumsActivityKVSListener
+ _OBJC_CLASS_$_PLSyndicationResourceFileCoordinator
+ _OBJC_METACLASS_$_PLBackgroundJobLowPrioritySearchIndexingWorker
+ _OBJC_METACLASS_$_PLBiomeDonations
+ _OBJC_METACLASS_$_PLFeatureAvailabilityLexemeCriteria
+ _OBJC_METACLASS_$_PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing
+ _OBJC_METACLASS_$_PLModelMigrationAction_ReevaluateAllowedForAnalysisForUnknownKindAssets
+ _OBJC_METACLASS_$_PLModelMigrationAction_ResetLocalAvailabilityRetryStateForDeferredProcessingFinalResources
+ _OBJC_METACLASS_$_PLModelMigrationAction_SetKeepOriginalsPrefetchModeForVisualIntelligenceLibrary
+ _OBJC_METACLASS_$_PLModelMigrationAction_SetRunOnceFlagToLinkOrphanedCollectionShareContributors
+ _OBJC_METACLASS_$_PLModelMigrationAction_SetRunOnceFlagToRestoreMissingCollectionSharePosts
+ _OBJC_METACLASS_$_PLSharedAlbumsActivityKVSListener
+ _OBJC_METACLASS_$_PLSyndicationResourceFileCoordinator
+ _PAMediaConversionServiceOptionFormatConversionOnlyKey
+ _PFTapToRadarCreateDraft
+ _PFTapToRadarGetAuthorizationStatus
+ _PLCloudSharedCommentPredicateForCollectionShare
+ _PLFeatureAvailabilityLexemeEvaluationResultCaptionsAreCurrent
+ _PLGetSandboxExtensionTokenCanonical
+ _PLGetSandboxExtensionTokenForProcessCanonical
+ _PLIncludeImageEmbeddingVersionInPredicate
+ _PLIsErrorOrUnderlyingErrorDatalessMaterializationPrevented
+ _PLIsValidContextualVideoThumbnailIdentifier
+ _PLLibraryIdentifierSupportsSearchProgressReporting
+ _PLNoFollowPath
+ _PLOpenRegularFileForClient
+ _PLPlatformBackgroundSearchIndexingSupported
+ _PLPlatformVisualIntelligenceSyncSupported
+ _PLSearchIndexProgressAnalyzedAndIndexedCountKey
+ _PLSearchIndexProgressInIndexCountKey
+ _PLSearchIndexProgressNeedingDonationCountKey
+ _PLSearchIndexProgressPartiallyDonatedCountKey
+ _PLSearchIndexProgressTotalAssetCountKey
+ _PLSearchOCRConfidenceThresholdDefault
+ _PLSearchOCRConfidenceThresholdHighRecall
+ _PLStringFromCoreAnalyticsLibraryID
+ _PLSyndicationCSProvideOptionsAllowDownload
+ _PLVettedResourcePath
+ _SANDBOX_EXTENSION_CANONICAL
+ _TCCAccessCopyBundleIdentifiersDisabledForService
+ __102-[PLCloudPhotoLibraryManager _disableACPLAfterMainScopeWipedInCloudIfNecessaryWithStatus:transaction:]_block_invoke
+ __103-[PLBackgroundJobSharedAssetContainerUpdateWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ __106-[PLBackgroundJobResourceUploadExtensionRunnerWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ __106-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:searchProgressOnly:completionHandler:]_block_invoke
+ __106-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:searchProgressOnly:completionHandler:]_block_invoke_2
+ __106-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:searchProgressOnly:completionHandler:]_block_invoke_3
+ __106-[PLSearchIndexingEngine getSearchDonationProgressInLibrary:shouldCompute:shouldReport:completionHandler:]_block_invoke
+ __106-[PLSearchIndexingEngine getSearchDonationProgressInLibrary:shouldCompute:shouldReport:completionHandler:]_block_invoke_2
+ __116-[PLSyndicationSyncServiceWrapper executeQueryForSyncManager:type:startDate:endDate:itemsHandler:completionHandler:]_block_invoke
+ __118-[PLCollectionShareCPLBackend updateAccessRequestForParticipant:toAcceptanceStatus:collectionShare:completionHandler:]_block_invoke
+ __139+[PLSyndicationResourceDataStore _provideSourceURLsForBundleID:syndicationIdentifier:typeIdentifier:isLivePhoto:options:completionHandler:]_block_invoke
+ __152-[PLSearchIndexingEngine _inq_donateSpotlightItemsByBundleID:leoDonatableItems:leoLexemeScoreUpdates:deleteIdentifiers:spotlightClientState:completion:]_block_invoke_2
+ __167+[PLSyndicationResourceDataStore provideFileURLAndUnwrapLivePhotoIfNeededForItemIdentifiersWithBundleIDs:destURLs:pathManager:options:resultHandler:completionHandler:]_block_invoke
+ __197+[PLIntensiveResourceTask(Constructors) taskForGeneratingDeferredAdjustmentForAsset:trackingIdentifier:imageConversionClient:videoConversionClient:reason:clientBundleID:allowCancellationByService:]_block_invoke
+ __202-[PLManagedAsset _generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:retryNumber:allowCancellationByService:clientBundleID:shouldSaveMediaConversionResultBlock:completion:]_block_invoke
+ __32-[PLIntensiveResourceTask start]_block_invoke
+ __61-[PLBackgroundJobService initWithWorkerClasses:statusCenter:]_block_invoke
+ __67-[PLBackgroundJobWorker pendingWorkItemsInLibrary:currentCriteria:]_block_invoke
+ __72-[PLManagedObjectPagingIterator countRemainingWithManagedObjectContext:]_block_invoke
+ __74-[PLSearchIndexingRebuildEngine _inq_performRebuildForLibrary:completion:]_block_invoke
+ __77-[PLSearchIndexingEngine reportFeatureProcessingSnapshot:library:completion:]_block_invoke
+ __81-[PLCloudPhotoLibraryManager _restoreMissingCollectionSharePostsWithCPLSettings:]_block_invoke
+ __85-[PLBackgroundJobWorker pendingCriteriaInLibrary:currentCriteria:outSignalAgainDate:]_block_invoke
+ __86-[PLCloudPhotoLibraryManager _linkOrphanedCollectionShareContributorsWithCPLSettings:]_block_invoke
+ __90-[PLBackgroundJobEditRenderingWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ __91-[PLCloudPhotoLibraryManager _deactivateCPLSyncWithResetMode:reason:willBecomeNonSyncable:]_block_invoke
+ __OBJC_$_CLASS_METHODS_PLAssetsdResourceService(Testing)
+ __OBJC_$_CLASS_METHODS_PLBackgroundJobLowPrioritySearchIndexingWorker
+ __OBJC_$_CLASS_METHODS_PLBiomeDonations
+ __OBJC_$_CLASS_METHODS_PLFeatureAvailabilityLexemeCriteria
+ __OBJC_$_CLASS_METHODS_PLFileBackedThumbnailVirtualResource
+ __OBJC_$_CLASS_METHODS_PLSyndicationResourceFileCoordinator
+ __OBJC_$_CLASS_METHODS_PLVirtualResource
+ __OBJC_$_INSTANCE_METHODS_PLBackgroundJobLowPrioritySearchIndexingWorker
+ __OBJC_$_INSTANCE_METHODS_PLFeatureAvailabilityLexemeCriteria
+ __OBJC_$_INSTANCE_METHODS_PLManagedFolder(PLJournalEntryPayload)
+ __OBJC_$_INSTANCE_METHODS_PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing
+ __OBJC_$_INSTANCE_METHODS_PLModelMigrationAction_ReevaluateAllowedForAnalysisForUnknownKindAssets
+ __OBJC_$_INSTANCE_METHODS_PLModelMigrationAction_ResetLocalAvailabilityRetryStateForDeferredProcessingFinalResources
+ __OBJC_$_INSTANCE_METHODS_PLModelMigrationAction_SetKeepOriginalsPrefetchModeForVisualIntelligenceLibrary
+ __OBJC_$_INSTANCE_METHODS_PLModelMigrationAction_SetRunOnceFlagToLinkOrphanedCollectionShareContributors
+ __OBJC_$_INSTANCE_METHODS_PLModelMigrationAction_SetRunOnceFlagToRestoreMissingCollectionSharePosts
+ __OBJC_$_INSTANCE_METHODS_PLSharedAlbumsActivityKVSListener
+ __OBJC_$_INSTANCE_METHODS_PLSyndicationResourceFileCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_PLFeatureAvailabilityLexemeCriteria
+ __OBJC_$_INSTANCE_VARIABLES_PLSharedAlbumsActivityKVSListener
+ __OBJC_$_INSTANCE_VARIABLES_PLSyndicationResourceFileCoordinator
+ __OBJC_$_PROP_LIST_PLMediaMetadataVirtualResource
+ __OBJC_$_PROP_LIST_PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing
+ __OBJC_$_PROP_LIST_PLModelMigrationAction_ReevaluateAllowedForAnalysisForUnknownKindAssets
+ __OBJC_$_PROP_LIST_PLModelMigrationAction_ResetLocalAvailabilityRetryStateForDeferredProcessingFinalResources
+ __OBJC_$_PROP_LIST_PLModelMigrationAction_SetKeepOriginalsPrefetchModeForVisualIntelligenceLibrary
+ __OBJC_$_PROP_LIST_PLModelMigrationAction_SetRunOnceFlagToLinkOrphanedCollectionShareContributors
+ __OBJC_$_PROP_LIST_PLModelMigrationAction_SetRunOnceFlagToRestoreMissingCollectionSharePosts
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
+ __OBJC_CLASS_PROTOCOLS_$_PLModelMigrationAction_ResetLocalAvailabilityRetryStateForDeferredProcessingFinalResources
+ __OBJC_CLASS_PROTOCOLS_$_PLModelMigrationAction_SetKeepOriginalsPrefetchModeForVisualIntelligenceLibrary
+ __OBJC_CLASS_PROTOCOLS_$_PLModelMigrationAction_SetRunOnceFlagToLinkOrphanedCollectionShareContributors
+ __OBJC_CLASS_PROTOCOLS_$_PLModelMigrationAction_SetRunOnceFlagToRestoreMissingCollectionSharePosts
+ __OBJC_CLASS_PROTOCOLS_$_PLPhotoLibraryBundleController
+ __OBJC_CLASS_RO_$_PLBackgroundJobLowPrioritySearchIndexingWorker
+ __OBJC_CLASS_RO_$_PLBiomeDonations
+ __OBJC_CLASS_RO_$_PLFeatureAvailabilityLexemeCriteria
+ __OBJC_CLASS_RO_$_PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing
+ __OBJC_CLASS_RO_$_PLModelMigrationAction_ReevaluateAllowedForAnalysisForUnknownKindAssets
+ __OBJC_CLASS_RO_$_PLModelMigrationAction_ResetLocalAvailabilityRetryStateForDeferredProcessingFinalResources
+ __OBJC_CLASS_RO_$_PLModelMigrationAction_SetKeepOriginalsPrefetchModeForVisualIntelligenceLibrary
+ __OBJC_CLASS_RO_$_PLModelMigrationAction_SetRunOnceFlagToLinkOrphanedCollectionShareContributors
+ __OBJC_CLASS_RO_$_PLModelMigrationAction_SetRunOnceFlagToRestoreMissingCollectionSharePosts
+ __OBJC_CLASS_RO_$_PLSharedAlbumsActivityKVSListener
+ __OBJC_CLASS_RO_$_PLSyndicationResourceFileCoordinator
+ __OBJC_LABEL_PROTOCOL_$_PLPhotoAnalysisServiceClientOperationCancelling
+ __OBJC_LABEL_PROTOCOL_$_PLPhotoAnalysisServiceClientVisionCancelling
+ __OBJC_LABEL_PROTOCOL_$_PLSharedAlbumsActivityKVSListenerDelegate
+ __OBJC_METACLASS_RO_$_PLBackgroundJobLowPrioritySearchIndexingWorker
+ __OBJC_METACLASS_RO_$_PLBiomeDonations
+ __OBJC_METACLASS_RO_$_PLFeatureAvailabilityLexemeCriteria
+ __OBJC_METACLASS_RO_$_PLModelMigrationAction_FixupAssetsStuckInDeferredProcessing
+ __OBJC_METACLASS_RO_$_PLModelMigrationAction_ReevaluateAllowedForAnalysisForUnknownKindAssets
+ __OBJC_METACLASS_RO_$_PLModelMigrationAction_ResetLocalAvailabilityRetryStateForDeferredProcessingFinalResources
+ __OBJC_METACLASS_RO_$_PLModelMigrationAction_SetKeepOriginalsPrefetchModeForVisualIntelligenceLibrary
+ __OBJC_METACLASS_RO_$_PLModelMigrationAction_SetRunOnceFlagToLinkOrphanedCollectionShareContributors
+ __OBJC_METACLASS_RO_$_PLModelMigrationAction_SetRunOnceFlagToRestoreMissingCollectionSharePosts
+ __OBJC_METACLASS_RO_$_PLSharedAlbumsActivityKVSListener
+ __OBJC_METACLASS_RO_$_PLSyndicationResourceFileCoordinator
+ __OBJC_PROTOCOL_$_PLPhotoAnalysisServiceClientOperationCancelling
+ __OBJC_PROTOCOL_$_PLPhotoAnalysisServiceClientVisionCancelling
+ __OBJC_PROTOCOL_$_PLSharedAlbumsActivityKVSListenerDelegate
+ __PLSafeEntityForNameInManagedObjectContext
+ __PLSyndicationResourceFileCoordinatorError
+ ___100-[PLBackgroundJobSyndicationAssetCleanupWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___102-[PLCloudPhotoLibraryManager _disableACPLAfterMainScopeWipedInCloudIfNecessaryWithStatus:transaction:]_block_invoke
+ ___103-[PLBackgroundJobSharedAssetContainerUpdateWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___103-[PLFeatureAvailabilityLexemeCriteria evaluateLexemeIDsByCategoryDictionary:foundUnrecognizedLexemeID:]_block_invoke
+ ___106-[PLBackgroundJobDeferredRenderDerivativesBaseWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___106-[PLBackgroundJobResourceUploadExtensionRunnerWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___106-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:searchProgressOnly:completionHandler:]_block_invoke
+ ___106-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:searchProgressOnly:completionHandler:]_block_invoke_2
+ ___106-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:searchProgressOnly:completionHandler:]_block_invoke_3
+ ___106-[PLIntensiveResourceTask tryPreparingForReplacementWithNewResponder:existingResponders:existingProgress:]_block_invoke
+ ___106-[PLSearchIndexingEngine getSearchDonationProgressInLibrary:shouldCompute:shouldReport:completionHandler:]_block_invoke
+ ___106-[PLSearchIndexingEngine getSearchDonationProgressInLibrary:shouldCompute:shouldReport:completionHandler:]_block_invoke_2
+ ___108-[PLBackgroundJobSyndicationResourceSanitizationWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___110-[PLAssetsdLibraryInternalService migrateLimitedLibraryAccessFromApplication:toApplication:completionHandler:]_block_invoke
+ ___116-[PLSyndicationSyncServiceWrapper executeQueryForSyncManager:type:startDate:endDate:itemsHandler:completionHandler:]_block_invoke
+ ___118-[PLCollectionShareCPLBackend updateAccessRequestForParticipant:toAcceptanceStatus:collectionShare:completionHandler:]_block_invoke
+ ___118-[PLCollectionShareCPLBackend updateAccessRequestForParticipant:toAcceptanceStatus:collectionShare:completionHandler:]_block_invoke_2
+ ___118-[PLCollectionShareCPLBackend updateAccessRequestForParticipant:toAcceptanceStatus:collectionShare:completionHandler:]_block_invoke_3
+ ___119-[PLModelMigrationAction_ReevaluateAllowedForAnalysisForUnknownKindAssets performActionWithManagedObjectContext:error:]_block_invoke
+ ___124-[PLBackgroundJobResourceUploadExtensionRunnerWorker criteriaNeedingProcessingInLibrary:currentCriteria:outSignalAgainDate:]_block_invoke
+ ___132-[PLAssetsdCloudInternalService updateAccessRequestForParticipantWithUUID:toAcceptanceStatus:inCollectionShareWithIdentifier:reply:]_block_invoke
+ ___137-[PLSyndicationResourceDataStore _copyProviderFileWantsVideoComplement:fromCoordinator:fileIdentifier:pathManager:copiedURL:inode:error:]_block_invoke
+ ___138-[PLModelMigrationAction_ResetLocalAvailabilityRetryStateForDeferredProcessingFinalResources performActionWithManagedObjectContext:error:]_block_invoke
+ ___139+[PLSyndicationResourceDataStore _provideSourceURLsForBundleID:syndicationIdentifier:typeIdentifier:isLivePhoto:options:completionHandler:]_block_invoke
+ ___139+[PLSyndicationResourceDataStore _provideSourceURLsForBundleID:syndicationIdentifier:typeIdentifier:isLivePhoto:options:completionHandler:]_block_invoke_2
+ ___155-[PLSyndicationResourceDataStore _copyAndMarkAsLocallyAvailablePairedLivePhotoResourceForRequestedResource:requestedVideoComplement:fileCoordinator:error:]_block_invoke
+ ___167+[PLSyndicationResourceDataStore provideFileURLAndUnwrapLivePhotoIfNeededForItemIdentifiersWithBundleIDs:destURLs:pathManager:options:resultHandler:completionHandler:]_block_invoke
+ ___202-[PLManagedAsset _generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:retryNumber:allowCancellationByService:clientBundleID:shouldSaveMediaConversionResultBlock:completion:]_block_invoke
+ ___202-[PLManagedAsset _generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:retryNumber:allowCancellationByService:clientBundleID:shouldSaveMediaConversionResultBlock:completion:]_block_invoke_2
+ ___41-[PLCPLSettings hasPersistedPrefetchMode]_block_invoke
+ ___51+[PLSharePost predicateToExcludePostsWithoutAssets]_block_invoke
+ ___54-[PLIntensiveResourceTask transitionToUninterruptible]_block_invoke
+ ___55-[PLBackgroundJobWorkerTypesBuffer redactedDescription]_block_invoke
+ ___56-[PLPhotoLibraryBundleController stateCaptureDictionary]_block_invoke
+ ___57+[PLCascadeUtilities _handleSuggestionsPreferenceChanged]_block_invoke
+ ___57-[PLFeatureAvailabilityLexemeCriteria evaluateLexemeIDs:]_block_invoke
+ ___64+[PLSharePost restoreMissingPostsWithCPLRecords:inPhotoLibrary:]_block_invoke
+ ___66+[PLShareParticipant orphanedCPLContributorRecordsInPhotoLibrary:]_block_invoke
+ ___67-[PLBackgroundJobWorker pendingWorkItemsInLibrary:currentCriteria:]_block_invoke
+ ___68-[PLPhotoLibraryBundleController _updateStateCaptureInfo:libraryID:]_block_invoke
+ ___70-[PLBackgroundJobLowPrioritySearchIndexingWorker locrIdentifyingBlock]_block_invoke
+ ___72-[PLManagedObjectPagingIterator countRemainingWithManagedObjectContext:]_block_invoke
+ ___72-[PLManagedObjectPagingIterator countRemainingWithManagedObjectContext:]_block_invoke_2
+ ___72-[PLManagedObjectPagingIterator countRemainingWithManagedObjectContext:]_block_invoke_3
+ ___74-[PLSearchIndexingRebuildEngine _inq_performRebuildForLibrary:completion:]_block_invoke
+ ___74-[PLSearchIndexingRebuildEngine _inq_performRebuildForLibrary:completion:]_block_invoke_2
+ ___81-[PLCloudPhotoLibraryManager _restoreMissingCollectionSharePostsWithCPLSettings:]_block_invoke
+ ___82+[PLShareParticipant linkCPLContributorContentWithUserIdentifiers:inPhotoLibrary:]_block_invoke
+ ___82-[PLAssetsdDebugService fileTapToRadarWithTitle:description:radarComponent:reply:]_block_invoke
+ ___84-[PLSyndicationResourceFileCoordinator _coordinateReadingSourcesWithError:accessor:]_block_invoke
+ ___84-[PLSyndicationResourceFileCoordinator _coordinateReadingSourcesWithError:accessor:]_block_invoke_2
+ ___85-[PLBackgroundJobWorker pendingCriteriaInLibrary:currentCriteria:outSignalAgainDate:]_block_invoke
+ ___86-[PLCloudPhotoLibraryManager _linkOrphanedCollectionShareContributorsWithCPLSettings:]_block_invoke
+ ___86-[PLCloudPhotoLibraryManager _linkOrphanedCollectionShareContributorsWithCPLSettings:]_block_invoke_2
+ ___87-[PLBackgroundJobPersonSyncWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___87-[PLBackgroundJobStableHashWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___90-[PLBackgroundJobEditRenderingWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___91-[PLBackgroundJobSearchIndexingWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___91-[PLCloudPhotoLibraryManager _deactivateCPLSyncWithResetMode:reason:willBecomeNonSyncable:]_block_invoke
+ ___91-[PLCloudPhotoLibraryManager _deactivateCPLSyncWithResetMode:reason:willBecomeNonSyncable:]_block_invoke_2
+ ___93-[PLAssetsdLibraryInternalService getSearchDonationProgressShouldCompute:shouldReport:reply:]_block_invoke
+ ___94-[PLBackgroundJobDuplicateDetectorWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___97-[PLBackgroundJobResourceAvailabilityWorker workItemsNeedingProcessingInLibrary:currentCriteria:]_block_invoke
+ ___98-[PLCloudPhotoLibraryManager _collectContributorUserIdentifiersForRecords:into:completionHandler:]_block_invoke
+ ___98-[PLCloudPhotoLibraryManager _collectContributorUserIdentifiersForRecords:into:completionHandler:]_block_invoke_2
+ ___98-[PLSyndicationResourceFileCoordinator copyToPrimaryDestination:videoComplementDestination:error:]_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64s72bs80r_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88bs96bs_e17_v16?0"NSArray"8l
+ ___block_descriptor_121_e8_32s40s48s56s64s72s80s88s96s104s112r_e32_v32?0"PLManagedObject"8Q16^B24l
+ ___block_descriptor_122_e8_32s40s48s56s64s72s80s88r96r104r_e5_v8?0l
+ ___block_descriptor_124_e8_32s40s48s56s64s72s80s88s96s104bs112r_e37_v32?0"NSURL"8"NSURL"16"NSError"24l
+ ___block_descriptor_136_e8_32s40s48s56s64s72s80s88bs96bs104r112r120r_e5_v8?0l
+ ___block_descriptor_136_e8_32s40s48s56s64s72s80s88r96r104r112r120r_e36_v24?0"CPLAdjustments"8"NSError"16l
+ ___block_descriptor_137_e8_32s40s48s56s64s72s80s88s96s104s112bs120n11_8_8_s0_t8w8_e5_v8?0l
+ ___block_descriptor_144_e8_32s40s48s56r64r72r80r88r96r104r112r120r128r_e53_v40?0"LEOItem"8"PLLeoLexemeIDSet"16"NSDate"24^B32l
+ ___block_descriptor_176_e8_32s40s48s56s64s72s80s88s96s104s112s120bs128r136r144r152r160r_e5_v8?0l
+ ___block_descriptor_184_e8_32s40s48s56s64s72s80s88s96s104s112s120s128bs136bs144bs152r160r_e63_v60?0B8"NSURL"12"NSURL"20Q28q36"NSDictionary"44"NSError"52l
+ ___block_descriptor_40_e8_32bs_e20_v48?0Q8Q16Q24Q32Q40l
+ ___block_descriptor_40_e8_32r_e24_v16?0"PLPhotoLibrary"8l
+ ___block_descriptor_40_e8_32s_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_40_e8_32s_e53_v32?0"CPLScopedIdentifier"8"CPLRecordChange"16^B24l
+ ___block_descriptor_40_e8_32s_e71_v32?0"PLManagedObject"8"CPLScopedIdentifier"16"PLCollectionShare"24l
+ ___block_descriptor_48_e8_32s40bs_e27_v24?0"NSURL"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e31_v16?0"PLFeatureAvailability"8l
+ ___block_descriptor_48_e8_32s40r_e12_v20?0I8^B12l
+ ___block_descriptor_48_e8_32s40r_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_56_e8_32s40bs48r_e15_v16?0"NSURL"8l
+ ___block_descriptor_56_e8_32s40r48r_e37_v32?0"NSNumber"8"NSIndexSet"16^B24l
+ ___block_descriptor_56_e8_32s40s48bs_e20_v48?0Q8Q16Q24Q32Q40l
+ ___block_descriptor_56_e8_32s40s48r_e24_v16?0"PLPhotoLibrary"8l
+ ___block_descriptor_56_e8_32s40s48s_e24_v16?0"PLPhotoLibrary"8l
+ ___block_descriptor_57_e8_32s40s48bs_e27_v24?0"NSURL"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48bs_e8_v12?0B8l
+ ___block_descriptor_64_e8_32s40s48r_e53_v32?0"CPLScopedIdentifier"8"CPLRecordChange"16^B24l
+ ___block_descriptor_64_e8_32s40s48r_e71_v32?0"PLManagedObject"8"CPLScopedIdentifier"16"PLCollectionShare"24l
+ ___block_descriptor_64_e8_32s40s48s56bs_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_65_e8_32s40s48bs56bs_e31_v16?0"PLFeatureAvailability"8l
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e15_v16?0"NSURL"8l
+ ___block_descriptor_72_e8_32s40s48r56r64r_e24_v16?0"PLPhotoLibrary"8l
+ ___block_descriptor_72_e8_32s40s48r56r64r_e59_v32?0"NSManagedObjectContext"8"PLInternalResource"16^B24l
+ ___block_descriptor_72_e8_32s40s48s56r64r_e25_v24?0"NSURL"8"NSURL"16l
+ ___block_descriptor_80_e8_32s40s48s56bs64r72r_e54_v48?0"NSString"8Q16"NSURL"24"NSData"32"NSError"40l
+ ___block_descriptor_81_e8_32s40s48s56r64r72r_e27_v24?0"NSURL"8"NSError"16l
+ ___block_descriptor_81_e8_32s40s48s56s64s72bs_e86_v68?0"NSString"8"NSString"16"NSString"24q32"NSString"40I48"NSDate"52"NSError"60l
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e36_v24?0"CPLScopeChange"8"NSError"16l
+ ___block_descriptor_95_e8_32s40s48s56s64s72bs_e62_v44?0"NSObject<OS_xpc_object>"8"NSNumber"16"NSURL"24S32q36l
+ ___copy_helper_block_e8_32s40s48s56r64r72r80r88r96r104r112r120r128r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88b96b104r112r120r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88r96r104r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88r96r104r112r120r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120b128r136r144r152r160r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128b136b144b152r160r
+ ___destroy_helper_block_e8_32s40s48s56r64r72r80r88r96r104r112r120r128r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88r96r104r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88r96r104r112r120r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128r136r144r152r160r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152r160r
+ _entityNamesAllowedByRestrictedDataEntitlements:.pl_once_object_17
+ _entityNamesAllowedByRestrictedDataEntitlements:.pl_once_token_17
+ _hasChangesForCloudShared:.pl_once_object_48
+ _hasChangesForCloudShared:.pl_once_token_48
+ _kTCCServiceSiriAccess
+ _objc_msgSend$_allAssetsAreSavedToLibraryForCollectionShare:inContext:
+ _objc_msgSend$_allCriteriaToUse
+ _objc_msgSend$_applyDefaultPrefetchModeIfNeededWithCPLSettings:createOptions:
+ _objc_msgSend$_calculateDonationCountsFromSnapshot:resultHandler:
+ _objc_msgSend$_cloneResourcesForSharePlaceholderAsset:sourceAsset:shouldBakeInAdjustments:shouldFlattenLivePhoto:withPlaceholderResourceURLToSourceResourceURLMap:fileManager:photoLibrary:
+ _objc_msgSend$_collectContributorUserIdentifiersForRecords:into:completionHandler:
+ _objc_msgSend$_coordinateReadingSourcesWithError:accessor:
+ _objc_msgSend$_copyAndMarkAsLocallyAvailablePairedLivePhotoResourceForRequestedResource:requestedVideoComplement:fileCoordinator:error:
+ _objc_msgSend$_copyFileAtURL:toDestination:error:
+ _objc_msgSend$_copyProvidedFilesForItemIdentifier:providerURL:primaryDestination:videoComplementDestination:pathManager:materializesDatalessFiles:resultHandler:
+ _objc_msgSend$_copyProviderFileWantsVideoComplement:fromCoordinator:fileIdentifier:pathManager:copiedURL:inode:error:
+ _objc_msgSend$_cplParticipantForParticipant:inScopeChange:collectionShare:
+ _objc_msgSend$_cplParticipantsWithBlockedIdentitiesLast:
+ _objc_msgSend$_deactivateCPLSyncWithResetMode:reason:willBecomeNonSyncable:
+ _objc_msgSend$_defaultResult
+ _objc_msgSend$_disableACPLAfterMainScopeWipedInCloudIfNecessaryWithStatus:transaction:
+ _objc_msgSend$_enumerateUnattributedCPLContributorContentInPhotoLibrary:usingBlock:
+ _objc_msgSend$_errorForCopyFailure:sourceURL:
+ _objc_msgSend$_forcefullyInvokeCurrentManagedObjectCompletionHandler
+ _objc_msgSend$_generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:retryNumber:allowCancellationByService:clientBundleID:shouldSaveMediaConversionResultBlock:completion:
+ _objc_msgSend$_getProcessingSetURL
+ _objc_msgSend$_handleSuggestionsPreferenceChanged
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
+ _objc_msgSend$_ocrTextLineCandidatesFromTextBlockObservation:tokenizer:includeLowConfidenceText:confidenceThreshold:
+ _objc_msgSend$_ocrTextLinesFromDocumentObservation:includeLowConfidenceText:confidenceThreshold:
+ _objc_msgSend$_participatesInOTARestore
+ _objc_msgSend$_path:isContainedWithinLibraryBundle:
+ _objc_msgSend$_popBiomeDeletedAssetsIntoDetail:
+ _objc_msgSend$_processDelayedAssetsForBiomeDelete:
+ _objc_msgSend$_provideSourceURLsForBundleID:syndicationIdentifier:typeIdentifier:isLivePhoto:options:completionHandler:
+ _objc_msgSend$_restoreMissingCollectionSharePostsWithCPLSettings:
+ _objc_msgSend$_richImageCaptionDefaultsToCurrent
+ _objc_msgSend$_setKeywordsFromMetadata:
+ _objc_msgSend$_setRatingFromMetadata:
+ _objc_msgSend$_siriExclusionNotificationName
+ _objc_msgSend$_syncOutputProgress:toSourceProgress:
+ _objc_msgSend$_unpackLivePhotoBundleAtURL:primaryURL:videoComplementURL:error:
+ _objc_msgSend$_updateCachedEventLogLastEnteredDate
+ _objc_msgSend$_updateCachedLastSeenDate
+ _objc_msgSend$_updateShareParticipantWithContributorUserIdentifier:collectionShare:inPhotoLibrary:
+ _objc_msgSend$_updateStateCaptureInfo:libraryID:
+ _objc_msgSend$backgroundJobWorkerTypesMaskGuestAssetSync:personSync:syndicationSync:syndicationResourceSanitization:syndicationResourceDownload:syndicationAssetCleanup:assetStack:duplicateDetector:deferredRenderDerivativesLowPriority:deferredRenderDerivativesHighPriority:resourceAvailability:stableHash:editRenderingImage:editRenderingVideo:highPrioritySearchIndexing:lowPrioritySearchIndexing:sharedAssetContainerUpdate:assetResourceUploadJob:assetResourceUploadExtensionRunner:featureAvailability:optimizeTableThumbs:cascadeDonation:provenanceTimestamp:
+ _objc_msgSend$biomeDeletedAssetCreationDateByAssetUUID
+ _objc_msgSend$clearWasCreatedFlag
+ _objc_msgSend$computeSearchProgressForPhotoLibrary:completionHandler:
+ _objc_msgSend$confidenceForMomentEdge:
+ _objc_msgSend$containerHasBeenWipedDueToEncryptedDataReset
+ _objc_msgSend$coordinateReadingItemAtURL:options:error:byAccessor:
+ _objc_msgSend$copiedPrimaryURL
+ _objc_msgSend$copiedVideoComplementURL
+ _objc_msgSend$copyJobContentsToHoldingDirectoryWithUUID:incomingPath:job:
+ _objc_msgSend$copyToPrimaryDestination:videoComplementDestination:error:
+ _objc_msgSend$countOfSharesWithUnreadBadgeActivitySinceLastSeenDate:eventLogDate:inManagedObjectContext:
+ _objc_msgSend$countRemainingWithManagedObjectContext:
+ _objc_msgSend$criteriaNeedingProcessingInLibrary:currentCriteria:outSignalAgainDate:
+ _objc_msgSend$defaultStore
+ _objc_msgSend$donateDeleteEventForAssetCreationDateByAssetUUID:
+ _objc_msgSend$estimatedJPEGThumbnailDataLengthForWidth:height:
+ _objc_msgSend$evaluateLexemeIDs:
+ _objc_msgSend$eventLogLastEnteredDate
+ _objc_msgSend$executeQueryForSyncManager:type:startDate:endDate:itemsHandler:completionHandler:
+ _objc_msgSend$featureAnalysisLexemeCategories
+ _objc_msgSend$generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:allowCancellationByService:clientBundleID:shouldSaveMediaConversionResultBlock:completion:
+ _objc_msgSend$getCloudCacheRecordsWithLocalScopedIdentifiers:desiredProperties:completionHandler:
+ _objc_msgSend$getSearchDonationProgressInLibrary:shouldCompute:shouldReport:completionHandler:
+ _objc_msgSend$hasPersistedPrefetchMode
+ _objc_msgSend$identifiersForMissingPostsInPhotoLibrary:
+ _objc_msgSend$initWithAsset:resourceType:version:recipeID:data:mediaMetadataType:
+ _objc_msgSend$initWithFilePresenter:
+ _objc_msgSend$initWithIdentifier:name:version:
+ _objc_msgSend$initWithLexemes:versionProvider:
+ _objc_msgSend$initWithLine:words:confidence:isLowConfidence:
+ _objc_msgSend$initWithMessage:libraryPath:
+ _objc_msgSend$initWithSourceURL:videoComplementSourceURL:pathManager:materializesDatalessFiles:
+ _objc_msgSend$initWithZeroWorkItemsForCurrentCriteria
+ _objc_msgSend$isAuthorizedAssetUUID:inManagedObjectContext:
+ _objc_msgSend$isEntitledForPrivatePhotosTCCForToken:
+ _objc_msgSend$isListening
+ _objc_msgSend$isLowConfidence
+ _objc_msgSend$isMomentLibrary
+ _objc_msgSend$kvsListener
+ _objc_msgSend$kvsListenerDidUpdateEventLogLastEnteredDate:
+ _objc_msgSend$kvsListenerDidUpdateLastSeenDate:
+ _objc_msgSend$lastEditedDate
+ _objc_msgSend$lastSeenDate
+ _objc_msgSend$lastUserEditedDate
+ _objc_msgSend$libraryPath
+ _objc_msgSend$linkAssets:
+ _objc_msgSend$linkCPLContributorContentWithUserIdentifiers:inPhotoLibrary:
+ _objc_msgSend$materializesDatalessFiles
+ _objc_msgSend$migrateLimitedLibraryFetchFilterFromApplicationIdentifier:toApplicationIdentifier:inManagedObjectContext:error:
+ _objc_msgSend$notificationPredicateForFilter:
+ _objc_msgSend$ocrTextLinesFromDocumentObservation:confidenceThreshold:
+ _objc_msgSend$ocrTextLinesFromDocumentObservation:includeLowConfidenceText:
+ _objc_msgSend$orphanedCPLContributorRecordsInPhotoLibrary:
+ _objc_msgSend$path:isSubpathOfPhotoDirectoryWithType:
+ _objc_msgSend$pendingCriteriaInLibrary:currentCriteria:outSignalAgainDate:
+ _objc_msgSend$pendingWorkItemsInLibrary:currentCriteria:
+ _objc_msgSend$performTransaction:withName:
+ _objc_msgSend$predicateForMigratedCPLCollectionShares
+ _objc_msgSend$predicateForPostsFromOthersCreatedAfterSubscriptionSinceDate:
+ _objc_msgSend$predicateToExcludePostsWithoutAssets
+ _objc_msgSend$provideFileURLAndUnwrapLivePhotoIfNeededForItemIdentifiersWithBundleIDs:destURLs:pathManager:options:resultHandler:completionHandler:
+ _objc_msgSend$reconcileOrphanedRelationshipsWithCPLCollectionShare:
+ _objc_msgSend$recordAssetForBiomeDelete:
+ _objc_msgSend$requestTapToRadarAuthorizationWithCompletion:
+ _objc_msgSend$restoreMissingPostsWithCPLRecords:inPhotoLibrary:
+ _objc_msgSend$scopedIdentifierWithScopeIdentifier:
+ _objc_msgSend$setAllowEmbeddedThumbnails:
+ _objc_msgSend$setBiomeDeletedAssetCreationDateByAssetUUID:
+ _objc_msgSend$setDiagnosticExtensionIdentifiers:
+ _objc_msgSend$setDisplayReason:
+ _objc_msgSend$setIsListening:
+ _objc_msgSend$setLastEditedDate:
+ _objc_msgSend$setLastUserEditedDate:
+ _objc_msgSend$setPrefetchModeSchedulingResourceUpdate:error:
+ _objc_msgSend$setProcessName:
+ _objc_msgSend$setShareContributorUserIdentifier:
+ _objc_msgSend$setUserInitiated:
+ _objc_msgSend$setZeroWorkItemsForCurrentCriteria:
+ _objc_msgSend$setupPlaceholderAssetWithRequiredPropertiesFromSourceAsset:placeholderAssetUUID:bundleScope:share:importSessionID:bakeInAdjustmentsFromSourceAsset:flattenLivePhoto:copyTitleDescriptionAndKeywords:copyCameraProcessingAdjustmentResources:copyLocationData:copyProvenanceData:isCurrentUser:library:
+ _objc_msgSend$skipAllBackgroundActionsForNewlyCreatedLibraryIfNeededWithPathManager:error:
+ _objc_msgSend$sourceURL
+ _objc_msgSend$starRating
+ _objc_msgSend$stateCaptureDictionariesForAllHandlers
+ _objc_msgSend$supportsSearchProgressReporting
+ _objc_msgSend$transitionToUninterruptible
+ _objc_msgSend$tryPreparingForReplacementWithNewResponder:existingResponders:existingProgress:
+ _objc_msgSend$updateAccessRequestForParticipant:toAcceptanceStatus:collectionShare:completionHandler:
+ _objc_msgSend$updateAccessRequestForShareParticipantUUID:toAcceptanceStatus:photoLibrary:completionHandler:
+ _objc_msgSend$updateImageExtendedGenerativeAttributesFromMetadata:policy:
+ _objc_msgSend$updatePostAssetsInPhotoLibrary:
+ _objc_msgSend$videoComplementFilename
+ _objc_msgSend$videoComplementSourceURL
+ _objc_msgSend$wasCreated
+ _objc_msgSend$workItemsNeedingProcessingInLibrary:currentCriteria:
+ _objc_msgSend$zeroWorkItemsForCurrentCriteria
+ _tcc_service_get_name
+ _tcc_service_singleton_for_CF_name
+ changeNotificationObjectIDKeys.pl_once_object_45
+ changeNotificationObjectIDKeys.pl_once_token_45
+ changeNotificationObjectIDMutationKeys.pl_once_object_44
+ changeNotificationObjectIDMutationKeys.pl_once_token_44
+ changeNotificationObjectKeys.pl_once_object_43
+ changeNotificationObjectKeys.pl_once_token_43
+ predicateToExcludeAssetsMissingMasterThumbnailsWithThumbnailIndexKeyPath:.pl_once_object_15
+ predicateToExcludeAssetsMissingMasterThumbnailsWithThumbnailIndexKeyPath:.pl_once_token_15
+ predicateToExcludeCameraAutoAdjustments.pl_once_object_16
+ predicateToExcludeCameraAutoAdjustments.pl_once_token_16
+ predicateToExcludeHiddenAssetsWithHiddenKeyPath:.pl_once_object_11
+ predicateToExcludeHiddenAssetsWithHiddenKeyPath:.pl_once_token_11
+ predicateToExcludeNonvisibleBurstAssets.pl_once_object_13
+ predicateToExcludeNonvisibleBurstAssets.pl_once_token_13
+ predicateToExcludeNonvisibleBurstAssetsWithAvalanchePickTypeKeyPath:.pl_once_object_14
+ predicateToExcludeNonvisibleBurstAssetsWithAvalanchePickTypeKeyPath:.pl_once_token_14
+ predicateToExcludePostsWithoutAssets.pl_once_object_20
+ predicateToExcludePostsWithoutAssets.pl_once_token_20
+ predicateToExcludeRestrictedLockedAssets.pl_once_object_12
+ predicateToExcludeRestrictedLockedAssets.pl_once_token_12
+ predicateToExcludeTrashedAssets.pl_once_object_9
+ predicateToExcludeTrashedAssets.pl_once_token_9
+ predicateToExcludeTrashedAssetsWithTrashedStateKeyPath:.pl_once_object_10
+ predicateToExcludeTrashedAssetsWithTrashedStateKeyPath:.pl_once_token_10
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
- +[PLManagedObjectContext _isAssetLibraryFetchingAlbum:]
- +[PLManagedObjectContext assetsLibraryLoggingEnabled]
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
- +[PLSearchOCRUtilities _ocrTextLineCandidatesFromTextBlockObservation:tokenizer:allowLowConfidence:]
- +[PLSearchOCRUtilities _ocrTextLinesFromDocumentObservation:allowLowConfidence:]
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
- -[PLAssetsdLibraryService transferAssetsWithUuids:fromLibraryURL:transferOptions:reply:]
- -[PLAssetsdLibraryService transferPersonsWithUuids:fromLibraryURL:transferOptions:reply:]
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
- -[PLCloudPhotoLibraryManager _deactivateCPLSyncWithResetMode:]
- -[PLCloudPhotoLibraryManager _deactivateCPLSyncWithResetMode:willBecomeNonSyncableReason:]
- -[PLCloudPhotoLibraryManager _disableaCPLAfterZoneWipedInCloudIfNecessaryWithStatus:transaction:]
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
- -[PLManagedObjectContext _notifyALAssetsLibraryWithChanges:usingObjectIDs:]
- -[PLManagedObjectContext isBackingALAssetsLibrary]
- -[PLManagedObjectContext resetAllFetchingAlbums]
- -[PLManagedObjectContext setIsBackingALAssetsLibrary:]
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
- -[PLSearchIndexingRebuildEngine _startRebuildForLibrary:]
- -[PLSearchOCRTextLineCandidate initWithLine:words:confidence:]
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
- -[PLSharePost setSkipAssetRelationshipValidationOnSave:]
- -[PLSharePost skipAssetRelationshipValidationOnSave]
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
- GCC_except_table10024
- GCC_except_table10055
- GCC_except_table10056
- GCC_except_table10058
- GCC_except_table10061
- GCC_except_table10064
- GCC_except_table10066
- GCC_except_table10068
- GCC_except_table10069
- GCC_except_table10135
- GCC_except_table10140
- GCC_except_table10144
- GCC_except_table10161
- GCC_except_table10168
- GCC_except_table10180
- GCC_except_table10182
- GCC_except_table10196
- GCC_except_table10255
- GCC_except_table10289
- GCC_except_table10293
- GCC_except_table10305
- GCC_except_table10317
- GCC_except_table10331
- GCC_except_table10345
- GCC_except_table10347
- GCC_except_table10354
- GCC_except_table10391
- GCC_except_table10396
- GCC_except_table10411
- GCC_except_table10421
- GCC_except_table1043
- GCC_except_table10433
- GCC_except_table10444
- GCC_except_table10452
- GCC_except_table10473
- GCC_except_table10486
- GCC_except_table10497
- GCC_except_table10576
- GCC_except_table10582
- GCC_except_table10584
- GCC_except_table10588
- GCC_except_table10590
- GCC_except_table10596
- GCC_except_table10600
- GCC_except_table10602
- GCC_except_table10608
- GCC_except_table10637
- GCC_except_table10644
- GCC_except_table1065
- GCC_except_table1066
- GCC_except_table10664
- GCC_except_table10695
- GCC_except_table10698
- GCC_except_table10751
- GCC_except_table10802
- GCC_except_table10814
- GCC_except_table10816
- GCC_except_table10836
- GCC_except_table10838
- GCC_except_table10849
- GCC_except_table10854
- GCC_except_table10859
- GCC_except_table10867
- GCC_except_table10887
- GCC_except_table11001
- GCC_except_table11044
- GCC_except_table11136
- GCC_except_table11142
- GCC_except_table11148
- GCC_except_table11150
- GCC_except_table11152
- GCC_except_table11154
- GCC_except_table11156
- GCC_except_table11158
- GCC_except_table11160
- GCC_except_table11162
- GCC_except_table11164
- GCC_except_table11166
- GCC_except_table11169
- GCC_except_table11172
- GCC_except_table11176
- GCC_except_table11179
- GCC_except_table11182
- GCC_except_table11184
- GCC_except_table11186
- GCC_except_table11188
- GCC_except_table11190
- GCC_except_table11192
- GCC_except_table11193
- GCC_except_table11196
- GCC_except_table11199
- GCC_except_table11202
- GCC_except_table11205
- GCC_except_table11207
- GCC_except_table11210
- GCC_except_table11213
- GCC_except_table11216
- GCC_except_table11217
- GCC_except_table11221
- GCC_except_table11226
- GCC_except_table11227
- GCC_except_table11229
- GCC_except_table11230
- GCC_except_table11231
- GCC_except_table11232
- GCC_except_table11233
- GCC_except_table11235
- GCC_except_table11236
- GCC_except_table11238
- GCC_except_table11239
- GCC_except_table1124
- GCC_except_table11240
- GCC_except_table11242
- GCC_except_table11243
- GCC_except_table11244
- GCC_except_table11245
- GCC_except_table11246
- GCC_except_table11247
- GCC_except_table11250
- GCC_except_table11251
- GCC_except_table11254
- GCC_except_table11256
- GCC_except_table11258
- GCC_except_table11260
- GCC_except_table11263
- GCC_except_table11264
- GCC_except_table11266
- GCC_except_table11338
- GCC_except_table11342
- GCC_except_table11353
- GCC_except_table11424
- GCC_except_table1145
- GCC_except_table11512
- GCC_except_table11553
- GCC_except_table11565
- GCC_except_table11665
- GCC_except_table11670
- GCC_except_table11693
- GCC_except_table11746
- GCC_except_table11802
- GCC_except_table12011
- GCC_except_table1203
- GCC_except_table12052
- GCC_except_table122
- GCC_except_table1226
- GCC_except_table12279
- GCC_except_table12312
- GCC_except_table1232
- GCC_except_table12337
- GCC_except_table12338
- GCC_except_table12339
- GCC_except_table12340
- GCC_except_table12342
- GCC_except_table12344
- GCC_except_table12359
- GCC_except_table1237
- GCC_except_table1243
- GCC_except_table12442
- GCC_except_table12454
- GCC_except_table12460
- GCC_except_table12465
- GCC_except_table12470
- GCC_except_table12475
- GCC_except_table12479
- GCC_except_table12483
- GCC_except_table12493
- GCC_except_table1250
- GCC_except_table12503
- GCC_except_table12508
- GCC_except_table12513
- GCC_except_table12517
- GCC_except_table12522
- GCC_except_table12527
- GCC_except_table12533
- GCC_except_table12543
- GCC_except_table12546
- GCC_except_table12561
- GCC_except_table12572
- GCC_except_table12590
- GCC_except_table12606
- GCC_except_table12666
- GCC_except_table12673
- GCC_except_table12675
- GCC_except_table12677
- GCC_except_table12679
- GCC_except_table12683
- GCC_except_table12685
- GCC_except_table12688
- GCC_except_table1269
- GCC_except_table12690
- GCC_except_table12699
- GCC_except_table1270
- GCC_except_table12708
- GCC_except_table12711
- GCC_except_table12715
- GCC_except_table12720
- GCC_except_table12726
- GCC_except_table12730
- GCC_except_table12744
- GCC_except_table12746
- GCC_except_table12748
- GCC_except_table12766
- GCC_except_table12768
- GCC_except_table12770
- GCC_except_table12772
- GCC_except_table12775
- GCC_except_table12777
- GCC_except_table12779
- GCC_except_table1278
- GCC_except_table12781
- GCC_except_table12783
- GCC_except_table12786
- GCC_except_table12789
- GCC_except_table12791
- GCC_except_table12793
- GCC_except_table12795
- GCC_except_table12797
- GCC_except_table12800
- GCC_except_table12802
- GCC_except_table12804
- GCC_except_table12806
- GCC_except_table12808
- GCC_except_table12809
- GCC_except_table12820
- GCC_except_table12826
- GCC_except_table12852
- GCC_except_table12856
- GCC_except_table12857
- GCC_except_table12865
- GCC_except_table12894
- GCC_except_table12923
- GCC_except_table130
- GCC_except_table1300
- GCC_except_table13013
- GCC_except_table13128
- GCC_except_table13130
- GCC_except_table13134
- GCC_except_table13152
- GCC_except_table13156
- GCC_except_table13163
- GCC_except_table13169
- GCC_except_table1318
- GCC_except_table13180
- GCC_except_table13185
- GCC_except_table13264
- GCC_except_table13280
- GCC_except_table13285
- GCC_except_table13289
- GCC_except_table13306
- GCC_except_table13308
- GCC_except_table13315
- GCC_except_table13317
- GCC_except_table13319
- GCC_except_table13324
- GCC_except_table13368
- GCC_except_table13377
- GCC_except_table13383
- GCC_except_table13385
- GCC_except_table13387
- GCC_except_table13430
- GCC_except_table13543
- GCC_except_table1355
- GCC_except_table13564
- GCC_except_table13571
- GCC_except_table13575
- GCC_except_table13622
- GCC_except_table13706
- GCC_except_table1371
- GCC_except_table13731
- GCC_except_table13743
- GCC_except_table1378
- GCC_except_table13797
- GCC_except_table13818
- GCC_except_table13821
- GCC_except_table13825
- GCC_except_table13828
- GCC_except_table13830
- GCC_except_table13834
- GCC_except_table13837
- GCC_except_table13846
- GCC_except_table1385
- GCC_except_table1387
- GCC_except_table13895
- GCC_except_table13913
- GCC_except_table13919
- GCC_except_table13941
- GCC_except_table1402
- GCC_except_table14036
- GCC_except_table14091
- GCC_except_table141
- GCC_except_table14103
- GCC_except_table14107
- GCC_except_table14123
- GCC_except_table14131
- GCC_except_table14165
- GCC_except_table14167
- GCC_except_table14169
- GCC_except_table14188
- GCC_except_table14279
- GCC_except_table14284
- GCC_except_table14307
- GCC_except_table14320
- GCC_except_table14322
- GCC_except_table14324
- GCC_except_table14432
- GCC_except_table14433
- GCC_except_table14437
- GCC_except_table14470
- GCC_except_table1448
- GCC_except_table14491
- GCC_except_table14502
- GCC_except_table14503
- GCC_except_table14504
- GCC_except_table14505
- GCC_except_table14506
- GCC_except_table14507
- GCC_except_table14508
- GCC_except_table14509
- GCC_except_table14510
- GCC_except_table14511
- GCC_except_table14512
- GCC_except_table14513
- GCC_except_table14514
- GCC_except_table14515
- GCC_except_table14519
- GCC_except_table14523
- GCC_except_table14579
- GCC_except_table14585
- GCC_except_table14605
- GCC_except_table14610
- GCC_except_table14615
- GCC_except_table14619
- GCC_except_table14653
- GCC_except_table14657
- GCC_except_table14661
- GCC_except_table14672
- GCC_except_table14683
- GCC_except_table14719
- GCC_except_table14769
- GCC_except_table14776
- GCC_except_table14793
- GCC_except_table14840
- GCC_except_table14864
- GCC_except_table1488
- GCC_except_table14886
- GCC_except_table1490
- GCC_except_table1499
- GCC_except_table1501
- GCC_except_table15019
- GCC_except_table1509
- GCC_except_table15100
- GCC_except_table15162
- GCC_except_table15179
- GCC_except_table15186
- GCC_except_table15190
- GCC_except_table15209
- GCC_except_table15298
- GCC_except_table15305
- GCC_except_table15307
- GCC_except_table15308
- GCC_except_table15311
- GCC_except_table15313
- GCC_except_table15320
- GCC_except_table1539
- GCC_except_table1547
- GCC_except_table15498
- GCC_except_table15577
- GCC_except_table15664
- GCC_except_table1567
- GCC_except_table15765
- GCC_except_table15766
- GCC_except_table1577
- GCC_except_table15773
- GCC_except_table15775
- GCC_except_table15780
- GCC_except_table15790
- GCC_except_table15792
- GCC_except_table15818
- GCC_except_table1582
- GCC_except_table15837
- GCC_except_table15848
- GCC_except_table15875
- GCC_except_table15915
- GCC_except_table15919
- GCC_except_table15920
- GCC_except_table15986
- GCC_except_table15990
- GCC_except_table15994
- GCC_except_table15999
- GCC_except_table16155
- GCC_except_table16185
- GCC_except_table16202
- GCC_except_table16207
- GCC_except_table16210
- GCC_except_table16212
- GCC_except_table16217
- GCC_except_table16218
- GCC_except_table16223
- GCC_except_table16224
- GCC_except_table16226
- GCC_except_table16236
- GCC_except_table16240
- GCC_except_table16243
- GCC_except_table16247
- GCC_except_table16249
- GCC_except_table16251
- GCC_except_table16253
- GCC_except_table16256
- GCC_except_table16259
- GCC_except_table16306
- GCC_except_table1631
- GCC_except_table16321
- GCC_except_table16324
- GCC_except_table16341
- GCC_except_table16345
- GCC_except_table16350
- GCC_except_table16355
- GCC_except_table16358
- GCC_except_table16360
- GCC_except_table16367
- GCC_except_table16371
- GCC_except_table16468
- GCC_except_table16472
- GCC_except_table16474
- GCC_except_table16476
- GCC_except_table16499
- GCC_except_table16500
- GCC_except_table16507
- GCC_except_table16516
- GCC_except_table16525
- GCC_except_table16530
- GCC_except_table16534
- GCC_except_table16547
- GCC_except_table16606
- GCC_except_table16608
- GCC_except_table16702
- GCC_except_table16763
- GCC_except_table16778
- GCC_except_table1678
- GCC_except_table16886
- GCC_except_table16907
- GCC_except_table1691
- GCC_except_table16913
- GCC_except_table16918
- GCC_except_table16926
- GCC_except_table16955
- GCC_except_table16967
- GCC_except_table17011
- GCC_except_table1702
- GCC_except_table17079
- GCC_except_table17087
- GCC_except_table17097
- GCC_except_table17109
- GCC_except_table17123
- GCC_except_table17129
- GCC_except_table17139
- GCC_except_table17152
- GCC_except_table17162
- GCC_except_table17172
- GCC_except_table17202
- GCC_except_table17206
- GCC_except_table17208
- GCC_except_table17210
- GCC_except_table17271
- GCC_except_table17274
- GCC_except_table17323
- GCC_except_table17354
- GCC_except_table17361
- GCC_except_table17427
- GCC_except_table17437
- GCC_except_table17449
- GCC_except_table17450
- GCC_except_table17454
- GCC_except_table17457
- GCC_except_table17461
- GCC_except_table17464
- GCC_except_table17465
- GCC_except_table17466
- GCC_except_table17467
- GCC_except_table17468
- GCC_except_table17470
- GCC_except_table17502
- GCC_except_table17508
- GCC_except_table17592
- GCC_except_table17629
- GCC_except_table17643
- GCC_except_table17695
- GCC_except_table17713
- GCC_except_table17753
- GCC_except_table17758
- GCC_except_table17797
- GCC_except_table17812
- GCC_except_table17824
- GCC_except_table17849
- GCC_except_table17880
- GCC_except_table17882
- GCC_except_table17917
- GCC_except_table17930
- GCC_except_table17971
- GCC_except_table17996
- GCC_except_table18012
- GCC_except_table18013
- GCC_except_table18040
- GCC_except_table18059
- GCC_except_table18097
- GCC_except_table18163
- GCC_except_table18188
- GCC_except_table18190
- GCC_except_table18192
- GCC_except_table18194
- GCC_except_table18196
- GCC_except_table18198
- GCC_except_table18202
- GCC_except_table18251
- GCC_except_table18391
- GCC_except_table18450
- GCC_except_table18461
- GCC_except_table18463
- GCC_except_table1847
- GCC_except_table185
- GCC_except_table18520
- GCC_except_table1853
- GCC_except_table18531
- GCC_except_table18545
- GCC_except_table18554
- GCC_except_table18571
- GCC_except_table18613
- GCC_except_table18642
- GCC_except_table18645
- GCC_except_table18662
- GCC_except_table18663
- GCC_except_table18668
- GCC_except_table18710
- GCC_except_table18728
- GCC_except_table18752
- GCC_except_table18760
- GCC_except_table18762
- GCC_except_table18764
- GCC_except_table18767
- GCC_except_table18768
- GCC_except_table18769
- GCC_except_table18770
- GCC_except_table18771
- GCC_except_table18772
- GCC_except_table18773
- GCC_except_table18775
- GCC_except_table18780
- GCC_except_table18784
- GCC_except_table18785
- GCC_except_table18788
- GCC_except_table18790
- GCC_except_table18792
- GCC_except_table18794
- GCC_except_table18795
- GCC_except_table18796
- GCC_except_table18798
- GCC_except_table18800
- GCC_except_table18801
- GCC_except_table18804
- GCC_except_table18855
- GCC_except_table18872
- GCC_except_table19080
- GCC_except_table19085
- GCC_except_table19088
- GCC_except_table19109
- GCC_except_table19111
- GCC_except_table19112
- GCC_except_table19113
- GCC_except_table19117
- GCC_except_table19118
- GCC_except_table19119
- GCC_except_table19121
- GCC_except_table19122
- GCC_except_table19127
- GCC_except_table19130
- GCC_except_table19132
- GCC_except_table19134
- GCC_except_table19136
- GCC_except_table19139
- GCC_except_table19144
- GCC_except_table19149
- GCC_except_table19152
- GCC_except_table19154
- GCC_except_table19160
- GCC_except_table19163
- GCC_except_table19166
- GCC_except_table19169
- GCC_except_table19171
- GCC_except_table19175
- GCC_except_table19179
- GCC_except_table19180
- GCC_except_table19187
- GCC_except_table19190
- GCC_except_table19192
- GCC_except_table19207
- GCC_except_table19217
- GCC_except_table19221
- GCC_except_table19229
- GCC_except_table19233
- GCC_except_table19235
- GCC_except_table19237
- GCC_except_table19239
- GCC_except_table19243
- GCC_except_table19244
- GCC_except_table19245
- GCC_except_table19249
- GCC_except_table19250
- GCC_except_table19255
- GCC_except_table19257
- GCC_except_table19260
- GCC_except_table19261
- GCC_except_table19264
- GCC_except_table19266
- GCC_except_table19268
- GCC_except_table19269
- GCC_except_table19270
- GCC_except_table19273
- GCC_except_table19276
- GCC_except_table19279
- GCC_except_table19282
- GCC_except_table19285
- GCC_except_table19287
- GCC_except_table19289
- GCC_except_table19291
- GCC_except_table19292
- GCC_except_table19294
- GCC_except_table19295
- GCC_except_table19306
- GCC_except_table19310
- GCC_except_table19314
- GCC_except_table19413
- GCC_except_table19419
- GCC_except_table19432
- GCC_except_table19435
- GCC_except_table19436
- GCC_except_table19437
- GCC_except_table19438
- GCC_except_table19439
- GCC_except_table19440
- GCC_except_table19448
- GCC_except_table19461
- GCC_except_table19463
- GCC_except_table19573
- GCC_except_table19585
- GCC_except_table19604
- GCC_except_table19679
- GCC_except_table19682
- GCC_except_table19684
- GCC_except_table19689
- GCC_except_table19692
- GCC_except_table19700
- GCC_except_table19721
- GCC_except_table19727
- GCC_except_table19731
- GCC_except_table19733
- GCC_except_table19737
- GCC_except_table19747
- GCC_except_table19752
- GCC_except_table19754
- GCC_except_table19762
- GCC_except_table19763
- GCC_except_table19766
- GCC_except_table19767
- GCC_except_table19770
- GCC_except_table198
- GCC_except_table19835
- GCC_except_table19900
- GCC_except_table19918
- GCC_except_table19990
- GCC_except_table19994
- GCC_except_table20
- GCC_except_table20016
- GCC_except_table20020
- GCC_except_table20022
- GCC_except_table20024
- GCC_except_table20038
- GCC_except_table20180
- GCC_except_table20191
- GCC_except_table20228
- GCC_except_table20234
- GCC_except_table20238
- GCC_except_table20243
- GCC_except_table2026
- GCC_except_table20269
- GCC_except_table20303
- GCC_except_table20312
- GCC_except_table20318
- GCC_except_table2032
- GCC_except_table20321
- GCC_except_table20326
- GCC_except_table20330
- GCC_except_table20335
- GCC_except_table20341
- GCC_except_table20358
- GCC_except_table20364
- GCC_except_table20377
- GCC_except_table20526
- GCC_except_table20530
- GCC_except_table20565
- GCC_except_table20569
- GCC_except_table20573
- GCC_except_table20575
- GCC_except_table20603
- GCC_except_table20643
- GCC_except_table20647
- GCC_except_table20651
- GCC_except_table20655
- GCC_except_table20659
- GCC_except_table20663
- GCC_except_table20667
- GCC_except_table20671
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
- GCC_except_table20719
- GCC_except_table20723
- GCC_except_table20760
- GCC_except_table20763
- GCC_except_table20771
- GCC_except_table20799
- GCC_except_table20803
- GCC_except_table20804
- GCC_except_table20805
- GCC_except_table20811
- GCC_except_table20824
- GCC_except_table20892
- GCC_except_table20943
- GCC_except_table20949
- GCC_except_table20992
- GCC_except_table20996
- GCC_except_table21012
- GCC_except_table21040
- GCC_except_table21065
- GCC_except_table21069
- GCC_except_table21115
- GCC_except_table21132
- GCC_except_table21150
- GCC_except_table21156
- GCC_except_table21165
- GCC_except_table21166
- GCC_except_table21170
- GCC_except_table21171
- GCC_except_table21175
- GCC_except_table21177
- GCC_except_table21182
- GCC_except_table21183
- GCC_except_table21185
- GCC_except_table21193
- GCC_except_table21199
- GCC_except_table21200
- GCC_except_table21201
- GCC_except_table21207
- GCC_except_table21209
- GCC_except_table21212
- GCC_except_table21213
- GCC_except_table21216
- GCC_except_table21217
- GCC_except_table21220
- GCC_except_table21221
- GCC_except_table21227
- GCC_except_table21229
- GCC_except_table21231
- GCC_except_table21233
- GCC_except_table21235
- GCC_except_table21237
- GCC_except_table21239
- GCC_except_table21241
- GCC_except_table21243
- GCC_except_table21245
- GCC_except_table21250
- GCC_except_table21254
- GCC_except_table21265
- GCC_except_table21398
- GCC_except_table21411
- GCC_except_table21417
- GCC_except_table21435
- GCC_except_table21537
- GCC_except_table21610
- GCC_except_table21630
- GCC_except_table21640
- GCC_except_table21700
- GCC_except_table21817
- GCC_except_table21818
- GCC_except_table21829
- GCC_except_table21830
- GCC_except_table21850
- GCC_except_table21852
- GCC_except_table21859
- GCC_except_table21877
- GCC_except_table21887
- GCC_except_table21905
- GCC_except_table21953
- GCC_except_table21960
- GCC_except_table21976
- GCC_except_table22030
- GCC_except_table22046
- GCC_except_table22063
- GCC_except_table22068
- GCC_except_table22080
- GCC_except_table22082
- GCC_except_table22111
- GCC_except_table22167
- GCC_except_table22179
- GCC_except_table22181
- GCC_except_table222
- GCC_except_table22212
- GCC_except_table22224
- GCC_except_table22229
- GCC_except_table22266
- GCC_except_table22279
- GCC_except_table22282
- GCC_except_table22310
- GCC_except_table22341
- GCC_except_table22430
- GCC_except_table22476
- GCC_except_table22480
- GCC_except_table22482
- GCC_except_table22484
- GCC_except_table22511
- GCC_except_table22583
- GCC_except_table22584
- GCC_except_table2261
- GCC_except_table22624
- GCC_except_table22664
- GCC_except_table22731
- GCC_except_table2280
- GCC_except_table2285
- GCC_except_table2293
- GCC_except_table2296
- GCC_except_table23138
- GCC_except_table2322
- GCC_except_table2327
- GCC_except_table23437
- GCC_except_table23449
- GCC_except_table2345
- GCC_except_table23458
- GCC_except_table2347
- GCC_except_table23505
- GCC_except_table23509
- GCC_except_table23577
- GCC_except_table23593
- GCC_except_table23694
- GCC_except_table23703
- GCC_except_table23733
- GCC_except_table23795
- GCC_except_table23809
- GCC_except_table23810
- GCC_except_table2384
- GCC_except_table23877
- GCC_except_table23895
- GCC_except_table23902
- GCC_except_table23926
- GCC_except_table2400
- GCC_except_table24105
- GCC_except_table24111
- GCC_except_table24130
- GCC_except_table24134
- GCC_except_table24213
- GCC_except_table24251
- GCC_except_table24254
- GCC_except_table24258
- GCC_except_table24301
- GCC_except_table24302
- GCC_except_table24368
- GCC_except_table24371
- GCC_except_table24386
- GCC_except_table24391
- GCC_except_table24400
- GCC_except_table24409
- GCC_except_table24411
- GCC_except_table24415
- GCC_except_table24422
- GCC_except_table24438
- GCC_except_table24445
- GCC_except_table24472
- GCC_except_table246
- GCC_except_table24661
- GCC_except_table24665
- GCC_except_table24672
- GCC_except_table24674
- GCC_except_table24675
- GCC_except_table24678
- GCC_except_table24679
- GCC_except_table24681
- GCC_except_table24683
- GCC_except_table24685
- GCC_except_table24692
- GCC_except_table24695
- GCC_except_table24696
- GCC_except_table24697
- GCC_except_table24700
- GCC_except_table24701
- GCC_except_table24702
- GCC_except_table24732
- GCC_except_table24735
- GCC_except_table24761
- GCC_except_table24767
- GCC_except_table24772
- GCC_except_table24776
- GCC_except_table2483
- GCC_except_table24846
- GCC_except_table24848
- GCC_except_table24850
- GCC_except_table24852
- GCC_except_table24854
- GCC_except_table24862
- GCC_except_table24864
- GCC_except_table24878
- GCC_except_table24904
- GCC_except_table24907
- GCC_except_table24914
- GCC_except_table24916
- GCC_except_table24918
- GCC_except_table24920
- GCC_except_table24924
- GCC_except_table24928
- GCC_except_table24944
- GCC_except_table24947
- GCC_except_table24951
- GCC_except_table24955
- GCC_except_table24965
- GCC_except_table24970
- GCC_except_table24974
- GCC_except_table24976
- GCC_except_table24978
- GCC_except_table24980
- GCC_except_table24988
- GCC_except_table24992
- GCC_except_table24996
- GCC_except_table25000
- GCC_except_table25002
- GCC_except_table25038
- GCC_except_table25054
- GCC_except_table25073
- GCC_except_table25101
- GCC_except_table25103
- GCC_except_table25128
- GCC_except_table25131
- GCC_except_table25134
- GCC_except_table25191
- GCC_except_table25249
- GCC_except_table25253
- GCC_except_table25256
- GCC_except_table25259
- GCC_except_table25266
- GCC_except_table25292
- GCC_except_table25295
- GCC_except_table25307
- GCC_except_table25311
- GCC_except_table25327
- GCC_except_table25333
- GCC_except_table25337
- GCC_except_table25340
- GCC_except_table2536
- GCC_except_table25362
- GCC_except_table25371
- GCC_except_table25374
- GCC_except_table25377
- GCC_except_table25384
- GCC_except_table25392
- GCC_except_table25393
- GCC_except_table25394
- GCC_except_table25401
- GCC_except_table25494
- GCC_except_table25495
- GCC_except_table25496
- GCC_except_table25497
- GCC_except_table25501
- GCC_except_table25505
- GCC_except_table25506
- GCC_except_table25507
- GCC_except_table25510
- GCC_except_table25540
- GCC_except_table25548
- GCC_except_table25552
- GCC_except_table2556
- GCC_except_table25629
- GCC_except_table25633
- GCC_except_table25641
- GCC_except_table25657
- GCC_except_table2566
- GCC_except_table25677
- GCC_except_table25681
- GCC_except_table2572
- GCC_except_table25805
- GCC_except_table25814
- GCC_except_table25817
- GCC_except_table25820
- GCC_except_table25823
- GCC_except_table25829
- GCC_except_table25832
- GCC_except_table25835
- GCC_except_table25838
- GCC_except_table25841
- GCC_except_table25844
- GCC_except_table25847
- GCC_except_table25850
- GCC_except_table25853
- GCC_except_table25856
- GCC_except_table25859
- GCC_except_table25862
- GCC_except_table25865
- GCC_except_table25868
- GCC_except_table25871
- GCC_except_table25874
- GCC_except_table25877
- GCC_except_table25883
- GCC_except_table25886
- GCC_except_table25889
- GCC_except_table25892
- GCC_except_table25898
- GCC_except_table25904
- GCC_except_table25907
- GCC_except_table25910
- GCC_except_table25913
- GCC_except_table25916
- GCC_except_table25919
- GCC_except_table25922
- GCC_except_table25925
- GCC_except_table25928
- GCC_except_table25931
- GCC_except_table25934
- GCC_except_table25937
- GCC_except_table25940
- GCC_except_table25943
- GCC_except_table25946
- GCC_except_table25952
- GCC_except_table25955
- GCC_except_table25961
- GCC_except_table25970
- GCC_except_table25973
- GCC_except_table25976
- GCC_except_table25979
- GCC_except_table25982
- GCC_except_table25985
- GCC_except_table25988
- GCC_except_table25991
- GCC_except_table25994
- GCC_except_table25997
- GCC_except_table26000
- GCC_except_table26003
- GCC_except_table26012
- GCC_except_table26015
- GCC_except_table26018
- GCC_except_table26021
- GCC_except_table26024
- GCC_except_table26027
- GCC_except_table26085
- GCC_except_table26088
- GCC_except_table26091
- GCC_except_table26129
- GCC_except_table26135
- GCC_except_table26183
- GCC_except_table26215
- GCC_except_table26220
- GCC_except_table26222
- GCC_except_table26224
- GCC_except_table26270
- GCC_except_table26320
- GCC_except_table26328
- GCC_except_table26333
- GCC_except_table26344
- GCC_except_table2635
- GCC_except_table26372
- GCC_except_table26374
- GCC_except_table2641
- GCC_except_table2642
- GCC_except_table26508
- GCC_except_table26514
- GCC_except_table26536
- GCC_except_table26575
- GCC_except_table26578
- GCC_except_table26584
- GCC_except_table26589
- GCC_except_table26593
- GCC_except_table26601
- GCC_except_table26628
- GCC_except_table26634
- GCC_except_table26636
- GCC_except_table26677
- GCC_except_table26821
- GCC_except_table26825
- GCC_except_table26828
- GCC_except_table26830
- GCC_except_table26942
- GCC_except_table27137
- GCC_except_table27144
- GCC_except_table27148
- GCC_except_table27159
- GCC_except_table27167
- GCC_except_table27169
- GCC_except_table27174
- GCC_except_table27176
- GCC_except_table27190
- GCC_except_table27195
- GCC_except_table27199
- GCC_except_table27219
- GCC_except_table2794
- GCC_except_table2796
- GCC_except_table2807
- GCC_except_table2836
- GCC_except_table2839
- GCC_except_table2879
- GCC_except_table2888
- GCC_except_table2891
- GCC_except_table2898
- GCC_except_table29
- GCC_except_table2907
- GCC_except_table2951
- GCC_except_table2952
- GCC_except_table2958
- GCC_except_table3014
- GCC_except_table3054
- GCC_except_table311
- GCC_except_table312
- GCC_except_table3163
- GCC_except_table3172
- GCC_except_table319
- GCC_except_table3193
- GCC_except_table3390
- GCC_except_table3396
- GCC_except_table3489
- GCC_except_table3491
- GCC_except_table3499
- GCC_except_table3517
- GCC_except_table3528
- GCC_except_table3544
- GCC_except_table3588
- GCC_except_table3593
- GCC_except_table3598
- GCC_except_table3602
- GCC_except_table3605
- GCC_except_table3606
- GCC_except_table3610
- GCC_except_table3612
- GCC_except_table3616
- GCC_except_table3620
- GCC_except_table366
- GCC_except_table3660
- GCC_except_table3667
- GCC_except_table38
- GCC_except_table3919
- GCC_except_table3923
- GCC_except_table3926
- GCC_except_table3929
- GCC_except_table3932
- GCC_except_table3935
- GCC_except_table3945
- GCC_except_table4003
- GCC_except_table4041
- GCC_except_table4044
- GCC_except_table4051
- GCC_except_table4052
- GCC_except_table4079
- GCC_except_table4090
- GCC_except_table4119
- GCC_except_table4181
- GCC_except_table4186
- GCC_except_table4197
- GCC_except_table4202
- GCC_except_table4205
- GCC_except_table4230
- GCC_except_table4232
- GCC_except_table4242
- GCC_except_table4262
- GCC_except_table4265
- GCC_except_table4271
- GCC_except_table4293
- GCC_except_table4296
- GCC_except_table4300
- GCC_except_table4303
- GCC_except_table4322
- GCC_except_table4326
- GCC_except_table4330
- GCC_except_table4334
- GCC_except_table4341
- GCC_except_table4357
- GCC_except_table4508
- GCC_except_table4517
- GCC_except_table452
- GCC_except_table4525
- GCC_except_table4527
- GCC_except_table4533
- GCC_except_table4535
- GCC_except_table455
- GCC_except_table4553
- GCC_except_table4558
- GCC_except_table4560
- GCC_except_table4568
- GCC_except_table4572
- GCC_except_table4578
- GCC_except_table458
- GCC_except_table4601
- GCC_except_table461
- GCC_except_table4634
- GCC_except_table464
- GCC_except_table4684
- GCC_except_table4688
- GCC_except_table470
- GCC_except_table4871
- GCC_except_table4878
- GCC_except_table4935
- GCC_except_table4957
- GCC_except_table4961
- GCC_except_table4990
- GCC_except_table502
- GCC_except_table5086
- GCC_except_table5091
- GCC_except_table5099
- GCC_except_table5125
- GCC_except_table5197
- GCC_except_table5305
- GCC_except_table5344
- GCC_except_table5352
- GCC_except_table5354
- GCC_except_table5357
- GCC_except_table5576
- GCC_except_table5591
- GCC_except_table56
- GCC_except_table5617
- GCC_except_table566
- GCC_except_table5695
- GCC_except_table5696
- GCC_except_table5709
- GCC_except_table5771
- GCC_except_table5790
- GCC_except_table5798
- GCC_except_table5802
- GCC_except_table5812
- GCC_except_table5815
- GCC_except_table582
- GCC_except_table5875
- GCC_except_table5890
- GCC_except_table5900
- GCC_except_table5928
- GCC_except_table5931
- GCC_except_table5942
- GCC_except_table5949
- GCC_except_table5957
- GCC_except_table5959
- GCC_except_table5994
- GCC_except_table5995
- GCC_except_table5998
- GCC_except_table5999
- GCC_except_table6007
- GCC_except_table6020
- GCC_except_table6113
- GCC_except_table613
- GCC_except_table6138
- GCC_except_table6180
- GCC_except_table620
- GCC_except_table6205
- GCC_except_table6210
- GCC_except_table6215
- GCC_except_table6217
- GCC_except_table6219
- GCC_except_table6237
- GCC_except_table6240
- GCC_except_table6242
- GCC_except_table6246
- GCC_except_table6248
- GCC_except_table63
- GCC_except_table6307
- GCC_except_table6347
- GCC_except_table6352
- GCC_except_table6365
- GCC_except_table638
- GCC_except_table6391
- GCC_except_table6393
- GCC_except_table6395
- GCC_except_table6404
- GCC_except_table6412
- GCC_except_table6413
- GCC_except_table6415
- GCC_except_table6417
- GCC_except_table6419
- GCC_except_table6420
- GCC_except_table6421
- GCC_except_table6422
- GCC_except_table6423
- GCC_except_table6424
- GCC_except_table6425
- GCC_except_table6429
- GCC_except_table6431
- GCC_except_table6433
- GCC_except_table6436
- GCC_except_table6439
- GCC_except_table6441
- GCC_except_table6442
- GCC_except_table6443
- GCC_except_table6444
- GCC_except_table6445
- GCC_except_table6446
- GCC_except_table6447
- GCC_except_table6448
- GCC_except_table6449
- GCC_except_table6450
- GCC_except_table6451
- GCC_except_table6454
- GCC_except_table6456
- GCC_except_table6458
- GCC_except_table6459
- GCC_except_table6461
- GCC_except_table6463
- GCC_except_table6464
- GCC_except_table6465
- GCC_except_table6467
- GCC_except_table6469
- GCC_except_table6470
- GCC_except_table6471
- GCC_except_table6472
- GCC_except_table6581
- GCC_except_table6647
- GCC_except_table67
- GCC_except_table6763
- GCC_except_table6832
- GCC_except_table7045
- GCC_except_table7104
- GCC_except_table7150
- GCC_except_table7157
- GCC_except_table7168
- GCC_except_table7174
- GCC_except_table7181
- GCC_except_table7188
- GCC_except_table7192
- GCC_except_table7195
- GCC_except_table7198
- GCC_except_table720
- GCC_except_table7215
- GCC_except_table7221
- GCC_except_table7226
- GCC_except_table7232
- GCC_except_table7238
- GCC_except_table7251
- GCC_except_table7255
- GCC_except_table7269
- GCC_except_table727
- GCC_except_table7279
- GCC_except_table7288
- GCC_except_table7293
- GCC_except_table7308
- GCC_except_table7310
- GCC_except_table7322
- GCC_except_table7340
- GCC_except_table7345
- GCC_except_table7348
- GCC_except_table7356
- GCC_except_table7358
- GCC_except_table7367
- GCC_except_table742
- GCC_except_table7429
- GCC_except_table744
- GCC_except_table7447
- GCC_except_table7455
- GCC_except_table7457
- GCC_except_table7458
- GCC_except_table7462
- GCC_except_table7463
- GCC_except_table7465
- GCC_except_table7468
- GCC_except_table7474
- GCC_except_table7476
- GCC_except_table7478
- GCC_except_table7480
- GCC_except_table7482
- GCC_except_table7487
- GCC_except_table7490
- GCC_except_table7498
- GCC_except_table750
- GCC_except_table7502
- GCC_except_table7507
- GCC_except_table7509
- GCC_except_table7511
- GCC_except_table7513
- GCC_except_table7526
- GCC_except_table7530
- GCC_except_table7534
- GCC_except_table7536
- GCC_except_table7538
- GCC_except_table7540
- GCC_except_table7542
- GCC_except_table7557
- GCC_except_table7561
- GCC_except_table7567
- GCC_except_table7571
- GCC_except_table7575
- GCC_except_table7603
- GCC_except_table7607
- GCC_except_table761
- GCC_except_table7633
- GCC_except_table7635
- GCC_except_table7650
- GCC_except_table767
- GCC_except_table781
- GCC_except_table786
- GCC_except_table7883
- GCC_except_table7890
- GCC_except_table7903
- GCC_except_table7904
- GCC_except_table791
- GCC_except_table7917
- GCC_except_table7939
- GCC_except_table7940
- GCC_except_table7951
- GCC_except_table7980
- GCC_except_table8000
- GCC_except_table8006
- GCC_except_table8010
- GCC_except_table8023
- GCC_except_table8026
- GCC_except_table8083
- GCC_except_table8087
- GCC_except_table8089
- GCC_except_table8100
- GCC_except_table8107
- GCC_except_table8162
- GCC_except_table817
- GCC_except_table8171
- GCC_except_table8183
- GCC_except_table8185
- GCC_except_table8207
- GCC_except_table8213
- GCC_except_table8217
- GCC_except_table8236
- GCC_except_table8242
- GCC_except_table8284
- GCC_except_table8299
- GCC_except_table8304
- GCC_except_table8306
- GCC_except_table8311
- GCC_except_table8321
- GCC_except_table8329
- GCC_except_table8333
- GCC_except_table8336
- GCC_except_table8345
- GCC_except_table8350
- GCC_except_table8378
- GCC_except_table8436
- GCC_except_table8437
- GCC_except_table8449
- GCC_except_table8455
- GCC_except_table8460
- GCC_except_table8461
- GCC_except_table8495
- GCC_except_table8500
- GCC_except_table8506
- GCC_except_table8518
- GCC_except_table8531
- GCC_except_table8544
- GCC_except_table856
- GCC_except_table8568
- GCC_except_table8598
- GCC_except_table8633
- GCC_except_table8636
- GCC_except_table8689
- GCC_except_table8697
- GCC_except_table871
- GCC_except_table8712
- GCC_except_table8714
- GCC_except_table8834
- GCC_except_table8879
- GCC_except_table888
- GCC_except_table8880
- GCC_except_table8904
- GCC_except_table894
- GCC_except_table903
- GCC_except_table9080
- GCC_except_table9084
- GCC_except_table9097
- GCC_except_table910
- GCC_except_table9101
- GCC_except_table915
- GCC_except_table9161
- GCC_except_table9173
- GCC_except_table9180
- GCC_except_table9183
- GCC_except_table9189
- GCC_except_table9214
- GCC_except_table9239
- GCC_except_table9243
- GCC_except_table9246
- GCC_except_table9253
- GCC_except_table9257
- GCC_except_table926
- GCC_except_table9299
- GCC_except_table931
- GCC_except_table9315
- GCC_except_table936
- GCC_except_table9438
- GCC_except_table9472
- GCC_except_table9476
- GCC_except_table9482
- GCC_except_table9484
- GCC_except_table9490
- GCC_except_table9493
- GCC_except_table9530
- GCC_except_table954
- GCC_except_table9577
- GCC_except_table9799
- GCC_except_table9800
- GCC_except_table9801
- GCC_except_table9818
- GCC_except_table9823
- GCC_except_table9836
- GCC_except_table985
- GCC_except_table9871
- GCC_except_table9882
- GCC_except_table993
- NavdRecentLocationsEntitlment_block_invoke.mediaStreamDownloadQueue
- NavdRecentLocationsEntitlment_block_invoke.onceToken
- OBJC_IVAR_$_PFAdjustment._autoIdentifier
- OBJC_IVAR_$_PFAdjustment._autoSettings
- OBJC_IVAR_$_PFAdjustment._enabled
- OBJC_IVAR_$_PFAdjustment._formatVersion
- OBJC_IVAR_$_PFAdjustment._identifier
- OBJC_IVAR_$_PFAdjustment._maskUUID
- OBJC_IVAR_$_PFAdjustment._settings
- OBJC_IVAR_$_PFAdjustmentStack._adjustments
- OBJC_IVAR_$_PFAdjustmentStack._formatVersion
- OBJC_IVAR_$_PFAdjustmentStack._maskUUIDs
- OBJC_IVAR_$_PLAggregateAlbumList._allAlbums
- OBJC_IVAR_$_PLAggregateAlbumList._childAlbumLists
- OBJC_IVAR_$_PLAggregateAlbumList._filter
- OBJC_IVAR_$_PLAggregateAlbumListChangeNotification._albumList
- OBJC_IVAR_$_PLAggregateAlbumListChangeNotification._indexOffet
- OBJC_IVAR_$_PLAggregateAlbumListChangeNotification._note
- OBJC_IVAR_$_PLBackgroundJobWorkerPendingWorkItems._zeroWorkItemsForValidCriteria
- OBJC_IVAR_$_PLChangeNotificationCenter._assetsWithCloudCommentChanges
- OBJC_IVAR_$_PLChangeNotificationCenter._changedCloudFeedEntries
- OBJC_IVAR_$_PLCloudCommentsChangeNotification._userInfo
- OBJC_IVAR_$_PLCloudFeedEntriesChangeNotification._deletedEntries
- OBJC_IVAR_$_PLCloudFeedEntriesChangeNotification._insertedEntries
- OBJC_IVAR_$_PLCloudFeedEntriesChangeNotification._shouldReload
- OBJC_IVAR_$_PLCloudFeedEntriesChangeNotification._updatedEntries
- OBJC_IVAR_$_PLInvitationRecordsChangeNotification._invitationRecordsDidChange
- OBJC_IVAR_$_PLInvitationRecordsChangeNotification._userInfo
- OBJC_IVAR_$_PLManagedAsset._height
- OBJC_IVAR_$_PLManagedAsset._width
- OBJC_IVAR_$_PLManagedObjectContext._isBackingALAssetsLibrary
- OBJC_IVAR_$_PLPhotoLibraryShouldReloadNotification._photoLibrary
- OBJC_IVAR_$_PLSearchTrackedAttributes._assetAttributesTrackedForSearch
- OBJC_IVAR_$_PLSearchTrackedAttributes._detectedFaceAttributesTrackedForSearch
- OBJC_IVAR_$_PLSearchTrackedAttributes._fetchingAlbumAttributesTrackedForSearch
- OBJC_IVAR_$_PLSearchTrackedAttributes._highlightAttributesTrackedForSearch
- OBJC_IVAR_$_PLSearchTrackedAttributes._managedAlbumAttributesTrackedForSearch
- OBJC_IVAR_$_PLSearchTrackedAttributes._mediaAnalysisAssetAttributesTrackedForSearch
- OBJC_IVAR_$_PLSearchTrackedAttributes._memoryAttributesTrackedForSearch
- OBJC_IVAR_$_PLSearchTrackedAttributes._personAttributesTrackedForSearch
- OBJC_IVAR_$_PLSearchTrackedChangeTypes._searchTrackedAttributes
- OBJC_IVAR_$_PLSharePost.skipAssetRelationshipValidationOnSave
- OBJC_IVAR_$_PLThumbnailResourceDataStoreOptions._overridingThumbnailIndex
- PLSearchIndexEnumeratePlacesFromBigToSmall.PLRevGeoOrderTypes
- PLSearchLeoDonationCurationAmbientEnabled.enabled
- PLSearchLeoDonationCurationAmbientEnabled.onceToken
- PLSearchLeoDonationCurationAmbientSceneEnabled.enabled
- PLSearchLeoDonationCurationAmbientSceneEnabled.onceToken
- PLXPCStoreAllowedEntityNames.pl_once_object_2
- PLXPCStoreAllowedEntityNames.pl_once_token_2
- PLXPCStoreDeniedEntityNames.pl_once_object_3
- PLXPCStoreDeniedEntityNames.pl_once_token_3
- TapToRadarKitLibraryCore.frameworkLibrary
- _AVAppleMakerNote_BurstUUID
- _AVAppleMakerNote_SpatialOverCaptureGroupIdentifier
- _CGImageCreateByMatchingToColorSpace
- _NSInvalidatedAllObjectsKey
- _NSStringFromPLCloudFeedEntryFilter
- _OBJC_CLASS_$_NSFetchIndexDescription
- _OBJC_CLASS_$_NSFetchIndexElementDescription
- _OBJC_CLASS_$_PFAdjustment
- _OBJC_CLASS_$_PFAdjustmentSerialization
- _OBJC_CLASS_$_PFAdjustmentStack
- _OBJC_CLASS_$_PILongExposureFusionAutoCalculator
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
- _PLGenericChangeNotification
- _PLGetSandboxExtensionTokenForProcess
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
- _PLSearchLeoDonationCurationAmbientEnabled
- _PLSearchLeoDonationCurationAmbientSceneEnabled
- _PLShouldCacheIOSurfaces
- _PhotosString
- _SyncedAssetGetIdentifier
- _SyncedAssetGetPartsCount
- _SyncedAssetGetVersion
- _SyncedAssetSyncedGetPartForFormatID
- _SyncedPartGetFaceIndex
- _TapToRadarKitLibrary
- _TapToRadarKitLibraryCore
- __102-[PLBackgroundJobSharedAssetContainerUpdateWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- __105-[PLBackgroundJobResourceUploadExtensionRunnerWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- __116-[PLSyndicationSyncServiceWrapper executeQueryForSyncManager:type:startDate:endDate:batchHandler:completionHandler:]_block_invoke
- __123-[PLBackgroundJobResourceUploadExtensionRunnerWorker criteriaNeedingProcessingInLibrary:validCriterias:outSignalAgainDate:]_block_invoke
- __126+[PLDiagnostics _tapToRadarKitDraftWithTitle:description:radarComponent:isUserInitiated:displayReason:parameters:attachments:]_block_invoke
- __155+[PLSyndicationResourceDataStore provideFileURLAndUnwrapLivePhotoIfNeededForItemIdentifiersWithBundleIDs:destURLs:options:resultHandler:completionHandler:]_block_invoke
- __162+[PLSyndicationResourceDataStore _provideFileURLAndUnwrapLivePhotoIfNeededForBundleID:syndicationIdentifier:typeIdentifier:isLivePhoto:options:completionHandler:]_block_invoke
- __165-[PLManagedAsset _generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:retryNumber:allowCancellationByService:clientBundleID:completion:]_block_invoke
- __52-[PLAggregateAlbumList assetContainerListDidChange:]_block_invoke
- __57-[PLSearchIndexingRebuildEngine _startRebuildForLibrary:]_block_invoke
- __66-[PLBackgroundJobWorker pendingWorkItemsInLibrary:validCriterias:]_block_invoke
- __69+[PLPhotoSharingHelper updateCloudSharedAlbumPublicURLStateOnServer:]_block_invoke
- __74+[PLPhotoSharingHelper acceptPendingInvitationForAlbum:completionHandler:]_block_invoke
- __75-[PLManagedObjectContext _notifyALAssetsLibraryWithChanges:usingObjectIDs:]_block_invoke
- __76+[PLCascadeUtilities registerSuggestionsPreferenceChangeNotificationHandler]_block_invoke
- __77+[PLPhotoSharingHelper sendPendingInvitationsForAlbum:resendInvitationGUIDs:]_block_invoke
- __78+[PLPhotoSharingHelper markPendingInvitationAsSpamForAlbum:completionHandler:]_block_invoke
- __79-[PLManagedObjectPagingIterator countRemainingWithManagedObjectContext:logger:]_block_invoke
- __80+[PLPhotoSharingHelper updateCloudSharedAlbumMultipleContributorsStateOnServer:]_block_invoke
- __80-[PLSearchIndexingEngine _inq_dropSearchIndexWithSourceName:reasons:completion:]_block_invoke_2
- __82-[PLFeatureAvailabilityComputer _scanLeoForPhotoLibrary:progress:completionBlock:]_block_invoke
- __83-[PLNotificationManager noteMultipleContributorStatusChangedForAlbum:mstreamdInfo:]_block_invoke
- __84-[PLBackgroundJobWorker pendingCriteriaInLibrary:validCriterias:outSignalAgainDate:]_block_invoke
- __85-[PLNotificationManager noteInvitationRecordStatusChanged:fromOldState:mstreamdInfo:]_block_invoke
- __87-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:completionHandler:]_block_invoke
- __87-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:completionHandler:]_block_invoke_2
- __87-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:completionHandler:]_block_invoke_3
- __89-[PLBackgroundJobEditRenderingWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- __90-[PLCloudPhotoLibraryManager _deactivateCPLSyncWithResetMode:willBecomeNonSyncableReason:]_block_invoke
- __93+[PLAssetSharingUtilities assetForVideoURL:metadata:library:outAudioMix:outVideoComposition:]_block_invoke
- __97-[PLCloudPhotoLibraryManager _disableaCPLAfterZoneWipedInCloudIfNecessaryWithStatus:transaction:]_block_invoke
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
- ___105-[PLBackgroundJobDeferredRenderDerivativesBaseWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___105-[PLBackgroundJobResourceUploadExtensionRunnerWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___105-[PLBackgroundJobResourceUploadExtensionRunnerWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke_2
- ___105-[PLBackgroundJobResourceUploadExtensionRunnerWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke_3
- ___107-[PLBackgroundJobSyndicationResourceSanitizationWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___115-[PLSyndicationResourceDataStore _requestLocalAvailabilityChangeForSyndicationOriginalResource:options:completion:]_block_invoke_2
- ___116-[PLSyndicationSyncServiceWrapper executeQueryForSyncManager:type:startDate:endDate:batchHandler:completionHandler:]_block_invoke
- ___123-[PLBackgroundJobResourceUploadExtensionRunnerWorker criteriaNeedingProcessingInLibrary:validCriterias:outSignalAgainDate:]_block_invoke
- ___138-[PLSearchIndexingRebuildEngine _lock_startPrepareAndRebuildForLibrary:type:calledBy:rebuildReasons:spotlightReasonForReindexingAllItems:]_block_invoke_2
- ___149-[PLSyndicationResourceDataStore _copyAndMarkAsLocallyAvailablePairedLivePhotoResourceForRequestedResource:requestedVideoComplement:sourceURL:error:]_block_invoke
- ___155+[PLSyndicationResourceDataStore provideFileURLAndUnwrapLivePhotoIfNeededForItemIdentifiersWithBundleIDs:destURLs:options:resultHandler:completionHandler:]_block_invoke
- ___162+[PLSyndicationResourceDataStore _provideFileURLAndUnwrapLivePhotoIfNeededForBundleID:syndicationIdentifier:typeIdentifier:isLivePhoto:options:completionHandler:]_block_invoke
- ___162+[PLSyndicationResourceDataStore _provideFileURLAndUnwrapLivePhotoIfNeededForBundleID:syndicationIdentifier:typeIdentifier:isLivePhoto:options:completionHandler:]_block_invoke_2
- ___165-[PLManagedAsset _generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:retryNumber:allowCancellationByService:clientBundleID:completion:]_block_invoke
- ___165-[PLManagedAsset _generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:retryNumber:allowCancellationByService:clientBundleID:completion:]_block_invoke_2
- ___32-[PLIntensiveResourceTask start]_block_invoke_2
- ___43-[PLManagedAsset(RM) resourcesWithVersion:]_block_invoke
- ___44+[PLManagedAsset predicateForReframedAssets]_block_invoke
- ___44-[PLGenericAlbum assetsByObjectIDAtIndexes:]_block_invoke
- ___48-[PLIntensiveResourceTask prepareForReplacement]_block_invoke
- ___49+[PLManagedAsset ptpResetEventAndFilenameMapping]_block_invoke
- ___51+[PLManagedAsset ptpAssetIDForEventAndFilenameKey:]_block_invoke
- ___51-[PLSocialGroup runAssetContainmentWithCompletion:]_block_invoke
- ___52-[PLAggregateAlbumList assetContainerListDidChange:]_block_invoke
- ___53+[PLManagedObjectContext assetsLibraryLoggingEnabled]_block_invoke
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
- ___68-[PLCloudPhotoLibraryManager cplConfigurationWithCompletionHandler:]_block_invoke
- ___68-[PLNotificationManager noteDidReceiveCMMInvitationWithMomentShare:]_block_invoke
- ___69+[PLPhotoSharingHelper updateCloudSharedAlbumPublicURLStateOnServer:]_block_invoke
- ___70+[PLDiagnostics addOSStateHandlerWithTitle:queue:propertyListHandler:]_block_invoke
- ___72+[PLGraphEdge fetchEdgesWithExternalIdentifiers:inManagedObjectContext:]_block_invoke
- ___72+[PLGraphNode fetchNodesWithExternalIdentifiers:inManagedObjectContext:]_block_invoke
- ___73-[PLManagedAssetRecoveryManager identifyAssetsWithInconsistentCloudState]_block_invoke
- ___73-[PLManagedAssetRecoveryManager identifyAssetsWithInconsistentCloudState]_block_invoke_2
- ___73-[PLManagedAssetRecoveryManager identifyAssetsWithInconsistentCloudState]_block_invoke_3
- ___74+[PLPhotoSharingHelper acceptPendingInvitationForAlbum:completionHandler:]_block_invoke
- ___75-[PLManagedObjectContext _notifyALAssetsLibraryWithChanges:usingObjectIDs:]_block_invoke
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
- ___80+[PLPhotoSharingHelper updateCloudSharedAlbumMultipleContributorsStateOnServer:]_block_invoke
- ___80+[PLPhotoSharingHelper updateCloudSharedAlbumMultipleContributorsStateOnServer:]_block_invoke_2
- ___81-[CNContactStore(PhotoLibraryAdditions) contactsMatchingPhoneNumber:keysToFetch:]_block_invoke
- ___82+[PLPersistentHistoryUtilities fetchTransactionCountSinceToken:withContext:error:]_block_invoke
- ___82-[PLPhotoEditRenderer calculateLongExposureFusionParametersWithCompletionHandler:]_block_invoke
- ___83-[PLNotificationManager noteMultipleContributorStatusChangedForAlbum:mstreamdInfo:]_block_invoke
- ___84+[PLGraphNode fetchObjectIDsForNodesWithExternalIdentifiers:inManagedObjectContext:]_block_invoke
- ___84-[PLBackgroundJobWorker pendingCriteriaInLibrary:validCriterias:outSignalAgainDate:]_block_invoke
- ___85-[PLNotificationManager noteInvitationRecordStatusChanged:fromOldState:mstreamdInfo:]_block_invoke
- ___86-[PLBackgroundJobPersonSyncWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___86-[PLBackgroundJobStableHashWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___87-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:completionHandler:]_block_invoke
- ___87-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:completionHandler:]_block_invoke_2
- ___87-[PLFeatureAvailabilityComputer _leo_computeSnapshotForPhotoLibrary:completionHandler:]_block_invoke_3
- ___89-[PLBackgroundJobEditRenderingWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___90-[PLBackgroundJobSearchIndexingWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___90-[PLCloudPhotoLibraryManager _deactivateCPLSyncWithResetMode:willBecomeNonSyncableReason:]_block_invoke
- ___90-[PLCloudPhotoLibraryManager _deactivateCPLSyncWithResetMode:willBecomeNonSyncableReason:]_block_invoke_2
- ___92+[PLCloudResource resetPrefetchStateForResourcesWithResourceType:itemIdentifiers:inLibrary:]_block_invoke
- ___93+[PLAssetSharingUtilities assetForVideoURL:metadata:library:outAudioMix:outVideoComposition:]_block_invoke
- ___93+[PLAssetSharingUtilities assetForVideoURL:metadata:library:outAudioMix:outVideoComposition:]_block_invoke_2
- ___93-[PLBackgroundJobDuplicateDetectorWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___96-[PLBackgroundJobResourceAvailabilityWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___96-[PLSyndicationResourceDataStore _copyItemAtURL:withPathManager:destFileIdentifier:inode:error:]_block_invoke
- ___97-[PLCloudPhotoLibraryManager _disableaCPLAfterZoneWipedInCloudIfNecessaryWithStatus:transaction:]_block_invoke
- ___98-[PLCollectionShareSharedStreamBackend checkServerForChangesForCollectionShare:completionHandler:]_block_invoke_4
- ___98-[PLCollectionShareSharedStreamBackend checkServerForChangesForCollectionShare:completionHandler:]_block_invoke_5
- ___99-[PLBackgroundJobSyndicationAssetCleanupWorker workItemsNeedingProcessingInLibrary:validCriterias:]_block_invoke
- ___PLDownloadMissingOriginals_block_invoke
- ___PLSearchIndexEnumeratePlacesFromBigToSmall_block_invoke
- ___PLSearchLeoDonationCurationAmbientEnabled_block_invoke
- ___PLSearchLeoDonationCurationAmbientSceneEnabled_block_invoke
- ___TapToRadarKitLibraryCore_block_invoke
- ___albumListTypes
- ___block_descriptor_120_e8_32s40s48s56s64s72r80r88r96r104r_e36_v24?0"CPLAdjustments"8"NSError"16l
- ___block_descriptor_123_e8_32s40s48s56s64s72s80s88s96s104bs112r_e37_v32?0"NSURL"8"NSURL"16"NSError"24l
- ___block_descriptor_128_e8_32s40s48s56s64s72s80s88bs96r104r112r_e5_v8?0l
- ___block_descriptor_129_e8_32s40s48s56s64s72s80s88s96s104s112s120r_e32_v32?0"PLManagedObject"8Q16^B24l
- ___block_descriptor_130_e8_32s40s48s56s64s72s80s88s96r104r112r_e5_v8?0l
- ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96s104s112bs120n11_8_8_s0_t8w8_e5_v8?0l
- ___block_descriptor_168_e8_32s40s48s56s64s72s80s88r96r104r112r120r128r136r144r152r_e12_v20?0I8^B12l
- ___block_descriptor_168_e8_32s40s48s56s64s72s80s88s96s104s112s120r128r136r144r152r_e5_v8?0l
- ___block_descriptor_176_e8_32s40s48s56s64s72s80s88s96s104s112s120s128bs136bs144r152r_e63_v60?0B8"NSURL"12"NSURL"20Q28q36"NSDictionary"44"NSError"52l
- ___block_descriptor_208_e8_32s40s48s56s64s72s80s88s96s104s112r120r128r136r144r152r160r168r176r184r_e53_v40?0"LEOItem"8"PLLeoLexemeIDSet"16"NSDate"24^B32l
- ___block_descriptor_32_e29_q24?0"NSValue"8"NSValue"16l
- ___block_descriptor_32_e33_B16?0"PLBackgroundJobCriteria"8l
- ___block_descriptor_32_e41_B24?0"PLManagedAsset"8"NSDictionary"16l
- ___block_descriptor_40_e8_32bs_e15_v16?0"NSURL"8l
- ___block_descriptor_40_e8_32bs_e35_v16?0"TapToRadarServiceSettings"8l
- ___block_descriptor_40_e8_32r_e11_v24?0Q8Q16l
- ___block_descriptor_40_e8_32s_e31_v32?0"PLNotification"8Q16^B24l
- ___block_descriptor_40_e8_32s_e33_B16?0"PLBackgroundJobCriteria"8l
- ___block_descriptor_40_e8_32s_e36_"NSMutableArray"20?0"NSArray"8B16l
- ___block_descriptor_42_e8_32s_e17_v16?0"NSError"8l
- ___block_descriptor_48_e8_32r_e17_v16?0"NSError"8l
- ___block_descriptor_48_e8_32r_e31_v32?0"PLGenericAlbum"8Q16^B24l
- ___block_descriptor_48_e8_32s40bs_e103_^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16?0^{os_state_hints_s=I*II}8l
- ___block_descriptor_48_e8_32s40bs_e11_v24?0Q8Q16l
- ___block_descriptor_48_e8_32s40bs_e15_v16?0"NSURL"8l
- ___block_descriptor_48_e8_32s_e33_B16?0"PLBackgroundJobCriteria"8l
- ___block_descriptor_49_e8_32s40bs_e24_v16?0"PLPhotoLibrary"8l
- ___block_descriptor_56_e8_32r40r48r_e67_v40?0"AVAsset"8"AVAudioMix"16"AVVideoComposition"24"NSError"32l
- ___block_descriptor_56_e8_32s40bs48r_e21_v24?0"NSString"8Q16l
- ___block_descriptor_56_e8_32s40s48s_e12_v24?0Q8^B16l
- ___block_descriptor_57_e8_32s40s48s_e53_v32?0"NSSet"8"NSMutableArray"16"NSMutableArray"24l
- ___block_descriptor_64_e8_32s40bs48r56r_e54_v48?0"NSString"8Q16"NSURL"24"NSData"32"NSError"40l
- ___block_descriptor_64_e8_32s40s48r56r_e24_v16?0"PLPhotoLibrary"8l
- ___block_descriptor_65_e8_32s40s48bs_e27_v24?0"NSURL"8"NSError"16l
- ___block_descriptor_72_e8_32s40s48r56r64r_e27_v24?0"NSURL"8"NSError"16l
- ___block_descriptor_72_e8_32s40s48s_e17_v16?0"NSError"8l
- ___block_descriptor_73_e8_32s40s48bs56r_e5_v8?0l
- ___block_descriptor_73_e8_32s40s48s56s64bs_e86_v68?0"NSString"8"NSString"16"NSString"24q32"NSString"40I48"NSDate"52"NSError"60l
- ___block_descriptor_81_e8_32s40s48s56r64r72r_e24_v16?0"PLPhotoLibrary"8l
- ___block_descriptor_87_e8_32s40s48s56s64bs_e62_v44?0"NSObject<OS_xpc_object>"8"NSNumber"16"NSURL"24S32q36l
- ___block_descriptor_88_e8_32s40s48s56s64bs72r_e34_v24?0"NSDictionary"8"NSError"16l
- ___cacheIOSurfaces
- ___copy_helper_block_e8_32s40s48s56s64s72r80r88r96r104r
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88b96r104r112r
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88r96r104r112r120r128r136r144r152r
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96r104r112r
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112r120r128r136r144r152r160r168r176r184r
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120r128r136r144r152r
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128b136b144r152r
- ___destroy_helper_block_e8_32s40s48s56s64s72r80r88r96r104r
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88r96r104r112r120r128r136r144r152r
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96r104r112r
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112r120r128r136r144r152r160r168r176r184r
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144r152r
- ___getRadarComponentClass_block_invoke
- ___getRadarDraftClass_block_invoke
- ___getTapToRadarServiceClass_block_invoke
- __cplDeviceLibraryConfigurationChanged
- __cplPendingDeviceLibraryConfigurationChanged
- _archivedAssetUUIDForPathDictionary
- _audit_stringTapToRadarKit
- _entityNamesAllowedByRestrictedDataEntitlements:.pl_once_object_4
- _entityNamesAllowedByRestrictedDataEntitlements:.pl_once_token_4
- _getTapToRadarServiceClass
- _hasChangesForCloudShared:.pl_once_object_49
- _hasChangesForCloudShared:.pl_once_token_49
- _kCGImagePropertyCIFFWhiteBalanceIndex
- _kCGImagePropertyExifColorSpace
- _kCGImagePropertyExifFlash
- _kCGImagePropertyExifLightSource
- _kCGImagePropertyExifWhiteBalance
- _kMaxTextCandidatesPerObservation
- _kOCRConfidenceThreshold
- _kPhotosApplicationURLAlbumID
- _kPhotosApplicationURLEventScheme
- _kPhotosApplicationURLEventShowAlbum
- _kPhotosApplicationURLEventShowImport
- _kPhotosApplicationURLEventUICommandKey
- _objc_msgSend$_assetsLibrary_isSharedPhotoStreamsSupportEnabled
- _objc_msgSend$_cloneResourcesForSharePlaceholderAsset:withPlaceholderResourceURLToSourceResourceURLMap:fileManager:photoLibrary:
- _objc_msgSend$_copyAndMarkAsLocallyAvailablePairedLivePhotoResourceForRequestedResource:requestedVideoComplement:sourceURL:error:
- _objc_msgSend$_copyItemAtURL:withPathManager:destFileIdentifier:inode:error:
- _objc_msgSend$_copyJobContentsToHoldingDirectoryWithUUID:incomingPath:job:
- _objc_msgSend$_countOfLocalCloudResourcesOfType:inManagedObjectContext:forMediumSized:localCount:unavailableCount:error:
- _objc_msgSend$_customSharedAlbumExportsOutputDirectoryForAssetWithUUID:
- _objc_msgSend$_deactivateCPLSyncWithResetMode:
- _objc_msgSend$_deactivateCPLSyncWithResetMode:willBecomeNonSyncableReason:
- _objc_msgSend$_debugDescription
- _objc_msgSend$_detailsForAlbum:
- _objc_msgSend$_disableaCPLAfterZoneWipedInCloudIfNecessaryWithStatus:transaction:
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
- _objc_msgSend$_isAssetLibraryFetchingAlbum:
- _objc_msgSend$_isAuthorizedAssetUUID:inManagedObjectContext:
- _objc_msgSend$_leo_computeSnapshotForPhotoLibrary:completionHandler:
- _objc_msgSend$_notifyALAssetsLibraryWithChanges:usingObjectIDs:
- _objc_msgSend$_ocrTextLineCandidatesFromTextBlockObservation:tokenizer:allowLowConfidence:
- _objc_msgSend$_ocrTextLinesFromDocumentObservation:allowLowConfidence:
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
- _objc_msgSend$assetsLibraryLoggingEnabled
- _objc_msgSend$authorizationStatus
- _objc_msgSend$backgroundJobWorkerTypesMaskGuestAssetSync:personSync:syndicationSync:syndicationResourceSanitization:syndicationResourceDownload:syndicationAssetCleanup:assetStack:duplicateDetector:deferredRenderDerivativesLowPriority:deferredRenderDerivativesHighPriority:resourceAvailability:stableHash:editRenderingImage:editRenderingVideo:highPrioritySearchIndexing:lowPriorityBatterySearchIndexing:lowPriorityChargerSearchIndexing:sharedAssetContainerUpdate:assetResourceUploadJob:assetResourceUploadExtensionRunner:featureAvailability:optimizeTableThumbs:cascadeDonation:provenanceTimestamp:
- _objc_msgSend$changedIndexesRelativeToSnapshot
- _objc_msgSend$changedObjects
- _objc_msgSend$compressData:error:
- _objc_msgSend$containsTypes:
- _objc_msgSend$countOfIndexesInRange:
- _objc_msgSend$countRemainingWithManagedObjectContext:logger:
- _objc_msgSend$cplDeviceLibraryConfigurationChanged
- _objc_msgSend$cplPendingDeviceLibraryConfigurationChanged
- _objc_msgSend$createDraft:forProcessNamed:withDisplayReason:completionHandler:
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
- _objc_msgSend$fileSystemProperties
- _objc_msgSend$fileURLFromAssetURL:photoLibrary:
- _objc_msgSend$filteredAlbumList:filter:
- _objc_msgSend$finishDecoding
- _objc_msgSend$generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:allowCancellationByService:clientBundleID:completion:
- _objc_msgSend$generatePathToAssetUUIDRecoveryMapping
- _objc_msgSend$getServiceSettingsWithCompletionHandler:
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
- _objc_msgSend$initWithLine:words:confidence:
- _objc_msgSend$initWithMessage:
- _objc_msgSend$initWithMultipleContributorEnabledForAlbum:
- _objc_msgSend$initWithName:elements:
- _objc_msgSend$initWithName:version:identifier:
- _objc_msgSend$initWithProperty:collationType:
- _objc_msgSend$initWithTransaction:
- _objc_msgSend$initWithZeroWorkItemsForValidCriteria
- _objc_msgSend$isBackingALAssetsLibrary
- _objc_msgSend$isLikePhoneNumber:
- _objc_msgSend$isValidArchiveDictionary:errors:
- _objc_msgSend$isValidEnvelopeDictionary:errors:
- _objc_msgSend$isVisualIntelligenceDefaultLibrary
- _objc_msgSend$lastImportedPhotosAlbumCreateIfNeeded:
- _objc_msgSend$localizedFailureReason
- _objc_msgSend$managedAlbumAttributesTrackedForSearch
- _objc_msgSend$maskForNotifyALAssetsLibraryWithChangesCloudSharedExclusions
- _objc_msgSend$maskForNotifyALAssetsLibraryWithChangesExclusions
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
- _objc_msgSend$ocrTextLinesFromDocumentObservation:
- _objc_msgSend$pendingCriteriaInLibrary:validCriterias:outSignalAgainDate:
- _objc_msgSend$pendingWorkItemsInLibrary:validCriterias:
- _objc_msgSend$personAttributesTrackedForSearch
- _objc_msgSend$phoneNumbers
- _objc_msgSend$pl_fetchObjectsWithIDs:
- _objc_msgSend$placesAlbumListInPhotoLibrary:
- _objc_msgSend$postShouldReloadNotificationWithPhotoLibrary:
- _objc_msgSend$predicateForUploadableAssetsWithMasterCloudLocalStateNotEqualTo:cplFeatureDataclasses:
- _objc_msgSend$prepareForReplacement
- _objc_msgSend$privateDownloadCloudPhotoLibraryAsset:resourceType:highPriority:completionHandler:
- _objc_msgSend$provideFileURLAndUnwrapLivePhotoIfNeededForItemIdentifiersWithBundleIDs:destURLs:options:resultHandler:completionHandler:
- _objc_msgSend$removeAssetContainerListChangeObserver:containerList:
- _objc_msgSend$requestAVAssetWithResultHandler:
- _objc_msgSend$resetAllFetchingAlbums
- _objc_msgSend$runWithCompletionHandler:
- _objc_msgSend$scenesAlbumListInPhotoLibrary:
- _objc_msgSend$searchTrackedAttributes
- _objc_msgSend$serializeDictionary:error:
- _objc_msgSend$setAutoDiagnostics:
- _objc_msgSend$setClassification:
- _objc_msgSend$setCloudRelationshipState:
- _objc_msgSend$setDeletedEntries:
- _objc_msgSend$setDiagnosticExtensionIDs:
- _objc_msgSend$setIndexes:
- _objc_msgSend$setInsertedEntries:
- _objc_msgSend$setIsUserInitiated:
- _objc_msgSend$setReproducibility:
- _objc_msgSend$setShouldReload:
- _objc_msgSend$setUpdatedEntries:
- _objc_msgSend$setZeroWorkItemsForValidCriteria:
- _objc_msgSend$setupPlaceholderAssetWithRequiredPropertiesFromSourceAsset:placeholderAssetUUID:bundleScope:share:importSessionID:bakeInAdjustmentsFromSourceAsset:flattenLivePhoto:copyTitleDescriptionAndKeywords:copyCameraProcessingAdjustmentResources:copyProvenanceData:isCurrentUser:library:
- _objc_msgSend$shared
- _objc_msgSend$validateArchive:containsEntryWithKey:ofType:errors:
- _objc_msgSend$validateValue:isOfType:errors:
- _objc_msgSend$workItemsNeedingProcessingInLibrary:validCriterias:
- _objc_msgSend$zeroWorkItemsForValidCriteria
- _xpc_dictionary_create_reply
- archivedAssetUUIDForPathDictionary_block_invoke.s_cplAssetDirectoryPrefix
- archivedAssetUUIDForPathDictionary_block_invoke.s_onceToken
- assetsLibraryLoggingEnabled.alLogging
- assetsLibraryLoggingEnabled.onceToken
- changeNotificationObjectIDKeys.pl_once_object_46
- changeNotificationObjectIDKeys.pl_once_token_46
- changeNotificationObjectIDMutationKeys.pl_once_object_45
- changeNotificationObjectIDMutationKeys.pl_once_token_45
- changeNotificationObjectKeys.pl_once_object_44
- changeNotificationObjectKeys.pl_once_token_44
- changeNotificationObjectMutationKeys.pl_once_object_43
- changeNotificationObjectMutationKeys.pl_once_token_43
- evaluateWhiteBalanceValueWithOriginalExifProperties:.canonWhiteBalance
- getRadarComponentClass.softClass
- getRadarDraftClass.softClass
- getTapToRadarServiceClass.softClass
- predicateForReframedAssets.onceToken
- predicateForReframedAssets.predicate
- predicateToExcludeAssetsMissingMasterThumbnailsWithThumbnailIndexKeyPath:.pl_once_object_17
- predicateToExcludeAssetsMissingMasterThumbnailsWithThumbnailIndexKeyPath:.pl_once_token_17
- predicateToExcludeCameraAutoAdjustments.pl_once_object_18
- predicateToExcludeCameraAutoAdjustments.pl_once_token_18
- predicateToExcludeHiddenAssetsWithHiddenKeyPath:.pl_once_object_13
- predicateToExcludeHiddenAssetsWithHiddenKeyPath:.pl_once_token_13
- predicateToExcludeNonvisibleBurstAssets.pl_once_object_15
- predicateToExcludeNonvisibleBurstAssets.pl_once_token_15
- predicateToExcludeNonvisibleBurstAssetsWithAvalanchePickTypeKeyPath:.pl_once_object_16
- predicateToExcludeNonvisibleBurstAssetsWithAvalanchePickTypeKeyPath:.pl_once_token_16
- predicateToExcludeRestrictedLockedAssets.pl_once_object_14
- predicateToExcludeRestrictedLockedAssets.pl_once_token_14
- predicateToExcludeTrashedAssets.pl_once_object_11
- predicateToExcludeTrashedAssets.pl_once_token_11
- predicateToExcludeTrashedAssetsWithTrashedStateKeyPath:.pl_once_object_12
- predicateToExcludeTrashedAssetsWithTrashedStateKeyPath:.pl_once_token_12
CStrings:
+ "\n\t%@ : %@"
+ "%@ (%llu)"
+ "%K == %@ AND %K == %@ AND %K == nil"
+ "%K == %@ AND %K == %@ AND (%K == nil OR %K == nil)"
+ "%K == nil OR %K >= %K"
+ "%K > %@ AND %K.%K == NO"
+ "%{public}@ requested to stop running remaining work items"
+ "%{public}@ setting _shouldDeferTask to YES due to error: %@"
+ "+[PLCascadeUtilities _handleSuggestionsPreferenceChanged]"
+ "+[PLManagedAsset countUsedAssetsWithKind:excludeTrashed:excludeInvisible:excludeCloudShared:excludePhotoStream:inManagedObjectContext:]"
+ "+[PLManagedObject entityInManagedObjectContext:]"
+ "-[PLAssetsdCloudInternalService updateAccessRequestForParticipantWithUUID:toAcceptanceStatus:inCollectionShareWithIdentifier:reply:]"
+ "-[PLAssetsdLibraryInternalService getSearchDonationProgressShouldCompute:shouldReport:reply:]"
+ "-[PLAssetsdLibraryInternalService migrateLimitedLibraryAccessFromApplication:toApplication:completionHandler:]"
+ "-[PLBackgroundJobGuestAssetSyncWorker workItemsNeedingProcessingInLibrary:currentCriteria:]"
+ "-[PLBackgroundJobPersonSyncWorker workItemsNeedingProcessingInLibrary:currentCriteria:]"
+ "-[PLBackgroundJobService _inq_pendingJobsForBundle:workerTypes:currentCriteria:]"
+ "-[PLCloudPhotoLibraryManager _deactivateCPLSyncWithResetMode:reason:willBecomeNonSyncable:]"
+ "-[PLCloudPhotoLibraryManager _linkOrphanedCollectionShareContributorsWithCPLSettings:]"
+ "-[PLCloudPhotoLibraryManager _restoreMissingCollectionSharePostsWithCPLSettings:]"
+ "-[PLCollectionShareCPLBackend updateAccessRequestForParticipant:toAcceptanceStatus:collectionShare:completionHandler:]"
+ "-[PLFeatureAvailabilityComputer _addHighlightStatusToProcessingSnapshot:managedObjectContext:error:]"
+ "-[PLFeatureAvailabilityComputer _assetCountForPredicate:managedObjectContext:error:]"
+ "-[PLFeatureAvailabilityComputer _fetchHighlightStatusInPhotoLibrary:completionBlock:]_block_invoke"
+ "-[PLManagedAsset _generateDeferredAdjustmentWithImageConversionClient:videoConversionClient:reason:retryNumber:allowCancellationByService:clientBundleID:shouldSaveMediaConversionResultBlock:completion:]"
+ "-[PLManagedAsset(Share) setupPlaceholderAssetWithRequiredPropertiesFromSourceAsset:placeholderAssetUUID:bundleScope:share:importSessionID:bakeInAdjustmentsFromSourceAsset:flattenLivePhoto:copyTitleDescriptionAndKeywords:copyCameraProcessingAdjustmentResources:copyLocationData:copyProvenanceData:isCurrentUser:library:]"
+ "-[PLModelMigrationAction_MigrateCloudSharedAlbumToCollectionShare performActionWithManagedObjectContext:error:]_block_invoke"
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
+ "Collection share is not published"
+ "Compute snapshot for search progress failed with error: %@"
+ "Container was wiped by an encrypted data reset for app library with main scope identifier: %{public}@"
+ "Creating sqliteErrorIndicatorFile"
+ "Creating sqliteErrorIndicatorFile before lightweight migration"
+ "Creating sqliteErrorIndicatorFile for background Migration failure"
+ "Creating sqliteErrorIndicatorFile for excessive persistent history size"
+ "DefaultToKeepOriginals"
+ "Deleting %tu identifiers from system Leo store"
+ "Direct upload batch is missing SharePost %{public}@ - its %lu assets will arrive before their post"
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
+ "Failed to fetch CPL collection shares: %@"
+ "Failed to fetch assets for post %@: %@"
+ "Failed to fetch collection share assets without a post: %@"
+ "Failed to look for migrated CPL collection shares: %@"
+ "Failed to mark background migration actions as skipped for newly created library. Error: %@"
+ "Failed to move compute sync resource file from %{public}@ to %{public}@: %@"
+ "Failed to obtain library identifier for library : %{public}@"
+ "Failed to obtain processing set URL"
+ "Filesystem Import took %1.1fs"
+ "Finished donating %tu items and deleting %tu items in managed Leo store"
+ "FixupAssetsStuckInDeferredProcessing: unsupported platform"
+ "Found sqliteErrorIndicatorFile (force rebuild indicator), will not attempt lightweight migration"
+ "Found work for library %@ (%@) - W: %{public}@ C: %{public}@ Cache hit: NO"
+ "Found work for library %@ (%@) - W: %{public}@ C: %{public}@ Cache hit: YES"
+ "Ignoring blocked identity for participant %{public}@ that is also a member of share %{public}@"
+ "Ignoring request to load file system data during OTA restore [%{public}@] for library %@, needs to prepare for background restore is %{public}@"
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
+ "LimitedLibrary: no LimitedLibraryFetchFilter to migrate for bundleIdentifier: %@"
+ "LimitedLibrary: pre-existing LimitedLibraryFetchFilter for applicationIdentifier: %@ before migration. Keeping that selection."
+ "Linked %lu assets that synced after post %{public}@ in share %{public}@"
+ "Linked %lu assets, %lu posts and %lu comments in share %{public}@ to participant %{public}@"
+ "Listening to Siri access changed notification: %@"
+ "LowPrioritySearchIndexing"
+ "MADEmbeddingSearchQueryResult returned nil sortedResults with no error"
+ "Marking background migration actions as skipped for newly created library"
+ "Migrating system photo library limited access filter from %@ to %@"
+ "NSManagedObjectContext is NULL looking for entity named %{public}@ (caller: %s)"
+ "No CPL settings on CPL library open, skipping the default prefetch mode"
+ "No assets match cloudBatchID in share %@ for post %@; the assets are linked once they sync"
+ "No custom key asset on CollectionShare %{public}@; pushing a scope change that omits keyAssetIdentifier and thumbnailImageData"
+ "No further bundles are registered for work under any criteria, shutting down."
+ "No participant matches contributor user identifier %@ in share %@ for asset %@; the contributor is linked once that participant syncs"
+ "No participant matches contributor user identifier %@ in share %@ for comment %@; the participant is linked once they sync"
+ "No participant matches contributor user identifier %@ in share %@ for post %@; the contributor is linked once that participant syncs"
+ "Not filing Tap-to-Radar draft '%@': Tap-to-Radar is not authorized for this process"
+ "Not propagating asset delete to cloud as its share scope could not be resolved: %{public}@"
+ "Not stashing camera job %{public}@, no asset UUID provided"
+ "Notification handler for Siri access change failed to get an LSM for the SPL"
+ "Notification handler for Siri access change failed to open the library: %@"
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
+ "PLXPC Service: migrateLimitedLibraryAccessFromApplication:toApplication:completionHandler:"
+ "PLXPC Service: updateAccessRequestForParticipantWithUUID:toAcceptanceStatus:inCollectionShareWithIdentifier:reply:"
+ "PXSharedAlbumsActivityLastSeenDateKey"
+ "PXSharedAlbumsEventLogLastEnteredDateKey"
+ "Participant %@ not found in collection share %@"
+ "Participant is not in the right state for this access request decision"
+ "Participant is not part of the collection share"
+ "Photos cannot proceed with the library (%@) in its current state.\n\n%@%@\n\nSelect \"Rebuild\" to allow rebuild of the photo library database (possible data loss) or \"Not now\" to stop now and leave it as-is"
+ "PostCollectionShareExpiringSoonNotification: skipping notification for collection: %@ because all assets are already saved to library"
+ "Preparing search index rebuild, called by %{public}@"
+ "Preserving generative attribution for asset %{public}@; render declares none"
+ "Preserving not-yet-pushed key asset %{public}@ on CollectionShare %{public}@ against no-key scope change (asset cloudLocalState %d, master cloudLocalState %d)"
+ "Progress donation to Spotlight failed because CSSearchableIndex is nil"
+ "Received notification for Siri access change"
+ "Refusing to move compute sync resource file outside the library bundle: %{public}@"
+ "Rejecting contextual video thumbnail identifier that cannot be used as part of a filename, asset %{public}@"
+ "Rejecting runDaemonJob from unauthorized client %d: %@"
+ "Removing sqliteErrorIndicatorFile after successful migration"
+ "Reported search indexing progress"
+ "Reporting search progress failed with error: %@"
+ "Reset localAvailability to none for %ld deferred processing final image/video resources previously stuck on the not-possible/retry-ladder"
+ "Resuming search index rebuild from entity: %{public}@, count remaining: %{public}@, resume objectID: %{public}@"
+ "SUBQUERY(%K, $post, $post.%K > %K AND $post.%K > 0).@count > 0"
+ "Search index rebuild completed (start date: %@)"
+ "Search index rebuild failed (start date: %@)"
+ "Search index rebuild paused (start date: %@)"
+ "Search index rebuild resumed (type: %{public}@, reasons: %{public}@, called by: %{public}@, start date: %@)"
+ "Search index rebuild started (type: %{public}@, reasons: %{public}@, called by: %{public}@)"
+ "Set the Visual Intelligence library to keep originals"
+ "Shared Albums not enabled"
+ "SharedStream Collection Shares do not support access requests"
+ "Should NOT show PLRebuildUserNotification for library %@ because of snooze until %@"
+ "Skipping direct upload for placeholder asset %@ - a master cannot be created until its resources land"
+ "Stashing camera job %{public}@ for replay at %@"
+ "Successfully dropped system leo store"
+ "Successfully migrated limited libraries between %@ and %@."
+ "System Leo delete items failed with error: %@"
+ "System Leo donate items failed with error: %@"
+ "System Leo store is nil, possible force close during indexing"
+ "System Leo update lexemes with entity scores failed with error: %@"
+ "TTR: zone was wiped for an unsupported app library"
+ "Tap-to-Radar is not authorized for this process"
+ "There are still bundles registered for work in the processing set, submitting activities."
+ "Unable to get attributes for sqliteErrorIndicatorFile %@: %@"
+ "Unable to register PLPhotoLibrary with bundle: bundle already shut down (reason: %{public}@ / %ld)"
+ "Unable to resolve TCC service for Siri access"
+ "Unexpected Cloud Photo Library state"
+ "Unexpected nil CSSearchableIndex"
+ "UpdateAccessRequest: Collection share %{public}@ is not published"
+ "UpdateAccessRequest: Failed to create scope change for collection share %{public}@"
+ "UpdateAccessRequest: Failed to move participant %{public}@ to %{public}@ for collection share %{public}@: %@"
+ "UpdateAccessRequest: Moved participant %{public}@ to %{public}@ for collection share %{public}@, updated scope change: %@"
+ "UpdateAccessRequest: Moving participant %{public}@ to %{public}@ for collection share %{public}@"
+ "UpdateAccessRequest: Participant %{public}@ is %{public}@, cannot be moved to %{public}@ in collection share %{public}@"
+ "UpdateAccessRequest: Participant %{public}@ is missing from the scope change for collection share %{public}@"
+ "UpdateAccessRequest: Received nil CPLScopeChange back from CPLLibraryManager for collection share %{public}@"
+ "Updating scores for %tu lexemes in system Leo store"
+ "Using master thumbnail during resource clone of placeholder Asset: %@"
+ "Visual Intelligence library already keeps originals"
+ "Will report search indexing progress"
+ "Zone was wiped for an unsupported app library with main scope identifier: %@, library identifier: %@/%@"
+ "Zone was wiped for app library with main scope identifier: %{public}@, library identifier: %{public}@/%{public}@"
+ "[Biome][Photos.Delete] Asset %{private}@ has no creation date; donating without an age classification"
+ "[Biome][Photos.Delete] Skipping delete donation: asset has no uuid"
+ "[Biome][Photos.Delete] Skipping delete donation: not supported on this platform"
+ "[RM] %@ Finalized deferred finalization image/video resource exists but proxy is missing, promoting to original. resource: %{public}@, asset: %{public}@, path: %{public}@"
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
+ "_restoreMissingCollectionSharePosts"
+ "_restoreMissingCollectionSharePosts: failed to read the cloud cache: %{public}@"
+ "_restoreMissingCollectionSharePosts: looking for %{public}lu missing collection share posts"
+ "_restoreMissingCollectionSharePosts: no cloud photo library manager"
+ "_restoreMissingCollectionSharePosts: no collection share assets are missing their post"
+ "_restoreMissingCollectionSharePosts: restored %{public}lu of %{public}lu missing posts"
+ "addAssetWithURLs: unable to find uuid for main URL: %{public}@"
+ "additionalAttributes.destinationAssetCopyState"
+ "album %@ has %lu missing assets and %lu known assets to check for missing comments"
+ "assertion failure: \"node != ((void*)0)\" -> %llu"
+ "assertion failure: Couldn't find container class for node: %@"
+ "assertion failure: _lock_canAcceptResponders returned YES but _lock_addResponder failed"
+ "assertion failure: shouldSaveMediaConversionResultBlock is a required parameter"
+ "client rebuilt search index"
+ "com.apple.PhotosViewService"
+ "com.apple.TCC.%s.authorization.changed"
+ "com.apple.photos.siri-access-changed"
+ "container was wiped by encrypted data reset"
+ "contributorUserIdentifier"
+ "criteriaNeedingProcessing(in:currentCriteria:outSignalAgainDate:)"
+ "deactivate with no apple account"
+ "direct deactivate on check-enable"
+ "direct deactivate via accounts"
+ "file coordination did not grant a read claim for %@"
+ "fileCoordinator"
+ "isLowConfidence: %@, "
+ "key_biomeDeletedAssetCreationDateByAssetUUID"
+ "lastBundleShutdownDate"
+ "lastBundleShutdownLibraryID"
+ "lastBundleShutdownReason"
+ "leo donatable item: %{public}@ object of entity %{public}@ uuid: %{public}@ "
+ "managed Leo store donate and delete"
+ "migrateLimitedLibraryAccessFromApplication requires non-nil old and new bundle identifiers"
+ "migrateLimitedLibraryAccessFromApplication: %@"
+ "migrateLimitedLibraryAccessFromApplication: requires non-nil old and new bundle identifiers"
+ "no CPL settings"
+ "nodeContainerClass: %{public}@ is not a kind of %{public}@ for node: %{public}@"
+ "participantsWithUserIdentifiers: called without a scope for user identifiers %@; reporting no participants"
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
+ "zone was deleted by user"
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
- "##### %@ PLGenericChangeNotification: %@"
- "##### %@ PLGenericChangeNotification: TOO LARGE"
- "##### %@ PLGenericChangeNotification: UNKNOWN MERGE"
- "##### %@ _notifyALAssetsLibraryWithChanges: %@"
- "##### %@ insertedAlbumOIDs: %@"
- "##### %@ updatedAlbumOIDs: %@"
- "##### %@ updatedAssetOIDs: %@"
- "##### %@ updatedAssetOIDsFiltered: %@"
- "%@ %@ cloudAssetGUIDs %@ album %@"
- "%@ %@[%@] -> %@"
- "%@ -- store %@ vs. plist %@"
- "%@ setting _shouldDeferTask to YES"
- "%@-GM"
- "%@: failed to find invitation GUIDs %@ to resend"
- "%{public}@ -- failed to save %ld asset mappings for store %{public}@: %{public}@"
- "%{public}@ -- saved %ld asset mappings for store %{public}@"
- "%{public}@: PLManagedAsset = %{public}@, like count = %tu, PLCloudCommentsChangeNotification = %@"
- "+setCloudAlbumSharingEnabled %@"
- "-[PLBackgroundJobGuestAssetSyncWorker workItemsNeedingProcessingInLibrary:validCriterias:]"
- "-[PLBackgroundJobPersonSyncWorker workItemsNeedingProcessingInLibrary:validCriterias:]"
- "-[PLBackgroundJobService _inq_pendingJobsForBundle:workerTypes:validCriterias:]"
- "-[PLCloudPhotoLibraryManager _deactivateCPLSyncWithResetMode:willBecomeNonSyncableReason:]"
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
- "/System/Library/../../AppleInternal/Library/Frameworks/TapToRadarKit.framework/Contents/MacOS/TapToRadarKit"
- "/private"
- "<%@ %p> "
- "<%@: %p> asset: %p, snapshot: %p"
- "<%@:%p adjustments=%@ masks=%@>"
- "<%@:%p identifer=%@ maskUUID=%@ enabled=%d settings=%@"
- "@\"NSMutableArray\"20@?0@\"NSArray\"8B16"
- "ALAssetsLibraryLoggingEnabled"
- "ANY %K.%K > %K"
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
- "Class getRadarComponentClass(void)_block_invoke"
- "Class getRadarDraftClass(void)_block_invoke"
- "Class getTapToRadarServiceClass(void)_block_invoke"
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
- "Ignoring request to load file system data during OTA restore [%{public}@] needs to prepare for background restore is %{public}@"
- "Index rebuild paused"
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
- "Notification handler for %s failed to get an LSM for the SPL"
- "Notification handler for %s failed to open the library: %@"
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
- "PL-PILongExposureFusionAutoCalculator"
- "PLCloudCommentsDidChangeNotification"
- "PLCloudFeedEntriesDidChangeNotification"
- "PLGenericChangeNotification"
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
- "PLSearchLeoDonationCurationAmbientEnabled"
- "PLSearchLeoDonationCurationAmbientEnabled: %d"
- "PLSearchLeoDonationCurationAmbientSceneEnabled"
- "PLSearchLeoDonationCurationAmbientSceneEnabled: %d"
- "PLSpotlightQueryUtilities.m"
- "Paused search index rebuild"
- "Photos cannot proceed with the library in its current state.\n\n%@\n\nSelect \"Rebuild\" to allow rebuild of the photo library database (possible data loss) or \"Not now\" to stop now and leave it as-is"
- "PhotosIDExtraction"
- "Preparing to rebuild search index for library: %@"
- "Preserving not-yet-pushed key asset %{public}@ on CollectionShare %{public}@ against no-key scope change"
- "RadarComponent"
- "RadarDraft"
- "Rebuild in progress, but required rebuild type is %{public}@"
- "Rebuild preparation complete, starting reindexing, rebuild type: %{public}@, reasons: %{public}@, called by: %{public}@"
- "Received notification %s"
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
- "SensitiveContentAnalysis"
- "Set prefetch mode requires cloud sync enabled"
- "SharePost %@ has no assets with matching cloudBatchID, deleting post"
- "Should NOT show PLRebuildUserNotification because of snooze until %@"
- "SiriCanLearnFromAppBlacklist"
- "Skipping exported item of unexpected class: %{public}@"
- "Start index rebuild event: %{public}@"
- "System leo delete items failed with error: %@"
- "System leo donate items failed with error: %@"
- "System leo store is nil, possible force close during indexing"
- "System leo update lexemes with entity scores failed with error: %@"
- "TapToRadarService"
- "TapToRadarService draft submitted"
- "TapToRadarService returned error: (%@)"
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
- "VectorIndex"
- "Workers that reported pending jobs on well known library identifier %@:\n"
- "Zone was wiped for app library with main scope identifier: %{public}@"
- "[ERROR] Could not create unarchiver for revGeoLocationData with error:%@"
- "[RM] %@ Deferred finalization resource exists but proxy is missing, promoting to original. resource: %{public}@, asset: %{public}@, path: %{public}@"
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
- "com.apple.photos.suggestions-settings-changed"
- "com.apple.suggestions"
- "com.apple.suggestions.settingsChanged"
- "criteriaNeedingProcessing(in:validCriterias:outSignalAgainDate:)"
- "current"
- "deleted=%@"
- "deletedAssetGroups"
- "dictionary"
- "envelope must not be nil"
- "errors"
- "exception"
- "expected"
- "found plAlbum %@ with invitationRecords %lu"
- "groupingUUID == %@"
- "input"
- "inserted=%@"
- "insertedAssetGroups"
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
- "softlink:o:path:/System/Library/../../AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit"
- "some workers"
- "spa_detection"
- "state information archive for %@ too large"
- "system leo deleteItems"
- "system leo donateItems"
- "system leo updateLexemesWithEntityScores"
- "uicmd"
- "unable to archive process state information for %@: %@"
- "updateCloudSharedAlbumMultipleContributorsStateOnServer:(%@ guid %@ requestedEnabledValue %i previousEnabledValue %i)"
- "updateCloudSharedAlbumPublicURLStateOnServer:(%@ guid %@ requestedEnabledValue %i previousEnabledValue %i)"
- "updated=%@"
- "updatedAssetGroups"
- "updatedAssets"
- "v16@?0@\"TapToRadarServiceSettings\"8"
- "v32@?0@\"NSSet\"8@\"NSMutableArray\"16@\"NSMutableArray\"24"
- "v32@?0@\"PLNotification\"8Q16^B24"
- "v40@?0@\"AVAsset\"8@\"AVAudioMix\"16@\"AVVideoComposition\"24@\"NSError\"32"
- "void *TapToRadarKitLibrary(void)"
- "will call -[PLCloudSharedDeleteAlbumsJob deleteLocalAlbumsForMSASAlbumGUIDs:albumGUIDs:] with arguments %@"
- "workItemsNeedingProcessing(in:validCriterias:)"
- "{PLConcurrencyLimiterRecordingAggregateEntry=IIIIQQQQ[8C]}"
- "\xf1"
```
