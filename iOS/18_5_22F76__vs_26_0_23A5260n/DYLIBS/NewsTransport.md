## NewsTransport

> `/System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport`

```diff

-5681.0.0.0.0
-  __TEXT.__text: 0x24f108
+5718.1.0.0.0
+  __TEXT.__text: 0x279068
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x37594
+  __TEXT.__objc_methlist: 0x37684
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x11cec
-  __TEXT.__unwind_info: 0x4ed0
-  __TEXT.__objc_classname: 0x2698
-  __TEXT.__objc_methname: 0x5569a
-  __TEXT.__objc_methtype: 0xcb83
-  __TEXT.__objc_stubs: 0x90a0
-  __DATA_CONST.__got: 0x958
+  __TEXT.__cstring: 0x11d38
+  __TEXT.__unwind_info: 0x4f30
+  __TEXT.__objc_classname: 0x26a7
+  __TEXT.__objc_methname: 0x5583a
+  __TEXT.__objc_methtype: 0xcbe2
+  __TEXT.__objc_stubs: 0x91c0
+  __DATA_CONST.__got: 0x940
   __DATA_CONST.__const: 0x72c8
-  __DATA_CONST.__objc_classlist: 0xb80
+  __DATA_CONST.__objc_classlist: 0xb88
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x114a8
-  __DATA_CONST.__objc_superrefs: 0xb80
+  __DATA_CONST.__objc_selrefs: 0x11518
+  __DATA_CONST.__objc_superrefs: 0xb88
   __AUTH_CONST.__auth_got: 0x238
-  __AUTH_CONST.__cfstring: 0x15fa0
-  __AUTH_CONST.__objc_const: 0x4d6e8
-  __AUTH.__objc_data: 0x9b0
-  __DATA.__objc_ivar: 0x3ffc
+  __AUTH_CONST.__cfstring: 0x16000
+  __AUTH_CONST.__objc_const: 0x4d8b0
+  __AUTH.__objc_data: 0x910
+  __DATA.__objc_ivar: 0x400c
   __DATA.__data: 0x60
-  __DATA_DIRTY.__objc_data: 0x6950
+  __DATA_DIRTY.__objc_data: 0x6a40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A85FCAD5-BB50-3E81-A14B-0D385EEABAA7
-  Functions: 18896
-  Symbols:   45714
-  CStrings:  19840
+  UUID: ABBA0A8B-CDCC-3F95-BD24-3D9FC6C4C66C
+  Functions: 18916
+  Symbols:   45770
+  CStrings:  19868
 
Symbols:
+ -[NTPBFeedItem backendArticleVersion]
+ -[NTPBFeedItem hasBackendArticleVersion]
+ -[NTPBFeedItem hasLastModifiedDateMilliseconds]
+ -[NTPBFeedItem lastModifiedDateMilliseconds]
+ -[NTPBFeedItem setBackendArticleVersion:]
+ -[NTPBFeedItem setHasBackendArticleVersion:]
+ -[NTPBFeedItem setHasLastModifiedDateMilliseconds:]
+ -[NTPBFeedItem setLastModifiedDateMilliseconds:]
+ -[NTPBFeedPersonalizingItem hasLastModifiedDateMilliseconds]
+ -[NTPBFeedPersonalizingItem lastModifiedDateMilliseconds]
+ -[NTPBFeedPersonalizingItem setHasLastModifiedDateMilliseconds:]
+ -[NTPBFeedPersonalizingItem setLastModifiedDateMilliseconds:]
+ -[NTPBRecipeItem copyWithZone:]
+ -[NTPBRecipeItem dealloc]
+ -[NTPBRecipeItem description]
+ -[NTPBRecipeItem dictionaryRepresentation]
+ -[NTPBRecipeItem hasRecipeRecord]
+ -[NTPBRecipeItem hasSurfacedBy]
+ -[NTPBRecipeItem hash]
+ -[NTPBRecipeItem isEqual:]
+ -[NTPBRecipeItem mergeFrom:]
+ -[NTPBRecipeItem readFrom:]
+ -[NTPBRecipeItem recipeRecord]
+ -[NTPBRecipeItem setRecipeRecord:]
+ -[NTPBRecipeItem setSurfacedBy:]
+ -[NTPBRecipeItem surfacedBy]
+ -[NTPBRecipeItem writeTo:]
+ -[NTPBRecipeRecord hasLastModifiedDate]
+ -[NTPBRecipeRecord lastModifiedDate]
+ -[NTPBRecipeRecord setLastModifiedDate:]
+ OBJC_IVAR_$_NTPBFeedItem._backendArticleVersion
+ OBJC_IVAR_$_NTPBFeedItem._lastModifiedDateMilliseconds
+ OBJC_IVAR_$_NTPBFeedPersonalizingItem._lastModifiedDateMilliseconds
+ OBJC_IVAR_$_NTPBRecipeItem._recipeRecord
+ OBJC_IVAR_$_NTPBRecipeItem._surfacedBy
+ OBJC_IVAR_$_NTPBRecipeRecord._lastModifiedDate
+ _NTPBRecipeItemReadFrom
+ _OBJC_CLASS_$_NTPBRecipeItem
+ _OBJC_METACLASS_$_NTPBRecipeItem
+ __OBJC_$_INSTANCE_METHODS_NTPBRecipeItem
+ __OBJC_$_INSTANCE_VARIABLES_NTPBRecipeItem
+ __OBJC_$_PROP_LIST_NTPBRecipeItem
+ __OBJC_CLASS_PROTOCOLS_$_NTPBRecipeItem
+ __OBJC_CLASS_RO_$_NTPBRecipeItem
+ __OBJC_METACLASS_RO_$_NTPBRecipeItem
+ _objc_msgSend$_setError
+ _objc_msgSend$data
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$length
+ _objc_msgSend$position
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setRecipeRecord:
+ _objc_msgSend$setSurfacedBy:
- +[NTPBRecipeRecord topicTagIDsType]
- -[NTPBRecipeRecord addTopicTagIDs:]
- -[NTPBRecipeRecord clearTopicTagIDs]
- -[NTPBRecipeRecord setTopicTagIDs:]
- -[NTPBRecipeRecord topicTagIDsAtIndex:]
- -[NTPBRecipeRecord topicTagIDsCount]
- -[NTPBRecipeRecord topicTagIDs]
- -[NTPBScoreProfile featureCtr]
- -[NTPBScoreProfile hasFeatureCtr]
- -[NTPBScoreProfile setFeatureCtr:]
- -[NTPBScoreProfile setHasFeatureCtr:]
- OBJC_IVAR_$_NTPBRecipeRecord._topicTagIDs
- OBJC_IVAR_$_NTPBScoreProfile._featureCtr
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
CStrings:
+ "@\"NTPBRecipeRecord\""
+ "NTPBRecipeItem"
+ "T@\"NSString\",&,N,V_surfacedBy"
+ "T@\"NTPBRecipeRecord\",&,N,V_recipeRecord"
+ "TQ,N,V_lastModifiedDateMilliseconds"
+ "_lastModifiedDateMilliseconds"
+ "_recipeRecord"
+ "_setError"
+ "_surfacedBy"
+ "data"
+ "getBytes:range:"
+ "hasLastModifiedDateMilliseconds"
+ "hasRecipeRecord"
+ "hasSurfacedBy"
+ "lastModifiedDateMilliseconds"
+ "last_modified_date_milliseconds"
+ "length"
+ "recipeRecord"
+ "recipe_record"
+ "setHasLastModifiedDateMilliseconds:"
+ "setLastModifiedDateMilliseconds:"
+ "setRecipeRecord:"
+ "setSurfacedBy:"
+ "surfacedBy"
+ "surfaced_by"
+ "{?=\"agedPersonalizationScore\"b1\"autoSubscribeCtr\"b1\"computedGlobalScoreCoefficient\"b1\"contentTriggerDampener\"b1\"conversionMultiplier\"b1\"dampenedStaticMultiplier\"b1\"democratizationFactor\"b1\"embeddingScore\"b1\"multiplier\"b1\"nicheContentMultiplier\"b1\"paidNonpaidSubscriptionCtr\"b1\"personalizationScore\"b1\"publisherDampener\"b1\"publisherFavorability\"b1\"qualitativeMultiplier\"b1\"rawPersonalizationScore\"b1\"rawUserFeedbackScore\"b1\"scoringVersion\"b1\"serverScoreDemocratizationFactor\"b1\"shadowAgedPersonalizationScore\"b1\"shadowTabiScore\"b1\"staticMultiplier\"b1\"subscribedChannelCtr\"b1\"tabiScore\"b1\"userFeedbackScore\"b1\"isCoread\"b1\"isEvergreen\"b1}"
+ "{?=\"backendArticleVersion\"b1\"bodyTextLength\"b1\"conditionalScore\"b1\"contentType\"b1\"feedHalfLifeMilliseconds\"b1\"globalUserFeedback\"b1\"lastModifiedDateMilliseconds\"b1\"minimumNewsVersion\"b1\"order\"b1\"publishDateMilliseconds\"b1\"publisherArticleVersion\"b1\"surfacedByFlags\"b1\"storyType\"b1\"hasAudioTrack\"b1\"hasThumbnail\"b1\"hasVideo\"b1\"hasVideoStillImage\"b1\"isAIGenerated\"b1\"isBundlePaid\"b1\"isCoread\"b1\"isEvergreen\"b1\"isExplicitContent\"b1\"isFeatureCandidate\"b1\"isFeatured\"b1\"isFromBlockedStorefront\"b1\"isHiddenFromAutoFavorites\"b1\"isIssueOnly\"b1\"isPaid\"b1\"isSponsored\"b1\"reduceVisibility\"b1\"reduceVisibilityForNonFollowers\"b1\"webConverted\"b1}"
+ "{?=\"bodyTextLength\"b1\"lastModifiedDateMilliseconds\"b1\"publishDateMilliseconds\"b1\"hasAudioTrack\"b1\"hasVideo\"b1\"isAIGenerated\"b1\"isANF\"b1\"isBundlePaid\"b1\"isFeatured\"b1\"isPaid\"b1}"
- "{?=\"agedPersonalizationScore\"b1\"autoSubscribeCtr\"b1\"computedGlobalScoreCoefficient\"b1\"contentTriggerDampener\"b1\"conversionMultiplier\"b1\"dampenedStaticMultiplier\"b1\"democratizationFactor\"b1\"embeddingScore\"b1\"featureCtr\"b1\"multiplier\"b1\"nicheContentMultiplier\"b1\"paidNonpaidSubscriptionCtr\"b1\"personalizationScore\"b1\"publisherDampener\"b1\"publisherFavorability\"b1\"qualitativeMultiplier\"b1\"rawPersonalizationScore\"b1\"rawUserFeedbackScore\"b1\"scoringVersion\"b1\"serverScoreDemocratizationFactor\"b1\"shadowAgedPersonalizationScore\"b1\"shadowTabiScore\"b1\"staticMultiplier\"b1\"subscribedChannelCtr\"b1\"tabiScore\"b1\"userFeedbackScore\"b1\"isCoread\"b1\"isEvergreen\"b1}"
- "{?=\"bodyTextLength\"b1\"conditionalScore\"b1\"contentType\"b1\"feedHalfLifeMilliseconds\"b1\"globalUserFeedback\"b1\"minimumNewsVersion\"b1\"order\"b1\"publishDateMilliseconds\"b1\"publisherArticleVersion\"b1\"surfacedByFlags\"b1\"storyType\"b1\"hasAudioTrack\"b1\"hasThumbnail\"b1\"hasVideo\"b1\"hasVideoStillImage\"b1\"isAIGenerated\"b1\"isBundlePaid\"b1\"isCoread\"b1\"isEvergreen\"b1\"isExplicitContent\"b1\"isFeatureCandidate\"b1\"isFeatured\"b1\"isFromBlockedStorefront\"b1\"isHiddenFromAutoFavorites\"b1\"isIssueOnly\"b1\"isPaid\"b1\"isSponsored\"b1\"reduceVisibility\"b1\"reduceVisibilityForNonFollowers\"b1\"webConverted\"b1}"
- "{?=\"bodyTextLength\"b1\"publishDateMilliseconds\"b1\"hasAudioTrack\"b1\"hasVideo\"b1\"isAIGenerated\"b1\"isANF\"b1\"isBundlePaid\"b1\"isFeatured\"b1\"isPaid\"b1}"

```
