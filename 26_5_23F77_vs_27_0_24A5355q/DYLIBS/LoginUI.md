## LoginUI

> `/System/Library/AccessibilityBundles/LoginUI.axbundle/LoginUI`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x1b8c
-  __TEXT.__auth_stubs: 0x200
+3036.2.0.0.0
+  __TEXT.__text: 0x1aa4
   __TEXT.__objc_methlist: 0x454
-  __TEXT.__cstring: 0x5dc
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x30
+  __TEXT.__cstring: 0x5dc
   __TEXT.__unwind_info: 0x138
-  __TEXT.__objc_classname: 0x475
-  __TEXT.__objc_methname: 0x555
-  __TEXT.__objc_methtype: 0x33
-  __TEXT.__objc_stubs: 0x540
-  __DATA_CONST.__got: 0x88
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1c0
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x110
+  __DATA_CONST.__got: 0x88
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x6e0
   __AUTH_CONST.__objc_const: 0xf30
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x870
   __DATA.__common: 0x8
   __DATA.__bss: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2826CB1D-5BA6-3946-A70A-32772A1475F2
-  Functions: 79
-  Symbols:   409
-  CStrings:  209
+  UUID: 5036CD60-F9B0-3F1D-9C9C-C51799998755
+  Functions: 78
+  Symbols:   410
+  CStrings:  119
 
Symbols:
+ GCC_except_table11
+ GCC_except_table18
+ GCC_except_table46
+ ___block_literal_global.250
+ ___block_literal_global.351
+ ___block_literal_global.357
+ ___block_literal_global.383
+ ___block_literal_global.387
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x27
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x26
- -[UIApplicationAccessibility__LoginUI__UIKit _accessibilitySoftwareMimicKeyboard].cold.1
- GCC_except_table3
- GCC_except_table5
- ___block_literal_global.330
- ___block_literal_global.336
- ___block_literal_global.362
- ___block_literal_global.366
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
Functions:
~ +[AXLoginUIGlue accessibilityInitializeBundle] : 152 -> 148
~ ___46+[AXLoginUIGlue accessibilityInitializeBundle]_block_invoke_2 : 88 -> 84
~ ___46+[AXLoginUIGlue accessibilityInitializeBundle]_block_invoke_3 : 320 -> 312
~ _accessibilityLocalizedString : 168 -> 160
~ +[LUIClassTableViewControllerAccessibility _accessibilityPerformValidations:] : 148 -> 140
~ +[LUIManagedDevicesNavigationControllerAccessibility _accessibilityPerformValidations:] : 136 -> 128
~ +[LUIManagedDevicesViewControllerAccessibility _accessibilityPerformValidations:] : 188 -> 180
~ -[LUIManagedDevicesViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 380 -> 356
~ -[LUIPaneHeaderViewAccessibility _accessibilityLoadAccessibilityInformation] : 212 -> 204
~ +[LUIPrivacyViewAccessibility _accessibilityPerformValidations:] : 144 -> 136
~ -[LUIPrivacyViewAccessibility _accessibilityMungeMoreButtonLabel] : 120 -> 112
~ -[LUIUserGridViewCellAccessibility accessibilityLabel] : 192 -> 180
~ +[UIApplicationAccessibility__LoginUI__UIKit _accessibilityPerformValidations:] : 188 -> 180
~ -[UIApplicationAccessibility__LoginUI__UIKit _accessibilitySoftwareMimicKeyboard] : 892 -> 844
~ -[UIApplicationAccessibility__LoginUI__UIKit _accessibilityActiveKeyboard] : 312 -> 300
~ -[UITableViewCellAccessibility__LoginUI__UIKit didMoveToWindow] : 124 -> 120
~ -[UITableViewCellAccessibility__LoginUI__UIKit _accessibilityLoadAccessibilityInformation] : 256 -> 236
~ -[UITableViewCellAccessibility__LoginUI__UIKit _accessibilityIgnoreInternalLabels] : 124 -> 120
~ -[LUIAppleIDSignInViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 196 -> 188
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXLoginUIGlue"
- "B16@0:8"
- "Q16@0:8"
- "SafeCategory"
- "__LUIAppleIDSignInViewControllerAccessibility_super"
- "__LUIClassTableViewCellAccessibility_super"
- "__LUIClassTableViewControllerAccessibility_super"
- "__LUIManagedDevicesNavigationControllerAccessibility_super"
- "__LUIManagedDevicesViewControllerAccessibility_super"
- "__LUIPaneHeaderViewAccessibility_super"
- "__LUIPrivacyViewAccessibility_super"
- "__LUIUserGridViewCellAccessibility_super"
- "__LUIUserGridViewControllerAccessibility_super"
- "__LUIUserTableViewCellAccessibility_super"
- "__LUI_UIGlintyStringViewAccessibility_super"
- "__UIApplicationAccessibility__LoginUI__UIKit_super"
- "__UITableViewCellAccessibility__LoginUI__UIKit_super"
- "_accessibilityActiveKeyboard"
- "_accessibilityIgnoreInternalLabels"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityMainWindow"
- "_accessibilityMungeMoreButtonLabel"
- "_accessibilityPerformValidations:"
- "_accessibilitySoftwareMimicKeyboard"
- "_accessibilityViewIsVisible"
- "accessibilityBundles"
- "accessibilityHint"
- "accessibilityIdentification"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityPerformEscape"
- "accessibilitySetIdentification:"
- "accessibilityTraits"
- "activeKeyboard"
- "array"
- "axSafelyAddObject:"
- "bundleForClass:"
- "childViewControllers"
- "countByEnumeratingWithState:objects:count:"
- "didMoveToWindow"
- "editableTextField"
- "indexOfObjectPassingTest:"
- "init"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "isEqualToString:"
- "localizedStringForKey:value:table:"
- "objectAtIndex:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "rootViewController"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeValueForKey:"
- "setAccessibilityElements:"
- "setAccessibilityLabel:"
- "setAccessibilityTraits:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "subviews"
- "superview"
- "text"
- "textLabel"
- "v16@0:8"
- "v24@0:8@16"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:isKindOfClass:"
- "window"

```
