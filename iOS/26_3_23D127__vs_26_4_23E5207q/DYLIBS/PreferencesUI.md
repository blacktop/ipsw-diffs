## PreferencesUI

> `/System/Library/AccessibilityBundles/PreferencesUI.axbundle/PreferencesUI`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x518
-  __TEXT.__auth_stubs: 0x120
+3005.16.0.0.0
+  __TEXT.__text: 0x560
+  __TEXT.__auth_stubs: 0x110
   __TEXT.__objc_methlist: 0xf4
   __TEXT.__cstring: 0x1ad
   __TEXT.__unwind_info: 0x98

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x98
+  __AUTH_CONST.__auth_got: 0x90
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x200
   __AUTH_CONST.__objc_const: 0x3f0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4A210B00-85F3-3D78-8117-E0909D2C425C
+  UUID: DB3EA8AD-0266-3353-B1AA-3D25D2960F3C
   Functions: 21
-  Symbols:   129
+  Symbols:   128
   CStrings:  72
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ _accessibilityLocalizedString : 184 -> 200
~ _accessibilityNonLocalizedStringForKey : 244 -> 268
~ ___52+[AXPreferencesUIGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___52+[AXPreferencesUIGlue accessibilityInitializeBundle]_block_invoke_3 : 84 -> 88
~ ___52+[AXPreferencesUIGlue accessibilityInitializeBundle]_block_invoke_4 : 92 -> 100
~ +[PSUICellularPlanOptionTableCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[PSUITouchIDPasscodeControllerAccessibility highlightFingerprintSpecifier:] : 136 -> 140

```
