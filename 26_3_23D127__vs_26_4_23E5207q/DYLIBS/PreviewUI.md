## PreviewUI

> `/System/Library/AccessibilityBundles/PreviewUI.axbundle/PreviewUI`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x56c
-  __TEXT.__auth_stubs: 0x110
+3005.16.0.0.0
+  __TEXT.__text: 0x5a4
+  __TEXT.__auth_stubs: 0x100
   __TEXT.__objc_methlist: 0x8c
   __TEXT.__cstring: 0x151
   __TEXT.__unwind_info: 0x78

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x90
+  __AUTH_CONST.__auth_got: 0x88
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x1c0
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D9255ABB-A1D5-3DE1-ADDA-C342CED6E192
+  UUID: F9E51A37-B689-30B0-89C9-424F4ED36C5B
   Functions: 14
-  Symbols:   99
+  Symbols:   98
   CStrings:  72
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXPreviewUIGlue accessibilityInitializeBundle] : 148 -> 152
~ ___48+[AXPreviewUIGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184
~ +[QLMarkupItemViewControllerAccessibility _accessibilityPerformValidations:] : 280 -> 288
~ -[QLMarkupItemViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 204 -> 220
~ -[QLMarkupItemViewControllerAccessibility viewDidLoad] : 104 -> 108
~ -[QLMarkupItemViewControllerAccessibility _axPhotoDescriptionFromContext:] : 100 -> 112

```
