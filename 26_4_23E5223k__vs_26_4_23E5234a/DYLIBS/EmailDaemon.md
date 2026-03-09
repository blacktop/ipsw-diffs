## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3864.500.172.0.0
-  __TEXT.__text: 0x2801a8
+3864.500.181.2.2
+  __TEXT.__text: 0x27f188
   __TEXT.__auth_stubs: 0x2750
-  __TEXT.__objc_methlist: 0x130f4
+  __TEXT.__objc_methlist: 0x1308c
   __TEXT.__const: 0x3a2c
-  __TEXT.__gcc_except_tab: 0x4eeb4
-  __TEXT.__cstring: 0x26c4a
+  __TEXT.__gcc_except_tab: 0x4ecb8
+  __TEXT.__cstring: 0x26bba
   __TEXT.__oslogstring: 0x1a8c4
   __TEXT.__dlopen_cstrs: 0x3bc
   __TEXT.__ustring: 0x22

   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x10f10
+  __TEXT.__unwind_info: 0x10e58
   __TEXT.__eh_frame: 0xcf8
-  __TEXT.__objc_classname: 0x3145
-  __TEXT.__objc_methname: 0x37cd9
-  __TEXT.__objc_methtype: 0x7bc7
-  __TEXT.__objc_stubs: 0x25840
-  __DATA_CONST.__got: 0x1c60
-  __DATA_CONST.__const: 0x9430
-  __DATA_CONST.__objc_classlist: 0x970
+  __TEXT.__objc_classname: 0x3135
+  __TEXT.__objc_methname: 0x37be9
+  __TEXT.__objc_methtype: 0x7b87
+  __TEXT.__objc_stubs: 0x257c0
+  __DATA_CONST.__got: 0x1c58
+  __DATA_CONST.__const: 0x9390
+  __DATA_CONST.__objc_classlist: 0x968
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x3f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf58
+  __DATA_CONST.__objc_selrefs: 0xaf38
   __DATA_CONST.__objc_protorefs: 0xf0
-  __DATA_CONST.__objc_superrefs: 0x600
+  __DATA_CONST.__objc_superrefs: 0x5f8
   __DATA_CONST.__objc_arraydata: 0x658
   __AUTH_CONST.__auth_got: 0x13b8
   __AUTH_CONST.__const: 0x5ea3
-  __AUTH_CONST.__cfstring: 0x10060
-  __AUTH_CONST.__objc_const: 0x21b68
+  __AUTH_CONST.__cfstring: 0x10000
+  __AUTH_CONST.__objc_const: 0x21ad8
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH.__objc_data: 0x1178
+  __AUTH.__objc_data: 0x1128
   __AUTH.__data: 0x580
   __DATA.__objc_ivar: 0x1474
   __DATA.__data: 0x3608

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DD020371-5AD0-312B-A315-8E49EA823A88
-  Functions: 10757
-  Symbols:   34789
-  CStrings:  16309
+  UUID: 918E5579-721E-38DF-9E7E-40C48BCC15FC
+  Functions: 10742
+  Symbols:   34729
+  CStrings:  16295
 
Symbols:
+ -[EDInMemoryThread _addMessagesToThread:]
+ -[EDInMemoryThread _calculateAndApplyChange]
+ -[EDInMemoryThread _calculateChangesAfterRemovingMessages:applyingChanges:threadIsEmpty:]
+ -[EDInMemoryThread _combinedCCList]
+ -[EDInMemoryThread _combinedFlagColors]
+ -[EDInMemoryThread _combinedFlagColors].cold.1
+ -[EDInMemoryThread _combinedFlags]
+ -[EDInMemoryThread _combinedHasAttachments]
+ -[EDInMemoryThread _combinedHasUnflagged]
+ -[EDInMemoryThread _combinedIsBlocked]
+ -[EDInMemoryThread _combinedIsVIP]
+ -[EDInMemoryThread _combinedMailboxes]
+ -[EDInMemoryThread _combinedReadLater]
+ -[EDInMemoryThread _combinedSenderList]
+ -[EDInMemoryThread _combinedToList]
+ -[EDInMemoryThread _createThreadWithObjectID:]
+ -[EDInMemoryThread _isSortedByDate:]
+ -[EDInMemoryThread _maxSearchRelevanceScore]
+ -[EDInMemoryThread _newestDisplayDate]
+ -[EDInMemoryThread _recalculateDisplayMessage]
+ -[EDInMemoryThread displayMessage]
+ -[EDInMemoryThread messageListItem]
+ -[EDInMemoryThread newestMessage]
+ -[EDInMemoryThread oldestMessage]
+ -[EDInMemoryThread setDisplayMessage:]
+ -[EDInMemoryThread setThread:]
+ _OBJC_IVAR_$_EDInMemoryThread._displayMessage
+ _OBJC_IVAR_$_EDInMemoryThread._messages
+ _OBJC_IVAR_$_EDInMemoryThread._thread
+ ___39-[EDInMemoryThread _combinedFlagColors]_block_invoke
+ ___44-[EDInMemoryThread _maxSearchRelevanceScore]_block_invoke
+ ___46-[EDInMemoryThread _createThreadWithObjectID:]_block_invoke
+ ___46-[EDInMemoryThread _createThreadWithObjectID:]_block_invoke.cold.1
+ ___46-[EDInMemoryThread _createThreadWithObjectID:]_block_invoke_2
+ ___46-[EDInMemoryThread _recalculateDisplayMessage]_block_invoke
+ ___block_descriptor_56_ea8_32s40s48s_e26_v32?0"EMMessage"8Q16^B24ls32l8s40l8s48l8
+ ___block_literal_global.21
+ ___block_literal_global.9
+ _objc_msgSend$_addMessagesToThread:
+ _objc_msgSend$_calculateAndApplyChange
+ _objc_msgSend$_calculateChangesAfterRemovingMessages:applyingChanges:threadIsEmpty:
+ _objc_msgSend$_combinedSenderList
+ _objc_msgSend$_createThreadWithObjectID:
+ _objc_msgSend$_recalculateDisplayMessage
+ _objc_msgSend$displayMessage
+ _objc_msgSend$messageListItem
+ _objc_msgSend$setDisplayMessage:
- -[EDInMemoryThread _removeMessages:andChangeMessages:threadIsEmpty:]
- -[EDInMemoryThread setState:]
- -[EDInMemoryThread state]
- -[_EDInMemoryThreadState .cxx_destruct]
- -[_EDInMemoryThreadState _addMessages:withComparator:]
- -[_EDInMemoryThreadState _changeMessages:]
- -[_EDInMemoryThreadState _combinedCCList]
- -[_EDInMemoryThreadState _combinedFlagColors]
- -[_EDInMemoryThreadState _combinedFlagColors].cold.1
- -[_EDInMemoryThreadState _combinedFlags]
- -[_EDInMemoryThreadState _combinedHasAttachments]
- -[_EDInMemoryThreadState _combinedHasUnflagged]
- -[_EDInMemoryThreadState _combinedIsBlocked]
- -[_EDInMemoryThreadState _combinedIsVIP]
- -[_EDInMemoryThreadState _combinedMailboxes]
- -[_EDInMemoryThreadState _combinedReadLater]
- -[_EDInMemoryThreadState _combinedSenderListWithDisplayMessage:]
- -[_EDInMemoryThreadState _combinedToList]
- -[_EDInMemoryThreadState _displayMessage]
- -[_EDInMemoryThreadState _maxSearchRelevanceScore]
- -[_EDInMemoryThreadState _newestDisplayDate]
- -[_EDInMemoryThreadState _newestMessage]
- -[_EDInMemoryThreadState _oldestMessage]
- -[_EDInMemoryThreadState _removeMessages:]
- -[_EDInMemoryThreadState _updateThreadWithObjectID:originatingQuery:]
- -[_EDInMemoryThreadState _updateThreadWithOriginatingQuery:]
- -[_EDInMemoryThreadState addMessages:withComparator:originatingQuery:]
- -[_EDInMemoryThreadState initWithMessages:objectID:originatingQuery:]
- -[_EDInMemoryThreadState messages]
- -[_EDInMemoryThreadState removeMessages:andChangeMessages:originatingQuery:threadIsEmpty:]
- -[_EDInMemoryThreadState setMessages:]
- -[_EDInMemoryThreadState setThread:]
- -[_EDInMemoryThreadState thread]
- -[_EDInMemoryThreadState updateMessage:fromOldObjectID:withComparator:originatingQuery:]
- _OBJC_CLASS_$__EDInMemoryThreadState
- _OBJC_IVAR_$_EDInMemoryThread._state
- _OBJC_IVAR_$__EDInMemoryThreadState._messages
- _OBJC_IVAR_$__EDInMemoryThreadState._thread
- _OBJC_METACLASS_$__EDInMemoryThreadState
- __OBJC_$_INSTANCE_METHODS__EDInMemoryThreadState
- __OBJC_$_INSTANCE_VARIABLES__EDInMemoryThreadState
- __OBJC_$_PROP_LIST__EDInMemoryThreadState
- __OBJC_CLASS_RO_$__EDInMemoryThreadState
- __OBJC_METACLASS_RO_$__EDInMemoryThreadState
- ___26-[EDInMemoryThread thread]_block_invoke
- ___28-[EDInMemoryThread messages]_block_invoke
- ___32-[EDInMemoryThread addMessages:]_block_invoke_2
- ___41-[_EDInMemoryThreadState _displayMessage]_block_invoke
- ___45-[_EDInMemoryThreadState _combinedFlagColors]_block_invoke
- ___50-[_EDInMemoryThreadState _maxSearchRelevanceScore]_block_invoke
- ___68-[EDInMemoryThread _removeMessages:andChangeMessages:threadIsEmpty:]_block_invoke
- ___69-[_EDInMemoryThreadState _updateThreadWithObjectID:originatingQuery:]_block_invoke
- ___69-[_EDInMemoryThreadState _updateThreadWithObjectID:originatingQuery:]_block_invoke.cold.1
- ___69-[_EDInMemoryThreadState _updateThreadWithObjectID:originatingQuery:]_block_invoke_2
- ___88-[_EDInMemoryThreadState updateMessage:fromOldObjectID:withComparator:originatingQuery:]_block_invoke
- ___block_descriptor_40_ea8_32r_e32_v16?0"_EDInMemoryThreadState"8lr32l8
- ___block_descriptor_64_ea8_32s40s48bs56r_e32_v16?0"_EDInMemoryThreadState"8lr56l8s32l8s48l8s40l8
- ___block_descriptor_72_ea8_32s40s48s56bs64r_e32_v16?0"_EDInMemoryThreadState"8lr64l8s32l8s40l8s56l8s48l8
- ___block_descriptor_72_ea8_32s40s48s56r64r_e32_v16?0"_EDInMemoryThreadState"8lr56l8s32l8s40l8s48l8r64l8
- ___block_descriptor_72_ea8_32s40s48s56s64bs_e26_v32?0"EMMessage"8Q16^B24ls32l8s40l8s48l8s64l8s56l8
- ___block_literal_global.120
- ___block_literal_global.131
- _objc_msgSend$_addMessages:withComparator:
- _objc_msgSend$_changeMessages:
- _objc_msgSend$_combinedSenderListWithDisplayMessage:
- _objc_msgSend$_displayMessage
- _objc_msgSend$_newestMessage
- _objc_msgSend$_removeMessages:
- _objc_msgSend$_removeMessages:andChangeMessages:threadIsEmpty:
- _objc_msgSend$_updateThreadWithObjectID:originatingQuery:
- _objc_msgSend$_updateThreadWithOriginatingQuery:
- _objc_msgSend$addMessages:withComparator:originatingQuery:
- _objc_msgSend$initWithMessages:objectID:originatingQuery:
- _objc_msgSend$removeMessages:andChangeMessages:originatingQuery:threadIsEmpty:
- _objc_msgSend$updateMessage:fromOldObjectID:withComparator:originatingQuery:
CStrings:
+ "T@\"<EMMessageListItem>\",R,N"
+ "T@\"EMMessage\",&,N,V_displayMessage"
+ "_addMessagesToThread:"
+ "_calculateAndApplyChange"
+ "_calculateChangesAfterRemovingMessages:applyingChanges:threadIsEmpty:"
+ "_combinedSenderList"
+ "_createThreadWithObjectID:"
+ "_isSortedByDate:"
+ "_recalculateDisplayMessage"
+ "messageListItem"
+ "oldestMessage"
+ "setDisplayMessage:"
- "@40@0:8@16@?24@32"
- "@48@0:8@16@24@32^B40"
- "@48@0:8@16@24@?32@40"
- "Display message for in-memory thread must be nonnull"
- "EDInMemoryThread.m"
- "Newest message for in-memory thread must be nonnull"
- "T@\"EFLocked\",&,N,V_state"
- "T@\"NSMutableArray\",&,N,V_messages"
- "_EDInMemoryThreadState"
- "_addMessages:withComparator:"
- "_changeMessages:"
- "_combinedSenderListWithDisplayMessage:"
- "_newestMessage"
- "_oldestMessage"
- "_removeMessages:"
- "_removeMessages:andChangeMessages:threadIsEmpty:"
- "_updateThreadWithObjectID:originatingQuery:"
- "_updateThreadWithOriginatingQuery:"
- "addMessages:withComparator:originatingQuery:"
- "initWithMessages:objectID:originatingQuery:"
- "removeMessages:andChangeMessages:originatingQuery:threadIsEmpty:"
- "updateMessage:fromOldObjectID:withComparator:originatingQuery:"
- "v16@?0@\"_EDInMemoryThreadState\"8"

```
