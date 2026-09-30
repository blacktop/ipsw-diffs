## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-64.309.0.0.0
-  __TEXT.__text: 0x2f26c
-  __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0x267c
-  __TEXT.__const: 0x1c0
-  __TEXT.__cstring: 0x2419
+64.313.1.0.0
+  __TEXT.__text: 0x3176c
+  __TEXT.__auth_stubs: 0xb40
+  __TEXT.__objc_methlist: 0x2774
+  __TEXT.__const: 0x1e0
+  __TEXT.__cstring: 0x2609
   __TEXT.__oslogstring: 0x3b36
   __TEXT.__gcc_except_tab: 0x2a8
-  __TEXT.__swift5_typeref: 0xa9
+  __TEXT.__swift5_typeref: 0xf5
   __TEXT.__swift5_capture: 0x88
   __TEXT.__constg_swiftt: 0x4c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x970
+  __TEXT.__unwind_info: 0x9c0
   __TEXT.__eh_frame: 0x2e8
-  __TEXT.__objc_classname: 0x4eb
-  __TEXT.__objc_methname: 0x5f2b
+  __TEXT.__objc_classname: 0x544
+  __TEXT.__objc_methname: 0x6094
   __TEXT.__objc_methtype: 0x852
-  __TEXT.__objc_stubs: 0x4900
-  __DATA_CONST.__got: 0xa70
-  __DATA_CONST.__const: 0x9d8
-  __DATA_CONST.__objc_classlist: 0x160
+  __TEXT.__objc_stubs: 0x4a80
+  __DATA_CONST.__got: 0xb10
+  __DATA_CONST.__const: 0xa18
+  __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14a0
+  __DATA_CONST.__objc_selrefs: 0x14f8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xf0
-  __DATA_CONST.__objc_arraydata: 0x98
-  __AUTH_CONST.__auth_got: 0x560
-  __AUTH_CONST.__auth_ptr: 0x90
-  __AUTH_CONST.__const: 0x888
-  __AUTH_CONST.__cfstring: 0x27a0
-  __AUTH_CONST.__objc_const: 0x4450
-  __AUTH_CONST.__objc_intobj: 0x630
+  __DATA_CONST.__objc_superrefs: 0xf8
+  __DATA_CONST.__objc_arraydata: 0xa0
+  __AUTH_CONST.__auth_got: 0x5b0
+  __AUTH_CONST.__auth_ptr: 0xb8
+  __AUTH_CONST.__const: 0x988
+  __AUTH_CONST.__cfstring: 0x2940
+  __AUTH_CONST.__objc_const: 0x4640
+  __AUTH_CONST.__objc_intobj: 0x708
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH.__objc_data: 0x3b0
+  __AUTH.__objc_data: 0x4a0
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x334
-  __DATA.__data: 0x358
-  __DATA.__bss: 0xe0
+  __DATA.__objc_ivar: 0x338
+  __DATA.__data: 0x3b0
+  __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0xa50
   __DATA_DIRTY.__bss: 0x1b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1135
-  Symbols:   459
-  CStrings:  1793
+  Functions: 1169
+  Symbols:   479
+  CStrings:  1829
 
Symbols:
+ _IAPayloadKeyGenmojiCreationPromptLanguage
+ _IAPayloadKeyGenmojiEditType
+ _IAPayloadKeySmartRepliesConversationType
+ _IAPayloadKeySmartRepliesInputLanguage
+ _IAPayloadKeyWritingToolsInputLanguage
+ _IAPayloadValueGenmojiEditTypeAnimated
+ _IAPayloadValueGenmojiEditTypeComic
+ _IAPayloadValueGenmojiEditTypeDelete
+ _IAPayloadValueGenmojiEditTypeOriginal
+ _IAPayloadValueGenmojiEditTypeOutline
+ _IAPayloadValueGenmojiEditTypePuffy
+ _IAPayloadValueGenmojiEditTypeRearrange
+ _IAPayloadValueGenmojiEditTypeShiny
+ _IAPayloadValueSmartRepliesConversationTypeMail
+ _IAPayloadValueSmartRepliesConversationTypeMessage
+ _IAPayloadValueSmartRepliesConversationTypeUnknown
+ _IAPayloadValueSmartRepliesConversationTypeUnspecified
+ __swiftEmptyDictionarySingleton
+ __swiftEmptySetSingleton
+ _swift_retain
CStrings:
+ "\x11\x12\x11\x12\x13A1"
+ "\x11\x15"
+ "\x12"
+ "\x14\x13\x15\x11\x11"
+ "\x17\x11\x135S"
+ "%@ %@ state=%@ editable=%@ featureDetails=%@ fatalError=%lu errors=%@"
+ "CreationUI"
+ "Encountered conflicting smart reply languages. Old language: %@. New langauge: %@"
+ "IASDailyGarbageCollectionStateMachineAnalyzer"
+ "IASGenmojiEdit"
+ "IASGenmojiEditAnalyzer"
+ "IASGenmojiEditAnalyzer.m"
+ "IASGenmojiEditEvent"
+ "IsEditable status changed from %@ to %@"
+ "Mail Smart Reply"
+ "Messages Smart Reply"
+ "T@\"NSNumber\",C,N,V_isEditable"
+ "T@\"NSString\",C,N,V_promptLanguage"
+ "T@\"NSString\",C,N,V_selectedLanguage"
+ "TODO: Implement in each child class"
+ "VisualGeneration.TextSanitizerError"
+ "_promptLanguage"
+ "_selectedLanguage"
+ "addObjectsFromArray:"
+ "com.apple."
+ "com.apple.Messages"
+ "com.apple.MobileSMS"
+ "com.apple.inputAnalytics.generatedEmojiEdits"
+ "com.apple.mail"
+ "conversationType"
+ "editType"
+ "editTypeFromPayload:"
+ "entryPointSignalArray"
+ "getNextStateForResultsRejectedSignal:"
+ "handleGenmojiEditSignal:"
+ "isEqualToNumber:"
+ "promptLanguage"
+ "recordCreationUISeenForToday"
+ "selectedLanguage"
+ "setPromptLanguage:"
+ "setSelectedLanguage:"
+ "smartRepliesLanguage"
- "\x11\x12\x11\x11\x13A1"
- "\x13\x13\x15\x11\x11"
- "\x16\x11\x134S"
- "!\x15"
- "\""
- "%@ %@ state=%@ editable=%lu featureDetails=%@ fatalError=%lu errors=%@"
- "TB,N,V_isEditable"
- "VisualGeneration.TextSanitizer.Error"

```
