## HDSViewService

> `/System/Library/AccessibilityBundles/HDSViewService.axbundle/HDSViewService`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x484
-  __TEXT.__auth_stubs: 0x100
+3005.16.0.0.0
+  __TEXT.__text: 0x4b4
+  __TEXT.__auth_stubs: 0xf0
   __TEXT.__objc_methlist: 0xbc
   __TEXT.__cstring: 0x182
   __TEXT.__unwind_info: 0x88

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x88
+  __AUTH_CONST.__auth_got: 0x80
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x1a0
   __AUTH_CONST.__objc_const: 0x2d0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F557CF22-3EC4-3EC7-89AC-582CC15D4182
+  UUID: 0A0CF429-819B-3A46-944A-65BDF2565165
   Functions: 15
-  Symbols:   102
+  Symbols:   101
   CStrings:  59
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[HomePodSetupLeftRightViewControllerAccessibility _accessibilityPerformValidations:] : 108 -> 116
~ -[HomePodSetupLeftRightViewControllerAccessibility _accessibilityMarkupStereoButtons] : 188 -> 204
~ +[AXHDSViewServiceGlue accessibilityInitializeBundle] : 148 -> 152
~ ___53+[AXHDSViewServiceGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___53+[AXHDSViewServiceGlue accessibilityInitializeBundle]_block_invoke_3 : 92 -> 100
~ _accessibilityLocalizedString : 176 -> 184

```
