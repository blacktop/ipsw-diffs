## HomeUIService

> `/System/Library/AccessibilityBundles/HomeUIService.axbundle/HomeUIService`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0xd84
-  __TEXT.__auth_stubs: 0x140
+3036.2.0.0.0
+  __TEXT.__text: 0xf1c
   __TEXT.__objc_methlist: 0x1a8
   __TEXT.__cstring: 0x301
-  __TEXT.__unwind_info: 0xb8
-  __TEXT.__objc_classname: 0x181
-  __TEXT.__objc_methname: 0x437
-  __TEXT.__objc_methtype: 0x4c
-  __TEXT.__objc_stubs: 0x380
-  __DATA_CONST.__got: 0x90
+  __TEXT.__unwind_info: 0xc0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xa8
+  __DATA_CONST.__got: 0x90
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x420
   __AUTH_CONST.__objc_const: 0x510
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x2d0
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D05B4ED1-C89C-3989-9612-EFC137845590
-  Functions: 34
-  Symbols:   194
-  CStrings:  133
+  UUID: AA34358C-64A3-3ADA-BC46-DE04BBD54998
+  Functions: 33
+  Symbols:   203
+  CStrings:  73
 
Symbols:
+ ___block_literal_global.352
+ ___block_literal_global.354
+ ___block_literal_global.360
+ ___block_literal_global.57
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x25
- +[AXHomeUIServiceGlue accessibilityInitializeBundle].cold.1
- ___block_literal_global.331
- ___block_literal_global.333
- ___block_literal_global.339
- _objc_retain_x19
Functions:
~ -[HSPCDetectedViewControllerAccessibility viewWillAppear:] : 176 -> 252
~ +[AXHomeUIServiceGlue accessibilityInitializeBundle] : 44 -> 40
~ ___52+[AXHomeUIServiceGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___52+[AXHomeUIServiceGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 96
~ ___52+[AXHomeUIServiceGlue accessibilityInitializeBundle]_block_invoke_4 : 140 -> 132
~ _accessibilityLocalizedString : 156 -> 148
~ +[HSPCCameraScanViewControllerAccessibility _accessibilityPerformValidations:] : 276 -> 268
~ -[HSPCCameraScanViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 296 -> 440
~ -[HSPCCameraScanViewControllerAccessibility _handleSetupCode:] : 180 -> 256
~ +[HSPCPasscodeEntryViewAccessibility _accessibilityPerformValidations:] : 236 -> 228
~ -[HSPCPasscodeEntryViewAccessibility accessibilityLabel] : 12 -> 152
~ -[HSPCPasscodeEntryViewAccessibility accessibilityTraits] : 192 -> 188
~ -[HSPCPasscodeEntryViewAccessibility accessibilityValue] : 248 -> 240
~ -[HSPCPasscodeEntryViewAccessibility insertText:] : 352 -> 340
~ ___49-[HSPCPasscodeEntryViewAccessibility insertText:]_block_invoke : 104 -> 184
~ -[HSPCPasscodeEntryViewAccessibility deleteBackward] : 196 -> 188
~ +[HSSetupTroubleshootingTipCellAccessibility _accessibilityPerformValidations:] : 152 -> 144
~ -[HSSetupTroubleshootingTipCellAccessibility _accessibilityLoadAccessibilityInformation] : 108 -> 104
CStrings:
- "#16@0:8"
- "@16@0:8"
- "@32@0:8q16@24"
- "AXHomeUIServiceGlue"
- "B16@0:8"
- "Q16@0:8"
- "SafeCategory"
- "__HSPCCameraScanViewControllerAccessibility_super"
- "__HSPCDetectedViewControllerAccessibility_super"
- "__HSPCPasscodeEntryViewAccessibility_super"
- "__HSSetupTroubleshootingTipCellAccessibility_super"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_accessibilitySetTextViewShouldBreakUpParagraphs:"
- "_axText"
- "accessibilityBundles"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityTraits"
- "accessibilityValue"
- "bundleForClass:"
- "dictionaryWithObjects:forKeys:count:"
- "initWithString:"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "isFirstResponder"
- "length"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeIntegerForKey:"
- "safeStringForKey:"
- "safeValueForKey:"
- "setAccessibilityHint:"
- "setAccessibilityTraits:"
- "setAttribute:forKey:"
- "setAttributes:"
- "setDebugBuild:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "stringWithFormat:"
- "stringWithString:"
- "substringWithRange:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:isKindOfClass:"

```
