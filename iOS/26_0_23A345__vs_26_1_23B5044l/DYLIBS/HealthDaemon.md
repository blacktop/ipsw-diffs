## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-6106.1.2.11.0
-  __TEXT.__text: 0x790578
+6200.2.7.2.1
+  __TEXT.__text: 0x791648
   __TEXT.__auth_stubs: 0x4820
-  __TEXT.__objc_methlist: 0x43a54
-  __TEXT.__const: 0x1dd74
+  __TEXT.__objc_methlist: 0x43ab4
+  __TEXT.__const: 0x1df7c
   __TEXT.__dlopen_cstrs: 0x15b
-  __TEXT.__cstring: 0x7c2fd
-  __TEXT.__constg_swiftt: 0x14a4
-  __TEXT.__swift5_typeref: 0xd25
+  __TEXT.__cstring: 0x7d07f
+  __TEXT.__constg_swiftt: 0x14dc
+  __TEXT.__swift5_typeref: 0xd9d
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0x5fe
-  __TEXT.__swift5_fieldmd: 0x8d8
-  __TEXT.__swift5_types: 0xf0
-  __TEXT.__swift5_proto: 0xe0
+  __TEXT.__swift5_reflstr: 0x67e
+  __TEXT.__swift5_fieldmd: 0x970
+  __TEXT.__swift5_types: 0xf8
+  __TEXT.__swift5_proto: 0x100
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__swift5_capture: 0x5e4
-  __TEXT.__oslogstring: 0x41a30
+  __TEXT.__swift5_capture: 0x5c4
+  __TEXT.__oslogstring: 0x41a07
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_assocty: 0x90
+  __TEXT.__swift5_assocty: 0xf0
   __TEXT.__swift_as_entry: 0x48
   __TEXT.__swift_as_ret: 0x60
-  __TEXT.__gcc_except_tab: 0x38470
+  __TEXT.__gcc_except_tab: 0x38348
   __TEXT.__ustring: 0x70
-  __TEXT.__unwind_info: 0x1ccb0
+  __TEXT.__unwind_info: 0x1ccf8
   __TEXT.__eh_frame: 0x2310
-  __TEXT.__objc_classname: 0xc597
-  __TEXT.__objc_methname: 0x8ea14
-  __TEXT.__objc_methtype: 0x16af4
-  __TEXT.__objc_stubs: 0x504a0
-  __DATA_CONST.__got: 0x5650
+  __TEXT.__objc_classname: 0xc5c3
+  __TEXT.__objc_methname: 0x8eb18
+  __TEXT.__objc_methtype: 0x16b0a
+  __TEXT.__objc_stubs: 0x504e0
+  __DATA_CONST.__got: 0x5660
   __DATA_CONST.__const: 0x1d250
-  __DATA_CONST.__objc_classlist: 0x29c8
+  __DATA_CONST.__objc_classlist: 0x29d8
   __DATA_CONST.__objc_catlist: 0x4c0
   __DATA_CONST.__objc_protolist: 0x9b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19e98
+  __DATA_CONST.__objc_selrefs: 0x19eb0
   __DATA_CONST.__objc_protorefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0x1d88
-  __DATA_CONST.__objc_arraydata: 0x8478
+  __DATA_CONST.__objc_arraydata: 0x8498
   __AUTH_CONST.__auth_got: 0x2428
-  __AUTH_CONST.__const: 0xfe40
-  __AUTH_CONST.__cfstring: 0x3d400
-  __AUTH_CONST.__objc_const: 0x7d7d0
-  __AUTH_CONST.__objc_arrayobj: 0x1e90
+  __AUTH_CONST.__const: 0xffe0
+  __AUTH_CONST.__cfstring: 0x3d5c0
+  __AUTH_CONST.__objc_const: 0x7d940
+  __AUTH_CONST.__objc_arrayobj: 0x1ec0
   __AUTH_CONST.__objc_intobj: 0x3e58
   __AUTH_CONST.__objc_doubleobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH.__objc_data: 0xd398
+  __AUTH.__objc_data: 0xd438
   __AUTH.__data: 0x7e0
-  __DATA.__objc_ivar: 0x43ac
-  __DATA.__data: 0x8188
+  __DATA.__objc_ivar: 0x43b4
+  __DATA.__data: 0x81c8
   __DATA.__common: 0x64
-  __DATA.__bss: 0x14c8
+  __DATA.__bss: 0x18c8
   __DATA_DIRTY.__objc_ivar: 0xe80
   __DATA_DIRTY.__objc_data: 0xdfc8
   __DATA_DIRTY.__data: 0x1a0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 32FD3324-4565-30F3-AC69-553F06AA92B7
-  Functions: 34708
-  Symbols:   103822
-  CStrings:  44213
+  UUID: 06AD7B45-E726-3C72-A85C-FEEBB5799387
+  Functions: 34751
+  Symbols:   103866
+  CStrings:  44249
 
Symbols:
+ +[HDBQuantitySampleEntityBase columnDefinitionsWithCount:]
+ +[HDBQuantitySampleEntityBase insertDataObject:withProvenance:inDatabase:persistentID:error:]
+ +[HDBQuantitySampleEntityBase isConcreteEntity]
+ +[HDOHSEntityBase columnDefinitionsWithCount:]
+ +[HDOHSEntityBase insertDataObject:withProvenance:inDatabase:persistentID:error:]
+ +[HDOHSEntityBase isConcreteEntity]
+ -[HDAnchoredObjectQueryServer _supportedTypesForBackgroundRunningCollection]
+ -[HDQueryServer _supportedTypesForBackgroundRunningCollection]
+ -[HDSleepDaySummaryBuilder applicableSleepSchedules:]
+ -[HDSleepPeriodArrayBuilder _currentPeriodInterval]
+ -[HDWorkoutLocationSmoother _queue_smoothNextActivityForCurrentTask]
+ -[HDWorkoutLocationSmoother _queue_startSmoothingCurrentTask]
+ -[HDWorkoutLocationSmoother setUnitTest_smootherCompletionHandlerDidReturn:]
+ -[HDWorkoutLocationSmoother unitTest_smootherCompletionHandlerDidReturn]
+ _OBJC_CLASS_$_HDBQuantitySampleEntityBase
+ _OBJC_CLASS_$_HDOHSEntityBase
+ _OBJC_CLASS_$__TtC12HealthDaemon11HDOHSEntity
+ _OBJC_CLASS_$__TtC12HealthDaemon18HDHRCResultsEntity
+ _OBJC_CLASS_$__TtC12HealthDaemon18HDHREResultsEntity
+ _OBJC_CLASS_$__TtC12HealthDaemon23HDBQuantitySampleEntity
+ _OBJC_CLASS_$__TtC12HealthDaemon29HDHRFAMeasureCollectionEntity
+ _OBJC_IVAR_$_HDWorkoutLocationSmoother._queueCurrentSmoother
+ _OBJC_IVAR_$_HDWorkoutLocationSmoother._unitTest_smootherCompletionHandlerDidReturn
+ _OBJC_METACLASS_$_HDBQuantitySampleEntityBase
+ _OBJC_METACLASS_$_HDOHSEntityBase
+ _OBJC_METACLASS_$__TtC12HealthDaemon11HDOHSEntity
+ _OBJC_METACLASS_$__TtC12HealthDaemon18HDHRCResultsEntity
+ _OBJC_METACLASS_$__TtC12HealthDaemon18HDHREResultsEntity
+ _OBJC_METACLASS_$__TtC12HealthDaemon23HDBQuantitySampleEntity
+ _OBJC_METACLASS_$__TtC12HealthDaemon29HDHRFAMeasureCollectionEntity
+ __CLASS_METHODS__TtC12HealthDaemon11HDOHSEntity
+ __CLASS_METHODS__TtC12HealthDaemon18HDHRCResultsEntity
+ __CLASS_METHODS__TtC12HealthDaemon18HDHREResultsEntity
+ __CLASS_METHODS__TtC12HealthDaemon23HDBQuantitySampleEntity
+ __CLASS_METHODS__TtC12HealthDaemon29HDHRFAMeasureCollectionEntity
+ __DATA__TtC12HealthDaemon11HDOHSEntity
+ __DATA__TtC12HealthDaemon18HDHRCResultsEntity
+ __DATA__TtC12HealthDaemon18HDHREResultsEntity
+ __DATA__TtC12HealthDaemon23HDBQuantitySampleEntity
+ __DATA__TtC12HealthDaemon29HDHRFAMeasureCollectionEntity
+ __HDAddBQuantitySampleTable
+ __HDAddHKHRSampleTablesPhase2
+ __HDAddOHSTable
+ __HDRemoveSingleBloodPressureAuthorizations
+ __HDResetMismatchedBloodPressureAuthorizations
+ __INSTANCE_METHODS__TtC12HealthDaemon11HDOHSEntity
+ __INSTANCE_METHODS__TtC12HealthDaemon18HDHRCResultsEntity
+ __INSTANCE_METHODS__TtC12HealthDaemon18HDHREResultsEntity
+ __INSTANCE_METHODS__TtC12HealthDaemon23HDBQuantitySampleEntity
+ __INSTANCE_METHODS__TtC12HealthDaemon29HDHRFAMeasureCollectionEntity
+ __METACLASS_DATA__TtC12HealthDaemon11HDOHSEntity
+ __METACLASS_DATA__TtC12HealthDaemon18HDHRCResultsEntity
+ __METACLASS_DATA__TtC12HealthDaemon18HDHREResultsEntity
+ __METACLASS_DATA__TtC12HealthDaemon23HDBQuantitySampleEntity
+ __METACLASS_DATA__TtC12HealthDaemon29HDHRFAMeasureCollectionEntity
+ __OBJC_$_CLASS_METHODS_HDBQuantitySampleEntityBase
+ __OBJC_$_CLASS_METHODS_HDOHSEntityBase
+ __OBJC_CLASS_RO_$_HDBQuantitySampleEntityBase
+ __OBJC_CLASS_RO_$_HDOHSEntityBase
+ __OBJC_METACLASS_RO_$_HDBQuantitySampleEntityBase
+ __OBJC_METACLASS_RO_$_HDOHSEntityBase
+ ___46-[HDSourceManager localDeviceSourceWithError:]_block_invoke_2
+ ___53-[HDSleepDaySummaryBuilder applicableSleepSchedules:]_block_invoke
+ ___65-[HDCreateWorkoutOperation performWithProfile:transaction:error:]_block_invoke_2.313
+ ___68-[HDWorkoutLocationSmoother _queue_smoothNextActivityForCurrentTask]_block_invoke
+ ___71-[HDDefaultWorkoutSessionController _takeLiveActivityAssertionIfNeeded]_block_invoke
+ ___72-[HDDefaultWorkoutSessionController _queue_collectFinalDataThroughDate:]_block_invoke.423
+ ___72-[HDDefaultWorkoutSessionController _queue_collectFinalDataThroughDate:]_block_invoke.425
+ ___72-[HDDefaultWorkoutSessionController _queue_collectFinalDataThroughDate:]_block_invoke.426
+ ___75-[HDWorkoutBasicDataSource workoutSession:didChangeToState:fromState:date:]_block_invoke.443
+ ___94-[HDWorkoutBasicDataSource _workoutDataDestination:requestsSamplesOfType:from:to:transaction:]_block_invoke.435
+ ___block_descriptor_40_e8_32s_e14_v32?0q8q16d24ls32l8
+ ___block_descriptor_56_e8_32s40bs48r_e35_B24?0"HDDatabaseTransaction"8^16ls40l8r48l8s32l8
+ ___block_descriptor_64_e8_32s40s48w56w_e29_v24?0"NSArray"8"NSError"16lw48l8w56l8s32l8s40l8
+ ___block_descriptor_64_ea8_32s40s48s56bs_e70_B40?0"HDDatabaseTransaction"8"HDSQLitePredicate"16"NSString"24^32ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e72_B32?0"HDStatisticsCollectionCalculator"8"HKQuantityType"16"NSUUID"24ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72w_e29_v24?0"NSArray"8"NSError"16lw72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72w_e5_v8?0lw72l8s32l8s40l8s64l8s48l8s56l8
+ _associated conformance 12HealthDaemon11HDOHSEntityC8PropertyOSHAASQ
+ _associated conformance 12HealthDaemon11HDOHSEntityC8PropertyOs12CaseIterableAA8AllCasessAFP_Sl
+ _associated conformance 12HealthDaemon23HDBQuantitySampleEntityC8PropertyOSHAASQ
+ _associated conformance 12HealthDaemon23HDBQuantitySampleEntityC8PropertyOs12CaseIterableAA8AllCasessAFP_Sl
+ _objc_msgSend$_supportedTypesForBackgroundRunningCollection
+ _objc_msgSend$applicableSleepSchedules:
+ _objc_msgSend$unitTest_smootherCompletionHandlerDidReturn
+ _symbolic Say_____G 12HealthDaemon11HDOHSEntityC8PropertyO
+ _symbolic Say_____G 12HealthDaemon23HDBQuantitySampleEntityC8PropertyO
+ _symbolic So15HDOHSEntityBaseC
+ _symbolic So27HDBQuantitySampleEntityBaseC
+ _symbolic _____ 12HealthDaemon11HDOHSEntityC
+ _symbolic _____ 12HealthDaemon11HDOHSEntityC8PropertyO
+ _symbolic _____ 12HealthDaemon18HDHRCResultsEntityC
+ _symbolic _____ 12HealthDaemon18HDHREResultsEntityC
+ _symbolic _____ 12HealthDaemon23HDBQuantitySampleEntityC
+ _symbolic _____ 12HealthDaemon23HDBQuantitySampleEntityC8PropertyO
+ _symbolic _____ 12HealthDaemon29HDHRFAMeasureCollectionEntityC
- -[HDSleepDaySummaryBuilder applicableSleepSchedules]
- -[HDWorkoutBuilderEntity _createTemporaryProtectedAssociatedSampleListInTransaction:error:]
- -[HDWorkoutLocationSmoother _queue_smoothNextActivityForTask:]
- -[HDWorkoutLocationSmoother _queue_startSmoothingTaskAttempt:]
- _OBJC_CLASS_$__TtC12HealthDaemon20HDHRIndicatorEEntity
- _OBJC_CLASS_$__TtC12HealthDaemon27HDHRIndicatorCResultsEntity
- _OBJC_CLASS_$__TtC12HealthDaemon27HDHRIndicatorEResultsEntity
- _OBJC_CLASS_$__TtC12HealthDaemon30HDHRFAAMeasureCollectionEntity
- _OBJC_CLASS_$__TtC12HealthDaemon30HDHRFABMeasureCollectionEntity
- _OBJC_METACLASS_$__TtC12HealthDaemon20HDHRIndicatorEEntity
- _OBJC_METACLASS_$__TtC12HealthDaemon27HDHRIndicatorCResultsEntity
- _OBJC_METACLASS_$__TtC12HealthDaemon27HDHRIndicatorEResultsEntity
- _OBJC_METACLASS_$__TtC12HealthDaemon30HDHRFAAMeasureCollectionEntity
- _OBJC_METACLASS_$__TtC12HealthDaemon30HDHRFABMeasureCollectionEntity
- __CLASS_METHODS__TtC12HealthDaemon20HDHRIndicatorEEntity
- __CLASS_METHODS__TtC12HealthDaemon27HDHRIndicatorCResultsEntity
- __CLASS_METHODS__TtC12HealthDaemon27HDHRIndicatorEResultsEntity
- __CLASS_METHODS__TtC12HealthDaemon30HDHRFAAMeasureCollectionEntity
- __CLASS_METHODS__TtC12HealthDaemon30HDHRFABMeasureCollectionEntity
- __DATA__TtC12HealthDaemon20HDHRIndicatorEEntity
- __DATA__TtC12HealthDaemon27HDHRIndicatorCResultsEntity
- __DATA__TtC12HealthDaemon27HDHRIndicatorEResultsEntity
- __DATA__TtC12HealthDaemon30HDHRFAAMeasureCollectionEntity
- __DATA__TtC12HealthDaemon30HDHRFABMeasureCollectionEntity
- __HDAddBilateralQuantitySampleTable
- __HDAddOverheadSquatTable
- __INSTANCE_METHODS__TtC12HealthDaemon20HDHRIndicatorEEntity
- __INSTANCE_METHODS__TtC12HealthDaemon27HDHRIndicatorCResultsEntity
- __INSTANCE_METHODS__TtC12HealthDaemon27HDHRIndicatorEResultsEntity
- __INSTANCE_METHODS__TtC12HealthDaemon30HDHRFAAMeasureCollectionEntity
- __INSTANCE_METHODS__TtC12HealthDaemon30HDHRFABMeasureCollectionEntity
- __METACLASS_DATA__TtC12HealthDaemon20HDHRIndicatorEEntity
- __METACLASS_DATA__TtC12HealthDaemon27HDHRIndicatorCResultsEntity
- __METACLASS_DATA__TtC12HealthDaemon27HDHRIndicatorEResultsEntity
- __METACLASS_DATA__TtC12HealthDaemon30HDHRFAAMeasureCollectionEntity
- __METACLASS_DATA__TtC12HealthDaemon30HDHRFABMeasureCollectionEntity
- ___52-[HDSleepDaySummaryBuilder applicableSleepSchedules]_block_invoke
- ___62-[HDWorkoutLocationSmoother _queue_smoothNextActivityForTask:]_block_invoke
- ___65-[HDCreateWorkoutOperation performWithProfile:transaction:error:]_block_invoke.313
- ___72-[HDDefaultWorkoutSessionController _queue_collectFinalDataThroughDate:]_block_invoke.418
- ___72-[HDDefaultWorkoutSessionController _queue_collectFinalDataThroughDate:]_block_invoke.419
- ___72-[HDDefaultWorkoutSessionController _queue_collectFinalDataThroughDate:]_block_invoke.421
- ___75-[HDWorkoutBasicDataSource workoutSession:didChangeToState:fromState:date:]_block_invoke.439
- ___79-[HDDefaultWorkoutSessionController _setLiveActivityBackgroundAssertionTimeout]_block_invoke
- ___92-[HDWorkoutBuilderEntity _simplerSetupForEnumerationOfTypes:interval:profile:error:handler:]_block_invoke
- ___94-[HDWorkoutBasicDataSource _workoutDataDestination:requestsSamplesOfType:from:to:transaction:]_block_invoke.431
- ___95-[HDWorkoutBuilderEntity _fasterSetupForEnumerationOfTypes:interval:transaction:error:handler:]_block_invoke
- ___block_descriptor_48_e8_32s40r_e14_v32?0q8q16d24lr40l8s32l8
- ___block_descriptor_56_e8_32s40s_e34_v16?0"<HDProfileReadyObserver>"8ls32l8u48l8s40l8
- ___block_descriptor_56_ea8_32s40s48bs_e9_B16?0^8ls48l8s32l8s40l8
- ___block_descriptor_64_ea8_32s40s48s56bs_e48_B32?0"HDDatabaseTransaction"8"NSString"16^24ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s72l8s56l8s64l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80r88r_e72_B32?0"HDStatisticsCollectionCalculator"8"HKQuantityType"16"NSUUID"24ls32l8s40l8s48l8r80l8s56l8r88l8s64l8s72l8
- _objc_msgSend$applicableSleepSchedules
- _symbolic _____ 12HealthDaemon20HDHRIndicatorEEntityC
- _symbolic _____ 12HealthDaemon27HDHRIndicatorCResultsEntityC
- _symbolic _____ 12HealthDaemon27HDHRIndicatorEResultsEntityC
- _symbolic _____ 12HealthDaemon30HDHRFAAMeasureCollectionEntityC
- _symbolic _____ 12HealthDaemon30HDHRFABMeasureCollectionEntityC
CStrings:
+ "%{public}@: Live Activity assertion already taken."
+ "+[HDBQuantitySampleEntityBase insertDataObject:withProvenance:inDatabase:persistentID:error:]"
+ "+[HDOHSEntityBase insertDataObject:withProvenance:inDatabase:persistentID:error:]"
+ "<Workout UUID=%@ \ntotalLocations=%tu \nTask Creation Date=%@ \nTask Start Date=%@ \nAttempts=%lu \nError=%@>"
+ "@\"CLLocationSmoother\""
+ "AND samples.start_date >= %f"
+ "CREATE TABLE IF NOT EXISTS hr_c_results           (           ROWID                         INTEGER PRIMARY KEY AUTOINCREMENT,           data_id                       INTEGER         NOT NULL REFERENCES samples (data_id) ON DELETE CASCADE,           source                        TEXT            NOT NULL,           measure_identifier            TEXT            NOT NULL,           level_id                      TEXT            NOT NULL,           quantity_value                REAL,                               unit_string                   TEXT,                               scale_level_ids               BLOB,                               thresholds                    BLOB,                               score                         REAL,                               start_date                    REAL            NOT NULL,           end_date                      REAL            NOT NULL,           contributing_data             BLOB                            )"
+ "CREATE TABLE IF NOT EXISTS hr_e_results           (           ROWID                     INTEGER PRIMARY KEY AUTOINCREMENT,           data_id                   INTEGER         NOT NULL REFERENCES samples (data_id) ON DELETE CASCADE,           source                    TEXT            NOT NULL,           e_identifier              TEXT            NOT NULL,           contributing_data         BLOB                            )"
+ "CREATE TABLE IF NOT EXISTS hr_f_a_measure_collection         (         ROWID                   INTEGER PRIMARY KEY AUTOINCREMENT,         type                    TEXT            NOT NULL,         f_a_identifier          BLOB            NOT NULL,         measure_identifier      TEXT            NOT NULL      )"
+ "CREATE TABLE b_quantity_samples (data_id INTEGER PRIMARY KEY REFERENCES samples (data_id) ON DELETE CASCADE, a_value REAL, a_original_value REAL, b_value REAL, b_original_value REAL, original_unit INTEGER REFERENCES unit_strings(ROWID))"
+ "CREATE TABLE ohs_samples (data_id INTEGER PRIMARY KEY REFERENCES samples (data_id) ON DELETE CASCADE, has_ad INTEGER NOT NULL, has_ftl INTEGER NOT NULL, has_kninp INTEGER NOT NULL, has_ssd INTEGER NOT NULL, has_hs INTEGER NOT NULL)"
+ "DELETE FROM authorization                                         WHERE (source_id, object_type) IN (                                             SELECT source_id, object_type                                             FROM authorization                                             WHERE object_type IN (16, 17)                                             GROUP BY source_id                                             HAVING COUNT(DISTINCT object_type) = 1)"
+ "DROP TABLE IF EXISTS b_quantity_samples"
+ "DROP TABLE IF EXISTS hr_c_results"
+ "DROP TABLE IF EXISTS hr_e_results"
+ "DROP TABLE IF EXISTS hr_f_a_measure_collection"
+ "DROP TABLE IF EXISTS ohs_samples"
+ "HDBQuantitySampleEntityBase"
+ "HDBQuantitySampleEntityBase.m"
+ "HDOHSEntityBase"
+ "HDOHSEntityBase.m"
+ "T@?,C,N,V_unitTest_smootherCompletionHandlerDidReturn"
+ "TimeOut: %f seconds \nTaskDuration: %f seconds \n\nDevice: %@ \n\nTask:\n%@ \n\nWorkout: %@"
+ "UPDATE authorization                                     SET status = 100                                     WHERE EXISTS (                                         SELECT 1                                         FROM authorization AS a2                                         WHERE authorization.source_id = a2.source_id                                             AND authorization.object_type IN (16, 17)                                             AND a2.object_type IN (16, 17)                                             AND authorization.object_type != a2.object_type                                             AND authorization.status != a2.status                                     )"
+ "[routes]: Calling smoother (%{public}@) for activity %{public}@ with %lu location points"
+ "[routes]: Previously timed out smoother (%{public}@) eventually returned, igorning result"
+ "[routes]: Smoother (%{public}@) did finish for activity %{public}@ with error: %{public}@"
+ "_TtC12HealthDaemon11HDOHSEntity"
+ "_TtC12HealthDaemon18HDHRCResultsEntity"
+ "_TtC12HealthDaemon18HDHREResultsEntity"
+ "_TtC12HealthDaemon23HDBQuantitySampleEntity"
+ "_TtC12HealthDaemon29HDHRFAMeasureCollectionEntity"
+ "_queueCurrentSmoother"
+ "_supportedTypesForBackgroundRunningCollection"
+ "_unitTest_smootherCompletionHandlerDidReturn"
+ "a_original_value"
+ "a_value"
+ "applicableSleepSchedules:"
+ "b_original_value"
+ "b_quantity_samples"
+ "b_value"
+ "has_ad"
+ "has_ftl"
+ "has_hs"
+ "has_kninp"
+ "has_ssd"
+ "hr_f_a_measure_collection"
+ "setUnitTest_smootherCompletionHandlerDidReturn:"
+ "unitTest_smootherCompletionHandlerDidReturn"
- "<%@:%p> Notified profile ready observer %@ in %0.1f seconds"
- "<%@:%p> Notifying profile ready observer %@"
- "<Workout UUID=%@ \ntotalLocations=%tu \nTask Creation Date=%@ \nTask Start Date=%@>"
- "AND (samples.start_date >= %f) AND (samples.start_date <= %f) AND (samples.end_date >= %f)"
- "B32@?0@\"HDDatabaseTransaction\"8@\"NSString\"16^@24"
- "Failed to get the dataInterval for %{public}@ at workout end; will exit existing statistics: %{public}@"
- "TimeOut: %f seconds \nTaskDuration: %f seconds \n\nWorkout: %@ \n\nTask:\n%@"
- "[routes]: Calling smoother for activity %{public}@ with %lu location points"
- "[routes]: Smoother did finish for activity %{public}@ with error: %{public}@"
- "_TtC12HealthDaemon20HDHRIndicatorEEntity"
- "_TtC12HealthDaemon27HDHRIndicatorCResultsEntity"
- "_TtC12HealthDaemon27HDHRIndicatorEResultsEntity"
- "_TtC12HealthDaemon30HDHRFAAMeasureCollectionEntity"
- "_TtC12HealthDaemon30HDHRFABMeasureCollectionEntity"
- "a_measure_identifier"
- "applicableSleepSchedules"
- "b_measure_identifier"
- "hr_f_a_a_measure_collection"
- "hr_f_a_b_measure_collection"
- "hr_indicator_c_results"
- "hr_indicator_e_results"
- "indicator_e_results_id"
- "indicator_e_results_row_id"
- "level_id"
- "quantity_value"
- "scale_level_ids"
- "thresholds"

```
