## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3856.100.4.0.0
-  __TEXT.__text: 0x26c384
+3858.100.10.2.1
+  __TEXT.__text: 0x26ce24
   __TEXT.__auth_stubs: 0x27b0
-  __TEXT.__objc_methlist: 0x162ac
+  __TEXT.__objc_methlist: 0x162e4
   __TEXT.__const: 0x1f1c
-  __TEXT.__gcc_except_tab: 0x500b0
-  __TEXT.__cstring: 0x22b47
-  __TEXT.__oslogstring: 0x19c34
+  __TEXT.__gcc_except_tab: 0x501b8
+  __TEXT.__cstring: 0x22b97
+  __TEXT.__oslogstring: 0x19d94
   __TEXT.__dlopen_cstrs: 0x478
   __TEXT.__ustring: 0x2c
   __TEXT.__constg_swiftt: 0x7c8

   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_proto: 0x154
   __TEXT.__swift5_types: 0xc8
-  __TEXT.__swift5_capture: 0x194
+  __TEXT.__swift5_capture: 0x1a4
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x10d10
-  __TEXT.__eh_frame: 0xc98
+  __TEXT.__unwind_info: 0x10d88
+  __TEXT.__eh_frame: 0xcc0
   __TEXT.__objc_classname: 0x2fae
-  __TEXT.__objc_methname: 0x3abd7
+  __TEXT.__objc_methname: 0x3ac8c
   __TEXT.__objc_methtype: 0x8851
-  __TEXT.__objc_stubs: 0x26040
-  __DATA_CONST.__got: 0x1c20
+  __TEXT.__objc_stubs: 0x260c0
+  __DATA_CONST.__got: 0x1c40
   __DATA_CONST.__const: 0x96e8
   __DATA_CONST.__objc_classlist: 0x9d8
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x410
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbdc0
+  __DATA_CONST.__objc_selrefs: 0xbde8
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x6d0
   __DATA_CONST.__objc_arraydata: 0x680
   __AUTH_CONST.__auth_got: 0x13e8
-  __AUTH_CONST.__const: 0x41b8
-  __AUTH_CONST.__cfstring: 0x11600
-  __AUTH_CONST.__objc_const: 0x25940
+  __AUTH_CONST.__const: 0x4200
+  __AUTH_CONST.__cfstring: 0x11660
+  __AUTH_CONST.__objc_const: 0x25990
   __AUTH_CONST.__objc_intobj: 0x978
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH.__objc_data: 0xd80
   __AUTH.__data: 0x3e8
-  __DATA.__objc_ivar: 0x1768
+  __DATA.__objc_ivar: 0x176c
   __DATA.__data: 0x3460
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x25f0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x5788
   __DATA_DIRTY.__data: 0xab0
-  __DATA_DIRTY.__bss: 0x13f8
+  __DATA_DIRTY.__bss: 0x1408
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 81225D00-9BBE-3050-BA99-59AEE9A7A371
-  Functions: 10875
-  Symbols:   36910
-  CStrings:  17054
+  UUID: A5B923EE-DD0A-32A5-A8DC-25C0CA53C937
+  Functions: 10885
+  Symbols:   36940
+  CStrings:  17072
 
Symbols:
+ +[EDInMemoryThreadQueryHandler signpostLog]
+ +[EDSearchableIndexExpressionGenerator expressionForPredicate:suggestion:bundleID:nonSpotlightPredicates:]
+ -[EDInMemoryThreadQueryHandler signpostID]
+ -[EDMessagePersistence _queryHasConversationIDPredicate:]
+ -[EDMessageQueryHelper isSearchCanceled]
+ -[EDPersistence reportWorkloadToDAS]
+ -[EDPersistence reportWorkloadToDAS].cold.1
+ GCC_except_table189
+ GCC_except_table284
+ GCC_except_table300
+ GCC_except_table307
+ GCC_except_table315
+ GCC_except_table316
+ _MDItemBundleID
+ _MDItemEventSourceBundleIdentifier
+ _OBJC_CLASS_$_BGSystemTaskWorkload
+ _OBJC_IVAR_$_EDInMemoryThreadQueryHandler._helperCount
+ __OBJC_$_PROP_LIST_EDLocalSearchDelegate
+ ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.404
+ ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.404.cold.1
+ ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.406
+ ___125-[EDMessageRepository performOneTimeCodeMessageDeletionWithObjectID:requestID:returnUndoAction:afterDelay:completionHandler:]_block_invoke.326
+ ___136-[EDMessageRepository messageListItemsForObjectIDs:requestID:observationIdentifier:loadSummaryForAdditionalObjectIDs:completionHandler:]_block_invoke.264
+ ___43+[EDInMemoryThreadQueryHandler signpostLog]_block_invoke
+ ___46-[EDMessagePersistence setGeneratedSummaries:]_block_invoke.743
+ ___46-[EDMessagePersistence setGeneratedSummaries:]_block_invoke_2.747
+ ___57-[EDMessagePersistence _queryHasConversationIDPredicate:]_block_invoke
+ ___59-[EDInMemoryThreadQueryHandler didSendUpdatesInCollection:]_block_invoke.51
+ ___67-[EDMessagePersistence _checkCachedMetadataRowLimitWithConnection:]_block_invoke.624
+ ___67-[EDMessageRepository startObservingOneTimeCode:completionHandler:]_block_invoke.241
+ ___70-[EDMessagePersistence _setCachedMetadataJSON:forKey:globalMessageID:]_block_invoke.611
+ ___89-[EDMessagePersistence updateDisplayDateForPersistedMessages:displayDate:changeIsRemote:]_block_invoke.730
+ ___block_descriptor_64_ea8_32s40bs48w56w_e17_v16?0"NSArray"8lw48l8w56l8s32l8s40l8
+ ___block_descriptor_64_ea8_32s40s48r56r_e33_v32?0"CSSearchableItem"8Q16^B24lr48l8s32l8r56l8s40l8
+ ___block_descriptor_64_ea8_32s40s48s56w_e17_v16?0"NSArray"8lw56l8s32l8s40l8s48l8
+ ___block_descriptor_72_ea8_32s40s48s56s64w_e41_v16?0"<EMSearchableIndexQueryBuilder>"8ls32l8w64l8s40l8s48l8s56l8
+ ___block_literal_global.104
+ ___block_literal_global.344
+ ___block_literal_global.353
+ ___block_literal_global.357
+ ___block_literal_global.366
+ ___block_literal_global.370
+ ___block_literal_global.392
+ ___block_literal_global.396
+ ___block_literal_global.440
+ ___block_literal_global.444
+ ___block_literal_global.514
+ ___block_literal_global.536
+ ___block_literal_global.542
+ ___block_literal_global.558
+ ___block_literal_global.563
+ ___block_literal_global.578
+ ___block_literal_global.607
+ ___block_literal_global.613
+ ___block_literal_global.626
+ ___block_literal_global.64
+ ___block_literal_global.674
+ ___block_literal_global.704
+ ___block_literal_global.706
+ ___block_literal_global.712
+ ___block_literal_global.714
+ ___block_literal_global.725
+ ___block_literal_global.729
+ ___block_literal_global.733
+ ___block_literal_global.742
+ ___block_literal_global.746
+ ___block_literal_global.753
+ ___block_literal_global.94
+ ___block_literal_global.948
+ ___block_literal_global.950
+ _block_copy_helper.35
+ _block_copy_helper.41
+ _block_descriptor.37
+ _block_descriptor.43
+ _block_destroy_helper.36
+ _block_destroy_helper.42
+ _objc_msgSend$_queryHasConversationIDPredicate:
+ _objc_msgSend$expressionForPredicate:suggestion:bundleID:nonSpotlightPredicates:
+ _objc_msgSend$isPredicateForMessagesInConversations:conversationIDs:
+ _objc_msgSend$isSearchCanceled
+ _objc_msgSend$reportSystemWorkload:ofCategory:error:
+ _objc_msgSend$syntheticDataTaskWithRequest:failOpen:background:completionHandler:
+ _objectdestroy.33Tm
- +[EDSearchableIndexExpressionGenerator expressionForPredicate:suggestion:nonSpotlightPredicates:]
- -[EDInMemoryThreadQueryHandler _createHelper].cold.1
- GCC_except_table288
- GCC_except_table302
- GCC_except_table309
- ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.401
- ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.401.cold.1
- ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.403
- ___125-[EDMessageRepository performOneTimeCodeMessageDeletionWithObjectID:requestID:returnUndoAction:afterDelay:completionHandler:]_block_invoke.323
- ___136-[EDMessageRepository messageListItemsForObjectIDs:requestID:observationIdentifier:loadSummaryForAdditionalObjectIDs:completionHandler:]_block_invoke.261
- ___46-[EDMessagePersistence setGeneratedSummaries:]_block_invoke.740
- ___46-[EDMessagePersistence setGeneratedSummaries:]_block_invoke_2.744
- ___59-[EDInMemoryThreadQueryHandler didSendUpdatesInCollection:]_block_invoke.49
- ___67-[EDMessagePersistence _checkCachedMetadataRowLimitWithConnection:]_block_invoke.621
- ___67-[EDMessageRepository startObservingOneTimeCode:completionHandler:]_block_invoke.238
- ___70-[EDMessagePersistence _setCachedMetadataJSON:forKey:globalMessageID:]_block_invoke.608
- ___89-[EDMessagePersistence updateDisplayDateForPersistedMessages:displayDate:changeIsRemote:]_block_invoke.727
- ___block_descriptor_56_ea8_32s40r48r_e33_v32?0"CSSearchableItem"8Q16^B24lr40l8s32l8r48l8
- ___block_descriptor_64_ea8_32s40s48bs56w_e17_v16?0"NSArray"8lw56l8s32l8s40l8s48l8
- ___block_descriptor_64_ea8_32s40s48s56s_e17_v16?0"NSArray"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_ea8_32s40s48s56s64s_e41_v16?0"<EMSearchableIndexQueryBuilder>"8ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.341
- ___block_literal_global.350
- ___block_literal_global.352
- ___block_literal_global.354
- ___block_literal_global.360
- ___block_literal_global.386
- ___block_literal_global.393
- ___block_literal_global.437
- ___block_literal_global.441
- ___block_literal_global.533
- ___block_literal_global.539
- ___block_literal_global.555
- ___block_literal_global.557
- ___block_literal_global.569
- ___block_literal_global.604
- ___block_literal_global.610
- ___block_literal_global.623
- ___block_literal_global.671
- ___block_literal_global.701
- ___block_literal_global.703
- ___block_literal_global.709
- ___block_literal_global.711
- ___block_literal_global.719
- ___block_literal_global.726
- ___block_literal_global.730
- ___block_literal_global.736
- ___block_literal_global.743
- ___block_literal_global.750
- ___block_literal_global.945
- ___block_literal_global.947
- _block_copy_helper.30
- _block_copy_helper.36
- _block_descriptor.32
- _block_descriptor.38
- _block_destroy_helper.31
- _block_destroy_helper.37
- _objc_msgSend$dataTaskWithRequest:isSynthetic:allowProxying:failOpen:completionHandler:
- _objc_msgSend$expressionForPredicate:suggestion:nonSpotlightPredicates:
- _objectdestroy.28Tm
CStrings:
+ "%@ == '%@'"
+ "%@ == 'com.apple.spotlight.events'"
+ "%p: Created helper #%lu: %p"
+ "%p: Created helper #%lu: %p, Threads Query: %@, Message Query: %@"
+ "EDInMemoryThreadQueryHandlerMessgeQueryHelper"
+ "Failed to report # of emails to DAS: %@"
+ "Reported %@ emails to DAS"
+ "Spotlight live search found Canceled for query %{public}@"
+ "Spotlight live search found Canceled for query %{public}@ message count:%lu"
+ "Spotlight top hits found Canceled for query %{public}@"
+ "_helperCount"
+ "_queryHasConversationIDPredicate:"
+ "counting query token"
+ "expressionForPredicate:suggestion:bundleID:nonSpotlightPredicates:"
+ "isPredicateForMessagesInConversations:conversationIDs:"
+ "isSearchCanceled"
+ "reportSystemWorkload:ofCategory:error:"
+ "reportWorkloadToDAS"
+ "syntheticDataTaskWithRequest:failOpen:background:completionHandler:"
- "%p: Message Query: %@"
- "%p: Threads Query: %@"
- "dataTaskWithRequest:isSynthetic:allowProxying:failOpen:completionHandler:"
- "expressionForPredicate:suggestion:nonSpotlightPredicates:"

```
