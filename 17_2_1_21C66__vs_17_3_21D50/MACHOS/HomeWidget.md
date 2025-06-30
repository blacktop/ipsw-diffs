## HomeWidget

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget`

```diff

-841.3.9.1.1
-  __TEXT.__text: 0x872f4
-  __TEXT.__auth_stubs: 0x2040
-  __TEXT.__objc_methlist: 0x50
-  __TEXT.__const: 0x2684
-  __TEXT.__constg_swiftt: 0xb0c
-  __TEXT.__swift5_typeref: 0x50ce
-  __TEXT.__cstring: 0x477f
+841.4.10.1.1
+  __TEXT.__text: 0x89e74
+  __TEXT.__auth_stubs: 0x2180
+  __TEXT.__objc_methlist: 0x2c
+  __TEXT.__const: 0x27e8
+  __TEXT.__constg_swiftt: 0xb5c
+  __TEXT.__swift5_typeref: 0x50c2
+  __TEXT.__cstring: 0x4917
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0xb33
-  __TEXT.__swift5_fieldmd: 0xb14
-  __TEXT.__swift5_types: 0xac
-  __TEXT.__objc_classname: 0x62
-  __TEXT.__objc_methname: 0xdf0
-  __TEXT.__objc_methtype: 0x297
+  __TEXT.__swift5_reflstr: 0xb71
+  __TEXT.__swift5_fieldmd: 0xb64
+  __TEXT.__objc_methname: 0xa33
+  __TEXT.__swift5_types: 0xb0
+  __TEXT.__objc_classname: 0x2f
+  __TEXT.__objc_methtype: 0x174
+  __TEXT.__swift5_proto: 0x174
   __TEXT.__swift5_assocty: 0x3f0
-  __TEXT.__swift5_proto: 0x160
-  __TEXT.__swift5_capture: 0x1d8
+  __TEXT.__swift5_capture: 0x190
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x2350
-  __TEXT.__eh_frame: 0x1e24
-  __DATA_CONST.__auth_got: 0x1020
-  __DATA_CONST.__got: 0x610
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__unwind_info: 0x1754
+  __TEXT.__eh_frame: 0x215c
+  __DATA_CONST.__auth_got: 0x10c0
+  __DATA_CONST.__got: 0x648
   __DATA_CONST.__auth_ptr: 0xd8
-  __DATA_CONST.__const: 0x22c0
+  __DATA_CONST.__const: 0x2458
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xb60
-  __DATA.__objc_selrefs: 0x2e8
-  __DATA.__objc_protorefs: 0x28
+  __DATA.__objc_const: 0x890
+  __DATA.__objc_selrefs: 0x308
+  __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0x118
-  __DATA.__objc_data: 0x188
-  __DATA.__data: 0x2e70
-  __DATA.__bss: 0x2db8
+  __DATA.__objc_data: 0xd8
+  __DATA.__data: 0x2ea0
   __DATA.__common: 0x1e8
+  __DATA.__bss: 0x2fb8
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 32511D29-AAE3-386A-B7F2-B079E0E3B192
-  Functions: 1740
-  Symbols:   226
-  CStrings:  569
+  UUID: 2B3B211D-D4B5-33AA-9809-E881CE7454AA
+  Functions: 1801
+  Symbols:   230
+  CStrings:  548
 
Symbols:
+ _swift_continuation_resume
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
- _OBJC_CLASS_$__TtC10HomeWidget14HomeKitManager
- _OBJC_METACLASS_$__TtC10HomeWidget14HomeKitManager
CStrings:
+ "%s unable to get shared HMHomeManager instance"
+ "Finished lazy loading of [HMHome]"
+ "HFHomeKitDispatcher.Async"
+ "HomeWidget.HMHome"
+ "Initial Characteristic Fetch for "
+ "Initial Fetch for HomeWidget"
+ "Requesting all homes available in HomeKit"
+ "_TtC14HomeWidgetCore10HomeWidget"
+ "_homeManager"
+ "addFailureBlock:"
+ "addSuccessBlock:"
+ "allAccessoriesAndScenes(allHomes:homeIdentifier:matching:)"
+ "allHomesFuture"
+ "allHomesFuture canceled"
+ "allHomesFuture is nil and not available"
+ "allHomesFuture result=error"
+ "allHomesFuture result=success"
+ "allHomesFuture task canceled before resuming"
+ "cancel"
+ "sceneAndAccessoryUUIDs(for:)"
+ "setSynchronizesHomeDataModel:"
+ "sortedHomes"
+ "task"
- ".cxx_destruct"
- "HFHomeManagerObserver"
- "HMHomeManagerDelegatePrivate"
- "Returning manager %@"
- "We are going to set a `homeManagerCreationBlock`: %s"
- "_TtC10HomeWidget14HomeKitManager"
- "dealloc"
- "fetchPredictions(homeManager:home:)"
- "homeKitDispatcher:manager:didChangeHome:"
- "homeManager:didRemoveHomePermanently:"
- "homeManager:didUpdateAccessAllowedWhenLocked:"
- "homeManager:didUpdateDevices:"
- "homeManager:didUpdateHH2MigrationAvailableState:"
- "homeManager:didUpdateHH2MigrationInProgressState:"
- "homeManager:didUpdateHH2State:"
- "homeManager:didUpdateHomeSafetySecurityEnabled:"
- "homeManager:didUpdateLocationSensingAvailability:"
- "homeManager:didUpdateMultiUserStatus:reason:"
- "homeManager:didUpdateResidentEnabledForThisDevice:"
- "homeManager:didUpdateStateForIncomingInvitations:"
- "homeManager:didUpdateStatus:"
- "homeManager:didUpdateThisDeviceIsResidentCapable:"
- "homeManager:residentProvisioningStatusChanged:"
- "homeManagerDidEndBatchNotifications:"
- "homeManagerDidFinishInitialDatabaseLoad:"
- "homeManagerDidFinishUnknownChange:"
- "homeManagerDidRemoveCurrentAccessory:"
- "homeManagerDidUpdateApplicationData:"
- "homeManagerDidUpdateAssistantIdentifiers:"
- "homeManagerDidUpdateCurrentHome:"
- "homeManagerDidUpdateDataSyncInProgress:"
- "homeManagerDidUpdateDataSyncState:"
- "homeManagerWillStartBatchNotifications:"
- "sceneAndAccessoryUUIDs(for:homeManager:)"
- "v16@0:8"
- "v28@0:8@\"HMHomeManager\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"HMHomeManager\"16@\"NSArray\"24"
- "v32@0:8@\"HMHomeManager\"16@\"NSSet\"24"
- "v32@0:8@\"HMHomeManager\"16@\"NSUUID\"24"
- "v40@0:8@\"HFHomeKitDispatcher\"16@\"HMHomeManager\"24@\"HMHome\"32"
- "v40@0:8@\"HMHomeManager\"16q24@\"NSString\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16q24@32"

```
