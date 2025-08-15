## HomeKitMetrics

> `/System/Library/PrivateFrameworks/HomeKitMetrics.framework/HomeKitMetrics`

```diff

-1092.4.10.0.0
-  __TEXT.__text: 0x13694
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0x18a4
+1124.5.8.1.1
+  __TEXT.__text: 0x15030
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__objc_methlist: 0x1a3c
   __TEXT.__const: 0x30
-  __TEXT.__gcc_except_tab: 0x550
-  __TEXT.__cstring: 0x6b0
-  __TEXT.__oslogstring: 0xe20
-  __TEXT.__unwind_info: 0x724
-  __TEXT.__objc_classname: 0x62c
-  __TEXT.__objc_methname: 0x3d80
-  __TEXT.__objc_methtype: 0xcd9
-  __TEXT.__objc_stubs: 0x2e80
+  __TEXT.__gcc_except_tab: 0x6b8
+  __TEXT.__cstring: 0x6d4
+  __TEXT.__oslogstring: 0xe59
+  __TEXT.__unwind_info: 0x7fc
+  __TEXT.__objc_classname: 0x67d
+  __TEXT.__objc_methname: 0x42ac
+  __TEXT.__objc_methtype: 0xdad
+  __TEXT.__objc_stubs: 0x3180
   __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x3e0
-  __DATA_CONST.__objc_classlist: 0x180
+  __DATA_CONST.__const: 0x430
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xc0
+  __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3780
-  __DATA_CONST.__objc_selrefs: 0xf00
+  __DATA_CONST.__objc_const: 0x3c60
+  __DATA_CONST.__objc_selrefs: 0xfe0
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x230
+  __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__objc_const: 0x1558
+  __AUTH_CONST.__objc_const: 0x1630
   __AUTH_CONST.__cfstring: 0xa00
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__const: 0x220
+  __AUTH_CONST.__const: 0x240
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x280
-  __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x228
-  __DATA.__objc_superrefs: 0x120
-  __DATA.__objc_ivar: 0x220
-  __DATA.__data: 0x928
-  __DATA.__bss: 0x58
+  __AUTH_CONST.__auth_got: 0x298
+  __AUTH.__objc_data: 0x6e0
+  __DATA.__objc_ivar: 0x250
+  __DATA.__data: 0x988
+  __DATA.__bss: 0x68
   __DATA_DIRTY.__objc_data: 0x910
-  __DATA_DIRTY.__bss: 0xa0
+  __DATA_DIRTY.__bss: 0x98
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6BFB8E5A-20C8-3861-B1DA-3FBF578FD87D
-  Functions: 528
-  Symbols:   2325
-  CStrings:  1179
+  UUID: 0C6D22A8-5506-30E3-BDE9-EDAE1740FFA7
+  Functions: 561
+  Symbols:   2472
+  CStrings:  1238
 
Symbols:
+ +[HMMDateProvider startOfDayForDate:]
+ +[HMMStandardCounterGroup groupFromSpecifier:dateProvider:partitionProvider:coreDataStorage:]
+ +[HMMStandardCounterGroup groupFromSpecifier:dateProvider:partitionProvider:coreDataStorage:uptimeProvider:]
+ +[HMMUptimeProvider sharedInstance]
+ -[HMMBufferingLogEventSubmitter .cxx_destruct]
+ -[HMMBufferingLogEventSubmitter initWithBufferSize:]
+ -[HMMBufferingLogEventSubmitter init]
+ -[HMMBufferingLogEventSubmitter processLogEventsWithSubmitter:]
+ -[HMMBufferingLogEventSubmitter submitLogEvent:]
+ -[HMMBufferingLogEventSubmitter submitLogEvent:error:]
+ -[HMMCountersManager addEphemeralContainerWithName:]
+ -[HMMCountersManager deactivateEphemeralContainerWithName:]
+ -[HMMCountersManager managedEphemeralContainerForName:]
+ -[HMMCountersManager managedEphemeralContainers]
+ -[HMMCountersManager removeEphemeralContainerWithName:]
+ -[HMMDailyPartitionProvider datePartitionContainingDate:]
+ -[HMMDailyPartitionProvider datePartitionWithOffset:fromDatePartition:]
+ -[HMMManagedEphemeralContainer .cxx_destruct]
+ -[HMMManagedEphemeralContainer activeDuration]
+ -[HMMManagedEphemeralContainer containerName]
+ -[HMMManagedEphemeralContainer initWithContainerName:]
+ -[HMMManagedEphemeralContainer isActive]
+ -[HMMManagedEphemeralContainer setActive:]
+ -[HMMManagedEphemeralContainer setStartTime:]
+ -[HMMManagedEphemeralContainer startTime]
+ -[HMMStandardCounterGroup addDuration:toCounter:endTime:]
+ -[HMMStandardCounterGroup addEphemeralContainerWithName:]
+ -[HMMStandardCounterGroup dateProvider]
+ -[HMMStandardCounterGroup deactivateEphemeralContainerWithName:]
+ -[HMMStandardCounterGroup durationForCounter:inDatePartition:]
+ -[HMMStandardCounterGroup durationForCounter:inEphemeralContainer:]
+ -[HMMStandardCounterGroup incrementCounter:inDatePartition:by:]
+ -[HMMStandardCounterGroup initWithCoreDataGroup:dateProvider:partitionProvider:coreDataStorage:]
+ -[HMMStandardCounterGroup initWithCoreDataGroup:dateProvider:partitionProvider:coreDataStorage:uptimeProvider:]
+ -[HMMStandardCounterGroup pauseDurationCounter:]
+ -[HMMStandardCounterGroup removeEphemeralContainerWithName:]
+ -[HMMStandardCounterGroup resumeDurationCounter:]
+ -[HMMStandardCounterGroup runningDurationCounters]
+ -[HMMStandardCounterGroup updateAllDurationCounters]
+ -[HMMStandardCounterGroup updateCountersBeforeSave]
+ -[HMMStandardCounterGroup updateDurationCounter:]
+ -[HMMStandardCounterGroup uptimeProvider]
+ -[HMMStandardStatisticsGroup addEphemeralContainerWithName:]
+ -[HMMStandardStatisticsGroup deactivateEphemeralContainerWithName:]
+ -[HMMStandardStatisticsGroup removeEphemeralContainerWithName:]
+ -[HMMUptimeProvider uptime]
+ GCC_except_table111
+ GCC_except_table136
+ GCC_except_table140
+ GCC_except_table180
+ GCC_except_table181
+ GCC_except_table182
+ GCC_except_table184
+ GCC_except_table188
+ GCC_except_table192
+ GCC_except_table195
+ GCC_except_table196
+ GCC_except_table202
+ GCC_except_table235
+ GCC_except_table236
+ GCC_except_table237
+ GCC_except_table255
+ GCC_except_table256
+ GCC_except_table257
+ GCC_except_table259
+ GCC_except_table261
+ GCC_except_table269
+ GCC_except_table270
+ GCC_except_table272
+ GCC_except_table274
+ GCC_except_table275
+ GCC_except_table276
+ GCC_except_table281
+ GCC_except_table282
+ GCC_except_table289
+ GCC_except_table293
+ GCC_except_table295
+ GCC_except_table331
+ GCC_except_table515
+ GCC_except_table526
+ GCC_except_table527
+ GCC_except_table528
+ GCC_except_table529
+ GCC_except_table530
+ GCC_except_table531
+ GCC_except_table537
+ GCC_except_table540
+ GCC_except_table546
+ _HMFUptime
+ _OBJC_CLASS_$_HMMBufferingLogEventSubmitter
+ _OBJC_CLASS_$_HMMManagedEphemeralContainer
+ _OBJC_CLASS_$_HMMUptimeProvider
+ _OBJC_CLASS_$_NSMergePolicy
+ _OBJC_IVAR_$_HMMBufferingLogEventSubmitter._bufferSize
+ _OBJC_IVAR_$_HMMBufferingLogEventSubmitter._bufferedLogEvents
+ _OBJC_IVAR_$_HMMBufferingLogEventSubmitter._lock
+ _OBJC_IVAR_$_HMMBufferingLogEventSubmitter._submitter
+ _OBJC_IVAR_$_HMMCountersManager._managedContainersByName
+ _OBJC_IVAR_$_HMMManagedEphemeralContainer._active
+ _OBJC_IVAR_$_HMMManagedEphemeralContainer._activeDuration
+ _OBJC_IVAR_$_HMMManagedEphemeralContainer._containerName
+ _OBJC_IVAR_$_HMMManagedEphemeralContainer._lock
+ _OBJC_IVAR_$_HMMManagedEphemeralContainer._startTime
+ _OBJC_IVAR_$_HMMStandardCounterGroup._dateProvider
+ _OBJC_IVAR_$_HMMStandardCounterGroup._runningDurationCounters
+ _OBJC_IVAR_$_HMMStandardCounterGroup._uptimeProvider
+ _OBJC_METACLASS_$_HMMBufferingLogEventSubmitter
+ _OBJC_METACLASS_$_HMMManagedEphemeralContainer
+ _OBJC_METACLASS_$_HMMUptimeProvider
+ __OBJC_$_CLASS_METHODS_HMMUptimeProvider
+ __OBJC_$_CLASS_PROP_LIST_HMMUptimeProvider
+ __OBJC_$_INSTANCE_METHODS_HMMBufferingLogEventSubmitter
+ __OBJC_$_INSTANCE_METHODS_HMMManagedEphemeralContainer
+ __OBJC_$_INSTANCE_METHODS_HMMUptimeProvider
+ __OBJC_$_INSTANCE_VARIABLES_HMMBufferingLogEventSubmitter
+ __OBJC_$_INSTANCE_VARIABLES_HMMManagedEphemeralContainer
+ __OBJC_$_PROP_LIST_HMMBufferingLogEventSubmitter
+ __OBJC_$_PROP_LIST_HMMManagedEphemeralContainer
+ __OBJC_$_PROP_LIST_HMMRTCSession.116
+ __OBJC_$_PROP_LIST_HMMUptimeProvider
+ __OBJC_$_PROP_LIST_HMMUptimeProvider.49
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMUptimeProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMUptimeProvider
+ __OBJC_$_PROTOCOL_REFS_HMMUptimeProvider
+ __OBJC_CLASS_PROTOCOLS_$_HMMBufferingLogEventSubmitter
+ __OBJC_CLASS_PROTOCOLS_$_HMMUptimeProvider
+ __OBJC_CLASS_RO_$_HMMBufferingLogEventSubmitter
+ __OBJC_CLASS_RO_$_HMMManagedEphemeralContainer
+ __OBJC_CLASS_RO_$_HMMUptimeProvider
+ __OBJC_LABEL_PROTOCOL_$_HMMUptimeProvider
+ __OBJC_METACLASS_RO_$_HMMBufferingLogEventSubmitter
+ __OBJC_METACLASS_RO_$_HMMManagedEphemeralContainer
+ __OBJC_METACLASS_RO_$_HMMUptimeProvider
+ __OBJC_PROTOCOL_$_HMMUptimeProvider
+ ___108+[HMMStandardCounterGroup groupFromSpecifier:dateProvider:partitionProvider:coreDataStorage:uptimeProvider:]_block_invoke
+ ___35+[HMMUptimeProvider sharedInstance]_block_invoke
+ ___52-[HMMStandardCounterGroup updateAllDurationCounters]_block_invoke
+ ___63-[HMMStandardCounterGroup incrementCounter:inDatePartition:by:]_block_invoke
+ ___Block_byref_object_copy_.1183
+ ___Block_byref_object_copy_.761
+ ___Block_byref_object_dispose_.1184
+ ___Block_byref_object_dispose_.762
+ ___block_descriptor_56_e8_32s40s_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s_e32_v16?0"NSManagedObjectContext"8ls32l8s40l8s48l8
+ ___block_literal_global.1317
+ ___block_literal_global.1585
+ ___block_literal_global.181
+ ___block_literal_global.1889
+ ___block_literal_global.1998
+ ___block_literal_global.300
+ ___block_literal_global.696
+ ___block_literal_global.97
+ ___block_literal_global.993
+ __unnamed_array_storage.773
+ _logCategory._hmf_once_t1.1888
+ _logCategory._hmf_once_v2.1890
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend$addDuration:toCounter:endTime:
+ _objc_msgSend$addEphemeralContainerWithName:
+ _objc_msgSend$addTimeInterval:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$containerName
+ _objc_msgSend$counterGroups
+ _objc_msgSend$datePartitionContainingDate:
+ _objc_msgSend$datePartitionWithOffset:fromDatePartition:
+ _objc_msgSend$deactivateEphemeralContainerWithName:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$groupFromSpecifier:dateProvider:partitionProvider:coreDataStorage:
+ _objc_msgSend$groupFromSpecifier:dateProvider:partitionProvider:coreDataStorage:uptimeProvider:
+ _objc_msgSend$incrementCounter:inDatePartition:by:
+ _objc_msgSend$initWithBufferSize:
+ _objc_msgSend$initWithContainerName:
+ _objc_msgSend$initWithCoreDataGroup:dateProvider:partitionProvider:coreDataStorage:
+ _objc_msgSend$initWithCoreDataGroup:dateProvider:partitionProvider:coreDataStorage:uptimeProvider:
+ _objc_msgSend$mergeByPropertyObjectTrumpMergePolicy
+ _objc_msgSend$removeEphemeralContainerWithName:
+ _objc_msgSend$runningDurationCounters
+ _objc_msgSend$setMergePolicy:
+ _objc_msgSend$updateAllDurationCounters
+ _objc_msgSend$updateCountersBeforeSave
+ _objc_msgSend$updateDurationCounter:
+ _objc_msgSend$uptime
+ _objc_msgSend$uptimeProvider
+ _objc_msgSend$valueForCounter:inDatePartition:
+ _objc_msgSend$valueForCounter:inEphemeralContainer:
+ _sharedInstance._hmf_once_t0.1316
+ _sharedInstance._hmf_once_t0.1997
+ _sharedInstance._hmf_once_t0.354
+ _sharedInstance._hmf_once_v1.1318
+ _sharedInstance._hmf_once_v1.1999
+ _sharedInstance._hmf_once_v1.355
- +[HMMLogEventDispatcher initialize]
- +[HMMLogEventDispatcher sharedInstance]
- +[HMMStandardCounterGroup groupFromSpecifier:partitionProvider:coreDataStorage:]
- -[HMMCountersManager activeEphemeralContainers]
- -[HMMCountersManager addEphemeralContainer:]
- -[HMMCountersManager deactivateEphemeralContainer:]
- -[HMMCountersManager removeEphemeralContainer:]
- -[HMMStandardCounterGroup addEphemeralContainer:]
- -[HMMStandardCounterGroup deactivateEphemeralContainer:]
- -[HMMStandardCounterGroup initWithCoreDataGroup:partitionProvider:coreDataStorage:]
- -[HMMStandardCounterGroup removeEphemeralContainer:]
- -[HMMStandardCounterGroup setCoreDataGroup:]
- -[HMMStandardStatisticsGroup addEphemeralContainer:]
- -[HMMStandardStatisticsGroup deactivateEphemeralContainer:]
- -[HMMStandardStatisticsGroup removeEphemeralContainer:]
- GCC_except_table108
- GCC_except_table133
- GCC_except_table137
- GCC_except_table173
- GCC_except_table174
- GCC_except_table175
- GCC_except_table176
- GCC_except_table177
- GCC_except_table185
- GCC_except_table187
- GCC_except_table191
- GCC_except_table197
- GCC_except_table232
- GCC_except_table233
- GCC_except_table234
- GCC_except_table246
- GCC_except_table247
- GCC_except_table248
- GCC_except_table249
- GCC_except_table250
- GCC_except_table251
- GCC_except_table260
- GCC_except_table262
- GCC_except_table266
- GCC_except_table273
- GCC_except_table308
- GCC_except_table494
- GCC_except_table495
- GCC_except_table496
- GCC_except_table497
- GCC_except_table498
- GCC_except_table504
- GCC_except_table507
- _OBJC_CLASS_$_NSMutableSet
- _OBJC_IVAR_$_HMMCountersManager._ephemeralContainerNames
- __OBJC_$_CLASS_METHODS_HMMLogEventDispatcher
- __OBJC_$_PROP_LIST_HMMRTCSession.115
- ___47-[HMMStandardCounterGroup incrementCounter:by:]_block_invoke
- ___80+[HMMStandardCounterGroup groupFromSpecifier:partitionProvider:coreDataStorage:]_block_invoke
- ___Block_byref_object_copy_.1051
- ___Block_byref_object_copy_.707
- ___Block_byref_object_dispose_.1052
- ___Block_byref_object_dispose_.708
- ___block_literal_global.1182
- ___block_literal_global.1446
- ___block_literal_global.164
- ___block_literal_global.1744
- ___block_literal_global.1852
- ___block_literal_global.247
- ___block_literal_global.640
- ___block_literal_global.861
- __unnamed_array_storage.724
- _logCategory._hmf_once_t1.1743
- _logCategory._hmf_once_v2.1745
- _objc_msgSend$addEphemeralContainer:
- _objc_msgSend$deactivateEphemeralContainer:
- _objc_msgSend$removeEphemeralContainer:
- _objc_msgSend$set
- _sharedDispatcher
- _sharedInstance._hmf_once_t0.1181
- _sharedInstance._hmf_once_t0.1851
- _sharedInstance._hmf_once_v1.1183
- _sharedInstance._hmf_once_v1.1853
CStrings:
+ "!"
+ "%{public}@Log event not buffered. Buffer full, size: %ld"
+ "("
+ "@\"<HMMUptimeProvider>\""
+ "@\"NSDate\"24@0:8@\"NSDate\"16"
+ "@\"NSDate\"32@0:8q16@\"NSDate\"24"
+ "@56@0:8@16@24@32@40@48"
+ "HMMBufferingLogEventSubmitter"
+ "HMMManagedEphemeralContainer"
+ "HMMUptimeProvider"
+ "T@\"<HMMUptimeProvider>\",R,N,V_uptimeProvider"
+ "T@\"HMMCoreDataNamedGroup\",R,N,V_coreDataGroup"
+ "T@\"HMMUptimeProvider\",R,N"
+ "T@\"NSMutableDictionary\",R,N,V_runningDurationCounters"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C,N,V_containerName"
+ "Td,N,V_startTime"
+ "Td,R,N"
+ "Td,R,N,V_activeDuration"
+ "_activeDuration"
+ "_bufferSize"
+ "_bufferedLogEvents"
+ "_containerName"
+ "_managedContainersByName"
+ "_runningDurationCounters"
+ "_uptimeProvider"
+ "activeDuration"
+ "addDuration:toCounter:endTime:"
+ "addEphemeralContainerWithName:"
+ "addTimeInterval:"
+ "arrayWithCapacity:"
+ "containerName"
+ "d32@0:8@\"NSString\"16@\"NSDate\"24"
+ "d32@0:8@\"NSString\"16@\"NSString\"24"
+ "d32@0:8@16@24"
+ "datePartitionContainingDate:"
+ "datePartitionWithOffset:fromDatePartition:"
+ "deactivateEphemeralContainerWithName:"
+ "doubleValue"
+ "durationForCounter:inDatePartition:"
+ "durationForCounter:inEphemeralContainer:"
+ "groupFromSpecifier:dateProvider:partitionProvider:coreDataStorage:"
+ "groupFromSpecifier:dateProvider:partitionProvider:coreDataStorage:uptimeProvider:"
+ "incrementCounter:inDatePartition:by:"
+ "initWithBufferSize:"
+ "initWithContainerName:"
+ "initWithCoreDataGroup:dateProvider:partitionProvider:coreDataStorage:"
+ "initWithCoreDataGroup:dateProvider:partitionProvider:coreDataStorage:uptimeProvider:"
+ "managedEphemeralContainerForName:"
+ "managedEphemeralContainers"
+ "mergeByPropertyObjectTrumpMergePolicy"
+ "pauseDurationCounter:"
+ "processLogEventsWithSubmitter:"
+ "removeEphemeralContainerWithName:"
+ "resumeDurationCounter:"
+ "runningDurationCounters"
+ "setMergePolicy:"
+ "updateAllDurationCounters"
+ "updateCountersBeforeSave"
+ "updateDurationCounter:"
+ "uptime"
+ "uptimeProvider"
+ "v24@0:8d16"
+ "v32@?0@\"NSString\"8@\"NSNumber\"16^B24"
+ "v40@0:8@16@24q32"
+ "v40@0:8d16@24@32"
- "@\"NSMutableSet\""
- "_ephemeralContainerNames"
- "activeEphemeralContainers"
- "addEphemeralContainer:"
- "deactivateEphemeralContainer:"
- "removeEphemeralContainer:"
- "set"

```
