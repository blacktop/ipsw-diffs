## Diagnostics

> `/System/Library/AccessibilityBundles/Diagnostics.axbundle/Diagnostics`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x1288
-  __TEXT.__auth_stubs: 0x1d0
+3036.2.0.0.0
+  __TEXT.__text: 0x11b8
   __TEXT.__objc_methlist: 0x22c
-  __TEXT.__cstring: 0x350
   __TEXT.__const: 0x8
+  __TEXT.__cstring: 0x350
   __TEXT.__unwind_info: 0xe8
-  __TEXT.__objc_classname: 0x193
-  __TEXT.__objc_methname: 0x3d2
-  __TEXT.__objc_methtype: 0x3b
-  __TEXT.__objc_stubs: 0x360
-  __DATA_CONST.__got: 0x58
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x58
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x560
   __AUTH_CONST.__objc_const: 0x750
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x410
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E1CD8A54-3A54-3CD1-B7B3-36AC7B3FB290
+  UUID: 811A28C5-E754-39C8-BD6B-E07EB3BFEB65
   Functions: 39
-  Symbols:   223
-  CStrings:  150
+  Symbols:   224
+  CStrings:  92
 
Symbols:
+ ___block_literal_global.351
+ ___block_literal_global.360
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- ___block_literal_global.330
- ___block_literal_global.339
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[AXDiagnosticsGlue accessibilityInitializeBundle] : 152 -> 148
~ ___50+[AXDiagnosticsGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ ___50+[AXDiagnosticsGlue accessibilityInitializeBundle]_block_invoke_3 : 180 -> 172
~ _accessibilityLocalizedString : 184 -> 176
~ +[DeviceInformationViewAccessibility _accessibilityPerformValidations:] : 352 -> 344
~ -[DeviceInformationViewAccessibility _accessibilityLoadAccessibilityInformation] : 372 -> 348
~ ___80-[DeviceInformationViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 268 -> 248
~ -[DeviceInformationViewAccessibility subviewsForStackViewElement] : 316 -> 288
~ -[DeviceInformationViewAccessibility _axLoadLabelAccessibility] : 352 -> 328
~ -[ImageButtonAccessibility accessibilityLabel] : 92 -> 84
~ +[PromptViewAccessibility _accessibilityPerformValidations:] : 196 -> 184
~ -[PromptViewAccessibility subviewsForStackViewElement] : 364 -> 336
~ -[TestRunnerViewAccessibility subviewsForStackViewElement] : 432 -> 428
~ -[TextButtonAccessibility accessibilityLabel] : 92 -> 84
~ +[CardViewCellAccessibility _accessibilityPerformValidations:] : 156 -> 144
~ -[CardViewCellAccessibility accessibilityElements] : 540 -> 532
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXDiagnosticsGlue"
- "B16@0:8"
- "Q16@0:8"
- "SafeCategory"
- "__CardViewCellAccessibility_super"
- "__DeviceInformationViewAccessibility_super"
- "__ImageButtonAccessibility_super"
- "__PromptViewAccessibility_super"
- "__TestRunnerViewAccessibility_super"
- "__TextButtonAccessibility_super"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_axLoadLabelAccessibility"
- "accessibilityContainerType"
- "accessibilityElements"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityTraits"
- "arrangedSubviews"
- "array"
- "axArrayByIgnoringNilElementsWithCount:"
- "axSafelyAddObject:"
- "axSafelyAddObjectsFromArray:"
- "bundleForClass:"
- "countByEnumeratingWithState:objects:count:"
- "init"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "q16@0:8"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeIntegerForKey:"
- "safeValueForKey:"
- "setAccessibilityHint:"
- "setAccessibilityLabel:"
- "setDebugBuild:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "subviews"
- "subviewsForStackViewElement"
- "text"
- "v16@0:8"
- "v24@0:8@16"
- "validateClass:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"

```
