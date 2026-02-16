## Diagnostics

> `/System/Library/AccessibilityBundles/Diagnostics.axbundle/Diagnostics`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x1198
-  __TEXT.__auth_stubs: 0x1e0
+3005.16.0.0.0
+  __TEXT.__text: 0x1288
+  __TEXT.__auth_stubs: 0x1d0
   __TEXT.__objc_methlist: 0x22c
   __TEXT.__cstring: 0x350
   __TEXT.__const: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xf8
+  __AUTH_CONST.__auth_got: 0xf0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x560
   __AUTH_CONST.__objc_const: 0x750

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9EF26FAA-F61F-3C83-AAE0-FDF72CF24843
+  UUID: FF5B83A4-1EFD-3330-82D8-2BCCB9FC6A35
   Functions: 39
-  Symbols:   224
+  Symbols:   223
   CStrings:  150
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXDiagnosticsGlue accessibilityInitializeBundle] : 148 -> 152
~ ___50+[AXDiagnosticsGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___50+[AXDiagnosticsGlue accessibilityInitializeBundle]_block_invoke_3 : 172 -> 180
~ _accessibilityLocalizedString : 176 -> 184
~ +[DeviceInformationViewAccessibility _accessibilityPerformValidations:] : 344 -> 352
~ -[DeviceInformationViewAccessibility _accessibilityLoadAccessibilityInformation] : 348 -> 372
~ ___80-[DeviceInformationViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 248 -> 268
~ -[DeviceInformationViewAccessibility subviewsForStackViewElement] : 288 -> 316
~ -[DeviceInformationViewAccessibility _axLoadLabelAccessibility] : 328 -> 352
~ -[ImageButtonAccessibility accessibilityLabel] : 84 -> 92
~ +[PromptViewAccessibility _accessibilityPerformValidations:] : 184 -> 196
~ -[PromptViewAccessibility subviewsForStackViewElement] : 336 -> 364
~ -[TestRunnerViewAccessibility subviewsForStackViewElement] : 412 -> 432
~ -[TextButtonAccessibility accessibilityLabel] : 84 -> 92
~ +[CardViewCellAccessibility _accessibilityPerformValidations:] : 144 -> 156
~ -[CardViewCellAccessibility accessibilityElements] : 516 -> 540

```
