## iAdFramework

> `/System/Library/AccessibilityBundles/iAdFramework.axbundle/iAdFramework`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x298
-  __TEXT.__auth_stubs: 0xe0
+3005.16.0.0.0
+  __TEXT.__text: 0x2ac
+  __TEXT.__auth_stubs: 0xd0
   __TEXT.__objc_methlist: 0x68
   __TEXT.__cstring: 0x78
   __TEXT.__unwind_info: 0x78

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x78
+  __AUTH_CONST.__auth_got: 0x70
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3ADA7A0D-EF7F-3D03-8526-2083441D7099
+  UUID: 8D836C3E-E631-340F-A8BB-5EC42E7B5466
   Functions: 10
-  Symbols:   77
+  Symbols:   76
   CStrings:  38
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
Functions:
~ _accessibilityLocalizedString : 176 -> 184
~ +[AXAdLibGlue accessibilityInitializeBundle] : 148 -> 152
~ ___44+[AXAdLibGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ -[ADBannerViewAccessibility isAccessibilityElement] : 116 -> 120

```
