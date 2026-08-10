## UserNotificationsUIKit

> `/System/Library/AccessibilityBundles/UserNotificationsUIKit.axbundle/UserNotificationsUIKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
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

-3045.0.0.0.0
-  __TEXT.__text: 0xdf5c
+3048.0.0.0.0
+  __TEXT.__text: 0xe0e8
   __TEXT.__objc_methlist: 0x1354
   __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x274
-  __TEXT.__cstring: 0x28d5
+  __TEXT.__gcc_except_tab: 0x288
+  __TEXT.__cstring: 0x2916
   __TEXT.__oslogstring: 0xb9
-  __TEXT.__unwind_info: 0x5c8
+  __TEXT.__unwind_info: 0x5d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__got: 0x170
   __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__cfstring: 0x2ec0
+  __AUTH_CONST.__cfstring: 0x2ee0
   __AUTH_CONST.__objc_const: 0x2b00
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 421
-  Symbols:   1227
-  CStrings:  414
+  Functions: 423
+  Symbols:   1232
+  CStrings:  415
 
Symbols:
+ GCC_except_table190
+ GCC_except_table192
+ GCC_except_table199
+ GCC_except_table236
+ GCC_except_table238
+ GCC_except_table317
+ GCC_except_table320
+ GCC_except_table323
+ GCC_except_table343
+ GCC_except_table348
+ GCC_except_table356
+ GCC_except_table358
+ GCC_except_table380
+ ___65-[NCNotificationListCellAccessibility axCustomActionsForActions:]_block_invoke_3
+ ___68-[NCNotificationViewControllerAccessibility _axAnnounceNotification]_block_invoke
+ _objc_msgSend$_axHandleAnnouncementFinished
+ _objc_msgSend$_axHasFinishedAnnouncement
- GCC_except_table189
- GCC_except_table191
- GCC_except_table198
- GCC_except_table235
- GCC_except_table237
- GCC_except_table316
- GCC_except_table319
- GCC_except_table322
- GCC_except_table342
- GCC_except_table347
- GCC_except_table355
- GCC_except_table357
Functions:
~ +[NCNotificationListCellAccessibility _accessibilityPerformValidations:] : 1380 -> 1388
~ ___65-[NCNotificationListCellAccessibility axCustomActionsForActions:]_block_invoke_2 : 132 -> 236
+ ___65-[NCNotificationListCellAccessibility axCustomActionsForActions:]_block_invoke_3
~ -[NCNotificationViewControllerAccessibility _axAnnounceNotification] : 440 -> 592
+ ___68-[NCNotificationViewControllerAccessibility _axAnnounceNotification]_block_invoke
CStrings:
+ "Notification announcement finish never arrived; releasing banner"
```
