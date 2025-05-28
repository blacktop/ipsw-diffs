## SleepHealth

> `/System/Library/PrivateFrameworks/SleepHealth.framework/SleepHealth`

```diff

-4146.1.11.3.0
-  __TEXT.__text: 0x2dd4
-  __TEXT.__auth_stubs: 0x2f0
+4146.2.12.1.3
+  __TEXT.__text: 0x2f14
+  __TEXT.__auth_stubs: 0x300
   __TEXT.__objc_methlist: 0x2bc
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0xc4
+  __TEXT.__cstring: 0xca
   __TEXT.__gcc_except_tab: 0x8c
   __TEXT.__oslogstring: 0x148
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__unwind_info: 0xf4
   __TEXT.__objc_classname: 0xa1
   __TEXT.__objc_methname: 0x1598
   __TEXT.__objc_methtype: 0x2b9

   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__auth_got: 0x188
+  __AUTH_CONST.__auth_got: 0x190
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x78
   __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x74
   __DATA.__data: 0x188
-  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 66
-  Symbols:   365
+  Symbols:   366
   CStrings:  250
 
Symbols:
+ +[HKSHSleepMetrics sleepMetricsWithMorningIndexRange:sleepAnalysisAsleepCount:sleepAnalysisInBedCount:sleepAnalysisCount:averageSleepDuration:averageInBedDuration:averageREMSleepDuration:averageCoreSleepDuration:averageDeepSleepDuration:averageUnspecifiedSleepDuration:averageAwakeDuration:bedtimeAchievedCount:sleepDurationGoalAchievedCount:sleepDurationGoalStreakCount:averageBedtimeMiss:averageSleepDurationGoalMiss:averageBedtime:averageWakeTime:averageInBedStartTime:averageInBedEndTime:averageSleepStartTime:averageSleepEndTime:standardDeviationActualTimeAsleep:standardDeviationScheduledTimeAsleep:standardDeviationActualVsScheduledTimeAsleep:]
+ +[HKSHSleepMetricsEngine _computeStandardDeviationFor:]
+ +[HKSHSleepMetricsEngine _dateComponentsForInterval:sinceDate:calendar:]
+ +[HKSHSleepMetricsEngine _firstAsleepSegment:]
+ +[HKSHSleepMetricsEngine _firstInBedSegment:]
+ +[HKSHSleepMetricsEngine _firstSegmentMatchingSleepValues:inPeriods:]
+ +[HKSHSleepMetricsEngine _lastAsleepSegment:]
+ +[HKSHSleepMetricsEngine _lastInBedSegment:]
+ +[HKSHSleepMetricsEngine _lastSegmentMatchingSleepValues:inPeriods:]
+ +[HKSHSleepMetricsEngine _timeIntervalForDate:sinceDate:calendar:]
+ +[HKSHSleepMetricsEngine sleepMetricsForDaySummaries:]
+ +[HKSHSleepMetricsEngine sleepMetricsForDaySummaries:inMorningIndexRange:]
+ -[HKSHSleepMetrics .cxx_destruct]
+ -[HKSHSleepMetrics averageAwakeDuration]
+ -[HKSHSleepMetrics averageBedtimeMiss]
+ -[HKSHSleepMetrics averageBedtime]
+ -[HKSHSleepMetrics averageCoreSleepDuration]
+ -[HKSHSleepMetrics averageDeepSleepDuration]
+ -[HKSHSleepMetrics averageInBedDuration]
+ -[HKSHSleepMetrics averageInBedEndTime]
+ -[HKSHSleepMetrics averageInBedStartTime]
+ -[HKSHSleepMetrics averageREMSleepDuration]
+ -[HKSHSleepMetrics averageSleepDurationGoalMiss]
+ -[HKSHSleepMetrics averageSleepDuration]
+ -[HKSHSleepMetrics averageSleepEndTime]
+ -[HKSHSleepMetrics averageSleepStartTime]
+ -[HKSHSleepMetrics averageUnspecifiedSleepDuration]
+ -[HKSHSleepMetrics averageWakeTime]
+ -[HKSHSleepMetrics bedtimeAchievedCount]
+ -[HKSHSleepMetrics morningIndexRange]
+ -[HKSHSleepMetrics sleepAnalysisAsleepCount]
+ -[HKSHSleepMetrics sleepAnalysisCount]
+ -[HKSHSleepMetrics sleepAnalysisInBedCount]
+ -[HKSHSleepMetrics sleepDurationGoalAchievedCount]
+ -[HKSHSleepMetrics sleepDurationGoalStreakCount]
+ -[HKSHSleepMetrics standardDeviationActualTimeAsleep]
+ -[HKSHSleepMetrics standardDeviationActualVsScheduledTimeAsleep]
+ -[HKSHSleepMetrics standardDeviationScheduledTimeAsleep]
+ -[HKSHSleepMetricsEngine .cxx_destruct]
+ -[HKSHSleepMetricsEngine fetchSleepMetricsForMorningIndexRange:completion:]
+ -[HKSHSleepMetricsEngine initWithHealthStore:]
+ _OBJC_CLASS_$_HKSHSleepMetrics
+ _OBJC_CLASS_$_HKSHSleepMetricsEngine
+ _OBJC_IVAR_$_HKSHSleepMetrics._averageAwakeDuration
+ _OBJC_IVAR_$_HKSHSleepMetrics._averageBedtime
+ _OBJC_IVAR_$_HKSHSleepMetrics._averageBedtimeMiss
+ _OBJC_IVAR_$_HKSHSleepMetrics._averageCoreSleepDuration
+ _OBJC_IVAR_$_HKSHSleepMetrics._averageDeepSleepDuration
+ _OBJC_IVAR_$_HKSHSleepMetrics._averageInBedDuration
+ _OBJC_IVAR_$_HKSHSleepMetrics._averageInBedEndTime
+ _OBJC_IVAR_$_HKSHSleepMetrics._averageInBedStartTime
+ _OBJC_IVAR_$_HKSHSleepMetrics._averageREMSleepDuration
+ _OBJC_IVAR_$_HKSHSleepMetrics._averageSleepDuration
+ _OBJC_IVAR_$_HKSHSleepMetrics._averageSleepDurationGoalMiss
+ _OBJC_IVAR_$_HKSHSleepMetrics._averageSleepEndTime
+ _OBJC_IVAR_$_HKSHSleepMetrics._averageSleepStartTime
+ _OBJC_IVAR_$_HKSHSleepMetrics._averageUnspecifiedSleepDuration
+ _OBJC_IVAR_$_HKSHSleepMetrics._averageWakeTime
+ _OBJC_IVAR_$_HKSHSleepMetrics._bedtimeAchievedCount
+ _OBJC_IVAR_$_HKSHSleepMetrics._morningIndexRange
+ _OBJC_IVAR_$_HKSHSleepMetrics._sleepAnalysisAsleepCount
+ _OBJC_IVAR_$_HKSHSleepMetrics._sleepAnalysisCount
+ _OBJC_IVAR_$_HKSHSleepMetrics._sleepAnalysisInBedCount
+ _OBJC_IVAR_$_HKSHSleepMetrics._sleepDurationGoalAchievedCount
+ _OBJC_IVAR_$_HKSHSleepMetrics._sleepDurationGoalStreakCount
+ _OBJC_IVAR_$_HKSHSleepMetrics._standardDeviationActualTimeAsleep
+ _OBJC_IVAR_$_HKSHSleepMetrics._standardDeviationActualVsScheduledTimeAsleep
+ _OBJC_IVAR_$_HKSHSleepMetrics._standardDeviationScheduledTimeAsleep
+ _OBJC_IVAR_$_HKSHSleepMetricsEngine._healthStore
+ _OBJC_METACLASS_$_HKSHSleepMetrics
+ _OBJC_METACLASS_$_HKSHSleepMetricsEngine
+ __HKSHSafeAverageDurationRoundedToNearestMinute
+ __OBJC_$_CLASS_METHODS_HKSHSleepMetrics
+ __OBJC_$_CLASS_METHODS_HKSHSleepMetricsEngine
+ __OBJC_$_INSTANCE_METHODS_HKSHSleepMetrics
+ __OBJC_$_INSTANCE_METHODS_HKSHSleepMetricsEngine
+ __OBJC_$_INSTANCE_VARIABLES_HKSHSleepMetrics
+ __OBJC_$_INSTANCE_VARIABLES_HKSHSleepMetricsEngine
+ __OBJC_$_PROP_LIST_HKSHSleepMetrics
+ __OBJC_CLASS_RO_$_HKSHSleepMetrics
+ __OBJC_CLASS_RO_$_HKSHSleepMetricsEngine
+ __OBJC_METACLASS_RO_$_HKSHSleepMetrics
+ __OBJC_METACLASS_RO_$_HKSHSleepMetricsEngine
+ ___74+[HKSHSleepMetricsEngine sleepMetricsForDaySummaries:inMorningIndexRange:]_block_invoke
+ ___75-[HKSHSleepMetricsEngine fetchSleepMetricsForMorningIndexRange:completion:]_block_invoke
+ _fmod
+ _objc_msgSend$sleepMetricsForDaySummaries:inMorningIndexRange:
+ _objc_msgSend$sleepMetricsWithMorningIndexRange:sleepAnalysisAsleepCount:sleepAnalysisInBedCount:sleepAnalysisCount:averageSleepDuration:averageInBedDuration:averageREMSleepDuration:averageCoreSleepDuration:averageDeepSleepDuration:averageUnspecifiedSleepDuration:averageAwakeDuration:bedtimeAchievedCount:sleepDurationGoalAchievedCount:sleepDurationGoalStreakCount:averageBedtimeMiss:averageSleepDurationGoalMiss:averageBedtime:averageWakeTime:averageInBedStartTime:averageInBedEndTime:averageSleepStartTime:averageSleepEndTime:standardDeviationActualTimeAsleep:standardDeviationScheduledTimeAsleep:standardDeviationActualVsScheduledTimeAsleep:
- +[HKSHGoalProgress goalProgressWithMorningIndexRange:sleepAnalysisAsleepCount:sleepAnalysisInBedCount:sleepAnalysisCount:averageSleepDuration:averageInBedDuration:averageREMSleepDuration:averageCoreSleepDuration:averageDeepSleepDuration:averageUnspecifiedSleepDuration:averageAwakeDuration:bedtimeAchievedCount:sleepDurationGoalAchievedCount:sleepDurationGoalStreakCount:averageBedtimeMiss:averageSleepDurationGoalMiss:averageBedtime:averageWakeTime:averageInBedStartTime:averageInBedEndTime:averageSleepStartTime:averageSleepEndTime:standardDeviationActualTimeAsleep:standardDeviationScheduledTimeAsleep:standardDeviationActualVsScheduledTimeAsleep:]
- +[HKSHGoalProgressEngine _computeStandardDeviationFor:]
- +[HKSHGoalProgressEngine _dateComponentsForInterval:sinceDate:calendar:]
- +[HKSHGoalProgressEngine _firstAsleepSegment:]
- +[HKSHGoalProgressEngine _firstInBedSegment:]
- +[HKSHGoalProgressEngine _firstSegmentMatchingSleepValues:inPeriods:]
- +[HKSHGoalProgressEngine _lastAsleepSegment:]
- +[HKSHGoalProgressEngine _lastInBedSegment:]
- +[HKSHGoalProgressEngine _lastSegmentMatchingSleepValues:inPeriods:]
- +[HKSHGoalProgressEngine _timeIntervalForDate:sinceDate:calendar:]
- +[HKSHGoalProgressEngine goalProgressForDaySummaries:]
- +[HKSHGoalProgressEngine goalProgressForDaySummaries:inMorningIndexRange:]
- -[HKSHGoalProgress .cxx_destruct]
- -[HKSHGoalProgress averageAwakeDuration]
- -[HKSHGoalProgress averageBedtimeMiss]
- -[HKSHGoalProgress averageBedtime]
- -[HKSHGoalProgress averageCoreSleepDuration]
- -[HKSHGoalProgress averageDeepSleepDuration]
- -[HKSHGoalProgress averageInBedDuration]
- -[HKSHGoalProgress averageInBedEndTime]
- -[HKSHGoalProgress averageInBedStartTime]
- -[HKSHGoalProgress averageREMSleepDuration]
- -[HKSHGoalProgress averageSleepDurationGoalMiss]
- -[HKSHGoalProgress averageSleepDuration]
- -[HKSHGoalProgress averageSleepEndTime]
- -[HKSHGoalProgress averageSleepStartTime]
- -[HKSHGoalProgress averageUnspecifiedSleepDuration]
- -[HKSHGoalProgress averageWakeTime]
- -[HKSHGoalProgress bedtimeAchievedCount]
- -[HKSHGoalProgress morningIndexRange]
- -[HKSHGoalProgress sleepAnalysisAsleepCount]
- -[HKSHGoalProgress sleepAnalysisCount]
- -[HKSHGoalProgress sleepAnalysisInBedCount]
- -[HKSHGoalProgress sleepDurationGoalAchievedCount]
- -[HKSHGoalProgress sleepDurationGoalStreakCount]
- -[HKSHGoalProgress standardDeviationActualTimeAsleep]
- -[HKSHGoalProgress standardDeviationActualVsScheduledTimeAsleep]
- -[HKSHGoalProgress standardDeviationScheduledTimeAsleep]
- -[HKSHGoalProgressEngine .cxx_destruct]
- -[HKSHGoalProgressEngine fetchGoalProgressForMorningIndexRange:completion:]
- -[HKSHGoalProgressEngine initWithHealthStore:]
- _OBJC_CLASS_$_HKSHGoalProgress
- _OBJC_CLASS_$_HKSHGoalProgressEngine
- _OBJC_IVAR_$_HKSHGoalProgress._averageAwakeDuration
- _OBJC_IVAR_$_HKSHGoalProgress._averageBedtime
- _OBJC_IVAR_$_HKSHGoalProgress._averageBedtimeMiss
- _OBJC_IVAR_$_HKSHGoalProgress._averageCoreSleepDuration
- _OBJC_IVAR_$_HKSHGoalProgress._averageDeepSleepDuration
- _OBJC_IVAR_$_HKSHGoalProgress._averageInBedDuration
- _OBJC_IVAR_$_HKSHGoalProgress._averageInBedEndTime
- _OBJC_IVAR_$_HKSHGoalProgress._averageInBedStartTime
- _OBJC_IVAR_$_HKSHGoalProgress._averageREMSleepDuration
- _OBJC_IVAR_$_HKSHGoalProgress._averageSleepDuration
- _OBJC_IVAR_$_HKSHGoalProgress._averageSleepDurationGoalMiss
- _OBJC_IVAR_$_HKSHGoalProgress._averageSleepEndTime
- _OBJC_IVAR_$_HKSHGoalProgress._averageSleepStartTime
- _OBJC_IVAR_$_HKSHGoalProgress._averageUnspecifiedSleepDuration
- _OBJC_IVAR_$_HKSHGoalProgress._averageWakeTime
- _OBJC_IVAR_$_HKSHGoalProgress._bedtimeAchievedCount
- _OBJC_IVAR_$_HKSHGoalProgress._morningIndexRange
- _OBJC_IVAR_$_HKSHGoalProgress._sleepAnalysisAsleepCount
- _OBJC_IVAR_$_HKSHGoalProgress._sleepAnalysisCount
- _OBJC_IVAR_$_HKSHGoalProgress._sleepAnalysisInBedCount
- _OBJC_IVAR_$_HKSHGoalProgress._sleepDurationGoalAchievedCount
- _OBJC_IVAR_$_HKSHGoalProgress._sleepDurationGoalStreakCount
- _OBJC_IVAR_$_HKSHGoalProgress._standardDeviationActualTimeAsleep
- _OBJC_IVAR_$_HKSHGoalProgress._standardDeviationActualVsScheduledTimeAsleep
- _OBJC_IVAR_$_HKSHGoalProgress._standardDeviationScheduledTimeAsleep
- _OBJC_IVAR_$_HKSHGoalProgressEngine._healthStore
- _OBJC_METACLASS_$_HKSHGoalProgress
- _OBJC_METACLASS_$_HKSHGoalProgressEngine
- __HKAverageDurationQuantity
- __OBJC_$_CLASS_METHODS_HKSHGoalProgress
- __OBJC_$_CLASS_METHODS_HKSHGoalProgressEngine
- __OBJC_$_INSTANCE_METHODS_HKSHGoalProgress
- __OBJC_$_INSTANCE_METHODS_HKSHGoalProgressEngine
- __OBJC_$_INSTANCE_VARIABLES_HKSHGoalProgress
- __OBJC_$_INSTANCE_VARIABLES_HKSHGoalProgressEngine
- __OBJC_$_PROP_LIST_HKSHGoalProgress
- __OBJC_CLASS_RO_$_HKSHGoalProgress
- __OBJC_CLASS_RO_$_HKSHGoalProgressEngine
- __OBJC_METACLASS_RO_$_HKSHGoalProgress
- __OBJC_METACLASS_RO_$_HKSHGoalProgressEngine
- ___74+[HKSHGoalProgressEngine goalProgressForDaySummaries:inMorningIndexRange:]_block_invoke
- ___75-[HKSHGoalProgressEngine fetchGoalProgressForMorningIndexRange:completion:]_block_invoke
- _objc_msgSend$goalProgressForDaySummaries:inMorningIndexRange:
- _objc_msgSend$goalProgressWithMorningIndexRange:sleepAnalysisAsleepCount:sleepAnalysisInBedCount:sleepAnalysisCount:averageSleepDuration:averageInBedDuration:averageREMSleepDuration:averageCoreSleepDuration:averageDeepSleepDuration:averageUnspecifiedSleepDuration:averageAwakeDuration:bedtimeAchievedCount:sleepDurationGoalAchievedCount:sleepDurationGoalStreakCount:averageBedtimeMiss:averageSleepDurationGoalMiss:averageBedtime:averageWakeTime:averageInBedStartTime:averageInBedEndTime:averageSleepStartTime:averageSleepEndTime:standardDeviationActualTimeAsleep:standardDeviationScheduledTimeAsleep:standardDeviationActualVsScheduledTimeAsleep:
CStrings:
+ "HKSHSleepMetrics"
+ "HKSHSleepMetricsEngine"
+ "SleepMetricsEngine"
+ "fetchSleepMetricsForMorningIndexRange:completion:"
+ "sleepMetricsForDaySummaries:"
+ "sleepMetricsForDaySummaries:inMorningIndexRange:"
+ "sleepMetricsWithMorningIndexRange:sleepAnalysisAsleepCount:sleepAnalysisInBedCount:sleepAnalysisCount:averageSleepDuration:averageInBedDuration:averageREMSleepDuration:averageCoreSleepDuration:averageDeepSleepDuration:averageUnspecifiedSleepDuration:averageAwakeDuration:bedtimeAchievedCount:sleepDurationGoalAchievedCount:sleepDurationGoalStreakCount:averageBedtimeMiss:averageSleepDurationGoalMiss:averageBedtime:averageWakeTime:averageInBedStartTime:averageInBedEndTime:averageSleepStartTime:averageSleepEndTime:standardDeviationActualTimeAsleep:standardDeviationScheduledTimeAsleep:standardDeviationActualVsScheduledTimeAsleep:"
- "GoalProgress"
- "HKSHGoalProgress"
- "HKSHGoalProgressEngine"
- "fetchGoalProgressForMorningIndexRange:completion:"
- "goalProgressForDaySummaries:"
- "goalProgressForDaySummaries:inMorningIndexRange:"
- "goalProgressWithMorningIndexRange:sleepAnalysisAsleepCount:sleepAnalysisInBedCount:sleepAnalysisCount:averageSleepDuration:averageInBedDuration:averageREMSleepDuration:averageCoreSleepDuration:averageDeepSleepDuration:averageUnspecifiedSleepDuration:averageAwakeDuration:bedtimeAchievedCount:sleepDurationGoalAchievedCount:sleepDurationGoalStreakCount:averageBedtimeMiss:averageSleepDurationGoalMiss:averageBedtime:averageWakeTime:averageInBedStartTime:averageInBedEndTime:averageSleepStartTime:averageSleepEndTime:standardDeviationActualTimeAsleep:standardDeviationScheduledTimeAsleep:standardDeviationActualVsScheduledTimeAsleep:"

```
