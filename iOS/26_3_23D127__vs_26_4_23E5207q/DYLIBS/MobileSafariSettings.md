## MobileSafariSettings

> `/System/Library/AccessibilityBundles/MobileSafariSettings.axbundle/MobileSafariSettings`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xbd4
-  __TEXT.__auth_stubs: 0x180
+3005.16.0.0.0
+  __TEXT.__text: 0xc70
+  __TEXT.__auth_stubs: 0x170
   __TEXT.__objc_methlist: 0x19c
   __TEXT.__cstring: 0x5d3
   __TEXT.__unwind_info: 0xa8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xc8
+  __AUTH_CONST.__auth_got: 0xc0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x660
   __AUTH_CONST.__objc_const: 0x630

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ECB84A55-E6C7-3FAD-98BA-963996E4ACE4
+  UUID: 283D48E5-64DD-3CBF-8AB7-990FF18C362A
   Functions: 37
-  Symbols:   193
+  Symbols:   192
   CStrings:  158
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ _accessibilityMobileSafariLocalizedString : 208 -> 224
~ _accessibilitySafariServicesLocalizedString : 208 -> 224
~ _accessibilitySafariScribbleLocalizedString : 208 -> 224
~ _profileSymbolAccessibilityLabel : 468 -> 480
~ -[ProfileIconButtonAccessibility accessibilityLabel] : 312 -> 344
~ +[ColorPickerButtonAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[ColorPickerButtonAccessibility accessibilityLabel] : 136 -> 148
~ +[SymbolCollectionViewCellAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[SymbolCollectionViewCellAccessibility accessibilityLabel] : 84 -> 92
~ ___59+[AXMobileSafariSettingsGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___59+[AXMobileSafariSettingsGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ ___59+[AXMobileSafariSettingsGlue accessibilityInitializeBundle]_block_invoke_4 : 152 -> 160
~ _accessibilityLocalizedString : 156 -> 164
~ -[SafariSavedPasswordsControllerAccessibility _accessibilityLoadAccessibilityInformation] : 104 -> 108

```
