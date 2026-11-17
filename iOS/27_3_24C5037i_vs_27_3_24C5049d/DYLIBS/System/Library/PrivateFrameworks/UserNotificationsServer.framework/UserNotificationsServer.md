## UserNotificationsServer

> `/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer`

```diff

-720.3.6.0.0
-  __TEXT.__text: 0x3ba00
-  __TEXT.__objc_methlist: 0x2504
-  __TEXT.__const: 0x504
-  __TEXT.__gcc_except_tab: 0x654
-  __TEXT.__cstring: 0x1788
-  __TEXT.__oslogstring: 0x6985
+720.3.13.0.0
+  __TEXT.__text: 0x3bdf0
+  __TEXT.__objc_methlist: 0x250c
+  __TEXT.__const: 0x514
+  __TEXT.__gcc_except_tab: 0x65c
+  __TEXT.__cstring: 0x17a8
+  __TEXT.__oslogstring: 0x6a45
   __TEXT.__constg_swiftt: 0x278
   __TEXT.__swift5_typeref: 0x43c
   __TEXT.__swift5_capture: 0x12c

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x1218
+  __TEXT.__unwind_info: 0x1228
   __TEXT.__eh_frame: 0x270
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c30
+  __DATA_CONST.__objc_selrefs: 0x2c38
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x988
+  __DATA_CONST.__got: 0x998
   __AUTH_CONST.__const: 0x778
-  __AUTH_CONST.__cfstring: 0xec0
+  __AUTH_CONST.__cfstring: 0xee0
   __AUTH_CONST.__objc_const: 0x5f30
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0xa38

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1148
-  Symbols:   2049
-  CStrings:  538
+  Functions: 1151
+  Symbols:   2054
+  CStrings:  541
 
Symbols:
+ -[UNSDefaultDataProviderFactory _queue_setCriticalAlertAuthorization:forNotificationSourceDescription:settingSource:completionHandler:]
+ -[UNSDefaultDataProviderFactory _queue_setSectionInfo:forBundleIdentifier:settingSource:]
+ -[UNSDefaultDataProviderFactory _queue_updateSettingsWithAuthorizationStatus:options:scheduledDeliveryEnabled:expirationDate:lastUserGrantDate:forNotificationSourceDescription:settingSource:completionHandler:]
+ -[UNSDefaultDataProviderFactory _queue_updateSettingsWithAuthorizationStatus:options:scheduledDeliveryEnabled:forNotificationSourceDescription:settingSource:completionHandler:]
+ -[UNSDefaultDataProviderFactory requestAuthorizationStatus:withOptions:scheduledDeliveryEnabled:expirationDate:lastUserGrantDate:forNotificationSourceDescription:settingSource:completionHandler:]
+ -[UNSDefaultDataProviderFactory requestAuthorizationStatus:withOptions:scheduledDeliveryEnabled:forNotificationSourceDescription:settingSource:completionHandler:]
+ -[UNSDefaultDataProviderFactory setCriticalAlertAuthorization:forNotificationSourceDescription:settingSource:completionHandler:]
+ -[UNSDefaultDataProviderFactory updateAuthorizationWithOptions:scheduledDeliveryEnabled:forNotificationSourceDescription:settingSource:completionHandler:]
+ -[UNSNotificationAuthorizationService _queue_requestAuthorizationWithOptions:requestedOptions:forNotificationSourceDescription:withExpirationDate:completionHandler:]
+ GCC_except_table40
+ GCC_except_table43
+ _BBBulletinContentTypeActiveCall
+ _BBSettingSourceFromUNSSettingSource
+ __UNNotificationContentTypeActiveCall
+ ___128-[UNSDefaultDataProviderFactory setCriticalAlertAuthorization:forNotificationSourceDescription:settingSource:completionHandler:]_block_invoke
+ ___128-[UNSDefaultDataProviderFactory setCriticalAlertAuthorization:forNotificationSourceDescription:settingSource:completionHandler:]_block_invoke_2
+ ___135-[UNSDefaultDataProviderFactory _queue_setCriticalAlertAuthorization:forNotificationSourceDescription:settingSource:completionHandler:]_block_invoke
+ ___154-[UNSDefaultDataProviderFactory updateAuthorizationWithOptions:scheduledDeliveryEnabled:forNotificationSourceDescription:settingSource:completionHandler:]_block_invoke
+ ___154-[UNSDefaultDataProviderFactory updateAuthorizationWithOptions:scheduledDeliveryEnabled:forNotificationSourceDescription:settingSource:completionHandler:]_block_invoke_2
+ ___162-[UNSDefaultDataProviderFactory requestAuthorizationStatus:withOptions:scheduledDeliveryEnabled:forNotificationSourceDescription:settingSource:completionHandler:]_block_invoke
+ ___162-[UNSDefaultDataProviderFactory requestAuthorizationStatus:withOptions:scheduledDeliveryEnabled:forNotificationSourceDescription:settingSource:completionHandler:]_block_invoke_2
+ ___165-[UNSNotificationAuthorizationService _queue_requestAuthorizationWithOptions:requestedOptions:forNotificationSourceDescription:withExpirationDate:completionHandler:]_block_invoke
+ ___195-[UNSDefaultDataProviderFactory requestAuthorizationStatus:withOptions:scheduledDeliveryEnabled:expirationDate:lastUserGrantDate:forNotificationSourceDescription:settingSource:completionHandler:]_block_invoke
+ ___195-[UNSDefaultDataProviderFactory requestAuthorizationStatus:withOptions:scheduledDeliveryEnabled:expirationDate:lastUserGrantDate:forNotificationSourceDescription:settingSource:completionHandler:]_block_invoke_2
+ ___209-[UNSDefaultDataProviderFactory _queue_updateSettingsWithAuthorizationStatus:options:scheduledDeliveryEnabled:expirationDate:lastUserGrantDate:forNotificationSourceDescription:settingSource:completionHandler:]_block_invoke
+ ___block_descriptor_105_e8_32s40s48s56s64s72bs_e32_v16?0"UNSDefaultDataProvider"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_105_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e8_v16?0q8ls32l8s40l8s56l8s48l8
+ ___block_descriptor_65_e8_32s40s48bs_e32_v16?0"UNSDefaultDataProvider"8ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_89_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_89_e8_32s40s48s56s64bs_e8_v16?0q8ls32l8s40l8s48l8s56l8s64l8
- -[UNSDefaultDataProviderFactory _queue_setCriticalAlertAuthorization:forNotificationSourceDescription:completionHandler:]
- -[UNSDefaultDataProviderFactory _queue_setSectionInfo:forBundleIdentifier:]
- -[UNSDefaultDataProviderFactory _queue_updateSettingsWithAuthorizationStatus:options:scheduledDeliveryEnabled:expirationDate:lastUserGrantDate:forNotificationSourceDescription:completionHandler:]
- -[UNSDefaultDataProviderFactory _queue_updateSettingsWithAuthorizationStatus:options:scheduledDeliveryEnabled:forNotificationSourceDescription:completionHandler:]
- -[UNSDefaultDataProviderFactory requestAuthorizationStatus:withOptions:scheduledDeliveryEnabled:expirationDate:lastUserGrantDate:forNotificationSourceDescription:completionHandler:]
- -[UNSDefaultDataProviderFactory setCriticalAlertAuthorization:forNotificationSourceDescription:completionHandler:]
- -[UNSDefaultDataProviderFactory updateAuthorizationWithOptions:scheduledDeliveryEnabled:forNotificationSourceDescription:completionHandler:]
- -[UNSNotificationAuthorizationService _queue_requestAuthorizationWithOptions:forNotificationSourceDescription:withExpirationDate:completionHandler:]
- GCC_except_table42
- ___114-[UNSDefaultDataProviderFactory setCriticalAlertAuthorization:forNotificationSourceDescription:completionHandler:]_block_invoke
- ___114-[UNSDefaultDataProviderFactory setCriticalAlertAuthorization:forNotificationSourceDescription:completionHandler:]_block_invoke_2
- ___121-[UNSDefaultDataProviderFactory _queue_setCriticalAlertAuthorization:forNotificationSourceDescription:completionHandler:]_block_invoke
- ___140-[UNSDefaultDataProviderFactory updateAuthorizationWithOptions:scheduledDeliveryEnabled:forNotificationSourceDescription:completionHandler:]_block_invoke
- ___140-[UNSDefaultDataProviderFactory updateAuthorizationWithOptions:scheduledDeliveryEnabled:forNotificationSourceDescription:completionHandler:]_block_invoke_2
- ___148-[UNSDefaultDataProviderFactory requestAuthorizationStatus:withOptions:scheduledDeliveryEnabled:forNotificationSourceDescription:completionHandler:]_block_invoke
- ___148-[UNSDefaultDataProviderFactory requestAuthorizationStatus:withOptions:scheduledDeliveryEnabled:forNotificationSourceDescription:completionHandler:]_block_invoke_2
- ___148-[UNSNotificationAuthorizationService _queue_requestAuthorizationWithOptions:forNotificationSourceDescription:withExpirationDate:completionHandler:]_block_invoke
- ___181-[UNSDefaultDataProviderFactory requestAuthorizationStatus:withOptions:scheduledDeliveryEnabled:expirationDate:lastUserGrantDate:forNotificationSourceDescription:completionHandler:]_block_invoke
- ___181-[UNSDefaultDataProviderFactory requestAuthorizationStatus:withOptions:scheduledDeliveryEnabled:expirationDate:lastUserGrantDate:forNotificationSourceDescription:completionHandler:]_block_invoke_2
- ___195-[UNSDefaultDataProviderFactory _queue_updateSettingsWithAuthorizationStatus:options:scheduledDeliveryEnabled:expirationDate:lastUserGrantDate:forNotificationSourceDescription:completionHandler:]_block_invoke
- ___block_descriptor_57_e8_32s40s48bs_e32_v16?0"UNSDefaultDataProvider"8ls32l8s40l8s48l8
- ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e8_v16?0q8ls32l8s40l8s48l8s56l8
- ___block_descriptor_73_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_81_e8_32s40s48s56s64bs_e8_v16?0q8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_97_e8_32s40s48s56s64s72bs_e32_v16?0"UNSDefaultDataProvider"8ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_97_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
CStrings:
+ "[%{public}@] BBSettingsGateway does not support setSectionInfo:forSectionID:source:. Writing without setting source"
+ "[%{public}@] No response to critical alert prompt. Leaving the setting untouched"
+ "numRequestedOptions"
```
