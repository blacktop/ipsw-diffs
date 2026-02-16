## AirDropUI

> `/System/Library/AccessibilityBundles/AirDropUI.axbundle/AirDropUI`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x37c
-  __TEXT.__auth_stubs: 0x110
+3005.16.0.0.0
+  __TEXT.__text: 0x3a4
+  __TEXT.__auth_stubs: 0x100
   __TEXT.__objc_methlist: 0xac
   __TEXT.__cstring: 0x14b
   __TEXT.__unwind_info: 0x80

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x90
+  __AUTH_CONST.__auth_got: 0x88
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0x2d0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 00A05599-F295-3204-B262-56CA1F35F69E
+  UUID: 52A20042-09B6-36B9-A524-2D01388855EE
   Functions: 14
-  Symbols:   100
+  Symbols:   99
   CStrings:  54
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXAirDropUIGlue accessibilityInitializeBundle] : 148 -> 152
~ ___48+[AXAirDropUIGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___48+[AXAirDropUIGlue accessibilityInitializeBundle]_block_invoke_3 : 92 -> 100
~ _accessibilityLocalizedString : 176 -> 184
~ +[LiveActivitiesHostingControllerAccessibility _accessibilityPerformValidations:] : 128 -> 136
~ -[LiveActivitiesHostingControllerAccessibility viewDidAppear:] : 176 -> 184

```
