## CoreAuthUI

> `/System/Library/AccessibilityBundles/CoreAuthUI.axbundle/CoreAuthUI`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x498
-  __TEXT.__auth_stubs: 0x110
+3036.2.0.0.0
+  __TEXT.__text: 0x470
   __TEXT.__objc_methlist: 0x8c
-  __TEXT.__cstring: 0x10c
   __TEXT.__const: 0x8
+  __TEXT.__cstring: 0x10c
   __TEXT.__unwind_info: 0x80
-  __TEXT.__objc_classname: 0x6a
-  __TEXT.__objc_methname: 0x28e
-  __TEXT.__objc_methtype: 0x35
-  __TEXT.__objc_stubs: 0x1c0
-  __DATA_CONST.__got: 0x38
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x90
+  __DATA_CONST.__got: 0x38
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x1b0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__bss: 0x11
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 43E6381C-58C0-35BF-A3C0-E7E9422F9D8B
+  UUID: C4F1349E-C424-3630-B541-FD64D32ED615
   Functions: 14
-  Symbols:   95
-  CStrings:  53
+  Symbols:   96
+  CStrings:  24
 
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
~ +[AXCoreAuthUIGlue accessibilityInitializeBundle] : 152 -> 148
~ ___49+[AXCoreAuthUIGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ _accessibilityLocalizedString : 184 -> 176
~ -[FaceIdViewControllerAccessibility _accessibilityNotificationFeedbackGenerator] : 100 -> 92
~ ___64-[FaceIdViewControllerAccessibility mechanismEvent:value:reply:]_block_invoke : 264 -> 248
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXCoreAuthUIGlue"
- "SafeCategory"
- "__FaceIdViewControllerAccessibility_super"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityNotificationFeedbackGenerator"
- "_accessibilityPerformValidations:"
- "_axNotificationFeedbackGenerator"
- "_setAXNotificationFeedbackGenerator:"
- "accessibilityInitializeBundle"
- "bundleForClass:"
- "init"
- "installSafeCategory:canInteractWithTargetClass:"
- "localizedStringForKey:value:table:"
- "notificationOccurred:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "setDebugBuild:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "v24@0:8@16"
- "v40@0:8q16@24@?32"
- "validateClass:hasInstanceMethod:withFullSignature:"

```
