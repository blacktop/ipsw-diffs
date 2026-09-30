## ScreenshotServicesFramework

> `/System/Library/AccessibilityBundles/ScreenshotServicesFramework.axbundle/ScreenshotServicesFramework`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x3b0
-  __TEXT.__auth_stubs: 0xf0
+3005.16.0.0.0
+  __TEXT.__text: 0x3d8
+  __TEXT.__auth_stubs: 0xd0
   __TEXT.__objc_methlist: 0xbc
   __TEXT.__cstring: 0x148
   __TEXT.__unwind_info: 0x80

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x80
+  __AUTH_CONST.__auth_got: 0x70
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x2d0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7797C03F-5C19-39BA-AC0F-B1B29340016C
+  UUID: 8D149F4D-45AD-3C1D-8233-78EB285DE6CC
   Functions: 15
-  Symbols:   100
+  Symbols:   98
   CStrings:  59
 
Symbols:
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXScreenshotServicesFrameworkGlue accessibilityInitializeBundle] : 148 -> 152
~ ___66+[AXScreenshotServicesFrameworkGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___66+[AXScreenshotServicesFrameworkGlue accessibilityInitializeBundle]_block_invoke_3 : 92 -> 100
~ _accessibilityLocalizedString : 176 -> 184
~ +[SSVellumOpacityControlAccessibility _accessibilityPerformValidations:] : 136 -> 144
~ -[SSVellumOpacityControlAccessibility _accessibilityLoadAccessibilityInformation] : 132 -> 140

```
