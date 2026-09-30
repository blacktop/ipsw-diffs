## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient`

```diff

-619.1.0.2.0
-  __TEXT.__text: 0x18d3bc
+619.5.1.0.0
+  __TEXT.__text: 0x19006c
   __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_methlist: 0x18aac
+  __TEXT.__objc_methlist: 0x18cf4
   __TEXT.__const: 0x6f8
-  __TEXT.__cstring: 0x1ba94
-  __TEXT.__oslogstring: 0x17944
-  __TEXT.__gcc_except_tab: 0x2314
+  __TEXT.__cstring: 0x1bba8
+  __TEXT.__oslogstring: 0x17a08
+  __TEXT.__gcc_except_tab: 0x232c
   __TEXT.__dlopen_cstrs: 0x42d
   __TEXT.__ustring: 0x18a
-  __TEXT.__unwind_info: 0x66c0
-  __TEXT.__objc_classname: 0x3bc8
-  __TEXT.__objc_methname: 0x341f1
-  __TEXT.__objc_methtype: 0x675c
-  __TEXT.__objc_stubs: 0x1cb60
-  __DATA_CONST.__got: 0x16e8
-  __DATA_CONST.__const: 0x62f0
+  __TEXT.__unwind_info: 0x6718
+  __TEXT.__objc_classname: 0x3bce
+  __TEXT.__objc_methname: 0x34671
+  __TEXT.__objc_methtype: 0x6782
+  __TEXT.__objc_stubs: 0x1cd80
+  __DATA_CONST.__got: 0x1710
+  __DATA_CONST.__const: 0x6388
   __DATA_CONST.__objc_classlist: 0xe40
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9ed0
+  __DATA_CONST.__objc_selrefs: 0x9fb0
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0xc48
   __DATA_CONST.__objc_arraydata: 0xaf8
   __AUTH_CONST.__auth_got: 0x790
   __AUTH_CONST.__const: 0x2a80
-  __AUTH_CONST.__cfstring: 0x151c0
-  __AUTH_CONST.__objc_const: 0x45c88
+  __AUTH_CONST.__cfstring: 0x15280
+  __AUTH_CONST.__objc_const: 0x45e68
   __AUTH_CONST.__objc_intobj: 0xa20
   __AUTH_CONST.__objc_arrayobj: 0x6d8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH.__objc_data: 0x4330
-  __DATA.__objc_ivar: 0x1c5c
+  __DATA.__objc_ivar: 0x1c6c
   __DATA.__data: 0x1cf0
   __DATA.__bss: 0x390
   __DATA_DIRTY.__objc_data: 0x4b50

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: EC592A56-774F-318E-AD3A-100DA634B7AE
-  Functions: 10663
-  Symbols:   35082
-  CStrings:  16021
+  UUID: 43701F98-273D-302F-BB4E-89E8AAB9EA8C
+  Functions: 10717
+  Symbols:   35245
+  CStrings:  16076
 
Symbols:
+ +[ATXDefaultHomeScreenItemManager _descriptorsByFilteringDescriptors:disabledApps:excludedWidgetsWithIdentifiers:client:personaIdentifier:]
+ +[ATXDefaultHomeScreenItemProducerUtilities mergedDescriptorsFrom:withAdditional:]
+ -[ATXBackgroundSystemTask _didDeferForTestMode]
+ -[ATXBackgroundSystemTask _setDoneForTestMode]
+ -[ATXBackgroundSystemTask _setProgressUnitsForTestMode:]
+ -[ATXBackgroundSystemTask configuration]
+ -[ATXBackgroundSystemTask identifier]
+ -[ATXBackgroundSystemTask initForTestingWithIdentifier:configuration:]
+ -[ATXBackgroundSystemTask jobCreationTime]
+ -[ATXBackgroundSystemTask resultStatusForJob]
+ -[ATXBackgroundSystemTask resultStatus]
+ -[ATXBackgroundSystemTask setConfiguration:]
+ -[ATXBackgroundSystemTask setIdentifier:]
+ -[ATXBackgroundSystemTask setJobCreationTime:]
+ -[ATXBackgroundSystemTask setResultStatus:]
+ -[ATXDefaultHomeScreenItemManager _generateSmartStackWithDescriptorCacheFromRequest:error:]
+ -[ATXDefaultHomeScreenItemManager _generateSmartStackWithDescriptorCacheFromRequest:error:].cold.1
+ -[ATXDefaultHomeScreenItemManager _generateSmartStacksWithRequest:error:]
+ -[ATXDefaultHomeScreenItemManager generateItemsForWidgetGalleryWithRequest:error:]
+ -[ATXDefaultHomeScreenItemManager generateItemsForWidgetGalleryWithRequest:error:].cold.1
+ -[ATXDefaultHomeScreenItemManager generateItemsForWidgetGalleryWithRequest:error:].cold.2
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer generatedStacksWithRequest:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer initWithCandidateWidgets:cachedWidgetPersonalityToAppScore:personalityToDescriptorDictionary:adblDrainClassification:isiPad:isDayZeroExperience:shouldIncludeContactsWidget:cachedHasiCloudFamily:appLaunchCounts:isAmbient:]
+ -[ATXDefaultHomeScreenItemProducer generatedStacksWithRequest:]
+ -[ATXFakeModeEntityScorer rankedAppsForMode:options:]
+ -[ATXFakeModeEntityScorer rankedAppsForMode:options:reply:]
+ -[ATXFakeModeEntityScorer rankedContactsForMode:options:reply:]
+ -[ATXFakeModeEntityScorer rankedNotificationsForMode:options:]
+ -[ATXFakeModeEntityScorer rankedNotificationsForMode:options:reply:]
+ -[ATXFakeNotificationSettingsReader areHighlightsEnabled]
+ -[ATXFakeNotificationSettingsReader areSummariesEnabled]
+ -[ATXHomeScreenConfigCache _filePathForHomeScreenPageConfigWithClientIdentifier:]
+ -[ATXHomeScreenConfigCache loadHomeScreenAndTodayPageConfigurationsIncludingHidden:forClientWithIdentifier:error:]
+ -[ATXHomeScreenConfigCache loadHomeScreenAndTodayPageConfigurationsIncludingHidden:forClientWithIdentifier:error:].cold.1
+ -[ATXHomeScreenConfigCache loadHomeScreenPageConfigurationsIncludingHidden:forClientWithIdentifier:error:]
+ -[ATXHomeScreenConfigCache writeHomeScreenPageConfigurations:forClientWithIdentifier:error:]
+ -[ATXHomeScreenConfigCache writeHomeScreenPageConfigurations:forClientWithIdentifier:error:].cold.1
+ -[ATXHomeScreenSuggestionClient _writeHomeScreenPageConfigurations:forClientWithIdentifier:guardedData:completionHandler:]
+ -[ATXHomeScreenSuggestionClient _writeHomeScreenPageConfigurations:forClientWithIdentifier:guardedData:completionHandler:].cold.1
+ -[ATXHomeScreenSuggestionClient loadHomeScreenPageConfigurationsForClientWithIdentifier:completionHandler:]
+ -[ATXHomeScreenSuggestionClient setActivePersonaWithClientIdentifier:]
+ -[ATXHomeScreenSuggestionClient writeHomeScreenPageConfigurations:forClientWithIdentifier:completionHandler:]
+ -[ATXModeEntityScorer rankedAppsForMode:options:]
+ -[ATXModeEntityScorer rankedAppsForMode:options:reply:]
+ -[ATXModeEntityScorer rankedContactsForMode:options:reply:]
+ -[ATXModeEntityScorer rankedNotificationsForMode:options:]
+ -[ATXModeEntityScorer rankedNotificationsForMode:options:reply:]
+ -[ATXModeEntityScorerClient rankedAppsForMode:options:reply:]
+ -[ATXModeEntityScorerClient rankedAppsForMode:options:reply:].cold.1
+ -[ATXModeEntityScorerClient rankedAppsForMode:options:reply:].cold.2
+ -[ATXModeEntityScorerClient rankedContactsForMode:options:reply:]
+ -[ATXModeEntityScorerClient rankedContactsForMode:options:reply:].cold.1
+ -[ATXModeEntityScorerClient rankedContactsForMode:options:reply:].cold.2
+ -[ATXModeEntityScorerClient rankedNotificationsForMode:options:reply:]
+ -[ATXModeEntityScorerClient rankedNotificationsForMode:options:reply:].cold.1
+ -[ATXModeEntityScorerClient rankedNotificationsForMode:options:reply:].cold.2
+ -[ATXNotificationSettingsReader areHighlightsEnabled]
+ -[ATXNotificationSettingsReader areSummariesEnabled]
+ -[ATXWidgetClientIdentity description]
+ -[ATXWidgetClientIdentity stringForWidgetClient]
+ -[ATXWidgetSmartStackRequest setStackLayoutSize:]
+ -[ATXWidgetSmartStackRequest stackLayoutSize]
+ GCC_except_table206
+ GCC_except_table209
+ GCC_except_table81
+ OBJC_IVAR_$_ATXHomeScreenSuggestionClientGuardedData.clientIdentifier
+ _ATXBGSTDeferAfterSecondsKey
+ _ATXBGSTStatusDeferKey
+ _ATXBGSTStatusDoneKey
+ _ATXBGSTStatusRanForSecondsKey
+ _OBJC_CLASS_$_ATXGlobalStateForTesting
+ _OBJC_IVAR_$_ATXBackgroundSystemTask._configuration
+ _OBJC_IVAR_$_ATXBackgroundSystemTask._identifier
+ _OBJC_IVAR_$_ATXBackgroundSystemTask._jobCreationTime
+ _OBJC_IVAR_$_ATXBackgroundSystemTask._resultStatus
+ _OBJC_IVAR_$_ATXWidgetSmartStackRequest._stackLayoutSize
+ ___106-[ATXHomeScreenConfigCache loadHomeScreenPageConfigurationsIncludingHidden:forClientWithIdentifier:error:]_block_invoke
+ ___107-[ATXHomeScreenSuggestionClient loadHomeScreenPageConfigurationsForClientWithIdentifier:completionHandler:]_block_invoke
+ ___109-[ATXHomeScreenSuggestionClient writeHomeScreenPageConfigurations:forClientWithIdentifier:completionHandler:]_block_invoke
+ ___112-[ATXModeEntityScorer assignModeEntityScores:entityTypeIdentifier:entityIdentifier:score:modeConfigurationType:]_block_invoke.31
+ ___112-[ATXModeEntityScorer assignModeEntityScores:entityTypeIdentifier:entityIdentifier:score:modeConfigurationType:]_block_invoke.31.cold.1
+ ___113-[ATXModeEntityScorer modeEntityScoresFromCacheForModeEntityTypeIdentifier:modeIdentifier:modeConfigurationType:]_block_invoke.28
+ ___113-[ATXModeEntityScorer modeEntityScoresFromCacheForModeEntityTypeIdentifier:modeIdentifier:modeConfigurationType:]_block_invoke.28.cold.1
+ ___122-[ATXHomeScreenSuggestionClient _writeHomeScreenPageConfigurations:forClientWithIdentifier:guardedData:completionHandler:]_block_invoke
+ ___124-[ATXModeEntityScorerClient assignModeEntityScores:entityTypeIdentifier:entityIdentifier:score:modeConfigurationType:reply:]_block_invoke.109
+ ___125-[ATXModeEntityScorerClient modeEntityScoresFromCacheForModeEntityTypeIdentifier:modeIdentifier:modeConfigurationType:reply:]_block_invoke.107
+ ___139+[ATXDefaultHomeScreenItemManager _descriptorsByFilteringDescriptors:disabledApps:excludedWidgetsWithIdentifiers:client:personaIdentifier:]_block_invoke
+ ___139+[ATXDefaultHomeScreenItemManager _descriptorsByFilteringDescriptors:disabledApps:excludedWidgetsWithIdentifiers:client:personaIdentifier:]_block_invoke.cold.1
+ ___139+[ATXDefaultHomeScreenItemManager _descriptorsByFilteringDescriptors:disabledApps:excludedWidgetsWithIdentifiers:client:personaIdentifier:]_block_invoke.cold.2
+ ___139+[ATXDefaultHomeScreenItemManager _descriptorsByFilteringDescriptors:disabledApps:excludedWidgetsWithIdentifiers:client:personaIdentifier:]_block_invoke.cold.3
+ ___201-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:]_block_invoke
+ ___201-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:chronoServicesProvider:store:logger:]_block_invoke.90
+ ___201-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:chronoServicesProvider:store:logger:]_block_invoke.90.cold.1
+ ___201-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:chronoServicesProvider:store:logger:]_block_invoke.94
+ ___201-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:chronoServicesProvider:store:logger:]_block_invoke.94.cold.1
+ ___201-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:chronoServicesProvider:store:logger:]_block_invoke_2.91
+ ___201-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:chronoServicesProvider:store:logger:]_block_invoke_2.91.cold.1
+ ___202-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedAmbientOnboardingStacksForSize:stack1RequiredWidgetPersonalities:stack2RequiredWidgetPersonalities:rankedWidgets:usedWidgetPersonalities:]_block_invoke.116
+ ___248-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedOnboardingStackForSize:requiredWidgetPersonalities:conditionalWidgetPersonalities:fallbackWidgetPersonalities:rankedThirdPartyWidgets:usedWidgetPersonalities:shouldAdd3PWidgetToStack:]_block_invoke.128
+ ___33-[ATXModeEntityScorerClient init]_block_invoke.69
+ ___47-[ATXModeEntityScorer scoreNotifications:mode:]_block_invoke.21
+ ___47-[ATXModeEntityScorer scoreNotifications:mode:]_block_invoke.21.cold.1
+ ___49-[ATXModeEntityScorer rankedAppsForMode:options:]_block_invoke
+ ___49-[ATXModeEntityScorer rankedAppsForMode:options:]_block_invoke.19
+ ___49-[ATXModeEntityScorer rankedAppsForMode:options:]_block_invoke.19.cold.1
+ ___49-[ATXModeEntityScorer rankedAppsForMode:options:]_block_invoke_2
+ ___49-[ATXModeEntityScorer scoreAppsForDenyList:mode:]_block_invoke.42
+ ___49-[ATXModeEntityScorer scoreAppsForDenyList:mode:]_block_invoke.42.cold.1
+ ___50-[ATXModeEntityScorerClient scoreApps:mode:reply:]_block_invoke.88
+ ___51-[ATXModeEntityScorer scoreUserNotifications:mode:]_block_invoke.20
+ ___51-[ATXModeEntityScorer scoreUserNotifications:mode:]_block_invoke.20.cold.1
+ ___52-[ATXModeEntityScorer rankedAppsForDenyListForMode:]_block_invoke.43
+ ___52-[ATXModeEntityScorer rankedAppsForDenyListForMode:]_block_invoke.43.cold.1
+ ___53-[ATXModeEntityScorer scoreContactsForDenyList:mode:]_block_invoke.44
+ ___53-[ATXModeEntityScorer scoreContactsForDenyList:mode:]_block_invoke.44.cold.1
+ ___53-[ATXModeEntityScorerClient rankedAppsForMode:reply:]_block_invoke.89
+ ___54-[ATXModeEntityScorerClient scoreContacts:mode:reply:]_block_invoke.84
+ ___55-[ATXModeEntityScorer rankedAppsForMode:options:reply:]_block_invoke
+ ___55-[ATXModeEntityScorer rankedAppsForMode:options:reply:]_block_invoke.cold.1
+ ___56-[ATXModeEntityScorerClient rankedWidgetsForMode:reply:]_block_invoke.91
+ ___57-[ATXModeEntityScorer rankedAppsForNotificationsForMode:]_block_invoke.24
+ ___57-[ATXModeEntityScorer rankedAppsForNotificationsForMode:]_block_invoke.24.cold.1
+ ___57-[ATXModeEntityScorerClient rankedContactsForMode:reply:]_block_invoke.86
+ ___58-[ATXModeEntityScorer rankedNotificationsForMode:options:]_block_invoke
+ ___58-[ATXModeEntityScorer rankedNotificationsForMode:options:]_block_invoke.22
+ ___58-[ATXModeEntityScorer rankedNotificationsForMode:options:]_block_invoke.23
+ ___58-[ATXModeEntityScorer rankedNotificationsForMode:options:]_block_invoke.23.cold.1
+ ___58-[ATXModeEntityScorer rankedNotificationsForMode:options:]_block_invoke.cold.1
+ ___59-[ATXModeEntityScorer rankedContactsForMode:options:reply:]_block_invoke
+ ___59-[ATXModeEntityScorer rankedContactsForMode:options:reply:]_block_invoke.cold.1
+ ___59-[ATXModeEntityScorerClient scoreNotifications:mode:reply:]_block_invoke.92
+ ___61-[ATXModeEntityScorer rankedContactsForNotificationsForMode:]_block_invoke.25
+ ___61-[ATXModeEntityScorer rankedContactsForNotificationsForMode:]_block_invoke.25.cold.1
+ ___61-[ATXModeEntityScorerClient rankedAppsForMode:options:reply:]_block_invoke
+ ___61-[ATXModeEntityScorerClient rankedAppsForMode:options:reply:]_block_invoke.90
+ ___61-[ATXModeEntityScorerClient rankedAppsForMode:options:reply:]_block_invoke.cold.1
+ ___61-[ATXModeEntityScorerClient scoreAppsForDenyList:mode:reply:]_block_invoke.100
+ ___62-[ATXModeEntityScorerClient rankedNotificationsForMode:reply:]_block_invoke.93
+ ___64-[ATXModeEntityScorer rankedContactsForDenyListForMode:options:]_block_invoke.45
+ ___64-[ATXModeEntityScorer rankedContactsForDenyListForMode:options:]_block_invoke.45.cold.1
+ ___64-[ATXModeEntityScorer rankedNotificationsForMode:options:reply:]_block_invoke
+ ___64-[ATXModeEntityScorer rankedNotificationsForMode:options:reply:]_block_invoke.cold.1
+ ___64-[ATXModeEntityScorerClient rankedAppsForDenyListForMode:reply:]_block_invoke.101
+ ___65-[ATXModeEntityScorerClient rankedContactsForMode:options:reply:]_block_invoke
+ ___65-[ATXModeEntityScorerClient rankedContactsForMode:options:reply:]_block_invoke.87
+ ___65-[ATXModeEntityScorerClient rankedContactsForMode:options:reply:]_block_invoke.cold.1
+ ___65-[ATXModeEntityScorerClient scoreContactsForDenyList:mode:reply:]_block_invoke.105
+ ___68-[ATXHomeScreenSuggestionClient listener:shouldAcceptNewConnection:]_block_invoke.173
+ ___69-[ATXModeEntityScorerClient rankedAppsForNotificationsForMode:reply:]_block_invoke.95
+ ___70-[ATXModeEntityScorerClient rankedNotificationsForMode:options:reply:]_block_invoke
+ ___70-[ATXModeEntityScorerClient rankedNotificationsForMode:options:reply:]_block_invoke.94
+ ___70-[ATXModeEntityScorerClient rankedNotificationsForMode:options:reply:]_block_invoke.cold.1
+ ___73-[ATXModeEntityScorerClient rankedContactsForNotificationsForMode:reply:]_block_invoke.96
+ ___76-[ATXModeEntityScorerClient rankedContactsForDenyListForMode:options:reply:]_block_invoke.106
+ ___79-[ATXDefaultHomeScreenItemOnboardingStacksProducer generatedStacksWithRequest:]_block_invoke
+ ___79-[ATXDefaultHomeScreenItemOnboardingStacksProducer generatedStacksWithRequest:]_block_invoke.94
+ ___79-[ATXDefaultHomeScreenItemOnboardingStacksProducer generatedStacksWithRequest:]_block_invoke.99
+ ___85-[ATXDefaultHomeScreenItemOnboardingStacksProducer hasConfiguredHomeAccessoryControl]_block_invoke.150
+ ___85-[ATXDefaultHomeScreenItemOnboardingStacksProducer hasConfiguredHomeAccessoryControl]_block_invoke.150.cold.1
+ ___86-[ATXDefaultHomeScreenItemManager fetchWidgetSmartStackWithRequest:completionHandler:]_block_invoke.66
+ ___86-[ATXDefaultHomeScreenItemManager fetchWidgetSmartStackWithRequest:completionHandler:]_block_invoke.70
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.76
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.76.cold.1
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.76.cold.2
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.76.cold.3
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.76.cold.4
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.81
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.86
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.90
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke_2.88
+ ___block_descriptor_56_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56s_e29_B16?0"CHSWidgetDescriptor"8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.109
+ ___block_literal_global.115
+ ___block_literal_global.127
+ ___block_literal_global.149
+ ___block_literal_global.160
+ ___block_literal_global.172
+ ___block_literal_global.175
+ ___block_literal_global.182
+ ___block_literal_global.194
+ ___block_literal_global.196
+ ___block_literal_global.198
+ ___block_literal_global.69
+ ___block_literal_global.93
+ ___kCFBooleanFalse
+ _objc_msgSend$_descriptorsByFilteringDescriptors:disabledApps:excludedWidgetsWithIdentifiers:client:personaIdentifier:
+ _objc_msgSend$_didDeferForTestMode
+ _objc_msgSend$_filePathForHomeScreenPageConfigWithClientIdentifier:
+ _objc_msgSend$_generateSmartStackWithDescriptorCacheFromRequest:error:
+ _objc_msgSend$_generateSmartStacksWithRequest:error:
+ _objc_msgSend$_personalizedStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:
+ _objc_msgSend$_setDoneForTestMode
+ _objc_msgSend$_setProgressUnitsForTestMode:
+ _objc_msgSend$_writeHomeScreenPageConfigurations:forClientWithIdentifier:guardedData:completionHandler:
+ _objc_msgSend$effectiveContainerBundleIdentifier
+ _objc_msgSend$generateItemsForWidgetGalleryWithRequest:error:
+ _objc_msgSend$generatedStacksWithRequest:
+ _objc_msgSend$initWithCandidateWidgets:cachedWidgetPersonalityToAppScore:personalityToDescriptorDictionary:adblDrainClassification:isiPad:isDayZeroExperience:shouldIncludeContactsWidget:cachedHasiCloudFamily:appLaunchCounts:isAmbient:
+ _objc_msgSend$isTestModeEnabled
+ _objc_msgSend$jobCreationTime
+ _objc_msgSend$loadHomeScreenAndTodayPageConfigurationsIncludingHidden:forClientWithIdentifier:error:
+ _objc_msgSend$loadHomeScreenPageConfigurationsIncludingHidden:forClientWithIdentifier:error:
+ _objc_msgSend$mergedDescriptorsFrom:withAdditional:
+ _objc_msgSend$prioritizationSetting
+ _objc_msgSend$rankedAppsForMode:options:reply:
+ _objc_msgSend$rankedContactsForMode:options:reply:
+ _objc_msgSend$rankedNotificationsForMode:options:
+ _objc_msgSend$rankedNotificationsForMode:options:reply:
+ _objc_msgSend$resolvedAction
+ _objc_msgSend$resultStatus
+ _objc_msgSend$setConfiguration:
+ _objc_msgSend$setJobCreationTime:
+ _objc_msgSend$setResultStatus:
+ _objc_msgSend$stringForWidgetClient
+ _objc_msgSend$summarizationSetting
+ _objc_msgSend$writeHomeScreenPageConfigurations:forClientWithIdentifier:error:
- +[ATXDefaultHomeScreenItemManager isCHSWidgetDescriptorAllowedForCarPlay:disabledApps:excludedWidgetsWithIdentifiers:]
- -[ATXDefaultHomeScreenItemManager _generateSmartStackForCarPlayWithDescriptorCacheFromRequest:error:]
- -[ATXDefaultHomeScreenItemManager _generateSmartStackForCarPlayWithDescriptorCacheFromRequest:error:].cold.1
- -[ATXDefaultHomeScreenItemManager _generateSmartStacksForCarPlayWithRequest:error:]
- -[ATXDefaultHomeScreenItemManager galleryItemsForCarPlayWithRequest:error:]
- -[ATXDefaultHomeScreenItemManager galleryItemsForCarPlayWithRequest:error:].cold.1
- -[ATXDefaultHomeScreenItemManager galleryItemsForCarPlayWithRequest:error:].cold.2
- -[ATXDefaultHomeScreenItemOnboardingStacksProducer _carPlayOnboardingStacks]
- -[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedCarPlayOnboardingStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:]
- -[ATXDefaultHomeScreenItemOnboardingStacksProducer initWithCandidateWidgets:cachedWidgetPersonalityToAppScore:personalityToDescriptorDictionary:adblDrainClassification:isiPad:isDayZeroExperience:shouldIncludeContactsWidget:cachedHasiCloudFamily:appLaunchCounts:isAmbient:isCarPlay:]
- -[ATXDefaultHomeScreenItemOnboardingStacksProducer isCarPlay]
- -[ATXDefaultHomeScreenItemOnboardingStacksProducer setSmartStackRequest:]
- -[ATXDefaultHomeScreenItemOnboardingStacksProducer smartStackRequest]
- -[ATXDefaultHomeScreenItemProducer carPlayOnboardingStacks]
- -[ATXHomeScreenConfigCache _filePathForHomeScreenPageConfig]
- -[ATXHomeScreenConfigCache loadHomeScreenAndTodayPageConfigurationsIncludingHidden:error:].cold.1
- -[ATXHomeScreenConfigCache writeHomeScreenPageConfigurations:error:].cold.1
- -[ATXHomeScreenSuggestionClient _writeHomeScreenPageConfigurations:guardedData:completionHandler:]
- -[ATXHomeScreenSuggestionClient _writeHomeScreenPageConfigurations:guardedData:completionHandler:].cold.1
- GCC_except_table202
- GCC_except_table205
- GCC_except_table32
- GCC_except_table36
- GCC_except_table70
- GCC_except_table83
- _OBJC_IVAR_$_ATXDefaultHomeScreenItemOnboardingStacksProducer._isCarPlay
- _OBJC_IVAR_$_ATXDefaultHomeScreenItemOnboardingStacksProducer._smartStackRequest
- ___101-[ATXDefaultHomeScreenItemManager _generateSmartStackForCarPlayWithDescriptorCacheFromRequest:error:]_block_invoke
- ___112-[ATXModeEntityScorer assignModeEntityScores:entityTypeIdentifier:entityIdentifier:score:modeConfigurationType:]_block_invoke.29
- ___112-[ATXModeEntityScorer assignModeEntityScores:entityTypeIdentifier:entityIdentifier:score:modeConfigurationType:]_block_invoke.30.cold.1
- ___113-[ATXModeEntityScorer modeEntityScoresFromCacheForModeEntityTypeIdentifier:modeIdentifier:modeConfigurationType:]_block_invoke.26
- ___113-[ATXModeEntityScorer modeEntityScoresFromCacheForModeEntityTypeIdentifier:modeIdentifier:modeConfigurationType:]_block_invoke.27.cold.1
- ___124-[ATXModeEntityScorerClient assignModeEntityScores:entityTypeIdentifier:entityIdentifier:score:modeConfigurationType:reply:]_block_invoke.100
- ___125-[ATXModeEntityScorerClient modeEntityScoresFromCacheForModeEntityTypeIdentifier:modeIdentifier:modeConfigurationType:reply:]_block_invoke.98
- ___201-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:chronoServicesProvider:store:logger:]_block_invoke.89
- ___201-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:chronoServicesProvider:store:logger:]_block_invoke.89.cold.1
- ___201-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:chronoServicesProvider:store:logger:]_block_invoke.92
- ___201-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:chronoServicesProvider:store:logger:]_block_invoke.92.cold.1
- ___201-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:chronoServicesProvider:store:logger:]_block_invoke_2.90
- ___201-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:chronoServicesProvider:store:logger:]_block_invoke_2.90.cold.1
- ___202-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedAmbientOnboardingStacksForSize:stack1RequiredWidgetPersonalities:stack2RequiredWidgetPersonalities:rankedWidgets:usedWidgetPersonalities:]_block_invoke.112
- ___218-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedCarPlayOnboardingStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:]_block_invoke
- ___248-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedOnboardingStackForSize:requiredWidgetPersonalities:conditionalWidgetPersonalities:fallbackWidgetPersonalities:rankedThirdPartyWidgets:usedWidgetPersonalities:shouldAdd3PWidgetToStack:]_block_invoke.124
- ___33-[ATXModeEntityScorerClient init]_block_invoke.63
- ___47-[ATXModeEntityScorer scoreNotifications:mode:]_block_invoke.20
- ___47-[ATXModeEntityScorer scoreNotifications:mode:]_block_invoke.20.cold.1
- ___49-[ATXModeEntityScorer scoreAppsForDenyList:mode:]_block_invoke.41
- ___49-[ATXModeEntityScorer scoreAppsForDenyList:mode:]_block_invoke.41.cold.1
- ___50-[ATXModeEntityScorer rankedNotificationsForMode:]_block_invoke
- ___50-[ATXModeEntityScorer rankedNotificationsForMode:]_block_invoke.21
- ___50-[ATXModeEntityScorer rankedNotificationsForMode:]_block_invoke.22
- ___50-[ATXModeEntityScorer rankedNotificationsForMode:]_block_invoke.22.cold.1
- ___50-[ATXModeEntityScorer rankedNotificationsForMode:]_block_invoke.cold.1
- ___50-[ATXModeEntityScorerClient scoreApps:mode:reply:]_block_invoke.81
- ___51-[ATXModeEntityScorer scoreUserNotifications:mode:]_block_invoke.19
- ___51-[ATXModeEntityScorer scoreUserNotifications:mode:]_block_invoke.19.cold.1
- ___52-[ATXModeEntityScorer rankedAppsForDenyListForMode:]_block_invoke.42
- ___52-[ATXModeEntityScorer rankedAppsForDenyListForMode:]_block_invoke.42.cold.1
- ___53-[ATXModeEntityScorer scoreContactsForDenyList:mode:]_block_invoke.43
- ___53-[ATXModeEntityScorer scoreContactsForDenyList:mode:]_block_invoke.43.cold.1
- ___53-[ATXModeEntityScorerClient rankedAppsForMode:reply:]_block_invoke.82
- ___54-[ATXModeEntityScorerClient scoreContacts:mode:reply:]_block_invoke.78
- ___56-[ATXModeEntityScorerClient rankedWidgetsForMode:reply:]_block_invoke.83
- ___57-[ATXModeEntityScorer rankedAppsForNotificationsForMode:]_block_invoke.23
- ___57-[ATXModeEntityScorer rankedAppsForNotificationsForMode:]_block_invoke.23.cold.1
- ___57-[ATXModeEntityScorerClient rankedContactsForMode:reply:]_block_invoke.80
- ___59-[ATXModeEntityScorerClient scoreNotifications:mode:reply:]_block_invoke.84
- ___61-[ATXModeEntityScorer rankedContactsForNotificationsForMode:]_block_invoke.24
- ___61-[ATXModeEntityScorer rankedContactsForNotificationsForMode:]_block_invoke.24.cold.1
- ___61-[ATXModeEntityScorerClient scoreAppsForDenyList:mode:reply:]_block_invoke.91
- ___62-[ATXModeEntityScorerClient rankedNotificationsForMode:reply:]_block_invoke.85
- ___64-[ATXModeEntityScorer rankedContactsForDenyListForMode:options:]_block_invoke.44
- ___64-[ATXModeEntityScorer rankedContactsForDenyListForMode:options:]_block_invoke.44.cold.1
- ___64-[ATXModeEntityScorerClient rankedAppsForDenyListForMode:reply:]_block_invoke.92
- ___65-[ATXModeEntityScorerClient scoreContactsForDenyList:mode:reply:]_block_invoke.96
- ___68-[ATXHomeScreenSuggestionClient listener:shouldAcceptNewConnection:]_block_invoke.172
- ___69-[ATXModeEntityScorerClient rankedAppsForNotificationsForMode:reply:]_block_invoke.86
- ___73-[ATXModeEntityScorerClient rankedContactsForNotificationsForMode:reply:]_block_invoke.87
- ___75-[ATXDefaultHomeScreenItemManager galleryItemsForCarPlayWithRequest:error:]_block_invoke
- ___76-[ATXDefaultHomeScreenItemOnboardingStacksProducer _carPlayOnboardingStacks]_block_invoke
- ___76-[ATXDefaultHomeScreenItemOnboardingStacksProducer _carPlayOnboardingStacks]_block_invoke.91
- ___76-[ATXDefaultHomeScreenItemOnboardingStacksProducer _carPlayOnboardingStacks]_block_invoke.96
- ___76-[ATXModeEntityScorerClient rankedContactsForDenyListForMode:options:reply:]_block_invoke.97
- ___82-[ATXHomeScreenConfigCache loadHomeScreenPageConfigurationsIncludingHidden:error:]_block_invoke
- ___85-[ATXDefaultHomeScreenItemOnboardingStacksProducer hasConfiguredHomeAccessoryControl]_block_invoke.146
- ___85-[ATXDefaultHomeScreenItemOnboardingStacksProducer hasConfiguredHomeAccessoryControl]_block_invoke.146.cold.1
- ___86-[ATXDefaultHomeScreenItemManager fetchWidgetSmartStackWithRequest:completionHandler:]_block_invoke.67
- ___86-[ATXDefaultHomeScreenItemManager fetchWidgetSmartStackWithRequest:completionHandler:]_block_invoke.71
- ___88-[ATXDefaultHomeScreenItemManager fetchWidgetGalleryItemsWithRequest:completionHandler:]_block_invoke_3
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.77.cold.1
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.77.cold.2
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.77.cold.3
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.77.cold.4
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.78
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.83
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.88
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.91
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke_2.89
- ___98-[ATXHomeScreenSuggestionClient _writeHomeScreenPageConfigurations:guardedData:completionHandler:]_block_invoke
- ___block_literal_global.105
- ___block_literal_global.114
- ___block_literal_global.117
- ___block_literal_global.123
- ___block_literal_global.145
- ___block_literal_global.159
- ___block_literal_global.171
- ___block_literal_global.174
- ___block_literal_global.181
- ___block_literal_global.195
- ___block_literal_global.197
- ___block_literal_global.94
- _objc_msgSend$_carPlayOnboardingStacks
- _objc_msgSend$_filePathForHomeScreenPageConfig
- _objc_msgSend$_generateSmartStackForCarPlayWithDescriptorCacheFromRequest:error:
- _objc_msgSend$_generateSmartStacksForCarPlayWithRequest:error:
- _objc_msgSend$_personalizedCarPlayOnboardingStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:
- _objc_msgSend$_writeHomeScreenPageConfigurations:guardedData:completionHandler:
- _objc_msgSend$bundleIdentifiersNotAllowed
- _objc_msgSend$carPlayOnboardingStacks
- _objc_msgSend$galleryItemsForCarPlayWithRequest:error:
- _objc_msgSend$initWithCandidateWidgets:cachedWidgetPersonalityToAppScore:personalityToDescriptorDictionary:adblDrainClassification:isiPad:isDayZeroExperience:shouldIncludeContactsWidget:cachedHasiCloudFamily:appLaunchCounts:isAmbient:isCarPlay:
- _objc_msgSend$isCHSWidgetDescriptorAllowedForCarPlay:disabledApps:excludedWidgetsWithIdentifiers:
- _objc_msgSend$isCarPlay
- _objc_msgSend$setSmartStackRequest:
- _objc_msgSend$writeHomeScreenPageConfigurations:error:
CStrings:
+ "%s: Client provided identifier %@ NOT equal to widget device identifier %@. Skipping descriptor: %@"
+ "%s: Fetching Widget Smart Stacks for Client: %@"
+ "%s: Fetching Widget gallery items for Client: %@"
+ "%s: No onboarding stack suggestions available for Client: %@, returning nil"
+ "%s: Skipping remote widget because local version exists for %@:%@"
+ "%s: Unexpected widget client value: %ld"
+ "%s: generating onboarding stacks for Client. dayZero:%d, numDescriptors:%lu, descriptorCacheSize:%lu"
+ "%s: personaIdentifier is nil. Skipping remote widget: %@"
+ "+[ATXDefaultHomeScreenItemManager _descriptorsByFilteringDescriptors:disabledApps:excludedWidgetsWithIdentifiers:client:personaIdentifier:]_block_invoke"
+ "-[ATXDefaultHomeScreenItemManager _generateSmartStackWithDescriptorCacheFromRequest:error:]"
+ "-[ATXDefaultHomeScreenItemManager _generateSmartStacksWithRequest:error:]"
+ "-[ATXDefaultHomeScreenItemManager generateItemsForWidgetGalleryWithRequest:error:]"
+ "-[ATXDefaultHomeScreenItemOnboardingStacksProducer generatedStacksWithRequest:]"
+ "-[ATXDefaultHomeScreenItemProducer generatedStacksWithRequest:]"
+ "<%@: %p; clientSessionIdentifier = %@; widgetClient = %@>"
+ "@36@0:8B16@20^@28"
+ "@56@0:8@16@24@32Q40@48"
+ "@80@0:8@16@24@32Q40B48B52B56@60@68B76"
+ "ATXHomeScreenSuggestionClient: Page %lu: %{public}@"
+ "ATXHomeScreenSuggestionClient: Stack on page %lu: %{public}@"
+ "Client: %@. Number of Stacks returned for %lu"
+ "Did not receive rankedContacts for mode:%@ %ld error:%@"
+ "Disfavored for CarPlay: %@"
+ "Failed to load widget descriptors or metadata."
+ "Failed to produce home screen item update for widget gallery."
+ "Filtered due to app protection: %@"
+ "Filtered due to deny list: %@"
+ "Linked before Crystal: %@"
+ "No gallery items found"
+ "Number of items returned for widget gallery suggestions is %lu; Widgets: %@"
+ "Special kind not allowed in CarPlay: %@"
+ "T@\"NSDate\",&,N,V_jobCreationTime"
+ "T@\"NSDictionary\",&,N,V_configuration"
+ "T@\"NSMutableDictionary\",&,N,V_resultStatus"
+ "TvOS"
+ "Unknown ATXStackLayoutSize: %lu"
+ "Unknown(%lu)"
+ "_descriptorsByFilteringDescriptors:disabledApps:excludedWidgetsWithIdentifiers:client:personaIdentifier:"
+ "_didDeferForTestMode"
+ "_filePathForHomeScreenPageConfigWithClientIdentifier:"
+ "_generateSmartStackWithDescriptorCacheFromRequest:error:"
+ "_generateSmartStacksWithRequest:error:"
+ "_jobCreationTime"
+ "_personalizedStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:"
+ "_resultStatus"
+ "_setDoneForTestMode"
+ "_setProgressUnitsForTestMode:"
+ "_writeHomeScreenPageConfigurations:forClientWithIdentifier:guardedData:completionHandler:"
+ "anyCalendarWidget"
+ "anyElectricCarAppWidget"
+ "anyHomeMonitoringAppWidget"
+ "anyMedia_MusicBooksPodcast_Widget"
+ "anyToDoWidget"
+ "areHighlightsEnabled"
+ "areSummariesEnabled"
+ "clientIdentifier"
+ "dayZeroDefaultStackTvOS"
+ "effectiveContainerBundleIdentifier"
+ "generateItemsForWidgetGalleryWithRequest:error:"
+ "generatedStacksWithRequest:"
+ "initForTestingWithIdentifier:configuration:"
+ "initWithCandidateWidgets:cachedWidgetPersonalityToAppScore:personalityToDescriptorDictionary:adblDrainClassification:isiPad:isDayZeroExperience:shouldIncludeContactsWidget:cachedHasiCloudFamily:appLaunchCounts:isAmbient:"
+ "isTestModeEnabled"
+ "jobCreationTime"
+ "loadHomeScreenAndTodayPageConfigurationsIncludingHidden:forClientWithIdentifier:error:"
+ "loadHomeScreenPageConfigurationsForClientWithIdentifier:completionHandler:"
+ "loadHomeScreenPageConfigurationsIncludingHidden:forClientWithIdentifier:error:"
+ "mergedDescriptorsFrom:withAdditional:"
+ "prioritizationSetting"
+ "rankedAppsForMode:options:"
+ "rankedAppsForMode:options:reply:"
+ "rankedContactsForMode:options:reply:"
+ "rankedNotificationsForMode:options:"
+ "rankedNotificationsForMode:options:reply:"
+ "resolvedAction"
+ "resultStatus"
+ "resultStatusForJob"
+ "setActivePersonaWithClientIdentifier:"
+ "setConfiguration:"
+ "setJobCreationTime:"
+ "setResultStatus:"
+ "stringForWidgetClient"
+ "summarizationSetting"
+ "writeHomeScreenPageConfigurations:forClientWithIdentifier:completionHandler:"
+ "writeHomeScreenPageConfigurations:forClientWithIdentifier:error:"
- "%s: Fetching Widget Smart Stacks for CarPlay with identifier: %@"
- "%s: Fetching Widget gallery items for CarPlay with identifier: %@"
- "%s: No onboarding stack suggestions available for CarPlay, returning nil"
- "%s: generating onboarding stacks for CarPlay. dayZero:%d, numDescriptors:%lu, descriptorCacheSize:%lu"
- "-[ATXDefaultHomeScreenItemManager _generateSmartStackForCarPlayWithDescriptorCacheFromRequest:error:]"
- "-[ATXDefaultHomeScreenItemManager _generateSmartStacksForCarPlayWithRequest:error:]"
- "-[ATXDefaultHomeScreenItemManager galleryItemsForCarPlayWithRequest:error:]"
- "-[ATXDefaultHomeScreenItemOnboardingStacksProducer _carPlayOnboardingStacks]"
- "-[ATXDefaultHomeScreenItemProducer carPlayOnboardingStacks]"
- "@84@0:8@16@24@32Q40B48B52B56@60@68B76B80"
- "Descriptor with container bundle identifier is either disabled on homescreen or locked/hidden due to app protection: %@"
- "Descriptor with extension bundle identifier is disfavored in CarPlay: %@"
- "Descriptor with extension bundle identifier is in the deny list: %@"
- "Descriptor with extension bundle identifier is linked before Crystal: %@"
- "Descriptor with kind is not allowed in CarPlay: %@"
- "Failed to load CarPlay widget descriptors or metadata."
- "Failed to produce home screen item update for CarPlay."
- "No CarPlay items found"
- "Number of Stacks returned for Carplay: %lu"
- "Number of widgets returned for CarPlay widget add sheet suggestions is %lu; Widgets: %@"
- "TB,R,N,V_isCarPlay"
- "_carPlayOnboardingStacks"
- "_filePathForHomeScreenPageConfig"
- "_generateSmartStackForCarPlayWithDescriptorCacheFromRequest:error:"
- "_generateSmartStacksForCarPlayWithRequest:error:"
- "_isCarPlay"
- "_personalizedCarPlayOnboardingStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:"
- "_writeHomeScreenPageConfigurations:guardedData:completionHandler:"
- "carPlayAnyCalendarWidget"
- "carPlayAnyMedia_MusicBooksPodcast_Widget"
- "carPlayAnyToDoWidget"
- "carPlayOnboardingStacks"
- "galleryItemsForCarPlayWithRequest:error:"
- "initWithCandidateWidgets:cachedWidgetPersonalityToAppScore:personalityToDescriptorDictionary:adblDrainClassification:isiPad:isDayZeroExperience:shouldIncludeContactsWidget:cachedHasiCloudFamily:appLaunchCounts:isAmbient:isCarPlay:"
- "isCHSWidgetDescriptorAllowedForCarPlay:disabledApps:excludedWidgetsWithIdentifiers:"
- "isCarPlay"

```
