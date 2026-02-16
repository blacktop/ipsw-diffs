## Email

> `/System/Library/PrivateFrameworks/Email.framework/Email`

```diff

-3864.400.21.0.0
-  __TEXT.__text: 0xce584
-  __TEXT.__auth_stubs: 0x14f0
-  __TEXT.__objc_methlist: 0xc974
-  __TEXT.__gcc_except_tab: 0x1b1c8
-  __TEXT.__const: 0x1238
-  __TEXT.__cstring: 0xb64c
-  __TEXT.__oslogstring: 0x6123
+3864.500.147.2.3
+  __TEXT.__text: 0xd92b0
+  __TEXT.__auth_stubs: 0x14d0
+  __TEXT.__objc_methlist: 0xcd74
+  __TEXT.__gcc_except_tab: 0x1b7bc
+  __TEXT.__const: 0x1240
+  __TEXT.__cstring: 0xb76c
+  __TEXT.__oslogstring: 0x6313
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__ustring: 0x154
+  __TEXT.__swift5_typeref: 0x385
   __TEXT.__constg_swiftt: 0x3e8
-  __TEXT.__swift5_typeref: 0x387
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_reflstr: 0x294
   __TEXT.__swift5_fieldmd: 0x3e0

   __TEXT.__swift5_capture: 0x38
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x7a90
-  __TEXT.__eh_frame: 0x1f8
-  __TEXT.__objc_classname: 0x1a4a
-  __TEXT.__objc_methname: 0x1b35a
-  __TEXT.__objc_methtype: 0x470e
-  __TEXT.__objc_stubs: 0x11da0
-  __DATA_CONST.__got: 0xca8
-  __DATA_CONST.__const: 0x4278
-  __DATA_CONST.__objc_classlist: 0x570
-  __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x330
+  __TEXT.__unwind_info: 0x8048
+  __TEXT.__eh_frame: 0x1b0
+  __TEXT.__objc_classname: 0x1b5b
+  __TEXT.__objc_methname: 0x1bd64
+  __TEXT.__objc_methtype: 0x4851
+  __TEXT.__objc_stubs: 0x12560
+  __DATA_CONST.__got: 0xc58
+  __DATA_CONST.__const: 0x4358
+  __DATA_CONST.__objc_classlist: 0x580
+  __DATA_CONST.__objc_catlist: 0x78
+  __DATA_CONST.__objc_protolist: 0x348
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5eb0
+  __DATA_CONST.__objc_selrefs: 0x60e0
   __DATA_CONST.__objc_protorefs: 0x118
-  __DATA_CONST.__objc_superrefs: 0x470
+  __DATA_CONST.__objc_superrefs: 0x480
   __DATA_CONST.__objc_arraydata: 0x1e8
-  __AUTH_CONST.__auth_got: 0xa88
-  __AUTH_CONST.__const: 0x1848
-  __AUTH_CONST.__cfstring: 0x9c00
-  __AUTH_CONST.__objc_const: 0x162f8
-  __AUTH_CONST.__objc_intobj: 0x360
+  __AUTH_CONST.__auth_got: 0xa78
+  __AUTH_CONST.__const: 0x18c8
+  __AUTH_CONST.__cfstring: 0x9fa0
+  __AUTH_CONST.__objc_const: 0x16bb0
+  __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x668
-  __AUTH.__data: 0x158
-  __DATA.__objc_ivar: 0xbdc
-  __DATA.__data: 0x28a8
-  __DATA.__bss: 0x1bb0
-  __DATA_DIRTY.__objc_data: 0x31b0
-  __DATA_DIRTY.__data: 0x1c0
-  __DATA_DIRTY.__bss: 0x850
+  __AUTH.__objc_data: 0x6b8
+  __AUTH.__data: 0x150
+  __DATA.__objc_ivar: 0xc2c
+  __DATA.__data: 0x2998
+  __DATA.__bss: 0x1ba0
+  __DATA_DIRTY.__objc_data: 0x3200
+  __DATA_DIRTY.__data: 0x1e0
+  __DATA_DIRTY.__bss: 0x888
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
+  - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures
   - /System/Library/PrivateFrameworks/CommunicationsFilter.framework/CommunicationsFilter
   - /System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B9F15F46-53D9-3B7A-A1B3-C5B3DAB174E4
-  Functions: 4762
-  Symbols:   17726
-  CStrings:  8418
+  UUID: 52628EAF-4871-31F6-A368-8362AC9C779E
+  Functions: 4857
+  Symbols:   18098
+  CStrings:  8592
 
Symbols:
+ +[EMMailSearchQueryBiomeLogger log]
+ +[EMMailSearchQueryBiomeLogger sharedInstance]
+ +[NSUserDefaults(Email) emLog]
+ +[NSUserDefaults(Email) emLog].cold.1
+ +[NSUserDefaults(Email) em_descriptionForRemoteContentOptions:]
+ -[BMMailSearchQuery(EMBiomeAdditions) ef_publicDescription]
+ -[BMPruner(EMBiomeAdditions) pruneAllLogs]
+ -[BMPruner(EMBiomeAdditions) pruneLogWithQueryString:]
+ -[CSSearchQueryContext(MailSessionID) em_setSessionID:queryID:]
+ -[CSSuggestion(EMBiomeAdditions) _biomeQueryStringFromCSSuggestionToken:]
+ -[CSSuggestion(EMBiomeAdditions) _biomeQueryStringFromQueryComponent:]
+ -[CSSuggestion(EMBiomeAdditions) _biomeTokenFromCSSuggestionToken:mailScope:]
+ -[CSSuggestion(EMBiomeAdditions) _queryComponentForTokenKind:itemSummary:]
+ -[CSSuggestion(EMBiomeAdditions) _wordCountForString:]
+ -[CSSuggestion(EMBiomeAdditions) em_biomeQueryString]
+ -[CSSuggestion(EMBiomeAdditions) em_biomeTokensWithMailScope:]
+ -[EMBiomeMessage .cxx_destruct]
+ -[EMBiomeMessage category]
+ -[EMBiomeMessage indexInSection]
+ -[EMBiomeMessage initWithMessageID:category:isTopHit:isInstantAnswer:indexInSection:]
+ -[EMBiomeMessage isInstantAnswer]
+ -[EMBiomeMessage isPrimary]
+ -[EMBiomeMessage isTopHit]
+ -[EMBiomeMessage messageID]
+ -[EMDaemonInterface connectionForProtocol:qosClass:]
+ -[EMFetchController fetchAllMessages:]
+ -[EMMailSearchQueryBiomeLogger .cxx_destruct]
+ -[EMMailSearchQueryBiomeLogger _abandonCurrentQueryWithReason:]
+ -[EMMailSearchQueryBiomeLogger _cleanupStateAfterLogging]
+ -[EMMailSearchQueryBiomeLogger _logStateToBiome:]
+ -[EMMailSearchQueryBiomeLogger _pruneAllBiomeLogs]
+ -[EMMailSearchQueryBiomeLogger _pruneBiomeLogForSuggestion:]
+ -[EMMailSearchQueryBiomeLogger _queryStringFromSuggestion:]
+ -[EMMailSearchQueryBiomeLogger initWithQueue:source:pruner:]
+ -[EMMailSearchQueryBiomeLogger init]
+ -[EMMailSearchQueryBiomeLogger pruneAllLogs]
+ -[EMMailSearchQueryBiomeLogger pruneLogForSuggestion:]
+ -[EMMailSearchQueryBiomeLogger pruner]
+ -[EMMailSearchQueryBiomeLogger queue]
+ -[EMMailSearchQueryBiomeLogger setPruner:]
+ -[EMMailSearchQueryBiomeLogger setQueue:]
+ -[EMMailSearchQueryBiomeLogger setSource:]
+ -[EMMailSearchQueryBiomeLogger setState:]
+ -[EMMailSearchQueryBiomeLogger source]
+ -[EMMailSearchQueryBiomeLogger state]
+ -[EMMailSearchQueryBiomeLogger trackAbandonmentWithReason:]
+ -[EMMailSearchQueryBiomeLogger trackCommittedQueryWithSuggestion:commitReason:]
+ -[EMMailSearchQueryBiomeLogger trackEngagementInSectionType:]
+ -[EMMailSearchQueryBiomeLogger trackResultViewDidChangeTo:]
+ -[EMMailSearchQueryBiomeLogger trackResultsReceivedResultCount:]
+ -[EMRemoteConnection _sendInvocation:withProxy:].cold.1
+ -[EMRemoteConnection initWithProtocol:proxyGenerator:qosClass:]
+ -[EMSearchQueryState .cxx_destruct]
+ -[EMSearchQueryState abandonedReason]
+ -[EMSearchQueryState canBeLogged]
+ -[EMSearchQueryState commitReason]
+ -[EMSearchQueryState engagedSectionType]
+ -[EMSearchQueryState hasResults]
+ -[EMSearchQueryState init]
+ -[EMSearchQueryState resultCount]
+ -[EMSearchQueryState resultEngaged]
+ -[EMSearchQueryState resultView]
+ -[EMSearchQueryState setAbandonedReason:]
+ -[EMSearchQueryState setCommitReason:]
+ -[EMSearchQueryState setEngagedSectionType:]
+ -[EMSearchQueryState setHasResults:]
+ -[EMSearchQueryState setResultCount:]
+ -[EMSearchQueryState setResultEngaged:]
+ -[EMSearchQueryState setResultView:]
+ -[EMSearchQueryState setSuggestion:]
+ -[EMSearchQueryState suggestion]
+ -[EMSearchableIndex startTurboMaildIndexer:]
+ -[EMSearchableIndex startTurboSearchIndexer:]
+ -[EMSearchableIndexQuery queryID]
+ -[EMSearchableIndexQuery sessionID]
+ -[EMSearchableIndexQuery setQueryID:]
+ -[EMSearchableIndexQuery setSessionID:]
+ -[EMSearchableIndexTopHitsQuery initWithSearchString:filterQueries:bundleID:keyboardLanguage:updatedSuggestion:generateSuggestions:logDescription:resultLimit:suggestionLimit:customFlags:feedbackQueryID:sessionID:queryID:]
+ _BMMailSearchQueryAbandonedReasonAsString
+ _BMMailSearchQueryResultViewAsString
+ _BMMailSearchQuerySectionTypeAsString
+ _BMMailSearchQueryStatusAsString
+ _BiomeLibrary
+ _EFGetElapsedTimeSinceAbsoluteTime.onceToken
+ _EFGetElapsedTimeSinceAbsoluteTime.sTimebaseInfo
+ _EMUserDefaultAutomationBucketOverride
+ _OBJC_CLASS_$_BMMailSearchQuery
+ _OBJC_CLASS_$_BMMailSearchUIEventToken
+ _OBJC_CLASS_$_BMPruner
+ _OBJC_CLASS_$_BMSource
+ _OBJC_CLASS_$_EMBiomeMessage
+ _OBJC_CLASS_$_EMMailSearchQueryBiomeLogger
+ _OBJC_CLASS_$_EMSearchQueryState
+ _OBJC_IVAR_$_EMBiomeMessage._category
+ _OBJC_IVAR_$_EMBiomeMessage._indexInSection
+ _OBJC_IVAR_$_EMBiomeMessage._isInstantAnswer
+ _OBJC_IVAR_$_EMBiomeMessage._isTopHit
+ _OBJC_IVAR_$_EMBiomeMessage._messageID
+ _OBJC_IVAR_$_EMMailSearchQueryBiomeLogger._pruner
+ _OBJC_IVAR_$_EMMailSearchQueryBiomeLogger._queue
+ _OBJC_IVAR_$_EMMailSearchQueryBiomeLogger._source
+ _OBJC_IVAR_$_EMMailSearchQueryBiomeLogger._state
+ _OBJC_IVAR_$_EMRemoteConnection._syncXPCInProgress
+ _OBJC_IVAR_$_EMSearchQueryState._abandonedReason
+ _OBJC_IVAR_$_EMSearchQueryState._commitReason
+ _OBJC_IVAR_$_EMSearchQueryState._engagedSectionType
+ _OBJC_IVAR_$_EMSearchQueryState._hasResults
+ _OBJC_IVAR_$_EMSearchQueryState._resultCount
+ _OBJC_IVAR_$_EMSearchQueryState._resultEngaged
+ _OBJC_IVAR_$_EMSearchQueryState._resultView
+ _OBJC_IVAR_$_EMSearchQueryState._suggestion
+ _OBJC_IVAR_$_EMSearchableIndexQuery._queryID
+ _OBJC_IVAR_$_EMSearchableIndexQuery._sessionID
+ _OBJC_METACLASS_$_EMBiomeMessage
+ _OBJC_METACLASS_$_EMMailSearchQueryBiomeLogger
+ _OBJC_METACLASS_$_EMSearchQueryState
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ __OBJC_$_CATEGORY_BMMailSearchQuery_$_EMBiomeAdditions
+ __OBJC_$_CATEGORY_BMPruner_$_EMBiomeAdditions
+ __OBJC_$_CATEGORY_BMSource_$_EMBiomeAdditions
+ __OBJC_$_CATEGORY_CSSearchQueryContext_$_MailSessionID
+ __OBJC_$_CATEGORY_CSSuggestion_$_EMBiomeAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_BMMailSearchQuery_$_EMBiomeAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_BMPruner_$_EMBiomeAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CSSearchQueryContext_$_MailSessionID
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CSSuggestion_$_EMBiomeAdditions
+ __OBJC_$_CLASS_METHODS_EMMailSearchQueryBiomeLogger
+ __OBJC_$_CLASS_PROP_LIST_EMMailSearchQueryBiomeLogger
+ __OBJC_$_INSTANCE_METHODS_EMBiomeMessage
+ __OBJC_$_INSTANCE_METHODS_EMMailSearchQueryBiomeLogger
+ __OBJC_$_INSTANCE_METHODS_EMSearchQueryState
+ __OBJC_$_INSTANCE_VARIABLES_EMBiomeMessage
+ __OBJC_$_INSTANCE_VARIABLES_EMMailSearchQueryBiomeLogger
+ __OBJC_$_INSTANCE_VARIABLES_EMSearchQueryState
+ __OBJC_$_PROP_LIST_BMMailSearchQuery_$_EMBiomeAdditions
+ __OBJC_$_PROP_LIST_BMPruner_$_EMBiomeAdditions
+ __OBJC_$_PROP_LIST_BMSource_$_EMBiomeAdditions
+ __OBJC_$_PROP_LIST_CSSuggestion_$_EMBiomeAdditions
+ __OBJC_$_PROP_LIST_EMBiomeMessage
+ __OBJC_$_PROP_LIST_EMMailSearchQueryBiomeLogger
+ __OBJC_$_PROP_LIST_EMSearchQueryState
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_EMBiomeStreamSearchQueryPruner
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_EMBiomeStreamSearchQuerySource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_EMBiomeSuggestion
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EMBiomeStreamSearchQueryPruner
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EMBiomeStreamSearchQuerySource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EMBiomeSuggestion
+ __OBJC_$_PROTOCOL_REFS_EMBiomeStreamSearchQueryPruner
+ __OBJC_$_PROTOCOL_REFS_EMBiomeStreamSearchQuerySource
+ __OBJC_$_PROTOCOL_REFS_EMBiomeSuggestion
+ __OBJC_CATEGORY_PROTOCOLS_$_BMMailSearchQuery_$_EMBiomeAdditions
+ __OBJC_CATEGORY_PROTOCOLS_$_BMPruner_$_EMBiomeAdditions
+ __OBJC_CATEGORY_PROTOCOLS_$_BMSource_$_EMBiomeAdditions
+ __OBJC_CATEGORY_PROTOCOLS_$_CSSuggestion_$_EMBiomeAdditions
+ __OBJC_CLASS_PROTOCOLS_$_EMMailSearchQueryBiomeLogger
+ __OBJC_CLASS_RO_$_EMBiomeMessage
+ __OBJC_CLASS_RO_$_EMMailSearchQueryBiomeLogger
+ __OBJC_CLASS_RO_$_EMSearchQueryState
+ __OBJC_LABEL_PROTOCOL_$_EMBiomeStreamSearchQueryPruner
+ __OBJC_LABEL_PROTOCOL_$_EMBiomeStreamSearchQuerySource
+ __OBJC_LABEL_PROTOCOL_$_EMBiomeSuggestion
+ __OBJC_METACLASS_RO_$_EMBiomeMessage
+ __OBJC_METACLASS_RO_$_EMMailSearchQueryBiomeLogger
+ __OBJC_METACLASS_RO_$_EMSearchQueryState
+ __OBJC_PROTOCOL_$_EMBiomeStreamSearchQueryPruner
+ __OBJC_PROTOCOL_$_EMBiomeStreamSearchQuerySource
+ __OBJC_PROTOCOL_$_EMBiomeSuggestion
+ ___221-[EMSearchableIndexTopHitsQuery initWithSearchString:filterQueries:bundleID:keyboardLanguage:updatedSuggestion:generateSuggestions:logDescription:resultLimit:suggestionLimit:customFlags:feedbackQueryID:sessionID:queryID:]_block_invoke
+ ___221-[EMSearchableIndexTopHitsQuery initWithSearchString:filterQueries:bundleID:keyboardLanguage:updatedSuggestion:generateSuggestions:logDescription:resultLimit:suggestionLimit:customFlags:feedbackQueryID:sessionID:queryID:]_block_invoke.102
+ ___30+[NSUserDefaults(Email) emLog]_block_invoke
+ ___35+[EMMailSearchQueryBiomeLogger log]_block_invoke
+ ___36-[EMMailSearchQueryBiomeLogger init]_block_invoke
+ ___42-[BMPruner(EMBiomeAdditions) pruneAllLogs]_block_invoke
+ ___44-[EMMailSearchQueryBiomeLogger pruneAllLogs]_block_invoke
+ ___45-[EMDaemonInterface resetProtocolConnections]_block_invoke.330
+ ___46+[EMMailSearchQueryBiomeLogger sharedInstance]_block_invoke
+ ___48-[EMRemoteConnection _sendInvocation:withProxy:]_block_invoke.76.cold.1
+ ___48-[EMRemoteConnection _sendInvocation:withProxy:]_block_invoke.76.cold.2
+ ___48-[EMRemoteConnection _sendInvocation:withProxy:]_block_invoke.cold.1
+ ___50-[EMDaemonInterface _connectionForProtocol:error:]_block_invoke.327
+ ___54-[BMPruner(EMBiomeAdditions) pruneLogWithQueryString:]_block_invoke
+ ___54-[CSSuggestion(EMBiomeAdditions) _wordCountForString:]_block_invoke
+ ___54-[EMMailSearchQueryBiomeLogger pruneLogForSuggestion:]_block_invoke
+ ___57-[EMSearchableIndexUserQuery initWithExpression:builder:]_block_invoke.496
+ ___59-[EMMailSearchQueryBiomeLogger trackAbandonmentWithReason:]_block_invoke
+ ___59-[EMMailSearchQueryBiomeLogger trackResultViewDidChangeTo:]_block_invoke
+ ___59-[EMMailSearchQueryBiomeLogger trackResultViewDidChangeTo:]_block_invoke.cold.1
+ ___61-[EMMailSearchQueryBiomeLogger trackEngagementInSectionType:]_block_invoke
+ ___64-[EMMailSearchQueryBiomeLogger trackResultsReceivedResultCount:]_block_invoke
+ ___64-[EMMailSearchQueryBiomeLogger trackResultsReceivedResultCount:]_block_invoke.cold.1
+ ___79-[EMMailSearchQueryBiomeLogger trackCommittedQueryWithSuggestion:commitReason:]_block_invoke
+ ___EFGetElapsedTimeSinceAbsoluteTime_block_invoke
+ ___block_descriptor_32_e26_B24?0"BMStoreEvent"8^B16l
+ ___block_descriptor_32_e35_B24?0"NSString"8"NSDictionary"16l
+ ___block_descriptor_40_ea8_32s_e26_B24?0"BMStoreEvent"8^B16ls32l8
+ ___block_descriptor_44_ea8_32s_e5_v8?0ls32l8
+ ___block_literal_global.118
+ ___block_literal_global.332
+ ___block_literal_global.419
+ ___block_literal_global.422
+ ___block_literal_global.471
+ ___block_literal_global.66
+ _dispatch_block_create
+ _emLog.log
+ _emLog.onceToken
+ _get_type_metadata 15Synchronization5MutexVy5Email21ActivityStateObserverC0E0OG noncopyable.24
+ _mach_absolute_time
+ _mach_timebase_info
+ _objc_msgSend$Mail
+ _objc_msgSend$Query
+ _objc_msgSend$Search
+ _objc_msgSend$_abandonCurrentQueryWithReason:
+ _objc_msgSend$_biomeQueryStringFromCSSuggestionToken:
+ _objc_msgSend$_biomeQueryStringFromQueryComponent:
+ _objc_msgSend$_biomeTokenFromCSSuggestionToken:mailScope:
+ _objc_msgSend$_cleanupStateAfterLogging
+ _objc_msgSend$_logStateToBiome:
+ _objc_msgSend$_pruneAllBiomeLogs
+ _objc_msgSend$_pruneBiomeLogForSuggestion:
+ _objc_msgSend$_queryComponentForTokenKind:itemSummary:
+ _objc_msgSend$_queryStringFromSuggestion:
+ _objc_msgSend$_wordCountForString:
+ _objc_msgSend$abandonedReason
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$canBeLogged
+ _objc_msgSend$componentsSeparatedByCharactersInSet:
+ _objc_msgSend$connectionForProtocol:qosClass:
+ _objc_msgSend$currentLocale
+ _objc_msgSend$deleteWithPolicy:eventsPassingTest:
+ _objc_msgSend$displayText
+ _objc_msgSend$emLog
+ _objc_msgSend$em_biomeQueryString
+ _objc_msgSend$em_descriptionForRemoteContentOptions:
+ _objc_msgSend$em_setSessionID:queryID:
+ _objc_msgSend$engagedSectionType
+ _objc_msgSend$eventBody
+ _objc_msgSend$fetchAllMessages:
+ _objc_msgSend$hasHasResults
+ _objc_msgSend$hasResultEngaged
+ _objc_msgSend$hasResults
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithInt:
+ _objc_msgSend$initWithProtocol:proxyGenerator:qosClass:
+ _objc_msgSend$initWithQueryString:queryStatus:hasResults:resultView:resultEngaged:resultEngagedSectionType:abandonedReason:
+ _objc_msgSend$initWithWordCount:charCount:queryComponent:mailScope:
+ _objc_msgSend$isPrimary
+ _objc_msgSend$itemSummary
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$pruneAllLogs
+ _objc_msgSend$pruneLogWithQueryString:
+ _objc_msgSend$pruner
+ _objc_msgSend$queryID
+ _objc_msgSend$queue
+ _objc_msgSend$registerActivityObserver:
+ _objc_msgSend$removeObserver:forKeyPath:context:
+ _objc_msgSend$resultEngaged
+ _objc_msgSend$resultEngagedSectionType
+ _objc_msgSend$resultView
+ _objc_msgSend$sendEvent:
+ _objc_msgSend$sessionID
+ _objc_msgSend$setAbandonedReason:
+ _objc_msgSend$setCommitReason:
+ _objc_msgSend$setEngagedSectionType:
+ _objc_msgSend$setHasResults:
+ _objc_msgSend$setLocalizedDateFormatFromTemplate:
+ _objc_msgSend$setPruner:
+ _objc_msgSend$setResultCount:
+ _objc_msgSend$setResultEngaged:
+ _objc_msgSend$setResultView:
+ _objc_msgSend$setState:
+ _objc_msgSend$source
+ _objc_msgSend$startTurboMaildIndexer:
+ _objc_msgSend$startTurboSearchIndexer:
+ _objc_msgSend$suggestionTokens
+ _objc_msgSend$textScope
+ _objc_msgSend$tokenKind
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
+ _sharedInstance.sharedInstance
- +[EMMessageIDRandomizer _createRandomizedStringForMessageID:]
- +[EMMessageIDRandomizer _createRandomizedStringForMessageID:].cold.1
- +[EMMessageIDRandomizer _deleteExpiredStringForMessageID:]
- +[EMMessageIDRandomizer _deleteExpiredStringForMessageID:].cold.1
- +[EMMessageIDRandomizer _findExistingStringError:messageID:]
- +[EMMessageIDRandomizer _findOrCreateRandomizedStringForMessageID:]
- +[EMMessageIDRandomizer _queryKeychainError:messageID:]
- +[EMMessageIDRandomizer _queryKeychainError:messageID:].cold.1
- +[EMMessageIDRandomizer log]
- +[EMMessageIDRandomizer randomizedStringForGlobalMessageID:]
- +[EMMessageIDRandomizer randomizedStringForGlobalMessageID:].cold.1
- -[EMMessageIDRandomizer init]
- -[EMRemoteConnection initWithProtocol:proxyGenerator:]
- -[EMSearchableIndexTopHitsQuery initWithSearchString:filterQueries:bundleID:keyboardLanguage:updatedSuggestion:generateSuggestions:logDescription:resultLimit:suggestionLimit:customFlags:feedbackQueryID:]
- _CFAutorelease
- _EFDeviceUnlockedSinceBoot
- _EMPersistenceStatisticsKeyMessagesToReindex
- _EMUserDefaultDropToChangeCategories
- _NSOSStatusErrorDomain
- _OBJC_CLASS_$_EMMessageIDRandomizer
- _OBJC_METACLASS_$_EMMessageIDRandomizer
- _SecItemAdd
- _SecItemCopyMatching
- _SecItemDelete
- __OBJC_$_CLASS_METHODS_EMMessageIDRandomizer
- __OBJC_$_CLASS_PROP_LIST_EMMessageIDRandomizer
- __OBJC_$_INSTANCE_METHODS_EMMessageIDRandomizer
- __OBJC_$_PROP_LIST_EMMessageIDRandomizer
- __OBJC_CLASS_PROTOCOLS_$_EMMessageIDRandomizer
- __OBJC_CLASS_RO_$_EMMessageIDRandomizer
- __OBJC_METACLASS_RO_$_EMMessageIDRandomizer
- ___203-[EMSearchableIndexTopHitsQuery initWithSearchString:filterQueries:bundleID:keyboardLanguage:updatedSuggestion:generateSuggestions:logDescription:resultLimit:suggestionLimit:customFlags:feedbackQueryID:]_block_invoke
- ___203-[EMSearchableIndexTopHitsQuery initWithSearchString:filterQueries:bundleID:keyboardLanguage:updatedSuggestion:generateSuggestions:logDescription:resultLimit:suggestionLimit:customFlags:feedbackQueryID:]_block_invoke.102
- ___28+[EMMessageIDRandomizer log]_block_invoke
- ___45-[EMDaemonInterface resetProtocolConnections]_block_invoke.327
- ___50-[EMDaemonInterface _connectionForProtocol:error:]_block_invoke.324
- ___57-[EMSearchableIndexUserQuery initWithExpression:builder:]_block_invoke.486
- ___block_literal_global.119
- ___block_literal_global.329
- ___block_literal_global.418
- ___block_literal_global.466
- ___block_literal_global.65
- _get_type_metadata 15Synchronization5MutexVy5Email21ActivityStateObserverC0E0OG.24
- _kSecAttrAccessGroup
- _kSecAttrAccessible
- _kSecAttrAccessibleAfterFirstUnlock
- _kSecAttrCreationDate
- _kSecAttrIsInvisible
- _kSecAttrService
- _kSecClass
- _kSecClassGenericPassword
- _kSecMatchLimit
- _kSecReturnAttributes
- _kSecReturnData
- _kSecValueData
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_createRandomizedStringForMessageID:
- _objc_msgSend$_deleteExpiredStringForMessageID:
- _objc_msgSend$_findExistingStringError:messageID:
- _objc_msgSend$_findOrCreateRandomizedStringForMessageID:
- _objc_msgSend$_queryKeychainError:messageID:
- _objc_msgSend$connectionForProtocol:
- _objc_msgSend$initWithProtocol:proxyGenerator:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ "%ld (%@)"
+ "%{public}@: Attempting to dispatch async message (selector: %{public}@) while synchronous XPC call is in progress on serial queue. This async message may never execute."
+ "%{public}@: SLOW synchronous XPC operation for selector: %{public}@ took %.2f seconds"
+ "%{public}@: asyncInvocation is nil, cannot invoke XPC call"
+ "%{public}@: asyncProxy is nil, cannot invoke XPC call for selector: %{public}@"
+ ".none"
+ ".requiringUserAction"
+ ".setByUser"
+ ".withoutProxy"
+ ".withoutSyntheticRequests"
+ "<%@ %p queryString:%@ queryStatus:%@ hasResults:%@ resultView:%@ resultEngaged:%@ resultEngagedSectionType:%@ abandonedReason:%@>"
+ "@\"<EMBiomeStreamSearchQueryPruner>\""
+ "@\"<EMBiomeStreamSearchQuerySource>\""
+ "@\"<EMBiomeSuggestion>\""
+ "@\"EMSearchQueryState\""
+ "@116@0:8@16@24@32@40@48B56@60Q68Q76@84q92@100@108"
+ "@28@0:8@16i24"
+ "@36@0:8@16@24I32"
+ "@48@0:8@16@24B32B36Q40"
+ "All logs pruned"
+ "AutomationBucketOverride"
+ "B24@?0@\"BMStoreEvent\"8^B16"
+ "B24@?0@\"NSString\"8@\"NSDictionary\"16"
+ "BiomeSearchQuery"
+ "Donated search query to Biome: %{public}@"
+ "Donation disabled by feature flag Mail/BiomeSearchQuery for: %{public}@"
+ "EMBiomeAdditions"
+ "EMBiomeMessage"
+ "EMBiomeStreamSearchQueryPruner"
+ "EMBiomeStreamSearchQuerySource"
+ "EMBiomeSuggestion"
+ "EMMailSearchQueryBiomeLogger"
+ "EMSearchQueryState"
+ "EMUserDefaults"
+ "Logs pruned for suggestion <%{public}p>"
+ "MailSessionID"
+ "Query"
+ "QueryComponentAttachment"
+ "QueryComponentCP"
+ "QueryComponentCd"
+ "QueryComponentCft"
+ "QueryComponentCm"
+ "QueryComponentCr"
+ "QueryComponentCs"
+ "QueryComponentDate"
+ "QueryComponentFlag"
+ "QueryComponentFlagColor"
+ "QueryComponentFreeText"
+ "QueryComponentOther"
+ "QueryComponentPeople"
+ "QueryComponentReadStatus"
+ "QueryComponentSenderContains"
+ "QueryComponentSubject"
+ "QueryComponentSubjectContains"
+ "QueryComponentUnknown"
+ "QueryComponentUserTyped"
+ "Setting EMUserDefaultLoadRemoteContentKey to %{public}@ (isEnabled=%d)"
+ "Skipping committed query since we're already tracking the same query"
+ "T@\"<EMBiomeStreamSearchQueryPruner>\",&,N,V_pruner"
+ "T@\"<EMBiomeStreamSearchQuerySource>\",&,N,V_source"
+ "T@\"<EMBiomeSuggestion>\",&,N,V_suggestion"
+ "T@\"EMCategory\",R,N,V_category"
+ "T@\"EMMailSearchQueryBiomeLogger\",R,N"
+ "T@\"EMSearchQueryState\",&,N,V_state"
+ "T@\"EMSearchableMessageID\",R,C,N,V_messageID"
+ "T@\"NSNumber\",&,N,V_resultCount"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@\"NSString\",C,N,V_queryID"
+ "T@\"NSString\",C,N,V_sessionID"
+ "TB,N,V_hasResults"
+ "TB,N,V_resultEngaged"
+ "TB,R,N,V_isInstantAnswer"
+ "TB,R,N,V_isTopHit"
+ "TQ,R,N,V_indexInSection"
+ "Ti,N,V_abandonedReason"
+ "Ti,N,V_engagedSectionType"
+ "Ti,N,V_resultView"
+ "Tq,N,V_commitReason"
+ "Tracking committed query commitReason=%ld"
+ "Tracking resultView=%@"
+ "Tracking results resultCount=%lu"
+ "[%@: %@]"
+ "_abandonCurrentQueryWithReason:"
+ "_abandonedReason"
+ "_biomeQueryStringFromCSSuggestionToken:"
+ "_biomeQueryStringFromQueryComponent:"
+ "_biomeTokenFromCSSuggestionToken:mailScope:"
+ "_cleanupStateAfterLogging"
+ "_commitReason"
+ "_engagedSectionType"
+ "_hasResults"
+ "_indexInSection"
+ "_isInstantAnswer"
+ "_isTopHit"
+ "_logStateToBiome:"
+ "_messageID"
+ "_pruneAllBiomeLogs"
+ "_pruneBiomeLogForSuggestion:"
+ "_pruner"
+ "_queryComponentForTokenKind:itemSummary:"
+ "_queryID"
+ "_queryStringFromSuggestion:"
+ "_resultCount"
+ "_resultEngaged"
+ "_resultView"
+ "_sessionID"
+ "_syncXPCInProgress"
+ "_wordCountForString:"
+ "abandonedReason"
+ "canBeLogged"
+ "com.apple.mail.biome.search-query"
+ "commitReason"
+ "componentsSeparatedByCharactersInSet:"
+ "connectionForProtocol:qosClass:"
+ "deleteWithPolicy:eventsPassingTest:"
+ "displayText"
+ "emLog"
+ "em_biomeQueryString"
+ "em_biomeTokensWithMailScope:"
+ "em_descriptionForRemoteContentOptions:"
+ "em_setSessionID:queryID:"
+ "engagedSectionType"
+ "eventBody"
+ "fetchAllMessages:"
+ "hasHasResults"
+ "hasResultEngaged"
+ "hasResults"
+ "i32@0:8q16@24"
+ "iCloud Mail will send a message from %@ to unsubscribe from this sender. Any future updates and promotions from this email address will be automatically moved to Trash.\n\nReview and manage in iCloud settings."
+ "iCloud Mail will unsubscribe using information provided by the sender. Any future updates and promotions from this email address will be automatically moved to Trash.\n\nReview and manage in iCloud settings."
+ "indexInSection"
+ "initWithMessageID:category:isTopHit:isInstantAnswer:indexInSection:"
+ "initWithProtocol:proxyGenerator:qosClass:"
+ "initWithQueryString:queryStatus:hasResults:resultView:resultEngaged:resultEngagedSectionType:abandonedReason:"
+ "initWithQueue:source:pruner:"
+ "initWithSearchString:filterQueries:bundleID:keyboardLanguage:updatedSuggestion:generateSuggestions:logDescription:resultLimit:suggestionLimit:customFlags:feedbackQueryID:sessionID:queryID:"
+ "initWithWordCount:charCount:queryComponent:mailScope:"
+ "isInstantAnswer"
+ "isTopHit"
+ "itemSummary"
+ "n/a"
+ "predicateWithBlock:"
+ "pruneAllLogs"
+ "pruneLogForSuggestion:"
+ "pruneLogWithQueryString:"
+ "pruner"
+ "queryID"
+ "resultCount"
+ "resultEngaged"
+ "resultEngagedSectionType"
+ "resultView"
+ "search-suggestion-deleted"
+ "sendEvent:"
+ "sessionID"
+ "setAbandonedReason:"
+ "setCommitReason:"
+ "setEngagedSectionType:"
+ "setHasResults:"
+ "setPruner:"
+ "setQueryID:"
+ "setQueue:"
+ "setResultCount:"
+ "setResultEngaged:"
+ "setResultView:"
+ "setSessionID:"
+ "startTurboMaildIndexer:"
+ "startTurboSearchIndexer:"
+ "suggestionTokens"
+ "textScope"
+ "tokenKind"
+ "trackAbandonmentWithReason:"
+ "trackCommittedQueryWithSuggestion:commitReason:"
+ "trackEngagementInSectionType:"
+ "trackResultViewDidChangeTo:"
+ "trackResultsReceivedResultCount:"
+ "v24@0:8@\"<BMStoreData>\"16"
+ "whitespaceAndNewlineCharacterSet"
+ "|"
+ "\xa1"
- "@100@0:8@16@24@32@40@48B56@60Q68Q76@84q92"
- "@32@0:8o^@16q24"
- "Could not generate randomized string. Device unlocked since boot: %@"
- "DropToChangeCategories"
- "EMMessageIDRandomizer"
- "Error creating new randomized string: %d"
- "Error deleting expired randomized string: %d"
- "Error finding existing randomized string: %d"
- "No randomized string found"
- "UnifiedMessageList"
- "Will create new randomized string for messageID %lld"
- "Will delete expired randomized string"
- "_createRandomizedStringForMessageID:"
- "_deleteExpiredStringForMessageID:"
- "_findExistingStringError:messageID:"
- "_findOrCreateRandomizedStringForMessageID:"
- "_queryKeychainError:messageID:"
- "com.apple.mail.categories"
- "iCloud Mail will send a message from %@ to unsubscribe from this sender. Any future updates and promotions from this email address will be automatically moved to Trash.\n\nReview and manage in iCloud Settings."
- "iCloud Mail will unsubscribe using information provided by the sender. Any future updates and promotions from this email address will be automatically moved to Trash.\n\nReview and manage in iCloud Settings."
- "initWithProtocol:proxyGenerator:"
- "initWithSearchString:filterQueries:bundleID:keyboardLanguage:updatedSuggestion:generateSuggestions:logDescription:resultLimit:suggestionLimit:customFlags:feedbackQueryID:"
- "messagesToReindex"
- "randomizedStringForGlobalMessageID:"
- "\x91"

```
