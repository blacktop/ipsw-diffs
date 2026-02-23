## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-4479.100.79.0.4
-  __TEXT.__text: 0x31fbc0
+4479.100.89.0.3
+  __TEXT.__text: 0x3215a0
   __TEXT.__auth_stubs: 0x1a90
-  __TEXT.__objc_methlist: 0x1a9d4
+  __TEXT.__objc_methlist: 0x1aa64
   __TEXT.__const: 0x4e0
-  __TEXT.__cstring: 0x7dcb5
-  __TEXT.__oslogstring: 0x3b548
-  __TEXT.__gcc_except_tab: 0x19e88
+  __TEXT.__cstring: 0x7dfe2
+  __TEXT.__oslogstring: 0x3b6dc
+  __TEXT.__gcc_except_tab: 0x19f70
   __TEXT.__ustring: 0x36
-  __TEXT.__unwind_info: 0xa7a8
+  __TEXT.__unwind_info: 0xa7e0
   __TEXT.__objc_classname: 0x2ae4
-  __TEXT.__objc_methname: 0x45972
-  __TEXT.__objc_methtype: 0x94bb
-  __TEXT.__objc_stubs: 0x2fa60
-  __DATA_CONST.__got: 0x1718
-  __DATA_CONST.__const: 0x94d8
+  __TEXT.__objc_methname: 0x45bbe
+  __TEXT.__objc_methtype: 0x94d2
+  __TEXT.__objc_stubs: 0x2fc60
+  __DATA_CONST.__got: 0x1728
+  __DATA_CONST.__const: 0x9500
   __DATA_CONST.__objc_classlist: 0xa58
   __DATA_CONST.__objc_catlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xea78
+  __DATA_CONST.__objc_selrefs: 0xeaf8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x910
-  __DATA_CONST.__objc_arraydata: 0xe78
+  __DATA_CONST.__objc_arraydata: 0xe98
   __AUTH_CONST.__auth_got: 0xd58
   __AUTH_CONST.__const: 0x2bc0
-  __AUTH_CONST.__cfstring: 0x227c0
-  __AUTH_CONST.__objc_const: 0x3d878
+  __AUTH_CONST.__cfstring: 0x229c0
+  __AUTH_CONST.__objc_const: 0x3d8e8
   __AUTH_CONST.__objc_intobj: 0xbe8
-  __AUTH_CONST.__objc_arrayobj: 0x240
+  __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH.__objc_data: 0x2698
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x1f40
+  __DATA.__objc_ivar: 0x1f48
   __DATA.__data: 0x2800
   __DATA.__bss: 0x210
   __DATA_DIRTY.__objc_data: 0x40d8

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 4BBF399B-7E2C-390F-90AF-CF95ECC02A02
-  Functions: 13755
-  Symbols:   45297
-  CStrings:  27781
+  UUID: 6854D774-36C4-3DE1-84F8-3AB896D26E5D
+  Functions: 13775
+  Symbols:   45365
+  CStrings:  27846
 
Symbols:
+ +[BRCAccountSession _readTelemetryInfoFileAtPath:]
+ -[BRCAccountSession _submitDelayedTelemetryEventIfNeeded:wait:withBlock:].cold.1
+ -[BRCAccountSession captureDBCorruptionInfoWithDescription:error:].cold.2
+ -[BRCAccountSession captureSessionOpenFailedInfoWithError:].cold.2
+ -[BRCAccountSession reportDBIntegrityIssueWithError:]
+ -[BRCAccountsManager _enumerateAccountHandlers:withoutAdoptingPersona:]
+ -[BRCAccountsManager enumerateAccountHandlersWithoutAdoptingPersona:]
+ -[BRCDirectoryItem _performDatabaseIntegrityCheckIfNeededAfterDeleteWithDB:]
+ -[BRCLocalItem _performDatabaseIntegrityCheckIfNeededWithDB:]
+ -[BRCLocalItem _performDatabaseIntegrityCheckIfNeededWithDB:].cold.1
+ -[BRCLocalItem _performDatabaseIntegrityCheckIfNeededWithDB:].cold.2
+ -[BRCServerChangeState lastResetDate]
+ -[BRCServerChangeState lastResetReason]
+ -[BRCServerChangeState setLastResetDate:]
+ -[BRCServerChangeState setLastResetReason:]
+ -[BRCServerZone recordResetWithReason:]
+ -[BRCUserDefaults dbIntegrityCheckParentItemReferences]
+ GCC_except_table128
+ GCC_except_table131
+ GCC_except_table142
+ GCC_except_table156
+ GCC_except_table170
+ GCC_except_table218
+ GCC_except_table225
+ GCC_except_table234
+ GCC_except_table238
+ GCC_except_table249
+ GCC_except_table258
+ GCC_except_table371
+ GCC_except_table491
+ GCC_except_table55
+ GCC_except_table572
+ GCC_except_table66
+ GCC_except_table76
+ _NSFileModificationDate
+ _OBJC_CLASS_$_NSLock
+ _OBJC_IVAR_$_BRCServerChangeState._lastResetDate
+ _OBJC_IVAR_$_BRCServerChangeState._lastResetReason
+ ___132-[BRCAccountSession _recoverNamespaceAndContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:]_block_invoke.284
+ ___148-[BRCServerZone didSyncDownRequestID:serverChangeToken:editedRecords:deletedRecordIDs:deletedShareRecordIDs:allocRankZones:caughtUp:pendingChanges:]_block_invoke.252
+ ___26-[BRCAccountSession close]_block_invoke.367
+ ___26-[BRCStageRegistry resume]_block_invoke.170
+ ___37-[BRCAccountSession destroyLocalData]_block_invoke.390
+ ___37-[BRCAccountSession destroyLocalData]_block_invoke.390.cold.1
+ ___39-[BRCServerZone collectTombstoneRanks:]_block_invoke.265
+ ___39-[BRCServerZone recordResetWithReason:]_block_invoke
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.328
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.332
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.333
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.333.cold.1
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.346
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.331
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.331.cold.1
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.331.cold.2
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.337
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_3.341
+ ___43-[BRCAccountSession _reportBasehashSalting]_block_invoke.266
+ ___43-[BRCAccountSession _reportBasehashSalting]_block_invoke.266.cold.1
+ ___43-[BRCStageRegistry _removeUnusedXattrBlobs]_block_invoke.148
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.392
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.392.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.392.cold.2
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.392.cold.3
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.392.cold.4
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.399.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.402
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.424
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.424.cold.1
+ ___46-[BRCDirectoryItem _deleteFromDB:keepAliases:]_block_invoke.121
+ ___46-[BRCStageRegistry cleanupStagedUploadWithID:]_block_invoke
+ ___46-[BRCStageRegistry cleanupStagedUploadWithID:]_block_invoke.cold.1
+ ___48-[BRCAccountSession openWithError:pushWorkloop:]_block_invoke.234
+ ___50-[BRCServerZone _updateParticipantsTableForShare:]_block_invoke.192
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.307
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.307.cold.1
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.307.cold.2
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.307.cold.3
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.307.cold.4
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.311
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.321
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.321.cold.1
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.321.cold.2
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.321.cold.3
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.321.cold.4
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.325
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.308
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.315
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.315.cold.1
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.315.cold.2
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.315.cold.3
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.315.cold.4
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.322
+ ___51-[BRCFSUploader _scheduleQuotaFetchForDefaultOwner]_block_invoke.275
+ ___53-[BRCAccountSession _pcsChainAllItemsWithSystemTask:]_block_invoke.237
+ ___54-[BRCNotificationPipe _watchItem:options:gatherReply:]_block_invoke.172
+ ___54-[BRCNotificationPipe _watchItem:options:gatherReply:]_block_invoke.172.cold.1
+ ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.437
+ ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.438
+ ___61-[BRCAccountSession _saltPartiallySaltedItemsWithSystemTask:]_block_invoke.254
+ ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke.228
+ ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke_2.229
+ ___66-[BRCAccountSession setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.454
+ ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke.160
+ ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke.163
+ ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke.163.cold.1
+ ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke_2.161
+ ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke_3.162
+ ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke_3.162.cold.1
+ ___71-[BRCAccountsManager _enumerateAccountHandlers:withoutAdoptingPersona:]_block_invoke
+ ___71-[BRCAccountsManager _enumerateAccountHandlers:withoutAdoptingPersona:]_block_invoke_2
+ ___71-[BRCAccountsManager _enumerateAccountHandlers:withoutAdoptingPersona:]_block_invoke_2.cold.1
+ ___73-[BRCAccountSession _submitDelayedTelemetryEventIfNeeded:wait:withBlock:]_block_invoke.cold.3
+ ___83-[BRCAccountSession locateItemWithIdentifier:zoneName:ownerName:completionHandler:]_block_invoke.489
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.430
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.430.cold.1
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.306
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.312
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.312.cold.1
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.313
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.310.cold.1
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.314
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_3
+ ___98-[BRCFSUploader _transferStreamOfSyncContext:didBecomeReadyWithMaxRecordsCount:sizeHint:priority:]_block_invoke.245
+ ___99-[BRCAccountSession learnNewItemIdentifier:forItemIdentifier:zoneName:ownerName:completionHandler:]_block_invoke.487
+ ___block_descriptor_48_e8_32s40bs_e80_v40?0"NSArray<NSFileProviderItem_Private>"8"NSArray"16"NSData"24"NSError"32ls32l8s40l8
+ ___block_descriptor_80_e8_32s40bs48r56r64r72w_e47_v24?0"NSFileProviderItemVersion"8"NSError"16lr48l8w72l8s32l8r56l8r64l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56r64w72w_e17_v16?0"NSError"8ls32l8r56l8w64l8w72l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56r64w72w_e17_v16?0"NSError"8lw64l8w72l8s32l8r56l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72w_e17_v16?0"NSError"8lw72l8s32l8s40l8r64l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72r80w_e5_v8?0ls32l8s40l8s48l8s56l8r72l8w80l8s64l8
+ ___block_literal_global.1051
+ ___block_literal_global.113
+ ___block_literal_global.131
+ ___block_literal_global.138
+ ___block_literal_global.147
+ ___block_literal_global.176
+ ___block_literal_global.203
+ ___block_literal_global.205
+ ___block_literal_global.259
+ ___block_literal_global.2853
+ ___block_literal_global.302
+ ___block_literal_global.310
+ ___block_literal_global.317
+ ___block_literal_global.324
+ ___block_literal_global.369
+ ___block_literal_global.377
+ ___block_literal_global.389
+ ___block_literal_global.401
+ ___block_literal_global.435
+ ___block_literal_global.508
+ _objc_msgSend$_enumerateAccountHandlers:withoutAdoptingPersona:
+ _objc_msgSend$_performDatabaseIntegrityCheckIfNeededAfterDeleteWithDB:
+ _objc_msgSend$_performDatabaseIntegrityCheckIfNeededWithDB:
+ _objc_msgSend$_readTelemetryInfoFileAtPath:
+ _objc_msgSend$brc_errorDBIntegrityDeletingNonEmptyDirectory
+ _objc_msgSend$brc_errorDBIntegrityInsertingOrphanItem
+ _objc_msgSend$dbIntegrityCheckParentItemReferences
+ _objc_msgSend$enumerateAccountHandlersWithoutAdoptingPersona:
+ _objc_msgSend$lastResetDate
+ _objc_msgSend$lastResetReason
+ _objc_msgSend$lock
+ _objc_msgSend$recordResetWithReason:
+ _objc_msgSend$reportDBIntegrityIssueWithError:
+ _objc_msgSend$setLastResetDate:
+ _objc_msgSend$setLastResetReason:
+ _objc_msgSend$unlock
- -[BRCFSUploader _isUploadingPackageAsRegularFileForItem:record:error:].cold.4
- GCC_except_table119
- GCC_except_table162
- GCC_except_table172
- GCC_except_table194
- GCC_except_table224
- GCC_except_table233
- GCC_except_table262
- GCC_except_table272
- GCC_except_table298
- GCC_except_table367
- GCC_except_table485
- GCC_except_table571
- ___132-[BRCAccountSession _recoverNamespaceAndContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:]_block_invoke.281
- ___148-[BRCServerZone didSyncDownRequestID:serverChangeToken:editedRecords:deletedRecordIDs:deletedShareRecordIDs:allocRankZones:caughtUp:pendingChanges:]_block_invoke.246
- ___26-[BRCAccountSession close]_block_invoke.364
- ___26-[BRCStageRegistry resume]_block_invoke.158
- ___37-[BRCAccountSession destroyLocalData]_block_invoke.387
- ___37-[BRCAccountSession destroyLocalData]_block_invoke.387.cold.1
- ___39-[BRCServerZone collectTombstoneRanks:]_block_invoke.259
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.325
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.326
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.330
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.330.cold.1
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.343
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.328
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.328.cold.1
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.328.cold.2
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.334
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_3.338
- ___43-[BRCAccountSession _reportBasehashSalting]_block_invoke.263
- ___43-[BRCAccountSession _reportBasehashSalting]_block_invoke.263.cold.1
- ___43-[BRCStageRegistry _removeUnusedXattrBlobs]_block_invoke.136
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.389
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.389.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.389.cold.2
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.389.cold.3
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.389.cold.4
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.396
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.396.cold.1
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.421
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.421.cold.1
- ___46-[BRCDirectoryItem _deleteFromDB:keepAliases:]_block_invoke.116
- ___47-[BRCAccountsManager enumerateAccountHandlers:]_block_invoke
- ___47-[BRCAccountsManager enumerateAccountHandlers:]_block_invoke_2
- ___47-[BRCAccountsManager enumerateAccountHandlers:]_block_invoke_2.cold.1
- ___48-[BRCAccountSession openWithError:pushWorkloop:]_block_invoke.231
- ___50-[BRCServerZone _updateParticipantsTableForShare:]_block_invoke.186
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.304
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.304.cold.1
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.304.cold.2
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.304.cold.3
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.304.cold.4
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.308
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.318
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.318.cold.1
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.318.cold.2
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.318.cold.3
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.318.cold.4
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.322
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.305
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.312
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.312.cold.1
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.312.cold.2
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.312.cold.3
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.312.cold.4
- ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.319
- ___51-[BRCFSUploader _scheduleQuotaFetchForDefaultOwner]_block_invoke.272
- ___53-[BRCAccountSession _pcsChainAllItemsWithSystemTask:]_block_invoke.234
- ___54-[BRCNotificationPipe _watchItem:options:gatherReply:]_block_invoke.167
- ___54-[BRCNotificationPipe _watchItem:options:gatherReply:]_block_invoke.169.cold.1
- ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.434
- ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.435
- ___61-[BRCAccountSession _saltPartiallySaltedItemsWithSystemTask:]_block_invoke.248
- ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke.225
- ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke_2.226
- ___66-[BRCAccountSession setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.451
- ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke.158
- ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke.162
- ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke.162.cold.1
- ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke_2.160
- ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke_3.161
- ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke_3.161.cold.1
- ___83-[BRCAccountSession locateItemWithIdentifier:zoneName:ownerName:completionHandler:]_block_invoke.486
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.427
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.427.cold.1
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.302
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.308
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.308.cold.1
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.309
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.306
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.306.cold.1
- ___98-[BRCFSUploader _transferStreamOfSyncContext:didBecomeReadyWithMaxRecordsCount:sizeHint:priority:]_block_invoke.242
- ___99-[BRCAccountSession learnNewItemIdentifier:forItemIdentifier:zoneName:ownerName:completionHandler:]_block_invoke.484
- ___block_descriptor_48_e8_32r40w_e17_v16?0"NSError"8lw40l8r32l8
- ___block_descriptor_48_e8_32s40bs_e72_v40?0"NSArray<NSFileProviderItem>"8"NSArray"16"NSData"24"NSError"32ls32l8s40l8
- ___block_descriptor_64_e8_32s40r48w56w_e17_v16?0"NSError"8lw48l8w56l8r40l8s32l8
- ___block_descriptor_72_e8_32s40s48s56r64w_e5_v8?0ls32l8s40l8s48l8w64l8r56l8
- ___block_descriptor_80_e8_32s40s48bs56r64r72r_e47_v24?0"NSFileProviderItemVersion"8"NSError"16lr56l8s32l8s40l8r64l8r72l8s48l8
- ___block_literal_global.1031
- ___block_literal_global.110
- ___block_literal_global.116
- ___block_literal_global.164
- ___block_literal_global.200
- ___block_literal_global.202
- ___block_literal_global.256
- ___block_literal_global.2850
- ___block_literal_global.299
- ___block_literal_global.314
- ___block_literal_global.321
- ___block_literal_global.366
- ___block_literal_global.374
- ___block_literal_global.386
- ___block_literal_global.398
- ___block_literal_global.432
- ___block_literal_global.504
CStrings:
+ "  %@"
+ " (%@)"
+ "+[BRCAccountSession _readTelemetryInfoFileAtPath:]"
+ ", last-reset:%@"
+ "-[BRCAccountsManager _enumerateAccountHandlers:withoutAdoptingPersona:]_block_invoke_2"
+ "-[BRCDirectoryItem _performDatabaseIntegrityCheckIfNeededAfterDeleteWithDB:]"
+ "-[BRCLocalItem _performDatabaseIntegrityCheckIfNeededWithDB:]"
+ "-[BRCStageRegistry cleanupStagedUploadWithID:]_block_invoke"
+ "-dup"
+ "/Library/Caches/com.apple.xbs/88193C22-C511-4C2E-AAB2-07EAEF658C22/TemporaryDirectory.w9SYU2/Sources/CloudDocs_plugins/core/shared/account/BRCAccountSession.m"
+ "/Library/Caches/com.apple.xbs/88193C22-C511-4C2E-AAB2-07EAEF658C22/TemporaryDirectory.w9SYU2/Sources/CloudDocs_plugins/core/shared/account/BRCAccountsManager.m"
+ "/Library/Caches/com.apple.xbs/88193C22-C511-4C2E-AAB2-07EAEF658C22/TemporaryDirectory.w9SYU2/Sources/CloudDocs_plugins/core/shared/containers/BRCClientZone.m"
+ "/Library/Caches/com.apple.xbs/88193C22-C511-4C2E-AAB2-07EAEF658C22/TemporaryDirectory.w9SYU2/Sources/CloudDocs_plugins/core/shared/containers/BRCContainerScheduler.m"
+ "/Library/Caches/com.apple.xbs/88193C22-C511-4C2E-AAB2-07EAEF658C22/TemporaryDirectory.w9SYU2/Sources/CloudDocs_plugins/core/shared/containers/BRCServerZone.m"
+ "/Library/Caches/com.apple.xbs/88193C22-C511-4C2E-AAB2-07EAEF658C22/TemporaryDirectory.w9SYU2/Sources/CloudDocs_plugins/core/shared/daemon/BRCDaemon.m"
+ "/Library/Caches/com.apple.xbs/88193C22-C511-4C2E-AAB2-07EAEF658C22/TemporaryDirectory.w9SYU2/Sources/CloudDocs_plugins/core/shared/database/BRCClientDatabaseFacade.m"
+ "/Library/Caches/com.apple.xbs/88193C22-C511-4C2E-AAB2-07EAEF658C22/TemporaryDirectory.w9SYU2/Sources/CloudDocs_plugins/core/shared/database/BRCClientState.m"
+ "/Library/Caches/com.apple.xbs/88193C22-C511-4C2E-AAB2-07EAEF658C22/TemporaryDirectory.w9SYU2/Sources/CloudDocs_plugins/core/shared/database/BRCDatabaseManager.m"
+ "/Library/Caches/com.apple.xbs/88193C22-C511-4C2E-AAB2-07EAEF658C22/TemporaryDirectory.w9SYU2/Sources/CloudDocs_plugins/core/shared/database/BRCDatabaseSchema.m"
+ "/Library/Caches/com.apple.xbs/88193C22-C511-4C2E-AAB2-07EAEF658C22/TemporaryDirectory.w9SYU2/Sources/CloudDocs_plugins/core/shared/database/BRCServerPersistedState.m"
+ "/Library/Caches/com.apple.xbs/88193C22-C511-4C2E-AAB2-07EAEF658C22/TemporaryDirectory.w9SYU2/Sources/CloudDocs_plugins/core/shared/foundation/BRCFairScheduler.m"
+ "/Library/Caches/com.apple.xbs/88193C22-C511-4C2E-AAB2-07EAEF658C22/TemporaryDirectory.w9SYU2/Sources/CloudDocs_plugins/core/shared/foundation/BRCPQLConnection.m"
+ "/Library/Caches/com.apple.xbs/88193C22-C511-4C2E-AAB2-07EAEF658C22/TemporaryDirectory.w9SYU2/Sources/CloudDocs_plugins/core/shared/items/BRCItemID.m"
+ "/Library/Caches/com.apple.xbs/88193C22-C511-4C2E-AAB2-07EAEF658C22/TemporaryDirectory.w9SYU2/Sources/CloudDocs_plugins/core/shared/notifs/BRCAccountHandler.m"
+ "/Library/Caches/com.apple.xbs/88193C22-C511-4C2E-AAB2-07EAEF658C22/TemporaryDirectory.w9SYU2/Sources/CloudDocs_plugins/core/shared/sync/records/CKRecord+BRCItemAdditions.m"
+ "/Library/Caches/com.apple.xbs/88193C22-C511-4C2E-AAB2-07EAEF658C22/TemporaryDirectory.w9SYU2/Sources/CloudDocs_plugins/core/shared/sync/transfers/BRCTransferStream.m"
+ "<unable to read>"
+ "DBIntegrtiry"
+ "Database Integrity Issue"
+ "Database Integrity Issue - %@"
+ "SELECT 1 FROM client_items WHERE item_id = %@ AND zone_rowid = %@ LIMIT 1"
+ "SELECT rowid, item_id, item_localname FROM client_items WHERE item_parent_id = %@   AND item_parent_zone_rowid = %@ LIMIT 1"
+ "T@\"NSDate\",&,N,V_lastResetDate"
+ "T@\"NSString\",&,N,V_lastResetReason"
+ "[CRIT] Assertion failed: parentExists.boolValue%@"
+ "[CRIT] UNREACHABLE: Inserted an item that is referencing bad parent%@"
+ "[CRIT] UNREACHABLE: We have orphan item: rowid=%llu, item_id=%@, name=%@%@"
+ "[DEBUG] Cleaning stage ID %@%@"
+ "[DEBUG] Error marking %@ as submitted: %{errno}d%@"
+ "[DEBUG] File at path %@ is directory: [%s]%@"
+ "[DEBUG] No item exists at the URL's path: %@, trying %@%@"
+ "[DEBUG] Removed existing %@%@"
+ "[DEBUG] Successfully marked %@ as submitted%@"
+ "[DEBUG] Telemetry at %@ has already been submitted, skipping%@"
+ "_enumerateAccountHandlers:withoutAdoptingPersona:"
+ "_lastResetDate"
+ "_lastResetReason"
+ "_performDatabaseIntegrityCheckIfNeededAfterDeleteWithDB:"
+ "_performDatabaseIntegrityCheckIfNeededWithDB:"
+ "_readTelemetryInfoFileAtPath:"
+ "brc_errorDBIntegrityDeletingNonEmptyDirectory"
+ "brc_errorDBIntegrityInsertingOrphanItem"
+ "com.apple.bird.telemetry-submitted"
+ "db.integrity-check.parent-item-references"
+ "dbIntegrityCheckParentItemReferences"
+ "enumerateAccountHandlersWithoutAdoptingPersona:"
+ "error_info: %@ (exception: %@)"
+ "error_info: %@ (modified: %@)"
+ "executed a query that breaks database integrity"
+ "lastResetDate"
+ "lastResetReason"
+ "lock"
+ "recordResetWithReason:"
+ "reportDBIntegrityIssueWithError:"
+ "setLastResetDate:"
+ "setLastResetReason:"
+ "unlock"
+ "v28@0:8@?16B24"
+ "v40@0:8@\"NSData\"16Q24@?<v@?@\"NSArray<NSFileProviderItem_Private>\"@\"NSArray\"@\"NSData\"@\"NSError\">32"
+ "v40@?0@\"NSArray<NSFileProviderItem_Private>\"8@\"NSArray\"16@\"NSData\"24@\"NSError\"32"
- "-[BRCAccountsManager enumerateAccountHandlers:]_block_invoke_2"
- "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/account/BRCAccountSession.m"
- "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/account/BRCAccountsManager.m"
- "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/containers/BRCClientZone.m"
- "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/containers/BRCContainerScheduler.m"
- "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/containers/BRCServerZone.m"
- "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/daemon/BRCDaemon.m"
- "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/database/BRCClientDatabaseFacade.m"
- "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/database/BRCClientState.m"
- "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/database/BRCDatabaseManager.m"
- "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/database/BRCDatabaseSchema.m"
- "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/database/BRCServerPersistedState.m"
- "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/foundation/BRCFairScheduler.m"
- "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/foundation/BRCPQLConnection.m"
- "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/items/BRCItemID.m"
- "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/notifs/BRCAccountHandler.m"
- "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/sync/records/CKRecord+BRCItemAdditions.m"
- "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/sync/transfers/BRCTransferStream.m"
- "[DEBUG] Error while deleting %@ - %@%@"
- "[DEBUG] File at path is directory: [%s]%@"
- "[DEBUG] Successfully deleted %@%@"
- "v40@0:8@\"NSData\"16Q24@?<v@?@\"NSArray<NSFileProviderItem>\"@\"NSArray\"@\"NSData\"@\"NSError\">32"
- "v40@?0@\"NSArray<NSFileProviderItem>\"8@\"NSArray\"16@\"NSData\"24@\"NSError\"32"

```
