## HealthMenstrualCyclesDaemon

> `/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon`

```diff

-7027.1.45.2.4
-  __TEXT.__text: 0x8eef0
-  __TEXT.__objc_methlist: 0x37ec
+7027.1.54.2.3
+  __TEXT.__text: 0x90924
+  __TEXT.__objc_methlist: 0x3b24
   __TEXT.__const: 0x1e30
-  __TEXT.__gcc_except_tab: 0xe28
-  __TEXT.__oslogstring: 0x6b5c
-  __TEXT.__cstring: 0x39c1
+  __TEXT.__gcc_except_tab: 0xfc0
+  __TEXT.__oslogstring: 0x6c2c
+  __TEXT.__cstring: 0x3a51
   __TEXT.__constg_swiftt: 0x81c
   __TEXT.__swift5_typeref: 0xd1a
   __TEXT.__swift5_reflstr: 0x871

   __TEXT.__swift5_proto: 0x134
   __TEXT.__swift5_types: 0x98
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x20c0
+  __TEXT.__unwind_info: 0x2128
   __TEXT.__eh_frame: 0xed8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x10a0
-  __DATA_CONST.__objc_classlist: 0x1a8
+  __DATA_CONST.__const: 0x1180
+  __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x280
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e58
+  __DATA_CONST.__objc_selrefs: 0x3080
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0xc8
-  __DATA_CONST.__got: 0xd48
-  __AUTH_CONST.__const: 0x12b8
-  __AUTH_CONST.__cfstring: 0x2460
-  __AUTH_CONST.__objc_const: 0x6a48
+  __DATA_CONST.__got: 0xd40
+  __AUTH_CONST.__const: 0x1318
+  __AUTH_CONST.__cfstring: 0x2480
+  __AUTH_CONST.__objc_const: 0x70a8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__auth_got: 0x11f8
-  __AUTH.__objc_data: 0x410
+  __AUTH_CONST.__auth_got: 0x1208
+  __AUTH.__objc_data: 0x460
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x4bc
-  __DATA.__data: 0x18f8
+  __DATA.__objc_ivar: 0x53c
+  __DATA.__data: 0x18e8
   __DATA.__objc_stublist: 0x8
   __DATA_DIRTY.__objc_data: 0x11c0
   __DATA_DIRTY.__data: 0xd20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/libsqlite3.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2424
-  Symbols:   3006
-  CStrings:  832
+  Functions: 2502
+  Symbols:   3132
+  CStrings:  838
 
Symbols:
+ +[HDMCAnalysisManager _test_isFingerprint:equalToFingerprint:]
+ +[HDSampleEntity(HKMenstrualCycles) _hdmc_sampleInfo:inTransaction:cacheKey:error:typesProvider:]
+ +[HDSampleEntity(HKMenstrualCycles) hdmc_analysisFingerprintSampleInfo:inTransaction:error:]
+ +[HDSampleEntity(HKMenstrualCycles) hdmc_heartStatisticsAnchorBeforeDate:inTransaction:error:]
+ -[HDMCAnalysisInputFingerprint .cxx_destruct]
+ -[HDMCAnalysisInputFingerprint algorithmVersion]
+ -[HDMCAnalysisInputFingerprint birthDateComponents]
+ -[HDMCAnalysisInputFingerprint deviationDetectionEnabledSetExplicitly]
+ -[HDMCAnalysisInputFingerprint deviationDetectionEnabledTypeMask]
+ -[HDMCAnalysisInputFingerprint deviationMinAnalysisWindowEndDay]
+ -[HDMCAnalysisInputFingerprint deviationsOnboardingRecordPresent]
+ -[HDMCAnalysisInputFingerprint deviationsUsageRequirementsSatisfied]
+ -[HDMCAnalysisInputFingerprint fertileWindowProjectionsEnabled]
+ -[HDMCAnalysisInputFingerprint hasDeviationInput]
+ -[HDMCAnalysisInputFingerprint hasDevicesWithHigherAlgorithmVersions]
+ -[HDMCAnalysisInputFingerprint heartStatisticsAnchor]
+ -[HDMCAnalysisInputFingerprint internalIgnoreCycleFactors]
+ -[HDMCAnalysisInputFingerprint internalIgnoreOvulationTestResults]
+ -[HDMCAnalysisInputFingerprint isEqualToFingerprint:]
+ -[HDMCAnalysisInputFingerprint lastCompletedSleepDay]
+ -[HDMCAnalysisInputFingerprint menopauseSupportedInCurrentRegion]
+ -[HDMCAnalysisInputFingerprint menstruationProjectionsEnabled]
+ -[HDMCAnalysisInputFingerprint sampleAnchorIsDeleted]
+ -[HDMCAnalysisInputFingerprint sampleAnchorUUID]
+ -[HDMCAnalysisInputFingerprint sampleAnchor]
+ -[HDMCAnalysisInputFingerprint setAlgorithmVersion:]
+ -[HDMCAnalysisInputFingerprint setBirthDateComponents:]
+ -[HDMCAnalysisInputFingerprint setDeviationDetectionEnabledSetExplicitly:]
+ -[HDMCAnalysisInputFingerprint setDeviationDetectionEnabledTypeMask:]
+ -[HDMCAnalysisInputFingerprint setDeviationMinAnalysisWindowEndDay:]
+ -[HDMCAnalysisInputFingerprint setDeviationsOnboardingRecordPresent:]
+ -[HDMCAnalysisInputFingerprint setDeviationsUsageRequirementsSatisfied:]
+ -[HDMCAnalysisInputFingerprint setFertileWindowProjectionsEnabled:]
+ -[HDMCAnalysisInputFingerprint setHasDeviationInput:]
+ -[HDMCAnalysisInputFingerprint setHasDevicesWithHigherAlgorithmVersions:]
+ -[HDMCAnalysisInputFingerprint setHeartStatisticsAnchor:]
+ -[HDMCAnalysisInputFingerprint setInternalIgnoreCycleFactors:]
+ -[HDMCAnalysisInputFingerprint setInternalIgnoreOvulationTestResults:]
+ -[HDMCAnalysisInputFingerprint setLastCompletedSleepDay:]
+ -[HDMCAnalysisInputFingerprint setMenopauseSupportedInCurrentRegion:]
+ -[HDMCAnalysisInputFingerprint setMenstruationProjectionsEnabled:]
+ -[HDMCAnalysisInputFingerprint setSampleAnchor:]
+ -[HDMCAnalysisInputFingerprint setSampleAnchorIsDeleted:]
+ -[HDMCAnalysisInputFingerprint setSampleAnchorUUID:]
+ -[HDMCAnalysisInputFingerprint setTimeZoneName:]
+ -[HDMCAnalysisInputFingerprint setTimeZoneSecondsFromGMT:]
+ -[HDMCAnalysisInputFingerprint setTodayIndex:]
+ -[HDMCAnalysisInputFingerprint setUseHeartRateInput:]
+ -[HDMCAnalysisInputFingerprint setUseWristTemperatureInput:]
+ -[HDMCAnalysisInputFingerprint setUserReportedCycleLength:]
+ -[HDMCAnalysisInputFingerprint setUserReportedCycleLengthDayIndex:]
+ -[HDMCAnalysisInputFingerprint setUserReportedMenstruationLength:]
+ -[HDMCAnalysisInputFingerprint setUserReportedMenstruationLengthDayIndex:]
+ -[HDMCAnalysisInputFingerprint timeZoneName]
+ -[HDMCAnalysisInputFingerprint timeZoneSecondsFromGMT]
+ -[HDMCAnalysisInputFingerprint todayIndex]
+ -[HDMCAnalysisInputFingerprint useHeartRateInput]
+ -[HDMCAnalysisInputFingerprint useWristTemperatureInput]
+ -[HDMCAnalysisInputFingerprint userReportedCycleLengthDayIndex]
+ -[HDMCAnalysisInputFingerprint userReportedCycleLength]
+ -[HDMCAnalysisInputFingerprint userReportedMenstruationLengthDayIndex]
+ -[HDMCAnalysisInputFingerprint userReportedMenstruationLength]
+ -[HDMCAnalysisManager _analysisWithAlgorithmsAnalysis:algorithmsCycles:recentSymptoms:mostRecentBasalBodyTemperature:lastLoggedDayIndex:lastMenstrualFlowDayIndex:currentDayIndex:numberOfDailySleepHeartRateStatisticsForPast100Days:numberOfDailyAwakeHeartRateStatisticsForPast100Days:featureSettings:useHeartRateInput:useWristTemperatureInput:deviationsFeatureSettings:addedCycleFactors:deletedCycleFactors:forPreview:replayingEarlierDay:hasDevicesWithHigherAlgorithmVersions:]
+ -[HDMCAnalysisManager _queue_analyzeNowWithForceIncludeCycles:forceAnalyzeCompleteHistory:mode:error:]
+ -[HDMCAnalysisManager _queue_markAnalysisInputsChanged]
+ -[HDMCAnalysisManager _queue_reusableAnalysisWithFingerprint:includeCycles:completeHistory:]
+ -[HDMCAnalysisManager _test_lastAnalysisInputFingerprint]
+ -[HDMCAnalysisManager _test_setAnalyzeOperationCurrentTimeProvider:]
+ -[HDMCAnalysisManager _test_waitForQueuedAnalysisWork]
+ GCC_except_table106
+ GCC_except_table110
+ GCC_except_table61
+ GCC_except_table8
+ GCC_except_table89
+ GCC_except_table94
+ GCC_except_table97
+ _HDMCDeviationDetectionEnabledTypeMask
+ _HDMCSampleTypeCodeList
+ _HDSQLiteColumnIsNull
+ _OBJC_CLASS_$_HDMCAnalysisInputFingerprint
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._algorithmVersion
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._birthDateComponents
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._deviationDetectionEnabledSetExplicitly
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._deviationDetectionEnabledTypeMask
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._deviationMinAnalysisWindowEndDay
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._deviationsOnboardingRecordPresent
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._deviationsUsageRequirementsSatisfied
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._fertileWindowProjectionsEnabled
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._hasDeviationInput
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._hasDevicesWithHigherAlgorithmVersions
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._heartStatisticsAnchor
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._internalIgnoreCycleFactors
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._internalIgnoreOvulationTestResults
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._lastCompletedSleepDay
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._menopauseSupportedInCurrentRegion
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._menstruationProjectionsEnabled
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._sampleAnchor
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._sampleAnchorIsDeleted
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._sampleAnchorUUID
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._timeZoneName
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._timeZoneSecondsFromGMT
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._todayIndex
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._useHeartRateInput
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._useWristTemperatureInput
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._userReportedCycleLength
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._userReportedCycleLengthDayIndex
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._userReportedMenstruationLength
+ _OBJC_IVAR_$_HDMCAnalysisInputFingerprint._userReportedMenstruationLengthDayIndex
+ _OBJC_IVAR_$_HDMCAnalysisManager._queue_analysisInputsChanged
+ _OBJC_IVAR_$_HDMCAnalysisManager._queue_lastAnalysisFingerprint
+ _OBJC_IVAR_$_HDMCAnalysisManager._queue_lastAnalysisIncludedCycles
+ _OBJC_IVAR_$_HDMCAnalysisManager._queue_lastAnalysisUsedCompleteHistory
+ _OBJC_METACLASS_$_HDMCAnalysisInputFingerprint
+ __OBJC_$_CLASS_METHODS_HDMCAnalysisManager
+ __OBJC_$_INSTANCE_METHODS_HDMCAnalysisInputFingerprint
+ __OBJC_$_INSTANCE_VARIABLES_HDMCAnalysisInputFingerprint
+ __OBJC_$_PROP_LIST_HDMCAnalysisInputFingerprint
+ __OBJC_CLASS_RO_$_HDMCAnalysisInputFingerprint
+ __OBJC_METACLASS_RO_$_HDMCAnalysisInputFingerprint
+ ___102-[HDMCAnalysisManager _queue_analyzeNowWithForceIncludeCycles:forceAnalyzeCompleteHistory:mode:error:]_block_invoke
+ ___475-[HDMCAnalysisManager _analysisWithAlgorithmsAnalysis:algorithmsCycles:recentSymptoms:mostRecentBasalBodyTemperature:lastLoggedDayIndex:lastMenstrualFlowDayIndex:currentDayIndex:numberOfDailySleepHeartRateStatisticsForPast100Days:numberOfDailyAwakeHeartRateStatisticsForPast100Days:featureSettings:useHeartRateInput:useWristTemperatureInput:deviationsFeatureSettings:addedCycleFactors:deletedCycleFactors:forPreview:replayingEarlierDay:hasDevicesWithHigherAlgorithmVersions:]_block_invoke
+ ___475-[HDMCAnalysisManager _analysisWithAlgorithmsAnalysis:algorithmsCycles:recentSymptoms:mostRecentBasalBodyTemperature:lastLoggedDayIndex:lastMenstrualFlowDayIndex:currentDayIndex:numberOfDailySleepHeartRateStatisticsForPast100Days:numberOfDailyAwakeHeartRateStatisticsForPast100Days:featureSettings:useHeartRateInput:useWristTemperatureInput:deviationsFeatureSettings:addedCycleFactors:deletedCycleFactors:forPreview:replayingEarlierDay:hasDevicesWithHigherAlgorithmVersions:]_block_invoke_2
+ ___54-[HDMCAnalysisManager _test_waitForQueuedAnalysisWork]_block_invoke
+ ___57-[HDMCAnalysisManager _test_lastAnalysisInputFingerprint]_block_invoke
+ ___92+[HDSampleEntity(HKMenstrualCycles) hdmc_analysisFingerprintSampleInfo:inTransaction:error:]_block_invoke
+ ___94+[HDSampleEntity(HKMenstrualCycles) hdmc_heartStatisticsAnchorBeforeDate:inTransaction:error:]_block_invoke
+ ___94+[HDSampleEntity(HKMenstrualCycles) hdmc_heartStatisticsAnchorBeforeDate:inTransaction:error:]_block_invoke_2
+ ___94+[HDSampleEntity(HKMenstrualCycles) hdmc_heartStatisticsAnchorBeforeDate:inTransaction:error:]_block_invoke_3
+ ___97+[HDSampleEntity(HKMenstrualCycles) _hdmc_sampleInfo:inTransaction:cacheKey:error:typesProvider:]_block_invoke
+ ___97+[HDSampleEntity(HKMenstrualCycles) _hdmc_sampleInfo:inTransaction:cacheKey:error:typesProvider:]_block_invoke_2
+ ___HDMCSampleTypeCodeList_block_invoke
+ ___block_descriptor_32_e14_"NSArray"8?0l
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e15_"NSString"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e23_v16?0^{sqlite3_stmt=}8ls32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_56_e8_32r40r_e35_B24?0"HDDatabaseTransaction"8^16lr32l8r40l8
+ ___block_descriptor_57_e8_32s40r48r_e35_B24?0"HDDatabaseTransaction"8^16lr40l8r48l8s32l8
+ ___block_descriptor_82_e8_32s40s48r_e9_B16?0^8lr48l8s32l8s40l8
+ _hdmc_analysisFingerprintSampleInfo:inTransaction:error:.lookupKey
+ _hdmc_analysisSampleInfo:forProfile:error:.lookupKey
+ _hdmc_heartStatisticsAnchorBeforeDate:inTransaction:error:.lookupKey
+ _sqlite3_bind_double
- -[HDMCAnalysisManager _analysisWithAlgorithmsAnalysis:algorithmsCycles:recentSymptoms:mostRecentBasalBodyTemperature:lastLoggedDayIndex:lastMenstrualFlowDayIndex:currentDayIndex:numberOfDailySleepHeartRateStatisticsForPast100Days:numberOfDailyAwakeHeartRateStatisticsForPast100Days:featureSettings:useHeartRateInput:useWristTemperatureInput:deviationsFeatureSettings:addedCycleFactors:deletedCycleFactors:forPreview:replayingEarlierDay:]
- -[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]
- GCC_except_table31
- GCC_except_table36
- GCC_except_table39
- GCC_except_table47
- GCC_except_table50
- _IDSBAASignerErrorDomain_block_invoke.lookupKey
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- ___437-[HDMCAnalysisManager _analysisWithAlgorithmsAnalysis:algorithmsCycles:recentSymptoms:mostRecentBasalBodyTemperature:lastLoggedDayIndex:lastMenstrualFlowDayIndex:currentDayIndex:numberOfDailySleepHeartRateStatisticsForPast100Days:numberOfDailyAwakeHeartRateStatisticsForPast100Days:featureSettings:useHeartRateInput:useWristTemperatureInput:deviationsFeatureSettings:addedCycleFactors:deletedCycleFactors:forPreview:replayingEarlierDay:]_block_invoke
- ___437-[HDMCAnalysisManager _analysisWithAlgorithmsAnalysis:algorithmsCycles:recentSymptoms:mostRecentBasalBodyTemperature:lastLoggedDayIndex:lastMenstrualFlowDayIndex:currentDayIndex:numberOfDailySleepHeartRateStatisticsForPast100Days:numberOfDailyAwakeHeartRateStatisticsForPast100Days:featureSettings:useHeartRateInput:useWristTemperatureInput:deviationsFeatureSettings:addedCycleFactors:deletedCycleFactors:forPreview:replayingEarlierDay:]_block_invoke_2
- ___78+[HDSampleEntity(HKMenstrualCycles) hdmc_analysisSampleInfo:forProfile:error:]_block_invoke_3
- ___78+[HDSampleEntity(HKMenstrualCycles) hdmc_analysisSampleInfo:forProfile:error:]_block_invoke_4
- ___97-[HDMCAnalysisManager _queue_analyzeNowWithForceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke
- ___block_descriptor_40_e8_32r_e35_B24?0"HDDatabaseTransaction"8^16lr32l8
- ___block_descriptor_58_e8_32s40s48r_e9_B16?0^8lr48l8s32l8s40l8
CStrings:
+ "@\"NSArray\"8@?0"
+ "SELECT MAX(data_id) FROM samples WHERE (data_type IN (%@)) AND (start_date < ? OR start_date IS NULL)"
+ "[%{public}@] Error reading analysis sample info, will not reuse: %{public}@"
+ "[%{public}@] Not reusing: no input fingerprint available"
+ "[%{public}@] Reusing last analysis: no analysis input changed (anchor %lld)"
+ "v16@?0^{sqlite3_stmt=}8"
```
