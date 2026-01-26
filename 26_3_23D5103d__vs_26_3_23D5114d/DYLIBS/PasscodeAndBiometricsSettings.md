## PasscodeAndBiometricsSettings

> `/System/Library/PrivateFrameworks/PasscodeAndBiometricsSettings.framework/PasscodeAndBiometricsSettings`

```diff

 17.2.1.0.0
-  __TEXT.__text: 0x31040
+  __TEXT.__text: 0x31060
   __TEXT.__auth_stubs: 0xc20
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0xdc

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C23D7352-1F79-39CD-9379-C7916B67B0F0
+  UUID: D3E9378D-456A-3590-8197-7CFB807938D1
   Functions: 1058
   Symbols:   3748
   CStrings:  2417
Symbols:
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.557
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.558
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.562
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.562.cold.1
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.564
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.564.cold.1
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke_2.560
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeRemoveFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.547
+ ___45-[PABSPasscodeLockController togglePasscode:]_block_invoke.515
+ ___45-[PABSPasscodeLockController togglePasscode:]_block_invoke.515.cold.1
+ ___47-[PABSPasscodeLockController showKeychainAlert]_block_invoke.722
+ ___55-[PABSPasscodeLockController setWipeEnabled:specifier:]_block_invoke.692
+ ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.873
+ ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.873.cold.1
+ ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.874
+ ___63-[PABSPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.616
+ ___63-[PABSPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.620
+ ___69-[PABSPasscodeLockController setEnabledInLockScreenForUSB:specifier:]_block_invoke.851
+ ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.932
+ ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.932.cold.1
+ ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.933
+ ___85-[PABSPasscodeLockController showAlertForVisionUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.937
+ ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.916
+ ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.920
+ ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.927
+ ___88-[PABSPasscodeLockController presentVisionUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.941
+ ___88-[PABSPasscodeLockController presentVisionUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.942
+ ___88-[PABSPasscodeLockController showAlertForPhoneAutoUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.912
+ ___block_literal_global.567
+ ___block_literal_global.622
+ ___block_literal_global.628
+ ___block_literal_global.718
+ ___block_literal_global.720
+ ___block_literal_global.724
+ ___block_literal_global.922
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.544
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.546
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.548
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.549
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.553.cold.1
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.555.cold.1
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke_2.551
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeRemoveFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.538
- ___45-[PABSPasscodeLockController togglePasscode:]_block_invoke.506
- ___45-[PABSPasscodeLockController togglePasscode:]_block_invoke.506.cold.1
- ___47-[PABSPasscodeLockController showKeychainAlert]_block_invoke.713
- ___55-[PABSPasscodeLockController setWipeEnabled:specifier:]_block_invoke.683
- ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.864
- ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.864.cold.1
- ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.865
- ___63-[PABSPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.607
- ___63-[PABSPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.611
- ___69-[PABSPasscodeLockController setEnabledInLockScreenForUSB:specifier:]_block_invoke.842
- ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.923
- ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.923.cold.1
- ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.924
- ___85-[PABSPasscodeLockController showAlertForVisionUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.928
- ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.907
- ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.911
- ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.918
- ___88-[PABSPasscodeLockController presentVisionUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.932
- ___88-[PABSPasscodeLockController presentVisionUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.933
- ___88-[PABSPasscodeLockController showAlertForPhoneAutoUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.903
- ___block_literal_global.558
- ___block_literal_global.613
- ___block_literal_global.619
- ___block_literal_global.709
- ___block_literal_global.711
- ___block_literal_global.715
- ___block_literal_global.913
Functions:
~ ___swift_instantiateConcreteTypeFromMangledNameV2 : 72 -> 84
~ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2 : 72 -> 92

```
