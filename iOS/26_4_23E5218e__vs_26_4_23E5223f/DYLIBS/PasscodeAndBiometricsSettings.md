## PasscodeAndBiometricsSettings

> `/System/Library/PrivateFrameworks/PasscodeAndBiometricsSettings.framework/PasscodeAndBiometricsSettings`

```diff

-17.4.8.0.0
-  __TEXT.__text: 0x43250
+17.4.9.0.0
+  __TEXT.__text: 0x43400
   __TEXT.__auth_stubs: 0x1530
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0x2324
+  __TEXT.__objc_methlist: 0x2334
   __TEXT.__const: 0x1014
   __TEXT.__gcc_except_tab: 0xb3c
   __TEXT.__cstring: 0x3773
-  __TEXT.__oslogstring: 0x535d
+  __TEXT.__oslogstring: 0x537d
   __TEXT.__dlopen_cstrs: 0x443
   __TEXT.__ustring: 0x4e
   __TEXT.__swift5_typeref: 0x714

   __TEXT.__swift5_types: 0x4c
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x38
-  __TEXT.__unwind_info: 0x1280
+  __TEXT.__unwind_info: 0x1288
   __TEXT.__eh_frame: 0x828
   __TEXT.__objc_classname: 0x6ed
-  __TEXT.__objc_methname: 0x76a0
+  __TEXT.__objc_methname: 0x76e0
   __TEXT.__objc_methtype: 0x1086
-  __TEXT.__objc_stubs: 0x6340
+  __TEXT.__objc_stubs: 0x6380
   __DATA_CONST.__got: 0x778
   __DATA_CONST.__const: 0x10f8
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f00
+  __DATA_CONST.__objc_selrefs: 0x1f10
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DB41C47D-A2F9-39D4-BAC0-6F457E5BCA77
-  Functions: 1441
-  Symbols:   4092
-  CStrings:  2579
+  UUID: 3D0F0C0E-18C8-3943-9240-00A815C15992
+  Functions: 1444
+  Symbols:   4096
+  CStrings:  2582
 
Symbols:
+ -[PABSPasscodeLockController viewWillAppear:]
+ -[PABSPearlPasscodeController startFaceIDEnrollmentWithSpecifier:]
+ -[PABSPearlPasscodeController startFaceIDEnrollmentWithSpecifier:].cold.1
+ GCC_except_table122
+ GCC_except_table124
+ GCC_except_table126
+ GCC_except_table135
+ GCC_except_table155
+ GCC_except_table26
+ GCC_except_table31
+ GCC_except_table41
+ GCC_except_table54
+ GCC_except_table81
+ GCC_except_table85
+ GCC_except_table88
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.596
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.597
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.603
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.603.cold.1
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke_2.599
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeRemoveFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.586
+ ___45-[PABSPasscodeLockController togglePasscode:]_block_invoke.556
+ ___45-[PABSPasscodeLockController togglePasscode:]_block_invoke.556.cold.1
+ ___47-[PABSPasscodeLockController showKeychainAlert]_block_invoke.762
+ ___55-[PABSPasscodeLockController setWipeEnabled:specifier:]_block_invoke.732
+ ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.910
+ ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.910.cold.1
+ ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.911
+ ___63-[PABSPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.656
+ ___63-[PABSPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.660
+ ___69-[PABSPasscodeLockController setEnabledInLockScreenForUSB:specifier:]_block_invoke.888
+ ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.969
+ ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.969.cold.1
+ ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.970
+ ___85-[PABSPasscodeLockController showAlertForVisionUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.974
+ ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.953
+ ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.957
+ ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.964
+ ___88-[PABSPasscodeLockController presentVisionUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.978
+ ___88-[PABSPasscodeLockController presentVisionUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.979
+ ___88-[PABSPasscodeLockController showAlertForPhoneAutoUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.949
+ ___block_literal_global.606
+ ___block_literal_global.662
+ ___block_literal_global.668
+ ___block_literal_global.760
+ ___block_literal_global.764
+ ___block_literal_global.959
+ _objc_msgSend$setPrefersLargeTitles:
+ _objc_msgSend$startFaceIDEnrollmentWithSpecifier:
- GCC_except_table121
- GCC_except_table123
- GCC_except_table125
- GCC_except_table134
- GCC_except_table154
- GCC_except_table28
- GCC_except_table30
- GCC_except_table35
- GCC_except_table53
- GCC_except_table80
- GCC_except_table87
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.590
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.595
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.599
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.599.cold.1
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke_2.597
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeRemoveFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.584
- ___45-[PABSPasscodeLockController togglePasscode:]_block_invoke.554
- ___45-[PABSPasscodeLockController togglePasscode:]_block_invoke.554.cold.1
- ___47-[PABSPasscodeLockController showKeychainAlert]_block_invoke.760
- ___55-[PABSPasscodeLockController setWipeEnabled:specifier:]_block_invoke.730
- ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.908
- ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.908.cold.1
- ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.909
- ___63-[PABSPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.654
- ___63-[PABSPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.658
- ___69-[PABSPasscodeLockController setEnabledInLockScreenForUSB:specifier:]_block_invoke.886
- ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.967
- ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.967.cold.1
- ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.968
- ___85-[PABSPasscodeLockController showAlertForVisionUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.972
- ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.951
- ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.955
- ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.962
- ___88-[PABSPasscodeLockController presentVisionUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.976
- ___88-[PABSPasscodeLockController presentVisionUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.977
- ___88-[PABSPasscodeLockController showAlertForPhoneAutoUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.947
- ___block_literal_global.604
- ___block_literal_global.660
- ___block_literal_global.666
- ___block_literal_global.756
- ___block_literal_global.762
- ___block_literal_global.957
CStrings:
+ "%@: Failed to extract passcode - %@"
+ "setPrefersLargeTitles:"
+ "startFaceIDEnrollmentWithSpecifier:"

```
