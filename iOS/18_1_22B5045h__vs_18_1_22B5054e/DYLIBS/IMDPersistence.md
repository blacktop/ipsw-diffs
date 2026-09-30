## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1402.200.57.0.0
-  __TEXT.__text: 0x11499c
-  __TEXT.__auth_stubs: 0x26b0
-  __TEXT.__objc_methlist: 0x3734
-  __TEXT.__const: 0xb5a
-  __TEXT.__cstring: 0x39151
-  __TEXT.__oslogstring: 0x19a55
-  __TEXT.__gcc_except_tab: 0xd2cc
+1402.200.75.2.1
+  __TEXT.__text: 0x1147c8
+  __TEXT.__auth_stubs: 0x26d0
+  __TEXT.__objc_methlist: 0x372c
+  __TEXT.__const: 0xb4a
+  __TEXT.__cstring: 0x39081
+  __TEXT.__oslogstring: 0x19a75
+  __TEXT.__gcc_except_tab: 0xd2c0
   __TEXT.__ustring: 0x430
   __TEXT.__dlopen_cstrs: 0x2a4
   __TEXT.__swift5_typeref: 0x206

   __TEXT.__swift5_capture: 0xe4
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_reflstr: 0x6f
-  __TEXT.__unwind_info: 0x4c98
+  __TEXT.__unwind_info: 0x4c80
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0xaac
-  __TEXT.__objc_methname: 0xff5c
-  __TEXT.__objc_methtype: 0x2414
-  __TEXT.__objc_stubs: 0xd400
-  __DATA_CONST.__got: 0xdd8
-  __DATA_CONST.__const: 0x10d78
+  __TEXT.__objc_methname: 0xfea7
+  __TEXT.__objc_methtype: 0x2402
+  __TEXT.__objc_stubs: 0xd380
+  __DATA_CONST.__got: 0xdd0
+  __DATA_CONST.__const: 0x10d70
   __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3978
+  __DATA_CONST.__objc_selrefs: 0x3958
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0xf0
-  __DATA_CONST.__objc_arraydata: 0x198
-  __AUTH_CONST.__auth_got: 0x1368
+  __DATA_CONST.__objc_arraydata: 0x190
+  __AUTH_CONST.__auth_got: 0x1378
   __AUTH_CONST.__auth_ptr: 0x90
   __AUTH_CONST.__const: 0x1aa8
-  __AUTH_CONST.__cfstring: 0x10c00
-  __AUTH_CONST.__objc_const: 0x68a0
+  __AUTH_CONST.__cfstring: 0x10be0
+  __AUTH_CONST.__objc_const: 0x6880
   __AUTH_CONST.__objc_intobj: 0x138
-  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH.__objc_data: 0x358
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x170

   __DATA.__bss: 0x3f8
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x17a0
-  __DATA_DIRTY.__data: 0xea8
+  __DATA_DIRTY.__data: 0xe98
   __DATA_DIRTY.__bss: 0x5c8
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4456
-  Symbols:   2308
-  CStrings:  7322
+  Functions: 4449
+  Symbols:   2309
+  CStrings:  7315
 
Symbols:
+ _IMMessageCreateBalloonPluginAssociatedMessageGUIDFromThreadIdentifier
+ _OBJC_CLASS_$_IMOneTimeCodeUtilities
+ _IMBalloonBundleIdentifierChatBot
+ _CFMakeCollectable
- _OBJC_CLASS_$_CSSearchQueryContext
- _OBJC_CLASS_$_CSSearchQuery
- _MDItemMessageType
CStrings:
+ "SELECT   m.ROWID FROM   message m WHERE   m.associated_message_guid IN (?, ?)  AND m.thread_originator_guid IS NULL"
+ "message %!@(MISSING) is from a chat bot and is OTC"
+ "Creating chat bot message containing OTC guid: %!@(MISSING)"
+ "ChatBot"
+ "createOTCFromMessageBody:sender:guid:"
+ "isFromChatBotNotOTC:"
+ "message %!@(MISSING) is from a chat bot but is not OTC"
- "handleIMDCoreSpotlightCheckIndexCount_IPCActionWithXPCConnection:requestMessage:responseMessage:completionHandler:"
- "-[IMDDatabase(Spotlight) checkSpotlightIndexCountWithCompletion:]"
- "%!{(MISSING)public}s Starting query with string %!{(MISSING)public}@"
- "v24@0:8@?<v@?q>16"
- "setBundleIDs:"
- "setCountChangedHandler:"
- "-[IMDDatabase(Spotlight) checkSpotlightIndexCountWithCompletion:]_block_invoke_2"
- "%!{(MISSING)public}s Got %!l(MISSING)ld total indexed items for query %!{(MISSING)public}@"
- "initWithQueryString:queryContext:"
- "setCounting:"
- "Query: Count the total number of indexed items in Spotlight"
- "%!@(MISSING) == \"%!@(MISSING)\""
- "SELECT   m.ROWID FROM   message m WHERE   m.associated_message_guid = ?  AND m.thread_originator_guid IS NULL"
- "checkSpotlightIndexCountWithCompletion:"

```
