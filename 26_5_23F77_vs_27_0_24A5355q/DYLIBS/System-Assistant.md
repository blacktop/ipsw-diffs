## System-Assistant

> `/System/Library/AccessibilityBundles/System-Assistant.axbundle/System-Assistant`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x2e8
-  __TEXT.__auth_stubs: 0xb0
+3036.2.0.0.0
+  __TEXT.__text: 0x2b0
   __TEXT.__objc_methlist: 0x58
   __TEXT.__cstring: 0x105
   __TEXT.__unwind_info: 0x78
-  __TEXT.__objc_classname: 0x8c
-  __TEXT.__objc_methname: 0x1d6
-  __TEXT.__objc_methtype: 0x20
-  __TEXT.__objc_stubs: 0x180
-  __DATA_CONST.__got: 0x28
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x60
+  __DATA_CONST.__got: 0x28
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x100
   __AUTH_CONST.__objc_const: 0x1b0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B6CDE0DD-D9AB-3E1D-808E-8E8BE0DDB740
-  Functions: 11
-  Symbols:   79
-  CStrings:  43
+  UUID: 542CAB5A-2469-3550-8D88-FFF1BF0CA9FD
+  Functions: 10
+  Symbols:   78
+  CStrings:  19
 
Symbols:
+ ___block_literal_global.352
+ ___block_literal_global.361
+ ___block_literal_global.370
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
- +[SiriSystemGlue accessibilityInitializeBundle].cold.1
- ___block_literal_global.331
- ___block_literal_global.340
- ___block_literal_global.349
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[SiriSystemGlue accessibilityInitializeBundle] : 44 -> 40
~ ___47+[SiriSystemGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___47+[SiriSystemGlue accessibilityInitializeBundle]_block_invoke_3 : 88 -> 84
~ _accessibilityLocalizedString : 184 -> 176
~ -[ACAssistantAlternateProviderResultViewAccessibility accessibilityLabel] : 196 -> 180
CStrings:
- "#16@0:8"
- "@16@0:8"
- "B16@0:8"
- "SafeCategory"
- "SiriSystemGlue"
- "__ACAssistantAlternateProviderResultViewAccessibility_super"
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
- "safeValueForKey:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "stringWithFormat:"
- "v16@0:8"
- "validateClass:hasInstanceVariable:withType:"

```
