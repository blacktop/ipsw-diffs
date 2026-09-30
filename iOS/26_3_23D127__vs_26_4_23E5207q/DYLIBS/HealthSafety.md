## HealthSafety

> `/System/Library/AccessibilityBundles/HealthSafety.axbundle/HealthSafety`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x278
+3005.16.0.0.0
+  __TEXT.__text: 0x290
   __TEXT.__auth_stubs: 0xb0
   __TEXT.__objc_methlist: 0xb8
   __TEXT.__cstring: 0x162

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A4E4D210-1C7A-3775-BBE0-74B822D3A808
+  UUID: B81CBD79-13DB-3416-BAC8-0F8983776210
   Functions: 15
   Symbols:   92
   CStrings:  47
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
Functions:
~ +[AXHealthSafetyGlue accessibilityInitializeBundle] : 148 -> 152
~ ___51+[AXHealthSafetyGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___51+[AXHealthSafetyGlue accessibilityInitializeBundle]_block_invoke_3 : 92 -> 100
~ _accessibilityLocalizedString : 176 -> 184

```
