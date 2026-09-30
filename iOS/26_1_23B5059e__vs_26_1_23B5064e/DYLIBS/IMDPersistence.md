## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1450.200.75.0.0
-  __TEXT.__text: 0x220bf0
-  __TEXT.__auth_stubs: 0x4530
-  __TEXT.__objc_methlist: 0x710c
-  __TEXT.__const: 0xa1e8
-  __TEXT.__cstring: 0x47afb
-  __TEXT.__oslogstring: 0x1d7b6
-  __TEXT.__gcc_except_tab: 0xd054
+1450.200.88.2.1
+  __TEXT.__text: 0x221a48
+  __TEXT.__auth_stubs: 0x4550
+  __TEXT.__objc_methlist: 0x719c
+  __TEXT.__const: 0xa218
+  __TEXT.__cstring: 0x47d3b
+  __TEXT.__oslogstring: 0x1d886
+  __TEXT.__gcc_except_tab: 0xd0cc
   __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x360
-  __TEXT.__constg_swiftt: 0x4ccc
-  __TEXT.__swift5_typeref: 0x324c
+  __TEXT.__constg_swiftt: 0x4cf8
+  __TEXT.__swift5_typeref: 0x3252
   __TEXT.__swift5_builtin: 0x244
   __TEXT.__swift5_reflstr: 0x2ac1
-  __TEXT.__swift5_fieldmd: 0x2d50
+  __TEXT.__swift5_fieldmd: 0x2d60
   __TEXT.__swift5_assocty: 0x530
   __TEXT.__swift5_proto: 0x664
-  __TEXT.__swift5_types: 0x31c
+  __TEXT.__swift5_types: 0x320
   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_capture: 0xfb0
   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x87b8
+  __TEXT.__unwind_info: 0x8830
   __TEXT.__eh_frame: 0x6de8
   __TEXT.__objc_classname: 0x11ad
-  __TEXT.__objc_methname: 0x177ac
-  __TEXT.__objc_methtype: 0x371a
-  __TEXT.__objc_stubs: 0x11a40
-  __DATA_CONST.__got: 0x16f8
-  __DATA_CONST.__const: 0x8330
-  __DATA_CONST.__objc_classlist: 0x5f0
+  __TEXT.__objc_methname: 0x179a4
+  __TEXT.__objc_methtype: 0x3781
+  __TEXT.__objc_stubs: 0x11b20
+  __DATA_CONST.__got: 0x1708
+  __DATA_CONST.__const: 0x8390
+  __DATA_CONST.__objc_classlist: 0x5f8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5200
+  __DATA_CONST.__objc_selrefs: 0x5248
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x220
-  __AUTH_CONST.__auth_got: 0x22a8
-  __AUTH_CONST.__const: 0x9878
-  __AUTH_CONST.__cfstring: 0x11ea0
-  __AUTH_CONST.__objc_const: 0xf320
+  __AUTH_CONST.__auth_got: 0x22b8
+  __AUTH_CONST.__const: 0x9890
+  __AUTH_CONST.__cfstring: 0x11f40
+  __AUTH_CONST.__objc_const: 0xf388
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x1b10
-  __AUTH.__data: 0x3e78
+  __AUTH.__objc_data: 0x1bc0
+  __AUTH.__data: 0x3ea8
   __DATA.__objc_ivar: 0x484
-  __DATA.__data: 0x2b90
+  __DATA.__data: 0x2ba0
   __DATA.__bss: 0x9fe0
   __DATA.__common: 0x168
   __DATA_DIRTY.__objc_data: 0x1620

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C41C9A2A-8081-35DA-BBC8-4B433D47A066
-  Functions: 10515
-  Symbols:   2563
-  CStrings:  12243
+  UUID: A0D7243A-A71A-3806-9756-9B481AA80077
+  Functions: 10542
+  Symbols:   2566
+  CStrings:  12271
 
Symbols:
+ _IMDChatRecordCopyChatForGUIDWithDisplayNameHiddenIfUnknown
+ _OBJC_CLASS_$__TtC14IMDPersistence29IMDChatQueriesKnownChatHelper
+ _OBJC_METACLASS_$__TtC14IMDPersistence29IMDChatQueriesKnownChatHelper
CStrings:
+ "-[IMDDatabase(LegacyMessages) fetchMessageRecordCountFilteredUsingPredicate:inChatsFilteredUsingPredicate:limit:completionHandler:]_block_invoke"
+ "Counting messages for chat: %@ filtered by predicate: %@"
+ "IMDCNPersonAliasResolver: Updating aliasToCNIDMap using %@ Contact Change History events"
+ "IMDCoreSpotlight: Contacts store reported a change"
+ "JOIN chat_message_join ON chat_message_join.message_id = message.rowid JOIN chat ON chat.rowid = chat_message_join.chat_id "
+ "SELECT COUNT(*) FROM (SELECT 1 FROM message %@ %@ LIMIT ?);"
+ "SELECT COUNT(*) FROM message %@ %@;"
+ "_TtC14IMDPersistence29IMDChatQueriesKnownChatHelper"
+ "_contactStoreDidChange"
+ "_isChatConfigurationKnownWithRecord:"
+ "_queryForMessageRecordCountWithMessageWhereClause:chatWhereClause:limit:"
+ "cancelPreviousPerformRequestsWithTarget:selector:object:"
+ "fetchMessageRecordCountFilteredUsingPredicate:inChatsFilteredUsingPredicate:limit:completionHandler:"
+ "fetchMessageRecordCountForChatRecordWithGUID:filteredUsingPredicate:limit:completionHandler:"
+ "hideNamesForUnknownGroupChats"
+ "isChatConfigurationKnownWith:handles:"
+ "isChatConfigurationKnownWith:participants:"
+ "message(schedule_type, schedule_state)"
+ "message_idx_composite_scheduled_message"
+ "performSelector:withObject:afterDelay:"
+ "v48@0:8@\"NSPredicate\"16@\"NSPredicate\"24Q32@?<v@?Q>40"
+ "v48@0:8@\"NSString\"16@\"NSPredicate\"24Q32@?<v@?Q>40"

```
