## HealthMenstrualCyclesDaemon

> `/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon`

```diff

-6200.4.9.0.0
-  __TEXT.__text: 0x7c348
-  __TEXT.__auth_stubs: 0x1ff0
-  __TEXT.__objc_methlist: 0x33ec
-  __TEXT.__const: 0x1890
-  __TEXT.__cstring: 0x4065
-  __TEXT.__oslogstring: 0x6482
-  __TEXT.__gcc_except_tab: 0xe88
+6200.5.77.2.6
+  __TEXT.__text: 0x85d10
+  __TEXT.__auth_stubs: 0x1fc0
+  __TEXT.__objc_methlist: 0x33f4
+  __TEXT.__const: 0x17c0
+  __TEXT.__gcc_except_tab: 0xe60
+  __TEXT.__oslogstring: 0x64ec
+  __TEXT.__cstring: 0x3751
   __TEXT.__constg_swiftt: 0x630
   __TEXT.__swift5_typeref: 0xb68
-  __TEXT.__swift5_reflstr: 0x74d
+  __TEXT.__swift5_reflstr: 0x731
   __TEXT.__swift5_fieldmd: 0x54c
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x1d8

   __TEXT.__swift5_types: 0x68
   __TEXT.__swift5_capture: 0x204
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x1680
-  __TEXT.__eh_frame: 0xec8
-  __TEXT.__objc_classname: 0xbd5
-  __TEXT.__objc_methname: 0x11228
-  __TEXT.__objc_methtype: 0x20f9
-  __TEXT.__objc_stubs: 0x95e0
-  __DATA_CONST.__got: 0xc28
-  __DATA_CONST.__const: 0xf28
+  __TEXT.__unwind_info: 0x1918
+  __TEXT.__eh_frame: 0xdb0
+  __TEXT.__objc_classname: 0x1049
+  __TEXT.__objc_methname: 0x114a5
+  __TEXT.__objc_methtype: 0x2465
+  __TEXT.__objc_stubs: 0x9b20
+  __DATA_CONST.__got: 0xbf0
+  __DATA_CONST.__const: 0xf50
   __DATA_CONST.__objc_classlist: 0x180
-  __DATA_CONST.__objc_catlist: 0x90
+  __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c88
+  __DATA_CONST.__objc_selrefs: 0x2bd8
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x118
-  __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0x1010
+  __DATA_CONST.__objc_arraydata: 0xa0
+  __AUTH_CONST.__auth_got: 0xff8
   __AUTH_CONST.__const: 0xea8
-  __AUTH_CONST.__cfstring: 0x22a0
-  __AUTH_CONST.__objc_const: 0x62b8
-  __AUTH_CONST.__objc_intobj: 0x2b8
+  __AUTH_CONST.__cfstring: 0x2280
+  __AUTH_CONST.__objc_const: 0x6280
+  __AUTH_CONST.__objc_intobj: 0x1f8
+  __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x3c8
   __AUTH.__data: 0x40
   __DATA.__objc_ivar: 0x47c
-  __DATA.__data: 0x1610
+  __DATA.__data: 0x1638
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x10e0
+  __DATA.__bss: 0x1060
   __DATA.__common: 0xb8
   __DATA_DIRTY.__objc_data: 0x1080
-  __DATA_DIRTY.__data: 0x890
-  __DATA_DIRTY.__bss: 0xd80
+  __DATA_DIRTY.__data: 0x928
+  __DATA_DIRTY.__bss: 0xe00
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F5C17EDF-61AB-3DDF-B11D-F07871454233
-  Functions: 2134
-  Symbols:   5497
-  CStrings:  3318
+  UUID: D74EEC2A-9991-3E50-884C-54ED663AAB57
+  Functions: 2129
+  Symbols:   5609
+  CStrings:  3271
 
Symbols:
+ -[HDMCPluginServer _queue_deleteCycleFactorSamples:error:]
+ -[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:completion:]
+ GCC_except_table72
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ __OBJC_$_CATEGORY_HDAlarmEvent_$_HDMCNotificationSyncManager
+ __OBJC_$_CLASS_METHODS_HDMCDailyAnalytics(Analysis|Deviation|Onboarding)
+ __OBJC_$_CLASS_METHODS_HKCountrySet(MenstrualCyclesDeviationDetection|MenstrualCyclesHeartRateInput|MenstrualCyclesWristTemperatureInput)
+ __OBJC_$_INSTANCE_METHODS_HDAlarmEvent(HDMCNotificationSyncManager|HKMenstrualCycles)
+ __OBJC_$_PROP_LIST_HDAlarmEvent_$_HDMCNotificationSyncManager
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB9foe210106Em
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE16__init_with_sizeB9foe210106IPdS5_EEvT_T0_m
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB9foe210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ ___130-[HDMCAnalysisManager(CycleFactorsAutomaticUpgrade) initiateCycleFactorsAutomaticUpgradeWithDatabaseAccessibilityAssertion:error:]_block_invoke.350
+ ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.404
+ ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.407
+ ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.411
+ ___182-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:completion:]_block_invoke
+ ___182-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:completion:]_block_invoke.368
+ ___182-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:completion:]_block_invoke_2
+ ___182-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:completion:]_block_invoke_2.372
+ ___191-[HDMCDailyAnalytics _collectDiagnosticFieldsForMetric:settingsManager:heartRateInputFeatureStatus:deviationDetectionFeatureStatus:wristTemperatureInputFeatureStatus:gregorianCalendar:error:]_block_invoke.360
+ ___41-[HDMCPluginServer _triggerImmediateSync]_block_invoke.431
+ ___41-[HDMCPluginServer _triggerImmediateSync]_block_invoke.431.cold.1
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.372
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.372.cold.1
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.373
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.375
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.375.cold.1
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.376
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.376.cold.1
+ ___60-[HDMCNotificationManager _queue_alarm:didReceiveDueEvents:]_block_invoke.370
+ ___88-[HDMCPluginServer _queue_saveLastMenstrualPeriodWithDayIndexRange:calendarCache:error:]_block_invoke.407
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e53_B36?0"<HKSampleAggregateCacheProviding>"8B16q20^28ls32l8s64l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e35_B24?0"HDDatabaseTransaction"8^16ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.346
+ ___block_literal_global.349
+ ___block_literal_global.354
+ ___block_literal_global.358
+ ___block_literal_global.360
+ ___block_literal_global.362
+ ___block_literal_global.364
+ ___block_literal_global.366
+ ___block_literal_global.369
+ ___block_literal_global.395
+ ___block_literal_global.398
+ ___block_literal_global.402
+ ___block_literal_global.439
+ ___block_literal_global.445
+ ___block_literal_global.529
+ ___block_literal_global.532
+ ___block_literal_global.561
+ _block_copy_helper.13
+ _block_copy_helper.16
+ _block_copy_helper.23
+ _block_descriptor.15
+ _block_descriptor.18
+ _block_descriptor.25
+ _block_destroy_helper.14
+ _block_destroy_helper.17
+ _block_destroy_helper.24
+ _objc_msgSend$_bridging_analysisProviding
+ _objc_msgSend$_queue_deleteCycleFactorSamples:error:
+ _objc_msgSend$allObservers
+ _objc_msgSend$client_deliverPregnancyModel:queryUUID:
+ _objc_msgSend$client_experienceModelDidUpdate:
+ _objc_msgSend$configuration
+ _objc_msgSend$configurationStepsReviewDate
+ _objc_msgSend$connection
+ _objc_msgSend$data
+ _objc_msgSend$dataForKey:error:
+ _objc_msgSend$debugDescription
+ _objc_msgSend$educationalStepsReviewDate
+ _objc_msgSend$enumerateIncludingDeletedObjects:error:handler:
+ _objc_msgSend$epoch
+ _objc_msgSend$experienceModelManager
+ _objc_msgSend$experienceModelManagerDidUpdateModel
+ _objc_msgSend$featureAvailabilityExtensionForFeatureIdentifier:
+ _objc_msgSend$featureAvailabilityRequirement:didUpdateSatisfaction:
+ _objc_msgSend$hk_dateOnDayIndex:atHour:calendar:
+ _objc_msgSend$init
+ _objc_msgSend$initWithData:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithExtensionBundleIdentifier:kind:
+ _objc_msgSend$initWithFeatureAvailabilityProviding:healthDataSource:currentCountryCode:
+ _objc_msgSend$initWithInteger:
+ _objc_msgSend$initWithModel:
+ _objc_msgSend$initWithPregnancyModeSetupCompletionSet:
+ _objc_msgSend$initWithPregnancySample:state:
+ _objc_msgSend$initWithProfile:debugIdentifier:delegate:
+ _objc_msgSend$initWithState:pregnancyStartDate:pregnancyEndDate:estimatedDueDate:pregnancyDuration:physiologicalWashoutEndDate:behavioralWashoutEndDate:trimesters:sample:educationalStepsCompletedDate:
+ _objc_msgSend$initWithUUID:configuration:client:delegate:
+ _objc_msgSend$initWithVersion:sampleUUID:educationalStepsReviewDate:configurationStepsReviewDate:pregnancyAdjustedFeaturesSet:postPregnancyFeatureAdjustmentCompletionLog:
+ _objc_msgSend$invalidateRelevancesOfKind:inBundle:completion:
+ _objc_msgSend$isCurrentOnboardingVersionCompletedWithError:
+ _objc_msgSend$isNotInPostPregnancy
+ _objc_msgSend$isRunningForMaintenance
+ _objc_msgSend$isiPad
+ _objc_msgSend$kind
+ _objc_msgSend$latestTimeZoneCalendar
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$menstrualCyclesExperienceModelData
+ _objc_msgSend$noOngoingPregnancy
+ _objc_msgSend$physiologicalWashoutEndDate
+ _objc_msgSend$postNotification:
+ _objc_msgSend$postPregnancyFeatureAdjustmentCompletionLog
+ _objc_msgSend$pregnancyAdjustedFeaturesSet
+ _objc_msgSend$pregnancyManager
+ _objc_msgSend$pregnancyModeSetupCompletionSet
+ _objc_msgSend$pregnancyModelDidUpdate:
+ _objc_msgSend$profileIdentifier
+ _objc_msgSend$registerObserver:
+ _objc_msgSend$registerObserver:isUserInitiated:
+ _objc_msgSend$registerWithObserver:
+ _objc_msgSend$reloadTimelineWithReason:
+ _objc_msgSend$removeWithObserver:
+ _objc_msgSend$requestWorkWithPriority:error:
+ _objc_msgSend$sampleUUID
+ _objc_msgSend$schemaWithDomain:dataKeys:
+ _objc_msgSend$setData:forKey:error:
+ _objc_msgSend$setEncodingOption:forKey:
+ _objc_msgSend$setEpoch:
+ _objc_msgSend$setFailIfNotFound:
+ _objc_msgSend$setFeatureSettingNumber:forKey:completion:
+ _objc_msgSend$setMenstrualCyclesExperienceModelData:
+ _objc_msgSend$sharedWidgetService
+ _objc_msgSend$updateDataWithStateStore:delegate:profile:transaction:error:
+ _objectdestroy.14Tm
- +[HAMenstrualAlgorithmsAnalysis(UnitTesting) hdmc_demoAnalysisWithStartDayIndex:]
- -[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]
- GCC_except_table71
- _OBJC_CLASS_$_HAMenstrualAlgorithmsAnalysis
- _OBJC_CLASS_$_HAMenstrualAlgorithmsDeviation
- _OBJC_CLASS_$_HAMenstrualAlgorithmsDeviationAnalysis
- _OBJC_CLASS_$_HAMenstrualAlgorithmsPrediction
- _OBJC_CLASS_$_HAMenstrualAlgorithmsStats
- _OBJC_CLASS_$_NSConstantDictionary
- __OBJC_$_CATEGORY_CLASS_METHODS_HAMenstrualAlgorithmsAnalysis_$_UnitTesting
- __OBJC_$_CATEGORY_HAMenstrualAlgorithmsAnalysis_$_UnitTesting
- __OBJC_$_CATEGORY_HDAlarmEvent_$_HKMenstrualCycles
- __OBJC_$_CLASS_METHODS_HDMCDailyAnalytics(Onboarding|Deviation|Analysis)
- __OBJC_$_CLASS_METHODS_HKCountrySet(MenstrualCyclesDeviationDetection|MenstrualCyclesWristTemperatureInput|MenstrualCyclesHeartRateInput)
- __OBJC_$_INSTANCE_METHODS_HDAlarmEvent(HKMenstrualCycles|HDMCNotificationSyncManager)
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne200100Em
- __ZNSt3__16vectorIdNS_9allocatorIdEEE16__init_with_sizeB8ne200100IPdS5_EEvT_T0_m
- __ZNSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ne200100Ev
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
- ___130-[HDMCAnalysisManager(CycleFactorsAutomaticUpgrade) initiateCycleFactorsAutomaticUpgradeWithDatabaseAccessibilityAssertion:error:]_block_invoke.311
- ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.365
- ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.368
- ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.372
- ___162-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]_block_invoke
- ___162-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]_block_invoke.329
- ___162-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]_block_invoke_2
- ___162-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]_block_invoke_2.333
- ___191-[HDMCDailyAnalytics _collectDiagnosticFieldsForMetric:settingsManager:heartRateInputFeatureStatus:deviationDetectionFeatureStatus:wristTemperatureInputFeatureStatus:gregorianCalendar:error:]_block_invoke.321
- ___41-[HDMCPluginServer _triggerImmediateSync]_block_invoke.392
- ___41-[HDMCPluginServer _triggerImmediateSync]_block_invoke.392.cold.1
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.333
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.333.cold.1
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.334
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.336
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.336.cold.1
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.337
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.337.cold.1
- ___60-[HDMCNotificationManager _queue_alarm:didReceiveDueEvents:]_block_invoke.331
- ___88-[HDMCPluginServer _queue_saveLastMenstrualPeriodWithDayIndexRange:calendarCache:error:]_block_invoke.368
- ___block_descriptor_72_e8_32s40s48s56s64bs_e44_B36?0"HKMCDailyHeartStatistics"8B16q20^28ls32l8s64l8s40l8s48l8s56l8
- ___block_descriptor_88_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.307
- ___block_literal_global.310
- ___block_literal_global.315
- ___block_literal_global.317
- ___block_literal_global.319
- ___block_literal_global.321
- ___block_literal_global.323
- ___block_literal_global.325
- ___block_literal_global.327
- ___block_literal_global.330
- ___block_literal_global.359
- ___block_literal_global.361
- ___block_literal_global.363
- ___block_literal_global.406
- ___block_literal_global.490
- ___block_literal_global.493
- ___block_literal_global.522
- _block_copy_helper.18
- _block_copy_helper.26
- _block_descriptor.20
- _block_descriptor.28
- _block_destroy_helper.19
- _block_destroy_helper.27
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$setDeviationAnalysis:
- _objc_msgSend$setEndProbabilityMean:
- _objc_msgSend$setEndProbabilityStdDev:
- _objc_msgSend$setFertilityPredictions:
- _objc_msgSend$setIrregularBleeding:
- _objc_msgSend$setJulianDayOfAnalysisWindowEnd:
- _objc_msgSend$setJulianDayOfAnalysisWindowStart:
- _objc_msgSend$setJulianDayOfFirstCycleStart:
- _objc_msgSend$setJulianDayOfLastCycleStart:
- _objc_msgSend$setJulianDayOfWindowStart:
- _objc_msgSend$setLowRange:
- _objc_msgSend$setLowerCycleLengthPercentile:
- _objc_msgSend$setLowerMenstruationLengthPercentile:
- _objc_msgSend$setMedianCycleLength:
- _objc_msgSend$setMedianMenstruationLength:
- _objc_msgSend$setMenstruationPredictions:
- _objc_msgSend$setMetricsForCoreAnalytics:
- _objc_msgSend$setNumberOfCyclesFound:
- _objc_msgSend$setProlongedBleeding:
- _objc_msgSend$setStartProbabilityMean:
- _objc_msgSend$setStartProbabilityStdDev:
- _objc_msgSend$setStats:
- _objc_msgSend$setUpperCycleLengthPercentile:
- _objc_msgSend$setUpperMenstruationLengthPercentile:
- _objc_release_x1
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objectdestroy.17Tm
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CIsgugCVryBf389iM77mqQYic07pCKE7zT5enFU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "02979F49-332F-481C-B7DE-7E80973B07BF"
+ "B36@?0@\"<HKSampleAggregateCacheProviding>\"8B16q20^@28"
+ "CBC78224-332F-481C-B7DE-7E80973B07BF"
+ "HDMCExperienceStoreServer"
+ "HealthMenstrualCyclesDaemon"
+ "[%{public}@] Delete %@ deleted cycle factors: %@"
+ "[%{public}@] Deleted %@ samples: %@"
+ "_queue_deleteCycleFactorSamples:error:"
+ "remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:deletedCycleFactors:initialAnalysisWindow:completion:"
+ "samplesMapWereRemoved:anchor:"
+ "setFailIfNotFound:"
+ "v32@0:8@\"NSDictionary\"16@\"NSNumber\"24"
+ "v72@0:8@\"NSDictionary\"16@\"NSDictionary\"24@\"NSArray\"32@\"NSArray\"40{?=qq}48@?<v@?@\"NSArray\"@\"NSError\">64"
+ "v72@0:8@16@24@32@40{?=qq}48@?64"
- "02979F49-FAFA-49CC-8478-C2562BC81FB6"
- "B36@?0@\"HKMCDailyHeartStatistics\"8B16q20^@28"
- "CBC78224-8F5E-4D43-8666-69ADBE2A6277"
- "UnitTesting"
- "hdmc_demoAnalysisWithStartDayIndex:"
- "remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:"
- "setDeviationAnalysis:"
- "setEndProbabilityMean:"
- "setEndProbabilityStdDev:"
- "setFertilityPredictions:"
- "setIrregularBleeding:"
- "setJulianDayOfAnalysisWindowEnd:"
- "setJulianDayOfAnalysisWindowStart:"
- "setJulianDayOfFirstCycleStart:"
- "setJulianDayOfLastCycleStart:"
- "setJulianDayOfWindowStart:"
- "setLowRange:"
- "setLowerCycleLengthPercentile:"
- "setLowerMenstruationLengthPercentile:"
- "setMedianCycleLength:"
- "setMedianMenstruationLength:"
- "setMenstruationPredictions:"
- "setMetricsForCoreAnalytics:"
- "setNumberOfCyclesFound:"
- "setProlongedBleeding:"
- "setStartProbabilityMean:"
- "setStartProbabilityStdDev:"
- "setStats:"
- "setUpperCycleLengthPercentile:"
- "setUpperMenstruationLengthPercentile:"
- "v64@0:8@\"NSDictionary\"16@\"NSDictionary\"24@\"NSArray\"32{?=qq}40@?<v@?@\"NSArray\"@\"NSError\">56"
- "v64@0:8@16@24@32{?=qq}40@?56"

```
