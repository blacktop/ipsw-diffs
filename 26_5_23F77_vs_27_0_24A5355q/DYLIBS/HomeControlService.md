## HomeControlService

> `/System/Library/AccessibilityBundles/HomeControlService.axbundle/HomeControlService`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x3a0
-  __TEXT.__auth_stubs: 0xf0
+3036.2.0.0.0
+  __TEXT.__text: 0x368
   __TEXT.__objc_methlist: 0x64
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x113
   __TEXT.__unwind_info: 0x80
-  __TEXT.__objc_classname: 0x78
-  __TEXT.__objc_methname: 0x206
-  __TEXT.__objc_methtype: 0x31
-  __TEXT.__objc_stubs: 0x140
-  __DATA_CONST.__got: 0x30
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x80
+  __DATA_CONST.__got: 0x30
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x1b0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E780B2EC-1B51-3A17-A4E8-29F7AFD443EB
-  Functions: 13
-  Symbols:   86
-  CStrings:  48
+  UUID: C495188E-E4C0-396D-A3F4-1F15A310D5D2
+  Functions: 12
+  Symbols:   85
+  CStrings:  23
 
Symbols:
+ ___block_literal_global.352
+ ___block_literal_global.354
+ ___block_literal_global.360
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x21
+ _objc_retain_x1
+ _objc_retain_x2
- +[AXHomeControlServiceGlue accessibilityInitializeBundle].cold.1
- ___block_literal_global.331
- ___block_literal_global.333
- ___block_literal_global.339
- _objc_release_x20
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[HCSRemoteViewControllerAccessibility _accessibilityPerformValidations:] : 188 -> 176
~ -[HCSRemoteViewControllerAccessibility willBeginTransition:forCompactModule:] : 232 -> 228
~ +[AXHomeControlServiceGlue accessibilityInitializeBundle] : 44 -> 40
~ ___57+[AXHomeControlServiceGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___57+[AXHomeControlServiceGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 96
~ _accessibilityLocalizedString : 156 -> 148
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXHomeControlServiceGlue"
- "SafeCategory"
- "__HCSRemoteViewControllerAccessibility_super"
- "_accessibilityPerformValidations:"
- "accessibilityBundles"
- "accessibilityInitializeBundle"
- "bundleForClass:"
- "installSafeCategory:canInteractWithTargetClass:"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeValueForKey:"
- "setDebugBuild:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8B16B20"
- "validateClass:hasInstanceMethod:withFullSignature:"

```
