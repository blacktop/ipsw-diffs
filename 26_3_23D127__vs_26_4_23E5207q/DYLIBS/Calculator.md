## Calculator

> `/System/Library/AccessibilityBundles/Calculator.axbundle/Calculator`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x210
-  __TEXT.__auth_stubs: 0xa0
+3005.16.0.0.0
+  __TEXT.__text: 0x228
+  __TEXT.__auth_stubs: 0x90
   __TEXT.__objc_methlist: 0x5c
   __TEXT.__cstring: 0xd2
   __TEXT.__unwind_info: 0x70

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x58
+  __AUTH_CONST.__auth_got: 0x50
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x100
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3ED4CF49-58F7-3F17-B5C5-A6DE4F39C8EE
+  UUID: F528A131-5A4B-3C85-98A6-278B92409902
   Functions: 9
-  Symbols:   69
+  Symbols:   68
   CStrings:  40
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
Functions:
~ +[AXCalculatorGlue accessibilityInitializeBundle] : 148 -> 152
~ ___49+[AXCalculatorGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ _accessibilityLocalizedString : 156 -> 164
~ -[Calculator_UIApplicationAccessibility _accessibilityActiveKeyboard] : 84 -> 92

```
