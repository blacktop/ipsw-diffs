## BackgroundSystemTasks

> `/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks`

```diff

-1856.120.12.0.0
-  __TEXT.__text: 0x107a4
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__objc_methlist: 0xfdc
-  __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x9b7
-  __TEXT.__oslogstring: 0x1c37
-  __TEXT.__gcc_except_tab: 0x564
-  __TEXT.__unwind_info: 0x440
-  __TEXT.__objc_classname: 0x206
-  __TEXT.__objc_methname: 0x33c8
-  __TEXT.__objc_methtype: 0x48f
-  __TEXT.__objc_stubs: 0x2160
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x5c8
-  __DATA_CONST.__objc_classlist: 0x80
+2109.0.44.502.1
+  __TEXT.__text: 0x13194
+  __TEXT.__auth_stubs: 0x620
+  __TEXT.__objc_methlist: 0x1264
+  __TEXT.__const: 0x110
+  __TEXT.__cstring: 0xa35
+  __TEXT.__oslogstring: 0x1f64
+  __TEXT.__gcc_except_tab: 0x6d4
+  __TEXT.__unwind_info: 0x4d0
+  __TEXT.__objc_classname: 0x266
+  __TEXT.__objc_methname: 0x3d4c
+  __TEXT.__objc_methtype: 0x52d
+  __TEXT.__objc_stubs: 0x25a0
+  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__const: 0x670
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa90
-  __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x310
+  __DATA_CONST.__objc_selrefs: 0xc18
+  __DATA_CONST.__objc_superrefs: 0x70
+  __AUTH_CONST.__auth_got: 0x320
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0xde0
-  __AUTH_CONST.__objc_const: 0x22f0
+  __AUTH_CONST.__cfstring: 0xe80
+  __AUTH_CONST.__objc_const: 0x2860
   __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x1a0
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x1ec
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x370

   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D3F6A489-0B5A-377F-BFD9-ADB95FBA3D58
-  Functions: 449
-  Symbols:   1648
-  CStrings:  993
+  UUID: 6DA88127-4370-3BA3-8C8B-E3B0A6745F77
+  Functions: 513
+  Symbols:   1861
+  CStrings:  1114
 
Symbols:
+ +[BGSystemTaskCheckpoints reportFeatureCheckpoint:forFeature:atDate:error:]
+ +[BGSystemTaskCheckpoints reportFeatureCheckpoint:forFeature:atDate:error:].cold.1
+ +[BGSystemTaskRequest descriptorWithTaskRequest:].cold.4
+ -[BGSystemTask deregisterThroughputTrackingFor:withEndTime:error:]
+ -[BGSystemTask deregisterThroughputTrackingFor:withEndTime:error:].cold.1
+ -[BGSystemTask initWithIdentifier:queue:taskRequest:]
+ -[BGSystemTask performanceMetricQueue]
+ -[BGSystemTask queue_reportThroughputForPerformanceMetric:error:]
+ -[BGSystemTask queue_reportThroughputForPerformanceMetric:error:].cold.1
+ -[BGSystemTask registerThroughputTrackingFor:withStartTime:error:]
+ -[BGSystemTask registerThroughputTrackingFor:withStartTime:error:].cold.1
+ -[BGSystemTask reportPendingThroughputMetrics]
+ -[BGSystemTask setPerformanceMetricQueue:]
+ -[BGSystemTask setThroughputMetricsMap:]
+ -[BGSystemTask taskRequest]
+ -[BGSystemTask throughputMetricsMap]
+ -[BGSystemTaskPerformanceMetadata .cxx_destruct]
+ -[BGSystemTaskPerformanceMetadata category]
+ -[BGSystemTaskPerformanceMetadata expectedMetricValue]
+ -[BGSystemTaskPerformanceMetadata featureCodes]
+ -[BGSystemTaskPerformanceMetadata initWithIdentifier:qos:workloadCategory:expectedMetricValue:]
+ -[BGSystemTaskPerformanceMetadata initWithIdentifier:taskName:qos:workloadCategory:expectedMetricValue:]
+ -[BGSystemTaskPerformanceMetadata performanceMetricIdentifier]
+ -[BGSystemTaskPerformanceMetadata qos]
+ -[BGSystemTaskPerformanceMetadata setExpectedMetricValue:]
+ -[BGSystemTaskPerformanceMetadata setFeatureCodes:]
+ -[BGSystemTaskPerformanceMetadata setQos:]
+ -[BGSystemTaskPerformanceMetadata setTaskName:]
+ -[BGSystemTaskPerformanceMetadata taskName]
+ -[BGSystemTaskProgressMetrics .cxx_destruct]
+ -[BGSystemTaskProgressMetrics initWithIdentifier:qos:workloadCategory:expectedMetricValue:itemsCompleted:totalItemCount:]
+ -[BGSystemTaskProgressMetrics initWithIdentifier:taskName:qos:workloadCategory:expectedMetricValue:itemsCompleted:totalItemCount:]
+ -[BGSystemTaskProgressMetrics itemsCompleted]
+ -[BGSystemTaskProgressMetrics setItemsCompleted:]
+ -[BGSystemTaskProgressMetrics setTotalItemCount:]
+ -[BGSystemTaskProgressMetrics totalItemCount]
+ -[BGSystemTaskRequest context]
+ -[BGSystemTaskRequest hash]
+ -[BGSystemTaskRequest isEqual:]
+ -[BGSystemTaskRequest requestsImmediateRuntime]
+ -[BGSystemTaskRequest setContext:]
+ -[BGSystemTaskRequest setRequestsImmediateRuntime:]
+ -[BGSystemTaskScheduler clampToBGQoS]
+ -[BGSystemTaskScheduler reportProgressMetrics:error:]
+ -[BGSystemTaskScheduler reportProgressMetrics:error:].cold.1
+ -[BGSystemTaskScheduler setClampToBGQoS:]
+ -[BGSystemTaskSchedulerRegistration generatedLaunchQueue]
+ -[BGSystemTaskSchedulerRegistration registeredLaunchQueue]
+ -[BGSystemTaskSchedulerRegistration setGeneratedLaunchQueue:]
+ -[BGSystemTaskSchedulerRegistration setRegisteredLaunchQueue:]
+ -[BGSystemTaskThroughputMetrics .cxx_destruct]
+ -[BGSystemTaskThroughputMetrics addItemCount:]
+ -[BGSystemTaskThroughputMetrics endTimestamp]
+ -[BGSystemTaskThroughputMetrics initWithIdentifier:qos:workloadCategory:expectedMetricValue:]
+ -[BGSystemTaskThroughputMetrics itemCount]
+ -[BGSystemTaskThroughputMetrics reportingUUID]
+ -[BGSystemTaskThroughputMetrics setEndTimestamp:]
+ -[BGSystemTaskThroughputMetrics setItemCount:]
+ -[BGSystemTaskThroughputMetrics setStartTimestamp:]
+ -[BGSystemTaskThroughputMetrics startTimestamp]
+ GCC_except_table11
+ GCC_except_table160
+ GCC_except_table161
+ GCC_except_table163
+ GCC_except_table164
+ GCC_except_table165
+ GCC_except_table18
+ GCC_except_table20
+ GCC_except_table26
+ GCC_except_table29
+ GCC_except_table32
+ GCC_except_table35
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table40
+ GCC_except_table43
+ GCC_except_table49
+ GCC_except_table54
+ GCC_except_table59
+ GCC_except_table69
+ GCC_except_table71
+ GCC_except_table75
+ GCC_except_table8
+ _OBJC_CLASS_$_BGSystemTaskPerformanceMetadata
+ _OBJC_CLASS_$_BGSystemTaskProgressMetrics
+ _OBJC_CLASS_$_BGSystemTaskThroughputMetrics
+ _OBJC_CLASS_$_NSDateInterval
+ _OBJC_CLASS_$_NSOrderedSet
+ _OBJC_IVAR_$_BGSystemTask._performanceMetricQueue
+ _OBJC_IVAR_$_BGSystemTask._taskRequest
+ _OBJC_IVAR_$_BGSystemTask._throughputMetricsMap
+ _OBJC_IVAR_$_BGSystemTaskPerformanceMetadata._category
+ _OBJC_IVAR_$_BGSystemTaskPerformanceMetadata._expectedMetricValue
+ _OBJC_IVAR_$_BGSystemTaskPerformanceMetadata._featureCodes
+ _OBJC_IVAR_$_BGSystemTaskPerformanceMetadata._performanceMetricIdentifier
+ _OBJC_IVAR_$_BGSystemTaskPerformanceMetadata._qos
+ _OBJC_IVAR_$_BGSystemTaskPerformanceMetadata._taskName
+ _OBJC_IVAR_$_BGSystemTaskProgressMetrics._itemsCompleted
+ _OBJC_IVAR_$_BGSystemTaskProgressMetrics._totalItemCount
+ _OBJC_IVAR_$_BGSystemTaskRequest._context
+ _OBJC_IVAR_$_BGSystemTaskRequest._requestsImmediateRuntime
+ _OBJC_IVAR_$_BGSystemTaskScheduler._clampToBGQoS
+ _OBJC_IVAR_$_BGSystemTaskSchedulerRegistration._generatedLaunchQueue
+ _OBJC_IVAR_$_BGSystemTaskSchedulerRegistration._registeredLaunchQueue
+ _OBJC_IVAR_$_BGSystemTaskThroughputMetrics._endTimestamp
+ _OBJC_IVAR_$_BGSystemTaskThroughputMetrics._itemCount
+ _OBJC_IVAR_$_BGSystemTaskThroughputMetrics._reportingUUID
+ _OBJC_IVAR_$_BGSystemTaskThroughputMetrics._startTimestamp
+ _OBJC_METACLASS_$_BGSystemTaskPerformanceMetadata
+ _OBJC_METACLASS_$_BGSystemTaskProgressMetrics
+ _OBJC_METACLASS_$_BGSystemTaskThroughputMetrics
+ __BGSTBirdRateLimitConfigurationName
+ __OBJC_$_INSTANCE_METHODS_BGSystemTaskPerformanceMetadata
+ __OBJC_$_INSTANCE_METHODS_BGSystemTaskProgressMetrics
+ __OBJC_$_INSTANCE_METHODS_BGSystemTaskThroughputMetrics
+ __OBJC_$_INSTANCE_VARIABLES_BGSystemTaskPerformanceMetadata
+ __OBJC_$_INSTANCE_VARIABLES_BGSystemTaskProgressMetrics
+ __OBJC_$_INSTANCE_VARIABLES_BGSystemTaskThroughputMetrics
+ __OBJC_$_PROP_LIST_BGSystemTaskPerformanceMetadata
+ __OBJC_$_PROP_LIST_BGSystemTaskProgressMetrics
+ __OBJC_$_PROP_LIST_BGSystemTaskThroughputMetrics
+ __OBJC_CLASS_RO_$_BGSystemTaskPerformanceMetadata
+ __OBJC_CLASS_RO_$_BGSystemTaskProgressMetrics
+ __OBJC_CLASS_RO_$_BGSystemTaskThroughputMetrics
+ __OBJC_METACLASS_RO_$_BGSystemTaskPerformanceMetadata
+ __OBJC_METACLASS_RO_$_BGSystemTaskProgressMetrics
+ __OBJC_METACLASS_RO_$_BGSystemTaskThroughputMetrics
+ ___46-[BGSystemTask reportPendingThroughputMetrics]_block_invoke
+ ___48-[BGSystemTaskScheduler resumeScheduling:error:]_block_invoke.93
+ ___48-[BGSystemTaskScheduler resumeScheduling:error:]_block_invoke.93.cold.1
+ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.101.cold.1
+ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.102
+ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.102.cold.1
+ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.104
+ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.109
+ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.110
+ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.99
+ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.99.cold.1
+ ___49-[BGSystemTaskScheduler submitTaskRequest:error:]_block_invoke.89
+ ___49-[BGSystemTaskScheduler submitTaskRequest:error:]_block_invoke.89.cold.1
+ ___49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.91
+ ___49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.91.cold.1
+ ___50-[BGSystemTaskScheduler installEventStreamHandler]_block_invoke.85
+ ___53-[BGSystemTaskScheduler reportProgressMetrics:error:]_block_invoke
+ ___54-[BGSystemTaskScheduler deregisterTaskWithIdentifier:]_block_invoke.113
+ ___58-[BGSystemTaskScheduler systemTask:consumedResults:error:]_block_invoke.129
+ ___58-[BGSystemTaskScheduler systemTask:producedResults:error:]_block_invoke.127
+ ___63-[BGSystemTaskScheduler cancelTaskRequestWithIdentifier:error:]_block_invoke.92
+ ___63-[BGSystemTaskScheduler expireTaskWithRegistration:withReason:]_block_invoke.112
+ ___63-[BGSystemTaskScheduler expireTaskWithRegistration:withReason:]_block_invoke.112.cold.1
+ ___66-[BGSystemTask deregisterThroughputTrackingFor:withEndTime:error:]_block_invoke
+ ___66-[BGSystemTask deregisterThroughputTrackingFor:withEndTime:error:]_block_invoke.cold.1
+ ___66-[BGSystemTask registerThroughputTrackingFor:withStartTime:error:]_block_invoke
+ ___68-[BGSystemTaskScheduler systemTask:resetResultsForIdentifier:error:]_block_invoke.130
+ ___block_descriptor_40_e8_32s_e8_I12?0B8ls32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0ls32l8r56l8r64l8s40l8s48l8
+ __os_feature_enabled_impl
+ _objc_msgSend$category
+ _objc_msgSend$context
+ _objc_msgSend$date
+ _objc_msgSend$deregisterThroughputTrackingFor:withEndTime:error:
+ _objc_msgSend$duration
+ _objc_msgSend$endTimestamp
+ _objc_msgSend$expectedMetricValue
+ _objc_msgSend$generatedLaunchQueue
+ _objc_msgSend$hash
+ _objc_msgSend$initWithIdentifier:qos:workloadCategory:expectedMetricValue:
+ _objc_msgSend$initWithIdentifier:queue:taskRequest:
+ _objc_msgSend$initWithStartDate:endDate:
+ _objc_msgSend$itemCount
+ _objc_msgSend$itemsCompleted
+ _objc_msgSend$orderedSetWithArray:
+ _objc_msgSend$performanceMetricIdentifier
+ _objc_msgSend$performanceMetricQueue
+ _objc_msgSend$qos
+ _objc_msgSend$queue_reportThroughputForPerformanceMetric:error:
+ _objc_msgSend$registeredLaunchQueue
+ _objc_msgSend$reportFeatureCheckpoint:forFeature:atDate:error:
+ _objc_msgSend$reportPendingThroughputMetrics
+ _objc_msgSend$reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:
+ _objc_msgSend$reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:
+ _objc_msgSend$reportingUUID
+ _objc_msgSend$requestsImmediateRuntime
+ _objc_msgSend$setContext:
+ _objc_msgSend$setEndTimestamp:
+ _objc_msgSend$setGeneratedLaunchQueue:
+ _objc_msgSend$setItemCount:
+ _objc_msgSend$setRequestsImmediateRuntime:
+ _objc_msgSend$setStartTimestamp:
+ _objc_msgSend$setTaskName:
+ _objc_msgSend$startTimestamp
+ _objc_msgSend$taskName
+ _objc_msgSend$throughputMetricsMap
+ _objc_msgSend$totalItemCount
+ _objc_retain_x4
- +[BGSystemTaskCheckpoints reportFeatureCheckpoint:forFeature:error:].cold.1
- -[BGSystemTaskScheduler runTaskWithRegistration:].cold.3
- -[BGSystemTaskSchedulerRegistration launchQueue]
- -[BGSystemTaskSchedulerRegistration setLaunchQueue:]
- GCC_except_table10
- GCC_except_table15
- GCC_except_table151
- GCC_except_table152
- GCC_except_table153
- GCC_except_table154
- GCC_except_table155
- GCC_except_table19
- GCC_except_table23
- GCC_except_table27
- GCC_except_table28
- GCC_except_table30
- GCC_except_table33
- GCC_except_table37
- GCC_except_table41
- GCC_except_table44
- GCC_except_table51
- GCC_except_table53
- GCC_except_table60
- GCC_except_table68
- GCC_except_table7
- _OBJC_IVAR_$_BGSystemTaskSchedulerRegistration._launchQueue
- ___48-[BGSystemTaskScheduler resumeScheduling:error:]_block_invoke.86
- ___48-[BGSystemTaskScheduler resumeScheduling:error:]_block_invoke.86.cold.1
- ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.100
- ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.92
- ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.92.cold.1
- ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.94
- ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.94.cold.1
- ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.95
- ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.95.cold.1
- ___49-[BGSystemTaskScheduler submitTaskRequest:error:]_block_invoke.82
- ___49-[BGSystemTaskScheduler submitTaskRequest:error:]_block_invoke.82.cold.1
- ___49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.84
- ___49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.84.cold.1
- ___50-[BGSystemTaskScheduler installEventStreamHandler]_block_invoke.78
- ___54-[BGSystemTaskScheduler deregisterTaskWithIdentifier:]_block_invoke.104
- ___58-[BGSystemTaskScheduler systemTask:consumedResults:error:]_block_invoke.120
- ___58-[BGSystemTaskScheduler systemTask:producedResults:error:]_block_invoke.118
- ___63-[BGSystemTaskScheduler cancelTaskRequestWithIdentifier:error:]_block_invoke.85
- ___63-[BGSystemTaskScheduler expireTaskWithRegistration:withReason:]_block_invoke.103
- ___63-[BGSystemTaskScheduler expireTaskWithRegistration:withReason:]_block_invoke.103.cold.1
- ___68-[BGSystemTaskScheduler systemTask:resetResultsForIdentifier:error:]_block_invoke.121
- _objc_msgSend$launchQueue
- _objc_msgSend$reportFeatureCheckpoint:forFeature:error:
- _objc_msgSend$setLaunchQueue:
CStrings:
+ "%@ was expired %ds ago, but hasn't responded yet"
+ "%@: Registered queue is of higher QoS than it should be. Expected Max QoS %u, Actual QoS %u"
+ "%{public}@: Invalid context"
+ "@\"NSDate\""
+ "@\"NSNumber\""
+ "@40@0:8@16@24@32"
+ "@48@0:8@16@24Q32@40"
+ "@56@0:8@16@24@32Q40@48"
+ "@64@0:8@16@24Q32@40@48@56"
+ "@72@0:8@16@24@32Q40@48@56@64"
+ "B48@0:8Q16Q24@32^@40"
+ "BGSystemTaskPerformanceMetadata"
+ "BGSystemTaskProgressMetrics"
+ "BGSystemTaskThroughputMetrics"
+ "BirdConfiguration"
+ "CX"
+ "Context"
+ "DAS"
+ "Error: %@ feature checkpoint %lu for feature %lu at %@"
+ "Failed to de-register throughput tracking for task %@ with error: %@"
+ "Failed to register throughput tracking for task %@ with error: %@"
+ "Found registration of invalid type for %@"
+ "I12@?0B8"
+ "Performance clamped to BG QoS"
+ "Received feature checkpoint %lu for feature %lu at: %@"
+ "Reporting progress metrics for %@"
+ "Reporting throughput metrics for %@"
+ "RequestsImmediateRuntime"
+ "T@\"BGSystemTaskRequest\",R,C,V_taskRequest"
+ "T@\"NSArray\",&,N,V_featureCodes"
+ "T@\"NSDate\",&,N,V_endTimestamp"
+ "T@\"NSDate\",&,N,V_startTimestamp"
+ "T@\"NSDictionary\",C,N,V_context"
+ "T@\"NSMutableDictionary\",&,N,V_throughputMetricsMap"
+ "T@\"NSNumber\",&,N,V_expectedMetricValue"
+ "T@\"NSNumber\",&,N,V_itemsCompleted"
+ "T@\"NSNumber\",&,N,V_qos"
+ "T@\"NSNumber\",&,N,V_totalItemCount"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_generatedLaunchQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_performanceMetricQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_registeredLaunchQueue"
+ "T@\"NSString\",&,N,V_taskName"
+ "T@\"NSString\",R,N,V_performanceMetricIdentifier"
+ "T@\"NSUUID\",R,N,V_reportingUUID"
+ "TB,N,V_clampToBGQoS"
+ "TB,N,V_requestsImmediateRuntime"
+ "TQ,N,V_itemCount"
+ "TQ,R,N,V_category"
+ "_category"
+ "_clampToBGQoS"
+ "_context"
+ "_endTimestamp"
+ "_expectedMetricValue"
+ "_generatedLaunchQueue"
+ "_itemCount"
+ "_itemsCompleted"
+ "_performanceMetricIdentifier"
+ "_performanceMetricQueue"
+ "_qos"
+ "_registeredLaunchQueue"
+ "_reportingUUID"
+ "_requestsImmediateRuntime"
+ "_startTimestamp"
+ "_taskName"
+ "_throughputMetricsMap"
+ "_totalItemCount"
+ "addItemCount:"
+ "bgst_clamp_to_bg_qos"
+ "category"
+ "clampToBGQoS"
+ "com.apple.BGSystemTask.perfMetricQ.%@"
+ "context"
+ "deregisterThroughputTrackingFor: %@:%@ hasn't been registered for throughput tracking. Use registerThroughputTrackingFor to register"
+ "deregisterThroughputTrackingFor:withEndTime:error:"
+ "duration"
+ "endTimestamp"
+ "expectedMetricValue"
+ "generatedLaunchQueue"
+ "initWithIdentifier:qos:workloadCategory:expectedMetricValue:"
+ "initWithIdentifier:qos:workloadCategory:expectedMetricValue:itemsCompleted:totalItemCount:"
+ "initWithIdentifier:queue:taskRequest:"
+ "initWithIdentifier:taskName:qos:workloadCategory:expectedMetricValue:"
+ "initWithIdentifier:taskName:qos:workloadCategory:expectedMetricValue:itemsCompleted:totalItemCount:"
+ "initWithStartDate:endDate:"
+ "itemCount"
+ "itemsCompleted"
+ "orderedSetWithArray:"
+ "performanceMetricIdentifier"
+ "performanceMetricQueue"
+ "qos"
+ "queue_reportThroughputForPerformanceMetric:error:"
+ "registerThroughputTrackingFor:withStartTime:error:"
+ "registeredLaunchQueue"
+ "reportFeatureCheckpoint:forFeature:atDate:error:"
+ "reportPendingThroughputMetrics"
+ "reportProgressMetrics: Failed to report progress metrics for %@"
+ "reportProgressMetrics: Reported progress metrics successfully for %@"
+ "reportProgressMetrics:error:"
+ "reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:"
+ "reportThroughputForPerformanceMetric: EndDate:%@ < StartDate:%@ for %@:%@"
+ "reportThroughputForPerformanceMetric: Failed to report throughput metrics successfully for %@"
+ "reportThroughputForPerformanceMetric: Reported throughput metrics successfully for %@"
+ "reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:"
+ "reportingUUID"
+ "requestsImmediateRuntime"
+ "setClampToBGQoS:"
+ "setContext:"
+ "setEndTimestamp:"
+ "setExpectedMetricValue:"
+ "setGeneratedLaunchQueue:"
+ "setItemCount:"
+ "setItemsCompleted:"
+ "setPerformanceMetricQueue:"
+ "setQos:"
+ "setRegisteredLaunchQueue:"
+ "setRequestsImmediateRuntime:"
+ "setStartTimestamp:"
+ "setTaskName:"
+ "setThroughputMetricsMap:"
+ "setTotalItemCount:"
+ "startTimestamp"
+ "taskName"
+ "throughputMetricsMap"
+ "totalItemCount"
+ "\xd1"
- "%{public}@ was expired %ds ago, but hasn't responded yet"
- "%{public}@: launchQueue is of higher QoS than it should be"
- "Error: %@ feature checkpoint %lu for feature %lu"
- "Found registration of invalid type for %{public}@"
- "Received feature checkpoint %lu for feature %lu"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_launchQueue"
- "_launchQueue"
- "launchQueue"
- "setLaunchQueue:"
- "\xa1"

```
