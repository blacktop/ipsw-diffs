## SiriInference

> `/System/Library/PrivateFrameworks/SiriInference.framework/SiriInference`

```diff

-3300.116.1.0.0
-  __TEXT.__text: 0x31eda0
-  __TEXT.__auth_stubs: 0x4f40
+3301.8.1.0.0
+  __TEXT.__text: 0x31e030
+  __TEXT.__auth_stubs: 0x4f60
   __TEXT.__objc_methlist: 0x4b8
-  __TEXT.__const: 0x1e320
-  __TEXT.__cstring: 0x1ea64
+  __TEXT.__const: 0x1e260
+  __TEXT.__cstring: 0x1e6b4
   __TEXT.__constg_swiftt: 0x88e0
-  __TEXT.__swift5_typeref: 0x7110
+  __TEXT.__swift5_typeref: 0x711c
   __TEXT.__swift5_builtin: 0x258
-  __TEXT.__swift5_reflstr: 0xe826
+  __TEXT.__swift5_reflstr: 0xe736
   __TEXT.__swift5_assocty: 0x1258
-  __TEXT.__swift5_capture: 0xcb0
-  __TEXT.__swift5_fieldmd: 0xea1c
-  __TEXT.__swift5_proto: 0x1d94
+  __TEXT.__swift5_capture: 0xcb4
+  __TEXT.__swift5_fieldmd: 0xe9a4
+  __TEXT.__swift5_proto: 0x1d88
   __TEXT.__swift5_types: 0xa2c
   __TEXT.__swift5_protos: 0x120
   __TEXT.__swift5_mpenum: 0x80
-  __TEXT.__unwind_info: 0xbdbc
-  __TEXT.__eh_frame: 0x130a8
+  __TEXT.__unwind_info: 0xbd54
+  __TEXT.__eh_frame: 0x13068
   __TEXT.__objc_classname: 0x9e
   __TEXT.__objc_methname: 0x4360
   __TEXT.__objc_methtype: 0x134

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x5fd8
   __DATA_CONST.__objc_selrefs: 0x16e8
-  __AUTH_CONST.__const: 0x1a3d8
+  __AUTH_CONST.__const: 0x1a378
   __AUTH_CONST.__auth_ptr: 0x8f0
   __AUTH_CONST.__objc_const: 0x3d0
-  __AUTH_CONST.__auth_got: 0x27a0
+  __AUTH_CONST.__auth_got: 0x27b0
   __AUTH.__data: 0x64b8
   __AUTH.__objc_data: 0x6c8
   __DATA.__objc_protorefs: 0x60
   __DATA.__objc_classrefs: 0x4b8
   __DATA.__objc_data: 0x98
-  __DATA.__data: 0xbfb8
-  __DATA.__bss: 0x344e0
+  __DATA.__data: 0xbfc0
+  __DATA.__bss: 0x34360
   __DATA.__common: 0x160
   __DATA_DIRTY.__objc_const: 0x48
   __DATA_DIRTY.__objc_data: 0xd40
-  __DATA_DIRTY.__data: 0x2ee0
+  __DATA_DIRTY.__data: 0x2ed0
   __DATA_DIRTY.__bss: 0xf00
   __DATA_DIRTY.__common: 0x208
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 22021
-  Symbols:   12904
-  CStrings:  3931
+  Functions: 22001
+  Symbols:   12889
+  CStrings:  3915
 
Symbols:
+ _OUTLINED_FUNCTION_112
+ _OUTLINED_FUNCTION_113
+ _symbolic Shy_____G 28SiriPrivateLearningInference20ContactSuggestionTagO
+ _symbolic _____ 13SiriInference17PLUSQueryExpanderV
+ _symbolic _____Sg 13SiriInference17PLUSQueryExpanderV
+ _symbolic ______pSg 28SiriPrivateLearningInference41PlusContactSuggestionStoreRuntimeQueryingP
- ___swift_memcpy10_1
- _associated conformance 13SiriInference0A26PrivateLearningFeatureFlagOSHAASQ
- _symbolic _____ 13SiriInference0A26PrivateLearningFeatureFlagO
- _symbolic _____Sg 28SiriPrivateLearningInference45PlusContactSuggestionStoreRuntimeQueryWrapperC
CStrings:
+ "PLUS: Here are the bundle ids: %s"
+ "PLUS: suggestion surfacing (phoneCall & messages) enabled by default "
+ "⚠️ Should only be set to FALSE in unit test mock to ignore Trial's ContactRanker model"
- "PICSRuntime"
- "PLUS: suggestion querying (all domains): false - Trial factor isPlusTrialEnabled"
- "PLUS: suggestion querying (all domains): true - OS supported. Feature flags enabled. Forcing PLUS on."
- "PLUS: suggestion querying (messages): %{bool}d - Trial factor isPlusTrialMessagesInferenceEnabled"
- "PLUS: suggestion querying (phoneCall): true - via Trial factor isPlusTrialEnabled"
- "PLUS: suggestion surfacing (all domains): false - PLUS disabled/request unsupported"
- "PLUS: suggestion surfacing (messages): %{bool}d - via Trial"
- "PLUS: suggestion surfacing (messages): true - via MESSAGES FEATURE FLAG"
- "PLUS: suggestion surfacing (phoneCall): %{bool}d - via Trial"
- "PLUS: suggestion surfacing (phoneCall): true - via PHONECALL FEATURE FLAG"
- "SiriPrivateLearning"
- "UsePLUSContactSuggestionsInMessages"
- "isPICSMessagesInferenceEnabled"
- "isPlusTrialEnabled"
- "isPlusTrialMessagesInferenceEnabled"
- "isPlusTrialMessagesSuggestionsEnabled"
- "isPlusTrialPhoneCallSuggestionsEnabled"
- "usePLUSContactSuggestions"
- "usePLUSContactSuggestionsInMessages"

```
