## NewsTransport

> `/System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport`

```diff

-3529.2.0.0.0
-  __TEXT.__text: 0x221ff0
+3557.1.0.0.0
+  __TEXT.__text: 0x2230e4
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_methlist: 0x32588
+  __TEXT.__objc_methlist: 0x32710
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x11084
+  __TEXT.__cstring: 0x11153
   __TEXT.__unwind_info: 0x472c
   __TEXT.__objc_classname: 0x2191
-  __TEXT.__objc_methname: 0x50032
-  __TEXT.__objc_methtype: 0xc186
-  __TEXT.__objc_stubs: 0x7fe0
+  __TEXT.__objc_methname: 0x5054e
+  __TEXT.__objc_methtype: 0xc227
+  __TEXT.__objc_stubs: 0x8040
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x7148
   __DATA_CONST.__objc_classlist: 0x9d0
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3ea08
-  __DATA_CONST.__objc_selrefs: 0xff70
-  __AUTH_CONST.__cfstring: 0x14720
+  __DATA_CONST.__objc_const: 0x3ec48
+  __DATA_CONST.__objc_selrefs: 0x10058
+  __AUTH_CONST.__cfstring: 0x14800
   __AUTH_CONST.__objc_const: 0x7a10
   __AUTH_CONST.__auth_got: 0x248
   __AUTH.__objc_data: 0x39a8
   __DATA.__objc_classrefs: 0x7d8
   __DATA.__objc_superrefs: 0x9d0
-  __DATA.__objc_ivar: 0x3ad4
+  __DATA.__objc_ivar: 0x3af8
   __DATA.__data: 0x60
   __DATA_DIRTY.__objc_data: 0x2878
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2DC590BF-48F1-3817-A136-E0D3B6D5A466
-  Functions: 17306
-  Symbols:   41464
-  CStrings:  18366
+  UUID: 64221FA3-04BB-36B0-B5AB-53FB6E53BFD8
+  Functions: 17339
+  Symbols:   41542
+  CStrings:  18425
 
Symbols:
+ -[NTPBCoefficients conversionCoefficient]
+ -[NTPBCoefficients halfLifeCoefficient]
+ -[NTPBCoefficients hasConversionCoefficient]
+ -[NTPBCoefficients hasHalfLifeCoefficient]
+ -[NTPBCoefficients setConversionCoefficient:]
+ -[NTPBCoefficients setHalfLifeCoefficient:]
+ -[NTPBCoefficients setHasConversionCoefficient:]
+ -[NTPBCoefficients setHasHalfLifeCoefficient:]
+ -[NTPBFeedItem hasReduceVisibilityForNonFollowers]
+ -[NTPBFeedItem reduceVisibilityForNonFollowers]
+ -[NTPBFeedItem setHasReduceVisibilityForNonFollowers:]
+ -[NTPBFeedItem setReduceVisibilityForNonFollowers:]
+ -[NTPBScoreProfile contentTriggerDampener]
+ -[NTPBScoreProfile democratizationFactor]
+ -[NTPBScoreProfile hasContentTriggerDampener]
+ -[NTPBScoreProfile hasDemocratizationFactor]
+ -[NTPBScoreProfile hasMultiplier]
+ -[NTPBScoreProfile hasNicheContentMultiplier]
+ -[NTPBScoreProfile hasServerScoreDemocratizationFactor]
+ -[NTPBScoreProfile multiplier]
+ -[NTPBScoreProfile nicheContentMultiplier]
+ -[NTPBScoreProfile serverScoreDemocratizationFactor]
+ -[NTPBScoreProfile setContentTriggerDampener:]
+ -[NTPBScoreProfile setDemocratizationFactor:]
+ -[NTPBScoreProfile setHasContentTriggerDampener:]
+ -[NTPBScoreProfile setHasDemocratizationFactor:]
+ -[NTPBScoreProfile setHasMultiplier:]
+ -[NTPBScoreProfile setHasNicheContentMultiplier:]
+ -[NTPBScoreProfile setHasServerScoreDemocratizationFactor:]
+ -[NTPBScoreProfile setMultiplier:]
+ -[NTPBScoreProfile setNicheContentMultiplier:]
+ -[NTPBScoreProfile setServerScoreDemocratizationFactor:]
+ -[NTPBTagRecord hasPropertyFlagsLocalized]
+ -[NTPBTagRecord hasSportsLogoAltImageCompactURL]
+ -[NTPBTagRecord hasSportsLogoAltImageLargeURL]
+ -[NTPBTagRecord hasSportsLogoAltImageURL]
+ -[NTPBTagRecord propertyFlagsLocalized]
+ -[NTPBTagRecord setHasPropertyFlagsLocalized:]
+ -[NTPBTagRecord setPropertyFlagsLocalized:]
+ -[NTPBTagRecord setSportsLogoAltImageCompactURL:]
+ -[NTPBTagRecord setSportsLogoAltImageLargeURL:]
+ -[NTPBTagRecord setSportsLogoAltImageURL:]
+ -[NTPBTagRecord sportsLogoAltImageCompactURL]
+ -[NTPBTagRecord sportsLogoAltImageLargeURL]
+ -[NTPBTagRecord sportsLogoAltImageURL]
+ OBJC_IVAR_$_NTPBCoefficients._conversionCoefficient
+ OBJC_IVAR_$_NTPBCoefficients._halfLifeCoefficient
+ OBJC_IVAR_$_NTPBFeedItem._reduceVisibilityForNonFollowers
+ OBJC_IVAR_$_NTPBScoreProfile._contentTriggerDampener
+ OBJC_IVAR_$_NTPBScoreProfile._democratizationFactor
+ OBJC_IVAR_$_NTPBScoreProfile._multiplier
+ OBJC_IVAR_$_NTPBScoreProfile._nicheContentMultiplier
+ OBJC_IVAR_$_NTPBScoreProfile._serverScoreDemocratizationFactor
+ OBJC_IVAR_$_NTPBTagRecord._propertyFlagsLocalized
+ OBJC_IVAR_$_NTPBTagRecord._sportsLogoAltImageCompactURL
+ OBJC_IVAR_$_NTPBTagRecord._sportsLogoAltImageLargeURL
+ OBJC_IVAR_$_NTPBTagRecord._sportsLogoAltImageURL
+ _objc_msgSend$setSportsLogoAltImageCompactURL:
+ _objc_msgSend$setSportsLogoAltImageLargeURL:
+ _objc_msgSend$setSportsLogoAltImageURL:
- -[NTPBScoreProfileDebug contentTriggerDampener]
- -[NTPBScoreProfileDebug halfLifeCoefficient]
- -[NTPBScoreProfileDebug hasContentTriggerDampener]
- -[NTPBScoreProfileDebug hasHalfLifeCoefficient]
- -[NTPBScoreProfileDebug hasNicheContentMultiplier]
- -[NTPBScoreProfileDebug nicheContentMultiplier]
- -[NTPBScoreProfileDebug setContentTriggerDampener:]
- -[NTPBScoreProfileDebug setHalfLifeCoefficient:]
- -[NTPBScoreProfileDebug setHasContentTriggerDampener:]
- -[NTPBScoreProfileDebug setHasHalfLifeCoefficient:]
- -[NTPBScoreProfileDebug setHasNicheContentMultiplier:]
- -[NTPBScoreProfileDebug setNicheContentMultiplier:]
- OBJC_IVAR_$_NTPBScoreProfileDebug._contentTriggerDampener
- OBJC_IVAR_$_NTPBScoreProfileDebug._halfLifeCoefficient
- OBJC_IVAR_$_NTPBScoreProfileDebug._nicheContentMultiplier
CStrings:
+ "T@\"NSString\",&,N,V_sportsLogoAltImageCompactURL"
+ "T@\"NSString\",&,N,V_sportsLogoAltImageLargeURL"
+ "T@\"NSString\",&,N,V_sportsLogoAltImageURL"
+ "TB,N,V_reduceVisibilityForNonFollowers"
+ "Td,N,V_conversionCoefficient"
+ "Td,N,V_multiplier"
+ "Td,N,V_serverScoreDemocratizationFactor"
+ "Tq,N,V_propertyFlagsLocalized"
+ "_conversionCoefficient"
+ "_multiplier"
+ "_propertyFlagsLocalized"
+ "_reduceVisibilityForNonFollowers"
+ "_serverScoreDemocratizationFactor"
+ "_sportsLogoAltImageCompactURL"
+ "_sportsLogoAltImageLargeURL"
+ "_sportsLogoAltImageURL"
+ "content_trigger_dampener"
+ "conversionCoefficient"
+ "conversion_coefficient"
+ "hasConversionCoefficient"
+ "hasMultiplier"
+ "hasPropertyFlagsLocalized"
+ "hasReduceVisibilityForNonFollowers"
+ "hasServerScoreDemocratizationFactor"
+ "hasSportsLogoAltImageCompactURL"
+ "hasSportsLogoAltImageLargeURL"
+ "hasSportsLogoAltImageURL"
+ "multiplier"
+ "niche_content_multiplier"
+ "propertyFlagsLocalized"
+ "property_flags_localized"
+ "reduceVisibilityForNonFollowers"
+ "reduce_visibility_for_non_followers"
+ "serverScoreDemocratizationFactor"
+ "server_score_democratization_factor"
+ "setConversionCoefficient:"
+ "setHasConversionCoefficient:"
+ "setHasMultiplier:"
+ "setHasPropertyFlagsLocalized:"
+ "setHasReduceVisibilityForNonFollowers:"
+ "setHasServerScoreDemocratizationFactor:"
+ "setMultiplier:"
+ "setPropertyFlagsLocalized:"
+ "setReduceVisibilityForNonFollowers:"
+ "setServerScoreDemocratizationFactor:"
+ "setSportsLogoAltImageCompactURL:"
+ "setSportsLogoAltImageLargeURL:"
+ "setSportsLogoAltImageURL:"
+ "sportsLogoAltImageCompactURL"
+ "sportsLogoAltImageLargeURL"
+ "sportsLogoAltImageURL"
+ "sports_logo_alt_image_URL"
+ "sports_logo_alt_image_compact_URL"
+ "sports_logo_alt_image_large_URL"
+ "{?=\"agedPersonalizationScore\"b1\"autoSubscribeCtr\"b1\"computedGlobalScoreCoefficient\"b1\"contentTriggerDampener\"b1\"conversionMultiplier\"b1\"dampenedStaticMultiplier\"b1\"democratizationFactor\"b1\"embeddingScore\"b1\"featureCtr\"b1\"multiplier\"b1\"nicheContentMultiplier\"b1\"paidNonpaidSubscriptionCtr\"b1\"personalizationScore\"b1\"publisherDampener\"b1\"publisherFavorability\"b1\"qualitativeMultiplier\"b1\"rawPersonalizationScore\"b1\"rawUserFeedbackScore\"b1\"scoringVersion\"b1\"serverScoreDemocratizationFactor\"b1\"shadowAgedPersonalizationScore\"b1\"shadowTabiScore\"b1\"staticMultiplier\"b1\"subscribedChannelCtr\"b1\"tabiScore\"b1\"userFeedbackScore\"b1\"isEvergreen\"b1}"
+ "{?=\"articleEmbeddingScoreCoefficient\"b1\"autofavoritedScoreCoefficient\"b1\"clientScoreCoefficient\"b1\"conversionCoefficient\"b1\"halfLifeCoefficient\"b1\"serverScoreCoefficient\"b1\"subscribedChannelScoreCoefficent\"b1\"subscribedTopicScoreCoefficient\"b1\"tabiScoreCoefficient\"b1}"
+ "{?=\"audioMultiplier\"b1\"bundleFreeMultiplier\"b1\"bundlePaidMultiplier\"b1\"evergreenMultiplier\"b1\"featuredMultiplier\"b1\"groupingReason\"b1\"listenedPenalty\"b1\"multiplierDampener\"b1\"mutedVoteDampener\"b1\"readPenalty\"b1\"scoringContext\"b1\"scoringType\"b1\"seenPenalty\"b1\"sparseTagsPenalty\"b1\"timeDecayPenalty\"b1\"userConversionScore\"b1}"
+ "{?=\"behaviorFlags\"b1\"contentProvider\"b1\"minimumNewsVersion\"b1\"nameImageBaselineShift\"b1\"nameImageScaleFactor\"b1\"propertyFlags\"b1\"propertyFlagsLocalized\"b1\"score\"b1\"subscriptionRate\"b1\"groupingAvailability\"b1\"type\"b1\"hideAccessoryText\"b1\"isDeprecated\"b1\"isExplicitContent\"b1\"isHidden\"b1\"isNotificationEnabled\"b1\"isPublic\"b1\"isSportsRecommendable\"b1\"publisherPaidLeakyPaywallOptOut\"b1\"publisherPaidWebOptIn\"b1}"
+ "{?=\"bodyTextLength\"b1\"contentType\"b1\"feedHalfLifeMilliseconds\"b1\"globalUserFeedback\"b1\"minimumNewsVersion\"b1\"order\"b1\"publishDateMilliseconds\"b1\"publisherArticleVersion\"b1\"hasAudioTrack\"b1\"hasThumbnail\"b1\"hasVideo\"b1\"hasVideoStillImage\"b1\"isBundlePaid\"b1\"isEvergreen\"b1\"isExplicitContent\"b1\"isFeatureCandidate\"b1\"isFeatured\"b1\"isFromBlockedStorefront\"b1\"isHiddenFromAutoFavorites\"b1\"isIssueOnly\"b1\"isPaid\"b1\"isSponsored\"b1\"reduceVisibility\"b1\"reduceVisibilityForNonFollowers\"b1\"webConverted\"b1}"
- "{?=\"agedPersonalizationScore\"b1\"autoSubscribeCtr\"b1\"computedGlobalScoreCoefficient\"b1\"conversionMultiplier\"b1\"dampenedStaticMultiplier\"b1\"embeddingScore\"b1\"featureCtr\"b1\"paidNonpaidSubscriptionCtr\"b1\"personalizationScore\"b1\"publisherDampener\"b1\"publisherFavorability\"b1\"qualitativeMultiplier\"b1\"rawPersonalizationScore\"b1\"rawUserFeedbackScore\"b1\"scoringVersion\"b1\"shadowAgedPersonalizationScore\"b1\"shadowTabiScore\"b1\"staticMultiplier\"b1\"subscribedChannelCtr\"b1\"tabiScore\"b1\"userFeedbackScore\"b1\"isEvergreen\"b1}"
- "{?=\"articleEmbeddingScoreCoefficient\"b1\"autofavoritedScoreCoefficient\"b1\"clientScoreCoefficient\"b1\"serverScoreCoefficient\"b1\"subscribedChannelScoreCoefficent\"b1\"subscribedTopicScoreCoefficient\"b1\"tabiScoreCoefficient\"b1}"
- "{?=\"audioMultiplier\"b1\"bundleFreeMultiplier\"b1\"bundlePaidMultiplier\"b1\"contentTriggerDampener\"b1\"evergreenMultiplier\"b1\"featuredMultiplier\"b1\"groupingReason\"b1\"halfLifeCoefficient\"b1\"listenedPenalty\"b1\"multiplierDampener\"b1\"mutedVoteDampener\"b1\"nicheContentMultiplier\"b1\"readPenalty\"b1\"scoringContext\"b1\"scoringType\"b1\"seenPenalty\"b1\"sparseTagsPenalty\"b1\"timeDecayPenalty\"b1\"userConversionScore\"b1}"
- "{?=\"behaviorFlags\"b1\"contentProvider\"b1\"minimumNewsVersion\"b1\"nameImageBaselineShift\"b1\"nameImageScaleFactor\"b1\"propertyFlags\"b1\"score\"b1\"subscriptionRate\"b1\"groupingAvailability\"b1\"type\"b1\"hideAccessoryText\"b1\"isDeprecated\"b1\"isExplicitContent\"b1\"isHidden\"b1\"isNotificationEnabled\"b1\"isPublic\"b1\"isSportsRecommendable\"b1\"publisherPaidLeakyPaywallOptOut\"b1\"publisherPaidWebOptIn\"b1}"
- "{?=\"bodyTextLength\"b1\"contentType\"b1\"feedHalfLifeMilliseconds\"b1\"globalUserFeedback\"b1\"minimumNewsVersion\"b1\"order\"b1\"publishDateMilliseconds\"b1\"publisherArticleVersion\"b1\"hasAudioTrack\"b1\"hasThumbnail\"b1\"hasVideo\"b1\"hasVideoStillImage\"b1\"isBundlePaid\"b1\"isEvergreen\"b1\"isExplicitContent\"b1\"isFeatureCandidate\"b1\"isFeatured\"b1\"isFromBlockedStorefront\"b1\"isHiddenFromAutoFavorites\"b1\"isIssueOnly\"b1\"isPaid\"b1\"isSponsored\"b1\"reduceVisibility\"b1\"webConverted\"b1}"

```
