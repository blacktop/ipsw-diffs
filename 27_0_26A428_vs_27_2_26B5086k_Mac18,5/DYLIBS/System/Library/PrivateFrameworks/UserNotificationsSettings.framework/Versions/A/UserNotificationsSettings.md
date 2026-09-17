## UserNotificationsSettings

> `/System/Library/PrivateFrameworks/UserNotificationsSettings.framework/Versions/A/UserNotificationsSettings`

```diff

-720.0.1.0.0
-  __TEXT.__text: 0xa3ec
-  __TEXT.__objc_methlist: 0xd3c
+720.2.6.0.0
+  __TEXT.__text: 0xa928
+  __TEXT.__objc_methlist: 0xd58
   __TEXT.__const: 0x80
   __TEXT.__cstring: 0xa1f
   __TEXT.__gcc_except_tab: 0x94
-  __TEXT.__oslogstring: 0xaf9
-  __TEXT.__unwind_info: 0x4a0
+  __TEXT.__oslogstring: 0xbca
+  __TEXT.__unwind_info: 0x4c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b0
+  __DATA_CONST.__objc_selrefs: 0x6b8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__got: 0x168
-  __AUTH_CONST.__const: 0x620
+  __AUTH_CONST.__const: 0x650
   __AUTH_CONST.__cfstring: 0x960
-  __AUTH_CONST.__objc_const: 0x1c80
+  __AUTH_CONST.__objc_const: 0x1c88
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x94
   __DATA.__data: 0x360

   - /System/Library/Frameworks/UserNotifications.framework/Versions/A/UserNotifications
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 330
-  Symbols:   797
-  CStrings:  143
+  Functions: 337
+  Symbols:   806
+  CStrings:  146
 
Symbols:
+ -[UNNotificationSettingsCenter copyNotificationSettingsFromSourceIdentifier:toSourceIdentifier:withCompletionHandler:]
+ -[UNUserNotificationSettingsServiceConnection copyNotificationSettingsFromSourceIdentifier:toSourceIdentifier:withCompletionHandler:]
+ GCC_except_table89
+ __133-[UNUserNotificationSettingsServiceConnection copyNotificationSettingsFromSourceIdentifier:toSourceIdentifier:withCompletionHandler:]_block_invoke
+ __133-[UNUserNotificationSettingsServiceConnection copyNotificationSettingsFromSourceIdentifier:toSourceIdentifier:withCompletionHandler:]_block_invoke_2
+ ___133-[UNUserNotificationSettingsServiceConnection copyNotificationSettingsFromSourceIdentifier:toSourceIdentifier:withCompletionHandler:]_block_invoke
+ ___133-[UNUserNotificationSettingsServiceConnection copyNotificationSettingsFromSourceIdentifier:toSourceIdentifier:withCompletionHandler:]_block_invoke_2
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56b
+ _objc_msgSend$copyNotificationSettingsFromSourceIdentifier:toSourceIdentifier:withCompletionHandler:
- GCC_except_table84
CStrings:
+ "Copy notification settings (sync) failed with error: %{public}@"
+ "Copy notification settings from source %{public}@ to %{public}@ (sync)"
+ "Copy notification settings to %{public}@ completed with success: %{BOOL}d"
```
