## UserNotificationsSettings

> `/System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings`

```diff

-640.2.11.0.0
-  __TEXT.__text: 0x6b88
-  __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_methlist: 0xa70
+640.3.14.0.0
+  __TEXT.__text: 0x7260
+  __TEXT.__auth_stubs: 0x3b0
+  __TEXT.__objc_methlist: 0xa90
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x688
+  __TEXT.__cstring: 0x702
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__oslogstring: 0x69e
-  __TEXT.__unwind_info: 0x268
+  __TEXT.__oslogstring: 0x776
+  __TEXT.__unwind_info: 0x280
   __TEXT.__objc_classname: 0x22b
-  __TEXT.__objc_methname: 0x1bfb
-  __TEXT.__objc_methtype: 0x672
-  __TEXT.__objc_stubs: 0xdc0
+  __TEXT.__objc_methname: 0x1c6b
+  __TEXT.__objc_methtype: 0x6ad
+  __TEXT.__objc_stubs: 0xe00
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x350
+  __DATA_CONST.__const: 0x400
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x558
+  __DATA_CONST.__objc_selrefs: 0x568
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x1e0
+  __AUTH_CONST.__auth_got: 0x1e8
   __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__cfstring: 0x600
+  __AUTH_CONST.__cfstring: 0x640
   __AUTH_CONST.__objc_const: 0x1ab0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x88

   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EAD933BA-AF5C-3919-BC5A-E44BDDB01540
-  Functions: 225
-  Symbols:   909
-  CStrings:  463
+  UUID: 3D089664-3192-31BA-A97A-1961B4D3A109
+  Functions: 231
+  Symbols:   934
+  CStrings:  474
 
Symbols:
+ -[UNNotificationSettingsCenter notificationSourcesWithFilter:sort:maxCount:completionHandler:]
+ -[UNUserNotificationSettingsServiceConnection notificationSourcesWithFilter:sort:maxCount:completionHandler:]
+ GCC_except_table61
+ _UNNotificationSourceSortOrderDefault
+ _UNNotificationSourceSortOrderWeeklyNotificationAverage
+ ___109-[UNUserNotificationSettingsServiceConnection notificationSourcesWithFilter:sort:maxCount:completionHandler:]_block_invoke
+ ___109-[UNUserNotificationSettingsServiceConnection notificationSourcesWithFilter:sort:maxCount:completionHandler:]_block_invoke.13
+ ___109-[UNUserNotificationSettingsServiceConnection notificationSourcesWithFilter:sort:maxCount:completionHandler:]_block_invoke.13.cold.1
+ ___109-[UNUserNotificationSettingsServiceConnection notificationSourcesWithFilter:sort:maxCount:completionHandler:]_block_invoke_2
+ ___109-[UNUserNotificationSettingsServiceConnection notificationSourcesWithFilter:sort:maxCount:completionHandler:]_block_invoke_2.cold.1
+ ___120-[UNUserNotificationSettingsServiceConnection revokeAuthorizationForNotificationSourceIdentifier:withCompletionHandler:]_block_invoke.20
+ ___120-[UNUserNotificationSettingsServiceConnection revokeAuthorizationForNotificationSourceIdentifier:withCompletionHandler:]_block_invoke.20.cold.1
+ ___126-[UNUserNotificationSettingsServiceConnection authorizationWithOptions:forNotificationSourceIdentifier:withCompletionHandler:]_block_invoke.16
+ ___126-[UNUserNotificationSettingsServiceConnection authorizationWithOptions:forNotificationSourceIdentifier:withCompletionHandler:]_block_invoke.16.cold.1
+ ___65-[UNUserNotificationSettingsServiceConnection setSourceSettings:]_block_invoke.25
+ ___73-[UNUserNotificationSettingsServiceConnection notificationSystemSettings]_block_invoke.32
+ ___77-[UNUserNotificationSettingsServiceConnection notificationSourcesWithFilter:]_block_invoke.10.cold.1
+ ___87-[UNUserNotificationSettingsServiceConnection notificationSettingsForSourceIdentifier:]_block_invoke.23
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32r_e29_v24?0"NSArray"8"NSError"16lr32l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
+ ___block_literal_global.15
+ ___block_literal_global.22
+ ___block_literal_global.27
+ ___block_literal_global.29
+ ___block_literal_global.31
+ ___block_literal_global.35
+ ___block_literal_global.37
+ _objc_msgSend$getNotificationSourcesWithFilter:sort:maxCount:completionHandler:
+ _objc_msgSend$notificationSourcesWithFilter:sort:maxCount:completionHandler:
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_retain_x5
- GCC_except_table57
- ___120-[UNUserNotificationSettingsServiceConnection revokeAuthorizationForNotificationSourceIdentifier:withCompletionHandler:]_block_invoke.17
- ___120-[UNUserNotificationSettingsServiceConnection revokeAuthorizationForNotificationSourceIdentifier:withCompletionHandler:]_block_invoke.17.cold.1
- ___126-[UNUserNotificationSettingsServiceConnection authorizationWithOptions:forNotificationSourceIdentifier:withCompletionHandler:]_block_invoke.13
- ___126-[UNUserNotificationSettingsServiceConnection authorizationWithOptions:forNotificationSourceIdentifier:withCompletionHandler:]_block_invoke.13.cold.1
- ___65-[UNUserNotificationSettingsServiceConnection setSourceSettings:]_block_invoke.22
- ___73-[UNUserNotificationSettingsServiceConnection notificationSystemSettings]_block_invoke.29
- ___87-[UNUserNotificationSettingsServiceConnection notificationSettingsForSourceIdentifier:]_block_invoke.20
- ___block_literal_global.12
- ___block_literal_global.16
- ___block_literal_global.24
- ___block_literal_global.26
- ___block_literal_global.28
- ___block_literal_global.32
- ___block_literal_global.34
- _objc_msgSend$getNotificationSourcesWithFilter:completionHandler:
CStrings:
+ "Getting notification sources with filter (async) failed with error: %{public}@"
+ "Getting notification sources with filter, sort order: %{public}@, max count: %@ (async)"
+ "Got notification sources with filter: %{public}@"
+ "UNNotificationSourceSortOrderDefault"
+ "UNNotificationSourceSortOrderWeeklyNotificationAverage"
+ "getNotificationSourcesWithFilter:sort:maxCount:completionHandler:"
+ "notificationSourcesWithFilter:sort:maxCount:completionHandler:"
+ "remoteObjectProxyWithErrorHandler:"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSNumber\"32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@16@24@32@?40"
- "getNotificationSourcesWithFilter:completionHandler:"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSSet\">24"

```
