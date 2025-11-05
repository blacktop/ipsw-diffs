## InputAnalytics

> `/System/Library/PrivateFrameworks/InputAnalytics.framework/Versions/A/InputAnalytics`

```diff

-64.224.0.0.0
-  __TEXT.__text: 0x22204
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_methlist: 0x2320
+64.315.0.0.0
+  __TEXT.__text: 0x24f30
+  __TEXT.__auth_stubs: 0x670
+  __TEXT.__objc_methlist: 0x27fc
   __TEXT.__const: 0x282
+  __TEXT.__cstring: 0x5a82
   __TEXT.__gcc_except_tab: 0x468
-  __TEXT.__oslogstring: 0x29e0
-  __TEXT.__cstring: 0x5992
+  __TEXT.__oslogstring: 0x2ba0
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x8a
+  __TEXT.__swift5_typeref: 0x8c
   __TEXT.__swift5_capture: 0x88
   __TEXT.__constg_swiftt: 0x4c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x8b0
+  __TEXT.__swift_as_entry: 0x1c
+  __TEXT.__swift_as_ret: 0x1c
+  __TEXT.__unwind_info: 0x978
   __TEXT.__eh_frame: 0x310
-  __TEXT.__objc_classname: 0x715
-  __TEXT.__objc_methname: 0x4d46
+  __TEXT.__objc_classname: 0x79b
+  __TEXT.__objc_methname: 0x4f58
   __TEXT.__objc_methtype: 0xa60
-  __TEXT.__objc_stubs: 0x3160
-  __DATA_CONST.__got: 0x248
-  __DATA_CONST.__const: 0xfd0
-  __DATA_CONST.__objc_classlist: 0x1c0
+  __TEXT.__objc_stubs: 0x33c0
+  __DATA_CONST.__got: 0x250
+  __DATA_CONST.__const: 0x1138
+  __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1110
+  __DATA_CONST.__objc_selrefs: 0x1238
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x120
+  __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x18c0
-  __AUTH_CONST.__auth_got: 0x368
-  __AUTH_CONST.__const: 0x8d8
-  __AUTH_CONST.__cfstring: 0x81c0
-  __AUTH_CONST.__objc_const: 0x48d8
-  __AUTH_CONST.__objc_intobj: 0x828
+  __AUTH_CONST.__auth_got: 0x348
+  __AUTH_CONST.__const: 0xa68
+  __AUTH_CONST.__cfstring: 0x86a0
+  __AUTH_CONST.__objc_const: 0x4670
+  __AUTH_CONST.__objc_intobj: 0x9c0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x11a0
+  __AUTH.__objc_data: 0x1330
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x24c
+  __DATA.__objc_ivar: 0x254
   __DATA.__data: 0x370
-  __DATA.__bss: 0x1a8
+  __DATA.__bss: 0x258
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 80A4CF09-A8F4-3307-A066-ED39E40C5052
-  Functions: 982
-  Symbols:   602
-  CStrings:  3328
+  UUID: 24B0F76A-0FD8-3808-9B1C-ADAAF13FE5B1
+  Functions: 1092
+  Symbols:   633
+  CStrings:  3433
 
Symbols:
+ _IAPayloadKeyFeedbackServiceRequestingBundleID
+ _IAPayloadKeyFeedbackServiceRequestingSceneID
+ _IAPayloadKeyGenmojiBundleID
+ _IAPayloadKeyGenmojiCreationErrorCode
+ _IAPayloadKeyGenmojiCreationErrorDomain
+ _IAPayloadKeyGenmojiCreationPromptTokenCount
+ _IAPayloadKeySmartRepliesBundleId
+ _IAPayloadKeySmartRepliesConversationType
+ _IAPayloadKeySmartRepliesInputLanguage
+ _IAPayloadKeySmartRepliesInputTokenCount
+ _IAPayloadKeySmartRepliesOutputTokenCount
+ _IAPayloadKeyWritingToolsInputTextTokenCount
+ _IAPayloadKeyWritingToolsOutputTextTokenCount
+ _IAPayloadValueGenmojiCreationFailReasonEmojiGenerationErrorOther
+ _IAPayloadValueGenmojiEditTypeAnimated
+ _IAPayloadValueGenmojiEditTypeComic
+ _IAPayloadValueGenmojiEditTypeOriginal
+ _IAPayloadValueGenmojiEditTypeOutline
+ _IAPayloadValueGenmojiEditTypePuffy
+ _IAPayloadValueGenmojiEditTypeShiny
+ _IAPayloadValueGenmojiEditTypeUnspecified
+ _IAPayloadValueGenmojiUsageTypePeel
+ _IAPayloadValueGenmojiUsageTypePeelCancel
+ _IAPayloadValueGenmojiUsageTypePeelCancelNoDrag
+ _IAPayloadValueGenmojiUsageTypeStick
+ _IAPayloadValueSmartRepliesConversationTypeMail
+ _IAPayloadValueSmartRepliesConversationTypeMessage
+ _IAPayloadValueSmartRepliesConversationTypeUnknown
+ _IAPayloadValueSmartRepliesConversationTypeUnspecified
+ _IASignalGenmojiCreationMessagesSendMenuButtonPressed
+ _IASignalWritingToolsHandoffRequested
+ _IASignalWritingToolsHandoffStarted
- _IAPayloadValueGenmojiUsageTypePeelAndStick
CStrings:
+ "Animated"
+ "CandidateBarSuggestion"
+ "Comic"
+ "Composition"
+ "ConversationType"
+ "Decomposition"
+ "ERROR: Invalid special case for genmoji usage analyzer"
+ "EmojiGenerationErrorOther"
+ "ErrorCode"
+ "ErrorDomain"
+ "FeedbackServiceRequestingBundleID"
+ "FeedbackServiceRequestingSceneID"
+ "HandoffRequested"
+ "HandoffStarted"
+ "IAGenmoji"
+ "IAGenmojiUsage"
+ "IASDailyGarbageCollectionStateMachineAnalyzer"
+ "IASGenmojiEdit"
+ "IASGenmojiEditAnalyzer"
+ "IASGenmojiEditAnalyzer.m"
+ "IASGenmojiEditEvent"
+ "IASGenmojiUsageAnalyzer"
+ "IASGenmojiUsageAnalyzer.m"
+ "IASGenmojiUsageEvent"
+ "Initialized analyzer"
+ "InputTextTokenCount"
+ "InputTokenCount"
+ "Message"
+ "MessagesSendMenuButtonPressed"
+ "Original"
+ "Outline"
+ "OutputTextTokenCount"
+ "OutputTokenCount"
+ "Peel"
+ "PeelCancel"
+ "PeelCancelNoDrag"
+ "PromptTokenCount"
+ "Puffy"
+ "Shiny"
+ "Stick"
+ "T@\"IADefaultsDataStore\",&,N,V_dataStore"
+ "TODO: Implement in each child class"
+ "TQ,N,V_state"
+ "[%{private}@] Publishing"
+ "[%{private}@] recordEngagementForToday: %@ %x->%x"
+ "[%{private}@] recordEngagementForToday: Failed to obtain daterange"
+ "[IATextInputActionsAnalytics] didCompositionReplacementForText:%{sensitive}@ withText:%{sensitive}@"
+ "[IATextInputActionsAnalytics] didDecompositionReplacementForText:%{sensitive}@ withText:%{sensitive}@"
+ "_dataStore"
+ "_state"
+ "analyzerVersion"
+ "com.apple.inputAnalytics.IASGenmojiUsageAnalyzer"
+ "com.apple.inputAnalytics.generatedEmojiEdits"
+ "com.apple.inputAnalytics.generatedEmojiUsage"
+ "conversationType"
+ "dataStore"
+ "didCompositionReplacementForText:withText:"
+ "didDecompositionReplacementForText:withText:"
+ "editType"
+ "editTypeFromPayload:"
+ "errorCodes"
+ "getDaterangeObjectWithName: Failed to obtain daterange with error: %{private}@"
+ "getDaterangeObjectWithName:dataStore:"
+ "handleGenmojiEditSignal:"
+ "handleGenmojiUsageSignal:"
+ "handleImageInsertedSignal:"
+ "imageTypeFromPayload:"
+ "init()"
+ "isSpecialCaseUsageSignal:"
+ "isUsageSignal:"
+ "recordEngagementForTodayWithDatastoreObjectName:"
+ "recordUsageForToday"
+ "setDataStore:"
+ "setState:"
+ "smart_reply.json"
+ "state"
+ "stringForState:"
+ "usageSourceFromPayload:"
+ "usageType"
+ "usageTypeEnum"
+ "usageTypeFromPayload:"
- "CandidateBarSuggestions"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "PeelAndStick"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
