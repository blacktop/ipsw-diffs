## DigitalSeparationUI

> `/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`

```diff

-552.0.0.0.0
-  __TEXT.__text: 0x51828
-  __TEXT.__auth_stubs: 0xfb0
-  __TEXT.__objc_methlist: 0x5118
-  __TEXT.__cstring: 0x4361
+565.0.1.0.0
+  __TEXT.__text: 0x52628
+  __TEXT.__auth_stubs: 0x1000
+  __TEXT.__objc_methlist: 0x50c8
+  __TEXT.__cstring: 0x4411
   __TEXT.__const: 0x6b4
-  __TEXT.__gcc_except_tab: 0x6f4
-  __TEXT.__oslogstring: 0x254e
-  __TEXT.__dlopen_cstrs: 0x2ba
-  __TEXT.__swift5_typeref: 0x51a
-  __TEXT.__swift5_capture: 0x27c
+  __TEXT.__gcc_except_tab: 0x6e8
+  __TEXT.__oslogstring: 0x266e
+  __TEXT.__dlopen_cstrs: 0x332
+  __TEXT.__swift5_typeref: 0x570
+  __TEXT.__swift5_capture: 0x28c
   __TEXT.__constg_swiftt: 0x27c
   __TEXT.__swift5_reflstr: 0x143
   __TEXT.__swift5_fieldmd: 0x120

   __TEXT.__swift_as_entry: 0x68
   __TEXT.__swift_as_ret: 0x74
   __TEXT.__swift5_assocty: 0x50
-  __TEXT.__unwind_info: 0x1598
+  __TEXT.__unwind_info: 0x15a0
   __TEXT.__eh_frame: 0x9f8
   __TEXT.__objc_classname: 0x968
-  __TEXT.__objc_methname: 0xd885
-  __TEXT.__objc_methtype: 0x28a3
-  __TEXT.__objc_stubs: 0x9ce0
-  __DATA_CONST.__got: 0x890
-  __DATA_CONST.__const: 0x1080
+  __TEXT.__objc_methname: 0xd909
+  __TEXT.__objc_methtype: 0x28ad
+  __TEXT.__objc_stubs: 0x9d00
+  __DATA_CONST.__got: 0x8a8
+  __DATA_CONST.__const: 0x1118
   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x33b8
+  __DATA_CONST.__objc_selrefs: 0x33c8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0xa0
-  __AUTH_CONST.__auth_got: 0x7e8
-  __AUTH_CONST.__const: 0xe58
+  __AUTH_CONST.__auth_got: 0x810
+  __AUTH_CONST.__const: 0xea0
   __AUTH_CONST.__cfstring: 0x4600
-  __AUTH_CONST.__objc_const: 0x10498
+  __AUTH_CONST.__objc_const: 0x10438
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH.__objc_data: 0x11e8
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x43c
-  __DATA.__data: 0xce0
-  __DATA.__bss: 0x568
+  __DATA.__objc_ivar: 0x434
+  __DATA.__data: 0xce8
+  __DATA.__bss: 0x588
   __DATA.__common: 0x1f8
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__data: 0x40

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A2339624-9EFE-3C72-AE89-423E73BCBD92
-  Functions: 2155
-  Symbols:   6782
-  CStrings:  3876
+  UUID: 48C709E7-84C4-3AD2-999B-936983D9E656
+  Functions: 2165
+  Symbols:   6807
+  CStrings:  3889
 
Symbols:
+ +[DSFeatureFlags isWifiSyncRemindersEnabled]
+ +[DSFeatureFlags isWifiSyncRemindersEnabled].cold.1
+ -[DSPasscodePopupViewController makeContextForPasscode:completion:]
+ -[DSPasscodePopupViewController makeContextForPasscode:completion:].cold.1
+ -[DSPasscodePopupViewController makeContextForPasscode:completion:].cold.2
+ -[DSPasscodePopupViewController passcodeContextNew]
+ -[DSPasscodePopupViewController passcodeContextOld]
+ -[DSPasscodePopupViewController setPasscodeContextNew:]
+ -[DSPasscodePopupViewController setPasscodeContextOld:]
+ -[DSPasscodePopupViewController validatePIN:context:]
+ -[DSPrivacyAppDetailController initWithTitle:detailText:symbolName:adoptTableViewScrollView:shouldShowSearchBar:]
+ -[DSPrivacyPermissionDetailController initWithTitle:detailText:symbolName:adoptTableViewScrollView:shouldShowSearchBar:]
+ -[DSTableWelcomeController initWithTitle:detailText:symbolName:adoptTableViewScrollView:shouldShowSearchBar:]
+ _ACMContextCreate
+ _ACMContextDelete
+ _ACMContextGetExternalForm
+ _ACMContextSetData
+ _OBJC_CLASS_$_DSApp
+ _OBJC_CLASS_$_DSSensor
+ _OBJC_CLASS_$_NSData
+ _OBJC_IVAR_$_DSPasscodePopupViewController._passcodeContextNew
+ _OBJC_IVAR_$_DSPasscodePopupViewController._passcodeContextOld
+ _PasscodeAndBiometricsSettingsLibraryCore.frameworkLibrary
+ ___38-[DSTouchIDController beginEnrollment]_block_invoke.346
+ ___43-[DSFaceIDController beginFaceIDEnrollment]_block_invoke.397
+ ___43-[DSFaceIDController beginFaceIDEnrollment]_block_invoke_2.402
+ ___44+[DSFeatureFlags isWifiSyncRemindersEnabled]_block_invoke
+ ___44-[DSEmergencyResetController safetyResetAll]_block_invoke.405
+ ___44-[DSEmergencyResetController safetyResetAll]_block_invoke.409
+ ___46-[DSPrivateRelayController turnOnPrivateRelay]_block_invoke.340
+ ___47-[DSPasscodePopupViewController _applyPasscode]_block_invoke.391
+ ___47-[DSPasscodePopupViewController _applyPasscode]_block_invoke.391.cold.1
+ ___47-[DSPasscodePopupViewController _applyPasscode]_block_invoke.392
+ ___47-[DSPasscodePopupViewController _applyPasscode]_block_invoke.392.cold.1
+ ___47-[DSPasscodePopupViewController _applyPasscode]_block_invoke.393
+ ___49+[DSIconFactory iconWithSize:contact:completion:]_block_invoke
+ ___49+[DSIconFactory iconWithSize:contact:completion:]_block_invoke_2
+ ___51-[DSContinuityController getDevicesWithCompletion:]_block_invoke.368
+ ___51-[DSEmergencySOSController gatherEmergencyContacts]_block_invoke.389
+ ___51-[DSEmergencySOSController gatherEmergencyContacts]_block_invoke.389.cold.1
+ ___51-[DSEmergencySOSController gatherEmergencyContacts]_block_invoke.393
+ ___51-[DSNavigationController authToReturnToSafetyCheck]_block_invoke.490.cold.1
+ ___51-[DSNavigationController authToReturnToSafetyCheck]_block_invoke.491
+ ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.316
+ ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.316.cold.1
+ ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.317
+ ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.317.cold.1
+ ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.318
+ ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.318.cold.1
+ ___54-[DSSafetyCheckWhenBlocking isSharingWith:completion:]_block_invoke.308
+ ___56-[DSPasscodePopupViewController handleNewPasscodeEntry:]_block_invoke
+ ___58-[DSBlockingPermissionsController selectAndStopAllSharing]_block_invoke.348
+ ___58-[DSWifiSyncController returnFromDetailAndRemoveComputer:]_block_invoke.411
+ ___60-[DSPasscodePopupViewController handleCurrentPasscodeEntry:]_block_invoke
+ ___61-[DSAlternateDeviceAccessManager performFetchWithCompletion:]_block_invoke.308
+ ___61-[DSAlternateDeviceAccessManager performFetchWithCompletion:]_block_invoke.308.cold.1
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.352
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.357
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.362
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.373
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.378
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.383
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.388
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.399
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.361
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.366
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.377
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.382
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.384
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.392
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.400
+ ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_3.398
+ ___61-[DSWifiSyncController removeAllPairedDevicesAndPushNextPane]_block_invoke.341
+ ___62-[DSCompletedController fetchAdditionalSharingWithCompletion:]_block_invoke.424
+ ___62-[DSCompletedController fetchAdditionalSharingWithCompletion:]_block_invoke.424.cold.1
+ ___62-[DSCompletedController fetchAdditionalSharingWithCompletion:]_block_invoke.426
+ ___64-[DSBlockingPermissionsDetailController _stopFindMyPushNextPane]_block_invoke.394
+ ___66-[DSEmergencySOSController emergencyContactFlow:didSelectContact:]_block_invoke.424
+ ___66-[DSWifiSyncController removeSelectedPairedDevicesAndPushNextPane]_block_invoke.388
+ ___67-[DSPasscodePopupViewController makeContextForPasscode:completion:]_block_invoke
+ ___70-[DSAlternateDeviceAccessManager resetAllAccessMethodsWithCompletion:]_block_invoke.315
+ ___70-[DSAlternateDeviceAccessManager resetAllAccessMethodsWithCompletion:]_block_invoke.315.cold.1
+ ___70-[DSAlternateDeviceAccessManager resetAllAccessMethodsWithCompletion:]_block_invoke.316
+ ___77-[DSPublicResourceSharingController stopSharingTypes:alertLabel:alertDetail:]_block_invoke.340
+ ___77-[DSPublicResourceSharingController stopSharingTypes:alertLabel:alertDetail:]_block_invoke.340.cold.1
+ ___77-[DSPublicResourceSharingController stopSharingTypes:alertLabel:alertDetail:]_block_invoke.342
+ ___83+[DSSafetyCheck showHSA2UpgradeWithPresentingViewController:safetyCheckController:]_block_invoke.431
+ ___83+[DSSafetyCheck showHSA2UpgradeWithPresentingViewController:safetyCheckController:]_block_invoke_2.434
+ ___86+[DSSafetyCheck authForSafetyCheckWithPresentingViewController:safetyCheckController:]_block_invoke.358
+ ___PasscodeAndBiometricsSettingsLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32bs_e13_v24?0r^v8Q16ls32l8
+ ___block_descriptor_40_e8_32bs_e17_v16?0"UIImage"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e16_v16?0"NSData"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.313
+ ___block_literal_global.329
+ ___block_literal_global.333
+ ___block_literal_global.345
+ ___block_literal_global.349
+ ___block_literal_global.350
+ ___block_literal_global.353
+ ___block_literal_global.360
+ ___block_literal_global.365
+ ___block_literal_global.373
+ ___block_literal_global.389
+ ___block_literal_global.393
+ ___block_literal_global.400
+ ___block_literal_global.410
+ ___block_literal_global.412
+ ___block_literal_global.421
+ ___block_literal_global.426
+ ___block_literal_global.436
+ ___block_literal_global.483
+ ___block_literal_global.493
+ ___getPABSBiometricControllerClass_block_invoke
+ ___getPABSBiometricControllerClass_block_invoke.cold.1
+ ___getPABSBiometricControllerClass_block_invoke.cold.2
+ _audit_stringPasscodeAndBiometricsSettings
+ _getPABSBiometricControllerClass.softClass
+ _get_witness_table qd0__7SwiftUI4ViewHD3_AaBPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAA15ModifiedContentVyAcAE5sheet11isPresented0D7Dismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQOyAcAE18confirmationDialog_AJ15titleVisibility7actions7messageQrqd___AoA0S0Oqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQOyAA01_c9Modifier_I0Vy017DigitalSeparationB0019SafetyCheckBlockingV0VG_SSAA05TupleC0VyAHyAcAE16keyboardShortcutyQrAA16KeyboardShortcutVFQOyAA6ButtonVyAA4TextVG_Qo_AA017_AppearanceActionV0VG_A10_SgtGA9_Qo__AY0yzC0VSgQo_A13_G_SbQo_HO.39
+ _isWifiSyncRemindersEnabled.isEnabled
+ _isWifiSyncRemindersEnabled.onceToken
+ _objc_msgSend$bytes
+ _objc_msgSend$changePasscodeWithOldPasscodeContext:newPasscodeContext:outError:
+ _objc_msgSend$changePasscodeWithOldPasscodeContext:newPasscodeContext:skipRecovery:outError:
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$isWifiSyncRemindersEnabled
+ _objc_msgSend$makeContextForPasscode:completion:
+ _objc_msgSend$nextIdentityNameForIdentityType:
+ _objc_msgSend$passcodeContext:meetsCurrentConstraintsOutError:
+ _objc_msgSend$passcodeContextNew
+ _objc_msgSend$passcodeContextOld
+ _objc_msgSend$setPasscodeContextNew:
+ _objc_msgSend$setPasscodeContextOld:
+ _objc_msgSend$unlockDeviceWithPasscodeContext:outError:
+ _objc_msgSend$validatePIN:context:
+ _symbolic _____y_____GSg 7SwiftUI6ButtonV AA4TextV
+ _symbolic _____y_____y_____G_SS_____y_____y_____y_____y_____G_Qo______G_AHSgtGAGQo_ 7SwiftUI4ViewPAAE18confirmationDialog_11isPresented15titleVisibility7actions7messageQrqd___AA7BindingVySbGAA0I0Oqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AA01_C16Modifier_ContentV 017DigitalSeparationB0019SafetyCheckBlockingM0V AA05TupleC0V AA08ModifiedN0V AcAE16keyboardShortcutyQrAA08KeyboardW0VFQO AA6ButtonV AA4TextV AA017_AppearanceActionM0V
+ _symbolic _____y_____y_____y_____G_Qo______G 7SwiftUI15ModifiedContentV AA4ViewPAAE16keyboardShortcutyQrAA08KeyboardG0VFQO AA6ButtonV AA4TextV AA25_AppearanceActionModifierV
+ _symbolic _____y_____y_____y_____G_Qo______G_ADSgt 7SwiftUI15ModifiedContentV AA4ViewPAAE16keyboardShortcutyQrAA08KeyboardG0VFQO AA6ButtonV AA4TextV AA25_AppearanceActionModifierV
+ _symbolic _____y_____y_____y_____y_____G_Qo______G_AESgtG 7SwiftUI9TupleViewV AA15ModifiedContentV AA0D0PAAE16keyboardShortcutyQrAA08KeyboardH0VFQO AA6ButtonV AA4TextV AA25_AppearanceActionModifierV
+ _symbolic _____y_____y_____y_____y_____G_SS_____yAAy_____y_____y_____G_Qo______G_AHSgtGAGQo_______SgQo_AJG 7SwiftUI15ModifiedContentV AA4ViewPAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaDRd__lFQO AeAE18confirmationDialog_AG15titleVisibility7actions7messageQrqd___AlA0P0Oqd_0_yXEqd_1_yXEtSyRd__AaDRd_0_AaDRd_1_r1_lFQO AA01_e9Modifier_D0V 017DigitalSeparationB0019SafetyCheckBlockingS0V AA05TupleE0V AeAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO AA6ButtonV AA4TextV AA017_AppearanceActionS0V AV0vwE0V
+ _symbolic _____y_____y_____y_____y_____y_____G_SS_____yAAy_____y_____y_____G_Qo______G_AHSgtGAGQo_______SgQo_AJG_SbQo_ 7SwiftUI4ViewPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AA15ModifiedContentV AcAE5sheet11isPresented0D7Dismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQO AcAE18confirmationDialog_AJ15titleVisibility7actions7messageQrqd___AoA0S0Oqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AA01_c9Modifier_I0V 017DigitalSeparationB0019SafetyCheckBlockingV0V AA05TupleC0V AcAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO AA6ButtonV AA4TextV AA017_AppearanceActionV0V AY0yzC0V
- +[DSSafetyCheck startEmergencyResetWithPresentingViewController:showRatchetWarning:]
- +[DSSafetyCheck startManageSharingWithPresentingViewController:showRatchetWarning:]
- -[DSAlternateDeviceAccessManager fetchAccessMethodsWithCompletion:].cold.1
- -[DSAlternateDeviceAccessManager setFetchNeeded:]
- -[DSEmergencyResetWelcomeController ratchetStateDidChange:]
- -[DSEmergencyResetWelcomeController setShouldShowRatchetPlatter:]
- -[DSEmergencyResetWelcomeController setShowRatchetPlatter:]
- -[DSEmergencyResetWelcomeController showRatchetPlatter]
- -[DSNavigationController setShouldShowRatchetPlatter:]
- -[DSNavigationController shouldShowRatchetPlatter]
- -[DSPasscodePopupViewController passcodeOld]
- -[DSPasscodePopupViewController setPasscodeOld:]
- -[DSPasscodePopupViewController validatePIN:]
- -[DSSharingWelcomeController ratchetStateDidChange:]
- -[DSSharingWelcomeController setShouldShowRatchetPlatter:]
- -[DSSharingWelcomeController setShowRatchetPlatter:]
- -[DSSharingWelcomeController showRatchetPlatter]
- _OBJC_IVAR_$_DSEmergencyResetWelcomeController._showRatchetPlatter
- _OBJC_IVAR_$_DSNavigationController._shouldShowRatchetPlatter
- _OBJC_IVAR_$_DSPasscodePopupViewController._passcodeOld
- _OBJC_IVAR_$_DSSharingWelcomeController._showRatchetPlatter
- ___38-[DSTouchIDController beginEnrollment]_block_invoke.340
- ___43-[DSFaceIDController beginFaceIDEnrollment]_block_invoke.391
- ___43-[DSFaceIDController beginFaceIDEnrollment]_block_invoke_2.396
- ___44-[DSEmergencyResetController safetyResetAll]_block_invoke.399
- ___44-[DSEmergencyResetController safetyResetAll]_block_invoke.403
- ___46-[DSPrivateRelayController turnOnPrivateRelay]_block_invoke.334
- ___47-[DSPasscodePopupViewController _applyPasscode]_block_invoke.387
- ___47-[DSPasscodePopupViewController _applyPasscode]_block_invoke.387.cold.1
- ___47-[DSPasscodePopupViewController _applyPasscode]_block_invoke.388
- ___47-[DSPasscodePopupViewController _applyPasscode]_block_invoke.388.cold.1
- ___47-[DSPasscodePopupViewController _applyPasscode]_block_invoke.389
- ___51-[DSContinuityController getDevicesWithCompletion:]_block_invoke.366
- ___51-[DSEmergencySOSController gatherEmergencyContacts]_block_invoke.386
- ___51-[DSEmergencySOSController gatherEmergencyContacts]_block_invoke.386.cold.1
- ___51-[DSEmergencySOSController gatherEmergencyContacts]_block_invoke.390
- ___51-[DSNavigationController authToReturnToSafetyCheck]_block_invoke.489
- ___51-[DSNavigationController authToReturnToSafetyCheck]_block_invoke.489.cold.1
- ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.310
- ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.310.cold.1
- ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.311
- ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.311.cold.1
- ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.312
- ___53-[DSPrivateRelayController shouldShowWithCompletion:]_block_invoke.312.cold.1
- ___54-[DSSafetyCheckWhenBlocking isSharingWith:completion:]_block_invoke.305
- ___58-[DSBlockingPermissionsController selectAndStopAllSharing]_block_invoke.342
- ___58-[DSWifiSyncController returnFromDetailAndRemoveComputer:]_block_invoke.409
- ___61-[DSAlternateDeviceAccessManager performFetchWithCompletion:]_block_invoke.305
- ___61-[DSAlternateDeviceAccessManager performFetchWithCompletion:]_block_invoke.305.cold.1
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.346
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.351
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.356
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.361
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.372
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.377
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.382
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke.387
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.355
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.360
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.365
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.376
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.378
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.386
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_2.388
- ___61-[DSEmergencyResetController initializeEmergencyResetActions]_block_invoke_3.392
- ___61-[DSWifiSyncController removeAllPairedDevicesAndPushNextPane]_block_invoke.335
- ___62-[DSCompletedController fetchAdditionalSharingWithCompletion:]_block_invoke.418
- ___62-[DSCompletedController fetchAdditionalSharingWithCompletion:]_block_invoke.418.cold.1
- ___62-[DSCompletedController fetchAdditionalSharingWithCompletion:]_block_invoke.420
- ___64-[DSBlockingPermissionsDetailController _stopFindMyPushNextPane]_block_invoke.391
- ___66-[DSEmergencySOSController emergencyContactFlow:didSelectContact:]_block_invoke.421
- ___66-[DSWifiSyncController removeSelectedPairedDevicesAndPushNextPane]_block_invoke.386
- ___70-[DSAlternateDeviceAccessManager resetAllAccessMethodsWithCompletion:]_block_invoke.312
- ___70-[DSAlternateDeviceAccessManager resetAllAccessMethodsWithCompletion:]_block_invoke.312.cold.1
- ___70-[DSAlternateDeviceAccessManager resetAllAccessMethodsWithCompletion:]_block_invoke.313
- ___77-[DSPublicResourceSharingController stopSharingTypes:alertLabel:alertDetail:]_block_invoke.334
- ___77-[DSPublicResourceSharingController stopSharingTypes:alertLabel:alertDetail:]_block_invoke.334.cold.1
- ___77-[DSPublicResourceSharingController stopSharingTypes:alertLabel:alertDetail:]_block_invoke.336
- ___83+[DSSafetyCheck showHSA2UpgradeWithPresentingViewController:safetyCheckController:]_block_invoke.428
- ___83+[DSSafetyCheck showHSA2UpgradeWithPresentingViewController:safetyCheckController:]_block_invoke_2.431
- ___86+[DSSafetyCheck authForSafetyCheckWithPresentingViewController:safetyCheckController:]_block_invoke.352
- ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.310
- ___block_literal_global.324
- ___block_literal_global.330
- ___block_literal_global.338
- ___block_literal_global.342
- ___block_literal_global.347
- ___block_literal_global.357
- ___block_literal_global.362
- ___block_literal_global.367
- ___block_literal_global.381
- ___block_literal_global.390
- ___block_literal_global.398
- ___block_literal_global.406
- ___block_literal_global.407
- ___block_literal_global.409
- ___block_literal_global.418
- ___block_literal_global.423
- ___block_literal_global.430
- ___block_literal_global.482
- ___block_literal_global.492
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_DigitalSeparationUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_DigitalSeparationUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_DigitalSeparationUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_DigitalSeparationUI
- _get_witness_table qd0__7SwiftUI4ViewHD3_AaBPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAA15ModifiedContentVyAcAE5sheet11isPresented0D7Dismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQOyAcAE18confirmationDialog_AJ15titleVisibility7actions7messageQrqd___AoA0S0Oqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQOyAA01_c9Modifier_I0Vy017DigitalSeparationB0019SafetyCheckBlockingV0VG_SSAA05TupleC0VyAcAE16keyboardShortcutyQrAA16KeyboardShortcutVFQOyAA6ButtonVyAA4TextVG_Qo__A10_tGA9_Qo__AY0yzC0VSgQo_AA017_AppearanceActionV0VG_SbQo_HO.39
- _objc_msgSend$changePasscodeFrom:to:outError:
- _objc_msgSend$changePasscodeFrom:to:skipRecovery:outError:
- _objc_msgSend$nextIdentityName
- _objc_msgSend$passcode:meetsCurrentConstraintsOutError:
- _objc_msgSend$passcodeOld
- _objc_msgSend$setFetchNeeded:
- _objc_msgSend$setPasscodeOld:
- _objc_msgSend$setShouldShowRatchetPlatter:
- _objc_msgSend$setShowRatchetPlatter:
- _objc_msgSend$shouldShowPlatterForRatchetState:
- _objc_msgSend$shouldShowRatchetPlatter
- _objc_msgSend$showRatchetPlatter
- _objc_msgSend$unlockDeviceWithPasscode:outError:
- _objc_msgSend$validatePIN:
- _symbolic _____y_____y_____G_Qo_ 7SwiftUI4ViewPAAE16keyboardShortcutyQrAA08KeyboardE0VFQO AA6ButtonV AA4TextV
- _symbolic _____y_____y_____G_Qo__ACt 7SwiftUI4ViewPAAE16keyboardShortcutyQrAA08KeyboardE0VFQO AA6ButtonV AA4TextV
- _symbolic _____y_____y_____G_SS_____y_____y_____y_____G_Qo__AGtGAFQo_ 7SwiftUI4ViewPAAE18confirmationDialog_11isPresented15titleVisibility7actions7messageQrqd___AA7BindingVySbGAA0I0Oqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AA01_C16Modifier_ContentV 017DigitalSeparationB0019SafetyCheckBlockingM0V AA05TupleC0V AcAE16keyboardShortcutyQrAA08KeyboardV0VFQO AA6ButtonV AA4TextV
- _symbolic _____y_____y_____y_____G_Qo__ADtG 7SwiftUI9TupleViewV AA0D0PAAE16keyboardShortcutyQrAA08KeyboardF0VFQO AA6ButtonV AA4TextV
- _symbolic _____y_____y_____y_____y_____G_SS_____y_____y_____y_____G_Qo__AHtGAGQo_______SgQo______G 7SwiftUI15ModifiedContentV AA4ViewPAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaDRd__lFQO AeAE18confirmationDialog_AG15titleVisibility7actions7messageQrqd___AlA0P0Oqd_0_yXEqd_1_yXEtSyRd__AaDRd_0_AaDRd_1_r1_lFQO AA01_e9Modifier_D0V 017DigitalSeparationB0019SafetyCheckBlockingS0V AA05TupleE0V AeAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO AA6ButtonV AA4TextV AV0vwE0V AA017_AppearanceActionS0V
- _symbolic _____y_____y_____y_____y_____y_____G_SS_____y_____y_____y_____G_Qo__AHtGAGQo_______SgQo______G_SbQo_ 7SwiftUI4ViewPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AA15ModifiedContentV AcAE5sheet11isPresented0D7Dismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQO AcAE18confirmationDialog_AJ15titleVisibility7actions7messageQrqd___AoA0S0Oqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AA01_c9Modifier_I0V 017DigitalSeparationB0019SafetyCheckBlockingV0V AA05TupleC0V AcAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO AA6ButtonV AA4TextV AY0yzC0V AA017_AppearanceActionV0V
CStrings:
+ "@\"NSData\""
+ "Class getPABSBiometricControllerClass(void)_block_invoke"
+ "Couldn't create auth context: ACM error %d"
+ "Couldn't set secret data for kACMContextDataTypePassphrase in auth context: ACM err %d"
+ "LEARN_MORE_WITH_ICON"
+ "PABSBiometricController"
+ "Presenting DSBlockingConfirmationView confirmation dialog"
+ "SCSharingTypeWiFiSync"
+ "T@\"NSData\",&,N,V_passcodeContextNew"
+ "T@\"NSData\",&,N,V_passcodeContextOld"
+ "[DSBlockingAlertController] creating alert for %@"
+ "[DSBlockingAlertController] presenting safety check"
+ "_passcodeContextNew"
+ "_passcodeContextOld"
+ "bytes"
+ "changePasscodeWithOldPasscodeContext:newPasscodeContext:outError:"
+ "changePasscodeWithOldPasscodeContext:newPasscodeContext:skipRecovery:outError:"
+ "dataUsingEncoding:"
+ "dataWithBytes:length:"
+ "initWithTitle:detailText:symbolName:adoptTableViewScrollView:"
+ "initWithTitle:detailText:symbolName:adoptTableViewScrollView:shouldShowSearchBar:"
+ "isWifiSyncRemindersEnabled"
+ "makeContextForPasscode:completion:"
+ "nextIdentityNameForIdentityType:"
+ "passcodeContext:meetsCurrentConstraintsOutError:"
+ "passcodeContextNew"
+ "passcodeContextOld"
+ "setPasscodeContextNew:"
+ "setPasscodeContextOld:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/PasscodeAndBiometricsSettings.framework/PasscodeAndBiometricsSettings"
+ "unlockDeviceWithPasscodeContext:outError:"
+ "v16@?0@\"NSData\"8"
+ "v24@?0r^v8Q16"
+ "validatePIN:context:"
+ "void *PasscodeAndBiometricsSettingsLibrary(void)"
- "RESTRICTIONS_LEARN_MORE"
- "T@\"NSString\",&,N,V_passcodeOld"
- "TB,N,V_shouldShowRatchetPlatter"
- "TB,N,V_showRatchetPlatter"
- "_passcodeOld"
- "_shouldShowRatchetPlatter"
- "_showRatchetPlatter"
- "changePasscodeFrom:to:outError:"
- "changePasscodeFrom:to:skipRecovery:outError:"
- "nextIdentityName"
- "passcode:meetsCurrentConstraintsOutError:"
- "passcodeOld"
- "setFetchNeeded:"
- "setPasscodeOld:"
- "setShouldShowRatchetPlatter:"
- "setShowRatchetPlatter:"
- "shouldShowRatchetPlatter"
- "showRatchetPlatter"
- "startEmergencyResetWithPresentingViewController:showRatchetWarning:"
- "startManageSharingWithPresentingViewController:showRatchetWarning:"
- "unlockDeviceWithPasscode:outError:"
- "validatePIN:"

```
