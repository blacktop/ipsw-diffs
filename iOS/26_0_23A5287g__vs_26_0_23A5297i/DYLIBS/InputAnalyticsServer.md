## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-95.0.0.0.0
-  __TEXT.__text: 0x3d7c8
+98.0.0.0.0
+  __TEXT.__text: 0x408ac
   __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_methlist: 0x336c
-  __TEXT.__const: 0x270
-  __TEXT.__cstring: 0x2e49
-  __TEXT.__oslogstring: 0x4166
-  __TEXT.__gcc_except_tab: 0x2f4
+  __TEXT.__objc_methlist: 0x36bc
+  __TEXT.__const: 0x2a0
+  __TEXT.__cstring: 0x30b9
+  __TEXT.__oslogstring: 0x4426
+  __TEXT.__gcc_except_tab: 0x5e0
   __TEXT.__swift5_typeref: 0x10d
   __TEXT.__swift5_capture: 0x98
   __TEXT.__constg_swiftt: 0x4c

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0xb68
+  __TEXT.__unwind_info: 0xc28
   __TEXT.__eh_frame: 0x310
-  __TEXT.__objc_classname: 0x778
-  __TEXT.__objc_methname: 0x7a2d
-  __TEXT.__objc_methtype: 0xaf7
-  __TEXT.__objc_stubs: 0x5e80
-  __DATA_CONST.__got: 0xdf8
-  __DATA_CONST.__const: 0xc98
-  __DATA_CONST.__objc_classlist: 0x210
+  __TEXT.__objc_classname: 0x7d5
+  __TEXT.__objc_methname: 0x8364
+  __TEXT.__objc_methtype: 0xbcb
+  __TEXT.__objc_stubs: 0x6600
+  __DATA_CONST.__got: 0xe48
+  __DATA_CONST.__const: 0xdd0
+  __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a70
+  __DATA_CONST.__objc_selrefs: 0x1c60
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x170
-  __DATA_CONST.__objc_arraydata: 0xb8
+  __DATA_CONST.__objc_superrefs: 0x178
+  __DATA_CONST.__objc_arraydata: 0xe8
   __AUTH_CONST.__auth_got: 0x658
-  __AUTH_CONST.__const: 0xae8
-  __AUTH_CONST.__cfstring: 0x3260
-  __AUTH_CONST.__objc_const: 0x5e80
-  __AUTH_CONST.__objc_intobj: 0xbd0
-  __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH.__objc_data: 0x8d8
+  __AUTH_CONST.__const: 0xb88
+  __AUTH_CONST.__cfstring: 0x3460
+  __AUTH_CONST.__objc_const: 0x6370
+  __AUTH_CONST.__objc_intobj: 0xc00
+  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH.__objc_data: 0x978
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x438
+  __DATA.__objc_ivar: 0x488
   __DATA.__data: 0x3b0
-  __DATA.__bss: 0x130
+  __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0xc08
   __DATA_DIRTY.__data: 0x48
   __DATA_DIRTY.__bss: 0x200

   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService
+  - /System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/GenerativeAssistantSettings
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics
   - /System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EF96A248-EFDA-3B91-B340-89EB45C3790F
-  Functions: 1438
-  Symbols:   570
-  CStrings:  2629
+  UUID: 4E4FD570-CBB2-3060-8389-3BB60DEDFBC0
+  Functions: 1528
+  Symbols:   580
+  CStrings:  2785
 
Symbols:
+ _IAPayloadKeyImageGenerationIngredientTypeAccessories
+ _IAPayloadKeyImageGenerationIngredientTypeAdditionalDescription
+ _IAPayloadKeyImageGenerationIngredientTypeFacialHair
+ _IAPayloadKeyImageGenerationIngredientTypeHair
+ _IAPayloadKeyImageGenerationInputTokenCount
+ _IASignalImageGenerationRewriteEnded
+ _IASignalImageGenerationRewriteFailed
+ _IASignalImageGenerationRewriteStarted
+ _IASignalImageGenerationStartGenerationPreviewStream
+ _OBJC_CLASS_$_GATSettings
CStrings:
+ "5"
+ "@\"IASImageGenerationCreationAnalyzer\""
+ "@\"IASImageGenerationPreviewImageModel\""
+ "@\"IASImageGenerationVGFResultModel\""
+ "@32@0:8@16Q24"
+ "@?24@0:8Q16"
+ "@?32@0:8Q16Q24"
+ "B16@?0Q8"
+ "Error enumerating details event for image %lu"
+ "Error getting reference to parent analyzer in consumeSignal for signal %{private}@ for some image"
+ "Error getting reference to parent analyzer in enumerateAnalyticsForSignal for signal %{private}@ for some image"
+ "Error getting reference to parent image in enumerateAnalyticsForSignal for signal %{private}@ for some image"
+ "Error getting reference to parent in willAcceptSignal for signal %{private}@ for image %lu"
+ "GenerativeAssistant.visualIntelligenceCamera"
+ "IASImageGenerationPreviewImageModel"
+ "IASImageGenerationPreviewImageModelStateFilters"
+ "IASImageGenerationVGFResultModel"
+ "Q20@0:8B16"
+ "T@\"IASAnalyzerErrors\",&,N,V_imageLevelErrors"
+ "T@\"IASAnalyzerErrors\",&,N,V_resultLevelErrors"
+ "T@\"IASImageGenerationCreationAnalyzer\",W,N,V_parentAnalyzer"
+ "T@\"IASImageGenerationPreviewImageModel\",W,N,V_parentImage"
+ "T@\"IASImageGenerationVGFResultModel\",&,N,V_vgfResultModel"
+ "T@\"NSDate\",&,N,V_rewriteStartTime"
+ "T@\"NSDate\",&,N,V_totalGenerationStartTime"
+ "T@\"NSDate\",&,N,V_vgfStartTime"
+ "T@\"NSNumber\",C,N,V_tokenCount"
+ "T@\"NSString\",C,N,V_accessoriesModifier"
+ "T@\"NSString\",C,N,V_additionalDescriptionModifier"
+ "T@\"NSString\",C,N,V_faceModifier"
+ "T@\"NSString\",C,N,V_hairModifier"
+ "TB,N,V_foundVGFLatency"
+ "TQ,N,V_previewIndex"
+ "Td,N,V_rewriteRuntime"
+ "Td,N,V_totalGenerationRuntime"
+ "Td,N,V_vgfRuntime"
+ "V"
+ "[%{private}@] Enumerating details event for standalone VGF model"
+ "[%{private}@] ignoring signal %{private}@ for image %lu"
+ "[%{private}@] ignoring signal %{private}@ for standalone VGF model"
+ "_accessoriesModifier"
+ "_additionalDescriptionModifier"
+ "_faceModifier"
+ "_foundVGFLatency"
+ "_hairModifier"
+ "_imageLevelErrors"
+ "_parentAnalyzer"
+ "_parentImage"
+ "_previewIndex"
+ "_resultLevelErrors"
+ "_rewriteRuntime"
+ "_rewriteStartTime"
+ "_tokenCount"
+ "_totalGenerationRuntime"
+ "_totalGenerationStartTime"
+ "_vgfResultModel"
+ "_vgfRuntime"
+ "_vgfStartTime"
+ "accessoriesModifier"
+ "accountTypeToMontaraAccount:"
+ "additionalDescriptionModifier"
+ "appleIntelligenceSettings"
+ "between:and:"
+ "bridgeAvailabilityToCameraIntelligence:"
+ "com.apple.Settings.AppleIntelligence"
+ "com.apple.VisualIntelligence.structuredExtraction.addToCalendar"
+ "com.apple.VisualIntelligenceCamera.ImageSearch"
+ "com.apple.VisualIntelligenceCamera.featureAwareness"
+ "com.apple.inputAnalytics.server.IASImageGenerationPreviewImageModel"
+ "com.apple.inputAnalytics.server.IASImageGenerationVGFResultModel"
+ "consumeSignal:"
+ "enumValueForBool:"
+ "enumerateAnalyticsForSignal:"
+ "equalTo:"
+ "faceHairModifier"
+ "faceModifier"
+ "featureAwareness"
+ "foundVGFLatency"
+ "hairModifier"
+ "handleImageIndexedSignal:onValidIndex:"
+ "handlePreviewGeneratedSignal:"
+ "handlePreviewGenerationStartedSignal:"
+ "handlePreviewNotGeneratedSignal:"
+ "handleRetryRequestedSignal:"
+ "imageLevelErrors"
+ "initWithParentAnalyzer:WithParentImage:"
+ "initWithParentAnalyzer:WithPreviewIndex:"
+ "isGenerating"
+ "lessThan:"
+ "montaraSettings"
+ "parentAnalyzer"
+ "parentImage"
+ "periodic24HourEvents: IASVICameraDailyAnalytics: Caught %{private}@"
+ "resetVGFModel"
+ "resultLevelErrors"
+ "rewriteLatency"
+ "rewriteLatencyRaw"
+ "rewriteRuntime"
+ "rewriteStartTime"
+ "sendSignal:ToFirstImageMatchingFilter:WithErrorCode:"
+ "sendSignalToAllPreviewImageModels:"
+ "sendSignalToCurrentPreviewImageModel:"
+ "setAccessoriesModifier:"
+ "setAdditionalDescriptionModifier:"
+ "setFaceModifier:"
+ "setFoundVGFLatency:"
+ "setHairModifier:"
+ "setImageLevelErrors:"
+ "setParentAnalyzer:"
+ "setParentImage:"
+ "setPreviewIndex:"
+ "setResultLevelErrors:"
+ "setRewriteRuntime:"
+ "setRewriteStartTime:"
+ "setTokenCount:"
+ "setTotalGenerationRuntime:"
+ "setTotalGenerationStartTime:"
+ "setVgfResultModel:"
+ "setVgfRuntime:"
+ "setVgfStartTime:"
+ "sssAppleIntelligenceSettingsValue"
+ "sssFeatureAwarenessValue"
+ "sssMontaraAccountValue"
+ "sssMontaraSettingsValue"
+ "summarization.visualIntelligenceCamera"
+ "terminateWithGenerationStatus:WithEndTimestamp:"
+ "textComposition.OpenEndedSchema"
+ "tokenCount"
+ "totalGenerationLatency"
+ "totalGenerationLatencyInMs"
+ "totalGenerationLatencyRaw"
+ "totalGenerationRuntime"
+ "totalGenerationStartTime"
+ "totalRewriteLatencyInMs"
+ "totalVgfLatencyInMs"
+ "updateTotalGenerationRuntimeWithEndTimestamp:"
+ "updateVGFRuntimeWithEndTimestamp:"
+ "v16@?0@\"NSNumber\"8"
+ "v32@0:8@16@?24"
+ "v32@0:8Q16@24"
+ "v40@0:8@16@?24@32"
+ "vgfLatency"
+ "vgfResultModel"
+ "vgfRuntime"
+ "vgfStartTime"
- "IASImageGenerationImageDetails"
- "Stray generation result"
- "currentlyViewedImageDetails"
- "enumerateImageLevelAnalytics"
- "enumeratePromptLevelAnalytics"
- "enumerateResultLevelAnalytics:"
- "updateImageDetailsIfGeneratingWithGenerationStatus:"

```
