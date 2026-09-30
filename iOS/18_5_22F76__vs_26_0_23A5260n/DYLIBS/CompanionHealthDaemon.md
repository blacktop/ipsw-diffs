## CompanionHealthDaemon

> `/System/Library/PrivateFrameworks/CompanionHealthDaemon.framework/CompanionHealthDaemon`

```diff

-1672.21.0.0.0
-  __TEXT.__text: 0x6ed8
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0x6b4
-  __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x220
-  __TEXT.__cstring: 0x454
-  __TEXT.__oslogstring: 0xc0c
-  __TEXT.__unwind_info: 0x1f0
-  __TEXT.__objc_classname: 0x1e3
-  __TEXT.__objc_methname: 0x19eb
-  __TEXT.__objc_methtype: 0x481
-  __TEXT.__objc_stubs: 0x1800
-  __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__const: 0x250
+1781.1.3.0.0
+  __TEXT.__text: 0x71d4
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__objc_methlist: 0x66c
+  __TEXT.__const: 0xc8
+  __TEXT.__gcc_except_tab: 0x26c
+  __TEXT.__cstring: 0x4a5
+  __TEXT.__oslogstring: 0xc42
+  __TEXT.__unwind_info: 0x200
+  __TEXT.__objc_classname: 0x1ca
+  __TEXT.__objc_methname: 0x1a7f
+  __TEXT.__objc_methtype: 0x485
+  __TEXT.__objc_stubs: 0x18e0
+  __DATA_CONST.__got: 0x298
+  __DATA_CONST.__const: 0x278
   __DATA_CONST.__objc_classlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x778
+  __DATA_CONST.__objc_selrefs: 0x7a0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x278
+  __AUTH_CONST.__auth_got: 0x270
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x460
-  __AUTH_CONST.__objc_const: 0x1b70
+  __AUTH_CONST.__cfstring: 0x480
+  __AUTH_CONST.__objc_const: 0x1ba8
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x60
-  __DATA.__data: 0x3c0
+  __DATA.__objc_ivar: 0x68
+  __DATA.__data: 0x360
   __DATA_DIRTY.__objc_data: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices
   - /System/Library/PrivateFrameworks/Fitness.framework/Fitness
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0470E476-0C1E-35F2-A295-53AA415EB8FB
-  Functions: 133
-  Symbols:   818
-  CStrings:  473
+  UUID: 97F86141-528B-3931-A7D3-D3FF363876FC
+  Functions: 130
+  Symbols:   813
+  CStrings:  482
 
Symbols:
+ -[CHCoachingDiagnosticManager profileDidBecomeReady:].cold.1
+ -[CHCompanionWidgetSchedulingManager associationsUpdatedForObject:subObject:type:behavior:objects:anchor:]
+ -[CHCompanionWidgetSchedulingManager associationsUpdatedForObject:subObject:type:behavior:objects:anchor:].cold.1
+ -[CHCompanionWidgetSchedulingManager associationsUpdatedForObject:subObject:type:behavior:objects:anchor:].cold.2
+ -[CHCompanionWidgetSchedulingManager associationsUpdatedForObject:subObject:type:behavior:objects:anchor:].cold.3
+ GCC_except_table10
+ GCC_except_table2
+ _HKLogCoachingCategory
+ _OBJC_CLASS_$_BGRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_HDDatabaseAvailabilityCondition
+ _OBJC_CLASS_$_HDRepeatingBackgroundTask
+ _OBJC_IVAR_$_CHCoachingDiagnosticManager._databaseAvailableCondition
+ _OBJC_IVAR_$_CHCoachingDiagnosticManager._lastRunDate
+ _OBJC_IVAR_$_CHCoachingDiagnosticManager._repeatingBackgroundTask
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HDAssociationObserver
+ ___53-[CHCoachingDiagnosticManager profileDidBecomeReady:]_block_invoke
+ ___53-[CHCoachingDiagnosticManager profileDidBecomeReady:]_block_invoke_2
+ ___56-[CHTrendsNotificationManager sendNotificationIfAllowed]_block_invoke.311
+ ___67-[CHCompanionWorkoutCreditManager _queue_performWorkoutCreditFixup]_block_invoke.322
+ ___block_descriptor_40_e8_32w_e55_v24?0"HDRepeatingBackgroundTask"8?<v?q"NSError">16lw32l8
+ ___block_descriptor_64_e8_32s40r48r56r_e5_v8?0lr40l8s32l8r48l8r56l8
+ _objc_msgSend$getRequest
+ _objc_msgSend$initWithDatabase:loggingCategory:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithName:loggingCategory:scheduler:handler:condition:
+ _objc_msgSend$isConditionMet
+ _objc_msgSend$setInterval:
+ _objc_msgSend$setPriority:
+ _objc_msgSend$setRequiresExternalPower:
+ _objc_msgSend$setRequiresProtectionClass:
+ _objc_msgSend$submitRequest:error:
+ _objc_retainBlock
- -[CHCoachingDiagnosticManager _queue_performRingCompletionDiagnostics].cold.1
- -[CHCoachingDiagnosticManager _queue_performRingCompletionDiagnostics].cold.2
- -[CHCoachingDiagnosticManager performPeriodicActivity:completion:]
- -[CHCoachingDiagnosticManager periodicActivity:configureXPCActivityCriteria:]
- -[CHCoachingDiagnosticManager periodicActivityRequiresProtectedData:]
- -[CHCompanionWidgetSchedulingManager associationsUpdatedForObject:subObject:type:objects:anchor:]
- -[CHCompanionWidgetSchedulingManager associationsUpdatedForObject:subObject:type:objects:anchor:].cold.1
- -[CHCompanionWidgetSchedulingManager associationsUpdatedForObject:subObject:type:objects:anchor:].cold.2
- -[CHCompanionWidgetSchedulingManager associationsUpdatedForObject:subObject:type:objects:anchor:].cold.3
- GCC_except_table12
- _OBJC_CLASS_$_HDPeriodicActivity
- _OBJC_IVAR_$_CHCoachingDiagnosticManager._scheduler
- _XPC_ACTIVITY_ALLOW_BATTERY
- _XPC_ACTIVITY_INTERVAL_8_HOURS
- _XPC_ACTIVITY_PRIORITY
- _XPC_ACTIVITY_PRIORITY_MAINTENANCE
- _XPC_ACTIVITY_REQUIRES_CLASS_A
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDAssociationObserver
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDPeriodicActivityDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HDPeriodicActivityDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_HDPeriodicActivityDelegate
- __OBJC_$_PROTOCOL_REFS_HDPeriodicActivityDelegate
- __OBJC_LABEL_PROTOCOL_$_HDPeriodicActivityDelegate
- __OBJC_PROTOCOL_$_HDPeriodicActivityDelegate
- ___56-[CHTrendsNotificationManager sendNotificationIfAllowed]_block_invoke.308
- ___66-[CHCoachingDiagnosticManager performPeriodicActivity:completion:]_block_invoke
- ___67-[CHCompanionWorkoutCreditManager _queue_performWorkoutCreditFixup]_block_invoke.319
- ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
- __os_log_debug_impl
- _objc_msgSend$initWithProfile:name:interval:delegate:loggingCategory:
- _objc_msgSend$isWaitingToRun
- _objc_msgSend$lastSuccessfulRunDate
- _xpc_dictionary_set_bool
- _xpc_dictionary_set_string
CStrings:
+ "\n\tExpected to submit: %@"
+ "@\"HDDatabaseAvailabilityCondition\""
+ "@\"HDRepeatingBackgroundTask\""
+ "Error submitting coaching diagnostic task request: %@"
+ "_databaseAvailableCondition"
+ "_lastRunDate"
+ "_repeatingBackgroundTask"
+ "associationsUpdatedForObject:subObject:type:behavior:objects:anchor:"
+ "getRequest"
+ "initWithDatabase:loggingCategory:"
+ "initWithIdentifier:"
+ "initWithName:loggingCategory:scheduler:handler:condition:"
+ "isConditionMet"
+ "setInterval:"
+ "setPriority:"
+ "setRequiresExternalPower:"
+ "setRequiresProtectionClass:"
+ "submitRequest:error:"
+ "v24@?0@\"HDRepeatingBackgroundTask\"8@?<v@?q@\"NSError\">16"
+ "v64@0:8@\"<HKAssociatableObject>\"16@\"<HKAssociatableObject>\"24Q32Q40@\"NSArray\"48@\"NSNumber\"56"
+ "v64@0:8@16@24Q32Q40@48@56"
- "@\"HDPeriodicActivity\""
- "B24@0:8@\"HDPeriodicActivity\"16"
- "HDPeriodicActivityDelegate"
- "_scheduler"
- "initWithProfile:name:interval:delegate:loggingCategory:"
- "isWaitingToRun"
- "lastSuccessfulRunDate"
- "performPeriodicActivity:completion:"
- "periodicActivity:configureXPCActivityCriteria:"
- "periodicActivityRequiresProtectedData:"
- "v32@0:8@\"HDPeriodicActivity\"16@\"NSObject<OS_xpc_object>\"24"
- "v32@0:8@\"HDPeriodicActivity\"16@?<v@?qd@\"NSError\">24"
- "v32@0:8@16@?24"

```
