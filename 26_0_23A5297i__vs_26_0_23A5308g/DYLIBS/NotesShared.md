## NotesShared

> `/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared`

```diff

-2948.0.0.502.2
-  __TEXT.__text: 0x34a104
-  __TEXT.__auth_stubs: 0x5190
-  __TEXT.__objc_methlist: 0x17acc
-  __TEXT.__const: 0xcc54
-  __TEXT.__cstring: 0x1a4ff
-  __TEXT.__oslogstring: 0x1c238
-  __TEXT.__gcc_except_tab: 0xfd30
+2952.0.0.0.0
+  __TEXT.__text: 0x34b0f4
+  __TEXT.__auth_stubs: 0x51a0
+  __TEXT.__objc_methlist: 0x17afc
+  __TEXT.__const: 0xcc44
+  __TEXT.__cstring: 0x1a58f
+  __TEXT.__oslogstring: 0x1c358
+  __TEXT.__gcc_except_tab: 0xfd48
   __TEXT.__dlopen_cstrs: 0x2fb
   __TEXT.__ustring: 0x38e
-  __TEXT.__swift5_typeref: 0x43ca
+  __TEXT.__swift5_typeref: 0x43d0
   __TEXT.__swift5_fieldmd: 0x2d6c
   __TEXT.__constg_swiftt: 0x366c
   __TEXT.__swift5_reflstr: 0x2058

   __TEXT.__swift_as_entry: 0x19c
   __TEXT.__swift_as_ret: 0x1c8
   __TEXT.__swift5_mpenum: 0x74
-  __TEXT.__unwind_info: 0xefe8
+  __TEXT.__unwind_info: 0xf018
   __TEXT.__eh_frame: 0x9068
   __TEXT.__objc_classname: 0x2123
-  __TEXT.__objc_methname: 0x35c56
-  __TEXT.__objc_methtype: 0x4bb5
-  __TEXT.__objc_stubs: 0x26a00
-  __DATA_CONST.__got: 0x2110
+  __TEXT.__objc_methname: 0x35e04
+  __TEXT.__objc_methtype: 0x4bc9
+  __TEXT.__objc_stubs: 0x26b00
+  __DATA_CONST.__got: 0x2118
   __DATA_CONST.__const: 0x62e8
   __DATA_CONST.__objc_classlist: 0xa30
   __DATA_CONST.__objc_catlist: 0x130
   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc730
+  __DATA_CONST.__objc_selrefs: 0xc780
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x6c0
   __DATA_CONST.__objc_arraydata: 0x1e8
-  __AUTH_CONST.__auth_got: 0x28e0
-  __AUTH_CONST.__const: 0xcea8
-  __AUTH_CONST.__cfstring: 0xf1a0
-  __AUTH_CONST.__objc_const: 0x21850
+  __AUTH_CONST.__auth_got: 0x28e8
+  __AUTH_CONST.__const: 0xd5d8
+  __AUTH_CONST.__cfstring: 0xf240
+  __AUTH_CONST.__objc_const: 0x21820
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x3798
+  __AUTH.__objc_data: 0x36f8
   __AUTH.__data: 0x1690
   __DATA.__objc_ivar: 0xd2c
-  __DATA.__data: 0x4b90
+  __DATA.__data: 0x4ba0
   __DATA.__objc_stublist: 0x20
-  __DATA.__bss: 0x10de0
+  __DATA.__bss: 0x10d60
   __DATA.__common: 0x1b8
-  __DATA_DIRTY.__objc_data: 0x3d90
-  __DATA_DIRTY.__data: 0x1888
-  __DATA_DIRTY.__bss: 0x20a8
+  __DATA_DIRTY.__objc_data: 0x3e30
+  __DATA_DIRTY.__data: 0x1898
+  __DATA_DIRTY.__bss: 0x2128
   __DATA_DIRTY.__common: 0x1b8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 85A028FD-738C-3799-BDB7-ADC900D2AC55
-  Functions: 18345
-  Symbols:   38187
-  CStrings:  16473
+  UUID: A3DADA7B-7AB5-3AE2-B946-A73E78395AB6
+  Functions: 18359
+  Symbols:   38211
+  CStrings:  16503
 
Symbols:
+ -[ICAccount visibleRootFolderWithTitle:]
+ -[ICAttachment(CloudKit) fixBrokenReferencesWithError:]
+ -[ICCloudSyncingObject findAndResaveUserSpecificRecordThrowingReferenceViolationForDeletionWithError:]
+ -[ICCloudSyncingObject fixBrokenReferencesWithError:]
+ -[ICCloudSyncingObject hasExpectedReferenceActionsInUserSpecificRecord:]
+ -[ICCloudSyncingObject updateNeedsToSaveUserSpecificRecordToUpdateReferenceActionsIfNeeded]
+ -[ICFolder visibleChildFolderWithTitle:]
+ -[ICFolder(CloudKit) fixBrokenReferencesWithError:]
+ -[ICFolder(CloudKit) fixBrokenReferencesWithError:].cold.1
+ -[ICFolder(CloudKit) hasExpectedReferenceActionsInUserSpecificRecord:]
+ -[ICMedia(CloudKit) fixBrokenReferencesWithError:]
+ -[ICNote(CloudKit) fixBrokenReferencesWithError:]
+ -[ICNote(CloudKit) hasExpectedReferenceActionsInUserSpecificRecord:]
+ -[ICNote(SearchIndexableNote) csPersonForShareParticipant:]
+ -[ICNotePasteboardData persistenceData].cold.1
+ GCC_except_table198
+ _CKErrorIsCode
+ _CKErrorServerDescriptionKey
+ _ICTTAttributeNameGeneratedByWritingTools
+ ___106-[ICCloudContext fetchRecordZoneChangesOperation:completedFetchForZoneID:serverChangeToken:error:context:]_block_invoke.602
+ ___43-[ICTableAttachmentProvider setAttachment:]_block_invoke
+ ___44-[ICCloudContext retryOperationsIfNecessary]_block_invoke.688
+ ___44-[ICCloudContext retryOperationsIfNecessary]_block_invoke.692
+ ___50+[ICAccount(Management) cloudKitAccountInContext:]_block_invoke.652
+ ___50+[ICAccount(Management) cloudKitAccountInContext:]_block_invoke.652.cold.1
+ ___54-[ICCloudContext startRetryTimerIfNecessaryWithError:]_block_invoke.682
+ ___54-[ICCloudContext startRetryTimerIfNecessaryWithError:]_block_invoke.684
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.654
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.657
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.657.cold.1
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke_2.655
+ ___59-[ICCloudContext updateSubscriptionsWithCompletionHandler:]_block_invoke.625
+ ___59-[ICCloudContext updateSubscriptionsWithCompletionHandler:]_block_invoke.627
+ ___62+[ICCloudSyncingObject deleteTemporaryAssetFilesForOperation:]_block_invoke.247
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke.637
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke.639
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.640
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.640.cold.1
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.640.cold.2
+ ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke.632
+ ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.633
+ ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.633.cold.1
+ ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.633.cold.2
+ ___67-[ICCloudContext _processCloudObjects:inSession:completionHandler:]_block_invoke.548
+ ___67-[ICCloudContext _processCloudObjects:inSession:completionHandler:]_block_invoke_2.549
+ ___74-[ICCloudContext enqueueLongLivedOperationsIfNeededWithCompletionHandler:]_block_invoke.661
+ ___74-[ICCloudContext enqueueLongLivedOperationsIfNeededWithCompletionHandler:]_block_invoke_2.663
+ ___84-[ICCloudContext fetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:]_block_invoke.573
+ ___88-[ICCloudContext enqueueLongLivedOperationsWithIDsIfNeeded:container:completionHandler:]_block_invoke.670
+ ___99-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:]_block_invoke.577
+ ___99-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:]_block_invoke_2.578
+ ___block_literal_global.234
+ ___block_literal_global.250
+ ___block_literal_global.317
+ ___block_literal_global.480
+ ___block_literal_global.497
+ ___block_literal_global.500
+ ___block_literal_global.503
+ ___block_literal_global.506
+ ___block_literal_global.509
+ ___block_literal_global.511
+ ___block_literal_global.618
+ ___block_literal_global.636
+ ___block_literal_global.665
+ ___unnamed_10
+ ___unnamed_11
+ _objc_msgSend$csPersonForShareParticipant:
+ _objc_msgSend$findAndResaveUserSpecificRecordThrowingReferenceViolationForDeletionWithError:
+ _objc_msgSend$fixBrokenReferencesWithError:
+ _objc_msgSend$hasExpectedReferenceActionsInUserSpecificRecord:
+ _objc_msgSend$needsToUpdateUserSpecificRecordReferenceActions
+ _objc_msgSend$objectWithRecordID:accountID:context:
+ _objc_msgSend$referenceAction
+ _objc_msgSend$setNeedsToUpdateUserSpecificRecordReferenceActions:
+ _objc_msgSend$setPrimaryRecipients:
+ _symbolic Igh_
- -[ICAccount(SearchIndexable) authorsExcludingCurrentUser]
- -[ICAttachment(CloudKit) fixBrokenReferences]
- -[ICAttachment(SearchIndexable) authorsExcludingCurrentUser]
- -[ICCloudSyncingObject fixBrokenReferences]
- -[ICFolder(CloudKit) fixBrokenReferences]
- -[ICFolder(CloudKit) fixBrokenReferences].cold.1
- -[ICFolder(SearchIndexable) authorsExcludingCurrentUser]
- -[ICHashtag(SearchIndexable) authorsExcludingCurrentUser]
- -[ICMedia(CloudKit) fixBrokenReferences]
- -[ICNote(CloudKit) fixBrokenReferences]
- GCC_except_table170
- GCC_except_table193
- GCC_except_table273
- GCC_except_table285
- ___106-[ICCloudContext fetchRecordZoneChangesOperation:completedFetchForZoneID:serverChangeToken:error:context:]_block_invoke.601
- ___44-[ICCloudContext retryOperationsIfNecessary]_block_invoke.687
- ___44-[ICCloudContext retryOperationsIfNecessary]_block_invoke.691
- ___50+[ICAccount(Management) cloudKitAccountInContext:]_block_invoke.650
- ___50+[ICAccount(Management) cloudKitAccountInContext:]_block_invoke.651.cold.1
- ___54-[ICCloudContext startRetryTimerIfNecessaryWithError:]_block_invoke.681
- ___54-[ICCloudContext startRetryTimerIfNecessaryWithError:]_block_invoke.683
- ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.652
- ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.656
- ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.656.cold.1
- ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke_2.654
- ___59-[ICCloudContext updateSubscriptionsWithCompletionHandler:]_block_invoke.624
- ___59-[ICCloudContext updateSubscriptionsWithCompletionHandler:]_block_invoke.626
- ___62+[ICCloudSyncingObject deleteTemporaryAssetFilesForOperation:]_block_invoke.233
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke.636
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke.638
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.639
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.639.cold.1
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.639.cold.2
- ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke.631
- ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.632
- ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.632.cold.1
- ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.632.cold.2
- ___67-[ICCloudContext _processCloudObjects:inSession:completionHandler:]_block_invoke.547
- ___67-[ICCloudContext _processCloudObjects:inSession:completionHandler:]_block_invoke_2.548
- ___74-[ICCloudContext enqueueLongLivedOperationsIfNeededWithCompletionHandler:]_block_invoke.660
- ___74-[ICCloudContext enqueueLongLivedOperationsIfNeededWithCompletionHandler:]_block_invoke_2.662
- ___84-[ICCloudContext fetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:]_block_invoke.572
- ___88-[ICCloudContext enqueueLongLivedOperationsWithIDsIfNeeded:container:completionHandler:]_block_invoke.669
- ___99-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:]_block_invoke.576
- ___99-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:]_block_invoke_2.577
- ___block_literal_global.216
- ___block_literal_global.220
- ___block_literal_global.236
- ___block_literal_global.303
- ___block_literal_global.466
- ___block_literal_global.484
- ___block_literal_global.487
- ___block_literal_global.490
- ___block_literal_global.493
- ___block_literal_global.496
- ___block_literal_global.498
- ___block_literal_global.617
- ___block_literal_global.635
- ___block_literal_global.664
- _objc_msgSend$fixBrokenReferences
CStrings:
+ "\"([^\"]+)\""
+ "-%@"
+ "?"
+ "@\"CKContainer\""
+ "@\"ICQueryObjC\""
+ "Error while serializing persistence data: %@"
+ "Fixing broken references for folder: %@\n\tParent: %@\n\tNotes: %@\n\tChildren: %@\n\tError: %@"
+ "Found user-specific record reference violation for %@, marking referenced object %@ as needing to save user-specific record to correct reference action"
+ "Local object not found referenced by user-specific record with record name %@"
+ "T@\"NSManagedObject<ICAccountObject>\",R,&,N"
+ "TTAttributeNameGeneratedByWritingTools"
+ "\\[([^\\]]+)\\]"
+ "_UserSpecific::"
+ "csPersonForShareParticipant:"
+ "findAndResaveUserSpecificRecordThrowingReferenceViolationForDeletionWithError:"
+ "fixBrokenReferencesWithError:"
+ "hasExpectedReferenceActionsInUserSpecificRecord:"
+ "needsToUpdateUserSpecificRecordReferenceActions"
+ "recordID=([^,]+)"
+ "referenceAction"
+ "setNeedsToUpdateUserSpecificRecordReferenceActions:"
+ "setPrimaryRecipients:"
+ "updateNeedsToSaveUserSpecificRecordToUpdateReferenceActionsIfNeeded"
+ "v24@0:8@\"NSError\"16"
+ "visibleChildFolderWithTitle:"
+ "visibleRootFolderWithTitle:"
- "-%@-%@"
- "Fixing broken references for folder: %@\n\tParent: %@\n\tNotes: %@\n\tChildren: %@"
- "T@\"NSManagedObject<ICAccountObject>\",R,C,N"
- "fixBrokenReferences"

```
