## ActivityUIServices

> `/System/Library/PrivateFrameworks/ActivityUIServices.framework/ActivityUIServices`

```diff

-127.7.100.0.0
-  __TEXT.__text: 0x49cc8
-  __TEXT.__auth_stubs: 0x1710
-  __TEXT.__objc_methlist: 0x1e18
-  __TEXT.__const: 0x2318
-  __TEXT.__gcc_except_tab: 0x94
-  __TEXT.__cstring: 0x48fb
+127.18.0.0.0
+  __TEXT.__text: 0x4154c
+  __TEXT.__auth_stubs: 0x14a0
+  __TEXT.__objc_methlist: 0x1ca8
+  __TEXT.__const: 0x2258
+  __TEXT.__gcc_except_tab: 0x6c
+  __TEXT.__cstring: 0x437b
   __TEXT.__oslogstring: 0x98
-  __TEXT.__swift5_typeref: 0x11da
-  __TEXT.__constg_swiftt: 0x1cc4
-  __TEXT.__swift5_reflstr: 0xcfd
-  __TEXT.__swift5_fieldmd: 0xc7c
+  __TEXT.__swift5_typeref: 0xe1e
+  __TEXT.__constg_swiftt: 0x1b68
+  __TEXT.__swift5_reflstr: 0xc0d
+  __TEXT.__swift5_fieldmd: 0xbf4
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_assocty: 0x270
   __TEXT.__swift5_proto: 0x1a4
-  __TEXT.__swift5_types: 0x138
-  __TEXT.__swift5_capture: 0x660
+  __TEXT.__swift5_types: 0x134
+  __TEXT.__swift5_capture: 0x5e4
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x1b70
+  __TEXT.__unwind_info: 0x1a3c
   __TEXT.__eh_frame: 0x378
-  __TEXT.__objc_classname: 0x4ce
-  __TEXT.__objc_methname: 0x3fcc
-  __TEXT.__objc_methtype: 0xff2
-  __TEXT.__objc_stubs: 0x1b40
-  __DATA_CONST.__got: 0x240
-  __DATA_CONST.__const: 0x4b8
-  __DATA_CONST.__objc_classlist: 0x1c0
+  __TEXT.__objc_classname: 0x4b6
+  __TEXT.__objc_methname: 0x3d16
+  __TEXT.__objc_methtype: 0xfb6
+  __TEXT.__objc_stubs: 0x19a0
+  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__const: 0x458
+  __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_nlclslist: 0x8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x8f30
-  __DATA_CONST.__objc_selrefs: 0xf38
-  __AUTH_CONST.__objc_const: 0xb28
+  __DATA_CONST.__objc_const: 0x8d30
+  __DATA_CONST.__objc_selrefs: 0xe90
+  __AUTH_CONST.__objc_const: 0xa50
   __AUTH_CONST.__cfstring: 0x2c0
-  __AUTH_CONST.__const: 0x2b50
+  __AUTH_CONST.__const: 0x28e0
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_ptr: 0x80
-  __AUTH_CONST.__auth_got: 0xb98
-  __AUTH.__objc_data: 0x2058
+  __AUTH_CONST.__auth_ptr: 0x70
+  __AUTH_CONST.__auth_got: 0xa60
+  __AUTH.__objc_data: 0x2010
   __AUTH.__data: 0x338
   __DATA.__objc_protorefs: 0x90
-  __DATA.__objc_classrefs: 0x270
-  __DATA.__objc_superrefs: 0x98
-  __DATA.__objc_ivar: 0xc4
+  __DATA.__objc_classrefs: 0x258
+  __DATA.__objc_superrefs: 0x90
+  __DATA.__objc_ivar: 0xbc
   __DATA.__objc_data: 0x228
-  __DATA.__data: 0x11c8
+  __DATA.__data: 0x1108
   __DATA.__bss: 0x2210
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x22e8
-  __DATA_DIRTY.__data: 0x8a0
-  __DATA_DIRTY.__bss: 0x1a0
+  __DATA_DIRTY.__objc_data: 0x20c0
+  __DATA_DIRTY.__data: 0x760
+  __DATA_DIRTY.__bss: 0x190
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
-  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2706
-  Symbols:   2541
-  CStrings:  1308
+  Functions: 2578
+  Symbols:   2416
+  CStrings:  1246
 
Symbols:
- +[ACUISActivityController sharedInstance]
- -[ACUISActivityController .cxx_destruct]
- -[ACUISActivityController activityController]
- -[ACUISActivityController activityProviderWrapping:]
- -[ACUISActivityController activityUpdateProviders]
- -[ACUISActivityController disableActivitiesForIdentifier:]
- -[ACUISActivityController endActivity:]
- -[ACUISActivityController init]
- -[ACUISActivityController isActivityActive:]
- -[ACUISActivityController isActivityEnabled]
- -[ACUISActivityController observeActivityAlertsWithHandler:]
- -[ACUISActivityController observeActivityUpdatesWithHandler:]
- -[ACUISActivityController setActivityController:]
- -[ACUISActivityController setActivityUpdateProviders:]
- -[ACUISActivityController setSystemProvidedMetrics:]
- GCC_except_table6
- _AnalyticsSendEventLazy
- _OBJC_CLASS_$_ACUISActivityController
- _OBJC_CLASS_$__TtC18ActivityUIServices18ActivityController
- _OBJC_IVAR_$_ACUISActivityController._activityController
- _OBJC_IVAR_$_ACUISActivityController._activityUpdateProviders
- _OBJC_METACLASS_$_ACUISActivityController
- _OBJC_METACLASS_$__TtC18ActivityUIServices18ActivityController
- __CLASS_PROPERTIES__TtC18ActivityUIServices18ActivityController
- __DATA__TtC18ActivityUIServices18ActivityController
- __IVARS__TtC18ActivityUIServices18ActivityController
- __METACLASS_DATA__TtC18ActivityUIServices18ActivityController
- __OBJC_$_CLASS_METHODS_ACUISActivityController
- __OBJC_$_CLASS_METHODS__TtC18ActivityUIServices18ActivityController
- __OBJC_$_CLASS_PROP_LIST_ACUISActivityController
- __OBJC_$_INSTANCE_METHODS_ACUISActivityController
- __OBJC_$_INSTANCE_METHODS__TtC18ActivityUIServices18ActivityController
- __OBJC_$_INSTANCE_VARIABLES_ACUISActivityController
- __OBJC_$_PROP_LIST_ACUISActivityController
- __OBJC_CLASS_RO_$_ACUISActivityController
- __OBJC_METACLASS_RO_$_ACUISActivityController
- __PROPERTIES__TtC18ActivityUIServices18ActivityController
- ___41+[ACUISActivityController sharedInstance]_block_invoke
- ___60-[ACUISActivityController observeActivityAlertsWithHandler:]_block_invoke
- ___61-[ACUISActivityController observeActivityUpdatesWithHandler:]_block_invoke
- ___block_descriptor_48_e8_32bs40w_e61_v16?0"<_TtP18ActivityUIServices22ActivityAlertProviding_>"8lw40l8s32l8
- ___block_descriptor_48_e8_32bs40w_e62_v16?0"<_TtP18ActivityUIServices23ActivityUpdateProviding_>"8lw40l8s32l8
- _block_copy_helper.30
- _block_descriptor.32
- _block_destroy_helper.31
- _objc_msgSend$activityProviderWrapping:
- _objc_msgSend$activityUpdateProviders
- _objc_msgSend$areActivitiesEnabled
- _objc_msgSend$disableActivitiesForBundleId:
- _objc_msgSend$endActivityWithIdentifier:
- _objc_msgSend$initWithActivityUpdateProviding:
- _objc_msgSend$isActivityActiveWithIdentifier:
- _objc_msgSend$observeActivityAlertsWithHandler:
- _objc_msgSend$observeActivityUpdates
- _objc_msgSend$observeActivityUpdatesWithHandler:
- _objc_msgSend$setSystemMetricsRequest:
- _objc_msgSend$shared
- _objc_msgSend$weakToWeakObjectsMapTable
- _objc_retain_x10
- _sharedInstance.__instance
- _sharedInstance.once
- _swift_arrayInitWithTakeBackToFront
- _swift_arrayInitWithTakeFrontToBack
- _swift_initStackObject
- _symbolic 18ActivityUIServices0A14AlertProviding_pIegg_
- _symbolic 18ActivityUIServices0A14AlertProviding_pIeyBy_
- _symbolic 18ActivityUIServices0A15UpdateProviding_pIegg_
- _symbolic 18ActivityUIServices0A15UpdateProviding_pIeyBy_
- _symbolic SDySS_____G 11ActivityKit0A10DescriptorV
- _symbolic SDySS_____G 18ActivityUIServices0A14UpdateProviderC
- _symbolic SS______t 11ActivityKit0A10DescriptorV
- _symbolic Say_____G 11ActivityKit0A15DescriptorStateV
- _symbolic Shy_____G 7Combine14AnyCancellableC
- _symbolic _____ 11ActivityKit0A7ManagerC
- _symbolic _____ 18ActivityUIServices0A10ControllerC
- _symbolic _____Sg 11ActivityKit06OpaqueA7PayloadV
- _symbolic _____Sg 11ActivityKit0A10DescriptorV
- _symbolic _____Sg 11ActivityKit0A13EndingOptionsV
- _symbolic _____Sg So17OS_dispatch_queueC8DispatchE16SchedulerOptionsV
- _symbolic _____y18ActivityUIServices0A14AlertProviding_p_____G 7Combine12AnyPublisherV s5NeverO
- _symbolic _____y18ActivityUIServices0A14AlertProviding_p_____G 7Combine18PassthroughSubjectC s5NeverO
- _symbolic _____y18ActivityUIServices0A15UpdateProviding_p_____G 7Combine12AnyPublisherV s5NeverO
- _symbolic _____y18ActivityUIServices0A15UpdateProviding_p_____G 7Combine18PassthroughSubjectC s5NeverO
- _symbolic _____ySSG s23_ContiguousArrayStorageC
- _symbolic _____ySSSo8NSObjectCG s18_DictionaryStorageC
- _symbolic _____ySS_So8NSObjectCtG s23_ContiguousArrayStorageC
- _symbolic _____ySS_____G s18_DictionaryStorageC 11ActivityKit0C10DescriptorV
- _symbolic _____ySS_____G s18_DictionaryStorageC 18ActivityUIServices0C14UpdateProviderC
- _symbolic _____ySay_____GG 7Combine4JustV 11ActivityKit0C15DescriptorStateV
- _symbolic _____ySay_____G______pG 7Combine12AnyPublisherV 11ActivityKit0D15DescriptorStateV s5ErrorP
- _symbolic _____y_____G s11_SetStorageC 7Combine14AnyCancellableC
- _symbolic _____y_____G s23_ContiguousArrayStorageC 11ActivityKit0D15DescriptorStateV
- _symbolic _____y______y18ActivityUIServices0A14AlertProviding_p_____GSo17OS_dispatch_queueCG 7Combine10PublishersO9ReceiveOnV AA12AnyPublisherV s5NeverO
- _symbolic _____y______y18ActivityUIServices0A15UpdateProviding_p_____GSo17OS_dispatch_queueCG 7Combine10PublishersO9ReceiveOnV AA12AnyPublisherV s5NeverO
- _symbolic _____y______ySay_____G______pGSo17OS_dispatch_queueCG 7Combine10PublishersO9ReceiveOnV AA12AnyPublisherV 11ActivityKit0G15DescriptorStateV s5ErrorP
- _symbolic _____y______y______ySay_____G______pGSo17OS_dispatch_queueCG_____yAEGG 7Combine10PublishersO5CatchV AC9ReceiveOnV AA12AnyPublisherV 11ActivityKit0H15DescriptorStateV s5ErrorP AA4JustV
CStrings:
- "%{public}s: %{public}s (%ld) %{public}s"
- "@\"NSDictionary\"8@?0"
- "@\"_TtC18ActivityUIServices18ActivityController\""
- "@24@0:8@?16"
- "ACUISActivityController"
- "Activity Descriptor update: %{public}s"
- "Activity controller could not listen for activities"
- "ActivityController failed to subscribe to activities stream"
- "Add active activity: %{public}s"
- "Alert provider handler callback"
- "Could not disable activities for bundle id: %{private}s"
- "End active activity: %{public}s"
- "Observing activity updates, subscribing for alerts"
- "Publishing activity id: %{public}s, activityState: %{public}ld, activitySceneOwner: %{private}s"
- "Remove inactive activity: %{public}s"
- "Subscribing to activity alert stream"
- "Subscribing to activity platter stream"
- "T@\"ACUISActivityController\",R,N"
- "T@\"NSMapTable\",&,N,V_activityUpdateProviders"
- "T@\"_TtC18ActivityUIServices18ActivityController\",&,N,V_activityController"
- "T@\"_TtC18ActivityUIServices18ActivityController\",N,R"
- "T@\"_TtC18ActivityUIServices22ActivityMetricsRequest\",N,&,VsystemMetricsRequest"
- "_TtC18ActivityUIServices18ActivityController"
- "_activityController"
- "_activityUpdateProviders"
- "activities"
- "activityController"
- "activityManager"
- "activityPlatterPublisher"
- "activityPlatterStream"
- "activityProviderWrapping:"
- "activityProviders"
- "activityUpdateProviders"
- "areActivitiesEnabled"
- "cancellableSet"
- "com.apple.ActivityUIServices.activityControllerQueue"
- "com.apple.activitykit.activity"
- "disableActivitiesForBundleId:"
- "disableActivitiesForIdentifier:"
- "endActivity:"
- "endActivityWithIdentifier:"
- "isActivityActive:"
- "isActivityActiveWithIdentifier:"
- "isActivityEnabled"
- "observeActivityAlertsWithHandler:"
- "observeActivityUpdates"
- "observeActivityUpdatesWithHandler:"
- "observingActivityUpdates"
- "provider handler callback"
- "setActivityController:"
- "setActivityUpdateProviders:"
- "setSystemMetricsRequest:"
- "shared"
- "sharedInstance"
- "v16@?0@\"<_TtP18ActivityUIServices22ActivityAlertProviding_>\"8"
- "v16@?0@\"<_TtP18ActivityUIServices23ActivityUpdateProviding_>\"8"
- "weakToWeakObjectsMapTable"

```
