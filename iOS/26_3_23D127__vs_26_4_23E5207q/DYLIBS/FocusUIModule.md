## FocusUIModule

> `/System/Library/AccessibilityBundles/FocusUIModule.axbundle/FocusUIModule`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xd3c
-  __TEXT.__auth_stubs: 0x170
+3005.16.0.0.0
+  __TEXT.__text: 0xdb0
+  __TEXT.__auth_stubs: 0x160
   __TEXT.__objc_methlist: 0xc8
   __TEXT.__const: 0x8
   __TEXT.__gcc_except_tab: 0x80

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x138
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xc8
+  __AUTH_CONST.__auth_got: 0xc0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x2c0
   __AUTH_CONST.__objc_const: 0x2d0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 97195276-8812-3CA1-9398-72F4D625480A
+  UUID: EAB0BAC2-1FF0-3402-BDDC-CD609360B6CB
   Functions: 24
-  Symbols:   158
+  Symbols:   157
   CStrings:  104
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[FCCCControlCenterModuleAccessibility _accessibilityPerformValidations:] : 260 -> 268
~ -[FCCCControlCenterModuleAccessibility _accessibilityLoadAccessibilityInformation] : 592 -> 596
~ ___82-[FCCCControlCenterModuleAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 164 -> 176
~ ___82-[FCCCControlCenterModuleAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_4 : 96 -> 100
~ -[FCCCControlCenterModuleAccessibility _accessibilityIsOnboardingControlVisible] : 176 -> 192
~ +[AXFocusUIModuleGlue accessibilityInitializeBundle] : 148 -> 152
~ ___52+[AXFocusUIModuleGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___52+[AXFocusUIModuleGlue accessibilityInitializeBundle]_block_invoke_3 : 92 -> 100
~ _accessibilityLocalizedString : 176 -> 184
~ +[FCCCModuleViewControllerAccessibility _accessibilityPerformValidations:] : 224 -> 232
~ -[FCCCModuleViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 676 -> 688
~ ___83-[FCCCModuleViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 172 -> 184
~ ___83-[FCCCModuleViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 112 -> 116
~ ___83-[FCCCModuleViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_3 : 100 -> 108
~ ___83-[FCCCModuleViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_4 : 88 -> 92

```
