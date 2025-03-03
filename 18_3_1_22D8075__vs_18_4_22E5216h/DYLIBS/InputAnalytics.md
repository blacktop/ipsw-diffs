## InputAnalytics

> `/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics`

```diff

-64.224.100.0.0
-  __TEXT.__text: 0x1f3a4
-  __TEXT.__auth_stubs: 0x860
-  __TEXT.__objc_methlist: 0x2320
+64.313.1.0.0
+  __TEXT.__text: 0x21d8c
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_methlist: 0x27fc
   __TEXT.__const: 0x282
+  __TEXT.__cstring: 0x4922
   __TEXT.__gcc_except_tab: 0x468
-  __TEXT.__oslogstring: 0x29f0
-  __TEXT.__cstring: 0x48c2
+  __TEXT.__oslogstring: 0x2bb0
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x8a
+  __TEXT.__swift5_typeref: 0x8c
   __TEXT.__swift5_capture: 0x88
   __TEXT.__constg_swiftt: 0x4c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x8a0
+  __TEXT.__swift_as_entry: 0x1c
+  __TEXT.__swift_as_ret: 0x1c
+  __TEXT.__unwind_info: 0x978
   __TEXT.__eh_frame: 0x2e8
-  __TEXT.__objc_classname: 0x715
-  __TEXT.__objc_methname: 0x4d31
+  __TEXT.__objc_classname: 0x79b
+  __TEXT.__objc_methname: 0x4f43
   __TEXT.__objc_methtype: 0xa60
-  __TEXT.__objc_stubs: 0x3100
-  __DATA_CONST.__got: 0x248
-  __DATA_CONST.__const: 0x12e8
-  __DATA_CONST.__objc_classlist: 0x1c0
+  __TEXT.__objc_stubs: 0x3360
+  __DATA_CONST.__got: 0x250
+  __DATA_CONST.__const: 0x1440
+  __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1108
+  __DATA_CONST.__objc_selrefs: 0x1230
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x120
+  __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0xdb0
-  __AUTH_CONST.__auth_got: 0x440
+  __AUTH_CONST.__auth_got: 0x420
   __AUTH_CONST.__auth_ptr: 0x28
-  __AUTH_CONST.__const: 0x518
-  __AUTH_CONST.__cfstring: 0x6ac0
-  __AUTH_CONST.__objc_const: 0x48d8
-  __AUTH_CONST.__objc_intobj: 0x840
+  __AUTH_CONST.__const: 0x678
+  __AUTH_CONST.__cfstring: 0x6ee0
+  __AUTH_CONST.__objc_const: 0x4670
+  __AUTH_CONST.__objc_intobj: 0x9c0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x7f0
+  __AUTH.__objc_data: 0x930
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x24c
+  __DATA.__objc_ivar: 0x254
   __DATA.__data: 0x370
+  __DATA.__bss: 0x190
   __DATA.__common: 0x8
-  __DATA.__bss: 0x100
-  __DATA_DIRTY.__objc_data: 0x9b0
-  __DATA_DIRTY.__bss: 0xa8
+  __DATA_DIRTY.__objc_data: 0xa00
+  __DATA_DIRTY.__bss: 0xc8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 963
-  Symbols:   629
-  CStrings:  2114
+  Functions: 1073
+  Symbols:   653
+  CStrings:  2173
 
Symbols:
+ _IAPayloadKeyFeedbackServiceRequestingBundleID
+ _IAPayloadKeyFeedbackServiceRequestingSceneID
+ _IAPayloadKeyGenmojiBundleID
+ _IAPayloadKeyGenmojiCreationErrorCode
+ _IAPayloadKeyGenmojiCreationErrorDomain
+ _IAPayloadKeySmartRepliesConversationType
+ _IAPayloadKeySmartRepliesInputLanguage
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
+ "Message"
+ "Original"
+ "Outline"
+ "Peel"
+ "PeelCancel"
+ "PeelCancelNoDrag"
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
