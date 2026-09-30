## HealthMedicationsDaemonPlugin

> `/System/Library/PrivateFrameworks/HealthMedicationsDaemonPlugin.framework/HealthMedicationsDaemonPlugin`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0x55574
+6074.1.2.4.0
+  __TEXT.__text: 0x56d48
   __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x44b4
-  __TEXT.__const: 0x190
-  __TEXT.__cstring: 0x6581
-  __TEXT.__gcc_except_tab: 0xa90
-  __TEXT.__oslogstring: 0x60cd
+  __TEXT.__objc_methlist: 0x451c
+  __TEXT.__const: 0x198
+  __TEXT.__cstring: 0x6569
+  __TEXT.__gcc_except_tab: 0xaa4
+  __TEXT.__oslogstring: 0x626b
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__unwind_info: 0x13c8
   __TEXT.__objc_classname: 0x120a
-  __TEXT.__objc_methname: 0xeee5
-  __TEXT.__objc_methtype: 0x2693
-  __TEXT.__objc_stubs: 0x8980
-  __DATA_CONST.__got: 0x830
-  __DATA_CONST.__const: 0x1c38
+  __TEXT.__objc_methname: 0xf103
+  __TEXT.__objc_methtype: 0x2689
+  __TEXT.__objc_stubs: 0x8b00
+  __DATA_CONST.__got: 0x818
+  __DATA_CONST.__const: 0x1c60
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ec8
+  __DATA_CONST.__objc_selrefs: 0x2f40
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x2d8
   __AUTH_CONST.__auth_got: 0x5c0
   __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__cfstring: 0x34a0
-  __AUTH_CONST.__objc_const: 0x7898
+  __AUTH_CONST.__cfstring: 0x3480
+  __AUTH_CONST.__objc_const: 0x78f0
   __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x390
+  __DATA.__objc_ivar: 0x394
   __DATA.__data: 0x1140
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x15e0

   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
+  - /System/Library/PrivateFrameworks/HealthContentDaemon.framework/HealthContentDaemon
   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon
   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
   - /System/Library/PrivateFrameworks/HealthMedications.framework/HealthMedications

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: B4E443D8-C7C1-3207-B178-E3938182B070
-  Functions: 1895
-  Symbols:   6781
-  CStrings:  3511
+  UUID: 3EDBD653-02BD-3B52-8FD1-26905041E6F1
+  Functions: 1908
+  Symbols:   6788
+  CStrings:  3530
 
Symbols:
+ +[HDCloudSyncStateUpdaterMedicationScheduleDelegate _canPersistCloudSchedule:profile:transaction:error:]
+ +[HDCloudSyncStateUpdaterMedicationScheduleDelegate _makeUnvailableSchedulesIntoNonNilLocalState:transaction:error:]
+ +[HDMedicationScheduleEntity canPersistSchedule:profile:transaction:error:]
+ +[HDMedicationScheduleManager _newDoseEventWithGeneratedMetadataLogOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:startDate:status:doseUnitString:isLastScheduledDose:]
+ +[HDMedicationUserDomainConceptEntity _predicateForSchedulesWithAMedicationsUUIDWithSubqueryDescriptor:]
+ +[HDMedicationUserDomainConceptEntity _predicateForSemanticIdsInSchedulesWithSubqueryDescriptor:]
+ +[HDMedicationUserDomainConceptEntity _queryDescriptorForNonDeletedSchedules]
+ +[HDMedicationUserDomainConceptEntity generateUserAnnotatedMedicationForUserDomainConcept:userAnnotatedMedicationOut:transaction:error:]
+ +[HDMedicationUserDomainConceptEntity predicateForHasSchedule:]
+ +[HDMedicationUserDomainConceptEntity supportsUserAnnotatedMedicationAPIObjectGeneration]
+ -[HDCloudSyncStateUpdaterMedicationScheduleDelegate .cxx_destruct]
+ -[HDCloudSyncStateUpdaterMedicationScheduleDelegate _callUnitTestingWillPersistHandler:]
+ -[HDCloudSyncStateUpdaterMedicationScheduleDelegate _persistCloudState:profile:error:]
+ -[HDCloudSyncStateUpdaterMedicationScheduleDelegate setUnitTesting_willPersistHandler:]
+ -[HDCloudSyncStateUpdaterMedicationScheduleDelegate unitTesting_willPersistHandler]
+ -[HDCodableMedicationScheduleCollection(StateSync) addSchedulesFrom:]
+ -[HDCodableMedicationScheduleData(StateSync) isLocallyTerminallyUnavailable]
+ -[HDMedicationsDemoDataGenerator asNeededDoseEventsForMedication:startDateTime:historyDayCount:doseUnitString:]
+ -[HDMedicationsDemoDataGenerator doseEventWithLogOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:startDate:status:doseUnitString:]
+ -[HDMedicationsDemoDataGenerator doseEventsForMedication:startDateTime:historyDayCount:logOrigin:doseUnitString:]
+ -[HDMedicationsDemoDataGenerator scheduledDoseEventsForMedication:startDateTime:historyDayCount:doseUnitString:]
+ _HDSQLEntityPropertyStar
+ _OBJC_CLASS_$_HKUserAnnotatedMedication
+ _OBJC_IVAR_$_HDCloudSyncStateUpdaterMedicationScheduleDelegate._unitTesting_willPersistHandler
+ __OBJC_$_INSTANCE_METHODS_HDCodableMedicationScheduleCollection(StateSync)
+ __OBJC_$_INSTANCE_VARIABLES_HDCloudSyncStateUpdaterMedicationScheduleDelegate
+ __OBJC_$_PROP_LIST_HDDrugInteractionFactorStateProvider.370
+ __OBJC_$_PROP_LIST_HDMedicationCountProvider.381
+ ___104+[HDCloudSyncStateUpdaterMedicationScheduleDelegate _canPersistCloudSchedule:profile:transaction:error:]_block_invoke
+ ___65-[HDMedicationsDeviceScopedStorageManager profileDidBecomeReady:]_block_invoke.311
+ ___68-[HDMedicationPeriodicScheduler performPeriodicActivity:completion:]_block_invoke.336
+ ___86-[HDCloudSyncStateUpdaterMedicationScheduleDelegate _persistCloudState:profile:error:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48s56r_e9_B16?0^8ls32l8r56l8s40l8s48l8
+ ___block_literal_global.340
+ ___block_literal_global.347
+ ___block_literal_global.357
+ ___block_literal_global.369
+ ___block_literal_global.381
+ ___block_literal_global.383
+ ___block_literal_global.386
+ ___block_literal_global.388
+ ___block_literal_global.391
+ ___block_literal_global.430
+ ___block_literal_global.467
+ _objc_msgSend$_setError
+ _objc_msgSend$addSchedulesFrom:
+ _objc_msgSend$asNeededDoseEventsForMedication:startDateTime:historyDayCount:doseUnitString:
+ _objc_msgSend$canPersistSchedule:profile:transaction:error:
+ _objc_msgSend$canonicalDoseUnitString
+ _objc_msgSend$doseEventWithLogOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:startDate:status:doseUnitString:
+ _objc_msgSend$doseEventsForMedication:startDateTime:historyDayCount:logOrigin:doseUnitString:
+ _objc_msgSend$doseUnitString
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$initWithNickname:isArchived:hasSchedule:medication:
+ _objc_msgSend$isLocallyTerminallyUnavailable
+ _objc_msgSend$medicationConcept
+ _objc_msgSend$medicationDoseEventWithLogOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:startDate:status:doseUnitString:metadata:
+ _objc_msgSend$medicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:status:medicationUuid:doseUnitString:
+ _objc_msgSend$position
+ _objc_msgSend$scheduledDoseEventsForMedication:startDateTime:historyDayCount:doseUnitString:
+ _objc_msgSend$setPosition:
- +[HDCloudSyncStateUpdaterMedicationScheduleDelegate _persistCloudState:profile:error:]
- +[HDMedicationScheduleManager _newDoseEventWithGeneratedMetadataLogOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:startDate:status:isLastScheduledDose:]
- -[HDMedicationDailyAnalyticsEvent _fetchFeatureSettingsAnalyticsWithDataSource:]
- -[HDMedicationScheduleDailyAnalytics _makeMedicationPayloadForConfigurationsWithProfile:]
- -[HDMedicationsDemoDataGenerator asNeededDoseEventsForMedication:startDateTime:historyDayCount:]
- -[HDMedicationsDemoDataGenerator doseEventWithLogOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:startDate:status:]
- -[HDMedicationsDemoDataGenerator doseEventsForMedication:startDateTime:historyDayCount:logOrigin:]
- -[HDMedicationsDemoDataGenerator scheduledDoseEventsForMedication:startDateTime:historyDayCount:]
- GCC_except_table13
- GCC_except_table17
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _OUTLINED_FUNCTION_28
- __OBJC_$_INSTANCE_METHODS_HDCodableMedicationScheduleCollection
- __OBJC_$_PROP_LIST_HDDrugInteractionFactorStateProvider.364
- __OBJC_$_PROP_LIST_HDMedicationCountProvider.375
- ___65-[HDMedicationsDeviceScopedStorageManager profileDidBecomeReady:]_block_invoke.308
- ___68-[HDMedicationPeriodicScheduler performPeriodicActivity:completion:]_block_invoke.330
- ___86+[HDCloudSyncStateUpdaterMedicationScheduleDelegate _persistCloudState:profile:error:]_block_invoke
- ___block_literal_global.334
- ___block_literal_global.335
- ___block_literal_global.351
- ___block_literal_global.363
- ___block_literal_global.371
- ___block_literal_global.375
- ___block_literal_global.379
- ___block_literal_global.380
- ___block_literal_global.382
- ___block_literal_global.424
- ___block_literal_global.461
- _objc_msgSend$asNeededDoseEventsForMedication:startDateTime:historyDayCount:
- _objc_msgSend$doseEventWithLogOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:startDate:status:
- _objc_msgSend$doseEventsForMedication:startDateTime:historyDayCount:logOrigin:
- _objc_msgSend$medicationDoseEventWithLogOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:startDate:status:metadata:
- _objc_msgSend$medicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:status:medicationUuid:
- _objc_msgSend$scheduledDoseEventsForMedication:startDateTime:historyDayCount:
- _objc_retain_x7
CStrings:
+ "%{public}@: Update cloud by dropping cloud schedule (%f, %lld, %lld), compatibility: %ld"
+ "%{public}@: Update cloud with local schedule (%f, %lld, %lld) replacing cloud schedule (%f, %lld, %lld), compatibility: %ld"
+ "%{public}@: Update local with cloud schedule (%f, %lld, %lld) replacing local schedule (%f, %lld, %lld), compatibility: %ld"
+ "@20@0:8B16"
+ "@48@0:8@16@24Q32@40"
+ "@56@0:8@16@24Q32q40@48"
+ "@88@0:8q16@24@32@40@48@56@64q72@80"
+ "T@?,C,N,V_unitTesting_willPersistHandler"
+ "[%{public}@] Found %ld unavailable local medication schedules for state sync"
+ "_setError"
+ "_unitTesting_willPersistHandler"
+ "addSchedulesFrom:"
+ "asNeededDoseEventsForMedication:startDateTime:historyDayCount:doseUnitString:"
+ "associationsUpdatedForObject:subObject:type:behavior:objects:anchor:"
+ "canPersistSchedule:profile:transaction:error:"
+ "canonicalDoseUnitString"
+ "doseEventWithLogOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:startDate:status:doseUnitString:"
+ "doseEventsForMedication:startDateTime:historyDayCount:logOrigin:doseUnitString:"
+ "doseUnitString"
+ "generateUserAnnotatedMedicationForUserDomainConcept:userAnnotatedMedicationOut:transaction:error:"
+ "getBytes:range:"
+ "hasError"
+ "initWithNickname:isArchived:hasSchedule:medication:"
+ "invalidateAndWait"
+ "isLocallyTerminallyUnavailable"
+ "medicationConcept"
+ "medicationDoseEventWithLogOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:startDate:status:doseUnitString:metadata:"
+ "medicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:status:medicationUuid:doseUnitString:"
+ "position"
+ "predicateForHasSchedule:"
+ "scheduledDoseEventsForMedication:startDateTime:historyDayCount:doseUnitString:"
+ "setPosition:"
+ "setUnitTesting_willPersistHandler:"
+ "supportsUserAnnotatedMedicationAPIObjectGeneration"
+ "unitTesting_willPersistHandler"
+ "v64@0:8@\"<HKAssociatableObject>\"16@\"<HKAssociatableObject>\"24Q32Q40@\"NSArray\"48@\"NSNumber\"56"
+ "v64@0:8@16@24Q32Q40@48@56"
- "@40@0:8@16@24Q32"
- "@48@0:8@16@24Q32q40"
- "@80@0:8q16@24@32@40@48@56@64q72"
- "_fetchFeatureSettingsAnalyticsWithDataSource:"
- "_makeMedicationPayloadForConfigurationsWithProfile:"
- "asNeededDoseEventsForMedication:startDateTime:historyDayCount:"
- "doseEventWithLogOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:startDate:status:"
- "doseEventsForMedication:startDateTime:historyDayCount:logOrigin:"
- "hasPregnancyModeEnabled"
- "medicationDoseEventWithLogOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:startDate:status:metadata:"
- "medicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:status:medicationUuid:"
- "nextSyncAnchorWithSession:predicate:startSyncAnchor:profile:error:"
- "q48@0:8@\"NSArray\"16@\"<HDSyncStore>\"24@\"HDProfile\"32^@40"
- "q56@0:8@\"HDSyncSession\"16@\"HDSQLitePredicate\"24q32@\"HDProfile\"40^@48"
- "q56@0:8@16@24q32@40^@48"
- "receiveSyncObjects:syncStore:profile:error:"
- "scheduledDoseEventsForMedication:startDateTime:historyDayCount:"

```
