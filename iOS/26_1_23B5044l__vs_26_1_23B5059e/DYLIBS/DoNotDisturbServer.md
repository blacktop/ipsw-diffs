## DoNotDisturbServer

> `/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer`

```diff

-468.1.6.0.0
-  __TEXT.__text: 0xc36c4
-  __TEXT.__auth_stubs: 0x1360
-  __TEXT.__objc_methlist: 0xa9e8
+468.1.12.0.0
+  __TEXT.__text: 0xc30fc
+  __TEXT.__auth_stubs: 0x1350
+  __TEXT.__objc_methlist: 0xa9c0
   __TEXT.__const: 0x530
-  __TEXT.__cstring: 0x8924
-  __TEXT.__oslogstring: 0x11390
+  __TEXT.__cstring: 0x8914
+  __TEXT.__oslogstring: 0x11170
   __TEXT.__gcc_except_tab: 0x1068
   __TEXT.__dlopen_cstrs: 0x59
   __TEXT.__constg_swiftt: 0x14c

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x2c
-  __TEXT.__unwind_info: 0x2850
+  __TEXT.__unwind_info: 0x2848
   __TEXT.__eh_frame: 0x530
   __TEXT.__objc_classname: 0x28e9
-  __TEXT.__objc_methname: 0x19a75
+  __TEXT.__objc_methname: 0x19a09
   __TEXT.__objc_methtype: 0x7696
-  __TEXT.__objc_stubs: 0x10bc0
-  __DATA_CONST.__got: 0xe60
-  __DATA_CONST.__const: 0x25d0
+  __TEXT.__objc_stubs: 0x10b80
+  __DATA_CONST.__got: 0xe68
+  __DATA_CONST.__const: 0x25d8
   __DATA_CONST.__objc_classlist: 0x5f8
   __DATA_CONST.__objc_catlist: 0x148
   __DATA_CONST.__objc_protolist: 0x3d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4cb8
+  __DATA_CONST.__objc_selrefs: 0x4cb0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x3e0
   __DATA_CONST.__objc_arraydata: 0x330
-  __AUTH_CONST.__auth_got: 0x9c0
+  __AUTH_CONST.__auth_got: 0x9b8
   __AUTH_CONST.__const: 0x10a8
   __AUTH_CONST.__cfstring: 0x7980
   __AUTH_CONST.__objc_const: 0x25fb0

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D21AE9FA-528B-3227-A68D-A9FFD4FE451D
-  Functions: 3809
-  Symbols:   14323
-  CStrings:  7635
+  UUID: 41F19F2B-D7FB-3C08-BFFF-762F87775D94
+  Functions: 3804
+  Symbols:   14313
+  CStrings:  7627
 
Symbols:
+ -[DNDSModeAssertionStore(SysdiagnoseRecord) sysdiagnoseDictionaryRepresentation:]
+ -[DNDSWorkoutTriggerManager _isWorkoutDNDMigrated]
+ -[DNDSWorkoutTriggerManager _setWorkoutDNDIsMigrated]
+ _OBJC_CLASS_$_STFocusStatusDomainData
+ ___62-[DNDSWorkoutTriggerManager _configureWorkoutTriggerWithMode:]_block_invoke.35
+ ___91-[DNDSServer _queue_updateScheduleManagerLifetimeMonitorsAndStateForReason:source:options:]_block_invoke.198
+ ___block_literal_global.209
+ ___block_literal_global.221
+ ___block_literal_global.224
+ ___block_literal_global.228
+ ___block_literal_global.81
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_DoNotDisturbServer
+ _objc_msgSend$_isWorkoutDNDMigrated
+ _objc_msgSend$_setWorkoutDNDIsMigrated
+ _objc_msgSend$setData:
+ _objc_msgSend$sysdiagnoseDictionaryRepresentation:
- -[DNDSModeAssertionStore(SysdiagnoseRecord) sysdiagnoseDictionaryRepresentation]
- -[DNDSWorkoutTriggerManager _npsQueue_refreshForNanoPreferenceChange]
- -[DNDSWorkoutTriggerManager _refreshForNanoPreferenceChange]
- -[DNDSWorkoutTriggerManager _setWorkoutDNDNanoPreferenceEnabled:]
- -[DNDSWorkoutTriggerManager _updateNanoPreferencesForRefreshWithModeConfiguration:]
- -[DNDSWorkoutTriggerManager dealloc]
- _CFNotificationCenterPostNotification
- _DNDWorkoutStateObserverCallback
- ___60-[DNDSWorkoutTriggerManager _refreshForNanoPreferenceChange]_block_invoke
- ___62-[DNDSWorkoutTriggerManager _configureWorkoutTriggerWithMode:]_block_invoke.37
- ___91-[DNDSServer _queue_updateScheduleManagerLifetimeMonitorsAndStateForReason:source:options:]_block_invoke.197
- ___block_literal_global.208
- ___block_literal_global.220
- ___block_literal_global.223
- ___block_literal_global.227
- ___block_literal_global.78
- _objc_msgSend$_npsQueue_refreshForNanoPreferenceChange
- _objc_msgSend$_refreshForNanoPreferenceChange
- _objc_msgSend$_setWorkoutDNDNanoPreferenceEnabled:
- _objc_msgSend$_updateNanoPreferencesForRefreshWithModeConfiguration:
- _objc_msgSend$setWorkoutTriggerEnabled:forWorkoutTriggerManager:
- _objc_msgSend$sysdiagnoseDictionaryRepresentation
CStrings:
+ "_isWorkoutDNDMigrated"
+ "_setWorkoutDNDIsMigrated"
+ "currentData has been set to nil"
+ "setData:"
+ "sysdiagnoseDictionaryRepresentation:"
+ "workoutDNDMigrated"
- "Create mode for workout trigger in response to nano preference update."
- "Disable workout DND preference for workout trigger mode deletion."
- "Disable workout DND preference to match disabled workout trigger."
- "Enable workout DND preference to match enabled workout trigger."
- "Refreshed workout trigger for nano preferences update: mode=%{public}@"
- "Requesting workout trigger refresh due to nano preferences change"
- "Update workout trigger for mode in response to nano preference update: enabled=%{public}@ mode=%{public}@"
- "Workout trigger already matches nano preferences update: mode=%{public}@"
- "WorkoutDNDStateChangedNotification"
- "_npsQueue_refreshForNanoPreferenceChange"
- "_refreshForNanoPreferenceChange"
- "_setWorkoutDNDNanoPreferenceEnabled:"
- "_updateNanoPreferencesForRefreshWithModeConfiguration:"
- "sysdiagnoseDictionaryRepresentation"

```
