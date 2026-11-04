## CallsAppUI

> `/System/Library/AccessibilityBundles/CallsAppUI.axbundle/CallsAppUI`

```diff

-3050.3.8.0.0
-  __TEXT.__text: 0x36c
-  __TEXT.__objc_methlist: 0x74
-  __TEXT.__cstring: 0xe5
-  __TEXT.__unwind_info: 0x80
+3050.3.12.0.0
+  __TEXT.__text: 0x44c
+  __TEXT.__objc_methlist: 0x8c
+  __TEXT.__cstring: 0x13b
+  __TEXT.__unwind_info: 0x90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa0
+  __DATA_CONST.__objc_selrefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x28
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x120
+  __AUTH_CONST.__cfstring: 0x180
   __AUTH_CONST.__objc_const: 0x1b0
   __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__objc_data: 0xf0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11
-  Symbols:   60
-  CStrings:  13
+  Functions: 13
+  Symbols:   62
+  CStrings:  17
 
Symbols:
+ -[RecentsViewControllerAccessibility _axAllowContentBehindContentUnavailableView]
+ -[RecentsViewControllerAccessibility setContentUnavailableConfiguration:]
Functions:
~ +[RecentsViewControllerAccessibility _accessibilityPerformValidations:] : 112 -> 188
~ -[RecentsViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 76 -> 84
CStrings:
+ "@"
+ "UIViewController"
+ "_contentUnavailableWrapperView"
+ "setContentUnavailableConfiguration:"
```
