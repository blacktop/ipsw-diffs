## BatteryWidget

> `/System/Library/AccessibilityBundles/BatteryWidget.axbundle/BatteryWidget`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x698
-  __TEXT.__auth_stubs: 0x140
+3036.2.0.0.0
+  __TEXT.__text: 0x648
   __TEXT.__objc_methlist: 0xc4
   __TEXT.__cstring: 0x229
   __TEXT.__unwind_info: 0x98
-  __TEXT.__objc_classname: 0xcf
-  __TEXT.__objc_methname: 0x2bd
-  __TEXT.__objc_methtype: 0x3c
-  __TEXT.__objc_stubs: 0x220
-  __DATA_CONST.__got: 0x30
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xa8
+  __DATA_CONST.__got: 0x30
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x280
   __AUTH_CONST.__objc_const: 0x2d0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ACADAF88-9DE0-3921-846E-D46304E41C24
+  UUID: 5684865D-5641-3EB2-B796-592C457202E8
   Functions: 16
-  Symbols:   111
-  CStrings:  82
+  Symbols:   112
+  CStrings:  45
 
Symbols:
+ ___block_literal_global.351
+ ___block_literal_global.357
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- ___block_literal_global.330
- ___block_literal_global.336
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[AXBatteryWidgetGlue accessibilityInitializeBundle] : 152 -> 148
~ ___52+[AXBatteryWidgetGlue accessibilityInitializeBundle]_block_invoke_2 : 88 -> 84
~ ___52+[AXBatteryWidgetGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 92
~ _accessibilityLocalizedString : 168 -> 160
~ +[BCBatteryWidgetViewControllerAccessibility _accessibilityPerformValidations:] : 156 -> 148
~ -[BCBatteryWidgetViewControllerAccessibility _updateRowView:withDevice:animated:] : 356 -> 348
~ +[BCBatteryWidgetRowViewAccessibility _accessibilityPerformValidations:] : 196 -> 184
~ -[BCBatteryWidgetRowViewAccessibility accessibilityLabel] : 180 -> 164
~ -[BCBatteryWidgetRowViewAccessibility accessibilityValue] : 220 -> 208
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXBatteryWidgetGlue"
- "B16@0:8"
- "SafeCategory"
- "__BCBatteryWidgetRowViewAccessibility_super"
- "__BCBatteryWidgetViewControllerAccessibility_super"
- "_accessibilityPerformValidations:"
- "accessibilityBundles"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityValue"
- "bundleForClass:"
- "init"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "localizedStringForKey:value:table:"
- "parts"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeBoolForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeUnsignedIntegerForKey:"
- "safeValueForKey:"
- "setAccessibilityLabel:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "stringWithFormat:"
- "v16@0:8"
- "v24@0:8@16"
- "v36@0:8@16@24B32"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"

```
