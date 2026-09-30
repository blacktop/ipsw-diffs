## BackgroundSystemTasks

> `/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks`

```diff

-2109.80.9.0.0
-  __TEXT.__text: 0x135fc
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x1274
+2109.100.198.0.0
+  __TEXT.__text: 0x1444c
+  __TEXT.__auth_stubs: 0x620
+  __TEXT.__objc_methlist: 0x12d4
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0xa7d
-  __TEXT.__oslogstring: 0x2013
-  __TEXT.__gcc_except_tab: 0x738
-  __TEXT.__unwind_info: 0x510
+  __TEXT.__cstring: 0xabc
+  __TEXT.__oslogstring: 0x20b3
+  __TEXT.__gcc_except_tab: 0x6dc
+  __TEXT.__unwind_info: 0x5d0
   __TEXT.__objc_classname: 0x266
-  __TEXT.__objc_methname: 0x3db8
-  __TEXT.__objc_methtype: 0x52d
-  __TEXT.__objc_stubs: 0x2620
+  __TEXT.__objc_methname: 0x3f46
+  __TEXT.__objc_methtype: 0x53d
+  __TEXT.__objc_stubs: 0x2700
   __DATA_CONST.__got: 0x150
   __DATA_CONST.__const: 0x698
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc40
+  __DATA_CONST.__objc_selrefs: 0xc90
   __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x330
+  __AUTH_CONST.__auth_got: 0x320
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0xf00
-  __AUTH_CONST.__objc_const: 0x2860
+  __AUTH_CONST.__cfstring: 0xf20
+  __AUTH_CONST.__objc_const: 0x28c0
   __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x1ec
+  __AUTH.__objc_data: 0x208
+  __DATA.__objc_ivar: 0x1f4
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x370
+  __DATA_DIRTY.__objc_data: 0x3e8
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FE9FDBDD-F66E-3899-A2A8-8A5A72DC8CF9
-  Functions: 518
-  Symbols:   1881
-  CStrings:  1129
+  UUID: FC199EC2-BC81-3DCD-8F9D-F774A71865DA
+  Functions: 531
+  Symbols:   1931
+  CStrings:  1149
 
Symbols:
+ -[BGSystemTask queue_reportThroughputForPerformanceMetric:error:].cold.2
+ -[BGSystemTaskRequest description]
+ -[BGSystemTaskRequest requiresUserInactivityIsSetByUser]
+ -[BGSystemTaskRequest setRequiresUserInactivityIsSetByUser:]
+ -[BGSystemTaskScheduler exemptTask:]
+ -[BGSystemTaskScheduler getSubmittedSystemTaskRequests:error:]
+ -[BGSystemTaskScheduler isInternalVariant]
+ -[BGSystemTaskScheduler setIsInternalVariant:]
+ -[BGSystemTaskScheduler suspensionThresholdForTask:]
+ GCC_except_table163
+ GCC_except_table167
+ GCC_except_table168
+ GCC_except_table169
+ GCC_except_table48
+ GCC_except_table51
+ GCC_except_table58
+ GCC_except_table61
+ GCC_except_table65
+ GCC_except_table73
+ GCC_except_table75
+ GCC_except_table79
+ _OBJC_IVAR_$_BGSystemTaskRequest._requiresUserInactivityIsSetByUser
+ _OBJC_IVAR_$_BGSystemTaskScheduler._isInternalVariant
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ ___48-[BGSystemTaskScheduler resumeScheduling:error:]_block_invoke.94
+ ___48-[BGSystemTaskScheduler resumeScheduling:error:]_block_invoke.94.cold.1
+ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.100
+ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.100.cold.1
+ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.103
+ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.103.cold.1
+ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.108
+ ___49-[BGSystemTaskScheduler submitTaskRequest:error:]_block_invoke.90
+ ___49-[BGSystemTaskScheduler submitTaskRequest:error:]_block_invoke.90.cold.1
+ ___49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.92
+ ___49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.92.cold.1
+ ___50-[BGSystemTaskScheduler installEventStreamHandler]_block_invoke.86
+ ___54-[BGSystemTaskScheduler deregisterTaskWithIdentifier:]_block_invoke.125
+ ___58-[BGSystemTaskScheduler systemTask:consumedResults:error:]_block_invoke.144
+ ___58-[BGSystemTaskScheduler systemTask:producedResults:error:]_block_invoke.142
+ ___62-[BGSystemTaskScheduler getSubmittedSystemTaskRequests:error:]_block_invoke
+ ___63-[BGSystemTaskScheduler cancelTaskRequestWithIdentifier:error:]_block_invoke.93
+ ___63-[BGSystemTaskScheduler expireTaskWithRegistration:withReason:]_block_invoke.cold.3
+ ___68-[BGSystemTaskScheduler systemTask:resetResultsForIdentifier:error:]_block_invoke.145
+ ___block_descriptor_48_e8_32r40r_e45_v24?0"NSObject<OS_xpc_object>"8"NSError"16lr32l8r40l8
+ ___block_descriptor_66_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ __das_xpc_object_string_interned
+ _arc4random_uniform
+ _objc_msgSend$das_dedup
+ _objc_msgSend$descriptionInStringsFileFormat
+ _objc_msgSend$exemptTask:
+ _objc_msgSend$getSubmittedSystemTaskRequestsWithCompletionHandler:
+ _objc_msgSend$requiresUserInactivityIsSetByUser
+ _objc_msgSend$setRequiresUserInactivityIsSetByUser:
+ _objc_msgSend$suspensionExemptionsForActivity:
+ _objc_msgSend$suspensionThresholdForTask:
+ _objc_opt_new
+ _objc_retainAutoreleasedReturnValue
+ _os_variant_has_internal_content
+ _qos_class_self
+ _xpc_array_get_count
+ _xpc_array_get_value
- GCC_except_table158
- GCC_except_table159
- GCC_except_table160
- GCC_except_table166
- GCC_except_table49
- GCC_except_table52
- GCC_except_table57
- GCC_except_table60
- GCC_except_table64
- GCC_except_table72
- GCC_except_table76
- ___48-[BGSystemTaskScheduler resumeScheduling:error:]_block_invoke.93
- ___48-[BGSystemTaskScheduler resumeScheduling:error:]_block_invoke.93.cold.1
- ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.101
- ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.101.cold.1
- ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.104
- ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.110
- ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.99
- ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.99.cold.1
- ___49-[BGSystemTaskScheduler submitTaskRequest:error:]_block_invoke.89
- ___49-[BGSystemTaskScheduler submitTaskRequest:error:]_block_invoke.89.cold.1
- ___49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.91
- ___49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.91.cold.1
- ___50-[BGSystemTaskScheduler installEventStreamHandler]_block_invoke.85
- ___54-[BGSystemTaskScheduler deregisterTaskWithIdentifier:]_block_invoke.126
- ___58-[BGSystemTaskScheduler systemTask:consumedResults:error:]_block_invoke.142
- ___58-[BGSystemTaskScheduler systemTask:producedResults:error:]_block_invoke.140
- ___63-[BGSystemTaskScheduler cancelTaskRequestWithIdentifier:error:]_block_invoke.92
- ___68-[BGSystemTaskScheduler systemTask:resetResultsForIdentifier:error:]_block_invoke.143
- ___block_descriptor_40_e8_32s_e8_I12?0B8ls32l8
- ___block_descriptor_65_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$suspensionDelayMitigationsForActivity:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x27
- _objc_retain_x28
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ "B32@0:8^@16^@24"
+ "Fetched submitted task requests: %{public}@"
+ "TB,N,V_isInternalVariant"
+ "TB,N,V_requiresUserInactivityIsSetByUser"
+ "_isInternalVariant"
+ "_requiresUserInactivityIsSetByUser"
+ "com.apple.dasd"
+ "das_dedup"
+ "descriptionInStringsFileFormat"
+ "exemptTask:"
+ "getSubmittedSystemTaskRequests:error:"
+ "getSubmittedSystemTaskRequestsWithCompletionHandler failed to fetch task requests: %{public}@"
+ "getSubmittedSystemTaskRequestsWithCompletionHandler:"
+ "isInternalVariant"
+ "reportThroughputForPerformanceMetric: Total Duration = 0, Infinite Throughput is invalid for %@:%@"
+ "requiresUserInactivityIsSetByUser"
+ "setIsInternalVariant:"
+ "setRequiresUserInactivityIsSetByUser:"
+ "suspensionExemptionsForActivity:"
+ "suspensionThresholdForTask:"
+ "v24@?0@\"NSObject<OS_xpc_object>\"8@\"NSError\"16"
- "%@: Applying Suspension Delay Mitigations: Since version %@.%@, Threshold %@"
- "I12@?0B8"
- "suspensionDelayMitigationsForActivity:"

```
