## PasscodeAndBiometricsSettings

> `/System/Library/PrivateFrameworks/PasscodeAndBiometricsSettings.framework/PasscodeAndBiometricsSettings`

```diff

-10.0.0.0.0
-  __TEXT.__text: 0x2fb2c
+11.0.0.0.0
+  __TEXT.__text: 0x2fd84
   __TEXT.__auth_stubs: 0xc40
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0xc8
   __TEXT.__objc_methlist: 0x1fc4
   __TEXT.__const: 0x4d4
+  __TEXT.__gcc_except_tab: 0xad8
   __TEXT.__cstring: 0x30cf
-  __TEXT.__gcc_except_tab: 0xab8
-  __TEXT.__oslogstring: 0x4544
+  __TEXT.__oslogstring: 0x45c6
   __TEXT.__dlopen_cstrs: 0x443
   __TEXT.__ustring: 0x4e
   __TEXT.__constg_swiftt: 0xe0

   __TEXT.__swift5_types: 0x10
   __TEXT.__unwind_info: 0xc30
   __TEXT.__objc_classname: 0x415
-  __TEXT.__objc_methname: 0x6f74
-  __TEXT.__objc_methtype: 0xd54
+  __TEXT.__objc_methname: 0x6f7d
+  __TEXT.__objc_methtype: 0xd62
   __TEXT.__objc_stubs: 0x5f80
   __DATA_CONST.__got: 0x5e0
-  __DATA_CONST.__const: 0x1048
+  __DATA_CONST.__const: 0x1078
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 591245C3-611F-307B-800C-F8552DC74FEE
+  UUID: 7BC73DE0-8EA5-3766-9140-A3E9C1D1A59C
   Functions: 1035
-  Symbols:   3701
-  CStrings:  2358
+  Symbols:   3695
+  CStrings:  2363
 
Symbols:
+ -[PABSBiometricController setStoreState:forceRefresh:]
+ -[PABSBiometricController updateStoreBiometricsStateAndForceRefresh:]
+ GCC_except_table71
+ GCC_except_table96
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.541
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.545
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.546
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.550
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.550.cold.1
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.552
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.552.cold.1
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke_2.548
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeRemoveFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.535
+ ___45-[PABSPasscodeLockController togglePasscode:]_block_invoke.503
+ ___45-[PABSPasscodeLockController togglePasscode:]_block_invoke.503.cold.1
+ ___47-[PABSPasscodeLockController showKeychainAlert]_block_invoke.709
+ ___52-[PABSBiometricController useBiometricForSpecifiers]_block_invoke.165
+ ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.860
+ ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.860.cold.1
+ ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.861
+ ___62-[PABSBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke.191
+ ___62-[PABSBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke.192
+ ___62-[PABSBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke_2.193
+ ___63-[PABSPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.604
+ ___63-[PABSPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.608
+ ___67-[PABSBiometricController setTouchIDForPurchasesEnabled:specifier:]_block_invoke.88
+ ___67-[PABSBiometricController setTouchIDForPurchasesEnabled:specifier:]_block_invoke_2.89
+ ___69-[PABSBiometricController updateStoreBiometricsStateAndForceRefresh:]_block_invoke
+ ___69-[PABSBiometricController updateStoreBiometricsStateAndForceRefresh:]_block_invoke_2
+ ___69-[PABSPasscodeLockController setEnabledInLockScreenForUSB:specifier:]_block_invoke.838
+ ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.919
+ ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.919.cold.1
+ ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.920
+ ___85-[PABSPasscodeLockController showAlertForVisionUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.924
+ ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.903
+ ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.907
+ ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.914
+ ___88-[PABSPasscodeLockController presentVisionUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.928
+ ___88-[PABSPasscodeLockController presentVisionUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.929
+ ___88-[PABSPasscodeLockController showAlertForPhoneAutoUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.899
+ ___93-[PABSBiometricController presentConfirmationAndProceedTouchIDForStockholmEnabled:specifier:]_block_invoke.125
+ ___block_descriptor_41_e8_32s_e20_v24?0q8"NSError"16ls32l8
+ ___block_descriptor_49_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_57_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0ls32l8s40l8s48l8w56l8
+ ___block_descriptor_tmp.151
+ ___block_descriptor_tmp.170
+ ___block_literal_global.153
+ ___block_literal_global.172
+ ___block_literal_global.555
+ ___block_literal_global.610
+ ___block_literal_global.616
+ ___block_literal_global.705
+ ___block_literal_global.707
+ ___block_literal_global.711
+ ___block_literal_global.909
+ _objc_msgSend$setStoreState:forceRefresh:
+ _objc_msgSend$updateStoreBiometricsStateAndForceRefresh:
- -[PABSBiometricController updateStoreBiometricsState]
- -[PABSBiometricController updateTouchIDForPurchasesSpecifier]
- GCC_except_table54
- GCC_except_table72
- GCC_except_table97
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.538
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.540
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.542
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.547
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.547.cold.1
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.549
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.549.cold.1
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke_2.545
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeRemoveFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.532
- ___45-[PABSPasscodeLockController togglePasscode:]_block_invoke.500
- ___45-[PABSPasscodeLockController togglePasscode:]_block_invoke.500.cold.1
- ___47-[PABSPasscodeLockController showKeychainAlert]_block_invoke.706
- ___52-[PABSBiometricController useBiometricForSpecifiers]_block_invoke.163
- ___53-[PABSBiometricController updateStoreBiometricsState]_block_invoke
- ___53-[PABSBiometricController updateStoreBiometricsState]_block_invoke_2
- ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.857
- ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.857.cold.1
- ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.858
- ___62-[PABSBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke.189
- ___62-[PABSBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke.190
- ___62-[PABSBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke_2.191
- ___63-[PABSPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.601
- ___63-[PABSPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.605
- ___67-[PABSBiometricController setTouchIDForPurchasesEnabled:specifier:]_block_invoke_3
- ___67-[PABSBiometricController setTouchIDForPurchasesEnabled:specifier:]_block_invoke_4
- ___69-[PABSPasscodeLockController setEnabledInLockScreenForUSB:specifier:]_block_invoke.835
- ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.916
- ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.916.cold.1
- ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.917
- ___85-[PABSPasscodeLockController showAlertForVisionUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.921
- ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.900
- ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.904
- ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.911
- ___88-[PABSPasscodeLockController presentVisionUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.925
- ___88-[PABSPasscodeLockController presentVisionUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.926
- ___88-[PABSPasscodeLockController showAlertForPhoneAutoUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.896
- ___93-[PABSBiometricController presentConfirmationAndProceedTouchIDForStockholmEnabled:specifier:]_block_invoke.123
- ___block_descriptor_40_e8_32s_e20_v24?0q8"NSError"16ls32l8
- ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0ls32l8s40l8w56l8s48l8
- ___block_descriptor_tmp.150
- ___block_descriptor_tmp.169
- ___block_literal_global.152
- ___block_literal_global.171
- ___block_literal_global.552
- ___block_literal_global.607
- ___block_literal_global.613
- ___block_literal_global.702
- ___block_literal_global.704
- ___block_literal_global.708
- ___block_literal_global.906
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_PasscodeAndBiometricsSettings
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_PasscodeAndBiometricsSettings
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_PasscodeAndBiometricsSettings
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_PasscodeAndBiometricsSettings
- _objc_msgSend$setStoreState:
- _objc_msgSend$updateStoreBiometricsState
CStrings:
+ "%@: Get: %@"
+ "%@: Set: %@ == current"
+ "%@: Set: Requesting StoreBiometrics to %@"
+ "%@: Set: StoreBiometrics set [%@] error %@"
+ "TOUCHID_PURCHASES_ID: Setting storeState to %@"
+ "setStoreState:forceRefresh:"
+ "updateStoreBiometricsStateAndForceRefresh:"
+ "v28@0:8q16B24"
- "Failed to set Touch ID for purchases"
- "updateStoreBiometricsState"
- "updateTouchIDForPurchasesSpecifier"

```
