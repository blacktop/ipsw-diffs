## MobileTimer

> `/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer`

```diff

-2295.0.0.0.0
-  __TEXT.__text: 0xf7868
-  __TEXT.__auth_stubs: 0x15f0
-  __TEXT.__objc_methlist: 0xd590
-  __TEXT.__const: 0x1220
-  __TEXT.__oslogstring: 0xf8d0
-  __TEXT.__cstring: 0x95c6
-  __TEXT.__gcc_except_tab: 0x1264
-  __TEXT.__dlopen_cstrs: 0x7ed
+2298.1.0.0.0
+  __TEXT.__text: 0x1044dc
+  __TEXT.__auth_stubs: 0x17b0
+  __TEXT.__objc_methlist: 0xd70c
+  __TEXT.__const: 0x12c0
+  __TEXT.__oslogstring: 0x10f43
+  __TEXT.__cstring: 0x9866
+  __TEXT.__gcc_except_tab: 0x1290
+  __TEXT.__dlopen_cstrs: 0x837
   __TEXT.__ustring: 0x1a
-  __TEXT.__swift5_typeref: 0x6d0
-  __TEXT.__swift5_reflstr: 0x228
+  __TEXT.__swift5_typeref: 0x85c
+  __TEXT.__swift5_reflstr: 0x282
   __TEXT.__swift5_assocty: 0xd8
-  __TEXT.__constg_swiftt: 0x4a4
-  __TEXT.__swift5_fieldmd: 0x298
+  __TEXT.__constg_swiftt: 0x548
+  __TEXT.__swift5_fieldmd: 0x328
   __TEXT.__swift5_proto: 0x68
-  __TEXT.__swift5_types: 0x58
-  __TEXT.__swift5_capture: 0xbe4
+  __TEXT.__swift5_types: 0x60
+  __TEXT.__swift5_capture: 0xf74
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift_as_entry: 0x100
-  __TEXT.__swift_as_ret: 0x104
-  __TEXT.__unwind_info: 0x41f8
-  __TEXT.__eh_frame: 0x2ec0
-  __TEXT.__objc_classname: 0x193b
-  __TEXT.__objc_methname: 0x17ca2
-  __TEXT.__objc_methtype: 0x41f6
-  __TEXT.__objc_stubs: 0x11a60
-  __DATA_CONST.__got: 0xbd0
-  __DATA_CONST.__const: 0x4108
-  __DATA_CONST.__objc_classlist: 0x688
+  __TEXT.__swift_as_entry: 0x104
+  __TEXT.__swift_as_ret: 0x108
+  __TEXT.__unwind_info: 0x4808
+  __TEXT.__eh_frame: 0x3018
+  __TEXT.__objc_classname: 0x1965
+  __TEXT.__objc_methname: 0x17e0c
+  __TEXT.__objc_methtype: 0x4210
+  __TEXT.__objc_stubs: 0x11c80
+  __DATA_CONST.__got: 0xc38
+  __DATA_CONST.__const: 0x41f0
+  __DATA_CONST.__objc_classlist: 0x690
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x358
+  __DATA_CONST.__objc_protolist: 0x368
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5f80
-  __DATA_CONST.__objc_protorefs: 0x88
+  __DATA_CONST.__objc_selrefs: 0x6010
+  __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x420
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0xb08
-  __AUTH_CONST.__const: 0x2cf0
+  __AUTH_CONST.__auth_got: 0xbe8
+  __AUTH_CONST.__const: 0x3960
   __AUTH_CONST.__cfstring: 0x7000
-  __AUTH_CONST.__objc_const: 0x28e38
+  __AUTH_CONST.__objc_const: 0x29158
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x2d18
-  __AUTH.__data: 0x3a0
-  __DATA.__objc_ivar: 0x944
-  __DATA.__data: 0x2978
+  __AUTH.__objc_data: 0x2df0
+  __AUTH.__data: 0x3c8
+  __DATA.__objc_ivar: 0x954
+  __DATA.__data: 0x2ab0
   __DATA.__common: 0x68
-  __DATA.__bss: 0x1100
+  __DATA.__bss: 0x1190
   __DATA_DIRTY.__objc_data: 0x18b0
   __DATA_DIRTY.__bss: 0x288
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 8E3E6D22-CCAA-38FD-8A8A-52926BF9C69F
-  Functions: 6254
-  Symbols:   17834
-  CStrings:  8264
+  UUID: 6447BBA7-F937-3CA8-90DE-466E1B3F53A0
+  Functions: 6529
+  Symbols:   18221
+  CStrings:  8382
 
Symbols:
+ +[MTUserNotificationCenter isPairedWatchIncompatibleWithAlarmKit]
+ +[MTUserNotificationCenter setCommonContent:alert:]
+ +[MTUtilities isCarPlayConnected]
+ +[MTUtilities isRunningUnitTest]
+ -[MTActivityCoordinator clearLegacySessions]
+ -[MTActivityCoordinator clearStaleAlarmSessions]
+ -[MTActivityCoordinator clearStaleTimerSessions]
+ -[MTActivityCoordinator handleAlarmStorageReady]
+ -[MTActivityCoordinator handleTimerStorageReady]
+ -[MTAlarmKit didFinishLoadingStore]
+ -[MTAlarmServer conductor]
+ -[MTAlarmServer setConductor:]
+ -[MTAlarmStorage conductor]
+ -[MTAlarmStorage didFinishLoadingStore]
+ -[MTAlarmStorage loadStore]
+ -[MTAlarmStorage registerStoreLoadCompletion:]
+ -[MTAlarmStorage setConductor:]
+ -[MTTimerServer conductor]
+ -[MTTimerServer setConductor:]
+ -[MTTimerStorage conductor]
+ -[MTTimerStorage didFinishLoadingStore]
+ -[MTTimerStorage loadStore]
+ -[MTTimerStorage registerStoreLoadCompletion:]
+ -[MTTimerStorage setConductor:]
+ -[MTUserNotificationCenter firingNotificationDestinations]
+ GCC_except_table15
+ GCC_except_table33
+ GCC_except_table35
+ GCC_except_table41
+ GCC_except_table45
+ GCC_except_table47
+ GCC_except_table49
+ GCC_except_table75
+ GCC_except_table77
+ GCC_except_table89
+ GCC_except_table91
+ _CarKitLibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_UNNotificationIcon
+ _OBJC_CLASS_$__TtC11MobileTimer13VoidConductor
+ _OBJC_CLASS_$__TtC11MobileTimer15StringConductor
+ _OBJC_IVAR_$_MTAlarmServer._conductor
+ _OBJC_IVAR_$_MTAlarmStorage._conductor
+ _OBJC_IVAR_$_MTTimerServer._conductor
+ _OBJC_IVAR_$_MTTimerStorage._conductor
+ _OBJC_METACLASS_$__TtC11MobileTimer13VoidConductor
+ _OBJC_METACLASS_$__TtC11MobileTimer15StringConductor
+ __DATA__TtC11MobileTimer13VoidConductor
+ __DATA__TtC11MobileTimer15StringConductor
+ __INSTANCE_METHODS__TtC11MobileTimer13VoidConductor
+ __INSTANCE_METHODS__TtC11MobileTimer15StringConductor
+ __IVARS__TtC11MobileTimer13VoidConductor
+ __IVARS__TtC11MobileTimer15StringConductor
+ __METACLASS_DATA__TtC11MobileTimer13VoidConductor
+ __METACLASS_DATA__TtC11MobileTimer15StringConductor
+ __OBJC_$_PROP_LIST_MTAlarmStorage.746
+ __OBJC_$_PROP_LIST_MTTimerStorage.342
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__TtP11MobileTimer21MTCDDataStoreObserver_
+ __OBJC_$_PROTOCOL_METHOD_TYPES__TtP11MobileTimer21MTCDDataStoreObserver_
+ __OBJC_LABEL_PROTOCOL_$__TtP11MobileTimer21MTCDDataStoreObserver_
+ __OBJC_PROTOCOL_$__TtP11MobileTimer21MTCDDataStoreObserver_
+ __PROTOCOL_INSTANCE_METHODS__TtP11MobileTimer21MTCDDataStoreObserver_
+ __PROTOCOL_METHOD_TYPES__TtP11MobileTimer21MTCDDataStoreObserver_
+ __PROTOCOL__TtP11MobileTimer21MTCDDataStoreObserver_
+ ___27-[MTAgent restoreDidFinish]_block_invoke.39
+ ___27-[MTAgent restoreDidFinish]_block_invoke_2
+ ___35-[MTObserverStore currentObservers]_block_invoke
+ ___41-[MTAlarmServer addAlarm:withCompletion:]_block_invoke
+ ___41-[MTAlarmServer addAlarm:withCompletion:]_block_invoke.19
+ ___41-[MTAlarmServer addAlarm:withCompletion:]_block_invoke.19.cold.1
+ ___41-[MTAlarmServer getAlarmsWithCompletion:]_block_invoke
+ ___41-[MTAlarmServer getAlarmsWithCompletion:]_block_invoke.16
+ ___41-[MTAlarmServer getAlarmsWithCompletion:]_block_invoke.16.cold.1
+ ___41-[MTTimerServer addTimer:withCompletion:]_block_invoke
+ ___41-[MTTimerServer addTimer:withCompletion:]_block_invoke.19
+ ___41-[MTTimerServer addTimer:withCompletion:]_block_invoke.19.cold.1
+ ___41-[MTTimerServer getTimersWithCompletion:]_block_invoke
+ ___41-[MTTimerServer getTimersWithCompletion:]_block_invoke.16
+ ___41-[MTTimerServer getTimersWithCompletion:]_block_invoke.16.cold.1
+ ___44-[MTActivityCoordinator clearLegacySessions]_block_invoke
+ ___44-[MTAlarmServer removeAlarm:withCompletion:]_block_invoke
+ ___44-[MTAlarmServer removeAlarm:withCompletion:]_block_invoke.21
+ ___44-[MTAlarmServer removeAlarm:withCompletion:]_block_invoke.21.cold.1
+ ___44-[MTAlarmServer updateAlarm:withCompletion:]_block_invoke
+ ___44-[MTAlarmServer updateAlarm:withCompletion:]_block_invoke.20
+ ___44-[MTAlarmServer updateAlarm:withCompletion:]_block_invoke.20.cold.1
+ ___44-[MTAlarmStorage _loadAlarmsWithCompletion:]_block_invoke.372
+ ___44-[MTSleepSessionManager deviceFirstUnlocked]_block_invoke.320
+ ___44-[MTTimerServer removeTimer:withCompletion:]_block_invoke
+ ___44-[MTTimerServer removeTimer:withCompletion:]_block_invoke.21
+ ___44-[MTTimerServer removeTimer:withCompletion:]_block_invoke.21.cold.1
+ ___44-[MTTimerServer updateTimer:withCompletion:]_block_invoke
+ ___44-[MTTimerServer updateTimer:withCompletion:]_block_invoke.20
+ ___44-[MTTimerServer updateTimer:withCompletion:]_block_invoke.20.cold.1
+ ___46-[MTAlarmServer nextSleepAlarmWithCompletion:]_block_invoke
+ ___46-[MTAlarmServer nextSleepAlarmWithCompletion:]_block_invoke.28
+ ___46-[MTAlarmServer nextSleepAlarmWithCompletion:]_block_invoke.28.cold.1
+ ___46-[MTAlarmStorage registerStoreLoadCompletion:]_block_invoke
+ ___46-[MTTimerStorage registerStoreLoadCompletion:]_block_invoke
+ ___48-[MTActivityCoordinator clearStaleAlarmSessions]_block_invoke
+ ___48-[MTActivityCoordinator clearStaleAlarmSessions]_block_invoke.5
+ ___48-[MTActivityCoordinator clearStaleAlarmSessions]_block_invoke.7
+ ___48-[MTActivityCoordinator clearStaleAlarmSessions]_block_invoke.9
+ ___48-[MTActivityCoordinator clearStaleAlarmSessions]_block_invoke_2
+ ___48-[MTActivityCoordinator clearStaleAlarmSessions]_block_invoke_2.10
+ ___48-[MTActivityCoordinator clearStaleAlarmSessions]_block_invoke_2.10.cold.1
+ ___48-[MTActivityCoordinator clearStaleAlarmSessions]_block_invoke_2.6
+ ___48-[MTActivityCoordinator clearStaleTimerSessions]_block_invoke
+ ___48-[MTActivityCoordinator clearStaleTimerSessions]_block_invoke.21
+ ___48-[MTActivityCoordinator clearStaleTimerSessions]_block_invoke.23
+ ___48-[MTActivityCoordinator clearStaleTimerSessions]_block_invoke_2
+ ___48-[MTActivityCoordinator clearStaleTimerSessions]_block_invoke_2.22
+ ___48-[MTActivityCoordinator clearStaleTimerSessions]_block_invoke_2.24
+ ___48-[MTActivityCoordinator clearStaleTimerSessions]_block_invoke_2.24.cold.1
+ ___48-[MTActivityCoordinator clearStaleTimerSessions]_block_invoke_3
+ ___49-[MTAlarmServer updateSleepAlarmsWithCompletion:]_block_invoke
+ ___49-[MTAlarmServer updateSleepAlarmsWithCompletion:]_block_invoke.31
+ ___49-[MTAlarmServer updateSleepAlarmsWithCompletion:]_block_invoke.31.cold.1
+ ___49-[MTTimerServer getTimerDurationsWithCompletion:]_block_invoke
+ ___49-[MTTimerServer getTimerDurationsWithCompletion:]_block_invoke.27
+ ___49-[MTTimerServer getTimerDurationsWithCompletion:]_block_invoke.27.cold.1
+ ___50-[MTTimerServer addRecentDuration:withCompletion:]_block_invoke
+ ___50-[MTTimerServer addRecentDuration:withCompletion:]_block_invoke.28
+ ___50-[MTTimerServer addRecentDuration:withCompletion:]_block_invoke.28.cold.1
+ ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.395
+ ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.395.cold.1
+ ___51-[MTTimerServer saveLatestDuration:withCompletion:]_block_invoke
+ ___51-[MTTimerServer saveLatestDuration:withCompletion:]_block_invoke.32
+ ___51-[MTTimerServer saveLatestDuration:withCompletion:]_block_invoke.32.cold.1
+ ___52-[MTTimerServer addFavoriteDuration:withCompletion:]_block_invoke
+ ___52-[MTTimerServer addFavoriteDuration:withCompletion:]_block_invoke.30
+ ___52-[MTTimerServer addFavoriteDuration:withCompletion:]_block_invoke.30.cold.1
+ ___53-[MTTimerServer removeRecentDuration:withCompletion:]_block_invoke
+ ___53-[MTTimerServer removeRecentDuration:withCompletion:]_block_invoke.29
+ ___53-[MTTimerServer removeRecentDuration:withCompletion:]_block_invoke.29.cold.1
+ ___55-[MTTimerServer removeFavoriteDuration:withCompletion:]_block_invoke
+ ___55-[MTTimerServer removeFavoriteDuration:withCompletion:]_block_invoke.31
+ ___55-[MTTimerServer removeFavoriteDuration:withCompletion:]_block_invoke.31.cold.1
+ ___58-[MTAlarmServer resetSleepAlarmSnoozeStateWithCompletion:]_block_invoke
+ ___58-[MTAlarmServer resetSleepAlarmSnoozeStateWithCompletion:]_block_invoke.32
+ ___58-[MTAlarmServer resetSleepAlarmSnoozeStateWithCompletion:]_block_invoke.32.cold.1
+ ___58-[MTTimerServer repeatTimerWithIdentifier:withCompletion:]_block_invoke.25
+ ___58-[MTTimerServer repeatTimerWithIdentifier:withCompletion:]_block_invoke.26
+ ___58-[MTTimerServer repeatTimerWithIdentifier:withCompletion:]_block_invoke.26.cold.1
+ ___59-[MTTimerServer dismissTimerWithIdentifier:withCompletion:]_block_invoke.22
+ ___59-[MTTimerServer dismissTimerWithIdentifier:withCompletion:]_block_invoke.24
+ ___59-[MTTimerServer dismissTimerWithIdentifier:withCompletion:]_block_invoke.24.cold.1
+ ___64-[MTSleepSessionManager sleepSessionTracker:sessionDidComplete:]_block_invoke.302
+ ___71-[MTAlarmServer snoozeAlarmWithIdentifier:snoozeAction:withCompletion:]_block_invoke.22
+ ___71-[MTAlarmServer snoozeAlarmWithIdentifier:snoozeAction:withCompletion:]_block_invoke.24
+ ___71-[MTAlarmServer snoozeAlarmWithIdentifier:snoozeAction:withCompletion:]_block_invoke.24.cold.1
+ ___73-[MTAlarmServer dismissAlarmWithIdentifier:dismissAction:withCompletion:]_block_invoke.25
+ ___73-[MTAlarmServer dismissAlarmWithIdentifier:dismissAction:withCompletion:]_block_invoke.26
+ ___73-[MTAlarmServer dismissAlarmWithIdentifier:dismissAction:withCompletion:]_block_invoke.26.cold.1
+ ___CarKitLibraryCore_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48bs_e8_v12?0B8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40bs48bs_e8_v12?0B8ls40l8s32l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.111
+ ___block_literal_global.254
+ ___block_literal_global.270
+ ___block_literal_global.276
+ ___block_literal_global.301
+ ___block_literal_global.315
+ ___block_literal_global.324
+ ___block_literal_global.362
+ ___block_literal_global.375
+ ___block_literal_global.381
+ ___block_literal_global.401
+ ___block_literal_global.405
+ ___block_literal_global.43
+ ___block_literal_global.482
+ ___getCARSessionStatusClass_block_invoke
+ ___getCARSessionStatusClass_block_invoke.cold.1
+ ___getCARSessionStatusClass_block_invoke.cold.2
+ ___swift_instantiateGenericMetadata
+ ___unnamed_3
+ _audit_stringCarKit
+ _block_copy_helper.19
+ _block_copy_helper.25
+ _block_copy_helper.34
+ _block_copy_helper.753
+ _block_copy_helper.764
+ _block_copy_helper.776
+ _block_copy_helper.788
+ _block_copy_helper.800
+ _block_copy_helper.812
+ _block_copy_helper.824
+ _block_copy_helper.836
+ _block_copy_helper.848
+ _block_copy_helper.860
+ _block_copy_helper.872
+ _block_copy_helper.884
+ _block_copy_helper.896
+ _block_copy_helper.908
+ _block_copy_helper.920
+ _block_copy_helper.932
+ _block_copy_helper.944
+ _block_copy_helper.956
+ _block_copy_helper.968
+ _block_copy_helper.980
+ _block_copy_helper.997
+ _block_descriptor.21
+ _block_descriptor.27
+ _block_descriptor.36
+ _block_descriptor.755
+ _block_descriptor.766
+ _block_descriptor.778
+ _block_descriptor.790
+ _block_descriptor.802
+ _block_descriptor.814
+ _block_descriptor.826
+ _block_descriptor.838
+ _block_descriptor.850
+ _block_descriptor.862
+ _block_descriptor.874
+ _block_descriptor.886
+ _block_descriptor.898
+ _block_descriptor.910
+ _block_descriptor.922
+ _block_descriptor.934
+ _block_descriptor.946
+ _block_descriptor.958
+ _block_descriptor.970
+ _block_descriptor.982
+ _block_descriptor.999
+ _block_destroy_helper.20
+ _block_destroy_helper.26
+ _block_destroy_helper.35
+ _block_destroy_helper.754
+ _block_destroy_helper.765
+ _block_destroy_helper.777
+ _block_destroy_helper.789
+ _block_destroy_helper.801
+ _block_destroy_helper.813
+ _block_destroy_helper.825
+ _block_destroy_helper.837
+ _block_destroy_helper.849
+ _block_destroy_helper.861
+ _block_destroy_helper.873
+ _block_destroy_helper.885
+ _block_destroy_helper.897
+ _block_destroy_helper.909
+ _block_destroy_helper.921
+ _block_destroy_helper.933
+ _block_destroy_helper.945
+ _block_destroy_helper.957
+ _block_destroy_helper.969
+ _block_destroy_helper.981
+ _block_destroy_helper.998
+ _flat unique 11MobileTimer21MTCDDataStoreObserver_p
+ _getCARSessionStatusClass.softClass
+ _kMTAlarmServerLoadTimeout
+ _kMTAlarmStorageLoadTimeout
+ _kMTTimerServerLoadTimeout
+ _kMTTimerStorageLoadTimeout
+ _malloc
+ _objc_msgSend$clearLegacySessions
+ _objc_msgSend$clearStaleAlarmSessions
+ _objc_msgSend$clearStaleTimerSessions
+ _objc_msgSend$currentSession
+ _objc_msgSend$firingNotificationDestinations
+ _objc_msgSend$handleAlarmStorageReady
+ _objc_msgSend$handleTimerStorageReady
+ _objc_msgSend$hasActivePairedDevice
+ _objc_msgSend$iconForApplicationIdentifier:
+ _objc_msgSend$initAndWaitUntilSessionUpdated
+ _objc_msgSend$isCarPlayConnected
+ _objc_msgSend$isPairedWatchIncompatibleWithAlarmKit
+ _objc_msgSend$isRunningUnitTest
+ _objc_msgSend$loadStore
+ _objc_msgSend$registerReplyPublisherWithTimeOut:completion:
+ _objc_msgSend$registerStoreLoadCompletion:
+ _objc_msgSend$saveLatestDuration:withCompletion:source:
+ _objc_msgSend$send
+ _objc_msgSend$setAlarmKitObserver:
+ _objc_msgSend$setAlarmObserver:
+ _objc_msgSend$setCommonContent:alert:
+ _objc_msgSend$setIcon:
+ _objc_msgSend$setSubtitle:
+ _objc_msgSend$setTimerObserver:
+ _objectdestroy.110Tm
+ _objectdestroy.189Tm
+ _objectdestroy.215Tm
+ _objectdestroy.228Tm
+ _objectdestroy.263Tm
+ _objectdestroy.321Tm
+ _objectdestroy.354Tm
+ _objectdestroy.362Tm
+ _objectdestroy.38Tm
+ _objectdestroy.414Tm
+ _objectdestroy.51Tm
+ _objectdestroy.69Tm
+ _swift_allocateGenericClassMetadata
+ _swift_bridgeObjectRelease_n
+ _swift_coroFrameAlloc
+ _swift_getGenericMetadata
+ _swift_initClassMetadata2
+ _swift_isEscapingClosureAtFileLocation
+ _swift_task_isCurrentExecutor
+ _swift_task_reportUnexpectedExecutor
+ _swift_unknownObjectWeakAssign
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _symbolic $s11MobileTimer21MTCDDataStoreObserverP
+ _symbolic B0
+ _symbolic Ig_
+ _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
+ _symbolic Say_____G So17OS_dispatch_queueC8DispatchE10AttributesV
+ _symbolic So17OS_dispatch_queueC
+ _symbolic _____ 11MobileTimer13VoidConductorC
+ _symbolic _____ 11MobileTimer15StringConductorC
+ _symbolic ______pSg 11MobileTimer21MTCDDataStoreObserverP
+ _symbolic ______pSgXw 11MobileTimer21MTCDDataStoreObserverP
+ _symbolic _____ySSG 11MobileTimer9ConductorC
+ _symbolic _____y______y______y______y______yyt_____GG_____GGSo17OS_dispatch_queueCG 7Combine10PublishersO7TimeoutV AC5FirstV AC14SetFailureTypeV AC5ShareC AA18PassthroughSubjectC s5NeverO 11MobileTimer15ConductorStatusO
+ _symbolic _____y______y______y______yyt_____GG_____GG 7Combine10PublishersO5FirstV AC14SetFailureTypeV AC5ShareC AA18PassthroughSubjectC s5NeverO 11MobileTimer15ConductorStatusO
+ _symbolic _____y______y______yyt_____GG_____G 7Combine10PublishersO14SetFailureTypeV AC5ShareC AA18PassthroughSubjectC s5NeverO 11MobileTimer15ConductorStatusO
+ _symbolic _____y______yyt_____GG 7Combine10PublishersO5ShareC AA18PassthroughSubjectC s5NeverO
+ _symbolic _____yx_____G 7Combine18PassthroughSubjectC s5NeverO
+ _symbolic _____yytG 11MobileTimer9ConductorC
+ _symbolic _____yyt_____G 7Combine18PassthroughSubjectC s5NeverO
+ _symbolic x
- +[MTUserNotificationCenter setCommonContent:alert:hasPairedWatchSupportingAlarmKit:]
- -[MTActivityCoordinator clearOutdatedSessions]
- -[MTActivityCoordinator handleActiveAlarmSessions]
- -[MTActivityCoordinator handleActiveTimerSessions]
- -[MTAlarm(MTScheduling) isRunningUnitTest]
- -[MTAlarmKit handleSystemReady]
- -[MTAlarmServer resetSleepAlarmSnoozeStateWithCompletion:].cold.1
- -[MTAlarmServer updateSleepAlarmsWithCompletion:].cold.1
- -[MTUserNotificationCenter conditionalAlarmPlaybackDestinations]
- -[MTUserNotificationCenter conditionalTimerPlaybackDestinations]
- -[MTUserNotificationCenter hasPairedWatchSupportingAlarmKit]
- GCC_except_table27
- GCC_except_table32
- GCC_except_table39
- GCC_except_table42
- GCC_except_table50
- GCC_except_table90
- _OBJC_CLASS_$__TtC11MobileTimer9Conductor
- _OBJC_METACLASS_$__TtC11MobileTimer9Conductor
- __DATA__TtC11MobileTimer9Conductor
- __INSTANCE_METHODS__TtC11MobileTimer9Conductor
- __METACLASS_DATA__TtC11MobileTimer9Conductor
- __OBJC_$_PROP_LIST_MTAlarmStorage.731
- __OBJC_$_PROP_LIST_MTTimerStorage.329
- ___44-[MTAlarmStorage _loadAlarmsWithCompletion:]_block_invoke.368
- ___44-[MTSleepSessionManager deviceFirstUnlocked]_block_invoke.317
- ___46-[MTActivityCoordinator clearOutdatedSessions]_block_invoke
- ___50-[MTActivityCoordinator handleActiveAlarmSessions]_block_invoke
- ___50-[MTActivityCoordinator handleActiveAlarmSessions]_block_invoke.5
- ___50-[MTActivityCoordinator handleActiveAlarmSessions]_block_invoke.7
- ___50-[MTActivityCoordinator handleActiveAlarmSessions]_block_invoke.9
- ___50-[MTActivityCoordinator handleActiveAlarmSessions]_block_invoke_2
- ___50-[MTActivityCoordinator handleActiveAlarmSessions]_block_invoke_2.10
- ___50-[MTActivityCoordinator handleActiveAlarmSessions]_block_invoke_2.10.cold.1
- ___50-[MTActivityCoordinator handleActiveAlarmSessions]_block_invoke_2.6
- ___50-[MTActivityCoordinator handleActiveTimerSessions]_block_invoke
- ___50-[MTActivityCoordinator handleActiveTimerSessions]_block_invoke.21
- ___50-[MTActivityCoordinator handleActiveTimerSessions]_block_invoke.23
- ___50-[MTActivityCoordinator handleActiveTimerSessions]_block_invoke_2
- ___50-[MTActivityCoordinator handleActiveTimerSessions]_block_invoke_2.22
- ___50-[MTActivityCoordinator handleActiveTimerSessions]_block_invoke_2.24
- ___50-[MTActivityCoordinator handleActiveTimerSessions]_block_invoke_2.24.cold.1
- ___50-[MTActivityCoordinator handleActiveTimerSessions]_block_invoke_3
- ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.390
- ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.390.cold.1
- ___64-[MTSleepSessionManager sleepSessionTracker:sessionDidComplete:]_block_invoke.299
- ___block_literal_global.108
- ___block_literal_global.19
- ___block_literal_global.230
- ___block_literal_global.246
- ___block_literal_global.252
- ___block_literal_global.298
- ___block_literal_global.312
- ___block_literal_global.321
- ___block_literal_global.338
- ___block_literal_global.351
- ___block_literal_global.376
- ___block_literal_global.396
- ___block_literal_global.400
- ___block_literal_global.477
- _objc_msgSend$clearOutdatedSessions
- _objc_msgSend$conditionalAlarmPlaybackDestinations
- _objc_msgSend$conditionalTimerPlaybackDestinations
- _objc_msgSend$handleActiveAlarmSessions
- _objc_msgSend$handleActiveTimerSessions
- _objc_msgSend$hasPairedWatchSupportingAlarmKit
- _objc_msgSend$setCommonContent:alert:hasPairedWatchSupportingAlarmKit:
- _objectdestroy.159Tm
- _objectdestroy.185Tm
- _objectdestroy.198Tm
- _objectdestroy.21Tm
- _objectdestroy.233Tm
- _objectdestroy.293Tm
- _objectdestroy.326Tm
- _objectdestroy.334Tm
- _objectdestroy.386Tm
- _objectdestroy.39Tm
- _objectdestroy.80Tm
- _objectdestroy.8Tm
CStrings:
+ "%{public}@ addAlarm reply publisher ready, proceeding with request"
+ "%{public}@ addAlarm reply publisher timed out, replying with error"
+ "%{public}@ addAlarm system not ready, registering reply publisher"
+ "%{public}@ addFavoriteDuration reply publisher ready, proceeding with request"
+ "%{public}@ addFavoriteDuration reply publisher timed out, replying with error"
+ "%{public}@ addFavoriteDuration system not ready, registering reply publisher"
+ "%{public}@ addRecentDuration reply publisher ready, proceeding with request"
+ "%{public}@ addRecentDuration reply publisher timed out, replying with error"
+ "%{public}@ addRecentDuration system not ready, registering reply publisher"
+ "%{public}@ addTimer reply publisher ready, proceeding with request"
+ "%{public}@ addTimer reply publisher timed out, replying with error"
+ "%{public}@ addTimer system not ready, registering reply publisher"
+ "%{public}@ data store is already ready, executing completion"
+ "%{public}@ didFinishLoadingStore"
+ "%{public}@ dismissAlarmWithIdentifier reply publisher ready, proceeding with request"
+ "%{public}@ dismissAlarmWithIdentifier reply publisher timed out, replying with error"
+ "%{public}@ dismissAlarmWithIdentifier system not ready, registering reply publisher"
+ "%{public}@ dismissTimerWithIdentifier reply publisher ready, proceeding with request"
+ "%{public}@ dismissTimerWithIdentifier reply publisher timed out, replying with error"
+ "%{public}@ dismissTimerWithIdentifier system not ready, registering reply publisher"
+ "%{public}@ executing alarm store load completion with status: %i"
+ "%{public}@ executing timer store load completion with status: %i"
+ "%{public}@ getAlarmsWithCompletion reply publisher ready, proceeding with request"
+ "%{public}@ getAlarmsWithCompletion reply publisher timed out, replying with error"
+ "%{public}@ getAlarmsWithCompletion system not ready, registering reply publisher"
+ "%{public}@ getTimerDurationsWithCompletion reply publisher ready, proceeding with request"
+ "%{public}@ getTimerDurationsWithCompletion reply publisher timed out, replying with error"
+ "%{public}@ getTimerDurationsWithCompletion system not ready, registering reply publisher"
+ "%{public}@ getTimersWithCompletion reply publisher ready, proceeding with request"
+ "%{public}@ getTimersWithCompletion reply publisher timed out, replying with error"
+ "%{public}@ getTimersWithCompletion system not ready, registering reply publisher"
+ "%{public}@ nextSleepAlarmWithCompletion reply publisher ready, proceeding with request"
+ "%{public}@ nextSleepAlarmWithCompletion reply publisher timed out, replying with error"
+ "%{public}@ nextSleepAlarmWithCompletion system not ready, registering reply publisher"
+ "%{public}@ received didFinishLoadingStore, proceeding to start AlarmKit"
+ "%{public}@ registerStoreLoadCompletion does not support core data, bypassing store load"
+ "%{public}@ registering alarm store load completion, core data store ready: %i"
+ "%{public}@ registering timer store load completion, core data store ready: %i, ordered timers: %@"
+ "%{public}@ removeAlarm reply publisher ready, proceeding with request"
+ "%{public}@ removeAlarm reply publisher timed out, replying with error"
+ "%{public}@ removeAlarm system not ready, registering reply publisher"
+ "%{public}@ removeFavoriteDuration reply publisher ready, proceeding with request"
+ "%{public}@ removeFavoriteDuration reply publisher timed out, replying with error"
+ "%{public}@ removeFavoriteDuration system not ready, registering reply publisher"
+ "%{public}@ removeRecentDuration reply publisher ready, proceeding with request"
+ "%{public}@ removeRecentDuration reply publisher timed out, replying with error"
+ "%{public}@ removeRecentDuration system not ready, registering reply publisher"
+ "%{public}@ removeTimer reply publisher ready, proceeding with request"
+ "%{public}@ removeTimer reply publisher timed out, replying with error"
+ "%{public}@ removeTimer system not ready, registering reply publisher"
+ "%{public}@ repeatTimerWithIdentifier reply publisher timed out, replying with error"
+ "%{public}@ repeatTimerWithIdentifier system not ready, registering reply publisher"
+ "%{public}@ resetSleepAlarmSnoozeStateWithCompletion could not reset sleep alarms snooze state:%{public}@"
+ "%{public}@ resetSleepAlarmSnoozeStateWithCompletion reply publisher ready, proceeding with request"
+ "%{public}@ resetSleepAlarmSnoozeStateWithCompletion system not ready, registering reply publisher"
+ "%{public}@ saveLatestDuration reply publisher ready, proceeding with request"
+ "%{public}@ saveLatestDuration reply publisher timed out, replying with error"
+ "%{public}@ saveLatestDuration system not ready, registering reply publisher"
+ "%{public}@ snoozeAlarmWithIdentifier reply publisher ready, proceeding with request"
+ "%{public}@ snoozeAlarmWithIdentifier reply publisher timed out, replying with error"
+ "%{public}@ snoozeAlarmWithIdentifier system not ready, registering reply publisher"
+ "%{public}@ updateAlarm reply publisher ready, proceeding with request"
+ "%{public}@ updateAlarm reply publisher timed out, replying with error"
+ "%{public}@ updateAlarm system not ready, registering reply publisher"
+ "%{public}@ updateSleepAlarmsWithCompletion could not refresh sleep alarms:%{public}@"
+ "%{public}@ updateSleepAlarmsWithCompletion reply publisher ready, proceeding with request"
+ "%{public}@ updateSleepAlarmsWithCompletion system not ready, registering reply publisher"
+ "%{public}@ updateTimer reply publisher ready, proceeding with request"
+ "%{public}@ updateTimer reply publisher timed out, replying with error"
+ "%{public}@ updateTimer system not ready, registering reply publisher"
+ "%{public}@: clearLegacySessions"
+ "%{public}@: clearStaleAlarmSessions"
+ "%{public}@: clearStaleTimerSessions"
+ "%{public}@: handle alarm storage ready received"
+ "%{public}@: handle timer storage ready received"
+ "%{public}@: is connected to CarPlay: %d"
+ "?"
+ "@\"_TtC11MobileTimer13VoidConductor\""
+ "@\"_TtC11MobileTimer15StringConductor\""
+ "CARSessionStatus"
+ "Calling loadStore"
+ "Class getCARSessionStatusClass(void)_block_invoke"
+ "Error loading core datat store: %@"
+ "Failed to initialize core data store actor: %@"
+ "Informing observers of data store load, %s, %s, %s"
+ "Initialized core data store actor"
+ "Loading data store"
+ "MobileTimer/MTCDDataStore.swift"
+ "T@\"<_TtP11MobileTimer21MTCDDataStoreObserver_>\",N,W,ValarmKitObserver"
+ "T@\"<_TtP11MobileTimer21MTCDDataStoreObserver_>\",N,W,ValarmObserver"
+ "T@\"<_TtP11MobileTimer21MTCDDataStoreObserver_>\",N,W,VtimerObserver"
+ "T@\"_TtC11MobileTimer13VoidConductor\",&,N,V_conductor"
+ "T@\"_TtC11MobileTimer15StringConductor\",&,N,V_conductor"
+ "_TtC11MobileTimer13VoidConductor"
+ "_TtC11MobileTimer15StringConductor"
+ "_TtP11MobileTimer21MTCDDataStoreObserver_"
+ "alarmKitObserver"
+ "alarmObserver"
+ "calloutQueue"
+ "clearLegacySessions"
+ "clearStaleAlarmSessions"
+ "clearStaleTimerSessions"
+ "com.apple.mobiletimer.MTCDDataStore.callout"
+ "com.apple.mobiletimer.MTCDDataStore.queue"
+ "currentSession"
+ "didFinishLoadingStore"
+ "firingNotificationDestinations"
+ "handleAlarmStorageReady"
+ "handleTimerStorageReady"
+ "iconForApplicationIdentifier:"
+ "initAndWaitUntilSessionUpdated"
+ "isCarPlayConnected"
+ "isPairedWatchIncompatibleWithAlarmKit"
+ "loadStore"
+ "registerReplyPublisherWithTimeOut:completion:"
+ "registerStoreLoadCompletion:"
+ "send"
+ "setAlarmKitObserver:"
+ "setAlarmObserver:"
+ "setCommonContent:alert:"
+ "setIcon:"
+ "setSubtitle:"
+ "setTimerObserver:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/CarKit.framework/CarKit"
+ "storeLoaded"
+ "timerObserver"
+ "void *CarKitLibrary(void)"
- "%{public}@ could not refresh sleep alarms:%{public}@"
- "%{public}@ could not reset sleep alarms snooze state:%{public}@"
- "%{public}@: clearOutdatedSessions"
- "%{public}@: handleAlarmSessions"
- "@\"_TtC11MobileTimer9Conductor\""
- "Failed to load core data actor: %@"
- "T@\"_TtC11MobileTimer9Conductor\",&,N,V_conductor"
- "_TtC11MobileTimer9Conductor"
- "clearOutdatedSessions"
- "conditionalAlarmPlaybackDestinations"
- "conditionalTimerPlaybackDestinations"
- "handleActiveAlarmSessions"
- "handleActiveTimerSessions"
- "hasPairedWatchSupportingAlarmKit"
- "setCommonContent:alert:hasPairedWatchSupportingAlarmKit:"
- "v36@0:8@16@24B32"

```
