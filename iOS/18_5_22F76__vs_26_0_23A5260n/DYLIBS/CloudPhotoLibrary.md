## CloudPhotoLibrary

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary`

```diff

-760.6.150.0.0
-  __TEXT.__text: 0x18b278
-  __TEXT.__auth_stubs: 0xef0
-  __TEXT.__objc_methlist: 0x12b9c
-  __TEXT.__const: 0x2e8
-  __TEXT.__gcc_except_tab: 0x41dc
-  __TEXT.__oslogstring: 0x14102
-  __TEXT.__cstring: 0x13533
-  __TEXT.__unwind_info: 0x59a8
-  __TEXT.__objc_classname: 0x1d77
-  __TEXT.__objc_methname: 0x29f1d
-  __TEXT.__objc_methtype: 0x451e
-  __TEXT.__objc_stubs: 0x198c0
-  __DATA_CONST.__got: 0xa28
-  __DATA_CONST.__const: 0x5df8
-  __DATA_CONST.__objc_classlist: 0x848
+800.14.111.0.0
+  __TEXT.__text: 0x1950b4
+  __TEXT.__auth_stubs: 0xf00
+  __TEXT.__objc_methlist: 0x12f3c
+  __TEXT.__const: 0x2f8
+  __TEXT.__gcc_except_tab: 0x4510
+  __TEXT.__oslogstring: 0x146cf
+  __TEXT.__cstring: 0x13fc3
+  __TEXT.__unwind_info: 0x5ae8
+  __TEXT.__objc_classname: 0x1e05
+  __TEXT.__objc_methname: 0x2a95e
+  __TEXT.__objc_methtype: 0x456b
+  __TEXT.__objc_stubs: 0x19d00
+  __DATA_CONST.__got: 0xa38
+  __DATA_CONST.__const: 0x60f0
+  __DATA_CONST.__objc_classlist: 0x878
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8388
+  __DATA_CONST.__objc_selrefs: 0x8510
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x7f0
-  __DATA_CONST.__objc_arraydata: 0x12d0
-  __AUTH_CONST.__auth_got: 0x788
-  __AUTH_CONST.__const: 0x25a0
-  __AUTH_CONST.__cfstring: 0x14a20
-  __AUTH_CONST.__objc_const: 0x1d538
-  __AUTH_CONST.__objc_intobj: 0x570
+  __DATA_CONST.__objc_superrefs: 0x810
+  __DATA_CONST.__objc_arraydata: 0x1320
+  __AUTH_CONST.__auth_got: 0x790
+  __AUTH_CONST.__const: 0x25c0
+  __AUTH_CONST.__cfstring: 0x154c0
+  __AUTH_CONST.__objc_const: 0x1dea8
+  __AUTH_CONST.__objc_intobj: 0x5b8
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x1734
-  __DATA.__data: 0xf30
-  __DATA.__bss: 0x890
+  __AUTH.__objc_data: 0x500
+  __DATA.__objc_ivar: 0x17bc
+  __DATA.__data: 0xf48
+  __DATA.__bss: 0xa88
   __DATA.__common: 0x21
-  __DATA_DIRTY.__objc_data: 0x5230
-  __DATA_DIRTY.__data: 0x9
-  __DATA_DIRTY.__bss: 0x580
+  __DATA_DIRTY.__objc_data: 0x4fb0
+  __DATA_DIRTY.__bss: 0x3a0
   __DATA_DIRTY.__common: 0x8
+  - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/MMCS.framework/MMCS
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcupolicy.dylib
-  - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 12323653-B73A-378C-B466-E996A6FD05BD
-  Functions: 8275
-  Symbols:   25562
-  CStrings:  14480
+  UUID: B130BC07-4FAB-3566-850B-88F6E2D44EEF
+  Functions: 8407
+  Symbols:   25972
+  CStrings:  14792
 
Symbols:
+ +[CPLAssetChange supportsCollectionShare]
+ +[CPLCommentChange supportsCollectionShare]
+ +[CPLCommentChange supportsDeletion]
+ +[CPLCommentChange supportsDirectDeletion]
+ +[CPLCommentChange supportsRecordModificationDate]
+ +[CPLEngineScheduler shouldShowBackgroundSchedulingStatusInTransport]
+ +[CPLErrors unableToDeserializeRecordInStorage:]
+ +[CPLErrors unableToSerializeRecordError:inStorage:]
+ +[CPLMasterChange supportsCollectionShare]
+ +[CPLReactChange(CPLPlaceholderRecord) relatedRecordClass]
+ +[CPLRecordChange supportsCollectionShare]
+ +[CPLRecordChange supportsRecordModificationDate]
+ +[CPLScopeChange supportsActivationOfScopeWithType:]
+ +[CPLSyncSessionPrediction maximumSignificantTimeInterval]
+ +[CPLTextCommentChange(CPLPlaceholderRecord) relatedRecordClass]
+ -[CPLArchiver _createContext]
+ -[CPLArchiver archiverContext]
+ -[CPLCommentChange .cxx_destruct]
+ -[CPLCommentChange assetIdentifier]
+ -[CPLCommentChange assetScopedIdentifier]
+ -[CPLCommentChange commentDate]
+ -[CPLCommentChange relatedIdentifier]
+ -[CPLCommentChange setAssetIdentifier:]
+ -[CPLCommentChange setAssetScopedIdentifier:]
+ -[CPLCommentChange setCommentDate:]
+ -[CPLCommentChange setRelatedIdentifier:]
+ -[CPLCommentChange validateChangeWithError:]
+ -[CPLCommentChange validateFullRecord]
+ -[CPLEngineDerivativesCache _cachedResourcesForReferenceResource:adjustment:includePosterFrame:]
+ -[CPLEngineDerivativesCache _cleanTempFolderURLForGeneratedResourcesWithReferenceResource:adjustment:includePosterFrame:]
+ -[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]
+ -[CPLEngineDerivativesCache _noteGeneratedResources:haveBeenGeneratedForReferenceResource:adjustment:includePosterFrame:]
+ -[CPLEngineLibrary updateBlockedMetrics:syncRequested:runtimeCharacteristics:]
+ -[CPLEngineResourceDownloadQueue _cloudResourceForLocalResource:cloudRecord:target:shouldNotTrustCaches:allowUnsafeClientCache:allowBypassingAllCaches:transportScopeMapping:error:]
+ -[CPLEngineScheduler _allowsJustInCaseSessions]
+ -[CPLEngineScheduler _justInCaseSessionIsPossible]
+ -[CPLEngineScheduler _noteSignificantEvent]
+ -[CPLEngineScheduler noteBlockedStateHasChanged:]
+ -[CPLEngineScope copyWithScopeType:]
+ -[CPLEngineScopeStorage _isAvailableSharingScope:]
+ -[CPLEngineStorage scopeIndexes]
+ -[CPLEngineStore _forceCloseWithCompletionHandler:]
+ -[CPLEngineStore clientCanPushScopeChange:]
+ -[CPLEngineStore storeVersionHasChanged]
+ -[CPLEngineTransport getBackgroundSchedulingStatusDictionaryWithCompletionHandler:]
+ -[CPLEngineTransport getBackgroundSchedulingStatusWithCompletionHandler:]
+ -[CPLLibraryManager initForLightweightUsageWithLibraryIdentifier:]
+ -[CPLMingleChangesScopeTask _shouldStashMasterRecords]
+ -[CPLPredictionDateFormatter stringForObjectValue:]
+ -[CPLPredictionDateFormatter stringForTimeIntervalNumber:now:]
+ -[CPLProxyLibraryManager _dispatchBlockWhenOpen:].cold.5
+ -[CPLPullScopesTask taskDidFinishWithError:]
+ -[CPLPushSessionTracker cleanupWithError:]
+ -[CPLPushSessionTracker deletedScopeIdentifiers]
+ -[CPLPushSessionUpdate deletedScopeIdentifiers]
+ -[CPLReactChange(CPLIDMapping) scopedIdentifiersForMapping]
+ -[CPLReactChange(CPLIDMapping) translateToClientChangeUsingIDMapping:error:]
+ -[CPLReactChange(CPLIDMapping) translateToCloudChangeUsingIDMapping:error:]
+ -[CPLRecordChange contributorUserIdentifier]
+ -[CPLRecordChange proposedCloudScopedIdentifier]
+ -[CPLRecordChange setContributorUserIdentifier:]
+ -[CPLRecordChange supportsCollectionShare]
+ -[CPLRecordChange supportsRecordModificationDate]
+ -[CPLResourceTransferTaskOptions allowsUnsafeClientCache]
+ -[CPLResourceTransferTaskOptions initWithIntent:bypassCaches:priority:]
+ -[CPLResourceTransferTaskOptions initWithIntent:priority:bypassCaches:timeRange:]
+ -[CPLResourceTransferTaskOptions shouldBypassCaches]
+ -[CPLScopedIdentifier initWithStringRepresentation:defaultScopeIdentifier:]
+ -[CPLScopedIdentifier isInACPLShare]
+ -[CPLScopedIdentifier stringRepresentation]
+ -[CPLShare setTransportShare:]
+ -[CPLShare transportShare]
+ -[CPLSyncSession isJustInCaseSession]
+ -[CPLSyncSession runtimeCharacteristics]
+ -[CPLSyncSession setIsJustInCaseSession:]
+ -[CPLSyncSession shouldBeTemporarilyNonDiscretionary]
+ -[CPLSyncSessionBlockedState .cxx_destruct]
+ -[CPLSyncSessionBlockedState initWithRescheduler:blocked:syncHasBeenRequested:runtimeCharacteristics:]
+ -[CPLSyncSessionBlockedState isBlocked]
+ -[CPLSyncSessionBlockedState rescheduler]
+ -[CPLSyncSessionBlockedState runtimeCharacteristics]
+ -[CPLSyncSessionBlockedState syncHasBeenRequested]
+ -[CPLSyncSessionPrediction descriptionWithNow:]
+ -[CPLSyncSessionPrediction predictedDateForType:]
+ -[CPLSyncSessionPrediction timeIntervalSincePredictedDateForType:]
+ -[CPLSyncSessionPrediction updatedPredictionRemovingValueForType:]
+ -[CPLSyncSessionPredictor removePredictedValueForType:]
+ -[CPLSyncSessionPredictor updatePredictedDate:forType:]
+ -[CPLTextCommentChange .cxx_destruct]
+ -[CPLTextCommentChange commentText]
+ -[CPLTextCommentChange setCommentText:]
+ -[CPLTextCommentChange(CPLIDMapping) scopedIdentifiersForMapping]
+ -[CPLTextCommentChange(CPLIDMapping) translateToClientChangeUsingIDMapping:error:]
+ -[CPLTextCommentChange(CPLIDMapping) translateToCloudChangeUsingIDMapping:error:]
+ -[CPLUploadPushedChangesTask _discardGenerateDerivativesProgress]
+ -[CPLUploadPushedChangesTask _generatingDerivativesForChange:fractionCompleted:chunkLength:]
+ -[CPLUploadPushedChangesTask _installGenerateDerivativesCancellationHandler:]
+ -[CPLUploadPushedChangesTask observeValueForKeyPath:ofObject:change:context:]
+ GCC_except_table1001
+ GCC_except_table1003
+ GCC_except_table1175
+ GCC_except_table1222
+ GCC_except_table1227
+ GCC_except_table1231
+ GCC_except_table1239
+ GCC_except_table1241
+ GCC_except_table1248
+ GCC_except_table1251
+ GCC_except_table1254
+ GCC_except_table1260
+ GCC_except_table1262
+ GCC_except_table1343
+ GCC_except_table1429
+ GCC_except_table1977
+ GCC_except_table207
+ GCC_except_table2084
+ GCC_except_table2090
+ GCC_except_table2131
+ GCC_except_table2219
+ GCC_except_table222
+ GCC_except_table2226
+ GCC_except_table228
+ GCC_except_table231
+ GCC_except_table233
+ GCC_except_table235
+ GCC_except_table2369
+ GCC_except_table2456
+ GCC_except_table2680
+ GCC_except_table2682
+ GCC_except_table2768
+ GCC_except_table2833
+ GCC_except_table2835
+ GCC_except_table2955
+ GCC_except_table2979
+ GCC_except_table3055
+ GCC_except_table3059
+ GCC_except_table3061
+ GCC_except_table3063
+ GCC_except_table3067
+ GCC_except_table3188
+ GCC_except_table3235
+ GCC_except_table324
+ GCC_except_table3479
+ GCC_except_table3548
+ GCC_except_table3552
+ GCC_except_table3554
+ GCC_except_table3563
+ GCC_except_table374
+ GCC_except_table383
+ GCC_except_table3843
+ GCC_except_table3873
+ GCC_except_table3900
+ GCC_except_table3917
+ GCC_except_table3924
+ GCC_except_table3932
+ GCC_except_table3934
+ GCC_except_table3948
+ GCC_except_table3950
+ GCC_except_table3952
+ GCC_except_table4289
+ GCC_except_table4421
+ GCC_except_table4431
+ GCC_except_table446
+ GCC_except_table4488
+ GCC_except_table4491
+ GCC_except_table450
+ GCC_except_table4666
+ GCC_except_table4674
+ GCC_except_table4754
+ GCC_except_table4758
+ GCC_except_table4762
+ GCC_except_table4767
+ GCC_except_table4782
+ GCC_except_table4783
+ GCC_except_table4787
+ GCC_except_table481
+ GCC_except_table4831
+ GCC_except_table4839
+ GCC_except_table4894
+ GCC_except_table4896
+ GCC_except_table4898
+ GCC_except_table4910
+ GCC_except_table498
+ GCC_except_table499
+ GCC_except_table5049
+ GCC_except_table508
+ GCC_except_table5091
+ GCC_except_table5100
+ GCC_except_table5101
+ GCC_except_table5160
+ GCC_except_table5163
+ GCC_except_table526
+ GCC_except_table535
+ GCC_except_table5437
+ GCC_except_table5465
+ GCC_except_table5507
+ GCC_except_table5527
+ GCC_except_table5553
+ GCC_except_table5564
+ GCC_except_table5585
+ GCC_except_table5605
+ GCC_except_table5609
+ GCC_except_table5635
+ GCC_except_table5667
+ GCC_except_table5766
+ GCC_except_table5807
+ GCC_except_table5820
+ GCC_except_table5831
+ GCC_except_table5838
+ GCC_except_table5891
+ GCC_except_table6016
+ GCC_except_table6029
+ GCC_except_table6032
+ GCC_except_table638
+ GCC_except_table644
+ GCC_except_table6512
+ GCC_except_table6551
+ GCC_except_table6555
+ GCC_except_table6557
+ GCC_except_table6572
+ GCC_except_table6578
+ GCC_except_table6586
+ GCC_except_table6592
+ GCC_except_table6596
+ GCC_except_table6604
+ GCC_except_table6607
+ GCC_except_table6627
+ GCC_except_table6634
+ GCC_except_table6657
+ GCC_except_table6691
+ GCC_except_table6715
+ GCC_except_table6724
+ GCC_except_table6742
+ GCC_except_table6745
+ GCC_except_table6747
+ GCC_except_table6749
+ GCC_except_table675
+ GCC_except_table6781
+ GCC_except_table679
+ GCC_except_table6851
+ GCC_except_table699
+ GCC_except_table6996
+ GCC_except_table701
+ GCC_except_table7018
+ GCC_except_table703
+ GCC_except_table7048
+ GCC_except_table705
+ GCC_except_table717
+ GCC_except_table719
+ GCC_except_table721
+ GCC_except_table7231
+ GCC_except_table7240
+ GCC_except_table7245
+ GCC_except_table7259
+ GCC_except_table7273
+ GCC_except_table728
+ GCC_except_table7283
+ GCC_except_table7288
+ GCC_except_table730
+ GCC_except_table732
+ GCC_except_table734
+ GCC_except_table736
+ GCC_except_table7367
+ GCC_except_table7448
+ GCC_except_table745
+ GCC_except_table7457
+ GCC_except_table747
+ GCC_except_table749
+ GCC_except_table751
+ GCC_except_table7513
+ GCC_except_table753
+ GCC_except_table7550
+ GCC_except_table7566
+ GCC_except_table7574
+ GCC_except_table7575
+ GCC_except_table7589
+ GCC_except_table779
+ GCC_except_table788
+ GCC_except_table795
+ GCC_except_table806
+ GCC_except_table897
+ GCC_except_table983
+ _CPLArchiverFailureContextKey
+ _CPLArchiverFailureExceptionName
+ _CPLCollectionSharePrefixForScopeWithIdentifier
+ _CPLForceCollectionShareFeatureEnabled
+ _CPLGetAppBoundaryKey
+ _CPLIsCollectionShareFeatureEnabled
+ _CPLLibraryManagerStreamingHintVideoCodec
+ _CPLLibraryManagerStreamingHintVideoDuration
+ _CPLLibraryManagerStreamingHintVideoNominalFrameRate
+ _CPLLibraryManagerStreamingHintVideoOrientedHeight
+ _CPLLibraryManagerStreamingHintVideoOrientedWidth
+ _CPLScopeIdentifierPrefixForCollectionShare
+ _CPLScopeIdentifierPrefixForCollectionShareForParallelUniverse
+ _CPLSyncSessionPredictionTypeLastSignificantEventDate
+ _NSInternalInconsistencyException
+ _OBJC_CLASS_$_ACAccountStore
+ _OBJC_CLASS_$_CPLCollectionShareScopeChange
+ _OBJC_CLASS_$_CPLCommentChange
+ _OBJC_CLASS_$_CPLPredictionDateFormatter
+ _OBJC_CLASS_$_CPLReactChange
+ _OBJC_CLASS_$_CPLSyncSessionBlockedState
+ _OBJC_CLASS_$_CPLTextCommentChange
+ _OBJC_CLASS_$_NSIndexSet
+ _OBJC_IVAR_$_CPLArchiver._context
+ _OBJC_IVAR_$_CPLArchiver._popContext
+ _OBJC_IVAR_$_CPLArchiver._pushContext
+ _OBJC_IVAR_$_CPLArchiver._unarchiving
+ _OBJC_IVAR_$_CPLCommentChange._assetIdentifier
+ _OBJC_IVAR_$_CPLCommentChange._commentDate
+ _OBJC_IVAR_$_CPLEngineDerivativesCache._delayedGeneratedDerivativesCalls
+ _OBJC_IVAR_$_CPLEngineDerivativesCache._isGeneratingDerivatives
+ _OBJC_IVAR_$_CPLEngineScheduler._nextSessionIsJustInCase
+ _OBJC_IVAR_$_CPLEngineSyncManager._lastSyncSessionDescription
+ _OBJC_IVAR_$_CPLEngineSyncManager._lastSyncSessionEndDate
+ _OBJC_IVAR_$_CPLEngineSyncManager._lastSyncSessionStartDate
+ _OBJC_IVAR_$_CPLMingleChangesScopeTask._didLogShouldStashMasterRecords
+ _OBJC_IVAR_$_CPLProxyLibraryManager._logKilled
+ _OBJC_IVAR_$_CPLPullScopesTask._hasSeenSomeChanges
+ _OBJC_IVAR_$_CPLPushSessionTracker._changesWithMissingIDMapping
+ _OBJC_IVAR_$_CPLPushSessionTracker._deletedScopeIdentifiers
+ _OBJC_IVAR_$_CPLPushSessionTracker._optimisticIDMapping
+ _OBJC_IVAR_$_CPLPushSessionTracker._realIDMapping
+ _OBJC_IVAR_$_CPLPushSessionUpdate._deletedScopeIdentifiers
+ _OBJC_IVAR_$_CPLRecordChange._contributorUserIdentifier
+ _OBJC_IVAR_$_CPLResourceTransferTaskOptions._shouldBypassCaches
+ _OBJC_IVAR_$_CPLShare._transportShare
+ _OBJC_IVAR_$_CPLSyncSession._descriptionSuffix
+ _OBJC_IVAR_$_CPLSyncSession._isJustInCaseSession
+ _OBJC_IVAR_$_CPLSyncSession._shouldBeTemporarilyNonDiscretionary
+ _OBJC_IVAR_$_CPLSyncSessionBlockedState._blocked
+ _OBJC_IVAR_$_CPLSyncSessionBlockedState._rescheduler
+ _OBJC_IVAR_$_CPLSyncSessionBlockedState._runtimeCharacteristics
+ _OBJC_IVAR_$_CPLSyncSessionBlockedState._syncHasBeenRequested
+ _OBJC_IVAR_$_CPLTextCommentChange._commentText
+ _OBJC_IVAR_$_CPLUploadPushedChangesTask._generateDerivativesCancellationHandler
+ _OBJC_IVAR_$_CPLUploadPushedChangesTask._generateDerivativesChange
+ _OBJC_IVAR_$_CPLUploadPushedChangesTask._generateDerivativesDeferredHandler
+ _OBJC_IVAR_$_CPLUploadPushedChangesTask._generateDerivativesLastFractionCompleted
+ _OBJC_IVAR_$_CPLUploadPushedChangesTask._generateDerivativesProgress
+ _OBJC_IVAR_$_CPLUploadPushedChangesTask._generateDerivativesTotalSize
+ _OBJC_METACLASS_$_CPLCollectionShareScopeChange
+ _OBJC_METACLASS_$_CPLCommentChange
+ _OBJC_METACLASS_$_CPLPredictionDateFormatter
+ _OBJC_METACLASS_$_CPLReactChange
+ _OBJC_METACLASS_$_CPLSyncSessionBlockedState
+ _OBJC_METACLASS_$_CPLTextCommentChange
+ _PLCoreAnalyticsLibrarySummaryiCPLSyncSessionActivityMotionStateBlockedCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLSyncSessionConsoleModeBlockedCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLSyncSessionDASDoItNowUnBlockedCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLSyncSessionDeviceActivityBlockedCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLSyncSessionDeviceActivityEarlyThermalWarningBlockedCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLSyncSessionSignificantTransferBlockedCountKey
+ __CPLArchiverFailure
+ __ClassesForInitialQueries.classesForInitialQueriesInCollectionShare
+ __OBJC_$_CLASS_METHODS_CPLCommentChange
+ __OBJC_$_CLASS_METHODS_CPLReactChange(CPLIDMapping|CPLPlaceholderRecord)
+ __OBJC_$_CLASS_METHODS_CPLSyncSessionPrediction
+ __OBJC_$_CLASS_METHODS_CPLTextCommentChange(CPLIDMapping|CPLPlaceholderRecord)
+ __OBJC_$_CLASS_PROP_LIST_CPLEngineScheduler
+ __OBJC_$_CLASS_PROP_LIST_CPLSyncSessionPrediction
+ __OBJC_$_INSTANCE_METHODS_CPLCommentChange
+ __OBJC_$_INSTANCE_METHODS_CPLPredictionDateFormatter
+ __OBJC_$_INSTANCE_METHODS_CPLReactChange(CPLIDMapping|CPLPlaceholderRecord)
+ __OBJC_$_INSTANCE_METHODS_CPLSyncSessionBlockedState
+ __OBJC_$_INSTANCE_METHODS_CPLTextCommentChange(CPLIDMapping|CPLPlaceholderRecord)
+ __OBJC_$_INSTANCE_VARIABLES_CPLCommentChange
+ __OBJC_$_INSTANCE_VARIABLES_CPLSyncSessionBlockedState
+ __OBJC_$_INSTANCE_VARIABLES_CPLTextCommentChange
+ __OBJC_$_PROP_LIST_CPLCommentChange
+ __OBJC_$_PROP_LIST_CPLSyncSessionBlockedState
+ __OBJC_$_PROP_LIST_CPLTextCommentChange
+ __OBJC_CLASS_RO_$_CPLCollectionShareScopeChange
+ __OBJC_CLASS_RO_$_CPLCommentChange
+ __OBJC_CLASS_RO_$_CPLPredictionDateFormatter
+ __OBJC_CLASS_RO_$_CPLReactChange
+ __OBJC_CLASS_RO_$_CPLSyncSessionBlockedState
+ __OBJC_CLASS_RO_$_CPLTextCommentChange
+ __OBJC_METACLASS_RO_$_CPLCollectionShareScopeChange
+ __OBJC_METACLASS_RO_$_CPLCommentChange
+ __OBJC_METACLASS_RO_$_CPLPredictionDateFormatter
+ __OBJC_METACLASS_RO_$_CPLReactChange
+ __OBJC_METACLASS_RO_$_CPLSyncSessionBlockedState
+ __OBJC_METACLASS_RO_$_CPLTextCommentChange
+ ___105-[CPLLibraryManager startExitFromSharedScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:]_block_invoke.418
+ ___110-[CPLLibraryManager beginDownloadForResource:clientBundleID:options:proposedTaskIdentifier:completionHandler:]_block_invoke.332
+ ___112-[CPLEngineDerivativesCache generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.64
+ ___112-[CPLEngineDerivativesCache generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.70
+ ___112-[CPLEngineDerivativesCache generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.71
+ ___112-[CPLEngineDerivativesCache generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke_3
+ ___112-[CPLEngineDerivativesCache generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke_4
+ ___112-[CPLEngineDerivativesCache generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke_5
+ ___112-[CPLEngineDerivativesCache generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke_6
+ ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke
+ ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.45
+ ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.49
+ ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.60
+ ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke_2
+ ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke_2.54
+ ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke_2.61
+ ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke_3
+ ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke_3.62
+ ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke_4
+ ___115-[CPLLibraryManager removeParticipants:fromSharedScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:]_block_invoke.423
+ ___116-[CPLUploadPushedChangesTask _generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:]_block_invoke.124
+ ___116-[CPLUploadPushedChangesTask _generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:]_block_invoke_2.132
+ ___116-[CPLUploadPushedChangesTask _generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:]_block_invoke_5
+ ___120-[CPLLibraryManager getStreamingURLOrMediaMakerDataForResource:intent:hints:timeRange:clientBundleID:completionHandler:]_block_invoke.338
+ ___122-[CPLLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke.508
+ ___160-[CPLEngineResourceDownloadQueue _downloadTaskForLocalResource:clientBundleID:options:proposedTaskIdentifier:didStartHandler:progressHandler:completionHandler:]_block_invoke.168
+ ___160-[CPLEngineResourceDownloadQueue _downloadTaskForLocalResource:clientBundleID:options:proposedTaskIdentifier:didStartHandler:progressHandler:completionHandler:]_block_invoke.177
+ ___160-[CPLEngineResourceDownloadQueue _downloadTaskForLocalResource:clientBundleID:options:proposedTaskIdentifier:didStartHandler:progressHandler:completionHandler:]_block_invoke.180
+ ___163-[CPLEngineResourceDownloadQueue _realDownloadTaskForLocalResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.201
+ ___163-[CPLEngineResourceDownloadQueue _realDownloadTaskForLocalResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.203
+ ___163-[CPLEngineResourceDownloadQueue _realDownloadTaskForLocalResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke_2.202
+ ___163-[CPLEngineResourceDownloadQueue _realDownloadTaskForLocalResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke_2.204
+ ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.191
+ ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.196
+ ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.197
+ ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.199
+ ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke_2.198
+ ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke_2.200
+ ___35-[CPLEngineStore _handleException:]_block_invoke_2
+ ___35-[CPLEngineStore _handleException:]_block_invoke_3
+ ___36-[CPLPushSessionTracker computeDiff]_block_invoke.44
+ ___36-[CPLPushSessionTracker computeDiff]_block_invoke.49
+ ___36-[CPLPushSessionTracker computeDiff]_block_invoke.55
+ ___36-[CPLPushSessionTracker computeDiff]_block_invoke.68
+ ___36-[CPLPushSessionTracker computeDiff]_block_invoke_2.50
+ ___36-[CPLPushSessionTracker computeDiff]_block_invoke_2.58
+ ___37-[CPLSyncSession isJustInCaseSession]_block_invoke
+ ___37-[CPLUploadPushedChangesTask cancel:]_block_invoke.164
+ ___40-[CPLSyncSession runtimeCharacteristics]_block_invoke
+ ___41-[CPLEngineDerivativesCache discardCache]_block_invoke
+ ___41-[CPLEngineScheduler noteQuotaHasChanged]_block_invoke.150
+ ___41-[CPLSyncSession setIsJustInCaseSession:]_block_invoke
+ ___42-[CPLEngineScheduler _prepareFirstSession]_block_invoke.153
+ ___42-[CPLEngineScheduler _prepareFirstSession]_block_invoke_2.154
+ ___42-[CPLLibraryManager discardCurrentSession]_block_invoke.297
+ ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.254
+ ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.281
+ ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.284
+ ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.288
+ ___47-[CPLLibraryManager openWithCompletionHandler:]_block_invoke.204
+ ___47-[CPLLibraryManager openWithCompletionHandler:]_block_invoke.208
+ ___47-[CPLLibraryManager openWithCompletionHandler:]_block_invoke.211
+ ___48-[CPLMingleChangesScopeTask _mingleOtherChanges]_block_invoke.72
+ ___49-[CPLEngineScheduler noteBlockedStateHasChanged:]_block_invoke
+ ___50+[CPLArchiver displayableDictionaryForDictionary:]_block_invoke.1705
+ ___51-[CPLEngineStore _forceCloseWithCompletionHandler:]_block_invoke
+ ___51-[CPLEngineStore _reallySchedulePendingUpdateApply]_block_invoke.341
+ ___51-[CPLLibraryManager createScope:completionHandler:]_block_invoke.348
+ ___53-[CPLEngineScheduler getStatusWithCompletionHandler:]_block_invoke_6
+ ___53-[CPLSyncSession shouldBeTemporarilyNonDiscretionary]_block_invoke
+ ___54-[CPLLibraryManager forceBackupWithCompletionHandler:]_block_invoke.493
+ ___55-[CPLSyncSessionPredictor removePredictedValueForType:]_block_invoke
+ ___55-[CPLSyncSessionPredictor removePredictedValueForType:]_block_invoke.63
+ ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.147
+ ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.149
+ ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.150
+ ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.151
+ ___56-[CPLEngineStore _closeAndDeactivate:completionHandler:]_block_invoke.328
+ ___57-[CPLLibraryManager acceptSharedScope:completionHandler:]_block_invoke.436
+ ___58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke.216
+ ___58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke.217
+ ___58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke.218
+ ___58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke_2.219
+ ___59-[CPLLibraryManager updateShareForScope:completionHandler:]_block_invoke.350
+ ___60-[CPLUploadPushedChangesTask _uploadTaskDidFinishWithError:]_block_invoke.171
+ ___62-[CPLSyncSessionPredictor updatePredictionWithValuesAndTypes:]_block_invoke.60
+ ___63-[CPLEngineScheduler getStatusDictionaryWithCompletionHandler:]_block_invoke_6
+ ___65-[CPLLibraryManager sharedLibraryRampCheckWithCompletionHandler:]_block_invoke.427
+ ___66-[CPLLibraryManager refreshScopeWithIdentifier:completionHandler:]_block_invoke.365
+ ___67-[CPLEngineScheduler _noteSyncSession:failedDuringPhase:withError:]_block_invoke.133
+ ___67-[CPLEngineScheduler _noteSyncSession:failedDuringPhase:withError:]_block_invoke.134
+ ___67-[CPLEngineScheduler _noteSyncSession:failedDuringPhase:withError:]_block_invoke.135
+ ___68-[CPLEngineScheduler _handleResetAnchorWithError:completionHandler:]_block_invoke.119
+ ___68-[CPLLibraryManager fetchSharedScopeFromShareURL:completionHandler:]_block_invoke.432
+ ___68-[CPLUploadPushedChangesTask _extractBatchWithTransaction:andStore:]_block_invoke_2.79
+ ___72-[CPLLibraryManager deleteScopeWithIdentifier:forced:completionHandler:]_block_invoke.361
+ ___72-[CPLLibraryManager requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.497
+ ___74-[CPLEngineScheduler _handleResetGlobalAnchorWithError:completionHandler:]_block_invoke.123
+ ___74-[CPLLibraryManager fetchExistingSharedLibraryScopeWithCompletionHandler:]_block_invoke.440
+ ___76-[CPLLibraryManager queryUserDetailsForShareParticipants:completionHandler:]_block_invoke.445
+ ___77-[CPLUploadPushedChangesTask _installGenerateDerivativesCancellationHandler:]_block_invoke
+ ___77-[CPLUploadPushedChangesTask _installGenerateDerivativesCancellationHandler:]_block_invoke_2
+ ___77-[CPLUploadPushedChangesTask _installGenerateDerivativesCancellationHandler:]_block_invoke_3
+ ___77-[CPLUploadPushedChangesTask observeValueForKeyPath:ofObject:change:context:]_block_invoke
+ ___78-[CPLEngineLibrary updateBlockedMetrics:syncRequested:runtimeCharacteristics:]_block_invoke
+ ___78-[CPLLibraryManager forceSynchronizingScopeWithIdentifiers:completionHandler:]_block_invoke.448
+ ___78-[CPLMingleChangesScopeTask _filteredBatchByStashingRecordsIfNecessary:error:]_block_invoke.59
+ ___79-[CPLLibraryManager checkHasBackgroundDownloadOperationsWithCompletionHandler:]_block_invoke.470
+ ___80-[CPLEngineCloudCache cloudChangeBatchFromBatch:usingMapping:isFinal:withError:]_block_invoke.31
+ ___82-[CPLLibraryManager rampingRequestForResourceType:numRequested:completionHandler:]_block_invoke.342
+ ___84-[CPLEngineStore _performWriteTransactionByPassBlocker:WithBlock:completionHandler:]_block_invoke.302
+ ___86-[CPLLibraryManager beginInMemoryDownloadOfResource:clientBundleID:completionHandler:]_block_invoke.344
+ ___87-[CPLLibraryManager requestClientToPullAllChangesInScopeIdentifiers:completionHandler:]_block_invoke.501
+ ___94-[CPLPullScopesTask _handleChangedOrNewScopes:deletedScopeIdentifiers:newScopeListSyncAnchor:]_block_invoke.3
+ ___94-[CPLPullScopesTask _handleChangedOrNewScopes:deletedScopeIdentifiers:newScopeListSyncAnchor:]_block_invoke.7
+ ___Block_byref_object_copy_.1013
+ ___Block_byref_object_copy_.11171
+ ___Block_byref_object_copy_.11464
+ ___Block_byref_object_copy_.1181
+ ___Block_byref_object_copy_.12222
+ ___Block_byref_object_copy_.13039
+ ___Block_byref_object_copy_.1346
+ ___Block_byref_object_copy_.13620
+ ___Block_byref_object_copy_.13946
+ ___Block_byref_object_copy_.14133
+ ___Block_byref_object_copy_.14950
+ ___Block_byref_object_copy_.15551
+ ___Block_byref_object_copy_.16272
+ ___Block_byref_object_copy_.16594
+ ___Block_byref_object_copy_.17066
+ ___Block_byref_object_copy_.1747
+ ___Block_byref_object_copy_.17667
+ ___Block_byref_object_copy_.18490
+ ___Block_byref_object_copy_.19961
+ ___Block_byref_object_copy_.20101
+ ___Block_byref_object_copy_.2055
+ ___Block_byref_object_copy_.20611
+ ___Block_byref_object_copy_.21225
+ ___Block_byref_object_copy_.21707
+ ___Block_byref_object_copy_.22044
+ ___Block_byref_object_copy_.23057
+ ___Block_byref_object_copy_.23356
+ ___Block_byref_object_copy_.24118
+ ___Block_byref_object_copy_.2551
+ ___Block_byref_object_copy_.2628
+ ___Block_byref_object_copy_.2951
+ ___Block_byref_object_copy_.3268
+ ___Block_byref_object_copy_.5787
+ ___Block_byref_object_copy_.6487
+ ___Block_byref_object_copy_.6638
+ ___Block_byref_object_copy_.677
+ ___Block_byref_object_copy_.7200
+ ___Block_byref_object_copy_.7580
+ ___Block_byref_object_copy_.7859
+ ___Block_byref_object_copy_.8292
+ ___Block_byref_object_copy_.883
+ ___Block_byref_object_copy_.9696
+ ___Block_byref_object_copy_.9938
+ ___Block_byref_object_dispose_.1014
+ ___Block_byref_object_dispose_.11172
+ ___Block_byref_object_dispose_.11465
+ ___Block_byref_object_dispose_.1182
+ ___Block_byref_object_dispose_.12223
+ ___Block_byref_object_dispose_.13040
+ ___Block_byref_object_dispose_.1347
+ ___Block_byref_object_dispose_.13621
+ ___Block_byref_object_dispose_.13947
+ ___Block_byref_object_dispose_.14134
+ ___Block_byref_object_dispose_.14951
+ ___Block_byref_object_dispose_.15552
+ ___Block_byref_object_dispose_.16273
+ ___Block_byref_object_dispose_.16595
+ ___Block_byref_object_dispose_.17067
+ ___Block_byref_object_dispose_.1748
+ ___Block_byref_object_dispose_.17668
+ ___Block_byref_object_dispose_.18491
+ ___Block_byref_object_dispose_.19962
+ ___Block_byref_object_dispose_.20102
+ ___Block_byref_object_dispose_.2056
+ ___Block_byref_object_dispose_.20612
+ ___Block_byref_object_dispose_.21226
+ ___Block_byref_object_dispose_.21708
+ ___Block_byref_object_dispose_.22045
+ ___Block_byref_object_dispose_.23058
+ ___Block_byref_object_dispose_.23357
+ ___Block_byref_object_dispose_.24119
+ ___Block_byref_object_dispose_.2552
+ ___Block_byref_object_dispose_.2629
+ ___Block_byref_object_dispose_.2952
+ ___Block_byref_object_dispose_.3269
+ ___Block_byref_object_dispose_.5788
+ ___Block_byref_object_dispose_.6488
+ ___Block_byref_object_dispose_.6639
+ ___Block_byref_object_dispose_.678
+ ___Block_byref_object_dispose_.7201
+ ___Block_byref_object_dispose_.7581
+ ___Block_byref_object_dispose_.7860
+ ___Block_byref_object_dispose_.8293
+ ___Block_byref_object_dispose_.884
+ ___Block_byref_object_dispose_.9697
+ ___Block_byref_object_dispose_.9939
+ ___CPLBoundaryKeyOSLogDomain
+ ___CPLBoundaryKeyOSLogDomain.onceToken
+ ___CPLBoundaryKeyOSLogDomain.result
+ ___CPLConfigurationOSLogDomain.19321
+ ___CPLConfigurationOSLogDomain.onceToken.19327
+ ___CPLConfigurationOSLogDomain.result.19329
+ ___CPLForceSyncOSLogDomain.20754
+ ___CPLForceSyncOSLogDomain.onceToken.20763
+ ___CPLForceSyncOSLogDomain.result.20764
+ ___CPLGetAppBoundaryKey_block_invoke
+ ___CPLPredictorOSLogDomain
+ ___CPLSchedulerOSLogDomain.7528
+ ___CPLSchedulerOSLogDomain.onceToken.7529
+ ___CPLSchedulerOSLogDomain.result.7530
+ ___CPLSessionOSLogDomain.16143
+ ___CPLSessionOSLogDomain.18050
+ ___CPLSessionOSLogDomain.22647
+ ___CPLSessionOSLogDomain.onceToken.16145
+ ___CPLSessionOSLogDomain.onceToken.18055
+ ___CPLSessionOSLogDomain.onceToken.22649
+ ___CPLSessionOSLogDomain.result.16146
+ ___CPLSessionOSLogDomain.result.18056
+ ___CPLSessionOSLogDomain.result.22651
+ ___CPLStorageOSLogDomain.11139
+ ___CPLStorageOSLogDomain.11224
+ ___CPLStorageOSLogDomain.17635
+ ___CPLStorageOSLogDomain.20081
+ ___CPLStorageOSLogDomain.2037
+ ___CPLStorageOSLogDomain.21372
+ ___CPLStorageOSLogDomain.22031
+ ___CPLStorageOSLogDomain.22279
+ ___CPLStorageOSLogDomain.505
+ ___CPLStorageOSLogDomain.6239
+ ___CPLStorageOSLogDomain.7809
+ ___CPLStorageOSLogDomain.8543
+ ___CPLStorageOSLogDomain.8984
+ ___CPLStorageOSLogDomain.909
+ ___CPLStorageOSLogDomain.9150
+ ___CPLStorageOSLogDomain.9343
+ ___CPLStorageOSLogDomain.onceToken.11150
+ ___CPLStorageOSLogDomain.onceToken.11227
+ ___CPLStorageOSLogDomain.onceToken.14470
+ ___CPLStorageOSLogDomain.onceToken.17637
+ ___CPLStorageOSLogDomain.onceToken.20083
+ ___CPLStorageOSLogDomain.onceToken.20361
+ ___CPLStorageOSLogDomain.onceToken.2039
+ ___CPLStorageOSLogDomain.onceToken.21376
+ ___CPLStorageOSLogDomain.onceToken.22036
+ ___CPLStorageOSLogDomain.onceToken.22287
+ ___CPLStorageOSLogDomain.onceToken.507
+ ___CPLStorageOSLogDomain.onceToken.6241
+ ___CPLStorageOSLogDomain.onceToken.7811
+ ___CPLStorageOSLogDomain.onceToken.8551
+ ___CPLStorageOSLogDomain.onceToken.8990
+ ___CPLStorageOSLogDomain.onceToken.915
+ ___CPLStorageOSLogDomain.onceToken.9152
+ ___CPLStorageOSLogDomain.onceToken.9345
+ ___CPLStorageOSLogDomain.result.11152
+ ___CPLStorageOSLogDomain.result.11229
+ ___CPLStorageOSLogDomain.result.14472
+ ___CPLStorageOSLogDomain.result.17639
+ ___CPLStorageOSLogDomain.result.20085
+ ___CPLStorageOSLogDomain.result.20362
+ ___CPLStorageOSLogDomain.result.2041
+ ___CPLStorageOSLogDomain.result.21378
+ ___CPLStorageOSLogDomain.result.22038
+ ___CPLStorageOSLogDomain.result.22289
+ ___CPLStorageOSLogDomain.result.509
+ ___CPLStorageOSLogDomain.result.6243
+ ___CPLStorageOSLogDomain.result.7812
+ ___CPLStorageOSLogDomain.result.8552
+ ___CPLStorageOSLogDomain.result.8992
+ ___CPLStorageOSLogDomain.result.9153
+ ___CPLStorageOSLogDomain.result.917
+ ___CPLStorageOSLogDomain.result.9346
+ ___CPLStoreOSLogDomain.3056
+ ___CPLStoreOSLogDomain.onceToken.3057
+ ___CPLStoreOSLogDomain.result.3058
+ ___CPLTaskOSLogDomain.11412
+ ___CPLTaskOSLogDomain.1344
+ ___CPLTaskOSLogDomain.13920
+ ___CPLTaskOSLogDomain.14382
+ ___CPLTaskOSLogDomain.15448
+ ___CPLTaskOSLogDomain.16977
+ ___CPLTaskOSLogDomain.21172
+ ___CPLTaskOSLogDomain.22983
+ ___CPLTaskOSLogDomain.24075
+ ___CPLTaskOSLogDomain.2614
+ ___CPLTaskOSLogDomain.5473
+ ___CPLTaskOSLogDomain.619
+ ___CPLTaskOSLogDomain.7123
+ ___CPLTaskOSLogDomain.onceToken.11448
+ ___CPLTaskOSLogDomain.onceToken.1372
+ ___CPLTaskOSLogDomain.onceToken.13922
+ ___CPLTaskOSLogDomain.onceToken.14384
+ ___CPLTaskOSLogDomain.onceToken.15457
+ ___CPLTaskOSLogDomain.onceToken.16984
+ ___CPLTaskOSLogDomain.onceToken.21214
+ ___CPLTaskOSLogDomain.onceToken.22994
+ ___CPLTaskOSLogDomain.onceToken.24083
+ ___CPLTaskOSLogDomain.onceToken.2616
+ ___CPLTaskOSLogDomain.onceToken.5476
+ ___CPLTaskOSLogDomain.onceToken.622
+ ___CPLTaskOSLogDomain.onceToken.7135
+ ___CPLTaskOSLogDomain.result.11450
+ ___CPLTaskOSLogDomain.result.1373
+ ___CPLTaskOSLogDomain.result.13924
+ ___CPLTaskOSLogDomain.result.14385
+ ___CPLTaskOSLogDomain.result.15459
+ ___CPLTaskOSLogDomain.result.16985
+ ___CPLTaskOSLogDomain.result.21215
+ ___CPLTaskOSLogDomain.result.22996
+ ___CPLTaskOSLogDomain.result.24084
+ ___CPLTaskOSLogDomain.result.2618
+ ___CPLTaskOSLogDomain.result.5478
+ ___CPLTaskOSLogDomain.result.624
+ ___CPLTaskOSLogDomain.result.7137
+ ____CPLGetAccountDSID_block_invoke
+ ____CPLGetAccountDSID_block_invoke.122
+ ____CPLGetAccountDSID_block_invoke_2
+ ____CPLGetAccountDSID_block_invoke_2.128
+ ____CPLGetAppBoundaryKey_block_invoke
+ ____CPLGetAppBoundaryKey_block_invoke_2
+ _____CPLBoundaryKeyOSLogDomain_block_invoke
+ _____CPLConfigurationOSLogDomain_block_invoke.19332
+ _____CPLForceSyncOSLogDomain_block_invoke.20766
+ _____CPLSchedulerOSLogDomain_block_invoke.7532
+ _____CPLSessionOSLogDomain_block_invoke.16148
+ _____CPLSessionOSLogDomain_block_invoke.18058
+ _____CPLSessionOSLogDomain_block_invoke.22654
+ _____CPLStorageOSLogDomain_block_invoke.11155
+ _____CPLStorageOSLogDomain_block_invoke.11232
+ _____CPLStorageOSLogDomain_block_invoke.14477
+ _____CPLStorageOSLogDomain_block_invoke.17642
+ _____CPLStorageOSLogDomain_block_invoke.20088
+ _____CPLStorageOSLogDomain_block_invoke.20368
+ _____CPLStorageOSLogDomain_block_invoke.2044
+ _____CPLStorageOSLogDomain_block_invoke.21381
+ _____CPLStorageOSLogDomain_block_invoke.22041
+ _____CPLStorageOSLogDomain_block_invoke.22292
+ _____CPLStorageOSLogDomain_block_invoke.512
+ _____CPLStorageOSLogDomain_block_invoke.6246
+ _____CPLStorageOSLogDomain_block_invoke.7814
+ _____CPLStorageOSLogDomain_block_invoke.8554
+ _____CPLStorageOSLogDomain_block_invoke.8995
+ _____CPLStorageOSLogDomain_block_invoke.9155
+ _____CPLStorageOSLogDomain_block_invoke.920
+ _____CPLStorageOSLogDomain_block_invoke.9348
+ _____CPLStoreOSLogDomain_block_invoke.3060
+ _____CPLTaskOSLogDomain_block_invoke.11453
+ _____CPLTaskOSLogDomain_block_invoke.1375
+ _____CPLTaskOSLogDomain_block_invoke.13927
+ _____CPLTaskOSLogDomain_block_invoke.14387
+ _____CPLTaskOSLogDomain_block_invoke.15462
+ _____CPLTaskOSLogDomain_block_invoke.16987
+ _____CPLTaskOSLogDomain_block_invoke.21217
+ _____CPLTaskOSLogDomain_block_invoke.22999
+ _____CPLTaskOSLogDomain_block_invoke.24086
+ _____CPLTaskOSLogDomain_block_invoke.2621
+ _____CPLTaskOSLogDomain_block_invoke.5481
+ _____CPLTaskOSLogDomain_block_invoke.627
+ _____CPLTaskOSLogDomain_block_invoke.7140
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96r104r_e49_v32?0"CPLRecordChange"8"NSArray"16"NSError"24ls32l8r96l8r104l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96r104r_e5_v8?0ls32l8s40l8s48l8s56l8r96l8r104l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96bs104r112r_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s96l8s56l8s64l8s72l8r104l8s80l8r112l8s88l8
+ ___block_descriptor_121_e8_32s40s48s56s64s72s80s88bs96bs104r112r_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s88l8s56l8s64l8r104l8s72l8r112l8s80l8s96l8
+ ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96s104s112bs120r128r_e5_v8?0ls32l8s40l8s112l8s48l8s56l8s64l8s72l8s80l8s88l8r120l8s96l8r128l8s104l8
+ ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96s104s112s120r128r_e5_v8?0lr120l8s32l8s40l8r128l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8
+ ___block_descriptor_137_e8_32s40s48s56s64s72s80s88s96s104bs112bs120r128r_e5_v8?0ls32l8s40l8s104l8s48l8s56l8s64l8s72l8s80l8r120l8s88l8r128l8s96l8s112l8
+ ___block_descriptor_145_e8_32s40s48s56s64s72s80s88s96s104bs112bs120r128r_e5_v8?0ls32l8s40l8r120l8s104l8s48l8s56l8s64l8s72l8s112l8s80l8s88l8r128l8s96l8
+ ___block_descriptor_152_e8_32s40s48s56s64s72s80s88s96s104s112s120bs128r136r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s120l8s88l8s96l8s104l8r128l8r136l8s112l8
+ ___block_descriptor_153_e8_32s40s48s56s64s72s80s88s96s104s112bs120bs128r136r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s112l8s88l8s96l8r128l8r136l8s104l8s120l8
+ ___block_descriptor_40_e8_32bs_e30_v24?0"NSString"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e31_v16?0"CPLBackgroundActivity"8ls32l8
+ ___block_descriptor_40_e8_32r_e25_v16?0"CPLCallObserver"8lr32l8
+ ___block_descriptor_40_e8_32s_e45_v24?0"CPLRecordChange"8"CPLRecordChange"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e25_v16?0"CPLCallObserver"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSData"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e49_v32?0"CPLRecordChange"8"NSArray"16"NSError"24ls32l8s40l8
+ ___block_descriptor_50_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48bs_e45_v24?0"CPLRecordChange"8"CPLRecordChange"16ls40l8s32l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e49_v32?0"CPLRecordChange"8"NSArray"16"NSError"24ls32l8s48l8s40l8
+ ___block_descriptor_57_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_57_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8r56l8s48l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e47_v24?0"_CPLResourcesMutableArray"8"NSError"16ls32l8s40l8s64l8s48l8s56l8
+ ___block_literal_global.10042
+ ___block_literal_global.10361
+ ___block_literal_global.1042
+ ___block_literal_global.105.18845
+ ___block_literal_global.1053
+ ___block_literal_global.10758
+ ___block_literal_global.10997
+ ___block_literal_global.110.20911
+ ___block_literal_global.11151
+ ___block_literal_global.11228
+ ___block_literal_global.11449
+ ___block_literal_global.1185
+ ___block_literal_global.12.7933
+ ___block_literal_global.12342
+ ___block_literal_global.12564
+ ___block_literal_global.13
+ ___block_literal_global.13060
+ ___block_literal_global.137
+ ___block_literal_global.13923
+ ___block_literal_global.14.14418
+ ___block_literal_global.140
+ ___block_literal_global.1413
+ ___block_literal_global.14181
+ ___block_literal_global.142.20915
+ ___block_literal_global.14417
+ ___block_literal_global.14471
+ ___block_literal_global.14634
+ ___block_literal_global.1493
+ ___block_literal_global.15167
+ ___block_literal_global.15187
+ ___block_literal_global.15252
+ ___block_literal_global.15458
+ ___block_literal_global.1574
+ ___block_literal_global.159.20916
+ ___block_literal_global.15998
+ ___block_literal_global.160
+ ___block_literal_global.16213
+ ___block_literal_global.16773
+ ___block_literal_global.1702
+ ___block_literal_global.17089
+ ___block_literal_global.171.20917
+ ___block_literal_global.172
+ ___block_literal_global.1722
+ ___block_literal_global.1724
+ ___block_literal_global.1732
+ ___block_literal_global.1734
+ ___block_literal_global.1736
+ ___block_literal_global.1738
+ ___block_literal_global.1740
+ ___block_literal_global.1742
+ ___block_literal_global.17432
+ ___block_literal_global.1744
+ ___block_literal_global.1744.5763
+ ___block_literal_global.1746
+ ___block_literal_global.1748
+ ___block_literal_global.1750
+ ___block_literal_global.1756
+ ___block_literal_global.1758
+ ___block_literal_global.1760
+ ___block_literal_global.1762
+ ___block_literal_global.17638
+ ___block_literal_global.1764
+ ___block_literal_global.1766
+ ___block_literal_global.1774
+ ___block_literal_global.1776
+ ___block_literal_global.1784
+ ___block_literal_global.1792
+ ___block_literal_global.1794
+ ___block_literal_global.1799
+ ___block_literal_global.18
+ ___block_literal_global.1801
+ ___block_literal_global.18068
+ ___block_literal_global.18240
+ ___block_literal_global.18378
+ ___block_literal_global.185
+ ___block_literal_global.1876
+ ___block_literal_global.18958
+ ___block_literal_global.1911
+ ___block_literal_global.19328
+ ___block_literal_global.194
+ ___block_literal_global.1955
+ ___block_literal_global.1961
+ ___block_literal_global.19713
+ ___block_literal_global.20084
+ ___block_literal_global.20248
+ ___block_literal_global.20364
+ ___block_literal_global.2040
+ ___block_literal_global.20907
+ ___block_literal_global.21232
+ ___block_literal_global.21377
+ ___block_literal_global.21551
+ ___block_literal_global.219
+ ___block_literal_global.220
+ ___block_literal_global.22037
+ ___block_literal_global.222
+ ___block_literal_global.22288
+ ___block_literal_global.22448
+ ___block_literal_global.22650
+ ___block_literal_global.22800
+ ___block_literal_global.23053
+ ___block_literal_global.2317
+ ___block_literal_global.23609
+ ___block_literal_global.23745
+ ___block_literal_global.23817
+ ___block_literal_global.24.14135
+ ___block_literal_global.24249
+ ___block_literal_global.24363
+ ___block_literal_global.244
+ ___block_literal_global.24482
+ ___block_literal_global.24667
+ ___block_literal_global.2492
+ ___block_literal_global.2550
+ ___block_literal_global.2617
+ ___block_literal_global.264.22995
+ ___block_literal_global.27.16232
+ ___block_literal_global.292
+ ___block_literal_global.2968
+ ___block_literal_global.3035
+ ___block_literal_global.305
+ ___block_literal_global.307
+ ___block_literal_global.309
+ ___block_literal_global.310
+ ___block_literal_global.311
+ ___block_literal_global.312
+ ___block_literal_global.32.22416
+ ___block_literal_global.3285
+ ___block_literal_global.33.7251
+ ___block_literal_global.34.2489
+ ___block_literal_global.34.9935
+ ___block_literal_global.341
+ ___block_literal_global.343
+ ___block_literal_global.344
+ ___block_literal_global.3557
+ ___block_literal_global.356
+ ___block_literal_global.37.10678
+ ___block_literal_global.374
+ ___block_literal_global.3795
+ ___block_literal_global.4033
+ ___block_literal_global.42.7940
+ ___block_literal_global.430
+ ___block_literal_global.4465
+ ___block_literal_global.451
+ ___block_literal_global.4600
+ ___block_literal_global.4814
+ ___block_literal_global.5.24376
+ ___block_literal_global.50.7242
+ ___block_literal_global.508
+ ___block_literal_global.5262
+ ___block_literal_global.532
+ ___block_literal_global.5339
+ ___block_literal_global.535
+ ___block_literal_global.54.5235
+ ___block_literal_global.5477
+ ___block_literal_global.549
+ ___block_literal_global.5617
+ ___block_literal_global.57.7944
+ ___block_literal_global.587
+ ___block_literal_global.59
+ ___block_literal_global.590
+ ___block_literal_global.61
+ ___block_literal_global.6154
+ ___block_literal_global.623
+ ___block_literal_global.6242
+ ___block_literal_global.6463
+ ___block_literal_global.660
+ ___block_literal_global.663
+ ___block_literal_global.666
+ ___block_literal_global.6743
+ ___block_literal_global.7136
+ ___block_literal_global.72.16731
+ ___block_literal_global.7250
+ ___block_literal_global.744
+ ___block_literal_global.747
+ ___block_literal_global.749
+ ___block_literal_global.750
+ ___block_literal_global.753
+ ___block_literal_global.7650
+ ___block_literal_global.77.15993
+ ___block_literal_global.7930
+ ___block_literal_global.8674
+ ___block_literal_global.869
+ ___block_literal_global.8885
+ ___block_literal_global.8991
+ ___block_literal_global.9089
+ ___block_literal_global.916
+ ___block_literal_global.93.18849
+ ___block_literal_global.93.7713
+ ___block_literal_global.9394
+ ___block_literal_global.9567
+ ___block_literal_global.9834
+ ___cpl_dispatch_async_block_invoke.10019
+ ___cpl_dispatch_async_block_invoke.11408
+ ___cpl_dispatch_async_block_invoke.12042
+ ___cpl_dispatch_async_block_invoke.1378
+ ___cpl_dispatch_async_block_invoke.13932
+ ___cpl_dispatch_async_block_invoke.14306
+ ___cpl_dispatch_async_block_invoke.14379
+ ___cpl_dispatch_async_block_invoke.15541
+ ___cpl_dispatch_async_block_invoke.16551
+ ___cpl_dispatch_async_block_invoke.17043
+ ___cpl_dispatch_async_block_invoke.17388
+ ___cpl_dispatch_async_block_invoke.17875
+ ___cpl_dispatch_async_block_invoke.1825
+ ___cpl_dispatch_async_block_invoke.18374
+ ___cpl_dispatch_async_block_invoke.19307
+ ___cpl_dispatch_async_block_invoke.20594
+ ___cpl_dispatch_async_block_invoke.21170
+ ___cpl_dispatch_async_block_invoke.21559
+ ___cpl_dispatch_async_block_invoke.22802
+ ___cpl_dispatch_async_block_invoke.23002
+ ___cpl_dispatch_async_block_invoke.24127
+ ___cpl_dispatch_async_block_invoke.2955
+ ___cpl_dispatch_async_block_invoke.6686
+ ___cpl_dispatch_async_block_invoke.682
+ ___cpl_dispatch_async_block_invoke.7121
+ ___cpl_dispatch_async_block_invoke.7391
+ ___cpl_dispatch_async_block_invoke.7820
+ ___cpl_dispatch_async_block_invoke.9680
+ __doProtected:.onceToken.15186
+ __doProtected:.onceToken.22799
+ __doProtected:.queue.22801
+ __statusDidChange.12239
+ _copyDerivativesFromRecordIfPossible:.originalDerivativesImageAndVideo.18868
+ _initWithCPLArchiver:.onceToken.1958
+ _initWithCPLArchiver:.stringClass.1959
+ _initWithCoder:.deletedScopeIdentifiersClasses
+ _initWithCoder:.logOnceToken.20250
+ _initWithCoder:.onceToken.10702
+ _initWithCoder:.onceToken.14180
+ _initWithCoder:.onceToken.18067
+ _initWithCoder:.onceToken.20247
+ _initWithCoder:.onceToken.22447
+ _initWithCoder:.onceToken.24666
+ _initWithCoder:.onceToken.5234
+ _initWithCoder:.onceToken.5338
+ _initWithCoder:.onceToken.6458
+ _initWithCoder:.pushContextsClasses.22449
+ _initWithCoder:.stringClass.10703
+ _isCollectionShareFeatureEnabled
+ _isSharedLibraryFeatureEnabled
+ _objc_msgSend$_allowsJustInCaseSessions
+ _objc_msgSend$_cachedResourcesForReferenceResource:adjustment:includePosterFrame:
+ _objc_msgSend$_cleanTempFolderURLForGeneratedResourcesWithReferenceResource:adjustment:includePosterFrame:
+ _objc_msgSend$_discardGenerateDerivativesProgress
+ _objc_msgSend$_forceCloseWithCompletionHandler:
+ _objc_msgSend$_generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:
+ _objc_msgSend$_generatingDerivativesForChange:fractionCompleted:chunkLength:
+ _objc_msgSend$_installGenerateDerivativesCancellationHandler:
+ _objc_msgSend$_justInCaseSessionIsPossible
+ _objc_msgSend$_noteGeneratedResources:haveBeenGeneratedForReferenceResource:adjustment:includePosterFrame:
+ _objc_msgSend$_noteSignificantEvent
+ _objc_msgSend$_setError
+ _objc_msgSend$_shouldStashMasterRecords
+ _objc_msgSend$aa_personID
+ _objc_msgSend$aa_primaryAppleAccount
+ _objc_msgSend$addObserver:forKeyPath:options:context:
+ _objc_msgSend$allowsUnsafeClientCache
+ _objc_msgSend$archiverContext
+ _objc_msgSend$assetScopedIdentifier
+ _objc_msgSend$clientAppBundleIdentifier
+ _objc_msgSend$clientCanPushScopeChange:
+ _objc_msgSend$copyWithScopeType:
+ _objc_msgSend$deletedScopeIdentifiers
+ _objc_msgSend$fractionCompleted
+ _objc_msgSend$getBackgroundSchedulingStatusDictionaryWithCompletionHandler:
+ _objc_msgSend$getBackgroundSchedulingStatusWithCompletionHandler:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$initWithIntent:priority:bypassCaches:timeRange:
+ _objc_msgSend$isBlocked
+ _objc_msgSend$isJustInCaseSession
+ _objc_msgSend$observeSyncCallOn:selector:block:
+ _objc_msgSend$predictedDateForType:
+ _objc_msgSend$proposedCloudScopedIdentifier
+ _objc_msgSend$removeObserver:forKeyPath:
+ _objc_msgSend$removePredictedValueForType:
+ _objc_msgSend$runtimeCharacteristics
+ _objc_msgSend$scopeIndexes
+ _objc_msgSend$setAssetScopedIdentifier:
+ _objc_msgSend$setCloudIndex:
+ _objc_msgSend$setIsJustInCaseSession:
+ _objc_msgSend$setLocalIndex:
+ _objc_msgSend$setStableIndex:
+ _objc_msgSend$setTransportShare:
+ _objc_msgSend$shouldBeDiscretionary
+ _objc_msgSend$shouldBeTemporarilyNonDiscretionary
+ _objc_msgSend$shouldBypassCaches
+ _objc_msgSend$shouldShowBackgroundSchedulingStatusInTransport
+ _objc_msgSend$stringForTimeIntervalNumber:now:
+ _objc_msgSend$supportsActivationOfScopeWithType:
+ _objc_msgSend$supportsCollectionShare
+ _objc_msgSend$supportsRecordModificationDate
+ _objc_msgSend$syncHasBeenRequested
+ _objc_msgSend$syncSessionRequestedImmediateRuntime
+ _objc_msgSend$updateBlockedMetrics:syncRequested:runtimeCharacteristics:
+ _objc_msgSend$updatePredictedDate:forType:
+ _objc_msgSend$updatedPredictionRemovingValueForType:
+ _objc_opt_new
+ _overridesCollectionShareFeatureFlag
+ _overridesSharedLibraryFeatureFlag
+ _propertiesForChangeType:.onceToken.15022
+ _propertiesForChangeType:.onceToken.18882
+ _propertiesForChangeType:.onceToken.23744
+ _propertiesForChangeType:.properties.23746
- -[CPLEngineDerivativesCache cachedResourcesForReferenceResource:adjustment:includePosterFrame:]
- -[CPLEngineDerivativesCache noteGeneratedResouces:haveBeenGeneratedForReferenceResource:adjustment:includePosterFrame:]
- -[CPLEngineDerivativesCache tempFolderURLForGeneratedResourcesWithReferenceResource:adjustment:includePosterFrame:]
- -[CPLEngineLibrary updateBlockedMetrics:syncRequested:]
- -[CPLEngineResourceDownloadQueue _bestQueueWithCancellableTransportTasks]
- -[CPLEngineResourceDownloadQueue _dispatchTransportTasksIfNecessary]
- -[CPLEngineResourceDownloadQueue _downloadTaskForLocalResource:clientBundleID:options:proposedTaskIdentifier:didStartHandler:progressHandler:completionHandler:]
- -[CPLEngineResourceDownloadQueue _realDownloadTaskForLocalResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]
- -[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]
- -[CPLEngineResourceDownloadQueue _shouldTryLowPriorityDownloadWithError:]
- -[CPLEngineResourceDownloadQueue _unscheduleBackgroundDownloads]
- -[CPLRecordChange(CPLIDMapping) proposedCloudScopedIdentifierWithError:]
- -[CPLScopedIdentifier isInAMomentShare]
- GCC_except_table1141
- GCC_except_table1187
- GCC_except_table1192
- GCC_except_table1196
- GCC_except_table1203
- GCC_except_table1206
- GCC_except_table1209
- GCC_except_table1215
- GCC_except_table1217
- GCC_except_table1297
- GCC_except_table1383
- GCC_except_table1913
- GCC_except_table2020
- GCC_except_table2026
- GCC_except_table203
- GCC_except_table2066
- GCC_except_table215
- GCC_except_table2152
- GCC_except_table2162
- GCC_except_table219
- GCC_except_table221
- GCC_except_table223
- GCC_except_table2296
- GCC_except_table2383
- GCC_except_table2604
- GCC_except_table2606
- GCC_except_table2692
- GCC_except_table2755
- GCC_except_table2757
- GCC_except_table2894
- GCC_except_table2897
- GCC_except_table2911
- GCC_except_table2980
- GCC_except_table2984
- GCC_except_table2986
- GCC_except_table2988
- GCC_except_table2992
- GCC_except_table3112
- GCC_except_table312
- GCC_except_table3159
- GCC_except_table3391
- GCC_except_table3458
- GCC_except_table3462
- GCC_except_table3464
- GCC_except_table3473
- GCC_except_table362
- GCC_except_table371
- GCC_except_table3746
- GCC_except_table3776
- GCC_except_table3803
- GCC_except_table3820
- GCC_except_table3827
- GCC_except_table3835
- GCC_except_table3837
- GCC_except_table3851
- GCC_except_table3853
- GCC_except_table3855
- GCC_except_table4192
- GCC_except_table4235
- GCC_except_table432
- GCC_except_table4323
- GCC_except_table436
- GCC_except_table4390
- GCC_except_table4393
- GCC_except_table4564
- GCC_except_table4572
- GCC_except_table4652
- GCC_except_table4656
- GCC_except_table4660
- GCC_except_table4665
- GCC_except_table467
- GCC_except_table4680
- GCC_except_table4681
- GCC_except_table4685
- GCC_except_table4728
- GCC_except_table4736
- GCC_except_table4791
- GCC_except_table4793
- GCC_except_table4795
- GCC_except_table4807
- GCC_except_table484
- GCC_except_table485
- GCC_except_table494
- GCC_except_table4942
- GCC_except_table4983
- GCC_except_table4992
- GCC_except_table4993
- GCC_except_table5050
- GCC_except_table5053
- GCC_except_table511
- GCC_except_table518
- GCC_except_table5323
- GCC_except_table5352
- GCC_except_table5394
- GCC_except_table5414
- GCC_except_table5440
- GCC_except_table5451
- GCC_except_table5472
- GCC_except_table5492
- GCC_except_table5496
- GCC_except_table5522
- GCC_except_table5554
- GCC_except_table5594
- GCC_except_table5653
- GCC_except_table5694
- GCC_except_table5718
- GCC_except_table5725
- GCC_except_table5778
- GCC_except_table5903
- GCC_except_table5916
- GCC_except_table5919
- GCC_except_table619
- GCC_except_table625
- GCC_except_table6398
- GCC_except_table6437
- GCC_except_table6441
- GCC_except_table6443
- GCC_except_table6458
- GCC_except_table6464
- GCC_except_table6472
- GCC_except_table6478
- GCC_except_table6482
- GCC_except_table6490
- GCC_except_table6493
- GCC_except_table6513
- GCC_except_table6520
- GCC_except_table6543
- GCC_except_table656
- GCC_except_table6577
- GCC_except_table660
- GCC_except_table6601
- GCC_except_table6610
- GCC_except_table6628
- GCC_except_table663
- GCC_except_table6631
- GCC_except_table6633
- GCC_except_table6635
- GCC_except_table665
- GCC_except_table6667
- GCC_except_table667
- GCC_except_table669
- GCC_except_table6737
- GCC_except_table680
- GCC_except_table686
- GCC_except_table6881
- GCC_except_table6903
- GCC_except_table692
- GCC_except_table6933
- GCC_except_table694
- GCC_except_table696
- GCC_except_table698
- GCC_except_table700
- GCC_except_table7116
- GCC_except_table7125
- GCC_except_table7130
- GCC_except_table7144
- GCC_except_table7158
- GCC_except_table7168
- GCC_except_table7173
- GCC_except_table724
- GCC_except_table7252
- GCC_except_table726
- GCC_except_table7331
- GCC_except_table7340
- GCC_except_table7396
- GCC_except_table740
- GCC_except_table7438
- GCC_except_table7446
- GCC_except_table7447
- GCC_except_table746
- GCC_except_table7460
- GCC_except_table755
- GCC_except_table762
- GCC_except_table864
- GCC_except_table950
- GCC_except_table968
- GCC_except_table970
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _CPLSyncSessionBlockedStateDidChangeNotification
- _CPLSyncSessionBlockedStateIsBlockedKey
- _CPLSyncSessionBlockedStateSyncRequestedKey
- _OBJC_IVAR_$_CPLEngineScheduler._syncObserver
- _OBJC_IVAR_$_CPLPushSessionTracker._checkScopeIdentifier
- _OBJC_IVAR_$_CPLPushSessionTracker._idMapping
- ___105-[CPLLibraryManager startExitFromSharedScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:]_block_invoke.398
- ___110-[CPLLibraryManager beginDownloadForResource:clientBundleID:options:proposedTaskIdentifier:completionHandler:]_block_invoke.312
- ___112-[CPLEngineDerivativesCache generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.43
- ___112-[CPLEngineDerivativesCache generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.45
- ___112-[CPLEngineDerivativesCache generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.48
- ___112-[CPLEngineDerivativesCache generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.59
- ___112-[CPLEngineDerivativesCache generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke_2.53
- ___115-[CPLLibraryManager removeParticipants:fromSharedScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:]_block_invoke.403
- ___120-[CPLLibraryManager getStreamingURLOrMediaMakerDataForResource:intent:hints:timeRange:clientBundleID:completionHandler:]_block_invoke.318
- ___122-[CPLLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke.488
- ___160-[CPLEngineResourceDownloadQueue _downloadTaskForLocalResource:clientBundleID:options:proposedTaskIdentifier:didStartHandler:progressHandler:completionHandler:]_block_invoke.166
- ___160-[CPLEngineResourceDownloadQueue _downloadTaskForLocalResource:clientBundleID:options:proposedTaskIdentifier:didStartHandler:progressHandler:completionHandler:]_block_invoke.173
- ___160-[CPLEngineResourceDownloadQueue _downloadTaskForLocalResource:clientBundleID:options:proposedTaskIdentifier:didStartHandler:progressHandler:completionHandler:]_block_invoke.176
- ___163-[CPLEngineResourceDownloadQueue _realDownloadTaskForLocalResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.197
- ___163-[CPLEngineResourceDownloadQueue _realDownloadTaskForLocalResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.199
- ___163-[CPLEngineResourceDownloadQueue _realDownloadTaskForLocalResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke_2.198
- ___163-[CPLEngineResourceDownloadQueue _realDownloadTaskForLocalResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke_2.200
- ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.187
- ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.189
- ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.192
- ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.195
- ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke_2.194
- ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke_2.196
- ___36-[CPLPushSessionTracker computeDiff]_block_invoke.48
- ___36-[CPLPushSessionTracker computeDiff]_block_invoke.54
- ___36-[CPLPushSessionTracker computeDiff]_block_invoke.67
- ___36-[CPLPushSessionTracker computeDiff]_block_invoke_2.49
- ___36-[CPLPushSessionTracker computeDiff]_block_invoke_2.57
- ___37-[CPLUploadPushedChangesTask cancel:]_block_invoke.142
- ___41-[CPLEngineScheduler noteQuotaHasChanged]_block_invoke.147
- ___42-[CPLEngineScheduler _prepareFirstSession]_block_invoke.151
- ___42-[CPLEngineScheduler _prepareFirstSession]_block_invoke_2.153
- ___42-[CPLLibraryManager discardCurrentSession]_block_invoke.277
- ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.242
- ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.269
- ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.272
- ___47-[CPLLibraryManager openWithCompletionHandler:]_block_invoke.184
- ___47-[CPLLibraryManager openWithCompletionHandler:]_block_invoke.188
- ___47-[CPLLibraryManager openWithCompletionHandler:]_block_invoke.191
- ___48-[CPLEngineScheduler openWithCompletionHandler:]_block_invoke_3
- ___48-[CPLEngineScheduler openWithCompletionHandler:]_block_invoke_4
- ___48-[CPLMingleChangesScopeTask _mingleOtherChanges]_block_invoke.68
- ___50+[CPLArchiver displayableDictionaryForDictionary:]_block_invoke.1667
- ___51-[CPLEngineStore _reallySchedulePendingUpdateApply]_block_invoke.328
- ___51-[CPLLibraryManager createScope:completionHandler:]_block_invoke.328
- ___54-[CPLLibraryManager forceBackupWithCompletionHandler:]_block_invoke.473
- ___55-[CPLEngineLibrary updateBlockedMetrics:syncRequested:]_block_invoke
- ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.128
- ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.130
- ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.131
- ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.132
- ___56-[CPLEngineStore _closeAndDeactivate:completionHandler:]_block_invoke.315
- ___57-[CPLLibraryManager acceptSharedScope:completionHandler:]_block_invoke.416
- ___58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke.196
- ___58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke.197
- ___58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke.198
- ___58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke_2.199
- ___59-[CPLLibraryManager updateShareForScope:completionHandler:]_block_invoke.330
- ___60-[CPLUploadPushedChangesTask _uploadTaskDidFinishWithError:]_block_invoke.149
- ___62-[CPLSyncSessionPredictor updatePredictionWithValuesAndTypes:]_block_invoke.46
- ___64-[CPLEngineResourceDownloadQueue _unscheduleBackgroundDownloads]_block_invoke
- ___65-[CPLLibraryManager sharedLibraryRampCheckWithCompletionHandler:]_block_invoke.407
- ___66-[CPLLibraryManager refreshScopeWithIdentifier:completionHandler:]_block_invoke.345
- ___67-[CPLEngineScheduler _noteSyncSession:failedDuringPhase:withError:]_block_invoke.130
- ___67-[CPLEngineScheduler _noteSyncSession:failedDuringPhase:withError:]_block_invoke.131
- ___67-[CPLEngineScheduler _noteSyncSession:failedDuringPhase:withError:]_block_invoke.132
- ___68-[CPLEngineScheduler _handleResetAnchorWithError:completionHandler:]_block_invoke.116
- ___68-[CPLLibraryManager fetchSharedScopeFromShareURL:completionHandler:]_block_invoke.412
- ___72-[CPLFingerprintContext refreshBoundaryKeyWithSource:completionHandler:]_block_invoke.38
- ___72-[CPLLibraryManager deleteScopeWithIdentifier:forced:completionHandler:]_block_invoke.341
- ___72-[CPLLibraryManager requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.477
- ___74-[CPLEngineScheduler _handleResetGlobalAnchorWithError:completionHandler:]_block_invoke.120
- ___74-[CPLLibraryManager fetchExistingSharedLibraryScopeWithCompletionHandler:]_block_invoke.420
- ___76-[CPLLibraryManager queryUserDetailsForShareParticipants:completionHandler:]_block_invoke.425
- ___78-[CPLLibraryManager forceSynchronizingScopeWithIdentifiers:completionHandler:]_block_invoke.428
- ___78-[CPLMingleChangesScopeTask _filteredBatchByStashingRecordsIfNecessary:error:]_block_invoke.54
- ___79-[CPLLibraryManager checkHasBackgroundDownloadOperationsWithCompletionHandler:]_block_invoke.450
- ___80-[CPLEngineCloudCache cloudChangeBatchFromBatch:usingMapping:isFinal:withError:]_block_invoke.28
- ___82-[CPLLibraryManager rampingRequestForResourceType:numRequested:completionHandler:]_block_invoke.322
- ___84-[CPLEngineStore _performWriteTransactionByPassBlocker:WithBlock:completionHandler:]_block_invoke.288
- ___86-[CPLLibraryManager beginInMemoryDownloadOfResource:clientBundleID:completionHandler:]_block_invoke.324
- ___87-[CPLLibraryManager requestClientToPullAllChangesInScopeIdentifiers:completionHandler:]_block_invoke.481
- ___94-[CPLPullScopesTask _handleChangedOrNewScopes:deletedScopeIdentifiers:newScopeListSyncAnchor:]_block_invoke.1
- ___94-[CPLPullScopesTask _handleChangedOrNewScopes:deletedScopeIdentifiers:newScopeListSyncAnchor:]_block_invoke.5
- ___Block_byref_object_copy_.10836
- ___Block_byref_object_copy_.11129
- ___Block_byref_object_copy_.1175
- ___Block_byref_object_copy_.11887
- ___Block_byref_object_copy_.12781
- ___Block_byref_object_copy_.1317
- ___Block_byref_object_copy_.13337
- ___Block_byref_object_copy_.13656
- ___Block_byref_object_copy_.13838
- ___Block_byref_object_copy_.14649
- ___Block_byref_object_copy_.15257
- ___Block_byref_object_copy_.15969
- ___Block_byref_object_copy_.16284
- ___Block_byref_object_copy_.16737
- ___Block_byref_object_copy_.1715
- ___Block_byref_object_copy_.17340
- ___Block_byref_object_copy_.18161
- ___Block_byref_object_copy_.19610
- ___Block_byref_object_copy_.19751
- ___Block_byref_object_copy_.2019
- ___Block_byref_object_copy_.20265
- ___Block_byref_object_copy_.20876
- ___Block_byref_object_copy_.21340
- ___Block_byref_object_copy_.21677
- ___Block_byref_object_copy_.22693
- ___Block_byref_object_copy_.22992
- ___Block_byref_object_copy_.23742
- ___Block_byref_object_copy_.2508
- ___Block_byref_object_copy_.2582
- ___Block_byref_object_copy_.2899
- ___Block_byref_object_copy_.3205
- ___Block_byref_object_copy_.5547
- ___Block_byref_object_copy_.6232
- ___Block_byref_object_copy_.6379
- ___Block_byref_object_copy_.668
- ___Block_byref_object_copy_.6923
- ___Block_byref_object_copy_.7290
- ___Block_byref_object_copy_.7568
- ___Block_byref_object_copy_.7985
- ___Block_byref_object_copy_.871
- ___Block_byref_object_copy_.9364
- ___Block_byref_object_copy_.9623
- ___Block_byref_object_copy_.999
- ___Block_byref_object_dispose_.1000
- ___Block_byref_object_dispose_.10837
- ___Block_byref_object_dispose_.11130
- ___Block_byref_object_dispose_.1176
- ___Block_byref_object_dispose_.11888
- ___Block_byref_object_dispose_.12782
- ___Block_byref_object_dispose_.1318
- ___Block_byref_object_dispose_.13338
- ___Block_byref_object_dispose_.13657
- ___Block_byref_object_dispose_.13839
- ___Block_byref_object_dispose_.14650
- ___Block_byref_object_dispose_.15258
- ___Block_byref_object_dispose_.15970
- ___Block_byref_object_dispose_.16285
- ___Block_byref_object_dispose_.16738
- ___Block_byref_object_dispose_.1716
- ___Block_byref_object_dispose_.17341
- ___Block_byref_object_dispose_.18162
- ___Block_byref_object_dispose_.19611
- ___Block_byref_object_dispose_.19752
- ___Block_byref_object_dispose_.2020
- ___Block_byref_object_dispose_.20266
- ___Block_byref_object_dispose_.20877
- ___Block_byref_object_dispose_.21341
- ___Block_byref_object_dispose_.21678
- ___Block_byref_object_dispose_.22694
- ___Block_byref_object_dispose_.22993
- ___Block_byref_object_dispose_.23743
- ___Block_byref_object_dispose_.2509
- ___Block_byref_object_dispose_.2583
- ___Block_byref_object_dispose_.2900
- ___Block_byref_object_dispose_.3206
- ___Block_byref_object_dispose_.5548
- ___Block_byref_object_dispose_.6233
- ___Block_byref_object_dispose_.6380
- ___Block_byref_object_dispose_.669
- ___Block_byref_object_dispose_.6924
- ___Block_byref_object_dispose_.7291
- ___Block_byref_object_dispose_.7569
- ___Block_byref_object_dispose_.7986
- ___Block_byref_object_dispose_.872
- ___Block_byref_object_dispose_.9365
- ___Block_byref_object_dispose_.9624
- ___CPLConfigurationOSLogDomain.18987
- ___CPLConfigurationOSLogDomain.onceToken.18993
- ___CPLConfigurationOSLogDomain.result.18995
- ___CPLForceSyncOSLogDomain.20397
- ___CPLForceSyncOSLogDomain.onceToken.20406
- ___CPLForceSyncOSLogDomain.result.20407
- ___CPLSchedulerOSLogDomain.7236
- ___CPLSchedulerOSLogDomain.onceToken.7237
- ___CPLSchedulerOSLogDomain.result.7238
- ___CPLSessionOSLogDomain.15839
- ___CPLSessionOSLogDomain.17720
- ___CPLSessionOSLogDomain.22280
- ___CPLSessionOSLogDomain.onceToken.15890
- ___CPLSessionOSLogDomain.onceToken.17725
- ___CPLSessionOSLogDomain.onceToken.22282
- ___CPLSessionOSLogDomain.result.15891
- ___CPLSessionOSLogDomain.result.17726
- ___CPLSessionOSLogDomain.result.22284
- ___CPLStorageOSLogDomain.10804
- ___CPLStorageOSLogDomain.10889
- ___CPLStorageOSLogDomain.17308
- ___CPLStorageOSLogDomain.19730
- ___CPLStorageOSLogDomain.2001
- ___CPLStorageOSLogDomain.21021
- ___CPLStorageOSLogDomain.21664
- ___CPLStorageOSLogDomain.21912
- ___CPLStorageOSLogDomain.497
- ___CPLStorageOSLogDomain.6011
- ___CPLStorageOSLogDomain.7525
- ___CPLStorageOSLogDomain.8267
- ___CPLStorageOSLogDomain.8673
- ___CPLStorageOSLogDomain.8840
- ___CPLStorageOSLogDomain.896
- ___CPLStorageOSLogDomain.9031
- ___CPLStorageOSLogDomain.onceToken.10815
- ___CPLStorageOSLogDomain.onceToken.10892
- ___CPLStorageOSLogDomain.onceToken.14173
- ___CPLStorageOSLogDomain.onceToken.17310
- ___CPLStorageOSLogDomain.onceToken.19732
- ___CPLStorageOSLogDomain.onceToken.20012
- ___CPLStorageOSLogDomain.onceToken.2003
- ___CPLStorageOSLogDomain.onceToken.21025
- ___CPLStorageOSLogDomain.onceToken.21669
- ___CPLStorageOSLogDomain.onceToken.21920
- ___CPLStorageOSLogDomain.onceToken.499
- ___CPLStorageOSLogDomain.onceToken.6013
- ___CPLStorageOSLogDomain.onceToken.7527
- ___CPLStorageOSLogDomain.onceToken.8275
- ___CPLStorageOSLogDomain.onceToken.8679
- ___CPLStorageOSLogDomain.onceToken.8842
- ___CPLStorageOSLogDomain.onceToken.902
- ___CPLStorageOSLogDomain.onceToken.9033
- ___CPLStorageOSLogDomain.result.10817
- ___CPLStorageOSLogDomain.result.10894
- ___CPLStorageOSLogDomain.result.14175
- ___CPLStorageOSLogDomain.result.17312
- ___CPLStorageOSLogDomain.result.19734
- ___CPLStorageOSLogDomain.result.20013
- ___CPLStorageOSLogDomain.result.2005
- ___CPLStorageOSLogDomain.result.21027
- ___CPLStorageOSLogDomain.result.21671
- ___CPLStorageOSLogDomain.result.21922
- ___CPLStorageOSLogDomain.result.501
- ___CPLStorageOSLogDomain.result.6015
- ___CPLStorageOSLogDomain.result.7528
- ___CPLStorageOSLogDomain.result.8276
- ___CPLStorageOSLogDomain.result.8681
- ___CPLStorageOSLogDomain.result.8843
- ___CPLStorageOSLogDomain.result.9034
- ___CPLStorageOSLogDomain.result.904
- ___CPLStoreOSLogDomain.2992
- ___CPLStoreOSLogDomain.onceToken.2993
- ___CPLStoreOSLogDomain.result.2994
- ___CPLTaskOSLogDomain.11076
- ___CPLTaskOSLogDomain.1315
- ___CPLTaskOSLogDomain.13631
- ___CPLTaskOSLogDomain.14085
- ___CPLTaskOSLogDomain.15154
- ___CPLTaskOSLogDomain.16648
- ___CPLTaskOSLogDomain.20823
- ___CPLTaskOSLogDomain.22619
- ___CPLTaskOSLogDomain.23697
- ___CPLTaskOSLogDomain.2568
- ___CPLTaskOSLogDomain.5275
- ___CPLTaskOSLogDomain.611
- ___CPLTaskOSLogDomain.6846
- ___CPLTaskOSLogDomain.onceToken.11111
- ___CPLTaskOSLogDomain.onceToken.1343
- ___CPLTaskOSLogDomain.onceToken.13633
- ___CPLTaskOSLogDomain.onceToken.14087
- ___CPLTaskOSLogDomain.onceToken.15163
- ___CPLTaskOSLogDomain.onceToken.16655
- ___CPLTaskOSLogDomain.onceToken.20865
- ___CPLTaskOSLogDomain.onceToken.22630
- ___CPLTaskOSLogDomain.onceToken.23705
- ___CPLTaskOSLogDomain.onceToken.2570
- ___CPLTaskOSLogDomain.onceToken.5278
- ___CPLTaskOSLogDomain.onceToken.614
- ___CPLTaskOSLogDomain.onceToken.6858
- ___CPLTaskOSLogDomain.result.11113
- ___CPLTaskOSLogDomain.result.1344
- ___CPLTaskOSLogDomain.result.13635
- ___CPLTaskOSLogDomain.result.14088
- ___CPLTaskOSLogDomain.result.15165
- ___CPLTaskOSLogDomain.result.16656
- ___CPLTaskOSLogDomain.result.20866
- ___CPLTaskOSLogDomain.result.22632
- ___CPLTaskOSLogDomain.result.23706
- ___CPLTaskOSLogDomain.result.2572
- ___CPLTaskOSLogDomain.result.5280
- ___CPLTaskOSLogDomain.result.616
- ___CPLTaskOSLogDomain.result.6860
- _____CPLConfigurationOSLogDomain_block_invoke.18998
- _____CPLForceSyncOSLogDomain_block_invoke.20409
- _____CPLSchedulerOSLogDomain_block_invoke.7240
- _____CPLSessionOSLogDomain_block_invoke.15893
- _____CPLSessionOSLogDomain_block_invoke.17728
- _____CPLSessionOSLogDomain_block_invoke.22287
- _____CPLStorageOSLogDomain_block_invoke.10820
- _____CPLStorageOSLogDomain_block_invoke.10897
- _____CPLStorageOSLogDomain_block_invoke.14180
- _____CPLStorageOSLogDomain_block_invoke.17315
- _____CPLStorageOSLogDomain_block_invoke.19737
- _____CPLStorageOSLogDomain_block_invoke.20019
- _____CPLStorageOSLogDomain_block_invoke.2008
- _____CPLStorageOSLogDomain_block_invoke.21030
- _____CPLStorageOSLogDomain_block_invoke.21674
- _____CPLStorageOSLogDomain_block_invoke.21925
- _____CPLStorageOSLogDomain_block_invoke.504
- _____CPLStorageOSLogDomain_block_invoke.6018
- _____CPLStorageOSLogDomain_block_invoke.7530
- _____CPLStorageOSLogDomain_block_invoke.8278
- _____CPLStorageOSLogDomain_block_invoke.8684
- _____CPLStorageOSLogDomain_block_invoke.8845
- _____CPLStorageOSLogDomain_block_invoke.9036
- _____CPLStorageOSLogDomain_block_invoke.907
- _____CPLStoreOSLogDomain_block_invoke.2996
- _____CPLTaskOSLogDomain_block_invoke.11116
- _____CPLTaskOSLogDomain_block_invoke.1346
- _____CPLTaskOSLogDomain_block_invoke.13638
- _____CPLTaskOSLogDomain_block_invoke.14090
- _____CPLTaskOSLogDomain_block_invoke.15168
- _____CPLTaskOSLogDomain_block_invoke.16658
- _____CPLTaskOSLogDomain_block_invoke.20868
- _____CPLTaskOSLogDomain_block_invoke.22635
- _____CPLTaskOSLogDomain_block_invoke.23708
- _____CPLTaskOSLogDomain_block_invoke.2575
- _____CPLTaskOSLogDomain_block_invoke.5283
- _____CPLTaskOSLogDomain_block_invoke.619
- _____CPLTaskOSLogDomain_block_invoke.6863
- ___block_descriptor_104_e8_32s40s48s56s64s72s80bs88r96r_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s80l8s48l8s56l8r88l8s64l8r96l8s72l8
- ___block_descriptor_113_e8_32s40s48s56s64s72s80bs88bs96r104r_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s80l8s48l8s56l8r96l8s64l8r104l8s72l8s88l8
- ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96s104s112s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8
- ___block_descriptor_129_e8_32s40s48s56s64s72s80s88bs96bs104r112r_e5_v8?0ls32l8s40l8r104l8s88l8s48l8s56l8s64l8s96l8s72l8r112l8s80l8
- ___block_descriptor_48_e8_32s40bs_e45_v24?0"CPLRecordChange"8"CPLRecordChange"16ls40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e25_v16?0"CPLCallObserver"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e47_v24?0"_CPLResourcesMutableArray"8"NSError"16ls32l8s64l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s64l8s48l8s56l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e49_v32?0"CPLRecordChange"8"NSArray"16"NSError"24ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_literal_global.10043
- ___block_literal_global.1019
- ___block_literal_global.1022
- ___block_literal_global.103
- ___block_literal_global.10425
- ___block_literal_global.105.18510
- ___block_literal_global.10662
- ___block_literal_global.10816
- ___block_literal_global.10893
- ___block_literal_global.110.20562
- ___block_literal_global.11112
- ___block_literal_global.1179
- ___block_literal_global.12.7650
- ___block_literal_global.12035
- ___block_literal_global.12311
- ___block_literal_global.12802
- ___block_literal_global.134
- ___block_literal_global.13634
- ___block_literal_global.1384
- ___block_literal_global.13886
- ___block_literal_global.14.14121
- ___block_literal_global.14.9080
- ___block_literal_global.14120
- ___block_literal_global.14174
- ___block_literal_global.142.20565
- ___block_literal_global.14337
- ___block_literal_global.1462
- ___block_literal_global.14875
- ___block_literal_global.14895
- ___block_literal_global.14959
- ___block_literal_global.15164
- ___block_literal_global.1542
- ___block_literal_global.15702
- ___block_literal_global.158
- ___block_literal_global.159.20566
- ___block_literal_global.15910
- ___block_literal_global.16461
- ___block_literal_global.1651
- ___block_literal_global.1664
- ___block_literal_global.16760
- ___block_literal_global.1678
- ___block_literal_global.1680
- ___block_literal_global.1682
- ___block_literal_global.1685
- ___block_literal_global.1689
- ___block_literal_global.1691
- ___block_literal_global.1693
- ___block_literal_global.1695
- ___block_literal_global.1697
- ___block_literal_global.1699
- ___block_literal_global.170
- ___block_literal_global.1701
- ___block_literal_global.1703
- ___block_literal_global.1705
- ___block_literal_global.1707
- ___block_literal_global.1709
- ___block_literal_global.171.20567
- ___block_literal_global.17105
- ___block_literal_global.1711
- ___block_literal_global.1712
- ___block_literal_global.1713
- ___block_literal_global.1715
- ___block_literal_global.1717
- ___block_literal_global.1719
- ___block_literal_global.1727
- ___block_literal_global.17311
- ___block_literal_global.1737
- ___block_literal_global.1745
- ___block_literal_global.1747
- ___block_literal_global.17738
- ___block_literal_global.17910
- ___block_literal_global.18048
- ___block_literal_global.183
- ___block_literal_global.1836
- ___block_literal_global.18624
- ___block_literal_global.187
- ___block_literal_global.1871
- ___block_literal_global.18994
- ___block_literal_global.190
- ___block_literal_global.1902
- ___block_literal_global.1908
- ___block_literal_global.19377
- ___block_literal_global.19733
- ___block_literal_global.19898
- ___block_literal_global.2.23973
- ___block_literal_global.20015
- ___block_literal_global.2004
- ___block_literal_global.202
- ___block_literal_global.20558
- ___block_literal_global.20883
- ___block_literal_global.21026
- ___block_literal_global.21197
- ___block_literal_global.212
- ___block_literal_global.21670
- ___block_literal_global.21921
- ___block_literal_global.22081
- ___block_literal_global.22283
- ___block_literal_global.22433
- ___block_literal_global.22689
- ___block_literal_global.2274
- ___block_literal_global.23245
- ___block_literal_global.23381
- ___block_literal_global.23453
- ___block_literal_global.23851
- ___block_literal_global.23967
- ___block_literal_global.24.13840
- ___block_literal_global.240
- ___block_literal_global.24081
- ___block_literal_global.24266
- ___block_literal_global.2451
- ___block_literal_global.25
- ___block_literal_global.2507
- ___block_literal_global.2571
- ___block_literal_global.264.22631
- ___block_literal_global.27.15929
- ___block_literal_global.276
- ___block_literal_global.279
- ___block_literal_global.290
- ___block_literal_global.2971
- ___block_literal_global.300
- ___block_literal_global.302
- ___block_literal_global.304
- ___block_literal_global.306
- ___block_literal_global.318
- ___block_literal_global.32.22049
- ___block_literal_global.3218
- ___block_literal_global.329
- ___block_literal_global.33.6975
- ___block_literal_global.34.2448
- ___block_literal_global.34.9620
- ___block_literal_global.3485
- ___block_literal_global.355
- ___block_literal_global.361
- ___block_literal_global.368.21301
- ___block_literal_global.3703
- ___block_literal_global.391
- ___block_literal_global.3920
- ___block_literal_global.42.7657
- ___block_literal_global.4341
- ___block_literal_global.443
- ___block_literal_global.4477
- ___block_literal_global.4631
- ___block_literal_global.47.7659
- ___block_literal_global.48
- ___block_literal_global.50.6966
- ___block_literal_global.500
- ___block_literal_global.5060
- ___block_literal_global.5141
- ___block_literal_global.5279
- ___block_literal_global.531
- ___block_literal_global.534
- ___block_literal_global.54.5040
- ___block_literal_global.543
- ___block_literal_global.5435
- ___block_literal_global.5544
- ___block_literal_global.577
- ___block_literal_global.580
- ___block_literal_global.60
- ___block_literal_global.6014
- ___block_literal_global.615
- ___block_literal_global.6208
- ___block_literal_global.6485
- ___block_literal_global.651
- ___block_literal_global.654
- ___block_literal_global.657
- ___block_literal_global.6859
- ___block_literal_global.6974
- ___block_literal_global.72.16419
- ___block_literal_global.731
- ___block_literal_global.7352
- ___block_literal_global.737
- ___block_literal_global.740
- ___block_literal_global.743
- ___block_literal_global.746
- ___block_literal_global.7647
- ___block_literal_global.77.15697
- ___block_literal_global.8.23983
- ___block_literal_global.8382
- ___block_literal_global.848
- ___block_literal_global.8574
- ___block_literal_global.8680
- ___block_literal_global.8779
- ___block_literal_global.90.7669
- ___block_literal_global.903
- ___block_literal_global.9082
- ___block_literal_global.9255
- ___block_literal_global.93.18514
- ___block_literal_global.9508
- ___block_literal_global.9729
- ___cpl_dispatch_async_block_invoke.11072
- ___cpl_dispatch_async_block_invoke.11696
- ___cpl_dispatch_async_block_invoke.1349
- ___cpl_dispatch_async_block_invoke.13643
- ___cpl_dispatch_async_block_invoke.14009
- ___cpl_dispatch_async_block_invoke.14081
- ___cpl_dispatch_async_block_invoke.15245
- ___cpl_dispatch_async_block_invoke.16248
- ___cpl_dispatch_async_block_invoke.16714
- ___cpl_dispatch_async_block_invoke.17059
- ___cpl_dispatch_async_block_invoke.17544
- ___cpl_dispatch_async_block_invoke.1784
- ___cpl_dispatch_async_block_invoke.18044
- ___cpl_dispatch_async_block_invoke.18973
- ___cpl_dispatch_async_block_invoke.20248
- ___cpl_dispatch_async_block_invoke.20821
- ___cpl_dispatch_async_block_invoke.21204
- ___cpl_dispatch_async_block_invoke.22435
- ___cpl_dispatch_async_block_invoke.22638
- ___cpl_dispatch_async_block_invoke.23751
- ___cpl_dispatch_async_block_invoke.6428
- ___cpl_dispatch_async_block_invoke.672
- ___cpl_dispatch_async_block_invoke.6844
- ___cpl_dispatch_async_block_invoke.7113
- ___cpl_dispatch_async_block_invoke.7539
- ___cpl_dispatch_async_block_invoke.9361
- ___cpl_dispatch_async_block_invoke.9706
- __doProtected:.onceToken.14894
- __doProtected:.onceToken.22432
- __doProtected:.queue.22434
- __statusDidChange.11902
- _copyDerivativesFromRecordIfPossible:.originalDerivativesImageAndVideo.18532
- _initWithCPLArchiver:.onceToken.1905
- _initWithCPLArchiver:.stringClass.1906
- _initWithCoder:.logOnceToken.19900
- _initWithCoder:.onceToken.10366
- _initWithCoder:.onceToken.13885
- _initWithCoder:.onceToken.17737
- _initWithCoder:.onceToken.19897
- _initWithCoder:.onceToken.22080
- _initWithCoder:.onceToken.24265
- _initWithCoder:.onceToken.5039
- _initWithCoder:.onceToken.5140
- _initWithCoder:.onceToken.6203
- _initWithCoder:.pushContextsClasses.22082
- _initWithCoder:.stringClass.10367
- _isFeatureEnabled
- _kPCSSetupDSIDAny
- _objc_msgSend$_activeQueueForTransferTask:
- _objc_msgSend$_bestQueueWithCancellableTransportTasks
- _objc_msgSend$_canScheduleBackgroundDownloads
- _objc_msgSend$_decodeKey:class:inDictionary:
- _objc_msgSend$_dequeueTransferTaskInActiveQueue:
- _objc_msgSend$_dispatchTransportTasksIfNecessary
- _objc_msgSend$_downloadTaskForLocalResource:clientBundleID:options:proposedTaskIdentifier:didStartHandler:progressHandler:completionHandler:
- _objc_msgSend$_encodeKey:
- _objc_msgSend$_enqueueTransferTaskInActiveQueue:
- _objc_msgSend$_failedTaskWithCompletionHandler:error:resource:taskIdentifier:options:
- _objc_msgSend$_launchTransportTaskForQueue:
- _objc_msgSend$_queuesStatus
- _objc_msgSend$_realDownloadTaskForLocalResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:
- _objc_msgSend$_requestBackgroundDownloads
- _objc_msgSend$_resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:
- _objc_msgSend$_scheduleBackgroundDownloadsIfNecessary
- _objc_msgSend$_shouldTryLowPriorityDownloadWithError:
- _objc_msgSend$cachedResourcesForReferenceResource:adjustment:includePosterFrame:
- _objc_msgSend$noteGeneratedResouces:haveBeenGeneratedForReferenceResource:adjustment:includePosterFrame:
- _objc_msgSend$object
- _objc_msgSend$proposedCloudScopedIdentifierWithError:
- _objc_msgSend$tempFolderURLForGeneratedResourcesWithReferenceResource:adjustment:includePosterFrame:
- _objc_msgSend$updateBlockedMetrics:syncRequested:
- _overridesFeatureFlag
- _propertiesForChangeType:.onceToken.14721
- _propertiesForChangeType:.onceToken.18547
- _propertiesForChangeType:.onceToken.23380
- _propertiesForChangeType:.properties.23382
CStrings:
+ "\n\tShared Collection feature is disabled"
+ "\nPrediction for %@ session:\n  %@"
+ "\nlast session: %@ - %@ for %@"
+ "\nlast session: %@ - %@ for less than 1s"
+ " (just-in-case)"
+ " <%@>"
+ "\"%@ %@ is not supported by %@\""
+ "\"%@ does not support %@ (key: %@)\""
+ "\"%@ does not support %@\""
+ "\"%@ is not supported for %@\""
+ "\"Incorrect class for CPLScopedIdentifier. Found %@: '%@'\""
+ "\"Incorrect number for NSDate. Found %@: '%@'\""
+ "\"Incorrect string for %@. Found %@: '%@'\""
+ "\"Incorrect string for CLLocation. Found %@: '%@'\""
+ "\"Incorrect string for CPLPersonReference. Found %@: '%@'\""
+ "\"Incorrect string for NSUUID. Found %@: '%@'\""
+ "\"Invalid %@. Found %@ in archive: '%@'\""
+ "\"Invalid object properties dictionary. Found %@ in archive: '%@'\""
+ "\"Unexpected array. Found %@: '%@'\""
+ "\"Unexpected dictionary for %@. Found %@: '%@'\""
+ "%@ (%@) is not supported"
+ "%@ after"
+ "%@ before"
+ "%@ failed %@: %@"
+ "%@ has no asset identifier"
+ "%@ is running while an other call is still ongoing"
+ "%@: %@ %@ is not supported by %@"
+ "%@: %@ does not support %@"
+ "%@: %@ does not support %@ (key: %@)"
+ "%@: %@ is not supported for %@"
+ "%@: Incorrect class for CPLScopedIdentifier. Found %@: '%@'"
+ "%@: Incorrect number for NSDate. Found %@: '%@'"
+ "%@: Incorrect string for %@. Found %@: '%@'"
+ "%@: Incorrect string for CLLocation. Found %@: '%@'"
+ "%@: Incorrect string for CPLPersonReference. Found %@: '%@'"
+ "%@: Incorrect string for NSUUID. Found %@: '%@'"
+ "%@: Invalid %@. Found %@ in archive: '%@'"
+ "%@: Invalid object properties dictionary. Found %@ in archive: '%@'"
+ "%@: Unexpected array. Found %@: '%@'"
+ "%@: Unexpected dictionary for %@. Found %@: '%@'"
+ "(no context)"
+ "/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLCallObserver.m"
+ "/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineDerivativesCache.m"
+ "/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLCommentChange.m"
+ "@\"<CPLSyncSessionRuntimeCharacteristics>\""
+ "@36@0:8Q16B24Q28"
+ "@84@0:8Q16Q24B32{?={?=qiIq}{?=qiIq}}36"
+ "ARCHIVING(%@)"
+ "ActivityMotionStateBlockedCount"
+ "Archiver exception raised - %@"
+ "Automatically reverting %@ to discretionary"
+ "CPLAllowCancellingDerivativesGeneration"
+ "CPLAllowDeferringDerivativesGeneration"
+ "CPLArchiverFailureContext"
+ "CPLAssertArchiverException"
+ "CPLCollectionShareScopeChange"
+ "CPLCommentChange"
+ "CPLEnableCollectionShares"
+ "CPLLegacyBackgroundSchedulingStatus"
+ "CPLMingleDisableStashMaster"
+ "CPLMingleDisableStashMaster user default set to override stash master on mingle: %@"
+ "CPLPredictionDateFormatter"
+ "CPLReactChange"
+ "CPLSyncSessionBlockedState"
+ "CPLTextCommentChange"
+ "CPLUsesSandboxEnvironment"
+ "Can't map cloud \"assetScopedIdentifier\" (%@) of %@"
+ "Can't map cloud \"assetScopedIdentifier\" in %@"
+ "Can't map cloud \"containerScopedIdentifier\" in %@"
+ "Can't map cloud \"itemScopedIdentifier\" in %@"
+ "Can't map cloud \"masterScopedIdentifier\" in %@"
+ "Can't map cloud \"parentScopedIdentifier\" in %@"
+ "Can't map cloud \"resourceCopyFromScopedIdentifier\" in %@"
+ "Can't map local \"assetScopedIdentifier\" (%@) of %@"
+ "Can't map local \"assetScopedIdentifier\" in %@"
+ "Can't map local \"containerScopedIdentifier\" in %@"
+ "Can't map local \"itemScopedIdentifier\" in %@"
+ "Can't map local \"masterScopedIdentifier\" in %@"
+ "Can't map local \"parentScopedIdentifier\" in %@"
+ "Cancelling derivatives generation %p before even being launched"
+ "Client tried to push %@ but this engine does not support that - ignoring"
+ "Closed database after opening error"
+ "Cloud resource %@ does not match any local resource of %@"
+ "CloudPhotoLibrary-800.14.111"
+ "ConsoleModeBlockedCount"
+ "Could not find primary Apple Account"
+ "Creating %{public}@"
+ "DASDoItNowUnBlockedCount"
+ "Deleted(React)"
+ "Deleted(TextComment)"
+ "Deleting active scope %{public}@ because client does not care"
+ "Deleting inactive scope %{public}@"
+ "Derivatives generation %p is delayed until previous calls complete"
+ "Derivatives generation from %@ has been cancelled"
+ "DeviceActivityBlockedCount"
+ "DeviceActivityEarlyThermalWarningBlockedCount"
+ "Failed to close database after opening error: %@"
+ "Failed to get Account Store"
+ "Failed to get Account store: %@"
+ "Fixing missing entry in ID mapping for %@"
+ "Found main scope %@ which has not been identified yet - forcing scope type to %@"
+ "Generating derivatives for %@: %.0f%% (chunk length: %@)"
+ "ID mapping entry is missing for %@ - will need to fix that"
+ "Internal inconsistency"
+ "Launching delayed derivatives generation %p"
+ "Marking %@ as just-in-case session"
+ "Missing object calling %@"
+ "Missing resource %@ on disk during push to transport for %@"
+ "Missing selector calling %@"
+ "NSString * _Nonnull CPLCollectionSharePrefixForScopeWithIdentifier(NSString *__strong _Nonnull)"
+ "New record but not full record"
+ "New(React)"
+ "New(TextComment)"
+ "No DSID attached to primary Apple Account"
+ "NotDeleted(React)"
+ "NotDeleted(TextComment)"
+ "Partial %@ from client but new to the cache"
+ "Removing just-in-case from %@"
+ "Removing just-in-case from %@ as it was associated with a rescheduler"
+ "Reverting %@ to discretionary for %@"
+ "SharedCollection-"
+ "SharedCollections"
+ "SignificantTransferBlockedCount"
+ "Some client is in foreground but synchronization is disabled because of %{public}@"
+ "T@\"<CPLSyncSessionRescheduler>\",R,N,V_rescheduler"
+ "T@\"<CPLSyncSessionRuntimeCharacteristics>\",R"
+ "T@\"<CPLSyncSessionRuntimeCharacteristics>\",R,V_runtimeCharacteristics"
+ "T@\"NSData\",C,N,V_transportShare"
+ "T@\"NSDate\",C,N,V_commentDate"
+ "T@\"NSSet\",R,N,V_deletedScopeIdentifiers"
+ "T@\"NSString\",C,N,V_assetIdentifier"
+ "T@\"NSString\",C,N,V_commentText"
+ "T@\"NSString\",C,N,V_contributorUserIdentifier"
+ "TB,R,N,GisBlocked,V_blocked"
+ "TB,R,N,V_shouldBeTemporarilyNonDiscretionary"
+ "TB,R,N,V_shouldBypassCaches"
+ "TB,R,N,V_syncHasBeenRequested"
+ "TB,V_isJustInCaseSession"
+ "Temporarily running %@ non-discretionary for %@"
+ "TestSharedCollection-"
+ "Trying to activate %@ (%@) but this is not supported by this engine"
+ "Trying to enable main scope %@ but it is not a library"
+ "Trying to send messages to %@ but %@ has been killed"
+ "Trying to send messages to %@ but %@ has no connection ready"
+ "Unable to deserialize record in %@"
+ "Unable to serialize %@ in %@"
+ "Unexpected main scope prefix for main scope: %@"
+ "[detached session%@]"
+ "[session #%lu%@%@]"
+ "_allowsJustInCaseSessions"
+ "_blocked"
+ "_cachedResourcesForReferenceResource:adjustment:includePosterFrame:"
+ "_changesWithMissingIDMapping"
+ "_cleanTempFolderURLForGeneratedResourcesWithReferenceResource:adjustment:includePosterFrame:"
+ "_cloudResourceForLocalResource:cloudRecord:target:shouldNotTrustCaches:allowUnsafeClientCache:allowBypassingAllCaches:transportScopeMapping:error:"
+ "_commentDate"
+ "_commentText"
+ "_contributorUserIdentifier"
+ "_delayedGeneratedDerivativesCalls"
+ "_deletedScopeIdentifiers"
+ "_descriptionSuffix"
+ "_didLogShouldStashMasterRecords"
+ "_discardGenerateDerivativesProgress"
+ "_forceCloseWithCompletionHandler:"
+ "_generateDerivativesCancellationHandler"
+ "_generateDerivativesChange"
+ "_generateDerivativesDeferredHandler"
+ "_generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:"
+ "_generateDerivativesLastFractionCompleted"
+ "_generateDerivativesProgress"
+ "_generateDerivativesTotalSize"
+ "_generatingDerivativesForChange:fractionCompleted:chunkLength:"
+ "_hasSeenSomeChanges"
+ "_installGenerateDerivativesCancellationHandler:"
+ "_isGeneratingDerivatives"
+ "_isJustInCaseSession"
+ "_justInCaseSessionIsPossible"
+ "_lastSyncSessionDescription"
+ "_lastSyncSessionEndDate"
+ "_lastSyncSessionStartDate"
+ "_logKilled"
+ "_nextSessionIsJustInCase"
+ "_noteGeneratedResources:haveBeenGeneratedForReferenceResource:adjustment:includePosterFrame:"
+ "_noteSignificantEvent"
+ "_optimisticIDMapping"
+ "_popContext"
+ "_realIDMapping"
+ "_runtimeCharacteristics"
+ "_setError"
+ "_shouldBeTemporarilyNonDiscretionary"
+ "_shouldBypassCaches"
+ "_shouldStashMasterRecords"
+ "_syncHasBeenRequested"
+ "_transportShare"
+ "_unarchiving"
+ "aa_personID"
+ "aa_primaryAppleAccount"
+ "accepted-collection-share"
+ "addObserver:forKeyPath:options:context:"
+ "administrator"
+ "allowsUnsafeClientCache"
+ "archiverContext"
+ "assetScopedIdentifier"
+ "assetsd"
+ "asst"
+ "boundarykey"
+ "cUI"
+ "cleanupWithError:"
+ "clientCanPushScopeChange:"
+ "cmdt"
+ "collection-share-scope-sync"
+ "com.apple.cpl.get-apple-account"
+ "com.apple.cpl.mingle.disable-stash-master"
+ "comm"
+ "commentDate"
+ "commentText"
+ "contributorUserIdentifier"
+ "copyWithScopeType:"
+ "cpl.store.close.force"
+ "declined"
+ "deletedScopeIdentifiers"
+ "dsi"
+ "force close store"
+ "fractionCompleted"
+ "getBackgroundSchedulingStatusDictionaryWithCompletionHandler:"
+ "getBackgroundSchedulingStatusWithCompletionHandler:"
+ "getBytes:range:"
+ "hasError"
+ "initForLightweightUsageWithLibraryIdentifier:"
+ "initWithIntent:bypassCaches:priority:"
+ "initWithIntent:priority:bypassCaches:timeRange:"
+ "initWithRescheduler:blocked:syncHasBeenRequested:runtimeCharacteristics:"
+ "initWithStringRepresentation:defaultScopeIdentifier:"
+ "isInACPLShare"
+ "isJustInCaseSession"
+ "just after"
+ "just before"
+ "lastEvent"
+ "maximumSignificantTimeInterval"
+ "new"
+ "noteBlockedStateHasChanged:"
+ "observeValueForKeyPath:ofObject:change:context:"
+ "owned-collection-share"
+ "predictedDateForType:"
+ "proposedCloudScopedIdentifier"
+ "reac"
+ "reactType"
+ "removeObserver:forKeyPath:"
+ "removePredictedValueForType:"
+ "runtimeCharacteristics"
+ "scopeIndexes"
+ "setAssetScopedIdentifier:"
+ "setCommentDate:"
+ "setCommentText:"
+ "setContributorUserIdentifier:"
+ "setIsJustInCaseSession:"
+ "setTransportShare:"
+ "shouldBeTemporarilyNonDiscretionary"
+ "shouldBypassCaches"
+ "shouldShowBackgroundSchedulingStatusInTransport"
+ "stringForTimeIntervalNumber:now:"
+ "stringRepresentation"
+ "supportsActivationOfScopeWithType:"
+ "supportsCollectionShare"
+ "supportsRecordModificationDate"
+ "syncHasBeenRequested"
+ "syncSessionRequestedImmediateRuntime"
+ "timeIntervalSincePredictedDateForType:"
+ "transportShare"
+ "unableToDeserializeRecordInStorage:"
+ "unableToSerializeRecordError:inStorage:"
+ "unsubscribed"
+ "updateBlockedMetrics:syncRequested:runtimeCharacteristics:"
+ "updatePredictedDate:forType:"
+ "updatedPredictionRemovingValueForType:"
+ "v32@0:8B16B20@24"
+ "v40@0:8@16d24Q32"
+ "v48@0:8@16@24@32^v40"
+ "videoCodec"
+ "videoDuration"
+ "videoNominalFrameRate"
+ "videoOrientedHeight"
+ "videoOrientedWidth"
+ "\xc1"
+ "\xf0\xa1"
+ "\xf0\xf01"
- "\nPrediction for %@ session: %@"
- "%@ %@ is not supported by %@"
- "%@ does not support %@"
- "%@ is not supported for %@"
- "/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLArchiver.m"
- "@40@0:8@16#24@32"
- "@56@0:8@?16@24@32@40@48"
- "@80@0:8@16@24@32@40@48@?56@?64@?72"
- "CPLSyncSessionBlockedStateDidChangeNotification"
- "Client pushed records for an unknown scope %@ (likely because CPL database has been wiped) but does not support re-creating that scope itself. Automatically recreating it"
- "CloudPhotoLibrary-760.6.150"
- "Creating %@"
- "Deleting inactive scope %@"
- "Failed to re-create scope %@ automatically: %@"
- "Incorrect class for CPLScopedIdentifier. Found %@: '%@'"
- "Incorrect number for NSDate. Found %@: '%@'"
- "Incorrect string for %@. Found %@: '%@'"
- "Incorrect string for CLLocation. Found %@: '%@'"
- "Incorrect string for CPLPersonReference. Found %@: '%@'"
- "Incorrect string for NSUUID. Found %@: '%@'"
- "Invalid %@. Found %@ in archive: '%@'"
- "Invalid object properties dictionary. Found %@ in archive: '%@'"
- "Resource storage is invalid during push to transport"
- "Sync session failed %@: %@"
- "Trying to send messages to %@ but we have no connection ready"
- "Unexpected array. Found %@: '%@'"
- "Unexpected dictionary for %@. Found %@: '%@'"
- "[detached session]"
- "[session #%lu]"
- "_activeQueueForTransferTask:"
- "_bestQueueWithCancellableTransportTasks"
- "_canScheduleBackgroundDownloads"
- "_checkScopeIdentifier"
- "_decodeKey:class:inDictionary:"
- "_dequeueTransferTaskInActiveQueue:"
- "_dispatchTransportTasksIfNecessary"
- "_downloadTaskForLocalResource:clientBundleID:options:proposedTaskIdentifier:didStartHandler:progressHandler:completionHandler:"
- "_encodeKey:"
- "_enqueueTransferTaskInActiveQueue:"
- "_failedTaskWithCompletionHandler:error:resource:taskIdentifier:options:"
- "_launchTransportTaskForQueue:"
- "_queuesStatus"
- "_realDownloadTaskForLocalResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:"
- "_requestBackgroundDownloads"
- "_scheduleBackgroundDownloadsIfNecessary"
- "_shouldTryLowPriorityDownloadWithError:"
- "_syncObserver"
- "_unscheduleBackgroundDownloads"
- "cachedResourcesForReferenceResource:adjustment:includePosterFrame:"
- "isInAMomentShare"
- "new record but not full record"
- "noteGeneratedResouces:haveBeenGeneratedForReferenceResource:adjustment:includePosterFrame:"
- "object"
- "proposedCloudScopedIdentifierWithError:"
- "syncRequested"
- "tempFolderURLForGeneratedResourcesWithReferenceResource:adjustment:includePosterFrame:"
- "updateBlockedMetrics:syncRequested:"
- "\xf0q"
- "\xf0\xf0A"

```
