## CloudPhotoLibrary

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary`

```diff

-652.0.110.0.0
-  __TEXT.__text: 0x164840
-  __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_methlist: 0x10670
+662.0.141.0.0
+  __TEXT.__text: 0x16effc
+  __TEXT.__auth_stubs: 0xf40
+  __TEXT.__objc_methlist: 0x10c60
   __TEXT.__const: 0x260
-  __TEXT.__gcc_except_tab: 0x27cc
-  __TEXT.__oslogstring: 0x126b0
-  __TEXT.__cstring: 0x117f5
-  __TEXT.__unwind_info: 0x5064
-  __TEXT.__objc_classname: 0x1aca
-  __TEXT.__objc_methname: 0x263d6
-  __TEXT.__objc_methtype: 0x4088
-  __TEXT.__objc_stubs: 0x17920
+  __TEXT.__gcc_except_tab: 0x2984
+  __TEXT.__oslogstring: 0x12c12
+  __TEXT.__cstring: 0x11db4
+  __TEXT.__unwind_info: 0x52ac
+  __TEXT.__objc_classname: 0x1b75
+  __TEXT.__objc_methname: 0x274b0
+  __TEXT.__objc_methtype: 0x4238
+  __TEXT.__objc_stubs: 0x180c0
   __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0x5208
-  __DATA_CONST.__objc_classlist: 0x790
+  __DATA_CONST.__const: 0x5570
+  __DATA_CONST.__objc_classlist: 0x7c0
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x16030
-  __DATA_CONST.__objc_selrefs: 0x7968
+  __DATA_CONST.__objc_const: 0x16870
+  __DATA_CONST.__objc_selrefs: 0x7bf0
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_classrefs: 0x800
-  __DATA_CONST.__objc_superrefs: 0x748
-  __DATA_CONST.__objc_arraydata: 0x1208
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__const: 0x13e0
-  __AUTH_CONST.__cfstring: 0x13000
+  __DATA_CONST.__objc_classrefs: 0x838
+  __DATA_CONST.__objc_superrefs: 0x768
+  __DATA_CONST.__objc_arraydata: 0x1240
+  __AUTH_CONST.__objc_const: 0x288
+  __AUTH_CONST.__const: 0x15c0
+  __AUTH_CONST.__cfstring: 0x13600
   __AUTH_CONST.__objc_intobj: 0x630
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH_CONST.__auth_got: 0x7a0
-  __DATA.__objc_ivar: 0x1534
-  __DATA.__data: 0xde0
+  __AUTH_CONST.__auth_got: 0x7b0
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x15cc
+  __DATA.__data: 0xde8
   __DATA.__common: 0x21
-  __DATA.__bss: 0x888
-  __DATA_DIRTY.__const: 0xe20
-  __DATA_DIRTY.__objc_const: 0x65d8
-  __DATA_DIRTY.__objc_data: 0x4ba0
+  __DATA.__bss: 0x8b8
+  __DATA_DIRTY.__const: 0xca0
+  __DATA_DIRTY.__objc_const: 0x6590
+  __DATA_DIRTY.__objc_data: 0x4b50
   __DATA_DIRTY.__data: 0x1
   __DATA_DIRTY.__common: 0x8
-  __DATA_DIRTY.__bss: 0x420
+  __DATA_DIRTY.__bss: 0x410
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8E4E1F5C-D5AA-3576-858D-5BB3E0616525
-  Functions: 7415
-  Symbols:   22973
-  CStrings:  13433
+  UUID: 2BCAA4F0-5B13-3B94-B14C-F7DF762131F3
+  Functions: 7602
+  Symbols:   23542
+  CStrings:  13694
 
Symbols:
+ +[CPLAssetChange(DefaultsSupport) serverSupportsComputeState]
+ +[CPLRecordComputeState supportsSecureCoding]
+ +[CPLRecordComputeStateValidator supportsSecureCoding]
+ -[CPLAssetChange computeStateAdjustmentFingerprint]
+ -[CPLAssetChange computeStateLastUpdatedDate]
+ -[CPLAssetChange computeStateVersion]
+ -[CPLAssetChange setComputeStateAdjustmentFingerprint:]
+ -[CPLAssetChange setComputeStateLastUpdatedDate:]
+ -[CPLAssetChange setComputeStateVersion:]
+ -[CPLConfiguration(CPLConveniencePrivate) isComputeStateTaskUploadEnabled]
+ -[CPLConfiguration(CPLConveniencePrivate) maximumComputeStatesToUploadPerBatch]
+ -[CPLEngineFileStorage _identityForIdentifier:]
+ -[CPLEngineFileStorage commitFileWithIdentifier:error:]
+ -[CPLEngineFileStorage deleteFileWithIdentifier:error:]
+ -[CPLEngineFileStorage discardUncommittedFileWithIdentifier:error:]
+ -[CPLEngineFileStorage hasFileWithIdentifier:]
+ -[CPLEngineFileStorage openWithFileRecoveryHandler:error:]
+ -[CPLEngineFileStorage retainFileURLForIdentifier:error:]
+ -[CPLEngineFileStorage storeData:identifier:needsCommit:error:]
+ -[CPLEngineFileStorage storeFileAtURL:identifier:moveIfPossible:needsCommit:error:]
+ -[CPLEngineFileStorage storeUnretainedData:identifier:error:]
+ -[CPLEngineFileStorage storeUnretainedFileAtURL:identifier:error:]
+ -[CPLEngineLibrary isKeychainCDPEnabled]
+ -[CPLEngineLibrary setKeychainCDPEnabled:]
+ -[CPLEngineLibrary updateComputeSyncMetrics:silentDecryptionFailed:error:]
+ -[CPLEngineRecordComputeStatePushQueue .cxx_destruct]
+ -[CPLEngineRecordComputeStatePushQueue addComputeState:error:]
+ -[CPLEngineRecordComputeStatePushQueue computeStatesToUploadWithScopeIdentifier:localState:maximumCount:]
+ -[CPLEngineRecordComputeStatePushQueue countOfComputeStates]
+ -[CPLEngineRecordComputeStatePushQueue createIncomingDownloadFolderIfNecessaryWithError:]
+ -[CPLEngineRecordComputeStatePushQueue createNewTempDownloadFolderWithError:]
+ -[CPLEngineRecordComputeStatePushQueue deleteIncomingDownloadFolderWithError:]
+ -[CPLEngineRecordComputeStatePushQueue deleteRecordsForScopeIndex:maxCount:deletedCount:error:]
+ -[CPLEngineRecordComputeStatePushQueue fileSizeForComputeStatePayloadFileURL:error:]
+ -[CPLEngineRecordComputeStatePushQueue fileStorage]
+ -[CPLEngineRecordComputeStatePushQueue hasChangesInScopeWithIdentifier:]
+ -[CPLEngineRecordComputeStatePushQueue incomingDownloadFolderURL]
+ -[CPLEngineRecordComputeStatePushQueue initWithEngineStore:name:]
+ -[CPLEngineRecordComputeStatePushQueue noteComputeStateDownloadRequest]
+ -[CPLEngineRecordComputeStatePushQueue openWithError:]
+ -[CPLEngineRecordComputeStatePushQueue performMaintenanceWithError:]
+ -[CPLEngineRecordComputeStatePushQueue releaseFileURL:forComputeState:error:]
+ -[CPLEngineRecordComputeStatePushQueue removeComputeState:error:]
+ -[CPLEngineRecordComputeStatePushQueue removeComputeStateWithLocalScopedIdentifier:error:]
+ -[CPLEngineRecordComputeStatePushQueue retainFileURLForComputeState:error:]
+ -[CPLEngineRecordComputeStatePushQueue scopeType]
+ -[CPLEngineRecordComputeStatePushQueue setThrottlingDate:]
+ -[CPLEngineRecordComputeStatePushQueue statusDictionary]
+ -[CPLEngineRecordComputeStatePushQueue status]
+ -[CPLEngineRecordComputeStatePushQueue throttlingDate]
+ -[CPLEngineRecordComputeStatePushQueue updateLocalStateForComputeState:newLocalState:error:]
+ -[CPLEngineRecordComputeStatePushQueue writeTransactionDidFail]
+ -[CPLEngineRecordComputeStatePushQueue writeTransactionDidSucceed]
+ -[CPLEngineResourceStorage performMaintenanceWithError:]
+ -[CPLEngineScheduler noteScopeNeedsToUploadComputeState]
+ -[CPLEngineScopeStorage doesScopeNeedToUploadComputeState:]
+ -[CPLEngineScopeStorage enumeratorForScopesNeedingToUploadComputeState]
+ -[CPLEngineScopeStorage hasScopesNeedingToUploadComputeState]
+ -[CPLEngineScopeStorage setScope:hasCompletedUploadComputeStateTask:error:]
+ -[CPLEngineScopeStorage setScopeNeedsToUploadComputeState:error:]
+ -[CPLEngineScopeStorage shouldDropAllUploadsForScope:dropReason:shouldQuarantineRecords:]
+ -[CPLEngineScopeStorage uploadComputeStateTaskForScope:]
+ -[CPLEngineStorage performMaintenanceWithError:]
+ -[CPLEngineStore recordComputeStatePushQueue]
+ -[CPLEngineTransport createGroupForComputeStateDownloadOnDemand]
+ -[CPLEngineTransport createGroupForComputeStateDownloadPrefetch]
+ -[CPLEngineTransport createGroupForComputeStateUpload]
+ -[CPLEngineTransport downloadComputeStatesWithScopedIdentifiers:scope:sharedScope:targetStorageURL:transportScopeMapping:completionHandler:]
+ -[CPLEngineTransport uploadComputeStates:scope:sharedScope:targetMapping:transportScopeMapping:knownRecords:completionHandler:]
+ -[CPLLibraryManager attachComputeStates:completionHandler:]
+ -[CPLLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:onDemand:completionHandler:]
+ -[CPLLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]
+ -[CPLMetrics .cxx_destruct]
+ -[CPLMetrics _loadIfNecessary]
+ -[CPLMetrics _save]
+ -[CPLMetrics countForKey:]
+ -[CPLMetrics forceLoad]
+ -[CPLMetrics incrementCountForKey:]
+ -[CPLMetrics initWithClientLibraryBaseURL:]
+ -[CPLMetrics initWithClientLibraryBaseURLForCPLEngine:]
+ -[CPLMetrics metricsDescription]
+ -[CPLMetrics resetMetrics]
+ -[CPLProxyLibraryManager attachComputeStates:completionHandler:]
+ -[CPLProxyLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]
+ -[CPLRecordComputeState .cxx_destruct]
+ -[CPLRecordComputeState adjustmentFingerprint]
+ -[CPLRecordComputeState description]
+ -[CPLRecordComputeState encodeWithCoder:]
+ -[CPLRecordComputeState fileStorageIdentifier]
+ -[CPLRecordComputeState fileURL]
+ -[CPLRecordComputeState initWithCoder:]
+ -[CPLRecordComputeState initWithItemScopedIdentifier:fileStorageIdentifier:version:fileURL:adjustmentFingerprint:lastUpdatedDate:]
+ -[CPLRecordComputeState initWithItemScopedIdentifier:version:fileURL:adjustmentFingerprint:lastUpdatedDate:]
+ -[CPLRecordComputeState itemScopedIdentifier]
+ -[CPLRecordComputeState lastUpdatedDate]
+ -[CPLRecordComputeState redactedDescription]
+ -[CPLRecordComputeState setFileStorageIdentifier:]
+ -[CPLRecordComputeState version]
+ -[CPLRecordComputeStateValidator encodeWithCoder:]
+ -[CPLRecordComputeStateValidator initWithCoder:]
+ -[CPLRecordComputeStateValidator isComputeStateValid:]
+ -[CPLRecordComputeStateVersion compare:]
+ -[CPLRecordComputeStateVersion description]
+ -[CPLRecordComputeStateVersion hash]
+ -[CPLRecordComputeStateVersion initWithMajorVersion:stage:]
+ -[CPLRecordComputeStateVersion initWithString:]
+ -[CPLRecordComputeStateVersion isEqual:]
+ -[CPLRecordComputeStateVersion majorVersion]
+ -[CPLRecordComputeStateVersion redactedDescription]
+ -[CPLRecordComputeStateVersion stage]
+ -[CPLStatus isKeychainCDPEnabled]
+ -[CPLStatus setKeychainCDPEnabled:]
+ -[CPLUploadComputeStatesScopeTask .cxx_destruct]
+ -[CPLUploadComputeStatesScopeTask _discardExtractedBatchAndGetNextBatch]
+ -[CPLUploadComputeStatesScopeTask _dropAllComputeStates]
+ -[CPLUploadComputeStatesScopeTask _getNextBatchAndUpload]
+ -[CPLUploadComputeStatesScopeTask _updateComputeSyncUploadMetricsWithError:]
+ -[CPLUploadComputeStatesScopeTask _uploadComputeStatesTaskDidFinishWithError:]
+ -[CPLUploadComputeStatesScopeTask _uploadExtractedBatch]
+ -[CPLUploadComputeStatesScopeTask cancel]
+ -[CPLUploadComputeStatesScopeTask checkScopeIsValidInTransaction:]
+ -[CPLUploadComputeStatesScopeTask initWithEngineLibrary:session:clientCacheIdentifier:scope:transportScope:]
+ -[CPLUploadComputeStatesScopeTask launch]
+ -[CPLUploadComputeStatesScopeTask taskDidFinishWithError:]
+ -[CPLUploadComputeStatesScopeTask taskIdentifier]
+ -[CPLUploadComputeStatesTask enumerateScopesForTaskInTransaction:]
+ -[CPLUploadComputeStatesTask newScopedTaskWithScope:session:transportScope:clientCacheIdentifier:]
+ -[CPLUploadComputeStatesTask taskIdentifier]
+ -[NSError(CPLAdditions) isCPLEncryptionError]
+ -[NSError(CPLAdditions) isCPLThrottlingError]
+ GCC_except_table1032
+ GCC_except_table1151
+ GCC_except_table1230
+ GCC_except_table1822
+ GCC_except_table1828
+ GCC_except_table183
+ GCC_except_table1868
+ GCC_except_table1950
+ GCC_except_table1960
+ GCC_except_table201
+ GCC_except_table2091
+ GCC_except_table210
+ GCC_except_table213
+ GCC_except_table215
+ GCC_except_table217
+ GCC_except_table2171
+ GCC_except_table2378
+ GCC_except_table2380
+ GCC_except_table2463
+ GCC_except_table2524
+ GCC_except_table2526
+ GCC_except_table2662
+ GCC_except_table2665
+ GCC_except_table2679
+ GCC_except_table2745
+ GCC_except_table2749
+ GCC_except_table2751
+ GCC_except_table2753
+ GCC_except_table2757
+ GCC_except_table2860
+ GCC_except_table2907
+ GCC_except_table3114
+ GCC_except_table3176
+ GCC_except_table3180
+ GCC_except_table3182
+ GCC_except_table3431
+ GCC_except_table3461
+ GCC_except_table3488
+ GCC_except_table3505
+ GCC_except_table3512
+ GCC_except_table3520
+ GCC_except_table3522
+ GCC_except_table3536
+ GCC_except_table3538
+ GCC_except_table3540
+ GCC_except_table356
+ GCC_except_table365
+ GCC_except_table3842
+ GCC_except_table3875
+ GCC_except_table3957
+ GCC_except_table3967
+ GCC_except_table4024
+ GCC_except_table4027
+ GCC_except_table4191
+ GCC_except_table4199
+ GCC_except_table425
+ GCC_except_table4276
+ GCC_except_table4280
+ GCC_except_table4284
+ GCC_except_table429
+ GCC_except_table4291
+ GCC_except_table4307
+ GCC_except_table4348
+ GCC_except_table4356
+ GCC_except_table4411
+ GCC_except_table4413
+ GCC_except_table4415
+ GCC_except_table4427
+ GCC_except_table4562
+ GCC_except_table458
+ GCC_except_table4599
+ GCC_except_table4608
+ GCC_except_table4609
+ GCC_except_table4666
+ GCC_except_table4669
+ GCC_except_table475
+ GCC_except_table476
+ GCC_except_table485
+ GCC_except_table4953
+ GCC_except_table4981
+ GCC_except_table5011
+ GCC_except_table502
+ GCC_except_table5030
+ GCC_except_table5044
+ GCC_except_table5048
+ GCC_except_table508
+ GCC_except_table5097
+ GCC_except_table5139
+ GCC_except_table5189
+ GCC_except_table5215
+ GCC_except_table5228
+ GCC_except_table5237
+ GCC_except_table5289
+ GCC_except_table5303
+ GCC_except_table5420
+ GCC_except_table5433
+ GCC_except_table5436
+ GCC_except_table5869
+ GCC_except_table5905
+ GCC_except_table5909
+ GCC_except_table5911
+ GCC_except_table5932
+ GCC_except_table5938
+ GCC_except_table5944
+ GCC_except_table5948
+ GCC_except_table5957
+ GCC_except_table5977
+ GCC_except_table5984
+ GCC_except_table6007
+ GCC_except_table6041
+ GCC_except_table6065
+ GCC_except_table607
+ GCC_except_table6074
+ GCC_except_table6092
+ GCC_except_table6095
+ GCC_except_table6097
+ GCC_except_table6099
+ GCC_except_table613
+ GCC_except_table6131
+ GCC_except_table6201
+ GCC_except_table634
+ GCC_except_table6343
+ GCC_except_table6365
+ GCC_except_table6394
+ GCC_except_table645
+ GCC_except_table6576
+ GCC_except_table6585
+ GCC_except_table6590
+ GCC_except_table660
+ GCC_except_table6604
+ GCC_except_table6628
+ GCC_except_table6633
+ GCC_except_table6713
+ GCC_except_table677
+ GCC_except_table6793
+ GCC_except_table6857
+ GCC_except_table688
+ GCC_except_table6901
+ GCC_except_table6902
+ GCC_except_table6915
+ GCC_except_table702
+ GCC_except_table716
+ GCC_except_table843
+ GCC_except_table861
+ GCC_except_table863
+ _CPLEngineElementUploadComputeStates
+ _CPLMaxComputeStatesToUploadPerBatchConfigurationKey
+ _CPLMetricsDidChangeNotification
+ _OBJC_CLASS_$_CPLEngineRecordComputeStatePushQueue
+ _OBJC_CLASS_$_CPLMetrics
+ _OBJC_CLASS_$_CPLRecordComputeState
+ _OBJC_CLASS_$_CPLRecordComputeStateValidator
+ _OBJC_CLASS_$_CPLRecordComputeStateVersion
+ _OBJC_CLASS_$_CPLUploadComputeStatesScopeTask
+ _OBJC_CLASS_$_CPLUploadComputeStatesTask
+ _OBJC_CLASS_$_NSDistributedNotificationCenter
+ _OBJC_IVAR_$_CPLAssetChange._computeStateAdjustmentFingerprint
+ _OBJC_IVAR_$_CPLAssetChange._computeStateLastUpdatedDate
+ _OBJC_IVAR_$_CPLAssetChange._computeStateVersion
+ _OBJC_IVAR_$_CPLEngineLibrary._metrics
+ _OBJC_IVAR_$_CPLEngineLibrary._metricsObserver
+ _OBJC_IVAR_$_CPLEngineRecordComputeStatePushQueue._fileStorage
+ _OBJC_IVAR_$_CPLEngineRecordComputeStatePushQueue._filesToCommit
+ _OBJC_IVAR_$_CPLEngineRecordComputeStatePushQueue._filesToDelete
+ _OBJC_IVAR_$_CPLEngineRecordComputeStatePushQueue._incomingDownloadFolderCreationDate
+ _OBJC_IVAR_$_CPLEngineRecordComputeStatePushQueue._incomingDownloadFolderURL
+ _OBJC_IVAR_$_CPLEngineRecordComputeStatePushQueue._lastComputeStateDownloadRequestDate
+ _OBJC_IVAR_$_CPLEngineRecordComputeStatePushQueue._lastComputeStateDownloadRequestDateLock
+ _OBJC_IVAR_$_CPLEngineRecordComputeStatePushQueue._tempFolderIndex
+ _OBJC_IVAR_$_CPLEngineRecordComputeStatePushQueue._throttlingDate
+ _OBJC_IVAR_$_CPLEngineStore._recordComputeStatePushQueue
+ _OBJC_IVAR_$_CPLMetrics._lock
+ _OBJC_IVAR_$_CPLMetrics._metrics
+ _OBJC_IVAR_$_CPLMetrics._metricsFileURL
+ _OBJC_IVAR_$_CPLRecordComputeState._adjustmentFingerprint
+ _OBJC_IVAR_$_CPLRecordComputeState._fileStorageIdentifier
+ _OBJC_IVAR_$_CPLRecordComputeState._fileURL
+ _OBJC_IVAR_$_CPLRecordComputeState._itemScopedIdentifier
+ _OBJC_IVAR_$_CPLRecordComputeState._lastUpdatedDate
+ _OBJC_IVAR_$_CPLRecordComputeState._version
+ _OBJC_IVAR_$_CPLRecordComputeStateVersion._majorVersion
+ _OBJC_IVAR_$_CPLRecordComputeStateVersion._stage
+ _OBJC_IVAR_$_CPLUploadComputeStatesScopeTask._cloudComputeStates
+ _OBJC_IVAR_$_CPLUploadComputeStatesScopeTask._countOfComputeStatesPutAside
+ _OBJC_IVAR_$_CPLUploadComputeStatesScopeTask._countOfDroppedComputeStates
+ _OBJC_IVAR_$_CPLUploadComputeStatesScopeTask._didUploadSomeComputeStates
+ _OBJC_IVAR_$_CPLUploadComputeStatesScopeTask._knownRecords
+ _OBJC_IVAR_$_CPLUploadComputeStatesScopeTask._queue
+ _OBJC_IVAR_$_CPLUploadComputeStatesScopeTask._sharedScope
+ _OBJC_IVAR_$_CPLUploadComputeStatesScopeTask._targetMapping
+ _OBJC_IVAR_$_CPLUploadComputeStatesScopeTask._taskItem
+ _OBJC_IVAR_$_CPLUploadComputeStatesScopeTask._transportGroup
+ _OBJC_IVAR_$_CPLUploadComputeStatesScopeTask._transportScopeMapping
+ _OBJC_IVAR_$_CPLUploadComputeStatesScopeTask._uploadComputeStatesTask
+ _OBJC_IVAR_$__CPLEngineSyncLastError._state
+ _OBJC_METACLASS_$_CPLEngineRecordComputeStatePushQueue
+ _OBJC_METACLASS_$_CPLMetrics
+ _OBJC_METACLASS_$_CPLRecordComputeState
+ _OBJC_METACLASS_$_CPLRecordComputeStateValidator
+ _OBJC_METACLASS_$_CPLRecordComputeStateVersion
+ _OBJC_METACLASS_$_CPLUploadComputeStatesScopeTask
+ _OBJC_METACLASS_$_CPLUploadComputeStatesTask
+ _PLCoreAnalyticsLibrarySummaryiCPLComputeSyncDownloadCKErrorCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLComputeSyncDownloadCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLComputeSyncDownloadDecryptionErrorCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLComputeSyncDownloadFailureCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLComputeSyncDownloadThrottledErrorCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLComputeSyncUploadCKErrorCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLComputeSyncUploadCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLComputeSyncUploadEncryptionErrorCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLComputeSyncUploadFailureCountKey
+ _PLCoreAnalyticsLibrarySummaryiCPLComputeSyncUploadThrottledErrorCountKey
+ __OBJC_$_CLASS_METHODS_CPLRecordComputeState
+ __OBJC_$_CLASS_METHODS_CPLRecordComputeStateValidator
+ __OBJC_$_CLASS_PROP_LIST_CPLRecordComputeState
+ __OBJC_$_CLASS_PROP_LIST_CPLRecordComputeStateValidator
+ __OBJC_$_INSTANCE_METHODS_CPLEngineRecordComputeStatePushQueue
+ __OBJC_$_INSTANCE_METHODS_CPLMetrics
+ __OBJC_$_INSTANCE_METHODS_CPLRecordComputeState
+ __OBJC_$_INSTANCE_METHODS_CPLRecordComputeStateValidator
+ __OBJC_$_INSTANCE_METHODS_CPLRecordComputeStateVersion
+ __OBJC_$_INSTANCE_METHODS_CPLUploadComputeStatesScopeTask
+ __OBJC_$_INSTANCE_METHODS_CPLUploadComputeStatesTask
+ __OBJC_$_INSTANCE_VARIABLES_CPLEngineRecordComputeStatePushQueue
+ __OBJC_$_INSTANCE_VARIABLES_CPLMetrics
+ __OBJC_$_INSTANCE_VARIABLES_CPLRecordComputeState
+ __OBJC_$_INSTANCE_VARIABLES_CPLRecordComputeStateVersion
+ __OBJC_$_INSTANCE_VARIABLES_CPLUploadComputeStatesScopeTask
+ __OBJC_$_PROP_LIST_CPLEngineRecordComputeStatePushQueue
+ __OBJC_$_PROP_LIST_CPLRecordComputeState
+ __OBJC_$_PROP_LIST_CPLRecordComputeStateVersion
+ __OBJC_CLASS_PROTOCOLS_$_CPLEngineRecordComputeStatePushQueue
+ __OBJC_CLASS_PROTOCOLS_$_CPLRecordComputeState
+ __OBJC_CLASS_PROTOCOLS_$_CPLRecordComputeStateValidator
+ __OBJC_CLASS_RO_$_CPLEngineRecordComputeStatePushQueue
+ __OBJC_CLASS_RO_$_CPLMetrics
+ __OBJC_CLASS_RO_$_CPLRecordComputeState
+ __OBJC_CLASS_RO_$_CPLRecordComputeStateValidator
+ __OBJC_CLASS_RO_$_CPLRecordComputeStateVersion
+ __OBJC_CLASS_RO_$_CPLUploadComputeStatesScopeTask
+ __OBJC_CLASS_RO_$_CPLUploadComputeStatesTask
+ __OBJC_METACLASS_RO_$_CPLEngineRecordComputeStatePushQueue
+ __OBJC_METACLASS_RO_$_CPLMetrics
+ __OBJC_METACLASS_RO_$_CPLRecordComputeState
+ __OBJC_METACLASS_RO_$_CPLRecordComputeStateValidator
+ __OBJC_METACLASS_RO_$_CPLRecordComputeStateVersion
+ __OBJC_METACLASS_RO_$_CPLUploadComputeStatesScopeTask
+ __OBJC_METACLASS_RO_$_CPLUploadComputeStatesTask
+ ___115-[CPLProxyLibraryManager beginDownloadForResource:clientBundleID:options:proposedTaskIdentifier:completionHandler:]_block_invoke.318
+ ___122-[CPLLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke
+ ___122-[CPLLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke.445
+ ___122-[CPLLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke_2
+ ___127-[CPLProxyLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke
+ ___127-[CPLProxyLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke.366
+ ___127-[CPLProxyLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke_2
+ ___127-[CPLProxyLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke_2.367
+ ___127-[CPLProxyLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke_3
+ ___23-[CPLMetrics forceLoad]_block_invoke
+ ___26-[CPLMetrics countForKey:]_block_invoke
+ ___26-[CPLMetrics resetMetrics]_block_invoke
+ ___32-[CPLMetrics metricsDescription]_block_invoke
+ ___33-[CPLStatus isKeychainCDPEnabled]_block_invoke
+ ___35-[CPLMetrics incrementCountForKey:]_block_invoke
+ ___35-[CPLStatus setKeychainCDPEnabled:]_block_invoke
+ ___36-[CPLEngineLibrary startSyncSession]_block_invoke.39
+ ___36-[CPLEngineLibrary startSyncSession]_block_invoke.40
+ ___38-[CPLPushToTransportScopeTask _launch]_block_invoke.88
+ ___38-[CPLPushToTransportScopeTask _launch]_block_invoke_2.90
+ ___41-[CPLEngineScheduler noteQuotaHasChanged]_block_invoke.130
+ ___41-[CPLUploadComputeStatesScopeTask cancel]_block_invoke
+ ___41-[CPLUploadComputeStatesScopeTask launch]_block_invoke
+ ___42-[CPLEngineLibrary forceFetchAccountFlags]_block_invoke.41
+ ___42-[CPLEngineLibrary forceFetchAccountFlags]_block_invoke.42
+ ___42-[CPLEngineLibrary performBlockOnLibrary:]_block_invoke.78
+ ___42-[CPLEngineLibrary performBlockOnLibrary:]_block_invoke.79
+ ___42-[CPLEngineScheduler _prepareFirstSession]_block_invoke.140
+ ___42-[CPLEngineScheduler _prepareFirstSession]_block_invoke.141
+ ___42-[CPLEngineScheduler _prepareFirstSession]_block_invoke_2.142
+ ___42-[CPLProxyLibraryManager _setupConnection]_block_invoke.265
+ ___42-[CPLProxyLibraryManager _setupConnection]_block_invoke.271
+ ___42-[CPLProxyLibraryManager _setupConnection]_block_invoke.272
+ ___42-[CPLProxyLibraryManager _setupConnection]_block_invoke.273
+ ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.243
+ ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.270
+ ___46-[CPLEngineLibrary openWithCompletionHandler:]_block_invoke_2
+ ___46-[CPLEngineLibrary openWithCompletionHandler:]_block_invoke_3
+ ___46-[CPLEngineRecordComputeStatePushQueue status]_block_invoke
+ ___49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.284
+ ___49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.285
+ ___49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.286
+ ___49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.289
+ ___50+[CPLArchiver displayableDictionaryForDictionary:]_block_invoke.1619
+ ___51-[CPLEngineStore _reallySchedulePendingUpdateApply]_block_invoke.325
+ ___51-[CPLPushToTransportScopeTask _updateContributors:]_block_invoke.66
+ ___52-[CPLEngineSyncManager resetTransportUserIdentifier]_block_invoke.226
+ ___52-[CPLEngineSyncManager resetTransportUserIdentifier]_block_invoke_2.229
+ ___52-[CPLProxyLibraryManager openWithCompletionHandler:]_block_invoke.297
+ ___52-[CPLProxyLibraryManager openWithCompletionHandler:]_block_invoke.299
+ ___52-[CPLProxyLibraryManager openWithCompletionHandler:]_block_invoke.300
+ ___53-[CPLProxyLibraryManager closeWithCompletionHandler:]_block_invoke.301
+ ___54-[CPLEngineRecordComputeStatePushQueue openWithError:]_block_invoke
+ ___54-[CPLEngineRecordComputeStatePushQueue openWithError:]_block_invoke_2
+ ___55-[CPLEngineLibrary attachObject:withCompletionHandler:]_block_invoke.67
+ ___55-[CPLEngineStore closeAndDeactivate:completionHandler:]_block_invoke.315
+ ___55-[CPLEngineSyncManager _launchForceSyncTaskIfNecessary]_block_invoke.265
+ ___56-[CPLEngineScheduler noteScopeNeedsToUploadComputeState]_block_invoke
+ ___56-[CPLEngineSyncManager _setupTaskWithCompletionHandler:]_block_invoke.279
+ ___56-[CPLEngineSyncManager _setupTaskWithCompletionHandler:]_block_invoke_2.281
+ ___56-[CPLUploadComputeStatesScopeTask _dropAllComputeStates]_block_invoke
+ ___56-[CPLUploadComputeStatesScopeTask _dropAllComputeStates]_block_invoke.30
+ ___56-[CPLUploadComputeStatesScopeTask _dropAllComputeStates]_block_invoke_2
+ ___56-[CPLUploadComputeStatesScopeTask _uploadExtractedBatch]_block_invoke
+ ___56-[CPLUploadComputeStatesScopeTask _uploadExtractedBatch]_block_invoke_2
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.107
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.115
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.121
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.127
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.133
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.139
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.146
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.151
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.157
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.163
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.169
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.175
+ ___57-[CPLEngineSyncManager setSyncSessionShouldBeForeground:]_block_invoke.237
+ ___57-[CPLUploadComputeStatesScopeTask _getNextBatchAndUpload]_block_invoke
+ ___57-[CPLUploadComputeStatesScopeTask _getNextBatchAndUpload]_block_invoke.20
+ ___57-[CPLUploadComputeStatesScopeTask _getNextBatchAndUpload]_block_invoke.22
+ ___57-[CPLUploadComputeStatesScopeTask _getNextBatchAndUpload]_block_invoke.27
+ ___57-[CPLUploadComputeStatesScopeTask _getNextBatchAndUpload]_block_invoke_2
+ ___57-[CPLUploadComputeStatesScopeTask _getNextBatchAndUpload]_block_invoke_3
+ ___57-[CPLUploadComputeStatesScopeTask _getNextBatchAndUpload]_block_invoke_4
+ ___58-[CPLEngineFileStorage openWithFileRecoveryHandler:error:]_block_invoke
+ ___58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke.302
+ ___58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke.304
+ ___58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke.306
+ ___58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke_2.303
+ ___58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke_2.305
+ ___58-[CPLProxyLibraryManager noteClientIsInForegroundQuietly:]_block_invoke.336
+ ___59-[CPLEngineLibrary provideCloudResource:completionHandler:]_block_invoke.86
+ ___59-[CPLEngineLibrary provideCloudResource:completionHandler:]_block_invoke.87
+ ___59-[CPLLibraryManager attachComputeStates:completionHandler:]_block_invoke
+ ___59-[CPLProxyLibraryManager forceBackupWithCompletionHandler:]_block_invoke_5
+ ___59-[CPLPushToTransportScopeTask _pushTaskDidFinishWithError:]_block_invoke.102
+ ___59-[CPLPushToTransportScopeTask _pushTaskDidFinishWithError:]_block_invoke_2.103
+ ___62-[CPLEngineRecordComputeStatePushQueue addComputeState:error:]_block_invoke
+ ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke.115
+ ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke.117
+ ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke_2.118
+ ___63-[CPLEngineRecordComputeStatePushQueue writeTransactionDidFail]_block_invoke
+ ___63-[CPLEngineRecordComputeStatePushQueue writeTransactionDidFail]_block_invoke_2
+ ___64-[CPLProxyLibraryManager attachComputeStates:completionHandler:]_block_invoke
+ ___64-[CPLProxyLibraryManager attachComputeStates:completionHandler:]_block_invoke_2
+ ___64-[CPLProxyLibraryManager attachComputeStates:completionHandler:]_block_invoke_3
+ ___66-[CPLEngineRecordComputeStatePushQueue writeTransactionDidSucceed]_block_invoke
+ ___66-[CPLEngineRecordComputeStatePushQueue writeTransactionDidSucceed]_block_invoke_2
+ ___66-[CPLEngineRecordComputeStatePushQueue writeTransactionDidSucceed]_block_invoke_3
+ ___66-[CPLEngineScheduler noteSyncSession:failedDuringPhase:withError:]_block_invoke.116
+ ___66-[CPLEngineScheduler noteSyncSession:failedDuringPhase:withError:]_block_invoke.117
+ ___66-[CPLEngineScheduler noteSyncSession:failedDuringPhase:withError:]_block_invoke.118
+ ___67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke.125
+ ___67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke.127
+ ___67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke_2.126
+ ___68-[CPLEngineScheduler _handleResetAnchorWithError:completionHandler:]_block_invoke.111
+ ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.101
+ ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.103
+ ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.105
+ ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.109
+ ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_2.104
+ ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_2.106
+ ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_2.110
+ ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_3.107
+ ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_4.108
+ ___71-[CPLEngineRecordComputeStatePushQueue noteComputeStateDownloadRequest]_block_invoke
+ ___72-[CPLUploadComputeStatesScopeTask _discardExtractedBatchAndGetNextBatch]_block_invoke
+ ___72-[CPLUploadComputeStatesScopeTask _discardExtractedBatchAndGetNextBatch]_block_invoke_2
+ ___72-[CPLUploadComputeStatesScopeTask _discardExtractedBatchAndGetNextBatch]_block_invoke_3
+ ___72-[CPLUploadComputeStatesScopeTask _discardExtractedBatchAndGetNextBatch]_block_invoke_4
+ ___74-[CPLEngineScheduler _handleResetGlobalAnchorWithError:completionHandler:]_block_invoke.115
+ ___75-[CPLEngineRecordComputeStatePushQueue retainFileURLForComputeState:error:]_block_invoke
+ ___76-[CPLEngineLibrary provideRecordWithCloudScopeIdentifier:completionHandler:]_block_invoke.85
+ ___76-[CPLProxyLibraryManager beginInMemoryDownloadOfResource:completionHandler:]_block_invoke.326
+ ___77-[CPLEngineRecordComputeStatePushQueue releaseFileURL:forComputeState:error:]_block_invoke
+ ___77-[CPLProxyLibraryManager requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_5
+ ___78-[CPLEngineLibrary forceBackupWithActivity:forceClientPush:completionHandler:]_block_invoke.114
+ ___78-[CPLEngineLibrary forceBackupWithActivity:forceClientPush:completionHandler:]_block_invoke.121
+ ___78-[CPLEngineLibrary forceBackupWithActivity:forceClientPush:completionHandler:]_block_invoke_2.118
+ ___78-[CPLUploadComputeStatesScopeTask _uploadComputeStatesTaskDidFinishWithError:]_block_invoke
+ ___78-[CPLUploadComputeStatesScopeTask _uploadComputeStatesTaskDidFinishWithError:]_block_invoke_2
+ ___78-[CPLUploadComputeStatesScopeTask _uploadComputeStatesTaskDidFinishWithError:]_block_invoke_3
+ ___78-[CPLUploadComputeStatesScopeTask _uploadComputeStatesTaskDidFinishWithError:]_block_invoke_4
+ ___79-[CPLEngineLibrary provideScopeChangeForScopeWithIdentifier:completionHandler:]_block_invoke.84
+ ___83-[CPLProxyLibraryManager forceSynchronizingScopeWithIdentifiers:completionHandler:]_block_invoke.345
+ ___84-[CPLEngineStore _performWriteTransactionByPassBlocker:WithBlock:completionHandler:]_block_invoke.288
+ ___Block_byref_object_copy_.10124
+ ___Block_byref_object_copy_.10762
+ ___Block_byref_object_copy_.1113
+ ___Block_byref_object_copy_.11605
+ ___Block_byref_object_copy_.12160
+ ___Block_byref_object_copy_.12462
+ ___Block_byref_object_copy_.1249
+ ___Block_byref_object_copy_.12584
+ ___Block_byref_object_copy_.13367
+ ___Block_byref_object_copy_.13953
+ ___Block_byref_object_copy_.14707
+ ___Block_byref_object_copy_.14975
+ ___Block_byref_object_copy_.15367
+ ___Block_byref_object_copy_.15990
+ ___Block_byref_object_copy_.16785
+ ___Block_byref_object_copy_.1717
+ ___Block_byref_object_copy_.18023
+ ___Block_byref_object_copy_.18159
+ ___Block_byref_object_copy_.18662
+ ___Block_byref_object_copy_.19269
+ ___Block_byref_object_copy_.19730
+ ___Block_byref_object_copy_.20065
+ ___Block_byref_object_copy_.21083
+ ___Block_byref_object_copy_.21382
+ ___Block_byref_object_copy_.2179
+ ___Block_byref_object_copy_.22124
+ ___Block_byref_object_copy_.2253
+ ___Block_byref_object_copy_.2732
+ ___Block_byref_object_copy_.309
+ ___Block_byref_object_copy_.4929
+ ___Block_byref_object_copy_.5595
+ ___Block_byref_object_copy_.5753
+ ___Block_byref_object_copy_.6238
+ ___Block_byref_object_copy_.638
+ ___Block_byref_object_copy_.6602
+ ___Block_byref_object_copy_.6857
+ ___Block_byref_object_copy_.7253
+ ___Block_byref_object_copy_.839
+ ___Block_byref_object_copy_.8558
+ ___Block_byref_object_copy_.8824
+ ___Block_byref_object_copy_.963
+ ___Block_byref_object_copy_.9831
+ ___Block_byref_object_dispose_.10125
+ ___Block_byref_object_dispose_.10763
+ ___Block_byref_object_dispose_.1114
+ ___Block_byref_object_dispose_.11606
+ ___Block_byref_object_dispose_.12161
+ ___Block_byref_object_dispose_.12463
+ ___Block_byref_object_dispose_.1250
+ ___Block_byref_object_dispose_.12585
+ ___Block_byref_object_dispose_.13368
+ ___Block_byref_object_dispose_.13954
+ ___Block_byref_object_dispose_.14708
+ ___Block_byref_object_dispose_.14976
+ ___Block_byref_object_dispose_.15368
+ ___Block_byref_object_dispose_.15991
+ ___Block_byref_object_dispose_.16786
+ ___Block_byref_object_dispose_.1718
+ ___Block_byref_object_dispose_.18024
+ ___Block_byref_object_dispose_.18160
+ ___Block_byref_object_dispose_.18663
+ ___Block_byref_object_dispose_.19270
+ ___Block_byref_object_dispose_.19731
+ ___Block_byref_object_dispose_.20066
+ ___Block_byref_object_dispose_.21084
+ ___Block_byref_object_dispose_.21383
+ ___Block_byref_object_dispose_.2180
+ ___Block_byref_object_dispose_.22125
+ ___Block_byref_object_dispose_.2254
+ ___Block_byref_object_dispose_.2733
+ ___Block_byref_object_dispose_.310
+ ___Block_byref_object_dispose_.4930
+ ___Block_byref_object_dispose_.5596
+ ___Block_byref_object_dispose_.5754
+ ___Block_byref_object_dispose_.6239
+ ___Block_byref_object_dispose_.639
+ ___Block_byref_object_dispose_.6603
+ ___Block_byref_object_dispose_.6858
+ ___Block_byref_object_dispose_.7254
+ ___Block_byref_object_dispose_.840
+ ___Block_byref_object_dispose_.8559
+ ___Block_byref_object_dispose_.8825
+ ___Block_byref_object_dispose_.964
+ ___Block_byref_object_dispose_.9832
+ ___CPLForceSyncOSLogDomain.18793
+ ___CPLForceSyncOSLogDomain.onceToken.18802
+ ___CPLForceSyncOSLogDomain.result.18803
+ ___CPLSchedulerOSLogDomain.6548
+ ___CPLSchedulerOSLogDomain.onceToken.6549
+ ___CPLSchedulerOSLogDomain.result.6550
+ ___CPLSessionOSLogDomain.14580
+ ___CPLSessionOSLogDomain.16364
+ ___CPLSessionOSLogDomain.20667
+ ___CPLSessionOSLogDomain.onceToken.14630
+ ___CPLSessionOSLogDomain.onceToken.16369
+ ___CPLSessionOSLogDomain.onceToken.20669
+ ___CPLSessionOSLogDomain.result.14631
+ ___CPLSessionOSLogDomain.result.16370
+ ___CPLSessionOSLogDomain.result.20671
+ ___CPLStorageOSLogDomain.15958
+ ___CPLStorageOSLogDomain.1697
+ ___CPLStorageOSLogDomain.18138
+ ___CPLStorageOSLogDomain.189
+ ___CPLStorageOSLogDomain.19410
+ ___CPLStorageOSLogDomain.20052
+ ___CPLStorageOSLogDomain.20300
+ ___CPLStorageOSLogDomain.466
+ ___CPLStorageOSLogDomain.5370
+ ___CPLStorageOSLogDomain.6815
+ ___CPLStorageOSLogDomain.7506
+ ___CPLStorageOSLogDomain.7912
+ ___CPLStorageOSLogDomain.8035
+ ___CPLStorageOSLogDomain.8217
+ ___CPLStorageOSLogDomain.858
+ ___CPLStorageOSLogDomain.9799
+ ___CPLStorageOSLogDomain.9884
+ ___CPLStorageOSLogDomain.onceToken.12918
+ ___CPLStorageOSLogDomain.onceToken.15960
+ ___CPLStorageOSLogDomain.onceToken.1699
+ ___CPLStorageOSLogDomain.onceToken.18140
+ ___CPLStorageOSLogDomain.onceToken.18408
+ ___CPLStorageOSLogDomain.onceToken.191
+ ___CPLStorageOSLogDomain.onceToken.19414
+ ___CPLStorageOSLogDomain.onceToken.20057
+ ___CPLStorageOSLogDomain.onceToken.20308
+ ___CPLStorageOSLogDomain.onceToken.468
+ ___CPLStorageOSLogDomain.onceToken.5372
+ ___CPLStorageOSLogDomain.onceToken.6817
+ ___CPLStorageOSLogDomain.onceToken.7511
+ ___CPLStorageOSLogDomain.onceToken.7918
+ ___CPLStorageOSLogDomain.onceToken.8037
+ ___CPLStorageOSLogDomain.onceToken.8219
+ ___CPLStorageOSLogDomain.onceToken.867
+ ___CPLStorageOSLogDomain.onceToken.9810
+ ___CPLStorageOSLogDomain.onceToken.9887
+ ___CPLStorageOSLogDomain.result.12920
+ ___CPLStorageOSLogDomain.result.15962
+ ___CPLStorageOSLogDomain.result.1701
+ ___CPLStorageOSLogDomain.result.18142
+ ___CPLStorageOSLogDomain.result.18410
+ ___CPLStorageOSLogDomain.result.193
+ ___CPLStorageOSLogDomain.result.19416
+ ___CPLStorageOSLogDomain.result.20059
+ ___CPLStorageOSLogDomain.result.20310
+ ___CPLStorageOSLogDomain.result.470
+ ___CPLStorageOSLogDomain.result.5374
+ ___CPLStorageOSLogDomain.result.6818
+ ___CPLStorageOSLogDomain.result.7512
+ ___CPLStorageOSLogDomain.result.7920
+ ___CPLStorageOSLogDomain.result.8039
+ ___CPLStorageOSLogDomain.result.8220
+ ___CPLStorageOSLogDomain.result.869
+ ___CPLStorageOSLogDomain.result.9812
+ ___CPLStorageOSLogDomain.result.9889
+ ___CPLStoreOSLogDomain.2526
+ ___CPLStoreOSLogDomain.onceToken.2527
+ ___CPLStoreOSLogDomain.result.2528
+ ___CPLTaskOSLogDomain.10071
+ ___CPLTaskOSLogDomain.12446
+ ___CPLTaskOSLogDomain.1247
+ ___CPLTaskOSLogDomain.12828
+ ___CPLTaskOSLogDomain.13850
+ ___CPLTaskOSLogDomain.15339
+ ___CPLTaskOSLogDomain.19216
+ ___CPLTaskOSLogDomain.21006
+ ___CPLTaskOSLogDomain.22075
+ ___CPLTaskOSLogDomain.2240
+ ___CPLTaskOSLogDomain.4661
+ ___CPLTaskOSLogDomain.582
+ ___CPLTaskOSLogDomain.6161
+ ___CPLTaskOSLogDomain.onceToken.10106
+ ___CPLTaskOSLogDomain.onceToken.12453
+ ___CPLTaskOSLogDomain.onceToken.1262
+ ___CPLTaskOSLogDomain.onceToken.12830
+ ___CPLTaskOSLogDomain.onceToken.13859
+ ___CPLTaskOSLogDomain.onceToken.15342
+ ___CPLTaskOSLogDomain.onceToken.19258
+ ___CPLTaskOSLogDomain.onceToken.21015
+ ___CPLTaskOSLogDomain.onceToken.22083
+ ___CPLTaskOSLogDomain.onceToken.2242
+ ___CPLTaskOSLogDomain.onceToken.4664
+ ___CPLTaskOSLogDomain.onceToken.585
+ ___CPLTaskOSLogDomain.onceToken.6173
+ ___CPLTaskOSLogDomain.result.10108
+ ___CPLTaskOSLogDomain.result.12455
+ ___CPLTaskOSLogDomain.result.1264
+ ___CPLTaskOSLogDomain.result.12832
+ ___CPLTaskOSLogDomain.result.13861
+ ___CPLTaskOSLogDomain.result.15343
+ ___CPLTaskOSLogDomain.result.19259
+ ___CPLTaskOSLogDomain.result.21016
+ ___CPLTaskOSLogDomain.result.22084
+ ___CPLTaskOSLogDomain.result.2244
+ ___CPLTaskOSLogDomain.result.4666
+ ___CPLTaskOSLogDomain.result.587
+ ___CPLTaskOSLogDomain.result.6175
+ _____CPLForceSyncOSLogDomain_block_invoke.18805
+ _____CPLSchedulerOSLogDomain_block_invoke.6552
+ _____CPLSessionOSLogDomain_block_invoke.14633
+ _____CPLSessionOSLogDomain_block_invoke.16372
+ _____CPLSessionOSLogDomain_block_invoke.20674
+ _____CPLStorageOSLogDomain_block_invoke.12925
+ _____CPLStorageOSLogDomain_block_invoke.15965
+ _____CPLStorageOSLogDomain_block_invoke.1704
+ _____CPLStorageOSLogDomain_block_invoke.18145
+ _____CPLStorageOSLogDomain_block_invoke.18417
+ _____CPLStorageOSLogDomain_block_invoke.19419
+ _____CPLStorageOSLogDomain_block_invoke.196
+ _____CPLStorageOSLogDomain_block_invoke.20062
+ _____CPLStorageOSLogDomain_block_invoke.20313
+ _____CPLStorageOSLogDomain_block_invoke.473
+ _____CPLStorageOSLogDomain_block_invoke.5377
+ _____CPLStorageOSLogDomain_block_invoke.6820
+ _____CPLStorageOSLogDomain_block_invoke.7514
+ _____CPLStorageOSLogDomain_block_invoke.7923
+ _____CPLStorageOSLogDomain_block_invoke.8042
+ _____CPLStorageOSLogDomain_block_invoke.8222
+ _____CPLStorageOSLogDomain_block_invoke.872
+ _____CPLStorageOSLogDomain_block_invoke.9815
+ _____CPLStorageOSLogDomain_block_invoke.9892
+ _____CPLStoreOSLogDomain_block_invoke.2530
+ _____CPLTaskOSLogDomain_block_invoke.10111
+ _____CPLTaskOSLogDomain_block_invoke.12458
+ _____CPLTaskOSLogDomain_block_invoke.1267
+ _____CPLTaskOSLogDomain_block_invoke.12835
+ _____CPLTaskOSLogDomain_block_invoke.13864
+ _____CPLTaskOSLogDomain_block_invoke.15345
+ _____CPLTaskOSLogDomain_block_invoke.19261
+ _____CPLTaskOSLogDomain_block_invoke.21018
+ _____CPLTaskOSLogDomain_block_invoke.22086
+ _____CPLTaskOSLogDomain_block_invoke.2247
+ _____CPLTaskOSLogDomain_block_invoke.4669
+ _____CPLTaskOSLogDomain_block_invoke.590
+ _____CPLTaskOSLogDomain_block_invoke.6178
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104s_e9_B16?0^8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_136_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s72l8s64l8
+ ___block_descriptor_40_e8_32bs_e29_B16?0"CPLResourceIdentity"8ls32l8
+ ___block_descriptor_40_e8_32s_e18_B16?0"NSString"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e23_v28?0B8Q12"NSError"20ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e36_v24?0"CPLScopeChange"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e37_v24?0"NSXPCConnection"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e62_v48?0"NSURL"8"NSData"16"NSDate"24"NSString"32"NSError"40ls40l8s32l8
+ ___block_descriptor_48_e8_32s_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32s40bs_e37_v24?0"NSXPCConnection"8"NSError"16ls40l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e25_v32?0"NSString"8Q16^B24lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40s48bs_e36_v24?0"CPLScopeChange"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_descriptor_74_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s64l8s56l8
+ ___block_descriptor_74_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e9_B16?0^8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_82_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
+ ___block_literal_global.1002
+ ___block_literal_global.1003
+ ___block_literal_global.1006
+ ___block_literal_global.10107
+ ___block_literal_global.102.17128
+ ___block_literal_global.106
+ ___block_literal_global.10908
+ ___block_literal_global.11
+ ___block_literal_global.110
+ ___block_literal_global.11148
+ ___block_literal_global.1118
+ ___block_literal_global.11626
+ ___block_literal_global.12.6929
+ ___block_literal_global.120.6568
+ ___block_literal_global.123
+ ___block_literal_global.12454
+ ___block_literal_global.1263
+ ___block_literal_global.12630
+ ___block_literal_global.12865
+ ___block_literal_global.129
+ ___block_literal_global.12919
+ ___block_literal_global.13090
+ ___block_literal_global.135
+ ___block_literal_global.13582
+ ___block_literal_global.13600
+ ___block_literal_global.13660
+ ___block_literal_global.13860
+ ___block_literal_global.14.12866
+ ___block_literal_global.14.4606
+ ___block_literal_global.140
+ ___block_literal_global.142.18958
+ ___block_literal_global.143.18409
+ ___block_literal_global.144
+ ___block_literal_global.14443
+ ___block_literal_global.14650
+ ___block_literal_global.148
+ ___block_literal_global.15131
+ ___block_literal_global.1529
+ ___block_literal_global.153
+ ___block_literal_global.15392
+ ___block_literal_global.1564
+ ___block_literal_global.15756
+ ___block_literal_global.159
+ ___block_literal_global.15961
+ ___block_literal_global.1603
+ ___block_literal_global.1630
+ ___block_literal_global.1632
+ ___block_literal_global.1634
+ ___block_literal_global.16382
+ ___block_literal_global.165
+ ___block_literal_global.1655
+ ___block_literal_global.16555
+ ___block_literal_global.1657
+ ___block_literal_global.1659
+ ___block_literal_global.1665
+ ___block_literal_global.1667
+ ___block_literal_global.16675
+ ___block_literal_global.1669
+ ___block_literal_global.1689
+ ___block_literal_global.1697
+ ___block_literal_global.1699
+ ___block_literal_global.1700
+ ___block_literal_global.1704
+ ___block_literal_global.1706
+ ___block_literal_global.171.18959
+ ___block_literal_global.17238
+ ___block_literal_global.177.18960
+ ___block_literal_global.17802
+ ___block_literal_global.18141
+ ___block_literal_global.18294
+ ___block_literal_global.18412
+ ___block_literal_global.1854
+ ___block_literal_global.1860
+ ___block_literal_global.18953
+ ___block_literal_global.192
+ ___block_literal_global.19276
+ ___block_literal_global.19415
+ ___block_literal_global.1956
+ ___block_literal_global.19586
+ ___block_literal_global.2.22340
+ ___block_literal_global.20058
+ ___block_literal_global.20309
+ ___block_literal_global.20469
+ ___block_literal_global.20670
+ ___block_literal_global.20822
+ ___block_literal_global.21079
+ ___block_literal_global.2129
+ ___block_literal_global.21633
+ ___block_literal_global.21769
+ ___block_literal_global.2178
+ ___block_literal_global.21837
+ ___block_literal_global.22.6932
+ ___block_literal_global.22223
+ ___block_literal_global.22334
+ ___block_literal_global.2243
+ ___block_literal_global.22430
+ ___block_literal_global.22616
+ ___block_literal_global.243
+ ___block_literal_global.2505
+ ___block_literal_global.27.14670
+ ___block_literal_global.274
+ ___block_literal_global.2749
+ ___block_literal_global.276
+ ___block_literal_global.278
+ ___block_literal_global.280
+ ___block_literal_global.288
+ ___block_literal_global.291
+ ___block_literal_global.299
+ ___block_literal_global.2990
+ ___block_literal_global.3176
+ ___block_literal_global.32.20437
+ ___block_literal_global.327
+ ___block_literal_global.33.6288
+ ___block_literal_global.332
+ ___block_literal_global.334
+ ___block_literal_global.3379
+ ___block_literal_global.37.6936
+ ___block_literal_global.3807
+ ___block_literal_global.3933
+ ___block_literal_global.4087
+ ___block_literal_global.414
+ ___block_literal_global.43
+ ___block_literal_global.4490
+ ___block_literal_global.4571
+ ___block_literal_global.4665
+ ___block_literal_global.469
+ ___block_literal_global.47.6939
+ ___block_literal_global.4811
+ ___block_literal_global.4926
+ ___block_literal_global.509
+ ___block_literal_global.512
+ ___block_literal_global.526
+ ___block_literal_global.529
+ ___block_literal_global.5373
+ ___block_literal_global.538
+ ___block_literal_global.541
+ ___block_literal_global.5570
+ ___block_literal_global.586
+ ___block_literal_global.604
+ ___block_literal_global.607
+ ___block_literal_global.613
+ ___block_literal_global.616
+ ___block_literal_global.6174
+ ___block_literal_global.6287
+ ___block_literal_global.651
+ ___block_literal_global.654
+ ___block_literal_global.657
+ ___block_literal_global.6665
+ ___block_literal_global.6926
+ ___block_literal_global.701
+ ___block_literal_global.76.15076
+ ___block_literal_global.7603
+ ___block_literal_global.777
+ ___block_literal_global.7813
+ ___block_literal_global.7919
+ ___block_literal_global.8
+ ___block_literal_global.8038
+ ___block_literal_global.8265
+ ___block_literal_global.8448
+ ___block_literal_global.85
+ ___block_literal_global.868
+ ___block_literal_global.8684
+ ___block_literal_global.8839
+ ___block_literal_global.89.12831
+ ___block_literal_global.9107
+ ___block_literal_global.93.17132
+ ___block_literal_global.9399
+ ___block_literal_global.9657
+ ___block_literal_global.9811
+ ___block_literal_global.9888
+ ___cpl_dispatch_async_block_invoke.10067
+ ___cpl_dispatch_async_block_invoke.10572
+ ___cpl_dispatch_async_block_invoke.12442
+ ___cpl_dispatch_async_block_invoke.1269
+ ___cpl_dispatch_async_block_invoke.12751
+ ___cpl_dispatch_async_block_invoke.12824
+ ___cpl_dispatch_async_block_invoke.13940
+ ___cpl_dispatch_async_block_invoke.1488
+ ___cpl_dispatch_async_block_invoke.14957
+ ___cpl_dispatch_async_block_invoke.15335
+ ___cpl_dispatch_async_block_invoke.15710
+ ___cpl_dispatch_async_block_invoke.16189
+ ___cpl_dispatch_async_block_invoke.16671
+ ___cpl_dispatch_async_block_invoke.18648
+ ___cpl_dispatch_async_block_invoke.19214
+ ___cpl_dispatch_async_block_invoke.19593
+ ___cpl_dispatch_async_block_invoke.20824
+ ___cpl_dispatch_async_block_invoke.21022
+ ___cpl_dispatch_async_block_invoke.22132
+ ___cpl_dispatch_async_block_invoke.5786
+ ___cpl_dispatch_async_block_invoke.6159
+ ___cpl_dispatch_async_block_invoke.6422
+ ___cpl_dispatch_async_block_invoke.644
+ ___cpl_dispatch_async_block_invoke.6828
+ ___cpl_dispatch_async_block_invoke.8555
+ ___cpl_dispatch_async_block_invoke.8822
+ __doProtected:.onceToken.13599
+ __doProtected:.onceToken.20821
+ __doProtected:.queue.20823
+ __statusDidChange.10783
+ __unnamed_array_storage.10861
+ __unnamed_array_storage.11999
+ __unnamed_array_storage.1518
+ __unnamed_array_storage.1600
+ __unnamed_array_storage.19695
+ __unnamed_array_storage.4810
+ __unnamed_array_storage.4937
+ _copyDerivativesFromRecordIfPossible:.originalDerivativesImageAndVideo.17150
+ _initWithCPLArchiver:.onceToken.1857
+ _initWithCPLArchiver:.stringClass.1858
+ _initWithCoder:.logOnceToken.18296
+ _initWithCoder:.onceToken.12629
+ _initWithCoder:.onceToken.16381
+ _initWithCoder:.onceToken.18293
+ _initWithCoder:.onceToken.20468
+ _initWithCoder:.onceToken.22615
+ _initWithCoder:.onceToken.4469
+ _initWithCoder:.onceToken.4570
+ _initWithCoder:.onceToken.5565
+ _initWithCoder:.onceToken.9398
+ _initWithCoder:.pushContextsClasses.20470
+ _initWithCoder:.stringClass.9400
+ _objc_msgSend$_discardExtractedBatchAndGetNextBatch
+ _objc_msgSend$_dropAllComputeStates
+ _objc_msgSend$_getNextBatchAndUpload
+ _objc_msgSend$_identityForIdentifier:
+ _objc_msgSend$_updateComputeSyncUploadMetricsWithError:
+ _objc_msgSend$_uploadComputeStatesTaskDidFinishWithError:
+ _objc_msgSend$_uploadExtractedBatch
+ _objc_msgSend$addComputeState:discardedFileStorageIdentifier:error:
+ _objc_msgSend$adjustmentFingerprint
+ _objc_msgSend$attachComputeStates:completionHandler:
+ _objc_msgSend$commitFileWithIdentifier:error:
+ _objc_msgSend$computeStatesToUploadWithScopeIdentifier:localState:maximumCount:
+ _objc_msgSend$countForKey:
+ _objc_msgSend$countOfComputeStates
+ _objc_msgSend$cplIsFileExistsError:
+ _objc_msgSend$createGroupForComputeStateDownloadOnDemand
+ _objc_msgSend$createGroupForComputeStateDownloadPrefetch
+ _objc_msgSend$createGroupForComputeStateUpload
+ _objc_msgSend$createIncomingDownloadFolderIfNecessaryWithError:
+ _objc_msgSend$deleteFileWithIdentifier:error:
+ _objc_msgSend$deleteIncomingDownloadFolderWithError:
+ _objc_msgSend$deleteRecordsForScopeIndex:discardedFileStorageIdentifiers:maxCount:deletedCount:error:
+ _objc_msgSend$dictionaryForKey:
+ _objc_msgSend$discardUncommittedFileWithIdentifier:error:
+ _objc_msgSend$doesScopeNeedToUploadComputeState:
+ _objc_msgSend$downloadComputeStatesWithScopedIdentifiers:scope:sharedScope:targetStorageURL:transportScopeMapping:completionHandler:
+ _objc_msgSend$enumeratorForScopesNeedingToUploadComputeState
+ _objc_msgSend$fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:
+ _objc_msgSend$fileSizeForComputeStatePayloadFileURL:error:
+ _objc_msgSend$fileStorageIdentifier
+ _objc_msgSend$forceLoad
+ _objc_msgSend$hasScopesNeedingToUploadComputeState
+ _objc_msgSend$hasSomeComputeStateWithFileStorageIdentifier:
+ _objc_msgSend$initWithItemScopedIdentifier:fileStorageIdentifier:version:fileURL:adjustmentFingerprint:lastUpdatedDate:
+ _objc_msgSend$initWithItemScopedIdentifier:version:fileURL:adjustmentFingerprint:lastUpdatedDate:
+ _objc_msgSend$initWithMajorVersion:stage:
+ _objc_msgSend$isCPLEncryptionError
+ _objc_msgSend$isCPLThrottlingError
+ _objc_msgSend$isComputeStateTaskUploadEnabled
+ _objc_msgSend$isKeychainCDPEnabled
+ _objc_msgSend$lastUpdatedDate
+ _objc_msgSend$maximumComputeStatesToUploadPerBatch
+ _objc_msgSend$openWithFileRecoveryHandler:error:
+ _objc_msgSend$performMaintenanceWithError:
+ _objc_msgSend$recordComputeStatePushQueue
+ _objc_msgSend$releaseFileURL:forComputeState:error:
+ _objc_msgSend$removeComputeState:discardedFileStorageIdentifier:error:
+ _objc_msgSend$removeComputeState:error:
+ _objc_msgSend$removeComputeStateWithLocalScopedIdentifier:discardedFileStorageIdentifier:error:
+ _objc_msgSend$removeComputeStateWithLocalScopedIdentifier:error:
+ _objc_msgSend$retainFileURLForComputeState:error:
+ _objc_msgSend$retainFileURLForIdentifier:error:
+ _objc_msgSend$setKeychainCDPEnabled:
+ _objc_msgSend$setScope:hasCompletedUploadComputeStateTask:error:
+ _objc_msgSend$setScopeNeedsToUploadComputeState:error:
+ _objc_msgSend$setValuesForKeysWithDictionary:
+ _objc_msgSend$shouldDropAllUploadsForScope:dropReason:shouldQuarantineRecords:
+ _objc_msgSend$storeData:identity:isOriginal:needsCommit:error:
+ _objc_msgSend$storeFileAtURL:identifier:moveIfPossible:needsCommit:error:
+ _objc_msgSend$throttlingDate
+ _objc_msgSend$totalUnitCount
+ _objc_msgSend$updateComputeSyncMetrics:silentDecryptionFailed:error:
+ _objc_msgSend$updateLocalStateForComputeState:newLocalState:error:
+ _objc_msgSend$uploadComputeStateTaskForScope:
+ _objc_msgSend$uploadComputeStates:scope:sharedScope:targetMapping:transportScopeMapping:knownRecords:completionHandler:
+ _objc_msgSend$version
+ _objc_setProperty_atomic_copy
+ _os_unfair_lock_assert_owner
+ _propertiesForChangeType:.onceToken.13443
+ _propertiesForChangeType:.onceToken.17165
+ _propertiesForChangeType:.onceToken.21768
+ _propertiesForChangeType:.properties.21770
- -[CPLStatus setSyncSessionMetrics:]
- -[CPLStatus syncSessionMetrics]
- -[CPLSyncSessionMetrics .cxx_destruct]
- -[CPLSyncSessionMetrics incrementCountForKey:]
- -[CPLSyncSessionMetrics initWithMetricsDict:]
- -[CPLSyncSessionMetrics init]
- -[CPLSyncSessionMetrics metricsDict]
- -[CPLSyncSessionMetrics setMetricsDict:]
- -[_CPLEngineSyncLastError date]
- -[_CPLEngineSyncLastError error]
- -[_CPLEngineSyncLastError setDate:]
- -[_CPLEngineSyncLastError setError:]
- GCC_except_table1066
- GCC_except_table1145
- GCC_except_table1642
- GCC_except_table1738
- GCC_except_table1778
- GCC_except_table182
- GCC_except_table1860
- GCC_except_table1870
- GCC_except_table200
- GCC_except_table2001
- GCC_except_table2021
- GCC_except_table2085
- GCC_except_table209
- GCC_except_table212
- GCC_except_table214
- GCC_except_table216
- GCC_except_table2288
- GCC_except_table2290
- GCC_except_table2373
- GCC_except_table2434
- GCC_except_table2436
- GCC_except_table2570
- GCC_except_table2573
- GCC_except_table2587
- GCC_except_table2756
- GCC_except_table2797
- GCC_except_table3004
- GCC_except_table3066
- GCC_except_table3070
- GCC_except_table3072
- GCC_except_table3317
- GCC_except_table3347
- GCC_except_table3374
- GCC_except_table3391
- GCC_except_table3398
- GCC_except_table3406
- GCC_except_table3408
- GCC_except_table3422
- GCC_except_table3424
- GCC_except_table3426
- GCC_except_table354
- GCC_except_table363
- GCC_except_table3721
- GCC_except_table3754
- GCC_except_table3836
- GCC_except_table3846
- GCC_except_table3903
- GCC_except_table3906
- GCC_except_table4070
- GCC_except_table4078
- GCC_except_table4155
- GCC_except_table4159
- GCC_except_table4163
- GCC_except_table4170
- GCC_except_table4185
- GCC_except_table4186
- GCC_except_table4227
- GCC_except_table423
- GCC_except_table4235
- GCC_except_table427
- GCC_except_table4290
- GCC_except_table4292
- GCC_except_table4294
- GCC_except_table4441
- GCC_except_table4478
- GCC_except_table4487
- GCC_except_table4488
- GCC_except_table4545
- GCC_except_table4548
- GCC_except_table456
- GCC_except_table473
- GCC_except_table474
- GCC_except_table483
- GCC_except_table4832
- GCC_except_table4860
- GCC_except_table4890
- GCC_except_table4909
- GCC_except_table4923
- GCC_except_table4927
- GCC_except_table4976
- GCC_except_table500
- GCC_except_table5018
- GCC_except_table506
- GCC_except_table5065
- GCC_except_table5089
- GCC_except_table5102
- GCC_except_table5111
- GCC_except_table5163
- GCC_except_table5177
- GCC_except_table5294
- GCC_except_table5307
- GCC_except_table5310
- GCC_except_table5736
- GCC_except_table5772
- GCC_except_table5776
- GCC_except_table5778
- GCC_except_table5800
- GCC_except_table5807
- GCC_except_table5830
- GCC_except_table5868
- GCC_except_table5892
- GCC_except_table5901
- GCC_except_table5919
- GCC_except_table5922
- GCC_except_table5924
- GCC_except_table5958
- GCC_except_table6027
- GCC_except_table605
- GCC_except_table611
- GCC_except_table6168
- GCC_except_table6190
- GCC_except_table6219
- GCC_except_table632
- GCC_except_table637
- GCC_except_table6401
- GCC_except_table6410
- GCC_except_table6415
- GCC_except_table6429
- GCC_except_table6443
- GCC_except_table6453
- GCC_except_table6458
- GCC_except_table652
- GCC_except_table6538
- GCC_except_table665
- GCC_except_table6682
- GCC_except_table6726
- GCC_except_table6727
- GCC_except_table6740
- GCC_except_table684
- GCC_except_table782
- GCC_except_table800
- GCC_except_table802
- GCC_except_table971
- _OBJC_CLASS_$_CPLSyncSessionMetrics
- _OBJC_IVAR_$_CPLSyncSessionMetrics._metricsDict
- _OBJC_METACLASS_$_CPLSyncSessionMetrics
- __OBJC_$_INSTANCE_METHODS_CPLSyncSessionMetrics
- __OBJC_$_INSTANCE_VARIABLES_CPLSyncSessionMetrics
- __OBJC_$_PROP_LIST_CPLSyncSessionMetrics
- __OBJC_$_PROP_LIST__CPLEngineSyncLastError
- __OBJC_CLASS_RO_$_CPLSyncSessionMetrics
- __OBJC_METACLASS_RO_$_CPLSyncSessionMetrics
- ___115-[CPLProxyLibraryManager beginDownloadForResource:clientBundleID:options:proposedTaskIdentifier:completionHandler:]_block_invoke.309
- ___31-[CPLStatus syncSessionMetrics]_block_invoke
- ___35-[CPLStatus setSyncSessionMetrics:]_block_invoke
- ___36-[CPLEngineLibrary startSyncSession]_block_invoke.36
- ___36-[CPLEngineLibrary startSyncSession]_block_invoke.37
- ___38-[CPLPushToTransportScopeTask _launch]_block_invoke.106
- ___38-[CPLPushToTransportScopeTask _launch]_block_invoke_2.108
- ___41-[CPLEngineScheduler noteQuotaHasChanged]_block_invoke.127
- ___42-[CPLEngineLibrary forceFetchAccountFlags]_block_invoke.38
- ___42-[CPLEngineLibrary forceFetchAccountFlags]_block_invoke.39
- ___42-[CPLEngineLibrary performBlockOnLibrary:]_block_invoke.75
- ___42-[CPLEngineLibrary performBlockOnLibrary:]_block_invoke.76
- ___42-[CPLEngineScheduler _prepareFirstSession]_block_invoke.137
- ___42-[CPLEngineScheduler _prepareFirstSession]_block_invoke.138
- ___42-[CPLEngineScheduler _prepareFirstSession]_block_invoke_2.139
- ___42-[CPLProxyLibraryManager _setupConnection]_block_invoke.255
- ___42-[CPLProxyLibraryManager _setupConnection]_block_invoke.256
- ___42-[CPLProxyLibraryManager _setupConnection]_block_invoke.262
- ___42-[CPLProxyLibraryManager _setupConnection]_block_invoke.263
- ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.239
- ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.266
- ___49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.275
- ___49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.276
- ___49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.277
- ___49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.280
- ___50+[CPLArchiver displayableDictionaryForDictionary:]_block_invoke.1601
- ___51-[CPLEngineStore _reallySchedulePendingUpdateApply]_block_invoke.321
- ___51-[CPLPushToTransportScopeTask _updateContributors:]_block_invoke.84
- ___52-[CPLEngineSyncManager resetTransportUserIdentifier]_block_invoke.221
- ___52-[CPLEngineSyncManager resetTransportUserIdentifier]_block_invoke_2.224
- ___52-[CPLProxyLibraryManager openWithCompletionHandler:]_block_invoke.288
- ___52-[CPLProxyLibraryManager openWithCompletionHandler:]_block_invoke.290
- ___52-[CPLProxyLibraryManager openWithCompletionHandler:]_block_invoke.291
- ___53-[CPLProxyLibraryManager closeWithCompletionHandler:]_block_invoke.292
- ___55-[CPLEngineLibrary attachObject:withCompletionHandler:]_block_invoke.64
- ___55-[CPLEngineStore closeAndDeactivate:completionHandler:]_block_invoke.311
- ___55-[CPLEngineSyncManager _launchForceSyncTaskIfNecessary]_block_invoke.260
- ___56-[CPLEngineSyncManager _setupTaskWithCompletionHandler:]_block_invoke.274
- ___56-[CPLEngineSyncManager _setupTaskWithCompletionHandler:]_block_invoke_2.276
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.108
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.116
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.122
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.128
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.134
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.140
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.147
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.152
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.158
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.164
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.170
- ___57-[CPLEngineSyncManager setSyncSessionShouldBeForeground:]_block_invoke.232
- ___58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke.293
- ___58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke.295
- ___58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke.297
- ___58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke_2.294
- ___58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke_2.296
- ___58-[CPLProxyLibraryManager noteClientIsInForegroundQuietly:]_block_invoke.327
- ___59-[CPLEngineLibrary provideCloudResource:completionHandler:]_block_invoke.83
- ___59-[CPLEngineLibrary provideCloudResource:completionHandler:]_block_invoke.84
- ___59-[CPLPushToTransportScopeTask _pushTaskDidFinishWithError:]_block_invoke.120
- ___59-[CPLPushToTransportScopeTask _pushTaskDidFinishWithError:]_block_invoke_2.121
- ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke.133
- ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke.135
- ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke_2.136
- ___66-[CPLEngineScheduler noteSyncSession:failedDuringPhase:withError:]_block_invoke.113
- ___66-[CPLEngineScheduler noteSyncSession:failedDuringPhase:withError:]_block_invoke.114
- ___66-[CPLEngineScheduler noteSyncSession:failedDuringPhase:withError:]_block_invoke.115
- ___67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke.122
- ___67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke.124
- ___67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke_2.123
- ___68-[CPLEngineScheduler _handleResetAnchorWithError:completionHandler:]_block_invoke.108
- ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.106
- ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.97
- ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.98
- ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.99
- ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_2.101
- ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_2.103
- ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_2.107
- ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_3.104
- ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_4.105
- ___74-[CPLEngineScheduler _handleResetGlobalAnchorWithError:completionHandler:]_block_invoke.112
- ___76-[CPLEngineLibrary provideRecordWithCloudScopeIdentifier:completionHandler:]_block_invoke.82
- ___76-[CPLProxyLibraryManager beginInMemoryDownloadOfResource:completionHandler:]_block_invoke.317
- ___78-[CPLEngineLibrary forceBackupWithActivity:forceClientPush:completionHandler:]_block_invoke.111
- ___78-[CPLEngineLibrary forceBackupWithActivity:forceClientPush:completionHandler:]_block_invoke.118
- ___78-[CPLEngineLibrary forceBackupWithActivity:forceClientPush:completionHandler:]_block_invoke_2.115
- ___79-[CPLEngineLibrary provideScopeChangeForScopeWithIdentifier:completionHandler:]_block_invoke.81
- ___83-[CPLProxyLibraryManager forceSynchronizingScopeWithIdentifiers:completionHandler:]_block_invoke.336
- ___84-[CPLEngineStore _performWriteTransactionByPassBlocker:WithBlock:completionHandler:]_block_invoke.284
- ___Block_byref_object_copy_.10289
- ___Block_byref_object_copy_.1105
- ___Block_byref_object_copy_.11139
- ___Block_byref_object_copy_.11693
- ___Block_byref_object_copy_.11995
- ___Block_byref_object_copy_.12117
- ___Block_byref_object_copy_.12910
- ___Block_byref_object_copy_.13494
- ___Block_byref_object_copy_.14243
- ___Block_byref_object_copy_.14501
- ___Block_byref_object_copy_.14932
- ___Block_byref_object_copy_.15556
- ___Block_byref_object_copy_.1562
- ___Block_byref_object_copy_.16352
- ___Block_byref_object_copy_.17583
- ___Block_byref_object_copy_.18024
- ___Block_byref_object_copy_.18601
- ___Block_byref_object_copy_.19084
- ___Block_byref_object_copy_.19417
- ___Block_byref_object_copy_.2016
- ___Block_byref_object_copy_.20434
- ___Block_byref_object_copy_.20734
- ___Block_byref_object_copy_.2092
- ___Block_byref_object_copy_.21477
- ___Block_byref_object_copy_.2458
- ___Block_byref_object_copy_.314
- ___Block_byref_object_copy_.4630
- ___Block_byref_object_copy_.5194
- ___Block_byref_object_copy_.5357
- ___Block_byref_object_copy_.5834
- ___Block_byref_object_copy_.6191
- ___Block_byref_object_copy_.643
- ___Block_byref_object_copy_.6456
- ___Block_byref_object_copy_.8077
- ___Block_byref_object_copy_.830
- ___Block_byref_object_copy_.8339
- ___Block_byref_object_copy_.9338
- ___Block_byref_object_copy_.954
- ___Block_byref_object_copy_.9630
- ___Block_byref_object_dispose_.10290
- ___Block_byref_object_dispose_.1106
- ___Block_byref_object_dispose_.11140
- ___Block_byref_object_dispose_.11694
- ___Block_byref_object_dispose_.11996
- ___Block_byref_object_dispose_.12118
- ___Block_byref_object_dispose_.12911
- ___Block_byref_object_dispose_.13495
- ___Block_byref_object_dispose_.14244
- ___Block_byref_object_dispose_.14502
- ___Block_byref_object_dispose_.14933
- ___Block_byref_object_dispose_.15557
- ___Block_byref_object_dispose_.1563
- ___Block_byref_object_dispose_.16353
- ___Block_byref_object_dispose_.17584
- ___Block_byref_object_dispose_.18025
- ___Block_byref_object_dispose_.18602
- ___Block_byref_object_dispose_.19085
- ___Block_byref_object_dispose_.19418
- ___Block_byref_object_dispose_.2017
- ___Block_byref_object_dispose_.20435
- ___Block_byref_object_dispose_.20735
- ___Block_byref_object_dispose_.2093
- ___Block_byref_object_dispose_.21478
- ___Block_byref_object_dispose_.2459
- ___Block_byref_object_dispose_.315
- ___Block_byref_object_dispose_.4631
- ___Block_byref_object_dispose_.5195
- ___Block_byref_object_dispose_.5358
- ___Block_byref_object_dispose_.5835
- ___Block_byref_object_dispose_.6192
- ___Block_byref_object_dispose_.644
- ___Block_byref_object_dispose_.6457
- ___Block_byref_object_dispose_.8078
- ___Block_byref_object_dispose_.831
- ___Block_byref_object_dispose_.8340
- ___Block_byref_object_dispose_.9339
- ___Block_byref_object_dispose_.955
- ___Block_byref_object_dispose_.9631
- ___CPLForceSyncOSLogDomain.18134
- ___CPLForceSyncOSLogDomain.onceToken.18143
- ___CPLForceSyncOSLogDomain.result.18144
- ___CPLSchedulerOSLogDomain.6141
- ___CPLSchedulerOSLogDomain.onceToken.6142
- ___CPLSchedulerOSLogDomain.result.6143
- ___CPLSessionOSLogDomain.14115
- ___CPLSessionOSLogDomain.15931
- ___CPLSessionOSLogDomain.20019
- ___CPLSessionOSLogDomain.onceToken.14166
- ___CPLSessionOSLogDomain.onceToken.15936
- ___CPLSessionOSLogDomain.onceToken.20021
- ___CPLSessionOSLogDomain.result.14167
- ___CPLSessionOSLogDomain.result.15937
- ___CPLSessionOSLogDomain.result.20023
- ___CPLStorageOSLogDomain.1543
- ___CPLStorageOSLogDomain.15524
- ___CPLStorageOSLogDomain.18741
- ___CPLStorageOSLogDomain.192
- ___CPLStorageOSLogDomain.19404
- ___CPLStorageOSLogDomain.19652
- ___CPLStorageOSLogDomain.471
- ___CPLStorageOSLogDomain.4975
- ___CPLStorageOSLogDomain.6413
- ___CPLStorageOSLogDomain.7037
- ___CPLStorageOSLogDomain.7434
- ___CPLStorageOSLogDomain.7557
- ___CPLStorageOSLogDomain.7737
- ___CPLStorageOSLogDomain.850
- ___CPLStorageOSLogDomain.9306
- ___CPLStorageOSLogDomain.9391
- ___CPLStorageOSLogDomain.onceToken.12451
- ___CPLStorageOSLogDomain.onceToken.1545
- ___CPLStorageOSLogDomain.onceToken.15526
- ___CPLStorageOSLogDomain.onceToken.17776
- ___CPLStorageOSLogDomain.onceToken.18745
- ___CPLStorageOSLogDomain.onceToken.194
- ___CPLStorageOSLogDomain.onceToken.19409
- ___CPLStorageOSLogDomain.onceToken.19660
- ___CPLStorageOSLogDomain.onceToken.473
- ___CPLStorageOSLogDomain.onceToken.4977
- ___CPLStorageOSLogDomain.onceToken.6415
- ___CPLStorageOSLogDomain.onceToken.7042
- ___CPLStorageOSLogDomain.onceToken.7440
- ___CPLStorageOSLogDomain.onceToken.7559
- ___CPLStorageOSLogDomain.onceToken.7739
- ___CPLStorageOSLogDomain.onceToken.859
- ___CPLStorageOSLogDomain.onceToken.9317
- ___CPLStorageOSLogDomain.onceToken.9394
- ___CPLStorageOSLogDomain.result.12453
- ___CPLStorageOSLogDomain.result.1547
- ___CPLStorageOSLogDomain.result.15528
- ___CPLStorageOSLogDomain.result.17778
- ___CPLStorageOSLogDomain.result.18747
- ___CPLStorageOSLogDomain.result.19411
- ___CPLStorageOSLogDomain.result.196
- ___CPLStorageOSLogDomain.result.19662
- ___CPLStorageOSLogDomain.result.475
- ___CPLStorageOSLogDomain.result.4979
- ___CPLStorageOSLogDomain.result.6416
- ___CPLStorageOSLogDomain.result.7043
- ___CPLStorageOSLogDomain.result.7442
- ___CPLStorageOSLogDomain.result.7561
- ___CPLStorageOSLogDomain.result.7740
- ___CPLStorageOSLogDomain.result.861
- ___CPLStorageOSLogDomain.result.9319
- ___CPLStorageOSLogDomain.result.9396
- ___CPLStoreOSLogDomain.2250
- ___CPLStoreOSLogDomain.onceToken.2251
- ___CPLStoreOSLogDomain.result.2252
- ___CPLTaskOSLogDomain.11979
- ___CPLTaskOSLogDomain.12361
- ___CPLTaskOSLogDomain.13393
- ___CPLTaskOSLogDomain.14904
- ___CPLTaskOSLogDomain.18546
- ___CPLTaskOSLogDomain.20357
- ___CPLTaskOSLogDomain.2077
- ___CPLTaskOSLogDomain.21429
- ___CPLTaskOSLogDomain.4404
- ___CPLTaskOSLogDomain.5757
- ___CPLTaskOSLogDomain.587
- ___CPLTaskOSLogDomain.9576
- ___CPLTaskOSLogDomain.onceToken.11986
- ___CPLTaskOSLogDomain.onceToken.12363
- ___CPLTaskOSLogDomain.onceToken.13402
- ___CPLTaskOSLogDomain.onceToken.14907
- ___CPLTaskOSLogDomain.onceToken.18588
- ___CPLTaskOSLogDomain.onceToken.20366
- ___CPLTaskOSLogDomain.onceToken.2079
- ___CPLTaskOSLogDomain.onceToken.21437
- ___CPLTaskOSLogDomain.onceToken.4407
- ___CPLTaskOSLogDomain.onceToken.5769
- ___CPLTaskOSLogDomain.onceToken.590
- ___CPLTaskOSLogDomain.onceToken.9612
- ___CPLTaskOSLogDomain.result.11988
- ___CPLTaskOSLogDomain.result.12365
- ___CPLTaskOSLogDomain.result.13404
- ___CPLTaskOSLogDomain.result.14908
- ___CPLTaskOSLogDomain.result.18590
- ___CPLTaskOSLogDomain.result.20367
- ___CPLTaskOSLogDomain.result.2081
- ___CPLTaskOSLogDomain.result.21438
- ___CPLTaskOSLogDomain.result.4409
- ___CPLTaskOSLogDomain.result.5771
- ___CPLTaskOSLogDomain.result.592
- ___CPLTaskOSLogDomain.result.9614
- _____CPLForceSyncOSLogDomain_block_invoke.18146
- _____CPLSchedulerOSLogDomain_block_invoke.6145
- _____CPLSessionOSLogDomain_block_invoke.14169
- _____CPLSessionOSLogDomain_block_invoke.15939
- _____CPLSessionOSLogDomain_block_invoke.20026
- _____CPLStorageOSLogDomain_block_invoke.12458
- _____CPLStorageOSLogDomain_block_invoke.1550
- _____CPLStorageOSLogDomain_block_invoke.15531
- _____CPLStorageOSLogDomain_block_invoke.17785
- _____CPLStorageOSLogDomain_block_invoke.18750
- _____CPLStorageOSLogDomain_block_invoke.19414
- _____CPLStorageOSLogDomain_block_invoke.19665
- _____CPLStorageOSLogDomain_block_invoke.199
- _____CPLStorageOSLogDomain_block_invoke.478
- _____CPLStorageOSLogDomain_block_invoke.4982
- _____CPLStorageOSLogDomain_block_invoke.6418
- _____CPLStorageOSLogDomain_block_invoke.7045
- _____CPLStorageOSLogDomain_block_invoke.7445
- _____CPLStorageOSLogDomain_block_invoke.7564
- _____CPLStorageOSLogDomain_block_invoke.7742
- _____CPLStorageOSLogDomain_block_invoke.864
- _____CPLStorageOSLogDomain_block_invoke.9322
- _____CPLStorageOSLogDomain_block_invoke.9399
- _____CPLStoreOSLogDomain_block_invoke.2254
- _____CPLTaskOSLogDomain_block_invoke.11991
- _____CPLTaskOSLogDomain_block_invoke.12368
- _____CPLTaskOSLogDomain_block_invoke.13407
- _____CPLTaskOSLogDomain_block_invoke.14910
- _____CPLTaskOSLogDomain_block_invoke.18593
- _____CPLTaskOSLogDomain_block_invoke.20369
- _____CPLTaskOSLogDomain_block_invoke.2084
- _____CPLTaskOSLogDomain_block_invoke.21440
- _____CPLTaskOSLogDomain_block_invoke.4412
- _____CPLTaskOSLogDomain_block_invoke.5774
- _____CPLTaskOSLogDomain_block_invoke.595
- _____CPLTaskOSLogDomain_block_invoke.9617
- ___block_descriptor_128_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_40_e8_32bs_e23_v28?0B8Q12"NSError"20ls32l8
- ___block_descriptor_48_e8_32s40bs_e36_v24?0"CPLScopeChange"8"NSError"16ls32l8s40l8
- ___block_descriptor_64_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_literal_global.100
- ___block_literal_global.10440
- ___block_literal_global.10670
- ___block_literal_global.111
- ___block_literal_global.1110
- ___block_literal_global.11160
- ___block_literal_global.118
- ___block_literal_global.11987
- ___block_literal_global.12.6537
- ___block_literal_global.12163
- ___block_literal_global.12398
- ___block_literal_global.124
- ___block_literal_global.12452
- ___block_literal_global.12623
- ___block_literal_global.130.18297
- ___block_literal_global.130.18589
- ___block_literal_global.13125
- ___block_literal_global.13143
- ___block_literal_global.13203
- ___block_literal_global.134
- ___block_literal_global.13403
- ___block_literal_global.138.16692
- ___block_literal_global.1388
- ___block_literal_global.13979
- ___block_literal_global.14.12399
- ___block_literal_global.14.4349
- ___block_literal_global.14186
- ___block_literal_global.1423
- ___block_literal_global.143.17777
- ___block_literal_global.143.18298
- ___block_literal_global.14653
- ___block_literal_global.149
- ___block_literal_global.14957
- ___block_literal_global.15322
- ___block_literal_global.154.18299
- ___block_literal_global.1546
- ___block_literal_global.15527
- ___block_literal_global.1585
- ___block_literal_global.15949
- ___block_literal_global.1598
- ___block_literal_global.160
- ___block_literal_global.1612
- ___block_literal_global.16122
- ___block_literal_global.1614
- ___block_literal_global.1619
- ___block_literal_global.1621
- ___block_literal_global.1623
- ___block_literal_global.16243
- ___block_literal_global.1625
- ___block_literal_global.1627
- ___block_literal_global.1629
- ___block_literal_global.1631
- ___block_literal_global.1633
- ___block_literal_global.1635
- ___block_literal_global.166
- ___block_literal_global.16803
- ___block_literal_global.1686
- ___block_literal_global.1688
- ___block_literal_global.172
- ___block_literal_global.17362
- ___block_literal_global.17662
- ___block_literal_global.17780
- ___block_literal_global.1792
- ___block_literal_global.18292
- ___block_literal_global.1836
- ___block_literal_global.1842
- ___block_literal_global.18608
- ___block_literal_global.18746
- ___block_literal_global.18918
- ___block_literal_global.19410
- ___block_literal_global.195
- ___block_literal_global.1966
- ___block_literal_global.19661
- ___block_literal_global.19821
- ___block_literal_global.2.16802
- ___block_literal_global.2.21695
- ___block_literal_global.20022
- ___block_literal_global.2015
- ___block_literal_global.20174
- ___block_literal_global.20430
- ___block_literal_global.2080
- ___block_literal_global.20985
- ___block_literal_global.21121
- ___block_literal_global.21189
- ___block_literal_global.21577
- ___block_literal_global.21689
- ___block_literal_global.21785
- ___block_literal_global.21971
- ___block_literal_global.22.6540
- ___block_literal_global.2229
- ___block_literal_global.225.6393
- ___block_literal_global.2476
- ___block_literal_global.27.14206
- ___block_literal_global.2700
- ___block_literal_global.271
- ___block_literal_global.273
- ___block_literal_global.275
- ___block_literal_global.277
- ___block_literal_global.279
- ___block_literal_global.282
- ___block_literal_global.2911
- ___block_literal_global.295
- ___block_literal_global.3114
- ___block_literal_global.32.19789
- ___block_literal_global.323
- ___block_literal_global.325
- ___block_literal_global.33.5884
- ___block_literal_global.3539
- ___block_literal_global.3665
- ___block_literal_global.37.16728
- ___block_literal_global.37.6544
- ___block_literal_global.3819
- ___block_literal_global.419
- ___block_literal_global.4228
- ___block_literal_global.4314
- ___block_literal_global.4408
- ___block_literal_global.4551
- ___block_literal_global.4626
- ___block_literal_global.47.6547
- ___block_literal_global.474
- ___block_literal_global.480
- ___block_literal_global.483
- ___block_literal_global.4978
- ___block_literal_global.5
- ___block_literal_global.514
- ___block_literal_global.517
- ___block_literal_global.5170
- ___block_literal_global.534
- ___block_literal_global.537
- ___block_literal_global.5770
- ___block_literal_global.5883
- ___block_literal_global.591
- ___block_literal_global.591.14485
- ___block_literal_global.594
- ___block_literal_global.600
- ___block_literal_global.603
- ___block_literal_global.6254
- ___block_literal_global.647
- ___block_literal_global.650
- ___block_literal_global.653
- ___block_literal_global.6534
- ___block_literal_global.697
- ___block_literal_global.7135
- ___block_literal_global.73
- ___block_literal_global.7335
- ___block_literal_global.7441
- ___block_literal_global.7560
- ___block_literal_global.769
- ___block_literal_global.7785
- ___block_literal_global.7967
- ___block_literal_global.82
- ___block_literal_global.8207
- ___block_literal_global.8349
- ___block_literal_global.860
- ___block_literal_global.8609
- ___block_literal_global.87
- ___block_literal_global.89.12364
- ___block_literal_global.8903
- ___block_literal_global.9164
- ___block_literal_global.9318
- ___block_literal_global.9395
- ___block_literal_global.96
- ___block_literal_global.9613
- ___block_literal_global.988
- ___block_literal_global.993
- ___block_literal_global.994
- ___cpl_dispatch_async_block_invoke.10092
- ___cpl_dispatch_async_block_invoke.11974
- ___cpl_dispatch_async_block_invoke.12284
- ___cpl_dispatch_async_block_invoke.12357
- ___cpl_dispatch_async_block_invoke.13484
- ___cpl_dispatch_async_block_invoke.1351
- ___cpl_dispatch_async_block_invoke.14483
- ___cpl_dispatch_async_block_invoke.14900
- ___cpl_dispatch_async_block_invoke.15275
- ___cpl_dispatch_async_block_invoke.15755
- ___cpl_dispatch_async_block_invoke.16239
- ___cpl_dispatch_async_block_invoke.18011
- ___cpl_dispatch_async_block_invoke.18544
- ___cpl_dispatch_async_block_invoke.18925
- ___cpl_dispatch_async_block_invoke.20176
- ___cpl_dispatch_async_block_invoke.20373
- ___cpl_dispatch_async_block_invoke.21486
- ___cpl_dispatch_async_block_invoke.5397
- ___cpl_dispatch_async_block_invoke.5755
- ___cpl_dispatch_async_block_invoke.6015
- ___cpl_dispatch_async_block_invoke.6426
- ___cpl_dispatch_async_block_invoke.646
- ___cpl_dispatch_async_block_invoke.8074
- ___cpl_dispatch_async_block_invoke.8337
- ___cpl_dispatch_async_block_invoke.9572
- __doProtected:.onceToken.13142
- __doProtected:.onceToken.20173
- __doProtected:.queue.20175
- __statusDidChange.10310
- __unnamed_array_storage.10393
- __unnamed_array_storage.11533
- __unnamed_array_storage.1377
- __unnamed_array_storage.1582
- __unnamed_array_storage.19049
- __unnamed_array_storage.4550
- __unnamed_array_storage.4638
- _copyDerivativesFromRecordIfPossible:.originalDerivativesImageAndVideo.16713
- _initWithCPLArchiver:.onceToken.1839
- _initWithCPLArchiver:.stringClass.1840
- _initWithCoder:.logOnceToken.17664
- _initWithCoder:.onceToken.12162
- _initWithCoder:.onceToken.15948
- _initWithCoder:.onceToken.17661
- _initWithCoder:.onceToken.19820
- _initWithCoder:.onceToken.21970
- _initWithCoder:.onceToken.4207
- _initWithCoder:.onceToken.4313
- _initWithCoder:.onceToken.5165
- _initWithCoder:.onceToken.8902
- _initWithCoder:.pushContextsClasses.19822
- _initWithCoder:.stringClass.8904
- _objc_msgSend$initWithMetricsDict:
- _objc_msgSend$metricsDict
- _objc_msgSend$setDate:
- _objc_msgSend$setSyncSessionMetrics:
- _objc_msgSend$syncSessionMetrics
- _propertiesForChangeType:.onceToken.12986
- _propertiesForChangeType:.onceToken.16727
- _propertiesForChangeType:.onceToken.21120
- _propertiesForChangeType:.properties.21122
CStrings:
+ "\x02\x18&\x12q!\x122\x15"
+ "\x03\x11\x13"
+ "\x04\x14\x15!\x11\x13\x1f\x04"
+ "\t\x11\x15\x16("
+ "\n\t%@ (%@): %@ %ld %@%@"
+ "\n\t%@ (%@): [DEFER] %@ %ld %@"
+ "\nIncoming download folder creation: %@"
+ "\nLast download request: %@"
+ "\nUploads have been throttled until %@ and will resume during the next sync session"
+ "\nUploads will resume %@"
+ "%@ = %ld"
+ "%@ appears to have been deleted - will need to check directly with the cloud"
+ "%@ is temporarily excluded from pushing to transport - won't upload any compute states for this scope"
+ "%lu"
+ "%lu compute states for %@ have been dropped"
+ "%lu compute states for %@ have been put aside"
+ "/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Upload Compute State Phase/CPLUploadComputeStatesTask.m"
+ "<%@ %@ %@ %@ %@ %@ %@>"
+ "<%@ %@ %@ %@ %@ %@>"
+ "@\"<CPLEngineTransportUploadComputeStatesTask>\""
+ "@\"CPLEngineRecordComputeStatePushQueue\""
+ "@\"CPLMetrics\""
+ "@40@0:8@16Q24Q32"
+ "@64@0:8@16@24@32@40@48@56"
+ "@64@0:8@16@24@32@40@48@?56"
+ "@72@0:8@16@24@32@40@48@56@?64"
+ "B40@0:8@16^@24^B32"
+ "B48@0:8@16@24^B32^@40"
+ "CPLEngineRecordComputeStatePushQueue"
+ "CPLEngineSyncManagerStateUploadComputeStates"
+ "CPLMetrics"
+ "CPLMetricsDidChangeNotification"
+ "CPLOverriddenConfigurationKeys"
+ "CPLRecordComputeState"
+ "CPLRecordComputeStateValidator"
+ "CPLRecordComputeStateVersion"
+ "CPLUploadComputeStatesScopeTask"
+ "CPLUploadComputeStatesTask"
+ "Can't create a transport upload compute states task for %@"
+ "Can't create an upload compute states task for %@"
+ "CloudPhotoLibrary-662.0.141"
+ "Creating incoming download folder at %@"
+ "Deleting incoming download folder at %@"
+ "DownloadCKErrorCount"
+ "DownloadCount"
+ "DownloadDecryptionErrorCount"
+ "DownloadFailureCount"
+ "DownloadThrottledErrorCount"
+ "Dropped %ld compute states for %@"
+ "Dropping compute state for %@ as the record is not known from the client cache view"
+ "Failed to create incoming download folder at %@: %@"
+ "Failed to create temporary download folder at %@: %@"
+ "Failed to delete temporary folder at %@: %@"
+ "Failed to determine filesize for compute state payload file at url: %@. Error: %@"
+ "Failed to find compute state payload for %@: %@"
+ "Failed to put compute state for %@ aside: %@"
+ "Failed to remove compute state for %@: %@"
+ "Failed to upload %lu compute states: %@"
+ "Overriding server configuration keys with %@"
+ "Putting compute state for %@ aside as the record is not in the cloud cache yet"
+ "Q32@0:8@16^@24"
+ "Setting compute state for %@ back to pending as the record is now in the cloud cache"
+ "T@\"CPLEngineRecordComputeStatePushQueue\",R,N,V_recordComputeStatePushQueue"
+ "T@\"CPLScopedIdentifier\",R,N,V_itemScopedIdentifier"
+ "T@\"NSDate\",&,N,V_computeStateLastUpdatedDate"
+ "T@\"NSDate\",C,V_throttlingDate"
+ "T@\"NSDate\",R,N,V_lastUpdatedDate"
+ "T@\"NSString\",&,N,V_computeStateAdjustmentFingerprint"
+ "T@\"NSString\",&,N,V_computeStateVersion"
+ "T@\"NSString\",C,N,V_fileStorageIdentifier"
+ "T@\"NSString\",R,N,V_adjustmentFingerprint"
+ "T@\"NSString\",R,N,V_version"
+ "T@\"NSURL\",R,N,V_incomingDownloadFolderURL"
+ "TB,N,GisKeychainCDPEnabled"
+ "TQ,R,N,V_majorVersion"
+ "TQ,R,N,V_stage"
+ "There should not be any compute states dequeued here"
+ "Tq,R"
+ "Trying to fetch compute states while the library is not open"
+ "UploadCKErrorCount"
+ "UploadCount"
+ "UploadEncryptionErrorCount"
+ "UploadFailureCount"
+ "UploadThrottledErrorCount"
+ "Uploaded %lu compute states (dropped %lu) successfully in %.1fs:\n%{public}@"
+ "Uploading compute states for %@ has been throttled"
+ "Uploading compute states for %{public}@ has been throttled, we will likely need to retry that"
+ "We must drop all compute states for %@: %@"
+ "_adjustmentFingerprint"
+ "_cloudComputeStates"
+ "_computeStateAdjustmentFingerprint"
+ "_computeStateLastUpdatedDate"
+ "_computeStateVersion"
+ "_countOfComputeStatesPutAside"
+ "_countOfDroppedComputeStates"
+ "_didUploadSomeComputeStates"
+ "_discardExtractedBatchAndGetNextBatch"
+ "_dropAllComputeStates"
+ "_fileStorageIdentifier"
+ "_filesToCommit"
+ "_filesToDelete"
+ "_getNextBatchAndUpload"
+ "_identityForIdentifier:"
+ "_incomingDownloadFolderCreationDate"
+ "_incomingDownloadFolderURL"
+ "_knownRecords"
+ "_lastComputeStateDownloadRequestDate"
+ "_lastComputeStateDownloadRequestDateLock"
+ "_lastUpdatedDate"
+ "_majorVersion"
+ "_metrics"
+ "_metricsFileURL"
+ "_metricsObserver"
+ "_recordComputeStatePushQueue"
+ "_stage"
+ "_tempFolderIndex"
+ "_throttlingDate"
+ "_updateComputeSyncUploadMetricsWithError:"
+ "_uploadComputeStatesTask"
+ "_uploadComputeStatesTaskDidFinishWithError:"
+ "_uploadExtractedBatch"
+ "addComputeState:discardedFileStorageIdentifier:error:"
+ "addComputeState:error:"
+ "adjustmentFingerprint"
+ "attachComputeStates:completionHandler:"
+ "commitFileWithIdentifier:error:"
+ "compute-state.upload-task"
+ "computeStateAdjustmentFingerprint"
+ "computeStateLastUpdatedDate"
+ "computeStateVersion"
+ "computeStatesToUploadWithScopeIdentifier:localState:maximumCount:"
+ "countForKey:"
+ "countOfComputeStates"
+ "createGroupForComputeStateDownloadOnDemand"
+ "createGroupForComputeStateDownloadPrefetch"
+ "createGroupForComputeStateUpload"
+ "createIncomingDownloadFolderIfNecessaryWithError:"
+ "createNewTempDownloadFolderWithError:"
+ "cstD"
+ "cstF"
+ "cstV"
+ "deleteFileWithIdentifier:error:"
+ "deleteIncomingDownloadFolderWithError:"
+ "deleteRecordsForScopeIndex:discardedFileStorageIdentifiers:maxCount:deletedCount:error:"
+ "dictionaryForKey:"
+ "discardUncommittedFileWithIdentifier:error:"
+ "doesScopeNeedToUploadComputeState:"
+ "downloadComputeStatesWithScopedIdentifiers:scope:sharedScope:targetStorageURL:transportScopeMapping:completionHandler:"
+ "engine.computestatequeue"
+ "engine.sync.uploadcomputestates"
+ "enumeratorForScopesNeedingToUploadComputeState"
+ "fetchComputeStatesForRecordsWithScopedIdentifiers:validator:onDemand:completionHandler:"
+ "fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:"
+ "fileSizeForComputeStatePayloadFileURL:error:"
+ "fileStorageIdentifier"
+ "forceLoad"
+ "hasFileWithIdentifier:"
+ "hasScopesNeedingToUploadComputeState"
+ "hasSomeComputeStateWithFileStorageIdentifier:"
+ "incomingDownloadFolderURL"
+ "incomingRecordComputeStates"
+ "initWithItemScopedIdentifier:fileStorageIdentifier:version:fileURL:adjustmentFingerprint:lastUpdatedDate:"
+ "initWithItemScopedIdentifier:version:fileURL:adjustmentFingerprint:lastUpdatedDate:"
+ "initWithMajorVersion:stage:"
+ "isCPLEncryptionError"
+ "isCPLThrottlingError"
+ "isComputeStateTaskUploadEnabled"
+ "isComputeStateValid:"
+ "isKeychainCDPEnabled"
+ "keychainCDPEnabled"
+ "lastUpdatedDate"
+ "majorVersion"
+ "max.num.computeStatesToUploadPerBatch"
+ "maximumComputeStatesToUploadPerBatch"
+ "metrics.plist"
+ "metricsDescription"
+ "noteComputeStateDownloadRequest"
+ "noteScopeNeedsToUploadComputeState"
+ "openWithFileRecoveryHandler:error:"
+ "outgoingRecordComputeStates"
+ "performMaintenanceWithError:"
+ "public.data"
+ "recordComputeStatePushQueue"
+ "releaseFileURL:forComputeState:error:"
+ "removeComputeState:discardedFileStorageIdentifier:error:"
+ "removeComputeState:error:"
+ "removeComputeStateWithLocalScopedIdentifier:discardedFileStorageIdentifier:error:"
+ "removeComputeStateWithLocalScopedIdentifier:error:"
+ "resetMetrics"
+ "retainFileURLForComputeState:error:"
+ "retainFileURLForIdentifier:error:"
+ "serverSupportsComputeState"
+ "setComputeStateAdjustmentFingerprint:"
+ "setComputeStateLastUpdatedDate:"
+ "setComputeStateVersion:"
+ "setFileStorageIdentifier:"
+ "setKeychainCDPEnabled:"
+ "setScope:hasCompletedUploadComputeStateTask:error:"
+ "setScopeNeedsToUploadComputeState:error:"
+ "setThrottlingDate:"
+ "setValuesForKeysWithDictionary:"
+ "shouldDropAllUploadsForScope:dropReason:shouldQuarantineRecords:"
+ "stage"
+ "storeData:identifier:needsCommit:error:"
+ "storeFileAtURL:identifier:moveIfPossible:needsCommit:error:"
+ "storeUnretainedData:identifier:error:"
+ "storeUnretainedFileAtURL:identifier:error:"
+ "throttlingDate"
+ "totalUnitCount"
+ "updateComputeSyncMetrics:silentDecryptionFailed:error:"
+ "updateLocalStateForComputeState:newLocalState:error:"
+ "upload compute states"
+ "upload-compute-states"
+ "uploadComputeStateTaskForScope:"
+ "uploadComputeStates:scope:sharedScope:targetMapping:transportScopeMapping:knownRecords:completionHandler:"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
+ "v36@0:8q16B24@28"
+ "v48@0:8@\"NSArray\"16@\"CPLRecordComputeStateValidator\"24B32B36@?<v@?@\"NSDictionary\"@\"NSError\">40"
+ "v48@0:8@16@24B32B36@?40"
+ "\xf0\xa1"
- "\x02\x18&\x12q!\x122\x12"
- "\x04\x14\x15!\x11\x13\x1f\x03"
- "\b\x11\x14\x16("
- "\n\t%@: %@ %ld %@%@"
- "\n\t%@: [DEFER] %@ %ld %@"
- "CPLSyncSessionMetrics"
- "CloudPhotoLibrary-652.0.110"
- "T@\"CPLSyncSessionMetrics\",C"
- "T@\"NSDate\",C,N,V_date"
- "T@\"NSDictionary\",C,N,V_metricsDict"
- "_metricsDict"
- "initWithMetricsDict:"
- "metricsDict"
- "setDate:"
- "setMetricsDict:"
- "setSyncSessionMetrics:"
- "\xf0\x81"

```
