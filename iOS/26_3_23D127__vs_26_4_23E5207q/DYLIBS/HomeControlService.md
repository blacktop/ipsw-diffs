## HomeControlService

> `/System/Library/AccessibilityBundles/HomeControlService.axbundle/HomeControlService`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x380
-  __TEXT.__auth_stubs: 0x100
+3005.16.0.0.0
+  __TEXT.__text: 0x3a0
+  __TEXT.__auth_stubs: 0xf0
   __TEXT.__objc_methlist: 0x64
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x113

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x88
+  __AUTH_CONST.__auth_got: 0x80
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A3FC604E-E313-332B-ACAD-20F9EE9A2282
+  UUID: A2E76230-BA8E-31B7-AB75-33ACF2978E03
   Functions: 13
-  Symbols:   87
+  Symbols:   86
   CStrings:  48
 
Symbols:
+ _objc_release_x20
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_release_x21
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[HCSRemoteViewControllerAccessibility _accessibilityPerformValidations:] : 176 -> 188
~ -[HCSRemoteViewControllerAccessibility willBeginTransition:forCompactModule:] : 228 -> 232
~ ___57+[AXHomeControlServiceGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___57+[AXHomeControlServiceGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ _accessibilityLocalizedString : 148 -> 156

```
