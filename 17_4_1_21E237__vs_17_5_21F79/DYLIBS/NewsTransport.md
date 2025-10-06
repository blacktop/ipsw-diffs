## NewsTransport

> `/System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport`

```diff

-5345.2.0.0.0
-  __TEXT.__text: 0x2235d4
+5407.3.0.0.0
+  __TEXT.__text: 0x224484
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_methlist: 0x32788
+  __TEXT.__objc_methlist: 0x32908
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x11179
-  __TEXT.__unwind_info: 0x472c
+  __TEXT.__cstring: 0x111b9
+  __TEXT.__unwind_info: 0x46a8
   __TEXT.__objc_classname: 0x2191
-  __TEXT.__objc_methname: 0x50635
-  __TEXT.__objc_methtype: 0xc24d
-  __TEXT.__objc_stubs: 0x8040
+  __TEXT.__objc_methname: 0x50876
+  __TEXT.__objc_methtype: 0xc289
+  __TEXT.__objc_stubs: 0x80a0
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x7148
   __DATA_CONST.__objc_classlist: 0x9d0
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3ed08
-  __DATA_CONST.__objc_selrefs: 0x10078
+  __DATA_CONST.__objc_const: 0x3eb08
+  __DATA_CONST.__objc_selrefs: 0x10128
   __DATA_CONST.__objc_classrefs: 0x7d8
   __DATA_CONST.__objc_superrefs: 0x9d0
-  __AUTH_CONST.__cfstring: 0x14820
-  __AUTH_CONST.__objc_const: 0x7a10
+  __AUTH_CONST.__cfstring: 0x148c0
+  __AUTH_CONST.__objc_const: 0x48
   __AUTH_CONST.__auth_got: 0x248
-  __AUTH.__objc_data: 0x3908
-  __DATA.__objc_ivar: 0x3b04
+  __DATA.__objc_ivar: 0x3b24
   __DATA.__data: 0x60
-  __DATA_DIRTY.__objc_data: 0x2918
+  __DATA_DIRTY.__objc_const: 0x7db8
+  __DATA_DIRTY.__objc_data: 0x6220
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0F2A504E-EE47-3551-A859-39C058EA2540
-  Functions: 17349
-  Symbols:   41565
-  CStrings:  18433
+  UUID: A9ED52C5-7B0C-31E9-8F54-F0FE396698DB
+  Functions: 17381
+  Symbols:   41640
+  CStrings:  18475
 
Symbols:
+ +[NTPBFeedItem surfacedByArticleListID2Type]
+ +[NTPBPuzzleTypeRecord latestPuzzleIDsType]
+ +[NTPBPuzzleTypeRecord promotedPuzzleIDsType]
+ -[COMAPPLEFELDSPARPROTOCOLANALYTICSEVENTSWidgetEngagement entryId]
+ -[COMAPPLEFELDSPARPROTOCOLANALYTICSEVENTSWidgetEngagement hasEntryId]
+ -[COMAPPLEFELDSPARPROTOCOLANALYTICSEVENTSWidgetEngagement setEntryId:]
+ -[NTPBFeedItem addSurfacedByArticleListID2:]
+ -[NTPBFeedItem clearSurfacedByArticleListID2s]
+ -[NTPBFeedItem conditionalScore]
+ -[NTPBFeedItem hasConditionalScore]
+ -[NTPBFeedItem hasIsCoread]
+ -[NTPBFeedItem isCoread]
+ -[NTPBFeedItem setConditionalScore:]
+ -[NTPBFeedItem setHasConditionalScore:]
+ -[NTPBFeedItem setHasIsCoread:]
+ -[NTPBFeedItem setIsCoread:]
+ -[NTPBFeedItem setSurfacedByArticleListID2s:]
+ -[NTPBFeedItem surfacedByArticleListID2AtIndex:]
+ -[NTPBFeedItem surfacedByArticleListID2sCount]
+ -[NTPBFeedItem surfacedByArticleListID2s]
+ -[NTPBForYouTodaySectionSpecificConfig feedMaxCount]
+ -[NTPBForYouTodaySectionSpecificConfig hasFeedMaxCount]
+ -[NTPBForYouTodaySectionSpecificConfig setFeedMaxCount:]
+ -[NTPBForYouTodaySectionSpecificConfig setHasFeedMaxCount:]
+ -[NTPBPuzzleRecord dataResourceID]
+ -[NTPBPuzzleRecord hasDataResourceID]
+ -[NTPBPuzzleRecord hasPuzzleTypeID]
+ -[NTPBPuzzleRecord puzzleTypeID]
+ -[NTPBPuzzleRecord setDataResourceID:]
+ -[NTPBPuzzleRecord setPuzzleTypeID:]
+ -[NTPBPuzzleTypeRecord addLatestPuzzleIDs:]
+ -[NTPBPuzzleTypeRecord addPromotedPuzzleIDs:]
+ -[NTPBPuzzleTypeRecord clearLatestPuzzleIDs]
+ -[NTPBPuzzleTypeRecord clearPromotedPuzzleIDs]
+ -[NTPBPuzzleTypeRecord engineResourceID]
+ -[NTPBPuzzleTypeRecord hasEngineResourceID]
+ -[NTPBPuzzleTypeRecord hasKind]
+ -[NTPBPuzzleTypeRecord kind]
+ -[NTPBPuzzleTypeRecord latestPuzzleIDsAtIndex:]
+ -[NTPBPuzzleTypeRecord latestPuzzleIDsCount]
+ -[NTPBPuzzleTypeRecord latestPuzzleIDs]
+ -[NTPBPuzzleTypeRecord promotedPuzzleIDsAtIndex:]
+ -[NTPBPuzzleTypeRecord promotedPuzzleIDsCount]
+ -[NTPBPuzzleTypeRecord promotedPuzzleIDs]
+ -[NTPBPuzzleTypeRecord setEngineResourceID:]
+ -[NTPBPuzzleTypeRecord setKind:]
+ -[NTPBPuzzleTypeRecord setLatestPuzzleIDs:]
+ -[NTPBPuzzleTypeRecord setPromotedPuzzleIDs:]
+ -[NTPBScoreProfile hasIsCoread]
+ -[NTPBScoreProfile isCoread]
+ -[NTPBScoreProfile setHasIsCoread:]
+ -[NTPBScoreProfile setIsCoread:]
+ -[NTPBTodayWidgetExposure entryId]
+ -[NTPBTodayWidgetExposure hasEntryId]
+ -[NTPBTodayWidgetExposure setEntryId:]
+ -[NTPBWidgetEngagement entryId]
+ -[NTPBWidgetEngagement hasEntryId]
+ -[NTPBWidgetEngagement setEntryId:]
+ OBJC_IVAR_$_COMAPPLEFELDSPARPROTOCOLANALYTICSEVENTSWidgetEngagement._entryId
+ OBJC_IVAR_$_NTPBFeedItem._conditionalScore
+ OBJC_IVAR_$_NTPBFeedItem._isCoread
+ OBJC_IVAR_$_NTPBFeedItem._surfacedByArticleListID2s
+ OBJC_IVAR_$_NTPBForYouTodaySectionSpecificConfig._feedMaxCount
+ OBJC_IVAR_$_NTPBPuzzleRecord._dataResourceID
+ OBJC_IVAR_$_NTPBPuzzleRecord._puzzleTypeID
+ OBJC_IVAR_$_NTPBPuzzleTypeRecord._engineResourceID
+ OBJC_IVAR_$_NTPBPuzzleTypeRecord._kind
+ OBJC_IVAR_$_NTPBPuzzleTypeRecord._latestPuzzleIDs
+ OBJC_IVAR_$_NTPBPuzzleTypeRecord._promotedPuzzleIDs
+ OBJC_IVAR_$_NTPBScoreProfile._isCoread
+ OBJC_IVAR_$_NTPBTodayWidgetExposure._entryId
+ OBJC_IVAR_$_NTPBWidgetEngagement._entryId
+ _objc_msgSend$addLatestPuzzleIDs:
+ _objc_msgSend$addPromotedPuzzleIDs:
+ _objc_msgSend$addSurfacedByArticleListID2:
+ _objc_msgSend$setDataResourceID:
+ _objc_msgSend$setEngineResourceID:
+ _objc_msgSend$setEntryId:
+ _objc_msgSend$setKind:
+ _objc_msgSend$setLatestPuzzleIDs:
+ _objc_msgSend$setPromotedPuzzleIDs:
+ _objc_msgSend$setPuzzleTypeID:
+ _objc_msgSend$setSurfacedByArticleListID2s:
- +[NTPBPuzzleTypeRecord latestPuzzleIdsType]
- +[NTPBPuzzleTypeRecord promotedPuzzleIdsType]
- -[NTPBFeedItem hasSourceArticleListID]
- -[NTPBFeedItem setSourceArticleListID:]
- -[NTPBFeedItem sourceArticleListID]
- -[NTPBPuzzleRecord dataResourceId]
- -[NTPBPuzzleRecord hasDataResourceId]
- -[NTPBPuzzleRecord hasPuzzleTypeId]
- -[NTPBPuzzleRecord puzzleTypeId]
- -[NTPBPuzzleRecord setDataResourceId:]
- -[NTPBPuzzleRecord setPuzzleTypeId:]
- -[NTPBPuzzleTypeRecord addLatestPuzzleIds:]
- -[NTPBPuzzleTypeRecord addPromotedPuzzleIds:]
- -[NTPBPuzzleTypeRecord clearLatestPuzzleIds]
- -[NTPBPuzzleTypeRecord clearPromotedPuzzleIds]
- -[NTPBPuzzleTypeRecord engineResourceId]
- -[NTPBPuzzleTypeRecord hasEngineResourceId]
- -[NTPBPuzzleTypeRecord latestPuzzleIdsAtIndex:]
- -[NTPBPuzzleTypeRecord latestPuzzleIdsCount]
- -[NTPBPuzzleTypeRecord latestPuzzleIds]
- -[NTPBPuzzleTypeRecord promotedPuzzleIdsAtIndex:]
- -[NTPBPuzzleTypeRecord promotedPuzzleIdsCount]
- -[NTPBPuzzleTypeRecord promotedPuzzleIds]
- -[NTPBPuzzleTypeRecord setEngineResourceId:]
- -[NTPBPuzzleTypeRecord setLatestPuzzleIds:]
- -[NTPBPuzzleTypeRecord setPromotedPuzzleIds:]
- OBJC_IVAR_$_NTPBFeedItem._sourceArticleListID
- OBJC_IVAR_$_NTPBPuzzleRecord._dataResourceId
- OBJC_IVAR_$_NTPBPuzzleRecord._puzzleTypeId
- OBJC_IVAR_$_NTPBPuzzleTypeRecord._engineResourceId
- OBJC_IVAR_$_NTPBPuzzleTypeRecord._latestPuzzleIds
- OBJC_IVAR_$_NTPBPuzzleTypeRecord._promotedPuzzleIds
- _objc_msgSend$addLatestPuzzleIds:
- _objc_msgSend$addPromotedPuzzleIds:
- _objc_msgSend$setDataResourceId:
- _objc_msgSend$setEngineResourceId:
- _objc_msgSend$setLatestPuzzleIds:
- _objc_msgSend$setPromotedPuzzleIds:
- _objc_msgSend$setPuzzleTypeId:
- _objc_msgSend$setSourceArticleListID:
CStrings:
+ "\x12#"
+ "\x1a!2\x11"
+ "T@\"NSMutableArray\",&,N,V_latestPuzzleIDs"
+ "T@\"NSMutableArray\",&,N,V_promotedPuzzleIDs"
+ "T@\"NSMutableArray\",&,N,V_surfacedByArticleListID2s"
+ "T@\"NSString\",&,N,V_dataResourceID"
+ "T@\"NSString\",&,N,V_engineResourceID"
+ "T@\"NSString\",&,N,V_entryId"
+ "T@\"NSString\",&,N,V_kind"
+ "T@\"NSString\",&,N,V_puzzleTypeID"
+ "TB,N,V_isCoread"
+ "TQ,N,V_feedMaxCount"
+ "Td,N,V_conditionalScore"
+ "_conditionalScore"
+ "_dataResourceID"
+ "_engineResourceID"
+ "_entryId"
+ "_feedMaxCount"
+ "_isCoread"
+ "_kind"
+ "_latestPuzzleIDs"
+ "_promotedPuzzleIDs"
+ "_puzzleTypeID"
+ "_surfacedByArticleListID2s"
+ "addLatestPuzzleIDs:"
+ "addPromotedPuzzleIDs:"
+ "addSurfacedByArticleListID2:"
+ "clearLatestPuzzleIDs"
+ "clearPromotedPuzzleIDs"
+ "clearSurfacedByArticleListID2s"
+ "conditionalScore"
+ "conditional_score"
+ "dataResourceID"
+ "data_resource_ID"
+ "engineResourceID"
+ "engine_resource_ID"
+ "entryId"
+ "entry_id"
+ "feedMaxCount"
+ "feed_max_count"
+ "hasConditionalScore"
+ "hasDataResourceID"
+ "hasEngineResourceID"
+ "hasEntryId"
+ "hasFeedMaxCount"
+ "hasIsCoread"
+ "hasKind"
+ "hasPuzzleTypeID"
+ "isCoread"
+ "is_coread"
+ "kind"
+ "latestPuzzleIDs"
+ "latestPuzzleIDsAtIndex:"
+ "latestPuzzleIDsCount"
+ "latestPuzzleIDsType"
+ "latest_puzzle_IDs"
+ "promotedPuzzleIDs"
+ "promotedPuzzleIDsAtIndex:"
+ "promotedPuzzleIDsCount"
+ "promotedPuzzleIDsType"
+ "promoted_puzzle_IDs"
+ "puzzleTypeID"
+ "puzzle_type_ID"
+ "setConditionalScore:"
+ "setDataResourceID:"
+ "setEngineResourceID:"
+ "setEntryId:"
+ "setFeedMaxCount:"
+ "setHasConditionalScore:"
+ "setHasFeedMaxCount:"
+ "setHasIsCoread:"
+ "setIsCoread:"
+ "setKind:"
+ "setLatestPuzzleIDs:"
+ "setPromotedPuzzleIDs:"
+ "setPuzzleTypeID:"
+ "setSurfacedByArticleListID2s:"
+ "surfacedByArticleListID2AtIndex:"
+ "surfacedByArticleListID2Type"
+ "surfacedByArticleListID2s"
+ "surfacedByArticleListID2sCount"
+ "surfaced_by_article_list_ID_2"
+ "{?=\"agedPersonalizationScore\"b1\"autoSubscribeCtr\"b1\"computedGlobalScoreCoefficient\"b1\"contentTriggerDampener\"b1\"conversionMultiplier\"b1\"dampenedStaticMultiplier\"b1\"democratizationFactor\"b1\"embeddingScore\"b1\"featureCtr\"b1\"multiplier\"b1\"nicheContentMultiplier\"b1\"paidNonpaidSubscriptionCtr\"b1\"personalizationScore\"b1\"publisherDampener\"b1\"publisherFavorability\"b1\"qualitativeMultiplier\"b1\"rawPersonalizationScore\"b1\"rawUserFeedbackScore\"b1\"scoringVersion\"b1\"serverScoreDemocratizationFactor\"b1\"shadowAgedPersonalizationScore\"b1\"shadowTabiScore\"b1\"staticMultiplier\"b1\"subscribedChannelCtr\"b1\"tabiScore\"b1\"userFeedbackScore\"b1\"isCoread\"b1\"isEvergreen\"b1}"
+ "{?=\"bodyTextLength\"b1\"conditionalScore\"b1\"contentType\"b1\"feedHalfLifeMilliseconds\"b1\"globalUserFeedback\"b1\"minimumNewsVersion\"b1\"order\"b1\"publishDateMilliseconds\"b1\"publisherArticleVersion\"b1\"hasAudioTrack\"b1\"hasThumbnail\"b1\"hasVideo\"b1\"hasVideoStillImage\"b1\"isBundlePaid\"b1\"isCoread\"b1\"isEvergreen\"b1\"isExplicitContent\"b1\"isFeatureCandidate\"b1\"isFeatured\"b1\"isFromBlockedStorefront\"b1\"isHiddenFromAutoFavorites\"b1\"isIssueOnly\"b1\"isPaid\"b1\"isSponsored\"b1\"reduceVisibility\"b1\"reduceVisibilityForNonFollowers\"b1\"webConverted\"b1}"
+ "{?=\"cutoffTime\"b1\"feedMaxCount\"b1\"headlinesPerFeedFetchCount\"b1\"localNewsPromotionIndex\"b1\"minimumUpdateInterval\"b1\"subscriptionsFetchCount\"b1\"fetchingBin\"b1}"
- "\x11#"
- "\x19!2\x11"
- "T@\"NSMutableArray\",&,N,V_latestPuzzleIds"
- "T@\"NSMutableArray\",&,N,V_promotedPuzzleIds"
- "T@\"NSString\",&,N,V_dataResourceId"
- "T@\"NSString\",&,N,V_engineResourceId"
- "T@\"NSString\",&,N,V_puzzleTypeId"
- "T@\"NSString\",&,N,V_sourceArticleListID"
- "_dataResourceId"
- "_engineResourceId"
- "_latestPuzzleIds"
- "_promotedPuzzleIds"
- "_puzzleTypeId"
- "_sourceArticleListID"
- "addLatestPuzzleIds:"
- "addPromotedPuzzleIds:"
- "clearLatestPuzzleIds"
- "clearPromotedPuzzleIds"
- "dataResourceId"
- "data_resource_id"
- "engineResourceId"
- "engine_resource_id"
- "hasDataResourceId"
- "hasEngineResourceId"
- "hasPuzzleTypeId"
- "hasSourceArticleListID"
- "latestPuzzleIds"
- "latestPuzzleIdsAtIndex:"
- "latestPuzzleIdsCount"
- "latestPuzzleIdsType"
- "latest_puzzle_ids"
- "promotedPuzzleIds"
- "promotedPuzzleIdsAtIndex:"
- "promotedPuzzleIdsCount"
- "promotedPuzzleIdsType"
- "promoted_puzzle_ids"
- "puzzleTypeId"
- "puzzle_type_id"
- "setDataResourceId:"
- "setEngineResourceId:"
- "setLatestPuzzleIds:"
- "setPromotedPuzzleIds:"
- "setPuzzleTypeId:"
- "setSourceArticleListID:"
- "sourceArticleListID"
- "source_article_list_ID"
- "{?=\"agedPersonalizationScore\"b1\"autoSubscribeCtr\"b1\"computedGlobalScoreCoefficient\"b1\"contentTriggerDampener\"b1\"conversionMultiplier\"b1\"dampenedStaticMultiplier\"b1\"democratizationFactor\"b1\"embeddingScore\"b1\"featureCtr\"b1\"multiplier\"b1\"nicheContentMultiplier\"b1\"paidNonpaidSubscriptionCtr\"b1\"personalizationScore\"b1\"publisherDampener\"b1\"publisherFavorability\"b1\"qualitativeMultiplier\"b1\"rawPersonalizationScore\"b1\"rawUserFeedbackScore\"b1\"scoringVersion\"b1\"serverScoreDemocratizationFactor\"b1\"shadowAgedPersonalizationScore\"b1\"shadowTabiScore\"b1\"staticMultiplier\"b1\"subscribedChannelCtr\"b1\"tabiScore\"b1\"userFeedbackScore\"b1\"isEvergreen\"b1}"
- "{?=\"bodyTextLength\"b1\"contentType\"b1\"feedHalfLifeMilliseconds\"b1\"globalUserFeedback\"b1\"minimumNewsVersion\"b1\"order\"b1\"publishDateMilliseconds\"b1\"publisherArticleVersion\"b1\"hasAudioTrack\"b1\"hasThumbnail\"b1\"hasVideo\"b1\"hasVideoStillImage\"b1\"isBundlePaid\"b1\"isEvergreen\"b1\"isExplicitContent\"b1\"isFeatureCandidate\"b1\"isFeatured\"b1\"isFromBlockedStorefront\"b1\"isHiddenFromAutoFavorites\"b1\"isIssueOnly\"b1\"isPaid\"b1\"isSponsored\"b1\"reduceVisibility\"b1\"reduceVisibilityForNonFollowers\"b1\"webConverted\"b1}"
- "{?=\"cutoffTime\"b1\"headlinesPerFeedFetchCount\"b1\"localNewsPromotionIndex\"b1\"minimumUpdateInterval\"b1\"subscriptionsFetchCount\"b1\"fetchingBin\"b1}"

```
