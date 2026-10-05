## InputAnalytics

> `/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics`

```diff

-154.1.5.0.0
-  __TEXT.__text: 0x1f008
-  __TEXT.__objc_methlist: 0x26fc
+154.1.8.0.0
+  __TEXT.__text: 0x1f6a8
+  __TEXT.__objc_methlist: 0x27bc
   __TEXT.__const: 0x32a
   __TEXT.__gcc_except_tab: 0x384
-  __TEXT.__cstring: 0x61c2
-  __TEXT.__oslogstring: 0x27ac
+  __TEXT.__cstring: 0x6602
+  __TEXT.__oslogstring: 0x27fc
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x8b
   __TEXT.__constg_swiftt: 0x4c

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__unwind_info: 0xce8
+  __TEXT.__unwind_info: 0xd18
   __TEXT.__eh_frame: 0x308
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2000
-  __DATA_CONST.__objc_classlist: 0x1c0
+  __DATA_CONST.__const: 0x21d8
+  __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1260
+  __DATA_CONST.__objc_selrefs: 0x12a0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x100
+  __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0xea0
-  __DATA_CONST.__got: 0x280
+  __DATA_CONST.__got: 0x288
   __AUTH_CONST.__const: 0x648
-  __AUTH_CONST.__cfstring: 0x94c0
-  __AUTH_CONST.__objc_const: 0x4238
-  __AUTH_CONST.__objc_intobj: 0x1260
+  __AUTH_CONST.__cfstring: 0x9b00
+  __AUTH_CONST.__objc_const: 0x4338
+  __AUTH_CONST.__objc_intobj: 0x12a8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x4a8
-  __AUTH.__objc_data: 0xa70
+  __AUTH.__objc_data: 0xa98
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x234
+  __DATA.__objc_ivar: 0x23c
   __DATA.__data: 0x300
-  __DATA_DIRTY.__objc_data: 0x730
+  __DATA_DIRTY.__objc_data: 0x758
   __DATA_DIRTY.__bss: 0xe8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1051
-  Symbols:   2687
-  CStrings:  1386
+  Functions: 1067
+  Symbols:   2771
+  CStrings:  1437
 
Symbols:
+ +[IATextInputActionsSessionKeyboardLatencyAction(NSSecureCoding) supportsSecureCoding]
+ -[IATextInputActionsAnalytics didMeasureKeyboardLatency:]
+ -[IATextInputActionsAnalytics(TestingSupport) setFlushedActionObserver:]
+ -[IATextInputActionsSessionAction asKeyboardLatency]
+ -[IATextInputActionsSessionKeyboardLatencyAction .cxx_destruct]
+ -[IATextInputActionsSessionKeyboardLatencyAction changedContent]
+ -[IATextInputActionsSessionKeyboardLatencyAction description]
+ -[IATextInputActionsSessionKeyboardLatencyAction inputActionCount]
+ -[IATextInputActionsSessionKeyboardLatencyAction keystrokeLatenciesMsByInputType]
+ -[IATextInputActionsSessionKeyboardLatencyAction setKeystrokeLatenciesMsByInputType:]
+ -[IATextInputActionsSessionKeyboardLatencyAction(NSSecureCoding) encodeWithCoder:]
+ -[IATextInputActionsSessionKeyboardLatencyAction(NSSecureCoding) initFromDictionary:]
+ -[IATextInputActionsSessionKeyboardLatencyAction(NSSecureCoding) initWithCoder:]
+ -[IATextInputActionsSessionKeyboardLatencyAction(NSSecureCoding) toDictionary]
+ _IAPayloadKeyImageGenerationBlockingSafetyModel
+ _IAPayloadKeyImageGenerationFailureReason
+ _IAPayloadKeyImageGenerationStyleEnum
+ _IAPayloadValueGenmojiUsageSourceFindAndReplace
+ _IAPayloadValueGenmojiUsageSourcePreGenerated
+ _IAPayloadValueGenmojiUsageTypeDelete
+ _IAPayloadValueGenmojiUsageTypeFindAndReplaceAccepted
+ _IAPayloadValueGenmojiUsageTypeFindAndReplaceHighlightShown
+ _IAPayloadValueGenmojiUsageTypeFindAndReplaceSuggestionShown
+ _IAPayloadValueGenmojiUsageTypeOther
+ _IAPayloadValueGenmojiUsageTypeShare
+ _IAPayloadValueImageGenerationBlockingSafetyModelMultimodalGuardrail
+ _IAPayloadValueImageGenerationBlockingSafetyModelPixelGuardrail
+ _IAPayloadValueImageGenerationBlockingSafetyModelTextGuardrail
+ _IAPayloadValueImageGenerationBlockingSafetyModelUnspecified
+ _IAPayloadValueImageGenerationFailureReasonBlocklistCategoryAppleProducts
+ _IAPayloadValueImageGenerationFailureReasonBlocklistCategoryBlocklistDrugs
+ _IAPayloadValueImageGenerationFailureReasonBlocklistCategoryCopyright
+ _IAPayloadValueImageGenerationFailureReasonBlocklistCategoryCustomWords
+ _IAPayloadValueImageGenerationFailureReasonBlocklistCategoryDesecration
+ _IAPayloadValueImageGenerationFailureReasonBlocklistCategoryMinor
+ _IAPayloadValueImageGenerationFailureReasonBlocklistCategoryPersonalization
+ _IAPayloadValueImageGenerationFailureReasonExternalGeneratorNetworkFailure
+ _IAPayloadValueImageGenerationFailureReasonExternalGeneratorRateLimited
+ _IAPayloadValueImageGenerationFailureReasonLexiconOrLanguage
+ _IAPayloadValueImageGenerationFailureReasonModelsDownloading
+ _IAPayloadValueImageGenerationFailureReasonPCCErrors
+ _IAPayloadValueImageGenerationFailureReasonPCCNoNodesAvailable
+ _IAPayloadValueImageGenerationFailureReasonSWErrors
+ _IAPayloadValueImageGenerationFailureReasonSafetyCategoryCSEAI
+ _IAPayloadValueImageGenerationFailureReasonSafetyCategoryCopyright
+ _IAPayloadValueImageGenerationFailureReasonSafetyCategoryDrugs
+ _IAPayloadValueImageGenerationFailureReasonSafetyCategoryHarassment
+ _IAPayloadValueImageGenerationFailureReasonSafetyCategoryHate
+ _IAPayloadValueImageGenerationFailureReasonSafetyCategoryIdentityEditing
+ _IAPayloadValueImageGenerationFailureReasonSafetyCategoryMapsAndFlags
+ _IAPayloadValueImageGenerationFailureReasonSafetyCategoryNudity
+ _IAPayloadValueImageGenerationFailureReasonSafetyCategoryOffensive
+ _IAPayloadValueImageGenerationFailureReasonSafetyCategoryPhotorealism
+ _IAPayloadValueImageGenerationFailureReasonSafetyCategoryPublicFigure
+ _IAPayloadValueImageGenerationFailureReasonSafetyCategoryRacy
+ _IAPayloadValueImageGenerationFailureReasonSafetyCategorySelfHarm
+ _IAPayloadValueImageGenerationFailureReasonSafetyCategorySuggestive
+ _IAPayloadValueImageGenerationFailureReasonSafetyCategoryTerrorism
+ _IAPayloadValueImageGenerationFailureReasonSafetyCategoryToxic
+ _IAPayloadValueImageGenerationFailureReasonSafetyCategoryViolenceAndGore
+ _IAPayloadValueImageGenerationFailureReasonUnspecified
+ _IASignalSmartRepliesMailFormattingBarIntentDismissed
+ _IASignalSmartRepliesMailFormattingBarIntentEngaged
+ _IASignalSmartRepliesMailFormattingBarIntentShown
+ _IASignalWritingToolsMailFormattingBarActionDismissed
+ _IASignalWritingToolsMailFormattingBarActionEngaged
+ _IASignalWritingToolsMailFormattingBarActionShown
+ _IATextInputActionsKeyboardTypeFloating
+ _IATextInputActionsKeyboardTypeHardware
+ _IATextInputActionsKeyboardTypeLandscape
+ _IATextInputActionsKeyboardTypePortrait
+ _IATextInputActionsKeyboardTypeSplit
+ _IATextInputActionsKeyboardTypeWebSuffix
+ _OBJC_CLASS_$_IATextInputActionsSessionKeyboardLatencyAction
+ _OBJC_IVAR_$_IATextInputActionsAnalytics._flushedActionObserver
+ _OBJC_IVAR_$_IATextInputActionsSessionKeyboardLatencyAction._keystrokeLatenciesMsByInputType
+ _OBJC_METACLASS_$_IATextInputActionsSessionKeyboardLatencyAction
+ __OBJC_$_CLASS_METHODS_IATextInputActionsSessionKeyboardLatencyAction(NSSecureCoding)
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionKeyboardLatencyAction(NSSecureCoding)
+ __OBJC_$_INSTANCE_VARIABLES_IATextInputActionsSessionKeyboardLatencyAction
+ __OBJC_$_PROP_LIST_IATextInputActionsSessionKeyboardLatencyAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionKeyboardLatencyAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionKeyboardLatencyAction
+ ___57-[IATextInputActionsAnalytics didMeasureKeyboardLatency:]_block_invoke
CStrings:
+ ", latencyInputTypeCount=%lu, latencySampleCount=%lu"
+ "BlockingSafetyModel"
+ "BlocklistAppleProducts"
+ "BlocklistCopyright"
+ "BlocklistCustomWords"
+ "BlocklistDesecration"
+ "BlocklistDrugs"
+ "BlocklistMinor"
+ "BlocklistPersonalization"
+ "FindAndReplace"
+ "FindAndReplaceAccepted"
+ "FindAndReplaceHighlightShown"
+ "FindAndReplaceSuggestionShown"
+ "Floating"
+ "Hardware"
+ "Landscape"
+ "MailFormattingBarActionDismissed"
+ "MailFormattingBarActionEngaged"
+ "MailFormattingBarActionShown"
+ "MailFormattingBarIntentDismissed"
+ "MailFormattingBarIntentEngaged"
+ "MailFormattingBarIntentShown"
+ "ModelsDownloading"
+ "MultimodalGuardrail"
+ "PCCErrors"
+ "PCCNoNodesAvailable"
+ "PixelGuardrail"
+ "PreGenerated"
+ "SWErrors"
+ "SafetyCategoryCSEAI"
+ "SafetyCategoryCopyright"
+ "SafetyCategoryDrugs"
+ "SafetyCategoryHarassment"
+ "SafetyCategoryHate"
+ "SafetyCategoryIdentityEditing"
+ "SafetyCategoryMapsAndFlags"
+ "SafetyCategoryNudity"
+ "SafetyCategoryOffensive"
+ "SafetyCategoryPhotorealism"
+ "SafetyCategoryPublicFigure"
+ "SafetyCategoryRacy"
+ "SafetyCategorySelfHarm"
+ "SafetyCategorySuggestive"
+ "SafetyCategoryTerrorism"
+ "SafetyCategoryToxic"
+ "SafetyCategoryViolenceAndGore"
+ "Split"
+ "StyleEnum"
+ "TextGuardrail"
+ "[IATextInputActionsAnalytics] didMeasureKeyboardLatency with %lu input types"
+ "keystrokeLatenciesMsByInputType"
```
