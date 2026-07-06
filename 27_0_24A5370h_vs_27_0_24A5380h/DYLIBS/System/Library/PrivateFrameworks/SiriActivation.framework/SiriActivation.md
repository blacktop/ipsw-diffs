## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-  __TEXT.__text: 0x6eae0
-  __TEXT.__objc_methlist: 0x6ea4
-  __TEXT.__const: 0x119c
-  __TEXT.__cstring: 0xc9a2
-  __TEXT.__oslogstring: 0x8f6f
+  __TEXT.__text: 0x6f024
+  __TEXT.__objc_methlist: 0x6ec4
+  __TEXT.__const: 0x11ac
+  __TEXT.__cstring: 0xca12
+  __TEXT.__oslogstring: 0x90a8
   __TEXT.__gcc_except_tab: 0xc88
   __TEXT.__dlopen_cstrs: 0x1bc
-  __TEXT.__swift5_typeref: 0x714
+  __TEXT.__swift5_typeref: 0x732
   __TEXT.__constg_swiftt: 0x3e4
   __TEXT.__swift5_reflstr: 0x1d1
   __TEXT.__swift5_fieldmd: 0x198
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_types: 0x28
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_capture: 0x504
+  __TEXT.__swift5_capture: 0x508
   __TEXT.__swift5_proto: 0x2c
   __TEXT.__swift_as_entry: 0x78
   __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__swift_as_cont: 0x8c
-  __TEXT.__unwind_info: 0x1e28
+  __TEXT.__unwind_info: 0x1e40
   __TEXT.__eh_frame: 0xee8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x17f8
+  __DATA_CONST.__const: 0x1800
   __DATA_CONST.__objc_classlist: 0x388
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x34c8
+  __DATA_CONST.__objc_selrefs: 0x34d8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x2c0
   __DATA_CONST.__objc_arraydata: 0x510
   __DATA_CONST.__got: 0xa58
   __AUTH_CONST.__const: 0x1488
-  __AUTH_CONST.__cfstring: 0x4fa0
-  __AUTH_CONST.__objc_const: 0xb010
+  __AUTH_CONST.__cfstring: 0x4fe0
+  __AUTH_CONST.__objc_const: 0xb068
   __AUTH_CONST.__objc_intobj: 0x978
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0xb70
-  __AUTH.__objc_data: 0x2050
+  __AUTH_CONST.__auth_got: 0xb88
+  __AUTH.__objc_data: 0x2000
   __AUTH.__data: 0x118
-  __DATA.__objc_ivar: 0x714
-  __DATA.__data: 0x1610
+  __DATA.__objc_ivar: 0x71c
+  __DATA.__data: 0x1660
   __DATA.__bss: 0x648
-  __DATA.__common: 0x268
-  __DATA_DIRTY.__objc_data: 0x5a0
+  __DATA.__common: 0x270
+  __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CallKit.framework/CallKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2869
-  Symbols:   8777
-  CStrings:  2420
+  Functions: 2870
+  Symbols:   8790
+  CStrings:  2430
 
Sections:
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__data : content changed
Symbols:
+ +[SRUIFSiriFeatureFlag(SWEFeatureFlags) isAssistedLinwoodVoiceResponseFromCompanionEnabled]
+ -[SASPreheatRequest initWithRequestSource:configuration:activationReferenceIdentifier:speechRequestOptions:]
+ -[SASPreheatRequest speechRequestOptions]
+ -[_SASPreheatRequestMutation setSpeechRequestOptions:]
+ _AFPreferencesHeadphonesAlwaysAuthenticatedEnabled
+ _OBJC_IVAR_$_SASPreheatRequest._speechRequestOptions
+ _OBJC_IVAR_$__SASPreheatRequestMutation._speechRequestOptions
+ ___56-[SASRemoteRequestManager _handleRemotePrewarmWithInfo:]_block_invoke
+ ___swift_closure_destructor.240Tm
+ _dispatch_block_create
+ _objc_msgSend$initWithRequestSource:configuration:activationReferenceIdentifier:speechRequestOptions:
+ _objc_msgSend$setButtonUpTimestamp:
+ _swift_retain_x26
+ _symbolic So24SASTimeIntervalTransportC
- -[SASPreheatRequest initWithRequestSource:configuration:activationReferenceIdentifier:]
- ___swift_closure_destructor.227Tm
- ___swift_closure_destructor.245Tm
- _objc_msgSend$initWithRequestSource:configuration:activationReferenceIdentifier:
CStrings:
+ "\""
+ "%s #activation #prewarm Remote request manager is preheating presentation"
+ "%s #activation Rejecting VT/RTS activation request since we have a Starting or Active presentation"
+ "%s #prewarm Remote request manager is handling prewarm for %@"
+ "%s 🎧 Headphones Always Authenticated internal setting is ON, returning YES"
+ "SASPreheatRequest::speechRequestOptions"
+ "assisted_linwood_voice_response_from_companion"
+ "speechRequestOptions = %@"

```
