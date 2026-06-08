## NFCControlCenterModule

> `/System/Library/AccessibilityBundles/NFCControlCenterModule.axbundle/NFCControlCenterModule`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x880
-  __TEXT.__auth_stubs: 0x140
+3036.2.0.0.0
+  __TEXT.__text: 0x81c
   __TEXT.__objc_methlist: 0xd8
-  __TEXT.__cstring: 0x222
   __TEXT.__const: 0x8
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__unwind_info: 0xb8
-  __TEXT.__objc_classname: 0xc4
-  __TEXT.__objc_methname: 0x345
-  __TEXT.__objc_methtype: 0x41
-  __TEXT.__objc_stubs: 0x2a0
-  __DATA_CONST.__got: 0x40
+  __TEXT.__cstring: 0x222
+  __TEXT.__unwind_info: 0xb0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xe8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xb0
+  __DATA_CONST.__got: 0x40
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x2d0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1F2F8071-3F0D-3ED6-8940-375C0541CAED
-  Functions: 22
-  Symbols:   135
-  CStrings:  98
+  UUID: DBBD3876-B2F3-34AC-91EA-C252C2E316CE
+  Functions: 21
+  Symbols:   134
+  CStrings:  56
 
Symbols:
+ GCC_except_table15
+ ___block_literal_global.352
+ ___block_literal_global.354
+ ___block_literal_global.360
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- +[AXNFCControlCenterModuleGlue accessibilityInitializeBundle].cold.1
- GCC_except_table3
- ___block_literal_global.331
- ___block_literal_global.333
- ___block_literal_global.339
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[AXNFCControlCenterModuleGlue accessibilityInitializeBundle] : 44 -> 40
~ ___61+[AXNFCControlCenterModuleGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___61+[AXNFCControlCenterModuleGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 96
~ ___61+[AXNFCControlCenterModuleGlue accessibilityInitializeBundle]_block_invoke_4 : 136 -> 128
~ _accessibilityLocalizedString : 168 -> 160
~ -[NFCCWrappedLabelAccessibility _accessibilityLoadAccessibilityInformation] : 108 -> 104
~ -[NFCCWrappedLabelAccessibility accessibilityLabel] : 92 -> 84
~ -[NFCCWrappedLabelAccessibility accessibilityTraits] : 68 -> 64
~ +[NFCCContentViewControllerAccessibility _accessibilityPerformValidations:] : 284 -> 276
~ -[NFCCContentViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 372 -> 368
~ ___84-[NFCCContentViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 272 -> 252
~ -[NFCCContentViewControllerAccessibility _setModuleState:animated:] : 184 -> 180
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXNFCControlCenterModuleGlue"
- "B16@0:8"
- "Q16@0:8"
- "SafeCategory"
- "__NFCCContentViewControllerAccessibility_super"
- "__NFCCWrappedLabelAccessibility_super"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_setAccessibilityTraitsBlock:"
- "_setAccessibilityValueBlock:"
- "accessibilityBundles"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityTraits"
- "alpha"
- "bundleForClass:"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeBoolForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeIntegerForKey:"
- "safeUIViewForKey:"
- "safeValueForKey:"
- "setDebugBuild:"
- "setIsAccessibilityElement:"
- "setNeedsLoadAccessibilityInformation"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "v24@0:8@16"
- "v28@0:8q16B24"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"

```
