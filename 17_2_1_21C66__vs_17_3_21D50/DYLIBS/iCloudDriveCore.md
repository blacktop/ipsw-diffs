## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-2461.62.1.0.0
-  __TEXT.__text: 0x2bcb90
+2461.80.8.0.0
+  __TEXT.__text: 0x2bd174
   __TEXT.__auth_stubs: 0x1b20
-  __TEXT.__objc_methlist: 0x15d24
+  __TEXT.__objc_methlist: 0x15da4
   __TEXT.__const: 0x368
-  __TEXT.__cstring: 0x716a6
-  __TEXT.__oslogstring: 0x36f60
-  __TEXT.__gcc_except_tab: 0x1304c
+  __TEXT.__cstring: 0x71719
+  __TEXT.__oslogstring: 0x36f59
+  __TEXT.__gcc_except_tab: 0x13044
   __TEXT.__ustring: 0x2be
   __TEXT.__unwind_info: 0x8018
   __TEXT.__objc_classname: 0x2075
-  __TEXT.__objc_methname: 0x39e5b
-  __TEXT.__objc_methtype: 0x70d5
-  __TEXT.__objc_stubs: 0x27760
+  __TEXT.__objc_methname: 0x3a031
+  __TEXT.__objc_methtype: 0x7114
+  __TEXT.__objc_stubs: 0x277c0
   __DATA_CONST.__got: 0xb00
   __DATA_CONST.__const: 0x7de8
   __DATA_CONST.__objc_classlist: 0x830
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x30dd0
-  __DATA_CONST.__objc_selrefs: 0xc838
+  __DATA_CONST.__objc_const: 0x30e50
+  __DATA_CONST.__objc_selrefs: 0xc880
   __DATA_CONST.__objc_arraydata: 0xe80
-  __AUTH_CONST.__cfstring: 0x1f940
+  __AUTH_CONST.__cfstring: 0x1f980
   __AUTH_CONST.__objc_const: 0x62f8
   __AUTH_CONST.__const: 0x23b0
   __AUTH_CONST.__objc_intobj: 0xb70

   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0xc88
   __DATA.__objc_superrefs: 0x778
-  __DATA.__objc_ivar: 0x1c54
+  __DATA.__objc_ivar: 0x1c5c
   __DATA.__data: 0x1e08
   __DATA.__bss: 0x230
   __DATA_DIRTY.__objc_data: 0x2a80

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 12920
-  Symbols:   38687
-  CStrings:  20782
+  Functions: 12932
+  Symbols:   38716
+  CStrings:  20798
 
Symbols:
+ -[AppTelemetryFPFSMigrationInvestigation hasItemsNotMigratedDelta]
+ -[AppTelemetryFPFSMigrationInvestigation hasItemsReconciledInFileProviderDelta]
+ -[AppTelemetryFPFSMigrationInvestigation itemsNotMigratedDelta]
+ -[AppTelemetryFPFSMigrationInvestigation itemsReconciledInFileProviderDelta]
+ -[AppTelemetryFPFSMigrationInvestigation setHasItemsNotMigratedDelta:]
+ -[AppTelemetryFPFSMigrationInvestigation setHasItemsReconciledInFileProviderDelta:]
+ -[AppTelemetryFPFSMigrationInvestigation setItemsNotMigratedDelta:]
+ -[AppTelemetryFPFSMigrationInvestigation setItemsReconciledInFileProviderDelta:]
+ -[BRCAccountSessionFPFS(FPFSAdditions) _populateFPFSImportStatusTelemetryEventForEvent:withFPImportReport:itemsNotMigrated:]
+ -[BRCClientZone _isSideSyncOperationBlockedWithName:isWaitingOnShareAccept:]
+ -[BRCClientZone _isSideSyncOperationBlockedWithName:isWaitingOnShareAccept:].cold.1
+ -[BRCClientZone _isSideSyncOperationBlockedWithName:isWaitingOnShareAccept:].cold.2
+ -[BRCClientZone _isSideSyncOperationBlockedWithName:isWaitingOnShareAccept:].cold.3
+ -[BRCClientZone _isSideSyncOperationBlockedWithName:isWaitingOnShareAccept:].cold.4
+ -[BRCClientZone _registerListOperation:shareAcceptOperation:]
+ -[BRCClientZone _registerListOperation:shareAcceptOperation:].cold.1
+ -[BRCClientZone _registerListOperation:shareAcceptOperation:].cold.2
+ -[BRCFSUploader _shouldReingestAfterUploadErrorWithItem:record:]
+ -[BRCFSUploader _shouldReingestAfterUploadErrorWithItem:record:].cold.1
+ -[BRCFSUploader _shouldReingestAfterUploadErrorWithItem:record:].cold.2
+ -[BRCServerZone zoneCreationState]
+ -[NSError(BRCAdditions) brc_isDatabaseRemovalError]
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationInvestigation._itemsNotMigratedDelta
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationInvestigation._itemsReconciledInFileProviderDelta
+ _objc_msgSend$_isSideSyncOperationBlockedWithName:isWaitingOnShareAccept:
+ _objc_msgSend$_populateFPFSImportStatusTelemetryEventForEvent:withFPImportReport:itemsNotMigrated:
+ _objc_msgSend$_registerListOperation:shareAcceptOperation:
+ _objc_msgSend$_shouldReingestAfterUploadErrorWithItem:record:
+ _objc_msgSend$brc_isDatabaseRemovalError
+ _objc_msgSend$setItemsNotMigratedDelta:
+ _objc_msgSend$setItemsReconciledInFileProviderDelta:
+ _objc_msgSend$zoneCreationState
- -[BRCAccountSessionFPFS(FPFSAdditions) _populateFPFSImportStatusTelemetryEventForEvent:withFPImportReport:]
- -[BRCClientZone _isSideSyncOperationBlockedWithName:isListDirectoryOp:]
- -[BRCClientZone _isSideSyncOperationBlockedWithName:isListDirectoryOp:].cold.1
- -[BRCClientZone _isSideSyncOperationBlockedWithName:isListDirectoryOp:].cold.2
- -[BRCClientZone _isSideSyncOperationBlockedWithName:isListDirectoryOp:].cold.3
- -[BRCClientZone _isSideSyncOperationBlockedWithName:isListDirectoryOp:].cold.4
- -[BRCClientZone _registerListOperation:]
- -[BRCClientZone _registerListOperation:].cold.1
- -[BRCClientZone _registerListOperation:].cold.2
- -[BRCFSUploader _fileForUploadExistsInStage:record:]
- _objc_msgSend$_fileForUploadExistsInStage:record:
- _objc_msgSend$_isSideSyncOperationBlockedWithName:isListDirectoryOp:
- _objc_msgSend$_populateFPFSImportStatusTelemetryEventForEvent:withFPImportReport:
- _objc_msgSend$_registerListOperation:
- _objc_msgSend$itemEnumerator
CStrings:
+ "-[BRCClientZone _isSideSyncOperationBlockedWithName:isWaitingOnShareAccept:]"
+ "-[BRCClientZone _registerListOperation:shareAcceptOperation:]"
+ "-[BRCFSUploader _shouldReingestAfterUploadErrorWithItem:record:]"
+ "Tq,N,V_itemsNotMigratedDelta"
+ "Tq,N,V_itemsReconciledInFileProviderDelta"
+ "UPDATE client_uploads SET transfer_queue = %@, transfer_operation = call_block(%@, next_retry_stamp), upload_error = %@ WHERE %@"
+ "[DEBUG] Couldn't find %@ on disk%@"
+ "[DEBUG] Found different gen count on disk for %@%@"
+ "[DEBUG] We received an asset unavailable error but it exists in the correct place. Computing new record and retrying upload%@"
+ "_isSideSyncOperationBlockedWithName:isWaitingOnShareAccept:"
+ "_itemsNotMigratedDelta"
+ "_itemsReconciledInFileProviderDelta"
+ "_populateFPFSImportStatusTelemetryEventForEvent:withFPImportReport:itemsNotMigrated:"
+ "_registerListOperation:shareAcceptOperation:"
+ "_shouldReingestAfterUploadErrorWithItem:record:"
+ "brc_isDatabaseRemovalError"
+ "hasItemsNotMigratedDelta"
+ "hasItemsReconciledInFileProviderDelta"
+ "itemsNotMigratedDelta"
+ "itemsReconciledInFileProviderDelta"
+ "setHasItemsNotMigratedDelta:"
+ "setHasItemsReconciledInFileProviderDelta:"
+ "setItemsNotMigratedDelta:"
+ "setItemsReconciledInFileProviderDelta:"
+ "zoneCreationState"
+ "{?=\"accountQuotaUsage\"b1\"bouncedItemsCount\"b1\"bouncedItemsMatrix\"b1\"busyDateNotMigratedCount\"b1\"childItemsNotMigratedCount\"b1\"durationBetweenDbCreationAndMigrationStart\"b1\"ignoredFromSyncItemsNotMigratedCount\"b1\"importTime\"b1\"itemsMigratedWithoutAlreadyMayExistFlag\"b1\"itemsNotFoundInDB\"b1\"itemsNotMigratedCount\"b1\"itemsNotMigratedDelta\"b1\"itemsReconciledInFileProvider\"b1\"itemsReconciledInFileProviderDelta\"b1\"numberOfItemsPendingReconciliation\"b1\"numberOfItemsPendingScanningDisk\"b1\"numberOfItemsPendingScanningProvider\"b1\"numberOfItemsPendingSelection\"b1\"stateOfDownloadJobs\"b1\"stateOfOtherJobs\"b1\"stateOfUploadJobs\"b1\"totalItemCount\"b1\"xpcActivityDasdContext\"b1\"xpcActivityTimeSinceLastActivation\"b1\"xpcActivityTimeSinceLastRegistration\"b1\"typesOfMigratedItemsMask\"b1\"typesOfNonMigratedItemsMask\"b1\"isAccountDataSeparated\"b1\"isStreamResetRunning\"b1\"isSuccessful\"b1\"xpcActivityIsActive\"b1\"xpcActivityRegisteredWithDuet\"b1}"
+ "\xf0\xa3"
- "-[BRCClientZone _isSideSyncOperationBlockedWithName:isListDirectoryOp:]"
- "-[BRCClientZone _registerListOperation:]"
- "-[BRCFSUploader _fileForUploadExistsInStage:record:]"
- "UPDATE client_uploads SET  transfer_operation = call_block(%@, next_retry_stamp), upload_error = %@ WHERE %@"
- "[DEBUG] We received an asset unavailable error but it exists in the correct place. This must be a file protected file or a rapid edit after the first edit%@"
- "[WARNING] CKAsset for %@ is pointing to the wrong device ID%@"
- "_fileForUploadExistsInStage:record:"
- "_isSideSyncOperationBlockedWithName:isListDirectoryOp:"
- "_populateFPFSImportStatusTelemetryEventForEvent:withFPImportReport:"
- "_registerListOperation:"
- "itemEnumerator"
- "{?=\"accountQuotaUsage\"b1\"bouncedItemsCount\"b1\"bouncedItemsMatrix\"b1\"busyDateNotMigratedCount\"b1\"childItemsNotMigratedCount\"b1\"durationBetweenDbCreationAndMigrationStart\"b1\"ignoredFromSyncItemsNotMigratedCount\"b1\"importTime\"b1\"itemsMigratedWithoutAlreadyMayExistFlag\"b1\"itemsNotFoundInDB\"b1\"itemsNotMigratedCount\"b1\"itemsReconciledInFileProvider\"b1\"numberOfItemsPendingReconciliation\"b1\"numberOfItemsPendingScanningDisk\"b1\"numberOfItemsPendingScanningProvider\"b1\"numberOfItemsPendingSelection\"b1\"stateOfDownloadJobs\"b1\"stateOfOtherJobs\"b1\"stateOfUploadJobs\"b1\"totalItemCount\"b1\"xpcActivityDasdContext\"b1\"xpcActivityTimeSinceLastActivation\"b1\"xpcActivityTimeSinceLastRegistration\"b1\"typesOfMigratedItemsMask\"b1\"typesOfNonMigratedItemsMask\"b1\"isAccountDataSeparated\"b1\"isStreamResetRunning\"b1\"isSuccessful\"b1\"xpcActivityIsActive\"b1\"xpcActivityRegisteredWithDuet\"b1}"
- "\xf0\x83"

```
