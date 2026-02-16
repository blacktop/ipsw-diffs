## RecentsAvocado

> `/System/Library/AccessibilityBundles/RecentsAvocado.axbundle/RecentsAvocado`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x46c
-  __TEXT.__auth_stubs: 0x140
+3005.16.0.0.0
+  __TEXT.__text: 0x4b4
+  __TEXT.__auth_stubs: 0x130
   __TEXT.__objc_methlist: 0x80
   __TEXT.__cstring: 0x159
   __TEXT.__unwind_info: 0x88

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xb8
-  __AUTH_CONST.__auth_got: 0xa8
+  __AUTH_CONST.__auth_got: 0xa0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x1a0
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 687A8F21-E3A9-387B-9E90-6A7900BC7D9C
+  UUID: 8CA8820E-E6DE-3603-B6BE-D8A9C2D905B6
   Functions: 12
-  Symbols:   92
+  Symbols:   91
   CStrings:  61
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXRecentsAvocadoGlue accessibilityInitializeBundle] : 148 -> 152
~ ___53+[AXRecentsAvocadoGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___53+[AXRecentsAvocadoGlue accessibilityInitializeBundle]_block_invoke_3 : 92 -> 100
~ _accessibilityLocalizedString : 176 -> 184
~ +[RecentItemCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[RecentItemCellAccessibility accessibilityLabel] : 296 -> 324
~ -[RecentItemCellAccessibility accessibilityUserInputLabels] : 112 -> 120

```
