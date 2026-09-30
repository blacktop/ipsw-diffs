## PassKitFramework

> `/System/Library/AccessibilityBundles/PassKitFramework.axbundle/PassKitFramework`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x5c8
-  __TEXT.__auth_stubs: 0x90
+3005.16.0.0.0
+  __TEXT.__text: 0x5dc
+  __TEXT.__auth_stubs: 0x80
   __TEXT.__objc_methlist: 0x14
   __TEXT.__cstring: 0x3ee
   __TEXT.__unwind_info: 0x78

   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x50
+  __AUTH_CONST.__auth_got: 0x48
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x620
   __AUTH_CONST.__objc_const: 0x90

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FB18C137-1DD9-3C46-9C32-09C16C84B041
+  UUID: 085C0DEC-6228-3BAD-BA19-B7F2DB943C1C
   Functions: 5
-  Symbols:   47
+  Symbols:   46
   CStrings:  124
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
Functions:
~ +[AXPassKitFrameworkGlue accessibilityInitializeBundle] : 100 -> 104
~ ___55+[AXPassKitFrameworkGlue accessibilityInitializeBundle]_block_invoke : 1104 -> 1108
~ ___55+[AXPassKitFrameworkGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184

```
