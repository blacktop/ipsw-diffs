## DuetActivityScheduler

> `/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler`

```diff

-1439.80.3.0.0
-  __TEXT.__text: 0x2085c
+1470.100.56.0.0
+  __TEXT.__text: 0x21634
   __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x22e0
+  __TEXT.__objc_methlist: 0x2338
   __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x954
-  __TEXT.__cstring: 0x1940
-  __TEXT.__oslogstring: 0x19e5
-  __TEXT.__unwind_info: 0x98c
-  __TEXT.__objc_classname: 0x4a1
-  __TEXT.__objc_methname: 0x714f
-  __TEXT.__objc_methtype: 0xd8a
-  __TEXT.__objc_stubs: 0x4180
+  __TEXT.__gcc_except_tab: 0x998
+  __TEXT.__cstring: 0x1954
+  __TEXT.__oslogstring: 0x1af6
+  __TEXT.__unwind_info: 0x9c8
+  __TEXT.__objc_classname: 0x4e5
+  __TEXT.__objc_methname: 0x72df
+  __TEXT.__objc_methtype: 0xe87
+  __TEXT.__objc_stubs: 0x4280
   __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x9a0
+  __DATA_CONST.__const: 0xa18
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0xc0
+  __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x45b8
-  __DATA_CONST.__objc_selrefs: 0x19a0
+  __DATA_CONST.__objc_const: 0x46b0
+  __DATA_CONST.__objc_selrefs: 0x19f8
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x1a8
+  __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__cfstring: 0x26c0
+  __AUTH_CONST.__cfstring: 0x2720
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_const: 0xb28

   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x318
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x1a8
-  __DATA.__objc_superrefs: 0x88
   __DATA.__objc_ivar: 0x2e0
-  __DATA.__data: 0xa08
+  __DATA.__data: 0xac8
   __DATA.__bss: 0x50
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x730

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1CAD8964-3F08-3AC4-A3CC-849523268192
-  Functions: 915
-  Symbols:   3327
-  CStrings:  2214
+  UUID: FE8A2D43-27BE-3E4C-9AE5-2310025C76B3
+  Functions: 935
+  Symbols:   3390
+  CStrings:  2251
 
Symbols:
+ -[NSMutableSet(_DASAdditions) enumerateObjectsInChunksOfSize:block:]
+ -[_DASActivity isCPUIntensive]
+ -[_DASActivity isDiskIntensive]
+ -[_DASActivity isMemoryIntensive]
+ -[_DASScheduler evaluateAllActivitiesWithHandle:]
+ -[_DASScheduler reportCustomCheckpoint:forTask:error:]
+ -[_DASScheduler reportFeatureCheckpoint:forFeature:error:]
+ -[_DASScheduler reportSystemWorkload:ofCategory:error:]
+ GCC_except_table162
+ GCC_except_table165
+ GCC_except_table168
+ GCC_except_table82
+ GCC_except_table92
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__DASBGSystemTaskDataCollection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__DASBGSystemTaskDataCollectionServer
+ __OBJC_$_PROTOCOL_METHOD_TYPES__DASBGSystemTaskDataCollection
+ __OBJC_$_PROTOCOL_METHOD_TYPES__DASBGSystemTaskDataCollectionServer
+ __OBJC_$_PROTOCOL_REFS__DASBGSystemTaskDataCollection
+ __OBJC_LABEL_PROTOCOL_$__DASBGSystemTaskDataCollection
+ __OBJC_LABEL_PROTOCOL_$__DASBGSystemTaskDataCollectionServer
+ __OBJC_PROTOCOL_$__DASBGSystemTaskDataCollection
+ __OBJC_PROTOCOL_$__DASBGSystemTaskDataCollectionServer
+ ___25-[_DASScheduler policies]_block_invoke.245
+ ___27-[_DASScheduler allBudgets]_block_invoke.242
+ ___27-[_DASScheduler clasStatus]_block_invoke.246
+ ___27-[_DASScheduler statistics]_block_invoke.241
+ ___31-[_DASScheduler runActivities:]_block_invoke.256
+ ___33-[_DASScheduler deferActivities:]_block_invoke.235
+ ___34-[_DASScheduler evaluatePolicies:]_block_invoke.247
+ ___35-[_DASScheduler currentPredictions]_block_invoke.239
+ ___35-[_DASScheduler submitTaskRequest:]_block_invoke.261
+ ___36-[_DASScheduler submittedActivities]_block_invoke.237
+ ___37-[_DASScheduler completeTaskRequest:]_block_invoke.264
+ ___37-[_DASScheduler completeTaskRequest:]_block_invoke.264.cold.1
+ ___37-[_DASScheduler pauseWithParameters:]_block_invoke.253
+ ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.263
+ ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.263.cold.1
+ ___40-[_DASScheduler enableTaskRegistryMode:]_block_invoke.251
+ ___41-[_DASScheduler addPauseExceptParameter:]_block_invoke.254
+ ___42-[_DASScheduler balanceForBudgetWithName:]_block_invoke.243
+ ___42-[_DASScheduler initWithListenerEndpoint:]_block_invoke.222
+ ___42-[_DASScheduler runProceedableActivities:]_block_invoke.249
+ ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.252
+ ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.252.cold.1
+ ___47-[_DASScheduler runActivitiesWithDelayedStart:]_block_invoke.255
+ ___48-[_DASScheduler blockingPoliciesWithParameters:]_block_invoke.250
+ ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.262
+ ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.262.cold.1
+ ___49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke
+ ___49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.248
+ ___49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.248.cold.1
+ ___49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.cold.1
+ ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.267
+ ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.267.cold.1
+ ___52-[_DASScheduler unregisterSystemTaskWithIdentifier:]_block_invoke.268
+ ___52-[_DASScheduler unregisterSystemTaskWithIdentifier:]_block_invoke.268.cold.1
+ ___54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke
+ ___54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.272
+ ___54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.272.cold.1
+ ___54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.cold.1
+ ___55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke
+ ___55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.271
+ ___55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.271.cold.1
+ ___55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.cold.1
+ ___58-[_DASScheduler reportFeatureCheckpoint:forFeature:error:]_block_invoke
+ ___58-[_DASScheduler reportFeatureCheckpoint:forFeature:error:]_block_invoke.269
+ ___58-[_DASScheduler reportFeatureCheckpoint:forFeature:error:]_block_invoke.269.cold.1
+ ___58-[_DASScheduler reportFeatureCheckpoint:forFeature:error:]_block_invoke.cold.1
+ ___59-[_DASScheduler acknowledgeSystemTaskLaunchWithIdentifier:]_block_invoke.265
+ ___59-[_DASScheduler acknowledgeSystemTaskLaunchWithIdentifier:]_block_invoke.265.cold.1
+ ___63-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:]_block_invoke.266
+ ___63-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:]_block_invoke.266.cold.1
+ ___block_descriptor_48_e8_32s40r_e8_v12?0B8lr40l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e17_v16?0"NSError"8ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e20_v20?0B8"NSError"12ls32l8r40l8r48l8
+ ___block_literal_global.258
+ ___block_literal_global.48
+ _objc_msgSend$allObjects
+ _objc_msgSend$evaluateAllActivities:handler:
+ _objc_msgSend$isCPUIntensive
+ _objc_msgSend$isDiskIntensive
+ _objc_msgSend$isMemoryIntensive
+ _objc_msgSend$reportCustomCheckpoint:forTask:withHandler:
+ _objc_msgSend$reportFeatureCheckpoint:forFeature:withHandler:
+ _objc_msgSend$reportSystemWorkload:ofCategory:withHandler:
+ _objc_msgSend$subarrayWithRange:
- -[_DASScheduler evaluateAllActivities]
- GCC_except_table79
- GCC_except_table89
- ___25-[_DASScheduler policies]_block_invoke.235
- ___27-[_DASScheduler allBudgets]_block_invoke.232
- ___27-[_DASScheduler clasStatus]_block_invoke.236
- ___27-[_DASScheduler statistics]_block_invoke.231
- ___31-[_DASScheduler runActivities:]_block_invoke.246
- ___33-[_DASScheduler deferActivities:]_block_invoke.225
- ___34-[_DASScheduler evaluatePolicies:]_block_invoke.237
- ___35-[_DASScheduler currentPredictions]_block_invoke.229
- ___35-[_DASScheduler submitTaskRequest:]_block_invoke.251
- ___36-[_DASScheduler submittedActivities]_block_invoke.227
- ___37-[_DASScheduler completeTaskRequest:]_block_invoke.254
- ___37-[_DASScheduler completeTaskRequest:]_block_invoke.254.cold.1
- ___37-[_DASScheduler pauseWithParameters:]_block_invoke.243
- ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.253
- ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.253.cold.1
- ___38-[_DASScheduler evaluateAllActivities]_block_invoke
- ___38-[_DASScheduler evaluateAllActivities]_block_invoke.238
- ___38-[_DASScheduler evaluateAllActivities]_block_invoke.cold.1
- ___40-[_DASScheduler enableTaskRegistryMode:]_block_invoke.241
- ___41-[_DASScheduler addPauseExceptParameter:]_block_invoke.244
- ___42-[_DASScheduler balanceForBudgetWithName:]_block_invoke.233
- ___42-[_DASScheduler initWithListenerEndpoint:]_block_invoke.212
- ___42-[_DASScheduler runProceedableActivities:]_block_invoke.239
- ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.242
- ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.242.cold.1
- ___47-[_DASScheduler runActivitiesWithDelayedStart:]_block_invoke.245
- ___48-[_DASScheduler blockingPoliciesWithParameters:]_block_invoke.240
- ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.252
- ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.252.cold.1
- ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.257
- ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.257.cold.1
- ___52-[_DASScheduler unregisterSystemTaskWithIdentifier:]_block_invoke.258
- ___52-[_DASScheduler unregisterSystemTaskWithIdentifier:]_block_invoke.258.cold.1
- ___59-[_DASScheduler acknowledgeSystemTaskLaunchWithIdentifier:]_block_invoke.255
- ___59-[_DASScheduler acknowledgeSystemTaskLaunchWithIdentifier:]_block_invoke.255.cold.1
- ___63-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:]_block_invoke.256
- ___63-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:]_block_invoke.256.cold.1
- ___block_literal_global.248
- ___block_literal_global.47
- _objc_msgSend$evaluateAllActivities:
CStrings:
+ " CPU"
+ " Disk"
+ " Memory"
+ ", Intensive:"
+ "B24@0:8@\"NSFileHandle\"16"
+ "B32@0:8Q16@?24"
+ "B40@0:8Q16@\"NSString\"24^@32"
+ "B40@0:8Q16@24^@32"
+ "B40@0:8Q16Q24^@32"
+ "Error evaluating all activities"
+ "T@\"NSString\",?,R,C"
+ "_DASBGSystemTaskDataCollection"
+ "_DASBGSystemTaskDataCollectionServer"
+ "enumerateObjectsInChunksOfSize:block:"
+ "evaluateAllActivities:handler:"
+ "evaluateAllActivitiesWithHandle:"
+ "isCPUIntensive"
+ "isDiskIntensive"
+ "isMemoryIntensive"
+ "reportCustomCheckpoint Failed: %@"
+ "reportCustomCheckpoint Failed: Server error %@"
+ "reportCustomCheckpoint:forTask:error:"
+ "reportCustomCheckpoint:forTask:withHandler:"
+ "reportFeatureCheckpoint Failed: %@"
+ "reportFeatureCheckpoint Failed: Server error %@"
+ "reportFeatureCheckpoint:forFeature:error:"
+ "reportFeatureCheckpoint:forFeature:withHandler:"
+ "reportSystemWorkload Failed: %@"
+ "reportSystemWorkload Failed: Server error %@"
+ "reportSystemWorkload:ofCategory:error:"
+ "reportSystemWorkload:ofCategory:withHandler:"
+ "subarrayWithRange:"
+ "v32@0:8@\"NSFileHandle\"16@?<v@?B>24"
+ "v40@0:8Q16@\"NSString\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8Q16@24@?32"
+ "v40@0:8Q16Q24@?32"
+ "v40@0:8Q16Q24@?<v@?B@\"NSError\">32"
- ", Intensive"
- "evaluateAllActivities"
- "evaluateAllActivities:"

```
