## UserNotificationsServer

> `/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer`

```diff

-720.0.0.0.0
-  __TEXT.__text: 0x3af34
-  __TEXT.__objc_methlist: 0x24d4
-  __TEXT.__const: 0x4e4
+720.2.6.0.0
+  __TEXT.__text: 0x3b738
+  __TEXT.__objc_methlist: 0x2504
+  __TEXT.__const: 0x4f4
   __TEXT.__gcc_except_tab: 0x654
-  __TEXT.__cstring: 0x16b8
-  __TEXT.__oslogstring: 0x6865
+  __TEXT.__cstring: 0x1758
+  __TEXT.__oslogstring: 0x68b5
   __TEXT.__constg_swiftt: 0x278
   __TEXT.__swift5_typeref: 0x43c
   __TEXT.__swift5_capture: 0x12c

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x11e8
+  __TEXT.__unwind_info: 0x1210
   __TEXT.__eh_frame: 0x270
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x12b0
+  __DATA_CONST.__const: 0x1320
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c10
+  __DATA_CONST.__objc_selrefs: 0x2c30
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0x988
   __AUTH_CONST.__const: 0x778
-  __AUTH_CONST.__cfstring: 0xdc0
-  __AUTH_CONST.__objc_const: 0x5f28
+  __AUTH_CONST.__cfstring: 0xe80
+  __AUTH_CONST.__objc_const: 0x5f30
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0xa30
+  __AUTH_CONST.__auth_got: 0xa38
   __AUTH.__objc_data: 0x170
   __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x23c

   - /System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
   - /System/Library/PrivateFrameworks/ClipServices.framework/ClipServices
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1138
-  Symbols:   3289
-  CStrings:  527
+  Functions: 1146
+  Symbols:   3305
+  CStrings:  535
 
Symbols:
+ -[UNSNotificationSettingsService copyNotificationSettingsFromSourceIdentifier:toSourceIdentifier:withCompletionHandler:]
+ -[UNSSettingsGateway copySectionSettingsFromSectionID:toSectionID:withCompletion:]
+ -[UNSSettingsGateway setSectionInfo:forSectionID:source:]
+ -[UNSUserNotificationServerSettingsConnectionListener copyNotificationSettingsFromSourceIdentifier:toSourceIdentifier:withCompletionHandler:]
+ GCC_except_table22
+ GCC_except_table25
+ GCC_except_table30
+ _AnalyticsSendEventLazy
+ ___120-[UNSNotificationSettingsService copyNotificationSettingsFromSourceIdentifier:toSourceIdentifier:withCompletionHandler:]_block_invoke
+ ___57-[UNSSettingsGateway setSectionInfo:forSectionID:source:]_block_invoke
+ ___82-[UNSSettingsGateway copySectionSettingsFromSectionID:toSectionID:withCompletion:]_block_invoke
+ ___UNSSendAuthorizationPromptAnalytics_block_invoke
+ ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
+ ___block_descriptor_58_e19_"NSDictionary"8?0l
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_81_e8_32s40s48s56s64bs_e8_v16?0q8ls32l8s40l8s48l8s56l8s64l8
+ _objc_msgSend$copyNotificationSettingsFromSourceIdentifier:toSourceIdentifier:withCompletionHandler:
+ _objc_msgSend$copySectionSettingsFromSectionID:toSectionID:withCompletion:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$setSectionInfo:forSectionID:source:
- GCC_except_table21
- GCC_except_table23
- GCC_except_table28
- ___block_descriptor_72_e8_32s40s48s56bs_e8_v16?0q8ls32l8s40l8s48l8s56l8
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "UNSNotificationSettingsService [%{public}@] Copying notification settings from %{public}@"
+ "com.apple.usernotifications.settings.authorizationPrompt"
+ "hasUsageDescription"
+ "outcome"
+ "promptKind"
+ "requestedOptions"
+ "showedDeliveryOptions"
```
