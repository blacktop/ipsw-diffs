## PassesLockScreenPlugin

> `/System/Library/AccessibilityBundles/PassesLockScreenPlugin.axbundle/PassesLockScreenPlugin`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x4c8
-  __TEXT.__auth_stubs: 0x140
+3005.16.0.0.0
+  __TEXT.__text: 0x4e8
+  __TEXT.__auth_stubs: 0x130
   __TEXT.__objc_methlist: 0x80
   __TEXT.__cstring: 0x10c
   __TEXT.__const: 0x18

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xb0
+  __AUTH_CONST.__auth_got: 0xa8
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ADE6BE1A-2DBF-3D0B-B9BC-7D484DCCC53F
+  UUID: 19F90E70-670F-3C95-AD30-D2411E0DE973
   Functions: 14
-  Symbols:   97
+  Symbols:   96
   CStrings:  54
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXPassesLockScreenPluginGlue accessibilityInitializeBundle] : 100 -> 104
~ ___61+[AXPassesLockScreenPluginGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ _accessibilityLocalizedString : 176 -> 184
~ +[WLLockScreenViewAccessibility _accessibilityPerformValidations:] : 204 -> 212
~ ___59-[WLLockScreenViewAccessibility accessibilityPerformEscape]_block_invoke : 180 -> 188

```
