## UserNotificationsSettings

> `/System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings`

```diff

-720.0.0.0.0
-  __TEXT.__text: 0x6c94
-  __TEXT.__objc_methlist: 0xb84
+720.2.6.0.0
+  __TEXT.__text: 0x7138
+  __TEXT.__objc_methlist: 0xba0
   __TEXT.__const: 0x80
   __TEXT.__cstring: 0x767
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__oslogstring: 0x7b5
-  __TEXT.__unwind_info: 0x360
+  __TEXT.__oslogstring: 0x886
+  __TEXT.__unwind_info: 0x378
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x410
+  __DATA_CONST.__const: 0x438
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x588
+  __DATA_CONST.__objc_selrefs: 0x590
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__got: 0x100
   __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0x680
-  __AUTH_CONST.__objc_const: 0x1b80
+  __AUTH_CONST.__objc_const: 0x1b88
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x8c
   __DATA.__data: 0x360

   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 240
-  Symbols:   634
-  CStrings:  97
+  Functions: 246
+  Symbols:   640
+  CStrings:  100
 
Symbols:
+ -[UNNotificationSettingsCenter copyNotificationSettingsFromSourceIdentifier:toSourceIdentifier:withCompletionHandler:]
+ -[UNUserNotificationSettingsServiceConnection copyNotificationSettingsFromSourceIdentifier:toSourceIdentifier:withCompletionHandler:]
+ GCC_except_table69
+ ___133-[UNUserNotificationSettingsServiceConnection copyNotificationSettingsFromSourceIdentifier:toSourceIdentifier:withCompletionHandler:]_block_invoke
+ ___133-[UNUserNotificationSettingsServiceConnection copyNotificationSettingsFromSourceIdentifier:toSourceIdentifier:withCompletionHandler:]_block_invoke_2
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ _objc_msgSend$copyNotificationSettingsFromSourceIdentifier:toSourceIdentifier:withCompletionHandler:
- GCC_except_table65
CStrings:
+ "Copy notification settings (sync) failed with error: %{public}@"
+ "Copy notification settings from source %{public}@ to %{public}@ (sync)"
+ "Copy notification settings to %{public}@ completed with success: %{BOOL}d"
```
