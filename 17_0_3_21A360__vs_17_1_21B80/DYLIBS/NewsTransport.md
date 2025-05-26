## NewsTransport

> `/System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport`

```diff

-3422.4.0.0.0
-  __TEXT.__text: 0x21f7d0
+3529.2.0.0.0
+  __TEXT.__text: 0x221ff0
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_methlist: 0x321a0
+  __TEXT.__objc_methlist: 0x32588
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x10f3f
-  __TEXT.__unwind_info: 0x46dc
-  __TEXT.__objc_classname: 0x216e
-  __TEXT.__objc_methname: 0x4f7f2
-  __TEXT.__objc_methtype: 0xc00e
-  __TEXT.__objc_stubs: 0x7f80
+  __TEXT.__cstring: 0x11084
+  __TEXT.__unwind_info: 0x472c
+  __TEXT.__objc_classname: 0x2191
+  __TEXT.__objc_methname: 0x50032
+  __TEXT.__objc_methtype: 0xc186
+  __TEXT.__objc_stubs: 0x7fe0
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x7148
-  __DATA_CONST.__objc_classlist: 0x9c0
+  __DATA_CONST.__objc_classlist: 0x9d0
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3e4a8
-  __DATA_CONST.__objc_selrefs: 0xfde8
-  __AUTH_CONST.__cfstring: 0x14580
-  __AUTH_CONST.__objc_const: 0x7980
+  __DATA_CONST.__objc_const: 0x3ea08
+  __DATA_CONST.__objc_selrefs: 0xff70
+  __AUTH_CONST.__cfstring: 0x14720
+  __AUTH_CONST.__objc_const: 0x7a10
   __AUTH_CONST.__auth_got: 0x248
-  __AUTH.__objc_data: 0x3908
-  __DATA.__objc_classrefs: 0x7c8
-  __DATA.__objc_superrefs: 0x9c0
-  __DATA.__objc_ivar: 0x3a88
+  __AUTH.__objc_data: 0x39a8
+  __DATA.__objc_classrefs: 0x7d8
+  __DATA.__objc_superrefs: 0x9d0
+  __DATA.__objc_ivar: 0x3ad4
   __DATA.__data: 0x60
   __DATA_DIRTY.__objc_data: 0x2878
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 17220
-  Symbols:   41260
-  CStrings:  15655
+  Functions: 17306
+  Symbols:   41464
+  CStrings:  15749
 
Symbols:
+ -[NTPBCoefficients articleEmbeddingScoreCoefficient]
+ -[NTPBCoefficients autofavoritedScoreCoefficient]
+ -[NTPBCoefficients clientScoreCoefficient]
+ -[NTPBCoefficients copyWithZone:]
+ -[NTPBCoefficients description]
+ -[NTPBCoefficients dictionaryRepresentation]
+ -[NTPBCoefficients hasArticleEmbeddingScoreCoefficient]
+ -[NTPBCoefficients hasAutofavoritedScoreCoefficient]
+ -[NTPBCoefficients hasClientScoreCoefficient]
+ -[NTPBCoefficients hasServerScoreCoefficient]
+ -[NTPBCoefficients hasSubscribedChannelScoreCoefficent]
+ -[NTPBCoefficients hasSubscribedTopicScoreCoefficient]
+ -[NTPBCoefficients hasTabiScoreCoefficient]
+ -[NTPBCoefficients hash]
+ -[NTPBCoefficients isEqual:]
+ -[NTPBCoefficients mergeFrom:]
+ -[NTPBCoefficients readFrom:]
+ -[NTPBCoefficients serverScoreCoefficient]
+ -[NTPBCoefficients setArticleEmbeddingScoreCoefficient:]
+ -[NTPBCoefficients setAutofavoritedScoreCoefficient:]
+ -[NTPBCoefficients setClientScoreCoefficient:]
+ -[NTPBCoefficients setHasArticleEmbeddingScoreCoefficient:]
+ -[NTPBCoefficients setHasAutofavoritedScoreCoefficient:]
+ -[NTPBCoefficients setHasClientScoreCoefficient:]
+ -[NTPBCoefficients setHasServerScoreCoefficient:]
+ -[NTPBCoefficients setHasSubscribedChannelScoreCoefficent:]
+ -[NTPBCoefficients setHasSubscribedTopicScoreCoefficient:]
+ -[NTPBCoefficients setHasTabiScoreCoefficient:]
+ -[NTPBCoefficients setServerScoreCoefficient:]
+ -[NTPBCoefficients setSubscribedChannelScoreCoefficent:]
+ -[NTPBCoefficients setSubscribedTopicScoreCoefficient:]
+ -[NTPBCoefficients setTabiScoreCoefficient:]
+ -[NTPBCoefficients subscribedChannelScoreCoefficent]
+ -[NTPBCoefficients subscribedTopicScoreCoefficient]
+ -[NTPBCoefficients tabiScoreCoefficient]
+ -[NTPBCoefficients writeTo:]
+ -[NTPBScoreProfile coefficients]
+ -[NTPBScoreProfile globalCohort]
+ -[NTPBScoreProfile hasCoefficients]
+ -[NTPBScoreProfile hasGlobalCohort]
+ -[NTPBScoreProfile hasScoringVersion]
+ -[NTPBScoreProfile hasShadowAgedPersonalizationScore]
+ -[NTPBScoreProfile hasShadowTabiScore]
+ -[NTPBScoreProfile scoringVersion]
+ -[NTPBScoreProfile setCoefficients:]
+ -[NTPBScoreProfile setGlobalCohort:]
+ -[NTPBScoreProfile setHasScoringVersion:]
+ -[NTPBScoreProfile setHasShadowAgedPersonalizationScore:]
+ -[NTPBScoreProfile setHasShadowTabiScore:]
+ -[NTPBScoreProfile setScoringVersion:]
+ -[NTPBScoreProfile setShadowAgedPersonalizationScore:]
+ -[NTPBScoreProfile setShadowTabiScore:]
+ -[NTPBScoreProfile shadowAgedPersonalizationScore]
+ -[NTPBScoreProfile shadowTabiScore]
+ -[NTPBScoreProfileDebug dealloc]
+ -[NTPBScoreProfileDebug hasScoringAssetsIdentifier]
+ -[NTPBScoreProfileDebug scoringAssetsIdentifier]
+ -[NTPBScoreProfileDebug setScoringAssetsIdentifier:]
+ -[NTPBScoringCohort clicks]
+ -[NTPBScoringCohort copyWithZone:]
+ -[NTPBScoringCohort dealloc]
+ -[NTPBScoringCohort description]
+ -[NTPBScoringCohort dictionaryRepresentation]
+ -[NTPBScoringCohort hasClicks]
+ -[NTPBScoringCohort hasIdentifier]
+ -[NTPBScoringCohort hasImpressions]
+ -[NTPBScoringCohort hasRawClicks]
+ -[NTPBScoringCohort hash]
+ -[NTPBScoringCohort identifier]
+ -[NTPBScoringCohort impressions]
+ -[NTPBScoringCohort isEqual:]
+ -[NTPBScoringCohort mergeFrom:]
+ -[NTPBScoringCohort rawClicks]
+ -[NTPBScoringCohort readFrom:]
+ -[NTPBScoringCohort setClicks:]
+ -[NTPBScoringCohort setHasClicks:]
+ -[NTPBScoringCohort setHasImpressions:]
+ -[NTPBScoringCohort setHasRawClicks:]
+ -[NTPBScoringCohort setIdentifier:]
+ -[NTPBScoringCohort setImpressions:]
+ -[NTPBScoringCohort setRawClicks:]
+ -[NTPBScoringCohort writeTo:]
+ OBJC_IVAR_$_NTPBCoefficients._articleEmbeddingScoreCoefficient
+ OBJC_IVAR_$_NTPBCoefficients._autofavoritedScoreCoefficient
+ OBJC_IVAR_$_NTPBCoefficients._clientScoreCoefficient
+ OBJC_IVAR_$_NTPBCoefficients._has
+ OBJC_IVAR_$_NTPBCoefficients._serverScoreCoefficient
+ OBJC_IVAR_$_NTPBCoefficients._subscribedChannelScoreCoefficent
+ OBJC_IVAR_$_NTPBCoefficients._subscribedTopicScoreCoefficient
+ OBJC_IVAR_$_NTPBCoefficients._tabiScoreCoefficient
+ OBJC_IVAR_$_NTPBScoreProfile._coefficients
+ OBJC_IVAR_$_NTPBScoreProfile._globalCohort
+ OBJC_IVAR_$_NTPBScoreProfile._scoringVersion
+ OBJC_IVAR_$_NTPBScoreProfile._shadowAgedPersonalizationScore
+ OBJC_IVAR_$_NTPBScoreProfile._shadowTabiScore
+ OBJC_IVAR_$_NTPBScoreProfileDebug._scoringAssetsIdentifier
+ OBJC_IVAR_$_NTPBScoringCohort._clicks
+ OBJC_IVAR_$_NTPBScoringCohort._has
+ OBJC_IVAR_$_NTPBScoringCohort._identifier
+ OBJC_IVAR_$_NTPBScoringCohort._impressions
+ OBJC_IVAR_$_NTPBScoringCohort._rawClicks
+ _NTPBCoefficientsReadFrom
+ _NTPBScoringCohortReadFrom
+ _OBJC_CLASS_$_NTPBCoefficients
+ _OBJC_CLASS_$_NTPBScoringCohort
+ _OBJC_METACLASS_$_NTPBCoefficients
+ _OBJC_METACLASS_$_NTPBScoringCohort
+ __OBJC_$_INSTANCE_METHODS_NTPBCoefficients
+ __OBJC_$_INSTANCE_METHODS_NTPBScoringCohort
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCoefficients
+ __OBJC_$_INSTANCE_VARIABLES_NTPBScoringCohort
+ __OBJC_$_PROP_LIST_NTPBCoefficients
+ __OBJC_$_PROP_LIST_NTPBScoringCohort
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCoefficients
+ __OBJC_CLASS_PROTOCOLS_$_NTPBScoringCohort
+ __OBJC_CLASS_RO_$_NTPBCoefficients
+ __OBJC_CLASS_RO_$_NTPBScoringCohort
+ __OBJC_METACLASS_RO_$_NTPBCoefficients
+ __OBJC_METACLASS_RO_$_NTPBScoringCohort
+ _objc_msgSend$setCoefficients:
+ _objc_msgSend$setGlobalCohort:
+ _objc_msgSend$setScoringAssetsIdentifier:
CStrings:
+ "@\"NTPBCoefficients\""
+ "@\"NTPBScoringCohort\""
+ "NTPBCoefficients"
+ "NTPBScoringCohort"
+ "T@\"NSString\",&,N,V_scoringAssetsIdentifier"
+ "T@\"NTPBCoefficients\",&,N,V_coefficients"
+ "T@\"NTPBScoringCohort\",&,N,V_globalCohort"
+ "TQ,N,V_scoringVersion"
+ "Td,N,V_articleEmbeddingScoreCoefficient"
+ "Td,N,V_autofavoritedScoreCoefficient"
+ "Td,N,V_clientScoreCoefficient"
+ "Td,N,V_serverScoreCoefficient"
+ "Td,N,V_shadowAgedPersonalizationScore"
+ "Td,N,V_shadowTabiScore"
+ "Td,N,V_subscribedChannelScoreCoefficent"
+ "Td,N,V_subscribedTopicScoreCoefficient"
+ "Td,N,V_tabiScoreCoefficient"
+ "_articleEmbeddingScoreCoefficient"
+ "_autofavoritedScoreCoefficient"
+ "_clientScoreCoefficient"
+ "_coefficients"
+ "_globalCohort"
+ "_scoringAssetsIdentifier"
+ "_scoringVersion"
+ "_serverScoreCoefficient"
+ "_shadowAgedPersonalizationScore"
+ "_shadowTabiScore"
+ "_subscribedChannelScoreCoefficent"
+ "_subscribedTopicScoreCoefficient"
+ "_tabiScoreCoefficient"
+ "articleEmbeddingScoreCoefficient"
+ "article_embedding_score_coefficient"
+ "autofavoritedScoreCoefficient"
+ "autofavorited_score_coefficient"
+ "clientScoreCoefficient"
+ "client_score_coefficient"
+ "coefficients"
+ "globalCohort"
+ "hasArticleEmbeddingScoreCoefficient"
+ "hasAutofavoritedScoreCoefficient"
+ "hasClientScoreCoefficient"
+ "hasCoefficients"
+ "hasGlobalCohort"
+ "hasScoringAssetsIdentifier"
+ "hasScoringVersion"
+ "hasServerScoreCoefficient"
+ "hasShadowAgedPersonalizationScore"
+ "hasShadowTabiScore"
+ "hasSubscribedChannelScoreCoefficent"
+ "hasSubscribedTopicScoreCoefficient"
+ "hasTabiScoreCoefficient"
+ "scoringAssetsIdentifier"
+ "scoringVersion"
+ "scoring_version"
+ "serverScoreCoefficient"
+ "server_score_coefficient"
+ "setArticleEmbeddingScoreCoefficient:"
+ "setAutofavoritedScoreCoefficient:"
+ "setClientScoreCoefficient:"
+ "setCoefficients:"
+ "setGlobalCohort:"
+ "setHasArticleEmbeddingScoreCoefficient:"
+ "setHasAutofavoritedScoreCoefficient:"
+ "setHasClientScoreCoefficient:"
+ "setHasScoringVersion:"
+ "setHasServerScoreCoefficient:"
+ "setHasShadowAgedPersonalizationScore:"
+ "setHasShadowTabiScore:"
+ "setHasSubscribedChannelScoreCoefficent:"
+ "setHasSubscribedTopicScoreCoefficient:"
+ "setHasTabiScoreCoefficient:"
+ "setScoringAssetsIdentifier:"
+ "setScoringVersion:"
+ "setServerScoreCoefficient:"
+ "setShadowAgedPersonalizationScore:"
+ "setShadowTabiScore:"
+ "setSubscribedChannelScoreCoefficent:"
+ "setSubscribedTopicScoreCoefficient:"
+ "setTabiScoreCoefficient:"
+ "shadowAgedPersonalizationScore"
+ "shadowTabiScore"
+ "subscribedChannelScoreCoefficent"
+ "subscribedTopicScoreCoefficient"
+ "subscribed_channel_score_coefficent"
+ "subscribed_topic_score_coefficient"
+ "tabiScoreCoefficient"
+ "tabi_score_coefficient"
+ "{?=\"agedPersonalizationScore\"b1\"autoSubscribeCtr\"b1\"computedGlobalScoreCoefficient\"b1\"conversionMultiplier\"b1\"dampenedStaticMultiplier\"b1\"embeddingScore\"b1\"featureCtr\"b1\"paidNonpaidSubscriptionCtr\"b1\"personalizationScore\"b1\"publisherDampener\"b1\"publisherFavorability\"b1\"qualitativeMultiplier\"b1\"rawPersonalizationScore\"b1\"rawUserFeedbackScore\"b1\"scoringVersion\"b1\"shadowAgedPersonalizationScore\"b1\"shadowTabiScore\"b1\"staticMultiplier\"b1\"subscribedChannelCtr\"b1\"tabiScore\"b1\"userFeedbackScore\"b1\"isEvergreen\"b1}"
+ "{?=\"articleEmbeddingScoreCoefficient\"b1\"autofavoritedScoreCoefficient\"b1\"clientScoreCoefficient\"b1\"serverScoreCoefficient\"b1\"subscribedChannelScoreCoefficent\"b1\"subscribedTopicScoreCoefficient\"b1\"tabiScoreCoefficient\"b1}"
+ "{?=\"clicks\"b1\"impressions\"b1\"rawClicks\"b1}"
- "{?=\"agedPersonalizationScore\"b1\"autoSubscribeCtr\"b1\"computedGlobalScoreCoefficient\"b1\"conversionMultiplier\"b1\"dampenedStaticMultiplier\"b1\"embeddingScore\"b1\"featureCtr\"b1\"paidNonpaidSubscriptionCtr\"b1\"personalizationScore\"b1\"publisherDampener\"b1\"publisherFavorability\"b1\"qualitativeMultiplier\"b1\"rawPersonalizationScore\"b1\"rawUserFeedbackScore\"b1\"staticMultiplier\"b1\"subscribedChannelCtr\"b1\"tabiScore\"b1\"userFeedbackScore\"b1\"isEvergreen\"b1}"

```
