## NotificationsSettings

> `/System/Library/AccessibilityBundles/NotificationsSettings.axbundle/NotificationsSettings`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x83c
-  __TEXT.__auth_stubs: 0x150
+3005.16.0.0.0
+  __TEXT.__text: 0x88c
+  __TEXT.__auth_stubs: 0x140
   __TEXT.__objc_methlist: 0x180
   __TEXT.__cstring: 0x25a
   __TEXT.__const: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xd0
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xb8
+  __AUTH_CONST.__auth_got: 0xb0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x320
   __AUTH_CONST.__objc_const: 0x510

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B1A56B46-B08C-3DC9-9E0C-F028B640BCA8
+  UUID: C89D62EC-8DC1-30ED-ABA3-15E3F2127C79
   Functions: 31
-  Symbols:   169
+  Symbols:   168
   CStrings:  98
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x21
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ _accessibilityLocalizedString : 176 -> 184
~ +[AXNotificationSettingsGlue accessibilityInitializeBundle] : 100 -> 104
~ ___59+[AXNotificationSettingsGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___59+[AXNotificationSettingsGlue accessibilityInitializeBundle]_block_invoke_3 : 132 -> 140
~ +[NCNotificationListDisplayStyleSelectionViewAccessibility _accessibilityPerformValidations:] : 160 -> 172
~ -[NCNotificationListDisplayStyleSelectionViewAccessibility accessibilityLabel] : 120 -> 128
~ +[AlertDeliveryLocationViewAccessibility _accessibilityPerformValidations:] : 160 -> 168
~ -[AlertDeliveryLocationViewAccessibility accessibilityIdentifier] : 84 -> 92
~ +[NotificationCellAccessibility _accessibilityPerformValidations:] : 128 -> 136
~ -[NotificationCellAccessibility accessibilityTraits] : 424 -> 432
~ ___52-[NotificationCellAccessibility accessibilityTraits]_block_invoke : 80 -> 84

```
