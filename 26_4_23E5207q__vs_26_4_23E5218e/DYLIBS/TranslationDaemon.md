## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon`

```diff

-365.1.1.2.0
-  __TEXT.__text: 0x1aab04
-  __TEXT.__auth_stubs: 0x1780
-  __TEXT.__objc_methlist: 0x1a080
-  __TEXT.__const: 0x974
+365.3.1.0.0
+  __TEXT.__text: 0x1ad478
+  __TEXT.__auth_stubs: 0x1850
+  __TEXT.__objc_methlist: 0x1a0d0
+  __TEXT.__const: 0xa04
   __TEXT.__gcc_except_tab: 0x1b308
-  __TEXT.__cstring: 0x5f33
-  __TEXT.__oslogstring: 0xccd1
+  __TEXT.__cstring: 0x5f43
+  __TEXT.__oslogstring: 0xcdaf
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__swift5_typeref: 0x263
-  __TEXT.__swift5_capture: 0xbc
-  __TEXT.__constg_swiftt: 0xbc
+  __TEXT.__swift5_typeref: 0x31b
+  __TEXT.__swift5_capture: 0xd0
+  __TEXT.__constg_swiftt: 0x118
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_reflstr: 0x63
-  __TEXT.__swift5_fieldmd: 0xb0
+  __TEXT.__swift5_fieldmd: 0xd0
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__swift5_proto: 0x3c
-  __TEXT.__swift5_types: 0x14
+  __TEXT.__swift5_proto: 0x40
+  __TEXT.__swift5_types: 0x18
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0xf940
-  __TEXT.__eh_frame: 0x368
-  __TEXT.__objc_classname: 0x482e
-  __TEXT.__objc_methname: 0x1bd59
-  __TEXT.__objc_methtype: 0xe14d
-  __TEXT.__objc_stubs: 0x130c0
-  __DATA_CONST.__got: 0xe18
-  __DATA_CONST.__const: 0x41e0
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__unwind_info: 0xf980
+  __TEXT.__eh_frame: 0x3d0
+  __TEXT.__objc_classname: 0x484e
+  __TEXT.__objc_methname: 0x1be8e
+  __TEXT.__objc_methtype: 0xe1ed
+  __TEXT.__objc_stubs: 0x13140
+  __DATA_CONST.__got: 0xea8
+  __DATA_CONST.__const: 0x4248
   __DATA_CONST.__objc_classlist: 0x11c8
   __DATA_CONST.__objc_catlist: 0x138
-  __DATA_CONST.__objc_protolist: 0xf0
+  __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x69c0
+  __DATA_CONST.__objc_selrefs: 0x69e0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1120
   __DATA_CONST.__objc_arraydata: 0x3c0
-  __AUTH_CONST.__auth_got: 0xbd8
-  __AUTH_CONST.__const: 0xfa0
-  __AUTH_CONST.__cfstring: 0x7a60
-  __AUTH_CONST.__objc_const: 0x2cca8
+  __AUTH_CONST.__auth_got: 0xc40
+  __AUTH_CONST.__const: 0x1018
+  __AUTH_CONST.__cfstring: 0x7aa0
+  __AUTH_CONST.__objc_const: 0x2cda8
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0xa5d8
-  __AUTH.__data: 0x110
-  __DATA.__objc_ivar: 0x11c4
-  __DATA.__data: 0xd00
+  __AUTH.__data: 0x118
+  __DATA.__objc_ivar: 0x11cc
+  __DATA.__data: 0xd90
   __DATA.__bss: 0x8d0
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0xc58

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D391CD80-8F8D-380F-A898-2395BCDDEB15
-  Functions: 10306
-  Symbols:   34577
-  CStrings:  9305
+  UUID: 8B199B4B-923C-35F8-BB95-6E6000D9F696
+  Functions: 10328
+  Symbols:   34607
+  CStrings:  9323
 
Symbols:
+ +[MTSchemaMTFrameworkRequestSent(LTTranslationAdditions) lt_initWithFrameworkRequestId:qssSessionId:requestType:requestRoute:requestSize:modelVersion:]
+ +[_LTDSELFLoggingProduction frameworkRequestSentWithFrameworkRequestId:qssSessionId:requestType:requestRoute:requestSize:mtId:sessionId:modelVersion:]
+ +[_LTDSELFLoggingProduction frameworkRequestSentWithFrameworkRequestId:qssSessionId:requestType:requestRoute:requestSize:mtId:sessionId:modelVersion:].cold.1
+ -[_LTAIAdapterTranslationEngine initWithLocalePair:taskHint:selfLoggingManager:processIdentifier:]
+ -[_LTAIAdapterTranslationEngine processIdentifier]
+ -[_LTDLanguageAssetCache llmStatusDidChange:]
+ -[_LTDLanguageAssetCacheObserver wantsAIStatusUpdates]
+ -[_LTDSELFLoggingFrameworkRequest initWithInvocationId:endpoints:sessionIdProvider:qssSessionId:requestType:requestRoute:requestSize:modelVersion:]
+ -[_LTDSELFLoggingManager sendFrameworkRequestWithInvocationId:qssSessionId:requestType:requestRoute:requestSize:modelVersion:]
+ -[_LTDSELFLoggingManager sendFrameworkRequestWithInvocationId:qssSessionId:requestType:requestRoute:requestSize:modelVersion:].cold.1
+ _OBJC_IVAR_$__LTAIAdapterTranslationEngine._processIdentifier
+ _OBJC_IVAR_$__LTDLanguageAssetCache._llmStatus
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__LTDLLMBasedTranslationStatusDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES__LTDLLMBasedTranslationStatusDelegate
+ __OBJC_$_PROTOCOL_REFS__LTDLLMBasedTranslationStatusDelegate
+ __OBJC_LABEL_PROTOCOL_$__LTDLLMBasedTranslationStatusDelegate
+ __OBJC_PROTOCOL_$__LTDLLMBasedTranslationStatusDelegate
+ ___65-[_LTOfflineTranslationEngine _waitForLIDWithContext:completion:]_block_invoke.70
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.102
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.103
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.103.cold.1
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.103.cold.2
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.119
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.120
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.95
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.96
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke_2.121
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke_2.99
+ ___80-[_LTOfflineTranslationEngine translate:withContext:paragraphResult:completion:]_block_invoke.67
+ ___80-[_LTOfflineTranslationEngine translate:withContext:paragraphResult:completion:]_block_invoke.67.cold.1
+ ___85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.78
+ ___85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.78.cold.1
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ _keypath_get_selector_delegate
+ _objc_msgSend$canReportAILanguagesForObserver:
+ _objc_msgSend$frameworkRequestSentWithFrameworkRequestId:qssSessionId:requestType:requestRoute:requestSize:mtId:sessionId:modelVersion:
+ _objc_msgSend$initWithInvocationId:endpoints:sessionIdProvider:qssSessionId:requestType:requestRoute:requestSize:modelVersion:
+ _objc_msgSend$initWithLocalePair:taskHint:processIdentifier:
+ _objc_msgSend$initWithLocalePair:taskHint:selfLoggingManager:processIdentifier:
+ _objc_msgSend$llmStatusDidChange:
+ _objc_msgSend$lt_initWithFrameworkRequestId:qssSessionId:requestType:requestRoute:requestSize:modelVersion:
+ _objc_msgSend$sendFrameworkRequestWithInvocationId:qssSessionId:requestType:requestRoute:requestSize:modelVersion:
+ _objc_msgSend$setProcessIdentifier:
+ _objc_msgSend$wantsAIStatusUpdates
+ _swift_bridgeObjectRelease_n
+ _swift_deletedMethodError
+ _swift_stdlib_isStackAllocationSafe
+ _swift_unknownObjectWeakAssign
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _symbolic $s17TranslationDaemon012_LTDLLMBasedA15StatusProvidingP
+ _symbolic So29_LTDLLMBasedTranslationStatusCSgXw
+ _symbolic So29_LTDLLMBasedTranslationStatusCSgXwz_Xx
+ _symbolic _____ 17TranslationDaemon24DefaultLLMStatusProviderV
+ _symbolic ______pSg 17TranslationDaemon012_LTDLLMBasedA15StatusProvidingP
+ _symbolic _____y_____G s11_SetStorageC 16GenerativeModels0cD12AvailabilityV0E0O15UnavailableInfoV0F6ReasonO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 16GenerativeModels0dE12AvailabilityV0F0O15UnavailableInfoV0G6ReasonO
- +[MTSchemaMTFrameworkRequestSent(LTTranslationAdditions) lt_initWithFrameworkRequestId:qssSessionId:requestType:requestRoute:requestSize:]
- +[_LTDSELFLoggingProduction frameworkRequestSentWithFrameworkRequestId:qssSessionId:requestType:requestRoute:requestSize:mtId:sessionId:]
- +[_LTDSELFLoggingProduction frameworkRequestSentWithFrameworkRequestId:qssSessionId:requestType:requestRoute:requestSize:mtId:sessionId:].cold.1
- -[_LTAIAdapterTranslationEngine initWithLocalePair:taskHint:selfLoggingManager:]
- -[_LTDSELFLoggingFrameworkRequest initWithInvocationId:endpoints:sessionIdProvider:qssSessionId:requestType:requestRoute:requestSize:]
- -[_LTDSELFLoggingManager sendFrameworkRequestWithInvocationId:qssSessionId:requestType:requestRoute:requestSize:]
- -[_LTDSELFLoggingManager sendFrameworkRequestWithInvocationId:qssSessionId:requestType:requestRoute:requestSize:].cold.1
- __CLASS_METHODS__LTDLLMBasedTranslationStatus
- __CLASS_PROPERTIES__LTDLLMBasedTranslationStatus
- ___65-[_LTOfflineTranslationEngine _waitForLIDWithContext:completion:]_block_invoke.67
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.100.cold.1
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.100.cold.2
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.116
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.117
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.92
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.93
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.97
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.99
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke_2.118
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke_2.96
- ___80-[_LTOfflineTranslationEngine translate:withContext:paragraphResult:completion:]_block_invoke.64
- ___80-[_LTOfflineTranslationEngine translate:withContext:paragraphResult:completion:]_block_invoke.64.cold.1
- ___85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.75
- ___85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.75.cold.1
- ___block_literal_global.36
- ___swift_destroy_boxed_opaque_existential_0Tm
- __swift_stdlib_bridgeErrorToNSError
- _objc_msgSend$frameworkRequestSentWithFrameworkRequestId:qssSessionId:requestType:requestRoute:requestSize:mtId:sessionId:
- _objc_msgSend$initWithInvocationId:endpoints:sessionIdProvider:qssSessionId:requestType:requestRoute:requestSize:
- _objc_msgSend$initWithLocalePair:
- _objc_msgSend$initWithLocalePair:taskHint:selfLoggingManager:
- _objc_msgSend$lt_initWithFrameworkRequestId:qssSessionId:requestType:requestRoute:requestSize:
- _objc_msgSend$sendFrameworkRequestWithInvocationId:qssSessionId:requestType:requestRoute:requestSize:
CStrings:
+ "@\"_LTDLLMBasedTranslationStatus\""
+ "@40@0:8@16q24q32"
+ "@48@0:8@16q24@32q40"
+ "@64@0:8@16@24q32q40Q48@56"
+ "@80@0:8@16@24@32@40q48q56Q64@72"
+ "Can't report AI languages for observer because there's no `provider`; observer: %{public}@"
+ "Device is capable of Apple Intelligence: [%{bool,public}d]"
+ "Initializing _LTDStreamStabilizer with state %p and segments %{sensitive}@"
+ "Reporting empty LLM observations because feature flag is disabled"
+ "Reusing existing AI adapter engine since it supports this locale pair and the task hint and process identifier haven't changed"
+ "T@\"<_LTDLLMBasedTranslationStatusDelegate>\",N,W,Vdelegate"
+ "Tq,R,N,V_processIdentifier"
+ "_LTDLLMBasedTranslationStatusDelegate"
+ "_llmStatus"
+ "_processIdentifier"
+ "adapter.v1"
+ "canReportAILanguagesForObserver:"
+ "frameworkRequestSentWithFrameworkRequestId:qssSessionId:requestType:requestRoute:requestSize:mtId:sessionId:modelVersion:"
+ "initWithInvocationId:endpoints:sessionIdProvider:qssSessionId:requestType:requestRoute:requestSize:modelVersion:"
+ "initWithLocalePair:taskHint:processIdentifier:"
+ "initWithLocalePair:taskHint:selfLoggingManager:processIdentifier:"
+ "legacy"
+ "llmStatusDidChange:"
+ "lt_initWithFrameworkRequestId:qssSessionId:requestType:requestRoute:requestSize:modelVersion:"
+ "sendFrameworkRequestWithInvocationId:qssSessionId:requestType:requestRoute:requestSize:modelVersion:"
+ "setProcessIdentifier:"
+ "v24@0:8@\"_LTDLLMBasedTranslationStatus\"16"
+ "v80@0:8@\"SISchemaUUID\"16@\"NSString\"24q32q40Q48@\"SISchemaUUID\"56@\"SISchemaUUID\"64@\"NSString\"72"
+ "v80@0:8@16@24q32q40Q48@56@64@72"
+ "wantsAIStatusUpdates"
+ "\x91"
- "@56@0:8@16@24q32q40Q48"
- "@72@0:8@16@24@32@40q48q56Q64"
- "Can use LLM translation for observer: %{public}s"
- "Initializing _LTDStreamStabilizer with state %p and segments %{public}@"
- "Reusing existing AI adapter engine since it supports this locale pair and the task hasn't changed"
- "T@\"_LTDLLMBasedTranslationStatus\",N,R"
- "frameworkRequestSentWithFrameworkRequestId:qssSessionId:requestType:requestRoute:requestSize:mtId:sessionId:"
- "initWithInvocationId:endpoints:sessionIdProvider:qssSessionId:requestType:requestRoute:requestSize:"
- "initWithLocalePair:"
- "initWithLocalePair:taskHint:selfLoggingManager:"
- "lt_initWithFrameworkRequestId:qssSessionId:requestType:requestRoute:requestSize:"
- "sendFrameworkRequestWithInvocationId:qssSessionId:requestType:requestRoute:requestSize:"
- "v72@0:8@\"SISchemaUUID\"16@\"NSString\"24q32q40Q48@\"SISchemaUUID\"56@\"SISchemaUUID\"64"
- "v72@0:8@16@24q32q40Q48@56@64"
- "\x81"

```
