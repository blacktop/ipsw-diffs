## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-3403.11.2.11.3
-  __TEXT.__text: 0x477dc
-  __TEXT.__auth_stubs: 0xb20
-  __TEXT.__objc_methlist: 0x4ec0
-  __TEXT.__const: 0x782
-  __TEXT.__cstring: 0x951d
-  __TEXT.__oslogstring: 0x6738
-  __TEXT.__gcc_except_tab: 0xa34
+3404.68.1.1.2
+  __TEXT.__text: 0x4962c
+  __TEXT.__auth_stubs: 0xb70
+  __TEXT.__objc_methlist: 0x5c6c
+  __TEXT.__const: 0x792
+  __TEXT.__cstring: 0x985d
+  __TEXT.__oslogstring: 0x683e
+  __TEXT.__gcc_except_tab: 0xa3c
   __TEXT.__dlopen_cstrs: 0x168
   __TEXT.__swift5_typeref: 0x102
   __TEXT.__constg_swiftt: 0x160

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_capture: 0x50
   __TEXT.__swift5_proto: 0x18
-  __TEXT.__unwind_info: 0x13d0
+  __TEXT.__swift_as_entry: 0x18
+  __TEXT.__swift_as_ret: 0xc
+  __TEXT.__unwind_info: 0x14a0
   __TEXT.__eh_frame: 0x110
-  __TEXT.__objc_classname: 0xe78
-  __TEXT.__objc_methname: 0xcd9e
-  __TEXT.__objc_methtype: 0x1f09
-  __TEXT.__objc_stubs: 0x8c20
-  __DATA_CONST.__got: 0x678
-  __DATA_CONST.__const: 0x1548
-  __DATA_CONST.__objc_classlist: 0x2f8
+  __TEXT.__objc_classname: 0xf6d
+  __TEXT.__objc_methname: 0xd2d8
+  __TEXT.__objc_methtype: 0x2084
+  __TEXT.__objc_stubs: 0x8ec0
+  __DATA_CONST.__got: 0x688
+  __DATA_CONST.__const: 0x15e8
+  __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x130
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29c0
+  __DATA_CONST.__objc_selrefs: 0x2be8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x268
-  __DATA_CONST.__objc_arraydata: 0x4f0
-  __AUTH_CONST.__auth_got: 0x5a0
+  __DATA_CONST.__objc_superrefs: 0x290
+  __DATA_CONST.__objc_arraydata: 0x510
+  __AUTH_CONST.__auth_got: 0x5c8
   __AUTH_CONST.__auth_ptr: 0x68
-  __AUTH_CONST.__const: 0x560
-  __AUTH_CONST.__cfstring: 0x44e0
-  __AUTH_CONST.__objc_const: 0xa270
-  __AUTH_CONST.__objc_intobj: 0x8b8
-  __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0xca8
+  __AUTH_CONST.__const: 0x5e0
+  __AUTH_CONST.__cfstring: 0x4700
+  __AUTH_CONST.__objc_const: 0x9730
+  __AUTH_CONST.__objc_intobj: 0x8e8
+  __AUTH_CONST.__objc_dictobj: 0xf0
+  __AUTH.__objc_data: 0xe18
   __AUTH.__data: 0xf0
-  __DATA.__objc_ivar: 0x5d8
-  __DATA.__data: 0xe78
-  __DATA.__bss: 0x480
+  __DATA.__objc_ivar: 0x624
+  __DATA.__data: 0xf38
+  __DATA.__bss: 0x4a0
   __DATA_DIRTY.__objc_data: 0x1220
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1977
-  Symbols:   2449
-  CStrings:  3701
+  Functions: 2066
+  Symbols:   2557
+  CStrings:  3792
 
Symbols:
+ _AFDeviceSupportsVisualIntelligence
+ _AFIsAppleIntelligenceEnabled
+ _AFRestrictionsChangedNotificationName
+ _OBJC_CLASS_$_BSActionResponse
+ _OBJC_CLASS_$_BSMutableSettings
+ _OBJC_CLASS_$_SASActivationLaunchActionResponse
+ _OBJC_CLASS_$_SASActivationSourceEligibility
+ _OBJC_CLASS_$_SASPreheatRequest
+ _OBJC_METACLASS_$_BSActionResponse
+ _OBJC_METACLASS_$_SASActivationLaunchActionResponse
+ _OBJC_METACLASS_$_SASActivationSourceEligibility
+ _OBJC_METACLASS_$_SASPreheatRequest
+ _SASPreheatConfigurationGetFromName
+ _SASPreheatConfigurationGetIsValid
+ _SASPreheatConfigurationGetIsValidAndSpecified
+ _SASPreheatConfigurationGetName
+ _SASPreheatOptionsKey
+ _SASPreheatRequestKey
+ _SiriIsCurrentProcessSpringBoard
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x28
CStrings:
+ "%s #activation %@"
+ "%s #activation isVisualIntelligenceCameraControlLaunchEnabled: %d, isVisualIntelligenceSupported: %d, isCameraControlEnabled: %d, isAppleIntelligenceEnabled: %d"
+ "%s #activation isVisualIntelligenceWidgetControlEnabled: %d"
+ "%s #activation prewarm"
+ "-[SASActivationSourceEligibility shouldSystemOfferActivationForSource:systemAssistantExperienceEnabled:]"
+ "-[SASSignalServer prewarmWithRequest:]"
+ "-[SiriDirectActionSource activateWithContext:]"
+ "-[SiriDirectActionSource activateWithContext:completion:]"
+ "-[SiriTostadaSource init]"
+ "-[SiriTostadaSource invalidate]"
+ "4\x14Q\x19##"
+ "; activationPreparationIdentifier=%@"
+ "@\"<SASActivationSourceEligibilityDelegate>\""
+ "@\"SASPreheatOptions\""
+ "@\"SASPreheatRequest\""
+ "@20@0:8B16"
+ "@40@0:8q16q24@32"
+ "B28@0:8q16B24"
+ "EagerLaunchActionDecisionNonCancellable"
+ "Identifier: "
+ "PresentationBringupCancellable"
+ "SASActivationLaunchActionResponse"
+ "SASActivationSourceEligibility"
+ "SASPreheatOptions::lockState"
+ "SASPreheatOptions::preheatRequest"
+ "SASPreheatOptionsMutability"
+ "SASPreheatOptionsMutating"
+ "SASPreheatRequest"
+ "SASPreheatRequest::activationReferenceIdentifier"
+ "SASPreheatRequest::configuration"
+ "SASPreheatRequest::requestSource"
+ "SASPreheatRequestMutability"
+ "SASPreheatRequestMutating"
+ "SASRequestOptionsActivationPreparationReferenceIdentifierCodingKey"
+ "SASRequestSourceControlCenterTalkToSiri"
+ "Should Activate: "
+ "SpringBoard"
+ "T@\"NSUUID\",&,N,V_activationIdentifier"
+ "T@\"NSUUID\",&,N,V_activationPreparationReferenceIdentifier"
+ "T@\"NSUUID\",R,C,N,V_activationReferenceIdentifier"
+ "T@\"NSUUID\",R,N,V_activationPreparationReferenceIdentifier"
+ "T@\"SASPreheatRequest\",R,C,N,V_preheatRequest"
+ "TB,N,V_loggingAllowed"
+ "TQ,R,N,V_lockState"
+ "Tq,R,N,V_configuration"
+ "Vv24@0:8@\"SASPreheatRequest\"16"
+ "_SASPreheatOptionsMutation"
+ "_SASPreheatRequestMutation"
+ "_activationIdentifier"
+ "_activationPreparationReferenceIdentifier"
+ "_activationReferenceIdentifier"
+ "_loggingAllowed"
+ "_preferencesDidChange"
+ "_preheatRequest"
+ "_restrictionsChanged:"
+ "_saeAvailable"
+ "activationEligibilityDidChange"
+ "activationHintStyleForSource:systemAssistantExperienceEnabled:"
+ "activationIdentifier"
+ "activationPreparationReferenceIdentifier"
+ "activationReferenceIdentifier"
+ "activationReferenceIdentifier = %@"
+ "configuration = %ld (%@)"
+ "eligibilityDidChange"
+ "error"
+ "info"
+ "initWithActivationDeviceIdentifier:requestInfo:activationPreparationReferenceIdentifier:"
+ "initWithApplicationBundleIdentifier:shouldActivate:"
+ "initWithDelegate:queue:"
+ "initWithInfo:error:"
+ "initWithLaunchActions:identifier:"
+ "initWithLoggingAllowed:"
+ "initWithPreheatRequest:lockState:"
+ "initWithRequestSource:configuration:activationReferenceIdentifier:"
+ "keyDescriptionForSetting:"
+ "lockState = %@"
+ "loggingAllowed"
+ "objectForSetting:"
+ "preheatRequest"
+ "preheatRequest = %@"
+ "prewarmWithRequest:"
+ "processName"
+ "q28@0:8q16B24"
+ "saeAvailable"
+ "setActivationIdentifier:"
+ "setActivationPreparationReferenceIdentifier:"
+ "setActivationReferenceIdentifier:"
+ "setLoggingAllowed:"
+ "setObject:forSetting:"
+ "setPreheatRequest:"
+ "shouldActivate"
+ "shouldSystemOfferActivationForSource:systemAssistantExperienceEnabled:"
+ "v16@?0@\"<SASPreheatOptionsMutating>\"8"
+ "v16@?0@\"<SASPreheatRequestMutating>\"8"
+ "v24@0:8@\"NSUUID\"16"
+ "v24@0:8@\"SASPreheatRequest\"16"
+ "visualIntelligenceCameraControlEnabled"
+ "{_mutationFlags=\"isDirty\"b1\"hasPreheatRequest\"b1\"hasLockState\"b1}"
+ "{_mutationFlags=\"isDirty\"b1\"hasRequestSource\"b1\"hasConfiguration\"b1\"hasActivationReferenceIdentifier\"b1}"
- "4\x14Q\x19#\""
- "<%@ %p; requestSource=%@; lockState=%@>"
- "@32@0:8q16Q24"
- "SASPreheatOptionsLockStateCodingKey"
- "SASPreheatOptionsRequestSourceCodingKey"
- "_isSAEEnabled"
- "appState"
- "com.apple.Tamale"
- "com.apple.VisualIntelligenceCamera"
- "initWithActivationDeviceIdentifier:requestInfo:"
- "initWithRequestSource:lockState:"
- "isInstalled"
- "isSAEEnabled"

```
