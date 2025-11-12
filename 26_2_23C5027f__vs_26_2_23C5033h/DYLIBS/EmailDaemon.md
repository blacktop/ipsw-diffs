## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3864.300.11.2.1
-  __TEXT.__text: 0x26429c
+3864.300.22.2.1
+  __TEXT.__text: 0x2642f4
   __TEXT.__auth_stubs: 0x2710
-  __TEXT.__objc_methlist: 0x12ee4
-  __TEXT.__const: 0x398c
-  __TEXT.__gcc_except_tab: 0x4e828
-  __TEXT.__cstring: 0x2665a
-  __TEXT.__oslogstring: 0x1a084
+  __TEXT.__objc_methlist: 0x12f1c
+  __TEXT.__const: 0x397c
+  __TEXT.__gcc_except_tab: 0x4e8b0
+  __TEXT.__cstring: 0x2668a
+  __TEXT.__oslogstring: 0x19e54
   __TEXT.__dlopen_cstrs: 0x3bc
   __TEXT.__ustring: 0x22
   __TEXT.__constg_swiftt: 0xb84

   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x107f0
+  __TEXT.__unwind_info: 0x10828
   __TEXT.__eh_frame: 0xfb0
   __TEXT.__objc_classname: 0x2bfe
-  __TEXT.__objc_methname: 0x373f8
-  __TEXT.__objc_methtype: 0x7807
-  __TEXT.__objc_stubs: 0x24cc0
+  __TEXT.__objc_methname: 0x374a1
+  __TEXT.__objc_methtype: 0x77ec
+  __TEXT.__objc_stubs: 0x24d40
   __DATA_CONST.__got: 0x1b90
-  __DATA_CONST.__const: 0x9340
+  __DATA_CONST.__const: 0x9318
   __DATA_CONST.__objc_classlist: 0x928
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x3f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaec0
+  __DATA_CONST.__objc_selrefs: 0xaee8
   __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x5f0
   __DATA_CONST.__objc_arraydata: 0x658
   __AUTH_CONST.__auth_got: 0x1398
   __AUTH_CONST.__const: 0x5c78
   __AUTH_CONST.__cfstring: 0x10160
-  __AUTH_CONST.__objc_const: 0x21390
+  __AUTH_CONST.__objc_const: 0x213f0
   __AUTH_CONST.__objc_intobj: 0x918
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH.__objc_data: 0xef0
   __AUTH.__data: 0x4f8
-  __DATA.__objc_ivar: 0x1458
+  __DATA.__objc_ivar: 0x1460
   __DATA.__data: 0x35e0
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x4750

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B8C631E8-E63A-3E1B-AC31-42C3FDBCB460
-  Functions: 10657
-  Symbols:   34252
+  UUID: BE4DBC3E-B05E-3188-B6BE-DB95F7ACC05C
+  Functions: 10661
+  Symbols:   34266
   CStrings:  16230
 
Symbols:
+ -[EDMessageQueryHandler _searchResultTypeForMessageObjectID:]
+ -[EDMessageQueryHandler _setSearchResultTypesForMessages:]
+ -[EDMessageQueryHandler messagesForObjectIDs:missedMessageObjectIDs:]
+ -[EDMessageQueryHelper _reportChangesForCurrentlyMatchingMessages:previouslyMatchingMessages:keyPaths:]
+ -[EDMessageQueryHelper _reportChangesForPersistedMessages:withPendingChangesKey:keyPaths:]
+ -[EDMessageRepository _enumerateMessageObjectIDs:queryHandler:usingBlock:]
+ -[_EDMessageQueryHandlerList entriesByObjectID]
+ -[_EDMessageQueryHelperEntry searchResultType]
+ _OBJC_IVAR_$__EDMessageQueryHandlerList._entriesByObjectID
+ _OBJC_IVAR_$__EDMessageQueryHelperEntry._searchResultType
+ ___103-[EDMessageQueryHelper _reportChangesForCurrentlyMatchingMessages:previouslyMatchingMessages:keyPaths:]_block_invoke
+ ___105-[EDMessageQueryHelper _calculateAndReportChangesForPersistedMessages:withPendingChangesKey:changeBlock:]_block_invoke.75
+ ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.404
+ ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.404.cold.1
+ ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.406
+ ___125-[EDMessageRepository performOneTimeCodeMessageDeletionWithObjectID:requestID:returnUndoAction:afterDelay:completionHandler:]_block_invoke.327
+ ___136-[EDMessageRepository messageListItemsForObjectIDs:requestID:observationIdentifier:loadSummaryForAdditionalObjectIDs:completionHandler:]_block_invoke.265
+ ___58-[EDMessageQueryHandler _setSearchResultTypesForMessages:]_block_invoke
+ ___61-[EDMessageQueryHandler _searchResultTypeForMessageObjectID:]_block_invoke
+ ___74-[EDMessageRepository _enumerateMessageObjectIDs:queryHandler:usingBlock:]_block_invoke
+ ___85-[EDMessageQueryHelper _persistenceDidDeleteMessages:includeMessagesWithDeletedFlag:]_block_invoke.63
+ ___block_descriptor_48_ea8_32s40bs_e43_v32?0"EMMessageObjectID"8"NSError"16^B24ls40l8s32l8
+ ___block_literal_global.345
+ ___block_literal_global.354
+ ___block_literal_global.358
+ ___block_literal_global.367
+ ___block_literal_global.371
+ ___block_literal_global.378
+ ___block_literal_global.381
+ ___block_literal_global.390
+ ___block_literal_global.393
+ ___block_literal_global.397
+ ___block_literal_global.440
+ ___block_literal_global.444
+ ___block_literal_global.955
+ _objc_msgSend$_enumerateMessageObjectIDs:queryHandler:usingBlock:
+ _objc_msgSend$_reportChangesForCurrentlyMatchingMessages:previouslyMatchingMessages:keyPaths:
+ _objc_msgSend$_reportChangesForPersistedMessages:withPendingChangesKey:keyPaths:
+ _objc_msgSend$_setSearchResultTypesForMessages:
+ _objc_msgSend$ef_addObjectIfAbsentAccordingToEquals:
+ _objc_msgSend$entriesByObjectID
+ _objc_msgSend$messagesForObjectIDs:missedMessageObjectIDs:
- -[EDMessageQueryHandler _messagesForInitialBatchWithMessagesFromQueryHelper:requestedMessage:].cold.1
- -[EDMessageQueryHandler _messagesForInitialBatchWithMessagesFromQueryHelper:requestedMessage:].cold.2
- -[EDMessageQueryHelper _performBlockAfterGenerationCheck:generation:keyPaths:removedMessages:changedMessages:addedMessages:]
- -[EDMessageQueryHelper _reportChangesForCurrentlyMatchingMessages:previouslyMatchingMessages:keyPaths:generation:]
- -[EDMessageQueryHelper _reportChangesForPersistedMessages:withPendingChangesKey:keyPaths:generation:]
- ___105-[EDMessageQueryHelper _calculateAndReportChangesForPersistedMessages:withPendingChangesKey:changeBlock:]_block_invoke.77
- ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.403
- ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.403.cold.1
- ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.405
- ___114-[EDMessageQueryHelper _reportChangesForCurrentlyMatchingMessages:previouslyMatchingMessages:keyPaths:generation:]_block_invoke
- ___124-[EDMessageQueryHelper _performBlockAfterGenerationCheck:generation:keyPaths:removedMessages:changedMessages:addedMessages:]_block_invoke
- ___124-[EDMessageQueryHelper _performBlockAfterGenerationCheck:generation:keyPaths:removedMessages:changedMessages:addedMessages:]_block_invoke.74
- ___125-[EDMessageRepository performOneTimeCodeMessageDeletionWithObjectID:requestID:returnUndoAction:afterDelay:completionHandler:]_block_invoke.326
- ___136-[EDMessageRepository messageListItemsForObjectIDs:requestID:observationIdentifier:loadSummaryForAdditionalObjectIDs:completionHandler:]_block_invoke.264
- ___85-[EDMessageQueryHelper _persistenceDidDeleteMessages:includeMessagesWithDeletedFlag:]_block_invoke.64
- ___block_descriptor_40_ea8_32r_e8_v16?0q8lr32l8
- ___block_descriptor_88_ea8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s80l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.344
- ___block_literal_global.353
- ___block_literal_global.355
- ___block_literal_global.357
- ___block_literal_global.363
- ___block_literal_global.366
- ___block_literal_global.369
- ___block_literal_global.372
- ___block_literal_global.392
- ___block_literal_global.396
- ___block_literal_global.439
- ___block_literal_global.443
- ___block_literal_global.951
- _objc_msgSend$_performBlockAfterGenerationCheck:generation:keyPaths:removedMessages:changedMessages:addedMessages:
- _objc_msgSend$_reportChangesForCurrentlyMatchingMessages:previouslyMatchingMessages:keyPaths:generation:
- _objc_msgSend$_reportChangesForPersistedMessages:withPendingChangesKey:keyPaths:generation:
CStrings:
+ "T@\"NSMutableDictionary\",R,N,V_entriesByObjectID"
+ "_entriesByObjectID"
+ "_enumerateMessageObjectIDs:queryHandler:usingBlock:"
+ "_reportChangesForCurrentlyMatchingMessages:previouslyMatchingMessages:keyPaths:"
+ "_reportChangesForPersistedMessages:withPendingChangesKey:keyPaths:"
+ "_searchResultTypeForMessageObjectID:"
+ "_setSearchResultTypesForMessages:"
+ "ef_addObjectIfAbsentAccordingToEquals:"
+ "entriesByObjectID"
+ "messagesForObjectIDs:missedMessageObjectIDs:"
+ "v32@?0@\"EMMessageObjectID\"8@\"NSError\"16^B24"
- "%p: %{public}@ - rescheduling changes for keyPaths:%{public}@ removed=%lu added=%lu changed=%lu after %.3f due to generation %lld not being higher than generation window of the change %lld"
- "Failed to fetch requested message: %{public}@"
- "Found requested message in initial batch: objectID=%{public}@"
- "Looking for requested message with objectID: %{public}@"
- "MISMATCH: Requested objectID %{public}@ but found message with objectID %{public}@"
- "Requested message not in initial batch, fetching separately: %{public}@"
- "Successfully fetched requested message: %{public}@"
- "_performBlockAfterGenerationCheck:generation:keyPaths:removedMessages:changedMessages:addedMessages:"
- "_reportChangesForCurrentlyMatchingMessages:previouslyMatchingMessages:keyPaths:generation:"
- "_reportChangesForPersistedMessages:withPendingChangesKey:keyPaths:generation:"
- "v64@0:8@?16@24@32@40@48@56"

```
