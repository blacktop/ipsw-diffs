## NewsCore

> `/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore`

```diff

-3422.4.0.0.0
-  __TEXT.__text: 0x2bd470
+3529.2.0.0.0
+  __TEXT.__text: 0x2bee0c
   __TEXT.__auth_stubs: 0x1310
-  __TEXT.__objc_methlist: 0x28028
-  __TEXT.__const: 0x13d8
+  __TEXT.__objc_methlist: 0x28300
+  __TEXT.__const: 0x13e8
   __TEXT.__swift5_typeref: 0x89
-  __TEXT.__cstring: 0x461b8
-  __TEXT.__oslogstring: 0xe990
+  __TEXT.__cstring: 0x45440
+  __TEXT.__oslogstring: 0xed20
   __TEXT.__gcc_except_tab: 0x350c
   __TEXT.__dlopen_cstrs: 0x11c
   __TEXT.__ustring: 0x122
-  __TEXT.__unwind_info: 0x9794
-  __TEXT.__objc_classname: 0x6818
-  __TEXT.__objc_methname: 0x77b8f
-  __TEXT.__objc_methtype: 0xb8ce
-  __TEXT.__objc_stubs: 0x30860
+  __TEXT.__unwind_info: 0x97ec
+  __TEXT.__objc_classname: 0x6886
+  __TEXT.__objc_methname: 0x786f7
+  __TEXT.__objc_methtype: 0xb924
+  __TEXT.__objc_stubs: 0x30a60
   __DATA_CONST.__got: 0x368
-  __DATA_CONST.__const: 0xf978
-  __DATA_CONST.__objc_classlist: 0x1890
+  __DATA_CONST.__const: 0xfa00
+  __DATA_CONST.__objc_classlist: 0x18a8
   __DATA_CONST.__objc_catlist: 0x268
   __DATA_CONST.__objc_protolist: 0x6b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5eea8
-  __DATA_CONST.__objc_selrefs: 0x121e0
+  __DATA_CONST.__objc_const: 0x5f498
+  __DATA_CONST.__objc_selrefs: 0x12338
   __DATA_CONST.__objc_arraydata: 0xfc8
-  __AUTH_CONST.__const: 0x45d0
-  __AUTH_CONST.__objc_const: 0x120f8
-  __AUTH_CONST.__cfstring: 0x28900
+  __AUTH_CONST.__const: 0x4590
+  __AUTH_CONST.__objc_const: 0x121d0
+  __AUTH_CONST.__cfstring: 0x28e60
   __AUTH_CONST.__objc_intobj: 0x1308
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0xbe0
   __AUTH_CONST.__objc_doubleobj: 0x100
   __AUTH_CONST.__auth_got: 0x9a0
-  __AUTH.__objc_data: 0x3930
+  __AUTH.__objc_data: 0x3a20
   __DATA.__objc_protorefs: 0xa8
-  __DATA.__objc_classrefs: 0x1df0
-  __DATA.__objc_superrefs: 0x1300
-  __DATA.__objc_ivar: 0x3c7c
-  __DATA.__data: 0x50b0
+  __DATA.__objc_classrefs: 0x1df8
+  __DATA.__objc_superrefs: 0x1318
+  __DATA.__objc_ivar: 0x3cd0
+  __DATA.__data: 0x50b8
   __DATA.__common: 0x8
   __DATA.__bss: 0x58
-  __DATA_DIRTY.__objc_ivar: 0xe74
+  __DATA_DIRTY.__objc_ivar: 0xe70
   __DATA_DIRTY.__objc_data: 0xbc70
   __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__common: 0x170
-  __DATA_DIRTY.__bss: 0xe68
+  __DATA_DIRTY.__bss: 0xe48
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17468
-  Symbols:   56856
-  CStrings:  27129
+  Functions: 17525
+  Symbols:   57037
+  CStrings:  27286
 
Symbols:
+ +[NSURL(FCAdditions) fc_NewsURLWithPathComponents:]
+ -[FCAssertPreparedFeedPersonalizer .cxx_destruct]
+ -[FCAssertPreparedFeedPersonalizer decayedPublisherDiversificationPenalty]
+ -[FCAssertPreparedFeedPersonalizer fetchAggregateMapForPersonalizingItem:completion:]
+ -[FCAssertPreparedFeedPersonalizer initWithTarget:]
+ -[FCAssertPreparedFeedPersonalizer init]
+ -[FCAssertPreparedFeedPersonalizer isPreparedForUse]
+ -[FCAssertPreparedFeedPersonalizer limitItemsByFlowRate:timeInterval:publisherCount:]
+ -[FCAssertPreparedFeedPersonalizer limitItemsByMinimumItemQuality:]
+ -[FCAssertPreparedFeedPersonalizer prepareForUseWithCompletionHandler:]
+ -[FCAssertPreparedFeedPersonalizer rankTagIDsDescending:]
+ -[FCAssertPreparedFeedPersonalizer scoresForTagIDs:]
+ -[FCAssertPreparedFeedPersonalizer setPreparedForUse:]
+ -[FCAssertPreparedFeedPersonalizer sortItems:options:configurationSet:]
+ -[FCAssertPreparedFeedPersonalizer target]
+ -[FCESLInventory _adoptInventory:]
+ -[FCESLInventory _rescoreInventoryIfNeeded:forScoringVersion:]
+ -[FCESLInventory allFeedItemScoreProfilesForConfigurationSet:scoringVersion:]
+ -[FCFeedItemScoreCache .cxx_destruct]
+ -[FCFeedItemScoreCache _accessScoreCacheForForConfigurationSet:withBlock:]
+ -[FCFeedItemScoreCache addScoreProfiles:configurationSet:]
+ -[FCFeedItemScoreCache feedPersonalizer]
+ -[FCFeedItemScoreCache initWithFeedPersonalizer:]
+ -[FCFeedItemScoreCache scoreProfilesByConfigurationSet]
+ -[FCFeedItemScoreCache scoreProfilesForFeedItems:configurationSet:]
+ -[FCFeedPersonalizedItemScoreProfile coefficients]
+ -[FCFeedPersonalizedItemScoreProfile globalCohort]
+ -[FCFeedPersonalizedItemScoreProfile setCoefficients:]
+ -[FCFeedPersonalizedItemScoreProfile setGlobalCohort:]
+ -[FCMyArticlesOperation prewarmScoreCache:]
+ -[FCNewsAppConfig shouldShuffleReportedHeadlines]
+ -[FCNewsAppConfig statelessPersonalizationAllowedForExtensions]
+ -[FCNewsPersonalizationTrainingConfiguration disableTrainingLegacyAggregates]
+ -[FCNewsPersonalizationTrainingConfiguration legacyBridgeConfiguration]
+ -[FCNewsPersonalizationTrainingConfiguration setDisableTrainingLegacyAggregates:]
+ -[FCNewsPersonalizationTrainingConfiguration setLegacyBridgeConfiguration:]
+ -[FCNewsPersonalizationTrainingLegacyBridgeConfiguration allowAllLegacyAggregatesToActAsPriors]
+ -[FCNewsPersonalizationTrainingLegacyBridgeConfiguration avoidDoubleCountingWhenPrioringWithLegacyAggregates]
+ -[FCNewsPersonalizationTrainingLegacyBridgeConfiguration createStatelessAggregatesWhichOnlyExistInLegacy]
+ -[FCNewsPersonalizationTrainingLegacyBridgeConfiguration description]
+ -[FCNewsPersonalizationTrainingLegacyBridgeConfiguration disablePrioringBaseline]
+ -[FCNewsPersonalizationTrainingLegacyBridgeConfiguration initWithDictionary:]
+ -[FCNewsPersonalizationTrainingLegacyBridgeConfiguration legacyDecayRate]
+ -[FCNewsPersonalizationTrainingLegacyBridgeConfiguration legacyMaxLinearImpressionCount]
+ -[FCNewsPersonalizationTrainingLegacyBridgeConfiguration legacyMultiplier]
+ -[FCNewsPersonalizationTrainingLegacyBridgeConfiguration priorStatelessAggregatesWithLegacyAggregates]
+ -[FCNewsPersonalizationTrainingLegacyBridgeConfiguration setAllowAllLegacyAggregatesToActAsPriors:]
+ -[FCNewsPersonalizationTrainingLegacyBridgeConfiguration setAvoidDoubleCountingWhenPrioringWithLegacyAggregates:]
+ -[FCNewsPersonalizationTrainingLegacyBridgeConfiguration setCreateStatelessAggregatesWhichOnlyExistInLegacy:]
+ -[FCNewsPersonalizationTrainingLegacyBridgeConfiguration setDisablePrioringBaseline:]
+ -[FCNewsPersonalizationTrainingLegacyBridgeConfiguration setLegacyDecayRate:]
+ -[FCNewsPersonalizationTrainingLegacyBridgeConfiguration setLegacyMaxLinearImpressionCount:]
+ -[FCNewsPersonalizationTrainingLegacyBridgeConfiguration setLegacyMultiplier:]
+ -[FCNewsPersonalizationTrainingLegacyBridgeConfiguration setPriorStatelessAggregatesWithLegacyAggregates:]
+ -[FCNewsPersonalizationTrainingLegacyBridgeConfiguration setStatelessMaxLinearImpressionCount:]
+ -[FCNewsPersonalizationTrainingLegacyBridgeConfiguration statelessMaxLinearImpressionCount]
+ -[FCPersonalizationTreatment scoringVersion]
+ -[FCPersonalizationTreatment setScoringVersion:]
+ -[FCPuzzleHistory updatePuzzle:puzzleTypeID:progressData:progressLevel:playDuration:isSolved:]
+ -[FCSmarterMessagingConfig maxPuzzleHubInfoBubbleTipPresentations]
+ -[FCSmarterMessagingConfig puzzleHubInfoBubbleTipBody]
+ -[FCSmarterMessagingConfig puzzleHubInfoBubbleTipIconUrl]
+ -[FCSmarterMessagingConfig puzzleHubInfoBubbleTipPresentationsQuiescenceInterval]
+ -[FCSmarterMessagingConfig puzzleHubInfoBubbleTipTitle]
+ -[FCSmarterMessagingConfig setPuzzleHubInfoBubbleTipBody:]
+ -[FCSmarterMessagingConfig setPuzzleHubInfoBubbleTipIconUrl:]
+ -[FCSmarterMessagingConfig setPuzzleHubInfoBubbleTipTitle:]
+ -[NTPBScoreProfileDebug(FCAdditions) scoringAssetsIdentifier]
+ -[NTPBScoreProfileDebug(FCAdditions) setScoringAssetsIdentifier:]
+ _FCFeedFilterOptionToNSString
+ _OBJC_CLASS_$_FCAssertPreparedFeedPersonalizer
+ _OBJC_CLASS_$_FCFeedItemScoreCache
+ _OBJC_CLASS_$_FCNewsPersonalizationTrainingLegacyBridgeConfiguration
+ _OBJC_IVAR_$_FCAssertPreparedFeedPersonalizer._preparedForUse
+ _OBJC_IVAR_$_FCAssertPreparedFeedPersonalizer._target
+ _OBJC_IVAR_$_FCFeedItemScoreCache._feedPersonalizer
+ _OBJC_IVAR_$_FCFeedItemScoreCache._scoreProfilesByConfigurationSet
+ _OBJC_IVAR_$_FCFeedPersonalizedItemScoreProfile._coefficients
+ _OBJC_IVAR_$_FCFeedPersonalizedItemScoreProfile._globalCohort
+ _OBJC_IVAR_$_FCNewsPersonalizationTrainingConfiguration._disableTrainingLegacyAggregates
+ _OBJC_IVAR_$_FCNewsPersonalizationTrainingConfiguration._legacyBridgeConfiguration
+ _OBJC_IVAR_$_FCNewsPersonalizationTrainingLegacyBridgeConfiguration._allowAllLegacyAggregatesToActAsPriors
+ _OBJC_IVAR_$_FCNewsPersonalizationTrainingLegacyBridgeConfiguration._avoidDoubleCountingWhenPrioringWithLegacyAggregates
+ _OBJC_IVAR_$_FCNewsPersonalizationTrainingLegacyBridgeConfiguration._createStatelessAggregatesWhichOnlyExistInLegacy
+ _OBJC_IVAR_$_FCNewsPersonalizationTrainingLegacyBridgeConfiguration._disablePrioringBaseline
+ _OBJC_IVAR_$_FCNewsPersonalizationTrainingLegacyBridgeConfiguration._legacyDecayRate
+ _OBJC_IVAR_$_FCNewsPersonalizationTrainingLegacyBridgeConfiguration._legacyMaxLinearImpressionCount
+ _OBJC_IVAR_$_FCNewsPersonalizationTrainingLegacyBridgeConfiguration._legacyMultiplier
+ _OBJC_IVAR_$_FCNewsPersonalizationTrainingLegacyBridgeConfiguration._priorStatelessAggregatesWithLegacyAggregates
+ _OBJC_IVAR_$_FCNewsPersonalizationTrainingLegacyBridgeConfiguration._statelessMaxLinearImpressionCount
+ _OBJC_IVAR_$_FCPersonalizationTreatment._scoringVersion
+ _OBJC_IVAR_$_FCSmarterMessagingConfig._maxPuzzleHubInfoBubbleTipPresentations
+ _OBJC_IVAR_$_FCSmarterMessagingConfig._puzzleHubInfoBubbleTipBody
+ _OBJC_IVAR_$_FCSmarterMessagingConfig._puzzleHubInfoBubbleTipIconUrl
+ _OBJC_IVAR_$_FCSmarterMessagingConfig._puzzleHubInfoBubbleTipPresentationsQuiescenceInterval
+ _OBJC_IVAR_$_FCSmarterMessagingConfig._puzzleHubInfoBubbleTipTitle
+ _OBJC_METACLASS_$_FCAssertPreparedFeedPersonalizer
+ _OBJC_METACLASS_$_FCFeedItemScoreCache
+ _OBJC_METACLASS_$_FCNewsPersonalizationTrainingLegacyBridgeConfiguration
+ __FCFeedFilterOptionsAsStrings
+ __OBJC_$_INSTANCE_METHODS_FCAssertPreparedFeedPersonalizer
+ __OBJC_$_INSTANCE_METHODS_FCFeedItemScoreCache
+ __OBJC_$_INSTANCE_METHODS_FCNewsPersonalizationTrainingLegacyBridgeConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_FCAssertPreparedFeedPersonalizer
+ __OBJC_$_INSTANCE_VARIABLES_FCFeedItemScoreCache
+ __OBJC_$_INSTANCE_VARIABLES_FCNewsPersonalizationTrainingLegacyBridgeConfiguration
+ __OBJC_$_PROP_LIST_FCAssertPreparedFeedPersonalizer
+ __OBJC_$_PROP_LIST_FCFeedItemScoreCache
+ __OBJC_$_PROP_LIST_FCNewsPersonalizationTrainingLegacyBridgeConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_FCAssertPreparedFeedPersonalizer
+ __OBJC_CLASS_RO_$_FCAssertPreparedFeedPersonalizer
+ __OBJC_CLASS_RO_$_FCFeedItemScoreCache
+ __OBJC_CLASS_RO_$_FCNewsPersonalizationTrainingLegacyBridgeConfiguration
+ __OBJC_METACLASS_RO_$_FCAssertPreparedFeedPersonalizer
+ __OBJC_METACLASS_RO_$_FCFeedItemScoreCache
+ __OBJC_METACLASS_RO_$_FCNewsPersonalizationTrainingLegacyBridgeConfiguration
+ ___34-[FCESLInventory _adoptInventory:]_block_invoke
+ ___34-[FCESLInventory _refreshIfNeeded]_block_invoke.24
+ ___34-[FCESLInventory _refreshIfNeeded]_block_invoke.33
+ ___34-[FCESLInventory _refreshIfNeeded]_block_invoke.37
+ ___34-[FCESLInventory _refreshIfNeeded]_block_invoke_2.25
+ ___34-[FCESLInventory _refreshIfNeeded]_block_invoke_2.35
+ ___34-[FCESLInventory _refreshIfNeeded]_block_invoke_3.27
+ ___34-[FCESLInventory _refreshIfNeeded]_block_invoke_4.29
+ ___41-[FCESLInventory _loadInventoryFromCache]_block_invoke.47
+ ___41-[FCESLInventory _loadInventoryFromCache]_block_invoke.50
+ ___50-[FCESLInventory _promiseIssuesWithConfiguration:]_block_invoke.53
+ ___56-[FCMyArticlesOperation _constructFeedRequestsFromTags:]_block_invoke.29
+ ___58-[FCFeedItemScoreCache addScoreProfiles:configurationSet:]_block_invoke
+ ___60-[FCESLInventory _promiseFeedItemsWithIssues:configuration:]_block_invoke.57
+ ___62-[FCESLInventory _promiseEvergreenFeedItemsWithConfiguration:]_block_invoke.59
+ ___62-[FCESLInventory _rescoreInventoryIfNeeded:forScoringVersion:]_block_invoke
+ ___67-[FCFeedItemScoreCache scoreProfilesForFeedItems:configurationSet:]_block_invoke
+ ___67-[FCFeedItemScoreCache scoreProfilesForFeedItems:configurationSet:]_block_invoke_2
+ ___71-[FCAssertPreparedFeedPersonalizer prepareForUseWithCompletionHandler:]_block_invoke
+ ___74-[FCFeedItemScoreCache _accessScoreCacheForForConfigurationSet:withBlock:]_block_invoke
+ ___block_descriptor_56_e8_32s40s_e14_v16?0?<v?>8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r_e20_v16?0"FCMapTable"8ls32l8s40l8r48l8
+ ___block_literal_global.1263
+ ___block_literal_global.1265
+ ___block_literal_global.1267
+ ___block_literal_global.1275
+ ___block_literal_global.1286
+ ___block_literal_global.1291
+ ___block_literal_global.1296
+ ___block_literal_global.1301
+ ___block_literal_global.137
+ ___block_literal_global.139
+ ___block_literal_global.821
+ ___block_literal_global.850
+ _kFCFCNewsPersonalizationTrainingLegacyBridgeConfigurationAllowAllLegacyAggregatesToActAsPriorsKey
+ _kFCFCNewsPersonalizationTrainingLegacyBridgeConfigurationAvoidDoubleCountingWhenPrioringWithLegacyAggregatesKey
+ _kFCFCNewsPersonalizationTrainingLegacyBridgeConfigurationCreateStatelessAggregatesWhichOnlyExistInLegacyKey
+ _kFCFCNewsPersonalizationTrainingLegacyBridgeConfigurationDisablePrioringBaselineKey
+ _kFCFCNewsPersonalizationTrainingLegacyBridgeConfigurationLegacyDecayRateKey
+ _kFCFCNewsPersonalizationTrainingLegacyBridgeConfigurationLegacyMaxLinearImpressionCountKey
+ _kFCFCNewsPersonalizationTrainingLegacyBridgeConfigurationLegacyMultiplierKey
+ _kFCFCNewsPersonalizationTrainingLegacyBridgeConfigurationPriorStatelessAggregatesWithLegacyAggregatesKey
+ _kFCFCNewsPersonalizationTrainingLegacyBridgeConfigurationStatelessMaxLinearImpressionCountKey
+ _kFCNewsPersonalizationTrainingConfigurationDisableTrainingLegacyAggregates
+ _kFCNewsPersonalizationTrainingConfigurationFeatureFlagsKey
+ _kFCNewsPersonalizationTrainingConfigurationLegacyBridgeConfigurationKey
+ _objc_msgSend$_accessScoreCacheForForConfigurationSet:withBlock:
+ _objc_msgSend$_adoptInventory:
+ _objc_msgSend$_rescoreInventoryIfNeeded:forScoringVersion:
+ _objc_msgSend$addScoreProfiles:configurationSet:
+ _objc_msgSend$allFeedItemScoreProfilesForConfigurationSet:scoringVersion:
+ _objc_msgSend$allowAllLegacyAggregatesToActAsPriors
+ _objc_msgSend$avoidDoubleCountingWhenPrioringWithLegacyAggregates
+ _objc_msgSend$createStatelessAggregatesWhichOnlyExistInLegacy
+ _objc_msgSend$disablePrioringBaseline
+ _objc_msgSend$disableTrainingLegacyAggregates
+ _objc_msgSend$fc_NewsURLWithPathComponents:
+ _objc_msgSend$fetchAggregateMapForPersonalizingItem:completion:
+ _objc_msgSend$legacyBridgeConfiguration
+ _objc_msgSend$legacyDecayRate
+ _objc_msgSend$legacyMaxLinearImpressionCount
+ _objc_msgSend$legacyMultiplier
+ _objc_msgSend$priorStatelessAggregatesWithLegacyAggregates
+ _objc_msgSend$scoreProfilesByConfigurationSet
+ _objc_msgSend$scoringVersion
+ _objc_msgSend$setPreparedForUse:
+ _objc_msgSend$statelessMaxLinearImpressionCount
+ _objc_msgSend$target
+ _scoringAssetsIdentifierKey
- +[NSURL(FCAdditions) fc_NewsURLWithPathComponents:withScheme:]
- +[NSURL(FCAdditions) fc_secureNewsURLForArticleID:hardPaywall:]
- -[FCESLInventory allFeedItemScoreProfilesForConfigurationSet:]
- -[FCFeedPersonalizedItemScoreProfile setShadowAgedPersonalizationScore:]
- -[FCFeedPersonalizedItemScoreProfile setShadowTabiScore:]
- -[FCFeedPersonalizedItemScoreProfile shadowAgedPersonalizationScore]
- -[FCFeedPersonalizedItemScoreProfile shadowTabiScore]
- -[FCMyArticlesOperation _accessScoreCacheForForConfigurationSet:withBlock:]
- -[FCMyArticlesOperation scoreProfilesForConfigurationSet:]
- -[FCPersonalizationScoringConfig shouldOverrideTabiCoefficient]
- -[FCPersonalizationScoringConfig tabiCoefficientOverride]
- -[FCPuzzleHistory updatePuzzle:progressData:progressLevel:playDuration:isSolved:]
- _OBJC_IVAR_$_FCFeedPersonalizedItemScoreProfile._shadowAgedPersonalizationScore
- _OBJC_IVAR_$_FCFeedPersonalizedItemScoreProfile._shadowTabiScore
- ___34-[FCESLInventory _refreshIfNeeded]_block_invoke.23
- ___34-[FCESLInventory _refreshIfNeeded]_block_invoke.32
- ___34-[FCESLInventory _refreshIfNeeded]_block_invoke.34
- ___34-[FCESLInventory _refreshIfNeeded]_block_invoke.38
- ___34-[FCESLInventory _refreshIfNeeded]_block_invoke_2.24
- ___34-[FCESLInventory _refreshIfNeeded]_block_invoke_2.36
- ___34-[FCESLInventory _refreshIfNeeded]_block_invoke_3.26
- ___34-[FCESLInventory _refreshIfNeeded]_block_invoke_4.28
- ___41-[FCESLInventory _loadInventoryFromCache]_block_invoke.48
- ___41-[FCESLInventory _loadInventoryFromCache]_block_invoke.52
- ___50-[FCESLInventory _promiseIssuesWithConfiguration:]_block_invoke.54
- ___56-[FCMyArticlesOperation _constructFeedRequestsFromTags:]_block_invoke.41
- ___57-[FCPersonalizationScoringConfig tabiCoefficientOverride]_block_invoke
- ___58-[FCMyArticlesOperation scoreProfilesForConfigurationSet:]_block_invoke
- ___58-[FCMyArticlesOperation scoreProfilesForConfigurationSet:]_block_invoke.9
- ___58-[FCMyArticlesOperation scoreProfilesForConfigurationSet:]_block_invoke_2
- ___59-[FCMyArticlesOperation _prewarmScoreCacheFromESLInventory]_block_invoke
- ___59-[FCMyArticlesOperation _prewarmScoreCacheFromESLInventory]_block_invoke_2
- ___60-[FCESLInventory _promiseFeedItemsWithIssues:configuration:]_block_invoke.58
- ___62-[FCESLInventory _promiseEvergreenFeedItemsWithConfiguration:]_block_invoke.60
- ___63-[FCPersonalizationScoringConfig shouldOverrideTabiCoefficient]_block_invoke
- ___75-[FCMyArticlesOperation _accessScoreCacheForForConfigurationSet:withBlock:]_block_invoke
- ___block_descriptor_56_e8_32s40r_e20_v16?0"FCMapTable"8ls32l8r40l8
- ___block_literal_global.1249
- ___block_literal_global.1251
- ___block_literal_global.1253
- ___block_literal_global.1261
- ___block_literal_global.1272
- ___block_literal_global.1277
- ___block_literal_global.1282
- ___block_literal_global.1287
- ___block_literal_global.153
- ___block_literal_global.813
- ___block_literal_global.842
- _kFCNewsPersonalizationTrainingConfigurationFeatureFlags
- _objc_msgSend$allFeedItemScoreProfilesForConfigurationSet:
- _objc_msgSend$fc_NewsURLWithPathComponents:withScheme:
- _objc_msgSend$scoreFeedItems
- _objc_msgSend$shouldOverrideTabiCoefficient
- _objc_msgSend$tabiCoefficientOverride
- _objc_msgSend$whitespaceAndNewlineCharacterSet
CStrings:
+ "\x14\x11#"
+ "*** Assertion failure (Identifier: FeedPersonalizerPreparation) : %s %s:%d %{public}@"
+ "-[FCAssertPreparedFeedPersonalizer decayedPublisherDiversificationPenalty]"
+ "-[FCAssertPreparedFeedPersonalizer fetchAggregateMapForPersonalizingItem:completion:]"
+ "-[FCAssertPreparedFeedPersonalizer initWithTarget:]"
+ "-[FCAssertPreparedFeedPersonalizer init]"
+ "-[FCAssertPreparedFeedPersonalizer limitItemsByFlowRate:timeInterval:publisherCount:]"
+ "-[FCAssertPreparedFeedPersonalizer limitItemsByMinimumItemQuality:]"
+ "-[FCAssertPreparedFeedPersonalizer rankTagIDsDescending:]"
+ "-[FCAssertPreparedFeedPersonalizer scoresForTagIDs:]"
+ "-[FCAssertPreparedFeedPersonalizer sortItems:options:configurationSet:]"
+ "-[FCESLInventory allFeedItemScoreProfilesForConfigurationSet:scoringVersion:]"
+ "/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAssertPreparedFeedPersonalizer.m"
+ "; allowAllLegacyAggregatesToActAsPriors: %d"
+ "; avoidDoubleCountingWhenPrioringWithLegacyAggregates: %d"
+ "; createStatelessAggregatesWhichOnlyExistInLegacy: %d"
+ "; disablePrioringBaseline: %d"
+ "; disableTrainingLegacyAggregates: %d"
+ "; legacyBridgeConfiguration: %@"
+ "; legacyDecayRate: %f"
+ "; legacyMaxLinearImpressionCount: %lld"
+ "; legacyMultiplier: %f"
+ "; priorStatelessAggregatesWithLegacyAggregates: %d"
+ "; statelessMaxLinearImpressionCount: %lld"
+ "@\"FCMapTable\"32@0:8q16Q24"
+ "@\"FCNewsPersonalizationTrainingLegacyBridgeConfiguration\""
+ "@\"NTPBCoefficients\""
+ "@\"NTPBScoringCohort\""
+ "C\x83"
+ "Defaults specified tabi configuration didn't specify any packageAssetIDs, proceeding as if no override is in place"
+ "FCAssertPreparedFeedPersonalizer"
+ "FCFeedItemScoreCache"
+ "FCNewsPersonalizationTrainingLegacyBridgeConfiguration"
+ "Failed to decode tabi config into Dictionary, proceeding as if no override is in place %{public}@"
+ "Found DawnburstB tabi configuration"
+ "Found tabi config override enabled, specified as %{public}@"
+ "Loaded user defaults tabi configuration version %{public}@"
+ "Loading internal news personalization configuration"
+ "Loading news personalization configuration"
+ "See an internal user, and an internal tabi configuration, but configured to ignore it by %{public}@"
+ "T@\"<FCFeedPersonalizing>\",R,N,V_target"
+ "T@\"FCNewsPersonalizationTrainingLegacyBridgeConfiguration\",&,N,V_legacyBridgeConfiguration"
+ "T@\"FCThreadSafeMutableDictionary\",R,N,V_scoreProfilesByConfigurationSet"
+ "T@\"NSString\",&,N"
+ "T@\"NSString\",C,N,V_puzzleHubInfoBubbleTipBody"
+ "T@\"NSString\",C,N,V_puzzleHubInfoBubbleTipIconUrl"
+ "T@\"NSString\",C,N,V_puzzleHubInfoBubbleTipTitle"
+ "T@\"NTPBCoefficients\",&,N,V_coefficients"
+ "T@\"NTPBScoringCohort\",&,N,V_globalCohort"
+ "TB,N,GisPreparedForUse,V_preparedForUse"
+ "TB,N,V_allowAllLegacyAggregatesToActAsPriors"
+ "TB,N,V_avoidDoubleCountingWhenPrioringWithLegacyAggregates"
+ "TB,N,V_createStatelessAggregatesWhichOnlyExistInLegacy"
+ "TB,N,V_disablePrioringBaseline"
+ "TB,N,V_disableTrainingLegacyAggregates"
+ "TB,N,V_priorStatelessAggregatesWithLegacyAggregates"
+ "TQ,D,N"
+ "TQ,N,V_scoringVersion"
+ "Td,N,V_legacyDecayRate"
+ "Td,N,V_legacyMultiplier"
+ "Tf,D,N"
+ "Tq,N,V_legacyMaxLinearImpressionCount"
+ "Tq,N,V_statelessMaxLinearImpressionCount"
+ "Tq,R,N,V_maxPuzzleHubInfoBubbleTipPresentations"
+ "Tq,R,N,V_puzzleHubInfoBubbleTipPresentationsQuiescenceInterval"
+ "Using baseline tabi configuration"
+ "_accessScoreCacheForForConfigurationSet:withBlock:"
+ "_adoptInventory:"
+ "_allowAllLegacyAggregatesToActAsPriors"
+ "_avoidDoubleCountingWhenPrioringWithLegacyAggregates"
+ "_coefficients"
+ "_createStatelessAggregatesWhichOnlyExistInLegacy"
+ "_disablePrioringBaseline"
+ "_disableTrainingLegacyAggregates"
+ "_globalCohort"
+ "_legacyBridgeConfiguration"
+ "_legacyDecayRate"
+ "_legacyMaxLinearImpressionCount"
+ "_legacyMultiplier"
+ "_maxPuzzleHubInfoBubbleTipPresentations"
+ "_priorStatelessAggregatesWithLegacyAggregates"
+ "_puzzleHubInfoBubbleTipBody"
+ "_puzzleHubInfoBubbleTipIconUrl"
+ "_puzzleHubInfoBubbleTipPresentationsQuiescenceInterval"
+ "_puzzleHubInfoBubbleTipTitle"
+ "_rescoreInventoryIfNeeded:forScoringVersion:"
+ "_scoringVersion"
+ "_statelessMaxLinearImpressionCount"
+ "_target"
+ "addScoreProfiles:configurationSet:"
+ "allFeedItemScoreProfilesForConfigurationSet:scoringVersion:"
+ "allowAllLegacyAggregatesToActAsPriors"
+ "avoidDoubleCountingWhenPrioringWithLegacyAggregates"
+ "coefficients"
+ "createStatelessAggregatesWhichOnlyExistInLegacy"
+ "defaults"
+ "did not rescore inventory because it is no longer the latest"
+ "disablePrioringBaseline"
+ "disableTrainingLegacyAggregates"
+ "fc_NewsURLWithPathComponents:"
+ "globalCohort"
+ "ignoreInternalNewsTabiConfiguration"
+ "initWithFeedPersonalizer:"
+ "initWithTarget:"
+ "internalNewsPersonalizationConfiguration"
+ "legacyBridgeConfiguration"
+ "legacyDecayRate"
+ "legacyMaxLinearImpressionCount"
+ "legacyMultiplier"
+ "maxPuzzleHubInfoBubbleTipPresentations"
+ "need to prepare personalizer for use before calling"
+ "news.news_personalization.allow_all_legacy_aggregates_to_act_as_priors"
+ "news.news_personalization.avoid_double_counting_when_prioring_with_legacy_aggregates"
+ "news.news_personalization.create_stateless_aggregates_which_only_exist_in_legacy"
+ "news.news_personalization.disable_prioring_baseline"
+ "news.news_personalization.disable_training_legacy_aggregates"
+ "news.news_personalization.enable_training_configuration_override"
+ "news.news_personalization.legacy_decay_rate"
+ "news.news_personalization.legacy_max_linear_impression_count"
+ "news.news_personalization.legacy_multiplier"
+ "news.news_personalization.prior_stateless_aggregates_with_legacy_aggregates"
+ "news.news_personalization.should_override_legacy_bridging_configuration"
+ "news.news_personalization.stateless_max_linear_impression_count"
+ "news.news_personalization.tabi.allow_tabi_configuration_from_user_defaults"
+ "news.news_personalization.tabi.custom_tabi_configuration"
+ "news.news_personalization.tabi.ignore_internal_news_tabi_configuration"
+ "newsTabiConfigurationDawnburstB"
+ "not rescoring inventory due to no score profile"
+ "not rescoring inventory due to version match"
+ "preparedForUse"
+ "prewarmScoreCache:"
+ "priorStatelessAggregatesWithLegacyAggregates"
+ "puzzleHubInfoBubbleTipBody"
+ "puzzleHubInfoBubbleTipIconUrl"
+ "puzzleHubInfoBubbleTipPresentationsQuiescenceInterval"
+ "puzzleHubInfoBubbleTipTitle"
+ "rescored inventory"
+ "rescoring inventory because cached scored version of %llu doesn't match %llu"
+ "score cache has all %lu requested feed item scores, context=%{public}@"
+ "score cache is missing %lu of %lu requested feed item scores, context=%{public}@"
+ "score cache took %llums to score %lu feed items, context=%{public}@"
+ "scoreProfilesByConfigurationSet"
+ "scoreProfilesForFeedItems:configurationSet:"
+ "scoringAssetsIdentifier"
+ "scoringVersion"
+ "setAllowAllLegacyAggregatesToActAsPriors:"
+ "setAvoidDoubleCountingWhenPrioringWithLegacyAggregates:"
+ "setCoefficients:"
+ "setCreateStatelessAggregatesWhichOnlyExistInLegacy:"
+ "setDisablePrioringBaseline:"
+ "setDisableTrainingLegacyAggregates:"
+ "setGlobalCohort:"
+ "setLegacyBridgeConfiguration:"
+ "setLegacyDecayRate:"
+ "setLegacyMaxLinearImpressionCount:"
+ "setLegacyMultiplier:"
+ "setPreparedForUse:"
+ "setPriorStatelessAggregatesWithLegacyAggregates:"
+ "setPuzzleHubInfoBubbleTipBody:"
+ "setPuzzleHubInfoBubbleTipIconUrl:"
+ "setPuzzleHubInfoBubbleTipTitle:"
+ "setScoringAssetsIdentifier:"
+ "setScoringVersion:"
+ "setStatelessMaxLinearImpressionCount:"
+ "shouldShuffleReportedHeadlines"
+ "statelessMaxLinearImpressionCount"
+ "statelessPersonalizationAllowedForExtensions"
+ "target"
+ "updatePuzzle:puzzleTypeID:progressData:progressLevel:playDuration:isSolved:"
+ "v60@0:8@16@24@32q40q48B56"
- "\x14\x11$"
- "%{public}@ score cache has all %lu requested feed item scores, context=%{public}@"
- "%{public}@ score cache is missing %lu of %lu requested feed item scores, context=%{public}@"
- "%{public}@ took %llums to score %lu feed items, context=%{public}@"
- "+[NSURL(FCAdditions) fc_secureNewsURLForArticleID:hardPaywall:]"
- "-[FCESLInventory allFeedItemScoreProfilesForConfigurationSet:]"
- "-[FCMyArticlesOperation scoreProfilesForConfigurationSet:]_block_invoke"
- "20230531_fy_v2"
- "@\"FCMapTable\"24@0:8q16"
- "Tf,N,V_shadowAgedPersonalizationScore"
- "Tf,N,V_shadowTabiScore"
- "_shadowAgedPersonalizationScore"
- "_shadowTabiScore"
- "allFeedItemScoreProfilesForConfigurationSet:"
- "f16@0:8"
- "fc_NewsURLWithPathComponents:withScheme:"
- "fc_secureNewsURLForArticleID:hardPaywall:"
- "news.news_personalization.tabi.enable_custom_scoring_package"
- "news.personalization.custom_scoring_package_id"
- "news.personalization.custom_tabi_scoring_coefficient"
- "scoreProfilesForConfigurationSet:"
- "scoring isn't enabled on this operation"
- "setShadowAgedPersonalizationScore:"
- "setShadowTabiScore:"
- "shouldOverrideTabiCoefficient"
- "tabiCoefficientOverride"
- "updatePuzzle:progressData:progressLevel:playDuration:isSolved:"
- "v20@0:8f16"
- "v52@0:8@16@24q32q40B48"
- "whitespaceAndNewlineCharacterSet"
- "{\"version\":\"custom_tabi_scoring_root_version\",\"packageAssetIDs\":[\"20230525_en_us_channel_endpoints\",\"%@\"],\"mlComputeUnits\":3,\"channelPickerSuggestionsConfiguration\":{\"bundleInputOutputConfiguration\":{\"contextFeatureKey\":\"context_tokens\",\"generalChannelSuggestionsOutputName\":\"general_channel_recs\",\"generalChannelSuggestionsScoreOutputName\":\"general_channel_recs_scores\",\"newsPlusChannelSuggestionsOutputName\":\"bundle_channel_recs\",\"newsPlusChannelSuggestionsScoreOutputName\":\"bundle_channel_recs_scores\"},\"nonBundleInputOutputConfiguration\":{\"contextFeatureKey\":\"context_tokens\",\"generalChannelSuggestionsOutputName\":\"general_channel_recs\",\"generalChannelSuggestionsScoreOutputName\":\"general_channel_recs_scores\",\"newsPlusChannelSuggestionsOutputName\":\"bundle_channel_recs\",\"newsPlusChannelSuggestionsScoreOutputName\":\"bundle_channel_recs_scores\"}},\"eventAggregationConfiguration\":{\"maxTopicIds\":12,\"maxSessionEvents\":128,\"readEventsOnly\":true,\"titleEmbeddingDimension\":768,\"fullBodyEmbeddingDimension\":768,\"bundleOutputConfiguration\":{\"outputNames\":[\"user_encoding\"]},\"nonBundleOutputConfiguration\":{\"outputNames\":[\"user_encoding\"]},\"eventConditions\":{\"articleReadConditions\":{\"probability\":1.0}}},\"feedPersonalizationConfiguration\":{\"maxTopicIds\":12,\"titleEmbeddingDimension\":768,\"fullBodyEmbeddingDimension\":768,\"bundleOutputConfiguration\":{\"tagScoringOutputName\":\"dur_pred\",\"defaultHeadlineScoringOutputName\":\"dur_pred\",\"topicFeedHeadlineScoringOutputName\":\"dur_pred\",\"magazineFeedHeadlineScoringOutputName\":\"dur_pred\",\"magazineFeedIssuesHeadlineScoringOutputName\":\"dur_pred\",\"legacyAudioFeedHeadlineScoringOutputName\":\"dur_pred\",\"audioFeedHeadlineScoringOutputName\":\"dur_pred\",\"articleRecirculationPrimaryHeadlineScoringOutputName\":\"dur_pred\",\"articleRecirculationSecondaryHeadlineScoringOutputName\":\"dur_pred\",\"articleRecirculationTertiaryHeadlineScoringOutputName\":\"dur_pred\",\"articleRecirculationQuaternaryHeadlineScoringOutputName\":\"dur_pred\",\"bestOfBundleHeadlineScoringOutputName\":\"dur_pred\",\"forYouGroupHeadlineScoringOutputName\":\"dur_pred\",\"greatStoriesYouMissedGroupHeadlineScoringOutputName\":\"dur_pred\",\"latestStoriesGroupHeadlineScoringOutputName\":\"dur_pred\",\"localNewsGroupHeadlineScoringOutputName\":\"dur_pred\",\"newspaperGroupMagazineFeedHeadlineScoringOutputName\":\"dur_pred\",\"todayWidgetHeadlineScoringOutputName\":\"dur_pred\",\"tagWidgetHeadlineScoringOutputName\":\"dur_pred\",\"notificationHeadlineScoringOutputName\":\"dur_pred\",\"mySportsGroupHeadlineScoringOutputName\":\"dur_pred\",\"sportsTopStoriesHeadlineScoringOutputName\":\"dur_pred\",\"introToSportsGroupHeadlineScoringOutputName\":\"dur_pred\",\"highlightsGroupHeadlineScoringOutputName\":\"dur_pred\",\"articleListTagFeedGroupHeadlineScoringOutputName\":\"dur_pred\",\"tagFeedHeadlineScoringOutputName\":\"dur_pred\",\"newspaperGroupTodayFeedHeadlineScoringOutputName\":\"dur_pred\",\"moreForYouGroupHeadlineScoringOutputName\":\"dur_pred\",\"introToSportsGroupForYouHeadlineScoringOutputName\":\"dur_pred\",\"mySportsGroupForYouHeadlineScoringOutputName\":\"dur_pred\",\"mySportsTopicsHeadlineScoringOutputName\":\"dur_pred\",\"curatedGroupHeadlineScoringOutputName\":\"dur_pred\",\"curatedGroupIssuesHeadlineScoringOutputName\":\"dur_pred\",\"localSectionGroupHeadlineScoringOutputName\":\"dur_pred\",\"newspaperSectionGroupHeadlineScoringOutputName\":\"dur_pred\",\"sportsEventArticlesGroupHeadlineScoringOutputName\":\"dur_pred\",\"tagFeedForYouGroupHeadlineScoringOutputName\":\"dur_pred\",\"tagRecentStoriesGroupHeadlineScoringOutputName\":\"dur_pred\",\"tagDateRangeGroupHeadlineScoringOutputName\":\"dur_pred\",\"sportsEventTopicGroupHeadlineScoringOutputName\":\"dur_pred\"},\"nonBundleOutputConfiguration\":{\"tagScoringOutputName\":\"dur_pred\",\"defaultHeadlineScoringOutputName\":\"dur_pred\",\"topicFeedHeadlineScoringOutputName\":\"dur_pred\",\"magazineFeedHeadlineScoringOutputName\":\"dur_pred\",\"magazineFeedIssuesHeadlineScoringOutputName\":\"dur_pred\",\"legacyAudioFeedHeadlineScoringOutputName\":\"dur_pred\",\"audioFeedHeadlineScoringOutputName\":\"dur_pred\",\"articleRecirculationPrimaryHeadlineScoringOutputName\":\"dur_pred\",\"articleRecirculationSecondaryHeadlineScoringOutputName\":\"dur_pred\",\"articleRecirculationTertiaryHeadlineScoringOutputName\":\"dur_pred\",\"articleRecirculationQuaternaryHeadlineScoringOutputName\":\"dur_pred\",\"bestOfBundleHeadlineScoringOutputName\":\"dur_pred\",\"forYouGroupHeadlineScoringOutputName\":\"dur_pred\",\"greatStoriesYouMissedGroupHeadlineScoringOutputName\":\"dur_pred\",\"latestStoriesGroupHeadlineScoringOutputName\":\"dur_pred\",\"localNewsGroupHeadlineScoringOutputName\":\"dur_pred\",\"newspaperGroupMagazineFeedHeadlineScoringOutputName\":\"dur_pred\",\"todayWidgetHeadlineScoringOutputName\":\"dur_pred\",\"tagWidgetHeadlineScoringOutputName\":\"dur_pred\",\"notificationHeadlineScoringOutputName\":\"dur_pred\",\"mySportsGroupHeadlineScoringOutputName\":\"dur_pred\",\"sportsTopStoriesHeadlineScoringOutputName\":\"dur_pred\",\"introToSportsGroupHeadlineScoringOutputName\":\"dur_pred\",\"highlightsGroupHeadlineScoringOutputName\":\"dur_pred\",\"articleListTagFeedGroupHeadlineScoringOutputName\":\"dur_pred\",\"tagFeedHeadlineScoringOutputName\":\"dur_pred\",\"newspaperGroupTodayFeedHeadlineScoringOutputName\":\"dur_pred\",\"moreForYouGroupHeadlineScoringOutputName\":\"dur_pred\",\"introToSportsGroupForYouHeadlineScoringOutputName\":\"dur_pred\",\"mySportsGroupForYouHeadlineScoringOutputName\":\"dur_pred\",\"mySportsTopicsHeadlineScoringOutputName\":\"dur_pred\",\"curatedGroupHeadlineScoringOutputName\":\"dur_pred\",\"curatedGroupIssuesHeadlineScoringOutputName\":\"dur_pred\",\"localSectionGroupHeadlineScoringOutputName\":\"dur_pred\",\"newspaperSectionGroupHeadlineScoringOutputName\":\"dur_pred\",\"sportsEventArticlesGroupHeadlineScoringOutputName\":\"dur_pred\",\"tagFeedForYouGroupHeadlineScoringOutputName\":\"dur_pred\",\"tagRecentStoriesGroupHeadlineScoringOutputName\":\"dur_pred\",\"tagDateRangeGroupHeadlineScoringOutputName\":\"dur_pred\",\"sportsEventTopicGroupHeadlineScoringOutputName\":\"dur_pred\"}},\"personalizedPaywallsConfiguration\":{\"contextFeatureKey\":\"context_tokens\",\"channelIDsOutputName\":\"paywall_recs\",\"scoresOutputName\":\"paywall_recs_scores\"}}"

```
