## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-64.503.0.0.0
-  __TEXT.__text: 0x34bc0
+64.504.0.0.0
+  __TEXT.__text: 0x35d48
   __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_methlist: 0x2864
+  __TEXT.__objc_methlist: 0x2964
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x2869
-  __TEXT.__oslogstring: 0x3c56
+  __TEXT.__cstring: 0x2929
+  __TEXT.__oslogstring: 0x3ca6
   __TEXT.__gcc_except_tab: 0x2a8
   __TEXT.__swift5_typeref: 0x115
   __TEXT.__swift5_capture: 0x88

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x9e0
+  __TEXT.__unwind_info: 0xa00
   __TEXT.__eh_frame: 0x2e8
-  __TEXT.__objc_classname: 0x545
-  __TEXT.__objc_methname: 0x643c
-  __TEXT.__objc_methtype: 0x852
-  __TEXT.__objc_stubs: 0x4d20
-  __DATA_CONST.__got: 0xb90
-  __DATA_CONST.__const: 0xa78
-  __DATA_CONST.__objc_classlist: 0x178
+  __TEXT.__objc_classname: 0x586
+  __TEXT.__objc_methname: 0x6664
+  __TEXT.__objc_methtype: 0x885
+  __TEXT.__objc_stubs: 0x4e80
+  __DATA_CONST.__got: 0xc48
+  __DATA_CONST.__const: 0xab0
+  __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15c0
+  __DATA_CONST.__objc_selrefs: 0x1618
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xf8
+  __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0xb8
   __AUTH_CONST.__auth_got: 0x650
   __AUTH_CONST.__auth_ptr: 0xd8
-  __AUTH_CONST.__const: 0x9b8
-  __AUTH_CONST.__cfstring: 0x2ae0
-  __AUTH_CONST.__objc_const: 0x47c0
+  __AUTH_CONST.__const: 0x9f8
+  __AUTH_CONST.__cfstring: 0x2b40
+  __AUTH_CONST.__objc_const: 0x4970
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__objc_intobj: 0x720
-  __AUTH.__objc_data: 0x4a0
+  __AUTH_CONST.__objc_intobj: 0x7e0
+  __AUTH.__objc_data: 0x540
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x354
+  __DATA.__objc_ivar: 0x360
   __DATA.__data: 0x3d8
-  __DATA.__bss: 0x130
+  __DATA.__bss: 0x140
   __DATA_DIRTY.__objc_data: 0xa50
   __DATA_DIRTY.__bss: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1201
-  Symbols:   495
-  CStrings:  1887
+  Functions: 1224
+  Symbols:   518
+  CStrings:  1913
 
Symbols:
+ _IAPayloadKeyImageGenerationBlockingCategory
+ _IAPayloadKeyImageGenerationBlockingInputOutputCategory
+ _IAPayloadKeyImageGenerationBlockingSubCategory
+ _IAPayloadValueGenmojiCreationFailReasonCancel
+ _IAPayloadValueGenmojiCreationFailReasonInputLanguage
+ _IAPayloadValueGenmojiCreationFailReasonInputLexicon
+ _IAPayloadValueGenmojiCreationFailReasonPolicyViolationDetectedFacesPolicy
+ _IAPayloadValueGenmojiUnspecified
+ _IAPayloadValueImageGenerationBlockingCategoryImageRejection
+ _IAPayloadValueImageGenerationBlockingCategoryPeoplePolicyViolation
+ _IAPayloadValueImageGenerationBlockingCategorySoftwareError
+ _IAPayloadValueImageGenerationBlockingCategoryTextPromptRejection
+ _IAPayloadValueImageGenerationBlockingInputOutputCategoryInput
+ _IAPayloadValueImageGenerationBlockingInputOutputCategoryOutput
+ _IAPayloadValueImageGenerationBlockingSubCategoryLexiconOrLanguage
+ _IAPayloadValueImageGenerationBlockingSubCategoryMultiplePeople
+ _IAPayloadValueImageGenerationBlockingSubCategoryUnexpectedPeopleInOutput
+ _IAPayloadValueImageGenerationBlockingSubCategoryUnspecified
+ _IAPayloadValueImageGenerationFeatureGenmoji
+ _IAPayloadValueImageGenerationFeatureImagePlayground
+ _IAPayloadValueImageGenerationFeatureImageWand
+ _IASignalImageGenerationPreviewGenerated
+ _IASignalImageGenerationPreviewNotGenerated
+ _OBJC_CLASS_$_BMWritingToolsComposeAndAdjust
- _IAPayloadKeyGenmojiCreationErrorDescription
CStrings:
+ "\x13"
+ "\x18\x11\x135U"
+ "%@"
+ "@\"BMWritingToolsComposeAndAdjust\""
+ "ComposeAndAdjust"
+ "IAImageGeneration"
+ "IASImageGenerationResultAnalyzer"
+ "IASImageGenerationResultAnalyzer.m"
+ "IASImageGenerationResultEvent"
+ "Obfuscating subcategory %{sensitive}@"
+ "Publishing"
+ "Q40@0:8@16@24Q32"
+ "T@\"BMWritingToolsComposeAndAdjust\",&,N,V_biomeWritingToolsComposeAndAdjust"
+ "WritingToolsFeatures"
+ "[%{private}@] Biome: Skip nil prompt"
+ "_biomeWritingToolsComposeAndAdjust"
+ "biomeWritingToolsComposeAndAdjust"
+ "com.apple.inputAnalytics.imageGenerationResult"
+ "com.apple.inputAnalytics.server.IASImageGenerationResultAnalyzer"
+ "featureForFeature:"
+ "generationResult"
+ "getObfuscatedFailureReasonString"
+ "initWithTimestamp:prompt:identifier:topic:userInterfaceLanguage:userSetRegionFormat:result:feature:"
+ "rejectionCategory"
+ "rejectionCategoryDetails"
+ "rejectionCategoryDetailsForBlockingSubCategory:"
+ "rejectionCategoryForBlockingCategory:"
+ "rejectionInputOutput"
+ "rejectionInputOutputForBlockingInputOutputCategory:"
+ "setBiomeWritingToolsComposeAndAdjust:"
+ "setValuesForKeysWithDictionary:"
+ "translateValue:withMapping:withDefaultValue:"
- "\x17\x11\x135U"
- "errorDescription"
- "genmojiCreationFailReasonToEnumMap"
- "shownFailReasonEnum"

```
