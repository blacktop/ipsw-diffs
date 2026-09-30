## PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

-255.0.0.0.0
-  __TEXT.__text: 0x722bc
+265.0.0.0.0
+  __TEXT.__text: 0x7278c
   __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_stubs: 0xb3e0
-  __TEXT.__objc_methlist: 0x71e4
-  __TEXT.__objc_classname: 0x83c
+  __TEXT.__objc_stubs: 0xb520
+  __TEXT.__objc_methlist: 0x7234
+  __TEXT.__objc_classname: 0x83e
   __TEXT.__objc_methtype: 0x1116
-  __TEXT.__cstring: 0xbe85
-  __TEXT.__objc_methname: 0x12cc6
+  __TEXT.__cstring: 0xbf65
+  __TEXT.__objc_methname: 0x12dfc
   __TEXT.__const: 0x500
   __TEXT.__gcc_except_tab: 0xe84
-  __TEXT.__oslogstring: 0x743b
+  __TEXT.__oslogstring: 0x753b
   __TEXT.__ustring: 0x10c
   __TEXT.__unwind_info: 0x12b8
   __DATA_CONST.__auth_got: 0x478
-  __DATA_CONST.__got: 0x530
+  __DATA_CONST.__got: 0x538
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x3238
-  __DATA_CONST.__cfstring: 0xf960
+  __DATA_CONST.__const: 0x3280
+  __DATA_CONST.__cfstring: 0xfaa0
   __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_floatobj: 0x1c0
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xc168
-  __DATA.__objc_selrefs: 0x3ab0
-  __DATA.__objc_ivar: 0x99c
+  __DATA.__objc_const: 0xc1c8
+  __DATA.__objc_selrefs: 0x3b00
+  __DATA.__objc_ivar: 0x9a4
   __DATA.__objc_data: 0x1d60
   __DATA.__data: 0x4d8
   __DATA.__bss: 0x50

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/Moments.framework/Moments
   - /System/Library/PrivateFrameworks/MomentsIntelligence.framework/MomentsIntelligence
   - /System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  UUID: 25060094-634D-370C-B90A-BD6C490CC3E8
-  Functions: 2627
-  Symbols:   19853
-  CStrings:  7822
+  UUID: 2D1BE678-939A-3FA7-B46E-0A2E469F4E22
+  Functions: 2635
+  Symbols:   19924
+  CStrings:  7858
 
Symbols:
+ +[MOPlatformInfo getDeviceClass]
+ +[MOPlatformInfo getDeviceClass].cold.1
+ +[MOPlatformInfo isDNUEnabled]
+ +[MOPlatformInfo isIHAEnabled]
+ -[MOEventBundleRankingInput maxSubBundleGoodnessScores]
+ -[MOEventBundleRankingInput setMaxSubBundleGoodnessScores:]
+ -[MOEventBundleRankingInput setSubBundleCount:]
+ -[MOEventBundleRankingInput subBundleCount]
+ GCC_except_table14
+ OBJC_IVAR_$_MOEventBundleRankingInput._maxSubBundleGoodnessScores
+ OBJC_IVAR_$_MOEventBundleRankingInput._subBundleCount
+ _OBJC_CLASS_$_MCProfileConnection
+ __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.1541
+ __62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke.517
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.694
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.694.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.698
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.698.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.705
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.706
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.710
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.720
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.721
+ __block_literal_global.1664
+ _kMOActivityContext
+ _kMODeviceClass
+ _kMOIsDNUEnabled
+ _kMOIsIHAEnabled
+ _kMOLocationContext
+ _kMOPeopleContext
+ _kMOPhotoTraitContext
+ _kMOTimeContext
+ _kSuggestionRecommendThresholdForThematicSummary
+ _objc_msgSend$getDeviceClass
+ _objc_msgSend$isDNUEnabled
+ _objc_msgSend$isDiagnosticSubmissionAllowed
+ _objc_msgSend$isHealthDataSubmissionAllowed
+ _objc_msgSend$isIHAEnabled
+ _objc_msgSend$maxSubBundleGoodnessScores
+ _objc_msgSend$setMaxSubBundleGoodnessScores:
+ _objc_msgSend$setSubBundleCount:
+ _objc_msgSend$sharedConnection
+ _objc_msgSend$subBundleCount
- __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.1538
- __62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke.514
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.691
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.691.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.695
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.695.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.699
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.703
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.707
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.717
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.718
- __block_literal_global.1661
CStrings:
+ "Could not get device class (MGError=%d)"
+ "PlatformInfoOverrideIsDNUEnabled"
+ "PlatformInfoOverrideIsIHAEnabled"
+ "Rejected thematic summary due to low maxSubBundleGoodnessScores or subBundleCount: suggestionID %@, maxSubBundleGoodnessScores=%.3f,subBundleCount=%lu, recommendThre=%.3f "
+ "Setting thematic summary visibility status to Recommended only: suggestionID %@, maxSubBundleGoodnessScores=%.3f,subBundleCount=%lu, recommendThre=%.3f "
+ "TQ,N,V_subBundleCount"
+ "Tf,N,V_maxSubBundleGoodnessScores"
+ "Thematic summary got rejected due to engagement signal: suggestionID %@, isBundleOrSubBundlesSelectedOrQuickAdded %d, isBundleOrSubBundleDeleted %d"
+ "_maxSubBundleGoodnessScores"
+ "_subBundleCount"
+ "activityContext"
+ "getDeviceClass"
+ "isDNUEnabled"
+ "isDiagnosticSubmissionAllowed"
+ "isHealthDataSubmissionAllowed"
+ "isIHAEnabled"
+ "kMODeviceClass"
+ "kMOIsDNUEnabled"
+ "kMOIsIHAEnabled"
+ "locationContext"
+ "maxSubBundleGoodnessScores"
+ "peopleContext"
+ "photoTraitContext"
+ "setMaxSubBundleGoodnessScores:"
+ "setSubBundleCount:"
+ "sharedConnection"
+ "subBundleCount"
+ "suggestionRecommendThresholdForThematicSummary"
- "Setting thematic summary visibility status to Recommended only: bundleID %@, suggestionID %@"
- "Thematic summary gotgot rejected due to engagement signal: bundleID %@, suggestionID %@, isBundleOrSubBundlesSelectedOrQuickAdded %d, isBundleOrSubBundleDeleted %d"

```
