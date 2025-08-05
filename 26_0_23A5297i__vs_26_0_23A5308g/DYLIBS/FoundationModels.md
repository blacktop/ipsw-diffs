## FoundationModels

> `/System/Library/Frameworks/FoundationModels.framework/FoundationModels`

```diff

-1.0.44.1.101
-  __TEXT.__text: 0xa3280
-  __TEXT.__auth_stubs: 0x2c70
-  __TEXT.__const: 0x654c
-  __TEXT.__cstring: 0x2057
-  __TEXT.__swift5_typeref: 0x2024
-  __TEXT.__swift5_reflstr: 0x10ef
-  __TEXT.__swift5_assocty: 0x698
-  __TEXT.__swift5_fieldmd: 0x1bf0
-  __TEXT.__constg_swiftt: 0x158c
-  __TEXT.__swift5_builtin: 0x104
+1.0.48.2.0
+  __TEXT.__text: 0xb5ba0
+  __TEXT.__auth_stubs: 0x3000
+  __TEXT.__const: 0x8c5c
+  __TEXT.__cstring: 0x25ab
+  __TEXT.__swift5_typeref: 0x27bc
+  __TEXT.__swift5_reflstr: 0x14f5
+  __TEXT.__swift5_assocty: 0x818
+  __TEXT.__swift5_fieldmd: 0x27fc
+  __TEXT.__constg_swiftt: 0x1e84
+  __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__swift5_proto: 0x53c
-  __TEXT.__swift5_types: 0x228
-  __TEXT.__swift5_capture: 0xa9c
-  __TEXT.__swift5_mpenum: 0x80
-  __TEXT.__swift_as_entry: 0xe4
-  __TEXT.__swift_as_ret: 0x130
-  __TEXT.__oslogstring: 0x425
-  __TEXT.__unwind_info: 0x2218
-  __TEXT.__eh_frame: 0x4f28
-  __TEXT.__objc_methname: 0x1d9
-  __DATA_CONST.__got: 0x688
-  __DATA_CONST.__const: 0xe8
-  __DATA_CONST.__objc_classlist: 0x20
+  __TEXT.__swift5_proto: 0x788
+  __TEXT.__swift5_types: 0x318
+  __TEXT.__swift5_capture: 0x844
+  __TEXT.__swift5_mpenum: 0xa4
+  __TEXT.__swift_as_entry: 0x108
+  __TEXT.__swift_as_ret: 0x124
+  __TEXT.__oslogstring: 0x517
+  __TEXT.__unwind_info: 0x29c0
+  __TEXT.__eh_frame: 0x5cf8
+  __TEXT.__objc_methname: 0x1e0
+  __DATA_CONST.__got: 0x780
+  __DATA_CONST.__const: 0x108
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc8
-  __AUTH_CONST.__auth_got: 0x1638
-  __AUTH_CONST.__const: 0x5048
-  __AUTH_CONST.__objc_const: 0x460
-  __AUTH.__objc_data: 0x140
-  __AUTH.__data: 0xf98
-  __DATA.__data: 0x1640
-  __DATA.__bss: 0x8ee0
-  __DATA.__common: 0xa8
+  __DATA_CONST.__objc_selrefs: 0xd8
+  __AUTH_CONST.__auth_got: 0x1800
+  __AUTH_CONST.__const: 0x7098
+  __AUTH_CONST.__objc_const: 0x5e0
+  __AUTH.__objc_data: 0x1e0
+  __AUTH.__data: 0x1910
+  __DATA.__data: 0x1fb8
+  __DATA.__bss: 0xd950
+  __DATA.__common: 0xf0
   - /System/Library/Frameworks/BackgroundAssets.framework/BackgroundAssets
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML
   - /System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration
   - /System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 83DF9E80-BA52-3671-99C5-D5B28CC023AF
-  Functions: 2775
-  Symbols:   173
-  CStrings:  245
+  UUID: BC34B523-BB69-3996-9D13-2B5BA5381358
+  Functions: 3444
+  Symbols:   182
+  CStrings:  288
 
Symbols:
+ _MobileGestalt_copy_buildVersion_obj
+ _MobileGestalt_copy_marketingProductName_obj
+ _MobileGestalt_copy_productVersion_obj
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_internalBuild
+ _NSMultipleUnderlyingErrorsKey
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSHTTPURLResponse
+ _OBJC_CLASS_$_NSURLSession
+ _objc_retain_x25
+ _objc_retain_x26
+ _swift_dynamicCastObjCClassUnconditional
- _objc_retain_x23
- _swift_deletedAsyncMethodErrorTu
- _swift_getTupleTypeMetadata
CStrings:
+ "%s does not support tokenization"
+ "Compile adapter (dry run) response: %{public}s"
+ "Exceeded rate limit for compiling adapters. Please try again later."
+ "Expected 'type' to contain 'FoundationModels.LanguageModelFeedback'"
+ "Failed to check compilation status of the adapter"
+ "FoundationModels.LanguageModelFeedback"
+ "FoundationModels.LanguageModelSession.GenerationError"
+ "FoundationModels/GenerativeModelInferenceSession.swift"
+ "FoundationModels/ServerLanguageModel.swift"
+ "HTTP error with status code "
+ "Invalid request: "
+ "Invalid response received"
+ "Invalid streaming data received"
+ "OpenAI does not support greedy sampling"
+ "OpenAI does not support setting a random seed"
+ "OpenAI does not support top K sampling"
+ "ServerModelInferenceSession does not support PromptTemplate"
+ "Temperature (%{public}f) is out of range. It should be between %{public}f and %{public}f inclusive."
+ "The arguments to 'Tool' should be a struct or enum. '%s' takes 'arguments' of primitive type '%s', which may not be properly called by the model."
+ "Too many nested arrays or dictionaries."
+ "Tool definition '%{public}s' is found in transcript but its implementation is missing in 'tools'. '%{public}s' will be ignored in the new LanguageModelSession."
+ "You are not supposed to respond. Why should this request be handled with care? Reply with a short reason for refusal, in a friendly tone. Only provide explanations when you fully understand the previous interactions. Respond in English."
+ "_TtC16FoundationModels29AdapterCompilationRateLimiter"
+ "_TtCVOC16FoundationModels20LanguageModelSession15GenerationError7Refusal16TranscriptRecord"
+ "application/json"
+ "assistant"
+ "content"
+ "explanationStream"
+ "function"
+ "image_url"
+ "initWithDomain:code:userInfo:"
+ "json_schema"
+ "locale"
+ "max_completion_tokens"
+ "messages"
+ "rateLimitPerDay"
+ "rateLimitWindow"
+ "response_format"
+ "runtimeInformation"
+ "schemaAugmentor"
+ "sharedSession"
+ "state"
+ "statusCode"
+ "stream"
+ "system"
+ "temperature"
+ "text content "
+ "text/event-stream"
+ "textAugmentor"
+ "tool_call_id"
+ "tool_calls"
+ "top_p"
+ "v1/chat/completions"
- "Expected 'type' to contain 'FoundationModels.LanguageModelFeedbackAttachment'"
- "FoundationModels.LanguageModelFeedbackAttachment"
- "FoundationModels/InstructionsBuilder.swift"
- "FoundationModels/PromptBuilder.swift"
- "Temperature (%{public}f) is out of range. It should be between 0 and 2 inclusive."
- "Tool definition '%s' is found in transcript but its implementation is missing in 'tools'. '%s' will be ignored in the new LanguageModelSession."
- "Unhandled error streaming response: %@"
- "modelBundleID"
- "preferredLocalizationsFromArray:forPreferences:"
- "root dependencies "

```
