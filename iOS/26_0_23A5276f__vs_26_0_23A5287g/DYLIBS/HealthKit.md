## HealthKit

> `/System/Library/Frameworks/HealthKit.framework/HealthKit`

```diff

-6087.1.2.1.0
-  __TEXT.__text: 0x332050
+6093.0.0.0.0
+  __TEXT.__text: 0x33280c
   __TEXT.__auth_stubs: 0x36b0
-  __TEXT.__objc_methlist: 0x2f77c
-  __TEXT.__cstring: 0x348e3
-  __TEXT.__const: 0xabd22
-  __TEXT.__oslogstring: 0xc053
+  __TEXT.__objc_methlist: 0x2f7bc
+  __TEXT.__cstring: 0x34923
+  __TEXT.__const: 0xabd62
+  __TEXT.__oslogstring: 0xc0e3
   __TEXT.__gcc_except_tab: 0x40e0
   __TEXT.__ustring: 0x78
   __TEXT.__dlopen_cstrs: 0x5da
   __TEXT.__constg_swiftt: 0x2ffc
-  __TEXT.__swift5_typeref: 0x2c8d
+  __TEXT.__swift5_typeref: 0x2cad
   __TEXT.__swift5_fieldmd: 0x2d28
   __TEXT.__swift5_builtin: 0x398
-  __TEXT.__swift5_reflstr: 0x1ed2
-  __TEXT.__swift5_assocty: 0xb60
-  __TEXT.__swift5_proto: 0xbdc
+  __TEXT.__swift5_reflstr: 0x1ee2
+  __TEXT.__swift5_assocty: 0xb78
+  __TEXT.__swift5_proto: 0xbe0
   __TEXT.__swift5_types: 0x408
   __TEXT.__swift5_capture: 0x77c
   __TEXT.__swift_as_entry: 0x14c
   __TEXT.__swift_as_ret: 0x14c
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0xf8e0
+  __TEXT.__unwind_info: 0xf8e8
   __TEXT.__eh_frame: 0x3fe8
-  __TEXT.__objc_classname: 0x896e
-  __TEXT.__objc_methname: 0x5d207
-  __TEXT.__objc_methtype: 0xbf12
-  __TEXT.__objc_stubs: 0x2b140
+  __TEXT.__objc_classname: 0x8970
+  __TEXT.__objc_methname: 0x5d363
+  __TEXT.__objc_methtype: 0xbf15
+  __TEXT.__objc_stubs: 0x2b1c0
   __DATA_CONST.__got: 0x1b00
-  __DATA_CONST.__const: 0xf480
+  __DATA_CONST.__const: 0xf4a0
   __DATA_CONST.__objc_classlist: 0x1aa0
   __DATA_CONST.__objc_catlist: 0x1c0
   __DATA_CONST.__objc_protolist: 0x7f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11280
+  __DATA_CONST.__objc_selrefs: 0x112a8
   __DATA_CONST.__objc_protorefs: 0x608
   __DATA_CONST.__objc_superrefs: 0x1728
   __DATA_CONST.__objc_arraydata: 0x68e8
   __AUTH_CONST.__auth_got: 0x1b70
-  __AUTH_CONST.__const: 0xb960
-  __AUTH_CONST.__cfstring: 0x31fa0
-  __AUTH_CONST.__objc_const: 0x4fa90
+  __AUTH_CONST.__const: 0xb980
+  __AUTH_CONST.__cfstring: 0x31fc0
+  __AUTH_CONST.__objc_const: 0x4faf0
   __AUTH_CONST.__objc_intobj: 0x4590
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_doubleobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x6d8
   __AUTH.__objc_data: 0xe9c0
   __AUTH.__data: 0x1988
-  __DATA.__objc_ivar: 0x2db8
+  __DATA.__objc_ivar: 0x2dc0
   __DATA.__data: 0xce38
-  __DATA.__bss: 0x182b0
+  __DATA.__bss: 0x18340
   __DATA.__common: 0x9a8
   __DATA_DIRTY.__objc_data: 0x2430
   __DATA_DIRTY.__data: 0x130

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 37DB915A-6155-32FD-BB37-8131C797EBA1
-  Functions: 23875
-  Symbols:   60666
-  CStrings:  29665
+  UUID: 1A05FFF3-9FBA-3753-BB2A-5D5E703778BD
+  Functions: 23887
+  Symbols:   60695
+  CStrings:  29678
 
Symbols:
+ +[HKMedicationDoseEvent _newMedicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationUUID:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:logStatus:doseUnitString:config:]
+ +[HKMedicationDoseEvent medicationDoseEventWithLogOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:startDate:logStatus:doseUnitString:metadata:]
+ +[HKMedicationDoseEvent(UnitTestSupport) medicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:logStatus:medicationUuid:]
+ +[HKMedicationDoseEvent(UnitTestSupport) medicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:logStatus:medicationUuid:doseUnitString:]
+ +[HKSleepDaySummary daySummaryWithMorningIndex:dateInterval:calendar:periods:schedules:sleepDurationGoal:minimumRecommendedSleepDurationGoal:creationInterval:]
+ -[HKMedicationDoseEvent _setLogStatus:]
+ -[HKSleepDaySummary initWithMorningIndex:dateInterval:calendar:periods:schedules:sleepDurationGoal:minimumRecommendedSleepDurationGoal:creationInterval:]
+ -[HKSleepDaySummary minimumRecommendedSleepDurationGoal]
+ -[NSDateComponents(HKDayIndex) _hk_hasValidDayIndexComponents]
+ -[NSDateComponents(HKDayIndex) hk_dayIndexByAddingYears:gregorianCalendar:]
+ -[_HKExpiringCompletionTimer initWithName:queue:completion:]
+ -[_HKExpiringCompletionTimer name]
+ _HKLogDaemonInitialization
+ _HKLogDaemonInitialization.category
+ _HKLogDaemonInitialization.cold.1
+ _HKLogDaemonInitialization.onceToken
+ _HKSleepDurationGoalAdultRecommendation
+ _HKSleepDurationGoalChildRecommendation
+ _OBJC_IVAR_$_HKMedicationDoseEvent._logStatus
+ _OBJC_IVAR_$_HKSleepDaySummary._minimumRecommendedSleepDurationGoal
+ _OBJC_IVAR_$__HKExpiringCompletionTimer._name
+ ___241+[HKMedicationDoseEvent _newMedicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationUUID:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:logStatus:doseUnitString:config:]_block_invoke
+ ___45-[HKWorkoutSession client_didGenerateEvents:]_block_invoke.238
+ ___45-[HKWorkoutSession endCurrentActivityOnDate:]_block_invoke.289
+ ___45-[HKWorkoutSession endCurrentActivityOnDate:]_block_invoke.289.cold.1
+ ___65-[HKWorkoutSession stopMirroringToCompanionDeviceWithCompletion:]_block_invoke.301
+ ___65-[HKWorkoutSession stopMirroringToCompanionDeviceWithCompletion:]_block_invoke.301.cold.1
+ ___66-[HKWorkoutSession startMirroringToCompanionDeviceWithCompletion:]_block_invoke.300
+ ___66-[HKWorkoutSession startMirroringToCompanionDeviceWithCompletion:]_block_invoke.300.cold.1
+ ___68-[HKWorkoutSession beginNewActivityWithConfiguration:date:metadata:]_block_invoke.288
+ ___68-[HKWorkoutSession beginNewActivityWithConfiguration:date:metadata:]_block_invoke.288.cold.1
+ ___70-[HKWorkoutSession _queue_sendPendingDataUpdateToRemoteWorkoutSession]_block_invoke.306
+ ___70-[HKWorkoutSession _queue_sendPendingDataUpdateToRemoteWorkoutSession]_block_invoke.306.cold.1
+ ___70-[HKWorkoutSession enableAutomaticDetectionForActivityConfigurations:]_block_invoke.284
+ ___70-[HKWorkoutSession enableAutomaticDetectionForActivityConfigurations:]_block_invoke.287
+ ___70-[HKWorkoutSession enableAutomaticDetectionForActivityConfigurations:]_block_invoke.287.cold.1
+ ___70-[HKWorkoutSession enableAutomaticDetectionForActivityConfigurations:]_block_invoke_2.286
+ ___71-[HKWorkoutSession client_didDisconnectFromRemoteWithError:completion:]_block_invoke.261
+ ___76-[HKWorkoutSession stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.274
+ ___76-[HKWorkoutSession stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.274.cold.1
+ ___77-[HKWorkoutSession client_didReceiveDataFromRemoteWorkoutSession:completion:]_block_invoke.250
+ ___HKLogDaemonInitialization_block_invoke
+ ___block_descriptor_tmp.183
+ ___block_literal_global.185
+ ___block_literal_global.264
+ ___block_literal_global.283
+ _associated conformance 9HealthKit8DayIndexVs12IdentifiableAA2IDsADP_SH
+ _objc_msgSend$_hk_hasValidDayIndexComponents
+ _objc_msgSend$_newMedicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationUUID:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:logStatus:doseUnitString:config:
+ _objc_msgSend$_setLogStatus:
+ _objc_msgSend$daySummaryWithMorningIndex:dateInterval:calendar:periods:schedules:sleepDurationGoal:minimumRecommendedSleepDurationGoal:creationInterval:
+ _objc_msgSend$initWithMorningIndex:dateInterval:calendar:periods:schedules:sleepDurationGoal:minimumRecommendedSleepDurationGoal:creationInterval:
+ _objc_msgSend$logStatus
+ _objc_msgSend$minimumRecommendedSleepDurationGoal
+ _symbolic $ss12IdentifiableP
- +[HKMedicationDoseEvent _newMedicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationUUID:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:status:doseUnitString:config:]
- +[HKMedicationDoseEvent medicationDoseEventWithLogOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:startDate:status:doseUnitString:metadata:]
- +[HKMedicationDoseEvent(UnitTestSupport) medicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:status:medicationUuid:]
- +[HKMedicationDoseEvent(UnitTestSupport) medicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:status:medicationUuid:doseUnitString:]
- +[HKSleepDaySummary daySummaryWithMorningIndex:dateInterval:calendar:periods:schedules:sleepDurationGoal:creationInterval:]
- -[HKMedicationDoseEvent _setStatus:]
- -[HKSleepDaySummary initWithMorningIndex:dateInterval:calendar:periods:schedules:sleepDurationGoal:creationInterval:]
- _OBJC_IVAR_$_HKMedicationDoseEvent._status
- ___238+[HKMedicationDoseEvent _newMedicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationUUID:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:status:doseUnitString:config:]_block_invoke
- ___45-[HKWorkoutSession client_didGenerateEvents:]_block_invoke_2
- ___45-[HKWorkoutSession endCurrentActivityOnDate:]_block_invoke.287
- ___45-[HKWorkoutSession endCurrentActivityOnDate:]_block_invoke.287.cold.1
- ___65-[HKWorkoutSession stopMirroringToCompanionDeviceWithCompletion:]_block_invoke.299
- ___65-[HKWorkoutSession stopMirroringToCompanionDeviceWithCompletion:]_block_invoke.299.cold.1
- ___66-[HKWorkoutSession startMirroringToCompanionDeviceWithCompletion:]_block_invoke.298
- ___66-[HKWorkoutSession startMirroringToCompanionDeviceWithCompletion:]_block_invoke.298.cold.1
- ___68-[HKWorkoutSession beginNewActivityWithConfiguration:date:metadata:]_block_invoke.286
- ___68-[HKWorkoutSession beginNewActivityWithConfiguration:date:metadata:]_block_invoke.286.cold.1
- ___70-[HKWorkoutSession _queue_sendPendingDataUpdateToRemoteWorkoutSession]_block_invoke.304
- ___70-[HKWorkoutSession _queue_sendPendingDataUpdateToRemoteWorkoutSession]_block_invoke.304.cold.1
- ___70-[HKWorkoutSession enableAutomaticDetectionForActivityConfigurations:]_block_invoke.282
- ___70-[HKWorkoutSession enableAutomaticDetectionForActivityConfigurations:]_block_invoke.285
- ___70-[HKWorkoutSession enableAutomaticDetectionForActivityConfigurations:]_block_invoke.285.cold.1
- ___70-[HKWorkoutSession enableAutomaticDetectionForActivityConfigurations:]_block_invoke_2.284
- ___71-[HKWorkoutSession client_didDisconnectFromRemoteWithError:completion:]_block_invoke.259
- ___76-[HKWorkoutSession stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.272
- ___76-[HKWorkoutSession stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.272.cold.1
- ___77-[HKWorkoutSession client_didReceiveDataFromRemoteWorkoutSession:completion:]_block_invoke_2
- ___block_literal_global.262
- ___block_literal_global.281
- _objc_msgSend$_newMedicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationUUID:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:status:doseUnitString:config:
- _objc_msgSend$daySummaryWithMorningIndex:dateInterval:calendar:periods:schedules:sleepDurationGoal:creationInterval:
- _objc_msgSend$initWithMorningIndex:dateInterval:calendar:periods:schedules:sleepDurationGoal:creationInterval:
CStrings:
+ "%{public}@: Did generate %lu events. Notifying client"
+ "<%@:%p %@ (%@ - %@), goal = %@/%@, schedules = %@, periods = %@, calendar = %@>"
+ "@80@0:8q16@24@32@40@48@56@64@72"
+ "MinimumRecommendedSleepDurationGoal"
+ "T@\"HKQuantity\",R,C,N,V_minimumRecommendedSleepDurationGoal"
+ "[mirroring] %{public}@: Did receive data from remote session. Notifying client"
+ "_hk_hasValidDayIndexComponents"
+ "_logStatus"
+ "_minimumRecommendedSleepDurationGoal"
+ "_newMedicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationUUID:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:logStatus:doseUnitString:config:"
+ "_setLogStatus:"
+ "daemon_initialization"
+ "daySummaryWithMorningIndex:dateInterval:calendar:periods:schedules:sleepDurationGoal:minimumRecommendedSleepDurationGoal:creationInterval:"
+ "hk_dayIndexByAddingYears:gregorianCalendar:"
+ "initWithMorningIndex:dateInterval:calendar:periods:schedules:sleepDurationGoal:minimumRecommendedSleepDurationGoal:creationInterval:"
+ "initWithName:queue:completion:"
+ "medicationDoseEventWithLogOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:startDate:logStatus:doseUnitString:metadata:"
+ "medicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:logStatus:medicationUuid:"
+ "medicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:logStatus:medicationUuid:doseUnitString:"
+ "minimumRecommendedSleepDurationGoal"
- "<%@:%p %@ (%@ - %@), goal = %@, schedules = %@, periods = %@, calendar = %@>"
- "@72@0:8q16@24@32@40@48@56@64"
- "_newMedicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationUUID:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:status:doseUnitString:config:"
- "daySummaryWithMorningIndex:dateInterval:calendar:periods:schedules:sleepDurationGoal:creationInterval:"
- "initWithMorningIndex:dateInterval:calendar:periods:schedules:sleepDurationGoal:creationInterval:"
- "medicationDoseEventWithLogOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:startDate:status:doseUnitString:metadata:"
- "medicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:status:medicationUuid:"
- "medicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:status:medicationUuid:doseUnitString:"

```
