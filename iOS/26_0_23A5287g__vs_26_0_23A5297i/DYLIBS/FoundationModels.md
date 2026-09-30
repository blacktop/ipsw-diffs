## FoundationModels

> `/System/Library/Frameworks/FoundationModels.framework/FoundationModels`

```diff

-1.0.40.0.0
-  __TEXT.__text: 0x88098
-  __TEXT.__auth_stubs: 0x2af0
-  __TEXT.__const: 0x5de8
-  __TEXT.__cstring: 0x1edb
-  __TEXT.__swift5_typeref: 0x1e11
-  __TEXT.__swift5_reflstr: 0xf57
-  __TEXT.__swift5_assocty: 0x608
-  __TEXT.__swift5_fieldmd: 0x1a28
-  __TEXT.__constg_swiftt: 0x1370
-  __TEXT.__swift5_builtin: 0xf0
+1.0.44.1.101
+  __TEXT.__text: 0xa3280
+  __TEXT.__auth_stubs: 0x2c70
+  __TEXT.__const: 0x654c
+  __TEXT.__cstring: 0x2057
+  __TEXT.__swift5_typeref: 0x2024
+  __TEXT.__swift5_reflstr: 0x10ef
+  __TEXT.__swift5_assocty: 0x698
+  __TEXT.__swift5_fieldmd: 0x1bf0
+  __TEXT.__constg_swiftt: 0x158c
+  __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__swift5_proto: 0x514
-  __TEXT.__swift5_types: 0x204
-  __TEXT.__swift5_mpenum: 0x6c
-  __TEXT.__swift5_capture: 0x4d0
-  __TEXT.__swift_as_entry: 0x88
-  __TEXT.__swift_as_ret: 0xd8
-  __TEXT.__oslogstring: 0x1c2
-  __TEXT.__unwind_info: 0x1ed0
-  __TEXT.__eh_frame: 0x4490
-  __TEXT.__objc_methname: 0x1a6
-  __DATA_CONST.__got: 0x638
+  __TEXT.__swift5_proto: 0x53c
+  __TEXT.__swift5_types: 0x228
+  __TEXT.__swift5_capture: 0xa9c
+  __TEXT.__swift5_mpenum: 0x80
+  __TEXT.__swift_as_entry: 0xe4
+  __TEXT.__swift_as_ret: 0x130
+  __TEXT.__oslogstring: 0x425
+  __TEXT.__unwind_info: 0x2218
+  __TEXT.__eh_frame: 0x4f28
+  __TEXT.__objc_methname: 0x1d9
+  __DATA_CONST.__got: 0x688
   __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa0
-  __AUTH_CONST.__auth_got: 0x1578
-  __AUTH_CONST.__const: 0x4730
-  __AUTH_CONST.__objc_const: 0x440
+  __DATA_CONST.__objc_selrefs: 0xc8
+  __AUTH_CONST.__auth_got: 0x1638
+  __AUTH_CONST.__const: 0x5048
+  __AUTH_CONST.__objc_const: 0x460
   __AUTH.__objc_data: 0x140
-  __AUTH.__data: 0xf00
-  __DATA.__data: 0x1358
-  __DATA.__bss: 0x8a30
+  __AUTH.__data: 0xf98
+  __DATA.__data: 0x1640
+  __DATA.__bss: 0x8ee0
   __DATA.__common: 0xa8
   - /System/Library/Frameworks/BackgroundAssets.framework/BackgroundAssets
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4EDB11B5-8E09-3502-8DA7-5992D2E489AF
-  Functions: 2508
+  UUID: 83DF9E80-BA52-3671-99C5-D5B28CC023AF
+  Functions: 2775
   Symbols:   173
-  CStrings:  225
+  CStrings:  245
 
CStrings:
+ "\"sentiment\" : \"<SENTIMENT_ANALYSIS_PLACEHOLDER>\","
+ "\"sentiment\" : \"neutral\","
+ "%s"
+ "Compile adapter response: %{public}s"
+ "Dictionary<String, "
+ "Expected 'type' to contain 'FoundationModels.LanguageModelFeedbackAttachment'"
+ "Failed to compile draft model."
+ "Failed to load safety guardrails"
+ "FoundationModels/LanguageModelFeedbackAttachment.swift"
+ "Missing top level 'title' key containing the type's name"
+ "Safety guardrails were triggered. If this is unexpected, please use `LanguageModelSession.logFeedbackAttachment(sentiment:issues:desiredOutput:)` to export the feedback attachment and file a feedback report at https://feedbackassistant.apple.com. "
+ "Streamed response may contain sensitive or unsafe content"
+ "Tool definition '%s' is found in transcript but its implementation is missing in 'tools'. '%s' will be ignored in the new LanguageModelSession."
+ "XCODE_RUNNING_FOR_PLAYGROUNDS"
+ "You initialized a session with instructions and then used a prompt\ntemplate with it. The instructions passed in the initializer will be\nignored."
+ "_rejectedEntries"
+ "code"
+ "com.apple.tokengeneration"
+ "domain"
+ "setBackends:"
+ "setMode:"
+ "underlyingErrors"
- "Expected 'type' to contain 'FoundationModels.LanguageModelFeedbackAttachment', but it had 'Foo' instead"
- "Safety guardrail was triggered after consecutive failures during streaming."

```
