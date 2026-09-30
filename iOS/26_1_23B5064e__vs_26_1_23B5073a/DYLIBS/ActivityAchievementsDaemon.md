## ActivityAchievementsDaemon

> `/System/Library/PrivateFrameworks/ActivityAchievementsDaemon.framework/ActivityAchievementsDaemon`

```diff

-2026.1.5.0.0
-  __TEXT.__text: 0x788cc
-  __TEXT.__auth_stubs: 0x1800
-  __TEXT.__objc_methlist: 0x60b4
-  __TEXT.__const: 0x868
+2026.1.5.1.1
+  __TEXT.__text: 0x790a8
+  __TEXT.__auth_stubs: 0x17f0
+  __TEXT.__objc_methlist: 0x6094
+  __TEXT.__const: 0x958
   __TEXT.__cstring: 0x6581
-  __TEXT.__gcc_except_tab: 0x2450
-  __TEXT.__oslogstring: 0x90cd
+  __TEXT.__gcc_except_tab: 0x2444
+  __TEXT.__oslogstring: 0x924d
   __TEXT.__swift5_typeref: 0x2f7
   __TEXT.__swift5_capture: 0x24
   __TEXT.__constg_swiftt: 0x180

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x68
   __TEXT.__swift5_types: 0x28
-  __TEXT.__unwind_info: 0x1f60
+  __TEXT.__unwind_info: 0x1f58
   __TEXT.__eh_frame: 0x438
   __TEXT.__objc_classname: 0xc7e
-  __TEXT.__objc_methname: 0x11abe
-  __TEXT.__objc_methtype: 0x2260
-  __TEXT.__objc_stubs: 0xa820
+  __TEXT.__objc_methname: 0x11a6e
+  __TEXT.__objc_methtype: 0x228d
+  __TEXT.__objc_stubs: 0xa7e0
   __DATA_CONST.__got: 0x758
   __DATA_CONST.__const: 0x2720
   __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37c0
+  __DATA_CONST.__objc_selrefs: 0x37b0
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x1c8
   __DATA_CONST.__objc_arraydata: 0x198
-  __AUTH_CONST.__auth_got: 0xc10
+  __AUTH_CONST.__auth_got: 0xc08
   __AUTH_CONST.__const: 0xcb8
   __AUTH_CONST.__cfstring: 0x2c60
-  __AUTH_CONST.__objc_const: 0x12050
+  __AUTH_CONST.__objc_const: 0x12020
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x280
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x720
-  __DATA.__data: 0x1088
+  __DATA.__objc_ivar: 0x71c
+  __DATA.__data: 0x1098
   __DATA.__bss: 0xdf0
   __DATA_DIRTY.__objc_data: 0x1450
-  __DATA_DIRTY.__data: 0x198
+  __DATA_DIRTY.__data: 0x188
   __DATA_DIRTY.__bss: 0x118
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4D92441D-B702-305F-80A7-D5B8D584D3DC
-  Functions: 2825
-  Symbols:   9209
-  CStrings:  4190
+  UUID: 784B8846-8EF5-31C7-AC3A-0B9F41FF02CF
+  Functions: 2824
+  Symbols:   9204
+  CStrings:  4194
 
Symbols:
+ -[ACHDataStorePropertyProviderSnapshot initWithDate:validThroughDate:version:properties:]
+ -[ACHDataStorePropertyProviderSnapshot initWithValidThroughDate:version:properties:]
+ -[ACHDataStorePropertyProviderSnapshot version]
+ -[ACHWorkoutAwardingSource _appendEarnedInstancesForWorkout:toSet:templates:calendar:numberOfDaysInWeek:predicates:firstDayOfFitnessWeek:watchCountryCode:error:]
+ -[ACHWorkoutAwardingSource _appendEarnedInstancesForWorkout:toSet:templates:calendar:numberOfDaysInWeek:predicates:firstDayOfFitnessWeek:watchCountryCode:error:].cold.1
+ -[ACHWorkoutAwardingSource _appendEarnedInstancesForWorkout:toSet:templates:calendar:numberOfDaysInWeek:predicates:firstDayOfFitnessWeek:watchCountryCode:error:].cold.2
+ -[ACHWorkoutAwardingSource _lock_createWorkoutEvaluationEnvironmentWithWorkout:firstDayOfFitnessWeek:numberOfDaysInWeek:calendar:error:]
+ -[ACHWorkoutAwardingSource _lock_createWorkoutEvaluationEnvironmentWithWorkout:firstDayOfFitnessWeek:numberOfDaysInWeek:calendar:error:].cold.1
+ -[ACHWorkoutAwardingSource _lock_createWorkoutEvaluationEnvironmentWithWorkout:firstDayOfFitnessWeek:numberOfDaysInWeek:calendar:error:].cold.2
+ _ACHCurrentDataStoreSnapshotVersion
+ _OBJC_IVAR_$_ACHDataStorePropertyProviderSnapshot._version
+ ___78-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:completion:]_block_invoke.407
+ ___78-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:completion:]_block_invoke.407.cold.1
+ ___block_descriptor_112_e8_32s40s48s56s64s72r80r88r_e19_B16?0"HKWorkout"8ls32l8r72l8s40l8s48l8s56l8s64l8r80l8r88l8
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ _objc_msgSend$_appendEarnedInstancesForWorkout:toSet:templates:calendar:numberOfDaysInWeek:predicates:firstDayOfFitnessWeek:watchCountryCode:error:
+ _objc_msgSend$_lock_createWorkoutEvaluationEnvironmentWithWorkout:firstDayOfFitnessWeek:numberOfDaysInWeek:calendar:error:
+ _objc_msgSend$initWithDate:validThroughDate:version:properties:
+ _objc_msgSend$initWithValidThroughDate:version:properties:
- -[ACHDataStorePropertyProviderSnapshot initWithDate:validThroughDate:properties:]
- -[ACHDataStorePropertyProviderSnapshot initWithValidThroughDate:properties:]
- -[ACHWorkoutAwardingSource _appendEarnedInstancesForWorkout:toSet:templates:calendar:numberOfDaysInWeek:predicates:firstDayOfFitnessWeek:watchCountryCode:]
- -[ACHWorkoutAwardingSource _appendEarnedInstancesForWorkout:toSet:templates:calendar:numberOfDaysInWeek:predicates:firstDayOfFitnessWeek:watchCountryCode:].cold.1
- -[ACHWorkoutAwardingSource _lock_createWorkoutEvaluationEnvironmentWithWorkout:firstDayOfFitnessWeek:numberOfDaysInWeek:calendar:]
- -[ACHWorkoutAwardingSource _lock_createWorkoutEvaluationEnvironmentWithWorkout:firstDayOfFitnessWeek:numberOfDaysInWeek:calendar:].cold.1
- -[ACHWorkoutAwardingSource _lock_createWorkoutEvaluationEnvironmentWithWorkout:firstDayOfFitnessWeek:numberOfDaysInWeek:calendar:].cold.2
- -[ACHWorkoutAwardingSource lastProcessedWorkoutEndDate]
- -[ACHWorkoutAwardingSource setLastProcessedWorkoutEndDate:]
- -[ACHWorkoutIterator query]
- -[ACHWorkoutIterator setQuery:]
- _OBJC_IVAR_$_ACHWorkoutAwardingSource._lastProcessedWorkoutEndDate
- _OBJC_IVAR_$_ACHWorkoutIterator._query
- ___78-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:completion:]_block_invoke.406.cold.1
- ___block_descriptor_104_e8_32s40s48s56s64s72r80r_e19_v16?0"HKWorkout"8ls32l8r72l8s40l8s48l8s56l8s64l8r80l8
- ___swift_instantiateConcreteTypeFromMangledName
- ___swift_instantiateConcreteTypeFromMangledNameAbstract
- _objc_msgSend$_appendEarnedInstancesForWorkout:toSet:templates:calendar:numberOfDaysInWeek:predicates:firstDayOfFitnessWeek:watchCountryCode:
- _objc_msgSend$_lock_createWorkoutEvaluationEnvironmentWithWorkout:firstDayOfFitnessWeek:numberOfDaysInWeek:calendar:
- _objc_msgSend$initWithDate:validThroughDate:properties:
- _objc_msgSend$initWithValidThroughDate:properties:
- _objc_msgSend$lastProcessedWorkoutEndDate
- _objc_msgSend$setLastProcessedWorkoutEndDate:
- _objc_setProperty_atomic
CStrings:
+ "1Z"
+ "@40@0:8@16q24@32"
+ "@48@0:8@16@24q32@40"
+ "@56@0:8@16q24Q32@40^@48"
+ "B16@?0@\"HKWorkout\"8"
+ "B88@0:8@16@24@32@40Q48@56q64@72^@80"
+ "Error creating evaluation environment not evaluating workout"
+ "Property provider %{public}@ doesn't have a valid through date, not saving a snapshot"
+ "Saving new snapshot for source: %{public}@ with value through date: %{public}@"
+ "Snapshot has version %ld which is lower than current version %ld, returning nil"
+ "Snapshot lookup error for source %@, not evaluating history: %@"
+ "There are no property providers registered, so not committing snapshot for %{public}@."
+ "Tq,R,V_version"
+ "_appendEarnedInstancesForWorkout:toSet:templates:calendar:numberOfDaysInWeek:predicates:firstDayOfFitnessWeek:watchCountryCode:error:"
+ "_lock_createWorkoutEvaluationEnvironmentWithWorkout:firstDayOfFitnessWeek:numberOfDaysInWeek:calendar:error:"
+ "_version"
+ "initWithDate:validThroughDate:version:properties:"
+ "initWithValidThroughDate:version:properties:"
- "1["
- "@48@0:8@16q24Q32@40"
- "Saving new snapshot for source: %@"
- "Snapshot lookup error for source %@: %@"
- "T@\"NSDate\",&,V_lastProcessedWorkoutEndDate"
- "_appendEarnedInstancesForWorkout:toSet:templates:calendar:numberOfDaysInWeek:predicates:firstDayOfFitnessWeek:watchCountryCode:"
- "_lastProcessedWorkoutEndDate"
- "_lock_createWorkoutEvaluationEnvironmentWithWorkout:firstDayOfFitnessWeek:numberOfDaysInWeek:calendar:"
- "initWithDate:validThroughDate:properties:"
- "initWithValidThroughDate:properties:"
- "lastProcessedWorkoutEndDate"
- "setLastProcessedWorkoutEndDate:"
- "v16@?0@\"HKWorkout\"8"
- "v80@0:8@16@24@32@40Q48@56q64@72"

```
