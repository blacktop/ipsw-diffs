## UserNotificationsUIKit

> `/System/Library/AccessibilityBundles/UserNotificationsUIKit.axbundle/UserNotificationsUIKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-3042.0.0.0.0
-  __TEXT.__text: 0xde68
+3045.0.0.0.0
+  __TEXT.__text: 0xdf5c
   __TEXT.__objc_methlist: 0x1354
   __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0x274
-  __TEXT.__cstring: 0x28ae
+  __TEXT.__cstring: 0x28d5
   __TEXT.__oslogstring: 0xb9
   __TEXT.__unwind_info: 0x5c8
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__got: 0x170
   __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__cfstring: 0x2ea0
+  __AUTH_CONST.__cfstring: 0x2ec0
   __AUTH_CONST.__objc_const: 0x2b00
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 420
-  Symbols:   1225
-  CStrings:  413
+  Functions: 421
+  Symbols:   1227
+  CStrings:  414
 
Symbols:
+ GCC_except_table235
+ GCC_except_table237
+ GCC_except_table316
+ GCC_except_table319
+ GCC_except_table322
+ GCC_except_table342
+ GCC_except_table347
+ GCC_except_table355
+ GCC_except_table357
+ ___60-[NCNotificationListCellAccessibility accessibilityActivate]_block_invoke_3
+ _objc_msgSend$_accessibilityOpenAction
- GCC_except_table234
- GCC_except_table236
- GCC_except_table315
- GCC_except_table318
- GCC_except_table321
- GCC_except_table341
- GCC_except_table346
- GCC_except_table354
- GCC_except_table356
Functions:
~ +[NCNotificationListCellAccessibility _accessibilityPerformValidations:] : 1300 -> 1380
~ -[NCNotificationListCellAccessibility accessibilityActivate] : 416 -> 556
~ ___60-[NCNotificationListCellAccessibility accessibilityActivate]_block_invoke_2 : 12 -> 16
+ ___60-[NCNotificationListCellAccessibility accessibilityActivate]_block_invoke_3
CStrings:
+ "handleTapOnNotificationViewController:"
```
