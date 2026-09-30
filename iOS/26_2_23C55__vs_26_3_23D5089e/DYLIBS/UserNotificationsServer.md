## UserNotificationsServer

> `/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer`

```diff

-640.2.11.0.0
-  __TEXT.__text: 0x3926c
+640.3.14.0.0
+  __TEXT.__text: 0x39a28
   __TEXT.__auth_stubs: 0x1100
-  __TEXT.__objc_methlist: 0x22d4
+  __TEXT.__objc_methlist: 0x2304
   __TEXT.__const: 0x394
-  __TEXT.__oslogstring: 0x629a
-  __TEXT.__cstring: 0x15a7
-  __TEXT.__gcc_except_tab: 0x868
+  __TEXT.__oslogstring: 0x636a
+  __TEXT.__cstring: 0x15e7
+  __TEXT.__gcc_except_tab: 0x8c4
   __TEXT.__swift5_typeref: 0x38e
   __TEXT.__swift5_fieldmd: 0x9c
   __TEXT.__constg_swiftt: 0x1f0

   __TEXT.__swift5_capture: 0x124
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0xd68
+  __TEXT.__unwind_info: 0xd80
   __TEXT.__eh_frame: 0x248
   __TEXT.__objc_classname: 0x700
-  __TEXT.__objc_methname: 0xb2ed
-  __TEXT.__objc_methtype: 0x1a09
-  __TEXT.__objc_stubs: 0x9360
-  __DATA_CONST.__got: 0x8a8
-  __DATA_CONST.__const: 0x10d0
+  __TEXT.__objc_methname: 0xb3e7
+  __TEXT.__objc_methtype: 0x1a8e
+  __TEXT.__objc_stubs: 0x9440
+  __DATA_CONST.__got: 0x8c8
+  __DATA_CONST.__const: 0x1108
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a00
+  __DATA_CONST.__objc_selrefs: 0x2a38
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x890
   __AUTH_CONST.__const: 0x5d8
-  __AUTH_CONST.__cfstring: 0xbc0
-  __AUTH_CONST.__objc_const: 0x59a8
+  __AUTH_CONST.__cfstring: 0xbe0
+  __AUTH_CONST.__objc_const: 0x59b0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xd8
   __AUTH.__data: 0x98

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient
   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
+  - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
+  - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices
   - /System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore
   - /System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 57B4CA2E-01D6-3C93-95E0-9496BCE5F5F2
-  Functions: 1045
-  Symbols:   4182
-  CStrings:  2293
+  UUID: BC9A9ADC-A354-3585-9008-B940B3EFB605
+  Functions: 1049
+  Symbols:   4207
+  CStrings:  2308
 
Symbols:
+ -[UNSNotificationSettingsService notificationSourcesWithFilter:sort:maxCount:completionHandler:]
+ -[UNSUserNotificationServer notificationRecordForIdentifier:bundleIdentifier:]
+ -[UNSUserNotificationServerSettingsConnectionListener getNotificationSourcesWithFilter:sort:maxCount:completionHandler:]
+ _OBJC_CLASS_$_ATXDigestSetupFlowClient
+ _UNLogAppFiltration
+ _UNNotificationSourceSortOrderDefault
+ _UNNotificationSourceSortOrderWeeklyNotificationAverage
+ ___96-[UNSNotificationSettingsService notificationSourcesWithFilter:sort:maxCount:completionHandler:]_block_invoke
+ ___96-[UNSNotificationSettingsService notificationSourcesWithFilter:sort:maxCount:completionHandler:]_block_invoke.cold.1
+ ___block_descriptor_64_e8_32s40s48bs56w_e23_v28?0"NSArray"8B16Q20lw56l8s48l8s32l8s40l8
+ ___block_literal_global.343
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_UserNotificationsServer
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_UserNotificationsServer
+ _objc_msgSend$appsSortedByNotificationsReceivedInPreviousNumDaysRaw:completionHandler:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$bundleId
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$notificationSourcesWithFilter:sort:maxCount:completionHandler:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$subarrayWithRange:
- -[UNSUserNotificationServerSettingsConnectionListener getNotificationSourcesWithFilter:completionHandler:]
- ___block_literal_global.341
CStrings:
+ "@\"UNSNotificationRecord\"32@0:8@\"NSString\"16@\"NSString\"24"
+ "Error getting ATXDigestSetupResponses for notification sources"
+ "Failed to retrieve notification volume data"
+ "Notification source not found for bundle ID: %{public}@"
+ "Unsupported sort order '%{public}@', returning filtered sources without sorting"
+ "appsSortedByNotificationsReceivedInPreviousNumDaysRaw:completionHandler:"
+ "arrayWithCapacity:"
+ "bundleId"
+ "dictionaryWithCapacity:"
+ "getNotificationSourcesWithFilter:sort:maxCount:completionHandler:"
+ "notificationSourcesWithFilter:sort:maxCount:completionHandler:"
+ "setObject:forKeyedSubscript:"
+ "subarrayWithRange:"
+ "v28@?0@\"NSArray\"8B16Q20"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSNumber\"32@?<v@?@\"NSArray\"@\"NSError\">40"
- "getNotificationSourcesWithFilter:completionHandler:"

```
