## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-3304.61.1.0.0
-  __TEXT.__text: 0x3fcc0
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_methlist: 0x46e0
+3305.4.1.1.2
+  __TEXT.__text: 0x409ac
+  __TEXT.__auth_stubs: 0x950
+  __TEXT.__objc_methlist: 0x4760
   __TEXT.__const: 0x458
-  __TEXT.__cstring: 0x8601
-  __TEXT.__oslogstring: 0x5f1c
-  __TEXT.__gcc_except_tab: 0x73c
+  __TEXT.__cstring: 0x86a5
+  __TEXT.__oslogstring: 0x600e
+  __TEXT.__gcc_except_tab: 0x770
   __TEXT.__dlopen_cstrs: 0x168
-  __TEXT.__unwind_info: 0x107c
-  __TEXT.__objc_classname: 0xd23
-  __TEXT.__objc_methname: 0xbf70
-  __TEXT.__objc_methtype: 0x1d4d
-  __TEXT.__objc_stubs: 0x8280
-  __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x1280
+  __TEXT.__unwind_info: 0x1068
+  __TEXT.__objc_classname: 0xd48
+  __TEXT.__objc_methname: 0xc238
+  __TEXT.__objc_methtype: 0x1dbc
+  __TEXT.__objc_stubs: 0x8340
+  __DATA_CONST.__got: 0x1c8
+  __DATA_CONST.__const: 0x12d8
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x120
+  __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7160
-  __DATA_CONST.__objc_selrefs: 0x26c0
+  __DATA_CONST.__objc_const: 0x72b0
+  __DATA_CONST.__objc_selrefs: 0x2728
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_classrefs: 0x488
+  __DATA_CONST.__objc_classrefs: 0x498
   __DATA_CONST.__objc_superrefs: 0x218
-  __DATA_CONST.__objc_arraydata: 0x450
-  __AUTH_CONST.__cfstring: 0x3d20
+  __DATA_CONST.__objc_arraydata: 0x460
+  __AUTH_CONST.__cfstring: 0x3d80
   __AUTH_CONST.__objc_const: 0x21f8
   __AUTH_CONST.__const: 0x420
-  __AUTH_CONST.__objc_intobj: 0x768
+  __AUTH_CONST.__objc_intobj: 0x780
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__auth_got: 0x498
-  __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0x55c
-  __DATA.__data: 0xe58
-  __DATA.__bss: 0xa0
-  __DATA_DIRTY.__objc_data: 0x1220
+  __AUTH_CONST.__auth_got: 0x4b8
+  __AUTH.__objc_data: 0x4b0
+  __DATA.__objc_ivar: 0x56c
+  __DATA.__data: 0xef8
+  __DATA.__bss: 0x60
+  __DATA_DIRTY.__objc_data: 0x14f0
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/PrivateFrameworks/AACCore.framework/AACCore
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3BEDABB1-9CA4-3EFC-A0B2-2EE681AAD53E
-  Functions: 1742
-  Symbols:   6176
-  CStrings:  3916
+  UUID: 867BDCC3-12D4-39EF-A105-1488A9BE9C25
+  Functions: 1759
+  Symbols:   6237
+  CStrings:  3954
 
Symbols:
+ -[SASSystemState gestalt]
+ -[SASSystemState isAssessmentModeActive]
+ -[SASSystemState restrictionEnforcer]
+ -[SASSystemState setGestalt:]
+ -[SASSystemState setIsAssessmentModeActive:]
+ -[SASSystemState setRestrictionEnforcer:]
+ -[SASSystemState shouldBeginRestrictingForAssessmentModeWithCompletion:]
+ -[SASSystemState shouldEndRestrictingForAssessmentModeWithCompletion:]
+ -[SiriActivationService assessmentModeChangedToIsActive:completion:]
+ -[SiriActivationService didDismissForAssesmentModeStartedCompeltion]
+ -[SiriActivationService setDidDismissForAssesmentModeStartedCompeltion:]
+ -[SiriLongPressButtonSource didRecognizeLongPressInteraction:].cold.1
+ GCC_except_table66
+ _NSDebugDescriptionErrorKey
+ _OBJC_CLASS_$_AEAssessmentAgentService
+ _OBJC_CLASS_$_AEAssessmentModeGestalt
+ _OBJC_IVAR_$_SASSystemState._gestalt
+ _OBJC_IVAR_$_SASSystemState._isAssessmentModeActive
+ _OBJC_IVAR_$_SASSystemState._restrictionEnforcer
+ _OBJC_IVAR_$_SiriActivationService._didDismissForAssesmentModeStartedCompeltion
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AEAssessmentModeRestrictionEnforcer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SASStateChangeListener
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AEAssessmentModeRestrictionEnforcer
+ __OBJC_$_PROTOCOL_REFS_SASStateChangeListener
+ __OBJC_LABEL_PROTOCOL_$_AEAssessmentModeRestrictionEnforcer
+ __OBJC_PROTOCOL_$_AEAssessmentModeRestrictionEnforcer
+ ___70-[SASSystemState shouldEndRestrictingForAssessmentModeWithCompletion:]_block_invoke
+ ___72-[SASSystemState shouldBeginRestrictingForAssessmentModeWithCompletion:]_block_invoke
+ ___72-[SASSystemState shouldBeginRestrictingForAssessmentModeWithCompletion:]_block_invoke_2
+ ___72-[SASSystemState shouldBeginRestrictingForAssessmentModeWithCompletion:]_block_invoke_3
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e8_v12?0B8lr40l8s32l8
+ ___block_literal_global.527
+ __unnamed_array_storage.306
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _kAFAssistantErrorDomain
+ _objc_msgSend$assessmentModeChangedToIsActive:completion:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$isActive
+ _objc_msgSend$isAssessmentModeActive
+ _objc_msgSend$registerRestrictionEnforcer:machServiceName:
+ _objc_msgSend$setIsAssessmentModeActive:
- ___block_literal_global.517
- __unnamed_array_storage.301
CStrings:
+ "\x02\x14\x19\x17"
+ "%s #activation Board sent a long press without a Speech interaction"
+ "%s #activation NO: Siri Setup is disabled while assessment session is active"
+ "%s #activation NO: assessment mode is active."
+ "%s #activation assessmentModeChangedToIsActive: %@"
+ "-[SiriActivationService assessmentModeChangedToIsActive:completion:]"
+ "/2"
+ "@\"<AEInvalidatable>\""
+ "@\"AEAssessmentModeGestalt\""
+ "AEAssessmentModeRestrictionEnforcer"
+ "AssessmentModeActive"
+ "Failed to deactivate assistant"
+ "T@\"<AEInvalidatable>\",&,N,V_restrictionEnforcer"
+ "T@\"AEAssessmentModeGestalt\",&,N,V_gestalt"
+ "T@?,C,N,V_didDismissForAssesmentModeStartedCompeltion"
+ "TB,N,V_isAssessmentModeActive"
+ "_didDismissForAssesmentModeStartedCompeltion"
+ "_gestalt"
+ "_isAssessmentModeActive"
+ "_restrictionEnforcer"
+ "assessmentModeChangedToIsActive:completion:"
+ "com.apple.siri.assessment-mode-restriction"
+ "didDismissForAssesmentModeStartedCompeltion"
+ "errorWithDomain:code:userInfo:"
+ "gestalt"
+ "isAssessmentModeActive"
+ "registerRestrictionEnforcer:machServiceName:"
+ "restrictionEnforcer"
+ "setDidDismissForAssesmentModeStartedCompeltion:"
+ "setGestalt:"
+ "setIsAssessmentModeActive:"
+ "setRestrictionEnforcer:"
+ "shouldBeginRestrictingForAssessmentModeWithCompletion:"
+ "shouldEndRestrictingForAssessmentModeWithCompletion:"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?B>20"
- "\x02\x14\x19\x16"
- "/"

```
