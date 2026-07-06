## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/Versions/A/TranslationDaemon`

```diff

-  __TEXT.__text: 0x1bbb94
-  __TEXT.__objc_methlist: 0x1a268
-  __TEXT.__const: 0xaca
-  __TEXT.__gcc_except_tab: 0x1b398
-  __TEXT.__cstring: 0x631b
-  __TEXT.__oslogstring: 0xd5a0
+  __TEXT.__text: 0x1b8f48
+  __TEXT.__objc_methlist: 0x1a2d8
+  __TEXT.__const: 0xaba
+  __TEXT.__gcc_except_tab: 0x1b3a0
+  __TEXT.__cstring: 0x632b
+  __TEXT.__oslogstring: 0xd670
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__swift5_typeref: 0x392
+  __TEXT.__swift5_typeref: 0x374
   __TEXT.__swift5_capture: 0xe0
   __TEXT.__constg_swiftt: 0x154
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__swift_as_cont: 0x14
+  __TEXT.__swift_as_cont: 0x10
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xfa28
-  __TEXT.__eh_frame: 0x400
+  __TEXT.__unwind_info: 0xfa60
+  __TEXT.__eh_frame: 0x388
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1748
+  __DATA_CONST.__const: 0x17a0
   __DATA_CONST.__objc_classlist: 0x11d8
-  __DATA_CONST.__objc_catlist: 0x138
+  __DATA_CONST.__objc_catlist: 0x140
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6ab0
+  __DATA_CONST.__objc_selrefs: 0x6b08
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1120
-  __DATA_CONST.__objc_arraydata: 0x3c0
-  __DATA_CONST.__got: 0xee8
-  __AUTH_CONST.__const: 0x41c8
-  __AUTH_CONST.__cfstring: 0x7ae0
-  __AUTH_CONST.__objc_const: 0x2d038
+  __DATA_CONST.__objc_arraydata: 0x3c8
+  __DATA_CONST.__got: 0xed8
+  __AUTH_CONST.__const: 0x41f8
+  __AUTH_CONST.__cfstring: 0x7b00
+  __AUTH_CONST.__objc_const: 0x2d088
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0xf0
+  __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__auth_got: 0xc38
-  __AUTH.__objc_data: 0xa260
+  __AUTH_CONST.__auth_got: 0xbb8
+  __AUTH.__objc_data: 0xa1c0
   __AUTH.__data: 0xa0
   __DATA.__objc_ivar: 0x11cc
-  __DATA.__data: 0xd08
+  __DATA.__data: 0xce8
   __DATA.__bss: 0x790
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x1040
-  __DATA_DIRTY.__data: 0x270
+  __DATA_DIRTY.__objc_data: 0x10e0
+  __DATA_DIRTY.__data: 0x268
   __DATA_DIRTY.__bss: 0x390
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10543
-  Symbols:   23975
-  CStrings:  3220
+  Functions: 10547
+  Symbols:   24001
+  CStrings:  3225
 
Sections:
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__data : content changed
Symbols:
+ +[MTSchemaMTApiInvocationMetadata(LTTranslationAdditions) lt_initWithTranslateAPIContext:]
+ +[MTSchemaMTInvocationCancelled(LTTranslationAdditions) lt_initWithExists:reason:localePair:qssSessionId:]
+ +[MTSchemaMTInvocationStarted(LTTranslationAdditions) lt_initWithTask:inputMode:invocationType:explicitLanguageFilterEnabled:onDevice:translateAppContext:translateAPIContext:]
+ +[_LTDLanguageAssetService _isValidPOSIXLocale:]
+ +[_LTDLanguageAssetService _sanitizeLocales:]
+ +[_LTDSELFLoggingProduction cancelWithExists:reason:localePair:qssSessionId:mtId:sessionId:]
+ +[_LTDSELFLoggingProduction startWithTask:inputMode:invocationType:interfaceMode:explicitLanguageFilterEnabled:onDevice:mtId:sessionId:translateAppContext:translateAPIContext:]
+ +[_LTDTTSAssetService _bestTTSAssetForLocaleIdentifier:]
+ +[_LTDTTSAssetService hasVoiceForLocaleIdentifier:]
+ -[_LTClientConnection selfLoggingInvocationCancelledForIDs:localePair:]
+ -[_LTClientConnection selfLoggingInvocationDidError:invocationId:localePair:]
+ -[_LTDLanguageAssetCache hasObservers]
+ -[_LTDSELFLoggingManager invocationCancelWithInvocationId:reason:qssSessionId:localePair:]
+ -[_LTDSELFLoggingManager invocationStartWithInvocationId:task:inputMode:invocationType:translateAppContext:translateAPIContext:]
+ -[_LTTranslationServer selfLoggingInvocationCancelledForIDs:localePair:]
+ -[_LTTranslationServer selfLoggingInvocationDidError:invocationId:localePair:]
+ _OBJC_CLASS_$_MTSchemaMTApiInvocationMetadata
+ _OBJC_CLASS_$__LTNullableLocalePair
+ __45+[_LTDLanguageAssetService _sanitizeLocales:]_block_invoke
+ __57-[_LTDLanguageAssetCache _filterAILanguages:forTaskHint:]_block_invoke
+ __CLASS_METHODS__LTDLLMBasedTranslationStatus
+ __LTDHasTTSVoiceForLocaleIdentifier
+ __OBJC_$_CATEGORY_CLASS_METHODS_MTSchemaMTApiInvocationMetadata_$_LTTranslationAdditions
+ __OBJC_$_CATEGORY_MTSchemaMTApiInvocationMetadata_$_LTTranslationAdditions
+ ___45+[_LTDLanguageAssetService _sanitizeLocales:]_block_invoke
+ ___72-[_LTTranslationServer selfLoggingInvocationCancelledForIDs:localePair:]_block_invoke
+ ___78-[_LTTranslationServer selfLoggingInvocationDidError:invocationId:localePair:]_block_invoke
+ ___block_descriptor_40_e18_B16?0"NSLocale"8l
+ ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56w
+ __preheatInFlight
+ __preheatPending
+ _objc_msgSend$_bestTTSAssetForLocaleIdentifier:
+ _objc_msgSend$_isValidPOSIXLocale:
+ _objc_msgSend$_sanitizeLocales:
+ _objc_msgSend$allowedLocalesForTaskHint:
+ _objc_msgSend$arrayByExcludingObjectsInArray:
+ _objc_msgSend$cancelWithExists:reason:localePair:qssSessionId:mtId:sessionId:
+ _objc_msgSend$hasVoiceForLocaleIdentifier:
+ _objc_msgSend$initWithLocalePair:
+ _objc_msgSend$invocationCancelWithInvocationId:reason:qssSessionId:localePair:
+ _objc_msgSend$invocationStartWithInvocationId:task:inputMode:invocationType:translateAppContext:translateAPIContext:
+ _objc_msgSend$lt_initWithExists:reason:localePair:qssSessionId:
+ _objc_msgSend$lt_initWithTask:inputMode:invocationType:explicitLanguageFilterEnabled:onDevice:translateAppContext:translateAPIContext:
+ _objc_msgSend$lt_initWithTranslateAPIContext:
+ _objc_msgSend$selfLoggingInvocationCancelledForIDs:localePair:
+ _objc_msgSend$selfLoggingInvocationDidError:invocationId:localePair:
+ _objc_msgSend$setApiInvocationMetadata:
+ _objc_msgSend$setTranslationLocalePair:
+ _objc_msgSend$startWithTask:inputMode:invocationType:interfaceMode:explicitLanguageFilterEnabled:onDevice:mtId:sessionId:translateAppContext:translateAPIContext:
+ _objc_msgSend$translateAPIContext
+ _symbolic ScSyytG
+ _symbolic _____yyt_G ScS8IteratorV
- +[MTSchemaMTInvocationCancelled(LTTranslationAdditions) lt_initWithExists:reason:qssSessionId:]
- +[MTSchemaMTInvocationStarted(LTTranslationAdditions) lt_initWithTask:inputMode:invocationType:explicitLanguageFilterEnabled:onDevice:translateAppContext:]
- +[_LTDSELFLoggingProduction cancelWithExists:reason:qssSessionId:mtId:sessionId:]
- +[_LTDSELFLoggingProduction startWithTask:inputMode:invocationType:interfaceMode:explicitLanguageFilterEnabled:onDevice:mtId:sessionId:translateAppContext:]
- -[_LTClientConnection selfLoggingInvocationCancelledForIDs:]
- -[_LTClientConnection selfLoggingInvocationDidError:invocationId:]
- -[_LTDSELFLoggingManager invocationCancelWithInvocationId:reason:qssSessionId:]
- -[_LTDSELFLoggingManager invocationStartWithInvocationId:task:inputMode:invocationType:translateAppContext:]
- -[_LTTranslationServer selfLoggingInvocationCancelledForIDs:]
- -[_LTTranslationServer selfLoggingInvocationDidError:invocationId:]
- GCC_except_table182
- ___61-[_LTTranslationServer selfLoggingInvocationCancelledForIDs:]_block_invoke
- ___67-[_LTTranslationServer selfLoggingInvocationDidError:invocationId:]_block_invoke
- ___block_descriptor_48_e5_v8?0l
- _block_invoke.preheating
- _objc_msgSend$cancelWithExists:reason:qssSessionId:mtId:sessionId:
- _objc_msgSend$invocationCancelWithInvocationId:reason:qssSessionId:
- _objc_msgSend$invocationStartWithInvocationId:task:inputMode:invocationType:translateAppContext:
- _objc_msgSend$lt_initWithExists:reason:qssSessionId:
- _objc_msgSend$lt_initWithTask:inputMode:invocationType:explicitLanguageFilterEnabled:onDevice:translateAppContext:
- _objc_msgSend$selfLoggingInvocationCancelledForIDs:
- _objc_msgSend$selfLoggingInvocationDidError:invocationId:
- _objc_msgSend$startWithTask:inputMode:invocationType:interfaceMode:explicitLanguageFilterEnabled:onDevice:mtId:sessionId:translateAppContext:
- _swift_willThrowTypedImpl
- _symbolic _____ 16GenerativeModels0aB12AvailabilityV
- _symbolic _____Sg 16GenerativeModels0aB12AvailabilityV0C0O
- _symbolic ______p s5ErrorP
- _symbolic _____y_____G s11_SetStorageC 16GenerativeModels0cD12AvailabilityV0E0O15UnavailableInfoV0F6ReasonO
- _symbolic _____y_____G s23_ContiguousArrayStorageC 16GenerativeModels0dE12AvailabilityV0F0O15UnavailableInfoV0G6ReasonO
CStrings:
+ "Add languages %{public}@"
+ "Filtering out invalid language locale [%{public}@]"
+ "LLM translation availability change event"
+ "Preheat skipped: no active observers"
+ "Sending Traditional observations over XPC: [%{public}@]"
+ "_ltLocaleIdentifier"
+ "assetForIdentifier: called with empty identifier; ignoring"
- "Add %zd languages"
- "LLM translation availability change event [%s]"
- "Obsv xpcmsg [%@]"

```
