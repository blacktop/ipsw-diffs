## PreferencesUI

> `/System/Library/PrivateFrameworks/PreferencesUI.framework/PreferencesUI`

```diff

-1250.3.13.0.0
-  __TEXT.__text: 0x3e1e8
+1250.3.17.0.0
+  __TEXT.__text: 0x43484
   __TEXT.__auth_stubs: 0xde0
-  __TEXT.__objc_methlist: 0x276c
+  __TEXT.__objc_methlist: 0x2a0c
   __TEXT.__const: 0xe6
-  __TEXT.__gcc_except_tab: 0x1084
-  __TEXT.__oslogstring: 0x2a66
-  __TEXT.__cstring: 0x4012
+  __TEXT.__gcc_except_tab: 0x1234
+  __TEXT.__oslogstring: 0x37e2
+  __TEXT.__cstring: 0x47e2
   __TEXT.__dlopen_cstrs: 0x618
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0x28
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1010
-  __TEXT.__objc_classname: 0x762
-  __TEXT.__objc_methname: 0xc0c4
-  __TEXT.__objc_methtype: 0x2306
-  __TEXT.__objc_stubs: 0x9500
+  __TEXT.__unwind_info: 0x1184
+  __TEXT.__objc_classname: 0x7fe
+  __TEXT.__objc_methname: 0xc642
+  __TEXT.__objc_methtype: 0x2335
+  __TEXT.__objc_stubs: 0x9aa0
   __DATA_CONST.__got: 0x4d8
-  __DATA_CONST.__const: 0x1240
-  __DATA_CONST.__objc_classlist: 0xe8
+  __DATA_CONST.__const: 0x1440
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4650
-  __DATA_CONST.__objc_selrefs: 0x2cf0
+  __DATA_CONST.__objc_const: 0x47b0
+  __DATA_CONST.__objc_selrefs: 0x2e70
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__objc_const: 0xbb0
-  __AUTH_CONST.__const: 0x5b0
-  __AUTH_CONST.__cfstring: 0x3f60
-  __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH_CONST.__objc_const: 0xdf0
+  __AUTH_CONST.__const: 0x5d0
+  __AUTH_CONST.__cfstring: 0x4660
+  __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x700
-  __AUTH.__objc_data: 0x4c8
+  __AUTH.__objc_data: 0x608
   __AUTH.__data: 0xc0
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x530
-  __DATA.__objc_superrefs: 0xd8
-  __DATA.__objc_ivar: 0x268
+  __DATA.__objc_classrefs: 0x570
+  __DATA.__objc_superrefs: 0xe0
+  __DATA.__objc_ivar: 0x284
   __DATA.__data: 0xdf0
   __DATA.__bss: 0x130
   __DATA.__common: 0x18

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 465109CA-B57F-35FE-B35F-376C1E539DE9
-  Functions: 1283
-  Symbols:   5155
-  CStrings:  3624
+  UUID: AC547A75-8118-3E49-8587-E34031E4178C
+  Functions: 1415
+  Symbols:   5526
+  CStrings:  3863
 
Symbols:
+ +[PSUIDeviceTakeOverController isRatchetFeatureAvailable]
+ +[PSUIRatchetedOperationGroupNameTransformer allowsReverseTransformation]
+ +[PSUIRatchetedOperationGroupNameTransformer transformedValueClass]
+ +[PSUIRatchetedOperationNameDetailedTransformer allowsReverseTransformation]
+ +[PSUIRatchetedOperationNameDetailedTransformer transformedValueClass]
+ +[PSUIRatchetedOperationNameTransformer allowsReverseTransformation]
+ +[PSUIRatchetedOperationNameTransformer transformedValueClass]
+ -[PSUIBiometricController dtoController]
+ -[PSUIBiometricController presentConfirmationAndProceedTouchIDForStockholmEnabled:specifier:]
+ -[PSUIBiometricController setDtoController:]
+ -[PSUIDeviceTakeOverController .cxx_destruct]
+ -[PSUIDeviceTakeOverController dealloc]
+ -[PSUIDeviceTakeOverController disableRatchetWithCompletion:]
+ -[PSUIDeviceTakeOverController enableRatchetWithCompletion:]
+ -[PSUIDeviceTakeOverController gateWithRatchetForOperation:completion:]
+ -[PSUIDeviceTakeOverController isRatchetEnabled]
+ -[PSUIDeviceTakeOverController laContext]
+ -[PSUIDeviceTakeOverController setLaContext:]
+ -[PSUIFingerprintController dtoController]
+ -[PSUIFingerprintController setDtoController:]
+ -[PSUIPasscodeLockController cdpCircleExists]
+ -[PSUIPasscodeLockController cdpCircleExists].cold.1
+ -[PSUIPasscodeLockController disableDTO:]
+ -[PSUIPasscodeLockController dtoController]
+ -[PSUIPasscodeLockController enableDTO:]
+ -[PSUIPasscodeLockController ensureAccountSecurityIsSufficientWithCompletion:]
+ -[PSUIPasscodeLockController ensureAccountSecurityIsSufficientWithCompletion:].cold.1
+ -[PSUIPasscodeLockController getDTOSpecifiers]
+ -[PSUIPasscodeLockController getDTOStatusForSpecifier:]
+ -[PSUIPasscodeLockController isFindMyEnabled]
+ -[PSUIPasscodeLockController openDTOFooterHelpLink]
+ -[PSUIPasscodeLockController performPreEnableDTOChecksWithCompletion:]
+ -[PSUIPasscodeLockController psCellForSpecifier:]
+ -[PSUIPasscodeLockController refreshCellForSpecifier:]
+ -[PSUIPasscodeLockController setDtoController:]
+ -[PSUIPasscodeLockController setIsFindMyEnabled:]
+ -[PSUIPasscodeLockController setNameForDTOToggle:]
+ -[PSUIPasscodeLockController setUpFindMyEnablementStatus]
+ -[PSUIPasscodeLockController setValueForDTOStatusLabel]
+ -[PSUIPasscodeLockController showAlertForFindMyIsDisabledWithCompletion:]
+ -[PSUIPasscodeLockController showDTOAlertForFailureToToggleToState:]
+ -[PSUIPasscodeLockController toggleDTO:]
+ -[PSUIPasscodeLockController toggledDTOSuccessfully:]
+ -[PSUIPasscodeLockController updateFooterForDTOGroupSpecifier:]
+ -[PSUIPearlPasscodeController dtoController]
+ -[PSUIPearlPasscodeController setDtoController:]
+ -[PSUIRatchetedOperationGroupNameTransformer transformedValue:]
+ -[PSUIRatchetedOperationNameDetailedTransformer transformedValue:]
+ -[PSUIRatchetedOperationNameTransformer transformedValue:]
+ -[PSUITouchIDPasscodeController dtoController]
+ -[PSUITouchIDPasscodeController setDtoController:]
+ GCC_except_table125
+ GCC_except_table129
+ GCC_except_table151
+ GCC_except_table23
+ GCC_except_table26
+ GCC_except_table33
+ GCC_except_table35
+ GCC_except_table40
+ GCC_except_table44
+ GCC_except_table57
+ GCC_except_table60
+ GCC_except_table67
+ GCC_except_table71
+ GCC_except_table76
+ GCC_except_table80
+ GCC_except_table83
+ GCC_except_table88
+ GCC_except_table99
+ _OBJC_CLASS_$_CDPStateController
+ _OBJC_CLASS_$_CDPUIDeviceToDeviceEncryptionFlowContext
+ _OBJC_CLASS_$_CDPUIDeviceToDeviceEncryptionHelper
+ _OBJC_CLASS_$_FMDFMIPManager
+ _OBJC_CLASS_$_LARatchet
+ _OBJC_CLASS_$_LARatchetManager
+ _OBJC_CLASS_$_NSValueTransformer
+ _OBJC_CLASS_$_PSUIDeviceTakeOverController
+ _OBJC_CLASS_$_PSUIRatchetedOperationGroupNameTransformer
+ _OBJC_CLASS_$_PSUIRatchetedOperationNameDetailedTransformer
+ _OBJC_CLASS_$_PSUIRatchetedOperationNameTransformer
+ _OBJC_IVAR_$_PSUIBiometricController._dtoController
+ _OBJC_IVAR_$_PSUIDeviceTakeOverController._laContext
+ _OBJC_IVAR_$_PSUIFingerprintController._dtoController
+ _OBJC_IVAR_$_PSUIPasscodeLockController._dtoController
+ _OBJC_IVAR_$_PSUIPasscodeLockController._isFindMyEnabled
+ _OBJC_IVAR_$_PSUIPearlPasscodeController._dtoController
+ _OBJC_IVAR_$_PSUITouchIDPasscodeController._dtoController
+ _OBJC_METACLASS_$_NSValueTransformer
+ _OBJC_METACLASS_$_PSUIDeviceTakeOverController
+ _OBJC_METACLASS_$_PSUIRatchetedOperationGroupNameTransformer
+ _OBJC_METACLASS_$_PSUIRatchetedOperationNameDetailedTransformer
+ _OBJC_METACLASS_$_PSUIRatchetedOperationNameTransformer
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _PSUI_LocalizedStringForPasscodeDimpleKey
+ __OBJC_$_CLASS_METHODS_PSUIDeviceTakeOverController
+ __OBJC_$_CLASS_METHODS_PSUIRatchetedOperationGroupNameTransformer
+ __OBJC_$_CLASS_METHODS_PSUIRatchetedOperationNameDetailedTransformer
+ __OBJC_$_CLASS_METHODS_PSUIRatchetedOperationNameTransformer
+ __OBJC_$_INSTANCE_METHODS_PSUIDeviceTakeOverController
+ __OBJC_$_INSTANCE_METHODS_PSUIRatchetedOperationGroupNameTransformer
+ __OBJC_$_INSTANCE_METHODS_PSUIRatchetedOperationNameDetailedTransformer
+ __OBJC_$_INSTANCE_METHODS_PSUIRatchetedOperationNameTransformer
+ __OBJC_$_INSTANCE_VARIABLES_PSUIDeviceTakeOverController
+ __OBJC_$_PROP_LIST_PSUIDeviceTakeOverController
+ __OBJC_CLASS_RO_$_PSUIDeviceTakeOverController
+ __OBJC_CLASS_RO_$_PSUIRatchetedOperationGroupNameTransformer
+ __OBJC_CLASS_RO_$_PSUIRatchetedOperationNameDetailedTransformer
+ __OBJC_CLASS_RO_$_PSUIRatchetedOperationNameTransformer
+ __OBJC_METACLASS_RO_$_PSUIDeviceTakeOverController
+ __OBJC_METACLASS_RO_$_PSUIRatchetedOperationGroupNameTransformer
+ __OBJC_METACLASS_RO_$_PSUIRatchetedOperationNameDetailedTransformer
+ __OBJC_METACLASS_RO_$_PSUIRatchetedOperationNameTransformer
+ ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.154
+ ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.156
+ ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.161
+ ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.161.cold.1
+ ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.161.cold.2
+ ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.163
+ ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.163.cold.1
+ ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke_2.159
+ ___38-[PSUIPearlPasscodeController enroll:]_block_invoke
+ ___38-[PSUIPearlPasscodeController enroll:]_block_invoke.103
+ ___38-[PSUIPearlPasscodeController enroll:]_block_invoke.103.cold.1
+ ___38-[PSUIPearlPasscodeController enroll:]_block_invoke.cold.1
+ ___40-[PSUIPasscodeLockController enableDTO:]_block_invoke
+ ___40-[PSUIPasscodeLockController enableDTO:]_block_invoke.282
+ ___40-[PSUIPasscodeLockController enableDTO:]_block_invoke.282.cold.1
+ ___40-[PSUIPasscodeLockController enableDTO:]_block_invoke.283
+ ___40-[PSUIPasscodeLockController enableDTO:]_block_invoke.283.cold.1
+ ___40-[PSUIPasscodeLockController enableDTO:]_block_invoke.284
+ ___41-[PSUIPasscodeLockController disableDTO:]_block_invoke
+ ___41-[PSUIPasscodeLockController disableDTO:]_block_invoke.293
+ ___41-[PSUIPasscodeLockController disableDTO:]_block_invoke.293.cold.1
+ ___41-[PSUIPasscodeLockController disableDTO:]_block_invoke.294
+ ___41-[PSUIPasscodeLockController disableDTO:]_block_invoke.294.cold.1
+ ___41-[PSUIPasscodeLockController disableDTO:]_block_invoke.295
+ ___41-[PSUIPasscodeLockController disableDTO:]_block_invoke.295.cold.1
+ ___41-[PSUIPasscodeLockController disableDTO:]_block_invoke.296
+ ___41-[PSUIPasscodeLockController disableDTO:]_block_invoke.cold.1
+ ___45-[PSUIPasscodeLockController togglePasscode:]_block_invoke
+ ___45-[PSUIPasscodeLockController togglePasscode:]_block_invoke.116
+ ___45-[PSUIPasscodeLockController togglePasscode:]_block_invoke.116.cold.1
+ ___45-[PSUIPasscodeLockController togglePasscode:]_block_invoke.cold.1
+ ___47-[PSUIFingerprintController deleteFingerprint:]_block_invoke
+ ___47-[PSUIFingerprintController deleteFingerprint:]_block_invoke.269
+ ___47-[PSUIFingerprintController deleteFingerprint:]_block_invoke.269.cold.1
+ ___47-[PSUIFingerprintController deleteFingerprint:]_block_invoke.cold.1
+ ___47-[PSUIPasscodeLockController showKeychainAlert]_block_invoke.384
+ ___47-[PSUITouchIDPasscodeController addEnrollment:]_block_invoke
+ ___47-[PSUITouchIDPasscodeController addEnrollment:]_block_invoke.87
+ ___47-[PSUITouchIDPasscodeController addEnrollment:]_block_invoke.87.cold.1
+ ___47-[PSUITouchIDPasscodeController addEnrollment:]_block_invoke.cold.1
+ ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke.265
+ ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke.267
+ ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke_2.268
+ ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke_2.268.cold.1
+ ___51-[PSUIPasscodeLockController openDTOFooterHelpLink]_block_invoke
+ ___51-[PSUIPasscodeLockController openDTOFooterHelpLink]_block_invoke.cold.1
+ ___56-[PSUIPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.548
+ ___57-[PSUIPasscodeLockController setUpFindMyEnablementStatus]_block_invoke
+ ___57-[PSUIPasscodeLockController setUpFindMyEnablementStatus]_block_invoke.cold.1
+ ___60-[PSUIDeviceTakeOverController enableRatchetWithCompletion:]_block_invoke
+ ___60-[PSUIDeviceTakeOverController enableRatchetWithCompletion:]_block_invoke.cold.1
+ ___61-[PSUIDeviceTakeOverController disableRatchetWithCompletion:]_block_invoke
+ ___61-[PSUIDeviceTakeOverController disableRatchetWithCompletion:]_block_invoke.cold.1
+ ___62-[PSUIBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke.157
+ ___62-[PSUIBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke.158
+ ___62-[PSUIBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke_2
+ ___62-[PSUIBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke_2.cold.1
+ ___62-[PSUIBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke_2.cold.2
+ ___63-[PSUIPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.217
+ ___66-[PSUIPearlPasscodeController enrollGlassesForExistingAppearance:]_block_invoke
+ ___66-[PSUIPearlPasscodeController enrollGlassesForExistingAppearance:]_block_invoke.141
+ ___66-[PSUIPearlPasscodeController enrollGlassesForExistingAppearance:]_block_invoke.141.cold.1
+ ___66-[PSUIPearlPasscodeController enrollGlassesForExistingAppearance:]_block_invoke.cold.1
+ ___67-[PSUIBiometricController setTouchIDForStockholmEnabled:specifier:]_block_invoke_2.cold.1
+ ___67-[PSUIBiometricController setTouchIDForStockholmEnabled:specifier:]_block_invoke_2.cold.2
+ ___68-[PSUIPasscodeLockController showDTOAlertForFailureToToggleToState:]_block_invoke
+ ___69-[PSUIPearlPasscodeController enrollPeriocularForExistingAppearance:]_block_invoke
+ ___69-[PSUIPearlPasscodeController enrollPeriocularForExistingAppearance:]_block_invoke_2
+ ___69-[PSUIPearlPasscodeController enrollPeriocularForExistingAppearance:]_block_invoke_2.cold.1
+ ___69-[PSUIPearlPasscodeController enrollPeriocularForExistingAppearance:]_block_invoke_2.cold.2
+ ___70-[PSUIPasscodeLockController performPreEnableDTOChecksWithCompletion:]_block_invoke
+ ___71-[PSUIDeviceTakeOverController gateWithRatchetForOperation:completion:]_block_invoke
+ ___71-[PSUIDeviceTakeOverController gateWithRatchetForOperation:completion:]_block_invoke.cold.1
+ ___71-[PSUIDeviceTakeOverController gateWithRatchetForOperation:completion:]_block_invoke.cold.2
+ ___72-[PSUIPearlPasscodeController deleteFaceIDIdentitiesCheckWithSpecifier:]_block_invoke
+ ___72-[PSUIPearlPasscodeController deleteFaceIDIdentitiesCheckWithSpecifier:]_block_invoke.271
+ ___72-[PSUIPearlPasscodeController deleteFaceIDIdentitiesCheckWithSpecifier:]_block_invoke.271.cold.1
+ ___72-[PSUIPearlPasscodeController deleteFaceIDIdentitiesCheckWithSpecifier:]_block_invoke.cold.1
+ ___73-[PSUIPasscodeLockController showAlertForFindMyIsDisabledWithCompletion:]_block_invoke
+ ___78-[PSUIPasscodeLockController ensureAccountSecurityIsSufficientWithCompletion:]_block_invoke
+ ___82-[PSUIFingerprintController presentAlertSheetForFingerprintBindingToGovernmentID:]_block_invoke.250
+ ___86-[PSUIPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.565
+ ___86-[PSUIPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.569
+ ___86-[PSUIPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.576
+ ___88-[PSUIPasscodeLockController showAlertForPhoneAutoUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.561
+ ___93-[PSUIBiometricController presentConfirmationAndProceedTouchIDForStockholmEnabled:specifier:]_block_invoke
+ ___93-[PSUIBiometricController presentConfirmationAndProceedTouchIDForStockholmEnabled:specifier:]_block_invoke_2
+ ___block_descriptor_33_e23_v16?0"UIAlertAction"8l
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32w_e20_v24?0Q8"NSError"16lw32l8
+ ___block_descriptor_48_e8_32bs40w_e34_v24?0"NSDictionary"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e8_v16?0Q8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48w_e8_v16?0Q8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_64_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_literal_global.186
+ ___block_literal_global.211
+ ___block_literal_global.213
+ ___block_literal_global.219
+ ___block_literal_global.227
+ ___block_literal_global.271
+ ___block_literal_global.273
+ ___block_literal_global.293
+ ___block_literal_global.295
+ ___block_literal_global.325
+ ___block_literal_global.380
+ ___block_literal_global.382
+ ___block_literal_global.386
+ ___block_literal_global.571
+ _objc_msgSend$armWithOptions:completion:
+ _objc_msgSend$cdpCircleExists
+ _objc_msgSend$disableDTO:
+ _objc_msgSend$disableFeatureWithContext:completion:
+ _objc_msgSend$disableRatchetWithCompletion:
+ _objc_msgSend$dtoController
+ _objc_msgSend$enableDTO:
+ _objc_msgSend$enableFeatureWithReply:
+ _objc_msgSend$enableRatchetWithCompletion:
+ _objc_msgSend$ensureAccountSecurityIsSufficientWithCompletion:
+ _objc_msgSend$fmipStateWithCompletion:
+ _objc_msgSend$gateWithRatchetForOperation:completion:
+ _objc_msgSend$getDTOSpecifiers
+ _objc_msgSend$getDTOStatusForSpecifier:
+ _objc_msgSend$initWithAltDSID:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$isFeatureAvailable
+ _objc_msgSend$isFeatureEnabled
+ _objc_msgSend$isFeatureSupported
+ _objc_msgSend$isFindMyEnabled
+ _objc_msgSend$isManateeAvailable:
+ _objc_msgSend$isRatchetEnabled
+ _objc_msgSend$isRatchetFeatureAvailable
+ _objc_msgSend$laContext
+ _objc_msgSend$performDeviceToDeviceEncryptionStateRepairWithCompletion:
+ _objc_msgSend$performPreEnableDTOChecksWithCompletion:
+ _objc_msgSend$presentConfirmationAndProceedTouchIDForStockholmEnabled:specifier:
+ _objc_msgSend$psCellForSpecifier:
+ _objc_msgSend$refreshCellContentsWithSpecifier:
+ _objc_msgSend$refreshCellForSpecifier:
+ _objc_msgSend$setDeviceToDeviceEncryptionUpgradeType:
+ _objc_msgSend$setDeviceToDeviceEncryptionUpgradeUIStyle:
+ _objc_msgSend$setFeatureName:
+ _objc_msgSend$setIsFindMyEnabled:
+ _objc_msgSend$setLaContext:
+ _objc_msgSend$setNameForDTOToggle:
+ _objc_msgSend$setUpFindMyEnablementStatus
+ _objc_msgSend$setValueForDTOStatusLabel
+ _objc_msgSend$showAlertForFindMyIsDisabledWithCompletion:
+ _objc_msgSend$showDTOAlertForFailureToToggleToState:
+ _objc_msgSend$toggleToState:forIdentifier:
+ _objc_msgSend$toggledDTOSuccessfully:
+ _objc_msgSend$transformedValue:
+ _objc_msgSend$updateFooterForDTOGroupSpecifier:
+ _objc_msgSend$valueTransformerForName:
- GCC_except_table116
- GCC_except_table14
- GCC_except_table22
- GCC_except_table41
- GCC_except_table55
- GCC_except_table63
- GCC_except_table75
- GCC_except_table90
- GCC_except_table94
- ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.148
- ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.150
- ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.153
- ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.157.cold.1
- ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.157.cold.2
- ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.159
- ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.159.cold.1
- ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke_2.155
- ___47-[PSUIPasscodeLockController showKeychainAlert]_block_invoke.305
- ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke.256
- ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke.258
- ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke_2.259
- ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke_2.259.cold.1
- ___56-[PSUIPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.470
- ___63-[PSUIPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.213
- ___82-[PSUIFingerprintController presentAlertSheetForFingerprintBindingToGovernmentID:]_block_invoke.241
- ___86-[PSUIPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.487
- ___86-[PSUIPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.491
- ___86-[PSUIPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.498
- ___88-[PSUIPasscodeLockController showAlertForPhoneAutoUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.483
- ___block_literal_global.182
- ___block_literal_global.205
- ___block_literal_global.207
- ___block_literal_global.215
- ___block_literal_global.223
- ___block_literal_global.261
- ___block_literal_global.263
- ___block_literal_global.288
- ___block_literal_global.290
- ___block_literal_global.301
- ___block_literal_global.303
- ___block_literal_global.307
- ___block_literal_global.493
CStrings:
+ "\x04"
+ "\x12\x15"
+ "\x17"
+ "3\x13"
+ "@\"PSUIDeviceTakeOverController\""
+ "Account security: CDP Circle: %@ Error: %@"
+ "Account security: No need to Upgrade"
+ "Account security: Upgrading [Failed] - %@"
+ "Account security: Upgrading [Failed] since HSA2 [%@] CDPCircle [%@] - Repaired: %@ Error: %@"
+ "Account security: Upgrading [Success] - Repaired: %@"
+ "Account security: Upgrading since HSA2 [%@] CDPCircle [%@]"
+ "BiometricForPasswordAutoFill"
+ "BiometricForWalletAndApplePay"
+ "DTO: Failed to open support link."
+ "DTO: Turn %@ Protection [Failed] - Alert [Dismissed]"
+ "DTO: Turn %@ Protection [Failed] - Alert [Shown]"
+ "DTO: Turn Off Protection [Failed]"
+ "DTO: Turn Off Protection [Failed] - No instance (self)"
+ "DTO: Turn Off Protection [Failed] as we are Ratcheted"
+ "DTO: Turn Off Protection [Proceeding]"
+ "DTO: Turn Off Protection [Success]"
+ "DTO: Turn On Protection [Failed]"
+ "DTO: Turn On Protection [Failed] - No instance (self)"
+ "DTO: Turn On Protection [Performing prechecks]"
+ "DTO: Turn On Protection [Prechecks: %@]"
+ "DTO: Turn On Protection [Success]"
+ "DTO: Unavailable"
+ "DTO: User pressed Turn Off Protection"
+ "DTO: User pressed Turn On Protection"
+ "DTO_ALERT_COULD_NOT_TOGGLE_OK_BUTTON"
+ "DTO_ALERT_COULD_NOT_TOGGLE_TO_OFF_TITLE"
+ "DTO_ALERT_COULD_NOT_TOGGLE_TO_ON_TITLE"
+ "DTO_ALERT_MUST_TURN_ON_FIND_MY_TITLE"
+ "DTO_ALERT_MUST_UPGRADE_ACCOUNT_SECURITY"
+ "DTO_GROUP_FOOTER_DESCRIPTION_FACE_ID"
+ "DTO_GROUP_FOOTER_DESCRIPTION_SUFFIX_LINK"
+ "DTO_GROUP_FOOTER_DESCRIPTION_TOUCH_ID"
+ "DTO_GROUP_ID"
+ "DTO_NOTIFICATION_DESCRIPTION_DEFAULT"
+ "DTO_OPERATION_DESCRIPTION_ADD_FINGERPRINT"
+ "DTO_OPERATION_DESCRIPTION_DEFAULT"
+ "DTO_OPERATION_DESCRIPTION_DELETE_FINGERPRINT"
+ "DTO_OPERATION_DESCRIPTION_DISABLE_USING_FACE_ID_FOR_FEATURES"
+ "DTO_OPERATION_DESCRIPTION_DISABLE_USING_TOUCH_ID_FOR_FEATURES"
+ "DTO_OPERATION_DESCRIPTION_RESET_FACE_ID"
+ "DTO_OPERATION_DESCRIPTION_SET_UP_FACE_ID"
+ "DTO_OPERATION_DESCRIPTION_SET_UP_FACE_ID_WITH_GLASSES"
+ "DTO_OPERATION_DESCRIPTION_SET_UP_FACE_ID_WITH_MASK"
+ "DTO_OPERATION_DESCRIPTION_TURN_OFF_PASSCODE"
+ "DTO_OPERATION_DESCRIPTION_TURN_OFF_STOLEN_DEVICE_PROTECTION"
+ "DTO_OPERATION_TITLE_NAME_CHANGE_FACE_ID"
+ "DTO_OPERATION_TITLE_NAME_CHANGE_PASSCODE"
+ "DTO_OPERATION_TITLE_NAME_CHANGE_STOLEN_DEVICE_PROTECTION"
+ "DTO_OPERATION_TITLE_NAME_CHANGE_TOUCH_ID"
+ "DTO_OPERATION_TITLE_NAME_DEFAULT"
+ "DTO_OPERATION_TITLE_NAME_ENROLL_FACE_ID"
+ "DTO_OPERATION_TITLE_NAME_ENROLL_TOUCH_ID"
+ "DTO_SECURITY_DELAY_BEGIN_DESCRIPTION_DEFAULT"
+ "DTO_SECURITY_DELAY_BEGIN_TITLE"
+ "DTO_SECURITY_DELAY_IN_PROGRESS_DESCRIPTION"
+ "DTO_SECURITY_FALLBACK_AUTHENTICATION_DESCRIPTION"
+ "DTO_STATUS_LABEL_DESCRIPTION"
+ "DTO_STATUS_LABEL_DESCRIPTION_STATE_OFF"
+ "DTO_STATUS_LABEL_DESCRIPTION_STATE_ON"
+ "DTO_STATUS_LABEL_ID"
+ "DTO_TOGGLE_BUTTON_DESCRIPTON_OFF"
+ "DTO_TOGGLE_BUTTON_DESCRIPTON_ON"
+ "DTO_TOGGLE_BUTTON_ID"
+ "Default"
+ "DimpleKey"
+ "Face ID: Not enrolling as we are Ratcheted"
+ "Face ID: Not enrolling as we are missing instance (self)"
+ "Face ID: Not enrolling periocular for existing appearance as we are Ratcheted"
+ "Face ID: Not enrolling periocular for existing appearance as we are missing instance (self)"
+ "Face ID: Not enrolling with Add Glasses as we are Ratcheted"
+ "Face ID: Not enrolling with Add Glasses as we are missing instance (self)"
+ "Face ID: Not resetting as we are Ratcheted"
+ "Face ID: Not resetting as we are missing instance (self)"
+ "Face ID: Resetting"
+ "Face ID: Starting enrollment"
+ "Face ID: Starting enrollment of periocular for existing appearance"
+ "Face ID: Starting enrollment with Add Glasses"
+ "FaceID"
+ "Find My Device: %@"
+ "Find My Device: Failed to retrieve state: %@"
+ "Find My Device: Failed to set property - No instance (self)"
+ "Find My: Alert [Dismissed]"
+ "Find My: Alert [Shown]"
+ "PSMultilineTableCell"
+ "PSUIDeviceTakeOverController"
+ "PSUIRatchetedOperationGroupNameTransformer"
+ "PSUIRatchetedOperationNameDetailedTransformer"
+ "PSUIRatchetedOperationNameTransformer"
+ "PasscodeLock-DimpleKey"
+ "Ratchet: Cannot proceed to perform critical operation as gating failed - Error: %@ - %@"
+ "Ratchet: Cannot proceed to perform critical operation as gating was successful but we are missing instance (self)"
+ "Ratchet: Current status [%@]"
+ "Ratchet: Disabled successfully"
+ "Ratchet: Enabled successfully"
+ "Ratchet: Failed to disable - Error: %@"
+ "Ratchet: Failed to enable - Error: %@"
+ "Ratchet: Performing gating check for identifier: %lu"
+ "Ratchet: Proceeding to perform critical operation as gating is not required"
+ "Ratchet: Proceeding to perform critical operation as gating was successful"
+ "SettingsPasscodePane_"
+ "StolenDeviceProtection"
+ "T@\"LAContext\",&,N,V_laContext"
+ "T@\"PSUIDeviceTakeOverController\",&,N,V_dtoController"
+ "TB,N,V_isFindMyEnabled"
+ "Touch ID: Not adding a fingerprint as we are Ratcheted"
+ "Touch ID: Not adding fingerprint as we are missing instance (self)"
+ "Touch ID: Not deleting fingerprint as we are Ratcheted"
+ "Touch ID: Not deleting fingerprint as we are missing instance (self)"
+ "Touch ID: Starting addition of fingerprint"
+ "Touch ID: Starting deletion of fingerprint"
+ "TouchID"
+ "Turn Off Passcode: Not proceeding - missing instance (self)"
+ "Turn Off Passcode: Not turning off as we are Ratcheted"
+ "Turn Off Passcode: Proceeding"
+ "Using biometric for Password AutoFill: Not toggling to Off as we are Ratcheted"
+ "Using biometric for Password AutoFill: Not toggling to Off as we are are missing instance (self)"
+ "Using biometric for Password AutoFill: Toggling to Off "
+ "Using biometric for Password AutoFill: User toggled to %@"
+ "Using biometric for Wallet & Apple Pay: Not toggling to Off as we are Ratcheted"
+ "Using biometric for Wallet & Apple Pay: Not toggling to Off as we are are missing instance (self)"
+ "Using biometric for Wallet & Apple Pay: Toggling to Off "
+ "Using biometric for Wallet & Apple Pay: User toggled to %@"
+ "_Ratchet_Identifier"
+ "_dtoController"
+ "_isFindMyEnabled"
+ "_laContext"
+ "allowsReverseTransformation"
+ "armWithOptions:completion:"
+ "cdpCircleExists"
+ "disableDTO:"
+ "disableFeatureWithContext:completion:"
+ "disableRatchetWithCompletion:"
+ "dtoController"
+ "enableDTO:"
+ "enableFeatureWithReply:"
+ "enableRatchetWithCompletion:"
+ "ensureAccountSecurityIsSufficientWithCompletion:"
+ "fmipStateWithCompletion:"
+ "gateWithRatchetForOperation:completion:"
+ "getDTOSpecifiers"
+ "getDTOStatusForSpecifier:"
+ "https://support.apple.com/kb/HT212510"
+ "initWithAltDSID:"
+ "initWithIdentifier:"
+ "isFeatureAvailable"
+ "isFeatureEnabled"
+ "isFeatureSupported"
+ "isFindMyEnabled"
+ "isManateeAvailable:"
+ "isRatchetEnabled"
+ "isRatchetFeatureAvailable"
+ "laContext"
+ "openDTOFooterHelpLink"
+ "performDeviceToDeviceEncryptionStateRepairWithCompletion:"
+ "performPreEnableDTOChecksWithCompletion:"
+ "prefs:root=PASSCODE"
+ "presentConfirmationAndProceedTouchIDForStockholmEnabled:specifier:"
+ "psCellForSpecifier:"
+ "refreshCellForSpecifier:"
+ "setDeviceToDeviceEncryptionUpgradeType:"
+ "setDeviceToDeviceEncryptionUpgradeUIStyle:"
+ "setDtoController:"
+ "setFeatureName:"
+ "setIsFindMyEnabled:"
+ "setLaContext:"
+ "setNameForDTOToggle:"
+ "setUpFindMyEnablementStatus"
+ "setValueForDTOStatusLabel"
+ "showAlertForFindMyIsDisabledWithCompletion:"
+ "showDTOAlertForFailureToToggleToState:"
+ "toggleDTO:"
+ "toggledDTOSuccessfully:"
+ "transformedValue:"
+ "transformedValueClass"
+ "updateFooterForDTOGroupSpecifier:"
+ "v24@?0Q8@\"NSError\"16"
+ "v32@0:8Q16@?24"
+ "valueTransformerForName:"
- "\x03"
- "\x12\x14"
- "\x16"
- "3\x12"

```
