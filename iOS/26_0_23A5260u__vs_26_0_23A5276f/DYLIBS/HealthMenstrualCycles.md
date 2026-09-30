## HealthMenstrualCycles

> `/System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles`

```diff

-6074.1.2.4.0
-  __TEXT.__text: 0x2a5d8
+6087.1.2.1.0
+  __TEXT.__text: 0x2a5f8
   __TEXT.__auth_stubs: 0x5a0
   __TEXT.__objc_methlist: 0x32d4
   __TEXT.__const: 0x2b8
-  __TEXT.__cstring: 0x3bd8
+  __TEXT.__cstring: 0x3be9
   __TEXT.__oslogstring: 0x2223
   __TEXT.__gcc_except_tab: 0x22c
   __TEXT.__ustring: 0x166

   __TEXT.__objc_methtype: 0x14a3
   __TEXT.__objc_stubs: 0x5480
   __DATA_CONST.__got: 0x518
-  __DATA_CONST.__const: 0xe00
+  __DATA_CONST.__const: 0xe08
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0xe0

   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__auth_got: 0x2e0
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x31e0
+  __AUTH_CONST.__cfstring: 0x3200
   __AUTH_CONST.__objc_const: 0x6030
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /System/Library/PrivateFrameworks/Sleep.framework/Sleep
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3196E60C-3606-3BF5-BB16-DD97768E9A13
+  UUID: 8167E8A4-F5BC-36BD-9218-0456CA829169
   Functions: 1167
-  Symbols:   4227
-  CStrings:  2663
+  Symbols:   4228
+  CStrings:  2665
 
Symbols:
+ _HKMCMenstrualCyclesWidgetContainerBundleID
+ __OBJC_$_PROP_LIST_HKMCViewModelProviderDataSource.379
+ ___103-[HKMCDaySummaryQuery client_deliverDaySummaries:clearPending:isFinalBatch:daySummaryAnchor:queryUUID:]_block_invoke.292
+ ___156-[HKMCOnboardingManager _saveUserEnteredCycleLength:userEnteredPeriodLength:userEnteredLastPeriodStartDay:addedCycleFactors:deletedCycleFactors:completion:]_block_invoke.386
+ ___156-[HKMCOnboardingManager _saveUserEnteredCycleLength:userEnteredPeriodLength:userEnteredLastPeriodStartDay:addedCycleFactors:deletedCycleFactors:completion:]_block_invoke.386.cold.1
+ ___156-[HKMCOnboardingManager _saveUserEnteredCycleLength:userEnteredPeriodLength:userEnteredLastPeriodStartDay:addedCycleFactors:deletedCycleFactors:completion:]_block_invoke.388
+ ___156-[HKMCOnboardingManager _saveUserEnteredCycleLength:userEnteredPeriodLength:userEnteredLastPeriodStartDay:addedCycleFactors:deletedCycleFactors:completion:]_block_invoke.388.cold.1
+ ___41-[HKMCOnboardingManager resetOnboarding:]_block_invoke.398
+ ___42-[HKMCExperienceStore unregisterObserver:]_block_invoke.305
+ ___54-[HKMCCycleFactorsDataSource pregnancyModelDidUpdate:]_block_invoke.305
+ ___58-[HKMCExperienceStore registerObserver:completionHandler:]_block_invoke.301
+ ___67-[HKMCOnboardingManager setOnboardingCompletedWithInfo:completion:]_block_invoke.394
+ ___67-[HKMCOnboardingManager setOnboardingCompletedWithInfo:completion:]_block_invoke.394.cold.1
+ ___67-[HKMCOnboardingManager setOnboardingCompletedWithInfo:completion:]_block_invoke.395
+ ___67-[HKMCOnboardingManager setOnboardingCompletedWithInfo:completion:]_block_invoke.395.cold.1
+ ___block_literal_global.294
+ ___block_literal_global.337
+ ___block_literal_global.400
+ ___block_literal_global.402
- __OBJC_$_PROP_LIST_HKMCViewModelProviderDataSource.376
- ___103-[HKMCDaySummaryQuery client_deliverDaySummaries:clearPending:isFinalBatch:daySummaryAnchor:queryUUID:]_block_invoke.289
- ___156-[HKMCOnboardingManager _saveUserEnteredCycleLength:userEnteredPeriodLength:userEnteredLastPeriodStartDay:addedCycleFactors:deletedCycleFactors:completion:]_block_invoke.383
- ___156-[HKMCOnboardingManager _saveUserEnteredCycleLength:userEnteredPeriodLength:userEnteredLastPeriodStartDay:addedCycleFactors:deletedCycleFactors:completion:]_block_invoke.383.cold.1
- ___156-[HKMCOnboardingManager _saveUserEnteredCycleLength:userEnteredPeriodLength:userEnteredLastPeriodStartDay:addedCycleFactors:deletedCycleFactors:completion:]_block_invoke.385
- ___156-[HKMCOnboardingManager _saveUserEnteredCycleLength:userEnteredPeriodLength:userEnteredLastPeriodStartDay:addedCycleFactors:deletedCycleFactors:completion:]_block_invoke.385.cold.1
- ___41-[HKMCOnboardingManager resetOnboarding:]_block_invoke.395
- ___42-[HKMCExperienceStore unregisterObserver:]_block_invoke.302
- ___54-[HKMCCycleFactorsDataSource pregnancyModelDidUpdate:]_block_invoke.302
- ___58-[HKMCExperienceStore registerObserver:completionHandler:]_block_invoke.298
- ___67-[HKMCOnboardingManager setOnboardingCompletedWithInfo:completion:]_block_invoke.388
- ___67-[HKMCOnboardingManager setOnboardingCompletedWithInfo:completion:]_block_invoke.391.cold.1
- ___67-[HKMCOnboardingManager setOnboardingCompletedWithInfo:completion:]_block_invoke.392
- ___67-[HKMCOnboardingManager setOnboardingCompletedWithInfo:completion:]_block_invoke.392.cold.1
- ___block_literal_global.291
- ___block_literal_global.334
- ___block_literal_global.397
- ___block_literal_global.399
Functions:
~ -[HKMCPregnancyModeSetupCompletionRecord initWithCoder:] : 584 -> 588
~ -[HKMCPregnancyModeSetupCompletionRecord initWithVersion:sampleUUID:educationalStepsReviewDate:configurationStepsReviewDate:pregnancyAdjustedFeaturesSet:postPregnancyFeatureAdjustmentCompletionLog:] : 276 -> 292
~ -[HKMCPregnancyModeSetupCompletionRecord .cxx_destruct] : 104 -> 116
CStrings:
+ "com.apple.Health"

```
