## NotesShared

> `/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared`

```diff

-2952.122.1.500.1
-  __TEXT.__text: 0x363e80
+2952.120.3.0.0
+  __TEXT.__text: 0x364128
   __TEXT.__auth_stubs: 0x5230
   __TEXT.__delay_stubs: 0x240
   __TEXT.__delay_helper: 0x830
-  __TEXT.__objc_methlist: 0x17e9c
+  __TEXT.__objc_methlist: 0x17e8c
   __TEXT.__const: 0xdcf8
-  __TEXT.__cstring: 0x18e41
-  __TEXT.__oslogstring: 0x1be18
-  __TEXT.__gcc_except_tab: 0xf7cc
+  __TEXT.__cstring: 0x18e71
+  __TEXT.__oslogstring: 0x1bf48
+  __TEXT.__gcc_except_tab: 0xf808
   __TEXT.__ustring: 0x38e
   __TEXT.__swift5_typeref: 0x43d4
   __TEXT.__swift5_fieldmd: 0x2d9c

   __TEXT.__swift_as_entry: 0x19c
   __TEXT.__swift_as_ret: 0x1c8
   __TEXT.__swift5_mpenum: 0x74
-  __TEXT.__unwind_info: 0xf568
+  __TEXT.__unwind_info: 0xf578
   __TEXT.__eh_frame: 0x8ce8
   __TEXT.__objc_classname: 0x2ada
-  __TEXT.__objc_methname: 0x37adf
+  __TEXT.__objc_methname: 0x37a6f
   __TEXT.__objc_methtype: 0x516f
-  __TEXT.__objc_stubs: 0x287a0
-  __DATA_CONST.__got: 0x2130
-  __DATA_CONST.__const: 0x6318
+  __TEXT.__objc_stubs: 0x28740
+  __DATA_CONST.__got: 0x2138
+  __DATA_CONST.__const: 0x62f0
   __DATA_CONST.__objc_classlist: 0xa40
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc990
+  __DATA_CONST.__objc_selrefs: 0xc980
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x6b8
   __DATA_CONST.__objc_arraydata: 0x1e8
   __AUTH_CONST.__auth_got: 0x2978
-  __AUTH_CONST.__const: 0xd7d0
-  __AUTH_CONST.__cfstring: 0xf480
+  __AUTH_CONST.__const: 0xd7f0
+  __AUTH_CONST.__cfstring: 0xf400
   __AUTH_CONST.__objc_const: 0x21d10
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x240

   __DATA.__objc_ivar: 0xd58
   __DATA.__data: 0x4aa4
   __DATA.__objc_stublist: 0x20
-  __DATA.__bss: 0x10930
+  __DATA.__bss: 0x10940
   __DATA.__common: 0x180
   __DATA_DIRTY.__objc_data: 0x46a8
   __DATA_DIRTY.__data: 0x1bb8

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A411E88C-5DE3-31B4-8A91-8264E01A32A0
-  Functions: 18402
-  Symbols:   38903
-  CStrings:  16507
+  UUID: 8BE613CA-67BB-3DC8-97F4-3DD8B2E3A4BD
+  Functions: 18407
+  Symbols:   38917
+  CStrings:  16502
 
Symbols:
+ +[ICAttachmentPaperBundleModel generateFallbackPDFDataForAttachment:].cold.1
+ -[ICNoteContext accountStoreDidChange:]
+ -[ICNoteContext accountStoreDidChange:].cold.1
+ -[ICTTMergeableString insertAttributedString:atIndex:].cold.1
+ GCC_except_table574
+ GCC_except_table578
+ GCC_except_table616
+ GCC_except_table646
+ GCC_except_table665
+ GCC_except_table93
+ _ICAccountUtilitiesStoreDidChangeNotification
+ ___113-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke.606
+ ___113-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke_2.607
+ ___120-[ICCloudContext fetchRecordZoneChangesOperation:completedFetchForZoneID:serverChangeToken:error:context:dispatchGroup:]_block_invoke.631
+ ___31-[ICNoteContext updateAccounts]_block_invoke.194
+ ___31-[ICNoteContext updateAccounts]_block_invoke_2.197
+ ___36-[ICNoteContext persistentContainer]_block_invoke.269
+ ___36-[ICNoteContext persistentContainer]_block_invoke_2.271
+ ___38-[ICCloudContext clearPendingActivity]_block_invoke.211
+ ___40-[ICNoteContext setupTrashDeletionTimer]_block_invoke.148
+ ___41-[ICCloudContext cloudKitAccountChanged:]_block_invoke.164.cold.1
+ ___44-[ICCloudContext retryOperationsIfNecessary]_block_invoke.718
+ ___44-[ICCloudContext retryOperationsIfNecessary]_block_invoke.722
+ ___50-[ICNoteContext cleanupAdditionalPersistentStores]_block_invoke.286
+ ___50-[ICNoteContext cleanupAdditionalPersistentStores]_block_invoke.286.cold.1
+ ___50-[ICNoteContext cleanupAdditionalPersistentStores]_block_invoke.286.cold.2
+ ___54-[ICCloudContext startRetryTimerIfNecessaryWithError:]_block_invoke.712
+ ___54-[ICCloudContext startRetryTimerIfNecessaryWithError:]_block_invoke.714
+ ___56-[ICCloudContext cancelEverythingWithCompletionHandler:]_block_invoke.207
+ ___56-[ICCloudContext cancelEverythingWithCompletionHandler:]_block_invoke.209
+ ___56-[ICCloudContext cancelEverythingWithCompletionHandler:]_block_invoke_2.208
+ ___56-[ICCloudContext cancelEverythingWithCompletionHandler:]_block_invoke_2.210
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.682
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.686
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.686.cold.1
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.690
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke_2.684
+ ___59-[ICCloudContext updateAccountStatusWithCompletionHandler:]_block_invoke.241
+ ___59-[ICCloudContext updateAccountStatusWithCompletionHandler:]_block_invoke_2.242
+ ___59-[ICCloudContext updateAccountStatusWithCompletionHandler:]_block_invoke_2.242.cold.1
+ ___59-[ICCloudContext updateAccountStatusWithCompletionHandler:]_block_invoke_2.242.cold.2
+ ___59-[ICCloudContext updateSubscriptionsWithCompletionHandler:]_block_invoke.654
+ ___59-[ICCloudContext updateSubscriptionsWithCompletionHandler:]_block_invoke.656
+ ___65-[ICCloudContext fetchUserRecordWithContainer:completionHandler:]_block_invoke.245
+ ___65-[ICCloudContext fetchUserRecordWithContainer:completionHandler:]_block_invoke.245.cold.1
+ ___65-[ICCloudContext fetchUserRecordWithContainer:completionHandler:]_block_invoke.245.cold.2
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke.666
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke.668
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.669
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.669.cold.1
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.669.cold.2
+ ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke.661
+ ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.662
+ ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.662.cold.1
+ ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.662.cold.2
+ ___67-[ICCloudContext _processCloudObjects:inSession:completionHandler:]_block_invoke.577
+ ___67-[ICCloudContext _processCloudObjects:inSession:completionHandler:]_block_invoke_2.578
+ ___69+[ICAttachmentPaperBundleModel generateFallbackPDFDataForAttachment:]_block_invoke
+ ___69+[ICAttachmentPaperBundleModel generateFallbackPDFDataForAttachment:]_block_invoke_2
+ ___74-[ICCloudContext _syncWithReason:uploadUnsyncedChanges:completionHandler:]_block_invoke.199.cold.1
+ ___74-[ICCloudContext _syncWithReason:uploadUnsyncedChanges:completionHandler:]_block_invoke.200
+ ___74-[ICCloudContext _syncWithReason:uploadUnsyncedChanges:completionHandler:]_block_invoke.201
+ ___74-[ICCloudContext _syncWithReason:uploadUnsyncedChanges:completionHandler:]_block_invoke.201.cold.1
+ ___74-[ICCloudContext _syncWithReason:uploadUnsyncedChanges:completionHandler:]_block_invoke.202
+ ___74-[ICCloudContext enqueueLongLivedOperationsIfNeededWithCompletionHandler:]_block_invoke.691
+ ___74-[ICCloudContext enqueueLongLivedOperationsIfNeededWithCompletionHandler:]_block_invoke_2.693
+ ___78-[ICCloudContext addOperationToProcessObjectsInSession:withCompletionHandler:]_block_invoke.396
+ ___80-[ICCloudContext deleteSharesForObjects:forSession:accountID:completionHandler:]_block_invoke.295
+ ___81-[ICCloudContext finishOperationsForRecordID:qualityOfService:completionHandler:]_block_invoke.233
+ ___81-[ICCloudContext finishOperationsForRecordID:qualityOfService:completionHandler:]_block_invoke.233.cold.1
+ ___84+[ICCloudNotificationsController registerForUserNotificationsWithCompletionHandler:]_block_invoke.31
+ ___84+[ICCloudNotificationsController registerForUserNotificationsWithCompletionHandler:]_block_invoke.35
+ ___84+[ICCloudNotificationsController registerForUserNotificationsWithCompletionHandler:]_block_invoke_2
+ ___88-[ICCloudContext enqueueLongLivedOperationsWithIDsIfNeeded:container:completionHandler:]_block_invoke.700
+ ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke.335
+ ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke.335.cold.1
+ ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke.335.cold.2
+ ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke_2.333
+ ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke_2.333.cold.1
+ ___92-[ICNoteContext createAdditionalPersistentStoresWithAccountIdentifiers:persistentContainer:]_block_invoke.282
+ ___92-[ICNoteContext createAdditionalPersistentStoresWithAccountIdentifiers:persistentContainer:]_block_invoke.282.cold.1
+ ___92-[ICNoteContext createAdditionalPersistentStoresWithAccountIdentifiers:persistentContainer:]_block_invoke.282.cold.2
+ ___97-[ICCloudContext deleteRecordZonesWithZoneIDs:accountID:markZonesAsUserPurged:completionHandler:]_block_invoke.213
+ ___97-[ICCloudContext deleteRecordZonesWithZoneIDs:accountID:markZonesAsUserPurged:completionHandler:]_block_invoke.213.cold.1
+ ___97-[ICCloudContext deleteRecordZonesWithZoneIDs:accountID:markZonesAsUserPurged:completionHandler:]_block_invoke.214
+ ___98-[ICCloudContext fetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke.602
+ ___99+[ICCloudContext batchRecordsToSave:delete:maxRecordCountPerBatch:maxRecordSizePerBatch:withBlock:]_block_invoke.324
+ ___Block_byref_object_copy_.23
+ ___Block_byref_object_copy_.45
+ ___Block_byref_object_dispose_.24
+ ___Block_byref_object_dispose_.46
+ ___block_descriptor_48_e8_32bs40r_e20_v20?0B8"NSError"12lr40l8s32l8
+ ___block_descriptor_56_e8_32s40s_e20_v24?0q8"NSError"16ls32l8s40l8
+ ___block_literal_global.143
+ ___block_literal_global.164
+ ___block_literal_global.177
+ ___block_literal_global.196
+ ___block_literal_global.200
+ ___block_literal_global.216
+ ___block_literal_global.252
+ ___block_literal_global.280
+ ___block_literal_global.289
+ ___block_literal_global.301
+ ___block_literal_global.321
+ ___block_literal_global.326
+ ___block_literal_global.370
+ ___block_literal_global.378
+ ___block_literal_global.55
+ ___block_literal_global.647
+ ___block_literal_global.695
+ _generateFallbackPDFDataForAttachment:.onceToken
+ _generateFallbackPDFDataForAttachment:.sPDFGenerationQueue
- -[ICAttachmentTableModel csvData]
- -[ICAttachmentTableModel csvString]
- GCC_except_table103
- GCC_except_table573
- GCC_except_table576
- GCC_except_table613
- GCC_except_table645
- GCC_except_table664
- ___113-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke.603
- ___113-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke_2.604
- ___120-[ICCloudContext fetchRecordZoneChangesOperation:completedFetchForZoneID:serverChangeToken:error:context:dispatchGroup:]_block_invoke.628
- ___31-[ICNoteContext updateAccounts]_block_invoke.192
- ___31-[ICNoteContext updateAccounts]_block_invoke_2.195
- ___35-[ICAttachmentTableModel csvString]_block_invoke
- ___35-[ICAttachmentTableModel csvString]_block_invoke_2
- ___36-[ICNoteContext persistentContainer]_block_invoke.267
- ___36-[ICNoteContext persistentContainer]_block_invoke_2.269
- ___38-[ICCloudContext clearPendingActivity]_block_invoke.208
- ___40-[ICNoteContext setupTrashDeletionTimer]_block_invoke.146
- ___44-[ICCloudContext retryOperationsIfNecessary]_block_invoke.715
- ___44-[ICCloudContext retryOperationsIfNecessary]_block_invoke.719
- ___50-[ICNoteContext cleanupAdditionalPersistentStores]_block_invoke.284
- ___50-[ICNoteContext cleanupAdditionalPersistentStores]_block_invoke.284.cold.1
- ___50-[ICNoteContext cleanupAdditionalPersistentStores]_block_invoke.284.cold.2
- ___54-[ICCloudContext startRetryTimerIfNecessaryWithError:]_block_invoke.709
- ___54-[ICCloudContext startRetryTimerIfNecessaryWithError:]_block_invoke.711
- ___56-[ICCloudContext cancelEverythingWithCompletionHandler:]_block_invoke.204
- ___56-[ICCloudContext cancelEverythingWithCompletionHandler:]_block_invoke.206
- ___56-[ICCloudContext cancelEverythingWithCompletionHandler:]_block_invoke_2.205
- ___56-[ICCloudContext cancelEverythingWithCompletionHandler:]_block_invoke_2.207
- ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.679
- ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.680
- ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.683.cold.1
- ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.687
- ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke_2.681
- ___59-[ICCloudContext updateAccountStatusWithCompletionHandler:]_block_invoke.238
- ___59-[ICCloudContext updateAccountStatusWithCompletionHandler:]_block_invoke_2.239
- ___59-[ICCloudContext updateAccountStatusWithCompletionHandler:]_block_invoke_2.239.cold.1
- ___59-[ICCloudContext updateAccountStatusWithCompletionHandler:]_block_invoke_2.239.cold.2
- ___59-[ICCloudContext updateSubscriptionsWithCompletionHandler:]_block_invoke.651
- ___59-[ICCloudContext updateSubscriptionsWithCompletionHandler:]_block_invoke.653
- ___65-[ICCloudContext fetchUserRecordWithContainer:completionHandler:]_block_invoke.242
- ___65-[ICCloudContext fetchUserRecordWithContainer:completionHandler:]_block_invoke.242.cold.1
- ___65-[ICCloudContext fetchUserRecordWithContainer:completionHandler:]_block_invoke.242.cold.2
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke.663
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke.665
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.666
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.666.cold.1
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.666.cold.2
- ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke.658
- ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.659
- ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.659.cold.1
- ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.659.cold.2
- ___67-[ICCloudContext _processCloudObjects:inSession:completionHandler:]_block_invoke.574
- ___67-[ICCloudContext _processCloudObjects:inSession:completionHandler:]_block_invoke_2.575
- ___74-[ICCloudContext _syncWithReason:uploadUnsyncedChanges:completionHandler:]_block_invoke.195
- ___74-[ICCloudContext _syncWithReason:uploadUnsyncedChanges:completionHandler:]_block_invoke.195.cold.1
- ___74-[ICCloudContext _syncWithReason:uploadUnsyncedChanges:completionHandler:]_block_invoke.196
- ___74-[ICCloudContext _syncWithReason:uploadUnsyncedChanges:completionHandler:]_block_invoke.196.cold.1
- ___74-[ICCloudContext _syncWithReason:uploadUnsyncedChanges:completionHandler:]_block_invoke.197
- ___74-[ICCloudContext enqueueLongLivedOperationsIfNeededWithCompletionHandler:]_block_invoke.688
- ___74-[ICCloudContext enqueueLongLivedOperationsIfNeededWithCompletionHandler:]_block_invoke_2.690
- ___78-[ICCloudContext addOperationToProcessObjectsInSession:withCompletionHandler:]_block_invoke.393
- ___80-[ICCloudContext deleteSharesForObjects:forSession:accountID:completionHandler:]_block_invoke.292
- ___81-[ICCloudContext finishOperationsForRecordID:qualityOfService:completionHandler:]_block_invoke.230
- ___81-[ICCloudContext finishOperationsForRecordID:qualityOfService:completionHandler:]_block_invoke.230.cold.1
- ___84+[ICCloudNotificationsController registerForUserNotificationsWithCompletionHandler:]_block_invoke.34
- ___88-[ICCloudContext enqueueLongLivedOperationsWithIDsIfNeeded:container:completionHandler:]_block_invoke.697
- ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke.329
- ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke.332.cold.1
- ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke.332.cold.2
- ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke_2.330
- ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke_2.330.cold.1
- ___92-[ICNoteContext createAdditionalPersistentStoresWithAccountIdentifiers:persistentContainer:]_block_invoke.280
- ___92-[ICNoteContext createAdditionalPersistentStoresWithAccountIdentifiers:persistentContainer:]_block_invoke.280.cold.1
- ___92-[ICNoteContext createAdditionalPersistentStoresWithAccountIdentifiers:persistentContainer:]_block_invoke.280.cold.2
- ___97-[ICCloudContext deleteRecordZonesWithZoneIDs:accountID:markZonesAsUserPurged:completionHandler:]_block_invoke.210
- ___97-[ICCloudContext deleteRecordZonesWithZoneIDs:accountID:markZonesAsUserPurged:completionHandler:]_block_invoke.210.cold.1
- ___97-[ICCloudContext deleteRecordZonesWithZoneIDs:accountID:markZonesAsUserPurged:completionHandler:]_block_invoke.211
- ___98-[ICCloudContext fetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke.599
- ___99+[ICCloudContext batchRecordsToSave:delete:maxRecordCountPerBatch:maxRecordSizePerBatch:withBlock:]_block_invoke.321
- ___Block_byref_object_copy_.21
- ___Block_byref_object_copy_.43
- ___Block_byref_object_dispose_.22
- ___Block_byref_object_dispose_.44
- ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12ls32l8
- ___block_descriptor_48_e8_32s40s_e23_v32?0"NSUUID"8Q16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s_e20_v24?0q8"NSError"16ls32l8
- ___block_literal_global.141
- ___block_literal_global.162
- ___block_literal_global.194
- ___block_literal_global.198
- ___block_literal_global.213
- ___block_literal_global.278
- ___block_literal_global.287
- ___block_literal_global.298
- ___block_literal_global.318
- ___block_literal_global.320
- ___block_literal_global.367
- ___block_literal_global.375
- ___block_literal_global.382
- ___block_literal_global.644
- ___block_literal_global.692
- _objc_msgSend$csvString
- _objc_msgSend$insertString:atIndex:
- _objc_msgSend$replaceOccurrencesOfString:withString:options:range:
CStrings:
+ "Account store did change, cleaning up stale persistent stores"
+ "AccountInfoChanged"
+ "CloudKit account info may have changed (status unchanged). Syncing to pick up potential server-side changes."
+ "Invalid location %lu when inserting attributed string into mergeable string with length %lu"
+ "Timed out waiting for user notification authorization"
+ "accountStoreDidChange:"
+ "com.apple.notes.fallback-pdf-generation"
- " ,\"\\\n"
- "\\"
- "\\\""
- "\\\\"
- "csvData"
- "csvString"
- "replaceOccurrencesOfString:withString:options:range:"

```
