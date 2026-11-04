## NotesShared

> `/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared`

```diff

-3001.42.1.0.0
-  __TEXT.__text: 0x343d2c
+3001.60.6.0.0
+  __TEXT.__text: 0x34b670
   __TEXT.__delay_stubs: 0x240
   __TEXT.__delay_helper: 0x830
-  __TEXT.__objc_methlist: 0x1856c
-  __TEXT.__const: 0xdde8
-  __TEXT.__cstring: 0x19614
-  __TEXT.__gcc_except_tab: 0xf1a8
-  __TEXT.__oslogstring: 0x1eb39
+  __TEXT.__objc_methlist: 0x186ec
+  __TEXT.__const: 0xde18
+  __TEXT.__cstring: 0x19c44
+  __TEXT.__gcc_except_tab: 0xf260
+  __TEXT.__oslogstring: 0x1f5d9
   __TEXT.__ustring: 0x39a
-  __TEXT.__swift5_typeref: 0x4550
+  __TEXT.__swift5_typeref: 0x4570
   __TEXT.__swift5_fieldmd: 0x2f8c
-  __TEXT.__constg_swiftt: 0x37d8
+  __TEXT.__constg_swiftt: 0x37f8
   __TEXT.__swift5_builtin: 0x208
   __TEXT.__swift5_reflstr: 0x2261
   __TEXT.__swift5_assocty: 0x7e0

   __TEXT.__swift_as_ret: 0x1b8
   __TEXT.__swift_as_cont: 0x3f4
   __TEXT.__swift5_mpenum: 0x74
-  __TEXT.__unwind_info: 0x127a0
-  __TEXT.__eh_frame: 0x891c
+  __TEXT.__unwind_info: 0x128e0
+  __TEXT.__eh_frame: 0x894c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x65a0
+  __DATA_CONST.__const: 0x6830
   __DATA_CONST.__objc_classlist: 0xa88
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xcd10
+  __DATA_CONST.__objc_selrefs: 0xce38
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x6c0
   __DATA_CONST.__objc_arraydata: 0x228
   __DATA_CONST.__got: 0x2148
-  __AUTH_CONST.__const: 0xdcc8
-  __AUTH_CONST.__cfstring: 0xfc20
-  __AUTH_CONST.__objc_const: 0x229b0
+  __AUTH_CONST.__const: 0xdce8
+  __AUTH_CONST.__cfstring: 0xfee0
+  __AUTH_CONST.__objc_const: 0x229c8
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x450
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x2ac0
+  __AUTH_CONST.__auth_got: 0x2b18
   __AUTH.__objc_data: 0x2d60
-  __AUTH.__data: 0x1700
+  __AUTH.__data: 0x1720
   __DATA.__objc_ivar: 0xd8c
-  __DATA.__data: 0x4ba4
+  __DATA.__data: 0x4c04
   __DATA.__objc_stublist: 0x20
   __DATA.__common: 0x188
   __DATA_DIRTY.__objc_data: 0x4a68
-  __DATA_DIRTY.__data: 0x1cb8
-  __DATA_DIRTY.__bss: 0x2a40
+  __DATA_DIRTY.__data: 0x1ca8
+  __DATA_DIRTY.__bss: 0x2a38
   __DATA_DIRTY.__common: 0x1f0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/Coherence.framework/Coherence
   - /System/Library/PrivateFrameworks/DataDetectorsCore.framework/DataDetectorsCore
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
+  - /System/Library/PrivateFrameworks/GenerativePartnerServiceUI.framework/GenerativePartnerServiceUI
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 18726
-  Symbols:   17851
-  CStrings:  5363
+  Functions: 18808
+  Symbols:   17917
+  CStrings:  5433
 
Symbols:
+ +[ICAccount(CloudKit) ic_isNoteBlockedFromPushing:]
+ +[ICAccount(CloudKit) ic_notesOnOtherPushes:]
+ +[ICAccount(CloudKit) ic_recentlyDeletedPushWaitTimeout]
+ +[ICAccount(CloudKit) ic_waitForOtherPushesOfNotes:inContext:until:then:]
+ +[ICAccount(Management) ic_manageStorageMoveBatchSize]
+ +[ICAccount(Management) ic_moveAllOwnedContentToRecentlyDeletedForAccountIdentifier:context:before:deletingFolders:savedHandler:completionHandler:]
+ +[ICAppURLUtilities acAccountIDInURL:]
+ +[ICAppURLUtilities accountToMoveAllToRecentlyDeletedInURL:context:]
+ +[ICAppURLUtilities isManageStorageMoveAllToRecentlyDeletedURL:]
+ +[ICAppURLUtilities isPrivateSettingsURL:]
+ +[ICAppURLUtilities manageStorageMoveAllToRecentlyDeletedURLForACAccountID:]
+ +[ICNote(LocalRecovery) copyNote:intoLocalFolder:]
+ +[ICNote(LocalRecovery) recoverNote:intoLocalFolder:]
+ -[ICAccount(CloudKit) hasUnsyncedNotesInRecentlyDeleted]
+ -[ICAccount(CloudKit) ic_pushOwedRecentlyDeletedObjectsInContext:cloudContext:waitingUntil:completionHandler:]
+ -[ICAccount(CloudKit) ic_pushRecentlyDeletedNotesWithCloudContext:completionHandler:]
+ -[ICAccount(CloudKit) ic_pushRecentlyDeletedNotesWithCompletionHandler:]
+ -[ICAccount(CloudKit) ic_recentlyDeletedNotesOwingPushWithLimit:]
+ -[ICAccount(Management) ic_deleteAllOwnedCustomFoldersBefore:]
+ -[ICAccount(Management) ic_deleteOwnedCustomFolderTree:rescuedNoteCount:]
+ -[ICAccount(Management) ic_folderTreeHoldsSparedNote:before:includingBlockedNotes:]
+ -[ICAccount(Management) ic_moveAllOwnedContentToRecentlyDeletedBefore:deletingFolders:savedHandler:completionHandler:]
+ -[ICAccount(Management) ic_moveAllOwnedNotesToRecentlyDeletedBefore:error:]
+ -[ICAccount(Management) ic_ownedSharedRootObjectsBefore:includingFolders:]
+ -[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:isResumedLongLivedOperation:]
+ -[ICCloudContext addResumedLongLivedModifyRecordsOperation:]
+ -[ICCloudContext adoptSharedOwnerFromUserSpecificRecordParser:forPlaceholder:]
+ -[ICCloudContext dropAdoptedOwnerFromPlaceholder:resolvedByRecord:]
+ -[ICNote(LocalRecovery) ic_wholeTextAttachmentCount]
+ -[ICQueryResultsController contains:]
+ GCC_except_table163
+ GCC_except_table173
+ GCC_except_table176
+ GCC_except_table211
+ GCC_except_table221
+ GCC_except_table253
+ GCC_except_table263
+ GCC_except_table292
+ GCC_except_table366
+ GCC_except_table402
+ GCC_except_table408
+ GCC_except_table417
+ GCC_except_table420
+ GCC_except_table421
+ GCC_except_table448
+ GCC_except_table458
+ _ICManageStorageSparesNote
+ __OBJC_$_CLASS_METHODS_ICNote(ActivityEvents|AirDropDocument|CloudKit|Management|AttachmentManagement|LocalRecovery|SearchIndexableNote|NotesShared|NotesShared1)
+ __OBJC_$_INSTANCE_METHODS_ICNote(ActivityEvents|AirDropDocument|CloudKit|Management|AttachmentManagement|LocalRecovery|SearchIndexableNote|NotesShared|NotesShared1)
+ __OBJC_CLASS_PROTOCOLS_$_ICNote(ActivityEvents|AirDropDocument|CloudKit|Management|AttachmentManagement|LocalRecovery|SearchIndexableNote|NotesShared|NotesShared1)
+ ___110-[ICAccount(CloudKit) ic_pushOwedRecentlyDeletedObjectsInContext:cloudContext:waitingUntil:completionHandler:]_block_invoke
+ ___110-[ICAccount(CloudKit) ic_pushOwedRecentlyDeletedObjectsInContext:cloudContext:waitingUntil:completionHandler:]_block_invoke_2
+ ___118-[ICAccount(Management) ic_moveAllOwnedContentToRecentlyDeletedBefore:deletingFolders:savedHandler:completionHandler:]_block_invoke
+ ___118-[ICAccount(Management) ic_moveAllOwnedContentToRecentlyDeletedBefore:deletingFolders:savedHandler:completionHandler:]_block_invoke_2
+ ___118-[ICAccount(Management) ic_moveAllOwnedContentToRecentlyDeletedBefore:deletingFolders:savedHandler:completionHandler:]_block_invoke_3
+ ___119-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:isResumedLongLivedOperation:]_block_invoke
+ ___119-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:isResumedLongLivedOperation:]_block_invoke_2
+ ___119-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:isResumedLongLivedOperation:]_block_invoke_3
+ ___147+[ICAccount(Management) ic_moveAllOwnedContentToRecentlyDeletedForAccountIdentifier:context:before:deletingFolders:savedHandler:completionHandler:]_block_invoke
+ ___147+[ICAccount(Management) ic_moveAllOwnedContentToRecentlyDeletedForAccountIdentifier:context:before:deletingFolders:savedHandler:completionHandler:]_block_invoke_2
+ ___45+[ICAccount(CloudKit) ic_notesOnOtherPushes:]_block_invoke
+ ___52-[ICNote(LocalRecovery) ic_wholeTextAttachmentCount]_block_invoke
+ ___56-[ICAccount(CloudKit) hasUnsyncedNotesInRecentlyDeleted]_block_invoke
+ ___73+[ICAccount(CloudKit) ic_waitForOtherPushesOfNotes:inContext:until:then:]_block_invoke
+ ___73+[ICAccount(CloudKit) ic_waitForOtherPushesOfNotes:inContext:until:then:]_block_invoke_2
+ ___85-[ICAccount(CloudKit) ic_pushRecentlyDeletedNotesWithCloudContext:completionHandler:]_block_invoke
+ ___85-[ICAccount(CloudKit) ic_pushRecentlyDeletedNotesWithCloudContext:completionHandler:]_block_invoke_2
+ ___85-[ICAccount(CloudKit) ic_pushRecentlyDeletedNotesWithCloudContext:completionHandler:]_block_invoke_3
+ ___ICDuplicateNoteForRecovery_block_invoke
+ ___block_descriptor_40_e8_32s_e34_B32?0"NSManagedObjectID"8Q16^B24ls32l8
+ ___block_descriptor_41_e8_32bs_e23_v24?0"NSError"8B16B20ls32l8
+ ___block_descriptor_41_e8_32bs_e8_v12?0B8ls32l8
+ ___block_descriptor_48_e8_32s40r_e27_v40?08{_NSRange=QQ}16^B32ls32l8r40l8
+ ___block_descriptor_49_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_50_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e45_v32?0"CKRecordID"8"CKRecord"16"NSError"24ls32l8w48l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56r64w_e41_v32?0"NSArray"8"NSArray"16"NSError"24lr56l8w64l8s32l8s40l8s48l8
+ ___block_descriptor_73_e8_32s40s48s56bs64bs_e5_v8?0ls32l8s40l8s56l8s48l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_81_e8_32s40s48s56bs64bs72r_e17_v16?0"NSError"8lr72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_81_e8_32s40s48s56s64bs72bs_e17_v16?0"NSError"8ls32l8s40l8s64l8s48l8s56l8s72l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_89_e8_32s40s48s56s64bs72bs80r_e5_v8?0lr80l8s32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72bs80bs_e5_v8?0ls32l8s40l8s72l8s48l8s56l8s64l8s80l8
+ _symbolic ______pSg 26GenerativePartnerServiceUI11LLMProviderP
+ _symbolic _____yS2SSgG s18_DictionaryStorageC
- -[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]
- GCC_except_table168
- GCC_except_table210
- GCC_except_table261
- GCC_except_table290
- GCC_except_table337
- GCC_except_table364
- GCC_except_table369
- GCC_except_table400
- GCC_except_table419
- GCC_except_table445
- GCC_except_table450
- GCC_except_table455
- __OBJC_$_CLASS_METHODS_ICNote(ActivityEvents|AirDropDocument|CloudKit|Management|AttachmentManagement|SearchIndexableNote|NotesShared|NotesShared1)
- __OBJC_$_INSTANCE_METHODS_ICNote(ActivityEvents|AirDropDocument|CloudKit|Management|AttachmentManagement|SearchIndexableNote|NotesShared|NotesShared1)
- __OBJC_CLASS_PROTOCOLS_$_ICNote(ActivityEvents|AirDropDocument|CloudKit|Management|AttachmentManagement|SearchIndexableNote|NotesShared|NotesShared1)
- ___36+[ICAuthenticationState sharedState]_block_invoke
- ___49+[ICCryptoConvergenceController sharedController]_block_invoke
- ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke
- ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke_2
- ___block_descriptor_64_e8_32s40s48r56w_e41_v32?0"NSArray"8"NSArray"16"NSError"24lr48l8w56l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48r56w_e45_v32?0"CKRecordID"8"CKRecord"16"NSError"24lr48l8s32l8w56l8s40l8
- _sharedState.onceToken
CStrings:
+ "Account has no managed object context"
+ "Account vanished before its content could be moved"
+ "B32@?0@\"NSManagedObjectID\"8Q16^B24"
+ "Cannot password-protect note {originalNote: %@}"
+ "Duplicated note"
+ "Duplicating note… {originalNote: %@, folder: %@}%s:%d"
+ "Error copying values to note %@"
+ "Error retrieving summarization provider display name"
+ "Error retrieving summarization provider icon symbol name"
+ "Failed to copy note values — deleting duplicated note {originalNote: %@, duplicatedNote: %@}"
+ "Failed to count ICSearchIndexState entities: %@"
+ "Failed to save after duplicating note {originalNote: %@, duplicatedNote: %@}"
+ "Failed to save after moving content to Recently Deleted"
+ "Failed to save note data — deleting duplicated note {originalNote: %@, duplicatedNote: %@}"
+ "ICManageStorage"
+ "ICNote * _Nullable ICDuplicateNoteForRecovery(ICNote *__strong, ICFolder *__strong)"
+ "ICNote * _Nullable ICDuplicateNoteForRecovery(ICNote *__strong, ICFolder *__strong)_block_invoke"
+ "ManageStorageFetchBeforeMove"
+ "ManageStorageMoveAllToRecentlyDeleted"
+ "ManageStoragePushRecentlyDeleted"
+ "Move"
+ "Move to Recently Deleted (Manage Storage folder cleanup)"
+ "Move to Recently Deleted (Manage Storage)"
+ "No worker context available"
+ "Not an iCloud account"
+ "Placeholder from a user-specific record is another user's shared object {object: %@}"
+ "Placeholder is resolved by a record of ours; dropping the owner its user-specific record gave it {object: %@}"
+ "Promoted joined subfolder out of a deleted custom folder (Manage Storage)"
+ "Re-parented joined note out of a deleted custom folder (Manage Storage)"
+ "Recently Deleted still owes a push"
+ "Refusing a Manage Storage deeplink that names the local account"
+ "Refusing a Manage Storage deeplink that resolved to a non-iCloud account"
+ "Response from %@: %@"
+ "Safety mechanism update required. You can see the status in [Apple Intelligence & Siri Settings](chinaai-settings)."
+ "Saved after duplicating note {originalNote: %@, duplicatedNote: %@}"
+ "Saved while duplicating note"
+ "Simulating quota exceeded, so not sending %@ with %lu trash recovery objects"
+ "Summary Provider"
+ "Sync isn't ready"
+ "Timed out fetching before the move"
+ "Transcript summarization is temporarily restricted due to triggering safety alerts multiple times."
+ "Unable to create a summary from this content."
+ "Unable to proceed. This content may not comply with laws and regulations."
+ "[MSQFA] Account %@ has no managed object context; cannot move content to Recently Deleted"
+ "[MSQFA] Account %@ not found; nothing to move to Recently Deleted"
+ "[MSQFA] Account %@ vanished after unsharing; aborting"
+ "[MSQFA] Account %@: Manage Storage cleanup sync complete"
+ "[MSQFA] Account %@: Recently Deleted is fully pushed, so not failing the delete on that sync error"
+ "[MSQFA] Account %@: Recently Deleted still owes a push after pushing it {note: %@, error: %@}"
+ "[MSQFA] Account %@: another push has %lu Recently Deleted note(s) on the way; pushing again once it's done"
+ "[MSQFA] Account %@: couldn't delete %lu share(s) before pushing Recently Deleted: %@"
+ "[MSQFA] Account %@: deleting %lu custom folder(s) {keptForNotesLeftInPlace: %lu, joinedNotesMovedToDefaultFolder: %lu}"
+ "[MSQFA] Account %@: error unsharing owned shares (continuing with delete): %@"
+ "[MSQFA] Account %@: fetch before the move failed, moving what's local: %@"
+ "[MSQFA] Account %@: moved %lu note(s) to Recently Deleted, deleted %lu custom folder(s)"
+ "[MSQFA] Account %@: moving %lu note(s) to Recently Deleted {joined: %lu, blocked: %lu, madeOrMovedAfterCutoff: %lu, cutoff: %{public}@, newestMovedDate: %{public}@}"
+ "[MSQFA] Account %@: no worker context available; aborting"
+ "[MSQFA] Account %@: not pushing %lu Recently Deleted note(s) yet; sync isn't ready"
+ "[MSQFA] Account %@: pushing %lu Recently Deleted object(s) on their own"
+ "[MSQFA] Account %@: pushing Recently Deleted failed (syncing anyway): %@"
+ "[MSQFA] Account %@: save failed with %lu note(s) already in Recently Deleted: %@"
+ "[MSQFA] Account %@: saved local changes, starting sync"
+ "[MSQFA] Account %@: sync error: %@"
+ "[MSQFA] Account %@: unsharing %lu owned share(s)"
+ "[MSQFA] Refusing to move content to Recently Deleted for account %@: it isn't an iCloud account"
+ "account == %@ AND serverShareData != nil"
+ "applenotessettings"
+ "folder.account == %@ AND serverShareData != nil"
+ "manageStorageMoveAllToRecentlyDeleted"
+ "settings-navigation://com.apple.Settings.Siri"
+ "text.line.2.summary"
+ "v24@?0@\"NSError\"8B16B20"
- "Failed to fetch ICSearchIndexState entities: %@"
- "Simulating quota exceeded for record recovering from trash: %@"
```
