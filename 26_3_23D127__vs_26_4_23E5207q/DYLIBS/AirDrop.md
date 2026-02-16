## AirDrop

> `/System/Library/AccessibilityBundles/AirDrop.axbundle/AirDrop`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x550
-  __TEXT.__auth_stubs: 0x160
+3005.16.0.0.0
+  __TEXT.__text: 0x57c
+  __TEXT.__auth_stubs: 0x150
   __TEXT.__objc_methlist: 0xc8
   __TEXT.__cstring: 0x173
   __TEXT.__const: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xc0
+  __AUTH_CONST.__auth_got: 0xb8
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x180
   __AUTH_CONST.__objc_const: 0x2d0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6A887ED7-B42D-38BC-A7F3-9DE3E8A4E1E3
+  UUID: 488C7BF3-070F-3BC9-90CF-C29696C57B28
   Functions: 18
-  Symbols:   121
+  Symbols:   120
   CStrings:  64
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXAirDropGlue accessibilityInitializeBundle] : 144 -> 148
~ ___46+[AXAirDropGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___46+[AXAirDropGlue accessibilityInitializeBundle]_block_invoke_3 : 92 -> 100
~ _accessibilityLocalizedString : 160 -> 168
~ +[AirDropBrowserViewControllerAccessibility _accessibilityPerformValidations:] : 192 -> 200
~ -[AirDropBrowserViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 244 -> 248
~ ___87-[AirDropBrowserViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 108 -> 116

```
