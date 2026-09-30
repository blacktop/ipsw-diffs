## NewsTransport

> `/System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport`

```diff

-5805.0.0.0.0
-  __TEXT.__text: 0x279158
+5861.1.0.0.0
+  __TEXT.__text: 0x295afc
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x376ac
+  __TEXT.__objc_methlist: 0x37c0c
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x11d2a
-  __TEXT.__unwind_info: 0x4fc0
-  __TEXT.__objc_classname: 0x26a7
-  __TEXT.__objc_methname: 0x557df
-  __TEXT.__objc_methtype: 0xcbd7
-  __TEXT.__objc_stubs: 0x91e0
-  __DATA_CONST.__got: 0x940
+  __TEXT.__cstring: 0x11e07
+  __TEXT.__unwind_info: 0x7910
+  __TEXT.__objc_classname: 0x26e8
+  __TEXT.__objc_methname: 0x55d37
+  __TEXT.__objc_methtype: 0xcc61
+  __TEXT.__objc_stubs: 0x92a0
+  __DATA_CONST.__got: 0x958
   __DATA_CONST.__const: 0x72c8
-  __DATA_CONST.__objc_classlist: 0xb88
+  __DATA_CONST.__objc_classlist: 0xba0
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11510
-  __DATA_CONST.__objc_superrefs: 0xb88
+  __DATA_CONST.__objc_selrefs: 0x11620
+  __DATA_CONST.__objc_superrefs: 0xba0
   __AUTH_CONST.__auth_got: 0x238
-  __AUTH_CONST.__cfstring: 0x16000
-  __AUTH_CONST.__objc_const: 0x4d8f0
-  __AUTH.__objc_data: 0x41c8
-  __DATA.__objc_ivar: 0x4010
+  __AUTH_CONST.__cfstring: 0x16120
+  __AUTH_CONST.__objc_const: 0x4e118
+  __AUTH.__objc_data: 0x42b8
+  __DATA.__objc_ivar: 0x4074
   __DATA.__data: 0x60
   __DATA_DIRTY.__objc_data: 0x3188
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 693BB843-6305-3250-9AF4-D49F47937E9B
-  Functions: 18919
-  Symbols:   45778
-  CStrings:  19867
+  UUID: 2044D96F-5E8A-3B7F-A59F-56967C255020
+  Functions: 19042
+  Symbols:   46062
+  CStrings:  19942
 
Symbols:
+ +[NTPBTodaySnapshot sectionsType]
+ +[NTPBTodaySnapshotSection itemsType]
+ -[NTPBArticleRecord hasLiveCoverageModifiedDate]
+ -[NTPBArticleRecord liveCoverageModifiedDate]
+ -[NTPBArticleRecord setLiveCoverageModifiedDate:]
+ -[NTPBArticleTopic hasIsEligibleForFeaturePromotion]
+ -[NTPBArticleTopic isEligibleForFeaturePromotion]
+ -[NTPBArticleTopic setHasIsEligibleForFeaturePromotion:]
+ -[NTPBArticleTopic setIsEligibleForFeaturePromotion:]
+ -[NTPBAsset etag]
+ -[NTPBAsset expiresAt]
+ -[NTPBAsset hasEtag]
+ -[NTPBAsset hasExpiresAt]
+ -[NTPBAsset setEtag:]
+ -[NTPBAsset setExpiresAt:]
+ -[NTPBForYouTodaySectionSpecificConfig hasStabilizeAcrossRefreshes]
+ -[NTPBForYouTodaySectionSpecificConfig setHasStabilizeAcrossRefreshes:]
+ -[NTPBForYouTodaySectionSpecificConfig setStabilizeAcrossRefreshes:]
+ -[NTPBForYouTodaySectionSpecificConfig stabilizeAcrossRefreshes]
+ -[NTPBPuzzleTypeRecord feedNavDarkModeImageURL]
+ -[NTPBPuzzleTypeRecord hasFeedNavDarkModeImageURL]
+ -[NTPBPuzzleTypeRecord setFeedNavDarkModeImageURL:]
+ -[NTPBReadingHistoryItem clusterID]
+ -[NTPBReadingHistoryItem hasClusterID]
+ -[NTPBReadingHistoryItem setClusterID:]
+ -[NTPBRecipeItem hasOrder]
+ -[NTPBRecipeItem order]
+ -[NTPBRecipeItem setHasOrder:]
+ -[NTPBRecipeItem setOrder:]
+ -[NTPBRecipeRecord hasRecipeRating]
+ -[NTPBRecipeRecord recipeRating]
+ -[NTPBRecipeRecord setRecipeRating:]
+ -[NTPBSportsEventRecord hasSportsLogoAltImageCompactURL]
+ -[NTPBSportsEventRecord hasSportsLogoAltImageLargeURL]
+ -[NTPBSportsEventRecord hasSportsLogoAltImageURL]
+ -[NTPBSportsEventRecord hasSportsLogoImageCompactURL]
+ -[NTPBSportsEventRecord hasSportsLogoImageLargeURL]
+ -[NTPBSportsEventRecord hasSportsLogoImageURL]
+ -[NTPBSportsEventRecord setSportsLogoAltImageCompactURL:]
+ -[NTPBSportsEventRecord setSportsLogoAltImageLargeURL:]
+ -[NTPBSportsEventRecord setSportsLogoAltImageURL:]
+ -[NTPBSportsEventRecord setSportsLogoImageCompactURL:]
+ -[NTPBSportsEventRecord setSportsLogoImageLargeURL:]
+ -[NTPBSportsEventRecord setSportsLogoImageURL:]
+ -[NTPBSportsEventRecord sportsLogoAltImageCompactURL]
+ -[NTPBSportsEventRecord sportsLogoAltImageLargeURL]
+ -[NTPBSportsEventRecord sportsLogoAltImageURL]
+ -[NTPBSportsEventRecord sportsLogoImageCompactURL]
+ -[NTPBSportsEventRecord sportsLogoImageLargeURL]
+ -[NTPBSportsEventRecord sportsLogoImageURL]
+ -[NTPBTagRecord feedNavDarkModeImageHQURL]
+ -[NTPBTagRecord feedNavDarkModeImageURL]
+ -[NTPBTagRecord hasFeedNavDarkModeImageHQURL]
+ -[NTPBTagRecord hasFeedNavDarkModeImageURL]
+ -[NTPBTagRecord setFeedNavDarkModeImageHQURL:]
+ -[NTPBTagRecord setFeedNavDarkModeImageURL:]
+ -[NTPBTagTodaySectionSpecificConfig hasStabilizeAcrossRefreshes]
+ -[NTPBTagTodaySectionSpecificConfig setHasStabilizeAcrossRefreshes:]
+ -[NTPBTagTodaySectionSpecificConfig setStabilizeAcrossRefreshes:]
+ -[NTPBTagTodaySectionSpecificConfig stabilizeAcrossRefreshes]
+ -[NTPBTodayResultOperationInfo hasLastEntrySnapshot]
+ -[NTPBTodayResultOperationInfo lastEntrySnapshot]
+ -[NTPBTodayResultOperationInfo setLastEntrySnapshot:]
+ -[NTPBTodaySnapshot .cxx_destruct]
+ -[NTPBTodaySnapshot addSections:]
+ -[NTPBTodaySnapshot clearSections]
+ -[NTPBTodaySnapshot copyWithZone:]
+ -[NTPBTodaySnapshot description]
+ -[NTPBTodaySnapshot dictionaryRepresentation]
+ -[NTPBTodaySnapshot hash]
+ -[NTPBTodaySnapshot isEqual:]
+ -[NTPBTodaySnapshot mergeFrom:]
+ -[NTPBTodaySnapshot readFrom:]
+ -[NTPBTodaySnapshot sectionsAtIndex:]
+ -[NTPBTodaySnapshot sectionsCount]
+ -[NTPBTodaySnapshot sections]
+ -[NTPBTodaySnapshot setSections:]
+ -[NTPBTodaySnapshot writeTo:]
+ -[NTPBTodaySnapshotItem .cxx_destruct]
+ -[NTPBTodaySnapshotItem copyWithZone:]
+ -[NTPBTodaySnapshotItem description]
+ -[NTPBTodaySnapshotItem dictionaryRepresentation]
+ -[NTPBTodaySnapshotItem hasIdentifier]
+ -[NTPBTodaySnapshotItem hash]
+ -[NTPBTodaySnapshotItem identifier]
+ -[NTPBTodaySnapshotItem isEqual:]
+ -[NTPBTodaySnapshotItem mergeFrom:]
+ -[NTPBTodaySnapshotItem readFrom:]
+ -[NTPBTodaySnapshotItem setIdentifier:]
+ -[NTPBTodaySnapshotItem writeTo:]
+ -[NTPBTodaySnapshotSection .cxx_destruct]
+ -[NTPBTodaySnapshotSection addItems:]
+ -[NTPBTodaySnapshotSection clearItems]
+ -[NTPBTodaySnapshotSection copyWithZone:]
+ -[NTPBTodaySnapshotSection description]
+ -[NTPBTodaySnapshotSection dictionaryRepresentation]
+ -[NTPBTodaySnapshotSection hasIdentifier]
+ -[NTPBTodaySnapshotSection hash]
+ -[NTPBTodaySnapshotSection identifier]
+ -[NTPBTodaySnapshotSection isEqual:]
+ -[NTPBTodaySnapshotSection itemsAtIndex:]
+ -[NTPBTodaySnapshotSection itemsCount]
+ -[NTPBTodaySnapshotSection items]
+ -[NTPBTodaySnapshotSection mergeFrom:]
+ -[NTPBTodaySnapshotSection readFrom:]
+ -[NTPBTodaySnapshotSection setIdentifier:]
+ -[NTPBTodaySnapshotSection setItems:]
+ -[NTPBTodaySnapshotSection writeTo:]
+ -[NTPBTodayWidgetConfig hasLiveCoverageActiveWindow]
+ -[NTPBTodayWidgetConfig liveCoverageActiveWindow]
+ -[NTPBTodayWidgetConfig setHasLiveCoverageActiveWindow:]
+ -[NTPBTodayWidgetConfig setLiveCoverageActiveWindow:]
+ OBJC_IVAR_$_NTPBArticleRecord._liveCoverageModifiedDate
+ OBJC_IVAR_$_NTPBArticleTopic._isEligibleForFeaturePromotion
+ OBJC_IVAR_$_NTPBAsset._etag
+ OBJC_IVAR_$_NTPBAsset._expiresAt
+ OBJC_IVAR_$_NTPBForYouTodaySectionSpecificConfig._stabilizeAcrossRefreshes
+ OBJC_IVAR_$_NTPBPuzzleTypeRecord._feedNavDarkModeImageURL
+ OBJC_IVAR_$_NTPBReadingHistoryItem._clusterID
+ OBJC_IVAR_$_NTPBRecipeItem._has
+ OBJC_IVAR_$_NTPBRecipeItem._order
+ OBJC_IVAR_$_NTPBRecipeRecord._recipeRating
+ OBJC_IVAR_$_NTPBSportsEventRecord._sportsLogoAltImageCompactURL
+ OBJC_IVAR_$_NTPBSportsEventRecord._sportsLogoAltImageLargeURL
+ OBJC_IVAR_$_NTPBSportsEventRecord._sportsLogoAltImageURL
+ OBJC_IVAR_$_NTPBSportsEventRecord._sportsLogoImageCompactURL
+ OBJC_IVAR_$_NTPBSportsEventRecord._sportsLogoImageLargeURL
+ OBJC_IVAR_$_NTPBSportsEventRecord._sportsLogoImageURL
+ OBJC_IVAR_$_NTPBTagRecord._feedNavDarkModeImageHQURL
+ OBJC_IVAR_$_NTPBTagRecord._feedNavDarkModeImageURL
+ OBJC_IVAR_$_NTPBTagTodaySectionSpecificConfig._stabilizeAcrossRefreshes
+ OBJC_IVAR_$_NTPBTodayResultOperationInfo._lastEntrySnapshot
+ OBJC_IVAR_$_NTPBTodaySnapshot._sections
+ OBJC_IVAR_$_NTPBTodaySnapshotItem._identifier
+ OBJC_IVAR_$_NTPBTodaySnapshotSection._identifier
+ OBJC_IVAR_$_NTPBTodaySnapshotSection._items
+ OBJC_IVAR_$_NTPBTodayWidgetConfig._liveCoverageActiveWindow
+ _NTPBTodaySnapshotItemReadFrom
+ _NTPBTodaySnapshotReadFrom
+ _NTPBTodaySnapshotSectionReadFrom
+ _OBJC_CLASS_$_NTPBTodaySnapshot
+ _OBJC_CLASS_$_NTPBTodaySnapshotItem
+ _OBJC_CLASS_$_NTPBTodaySnapshotSection
+ _OBJC_METACLASS_$_NTPBTodaySnapshot
+ _OBJC_METACLASS_$_NTPBTodaySnapshotItem
+ _OBJC_METACLASS_$_NTPBTodaySnapshotSection
+ __OBJC_$_CLASS_METHODS_NTPBTodaySnapshot
+ __OBJC_$_CLASS_METHODS_NTPBTodaySnapshotSection
+ __OBJC_$_INSTANCE_METHODS_NTPBTodaySnapshot
+ __OBJC_$_INSTANCE_METHODS_NTPBTodaySnapshotItem
+ __OBJC_$_INSTANCE_METHODS_NTPBTodaySnapshotSection
+ __OBJC_$_INSTANCE_VARIABLES_NTPBTodaySnapshot
+ __OBJC_$_INSTANCE_VARIABLES_NTPBTodaySnapshotItem
+ __OBJC_$_INSTANCE_VARIABLES_NTPBTodaySnapshotSection
+ __OBJC_$_PROP_LIST_NTPBTodaySnapshot
+ __OBJC_$_PROP_LIST_NTPBTodaySnapshotItem
+ __OBJC_$_PROP_LIST_NTPBTodaySnapshotSection
+ __OBJC_CLASS_PROTOCOLS_$_NTPBTodaySnapshot
+ __OBJC_CLASS_PROTOCOLS_$_NTPBTodaySnapshotItem
+ __OBJC_CLASS_PROTOCOLS_$_NTPBTodaySnapshotSection
+ __OBJC_CLASS_RO_$_NTPBTodaySnapshot
+ __OBJC_CLASS_RO_$_NTPBTodaySnapshotItem
+ __OBJC_CLASS_RO_$_NTPBTodaySnapshotSection
+ __OBJC_METACLASS_RO_$_NTPBTodaySnapshot
+ __OBJC_METACLASS_RO_$_NTPBTodaySnapshotItem
+ __OBJC_METACLASS_RO_$_NTPBTodaySnapshotSection
+ _objc_msgSend$addSections:
+ _objc_msgSend$setFeedNavDarkModeImageHQURL:
+ _objc_msgSend$setFeedNavDarkModeImageURL:
+ _objc_msgSend$setLastEntrySnapshot:
+ _objc_msgSend$setLiveCoverageModifiedDate:
+ _objc_msgSend$setRecipeRating:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x22
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x8
CStrings:
+ "@\"NTPBTodaySnapshot\""
+ "NTPBTodaySnapshot"
+ "NTPBTodaySnapshotItem"
+ "NTPBTodaySnapshotSection"
+ "T"
+ "T@\"NSData\",&,N,V_recipeRating"
+ "T@\"NSMutableArray\",&,N,V_sections"
+ "T@\"NSString\",&,N,V_feedNavDarkModeImageHQURL"
+ "T@\"NSString\",&,N,V_feedNavDarkModeImageURL"
+ "T@\"NTPBDate\",&,N,V_liveCoverageModifiedDate"
+ "T@\"NTPBTodaySnapshot\",&,N,V_lastEntrySnapshot"
+ "TB,N,V_isEligibleForFeaturePromotion"
+ "TB,N,V_stabilizeAcrossRefreshes"
+ "Td,N,V_liveCoverageActiveWindow"
+ "Tq,N,V_order"
+ "_feedNavDarkModeImageHQURL"
+ "_feedNavDarkModeImageURL"
+ "_isEligibleForFeaturePromotion"
+ "_lastEntrySnapshot"
+ "_liveCoverageActiveWindow"
+ "_liveCoverageModifiedDate"
+ "_recipeRating"
+ "_sections"
+ "_stabilizeAcrossRefreshes"
+ "addSections:"
+ "clearSections"
+ "feedNavDarkModeImageHQURL"
+ "feedNavDarkModeImageURL"
+ "feed_nav_dark_mode_image_HQ_URL"
+ "feed_nav_dark_mode_image_URL"
+ "hasFeedNavDarkModeImageHQURL"
+ "hasFeedNavDarkModeImageURL"
+ "hasIsEligibleForFeaturePromotion"
+ "hasLastEntrySnapshot"
+ "hasLiveCoverageActiveWindow"
+ "hasLiveCoverageModifiedDate"
+ "hasRecipeRating"
+ "hasStabilizeAcrossRefreshes"
+ "isEligibleForFeaturePromotion"
+ "is_eligible_for_feature_promotion"
+ "lastEntrySnapshot"
+ "last_entry_snapshot"
+ "liveCoverageActiveWindow"
+ "liveCoverageModifiedDate"
+ "live_coverage_active_window"
+ "live_coverage_modified_date"
+ "recipeRating"
+ "recipe_rating"
+ "sections"
+ "sectionsAtIndex:"
+ "sectionsCount"
+ "sectionsType"
+ "setFeedNavDarkModeImageHQURL:"
+ "setFeedNavDarkModeImageURL:"
+ "setHasIsEligibleForFeaturePromotion:"
+ "setHasLiveCoverageActiveWindow:"
+ "setHasStabilizeAcrossRefreshes:"
+ "setIsEligibleForFeaturePromotion:"
+ "setLastEntrySnapshot:"
+ "setLiveCoverageActiveWindow:"
+ "setLiveCoverageModifiedDate:"
+ "setRecipeRating:"
+ "setSections:"
+ "setStabilizeAcrossRefreshes:"
+ "stabilizeAcrossRefreshes"
+ "stabilize_across_refreshes"
+ "{?=\"cutoffTime\"b1\"feedItemMaxCount\"b1\"feedMaxCount\"b1\"headlinesPerFeedFetchCount\"b1\"localNewsPromotionIndex\"b1\"minimumUpdateInterval\"b1\"subscriptionsFetchCount\"b1\"subscriptionsMinCount\"b1\"fetchingBin\"b1\"stabilizeAcrossRefreshes\"b1}"
+ "{?=\"cutoffTime\"b1\"headlinesPerFeedFetchCount\"b1\"minimumUpdateInterval\"b1\"fetchingBin\"b1\"stabilizeAcrossRefreshes\"b1}"
+ "{?=\"flowRate\"b1\"ontologyLevel\"b1\"quality\"b1\"subscriptionRate\"b1\"hardFollowRequiredForGrouping\"b1\"isDisallowedFromGrouping\"b1\"isEligibleForFeaturePromotion\"b1\"isEligibleForFoodGrouping\"b1\"isEligibleForFoodGroupingIfAutofavorited\"b1\"isEligibleForFoodGroupingIfFavorited\"b1\"isEligibleForGrouping\"b1\"isEligibleForGroupingIfAutofavorited\"b1\"isEligibleForGroupingIfFavorited\"b1\"isHidden\"b1\"isManagedTopic\"b1\"isManagedTopicWinner\"b1}"
+ "{?=\"liveCoverageActiveWindow\"b1\"minimumArticleExposureDurationToBePreseen\"b1\"prerollLoadingTimeout\"b1\"widgetSystemReloadInterval\"b1\"widgetSystemReloadJitterMax\"b1\"minimumNumberOfTimesPreseenToBeSeen\"b1\"contentPrefetchEnabled\"b1\"widgetBackgroundInteractionEnabled\"b1}"
- "D"
- "{?=\"cutoffTime\"b1\"feedItemMaxCount\"b1\"feedMaxCount\"b1\"headlinesPerFeedFetchCount\"b1\"localNewsPromotionIndex\"b1\"minimumUpdateInterval\"b1\"subscriptionsFetchCount\"b1\"subscriptionsMinCount\"b1\"fetchingBin\"b1}"
- "{?=\"cutoffTime\"b1\"headlinesPerFeedFetchCount\"b1\"minimumUpdateInterval\"b1\"fetchingBin\"b1}"
- "{?=\"flowRate\"b1\"ontologyLevel\"b1\"quality\"b1\"subscriptionRate\"b1\"hardFollowRequiredForGrouping\"b1\"isDisallowedFromGrouping\"b1\"isEligibleForFoodGrouping\"b1\"isEligibleForFoodGroupingIfAutofavorited\"b1\"isEligibleForFoodGroupingIfFavorited\"b1\"isEligibleForGrouping\"b1\"isEligibleForGroupingIfAutofavorited\"b1\"isEligibleForGroupingIfFavorited\"b1\"isHidden\"b1\"isManagedTopic\"b1\"isManagedTopicWinner\"b1}"
- "{?=\"minimumArticleExposureDurationToBePreseen\"b1\"prerollLoadingTimeout\"b1\"widgetSystemReloadInterval\"b1\"widgetSystemReloadJitterMax\"b1\"minimumNumberOfTimesPreseenToBeSeen\"b1\"contentPrefetchEnabled\"b1\"widgetBackgroundInteractionEnabled\"b1}"

```
