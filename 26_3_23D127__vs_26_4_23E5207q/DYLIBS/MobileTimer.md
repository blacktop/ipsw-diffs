## MobileTimer

> `/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer`

```diff

-2303.3.1.0.0
-  __TEXT.__text: 0x10c488
-  __TEXT.__auth_stubs: 0x1920
-  __TEXT.__objc_methlist: 0xd98c
+2303.4.19.100.0
+  __TEXT.__text: 0x11334c
+  __TEXT.__auth_stubs: 0x18b0
+  __TEXT.__objc_methlist: 0xda5c
   __TEXT.__const: 0x1750
-  __TEXT.__oslogstring: 0x110c3
-  __TEXT.__cstring: 0x9826
-  __TEXT.__gcc_except_tab: 0x14a8
+  __TEXT.__oslogstring: 0x11153
+  __TEXT.__cstring: 0x9012
+  __TEXT.__gcc_except_tab: 0x14c4
   __TEXT.__dlopen_cstrs: 0x7e1
   __TEXT.__ustring: 0x1a
   __TEXT.__swift5_typeref: 0xa26

   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift_as_entry: 0x124
   __TEXT.__swift_as_ret: 0x124
-  __TEXT.__unwind_info: 0x46f0
-  __TEXT.__eh_frame: 0x3300
-  __TEXT.__objc_classname: 0x195a
-  __TEXT.__objc_methname: 0x181a0
-  __TEXT.__objc_methtype: 0x42ac
-  __TEXT.__objc_stubs: 0x11e80
-  __DATA_CONST.__got: 0xc78
-  __DATA_CONST.__const: 0x4300
+  __TEXT.__unwind_info: 0x4da0
+  __TEXT.__eh_frame: 0x3360
+  __TEXT.__objc_classname: 0x1be4
+  __TEXT.__objc_methname: 0x18a2c
+  __TEXT.__objc_methtype: 0x43ed
+  __TEXT.__objc_stubs: 0x12680
+  __DATA_CONST.__got: 0xc50
+  __DATA_CONST.__const: 0x4358
   __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6100
+  __DATA_CONST.__objc_selrefs: 0x6180
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x420
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0xca0
-  __AUTH_CONST.__const: 0x3d60
-  __AUTH_CONST.__cfstring: 0x6fe0
-  __AUTH_CONST.__objc_const: 0x290a8
+  __AUTH_CONST.__auth_got: 0xc68
+  __AUTH_CONST.__const: 0x3d20
+  __AUTH_CONST.__cfstring: 0x70e0
+  __AUTH_CONST.__objc_const: 0x29168
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x2f38
   __AUTH.__data: 0x4b8
-  __DATA.__objc_ivar: 0x96c
-  __DATA.__data: 0x2ba8
+  __DATA.__objc_ivar: 0x978
+  __DATA.__data: 0x2bb0
   __DATA.__common: 0x68
   __DATA.__bss: 0x1390
   __DATA_DIRTY.__objc_data: 0x18b0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 1253094D-8993-3330-9888-B611C9FF5949
-  Functions: 6734
-  Symbols:   18470
-  CStrings:  8435
+  UUID: 69DAC427-249C-3E98-8ADB-B70F558641FD
+  Functions: 6764
+  Symbols:   18709
+  CStrings:  8441
 
Symbols:
+ +[MTAlarm defaultCoordinationPolicy:]
+ +[MTSleepUtilities coordinationPolicyForOccurrence:]
+ +[MTUserNotificationCenter _canOptOutOfAlertCoordination]
+ +[MTUserNotificationCenter _categoryForWakeUpAlarm:]
+ -[MTAlarm coordinationPolicy]
+ -[MTAlarm setCoordinationPolicy:]
+ -[MTAlarmManager _initWithConnectionProvidingBlock:metrics:donatesAppIntents:]
+ -[MTAlarmManager _initWithConnectionProvidingBlock:metrics:donatesAppIntents:notificationCenter:]
+ -[MTAlarmManager dismissAlarm:dismissAction:]
+ -[MTAlarmManager donatesAppIntents]
+ -[MTAlarmManager initWithAppIntentDonations:]
+ -[MTAlarmManager initWithMetrics:donatesAppIntents:]
+ -[MTAlarmManager snoozeAlarm:snoozeAction:]
+ -[MTPairedDeviceListener hasActivePairedDeviceSupportingCoordination]
+ -[MTStopwatchServer registerStoreObserver:]
+ -[MTTimerManager _initWithConnectionProvidingBlock:metrics:donatesAppIntents:]
+ -[MTTimerManager _initWithConnectionProvidingBlock:metrics:donatesAppIntents:notificationCenter:]
+ -[MTTimerManager donatesAppIntents]
+ -[MTTimerManager initWithAppIntentDonations:]
+ -[MTTimerManager initWithMetrics:donatesAppIntents:]
+ -[MTTimerManager timerSyncWithIdentifier:]
+ GCC_except_table20
+ GCC_except_table35
+ GCC_except_table70
+ GCC_except_table79
+ GCC_except_table80
+ _MTAlarmCoordinationPolicyKey
+ _MTAlarmCoordinationPolicyString
+ _MTWakeUpAlarmNoSnoozeUncoordinatedCategory
+ _MTWakeUpAlarmUncoordinatedCategory
+ _OBJC_IVAR_$_MTAlarm._coordinationPolicy
+ _OBJC_IVAR_$_MTAlarmManager._donatesAppIntents
+ _OBJC_IVAR_$_MTTimerManager._donatesAppIntents
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_PROP_LIST_MTAlarmStorage.807
+ ___42-[MTTimerManager timerSyncWithIdentifier:]_block_invoke
+ ___43-[MTAlarmManager snoozeAlarm:snoozeAction:]_block_invoke
+ ___43-[MTAlarmManager snoozeAlarm:snoozeAction:]_block_invoke_2
+ ___43-[MTAlarmStorage updateSleepAlarms:source:]_block_invoke.449
+ ___44-[MTAlarmStorage _loadAlarmsWithCompletion:]_block_invoke.412
+ ___44-[MTAlarmStorage _loadAlarmsWithCompletion:]_block_invoke.421
+ ___44-[MTSleepSessionManager deviceFirstUnlocked]_block_invoke.368
+ ___45-[MTAlarmManager dismissAlarm:dismissAction:]_block_invoke
+ ___45-[MTAlarmManager dismissAlarm:dismissAction:]_block_invoke_2
+ ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.445
+ ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.445.cold.1
+ ___52-[MTAlarmManager initWithMetrics:donatesAppIntents:]_block_invoke
+ ___52-[MTAlarmManager initWithMetrics:donatesAppIntents:]_block_invoke_2
+ ___52-[MTTimerManager initWithMetrics:donatesAppIntents:]_block_invoke
+ ___52-[MTTimerManager initWithMetrics:donatesAppIntents:]_block_invoke_2
+ ___55-[MTAlarmStorage loadAlarmsFromCoreDataWithCompletion:]_block_invoke.427
+ ___64-[MTSleepSessionManager sleepSessionTracker:sessionDidComplete:]_block_invoke.350
+ ___69-[MTPairedDeviceListener hasActivePairedDeviceSupportingCoordination]_block_invoke
+ ___75-[MTUserNotificationCenter retrieveDelieveredNotificationForId:completion:]_block_invoke.125
+ ___97-[MTAlarmManager _initWithConnectionProvidingBlock:metrics:donatesAppIntents:notificationCenter:]_block_invoke
+ ___97-[MTAlarmManager _initWithConnectionProvidingBlock:metrics:donatesAppIntents:notificationCenter:]_block_invoke_2
+ ___97-[MTAlarmManager _initWithConnectionProvidingBlock:metrics:donatesAppIntents:notificationCenter:]_block_invoke_3
+ ___97-[MTAlarmManager _initWithConnectionProvidingBlock:metrics:donatesAppIntents:notificationCenter:]_block_invoke_4
+ ___97-[MTTimerManager _initWithConnectionProvidingBlock:metrics:donatesAppIntents:notificationCenter:]_block_invoke
+ ___97-[MTTimerManager _initWithConnectionProvidingBlock:metrics:donatesAppIntents:notificationCenter:]_block_invoke_2
+ ___97-[MTTimerManager _initWithConnectionProvidingBlock:metrics:donatesAppIntents:notificationCenter:]_block_invoke_3
+ ___97-[MTTimerManager _initWithConnectionProvidingBlock:metrics:donatesAppIntents:notificationCenter:]_block_invoke_4
+ ___block_descriptor_40_e8_32s_e27_"NAFuture"16?0"MTAlarm"8ls32l8
+ ___block_descriptor_48_e8_32s_e27_"NAFuture"16?0"MTAlarm"8ls32l8
+ ___block_literal_global.122
+ ___block_literal_global.133
+ ___block_literal_global.135
+ ___block_literal_global.137
+ ___block_literal_global.139
+ ___block_literal_global.349
+ ___block_literal_global.363
+ ___block_literal_global.372
+ ___block_literal_global.431
+ ___block_literal_global.452
+ ___block_literal_global.456
+ ___block_literal_global.51
+ ___block_literal_global.533
+ ___block_literal_global.74
+ ___block_literal_global.79
+ ___block_literal_global.82
+ _block_copy_helper.1001
+ _block_copy_helper.1018
+ _block_copy_helper.774
+ _block_copy_helper.785
+ _block_copy_helper.797
+ _block_copy_helper.809
+ _block_copy_helper.821
+ _block_copy_helper.833
+ _block_copy_helper.845
+ _block_copy_helper.857
+ _block_copy_helper.869
+ _block_copy_helper.881
+ _block_copy_helper.893
+ _block_copy_helper.905
+ _block_copy_helper.917
+ _block_copy_helper.929
+ _block_copy_helper.941
+ _block_copy_helper.953
+ _block_copy_helper.965
+ _block_copy_helper.977
+ _block_copy_helper.989
+ _block_descriptor.1003
+ _block_descriptor.1020
+ _block_descriptor.776
+ _block_descriptor.787
+ _block_descriptor.799
+ _block_descriptor.811
+ _block_descriptor.823
+ _block_descriptor.835
+ _block_descriptor.847
+ _block_descriptor.859
+ _block_descriptor.871
+ _block_descriptor.883
+ _block_descriptor.895
+ _block_descriptor.907
+ _block_descriptor.919
+ _block_descriptor.931
+ _block_descriptor.943
+ _block_descriptor.955
+ _block_descriptor.967
+ _block_descriptor.979
+ _block_descriptor.991
+ _block_destroy_helper.1002
+ _block_destroy_helper.1019
+ _block_destroy_helper.775
+ _block_destroy_helper.786
+ _block_destroy_helper.798
+ _block_destroy_helper.810
+ _block_destroy_helper.822
+ _block_destroy_helper.834
+ _block_destroy_helper.846
+ _block_destroy_helper.858
+ _block_destroy_helper.870
+ _block_destroy_helper.882
+ _block_destroy_helper.894
+ _block_destroy_helper.906
+ _block_destroy_helper.918
+ _block_destroy_helper.930
+ _block_destroy_helper.942
+ _block_destroy_helper.954
+ _block_destroy_helper.966
+ _block_destroy_helper.978
+ _block_destroy_helper.990
+ _kMTAlarmCoordinationPolicyEncodingKey
+ _keypath_get_selector_coordinationPolicy
+ _objc_msgSend$URLByAppendingPathComponent:isDirectory:
+ _objc_msgSend$URLForResource:withExtension:
+ _objc_msgSend$_canOptOutOfAlertCoordination
+ _objc_msgSend$_categoryForWakeUpAlarm:
+ _objc_msgSend$_initWithConnectionProvidingBlock:metrics:donatesAppIntents:
+ _objc_msgSend$_initWithConnectionProvidingBlock:metrics:donatesAppIntents:notificationCenter:
+ _objc_msgSend$archivedDataWithRootObject:
+ _objc_msgSend$attributes
+ _objc_msgSend$configuration
+ _objc_msgSend$containerURLForSecurityApplicationGroupIdentifier:
+ _objc_msgSend$coordinationPolicy
+ _objc_msgSend$coordinationPolicyForOccurrence:
+ _objc_msgSend$defaultCoordinationPolicy:
+ _objc_msgSend$deleteObject:
+ _objc_msgSend$didFinishLoadingStore
+ _objc_msgSend$dismissAlarm:dismissAction:
+ _objc_msgSend$executeRequest:error:
+ _objc_msgSend$hasActivePairedDeviceSupportingCoordination
+ _objc_msgSend$initFileURLWithPath:
+ _objc_msgSend$initWithBundleID:status:
+ _objc_msgSend$initWithContainerIdentifier:
+ _objc_msgSend$initWithContentsOfURL:
+ _objc_msgSend$initWithContext:
+ _objc_msgSend$initWithDouble:
+ _objc_msgSend$initWithEntity:insertIntoManagedObjectContext:
+ _objc_msgSend$initWithEntityName:
+ _objc_msgSend$initWithFetchRequest:
+ _objc_msgSend$initWithIdentifier:data:attributes:
+ _objc_msgSend$initWithMetrics:donatesAppIntents:
+ _objc_msgSend$initWithName:managedObjectModel:
+ _objc_msgSend$initWithType:subpredicates:
+ _objc_msgSend$initWithURL:
+ _objc_msgSend$initializeCloudKitSchemaWithOptions:error:
+ _objc_msgSend$isFavorite
+ _objc_msgSend$latest
+ _objc_msgSend$loadPersistentStoresWithCompletionHandler:
+ _objc_msgSend$newBackgroundContext
+ _objc_msgSend$save:
+ _objc_msgSend$setApsConnectionMachServiceName:
+ _objc_msgSend$setAttributes:
+ _objc_msgSend$setAutomaticallyMergesChangesFromParent:
+ _objc_msgSend$setBundleID:
+ _objc_msgSend$setCloudKitContainerOptions:
+ _objc_msgSend$setConfiguration:
+ _objc_msgSend$setCoordinationPolicy:
+ _objc_msgSend$setData:
+ _objc_msgSend$setIncludesSubentities:
+ _objc_msgSend$setIsFavorite:
+ _objc_msgSend$setLatest:
+ _objc_msgSend$setMediaItemIdentifier:
+ _objc_msgSend$setMtid:
+ _objc_msgSend$setPersistentStoreDescriptions:
+ _objc_msgSend$setPredicate:
+ _objc_msgSend$setResourceValue:forKey:error:
+ _objc_msgSend$setSoundType:
+ _objc_msgSend$setStatus:
+ _objc_msgSend$setTimer:
+ _objc_msgSend$setValidRecent:
+ _objc_msgSend$setVolumeLevel:
+ _objc_msgSend$signatureWithDomain:type:subType:detectedProcess:triggerThresholdValues:
+ _objc_msgSend$snapshotWithSignature:duration:event:payload:reply:
+ _objc_msgSend$snoozeAlarm:snoozeAction:
+ _objc_msgSend$status
+ _objc_msgSend$validRecent
+ _objc_msgSend$viewContext
+ _objc_msgSend$weakToStrongObjectsMapTable
+ _swift_release_n
- -[MTAlarmManager _initWithConnectionProvidingBlock:metrics:]
- -[MTAlarmManager _initWithConnectionProvidingBlock:metrics:notificationCenter:]
- -[MTTimerManager _initWithConnectionProvidingBlock:metrics:]
- -[MTTimerManager _initWithConnectionProvidingBlock:metrics:notificationCenter:]
- GCC_except_table11
- GCC_except_table58
- GCC_except_table69
- GCC_except_table75
- __OBJC_$_PROP_LIST_MTAlarmStorage.759
- ___34-[MTAlarmManager initWithMetrics:]_block_invoke
- ___34-[MTAlarmManager initWithMetrics:]_block_invoke_2
- ___34-[MTTimerManager initWithMetrics:]_block_invoke
- ___34-[MTTimerManager initWithMetrics:]_block_invoke_2
- ___43-[MTAlarmStorage updateSleepAlarms:source:]_block_invoke.401
- ___44-[MTAlarmStorage _loadAlarmsWithCompletion:]_block_invoke.364
- ___44-[MTAlarmStorage _loadAlarmsWithCompletion:]_block_invoke.373
- ___44-[MTSleepSessionManager deviceFirstUnlocked]_block_invoke.320
- ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.397
- ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.397.cold.1
- ___55-[MTAlarmStorage loadAlarmsFromCoreDataWithCompletion:]_block_invoke.379
- ___57-[MTAlarmManager snoozeAlarmWithIdentifier:snoozeAction:]_block_invoke_2
- ___59-[MTAlarmManager dismissAlarmWithIdentifier:dismissAction:]_block_invoke_2
- ___64-[MTSleepSessionManager sleepSessionTracker:sessionDidComplete:]_block_invoke.302
- ___75-[MTUserNotificationCenter retrieveDelieveredNotificationForId:completion:]_block_invoke.124
- ___79-[MTAlarmManager _initWithConnectionProvidingBlock:metrics:notificationCenter:]_block_invoke
- ___79-[MTAlarmManager _initWithConnectionProvidingBlock:metrics:notificationCenter:]_block_invoke_2
- ___79-[MTAlarmManager _initWithConnectionProvidingBlock:metrics:notificationCenter:]_block_invoke_3
- ___79-[MTAlarmManager _initWithConnectionProvidingBlock:metrics:notificationCenter:]_block_invoke_4
- ___79-[MTTimerManager _initWithConnectionProvidingBlock:metrics:notificationCenter:]_block_invoke
- ___79-[MTTimerManager _initWithConnectionProvidingBlock:metrics:notificationCenter:]_block_invoke_2
- ___79-[MTTimerManager _initWithConnectionProvidingBlock:metrics:notificationCenter:]_block_invoke_3
- ___79-[MTTimerManager _initWithConnectionProvidingBlock:metrics:notificationCenter:]_block_invoke_4
- ___block_descriptor_48_e8_32s40s_e27_"NAFuture"16?0"MTAlarm"8ls32l8s40l8
- ___block_literal_global.121
- ___block_literal_global.130
- ___block_literal_global.132
- ___block_literal_global.134
- ___block_literal_global.136
- ___block_literal_global.301
- ___block_literal_global.315
- ___block_literal_global.324
- ___block_literal_global.383
- ___block_literal_global.404
- ___block_literal_global.408
- ___block_literal_global.42
- ___block_literal_global.485
- ___block_literal_global.49
- ___block_literal_global.71
- ___block_literal_global.73
- ___block_literal_global.86
- _block_copy_helper.1016
- _block_copy_helper.20
- _block_copy_helper.772
- _block_copy_helper.783
- _block_copy_helper.795
- _block_copy_helper.807
- _block_copy_helper.819
- _block_copy_helper.831
- _block_copy_helper.843
- _block_copy_helper.855
- _block_copy_helper.867
- _block_copy_helper.879
- _block_copy_helper.891
- _block_copy_helper.903
- _block_copy_helper.915
- _block_copy_helper.927
- _block_copy_helper.939
- _block_copy_helper.951
- _block_copy_helper.963
- _block_copy_helper.975
- _block_copy_helper.987
- _block_copy_helper.999
- _block_descriptor.1001
- _block_descriptor.1018
- _block_descriptor.22
- _block_descriptor.774
- _block_descriptor.785
- _block_descriptor.797
- _block_descriptor.809
- _block_descriptor.821
- _block_descriptor.833
- _block_descriptor.845
- _block_descriptor.857
- _block_descriptor.869
- _block_descriptor.881
- _block_descriptor.893
- _block_descriptor.905
- _block_descriptor.917
- _block_descriptor.929
- _block_descriptor.941
- _block_descriptor.953
- _block_descriptor.965
- _block_descriptor.977
- _block_descriptor.989
- _block_destroy_helper.1000
- _block_destroy_helper.1017
- _block_destroy_helper.21
- _block_destroy_helper.773
- _block_destroy_helper.784
- _block_destroy_helper.796
- _block_destroy_helper.808
- _block_destroy_helper.820
- _block_destroy_helper.832
- _block_destroy_helper.844
- _block_destroy_helper.856
- _block_destroy_helper.868
- _block_destroy_helper.880
- _block_destroy_helper.892
- _block_destroy_helper.904
- _block_destroy_helper.916
- _block_destroy_helper.928
- _block_destroy_helper.940
- _block_destroy_helper.952
- _block_destroy_helper.964
- _block_destroy_helper.976
- _block_destroy_helper.988
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$dismissAlarmWithIdentifier:dismissAction:
- _objc_msgSend$snoozeAlarmWithIdentifier:snoozeAction:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ " \n \tcoordinationPolicy: "
+ "                              \n \tsleepAlarm: "
+ "%{public}@ has active paired watch supporting custom alert coordination"
+ "%{public}@ paired watch version is too old for custom alert coordination"
+ "%{public}@ snoozeAlarm:%{public}@ with action:%{public}@"
+ "@36@0:8@?16@24B32"
+ "@44@0:8@?16@24B32@36"
+ "AKCDAlarm"
+ "AKCDAttributes"
+ "C0F3C2C3-332F-481C-B7DE-7E80973B07BF"
+ "D0482616-332F-481C-B7DE-7E80973B07BF"
+ "D5834418-332F-481C-B7DE-7E80973B07BF"
+ "MTAlarmCoordinationPolicy"
+ "MTCDAlarm"
+ "MTCDSound"
+ "MTCDTimer"
+ "MTCoordinationPolicy"
+ "MTWakeUpAlarmNoSnoozeUncoordinatedCategory"
+ "MTWakeUpAlarmUncoordinatedCategory"
+ "TB,R,N,V_donatesAppIntents"
+ "TQ,N,V_coordinationPolicy"
+ "_canOptOutOfAlertCoordination"
+ "_categoryForWakeUpAlarm:"
+ "_coordinationPolicy"
+ "_donatesAppIntents"
+ "_initWithConnectionProvidingBlock:metrics:donatesAppIntents:"
+ "_initWithConnectionProvidingBlock:metrics:donatesAppIntents:notificationCenter:"
+ "coordinationPolicy"
+ "coordinationPolicyForOccurrence:"
+ "defaultCoordinationPolicy:"
+ "dismissAlarm:dismissAction:"
+ "donatesAppIntents"
+ "hasActivePairedDeviceSupportingCoordination"
+ "initWithAppIntentDonations:"
+ "initWithMetrics:donatesAppIntents:"
+ "optIn"
+ "optOut"
+ "registerStoreObserver:"
+ "setCoordinationPolicy:"
+ "snoozeAlarm:snoozeAction:"
+ "timerSyncWithIdentifier:"
- "                               \n \tsleepAlarm: "
- "%{public}@ snoozeAlarmWithIdentifier:%{public}@"
- "C0F3C2C3-0CDE-4DF9-A95A-789AC9A0348B"
- "D5834418-F4A0-4C74-AA38-8ED5F7765BD1"

```
