## TipsNotificationExtension

> `/System/Library/AccessibilityBundles/TipsNotificationExtension.axbundle/TipsNotificationExtension`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x89c
-  __TEXT.__auth_stubs: 0x160
+3036.2.0.0.0
+  __TEXT.__text: 0x814
   __TEXT.__objc_methlist: 0xb4
   __TEXT.__cstring: 0x1da
   __TEXT.__unwind_info: 0x98
-  __TEXT.__objc_classname: 0xdb
-  __TEXT.__objc_methname: 0x3bc
-  __TEXT.__objc_methtype: 0x52
-  __TEXT.__objc_stubs: 0x3a0
-  __DATA_CONST.__got: 0x48
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x120
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xb8
+  __DATA_CONST.__got: 0x48
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x2c0
   __AUTH_CONST.__objc_const: 0x2d0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__data: 0x8
   __DATA.__common: 0x8

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
-  - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 54E640FF-EB9F-332E-A010-09634F1A3573
+  UUID: 5407AE45-32A3-32F2-B477-D5F1039AA27D
   Functions: 16
-  Symbols:   131
-  CStrings:  96
+  Symbols:   132
+  CStrings:  48
 
Symbols:
+ ___block_literal_global.17
+ ___block_literal_global.396
+ ___block_literal_global.405
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- ___block_literal_global.333
- ___block_literal_global.342
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[AXTipsNotificationExtensionGlue accessibilityInitializeBundle] : 152 -> 148
~ ___64+[AXTipsNotificationExtensionGlue accessibilityInitializeBundle]_block_invoke_2 : 88 -> 84
~ ___64+[AXTipsNotificationExtensionGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 92
~ _accessibilityTipsLocalizedString : 212 -> 196
~ -[TipsWidgetExtensionUIViewAccessibility _accessibilityUseAccessibilityFrameForHittest] : 128 -> 120
~ -[TipsWidgetExtensionUIViewAccessibility _accessibilityOverridesInvalidFrames] : 128 -> 120
~ -[TipsWidgetExtensionUIViewAccessibility accessibilityFrame] : 216 -> 188
~ +[TPSSingleTipViewControllerAccessibility _accessibilityPerformValidations:] : 308 -> 300
~ -[TPSSingleTipViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 648 -> 596
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXTipsNotificationExtensionGlue"
- "B16@0:8"
- "SafeCategory"
- "__TPSSingleTipViewControllerAccessibility_super"
- "__TipsWidgetExtensionUIViewAccessibility_super"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityOverridesInvalidFrames"
- "_accessibilityPerformValidations:"
- "_accessibilityUseAccessibilityFrameForHittest"
- "accessibilityFrame"
- "accessibilityIdentifier"
- "accessibilityInitializeBundle"
- "bundleWithPath:"
- "indexOfObjectPassingTest:"
- "init"
- "installSafeCategory:canInteractWithTargetClass:"
- "isEqualToString:"
- "isHidden"
- "layer"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeStringForKey:"
- "safeValueForKey:"
- "setAccessibilityHint:"
- "setAccessibilityIdentifier:"
- "setAccessibilityLabel:"
- "setAccessibilityTraits:"
- "setIsAccessibilityElement:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "stringByAppendingPathComponent:"
- "sublayers"
- "superview"
- "v16@0:8"
- "v24@0:8@16"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:isKindOfClass:"
- "view"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"

```
