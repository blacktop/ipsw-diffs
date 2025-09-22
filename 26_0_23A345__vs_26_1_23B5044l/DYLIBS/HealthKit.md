## HealthKit

> `/System/Library/Frameworks/HealthKit.framework/HealthKit`

```diff

-6106.1.2.11.0
-  __TEXT.__text: 0x341ff4
-  __TEXT.__auth_stubs: 0x37a0
-  __TEXT.__objc_methlist: 0x2fc14
-  __TEXT.__cstring: 0x35a13
+6200.2.7.2.1
+  __TEXT.__text: 0x348500
+  __TEXT.__auth_stubs: 0x3790
+  __TEXT.__objc_methlist: 0x3031c
+  __TEXT.__cstring: 0x35d23
   __TEXT.__const: 0xac5c2
-  __TEXT.__oslogstring: 0xc623
-  __TEXT.__gcc_except_tab: 0x4138
+  __TEXT.__oslogstring: 0xc703
+  __TEXT.__gcc_except_tab: 0x4218
   __TEXT.__ustring: 0x78
   __TEXT.__dlopen_cstrs: 0x644
   __TEXT.__constg_swiftt: 0x3064

   __TEXT.__swift_as_ret: 0x174
   __TEXT.__swift5_protos: 0x50
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0xfc98
+  __TEXT.__unwind_info: 0xfe10
   __TEXT.__eh_frame: 0x4628
-  __TEXT.__objc_classname: 0x89e6
-  __TEXT.__objc_methname: 0x5ddef
-  __TEXT.__objc_methtype: 0xbfad
-  __TEXT.__objc_stubs: 0x2b4a0
-  __DATA_CONST.__got: 0x1b58
-  __DATA_CONST.__const: 0xf678
-  __DATA_CONST.__objc_classlist: 0x1ad0
+  __TEXT.__objc_classname: 0x8a0d
+  __TEXT.__objc_methname: 0x5f5ed
+  __TEXT.__objc_methtype: 0xc05d
+  __TEXT.__objc_stubs: 0x2bfc0
+  __DATA_CONST.__got: 0x1b68
+  __DATA_CONST.__const: 0xf6c8
+  __DATA_CONST.__objc_classlist: 0x1ae0
   __DATA_CONST.__objc_catlist: 0x1c0
   __DATA_CONST.__objc_protolist: 0x808
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x114a8
+  __DATA_CONST.__objc_selrefs: 0x118b8
   __DATA_CONST.__objc_protorefs: 0x618
-  __DATA_CONST.__objc_superrefs: 0x1730
-  __DATA_CONST.__objc_arraydata: 0x6958
-  __AUTH_CONST.__auth_got: 0x1be8
+  __DATA_CONST.__objc_superrefs: 0x1738
+  __DATA_CONST.__objc_arraydata: 0x6968
+  __AUTH_CONST.__auth_got: 0x1be0
   __AUTH_CONST.__const: 0xc6a0
-  __AUTH_CONST.__cfstring: 0x326a0
-  __AUTH_CONST.__objc_const: 0x50260
-  __AUTH_CONST.__objc_intobj: 0x4608
+  __AUTH_CONST.__cfstring: 0x32aa0
+  __AUTH_CONST.__objc_const: 0x50968
+  __AUTH_CONST.__objc_intobj: 0x4620
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_doubleobj: 0x140
-  __AUTH_CONST.__objc_arrayobj: 0x720
-  __AUTH.__objc_data: 0xec40
+  __AUTH_CONST.__objc_arrayobj: 0x750
+  __AUTH.__objc_data: 0xece0
   __AUTH.__data: 0x19a8
-  __DATA.__objc_ivar: 0x2dec
+  __DATA.__objc_ivar: 0x2e6c
   __DATA.__data: 0xd0c8
   __DATA.__bss: 0x18c60
   __DATA.__common: 0x9c0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 45984941-72CA-30C0-8EC5-20DC2936C6AE
-  Functions: 24208
-  Symbols:   60976
-  CStrings:  29980
+  UUID: B5C8056B-B05F-389C-8D3E-1E312724BCBF
+  Functions: 24353
+  Symbols:   61436
+  CStrings:  30235
 
Symbols:
+ +[HKSleepMetrics sleepMetricsWithMorningIndexRange:sleepAnalysisAsleepCount:sleepAnalysisInBedCount:sleepAnalysisCount:averageSleepDuration:averageInBedDuration:averageREMSleepDuration:averageCoreSleepDuration:averageDeepSleepDuration:averageUnspecifiedSleepDuration:averageAwakeDuration:bedtimeAchievedCount:sleepDurationGoalAchievedCount:sleepDurationGoalStreakCount:averageBedtimeMiss:averageSleepDurationGoalMiss:averageBedtime:averageWakeTime:averageInBedStartTime:averageInBedEndTime:averageSleepStartTime:averageSleepEndTime:standardDeviationActualTimeAsleep:standardDeviationScheduledTimeAsleep:standardDeviationActualVsScheduledTimeAsleep:averageSleepStartOffset:averageSleepEndOffset:averageInBedStartOffset:averageInBedEndOffset:]
+ +[HKSleepMetrics supportsSecureCoding]
+ +[HKSleepMetricsEngine _computeStandardDeviationFor:]
+ +[HKSleepMetricsEngine _dateComponentsForInterval:sinceDate:calendar:]
+ +[HKSleepMetricsEngine _firstAsleepSegment:]
+ +[HKSleepMetricsEngine _firstInBedSegment:]
+ +[HKSleepMetricsEngine _firstSegmentMatchingSleepValues:inPeriods:]
+ +[HKSleepMetricsEngine _generateConsiderationIntervalFromDaySummaries:morningIndexRange:]
+ +[HKSleepMetricsEngine _generateStrategyWithSleepDayInterval:considerationInterval:]
+ +[HKSleepMetricsEngine _lastAsleepSegment:]
+ +[HKSleepMetricsEngine _lastInBedSegment:]
+ +[HKSleepMetricsEngine _lastSegmentMatchingSleepValues:inPeriods:]
+ +[HKSleepMetricsEngine _timeIntervalForDate:sinceDate:calendar:]
+ +[HKSleepMetricsEngine sleepMetricsForDaySummaries:]
+ +[HKSleepMetricsEngine sleepMetricsForDaySummaries:inMorningIndexRange:]
+ -[HKActivityCache _lock_activeHoursGoalCount]
+ -[HKActivityCache _lock_activeHoursGoalPercentage]
+ -[HKActivityCache _lock_activeHoursGoal]
+ -[HKActivityCache _lock_activeHours]
+ -[HKActivityCache _lock_activityMoveMode]
+ -[HKActivityCache _lock_briskMinutesGoalInMinutes]
+ -[HKActivityCache _lock_briskMinutesGoalPercentage]
+ -[HKActivityCache _lock_briskMinutesGoal]
+ -[HKActivityCache _lock_briskMinutes]
+ -[HKActivityCache _lock_cacheIndex]
+ -[HKActivityCache _lock_dailyBriskMinutesStatistics]
+ -[HKActivityCache _lock_dailyEnergyBurnedStatistics]
+ -[HKActivityCache _lock_dailyMoveMinutesStatistics]
+ -[HKActivityCache _lock_dateComponents]
+ -[HKActivityCache _lock_deepBreathingDuration]
+ -[HKActivityCache _lock_endDate]
+ -[HKActivityCache _lock_energyBurnedGoalDate]
+ -[HKActivityCache _lock_energyBurnedGoalInKilocalories]
+ -[HKActivityCache _lock_energyBurnedGoalPercentage]
+ -[HKActivityCache _lock_energyBurnedGoal]
+ -[HKActivityCache _lock_energyBurnedInKilocalories]
+ -[HKActivityCache _lock_energyBurned]
+ -[HKActivityCache _lock_fallbackActiveHoursGoal]
+ -[HKActivityCache _lock_fallbackBriskMinutesGoal]
+ -[HKActivityCache _lock_flightsClimbed]
+ -[HKActivityCache _lock_hasActiveHoursGoalDate]
+ -[HKActivityCache _lock_hasActiveHoursGoal]
+ -[HKActivityCache _lock_hasActiveHours]
+ -[HKActivityCache _lock_hasBriskMinutesGoalDate]
+ -[HKActivityCache _lock_hasBriskMinutesGoal]
+ -[HKActivityCache _lock_hasBriskMinutes]
+ -[HKActivityCache _lock_hasDailyBriskMinutesStatistics]
+ -[HKActivityCache _lock_hasDailyEnergyBurnedStatistics]
+ -[HKActivityCache _lock_hasDailyMoveMinutesStatistics]
+ -[HKActivityCache _lock_hasDateComponents]
+ -[HKActivityCache _lock_hasDeepBreathingDuration]
+ -[HKActivityCache _lock_hasEnergyBurnedGoal]
+ -[HKActivityCache _lock_hasEnergyBurned]
+ -[HKActivityCache _lock_hasFlightsClimbed]
+ -[HKActivityCache _lock_hasMoveMinutesGoal]
+ -[HKActivityCache _lock_hasMoveMinutes]
+ -[HKActivityCache _lock_hasPushCount]
+ -[HKActivityCache _lock_hasStepCount]
+ -[HKActivityCache _lock_hasWalkingAndRunningDistance]
+ -[HKActivityCache _lock_hasWheelchairUse]
+ -[HKActivityCache _lock_isEqualToActivityCache:]
+ -[HKActivityCache _lock_isPaused]
+ -[HKActivityCache _lock_knownFields]
+ -[HKActivityCache _lock_metadata]
+ -[HKActivityCache _lock_moveMinutesGoalDate]
+ -[HKActivityCache _lock_moveMinutesGoalInMinutes]
+ -[HKActivityCache _lock_moveMinutesGoalPercentage]
+ -[HKActivityCache _lock_moveMinutesGoal]
+ -[HKActivityCache _lock_moveMinutes]
+ -[HKActivityCache _lock_pushCount]
+ -[HKActivityCache _lock_sequence]
+ -[HKActivityCache _lock_setActiveHours:]
+ -[HKActivityCache _lock_setActiveHoursGoal:date:]
+ -[HKActivityCache _lock_setActiveHoursGoal:date:].cold.1
+ -[HKActivityCache _lock_setActiveHoursGoalDateOnly:]
+ -[HKActivityCache _lock_setActiveHoursGoalOnly:]
+ -[HKActivityCache _lock_setActivityMoveMode:]
+ -[HKActivityCache _lock_setActivityMoveMode:].cold.1
+ -[HKActivityCache _lock_setBriskMinutes:]
+ -[HKActivityCache _lock_setBriskMinutesGoal:date:]
+ -[HKActivityCache _lock_setBriskMinutesGoal:date:].cold.1
+ -[HKActivityCache _lock_setBriskMinutesGoalDateOnly:]
+ -[HKActivityCache _lock_setBriskMinutesGoalOnly:]
+ -[HKActivityCache _lock_setCacheIndex:]
+ -[HKActivityCache _lock_setDailyBriskMinutesStatistics:]
+ -[HKActivityCache _lock_setDailyEnergyBurnedStatistics:]
+ -[HKActivityCache _lock_setDailyMoveMinutesStatistics:]
+ -[HKActivityCache _lock_setDeepBreathingDuration:]
+ -[HKActivityCache _lock_setEndDate:]
+ -[HKActivityCache _lock_setEnergyBurned:]
+ -[HKActivityCache _lock_setEnergyBurnedGoal:date:]
+ -[HKActivityCache _lock_setEnergyBurnedGoalDateOnly:]
+ -[HKActivityCache _lock_setEnergyBurnedGoalOnly:]
+ -[HKActivityCache _lock_setFlightsClimbed:]
+ -[HKActivityCache _lock_setMetadata:]
+ -[HKActivityCache _lock_setMoveMinutes:]
+ -[HKActivityCache _lock_setMoveMinutesGoal:date:]
+ -[HKActivityCache _lock_setMoveMinutesGoalDateOnly:]
+ -[HKActivityCache _lock_setMoveMinutesGoalOnly:]
+ -[HKActivityCache _lock_setPaused:]
+ -[HKActivityCache _lock_setPushCount:]
+ -[HKActivityCache _lock_setSequence:]
+ -[HKActivityCache _lock_setStartDate:]
+ -[HKActivityCache _lock_setStepCount:]
+ -[HKActivityCache _lock_setVersion:]
+ -[HKActivityCache _lock_setWalkingAndRunningDistance:]
+ -[HKActivityCache _lock_setWheelchairUse:]
+ -[HKActivityCache _lock_startDate]
+ -[HKActivityCache _lock_stepCount]
+ -[HKActivityCache _lock_version]
+ -[HKActivityCache _lock_walkingAndRunningDistanceInMeters]
+ -[HKActivityCache _lock_walkingAndRunningDistance]
+ -[HKActivityCache _lock_wheelchairUse]
+ -[HKActivityCache _setEndDate:]
+ -[HKActivityCache _setMetadata:]
+ -[HKActivityCache _setStartDate:]
+ -[HKActivityCache endDate]
+ -[HKActivityCache metadata]
+ -[HKActivityCache startDate]
+ -[HKCorrelation _validateWithConfiguration:].cold.1
+ -[HKCorrelation _validateWithConfiguration:].cold.2
+ -[HKHealthStore _typesWithBothBloodPressureIfNeeded:]
+ -[HKHealthStore _typesWithBothBloodPressureIfNeeded:].cold.1
+ -[HKHealthStoreImplementation _typesWithBothBloodPressureIfNeeded:]
+ -[HKHealthStoreImplementation _typesWithBothBloodPressureIfNeeded:].cold.1
+ -[HKSleepMetrics .cxx_destruct]
+ -[HKSleepMetrics averageAwakeDuration]
+ -[HKSleepMetrics averageBedtimeMiss]
+ -[HKSleepMetrics averageBedtime]
+ -[HKSleepMetrics averageCoreSleepDuration]
+ -[HKSleepMetrics averageDeepSleepDuration]
+ -[HKSleepMetrics averageInBedDuration]
+ -[HKSleepMetrics averageInBedEndOffset]
+ -[HKSleepMetrics averageInBedEndTime]
+ -[HKSleepMetrics averageInBedStartOffset]
+ -[HKSleepMetrics averageInBedStartTime]
+ -[HKSleepMetrics averageREMSleepDuration]
+ -[HKSleepMetrics averageSleepDurationGoalMiss]
+ -[HKSleepMetrics averageSleepDuration]
+ -[HKSleepMetrics averageSleepEndOffset]
+ -[HKSleepMetrics averageSleepEndTime]
+ -[HKSleepMetrics averageSleepStartOffset]
+ -[HKSleepMetrics averageSleepStartTime]
+ -[HKSleepMetrics averageUnspecifiedSleepDuration]
+ -[HKSleepMetrics averageWakeTime]
+ -[HKSleepMetrics bedtimeAchievedCount]
+ -[HKSleepMetrics encodeWithCoder:]
+ -[HKSleepMetrics hash]
+ -[HKSleepMetrics initWithCoder:]
+ -[HKSleepMetrics isEqual:]
+ -[HKSleepMetrics morningIndexRange]
+ -[HKSleepMetrics sleepAnalysisAsleepCount]
+ -[HKSleepMetrics sleepAnalysisCount]
+ -[HKSleepMetrics sleepAnalysisInBedCount]
+ -[HKSleepMetrics sleepDurationGoalAchievedCount]
+ -[HKSleepMetrics sleepDurationGoalStreakCount]
+ -[HKSleepMetrics standardDeviationActualTimeAsleep]
+ -[HKSleepMetrics standardDeviationActualVsScheduledTimeAsleep]
+ -[HKSleepMetrics standardDeviationScheduledTimeAsleep]
+ -[HKSleepMetricsEngine .cxx_destruct]
+ -[HKSleepMetricsEngine fetchSleepMetricsForMorningIndexRange:completion:]
+ -[HKSleepMetricsEngine initWithHealthStore:]
+ -[_HKBehavior enableBloodPressureValidations]
+ -[_HKBehavior setEnableBloodPressureValidations:]
+ -[_HKFeatureFlags bloodPressureValidationsEnabled]
+ -[_HKFeatureFlags setBloodPressureValidationsEnabled:]
+ -[_HKFeatureFlags setSleepResultsNotificationsOnWatch:]
+ -[_HKFeatureFlags sleepResultsNotificationsOnWatch]
+ GCC_except_table152
+ GCC_except_table164
+ GCC_except_table174
+ GCC_except_table175
+ GCC_except_table212
+ GCC_except_table214
+ GCC_except_table269
+ GCC_except_table270
+ _HKSleepCopyViaSecureCoding
+ _HKSleepDurationGoalLeeway
+ _HKSleepStandardDeviationDecimalPrecision
+ _HKSleepTestScheduleWithMetadata
+ _OBJC_CLASS_$_HKSleepMetrics
+ _OBJC_CLASS_$_HKSleepMetricsEngine
+ _OBJC_IVAR_$_HKActivityCache._lock
+ _OBJC_IVAR_$_HKJSONValidator._ivarLock
+ _OBJC_IVAR_$_HKSleepMetrics._averageAwakeDuration
+ _OBJC_IVAR_$_HKSleepMetrics._averageBedtime
+ _OBJC_IVAR_$_HKSleepMetrics._averageBedtimeMiss
+ _OBJC_IVAR_$_HKSleepMetrics._averageCoreSleepDuration
+ _OBJC_IVAR_$_HKSleepMetrics._averageDeepSleepDuration
+ _OBJC_IVAR_$_HKSleepMetrics._averageInBedDuration
+ _OBJC_IVAR_$_HKSleepMetrics._averageInBedEndOffset
+ _OBJC_IVAR_$_HKSleepMetrics._averageInBedEndTime
+ _OBJC_IVAR_$_HKSleepMetrics._averageInBedStartOffset
+ _OBJC_IVAR_$_HKSleepMetrics._averageInBedStartTime
+ _OBJC_IVAR_$_HKSleepMetrics._averageREMSleepDuration
+ _OBJC_IVAR_$_HKSleepMetrics._averageSleepDuration
+ _OBJC_IVAR_$_HKSleepMetrics._averageSleepDurationGoalMiss
+ _OBJC_IVAR_$_HKSleepMetrics._averageSleepEndOffset
+ _OBJC_IVAR_$_HKSleepMetrics._averageSleepEndTime
+ _OBJC_IVAR_$_HKSleepMetrics._averageSleepStartOffset
+ _OBJC_IVAR_$_HKSleepMetrics._averageSleepStartTime
+ _OBJC_IVAR_$_HKSleepMetrics._averageUnspecifiedSleepDuration
+ _OBJC_IVAR_$_HKSleepMetrics._averageWakeTime
+ _OBJC_IVAR_$_HKSleepMetrics._bedtimeAchievedCount
+ _OBJC_IVAR_$_HKSleepMetrics._morningIndexRange
+ _OBJC_IVAR_$_HKSleepMetrics._sleepAnalysisAsleepCount
+ _OBJC_IVAR_$_HKSleepMetrics._sleepAnalysisCount
+ _OBJC_IVAR_$_HKSleepMetrics._sleepAnalysisInBedCount
+ _OBJC_IVAR_$_HKSleepMetrics._sleepDurationGoalAchievedCount
+ _OBJC_IVAR_$_HKSleepMetrics._sleepDurationGoalStreakCount
+ _OBJC_IVAR_$_HKSleepMetrics._standardDeviationActualTimeAsleep
+ _OBJC_IVAR_$_HKSleepMetrics._standardDeviationActualVsScheduledTimeAsleep
+ _OBJC_IVAR_$_HKSleepMetrics._standardDeviationScheduledTimeAsleep
+ _OBJC_IVAR_$_HKSleepMetricsEngine._healthStore
+ _OBJC_IVAR_$__HKFeatureFlags._bloodPressureValidationsEnabled
+ _OBJC_IVAR_$__HKFeatureFlags._sleepResultsNotificationsOnWatch
+ _OBJC_METACLASS_$_HKSleepMetrics
+ _OBJC_METACLASS_$_HKSleepMetricsEngine
+ __HKSleepSafeAverageDurationRoundedToNearestMinute
+ __OBJC_$_CLASS_METHODS_HKSleepMetrics
+ __OBJC_$_CLASS_METHODS_HKSleepMetricsEngine
+ __OBJC_$_CLASS_PROP_LIST_HKSleepMetrics
+ __OBJC_$_INSTANCE_METHODS_HKSleepMetrics
+ __OBJC_$_INSTANCE_METHODS_HKSleepMetricsEngine
+ __OBJC_$_INSTANCE_VARIABLES_HKSleepMetrics
+ __OBJC_$_INSTANCE_VARIABLES_HKSleepMetricsEngine
+ __OBJC_$_PROP_LIST_HKSleepMetrics
+ __OBJC_CLASS_PROTOCOLS_$_HKSleepMetrics
+ __OBJC_CLASS_RO_$_HKSleepMetrics
+ __OBJC_CLASS_RO_$_HKSleepMetricsEngine
+ __OBJC_METACLASS_RO_$_HKSleepMetrics
+ __OBJC_METACLASS_RO_$_HKSleepMetricsEngine
+ ___33-[HKHealthStore dropEntitlement:]_block_invoke.632
+ ___34-[HKHealthStore _supportsFeature:]_block_invoke.533
+ ___34-[HKHealthStore _supportsFeature:]_block_invoke.533.cold.1
+ ___36-[HKHealthStore restoreEntitlement:]_block_invoke.633
+ ___47-[HKHealthStoreImplementation dropEntitlement:]_block_invoke.651
+ ___48-[HKHealthStoreImplementation _supportsFeature:]_block_invoke.550
+ ___48-[HKHealthStoreImplementation _supportsFeature:]_block_invoke.550.cold.1
+ ___50-[HKHealthStoreImplementation restoreEntitlement:]_block_invoke.652
+ ___50-[_HKFeatureFlags bloodPressureValidationsEnabled]_block_invoke
+ ___51-[HKHealthStore _deleteObjects:options:completion:]_block_invoke.507
+ ___51-[HKHealthStore _deleteObjects:options:completion:]_block_invoke_2.508
+ ___51-[_HKFeatureFlags sleepResultsNotificationsOnWatch]_block_invoke
+ ___56-[HKHealthStore setWorkoutSessionMirroringStartHandler:]_block_invoke.551
+ ___56-[HKHealthStore setWorkoutSessionMirroringStartHandler:]_block_invoke.551.cold.1
+ ___59-[HKHealthStore _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.593
+ ___59-[HKHealthStore _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.593.cold.1
+ ___67-[HKHealthStore splitTotalEnergy:startDate:endDate:resultsHandler:]_block_invoke.606
+ ___70-[HKHealthStore clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke.626
+ ___70-[HKHealthStore deleteObjectsOfType:predicate:options:withCompletion:]_block_invoke.512
+ ___70-[HKHealthStore deleteObjectsOfType:predicate:options:withCompletion:]_block_invoke_2.513
+ ___70-[HKHealthStoreImplementation setWorkoutSessionMirroringStartHandler:]_block_invoke.569
+ ___70-[HKHealthStoreImplementation setWorkoutSessionMirroringStartHandler:]_block_invoke.569.cold.1
+ ___72+[HKSleepMetricsEngine sleepMetricsForDaySummaries:inMorningIndexRange:]_block_invoke
+ ___73-[HKHealthStoreImplementation _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.611
+ ___73-[HKHealthStoreImplementation _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.611.cold.1
+ ___73-[HKSleepMetricsEngine fetchSleepMetricsForMorningIndexRange:completion:]_block_invoke
+ ___84-[HKHealthStore requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.425
+ ___84-[HKHealthStoreImplementation clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke.645
+ ___98-[HKHealthStoreImplementation requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.440
+ ___block_descriptor_56_e8_32r_e17_v32?0{?=qq}8^B24lr32l8
+ ___block_descriptor_64_e8_32s40bs_e56_v32?0"HKSleepDaySummaryQuery"8"NSArray"16"NSError"24ls40l8s32l8
+ ___block_literal_global.104
+ ___block_literal_global.107
+ ___block_literal_global.110
+ ___block_literal_global.116
+ ___block_literal_global.119
+ ___block_literal_global.131
+ ___block_literal_global.140
+ ___block_literal_global.166
+ ___block_literal_global.429
+ ___block_literal_global.444
+ ___block_literal_global.471
+ ___block_literal_global.479
+ ___block_literal_global.486
+ ___block_literal_global.490
+ ___block_literal_global.494
+ ___block_literal_global.535
+ ___block_literal_global.537
+ ___block_literal_global.539
+ ___block_literal_global.541
+ ___block_literal_global.550
+ ___block_literal_global.555
+ ___block_literal_global.557
+ ___block_literal_global.559
+ ___block_literal_global.568
+ ___block_literal_global.576
+ ___block_literal_global.582
+ ___block_literal_global.592
+ ___block_literal_global.594
+ ___block_literal_global.600
+ ___block_literal_global.610
+ ___block_literal_global.611
+ ___block_literal_global.615
+ ___block_literal_global.617
+ ___block_literal_global.619
+ ___block_literal_global.621
+ ___block_literal_global.623
+ ___block_literal_global.628
+ ___block_literal_global.630
+ ___block_literal_global.632
+ ___block_literal_global.634
+ ___block_literal_global.636
+ ___block_literal_global.638
+ ___block_literal_global.640
+ ___block_literal_global.642
+ ___block_literal_global.647
+ ___block_literal_global.74
+ ___block_literal_global.92
+ ___block_literal_global.95
+ _fmod
+ _objc_msgSend$_computeStandardDeviationFor:
+ _objc_msgSend$_dateComponentsForInterval:sinceDate:calendar:
+ _objc_msgSend$_firstAsleepSegment:
+ _objc_msgSend$_firstInBedSegment:
+ _objc_msgSend$_firstSegmentMatchingSleepValues:inPeriods:
+ _objc_msgSend$_generateConsiderationIntervalFromDaySummaries:morningIndexRange:
+ _objc_msgSend$_generateStrategyWithSleepDayInterval:considerationInterval:
+ _objc_msgSend$_lastAsleepSegment:
+ _objc_msgSend$_lastInBedSegment:
+ _objc_msgSend$_lastSegmentMatchingSleepValues:inPeriods:
+ _objc_msgSend$_lock_activeHours
+ _objc_msgSend$_lock_activeHoursGoal
+ _objc_msgSend$_lock_activeHoursGoalCount
+ _objc_msgSend$_lock_activeHoursGoalPercentage
+ _objc_msgSend$_lock_activityMoveMode
+ _objc_msgSend$_lock_briskMinutes
+ _objc_msgSend$_lock_briskMinutesGoal
+ _objc_msgSend$_lock_briskMinutesGoalInMinutes
+ _objc_msgSend$_lock_briskMinutesGoalPercentage
+ _objc_msgSend$_lock_cacheIndex
+ _objc_msgSend$_lock_dailyBriskMinutesStatistics
+ _objc_msgSend$_lock_dailyEnergyBurnedStatistics
+ _objc_msgSend$_lock_dailyMoveMinutesStatistics
+ _objc_msgSend$_lock_dateComponents
+ _objc_msgSend$_lock_endDate
+ _objc_msgSend$_lock_energyBurned
+ _objc_msgSend$_lock_energyBurnedGoal
+ _objc_msgSend$_lock_energyBurnedGoalDate
+ _objc_msgSend$_lock_energyBurnedGoalInKilocalories
+ _objc_msgSend$_lock_energyBurnedGoalPercentage
+ _objc_msgSend$_lock_energyBurnedInKilocalories
+ _objc_msgSend$_lock_fallbackActiveHoursGoal
+ _objc_msgSend$_lock_fallbackBriskMinutesGoal
+ _objc_msgSend$_lock_hasActiveHours
+ _objc_msgSend$_lock_hasActiveHoursGoal
+ _objc_msgSend$_lock_hasActiveHoursGoalDate
+ _objc_msgSend$_lock_hasBriskMinutes
+ _objc_msgSend$_lock_hasBriskMinutesGoal
+ _objc_msgSend$_lock_hasBriskMinutesGoalDate
+ _objc_msgSend$_lock_hasDailyBriskMinutesStatistics
+ _objc_msgSend$_lock_hasDailyEnergyBurnedStatistics
+ _objc_msgSend$_lock_hasDailyMoveMinutesStatistics
+ _objc_msgSend$_lock_hasDateComponents
+ _objc_msgSend$_lock_hasDeepBreathingDuration
+ _objc_msgSend$_lock_hasEnergyBurned
+ _objc_msgSend$_lock_hasEnergyBurnedGoal
+ _objc_msgSend$_lock_hasFlightsClimbed
+ _objc_msgSend$_lock_hasMoveMinutes
+ _objc_msgSend$_lock_hasMoveMinutesGoal
+ _objc_msgSend$_lock_hasPushCount
+ _objc_msgSend$_lock_hasStepCount
+ _objc_msgSend$_lock_hasWalkingAndRunningDistance
+ _objc_msgSend$_lock_hasWheelchairUse
+ _objc_msgSend$_lock_isEqualToActivityCache:
+ _objc_msgSend$_lock_isPaused
+ _objc_msgSend$_lock_knownFields
+ _objc_msgSend$_lock_metadata
+ _objc_msgSend$_lock_moveMinutes
+ _objc_msgSend$_lock_moveMinutesGoal
+ _objc_msgSend$_lock_moveMinutesGoalDate
+ _objc_msgSend$_lock_moveMinutesGoalInMinutes
+ _objc_msgSend$_lock_moveMinutesGoalPercentage
+ _objc_msgSend$_lock_sequence
+ _objc_msgSend$_lock_setActiveHours:
+ _objc_msgSend$_lock_setActiveHoursGoal:date:
+ _objc_msgSend$_lock_setActiveHoursGoalDateOnly:
+ _objc_msgSend$_lock_setActiveHoursGoalOnly:
+ _objc_msgSend$_lock_setActivityMoveMode:
+ _objc_msgSend$_lock_setBriskMinutes:
+ _objc_msgSend$_lock_setBriskMinutesGoal:date:
+ _objc_msgSend$_lock_setBriskMinutesGoalDateOnly:
+ _objc_msgSend$_lock_setBriskMinutesGoalOnly:
+ _objc_msgSend$_lock_setCacheIndex:
+ _objc_msgSend$_lock_setDailyBriskMinutesStatistics:
+ _objc_msgSend$_lock_setDailyEnergyBurnedStatistics:
+ _objc_msgSend$_lock_setDailyMoveMinutesStatistics:
+ _objc_msgSend$_lock_setDeepBreathingDuration:
+ _objc_msgSend$_lock_setEndDate:
+ _objc_msgSend$_lock_setEnergyBurned:
+ _objc_msgSend$_lock_setEnergyBurnedGoal:date:
+ _objc_msgSend$_lock_setEnergyBurnedGoalDateOnly:
+ _objc_msgSend$_lock_setEnergyBurnedGoalOnly:
+ _objc_msgSend$_lock_setFlightsClimbed:
+ _objc_msgSend$_lock_setMetadata:
+ _objc_msgSend$_lock_setMoveMinutes:
+ _objc_msgSend$_lock_setMoveMinutesGoal:date:
+ _objc_msgSend$_lock_setMoveMinutesGoalDateOnly:
+ _objc_msgSend$_lock_setMoveMinutesGoalOnly:
+ _objc_msgSend$_lock_setPaused:
+ _objc_msgSend$_lock_setPushCount:
+ _objc_msgSend$_lock_setSequence:
+ _objc_msgSend$_lock_setStartDate:
+ _objc_msgSend$_lock_setStepCount:
+ _objc_msgSend$_lock_setVersion:
+ _objc_msgSend$_lock_setWalkingAndRunningDistance:
+ _objc_msgSend$_lock_setWheelchairUse:
+ _objc_msgSend$_lock_startDate
+ _objc_msgSend$_lock_version
+ _objc_msgSend$_lock_walkingAndRunningDistance
+ _objc_msgSend$_lock_walkingAndRunningDistanceInMeters
+ _objc_msgSend$_lock_wheelchairUse
+ _objc_msgSend$_timeIntervalForDate:sinceDate:calendar:
+ _objc_msgSend$_typesWithBothBloodPressureIfNeeded:
+ _objc_msgSend$bloodPressureValidationsEnabled
+ _objc_msgSend$durationsForStrategy:
+ _objc_msgSend$enableBloodPressureValidations
+ _objc_msgSend$finishEncoding
+ _objc_msgSend$hasNonZeroSleepDurationGoal
+ _objc_msgSend$hk_enumerateDayIndexRangesWithOptions:usingBlock:
+ _objc_msgSend$hk_quantityWithSeconds:
+ _objc_msgSend$hk_sleepDayIntervalForMorningIndexRange:calendar:
+ _objc_msgSend$initWithDouble:
+ _objc_msgSend$initWithMorningIndexRange:ascending:limit:options:resultsHandler:
+ _objc_msgSend$primarySchedule
+ _objc_msgSend$setBloodPressureValidationsEnabled:
+ _objc_msgSend$sleepMetricsForDaySummaries:inMorningIndexRange:
+ _objc_msgSend$sleepMetricsWithMorningIndexRange:sleepAnalysisAsleepCount:sleepAnalysisInBedCount:sleepAnalysisCount:averageSleepDuration:averageInBedDuration:averageREMSleepDuration:averageCoreSleepDuration:averageDeepSleepDuration:averageUnspecifiedSleepDuration:averageAwakeDuration:bedtimeAchievedCount:sleepDurationGoalAchievedCount:sleepDurationGoalStreakCount:averageBedtimeMiss:averageSleepDurationGoalMiss:averageBedtime:averageWakeTime:averageInBedStartTime:averageInBedEndTime:averageSleepStartTime:averageSleepEndTime:standardDeviationActualTimeAsleep:standardDeviationScheduledTimeAsleep:standardDeviationActualVsScheduledTimeAsleep:averageSleepStartOffset:averageSleepEndOffset:averageInBedStartOffset:averageInBedEndOffset:
- -[HKActivityCache _fallbackActiveHoursGoal]
- -[HKActivityCache _fallbackBriskMinutesGoal]
- -[HKActivityCache _setActiveHoursGoal:date:].cold.1
- -[HKActivityCache _setActivityMoveMode:].cold.1
- -[HKActivityCache _setBriskMinutesGoal:date:].cold.1
- -[HKHealthStore _throwIfBothBloodPressureTypesNotRequestedForSharing:types:]
- -[HKHealthStore _throwIfBothBloodPressureTypesNotRequestedForSharing:types:].cold.1
- -[HKHealthStoreImplementation _throwIfBothBloodPressureTypesNotRequestedForSharing:types:]
- -[HKHealthStoreImplementation _throwIfBothBloodPressureTypesNotRequestedForSharing:types:].cold.1
- -[_HKFeatureFlags cycleTrackingGeminiOrchestration]
- -[_HKFeatureFlags maskRestingHeartRateSamplesWithSleepSamples]
- -[_HKFeatureFlags setCycleTrackingGeminiOrchestration:]
- -[_HKFeatureFlags setMaskRestingHeartRateSamplesWithSleepSamples:]
- GCC_except_table113
- GCC_except_table159
- GCC_except_table160
- GCC_except_table167
- GCC_except_table267
- GCC_except_table268
- GCC_except_table65
- _OBJC_IVAR_$__HKFeatureFlags._cycleTrackingGeminiOrchestration
- _OBJC_IVAR_$__HKFeatureFlags._maskRestingHeartRateSamplesWithSleepSamples
- ___33-[HKHealthStore dropEntitlement:]_block_invoke.635
- ___34-[HKHealthStore _supportsFeature:]_block_invoke.536
- ___34-[HKHealthStore _supportsFeature:]_block_invoke.536.cold.1
- ___36-[HKHealthStore restoreEntitlement:]_block_invoke.636
- ___47-[HKHealthStoreImplementation dropEntitlement:]_block_invoke.654
- ___48-[HKHealthStoreImplementation _supportsFeature:]_block_invoke.553
- ___48-[HKHealthStoreImplementation _supportsFeature:]_block_invoke.553.cold.1
- ___50-[HKHealthStoreImplementation restoreEntitlement:]_block_invoke.655
- ___51-[HKHealthStore _deleteObjects:options:completion:]_block_invoke.510
- ___51-[HKHealthStore _deleteObjects:options:completion:]_block_invoke_2.511
- ___51-[_HKFeatureFlags cycleTrackingGeminiOrchestration]_block_invoke
- ___56-[HKHealthStore setWorkoutSessionMirroringStartHandler:]_block_invoke.554
- ___56-[HKHealthStore setWorkoutSessionMirroringStartHandler:]_block_invoke.554.cold.1
- ___59-[HKHealthStore _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.596
- ___59-[HKHealthStore _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.596.cold.1
- ___62-[_HKFeatureFlags maskRestingHeartRateSamplesWithSleepSamples]_block_invoke
- ___67-[HKHealthStore splitTotalEnergy:startDate:endDate:resultsHandler:]_block_invoke.609
- ___70-[HKHealthStore clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke.629
- ___70-[HKHealthStore deleteObjectsOfType:predicate:options:withCompletion:]_block_invoke.515
- ___70-[HKHealthStore deleteObjectsOfType:predicate:options:withCompletion:]_block_invoke_2.516
- ___70-[HKHealthStoreImplementation setWorkoutSessionMirroringStartHandler:]_block_invoke.572
- ___70-[HKHealthStoreImplementation setWorkoutSessionMirroringStartHandler:]_block_invoke.572.cold.1
- ___73-[HKHealthStoreImplementation _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.614
- ___73-[HKHealthStoreImplementation _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.614.cold.1
- ___84-[HKHealthStore requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.424
- ___84-[HKHealthStoreImplementation clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke.648
- ___98-[HKHealthStoreImplementation requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.439
- ___block_literal_global.102
- ___block_literal_global.108
- ___block_literal_global.111
- ___block_literal_global.114
- ___block_literal_global.120
- ___block_literal_global.123
- ___block_literal_global.132
- ___block_literal_global.135
- ___block_literal_global.138
- ___block_literal_global.156
- ___block_literal_global.241
- ___block_literal_global.28
- ___block_literal_global.383
- ___block_literal_global.428
- ___block_literal_global.443
- ___block_literal_global.474
- ___block_literal_global.482
- ___block_literal_global.489
- ___block_literal_global.497
- ___block_literal_global.538
- ___block_literal_global.540
- ___block_literal_global.542
- ___block_literal_global.544
- ___block_literal_global.556
- ___block_literal_global.558
- ___block_literal_global.560
- ___block_literal_global.562
- ___block_literal_global.571
- ___block_literal_global.579
- ___block_literal_global.585
- ___block_literal_global.597
- ___block_literal_global.598
- ___block_literal_global.603
- ___block_literal_global.614
- ___block_literal_global.620
- ___block_literal_global.622
- ___block_literal_global.624
- ___block_literal_global.626
- ___block_literal_global.631
- ___block_literal_global.633
- ___block_literal_global.635
- ___block_literal_global.637
- ___block_literal_global.639
- ___block_literal_global.641
- ___block_literal_global.643
- ___block_literal_global.645
- ___block_literal_global.650
- ___block_literal_global.90
- ___block_literal_global.96
- ___block_literal_global.99
- _objc_msgSend$_activeHoursGoalCount
- _objc_msgSend$_briskMinutesGoalInMinutes
- _objc_msgSend$_energyBurnedGoalInKilocalories
- _objc_msgSend$_energyBurnedInKilocalories
- _objc_msgSend$_fallbackActiveHoursGoal
- _objc_msgSend$_fallbackBriskMinutesGoal
- _objc_msgSend$_moveMinutesGoalInMinutes
- _objc_msgSend$_setCacheIndex:
- _objc_msgSend$_setSequence:
- _objc_msgSend$_throwIfBothBloodPressureTypesNotRequestedForSharing:types:
- _objc_msgSend$_walkingAndRunningDistanceInMeters
- _objc_msgSend$hasActiveHours
- _objc_msgSend$hasActiveHoursGoal
- _objc_msgSend$hasActiveHoursGoalDate
- _objc_msgSend$hasBriskMinutes
- _objc_msgSend$hasBriskMinutesGoal
- _objc_msgSend$hasBriskMinutesGoalDate
- _objc_msgSend$hasDeepBreathingDuration
- _objc_msgSend$hasEnergyBurned
- _objc_msgSend$hasEnergyBurnedGoal
- _objc_msgSend$hasFlightsClimbed
- _objc_msgSend$hasMoveMinutes
- _objc_msgSend$hasMoveMinutesGoal
- _objc_msgSend$hasPushCount
- _objc_msgSend$hasStepCount
- _objc_msgSend$hasWalkingAndRunningDistance
- _objc_msgSend$hasWheelchairUse
- _objc_msgSend$sequence
CStrings:
+ "\n    Blood Pressure Validations: "
+ "%@: Blood pressure correlations must have 2 objects, one systolic BP and one diastolic BP. Received %ld objects."
+ "%@: Blood pressure correlations must have a systolic and diastolic quantity type. hasSystolic = %@, hasDiastolic = %@"
+ "7?"
+ "@\"HKSleepMetrics\""
+ "@256@0:8{?=qq}16q32q40q48@56@64@72@80@88@96@104q112q120q128@136@144@152@160@168@176@184@192@200@208@216@224@232@240@248"
+ "@40@0:8@16{?=qq}24"
+ "@40@0:8d16@24@32"
+ "App did not pass in both blood pressure types. containsSystolic = %{BOOL}d containsDiastolic = %{BOOL}d. Automatically adding missing one."
+ "Blood pressure correlations must have 2 objects, one systolic BP and one diastolic BP. Received %ld objects."
+ "Blood pressure correlations must have one systolic and one diastolic object."
+ "BloodPressureValidationsEnabled"
+ "HKSleepMetrics"
+ "HKSleepMetricsEngine"
+ "HealthKit Feature Support"
+ "Routes"
+ "SleepMetricsEngine"
+ "T@\"HKQuantity\",R,C,N,V_averageAwakeDuration"
+ "T@\"HKQuantity\",R,C,N,V_averageBedtimeMiss"
+ "T@\"HKQuantity\",R,C,N,V_averageCoreSleepDuration"
+ "T@\"HKQuantity\",R,C,N,V_averageDeepSleepDuration"
+ "T@\"HKQuantity\",R,C,N,V_averageInBedDuration"
+ "T@\"HKQuantity\",R,C,N,V_averageREMSleepDuration"
+ "T@\"HKQuantity\",R,C,N,V_averageSleepDuration"
+ "T@\"HKQuantity\",R,C,N,V_averageSleepDurationGoalMiss"
+ "T@\"HKQuantity\",R,C,N,V_averageUnspecifiedSleepDuration"
+ "T@\"HKSleepMetrics\",N,R,Vmetrics"
+ "T@\"NSDateComponents\",R,C,N,V_averageBedtime"
+ "T@\"NSDateComponents\",R,C,N,V_averageInBedEndTime"
+ "T@\"NSDateComponents\",R,C,N,V_averageInBedStartTime"
+ "T@\"NSDateComponents\",R,C,N,V_averageSleepEndTime"
+ "T@\"NSDateComponents\",R,C,N,V_averageSleepStartTime"
+ "T@\"NSDateComponents\",R,C,N,V_averageWakeTime"
+ "T@\"NSNumber\",R,C,N,V_averageInBedEndOffset"
+ "T@\"NSNumber\",R,C,N,V_averageInBedStartOffset"
+ "T@\"NSNumber\",R,C,N,V_averageSleepEndOffset"
+ "T@\"NSNumber\",R,C,N,V_averageSleepStartOffset"
+ "T@\"NSNumber\",R,C,N,V_standardDeviationActualTimeAsleep"
+ "T@\"NSNumber\",R,C,N,V_standardDeviationActualVsScheduledTimeAsleep"
+ "T@\"NSNumber\",R,C,N,V_standardDeviationScheduledTimeAsleep"
+ "Tq,R,N,V_bedtimeAchievedCount"
+ "Tq,R,N,V_sleepAnalysisAsleepCount"
+ "Tq,R,N,V_sleepAnalysisCount"
+ "Tq,R,N,V_sleepAnalysisInBedCount"
+ "Tq,R,N,V_sleepDurationGoalAchievedCount"
+ "Tq,R,N,V_sleepDurationGoalStreakCount"
+ "Tq,S_setSequence:"
+ "_averageAwakeDuration"
+ "_averageBedtime"
+ "_averageBedtimeMiss"
+ "_averageCoreSleepDuration"
+ "_averageDeepSleepDuration"
+ "_averageInBedDuration"
+ "_averageInBedEndOffset"
+ "_averageInBedEndTime"
+ "_averageInBedStartOffset"
+ "_averageInBedStartTime"
+ "_averageREMSleepDuration"
+ "_averageSleepDuration"
+ "_averageSleepDurationGoalMiss"
+ "_averageSleepEndOffset"
+ "_averageSleepEndTime"
+ "_averageSleepStartOffset"
+ "_averageSleepStartTime"
+ "_averageUnspecifiedSleepDuration"
+ "_averageWakeTime"
+ "_bedtimeAchievedCount"
+ "_bloodPressureValidationsEnabled"
+ "_computeStandardDeviationFor:"
+ "_dateComponentsForInterval:sinceDate:calendar:"
+ "_firstAsleepSegment:"
+ "_firstInBedSegment:"
+ "_firstSegmentMatchingSleepValues:inPeriods:"
+ "_generateConsiderationIntervalFromDaySummaries:morningIndexRange:"
+ "_generateStrategyWithSleepDayInterval:considerationInterval:"
+ "_lastAsleepSegment:"
+ "_lastInBedSegment:"
+ "_lastSegmentMatchingSleepValues:inPeriods:"
+ "_lock_activeHours"
+ "_lock_activeHoursGoal"
+ "_lock_activeHoursGoalCount"
+ "_lock_activeHoursGoalPercentage"
+ "_lock_activityMoveMode"
+ "_lock_briskMinutes"
+ "_lock_briskMinutesGoal"
+ "_lock_briskMinutesGoalInMinutes"
+ "_lock_briskMinutesGoalPercentage"
+ "_lock_cacheIndex"
+ "_lock_dailyBriskMinutesStatistics"
+ "_lock_dailyEnergyBurnedStatistics"
+ "_lock_dailyMoveMinutesStatistics"
+ "_lock_dateComponents"
+ "_lock_endDate"
+ "_lock_energyBurned"
+ "_lock_energyBurnedGoal"
+ "_lock_energyBurnedGoalDate"
+ "_lock_energyBurnedGoalInKilocalories"
+ "_lock_energyBurnedGoalPercentage"
+ "_lock_energyBurnedInKilocalories"
+ "_lock_fallbackActiveHoursGoal"
+ "_lock_fallbackBriskMinutesGoal"
+ "_lock_hasActiveHours"
+ "_lock_hasActiveHoursGoal"
+ "_lock_hasActiveHoursGoalDate"
+ "_lock_hasBriskMinutes"
+ "_lock_hasBriskMinutesGoal"
+ "_lock_hasBriskMinutesGoalDate"
+ "_lock_hasDailyBriskMinutesStatistics"
+ "_lock_hasDailyEnergyBurnedStatistics"
+ "_lock_hasDailyMoveMinutesStatistics"
+ "_lock_hasDateComponents"
+ "_lock_hasDeepBreathingDuration"
+ "_lock_hasEnergyBurned"
+ "_lock_hasEnergyBurnedGoal"
+ "_lock_hasFlightsClimbed"
+ "_lock_hasMoveMinutes"
+ "_lock_hasMoveMinutesGoal"
+ "_lock_hasPushCount"
+ "_lock_hasStepCount"
+ "_lock_hasWalkingAndRunningDistance"
+ "_lock_hasWheelchairUse"
+ "_lock_isEqualToActivityCache:"
+ "_lock_isPaused"
+ "_lock_knownFields"
+ "_lock_moveMinutes"
+ "_lock_moveMinutesGoal"
+ "_lock_moveMinutesGoalDate"
+ "_lock_moveMinutesGoalInMinutes"
+ "_lock_moveMinutesGoalPercentage"
+ "_lock_sequence"
+ "_lock_setActiveHours:"
+ "_lock_setActiveHoursGoal:date:"
+ "_lock_setActiveHoursGoalDateOnly:"
+ "_lock_setActiveHoursGoalOnly:"
+ "_lock_setActivityMoveMode:"
+ "_lock_setBriskMinutes:"
+ "_lock_setBriskMinutesGoal:date:"
+ "_lock_setBriskMinutesGoalDateOnly:"
+ "_lock_setBriskMinutesGoalOnly:"
+ "_lock_setCacheIndex:"
+ "_lock_setDailyBriskMinutesStatistics:"
+ "_lock_setDailyEnergyBurnedStatistics:"
+ "_lock_setDailyMoveMinutesStatistics:"
+ "_lock_setDeepBreathingDuration:"
+ "_lock_setEndDate:"
+ "_lock_setEnergyBurned:"
+ "_lock_setEnergyBurnedGoal:date:"
+ "_lock_setEnergyBurnedGoalDateOnly:"
+ "_lock_setEnergyBurnedGoalOnly:"
+ "_lock_setFlightsClimbed:"
+ "_lock_setMetadata:"
+ "_lock_setMoveMinutes:"
+ "_lock_setMoveMinutesGoal:date:"
+ "_lock_setMoveMinutesGoalDateOnly:"
+ "_lock_setMoveMinutesGoalOnly:"
+ "_lock_setPaused:"
+ "_lock_setPushCount:"
+ "_lock_setSequence:"
+ "_lock_setStartDate:"
+ "_lock_setStepCount:"
+ "_lock_setVersion:"
+ "_lock_setWalkingAndRunningDistance:"
+ "_lock_setWheelchairUse:"
+ "_lock_startDate"
+ "_lock_version"
+ "_lock_walkingAndRunningDistance"
+ "_lock_walkingAndRunningDistanceInMeters"
+ "_lock_wheelchairUse"
+ "_sleepAnalysisAsleepCount"
+ "_sleepAnalysisCount"
+ "_sleepAnalysisInBedCount"
+ "_sleepDurationGoalAchievedCount"
+ "_sleepDurationGoalStreakCount"
+ "_sleepResultsNotificationsOnWatch"
+ "_standardDeviationActualTimeAsleep"
+ "_standardDeviationActualVsScheduledTimeAsleep"
+ "_standardDeviationScheduledTimeAsleep"
+ "_timeIntervalForDate:sinceDate:calendar:"
+ "_typesWithBothBloodPressureIfNeeded:"
+ "averageAwakeDuration"
+ "averageBedtime"
+ "averageBedtimeMiss"
+ "averageCoreSleepDuration"
+ "averageDeepSleepDuration"
+ "averageInBedDuration"
+ "averageInBedEndOffset"
+ "averageInBedEndTime"
+ "averageInBedStartOffset"
+ "averageInBedStartTime"
+ "averageREMSleepDuration"
+ "averageSleepDuration"
+ "averageSleepDurationGoalMiss"
+ "averageSleepEndOffset"
+ "averageSleepEndTime"
+ "averageSleepStartOffset"
+ "averageSleepStartTime"
+ "averageUnspecifiedSleepDuration"
+ "averageWakeTime"
+ "bedtimeAchievedCount"
+ "bloodPressureValidationsEnabled"
+ "enableBloodPressureValidations"
+ "fetchSleepMetricsForMorningIndexRange:completion:"
+ "finishEncoding"
+ "initWithDouble:"
+ "metrics"
+ "morningIndexRangeDuration"
+ "morningIndexRangeStart"
+ "setBloodPressureValidationsEnabled:"
+ "setEnableBloodPressureValidations:"
+ "setSleepResultsNotificationsOnWatch:"
+ "sleepAnalysisAsleepCount"
+ "sleepAnalysisCount"
+ "sleepAnalysisInBedCount"
+ "sleepDurationGoalAchievedCount"
+ "sleepDurationGoalStreakCount"
+ "sleepMetricsForDaySummaries:"
+ "sleepMetricsForDaySummaries:inMorningIndexRange:"
+ "sleepMetricsWithMorningIndexRange:sleepAnalysisAsleepCount:sleepAnalysisInBedCount:sleepAnalysisCount:averageSleepDuration:averageInBedDuration:averageREMSleepDuration:averageCoreSleepDuration:averageDeepSleepDuration:averageUnspecifiedSleepDuration:averageAwakeDuration:bedtimeAchievedCount:sleepDurationGoalAchievedCount:sleepDurationGoalStreakCount:averageBedtimeMiss:averageSleepDurationGoalMiss:averageBedtime:averageWakeTime:averageInBedStartTime:averageInBedEndTime:averageSleepStartTime:averageSleepEndTime:standardDeviationActualTimeAsleep:standardDeviationScheduledTimeAsleep:standardDeviationActualVsScheduledTimeAsleep:averageSleepStartOffset:averageSleepEndOffset:averageInBedStartOffset:averageInBedEndOffset:"
+ "sleepResultsNotificationsOnWatch"
+ "standardDeviationActualTimeAsleep"
+ "standardDeviationActualVsScheduledTimeAsleep"
+ "standardDeviationScheduledTimeAsleep"
+ "v32@?0{?=qq}8^B24"
+ "v40@0:8{?=qq}16@?32"
- "Authorization to %s for blood pressure types does not include both diastolic and systolic types"
- "Authorization to %{public}s for blood pressure types does not include both diastolic and systolic types"
- "EnableChutneyLiveOn"
- "EnableHermitLiveOn"
- "Td,N,R"
- "Tq,S_setSequence:,V_sequence"
- "_cycleTrackingGeminiOrchestration"
- "_fallbackActiveHoursGoal"
- "_fallbackBriskMinutesGoal"
- "_maskRestingHeartRateSamplesWithSleepSamples"
- "_throwIfBothBloodPressureTypesNotRequestedForSharing:types:"
- "cycleTrackingGeminiOrchestration"
- "maskRestingHeartRateSamplesWithSleepSamples"
- "numberOfNonEmptySleepDaySummaries"
- "setCycleTrackingGeminiOrchestration:"
- "setMaskRestingHeartRateSamplesWithSleepSamples:"
- "totalAwakeDuration"
- "totalCoreSleepDuration"
- "totalDeepSleepDuration"
- "totalInBedDuration"
- "totalREMSleepDuration"
- "totalTimeAsleepDuration"

```
