## DisembarkUI

> `/System/Library/PrivateFrameworks/DisembarkUI.framework/DisembarkUI`

```diff

-285.0.0.0.0
-  __TEXT.__text: 0x1fdc0
-  __TEXT.__objc_methlist: 0x2a38
-  __TEXT.__const: 0x194
-  __TEXT.__cstring: 0x1ea4
-  __TEXT.__gcc_except_tab: 0x2a4
-  __TEXT.__oslogstring: 0x1101
+285.1.3.0.0
+  __TEXT.__text: 0x21b60
+  __TEXT.__objc_methlist: 0x2bd0
+  __TEXT.__const: 0x1b4
+  __TEXT.__cstring: 0x2088
+  __TEXT.__gcc_except_tab: 0x2b8
+  __TEXT.__oslogstring: 0x11cf
   __TEXT.__dlopen_cstrs: 0xc6
-  __TEXT.__swift5_typeref: 0x1c0
-  __TEXT.__swift5_capture: 0xf0
+  __TEXT.__swift5_typeref: 0x202
+  __TEXT.__swift5_capture: 0x12c
   __TEXT.__constg_swiftt: 0xb8
   __TEXT.__swift5_reflstr: 0xf
   __TEXT.__swift5_fieldmd: 0x2c

   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x10
-  __TEXT.__unwind_info: 0xaf0
-  __TEXT.__eh_frame: 0x180
+  __TEXT.__unwind_info: 0xbb0
+  __TEXT.__eh_frame: 0x188
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1070
-  __DATA_CONST.__objc_classlist: 0x180
+  __DATA_CONST.__const: 0x10d0
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xf0
+  __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b20
+  __DATA_CONST.__objc_selrefs: 0x1c50
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xc0
-  __DATA_CONST.__got: 0x4c8
-  __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x16c0
-  __AUTH_CONST.__objc_const: 0x50a8
+  __DATA_CONST.__objc_superrefs: 0xc8
+  __DATA_CONST.__got: 0x508
+  __AUTH_CONST.__const: 0x4d0
+  __AUTH_CONST.__cfstring: 0x17e0
+  __AUTH_CONST.__objc_const: 0x5408
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x5d8
-  __AUTH.__objc_data: 0xf98
-  __AUTH.__data: 0x140
-  __DATA.__objc_ivar: 0x2d4
-  __DATA.__data: 0xaf0
+  __AUTH_CONST.__auth_got: 0x5f0
+  __AUTH.__objc_data: 0x10c8
+  __AUTH.__data: 0x190
+  __DATA.__objc_ivar: 0x2f8
+  __DATA.__data: 0xb80
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppManagedFeatures.framework/AppManagedFeatures
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/PassKit.framework/PassKit
+  - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AppManagedFeaturesUI.framework/AppManagedFeaturesUI
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup
   - /System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach
+  - /System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
   - /System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 988
-  Symbols:   2634
-  CStrings:  384
+  Functions: 1055
+  Symbols:   2742
+  CStrings:  403
 
Symbols:
+ -[DKAnalyticsHandler pendingSanitizeStorageEligible]
+ -[DKAnalyticsHandler pendingSanitizeStorageSelected]
+ -[DKAnalyticsHandler setPendingSanitizeStorageEligible:]
+ -[DKAnalyticsHandler setPendingSanitizeStorageSelected:]
+ -[DKEraseFlow _allowAppSwitching]
+ -[DKEraseFlow _disallowAppSwitching]
+ -[DKEraseFlow _isAppSwitchingAllowedForState:]
+ -[DKEraseFlow captureButtonSuppressionAssertion]
+ -[DKEraseFlow sanitizeStorage]
+ -[DKEraseFlow setCaptureButtonSuppressionAssertion:]
+ -[DKEraseFlow setSanitizeStorage:]
+ -[DKIntroViewController _createSanitizeStorageLearnMoreController]
+ -[DKIntroViewController _createSanitizeStorageRowView]
+ -[DKIntroViewController _presentSanitizeStorageConfirmation:]
+ -[DKIntroViewController sanitizeStorageLearnMoreController]
+ -[DKIntroViewController sanitizeStorageRowView]
+ -[DKIntroViewController setSanitizeStorageLearnMoreController:]
+ -[DKIntroViewController setSanitizeStorageRowView:]
+ -[DKNotableUserData isEligibleForStorageSanitize]
+ -[DKNotableUserData partnerFinancingInformation]
+ -[DKNotableUserData setIsEligibleForStorageSanitize:]
+ -[DKNotableUserData setPartnerFinancingInformation:]
+ -[DKNotableUserDataProvider sanitizeStorageProvider]
+ -[DKNotableUserDataProvider setSanitizeStorageProvider:]
+ -[DKPartnerFinancingConfirmationController initWithPartnerFinancingInformation:canMakePhoneCalls:continueBlock:notNowBlock:]
+ -[DKPartnerFinancingConfirmationController partnerFinancingInformation]
+ -[DKPartnerFinancingConfirmationController setPartnerFinancingInformation:]
+ -[DKSanitizeStorageManager _determineSanitizeStorageEligibility]
+ -[DKSanitizeStorageManager initWithEligibility:]
+ -[DKSanitizeStorageManager init]
+ -[DKSanitizeStorageManager isEligible]
+ -[DKSanitizeStorageManager sanitizeStorageEligible]
+ -[DKSanitizeStorageManager setSanitizeStorageEligible:]
+ _OBJC_CLASS_$_DKPartnerFinancingInformation
+ _OBJC_CLASS_$_DKSanitizeStorageManager
+ _OBJC_CLASS_$_DKSanitizeStorageRowView
+ _OBJC_CLASS_$_OBPrivacyLinkController
+ _OBJC_CLASS_$_OSEligibilityQuery
+ _OBJC_CLASS_$_UISwitch
+ _OBJC_IVAR_$_DKAnalyticsHandler._pendingSanitizeStorageEligible
+ _OBJC_IVAR_$_DKAnalyticsHandler._pendingSanitizeStorageSelected
+ _OBJC_IVAR_$_DKEraseFlow._captureButtonSuppressionAssertion
+ _OBJC_IVAR_$_DKEraseFlow._sanitizeStorage
+ _OBJC_IVAR_$_DKIntroViewController._sanitizeStorageLearnMoreController
+ _OBJC_IVAR_$_DKIntroViewController._sanitizeStorageRowView
+ _OBJC_IVAR_$_DKNotableUserData._isEligibleForStorageSanitize
+ _OBJC_IVAR_$_DKNotableUserData._partnerFinancingInformation
+ _OBJC_IVAR_$_DKNotableUserDataProvider._sanitizeStorageProvider
+ _OBJC_IVAR_$_DKPartnerFinancingConfirmationController._partnerFinancingInformation
+ _OBJC_IVAR_$_DKSanitizeStorageManager._sanitizeStorageEligible
+ _OBJC_METACLASS_$_DKPartnerFinancingInformation
+ _OBJC_METACLASS_$_DKSanitizeStorageManager
+ _OBJC_METACLASS_$_DKSanitizeStorageRowView
+ __DATA_DKPartnerFinancingInformation
+ __DATA_DKSanitizeStorageRowView
+ __INSTANCE_METHODS_DKPartnerFinancingInformation
+ __INSTANCE_METHODS_DKSanitizeStorageRowView
+ __IVARS_DKPartnerFinancingInformation
+ __IVARS_DKSanitizeStorageRowView
+ __METACLASS_DATA_DKPartnerFinancingInformation
+ __METACLASS_DATA_DKSanitizeStorageRowView
+ __OBJC_$_INSTANCE_METHODS_DKSanitizeStorageManager
+ __OBJC_$_INSTANCE_VARIABLES_DKSanitizeStorageManager
+ __OBJC_$_PROP_LIST_DKSanitizeStorageManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DKSanitizeStorageProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DKSanitizeStorageProvider
+ __OBJC_$_PROTOCOL_REFS_DKSanitizeStorageProvider
+ __OBJC_CLASS_PROTOCOLS_$_DKSanitizeStorageManager
+ __OBJC_CLASS_RO_$_DKSanitizeStorageManager
+ __OBJC_LABEL_PROTOCOL_$_DKSanitizeStorageProvider
+ __OBJC_METACLASS_RO_$_DKSanitizeStorageManager
+ __OBJC_PROTOCOL_$_DKSanitizeStorageProvider
+ __PROPERTIES_DKPartnerFinancingInformation
+ __PROPERTIES_DKSanitizeStorageRowView
+ ___54-[DKIntroViewController _createSanitizeStorageRowView]_block_invoke
+ ___54-[DKIntroViewController _createSanitizeStorageRowView]_block_invoke_2
+ ___61-[DKIntroViewController _presentSanitizeStorageConfirmation:]_block_invoke
+ ___61-[DKIntroViewController _presentSanitizeStorageConfirmation:]_block_invoke_2
+ ___block_descriptor_32_e11_v16?0B8B12l
+ ___block_descriptor_40_e8_32s_e11_v16?0B8B12ls32l8
+ ___block_descriptor_48_e8_32s40bs_e39_v16?0"DKPartnerFinancingInformation"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e27_v16?0"DKNotableUserData"8ls32l8s40l8s48l8
+ _kCACornerCurveContinuous
+ _keypath_get_selector_switchToggled
+ _objc_msgSend$_allowAppSwitching
+ _objc_msgSend$_createSanitizeStorageLearnMoreController
+ _objc_msgSend$_createSanitizeStorageRowView
+ _objc_msgSend$_determineSanitizeStorageEligibility
+ _objc_msgSend$_disallowAppSwitching
+ _objc_msgSend$_isAppSwitchingAllowedForState:
+ _objc_msgSend$_presentSanitizeStorageConfirmation:
+ _objc_msgSend$acquireCaptureButtonSuppressionAssertionWithOptions:reason:
+ _objc_msgSend$answer
+ _objc_msgSend$captureButtonSuppressionAssertion
+ _objc_msgSend$initWithArrangedSubviews:
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$initWithCompany:phoneNumber:appName:logo:
+ _objc_msgSend$initWithDomain:error:
+ _objc_msgSend$initWithEligibility:
+ _objc_msgSend$initWithPartnerFinancingInformation:canMakePhoneCalls:continueBlock:notNowBlock:
+ _objc_msgSend$initWithTitle:
+ _objc_msgSend$isEligible
+ _objc_msgSend$isEligibleForStorageSanitize
+ _objc_msgSend$isOn
+ _objc_msgSend$layer
+ _objc_msgSend$linkWithBundleAtPath:
+ _objc_msgSend$partnerFinancingInformation
+ _objc_msgSend$pathForResource:ofType:
+ _objc_msgSend$pendingSanitizeStorageEligible
+ _objc_msgSend$pendingSanitizeStorageSelected
+ _objc_msgSend$sanitizeStorage
+ _objc_msgSend$sanitizeStorageEligible
+ _objc_msgSend$sanitizeStorageProvider
+ _objc_msgSend$sanitizeStorageRowView
+ _objc_msgSend$setAccessibilityLabel:
+ _objc_msgSend$setAlignment:
+ _objc_msgSend$setCaptureButtonSuppressionAssertion:
+ _objc_msgSend$setCornerCurve:
+ _objc_msgSend$setCornerRadius:
+ _objc_msgSend$setIsEligibleForStorageSanitize:
+ _objc_msgSend$setOn:animated:
+ _objc_msgSend$setPartnerFinancingInformation:
+ _objc_msgSend$setPendingSanitizeStorageEligible:
+ _objc_msgSend$setPendingSanitizeStorageSelected:
+ _objc_msgSend$setSanitizeStorage:
+ _objc_msgSend$setSanitizeStorageEligible:
+ _objc_msgSend$setSanitizeStorageLearnMoreController:
+ _objc_msgSend$setSanitizeStorageRowView:
+ _objc_msgSend$setSwitchToggled:
+ _objc_msgSend$switchControl
+ _objc_msgSend$switchToggled
+ _swift_getWitnessTable
+ _swift_retain
+ _swift_retain_x1
+ _symbolic SbytIegnr_
+ _symbolic So29DKPartnerFinancingInformationCSgIegg_
+ _symbolic So29DKPartnerFinancingInformationCSgIeyBy_
- -[DKEraseFlow _allowHomeButton]
- -[DKEraseFlow _disallowHomeButton]
- -[DKEraseFlow _isHomeButtonAllowedForState:]
- -[DKNotableUserData isPartnerFinancingEnabled]
- -[DKNotableUserData setIsPartnerFinancingEnabled:]
- -[DKPartnerFinancingConfirmationController initWithPartnerFinancingProvider:canMakePhoneCalls:continueBlock:notNowBlock:]
- -[DKPartnerFinancingConfirmationController partnerFinancingProvider]
- -[DKPartnerFinancingConfirmationController setPartnerFinancingProvider:]
- _OBJC_IVAR_$_DKNotableUserData._isPartnerFinancingEnabled
- _OBJC_IVAR_$_DKPartnerFinancingConfirmationController._partnerFinancingProvider
- __IVARS_DKPartnerFinancingManager
- __OBJC_$_PROP_LIST_DKPartnerFinancingProvider
- __PROPERTIES_DKPartnerFinancingManager
- ___block_descriptor_32_e8_v12?0B8l
- ___block_descriptor_49_e8_32s40bs_e27_v16?0"DKNotableUserData"8ls32l8s40l8
- _objc_msgSend$_allowHomeButton
- _objc_msgSend$_disallowHomeButton
- _objc_msgSend$_isHomeButtonAllowedForState:
- _objc_msgSend$appName
- _objc_msgSend$company
- _objc_msgSend$initWithPartnerFinancingProvider:canMakePhoneCalls:continueBlock:notNowBlock:
- _objc_msgSend$isPartnerFinancingEnabled
- _objc_msgSend$logo
- _objc_msgSend$setAppName:
- _objc_msgSend$setCompany:
- _objc_msgSend$setIsPartnerFinancingEnabled:
- _objc_msgSend$setLogo:
- _objc_msgSend$setPhoneNumber:
- _symbolic So25DKPartnerFinancingManagerC
CStrings:
+ "&"
+ "Allowing capture button use..."
+ "Device eligibility for sanitization: %lu"
+ "Disallowing capture button use..."
+ "DisembarkUI"
+ "DisembarkUI/DKSanitizeStorageRowView.swift"
+ "DisembarkUIModule.DKSanitizeStorageRowView"
+ "DisembarkUI_Private.DKPartnerFinancingInformation"
+ "Failed to determine Sanitize Storage eligibility: %@"
+ "No logo found for: "
+ "OverwriteStorageLearnMore"
+ "SANITIZE_STORAGE"
+ "SANITIZE_STORAGE_CONFIRMATION_ALERT_BUTTON"
+ "SANITIZE_STORAGE_CONFIRMATION_ALERT_MESSAGE"
+ "SANITIZE_STORAGE_CONFIRMATION_ALERT_TITLE"
+ "Somehow attempting to show the partner financing controller with no partner financing information loaded."
+ "Successfully prepared partner financing information"
+ "bundle"
+ "init()"
+ "init(frame:)"
+ "sanitizeStorageEligible"
+ "sanitizeStorageSelected"
+ "self.sanitizeStorageProvider"
+ "v16@?0@\"DKPartnerFinancingInformation\"8"
- "\t"
- " and phone number: "
- "%"
- "Got an app managed features configuration with company: "
- "Missing company name or phone number for partner financing"
```
