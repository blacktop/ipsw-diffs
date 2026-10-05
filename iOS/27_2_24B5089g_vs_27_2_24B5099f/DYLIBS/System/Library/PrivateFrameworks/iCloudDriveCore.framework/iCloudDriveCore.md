## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-5168.40.149.0.1
-  __TEXT.__text: 0x302560
-  __TEXT.__objc_methlist: 0x1c21c
+5168.40.162.0.0
+  __TEXT.__text: 0x30255c
+  __TEXT.__objc_methlist: 0x1c204
   __TEXT.__const: 0x4f0
-  __TEXT.__cstring: 0x845e9
-  __TEXT.__oslogstring: 0x3ee91
-  __TEXT.__gcc_except_tab: 0x17ad8
+  __TEXT.__cstring: 0x849ab
+  __TEXT.__oslogstring: 0x3ee7b
+  __TEXT.__gcc_except_tab: 0x17adc
   __TEXT.__ustring: 0x36
-  __TEXT.__unwind_info: 0xd568
+  __TEXT.__unwind_info: 0xd570
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa150
+  __DATA_CONST.__const: 0xa1f8
   __DATA_CONST.__objc_classlist: 0xad0
   __DATA_CONST.__objc_catlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x2d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf318
+  __DATA_CONST.__objc_selrefs: 0xf310
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x968
   __DATA_CONST.__objc_arraydata: 0xeb8
   __DATA_CONST.__got: 0x17b8
   __AUTH_CONST.__const: 0x2d28
-  __AUTH_CONST.__cfstring: 0x23b00
-  __AUTH_CONST.__objc_const: 0x42388
+  __AUTH_CONST.__cfstring: 0x23b20
+  __AUTH_CONST.__objc_const: 0x423a8
   __AUTH_CONST.__objc_intobj: 0xc18
   __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0xf0

   __AUTH_CONST.__auth_got: 0xda0
   __AUTH.__objc_data: 0x2698
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x2050
+  __DATA.__objc_ivar: 0x2054
   __DATA.__data: 0x2ab0
   __DATA_DIRTY.__objc_data: 0x4588
   __DATA_DIRTY.__data: 0xd0

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14323
-  Symbols:   18399
-  CStrings:  12261
+  Functions: 14324
+  Symbols:   18404
+  CStrings:  12267
 
Symbols:
+ -[BRCFetchRecordSubResourcesHandler saveChangedRecords:deletedRecordIDs:deletedShareRecordIDs:clientChangeToken:serverChangeToken:caughtUp:pendingChanges:shareIDsFromDeltaSync:]
+ -[BRCFetchRecordSubResourcesOperation addRecord:fromDeltaSync:]
+ -[BRCServerZone _populateParticipantsAndSendUserNotificationsIfNeededWithShare:fromDeltaSync:]
+ -[BRCServerZone _saveEditedRecord:zonesNeedingAllocRanks:fromDeltaSync:error:]
+ -[BRCServerZone _saveEditedShareRecord:fromDeltaSync:error:]
+ -[BRCServerZone _saveEditedShareRecords:deletedShareRecordIDs:zonesNeedingAllocRanks:shareIDsFromDeltaSync:]
+ -[BRCServerZone _savePendingChangesSharesIgnoringRecordIDs:zonesNeedingAllocRanks:pendingChangeStream:fromDeltaSync:]
+ -[BRCServerZone _sendApprovedNotificationIfNeededWithShare:fromDeltaSync:]
+ -[BRCServerZone _shouldSendRequestForAccessNotificationFromDeltaSync:]
+ -[BRCServerZone didSyncDownRequestID:serverChangeToken:editedRecords:deletedRecordIDs:deletedShareRecordIDs:allocRankZones:caughtUp:pendingChanges:shareIDsFromDeltaSync:]
+ GCC_except_table106
+ GCC_except_table133
+ GCC_except_table139
+ GCC_except_table142
+ GCC_except_table166
+ GCC_except_table169
+ GCC_except_table174
+ GCC_except_table186
+ GCC_except_table193
+ GCC_except_table199
+ GCC_except_table210
+ GCC_except_table213
+ GCC_except_table218
+ GCC_except_table223
+ GCC_except_table229
+ GCC_except_table234
+ GCC_except_table237
+ GCC_except_table241
+ GCC_except_table255
+ GCC_except_table272
+ GCC_except_table280
+ GCC_except_table284
+ GCC_except_table305
+ GCC_except_table310
+ GCC_except_table333
+ GCC_except_table336
+ GCC_except_table339
+ GCC_except_table346
+ GCC_except_table361
+ GCC_except_table364
+ GCC_except_table369
+ GCC_except_table372
+ GCC_except_table376
+ GCC_except_table380
+ GCC_except_table383
+ GCC_except_table393
+ GCC_except_table399
+ GCC_except_table404
+ GCC_except_table407
+ GCC_except_table413
+ GCC_except_table418
+ GCC_except_table422
+ GCC_except_table427
+ GCC_except_table432
+ GCC_except_table435
+ GCC_except_table443
+ GCC_except_table446
+ GCC_except_table449
+ GCC_except_table455
+ GCC_except_table466
+ GCC_except_table470
+ GCC_except_table476
+ GCC_except_table480
+ GCC_except_table492
+ GCC_except_table499
+ GCC_except_table79
+ _OBJC_IVAR_$_BRCFetchRecordSubResourcesOperation._shareIDsFromDeltaSync
+ ___113-[BRCFSUploader transferStreamOfSyncContext:didBecomeReadyWithMaxRecordsCount:sizeHint:priority:completionBlock:]_block_invoke_2
+ ___117-[BRCServerZone _savePendingChangesSharesIgnoringRecordIDs:zonesNeedingAllocRanks:pendingChangeStream:fromDeltaSync:]_block_invoke
+ ___117-[BRCServerZone _savePendingChangesSharesIgnoringRecordIDs:zonesNeedingAllocRanks:pendingChangeStream:fromDeltaSync:]_block_invoke_2
+ ___170-[BRCServerZone didSyncDownRequestID:serverChangeToken:editedRecords:deletedRecordIDs:deletedShareRecordIDs:allocRankZones:caughtUp:pendingChanges:shareIDsFromDeltaSync:]_block_invoke
+ ___177-[BRCFetchRecordSubResourcesHandler saveChangedRecords:deletedRecordIDs:deletedShareRecordIDs:clientChangeToken:serverChangeToken:caughtUp:pendingChanges:shareIDsFromDeltaSync:]_block_invoke
+ ___60-[BRCServerZone _saveEditedShareRecord:fromDeltaSync:error:]_block_invoke
+ ___74-[BRCServerZone _sendApprovedNotificationIfNeededWithShare:fromDeltaSync:]_block_invoke
+ ___94-[BRCServerZone _populateParticipantsAndSendUserNotificationsIfNeededWithShare:fromDeltaSync:]_block_invoke
+ ___block_descriptor_137_e8_32s40s48s56s64s72s80s88s96s104r112r_e23_B16?0"PQLConnection"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8r104l8r112l8s88l8s96l8
+ ___block_descriptor_57_e8_32s40s48s_e33_B24?0"CKRecordID"8"CKRecord"16ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s_e23_B16?0"PQLConnection"8ls32l8s40l8
- -[BRCFetchRecordSubResourcesHandler saveChangedRecords:deletedRecordIDs:deletedShareRecordIDs:clientChangeToken:serverChangeToken:caughtUp:pendingChanges:]
- -[BRCFetchRecordSubResourcesOperation addRecord:]
- -[BRCServerZone _populateParticipantsAndSendUserNotificationsIfNeededWithShare:]
- -[BRCServerZone _saveEditedRecord:zonesNeedingAllocRanks:error:]
- -[BRCServerZone _saveEditedShareRecord:error:]
- -[BRCServerZone _saveEditedShareRecords:deletedShareRecordIDs:zonesNeedingAllocRanks:]
- -[BRCServerZone _savePendingChangesSharesIgnoringRecordIDs:zonesNeedingAllocRanks:pendingChangeStream:]
- -[BRCServerZone _sendApprovedNotificationIfNeededWithShare:]
- -[BRCServerZone _shouldSendNotification]
- -[BRCServerZone didSyncDownRequestID:serverChangeToken:editedRecords:deletedRecordIDs:deletedShareRecordIDs:allocRankZones:caughtUp:pendingChanges:]
- -[BRCXPCClient _auditURL:]
- -[BRCXPCClient _auditedURLFromPath:]
- GCC_except_table108
- GCC_except_table132
- GCC_except_table135
- GCC_except_table138
- GCC_except_table165
- GCC_except_table171
- GCC_except_table178
- GCC_except_table201
- GCC_except_table207
- GCC_except_table217
- GCC_except_table222
- GCC_except_table227
- GCC_except_table238
- GCC_except_table239
- GCC_except_table248
- GCC_except_table254
- GCC_except_table278
- GCC_except_table282
- GCC_except_table304
- GCC_except_table307
- GCC_except_table312
- GCC_except_table335
- GCC_except_table338
- GCC_except_table345
- GCC_except_table351
- GCC_except_table363
- GCC_except_table366
- GCC_except_table371
- GCC_except_table374
- GCC_except_table382
- GCC_except_table385
- GCC_except_table395
- GCC_except_table401
- GCC_except_table406
- GCC_except_table415
- GCC_except_table420
- GCC_except_table424
- GCC_except_table429
- GCC_except_table434
- GCC_except_table437
- GCC_except_table441
- GCC_except_table445
- GCC_except_table448
- GCC_except_table453
- GCC_except_table461
- GCC_except_table468
- GCC_except_table474
- GCC_except_table478
- GCC_except_table490
- GCC_except_table500
- GCC_except_table501
- GCC_except_table98
- ___103-[BRCServerZone _savePendingChangesSharesIgnoringRecordIDs:zonesNeedingAllocRanks:pendingChangeStream:]_block_invoke
- ___103-[BRCServerZone _savePendingChangesSharesIgnoringRecordIDs:zonesNeedingAllocRanks:pendingChangeStream:]_block_invoke_2
- ___148-[BRCServerZone didSyncDownRequestID:serverChangeToken:editedRecords:deletedRecordIDs:deletedShareRecordIDs:allocRankZones:caughtUp:pendingChanges:]_block_invoke
- ___155-[BRCFetchRecordSubResourcesHandler saveChangedRecords:deletedRecordIDs:deletedShareRecordIDs:clientChangeToken:serverChangeToken:caughtUp:pendingChanges:]_block_invoke
- ___46-[BRCServerZone _saveEditedShareRecord:error:]_block_invoke
- ___60-[BRCServerZone _sendApprovedNotificationIfNeededWithShare:]_block_invoke
- ___80-[BRCServerZone _populateParticipantsAndSendUserNotificationsIfNeededWithShare:]_block_invoke
- ___block_descriptor_129_e8_32s40s48s56s64s72s80s88s96r104r_e23_B16?0"PQLConnection"8ls32l8s40l8s48l8s56l8s64l8s72l8r96l8r104l8s80l8s88l8
- ___block_descriptor_80_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
CStrings:
+ "-[BRCFetchRecordSubResourcesOperation addRecord:fromDeltaSync:]"
+ "-[BRCServerZone _populateParticipantsAndSendUserNotificationsIfNeededWithShare:fromDeltaSync:]"
+ "-[BRCServerZone _saveEditedRecord:zonesNeedingAllocRanks:fromDeltaSync:error:]"
+ "-[BRCServerZone _saveEditedShareRecord:fromDeltaSync:error:]"
+ "-[BRCServerZone _saveEditedShareRecord:fromDeltaSync:error:]_block_invoke"
+ "-[BRCServerZone _shouldSendRequestForAccessNotificationFromDeltaSync:]"
+ "-[BRCServerZone didSyncDownRequestID:serverChangeToken:editedRecords:deletedRecordIDs:deletedShareRecordIDs:allocRankZones:caughtUp:pendingChanges:shareIDsFromDeltaSync:]"
+ "-[BRCServerZone didSyncDownRequestID:serverChangeToken:editedRecords:deletedRecordIDs:deletedShareRecordIDs:allocRankZones:caughtUp:pendingChanges:shareIDsFromDeltaSync:]_block_invoke"
+ "SELECT COUNT(*) FROM client_items AS ci WHERE ci.item_localsyncupstate != 0   AND ci.item_localsyncupstate IN (2, 3, 4, 7, 8)   AND ci.item_state = 0   AND ci.item_stat_ckinfo IS NULL   AND ci.item_type IN (0, 9, 10)   AND NOT item_id_is_documents(ci.item_id)   AND NOT EXISTS (SELECT 1 FROM client_items AS p                   WHERE p.zone_rowid = ci.zone_rowid                     AND p.item_id = ci.item_parent_id                     AND p.item_localsyncupstate != 0                     AND p.item_localsyncupstate IN (2, 3, 4, 7, 8)                     AND p.item_state = 0                     AND p.item_stat_ckinfo IS NULL)"
+ "[CRIT] UNREACHABLE: %@ is not owning the container whose metadata it is updating%@"
+ "[DEBUG] AppLibrary %@ added to a new zone. Mark special directories as listed + pristine for doc%@"
+ "[ERROR] Found a key that is not of type String%@"
+ "[ERROR] checksum from bookmark is not equal to expected checksum%@"
+ "[WARNING] Can't find appLibrary%@"
+ "crossZoneMoveNeedsSyncUpMoreThan10"
+ "crossZoneMoveNeedsSyncUpMoreThan25"
+ "crossZoneMoveNeedsSyncUpMoreThan50"
+ "nonIdleItemsMoreThan10"
+ "nonIdleItemsMoreThan25"
+ "nonIdleItemsMoreThan50"
+ "tombstoneNeedsSyncUpMoreThan10"
+ "tombstoneNeedsSyncUpMoreThan25"
+ "tombstoneNeedsSyncUpMoreThan50"
+ "uv2MigrationEstimatedReimports"
+ "uv2MigrationEstimatedReimportsMoreThan10"
+ "uv2MigrationEstimatedReimportsMoreThan100"
+ "uv2MigrationEstimatedReimportsMoreThan25"
+ "uv2MigrationEstimatedReimportsMoreThan50"
- "-[BRCFetchRecordSubResourcesOperation addRecord:]"
- "-[BRCServerZone _populateParticipantsAndSendUserNotificationsIfNeededWithShare:]"
- "-[BRCServerZone _saveEditedRecord:zonesNeedingAllocRanks:error:]"
- "-[BRCServerZone _saveEditedShareRecord:error:]"
- "-[BRCServerZone _saveEditedShareRecord:error:]_block_invoke"
- "-[BRCServerZone _shouldSendNotification]"
- "-[BRCServerZone didSyncDownRequestID:serverChangeToken:editedRecords:deletedRecordIDs:deletedShareRecordIDs:allocRankZones:caughtUp:pendingChanges:]"
- "-[BRCServerZone didSyncDownRequestID:serverChangeToken:editedRecords:deletedRecordIDs:deletedShareRecordIDs:allocRankZones:caughtUp:pendingChanges:]_block_invoke"
- "-[BRCXPCClient _auditURL:]"
- "-[BRCXPCRegularIPCsClient _removeSandboxedAttributes:]"
- "[CRIT] UNREACHABLE: %@ is not owning %@ and updating its metadata%@"
- "[DEBUG] AppLibrary %@ added to a new zone. Mark as listed all + pristine for doc%@"
- "[ERROR] Client %@ gave us a non-existing fault URL path %@%@"
- "[ERROR] key: %@ is not of class NSString%@"
- "[WARNING] Can't find appLibrary for id %@%@"
- "[WARNING] Stripping attributes request from %@ to %@%@"
- "crossZoneMoveNeedsSyncUpMoreThan1000"
- "crossZoneMoveNeedsSyncUpMoreThan10000"
- "nonIdleItemsMoreThan1000"
- "nonIdleItemsMoreThan10000"
- "tombstoneNeedsSyncUpMoreThan1000"
- "tombstoneNeedsSyncUpMoreThan10000"
```
