## PasscodeAndBiometricsSettings

> `/System/Library/PrivateFrameworks/PasscodeAndBiometricsSettings.framework/PasscodeAndBiometricsSettings`

```diff

-15.0.0.0.0
-  __TEXT.__text: 0x3081c
-  __TEXT.__auth_stubs: 0xc40
+17.0.0.0.0
+  __TEXT.__text: 0x30bd4
+  __TEXT.__auth_stubs: 0xc30
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x1ff4
+  __TEXT.__objc_methlist: 0x205c
   __TEXT.__const: 0x4d4
-  __TEXT.__gcc_except_tab: 0xad8
-  __TEXT.__cstring: 0x319f
-  __TEXT.__oslogstring: 0x46d8
+  __TEXT.__gcc_except_tab: 0xb00
+  __TEXT.__cstring: 0x317f
+  __TEXT.__oslogstring: 0x4732
   __TEXT.__dlopen_cstrs: 0x443
   __TEXT.__ustring: 0x4e
   __TEXT.__constg_swiftt: 0xe0

   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x30
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0xc40
+  __TEXT.__unwind_info: 0xc58
   __TEXT.__objc_classname: 0x415
-  __TEXT.__objc_methname: 0x6ff6
-  __TEXT.__objc_methtype: 0xd62
-  __TEXT.__objc_stubs: 0x5f80
-  __DATA_CONST.__got: 0x5d8
+  __TEXT.__objc_methname: 0x709c
+  __TEXT.__objc_methtype: 0xd73
+  __TEXT.__objc_stubs: 0x6020
+  __DATA_CONST.__got: 0x5f0
   __DATA_CONST.__const: 0x10a8
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d98
+  __DATA_CONST.__objc_selrefs: 0x1dc0
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x638
+  __AUTH_CONST.__auth_got: 0x630
   __AUTH_CONST.__const: 0x428
-  __AUTH_CONST.__cfstring: 0x2ba0
+  __AUTH_CONST.__cfstring: 0x2c40
   __AUTH_CONST.__objc_const: 0x1fa8
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 00A25E3A-8DB4-3D15-A8D8-86FA5B7C7DA5
-  Functions: 1043
-  Symbols:   3710
-  CStrings:  2390
+  UUID: 8CC3160F-5031-3A77-8724-ADA4797D934C
+  Functions: 1054
+  Symbols:   3738
+  CStrings:  2403
 
Symbols:
+ -[PABSBiometricController localizedPlacardSubtitle]
+ -[PABSBiometricController localizedPlacardTitle]
+ -[PABSBiometricController placardGraphicIconTypeIdentifier]
+ -[PABSBiometricController placardSpecifiersWithTitle:subtitle:icon:]
+ -[PABSPearlPasscodeController localizedPlacardSubtitle]
+ -[PABSPearlPasscodeController localizedPlacardTitle]
+ -[PABSPearlPasscodeController placardGraphicIconTypeIdentifier]
+ -[PABSTouchIDPasscodeController localizedPlacardSubtitle]
+ -[PABSTouchIDPasscodeController localizedPlacardTitle]
+ -[PABSTouchIDPasscodeController placardGraphicIconTypeIdentifier]
+ GCC_except_table70
+ GCC_except_table72
+ GCC_except_table78
+ GCC_except_table90
+ GCC_except_table97
+ _OBJC_CLASS_$_PESettingsFeatureDescriptionCell
+ _PSIconUTTypeIdentifierKey
+ ___47-[PABSFingerprintController deleteFingerprint:]_block_invoke.314
+ ___47-[PABSFingerprintController deleteFingerprint:]_block_invoke.314.cold.1
+ ___47-[PABSTouchIDPasscodeController addEnrollment:]_block_invoke.113
+ ___47-[PABSTouchIDPasscodeController addEnrollment:]_block_invoke.113.cold.1
+ ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke.309
+ ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke.311
+ ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke_2.312
+ ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke_2.312.cold.1
+ ___52-[PABSBiometricController useBiometricForSpecifiers]_block_invoke.174
+ ___62-[PABSBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke.201
+ ___62-[PABSBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke.202
+ ___62-[PABSBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke_2.203
+ ___72-[PABSPearlPasscodeController deleteFaceIDIdentitiesCheckWithSpecifier:]_block_invoke.279
+ ___72-[PABSPearlPasscodeController deleteFaceIDIdentitiesCheckWithSpecifier:]_block_invoke.279.cold.1
+ ___82-[PABSFingerprintController presentAlertSheetForFingerprintBindingToGovernmentID:]_block_invoke.291
+ ___block_literal_global.316
+ ___block_literal_global.318
+ _objc_msgSend$localizedPlacardSubtitle
+ _objc_msgSend$localizedPlacardTitle
+ _objc_msgSend$pe_isSettingsFeatureDescriptionCellSupported
+ _objc_msgSend$placardGraphicIconTypeIdentifier
+ _objc_msgSend$placardSpecifiersWithTitle:subtitle:icon:
+ _objc_msgSend$traitCollection
- -[PABSBiometricController placardSpecifier]
- GCC_except_table34
- GCC_except_table67
- GCC_except_table69
- GCC_except_table75
- GCC_except_table81
- GCC_except_table94
- _NSClassFromString
- ___47-[PABSFingerprintController deleteFingerprint:]_block_invoke.305
- ___47-[PABSFingerprintController deleteFingerprint:]_block_invoke.305.cold.1
- ___47-[PABSTouchIDPasscodeController addEnrollment:]_block_invoke.107
- ___47-[PABSTouchIDPasscodeController addEnrollment:]_block_invoke.107.cold.1
- ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke.300
- ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke.302
- ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke_2.303
- ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke_2.303.cold.1
- ___52-[PABSBiometricController useBiometricForSpecifiers]_block_invoke.164
- ___62-[PABSBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke.191
- ___62-[PABSBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke.192
- ___62-[PABSBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke_2.193
- ___72-[PABSPearlPasscodeController deleteFaceIDIdentitiesCheckWithSpecifier:]_block_invoke.273
- ___72-[PABSPearlPasscodeController deleteFaceIDIdentitiesCheckWithSpecifier:]_block_invoke.273.cold.1
- ___82-[PABSFingerprintController presentAlertSheetForFingerprintBindingToGovernmentID:]_block_invoke.282
- ___block_literal_global.301
- ___block_literal_global.303
- _objc_msgSend$placardSpecifier
CStrings:
+ "@40@0:8@16@24@32"
+ "PLACARD_GROUP_ID"
+ "PLACARD_ID"
+ "Unlock using Vision: %@ %@"
+ "Unlock using Vision: supportsVisionUnlock [%@]"
+ "Unlock using Watch: %@ %@"
+ "Unlock using Watch: hasPairedWatch [%@]"
+ "com.apple.PasscodeAndBiometricsSettings"
+ "localizedPlacardSubtitle"
+ "localizedPlacardTitle"
+ "pe_isSettingsFeatureDescriptionCellSupported"
+ "placardGraphicIconTypeIdentifier"
+ "placardSpecifiersWithTitle:subtitle:icon:"
+ "traitCollection"
- "PASSCODE_PLACARD"
- "PasscodeAndBiometricsSettings"
- "PasscodeAndBiometricsSettings.PasscodePlacardCell"
- "Unlock using Vision: %@"
- "Unlock using watch: %@ %@"
- "placardSpecifier"

```
