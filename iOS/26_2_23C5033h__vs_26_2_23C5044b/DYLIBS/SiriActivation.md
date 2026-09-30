## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-3510.7.1.1.2
-  __TEXT.__text: 0x4f830
+3510.7.2.11.5
+  __TEXT.__text: 0x4fd54
   __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0x60a4
+  __TEXT.__objc_methlist: 0x60e4
   __TEXT.__const: 0x838
-  __TEXT.__cstring: 0xa1ad
-  __TEXT.__oslogstring: 0x6f5b
+  __TEXT.__cstring: 0xa1dd
+  __TEXT.__oslogstring: 0x6ff3
   __TEXT.__gcc_except_tab: 0xe5c
   __TEXT.__dlopen_cstrs: 0x1bc
   __TEXT.__swift5_typeref: 0x102

   __TEXT.__swift_as_ret: 0xc
   __TEXT.__unwind_info: 0x1610
   __TEXT.__eh_frame: 0x138
-  __TEXT.__objc_classname: 0x101d
-  __TEXT.__objc_methname: 0xdf0e
-  __TEXT.__objc_methtype: 0x23c9
-  __TEXT.__objc_stubs: 0x95c0
-  __DATA_CONST.__got: 0x6a8
-  __DATA_CONST.__const: 0x1678
+  __TEXT.__objc_classname: 0x104d
+  __TEXT.__objc_methname: 0xdfff
+  __TEXT.__objc_methtype: 0x23ec
+  __TEXT.__objc_stubs: 0x9620
+  __DATA_CONST.__got: 0x6b0
+  __DATA_CONST.__const: 0x1680
   __DATA_CONST.__objc_classlist: 0x330
-  __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x150
+  __DATA_CONST.__objc_catlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e40
+  __DATA_CONST.__objc_selrefs: 0x2e58
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x540
   __AUTH_CONST.__auth_got: 0x600
   __AUTH_CONST.__const: 0x5e8
-  __AUTH_CONST.__cfstring: 0x49e0
-  __AUTH_CONST.__objc_const: 0x9d00
+  __AUTH_CONST.__cfstring: 0x4a00
+  __AUTH_CONST.__objc_const: 0x9da8
   __AUTH_CONST.__objc_intobj: 0x978
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH.__objc_data: 0x1c28
   __AUTH.__data: 0xf0
-  __DATA.__objc_ivar: 0x678
-  __DATA.__data: 0xf98
+  __DATA.__objc_ivar: 0x680
+  __DATA.__data: 0xff8
   __DATA.__bss: 0x510
   __DATA_DIRTY.__objc_data: 0x4b0
   - /System/Library/Frameworks/CallKit.framework/CallKit

   - /System/Library/PrivateFrameworks/SiriObservation.framework/SiriObservation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /System/Library/PrivateFrameworks/SystemVoiceAssistantServices.framework/SystemVoiceAssistantServices
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 58DF4F11-5232-3457-A8A3-98E5CBA8A9A0
-  Functions: 2176
-  Symbols:   7447
-  CStrings:  4567
+  UUID: 9A0B4BE9-50B9-31CF-9FC5-39A3FEA4B914
+  Functions: 2179
+  Symbols:   7466
+  CStrings:  4579
 
Symbols:
+ -[BSActionResponse(SASActivationLaunchActionResponse) isSelectedAssistantApplicationLaunchResponse]
+ -[SASActivationLaunchActionResponse isSelectedAssistantApplicationLaunchResponse]
+ _OBJC_CLASS_$_SVASActivationSourceEligibility
+ _OBJC_IVAR_$_SASActivationSourceEligibility._shouldUseSystemVoiceAssistantEligibilityProvider
+ _OBJC_IVAR_$_SASActivationSourceEligibility._systemVoiceAssistantEligibilityProvider
+ __OBJC_$_CATEGORY_BSActionResponse_$_SASActivationLaunchActionResponse
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_BSActionResponse_$_SASActivationLaunchActionResponse
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SVASActivationSourceEligibilityProviderDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SVASActivationSourceEligibilityProviderDelegate
+ __OBJC_$_PROTOCOL_REFS_SVASActivationSourceEligibilityProviderDelegate
+ __OBJC_LABEL_PROTOCOL_$_SVASActivationSourceEligibilityProviderDelegate
+ __OBJC_PROTOCOL_$_SVASActivationSourceEligibilityProviderDelegate
+ ___53-[SASActivationSourceEligibility didChangeLockState:]_block_invoke
+ ___73-[SiriActivationService buttonTapFromButtonIdentifier:timestamp:context:]_block_invoke.144
+ ___93-[SiriActivationService _activatePresentationWithIdentifier:requestOptions:analyticsContext:]_block_invoke.180
+ ___block_literal_global.148
+ ___block_literal_global.187
+ ___block_literal_global.591
+ ___block_literal_global.596
+ _objc_msgSend$isRequestSourceEligible:systemAssistantExperienceEnabled:deviceEffectivelyLocked:
+ _objc_msgSend$modelExistsForPresentationIdentifier:
+ _objc_msgSend$shouldCheckEligibility
- ___73-[SiriActivationService buttonTapFromButtonIdentifier:timestamp:context:]_block_invoke.138
- ___93-[SiriActivationService _activatePresentationWithIdentifier:requestOptions:analyticsContext:]_block_invoke.174
- ___block_literal_global.142
- ___block_literal_global.181
- ___block_literal_global.585
- ___block_literal_global.590
CStrings:
+ "%s #activation NO: active call"
+ "%s #activation button activation captured by system assitant ? %@"
+ "%s #activation invalid source for System Assistant %ld"
+ "@\"SVASActivationSourceEligibility\""
+ "SVASActivationSourceEligibilityProviderDelegate"
+ "SiriPresentationSystemVoiceAssistantIdentifier"
+ "_shouldUseSystemVoiceAssistantEligibilityProvider"
+ "_systemVoiceAssistantEligibilityProvider"
+ "isRequestSourceEligible:systemAssistantExperienceEnabled:deviceEffectivelyLocked:"
+ "isSelectedAssistantApplicationLaunchResponse"
+ "shouldCheckEligibility"

```
