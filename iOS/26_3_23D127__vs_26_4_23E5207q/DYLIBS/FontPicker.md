## FontPicker

> `/System/Library/AccessibilityBundles/FontPicker.axbundle/FontPicker`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x460
-  __TEXT.__auth_stubs: 0x150
+3005.16.0.0.0
+  __TEXT.__text: 0x480
+  __TEXT.__auth_stubs: 0x140
   __TEXT.__objc_methlist: 0x68
   __TEXT.__cstring: 0x14e
   __TEXT.__const: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xb8
+  __AUTH_CONST.__auth_got: 0xb0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AA55F31E-5B00-3AC1-AE90-CB1BA69D9B7C
+  UUID: D4B96218-3384-3267-B74E-C56CA8F8DD8E
   Functions: 11
-  Symbols:   93
+  Symbols:   92
   CStrings:  54
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXFontPickerGlue accessibilityInitializeBundle] : 148 -> 152
~ ___49+[AXFontPickerGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184
~ +[_UIFontPickerTableViewCellAccessibility _accessibilityPerformValidations:] : 140 -> 148
~ -[_UIFontPickerTableViewCellAccessibility _accessibilityLoadAccessibilityInformation] : 260 -> 264
~ ___85-[_UIFontPickerTableViewCellAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 172 -> 176

```
