## PasscodeAndBiometricsSettings

> `/System/Library/PrivateFrameworks/PasscodeAndBiometricsSettings.framework/PasscodeAndBiometricsSettings`

```diff

-12.2.0.0.0
-  __TEXT.__text: 0x2fe48
+14.0.0.0.0
+  __TEXT.__text: 0x306c4
   __TEXT.__auth_stubs: 0xc40
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x1fc4
+  __TEXT.__objc_methlist: 0x1ff4
   __TEXT.__const: 0x4d4
   __TEXT.__gcc_except_tab: 0xad8
-  __TEXT.__cstring: 0x30df
-  __TEXT.__oslogstring: 0x45f3
+  __TEXT.__cstring: 0x319f
+  __TEXT.__oslogstring: 0x4690
   __TEXT.__dlopen_cstrs: 0x443
   __TEXT.__ustring: 0x4e
   __TEXT.__constg_swiftt: 0xe0

   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x30
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0xc38
+  __TEXT.__unwind_info: 0xc40
   __TEXT.__objc_classname: 0x415
-  __TEXT.__objc_methname: 0x6f7d
+  __TEXT.__objc_methname: 0x6ff6
   __TEXT.__objc_methtype: 0xd62
   __TEXT.__objc_stubs: 0x5f80
-  __DATA_CONST.__got: 0x5e0
-  __DATA_CONST.__const: 0x1078
+  __DATA_CONST.__got: 0x5d8
+  __DATA_CONST.__const: 0x10a8
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d90
+  __DATA_CONST.__objc_selrefs: 0x1d98
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x638
-  __AUTH_CONST.__const: 0x448
-  __AUTH_CONST.__cfstring: 0x2ae0
-  __AUTH_CONST.__objc_const: 0x1f78
+  __AUTH_CONST.__const: 0x428
+  __AUTH_CONST.__cfstring: 0x2ba0
+  __AUTH_CONST.__objc_const: 0x1fa8
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x740
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0xf0
+  __DATA.__objc_ivar: 0xf4
   __DATA.__data: 0x674
   __DATA.__bss: 0x778
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2AF5FE09-1E0D-35A2-B55B-9F7A1D02FED8
-  Functions: 1035
-  Symbols:   3695
-  CStrings:  2365
+  UUID: 628DEEDA-5DD8-3509-8350-32EAF78DA2A6
+  Functions: 1042
+  Symbols:   3710
+  CStrings:  2387
 
Symbols:
+ -[PABSBiometricController boundCredentialsCount]
+ -[PABSBiometricController setBoundCredentialsCount:]
+ -[PABSDeviceTakeOverSectionController viewDidLoad]
+ -[PABSUnlockWithAppleWatchManager canUseVisionToUnlockWithCompletionHandler:]
+ GCC_except_table29
+ GCC_except_table32
+ GCC_except_table45
+ GCC_except_table51
+ GCC_except_table69
+ GCC_except_table94
+ _OBJC_IVAR_$_PABSBiometricController._boundCredentialsCount
+ _SFAutoUnlockManagerErrorTitleKey
+ _SharingLibrary
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.544
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.548
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.549
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.553
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.553.cold.1
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.555
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.555.cold.1
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke_2.551
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeRemoveFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.538
+ ___45-[PABSPasscodeLockController togglePasscode:]_block_invoke.506
+ ___45-[PABSPasscodeLockController togglePasscode:]_block_invoke.506.cold.1
+ ___47-[PABSFingerprintController deleteFingerprint:]_block_invoke.305
+ ___47-[PABSFingerprintController deleteFingerprint:]_block_invoke.305.cold.1
+ ___47-[PABSPasscodeLockController showKeychainAlert]_block_invoke.713
+ ___47-[PABSTouchIDPasscodeController addEnrollment:]_block_invoke.107
+ ___47-[PABSTouchIDPasscodeController addEnrollment:]_block_invoke.107.cold.1
+ ___48-[PABSDeviceTakeOverSectionController enableDTO]_block_invoke.98
+ ___48-[PABSDeviceTakeOverSectionController enableDTO]_block_invoke.98.cold.1
+ ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke.300
+ ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke.302
+ ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke_2.303
+ ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke_2.303.cold.1
+ ___49-[PABSDeviceTakeOverSectionController disableDTO]_block_invoke.100
+ ___49-[PABSDeviceTakeOverSectionController disableDTO]_block_invoke.100.cold.1
+ ___52-[PABSBiometricController useBiometricForSpecifiers]_block_invoke.164
+ ___55-[PABSPasscodeLockController setWipeEnabled:specifier:]_block_invoke.683
+ ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.864
+ ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.864.cold.1
+ ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.865
+ ___57-[PABSDeviceTakeOverSectionController proceedToEnableDTO]_block_invoke.95
+ ___57-[PABSDeviceTakeOverSectionController proceedToEnableDTO]_block_invoke.95.cold.1
+ ___63-[PABSPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.607
+ ___63-[PABSPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.611
+ ___67-[PABSBiometricController setTouchIDForPurchasesEnabled:specifier:]_block_invoke.87
+ ___67-[PABSBiometricController setTouchIDForPurchasesEnabled:specifier:]_block_invoke_2.88
+ ___67-[PABSDeviceTakeOverSectionController userUpdatedSecurityOptionTo:]_block_invoke.162
+ ___67-[PABSDeviceTakeOverSectionController userUpdatedSecurityOptionTo:]_block_invoke.162.cold.1
+ ___69-[PABSPasscodeLockController setEnabledInLockScreenForUSB:specifier:]_block_invoke.842
+ ___72-[PABSPearlPasscodeController deleteFaceIDIdentitiesCheckWithSpecifier:]_block_invoke.273
+ ___72-[PABSPearlPasscodeController deleteFaceIDIdentitiesCheckWithSpecifier:]_block_invoke.273.cold.1
+ ___76-[PABSUnlockWithAppleWatchManager canUseWatchToUnlockWithCompletionHandler:]_block_invoke.cold.1
+ ___77-[PABSUnlockWithAppleWatchManager canUseVisionToUnlockWithCompletionHandler:]_block_invoke
+ ___77-[PABSUnlockWithAppleWatchManager canUseVisionToUnlockWithCompletionHandler:]_block_invoke.cold.1
+ ___82-[PABSFingerprintController presentAlertSheetForFingerprintBindingToGovernmentID:]_block_invoke.282
+ ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.923
+ ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.923.cold.1
+ ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.924
+ ___85-[PABSPasscodeLockController showAlertForVisionUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.928
+ ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.911
+ ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.918
+ ___88-[PABSPasscodeLockController presentVisionUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.932
+ ___88-[PABSPasscodeLockController presentVisionUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.933
+ ___88-[PABSPasscodeLockController showAlertForPhoneAutoUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.903
+ ___93-[PABSBiometricController presentConfirmationAndProceedTouchIDForStockholmEnabled:specifier:]_block_invoke.124
+ ___94-[PABSDeviceTakeOverSectionController showDTOAlertForFailureToToggleToState:withRatchetError:]_block_invoke.146
+ ___block_descriptor_40_e8_32bs_e27_v24?0"NSSet"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32bs40w_e32_v32?0"NSArray"8q16"NSError"24lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48w_e32_v32?0"NSArray"8q16"NSError"24lw48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_80_e8_32s40s48s56s64w_e5_v8?0lw64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.167
+ ___block_literal_global.301
+ ___block_literal_global.303
+ ___block_literal_global.307
+ ___block_literal_global.309
+ ___block_literal_global.558
+ ___block_literal_global.613
+ ___block_literal_global.619
+ ___block_literal_global.709
+ ___block_literal_global.715
+ ___block_literal_global.913
+ ___getSFAuthenticationManagerClass_block_invoke
+ ___getSFAuthenticationManagerClass_block_invoke.cold.1
+ _getSFAuthenticationManagerClass.softClass
+ _notify_post
+ _objc_msgSend$boundCredentialsCount
+ _objc_msgSend$globalAuthACLTemplateUUIDsAndBoundCredentialsCountWithCompletion:
+ _objc_msgSend$setBoundCredentialsCount:
- GCC_except_table18
- GCC_except_table31
- GCC_except_table47
- GCC_except_table71
- GCC_except_table96
- _NSLog
- _OBJC_CLASS_$_DCBiometricStore
- _PSControlKey
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.541
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.543
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.545
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.550
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.550.cold.1
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.552
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.552.cold.1
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke_2.548
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeRemoveFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.535
- ___45-[PABSPasscodeLockController togglePasscode:]_block_invoke.503
- ___45-[PABSPasscodeLockController togglePasscode:]_block_invoke.503.cold.1
- ___46-[PABSBiometricController deleteGlobalAuthACL]_block_invoke
- ___46-[PABSBiometricController deleteGlobalAuthACL]_block_invoke_2
- ___46-[PABSBiometricController deleteGlobalAuthACL]_block_invoke_2.cold.1
- ___47-[PABSFingerprintController deleteFingerprint:]_block_invoke.292
- ___47-[PABSFingerprintController deleteFingerprint:]_block_invoke.292.cold.1
- ___47-[PABSPasscodeLockController showKeychainAlert]_block_invoke.709
- ___47-[PABSTouchIDPasscodeController addEnrollment:]_block_invoke.101
- ___47-[PABSTouchIDPasscodeController addEnrollment:]_block_invoke.101.cold.1
- ___48-[PABSDeviceTakeOverSectionController enableDTO]_block_invoke.96
- ___48-[PABSDeviceTakeOverSectionController enableDTO]_block_invoke.96.cold.1
- ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke.288
- ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke.290
- ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke_2.291
- ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke_2.291.cold.1
- ___49-[PABSDeviceTakeOverSectionController disableDTO]_block_invoke.98
- ___49-[PABSDeviceTakeOverSectionController disableDTO]_block_invoke.98.cold.1
- ___52-[PABSBiometricController useBiometricForSpecifiers]_block_invoke.165
- ___55-[PABSPasscodeLockController setWipeEnabled:specifier:]_block_invoke_2
- ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.860
- ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.860.cold.1
- ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.861
- ___57-[PABSDeviceTakeOverSectionController proceedToEnableDTO]_block_invoke.93
- ___57-[PABSDeviceTakeOverSectionController proceedToEnableDTO]_block_invoke.93.cold.1
- ___63-[PABSPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.604
- ___63-[PABSPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.608
- ___67-[PABSBiometricController setTouchIDForPurchasesEnabled:specifier:]_block_invoke.88
- ___67-[PABSBiometricController setTouchIDForPurchasesEnabled:specifier:]_block_invoke_2.89
- ___67-[PABSDeviceTakeOverSectionController userUpdatedSecurityOptionTo:]_block_invoke.160
- ___67-[PABSDeviceTakeOverSectionController userUpdatedSecurityOptionTo:]_block_invoke.160.cold.1
- ___69-[PABSPasscodeLockController setEnabledInLockScreenForUSB:specifier:]_block_invoke.838
- ___72-[PABSPearlPasscodeController deleteFaceIDIdentitiesCheckWithSpecifier:]_block_invoke.270
- ___72-[PABSPearlPasscodeController deleteFaceIDIdentitiesCheckWithSpecifier:]_block_invoke.270.cold.1
- ___82-[PABSFingerprintController presentAlertSheetForFingerprintBindingToGovernmentID:]_block_invoke.273
- ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.919
- ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.919.cold.1
- ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.920
- ___85-[PABSPasscodeLockController showAlertForVisionUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.924
- ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.903
- ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.914
- ___88-[PABSPasscodeLockController presentVisionUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.928
- ___88-[PABSPasscodeLockController presentVisionUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.929
- ___88-[PABSPasscodeLockController showAlertForPhoneAutoUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.899
- ___93-[PABSBiometricController presentConfirmationAndProceedTouchIDForStockholmEnabled:specifier:]_block_invoke.125
- ___94-[PABSDeviceTakeOverSectionController showDTOAlertForFailureToToggleToState:withRatchetError:]_block_invoke.144
- ___block_descriptor_32_e17_v16?0"NSError"8l
- ___block_descriptor_48_e8_32bs40w_e29_v24?0"NSArray"8"NSError"16lw40l8s32l8
- ___block_descriptor_56_e8_32s40s48w_e29_v24?0"NSArray"8"NSError"16lw48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64w_e5_v8?0lw64l8s32l8s40l8s48l8s56l8
- ___block_literal_global.165
- ___block_literal_global.292
- ___block_literal_global.294
- ___block_literal_global.296
- ___block_literal_global.555
- ___block_literal_global.610
- ___block_literal_global.616
- ___block_literal_global.705
- ___block_literal_global.707
- ___block_literal_global.909
- _objc_msgSend$deleteBoundACLWithCompletion:
- _objc_msgSend$globalAuthACLTemplateUUIDsWithCompletion:
- _objc_msgSend$setOn:animated:
CStrings:
+ "#\""
+ "%@: Get: %@ (policyMax: %@)"
+ "%@: Presenting confirmation alert"
+ "%@: User canceled. - Reloading - "
+ "%@: User confirmed"
+ "BOUND_CREDENTIALS_COUNT_BINDING"
+ "DELETE_FINGERPRINT_ALERT_MESSAGE_PLURAL"
+ "DELETE_FINGERPRINT_SHEET_MESSAGE_PLURAL"
+ "PEARL_RESET_ALERT_SHEET_MESSAGE_PLURAL"
+ "PEARL_RESET_SECOND_ALERT_MESSAGE_PLURAL"
+ "SFAuthenticationManager"
+ "Tq,N,V_boundCredentialsCount"
+ "Unlock using Vision: %@"
+ "WIPE_DEVICE: Setting to %@"
+ "_boundCredentialsCount"
+ "boundCredentialsCount"
+ "canUseVisionToUnlockWithCompletionHandler:"
+ "com.apple.passd.bound-biometric-reset"
+ "globalAuthACLTemplateUUIDsAndBoundCredentialsCountWithCompletion:"
+ "setBoundCredentialsCount:"
+ "v32@?0@\"NSArray\"8q16@\"NSError\"24"
+ "\x91"
- "%s: Encountered error '%{public}@'"
- "-[PABSBiometricController deleteGlobalAuthACL]_block_invoke_2"
- "deleteBoundACLWithCompletion:"
- "globalAuthACLTemplateUUIDsWithCompletion:"
- "setOn:animated:"
- "\x81"

```
