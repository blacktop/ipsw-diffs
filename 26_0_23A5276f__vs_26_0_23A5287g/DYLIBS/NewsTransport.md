## NewsTransport

> `/System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport`

```diff

-5722.0.0.0.0
-  __TEXT.__text: 0x279068
+5726.2.0.0.0
+  __TEXT.__text: 0x278da8
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x37684
+  __TEXT.__objc_methlist: 0x37654
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x11d38
-  __TEXT.__unwind_info: 0x4f30
+  __TEXT.__cstring: 0x11d1d
+  __TEXT.__unwind_info: 0x4fc0
   __TEXT.__objc_classname: 0x26a7
-  __TEXT.__objc_methname: 0x5583a
-  __TEXT.__objc_methtype: 0xcbe2
+  __TEXT.__objc_methname: 0x55788
+  __TEXT.__objc_methtype: 0xcbc5
   __TEXT.__objc_stubs: 0x91c0
   __DATA_CONST.__got: 0x940
   __DATA_CONST.__const: 0x72c8
   __DATA_CONST.__objc_classlist: 0xb88
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11518
+  __DATA_CONST.__objc_selrefs: 0x114f8
   __DATA_CONST.__objc_superrefs: 0xb88
   __AUTH_CONST.__auth_got: 0x238
-  __AUTH_CONST.__cfstring: 0x16000
-  __AUTH_CONST.__objc_const: 0x4d8b0
+  __AUTH_CONST.__cfstring: 0x15fe0
+  __AUTH_CONST.__objc_const: 0x4d870
   __AUTH.__objc_data: 0x910
-  __DATA.__objc_ivar: 0x400c
+  __DATA.__objc_ivar: 0x4008
   __DATA.__data: 0x60
   __DATA_DIRTY.__objc_data: 0x6a40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1B6A0466-4153-38BF-B0E1-0A2D1DBF16A9
-  Functions: 18916
-  Symbols:   45770
-  CStrings:  19868
+  UUID: 7BD282CD-4ADD-3017-9F41-08FC43BF9746
+  Functions: 18912
+  Symbols:   45761
+  CStrings:  19860
 
Symbols:
+ -[NTPBForYouTodaySectionSpecificConfig hasSubscriptionsMinCount]
+ -[NTPBForYouTodaySectionSpecificConfig setHasSubscriptionsMinCount:]
+ -[NTPBForYouTodaySectionSpecificConfig setSubscriptionsMinCount:]
+ -[NTPBForYouTodaySectionSpecificConfig subscriptionsMinCount]
+ OBJC_IVAR_$_NTPBForYouTodaySectionSpecificConfig._subscriptionsMinCount
- -[NTPBCoefficients articleEmbeddingScoreCoefficient]
- -[NTPBCoefficients hasArticleEmbeddingScoreCoefficient]
- -[NTPBCoefficients setArticleEmbeddingScoreCoefficient:]
- -[NTPBCoefficients setHasArticleEmbeddingScoreCoefficient:]
- -[NTPBScoreProfile embeddingScore]
- -[NTPBScoreProfile hasEmbeddingScore]
- -[NTPBScoreProfile setEmbeddingScore:]
- -[NTPBScoreProfile setHasEmbeddingScore:]
- OBJC_IVAR_$_NTPBCoefficients._articleEmbeddingScoreCoefficient
- OBJC_IVAR_$_NTPBScoreProfile._embeddingScore
CStrings:
+ "TQ,N,V_subscriptionsMinCount"
+ "_subscriptionsMinCount"
+ "hasSubscriptionsMinCount"
+ "setHasSubscriptionsMinCount:"
+ "setSubscriptionsMinCount:"
+ "subscriptionsMinCount"
+ "subscriptions_min_count"
+ "{?=\"agedPersonalizationScore\"b1\"autoSubscribeCtr\"b1\"computedGlobalScoreCoefficient\"b1\"contentTriggerDampener\"b1\"conversionMultiplier\"b1\"dampenedStaticMultiplier\"b1\"democratizationFactor\"b1\"multiplier\"b1\"nicheContentMultiplier\"b1\"paidNonpaidSubscriptionCtr\"b1\"personalizationScore\"b1\"publisherDampener\"b1\"publisherFavorability\"b1\"qualitativeMultiplier\"b1\"rawPersonalizationScore\"b1\"rawUserFeedbackScore\"b1\"scoringVersion\"b1\"serverScoreDemocratizationFactor\"b1\"shadowAgedPersonalizationScore\"b1\"shadowTabiScore\"b1\"staticMultiplier\"b1\"subscribedChannelCtr\"b1\"tabiScore\"b1\"userFeedbackScore\"b1\"isCoread\"b1\"isEvergreen\"b1}"
+ "{?=\"autofavoritedScoreCoefficient\"b1\"clientScoreCoefficient\"b1\"conversionCoefficient\"b1\"halfLifeCoefficient\"b1\"serverScoreCoefficient\"b1\"subscribedChannelScoreCoefficent\"b1\"subscribedTopicScoreCoefficient\"b1\"tabiScoreCoefficient\"b1}"
+ "{?=\"cutoffTime\"b1\"feedItemMaxCount\"b1\"feedMaxCount\"b1\"headlinesPerFeedFetchCount\"b1\"localNewsPromotionIndex\"b1\"minimumUpdateInterval\"b1\"subscriptionsFetchCount\"b1\"subscriptionsMinCount\"b1\"fetchingBin\"b1}"
- "Td,N,V_articleEmbeddingScoreCoefficient"
- "Td,N,V_embeddingScore"
- "_articleEmbeddingScoreCoefficient"
- "_embeddingScore"
- "articleEmbeddingScoreCoefficient"
- "article_embedding_score_coefficient"
- "embeddingScore"
- "hasArticleEmbeddingScoreCoefficient"
- "hasEmbeddingScore"
- "setArticleEmbeddingScoreCoefficient:"
- "setEmbeddingScore:"
- "setHasArticleEmbeddingScoreCoefficient:"
- "setHasEmbeddingScore:"
- "{?=\"agedPersonalizationScore\"b1\"autoSubscribeCtr\"b1\"computedGlobalScoreCoefficient\"b1\"contentTriggerDampener\"b1\"conversionMultiplier\"b1\"dampenedStaticMultiplier\"b1\"democratizationFactor\"b1\"embeddingScore\"b1\"multiplier\"b1\"nicheContentMultiplier\"b1\"paidNonpaidSubscriptionCtr\"b1\"personalizationScore\"b1\"publisherDampener\"b1\"publisherFavorability\"b1\"qualitativeMultiplier\"b1\"rawPersonalizationScore\"b1\"rawUserFeedbackScore\"b1\"scoringVersion\"b1\"serverScoreDemocratizationFactor\"b1\"shadowAgedPersonalizationScore\"b1\"shadowTabiScore\"b1\"staticMultiplier\"b1\"subscribedChannelCtr\"b1\"tabiScore\"b1\"userFeedbackScore\"b1\"isCoread\"b1\"isEvergreen\"b1}"
- "{?=\"articleEmbeddingScoreCoefficient\"b1\"autofavoritedScoreCoefficient\"b1\"clientScoreCoefficient\"b1\"conversionCoefficient\"b1\"halfLifeCoefficient\"b1\"serverScoreCoefficient\"b1\"subscribedChannelScoreCoefficent\"b1\"subscribedTopicScoreCoefficient\"b1\"tabiScoreCoefficient\"b1}"
- "{?=\"cutoffTime\"b1\"feedItemMaxCount\"b1\"feedMaxCount\"b1\"headlinesPerFeedFetchCount\"b1\"localNewsPromotionIndex\"b1\"minimumUpdateInterval\"b1\"subscriptionsFetchCount\"b1\"fetchingBin\"b1}"

```
