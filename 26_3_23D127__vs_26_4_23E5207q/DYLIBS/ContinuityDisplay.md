## ContinuityDisplay

> `/System/Library/AccessibilityBundles/ContinuityDisplay.axbundle/ContinuityDisplay`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x2b0
-  __TEXT.__auth_stubs: 0xc0
+3005.16.0.0.0
+  __TEXT.__text: 0x2c8
+  __TEXT.__auth_stubs: 0xb0
   __TEXT.__objc_methlist: 0x5c
   __TEXT.__cstring: 0x123
   __TEXT.__unwind_info: 0x78

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x68
+  __AUTH_CONST.__auth_got: 0x60
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 928CABAB-5E89-34A8-BAB7-EE0DA9BA03B7
+  UUID: 972793F3-5B6A-3546-BC06-C0DFC1F228B7
   Functions: 9
-  Symbols:   75
+  Symbols:   74
   CStrings:  46
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
Functions:
~ -[DisplayViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 164 -> 172
~ +[AXContinuityDisplayGlue accessibilityInitializeBundle] : 148 -> 152
~ ___56+[AXContinuityDisplayGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ _accessibilityLocalizedString : 176 -> 184

```
