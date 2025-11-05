## Email

> `/System/Library/PrivateFrameworks/Email.framework/Versions/A/Email`

```diff

-3826.400.131.1.6
-  __TEXT.__text: 0xe7620
-  __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_methlist: 0xaee4
-  __TEXT.__gcc_except_tab: 0x1d014
-  __TEXT.__const: 0x28a
-  __TEXT.__cstring: 0xa1a0
-  __TEXT.__oslogstring: 0x606c
+3826.500.181.1.5
+  __TEXT.__text: 0xea888
+  __TEXT.__auth_stubs: 0xd70
+  __TEXT.__objc_methlist: 0xd614
+  __TEXT.__gcc_except_tab: 0x1d474
+  __TEXT.__const: 0x36a
+  __TEXT.__cstring: 0xa3d9
+  __TEXT.__oslogstring: 0x6363
   __TEXT.__ustring: 0x154
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__constg_swiftt: 0xa4
-  __TEXT.__swift5_typeref: 0x59
-  __TEXT.__swift5_reflstr: 0x49
-  __TEXT.__swift5_fieldmd: 0x34
+  __TEXT.__swift5_typeref: 0x71
+  __TEXT.__swift5_reflstr: 0x59
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__constg_swiftt: 0xf0
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_fieldmd: 0x40
   __TEXT.__swift5_capture: 0x24
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x8100
-  __TEXT.__objc_classname: 0x1bf4
-  __TEXT.__objc_methname: 0x1be2f
-  __TEXT.__objc_methtype: 0x4c45
-  __TEXT.__objc_stubs: 0x12500
-  __DATA_CONST.__got: 0xb98
-  __DATA_CONST.__const: 0x1770
-  __DATA_CONST.__objc_classlist: 0x598
+  __TEXT.__swift5_proto: 0xc
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__unwind_info: 0x8320
+  __TEXT.__objc_classname: 0x1c4f
+  __TEXT.__objc_methname: 0x1c2d9
+  __TEXT.__objc_methtype: 0x4df7
+  __TEXT.__objc_stubs: 0x127a0
+  __DATA_CONST.__got: 0xbd8
+  __DATA_CONST.__const: 0x17e8
+  __DATA_CONST.__objc_classlist: 0x5a0
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x340
+  __DATA_CONST.__objc_protolist: 0x350
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d68
+  __DATA_CONST.__objc_selrefs: 0x6038
   __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_superrefs: 0x488
-  __DATA_CONST.__objc_arraydata: 0x160
-  __AUTH_CONST.__auth_got: 0x698
-  __AUTH_CONST.__const: 0x4c90
-  __AUTH_CONST.__cfstring: 0x9320
-  __AUTH_CONST.__objc_const: 0x1bb90
-  __AUTH_CONST.__objc_intobj: 0x2e8
+  __DATA_CONST.__objc_superrefs: 0x490
+  __DATA_CONST.__objc_arraydata: 0x1d0
+  __AUTH_CONST.__auth_got: 0x6c8
+  __AUTH_CONST.__const: 0x4e00
+  __AUTH_CONST.__cfstring: 0x9580
+  __AUTH_CONST.__objc_const: 0x17b10
+  __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x1c58
-  __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0xcac
-  __DATA.__data: 0x2740
-  __DATA.__bss: 0x498
+  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH.__objc_data: 0x1ce0
+  __AUTH.__data: 0x40
+  __DATA.__objc_ivar: 0xcc4
+  __DATA.__data: 0x2820
+  __DATA.__bss: 0x6b0
   __DATA_DIRTY.__objc_data: 0x1c70
   __DATA_DIRTY.__bss: 0x368
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 489D43E5-A427-3B71-AB7A-7F7F4A42B67A
-  Functions: 4675
-  Symbols:   13925
-  CStrings:  8373
+  UUID: 264F50E9-8846-3675-A361-30C9CB40E1E3
+  Functions: 4820
+  Symbols:   14154
+  CStrings:  8478
 
Symbols:
+ +[EMContentRepresentation contentRequestDelegateInterface].cold.1
+ +[EMDaemonInterfaceRequest systemScopeSignpostLog].cold.1
+ +[EMGeneratedSummary consideredUrgentHourLimit].cold.1
+ +[EMHideMyEmail sharedInstance].cold.1
+ +[EMInMemoryThread _dateSortDescriptors].cold.1
+ +[EMInternalPreferences _testOverrideForPreference:]
+ +[EMInternalPreferences _testingOverrideDictionary]
+ +[EMInternalPreferences _testingOverrideDictionary].cold.1
+ +[EMInternalPreferences clearPreferenceForTesting:]
+ +[EMInternalPreferences setPreferenceForTesting:enabled:]
+ +[EMListUnsubscribeDetector unsubscribeTypeForHeader:].cold.1
+ +[EMMailboxScope allMailboxesScope].cold.1
+ +[EMMailboxScope noMailboxesScope].cold.1
+ +[EMMessage(ExternalDataTypes) externalDataTypeIdentifiers].cold.1
+ +[EMMessageList simpleMessageListForMailboxes:withRepository:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:sortDescriptors:transformPredicate:]
+ +[EMMessageList threadedMessageListForMailboxes:withRepository:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:sortDescriptors:sectionPredicates:transformPredicate:]
+ +[EMMessageRepository addValidSortDescriptorsToEMQuery].cold.1
+ +[EMObjectID _decodableClasses].cold.1
+ +[EMRemoteContentURLSession genericHTTPHeaderFields].cold.1
+ +[EMSearchableIndex protectionClass]
+ +[EMSearchableIndexQuery intervalForSpotlightFailureSimulation].cold.1
+ +[EMUbiquitouslyPersistedDictionary sharedDictionaryWithIdentifier:].cold.1
+ +[EMVIPManager _plistURL].cold.1
+ +[NSError(EMNSErrorAdditions) em_internalErrorWithReason:userInfo:].cold.1
+ +[NSError(EMNSErrorAdditions) em_itemNotFoundErrorWithItemID:].cold.1
+ +[NSError(EMNSErrorAdditions) em_itemTimeoutError].cold.1
+ +[NSURL(EMNSURLAdditions) em_mailToFromQueryItemKey].cold.1
+ +[NSUserDefaults(Email) em_lockdownModeEnabled].cold.1
+ +[NSUserDefaults(Email) em_userDefaults].cold.1
+ -[EMBaseMessageListItem ef_shortPublicDescription]
+ -[EMCategorizationSyncManager .cxx_destruct]
+ -[EMCategorizationSyncManager accountRepository]
+ -[EMCategorizationSyncManager categoryCloudStorage:didChangeLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:originator:]
+ -[EMCategorizationSyncManager categoryRulesController:didReceiveNewOldTimestamps:]
+ -[EMCategorizationSyncManager initWithMailboxCategoryCloudStorage:mailboxRepository:accountRepository:]
+ -[EMCategorizationSyncManager loadiCloudMCCKit]
+ -[EMCategorizationSyncManager loadiCloudMCCKit].cold.1
+ -[EMCategorizationSyncManager loadiCloudMCCKit].cold.2
+ -[EMCategorizationSyncManager loadiCloudMCCKit].cold.3
+ -[EMCategorizationSyncManager mailboxCategoryCloudStorage]
+ -[EMCategorizationSyncManager mailboxRepository]
+ -[EMCategorizationSyncManager primaryIcloudMailbox]
+ -[EMCategorizationSyncManager rulesController]
+ -[EMCategory(EFCacheable) cachedSelf].cold.1
+ -[EMCoreAnalyticsCollector _registerXPCActivity].cold.1
+ -[EMDaemonInterface _connectionForProtocol:error:].cold.1
+ -[EMDiagnosticInfoGatherer gatherIndexingDiagnosticsWithCompletionHandler:]
+ -[EMGroupedSenderCollectionItemID(EFCacheable) cachedSelf].cold.1
+ -[EMHideMyEmail _isConfiguredForAccount:error:].cold.2
+ -[EMInMemoryThread _combinedFlagColors].cold.1
+ -[EMInMemoryThreadCollection _shouldSectionItemsRemainInSection]
+ -[EMInMemoryThreadCollection _updateThreadProxy:threadIsEmpty:thread:].cold.1
+ -[EMMailbox isTrashMailbox]
+ -[EMMailboxCategoryCloudStorage _notifyObserversAboutChangedLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:originator:]
+ -[EMMailboxCategoryCloudStorage setIfNeededLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:originator:]
+ -[EMMailboxCategoryCloudStorage setIfNeededLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:originator:].cold.1
+ -[EMMailboxScope(EFCacheable) cachedSelf].cold.1
+ -[EMMessageCollectionItemID(EFCacheable) cachedSelf].cold.1
+ -[EMMessageList filteredMessageListWithPredicate:userFiltered:]
+ -[EMMessageList initWithMailboxes:repository:sortDescriptors:sectionPredicates:transformPredicate:targetClass:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:labelPrefix:]
+ -[EMMessageList itemIDSections]
+ -[EMMessageListItemChange brandIndicatorLocation]
+ -[EMMessageListItemChange setBrandIndicatorLocation:]
+ -[EMMessageRepository _addPrecachedItemsFromExtraInfoIfNeeded:]
+ -[EMMessageRepository _observedCachedItemForItem:itemDescriptionForLogging:validationBlock:]
+ -[EMMessageRepository reportIncorrectBusinessForAddress:isBusinessConnectGrouping:fromClassName:]
+ -[EMObjectID cachedSelf].cold.1
+ -[EMQuery addTargetClassOptions:]
+ -[EMQueryingCollection queryScheduler].cold.1
+ -[EMRemoteContentURLCache _storeCancelationForDataTask:].cold.1
+ -[EMSearchableIndexQuery _isFinishedQueryStatus:].cold.1
+ -[EMSectionedMessageList filteredMessageListWithPredicate:userFiltered:]
+ -[EMThread ef_shortPublicDescription]
+ -[EMThreadCollectionItemID(EFCacheable) cachedSelf].cold.1
+ -[EMThreadObjectID cachedSelf].cold.1
+ -[EMThreadScope(EFCacheable) cachedSelf].cold.1
+ -[_EMSectionedMessageListItem(EFCacheable) cachedSelf].cold.1
+ -[_EMSectionedMessageListItemID(EFCacheable) cachedSelf].cold.1
+ -[_EMSectionedObjectID(EFCacheable) cachedSelf].cold.1
+ -[_EMSpecialMailboxScope(EFCacheable) cachedSelf].cold.1
+ EMBlackPearlIsFeatureEnabled.cold.1
+ EMBlackPearlIsLanguageSupported.cold.1
+ EMIsGreymatterAvailable.cold.1
+ EMIsGreymatterSupported.cold.1
+ EMLogBIMI.cold.1
+ EMLogCategoryMessageLoading.cold.1
+ EMLogCompose.cold.1
+ EMLogMailDrop.cold.1
+ EMLogSearch.cold.1
+ EMLogSearchableIndexStatus.cold.1
+ EMLogUtilities.cold.1
+ EMLogUtilities.onceToken
+ EMLogUtilities.os_log
+ EMPrivacyProxyIsDisabledForNetwork.cold.1
+ GCC_except_table178
+ GCC_except_table181
+ GCC_except_table183
+ GCC_except_table184
+ GCC_except_table208
+ GCC_except_table209
+ GCC_except_table211
+ GCC_except_table225
+ GCC_except_table226
+ GCC_except_table227
+ GCC_except_table231
+ GCC_except_table232
+ GCC_except_table236
+ GCC_except_table241
+ GCC_except_table242
+ GCC_except_table246
+ GCC_except_table248
+ GCC_except_table253
+ GCC_except_table254
+ GCC_except_table272
+ GCC_except_table273
+ GCC_except_table274
+ GCC_except_table290
+ GCC_except_table291
+ GCC_except_table297
+ LoadicloudMCCKit.frameworkLibrary
+ LoadicloudMCCKit.loadPredicate
+ OBJC_IVAR_$_EMCategorizationSyncManager._accountRepository
+ OBJC_IVAR_$_EMCategorizationSyncManager._icloudSyncScheduler
+ OBJC_IVAR_$_EMCategorizationSyncManager._mailboxCategoryCloudStorage
+ OBJC_IVAR_$_EMCategorizationSyncManager._mailboxRepository
+ OBJC_IVAR_$_EMCategorizationSyncManager._rulesController
+ OBJC_IVAR_$_EMMessageListItemChange._brandIndicatorLocation
+ _EMGenerativeModelsAvailabilityFeature.cold.1
+ _EMGenerativeModelsAvailabilityFeature.featureDictionary
+ _EMGenerativeModelsAvailabilityFeature.onceToken
+ _EMGenerativeModelsOnDemandSummarizationAvailabilityDidChange
+ _EMGenerativeModelsSmartReplyAvailabilityDidChange
+ _EMGenerativeModelsSummarizationAvailabilityDidChange
+ _EMLogUtilities
+ _EMMessageListItemKeyPathBrandIndicatorLocation
+ _EMMessageListQueryOptionShouldSectionItemsRemainInSection
+ _EMPersistenceStatisticsKeyPercentIndexedLastMonth
+ _EMPersistenceStatisticsKeyPercentIndexedLastTwoDays
+ _EMUserDefaultAddLogoOriginBadges
+ _EMUserDefaultAllowBIMILogosInGroupedSenders
+ _EMUserDefaultCategoriesEnabledByDefault
+ _EMUserDefaultDeleteOrMoveMessageAction
+ _EMUserDefaultDisableCategorizationOnboardingPrimaryBadgeCount
+ _EMUserDefaultDisableCategorizationOnboardingPrimaryV1
+ _EMUserDefaultIncorrectBusinessAddressMappingsReported
+ _EMUserDefaultShowCategoryAsTimeSensitiveImage
+ _EMUserDefaultSimulateSensitiveContentSummarizationError
+ _MCCCategoryRulesControllerFunction
+ _MCCSecretAgentControllerFunction
+ _NSLog
+ _OBJC_$_PROP_LIST_EMObject.82
+ _OBJC_$_PROP_LIST_EMSortableMessage.83
+ _OBJC_CLASS_$_EMCategorizationSyncManager
+ _OBJC_METACLASS_$_EMCategorizationSyncManager
+ __106-[EMMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.572
+ __106-[EMMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.572.cold.1
+ __146-[EMCategorizationSyncManager categoryCloudStorage:didChangeLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:originator:]_block_invoke.23
+ __203-[EMSearchableIndexTopHitsQuery initWithSearchString:filterQueries:bundleID:keyboardLanguage:updatedSuggestion:generateSuggestions:logDescription:resultLimit:suggestionLimit:customFlags:feedbackQueryID:]_block_invoke.112
+ __26-[EMThread displayMessage]_block_invoke.210
+ __32-[EMMessageList collapseThread:]_block_invoke.162
+ __32-[EMMessageList collapseThread:]_block_invoke.162.cold.1
+ __33-[EMDaemonInterface proxyCreator]_block_invoke.309.cold.1
+ __33-[EMDaemonInterface proxyCreator]_block_invoke.314
+ __33-[EMDaemonInterface proxyCreator]_block_invoke_2.310
+ __38-[EMMessageRepository _vipsDidChange:]_block_invoke.694
+ __44-[EMDaemonInterface checkInMailAppEndpoint:]_block_invoke.379
+ __44-[EMDaemonInterface checkInMailAppEndpoint:]_block_invoke.379.cold.1
+ __44-[EMMessageRepository metadataForAddresses:]_block_invoke.617
+ __44-[EMMessageRepository metadataForAddresses:]_block_invoke.617.cold.1
+ __45-[EMDaemonInterface resetProtocolConnections]_block_invoke.371
+ __48-[EMMessageRepository _blockedSendersDidChange:]_block_invoke.685
+ __50-[EMDaemonInterface _connectionForProtocol:error:]_block_invoke.367
+ __51-[EMCategorizationSyncManager primaryIcloudMailbox]_block_invoke.30
+ __53-[EMDiagnosticInfoGatherer initWithRemoteConnection:]_block_invoke.102
+ __54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.180
+ __54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.187
+ __54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.187.cold.1
+ __54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.191
+ __54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke_2.181
+ __54-[EMMessageRepository persistentIDForMessageObjectID:]_block_invoke.671
+ __54-[EMMessageRepository persistentIDForMessageObjectID:]_block_invoke.671.cold.1
+ __55-[EMMessageRepository setUpURLCacheWithMemoryCapacity:]_block_invoke.628
+ __55-[EMMessageRepository setUpURLCacheWithMemoryCapacity:]_block_invoke.631
+ __56-[EMMessageList queryMatchedChangedObjectIDs:extraInfo:]_block_invoke.225
+ __58-[EMMessageList _attemptToFinishRetryingPromisesByItemID:]_block_invoke.195
+ __58-[EMMessageRepository cachedMetadataJSONForKey:messageID:]_block_invoke.608
+ __59-[EMDiagnosticInfoGatherer registerDiagnosticInfoProvider:]_block_invoke.179
+ __59-[EMMessageRepository _updateObserversForDeletedObjectIDs:]_block_invoke.601
+ __60+[EMMailbox(EMQueryAdditions) sortDescriptorForDisplayOrder]_block_invoke.cold.1
+ __62-[EMSearchableIndexTopHitsQuery _configureTopHitsSearchQuery:]_block_invoke.118
+ __66-[EMMessageRepository _localInMemoryMessageObjectIDsForObjectIDs:]_block_invoke.317
+ __68-[EMDiagnosticInfoGatherer provideDiagnosticsAt:options:completion:]_block_invoke.189
+ __68-[EMDiagnosticInfoGatherer provideDiagnosticsAt:options:completion:]_block_invoke.191
+ __68-[EMDiagnosticInfoGatherer provideDiagnosticsAt:options:completion:]_block_invoke.195
+ __69-[EMMessageList queryMatchedOldestItemsUpdatedForMailboxesObjectIDs:]_block_invoke.233
+ __74-[EMMessageRepository requestRichLinkURLsForMessageIDs:completionHandler:]_block_invoke.586
+ __76-[EMMessageRepository requestAttachmentURLsForMessageIDs:completionHandler:]_block_invoke.582
+ __77-[EMMessageRepository messagesInConversationIDs:limit:observationIdentifier:]_block_invoke.643
+ __80-[EMMessageRepository _broadcastMessageListItemChangesToObservers:forObjectIDs:]_block_invoke.704
+ __82-[EMCategorizationSyncManager categoryRulesController:didReceiveNewOldTimestamps:]_block_invoke.17
+ __82-[EMCategorizationSyncManager categoryRulesController:didReceiveNewOldTimestamps:]_block_invoke.cold.1
+ __82-[EMMessageRepository _removeItemsFromObservedItemsCacheIfNotObservedByObservers:]_block_invoke.562
+ __86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.275
+ __86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.278
+ __86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.281
+ __86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.299
+ __88-[EMMessageRepository requestRichLinkMetadataForRichLinkID:messageID:completionHandler:]_block_invoke.578
+ __EMBlackPearlIsFeatureEnabled_block_invoke.cold.1
+ __EMBlackPearlIsLanguageSupported_block_invoke_2.cold.1
+ __EMGenerativeModelsAvailabilityFeature
+ __OBJC_$_INSTANCE_METHODS_EMCategorizationSyncManager
+ __OBJC_$_INSTANCE_VARIABLES_EMCategorizationSyncManager
+ __OBJC_$_PROP_LIST_EMCategorizationSyncManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_EMMailboxCategoryCloudStorageObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_EFPubliclyDescribable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MCCCategoryRulesDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EMMailboxCategoryCloudStorageObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MCCCategoryRulesDelegate
+ __OBJC_$_PROTOCOL_REFS_EMMailboxCategoryCloudStorageObserver
+ __OBJC_$_PROTOCOL_REFS_MCCCategoryRulesDelegate
+ __OBJC_CLASS_PROTOCOLS_$_EMCategorizationSyncManager
+ __OBJC_CLASS_RO_$_EMCategorizationSyncManager
+ __OBJC_LABEL_PROTOCOL_$_EMMailboxCategoryCloudStorageObserver
+ __OBJC_LABEL_PROTOCOL_$_MCCCategoryRulesDelegate
+ __OBJC_METACLASS_RO_$_EMCategorizationSyncManager
+ __OBJC_PROTOCOL_$_EMMailboxCategoryCloudStorageObserver
+ __OBJC_PROTOCOL_$_MCCCategoryRulesDelegate
+ __PROPERTIES__TtC5Email30EMGenerativeModelsAvailability
+ ___113+[EMMessageListChangeObserverHelper collection:notifyChangeObserversAboutChangedItemIDs:itemIDsWithCountChanges:]_block_invoke_2
+ ___113+[EMMessageListChangeObserverHelper collection:notifyChangeObserversAboutChangedItemIDs:itemIDsWithCountChanges:]_block_invoke_3
+ ___113+[EMMessageListChangeObserverHelper collection:notifyChangeObserversAboutChangedItemIDs:itemIDsWithCountChanges:]_block_invoke_4
+ ___129-[EMMailboxCategoryCloudStorage setIfNeededLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:originator:]_block_invoke
+ ___146-[EMCategorizationSyncManager categoryCloudStorage:didChangeLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:originator:]_block_invoke
+ ___146-[EMMailboxCategoryCloudStorage _notifyObserversAboutChangedLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:originator:]_block_invoke
+ ___51+[EMInternalPreferences _testingOverrideDictionary]_block_invoke
+ ___51-[EMCategorizationSyncManager primaryIcloudMailbox]_block_invoke
+ ___63-[EMMessageList filteredMessageListWithPredicate:userFiltered:]_block_invoke
+ ___63-[EMMessageRepository _addPrecachedItemsFromExtraInfoIfNeeded:]_block_invoke
+ ___72-[EMSectionedMessageList filteredMessageListWithPredicate:userFiltered:]_block_invoke
+ ___82-[EMCategorizationSyncManager categoryRulesController:didReceiveNewOldTimestamps:]_block_invoke
+ ___EMBlackPearlIsLanguageSupported_block_invoke_2
+ ___EMLogUtilities_block_invoke
+ ___LoadicloudMCCKit_block_invoke
+ ____EMGenerativeModelsAvailabilityFeature_block_invoke
+ ____ef_log_EMCategorizationSyncManager_block_invoke
+ ___block_descriptor_32_e19_B16?0"EMAccount"8l
+ ___block_descriptor_32_e20_v20?0B8"NSError"12l
+ ___block_descriptor_40_ea8_32r_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_48_ea8_32s40s_e34_v32?0"NSString"8"NSArray"16^B24l
+ ___block_descriptor_48_ea8_32s40s_e35_v32?0"NSString"8"NSNumber"16^B24l
+ ___block_descriptor_49_ea8_32s40r_e56_v40?0Q8"<NSObject><NSCopying>"16"EMMessageList"24^B32l
+ ___block_descriptor_56_ea8_32s40s48r_e54_v32?0"EMRepositoryObject<EMMessageListItem>"8Q16^B24l
+ ___block_descriptor_64_ea8_32s40s48s56s_e26_"NSArray"16?0"NSArray"8l
+ ___block_descriptor_88_ea8_32s40s48s56s64s_e38_v16?0"<EMCollectionChangeObserver>"8l
+ __block_literal_global.103
+ __block_literal_global.23
+ __block_literal_global.230
+ __block_literal_global.239
+ __block_literal_global.245
+ __block_literal_global.251
+ __block_literal_global.320
+ __block_literal_global.325
+ __block_literal_global.366
+ __block_literal_global.373
+ __block_literal_global.470
+ __block_literal_global.482
+ __block_literal_global.518
+ __block_literal_global.55
+ __block_literal_global.603
+ __block_literal_global.620
+ __block_literal_global.696
+ __block_literal_global.700
+ __block_literal_global.92
+ __block_literal_global.97
+ __ef_log_EMCategorizationSyncManager
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance 5Email37EMGenerativeModelsAvailabilityFeatureOSHAASQ
+ _classMCCCategoryRulesController
+ _classMCCSecretAgentController
+ _dlopen
+ _ef_log_EMCategorizationSyncManager.cold.1
+ _ef_log_EMCategorizationSyncManager.log
+ _ef_log_EMCategorizationSyncManager.onceToken
+ _ef_log_EMFocusController.cold.1
+ _ef_log_EMGroupedSenderCollectionItemID.cold.1
+ _ef_log_EMMailboxCategoryCloudStorage.cold.1
+ _ef_log_EMRemoteContentURLSession.cold.1
+ _ef_log_EMSMIMEUtilities.cold.1
+ _ef_log_EMServerConfiguration.cold.1
+ _getMCCCategoryRulesControllerClass
+ _getMCCSecretAgentControllerClass
+ _initMCCCategoryRulesController
+ _initMCCSecretAgentController
+ _objc_msgSend$_addPrecachedItemsFromExtraInfoIfNeeded:
+ _objc_msgSend$_deviceLanguage
+ _objc_msgSend$_observedCachedItemForItem:itemDescriptionForLogging:validationBlock:
+ _objc_msgSend$addCloudStorageObserver:
+ _objc_msgSend$areInternalSecurityPoliciesAllowed
+ _objc_msgSend$categoryCloudStorage:didChangeLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:originator:
+ _objc_msgSend$externalURL
+ _objc_msgSend$filteredMessageListWithPredicate:userFiltered:
+ _objc_msgSend$gatherIndexingDiagnosticsWithCompletionHandler:
+ _objc_msgSend$initWithMailboxes:repository:sortDescriptors:sectionPredicates:transformPredicate:targetClass:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:labelPrefix:
+ _objc_msgSend$isCategorizationSupportedForLocale:completion:
+ _objc_msgSend$isFeatureAvailable:
+ _objc_msgSend$isFeatureRestricted:
+ _objc_msgSend$isMac
+ _objc_msgSend$isPad
+ _objc_msgSend$itemIDSections
+ _objc_msgSend$loadiCloudMCCKit
+ _objc_msgSend$mailboxCategoryCloudStorage
+ _objc_msgSend$performQuery:completionHandler:
+ _objc_msgSend$predicateForPrimaryMailboxWithAccount:
+ _objc_msgSend$primaryIcloudMailbox
+ _objc_msgSend$protectionClass
+ _objc_msgSend$redactedQueryStringForSearchableQueryString:
+ _objc_msgSend$registerForWebRuleNotifications
+ _objc_msgSend$reportIncorrectBusinessForAddress:isBusinessConnectGrouping:fromClassName:
+ _objc_msgSend$setIfNeededLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:originator:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$simpleMessageListForMailboxes:withRepository:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:sortDescriptors:transformPredicate:
+ _objc_msgSend$syncNewOldCategoryTimestamps:
+ _objc_msgSend$threadedMessageListForMailboxes:withRepository:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:sortDescriptors:sectionPredicates:transformPredicate:
+ _swift_isaMask
+ _symbolic $sSY
+ _symbolic Si
+ _symbolic _____ 5Email37EMGenerativeModelsAvailabilityFeatureO
+ _testingOverrideDictionary.onceToken
+ _testingOverrideDictionary.testingOverrideDictionary
+ initMCCCategoryRulesController.cold.1
+ initMCCSecretAgentController.cold.1
- +[EMMessageList simpleMessageListForMailboxes:withRepository:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:sortDescriptors:transformPredicate:ignoreMessageAdditionsPredicate:shouldShowBundle:]
- +[EMMessageList threadedMessageListForMailboxes:withRepository:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:sortDescriptors:sectionPredicates:transformPredicate:ignoreMessageAdditionsPredicate:shouldShowBundle:]
- -[EMMailboxCategoryCloudStorage _notifyObserversAboutChangedLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:]
- -[EMMailboxCategoryCloudStorage setIfNeededLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:]
- -[EMMailboxCategoryCloudStorage setIfNeededLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:].cold.1
- -[EMMessageList filteredMessageListWithPredicate:ignoredMessagesPredicate:userFiltered:]
- -[EMMessageList initWithMailboxes:repository:sortDescriptors:sectionPredicates:transformPredicate:ignoreMessageAdditionsPredicate:targetClass:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:labelPrefix:shouldShowBundle:]
- -[EMMessageRepository _addPrecachedItems:]
- -[EMSectionedMessageList filteredMessageListWithPredicate:ignoredMessagesPredicate:userFiltered:]
- -[_EMMessageRepositoryQueryObserver _precachedItemsFromExtraInfo:]
- EMIsGreymatterSupportedWithOverride.isGreymatterSupported
- EMIsGreymatterSupportedWithOverride.onceToken
- GCC_except_table193
- GCC_except_table194
- GCC_except_table200
- GCC_except_table207
- GCC_except_table212
- GCC_except_table214
- GCC_except_table228
- GCC_except_table229
- GCC_except_table233
- GCC_except_table235
- GCC_except_table239
- GCC_except_table240
- GCC_except_table245
- GCC_except_table250
- GCC_except_table251
- GCC_except_table255
- GCC_except_table256
- GCC_except_table260
- GCC_except_table284
- GCC_except_table288
- GCC_except_table294
- _EFIsSeedBuild
- _EMGenerativeModelsAvailabilityDidChange
- _EMInteractionLoggerShouldLog
- _EMIsGreymatterAvailableWithOverride
- _EMIsGreymatterSupportedWithOverride
- _EMMessageListIgnoreMessageAdditionsPredicate
- _EMUserDefaultAllowBIMIWithDKIMSignature
- _EMUserDefaultAllowFindInDigestView
- _EMUserDefaultEnableHighImpactRegex
- _EMUserDefaultEnableThreadedMessagesInWidget
- _EMUserDefaultNewFilterCardEnabled
- _EMUserDefaultNewQueryResults
- _EMUserDefaultQueryResultComparison
- _EMUserDefaultSearchFlagColors
- _EMUserDefaultSharingFromSafariUI
- _OBJC_$_PROP_LIST_EMObject.79
- _OBJC_$_PROP_LIST_EMSortableMessage.80
- __106-[EMMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.564
- __106-[EMMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.564.cold.1
- __203-[EMSearchableIndexTopHitsQuery initWithSearchString:filterQueries:bundleID:keyboardLanguage:updatedSuggestion:generateSuggestions:logDescription:resultLimit:suggestionLimit:customFlags:feedbackQueryID:]_block_invoke.113
- __26-[EMThread displayMessage]_block_invoke.203
- __32-[EMMessageList collapseThread:]_block_invoke.161
- __32-[EMMessageList collapseThread:]_block_invoke.161.cold.1
- __33-[EMDaemonInterface proxyCreator]_block_invoke.304
- __33-[EMDaemonInterface proxyCreator]_block_invoke.304.cold.1
- __33-[EMDaemonInterface proxyCreator]_block_invoke_2.305
- __38-[EMMessageRepository _vipsDidChange:]_block_invoke.682
- __44-[EMDaemonInterface checkInMailAppEndpoint:]_block_invoke.374
- __44-[EMDaemonInterface checkInMailAppEndpoint:]_block_invoke.374.cold.1
- __44-[EMMessageRepository metadataForAddresses:]_block_invoke.609
- __44-[EMMessageRepository metadataForAddresses:]_block_invoke.609.cold.1
- __45-[EMDaemonInterface resetProtocolConnections]_block_invoke.366
- __48-[EMMessageRepository _blockedSendersDidChange:]_block_invoke.673
- __50-[EMDaemonInterface _connectionForProtocol:error:]_block_invoke.362
- __53-[EMDiagnosticInfoGatherer initWithRemoteConnection:]_block_invoke.96
- __54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.179
- __54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.186
- __54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.186.cold.1
- __54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.190
- __54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke_2.180
- __54-[EMMessageRepository persistentIDForMessageObjectID:]_block_invoke.663
- __54-[EMMessageRepository persistentIDForMessageObjectID:]_block_invoke.663.cold.1
- __55-[EMMessageRepository setUpURLCacheWithMemoryCapacity:]_block_invoke.620
- __55-[EMMessageRepository setUpURLCacheWithMemoryCapacity:]_block_invoke.623
- __56-[EMMessageList queryMatchedChangedObjectIDs:extraInfo:]_block_invoke.224
- __58-[EMMessageList _attemptToFinishRetryingPromisesByItemID:]_block_invoke.194
- __58-[EMMessageRepository cachedMetadataJSONForKey:messageID:]_block_invoke.600
- __59-[EMDiagnosticInfoGatherer registerDiagnosticInfoProvider:]_block_invoke.171
- __59-[EMMessageRepository _updateObserversForDeletedObjectIDs:]_block_invoke.593
- __62-[EMSearchableIndexTopHitsQuery _configureTopHitsSearchQuery:]_block_invoke.119
- __66-[EMMessageRepository _localInMemoryMessageObjectIDsForObjectIDs:]_block_invoke.313
- __68-[EMDiagnosticInfoGatherer provideDiagnosticsAt:options:completion:]_block_invoke.181
- __68-[EMDiagnosticInfoGatherer provideDiagnosticsAt:options:completion:]_block_invoke.183
- __68-[EMDiagnosticInfoGatherer provideDiagnosticsAt:options:completion:]_block_invoke.187
- __69-[EMMessageList queryMatchedOldestItemsUpdatedForMailboxesObjectIDs:]_block_invoke.232
- __74-[EMMessageRepository requestRichLinkURLsForMessageIDs:completionHandler:]_block_invoke.578
- __76-[EMMessageRepository requestAttachmentURLsForMessageIDs:completionHandler:]_block_invoke.574
- __77-[EMMessageRepository messagesInConversationIDs:limit:observationIdentifier:]_block_invoke.635
- __80-[EMMessageRepository _broadcastMessageListItemChangesToObservers:forObjectIDs:]_block_invoke.692
- __82-[EMMessageRepository _removeItemsFromObservedItemsCacheIfNotObservedByObservers:]_block_invoke.554
- __86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.271
- __86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.274
- __86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.277
- __86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.295
- __88-[EMMessageRepository requestRichLinkMetadataForRichLinkID:messageID:completionHandler:]_block_invoke.570
- __CLASS_PROPERTIES__TtC5Email30EMGenerativeModelsAvailability
- ___118-[EMMailboxCategoryCloudStorage setIfNeededLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:]_block_invoke
- ___135-[EMMailboxCategoryCloudStorage _notifyObserversAboutChangedLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:]_block_invoke
- ___68-[EMMessageRepository _cachedItemForItem:observers:validationBlock:]_block_invoke
- ___88-[EMMessageList filteredMessageListWithPredicate:ignoredMessagesPredicate:userFiltered:]_block_invoke
- ___97-[EMSectionedMessageList filteredMessageListWithPredicate:ignoredMessagesPredicate:userFiltered:]_block_invoke
- ___EMIsGreymatterSupportedWithOverride_block_invoke
- ___block_descriptor_48_ea8_32s40s_e37_v32?0"<NSCopying>"8"NSArray"16^B24l
- ___block_descriptor_56_ea8_32s40r_e29_v16?0"NSMutableDictionary"8l
- ___block_descriptor_57_ea8_32s40s48r_e56_v40?0Q8"<NSObject><NSCopying>"16"EMMessageList"24^B32l
- ___block_descriptor_72_ea8_32s40s48s_e38_v16?0"<EMCollectionChangeObserver>"8l
- __block_literal_global.227
- __block_literal_global.240
- __block_literal_global.246
- __block_literal_global.252
- __block_literal_global.316
- __block_literal_global.321
- __block_literal_global.328
- __block_literal_global.34
- __block_literal_global.361
- __block_literal_global.368
- __block_literal_global.37
- __block_literal_global.40
- __block_literal_global.44
- __block_literal_global.467
- __block_literal_global.479
- __block_literal_global.513
- __block_literal_global.595
- __block_literal_global.612
- __block_literal_global.676
- __block_literal_global.684
- _objc_msgSend$_addPrecachedItems:
- _objc_msgSend$_precachedItemsFromExtraInfo:
- _objc_msgSend$categoryCloudStorage:didChangeLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:
- _objc_msgSend$ef_preferredLanguageIdentifier
- _objc_msgSend$filteredMessageListWithPredicate:ignoredMessagesPredicate:userFiltered:
- _objc_msgSend$initWithMailboxes:repository:sortDescriptors:sectionPredicates:transformPredicate:ignoreMessageAdditionsPredicate:targetClass:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:labelPrefix:shouldShowBundle:
- _objc_msgSend$isRestricted
- _objc_msgSend$simpleMessageListForMailboxes:withRepository:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:sortDescriptors:transformPredicate:ignoreMessageAdditionsPredicate:shouldShowBundle:
- _objc_msgSend$threadedMessageListForMailboxes:withRepository:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:sortDescriptors:sectionPredicates:transformPredicate:ignoreMessageAdditionsPredicate:shouldShowBundle:
CStrings:
+ "### Failed to Soft Linked: /System/Library/PrivateFrameworks/icloudMCCKit.framework/icloudMCCKit"
+ "% indexed last 2 days"
+ "% indexed last month"
+ "%@ \n\tConversationID:%@\n\tSubject:%@ \n\tFlags:%@ \n"
+ "%@ \n\tConversationID:%@ \n\tFlags:%@ \n\tDate:%@ \n"
+ "%p: Missing threadProxy. Created new threadProxy:%p for itemID:%{public}@"
+ "+[EMInternalPreferences _testingOverrideDictionary]"
+ "/System/Library/PrivateFrameworks/icloudMCCKit.framework/icloudMCCKit"
+ "<%p> Cached observed item <%{public}@: %p> exists for %{public}@ <%{public}@: %p> with objectID %{public}@"
+ "<%p> No cached item exists for %{public}@ <%{public}@: %p> with objectID %{public}@. Adding to observed cache."
+ "<%p> No cached observed item, cached unobserved item <%{public}@: %p> exists for %{public}@ <%{public}@: %p> with objectID %{public}@. Moving to observed cache."
+ "@\"<EMMessageListItemChangeBrandIndicatorLocation>\""
+ "@\"EMMailboxCategoryCloudStorage\""
+ "@\"MCCCategoryRulesController\""
+ "@\"NSString\"24@0:8@\"<EMCollection>\"16"
+ "@28@0:8@\"NSPredicate\"16B24"
+ "@68@0:8@16@24Q32Q40B48@52@?60"
+ "@76@0:8@16@24Q32Q40B48@52@60@?68"
+ "@92@0:8@16@24@32@40@?48#56Q64Q72B80@84"
+ "AddLogoOriginBadges"
+ "B16@?0@\"EMAccount\"8"
+ "B56@0:8@16@24@32@40Q48"
+ "Cannot create Rules listener"
+ "Cannot load MCCKit framework"
+ "CatchUpCategorization"
+ "CatchUpHighlights"
+ "CatchUpHighlightsV2"
+ "CatchUpNotifications"
+ "CategoriesEnabledByDefault"
+ "ClassCData"
+ "Current GenerativeModelsAvailability for %s: %s"
+ "DeleteOrMoveMessageAction"
+ "DisableCategorizationOnboardingPrimary-v2"
+ "DisableCategorizationOnboardingPrimaryBadgeCount"
+ "EMCategorizationSyncManager"
+ "EMFeatureFlag.m"
+ "EMGenerativeModelsOnDemandSummarizationAvailabilityDidChange"
+ "EMGenerativeModelsSmartReplyAvailabilityDidChange"
+ "EMGenerativeModelsSummarizationAvailabilityDidChange"
+ "EMInternalPreferences.m"
+ "EMMailboxCategoryCloudStorage didChangeLastSeenDate: %@, lastSeenDisplayDate: %@, categoryType: %@, url: %@"
+ "EMMailboxCategoryCloudStorageObserver"
+ "Email.EMGenerativeModelsAvailability"
+ "Error occured when checking for supported locale: %@"
+ "GenerativeModelsAvailability for %s changed from: %s, to: %s"
+ "GenerativeModelsAvailability for %s changed to: %s, but was already: %s. Skipping availability-change notification"
+ "GroupedSendersShowsBIMI"
+ "IncorrectBusinessAddressMappingsReported"
+ "Initiated MCCCategoryRulesController and registered for new/old notifications"
+ "MCCCategoryRulesController"
+ "MCCCategoryRulesController didReceiveNewOldTimestamps: %@"
+ "MCCCategoryRulesDelegate"
+ "MCCSecretAgentController"
+ "No primary iCloud account has found."
+ "No primary iCloud mailbox has found."
+ "Received Last Seend date change, ignoring it as the originator is webmail."
+ "Setting user query with expression: %{private}@ context: %{private}@"
+ "ShouldSectionItemsRemainInSection"
+ "ShowCategoryAsTimeSensitiveImage"
+ "SimulateSensitiveContentSummarizationError"
+ "Skipping syncing, no primary iCloud Mailbox found."
+ "Skipping syncing, not a primary iCloud mailbox change"
+ "Syncing category: %@ with timestamp: %@"
+ "T@\"<EMMessageListItemChangeBrandIndicatorLocation>\",&,N,V_brandIndicatorLocation"
+ "T@\"EFLocked\",R,N,V_itemIDSections"
+ "T@\"EMMailboxCategoryCloudStorage\",R,N,V_mailboxCategoryCloudStorage"
+ "T@\"MCCCategoryRulesController\",R,N,V_rulesController"
+ "T@\"NSString\",?,R,C,N"
+ "Tq,N,Vfeature"
+ "Unable to save New/Old timestamps. Categories: %@, icloudMailbox: %@"
+ "Utilities"
+ "_EMGenerativeModelsAvailabilityFeature"
+ "_addPrecachedItemsFromExtraInfoIfNeeded:"
+ "_deviceLanguage"
+ "_icloudSyncScheduler"
+ "_mailboxCategoryCloudStorage"
+ "_observedCachedItemForItem:itemDescriptionForLogging:validationBlock:"
+ "_rulesController"
+ "_testingOverrideDictionary"
+ "addTargetClassOptions:"
+ "areInternalSecurityPoliciesAllowed"
+ "categoryCloudStorage:didChangeLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:originator:"
+ "categoryRulesController:didAlterConnectionWithReason:"
+ "categoryRulesController:didReceiveNewOldTimestamps:"
+ "categoryRulesController:didReceiveOverrideRules:"
+ "categoryRulesController:didReceiveSyncAllOverrideRules:"
+ "clearPreferenceForTesting:"
+ "com.apple.email.%@.icloudSyncScheduler"
+ "ef_shortPublicDescription"
+ "feature"
+ "featureNumber"
+ "filteredMessageListWithPredicate:userFiltered:"
+ "gatherIndexingDiagnosticsWithCompletionHandler:"
+ "init()"
+ "initWithMailboxCategoryCloudStorage:mailboxRepository:accountRepository:"
+ "initWithMailboxes:repository:sortDescriptors:sectionPredicates:transformPredicate:targetClass:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:labelPrefix:"
+ "isCategorizationSupportedForLocale:completion:"
+ "isFeatureAvailable:"
+ "isFeaturePolicyLimited:"
+ "isFeatureRestricted:"
+ "isMac"
+ "isPad"
+ "isTrashMailbox"
+ "item"
+ "itemIDSections"
+ "loadiCloudMCCKit"
+ "mailboxCategoryCloudStorage"
+ "precached item"
+ "primaryIcloudMailbox"
+ "protectionClass"
+ "redactedQueryStringForSearchableQueryString:"
+ "registerForWebRuleNotifications"
+ "reportIncorrectBusinessForAddress:isBusinessConnectGrouping:fromClassName:"
+ "rulesController"
+ "setFeature:"
+ "setIfNeededLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:originator:"
+ "setObject:atIndexedSubscript:"
+ "setPreferenceForTesting:enabled:"
+ "simpleMessageListForMailboxes:withRepository:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:sortDescriptors:transformPredicate:"
+ "summarization.summarizeMailMessageThreadOnDemand"
+ "syncNewOldCategoryTimestamps:"
+ "textComposition.MailReply"
+ "threadedMessageListForMailboxes:withRepository:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:sortDescriptors:sectionPredicates:transformPredicate:"
+ "v24@0:8@?<v@?@\"NSURL\"@\"NSError\">16"
+ "v32@0:8@\"MCCCategoryRulesController\"16@\"NSArray\"24"
+ "v32@0:8@\"MCCCategoryRulesController\"16@\"NSDictionary\"24"
+ "v32@0:8@\"MCCCategoryRulesController\"16q24"
+ "v32@?0@\"EMRepositoryObject<EMMessageListItem>\"8Q16^B24"
+ "v32@?0@\"NSString\"8@\"NSArray\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSNumber\"16^B24"
+ "v36@0:8@\"<ECEmailAddressConvertible>\"16B24@\"NSString\"28"
+ "v64@0:8@\"EMMailboxCategoryCloudStorage\"16@\"NSDate\"24@\"NSDate\"32@\"NSNumber\"40@\"NSURL\"48Q56"
+ "v64@0:8@16@24@32@40@48Q56"
- "<%p> Adding precached item <%{public}@: %p> to observed cache for objectID %{public}@"
- "<%p> Cached observed item <%{public}@: %p> exists for item <%{public}@: %p> with objectID %{public}@"
- "<%p> No cached item exists for item <%{public}@: %p> with objectID %{public}@. Adding to observed cache."
- "<%p> No cached observed item, cached unobserved item <%{public}@: %p> exists for item <%{public}@: %p> with objectID %{public}@. Moving to observed cache."
- "@\"<NSCopying>\"24@0:8@\"<EMCollection>\"16"
- "@104@0:8@16@24@32@40@?48@56#64Q72Q80B88@92B100"
- "@36@0:8@\"NSPredicate\"16@\"NSPredicate\"24B32"
- "@80@0:8@16@24Q32Q40B48@52@?60@68B76"
- "@88@0:8@16@24Q32Q40B48@52@60@?68@76B84"
- "AllowBIMIWithDKIMSignature"
- "AllowFindInDigestView"
- "B48@0:8@16@24@32@40"
- "Current GenerativeModelsAvailability: %s"
- "EMGenerativeModelsAvailabilityDidChange"
- "EMMessageListIgnoreMessageAdditionsPredicate"
- "EMUserDefaultEnableHighImpactRegex"
- "EnableNewFilterCard"
- "EnableNewQueryResults"
- "EnableQueryResultComparison"
- "EnableSharingFromSafariUI"
- "EnableThreadedMessagesInWidget"
- "Fatal error"
- "GenerativeModelsAvailability changed from: %s, to: %s"
- "GenerativeModelsAvailability changed to: %s, but was already: %s. Skipping availability-change notification"
- "Insufficient space allocated to copy string contents"
- "SearchFlagColors"
- "Setting user query with expression: %@ context: %@"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "TB,N,R"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_addPrecachedItems:"
- "_precachedItemsFromExtraInfo:"
- "categoryCloudStorage:didChangeLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:"
- "ef_preferredLanguageIdentifier"
- "filteredMessageListWithPredicate:ignoredMessagesPredicate:userFiltered:"
- "initWithMailboxes:repository:sortDescriptors:sectionPredicates:transformPredicate:ignoreMessageAdditionsPredicate:targetClass:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:labelPrefix:shouldShowBundle:"
- "invalid Collection: less than 'count' elements in collection"
- "isRestricted"
- "setIfNeededLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:"
- "simpleMessageListForMailboxes:withRepository:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:sortDescriptors:transformPredicate:ignoreMessageAdditionsPredicate:shouldShowBundle:"
- "threadedMessageListForMailboxes:withRepository:additionalQueryOptions:countOfItemsToPrecache:shouldUpdateDisplayDate:sortDescriptors:sectionPredicates:transformPredicate:ignoreMessageAdditionsPredicate:shouldShowBundle:"
- "v32@?0@\"<NSCopying>\"8@\"NSArray\"16^B24"

```
