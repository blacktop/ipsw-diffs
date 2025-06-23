## AppPredictionInternal

> `/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal`

```diff

-610.0.11.0.0
-  __TEXT.__text: 0x47ece0
+613.0.1.0.0
+  __TEXT.__text: 0x4803b4
   __TEXT.__auth_stubs: 0x3de0
-  __TEXT.__objc_methlist: 0x38c24
+  __TEXT.__objc_methlist: 0x38d84
   __TEXT.__const: 0x3b6a
-  __TEXT.__cstring: 0x59b71
-  __TEXT.__oslogstring: 0x3a969
-  __TEXT.__gcc_except_tab: 0xfb88
+  __TEXT.__cstring: 0x5a131
+  __TEXT.__oslogstring: 0x3aa19
+  __TEXT.__gcc_except_tab: 0xfcf8
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__ustring: 0x90
   __TEXT.__swift5_typeref: 0x12aa

   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xe338
+  __TEXT.__unwind_info: 0xe350
   __TEXT.__eh_frame: 0x26fc
-  __TEXT.__objc_classname: 0x8c8c
-  __TEXT.__objc_methname: 0xad943
-  __TEXT.__objc_methtype: 0x1804e
-  __TEXT.__objc_stubs: 0x4cba0
-  __DATA_CONST.__got: 0x3940
-  __DATA_CONST.__const: 0xbdb0
+  __TEXT.__objc_classname: 0x8c8d
+  __TEXT.__objc_methname: 0xae291
+  __TEXT.__objc_methtype: 0x1806b
+  __TEXT.__objc_stubs: 0x4cf40
+  __DATA_CONST.__got: 0x3948
+  __DATA_CONST.__const: 0xbe48
   __DATA_CONST.__objc_classlist: 0x1fa0
   __DATA_CONST.__objc_catlist: 0x140
   __DATA_CONST.__objc_protolist: 0x4d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bd10
+  __DATA_CONST.__objc_selrefs: 0x1be00
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x1530
   __DATA_CONST.__objc_arraydata: 0x1398
   __AUTH_CONST.__auth_got: 0x1f08
-  __AUTH_CONST.__const: 0x8528
-  __AUTH_CONST.__cfstring: 0x3a380
-  __AUTH_CONST.__objc_const: 0x83a30
+  __AUTH_CONST.__const: 0x8548
+  __AUTH_CONST.__cfstring: 0x3a860
+  __AUTH_CONST.__objc_const: 0x83cd8
   __AUTH_CONST.__objc_intobj: 0x3438
   __AUTH_CONST.__objc_arrayobj: 0x1098
   __AUTH_CONST.__objc_dictobj: 0x1b8

   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH.__objc_data: 0x5350
   __AUTH.__data: 0x2160
-  __DATA.__objc_ivar: 0x4ab4
+  __DATA.__objc_ivar: 0x4aec
   __DATA.__data: 0x3d08
   __DATA.__bss: 0x27e8
   __DATA.__common: 0x108

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
-  - /System/Library/PrivateFrameworks/Spotlight.framework/Spotlight
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/ToolKit.framework/ToolKit
   - /System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/UIIntelligenceSupport

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E84086E1-E274-3C3D-B0F2-E5C5E8957753
-  Functions: 25424
-  Symbols:   76726
-  CStrings:  42740
+  UUID: A08CF582-C81D-35D9-BD65-4D53BAB18869
+  Functions: 25463
+  Symbols:   76840
+  CStrings:  42882
 
Symbols:
+ +[ATXAppPredictionDataHarvester harvestDataFromActionPredictionItem:isMenuItem:itemIndex:itemOutcome:sessionOutcome:sessionUUID:numItemsInSession:]
+ -[ATXPredictionDataHistograms documentAirplaneModeHistogram]
+ -[ATXPredictionDataHistograms documentAmbientLightHistogram]
+ -[ATXPredictionDataHistograms documentCategoryDayOfWeekHistogram]
+ -[ATXPredictionDataHistograms documentCategoryOpenHistogram]
+ -[ATXPredictionDataHistograms documentCategoryPartOfWeekHistogram]
+ -[ATXPredictionDataHistograms documentCategoryTrendingOpenHistogram]
+ -[ATXPredictionDataHistograms documentConfirmsHistogram]
+ -[ATXPredictionDataHistograms documentCoreMotionOpenHistogram]
+ -[ATXPredictionDataHistograms documentDayOfWeekHistogram]
+ -[ATXPredictionDataHistograms documentOpenHistogram]
+ -[ATXPredictionDataHistograms documentPartOfWeekHistogram]
+ -[ATXPredictionDataHistograms documentTrendingOpenHistogram]
+ -[ATXPredictionDataHistograms documentUnlockTimeHistogram]
+ -[ATXPredictionDataHistograms documentWifiOpenHistogram]
+ -[ATXServer fetchLastExecutedActionsWithCompletion:]
+ -[_ATXAppLaunchCategoricalHistogram initWithType:maxCategoryCount:pruningMethod:].cold.37
+ -[_ATXAppLaunchCategoricalHistogram initWithType:maxCategoryCount:pruningMethod:].cold.38
+ -[_ATXAppLaunchCategoricalHistogram initWithType:maxCategoryCount:pruningMethod:].cold.39
+ -[_ATXAppLaunchHistogram initWithType:].cold.83
+ -[_ATXGlobals documentAirplaneModeDecayHalflife]
+ -[_ATXGlobals documentAmbientLightDecayHalflife]
+ -[_ATXGlobals documentCategoryDayOfWeekDecayHalflife]
+ -[_ATXGlobals documentCategoryOpenDecayHalflife]
+ -[_ATXGlobals documentCategoryPartOfWeekDecayHalflife]
+ -[_ATXGlobals documentCategoryTrendingOpenDecayHalflife]
+ -[_ATXGlobals documentConfirmsDecayHalflife]
+ -[_ATXGlobals documentCoreMotionOpenDecayHalflife]
+ -[_ATXGlobals documentDayOfWeekDecayHalflife]
+ -[_ATXGlobals documentOpenDecayHalflife]
+ -[_ATXGlobals documentPartOfWeekDecayHalflife]
+ -[_ATXGlobals documentTrendingOpenDecayHalflife]
+ -[_ATXGlobals documentUnlockTimeDecayHalflife]
+ -[_ATXGlobals documentWifiOpenDecayHalflife]
+ _ATXMenuItemIntentType
+ _OBJC_IVAR_$_ATXPredictionDataHistograms._documentAirplaneModeHistogram
+ _OBJC_IVAR_$_ATXPredictionDataHistograms._documentAmbientLightHistogram
+ _OBJC_IVAR_$_ATXPredictionDataHistograms._documentCategoryDayOfWeekHistogram
+ _OBJC_IVAR_$_ATXPredictionDataHistograms._documentCategoryOpenHistogram
+ _OBJC_IVAR_$_ATXPredictionDataHistograms._documentCategoryPartOfWeekHistogram
+ _OBJC_IVAR_$_ATXPredictionDataHistograms._documentCategoryTrendingOpenHistogram
+ _OBJC_IVAR_$_ATXPredictionDataHistograms._documentConfirmsHistogram
+ _OBJC_IVAR_$_ATXPredictionDataHistograms._documentCoreMotionOpenHistogram
+ _OBJC_IVAR_$_ATXPredictionDataHistograms._documentDayOfWeekHistogram
+ _OBJC_IVAR_$_ATXPredictionDataHistograms._documentOpenHistogram
+ _OBJC_IVAR_$_ATXPredictionDataHistograms._documentPartOfWeekHistogram
+ _OBJC_IVAR_$_ATXPredictionDataHistograms._documentTrendingOpenHistogram
+ _OBJC_IVAR_$_ATXPredictionDataHistograms._documentUnlockTimeHistogram
+ _OBJC_IVAR_$_ATXPredictionDataHistograms._documentWifiOpenHistogram
+ ___200-[_ATXAppPredictor predictWithLimit:consumerSubType:intent:candidateBundleIdentifiers:candidateActiontypes:scoreLogger:predictionItemsToKeep:predictedItemsOutParameter:context:datastore:featureCache:]_block_invoke.185
+ ___52-[ATXServer fetchLastExecutedActionsWithCompletion:]_block_invoke
+ ___52-[ATXServer fetchLastExecutedActionsWithCompletion:]_block_invoke_2
+ ___58-[ATXFaceGalleryLayoutGenerator rankedFeaturedDescriptors]_block_invoke.64
+ ___64-[ATXUpdatePredictionsManager processAppDirectoryFeedbackNoSync]_block_invoke.81
+ ___ATX_HISTOGRAM_FOR_TYPE___ATXHistogramTypeDocumentCategoryDayOfWeek
+ ___ATX_HISTOGRAM_FOR_TYPE___ATXHistogramTypeDocumentCategoryOpen
+ ___ATX_HISTOGRAM_FOR_TYPE___ATXHistogramTypeDocumentCategoryPartOfWeek
+ ___ATX_HISTOGRAM_FOR_TYPE___ATXHistogramTypeDocumentCategoryTrendingOpen
+ ___Block_byref_object_copy_.174
+ ___Block_byref_object_dispose_.175
+ ____ATXInitializeInOwnerProcess_block_invoke.391
+ ____ATXInitializeInOwnerProcess_block_invoke.401
+ ____ATXInitializeInOwnerProcess_block_invoke.462
+ ____ATXInitializeInOwnerProcess_block_invoke.475
+ ____ATXInitializeInOwnerProcess_block_invoke.481
+ ____ATXInitializeInOwnerProcess_block_invoke_2.407
+ ____ATXInitializeInOwnerProcess_block_invoke_2.476
+ ____ATXInitializeInOwnerProcess_block_invoke_3.477
+ ____ATXInitializeInOwnerProcess_block_invoke_3.477.cold.1
+ ___block_descriptor_32_e24_16?0"ATXIntentEvent"8l
+ ___block_descriptor_32_e42_v24?0^{ATXPredictionItem=Q[827f]fBB}8d16l
+ ___block_descriptor_3376_ea8_32s40c23_ZTS17ATXPredictionItem_e57_v16?0"ATXBehavioralPredictionsFeatureCacheGuardedData"8l
+ ___block_descriptor_40_ea8_32r_e42_v24?0^{ATXPredictionItem=Q[827f]fBB}8d16lr32l8
+ ___block_descriptor_40_ea8_32s_e40_v16?0r^{ATXPredictionItem=Q[827f]fBB}8ls32l8
+ ___block_descriptor_40_ea8_32s_e42_v24?0^{ATXPredictionItem=Q[827f]fBB}8d16ls32l8
+ ___block_descriptor_40_ea8_32s_e64_v24?0"ATXScoredPrediction"8r^{ATXPredictionItem=Q[827f]fBB}16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSArray"8ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40r_e40_v16?0r^{ATXPredictionItem=Q[827f]fBB}8lr40l8s32l8
+ ___block_descriptor_48_ea8_32s40r_e42_v24?0^{ATXPredictionItem=Q[827f]fBB}8d16ls32l8r40l8
+ ___block_descriptor_64_ea8_32s40r48r_e40_v16?0r^{ATXPredictionItem=Q[827f]fBB}8ls32l8r40l8r48l8
+ ___block_descriptor_80_ea8_32s40s48r56r_e40_v16?0r^{ATXPredictionItem=Q[827f]fBB}8ls32l8r48l8r56l8s40l8
+ ___block_descriptor_88_ea8_32s40s48s56s64r_e40_v16?0r^{ATXPredictionItem=Q[827f]fBB}8lr64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.200
+ ___block_literal_global.2496
+ ___block_literal_global.383
+ ___block_literal_global.389
+ ___block_literal_global.394
+ ___block_literal_global.409
+ ___block_literal_global.416
+ ___block_literal_global.421
+ ___block_literal_global.426
+ ___block_literal_global.428
+ ___block_literal_global.430
+ ___block_literal_global.432
+ ___block_literal_global.434
+ ___block_literal_global.442
+ ___block_literal_global.464
+ ___block_literal_global.474
+ ___block_literal_global.479
+ ___block_literal_global.483
+ ___block_literal_global.485
+ ___block_literal_global.489
+ ___block_literal_global.494
+ ___block_literal_global.504
+ ___block_literal_global.514
+ ___block_literal_global.518
+ ___block_literal_global.523
+ ___block_literal_global.527
+ ___block_literal_global.535
+ ___block_literal_global.542
+ ___block_literal_global.547
+ ___block_literal_global.551
+ ___block_literal_global.555
+ ___block_literal_global.559
+ ___block_literal_global.563
+ ___block_literal_global.567
+ ___block_literal_global.573
+ ___block_literal_global.579
+ ___block_literal_global.584
+ ___block_literal_global.588
+ ___block_literal_global.602
+ ___block_literal_global.608
+ ___block_literal_global.616
+ ___block_literal_global.624
+ ___block_literal_global.630
+ ___block_literal_global.635
+ ___block_literal_global.639
+ ___block_literal_global.643
+ ___block_literal_global.647
+ ___block_literal_global.652
+ ___block_literal_global.659
+ ___block_literal_global.663
+ ___block_literal_global.667
+ ___block_literal_global.671
+ ___block_literal_global.677
+ ___block_literal_global.686
+ ___block_literal_global.693
+ ___block_literal_global.697
+ ___block_literal_global.701
+ ___block_literal_global.722
+ ___block_literal_global.726
+ ___block_literal_global.730
+ ___block_literal_global.735
+ ___block_literal_global.744
+ ___registerForBackupBGSTJob_block_invoke.515
+ ___registerForDailyRoutinesCTSJob_block_invoke.530
+ ___registerForEverydayShortcutsTriggersCTSJobs_block_invoke.525
+ ___registerForFaceSuggestionsCTSJob_block_invoke.653
+ ___registerForFaceSuggestionsCTSJob_block_invoke.653.cold.1
+ ___registerForNotificationAndSuggestionDatastorePruning_block_invoke.704
+ ___registerForRestoreStateNotifications_block_invoke.491
+ ___registerForUserRequestedBackupJob_block_invoke.502
+ _objc_msgSend$documentAirplaneModeDecayHalflife
+ _objc_msgSend$documentAirplaneModeHistogram
+ _objc_msgSend$documentAmbientLightDecayHalflife
+ _objc_msgSend$documentAmbientLightHistogram
+ _objc_msgSend$documentCategoryDayOfWeekDecayHalflife
+ _objc_msgSend$documentCategoryDayOfWeekHistogram
+ _objc_msgSend$documentCategoryOpenDecayHalflife
+ _objc_msgSend$documentCategoryOpenHistogram
+ _objc_msgSend$documentCategoryPartOfWeekDecayHalflife
+ _objc_msgSend$documentCategoryPartOfWeekHistogram
+ _objc_msgSend$documentCategoryTrendingOpenDecayHalflife
+ _objc_msgSend$documentCategoryTrendingOpenHistogram
+ _objc_msgSend$documentConfirmsDecayHalflife
+ _objc_msgSend$documentConfirmsHistogram
+ _objc_msgSend$documentCoreMotionOpenDecayHalflife
+ _objc_msgSend$documentCoreMotionOpenHistogram
+ _objc_msgSend$documentDayOfWeekDecayHalflife
+ _objc_msgSend$documentDayOfWeekHistogram
+ _objc_msgSend$documentOpenDecayHalflife
+ _objc_msgSend$documentOpenHistogram
+ _objc_msgSend$documentPartOfWeekDecayHalflife
+ _objc_msgSend$documentPartOfWeekHistogram
+ _objc_msgSend$documentTrendingOpenDecayHalflife
+ _objc_msgSend$documentTrendingOpenHistogram
+ _objc_msgSend$documentUnlockTimeDecayHalflife
+ _objc_msgSend$documentUnlockTimeHistogram
+ _objc_msgSend$documentWifiOpenDecayHalflife
+ _objc_msgSend$documentWifiOpenHistogram
+ _objc_msgSend$getSortedCombinedIntentEventsForTestingActionsBetweenStartDate:endDate:
+ _objc_msgSend$harvestDataFromActionPredictionItem:isMenuItem:itemIndex:itemOutcome:sessionOutcome:sessionUUID:numItemsInSession:
- +[ATXAppPredictionDataHarvester harvestDataFromActionPredictionItem:itemIndex:itemOutcome:sessionOutcome:sessionUUID:numItemsInSession:]
- ___200-[_ATXAppPredictor predictWithLimit:consumerSubType:intent:candidateBundleIdentifiers:candidateActiontypes:scoreLogger:predictionItemsToKeep:predictedItemsOutParameter:context:datastore:featureCache:]_block_invoke.187
- ___58-[ATXFaceGalleryLayoutGenerator rankedFeaturedDescriptors]_block_invoke.63
- ___64-[ATXUpdatePredictionsManager processAppDirectoryFeedbackNoSync]_block_invoke_2
- ___71-[_ATXAppPredictor scoreActionWithFeaturesUsingCoreML:consumerSubType:]_block_invoke.cold.1
- ___72-[_ATXAppPredictor scoreActionsWithFeaturesUsingCoreML:consumerSubType:]_block_invoke.cold.1
- ___Block_byref_object_copy_.176
- ___Block_byref_object_dispose_.177
- ____ATXInitializeInOwnerProcess_block_invoke.388
- ____ATXInitializeInOwnerProcess_block_invoke.398
- ____ATXInitializeInOwnerProcess_block_invoke.459
- ____ATXInitializeInOwnerProcess_block_invoke.469
- ____ATXInitializeInOwnerProcess_block_invoke.478
- ____ATXInitializeInOwnerProcess_block_invoke_2.404
- ____ATXInitializeInOwnerProcess_block_invoke_2.473
- ____ATXInitializeInOwnerProcess_block_invoke_3.474
- ____ATXInitializeInOwnerProcess_block_invoke_3.474.cold.1
- ___block_descriptor_32_e42_v24?0^{ATXPredictionItem=Q[817f]fBB}8d16l
- ___block_descriptor_3336_ea8_32s40c23_ZTS17ATXPredictionItem_e57_v16?0"ATXBehavioralPredictionsFeatureCacheGuardedData"8l
- ___block_descriptor_40_ea8_32r_e42_v24?0^{ATXPredictionItem=Q[817f]fBB}8d16lr32l8
- ___block_descriptor_40_ea8_32s_e40_v16?0r^{ATXPredictionItem=Q[817f]fBB}8ls32l8
- ___block_descriptor_40_ea8_32s_e64_v24?0"ATXScoredPrediction"8r^{ATXPredictionItem=Q[817f]fBB}16ls32l8
- ___block_descriptor_48_ea8_32s40r_e40_v16?0r^{ATXPredictionItem=Q[817f]fBB}8lr40l8s32l8
- ___block_descriptor_64_ea8_32s40r48r_e40_v16?0r^{ATXPredictionItem=Q[817f]fBB}8ls32l8r40l8r48l8
- ___block_descriptor_80_ea8_32s40s48r56r_e40_v16?0r^{ATXPredictionItem=Q[817f]fBB}8ls32l8r48l8r56l8s40l8
- ___block_descriptor_88_ea8_32s40s48s56s64r_e40_v16?0r^{ATXPredictionItem=Q[817f]fBB}8lr64l8s32l8s40l8s48l8s56l8
- ___block_literal_global.2466
- ___block_literal_global.367
- ___block_literal_global.380
- ___block_literal_global.386
- ___block_literal_global.391
- ___block_literal_global.406
- ___block_literal_global.413
- ___block_literal_global.418
- ___block_literal_global.420
- ___block_literal_global.425
- ___block_literal_global.427
- ___block_literal_global.429
- ___block_literal_global.431
- ___block_literal_global.439
- ___block_literal_global.461
- ___block_literal_global.471
- ___block_literal_global.476
- ___block_literal_global.480
- ___block_literal_global.482
- ___block_literal_global.486
- ___block_literal_global.491
- ___block_literal_global.495
- ___block_literal_global.511
- ___block_literal_global.515
- ___block_literal_global.524
- ___block_literal_global.526
- ___block_literal_global.536
- ___block_literal_global.544
- ___block_literal_global.548
- ___block_literal_global.552
- ___block_literal_global.556
- ___block_literal_global.560
- ___block_literal_global.564
- ___block_literal_global.570
- ___block_literal_global.576
- ___block_literal_global.581
- ___block_literal_global.585
- ___block_literal_global.596
- ___block_literal_global.605
- ___block_literal_global.610
- ___block_literal_global.621
- ___block_literal_global.627
- ___block_literal_global.632
- ___block_literal_global.636
- ___block_literal_global.640
- ___block_literal_global.644
- ___block_literal_global.649
- ___block_literal_global.653
- ___block_literal_global.660
- ___block_literal_global.664
- ___block_literal_global.668
- ___block_literal_global.674
- ___block_literal_global.680
- ___block_literal_global.687
- ___block_literal_global.698
- ___block_literal_global.703
- ___block_literal_global.719
- ___block_literal_global.723
- ___block_literal_global.727
- ___block_literal_global.732
- ___block_literal_global.741
- ___registerForBackupBGSTJob_block_invoke.512
- ___registerForDailyRoutinesCTSJob_block_invoke.527
- ___registerForEverydayShortcutsTriggersCTSJobs_block_invoke.522
- ___registerForFaceSuggestionsCTSJob_block_invoke.650
- ___registerForFaceSuggestionsCTSJob_block_invoke.650.cold.1
- ___registerForNotificationAndSuggestionDatastorePruning_block_invoke.701
- ___registerForRestoreStateNotifications_block_invoke.488
- ___registerForUserRequestedBackupJob_block_invoke.499
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_AppPredictionInternal
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AppPredictionInternal
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AppPredictionInternal
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AppPredictionInternal
- _objc_msgSend$harvestDataFromActionPredictionItem:itemIndex:itemOutcome:sessionOutcome:sessionUUID:numItemsInSession:
CStrings:
+ "@16@?0@\"ATXIntentEvent\"8"
+ "@24@0:8^{ATXPredictionItem=@Q[827f]fBB}16"
+ "@24@0:8r^{ATXPredictionItem=@Q[827f]fBB}16"
+ "@32@0:8^{ATXPredictionItem=@Q[827f]fBB}16@24"
+ "@3352@0:8{ATXPredictionItem=@Q[827f]fBB}16"
+ "@3360@0:8{ATXPredictionItem=@Q[827f]fBB}16@3352"
+ "@3368@0:8{ATXPredictionItem=@Q[827f]fBB}16@3352@3360"
+ "@3388@0:8@16@24@32f40@44{ATXPredictionItem=@Q[827f]fBB}52"
+ "@40@0:8@16r^{ATXPredictionItem=@Q[827f]fBB}24@32"
+ "@56@0:8@16r^{ATXPredictionItem=@Q[827f]fBB}24d32@40@48"
+ "@64@0:8@16@24@32r^{ATXPredictionItem=@Q[827f]fBB}40d48@56"
+ "@72@0:8@16@24r^{ATXPredictionItem=@Q[827f]fBB}32d40@48i56B60@64"
+ "@80@0:8@16@24r^{ATXPredictionItem=@Q[827f]fBB}32d40@48i56B60^v64@72"
+ "Action %@ has a score of %f which is below the confidenceThreshold of %f"
+ "B3352@0:8{ATXPredictionItem=@Q[827f]fBB}16"
+ "B40@0:8^{ATXPredictionItem=@Q[827f]fBB}16@?24^@32"
+ "DocumentAirplaneModeDecayHalflife"
+ "DocumentAmbientLightDecayHalflife"
+ "DocumentAssociatedAppPredictionScore"
+ "DocumentCategoryDayOfWeekDecayHalflife"
+ "DocumentCategoryDayOfWeekPopularity"
+ "DocumentCategoryDayOfWeekRelativePopularity"
+ "DocumentCategoryOpenDecayHalflife"
+ "DocumentCategoryPartOfWeekDecayHalflife"
+ "DocumentCategoryPartOfWeekPopularity"
+ "DocumentCategoryPartOfWeekRelativePopularity"
+ "DocumentCategoryPopularity"
+ "DocumentCategoryTrendingOpenDecayHalflife"
+ "DocumentCategoryTrendingPopularity"
+ "DocumentConfirmsDecayHalflife"
+ "DocumentCoreMotionOpenDecayHalflife"
+ "DocumentCreatedAge"
+ "DocumentDayOfWeekDecayHalflife"
+ "DocumentModifiedAge"
+ "DocumentOpenDecayHalflife"
+ "DocumentOpenedAge"
+ "DocumentPartOfWeekDecayHalflife"
+ "DocumentTrendingOpenDecayHalflife"
+ "DocumentUnlockTimeDecayHalflife"
+ "DocumentWifiOpenDecayHalflife"
+ "Got a score of %f for %@ by model %@"
+ "Got app directory feedback: %@"
+ "Sending action back to ZKW: %@"
+ "T@\"_ATXAppLaunchCategoricalHistogram\",R,N,V_documentAmbientLightHistogram"
+ "T@\"_ATXAppLaunchCategoricalHistogram\",R,N,V_documentCategoryPartOfWeekHistogram"
+ "T@\"_ATXAppLaunchCategoricalHistogram\",R,N,V_documentCoreMotionOpenHistogram"
+ "T@\"_ATXAppLaunchCategoricalHistogram\",R,N,V_documentPartOfWeekHistogram"
+ "T@\"_ATXAppLaunchCategoricalHistogram\",R,N,V_documentWifiOpenHistogram"
+ "T@\"_ATXAppLaunchHistogram\",R,N,V_documentAirplaneModeHistogram"
+ "T@\"_ATXAppLaunchHistogram\",R,N,V_documentCategoryDayOfWeekHistogram"
+ "T@\"_ATXAppLaunchHistogram\",R,N,V_documentCategoryOpenHistogram"
+ "T@\"_ATXAppLaunchHistogram\",R,N,V_documentCategoryTrendingOpenHistogram"
+ "T@\"_ATXAppLaunchHistogram\",R,N,V_documentConfirmsHistogram"
+ "T@\"_ATXAppLaunchHistogram\",R,N,V_documentDayOfWeekHistogram"
+ "T@\"_ATXAppLaunchHistogram\",R,N,V_documentOpenHistogram"
+ "T@\"_ATXAppLaunchHistogram\",R,N,V_documentTrendingOpenHistogram"
+ "T@\"_ATXAppLaunchHistogram\",R,N,V_documentUnlockTimeHistogram"
+ "T^{ATXPredictionItem=@Q[827f]fBB},N,V_predictionItem"
+ "Tr^{ATXPredictionItem=@Q[827f]fBB},R,N"
+ "T{ATXPredictionItem=@Q[827f]fBB},N"
+ "[827f]"
+ "^{ATXPredictionItem=@Q[827f]fBB}16@0:8"
+ "_ATXHistogramTypeDocumentCategoryDayOfWeek"
+ "_ATXHistogramTypeDocumentCategoryOpen"
+ "_ATXHistogramTypeDocumentCategoryPartOfWeek"
+ "_ATXHistogramTypeDocumentCategoryTrendingOpen"
+ "_ATXScoreInputDocumentAssociatedAppPredictionScore"
+ "_ATXScoreInputDocumentCategoryDayOfWeekPopularity"
+ "_ATXScoreInputDocumentCategoryDayOfWeekRelativePopularity"
+ "_ATXScoreInputDocumentCategoryPartOfWeekPopularity"
+ "_ATXScoreInputDocumentCategoryPartOfWeekRelativePopularity"
+ "_ATXScoreInputDocumentCategoryPopularity"
+ "_ATXScoreInputDocumentCategoryTrendingPopularity"
+ "_ATXScoreInputDocumentCreatedAge"
+ "_ATXScoreInputDocumentModifiedAge"
+ "_ATXScoreInputDocumentOpenedAge"
+ "_documentAirplaneModeHistogram"
+ "_documentAmbientLightHistogram"
+ "_documentCategoryDayOfWeekHistogram"
+ "_documentCategoryOpenHistogram"
+ "_documentCategoryPartOfWeekHistogram"
+ "_documentCategoryTrendingOpenHistogram"
+ "_documentConfirmsHistogram"
+ "_documentCoreMotionOpenHistogram"
+ "_documentDayOfWeekHistogram"
+ "_documentOpenHistogram"
+ "_documentPartOfWeekHistogram"
+ "_documentTrendingOpenHistogram"
+ "_documentUnlockTimeHistogram"
+ "_documentWifiOpenHistogram"
+ "d24@0:8^{ATXPredictionItem=@Q[827f]fBB}16"
+ "d28@0:8^{ATXPredictionItem=@Q[827f]fBB}16C24"
+ "d52@0:8^{ATXPredictionItem=@Q[827f]fBB}16@24C32@36@44"
+ "documentAirplaneModeDecayHalflife"
+ "documentAirplaneModeHistogram"
+ "documentAmbientLightDecayHalflife"
+ "documentAmbientLightHistogram"
+ "documentCategoryDayOfWeekDecayHalflife"
+ "documentCategoryDayOfWeekHistogram"
+ "documentCategoryOpenDecayHalflife"
+ "documentCategoryOpenHistogram"
+ "documentCategoryPartOfWeekDecayHalflife"
+ "documentCategoryPartOfWeekHistogram"
+ "documentCategoryTrendingOpenDecayHalflife"
+ "documentCategoryTrendingOpenHistogram"
+ "documentConfirmsDecayHalflife"
+ "documentConfirmsHistogram"
+ "documentCoreMotionOpenDecayHalflife"
+ "documentCoreMotionOpenHistogram"
+ "documentDayOfWeekDecayHalflife"
+ "documentDayOfWeekHistogram"
+ "documentOpenDecayHalflife"
+ "documentOpenHistogram"
+ "documentPartOfWeekDecayHalflife"
+ "documentPartOfWeekHistogram"
+ "documentTrendingOpenDecayHalflife"
+ "documentTrendingOpenHistogram"
+ "documentUnlockTimeDecayHalflife"
+ "documentUnlockTimeHistogram"
+ "documentWifiOpenDecayHalflife"
+ "documentWifiOpenHistogram"
+ "fetchLastExecutedActionsWithCompletion:"
+ "getSortedCombinedIntentEventsForTestingActionsBetweenStartDate:endDate:"
+ "harvestDataFromActionPredictionItem:isMenuItem:itemIndex:itemOutcome:sessionOutcome:sessionUUID:numItemsInSession:"
+ "isMenuItem"
+ "q3352@0:8{ATXPredictionItem=@Q[827f]fBB}16"
+ "r^{ATXPredictionItem=@Q[827f]fBB}16@0:8"
+ "v16@?0r^{ATXPredictionItem=@Q[827f]fBB}8"
+ "v24@0:8^{ATXPredictionItem=@Q[827f]fBB}16"
+ "v24@0:8r^{ATXPredictionItem=@Q[827f]fBB}16"
+ "v24@?0@\"ATXScoredPrediction\"8r^{ATXPredictionItem=@Q[827f]fBB}16"
+ "v24@?0^{ATXPredictionItem=@Q[827f]fBB}8d16"
+ "v32@0:8^{ATXPredictionItem=@Q[827f]fBB}16@24"
+ "v32@0:8r^{ATXPredictionItem=@Q[827f]fBB}16^{ATXPredictionItem=@Q[827f]fBB}24"
+ "v3352@0:8{ATXPredictionItem=@Q[827f]fBB}16"
+ "v3360@0:8{ATXPredictionItem=@Q[827f]fBB}16@3352"
+ "v40@0:8@16r^{ATXPredictionItem=@Q[827f]fBB}24d32"
+ "v40@0:8^{ATXPredictionItem=@Q[827f]fBB}16Q24@32"
+ "v48@0:8^{ATXPredictionItem=@Q[827f]fBB}16@24@32@40"
+ "v64@0:8r^{ATXPredictionItem=@Q[827f]fBB}16Q24Q32Q40@48Q56"
+ "v68@0:8@16B24Q28Q36Q44@52Q60"
+ "{ATXPredictionItem=\"key\"@\"NSString\"\"actionHash\"Q\"inputSignals\"[827f]\"score\"f\"isMediumConfidenceForBlendingLayer\"B\"isHighConfidenceForBlendingLayer\"B}"
+ "{ATXPredictionItem=@Q[827f]fBB}16@0:8"
+ "{ATXPredictionItem=@Q[827f]fBB}24@0:8@16"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x91"
- "@24@0:8^{ATXPredictionItem=@Q[817f]fBB}16"
- "@24@0:8r^{ATXPredictionItem=@Q[817f]fBB}16"
- "@32@0:8^{ATXPredictionItem=@Q[817f]fBB}16@24"
- "@3312@0:8{ATXPredictionItem=@Q[817f]fBB}16"
- "@3320@0:8{ATXPredictionItem=@Q[817f]fBB}16@3312"
- "@3328@0:8{ATXPredictionItem=@Q[817f]fBB}16@3312@3320"
- "@3348@0:8@16@24@32f40@44{ATXPredictionItem=@Q[817f]fBB}52"
- "@40@0:8@16r^{ATXPredictionItem=@Q[817f]fBB}24@32"
- "@56@0:8@16r^{ATXPredictionItem=@Q[817f]fBB}24d32@40@48"
- "@64@0:8@16@24@32r^{ATXPredictionItem=@Q[817f]fBB}40d48@56"
- "@72@0:8@16@24r^{ATXPredictionItem=@Q[817f]fBB}32d40@48i56B60@64"
- "@80@0:8@16@24r^{ATXPredictionItem=@Q[817f]fBB}32d40@48i56B60^v64@72"
- "B3312@0:8{ATXPredictionItem=@Q[817f]fBB}16"
- "B40@0:8^{ATXPredictionItem=@Q[817f]fBB}16@?24^@32"
- "T^{ATXPredictionItem=@Q[817f]fBB},N,V_predictionItem"
- "Tr^{ATXPredictionItem=@Q[817f]fBB},R,N"
- "T{ATXPredictionItem=@Q[817f]fBB},N"
- "[817f]"
- "^{ATXPredictionItem=@Q[817f]fBB}16@0:8"
- "d24@0:8^{ATXPredictionItem=@Q[817f]fBB}16"
- "d28@0:8^{ATXPredictionItem=@Q[817f]fBB}16C24"
- "d52@0:8^{ATXPredictionItem=@Q[817f]fBB}16@24C32@36@44"
- "harvestDataFromActionPredictionItem:itemIndex:itemOutcome:sessionOutcome:sessionUUID:numItemsInSession:"
- "q3312@0:8{ATXPredictionItem=@Q[817f]fBB}16"
- "r^{ATXPredictionItem=@Q[817f]fBB}16@0:8"
- "v16@?0r^{ATXPredictionItem=@Q[817f]fBB}8"
- "v24@0:8^{ATXPredictionItem=@Q[817f]fBB}16"
- "v24@0:8r^{ATXPredictionItem=@Q[817f]fBB}16"
- "v24@?0@\"ATXScoredPrediction\"8r^{ATXPredictionItem=@Q[817f]fBB}16"
- "v24@?0^{ATXPredictionItem=@Q[817f]fBB}8d16"
- "v32@0:8^{ATXPredictionItem=@Q[817f]fBB}16@24"
- "v32@0:8r^{ATXPredictionItem=@Q[817f]fBB}16^{ATXPredictionItem=@Q[817f]fBB}24"
- "v3312@0:8{ATXPredictionItem=@Q[817f]fBB}16"
- "v3320@0:8{ATXPredictionItem=@Q[817f]fBB}16@3312"
- "v40@0:8@16r^{ATXPredictionItem=@Q[817f]fBB}24d32"
- "v40@0:8^{ATXPredictionItem=@Q[817f]fBB}16Q24@32"
- "v48@0:8^{ATXPredictionItem=@Q[817f]fBB}16@24@32@40"
- "v64@0:8r^{ATXPredictionItem=@Q[817f]fBB}16Q24Q32Q40@48Q56"
- "{ATXPredictionItem=\"key\"@\"NSString\"\"actionHash\"Q\"inputSignals\"[817f]\"score\"f\"isMediumConfidenceForBlendingLayer\"B\"isHighConfidenceForBlendingLayer\"B}"
- "{ATXPredictionItem=@Q[817f]fBB}16@0:8"
- "{ATXPredictionItem=@Q[817f]fBB}24@0:8@16"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0A"

```
