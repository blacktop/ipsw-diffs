## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-3600.55.30.0.0
-  __TEXT.__text: 0x6f570
-  __TEXT.__objc_methlist: 0x6f54
-  __TEXT.__const: 0x11ac
-  __TEXT.__cstring: 0xca82
-  __TEXT.__oslogstring: 0x90da
-  __TEXT.__gcc_except_tab: 0xc88
+3600.55.37.11.2
+  __TEXT.__text: 0x743f8
+  __TEXT.__objc_methlist: 0x6fa4
+  __TEXT.__const: 0x11dc
+  __TEXT.__cstring: 0xcc42
+  __TEXT.__oslogstring: 0x934c
+  __TEXT.__gcc_except_tab: 0xc8c
   __TEXT.__dlopen_cstrs: 0x1bc
-  __TEXT.__swift5_typeref: 0x732
-  __TEXT.__constg_swiftt: 0x3e4
-  __TEXT.__swift5_reflstr: 0x1d1
-  __TEXT.__swift5_fieldmd: 0x198
+  __TEXT.__swift5_typeref: 0x77a
+  __TEXT.__constg_swiftt: 0x42c
+  __TEXT.__swift5_reflstr: 0x241
+  __TEXT.__swift5_fieldmd: 0x1b0
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_types: 0x28
   __TEXT.__swift5_assocty: 0x30

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__swift_as_cont: 0x8c
-  __TEXT.__unwind_info: 0x1e60
-  __TEXT.__eh_frame: 0xee8
+  __TEXT.__unwind_info: 0x1ea8
+  __TEXT.__eh_frame: 0xf58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x34f0
+  __DATA_CONST.__objc_selrefs: 0x3528
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0x510
-  __DATA_CONST.__got: 0xa60
-  __AUTH_CONST.__const: 0x1488
+  __DATA_CONST.__got: 0xa80
+  __AUTH_CONST.__const: 0x14b0
   __AUTH_CONST.__cfstring: 0x5000
-  __AUTH_CONST.__objc_const: 0xb138
+  __AUTH_CONST.__objc_const: 0xb188
   __AUTH_CONST.__objc_intobj: 0x978
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0xb88
-  __AUTH.__objc_data: 0x2050
+  __AUTH_CONST.__auth_got: 0xbd8
+  __AUTH.__objc_data: 0x20a0
   __AUTH.__data: 0x118
   __DATA.__objc_ivar: 0x720
-  __DATA.__data: 0x1660
+  __DATA.__data: 0x16a0
   __DATA.__bss: 0x648
   __DATA.__common: 0x270
   __DATA_DIRTY.__objc_data: 0x5f0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2880
-  Symbols:   5998
-  CStrings:  1792
+  Functions: 2906
+  Symbols:   6020
+  CStrings:  1806
 
Symbols:
+ -[SASPresentationManager _locked_requestState]
+ -[SASPresentationManager updateIsPreprocessRequestForActivePresentations:]
+ -[SASPresentationServer resetSiriToOff]
+ -[SASPresentationServer speechRequestStartedFromPresentationInterface]
+ -[SiriActivationService _activationConditionForRequest:systemState:presentationIdentifier:]
+ -[SiriActivationServiceClientConnection speechRequestStartedFromPresentationInterface]
+ GCC_except_table100
+ GCC_except_table106
+ GCC_except_table164
+ GCC_except_table17
+ GCC_except_table69
+ ___70-[SASPresentationServer speechRequestStartedFromPresentationInterface]_block_invoke
+ ___swift_closure_destructor.247Tm
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ _objc_msgSend$_activationConditionForRequest:systemState:presentationIdentifier:
+ _objc_msgSend$_locked_requestState
+ _objc_msgSend$isInitiatedByPresentedAssistantInterface
+ _objc_msgSend$referenceIdentifier
+ _objc_msgSend$requestOptions
+ _objc_msgSend$speechRequestStartedFromPresentationInterface
+ _objc_msgSend$updateIsPreprocessRequestForActivePresentations:
+ _swift_arrayDestroy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_release_x12
+ _symbolic Shy_____G 10Foundation4UUIDV
+ _symbolic So17SAFRequestOptionsCSg
+ _symbolic _____Sg 10Foundation4UUIDV
+ _symbolic _____y_____G s11_SetStorageC 10Foundation4UUIDV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation4UUIDV
- +[SRUIFSiriFeatureFlag(SWEFeatureFlags) isAssistedLinwoodVoiceResponseFromCompanionEnabled]
- GCC_except_table104
- GCC_except_table16
- GCC_except_table163
- GCC_except_table18
- GCC_except_table65
- GCC_except_table99
- ___swift_closure_destructor.240Tm
CStrings:
+ " was initiated by the presented assistant interface"
+ "#activation Request "
+ "%s #activation NO: Ignoring post-activation voice trigger that is not allowed to activate"
+ "%s #activation SAS client notified SAS that a speech request started from the presentation interface."
+ "%s #activation SAS client notifying SAS that a speech request started from the presentation interface..."
+ "%s #activation Shell indicates that speech request was started via a presented assistant interface"
+ "%s #activation _shouldRejectActivationWithButtonIdentifier - rejecting: Siri is disabled while passcode locked"
+ "%s #activation speech request state did change (state = %ld) and self request state: %ld"
+ "%s #myriad BTLE advertising a watch in-task voice trigger"
+ "%s %p #activation resetSiriToOff"
+ "-[SASPresentationManager _locked_requestState]"
+ "-[SASPresentationManager updateIsPreprocessRequestForActivePresentations:]"
+ "-[SASPresentationServer resetSiriToOff]"
+ "-[SASPresentationServer speechRequestStartedFromPresentationInterface]_block_invoke"
+ "-[SiriActivationServiceClientConnection speechRequestStartedFromPresentationInterface]"
+ "notifySpeechRequestInitiatedFromApplicationIfNeeded(_:)"
- "%s #activation speech request state did change (state = %ld)"
- "assisted_linwood_voice_response_from_companion"
```
