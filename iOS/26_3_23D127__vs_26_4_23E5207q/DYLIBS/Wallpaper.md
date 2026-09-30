## Wallpaper

> `/System/Library/AccessibilityBundles/Wallpaper.axbundle/Wallpaper`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x3d8
-  __TEXT.__auth_stubs: 0x100
+3005.16.0.0.0
+  __TEXT.__text: 0x40c
+  __TEXT.__auth_stubs: 0xf0
   __TEXT.__objc_methlist: 0x68
   __TEXT.__cstring: 0x17f
   __TEXT.__unwind_info: 0x78

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x88
+  __AUTH_CONST.__auth_got: 0x80
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x180
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 58AE921B-366E-39A5-BEC4-F597B3E8C147
+  UUID: FEDD3E13-28B5-3010-A0FF-F456A289A393
   Functions: 11
-  Symbols:   86
+  Symbols:   85
   CStrings:  56
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ _accessibilityLocalizedString : 176 -> 184
~ +[AXWallpaperGlue accessibilityInitializeBundle] : 152 -> 156
~ ___48+[AXWallpaperGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ +[WallpaperPreviewCellAccessibility _accessibilityPerformValidations:] : 152 -> 164
~ -[WallpaperPreviewCellAccessibility _accessibilityLoadAccessibilityInformation] : 276 -> 300

```
