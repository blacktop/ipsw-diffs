## ARTraceModule

> `/System/Library/AccessibilityBundles/ARTraceModule.axbundle/ARTraceModule`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x26c
-  __TEXT.__auth_stubs: 0x90
+3036.2.0.0.0
+  __TEXT.__text: 0x240
   __TEXT.__objc_methlist: 0x70
   __TEXT.__cstring: 0xca
   __TEXT.__unwind_info: 0x78
-  __TEXT.__objc_classname: 0x67
-  __TEXT.__objc_methname: 0x231
-  __TEXT.__objc_methtype: 0x23
-  __TEXT.__objc_stubs: 0x140
-  __DATA_CONST.__got: 0x28
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x50
+  __DATA_CONST.__got: 0x28
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x100
   __AUTH_CONST.__objc_const: 0x1b0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 67DF9AD7-3E78-3ECD-858F-6E6600BCC24A
-  Functions: 13
-  Symbols:   78
-  CStrings:  43
+  UUID: 9B359EBB-537D-3B3D-8830-61EA51B1BD99
+  Functions: 12
+  Symbols:   77
+  CStrings:  18
 
Symbols:
+ ___block_literal_global.352
+ ___block_literal_global.354
+ ___block_literal_global.360
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
- +[AXARTraceModuleGlue accessibilityInitializeBundle].cold.1
- ___block_literal_global.331
- ___block_literal_global.333
- ___block_literal_global.339
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[AXARTraceModuleGlue accessibilityInitializeBundle] : 44 -> 40
~ ___52+[AXARTraceModuleGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___52+[AXARTraceModuleGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 96
~ ___52+[AXARTraceModuleGlue accessibilityInitializeBundle]_block_invoke_4 : 96 -> 92
~ _accessibilityLocalizedString : 168 -> 160
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXARTraceModuleGlue"
- "SafeCategory"
- "__CCUIARTraceModuleAccessibility_super"
- "_accessibilityControlCenterButtonIdentifier"
- "_accessibilityControlCenterButtonLabel"
- "_accessibilityPerformValidations:"
- "accessibilityBundles"
- "accessibilityInitializeBundle"
- "bundleForClass:"
- "installSafeCategory:canInteractWithTargetClass:"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "setDebugBuild:"
- "setNeedsLoadAccessibilityInformation"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "v24@0:8@16"
- "validateClass:isKindOfClass:"

```
