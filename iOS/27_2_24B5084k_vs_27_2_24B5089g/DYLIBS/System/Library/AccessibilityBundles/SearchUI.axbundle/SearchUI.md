## SearchUI

> `/System/Library/AccessibilityBundles/SearchUI.axbundle/SearchUI`

```diff

-3050.3.0.0.0
-  __TEXT.__text: 0x9bcc
-  __TEXT.__objc_methlist: 0xf64
+3050.3.1.0.0
+  __TEXT.__text: 0x9ccc
+  __TEXT.__objc_methlist: 0xf74
   __TEXT.__const: 0x28
   __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__cstring: 0x1a39
+  __TEXT.__cstring: 0x1a83
   __TEXT.__oslogstring: 0xf
-  __TEXT.__unwind_info: 0x4b0
+  __TEXT.__unwind_info: 0x4b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x350
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x568
+  __DATA_CONST.__objc_selrefs: 0x578
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__got: 0x178
   __AUTH_CONST.__const: 0x440
-  __AUTH_CONST.__cfstring: 0x2440
+  __AUTH_CONST.__cfstring: 0x24c0
   __AUTH_CONST.__objc_const: 0x27c8
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 321
-  Symbols:   995
-  CStrings:  307
+  Functions: 322
+  Symbols:   998
+  CStrings:  311
 
Symbols:
+ -[SearchUIButtonItemViewAccessibility _accessibilityIsCopyButtonInCopiedState]
+ GCC_except_table112
+ GCC_except_table82
+ GCC_except_table93
+ _objc_msgSend$_accessibilityIsCopyButtonInCopiedState
+ _objc_msgSend$safeIntegerForKey:
- GCC_except_table111
- GCC_except_table81
- GCC_except_table92
Functions:
~ +[SearchUIButtonItemViewAccessibility _accessibilityPerformValidations:] : 180 -> 264
~ -[SearchUIButtonItemViewAccessibility accessibilityLabel] : 228 -> 260
+ -[SearchUIButtonItemViewAccessibility _accessibilityIsCopyButtonInCopiedState]
CStrings:
+ "SearchUIButtonItem"
+ "SearchUICopyButtonItem"
+ "copy.button.copied.label"
+ "status"
```
