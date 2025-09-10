## CloudDocsDaemon

> `/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/CloudDocsDaemon`

```diff

-2720.100.117.0.0
-  __TEXT.__text: 0x32a1bc
+2720.120.29.0.0
+  __TEXT.__text: 0x329e20
   __TEXT.__auth_stubs: 0x1d30
-  __TEXT.__objc_methlist: 0x173e4
+  __TEXT.__objc_methlist: 0x1748c
   __TEXT.__const: 0x3e0
-  __TEXT.__cstring: 0x7c785
-  __TEXT.__oslogstring: 0x4393c
-  __TEXT.__gcc_except_tab: 0x1823c
+  __TEXT.__cstring: 0x7ca18
+  __TEXT.__oslogstring: 0x438d3
+  __TEXT.__gcc_except_tab: 0x1804c
   __TEXT.__ustring: 0x36
-  __TEXT.__unwind_info: 0x92c0
-  __TEXT.__objc_classname: 0x2397
-  __TEXT.__objc_methname: 0x3ddc3
-  __TEXT.__objc_methtype: 0x7e7e
-  __TEXT.__objc_stubs: 0x2aec0
-  __DATA_CONST.__got: 0xb90
-  __DATA_CONST.__const: 0x8ac8
-  __DATA_CONST.__objc_classlist: 0x8e8
+  __TEXT.__unwind_info: 0x92a4
+  __TEXT.__objc_classname: 0x23ad
+  __TEXT.__objc_methname: 0x3e07b
+  __TEXT.__objc_methtype: 0x7efb
+  __TEXT.__objc_stubs: 0x2afe0
+  __DATA_CONST.__got: 0xb88
+  __DATA_CONST.__const: 0x8b40
+  __DATA_CONST.__objc_classlist: 0x8f0
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x35f00
-  __DATA_CONST.__objc_selrefs: 0xd560
+  __DATA_CONST.__objc_const: 0x36048
+  __DATA_CONST.__objc_selrefs: 0xd5c8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0xd78
+  __DATA_CONST.__objc_classrefs: 0xd88
   __DATA_CONST.__objc_superrefs: 0x818
   __DATA_CONST.__objc_arraydata: 0xd28
-  __AUTH_CONST.__const: 0x2568
-  __AUTH_CONST.__objc_const: 0x6d80
-  __AUTH_CONST.__cfstring: 0x20240
+  __AUTH_CONST.__const: 0x2508
+  __AUTH_CONST.__objc_const: 0x6dc8
+  __AUTH_CONST.__cfstring: 0x20460
   __AUTH_CONST.__objc_intobj: 0x9d8
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x28

   __AUTH_CONST.__auth_got: 0xea8
   __AUTH.__objc_data: 0x24e0
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x1f74
+  __DATA.__objc_ivar: 0x1f88
   __DATA.__data: 0x2068
-  __DATA.__bss: 0x380
-  __DATA_DIRTY.__objc_data: 0x3430
+  __DATA.__bss: 0x350
+  __DATA_DIRTY.__objc_data: 0x3480
   __DATA_DIRTY.__data: 0x2c8
   __DATA_DIRTY.__bss: 0x230
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 166BB067-9FD5-33A6-A9A9-B0C2548464E3
-  Functions: 14408
-  Symbols:   42973
-  CStrings:  27136
+  UUID: 821B70BE-9D95-3793-BF88-DB08C1312665
+  Functions: 14406
+  Symbols:   42975
+  CStrings:  27191
 
Symbols:
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newAggregatedEventWithIdentifier:recordID:zoneMangledID:error:count:]
+ +[BRCFSDownloaderUtil downloadKindWithEtagIfLoser:options:]
+ +[BRCTrackedVersion trackedVersionFor:withEtagIfLoser:kind:]
+ -[AppTelemetryFPFSMigrationInvestigation hasXpcActivityTimeSinceLastAbleToRun]
+ -[AppTelemetryFPFSMigrationInvestigation setHasXpcActivityTimeSinceLastAbleToRun:]
+ -[AppTelemetryFPFSMigrationInvestigation setXpcActivityTimeSinceLastAbleToRun:]
+ -[AppTelemetryFPFSMigrationInvestigation xpcActivityTimeSinceLastAbleToRun]
+ -[BRCAnalyticsReporter aggregateReportForAppTelemetryIdentifier:error:]
+ -[BRCAnalyticsReporter aggregateReportForAppTelemetryIdentifier:itemID:zoneMangledID:advancedDataProtectionEnabled:error:]
+ -[BRCClientZone _blockExistingOperationIfNecessary:onNewOperation:considerPriority:]
+ -[BRCDownloadContent initWithDocument:stageID:etagIfLoser:downloadKind:]
+ -[BRCFSDownloader scheduleContentDownloadForItem:serverItem:options:etagIfLoser:stageFileName:error:]
+ -[BRCFSDownloader scheduleContentDownloadForItem:serverItem:options:etagIfLoser:stageFileName:error:].cold.1
+ -[BRCFSDownloader scheduleContentDownloadForItem:serverItem:options:etagIfLoser:stageFileName:error:].cold.2
+ -[BRCFSDownloaderBatchEnumerator kind]
+ -[BRCFileProvidingRequestOperation kind]
+ -[BRCLocalItem(CKConversions) structureRecordBeingDeadInServerTruth:stageID:shouldPCSChainStatus:saltGetter:childBasehashSalt:].cold.2
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
+ ___35-[BRCFSDownloader makeContentLive:]_block_invoke.264
+ ___35-[BRCFSDownloader makeContentLive:]_block_invoke.266
+ ___35-[BRCFSDownloader makeContentLive:]_block_invoke.266.cold.1
+ ___49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.462
+ ___49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.488
+ ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.210
+ ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.210.cold.1
+ ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.210.cold.2
+ ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.215
+ ___70-[NSFileProviderManager(BRCAdditions) br_addDomain:completionHandler:]_block_invoke
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.697
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.700
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.699
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.699.cold.1
+ ___86-[NSFileProviderManager(BRCAdditions) br_removeDomain:options:sync:completionHandler:]_block_invoke.6
+ ___86-[NSFileProviderManager(BRCAdditions) br_removeDomain:options:sync:completionHandler:]_block_invoke.6.cold.1
+ ___90-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke_2.cold.1
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.634
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.634.cold.1
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.635
+ ___block_descriptor_48_e8_32s40s_e24_v16?0?<v?"NSError">8ls32l8s40l8
+ ___block_descriptor_68_e8_32s40s48s56s_e23_B16?0"PQLConnection"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48bs_e17_v16?0"NSError"8ls48l8s32l8s40l8
+ ___block_descriptor_76_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.465
+ ___block_literal_global.721
+ _objc_msgSend$_blockExistingOperationIfNecessary:onNewOperation:considerPriority:
+ _objc_msgSend$_collectAggregatedTelemetryForSession:
+ _objc_msgSend$_verifyValueForRecordWithNumber:key:item:error:
+ _objc_msgSend$aggregateReportForAppTelemetryIdentifier:itemID:zoneMangledID:advancedDataProtectionEnabled:error:
+ _objc_msgSend$aggregatedEvents
+ _objc_msgSend$br_errorDescription
+ _objc_msgSend$br_isCKErrorCode:
+ _objc_msgSend$br_signalWorkingSetEnumeratorWithCompletionHandler:
+ _objc_msgSend$downloadKindWithEtagIfLoser:options:
+ _objc_msgSend$executeAsyncXPCWithMaxRetries:completion:xpcInvokeBlock:
+ _objc_msgSend$initWithDocument:stageID:etagIfLoser:downloadKind:
+ _objc_msgSend$newAggregatedEventWithIdentifier:recordID:zoneMangledID:error:count:
+ _objc_msgSend$performWithPersonaID:block:
+ _objc_msgSend$scheduleContentDownloadForItem:serverItem:options:etagIfLoser:stageFileName:error:
+ _objc_msgSend$serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:error:
+ _objc_msgSend$serializeVersion:diffs:deadInServerTruth:basehashSalt:error:
+ _objc_msgSend$trackedVersionFor:withEtagIfLoser:kind:
- +[BRCTrackedVersion trackedVersionFor:withEtagIfLoser:]
- -[BRCClientZone _blockExistingOperationIfNecessary:onNewOperation:]
- -[BRCDownloadContent initWithDocument:stageID:etagIfLoser:]
- -[BRCFSDownloader _appLibraryForDownload:kind:operationID:]
- -[BRCFSDownloader scheduleContentDownloadForItem:serverItem:userInitiated:etagIfLoser:stageFileName:error:]
- -[BRCFSDownloader scheduleContentDownloadForItem:serverItem:userInitiated:etagIfLoser:stageFileName:error:].cold.1
- -[BRCFSDownloader scheduleContentDownloadForItem:serverItem:userInitiated:etagIfLoser:stageFileName:error:].cold.2
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
- _NSFileProviderRootContainerItemIdentifier
- ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke
- ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke.cold.1
- ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke.cold.2
- ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke.cold.3
- ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke.cold.4
- ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke_2
- ___35-[BRCFSDownloader makeContentLive:]_block_invoke.267
- ___35-[BRCFSDownloader makeContentLive:]_block_invoke.269
- ___35-[BRCFSDownloader makeContentLive:]_block_invoke.269.cold.1
- ___49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.441
- ___49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.467
- ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.213
- ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.213.cold.1
- ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.213.cold.2
- ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.218
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.670
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.673
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.672
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.672.cold.1
- ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke
- ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke.cold.1
- ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke.cold.2
- ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke.cold.3
- ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke.cold.4
- ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke_2
- ___86-[NSFileProviderManager(BRCAdditions) br_removeDomain:options:sync:completionHandler:]_block_invoke.8
- ___86-[NSFileProviderManager(BRCAdditions) br_removeDomain:options:sync:completionHandler:]_block_invoke.8.cold.1
- ___90-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke.cold.1
- ___90-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke.cold.2
- ___90-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke.cold.3
- ___90-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke.cold.4
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.607
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.607.cold.1
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.608
- ___block_descriptor_72_e8_32s40s48bs56w_e17_v16?0"NSError"8ls48l8w56l8s32l8s40l8
- ___block_literal_global.444
- ___block_literal_global.694
- _objc_msgSend$_blockExistingOperationIfNecessary:onNewOperation:
- _objc_msgSend$_br_addDomain:retries:completionHandler:
- _objc_msgSend$_br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:
- _objc_msgSend$initWithDocument:stageID:etagIfLoser:
- _objc_msgSend$scheduleContentDownloadForItem:serverItem:userInitiated:etagIfLoser:stageFileName:error:
- _objc_msgSend$serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:
- _objc_msgSend$serializeVersion:diffs:deadInServerTruth:basehashSalt:
- _objc_msgSend$trackedVersionFor:withEtagIfLoser:
CStrings:
+ "\b"
+ "-[BRCClientZone _blockExistingOperationIfNecessary:onNewOperation:considerPriority:]"
+ "-[BRCFSDownloader scheduleContentDownloadForItem:serverItem:options:etagIfLoser:stageFileName:error:]"
+ "-[CKRecord(BRCSerializationAdditions) _verifyValueForRecordWithNumber:key:item:error:]"
+ "-[CKRecord(BRCSerializationAdditions) serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:error:]"
+ "-[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:error:]"
+ "-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke_2"
+ "@44@0:8@16@24@32i40"
+ "@52@0:8i16@20@28@36q44"
+ "B36@0:8@16@24B32"
+ "B52@0:8@16Q24B32@36^@44"
+ "B64@0:8@16@24Q32@40@48^@56"
+ "B72@0:8@16Q24@32B40C44@48@56^@64"
+ "BRCFSDownloaderUtil"
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
+ "_aggregatedEvents"
+ "_blockExistingOperationIfNecessary:onNewOperation:considerPriority:"
+ "_collectAggregatedTelemetryForSession:"
+ "_verifyValueForRecordWithNumber:key:item:error:"
+ "_xpcActivityTimeSinceLastAbleToRun"
+ "aggregateReportForAppTelemetryIdentifier:error:"
+ "aggregateReportForAppTelemetryIdentifier:itemID:zoneMangledID:advancedDataProtectionEnabled:error:"
+ "aggregatedEvents"
+ "br_errorDescription"
+ "br_isCKErrorCode:"
+ "br_signalWorkingSetEnumeratorWithCompletionHandler:"
+ "downloadKindWithEtagIfLoser:options:"
+ "executeAsyncXPCWithMaxRetries:completion:xpcInvokeBlock:"
+ "hasXpcActivityTimeSinceLastAbleToRun"
+ "i32@0:8@16Q24"
+ "initWithDocument:stageID:etagIfLoser:downloadKind:"
+ "newAggregatedEventWithIdentifier:recordID:zoneMangledID:error:count:"
+ "performWithPersonaID:block:"
+ "scheduleContentDownloadForItem:serverItem:options:etagIfLoser:stageFileName:error:"
+ "serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:error:"
+ "serializeVersion:diffs:deadInServerTruth:basehashSalt:error:"
+ "setHasXpcActivityTimeSinceLastAbleToRun:"
+ "setXpcActivityTimeSinceLastAbleToRun:"
+ "trackedVersionFor:withEtagIfLoser:kind:"
+ "v16@?0@?<v@?@\"NSError\">8"
+ "v52@0:8i16@20@28@36@44"
+ "xpcActivityTimeSinceLastAbleToRun"
+ "{?=\"accountQuotaUsage\"b1\"bouncedItemsCount\"b1\"bouncedItemsMatrix\"b1\"busyDateNotMigratedCount\"b1\"childItemsNotMigratedCount\"b1\"durationBetweenDbCreationAndMigrationStart\"b1\"ignoredFromSyncItemsNotMigratedCount\"b1\"importTime\"b1\"itemsMigratedWithoutAlreadyMayExistFlag\"b1\"itemsNotFoundInDB\"b1\"itemsNotMigratedCount\"b1\"itemsNotMigratedDelta\"b1\"itemsReconciledInFileProvider\"b1\"itemsReconciledInFileProviderDelta\"b1\"numberOfItemsPendingReconciliation\"b1\"numberOfItemsPendingScanningDisk\"b1\"numberOfItemsPendingScanningProvider\"b1\"numberOfItemsPendingSelection\"b1\"stateOfDownloadJobs\"b1\"stateOfOtherJobs\"b1\"stateOfUploadJobs\"b1\"totalItemCount\"b1\"xpcActivityDasdContext\"b1\"xpcActivityTimeSinceLastAbleToRun\"b1\"xpcActivityTimeSinceLastActivation\"b1\"xpcActivityTimeSinceLastRegistration\"b1\"typesOfMigratedItemsMask\"b1\"typesOfNonMigratedItemsMask\"b1\"isAccountDataSeparated\"b1\"isStreamResetRunning\"b1\"isSuccessful\"b1\"xpcActivityIsActive\"b1\"xpcActivityRegisteredWithDuet\"b1}"
+ "\xf0\xb3"
- "-[BRCClientZone _blockExistingOperationIfNecessary:onNewOperation:]"
- "-[BRCFSDownloader _appLibraryForDownload:kind:operationID:]"
- "-[BRCFSDownloader scheduleContentDownloadForItem:serverItem:userInitiated:etagIfLoser:stageFileName:error:]"
- "-[CKRecord(BRCSerializationAdditions) serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:]"
- "-[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:]"
- "-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke"
- "-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke"
- "-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke"
- "@36@0:8@16i24@28"
- "B60@0:8@16@24B32@36@44^@52"
- "SELECT app_library_rowid FROM client_downloads WHERE throttle_id = %@ AND download_kind = %u AND download_etag = %@   AND transfer_operation = %@"
- "[CRIT] UNREACHABLE: Failed to adopt persona for _br_addDomain retry%@"
- "[CRIT] UNREACHABLE: Failed to adopt persona for _br_signalEnumeratorForContainerItemIdentifier retry%@"
- "[DEBUG] Generated sync health report with upload failures:%@\ndownload failures:%@\nsync up failures:%@\nzone sync up errors:%@\nzone sync down errors:%@%@"
- "[WARNING] No appLibraryEntry for Downloader[%@-%s-%@] with transfer_operation %@%@"
- "_appLibraryForDownload:kind:operationID:"
- "_blockExistingOperationIfNecessary:onNewOperation:"
- "_br_addDomain:retries:completionHandler:"
- "_br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:"
- "initWithDocument:stageID:etagIfLoser:"
- "scheduleContentDownloadForItem:serverItem:userInitiated:etagIfLoser:stageFileName:error:"
- "serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:"
- "serializeVersion:diffs:deadInServerTruth:basehashSalt:"
- "trackedVersionFor:withEtagIfLoser:"
- "v44@0:8@16Q24B32@36"
- "v64@0:8@16Q24@32B40C44@48@56"
- "{?=\"accountQuotaUsage\"b1\"bouncedItemsCount\"b1\"bouncedItemsMatrix\"b1\"busyDateNotMigratedCount\"b1\"childItemsNotMigratedCount\"b1\"durationBetweenDbCreationAndMigrationStart\"b1\"ignoredFromSyncItemsNotMigratedCount\"b1\"importTime\"b1\"itemsMigratedWithoutAlreadyMayExistFlag\"b1\"itemsNotFoundInDB\"b1\"itemsNotMigratedCount\"b1\"itemsNotMigratedDelta\"b1\"itemsReconciledInFileProvider\"b1\"itemsReconciledInFileProviderDelta\"b1\"numberOfItemsPendingReconciliation\"b1\"numberOfItemsPendingScanningDisk\"b1\"numberOfItemsPendingScanningProvider\"b1\"numberOfItemsPendingSelection\"b1\"stateOfDownloadJobs\"b1\"stateOfOtherJobs\"b1\"stateOfUploadJobs\"b1\"totalItemCount\"b1\"xpcActivityDasdContext\"b1\"xpcActivityTimeSinceLastActivation\"b1\"xpcActivityTimeSinceLastRegistration\"b1\"typesOfMigratedItemsMask\"b1\"typesOfNonMigratedItemsMask\"b1\"isAccountDataSeparated\"b1\"isStreamResetRunning\"b1\"isSuccessful\"b1\"xpcActivityIsActive\"b1\"xpcActivityRegisteredWithDuet\"b1}"
- "\xf0\xa3"

```
