## UserNotificationsSettings

> `/System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-713.0.0.0.0
-  __TEXT.__text: 0x6d10
-  __TEXT.__objc_methlist: 0xb60
+717.0.0.0.0
+  __TEXT.__text: 0x6f4c
+  __TEXT.__objc_methlist: 0xb84
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x766
+  __TEXT.__cstring: 0x767
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__oslogstring: 0x776
+  __TEXT.__oslogstring: 0x7b5
   __TEXT.__unwind_info: 0x2a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x578
+  __DATA_CONST.__objc_selrefs: 0x588
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__got: 0x100
-  __AUTH_CONST.__const: 0x1a0
+  __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0x680
-  __AUTH_CONST.__objc_const: 0x1b58
+  __AUTH_CONST.__objc_const: 0x1b80
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x88
+  __DATA.__objc_ivar: 0x8c
   __DATA.__data: 0x360
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__bss: 0x40

   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 235
-  Symbols:   627
-  CStrings:  96
+  Functions: 240
+  Symbols:   634
+  CStrings:  97
 
Symbols:
+ -[UNUserNotificationSettingsServiceConnection _queue_registerForSettingsUpdates]
+ -[UNUserNotificationSettingsServiceConnection registerForSettingsUpdates]
+ -[UNUserNotificationSettingsServiceConnection updateNotificationSourcesWithBundleIdentifiers:reply:]
+ -[UNUserNotificationSettingsServiceConnection updateNotificationSystemSettings:reply:]
+ GCC_except_table65
+ _OBJC_IVAR_$_UNUserNotificationSettingsServiceConnection._registeredForSettingsUpdates
+ ___73-[UNUserNotificationSettingsServiceConnection registerForSettingsUpdates]_block_invoke
+ ___80-[UNUserNotificationSettingsServiceConnection _queue_registerForSettingsUpdates]_block_invoke
+ _objc_msgSend$_queue_registerForSettingsUpdates
+ _objc_msgSend$registerForSettingsUpdates
- -[UNUserNotificationSettingsServiceConnection updateNotificationSourcesWithBundleIdentifiers:]
- -[UNUserNotificationSettingsServiceConnection updateNotificationSystemSettings:]
- GCC_except_table61
CStrings:
+ "Registering for settings updates failed with error: %{public}@"
```
