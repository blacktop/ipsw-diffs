## PreviewUI

> `/System/Library/AccessibilityBundles/PreviewUI.axbundle/PreviewUI`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x5a4
-  __TEXT.__auth_stubs: 0x100
+3036.2.0.0.0
+  __TEXT.__text: 0x56c
   __TEXT.__objc_methlist: 0x8c
   __TEXT.__cstring: 0x151
   __TEXT.__unwind_info: 0x78
-  __TEXT.__objc_classname: 0x75
-  __TEXT.__objc_methname: 0x32c
-  __TEXT.__objc_methtype: 0x4b
-  __TEXT.__objc_stubs: 0x280
-  __DATA_CONST.__got: 0x28
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x88
+  __DATA_CONST.__got: 0x28
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x1c0
   __AUTH_CONST.__objc_const: 0x1b0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F8FEAD52-D34C-3487-A5C8-94FFE204C85D
+  UUID: D72EC424-B62F-3604-8B39-889EAF915332
   Functions: 14
-  Symbols:   98
-  CStrings:  72
+  Symbols:   99
+  CStrings:  34
 
Symbols:
+ ___block_literal_global.3
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
~ +[AXPreviewUIGlue accessibilityInitializeBundle] : 152 -> 148
~ ___48+[AXPreviewUIGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ _accessibilityLocalizedString : 184 -> 176
~ +[QLMarkupItemViewControllerAccessibility _accessibilityPerformValidations:] : 288 -> 280
~ -[QLMarkupItemViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 220 -> 204
~ -[QLMarkupItemViewControllerAccessibility viewDidLoad] : 108 -> 104
~ -[QLMarkupItemViewControllerAccessibility _axPhotoDescriptionFromContext:] : 112 -> 100
CStrings:
- "#16@0:8"
- "@16@0:8"
- "@24@0:8@16"
- "AXPreviewUIGlue"
- "SafeCategory"
- "__QLMarkupItemViewControllerAccessibility_super"
- "_accessibilityFindSubviewDescendant:"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_axPhotoDescriptionFromContext:"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "bundleForClass:"
- "init"
- "installSafeCategory:canInteractWithTargetClass:"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeUIViewForKey:"
- "safeValueForKey:"
- "setAccessibilityLabel:"
- "setAccessibilityViewIsModal:"
- "setDebugBuild:"
- "setIsAccessibilityElement:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v40@0:8@16@24@?32"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:isKindOfClass:"
- "viewDidLoad"

```
