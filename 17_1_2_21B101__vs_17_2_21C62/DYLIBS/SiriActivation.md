## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-3301.15.1.0.0
-  __TEXT.__text: 0x3e088
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x4610
+3302.13.3.1.1
+  __TEXT.__text: 0x3f40c
+  __TEXT.__auth_stubs: 0x910
+  __TEXT.__objc_methlist: 0x46a0
   __TEXT.__const: 0x458
-  __TEXT.__cstring: 0x819d
-  __TEXT.__oslogstring: 0x5c4e
-  __TEXT.__gcc_except_tab: 0x728
+  __TEXT.__cstring: 0x84f4
+  __TEXT.__oslogstring: 0x5e7a
+  __TEXT.__gcc_except_tab: 0x73c
   __TEXT.__dlopen_cstrs: 0x168
-  __TEXT.__unwind_info: 0x1048
-  __TEXT.__objc_classname: 0xd2d
-  __TEXT.__objc_methname: 0xbb82
-  __TEXT.__objc_methtype: 0x1cce
-  __TEXT.__objc_stubs: 0x8060
-  __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__const: 0x1230
+  __TEXT.__unwind_info: 0x106c
+  __TEXT.__objc_classname: 0xd3a
+  __TEXT.__objc_methname: 0xbede
+  __TEXT.__objc_methtype: 0x1d4d
+  __TEXT.__objc_stubs: 0x8220
+  __DATA_CONST.__got: 0x1b8
+  __DATA_CONST.__const: 0x1278
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x118
+  __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6ee0
-  __DATA_CONST.__objc_selrefs: 0x2628
+  __DATA_CONST.__objc_const: 0x7148
+  __DATA_CONST.__objc_selrefs: 0x26a8
   __DATA_CONST.__objc_arraydata: 0x440
-  __AUTH_CONST.__cfstring: 0x3b80
+  __AUTH_CONST.__cfstring: 0x3d20
   __AUTH_CONST.__objc_const: 0x2240
-  __AUTH_CONST.__const: 0x400
+  __AUTH_CONST.__const: 0x420
   __AUTH_CONST.__objc_intobj: 0x750
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__auth_got: 0x468
+  __AUTH_CONST.__auth_got: 0x498
   __AUTH.__objc_data: 0x780
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x480
+  __DATA.__objc_classrefs: 0x4a0
   __DATA.__objc_superrefs: 0x218
-  __DATA.__objc_ivar: 0x548
-  __DATA.__data: 0xdf8
+  __DATA.__objc_ivar: 0x554
+  __DATA.__data: 0xe58
   __DATA.__bss: 0xa0
   __DATA_DIRTY.__objc_data: 0x1270
   - /System/Library/Frameworks/CallKit.framework/CallKit

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics
+  - /System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration
   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
+  - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1709
-  Symbols:   6074
-  CStrings:  3339
+  Functions: 1724
+  Symbols:   6142
+  CStrings:  3415
 
Symbols:
+ -[SASMyriadController _cacheFactors]
+ -[SASMyriadController _calculateExpBoosts:eventTime:trialBoostSecondDegree:trialBoostFirstDegree:trialBoostIntercept:]
+ -[SASMyriadController _calculateExponentialBoost:secondDegree:firstDegree:intercept:]
+ -[SASMyriadController _isTrialFeatureFlagEnabled]
+ -[SASMyriadController _isTrialMotionBoostEnabled]
+ -[SASMyriadController _isTrialUnlockBoostEnabled]
+ -[SASMyriadController _isTrialWakeBoostEnabled]
+ -[SASMyriadController _setupTrialRefresh]
+ -[SASMyriadController activateForRequest:withTimeout:visible:].cold.6
+ -[SASMyriadController scdaShouldAbortAnotherDeviceBetter:]
+ -[SASMyriadController scdaShouldContinue:]
+ -[SiriActivationService scdaShouldAbort:]
+ -[SiriActivationService scdaShouldContinue:]
+ GCC_except_table27
+ _AFMyriadGoodnessComputeExponentialBoost
+ _AFSiriLogContextDaemon
+ _AFSiriLogContextPerformance
+ _AFSupportsSCDAFramework
+ _OBJC_CLASS_$_SCDAContext
+ _OBJC_CLASS_$_SCDACoordinator
+ _OBJC_CLASS_$_SCDAGoodnessScoreOverrideState
+ _OBJC_CLASS_$_TRIClient
+ _OBJC_IVAR_$_SASMyriadController._scdaCoordinator
+ _OBJC_IVAR_$_SASMyriadController._trialClient
+ _OBJC_IVAR_$_SASMyriadController._trialRefreshQueue
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SCDADelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SCDADelegate
+ __OBJC_$_PROTOCOL_REFS_SCDADelegate
+ __OBJC_LABEL_PROTOCOL_$_SCDADelegate
+ __OBJC_PROTOCOL_$_SCDADelegate
+ ___41-[SASMyriadController _setupTrialRefresh]_block_invoke
+ ___54-[SASMyriadController _configureMotionActivityManager]_block_invoke.94
+ ___62-[SASMyriadController activateForRequest:withTimeout:visible:]_block_invoke.69
+ ___62-[SASMyriadController activateForRequest:withTimeout:visible:]_block_invoke.76
+ ___block_descriptor_32_e31_v16?0"<SCDAContextMutating>"8l
+ ___block_descriptor_48_e8_32s40w_e38_v16?0"<TRINamespaceUpdateProtocol>"8lw40l8s32l8
+ ___block_literal_global.514
+ ___block_literal_global.79
+ __os_signpost_emit_with_name_impl
+ _exp
+ _objc_msgSend$_cacheFactors
+ _objc_msgSend$_calculateExpBoosts:eventTime:trialBoostSecondDegree:trialBoostFirstDegree:trialBoostIntercept:
+ _objc_msgSend$_isTrialFeatureFlagEnabled
+ _objc_msgSend$_isTrialMotionBoostEnabled
+ _objc_msgSend$_isTrialUnlockBoostEnabled
+ _objc_msgSend$_isTrialWakeBoostEnabled
+ _objc_msgSend$_setupTrialRefresh
+ _objc_msgSend$addUpdateHandlerForNamespaceName:queue:usingBlock:
+ _objc_msgSend$booleanValue
+ _objc_msgSend$clientWithIdentifier:
+ _objc_msgSend$levelForFactor:withNamespaceName:
+ _objc_msgSend$refresh
+ _objc_msgSend$scdaShouldAbort:
+ _objc_msgSend$scdaShouldContinue:
+ _os_signpost_enabled
+ _os_signpost_id_generate
- ___54-[SASMyriadController _configureMotionActivityManager]_block_invoke.36
- ___62-[SASMyriadController activateForRequest:withTimeout:visible:]_block_invoke.23
- ___block_literal_global.512
CStrings:
+ "\x14\x12!3"
+ "%s #myriad Myriad Trial FF enabled"
+ "%s #myriad SCDA continues to interact, device won election"
+ "%s #myriad SCDA should abort session"
+ "%s #myriad Trial FF enabled"
+ "%s #myriad error reading trial levels for trialBoostSecondDegree"
+ "%s #myriad trial bump uint8_t %d"
+ "%s #myriad trial coefficients %@:%f, %@:%f, %@:%f"
+ "%s #myriad trialMotionBoostEnabled"
+ "%s #myriad trialUnlockBoostEnabled]"
+ "%s #myriad trialWakeBoostEnabled"
+ "%s Myriad Trial boosts updated: %@"
+ "%s Registering update handler"
+ "-[SASMyriadController _calculateExpBoosts:eventTime:trialBoostSecondDegree:trialBoostFirstDegree:trialBoostIntercept:]"
+ "-[SASMyriadController _setupTrialRefresh]"
+ "-[SASMyriadController _setupTrialRefresh]_block_invoke"
+ "-[SASMyriadController scdaShouldAbortAnotherDeviceBetter:]"
+ "-[SASMyriadController scdaShouldContinue:]"
+ "-[SiriActivationService scdaShouldAbort:]"
+ "-[SiriActivationService scdaShouldContinue:]"
+ "@\"SCDACoordinator\""
+ "@\"TRIClient\""
+ "C56@0:8d16d24@32@40@48"
+ "MOTION_BOOST_FIRST_DEGREE_COEFF"
+ "MOTION_BOOST_INTERCEPT"
+ "MOTION_BOOST_SECOND_DEGREE_COEFF"
+ "MOTION_BOOST_TRIAL_ENABLE"
+ "MYRIAD_BOOSTS"
+ "SASMyriadController._cacheFactors"
+ "SASMyriadController._calculateTrialWakeBoost"
+ "SCDADelegate"
+ "Siri"
+ "UNLOCK_BOOST_INTERCEPT"
+ "UNLOCK_BOOST_TRIAL_ENABLE"
+ "UNLOCK_FIRST_DEGREE_COEFF"
+ "UNLOCK_SECOND_DEGREE_COEFF"
+ "WAKE_BOOST_FIRST_DEGREE_COEFF"
+ "WAKE_BOOST_INTERCEPT"
+ "WAKE_BOOST_SECOND_DEGREE_COEFF"
+ "WAKE_BOOST_TRIAL_ENABLE"
+ "_cacheFactors"
+ "_calculateExpBoosts:eventTime:trialBoostSecondDegree:trialBoostFirstDegree:trialBoostIntercept:"
+ "_calculateExponentialBoost:secondDegree:firstDegree:intercept:"
+ "_isTrialFeatureFlagEnabled"
+ "_isTrialMotionBoostEnabled"
+ "_isTrialUnlockBoostEnabled"
+ "_isTrialWakeBoostEnabled"
+ "_scdaCoordinator"
+ "_setupTrialRefresh"
+ "_trialClient"
+ "_trialRefreshQueue"
+ "addUpdateHandlerForNamespaceName:queue:usingBlock:"
+ "booleanValue"
+ "clientWithIdentifier:"
+ "d48@0:8d16d24d32d40"
+ "levelForFactor:withNamespaceName:"
+ "refresh"
+ "scdaAdvertisingDidBegin:"
+ "scdaAdvertisingDidEnd:"
+ "scdaAdvertisingWillBeginWithDelay:advertisingInterval:"
+ "scdaCoordinatorDidHandleEmergency:"
+ "scdaCoordinatorWillHandleEmergency:"
+ "scdaListeningDidBegin:"
+ "scdaListeningDidEnd:"
+ "scdaShouldAbort:"
+ "scdaShouldAbortAnotherDeviceBetter:"
+ "scdaShouldContinue:"
+ "scdaShouldHandleEmergency:"
+ "scdaShouldUnduck:"
+ "scdaWillEndSession:"
+ "scdaWillStartWithSession:"
+ "scda_trial_boosts"
+ "v16@?0@\"<SCDAContextMutating>\"8"
+ "v16@?0@\"<TRINamespaceUpdateProtocol>\"8"
+ "v24@0:8@\"SCDACoordinator\"16"
+ "v24@0:8@\"SCDASession\"16"
- "\x11\x12!3"

```
