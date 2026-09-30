## UserNotificationsSettings

> `/System/Library/PrivateFrameworks/UserNotificationsSettings.framework/Versions/A/UserNotificationsSettings`

### Sections with Same Size but Changed Content

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
-  __TEXT.__text: 0xa5dc
-  __TEXT.__objc_methlist: 0xd18
+717.0.0.0.0
+  __TEXT.__text: 0xa830
+  __TEXT.__objc_methlist: 0xd3c
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0xa1e
+  __TEXT.__cstring: 0xa1f
   __TEXT.__gcc_except_tab: 0x94
-  __TEXT.__oslogstring: 0xaba
-  __TEXT.__unwind_info: 0x368
+  __TEXT.__oslogstring: 0xaf9
+  __TEXT.__unwind_info: 0x360
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a0
+  __DATA_CONST.__objc_selrefs: 0x6b0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__got: 0x168
-  __AUTH_CONST.__const: 0x600
+  __AUTH_CONST.__const: 0x620
   __AUTH_CONST.__cfstring: 0x960
-  __AUTH_CONST.__objc_const: 0x1c58
+  __AUTH_CONST.__objc_const: 0x1c80
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x90
+  __DATA.__objc_ivar: 0x94
   __DATA.__data: 0x360
   __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__bss: 0x50

   - /System/Library/Frameworks/UserNotifications.framework/Versions/A/UserNotifications
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 325
-  Symbols:   789
-  CStrings:  142
+  Functions: 330
+  Symbols:   797
+  CStrings:  143
 
Symbols:
+ -[UNUserNotificationSettingsServiceConnection _queue_registerForSettingsUpdates]
+ -[UNUserNotificationSettingsServiceConnection registerForSettingsUpdates]
+ -[UNUserNotificationSettingsServiceConnection updateNotificationSourcesWithBundleIdentifiers:reply:]
+ -[UNUserNotificationSettingsServiceConnection updateNotificationSystemSettings:reply:]
+ GCC_except_table84
+ OBJC_IVAR_$_UNUserNotificationSettingsServiceConnection._registeredForSettingsUpdates
+ __80-[UNUserNotificationSettingsServiceConnection _queue_registerForSettingsUpdates]_block_invoke
+ ___73-[UNUserNotificationSettingsServiceConnection registerForSettingsUpdates]_block_invoke
+ ___80-[UNUserNotificationSettingsServiceConnection _queue_registerForSettingsUpdates]_block_invoke
+ _objc_msgSend$_queue_registerForSettingsUpdates
+ _objc_msgSend$registerForSettingsUpdates
- -[UNUserNotificationSettingsServiceConnection updateNotificationSourcesWithBundleIdentifiers:]
- -[UNUserNotificationSettingsServiceConnection updateNotificationSystemSettings:]
- GCC_except_table80
CStrings:
+ "Registering for settings updates failed with error: %{public}@"
```
