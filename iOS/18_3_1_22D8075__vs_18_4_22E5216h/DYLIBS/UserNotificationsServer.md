## UserNotificationsServer

> `/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer`

```diff

-579.4.3.401.0
-  __TEXT.__text: 0x3a75c
-  __TEXT.__auth_stubs: 0x1140
-  __TEXT.__objc_methlist: 0x1934
-  __TEXT.__const: 0x264
-  __TEXT.__oslogstring: 0x623a
-  __TEXT.__cstring: 0x2397
-  __TEXT.__gcc_except_tab: 0x858
+579.5.20.0.0
+  __TEXT.__text: 0x3a92c
+  __TEXT.__auth_stubs: 0x10f0
+  __TEXT.__objc_methlist: 0x22d4
+  __TEXT.__const: 0x284
+  __TEXT.__oslogstring: 0x638a
+  __TEXT.__cstring: 0x2077
+  __TEXT.__gcc_except_tab: 0x860
   __TEXT.__swift5_typeref: 0x382
   __TEXT.__swift5_fieldmd: 0x9c
   __TEXT.__constg_swiftt: 0x1f0

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_capture: 0x114
-  __TEXT.__unwind_info: 0xd58
-  __TEXT.__eh_frame: 0x218
+  __TEXT.__swift_as_entry: 0xc
+  __TEXT.__swift_as_ret: 0xc
+  __TEXT.__unwind_info: 0xd60
+  __TEXT.__eh_frame: 0x220
   __TEXT.__objc_classname: 0x708
-  __TEXT.__objc_methname: 0xbc84
+  __TEXT.__objc_methname: 0xbdb2
   __TEXT.__objc_methtype: 0x19cf
-  __TEXT.__objc_stubs: 0xa0e0
+  __TEXT.__objc_stubs: 0xa1c0
   __DATA_CONST.__got: 0x910
-  __DATA_CONST.__const: 0x1168
+  __DATA_CONST.__const: 0x1170
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b38
+  __DATA_CONST.__objc_selrefs: 0x2d68
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x8b0
+  __AUTH_CONST.__auth_got: 0x888
   __AUTH_CONST.__auth_ptr: 0xb8
   __AUTH_CONST.__const: 0x5a8
   __AUTH_CONST.__cfstring: 0x18a0
-  __AUTH_CONST.__objc_const: 0x6ae0
+  __AUTH_CONST.__objc_const: 0x59e0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xf8
-  __AUTH.__data: 0x238
+  __AUTH.__objc_data: 0xd8
+  __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x208
-  __DATA.__data: 0xcd0
+  __DATA.__data: 0xc90
   __DATA.__bss: 0x1a
-  __DATA.__common: 0x30
+  __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x758
-  __DATA_DIRTY.__data: 0x220
+  __DATA_DIRTY.__data: 0x410
   __DATA_DIRTY.__bss: 0x50
-  __DATA_DIRTY.__common: 0x18
+  __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1027
-  Symbols:   1432
-  CStrings:  2424
+  Functions: 1043
+  Symbols:   1447
+  CStrings:  2418
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ _objc_retain_x10
- _UNCUsePipeline
- _objc_retain_x9
CStrings:
+ "%@ is hidden by appprotection, blocking alert"
+ "Getting GlobalPrioritizationSetting"
+ "Getting globalPrioritizationSetting from settingsGateway: [%{public}@]"
+ "Setting globalPrioritizationSetting from settingsGateway: [%{public}@]"
+ "UNSNotificationSettingsService [%{public}@] Setting Notification System Setting for Prioritization"
+ "_queue_globalPrioritizationSetting"
+ "_queue_setGlobalPrioritizationSetting:"
+ "addInitialBulletins:categories:sourceDescription:settings:"
+ "createBulletin:category:destinations:sourceDescription:settings:completion:"
+ "effectiveGlobalHighlightsSetting"
+ "globalHighlightsSetting"
+ "globalPrioritizationSetting"
+ "initWithShowPreviewsSetting:announcementSetting:announcementHeadphonesSetting:announcementCarPlaySetting:scheduledDeliverySetting:scheduledDeliveryTimes:scheduledDeliveryShowNextSummarySetting:notificationListDisplayStyleSetting:summarizationSetting:prioritizationSetting:"
+ "prioritizationSetting"
+ "setEffectiveGlobalHighlightsSetting:"
+ "setGlobalPrioritizationSetting:"
+ "setPrioritizationSetting:"
+ "settingsWithAuthorizationStatus:soundSetting:badgeSetting:alertSetting:notificationCenterSetting:lockScreenSetting:carPlaySetting:remoteNotificationsSetting:announcementSetting:criticalAlertSetting:timeSensitiveSetting:scheduledDeliverySetting:directMessagesSetting:summarizationSetting:prioritizationSetting:alertStyle:showPreviewsSetting:groupingSetting:providesAppNotificationSettings:"
+ "updateBulletin:category:destinations:sourceDescription:settings:completion:"
+ "v48@0:8@16@24@32@40"
+ "v64@0:8@16@24Q32@40@48@?56"
- "Division by zero"
- "Division results in an overflow"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_isEligibleForPipeline"
- "addInitialBulletins:categories:sourceDescription:"
- "createBulletin:category:destinations:sourceDescription:completion:"
- "initWithShowPreviewsSetting:announcementSetting:announcementHeadphonesSetting:announcementCarPlaySetting:scheduledDeliverySetting:scheduledDeliveryTimes:scheduledDeliveryShowNextSummarySetting:notificationListDisplayStyleSetting:summarizationSetting:"
- "invalid Collection: less than 'count' elements in collection"
- "isEligibleForIndexing"
- "settingsWithAuthorizationStatus:soundSetting:badgeSetting:alertSetting:notificationCenterSetting:lockScreenSetting:carPlaySetting:remoteNotificationsSetting:announcementSetting:criticalAlertSetting:timeSensitiveSetting:scheduledDeliverySetting:directMessagesSetting:summarizationSetting:alertStyle:showPreviewsSetting:groupingSetting:providesAppNotificationSettings:"
- "updateBulletin:category:destinations:sourceDescription:completion:"
- "v56@0:8@16@24Q32@40@?48"

```
