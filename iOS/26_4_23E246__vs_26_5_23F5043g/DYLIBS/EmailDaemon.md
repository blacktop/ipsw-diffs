## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3864.500.181.2.2
-  __TEXT.__text: 0x27f188
+3864.600.1.2.3
+  __TEXT.__text: 0x2802a8
   __TEXT.__auth_stubs: 0x2750
-  __TEXT.__objc_methlist: 0x1308c
+  __TEXT.__objc_methlist: 0x130fc
   __TEXT.__const: 0x3a2c
-  __TEXT.__gcc_except_tab: 0x4ecb8
-  __TEXT.__cstring: 0x26bba
+  __TEXT.__gcc_except_tab: 0x4eeec
+  __TEXT.__cstring: 0x26c4a
   __TEXT.__oslogstring: 0x1a8c4
   __TEXT.__dlopen_cstrs: 0x3bc
   __TEXT.__ustring: 0x22

   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x10e58
+  __TEXT.__unwind_info: 0x10f10
   __TEXT.__eh_frame: 0xcf8
-  __TEXT.__objc_classname: 0x3135
-  __TEXT.__objc_methname: 0x37be9
-  __TEXT.__objc_methtype: 0x7b87
-  __TEXT.__objc_stubs: 0x257c0
-  __DATA_CONST.__got: 0x1c58
-  __DATA_CONST.__const: 0x9390
-  __DATA_CONST.__objc_classlist: 0x968
+  __TEXT.__objc_classname: 0x3145
+  __TEXT.__objc_methname: 0x37ca9
+  __TEXT.__objc_methtype: 0x7bc7
+  __TEXT.__objc_stubs: 0x25800
+  __DATA_CONST.__got: 0x1c60
+  __DATA_CONST.__const: 0x9450
+  __DATA_CONST.__objc_classlist: 0x970
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x3f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf38
+  __DATA_CONST.__objc_selrefs: 0xaf50
   __DATA_CONST.__objc_protorefs: 0xf0
-  __DATA_CONST.__objc_superrefs: 0x5f8
+  __DATA_CONST.__objc_superrefs: 0x600
   __DATA_CONST.__objc_arraydata: 0x658
   __AUTH_CONST.__auth_got: 0x13b8
   __AUTH_CONST.__const: 0x5ea3
-  __AUTH_CONST.__cfstring: 0x10000
-  __AUTH_CONST.__objc_const: 0x21ad8
+  __AUTH_CONST.__cfstring: 0x10060
+  __AUTH_CONST.__objc_const: 0x21b98
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH.__objc_data: 0x1128
+  __AUTH.__objc_data: 0x1178
   __AUTH.__data: 0x580
-  __DATA.__objc_ivar: 0x1474
+  __DATA.__objc_ivar: 0x1478
   __DATA.__data: 0x3608
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x4620

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 918E5579-721E-38DF-9E7E-40C48BCC15FC
-  Functions: 10742
-  Symbols:   34729
-  CStrings:  16295
+  UUID: 59FC3F82-F529-3C4C-B084-1C55BDE57CE3
+  Functions: 10758
+  Symbols:   34790
+  CStrings:  16309
 
Symbols:
+ -[EDInMemoryThread _removeMessages:andChangeMessages:threadIsEmpty:]
+ -[EDInMemoryThread setState:]
+ -[EDInMemoryThread state]
+ -[_EDInMemoryThreadState .cxx_destruct]
+ -[_EDInMemoryThreadState _addMessages:withComparator:]
+ -[_EDInMemoryThreadState _changeMessages:]
+ -[_EDInMemoryThreadState _combinedCCList]
+ -[_EDInMemoryThreadState _combinedFlagColors]
+ -[_EDInMemoryThreadState _combinedFlagColors].cold.1
+ -[_EDInMemoryThreadState _combinedFlags]
+ -[_EDInMemoryThreadState _combinedHasAttachments]
+ -[_EDInMemoryThreadState _combinedHasUnflagged]
+ -[_EDInMemoryThreadState _combinedIsBlocked]
+ -[_EDInMemoryThreadState _combinedIsVIP]
+ -[_EDInMemoryThreadState _combinedMailboxes]
+ -[_EDInMemoryThreadState _combinedReadLater]
+ -[_EDInMemoryThreadState _combinedSenderListWithDisplayMessage:]
+ -[_EDInMemoryThreadState _combinedToList]
+ -[_EDInMemoryThreadState _displayMessage]
+ -[_EDInMemoryThreadState _maxSearchRelevanceScore]
+ -[_EDInMemoryThreadState _newestDisplayDate]
+ -[_EDInMemoryThreadState _newestMessage]
+ -[_EDInMemoryThreadState _oldestMessage]
+ -[_EDInMemoryThreadState _removeMessages:]
+ -[_EDInMemoryThreadState _updateThreadWithOriginatingQuery:]
+ -[_EDInMemoryThreadState addMessages:withComparator:originatingQuery:]
+ -[_EDInMemoryThreadState initWithMessages:objectID:originatingQuery:]
+ -[_EDInMemoryThreadState messages]
+ -[_EDInMemoryThreadState objectID]
+ -[_EDInMemoryThreadState removeMessages:andChangeMessages:originatingQuery:threadIsEmpty:]
+ -[_EDInMemoryThreadState setMessages:]
+ -[_EDInMemoryThreadState setObjectID:]
+ -[_EDInMemoryThreadState setThread:]
+ -[_EDInMemoryThreadState thread]
+ -[_EDInMemoryThreadState updateMessage:fromOldObjectID:withComparator:originatingQuery:]
+ GCC_except_table286
+ GCC_except_table292
+ GCC_except_table294
+ GCC_except_table307
+ GCC_except_table313
+ GCC_except_table320
+ GCC_except_table329
+ _OBJC_CLASS_$__EDInMemoryThreadState
+ _OBJC_IVAR_$_EDInMemoryThread._state
+ _OBJC_IVAR_$__EDInMemoryThreadState._messages
+ _OBJC_IVAR_$__EDInMemoryThreadState._objectID
+ _OBJC_IVAR_$__EDInMemoryThreadState._thread
+ _OBJC_METACLASS_$__EDInMemoryThreadState
+ __OBJC_$_INSTANCE_METHODS__EDInMemoryThreadState
+ __OBJC_$_INSTANCE_VARIABLES__EDInMemoryThreadState
+ __OBJC_$_PROP_LIST__EDInMemoryThreadState
+ __OBJC_CLASS_RO_$__EDInMemoryThreadState
+ __OBJC_METACLASS_RO_$__EDInMemoryThreadState
+ ___115-[EDMessagePersistence _iteratePersistedMessagesMatchingQuery:limit:cancelationToken:requireProtectedData:handler:]_block_invoke.512
+ ___26-[EDInMemoryThread thread]_block_invoke
+ ___28-[EDInMemoryThread messages]_block_invoke
+ ___32-[EDInMemoryThread addMessages:]_block_invoke_2
+ ___41-[_EDInMemoryThreadState _displayMessage]_block_invoke
+ ___45-[_EDInMemoryThreadState _combinedFlagColors]_block_invoke
+ ___46-[EDMessagePersistence setGeneratedSummaries:]_block_invoke.768
+ ___46-[EDMessagePersistence setGeneratedSummaries:]_block_invoke_2.772
+ ___50-[_EDInMemoryThreadState _maxSearchRelevanceScore]_block_invoke
+ ___60-[_EDInMemoryThreadState _updateThreadWithOriginatingQuery:]_block_invoke
+ ___60-[_EDInMemoryThreadState _updateThreadWithOriginatingQuery:]_block_invoke.cold.1
+ ___60-[_EDInMemoryThreadState _updateThreadWithOriginatingQuery:]_block_invoke_2
+ ___67-[EDMessagePersistence _checkCachedMetadataRowLimitWithConnection:]_block_invoke.641
+ ___68-[EDInMemoryThread _removeMessages:andChangeMessages:threadIsEmpty:]_block_invoke
+ ___70-[EDMessagePersistence _setCachedMetadataJSON:forKey:globalMessageID:]_block_invoke.628
+ ___76-[EDMessagePersistence messageObjectIDCriterionExpressionForPredicateValue:]_block_invoke.457
+ ___82-[EDMessagePersistence persistedMessagesMatchingQuery:limit:requireProtectedData:]_block_invoke.510
+ ___85+[EDMessagePersistence addStandardKeyPathMappersToDictionary:schema:protectedSchema:]_block_invoke_8
+ ___85-[EDMessagePersistence _iterateMessagesMatchingQuery:limit:cancelationToken:handler:]_block_invoke.474
+ ___88-[_EDInMemoryThreadState updateMessage:fromOldObjectID:withComparator:originatingQuery:]_block_invoke
+ ___89-[EDMessagePersistence updateDisplayDateForPersistedMessages:displayDate:changeIsRemote:]_block_invoke.755
+ ___block_descriptor_40_ea8_32r_e32_v16?0"_EDInMemoryThreadState"8lr32l8
+ ___block_descriptor_48_e61_"<EFSQLValueExpressable>"24?0"<EFSQLValueExpressable>"8Q16l
+ ___block_descriptor_64_ea8_32s40s48bs56r_e32_v16?0"_EDInMemoryThreadState"8lr56l8s32l8s48l8s40l8
+ ___block_descriptor_72_ea8_32s40s48s56bs64r_e32_v16?0"_EDInMemoryThreadState"8lr64l8s32l8s40l8s56l8s48l8
+ ___block_descriptor_72_ea8_32s40s48s56r64r_e32_v16?0"_EDInMemoryThreadState"8lr56l8s32l8s40l8s48l8r64l8
+ ___block_descriptor_72_ea8_32s40s48s56s64bs_e26_v32?0"EMMessage"8Q16^B24ls32l8s40l8s48l8s64l8s56l8
+ ___block_literal_global.120
+ ___block_literal_global.131
+ ___block_literal_global.373
+ ___block_literal_global.375
+ ___block_literal_global.460
+ ___block_literal_global.528
+ ___block_literal_global.531
+ ___block_literal_global.553
+ ___block_literal_global.559
+ ___block_literal_global.577
+ ___block_literal_global.580
+ ___block_literal_global.589
+ ___block_literal_global.592
+ ___block_literal_global.595
+ ___block_literal_global.624
+ ___block_literal_global.630
+ ___block_literal_global.643
+ ___block_literal_global.649
+ ___block_literal_global.694
+ ___block_literal_global.724
+ ___block_literal_global.732
+ ___block_literal_global.738
+ ___block_literal_global.740
+ ___block_literal_global.748
+ ___block_literal_global.758
+ ___block_literal_global.764
+ ___block_literal_global.771
+ ___block_literal_global.778
+ _objc_msgSend$_addMessages:withComparator:
+ _objc_msgSend$_changeMessages:
+ _objc_msgSend$_combinedSenderListWithDisplayMessage:
+ _objc_msgSend$_displayMessage
+ _objc_msgSend$_newestMessage
+ _objc_msgSend$_removeMessages:
+ _objc_msgSend$_removeMessages:andChangeMessages:threadIsEmpty:
+ _objc_msgSend$_updateThreadWithOriginatingQuery:
+ _objc_msgSend$addMessages:withComparator:originatingQuery:
+ _objc_msgSend$initWithMessages:objectID:originatingQuery:
+ _objc_msgSend$removeMessages:andChangeMessages:originatingQuery:threadIsEmpty:
+ _objc_msgSend$updateMessage:fromOldObjectID:withComparator:originatingQuery:
- +[EDMessageListItemPredicates expandedPredicateForReadLaterIsActivePredicate:]
- -[EDInMemoryThread _addMessagesToThread:]
- -[EDInMemoryThread _calculateAndApplyChange]
- -[EDInMemoryThread _calculateChangesAfterRemovingMessages:applyingChanges:threadIsEmpty:]
- -[EDInMemoryThread _combinedCCList]
- -[EDInMemoryThread _combinedFlagColors]
- -[EDInMemoryThread _combinedFlagColors].cold.1
- -[EDInMemoryThread _combinedFlags]
- -[EDInMemoryThread _combinedHasAttachments]
- -[EDInMemoryThread _combinedHasUnflagged]
- -[EDInMemoryThread _combinedIsBlocked]
- -[EDInMemoryThread _combinedIsVIP]
- -[EDInMemoryThread _combinedMailboxes]
- -[EDInMemoryThread _combinedReadLater]
- -[EDInMemoryThread _combinedSenderList]
- -[EDInMemoryThread _combinedToList]
- -[EDInMemoryThread _createThreadWithObjectID:]
- -[EDInMemoryThread _isSortedByDate:]
- -[EDInMemoryThread _maxSearchRelevanceScore]
- -[EDInMemoryThread _newestDisplayDate]
- -[EDInMemoryThread _recalculateDisplayMessage]
- -[EDInMemoryThread displayMessage]
- -[EDInMemoryThread messageListItem]
- -[EDInMemoryThread newestMessage]
- -[EDInMemoryThread oldestMessage]
- -[EDInMemoryThread setDisplayMessage:]
- -[EDInMemoryThread setThread:]
- GCC_except_table287
- GCC_except_table293
- GCC_except_table295
- GCC_except_table308
- GCC_except_table314
- GCC_except_table321
- _OBJC_IVAR_$_EDInMemoryThread._displayMessage
- _OBJC_IVAR_$_EDInMemoryThread._messages
- _OBJC_IVAR_$_EDInMemoryThread._thread
- ___115-[EDMessagePersistence _iteratePersistedMessagesMatchingQuery:limit:cancelationToken:requireProtectedData:handler:]_block_invoke.507
- ___39-[EDInMemoryThread _combinedFlagColors]_block_invoke
- ___44-[EDInMemoryThread _maxSearchRelevanceScore]_block_invoke
- ___46-[EDInMemoryThread _createThreadWithObjectID:]_block_invoke
- ___46-[EDInMemoryThread _createThreadWithObjectID:]_block_invoke.cold.1
- ___46-[EDInMemoryThread _createThreadWithObjectID:]_block_invoke_2
- ___46-[EDInMemoryThread _recalculateDisplayMessage]_block_invoke
- ___46-[EDMessagePersistence setGeneratedSummaries:]_block_invoke.764
- ___46-[EDMessagePersistence setGeneratedSummaries:]_block_invoke_2.768
- ___67-[EDMessagePersistence _checkCachedMetadataRowLimitWithConnection:]_block_invoke.636
- ___70-[EDMessagePersistence _setCachedMetadataJSON:forKey:globalMessageID:]_block_invoke.623
- ___76-[EDMessagePersistence messageObjectIDCriterionExpressionForPredicateValue:]_block_invoke.452
- ___82-[EDMessagePersistence persistedMessagesMatchingQuery:limit:requireProtectedData:]_block_invoke.505
- ___85-[EDMessagePersistence _iterateMessagesMatchingQuery:limit:cancelationToken:handler:]_block_invoke.469
- ___89-[EDMessagePersistence updateDisplayDateForPersistedMessages:displayDate:changeIsRemote:]_block_invoke.751
- ___block_descriptor_56_ea8_32s40s48s_e26_v32?0"EMMessage"8Q16^B24ls32l8s40l8s48l8
- ___block_literal_global.21
- ___block_literal_global.368
- ___block_literal_global.455
- ___block_literal_global.523
- ___block_literal_global.526
- ___block_literal_global.548
- ___block_literal_global.554
- ___block_literal_global.570
- ___block_literal_global.572
- ___block_literal_global.584
- ___block_literal_global.587
- ___block_literal_global.590
- ___block_literal_global.619
- ___block_literal_global.625
- ___block_literal_global.638
- ___block_literal_global.644
- ___block_literal_global.689
- ___block_literal_global.719
- ___block_literal_global.722
- ___block_literal_global.733
- ___block_literal_global.735
- ___block_literal_global.743
- ___block_literal_global.746
- ___block_literal_global.760
- ___block_literal_global.763
- ___block_literal_global.774
- ___block_literal_global.9
- _objc_msgSend$_addMessagesToThread:
- _objc_msgSend$_calculateAndApplyChange
- _objc_msgSend$_calculateChangesAfterRemovingMessages:applyingChanges:threadIsEmpty:
- _objc_msgSend$_combinedSenderList
- _objc_msgSend$_createThreadWithObjectID:
- _objc_msgSend$_recalculateDisplayMessage
- _objc_msgSend$displayMessage
- _objc_msgSend$expandedPredicateForReadLaterIsActivePredicate:
- _objc_msgSend$messageListItem
- _objc_msgSend$setDisplayMessage:
CStrings:
+ "@40@0:8@16@?24@32"
+ "@48@0:8@16@24@32^B40"
+ "@48@0:8@16@24@?32@40"
+ "Display message for in-memory thread must be nonnull"
+ "EDInMemoryThread.m"
+ "Newest message for in-memory thread must be nonnull"
+ "T@\"EFLocked\",&,N,V_state"
+ "T@\"EMThreadObjectID\",&,N,V_objectID"
+ "T@\"NSMutableArray\",&,N,V_messages"
+ "_EDInMemoryThreadState"
+ "_addMessages:withComparator:"
+ "_changeMessages:"
+ "_combinedSenderListWithDisplayMessage:"
+ "_newestMessage"
+ "_oldestMessage"
+ "_removeMessages:"
+ "_removeMessages:andChangeMessages:threadIsEmpty:"
+ "_updateThreadWithOriginatingQuery:"
+ "addMessages:withComparator:originatingQuery:"
+ "initWithMessages:objectID:originatingQuery:"
+ "removeMessages:andChangeMessages:originatingQuery:threadIsEmpty:"
+ "setObjectID:"
+ "updateMessage:fromOldObjectID:withComparator:originatingQuery:"
+ "v16@?0@\"_EDInMemoryThreadState\"8"
- "T@\"<EMMessageListItem>\",R,N"
- "T@\"EMMessage\",&,N,V_displayMessage"
- "_addMessagesToThread:"
- "_calculateAndApplyChange"
- "_calculateChangesAfterRemovingMessages:applyingChanges:threadIsEmpty:"
- "_combinedSenderList"
- "_createThreadWithObjectID:"
- "_isSortedByDate:"
- "_recalculateDisplayMessage"
- "expandedPredicateForReadLaterIsActivePredicate:"
- "messageListItem"
- "oldestMessage"
- "setDisplayMessage:"

```
