## PasswordsSettings

> `/System/Library/AccessibilityBundles/PasswordsSettings.axbundle/PasswordsSettings`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x32c
-  __TEXT.__auth_stubs: 0xf0
+3005.16.0.0.0
+  __TEXT.__text: 0x354
+  __TEXT.__auth_stubs: 0xe0
   __TEXT.__objc_methlist: 0x74
   __TEXT.__cstring: 0xd8
   __TEXT.__unwind_info: 0x80

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x80
+  __AUTH_CONST.__auth_got: 0x78
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 14E38B15-8761-3702-B1D4-66E95ABDC551
+  UUID: 0FA82643-AF7C-3394-B3ED-0ACB09B82AB7
   Functions: 11
-  Symbols:   84
+  Symbols:   83
   CStrings:  47
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXPasswordsSettingsGlue accessibilityInitializeBundle] : 148 -> 152
~ ___56+[AXPasswordsSettingsGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184
~ +[PMPopUpMenuCellViewAccessibility _accessibilityPerformValidations:] : 108 -> 116
~ -[PMPopUpMenuCellViewAccessibility accessibilityValue] : 208 -> 224

```
