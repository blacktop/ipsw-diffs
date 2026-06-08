## BPSStingSetup

> `/System/Library/AccessibilityBundles/BPSStingSetup.axbundle/BPSStingSetup`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x314
-  __TEXT.__auth_stubs: 0xd0
+3036.2.0.0.0
+  __TEXT.__text: 0x2f0
   __TEXT.__objc_methlist: 0x68
   __TEXT.__cstring: 0xe6
   __TEXT.__unwind_info: 0x80
-  __TEXT.__objc_classname: 0x6b
-  __TEXT.__objc_methname: 0x1eb
-  __TEXT.__objc_methtype: 0x2b
-  __TEXT.__objc_stubs: 0x160
-  __DATA_CONST.__got: 0x20
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x70
+  __DATA_CONST.__got: 0x20
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x1b0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6CAEB597-4A51-36D1-AF9B-5A8FFDF86D9E
+  UUID: 5813DEB8-4F16-32E0-80B5-D51FC0C24023
   Functions: 10
-  Symbols:   75
-  CStrings:  46
+  Symbols:   76
+  CStrings:  20
 
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
~ +[AXBPSStingSetupGlue accessibilityInitializeBundle] : 152 -> 148
~ ___52+[AXBPSStingSetupGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ _accessibilityLocalizedString : 184 -> 176
~ +[BPSStingFeatureCellAccessibility _accessibilityPerformValidations:] : 132 -> 124
~ -[BPSStingFeatureCellAccessibility accessibilityLabel] : 160 -> 148
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXBPSStingSetupGlue"
- "B16@0:8"
- "SafeCategory"
- "__BPSStingFeatureCellAccessibility_super"
- "_accessibilityPerformValidations:"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "bundleForClass:"
- "init"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
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
- "validateClass:hasProperty:withType:"

```
