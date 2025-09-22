## UserNotificationsSettings

> `/System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings`

```diff

-640.0.0.0.0
-  __TEXT.__text: 0x66d8
+640.1.9.100.0
+  __TEXT.__text: 0x6b88
   __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_methlist: 0xa54
+  __TEXT.__objc_methlist: 0xa70
   __TEXT.__const: 0x80
   __TEXT.__cstring: 0x688
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__oslogstring: 0x5ec
-  __TEXT.__unwind_info: 0x260
+  __TEXT.__oslogstring: 0x69e
+  __TEXT.__unwind_info: 0x268
   __TEXT.__objc_classname: 0x22b
-  __TEXT.__objc_methname: 0x1bb1
-  __TEXT.__objc_methtype: 0x649
-  __TEXT.__objc_stubs: 0xda0
+  __TEXT.__objc_methname: 0x1bfb
+  __TEXT.__objc_methtype: 0x672
+  __TEXT.__objc_stubs: 0xdc0
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x328
+  __DATA_CONST.__const: 0x350
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x550
+  __DATA_CONST.__objc_selrefs: 0x558
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x48
   __AUTH_CONST.__auth_got: 0x1e0
-  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__cfstring: 0x600
-  __AUTH_CONST.__objc_const: 0x1aa8
+  __AUTH_CONST.__objc_const: 0x1ab0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x88
   __DATA.__data: 0x300

   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F21B0936-24D2-390C-81E2-BBCB579A6894
-  Functions: 219
-  Symbols:   892
-  CStrings:  458
+  UUID: D6A98672-D51B-37C2-88A8-23F659AC7DBD
+  Functions: 225
+  Symbols:   909
+  CStrings:  463
 
Symbols:
+ -[UNNotificationSettingsCenter revokeAuthorizationForNotificationSourceIdentifier:withCompletionHandler:]
+ -[UNUserNotificationSettingsServiceConnection revokeAuthorizationForNotificationSourceIdentifier:withCompletionHandler:]
+ GCC_except_table57
+ ___120-[UNUserNotificationSettingsServiceConnection revokeAuthorizationForNotificationSourceIdentifier:withCompletionHandler:]_block_invoke
+ ___120-[UNUserNotificationSettingsServiceConnection revokeAuthorizationForNotificationSourceIdentifier:withCompletionHandler:]_block_invoke.17
+ ___120-[UNUserNotificationSettingsServiceConnection revokeAuthorizationForNotificationSourceIdentifier:withCompletionHandler:]_block_invoke.17.cold.1
+ ___120-[UNUserNotificationSettingsServiceConnection revokeAuthorizationForNotificationSourceIdentifier:withCompletionHandler:]_block_invoke_2
+ ___120-[UNUserNotificationSettingsServiceConnection revokeAuthorizationForNotificationSourceIdentifier:withCompletionHandler:]_block_invoke_2.cold.1
+ ___65-[UNUserNotificationSettingsServiceConnection setSourceSettings:]_block_invoke.22
+ ___73-[UNUserNotificationSettingsServiceConnection notificationSystemSettings]_block_invoke.29
+ ___87-[UNUserNotificationSettingsServiceConnection notificationSettingsForSourceIdentifier:]_block_invoke.20
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.19
+ ___block_literal_global.24
+ ___block_literal_global.26
+ ___block_literal_global.28
+ ___block_literal_global.32
+ ___block_literal_global.34
+ _objc_msgSend$revokeAuthorizationForNotificationSourceIdentifier:withCompletionHandler:
- GCC_except_table53
- ___65-[UNUserNotificationSettingsServiceConnection setSourceSettings:]_block_invoke.19
- ___73-[UNUserNotificationSettingsServiceConnection notificationSystemSettings]_block_invoke.26
- ___87-[UNUserNotificationSettingsServiceConnection notificationSettingsForSourceIdentifier:]_block_invoke.17
- ___block_literal_global.21
- ___block_literal_global.23
- ___block_literal_global.25
- ___block_literal_global.29
- ___block_literal_global.31
CStrings:
+ "Revoke authorization (sync) failed with error: %{public}@"
+ "Revoke authorization for %{public}@ completed with status granted: %d"
+ "Revoke authorization for source %{public}@ (sync)"
+ "revokeAuthorizationForNotificationSourceIdentifier:withCompletionHandler:"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"

```
