## libAXSafeCategoryBundle.dylib

> `/usr/lib/libAXSafeCategoryBundle.dylib`

```diff

-3191.7.24.0.0
-  __TEXT.__text: 0x11d4
-  __TEXT.__auth_stubs: 0x350
+3191.19.0.0.0
+  __TEXT.__text: 0x121c
+  __TEXT.__auth_stubs: 0x320
   __TEXT.__objc_methlist: 0xb0
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x277

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x1b0
+  __AUTH_CONST.__auth_got: 0x198
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0x138

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1FBEF6E5-DE54-340F-B962-8A62A5CAE07B
+  UUID: 73144E0F-951D-3793-8AEE-17EC92006474
   Functions: 26
-  Symbols:   161
+  Symbols:   158
   CStrings:  79
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x26
- _objc_retain_x3
Functions:
~ +[UIAccessibilitySafeCategory safeCategoryTargetClass] : 76 -> 84
~ +[UIAccessibilitySafeCategory _initializeSafeCategoryFromValidationManager] : 92 -> 100
~ +[UIAccessibilitySafeCategory _installSafeCategoryValidationMethod] : 88 -> 96
~ +[UIAccessibilitySafeCategory _installLocalValidationMethodOnClassNamed:] : 344 -> 356
~ +[UIAccessibilitySafeCategory _addCategoryMethods:count:excluding:toClass:isClass:useReplace:] : 908 -> 916
~ +[UIAccessibilitySafeCategory _installSafeCategoryOnClass:isManaged:] : 624 -> 656
~ ___69+[UIAccessibilitySafeCategory _installSafeCategoryOnClass:isManaged:]_block_invoke : 100 -> 104
~ _UIAccessibilityInstallSafeCategory : 184 -> 196
~ _UIAccessibilityInstallSafeCategories : 732 -> 720
~ __UIAccessibilityCopyClassPath : 180 -> 184
~ __UIAccessibilitySafeCategoryDependsOnSafeCategory : 260 -> 256
~ __UIAccessibilitySafeCategoryAddDependenciesToArray : 348 -> 340

```
