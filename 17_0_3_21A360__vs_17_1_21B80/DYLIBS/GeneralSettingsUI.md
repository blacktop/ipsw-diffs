## GeneralSettingsUI

> `/System/Library/PrivateFrameworks/Settings/GeneralSettingsUI.framework/GeneralSettingsUI`

```diff

-1153.0.0.0.0
-  __TEXT.__text: 0x30edc
-  __TEXT.__auth_stubs: 0xe90
-  __TEXT.__objc_methlist: 0x20bc
-  __TEXT.__const: 0x168
-  __TEXT.__gcc_except_tab: 0x76c
-  __TEXT.__cstring: 0x3f84
+1156.2.2.0.0
+  __TEXT.__text: 0x31360
+  __TEXT.__auth_stubs: 0xeb0
+  __TEXT.__objc_methlist: 0x2114
+  __TEXT.__const: 0x178
+  __TEXT.__gcc_except_tab: 0x774
+  __TEXT.__cstring: 0x40b5
   __TEXT.__oslogstring: 0x1418
   __TEXT.__dlopen_cstrs: 0x372
-  __TEXT.__unwind_info: 0xaf8
+  __TEXT.__unwind_info: 0xb04
   __TEXT.__objc_classname: 0x6f1
-  __TEXT.__objc_methname: 0x8ce1
-  __TEXT.__objc_methtype: 0x15cc
-  __TEXT.__objc_stubs: 0x7a60
+  __TEXT.__objc_methname: 0x8e93
+  __TEXT.__objc_methtype: 0x15e9
+  __TEXT.__objc_stubs: 0x7be0
   __DATA_CONST.__got: 0x570
   __DATA_CONST.__const: 0xb50
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3f38
-  __DATA_CONST.__objc_selrefs: 0x2518
+  __DATA_CONST.__objc_const: 0x3f58
+  __DATA_CONST.__objc_selrefs: 0x25a0
   __DATA_CONST.__objc_arraydata: 0x1c0
-  __AUTH_CONST.__cfstring: 0x4540
+  __AUTH_CONST.__cfstring: 0x46c0
   __AUTH_CONST.__objc_const: 0x1090
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__auth_got: 0x758
+  __AUTH_CONST.__auth_got: 0x768
   __AUTH.__objc_data: 0xaa0
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x5c0
+  __DATA.__objc_classrefs: 0x5d8
   __DATA.__objc_superrefs: 0x158
   __DATA.__objc_ivar: 0x25c
   __DATA.__data: 0x790

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /System/Library/PrivateFrameworks/IAP.framework/IAP
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
+  - /System/Library/PrivateFrameworks/ManagedConfigurationUI.framework/ManagedConfigurationUI
   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup
   - /System/Library/PrivateFrameworks/NearField.framework/NearField
+  - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/Pegasus.framework/Pegasus
   - /System/Library/PrivateFrameworks/PhoneNumbers.framework/PhoneNumbers
   - /System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtzupdate.dylib
-  Functions: 926
-  Symbols:   4192
-  CStrings:  2624
+  Functions: 933
+  Symbols:   4223
+  CStrings:  2657
 
Symbols:
+ -[PSGAirDropController _presentPrivacyFlow]
+ -[PSGAirDropController isCellularUsageEnabled:]
+ -[PSGAirDropController privacyBundle]
+ -[PSGAirDropController privacyFlow]
+ -[PSGAirDropController setCellularUsageEnabled:specifier:]
+ -[PSGAirDropController setPrivacyBundle:]
+ -[PSGAirDropController setPrivacyFlow:]
+ -[PSGSWVersionDetailCell deviceNameString]
+ _MGGetStringAnswer
+ _NSStringFromSelector
+ _OBJC_CLASS_$_OBBundle
+ _OBJC_CLASS_$_OBPrivacyFlow
+ _OBJC_CLASS_$_OBPrivacyPresenter
+ _OBJC_IVAR_$_PSGAirDropController._privacyBundle
+ _OBJC_IVAR_$_PSGAirDropController._privacyFlow
+ ___block_literal_global.12
+ _objc_msgSend$bundleWithIdentifier:
+ _objc_msgSend$deviceNameString
+ _objc_msgSend$filteredSetUsingPredicate:
+ _objc_msgSend$flowWithBundle:
+ _objc_msgSend$isCellularUsageEnabled
+ _objc_msgSend$localizedButtonTitle
+ _objc_msgSend$predicateWithFormat:
+ _objc_msgSend$present
+ _objc_msgSend$presenterForPrivacySplashWithIdentifier:
+ _objc_msgSend$privacyBundle
+ _objc_msgSend$privacyFlow
+ _objc_msgSend$setCellularUsageEnabled:
+ _objc_msgSend$setPresentingViewController:
- -[PSGAirDropController _refreshFooterForSpecifier:]
- _OBJC_IVAR_$_PSGAirDropController._nearbySharingGroupSpecifier
- _OBJC_IVAR_$_PSGAirDropController._nearbySharingSpecifier
- ___block_literal_global.5
- _objc_msgSend$model
CStrings:
+ "@\"OBBundle\""
+ "@\"OBPrivacyFlow\""
+ "AIRDROP_CELLULAR_USAGE_FOOTER_WIFI"
+ "AIRDROP_CELLULAR_USAGE_GROUP_ID"
+ "AIRDROP_CELLULAR_USAGE_HEADER"
+ "AIRDROP_CELLULAR_USAGE_ID"
+ "AIRDROP_CELLULAR_USAGE_TITLE"
+ "AIRDROP_FOOTER_FORMAT"
+ "AIRDROP_NFC_TITLE"
+ "HasBaseband"
+ "MarketingDeviceFamilyName"
+ "NOT (productName CONTAINS[c] %@)"
+ "T@\"OBBundle\",&,N,V_privacyBundle"
+ "T@\"OBPrivacyFlow\",&,N,V_privacyFlow"
+ "UC Automouse"
+ "_presentPrivacyFlow"
+ "_privacyBundle"
+ "_privacyFlow"
+ "bundleWithIdentifier:"
+ "com.apple.onboarding.airdrop"
+ "deviceNameString"
+ "filteredSetUsingPredicate:"
+ "flowWithBundle:"
+ "isCellularUsageEnabled"
+ "isCellularUsageEnabled:"
+ "localizedButtonTitle"
+ "predicateWithFormat:"
+ "present"
+ "presenterForPrivacySplashWithIdentifier:"
+ "privacyBundle"
+ "privacyFlow"
+ "setCellularUsageEnabled:"
+ "setCellularUsageEnabled:specifier:"
+ "setPresentingViewController:"
+ "setPrivacyBundle:"
+ "setPrivacyFlow:"
- "_nearbySharingGroupSpecifier"
- "_nearbySharingSpecifier"
- "model"

```
