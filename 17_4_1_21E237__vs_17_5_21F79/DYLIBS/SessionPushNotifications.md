## SessionPushNotifications

> `/System/Library/PrivateFrameworks/SessionPushNotifications.framework/SessionPushNotifications`

```diff

-127.107.0.0.0
-  __TEXT.__text: 0x422e8
-  __TEXT.__auth_stubs: 0x1030
+127.300.101.0.0
+  __TEXT.__text: 0x5427c
+  __TEXT.__auth_stubs: 0x1130
   __TEXT.__objc_methlist: 0x78
-  __TEXT.__const: 0x1370
-  __TEXT.__swift5_typeref: 0x887
-  __TEXT.__cstring: 0x205c
-  __TEXT.__constg_swiftt: 0xb30
-  __TEXT.__swift5_reflstr: 0x6e4
-  __TEXT.__swift5_fieldmd: 0x828
+  __TEXT.__const: 0x1bb8
+  __TEXT.__swift5_typeref: 0xd29
+  __TEXT.__cstring: 0x32cc
+  __TEXT.__constg_swiftt: 0x1058
+  __TEXT.__swift5_reflstr: 0xb84
+  __TEXT.__swift5_fieldmd: 0xb9c
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_proto: 0xbc
-  __TEXT.__swift5_types: 0x90
-  __TEXT.__swift5_protos: 0x28
+  __TEXT.__swift5_proto: 0x10c
+  __TEXT.__swift5_types: 0xb0
+  __TEXT.__swift5_protos: 0x4c
+  __TEXT.__swift5_capture: 0x3d4
   __TEXT.__swift5_mpenum: 0x20
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_capture: 0x1ac
-  __TEXT.__unwind_info: 0x163c
-  __TEXT.__eh_frame: 0x9e8
-  __TEXT.__objc_classname: 0x1f
-  __TEXT.__objc_methname: 0x578
-  __TEXT.__objc_methtype: 0x342
-  __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0xa8
-  __DATA_CONST.__objc_classlist: 0x48
+  __TEXT.__unwind_info: 0x1c60
+  __TEXT.__eh_frame: 0xc08
+  __TEXT.__objc_classname: 0x41
+  __TEXT.__objc_methname: 0x623
+  __TEXT.__objc_methtype: 0x38a
+  __DATA_CONST.__got: 0x1b8
+  __DATA_CONST.__const: 0xf8
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xcf0
-  __DATA_CONST.__objc_selrefs: 0x110
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0x48
-  __AUTH_CONST.__const: 0x1508
-  __AUTH_CONST.__auth_ptr: 0x58
+  __DATA_CONST.__objc_const: 0x1918
+  __DATA_CONST.__objc_selrefs: 0x140
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x60
+  __AUTH_CONST.__const: 0x20f0
+  __AUTH_CONST.__auth_ptr: 0x70
   __AUTH_CONST.__objc_const: 0x40
-  __AUTH_CONST.__auth_got: 0x818
-  __AUTH.__data: 0x388
-  __AUTH.__objc_data: 0x90
-  __DATA.__data: 0x380
-  __DATA.__bss: 0xe80
-  __DATA_DIRTY.__objc_data: 0x2c8
-  __DATA_DIRTY.__data: 0xb80
+  __AUTH_CONST.__auth_got: 0x898
+  __AUTH.__data: 0xa80
+  __AUTH.__objc_data: 0xe0
+  __DATA.__data: 0x640
+  __DATA.__bss: 0x1300
+  __DATA_DIRTY.__const: 0x88
+  __DATA_DIRTY.__objc_data: 0x298
+  __DATA_DIRTY.__data: 0xa18
   __DATA_DIRTY.__bss: 0x480
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/PushKit.framework/PushKit
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
+  - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/SessionFoundation.framework/SessionFoundation
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1212
-  Symbols:   455
-  CStrings:  277
+  Functions: 1642
+  Symbols:   684
+  CStrings:  384
 
Symbols:
+ _IOPMScheduleUserActivityLevelNotificationWithTimeout
+ _IOPMUnregisterNotification
+ _IOPSCopyPowerSourcesByTypePrecise
+ _IOPSCopyPowerSourcesList
+ _IOPSGetPowerSourceDescription
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$__CDClientContext
+ _OBJC_CLASS_$__CDContextQueries
+ __DATA__TtC24SessionPushNotifications11BudgetCache
+ __DATA__TtC24SessionPushNotifications12BudgetServer
+ __DATA__TtC24SessionPushNotifications19BudgetLevelResolver
+ __DATA__TtC24SessionPushNotifications20WatchActivityMonitor
+ __DATA__TtC24SessionPushNotifications21DeviceActivityMonitor
+ __DATA__TtC24SessionPushNotifications33DeviceActivityBudgetLevelProvider
+ __DATA__TtC24SessionPushNotificationsP33_3F511B504C88F0626D8587C509C685D417IDSBagValueServer
+ __IVARS__TtC24SessionPushNotifications11BudgetCache
+ __IVARS__TtC24SessionPushNotifications12BudgetServer
+ __IVARS__TtC24SessionPushNotifications19BudgetLevelResolver
+ __IVARS__TtC24SessionPushNotifications20WatchActivityMonitor
+ __IVARS__TtC24SessionPushNotifications21DeviceActivityMonitor
+ __IVARS__TtC24SessionPushNotifications33DeviceActivityBudgetLevelProvider
+ __IVARS__TtC24SessionPushNotificationsP33_3F511B504C88F0626D8587C509C685D417IDSBagValueServer
+ __METACLASS_DATA__TtC24SessionPushNotifications11BudgetCache
+ __METACLASS_DATA__TtC24SessionPushNotifications12BudgetServer
+ __METACLASS_DATA__TtC24SessionPushNotifications19BudgetLevelResolver
+ __METACLASS_DATA__TtC24SessionPushNotifications20WatchActivityMonitor
+ __METACLASS_DATA__TtC24SessionPushNotifications21DeviceActivityMonitor
+ __METACLASS_DATA__TtC24SessionPushNotifications33DeviceActivityBudgetLevelProvider
+ __METACLASS_DATA__TtC24SessionPushNotificationsP33_3F511B504C88F0626D8587C509C685D417IDSBagValueServer
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_destroy_boxed_opaque_existential_2Tm
+ ___swift_memcpy68_8
+ ___swift_project_boxed_opaque_existential_1Tm
+ _acTryWithObjCException
+ _associated conformance 24SessionPushNotifications0B5TokenVSHAASQ
+ _associated conformance 24SessionPushNotifications19DeviceActivityLevelOSHAASQ
+ _associated conformance 24SessionPushNotifications6BudgetV0D4TypeOSHAASQ
+ _associated conformance 24SessionPushNotifications6BudgetV5LevelOSLAASQ
+ _block_copy_helper.11
+ _block_copy_helper.18
+ _block_copy_helper.22
+ _block_copy_helper.24
+ _block_copy_helper.37
+ _block_copy_helper.45
+ _block_copy_helper.48
+ _block_copy_helper.51
+ _block_copy_helper.54
+ _block_copy_helper.60
+ _block_copy_helper.66
+ _block_copy_helper.72
+ _block_copy_helper.75
+ _block_copy_helper.83
+ _block_copy_helper.86
+ _block_descriptor.13
+ _block_descriptor.20
+ _block_descriptor.24
+ _block_descriptor.26
+ _block_descriptor.39
+ _block_descriptor.47
+ _block_descriptor.50
+ _block_descriptor.53
+ _block_descriptor.56
+ _block_descriptor.62
+ _block_descriptor.68
+ _block_descriptor.74
+ _block_descriptor.77
+ _block_descriptor.85
+ _block_descriptor.88
+ _block_destroy_helper.12
+ _block_destroy_helper.19
+ _block_destroy_helper.23
+ _block_destroy_helper.25
+ _block_destroy_helper.38
+ _block_destroy_helper.46
+ _block_destroy_helper.49
+ _block_destroy_helper.52
+ _block_destroy_helper.55
+ _block_destroy_helper.61
+ _block_destroy_helper.67
+ _block_destroy_helper.73
+ _block_destroy_helper.76
+ _block_destroy_helper.84
+ _block_destroy_helper.87
+ _notify_register_dispatch
+ _objectdestroy.24Tm
+ _objectdestroy.27Tm
+ _objectdestroy.2Tm
+ _objectdestroy.30Tm
+ _objectdestroy.33Tm
+ _objectdestroy.58Tm
+ _objectdestroy.6Tm
+ _swift_deallocUninitializedObject
+ _swift_retain_n
+ _swift_updateClassMetadata2
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
+ _symbolic $s24SessionPushNotifications0B15EventPublishingP
+ _symbolic $s24SessionPushNotifications0B17PriorityProvidingP
+ _symbolic $s24SessionPushNotifications0B24PriorityChangePublishingP
+ _symbolic $s24SessionPushNotifications13BudgetServingP
+ _symbolic $s24SessionPushNotifications13BudgetStoringP
+ _symbolic $s24SessionPushNotifications20BudgetLevelProvidingP
+ _symbolic $s24SessionPushNotifications20BudgetLevelResolvingP
+ _symbolic $s24SessionPushNotifications24DeviceActivityMonitoringP
+ _symbolic $s24SessionPushNotifications27BudgetLevelChangePublishingP
+ _symbolic Ieg_
+ _symbolic SDySS_____G 24SessionPushNotifications6BudgetV
+ _symbolic SS3key______5valuet 24SessionPushNotifications6BudgetV
+ _symbolic SS3key______5valuetSg 24SessionPushNotifications6BudgetV
+ _symbolic SS_____Ieggn_ 24SessionPushNotifications6BudgetV5LevelO
+ _symbolic SS______t 24SessionPushNotifications6BudgetV
+ _symbolic Say______pG 24SessionPushNotifications20BudgetLevelProvidingP
+ _symbolic Say______pG 24SessionPushNotifications24DeviceActivityMonitoringP
+ _symbolic Sd
+ _symbolic Shy_____G 7Combine14AnyCancellableC
+ _symbolic SiSg
+ _symbolic So9NSCopying_So14NSSecureCodingSo8NSObjectp
+ _symbolic SuSg
+ _symbolic _____ 24SessionPushNotifications11BudgetCacheC
+ _symbolic _____ 24SessionPushNotifications12BudgetServerC
+ _symbolic _____ 24SessionPushNotifications17IDSBagValueServer33_3F511B504C88F0626D8587C509C685D4LLC
+ _symbolic _____ 24SessionPushNotifications19BudgetLevelResolverC
+ _symbolic _____ 24SessionPushNotifications19DeviceActivityLevelO
+ _symbolic _____ 24SessionPushNotifications20WatchActivityMonitorC
+ _symbolic _____ 24SessionPushNotifications21DeviceActivityMonitorC
+ _symbolic _____ 24SessionPushNotifications33DeviceActivityBudgetLevelProviderC
+ _symbolic _____ 24SessionPushNotifications6BudgetV0D4TypeO
+ _symbolic _____ s5Int32V
+ _symbolic _____Sg 24SessionPushNotifications6BudgetV
+ _symbolic _____Sg 24SessionPushNotifications6BudgetV5LevelO
+ _symbolic _____SgXw 24SessionPushNotifications12BudgetServerC
+ _symbolic _____SgXw 24SessionPushNotifications19BudgetLevelResolverC
+ _symbolic _____SgXw 24SessionPushNotifications20WatchActivityMonitorC
+ _symbolic _____SgXw 24SessionPushNotifications21DeviceActivityMonitorC
+ _symbolic _____SgXw 24SessionPushNotifications33DeviceActivityBudgetLevelProviderC
+ _symbolic _____SgXwz_Xx 24SessionPushNotifications21DeviceActivityMonitorC
+ _symbolic _____Sgz_Xx 10Foundation4DataV
+ _symbolic _____XDXMT 24SessionPushNotifications20WatchActivityMonitorC
+ _symbolic _____XDXMT 24SessionPushNotifications21DeviceActivityMonitorC
+ _symbolic ___________p 24SessionPushNotifications13BudgetServingP AA0B17PriorityProvidingP
+ _symbolic ______p 24SessionPushNotifications13BudgetStoringP
+ _symbolic ______p 24SessionPushNotifications20BudgetLevelProvidingP
+ _symbolic ______p 24SessionPushNotifications20BudgetLevelResolvingP
+ _symbolic ______pSg 24SessionPushNotifications13BudgetStoringP
+ _symbolic _____ySS_____G s18_DictionaryStorageC 24SessionPushNotifications6BudgetV
+ _symbolic _____ySS______t_____G 7Combine12AnyPublisherV 24SessionPushNotifications6BudgetV5LevelO s5NeverO
+ _symbolic _____ySS______t_____G 7Combine18PassthroughSubjectC 24SessionPushNotifications6BudgetV5LevelO s5NeverO
+ _symbolic _____ySS______t_____GSg 7Combine12AnyPublisherV 24SessionPushNotifications6BudgetV5LevelO s5NeverO
+ _symbolic _____ySay_____G_____G 7Combine18PassthroughSubjectC 24SessionPushNotifications0E5TokenV s5NeverO
+ _symbolic _____ySb_____G 7Combine12AnyPublisherV s5NeverO
+ _symbolic _____ySb_____G 7Combine18PassthroughSubjectC s5NeverO
+ _symbolic _____ySb_____GSg 7Combine12AnyPublisherV s5NeverO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 24SessionPushNotifications6BudgetV
+ _symbolic _____y______pG s23_ContiguousArrayStorageC 24SessionPushNotifications20BudgetLevelProvidingP
+ _symbolic _____y______ySS______t_____GSo17OS_dispatch_queueCG 7Combine10PublishersO9ReceiveOnV AA12AnyPublisherV 24SessionPushNotifications6BudgetV5LevelO s5NeverO
+ _symbolic _____y______ySb_____GSo17OS_dispatch_queueCG 7Combine10PublishersO9ReceiveOnV AA12AnyPublisherV s5NeverO
+ _symbolic _____y______yyt_____GSo17OS_dispatch_queueCG 7Combine10PublishersO9ReceiveOnV AA12AnyPublisherV s5NeverO
+ _symbolic _____yyt_____G 7Combine12AnyPublisherV s5NeverO
+ _symbolic _____yyt_____G 7Combine18PassthroughSubjectC s5NeverO
+ _symbolic _____yyt_____GSg 7Combine12AnyPublisherV s5NeverO
+ _symbolic yp
- __DATA__TtC24SessionPushNotificationsP33_AF5B497284980FF868298026FC58F43117IDSBagValueServer
- __IVARS__TtC24SessionPushNotificationsP33_AF5B497284980FF868298026FC58F43117IDSBagValueServer
- __METACLASS_DATA__TtC24SessionPushNotificationsP33_AF5B497284980FF868298026FC58F43117IDSBagValueServer
- ___swift_destroy_boxed_opaque_existential_1Tm
- _block_copy_helper.110
- _block_copy_helper.30
- _block_descriptor.112
- _block_descriptor.32
- _block_destroy_helper.111
- _block_destroy_helper.31
- _objc_retain_x28
- _objectdestroy.12Tm
- _objectdestroy.34Tm
- _objectdestroy.37Tm
- _objectdestroy.43Tm
- _symbolic SS3key______5valuet 24SessionPushNotifications0B12SubscriptionV
- _symbolic SS3key______5valuetSg 24SessionPushNotifications0B12SubscriptionV
- _symbolic SS______t 24SessionPushNotifications0B12SubscriptionV
- _symbolic _____ 24SessionPushNotifications17IDSBagValueServer33_AF5B497284980FF868298026FC58F431LLC
- _symbolic _____Sg 24SessionPushNotifications0B12SubscriptionV
- _symbolic _____Sg 7Combine14AnyCancellableC
- _symbolic _____Sg_ABt 24SessionPushNotifications0B12SubscriptionV
- _symbolic _____y__________G 7Combine18PassthroughSubjectC 24SessionPushNotifications0E5TokenV s5NeverO
CStrings:
+ "$__lazy_storage_$_budgetLevelChangePublisher"
+ "$__lazy_storage_$_budgetLevelExceededPublisher"
+ "$__lazy_storage_$_deviceActivityStatePublisher"
+ "$__lazy_storage_$_pushPriorityChangePublisher"
+ "; maximumBudgetPerWindow: "
+ "; remainingBudget: "
+ "; subscriptionID: "
+ "; windowDuration: "
+ "@24@0:8@\"NSCoder\"16"
+ "@24@0:8@16"
+ "@24@0:8^{_NSZone=}16"
+ "Accessory Category"
+ "Adding activity push budget for %{public}s"
+ "Adding push-to-start budget for %{public}s"
+ "Budget does not exist; not reducing budget for %{public}s"
+ "Budget level resolver published a change"
+ "Budget server says budget level exceeded for %{public}s"
+ "Budget server says priority has changed; updating enabled topics"
+ "Cannot last use date keypath; device is treated as active"
+ "Cannot obtain last activity date; device is treated as active"
+ "Cannot obtain user context; device is treated as active"
+ "Could not find a connected watch"
+ "Could not get connected device list"
+ "Could not get power source description"
+ "Could not register for attachment notifications"
+ "Could not register for power source notifications"
+ "Device active (last active at %s)"
+ "Device activity state may have changed to %{bool,public}d"
+ "Device activity timeout overridden; set to %{public}f"
+ "Device inactive (last active at %s)"
+ "Device is active as grace period has not expired.  Scheduling another wake."
+ "Device is active; publishing budget level change event"
+ "Device is inactive after grace period expired.  Publishing budget level change event."
+ "Device is inactive and grace period has already expired.  Publishing budget level change event."
+ "Device is inactive; scheduling activity check at %{public}s"
+ "Device is inactive; scheduling check after grace period"
+ "DeviceActivityBudgetLevelProvider has no opinion on budget level for %{private}s"
+ "DeviceActivityBudgetLevelProvider thinks %{private}s should have level %{public}s, privacy: .public)"
+ "DeviceInactiveCheck"
+ "Failed to register for device activity events"
+ "Found existing push token for topic: %{private}s"
+ "Found watch with charging state %{bool,public}d"
+ "Incoming message contains a payload that cannot be serialized to data: %{public}@"
+ "Incoming message contains attributes that cannot be serialized to data"
+ "Incoming message contains attributes that cannot be serialized to data: %{public}@"
+ "Inductive In-Band"
+ "NSCoding"
+ "NSCopying"
+ "NSSecureCoding"
+ "Received push event for %{public}s"
+ "Registered for device activity events"
+ "Removed expired budget for %{private}s"
+ "Reported last activity date is nonsense; device is treated as active"
+ "Requesting frequent updates permission for activity exceeding reduced budget %{public}s"
+ "Requesting frequent updates permission for activity exceeding reduced budget %{public}s; remaining budget: %{public}ld"
+ "Restored %{public}ld budgets"
+ "TB,R"
+ "Topic %{private}s has not used any budget for %{public}s"
+ "Topic %{private}s has remaining budget for %{public}s of %{public}ld"
+ "Topic %{private}s is out of budget because %{public}s is exhausted"
+ "Watch charging state has changed to %{bool,public}d"
+ "_TtC24SessionPushNotifications11BudgetCache"
+ "_TtC24SessionPushNotifications12BudgetServer"
+ "_TtC24SessionPushNotifications19BudgetLevelResolver"
+ "_TtC24SessionPushNotifications20WatchActivityMonitor"
+ "_TtC24SessionPushNotifications21DeviceActivityMonitor"
+ "_TtC24SessionPushNotifications33DeviceActivityBudgetLevelProvider"
+ "_TtC24SessionPushNotificationsP33_3F511B504C88F0626D8587C509C685D417IDSBagValueServer"
+ "_budgetLevelChangePublisher"
+ "_budgetLevelExceededPublisher"
+ "_deviceActivityStatePublisher"
+ "_lock_maximumUpdateBudgetPerWindow"
+ "_pushPriorityChangePublisher"
+ "attachToken"
+ "boolValue"
+ "budgetLevelResolver"
+ "budgetServer"
+ "cancellableSubscriptions"
+ "com.apple.SessionPushNotifications.BudgetLevelResolver.callout"
+ "com.apple.SessionPushNotifications.BudgetLevelResolver.internal"
+ "com.apple.SessionPushNotifications.BudgetServer.callout"
+ "com.apple.SessionPushNotifications.BudgetServer.internal"
+ "com.apple.SessionPushNotifications.BudgetStore.internal"
+ "com.apple.SessionPushNotifications.DeviceActivityBudgetLevelProvider.callout"
+ "com.apple.SessionPushNotifications.DeviceActivityBudgetLevelProvider.internal"
+ "com.apple.SessionPushNotifications.DeviceActivityMonitor.internal"
+ "com.apple.SessionPushNotifications.WatchActivityMonitor.internal"
+ "com.apple.system.accpowersources.attach"
+ "com.apple.system.accpowersources.source"
+ "copyWithZone:"
+ "deviceActivityMonitors"
+ "doubleForKey:"
+ "encodeWithCoder:"
+ "handle"
+ "initWithCoder:"
+ "integerValue"
+ "keyPathForLastUseDate"
+ "objectForContextualKeyPath:"
+ "overrideMaximumPushToStartBudgetPerWindow"
+ "overrideMaximumUpdateBudgetPerWindow"
+ "overrideWindowDuration"
+ "persistentStore"
+ "powerSourceToken"
+ "queue_budgetsBySubscriptionID"
+ "queue_inactivityCheckTask"
+ "queue_isActive"
+ "queue_isWatchCharging"
+ "queue_lastActivityDate"
+ "queue_nextBudgetResetWake"
+ "queue_providers"
+ "queue_store"
+ "queue_subscriptions"
+ "subscriptions"
+ "supportsSecureCoding"
+ "userContext"
+ "v12@?0i8"
+ "v24@0:8@\"NSCoder\"16"
+ "v24@?0Q8Q16"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Requesting frequent updates permission for activity exceeding reduced budget %{public}s remaining budget: %{public}ld"
- "Subscription for activity has unexpected type: %{public}s"
- "Swift/Array.swift"
- "Swift/IntegerTypes.swift"
- "_TtC24SessionPushNotificationsP33_AF5B497284980FF868298026FC58F43117IDSBagValueServer"
- "_lock_maximumBudgetPerWindow"
- "budgetEnforcementPolicyProviderSubscription"
- "nextBudgetTimeoutExpirationWake"

```
