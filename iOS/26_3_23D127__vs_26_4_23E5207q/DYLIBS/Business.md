## Business

> `/System/Library/AccessibilityBundles/Business.axbundle/Business`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xb74
-  __TEXT.__auth_stubs: 0x180
+3005.16.0.0.0
+  __TEXT.__text: 0xbf0
+  __TEXT.__auth_stubs: 0x170
   __TEXT.__objc_methlist: 0x29c
   __TEXT.__cstring: 0x329
   __TEXT.__unwind_info: 0xd8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xe8
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xc8
+  __AUTH_CONST.__auth_got: 0xc0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x460
   __AUTH_CONST.__objc_const: 0x8b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A1BCEE47-C99E-36B9-B0CE-0B6B7D1E1F01
+  UUID: A8750210-1CB5-3883-ACEA-6B55F8DE54C2
   Functions: 45
-  Symbols:   236
+  Symbols:   235
   CStrings:  128
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXBusinessGlue accessibilityInitializeBundle] : 148 -> 152
~ ___47+[AXBusinessGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___47+[AXBusinessGlue accessibilityInitializeBundle]_block_invoke_3 : 192 -> 200
~ _accessibilityLocalizedString : 176 -> 184
~ -[ApplePayBubbleViewAccessibility accessibilityLabel] : 148 -> 160
~ +[IMBBubbleViewAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[IMBTimeslotsContainerViewAccessibility accessibilityElements] : 160 -> 168
~ +[ListPickerTableViewCellAccessibility _accessibilityPerformValidations:] : 188 -> 200
~ -[ListPickerTableViewCellAccessibility accessibilityTraits] : 376 -> 392
~ +[IMBDateTableViewCellAccessibility _accessibilityPerformValidations:] : 212 -> 224
~ -[IMBDateTableViewCellAccessibility accessibilityElements] : 356 -> 384

```
