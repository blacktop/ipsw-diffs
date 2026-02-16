## MechPearl

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPearl.bundle/MechPearl`

```diff

-2005.80.10.0.0
-  __TEXT.__text: 0x68b0
-  __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_stubs: 0x1440
-  __TEXT.__objc_methlist: 0x5dc
-  __TEXT.__const: 0xe0
-  __TEXT.__objc_methname: 0x1704
-  __TEXT.__oslogstring: 0x6eb
-  __TEXT.__cstring: 0x377
+2005.100.174.0.0
+  __TEXT.__text: 0x88c8
+  __TEXT.__auth_stubs: 0x390
+  __TEXT.__objc_stubs: 0x1640
+  __TEXT.__objc_methlist: 0x5ec
+  __TEXT.__const: 0xd0
+  __TEXT.__objc_methname: 0x18b8
+  __TEXT.__oslogstring: 0x77c
+  __TEXT.__cstring: 0x38b
   __TEXT.__objc_classname: 0xea
-  __TEXT.__objc_methtype: 0x605
-  __TEXT.__gcc_except_tab: 0x164
-  __TEXT.__unwind_info: 0x268
-  __DATA_CONST.__auth_got: 0x1d0
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x450
+  __TEXT.__objc_methtype: 0x61e
+  __TEXT.__gcc_except_tab: 0x1f0
+  __TEXT.__unwind_info: 0x2b0
+  __DATA_CONST.__auth_got: 0x1d8
+  __DATA_CONST.__got: 0x328
+  __DATA_CONST.__const: 0x528
   __DATA_CONST.__cfstring: 0x320
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_intobj: 0x270
-  __DATA.__objc_const: 0x890
-  __DATA.__objc_selrefs: 0x700
-  __DATA.__objc_ivar: 0x7c
+  __DATA_CONST.__objc_intobj: 0x60
+  __DATA.__objc_const: 0x838
+  __DATA.__objc_selrefs: 0x780
+  __DATA.__objc_ivar: 0x74
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x300
   __DATA.__bss: 0x14

   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0305A5A9-8CEF-34D9-82AC-B98E351AE181
-  Functions: 128
-  Symbols:   96
-  CStrings:  464
+  UUID: A7CB25FC-F8D9-3F0F-A4BF-6A24D4CAC2B3
+  Functions: 143
+  Symbols:   172
+  CStrings:  481
 
Symbols:
+ _LACCoachingFeedbackBottomFaceOccluded
+ _LACCoachingFeedbackCameraObstructed
+ _LACCoachingFeedbackFaceNotDetected
+ _LACCoachingFeedbackFaceOccluded
+ _LACCoachingFeedbackFacePartiallyOutOfView
+ _LACCoachingFeedbackFaceTooClose
+ _LACCoachingFeedbackFaceTooFar
+ _LACCoachingFeedbackNoAttention
+ _LACCoachingFeedbackNone
+ _LACCoachingFeedbackPoseMarginal
+ _LACCoachingFeedbackPoseOutOfNegativePitchRange
+ _LACCoachingFeedbackPoseOutOfRange
+ _LACCoachingFeedbackUnsupportedGlasses
+ _LACErrorCodeAuthenticationFailed
+ _LACErrorCodeBiometryDeniedForApp
+ _LACErrorCodeDoublePressRequired
+ _LACErrorCodeInternal
+ _LACErrorCodeRequestFailed
+ _LACErrorCodeSystemCancel
+ _LACErrorCodeWrongAuthentication
+ _LACErrorInfoTCCServerPromptKey
+ _LACErrorInfoTCCServiceKey
+ _LACErrorSubcodeBiometryFailedToStart
+ _LACErrorSubcodeFaceDetectTimeout
+ _LACErrorSubcodeFaceIDHighTemperature
+ _LACErrorSubcodeFaceIDLowPower
+ _LACErrorSubcodeFaceIDLowTemperature
+ _LACEventParamCoachingFeedback
+ _LACEventParamCredentialPresent
+ _LACEventParamMirroringToDefaultUI
+ _LACEventParamPearlLockoutError
+ _LACEventParamPearlSimpleStatus
+ _LACEventPearl
+ _LACEventProcessingMirroringTypeNone
+ _LACEventProcessingOptionMirrorDefaultUI
+ _LACEventPushButton
+ _LACEventSimpleStatusFaceIDFaceDetectBegin
+ _LACEventSimpleStatusFaceIDFaceDetectTimeoutExpired
+ _LACEventSimpleStatusFaceIDFaceDetectTimeoutSet
+ _LACEventSimpleStatusFaceIDFaceIn
+ _LACEventSimpleStatusFaceIDFaceMatchingBegin
+ _LACEventSimpleStatusFaceIDFaceMatchingEnd
+ _LACEventSimpleStatusFaceIDFaceOut
+ _LACEventSimpleStatusFaceIDHardwareFailure
+ _LACEventSimpleStatusFaceIDMatch
+ _LACEventSimpleStatusFaceIDMatchExpired
+ _LACEventSimpleStatusFaceIDNoMatch
+ _LACEventSimpleStatusFaceIDPrepareSecureUI
+ _LACEventSimpleStatusFaceIDSensorActive
+ _LACEventSimpleStatusFaceIDSensorInactive
+ _LACEventSimpleStatusFaceIDUnboundMatch
+ _LACMechanismUserInfoKeyHardwareIssue
+ _LACMechanismUserInfoKeyUnderlyingError
+ _LACPolicyOptionCallerAuditToken
+ _LACPolicyOptionCallerAuditTokenUsage
+ _LACPolicyOptionEventProcessing
+ _LACPolicyOptionFaceDetectLength
+ _LACPolicyOptionMatchForUnlock
+ _LACPolicyOptionMaxBiometryFailures
+ _LACPolicyOptionNoFailureUI
+ _LACPolicyOptionPresentingEmbeddedUI
+ _LACPolicyOptionReturnBiometryDatabaseHash
+ _LACPolicyOptionSkipDoublePress
+ _LACPolicyStockholm
+ _LACPurposeNone
+ _LACResultBiometryCredentialAdded
+ _LACResultBiometryDatabaseHash
+ _LACResultBiometryKeyBagUnlock
+ _LACResultBiometryLockout
+ _LACResultPassedBiometry
+ _LACResultPushButtonPressed
+ _LACResultUserID
+ _NSDebugDescriptionErrorKey
+ _OBJC_CLASS_$_LACFlags
+ _OBJC_CLASS_$_LACMutableEvaluationEventValueBiometricStatus
+ _OBJC_CLASS_$_LACMutableEvaluationEventValueCoachingFeedback
+ _OBJC_CLASS_$_LACMutableEvaluationEventValuePushButtonStatus
+ _OBJC_CLASS_$_LACPasscodeHelper
+ _OBJC_CLASS_$_Request
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
+ _objc_retain_x27
- _LAErrorInfoTCCServerPrompt
- _LAErrorInfoTCCService
- _OBJC_CLASS_$_LAErrorHelper
- _OBJC_CLASS_$_LAPasscodeHelper
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
CStrings:
+ "-[CoachingFeedbackFilter dispatchNowOrWhenFeedbackDurationAchieved:finish:isCoaching:block:]"
+ "Mechanism event %@(%{public}@) on %{public}@"
+ "Sending mechanism event after coaching %d (%@)"
+ "Will not activate %@ at this moment, event is paused"
+ "_runWithHints:eventHandler:"
+ "_serviceLocator"
+ "dispatchNowOrWhenFeedbackDurationAchieved:finish:isCoaching:block:"
+ "errorWithCode:subcode:debugDescription:"
+ "errorWithCode:subcode:underlyingError:debugDescription:"
+ "errorWithCode:underlyingError:debugDescription:"
+ "errorWithCode:userInfo:"
+ "eventHandler"
+ "featureFlagPresentationContextEnabled"
+ "feedbackType"
+ "handleBiometricStatusEventWithValue:completion:"
+ "handleEvaluationEvent:value:"
+ "handleEvaluationEvent:value:timeout:reply:"
+ "isEventPaused:"
+ "matchingStatus"
+ "operation:captureInterrupted:"
+ "runWithHints:eventHandler:activationCompletion:reply:"
+ "runWithHints:eventHandler:reply:"
+ "setFeedbackType:"
+ "setIsCredentialPresent:"
+ "setLockoutError:"
+ "setMatchingStatus:"
+ "setObject:forKeyedSubscript:"
+ "setPayload:"
+ "v12@?0B8"
+ "v36@0:8B16B20B24@?28"
+ "v48@0:8@16@24@?32@?40"
- "-[CoachingFeedbackFilter dispatchNowOrWhenFeedbackDurationAchieved:finish:block:]"
- "TB,N,V_hasFallback"
- "TB,N,V_hasUI"
- "_hasFallback"
- "_hasUI"
- "dispatchNowOrWhenFeedbackDurationAchieved:finish:block:"
- "errorWithCode:message:"
- "errorWithCode:message:moreInfo:"
- "errorWithCode:message:suberror:"
- "errorWithCode:subcode:message:"
- "errorWithCode:subcode:message:suberror:"
- "setHasFallback:"
- "setHasUI:"
- "v32@0:8B16B20@?24"

```
