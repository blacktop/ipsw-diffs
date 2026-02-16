## InputUI

> `/System/Library/AccessibilityBundles/InputUI.axbundle/InputUI`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x7c4
-  __TEXT.__auth_stubs: 0x190
+3005.16.0.0.0
+  __TEXT.__text: 0x80c
+  __TEXT.__auth_stubs: 0x180
   __TEXT.__objc_methlist: 0x74
   __TEXT.__cstring: 0x1d9
   __TEXT.__const: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xd0
+  __AUTH_CONST.__auth_got: 0xc8
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x2e0
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 89233CE5-3413-3018-B02F-81FEE6D49956
+  UUID: B7E77182-FF79-334A-971C-81DCF58FAA68
   Functions: 14
-  Symbols:   124
+  Symbols:   123
   CStrings:  92
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXInputUIGlue accessibilityInitializeBundle] : 148 -> 152
~ ___46+[AXInputUIGlue accessibilityInitializeBundle]_block_invoke : 216 -> 220
~ ___46+[AXInputUIGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184
~ +[InputUIWindowAccessibility _accessibilityPerformValidations:] : 204 -> 212
~ -[InputUIWindowAccessibility _accessibilityLoadAccessibilityInformation] : 532 -> 544
~ ___72-[InputUIWindowAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 120 -> 132
~ ___72-[InputUIWindowAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_3 : 224 -> 244

```
