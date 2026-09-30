## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient`

```diff

-588.12.0.0.0
-  __TEXT.__text: 0x1781b0
-  __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_methlist: 0x17584
+610.0.11.0.0
+  __TEXT.__text: 0x18a5f4
+  __TEXT.__auth_stubs: 0xf00
+  __TEXT.__objc_methlist: 0x1893c
   __TEXT.__const: 0x6f8
-  __TEXT.__cstring: 0x1a62c
-  __TEXT.__oslogstring: 0x16840
-  __TEXT.__gcc_except_tab: 0x21f0
+  __TEXT.__cstring: 0x1b514
+  __TEXT.__oslogstring: 0x171bd
+  __TEXT.__gcc_except_tab: 0x22d0
   __TEXT.__dlopen_cstrs: 0x3d0
   __TEXT.__ustring: 0x18a
-  __TEXT.__unwind_info: 0x60b0
-  __TEXT.__objc_classname: 0x3825
-  __TEXT.__objc_methname: 0x31351
-  __TEXT.__objc_methtype: 0x64fd
-  __TEXT.__objc_stubs: 0x1b4e0
-  __DATA_CONST.__got: 0x1680
-  __DATA_CONST.__const: 0x5e98
-  __DATA_CONST.__objc_classlist: 0xd40
-  __DATA_CONST.__objc_catlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x248
+  __TEXT.__unwind_info: 0x65a0
+  __TEXT.__objc_classname: 0x3bbb
+  __TEXT.__objc_methname: 0x33d9c
+  __TEXT.__objc_methtype: 0x675a
+  __TEXT.__objc_stubs: 0x1c900
+  __DATA_CONST.__got: 0x16f0
+  __DATA_CONST.__const: 0x62d0
+  __DATA_CONST.__objc_classlist: 0xe40
+  __DATA_CONST.__objc_catlist: 0x90
+  __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9680
-  __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__objc_superrefs: 0xb70
-  __DATA_CONST.__objc_arraydata: 0xae8
-  __AUTH_CONST.__auth_got: 0x770
-  __AUTH_CONST.__const: 0x2720
-  __AUTH_CONST.__cfstring: 0x14220
-  __AUTH_CONST.__objc_const: 0x42960
-  __AUTH_CONST.__objc_intobj: 0xa08
-  __AUTH_CONST.__objc_arrayobj: 0x6a8
+  __DATA_CONST.__objc_selrefs: 0x9df8
+  __DATA_CONST.__objc_protorefs: 0xb0
+  __DATA_CONST.__objc_superrefs: 0xc48
+  __DATA_CONST.__objc_arraydata: 0xaf8
+  __AUTH_CONST.__auth_got: 0x790
+  __AUTH_CONST.__const: 0x2a20
+  __AUTH_CONST.__cfstring: 0x14f60
+  __AUTH_CONST.__objc_const: 0x45c00
+  __AUTH_CONST.__objc_intobj: 0xa38
+  __AUTH_CONST.__objc_arrayobj: 0x6d8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x168
-  __AUTH.__objc_data: 0x2738
-  __DATA.__objc_ivar: 0x1b14
-  __DATA.__data: 0x1bb0
-  __DATA.__bss: 0x2f8
-  __DATA_DIRTY.__objc_data: 0x5d48
+  __AUTH.__objc_data: 0x3d90
+  __DATA.__objc_ivar: 0x1c50
+  __DATA.__data: 0x1cf0
+  __DATA.__bss: 0x378
+  __DATA_DIRTY.__objc_data: 0x50f0
   __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0x2b8
+  __DATA_DIRTY.__bss: 0x2c8
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppPredictionFoundation.framework/AppPredictionFoundation
   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams

   - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
   - /System/Library/PrivateFrameworks/ProactiveContextClient.framework/ProactiveContextClient
   - /System/Library/PrivateFrameworks/ProactiveEventTracker.framework/ProactiveEventTracker
+  - /System/Library/PrivateFrameworks/ProactivePredictionClient.framework/ProactivePredictionClient
   - /System/Library/PrivateFrameworks/ProactiveSuggestionClientModel.framework/ProactiveSuggestionClientModel
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 5FC0E22D-21B4-352A-A8DD-9379141927AC
-  Functions: 10133
-  Symbols:   33467
-  CStrings:  15227
+  UUID: 9E53C382-6FF2-3FBA-AB1C-21414C6838DD
+  Functions: 10616
+  Symbols:   34957
+  CStrings:  15916
 
Symbols:
+ +[ATXAppDisplayIdentifiers _allIdentifiersIncludingRemoteApps:includeInternalMacOSApps:]
+ +[ATXAppDisplayIdentifiers _appIdentifiersIncludingRemoteApps:includeInternalMacOSApps:]
+ +[ATXAppDisplayIdentifiers _processIdentifiersFromEnumerator:intoSet:withSupportedAppPaths:includeInternalMacOSApps:]
+ +[ATXAppIdentity currentAppIdentity]
+ +[ATXAppIdentity descriptionForAppType:]
+ +[ATXAppIdentity supportsSecureCoding]
+ +[ATXApplicationRecord isAppleOwnedAppForBundleId:]
+ +[ATXApplicationRecord isAppleOwnedIncludingInternalOrSystemAppForBundleId:]
+ +[ATXDefaultHomeScreenItemManager _descriptorsByFilteringDescriptors:variant:fromAppsDisabledOnHomeScreen:fromExcludedWidgetsWithIdentifiers:personaIdentifier:]
+ +[ATXDefaultHomeScreenItemManager shouldFilterOutWidgetDescriptorDueToDenyList:fromExcludedWidgetsWithIdentifiers:]
+ +[ATXDefaultHomeScreenItemUpdater atxHomeScreenStackConfigFromATXWidgetStack:]
+ +[ATXDefaultHomeScreenItemUpdater atxHomeScreenWidgetIdentifierFromATXWidget:]
+ +[ATXDocumentCategory localizedStringForCategoryID:]
+ +[ATXDocumentInteraction supportsSecureCoding]
+ +[ATXDocumentInteractionDonationClient shared]
+ +[ATXDocumentInteractionDonationClient shared].cold.1
+ +[ATXDocumentPredictionClient categoriesForRequest:withReply:]
+ +[ATXDocumentPredictionClient(Demo) _demoDocumentsPath]
+ +[ATXDocumentPredictionClient(Demo) _getDocumentsForDemoMode]
+ +[ATXDocumentPredictionClient(Demo) _getDocumentsForDemoMode].cold.1
+ +[ATXDocumentPredictionClient(Demo) _getDocumentsForDemoMode].cold.2
+ +[ATXDocumentPredictionClient(Demo) _isDemoModeEnabled]
+ +[ATXDocumentRegexFilter sharedInstance]
+ +[ATXDocumentRegexFilter sharedInstance].cold.1
+ +[ATXDonationManager sharedManager]
+ +[ATXDonationManager sharedManager].cold.1
+ +[ATXFileIdentity supportsSecureCoding]
+ +[ATXHomeScreenConfigCache loadHomeScreenAndTodayPageConfigurationsFromJSONAtPath:error:]
+ +[ATXMenuItemDonationClient shared]
+ +[ATXMenuItemDonationClient shared].cold.1
+ +[ATXMenuItemIdentity supportsSecureCoding]
+ +[ATXMenuItemInvocation stringForMenuItemInvocationType:]
+ +[ATXMenuItemInvocation stringForMenuItemInvocationType:].cold.1
+ +[ATXMenuItemInvocation stringForMenuItemSourceType:]
+ +[ATXMenuItemInvocation stringForMenuItemSourceType:].cold.1
+ +[ATXMenuItemInvocation supportsSecureCoding]
+ +[ATXMenuItemRegexFilter joinComponentsOfMenuItemPath:]
+ +[ATXMenuItemRegexFilter sharedInstance]
+ +[ATXMenuItemRegexFilter sharedInstance].cold.1
+ +[ATXPBAction menuItemPathComponentType]
+ +[ATXPBAction parameterKeysForToolInvocationType]
+ +[ATXPBSpotlightEvent documentSuggestionIdsType]
+ +[ATXPredictedDocumentCacheItem supportsSecureCoding]
+ +[ATXPredictedDocumentIdentity documentSuggestionTypeFromString:]
+ +[ATXPredictedDocumentIdentity stringForDocumentSuggestionType:]
+ +[ATXPredictedDocumentIdentity supportsSecureCoding]
+ +[ATXRegexFilter _compilePatterns:assetName:ruleName:]
+ +[ATXSettingsAction isActionEligibleForAnySettingsSuggestions:]
+ +[ATXSettingsAction isActionEligibleForAnySettingsSuggestionsWithBundleIdentifier:actionIdentifier:]
+ +[ATXSettingsAction isActionEligibleForWatchAppSettingsSuggestions:]
+ +[ATXSpotlightClient _responseWithSpotlightLayout:andSpotlightRecentTopics:actionScope:limit:]
+ +[ATXSpotlightClient _resultWithIntent:title:subtitle:bundleIdForDisplay:appIcon:].cold.2
+ +[ATXSpotlightClient _suggestedResultResponseWithLimit:andSpotlightRecentTopics:actionScope:]
+ +[ATXSpotlightClient descriptionForTopic:]
+ +[ATXSpotlightClient isValidSuggestion:forScope:]
+ +[ATXSpotlightClient predictionsForRequest:withCompletion:]
+ +[ATXSpotlightClient zkwPredictionsForRequest:error:]
+ +[ATXSpotlightEvent(Initializers) documentSuggestionTappedWithPath:date:]
+ +[ATXToolKitActionStream sanitizeTitleForToolKitIntents:withCompletion:]
+ +[ATXToolKitActionStream sanitizeTitleForToolKitIntents:withCompletion:].cold.1
+ +[ATXUserEducationSuggestionPosterSetup suggestionType]
+ +[ATXUserEducationSuggestionPosterSetup supportsSecureCoding]
+ +[ATXWidgetClientIdentity supportsSecureCoding]
+ +[ATXWidgetGalleryRequest supportsSecureCoding]
+ +[ATXWidgetGalleryResponse supportsSecureCoding]
+ +[ATXWidgetSmartStackRequest supportsSecureCoding]
+ +[ATXWidgetSmartStackResponse supportsSecureCoding]
+ -[ATXAction encodedToolInvocation]
+ -[ATXAction initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:menuItemPath:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:toolInvocationID:encodedToolInvocation:parameterKeysForToolInvocation:]
+ -[ATXAction initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:menuItemPath:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:toolInvocationID:encodedToolInvocation:parameterKeysForToolInvocation:].cold.1
+ -[ATXAction initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:menuItemPath:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:toolInvocationID:encodedToolInvocation:parameterKeysForToolInvocation:].cold.2
+ -[ATXAction initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:menuItemPath:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:toolInvocationID:encodedToolInvocation:parameterKeysForToolInvocation:].cold.3
+ -[ATXAction initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:menuItemPath:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:toolInvocationID:encodedToolInvocation:parameterKeysForToolInvocation:].cold.4
+ -[ATXAction initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:menuItemPath:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:toolInvocationID:encodedToolInvocation:parameterKeysForToolInvocation:].cold.5
+ -[ATXAction initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:menuItemPath:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:toolInvocationID:encodedToolInvocation:parameterKeysForToolInvocation:].cold.6
+ -[ATXAction initWithMenuItemPath:actionUUID:bundleId:title:subtitle:]
+ -[ATXAction initWithToolID:encodedToolKitAction:actionUUID:parameterKeys:bundleId:title:subtitle:]
+ -[ATXAction menuItemPath]
+ -[ATXAction obfuscatedJsonWithMapping:]
+ -[ATXAction parameterKeysForToolInvocation]
+ -[ATXAction setTitle:]
+ -[ATXAction toolInvocationID]
+ -[ATXActionScope .cxx_destruct]
+ -[ATXActionScope actionType]
+ -[ATXActionScope appEntityKeyValueMapping]
+ -[ATXActionScope appIdentifier]
+ -[ATXActionScope description]
+ -[ATXActionScope hash]
+ -[ATXActionScope initWithAppIdentifier:]
+ -[ATXActionScope initWithAppIdentifier:appEntityKeyValueMapping:actionType:intentClassName:error:]
+ -[ATXActionScope intentClassName]
+ -[ATXActionScope isEqual:]
+ -[ATXActionScope isEqualToATXActionScope:]
+ -[ATXActionScope type]
+ -[ATXActionSuggestionRequest .cxx_destruct]
+ -[ATXActionSuggestionRequest initWithLimit:scope:spotlightRecentTopics:]
+ -[ATXActionSuggestionRequest setSpotlightRecentTopics:]
+ -[ATXActionSuggestionRequest spotlightRecentTopics]
+ -[ATXAppDirectoryCategory appIdentities]
+ -[ATXAppDirectoryCategory initWithCategoryID:appIdentities:]
+ -[ATXAppDirectoryCategory initWithCategoryID:appIdentitites:localizedName:]
+ -[ATXAppDirectoryCategory initWithCategoryID:appIdentitites:localizedName:].cold.1
+ -[ATXAppDirectoryClient getDirectoryResponseFromCacheWithMaxNumberOfAppsToPredict:]
+ -[ATXAppDirectoryClient getDirectoryResponseFromCacheWithMaxNumberOfAppsToPredict:].cold.1
+ -[ATXAppDirectoryResponse initWithSuggestionLayout:includeRemoteApps:recentApps:hiddenApps:otherAppsOnScreen:numAppsToPredict:error:]
+ -[ATXAppDirectoryResponse initWithSuggestionLayout:includeRemoteApps:recentApps:hiddenApps:otherAppsOnScreen:numAppsToPredict:error:].cold.1
+ -[ATXAppDirectoryResponse predictedAppIdentities]
+ -[ATXAppDirectoryResponse proactiveSuggestionForIdentity:]
+ -[ATXAppDirectoryResponse recentAppIdentities]
+ -[ATXAppDirectoryResponse uuidForIdentities:]
+ -[ATXAppDirectoryResponse uuidForIdentity:]
+ -[ATXAppDisplayIdentifiersDenyList .cxx_destruct]
+ -[ATXAppDisplayIdentifiersDenyList bundleIdentifiersNotAllowed]
+ -[ATXAppDisplayIdentifiersDenyList bundleIdentifiersNotAllowed].cold.1
+ -[ATXAppDisplayIdentifiersDenyList bundleIdentifiersNotAllowed].cold.2
+ -[ATXAppDisplayIdentifiersDenyList bundleIdentifiersNotAllowed].cold.3
+ -[ATXAppDisplayIdentifiersDenyList bundleIdentifiersNotAllowed].cold.4
+ -[ATXAppDisplayIdentifiersDenyList bundleIdentifiersNotAllowed].cold.5
+ -[ATXAppDisplayIdentifiersDenyList init]
+ -[ATXAppIdentity .cxx_destruct]
+ -[ATXAppIdentity _initWithBundleIdentifier:bundleURL:appType:]
+ -[ATXAppIdentity appType]
+ -[ATXAppIdentity bundleIDWithRelevantPrefix]
+ -[ATXAppIdentity bundleIdentifier]
+ -[ATXAppIdentity bundleURL]
+ -[ATXAppIdentity copyWithZone:]
+ -[ATXAppIdentity description]
+ -[ATXAppIdentity encodeWithCoder:]
+ -[ATXAppIdentity hash]
+ -[ATXAppIdentity initWithBundleIdentifier:]
+ -[ATXAppIdentity initWithBundleIdentifier:appType:]
+ -[ATXAppIdentity initWithBundleURL:]
+ -[ATXAppIdentity initWithBundleURL:appType:]
+ -[ATXAppIdentity initWithCoder:]
+ -[ATXAppIdentity isEqual:]
+ -[ATXAppIdentity isEqualToATXAppIdentity:]
+ -[ATXAppLaunchCarPlayContext .cxx_destruct]
+ -[ATXAppLaunchCarPlayContext appLaunchCountAndDistinctDaysLaunchedWhileConnectedToCarPlayForNumberOfDays:]
+ -[ATXAppLaunchCarPlayContext initWithAppInFocusStream:carPlayStream:]
+ -[ATXAppLaunchCarPlayContext init]
+ -[ATXAppProtectionInfo _effectiveBundleIdentifierForBundleIdentifier:]
+ -[ATXBackgroundSystemTask .cxx_destruct]
+ -[ATXBackgroundSystemTask bgSystemTask]
+ -[ATXBackgroundSystemTask currentProgressUnits]
+ -[ATXBackgroundSystemTask didDefer]
+ -[ATXBackgroundSystemTask didDefer].cold.1
+ -[ATXBackgroundSystemTask handle]
+ -[ATXBackgroundSystemTask initWithBackgroundSystemTask:]
+ -[ATXBackgroundSystemTask initWithBackgroundSystemTask:logHandle:]
+ -[ATXBackgroundSystemTask init]
+ -[ATXBackgroundSystemTask setBgSystemTask:]
+ -[ATXBackgroundSystemTask setCurrentProgressUnits:]
+ -[ATXBackgroundSystemTask setDone]
+ -[ATXBackgroundSystemTask setHandle:]
+ -[ATXBackgroundSystemTask setProgressUnits:]
+ -[ATXBackgroundSystemTask setProgressUnits:].cold.1
+ -[ATXBackgroundSystemTask setTaskDeferred:]
+ -[ATXBackgroundSystemTask setTaskExpiryCalled:]
+ -[ATXBackgroundSystemTask shouldDefer]
+ -[ATXBackgroundSystemTask shouldDefer].cold.1
+ -[ATXBackgroundSystemTask taskDeferred]
+ -[ATXBackgroundSystemTask taskExpiryCalled]
+ -[ATXClient fetchMenuItemsForCurrentAppInFocus:]
+ -[ATXClient fetchPreWarmedContextualActionSuggestionsWithError:]
+ -[ATXClient fetchToolKitBasedFallbackActionIds:]
+ -[ATXClient notifySpotlightInvoked:]
+ -[ATXClient recentURLsWithLimit:typeIdentifiersForScope:withCompletion:]
+ -[ATXClient semanticallySimilarDocumentsFromOnScreenAppEntities]
+ -[ATXCombinedIntentStream getCombinedIntentEventsBetweenStartDate:endDate:ascending:]
+ -[ATXCombinedIntentStream getCombinedIntentEventsFromLastMonth]
+ -[ATXCombinedIntentStream getIntentEventForSourceItemID:forSource:]
+ -[ATXCombinedIntentStream getSortedCombinedIntentEventsBetweenStartDate:endDate:bundleIdFilter:comparator:]
+ -[ATXCombinedIntentStream initWithIntentStream:activityStream:menuItemStream:toolKitActionStream:]
+ -[ATXDefaultHomeScreenItemManager _generateSmartStackForCarPlayWithDescriptorCacheFromRequest:error:]
+ -[ATXDefaultHomeScreenItemManager _generateSmartStackForCarPlayWithDescriptorCacheFromRequest:error:].cold.1
+ -[ATXDefaultHomeScreenItemManager _generateSmartStacksForCarPlayWithRequest:error:]
+ -[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:personaIdentifier:completionHandler:]
+ -[ATXDefaultHomeScreenItemManager fetchWidgetGalleryItemsWithRequest:completionHandler:]
+ -[ATXDefaultHomeScreenItemManager fetchWidgetSmartStackWithRequest:completionHandler:]
+ -[ATXDefaultHomeScreenItemManager galleryItemsForCarPlayWithRequest:error:]
+ -[ATXDefaultHomeScreenItemManager galleryItemsForCarPlayWithRequest:error:].cold.1
+ -[ATXDefaultHomeScreenItemManager galleryItemsForCarPlayWithRequest:error:].cold.2
+ -[ATXDefaultHomeScreenItemOnboardingStacks initWithOnboardingStacks:sortedThirdPartyWidgets:]
+ -[ATXDefaultHomeScreenItemOnboardingStacks onboardingStacks]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedCarPlayOnboardingStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer setSmartStackRequest:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer smartStackRequest]
+ -[ATXDefaultHomeScreenItemProducer galleryRequest]
+ -[ATXDefaultHomeScreenItemProducer setGalleryRequest:]
+ -[ATXDefaultHomeScreenItemProducer setSmartStackRequest:]
+ -[ATXDefaultHomeScreenItemProducer smartStackRequest]
+ -[ATXDefaultHomeScreenItemRanker widgetsBySortingAndFilteringWidgetsUsingPersonalizedGalleryAlgorithm:rankerPlistType:regularlyUsedThreshold:limit:]
+ -[ATXDocumentCategory .cxx_destruct]
+ -[ATXDocumentCategory categoryID]
+ -[ATXDocumentCategory description]
+ -[ATXDocumentCategory documentURLs]
+ -[ATXDocumentCategory initWithCategoryID:documentURLs:]
+ -[ATXDocumentInteraction .cxx_destruct]
+ -[ATXDocumentInteraction appIdentity]
+ -[ATXDocumentInteraction contentTypeIdentifier]
+ -[ATXDocumentInteraction copyWithZone:]
+ -[ATXDocumentInteraction encodeWithCoder:]
+ -[ATXDocumentInteraction fileIdentity]
+ -[ATXDocumentInteraction hash]
+ -[ATXDocumentInteraction initWithCoder:]
+ -[ATXDocumentInteraction initWithType:fileIdentity:contentTypeIdentifier:appIdentity:]
+ -[ATXDocumentInteraction initWithType:fileIdentity:contentTypeIdentifier:appIdentity:].cold.1
+ -[ATXDocumentInteraction initWithType:fileIdentity:contentTypeIdentifier:appIdentity:].cold.2
+ -[ATXDocumentInteraction init]
+ -[ATXDocumentInteraction isEqual:]
+ -[ATXDocumentInteraction isEqualToATXDocumentInteraction:]
+ -[ATXDocumentInteraction type]
+ -[ATXDocumentInteractionDonationClient donateDocumentInteraction:completion:]
+ -[ATXDocumentInteractionDonationClient donateDocumentInteraction:completion:].cold.1
+ -[ATXDocumentInteractionDonationClient donateDocumentInteractionForType:fileURL:contentTypeIdentifier:completion:]
+ -[ATXDocumentPredictionClient zkwPredictionsForRequest:error:]
+ -[ATXDocumentPredictionClient zkwPredictionsForRequest:usingPredictionManager:]
+ -[ATXDocumentPredictionRequest .cxx_destruct]
+ -[ATXDocumentPredictionRequest categoryWithLimit]
+ -[ATXDocumentPredictionRequest initWithLimit:documentScope:]
+ -[ATXDocumentPredictionRequest setCategoryWithLimit:]
+ -[ATXDocumentPredictionRequest setLimit:forCategory:]
+ -[ATXDocumentPredictionResponse .cxx_destruct]
+ -[ATXDocumentPredictionResponse initWithDocuments:]
+ -[ATXDocumentPredictionResponse predictedDocumentIdentities]
+ -[ATXDocumentPredictionResponse urls]
+ -[ATXDocumentRegexFilter init]
+ -[ATXDocumentRegexFilter shouldFilterOutBundleId:andURL:]
+ -[ATXDocumentRegexFilter shouldFilterOutURL:]
+ -[ATXDocumentScope .cxx_destruct]
+ -[ATXDocumentScope description]
+ -[ATXDocumentScope hash]
+ -[ATXDocumentScope initWithUTTypes:error:]
+ -[ATXDocumentScope isEqual:]
+ -[ATXDocumentScope isEqualToATXDocumentScope:]
+ -[ATXDocumentScope type]
+ -[ATXDocumentScope types]
+ -[ATXDonationManager .cxx_destruct]
+ -[ATXDonationManager _cleanUpConnection]
+ -[ATXDonationManager _cleanUpConnection].cold.1
+ -[ATXDonationManager _connection]
+ -[ATXDonationManager _connection].cold.1
+ -[ATXDonationManager _donateDocumentInteraction:completion:]
+ -[ATXDonationManager _donateMenuItem:completion:]
+ -[ATXDonationManager _init]
+ -[ATXDonationManager dealloc]
+ -[ATXDonationManager donateDocumentInteraction:completion:]
+ -[ATXDonationManager donateMenuItem:completion:]
+ -[ATXDonationManager queue]
+ -[ATXDonationManager xpcConnection]
+ -[ATXFaceSuggestionClient fetchFaceGalleryConfigurationForSemanticType:completion:]
+ -[ATXFileIdentity .cxx_destruct]
+ -[ATXFileIdentity bookmarkData]
+ -[ATXFileIdentity copyWithZone:]
+ -[ATXFileIdentity encodeWithCoder:]
+ -[ATXFileIdentity hash]
+ -[ATXFileIdentity initWithCoder:]
+ -[ATXFileIdentity initWithItemURL:]
+ -[ATXFileIdentity initWithItemURL:].cold.1
+ -[ATXFileIdentity initWithItemURL:bookmarkData:]
+ -[ATXFileIdentity init]
+ -[ATXFileIdentity isEqual:]
+ -[ATXFileIdentity isEqualToATXFileIdentity:]
+ -[ATXFileIdentity itemURL]
+ -[ATXFileIdentity resolveItemURLWithError:]
+ -[ATXIntentStream _getIntentEventFromLinkActionRecord:source:bundleIdFilter:allowMissingTitles:].cold.10
+ -[ATXMenuItemDonationClient donateMenuItem:completion:]
+ -[ATXMenuItemDonationClient donateMenuItemInvocation:completion:]
+ -[ATXMenuItemDonationClient donateMenuItemInvocation:completion:].cold.1
+ -[ATXMenuItemIdentity .cxx_destruct]
+ -[ATXMenuItemIdentity appIdentity]
+ -[ATXMenuItemIdentity copyWithZone:]
+ -[ATXMenuItemIdentity description]
+ -[ATXMenuItemIdentity encodeWithCoder:]
+ -[ATXMenuItemIdentity hash]
+ -[ATXMenuItemIdentity initWithAppIdentity:menuItemsPath:]
+ -[ATXMenuItemIdentity initWithCoder:]
+ -[ATXMenuItemIdentity init]
+ -[ATXMenuItemIdentity isEqual:]
+ -[ATXMenuItemIdentity isEqualToATXMenuItemIdentity:]
+ -[ATXMenuItemIdentity menuItemsPath]
+ -[ATXMenuItemInvocation .cxx_destruct]
+ -[ATXMenuItemInvocation copyWithZone:]
+ -[ATXMenuItemInvocation description]
+ -[ATXMenuItemInvocation encodeWithCoder:]
+ -[ATXMenuItemInvocation hash]
+ -[ATXMenuItemInvocation identity]
+ -[ATXMenuItemInvocation initWithCoder:]
+ -[ATXMenuItemInvocation initWithIdentity:invocationType:sourceType:localizedKeyboardShorctcutDisplayName:]
+ -[ATXMenuItemInvocation invocationType]
+ -[ATXMenuItemInvocation isEqual:]
+ -[ATXMenuItemInvocation isEqualToATXMenuItemInvocation:]
+ -[ATXMenuItemInvocation localizedKeyboardShorctcutDisplayName]
+ -[ATXMenuItemInvocation sourceType]
+ -[ATXMenuItemRegexFilter init]
+ -[ATXMenuItemRegexFilter shouldFilterOutAction:]
+ -[ATXMenuItemStream _enumerateMenuItemEventsBetweenStartDate:endDate:bundleIdFilter:reversed:block:]
+ -[ATXMenuItemStream _getIntentEventFromBMAppMenuItem:bundleIdFilter:]
+ -[ATXMenuItemStream _getIntentEventFromBMAppMenuItem:bundleIdFilter:].cold.1
+ -[ATXMenuItemStream _getIntentEventFromBMAppMenuItem:bundleIdFilter:].cold.2
+ -[ATXMenuItemStream _getIntentEventFromBMAppMenuItem:bundleIdFilter:].cold.3
+ -[ATXMenuItemStream getMenuItemEventsBetweenStartDate:endDate:]
+ -[ATXMenuItemStream getMenuItemEventsBetweenStartDate:endDate:bundleIdFilter:]
+ -[ATXMenuItemStream getMenuItemEventsBetweenStartDate:endDate:bundleIdFilter:limit:]
+ -[ATXMenuItemStream numberOfMenuItemEventsBetweenStartDate:endDate:]
+ -[ATXPBAction addMenuItemPathComponent:]
+ -[ATXPBAction addParameterKeysForToolInvocation:]
+ -[ATXPBAction clearMenuItemPathComponents]
+ -[ATXPBAction clearParameterKeysForToolInvocations]
+ -[ATXPBAction encodedToolInvocation]
+ -[ATXPBAction hasEncodedToolInvocation]
+ -[ATXPBAction hasToolInvocationID]
+ -[ATXPBAction menuItemPathComponentAtIndex:]
+ -[ATXPBAction menuItemPathComponentsCount]
+ -[ATXPBAction menuItemPathComponents]
+ -[ATXPBAction parameterKeysForToolInvocationAtIndex:]
+ -[ATXPBAction parameterKeysForToolInvocationsCount]
+ -[ATXPBAction parameterKeysForToolInvocations]
+ -[ATXPBAction setEncodedToolInvocation:]
+ -[ATXPBAction setMenuItemPathComponents:]
+ -[ATXPBAction setParameterKeysForToolInvocations:]
+ -[ATXPBAction setToolInvocationID:]
+ -[ATXPBAction toolInvocationID]
+ -[ATXPBSpotlightEvent addDocumentSuggestionIds:]
+ -[ATXPBSpotlightEvent clearDocumentSuggestionIds]
+ -[ATXPBSpotlightEvent documentSuggestionIdsAtIndex:]
+ -[ATXPBSpotlightEvent documentSuggestionIdsCount]
+ -[ATXPBSpotlightEvent documentSuggestionIds]
+ -[ATXPBSpotlightEvent setDocumentSuggestionIds:]
+ -[ATXPredictedDocumentCacheItem .cxx_destruct]
+ -[ATXPredictedDocumentCacheItem associatedAppBundleID]
+ -[ATXPredictedDocumentCacheItem copyWithZone:]
+ -[ATXPredictedDocumentCacheItem encodeWithCoder:]
+ -[ATXPredictedDocumentCacheItem initWithCoder:]
+ -[ATXPredictedDocumentCacheItem initWithPredictedDocuments:associatedAppBundleID:]
+ -[ATXPredictedDocumentCacheItem init]
+ -[ATXPredictedDocumentCacheItem predictedDocuments]
+ -[ATXPredictedDocumentIdentity .cxx_destruct]
+ -[ATXPredictedDocumentIdentity bookmarkData]
+ -[ATXPredictedDocumentIdentity copyWithZone:]
+ -[ATXPredictedDocumentIdentity documentURL]
+ -[ATXPredictedDocumentIdentity encodeWithCoder:]
+ -[ATXPredictedDocumentIdentity initWithCoder:]
+ -[ATXPredictedDocumentIdentity initWithDocumentURL:predictionScore:]
+ -[ATXPredictedDocumentIdentity initWithDocumentURL:predictionScore:bookmarkData:type:]
+ -[ATXPredictedDocumentIdentity initWithDocumentURL:predictionScore:type:]
+ -[ATXPredictedDocumentIdentity init]
+ -[ATXPredictedDocumentIdentity predictionScore]
+ -[ATXPredictedDocumentIdentity resolvedURL]
+ -[ATXPredictedDocumentIdentity resolvedURL].cold.1
+ -[ATXPredictedDocumentIdentity setBookmarkData:]
+ -[ATXPredictedDocumentIdentity type]
+ -[ATXPredictionRequest .cxx_destruct]
+ -[ATXPredictionRequest initWithLimit:scope:]
+ -[ATXPredictionRequest limit]
+ -[ATXPredictionRequest scope]
+ -[ATXPredictionResponse .cxx_destruct]
+ -[ATXPredictionResponse initWithUUID:]
+ -[ATXPredictionResponse uuid]
+ -[ATXRegexFilter .cxx_destruct]
+ -[ATXRegexFilter _checkString:againstRegexesArray:]
+ -[ATXRegexFilter _checkString:againstRegexesArray:].cold.1
+ -[ATXRegexFilter _checkString:againstRegexesArrayDictionary:]
+ -[ATXRegexFilter _checkString:againstRegexesArrayDictionary:].cold.1
+ -[ATXRegexFilter _initWithAssetName:asset:]
+ -[ATXRegexFilter _initWithAssetName:asset:].cold.1
+ -[ATXRegexFilter description]
+ -[ATXRegexFilter initWithAssetName:]
+ -[ATXRegexFilter shouldFilterOutAction:]
+ -[ATXRegexFilter shouldFilterOutAction:].cold.1
+ -[ATXRegexFilter shouldFilterOutBundleId:andAttribute:]
+ -[ATXRegexFilter shouldFilterOutOnlyBasedOnAttribute:]
+ -[ATXRegexFilter shouldFilterOutOnlyBasedOnBundleId:]
+ -[ATXResponse predictedAppIdentities]
+ -[ATXSettingsAction associatedBundleId]
+ -[ATXSettingsAction associatedBundleId].cold.1
+ -[ATXSettingsAction associatedBundleId].cold.2
+ -[ATXSettingsAction associatedBundleId].cold.3
+ -[ATXSettingsAction associatedBundleId].cold.4
+ -[ATXSettingsAction bundleIdentifierIsHiddenForSettingsAction]
+ -[ATXSettingsActionsClientRequest clientBundleID]
+ -[ATXSettingsActionsClientRequest setClientBundleID:]
+ -[ATXSpotlightEvent documentSuggestionIds]
+ -[ATXSpotlightEvent initWithAbsoluteDate:eventType:appConsumerSubType:actionConsumerSubType:appBlendingCacheId:actionBlendingCacheId:appSuggestionIds:actionSuggestionIds:documentSuggestionIds:metadata:]
+ -[ATXSpotlightEvent initWithDate:eventType:appConsumerSubType:actionConsumerSubType:appBlendingCacheId:actionBlendingCacheId:appSuggestionIds:actionSuggestionIds:documentSuggestionIds:metadata:]
+ -[ATXSpotlightEvent setDocumentSuggestionIds:]
+ -[ATXSuggestionSearchResult score]
+ -[ATXSuggestionSearchResult setScore:]
+ -[ATXToolKitActionStream getToolKitActionEventsBetweenStartDate:endDate:]
+ -[ATXToolKitActionStream getToolKitActionEventsBetweenStartDate:endDate:bundleIdFilter:]
+ -[ATXToolKitActionStream getToolKitActionEventsBetweenStartDate:endDate:bundleIdFilter:limit:]
+ -[ATXToolKitActionStream lastDateOfToolKitAction]
+ -[ATXToolKitActionStream numberOfToolKitActionEventsBetweenStartDate:endDate:]
+ -[ATXUserEducationSuggestion initWithUUID_ATXUserEducationSuggestion:]
+ -[ATXUserEducationSuggestionPosterSetup .cxx_destruct]
+ -[ATXUserEducationSuggestionPosterSetup description]
+ -[ATXUserEducationSuggestionPosterSetup encodeWithCoder:]
+ -[ATXUserEducationSuggestionPosterSetup initWithCoder:]
+ -[ATXUserEducationSuggestionPosterSetup initWithCoder:].cold.1
+ -[ATXUserEducationSuggestionPosterSetup initWithPosterId:]
+ -[ATXUserEducationSuggestionPosterSetup posterId]
+ -[ATXWidgetClientIdentity .cxx_destruct]
+ -[ATXWidgetClientIdentity clientSessionIdentifier]
+ -[ATXWidgetClientIdentity encodeWithCoder:]
+ -[ATXWidgetClientIdentity initWithClientSessionIdentifier:widgetClient:]
+ -[ATXWidgetClientIdentity initWithCoder:]
+ -[ATXWidgetClientIdentity setClientSessionIdentifier:]
+ -[ATXWidgetClientIdentity setWidgetClient:]
+ -[ATXWidgetClientIdentity widgetClient]
+ -[ATXWidgetGalleryRequest .cxx_destruct]
+ -[ATXWidgetGalleryRequest clientIdentity]
+ -[ATXWidgetGalleryRequest denyListOfExtensions]
+ -[ATXWidgetGalleryRequest encodeWithCoder:]
+ -[ATXWidgetGalleryRequest galleryVariant]
+ -[ATXWidgetGalleryRequest initWithClientIdentity:]
+ -[ATXWidgetGalleryRequest initWithCoder:]
+ -[ATXWidgetGalleryRequest limit]
+ -[ATXWidgetGalleryRequest setDenyListOfExtensions:]
+ -[ATXWidgetGalleryRequest setGalleryVariant:]
+ -[ATXWidgetGalleryRequest setLimit:]
+ -[ATXWidgetGalleryRequest setWidgetFamilyMask:]
+ -[ATXWidgetGalleryRequest setWidgetGridSize:]
+ -[ATXWidgetGalleryRequest widgetFamilyMask]
+ -[ATXWidgetGalleryRequest widgetGridSize]
+ -[ATXWidgetGalleryResponse .cxx_destruct]
+ -[ATXWidgetGalleryResponse encodeWithCoder:]
+ -[ATXWidgetGalleryResponse initWithCoder:]
+ -[ATXWidgetGalleryResponse initWithItems:]
+ -[ATXWidgetGalleryResponse items]
+ -[ATXWidgetSmartStackRequest .cxx_destruct]
+ -[ATXWidgetSmartStackRequest clientIdentity]
+ -[ATXWidgetSmartStackRequest denyListOfExtensions]
+ -[ATXWidgetSmartStackRequest encodeWithCoder:]
+ -[ATXWidgetSmartStackRequest initWithClientIdentity:]
+ -[ATXWidgetSmartStackRequest initWithCoder:]
+ -[ATXWidgetSmartStackRequest maximumWidgetsPerStack]
+ -[ATXWidgetSmartStackRequest numberOfStacks]
+ -[ATXWidgetSmartStackRequest setDenyListOfExtensions:]
+ -[ATXWidgetSmartStackRequest setMaximumWidgetsPerStack:]
+ -[ATXWidgetSmartStackRequest setNumberOfStacks:]
+ -[ATXWidgetSmartStackRequest setSmartStackVariant:]
+ -[ATXWidgetSmartStackRequest smartStackVariant]
+ -[ATXWidgetSmartStackResponse .cxx_destruct]
+ -[ATXWidgetSmartStackResponse encodeWithCoder:]
+ -[ATXWidgetSmartStackResponse initWithCoder:]
+ -[ATXWidgetSmartStackResponse initWithStacks:]
+ -[ATXWidgetSmartStackResponse stacks]
+ -[NSArray(ATXAppIdentity) bundleIDsFromIdentities]
+ -[NSArray(ATXAppIdentity_NSString) appIdentitiesFromBundleIDs]
+ GCC_except_table54
+ GCC_except_table57
+ GCC_except_table60
+ GCC_except_table63
+ GCC_except_table68
+ OBJC_IVAR_$_ATXPBAction._encodedToolInvocation
+ OBJC_IVAR_$_ATXPBAction._menuItemPathComponents
+ OBJC_IVAR_$_ATXPBAction._parameterKeysForToolInvocations
+ OBJC_IVAR_$_ATXPBAction._toolInvocationID
+ OBJC_IVAR_$_ATXPBSpotlightEvent._documentSuggestionIds
+ _ATXBundleIdForRemoteBundleId
+ _ATXClientDonationsInterface
+ _ATXDocumentInteractionTypeGetName
+ _ATXDocumentInteractionTypeIsValid
+ _ATXIsRemoteAppBundleId
+ _ATXMenuItemIntentType
+ _ATXMenuItemPathSeparatorForTitle
+ _ATXPredictionErrorDomain
+ _ATXRemoteAppSuggestionsEnabled
+ _ATXRemoteBundleIdForBundleId
+ _OBJC_CLASS_$_ATXActionScope
+ _OBJC_CLASS_$_ATXActionSuggestionRequest
+ _OBJC_CLASS_$_ATXAppDisplayIdentifiersDenyList
+ _OBJC_CLASS_$_ATXAppIdentity
+ _OBJC_CLASS_$_ATXAppInFocusStream
+ _OBJC_CLASS_$_ATXAppLaunchCarPlayContext
+ _OBJC_CLASS_$_ATXBackgroundSystemTask
+ _OBJC_CLASS_$_ATXCarPlayConnectedStream
+ _OBJC_CLASS_$_ATXDocumentCategory
+ _OBJC_CLASS_$_ATXDocumentInteraction
+ _OBJC_CLASS_$_ATXDocumentInteractionDonationClient
+ _OBJC_CLASS_$_ATXDocumentPredictionClient
+ _OBJC_CLASS_$_ATXDocumentPredictionRequest
+ _OBJC_CLASS_$_ATXDocumentPredictionResponse
+ _OBJC_CLASS_$_ATXDocumentRegexFilter
+ _OBJC_CLASS_$_ATXDocumentScope
+ _OBJC_CLASS_$_ATXDonationManager
+ _OBJC_CLASS_$_ATXFileIdentity
+ _OBJC_CLASS_$_ATXMenuItemDonationClient
+ _OBJC_CLASS_$_ATXMenuItemIdentity
+ _OBJC_CLASS_$_ATXMenuItemInvocation
+ _OBJC_CLASS_$_ATXMenuItemRegexFilter
+ _OBJC_CLASS_$_ATXMenuItemStream
+ _OBJC_CLASS_$_ATXPredictedDocumentCacheItem
+ _OBJC_CLASS_$_ATXPredictedDocumentIdentity
+ _OBJC_CLASS_$_ATXPredictionRequest
+ _OBJC_CLASS_$_ATXPredictionResponse
+ _OBJC_CLASS_$_ATXRegexFilter
+ _OBJC_CLASS_$_ATXSpotlightClientEncodedToolAction
+ _OBJC_CLASS_$_ATXToolKitActionStream
+ _OBJC_CLASS_$_ATXToolKitActionStreamWrapper
+ _OBJC_CLASS_$_ATXUserEducationSuggestionPosterSetup
+ _OBJC_CLASS_$_ATXWidgetClientIdentity
+ _OBJC_CLASS_$_ATXWidgetGalleryRequest
+ _OBJC_CLASS_$_ATXWidgetGalleryResponse
+ _OBJC_CLASS_$_ATXWidgetSmartStackRequest
+ _OBJC_CLASS_$_ATXWidgetSmartStackResponse
+ _OBJC_CLASS_$_BGSystemTaskProgressMetrics
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_CLASS_$_SFExecuteMenuItemCommand
+ _OBJC_CLASS_$_SFExecuteToolCommand
+ _OBJC_IVAR_$_ATXAction._encodedToolInvocation
+ _OBJC_IVAR_$_ATXAction._menuItemPath
+ _OBJC_IVAR_$_ATXAction._parameterKeysForToolInvocation
+ _OBJC_IVAR_$_ATXAction._toolInvocationID
+ _OBJC_IVAR_$_ATXActionScope._actionType
+ _OBJC_IVAR_$_ATXActionScope._appEntityKeyValueMapping
+ _OBJC_IVAR_$_ATXActionScope._appIdentifier
+ _OBJC_IVAR_$_ATXActionScope._intentClassName
+ _OBJC_IVAR_$_ATXActionSuggestionRequest._spotlightRecentTopics
+ _OBJC_IVAR_$_ATXAppDirectoryCategory._appIdentities
+ _OBJC_IVAR_$_ATXAppDirectoryResponse._predictedAppIdentities
+ _OBJC_IVAR_$_ATXAppDirectoryResponse._recentAppIdentities
+ _OBJC_IVAR_$_ATXAppDisplayIdentifiersDenyList._path
+ _OBJC_IVAR_$_ATXAppIdentity._appType
+ _OBJC_IVAR_$_ATXAppIdentity._bundleIdentifier
+ _OBJC_IVAR_$_ATXAppIdentity._bundleURL
+ _OBJC_IVAR_$_ATXAppLaunchCarPlayContext._appInFocusStream
+ _OBJC_IVAR_$_ATXAppLaunchCarPlayContext._carPlayConnectedStream
+ _OBJC_IVAR_$_ATXBackgroundSystemTask._bgSystemTask
+ _OBJC_IVAR_$_ATXBackgroundSystemTask._currentProgressUnits
+ _OBJC_IVAR_$_ATXBackgroundSystemTask._handle
+ _OBJC_IVAR_$_ATXBackgroundSystemTask._taskDeferred
+ _OBJC_IVAR_$_ATXBackgroundSystemTask._taskExpiryCalled
+ _OBJC_IVAR_$_ATXCombinedIntentStream._menuItemStream
+ _OBJC_IVAR_$_ATXCombinedIntentStream._toolKitActionStream
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemOnboardingStacks._onboardingStacks
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemOnboardingStacksProducer._smartStackRequest
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemProducer._galleryRequest
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemProducer._smartStackRequest
+ _OBJC_IVAR_$_ATXDocumentCategory._categoryID
+ _OBJC_IVAR_$_ATXDocumentCategory._documentURLs
+ _OBJC_IVAR_$_ATXDocumentInteraction._appIdentity
+ _OBJC_IVAR_$_ATXDocumentInteraction._contentTypeIdentifier
+ _OBJC_IVAR_$_ATXDocumentInteraction._fileIdentity
+ _OBJC_IVAR_$_ATXDocumentInteraction._type
+ _OBJC_IVAR_$_ATXDocumentPredictionRequest._categoryWithLimit
+ _OBJC_IVAR_$_ATXDocumentPredictionResponse._predictedDocumentIdentities
+ _OBJC_IVAR_$_ATXDocumentScope._types
+ _OBJC_IVAR_$_ATXDonationManager._queue
+ _OBJC_IVAR_$_ATXDonationManager._xpcConnection
+ _OBJC_IVAR_$_ATXFileIdentity._bookmarkData
+ _OBJC_IVAR_$_ATXFileIdentity._itemURL
+ _OBJC_IVAR_$_ATXMenuItemIdentity._appIdentity
+ _OBJC_IVAR_$_ATXMenuItemIdentity._menuItemsPath
+ _OBJC_IVAR_$_ATXMenuItemInvocation._identity
+ _OBJC_IVAR_$_ATXMenuItemInvocation._invocationType
+ _OBJC_IVAR_$_ATXMenuItemInvocation._localizedKeyboardShorctcutDisplayName
+ _OBJC_IVAR_$_ATXMenuItemInvocation._sourceType
+ _OBJC_IVAR_$_ATXPredictedDocumentCacheItem._associatedAppBundleID
+ _OBJC_IVAR_$_ATXPredictedDocumentCacheItem._predictedDocuments
+ _OBJC_IVAR_$_ATXPredictedDocumentIdentity._bookmarkData
+ _OBJC_IVAR_$_ATXPredictedDocumentIdentity._documentURL
+ _OBJC_IVAR_$_ATXPredictedDocumentIdentity._predictionScore
+ _OBJC_IVAR_$_ATXPredictedDocumentIdentity._type
+ _OBJC_IVAR_$_ATXPredictionRequest._limit
+ _OBJC_IVAR_$_ATXPredictionRequest._scope
+ _OBJC_IVAR_$_ATXPredictionResponse._uuid
+ _OBJC_IVAR_$_ATXRegexFilter._assetName
+ _OBJC_IVAR_$_ATXRegexFilter._attributesFilters
+ _OBJC_IVAR_$_ATXRegexFilter._bundleIdsFilters
+ _OBJC_IVAR_$_ATXRegexFilter._combinedFilters
+ _OBJC_IVAR_$_ATXSettingsActionsClientRequest._clientBundleID
+ _OBJC_IVAR_$_ATXSpotlightEvent._documentSuggestionIds
+ _OBJC_IVAR_$_ATXSuggestionSearchResult._score
+ _OBJC_IVAR_$_ATXUserEducationSuggestionPosterSetup._posterId
+ _OBJC_IVAR_$_ATXWidgetClientIdentity._clientSessionIdentifier
+ _OBJC_IVAR_$_ATXWidgetClientIdentity._widgetClient
+ _OBJC_IVAR_$_ATXWidgetGalleryRequest._clientIdentity
+ _OBJC_IVAR_$_ATXWidgetGalleryRequest._denyListOfExtensions
+ _OBJC_IVAR_$_ATXWidgetGalleryRequest._galleryVariant
+ _OBJC_IVAR_$_ATXWidgetGalleryRequest._limit
+ _OBJC_IVAR_$_ATXWidgetGalleryRequest._widgetFamilyMask
+ _OBJC_IVAR_$_ATXWidgetGalleryRequest._widgetGridSize
+ _OBJC_IVAR_$_ATXWidgetGalleryResponse._items
+ _OBJC_IVAR_$_ATXWidgetSmartStackRequest._clientIdentity
+ _OBJC_IVAR_$_ATXWidgetSmartStackRequest._denyListOfExtensions
+ _OBJC_IVAR_$_ATXWidgetSmartStackRequest._maximumWidgetsPerStack
+ _OBJC_IVAR_$_ATXWidgetSmartStackRequest._numberOfStacks
+ _OBJC_IVAR_$_ATXWidgetSmartStackRequest._smartStackVariant
+ _OBJC_IVAR_$_ATXWidgetSmartStackResponse._stacks
+ _OBJC_METACLASS_$_ATXActionScope
+ _OBJC_METACLASS_$_ATXActionSuggestionRequest
+ _OBJC_METACLASS_$_ATXAppDisplayIdentifiersDenyList
+ _OBJC_METACLASS_$_ATXAppIdentity
+ _OBJC_METACLASS_$_ATXAppLaunchCarPlayContext
+ _OBJC_METACLASS_$_ATXBackgroundSystemTask
+ _OBJC_METACLASS_$_ATXDocumentCategory
+ _OBJC_METACLASS_$_ATXDocumentInteraction
+ _OBJC_METACLASS_$_ATXDocumentInteractionDonationClient
+ _OBJC_METACLASS_$_ATXDocumentPredictionClient
+ _OBJC_METACLASS_$_ATXDocumentPredictionRequest
+ _OBJC_METACLASS_$_ATXDocumentPredictionResponse
+ _OBJC_METACLASS_$_ATXDocumentRegexFilter
+ _OBJC_METACLASS_$_ATXDocumentScope
+ _OBJC_METACLASS_$_ATXDonationManager
+ _OBJC_METACLASS_$_ATXFileIdentity
+ _OBJC_METACLASS_$_ATXMenuItemDonationClient
+ _OBJC_METACLASS_$_ATXMenuItemIdentity
+ _OBJC_METACLASS_$_ATXMenuItemInvocation
+ _OBJC_METACLASS_$_ATXMenuItemRegexFilter
+ _OBJC_METACLASS_$_ATXMenuItemStream
+ _OBJC_METACLASS_$_ATXPredictedDocumentCacheItem
+ _OBJC_METACLASS_$_ATXPredictedDocumentIdentity
+ _OBJC_METACLASS_$_ATXPredictionRequest
+ _OBJC_METACLASS_$_ATXPredictionResponse
+ _OBJC_METACLASS_$_ATXRegexFilter
+ _OBJC_METACLASS_$_ATXToolKitActionStream
+ _OBJC_METACLASS_$_ATXUserEducationSuggestionPosterSetup
+ _OBJC_METACLASS_$_ATXWidgetClientIdentity
+ _OBJC_METACLASS_$_ATXWidgetGalleryRequest
+ _OBJC_METACLASS_$_ATXWidgetGalleryResponse
+ _OBJC_METACLASS_$_ATXWidgetSmartStackRequest
+ _OBJC_METACLASS_$_ATXWidgetSmartStackResponse
+ __OBJC_$_CATEGORY_NSArray_$_ATXAppIdentity
+ __OBJC_$_CLASS_METHODS_ATXAppIdentity
+ __OBJC_$_CLASS_METHODS_ATXDocumentCategory
+ __OBJC_$_CLASS_METHODS_ATXDocumentInteraction
+ __OBJC_$_CLASS_METHODS_ATXDocumentInteractionDonationClient
+ __OBJC_$_CLASS_METHODS_ATXDocumentPredictionClient(Demo)
+ __OBJC_$_CLASS_METHODS_ATXDocumentRegexFilter
+ __OBJC_$_CLASS_METHODS_ATXDonationManager
+ __OBJC_$_CLASS_METHODS_ATXFileIdentity
+ __OBJC_$_CLASS_METHODS_ATXMenuItemDonationClient
+ __OBJC_$_CLASS_METHODS_ATXMenuItemIdentity
+ __OBJC_$_CLASS_METHODS_ATXMenuItemInvocation
+ __OBJC_$_CLASS_METHODS_ATXMenuItemRegexFilter
+ __OBJC_$_CLASS_METHODS_ATXPredictedDocumentCacheItem
+ __OBJC_$_CLASS_METHODS_ATXPredictedDocumentIdentity
+ __OBJC_$_CLASS_METHODS_ATXRegexFilter
+ __OBJC_$_CLASS_METHODS_ATXToolKitActionStream
+ __OBJC_$_CLASS_METHODS_ATXUserEducationSuggestionPosterSetup
+ __OBJC_$_CLASS_METHODS_ATXWidgetClientIdentity
+ __OBJC_$_CLASS_METHODS_ATXWidgetGalleryRequest
+ __OBJC_$_CLASS_METHODS_ATXWidgetGalleryResponse
+ __OBJC_$_CLASS_METHODS_ATXWidgetSmartStackRequest
+ __OBJC_$_CLASS_METHODS_ATXWidgetSmartStackResponse
+ __OBJC_$_CLASS_PROP_LIST_ATXAppIdentity
+ __OBJC_$_CLASS_PROP_LIST_ATXDocumentInteraction
+ __OBJC_$_CLASS_PROP_LIST_ATXFileIdentity
+ __OBJC_$_CLASS_PROP_LIST_ATXMenuItemIdentity
+ __OBJC_$_CLASS_PROP_LIST_ATXMenuItemInvocation
+ __OBJC_$_CLASS_PROP_LIST_ATXPredictedDocumentCacheItem
+ __OBJC_$_CLASS_PROP_LIST_ATXPredictedDocumentIdentity
+ __OBJC_$_CLASS_PROP_LIST_ATXWidgetClientIdentity
+ __OBJC_$_CLASS_PROP_LIST_ATXWidgetGalleryRequest
+ __OBJC_$_CLASS_PROP_LIST_ATXWidgetGalleryResponse
+ __OBJC_$_CLASS_PROP_LIST_ATXWidgetSmartStackRequest
+ __OBJC_$_CLASS_PROP_LIST_ATXWidgetSmartStackResponse
+ __OBJC_$_INSTANCE_METHODS_ATXActionScope
+ __OBJC_$_INSTANCE_METHODS_ATXActionSuggestionRequest
+ __OBJC_$_INSTANCE_METHODS_ATXAppDisplayIdentifiersDenyList
+ __OBJC_$_INSTANCE_METHODS_ATXAppIdentity
+ __OBJC_$_INSTANCE_METHODS_ATXAppLaunchCarPlayContext
+ __OBJC_$_INSTANCE_METHODS_ATXBackgroundSystemTask
+ __OBJC_$_INSTANCE_METHODS_ATXDocumentCategory
+ __OBJC_$_INSTANCE_METHODS_ATXDocumentInteraction
+ __OBJC_$_INSTANCE_METHODS_ATXDocumentInteractionDonationClient
+ __OBJC_$_INSTANCE_METHODS_ATXDocumentPredictionClient
+ __OBJC_$_INSTANCE_METHODS_ATXDocumentPredictionRequest
+ __OBJC_$_INSTANCE_METHODS_ATXDocumentPredictionResponse
+ __OBJC_$_INSTANCE_METHODS_ATXDocumentRegexFilter
+ __OBJC_$_INSTANCE_METHODS_ATXDocumentScope
+ __OBJC_$_INSTANCE_METHODS_ATXDonationManager
+ __OBJC_$_INSTANCE_METHODS_ATXFileIdentity
+ __OBJC_$_INSTANCE_METHODS_ATXMenuItemDonationClient
+ __OBJC_$_INSTANCE_METHODS_ATXMenuItemIdentity
+ __OBJC_$_INSTANCE_METHODS_ATXMenuItemInvocation
+ __OBJC_$_INSTANCE_METHODS_ATXMenuItemRegexFilter
+ __OBJC_$_INSTANCE_METHODS_ATXMenuItemStream
+ __OBJC_$_INSTANCE_METHODS_ATXPredictedDocumentCacheItem
+ __OBJC_$_INSTANCE_METHODS_ATXPredictedDocumentIdentity
+ __OBJC_$_INSTANCE_METHODS_ATXPredictionRequest
+ __OBJC_$_INSTANCE_METHODS_ATXPredictionResponse
+ __OBJC_$_INSTANCE_METHODS_ATXRegexFilter
+ __OBJC_$_INSTANCE_METHODS_ATXToolKitActionStream
+ __OBJC_$_INSTANCE_METHODS_ATXUserEducationSuggestionPosterSetup
+ __OBJC_$_INSTANCE_METHODS_ATXWidgetClientIdentity
+ __OBJC_$_INSTANCE_METHODS_ATXWidgetGalleryRequest
+ __OBJC_$_INSTANCE_METHODS_ATXWidgetGalleryResponse
+ __OBJC_$_INSTANCE_METHODS_ATXWidgetSmartStackRequest
+ __OBJC_$_INSTANCE_METHODS_ATXWidgetSmartStackResponse
+ __OBJC_$_INSTANCE_METHODS_NSArray(ATXAppIdentity|ATXAppIdentity_NSString)
+ __OBJC_$_INSTANCE_VARIABLES_ATXActionScope
+ __OBJC_$_INSTANCE_VARIABLES_ATXActionSuggestionRequest
+ __OBJC_$_INSTANCE_VARIABLES_ATXAppDisplayIdentifiersDenyList
+ __OBJC_$_INSTANCE_VARIABLES_ATXAppIdentity
+ __OBJC_$_INSTANCE_VARIABLES_ATXAppLaunchCarPlayContext
+ __OBJC_$_INSTANCE_VARIABLES_ATXBackgroundSystemTask
+ __OBJC_$_INSTANCE_VARIABLES_ATXDocumentCategory
+ __OBJC_$_INSTANCE_VARIABLES_ATXDocumentInteraction
+ __OBJC_$_INSTANCE_VARIABLES_ATXDocumentPredictionRequest
+ __OBJC_$_INSTANCE_VARIABLES_ATXDocumentPredictionResponse
+ __OBJC_$_INSTANCE_VARIABLES_ATXDocumentScope
+ __OBJC_$_INSTANCE_VARIABLES_ATXDonationManager
+ __OBJC_$_INSTANCE_VARIABLES_ATXFileIdentity
+ __OBJC_$_INSTANCE_VARIABLES_ATXMenuItemIdentity
+ __OBJC_$_INSTANCE_VARIABLES_ATXMenuItemInvocation
+ __OBJC_$_INSTANCE_VARIABLES_ATXPredictedDocumentCacheItem
+ __OBJC_$_INSTANCE_VARIABLES_ATXPredictedDocumentIdentity
+ __OBJC_$_INSTANCE_VARIABLES_ATXPredictionRequest
+ __OBJC_$_INSTANCE_VARIABLES_ATXPredictionResponse
+ __OBJC_$_INSTANCE_VARIABLES_ATXRegexFilter
+ __OBJC_$_INSTANCE_VARIABLES_ATXUserEducationSuggestionPosterSetup
+ __OBJC_$_INSTANCE_VARIABLES_ATXWidgetClientIdentity
+ __OBJC_$_INSTANCE_VARIABLES_ATXWidgetGalleryRequest
+ __OBJC_$_INSTANCE_VARIABLES_ATXWidgetGalleryResponse
+ __OBJC_$_INSTANCE_VARIABLES_ATXWidgetSmartStackRequest
+ __OBJC_$_INSTANCE_VARIABLES_ATXWidgetSmartStackResponse
+ __OBJC_$_PROP_LIST_ATXActionScope
+ __OBJC_$_PROP_LIST_ATXActionSuggestionRequest
+ __OBJC_$_PROP_LIST_ATXAppIdentity
+ __OBJC_$_PROP_LIST_ATXBackgroundSystemTask
+ __OBJC_$_PROP_LIST_ATXDocumentCategory
+ __OBJC_$_PROP_LIST_ATXDocumentInteraction
+ __OBJC_$_PROP_LIST_ATXDocumentPredictionRequest
+ __OBJC_$_PROP_LIST_ATXDocumentPredictionResponse
+ __OBJC_$_PROP_LIST_ATXDocumentScope
+ __OBJC_$_PROP_LIST_ATXDonationManager
+ __OBJC_$_PROP_LIST_ATXFileIdentity
+ __OBJC_$_PROP_LIST_ATXMenuItemIdentity
+ __OBJC_$_PROP_LIST_ATXMenuItemInvocation
+ __OBJC_$_PROP_LIST_ATXPredictedDocumentCacheItem
+ __OBJC_$_PROP_LIST_ATXPredictedDocumentIdentity
+ __OBJC_$_PROP_LIST_ATXPredictionRequest
+ __OBJC_$_PROP_LIST_ATXPredictionResponse
+ __OBJC_$_PROP_LIST_ATXPredictionScope
+ __OBJC_$_PROP_LIST_ATXUserEducationSuggestion.76
+ __OBJC_$_PROP_LIST_ATXUserEducationSuggestionPosterSetup
+ __OBJC_$_PROP_LIST_ATXWidgetClientIdentity
+ __OBJC_$_PROP_LIST_ATXWidgetGalleryRequest
+ __OBJC_$_PROP_LIST_ATXWidgetGalleryResponse
+ __OBJC_$_PROP_LIST_ATXWidgetSmartStackRequest
+ __OBJC_$_PROP_LIST_ATXWidgetSmartStackResponse
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ATXActivityProgressProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ATXClientDonationsXPCInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ATXPredictionScope
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ATXActivityProgressProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ATXClientDonationsXPCInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ATXPredictionScope
+ __OBJC_$_PROTOCOL_REFS_ATXActivityProgressProtocol
+ __OBJC_$_PROTOCOL_REFS_ATXBackgroundActivityProtocol
+ __OBJC_$_PROTOCOL_REFS_ATXPredictionScope
+ __OBJC_CLASS_PROTOCOLS_$_ATXActionScope
+ __OBJC_CLASS_PROTOCOLS_$_ATXAppIdentity
+ __OBJC_CLASS_PROTOCOLS_$_ATXBackgroundSystemTask
+ __OBJC_CLASS_PROTOCOLS_$_ATXDocumentInteraction
+ __OBJC_CLASS_PROTOCOLS_$_ATXDocumentScope
+ __OBJC_CLASS_PROTOCOLS_$_ATXDonationManager
+ __OBJC_CLASS_PROTOCOLS_$_ATXFileIdentity
+ __OBJC_CLASS_PROTOCOLS_$_ATXMenuItemIdentity
+ __OBJC_CLASS_PROTOCOLS_$_ATXMenuItemInvocation
+ __OBJC_CLASS_PROTOCOLS_$_ATXPredictedDocumentCacheItem
+ __OBJC_CLASS_PROTOCOLS_$_ATXPredictedDocumentIdentity
+ __OBJC_CLASS_PROTOCOLS_$_ATXWidgetClientIdentity
+ __OBJC_CLASS_PROTOCOLS_$_ATXWidgetGalleryRequest
+ __OBJC_CLASS_PROTOCOLS_$_ATXWidgetGalleryResponse
+ __OBJC_CLASS_PROTOCOLS_$_ATXWidgetSmartStackRequest
+ __OBJC_CLASS_PROTOCOLS_$_ATXWidgetSmartStackResponse
+ __OBJC_CLASS_RO_$_ATXActionScope
+ __OBJC_CLASS_RO_$_ATXActionSuggestionRequest
+ __OBJC_CLASS_RO_$_ATXAppDisplayIdentifiersDenyList
+ __OBJC_CLASS_RO_$_ATXAppIdentity
+ __OBJC_CLASS_RO_$_ATXAppLaunchCarPlayContext
+ __OBJC_CLASS_RO_$_ATXBackgroundSystemTask
+ __OBJC_CLASS_RO_$_ATXDocumentCategory
+ __OBJC_CLASS_RO_$_ATXDocumentInteraction
+ __OBJC_CLASS_RO_$_ATXDocumentInteractionDonationClient
+ __OBJC_CLASS_RO_$_ATXDocumentPredictionClient
+ __OBJC_CLASS_RO_$_ATXDocumentPredictionRequest
+ __OBJC_CLASS_RO_$_ATXDocumentPredictionResponse
+ __OBJC_CLASS_RO_$_ATXDocumentRegexFilter
+ __OBJC_CLASS_RO_$_ATXDocumentScope
+ __OBJC_CLASS_RO_$_ATXDonationManager
+ __OBJC_CLASS_RO_$_ATXFileIdentity
+ __OBJC_CLASS_RO_$_ATXMenuItemDonationClient
+ __OBJC_CLASS_RO_$_ATXMenuItemIdentity
+ __OBJC_CLASS_RO_$_ATXMenuItemInvocation
+ __OBJC_CLASS_RO_$_ATXMenuItemRegexFilter
+ __OBJC_CLASS_RO_$_ATXMenuItemStream
+ __OBJC_CLASS_RO_$_ATXPredictedDocumentCacheItem
+ __OBJC_CLASS_RO_$_ATXPredictedDocumentIdentity
+ __OBJC_CLASS_RO_$_ATXPredictionRequest
+ __OBJC_CLASS_RO_$_ATXPredictionResponse
+ __OBJC_CLASS_RO_$_ATXRegexFilter
+ __OBJC_CLASS_RO_$_ATXToolKitActionStream
+ __OBJC_CLASS_RO_$_ATXUserEducationSuggestionPosterSetup
+ __OBJC_CLASS_RO_$_ATXWidgetClientIdentity
+ __OBJC_CLASS_RO_$_ATXWidgetGalleryRequest
+ __OBJC_CLASS_RO_$_ATXWidgetGalleryResponse
+ __OBJC_CLASS_RO_$_ATXWidgetSmartStackRequest
+ __OBJC_CLASS_RO_$_ATXWidgetSmartStackResponse
+ __OBJC_LABEL_PROTOCOL_$_ATXActivityProgressProtocol
+ __OBJC_LABEL_PROTOCOL_$_ATXBackgroundActivityProtocol
+ __OBJC_LABEL_PROTOCOL_$_ATXClientDonationsXPCInterface
+ __OBJC_LABEL_PROTOCOL_$_ATXPredictionScope
+ __OBJC_METACLASS_RO_$_ATXActionScope
+ __OBJC_METACLASS_RO_$_ATXActionSuggestionRequest
+ __OBJC_METACLASS_RO_$_ATXAppDisplayIdentifiersDenyList
+ __OBJC_METACLASS_RO_$_ATXAppIdentity
+ __OBJC_METACLASS_RO_$_ATXAppLaunchCarPlayContext
+ __OBJC_METACLASS_RO_$_ATXBackgroundSystemTask
+ __OBJC_METACLASS_RO_$_ATXDocumentCategory
+ __OBJC_METACLASS_RO_$_ATXDocumentInteraction
+ __OBJC_METACLASS_RO_$_ATXDocumentInteractionDonationClient
+ __OBJC_METACLASS_RO_$_ATXDocumentPredictionClient
+ __OBJC_METACLASS_RO_$_ATXDocumentPredictionRequest
+ __OBJC_METACLASS_RO_$_ATXDocumentPredictionResponse
+ __OBJC_METACLASS_RO_$_ATXDocumentRegexFilter
+ __OBJC_METACLASS_RO_$_ATXDocumentScope
+ __OBJC_METACLASS_RO_$_ATXDonationManager
+ __OBJC_METACLASS_RO_$_ATXFileIdentity
+ __OBJC_METACLASS_RO_$_ATXMenuItemDonationClient
+ __OBJC_METACLASS_RO_$_ATXMenuItemIdentity
+ __OBJC_METACLASS_RO_$_ATXMenuItemInvocation
+ __OBJC_METACLASS_RO_$_ATXMenuItemRegexFilter
+ __OBJC_METACLASS_RO_$_ATXMenuItemStream
+ __OBJC_METACLASS_RO_$_ATXPredictedDocumentCacheItem
+ __OBJC_METACLASS_RO_$_ATXPredictedDocumentIdentity
+ __OBJC_METACLASS_RO_$_ATXPredictionRequest
+ __OBJC_METACLASS_RO_$_ATXPredictionResponse
+ __OBJC_METACLASS_RO_$_ATXRegexFilter
+ __OBJC_METACLASS_RO_$_ATXToolKitActionStream
+ __OBJC_METACLASS_RO_$_ATXUserEducationSuggestionPosterSetup
+ __OBJC_METACLASS_RO_$_ATXWidgetClientIdentity
+ __OBJC_METACLASS_RO_$_ATXWidgetGalleryRequest
+ __OBJC_METACLASS_RO_$_ATXWidgetGalleryResponse
+ __OBJC_METACLASS_RO_$_ATXWidgetSmartStackRequest
+ __OBJC_METACLASS_RO_$_ATXWidgetSmartStackResponse
+ __OBJC_PROTOCOL_$_ATXActivityProgressProtocol
+ __OBJC_PROTOCOL_$_ATXBackgroundActivityProtocol
+ __OBJC_PROTOCOL_$_ATXClientDonationsXPCInterface
+ __OBJC_PROTOCOL_$_ATXPredictionScope
+ __OBJC_PROTOCOL_REFERENCE_$_ATXClientDonationsXPCInterface
+ ___100-[ATXMenuItemStream _enumerateMenuItemEventsBetweenStartDate:endDate:bundleIdFilter:reversed:block:]_block_invoke
+ ___100-[ATXMenuItemStream _enumerateMenuItemEventsBetweenStartDate:endDate:bundleIdFilter:reversed:block:]_block_invoke.12
+ ___100-[ATXMenuItemStream _enumerateMenuItemEventsBetweenStartDate:endDate:bundleIdFilter:reversed:block:]_block_invoke.cold.1
+ ___101-[ATXDefaultHomeScreenItemManager _generateSmartStackForCarPlayWithDescriptorCacheFromRequest:error:]_block_invoke
+ ___106-[ATXAppLaunchCarPlayContext appLaunchCountAndDistinctDaysLaunchedWhileConnectedToCarPlayForNumberOfDays:]_block_invoke
+ ___106-[ATXAppLaunchCarPlayContext appLaunchCountAndDistinctDaysLaunchedWhileConnectedToCarPlayForNumberOfDays:]_block_invoke.25
+ ___106-[ATXAppLaunchCarPlayContext appLaunchCountAndDistinctDaysLaunchedWhileConnectedToCarPlayForNumberOfDays:]_block_invoke_2
+ ___106-[ATXAppLaunchCarPlayContext appLaunchCountAndDistinctDaysLaunchedWhileConnectedToCarPlayForNumberOfDays:]_block_invoke_3
+ ___106-[ATXAppLaunchCarPlayContext appLaunchCountAndDistinctDaysLaunchedWhileConnectedToCarPlayForNumberOfDays:]_block_invoke_4
+ ___106-[ATXAppLaunchCarPlayContext appLaunchCountAndDistinctDaysLaunchedWhileConnectedToCarPlayForNumberOfDays:]_block_invoke_5
+ ___113-[ATXAppDirectoryClient predictedAppsAndRecentAppsWithMaxNumberOfPredictedApps:shouldUseDefaultCategories:reply:]_block_invoke.29
+ ___113-[ATXAppDirectoryClient predictedAppsAndRecentAppsWithMaxNumberOfPredictedApps:shouldUseDefaultCategories:reply:]_block_invoke.30
+ ___126-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:personaIdentifier:completionHandler:]_block_invoke
+ ___126-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:personaIdentifier:completionHandler:]_block_invoke.51
+ ___126-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:personaIdentifier:completionHandler:]_block_invoke.58
+ ___126-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:personaIdentifier:completionHandler:]_block_invoke.cold.1
+ ___126-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:personaIdentifier:completionHandler:]_block_invoke.cold.2
+ ___126-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:personaIdentifier:completionHandler:]_block_invoke_2
+ ___126-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:personaIdentifier:completionHandler:]_block_invoke_3
+ ___126-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:personaIdentifier:completionHandler:]_block_invoke_4
+ ___160+[ATXDefaultHomeScreenItemManager _descriptorsByFilteringDescriptors:variant:fromAppsDisabledOnHomeScreen:fromExcludedWidgetsWithIdentifiers:personaIdentifier:]_block_invoke
+ ___160+[ATXDefaultHomeScreenItemManager _descriptorsByFilteringDescriptors:variant:fromAppsDisabledOnHomeScreen:fromExcludedWidgetsWithIdentifiers:personaIdentifier:]_block_invoke.cold.1
+ ___160+[ATXDefaultHomeScreenItemManager _descriptorsByFilteringDescriptors:variant:fromAppsDisabledOnHomeScreen:fromExcludedWidgetsWithIdentifiers:personaIdentifier:]_block_invoke.cold.2
+ ___18-[ATXAction proto]_block_invoke.117
+ ___202-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedAmbientOnboardingStacksForSize:stack1RequiredWidgetPersonalities:stack2RequiredWidgetPersonalities:rankedWidgets:usedWidgetPersonalities:]_block_invoke.99
+ ___218-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedCarPlayOnboardingStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:]_block_invoke
+ ___248-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedOnboardingStackForSize:requiredWidgetPersonalities:conditionalWidgetPersonalities:fallbackWidgetPersonalities:rankedThirdPartyWidgets:usedWidgetPersonalities:shouldAdd3PWidgetToStack:]_block_invoke.111
+ ___28-[ATXResponse predictedApps]_block_invoke
+ ___32-[ATXClient _minuteZeroResponse]_block_invoke_2
+ ___33-[ATXDonationManager _connection]_block_invoke
+ ___33-[ATXDonationManager _connection]_block_invoke.13
+ ___33-[ATXDonationManager _connection]_block_invoke.13.cold.1
+ ___33-[ATXDonationManager _connection]_block_invoke.14
+ ___33-[ATXDonationManager _connection]_block_invoke.cold.1
+ ___35+[ATXDonationManager sharedManager]_block_invoke
+ ___35+[ATXMenuItemDonationClient shared]_block_invoke
+ ___36-[ATXClient notifySpotlightInvoked:]_block_invoke
+ ___36-[ATXClient notifySpotlightInvoked:]_block_invoke_2
+ ___36-[ATXClient notifySpotlightInvoked:]_block_invoke_2.cold.1
+ ___37-[ATXDocumentPredictionResponse urls]_block_invoke
+ ___37-[ATXResponse predictedAppIdentities]_block_invoke
+ ___39-[ATXSettingsAction associatedBundleId]_block_invoke
+ ___39-[ATXSettingsAction associatedBundleId]_block_invoke.82
+ ___40+[ATXDocumentRegexFilter sharedInstance]_block_invoke
+ ___40+[ATXMenuItemRegexFilter sharedInstance]_block_invoke
+ ___43-[ATXRegexFilter _initWithAssetName:asset:]_block_invoke
+ ___43-[ATXRegexFilter _initWithAssetName:asset:]_block_invoke.cold.1
+ ___45-[ATXAppDirectoryResponse uuidForIdentities:]_block_invoke
+ ___46+[ATXDocumentInteractionDonationClient shared]_block_invoke
+ ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.374
+ ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.374.cold.1
+ ___48-[ATXClient fetchMenuItemsForCurrentAppInFocus:]_block_invoke
+ ___48-[ATXClient fetchMenuItemsForCurrentAppInFocus:]_block_invoke_2
+ ___48-[ATXClient fetchToolKitBasedFallbackActionIds:]_block_invoke
+ ___48-[ATXClient fetchToolKitBasedFallbackActionIds:]_block_invoke_2
+ ___48-[ATXDonationManager donateMenuItem:completion:]_block_invoke
+ ___49+[ATXSpotlightClient isValidSuggestion:forScope:]_block_invoke
+ ___50-[NSArray(ATXAppIdentity) bundleIDsFromIdentities]_block_invoke
+ ___50-[NSArray(ATXAppIdentity) bundleIDsFromIdentities]_block_invoke.cold.1
+ ___54+[ATXRegexFilter _compilePatterns:assetName:ruleName:]_block_invoke
+ ___55-[ATXRegexFilter shouldFilterOutBundleId:andAttribute:]_block_invoke
+ ___59+[ATXSpotlightClient predictionsForRequest:withCompletion:]_block_invoke
+ ___59-[ATXDonationManager donateDocumentInteraction:completion:]_block_invoke
+ ___61+[ATXDocumentPredictionClient(Demo) _getDocumentsForDemoMode]_block_invoke
+ ___61+[ATXDocumentPredictionClient(Demo) _getDocumentsForDemoMode]_block_invoke_2
+ ___61-[ATXRegexFilter _checkString:againstRegexesArrayDictionary:]_block_invoke
+ ___62-[NSArray(ATXAppIdentity_NSString) appIdentitiesFromBundleIDs]_block_invoke
+ ___64-[ATXClient fetchPreWarmedContextualActionSuggestionsWithError:]_block_invoke
+ ___64-[ATXClient fetchPreWarmedContextualActionSuggestionsWithError:]_block_invoke_2
+ ___64-[ATXClient semanticallySimilarDocumentsFromOnScreenAppEntities]_block_invoke
+ ___64-[ATXClient semanticallySimilarDocumentsFromOnScreenAppEntities]_block_invoke.121
+ ___64-[ATXClient semanticallySimilarDocumentsFromOnScreenAppEntities]_block_invoke_2
+ ___64-[ATXClient semanticallySimilarDocumentsFromOnScreenAppEntities]_block_invoke_2.cold.1
+ ___65-[ATXMenuItemDonationClient donateMenuItemInvocation:completion:]_block_invoke
+ ___66-[ATXBackgroundSystemTask initWithBackgroundSystemTask:logHandle:]_block_invoke
+ ___68-[ATXMenuItemStream numberOfMenuItemEventsBetweenStartDate:endDate:]_block_invoke
+ ___71-[ATXFaceSuggestionClient fetchFaceSuggestionsForFocusMode:completion:]_block_invoke.44
+ ___71-[ATXFaceSuggestionClient fetchFaceSuggestionsForFocusMode:completion:]_block_invoke.45
+ ___72+[ATXToolKitActionStream sanitizeTitleForToolKitIntents:withCompletion:]_block_invoke
+ ___72+[ATXToolKitActionStream sanitizeTitleForToolKitIntents:withCompletion:]_block_invoke.11
+ ___72+[ATXToolKitActionStream sanitizeTitleForToolKitIntents:withCompletion:]_block_invoke.11.cold.1
+ ___72-[ATXClient recentURLsWithLimit:typeIdentifiersForScope:withCompletion:]_block_invoke
+ ___72-[ATXClient recentURLsWithLimit:typeIdentifiersForScope:withCompletion:]_block_invoke.cold.1
+ ___72-[ATXClient recentURLsWithLimit:typeIdentifiersForScope:withCompletion:]_block_invoke.cold.2
+ ___73+[ATXSpotlightClient rerankRecents_LimitCount:oneCountDays:twoCountDays:]_block_invoke.339
+ ___73+[ATXSpotlightClient rerankRecents_LimitCount:oneCountDays:twoCountDays:]_block_invoke.339.cold.1
+ ___73+[ATXSpotlightClient rerankRecents_LimitCount:oneCountDays:twoCountDays:]_block_invoke.339.cold.2
+ ___77-[ATXDocumentInteractionDonationClient donateDocumentInteraction:completion:]_block_invoke
+ ___78+[ATXDefaultHomeScreenItemUpdater atxHomeScreenStackConfigFromATXWidgetStack:]_block_invoke
+ ___83-[ATXFaceSuggestionClient fetchFaceGalleryConfigurationForSemanticType:completion:]_block_invoke
+ ___83-[ATXFaceSuggestionClient fetchFaceGalleryConfigurationForSemanticType:completion:]_block_invoke.40
+ ___83-[ATXFaceSuggestionClient fetchFaceGalleryConfigurationForSemanticType:completion:]_block_invoke.41
+ ___84-[ATXMenuItemStream getMenuItemEventsBetweenStartDate:endDate:bundleIdFilter:limit:]_block_invoke
+ ___85-[ATXCombinedIntentStream getCombinedIntentEventsBetweenStartDate:endDate:ascending:]_block_invoke
+ ___86-[ATXDefaultHomeScreenItemManager fetchWidgetSmartStackWithRequest:completionHandler:]_block_invoke
+ ___86-[ATXDefaultHomeScreenItemManager fetchWidgetSmartStackWithRequest:completionHandler:]_block_invoke_2
+ ___86-[ATXDefaultHomeScreenItemManager fetchWidgetSmartStackWithRequest:completionHandler:]_block_invoke_3
+ ___88-[ATXDefaultHomeScreenItemManager fetchWidgetGalleryItemsWithRequest:completionHandler:]_block_invoke
+ ___88-[ATXDefaultHomeScreenItemManager fetchWidgetGalleryItemsWithRequest:completionHandler:]_block_invoke_2
+ ___88-[ATXDefaultHomeScreenItemManager fetchWidgetGalleryItemsWithRequest:completionHandler:]_block_invoke_3
+ ___91-[ATXDefaultHomeScreenItemUpdater _updateAmbientDefaultsOnQueueWithReason:appLaunchCounts:]_block_invoke.52
+ ___91-[ATXDefaultHomeScreenItemUpdater _updateAmbientDefaultsOnQueueWithReason:appLaunchCounts:]_block_invoke_2.57
+ ___91-[ATXDefaultHomeScreenItemUpdater _updateAmbientDefaultsOnQueueWithReason:appLaunchCounts:]_block_invoke_2.57.cold.1
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.72
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.72.cold.1
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.72.cold.2
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.72.cold.3
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.72.cold.4
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.73
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.77
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.78
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.82
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.83
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.86
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke_2.84
+ _____atxlog_handle_client_donations_block_invoke
+ _____atxlog_handle_document_predictor_block_invoke
+ _____atxlog_handle_menu_items_block_invoke
+ _____atxlog_handle_ml_inference_block_invoke
+ _____atxlog_handle_screen_entities_block_invoke
+ ___atxlog_handle_client_donations
+ ___atxlog_handle_client_donations.cold.1
+ ___atxlog_handle_client_donations.log
+ ___atxlog_handle_client_donations.onceToken
+ ___atxlog_handle_document_predictor
+ ___atxlog_handle_document_predictor.cold.1
+ ___atxlog_handle_document_predictor.log
+ ___atxlog_handle_document_predictor.onceToken
+ ___atxlog_handle_menu_items
+ ___atxlog_handle_menu_items.cold.1
+ ___atxlog_handle_menu_items.log
+ ___atxlog_handle_menu_items.onceToken
+ ___atxlog_handle_ml_inference
+ ___atxlog_handle_ml_inference.cold.1
+ ___atxlog_handle_ml_inference.log
+ ___atxlog_handle_ml_inference.onceToken
+ ___atxlog_handle_screen_entities
+ ___atxlog_handle_screen_entities.cold.1
+ ___atxlog_handle_screen_entities.log
+ ___atxlog_handle_screen_entities.onceToken
+ ___block_descriptor_32_e32_"NSData"16?0"ATXIntentEvent"8l
+ ___block_descriptor_32_e34_"ATXAppIdentity"16?0"NSString"8l
+ ___block_descriptor_32_e34_B16?0"ATXCarPlayConnectedEvent"8l
+ ___block_descriptor_32_e38_16?0"ATXPredictedDocumentIdentity"8l
+ ___block_descriptor_32_e63_q24?0"ATXCarPlayConnectedEvent"8"ATXCarPlayConnectedEvent"16l
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
+ ___block_descriptor_40_e8_32s_e24_16?0"ATXAppIdentity"8ls32l8
+ ___block_descriptor_40_e8_32s_e27_B24?0"NSDate"8"NSDate"16ls32l8
+ ___block_descriptor_40_e8_32s_e34_v16?0"ATXCarPlayConnectedEvent"8ls32l8
+ ___block_descriptor_40_e8_32w_e8_v16?0Q8lw32l8
+ ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32r40r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e25_v32?0"NSString"816^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e39_"NSRegularExpression"16?0"NSString"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_48_e8_32s_e30_"ATXAppDirectoryResponse"8?0ls32l8
+ ___block_descriptor_48_e8_32s_e31_v32?0"ATXAppIdentity"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32s_e34_"NSString"16?0"ATXAppIdentity"8ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e22_B16?0"BMStoreEvent"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48r_e34_v32?0"NSString"8"NSArray"16^B24ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e35_B16?0"ATXAppInFocusEventSession"8ls56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e37_v32?0"NSString"8"_PASTuple2"16^B24ls32l8s40l8s48l8r56l8
+ ___block_descriptor_72_e8_32s40bs_e52_v24?0"ATXDefaultHomeScreenItemUpdate"8"NSError"16ls40l8s32l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s_e39_B16?0"ATXHomeScreenWidgetDescriptor"8ls32l8s40l8s48l8
+ ___block_literal_global.108
+ ___block_literal_global.118
+ ___block_literal_global.12
+ ___block_literal_global.120
+ ___block_literal_global.124
+ ___block_literal_global.128
+ ___block_literal_global.131
+ ___block_literal_global.134
+ ___block_literal_global.137
+ ___block_literal_global.48
+ ___block_literal_global.569
+ ___block_literal_global.63
+ ___block_literal_global.94
+ ___block_literal_global.99
+ __decodeArrayOrFail
+ __decodeTopLevelObjectOrFail
+ _objc_msgSend$URLByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:
+ _objc_msgSend$_allIdentifiersIncludingRemoteApps:includeInternalMacOSApps:
+ _objc_msgSend$_appIdentifiersIncludingRemoteApps:includeInternalMacOSApps:
+ _objc_msgSend$_checkString:againstRegexesArray:
+ _objc_msgSend$_checkString:againstRegexesArrayDictionary:
+ _objc_msgSend$_cleanUpConnection
+ _objc_msgSend$_compilePatterns:assetName:ruleName:
+ _objc_msgSend$_demoDocumentsPath
+ _objc_msgSend$_descriptorsByFilteringDescriptors:variant:fromAppsDisabledOnHomeScreen:fromExcludedWidgetsWithIdentifiers:personaIdentifier:
+ _objc_msgSend$_donateDocumentInteraction:completion:
+ _objc_msgSend$_donateMenuItem:completion:
+ _objc_msgSend$_effectiveBundleIdentifierForBundleIdentifier:
+ _objc_msgSend$_enumerateMenuItemEventsBetweenStartDate:endDate:bundleIdFilter:reversed:block:
+ _objc_msgSend$_generateSmartStackForCarPlayWithDescriptorCacheFromRequest:error:
+ _objc_msgSend$_generateSmartStacksForCarPlayWithRequest:error:
+ _objc_msgSend$_getIntentEventFromBMAppMenuItem:bundleIdFilter:
+ _objc_msgSend$_initWithAssetName:asset:
+ _objc_msgSend$_initWithBundleIdentifier:bundleURL:appType:
+ _objc_msgSend$_pas_componentsJoinedByString:
+ _objc_msgSend$_personalizedCarPlayOnboardingStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:
+ _objc_msgSend$_responseWithSpotlightLayout:andSpotlightRecentTopics:actionScope:limit:
+ _objc_msgSend$_setError
+ _objc_msgSend$_suggestedResultResponseWithLimit:andSpotlightRecentTopics:actionScope:
+ _objc_msgSend$addMenuItemPathComponent:
+ _objc_msgSend$addParameterKeysForToolInvocation:
+ _objc_msgSend$appEntityKeyValueMapping
+ _objc_msgSend$appIdentifier
+ _objc_msgSend$appIdentities
+ _objc_msgSend$appIdentitiesFromBundleIDs
+ _objc_msgSend$appIdentity
+ _objc_msgSend$appLaunchCountAndDistinctDaysLaunchedWhileConnectedToCarPlayForNumberOfDays:
+ _objc_msgSend$appSessionEndTime
+ _objc_msgSend$appSessionStartTime
+ _objc_msgSend$appType
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$associatedAppBundleID
+ _objc_msgSend$associatedBundleId
+ _objc_msgSend$atxHomeScreenStackConfigFromATXWidgetStack:
+ _objc_msgSend$atxHomeScreenWidgetIdentifierFromATXWidget:
+ _objc_msgSend$atx_errorWithCode:debugDescription:
+ _objc_msgSend$bgSystemTask
+ _objc_msgSend$bookmarkData
+ _objc_msgSend$bookmarkDataWithOptions:includingResourceValuesForKeys:relativeToURL:error:
+ _objc_msgSend$bundleIDWithRelevantPrefix
+ _objc_msgSend$bundleIDsFromIdentities
+ _objc_msgSend$bundleIdentifiersNotAllowed
+ _objc_msgSend$bundleURL
+ _objc_msgSend$bundleWithURL:
+ _objc_msgSend$categoryWithLimit
+ _objc_msgSend$clearMenuItemPathComponents
+ _objc_msgSend$clearParameterKeysForToolInvocations
+ _objc_msgSend$client
+ _objc_msgSend$clientIdentity
+ _objc_msgSend$clientSessionIdentifier
+ _objc_msgSend$conversationIdentifier
+ _objc_msgSend$currentAppIdentity
+ _objc_msgSend$currentProgressUnits
+ _objc_msgSend$denyListOfExtensions
+ _objc_msgSend$descriptionForAppType:
+ _objc_msgSend$descriptionForTopic:
+ _objc_msgSend$deviceIdentifier
+ _objc_msgSend$dictionaryWithValuesForKeys:
+ _objc_msgSend$documentURL
+ _objc_msgSend$documentURLs
+ _objc_msgSend$donateDocumentInteraction:completion:
+ _objc_msgSend$donateMenuItem:completion:
+ _objc_msgSend$donateMenuItemInvocation:completion:
+ _objc_msgSend$encodedToolInvocation
+ _objc_msgSend$enumerateAllAppLaunchSessionsFromStartDate:bundleIDFilter:block:
+ _objc_msgSend$enumerateConnectedEventsFromStartDate:endDate:filterBlock:limit:ascending:block:
+ _objc_msgSend$fetchFaceGalleryConfigurationForSemanticType:completion:
+ _objc_msgSend$fetchGalleryItemsForVariant:gridSize:supportedFamilies:personaIdentifier:completionHandler:
+ _objc_msgSend$fetchMenuItemsForCurrentAppInFocusWithCompletion:
+ _objc_msgSend$fetchPreWarmedContextualActionSuggestionsWithCompletion:
+ _objc_msgSend$fetchSemanticallySimilarDocumentsWithCompletion:
+ _objc_msgSend$fetchTitlesFromToolInvocations:completionHandler:
+ _objc_msgSend$fetchToolKitBasedFallbackActionIdsWithCompletion:
+ _objc_msgSend$galleryItemsForCarPlayWithRequest:error:
+ _objc_msgSend$galleryVariant
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$getCombinedIntentEventsBetweenStartDate:endDate:ascending:
+ _objc_msgSend$getDirectoryResponseFromCacheWithMaxNumberOfAppsToPredict:
+ _objc_msgSend$getIntentEventForSourceItemID:forSource:
+ _objc_msgSend$getMenuItemEventsBetweenStartDate:endDate:bundleIdFilter:
+ _objc_msgSend$getMenuItemEventsBetweenStartDate:endDate:bundleIdFilter:limit:
+ _objc_msgSend$getSortedCombinedIntentEventsBetweenStartDate:endDate:bundleIdFilter:comparator:
+ _objc_msgSend$getToolKitActionEventsBetweenStartDate:endDate:bundleIdFilter:
+ _objc_msgSend$getToolKitActionEventsBetweenStartDate:endDate:bundleIdFilter:limit:
+ _objc_msgSend$hasError
+ _objc_msgSend$identity
+ _objc_msgSend$initWithAbsoluteDate:eventType:appConsumerSubType:actionConsumerSubType:appBlendingCacheId:actionBlendingCacheId:appSuggestionIds:actionSuggestionIds:documentSuggestionIds:metadata:
+ _objc_msgSend$initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:menuItemPath:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:toolInvocationID:encodedToolInvocation:parameterKeysForToolInvocation:
+ _objc_msgSend$initWithAppIdentifier:appEntityKeyValueMapping:actionType:intentClassName:error:
+ _objc_msgSend$initWithAppIdentity:menuItemsPath:
+ _objc_msgSend$initWithAppInFocusStream:carPlayStream:
+ _objc_msgSend$initWithBackgroundSystemTask:logHandle:
+ _objc_msgSend$initWithBundleIdentifier:
+ _objc_msgSend$initWithBundleIdentifier:appType:
+ _objc_msgSend$initWithCategoryID:appIdentities:
+ _objc_msgSend$initWithCategoryID:appIdentitites:localizedName:
+ _objc_msgSend$initWithClientIdentity:
+ _objc_msgSend$initWithClientSessionIdentifier:widgetClient:
+ _objc_msgSend$initWithDate:eventType:appConsumerSubType:actionConsumerSubType:appBlendingCacheId:actionBlendingCacheId:appSuggestionIds:actionSuggestionIds:documentSuggestionIds:metadata:
+ _objc_msgSend$initWithDocumentURL:predictionScore:bookmarkData:type:
+ _objc_msgSend$initWithDocumentURL:predictionScore:type:
+ _objc_msgSend$initWithIdentifier:qos:workloadCategory:expectedMetricValue:itemsCompleted:totalItemCount:
+ _objc_msgSend$initWithIdentity:invocationType:sourceType:localizedKeyboardShorctcutDisplayName:
+ _objc_msgSend$initWithIntentStream:activityStream:menuItemStream:toolKitActionStream:
+ _objc_msgSend$initWithItemURL:
+ _objc_msgSend$initWithItemURL:bookmarkData:
+ _objc_msgSend$initWithItems:
+ _objc_msgSend$initWithMenuItemPath:actionUUID:bundleId:title:subtitle:
+ _objc_msgSend$initWithOnboardingStacks:sortedThirdPartyWidgets:
+ _objc_msgSend$initWithPattern:options:error:
+ _objc_msgSend$initWithPredictedDocuments:associatedAppBundleID:
+ _objc_msgSend$initWithQueryString:queryContext:
+ _objc_msgSend$initWithRemotePlaceholderBundleIdentifier:error:
+ _objc_msgSend$initWithStacks:
+ _objc_msgSend$initWithSuggestionLayout:includeRemoteApps:recentApps:hiddenApps:otherAppsOnScreen:numAppsToPredict:error:
+ _objc_msgSend$initWithType:fileIdentity:contentTypeIdentifier:appIdentity:
+ _objc_msgSend$initWithUUID_ATXUserEducationSuggestion:
+ _objc_msgSend$intentClassName
+ _objc_msgSend$invocationType
+ _objc_msgSend$isActionEligibleForAnySettingsSuggestions:
+ _objc_msgSend$isActionEligibleForAnySettingsSuggestionsWithBundleIdentifier:actionIdentifier:
+ _objc_msgSend$isAppleOwnedAppForBundleId:
+ _objc_msgSend$isEqualToATXActionScope:
+ _objc_msgSend$isEqualToATXAppIdentity:
+ _objc_msgSend$isEqualToATXDocumentInteraction:
+ _objc_msgSend$isEqualToATXDocumentScope:
+ _objc_msgSend$isEqualToATXFileIdentity:
+ _objc_msgSend$isEqualToATXMenuItemIdentity:
+ _objc_msgSend$isEqualToATXMenuItemInvocation:
+ _objc_msgSend$isRemote
+ _objc_msgSend$isValidSuggestion:forScope:
+ _objc_msgSend$joinComponentsOfMenuItemPath:
+ _objc_msgSend$lastDateForToolKitActionEvent
+ _objc_msgSend$limit
+ _objc_msgSend$localizedKeyboardShorctcutDisplayName
+ _objc_msgSend$mainBundle
+ _objc_msgSend$maximumWidgetsPerStack
+ _objc_msgSend$menuItemPath
+ _objc_msgSend$menuItemPathComponentAtIndex:
+ _objc_msgSend$menuItemPathComponents
+ _objc_msgSend$menuItemPathComponentsCount
+ _objc_msgSend$menuItemsPath
+ _objc_msgSend$notifySpotlightInvoked:
+ _objc_msgSend$numberOfStacks
+ _objc_msgSend$parameterKeysForToolInvocation
+ _objc_msgSend$parameterKeysForToolInvocationAtIndex:
+ _objc_msgSend$parameterKeysForToolInvocations
+ _objc_msgSend$parameterKeysForToolInvocationsCount
+ _objc_msgSend$position
+ _objc_msgSend$predictedAppIdentities
+ _objc_msgSend$predictedDocumentIdentities
+ _objc_msgSend$predictedDocuments
+ _objc_msgSend$predictionScore
+ _objc_msgSend$recentApps
+ _objc_msgSend$recentURLsWithLimit:typeIdentifiersForScope:withCompletion:
+ _objc_msgSend$reportProgressMetrics:error:
+ _objc_msgSend$resolveItemURLWithError:
+ _objc_msgSend$safeStringForConsumerSubtype:
+ _objc_msgSend$setBgSystemTask:
+ _objc_msgSend$setCategoryWithLimit:
+ _objc_msgSend$setCurrentProgressUnits:
+ _objc_msgSend$setEncodedToolInvocation:
+ _objc_msgSend$setExpirationHandlerWithReason:
+ _objc_msgSend$setGalleryRequest:
+ _objc_msgSend$setHandle:
+ _objc_msgSend$setMenuItemIdentifier:
+ _objc_msgSend$setParameterKeysForToolInvocations:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setProgressUnits:
+ _objc_msgSend$setSmartStackRequest:
+ _objc_msgSend$setSpotlightRecentTopics:
+ _objc_msgSend$setTaskCompleted
+ _objc_msgSend$setTaskDeferred:
+ _objc_msgSend$setTaskExpiredWithRetryAfter:error:
+ _objc_msgSend$setTaskExpiryCalled:
+ _objc_msgSend$setToolIdentifier:
+ _objc_msgSend$setToolInvocationData:
+ _objc_msgSend$setToolInvocationID:
+ _objc_msgSend$sharedManager
+ _objc_msgSend$sharedScheduler
+ _objc_msgSend$shouldFilterOutBundleId:andAttribute:
+ _objc_msgSend$shouldFilterOutOnlyBasedOnAttribute:
+ _objc_msgSend$shouldFilterOutOnlyBasedOnBundleId:
+ _objc_msgSend$shouldFilterOutWidgetDescriptorDueToDenyList:fromExcludedWidgetsWithIdentifiers:
+ _objc_msgSend$smartStackVariant
+ _objc_msgSend$sourceType
+ _objc_msgSend$spotlightRecentTopics
+ _objc_msgSend$stringArrayForKey:
+ _objc_msgSend$stringForMenuItemInvocationType:
+ _objc_msgSend$stringForMenuItemSourceType:
+ _objc_msgSend$taskDeferred
+ _objc_msgSend$taskExpiryCalled
+ _objc_msgSend$toolInvocationID
+ _objc_msgSend$types
+ _objc_msgSend$widgetClient
+ _objc_msgSend$widgetGridSize
+ _objc_msgSend$widgetSuggestionsEnabled
+ _objc_msgSend$widgetsBySortingAndFilteringWidgetsUsingPersonalizedGalleryAlgorithm:rankerPlistType:regularlyUsedThreshold:limit:
+ _objc_msgSend$zkwPredictionsForRequest:error:
+ _qos_class_self
+ _shared.onceToken
+ _shared.sharedInstance
+ _sharedInstance._pasOnceToken7
+ _sharedInstance._pasOnceToken9
+ _sharedInstanceWithMobileAssets._pasOnceToken12
+ _sharedManager.onceToken
+ _sharedManager.shared
- +[ATXClientDuetHelper sharedInstance]
- +[ATXClientDuetHelper sharedInstance].cold.1
- +[ATXDefaultHomeScreenItemManager _descriptorsByFilteringDescriptors:variant:fromAppsDisabledOnHomeScreen:]
- +[ATXSettingsAction isActionEligibleForSettingsSuggestionsWithBundleIdentifier:actionIdentifier:]
- +[ATXSpotlightClient _descriptionForTopic:]
- +[ATXSpotlightClient _responseWithSpotlightLayout:andSpotlightRecentTopics:]
- -[ATXAction initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:]
- -[ATXAction initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:].cold.1
- -[ATXAction initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:].cold.2
- -[ATXAction initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:].cold.3
- -[ATXAction initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:].cold.4
- -[ATXAction initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:].cold.5
- -[ATXAppDirectoryClient _logToDuet:metadata:]
- -[ATXAppDirectoryClient _logToDuet:metadata:].cold.1
- -[ATXAppDirectoryClient _logToDuet:metadata:].cold.2
- -[ATXAppDirectoryResponse initWithSuggestionLayout:recentApps:hiddenApps:otherAppsOnScreen:numAppsToPredict:error:]
- -[ATXAppDirectoryResponse initWithSuggestionLayout:recentApps:hiddenApps:otherAppsOnScreen:numAppsToPredict:error:].cold.1
- -[ATXClientDuetHelper _enumerateBatchesInDuetStream:startDate:endDate:otherPredicates:limit:block:]
- -[ATXClientDuetHelper _enumerateBatchesInDuetStream:startDate:endDate:otherPredicates:limit:block:].cold.1
- -[ATXClientDuetHelper _getIntentEventForSource:startDate:endDate:otherPredicates:bundleIdFilter:limit:]
- -[ATXClientDuetHelper _getIntentEventForSource:startDate:endDate:otherPredicates:bundleIdFilter:limit:].cold.1
- -[ATXClientDuetHelper _getIntentEventForSource:startDate:endDate:otherPredicates:bundleIdFilter:limit:].cold.2
- -[ATXClientDuetHelper _queryDuetStream:startDate:endDate:otherPredicates:limit:]
- -[ATXClientDuetHelper _queryDuetStreamUnbatched:startDate:endDate:otherPredicates:limit:]
- -[ATXClientDuetHelper _queryDuetStreamUnbatched:startDate:endDate:otherPredicates:limit:].cold.1
- -[ATXClientDuetHelper _queryDuetStreamUnbatched:startDate:endDate:otherPredicates:limit:].cold.2
- -[ATXClientDuetHelper _queryDuetStreamUnbatched:startDate:endDate:otherPredicates:limit:].cold.3
- -[ATXClientDuetHelper getActivityEventsBetweenStartDate:endDate:]
- -[ATXClientDuetHelper getActivityEventsBetweenStartDate:endDate:bundleIdFilter:]
- -[ATXClientDuetHelper getActivityEventsBetweenStartDate:endDate:bundleIdFilter:].cold.1
- -[ATXClientDuetHelper getActivityEventsBetweenStartDate:endDate:bundleIdFilter:].cold.2
- -[ATXClientDuetHelper getActivityEventsBetweenStartDate:endDate:bundleIdFilter:].cold.3
- -[ATXClientDuetHelper getActivityEventsBetweenStartDate:endDate:bundleIdFilter:].cold.4
- -[ATXClientDuetHelper getIntentEventsBetweenStartDate:endDate:]
- -[ATXClientDuetHelper getIntentEventsBetweenStartDate:endDate:bundleIdFilter:forSource:]
- -[ATXClientDuetHelper getIntentEventsBetweenStartDate:endDate:forSource:]
- -[ATXCombinedIntentStream getActivityAndIntentEventsBetweenStartDate:endDate:ascending:]
- -[ATXCombinedIntentStream getActivityAndIntentEventsFromLastMonth]
- -[ATXCombinedIntentStream getSortedActivityAndIntentEventsBetweenStartDate:endDate:bundleIdFilter:comparator:]
- -[ATXDefaultHomeScreenItemManager _generateSmartStackForCarPlayWithDescriptorCache]
- -[ATXDefaultHomeScreenItemManager _generateSmartStackForCarPlayWithDescriptorCache].cold.1
- -[ATXDefaultHomeScreenItemManager _generateSmartStacksForCarPlay]
- -[ATXDefaultHomeScreenItemRanker widgetsBySortingAndFilteringWidgetsUsingPersonalizedGalleryAlgorithm:rankerPlistType:regularlyUsedThreshold:]
- -[ATXHomeScreenConfigCache loadHomeScreenAndTodayPageConfigurationsFromJSONAtPath:error:]
- -[ATXSpotlightClient .cxx_destruct]
- -[ATXSpotlightClient delegate]
- -[ATXSpotlightClient setDelegate:]
- -[ATXSpotlightEvent initWithAbsoluteDate:eventType:appConsumerSubType:actionConsumerSubType:appBlendingCacheId:actionBlendingCacheId:appSuggestionIds:actionSuggestionIds:metadata:]
- -[ATXSpotlightEvent initWithDate:eventType:appConsumerSubType:actionConsumerSubType:appBlendingCacheId:actionBlendingCacheId:appSuggestionIds:actionSuggestionIds:metadata:]
- -[ATXUserEducationSuggestion initWithUUID:]
- GCC_except_table34
- GCC_except_table64
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _OBJC_CLASS_$_ATXClientDuetHelper
- _OBJC_CLASS_$_NSCompoundPredicate
- _OBJC_CLASS_$__DKAnyIntegerCategory
- _OBJC_CLASS_$__DKApplicationActivityMetadataKey
- _OBJC_CLASS_$__DKCategory
- _OBJC_CLASS_$__DKEvent
- _OBJC_CLASS_$__DKEventQuery
- _OBJC_CLASS_$__DKIntentMetadataKey
- _OBJC_CLASS_$__DKKnowledgeStore
- _OBJC_CLASS_$__DKQuery
- _OBJC_CLASS_$__DKSystemEventStreams
- _OBJC_IVAR_$_ATXAppDirectoryCategory._appBundleIDs
- _OBJC_IVAR_$_ATXAppDirectoryClient._knowledgeStore
- _OBJC_IVAR_$_ATXAppDirectoryClient._knowledgeStream
- _OBJC_IVAR_$_ATXAppDirectoryResponse._predictedApps
- _OBJC_IVAR_$_ATXAppDirectoryResponse._recentApps
- _OBJC_IVAR_$_ATXSpotlightClient._delegate
- _OBJC_METACLASS_$_ATXClientDuetHelper
- __OBJC_$_CLASS_METHODS_ATXClientDuetHelper
- __OBJC_$_INSTANCE_METHODS_ATXClientDuetHelper
- __OBJC_$_INSTANCE_METHODS_ATXSpotlightClient
- __OBJC_$_INSTANCE_VARIABLES_ATXSpotlightClient
- __OBJC_$_PROP_LIST_ATXSpotlightClient
- __OBJC_$_PROP_LIST_ATXUserEducationSuggestion.64
- __OBJC_CLASS_RO_$_ATXClientDuetHelper
- __OBJC_METACLASS_RO_$_ATXClientDuetHelper
- ___107+[ATXDefaultHomeScreenItemManager _descriptorsByFilteringDescriptors:variant:fromAppsDisabledOnHomeScreen:]_block_invoke
- ___108-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:completionHandler:]_block_invoke
- ___108-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:completionHandler:]_block_invoke.43
- ___108-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:completionHandler:]_block_invoke.50
- ___108-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:completionHandler:]_block_invoke.cold.1
- ___108-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:completionHandler:]_block_invoke.cold.2
- ___108-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:completionHandler:]_block_invoke_2
- ___108-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:completionHandler:]_block_invoke_3
- ___108-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:completionHandler:]_block_invoke_4
- ___113-[ATXAppDirectoryClient predictedAppsAndRecentAppsWithMaxNumberOfPredictedApps:shouldUseDefaultCategories:reply:]_block_invoke.38
- ___113-[ATXAppDirectoryClient predictedAppsAndRecentAppsWithMaxNumberOfPredictedApps:shouldUseDefaultCategories:reply:]_block_invoke.39
- ___113-[ATXAppDirectoryClient predictedAppsAndRecentAppsWithMaxNumberOfPredictedApps:shouldUseDefaultCategories:reply:]_block_invoke.cold.1
- ___18-[ATXAction proto]_block_invoke.108
- ___202-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedAmbientOnboardingStacksForSize:stack1RequiredWidgetPersonalities:stack2RequiredWidgetPersonalities:rankedWidgets:usedWidgetPersonalities:]_block_invoke.94
- ___248-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedOnboardingStackForSize:requiredWidgetPersonalities:conditionalWidgetPersonalities:fallbackWidgetPersonalities:rankedThirdPartyWidgets:usedWidgetPersonalities:shouldAdd3PWidgetToStack:]_block_invoke.104
- ___37+[ATXClientDuetHelper sharedInstance]_block_invoke
- ___45-[ATXAppDirectoryClient _logToDuet:metadata:]_block_invoke
- ___45-[ATXAppDirectoryClient _logToDuet:metadata:]_block_invoke.cold.1
- ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.371
- ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.371.cold.1
- ___63-[ATXClientDuetHelper getIntentEventsBetweenStartDate:endDate:]_block_invoke
- ___71-[ATXFaceSuggestionClient fetchFaceSuggestionsForFocusMode:completion:]_block_invoke.42
- ___71-[ATXFaceSuggestionClient fetchFaceSuggestionsForFocusMode:completion:]_block_invoke.43
- ___73+[ATXSpotlightClient rerankRecents_LimitCount:oneCountDays:twoCountDays:]_block_invoke.242
- ___73+[ATXSpotlightClient rerankRecents_LimitCount:oneCountDays:twoCountDays:]_block_invoke.242.cold.1
- ___73+[ATXSpotlightClient rerankRecents_LimitCount:oneCountDays:twoCountDays:]_block_invoke.242.cold.2
- ___80-[ATXClientDuetHelper _queryDuetStream:startDate:endDate:otherPredicates:limit:]_block_invoke
- ___83-[ATXDefaultHomeScreenItemManager _generateSmartStackForCarPlayWithDescriptorCache]_block_invoke
- ___88-[ATXCombinedIntentStream getActivityAndIntentEventsBetweenStartDate:endDate:ascending:]_block_invoke
- ___91-[ATXDefaultHomeScreenItemUpdater _updateAmbientDefaultsOnQueueWithReason:appLaunchCounts:]_block_invoke.51
- ___91-[ATXDefaultHomeScreenItemUpdater _updateAmbientDefaultsOnQueueWithReason:appLaunchCounts:]_block_invoke_2.55
- ___91-[ATXDefaultHomeScreenItemUpdater _updateAmbientDefaultsOnQueueWithReason:appLaunchCounts:]_block_invoke_2.55.cold.1
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.53
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.53.cold.1
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.54
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.54.cold.1
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.54.cold.2
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.54.cold.3
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.54.cold.4
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.55
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.59
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.60
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.64
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.65
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.68
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke_2.66
- ___ATXHomeScreenStackConfigFromATXWidgetStack_block_invoke
- ___block_descriptor_32_e20_v20?0B8"NSError"12l
- ___block_descriptor_40_e8_32s_e17_v16?0"NSArray"8ls32l8
- ___block_descriptor_48_e8_32s_e25_v32?0"NSString"8Q16^B24ls32l8
- ___block_descriptor_56_e8_32s40s_e30_"ATXAppDirectoryResponse"8?0ls32l8s40l8
- ___block_descriptor_56_e8_32s_e39_B16?0"ATXHomeScreenWidgetDescriptor"8ls32l8
- ___block_descriptor_64_e8_32bs_e52_v24?0"ATXDefaultHomeScreenItemUpdate"8"NSError"16ls32l8
- ___block_literal_global.11
- ___block_literal_global.111
- ___block_literal_global.45
- ___block_literal_global.519
- ___block_literal_global.54
- ___block_literal_global.75
- ___block_literal_global.8
- ___block_literal_global.93
- ___block_literal_global.96
- __enumerateBatchesInDuetStream:startDate:endDate:otherPredicates:limit:block:.duetLock
- _objc_msgSend$_descriptionForTopic:
- _objc_msgSend$_descriptorsByFilteringDescriptors:variant:fromAppsDisabledOnHomeScreen:
- _objc_msgSend$_enumerateBatchesInDuetStream:startDate:endDate:otherPredicates:limit:block:
- _objc_msgSend$_generateSmartStackForCarPlayWithDescriptorCache
- _objc_msgSend$_generateSmartStacksForCarPlay
- _objc_msgSend$_getIntentEventForSource:startDate:endDate:otherPredicates:bundleIdFilter:limit:
- _objc_msgSend$_logToDuet:metadata:
- _objc_msgSend$_queryDuetStream:startDate:endDate:otherPredicates:limit:
- _objc_msgSend$_queryDuetStreamUnbatched:startDate:endDate:otherPredicates:limit:
- _objc_msgSend$_responseWithSpotlightLayout:andSpotlightRecentTopics:
- _objc_msgSend$allIdentifiers
- _objc_msgSend$andPredicateWithSubpredicates:
- _objc_msgSend$appActivityStream
- _objc_msgSend$appBundleIDs
- _objc_msgSend$appDirectoryInteractionStream
- _objc_msgSend$appIntentsStream
- _objc_msgSend$categoryWithInteger:type:
- _objc_msgSend$eventQueryWithPredicate:eventStreams:offset:limit:sortDescriptors:
- _objc_msgSend$eventStreams
- _objc_msgSend$eventWithStream:startDate:endDate:value:metadata:
- _objc_msgSend$executeQuery:error:
- _objc_msgSend$getActivityAndIntentEventsBetweenStartDate:endDate:ascending:
- _objc_msgSend$getActivityEventsBetweenStartDate:endDate:
- _objc_msgSend$getActivityEventsBetweenStartDate:endDate:bundleIdFilter:
- _objc_msgSend$getIntentEventsBetweenStartDate:endDate:bundleIdFilter:forSource:
- _objc_msgSend$getIntentEventsBetweenStartDate:endDate:forSource:
- _objc_msgSend$getSortedActivityAndIntentEventsBetweenStartDate:endDate:bundleIdFilter:comparator:
- _objc_msgSend$initWithAbsoluteDate:eventType:appConsumerSubType:actionConsumerSubType:appBlendingCacheId:actionBlendingCacheId:appSuggestionIds:actionSuggestionIds:metadata:
- _objc_msgSend$initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:
- _objc_msgSend$initWithCategoryID:appBundleIDs:
- _objc_msgSend$initWithDate:eventType:appConsumerSubType:actionConsumerSubType:appBlendingCacheId:actionBlendingCacheId:appSuggestionIds:actionSuggestionIds:metadata:
- _objc_msgSend$initWithQueryString:context:
- _objc_msgSend$initWithSuggestionLayout:recentApps:hiddenApps:otherAppsOnScreen:numAppsToPredict:error:
- _objc_msgSend$initWithUUID:
- _objc_msgSend$intentHandlingStatus
- _objc_msgSend$isActionEligibleForSettingsSuggestionsWithBundleIdentifier:actionIdentifier:
- _objc_msgSend$knowledgeStore
- _objc_msgSend$metadata
- _objc_msgSend$predicateForObjectsWithMetadataKey:andIntegerValue:
- _objc_msgSend$saveObjects:responseQueue:withCompletion:
- _objc_msgSend$serializedInteraction
- _objc_msgSend$widgetsBySortingAndFilteringWidgetsUsingPersonalizedGalleryAlgorithm:rankerPlistType:regularlyUsedThreshold:
- _sharedInstance._pasOnceToken6
- _sharedInstance._pasOnceToken8
- _sharedInstanceWithMobileAssets._pasOnceToken11
CStrings:
+ " > "
+ "!(intent && activityString && menuItemPath) && !(intent && activityString) && !(intent && menuItemPath) && !(activityString && menuItemPath)"
+ "!intent && !activityString && !menuItemPath && !toolInvocationID"
+ "!intent && !activityString && !menuItemPath && !userActivityProxy"
+ "%@ - %@"
+ "%@ asset for rule %@ is malformed, the rule will be ignored"
+ "%@ asset for rule %@ is not compiling pattern %@ with error %@"
+ "%s Unable to create bookmark data for file URL %@ because of error %@."
+ "%s: ATXDefaultHomeScreenItemUpdate is nil"
+ "%s: Activating connection"
+ "%s: Error fetching widget descriptors - %{public}@"
+ "%s: Error when attempting to fetch widget descriptors or list was empty - %{public}@"
+ "%s: Fetching Widget Smart Stacks for CarPlay with identifier: %@"
+ "%s: Fetching Widget gallery items for CarPlay with identifier: %@"
+ "%s: Invalidating and cleaning up connection"
+ "%s: No onboarding stack suggestions available for CarPlay, returning nil"
+ "%s: PersonaIdentifier %@ doesn't match widget device identifier %@. Not returning widget descriptor: %@"
+ "%s: PersonaIdentifier is nil. Not returning Remote widgets"
+ "%s: filtering out widget descriptor: %@. Reason: Widget's extension identifier in deny list %@"
+ "%s: filtering out widget descriptor: %@. Reason: Widget's full descriptor found in deny list %@"
+ "%s: filtering out widget descriptor: %@. Reason: Widget's parent bundleId in deny list %@"
+ "("
+ "+[ATXDefaultHomeScreenItemManager _descriptorsByFilteringDescriptors:variant:fromAppsDisabledOnHomeScreen:fromExcludedWidgetsWithIdentifiers:personaIdentifier:]_block_invoke"
+ "+[ATXDefaultHomeScreenItemManager shouldFilterOutWidgetDescriptorDueToDenyList:fromExcludedWidgetsWithIdentifiers:]"
+ "-[ATXDefaultHomeScreenItemManager _generateSmartStackForCarPlayWithDescriptorCacheFromRequest:error:]"
+ "-[ATXDefaultHomeScreenItemManager _generateSmartStacksForCarPlayWithRequest:error:]"
+ "-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:personaIdentifier:completionHandler:]"
+ "-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:personaIdentifier:completionHandler:]_block_invoke"
+ "-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:personaIdentifier:completionHandler:]_block_invoke_2"
+ "-[ATXDefaultHomeScreenItemManager galleryItemsForCarPlayWithRequest:error:]"
+ "-[ATXDonationManager _cleanUpConnection]"
+ "-[ATXDonationManager _connection]"
+ "-[ATXDonationManager _connection]_block_invoke"
+ "-[ATXFaceSuggestionClient fetchFaceGalleryConfigurationForSemanticType:completion:]"
+ "-[ATXFaceSuggestionClient fetchFaceGalleryConfigurationForSemanticType:completion:]_block_invoke"
+ "-[ATXFileIdentity initWithItemURL:]"
+ "-[ATXUserEducationSuggestionPosterSetup initWithCoder:]"
+ ".*"
+ "/"
+ "<%@ posterId: %@>"
+ "<%@:%@>"
+ "<ATXMenuItemInvocation of %@ through %@ from %@ %@>"
+ "<ATXRegexFilter: %@ %@ %@>"
+ "@\"<ATXPredictionScope>\""
+ "@\"ATXAppIdentity\""
+ "@\"ATXAppIdentity\"16@?0@\"NSString\"8"
+ "@\"ATXAppInFocusStream\""
+ "@\"ATXCarPlayConnectedStream\""
+ "@\"ATXFileIdentity\""
+ "@\"ATXMenuItemIdentity\""
+ "@\"ATXMenuItemStream\""
+ "@\"ATXToolKitActionStream\""
+ "@\"ATXWidgetClientIdentity\""
+ "@\"ATXWidgetGalleryRequest\""
+ "@\"ATXWidgetSmartStackRequest\""
+ "@\"BGSystemTask\""
+ "@\"NSData\"16@?0@\"ATXIntentEvent\"8"
+ "@\"NSRegularExpression\"16@?0@\"NSString\"8"
+ "@\"NSString\"16@?0@\"ATXAppIdentity\"8"
+ "@16@?0@\"ATXAppIdentity\"8"
+ "@16@?0@\"ATXPredictedDocumentIdentity\"8"
+ "@188@0:8@16@24@32@40@48@56@64@72@80Q88@96@104@112B120@124@132@140@148@156@164@172@180"
+ "@24@0:8B16B20"
+ "@44@0:8@16i24d28@36"
+ "@48@0:8@16Q24Q32@40"
+ "@56@0:8@16@24Q32@40^@48"
+ "@56@0:8@16Q24@32@40@48"
+ "@64@0:8Q16@24@32@40Q48@56"
+ "@68@0:8@16B24@28@36@44Q52@60"
+ "@92@0:8@16i24@28@36@44@52@60@68@76@84"
+ "@92@0:8d16i24@28@36@44@52@60@68@76@84"
+ "ATXActionScope"
+ "ATXActionScope: %@, %@, %@, %@"
+ "ATXActionSuggestionRequest"
+ "ATXActionTypeMenuItem"
+ "ATXActionTypeToolKitAction"
+ "ATXActivityProgressProtocol"
+ "ATXAppDirectoryCategory.m"
+ "ATXAppDirectoryClient.DiskRead"
+ "ATXAppDirectoryClient: Attempting to retrieve relevant App Directory cached entities: Predicted Apps, Recent apps and Hidden apps"
+ "ATXAppDirectoryClient: Failed to read Recent apps with error: %@"
+ "ATXAppDisplayIdentifiersDenyList"
+ "ATXAppIdentity"
+ "ATXAppIdentity %@, type: %@;"
+ "ATXAppIdentity.m"
+ "ATXAppIdentity_NSString"
+ "ATXAppLaunchCarPlayContext"
+ "ATXBackgroundActivityProtocol"
+ "ATXBackgroundSystemTask"
+ "ATXClientDonationsXPCInterface"
+ "ATXDefaultHomeScreenItemProducer: not adding required widget %{public}@ to stack because it is already used"
+ "ATXDefaultHomeScreenItemProducer: not adding required widget %{public}@ to stack because it is in client's deny list"
+ "ATXDocumentCategory"
+ "ATXDocumentInteraction"
+ "ATXDocumentInteraction.m"
+ "ATXDocumentInteractionCodingKeyAppIdentity"
+ "ATXDocumentInteractionCodingKeyContentTypeIdentifier"
+ "ATXDocumentInteractionCodingKeyFileIdentity"
+ "ATXDocumentInteractionCodingKeyType"
+ "ATXDocumentInteractionDonationClient"
+ "ATXDocumentPredictionClient"
+ "ATXDocumentPredictionRequest"
+ "ATXDocumentPredictionResponse"
+ "ATXDocumentRegexFilter"
+ "ATXDocumentScope"
+ "ATXDocumentScope: %@"
+ "ATXDonationManager"
+ "ATXFileIdentity"
+ "ATXFileIdentityCodingKeyBookmarkData"
+ "ATXFileIdentityCodingKeyItemURL"
+ "ATXMenuItemDonationClient"
+ "ATXMenuItemIdentity"
+ "ATXMenuItemInvocation"
+ "ATXMenuItemRegexFilter"
+ "ATXMenuItemStream"
+ "ATXMenuItemStream: Can't read App.MenuItem stream with error: %@"
+ "ATXPredictedDocumentCacheItem"
+ "ATXPredictedDocumentIdentity"
+ "ATXPredictionRequest"
+ "ATXPredictionResponse"
+ "ATXPredictionScope"
+ "ATXRegexFilter"
+ "ATXRegexFilter %@ asset is malformed"
+ "ATXRegexFilter for %@ has been evaluated on a nil string."
+ "ATXRegexFilter for %@ should not call the base class method to perform any filtering."
+ "ATXSpotlightClient: _resultWithActionSuggestion action %@ has no intent nor user activity, and is not a menu item"
+ "ATXToolKitActionStream"
+ "ATXUserEducationSuggestionPosterSetup"
+ "ATXWidgetClientIdentity"
+ "ATXWidgetGalleryRequest"
+ "ATXWidgetGalleryResponse"
+ "ATXWidgetSmartStackRequest"
+ "ATXWidgetSmartStackResponse"
+ "Accessibility"
+ "Activities using BGST (%@) should only call didDefer which handles the deferral"
+ "B16@?0@\"ATXAppInFocusEventSession\"8"
+ "B16@?0@\"ATXCarPlayConnectedEvent\"8"
+ "B24@?0@\"NSDate\"8@\"NSDate\"16"
+ "Background task %@ has expired"
+ "Behavioral"
+ "Blending providing suggestions to %@ inside ATXActionPredictionClient..."
+ "Bookmark data is nil."
+ "Bundle identifier is hidden for Settings action: %@"
+ "ContextualMenu"
+ "Could not obtain semantically similar file URLs with error: %@"
+ "Couldn't get path for ATXAppDisplayIdentifiersDenyList"
+ "DOCUMENT_SUGGESTIONS"
+ "Demo"
+ "DiscoverySuggestions.codingKeyForPosterId"
+ "DocumentPredictionDemo.json"
+ "Donate document interaction: %@"
+ "Donation Processing (Link) - Action not predictable: %@"
+ "Donation Processing (Link) - Could not fetch INAppIntent(_className); bundle id: %@; action id: %@"
+ "Donation Processing (Menu Item) - Empty path"
+ "Donation Processing (Menu Item) - Nil app identifiers"
+ "Donation Processing (Menu Item) - Rejected: filtered out bundle id %@ that doesn't match %@"
+ "Edit"
+ "EnabledPreferenceRules"
+ "Error loading ATXAppDisplayIdentifiersDenyList contents: %@"
+ "Error loading ATXAppDisplayIdentifiersDenyList with path %@: %@"
+ "Failed to call setTaskExpiredWithRetryAfter for %@ : %@"
+ "Failed to encodedInvocations.count != toolKitIntents.count ==> %ld != %ld"
+ "Failed to fetch titles: %@"
+ "Failed to generate smart stacks"
+ "Failed to get recents: %@"
+ "Failed to load CarPlay widget descriptors or metadata."
+ "Failed to notify spotlight invoked: %@"
+ "Failed to produce home screen item update for CarPlay."
+ "Failed to report progress for %@ to bgst: %@"
+ "Failed to resolve document at %@ : %@"
+ "Filtering %@ as it doesn't meet the scope: %@"
+ "Got recents: %@"
+ "KeyboardShortcut"
+ "Menu item invocation donation: %@"
+ "MenuBar"
+ "MenuItem"
+ "Mouse"
+ "Native app"
+ "No CarPlay items found"
+ "No items found"
+ "No smart stacks generated for CarPlay"
+ "Open"
+ "PosterSetup"
+ "Predictable parameters for %@ from link: %@"
+ "RECENT_DOCUMENTS"
+ "Remote app"
+ "ReturnKey"
+ "RunIntelligenceCommand"
+ "Save"
+ "Semantic"
+ "Settings action does not have an associated bundle id containing a string anymore; actual: %@"
+ "Settings action does not have an associated bundle id property anymore"
+ "SpatialPhotos"
+ "SpotlightPlusDemoModeEnabled"
+ "Successfully called setTaskExpiredWithRetryAfter:BGSystemTaskRetryAfterDefault for %@"
+ "System.iphoneApps"
+ "System.onenessApps"
+ "SystemAccepted"
+ "T@\"<ATXPredictionScope>\",R,N,V_scope"
+ "T@\"ATXAppIdentity\",R"
+ "T@\"ATXAppIdentity\",R,C,N,V_appIdentity"
+ "T@\"ATXAppIdentity\",R,N,V_appIdentifier"
+ "T@\"ATXAppIdentity\",R,N,V_appIdentity"
+ "T@\"ATXFileIdentity\",R,C,N,V_fileIdentity"
+ "T@\"ATXMenuItemIdentity\",R,N,V_identity"
+ "T@\"ATXWidgetClientIdentity\",R,N,V_clientIdentity"
+ "T@\"ATXWidgetGalleryRequest\",&,N,V_galleryRequest"
+ "T@\"ATXWidgetSmartStackRequest\",&,N,V_smartStackRequest"
+ "T@\"BGSystemTask\",&,N,V_bgSystemTask"
+ "T@\"NSArray\",&,N,V_documentSuggestionIds"
+ "T@\"NSArray\",&,N,V_spotlightRecentTopics"
+ "T@\"NSArray\",C,N,V_denyListOfExtensions"
+ "T@\"NSArray\",R,C,N,V_menuItemPath"
+ "T@\"NSArray\",R,C,N,V_onboardingStacks"
+ "T@\"NSArray\",R,C,N,V_predictedDocuments"
+ "T@\"NSArray\",R,C,N,V_stacks"
+ "T@\"NSArray\",R,N,V_appIdentities"
+ "T@\"NSArray\",R,N,V_documentURLs"
+ "T@\"NSArray\",R,N,V_menuItemsPath"
+ "T@\"NSArray\",R,N,V_parameterKeysForToolInvocation"
+ "T@\"NSArray\",R,N,V_predictedAppIdentities"
+ "T@\"NSArray\",R,N,V_predictedDocumentIdentities"
+ "T@\"NSArray\",R,N,V_recentAppIdentities"
+ "T@\"NSArray\",R,N,V_types"
+ "T@\"NSData\",&,N,V_bookmarkData"
+ "T@\"NSData\",&,N,V_encodedToolInvocation"
+ "T@\"NSData\",R,C,N,V_bookmarkData"
+ "T@\"NSData\",R,N,V_encodedToolInvocation"
+ "T@\"NSDictionary\",R,N,V_appEntityKeyValueMapping"
+ "T@\"NSMutableArray\",&,N,V_menuItemPathComponents"
+ "T@\"NSMutableArray\",&,N,V_parameterKeysForToolInvocations"
+ "T@\"NSMutableDictionary\",&,N,V_categoryWithLimit"
+ "T@\"NSNumber\",&,N,V_limit"
+ "T@\"NSNumber\",&,N,V_maximumWidgetsPerStack"
+ "T@\"NSNumber\",&,N,V_numberOfStacks"
+ "T@\"NSNumber\",R,N,V_predictionScore"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
+ "T@\"NSObject<OS_os_log>\",&,N,V_handle"
+ "T@\"NSString\",&,N,V_clientBundleID"
+ "T@\"NSString\",&,N,V_toolInvocationID"
+ "T@\"NSString\",C,N,V_clientSessionIdentifier"
+ "T@\"NSString\",R,C,N,V_associatedAppBundleID"
+ "T@\"NSString\",R,C,N,V_contentTypeIdentifier"
+ "T@\"NSString\",R,N,V_bundleIdentifier"
+ "T@\"NSString\",R,N,V_intentClassName"
+ "T@\"NSString\",R,N,V_localizedKeyboardShorctcutDisplayName"
+ "T@\"NSString\",R,N,V_posterId"
+ "T@\"NSString\",R,N,V_toolInvocationID"
+ "T@\"NSURL\",R,C,N,V_itemURL"
+ "T@\"NSURL\",R,N,V_bundleURL"
+ "T@\"NSURL\",R,N,V_documentURL"
+ "TB,N,V_taskDeferred"
+ "TB,N,V_taskExpiryCalled"
+ "TC,N,V_currentProgressUnits"
+ "TQ,N,V_galleryVariant"
+ "TQ,N,V_smartStackVariant"
+ "TQ,N,V_widgetClient"
+ "TQ,N,V_widgetGridSize"
+ "TQ,R,N,V_appType"
+ "TQ,R,N,V_invocationType"
+ "TQ,R,N,V_limit"
+ "TQ,R,N,V_sourceType"
+ "Tall"
+ "ToolKit"
+ "URLByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:"
+ "Unknown (%tu)"
+ "Unknown app type"
+ "UserAccepted"
+ "UserEdited"
+ "Web app"
+ "[ATXAppDisplayIdentifiersDenyList] Invalid plist format for with path: %@"
+ "[ATXAppDisplayIdentifiersDenyList] Non-string item found in plist: %@"
+ "[Demo] Could not load demo documents: %@"
+ "[Demo] Could not parse demo documents %@: %@"
+ "[Demo] Recents: %@, Suggestions: %@"
+ "_allIdentifiersIncludingRemoteApps:includeInternalMacOSApps:"
+ "_appEntityKeyValueMapping"
+ "_appIdentifier"
+ "_appIdentifiersIncludingRemoteApps:includeInternalMacOSApps:"
+ "_appIdentities"
+ "_appIdentity"
+ "_appInFocusStream"
+ "_appType"
+ "_assetName"
+ "_associatedAppBundleID"
+ "_attributesFilters"
+ "_bgSystemTask"
+ "_bookmarkData"
+ "_bundleIdentifier"
+ "_bundleIdsFilters"
+ "_bundleURL"
+ "_carPlayConnectedStream"
+ "_categoryWithLimit"
+ "_checkString:againstRegexesArray:"
+ "_checkString:againstRegexesArrayDictionary:"
+ "_cleanUpConnection"
+ "_clientBundleID"
+ "_clientIdentity"
+ "_clientSessionIdentifier"
+ "_combinedFilters"
+ "_compilePatterns:assetName:ruleName:"
+ "_contentTypeIdentifier"
+ "_currentProgressUnits"
+ "_demoDocumentsPath"
+ "_denyListOfExtensions"
+ "_descriptorsByFilteringDescriptors:variant:fromAppsDisabledOnHomeScreen:fromExcludedWidgetsWithIdentifiers:personaIdentifier:"
+ "_documentSuggestionIds"
+ "_documentURL"
+ "_documentURLs"
+ "_donateDocumentInteraction:completion:"
+ "_donateMenuItem:completion:"
+ "_effectiveBundleIdentifierForBundleIdentifier:"
+ "_encodedToolInvocation"
+ "_enumerateMenuItemEventsBetweenStartDate:endDate:bundleIdFilter:reversed:block:"
+ "_fileIdentity"
+ "_galleryRequest"
+ "_galleryVariant"
+ "_generateSmartStackForCarPlayWithDescriptorCacheFromRequest:error:"
+ "_generateSmartStacksForCarPlayWithRequest:error:"
+ "_getDocumentsForDemoMode"
+ "_getIntentEventFromBMAppMenuItem:bundleIdFilter:"
+ "_identity"
+ "_initWithAssetName:asset:"
+ "_initWithBundleIdentifier:bundleURL:appType:"
+ "_intentClassName"
+ "_invocationType"
+ "_isDemoModeEnabled"
+ "_itemURL"
+ "_localizedKeyboardShorctcutDisplayName"
+ "_maximumWidgetsPerStack"
+ "_menuItemPath"
+ "_menuItemPathComponents"
+ "_menuItemStream"
+ "_menuItemsPath"
+ "_numberOfStacks"
+ "_parameterKeysForToolInvocation"
+ "_parameterKeysForToolInvocations"
+ "_pas_componentsJoinedByString:"
+ "_personalizedCarPlayOnboardingStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:"
+ "_posterId"
+ "_predictedAppIdentities"
+ "_predictedDocumentIdentities"
+ "_predictedDocuments"
+ "_predictionScore"
+ "_processIdentifiersFromEnumerator:intoSet:withSupportedAppPaths:includeInternalMacOSApps:"
+ "_recentAppIdentities"
+ "_responseWithSpotlightLayout:andSpotlightRecentTopics:actionScope:limit:"
+ "_setError"
+ "_smartStackRequest"
+ "_smartStackVariant"
+ "_sourceType"
+ "_spotlightRecentTopics"
+ "_suggestedResultResponseWithLimit:andSpotlightRecentTopics:actionScope:"
+ "_taskDeferred"
+ "_taskExpiryCalled"
+ "_toolInvocationID"
+ "_toolKitActionStream"
+ "_types"
+ "_widgetClient"
+ "_widgetGridSize"
+ "addMenuItemPathComponent:"
+ "addParameterKeysForToolInvocation:"
+ "appEntityKeyValueMapping"
+ "appIdentifier"
+ "appIdentities"
+ "appIdentitiesFromBundleIDs"
+ "appIdentity"
+ "appIdentity != nil"
+ "appIdentity.bundleIdentifier is nil"
+ "appLaunchCountAndDistinctDaysLaunchedWhileConnectedToCarPlayForNumberOfDays:"
+ "appSessionEndTime"
+ "appSessionStartTime"
+ "appType"
+ "arrayWithCapacity:"
+ "associatedAppBundleID"
+ "associatedApplicationBundleIdentifier"
+ "associatedBundleId"
+ "attributesRegexes"
+ "atxHomeScreenStackConfigFromATXWidgetStack:"
+ "atxHomeScreenWidgetIdentifierFromATXWidget:"
+ "atx_errorWithCode:debugDescription:"
+ "bgSystemTask"
+ "bookmarkData"
+ "bookmarkDataWithOptions:includingResourceValuesForKeys:relativeToURL:error:"
+ "bundleIDWithRelevantPrefix"
+ "bundleIDsFromIdentities"
+ "bundleIdentifier should be non-nil when using bundleIDsFromIdentities"
+ "bundleIdentifierIsHiddenForSettingsAction"
+ "bundleIdentifiersNotAllowed"
+ "bundleIdsRegexes"
+ "bundleURL"
+ "bundleWithURL:"
+ "carPlayOnboardingRequiredWidgetsForDefaultStack%ld"
+ "categoriesForRequest:withReply:"
+ "categoryWithLimit"
+ "clearMenuItemPathComponents"
+ "clearParameterKeysForToolInvocations"
+ "clientBundleID"
+ "clientIdentity"
+ "clientSessionIdentifier"
+ "client_donations"
+ "com.apple.ATXPredictionErrorDomain"
+ "com.apple.Bridge"
+ "com.apple.Health.Sleep"
+ "com.apple.Spotlight"
+ "com.apple.duetexpertd.atx.screenEntities"
+ "com.apple.proactive.app-client.donation"
+ "contentTypeIdentifier"
+ "conversationIdentifier"
+ "currentAppIdentity"
+ "currentProgressUnits"
+ "denyListOfExtensions"
+ "descriptionForAppType:"
+ "descriptionForTopic:"
+ "deviceIdentifier"
+ "dictionaryWithValuesForKeys:"
+ "documentPredictor"
+ "documentSuggestionIds"
+ "documentSuggestionTappedWithPath:date:"
+ "documentSuggestionTypeFromString:"
+ "documentURL"
+ "documentURLs"
+ "donateDocumentInteraction:completion:"
+ "donateDocumentInteractionForType:fileURL:contentTypeIdentifier:completion:"
+ "donateMenuItem:completion:"
+ "donateMenuItemInvocation:completion:"
+ "encodedToolInvocation"
+ "enumerateAllAppLaunchSessionsFromStartDate:bundleIDFilter:block:"
+ "enumerateConnectedEventsFromStartDate:endDate:filterBlock:limit:ascending:block:"
+ "fetchFaceGalleryConfigurationForSemanticType"
+ "fetchFaceGalleryConfigurationForSemanticType:completion:"
+ "fetchGalleryItemsForVariant:gridSize:supportedFamilies:personaIdentifier:completionHandler:"
+ "fetchMenuItemsForCurrentAppInFocus:"
+ "fetchMenuItemsForCurrentAppInFocusWithCompletion:"
+ "fetchPreWarmedContextualActionSuggestionsWithCompletion:"
+ "fetchPreWarmedContextualActionSuggestionsWithError:"
+ "fetchSemanticallySimilarDocumentsWithCompletion:"
+ "fetchTitlesFromToolInvocations:completionHandler:"
+ "fetchToolKitBasedFallbackActionIds:"
+ "fetchToolKitBasedFallbackActionIdsWithCompletion:"
+ "fetchWidgetGalleryItemsWithRequest:completionHandler:"
+ "fetchWidgetSmartStackWithRequest:completionHandler:"
+ "fileIdentity"
+ "fileIdentity != nil"
+ "galleryItemsForCarPlayWithRequest:error:"
+ "galleryRequest"
+ "galleryVariant"
+ "getBytes:range:"
+ "getCombinedIntentEventsBetweenStartDate:endDate:ascending:"
+ "getCombinedIntentEventsFromLastMonth"
+ "getDirectoryResponseFromCacheWithMaxNumberOfAppsToPredict:"
+ "getMenuItemEventsBetweenStartDate:endDate:"
+ "getMenuItemEventsBetweenStartDate:endDate:bundleIdFilter:"
+ "getMenuItemEventsBetweenStartDate:endDate:bundleIdFilter:limit:"
+ "getSortedCombinedIntentEventsBetweenStartDate:endDate:bundleIdFilter:comparator:"
+ "getToolKitActionEventsBetweenStartDate:endDate:"
+ "getToolKitActionEventsBetweenStartDate:endDate:bundleIdFilter:"
+ "getToolKitActionEventsBetweenStartDate:endDate:bundleIdFilter:limit:"
+ "hasEncodedToolInvocation"
+ "hasError"
+ "hasToolInvocationID"
+ "identity"
+ "inference"
+ "initWithAbsoluteDate:eventType:appConsumerSubType:actionConsumerSubType:appBlendingCacheId:actionBlendingCacheId:appSuggestionIds:actionSuggestionIds:documentSuggestionIds:metadata:"
+ "initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:menuItemPath:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:toolInvocationID:encodedToolInvocation:parameterKeysForToolInvocation:"
+ "initWithAppIdentifier:"
+ "initWithAppIdentifier:appEntityKeyValueMapping:actionType:intentClassName:error:"
+ "initWithAppIdentity:menuItemsPath:"
+ "initWithAppInFocusStream:carPlayStream:"
+ "initWithAssetName:"
+ "initWithBackgroundSystemTask:"
+ "initWithBackgroundSystemTask:logHandle:"
+ "initWithBundleIdentifier:"
+ "initWithBundleIdentifier:appType:"
+ "initWithBundleURL:"
+ "initWithBundleURL:appType:"
+ "initWithCategoryID:appIdentities:"
+ "initWithCategoryID:appIdentitites:localizedName:"
+ "initWithCategoryID:documentURLs:"
+ "initWithClientIdentity:"
+ "initWithClientSessionIdentifier:widgetClient:"
+ "initWithDate:eventType:appConsumerSubType:actionConsumerSubType:appBlendingCacheId:actionBlendingCacheId:appSuggestionIds:actionSuggestionIds:documentSuggestionIds:metadata:"
+ "initWithDocumentURL:predictionScore:"
+ "initWithDocumentURL:predictionScore:bookmarkData:type:"
+ "initWithDocumentURL:predictionScore:type:"
+ "initWithDocuments:"
+ "initWithIdentifier:qos:workloadCategory:expectedMetricValue:itemsCompleted:totalItemCount:"
+ "initWithIdentity:invocationType:sourceType:localizedKeyboardShorctcutDisplayName:"
+ "initWithIntentStream:activityStream:menuItemStream:toolKitActionStream:"
+ "initWithItemURL:"
+ "initWithItemURL:bookmarkData:"
+ "initWithItems:"
+ "initWithLimit:documentScope:"
+ "initWithLimit:scope:"
+ "initWithLimit:scope:spotlightRecentTopics:"
+ "initWithMenuItemPath:actionUUID:bundleId:title:subtitle:"
+ "initWithOnboardingStacks:sortedThirdPartyWidgets:"
+ "initWithPattern:options:error:"
+ "initWithPosterId:"
+ "initWithPredictedDocuments:associatedAppBundleID:"
+ "initWithQueryString:queryContext:"
+ "initWithRemotePlaceholderBundleIdentifier:error:"
+ "initWithStacks:"
+ "initWithSuggestionLayout:includeRemoteApps:recentApps:hiddenApps:otherAppsOnScreen:numAppsToPredict:error:"
+ "initWithToolID:encodedToolKitAction:actionUUID:parameterKeys:bundleId:title:subtitle:"
+ "initWithType:fileIdentity:contentTypeIdentifier:appIdentity:"
+ "initWithUTTypes:error:"
+ "initWithUUID_ATXUserEducationSuggestion:"
+ "intent || activityString || userActivityProxy || menuItemPath || toolInvocationID"
+ "intentClassName"
+ "invocationType"
+ "isActionEligibleForAnySettingsSuggestions:"
+ "isActionEligibleForAnySettingsSuggestionsWithBundleIdentifier:actionIdentifier:"
+ "isActionEligibleForWatchAppSettingsSuggestions:"
+ "isAppleOwnedAppForBundleId:"
+ "isAppleOwnedIncludingInternalOrSystemAppForBundleId:"
+ "isEqualToATXActionScope:"
+ "isEqualToATXAppIdentity:"
+ "isEqualToATXDocumentInteraction:"
+ "isEqualToATXDocumentScope:"
+ "isEqualToATXFileIdentity:"
+ "isEqualToATXMenuItemIdentity:"
+ "isEqualToATXMenuItemInvocation:"
+ "isRemote"
+ "isValidSuggestion:forScope:"
+ "itemURL"
+ "joinComponentsOfMenuItemPath:"
+ "lastDateForToolKitActionEvent"
+ "lastDateOfToolKitAction"
+ "localizedKeyboardShorctcutDisplayName"
+ "mainBundle"
+ "maximumWidgetsPerStack"
+ "menuItemPath"
+ "menuItemPathComponent"
+ "menuItemPathComponentAtIndex:"
+ "menuItemPathComponentType"
+ "menuItemPathComponents"
+ "menuItemPathComponentsCount"
+ "menuItems"
+ "menuItemsPath"
+ "menuPath"
+ "no keyboard shortcut defined"
+ "notifySpotlightInvoked:"
+ "numberOfMenuItemEventsBetweenStartDate:endDate:"
+ "numberOfStacks"
+ "numberOfToolKitActionEventsBetweenStartDate:endDate:"
+ "obfuscatedConversationIdentifier"
+ "obfuscatedJsonWithMapping:"
+ "parameterKeysForToolInvocation"
+ "parameterKeysForToolInvocationAtIndex:"
+ "parameterKeysForToolInvocationType"
+ "parameterKeysForToolInvocations"
+ "parameterKeysForToolInvocationsCount"
+ "position"
+ "posterId"
+ "predictedAppIdentities"
+ "predictedDocumentIdentities"
+ "predictedDocuments"
+ "predictionScore"
+ "predictionType"
+ "predictionsForRequest:withCompletion:"
+ "proactiveSuggestionForIdentity:"
+ "q24@?0@\"ATXCarPlayConnectedEvent\"8@\"ATXCarPlayConnectedEvent\"16"
+ "queue"
+ "recentAppIdentities"
+ "recentURLsWithLimit:typeIdentifiersForScope:withCompletion:"
+ "reportProgressMetrics:error:"
+ "resolveItemURLWithError:"
+ "resolvedURL"
+ "safeStringForConsumerSubtype:"
+ "sanitizeTitleForToolKitIntents:withCompletion:"
+ "screenEntities"
+ "semanticallySimilarDocumentsFromOnScreenAppEntities"
+ "setBgSystemTask:"
+ "setBookmarkData:"
+ "setCategoryWithLimit:"
+ "setClientBundleID:"
+ "setClientSessionIdentifier:"
+ "setCurrentProgressUnits:"
+ "setDenyListOfExtensions:"
+ "setDocumentSuggestionIds:"
+ "setEncodedToolInvocation:"
+ "setExpirationHandlerWithReason:"
+ "setGalleryRequest:"
+ "setGalleryVariant:"
+ "setHandle:"
+ "setLimit:forCategory:"
+ "setMaximumWidgetsPerStack:"
+ "setMenuItemIdentifier:"
+ "setMenuItemPathComponents:"
+ "setNumberOfStacks:"
+ "setParameterKeysForToolInvocations:"
+ "setPosition:"
+ "setProgressUnits:"
+ "setSmartStackRequest:"
+ "setSmartStackVariant:"
+ "setSpotlightRecentTopics:"
+ "setTaskCompleted"
+ "setTaskDeferred:"
+ "setTaskExpiredWithRetryAfter:error:"
+ "setTaskExpiryCalled:"
+ "setToolIdentifier:"
+ "setToolInvocationData:"
+ "setToolInvocationID:"
+ "setWidgetClient:"
+ "setWidgetGridSize:"
+ "shared"
+ "sharedManager"
+ "sharedScheduler"
+ "shouldFilterOutAction:"
+ "shouldFilterOutBundleId:andAttribute:"
+ "shouldFilterOutBundleId:andURL:"
+ "shouldFilterOutOnlyBasedOnAttribute:"
+ "shouldFilterOutOnlyBasedOnBundleId:"
+ "shouldFilterOutURL:"
+ "shouldFilterOutWidgetDescriptorDueToDenyList:fromExcludedWidgetsWithIdentifiers:"
+ "smartStackRequest"
+ "smartStackVariant"
+ "spotlightRecentTopics"
+ "stringArrayForKey:"
+ "stringForATXMenuItemInvocationType called with invalid ATXMenuItemInvocationType value of %lu"
+ "stringForDocumentSuggestionType:"
+ "stringForMenuItemInvocationType:"
+ "stringForMenuItemSourceType called with invalid ATXMenuItemSourceType value of %lu"
+ "stringForMenuItemSourceType:"
+ "taskDeferred"
+ "taskExpiryCalled"
+ "toolInvocationID"
+ "types"
+ "urls"
+ "uuidForIdentities:"
+ "uuidForIdentity:"
+ "v16@?0@\"ATXCarPlayConnectedEvent\"8"
+ "v16@?0Q8"
+ "v32@0:8@\"ATXDocumentInteraction\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"ATXMenuItemIdentity\"16@?<v@?@\"NSError\">24"
+ "v32@0:8Q16Q24"
+ "v32@0:8q16@?<v@?@\"ATXFaceGalleryConfiguration\"@\"NSError\">24"
+ "v32@?0@\"ATXAppIdentity\"8Q16^B24"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
+ "v32@?0@\"NSString\"8@\"_PASTuple2\"16^B24"
+ "v32@?0@\"NSString\"8@16^B24"
+ "v40@0:8Q16@\"NSArray\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8Q16@24@?32"
+ "v48@0:8Q16@24@32@?40"
+ "v56@0:8Q16Q24Q32@40@?48"
+ "widgetClient"
+ "widgetGridSize"
+ "widgetSuggestionsEnabled"
+ "widgetsBySortingAndFilteringWidgetsUsingPersonalizedGalleryAlgorithm:rankerPlistType:regularlyUsedThreshold:limit:"
+ "zkwPredictionsForRequest:error:"
+ "zkwPredictionsForRequest:usingPredictionManager:"
- "!(intent && activityString)"
- "!intent && !activityString"
- "%s: New first time CarPlay connection. Returning default OnBoarding suggestions"
- "%s: No OnBoarding suggestions available, returning nil"
- "%s: generated CarPlay smart stacks were nil"
- "%s: generated CarPlay smart stacks. Stack1: %tu widgets, stack2: %tu widgets"
- "(startDate > %@ AND startDate < %@) OR (endDate > %@ AND endDate < %@)"
- "-[ATXClientDuetHelper _queryDuetStreamUnbatched:startDate:endDate:otherPredicates:limit:]"
- "-[ATXDefaultHomeScreenItemManager _generateSmartStackForCarPlayWithDescriptorCache]"
- "-[ATXDefaultHomeScreenItemManager _generateSmartStacksForCarPlay]"
- "-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:completionHandler:]"
- "-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:completionHandler:]_block_invoke"
- "-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:completionHandler:]_block_invoke_2"
- "-[ATXDefaultHomeScreenItemUpdater _updateCarPlayDefaultsOnQueueWithReason:appLaunchCounts:]"
- "?"
- "@\"<ATXSpotlightClientDelegate>\""
- "@\"<_DKKnowledgeSaving>\""
- "@\"_DKEventStream\""
- "@156@0:8@16@24@32@40@48@56@64@72Q80@88@96@104B112@116@124@132@140@148"
- "@56@0:8@16@24@32@40Q48"
- "@64@0:8q16@24@32@40@48Q56"
- "@84@0:8@16i24@28@36@44@52@60@68@76"
- "@84@0:8d16i24@28@36@44@52@60@68@76"
- "ATXAppDirectoryCategory archive contains a nil or missing list of apps"
- "ATXAppDirectoryCategory archive contains unexpected class contents"
- "ATXAppDirectoryClient: Failed to retrieve knowledge store, bailing"
- "ATXAppDirectoryClient: Failed to retrieve knowledge stream, bailing"
- "ATXAppDirectoryClient: Read suggestion layout from cache"
- "ATXAppDirectoryClient: Recent apps deduplication failed with error: %@"
- "ATXAppDirectoryClient: Starting to process recent apps"
- "ATXAppDirectoryClient: log to duet failed, error: %@"
- "ATXClientDuetHelper"
- "ATXClientDuetHelper.m"
- "ATXDefaultHomeScreenItemUpdater: %s error fetching CarPlay config: %@"
- "ATXSFL: didPerformCommand ---> %@"
- "ATXSpotlightClient: _resultWithActionSuggestion action %@ has no intent nor user activity"
- "Blending providing suggestions to ATXConsumerSubTypeActionSettings inside ATXActionPredictionClient..."
- "Blending providing suggestions to ATXConsumerSubTypeActionSpotlightUnknown inside ATXActionPredictionClient..."
- "Donation Processing (Link) - Action not predictable"
- "Duet query: %{public}@, %s, %@"
- "Error querying Duet: %@"
- "Error unarchiving intent: %@"
- "Nil activityType for NSUserActivity: %@"
- "Nil or empty title attached to event of activityType: %@ -- filtering out"
- "Nil or empty title attached to intent event -- filtering out"
- "Nil requiredString for bundleId: %@"
- "No bundleId for intent: %@, intentType: %@, intentSource: %lld"
- "No bundleId found for eventUUID: %@"
- "T@\"<ATXSpotlightClientDelegate>\",W,N,V_delegate"
- "T@\"NSArray\",R,N,V_appBundleIDs"
- "T@\"NSArray\",R,N,V_predictedApps"
- "T@\"NSArray\",R,N,V_recentApps"
- "_appBundleIDs"
- "_descriptionForTopic:"
- "_descriptorsByFilteringDescriptors:variant:fromAppsDisabledOnHomeScreen:"
- "_enumerateBatchesInDuetStream:startDate:endDate:otherPredicates:limit:block:"
- "_generateSmartStackForCarPlayWithDescriptorCache"
- "_generateSmartStacksForCarPlay"
- "_getIntentEventForSource:startDate:endDate:otherPredicates:bundleIdFilter:limit:"
- "_knowledgeStore"
- "_knowledgeStream"
- "_logToDuet:metadata:"
- "_predictedApps"
- "_queryDuetStream:startDate:endDate:otherPredicates:limit:"
- "_queryDuetStreamUnbatched:startDate:endDate:otherPredicates:limit:"
- "_recentApps"
- "_responseWithSpotlightLayout:andSpotlightRecentTopics:"
- "andPredicateWithSubpredicates:"
- "appActivityStream"
- "appDirectoryInteractionStream"
- "appIntentsStream"
- "categoryWithInteger:type:"
- "com.apple.duet.appDirectory"
- "eventQueryWithPredicate:eventStreams:offset:limit:sortDescriptors:"
- "eventStreams"
- "eventWithStream:startDate:endDate:value:metadata:"
- "executeQuery:error:"
- "getActivityAndIntentEventsBetweenStartDate:endDate:ascending:"
- "getActivityAndIntentEventsFromLastMonth"
- "getActivityEventsBetweenStartDate:endDate:"
- "getActivityEventsBetweenStartDate:endDate:bundleIdFilter:"
- "getIntentEventsBetweenStartDate:endDate:"
- "getIntentEventsBetweenStartDate:endDate:bundleIdFilter:forSource:"
- "getSortedActivityAndIntentEventsBetweenStartDate:endDate:bundleIdFilter:comparator:"
- "initWithAbsoluteDate:eventType:appConsumerSubType:actionConsumerSubType:appBlendingCacheId:actionBlendingCacheId:appSuggestionIds:actionSuggestionIds:metadata:"
- "initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:"
- "initWithDate:eventType:appConsumerSubType:actionConsumerSubType:appBlendingCacheId:actionBlendingCacheId:appSuggestionIds:actionSuggestionIds:metadata:"
- "initWithQueryString:context:"
- "initWithSuggestionLayout:recentApps:hiddenApps:otherAppsOnScreen:numAppsToPredict:error:"
- "intent || activityString || userActivityProxy"
- "intentHandlingStatus"
- "isActionEligibleForSettingsSuggestionsWithBundleIdentifier:actionIdentifier:"
- "knowledgeStore"
- "limit > 0"
- "predicateForObjectsWithMetadataKey:andIntegerValue:"
- "recent apps"
- "saveObjects:responseQueue:withCompletion:"
- "searchPredicate"
- "serializedInteraction"
- "source-bundleId"
- "v64@0:8@16@24@32@40Q48@?56"
- "widgetsBySortingAndFilteringWidgetsUsingPersonalizedGalleryAlgorithm:rankerPlistType:regularlyUsedThreshold:"

```
