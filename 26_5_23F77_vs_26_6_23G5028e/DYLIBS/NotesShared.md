## NotesShared

> `/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared`

```diff

-2952.120.8.0.0
-  __TEXT.__text: 0x364a70
+2952.140.1.0.0
+  __TEXT.__text: 0x3646bc
   __TEXT.__auth_stubs: 0x5230
   __TEXT.__delay_stubs: 0x240
   __TEXT.__delay_helper: 0x830
-  __TEXT.__objc_methlist: 0x17f0c
+  __TEXT.__objc_methlist: 0x17f2c
   __TEXT.__const: 0xdcf8
-  __TEXT.__cstring: 0x18e71
-  __TEXT.__oslogstring: 0x1bff8
+  __TEXT.__cstring: 0x18e21
+  __TEXT.__oslogstring: 0x1bfb8
   __TEXT.__gcc_except_tab: 0xf808
   __TEXT.__ustring: 0x392
   __TEXT.__swift5_typeref: 0x43d4

   __TEXT.__swift_as_entry: 0x19c
   __TEXT.__swift_as_ret: 0x1c8
   __TEXT.__swift5_mpenum: 0x74
-  __TEXT.__unwind_info: 0xf5a8
+  __TEXT.__unwind_info: 0xf598
   __TEXT.__eh_frame: 0x8ce8
   __TEXT.__objc_classname: 0x2ada
-  __TEXT.__objc_methname: 0x37b6f
-  __TEXT.__objc_methtype: 0x518f
-  __TEXT.__objc_stubs: 0x28800
+  __TEXT.__objc_methname: 0x37b8f
+  __TEXT.__objc_methtype: 0x51cf
+  __TEXT.__objc_stubs: 0x287c0
   __DATA_CONST.__got: 0x2138
-  __DATA_CONST.__const: 0x62f0
+  __DATA_CONST.__const: 0x62c8
   __DATA_CONST.__objc_classlist: 0xa40
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc9c0
+  __DATA_CONST.__objc_selrefs: 0xc9c8
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x6b8
   __DATA_CONST.__objc_arraydata: 0x1e8
   __AUTH_CONST.__auth_got: 0x2978
   __AUTH_CONST.__const: 0xd8e0
   __AUTH_CONST.__cfstring: 0xf440
-  __AUTH_CONST.__objc_const: 0x21d80
+  __AUTH_CONST.__objc_const: 0x21de8
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x2f40
   __AUTH.__data: 0x14b0
-  __DATA.__objc_ivar: 0xd58
-  __DATA.__data: 0x4ab4
+  __DATA.__objc_ivar: 0xd5c
+  __DATA.__data: 0x4aa4
   __DATA.__objc_stublist: 0x20
   __DATA.__bss: 0x10940
   __DATA.__common: 0x180

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 218F3D60-7F9A-3A44-96D5-CC62B1D47BD5
-  Functions: 18431
-  Symbols:   38938
-  CStrings:  16518
+  UUID: F5C64D20-B7C4-3B1A-B12D-15969E164280
+  Functions: 18433
+  Symbols:   38939
+  CStrings:  16522
 
Symbols:
+ +[ICInvitation hasInvitationMatchingPredicate:context:]
+ +[ICNote(Management) hasNoteMatchingPredicate:context:]
+ -[ICAccount hasVisibleNotes]
+ -[ICCloudContext backgroundContextLock]
+ -[ICCloudContext lastKnownWalrusStatus]
+ -[ICCloudContext setBackgroundContextLock:]
+ -[ICCloudContext setLastKnownWalrusStatus:]
+ -[ICFolder hasVisibleNotes]
+ -[ICFolder(Management) hasVisibleNotesInFolder]
+ -[ICNoteContainer hasVisibleNotes]
+ GCC_except_table164
+ GCC_except_table188
+ GCC_except_table193
+ GCC_except_table300
+ GCC_except_table323
+ GCC_except_table346
+ GCC_except_table581
+ GCC_except_table582
+ GCC_except_table618
+ GCC_except_table619
+ GCC_except_table620
+ GCC_except_table650
+ GCC_except_table669
+ _OBJC_IVAR_$_ICCloudContext._backgroundContextLock
+ _OBJC_IVAR_$_ICCloudContext._lastKnownWalrusStatus
+ _OUTLINED_FUNCTION_39
+ ___113-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke.607
+ ___113-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke_2.608
+ ___120-[ICCloudContext fetchRecordZoneChangesOperation:completedFetchForZoneID:serverChangeToken:error:context:dispatchGroup:]_block_invoke.632
+ ___44-[ICCloudContext retryOperationsIfNecessary]_block_invoke.719
+ ___44-[ICCloudContext retryOperationsIfNecessary]_block_invoke.723
+ ___50+[ICAccount(Management) cloudKitAccountInContext:]_block_invoke.634
+ ___50+[ICAccount(Management) cloudKitAccountInContext:]_block_invoke.635
+ ___50+[ICAccount(Management) cloudKitAccountInContext:]_block_invoke.635.cold.1
+ ___54-[ICCloudContext startRetryTimerIfNecessaryWithError:]_block_invoke.713
+ ___54-[ICCloudContext startRetryTimerIfNecessaryWithError:]_block_invoke.715
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.684
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.687
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.687.cold.1
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.691
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke_2.685
+ ___59-[ICCloudContext updateSubscriptionsWithCompletionHandler:]_block_invoke.655
+ ___59-[ICCloudContext updateSubscriptionsWithCompletionHandler:]_block_invoke.657
+ ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1186.cold.1
+ ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1186.cold.2
+ ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1188
+ ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1188.cold.1
+ ___65-[ICCloudContext fetchUserRecordWithContainer:completionHandler:]_block_invoke.246
+ ___65-[ICCloudContext fetchUserRecordWithContainer:completionHandler:]_block_invoke.246.cold.1
+ ___65-[ICCloudContext fetchUserRecordWithContainer:completionHandler:]_block_invoke.246.cold.2
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke.667
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke.669
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.670
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.670.cold.1
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.670.cold.2
+ ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke.662
+ ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.663
+ ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.663.cold.1
+ ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.663.cold.2
+ ___67-[ICCloudContext _processCloudObjects:inSession:completionHandler:]_block_invoke.578
+ ___67-[ICCloudContext _processCloudObjects:inSession:completionHandler:]_block_invoke_2.579
+ ___74-[ICCloudContext enqueueLongLivedOperationsIfNeededWithCompletionHandler:]_block_invoke.692
+ ___74-[ICCloudContext enqueueLongLivedOperationsIfNeededWithCompletionHandler:]_block_invoke_2.694
+ ___78-[ICCloudContext addOperationToProcessObjectsInSession:withCompletionHandler:]_block_invoke.397
+ ___80-[ICCloudContext deleteSharesForObjects:forSession:accountID:completionHandler:]_block_invoke.296
+ ___88-[ICCloudContext enqueueLongLivedOperationsWithIDsIfNeeded:container:completionHandler:]_block_invoke.701
+ ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke.333
+ ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke.336
+ ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke.336.cold.1
+ ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke.336.cold.2
+ ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke_2.334
+ ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke_2.334.cold.1
+ ___98-[ICCloudContext fetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke.603
+ ___99+[ICCloudContext batchRecordsToSave:delete:maxRecordCountPerBatch:maxRecordSizePerBatch:withBlock:]_block_invoke.325
+ ___block_descriptor_56_e8_32s40s48bs_e35_v24?0"CKAccountInfo"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s_e20_v24?0q8"NSError"16ls32l8s40l8
+ ___block_literal_global.1154
+ ___block_literal_global.1167
+ ___block_literal_global.1183
+ ___block_literal_global.146
+ ___block_literal_global.302
+ ___block_literal_global.322
+ ___block_literal_global.324
+ ___block_literal_global.327
+ ___block_literal_global.371
+ ___block_literal_global.379
+ ___block_literal_global.386
+ ___block_literal_global.619
+ ___block_literal_global.648
+ ___block_literal_global.696
+ _objc_msgSend$accountInfoWithCompletionHandler:
+ _objc_msgSend$hasNoteMatchingPredicate:context:
+ _objc_msgSend$hasVisibleNotes
+ _objc_msgSend$hasVisibleNotesInFolder
+ _objc_msgSend$ic_hasObjectMatchingPredicate:context:
+ _objc_msgSend$lastKnownWalrusStatus
+ _objc_msgSend$setLastKnownWalrusStatus:
+ _objc_msgSend$walrusStatus
- -[ICAccount addTrashObserversIfNecessary]
- -[ICAccount didAddTrashObservers]
- -[ICAccount managedObjectContextDidSave:]
- -[ICAccount observeValueForKeyPath:ofObject:change:context:]
- -[ICAccount removeAllObserversIfNecessary]
- -[ICAccount removeTrashObserversIfNecessary]
- -[ICAccount setDidAddTrashObservers:]
- -[ICAccount updateTrashFolderHiddenNoteContainerState]
- GCC_except_table198
- GCC_except_table345
- GCC_except_table398
- GCC_except_table574
- GCC_except_table577
- GCC_except_table614
- GCC_except_table615
- GCC_except_table616
- GCC_except_table646
- GCC_except_table665
- _OBJC_IVAR_$_ICAccount._didAddTrashObservers
- ___113-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke.606
- ___113-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke_2.607
- ___120-[ICCloudContext fetchRecordZoneChangesOperation:completedFetchForZoneID:serverChangeToken:error:context:dispatchGroup:]_block_invoke.631
- ___44-[ICCloudContext retryOperationsIfNecessary]_block_invoke.718
- ___44-[ICCloudContext retryOperationsIfNecessary]_block_invoke.722
- ___50+[ICAccount(Management) cloudKitAccountInContext:]_block_invoke.651
- ___50+[ICAccount(Management) cloudKitAccountInContext:]_block_invoke.652
- ___50+[ICAccount(Management) cloudKitAccountInContext:]_block_invoke.652.cold.1
- ___54-[ICAccount updateTrashFolderHiddenNoteContainerState]_block_invoke
- ___54-[ICCloudContext startRetryTimerIfNecessaryWithError:]_block_invoke.712
- ___54-[ICCloudContext startRetryTimerIfNecessaryWithError:]_block_invoke.714
- ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.682
- ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.686
- ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.686.cold.1
- ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.690
- ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke_2.684
- ___59-[ICCloudContext updateSubscriptionsWithCompletionHandler:]_block_invoke.654
- ___59-[ICCloudContext updateSubscriptionsWithCompletionHandler:]_block_invoke.656
- ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1185
- ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1185.cold.1
- ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1185.cold.2
- ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1187.cold.1
- ___65-[ICCloudContext fetchUserRecordWithContainer:completionHandler:]_block_invoke.245
- ___65-[ICCloudContext fetchUserRecordWithContainer:completionHandler:]_block_invoke.245.cold.1
- ___65-[ICCloudContext fetchUserRecordWithContainer:completionHandler:]_block_invoke.245.cold.2
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke.666
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke.668
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.669
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.669.cold.1
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.669.cold.2
- ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke.661
- ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.662
- ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.662.cold.1
- ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.662.cold.2
- ___67-[ICCloudContext _processCloudObjects:inSession:completionHandler:]_block_invoke.577
- ___67-[ICCloudContext _processCloudObjects:inSession:completionHandler:]_block_invoke_2.578
- ___74-[ICCloudContext enqueueLongLivedOperationsIfNeededWithCompletionHandler:]_block_invoke.691
- ___74-[ICCloudContext enqueueLongLivedOperationsIfNeededWithCompletionHandler:]_block_invoke_2.693
- ___78-[ICCloudContext addOperationToProcessObjectsInSession:withCompletionHandler:]_block_invoke.396
- ___80-[ICCloudContext deleteSharesForObjects:forSession:accountID:completionHandler:]_block_invoke.295
- ___88-[ICCloudContext enqueueLongLivedOperationsWithIDsIfNeeded:container:completionHandler:]_block_invoke.700
- ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke.332
- ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke.335
- ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke.335.cold.1
- ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke.335.cold.2
- ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke_2.333
- ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke_2.333.cold.1
- ___98-[ICCloudContext fetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke.602
- ___99+[ICCloudContext batchRecordsToSave:delete:maxRecordCountPerBatch:maxRecordSizePerBatch:withBlock:]_block_invoke.324
- ___block_descriptor_56_e8_32s40s48bs_e20_v24?0q8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s_e20_v24?0q8"NSError"16ls32l8s40l8
- ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.1153
- ___block_literal_global.1166
- ___block_literal_global.1182
- ___block_literal_global.151
- ___block_literal_global.154
- ___block_literal_global.301
- ___block_literal_global.321
- ___block_literal_global.326
- ___block_literal_global.370
- ___block_literal_global.378
- ___block_literal_global.636
- ___block_literal_global.647
- ___block_literal_global.695
- _objc_msgSend$accountStatusWithCompletionHandler:
- _objc_msgSend$addTrashObserversIfNecessary
- _objc_msgSend$didAddTrashObservers
- _objc_msgSend$ic_addObserver:forKeyPath:context:explicitOptions:
- _objc_msgSend$isHiddenNoteContainer
- _objc_msgSend$removeAllObserversIfNecessary
- _objc_msgSend$removeTrashObserversIfNecessary
- _objc_msgSend$setDidAddTrashObservers:
- _objc_msgSend$setIsHiddenNoteContainer:
- _objc_msgSend$updateTrashFolderHiddenNoteContainerState
CStrings:
+ "Tq,N,V_lastKnownWalrusStatus"
+ "T{os_unfair_lock_s=I},N,V_backgroundContextLock"
+ "Walrus status changed from %ld to %ld, syncing."
+ "WalrusStatusChanged"
+ "_backgroundContextLock"
+ "_lastKnownWalrusStatus"
+ "accountInfoWithCompletionHandler:"
+ "backgroundContextLock"
+ "hasInvitationMatchingPredicate:context:"
+ "hasNoteMatchingPredicate:context:"
+ "hasVisibleNotes"
+ "hasVisibleNotesInFolder"
+ "ic_hasObjectMatchingPredicate:context:"
+ "lastKnownWalrusStatus"
+ "owner != self && folderType != %d && (folderType != %d || SUBQUERY(notes, $n, $n.markedForDeletion != YES).@count > 0)"
+ "setBackgroundContextLock:"
+ "setLastKnownWalrusStatus:"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "v24@?0@\"CKAccountInfo\"8@\"NSError\"16"
+ "walrusStatus"
+ "{os_unfair_lock_s=I}16@0:8"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MobileNotesSupport/Ironcade/Shared/CoreData/ICAccount.m"
- "AccountInfoChanged"
- "CloudKit account info may have changed (status unchanged). Syncing to pick up potential server-side changes."
- "TB,N,V_didAddTrashObservers"
- "_didAddTrashObservers"
- "accountStatusWithCompletionHandler:"
- "addTrashObserversIfNecessary"
- "didAddTrashObservers"
- "ic_addObserver:forKeyPath:context:explicitOptions:"
- "isHiddenNoteContainer"
- "kICTrashFolderKVOObserverContext"
- "owner != self && isHiddenNoteContainer == NO"
- "removeAllObserversIfNecessary"
- "removeTrashObserversIfNecessary"
- "setDidAddTrashObservers:"
- "setIsHiddenNoteContainer:"
- "updateTrashFolderHiddenNoteContainerState"

```
