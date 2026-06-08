## AirDrop

> `/System/Library/AccessibilityBundles/AirDrop.axbundle/AirDrop`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x57c
-  __TEXT.__auth_stubs: 0x150
+3036.2.0.0.0
+  __TEXT.__text: 0x550
   __TEXT.__objc_methlist: 0xc8
-  __TEXT.__cstring: 0x173
   __TEXT.__const: 0x8
   __TEXT.__gcc_except_tab: 0x14
+  __TEXT.__cstring: 0x173
   __TEXT.__unwind_info: 0xa8
-  __TEXT.__objc_classname: 0xc3
-  __TEXT.__objc_methname: 0x2ce
-  __TEXT.__objc_methtype: 0x3c
-  __TEXT.__objc_stubs: 0x1e0
-  __DATA_CONST.__got: 0x38
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xb8
+  __DATA_CONST.__got: 0x38
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x180
   __AUTH_CONST.__objc_const: 0x2d0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9B2E0092-9512-3FCA-B881-F3CB5F80F1D5
+  UUID: 6DA69B35-057E-38DC-AD03-01A5DB17053F
   Functions: 18
-  Symbols:   120
-  CStrings:  64
+  Symbols:   121
+  CStrings:  29
 
Symbols:
+ GCC_except_table8
+ ___block_literal_global.3
+ ___block_literal_global.351
+ ___block_literal_global.357
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- GCC_except_table3
- ___block_literal_global.330
- ___block_literal_global.336
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[AXAirDropGlue accessibilityInitializeBundle] : 148 -> 144
~ ___46+[AXAirDropGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ ___46+[AXAirDropGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 92
~ _accessibilityLocalizedString : 168 -> 160
~ +[AirDropBrowserViewControllerAccessibility _accessibilityPerformValidations:] : 200 -> 192
~ -[AirDropBrowserViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 248 -> 244
~ ___87-[AirDropBrowserViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 116 -> 108
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXAirDropGlue"
- "B16@0:8"
- "SafeCategory"
- "__AirDropBrowserViewControllerAccessibility_super"
- "__AirDropNoContentViewAccessibility_super"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityOverridesInvalidFrames"
- "_accessibilityPerformValidations:"
- "_setIsAccessibilityElementBlock:"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "bundleForClass:"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "length"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeValueForKeyPath:"
- "setDebugBuild:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "v24@0:8@16"
- "v40@0:8@16@24@32"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:isKindOfClass:"
- "viewDidLoad"

```
