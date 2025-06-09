## HealthMenstrualCycles

> `/System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0x2a5e4
+6074.1.2.4.0
+  __TEXT.__text: 0x2a5d8
   __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0x3314
-  __TEXT.__const: 0x240
+  __TEXT.__objc_methlist: 0x32d4
+  __TEXT.__const: 0x2b8
   __TEXT.__cstring: 0x3bd8
   __TEXT.__oslogstring: 0x2223
   __TEXT.__gcc_except_tab: 0x22c
   __TEXT.__ustring: 0x166
-  __TEXT.__unwind_info: 0xb30
-  __TEXT.__objc_classname: 0x7f9
-  __TEXT.__objc_methname: 0xb7fd
-  __TEXT.__objc_methtype: 0x14c3
-  __TEXT.__objc_stubs: 0x54a0
+  __TEXT.__unwind_info: 0xb48
+  __TEXT.__objc_classname: 0x7fc
+  __TEXT.__objc_methname: 0xb6d3
+  __TEXT.__objc_methtype: 0x14a3
+  __TEXT.__objc_stubs: 0x5480
   __DATA_CONST.__got: 0x518
   __DATA_CONST.__const: 0xe00
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f40
+  __DATA_CONST.__objc_selrefs: 0x1f18
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__auth_got: 0x2e0
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__cfstring: 0x31e0
-  __AUTH_CONST.__objc_const: 0x6018
+  __AUTH_CONST.__objc_const: 0x6030
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x3e0
-  __DATA.__data: 0xa90
-  __DATA.__common: 0x10
+  __DATA.__objc_ivar: 0x3e4
+  __DATA.__data: 0xa88
   __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x960
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/Sleep.framework/Sleep
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 10E4538F-F88C-3497-AFC3-B8D64810B4D3
-  Functions: 1171
-  Symbols:   4240
-  CStrings:  2669
+  UUID: 3196E60C-3606-3BF5-BB16-DD97768E9A13
+  Functions: 1167
+  Symbols:   4227
+  CStrings:  2663
 
Symbols:
+ +[HKMCDaySummary(TestSupport) daySummaryWithDayIndex:pregnancyTestResult:]
+ -[HKMCAnalysisProvider registerObserver:]
+ -[HKMCAnalysisProvider unregisterObserver:]
+ _HAMenstrualAlgorithmsPregnancyTestResultFromHKMCPregnancyTestResult
+ _OBJC_IVAR_$_HKMCAnalysisProvider._queue
+ __OBJC_$_PROP_LIST_HKMCViewModelProviderDataSource.376
+ ___103-[HKMCDaySummaryQuery client_deliverDaySummaries:clearPending:isFinalBatch:daySummaryAnchor:queryUUID:]_block_invoke.289
+ ___156-[HKMCOnboardingManager _saveUserEnteredCycleLength:userEnteredPeriodLength:userEnteredLastPeriodStartDay:addedCycleFactors:deletedCycleFactors:completion:]_block_invoke.383
+ ___156-[HKMCOnboardingManager _saveUserEnteredCycleLength:userEnteredPeriodLength:userEnteredLastPeriodStartDay:addedCycleFactors:deletedCycleFactors:completion:]_block_invoke.383.cold.1
+ ___156-[HKMCOnboardingManager _saveUserEnteredCycleLength:userEnteredPeriodLength:userEnteredLastPeriodStartDay:addedCycleFactors:deletedCycleFactors:completion:]_block_invoke.385
+ ___156-[HKMCOnboardingManager _saveUserEnteredCycleLength:userEnteredPeriodLength:userEnteredLastPeriodStartDay:addedCycleFactors:deletedCycleFactors:completion:]_block_invoke.385.cold.1
+ ___41-[HKMCAnalysisProvider registerObserver:]_block_invoke
+ ___41-[HKMCOnboardingManager resetOnboarding:]_block_invoke.395
+ ___42-[HKMCExperienceStore unregisterObserver:]_block_invoke.302
+ ___54-[HKMCCycleFactorsDataSource pregnancyModelDidUpdate:]_block_invoke.302
+ ___58-[HKMCExperienceStore registerObserver:completionHandler:]_block_invoke.298
+ ___67-[HKMCOnboardingManager setOnboardingCompletedWithInfo:completion:]_block_invoke.391
+ ___67-[HKMCOnboardingManager setOnboardingCompletedWithInfo:completion:]_block_invoke.391.cold.1
+ ___67-[HKMCOnboardingManager setOnboardingCompletedWithInfo:completion:]_block_invoke.392
+ ___67-[HKMCOnboardingManager setOnboardingCompletedWithInfo:completion:]_block_invoke.392.cold.1
+ ___block_literal_global.291
+ ___block_literal_global.334
+ ___block_literal_global.397
+ ___block_literal_global.399
+ _objc_msgSend$setPregnancyTestResult:
- -[HKMCAnalysisProvider addObserver:queue:]
- -[HKMCAnalysisProvider removeObserver:]
- -[HKMCNotification setCategory:]
- -[HKMCNotification setDueDateComponents:]
- -[HKMCPregnancyModeSetupCompletionRecord setConfigurationStepsReviewDate:]
- -[HKMCPregnancyModeSetupCompletionRecord setPostPregnancyFeatureAdjustmentCompletionLog:]
- -[HKMCPregnancyModeSetupCompletionRecord setPregnancyAdjustedFeaturesSet:]
- -[HKMCViewModelProvider initWithHealthStore:analysisProvider:pregnancyModelProvider:maximumActiveDuration:minimumBufferDuration:shouldFetchCycleFactors:calendarCache:queue:]
- __OBJC_$_PROP_LIST_HKMCViewModelProviderDataSource.373
- ___103-[HKMCDaySummaryQuery client_deliverDaySummaries:clearPending:isFinalBatch:daySummaryAnchor:queryUUID:]_block_invoke.286
- ___156-[HKMCOnboardingManager _saveUserEnteredCycleLength:userEnteredPeriodLength:userEnteredLastPeriodStartDay:addedCycleFactors:deletedCycleFactors:completion:]_block_invoke.380
- ___156-[HKMCOnboardingManager _saveUserEnteredCycleLength:userEnteredPeriodLength:userEnteredLastPeriodStartDay:addedCycleFactors:deletedCycleFactors:completion:]_block_invoke.380.cold.1
- ___156-[HKMCOnboardingManager _saveUserEnteredCycleLength:userEnteredPeriodLength:userEnteredLastPeriodStartDay:addedCycleFactors:deletedCycleFactors:completion:]_block_invoke.382
- ___156-[HKMCOnboardingManager _saveUserEnteredCycleLength:userEnteredPeriodLength:userEnteredLastPeriodStartDay:addedCycleFactors:deletedCycleFactors:completion:]_block_invoke.382.cold.1
- ___41-[HKMCOnboardingManager resetOnboarding:]_block_invoke.392
- ___42-[HKMCAnalysisProvider addObserver:queue:]_block_invoke
- ___42-[HKMCExperienceStore unregisterObserver:]_block_invoke.299
- ___54-[HKMCCycleFactorsDataSource pregnancyModelDidUpdate:]_block_invoke.299
- ___58-[HKMCExperienceStore registerObserver:completionHandler:]_block_invoke.295
- ___67-[HKMCOnboardingManager setOnboardingCompletedWithInfo:completion:]_block_invoke.385
- ___67-[HKMCOnboardingManager setOnboardingCompletedWithInfo:completion:]_block_invoke.388.cold.1
- ___67-[HKMCOnboardingManager setOnboardingCompletedWithInfo:completion:]_block_invoke.389
- ___67-[HKMCOnboardingManager setOnboardingCompletedWithInfo:completion:]_block_invoke.389.cold.1
- ___block_literal_global.288
- ___block_literal_global.331
- ___block_literal_global.394
- ___block_literal_global.396
- _objc_msgSend$addObserver:queue:
- _objc_msgSend$initWithHealthStore:analysisProvider:pregnancyModelProvider:maximumActiveDuration:minimumBufferDuration:shouldFetchCycleFactors:calendarCache:queue:
CStrings:
+ "T@\"NSDate\",R,N,V_configurationStepsReviewDate"
+ "T@\"NSDateComponents\",R,C,N,V_dueDateComponents"
+ "T@\"NSDictionary\",R,N,V_postPregnancyFeatureAdjustmentCompletionLog"
+ "T@\"NSSet\",R,N,V_pregnancyAdjustedFeaturesSet"
+ "T@\"NSString\",R,C,N,V_category"
+ "daySummaryWithDayIndex:pregnancyTestResult:"
- "@76@0:8@16@24@32q40q48B56@60@68"
- "T@\"NSDate\",&,N,V_configurationStepsReviewDate"
- "T@\"NSDateComponents\",C,N,V_dueDateComponents"
- "T@\"NSDictionary\",&,N,V_postPregnancyFeatureAdjustmentCompletionLog"
- "T@\"NSSet\",&,N,V_pregnancyAdjustedFeaturesSet"
- "T@\"NSString\",C,N,V_category"
- "featureAvailabilityProvidingDidUpdatePairedDeviceCapability:"
- "initWithHealthStore:analysisProvider:pregnancyModelProvider:maximumActiveDuration:minimumBufferDuration:shouldFetchCycleFactors:calendarCache:queue:"
- "setConfigurationStepsReviewDate:"
- "setDueDateComponents:"
- "setPostPregnancyFeatureAdjustmentCompletionLog:"
- "setPregnancyAdjustedFeaturesSet:"

```
