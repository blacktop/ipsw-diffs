## NotesShared

> `/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared`

```diff

-2463.0.0.0.0
-  __TEXT.__text: 0x2d16ec
+2481.0.0.0.0
+  __TEXT.__text: 0x2d2ec4
   __TEXT.__auth_stubs: 0x4130
-  __TEXT.__objc_methlist: 0x145f0
+  __TEXT.__objc_methlist: 0x14658
   __TEXT.__const: 0x8a78
-  __TEXT.__cstring: 0x1826f
-  __TEXT.__oslogstring: 0x170b3
-  __TEXT.__gcc_except_tab: 0xd484
+  __TEXT.__cstring: 0x183ef
+  __TEXT.__oslogstring: 0x17267
+  __TEXT.__gcc_except_tab: 0xd4e0
   __TEXT.__dlopen_cstrs: 0x2fb
   __TEXT.__ustring: 0x39a
-  __TEXT.__swift5_typeref: 0x2ccd
+  __TEXT.__swift5_typeref: 0x2d2b
   __TEXT.__constg_swiftt: 0x216c
   __TEXT.__swift5_builtin: 0x17c
   __TEXT.__swift5_reflstr: 0x1118

   __TEXT.__swift5_proto: 0x790
   __TEXT.__swift5_types: 0x264
   __TEXT.__swift5_protos: 0x4c
-  __TEXT.__swift5_capture: 0xed8
+  __TEXT.__swift5_capture: 0xf10
   __TEXT.__swift5_mpenum: 0x68
-  __TEXT.__unwind_info: 0xe140
-  __TEXT.__eh_frame: 0x5a58
+  __TEXT.__unwind_info: 0xe24c
+  __TEXT.__eh_frame: 0x5b08
   __TEXT.__objc_classname: 0x1fa0
-  __TEXT.__objc_methname: 0x31527
-  __TEXT.__objc_methtype: 0x4665
-  __TEXT.__objc_stubs: 0x24160
+  __TEXT.__objc_methname: 0x316c7
+  __TEXT.__objc_methtype: 0x4676
+  __TEXT.__objc_stubs: 0x24240
   __DATA_CONST.__got: 0xed8
-  __DATA_CONST.__const: 0x58e0
+  __DATA_CONST.__const: 0x5918
   __DATA_CONST.__objc_classlist: 0x920
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x18378
-  __DATA_CONST.__objc_selrefs: 0xb480
+  __DATA_CONST.__objc_const: 0x18400
+  __DATA_CONST.__objc_selrefs: 0xb4d8
   __DATA_CONST.__objc_arraydata: 0x1e8
-  __AUTH_CONST.__cfstring: 0xe1c0
+  __AUTH_CONST.__cfstring: 0xe240
   __AUTH_CONST.__objc_const: 0x7880
-  __AUTH_CONST.__const: 0xb608
+  __AUTH_CONST.__const: 0xb660
   __AUTH_CONST.__objc_intobj: 0x390
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x20

   __AUTH.__objc_data: 0x29f0
   __AUTH.__data: 0xca0
   __DATA.__objc_protorefs: 0x88
-  __DATA.__objc_classrefs: 0xdf0
+  __DATA.__objc_classrefs: 0xdf8
   __DATA.__objc_superrefs: 0x680
-  __DATA.__objc_ivar: 0xc74
+  __DATA.__objc_ivar: 0xc78
   __DATA.__objc_data: 0x120
-  __DATA.__data: 0x4618
+  __DATA.__data: 0x4628
   __DATA.__objc_stublist: 0x20
   __DATA.__bss: 0xd890
   __DATA.__common: 0x680

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 48ADADD5-B637-3F87-A607-01E9624C0993
-  Functions: 17263
-  Symbols:   35120
-  CStrings:  15068
+  UUID: E48BB294-DE7D-3DA4-999B-4746E7D003B5
+  Functions: 17289
+  Symbols:   35162
+  CStrings:  15097
 
Symbols:
+ +[ICAppURLUtilities detectedURLInString:allowNonLinkCharacters:]
+ +[ICAppURLUtilities detectedURLInString:allowNonLinkCharacters:].cold.1
+ -[ICCloudContext setShouldResumeSyncOnForeground:]
+ -[ICCloudContext shouldResumeSyncOnForeground]
+ -[ICCloudContext updateCloudContextStateWithCompletion:]
+ -[ICCloudSyncingObject clearServerRecords]
+ -[ICCloudSyncingObject clearServerRecords].cold.1
+ -[ICCloudSyncingObject setServerRecord:].cold.1
+ -[ICCloudSyncingObject setUserSpecificServerRecord:].cold.1
+ -[ICEvernoteResource md5Hash]
+ -[ICEvernoteResource setMd5Hash:]
+ -[ICNote visibleTopLevelAttachmentsCount]
+ -[ICNote visibleTopLevelAttachmentsCount].cold.1
+ -[ICNote(SearchIndexableNote) folderManagedIdentifier]
+ -[ICSearchSuggestion token]
+ GCC_except_table164
+ GCC_except_table187
+ GCC_except_table188
+ GCC_except_table192
+ GCC_except_table299
+ GCC_except_table318
+ GCC_except_table337
+ GCC_except_table347
+ _ICAccountDidPurgeHashtagNotification
+ _OBJC_CLASS_$_NSDataDetector
+ _OBJC_IVAR_$_ICCloudContext._shouldResumeSyncOnForeground
+ _OBJC_IVAR_$_ICEvernoteResource._md5Hash
+ _OBJC_IVAR_$_ICSearchSuggestion._token
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ __OBJC_$_CLASS_METHODS_ICSearchQueryOperation(NotesShared)
+ __OBJC_$_INSTANCE_METHODS_ICSearchQueryOperation(NotesShared)
+ ___106-[ICCloudContext fetchRecordZoneChangesOperation:completedFetchForZoneID:serverChangeToken:error:context:]_block_invoke.531
+ ___44-[ICCloudContext retryOperationsIfNecessary]_block_invoke.604
+ ___44-[ICCloudContext retryOperationsIfNecessary]_block_invoke.608
+ ___45-[ICCloudContext checkForLongLivedOperations]_block_invoke.584
+ ___45-[ICCloudContext checkForLongLivedOperations]_block_invoke.584.cold.1
+ ___45-[ICCloudContext checkForLongLivedOperations]_block_invoke.584.cold.2
+ ___45-[ICCloudContext checkForLongLivedOperations]_block_invoke.584.cold.3
+ ___45-[ICCloudContext checkForLongLivedOperations]_block_invoke.584.cold.4
+ ___45-[ICCloudContext checkForLongLivedOperations]_block_invoke.584.cold.5
+ ___45-[ICCloudContext checkForLongLivedOperations]_block_invoke.585
+ ___50+[ICAccount(Management) cloudKitAccountInContext:]_block_invoke.605
+ ___50+[ICAccount(Management) cloudKitAccountInContext:]_block_invoke.606
+ ___50+[ICAccount(Management) cloudKitAccountInContext:]_block_invoke.606.cold.1
+ ___50+[ICAccount(Management) cloudKitAccountInContext:]_block_invoke_2
+ ___54-[ICCloudContext startRetryTimerIfNecessaryWithError:]_block_invoke.598
+ ___54-[ICCloudContext startRetryTimerIfNecessaryWithError:]_block_invoke.600
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.576
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.577
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.580
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.580.cold.1
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.cold.1
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke_2
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke_2.578
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke_2.cold.1
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke_3
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke_3.cold.1
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke_3.cold.2
+ ___59-[ICCloudContext updateSubscriptionsWithCompletionHandler:]_block_invoke.554
+ ___59-[ICCloudContext updateSubscriptionsWithCompletionHandler:]_block_invoke.556
+ ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1066
+ ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1066.cold.1
+ ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1066.cold.2
+ ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1067
+ ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1068
+ ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1068.cold.1
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke.563
+ ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke.558
+ ___68-[ICCloudContext addOperationToProcessObjectsWithCompletionHandler:]_block_invoke.323
+ ___72-[ICCloudContext _processCloudObjects:operationQueue:completionHandler:]_block_invoke.482
+ ___83-[ICCloudContext fetchRecordZoneChangesForAccountZoneIDs:reason:completionHandler:]_block_invoke.504
+ ___98-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:reason:completionHandler:]_block_invoke.508
+ ___98-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:reason:completionHandler:]_block_invoke_2.509
+ ___block_descriptor_56_e8_32s40bs48r_e20_v24?0q8"NSError"16ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_literal_global.1043
+ ___block_literal_global.1063
+ ___block_literal_global.161
+ ___block_literal_global.275
+ ___block_literal_global.308
+ ___block_literal_global.332
+ ___block_literal_global.516
+ ___block_literal_global.547
+ ___block_literal_global.591
+ ___block_literal_global.944
+ __unnamed_array_storage.865
+ __unnamed_array_storage.885
+ __unnamed_array_storage.892
+ _objc_msgSend$clearServerRecords
+ _objc_msgSend$dataDetectorWithTypes:error:
+ _objc_msgSend$detectedURLInString:allowNonLinkCharacters:
+ _objc_msgSend$isExchangeAccount
+ _objc_msgSend$matchesInString:options:range:
+ _objc_msgSend$md5Hash
+ _objc_msgSend$setMd5Hash:
+ _objc_msgSend$token
+ _objc_msgSend$updateCloudContextStateWithCompletion:
+ _objc_msgSend$visibleTopLevelAttachmentsCount
+ _symbolic So21ICLinkSuggestionQueryC
+ _symbolic So22ICSearchQueryOperationCXMo
+ _symbolic So7NSArrayCSgSo7NSErrorCSgIeyByy_
- +[ICAccount(Management) cloudKitAccountInContext:].cold.6
- -[ICCloudSyncingObject clearServerRecord]
- -[ICEvernoteResource setSha256Hash:]
- -[ICEvernoteResource sha256Hash]
- -[ICNote canAddAttachments:].cold.1
- -[ICSearchSuggestion tokens]
- GCC_except_table184
- GCC_except_table336
- GCC_except_table341
- GCC_except_table346
- _OBJC_IVAR_$_ICEvernoteResource._sha256Hash
- _OBJC_IVAR_$_ICSearchSuggestion._tokens
- __OBJC_$_CLASS_METHODS_ICSearchQueryOperation
- __OBJC_$_INSTANCE_METHODS_ICSearchQueryOperation
- ___106-[ICCloudContext fetchRecordZoneChangesOperation:completedFetchForZoneID:serverChangeToken:error:context:]_block_invoke.528
- ___41-[ICCloudContext updateCloudContextState]_block_invoke
- ___41-[ICCloudContext updateCloudContextState]_block_invoke.573
- ___41-[ICCloudContext updateCloudContextState]_block_invoke.574
- ___41-[ICCloudContext updateCloudContextState]_block_invoke.577
- ___41-[ICCloudContext updateCloudContextState]_block_invoke.577.cold.1
- ___41-[ICCloudContext updateCloudContextState]_block_invoke.cold.1
- ___41-[ICCloudContext updateCloudContextState]_block_invoke_2
- ___41-[ICCloudContext updateCloudContextState]_block_invoke_2.575
- ___41-[ICCloudContext updateCloudContextState]_block_invoke_2.cold.1
- ___41-[ICCloudContext updateCloudContextState]_block_invoke_3
- ___41-[ICCloudContext updateCloudContextState]_block_invoke_3.cold.1
- ___41-[ICCloudContext updateCloudContextState]_block_invoke_3.cold.2
- ___41-[ICSearchSuggestion initWithSuggestion:]_block_invoke
- ___44-[ICCloudContext retryOperationsIfNecessary]_block_invoke.601
- ___44-[ICCloudContext retryOperationsIfNecessary]_block_invoke.605
- ___45-[ICCloudContext checkForLongLivedOperations]_block_invoke.581
- ___45-[ICCloudContext checkForLongLivedOperations]_block_invoke.581.cold.1
- ___45-[ICCloudContext checkForLongLivedOperations]_block_invoke.581.cold.2
- ___45-[ICCloudContext checkForLongLivedOperations]_block_invoke.581.cold.3
- ___45-[ICCloudContext checkForLongLivedOperations]_block_invoke.581.cold.4
- ___45-[ICCloudContext checkForLongLivedOperations]_block_invoke.581.cold.5
- ___45-[ICCloudContext checkForLongLivedOperations]_block_invoke.582
- ___54-[ICCloudContext startRetryTimerIfNecessaryWithError:]_block_invoke.595
- ___54-[ICCloudContext startRetryTimerIfNecessaryWithError:]_block_invoke.597
- ___59-[ICCloudContext updateSubscriptionsWithCompletionHandler:]_block_invoke.551
- ___59-[ICCloudContext updateSubscriptionsWithCompletionHandler:]_block_invoke.553
- ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1062
- ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1062.cold.1
- ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1062.cold.2
- ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1063
- ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1064
- ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1064.cold.1
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke.560
- ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke.555
- ___68-[ICCloudContext addOperationToProcessObjectsWithCompletionHandler:]_block_invoke.320
- ___72-[ICCloudContext _processCloudObjects:operationQueue:completionHandler:]_block_invoke.479
- ___83-[ICCloudContext fetchRecordZoneChangesForAccountZoneIDs:reason:completionHandler:]_block_invoke.501
- ___98-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:reason:completionHandler:]_block_invoke.505
- ___98-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:reason:completionHandler:]_block_invoke_2.506
- ___block_descriptor_32_e43_"ICSearchToken"16?0"_CSSuggestionToken"8l
- ___block_descriptor_40_e8_32s_e20_v24?0q8"NSError"16ls32l8
- ___block_literal_global.1039
- ___block_literal_global.1059
- ___block_literal_global.155
- ___block_literal_global.269
- ___block_literal_global.305
- ___block_literal_global.326
- ___block_literal_global.423
- ___block_literal_global.511
- ___block_literal_global.544
- ___block_literal_global.588
- ___block_literal_global.84
- ___block_literal_global.940
- __unnamed_array_storage.859
- __unnamed_array_storage.880
- __unnamed_array_storage.887
- _objc_msgSend$clearServerRecord
- _objc_msgSend$setSha256Hash:
- _objc_msgSend$sha256Hash
CStrings:
+ "-[ICCloudSyncingObject setServerRecord:]"
+ "-[ICCloudSyncingObject setUserSpecificServerRecord:]"
+ "@\"ICSearchToken\""
+ "Can't add attachments %lu %lu %lu %p"
+ "Clearing server records… {object: %@}"
+ "Could not create NSDataDetector."
+ "Duplicate record ID after sorting in ICCloudContext"
+ "Duplicate record ID after sorting in ICCloudContext — skipping {recordID: %@}"
+ "Error fetching count of visible top level attachments via fetch request. Falling back to fetch attachment objects for count (%lu)"
+ "ICAccountDidPurgeHashtagNotification"
+ "Setting server record with mismatched record name"
+ "Setting server record with mismatched record name {objectRecordName: %@, serverRecordName: %@}"
+ "Setting user-specific server record with mismatched shared record name"
+ "Setting user-specific server record with mismatched shared record name {serverRecordName: %@, objectRecordName: %@}"
+ "T@\"ICSearchToken\",R,N,V_token"
+ "T@\"NSString\",C,N,V_md5Hash"
+ "TB,N,V_shouldResumeSyncOnForeground"
+ "_md5Hash"
+ "_shouldResumeSyncOnForeground"
+ "_token"
+ "clearServerRecords"
+ "dataDetectorWithTypes:error:"
+ "detectedURLInString:allowNonLinkCharacters:"
+ "folderManagedIdentifier"
+ "matchesInString:options:range:"
+ "md5Hash"
+ "note == %@ AND parentAttachment == nil"
+ "searchSuggestionsQueue"
+ "setMd5Hash:"
+ "setShouldResumeSyncOnForeground:"
+ "shouldResumeSyncOnForeground"
+ "suggestionSearchResultsWithLinkSuggestionQuery:completionHandler:"
+ "token"
+ "updateCloudContextStateWithCompletion:"
+ "v32@0:8@\"ICLinkSuggestionQuery\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "visibleTopLevelAttachmentsCount"
- "@\"ICSearchToken\"16@?0@\"_CSSuggestionToken\"8"
- "Can't add attachments %lu %lu %p %lu %p"
- "Reading image/photo data"
- "T@\"NSArray\",R,N,V_tokens"
- "T@\"NSString\",C,N,V_sha256Hash"
- "Transmitting image/photo data"
- "_sha256Hash"
- "_tokens"
- "clearServerRecord"
- "http://%@"
- "setSha256Hash:"
- "sha256Hash"

```
