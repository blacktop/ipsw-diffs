## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4416.39.103.0.0
-  __TEXT.__text: 0x88112c
-  __TEXT.__auth_stubs: 0x4e70
+4416.41.0.0.0
+  __TEXT.__text: 0x884748
+  __TEXT.__auth_stubs: 0x4f00
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x84c84
-  __TEXT.__const: 0x10c60
-  __TEXT.__cstring: 0x6a356
-  __TEXT.__gcc_except_tab: 0xe184
-  __TEXT.__oslogstring: 0x47cba
+  __TEXT.__objc_methlist: 0x84de4
+  __TEXT.__const: 0x10c70
+  __TEXT.__cstring: 0x6a4a6
+  __TEXT.__gcc_except_tab: 0xe1b8
+  __TEXT.__oslogstring: 0x47d51
   __TEXT.__ustring: 0x1418
   __TEXT.__dlopen_cstrs: 0x2e6
-  __TEXT.__unwind_info: 0x239e8
+  __TEXT.__unwind_info: 0x23a78
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x1badd
-  __TEXT.__objc_methname: 0x185280
-  __TEXT.__objc_methtype: 0x3ecc3
-  __TEXT.__objc_stubs: 0xcf3c0
-  __DATA_CONST.__got: 0x2758
-  __DATA_CONST.__const: 0x19320
-  __DATA_CONST.__objc_classlist: 0x44c0
+  __TEXT.__objc_classname: 0x1bb65
+  __TEXT.__objc_methname: 0x185846
+  __TEXT.__objc_methtype: 0x3eded
+  __TEXT.__objc_stubs: 0xcf760
+  __DATA_CONST.__got: 0x2760
+  __DATA_CONST.__const: 0x19350
+  __DATA_CONST.__objc_classlist: 0x44c8
   __DATA_CONST.__objc_catlist: 0x2b0
   __DATA_CONST.__objc_nlcatlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x21a8
+  __DATA_CONST.__objc_protolist: 0x21b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1da108
-  __DATA_CONST.__objc_selrefs: 0x3e500
+  __DATA_CONST.__objc_const: 0x1da8b8
+  __DATA_CONST.__objc_selrefs: 0x3e5f8
   __DATA_CONST.__objc_arraydata: 0x14f8
-  __AUTH_CONST.__cfstring: 0x60980
-  __AUTH_CONST.__objc_const: 0x2e818
+  __AUTH_CONST.__cfstring: 0x60a40
+  __AUTH_CONST.__objc_const: 0x2e860
   __AUTH_CONST.__const: 0xded0
   __AUTH_CONST.__objc_arrayobj: 0x15a8
-  __AUTH_CONST.__objc_intobj: 0x2418
+  __AUTH_CONST.__objc_intobj: 0x2490
   __AUTH_CONST.__objc_doubleobj: 0x530
   __AUTH_CONST.__objc_dictobj: 0x2f8
-  __AUTH_CONST.__auth_got: 0x2750
-  __AUTH.__objc_data: 0xf410
+  __AUTH_CONST.__auth_got: 0x2798
+  __AUTH.__objc_data: 0xf460
   __DATA.__objc_protorefs: 0xa8
-  __DATA.__objc_classrefs: 0x63b0
-  __DATA.__objc_superrefs: 0x3578
-  __DATA.__objc_ivar: 0xc7c8
-  __DATA.__data: 0x1a748
+  __DATA.__objc_classrefs: 0x63d0
+  __DATA.__objc_superrefs: 0x3580
+  __DATA.__objc_ivar: 0xc808
+  __DATA.__data: 0x1a7a8
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0xbb0
   __DATA.__common: 0x58

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: CE56F561-F801-3A36-888C-D72B1C38B4B7
-  Functions: 56295
-  Symbols:   191703
-  CStrings:  88846
+  UUID: 7346EBA7-83F7-30E7-9D81-18C47EA290EF
+  Functions: 56332
+  Symbols:   191864
+  CStrings:  88915
 
Symbols:
+ -[SBDisplayProfileRegistry _modifyParameters:orientation:interfaceOrientationMode:chamoisEnabled:]
+ -[SBLockScreenManager _dismissLostModeBiometricAuthenticationTransientOverlay]
+ -[SBLockScreenManager _needsBiometricAuthenticationToExitLostMode]
+ -[SBLockScreenManager _presentLostModeBiometricAuthenticationTransientOverlay]
+ -[SBLockScreenManager _relockUIForLostMode]
+ -[SBLockScreenManager _runPreflightLocationBasedEvaluationToExitLostModeIfNecessary]
+ -[SBLockScreenManager lostModeBiometricAuthenticationViewControllerDidFailOrCancelAuthentication:]
+ -[SBLockScreenManager lostModeBiometricAuthenticationViewControllerDidSucceedAuthentication:]
+ -[SBLockScreenManager lostModeBiometricAuthenticationViewControllerDidTapEmergencyButton:]
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController .cxx_destruct]
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController _biometricAuthenticationButtonAction]
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController _biometricCapabilityText]
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController _buttonsBottomSpacing]
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController _handleCancelButtonAction]
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController _handleEmergencyButtonAction]
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController _hasTelephonyCapability]
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController _runLocalAuthenticationEvaluation]
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController _runLocalAuthenticationEvaluation].cold.1
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController allowsStackingOverlayContentAbove]
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController coverSheetIdentifier]
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController dealloc]
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController delegate]
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController initWithLockScreenManager:biometricResource:]
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController isLocked]
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController participantState]
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController setDelegate:]
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController showPasscode]
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController unlockFromSource:]
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController viewDidLoad]
+ -[SBLostModeBiometricAuthenticationTransientOverlayViewController viewWillDisappear:]
+ -[SBSystemApertureProximityBacklightPolicy _nontelephonyTouchAllowanceGracePeriod]
+ _CoverSheetModalViewBottomBaselineOffsetPortrait
+ _OBJC_CLASS_$_CSPasscodeBackgroundView
+ _OBJC_CLASS_$_SBLostModeBiometricAuthenticationTransientOverlayViewController
+ _OBJC_CLASS_$_UIButtonConfiguration
+ _OBJC_CLASS_$_UILayoutGuide
+ _OBJC_IVAR_$_SBLockScreenManager._isInFamiliarLocationToExitLostMode
+ _OBJC_IVAR_$_SBLockScreenManager._lostModeBiometricAuthenticationTransientOverlay
+ _OBJC_IVAR_$_SBLockScreenManager._lostModePreflightLocalAuthContext
+ _OBJC_IVAR_$_SBLostModeBiometricAuthenticationTransientOverlayViewController._authContext
+ _OBJC_IVAR_$_SBLostModeBiometricAuthenticationTransientOverlayViewController._backgroundView
+ _OBJC_IVAR_$_SBLostModeBiometricAuthenticationTransientOverlayViewController._biometricAuthButton
+ _OBJC_IVAR_$_SBLostModeBiometricAuthenticationTransientOverlayViewController._biometricResource
+ _OBJC_IVAR_$_SBLostModeBiometricAuthenticationTransientOverlayViewController._cancelButton
+ _OBJC_IVAR_$_SBLostModeBiometricAuthenticationTransientOverlayViewController._delegate
+ _OBJC_IVAR_$_SBLostModeBiometricAuthenticationTransientOverlayViewController._didAuthenticate
+ _OBJC_IVAR_$_SBLostModeBiometricAuthenticationTransientOverlayViewController._emergencyButton
+ _OBJC_IVAR_$_SBLostModeBiometricAuthenticationTransientOverlayViewController._labelsStackView
+ _OBJC_IVAR_$_SBLostModeBiometricAuthenticationTransientOverlayViewController._layoutGuide
+ _OBJC_IVAR_$_SBLostModeBiometricAuthenticationTransientOverlayViewController._lockScreenManager
+ _OBJC_IVAR_$_SBLostModeBiometricAuthenticationTransientOverlayViewController._subtitleLabel
+ _OBJC_IVAR_$_SBLostModeBiometricAuthenticationTransientOverlayViewController._titleLabel
+ _OBJC_METACLASS_$_SBLostModeBiometricAuthenticationTransientOverlayViewController
+ __OBJC_$_INSTANCE_METHODS_SBLostModeBiometricAuthenticationTransientOverlayViewController
+ __OBJC_$_INSTANCE_VARIABLES_SBLostModeBiometricAuthenticationTransientOverlayViewController
+ __OBJC_$_PROP_LIST_SBLostModeBiometricAuthenticationTransientOverlayViewController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBLostModeBiometricAuthenticationTransientOverlayViewControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBLostModeBiometricAuthenticationTransientOverlayViewControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_SBLostModeBiometricAuthenticationTransientOverlayViewControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_SBLostModeBiometricAuthenticationTransientOverlayViewController
+ __OBJC_CLASS_RO_$_SBLostModeBiometricAuthenticationTransientOverlayViewController
+ __OBJC_LABEL_PROTOCOL_$_SBLostModeBiometricAuthenticationTransientOverlayViewControllerDelegate
+ __OBJC_METACLASS_RO_$_SBLostModeBiometricAuthenticationTransientOverlayViewController
+ __OBJC_PROTOCOL_$_SBLostModeBiometricAuthenticationTransientOverlayViewControllerDelegate
+ __SBF_Private_IsD33OrSimilarDevice
+ __SBF_Private_IsD52OrSimilarDevice
+ __SBF_Private_IsD52ZoomedOrSimilarDevice
+ __SBF_Private_IsD53
+ __SBF_Private_IsD54
+ __SBF_Private_IsD63Like
+ __SBF_Private_IsD64Like
+ __SBF_Private_IsN84OrSimilarDevice
+ __SBF_Private_IsN84ZoomedOrSimilarDevice
+ __SBXXSetWantsVolumeButtonEvents.cold.1
+ ___100-[SBLostModeBiometricAuthenticationTransientOverlayViewController _runLocalAuthenticationEvaluation]_block_invoke
+ ___100-[SBLostModeBiometricAuthenticationTransientOverlayViewController _runLocalAuthenticationEvaluation]_block_invoke_2
+ ___100-[SBLostModeBiometricAuthenticationTransientOverlayViewController _runLocalAuthenticationEvaluation]_block_invoke_2.cold.1
+ ___103-[SBLostModeBiometricAuthenticationTransientOverlayViewController _biometricAuthenticationButtonAction]_block_invoke
+ ___52-[SBLockScreenManager _setPasscodeVisible:animated:]_block_invoke.348
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.339
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.342
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke_2.341
+ ___75-[SBLockScreenManager _unlockWithRequest:cancelPendingRequests:completion:]_block_invoke.367
+ ___81-[SBLockScreenManager _attemptUnlockWithPasscode:mesa:finishUIUnlock:completion:]_block_invoke.402
+ ___84-[SBLockScreenManager _runPreflightLocationBasedEvaluationToExitLostModeIfNecessary]_block_invoke
+ ___98-[SBDisplayProfileRegistry _modifyParameters:orientation:interfaceOrientationMode:chamoisEnabled:]_block_invoke
+ ___98-[SBDisplayProfileRegistry _modifyParameters:orientation:interfaceOrientationMode:chamoisEnabled:]_block_invoke_2
+ ___block_descriptor_40_e8_32w_e34_v24?0"NSDictionary"8"NSError"16lw32l8
+ _objc_msgSend$_biometricAuthenticationButtonAction
+ _objc_msgSend$_biometricCapabilityText
+ _objc_msgSend$_buttonsBottomSpacing
+ _objc_msgSend$_dismissLostModeBiometricAuthenticationTransientOverlay
+ _objc_msgSend$_hasTelephonyCapability
+ _objc_msgSend$_modifyParameters:orientation:interfaceOrientationMode:chamoisEnabled:
+ _objc_msgSend$_needsBiometricAuthenticationToExitLostMode
+ _objc_msgSend$_nontelephonyTouchAllowanceGracePeriod
+ _objc_msgSend$_presentLostModeBiometricAuthenticationTransientOverlay
+ _objc_msgSend$_relockUIForLostMode
+ _objc_msgSend$_runLocalAuthenticationEvaluation
+ _objc_msgSend$_runPreflightLocationBasedEvaluationToExitLostModeIfNecessary
+ _objc_msgSend$addLayoutGuide:
+ _objc_msgSend$canEvaluatePolicy:error:
+ _objc_msgSend$constraintEqualToAnchor:multiplier:
+ _objc_msgSend$evaluatePolicy:options:reply:
+ _objc_msgSend$filledButtonConfiguration
+ _objc_msgSend$hasMesaSupport
+ _objc_msgSend$initWithLockScreenManager:biometricResource:
+ _objc_msgSend$lostModeBiometricAuthenticationViewControllerDidFailOrCancelAuthentication:
+ _objc_msgSend$lostModeBiometricAuthenticationViewControllerDidSucceedAuthentication:
+ _objc_msgSend$lostModeBiometricAuthenticationViewControllerDidTapEmergencyButton:
+ _objc_msgSend$pinKeypadStatusSubtitleViewTitleFont
+ _objc_msgSend$pinKeypadStatusTitleViewTitleFont
+ _objc_msgSend$plainButtonConfiguration
+ _objc_msgSend$sensorCharacteristics
+ _objc_msgSend$setBaseBackgroundColor:
+ _objc_msgSend$setBaseForegroundColor:
+ _objc_msgSend$setCornerStyle:
+ _objc_msgSend$suggestedSystemApertureGracePeriodForScreenOff
- -[SBDisplayProfileRegistry _modifyParameters:orientation:chamoisEnabled:]
- ___52-[SBLockScreenManager _setPasscodeVisible:animated:]_block_invoke.347
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.338
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.341
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke_2.340
- ___73-[SBDisplayProfileRegistry _modifyParameters:orientation:chamoisEnabled:]_block_invoke
- ___73-[SBDisplayProfileRegistry _modifyParameters:orientation:chamoisEnabled:]_block_invoke_2
- ___75-[SBLockScreenManager _unlockWithRequest:cancelPendingRequests:completion:]_block_invoke.366
- ___81-[SBLockScreenManager _attemptUnlockWithPasscode:mesa:finishUIUnlock:completion:]_block_invoke.401
- ___block_literal_global.333
- _objc_msgSend$_modifyParameters:orientation:chamoisEnabled:
CStrings:
+ "\x06\x11\x11\x12\x11\x1f\x05\x15\x12"
+ "@\"<SBLostModeBiometricAuthenticationTransientOverlayViewControllerDelegate>\""
+ "@\"CSPasscodeBackgroundView\""
+ "@\"LAContext\""
+ "@\"SBLostModeBiometricAuthenticationTransientOverlayViewController\""
+ "@\"UILayoutGuide\""
+ "@44@0:8@16q24q32B40"
+ "Cannot evaluate local authentication policy with error: %@"
+ "DimpleKey"
+ "Failed lost mode biometric authentication with error: %@"
+ "LOST_MODE_BIO_AUTHENTICATION_CANCEL"
+ "LOST_MODE_BIO_AUTHENTICATION_EMERGENCY"
+ "LOST_MODE_BIO_AUTHENTICATION_FACE_ID"
+ "LOST_MODE_BIO_AUTHENTICATION_SUBTITLE"
+ "LOST_MODE_BIO_AUTHENTICATION_TITLE"
+ "LOST_MODE_BIO_AUTHENTICATION_TOUCH_ID"
+ "LocalAuthentication"
+ "Only Apple applications may use %s"
+ "SBLostModeBiometricAuthenticationTransientOverlayViewController"
+ "SBLostModeBiometricAuthenticationTransientOverlayViewControllerDelegate"
+ "T@\"<SBLostModeBiometricAuthenticationTransientOverlayViewControllerDelegate>\",W,N,V_delegate"
+ "_authContext"
+ "_biometricAuthButton"
+ "_biometricAuthenticationButtonAction"
+ "_biometricCapabilityText"
+ "_buttonsBottomSpacing"
+ "_cancelButton"
+ "_didAuthenticate"
+ "_dismissLostModeBiometricAuthenticationTransientOverlay"
+ "_emergencyButton"
+ "_handleCancelButtonAction"
+ "_handleEmergencyButtonAction"
+ "_hasTelephonyCapability"
+ "_isInFamiliarLocationToExitLostMode"
+ "_labelsStackView"
+ "_layoutGuide"
+ "_lostModeBiometricAuthenticationTransientOverlay"
+ "_lostModePreflightLocalAuthContext"
+ "_modifyParameters:orientation:interfaceOrientationMode:chamoisEnabled:"
+ "_needsBiometricAuthenticationToExitLostMode"
+ "_nontelephonyTouchAllowanceGracePeriod"
+ "_presentLostModeBiometricAuthenticationTransientOverlay"
+ "_relockUIForLostMode"
+ "_runLocalAuthenticationEvaluation"
+ "_runPreflightLocationBasedEvaluationToExitLostModeIfNecessary"
+ "addLayoutGuide:"
+ "canEvaluatePolicy:error:"
+ "constraintEqualToAnchor:multiplier:"
+ "evaluatePolicy:options:reply:"
+ "filledButtonConfiguration"
+ "hasMesaSupport"
+ "initWithLockScreenManager:biometricResource:"
+ "kern_return_t _SBXXSetWantsVolumeButtonEvents(mach_port_t, int32_t, audit_token_t)"
+ "lostModeBiometricAuthenticationViewControllerDidFailOrCancelAuthentication:"
+ "lostModeBiometricAuthenticationViewControllerDidSucceedAuthentication:"
+ "lostModeBiometricAuthenticationViewControllerDidTapEmergencyButton:"
+ "pinKeypadStatusSubtitleViewTitleFont"
+ "pinKeypadStatusTitleViewTitleFont"
+ "plainButtonConfiguration"
+ "sensorCharacteristics"
+ "setBaseBackgroundColor:"
+ "setBaseForegroundColor:"
+ "setCornerStyle:"
+ "suggestedSystemApertureGracePeriodForScreenOff"
+ "v24@0:8@\"SBLostModeBiometricAuthenticationTransientOverlayViewController\"16"
- "\x06\x11\x11\x12\x11\x1f\x05\x13\x12"
- "_modifyParameters:orientation:chamoisEnabled:"

```
