## CloudPhotoLibrary

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary`

```diff

-800.20.101.0.0
-  __TEXT.__text: 0x19646c
+800.26.109.0.0
+  __TEXT.__text: 0x198c54
   __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_methlist: 0x130f4
+  __TEXT.__objc_methlist: 0x1322c
   __TEXT.__const: 0x2f8
-  __TEXT.__gcc_except_tab: 0x4674
-  __TEXT.__oslogstring: 0x146d4
-  __TEXT.__cstring: 0x1400d
-  __TEXT.__unwind_info: 0x5b90
-  __TEXT.__objc_classname: 0x1e86
-  __TEXT.__objc_methname: 0x2ad02
-  __TEXT.__objc_methtype: 0x4683
-  __TEXT.__objc_stubs: 0x19f80
+  __TEXT.__gcc_except_tab: 0x4740
+  __TEXT.__oslogstring: 0x146ee
+  __TEXT.__cstring: 0x14118
+  __TEXT.__unwind_info: 0x5ca0
+  __TEXT.__objc_classname: 0x1ea7
+  __TEXT.__objc_methname: 0x2ae90
+  __TEXT.__objc_methtype: 0x4798
+  __TEXT.__objc_stubs: 0x1a0c0
   __DATA_CONST.__got: 0xa48
-  __DATA_CONST.__const: 0x6178
+  __DATA_CONST.__const: 0x62b8
   __DATA_CONST.__objc_classlist: 0x888
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x130
+  __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x85d0
+  __DATA_CONST.__objc_selrefs: 0x8618
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x820
   __DATA_CONST.__objc_arraydata: 0x1320
   __AUTH_CONST.__auth_got: 0x790
-  __AUTH_CONST.__const: 0x2620
-  __AUTH_CONST.__cfstring: 0x15540
-  __AUTH_CONST.__objc_const: 0x1e238
+  __AUTH_CONST.__const: 0x26c0
+  __AUTH_CONST.__cfstring: 0x156a0
+  __AUTH_CONST.__objc_const: 0x1e488
   __AUTH_CONST.__objc_intobj: 0x5b8
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x17e4
-  __DATA.__data: 0x1008
+  __AUTH.__objc_data: 0x5f0
+  __DATA.__objc_ivar: 0x17f0
+  __DATA.__data: 0x1068
   __DATA.__bss: 0xa88
   __DATA.__common: 0x21
-  __DATA_DIRTY.__objc_data: 0x4fb0
+  __DATA_DIRTY.__objc_data: 0x4f60
   __DATA_DIRTY.__bss: 0x3a0
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1C890D41-6873-3917-A858-3183B4BFB480
-  Functions: 8447
-  Symbols:   26119
-  CStrings:  14850
+  UUID: 3807FCC9-1B2C-33D9-A601-2B4E643C6F39
+  Functions: 8502
+  Symbols:   26262
+  CStrings:  14897
 
Symbols:
+ -[CPLBackgroundDownloadsTask _reportDownloadedTasks]
+ -[CPLEngineForceSyncTask(CPLEngineSyncManagerForcedTask) allowsBackgroundDispatch]
+ -[CPLEngineForceSyncTask(CPLEngineSyncManagerForcedTask) allowsForcedTaskQueuing]
+ -[CPLEngineForceSyncTask(CPLEngineSyncManagerForcedTask) discardedError]
+ -[CPLEngineForceSyncTask(CPLEngineSyncManagerForcedTask) forcedTaskPriority]
+ -[CPLEngineForceSyncTask(CPLEngineSyncManagerForcedTask) simpleDescription]
+ -[CPLEngineScopeCleanupTasks cleanupStepHasMore:deletedCount:error:]
+ -[CPLEngineSyncManager _canLaunchForcedTaskVsOtherForcedTask:otherForcedTask:discardOtherForcedTask:]
+ -[CPLEngineSyncManager _checkForegroundAtLaunchForForcedTask]
+ -[CPLEngineSyncManager _disableSchedulerForForcedTaskIfNecessary]
+ -[CPLEngineSyncManager _discardPendingForcedTasksWithError:]
+ -[CPLEngineSyncManager _forcedTaskDidFinishWithError:]
+ -[CPLEngineSyncManager _launchForcedTaskIfNecessary]
+ -[CPLEngineSyncManager _recordForcedTask:discarded:error:]
+ -[CPLEngineSyncManager _reenableSchedulerForForcedTaskIfNecessary]
+ -[CPLEngineSyncManager cancelScheduledForcedTaskForLaunch:]
+ -[CPLEngineSyncManager scheduleForcedTaskForLaunch:]
+ -[CPLEngineTransientRepository unstashRecordsForScopeWithIdentifier:maxCount:hasMore:unstashedCount:error:]
+ -[CPLPushToTransportScopeTask _launchSubTask:subIdentifier:]
+ -[CPLSyncSessionThroughputMetrics copyWithZone:]
+ -[CPLSyncSessionThroughputMetrics description]
+ -[CPLSyncSessionThroughputMetrics redactedDescription]
+ -[CPLSyncThroughputReporter _beginKindOfWorkIfNecessary:]
+ -[CPLSyncThroughputReporter addCompletedWorkBytesCount:kindOfWork:]
+ -[CPLSyncThroughputReporter beginKindOfWork:]
+ -[CPLSyncThroughputReporter endKindOfWork:]
+ -[CPLUploadPushedChangesTask _finishReportingDerivativesIsNecessary]
+ -[_CPLForcedTaskHistory .cxx_destruct]
+ -[_CPLForcedTaskHistory creationDate]
+ -[_CPLForcedTaskHistory descriptionWithNow:]
+ -[_CPLForcedTaskHistory discarded]
+ -[_CPLForcedTaskHistory errorDescription]
+ -[_CPLForcedTaskHistory initWithForcedTask:discarded:error:]
+ -[_CPLForcedTaskHistory simpleDescription]
+ -[_CPLForcedTaskHistory taskClass]
+ GCC_except_table1011
+ GCC_except_table1013
+ GCC_except_table1186
+ GCC_except_table1234
+ GCC_except_table1239
+ GCC_except_table1243
+ GCC_except_table1251
+ GCC_except_table1260
+ GCC_except_table1263
+ GCC_except_table1266
+ GCC_except_table1272
+ GCC_except_table1274
+ GCC_except_table1355
+ GCC_except_table1441
+ GCC_except_table1989
+ GCC_except_table2096
+ GCC_except_table2104
+ GCC_except_table2145
+ GCC_except_table2233
+ GCC_except_table2240
+ GCC_except_table2383
+ GCC_except_table2472
+ GCC_except_table2708
+ GCC_except_table2710
+ GCC_except_table2796
+ GCC_except_table2861
+ GCC_except_table2863
+ GCC_except_table2983
+ GCC_except_table3007
+ GCC_except_table3083
+ GCC_except_table3087
+ GCC_except_table3089
+ GCC_except_table3091
+ GCC_except_table3095
+ GCC_except_table3216
+ GCC_except_table3263
+ GCC_except_table3507
+ GCC_except_table3576
+ GCC_except_table3580
+ GCC_except_table3582
+ GCC_except_table3591
+ GCC_except_table3871
+ GCC_except_table3901
+ GCC_except_table3928
+ GCC_except_table3945
+ GCC_except_table3952
+ GCC_except_table3960
+ GCC_except_table3962
+ GCC_except_table3976
+ GCC_except_table3978
+ GCC_except_table3981
+ GCC_except_table4318
+ GCC_except_table4362
+ GCC_except_table4450
+ GCC_except_table4460
+ GCC_except_table4517
+ GCC_except_table4520
+ GCC_except_table4695
+ GCC_except_table4703
+ GCC_except_table4783
+ GCC_except_table4787
+ GCC_except_table4793
+ GCC_except_table4800
+ GCC_except_table4815
+ GCC_except_table4816
+ GCC_except_table4822
+ GCC_except_table4866
+ GCC_except_table4874
+ GCC_except_table4934
+ GCC_except_table4936
+ GCC_except_table4938
+ GCC_except_table4950
+ GCC_except_table5092
+ GCC_except_table5134
+ GCC_except_table5143
+ GCC_except_table5144
+ GCC_except_table5203
+ GCC_except_table5206
+ GCC_except_table5286
+ GCC_except_table5323
+ GCC_except_table5489
+ GCC_except_table5517
+ GCC_except_table5559
+ GCC_except_table5579
+ GCC_except_table5605
+ GCC_except_table5616
+ GCC_except_table5637
+ GCC_except_table5657
+ GCC_except_table5661
+ GCC_except_table5687
+ GCC_except_table5719
+ GCC_except_table5759
+ GCC_except_table5818
+ GCC_except_table5859
+ GCC_except_table5872
+ GCC_except_table5883
+ GCC_except_table5890
+ GCC_except_table5943
+ GCC_except_table6068
+ GCC_except_table6081
+ GCC_except_table6084
+ GCC_except_table6564
+ GCC_except_table6607
+ GCC_except_table6630
+ GCC_except_table6638
+ GCC_except_table6648
+ GCC_except_table6656
+ GCC_except_table6659
+ GCC_except_table6679
+ GCC_except_table6686
+ GCC_except_table6709
+ GCC_except_table6743
+ GCC_except_table6767
+ GCC_except_table6778
+ GCC_except_table6796
+ GCC_except_table6799
+ GCC_except_table6801
+ GCC_except_table6803
+ GCC_except_table6836
+ GCC_except_table6911
+ GCC_except_table7057
+ GCC_except_table7079
+ GCC_except_table7109
+ GCC_except_table7292
+ GCC_except_table7301
+ GCC_except_table7306
+ GCC_except_table7322
+ GCC_except_table7336
+ GCC_except_table7346
+ GCC_except_table7351
+ GCC_except_table7433
+ GCC_except_table7531
+ GCC_except_table7540
+ GCC_except_table7596
+ GCC_except_table7616
+ GCC_except_table7622
+ GCC_except_table7644
+ GCC_except_table7652
+ GCC_except_table7674
+ GCC_except_table7684
+ GCC_except_table802
+ GCC_except_table814
+ GCC_except_table907
+ GCC_except_table993
+ _OBJC_CLASS_$__CPLForcedTaskHistory
+ _OBJC_IVAR_$_CPLBackgroundDownloadsTask._countOfFinishedDownloadTasksSinceLastReport
+ _OBJC_IVAR_$_CPLBackgroundDownloadsTask._reportTimer
+ _OBJC_IVAR_$_CPLEngineSyncManager._currentForcedTask
+ _OBJC_IVAR_$_CPLEngineSyncManager._disabledSchedulerForForcedTask
+ _OBJC_IVAR_$_CPLEngineSyncManager._forcedTaskHistory
+ _OBJC_IVAR_$_CPLEngineSyncManager._pendingForcedTasks
+ _OBJC_IVAR_$_CPLUploadPushedChangesTask._derivativesSizeReportTimer
+ _OBJC_IVAR_$_CPLUploadPushedChangesTask._derivativesSizeToReport
+ _OBJC_IVAR_$__CPLForcedTaskHistory._creationDate
+ _OBJC_IVAR_$__CPLForcedTaskHistory._discarded
+ _OBJC_IVAR_$__CPLForcedTaskHistory._errorDescription
+ _OBJC_IVAR_$__CPLForcedTaskHistory._simpleDescription
+ _OBJC_IVAR_$__CPLForcedTaskHistory._taskClass
+ _OBJC_METACLASS_$__CPLForcedTaskHistory
+ __OBJC_$_INSTANCE_METHODS_CPLEngineForceSyncTask(CPLEngineSyncManagerForcedTask)
+ __OBJC_$_INSTANCE_METHODS__CPLForcedTaskHistory
+ __OBJC_$_INSTANCE_VARIABLES__CPLForcedTaskHistory
+ __OBJC_$_PROP_LIST_CPLEngineSyncManagerForcedTask
+ __OBJC_$_PROP_LIST__CPLForcedTaskHistory
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPLEngineSyncManagerForcedTask
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPLEngineSyncManagerForcedTask
+ __OBJC_$_PROTOCOL_REFS_CPLEngineSyncManagerForcedTask
+ __OBJC_CLASS_PROTOCOLS_$_CPLEngineForceSyncTask(CPLEngineSyncManagerForcedTask)
+ __OBJC_CLASS_PROTOCOLS_$_CPLSyncSessionThroughputMetrics
+ __OBJC_CLASS_RO_$__CPLForcedTaskHistory
+ __OBJC_LABEL_PROTOCOL_$_CPLEngineSyncManagerForcedTask
+ __OBJC_METACLASS_RO_$__CPLForcedTaskHistory
+ __OBJC_PROTOCOL_$_CPLEngineSyncManagerForcedTask
+ ___110-[CPLUploadPushedChangesTask _reportRemainingUploadSizeWithReportedUploadedSizes:totalSizesPerRecord:success:]_block_invoke
+ ___110-[CPLUploadPushedChangesTask _reportRemainingUploadSizeWithReportedUploadedSizes:totalSizesPerRecord:success:]_block_invoke_2
+ ___110-[CPLUploadPushedChangesTask _reportRemainingUploadSizeWithReportedUploadedSizes:totalSizesPerRecord:success:]_block_invoke_3
+ ___116-[CPLUploadPushedChangesTask _generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:]_block_invoke.146
+ ___116-[CPLUploadPushedChangesTask _generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:]_block_invoke_2.154
+ ___116-[CPLUploadPushedChangesTask _generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:]_block_invoke_3.155
+ ___148-[CPLUploadPushedChangesTask _reportUploadSizeForRecordWithScopedIdentifier:uploadProgress:reportedUploadedSizes:totalSizesPerRecord:batchToUpload:]_block_invoke
+ ___33-[CPLCleanupTask _doOneIteration]_block_invoke_3
+ ___33-[CPLCleanupTask _doOneIteration]_block_invoke_4
+ ___37-[CPLEngineMultiscopeSyncTask launch]_block_invoke.120
+ ___37-[CPLEngineMultiscopeSyncTask launch]_block_invoke_2.121
+ ___37-[CPLUploadPushedChangesTask cancel:]_block_invoke.193
+ ___38-[CPLPushToTransportScopeTask _launch]_block_invoke.91
+ ___38-[CPLPushToTransportScopeTask _launch]_block_invoke_2.93
+ ___38-[CPLReshareScopeTask _doOneIteration]_block_invoke.19
+ ___46-[CPLMingleChangesScopeTask _mingleRemappings]_block_invoke_5
+ ___46-[CPLMingleChangesScopeTask _mingleRemappings]_block_invoke_6
+ ___48-[CPLMingleChangesScopeTask _mingleOtherChanges]_block_invoke.76
+ ___48-[CPLMingleChangesScopeTask _mingleOtherChanges]_block_invoke_4
+ ___48-[CPLMingleChangesScopeTask _mingleOtherChanges]_block_invoke_5
+ ___49-[CPLBackgroundDownloadsTask _enqueueTasksLocked]_block_invoke.36
+ ___51-[CPLPushToTransportScopeTask _updateContributors:]_block_invoke.70
+ ___52-[CPLBackgroundDownloadsTask _reportDownloadedTasks]_block_invoke
+ ___52-[CPLBackgroundDownloadsTask _reportDownloadedTasks]_block_invoke_2
+ ___52-[CPLEngineSyncManager _launchForcedTaskIfNecessary]_block_invoke
+ ___52-[CPLEngineSyncManager _launchForcedTaskIfNecessary]_block_invoke.270
+ ___52-[CPLEngineSyncManager scheduleForcedTaskForLaunch:]_block_invoke
+ ___53-[CPLBackgroundDownloadsTask taskDidFinishWithError:]_block_invoke
+ ___53-[CPLBackgroundDownloadsTask taskDidFinishWithError:]_block_invoke_2
+ ___53-[CPLMingleChangesScopeTask _unstashRecordsForScope:]_block_invoke_4
+ ___53-[CPLMingleChangesScopeTask _unstashRecordsForScope:]_block_invoke_5
+ ___53-[CPLPullFromTransportScopeTask _launchNextQueryTask]_block_invoke.96
+ ___54-[CPLProcessStagedScopesScopeTask _startActualCleanup]_block_invoke.40
+ ___54-[CPLProcessStagedScopesScopeTask _startActualCleanup]_block_invoke_2.47
+ ___54-[CPLProcessStagedScopesScopeTask _startActualCleanup]_block_invoke_3.48
+ ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke.134
+ ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke.137
+ ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke_2.135
+ ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke_3
+ ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.167
+ ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.174
+ ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.176
+ ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.177
+ ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.178
+ ___56-[CPLEngineSyncManager _setupTaskWithCompletionHandler:]_block_invoke.284
+ ___56-[CPLEngineSyncManager _setupTaskWithCompletionHandler:]_block_invoke_2.286
+ ___56-[CPLPullFromTransportScopeTask _fetchInitialSyncAnchor]_block_invoke.116
+ ___56-[CPLPullFromTransportScopeTask _fetchInitialSyncAnchor]_block_invoke_2.117
+ ___56-[CPLPullFromTransportScopeTask taskDidFinishWithError:]_block_invoke.144
+ ___56-[CPLUploadComputeStatesScopeTask _dropAllComputeStates]_block_invoke.58
+ ___56-[CPLUploadComputeStatesScopeTask _dropAllComputeStates]_block_invoke_3
+ ___56-[CPLUploadComputeStatesScopeTask _dropAllComputeStates]_block_invoke_4
+ ___56-[CPLUploadComputeStatesScopeTask _uploadExtractedBatch]_block_invoke.9
+ ___57-[CPLEngineSyncManager setSyncSessionShouldBeForeground:]_block_invoke.239
+ ___57-[CPLUploadComputeStatesScopeTask _getNextBatchAndUpload]_block_invoke.40
+ ___57-[CPLUploadComputeStatesScopeTask _getNextBatchAndUpload]_block_invoke.41
+ ___57-[CPLUploadComputeStatesScopeTask _getNextBatchAndUpload]_block_invoke.46
+ ___57-[CPLUploadComputeStatesScopeTask _getNextBatchAndUpload]_block_invoke_5
+ ___57-[CPLUploadPushedChangesTask _uploadBatchWithFetchCache:]_block_invoke.100
+ ___58-[CPLUploadComputeStatesScopeTask _requestMissingPayloads]_block_invoke.27
+ ___58-[CPLUploadComputeStatesScopeTask _requestMissingPayloads]_block_invoke.29
+ ___58-[CPLUploadComputeStatesScopeTask _requestMissingPayloads]_block_invoke.30
+ ___58-[CPLUploadComputeStatesScopeTask _requestMissingPayloads]_block_invoke_2.28
+ ___59-[CPLEngineSyncManager cancelScheduledForcedTaskForLaunch:]_block_invoke
+ ___59-[CPLPushToTransportScopeTask _pushTaskDidFinishWithError:]_block_invoke.105
+ ___59-[CPLPushToTransportScopeTask _pushTaskDidFinishWithError:]_block_invoke_2.106
+ ___60-[CPLPushToTransportScopeTask _launchSubTask:subIdentifier:]_block_invoke
+ ___60-[CPLPushToTransportScopeTask _launchSubTask:subIdentifier:]_block_invoke_2
+ ___60-[CPLUploadPushedChangesTask _uploadTaskDidFinishWithError:]_block_invoke.200
+ ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke.118
+ ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke.120
+ ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke_2.121
+ ___67-[CPLPullFromTransportScopeTask _launchPullTasksAndDisableQueries:]_block_invoke.109
+ ___68-[CPLUploadPushedChangesTask _extractBatchWithTransaction:andStore:]_block_invoke.81
+ ___68-[CPLUploadPushedChangesTask _extractBatchWithTransaction:andStore:]_block_invoke.82
+ ___68-[CPLUploadPushedChangesTask _extractBatchWithTransaction:andStore:]_block_invoke_2.83
+ ___68-[CPLUploadPushedChangesTask _extractBatchWithTransaction:andStore:]_block_invoke_3
+ ___68-[CPLUploadPushedChangesTask _extractBatchWithTransaction:andStore:]_block_invoke_3.84
+ ___68-[CPLUploadPushedChangesTask _finishReportingDerivativesIsNecessary]_block_invoke
+ ___68-[CPLUploadPushedChangesTask _finishReportingDerivativesIsNecessary]_block_invoke_2
+ ___69-[CPLProcessStagedScopesScopeTask _checkDestinationAndProcessCleanup]_block_invoke.52
+ ___69-[CPLProcessStagedScopesScopeTask _checkDestinationAndProcessCleanup]_block_invoke.61
+ ___72-[CPLUploadComputeStatesScopeTask _discardExtractedBatchAndGetNextBatch]_block_invoke.55
+ ___72-[CPLUploadComputeStatesScopeTask _discardExtractedBatchAndGetNextBatch]_block_invoke_2.57
+ ___75-[CPLBackgroundDownloadsTask _launchNecessaryDownloadTasksWithTransaction:]_block_invoke_10
+ ___75-[CPLBackgroundDownloadsTask _launchNecessaryDownloadTasksWithTransaction:]_block_invoke_11
+ ___75-[CPLBackgroundDownloadsTask _launchNecessaryDownloadTasksWithTransaction:]_block_invoke_9
+ ___78-[CPLUploadComputeStatesScopeTask _uploadComputeStatesTaskDidFinishWithError:]_block_invoke.66
+ ___78-[CPLUploadComputeStatesScopeTask _uploadComputeStatesTaskDidFinishWithError:]_block_invoke_2.67
+ ___81-[CPLPullFromTransportScopeTask _checkServerFeatureVersionWithCompletionHandler:]_block_invoke.126
+ ___81-[CPLPullFromTransportScopeTask _checkServerFeatureVersionWithCompletionHandler:]_block_invoke.138
+ ___82-[CPLPullFromTransportScopeTask _handleNewBatchFromQuery:newCursor:inTransaction:]_block_invoke_3
+ ___82-[CPLPullFromTransportScopeTask _handleNewBatchFromQuery:newCursor:inTransaction:]_block_invoke_4
+ ___88-[CPLPullFromTransportScopeTask _handleNewBatchFromChanges:newSyncAnchor:inTransaction:]_block_invoke_2
+ ___88-[CPLPullFromTransportScopeTask _handleNewBatchFromChanges:newSyncAnchor:inTransaction:]_block_invoke_3
+ ___90-[CPLPullFromTransportScopeTask _extractAndMingleAssetsIfPossibleFromBatch:inTransaction:]_block_invoke.20
+ ___91-[CPLBackgroundDownloadsTask _completeBackgroundDownloadForResource:error:withTransaction:]_block_invoke.35
+ ___92-[CPLUploadPushedChangesTask _generatingDerivativesForChange:fractionCompleted:chunkLength:]_block_invoke
+ ___92-[CPLUploadPushedChangesTask _generatingDerivativesForChange:fractionCompleted:chunkLength:]_block_invoke_2
+ ___94-[CPLPullScopesTask _handleChangedOrNewScopes:deletedScopeIdentifiers:newScopeListSyncAnchor:]_block_invoke.12
+ ___94-[CPLPullScopesTask _handleChangedOrNewScopes:deletedScopeIdentifiers:newScopeListSyncAnchor:]_block_invoke.8
+ ___94-[CPLPullScopesTask _handleChangedOrNewScopes:deletedScopeIdentifiers:newScopeListSyncAnchor:]_block_invoke_3
+ ___94-[CPLPullScopesTask _handleChangedOrNewScopes:deletedScopeIdentifiers:newScopeListSyncAnchor:]_block_invoke_4
+ ___Block_byref_object_copy_.10074
+ ___Block_byref_object_copy_.11308
+ ___Block_byref_object_copy_.11603
+ ___Block_byref_object_copy_.12365
+ ___Block_byref_object_copy_.13185
+ ___Block_byref_object_copy_.13766
+ ___Block_byref_object_copy_.14097
+ ___Block_byref_object_copy_.14283
+ ___Block_byref_object_copy_.15115
+ ___Block_byref_object_copy_.15731
+ ___Block_byref_object_copy_.16455
+ ___Block_byref_object_copy_.16777
+ ___Block_byref_object_copy_.17251
+ ___Block_byref_object_copy_.1734
+ ___Block_byref_object_copy_.17850
+ ___Block_byref_object_copy_.18672
+ ___Block_byref_object_copy_.20145
+ ___Block_byref_object_copy_.20284
+ ___Block_byref_object_copy_.2046
+ ___Block_byref_object_copy_.20791
+ ___Block_byref_object_copy_.21406
+ ___Block_byref_object_copy_.21902
+ ___Block_byref_object_copy_.22239
+ ___Block_byref_object_copy_.23256
+ ___Block_byref_object_copy_.23558
+ ___Block_byref_object_copy_.24365
+ ___Block_byref_object_copy_.2535
+ ___Block_byref_object_copy_.2613
+ ___Block_byref_object_copy_.2938
+ ___Block_byref_object_copy_.3256
+ ___Block_byref_object_copy_.5793
+ ___Block_byref_object_copy_.6496
+ ___Block_byref_object_copy_.6659
+ ___Block_byref_object_copy_.7326
+ ___Block_byref_object_copy_.7704
+ ___Block_byref_object_copy_.7991
+ ___Block_byref_object_copy_.8424
+ ___Block_byref_object_copy_.9829
+ ___Block_byref_object_dispose_.10075
+ ___Block_byref_object_dispose_.11309
+ ___Block_byref_object_dispose_.11604
+ ___Block_byref_object_dispose_.12366
+ ___Block_byref_object_dispose_.13186
+ ___Block_byref_object_dispose_.13767
+ ___Block_byref_object_dispose_.14098
+ ___Block_byref_object_dispose_.14284
+ ___Block_byref_object_dispose_.15116
+ ___Block_byref_object_dispose_.15732
+ ___Block_byref_object_dispose_.16456
+ ___Block_byref_object_dispose_.16778
+ ___Block_byref_object_dispose_.17252
+ ___Block_byref_object_dispose_.1735
+ ___Block_byref_object_dispose_.17851
+ ___Block_byref_object_dispose_.18673
+ ___Block_byref_object_dispose_.20146
+ ___Block_byref_object_dispose_.20285
+ ___Block_byref_object_dispose_.2047
+ ___Block_byref_object_dispose_.20792
+ ___Block_byref_object_dispose_.21407
+ ___Block_byref_object_dispose_.21903
+ ___Block_byref_object_dispose_.22240
+ ___Block_byref_object_dispose_.23257
+ ___Block_byref_object_dispose_.23559
+ ___Block_byref_object_dispose_.24366
+ ___Block_byref_object_dispose_.2536
+ ___Block_byref_object_dispose_.2614
+ ___Block_byref_object_dispose_.2939
+ ___Block_byref_object_dispose_.3257
+ ___Block_byref_object_dispose_.5794
+ ___Block_byref_object_dispose_.6497
+ ___Block_byref_object_dispose_.6660
+ ___Block_byref_object_dispose_.7327
+ ___Block_byref_object_dispose_.7705
+ ___Block_byref_object_dispose_.7992
+ ___Block_byref_object_dispose_.8425
+ ___Block_byref_object_dispose_.9830
+ ___CPLConfigurationOSLogDomain.19507
+ ___CPLConfigurationOSLogDomain.onceToken.19513
+ ___CPLConfigurationOSLogDomain.result.19515
+ ___CPLForcedOSLogDomain
+ ___CPLForcedOSLogDomain.onceToken
+ ___CPLForcedOSLogDomain.result
+ ___CPLSchedulerOSLogDomain.7652
+ ___CPLSchedulerOSLogDomain.onceToken.7653
+ ___CPLSchedulerOSLogDomain.result.7654
+ ___CPLSessionOSLogDomain.16326
+ ___CPLSessionOSLogDomain.18233
+ ___CPLSessionOSLogDomain.22842
+ ___CPLSessionOSLogDomain.onceToken.16328
+ ___CPLSessionOSLogDomain.onceToken.18238
+ ___CPLSessionOSLogDomain.onceToken.22844
+ ___CPLSessionOSLogDomain.result.16329
+ ___CPLSessionOSLogDomain.result.18239
+ ___CPLSessionOSLogDomain.result.22846
+ ___CPLStorageOSLogDomain.11276
+ ___CPLStorageOSLogDomain.11361
+ ___CPLStorageOSLogDomain.17818
+ ___CPLStorageOSLogDomain.2026
+ ___CPLStorageOSLogDomain.20264
+ ___CPLStorageOSLogDomain.21557
+ ___CPLStorageOSLogDomain.22226
+ ___CPLStorageOSLogDomain.22474
+ ___CPLStorageOSLogDomain.6249
+ ___CPLStorageOSLogDomain.7941
+ ___CPLStorageOSLogDomain.8676
+ ___CPLStorageOSLogDomain.9118
+ ___CPLStorageOSLogDomain.9284
+ ___CPLStorageOSLogDomain.9477
+ ___CPLStorageOSLogDomain.onceToken.11287
+ ___CPLStorageOSLogDomain.onceToken.11364
+ ___CPLStorageOSLogDomain.onceToken.14635
+ ___CPLStorageOSLogDomain.onceToken.17820
+ ___CPLStorageOSLogDomain.onceToken.20266
+ ___CPLStorageOSLogDomain.onceToken.2028
+ ___CPLStorageOSLogDomain.onceToken.20545
+ ___CPLStorageOSLogDomain.onceToken.21561
+ ___CPLStorageOSLogDomain.onceToken.22231
+ ___CPLStorageOSLogDomain.onceToken.22482
+ ___CPLStorageOSLogDomain.onceToken.6251
+ ___CPLStorageOSLogDomain.onceToken.7943
+ ___CPLStorageOSLogDomain.onceToken.8684
+ ___CPLStorageOSLogDomain.onceToken.9124
+ ___CPLStorageOSLogDomain.onceToken.9286
+ ___CPLStorageOSLogDomain.onceToken.9479
+ ___CPLStorageOSLogDomain.result.11289
+ ___CPLStorageOSLogDomain.result.11366
+ ___CPLStorageOSLogDomain.result.14637
+ ___CPLStorageOSLogDomain.result.17822
+ ___CPLStorageOSLogDomain.result.20268
+ ___CPLStorageOSLogDomain.result.2030
+ ___CPLStorageOSLogDomain.result.20546
+ ___CPLStorageOSLogDomain.result.21563
+ ___CPLStorageOSLogDomain.result.22233
+ ___CPLStorageOSLogDomain.result.22484
+ ___CPLStorageOSLogDomain.result.6253
+ ___CPLStorageOSLogDomain.result.7944
+ ___CPLStorageOSLogDomain.result.8685
+ ___CPLStorageOSLogDomain.result.9126
+ ___CPLStorageOSLogDomain.result.9287
+ ___CPLStorageOSLogDomain.result.9480
+ ___CPLStoreOSLogDomain.3044
+ ___CPLStoreOSLogDomain.onceToken.3045
+ ___CPLStoreOSLogDomain.result.3046
+ ___CPLTaskOSLogDomain.11549
+ ___CPLTaskOSLogDomain.14066
+ ___CPLTaskOSLogDomain.14540
+ ___CPLTaskOSLogDomain.15619
+ ___CPLTaskOSLogDomain.17161
+ ___CPLTaskOSLogDomain.21353
+ ___CPLTaskOSLogDomain.23183
+ ___CPLTaskOSLogDomain.24321
+ ___CPLTaskOSLogDomain.2598
+ ___CPLTaskOSLogDomain.5477
+ ___CPLTaskOSLogDomain.7245
+ ___CPLTaskOSLogDomain.onceToken.11584
+ ___CPLTaskOSLogDomain.onceToken.1357
+ ___CPLTaskOSLogDomain.onceToken.14068
+ ___CPLTaskOSLogDomain.onceToken.14542
+ ___CPLTaskOSLogDomain.onceToken.15631
+ ___CPLTaskOSLogDomain.onceToken.17168
+ ___CPLTaskOSLogDomain.onceToken.21395
+ ___CPLTaskOSLogDomain.onceToken.23194
+ ___CPLTaskOSLogDomain.onceToken.24329
+ ___CPLTaskOSLogDomain.onceToken.2600
+ ___CPLTaskOSLogDomain.onceToken.5484
+ ___CPLTaskOSLogDomain.onceToken.7260
+ ___CPLTaskOSLogDomain.result.11586
+ ___CPLTaskOSLogDomain.result.1358
+ ___CPLTaskOSLogDomain.result.14070
+ ___CPLTaskOSLogDomain.result.14544
+ ___CPLTaskOSLogDomain.result.15632
+ ___CPLTaskOSLogDomain.result.17169
+ ___CPLTaskOSLogDomain.result.21396
+ ___CPLTaskOSLogDomain.result.23195
+ ___CPLTaskOSLogDomain.result.24330
+ ___CPLTaskOSLogDomain.result.2602
+ ___CPLTaskOSLogDomain.result.5486
+ ___CPLTaskOSLogDomain.result.7262
+ _____CPLConfigurationOSLogDomain_block_invoke.19518
+ _____CPLForcedOSLogDomain_block_invoke
+ _____CPLSchedulerOSLogDomain_block_invoke.7656
+ _____CPLSessionOSLogDomain_block_invoke.16331
+ _____CPLSessionOSLogDomain_block_invoke.18241
+ _____CPLSessionOSLogDomain_block_invoke.22849
+ _____CPLStorageOSLogDomain_block_invoke.11292
+ _____CPLStorageOSLogDomain_block_invoke.11369
+ _____CPLStorageOSLogDomain_block_invoke.14642
+ _____CPLStorageOSLogDomain_block_invoke.17825
+ _____CPLStorageOSLogDomain_block_invoke.20271
+ _____CPLStorageOSLogDomain_block_invoke.2033
+ _____CPLStorageOSLogDomain_block_invoke.20552
+ _____CPLStorageOSLogDomain_block_invoke.21566
+ _____CPLStorageOSLogDomain_block_invoke.22236
+ _____CPLStorageOSLogDomain_block_invoke.22487
+ _____CPLStorageOSLogDomain_block_invoke.6256
+ _____CPLStorageOSLogDomain_block_invoke.7946
+ _____CPLStorageOSLogDomain_block_invoke.8687
+ _____CPLStorageOSLogDomain_block_invoke.9129
+ _____CPLStorageOSLogDomain_block_invoke.9289
+ _____CPLStorageOSLogDomain_block_invoke.9482
+ _____CPLStoreOSLogDomain_block_invoke.3048
+ _____CPLTaskOSLogDomain_block_invoke.11589
+ _____CPLTaskOSLogDomain_block_invoke.1360
+ _____CPLTaskOSLogDomain_block_invoke.14073
+ _____CPLTaskOSLogDomain_block_invoke.14547
+ _____CPLTaskOSLogDomain_block_invoke.15634
+ _____CPLTaskOSLogDomain_block_invoke.17171
+ _____CPLTaskOSLogDomain_block_invoke.21398
+ _____CPLTaskOSLogDomain_block_invoke.23197
+ _____CPLTaskOSLogDomain_block_invoke.24332
+ _____CPLTaskOSLogDomain_block_invoke.2605
+ _____CPLTaskOSLogDomain_block_invoke.5489
+ _____CPLTaskOSLogDomain_block_invoke.7265
+ ___block_descriptor_40_e8_32r_e35_v16?0"CPLSyncThroughputReporter"8lr32l8
+ ___block_descriptor_40_e8_32s_e11_v24?0Q8Q16ls32l8
+ ___block_descriptor_40_e8_32s_e35_v16?0"CPLSyncThroughputReporter"8ls32l8
+ ___block_descriptor_40_e8_32s_e49_v32?0"<CPLEngineSyncManagerForcedTask>"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e46_v32?0"CPLScopedIdentifier"8"NSNumber"16^B24ls32l8r40l8
+ ___block_descriptor_56_e8_32s40bs48w_e54_v24?0"<CPLEngineSyncManagerForcedTask>"8"NSError"16lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40r_e42_v20?0"CPLEngineResourceDownloadTask"8f16lr40l8s32l8
+ ___block_descriptor_64_e8_32s40s48s56s_e32_v20?0"CPLScopedIdentifier"8f16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e9_B16?0^8ls32l8s40l8r64l8s48l8s56l8
+ ___block_descriptor_76_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72r_e51_v24?0"CPLEngineResourceDownloadTask"8"NSError"16lr72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_89_e8_32s40s48s56r64r72r80r_e9_B16?0^8lr56l8s32l8s40l8s48l8r64l8r72l8r80l8
+ ___block_literal_global.101.14543
+ ___block_literal_global.10178
+ ___block_literal_global.10499
+ ___block_literal_global.105.19030
+ ___block_literal_global.10895
+ ___block_literal_global.110.21078
+ ___block_literal_global.11134
+ ___block_literal_global.11288
+ ___block_literal_global.11365
+ ___block_literal_global.11585
+ ___block_literal_global.12.8065
+ ___block_literal_global.12486
+ ___block_literal_global.127
+ ___block_literal_global.12709
+ ___block_literal_global.128
+ ___block_literal_global.128.24489
+ ___block_literal_global.13206
+ ___block_literal_global.133
+ ___block_literal_global.136
+ ___block_literal_global.1398
+ ___block_literal_global.14.14578
+ ___block_literal_global.14069
+ ___block_literal_global.142.21082
+ ___block_literal_global.14331
+ ___block_literal_global.14577
+ ___block_literal_global.14636
+ ___block_literal_global.14799
+ ___block_literal_global.1481
+ ___block_literal_global.15332
+ ___block_literal_global.15352
+ ___block_literal_global.15417
+ ___block_literal_global.1561
+ ___block_literal_global.15642
+ ___block_literal_global.159.21083
+ ___block_literal_global.16.15626
+ ___block_literal_global.16181
+ ___block_literal_global.16396
+ ___block_literal_global.16956
+ ___block_literal_global.171.21084
+ ___block_literal_global.17273
+ ___block_literal_global.1731
+ ___block_literal_global.17615
+ ___block_literal_global.17821
+ ___block_literal_global.18251
+ ___block_literal_global.18422
+ ___block_literal_global.18560
+ ___block_literal_global.1864
+ ___block_literal_global.1899
+ ___block_literal_global.19144
+ ___block_literal_global.19514
+ ___block_literal_global.19898
+ ___block_literal_global.20267
+ ___block_literal_global.2029
+ ___block_literal_global.20432
+ ___block_literal_global.20548
+ ___block_literal_global.21074
+ ___block_literal_global.21413
+ ___block_literal_global.21562
+ ___block_literal_global.21736
+ ___block_literal_global.22232
+ ___block_literal_global.22483
+ ___block_literal_global.22643
+ ___block_literal_global.22845
+ ___block_literal_global.22996
+ ___block_literal_global.2300
+ ___block_literal_global.23252
+ ___block_literal_global.23867
+ ___block_literal_global.24.14285
+ ___block_literal_global.24003
+ ___block_literal_global.24075
+ ___block_literal_global.24513
+ ___block_literal_global.24627
+ ___block_literal_global.24746
+ ___block_literal_global.2476
+ ___block_literal_global.24931
+ ___block_literal_global.2534
+ ___block_literal_global.260
+ ___block_literal_global.2601
+ ___block_literal_global.27.16415
+ ___block_literal_global.270
+ ___block_literal_global.2955
+ ___block_literal_global.3023
+ ___block_literal_global.32.22611
+ ___block_literal_global.3285
+ ___block_literal_global.33.7376
+ ___block_literal_global.34.10071
+ ___block_literal_global.34.2473
+ ___block_literal_global.3558
+ ___block_literal_global.37.10815
+ ___block_literal_global.3794
+ ___block_literal_global.4031
+ ___block_literal_global.42.8072
+ ___block_literal_global.4468
+ ___block_literal_global.459
+ ___block_literal_global.4605
+ ___block_literal_global.4817
+ ___block_literal_global.5.24640
+ ___block_literal_global.50.7367
+ ___block_literal_global.5265
+ ___block_literal_global.5342
+ ___block_literal_global.54.5238
+ ___block_literal_global.5485
+ ___block_literal_global.5626
+ ___block_literal_global.57.8076
+ ___block_literal_global.6.15640
+ ___block_literal_global.6164
+ ___block_literal_global.6252
+ ___block_literal_global.6472
+ ___block_literal_global.6768
+ ___block_literal_global.705
+ ___block_literal_global.708
+ ___block_literal_global.711
+ ___block_literal_global.72.16914
+ ___block_literal_global.7261
+ ___block_literal_global.7375
+ ___block_literal_global.77.16176
+ ___block_literal_global.7774
+ ___block_literal_global.8062
+ ___block_literal_global.8807
+ ___block_literal_global.9018
+ ___block_literal_global.91
+ ___block_literal_global.9125
+ ___block_literal_global.9223
+ ___block_literal_global.93.19035
+ ___block_literal_global.93.7838
+ ___block_literal_global.9528
+ ___block_literal_global.96
+ ___block_literal_global.9700
+ ___block_literal_global.9970
+ ___cpl_dispatch_async_block_invoke.10155
+ ___cpl_dispatch_async_block_invoke.11545
+ ___cpl_dispatch_async_block_invoke.12187
+ ___cpl_dispatch_async_block_invoke.1362
+ ___cpl_dispatch_async_block_invoke.14078
+ ___cpl_dispatch_async_block_invoke.14456
+ ___cpl_dispatch_async_block_invoke.14533
+ ___cpl_dispatch_async_block_invoke.15717
+ ___cpl_dispatch_async_block_invoke.16734
+ ___cpl_dispatch_async_block_invoke.17228
+ ___cpl_dispatch_async_block_invoke.17572
+ ___cpl_dispatch_async_block_invoke.18058
+ ___cpl_dispatch_async_block_invoke.1813
+ ___cpl_dispatch_async_block_invoke.18556
+ ___cpl_dispatch_async_block_invoke.19493
+ ___cpl_dispatch_async_block_invoke.20778
+ ___cpl_dispatch_async_block_invoke.21351
+ ___cpl_dispatch_async_block_invoke.21744
+ ___cpl_dispatch_async_block_invoke.22998
+ ___cpl_dispatch_async_block_invoke.23200
+ ___cpl_dispatch_async_block_invoke.24374
+ ___cpl_dispatch_async_block_invoke.2942
+ ___cpl_dispatch_async_block_invoke.6711
+ ___cpl_dispatch_async_block_invoke.7243
+ ___cpl_dispatch_async_block_invoke.7515
+ ___cpl_dispatch_async_block_invoke.7952
+ ___cpl_dispatch_async_block_invoke.9813
+ __doProtected:.onceToken.15351
+ __doProtected:.onceToken.22995
+ __doProtected:.queue.22997
+ __statusDidChange.12383
+ _copyDerivativesFromRecordIfPossible:.originalDerivativesImageAndVideo.19054
+ _initWithCoder:.logOnceToken.20434
+ _initWithCoder:.onceToken.10839
+ _initWithCoder:.onceToken.14330
+ _initWithCoder:.onceToken.18250
+ _initWithCoder:.onceToken.20431
+ _initWithCoder:.onceToken.22642
+ _initWithCoder:.onceToken.24930
+ _initWithCoder:.onceToken.5237
+ _initWithCoder:.onceToken.5341
+ _initWithCoder:.onceToken.6467
+ _initWithCoder:.pushContextsClasses.22644
+ _initWithCoder:.stringClass.10840
+ _objc_msgSend$_checkForegroundAtLaunchForForcedTask
+ _objc_msgSend$_disableSchedulerForForcedTaskIfNecessary
+ _objc_msgSend$_discardPendingForcedTasksWithError:
+ _objc_msgSend$_finishReportingDerivativesIsNecessary
+ _objc_msgSend$_forcedTaskDidFinishWithError:
+ _objc_msgSend$_launchForcedTaskIfNecessary
+ _objc_msgSend$_launchSubTask:subIdentifier:
+ _objc_msgSend$_recordForcedTask:discarded:error:
+ _objc_msgSend$_reenableSchedulerForForcedTaskIfNecessary
+ _objc_msgSend$_reportDownloadedTasks
+ _objc_msgSend$addCompletedWorkBytesCount:kindOfWork:
+ _objc_msgSend$allowsBackgroundDispatch
+ _objc_msgSend$allowsForcedTaskQueuing
+ _objc_msgSend$beginKindOfWork:
+ _objc_msgSend$cancelScheduledForcedTaskForLaunch:
+ _objc_msgSend$cleanupStepHasMore:deletedCount:error:
+ _objc_msgSend$discardedError
+ _objc_msgSend$endKindOfWork:
+ _objc_msgSend$forcedTaskPriority
+ _objc_msgSend$initWithForcedTask:discarded:error:
+ _objc_msgSend$realResourceSize
+ _objc_msgSend$scheduleForcedTaskForLaunch:
+ _objc_msgSend$unstashRecordsForScopeWithIdentifier:maxCount:hasMore:unstashedCount:error:
+ _propertiesForChangeType:.onceToken.15187
+ _propertiesForChangeType:.onceToken.19068
+ _propertiesForChangeType:.onceToken.24002
+ _propertiesForChangeType:.properties.24004
- -[CPLEngineScopeCleanupTasks cleanupStepHasMore:error:]
- -[CPLEngineSyncManager _checkForegroundAtLaunchForForceSyncTask]
- -[CPLEngineSyncManager _disableSchedulerForForceSyncTaskIfNecessary]
- -[CPLEngineSyncManager _discardPendingForceSyncTaskWithError:]
- -[CPLEngineSyncManager _forceSyncTaskDidFinishWithError:]
- -[CPLEngineSyncManager _launchForceSyncTaskIfNecessary]
- -[CPLEngineSyncManager _recordForcedSyncTask:discarded:error:]
- -[CPLEngineSyncManager _reenableSchedulerForForceSyncTaskIfNecessary]
- -[CPLEngineTransientRepository unstashRecordsForScopeWithIdentifier:maxCount:hasMore:error:]
- -[CPLPushToTransportScopeTask _launchSubTask:]
- -[CPLUploadPushedChangesTask _extractBatchWithTransaction:andStore:]
- -[CPLUploadPushedChangesTask _shouldUploadBatchesWithDropReason:shouldQuarantineRecords:inTransaction:]
- -[_CPLForcedSyncHistory .cxx_destruct]
- -[_CPLForcedSyncHistory creationDate]
- -[_CPLForcedSyncHistory descriptionWithNow:]
- -[_CPLForcedSyncHistory discarded]
- -[_CPLForcedSyncHistory errorDescription]
- -[_CPLForcedSyncHistory filter]
- -[_CPLForcedSyncHistory initWithForcedSyncTask:discarded:error:]
- -[_CPLForcedSyncHistory taskClass]
- GCC_except_table1006
- GCC_except_table1008
- GCC_except_table1180
- GCC_except_table1227
- GCC_except_table1232
- GCC_except_table1236
- GCC_except_table1244
- GCC_except_table1246
- GCC_except_table1256
- GCC_except_table1259
- GCC_except_table1265
- GCC_except_table1267
- GCC_except_table1348
- GCC_except_table1434
- GCC_except_table1982
- GCC_except_table2089
- GCC_except_table2095
- GCC_except_table2136
- GCC_except_table2224
- GCC_except_table2231
- GCC_except_table2374
- GCC_except_table2463
- GCC_except_table2688
- GCC_except_table2690
- GCC_except_table2776
- GCC_except_table2841
- GCC_except_table2843
- GCC_except_table2963
- GCC_except_table2987
- GCC_except_table3063
- GCC_except_table3067
- GCC_except_table3069
- GCC_except_table3071
- GCC_except_table3075
- GCC_except_table3196
- GCC_except_table3243
- GCC_except_table3487
- GCC_except_table3556
- GCC_except_table3560
- GCC_except_table3562
- GCC_except_table3571
- GCC_except_table3851
- GCC_except_table3881
- GCC_except_table3908
- GCC_except_table3925
- GCC_except_table3932
- GCC_except_table3940
- GCC_except_table3942
- GCC_except_table3956
- GCC_except_table3958
- GCC_except_table3961
- GCC_except_table4298
- GCC_except_table4342
- GCC_except_table4430
- GCC_except_table4440
- GCC_except_table4497
- GCC_except_table4500
- GCC_except_table4675
- GCC_except_table4683
- GCC_except_table4763
- GCC_except_table4767
- GCC_except_table4771
- GCC_except_table4776
- GCC_except_table4791
- GCC_except_table4792
- GCC_except_table4796
- GCC_except_table4840
- GCC_except_table4848
- GCC_except_table4903
- GCC_except_table4905
- GCC_except_table4907
- GCC_except_table4919
- GCC_except_table5058
- GCC_except_table5100
- GCC_except_table5109
- GCC_except_table5110
- GCC_except_table5169
- GCC_except_table5172
- GCC_except_table5252
- GCC_except_table5254
- GCC_except_table5454
- GCC_except_table5482
- GCC_except_table5524
- GCC_except_table5544
- GCC_except_table5570
- GCC_except_table5581
- GCC_except_table5602
- GCC_except_table5622
- GCC_except_table5626
- GCC_except_table5652
- GCC_except_table5684
- GCC_except_table5724
- GCC_except_table5783
- GCC_except_table5824
- GCC_except_table5837
- GCC_except_table5848
- GCC_except_table5855
- GCC_except_table5908
- GCC_except_table6033
- GCC_except_table6046
- GCC_except_table6049
- GCC_except_table6529
- GCC_except_table6568
- GCC_except_table6572
- GCC_except_table6574
- GCC_except_table6589
- GCC_except_table6595
- GCC_except_table6613
- GCC_except_table6621
- GCC_except_table6651
- GCC_except_table6674
- GCC_except_table6708
- GCC_except_table6732
- GCC_except_table6741
- GCC_except_table6759
- GCC_except_table6762
- GCC_except_table6764
- GCC_except_table6766
- GCC_except_table6798
- GCC_except_table6868
- GCC_except_table7013
- GCC_except_table7035
- GCC_except_table7065
- GCC_except_table7248
- GCC_except_table7257
- GCC_except_table7262
- GCC_except_table7276
- GCC_except_table7290
- GCC_except_table7300
- GCC_except_table7305
- GCC_except_table7386
- GCC_except_table7487
- GCC_except_table7496
- GCC_except_table7552
- GCC_except_table7590
- GCC_except_table7606
- GCC_except_table7614
- GCC_except_table7615
- GCC_except_table7629
- GCC_except_table800
- GCC_except_table811
- GCC_except_table902
- GCC_except_table988
- _OBJC_CLASS_$__CPLForcedSyncHistory
- _OBJC_IVAR_$_CPLBackgroundDownloadsTask._total
- _OBJC_IVAR_$_CPLEngineSyncManager._currentForceSyncTask
- _OBJC_IVAR_$_CPLEngineSyncManager._disabledSchedulerForForceSyncTask
- _OBJC_IVAR_$_CPLEngineSyncManager._forcedSyncHistory
- _OBJC_IVAR_$_CPLEngineSyncManager._pendingForceSyncTask
- _OBJC_IVAR_$__CPLForcedSyncHistory._creationDate
- _OBJC_IVAR_$__CPLForcedSyncHistory._discarded
- _OBJC_IVAR_$__CPLForcedSyncHistory._errorDescription
- _OBJC_IVAR_$__CPLForcedSyncHistory._filter
- _OBJC_IVAR_$__CPLForcedSyncHistory._taskClass
- _OBJC_METACLASS_$__CPLForcedSyncHistory
- __OBJC_$_INSTANCE_METHODS_CPLEngineForceSyncTask
- __OBJC_$_INSTANCE_METHODS__CPLForcedSyncHistory
- __OBJC_$_INSTANCE_VARIABLES__CPLForcedSyncHistory
- __OBJC_$_PROP_LIST_CPLEngineForceSyncTask
- __OBJC_$_PROP_LIST__CPLForcedSyncHistory
- __OBJC_CLASS_PROTOCOLS_$_CPLEngineForceSyncTask
- __OBJC_CLASS_RO_$__CPLForcedSyncHistory
- __OBJC_METACLASS_RO_$__CPLForcedSyncHistory
- ___116-[CPLUploadPushedChangesTask _generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:]_block_invoke.124
- ___116-[CPLUploadPushedChangesTask _generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:]_block_invoke_2.132
- ___37-[CPLEngineMultiscopeSyncTask launch]_block_invoke.117
- ___37-[CPLEngineMultiscopeSyncTask launch]_block_invoke_2.118
- ___37-[CPLUploadPushedChangesTask cancel:]_block_invoke.172
- ___38-[CPLPushToTransportScopeTask _launch]_block_invoke.88
- ___38-[CPLPushToTransportScopeTask _launch]_block_invoke_2.90
- ___46-[CPLPushToTransportScopeTask _launchSubTask:]_block_invoke
- ___46-[CPLPushToTransportScopeTask _launchSubTask:]_block_invoke_2
- ___48-[CPLMingleChangesScopeTask _mingleOtherChanges]_block_invoke.72
- ___49-[CPLBackgroundDownloadsTask _enqueueTasksLocked]_block_invoke.31
- ___51-[CPLPushToTransportScopeTask _updateContributors:]_block_invoke.67
- ___53-[CPLEngineSyncManager forceSyncTaskHasBeenLaunched:]_block_invoke
- ___53-[CPLPullFromTransportScopeTask _launchNextQueryTask]_block_invoke.99
- ___54-[CPLEngineSyncManager forceSyncTaskHasBeenCancelled:]_block_invoke
- ___54-[CPLProcessStagedScopesScopeTask _startActualCleanup]_block_invoke.41
- ___54-[CPLProcessStagedScopesScopeTask _startActualCleanup]_block_invoke_2.42
- ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke.126
- ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke.129
- ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke_2.127
- ___55-[CPLEngineSyncManager _launchForceSyncTaskIfNecessary]_block_invoke
- ___55-[CPLEngineSyncManager _launchForceSyncTaskIfNecessary]_block_invoke.265
- ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.144
- ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.155
- ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.157
- ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.158
- ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.159
- ___56-[CPLEngineSyncManager _setupTaskWithCompletionHandler:]_block_invoke.279
- ___56-[CPLEngineSyncManager _setupTaskWithCompletionHandler:]_block_invoke_2.281
- ___56-[CPLPullFromTransportScopeTask _fetchInitialSyncAnchor]_block_invoke.117
- ___56-[CPLPullFromTransportScopeTask _fetchInitialSyncAnchor]_block_invoke_2.118
- ___56-[CPLPullFromTransportScopeTask addCountOfPulledAssets:]_block_invoke
- ___56-[CPLPullFromTransportScopeTask taskDidFinishWithError:]_block_invoke.145
- ___56-[CPLUploadComputeStatesScopeTask _dropAllComputeStates]_block_invoke.41
- ___57-[CPLUploadComputeStatesScopeTask _getNextBatchAndUpload]_block_invoke.30
- ___57-[CPLUploadComputeStatesScopeTask _getNextBatchAndUpload]_block_invoke.31
- ___57-[CPLUploadComputeStatesScopeTask _getNextBatchAndUpload]_block_invoke.36
- ___58-[CPLUploadComputeStatesScopeTask _requestMissingPayloads]_block_invoke.21
- ___58-[CPLUploadComputeStatesScopeTask _requestMissingPayloads]_block_invoke.23
- ___58-[CPLUploadComputeStatesScopeTask _requestMissingPayloads]_block_invoke_2.22
- ___59-[CPLPushToTransportScopeTask _pushTaskDidFinishWithError:]_block_invoke.102
- ___59-[CPLPushToTransportScopeTask _pushTaskDidFinishWithError:]_block_invoke_2.103
- ___60-[CPLUploadPushedChangesTask _uploadTaskDidFinishWithError:]_block_invoke.179
- ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke.115
- ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke.117
- ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke_2.118
- ___67-[CPLPullFromTransportScopeTask _launchPullTasksAndDisableQueries:]_block_invoke.113
- ___68-[CPLUploadPushedChangesTask _extractBatchWithTransaction:andStore:]_block_invoke.77
- ___68-[CPLUploadPushedChangesTask _extractBatchWithTransaction:andStore:]_block_invoke.78
- ___68-[CPLUploadPushedChangesTask _extractBatchWithTransaction:andStore:]_block_invoke_2.79
- ___69-[CPLProcessStagedScopesScopeTask _checkDestinationAndProcessCleanup]_block_invoke.46
- ___69-[CPLProcessStagedScopesScopeTask _checkDestinationAndProcessCleanup]_block_invoke.55
- ___72-[CPLUploadComputeStatesScopeTask _discardExtractedBatchAndGetNextBatch]_block_invoke.38
- ___72-[CPLUploadComputeStatesScopeTask _discardExtractedBatchAndGetNextBatch]_block_invoke_2.40
- ___78-[CPLUploadComputeStatesScopeTask _uploadComputeStatesTaskDidFinishWithError:]_block_invoke.49
- ___78-[CPLUploadComputeStatesScopeTask _uploadComputeStatesTaskDidFinishWithError:]_block_invoke_2.50
- ___81-[CPLPullFromTransportScopeTask _checkServerFeatureVersionWithCompletionHandler:]_block_invoke.127
- ___81-[CPLPullFromTransportScopeTask _checkServerFeatureVersionWithCompletionHandler:]_block_invoke.139
- ___90-[CPLPullFromTransportScopeTask _extractAndMingleAssetsIfPossibleFromBatch:inTransaction:]_block_invoke.25
- ___91-[CPLBackgroundDownloadsTask _completeBackgroundDownloadForResource:error:withTransaction:]_block_invoke.30
- ___94-[CPLPullScopesTask _handleChangedOrNewScopes:deletedScopeIdentifiers:newScopeListSyncAnchor:]_block_invoke.3
- ___94-[CPLPullScopesTask _handleChangedOrNewScopes:deletedScopeIdentifiers:newScopeListSyncAnchor:]_block_invoke.7
- ___Block_byref_object_copy_.10004
- ___Block_byref_object_copy_.11238
- ___Block_byref_object_copy_.11533
- ___Block_byref_object_copy_.12293
- ___Block_byref_object_copy_.13111
- ___Block_byref_object_copy_.13691
- ___Block_byref_object_copy_.14017
- ___Block_byref_object_copy_.14204
- ___Block_byref_object_copy_.15021
- ___Block_byref_object_copy_.15629
- ___Block_byref_object_copy_.16355
- ___Block_byref_object_copy_.16677
- ___Block_byref_object_copy_.17148
- ___Block_byref_object_copy_.1744
- ___Block_byref_object_copy_.17750
- ___Block_byref_object_copy_.18573
- ___Block_byref_object_copy_.20046
- ___Block_byref_object_copy_.20186
- ___Block_byref_object_copy_.2053
- ___Block_byref_object_copy_.20698
- ___Block_byref_object_copy_.21312
- ___Block_byref_object_copy_.21794
- ___Block_byref_object_copy_.22132
- ___Block_byref_object_copy_.23148
- ___Block_byref_object_copy_.23449
- ___Block_byref_object_copy_.24285
- ___Block_byref_object_copy_.2541
- ___Block_byref_object_copy_.2619
- ___Block_byref_object_copy_.2940
- ___Block_byref_object_copy_.3257
- ___Block_byref_object_copy_.5773
- ___Block_byref_object_copy_.6478
- ___Block_byref_object_copy_.6641
- ___Block_byref_object_copy_.7257
- ___Block_byref_object_copy_.7636
- ___Block_byref_object_copy_.7922
- ___Block_byref_object_copy_.8355
- ___Block_byref_object_copy_.9759
- ___Block_byref_object_dispose_.10005
- ___Block_byref_object_dispose_.11239
- ___Block_byref_object_dispose_.11534
- ___Block_byref_object_dispose_.12294
- ___Block_byref_object_dispose_.13112
- ___Block_byref_object_dispose_.13692
- ___Block_byref_object_dispose_.14018
- ___Block_byref_object_dispose_.14205
- ___Block_byref_object_dispose_.15022
- ___Block_byref_object_dispose_.15630
- ___Block_byref_object_dispose_.16356
- ___Block_byref_object_dispose_.16678
- ___Block_byref_object_dispose_.17149
- ___Block_byref_object_dispose_.1745
- ___Block_byref_object_dispose_.17751
- ___Block_byref_object_dispose_.18574
- ___Block_byref_object_dispose_.20047
- ___Block_byref_object_dispose_.20187
- ___Block_byref_object_dispose_.2054
- ___Block_byref_object_dispose_.20699
- ___Block_byref_object_dispose_.21313
- ___Block_byref_object_dispose_.21795
- ___Block_byref_object_dispose_.22133
- ___Block_byref_object_dispose_.23149
- ___Block_byref_object_dispose_.23450
- ___Block_byref_object_dispose_.24286
- ___Block_byref_object_dispose_.2542
- ___Block_byref_object_dispose_.2620
- ___Block_byref_object_dispose_.2941
- ___Block_byref_object_dispose_.3258
- ___Block_byref_object_dispose_.5774
- ___Block_byref_object_dispose_.6479
- ___Block_byref_object_dispose_.6642
- ___Block_byref_object_dispose_.7258
- ___Block_byref_object_dispose_.7637
- ___Block_byref_object_dispose_.7923
- ___Block_byref_object_dispose_.8356
- ___Block_byref_object_dispose_.9760
- ___CPLConfigurationOSLogDomain.19407
- ___CPLConfigurationOSLogDomain.onceToken.19413
- ___CPLConfigurationOSLogDomain.result.19415
- ___CPLForceSyncOSLogDomain.20841
- ___CPLForceSyncOSLogDomain.onceToken.20850
- ___CPLForceSyncOSLogDomain.result.20851
- ___CPLSchedulerOSLogDomain.7584
- ___CPLSchedulerOSLogDomain.onceToken.7585
- ___CPLSchedulerOSLogDomain.result.7586
- ___CPLSessionOSLogDomain.16226
- ___CPLSessionOSLogDomain.18133
- ___CPLSessionOSLogDomain.22735
- ___CPLSessionOSLogDomain.onceToken.16228
- ___CPLSessionOSLogDomain.onceToken.18138
- ___CPLSessionOSLogDomain.onceToken.22737
- ___CPLSessionOSLogDomain.result.16229
- ___CPLSessionOSLogDomain.result.18139
- ___CPLSessionOSLogDomain.result.22739
- ___CPLStorageOSLogDomain.11206
- ___CPLStorageOSLogDomain.11291
- ___CPLStorageOSLogDomain.17718
- ___CPLStorageOSLogDomain.20166
- ___CPLStorageOSLogDomain.2035
- ___CPLStorageOSLogDomain.21459
- ___CPLStorageOSLogDomain.22119
- ___CPLStorageOSLogDomain.22367
- ___CPLStorageOSLogDomain.6231
- ___CPLStorageOSLogDomain.7872
- ___CPLStorageOSLogDomain.8607
- ___CPLStorageOSLogDomain.9048
- ___CPLStorageOSLogDomain.9214
- ___CPLStorageOSLogDomain.9407
- ___CPLStorageOSLogDomain.onceToken.11217
- ___CPLStorageOSLogDomain.onceToken.11294
- ___CPLStorageOSLogDomain.onceToken.14541
- ___CPLStorageOSLogDomain.onceToken.17720
- ___CPLStorageOSLogDomain.onceToken.20168
- ___CPLStorageOSLogDomain.onceToken.2037
- ___CPLStorageOSLogDomain.onceToken.20446
- ___CPLStorageOSLogDomain.onceToken.21463
- ___CPLStorageOSLogDomain.onceToken.22124
- ___CPLStorageOSLogDomain.onceToken.22375
- ___CPLStorageOSLogDomain.onceToken.6233
- ___CPLStorageOSLogDomain.onceToken.7874
- ___CPLStorageOSLogDomain.onceToken.8615
- ___CPLStorageOSLogDomain.onceToken.9054
- ___CPLStorageOSLogDomain.onceToken.9216
- ___CPLStorageOSLogDomain.onceToken.9409
- ___CPLStorageOSLogDomain.result.11219
- ___CPLStorageOSLogDomain.result.11296
- ___CPLStorageOSLogDomain.result.14543
- ___CPLStorageOSLogDomain.result.17722
- ___CPLStorageOSLogDomain.result.20170
- ___CPLStorageOSLogDomain.result.2039
- ___CPLStorageOSLogDomain.result.20447
- ___CPLStorageOSLogDomain.result.21465
- ___CPLStorageOSLogDomain.result.22126
- ___CPLStorageOSLogDomain.result.22377
- ___CPLStorageOSLogDomain.result.6235
- ___CPLStorageOSLogDomain.result.7875
- ___CPLStorageOSLogDomain.result.8616
- ___CPLStorageOSLogDomain.result.9056
- ___CPLStorageOSLogDomain.result.9217
- ___CPLStorageOSLogDomain.result.9410
- ___CPLStoreOSLogDomain.3045
- ___CPLStoreOSLogDomain.onceToken.3046
- ___CPLStoreOSLogDomain.result.3047
- ___CPLTaskOSLogDomain.11478
- ___CPLTaskOSLogDomain.13991
- ___CPLTaskOSLogDomain.14453
- ___CPLTaskOSLogDomain.15525
- ___CPLTaskOSLogDomain.17059
- ___CPLTaskOSLogDomain.21259
- ___CPLTaskOSLogDomain.23075
- ___CPLTaskOSLogDomain.24240
- ___CPLTaskOSLogDomain.2604
- ___CPLTaskOSLogDomain.5461
- ___CPLTaskOSLogDomain.7180
- ___CPLTaskOSLogDomain.onceToken.11514
- ___CPLTaskOSLogDomain.onceToken.1370
- ___CPLTaskOSLogDomain.onceToken.13993
- ___CPLTaskOSLogDomain.onceToken.14455
- ___CPLTaskOSLogDomain.onceToken.15535
- ___CPLTaskOSLogDomain.onceToken.17066
- ___CPLTaskOSLogDomain.onceToken.21301
- ___CPLTaskOSLogDomain.onceToken.23087
- ___CPLTaskOSLogDomain.onceToken.24248
- ___CPLTaskOSLogDomain.onceToken.2606
- ___CPLTaskOSLogDomain.onceToken.5464
- ___CPLTaskOSLogDomain.onceToken.7192
- ___CPLTaskOSLogDomain.result.11516
- ___CPLTaskOSLogDomain.result.1371
- ___CPLTaskOSLogDomain.result.13995
- ___CPLTaskOSLogDomain.result.14456
- ___CPLTaskOSLogDomain.result.15536
- ___CPLTaskOSLogDomain.result.17067
- ___CPLTaskOSLogDomain.result.21302
- ___CPLTaskOSLogDomain.result.23088
- ___CPLTaskOSLogDomain.result.24249
- ___CPLTaskOSLogDomain.result.2608
- ___CPLTaskOSLogDomain.result.5466
- ___CPLTaskOSLogDomain.result.7194
- _____CPLConfigurationOSLogDomain_block_invoke.19418
- _____CPLForceSyncOSLogDomain_block_invoke.20853
- _____CPLSchedulerOSLogDomain_block_invoke.7588
- _____CPLSessionOSLogDomain_block_invoke.16231
- _____CPLSessionOSLogDomain_block_invoke.18141
- _____CPLSessionOSLogDomain_block_invoke.22742
- _____CPLStorageOSLogDomain_block_invoke.11222
- _____CPLStorageOSLogDomain_block_invoke.11299
- _____CPLStorageOSLogDomain_block_invoke.14548
- _____CPLStorageOSLogDomain_block_invoke.17725
- _____CPLStorageOSLogDomain_block_invoke.20173
- _____CPLStorageOSLogDomain_block_invoke.2042
- _____CPLStorageOSLogDomain_block_invoke.20453
- _____CPLStorageOSLogDomain_block_invoke.21468
- _____CPLStorageOSLogDomain_block_invoke.22129
- _____CPLStorageOSLogDomain_block_invoke.22380
- _____CPLStorageOSLogDomain_block_invoke.6238
- _____CPLStorageOSLogDomain_block_invoke.7877
- _____CPLStorageOSLogDomain_block_invoke.8618
- _____CPLStorageOSLogDomain_block_invoke.9059
- _____CPLStorageOSLogDomain_block_invoke.9219
- _____CPLStorageOSLogDomain_block_invoke.9412
- _____CPLStoreOSLogDomain_block_invoke.3049
- _____CPLTaskOSLogDomain_block_invoke.11519
- _____CPLTaskOSLogDomain_block_invoke.1373
- _____CPLTaskOSLogDomain_block_invoke.13998
- _____CPLTaskOSLogDomain_block_invoke.14458
- _____CPLTaskOSLogDomain_block_invoke.15538
- _____CPLTaskOSLogDomain_block_invoke.17069
- _____CPLTaskOSLogDomain_block_invoke.21304
- _____CPLTaskOSLogDomain_block_invoke.23090
- _____CPLTaskOSLogDomain_block_invoke.24251
- _____CPLTaskOSLogDomain_block_invoke.2611
- _____CPLTaskOSLogDomain_block_invoke.5469
- _____CPLTaskOSLogDomain_block_invoke.7197
- ___block_descriptor_40_e8_32s_e32_v20?0"CPLScopedIdentifier"8f16ls32l8
- ___block_descriptor_52_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs48w_e44_v24?0"CPLEngineForceSyncTask"8"NSError"16lw48l8s32l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e51_v24?0"CPLEngineResourceDownloadTask"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_73_e8_32s40s48s56r64r_e9_B16?0^8lr56l8s32l8s40l8s48l8r64l8
- ___block_literal_global.10108
- ___block_literal_global.10429
- ___block_literal_global.105.18931
- ___block_literal_global.10825
- ___block_literal_global.110.20998
- ___block_literal_global.11064
- ___block_literal_global.111
- ___block_literal_global.11218
- ___block_literal_global.11295
- ___block_literal_global.11515
- ___block_literal_global.12.7996
- ___block_literal_global.12414
- ___block_literal_global.12636
- ___block_literal_global.13.24560
- ___block_literal_global.130
- ___block_literal_global.13132
- ___block_literal_global.13994
- ___block_literal_global.14.14489
- ___block_literal_global.1411
- ___block_literal_global.142.21002
- ___block_literal_global.14252
- ___block_literal_global.14488
- ___block_literal_global.14542
- ___block_literal_global.14705
- ___block_literal_global.1490
- ___block_literal_global.15238
- ___block_literal_global.15258
- ___block_literal_global.15323
- ___block_literal_global.15543
- ___block_literal_global.1571
- ___block_literal_global.159.21003
- ___block_literal_global.16081
- ___block_literal_global.16296
- ___block_literal_global.16856
- ___block_literal_global.171.21004
- ___block_literal_global.17171
- ___block_literal_global.1741
- ___block_literal_global.17515
- ___block_literal_global.17721
- ___block_literal_global.18151
- ___block_literal_global.18323
- ___block_literal_global.18461
- ___block_literal_global.1873
- ___block_literal_global.19044
- ___block_literal_global.1908
- ___block_literal_global.19414
- ___block_literal_global.19799
- ___block_literal_global.20169
- ___block_literal_global.20333
- ___block_literal_global.2038
- ___block_literal_global.20449
- ___block_literal_global.20994
- ___block_literal_global.21319
- ___block_literal_global.21464
- ___block_literal_global.21638
- ___block_literal_global.22125
- ___block_literal_global.22376
- ___block_literal_global.22536
- ___block_literal_global.22738
- ___block_literal_global.22888
- ___block_literal_global.2307
- ___block_literal_global.23144
- ___block_literal_global.23775
- ___block_literal_global.23911
- ___block_literal_global.23983
- ___block_literal_global.24.14206
- ___block_literal_global.24423
- ___block_literal_global.24537
- ___block_literal_global.24658
- ___block_literal_global.2482
- ___block_literal_global.24843
- ___block_literal_global.252
- ___block_literal_global.2540
- ___block_literal_global.2607
- ___block_literal_global.27.16315
- ___block_literal_global.271
- ___block_literal_global.2957
- ___block_literal_global.3024
- ___block_literal_global.32.22504
- ___block_literal_global.3274
- ___block_literal_global.33.7308
- ___block_literal_global.34.10001
- ___block_literal_global.34.2479
- ___block_literal_global.3546
- ___block_literal_global.37.10745
- ___block_literal_global.3782
- ___block_literal_global.4017
- ___block_literal_global.42.8003
- ___block_literal_global.439
- ___block_literal_global.4451
- ___block_literal_global.4588
- ___block_literal_global.4802
- ___block_literal_global.5.24550
- ___block_literal_global.50.7299
- ___block_literal_global.5250
- ___block_literal_global.5327
- ___block_literal_global.54.5223
- ___block_literal_global.5465
- ___block_literal_global.5605
- ___block_literal_global.57.8007
- ___block_literal_global.6.15541
- ___block_literal_global.6146
- ___block_literal_global.6234
- ___block_literal_global.6454
- ___block_literal_global.660
- ___block_literal_global.663
- ___block_literal_global.666
- ___block_literal_global.6750
- ___block_literal_global.7193
- ___block_literal_global.72.16814
- ___block_literal_global.7307
- ___block_literal_global.77.16076
- ___block_literal_global.7706
- ___block_literal_global.7993
- ___block_literal_global.8738
- ___block_literal_global.89
- ___block_literal_global.8949
- ___block_literal_global.9055
- ___block_literal_global.9153
- ___block_literal_global.93.18935
- ___block_literal_global.93.7769
- ___block_literal_global.9458
- ___block_literal_global.9630
- ___block_literal_global.9900
- ___cpl_dispatch_async_block_invoke.10085
- ___cpl_dispatch_async_block_invoke.11474
- ___cpl_dispatch_async_block_invoke.12115
- ___cpl_dispatch_async_block_invoke.1376
- ___cpl_dispatch_async_block_invoke.14003
- ___cpl_dispatch_async_block_invoke.14377
- ___cpl_dispatch_async_block_invoke.14450
- ___cpl_dispatch_async_block_invoke.15618
- ___cpl_dispatch_async_block_invoke.16634
- ___cpl_dispatch_async_block_invoke.17125
- ___cpl_dispatch_async_block_invoke.17471
- ___cpl_dispatch_async_block_invoke.17958
- ___cpl_dispatch_async_block_invoke.1822
- ___cpl_dispatch_async_block_invoke.18457
- ___cpl_dispatch_async_block_invoke.19393
- ___cpl_dispatch_async_block_invoke.20681
- ___cpl_dispatch_async_block_invoke.21257
- ___cpl_dispatch_async_block_invoke.21646
- ___cpl_dispatch_async_block_invoke.22890
- ___cpl_dispatch_async_block_invoke.23092
- ___cpl_dispatch_async_block_invoke.24293
- ___cpl_dispatch_async_block_invoke.2944
- ___cpl_dispatch_async_block_invoke.6693
- ___cpl_dispatch_async_block_invoke.7178
- ___cpl_dispatch_async_block_invoke.7447
- ___cpl_dispatch_async_block_invoke.7883
- ___cpl_dispatch_async_block_invoke.9743
- __doProtected:.onceToken.15257
- __doProtected:.onceToken.22887
- __doProtected:.queue.22889
- __statusDidChange.12311
- __willDownloadInBackgroundErrorForTask
- _copyDerivativesFromRecordIfPossible:.originalDerivativesImageAndVideo.18954
- _initWithCoder:.logOnceToken.20335
- _initWithCoder:.onceToken.10769
- _initWithCoder:.onceToken.14251
- _initWithCoder:.onceToken.18150
- _initWithCoder:.onceToken.20332
- _initWithCoder:.onceToken.22535
- _initWithCoder:.onceToken.24842
- _initWithCoder:.onceToken.5222
- _initWithCoder:.onceToken.5326
- _initWithCoder:.onceToken.6449
- _initWithCoder:.pushContextsClasses.22537
- _initWithCoder:.stringClass.10770
- _objc_msgSend$_checkForegroundAtLaunchForForceSyncTask
- _objc_msgSend$_disableSchedulerForForceSyncTaskIfNecessary
- _objc_msgSend$_discardPendingForceSyncTaskWithError:
- _objc_msgSend$_extractBatchWithTransaction:andStore:
- _objc_msgSend$_forceSyncTaskDidFinishWithError:
- _objc_msgSend$_launchForceSyncTaskIfNecessary
- _objc_msgSend$_launchSubTask:
- _objc_msgSend$_recordForcedSyncTask:discarded:error:
- _objc_msgSend$_reenableSchedulerForForceSyncTaskIfNecessary
- _objc_msgSend$_uploadBatchWithFetchCache:
- _objc_msgSend$cleanupStepHasMore:error:
- _objc_msgSend$initWithForcedSyncTask:discarded:error:
- _objc_msgSend$unstashRecordsForScopeWithIdentifier:maxCount:hasMore:error:
- _propertiesForChangeType:.onceToken.15093
- _propertiesForChangeType:.onceToken.18968
- _propertiesForChangeType:.onceToken.23910
- _propertiesForChangeType:.properties.23912
CStrings:
+ " + %lu others"
+ "@\"<CPLEngineStoreUserIdentifier>\"16@0:8"
+ "@\"<CPLEngineSyncManagerForcedTask>\""
+ "@\"NSDate\"16@0:8"
+ "@\"NSError\"16@0:8"
+ "@?<v@?@\"<CPLEngineSyncManagerForcedTask>\"@\"NSError\">16@0:8"
+ "B40@0:8^B16^Q24^@32"
+ "B56@0:8@16Q24^B32^Q40^@48"
+ "CPLEngineSyncManagerForcedTask"
+ "CPLForceForegroundAtLaunchForForcedTask"
+ "Cancelling %lu pending forced tasks (first: %@)"
+ "CloudPhotoLibrary-800.26.109"
+ "T@\"<CPLEngineStoreUserIdentifier>\",&,N"
+ "T@\"NSString\",R,N,V_simpleDescription"
+ "T@?,C,N"
+ "_CPLForcedTaskHistory"
+ "_checkForegroundAtLaunchForForcedTask"
+ "_countOfFinishedDownloadTasksSinceLastReport"
+ "_currentForcedTask"
+ "_derivativesSizeReportTimer"
+ "_derivativesSizeToReport"
+ "_disableSchedulerForForcedTaskIfNecessary"
+ "_disabledSchedulerForForcedTask"
+ "_discardPendingForcedTasksWithError:"
+ "_finishReportingDerivativesIsNecessary"
+ "_forcedTaskDidFinishWithError:"
+ "_forcedTaskHistory"
+ "_launchForcedTaskIfNecessary"
+ "_launchSubTask:subIdentifier:"
+ "_pendingForcedTasks"
+ "_recordForcedTask:discarded:error:"
+ "_reenableSchedulerForForcedTaskIfNecessary"
+ "_reportDownloadedTasks"
+ "_reportTimer"
+ "_simpleDescription"
+ "addCompletedWorkBytesCount:kindOfWork:"
+ "allowsBackgroundDispatch"
+ "allowsForcedTaskQueuing"
+ "aside.states"
+ "beginKindOfWork:"
+ "cancelScheduledForcedTaskForLaunch:"
+ "cleanupStepHasMore:deletedCount:error:"
+ "deleted.records"
+ "derivatives.kb"
+ "discard.changes"
+ "discardedError"
+ "dropped.states"
+ "endKindOfWork:"
+ "engine.sync."
+ "engine.syncmanager.forced"
+ "forcedTaskPriority"
+ "initWithForcedTask:discarded:error:"
+ "performing a forced task"
+ "requested.states"
+ "resources.kb"
+ "scheduleForcedTaskForLaunch:"
+ "unstashRecordsForScopeWithIdentifier:maxCount:hasMore:unstashedCount:error:"
+ "unstashed.records"
+ "upload.changes"
+ "upload.kb"
+ "uploaded.states"
+ "v24@0:8@\"<CPLEngineStoreUserIdentifier>\"16"
+ "v24@0:8@?<v@?@\"<CPLEngineSyncManagerForcedTask>\"@\"NSError\">16"
+ "v24@?0@\"<CPLEngineSyncManagerForcedTask>\"8@\"NSError\"16"
+ "v32@?0@\"<CPLEngineSyncManagerForcedTask>\"8Q16^B24"
- "@\"CPLEngineForceSyncTask\""
- "B32@0:8^B16^@24"
- "CPLForceForegroundAtLaunchForForceSyncTask"
- "Cancelling pending %@"
- "CloudPhotoLibrary-800.20.101"
- "T@\"CPLScopeFilter\",R,N,V_filter"
- "_CPLForcedSyncHistory"
- "_checkForegroundAtLaunchForForceSyncTask"
- "_currentForceSyncTask"
- "_disableSchedulerForForceSyncTaskIfNecessary"
- "_disabledSchedulerForForceSyncTask"
- "_discardPendingForceSyncTaskWithError:"
- "_extractBatchWithTransaction:andStore:"
- "_forceSyncTaskDidFinishWithError:"
- "_forcedSyncHistory"
- "_launchForceSyncTaskIfNecessary"
- "_launchSubTask:"
- "_pendingForceSyncTask"
- "_recordForcedSyncTask:discarded:error:"
- "_reenableSchedulerForForceSyncTaskIfNecessary"
- "_total"
- "_uploadBatchWithFetchCache:"
- "cleanupStepHasMore:error:"
- "engine.syncmanager.forcesync"
- "initWithForcedSyncTask:discarded:error:"
- "kb"
- "performing a forced sync session"
- "pull.assets"
- "unstashRecordsForScopeWithIdentifier:maxCount:hasMore:error:"

```
