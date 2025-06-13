## AccountsUI

> `/System/Library/PrivateFrameworks/AccountsUI.framework/AccountsUI`

```diff

-331.0.0.0.0
-  __TEXT.__text: 0x3ada8
+331.1.0.0.0
+  __TEXT.__text: 0x3b918
   __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_methlist: 0x146c
-  __TEXT.__cstring: 0x278c
+  __TEXT.__objc_methlist: 0x148c
+  __TEXT.__cstring: 0x2929
   __TEXT.__gcc_except_tab: 0x55c
   __TEXT.__const: 0x38
   __TEXT.__dlopen_cstrs: 0x18b
-  __TEXT.__oslogstring: 0x14a0
+  __TEXT.__oslogstring: 0x14cc
   __TEXT.__ustring: 0x10
   __TEXT.__objc_const_ax: 0x180
-  __TEXT.__unwind_info: 0x4f8
+  __TEXT.__unwind_info: 0x50c
   __TEXT.__objc_classname: 0x475
-  __TEXT.__objc_methname: 0x6058
+  __TEXT.__objc_methname: 0x625e
   __TEXT.__objc_methtype: 0x1043
-  __TEXT.__objc_stubs: 0x5360
-  __DATA_CONST.__got: 0x448
-  __DATA_CONST.__const: 0x9d8
+  __TEXT.__objc_stubs: 0x5600
+  __DATA_CONST.__got: 0x450
+  __DATA_CONST.__const: 0x9f8
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x3890
-  __DATA_CONST.__objc_selrefs: 0x1860
+  __DATA_CONST.__objc_selrefs: 0x1910
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__cfstring: 0x1fa0
+  __AUTH_CONST.__cfstring: 0x2080
   __AUTH_CONST.__objc_const: 0xa58
   __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH_CONST.__const: 0x220
+  __AUTH_CONST.__const: 0x260
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x308
   __AUTH.__objc_data: 0x780
   __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x2b8
+  __DATA.__objc_classrefs: 0x2e0
   __DATA.__objc_superrefs: 0x98
   __DATA.__objc_ivar: 0x1b8
   __DATA.__objc_const_ax: 0x0

   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 99B4EEEC-4062-38D0-A707-8AB57B12DD37
-  Functions: 586
-  Symbols:   2738
-  CStrings:  1845
+  UUID: 70D930A8-3A2B-350A-BDB9-0F8BAE60A46A
+  Functions: 591
+  Symbols:   2778
+  CStrings:  1885
 
Symbols:
+ +[ACUIViewController guestUserModeContentUnavailableConfiguration:]
+ -[ACUIAddAccountViewController isStolenDeviceProtectionFeatureAvailableAndEnabled]
+ _NSDirectionalEdgeInsetsMake
+ _OBJC_CLASS_$_LARatchetManager
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_UIContentUnavailableConfiguration
+ _OBJC_CLASS_$_UIFontMetrics
+ _OBJC_CLASS_$_UIImageSymbolConfiguration
+ _UIFontWeightBold
+ ___62-[ACUIAddAccountViewController _addAccountSpecifierWasTapped:]_block_invoke.116
+ ___62-[ACUIAddAccountViewController _addAccountSpecifierWasTapped:]_block_invoke_2
+ ___69-[ACUIAddAccountViewController _createCustomControlledAccountTapped:]_block_invoke.160
+ ___69-[ACUIAddAccountViewController _createCustomControlledAccountTapped:]_block_invoke.161
+ ___block_descriptor_32_e23_v16?0"UIAlertAction"8l
+ ___block_literal_global.105
+ ___block_literal_global.112
+ ___block_literal_global.319
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$configurationWithPointSize:
+ _objc_msgSend$defaultMetrics
+ _objc_msgSend$directionalLayoutMargins
+ _objc_msgSend$emptyConfiguration
+ _objc_msgSend$imageProperties
+ _objc_msgSend$isFeatureAvailable
+ _objc_msgSend$isFeatureEnabled
+ _objc_msgSend$isFeatureSupported
+ _objc_msgSend$isStolenDeviceProtectionFeatureAvailableAndEnabled
+ _objc_msgSend$openURL:withCompletionHandler:
+ _objc_msgSend$safeAreaInsets
+ _objc_msgSend$scaledValueForValue:
+ _objc_msgSend$setColor:
+ _objc_msgSend$setDirectionalLayoutMargins:
+ _objc_msgSend$setImageToTextPadding:
+ _objc_msgSend$setPreferredSymbolConfiguration:
+ _objc_msgSend$setSecondaryText:
+ _objc_msgSend$systemFontOfSize:weight:
+ _objc_msgSend$systemImageNamed:
+ _objc_msgSend$textProperties
- GCC_except_table25
- GCC_except_table43
- ___69-[ACUIAddAccountViewController _createCustomControlledAccountTapped:]_block_invoke.136
- ___69-[ACUIAddAccountViewController _createCustomControlledAccountTapped:]_block_invoke.137
- ___block_literal_global.296
CStrings:
+ "%s (%d) \"DTO: Failed to open support link.\""
+ "-[ACUIAddAccountViewController _addAccountSpecifierWasTapped:]_block_invoke_2"
+ "CONTENT_UNAVAILABLE_SHARING_MODE_SECONDARY_TEXT"
+ "CONTENT_UNAVAILABLE_SHARING_MODE_TEXT"
+ "DTO_ENABLED_ADD_EXCHANGE_ACCOUNT_ALERT_LEARN_MORE_ACTION_TITLE"
+ "DTO_ENABLED_ADD_EXCHANGE_ACCOUNT_ALERT_MESSAGE"
+ "DTO_ENABLED_ADD_EXCHANGE_ACCOUNT_ALERT_TITLE"
+ "DimpleKey"
+ "LocalAuthentication"
+ "URLWithString:"
+ "configurationWithPointSize:"
+ "defaultMetrics"
+ "directionalLayoutMargins"
+ "emptyConfiguration"
+ "guestUserModeContentUnavailableConfiguration:"
+ "https://support.apple.com/kb/HT212510"
+ "imageProperties"
+ "isFeatureAvailable"
+ "isFeatureEnabled"
+ "isFeatureSupported"
+ "isStolenDeviceProtectionFeatureAvailableAndEnabled"
+ "openURL:withCompletionHandler:"
+ "person.crop.circle.dashed"
+ "safeAreaInsets"
+ "scaledValueForValue:"
+ "setColor:"
+ "setDirectionalLayoutMargins:"
+ "setImageToTextPadding:"
+ "setPreferredSymbolConfiguration:"
+ "setSecondaryText:"
+ "systemFontOfSize:weight:"
+ "systemImageNamed:"
+ "textProperties"

```
