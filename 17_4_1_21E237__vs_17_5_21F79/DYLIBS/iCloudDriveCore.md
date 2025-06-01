## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-2720.100.117.0.0
-  __TEXT.__text: 0x2bfea4
+2720.120.29.0.0
+  __TEXT.__text: 0x2c03e0
   __TEXT.__auth_stubs: 0x1b50
-  __TEXT.__objc_methlist: 0x158b4
+  __TEXT.__objc_methlist: 0x1595c
   __TEXT.__const: 0x358
-  __TEXT.__cstring: 0x73e63
-  __TEXT.__oslogstring: 0x37ec6
-  __TEXT.__gcc_except_tab: 0x134a8
+  __TEXT.__cstring: 0x74257
+  __TEXT.__oslogstring: 0x37e5d
+  __TEXT.__gcc_except_tab: 0x132d4
   __TEXT.__ustring: 0x36
-  __TEXT.__unwind_info: 0x82e8
-  __TEXT.__objc_classname: 0x21a9
-  __TEXT.__objc_methname: 0x39bf7
-  __TEXT.__objc_methtype: 0x6b14
-  __TEXT.__objc_stubs: 0x27ec0
+  __TEXT.__unwind_info: 0x8214
+  __TEXT.__objc_classname: 0x21c2
+  __TEXT.__objc_methname: 0x39ed7
+  __TEXT.__objc_methtype: 0x6ba5
+  __TEXT.__objc_stubs: 0x28080
   __DATA_CONST.__got: 0xaf8
-  __DATA_CONST.__const: 0x8120
-  __DATA_CONST.__objc_classlist: 0x880
+  __DATA_CONST.__const: 0x81c0
+  __DATA_CONST.__objc_classlist: 0x888
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x30a98
-  __DATA_CONST.__objc_selrefs: 0xc728
+  __DATA_CONST.__objc_const: 0x30c00
+  __DATA_CONST.__objc_selrefs: 0xc798
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0xcc8
+  __DATA_CONST.__objc_classrefs: 0xcd8
   __DATA_CONST.__objc_superrefs: 0x7a0
   __DATA_CONST.__objc_arraydata: 0xd98
-  __AUTH_CONST.__cfstring: 0x1f8a0
-  __AUTH_CONST.__objc_const: 0x6808
-  __AUTH_CONST.__const: 0x2528
+  __AUTH_CONST.__cfstring: 0x1fb20
+  __AUTH_CONST.__objc_const: 0x6850
+  __AUTH_CONST.__const: 0x24e8
   __AUTH_CONST.__objc_intobj: 0xa08
   __AUTH_CONST.__objc_arrayobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__auth_got: 0xdb8
-  __AUTH.__objc_data: 0x2940
+  __AUTH.__objc_data: 0x2850
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x1bec
-  __DATA.__data: 0x1ee0
-  __DATA.__bss: 0x270
-  __DATA_DIRTY.__objc_data: 0x2bc0
+  __DATA.__objc_ivar: 0x1c04
+  __DATA.__data: 0x1ef0
+  __DATA.__bss: 0x240
+  __DATA_DIRTY.__objc_data: 0x2d00
   __DATA_DIRTY.__data: 0xd0
   __DATA_DIRTY.__bss: 0x2f0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E64AA843-AD48-3D38-9488-03779E2E8D09
-  Functions: 12904
-  Symbols:   38855
-  CStrings:  24868
+  UUID: 1E1EE402-F0C2-30C6-95E6-7839CED7F349
+  Functions: 12907
+  Symbols:   38871
+  CStrings:  24930
 
Symbols:
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newAggregatedEventWithIdentifier:recordID:zoneMangledID:error:count:]
+ +[BRCFSDownloaderUtil downloadKindWithEtagIfLoser:options:]
+ +[BRCTrackedVersion trackedVersionFor:withEtagIfLoser:kind:]
+ -[AppTelemetryFPFSMigrationInvestigation hasXpcActivityTimeSinceLastAbleToRun]
+ -[AppTelemetryFPFSMigrationInvestigation setHasXpcActivityTimeSinceLastAbleToRun:]
+ -[AppTelemetryFPFSMigrationInvestigation setXpcActivityTimeSinceLastAbleToRun:]
+ -[AppTelemetryFPFSMigrationInvestigation xpcActivityTimeSinceLastAbleToRun]
+ -[BRCAccountSessionFPFS(FPFSAdditions) _populateNonMigratedItemEventForLocalDataWithEvent:fileIDData:diagnosticDescriptor:migrationStart:]
+ -[BRCAnalyticsReporter aggregateReportForAppTelemetryIdentifier:error:]
+ -[BRCAnalyticsReporter aggregateReportForAppTelemetryIdentifier:itemID:zoneMangledID:advancedDataProtectionEnabled:error:]
+ -[BRCClientZone _blockExistingOperationIfNecessary:onNewOperation:considerPriority:]
+ -[BRCDownloadContent initWithDocument:stageID:etagIfLoser:downloadKind:]
+ -[BRCDownloadTrackers document:didCompleteDownloadEtagIfLoser:kind:withError:]
+ -[BRCFSDownloader scheduleContentDownloadForItem:serverItem:options:etagIfLoser:stageFileName:error:]
+ -[BRCFSDownloader scheduleContentDownloadForItem:serverItem:options:etagIfLoser:stageFileName:error:].cold.1
+ -[BRCFSDownloader scheduleContentDownloadForItem:serverItem:options:etagIfLoser:stageFileName:error:].cold.2
+ -[BRCFSDownloaderBatchEnumerator kind]
+ -[BRCFileProvidingRequestOperation kind]
+ -[BRCFileProvidingRequestOperation(FPFSAdditions) initWithDocumentItem:client:session:etagIfLoser:stageFileName:options:]
+ -[BRCLocalItem(CKConversions) structureRecordBeingDeadInServerTruth:stageID:shouldPCSChainStatus:saltGetter:childBasehashSalt:].cold.2
+ -[BRCLocalItem(FPFSAdditions) markBouncedToNextAvailableBounceNumber:]
+ -[BRCSyncHealthReport _collectAggregatedTelemetryForSession:]
+ -[BRCSyncHealthReport aggregatedEvents]
+ -[BRCTrackedVersion kind]
+ -[CKRecord(BRCSerializationAdditions) _verifyValueForRecordWithNumber:key:item:error:]
+ -[CKRecord(BRCSerializationAdditions) serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:error:]
+ -[CKRecord(BRCSerializationAdditions) serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:error:].cold.1
+ -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:error:]
+ -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:error:].cold.1
+ -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:error:].cold.2
+ -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:error:].cold.3
+ -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:error:].cold.4
+ -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:error:].cold.5
+ -[NSFileProviderManager(BRCAdditions) br_signalWorkingSetEnumeratorWithCompletionHandler:]
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationInvestigation._xpcActivityTimeSinceLastAbleToRun
+ OBJC_IVAR_$_BRCFileProvidingRequestOperation._options
+ _OBJC_CLASS_$_BRCFSDownloaderUtil
+ _OBJC_CLASS_$_BRPersonaUtils
+ _OBJC_IVAR_$_BRCDownloadContent._kind
+ _OBJC_IVAR_$_BRCFSDownloaderBatchEnumerator._kind
+ _OBJC_IVAR_$_BRCSyncHealthReport._aggregatedEvents
+ _OBJC_IVAR_$_BRCTrackedVersion._kind
+ _OBJC_METACLASS_$_BRCFSDownloaderUtil
+ __OBJC_$_CLASS_METHODS_BRCFSDownloaderUtil
+ __OBJC_CLASS_RO_$_BRCFSDownloaderUtil
+ __OBJC_METACLASS_RO_$_BRCFSDownloaderUtil
+ ___103-[NSFileProviderManager(BRCAdditions) br_signalEnumeratorForContainerItemIdentifier:completionHandler:]_block_invoke
+ ___122-[BRCAnalyticsReporter aggregateReportForAppTelemetryIdentifier:itemID:zoneMangledID:advancedDataProtectionEnabled:error:]_block_invoke
+ ___122-[BRCAnalyticsReporter aggregateReportForAppTelemetryIdentifier:itemID:zoneMangledID:advancedDataProtectionEnabled:error:]_block_invoke_2
+ ___49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.478
+ ___59+[BRCImportUtil forceIngestionForItemID:completionHandler:]_block_invoke
+ ___59-[BRCFileProvidingRequestOperation finishWithResult:error:]_block_invoke_2.14
+ ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.211
+ ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.211.cold.1
+ ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.211.cold.2
+ ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.216
+ ___70-[NSFileProviderManager(BRCAdditions) br_addDomain:completionHandler:]_block_invoke
+ ___72-[BRCXPCRegularIPCsClient(FPFSAdditions) waitForStabilizationWithReply:]_block_invoke.149
+ ___74-[BRCXPCRegularIPCsClient(FPFSAdditions) getFPItemIDOfAppLibraryID:reply:]_block_invoke.134
+ ___74-[BRCXPCRegularIPCsClient(FPFSAdditions) getFPItemIDOfAppLibraryID:reply:]_block_invoke.134.cold.1
+ ___75-[BRCAccountSessionFPFS(FPFSAdditions) _sendFPFSImportStatusTelemetryEvent]_block_invoke.175
+ ___75-[BRCAccountSessionFPFS(FPFSAdditions) _sendFPFSImportStatusTelemetryEvent]_block_invoke_2.176
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.691
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.694
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.693
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.693.cold.1
+ ___77-[BRCXPCRegularIPCsClient(FPFSAdditions) copyShareIDForItemIdentifier:reply:]_block_invoke.130
+ ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke.126
+ ___86-[NSFileProviderManager(BRCAdditions) br_removeDomain:options:sync:completionHandler:]_block_invoke.6
+ ___86-[NSFileProviderManager(BRCAdditions) br_removeDomain:options:sync:completionHandler:]_block_invoke.6.cold.1
+ ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) checkIfItemIsShareableWithItemIdentifier:reply:]_block_invoke.131
+ ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) startOperation:toWaitForFPFSMigrationWithReply:]_block_invoke.139
+ ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getCreatorNameComponentsForItemIdentifier:reply:]_block_invoke.132
+ ___90-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke_2.cold.1
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) cloneLatestContentRevisionForItemIdentifier:reply:]_block_invoke.125
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) fetchLatestContentRevisionForItemIdentifier:reply:]_block_invoke.124
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.624
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.624.cold.1
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.625
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.628
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.628.cold.1
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.628.cold.2
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.630
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.631
+ ___95-[BRCXPCRegularIPCsClient(FPFSAdditions) launchItemCountMismatchChecksForItemIdentifier:reply:]_block_invoke.128
+ ___block_descriptor_132_e8_32s40s48s56s64s72s80s88s96s104bs_e17_B16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s104l8s96l8
+ ___block_descriptor_140_e8_32s40s48s56s64s72s80s88s96s104s112bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s112l8s104l8
+ ___block_descriptor_40_e8_32s_e24_v16?0?<v?"NSError">8ls32l8
+ ___block_descriptor_48_e8_32s40s_e24_v16?0?<v?"NSError">8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e20_v20?0B8"NSError"12ls32l8s56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_68_e8_32s40s48s56s_e23_B16?0"PQLConnection"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48bs_e17_v16?0"NSError"8ls48l8s32l8s40l8
+ ___block_descriptor_76_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.2102
+ ___block_literal_global.2128
+ ___block_literal_global.2147
+ ___block_literal_global.2150
+ ___block_literal_global.715
+ __unnamed_array_storage.171
+ _br_update_tables_31_003
+ _br_update_tables_31_004
+ _objc_msgSend$_blockExistingOperationIfNecessary:onNewOperation:considerPriority:
+ _objc_msgSend$_collectAggregatedTelemetryForSession:
+ _objc_msgSend$_populateNonMigratedItemEventForLocalDataWithEvent:fileIDData:diagnosticDescriptor:migrationStart:
+ _objc_msgSend$_verifyValueForRecordWithNumber:key:item:error:
+ _objc_msgSend$aggregateReportForAppTelemetryIdentifier:error:
+ _objc_msgSend$aggregateReportForAppTelemetryIdentifier:itemID:zoneMangledID:advancedDataProtectionEnabled:error:
+ _objc_msgSend$aggregatedEvents
+ _objc_msgSend$br_errorDescription
+ _objc_msgSend$br_isCKErrorCode:
+ _objc_msgSend$br_signalWorkingSetEnumeratorWithCompletionHandler:
+ _objc_msgSend$document:didCompleteDownloadEtagIfLoser:kind:withError:
+ _objc_msgSend$downloadKindWithEtagIfLoser:options:
+ _objc_msgSend$executeAsyncXPCWithMaxRetries:completion:xpcInvokeBlock:
+ _objc_msgSend$initWithDocument:stageID:etagIfLoser:downloadKind:
+ _objc_msgSend$initWithDocumentItem:client:session:etagIfLoser:stageFileName:options:
+ _objc_msgSend$itemEnumerator
+ _objc_msgSend$markBouncedToNextAvailableBounceNumber:
+ _objc_msgSend$newAggregatedEventWithIdentifier:recordID:zoneMangledID:error:count:
+ _objc_msgSend$originalName
+ _objc_msgSend$performWithPersonaID:block:
+ _objc_msgSend$scheduleContentDownloadForItem:serverItem:options:etagIfLoser:stageFileName:error:
+ _objc_msgSend$serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:error:
+ _objc_msgSend$serializeVersion:diffs:deadInServerTruth:basehashSalt:error:
+ _objc_msgSend$setXpcActivityTimeSinceLastAbleToRun:
+ _objc_msgSend$trackedVersionFor:withEtagIfLoser:kind:
+ _objc_msgSend$xpcActivityTimeSinceLastAbleToRun
- +[BRCTrackedVersion trackedVersionFor:withEtagIfLoser:]
- -[BRCAccountSessionFPFS(FPFSAdditions) _populateNonMigratedItemEventForLocalDataWithEvent:fileIDData:diagnosticDescriptor:]
- -[BRCClientZone _blockExistingOperationIfNecessary:onNewOperation:]
- -[BRCDownloadContent initWithDocument:stageID:etagIfLoser:]
- -[BRCDownloadTrackers document:didCompleteDownloadEtagIfLoser:withError:]
- -[BRCFSDownloader _appLibraryForDownload:kind:operationID:]
- -[BRCFSDownloader scheduleContentDownloadForItem:serverItem:userInitiated:etagIfLoser:stageFileName:error:]
- -[BRCFSDownloader scheduleContentDownloadForItem:serverItem:userInitiated:etagIfLoser:stageFileName:error:].cold.1
- -[BRCFSDownloader scheduleContentDownloadForItem:serverItem:userInitiated:etagIfLoser:stageFileName:error:].cold.2
- -[BRCFileProvidingRequestOperation(FPFSAdditions) initWithDocumentItem:client:session:etagIfLoser:stageFileName:]
- -[BRCLocalItem(FPFSAdditions) markBouncedToNextAvailableBounceNumber]
- -[CKRecord(BRCSerializationAdditions) serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:]
- -[CKRecord(BRCSerializationAdditions) serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:].cold.1
- -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:]
- -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:].cold.1
- -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:].cold.2
- -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:].cold.3
- -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:].cold.4
- -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:].cold.5
- -[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]
- -[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]
- ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke
- ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke.cold.1
- ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke.cold.2
- ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke.cold.3
- ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke.cold.4
- ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke_2
- ___49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.457
- ___59-[BRCFileProvidingRequestOperation finishWithResult:error:]_block_invoke_2.13
- ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.214
- ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.214.cold.1
- ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.214.cold.2
- ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.219
- ___72-[BRCXPCRegularIPCsClient(FPFSAdditions) waitForStabilizationWithReply:]_block_invoke.148
- ___74-[BRCXPCRegularIPCsClient(FPFSAdditions) getFPItemIDOfAppLibraryID:reply:]_block_invoke.133
- ___74-[BRCXPCRegularIPCsClient(FPFSAdditions) getFPItemIDOfAppLibraryID:reply:]_block_invoke.133.cold.1
- ___75-[BRCAccountSessionFPFS(FPFSAdditions) _sendFPFSImportStatusTelemetryEvent]_block_invoke.172
- ___75-[BRCAccountSessionFPFS(FPFSAdditions) _sendFPFSImportStatusTelemetryEvent]_block_invoke_2.173
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.664
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.667
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.666
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.666.cold.1
- ___77-[BRCXPCRegularIPCsClient(FPFSAdditions) copyShareIDForItemIdentifier:reply:]_block_invoke.129
- ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke
- ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke.cold.1
- ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke.cold.2
- ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke.cold.3
- ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke.cold.4
- ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke_2
- ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke.125
- ___86-[NSFileProviderManager(BRCAdditions) br_removeDomain:options:sync:completionHandler:]_block_invoke.8
- ___86-[NSFileProviderManager(BRCAdditions) br_removeDomain:options:sync:completionHandler:]_block_invoke.8.cold.1
- ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) checkIfItemIsShareableWithItemIdentifier:reply:]_block_invoke.130
- ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) startOperation:toWaitForFPFSMigrationWithReply:]_block_invoke.138
- ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getCreatorNameComponentsForItemIdentifier:reply:]_block_invoke.131
- ___90-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke.cold.1
- ___90-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke.cold.2
- ___90-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke.cold.3
- ___90-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke.cold.4
- ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) cloneLatestContentRevisionForItemIdentifier:reply:]_block_invoke_2
- ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) fetchLatestContentRevisionForItemIdentifier:reply:]_block_invoke_2
- ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.69.cold.3
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.597
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.597.cold.1
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.598
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.601
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.601.cold.1
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.601.cold.2
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.603
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.604
- ___95-[BRCXPCRegularIPCsClient(FPFSAdditions) launchItemCountMismatchChecksForItemIdentifier:reply:]_block_invoke.127
- ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96s104bs_e17_B16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s104l8s96l8
- ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96s104s112bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s112l8s104l8
- ___block_descriptor_56_e8_32s40s48s_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e20_v20?0B8"NSError"12ls32l8s40l8s56l8s48l8
- ___block_descriptor_72_e8_32s40s48bs56w_e17_v16?0"NSError"8ls48l8w56l8s32l8s40l8
- ___block_literal_global.11
- ___block_literal_global.2096
- ___block_literal_global.2122
- ___block_literal_global.2141
- ___block_literal_global.2144
- ___block_literal_global.688
- __unnamed_array_storage.168
- __unnamed_array_storage.186
- _objc_msgSend$_blockExistingOperationIfNecessary:onNewOperation:
- _objc_msgSend$_br_addDomain:retries:completionHandler:
- _objc_msgSend$_br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:
- _objc_msgSend$_populateNonMigratedItemEventForLocalDataWithEvent:fileIDData:diagnosticDescriptor:
- _objc_msgSend$document:didCompleteDownloadEtagIfLoser:withError:
- _objc_msgSend$initWithDocument:stageID:etagIfLoser:
- _objc_msgSend$initWithDocumentItem:client:session:etagIfLoser:stageFileName:
- _objc_msgSend$markBouncedToNextAvailableBounceNumber
- _objc_msgSend$scheduleContentDownloadForItem:serverItem:userInitiated:etagIfLoser:stageFileName:error:
- _objc_msgSend$serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:
- _objc_msgSend$serializeVersion:diffs:deadInServerTruth:basehashSalt:
- _objc_msgSend$trackedVersionFor:withEtagIfLoser:
CStrings:
+ "\x02\x18"
+ "\b"
+ "-[BRCClientZone _blockExistingOperationIfNecessary:onNewOperation:considerPriority:]"
+ "-[BRCDownloadTrackers document:didCompleteDownloadEtagIfLoser:kind:withError:]"
+ "-[BRCFSDownloader scheduleContentDownloadForItem:serverItem:options:etagIfLoser:stageFileName:error:]"
+ "-[BRCLocalItem(FPFSAdditions) markBouncedToNextAvailableBounceNumber:]"
+ "-[CKRecord(BRCSerializationAdditions) _verifyValueForRecordWithNumber:key:item:error:]"
+ "-[CKRecord(BRCSerializationAdditions) serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:error:]"
+ "-[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:error:]"
+ "-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke_2"
+ "@44@0:8@16@24@32i40"
+ "@52@0:8i16@20@28@36q44"
+ "ALTER TABLE aggregated_daily_telemetry RENAME advanced_data_protection_enabled TO enhanced_drive_privacy_enabled"
+ "Account is not ready"
+ "B36@0:8@16@24B32"
+ "B52@0:8@16Q24B32@36^@44"
+ "B64@0:8@16@24Q32@40@48^@56"
+ "B72@0:8@16Q24@32B40C44@48@56^@64"
+ "BRCFSDownloaderUtil"
+ "CREATE TABLE aggregated_daily_telemetry ( app_telemetry_identifier integer NOT NULL, zone_mangled_id text NOT NULL, item_id text NOT NULL, advanced_data_protection_enabled text NOT NULL, error_domain text NOT NULL, error_code int NOT NULL, error_description text NOT NULL, count int NOT NULL DEFAULT 1, PRIMARY KEY (app_telemetry_identifier, zone_mangled_id, item_id, advanced_data_protection_enabled, error_domain, error_code))"
+ "DELETE FROM aggregated_daily_telemetry"
+ "INSERT INTO aggregated_daily_telemetry (app_telemetry_identifier, zone_mangled_id, item_id, enhanced_drive_privacy_enabled, error_domain, error_code, error_description) VALUES (%d, %@, %@, %@, %@, %ld, %@) ON CONFLICT DO UPDATE SET count=count+1"
+ "ITEM_BOUNCE_APPLY_EXISTING_WITH_EXISTING"
+ "ITEM_BOUNCE_APPLY_EXISTING_WITH_NEW"
+ "ITEM_BOUNCE_APPLY_NEW_WITH_EXISTING"
+ "ITEM_BOUNCE_BY_SERVER"
+ "ITEM_BOUNCE_CHANGE_ITEM_WITH_EXISTING"
+ "ITEM_BOUNCE_CREATE_ITEM_WITH_EXISTING"
+ "ITEM_BOUNCE_EXISTING_WITH_NEW_DIRECTORY"
+ "ITEM_BOUNCE_ITEM_DIRECTORY_MERGE"
+ "ITEM_BOUNCE_NEW_DIRECTORY_WITH_EXISTING"
+ "ITEM_BOUNCE_SHARE_ACCEPT_EXISTING_WITH_NEW"
+ "ITEM_BOUNCE_SHARE_ACCEPT_NEW_WITH_EXISTING"
+ "ITEM_BOUNCE_TRASHED_ITEM"
+ "RECORD_VALUE_ERROR"
+ "SELECT app_telemetry_identifier, zone_mangled_id, item_id, enhanced_drive_privacy_enabled, error_domain, error_code, error_description, count FROM aggregated_daily_telemetry"
+ "T@\"NSArray\",R,N,V_aggregatedEvents"
+ "Tq,N,V_xpcActivityTimeSinceLastAbleToRun"
+ "[CRIT] UNREACHABLE: %@ has negative value %@!%@"
+ "[DEBUG] Error creating record %@ for item %@%@"
+ "[DEBUG] Error creating record %@%@"
+ "[DEBUG] Generated sync health report with upload failures:%@\ndownload failures:%@\nsync up failures:%@\nzone sync up errors:%@\nzone sync down errors:%@\naggregated events:%@%@"
+ "[ERROR] Received item with unexpected type and no content %@. Rejecting it%@"
+ "[WARNING] CKAsset for %@ is pointing to the wrong device ID%@"
+ "_aggregatedEvents"
+ "_blockExistingOperationIfNecessary:onNewOperation:considerPriority:"
+ "_collectAggregatedTelemetryForSession:"
+ "_populateNonMigratedItemEventForLocalDataWithEvent:fileIDData:diagnosticDescriptor:migrationStart:"
+ "_verifyValueForRecordWithNumber:key:item:error:"
+ "_xpcActivityTimeSinceLastAbleToRun"
+ "aggregateReportForAppTelemetryIdentifier:error:"
+ "aggregateReportForAppTelemetryIdentifier:itemID:zoneMangledID:advancedDataProtectionEnabled:error:"
+ "aggregatedEvents"
+ "br_errorDescription"
+ "br_isCKErrorCode:"
+ "br_signalWorkingSetEnumeratorWithCompletionHandler:"
+ "document:didCompleteDownloadEtagIfLoser:kind:withError:"
+ "downloadKindWithEtagIfLoser:options:"
+ "executeAsyncXPCWithMaxRetries:completion:xpcInvokeBlock:"
+ "hasXpcActivityTimeSinceLastAbleToRun"
+ "i32@0:8@16Q24"
+ "initWithDocument:stageID:etagIfLoser:downloadKind:"
+ "initWithDocumentItem:client:session:etagIfLoser:stageFileName:options:"
+ "itemEnumerator"
+ "markBouncedToNextAvailableBounceNumber:"
+ "newAggregatedEventWithIdentifier:recordID:zoneMangledID:error:count:"
+ "performWithPersonaID:block:"
+ "scheduleContentDownloadForItem:serverItem:options:etagIfLoser:stageFileName:error:"
+ "serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:error:"
+ "serializeVersion:diffs:deadInServerTruth:basehashSalt:error:"
+ "setHasXpcActivityTimeSinceLastAbleToRun:"
+ "setXpcActivityTimeSinceLastAbleToRun:"
+ "trackedVersionFor:withEtagIfLoser:kind:"
+ "v16@?0@?<v@?@\"NSError\">8"
+ "v44@0:8@16@24i32@36"
+ "v52@0:8i16@20@28@36@44"
+ "xpcActivityTimeSinceLastAbleToRun"
+ "{?=\"accountQuotaUsage\"b1\"bouncedItemsCount\"b1\"bouncedItemsMatrix\"b1\"busyDateNotMigratedCount\"b1\"childItemsNotMigratedCount\"b1\"durationBetweenDbCreationAndMigrationStart\"b1\"ignoredFromSyncItemsNotMigratedCount\"b1\"importTime\"b1\"itemsMigratedWithoutAlreadyMayExistFlag\"b1\"itemsNotFoundInDB\"b1\"itemsNotMigratedCount\"b1\"itemsNotMigratedDelta\"b1\"itemsReconciledInFileProvider\"b1\"itemsReconciledInFileProviderDelta\"b1\"numberOfItemsPendingReconciliation\"b1\"numberOfItemsPendingScanningDisk\"b1\"numberOfItemsPendingScanningProvider\"b1\"numberOfItemsPendingSelection\"b1\"stateOfDownloadJobs\"b1\"stateOfOtherJobs\"b1\"stateOfUploadJobs\"b1\"totalItemCount\"b1\"xpcActivityDasdContext\"b1\"xpcActivityTimeSinceLastAbleToRun\"b1\"xpcActivityTimeSinceLastActivation\"b1\"xpcActivityTimeSinceLastRegistration\"b1\"typesOfMigratedItemsMask\"b1\"typesOfNonMigratedItemsMask\"b1\"isAccountDataSeparated\"b1\"isStreamResetRunning\"b1\"isSuccessful\"b1\"xpcActivityIsActive\"b1\"xpcActivityRegisteredWithDuet\"b1}"
+ "\xf0\xb3"
- "-[BRCClientZone _blockExistingOperationIfNecessary:onNewOperation:]"
- "-[BRCDownloadTrackers document:didCompleteDownloadEtagIfLoser:withError:]"
- "-[BRCFSDownloader _appLibraryForDownload:kind:operationID:]"
- "-[BRCFSDownloader scheduleContentDownloadForItem:serverItem:userInitiated:etagIfLoser:stageFileName:error:]"
- "-[BRCLocalItem(FPFSAdditions) markBouncedToNextAvailableBounceNumber]"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) cloneLatestContentRevisionForItemIdentifier:reply:]_block_invoke_2"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) fetchLatestContentRevisionForItemIdentifier:reply:]_block_invoke_2"
- "-[CKRecord(BRCSerializationAdditions) serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:]"
- "-[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:]"
- "-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke"
- "-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke"
- "-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke"
- "@36@0:8@16i24@28"
- "B60@0:8@16@24B32@36@44^@52"
- "SELECT app_library_rowid FROM client_downloads WHERE throttle_id = %@ AND download_kind = %u AND download_etag = %@   AND transfer_operation = %@"
- "[CRIT] UNREACHABLE: Attempt to download %@ which is uploading%@"
- "[CRIT] UNREACHABLE: Failed to adopt persona for _br_addDomain retry%@"
- "[CRIT] UNREACHABLE: Failed to adopt persona for _br_signalEnumeratorForContainerItemIdentifier retry%@"
- "[CRIT] UNREACHABLE: Received item with unexpected type and no content %@%@"
- "[DEBUG] Generated sync health report with upload failures:%@\ndownload failures:%@\nsync up failures:%@\nzone sync up errors:%@\nzone sync down errors:%@%@"
- "[WARNING] No appLibraryEntry for Downloader[%@-%s-%@] with transfer_operation %@%@"
- "_appLibraryForDownload:kind:operationID:"
- "_blockExistingOperationIfNecessary:onNewOperation:"
- "_br_addDomain:retries:completionHandler:"
- "_br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:"
- "_populateNonMigratedItemEventForLocalDataWithEvent:fileIDData:diagnosticDescriptor:"
- "document:didCompleteDownloadEtagIfLoser:withError:"
- "initWithDocument:stageID:etagIfLoser:"
- "initWithDocumentItem:client:session:etagIfLoser:stageFileName:"
- "markBouncedToNextAvailableBounceNumber"
- "scheduleContentDownloadForItem:serverItem:userInitiated:etagIfLoser:stageFileName:error:"
- "serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:"
- "serializeVersion:diffs:deadInServerTruth:basehashSalt:"
- "trackedVersionFor:withEtagIfLoser:"
- "v44@0:8@16Q24B32@36"
- "v64@0:8@16Q24@32B40C44@48@56"
- "{?=\"accountQuotaUsage\"b1\"bouncedItemsCount\"b1\"bouncedItemsMatrix\"b1\"busyDateNotMigratedCount\"b1\"childItemsNotMigratedCount\"b1\"durationBetweenDbCreationAndMigrationStart\"b1\"ignoredFromSyncItemsNotMigratedCount\"b1\"importTime\"b1\"itemsMigratedWithoutAlreadyMayExistFlag\"b1\"itemsNotFoundInDB\"b1\"itemsNotMigratedCount\"b1\"itemsNotMigratedDelta\"b1\"itemsReconciledInFileProvider\"b1\"itemsReconciledInFileProviderDelta\"b1\"numberOfItemsPendingReconciliation\"b1\"numberOfItemsPendingScanningDisk\"b1\"numberOfItemsPendingScanningProvider\"b1\"numberOfItemsPendingSelection\"b1\"stateOfDownloadJobs\"b1\"stateOfOtherJobs\"b1\"stateOfUploadJobs\"b1\"totalItemCount\"b1\"xpcActivityDasdContext\"b1\"xpcActivityTimeSinceLastActivation\"b1\"xpcActivityTimeSinceLastRegistration\"b1\"typesOfMigratedItemsMask\"b1\"typesOfNonMigratedItemsMask\"b1\"isAccountDataSeparated\"b1\"isStreamResetRunning\"b1\"isSuccessful\"b1\"xpcActivityIsActive\"b1\"xpcActivityRegisteredWithDuet\"b1}"
- "\xf0\xa3"

```
