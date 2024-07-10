## Email

> `/System/Library/PrivateFrameworks/Email.framework/Versions/A/Email`

```diff

-3812.100.13.1.1
-  __TEXT.__text: 0xd86fc
+3810.100.6.0.0
+  __TEXT.__text: 0xd80c8
   __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_methlist: 0xa614
-  __TEXT.__gcc_except_tab: 0x1b1fc
-  __TEXT.__const: 0x28a
+  __TEXT.__objc_methlist: 0xa604
+  __TEXT.__gcc_except_tab: 0x1b16c
+  __TEXT.__const: 0x24a
   __TEXT.__cstring: 0x96a0
-  __TEXT.__oslogstring: 0x513c
+  __TEXT.__oslogstring: 0x4f2c
   __TEXT.__ustring: 0x154
   __TEXT.__dlopen_cstrs: 0x5e
   __TEXT.__constg_swiftt: 0xa4

   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_capture: 0x24
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x7a58
+  __TEXT.__unwind_info: 0x7a50
   __TEXT.__objc_classname: 0x1a9e
-  __TEXT.__objc_methname: 0x1ae27
-  __TEXT.__objc_methtype: 0x4afd
-  __TEXT.__objc_stubs: 0x11d20
+  __TEXT.__objc_methname: 0x1adb5
+  __TEXT.__objc_methtype: 0x4af7
+  __TEXT.__objc_stubs: 0x11ce0
   __DATA_CONST.__got: 0xb60
-  __DATA_CONST.__const: 0x15a0
+  __DATA_CONST.__const: 0x1580
   __DATA_CONST.__objc_classlist: 0x548
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x338
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5ac8
+  __DATA_CONST.__objc_selrefs: 0x5ab8
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x438
   __DATA_CONST.__objc_arraydata: 0x110
   __AUTH_CONST.__auth_got: 0x688
   __AUTH_CONST.__auth_ptr: 0x38
   __AUTH_CONST.__const: 0x4720
-  __AUTH_CONST.__cfstring: 0x86e0
-  __AUTH_CONST.__objc_const: 0x1a550
+  __AUTH_CONST.__cfstring: 0x8660
+  __AUTH_CONST.__objc_const: 0x1a4e8
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4426
-  Symbols:   13265
-  CStrings:  1402
+  Functions: 4424
+  Symbols:   13257
+  CStrings:  1398
 
Symbols:
+ +[EMMessageList simpleMessageListForMailboxes:withRepository:additionalQueryOptions:shouldUpdateDisplayDate:sortDescriptors:transformPredicate:ignoreMessageAdditionsPredicate:]
+ +[EMMessageList threadedMessageListForMailboxes:withRepository:additionalQueryOptions:shouldUpdateDisplayDate:sortDescriptors:transformPredicate:ignoreMessageAdditionsPredicate:]
+ -[EMMessageList _addPrefetchedItems:]
+ -[EMMessageList _prefetchedThreadsFromExtraInfo:]
+ -[EMMessageList initWithMailboxes:repository:sortDescriptors:transformPredicate:ignoreMessageAdditionsPredicate:targetClass:additionalQueryOptions:shouldUpdateDisplayDate:labelPrefix:]
+ -[EMMessageRepository _addPrefetchedItems:]
+ -[_EMMessageRepositoryQueryObserver _prefetchedThreadsFromExtraInfo:]
+ _EMMessageListChangedItemsExtraInfoKeyPrefetchedItems
+ __32-[EMMessageList collapseThread:]_block_invoke.124
+ __32-[EMMessageList collapseThread:]_block_invoke.124.cold.1
+ __54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.140
+ __54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.147
+ __54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.147.cold.1
+ __54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.151
+ __54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke_2.141
+ __56-[EMMessageList queryMatchedChangedObjectIDs:extraInfo:]_block_invoke.185
+ __58-[EMMessageList _attemptToFinishRetryingPromisesByItemID:]_block_invoke.155
+ __69-[EMMessageList queryMatchedOldestItemsUpdatedForMailboxesObjectIDs:]_block_invoke.194
+ ___37-[EMMessageList _addPrefetchedItems:]_block_invoke
+ __block_literal_global.243
+ __block_literal_global.249
+ __block_literal_global.255
+ _objc_msgSend$_addPrefetchedItems:
+ _objc_msgSend$_prefetchedThreadsFromExtraInfo:
+ _objc_msgSend$initWithMailboxes:repository:sortDescriptors:transformPredicate:ignoreMessageAdditionsPredicate:targetClass:additionalQueryOptions:shouldUpdateDisplayDate:labelPrefix:
+ _objc_msgSend$simpleMessageListForMailboxes:withRepository:additionalQueryOptions:shouldUpdateDisplayDate:sortDescriptors:transformPredicate:ignoreMessageAdditionsPredicate:
+ _objc_msgSend$threadedMessageListForMailboxes:withRepository:additionalQueryOptions:shouldUpdateDisplayDate:sortDescriptors:transformPredicate:ignoreMessageAdditionsPredicate:
- +[EMMessageList simpleMessageListForMailboxes:withRepository:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:sortDescriptors:transformPredicate:ignoreMessageAdditionsPredicate:]
- +[EMMessageList threadedMessageListForMailboxes:withRepository:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:sortDescriptors:transformPredicate:ignoreMessageAdditionsPredicate:]
- -[EMMessageList _addPrecachedItemsFromExtraInfo:]
- -[EMMessageList initWithMailboxes:repository:sortDescriptors:transformPredicate:ignoreMessageAdditionsPredicate:targetClass:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:labelPrefix:]
- -[EMMessageRepository _addPrecachedItems:]
- -[EMSortableThreadProxy description]
- -[EMSortableThreadProxy ef_publicDescription]
- -[_EMMessageRepositoryQueryObserver _precachedItemsFromExtraInfo:]
- _EMCategoryFromSubtype
- _EMMessageListChangedItemsExtraInfoKeyPrecachedItems
- _EMMessageListQueryOptionPrecacheAndIncludeItemWithObjectIDInInitialBatch
- _EMMessageListQueryOptionPrecacheItemsInInitialBatchWithCount
- __32-[EMMessageList collapseThread:]_block_invoke.130
- __32-[EMMessageList collapseThread:]_block_invoke.130.cold.1
- __54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.146
- __54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.153
- __54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.153.cold.1
- __54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.157
- __54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke_2.147
- __56-[EMMessageList queryMatchedChangedObjectIDs:extraInfo:]_block_invoke.191
- __58-[EMMessageList _attemptToFinishRetryingPromisesByItemID:]_block_invoke.161
- __69-[EMMessageList queryMatchedOldestItemsUpdatedForMailboxesObjectIDs:]_block_invoke.200
- __OBJC_CLASS_PROTOCOLS_$_EMSortableThreadProxy
- ___49-[EMMessageList _addPrecachedItemsFromExtraInfo:]_block_invoke
- __block_literal_global.240
- __block_literal_global.246
- __block_literal_global.252
- _objc_msgSend$_addPrecachedItems:
- _objc_msgSend$_addPrecachedItemsFromExtraInfo:
- _objc_msgSend$_precachedItemsFromExtraInfo:
- _objc_msgSend$initWithMailboxes:repository:sortDescriptors:transformPredicate:ignoreMessageAdditionsPredicate:targetClass:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:labelPrefix:
- _objc_msgSend$predicateFormat
- _objc_msgSend$simpleMessageListForMailboxes:withRepository:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:sortDescriptors:transformPredicate:ignoreMessageAdditionsPredicate:
- _objc_msgSend$threadedMessageListForMailboxes:withRepository:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:sortDescriptors:transformPredicate:ignoreMessageAdditionsPredicate:
CStrings:
+ "This should never happen, looks like a bug in how events are wired up in the UI"
+ "prefetchedItems"
- "System_Account"
- "[%!l(MISSING)ld - %!@(MISSING) (%!@(MISSING))]"
- "[%!l(MISSING)ld - %!@(MISSING)]"
- "objectIDForInitialBatch"
- "precacheItemsWithCount"
- "precachedItems"

```
