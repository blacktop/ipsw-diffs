## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-64.224.100.0.0
-  __TEXT.__text: 0x2c12c
-  __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_methlist: 0x219c
+64.309.0.0.0
+  __TEXT.__text: 0x2f26c
+  __TEXT.__auth_stubs: 0xaa0
+  __TEXT.__objc_methlist: 0x267c
   __TEXT.__const: 0x1c0
-  __TEXT.__cstring: 0x2449
-  __TEXT.__oslogstring: 0x3896
+  __TEXT.__cstring: 0x2419
+  __TEXT.__oslogstring: 0x3b36
   __TEXT.__gcc_except_tab: 0x2a8
-  __TEXT.__swift5_typeref: 0xa7
+  __TEXT.__swift5_typeref: 0xa9
   __TEXT.__swift5_capture: 0x88
   __TEXT.__constg_swiftt: 0x4c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x878
+  __TEXT.__swift_as_entry: 0x1c
+  __TEXT.__swift_as_ret: 0x1c
+  __TEXT.__unwind_info: 0x970
   __TEXT.__eh_frame: 0x2e8
-  __TEXT.__objc_classname: 0x49c
-  __TEXT.__objc_methname: 0x5973
-  __TEXT.__objc_methtype: 0x81a
-  __TEXT.__objc_stubs: 0x44c0
-  __DATA_CONST.__got: 0x9f0
-  __DATA_CONST.__const: 0x968
-  __DATA_CONST.__objc_classlist: 0x148
+  __TEXT.__objc_classname: 0x4eb
+  __TEXT.__objc_methname: 0x5f2b
+  __TEXT.__objc_methtype: 0x852
+  __TEXT.__objc_stubs: 0x4900
+  __DATA_CONST.__got: 0xa70
+  __DATA_CONST.__const: 0x9d8
+  __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12f0
+  __DATA_CONST.__objc_selrefs: 0x14a0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xe0
-  __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x578
+  __DATA_CONST.__objc_superrefs: 0xf0
+  __DATA_CONST.__objc_arraydata: 0x98
+  __AUTH_CONST.__auth_got: 0x560
   __AUTH_CONST.__auth_ptr: 0x90
-  __AUTH_CONST.__const: 0x7a8
-  __AUTH_CONST.__cfstring: 0x2580
-  __AUTH_CONST.__objc_const: 0x44f8
-  __AUTH_CONST.__objc_intobj: 0x570
-  __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH.__objc_data: 0x590
+  __AUTH_CONST.__const: 0x888
+  __AUTH_CONST.__cfstring: 0x27a0
+  __AUTH_CONST.__objc_const: 0x4450
+  __AUTH_CONST.__objc_intobj: 0x630
+  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __AUTH.__objc_data: 0x3b0
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x308
-  __DATA.__data: 0x350
-  __DATA.__bss: 0x120
-  __DATA_DIRTY.__objc_data: 0x780
-  __DATA_DIRTY.__bss: 0x100
+  __DATA.__objc_ivar: 0x334
+  __DATA.__data: 0x358
+  __DATA.__bss: 0xe0
+  __DATA_DIRTY.__objc_data: 0xa50
+  __DATA_DIRTY.__bss: 0x1b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/Anvil.framework/Anvil

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1019
-  Symbols:   444
-  CStrings:  1713
+  Functions: 1135
+  Symbols:   459
+  CStrings:  1793
 
Symbols:
+ _IAPayloadKeyFeedbackServiceRequestingBundleID
+ _IAPayloadKeyFeedbackServiceRequestingSceneID
+ _IAPayloadKeyGenmojiBundleID
+ _IAPayloadKeyGenmojiCreationErrorCode
+ _IAPayloadKeyGenmojiCreationErrorDomain
+ _IAPayloadKeyGenmojiUsageType
+ _IAPayloadKeyWritingToolsSystemPrompt
+ _IAPayloadValueGenmojiUsageTypePeel
+ _IAPayloadValueGenmojiUsageTypePeelCancel
+ _IAPayloadValueGenmojiUsageTypePeelCancelNoDrag
+ _IAPayloadValueGenmojiUsageTypeStick
+ _IAPayloadValueGenmojiUsageTypeTap
+ _IAPayloadValueGenmojiUsageTypeTapback
+ _IASignalWritingToolsHandoffRequested
+ _IASignalWritingToolsHandoffStarted
CStrings:
+ "\x03"
+ "\x16\x11\x134S"
+ "!\x15"
+ ", %@, %@, %@"
+ "@\"BMGeneratedImageUserInteraction\""
+ "@72@0:8q16@24@32q40@48@56@64"
+ "ERROR: Invalid special case for genmoji usage analyzer"
+ "IAGenmojiUsage"
+ "IASGenmojiAnalyzerFailureReason"
+ "IASGenmojiUsageAnalyzer"
+ "IASGenmojiUsageAnalyzer.m"
+ "IASGenmojiUsageEvent"
+ "InputAnalytics.IASGenmojiAnalyzerError"
+ "Not caching failure due to all args being nil"
+ "Received HandoffRequested with mode (%@) which is not supported."
+ "StickerKit.EmojiGenerationError"
+ "T@\"BMGeneratedImageUserInteraction\",&,N,V_biomeGeneratedImageUserInteraction"
+ "T@\"IADefaultsDataStore\",&,N,V_usageDataStore"
+ "T@\"NSMutableArray\",&,N,V_failureReasonArray"
+ "T@\"NSNumber\",C,N,V_errorCode"
+ "T@\"NSString\",C,N,V_errorDomain"
+ "T@\"NSString\",C,N,V_failureReasonPayloadValue"
+ "T@\"NSString\",C,N,V_handoffModel"
+ "T@\"NSString\",C,N,V_preHandoffFeatureDetails"
+ "TB,N,V_isActivelyGeneratingInitialImage"
+ "TB,N,V_isCached"
+ "TB,N,V_isFromHandoff"
+ "VisualGeneration.ImageCheckerError"
+ "VisualGeneration.PolicyViolationError"
+ "VisualGeneration.PromptError"
+ "VisualGeneration.TextSanitizer.Error"
+ "Y"
+ "[%{private}@] Biome: %{sensitive}@"
+ "[%{private}@] Edge detected, isCached was inconsistent for analyzer session %{private}@"
+ "[%{private}@] Failures: %{private}@"
+ "[%{private}@] Logging userCancelled"
+ "[%{private}@] Not logging userCancelled because not actively generating"
+ "[%{private}@] Set isActivelyGeneratingInitialImage"
+ "[%{private}@] Unset isActivelyGeneratingInitialImage"
+ "[%{private}@] handleResultsRequestedForMontara:isRefinement: payloads are malformed, neither Prompt nor SystemPrompt is present"
+ "_biomeGeneratedImageUserInteraction"
+ "_errorCode"
+ "_errorDomain"
+ "_failureReasonArray"
+ "_failureReasonPayloadValue"
+ "_handoffModel"
+ "_isActivelyGeneratingInitialImage"
+ "_isCached"
+ "_isFromHandoff"
+ "_preHandoffFeatureDetails"
+ "_usageDataStore"
+ "addFailureReasonToCache:errorDomain:errorCode:"
+ "attemptToCacheBundleId:"
+ "biomeGeneratedImageUserInteraction"
+ "com.apple.RealityKeyboard"
+ "com.apple.inputAnalytics.IASGenmojiUsageAnalyzer"
+ "com.apple.inputAnalytics.generatedEmojiUsage"
+ "errorCode"
+ "errorDomain"
+ "failureReasonArray"
+ "failureReasonPayloadValue"
+ "failureReasonSet"
+ "handleGenmojiUsageSignal:"
+ "handleHandoffRequestedForMontara:"
+ "handleHandoffStartedForMontara:"
+ "handleImageInsertedSignal:"
+ "handleResultsRequestedForMontara:isInitialRequest:"
+ "handoffModel"
+ "imageTypeFromPayload:"
+ "init()"
+ "initWithFeatureDomain:bundleId:sceneId:action:originalContent:generatedContent:modelInfo:"
+ "isActivelyGeneratingInitialImage"
+ "isFromHandoff"
+ "isSpecialCaseUsageSignal:"
+ "isUsageSignal:"
+ "lastObject"
+ "periodic24HourEventsWithModelAvailability: Failed to obtain usage datastore"
+ "periodic24HourEventsWithModelAvailability: Usage %x"
+ "periodic24HourEventsWithModelAvailability:dataStore:usageDataStore:eventHandler:"
+ "preHandoffFeatureDetails"
+ "sceneId"
+ "setBiomeGeneratedImageUserInteraction:"
+ "setErrorCode:"
+ "setErrorDomain:"
+ "setFailureReasonArray:"
+ "setFailureReasonPayloadValue:"
+ "setHandoffModel:"
+ "setIsActivelyGeneratingInitialImage:"
+ "setIsCached:"
+ "setIsFromHandoff:"
+ "setPreHandoffFeatureDetails:"
+ "setSceneId:"
+ "setUsageDataStore:"
+ "usageDataStore"
+ "usageSourceFromPayload:"
+ "usageType"
+ "usageTypeEnum"
+ "usageTypeFromPayload:"
+ "v48@0:8Q16@24@32@?40"
- "\x16\x11\x134Q"
- "!\x13"
- "@64@0:8q16@24q32@40@48@56"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T@\"NSMutableSet\",&,N,V_failureReasons"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_failureReasons"
- "failureReasons"
- "handleResultsRequestedForMontara:isRefinement:"
- "initWithFeatureDomain:bundleId:action:originalContent:generatedContent:modelInfo:"
- "invalid Collection: less than 'count' elements in collection"
- "setFailureReasons:"

```
