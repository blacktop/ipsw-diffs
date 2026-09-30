## ContinuityCapture

> `/System/Library/AccessibilityBundles/ContinuityCapture.axbundle/ContinuityCapture`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x728
-  __TEXT.__auth_stubs: 0x120
+3005.16.0.0.0
+  __TEXT.__text: 0x77c
+  __TEXT.__auth_stubs: 0x110
   __TEXT.__objc_methlist: 0x124
   __TEXT.__cstring: 0x1fc
   __TEXT.__unwind_info: 0xa0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x98
+  __AUTH_CONST.__auth_got: 0x90
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x3a0
   __AUTH_CONST.__objc_const: 0x3f0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 29CB22A1-420C-36EF-B93B-8E34B63043CE
+  UUID: 3D20CBD1-C36F-36A8-B5DA-3549E1AB5FCA
   Functions: 22
-  Symbols:   130
+  Symbols:   129
   CStrings:  104
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXContinuityCaptureGlue accessibilityInitializeBundle] : 148 -> 152
~ ___56+[AXContinuityCaptureGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___56+[AXContinuityCaptureGlue accessibilityInitializeBundle]_block_invoke_3 : 112 -> 120
~ _accessibilityLocalizedString : 176 -> 184
~ -[CSToggleButtonAccessibility accessibilityValue] : 88 -> 92
~ +[CSShieldViewControllerAccessibility _accessibilityPerformValidations:] : 208 -> 220
~ -[CSShieldViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 340 -> 372
~ +[CSMicControlAccessibility _accessibilityPerformValidations:] : 148 -> 156
~ -[CSMicControlAccessibility accessibilityValue] : 116 -> 120

```
