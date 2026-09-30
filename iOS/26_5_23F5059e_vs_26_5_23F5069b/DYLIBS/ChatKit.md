## ChatKit

> `/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit`

```diff

-1450.600.53.2.3
-  __TEXT.__text: 0xbb0b28
+1450.600.61.2.7
+  __TEXT.__text: 0xbb1090
   __TEXT.__auth_stubs: 0xc1f0
   __TEXT.__delay_helper: 0xcd0
-  __TEXT.__objc_methlist: 0x70694
-  __TEXT.__const: 0x3bd74
-  __TEXT.__gcc_except_tab: 0x242d0
-  __TEXT.__cstring: 0x3c431
-  __TEXT.__oslogstring: 0x4e5f3
+  __TEXT.__objc_methlist: 0x706a4
+  __TEXT.__const: 0x3bd84
+  __TEXT.__gcc_except_tab: 0x24300
+  __TEXT.__cstring: 0x3c441
+  __TEXT.__oslogstring: 0x4e7b3
   __TEXT.__dlopen_cstrs: 0xb55
   __TEXT.__ustring: 0x1c4
   __TEXT.__swift5_typeref: 0x40592

   __TEXT.__unwind_info: 0x31f68
   __TEXT.__eh_frame: 0xddd4
   __TEXT.__objc_classname: 0x12626
-  __TEXT.__objc_methname: 0x117dba
+  __TEXT.__objc_methname: 0x117e3a
   __TEXT.__objc_methtype: 0x25836
-  __TEXT.__objc_stubs: 0xadae0
+  __TEXT.__objc_stubs: 0xadb40
   __DATA_CONST.__got: 0x7300
   __DATA_CONST.__const: 0xed80
   __DATA_CONST.__objc_classlist: 0x2f10
   __DATA_CONST.__objc_catlist: 0x548
   __DATA_CONST.__objc_protolist: 0x1350
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35c28
+  __DATA_CONST.__objc_selrefs: 0x35c40
   __DATA_CONST.__objc_protorefs: 0x518
   __DATA_CONST.__objc_superrefs: 0x19e8
   __DATA_CONST.__objc_arraydata: 0xef0
   __AUTH_CONST.__auth_got: 0x6108
   __AUTH_CONST.__const: 0x3a248
-  __AUTH_CONST.__cfstring: 0x24140
+  __AUTH_CONST.__cfstring: 0x24160
   __AUTH_CONST.__objc_const: 0x99d30
   __AUTH_CONST.__objc_arrayobj: 0xe28
-  __AUTH_CONST.__objc_intobj: 0x1008
+  __AUTH_CONST.__objc_intobj: 0xf60
   __AUTH_CONST.__objc_doubleobj: 0x880
   __AUTH_CONST.__objc_floatobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x1e0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EDA6BB80-2C7A-3D9A-9159-4648284C27FC
-  Functions: 70642
-  Symbols:   146817
-  CStrings:  59650
+  UUID: 0EFF94FC-A9BD-3EA8-8EA4-09803C5F2E75
+  Functions: 70643
+  Symbols:   146822
+  CStrings:  59658
 
Symbols:
+ -[CKConversationListScrollingController _setDate:forFilterMode:inDictionary:]
+ ___96-[CKConversationListScrollingController _loadOlderConversationsWithFilterModes:limit:iteration:]_block_invoke.265
+ ___block_descriptor_48_e8_32s40s_e33_v32?0"NSNumber"8"NSDate"16^B24ls32l8s40l8
+ _objc_msgSend$_setDate:forFilterMode:inDictionary:
+ _objc_msgSend$chatWithHandles:displayName:joinedChatsOnly:findMatchingNamedGroups:lastAddressedHandle:lastAddressedSIMID:needsFreshGroupCreation:
+ _objc_msgSend$hasDisappearedChatBot
+ _objc_msgSend$nameForDisappearedChatBot
- ___96-[CKConversationListScrollingController _loadOlderConversationsWithFilterModes:limit:iteration:]_block_invoke.261
- ___block_descriptor_40_e8_32s_e33_v32?0"NSNumber"8"NSDate"16^B24ls32l8
- _objc_msgSend$chatWithHandles:displayName:joinedChatsOnly:findMatchingNamedGroups:lastAddressedHandle:lastAddressedSIMID:
CStrings:
+ "(nil, using now)"
+ "Input filterCategoryToEarliestInitiallyFetchedLastMessageDate: %@"
+ "Kicking off request (%llu) for %llu older conversations with filter mode %d filterModeNum=%@ predicate=%@ older than date %@ (oldest conversation date: %@) conversationCount=%llu"
+ "Pagination decision: repeat=%@ nextLimit=%llu earliestReachedDate=%@ earliestLoadedConversationDate=%@ fetchDate=%@ filterModeNum=%@ updatingCursor from %@ to %@"
+ "_setDate:forFilterMode:inDictionary:"
+ "chatWithHandles:displayName:joinedChatsOnly:findMatchingNamedGroups:lastAddressedHandle:lastAddressedSIMID:needsFreshGroupCreation:"
+ "hasDisappearedChatBot"
+ "nameForDisappearedChatBot"
+ "reachedConversation: date=%@ filterModes=%@ filterModeNum=%@ earliestFetchedDate=%@ (from dict: %@) earliestReachedDate=%@ remainingRows=%ld allFetchedDates=%@"
- "Kicking off request (%llu) for %llu older conversations with filter mode %d older than date %@ (oldest conversation date: %@)"
- "chatWithHandles:displayName:joinedChatsOnly:findMatchingNamedGroups:lastAddressedHandle:lastAddressedSIMID:"

```
