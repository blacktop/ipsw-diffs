## FocusUIModule

> `/System/Library/AccessibilityBundles/FocusUIModule.axbundle/FocusUIModule`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0xdb0
-  __TEXT.__auth_stubs: 0x160
-  __TEXT.__objc_methlist: 0xc8
+3036.2.0.0.0
+  __TEXT.__text: 0xd3c
+  __TEXT.__objc_methlist: 0xbc
   __TEXT.__const: 0x8
-  __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__cstring: 0x25f
-  __TEXT.__unwind_info: 0xc8
-  __TEXT.__objc_classname: 0xc7
-  __TEXT.__objc_methname: 0x4b5
-  __TEXT.__objc_methtype: 0x2b
-  __TEXT.__objc_stubs: 0x440
-  __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x108
+  __TEXT.__gcc_except_tab: 0x78
+  __TEXT.__cstring: 0x263
+  __TEXT.__unwind_info: 0xc0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x138
+  __DATA_CONST.__objc_selrefs: 0x130
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xc0
+  __DATA_CONST.__got: 0x40
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x2c0
+  __AUTH_CONST.__cfstring: 0x2a0
   __AUTH_CONST.__objc_const: 0x2d0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B9904CB5-42E4-3E3D-8E15-BF15BF5E83FA
-  Functions: 24
-  Symbols:   157
-  CStrings:  104
+  UUID: DB0F6243-93F8-3F06-B3BE-D25114F2F54D
+  Functions: 23
+  Symbols:   154
+  CStrings:  50
 
Symbols:
+ GCC_except_table15
+ GCC_except_table2
+ ___block_literal_global.351
+ ___block_literal_global.360
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_setAccessibilityActivateBlock:
+ _objc_msgSend$performGlyphButtonActionForControlTemplateView:
+ _objc_retain_x1
+ _objc_retain_x2
- -[FCCCModuleViewControllerAccessibility _accessibilityButtonView]
- GCC_except_table3
- ___block_descriptor_40_e8_32w_e16_{CGPoint=dd}8?0lw32l8
- ___block_literal_global.330
- ___block_literal_global.339
- _objc_msgSend$_accessibilityButtonView
- _objc_msgSend$_setAccessibilityActivationPointBlock:
- _objc_msgSend$accessibilityActivationPoint
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[FCCCControlCenterModuleAccessibility _accessibilityPerformValidations:] : 268 -> 260
~ -[FCCCControlCenterModuleAccessibility _accessibilityLoadAccessibilityInformation] : 596 -> 592
~ ___82-[FCCCControlCenterModuleAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 176 -> 164
~ ___82-[FCCCControlCenterModuleAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_4 : 100 -> 96
~ -[FCCCControlCenterModuleAccessibility _accessibilityIsOnboardingControlVisible] : 192 -> 176
~ +[AXFocusUIModuleGlue accessibilityInitializeBundle] : 152 -> 148
~ ___52+[AXFocusUIModuleGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ ___52+[AXFocusUIModuleGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 92
~ _accessibilityLocalizedString : 184 -> 176
~ +[FCCCModuleViewControllerAccessibility _accessibilityPerformValidations:] : 232 -> 224
~ -[FCCCModuleViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 688 -> 644
~ ___83-[FCCCModuleViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 184 -> 172
~ ___83-[FCCCModuleViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 116 -> 112
~ ___83-[FCCCModuleViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_4 : 92 -> 124
CStrings:
+ "performGlyphButtonActionForControlTemplateView:"
- "#16@0:8"
- "@"
- "@16@0:8"
- "AXFocusUIModuleGlue"
- "B16@0:8"
- "SafeCategory"
- "__FCCCControlCenterModuleAccessibility_super"
- "__FCCCModuleViewControllerAccessibility_super"
- "_accessibilityButtonView"
- "_accessibilityIsOnboardingControlVisible"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityModuleViewController"
- "_accessibilityPerformValidations:"
- "_roundButton"
- "_setAccessibilityActivationPointBlock:"
- "_setAccessibilityCustomActionsBlock:"
- "_setAccessibilityHintBlock:"
- "_setAccessibilityLabelBlock:"
- "_setAccessibilityTraitsBlock:"
- "_setAccessibilityValueBlock:"
- "_setIsAccessibilityElementBlock:"
- "accessibilityActivationPoint"
- "accessibilityCustomActions"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "bundleForClass:"
- "init"
- "installSafeCategory:canInteractWithTargetClass:"
- "localizedCaseInsensitiveCompare:"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "roundButton"
- "safeBoolForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeUIViewForKey:"
- "safeValueForKey:"
- "setAccessibilityLabel:"
- "setDebugBuild:"
- "setIsAccessibilityElement:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "v24@0:8@16"
- "validateClass:"
- "validateClass:hasClassMethod:withFullSignature:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:isKindOfClass:"
- "validateProtocol:hasRequiredInstanceMethod:"
- "{CGPoint=dd}8@?0"

```
