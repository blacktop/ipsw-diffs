## LoginUI

> `/System/Library/AccessibilityBundles/LoginUI.axbundle/LoginUI`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x1a90
-  __TEXT.__auth_stubs: 0x210
+3005.16.0.0.0
+  __TEXT.__text: 0x1b8c
+  __TEXT.__auth_stubs: 0x200
   __TEXT.__objc_methlist: 0x454
   __TEXT.__cstring: 0x5dc
   __TEXT.__const: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1c0
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x118
+  __AUTH_CONST.__auth_got: 0x110
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x6e0
   __AUTH_CONST.__objc_const: 0xf30

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 20DC1BD0-5564-32D4-83DB-68B724204109
+  UUID: 6DAAD188-013E-3165-9423-D32B675EE9D4
   Functions: 79
-  Symbols:   410
+  Symbols:   409
   CStrings:  209
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x25
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXLoginUIGlue accessibilityInitializeBundle] : 148 -> 152
~ ___46+[AXLoginUIGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ ___46+[AXLoginUIGlue accessibilityInitializeBundle]_block_invoke_3 : 312 -> 320
~ _accessibilityLocalizedString : 160 -> 168
~ +[LUIClassTableViewControllerAccessibility _accessibilityPerformValidations:] : 140 -> 148
~ -[LUIClassTableViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 508 -> 520
~ +[LUIManagedDevicesNavigationControllerAccessibility _accessibilityPerformValidations:] : 128 -> 136
~ +[LUIManagedDevicesViewControllerAccessibility _accessibilityPerformValidations:] : 180 -> 188
~ -[LUIManagedDevicesViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 356 -> 380
~ -[LUIPaneHeaderViewAccessibility _accessibilityLoadAccessibilityInformation] : 204 -> 212
~ +[LUIPrivacyViewAccessibility _accessibilityPerformValidations:] : 136 -> 144
~ -[LUIPrivacyViewAccessibility _accessibilityMungeMoreButtonLabel] : 112 -> 120
~ -[LUIUserGridViewCellAccessibility accessibilityLabel] : 180 -> 192
~ +[UIApplicationAccessibility__LoginUI__UIKit _accessibilityPerformValidations:] : 180 -> 188
~ -[UIApplicationAccessibility__LoginUI__UIKit _accessibilitySoftwareMimicKeyboard] : 820 -> 892
~ -[UIApplicationAccessibility__LoginUI__UIKit _accessibilityActiveKeyboard] : 296 -> 312
~ -[UITableViewCellAccessibility__LoginUI__UIKit didMoveToWindow] : 120 -> 124
~ -[UITableViewCellAccessibility__LoginUI__UIKit _accessibilityLoadAccessibilityInformation] : 236 -> 256
~ -[UITableViewCellAccessibility__LoginUI__UIKit _accessibilityIgnoreInternalLabels] : 120 -> 124
~ -[LUIAppleIDSignInViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 188 -> 196

```
