## NewsCore

> `/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore`

```diff

-3529.2.0.0.0
-  __TEXT.__text: 0x2bee0c
-  __TEXT.__auth_stubs: 0x1310
-  __TEXT.__objc_methlist: 0x28300
-  __TEXT.__const: 0x13e8
+3557.1.0.0.0
+  __TEXT.__text: 0x2c5740
+  __TEXT.__auth_stubs: 0x1360
+  __TEXT.__objc_methlist: 0x28c88
+  __TEXT.__const: 0x1408
   __TEXT.__swift5_typeref: 0x89
-  __TEXT.__cstring: 0x45440
-  __TEXT.__oslogstring: 0xed20
-  __TEXT.__gcc_except_tab: 0x350c
+  __TEXT.__cstring: 0x46093
+  __TEXT.__oslogstring: 0xef64
+  __TEXT.__gcc_except_tab: 0x362c
   __TEXT.__dlopen_cstrs: 0x11c
   __TEXT.__ustring: 0x122
-  __TEXT.__unwind_info: 0x97ec
-  __TEXT.__objc_classname: 0x6886
-  __TEXT.__objc_methname: 0x786f7
-  __TEXT.__objc_methtype: 0xb924
-  __TEXT.__objc_stubs: 0x30a60
-  __DATA_CONST.__got: 0x368
-  __DATA_CONST.__const: 0xfa00
-  __DATA_CONST.__objc_classlist: 0x18a8
+  __TEXT.__unwind_info: 0x9a9c
+  __TEXT.__objc_classname: 0x6a35
+  __TEXT.__objc_methname: 0x792f1
+  __TEXT.__objc_methtype: 0xbaac
+  __TEXT.__objc_stubs: 0x31120
+  __DATA_CONST.__got: 0x370
+  __DATA_CONST.__const: 0xfe38
+  __DATA_CONST.__objc_classlist: 0x1918
   __DATA_CONST.__objc_catlist: 0x268
-  __DATA_CONST.__objc_protolist: 0x6b0
+  __DATA_CONST.__objc_protolist: 0x6b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5f498
-  __DATA_CONST.__objc_selrefs: 0x12338
+  __DATA_CONST.__objc_const: 0x61250
+  __DATA_CONST.__objc_selrefs: 0x126d0
   __DATA_CONST.__objc_arraydata: 0xfc8
-  __AUTH_CONST.__const: 0x4590
-  __AUTH_CONST.__objc_const: 0x121d0
-  __AUTH_CONST.__cfstring: 0x28e60
+  __AUTH_CONST.__const: 0x4670
+  __AUTH_CONST.__objc_const: 0x12650
+  __AUTH_CONST.__cfstring: 0x29920
   __AUTH_CONST.__objc_intobj: 0x1308
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0xbe0
-  __AUTH_CONST.__objc_doubleobj: 0x100
-  __AUTH_CONST.__auth_got: 0x9a0
-  __AUTH.__objc_data: 0x3a20
+  __AUTH_CONST.__objc_doubleobj: 0x110
+  __AUTH_CONST.__auth_got: 0x9c8
+  __AUTH.__objc_data: 0x3ed0
   __DATA.__objc_protorefs: 0xa8
-  __DATA.__objc_classrefs: 0x1df8
-  __DATA.__objc_superrefs: 0x1318
-  __DATA.__objc_ivar: 0x3cd0
-  __DATA.__data: 0x50b8
+  __DATA.__objc_classrefs: 0x1e68
+  __DATA.__objc_superrefs: 0x1380
+  __DATA.__objc_ivar: 0x3e1c
+  __DATA.__data: 0x5118
   __DATA.__common: 0x8
   __DATA.__bss: 0x58
-  __DATA_DIRTY.__objc_ivar: 0xe70
-  __DATA_DIRTY.__objc_data: 0xbc70
+  __DATA_DIRTY.__objc_ivar: 0xeb8
+  __DATA_DIRTY.__objc_data: 0xbc20
   __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__common: 0x170
   __DATA_DIRTY.__bss: 0xe48

   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 62947CD6-44A0-32D9-994D-4C0C24792C8F
-  Functions: 17525
-  Symbols:   57037
-  CStrings:  32521
+  UUID: E8739C06-43EF-35DF-B1BA-B5E7B9A09C26
+  Functions: 17808
+  Symbols:   57910
+  CStrings:  32994
 
Symbols:
+ +[FCBaseURLConfiguration liveActivityBaseURLForConfiguration:]
+ +[FCBaseURLConfiguration puzzlesArchiveBaseURLForConfiguration:]
+ +[FCUserEventHistoryAggregateCounts empty]
+ +[FCUserEventHistoryAggregateStoreData empty]
+ +[FCUserEventHistoryEventCounts empty]
+ +[FCUserEventHistoryMetadata emptyWithSessionsOnDiskSize:personalizationAnalyticsEnabled:]
+ -[FCArticleHeadline isAIGenerated]
+ -[FCArticleHeadline reduceVisibilityForNonFollowers]
+ -[FCArticleHeadline setAiGenerated:]
+ -[FCBaseURLConfiguration puzzlesArchiveBaseURLForConfiguration]
+ -[FCChannelPaywallConfig .cxx_destruct]
+ -[FCChannelPaywallConfig articleSoftPaywallPositionForPaidBundleSubscribers]
+ -[FCChannelPaywallConfig articleSoftPaywallPosition]
+ -[FCChannelPaywallConfig channelID]
+ -[FCChannelPaywallConfig filterALaCartePaidArticlesForPaidBundleSubscribers]
+ -[FCChannelPaywallConfig initWithChannelID:configDictionary:]
+ -[FCCloudContext _createESLInventory]
+ -[FCESLInventory _childInventories]
+ -[FCESLInventory _enumerateChildInventories:]
+ -[FCESLInventory globalInventory]
+ -[FCESLInventory initWithGlobalInventory:tagInventory:]
+ -[FCESLInventory prewarmScoreCache:configuration:]
+ -[FCESLInventory refreshIfNeededWithCompletion:]
+ -[FCESLInventory tagInventory]
+ -[FCEditorialTopicEventMappingProperty .cxx_destruct]
+ -[FCEditorialTopicEventMappingProperty initWithDictionary:]
+ -[FCEditorialTopicEventMappingProperty mappingType]
+ -[FCEndpointConfiguration initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:puzzlesArchiveAPIBaseURLString:appAnalyticsNotificationReceiptBaseURLString:authTokenAPIBaseURLString:sportsDataVisualizationAPIBaseURLString:fineGrainedNewsletterSubscriptionBaseURLString:appAnalyticsSportsEventsBaseURLString:appAnalyticsAppHealthBaseURLString:ckOrderFeedBaseURLString:ckMultiFetchBaseURLString:ckRecordFetchBaseURLString:ckEdgeCachedOrderFeedBaseURLString:ckEdgeCachedMultiFetchBaseURLString:]
+ -[FCEndpointConfiguration puzzlesArchiveAPIBaseURLString]
+ -[FCFeedDescriptor referringFeedItemIdentifier]
+ -[FCFeedDescriptor setReferringFeedItemIdentifier:]
+ -[FCFeedItemInventory .cxx_destruct]
+ -[FCFeedItemInventory _adoptInventory:]
+ -[FCFeedItemInventory _isRefreshNeeded]
+ -[FCFeedItemInventory _loadInventoryFromCache]
+ -[FCFeedItemInventory _populateScoreProfilesForFeedItems:]
+ -[FCFeedItemInventory _populateScoreProfilesForFeedItems:configurationSet:]
+ -[FCFeedItemInventory _prepareForUse]
+ -[FCFeedItemInventory _refreshIfNeededWithQoS:]
+ -[FCFeedItemInventory _refreshIfNeeded]
+ -[FCFeedItemInventory _rescoreInventoryIfNeeded:forScoringVersion:]
+ -[FCFeedItemInventory allFeedItemScoreProfilesForConfigurationSet:scoringVersion:]
+ -[FCFeedItemInventory allFeedItemsWithTopic:]
+ -[FCFeedItemInventory allFeedItems]
+ -[FCFeedItemInventory context]
+ -[FCFeedItemInventory feedItemService]
+ -[FCFeedItemInventory feedItemsRefreshSerialQueue]
+ -[FCFeedItemInventory filePath]
+ -[FCFeedItemInventory initWithContext:feedItemService:filePath:version:refreshInterval:loggingKey:]
+ -[FCFeedItemInventory init]
+ -[FCFeedItemInventory latestInventory]
+ -[FCFeedItemInventory loadFromCacheOnce]
+ -[FCFeedItemInventory loggingKey]
+ -[FCFeedItemInventory refreshIfNeededWithCompletion:]
+ -[FCFeedItemInventory refreshInterval]
+ -[FCFeedItemInventory setLatestInventory:]
+ -[FCFeedItemInventory version]
+ -[FCFeedRequestOperation _reportProgressWithFeedItems:]
+ -[FCFeedRequestOperation progressHandler]
+ -[FCFeedRequestOperation setProgressHandler:]
+ -[FCGlobalCuratedESLArticlesOperation .cxx_destruct]
+ -[FCGlobalCuratedESLArticlesOperation completionHandler]
+ -[FCGlobalCuratedESLArticlesOperation initWithContext:configuration:bundleSubscriptionManager:]
+ -[FCGlobalCuratedESLArticlesOperation init]
+ -[FCGlobalCuratedESLArticlesOperation networkEvents]
+ -[FCGlobalCuratedESLArticlesOperation operationWillFinishWithError:]
+ -[FCGlobalCuratedESLArticlesOperation performOperation]
+ -[FCGlobalCuratedESLArticlesOperation prepareOperation]
+ -[FCGlobalCuratedESLArticlesOperation setCompletionHandler:]
+ -[FCGlobalESLService .cxx_destruct]
+ -[FCGlobalESLService _promiseConfiguration]
+ -[FCGlobalESLService _promiseCuratedFeedItemsWithConfiguration:]
+ -[FCGlobalESLService _promiseFeedItemsWithIssues:configuration:]
+ -[FCGlobalESLService _promiseIssueFeedItemsWithConfiguration:]
+ -[FCGlobalESLService _promiseIssuesWithConfiguration:]
+ -[FCGlobalESLService context]
+ -[FCGlobalESLService fetchFeedItemsWithCompletion:]
+ -[FCGlobalESLService initWithContext:]
+ -[FCGlobalESLService init]
+ -[FCHeadline isAIGenerated]
+ -[FCHeadline reduceVisibilityForNonFollowers]
+ -[FCHeadline setAiGenerated:]
+ -[FCLocalAreasMapping tagIDsForLocation:searchOption:]
+ -[FCLocalRegion centerLocationCoordinateForEntireRegion]
+ -[FCLocationSharingUpsellConfig initWithConfigDictionary:]
+ -[FCLocationSharingUpsellConfig landingPageArticleID]
+ -[FCLocationSharingUpsellConfig setLandingPageArticleID:]
+ -[FCMTWriterLock readBool:]
+ -[FCMTWriterLock readObject:]
+ -[FCMyArticlesOperation progressHandler]
+ -[FCMyArticlesOperation setProgressHandler:]
+ -[FCNewsAppConfig channelPaywallConfigsByChannelID]
+ -[FCNewsAppConfig editorialTopicEventMappingProperties]
+ -[FCNewsAppConfig freeGlobalESLArticleListIDs]
+ -[FCNewsAppConfig freeTagESLArticleListIDPrefix]
+ -[FCNewsAppConfig liveActivitiesEnabled]
+ -[FCNewsAppConfig liveActivityAssetServerURLs]
+ -[FCNewsAppConfig locationSharingUpsellConfig]
+ -[FCNewsAppConfig maxTagESLArticleListsToQuery]
+ -[FCNewsAppConfig moreFromIssueEOAEnabled]
+ -[FCNewsAppConfig moreToReadEOAEnabled]
+ -[FCNewsAppConfig paidGlobalESLArticleListIDs]
+ -[FCNewsAppConfig paidTagESLArticleListIDPrefix]
+ -[FCNewsAppConfig personalizationAnalyticsEnabled]
+ -[FCNewsAppConfig sportsSyncingConfigurationV2ResourceId]
+ -[FCNewsAppConfig sportsSyncingV2Enabled]
+ -[FCNewsAppConfig sportsTopStoriesTagID]
+ -[FCNewsAppConfig tagSubscriptionRepromptDelay]
+ -[FCNewsAppConfig todayFeedEditionConfigJSON]
+ -[FCNewsAppConfig webEmbedDataSourcesConfigurationResourceId]
+ -[FCNewsTabiChannelPickerSuggestionsConfiguration filterLocationSuggestionsOnlyToAppleNewsLocal]
+ -[FCNewsTabiChannelPickerSuggestionsConfiguration setFilterLocationSuggestionsOnlyToAppleNewsLocal:]
+ -[FCNewsTabiChannelPickerSuggestionsInputOutputConfiguration setDictionary:]
+ -[FCNewsTabiConfiguration setDictionary:]
+ -[FCNewsTabiEventAggregationOutputConfiguration setDictionary:]
+ -[FCNewsletterManager activeiTunesAccountName]
+ -[FCNewsletterManager setActiveiTunesAccountName:]
+ -[FCNotificationArticleHeadline reduceVisibilityForNonFollowers]
+ -[FCPBFeedItemInventory addFeedItems:]
+ -[FCPBFeedItemInventory copyWithZone:]
+ -[FCPBFeedItemInventory dealloc]
+ -[FCPBFeedItemInventory description]
+ -[FCPBFeedItemInventory dictionaryRepresentation]
+ -[FCPBFeedItemInventory feedItemVersion]
+ -[FCPBFeedItemInventory feedItems]
+ -[FCPBFeedItemInventory hash]
+ -[FCPBFeedItemInventory inventoryVersion]
+ -[FCPBFeedItemInventory isEqual:]
+ -[FCPBFeedItemInventory lastRefreshed]
+ -[FCPBFeedItemInventory readFrom:]
+ -[FCPBFeedItemInventory setFeedItemVersion:]
+ -[FCPBFeedItemInventory setFeedItems:]
+ -[FCPBFeedItemInventory setInventoryVersion:]
+ -[FCPBFeedItemInventory setLastRefreshed:]
+ -[FCPBFeedItemInventory writeTo:]
+ -[FCPaidBundleConfiguration aLaCarteArticleSoftPaywallPosition]
+ -[FCPaidBundleConfiguration articleSoftPaywallPosition]
+ -[FCPersonalizationTreatment affinityGroupOntologyLevelConfig]
+ -[FCPersonalizationTreatment affinityGroupScoringConfig]
+ -[FCPersonalizationTreatment affinityGroupTopicsConfig]
+ -[FCPersonalizationTreatment shadowAffinityGroupOntologyLevelConfig]
+ -[FCPersonalizationTreatment shadowAffinityGroupScoringConfig]
+ -[FCPersonalizationTreatment shadowAffinityGroupTopicsConfig]
+ -[FCProxyHeadline routeURL]
+ -[FCPuzzle initWithIdentifier:title:subtitle:puzzleDescription:puzzleType:dataResourceID:authors:publishDate:isPaid:difficulty:difficultyDescription:thumbnailLargeImageAssetHandle:loadDate:teaserClue:teaserAnswer:teaserInfo:teaserDirection:teaserNumber:language:blockedStorefrontIDs:allowedStorefrontIDs:minimumNewsVersion:showInfoModalOnFirstPlay:isDeprecated:isDraft:lastModifiedDate:]
+ -[FCPuzzle lastModifiedDate]
+ -[FCPuzzleController createPuzzleForPuzzleType:identifier:title:subtitle:puzzleDescription:dataResourceID:authors:behaviorFlags:publishDate:isPaid:difficulty:difficultyDescription:thumbnailLargeURL:loadDate:teaserClue:teaserAnswer:teaserInfo:teaserDirection:teaserNumber:language:blockedStorefrontIDs:allowedStorefrontIDs:minimumNewsVersion:isDeprecated:isDraft:lastModifiedDate:]
+ -[FCPuzzleController savePuzzleToCache:]
+ -[FCPuzzleFullArchiveMenuOptionItem .cxx_destruct]
+ -[FCPuzzleFullArchiveMenuOptionItem difficultyIndex]
+ -[FCPuzzleFullArchiveMenuOptionItem icon]
+ -[FCPuzzleFullArchiveMenuOptionItem initWithTitle:icon:level:difficultyIndex:]
+ -[FCPuzzleFullArchiveMenuOptionItem level]
+ -[FCPuzzleFullArchiveMenuOptionItem title]
+ -[FCPuzzleFullArchiveMenuOptionsConfiguration .cxx_destruct]
+ -[FCPuzzleFullArchiveMenuOptionsConfiguration icon]
+ -[FCPuzzleFullArchiveMenuOptionsConfiguration initWithConfigDictionary:]
+ -[FCPuzzleFullArchiveMenuOptionsConfiguration items]
+ -[FCPuzzleFullArchiveMenuOptionsConfiguration title]
+ -[FCPuzzleFullArchiveMenuOptionsConfiguration type]
+ -[FCPuzzleThumbnailHandle downloadIfNeededWithGroup:completion:]
+ -[FCPuzzleType hasEvergreenArticleList]
+ -[FCPuzzlesConfiguration puzzleFullArchiveMenuOptionsConfigByPuzzleTypeID]
+ -[FCPuzzlesConfiguration puzzleFullArchiveTagID]
+ -[FCPuzzlesConfiguration puzzlesArchiveAPIEnabled]
+ -[FCPuzzlesConfiguration puzzlesCacheLifetime]
+ -[FCPuzzlesConfiguration recentPuzzlesCacheLifetime]
+ -[FCSingleTagFeedDescriptor initWithContext:tag:feedConfiguration:referringFeedItemIdentifier:]
+ -[FCSingleTagFeedDescriptor initWithContext:tag:sortMethod:filterOptions:personalizationConfigurationSet:feedConfiguration:referringFeedItemIdentifier:]
+ -[FCSingleTagFeedDescriptor referringFeedItemIdentifier]
+ -[FCSingleTagFeedDescriptor setReferringFeedItemIdentifier:]
+ -[FCSportsData setSportsSecondaryShortName:]
+ -[FCSportsData sportsSecondaryShortName]
+ -[FCSportsEvent hasEvergreenArticleList]
+ -[FCSportsEvent sportsLogoAltImageAssetHandle]
+ -[FCSportsEvent sportsLogoAltImageCompactAssetHandle]
+ -[FCSportsEvent sportsLogoAltImageLargeAssetHandle]
+ -[FCSportsEvent sportsParentTagIdentifiers]
+ -[FCSportsEvent sportsSecondaryShortName]
+ -[FCTag hasEvergreenArticleList]
+ -[FCTag sportsLogoAltImageAssetHandle]
+ -[FCTag sportsLogoAltImageCompactAssetHandle]
+ -[FCTag sportsLogoAltImageLargeAssetHandle]
+ -[FCTag sportsParentTagIdentifiers]
+ -[FCTag sportsSecondaryShortName]
+ -[FCTagCuratedESLArticlesOperation .cxx_destruct]
+ -[FCTagCuratedESLArticlesOperation completionHandler]
+ -[FCTagCuratedESLArticlesOperation initWithTags:context:configuration:bundleSubscriptionManager:]
+ -[FCTagCuratedESLArticlesOperation init]
+ -[FCTagCuratedESLArticlesOperation networkEvents]
+ -[FCTagCuratedESLArticlesOperation operationWillFinishWithError:]
+ -[FCTagCuratedESLArticlesOperation performOperation]
+ -[FCTagCuratedESLArticlesOperation prepareOperation]
+ -[FCTagCuratedESLArticlesOperation setCompletionHandler:]
+ -[FCTagESLService .cxx_destruct]
+ -[FCTagESLService _promiseConfiguration]
+ -[FCTagESLService _promiseCuratedFeedItemsForTags:configuration:]
+ -[FCTagESLService _promiseRelevantTagsWithConfiguration:]
+ -[FCTagESLService context]
+ -[FCTagESLService fetchFeedItemsWithCompletion:]
+ -[FCTagESLService initWithContext:]
+ -[FCTagESLService init]
+ -[FCTagMetadata sportsSecondaryShortName]
+ -[FCTopKESLService .cxx_destruct]
+ -[FCTopKESLService _promiseConfiguration]
+ -[FCTopKESLService _promiseFeedItemsForTags:configuration:]
+ -[FCTopKESLService _promiseRelevantTagsWithConfiguration:]
+ -[FCTopKESLService context]
+ -[FCTopKESLService fetchFeedItemsWithCompletion:]
+ -[FCTopKESLService initWithContext:]
+ -[FCTopKESLService init]
+ -[FCUserEventHistoryAggregateCounts channelTopic]
+ -[FCUserEventHistoryAggregateCounts group]
+ -[FCUserEventHistoryAggregateCounts setChannelTopic:]
+ -[FCUserEventHistoryAggregateCounts setGroup:]
+ -[FCUserEventHistoryAggregateCounts setTag:]
+ -[FCUserEventHistoryAggregateCounts tag]
+ -[FCUserEventHistoryAggregateStoreData .cxx_destruct]
+ -[FCUserEventHistoryAggregateStoreData aggregateCounts]
+ -[FCUserEventHistoryAggregateStoreData baselineStatelessEventCount]
+ -[FCUserEventHistoryAggregateStoreData baselineTimestamp]
+ -[FCUserEventHistoryAggregateStoreData baselineTotalEventCount]
+ -[FCUserEventHistoryAggregateStoreData init]
+ -[FCUserEventHistoryAggregateStoreData setAggregateCounts:]
+ -[FCUserEventHistoryAggregateStoreData setBaselineStatelessEventCount:]
+ -[FCUserEventHistoryAggregateStoreData setBaselineTimestamp:]
+ -[FCUserEventHistoryAggregateStoreData setBaselineTotalEventCount:]
+ -[FCUserEventHistoryEventCounts articleDislikedEventCount]
+ -[FCUserEventHistoryEventCounts articleLikedEventCount]
+ -[FCUserEventHistoryEventCounts articleReadEventCount]
+ -[FCUserEventHistoryEventCounts articleSavedEventCount]
+ -[FCUserEventHistoryEventCounts articleSeenEventCount]
+ -[FCUserEventHistoryEventCounts articleSharedEventCount]
+ -[FCUserEventHistoryEventCounts articleVisitedEventCount]
+ -[FCUserEventHistoryEventCounts description]
+ -[FCUserEventHistoryEventCounts feedViewEventCount]
+ -[FCUserEventHistoryEventCounts initWithArticleSeenEventCount:articleVisitedEventCount:articleReadEventCount:articleLikedEventCount:articleDislikedEventCount:articleSharedEventCount:articleSavedEventCount:feedViewEventCount:tagFollowedEventCount:tagUnfollowedEventCount:tagMutedEventCount:]
+ -[FCUserEventHistoryEventCounts setArticleDislikedEventCount:]
+ -[FCUserEventHistoryEventCounts setArticleLikedEventCount:]
+ -[FCUserEventHistoryEventCounts setArticleReadEventCount:]
+ -[FCUserEventHistoryEventCounts setArticleSavedEventCount:]
+ -[FCUserEventHistoryEventCounts setArticleSeenEventCount:]
+ -[FCUserEventHistoryEventCounts setArticleSharedEventCount:]
+ -[FCUserEventHistoryEventCounts setArticleVisitedEventCount:]
+ -[FCUserEventHistoryEventCounts setFeedViewEventCount:]
+ -[FCUserEventHistoryEventCounts setTagFollowedEventCount:]
+ -[FCUserEventHistoryEventCounts setTagMutedEventCount:]
+ -[FCUserEventHistoryEventCounts setTagUnfollowedEventCount:]
+ -[FCUserEventHistoryEventCounts tagFollowedEventCount]
+ -[FCUserEventHistoryEventCounts tagMutedEventCount]
+ -[FCUserEventHistoryEventCounts tagUnfollowedEventCount]
+ -[FCUserEventHistoryMetadata .cxx_destruct]
+ -[FCUserEventHistoryMetadata aggregateStoreData]
+ -[FCUserEventHistoryMetadata eventCounts]
+ -[FCUserEventHistoryMetadata initWithAggregateStoreGenerationTime:aggregateTotalCount:meanCountOfEvents:sessionsOnDiskSize:standardDeviationOfEvents:totalEventsCount:headlineEventCount:headlinesWithValidTitleEmbeddingsEventCount:headlinesWithInvalidTitleEmbeddingsEventCount:headlinesWithValidBodyEmbeddingsEventCount:headlinesWithInvalidBodyEmbeddingsEventCount:eventCounts:aggregateStoreData:]
+ -[FCUserEventHistoryMetadata setAggregateStoreData:]
+ -[FCUserEventHistoryMetadata setEventCounts:]
+ -[FCUserEventHistoryStorage configurationManager]
+ -[FCUserEventHistoryStorage initWithPrivateDataDirectory:configurationManager:]
+ -[FCUserEventHistoryStorage setConfigurationManager:]
+ -[FCUserEventHistoryStorage setMetadataWithAggregateStoreGenerationTime:aggregateTotalCount:meanCountOfEvents:standardDeviationOfEvents:totalEventsCount:headlineEventCount:headlinesWithValidTitleEmbeddingsEventCount:headlinesWithInvalidTitleEmbeddingsEventCount:headlinesWithValidBodyEmbeddingsEventCount:headlinesWithInvalidBodyEmbeddingsEventCount:eventCounts:aggregateStoreData:]
+ -[NTPBTagRecord(FCAdditions) generateSportsLogoAltImageAssetHandleWithAssetManager:]
+ -[NTPBTagRecord(FCAdditions) generateSportsLogoAltImageCompactAssetHandleWithAssetManager:]
+ -[NTPBTagRecord(FCAdditions) generateSportsLogoAltImageLargeAssetHandleWithAssetManager:]
+ GCC_except_table115
+ GCC_except_table126
+ GCC_except_table131
+ GCC_except_table137
+ _.str.112
+ _AMSErrorDomain
+ _CGRectGetMidX
+ _CGRectGetMidY
+ _CLLocationCoordinate2DMake
+ _FCCKTagPropertyFlagsLocalizedKey
+ _FCCKTagSportsLogoAltImageCompactKey
+ _FCCKTagSportsLogoAltImageKey
+ _FCCKTagSportsLogoAltImageLargeKey
+ _FCClearGlobalESLNextLaunchSharedPreferenceKey
+ _FCClearPerTagESLNextLaunchSharedPreferenceKey
+ _FCDefaultPuzzlesArchiveBaseURLStringForEnvironment
+ _FCEnableAIAttribution
+ _FCPBFeedItemInventoryReadFrom
+ _FCSimulatePerTagESLWithTopKSharedPreferenceKey
+ _FCTagAdjustName
+ _FCTagURLSubscriptionPromptDatesKey
+ _NTPBDateReadFrom
+ _NTPBFeedItemReadFrom
+ _OBJC_CLASS_$_CLLocation
+ _OBJC_CLASS_$_FCChannelPaywallConfig
+ _OBJC_CLASS_$_FCEditorialTopicEventMappingProperty
+ _OBJC_CLASS_$_FCFeedItemInventory
+ _OBJC_CLASS_$_FCGlobalCuratedESLArticlesOperation
+ _OBJC_CLASS_$_FCGlobalESLService
+ _OBJC_CLASS_$_FCLocationSharingUpsellConfig
+ _OBJC_CLASS_$_FCPBFeedItemInventory
+ _OBJC_CLASS_$_FCPuzzleFullArchiveMenuOptionItem
+ _OBJC_CLASS_$_FCPuzzleFullArchiveMenuOptionsConfiguration
+ _OBJC_CLASS_$_FCTagCuratedESLArticlesOperation
+ _OBJC_CLASS_$_FCTagESLService
+ _OBJC_CLASS_$_FCTopKESLService
+ _OBJC_CLASS_$_FCUserEventHistoryAggregateCounts
+ _OBJC_CLASS_$_FCUserEventHistoryAggregateStoreData
+ _OBJC_CLASS_$_FCUserEventHistoryEventCounts
+ _OBJC_IVAR_$_FCArticleHeadline._isEvergreen
+ _OBJC_IVAR_$_FCArticleHeadline._reduceVisibilityForNonFollowers
+ _OBJC_IVAR_$_FCChannelPaywallConfig._articleSoftPaywallPosition
+ _OBJC_IVAR_$_FCChannelPaywallConfig._articleSoftPaywallPositionForPaidBundleSubscribers
+ _OBJC_IVAR_$_FCChannelPaywallConfig._channelID
+ _OBJC_IVAR_$_FCChannelPaywallConfig._filterALaCartePaidArticlesForPaidBundleSubscribers
+ _OBJC_IVAR_$_FCESLInventory._globalInventory
+ _OBJC_IVAR_$_FCESLInventory._tagInventory
+ _OBJC_IVAR_$_FCEditorialTopicEventMappingProperty._mappingType
+ _OBJC_IVAR_$_FCEndpointConfiguration._puzzlesArchiveAPIBaseURLString
+ _OBJC_IVAR_$_FCFeedDescriptor._referringFeedItemIdentifier
+ _OBJC_IVAR_$_FCFeedItemInventory._context
+ _OBJC_IVAR_$_FCFeedItemInventory._feedItemService
+ _OBJC_IVAR_$_FCFeedItemInventory._feedItemsRefreshSerialQueue
+ _OBJC_IVAR_$_FCFeedItemInventory._filePath
+ _OBJC_IVAR_$_FCFeedItemInventory._latestInventory
+ _OBJC_IVAR_$_FCFeedItemInventory._loadFromCacheOnce
+ _OBJC_IVAR_$_FCFeedItemInventory._loggingKey
+ _OBJC_IVAR_$_FCFeedItemInventory._refreshInterval
+ _OBJC_IVAR_$_FCFeedItemInventory._version
+ _OBJC_IVAR_$_FCGlobalESLService._context
+ _OBJC_IVAR_$_FCHeadline._aiGenerated
+ _OBJC_IVAR_$_FCHeadline._reduceVisibilityForNonFollowers
+ _OBJC_IVAR_$_FCLocationSharingUpsellConfig._landingPageArticleID
+ _OBJC_IVAR_$_FCNewsAppConfig._channelPaywallConfigsByChannelID
+ _OBJC_IVAR_$_FCNewsAppConfig._locationSharingUpsellConfig
+ _OBJC_IVAR_$_FCNewsAppConfig._sportsTopStoriesTagID
+ _OBJC_IVAR_$_FCNewsTabiChannelPickerSuggestionsConfiguration._filterLocationSuggestionsOnlyToAppleNewsLocal
+ _OBJC_IVAR_$_FCNewsTabiChannelPickerSuggestionsInputOutputConfiguration._dictionary
+ _OBJC_IVAR_$_FCNewsTabiConfiguration._dictionary
+ _OBJC_IVAR_$_FCNewsTabiEventAggregationConditions._dictionary
+ _OBJC_IVAR_$_FCNewsTabiEventAggregationOutputConfiguration._dictionary
+ _OBJC_IVAR_$_FCNewsletterManager._activeiTunesAccountName
+ _OBJC_IVAR_$_FCPaidBundleConfiguration._aLaCarteArticleSoftPaywallPosition
+ _OBJC_IVAR_$_FCPaidBundleConfiguration._articleSoftPaywallPosition
+ _OBJC_IVAR_$_FCPersonalizationTreatment._affinityGroupOntologyLevelConfig
+ _OBJC_IVAR_$_FCPersonalizationTreatment._affinityGroupScoringConfig
+ _OBJC_IVAR_$_FCPersonalizationTreatment._affinityGroupTopicsConfig
+ _OBJC_IVAR_$_FCPersonalizationTreatment._shadowAffinityGroupOntologyLevelConfig
+ _OBJC_IVAR_$_FCPersonalizationTreatment._shadowAffinityGroupScoringConfig
+ _OBJC_IVAR_$_FCPersonalizationTreatment._shadowAffinityGroupTopicsConfig
+ _OBJC_IVAR_$_FCPuzzle._lastModifiedDate
+ _OBJC_IVAR_$_FCPuzzleFullArchiveMenuOptionItem._difficultyIndex
+ _OBJC_IVAR_$_FCPuzzleFullArchiveMenuOptionItem._icon
+ _OBJC_IVAR_$_FCPuzzleFullArchiveMenuOptionItem._level
+ _OBJC_IVAR_$_FCPuzzleFullArchiveMenuOptionItem._title
+ _OBJC_IVAR_$_FCPuzzleFullArchiveMenuOptionsConfiguration._icon
+ _OBJC_IVAR_$_FCPuzzleFullArchiveMenuOptionsConfiguration._items
+ _OBJC_IVAR_$_FCPuzzleFullArchiveMenuOptionsConfiguration._title
+ _OBJC_IVAR_$_FCPuzzleFullArchiveMenuOptionsConfiguration._type
+ _OBJC_IVAR_$_FCPuzzlesConfiguration._puzzleFullArchiveMenuOptionsConfigByPuzzleTypeID
+ _OBJC_IVAR_$_FCPuzzlesConfiguration._puzzleFullArchiveTagID
+ _OBJC_IVAR_$_FCPuzzlesConfiguration._puzzlesArchiveAPIEnabled
+ _OBJC_IVAR_$_FCPuzzlesConfiguration._puzzlesCacheLifetime
+ _OBJC_IVAR_$_FCPuzzlesConfiguration._recentPuzzlesCacheLifetime
+ _OBJC_IVAR_$_FCSportsData._sportsSecondaryShortName
+ _OBJC_IVAR_$_FCSportsEvent._sportsLogoAltImageAssetHandle
+ _OBJC_IVAR_$_FCSportsEvent._sportsLogoAltImageCompactAssetHandle
+ _OBJC_IVAR_$_FCSportsEvent._sportsLogoAltImageLargeAssetHandle
+ _OBJC_IVAR_$_FCSportsEvent._sportsSecondaryShortName
+ _OBJC_IVAR_$_FCTag._hasEvergreenArticleList
+ _OBJC_IVAR_$_FCTag._sportsLogoAltImageAssetHandle
+ _OBJC_IVAR_$_FCTag._sportsLogoAltImageCompactAssetHandle
+ _OBJC_IVAR_$_FCTag._sportsLogoAltImageLargeAssetHandle
+ _OBJC_IVAR_$_FCTag._sportsSecondaryShortName
+ _OBJC_IVAR_$_FCTagESLService._context
+ _OBJC_IVAR_$_FCTopKESLService._context
+ _OBJC_IVAR_$_FCUserEventHistoryAggregateCounts._channelTopic
+ _OBJC_IVAR_$_FCUserEventHistoryAggregateCounts._group
+ _OBJC_IVAR_$_FCUserEventHistoryAggregateCounts._tag
+ _OBJC_IVAR_$_FCUserEventHistoryAggregateStoreData._aggregateCounts
+ _OBJC_IVAR_$_FCUserEventHistoryAggregateStoreData._baselineStatelessEventCount
+ _OBJC_IVAR_$_FCUserEventHistoryAggregateStoreData._baselineTimestamp
+ _OBJC_IVAR_$_FCUserEventHistoryAggregateStoreData._baselineTotalEventCount
+ _OBJC_IVAR_$_FCUserEventHistoryEventCounts._articleDislikedEventCount
+ _OBJC_IVAR_$_FCUserEventHistoryEventCounts._articleLikedEventCount
+ _OBJC_IVAR_$_FCUserEventHistoryEventCounts._articleReadEventCount
+ _OBJC_IVAR_$_FCUserEventHistoryEventCounts._articleSavedEventCount
+ _OBJC_IVAR_$_FCUserEventHistoryEventCounts._articleSeenEventCount
+ _OBJC_IVAR_$_FCUserEventHistoryEventCounts._articleSharedEventCount
+ _OBJC_IVAR_$_FCUserEventHistoryEventCounts._articleVisitedEventCount
+ _OBJC_IVAR_$_FCUserEventHistoryEventCounts._feedViewEventCount
+ _OBJC_IVAR_$_FCUserEventHistoryEventCounts._tagFollowedEventCount
+ _OBJC_IVAR_$_FCUserEventHistoryEventCounts._tagMutedEventCount
+ _OBJC_IVAR_$_FCUserEventHistoryEventCounts._tagUnfollowedEventCount
+ _OBJC_IVAR_$_FCUserEventHistoryMetadata._aggregateStoreData
+ _OBJC_IVAR_$_FCUserEventHistoryMetadata._eventCounts
+ _OBJC_IVAR_$_FCUserEventHistoryStorage._configurationManager
+ _OBJC_METACLASS_$_FCChannelPaywallConfig
+ _OBJC_METACLASS_$_FCEditorialTopicEventMappingProperty
+ _OBJC_METACLASS_$_FCFeedItemInventory
+ _OBJC_METACLASS_$_FCGlobalCuratedESLArticlesOperation
+ _OBJC_METACLASS_$_FCGlobalESLService
+ _OBJC_METACLASS_$_FCLocationSharingUpsellConfig
+ _OBJC_METACLASS_$_FCPBFeedItemInventory
+ _OBJC_METACLASS_$_FCPuzzleFullArchiveMenuOptionItem
+ _OBJC_METACLASS_$_FCPuzzleFullArchiveMenuOptionsConfiguration
+ _OBJC_METACLASS_$_FCTagCuratedESLArticlesOperation
+ _OBJC_METACLASS_$_FCTagESLService
+ _OBJC_METACLASS_$_FCTopKESLService
+ _OBJC_METACLASS_$_FCUserEventHistoryAggregateCounts
+ _OBJC_METACLASS_$_FCUserEventHistoryAggregateStoreData
+ _OBJC_METACLASS_$_FCUserEventHistoryEventCounts
+ __OBJC_$_CLASS_METHODS_FCUserEventHistoryAggregateCounts
+ __OBJC_$_CLASS_METHODS_FCUserEventHistoryAggregateStoreData
+ __OBJC_$_CLASS_METHODS_FCUserEventHistoryEventCounts
+ __OBJC_$_CLASS_PROP_LIST_FCUserEventHistoryAggregateCounts
+ __OBJC_$_CLASS_PROP_LIST_FCUserEventHistoryAggregateStoreData
+ __OBJC_$_CLASS_PROP_LIST_FCUserEventHistoryEventCounts
+ __OBJC_$_INSTANCE_METHODS_FCChannelPaywallConfig
+ __OBJC_$_INSTANCE_METHODS_FCEditorialTopicEventMappingProperty
+ __OBJC_$_INSTANCE_METHODS_FCFeedItemInventory
+ __OBJC_$_INSTANCE_METHODS_FCGlobalCuratedESLArticlesOperation
+ __OBJC_$_INSTANCE_METHODS_FCGlobalESLService
+ __OBJC_$_INSTANCE_METHODS_FCLocationSharingUpsellConfig
+ __OBJC_$_INSTANCE_METHODS_FCPBFeedItemInventory
+ __OBJC_$_INSTANCE_METHODS_FCPuzzleFullArchiveMenuOptionItem
+ __OBJC_$_INSTANCE_METHODS_FCPuzzleFullArchiveMenuOptionsConfiguration
+ __OBJC_$_INSTANCE_METHODS_FCTagCuratedESLArticlesOperation
+ __OBJC_$_INSTANCE_METHODS_FCTagESLService
+ __OBJC_$_INSTANCE_METHODS_FCTopKESLService
+ __OBJC_$_INSTANCE_METHODS_FCUserEventHistoryAggregateCounts
+ __OBJC_$_INSTANCE_METHODS_FCUserEventHistoryAggregateStoreData
+ __OBJC_$_INSTANCE_METHODS_FCUserEventHistoryEventCounts
+ __OBJC_$_INSTANCE_VARIABLES_FCChannelPaywallConfig
+ __OBJC_$_INSTANCE_VARIABLES_FCEditorialTopicEventMappingProperty
+ __OBJC_$_INSTANCE_VARIABLES_FCFeedItemInventory
+ __OBJC_$_INSTANCE_VARIABLES_FCGlobalCuratedESLArticlesOperation
+ __OBJC_$_INSTANCE_VARIABLES_FCGlobalESLService
+ __OBJC_$_INSTANCE_VARIABLES_FCLocationSharingUpsellConfig
+ __OBJC_$_INSTANCE_VARIABLES_FCPBFeedItemInventory
+ __OBJC_$_INSTANCE_VARIABLES_FCPuzzleFullArchiveMenuOptionItem
+ __OBJC_$_INSTANCE_VARIABLES_FCPuzzleFullArchiveMenuOptionsConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_FCTagCuratedESLArticlesOperation
+ __OBJC_$_INSTANCE_VARIABLES_FCTagESLService
+ __OBJC_$_INSTANCE_VARIABLES_FCTopKESLService
+ __OBJC_$_INSTANCE_VARIABLES_FCUserEventHistoryAggregateCounts
+ __OBJC_$_INSTANCE_VARIABLES_FCUserEventHistoryAggregateStoreData
+ __OBJC_$_INSTANCE_VARIABLES_FCUserEventHistoryEventCounts
+ __OBJC_$_PROP_LIST_FCChannelPaywallConfig
+ __OBJC_$_PROP_LIST_FCEditorialTopicEventMappingProperty
+ __OBJC_$_PROP_LIST_FCFeedItemInventory
+ __OBJC_$_PROP_LIST_FCFeedItemInventoryType
+ __OBJC_$_PROP_LIST_FCGlobalCuratedESLArticlesOperation
+ __OBJC_$_PROP_LIST_FCGlobalESLService
+ __OBJC_$_PROP_LIST_FCLocationSharingUpsellConfig
+ __OBJC_$_PROP_LIST_FCNewsletterManager.305
+ __OBJC_$_PROP_LIST_FCPBFeedItemInventory
+ __OBJC_$_PROP_LIST_FCPuzzleFullArchiveMenuOptionItem
+ __OBJC_$_PROP_LIST_FCPuzzleFullArchiveMenuOptionsConfiguration
+ __OBJC_$_PROP_LIST_FCTagCuratedESLArticlesOperation
+ __OBJC_$_PROP_LIST_FCTagESLService
+ __OBJC_$_PROP_LIST_FCTopKESLService
+ __OBJC_$_PROP_LIST_FCUserEventHistoryAggregateCounts
+ __OBJC_$_PROP_LIST_FCUserEventHistoryAggregateStoreData
+ __OBJC_$_PROP_LIST_FCUserEventHistoryEventCounts
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FCFeedItemInventoryType
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FCFeedItemServiceType
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FCFeedItemInventoryType
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FCFeedItemServiceType
+ __OBJC_CLASS_PROTOCOLS_$_FCFeedItemInventory
+ __OBJC_CLASS_PROTOCOLS_$_FCGlobalESLService
+ __OBJC_CLASS_PROTOCOLS_$_FCPBFeedItemInventory
+ __OBJC_CLASS_PROTOCOLS_$_FCTagESLService
+ __OBJC_CLASS_PROTOCOLS_$_FCTopKESLService
+ __OBJC_CLASS_RO_$_FCChannelPaywallConfig
+ __OBJC_CLASS_RO_$_FCEditorialTopicEventMappingProperty
+ __OBJC_CLASS_RO_$_FCFeedItemInventory
+ __OBJC_CLASS_RO_$_FCGlobalCuratedESLArticlesOperation
+ __OBJC_CLASS_RO_$_FCGlobalESLService
+ __OBJC_CLASS_RO_$_FCLocationSharingUpsellConfig
+ __OBJC_CLASS_RO_$_FCPBFeedItemInventory
+ __OBJC_CLASS_RO_$_FCPuzzleFullArchiveMenuOptionItem
+ __OBJC_CLASS_RO_$_FCPuzzleFullArchiveMenuOptionsConfiguration
+ __OBJC_CLASS_RO_$_FCTagCuratedESLArticlesOperation
+ __OBJC_CLASS_RO_$_FCTagESLService
+ __OBJC_CLASS_RO_$_FCTopKESLService
+ __OBJC_CLASS_RO_$_FCUserEventHistoryAggregateCounts
+ __OBJC_CLASS_RO_$_FCUserEventHistoryAggregateStoreData
+ __OBJC_CLASS_RO_$_FCUserEventHistoryEventCounts
+ __OBJC_LABEL_PROTOCOL_$_FCFeedItemInventoryType
+ __OBJC_LABEL_PROTOCOL_$_FCFeedItemServiceType
+ __OBJC_METACLASS_RO_$_FCChannelPaywallConfig
+ __OBJC_METACLASS_RO_$_FCEditorialTopicEventMappingProperty
+ __OBJC_METACLASS_RO_$_FCFeedItemInventory
+ __OBJC_METACLASS_RO_$_FCGlobalCuratedESLArticlesOperation
+ __OBJC_METACLASS_RO_$_FCGlobalESLService
+ __OBJC_METACLASS_RO_$_FCLocationSharingUpsellConfig
+ __OBJC_METACLASS_RO_$_FCPBFeedItemInventory
+ __OBJC_METACLASS_RO_$_FCPuzzleFullArchiveMenuOptionItem
+ __OBJC_METACLASS_RO_$_FCPuzzleFullArchiveMenuOptionsConfiguration
+ __OBJC_METACLASS_RO_$_FCTagCuratedESLArticlesOperation
+ __OBJC_METACLASS_RO_$_FCTagESLService
+ __OBJC_METACLASS_RO_$_FCTopKESLService
+ __OBJC_METACLASS_RO_$_FCUserEventHistoryAggregateCounts
+ __OBJC_METACLASS_RO_$_FCUserEventHistoryAggregateStoreData
+ __OBJC_METACLASS_RO_$_FCUserEventHistoryEventCounts
+ __OBJC_PROTOCOL_$_FCFeedItemInventoryType
+ __OBJC_PROTOCOL_$_FCFeedItemServiceType
+ ___103-[FCSubscriptionController fetchAllTagsWithCallbackQueue:maximumCachedAge:qualityOfService:completion:]_block_invoke.391
+ ___103-[FCSubscriptionController fetchAllTagsWithCallbackQueue:maximumCachedAge:qualityOfService:completion:]_block_invoke_2.392
+ ___122-[FCSubscriptionController addAutoFavoriteSubscriptionForTagIDs:groupableSubscriptionForTagIDs:originProvider:completion:]_block_invoke.413
+ ___122-[FCSubscriptionController addAutoFavoriteSubscriptionForTagIDs:groupableSubscriptionForTagIDs:originProvider:completion:]_block_invoke.419
+ ___122-[FCSubscriptionController addAutoFavoriteSubscriptionForTagIDs:groupableSubscriptionForTagIDs:originProvider:completion:]_block_invoke.425
+ ___122-[FCSubscriptionController addAutoFavoriteSubscriptionForTagIDs:groupableSubscriptionForTagIDs:originProvider:completion:]_block_invoke_2.416
+ ___122-[FCSubscriptionController addAutoFavoriteSubscriptionForTagIDs:groupableSubscriptionForTagIDs:originProvider:completion:]_block_invoke_2.426
+ ___126-[FCPurchaseController verifyAccessTokenWithTagID:accessToken:consumedArticleCount:serialCompletion:callbackQueue:completion:]_block_invoke.237
+ ___126-[FCPurchaseController verifyAccessTokenWithTagID:accessToken:consumedArticleCount:serialCompletion:callbackQueue:completion:]_block_invoke.252
+ ___126-[FCPurchaseController verifyAccessTokenWithTagID:accessToken:consumedArticleCount:serialCompletion:callbackQueue:completion:]_block_invoke.255
+ ___126-[FCPurchaseController verifyAccessTokenWithTagID:accessToken:consumedArticleCount:serialCompletion:callbackQueue:completion:]_block_invoke_2.253
+ ___27-[FCMTWriterLock readBool:]_block_invoke
+ ___29-[FCMTWriterLock readObject:]_block_invoke
+ ___30-[FCESLInventory allFeedItems]_block_invoke
+ ___30-[FCESLInventory allFeedItems]_block_invoke_2
+ ___37-[FCCloudContext _createESLInventory]_block_invoke
+ ___37-[FCFeedItemInventory _prepareForUse]_block_invoke
+ ___380-[FCPuzzleController createPuzzleForPuzzleType:identifier:title:subtitle:puzzleDescription:dataResourceID:authors:behaviorFlags:publishDate:isPaid:difficulty:difficultyDescription:thumbnailLargeURL:loadDate:teaserClue:teaserAnswer:teaserInfo:teaserDirection:teaserNumber:language:blockedStorefrontIDs:allowedStorefrontIDs:minimumNewsVersion:isDeprecated:isDraft:lastModifiedDate:]_block_invoke
+ ___39-[FCFeedItemInventory _adoptInventory:]_block_invoke
+ ___40-[FCESLInventory allFeedItemsWithTopic:]_block_invoke_2
+ ___45-[FCFeedItemInventory allFeedItemsWithTopic:]_block_invoke
+ ___46-[FCFeedItemInventory _loadInventoryFromCache]_block_invoke
+ ___46-[FCFeedItemInventory _loadInventoryFromCache]_block_invoke.34
+ ___46-[FCFeedItemInventory _loadInventoryFromCache]_block_invoke.35
+ ___46-[FCFeedItemInventory _loadInventoryFromCache]_block_invoke.36
+ ___46-[FCNewsAppConfig liveActivityAssetServerURLs]_block_invoke
+ ___47-[FCFeedItemInventory _refreshIfNeededWithQoS:]_block_invoke
+ ___47-[FCFeedItemInventory _refreshIfNeededWithQoS:]_block_invoke.20
+ ___47-[FCFeedItemInventory _refreshIfNeededWithQoS:]_block_invoke_2
+ ___47-[FCFeedItemInventory _refreshIfNeededWithQoS:]_block_invoke_2.21
+ ___47-[FCFeedItemInventory _refreshIfNeededWithQoS:]_block_invoke_3
+ ___47-[FCFeedItemInventory _refreshIfNeededWithQoS:]_block_invoke_4
+ ___47-[FCFeedItemInventory _refreshIfNeededWithQoS:]_block_invoke_5
+ ___47-[FCFeedItemInventory _refreshIfNeededWithQoS:]_block_invoke_6
+ ___48-[FCESLInventory refreshIfNeededWithCompletion:]_block_invoke
+ ___48-[FCESLInventory refreshIfNeededWithCompletion:]_block_invoke_2
+ ___48-[FCESLInventory refreshIfNeededWithCompletion:]_block_invoke_3
+ ___48-[FCESLInventory refreshIfNeededWithCompletion:]_block_invoke_4
+ ___48-[FCTagESLService fetchFeedItemsWithCompletion:]_block_invoke
+ ___48-[FCTagESLService fetchFeedItemsWithCompletion:]_block_invoke_2
+ ___48-[FCTagESLService fetchFeedItemsWithCompletion:]_block_invoke_3
+ ___48-[FCTagESLService fetchFeedItemsWithCompletion:]_block_invoke_4
+ ___48-[FCTagESLService fetchFeedItemsWithCompletion:]_block_invoke_5
+ ___49-[FCTopKESLService fetchFeedItemsWithCompletion:]_block_invoke
+ ___49-[FCTopKESLService fetchFeedItemsWithCompletion:]_block_invoke_2
+ ___49-[FCTopKESLService fetchFeedItemsWithCompletion:]_block_invoke_3
+ ___49-[FCTopKESLService fetchFeedItemsWithCompletion:]_block_invoke_4
+ ___49-[FCTopKESLService fetchFeedItemsWithCompletion:]_block_invoke_5
+ ___50-[FCESLInventory prewarmScoreCache:configuration:]_block_invoke
+ ___51-[FCGlobalESLService fetchFeedItemsWithCompletion:]_block_invoke
+ ___51-[FCGlobalESLService fetchFeedItemsWithCompletion:]_block_invoke_2
+ ___51-[FCGlobalESLService fetchFeedItemsWithCompletion:]_block_invoke_3
+ ___51-[FCGlobalESLService fetchFeedItemsWithCompletion:]_block_invoke_4
+ ___51-[FCGlobalESLService fetchFeedItemsWithCompletion:]_block_invoke_5
+ ___51-[FCGlobalESLService fetchFeedItemsWithCompletion:]_block_invoke_6
+ ___52-[FCTagCuratedESLArticlesOperation performOperation]_block_invoke
+ ___52-[FCTagCuratedESLArticlesOperation performOperation]_block_invoke.22
+ ___52-[FCTagCuratedESLArticlesOperation performOperation]_block_invoke_2
+ ___52-[FCTagCuratedESLArticlesOperation performOperation]_block_invoke_3
+ ___52-[FCTagCuratedESLArticlesOperation performOperation]_block_invoke_4
+ ___52-[FCTagCuratedESLArticlesOperation performOperation]_block_invoke_5
+ ___52-[FCTagCuratedESLArticlesOperation performOperation]_block_invoke_6
+ ___52-[FCTagCuratedESLArticlesOperation performOperation]_block_invoke_7
+ ___52-[FCTagCuratedESLArticlesOperation prepareOperation]_block_invoke
+ ___52-[FCTagCuratedESLArticlesOperation prepareOperation]_block_invoke.16
+ ___52-[FCTagCuratedESLArticlesOperation prepareOperation]_block_invoke_4
+ ___53-[FCFeedItemInventory refreshIfNeededWithCompletion:]_block_invoke
+ ___53-[FCFeedItemInventory refreshIfNeededWithCompletion:]_block_invoke_2
+ ___54-[FCGlobalESLService _promiseIssuesWithConfiguration:]_block_invoke
+ ___54-[FCGlobalESLService _promiseIssuesWithConfiguration:]_block_invoke.16
+ ___54-[FCGlobalESLService _promiseIssuesWithConfiguration:]_block_invoke_2
+ ___54-[FCLocalAreasMapping tagIDsForLocation:searchOption:]_block_invoke
+ ___54-[FCLocalAreasMapping tagIDsForLocation:searchOption:]_block_invoke_2
+ ___54-[FCLocalAreasMapping tagIDsForLocation:searchOption:]_block_invoke_3
+ ___54-[FCLocalAreasMapping tagIDsForLocation:searchOption:]_block_invoke_4
+ ___54-[FCPrivateChannelMembershipController hasMemberships]_block_invoke
+ ___54-[FCSubscriptionController _saveReadableSubscriptions]_block_invoke.517
+ ___55-[FCFeedRequestOperation _reportProgressWithFeedItems:]_block_invoke_2
+ ___55-[FCGlobalCuratedESLArticlesOperation performOperation]_block_invoke
+ ___55-[FCGlobalCuratedESLArticlesOperation performOperation]_block_invoke.18
+ ___55-[FCGlobalCuratedESLArticlesOperation performOperation]_block_invoke_2
+ ___55-[FCGlobalCuratedESLArticlesOperation performOperation]_block_invoke_3
+ ___55-[FCGlobalCuratedESLArticlesOperation performOperation]_block_invoke_4
+ ___55-[FCGlobalCuratedESLArticlesOperation performOperation]_block_invoke_5
+ ___55-[FCGlobalCuratedESLArticlesOperation prepareOperation]_block_invoke
+ ___55-[FCNewsAppConfig editorialTopicEventMappingProperties]_block_invoke
+ ___56-[FCPrivateChannelMembershipController addItem:toStore:]_block_invoke
+ ___57-[FCTagESLService _promiseRelevantTagsWithConfiguration:]_block_invoke
+ ___57-[FCTagESLService _promiseRelevantTagsWithConfiguration:]_block_invoke_2
+ ___57-[FCTagESLService _promiseRelevantTagsWithConfiguration:]_block_invoke_3
+ ___57-[FCTagESLService _promiseRelevantTagsWithConfiguration:]_block_invoke_4
+ ___58-[FCTopKESLService _promiseRelevantTagsWithConfiguration:]_block_invoke
+ ___58-[FCTopKESLService _promiseRelevantTagsWithConfiguration:]_block_invoke_2
+ ___58-[FCTopKESLService _promiseRelevantTagsWithConfiguration:]_block_invoke_3
+ ___59-[FCTopKESLService _promiseFeedItemsForTags:configuration:]_block_invoke.25
+ ___59-[FCTopKESLService _promiseFeedItemsForTags:configuration:]_block_invoke_2
+ ___59-[FCTopKESLService _promiseFeedItemsForTags:configuration:]_block_invoke_2.26
+ ___59-[FCTopKESLService _promiseFeedItemsForTags:configuration:]_block_invoke_3
+ ___60-[FCPrivateChannelMembershipController isMemberOfChannelID:]_block_invoke_2
+ ___60-[FCPrivateChannelMembershipController membershipChannelIDs]_block_invoke_2
+ ___61-[FCPrivateChannelMembershipController removeItemWithItemID:]_block_invoke
+ ___62-[FCAssetManager _fetchDataProviderForAssetHandle:completion:]_block_invoke.62
+ ___62-[FCGlobalESLService _promiseIssueFeedItemsWithConfiguration:]_block_invoke
+ ___62-[FCGlobalESLService _promiseIssueFeedItemsWithConfiguration:]_block_invoke_2
+ ___63-[FCBaseURLConfiguration puzzlesArchiveBaseURLForConfiguration]_block_invoke
+ ___64-[FCAssetManager _populateRawFilePathForAssetHandle:completion:]_block_invoke.55
+ ___64-[FCAssetManager _populateRawFilePathForAssetHandle:completion:]_block_invoke_2.56
+ ___64-[FCGlobalESLService _promiseCuratedFeedItemsWithConfiguration:]_block_invoke
+ ___64-[FCGlobalESLService _promiseCuratedFeedItemsWithConfiguration:]_block_invoke.26
+ ___64-[FCGlobalESLService _promiseCuratedFeedItemsWithConfiguration:]_block_invoke_2
+ ___64-[FCGlobalESLService _promiseFeedItemsWithIssues:configuration:]_block_invoke
+ ___64-[FCGlobalESLService _promiseFeedItemsWithIssues:configuration:]_block_invoke.22
+ ___64-[FCGlobalESLService _promiseFeedItemsWithIssues:configuration:]_block_invoke_2
+ ___64-[FCPrivateChannelMembershipController loadLocalCachesFromStore]_block_invoke
+ ___64-[FCPuzzleThumbnailHandle downloadIfNeededWithGroup:completion:]_block_invoke
+ ___65-[FCPurchaseController addAppStoreDiscoveredChannelsToFavorites:]_block_invoke_2
+ ___65-[FCTagESLService _promiseCuratedFeedItemsForTags:configuration:]_block_invoke.22
+ ___65-[FCTagESLService _promiseCuratedFeedItemsForTags:configuration:]_block_invoke_2
+ ___65-[FCTagESLService _promiseCuratedFeedItemsForTags:configuration:]_block_invoke_2.23
+ ___67-[FCFeedItemInventory _rescoreInventoryIfNeeded:forScoringVersion:]_block_invoke
+ ___71-[FCCloudContext fetchShouldSecureSubscriptionsForDatabase:completion:]_block_invoke.198
+ ___71-[FCCloudContext fetchShouldSecureSubscriptionsForDatabase:completion:]_block_invoke_2.200
+ ___72-[FCArticleHeadline _adoptNarrativeTrackFromArticleRecord:assetManager:]_block_invoke.42
+ ___72-[FCArticleHeadline _adoptNarrativeTrackFromArticleRecord:assetManager:]_block_invoke.43
+ ___72-[FCPuzzleFullArchiveMenuOptionsConfiguration initWithConfigDictionary:]_block_invoke
+ ___73-[FCPrivateChannelMembershipController isAllowedToSeeDraftsForChannelID:]_block_invoke_2
+ ___75-[FCPaidBundleConfiguration arePaywallConfigsEqualToOtherPaidBundleConfig:]_block_invoke.29
+ ___76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke.172
+ ___76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke.181
+ ___76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke_2.173
+ ___76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke_2.183
+ ___77-[FCESLInventory allFeedItemScoreProfilesForConfigurationSet:scoringVersion:]_block_invoke
+ ___77-[FCPrivateChannelMembershipController feedDescriptorForDraftFeedForChannel:]_block_invoke
+ ___77-[FCPrivateChannelMembershipController referenceToMembershipForMembershipID:]_block_invoke
+ ___77-[FCPrivateChannelMembershipController referenceToMembershipForMembershipID:]_block_invoke_2
+ ___78-[FCPrivateChannelMembershipController isAllowedToSeeIssueID:completionBlock:]_block_invoke_3
+ ___79-[FCUserEventHistoryStorage initWithPrivateDataDirectory:configurationManager:]_block_invoke
+ ___79-[FCUserEventHistoryStorage initWithPrivateDataDirectory:configurationManager:]_block_invoke_2
+ ___80-[FCPrivateChannelMembershipController _refreshPublicMembershipsWithCompletion:]_block_invoke.58
+ ___80-[FCPrivateChannelMembershipController _refreshPublicMembershipsWithCompletion:]_block_invoke_2
+ ___80-[FCPrivateChannelMembershipController isAllowedToSeeArticleID:completionBlock:]_block_invoke_3
+ ___82-[FCPrivateChannelMembershipController allKnownRecordNamesWithinRecordZoneWithID:]_block_invoke_2
+ ___83-[FCMyArticlesOperation _fetchAllFeedItemsWithFeedRequests:feedContext:completion:]_block_invoke
+ ___83-[FCMyArticlesOperation _fetchAllFeedItemsWithFeedRequests:feedContext:completion:]_block_invoke_2
+ ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke.448
+ ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke_2.449
+ ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke_3.453
+ ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke_4.456
+ ___87-[FCCloudContext fetchOriginalDataShouldBeDeletedAfterMigrationForDatabase:completion:]_block_invoke.187
+ ___87-[FCCloudContext fetchOriginalDataShouldBeDeletedAfterMigrationForDatabase:completion:]_block_invoke_2.189
+ ___88-[FCGlobalCuratedESLArticlesOperation _feedItemsFromArticleRecords:sourceArticleListID:]_block_invoke
+ ___92-[FCPuzzlesConfiguration initWithConfigDictionary:storefrontID:defaultSupportedStorefronts:]_block_invoke
+ ___92-[FCPuzzlesConfiguration initWithConfigDictionary:storefrontID:defaultSupportedStorefronts:]_block_invoke_2
+ ___93-[FCPurchaseController handleAccessTokenVerificationSuccessWithTagID:subscribed:accessToken:]_block_invoke.235
+ ___block_descriptor_32_e25_"NSURL"16?0"NSString"8l
+ ___block_descriptor_32_e31_q24?0"NSNumber"8"NSNumber"16l
+ ___block_descriptor_32_e43_B32?0"NSString"8"<FCTagProviding>"16^B24l
+ ___block_descriptor_40_e8_32bs_e17_16?0"NSArray"8ls32l8
+ ___block_descriptor_40_e8_32bs_e35_v16?0"<FCFeedItemInventoryType>"8ls32l8
+ ___block_descriptor_40_e8_32r_e17_16?0"NSArray"8lr32l8
+ ___block_descriptor_40_e8_32s_e15_v32?0816^B24ls32l8
+ ___block_descriptor_40_e8_32s_e23_16?0"FCLocalRegion"8ls32l8
+ ___block_descriptor_40_e8_32s_e26_"<FCPuzzleProviding>"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e26_16?0"<FCTagProviding>"8ls32l8
+ ___block_descriptor_40_e8_32s_e30_"<FCFeedItemServiceType>"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e33_B16?0"FCReferenceToMembership"8ls32l8
+ ___block_descriptor_48_e8_32bs40bs_e8_v16?08ls32l8s40l8
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e35_v16?0"<FCFeedItemInventoryType>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e35_v16?0"<FCFeedItemInventoryType>"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e8_v12?0B8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e29_v32?0"NTPBFeedItem"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e39_v32?0"NSArray"8"NSSet"16"NSError"24ls32l8w40l8
+ ___block_descriptor_48_e8_32s_e35_v16?0"<FCFeedItemInventoryType>"8ls32l8
+ ___block_descriptor_56_e8_32s40bs48bs_e14_v16?0?<v?>8ls40l8s48l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e32_v16?0"FCFetchOperationResult"8ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s_e24_v16?0"NSMutableArray"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s_e26_16?0"<FCTagProviding>"8ls32l8
+ ___block_descriptor_56_e8_32s_e35_v16?0"<FCFeedItemInventoryType>"8ls32l8
+ ___block_descriptor_64_e8_32s40bs48bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8
+ ___block_literal_global.111
+ ___block_literal_global.113
+ ___block_literal_global.118
+ ___block_literal_global.1184
+ ___block_literal_global.122
+ ___block_literal_global.124
+ ___block_literal_global.1251
+ ___block_literal_global.128
+ ___block_literal_global.130
+ ___block_literal_global.132
+ ___block_literal_global.1326
+ ___block_literal_global.1328
+ ___block_literal_global.1330
+ ___block_literal_global.1338
+ ___block_literal_global.134
+ ___block_literal_global.1349
+ ___block_literal_global.1354
+ ___block_literal_global.1359
+ ___block_literal_global.136
+ ___block_literal_global.1364
+ ___block_literal_global.169
+ ___block_literal_global.1745
+ ___block_literal_global.1777
+ ___block_literal_global.1829
+ ___block_literal_global.1842
+ ___block_literal_global.1855
+ ___block_literal_global.1865
+ ___block_literal_global.1878
+ ___block_literal_global.2011
+ ___block_literal_global.2036
+ ___block_literal_global.2106
+ ___block_literal_global.2119
+ ___block_literal_global.32
+ ___block_literal_global.400
+ ___block_literal_global.403
+ ___block_literal_global.415
+ ___block_literal_global.418
+ ___block_literal_global.429
+ ___block_literal_global.432
+ ___block_literal_global.437
+ ___block_literal_global.446
+ ___block_literal_global.452
+ ___block_literal_global.455
+ ___block_literal_global.463
+ ___block_literal_global.466
+ ___block_literal_global.469
+ ___block_literal_global.484
+ ___block_literal_global.497
+ ___block_literal_global.514
+ ___block_literal_global.525
+ ___block_literal_global.530
+ ___block_literal_global.844
+ ___block_literal_global.873
+ ___block_literal_global.97
+ __unnamed_array_storage.124
+ __unnamed_array_storage.125
+ __unnamed_array_storage.137
+ __unnamed_array_storage.42
+ __unnamed_array_storage.93
+ __unnamed_array_storage.94
+ _kFCNewsTabiChannelPickerSuggestionsConfigurationFilterLocationSuggestionsOnlyToAppleNewsLocalKey
+ _kFCPuzzlesArchiveAPIEnabledKey
+ _kFCPuzzlesCacheLifetime
+ _kFCPuzzlesConfigurationPuzzleFullArchiveTagIDKey
+ _kFCPuzzlesFullArchiveMenuConfig
+ _kFCPuzzlesFullArchiveMenuSections
+ _kFCPuzzlesRecentCacheLifetime
+ _objc_msgSend$_childInventories
+ _objc_msgSend$_createESLInventory
+ _objc_msgSend$_enumerateChildInventories:
+ _objc_msgSend$_populateScoreProfilesForFeedItems:
+ _objc_msgSend$_populateScoreProfilesForFeedItems:configurationSet:
+ _objc_msgSend$_promiseCuratedFeedItemsForTags:configuration:
+ _objc_msgSend$_promiseCuratedFeedItemsWithConfiguration:
+ _objc_msgSend$_promiseFeedItemsForTags:configuration:
+ _objc_msgSend$_promiseRelevantTagsWithConfiguration:
+ _objc_msgSend$_refreshIfNeededWithQoS:
+ _objc_msgSend$addFeedItems:
+ _objc_msgSend$aggregateStoreData
+ _objc_msgSend$allFeedItemsWithTopic:
+ _objc_msgSend$articleDislikedEventCount
+ _objc_msgSend$articleLikedEventCount
+ _objc_msgSend$articleReadEventCount
+ _objc_msgSend$articleSavedEventCount
+ _objc_msgSend$articleSeenEventCount
+ _objc_msgSend$articleSharedEventCount
+ _objc_msgSend$articleVisitedEventCount
+ _objc_msgSend$centerLocationCoordinateForEntireRegion
+ _objc_msgSend$coefficients
+ _objc_msgSend$defaultDeviceInfo
+ _objc_msgSend$distanceFromLocation:
+ _objc_msgSend$downloadIfNeededWithGroup:completion:
+ _objc_msgSend$empty
+ _objc_msgSend$emptyWithSessionsOnDiskSize:personalizationAnalyticsEnabled:
+ _objc_msgSend$eventCounts
+ _objc_msgSend$fastCachedPuzzleForID:
+ _objc_msgSend$feedIDForBin:
+ _objc_msgSend$feedItemService
+ _objc_msgSend$feedViewEventCount
+ _objc_msgSend$fetchFeedItemsWithCompletion:
+ _objc_msgSend$filterLocationSuggestionsOnlyToAppleNewsLocal
+ _objc_msgSend$freeGlobalESLArticleListIDs
+ _objc_msgSend$freeTagESLArticleListIDPrefix
+ _objc_msgSend$generateSportsLogoAltImageAssetHandleWithAssetManager:
+ _objc_msgSend$generateSportsLogoAltImageCompactAssetHandleWithAssetManager:
+ _objc_msgSend$generateSportsLogoAltImageLargeAssetHandleWithAssetManager:
+ _objc_msgSend$globalInventory
+ _objc_msgSend$hasEvergreenArticleList
+ _objc_msgSend$initWithAggregateStoreGenerationTime:aggregateTotalCount:meanCountOfEvents:sessionsOnDiskSize:standardDeviationOfEvents:totalEventsCount:headlineEventCount:headlinesWithValidTitleEmbeddingsEventCount:headlinesWithInvalidTitleEmbeddingsEventCount:headlinesWithValidBodyEmbeddingsEventCount:headlinesWithInvalidBodyEmbeddingsEventCount:eventCounts:aggregateStoreData:
+ _objc_msgSend$initWithArticleSeenEventCount:articleVisitedEventCount:articleReadEventCount:articleLikedEventCount:articleDislikedEventCount:articleSharedEventCount:articleSavedEventCount:feedViewEventCount:tagFollowedEventCount:tagUnfollowedEventCount:tagMutedEventCount:
+ _objc_msgSend$initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:puzzlesArchiveAPIBaseURLString:appAnalyticsNotificationReceiptBaseURLString:authTokenAPIBaseURLString:sportsDataVisualizationAPIBaseURLString:fineGrainedNewsletterSubscriptionBaseURLString:appAnalyticsSportsEventsBaseURLString:appAnalyticsAppHealthBaseURLString:ckOrderFeedBaseURLString:ckMultiFetchBaseURLString:ckRecordFetchBaseURLString:ckEdgeCachedOrderFeedBaseURLString:ckEdgeCachedMultiFetchBaseURLString:
+ _objc_msgSend$initWithContext:feedItemService:filePath:version:refreshInterval:loggingKey:
+ _objc_msgSend$initWithContext:tag:feedConfiguration:referringFeedItemIdentifier:
+ _objc_msgSend$initWithContext:tag:sortMethod:filterOptions:personalizationConfigurationSet:feedConfiguration:referringFeedItemIdentifier:
+ _objc_msgSend$initWithGlobalInventory:tagInventory:
+ _objc_msgSend$initWithIdentifier:title:subtitle:puzzleDescription:puzzleType:dataResourceID:authors:publishDate:isPaid:difficulty:difficultyDescription:thumbnailLargeImageAssetHandle:loadDate:teaserClue:teaserAnswer:teaserInfo:teaserDirection:teaserNumber:language:blockedStorefrontIDs:allowedStorefrontIDs:minimumNewsVersion:showInfoModalOnFirstPlay:isDeprecated:isDraft:lastModifiedDate:
+ _objc_msgSend$initWithLatitude:longitude:
+ _objc_msgSend$initWithPrivateDataDirectory:configurationManager:
+ _objc_msgSend$initWithStartDate:timeInterval:
+ _objc_msgSend$initWithTags:context:configuration:bundleSubscriptionManager:
+ _objc_msgSend$initWithTitle:icon:level:difficultyIndex:
+ _objc_msgSend$keysSortedByValueUsingComparator:
+ _objc_msgSend$maxTagESLArticleListsToQuery
+ _objc_msgSend$paidGlobalESLArticleListIDs
+ _objc_msgSend$paidTagESLArticleListIDPrefix
+ _objc_msgSend$personalizationAnalyticsEnabled
+ _objc_msgSend$propertyFlagsLocalized
+ _objc_msgSend$puzzleFullArchiveTagID
+ _objc_msgSend$puzzlesArchiveAPIBaseURLString
+ _objc_msgSend$puzzlesArchiveBaseURLForConfiguration
+ _objc_msgSend$readBool:
+ _objc_msgSend$readObject:
+ _objc_msgSend$reduceVisibilityForNonFollowers
+ _objc_msgSend$refreshIfNeededWithCompletion:
+ _objc_msgSend$refreshInterval
+ _objc_msgSend$savePuzzleToCache:
+ _objc_msgSend$setActiveiTunesAccountName:
+ _objc_msgSend$setAggregateCounts:
+ _objc_msgSend$setBaselineStatelessEventCount:
+ _objc_msgSend$setBaselineTimestamp:
+ _objc_msgSend$setBaselineTotalEventCount:
+ _objc_msgSend$setChannelTopic:
+ _objc_msgSend$setGroup:
+ _objc_msgSend$setPropertyFlagsLocalized:
+ _objc_msgSend$setReduceVisibilityForNonFollowers:
+ _objc_msgSend$setSportsLogoAltImageCompactURL:
+ _objc_msgSend$setSportsLogoAltImageLargeURL:
+ _objc_msgSend$setSportsLogoAltImageURL:
+ _objc_msgSend$setTag:
+ _objc_msgSend$sportsDataVisualizationBaseURLForConfiguration:
+ _objc_msgSend$sportsLogoAltImageCompactURL
+ _objc_msgSend$sportsLogoAltImageLargeURL
+ _objc_msgSend$sportsLogoAltImageURL
+ _objc_msgSend$sportsSecondaryShortName
+ _objc_msgSend$sportsTopStoriesTagID
+ _objc_msgSend$subscriptionsWithCompletion:
+ _objc_msgSend$tagFollowedEventCount
+ _objc_msgSend$tagInventory
+ _objc_msgSend$tagMutedEventCount
+ _objc_msgSend$tagUnfollowedEventCount
- +[FCNewsTabiEventAggregationBaseEventConditions noConditions]
- +[FCUserEventHistoryMetadata emptyWithSessionsOnDiskSize:]
- -[FCConfigurationManager _deviceInfoWithFormatVersion:]
- -[FCESLInventory _adoptInventory:]
- -[FCESLInventory _isRefreshNeeded]
- -[FCESLInventory _loadInventoryFromCache]
- -[FCESLInventory _prepareForUse]
- -[FCESLInventory _promiseConfiguration]
- -[FCESLInventory _promiseEvergreenFeedItemsWithConfiguration:]
- -[FCESLInventory _promiseFeedItemsWithIssues:configuration:]
- -[FCESLInventory _promiseIssueFeedItemsWithConfiguration:]
- -[FCESLInventory _promiseIssuesWithConfiguration:]
- -[FCESLInventory _refreshIfNeeded]
- -[FCESLInventory _rescoreInventoryIfNeeded:forScoringVersion:]
- -[FCESLInventory cacheDataPath]
- -[FCESLInventory context]
- -[FCESLInventory feedItemsRefreshSerialQueue]
- -[FCESLInventory initWithContext:cacheDirectory:]
- -[FCESLInventory init]
- -[FCESLInventory latestInventory]
- -[FCESLInventory loadFromCacheOnce]
- -[FCESLInventory populateScoreProfilesForFeedItems:]
- -[FCESLInventory populateScoreProfilesForFeedItems:configurationSet:]
- -[FCESLInventory setLatestInventory:]
- -[FCEndpointConfiguration initWithClientAPIBaseURLString:notificationsBaseURLString:]
- -[FCEndpointConfiguration initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:]
- -[FCEndpointConfiguration initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:]
- -[FCEndpointConfiguration initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:]
- -[FCEndpointConfiguration initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:]
- -[FCEndpointConfiguration initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:]
- -[FCEndpointConfiguration initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:appAnalyticsNotificationReceiptBaseURLString:]
- -[FCEndpointConfiguration initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:appAnalyticsNotificationReceiptBaseURLString:authTokenAPIBaseURLString:]
- -[FCEndpointConfiguration initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:appAnalyticsNotificationReceiptBaseURLString:authTokenAPIBaseURLString:sportsDataVisualizationAPIBaseURLString:fineGrainedNewsletterSubscriptionBaseURLString:]
- -[FCEvergreenArticlesOperation .cxx_destruct]
- -[FCEvergreenArticlesOperation completionHandler]
- -[FCEvergreenArticlesOperation initWithContext:configuration:bundleSubscriptionManager:]
- -[FCEvergreenArticlesOperation init]
- -[FCEvergreenArticlesOperation networkEvents]
- -[FCEvergreenArticlesOperation operationWillFinishWithError:]
- -[FCEvergreenArticlesOperation performOperation]
- -[FCEvergreenArticlesOperation prepareOperation]
- -[FCEvergreenArticlesOperation setCompletionHandler:]
- -[FCMyArticlesOperation prewarmScoreCache:]
- -[FCMyArticlesOperation scoreFeedItems]
- -[FCMyArticlesOperation setScoreFeedItems:]
- -[FCNewsAppConfig feedContentExposureTestMaximumInterval]
- -[FCNewsAppConfig freeEvergreenArticleListIDs]
- -[FCNewsAppConfig paidEvergreenArticleListIDs]
- -[FCNewsTabiChannelPickerSuggestionsConfiguration dictionary]
- -[FCNewsTabiChannelPickerSuggestionsConfiguration initWithBundleInputOutputConfiguration:nonBundleInputOutputConfiguration:userContextConfiguration:]
- -[FCNewsTabiChannelPickerSuggestionsInputOutputConfiguration initWithContextFeatureKey:generalChannelSuggestionsOutputName:generalChannelSuggestionsScoreOutputName:newsPlusChannelSuggestionsOutputName:newsPlusChannelSuggestionsScoreOutputName:]
- -[FCNewsTabiChannelPickerSuggestionsUserContextConfiguration dictionary]
- -[FCNewsTabiEventAggregationBaseEventConditions dictionary]
- -[FCNewsTabiEventAggregationConditions initWithArticleSeenConditions:articleReadConditions:articleVisitedConditions:articleSharedConditions:articleLikedConditions:articleDislikedConditions:articleSavedConditions:trackVisitedConditions:trackListenedConditions:trackFinishedConditions:articleUnlikedConditions:articleUndislikedConditions:articleUnsavedConditions:]
- -[FCNewsTabiEventAggregationConfiguration dictionary]
- -[FCNewsTabiEventAggregationConfiguration initWithMaxTopicIds:maxSessionEvents:readEventsOnly:titleEmbeddingDimension:fullBodyEmbeddingDimension:bundleOutputConfiguration:nonBundleOutputConfiguration:eventConditions:]
- -[FCNewsTabiEventAggregationDurationEventConditions dictionary]
- -[FCNewsTabiEventAggregationOutputConfiguration initWithOutputNames:]
- -[FCNewsTabiFeedPersonalizationConfiguration dictionary]
- -[FCNewsTabiFeedPersonalizationConfiguration initWithMaxTopicIds:titleEmbeddingDimension:fullBodyEmbeddingDimension:bundleOutputConfiguration:nonBundleOutputConfiguration:]
- -[FCNewsTabiFeedPersonalizationOutputConfiguration dictionary]
- -[FCNewsTabiFeedPersonalizationOutputConfiguration initWithTagScoringOutputName:defaultHeadlineScoringOutputName:topicFeedHeadlineScoringOutputName:magazineFeedHeadlineScoringOutputName:magazineFeedIssuesHeadlineScoringOutputName:legacyAudioFeedHeadlineScoringOutputName:audioFeedHeadlineScoringOutputName:articleRecirculationPrimaryHeadlineScoringOutputName:articleRecirculationSecondaryHeadlineScoringOutputName:articleRecirculationTertiaryHeadlineScoringOutputName:articleRecirculationQuaternaryHeadlineScoringOutputName:bestOfBundleHeadlineScoringOutputName:forYouGroupHeadlineScoringOutputName:greatStoriesYouMissedGroupHeadlineScoringOutputName:latestStoriesGroupHeadlineScoringOutputName:localNewsGroupHeadlineScoringOutputName:newspaperGroupMagazineFeedHeadlineScoringOutputName:todayWidgetHeadlineScoringOutputName:tagWidgetHeadlineScoringOutputName:notificationHeadlineScoringOutputName:mySportsGroupHeadlineScoringOutputName:sportsTopStoriesHeadlineScoringOutputName:introToSportsGroupHeadlineScoringOutputName:highlightsGroupHeadlineScoringOutputName:articleListTagFeedGroupHeadlineScoringOutputName:tagFeedHeadlineScoringOutputName:newspaperGroupTodayFeedHeadlineScoringOutputName:moreForYouGroupHeadlineScoringOutputName:introToSportsGroupForYouHeadlineScoringOutputName:mySportsGroupForYouHeadlineScoringOutputName:mySportsTopicsHeadlineScoringOutputName:curatedGroupHeadlineScoringOutputName:curatedGroupIssuesHeadlineScoringOutputName:localSectionGroupHeadlineScoringOutputName:newspaperSectionGroupHeadlineScoringOutputName:sportsEventArticlesGroupHeadlineScoringOutputName:tagFeedForYouGroupHeadlineScoringOutputName:tagRecentStoriesGroupHeadlineScoringOutputName:tagDateRangeGroupHeadlineScoringOutputName:sportsEventTopicGroupHeadlineScoringOutputName:shadowDefaultHeadlineScoringOutputName:shadowTopicFeedHeadlineScoringOutputName:shadowMagazineFeedHeadlineScoringOutputName:shadowMagazineFeedIssuesHeadlineScoringOutputName:shadowLegacyAudioFeedHeadlineScoringOutputName:shadowAudioFeedHeadlineScoringOutputName:shadowArticleRecirculationPrimaryHeadlineScoringOutputName:shadowArticleRecirculationSecondaryHeadlineScoringOutputName:shadowArticleRecirculationTertiaryHeadlineScoringOutputName:shadowArticleRecirculationQuaternaryHeadlineScoringOutputName:shadowBestOfBundleHeadlineScoringOutputName:shadowForYouGroupHeadlineScoringOutputName:shadowGreatStoriesYouMissedGroupHeadlineScoringOutputName:shadowLatestStoriesGroupHeadlineScoringOutputName:shadowLocalNewsGroupHeadlineScoringOutputName:shadowNewspaperGroupMagazineFeedHeadlineScoringOutputName:shadowTodayWidgetHeadlineScoringOutputName:shadowTagWidgetHeadlineScoringOutputName:shadowNotificationHeadlineScoringOutputName:shadowMySportsGroupHeadlineScoringOutputName:shadowSportsTopStoriesHeadlineScoringOutputName:shadowIntroToSportsGroupHeadlineScoringOutputName:shadowHighlightsGroupHeadlineScoringOutputName:shadowArticleListTagFeedGroupHeadlineScoringOutputName:shadowTagFeedHeadlineScoringOutputName:shadowNewspaperGroupTodayFeedHeadlineScoringOutputName:shadowMoreForYouGroupHeadlineScoringOutputName:shadowIntroToSportsGroupForYouHeadlineScoringOutputName:shadowMySportsGroupForYouHeadlineScoringOutputName:shadowMySportsTopicsHeadlineScoringOutputName:shadowCuratedGroupHeadlineScoringOutputName:shadowCuratedGroupIssuesHeadlineScoringOutputName:shadowLocalSectionGroupHeadlineScoringOutputName:shadowNewspaperSectionGroupHeadlineScoringOutputName:shadowSportsEventArticlesGroupHeadlineScoringOutputName:shadowTagFeedForYouGroupHeadlineScoringOutputName:shadowTagRecentStoriesGroupHeadlineScoringOutputName:shadowTagDateRangeGroupHeadlineScoringOutputName:shadowSportsEventTopicGroupHeadlineScoringOutputName:]
- -[FCNewsTabiPersonalizedPaywallsConfiguration dictionary]
- -[FCNewsTabiPersonalizedPaywallsConfiguration initWithContextFeatureKey:channelIDsOutputName:scoresOutputName:]
- -[FCNewsTabiRecommendedIssuesConfiguration dictionary]
- -[FCNewsTabiRecommendedIssuesConfiguration initWithBundleInputOutputConfiguration:nonBundleInputOutputConfiguration:userContextConfiguration:]
- -[FCNewsTabiRecommendedIssuesInputOutputConfiguration dictionary]
- -[FCNewsTabiRecommendedIssuesInputOutputConfiguration initWithContextFeatureKey:recommendedIssuePublisherOutputName:recommendedIssuePublisherScoreOutputName:]
- -[FCNewsTabiRecommendedIssuesUserContextConfiguration dictionary]
- -[FCPuzzle initWithIdentifier:title:subtitle:puzzleDescription:puzzleType:dataResourceID:authors:publishDate:isPaid:difficulty:difficultyDescription:thumbnailLargeImageAssetHandle:loadDate:teaserClue:teaserAnswer:teaserInfo:teaserDirection:teaserNumber:language:blockedStorefrontIDs:allowedStorefrontIDs:minimumNewsVersion:showInfoModalOnFirstPlay:isDeprecated:isDraft:]
- -[FCUserEventHistoryMetadata initWithAggregateStoreGenerationTime:aggregateTotalCount:meanCountOfEvents:sessionsOnDiskSize:standardDeviationOfEvents:totalEventsCount:headlineEventCount:headlinesWithValidTitleEmbeddingsEventCount:headlinesWithInvalidTitleEmbeddingsEventCount:headlinesWithValidBodyEmbeddingsEventCount:headlinesWithInvalidBodyEmbeddingsEventCount:]
- -[FCUserEventHistoryStorage setMetadataWithAggregateStoreGenerationTime:aggregateTotalCount:meanCountOfEvents:standardDeviationOfEvents:totalEventsCount:headlineEventCount:headlinesWithValidTitleEmbeddingsEventCount:headlinesWithInvalidTitleEmbeddingsEventCount:headlinesWithValidBodyEmbeddingsEventCount:headlinesWithInvalidBodyEmbeddingsEventCount:]
- GCC_except_table114
- GCC_except_table125
- GCC_except_table130
- GCC_except_table136
- _OBJC_CLASS_$_FCEvergreenArticlesOperation
- _OBJC_CLASS_$_NTPBFeedItemInventory
- _OBJC_IVAR_$_FCESLInventory._cacheDataPath
- _OBJC_IVAR_$_FCESLInventory._context
- _OBJC_IVAR_$_FCESLInventory._feedItemsRefreshSerialQueue
- _OBJC_IVAR_$_FCESLInventory._latestInventory
- _OBJC_IVAR_$_FCESLInventory._loadFromCacheOnce
- _OBJC_METACLASS_$_FCEvergreenArticlesOperation
- __OBJC_$_CLASS_METHODS_FCNewsTabiEventAggregationBaseEventConditions
- __OBJC_$_INSTANCE_METHODS_FCEvergreenArticlesOperation
- __OBJC_$_INSTANCE_VARIABLES_FCEvergreenArticlesOperation
- __OBJC_$_PROP_LIST_FCESLInventoryType
- __OBJC_$_PROP_LIST_FCEvergreenArticlesOperation
- __OBJC_$_PROP_LIST_FCNewsletterManager.300
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_FCESLInventoryType
- __OBJC_$_PROTOCOL_METHOD_TYPES_FCESLInventoryType
- __OBJC_CLASS_RO_$_FCEvergreenArticlesOperation
- __OBJC_LABEL_PROTOCOL_$_FCESLInventoryType
- __OBJC_METACLASS_RO_$_FCEvergreenArticlesOperation
- __OBJC_PROTOCOL_$_FCESLInventoryType
- ___103-[FCSubscriptionController fetchAllTagsWithCallbackQueue:maximumCachedAge:qualityOfService:completion:]_block_invoke.387
- ___103-[FCSubscriptionController fetchAllTagsWithCallbackQueue:maximumCachedAge:qualityOfService:completion:]_block_invoke_2.390
- ___122-[FCSubscriptionController addAutoFavoriteSubscriptionForTagIDs:groupableSubscriptionForTagIDs:originProvider:completion:]_block_invoke.411
- ___122-[FCSubscriptionController addAutoFavoriteSubscriptionForTagIDs:groupableSubscriptionForTagIDs:originProvider:completion:]_block_invoke.417
- ___122-[FCSubscriptionController addAutoFavoriteSubscriptionForTagIDs:groupableSubscriptionForTagIDs:originProvider:completion:]_block_invoke.421
- ___122-[FCSubscriptionController addAutoFavoriteSubscriptionForTagIDs:groupableSubscriptionForTagIDs:originProvider:completion:]_block_invoke_2.414
- ___122-[FCSubscriptionController addAutoFavoriteSubscriptionForTagIDs:groupableSubscriptionForTagIDs:originProvider:completion:]_block_invoke_2.422
- ___126-[FCPurchaseController verifyAccessTokenWithTagID:accessToken:consumedArticleCount:serialCompletion:callbackQueue:completion:]_block_invoke.236
- ___126-[FCPurchaseController verifyAccessTokenWithTagID:accessToken:consumedArticleCount:serialCompletion:callbackQueue:completion:]_block_invoke.250
- ___126-[FCPurchaseController verifyAccessTokenWithTagID:accessToken:consumedArticleCount:serialCompletion:callbackQueue:completion:]_block_invoke.254
- ___126-[FCPurchaseController verifyAccessTokenWithTagID:accessToken:consumedArticleCount:serialCompletion:callbackQueue:completion:]_block_invoke_2.252
- ___32-[FCESLInventory _prepareForUse]_block_invoke
- ___34-[FCESLInventory _adoptInventory:]_block_invoke
- ___34-[FCESLInventory _refreshIfNeeded]_block_invoke
- ___34-[FCESLInventory _refreshIfNeeded]_block_invoke.24
- ___34-[FCESLInventory _refreshIfNeeded]_block_invoke.33
- ___34-[FCESLInventory _refreshIfNeeded]_block_invoke.37
- ___34-[FCESLInventory _refreshIfNeeded]_block_invoke_2
- ___34-[FCESLInventory _refreshIfNeeded]_block_invoke_2.25
- ___34-[FCESLInventory _refreshIfNeeded]_block_invoke_2.35
- ___34-[FCESLInventory _refreshIfNeeded]_block_invoke_3
- ___34-[FCESLInventory _refreshIfNeeded]_block_invoke_3.27
- ___34-[FCESLInventory _refreshIfNeeded]_block_invoke_4
- ___34-[FCESLInventory _refreshIfNeeded]_block_invoke_4.29
- ___37-[FCNewsTabiConfiguration dictionary]_block_invoke
- ___41-[FCESLInventory _loadInventoryFromCache]_block_invoke
- ___41-[FCESLInventory _loadInventoryFromCache]_block_invoke.47
- ___41-[FCESLInventory _loadInventoryFromCache]_block_invoke.50
- ___41-[FCESLInventory _loadInventoryFromCache]_block_invoke.51
- ___48-[FCEvergreenArticlesOperation performOperation]_block_invoke
- ___48-[FCEvergreenArticlesOperation performOperation]_block_invoke.18
- ___48-[FCEvergreenArticlesOperation performOperation]_block_invoke_2
- ___48-[FCEvergreenArticlesOperation performOperation]_block_invoke_3
- ___48-[FCEvergreenArticlesOperation performOperation]_block_invoke_4
- ___48-[FCEvergreenArticlesOperation performOperation]_block_invoke_5
- ___48-[FCEvergreenArticlesOperation prepareOperation]_block_invoke
- ___50-[FCESLInventory _promiseIssuesWithConfiguration:]_block_invoke
- ___50-[FCESLInventory _promiseIssuesWithConfiguration:]_block_invoke.53
- ___50-[FCESLInventory _promiseIssuesWithConfiguration:]_block_invoke_2
- ___53-[FCPuzzleThumbnailHandle downloadIfNeededWithGroup:]_block_invoke
- ___54-[FCSubscriptionController _saveReadableSubscriptions]_block_invoke.515
- ___56-[FCNewsTabiFeedPersonalizationConfiguration dictionary]_block_invoke
- ___58-[FCESLInventory _promiseIssueFeedItemsWithConfiguration:]_block_invoke
- ___58-[FCESLInventory _promiseIssueFeedItemsWithConfiguration:]_block_invoke_2
- ___58-[FCUserEventHistoryStorage initWithPrivateDataDirectory:]_block_invoke
- ___58-[FCUserEventHistoryStorage initWithPrivateDataDirectory:]_block_invoke_2
- ___60-[FCESLInventory _promiseFeedItemsWithIssues:configuration:]_block_invoke
- ___60-[FCESLInventory _promiseFeedItemsWithIssues:configuration:]_block_invoke.57
- ___60-[FCESLInventory _promiseFeedItemsWithIssues:configuration:]_block_invoke_2
- ___62-[FCAssetManager _fetchDataProviderForAssetHandle:completion:]_block_invoke.60
- ___62-[FCESLInventory _promiseEvergreenFeedItemsWithConfiguration:]_block_invoke
- ___62-[FCESLInventory _promiseEvergreenFeedItemsWithConfiguration:]_block_invoke.59
- ___62-[FCESLInventory _promiseEvergreenFeedItemsWithConfiguration:]_block_invoke_2
- ___62-[FCESLInventory _rescoreInventoryIfNeeded:forScoringVersion:]_block_invoke
- ___64-[FCAssetManager _populateRawFilePathForAssetHandle:completion:]_block_invoke.53
- ___64-[FCAssetManager _populateRawFilePathForAssetHandle:completion:]_block_invoke_2.54
- ___71-[FCCloudContext fetchShouldSecureSubscriptionsForDatabase:completion:]_block_invoke.200
- ___71-[FCCloudContext fetchShouldSecureSubscriptionsForDatabase:completion:]_block_invoke_2.201
- ___71-[FCMyArticlesOperation _fetchAllFeedItemsWithFeedRequests:completion:]_block_invoke
- ___72-[FCArticleHeadline _adoptNarrativeTrackFromArticleRecord:assetManager:]_block_invoke.49
- ___72-[FCArticleHeadline _adoptNarrativeTrackFromArticleRecord:assetManager:]_block_invoke.50
- ___75-[FCPaidBundleConfiguration arePaywallConfigsEqualToOtherPaidBundleConfig:]_block_invoke.11
- ___76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke.173
- ___76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke.182
- ___76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke_2.174
- ___76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke_2.184
- ___78-[FCFeedRequestOperation _gatherEdgeCachedFeedResponsesWithCompletionHandler:]_block_invoke_5
- ___81-[FCEvergreenArticlesOperation _feedItemsFromArticleRecords:sourceArticleListID:]_block_invoke
- ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke.446
- ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke_2.447
- ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke_3.451
- ___85-[FCSubscriptionController _fetchTagsForIDs:cachePolicy:qualityOfService:completion:]_block_invoke_4.454
- ___87-[FCCloudContext fetchOriginalDataShouldBeDeletedAfterMigrationForDatabase:completion:]_block_invoke.189
- ___87-[FCCloudContext fetchOriginalDataShouldBeDeletedAfterMigrationForDatabase:completion:]_block_invoke_2.190
- ___93-[FCPurchaseController handleAccessTokenVerificationSuccessWithTagID:subscribed:accessToken:]_block_invoke.234
- ___block_descriptor_40_e8_32bs_e31_16?0"NTPBFeedItemInventory"8ls32l8
- ___block_descriptor_48_e8_32s40r_e17_16?0"NSArray"8lr40l8s32l8
- ___block_literal_global.112
- ___block_literal_global.117
- ___block_literal_global.119
- ___block_literal_global.121
- ___block_literal_global.1263
- ___block_literal_global.1265
- ___block_literal_global.1267
- ___block_literal_global.1275
- ___block_literal_global.1286
- ___block_literal_global.1291
- ___block_literal_global.1296
- ___block_literal_global.1301
- ___block_literal_global.131
- ___block_literal_global.133
- ___block_literal_global.1733
- ___block_literal_global.1765
- ___block_literal_global.1817
- ___block_literal_global.1830
- ___block_literal_global.1843
- ___block_literal_global.1853
- ___block_literal_global.1866
- ___block_literal_global.1999
- ___block_literal_global.2024
- ___block_literal_global.2094
- ___block_literal_global.2107
- ___block_literal_global.393
- ___block_literal_global.398
- ___block_literal_global.401
- ___block_literal_global.413
- ___block_literal_global.416
- ___block_literal_global.427
- ___block_literal_global.428
- ___block_literal_global.430
- ___block_literal_global.433
- ___block_literal_global.445
- ___block_literal_global.450
- ___block_literal_global.453
- ___block_literal_global.457
- ___block_literal_global.460
- ___block_literal_global.467
- ___block_literal_global.478
- ___block_literal_global.479
- ___block_literal_global.496
- ___block_literal_global.507
- ___block_literal_global.512
- ___block_literal_global.77
- ___block_literal_global.80
- ___block_literal_global.821
- ___block_literal_global.850
- ___block_literal_global.94
- __unnamed_array_storage.121
- __unnamed_array_storage.90
- __unnamed_array_storage.91
- _objc_msgSend$_promiseEvergreenFeedItemsWithConfiguration:
- _objc_msgSend$articleDislikedConditions
- _objc_msgSend$articleLikedConditions
- _objc_msgSend$articleReadConditions
- _objc_msgSend$articleSavedConditions
- _objc_msgSend$articleSeenConditions
- _objc_msgSend$articleSharedConditions
- _objc_msgSend$articleUndislikedConditions
- _objc_msgSend$articleUnlikedConditions
- _objc_msgSend$articleUnsavedConditions
- _objc_msgSend$articleVisitedConditions
- _objc_msgSend$cacheDataPath
- _objc_msgSend$defaultDeviceInfoWithAppVersion:formatVersion:seedNumber:buildNumber:
- _objc_msgSend$emptyWithSessionsOnDiskSize:
- _objc_msgSend$eslInventory
- _objc_msgSend$freeEvergreenArticleListIDs
- _objc_msgSend$includeEvergreenFeedItems
- _objc_msgSend$initWithAggregateStoreGenerationTime:aggregateTotalCount:meanCountOfEvents:sessionsOnDiskSize:standardDeviationOfEvents:totalEventsCount:headlineEventCount:headlinesWithValidTitleEmbeddingsEventCount:headlinesWithInvalidTitleEmbeddingsEventCount:headlinesWithValidBodyEmbeddingsEventCount:headlinesWithInvalidBodyEmbeddingsEventCount:
- _objc_msgSend$initWithArticleSeenConditions:articleReadConditions:articleVisitedConditions:articleSharedConditions:articleLikedConditions:articleDislikedConditions:articleSavedConditions:trackVisitedConditions:trackListenedConditions:trackFinishedConditions:articleUnlikedConditions:articleUndislikedConditions:articleUnsavedConditions:
- _objc_msgSend$initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:
- _objc_msgSend$initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:
- _objc_msgSend$initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:
- _objc_msgSend$initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:
- _objc_msgSend$initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:appAnalyticsNotificationReceiptBaseURLString:
- _objc_msgSend$initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:appAnalyticsNotificationReceiptBaseURLString:authTokenAPIBaseURLString:
- _objc_msgSend$initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:appAnalyticsNotificationReceiptBaseURLString:authTokenAPIBaseURLString:sportsDataVisualizationAPIBaseURLString:fineGrainedNewsletterSubscriptionBaseURLString:
- _objc_msgSend$initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:appAnalyticsNotificationReceiptBaseURLString:authTokenAPIBaseURLString:sportsDataVisualizationAPIBaseURLString:fineGrainedNewsletterSubscriptionBaseURLString:appAnalyticsSportsEventsBaseURLString:appAnalyticsAppHealthBaseURLString:ckOrderFeedBaseURLString:ckMultiFetchBaseURLString:ckRecordFetchBaseURLString:ckEdgeCachedOrderFeedBaseURLString:ckEdgeCachedMultiFetchBaseURLString:
- _objc_msgSend$initWithContext:cacheDirectory:
- _objc_msgSend$initWithContext:tag:sortMethod:filterOptions:personalizationConfigurationSet:feedConfiguration:
- _objc_msgSend$initWithIdentifier:title:subtitle:puzzleDescription:puzzleType:dataResourceID:authors:publishDate:isPaid:difficulty:difficultyDescription:thumbnailLargeImageAssetHandle:loadDate:teaserClue:teaserAnswer:teaserInfo:teaserDirection:teaserNumber:language:blockedStorefrontIDs:allowedStorefrontIDs:minimumNewsVersion:showInfoModalOnFirstPlay:isDeprecated:isDraft:
- _objc_msgSend$initWithOutputNames:
- _objc_msgSend$maximumTagCount
- _objc_msgSend$maximumTopicTagsPerHeadline
- _objc_msgSend$paidEvergreenArticleListIDs
- _objc_msgSend$populateScoreProfilesForFeedItems:
- _objc_msgSend$populateScoreProfilesForFeedItems:configurationSet:
- _objc_msgSend$trackFinishedConditions
- _objc_msgSend$trackListenedConditions
- _objc_msgSend$trackVisitedConditions
CStrings:
+ "\x01R"
+ "\x02\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0/\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\r"
+ "\x03\x11\x11"
+ "\x05\"\x17\x15"
+ "\x0e"
+ "\x13Aa"
+ "\x14\x12#"
+ "\x17\x16\x18"
+ "\x1a\x12\x11"
+ "\x1a\x1f\x12\x1b\x15"
+ "\x1f\x0f\x0f\x01"
+ "%@ found a purchaseLookupEntry with not supported validation state for tagID %{public}@"
+ "%{public}@ found no prefix for per-tag ESL article lists"
+ "*"
+ "-[FCFeedItemInventory _loadInventoryFromCache]"
+ "-[FCFeedItemInventory _populateScoreProfilesForFeedItems:configurationSet:]"
+ "-[FCFeedItemInventory allFeedItemScoreProfilesForConfigurationSet:scoringVersion:]"
+ "-[FCFeedItemInventory init]"
+ "-[FCGlobalCuratedESLArticlesOperation init]"
+ "-[FCGlobalESLService init]"
+ "-[FCSingleTagFeedDescriptor initWithContext:tag:sortMethod:filterOptions:personalizationConfigurationSet:feedConfiguration:referringFeedItemIdentifier:]"
+ "-[FCTagCuratedESLArticlesOperation init]"
+ "-[FCTagESLService init]"
+ "-[FCTopKESLService init]"
+ "/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedItemInventory.m"
+ "/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCGlobalCuratedESLArticlesOperation.m"
+ "/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCGlobalESLService.m"
+ "/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagCuratedESLArticlesOperation.m"
+ "/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagESLService.m"
+ "/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTopKESLService.m"
+ "/liveactivity/v1/"
+ "; articleDislikedEventCount: %lld"
+ "; articleLikedEventCount: %lld"
+ "; articleReadEventCount: %lld"
+ "; articleSavedEventCount: %lld"
+ "; articleSeenEventCount: %lld"
+ "; articleSharedEventCount: %lld"
+ "; articleVisitedEventCount: %lld"
+ "; feedViewEventCount: %lld"
+ "; filterLocationSuggestionsOnlyToAppleNewsLocal: %d"
+ "; tagFollowedEventCount: %lld"
+ "; tagMutedEventCount: %lld"
+ "; tagUnfollowedEventCount: %lld"
+ "@\"<FCFeedItemInventoryType>\""
+ "@\"<FCFeedItemServiceType>\""
+ "@\"<FCFeedItemServiceType>\"8@?0"
+ "@\"<FCPuzzleProviding>\"8@?0"
+ "@\"FCESLInventory\""
+ "@\"FCLocationSharingUpsellConfig\""
+ "@\"FCLocationSharingUpsellConfig\"16@0:8"
+ "@\"FCPBFeedItemInventory\""
+ "@\"FCUserEventHistoryAggregateCounts\""
+ "@\"FCUserEventHistoryAggregateStoreData\""
+ "@\"FCUserEventHistoryEventCounts\""
+ "@\"NSArray\"32@0:8@\"CLLocation\"16Q24"
+ "@\"NTPBDate\""
+ "@104@0:8q16q24q32q40q48q56q64q72q80q88q96"
+ "@120@0:8q16q24d32q40d48q56q64q72q80q88q96@104@112"
+ "@16@?0@\"FCLocalRegion\"8"
+ "@176@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168"
+ "@208@0:8@16@24@32@40@48@56@64@72B80q84@92@100@108@116@124@132@140@148@156@164@172q180B188B192B196@200"
+ "@212@0:8@16@24@32@40@48@56@64q72@80B88q92@100@108@116@124@132@140@148@156@164@172@180@188B196B200@204"
+ "@48@0:8@16@24Q32@40"
+ "@48@0:8@16@24Q32q40"
+ "@60@0:8@16@24@32I40d44@52"
+ "@72@0:8@16@24q32Q40q48Q56@64"
+ "AffinityGroup"
+ "B16@?0@\"FCReferenceToMembership\"8"
+ "B32@?0@\"NSString\"8@\"<FCTagProviding>\"16^B24"
+ "D''\x13/\x0f\x06\x1f\x0e\x12\x151=\x1f\x05"
+ "FCChannelPaywallConfig"
+ "FCEditorialTopicEventMappingProperty"
+ "FCFeedItemInventory"
+ "FCFeedItemInventoryType"
+ "FCFeedItemServiceType"
+ "FCGlobalCuratedESLArticlesOperation"
+ "FCGlobalESLService"
+ "FCLocationSharingUpsellConfig"
+ "FCPBFeedItemInventory"
+ "FCPuzzleFullArchiveMenuOptionItem"
+ "FCPuzzleFullArchiveMenuOptionsConfiguration"
+ "FCTagCuratedESLArticlesOperation"
+ "FCTagESLService"
+ "FCTopKESLService"
+ "FCUserEventHistoryAggregateCounts"
+ "FCUserEventHistoryAggregateStoreData"
+ "FCUserEventHistoryEventCounts"
+ "Fetching Entitlements with ignoreCaches: %d"
+ "Global"
+ "News Edge - Puzzle Archive"
+ "Newsletter Manager: account changed, resetting caches"
+ "NonBundleArticles"
+ "Per-Tag"
+ "PuzzleFullArchive"
+ "ReduceVisibilityForNonFollowers"
+ "Sports"
+ "T@\"<FCFeedItemInventoryType>\",R,N,V_globalInventory"
+ "T@\"<FCFeedItemInventoryType>\",R,N,V_tagInventory"
+ "T@\"<FCFeedItemServiceType>\",R,N,V_feedItemService"
+ "T@\"<FCNewsAppConfigurationManager>\",&,N,V_configurationManager"
+ "T@\"FCAssetHandle\",R,N,V_sportsLogoAltImageAssetHandle"
+ "T@\"FCAssetHandle\",R,N,V_sportsLogoAltImageCompactAssetHandle"
+ "T@\"FCAssetHandle\",R,N,V_sportsLogoAltImageLargeAssetHandle"
+ "T@\"FCESLInventory\",R,N,V_eslInventory"
+ "T@\"FCLocationSharingUpsellConfig\",R,N"
+ "T@\"FCLocationSharingUpsellConfig\",R,N,V_locationSharingUpsellConfig"
+ "T@\"FCPBFeedItemInventory\",&,V_latestInventory"
+ "T@\"FCPersonalizationOntologyLevelConfig\",R,N,V_affinityGroupOntologyLevelConfig"
+ "T@\"FCPersonalizationScoringConfig\",R,N,V_affinityGroupScoringConfig"
+ "T@\"FCPersonalizationTopicsConfig\",R,N,V_affinityGroupTopicsConfig"
+ "T@\"FCUserEventHistoryAggregateCounts\",&,N,V_aggregateCounts"
+ "T@\"FCUserEventHistoryAggregateCounts\",R,N"
+ "T@\"FCUserEventHistoryAggregateStoreData\",&,N,V_aggregateStoreData"
+ "T@\"FCUserEventHistoryAggregateStoreData\",R,N"
+ "T@\"FCUserEventHistoryEventCounts\",&,N,V_eventCounts"
+ "T@\"FCUserEventHistoryEventCounts\",R,N"
+ "T@\"NSArray\",R,N,V_items"
+ "T@\"NSArray\",R,N,V_shadowAffinityGroupTopicsConfig"
+ "T@\"NSDictionary\",R,N,V_channelPaywallConfigsByChannelID"
+ "T@\"NSDictionary\",R,N,V_puzzleFullArchiveMenuOptionsConfigByPuzzleTypeID"
+ "T@\"NSDictionary\",R,N,V_shadowAffinityGroupOntologyLevelConfig"
+ "T@\"NSDictionary\",R,N,V_shadowAffinityGroupScoringConfig"
+ "T@\"NSMutableArray\",&,N,V_feedItems"
+ "T@\"NSString\",C,N,V_activeiTunesAccountName"
+ "T@\"NSString\",C,N,V_referringFeedItemIdentifier"
+ "T@\"NSString\",C,N,V_sportsSecondaryShortName"
+ "T@\"NSString\",R,C,N,V_mappingType"
+ "T@\"NSString\",R,C,N,V_sportsSecondaryShortName"
+ "T@\"NSString\",R,N,V_icon"
+ "T@\"NSString\",R,N,V_loggingKey"
+ "T@\"NSString\",R,N,V_puzzleFullArchiveTagID"
+ "T@\"NSString\",R,N,V_puzzlesArchiveAPIBaseURLString"
+ "T@\"NSString\",R,N,V_sportsTopStoriesTagID"
+ "T@\"NTPBDate\",&,N,V_lastRefreshed"
+ "TB,N,GisAIGenerated,V_aiGenerated"
+ "TB,N,V_filterLocationSuggestionsOnlyToAppleNewsLocal"
+ "TB,R,N,GisAIGenerated"
+ "TB,R,N,V_filterALaCartePaidArticlesForPaidBundleSubscribers"
+ "TB,R,N,V_hasEvergreenArticleList"
+ "TB,R,N,V_puzzlesArchiveAPIEnabled"
+ "TB,R,N,V_reduceVisibilityForNonFollowers"
+ "TI,N,V_feedItemVersion"
+ "TI,N,V_inventoryVersion"
+ "TI,R,N,V_version"
+ "TQ,R,N,V_aLaCarteArticleSoftPaywallPosition"
+ "TQ,R,N,V_articleSoftPaywallPosition"
+ "TQ,R,N,V_articleSoftPaywallPositionForPaidBundleSubscribers"
+ "TQ,R,N,V_level"
+ "Td,R,N,V_puzzlesCacheLifetime"
+ "Td,R,N,V_recentPuzzlesCacheLifetime"
+ "Td,R,N,V_refreshInterval"
+ "Tq,N,V_articleDislikedEventCount"
+ "Tq,N,V_articleLikedEventCount"
+ "Tq,N,V_articleReadEventCount"
+ "Tq,N,V_articleSavedEventCount"
+ "Tq,N,V_articleSeenEventCount"
+ "Tq,N,V_articleSharedEventCount"
+ "Tq,N,V_articleVisitedEventCount"
+ "Tq,N,V_baselineStatelessEventCount"
+ "Tq,N,V_baselineTimestamp"
+ "Tq,N,V_baselineTotalEventCount"
+ "Tq,N,V_channelTopic"
+ "Tq,N,V_feedViewEventCount"
+ "Tq,N,V_group"
+ "Tq,N,V_tag"
+ "Tq,N,V_tagFollowedEventCount"
+ "Tq,N,V_tagMutedEventCount"
+ "Tq,N,V_tagUnfollowedEventCount"
+ "Tq,R,N,V_difficultyIndex"
+ "User Event History Metadata { aggregateStoreGenerationTime: %lld sessionsOnDiskSize: %lld aggregateTotalCount: %lld meanCountOfEvents: %.4f standardDeviationOfEvents: %.4f totalEventsCount: %lld headlineEventCount: %lld headlinesWithValidTitleEmbeddingsEventCount: %lld headlinesWithInvalidTitleEmbeddingsEventCount: %lld headlinesWithValidBodyEmbeddingsEventCount: %lld headlinesWithInvalidBodyEmbeddingsEventCount: %lld eventCounts: %@ aggregateStoreData: %@ }"
+ "[%{public}@] did not rescore inventory because it is no longer the latest"
+ "[%{public}@] failed to initialize inventory from cached data"
+ "[%{public}@] failed to persist with error: %{public}@"
+ "[%{public}@] failed to refresh with error: %{public}@"
+ "[%{public}@] found no cached data on disk"
+ "[%{public}@] ignoring cached data because its feed item version %u does not match the current version %u"
+ "[%{public}@] ignoring cached data because its inventory version %u does not match the current version %u"
+ "[%{public}@] loaded cached data in %llums with %lu feed items and last-refresh date %{public}@"
+ "[%{public}@] not rescoring inventory due to no score profile"
+ "[%{public}@] not rescoring inventory due to version match"
+ "[%{public}@] rescored inventory"
+ "[%{public}@] rescoring inventory because cached scored version of %llu doesn't match %llu"
+ "[%{public}@] successfully fetched %lu feed items in %llums, will generate score profiles"
+ "[%{public}@] successfully persisted with size: %{public}@"
+ "[%{public}@] successfully refreshed in %llums"
+ "[%{public}@] took %llums to generate score profiles"
+ "[%{public}@] will refresh because last refresh was at %{public}@"
+ "[%{public}@] will refresh because there is no cached instance"
+ "_aLaCarteArticleSoftPaywallPosition"
+ "_activeiTunesAccountName"
+ "_affinityGroupOntologyLevelConfig"
+ "_affinityGroupScoringConfig"
+ "_affinityGroupTopicsConfig"
+ "_aggregateCounts"
+ "_aggregateStoreData"
+ "_aiGenerated"
+ "_articleDislikedEventCount"
+ "_articleLikedEventCount"
+ "_articleReadEventCount"
+ "_articleSavedEventCount"
+ "_articleSeenEventCount"
+ "_articleSharedEventCount"
+ "_articleSoftPaywallPosition"
+ "_articleSoftPaywallPositionForPaidBundleSubscribers"
+ "_articleVisitedEventCount"
+ "_baselineStatelessEventCount"
+ "_baselineTimestamp"
+ "_baselineTotalEventCount"
+ "_channelPaywallConfigsByChannelID"
+ "_channelTopic"
+ "_childInventories"
+ "_createESLInventory"
+ "_difficultyIndex"
+ "_enumerateChildInventories:"
+ "_eventCounts"
+ "_feedItemService"
+ "_feedItemVersion"
+ "_feedViewEventCount"
+ "_filterALaCartePaidArticlesForPaidBundleSubscribers"
+ "_filterLocationSuggestionsOnlyToAppleNewsLocal"
+ "_globalInventory"
+ "_hasEvergreenArticleList"
+ "_icon"
+ "_inventoryVersion"
+ "_items"
+ "_lastRefreshed"
+ "_level"
+ "_locationSharingUpsellConfig"
+ "_mappingType"
+ "_membershipsLock"
+ "_populateScoreProfilesForFeedItems:"
+ "_populateScoreProfilesForFeedItems:configurationSet:"
+ "_progressReportedFeedItems"
+ "_promiseCuratedFeedItemsForTags:configuration:"
+ "_promiseCuratedFeedItemsWithConfiguration:"
+ "_promiseFeedItemsForTags:configuration:"
+ "_promiseRelevantTagsWithConfiguration:"
+ "_puzzleFullArchiveMenuOptionsConfigByPuzzleTypeID"
+ "_puzzleFullArchiveTagID"
+ "_puzzlesArchiveAPIBaseURLString"
+ "_puzzlesArchiveAPIEnabled"
+ "_puzzlesCacheLifetime"
+ "_recentPuzzlesCacheLifetime"
+ "_reduceVisibilityForNonFollowers"
+ "_referringFeedItemIdentifier"
+ "_refreshIfNeededWithQoS:"
+ "_refreshInterval"
+ "_shadowAffinityGroupOntologyLevelConfig"
+ "_shadowAffinityGroupScoringConfig"
+ "_shadowAffinityGroupTopicsConfig"
+ "_sportsLogoAltImageAssetHandle"
+ "_sportsLogoAltImageCompactAssetHandle"
+ "_sportsLogoAltImageLargeAssetHandle"
+ "_sportsSecondaryShortName"
+ "_sportsTopStoriesTagID"
+ "_tagFollowedEventCount"
+ "_tagInventory"
+ "_tagMutedEventCount"
+ "_tagUnfollowedEventCount"
+ "_tags"
+ "aLaCarteArticleSoftPaywallPosition"
+ "activeiTunesAccountName"
+ "addFeedItems:"
+ "affinityGroupOntologyLevelConfig"
+ "affinityGroupScoringConfig"
+ "affinityGroupTopicsConfig"
+ "aggregateCounts"
+ "aggregateStoreData"
+ "aiGenerated"
+ "articleDislikedEventCount"
+ "articleLikedEventCount"
+ "articleReadEventCount"
+ "articleSavedEventCount"
+ "articleSeenEventCount"
+ "articleSharedEventCount"
+ "articleSoftPaywallPosition"
+ "articleSoftPaywallPositionForPaidBundleSubscribers"
+ "articleVisitedEventCount"
+ "baselineStatelessEventCount"
+ "baselineTimestamp"
+ "baselineTotalEventCount"
+ "both"
+ "centerLocationCoordinateForEntireRegion"
+ "channelPaywallConfigsByChannelID"
+ "channelPaywallConfigurations"
+ "channelTopic"
+ "contentTriggerDampener"
+ "createPuzzleForPuzzleType:identifier:title:subtitle:puzzleDescription:dataResourceID:authors:behaviorFlags:publishDate:isPaid:difficulty:difficultyDescription:thumbnailLargeURL:loadDate:teaserClue:teaserAnswer:teaserInfo:teaserDirection:teaserNumber:language:blockedStorefrontIDs:allowedStorefrontIDs:minimumNewsVersion:isDeprecated:isDraft:lastModifiedDate:"
+ "defaultDeviceInfo"
+ "did fetch %lu global evergreen feed items"
+ "did fetch %lu tag evergreen feed items"
+ "difficulty-10"
+ "difficulty-20"
+ "difficulty-30"
+ "difficultyIndex"
+ "distanceFromLocation:"
+ "downloadIfNeededWithGroup:completion:"
+ "editorialTopicEventMappingProperties"
+ "emptyWithSessionsOnDiskSize:personalizationAnalyticsEnabled:"
+ "enableAIAttribution"
+ "enable_ai_attribution"
+ "eventCounts"
+ "feedItemService"
+ "feedViewEventCount"
+ "feed_item_version"
+ "feed_items"
+ "fetchFeedItemsWithCompletion:"
+ "filterALaCartePaidArticlesForPaidBundleSubscribers"
+ "filterLocationSuggestionsOnlyToAppleNewsLocal"
+ "freeGlobalESLArticleListIDs"
+ "freeTagESLArticleListIDPrefix"
+ "freeTagEvergreenArticleListIdPrefix"
+ "generateSportsLogoAltImageAssetHandleWithAssetManager:"
+ "generateSportsLogoAltImageCompactAssetHandleWithAssetManager:"
+ "generateSportsLogoAltImageLargeAssetHandleWithAssetManager:"
+ "globalInventory"
+ "hasEvergreenArticleList"
+ "icon"
+ "initWithAggregateStoreGenerationTime:aggregateTotalCount:meanCountOfEvents:sessionsOnDiskSize:standardDeviationOfEvents:totalEventsCount:headlineEventCount:headlinesWithValidTitleEmbeddingsEventCount:headlinesWithInvalidTitleEmbeddingsEventCount:headlinesWithValidBodyEmbeddingsEventCount:headlinesWithInvalidBodyEmbeddingsEventCount:eventCounts:aggregateStoreData:"
+ "initWithArticleSeenEventCount:articleVisitedEventCount:articleReadEventCount:articleLikedEventCount:articleDislikedEventCount:articleSharedEventCount:articleSavedEventCount:feedViewEventCount:tagFollowedEventCount:tagUnfollowedEventCount:tagMutedEventCount:"
+ "initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:puzzlesArchiveAPIBaseURLString:appAnalyticsNotificationReceiptBaseURLString:authTokenAPIBaseURLString:sportsDataVisualizationAPIBaseURLString:fineGrainedNewsletterSubscriptionBaseURLString:appAnalyticsSportsEventsBaseURLString:appAnalyticsAppHealthBaseURLString:ckOrderFeedBaseURLString:ckMultiFetchBaseURLString:ckRecordFetchBaseURLString:ckEdgeCachedOrderFeedBaseURLString:ckEdgeCachedMultiFetchBaseURLString:"
+ "initWithContext:feedItemService:filePath:version:refreshInterval:loggingKey:"
+ "initWithContext:tag:feedConfiguration:referringFeedItemIdentifier:"
+ "initWithContext:tag:sortMethod:filterOptions:personalizationConfigurationSet:feedConfiguration:referringFeedItemIdentifier:"
+ "initWithGlobalInventory:tagInventory:"
+ "initWithIdentifier:title:subtitle:puzzleDescription:puzzleType:dataResourceID:authors:publishDate:isPaid:difficulty:difficultyDescription:thumbnailLargeImageAssetHandle:loadDate:teaserClue:teaserAnswer:teaserInfo:teaserDirection:teaserNumber:language:blockedStorefrontIDs:allowedStorefrontIDs:minimumNewsVersion:showInfoModalOnFirstPlay:isDeprecated:isDraft:lastModifiedDate:"
+ "initWithLatitude:longitude:"
+ "initWithPrivateDataDirectory:configurationManager:"
+ "initWithTags:context:configuration:bundleSubscriptionManager:"
+ "initWithTitle:icon:level:difficultyIndex:"
+ "inventory_version"
+ "isAIGenerated"
+ "keysSortedByValueUsingComparator:"
+ "last_refreshed"
+ "level"
+ "liveActivitiesEnabled"
+ "liveActivitiesEnabledLevel"
+ "liveActivityAssetServerURLs"
+ "liveActivityBaseURLForConfiguration:"
+ "locationSharingUpsellConfig"
+ "locationSharingUpsellConfiguration"
+ "mappingType"
+ "maxTagESLArticleListsToQuery"
+ "maxTagEvergreenArticleListsToQuery"
+ "moreFromIssueEOAEnabled"
+ "moreFromIssueEOAEnabledLevel"
+ "moreToReadEOAEnabled"
+ "moreToReadEOAEnabledLevel"
+ "multiplier"
+ "news.esl_inventory.clear_global_next_launch"
+ "news.esl_inventory.force_enable_all_tags"
+ "news.esl_inventory.simulate_with_top_k"
+ "news.features.personalizationAnalytics"
+ "news.news_personalization.should_filter_location_suggestions_only_to_apple_news_local"
+ "news.news_personalization.should_override_local_channel_picker_configuration"
+ "nicheContentMultiplier"
+ "none"
+ "paidGlobalESLArticleListIDs"
+ "paidTagESLArticleListIDPrefix"
+ "paidTagEvergreenArticleListIdPrefix"
+ "personalizationAnalytics"
+ "personalizationAnalyticsEnabled"
+ "prewarmScoreCache:configuration:"
+ "progress"
+ "progress-completed"
+ "progress-inprogress"
+ "progress-unplayed"
+ "propertyFlagsLocalized"
+ "puzzleFullArchiveMenuOptionsConfigByPuzzleTypeID"
+ "puzzleFullArchiveTagID"
+ "puzzleFullArchiveTagId"
+ "puzzlesArchiveAPIBaseURLString"
+ "puzzlesArchiveAPIEnabled"
+ "puzzlesArchiveApiBaseUrl"
+ "puzzlesArchiveBaseURLForConfiguration"
+ "puzzlesArchiveBaseURLForConfiguration:"
+ "puzzlesCacheLifetime"
+ "puzzlesFullArchiveMenuConfig"
+ "q24@?0@\"NSNumber\"8@\"NSNumber\"16"
+ "readBool:"
+ "readObject:"
+ "recentPuzzlesCacheLifetime"
+ "reduceVisibilityForNonFollowers"
+ "referringFeedItemIdentifier"
+ "refreshIfNeededWithCompletion:"
+ "refreshInterval"
+ "savePuzzleToCache:"
+ "secondaryShortName"
+ "serverScoreDemocratizationFactor"
+ "setActiveiTunesAccountName:"
+ "setAggregateCounts:"
+ "setAggregateStoreData:"
+ "setAiGenerated:"
+ "setArticleDislikedEventCount:"
+ "setArticleLikedEventCount:"
+ "setArticleReadEventCount:"
+ "setArticleSavedEventCount:"
+ "setArticleSeenEventCount:"
+ "setArticleSharedEventCount:"
+ "setArticleVisitedEventCount:"
+ "setBaselineStatelessEventCount:"
+ "setBaselineTimestamp:"
+ "setBaselineTotalEventCount:"
+ "setChannelTopic:"
+ "setEventCounts:"
+ "setFeedViewEventCount:"
+ "setFilterLocationSuggestionsOnlyToAppleNewsLocal:"
+ "setMetadataWithAggregateStoreGenerationTime:aggregateTotalCount:meanCountOfEvents:standardDeviationOfEvents:totalEventsCount:headlineEventCount:headlinesWithValidTitleEmbeddingsEventCount:headlinesWithInvalidTitleEmbeddingsEventCount:headlinesWithValidBodyEmbeddingsEventCount:headlinesWithInvalidBodyEmbeddingsEventCount:eventCounts:aggregateStoreData:"
+ "setPropertyFlagsLocalized:"
+ "setReduceVisibilityForNonFollowers:"
+ "setReferringFeedItemIdentifier:"
+ "setSportsLogoAltImageCompactURL:"
+ "setSportsLogoAltImageLargeURL:"
+ "setSportsLogoAltImageURL:"
+ "setSportsSecondaryShortName:"
+ "setTagFollowedEventCount:"
+ "setTagMutedEventCount:"
+ "setTagUnfollowedEventCount:"
+ "shadowAffinityGroupOntologyLevelConfig"
+ "shadowAffinityGroupScoringConfig"
+ "shadowAffinityGroupTopicsConfig"
+ "shortSecondaryName"
+ "sportsLogoAltImage"
+ "sportsLogoAltImageAssetHandle"
+ "sportsLogoAltImageCompact"
+ "sportsLogoAltImageCompactAssetHandle"
+ "sportsLogoAltImageCompactURL"
+ "sportsLogoAltImageLarge"
+ "sportsLogoAltImageLargeAssetHandle"
+ "sportsLogoAltImageLargeURL"
+ "sportsLogoAltImageURL"
+ "sportsParentTagIdentifiers"
+ "sportsSecondaryShortName"
+ "sportsSyncingConfigurationV2ResourceId"
+ "sportsSyncingV2Enabled"
+ "sportsSyncingV2EnabledLevel"
+ "sportsTopStoriesTagID"
+ "sportsTopStoriesTagId"
+ "tag-esl-inventory"
+ "tagFollowedEventCount"
+ "tagIDsForLocation:searchOption:"
+ "tagInventory"
+ "tagMutedEventCount"
+ "tagSubscriptionRepromptDelay"
+ "tagUnfollowedEventCount"
+ "tag_url_subscription_prompt_dates"
+ "todayFeedEditionConfigJSON"
+ "todayFeedEditionConfigJson"
+ "v112@0:8q16q24d32d40q48q56q64q72q80q88@\"FCUserEventHistoryEventCounts\"96@\"FCUserEventHistoryAggregateStoreData\"104"
+ "v112@0:8q16q24d32d40q48q56q64q72q80q88@96@104"
+ "v16@?0@\"<FCFeedItemInventoryType>\"8"
+ "v20@0:8I16"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "webEmbedDataSourcesConfigurationResourceId"
+ "will fetch global evergreen feed items with operation: %{public}@"
+ "will fetch tag evergreen feed items with operation: %{public}@"
+ "{?=\"feedItemVersion\"b1\"inventoryVersion\"b1}"
+ "{CLLocationCoordinate2D=dd}16@0:8"
+ "\xb2"
- "\x01Q"
- "\x02\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0/\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\a"
- "\x03\x11"
- "\x05\"\x16\x14"
- "\r"
- "\x0f\x04"
- "\x12A"
- "\x14\x11#"
- "\x14\x13"
- "\x17\x16\x17"
- "\x19\x12\x11"
- "\x1a\x1e\x12\x18\x15"
- "\x1f\x0f\r"
- "%{public}@ will incorporate %lu evergreen feed items, lookup time=%llums"
- "-[FCESLInventory _loadInventoryFromCache]"
- "-[FCESLInventory allFeedItemScoreProfilesForConfigurationSet:scoringVersion:]"
- "-[FCESLInventory init]"
- "-[FCESLInventory populateScoreProfilesForFeedItems:configurationSet:]"
- "-[FCEvergreenArticlesOperation init]"
- "-[FCSingleTagFeedDescriptor initWithContext:tag:sortMethod:filterOptions:personalizationConfigurationSet:feedConfiguration:]"
- "/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCESLInventory.m"
- "/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCEvergreenArticlesOperation.m"
- "@\"<FCESLInventoryType>\""
- "@\"NTPBFeedItemInventory\""
- "@104@0:8q16q24d32q40d48q56q64q72q80q88q96"
- "@112@0:8@16@24@32@40@48@56@64@72@80@88@96@104"
- "@120@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112"
- "@16@?0@\"NTPBFeedItemInventory\"8"
- "@200@0:8@16@24@32@40@48@56@64@72B80q84@92@100@108@116@124@132@140@148@156@164@172q180B188B192B196"
- "@56@0:8q16q24q32@40@48"
- "@648@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232@240@248@256@264@272@280@288@296@304@312@320@328@336@344@352@360@368@376@384@392@400@408@416@424@432@440@448@456@464@472@480@488@496@504@512@520@528@536@544@552@560@568@576@584@592@600@608@616@624@632@640"
- "@76@0:8q16q24B32q36q44@52@60@68"
- "D''\x13/\x0f\x06\x1f\n\x12\x151=\x1f\x05"
- "FCESLInventoryType"
- "FCEvergreenArticlesOperation"
- "T@\"<FCESLInventoryType>\",R,N,V_eslInventory"
- "T@\"NSString\",R,N,V_cacheDataPath"
- "T@\"NTPBFeedItemInventory\",&,V_latestInventory"
- "TB,N,V_scoreFeedItems"
- "User Event History Metadata { aggregateStoreGenerationTime: %lu sessionsOnDiskSize: %lu aggregateTotalCount: %lu meanCountOfEvents: %.4f standardDeviationOfEvents: %.4f totalEventsCount: %lu headlineEventCount: %lu headlinesWithValidTitleEmbeddingsEventCount: %lu headlinesWithInvalidTitleEmbeddingsEventCount: %lu headlinesWithValidBodyEmbeddingsEventCount: %lu headlinesWithInvalidBodyEmbeddingsEventCount: %lu }"
- "_cacheDataPath"
- "_promiseEvergreenFeedItemsWithConfiguration:"
- "_scoreFeedItems"
- "cacheDataPath"
- "defaultDeviceInfoWithAppVersion:formatVersion:seedNumber:buildNumber:"
- "did fetch %lu evergreen feed items"
- "did not rescore inventory because it is no longer the latest"
- "emptyWithSessionsOnDiskSize:"
- "failed to initialize inventory from cached data"
- "failed to persist with error: %{public}@"
- "failed to refresh with error: %{public}@"
- "feedContentExposureTestMaximumInterval"
- "found no cached data on disk"
- "freeEvergreenArticleListIDs"
- "ignoring cached data because its feed item version %u does not match the current version %u"
- "ignoring cached data because its inventory version %u does not match the current version %u"
- "initWithAggregateStoreGenerationTime:aggregateTotalCount:meanCountOfEvents:sessionsOnDiskSize:standardDeviationOfEvents:totalEventsCount:headlineEventCount:headlinesWithValidTitleEmbeddingsEventCount:headlinesWithInvalidTitleEmbeddingsEventCount:headlinesWithValidBodyEmbeddingsEventCount:headlinesWithInvalidBodyEmbeddingsEventCount:"
- "initWithArticleSeenConditions:articleReadConditions:articleVisitedConditions:articleSharedConditions:articleLikedConditions:articleDislikedConditions:articleSavedConditions:trackVisitedConditions:trackListenedConditions:trackFinishedConditions:articleUnlikedConditions:articleUndislikedConditions:articleUnsavedConditions:"
- "initWithBundleInputOutputConfiguration:nonBundleInputOutputConfiguration:userContextConfiguration:"
- "initWithClientAPIBaseURLString:notificationsBaseURLString:"
- "initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:"
- "initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:"
- "initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:"
- "initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:"
- "initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:"
- "initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:appAnalyticsNotificationReceiptBaseURLString:"
- "initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:appAnalyticsNotificationReceiptBaseURLString:authTokenAPIBaseURLString:"
- "initWithClientAPIBaseURLString:notificationsBaseURLString:staticAssetBaseURLString:remoteDataSourceBaseURLString:newsletterAPIBaseURLString:appAnalyticsBaseURLString:fairPlayBaseURLString:searchAPIBaseURLString:appAnalyticsNotificationReceiptBaseURLString:authTokenAPIBaseURLString:sportsDataVisualizationAPIBaseURLString:fineGrainedNewsletterSubscriptionBaseURLString:"
- "initWithContext:cacheDirectory:"
- "initWithContextFeatureKey:channelIDsOutputName:scoresOutputName:"
- "initWithContextFeatureKey:generalChannelSuggestionsOutputName:generalChannelSuggestionsScoreOutputName:newsPlusChannelSuggestionsOutputName:newsPlusChannelSuggestionsScoreOutputName:"
- "initWithContextFeatureKey:recommendedIssuePublisherOutputName:recommendedIssuePublisherScoreOutputName:"
- "initWithIdentifier:title:subtitle:puzzleDescription:puzzleType:dataResourceID:authors:publishDate:isPaid:difficulty:difficultyDescription:thumbnailLargeImageAssetHandle:loadDate:teaserClue:teaserAnswer:teaserInfo:teaserDirection:teaserNumber:language:blockedStorefrontIDs:allowedStorefrontIDs:minimumNewsVersion:showInfoModalOnFirstPlay:isDeprecated:isDraft:"
- "initWithMaxTopicIds:maxSessionEvents:readEventsOnly:titleEmbeddingDimension:fullBodyEmbeddingDimension:bundleOutputConfiguration:nonBundleOutputConfiguration:eventConditions:"
- "initWithMaxTopicIds:titleEmbeddingDimension:fullBodyEmbeddingDimension:bundleOutputConfiguration:nonBundleOutputConfiguration:"
- "initWithOutputNames:"
- "initWithTagScoringOutputName:defaultHeadlineScoringOutputName:topicFeedHeadlineScoringOutputName:magazineFeedHeadlineScoringOutputName:magazineFeedIssuesHeadlineScoringOutputName:legacyAudioFeedHeadlineScoringOutputName:audioFeedHeadlineScoringOutputName:articleRecirculationPrimaryHeadlineScoringOutputName:articleRecirculationSecondaryHeadlineScoringOutputName:articleRecirculationTertiaryHeadlineScoringOutputName:articleRecirculationQuaternaryHeadlineScoringOutputName:bestOfBundleHeadlineScoringOutputName:forYouGroupHeadlineScoringOutputName:greatStoriesYouMissedGroupHeadlineScoringOutputName:latestStoriesGroupHeadlineScoringOutputName:localNewsGroupHeadlineScoringOutputName:newspaperGroupMagazineFeedHeadlineScoringOutputName:todayWidgetHeadlineScoringOutputName:tagWidgetHeadlineScoringOutputName:notificationHeadlineScoringOutputName:mySportsGroupHeadlineScoringOutputName:sportsTopStoriesHeadlineScoringOutputName:introToSportsGroupHeadlineScoringOutputName:highlightsGroupHeadlineScoringOutputName:articleListTagFeedGroupHeadlineScoringOutputName:tagFeedHeadlineScoringOutputName:newspaperGroupTodayFeedHeadlineScoringOutputName:moreForYouGroupHeadlineScoringOutputName:introToSportsGroupForYouHeadlineScoringOutputName:mySportsGroupForYouHeadlineScoringOutputName:mySportsTopicsHeadlineScoringOutputName:curatedGroupHeadlineScoringOutputName:curatedGroupIssuesHeadlineScoringOutputName:localSectionGroupHeadlineScoringOutputName:newspaperSectionGroupHeadlineScoringOutputName:sportsEventArticlesGroupHeadlineScoringOutputName:tagFeedForYouGroupHeadlineScoringOutputName:tagRecentStoriesGroupHeadlineScoringOutputName:tagDateRangeGroupHeadlineScoringOutputName:sportsEventTopicGroupHeadlineScoringOutputName:shadowDefaultHeadlineScoringOutputName:shadowTopicFeedHeadlineScoringOutputName:shadowMagazineFeedHeadlineScoringOutputName:shadowMagazineFeedIssuesHeadlineScoringOutputName:shadowLegacyAudioFeedHeadlineScoringOutputName:shadowAudioFeedHeadlineScoringOutputName:shadowArticleRecirculationPrimaryHeadlineScoringOutputName:shadowArticleRecirculationSecondaryHeadlineScoringOutputName:shadowArticleRecirculationTertiaryHeadlineScoringOutputName:shadowArticleRecirculationQuaternaryHeadlineScoringOutputName:shadowBestOfBundleHeadlineScoringOutputName:shadowForYouGroupHeadlineScoringOutputName:shadowGreatStoriesYouMissedGroupHeadlineScoringOutputName:shadowLatestStoriesGroupHeadlineScoringOutputName:shadowLocalNewsGroupHeadlineScoringOutputName:shadowNewspaperGroupMagazineFeedHeadlineScoringOutputName:shadowTodayWidgetHeadlineScoringOutputName:shadowTagWidgetHeadlineScoringOutputName:shadowNotificationHeadlineScoringOutputName:shadowMySportsGroupHeadlineScoringOutputName:shadowSportsTopStoriesHeadlineScoringOutputName:shadowIntroToSportsGroupHeadlineScoringOutputName:shadowHighlightsGroupHeadlineScoringOutputName:shadowArticleListTagFeedGroupHeadlineScoringOutputName:shadowTagFeedHeadlineScoringOutputName:shadowNewspaperGroupTodayFeedHeadlineScoringOutputName:shadowMoreForYouGroupHeadlineScoringOutputName:shadowIntroToSportsGroupForYouHeadlineScoringOutputName:shadowMySportsGroupForYouHeadlineScoringOutputName:shadowMySportsTopicsHeadlineScoringOutputName:shadowCuratedGroupHeadlineScoringOutputName:shadowCuratedGroupIssuesHeadlineScoringOutputName:shadowLocalSectionGroupHeadlineScoringOutputName:shadowNewspaperSectionGroupHeadlineScoringOutputName:shadowSportsEventArticlesGroupHeadlineScoringOutputName:shadowTagFeedForYouGroupHeadlineScoringOutputName:shadowTagRecentStoriesGroupHeadlineScoringOutputName:shadowTagDateRangeGroupHeadlineScoringOutputName:shadowSportsEventTopicGroupHeadlineScoringOutputName:"
- "loaded cached data in %llums with %lu feed items and last-refresh date %{public}@"
- "noConditions"
- "not rescoring inventory due to no score profile"
- "not rescoring inventory due to version match"
- "paidEvergreenArticleListIDs"
- "populateScoreProfilesForFeedItems:"
- "populateScoreProfilesForFeedItems:configurationSet:"
- "prewarmScoreCache:"
- "rescored inventory"
- "rescoring inventory because cached scored version of %llu doesn't match %llu"
- "scoreFeedItems"
- "setMetadataWithAggregateStoreGenerationTime:aggregateTotalCount:meanCountOfEvents:standardDeviationOfEvents:totalEventsCount:headlineEventCount:headlinesWithValidTitleEmbeddingsEventCount:headlinesWithInvalidTitleEmbeddingsEventCount:headlinesWithValidBodyEmbeddingsEventCount:headlinesWithInvalidBodyEmbeddingsEventCount:"
- "setScoreFeedItems:"
- "successfully persisted with size: %{public}@"
- "successfully refreshed with %lu total feed items"
- "took %llums to generate score profiles"
- "v96@0:8q16q24d32d40q48q56q64q72q80q88"
- "will fetch evergreen feed items with operation: %{public}@"
- "will refresh because last refresh was at %{public}@"
- "will refresh because there is no cached instance"

```
