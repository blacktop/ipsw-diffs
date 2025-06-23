## UserNotificationsSettings

> `/System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings`

```diff

-616.0.1.0.0
-  __TEXT.__text: 0x5cb0
-  __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0x9fc
+623.0.0.0.0
+  __TEXT.__text: 0x6254
+  __TEXT.__auth_stubs: 0x390
+  __TEXT.__objc_methlist: 0xa28
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x609
+  __TEXT.__cstring: 0x666
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__oslogstring: 0x52a
-  __TEXT.__unwind_info: 0x230
+  __TEXT.__oslogstring: 0x5a0
+  __TEXT.__unwind_info: 0x248
   __TEXT.__objc_classname: 0x22b
-  __TEXT.__objc_methname: 0x1a4d
-  __TEXT.__objc_methtype: 0x5c2
-  __TEXT.__objc_stubs: 0xcc0
-  __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x2a8
+  __TEXT.__objc_methname: 0x1b60
+  __TEXT.__objc_methtype: 0x60d
+  __TEXT.__objc_stubs: 0xd60
+  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__const: 0x2d0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x500
+  __DATA_CONST.__objc_selrefs: 0x538
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x1d0
-  __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x5a0
-  __AUTH_CONST.__objc_const: 0x1a98
+  __AUTH_CONST.__auth_got: 0x1d8
+  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__cfstring: 0x5e0
+  __AUTH_CONST.__objc_const: 0x1aa0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x88
   __DATA.__data: 0x300

   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 99885C2D-65F4-3EF2-A1E0-BB89E2A18DB0
-  Functions: 206
-  Symbols:   848
-  CStrings:  434
+  UUID: 7435B079-B356-3A28-B326-359801C4269F
+  Functions: 213
+  Symbols:   873
+  CStrings:  449
 
Symbols:
+ -[UNMutableNotificationSystemSettings setPrioritizationSetting:]
+ -[UNNotificationSettingsCenter mutateNotificationSettingsForSourceIdentifier:mutatingBlock:error:]
+ -[UNUserNotificationSettingsServiceConnection notificationSettingsForSourceIdentifier:]
+ GCC_except_table49
+ _NSCocoaErrorDomain
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSError
+ ___73-[UNUserNotificationSettingsServiceConnection notificationSystemSettings]_block_invoke.25
+ ___87-[UNUserNotificationSettingsServiceConnection notificationSettingsForSourceIdentifier:]_block_invoke
+ ___87-[UNUserNotificationSettingsServiceConnection notificationSettingsForSourceIdentifier:]_block_invoke.17
+ ___87-[UNUserNotificationSettingsServiceConnection notificationSettingsForSourceIdentifier:]_block_invoke_2
+ ___87-[UNUserNotificationSettingsServiceConnection notificationSettingsForSourceIdentifier:]_block_invoke_2.cold.1
+ ___block_descriptor_40_e8_32r_e32_v16?0"UNNotificationSettings"8lr32l8
+ ___block_literal_global.22
+ ___block_literal_global.28
+ ___block_literal_global.30
+ _objc_autorelease
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$getNotificationSettingsForSourceIdentifier:withCompletionHandler:
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$notificationSettingsForSourceIdentifier:
- GCC_except_table45
- ___73-[UNUserNotificationSettingsServiceConnection notificationSystemSettings]_block_invoke.21
- ___block_literal_global.18
- ___block_literal_global.26
CStrings:
+ "B40@0:8@16@?24o^@32"
+ "Get notification settings (sync) failed with error: %{public}@"
+ "Get notification settings for source %{public}@ (sync)"
+ "dictionaryWithObjects:forKeys:count:"
+ "errorWithDomain:code:userInfo:"
+ "getNotificationSettingsForSourceIdentifier:withCompletionHandler:"
+ "mutableCopy"
+ "mutateNotificationSettingsForSourceIdentifier:mutatingBlock:error:"
+ "mutatingBlock cannot be nil"
+ "notificationSettingsForSourceIdentifier:"
+ "setPrioritizationSetting:"
+ "settings object is nil for '%@'"
+ "v16@?0@\"UNNotificationSettings\"8"
+ "v32@0:8@\"NSString\"16@?<v@?@\"UNNotificationSettings\">24"
- "Tq,N"

```
