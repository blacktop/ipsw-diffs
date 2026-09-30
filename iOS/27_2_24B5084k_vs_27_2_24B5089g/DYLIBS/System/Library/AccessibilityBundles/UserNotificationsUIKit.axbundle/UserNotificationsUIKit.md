## UserNotificationsUIKit

> `/System/Library/AccessibilityBundles/UserNotificationsUIKit.axbundle/UserNotificationsUIKit`

```diff

-3050.3.0.0.0
-  __TEXT.__text: 0xda70
+3050.3.1.0.0
+  __TEXT.__text: 0xda94
   __TEXT.__objc_methlist: 0x1354
   __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x288
-  __TEXT.__cstring: 0x2916
-  __TEXT.__oslogstring: 0xb9
-  __TEXT.__unwind_info: 0x698
+  __TEXT.__gcc_except_tab: 0x274
+  __TEXT.__cstring: 0x2919
+  __TEXT.__oslogstring: 0xfd
+  __TEXT.__unwind_info: 0x690
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 423
-  Symbols:   1231
-  CStrings:  415
+  Symbols:   1230
+  CStrings:  416
 
Symbols:
+ -[NCNotificationListCellAccessibility _axNotificationContentLabel]
+ ___57-[NCNotificationListCellAccessibility accessibilityLabel]_block_invoke
+ _objc_msgSend$_axNotificationContentLabel
+ _objc_msgSend$_staticContentProviderLoadingIfNecessary
- -[NCNotificationListCellAccessibility _accessibilityOpenAction]
- GCC_except_table192
- ___63-[NCNotificationListCellAccessibility _accessibilityOpenAction]_block_invoke
- _objc_msgSend$_accessibilityOpenAction
- _objc_msgSend$defaultActionForNotificationListCell:
Functions:
~ +[NCNotificationListCellAccessibility _accessibilityPerformValidations:] : 1376 -> 1400
~ -[NCNotificationListCellAccessibility accessibilityActivate] : 556 -> 588
~ ___60-[NCNotificationListCellAccessibility accessibilityActivate]_block_invoke_2 : 16 -> 12
~ -[NCNotificationListCellAccessibility accessibilityLabel] : 976 -> 332
~ -[NCNotificationListCellAccessibility accessibilityIdentifier] -> ___57-[NCNotificationListCellAccessibility accessibilityLabel]_block_invoke : 108 -> 8
~ -[NCNotificationListCellAccessibility _accessibilityOpenAction] -> -[NCNotificationListCellAccessibility _axNotificationContentLabel] : 288 -> 976
~ ___63-[NCNotificationListCellAccessibility _accessibilityOpenAction]_block_invoke -> -[NCNotificationListCellAccessibility accessibilityIdentifier] : 68 -> 108
CStrings:
+ "Notification cell label empty on read; forcing static content setup"
+ "_staticContentProviderLoadingIfNecessary"
- "defaultActionForNotificationListCell:"
```
