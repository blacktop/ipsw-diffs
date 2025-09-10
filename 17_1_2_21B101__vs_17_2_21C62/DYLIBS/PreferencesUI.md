## PreferencesUI

> `/System/Library/PrivateFrameworks/PreferencesUI.framework/PreferencesUI`

```diff

-1250.2.1.0.0
-  __TEXT.__text: 0x3db78
+1250.3.13.0.0
+  __TEXT.__text: 0x3e1e8
   __TEXT.__auth_stubs: 0xde0
-  __TEXT.__objc_methlist: 0x2714
+  __TEXT.__objc_methlist: 0x276c
   __TEXT.__const: 0xe6
-  __TEXT.__gcc_except_tab: 0x1088
-  __TEXT.__oslogstring: 0x281d
-  __TEXT.__cstring: 0x4022
+  __TEXT.__gcc_except_tab: 0x1084
+  __TEXT.__oslogstring: 0x2a66
+  __TEXT.__cstring: 0x4012
   __TEXT.__dlopen_cstrs: 0x618
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0x28
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xff0
+  __TEXT.__unwind_info: 0x1010
   __TEXT.__objc_classname: 0x762
-  __TEXT.__objc_methname: 0xbf94
-  __TEXT.__objc_methtype: 0x22f8
-  __TEXT.__objc_stubs: 0x9400
+  __TEXT.__objc_methname: 0xc0c4
+  __TEXT.__objc_methtype: 0x2306
+  __TEXT.__objc_stubs: 0x9500
   __DATA_CONST.__got: 0x4d8
   __DATA_CONST.__const: 0x1240
   __DATA_CONST.__objc_classlist: 0xe8

   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4650
-  __DATA_CONST.__objc_selrefs: 0x2ca8
+  __DATA_CONST.__objc_selrefs: 0x2cf0
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__objc_const: 0xbb0
   __AUTH_CONST.__const: 0x5b0
-  __AUTH_CONST.__cfstring: 0x3f80
+  __AUTH_CONST.__cfstring: 0x3f60
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28

   - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/ClassroomKit.framework/ClassroomKit
   - /System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP
+  - /System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI
   - /System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred
   - /System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI
   - /System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider

   - /System/Library/PrivateFrameworks/FTServices.framework/FTServices
   - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
   - /System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI
+  - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice
   - /System/Library/PrivateFrameworks/HeadphoneSettings.framework/HeadphoneSettings
   - /System/Library/PrivateFrameworks/Home.framework/Home
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6C73E321-2F3D-35DA-B01F-6D2F81DFE79D
-  Functions: 1275
-  Symbols:   5131
-  CStrings:  3605
+  UUID: 465109CA-B57F-35FE-B35F-376C1E539DE9
+  Functions: 1283
+  Symbols:   5155
+  CStrings:  3624
 
Symbols:
+ -[PSUIFingerprintController proceedWithDeleteFingerprintFor:]
+ -[PSUIPasscodeLockController proceedToTurnOffPasscode:]
+ -[PSUIPearlPasscodeController proceedToEnrollGlassesForExistingAppearance:]
+ -[PSUIPearlPasscodeController proceedToEnrollPeriocularForExistingAppearance:]
+ -[PSUIPearlPasscodeController proceedToEnrollWithSpecifier:]
+ -[PSUIPearlPasscodeController proceedWithChecksToDeleteFaceIDWithSpecifier:]
+ -[PSUIPearlPasscodeController toggleToState:forIdentifier:]
+ -[PSUITouchIDPasscodeController proceedToAddEnrollment:]
+ GCC_except_table116
+ GCC_except_table14
+ GCC_except_table22
+ GCC_except_table53
+ GCC_except_table55
+ GCC_except_table63
+ GCC_except_table75
+ GCC_except_table90
+ GCC_except_table94
+ ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke.256
+ ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke.258
+ ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke_2.259
+ ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke_2.259.cold.1
+ ___55-[PSUIPasscodeLockController proceedToTurnOffPasscode:]_block_invoke
+ ___56-[PSUITouchIDPasscodeController proceedToAddEnrollment:]_block_invoke
+ ___56-[PSUITouchIDPasscodeController proceedToAddEnrollment:]_block_invoke_2
+ ___58-[PSUIPrefsListController vpnSpecifierGeneratorDidUpdate:]_block_invoke.1165
+ ___60-[PSUIPearlPasscodeController proceedToEnrollWithSpecifier:]_block_invoke
+ ___60-[PSUIPearlPasscodeController proceedToEnrollWithSpecifier:]_block_invoke_2
+ ___61-[PSUIFingerprintController proceedWithDeleteFingerprintFor:]_block_invoke
+ ___61-[PSUIPrefsListController familySpecifierGeneratorDidUpdate:]_block_invoke.1162
+ ___76-[PSUIPearlPasscodeController proceedWithChecksToDeleteFaceIDWithSpecifier:]_block_invoke
+ ___82-[PSUIFingerprintController presentAlertSheetForFingerprintBindingToGovernmentID:]_block_invoke.241
+ ___86-[PSUIPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.487
+ ___86-[PSUIPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.491
+ ___86-[PSUIPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.498
+ ___88-[PSUIPasscodeLockController showAlertForPhoneAutoUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.483
+ ___block_literal_global.261
+ ___block_literal_global.263
+ ___block_literal_global.493
+ __unnamed_array_storage.1195
+ __unnamed_array_storage.1196
+ _objc_msgSend$proceedToAddEnrollment:
+ _objc_msgSend$proceedToEnrollGlassesForExistingAppearance:
+ _objc_msgSend$proceedToEnrollPeriocularForExistingAppearance:
+ _objc_msgSend$proceedToEnrollWithSpecifier:
+ _objc_msgSend$proceedToTurnOffPasscode:
+ _objc_msgSend$proceedWithChecksToDeleteFaceIDWithSpecifier:
+ _objc_msgSend$proceedWithDeleteFingerprintFor:
+ _objc_msgSend$searchQueryTextChanged
- GCC_except_table115
- GCC_except_table21
- GCC_except_table37
- GCC_except_table43
- GCC_except_table52
- GCC_except_table70
- GCC_except_table89
- GCC_except_table93
- ___38-[PSUIPearlPasscodeController enroll:]_block_invoke
- ___38-[PSUIPearlPasscodeController enroll:]_block_invoke_2
- ___45-[PSUIPasscodeLockController togglePasscode:]_block_invoke
- ___47-[PSUIFingerprintController deleteFingerprint:]_block_invoke
- ___47-[PSUITouchIDPasscodeController addEnrollment:]_block_invoke
- ___47-[PSUITouchIDPasscodeController addEnrollment:]_block_invoke_2
- ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke.255
- ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke.257
- ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke_2.258
- ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke_2.258.cold.1
- ___58-[PSUIPrefsListController vpnSpecifierGeneratorDidUpdate:]_block_invoke.1163
- ___61-[PSUIPrefsListController familySpecifierGeneratorDidUpdate:]_block_invoke.1160
- ___72-[PSUIPearlPasscodeController deleteFaceIDIdentitiesCheckWithSpecifier:]_block_invoke
- ___82-[PSUIFingerprintController presentAlertSheetForFingerprintBindingToGovernmentID:]_block_invoke.240
- ___86-[PSUIPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.490
- ___86-[PSUIPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.494
- ___86-[PSUIPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.501
- ___88-[PSUIPasscodeLockController showAlertForPhoneAutoUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.486
- ___block_literal_global.260
- ___block_literal_global.262
- ___block_literal_global.496
- __unnamed_array_storage.1193
- __unnamed_array_storage.1194
CStrings:
+ "%@: Auto toggling to state [%@]"
+ "Face ID: Not enrolling as we have a faceIDEnrollmentCoordinator"
+ "Face ID: Not enrolling periocular for existing appearance as we have a faceIDEnrollmentCoordinator"
+ "Face ID: Not enrolling with Add Glasses as we have a faceIDEnrollmentCoordinator"
+ "Face ID: User pressed Add Glasses"
+ "Face ID: User pressed Reset"
+ "Face ID: User pressed Set Up an Alternate Appearance"
+ "Face ID: User pressed Set up Face ID/an Alternate Appearance"
+ "Face ID: User toggled to ON - Face ID with a Mask"
+ "Touch ID: User pressed Add a Fingerprint"
+ "Touch ID: User pressed Delete Fingerprint"
+ "proceedToAddEnrollment:"
+ "proceedToEnrollGlassesForExistingAppearance:"
+ "proceedToEnrollPeriocularForExistingAppearance:"
+ "proceedToEnrollWithSpecifier:"
+ "proceedToTurnOffPasscode:"
+ "proceedWithChecksToDeleteFaceIDWithSpecifier:"
+ "proceedWithDeleteFingerprintFor:"
+ "searchQueryTextChanged"
+ "toggleToState:forIdentifier:"
+ "v28@0:8B16@20"
- "CHANGE_PASSCODE"

```
