## TipsWidgetExtension

> `/System/Library/AccessibilityBundles/TipsWidgetExtension.axbundle/TipsWidgetExtension`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x550
-  __TEXT.__auth_stubs: 0xf0
+3036.2.0.0.0
+  __TEXT.__text: 0x4f4
   __TEXT.__objc_methlist: 0xc4
   __TEXT.__cstring: 0x12e
   __TEXT.__unwind_info: 0x98
-  __TEXT.__objc_classname: 0xc1
-  __TEXT.__objc_methname: 0x286
-  __TEXT.__objc_methtype: 0x52
-  __TEXT.__objc_stubs: 0x1e0
-  __DATA_CONST.__got: 0x20
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x80
+  __DATA_CONST.__got: 0x20
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x1c0
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
-  UUID: 4E99F623-CE20-31F2-87CF-536C908C59BF
+  UUID: 2725ACED-8CE0-361E-94B3-3596FC4C7518
   Functions: 16
-  Symbols:   103
-  CStrings:  64
+  Symbols:   104
+  CStrings:  31
 
Symbols:
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
~ +[AXTipsWidgetExtensionGlue accessibilityInitializeBundle] : 152 -> 148
~ ___58+[AXTipsWidgetExtensionGlue accessibilityInitializeBundle]_block_invoke_2 : 88 -> 84
~ ___58+[AXTipsWidgetExtensionGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 92
~ _accessibilityTipsLocalizedString : 212 -> 196
~ +[TPSWidgetTipViewAccessibility _accessibilityPerformValidations:] : 164 -> 152
~ -[TPSWidgetTipViewAccessibility accessibilityFrame] : 100 -> 96
~ -[TipsWidgetExtensionUIViewAccessibility _accessibilityUseAccessibilityFrameForHittest] : 128 -> 120
~ -[TipsWidgetExtensionUIViewAccessibility _accessibilityOverridesInvalidFrames] : 128 -> 120
~ -[TipsWidgetExtensionUIViewAccessibility accessibilityFrame] : 216 -> 188
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXTipsWidgetExtensionGlue"
- "B16@0:8"
- "SafeCategory"
- "__TPSWidgetTipViewAccessibility_super"
- "__TipsWidgetExtensionUIViewAccessibility_super"
- "_accessibilityOverridesInvalidFrames"
- "_accessibilityPerformValidations:"
- "_accessibilityUseAccessibilityFrameForHittest"
- "accessibilityFrame"
- "accessibilityIdentifier"
- "accessibilityInitializeBundle"
- "bundleWithPath:"
- "init"
- "installSafeCategory:canInteractWithTargetClass:"
- "isEqualToString:"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "stringByAppendingPathComponent:"
- "superview"
- "v16@0:8"
- "v24@0:8@16"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:isKindOfClass:"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"

```
