## CloudDocsDaemon

> `/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/CloudDocsDaemon`

```diff

-2461.62.1.0.0
-  __TEXT.__text: 0x331298
+2461.80.8.0.0
+  __TEXT.__text: 0x331830
   __TEXT.__auth_stubs: 0x1d10
-  __TEXT.__objc_methlist: 0x17bdc
+  __TEXT.__objc_methlist: 0x17c5c
   __TEXT.__const: 0x3e0
-  __TEXT.__cstring: 0x7c259
+  __TEXT.__cstring: 0x7c2c0
   __TEXT.__oslogstring: 0x436ba
   __TEXT.__gcc_except_tab: 0x1849c
   __TEXT.__ustring: 0xa
   __TEXT.__unwind_info: 0x9214
   __TEXT.__objc_classname: 0x22e3
-  __TEXT.__objc_methname: 0x3eaab
-  __TEXT.__objc_methtype: 0x84eb
-  __TEXT.__objc_stubs: 0x2b2a0
+  __TEXT.__objc_methname: 0x3ec75
+  __TEXT.__objc_methtype: 0x852a
+  __TEXT.__objc_stubs: 0x2b2e0
   __DATA_CONST.__got: 0xb98
   __DATA_CONST.__const: 0x8948
   __DATA_CONST.__objc_classlist: 0x8b0
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x36850
-  __DATA_CONST.__objc_selrefs: 0xd870
+  __DATA_CONST.__objc_const: 0x368d0
+  __DATA_CONST.__objc_selrefs: 0xd8c0
   __DATA_CONST.__objc_arraydata: 0xdd0
   __AUTH_CONST.__const: 0x24e8
   __AUTH_CONST.__objc_const: 0x6950
-  __AUTH_CONST.__cfstring: 0x206e0
+  __AUTH_CONST.__cfstring: 0x20720
   __AUTH_CONST.__objc_intobj: 0xaf8
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x50

   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0xd40
   __DATA.__objc_superrefs: 0x800
-  __DATA.__objc_ivar: 0x2028
+  __DATA.__objc_ivar: 0x2030
   __DATA.__data: 0x1ff0
   __DATA.__bss: 0x360
   __DATA_DIRTY.__objc_data: 0x3430

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 66C1D940-B5CD-3981-AEF0-AE6996560B88
-  Functions: 14583
-  Symbols:   43302
-  CStrings:  27363
+  UUID: 3A61F826-E2CA-3D42-8B2A-72164529AC53
+  Functions: 14593
+  Symbols:   43326
+  CStrings:  27381
 
Symbols:
+ -[AppTelemetryFPFSMigrationInvestigation hasItemsNotMigratedDelta]
+ -[AppTelemetryFPFSMigrationInvestigation hasItemsReconciledInFileProviderDelta]
+ -[AppTelemetryFPFSMigrationInvestigation itemsNotMigratedDelta]
+ -[AppTelemetryFPFSMigrationInvestigation itemsReconciledInFileProviderDelta]
+ -[AppTelemetryFPFSMigrationInvestigation setHasItemsNotMigratedDelta:]
+ -[AppTelemetryFPFSMigrationInvestigation setHasItemsReconciledInFileProviderDelta:]
+ -[AppTelemetryFPFSMigrationInvestigation setItemsNotMigratedDelta:]
+ -[AppTelemetryFPFSMigrationInvestigation setItemsReconciledInFileProviderDelta:]
+ -[BRCClientZone _isSideSyncOperationBlockedWithName:isWaitingOnShareAccept:]
+ -[BRCClientZone _isSideSyncOperationBlockedWithName:isWaitingOnShareAccept:].cold.1
+ -[BRCClientZone _isSideSyncOperationBlockedWithName:isWaitingOnShareAccept:].cold.2
+ -[BRCClientZone _isSideSyncOperationBlockedWithName:isWaitingOnShareAccept:].cold.3
+ -[BRCClientZone _isSideSyncOperationBlockedWithName:isWaitingOnShareAccept:].cold.4
+ -[BRCClientZone _registerListOperation:shareAcceptOperation:]
+ -[BRCClientZone _registerListOperation:shareAcceptOperation:].cold.1
+ -[BRCClientZone _registerListOperation:shareAcceptOperation:].cold.2
+ -[BRCServerZone zoneCreationState]
+ -[NSError(BRCAdditions) brc_isDatabaseRemovalError]
+ GCC_except_table101
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationInvestigation._itemsNotMigratedDelta
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationInvestigation._itemsReconciledInFileProviderDelta
+ _objc_msgSend$_isSideSyncOperationBlockedWithName:isWaitingOnShareAccept:
+ _objc_msgSend$_registerListOperation:shareAcceptOperation:
+ _objc_msgSend$brc_isDatabaseRemovalError
+ _objc_msgSend$zoneCreationState
- -[BRCClientZone _isSideSyncOperationBlockedWithName:isListDirectoryOp:]
- -[BRCClientZone _isSideSyncOperationBlockedWithName:isListDirectoryOp:].cold.1
- -[BRCClientZone _isSideSyncOperationBlockedWithName:isListDirectoryOp:].cold.2
- -[BRCClientZone _isSideSyncOperationBlockedWithName:isListDirectoryOp:].cold.3
- -[BRCClientZone _isSideSyncOperationBlockedWithName:isListDirectoryOp:].cold.4
- -[BRCClientZone _registerListOperation:]
- -[BRCClientZone _registerListOperation:].cold.1
- -[BRCClientZone _registerListOperation:].cold.2
- _objc_msgSend$_isSideSyncOperationBlockedWithName:isListDirectoryOp:
- _objc_msgSend$_registerListOperation:
CStrings:
+ "-[BRCClientZone _isSideSyncOperationBlockedWithName:isWaitingOnShareAccept:]"
+ "-[BRCClientZone _registerListOperation:shareAcceptOperation:]"
+ "Tq,N,V_itemsNotMigratedDelta"
+ "Tq,N,V_itemsReconciledInFileProviderDelta"
+ "UPDATE client_uploads SET transfer_queue = %@, transfer_operation = call_block(%@, next_retry_stamp), upload_error = %@ WHERE %@"
+ "_isSideSyncOperationBlockedWithName:isWaitingOnShareAccept:"
+ "_itemsNotMigratedDelta"
+ "_itemsReconciledInFileProviderDelta"
+ "_registerListOperation:shareAcceptOperation:"
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
- "UPDATE client_uploads SET  transfer_operation = call_block(%@, next_retry_stamp), upload_error = %@ WHERE %@"
- "_isSideSyncOperationBlockedWithName:isListDirectoryOp:"
- "_registerListOperation:"
- "{?=\"accountQuotaUsage\"b1\"bouncedItemsCount\"b1\"bouncedItemsMatrix\"b1\"busyDateNotMigratedCount\"b1\"childItemsNotMigratedCount\"b1\"durationBetweenDbCreationAndMigrationStart\"b1\"ignoredFromSyncItemsNotMigratedCount\"b1\"importTime\"b1\"itemsMigratedWithoutAlreadyMayExistFlag\"b1\"itemsNotFoundInDB\"b1\"itemsNotMigratedCount\"b1\"itemsReconciledInFileProvider\"b1\"numberOfItemsPendingReconciliation\"b1\"numberOfItemsPendingScanningDisk\"b1\"numberOfItemsPendingScanningProvider\"b1\"numberOfItemsPendingSelection\"b1\"stateOfDownloadJobs\"b1\"stateOfOtherJobs\"b1\"stateOfUploadJobs\"b1\"totalItemCount\"b1\"xpcActivityDasdContext\"b1\"xpcActivityTimeSinceLastActivation\"b1\"xpcActivityTimeSinceLastRegistration\"b1\"typesOfMigratedItemsMask\"b1\"typesOfNonMigratedItemsMask\"b1\"isAccountDataSeparated\"b1\"isStreamResetRunning\"b1\"isSuccessful\"b1\"xpcActivityIsActive\"b1\"xpcActivityRegisteredWithDuet\"b1}"
- "\xf0\x83"

```
