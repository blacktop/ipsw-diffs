## ShortcutsUI

> `/System/Library/AccessibilityBundles/ShortcutsUI.axbundle/ShortcutsUI`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x468
-  __TEXT.__auth_stubs: 0x140
+3005.16.0.0.0
+  __TEXT.__text: 0x4b0
+  __TEXT.__auth_stubs: 0x130
   __TEXT.__objc_methlist: 0x5c
   __TEXT.__cstring: 0x163
   __TEXT.__unwind_info: 0x80

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xa8
+  __AUTH_CONST.__auth_got: 0xa0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6C7F15A7-24C9-3E9E-9697-5BECE47EA576
+  UUID: B1EF1CA5-5198-3D3C-8D25-E0E6C3A4194A
   Functions: 9
-  Symbols:   82
+  Symbols:   81
   CStrings:  62
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXShortcutsUIGlue accessibilityInitializeBundle] : 148 -> 152
~ ___50+[AXShortcutsUIGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184
~ +[WFApertureStatusViewControllerAccessibility _accessibilityPerformValidations:] : 248 -> 260
~ -[WFApertureStatusViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 408 -> 452

```
