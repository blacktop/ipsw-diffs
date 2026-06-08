## CoreDynamicUIPlugin

> `/System/Library/AccessibilityBundles/CoreDynamicUIPlugin.axbundle/CoreDynamicUIPlugin`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x33c
-  __TEXT.__auth_stubs: 0xd0
+3036.2.0.0.0
+  __TEXT.__text: 0x31c
   __TEXT.__objc_methlist: 0xb8
   __TEXT.__cstring: 0x126
   __TEXT.__unwind_info: 0x80
-  __TEXT.__objc_classname: 0xa7
-  __TEXT.__objc_methname: 0x20b
-  __TEXT.__objc_methtype: 0x33
-  __TEXT.__objc_stubs: 0x160
-  __DATA_CONST.__got: 0x28
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x70
+  __DATA_CONST.__got: 0x28
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0x2d0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 75A9E6DC-6C11-315B-BFDC-4C2E294A063E
+  UUID: 8C4C6249-BC9D-3BB1-AE02-8A569762E543
   Functions: 15
   Symbols:   96
-  CStrings:  52
+  CStrings:  22
 
Symbols:
+ ___block_literal_global.351
+ ___block_literal_global.360
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
- ___block_literal_global.330
- ___block_literal_global.339
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ -[TextComponentAccessibility accessibilityLabel] : 112 -> 104
~ +[AXCoreDynamicUIPluginGlue accessibilityInitializeBundle] : 152 -> 148
~ ___58+[AXCoreDynamicUIPluginGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ ___58+[AXCoreDynamicUIPluginGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 92
~ _accessibilityLocalizedString : 184 -> 176
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXCoreDynamicUIPluginGlue"
- "B16@0:8"
- "Q16@0:8"
- "SafeCategory"
- "__ButtonComponentAccessibility_super"
- "__TextComponentAccessibility_super"
- "_accessibilityPerformValidations:"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityTraits"
- "bundleForClass:"
- "init"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeSwiftValueForKey:"
- "setDebugBuild:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "v24@0:8@16"
- "validateClass:hasSwiftField:withSwiftType:"

```
