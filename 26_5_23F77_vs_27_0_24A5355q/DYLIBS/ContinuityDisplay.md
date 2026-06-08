## ContinuityDisplay

> `/System/Library/AccessibilityBundles/ContinuityDisplay.axbundle/ContinuityDisplay`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x2c8
-  __TEXT.__auth_stubs: 0xb0
+3036.2.0.0.0
+  __TEXT.__text: 0x2b0
   __TEXT.__objc_methlist: 0x5c
   __TEXT.__cstring: 0x123
   __TEXT.__unwind_info: 0x78
-  __TEXT.__objc_classname: 0x73
-  __TEXT.__objc_methname: 0x236
-  __TEXT.__objc_methtype: 0x23
-  __TEXT.__objc_stubs: 0x1a0
-  __DATA_CONST.__got: 0x28
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x60
+  __DATA_CONST.__got: 0x28
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x1b0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__common: 0x8
   __DATA.__bss: 0x8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F41D0CC6-8C85-316A-892E-A99BFDF44A2C
+  UUID: 02A0D47E-B945-3782-AA29-7C7DCAA1D628
   Functions: 9
-  Symbols:   74
-  CStrings:  46
+  Symbols:   75
+  CStrings:  20
 
Symbols:
+ ___block_literal_global.351
+ ___block_literal_global.360
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
- ___block_literal_global.330
- ___block_literal_global.339
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ -[DisplayViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 172 -> 164
~ +[AXContinuityDisplayGlue accessibilityInitializeBundle] : 152 -> 148
~ ___56+[AXContinuityDisplayGlue accessibilityInitializeBundle]_block_invoke_2 : 88 -> 84
~ _accessibilityLocalizedString : 184 -> 176
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXContinuityDisplayGlue"
- "SafeCategory"
- "__DisplayViewControllerAccessibility_super"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "accessibilityInitializeBundle"
- "bundleForClass:"
- "init"
- "installSafeCategory:canInteractWithTargetClass:"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeValueForKey:"
- "setAccessibilityLabel:"
- "setAccessibilityTraits:"
- "setIsAccessibilityElement:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "v24@0:8@16"
- "validateClass:hasInstanceMethod:withFullSignature:"

```
