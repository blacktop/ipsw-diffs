## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-4479.120.19.0.0
-  __TEXT.__text: 0x324de8
+4479.122.1.0.0
+  __TEXT.__text: 0x325498
   __TEXT.__auth_stubs: 0x1a80
-  __TEXT.__objc_methlist: 0x1abbc
+  __TEXT.__objc_methlist: 0x1ac04
   __TEXT.__const: 0x510
-  __TEXT.__cstring: 0x7ee61
-  __TEXT.__oslogstring: 0x3b991
+  __TEXT.__cstring: 0x7f106
+  __TEXT.__oslogstring: 0x3ba12
   __TEXT.__gcc_except_tab: 0x1a150
   __TEXT.__ustring: 0x36
-  __TEXT.__unwind_info: 0xa870
+  __TEXT.__unwind_info: 0xa880
   __TEXT.__objc_classname: 0x2b45
-  __TEXT.__objc_methname: 0x45e1e
+  __TEXT.__objc_methname: 0x45f2d
   __TEXT.__objc_methtype: 0x9570
-  __TEXT.__objc_stubs: 0x2fe00
+  __TEXT.__objc_stubs: 0x2fec0
   __DATA_CONST.__got: 0x1730
   __DATA_CONST.__const: 0x96e8
   __DATA_CONST.__objc_classlist: 0xa68
   __DATA_CONST.__objc_catlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xeb78
+  __DATA_CONST.__objc_selrefs: 0xebb0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x918
   __DATA_CONST.__objc_arraydata: 0xea0
   __AUTH_CONST.__auth_got: 0xd50
-  __AUTH_CONST.__const: 0x2bb0
-  __AUTH_CONST.__cfstring: 0x22d20
-  __AUTH_CONST.__objc_const: 0x3e1c8
+  __AUTH_CONST.__const: 0x2bc0
+  __AUTH_CONST.__cfstring: 0x22ea0
+  __AUTH_CONST.__objc_const: 0x3e1e8
   __AUTH_CONST.__objc_intobj: 0xbe8
   __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0xf0

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 83EC03EA-0C48-3EE2-A52C-BA526517E793
-  Functions: 13813
-  Symbols:   45500
-  CStrings:  27972
+  UUID: 7E908C82-2A16-3A45-AD87-C84A25E4E94D
+  Functions: 13820
+  Symbols:   45520
+  CStrings:  28006
 
Symbols:
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newDirectoryRevivalEventWithInodesMatch:]
+ -[BRCDirectoryItem(FPFSAdditions) _reportRevivalTelemetryForDeadItem:createdFileID:]
+ -[BRCDirectoryItem(FPFSAdditions) _reportRevivalTelemetryForDeadItem:createdFileID:].cold.1
+ -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:createdFileID:]
+ -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:createdFileID:].cold.1
+ -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:createdFileID:].cold.2
+ -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:createdFileID:].cold.3
+ -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:createdFileID:].cold.4
+ -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:createdFileID:].cold.5
+ -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:createdFileID:].cold.6
+ -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:createdFileID:].cold.7
+ -[BRCUserDefaults checkRevivalInodeMatch]
+ -[BRCUserDefaults lookupServerPathMatchWhenRevivingDeadDirsOnNewDirCreations]
+ -[BRCUserDefaults resetOnRevivalInodeMatch]
+ GCC_except_table280
+ GCC_except_table301
+ GCC_except_table578
+ ___104-[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:createdFileID:]_block_invoke
+ ___104-[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:createdFileID:]_block_invoke.cold.1
+ ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke.185
+ ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke.185.cold.1
+ ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) capabilityWhenTryingToReparentItemIdentifier:toNewParent:reply:]_block_invoke.150
+ ___107-[BRCXPCRegularIPCsClient(FPFSAdditions) getPublishedURLForItemIdentifier:forStreaming:requestedTTL:reply:]_block_invoke.156
+ ___107-[BRCXPCRegularIPCsClient(FPFSAdditions) getPublishedURLForItemIdentifier:forStreaming:requestedTTL:reply:]_block_invoke.156.cold.1
+ ___108-[BRCXPCRegularIPCsClient(FPFSAdditions) _fetchLatestContentRevisionAndSharingStateForItemIdentifier:reply:]_block_invoke.164
+ ___110-[BRCXPCRegularIPCsClient(FPFSAdditions) setiWorkPublishingInfoForItemIdentifier:isForPublish:readonly:reply:]_block_invoke.159
+ ___123-[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionAndSharingStateForItemIdentifier:retryOnApplyFailure:reply:]_block_invoke.162
+ ___125-[BRCXPCRegularIPCsClient(FPFSAdditions) uploadItemIdentifier:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.216
+ ___138-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke.132
+ ___138-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke.134
+ ___138-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke.136
+ ___138-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke_2.133
+ ___138-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke_2.135
+ ___66-[BRCXPCRegularIPCsClient(FPFSAdditions) notifyReimportCompleted:]_block_invoke.145
+ ___71-[BRCXPCRegularIPCsClient(FPFSAdditions) reimportItemIdentifier:reply:]_block_invoke.137
+ ___71-[BRCXPCRegularIPCsClient(FPFSAdditions) reimportItemIdentifier:reply:]_block_invoke.141
+ ___72-[BRCXPCRegularIPCsClient(FPFSAdditions) waitForStabilizationWithReply:]_block_invoke.214
+ ___73-[BRCXPCRegularIPCsClient(FPFSAdditions) getCKRecordIDsForFPItems:reply:]_block_invoke.218
+ ___75-[BRCXPCRegularIPCsClient(FPFSAdditions) getFPItemIDsForCKRecordIDs:reply:]_block_invoke.220
+ ___77-[BRCXPCRegularIPCsClient(FPFSAdditions) copyShareIDForItemIdentifier:reply:]_block_invoke.178
+ ___80-[BRCXPCRegularIPCsClient(FPFSAdditions) getStructureRecordIDsForFPItems:reply:]_block_invoke.219
+ ___84-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:reply:]_block_invoke.166
+ ___84-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:reply:]_block_invoke.167
+ ___84-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:reply:]_block_invoke.167.cold.1
+ ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerSaltingKeysAtItemIdentifier:reply:]_block_invoke.201
+ ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerSaltingKeysAtItemIdentifier:reply:]_block_invoke.207
+ ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke.174
+ ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) copyStructureRecordIDForItemIdentifier:reply:]_block_invoke.180
+ ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) enumerateTrashItemsFromRank:limit:completion:]_block_invoke.142
+ ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) enumerateTrashItemsFromRank:limit:completion:]_block_invoke.144
+ ___88-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkPublishingInfoForItemIdentifier:reply:]_block_invoke.158
+ ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) checkIfItemIsShareableWithItemIdentifier:reply:]_block_invoke.181
+ ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) startOperation:toWaitForFPFSMigrationWithReply:]_block_invoke.188
+ ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getCreatorNameComponentsForItemIdentifier:reply:]_block_invoke.182
+ ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerContentSignatureAtItemIdentifier:reply:]_block_invoke.208
+ ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerContentSignatureAtItemIdentifier:reply:]_block_invoke.209
+ ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:forURL:reply:]_block_invoke.172
+ ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:forURL:reply:]_block_invoke.172.cold.1
+ ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkNeedsShareMigrateForItemIdentifier:reply:]_block_invoke.161
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) cloneLatestContentRevisionForItemIdentifier:reply:]_block_invoke.173
+ ___95-[BRCXPCRegularIPCsClient(FPFSAdditions) launchItemCountMismatchChecksForItemIdentifier:reply:]_block_invoke.176
+ ___97-[BRCXPCRegularIPCsClient(FPFSAdditions) getClientSaltingVerificationKeysAtItemIdentifier:reply:]_block_invoke.193
+ ___97-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkPublishingBadgingStatusForItemIdentifier:reply:]_block_invoke.160
+ ___block_descriptor_81_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.139
+ ___block_literal_global.187
+ ___block_literal_global.2268
+ ___block_literal_global.2294
+ ___block_literal_global.2316
+ ___block_literal_global.2325
+ ___block_literal_global.2334
+ ___block_literal_global.2862
+ _br_update_tables_34_103
+ _objc_msgSend$_reportRevivalTelemetryForDeadItem:createdFileID:
+ _objc_msgSend$brc_errorZoneResetRevivalInodeMatch
+ _objc_msgSend$checkRevivalInodeMatch
+ _objc_msgSend$deletedDirectoryFileID
+ _objc_msgSend$handlePathMatchConflictForDirectoryCreationIfNecessary:createdFileID:
+ _objc_msgSend$newDirectoryRevivalEventWithInodesMatch:
+ _objc_msgSend$resetOnRevivalInodeMatch
- -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:]
- -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:].cold.1
- -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:].cold.2
- -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:].cold.3
- -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:].cold.4
- -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:].cold.5
- -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:].cold.6
- -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:].cold.7
- GCC_except_table300
- GCC_except_table575
- ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke.182
- ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke.182.cold.1
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) capabilityWhenTryingToReparentItemIdentifier:toNewParent:reply:]_block_invoke.147
- ___107-[BRCXPCRegularIPCsClient(FPFSAdditions) getPublishedURLForItemIdentifier:forStreaming:requestedTTL:reply:]_block_invoke.153
- ___107-[BRCXPCRegularIPCsClient(FPFSAdditions) getPublishedURLForItemIdentifier:forStreaming:requestedTTL:reply:]_block_invoke.153.cold.1
- ___108-[BRCXPCRegularIPCsClient(FPFSAdditions) _fetchLatestContentRevisionAndSharingStateForItemIdentifier:reply:]_block_invoke.161
- ___110-[BRCXPCRegularIPCsClient(FPFSAdditions) setiWorkPublishingInfoForItemIdentifier:isForPublish:readonly:reply:]_block_invoke.156
- ___123-[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionAndSharingStateForItemIdentifier:retryOnApplyFailure:reply:]_block_invoke.159
- ___125-[BRCXPCRegularIPCsClient(FPFSAdditions) uploadItemIdentifier:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.213
- ___138-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke.128
- ___138-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke.129
- ___138-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke.133
- ___138-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke_2.130
- ___138-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke_2.132
- ___66-[BRCXPCRegularIPCsClient(FPFSAdditions) notifyReimportCompleted:]_block_invoke.142
- ___71-[BRCXPCRegularIPCsClient(FPFSAdditions) reimportItemIdentifier:reply:]_block_invoke.134
- ___71-[BRCXPCRegularIPCsClient(FPFSAdditions) reimportItemIdentifier:reply:]_block_invoke.138
- ___72-[BRCXPCRegularIPCsClient(FPFSAdditions) waitForStabilizationWithReply:]_block_invoke.211
- ___73-[BRCXPCRegularIPCsClient(FPFSAdditions) getCKRecordIDsForFPItems:reply:]_block_invoke.215
- ___75-[BRCXPCRegularIPCsClient(FPFSAdditions) getFPItemIDsForCKRecordIDs:reply:]_block_invoke.217
- ___77-[BRCXPCRegularIPCsClient(FPFSAdditions) copyShareIDForItemIdentifier:reply:]_block_invoke.175
- ___80-[BRCXPCRegularIPCsClient(FPFSAdditions) getStructureRecordIDsForFPItems:reply:]_block_invoke.216
- ___84-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:reply:]_block_invoke.163
- ___84-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:reply:]_block_invoke.164
- ___84-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:reply:]_block_invoke.164.cold.1
- ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerSaltingKeysAtItemIdentifier:reply:]_block_invoke.198
- ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerSaltingKeysAtItemIdentifier:reply:]_block_invoke.204
- ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke.171
- ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) copyStructureRecordIDForItemIdentifier:reply:]_block_invoke.177
- ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) enumerateTrashItemsFromRank:limit:completion:]_block_invoke.139
- ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) enumerateTrashItemsFromRank:limit:completion:]_block_invoke.141
- ___88-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkPublishingInfoForItemIdentifier:reply:]_block_invoke.155
- ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) checkIfItemIsShareableWithItemIdentifier:reply:]_block_invoke.178
- ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) startOperation:toWaitForFPFSMigrationWithReply:]_block_invoke.185
- ___90-[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:]_block_invoke
- ___90-[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:]_block_invoke.cold.1
- ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getCreatorNameComponentsForItemIdentifier:reply:]_block_invoke.179
- ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerContentSignatureAtItemIdentifier:reply:]_block_invoke.205
- ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerContentSignatureAtItemIdentifier:reply:]_block_invoke.206
- ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:forURL:reply:]_block_invoke.169
- ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:forURL:reply:]_block_invoke.169.cold.1
- ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkNeedsShareMigrateForItemIdentifier:reply:]_block_invoke.158
- ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) cloneLatestContentRevisionForItemIdentifier:reply:]_block_invoke.170
- ___95-[BRCXPCRegularIPCsClient(FPFSAdditions) launchItemCountMismatchChecksForItemIdentifier:reply:]_block_invoke.173
- ___97-[BRCXPCRegularIPCsClient(FPFSAdditions) getClientSaltingVerificationKeysAtItemIdentifier:reply:]_block_invoke.190
- ___97-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkPublishingBadgingStatusForItemIdentifier:reply:]_block_invoke.157
- ___block_descriptor_73_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.136
- ___block_literal_global.184
- ___block_literal_global.2265
- ___block_literal_global.2291
- ___block_literal_global.2310
- ___block_literal_global.2322
- ___block_literal_global.2331
- ___block_literal_global.2853
- _objc_msgSend$handlePathMatchConflictForDirectoryCreationIfNecessary:
CStrings:
+ "-[BRCDirectoryItem(FPFSAdditions) _reportRevivalTelemetryForDeadItem:createdFileID:]"
+ "-[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:createdFileID:]"
+ "-[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:createdFileID:]_block_invoke"
+ "A directory was deleted and re-created at the same path with the same inode."
+ "ALTER TABLE client_items ADD COLUMN item_deleted_file_id INTEGER"
+ "DIRECTORY_REVIVAL"
+ "Directory revival with matching inodes"
+ "RevivalInodeMatch"
+ "SELECT item_deleted_file_id FROM client_items WHERE rowid = %llu"
+ "SHARED_TO_ME_ITEMS_STUCK_SIDE_CAR_SYNC_JOBS_COUNT"
+ "UPDATE client_items SET item_deleted_file_id = %@ WHERE rowid = %llu"
+ "[DEBUG] Directory revival with matching inodes for dead item %@%@"
+ "[ERROR] Failed to persist deleted file ID for rowid %llu: %@%@"
+ "_reportRevivalTelemetryForDeadItem:createdFileID:"
+ "brc_errorZoneResetRevivalInodeMatch"
+ "checkRevivalInodeMatch"
+ "deletedDirectoryFileID"
+ "directory was revived with the same inode"
+ "handlePathMatchConflictForDirectoryCreationIfNecessary:createdFileID:"
+ "lookupServerPathMatchWhenRevivingDeadDirsOnNewDirCreations"
+ "newDirectoryRevivalEventWithInodesMatch:"
+ "resetOnRevivalInodeMatch"
+ "revive.check-inode-match"
+ "revive.reset-on-inode-match"
+ "sync.lookup-server-path-match-revive-dead-dirs-on-new-dir-creations"
- "-[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:]"
- "-[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:]_block_invoke"
- "handlePathMatchConflictForDirectoryCreationIfNecessary:"

```
