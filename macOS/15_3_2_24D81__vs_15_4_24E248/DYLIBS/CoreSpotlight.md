## CoreSpotlight

> `/System/Library/Frameworks/CoreSpotlight.framework/Versions/A/CoreSpotlight`

```diff

-2328.7.8.7.0
-  __TEXT.__text: 0xdecac
-  __TEXT.__auth_stubs: 0x1ed0
-  __TEXT.__objc_methlist: 0xc14c
-  __TEXT.__const: 0xb52
-  __TEXT.__gcc_except_tab: 0x2f48
-  __TEXT.__cstring: 0x11bb2
-  __TEXT.__oslogstring: 0x6b10
+2333.22.13.7.0
+  __TEXT.__text: 0xe08f0
+  __TEXT.__auth_stubs: 0x1ee0
+  __TEXT.__objc_methlist: 0xc870
+  __TEXT.__const: 0xbb2
+  __TEXT.__gcc_except_tab: 0x2f9c
+  __TEXT.__cstring: 0x11fe2
+  __TEXT.__oslogstring: 0x6cd7
   __TEXT.__dlopen_cstrs: 0x365
   __TEXT.__ustring: 0x2c
   __TEXT.__swift5_typeref: 0x2a0

   __TEXT.__swift5_capture: 0x10c
   __TEXT.__swift5_proto: 0x54
   __TEXT.__swift5_types: 0x28
+  __TEXT.__swift_as_entry: 0x24
+  __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x3370
+  __TEXT.__unwind_info: 0x34e8
   __TEXT.__eh_frame: 0x1e8
-  __TEXT.__objc_classname: 0xfbb
-  __TEXT.__objc_methname: 0x1cac7
-  __TEXT.__objc_methtype: 0x205c
-  __TEXT.__objc_stubs: 0xf9e0
-  __DATA_CONST.__got: 0x798
-  __DATA_CONST.__const: 0x3420
-  __DATA_CONST.__objc_classlist: 0x450
-  __DATA_CONST.__objc_catlist: 0x38
+  __TEXT.__objc_classname: 0x100d
+  __TEXT.__objc_methname: 0x1d4be
+  __TEXT.__objc_methtype: 0x20ea
+  __TEXT.__objc_stubs: 0xfe60
+  __DATA_CONST.__got: 0x7a8
+  __DATA_CONST.__const: 0x3578
+  __DATA_CONST.__objc_classlist: 0x468
+  __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x73b0
+  __DATA_CONST.__objc_selrefs: 0x7610
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x328
-  __DATA_CONST.__objc_arraydata: 0xab0
-  __AUTH_CONST.__auth_got: 0xf78
-  __AUTH_CONST.__const: 0x3608
-  __AUTH_CONST.__cfstring: 0x10f40
-  __AUTH_CONST.__objc_const: 0x124f8
-  __AUTH_CONST.__objc_intobj: 0x708
-  __AUTH_CONST.__objc_arrayobj: 0x978
-  __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH.__objc_data: 0x14a0
+  __DATA_CONST.__objc_superrefs: 0x340
+  __DATA_CONST.__objc_arraydata: 0xb88
+  __AUTH_CONST.__auth_got: 0xf80
+  __AUTH_CONST.__const: 0x36b8
+  __AUTH_CONST.__cfstring: 0x11340
+  __AUTH_CONST.__objc_const: 0x12660
+  __AUTH_CONST.__objc_intobj: 0x750
+  __AUTH_CONST.__objc_doubleobj: 0x90
+  __AUTH_CONST.__objc_dictobj: 0xc8
+  __AUTH_CONST.__objc_arrayobj: 0x9c0
+  __AUTH.__objc_data: 0x1590
   __AUTH.__data: 0x3a0
-  __DATA.__objc_ivar: 0xb34
+  __DATA.__objc_ivar: 0xbb0
   __DATA.__data: 0xa30
-  __DATA.__bss: 0x12a0
+  __DATA.__bss: 0x1320
   __DATA.__common: 0xc
   __DATA_DIRTY.__objc_data: 0x1680
-  __DATA_DIRTY.__data: 0x58
-  __DATA_DIRTY.__bss: 0x6fd8
+  __DATA_DIRTY.__data: 0x60
+  __DATA_DIRTY.__bss: 0x7440
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 28AE3FE5-0310-30C8-8E44-D8EAB5BDB25D
-  Functions: 5380
-  Symbols:   11855
-  CStrings:  11485
+  UUID: 17EA1B88-EF9D-335C-8C38-CA6C87A94773
+  Functions: 5537
+  Symbols:   12148
+  CStrings:  11682
 
Symbols:
+ +[CSAttributeEvaluator enumerateTokensForString:locale:options:withHandler:].cold.1
+ +[CSCoder encodeURL:withSandboxExtensionData:]
+ +[CSContactsWrapper sharedInstance].cold.1
+ +[CSCustomAttributeKey _keyNameIsValid:].cold.1
+ +[CSDeviceListener sharedListener].cold.1
+ +[CSGenerativeModelsAvailabilityManager sharedInstance]
+ +[CSImporter sharedImporterForUser:].cold.1
+ +[CSInstantAnswers commonStopWords].cold.1
+ +[CSInstantAnswers commonTriggerPhrases].cold.1
+ +[CSInstantAnswers flightIntentTokens].cold.1
+ +[CSInstantAnswers flightStopWords].cold.1
+ +[CSInstantAnswers flightTriggerPhrases].cold.1
+ +[CSInstantAnswers hotelIntentTokens].cold.1
+ +[CSInstantAnswers hotelStopWords].cold.1
+ +[CSInstantAnswers hotelTriggerPhrases].cold.1
+ +[CSInstantAnswers noInstantAnswersQueries].cold.1
+ +[CSInstantAnswers overrideTokens].cold.1
+ +[CSIntentsWrapper sharedInstance].cold.1
+ +[CSPersonalAnswers attributeIntentsFromQU:].cold.1
+ +[CSPersonalAnswers fetchAttributes].cold.1
+ +[CSPersonalAnswersUtils getCategoryAttributeMap].cold.1
+ +[CSQueryResultMatchingHint _snippetHintAttributeSet].cold.1
+ +[CSSearchConnection sharedCSUserFSConnection].cold.1
+ +[CSSearchConnection sharedSearchConnection].cold.1
+ +[CSSearchQueryContext pommesSupportedBundleIDs].cold.1
+ +[CSSearchableIndex defaultSearchableIndex].cold.1
+ +[CSSearchableIndex fetchAttributesFromImportFileURL:bundleID:fileType:identifier:sandboxExtension:attributesWithCompletionHandler:]
+ +[CSSearchableIndex fetchFile:attributesWithSandbox:completionHandler:]
+ +[CSSearchableIndex fetchFile:attributesWithSandbox:completionHandler:].cold.1
+ +[CSSearchableIndex mainBundleID].cold.1
+ +[CSSearchableIndex mainBundleLocalizedString].cold.1
+ +[CSSearchableIndex(InternalSPI) allSupportedProtectionClasses].cold.1
+ +[CSSearchableItemAttributeSet _allKeys].cold.1
+ +[CSSearchableItemAttributeSet _requiredAttributesForContentType:].cold.1
+ +[CSSuggestion noreplyTemplates].cold.1
+ +[CSUnhousedIndexConnection unhousedIndexConnectionForToken:].cold.2
+ +[CSUserQuery mailResources].cold.1
+ +[CSUserQuery(CSSuggestionBlending) computeScoreForNameUnigrams:queryUnigrams:queryString:locale:isContactsSuggestion:].cold.1
+ +[CSUserQuery(CSSuggestionBlending) emailSpecialChars].cold.1
+ +[_CSContactSearch autocompleteStore].cold.1
+ +[_CSContactSearch contactStore].cold.1
+ +[_CSContactSearch targetQueue].cold.1
+ +[_MDExtensionContext _extensionAuxiliaryHostProtocol].cold.1
+ +[_MDExtensionContext _extensionAuxiliaryVendorProtocol].cold.1
+ +[_MDImportExtensionLoader _matchDictionary].cold.1
+ +[_MDImportExtensionManager sharedManager].cold.1
+ +[_MDIndexExtensionLoader _matchDictionary].cold.1
+ +[_MDIndexExtensionManager sharedManager].cold.1
+ -[CSDateTag initWithDate:confidence:].cold.1
+ -[CSDeviceListener init].cold.1
+ -[CSFilesSearchQuery handleCompletion:]
+ -[CSFilesSearchQuery handleGatherEnded]
+ -[CSGenerativeModelsAvailabilityManager .cxx_destruct]
+ -[CSGenerativeModelsAvailabilityManager _isAvailableForUseCaseIdentifiers:]
+ -[CSGenerativeModelsAvailabilityManager dealloc]
+ -[CSGenerativeModelsAvailabilityManager init]
+ -[CSGenerativeModelsAvailabilityManager init].cold.1
+ -[CSGenerativeModelsAvailabilityManager isPhotosSemanticSearchAvailable]
+ -[CSGenerativeModelsAvailabilityManager isSemanticSearchAvailable]
+ -[CSGenerativeModelsAvailabilityManager isTextPersonExtractionAvailable]
+ -[CSGenerativeModelsAvailabilityManager setUseCaseStatus:]
+ -[CSGenerativeModelsAvailabilityManager useCaseStatus]
+ -[CSIndexExtensionRequestHandler searchableItemsDidUpdate:]
+ -[CSIndexExtensionRequestHandler searchableItemsDidUpdate:].cold.1
+ -[CSIndexExtensionRequestHandler searchableItemsForIdentifiers:searchableItemsHandler:]
+ -[CSIndexExtensionRequestHandler searchableItemsForIdentifiers:searchableItemsHandler:].cold.1
+ -[CSLocationTag .cxx_destruct]
+ -[CSLocationTag country]
+ -[CSLocationTag initWithLocation:parent:country:lat:lng:confidence:]
+ -[CSLocationTag location]
+ -[CSLocationTag parent]
+ -[CSRankingConfiguration .cxx_destruct]
+ -[CSRankingConfiguration bundleIDs]
+ -[CSRankingConfiguration enableExtendedEmbeddingTimeout]
+ -[CSRankingConfiguration enablePommesRanking]
+ -[CSRankingConfiguration enablePommesSuggestions]
+ -[CSRankingConfiguration enableSemanticSearch]
+ -[CSRankingConfiguration enableSuggestions]
+ -[CSRankingConfiguration enableUniversalSuggestions]
+ -[CSRankingConfiguration initWithQueryContext:]
+ -[CSRankingConfiguration initWithQueryContext:].cold.1
+ -[CSRankingConfiguration isCJK]
+ -[CSRankingConfiguration isMail]
+ -[CSRankingConfiguration isNotes]
+ -[CSRankingConfiguration isPhotos]
+ -[CSRankingConfiguration isPommesCtl]
+ -[CSRankingConfiguration isPommesZKW]
+ -[CSRankingConfiguration isSafari]
+ -[CSRankingConfiguration isSearch]
+ -[CSRankingConfiguration isSettings]
+ -[CSRankingConfiguration isSpotlight]
+ -[CSRankingConfiguration maxSuggestionCount]
+ -[CSRankingConfiguration nlpContextID]
+ -[CSRankingConfiguration suggestionRankingWeights]
+ -[CSSearchConnection initWithMachServiceName:].cold.1
+ -[CSSearchQuery commonInitWithQueryString:queryContext:].cold.1
+ -[CSSearchQuery initMDQueryWithQueryString:queryContext:].cold.1
+ -[CSSearchQuery protectionClasses].cold.1
+ -[CSSearchQuery setupFetchAttributesForSearch].cold.2
+ -[CSSearchQuery(TopHitRanking) getTopHitResult:fetchAttrs:].cold.2
+ -[CSSearchQuery(TopHitRanking) getTopHitResult:fetchAttrs:].cold.3
+ -[CSSearchQuery(TopHitRanking) setupTopHitQueryContextForClientBundleId:].cold.7
+ -[CSSearchQuery(TopHitRanking) setupTopHitQueryContextForClientBundleId:].cold.8
+ -[CSSearchQueryContext filterOutHiddenApps]
+ -[CSSearchQueryContext setFilterOutHiddenApps:]
+ -[CSSearchableIndex _fetchBundleIDsWithCompletionHandler:]
+ -[CSSearchableIndex _setMailMessageAttributes:].cold.1
+ -[CSSearchableIndex criticalQueue].cold.1
+ -[CSSearchableIndex requestQueue].cold.1
+ -[CSSearchableIndex throttle:]
+ -[CSSearchableIndex unthrottle:]
+ -[CSSearchableIndexRequest cost]
+ -[CSSearchableIndexRequest initWithSearchableIndex:label:critical:cost:]
+ -[CSSearchableIndexRequest initWithSearchableIndex:label:critical:cost:].cold.1
+ -[CSSearchableIndexRequest initWithSearchableIndex:label:critical:cost:].cold.2
+ -[CSSearchableItem needsPriority]
+ -[CSSearchableItem needsSummary]
+ -[CSSearchableItem setUpdateListenerOptions:]
+ -[CSSearchableItem updateListenerOptions]
+ -[CSSearchableItem(Internal) filteredSpotlightAttributes].cold.1
+ -[CSSearchableItem(Internal) standardizeAttributesForBundle:protectionClass:].cold.1
+ -[CSSearchableItemAttributeSet _copyInternalsFrom:]
+ -[CSSearchableItemAttributeSet moveFrom:]
+ -[CSSearchableItemAttributeSet(CSAttributes) setTranscribedTextContent:]
+ -[CSSearchableItemAttributeSet(CSAttributes) transcribedTextContent]
+ -[CSSearchableItemAttributeSet(CSMail_Private) isPriority]
+ -[CSSearchableItemAttributeSet(CSMail_Private) passbookIsPaymentPass]
+ -[CSSearchableItemAttributeSet(CSMail_Private) setPassbookIsPaymentPass:]
+ -[CSSearchableItemAttributeSet(CSPhotos_Private) photosPhotographicStyles]
+ -[CSSearchableItemAttributeSet(CSPhotos_Private) setPhotosPhotographicStyles:]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) eventIsCancelled]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) eventUpdateStatus]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) setEventIsCancelled:]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) setEventUpdateStatus:]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) setTextContentSummary:]
+ -[CSSearchableItemAttributeSet(CSPrivateAttributes) textContentSummary]
+ -[CSSuggestionsRanker .cxx_destruct]
+ -[CSSuggestionsRanker collectSuggestions:]
+ -[CSSuggestionsRanker currentLocalSuggestions]
+ -[CSSuggestionsRanker currentPeopleSuggestions]
+ -[CSSuggestionsRanker currentTokenSuggestions]
+ -[CSSuggestionsRanker initWithRankingConfiguration:]
+ -[CSSuggestionsRanker rankingConfiguration]
+ -[CSSuggestionsRanker suggestions]
+ -[CSSuggestionsRanker suggestions].cold.1
+ -[CSTokenScopeParser tokenScopeConfigurationTable].cold.1
+ -[CSUnhousedSearchableIndex initWithPath:bundleId:]
+ -[CSUserQuery handleSuggestions].cold.2
+ -[CSUserQuery queryStringWithQueryContext:searchString:options:].cold.10
+ -[CSUserQuery queryStringWithQueryContext:searchString:options:].cold.11
+ -[CSUserQuery queryStringWithQueryContext:searchString:options:].cold.12
+ -[NSNull(CSCoderAdditions) encodeWithCSCoder:]
+ -[NSString(CSUserQuery) containsCJK].cold.1
+ -[NSString(CSUserQuery) normalizeForSemanticSearch].cold.1
+ -[_CSContactSearch autocompleteFetch:didReceiveResults:].cold.1
+ -[_CSContactSearch handleCompletionWithContacts:error:].cold.2
+ -[_CSSuggestionToken initWithUserString:displayString:attributeValues:attributeStrings:options:].cold.1
+ -[_CSSuggestionToken initWithUserString:suggestionTokenResult:].cold.1
+ -[_CSSuggestionToken isTopHit]
+ -[_CSSuggestionToken setIsTopHit:]
+ -[_MDRemoteExtensionContext _bundleIsICloudDriveOrFruitbasket:]
+ -[_MDRemoteExtensionContext ifURLIsNotDataless:getResultOf:]
+ -[_MDRemoteExtensionContext performJob:acknowledgementHandler:].cold.2
+ CSCodedDataDealloctor.cold.1
+ CSGetCurrentLocale.cold.1
+ CSQueryAttributeKeyMap.onceToken
+ CSQueryAttributeKeyMap.sQueryInfoKeys
+ CSQueryAttributeKeyMap.sQueryInfoMap
+ CSRedactString.cold.1
+ CSRedactStringArray.cold.1
+ CSSimpleQueryCancel.cold.1
+ CSSimpleQueryHasResultsForQuery.cold.1
+ CSUnhousedIndexDefaultPath.cold.1
+ CSUnhousedUUID.cold.1
+ GCC_except_table111
+ GCC_except_table112
+ GCC_except_table126
+ GCC_except_table127
+ GCC_except_table134
+ GCC_except_table138
+ GCC_except_table140
+ GCC_except_table144
+ GCC_except_table145
+ GCC_except_table154
+ GCC_except_table155
+ GCC_except_table163
+ GCC_except_table164
+ GCC_except_table183
+ GCC_except_table184
+ GCC_except_table188
+ GCC_except_table191
+ GCC_except_table192
+ GCC_except_table196
+ GCC_except_table200
+ GCC_except_table201
+ GCC_except_table210
+ GCC_except_table211
+ GCC_except_table219
+ GCC_except_table230
+ GCC_except_table24
+ GCC_except_table240
+ GCC_except_table241
+ GCC_except_table249
+ GCC_except_table256
+ GCC_except_table258
+ GCC_except_table266
+ GCC_except_table267
+ GCC_except_table272
+ GCC_except_table273
+ GCC_except_table277
+ GCC_except_table282
+ GCC_except_table296
+ GCC_except_table297
+ GCC_except_table300
+ GCC_except_table301
+ GCC_except_table305
+ GCC_except_table306
+ GCC_except_table308
+ GCC_except_table325
+ GCC_except_table326
+ GCC_except_table329
+ GCC_except_table338
+ GCC_except_table34
+ GCC_except_table354
+ GCC_except_table364
+ GCC_except_table366
+ GCC_except_table371
+ GCC_except_table384
+ GCC_except_table385
+ GCC_except_table388
+ GCC_except_table394
+ GCC_except_table398
+ GCC_except_table404
+ GCC_except_table405
+ GCC_except_table414
+ GCC_except_table50
+ GCC_except_table502
+ GCC_except_table503
+ GCC_except_table511
+ GCC_except_table522
+ GCC_except_table548
+ GCC_except_table598
+ GCC_except_table63
+ GCC_except_table682
+ GCC_except_table70
+ GCC_except_table78
+ GCC_except_table79
+ GCC_except_table95
+ GCC_except_table96
+ GCC_except_table996
+ GetCSUserQueryParser.cold.1
+ MDCopyTypePedigree.cold.1
+ OBJC_IVAR_$_CSGenerativeModelsAvailabilityManager._gmStatusQueue
+ OBJC_IVAR_$_CSGenerativeModelsAvailabilityManager._gmsNotifyToken
+ OBJC_IVAR_$_CSGenerativeModelsAvailabilityManager._useCaseStatus
+ OBJC_IVAR_$_CSLocationTag._country
+ OBJC_IVAR_$_CSLocationTag._location
+ OBJC_IVAR_$_CSLocationTag._parent
+ OBJC_IVAR_$_CSRankingConfiguration._bundleIDs
+ OBJC_IVAR_$_CSRankingConfiguration._enableExtendedEmbeddingTimeout
+ OBJC_IVAR_$_CSRankingConfiguration._enablePommesRanking
+ OBJC_IVAR_$_CSRankingConfiguration._enablePommesSuggestions
+ OBJC_IVAR_$_CSRankingConfiguration._enableSemanticSearch
+ OBJC_IVAR_$_CSRankingConfiguration._enableSuggestions
+ OBJC_IVAR_$_CSRankingConfiguration._enableUniversalSuggestions
+ OBJC_IVAR_$_CSRankingConfiguration._isCJK
+ OBJC_IVAR_$_CSRankingConfiguration._isMail
+ OBJC_IVAR_$_CSRankingConfiguration._isNotes
+ OBJC_IVAR_$_CSRankingConfiguration._isPhotos
+ OBJC_IVAR_$_CSRankingConfiguration._isPommesCtl
+ OBJC_IVAR_$_CSRankingConfiguration._isPommesZKW
+ OBJC_IVAR_$_CSRankingConfiguration._isSafari
+ OBJC_IVAR_$_CSRankingConfiguration._isSearch
+ OBJC_IVAR_$_CSRankingConfiguration._isSettings
+ OBJC_IVAR_$_CSRankingConfiguration._isSpotlight
+ OBJC_IVAR_$_CSRankingConfiguration._maxSuggestionCount
+ OBJC_IVAR_$_CSRankingConfiguration._nlpContextID
+ OBJC_IVAR_$_CSRankingConfiguration._suggestionRankingWeights
+ OBJC_IVAR_$_CSSearchQueryContext._filterOutHiddenApps
+ OBJC_IVAR_$_CSSearchableIndexRequest._cost
+ OBJC_IVAR_$_CSSuggestionsRanker._lockedLocalPeopleSuggestions
+ OBJC_IVAR_$_CSSuggestionsRanker._lockedPeopleSuggestions
+ OBJC_IVAR_$_CSSuggestionsRanker._lockedTokenSuggestions
+ OBJC_IVAR_$_CSSuggestionsRanker._lockedlocalSuggestions
+ OBJC_IVAR_$_CSSuggestionsRanker._rankingConfiguration
+ OBJC_IVAR_$_CSUserQuery._rankingConfig
+ OBJC_IVAR_$_CSUserQuery._suggestionsRanker
+ OBJC_IVAR_$__CSSuggestionToken._isTopHit
+ _CSAttributedEntityTypePhotosPhotographicStylesKey
+ _MDItemAppEntityTitle
+ _MDItemEventIsCancelled
+ _MDItemEventUpdateStatus
+ _MDItemExtractedCurrenciesValues
+ _MDItemExtractedDatesValues
+ _MDItemExtractedLocationsValues
+ _MDItemFileProviderFilename
+ _MDItemIsPriority
+ _MDItemPassbookIsPaymentPass
+ _MDItemPassbookTransactionStatus
+ _MDItemPassbookTransactionType
+ _MDItemPhotosPhotographicStyles
+ _MDItemPriorityStatus
+ _MDItemTextContentSummary
+ _OBJC_CLASS_$_CSGenerativeModelsAvailabilityManager
+ _OBJC_CLASS_$_CSRankingConfiguration
+ _OBJC_CLASS_$_CSSuggestionsRanker
+ _OBJC_METACLASS_$_CSGenerativeModelsAvailabilityManager
+ _OBJC_METACLASS_$_CSRankingConfiguration
+ _OBJC_METACLASS_$_CSSuggestionsRanker
+ _ZN24CSFriendlyFieldNameTable11in_word_setEPKcj.cold.1
+ __110-[CSSearchableIndex _fetchAttributes:protectionClass:bundleID:items:includeParents:options:completionHandler:]_block_invoke.448
+ __115-[CSSearchableIndex fetchLastClientStateWithProtectionClass:forBundleID:clientStateName:options:completionHandler:]_block_invoke.322
+ __21-[CSSearchQuery poll]_block_invoke.1124
+ __23-[CSSearchQuery cancel]_block_invoke.1133
+ __34-[CSSearchConnection cancelQuery:]_block_invoke.1530
+ __34-[CSSearchConnection cancelQuery:]_block_invoke.1530.cold.1
+ __36-[CSSearchQuery processResultItems:]_block_invoke.1189
+ __54-[CSSearchQuery copyResultsFromPlist:protectionClass:]_block_invoke.1157
+ __54-[CSSearchQuery copyResultsFromPlist:protectionClass:]_block_invoke.1159
+ __55-[CSSuggestion addSuggestionHighlight:withDisplayText:]_block_invoke.1197
+ __57-[CSSearchQuery initMDQueryWithQueryString:queryContext:]_block_invoke.1060
+ __57-[CSSearchQuery initMDQueryWithQueryString:queryContext:]_block_invoke.1061
+ __58-[CSSearchableIndex _fetchBundleIDsWithCompletionHandler:]_block_invoke.293
+ __59-[CSRequestQueue initWithLabel:target:critical:startBlock:]_block_invoke.192
+ __60-[CSSearchableItem(Internal) _standardizeExtractedEntities:]_block_invoke.256
+ __60-[CSSearchableItem(Internal) _standardizeExtractedEntities:]_block_invoke_2.259
+ __63-[CSSearchableIndex _issueDiagnose:logQuery:completionHandler:]_block_invoke.301
+ __63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.118
+ __63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.119
+ __63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.136
+ __63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.136.cold.1
+ __63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.157
+ __63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.168
+ __63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.168.cold.1
+ __63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke_2.160
+ __63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke_2.160.cold.1
+ __64-[CSUserQuery queryStringWithQueryContext:searchString:options:]_block_invoke.480
+ __64-[CSUserQuery queryStringWithQueryContext:searchString:options:]_block_invoke.720
+ __67-[CSSearchableItem(Internal) _standardizeExtractedNumericEntities:]_block_invoke.307
+ __67-[CSSearchableItem(Internal) _standardizeExtractedNumericEntities:]_block_invoke.325
+ __73-[CSSearchableIndex(SpotlightCache) issueCacheCommand:completionHandler:]_block_invoke.773
+ __76-[CSSearchableIndex performIndexJob:protectionClass:acknowledgementHandler:]_block_invoke.372
+ __80-[CSSearchQuery filterMegadomePeopleSuggestions:isShortQuery:completionHandler:]_block_invoke.1164
+ __80-[CSSearchableItemAttributeSet(CSCoderAdditions) encodeWithCSCoder:includeText:]_block_invoke.1991
+ __94-[CSSearchableIndex transferDeletionJournalsForProtectionClass:toDirectory:completionHandler:]_block_invoke.385
+ __94-[CSUserQuery filterContactPeopleSuggestions:cachedSuggestionsEmailToScope:completionHandler:]_block_invoke.767
+ __99-[CSSearchableIndex _fetchCacheFileDescriptorsForProtectionClass:bundleID:items:completionHandler:]_block_invoke.458
+ __99-[CSSearchableIndex _fetchCacheFileDescriptorsForProtectionClass:bundleID:items:completionHandler:]_block_invoke.461
+ __Block_byref_object_copy_.459
+ __Block_byref_object_dispose_.460
+ __CSQueryAttributeKeyMap_block_invoke.cold.1
+ __MDQuerySetAttributedUserQuery
+ __MDQuerySetClientBundleID
+ __MDQuerySetPommesRanking
+ __MDQuerySetQueryUnderstanding
+ __MDQuerySetTokenRewrites
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSNull_$_CSCoderAdditions
+ __OBJC_$_CATEGORY_NSNull_$_CSCoderAdditions
+ __OBJC_$_CLASS_METHODS_CSGenerativeModelsAvailabilityManager
+ __OBJC_$_INSTANCE_METHODS_CSGenerativeModelsAvailabilityManager
+ __OBJC_$_INSTANCE_METHODS_CSRankingConfiguration
+ __OBJC_$_INSTANCE_METHODS_CSSuggestionsRanker
+ __OBJC_$_INSTANCE_VARIABLES_CSGenerativeModelsAvailabilityManager
+ __OBJC_$_INSTANCE_VARIABLES_CSRankingConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_CSSuggestionsRanker
+ __OBJC_$_PROP_LIST_CSGenerativeModelsAvailabilityManager
+ __OBJC_$_PROP_LIST_CSRankingConfiguration
+ __OBJC_$_PROP_LIST_CSSuggestionsRanker
+ __OBJC_CATEGORY_PROTOCOLS_$_NSNull_$_CSCoderAdditions
+ __OBJC_CLASS_RO_$_CSGenerativeModelsAvailabilityManager
+ __OBJC_CLASS_RO_$_CSRankingConfiguration
+ __OBJC_CLASS_RO_$_CSSuggestionsRanker
+ __OBJC_METACLASS_RO_$_CSGenerativeModelsAvailabilityManager
+ __OBJC_METACLASS_RO_$_CSRankingConfiguration
+ __OBJC_METACLASS_RO_$_CSSuggestionsRanker
+ ___132+[CSSearchableIndex fetchAttributesFromImportFileURL:bundleID:fileType:identifier:sandboxExtension:attributesWithCompletionHandler:]_block_invoke
+ ___45-[CSGenerativeModelsAvailabilityManager init]_block_invoke
+ ___47-[CSRankingConfiguration initWithQueryContext:]_block_invoke
+ ___55+[CSGenerativeModelsAvailabilityManager sharedInstance]_block_invoke
+ ___58-[CSSearchableIndex _fetchBundleIDsWithCompletionHandler:]_block_invoke
+ ___58-[CSSearchableIndex _fetchBundleIDsWithCompletionHandler:]_block_invoke_2
+ ___71+[CSSearchableIndex fetchFile:attributesWithSandbox:completionHandler:]_block_invoke
+ ___71+[CSSearchableIndex fetchFile:attributesWithSandbox:completionHandler:]_block_invoke_2
+ ___71+[CSSearchableIndex fetchFile:attributesWithSandbox:completionHandler:]_block_invoke_3
+ ___CSQueryAttributeKeyMap_block_invoke
+ ___block_descriptor_108_e8_32s40s48s56s_e8_v16?0Q8l
+ ___block_descriptor_116_e8_32s40s48s56s64r_e13_v24?0^8^B16l
+ ___block_descriptor_116_e8_32s40s48s56s64r_e8_v16?0Q8l
+ ___block_descriptor_122_e8_32s40s48s56r_e13_v24?0^8^B16l
+ ___block_descriptor_40_e8_32s_e8_v12?0i8l
+ ___block_descriptor_48_e8_32s40w_e5_v8?0l
+ ___block_descriptor_56_e8_32s40s48r_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48s_e35_"CSSearchableItemAttributeSet"8?0l
+ ___block_descriptor_80_e8_32s40s48s56s_e8_v16?0Q8l
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.1025
+ __block_literal_global.103
+ __block_literal_global.1066
+ __block_literal_global.1070
+ __block_literal_global.1127
+ __block_literal_global.1133
+ __block_literal_global.1136
+ __block_literal_global.1381
+ __block_literal_global.1413
+ __block_literal_global.1439
+ __block_literal_global.1501
+ __block_literal_global.1503
+ __block_literal_global.1505
+ __block_literal_global.1508
+ __block_literal_global.1510
+ __block_literal_global.1511
+ __block_literal_global.1512
+ __block_literal_global.1516
+ __block_literal_global.1518
+ __block_literal_global.1520
+ __block_literal_global.1522
+ __block_literal_global.1630
+ __block_literal_global.1938
+ __block_literal_global.194
+ __block_literal_global.246
+ __block_literal_global.248
+ __block_literal_global.258
+ __block_literal_global.261
+ __block_literal_global.263
+ __block_literal_global.265
+ __block_literal_global.300
+ __block_literal_global.309
+ __block_literal_global.319
+ __block_literal_global.327
+ __block_literal_global.328
+ __block_literal_global.334
+ __block_literal_global.339
+ __block_literal_global.351
+ __block_literal_global.391
+ __block_literal_global.482
+ __block_literal_global.604
+ __block_literal_global.633
+ __block_literal_global.637
+ __block_literal_global.722
+ __block_literal_global.764
+ __block_literal_global.766
+ __block_literal_global.783
+ __block_literal_global.810
+ __block_literal_global.824
+ __block_literal_global.832
+ _objc_msgSend$_bundleIsICloudDriveOrFruitbasket:
+ _objc_msgSend$_copyInternalsFrom:
+ _objc_msgSend$_isAvailableForUseCaseIdentifiers:
+ _objc_msgSend$collectSuggestions:
+ _objc_msgSend$cost
+ _objc_msgSend$currentLocalSuggestions
+ _objc_msgSend$currentPeopleSuggestions
+ _objc_msgSend$currentTokenSuggestions
+ _objc_msgSend$dataWrapper
+ _objc_msgSend$enableExtendedEmbeddingTimeout
+ _objc_msgSend$enablePommesRanking
+ _objc_msgSend$enablePommesSuggestions
+ _objc_msgSend$enableSemanticSearch
+ _objc_msgSend$enableUniversalSuggestions
+ _objc_msgSend$fetchFile:attributesWithSandbox:completionHandler:
+ _objc_msgSend$filterOutHiddenApps
+ _objc_msgSend$ifURLIsNotDataless:getResultOf:
+ _objc_msgSend$indexRequestsPerformDataJob:forBundle:completionHandler:
+ _objc_msgSend$initWithLocation:parent:country:lat:lng:confidence:
+ _objc_msgSend$initWithQueryContext:
+ _objc_msgSend$initWithRankingConfiguration:
+ _objc_msgSend$initWithSearchableIndex:label:critical:cost:
+ _objc_msgSend$isPommesCtl
+ _objc_msgSend$isPommesZKW
+ _objc_msgSend$isSearch
+ _objc_msgSend$isSemanticSearchAvailable
+ _objc_msgSend$isTopHit
+ _objc_msgSend$isUrgent
+ _objc_msgSend$moveFrom:
+ _objc_msgSend$nlpContextID
+ _objc_msgSend$rankingConfiguration
+ _objc_msgSend$rankingConfigurationWithMeContact:emailAddresses:phoneFavorites:vipList:clientBundle:isScopedSearch:isAdvancedSyntax:spotlightQuery:userQuery:tokenString:queryKind:isPeopleSearch:keyboardLanguage:
+ _objc_msgSend$setBundleIdentifier:
+ _objc_msgSend$setFilterOutHiddenApps:
+ _objc_msgSend$setIsTopHit:
+ _objc_msgSend$setUseCaseStatus:
+ _objc_msgSend$suggestionRankingWeights
+ _objc_msgSend$suggestions
+ _objc_msgSend$throttle:
+ _objc_msgSend$tokenRewrites
+ _objc_msgSend$unthrottle:
+ _objc_msgSend$updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:
+ _objc_msgSend$useCaseStatus
+ _sCSAttrInfoArray
+ dateForString.cold.1
+ defaultSearchableIndex.onceToken.850
+ defaultSearchableIndex.onceToken.857
+ defaultSearchableIndex.sDefaultInstance.849
+ defaultSearchableIndex.sDefaultInstance.856
+ fetchFile:attributesWithSandbox:completionHandler:.onceToken
+ fetchFile:attributesWithSandbox:completionHandler:.queue
+ fetchFile:attributesWithSandbox:completionHandler:.semaphore
+ hasInternalCSEntitlement.cold.1
+ hasPrivateIndexUnsandboxEntitlement.cold.1
+ initEntitlements.cold.1
+ initWithQueryContext:.gIsFeatureFlagsEnabled
+ initWithQueryContext:.gIsMailSemanticSearchEnabled
+ initWithQueryContext:.onceToken
+ isAppleInternalInstall.cold.1
+ logForCSLogCategoryDaemonClient.cold.1
+ logForCSLogCategoryDefault.cold.1
+ logForCSLogCategoryIndex.cold.1
+ logForCSLogCategoryPersonalization.cold.1
+ logForCSLogCategoryPhotosQU.cold.1
+ logForCSLogCategoryQuery.cold.1
+ logForCSLogCategoryRecs.cold.1
+ logForCSLogCategoryUA.cold.1
+ md_fsgetpath_ext.cold.1
+ queryStringWithQueryContext:searchString:options:.onceAttributesToken.719
+ readNSDate.cold.1
+ registerForGameModeChange.cold.1
+ tokenScopesForPeopleSuggestions.cold.1
+ tokenScopesWithPersonKey.cold.1
+ updateTopHitCandidatesAndReturnItemToBeSentToClientNow.cold.1
+ x2_openat.cold.1
- -[CSFilesSearchQuery completed]
- -[CSFilesSearchQuery completions]
- -[CSFilesSearchQuery dealloc]
- -[CSFilesSearchQuery handleNotification:]
- -[CSFilesSearchQuery handleNotification:].cold.1
- -[CSFilesSearchQuery initWithQueryString:context:].cold.1
- -[CSFilesSearchQuery mdQuery]
- -[CSFilesSearchQuery processedItems]
- -[CSFilesSearchQuery queue]
- -[CSFilesSearchQuery setCompleted:]
- -[CSFilesSearchQuery setCompletions:]
- -[CSFilesSearchQuery setMdQuery:]
- -[CSFilesSearchQuery setProcessedItems:]
- -[CSFilesSearchQuery setQueue:]
- -[CSLocationTag initWithLocationID:lat:lng:confidence:]
- -[CSSearchableIndex throttle].cold.1
- -[CSSearchableIndex unthrottle].cold.1
- -[CSSearchableIndexRequest initWithSearchableIndex:label:critical:].cold.1
- -[CSSearchableIndexRequest initWithSearchableIndex:label:critical:].cold.2
- GCC_except_table105
- GCC_except_table106
- GCC_except_table124
- GCC_except_table125
- GCC_except_table132
- GCC_except_table135
- GCC_except_table136
- GCC_except_table141
- GCC_except_table142
- GCC_except_table143
- GCC_except_table152
- GCC_except_table153
- GCC_except_table160
- GCC_except_table161
- GCC_except_table17
- GCC_except_table174
- GCC_except_table175
- GCC_except_table176
- GCC_except_table179
- GCC_except_table180
- GCC_except_table181
- GCC_except_table182
- GCC_except_table185
- GCC_except_table186
- GCC_except_table190
- GCC_except_table194
- GCC_except_table198
- GCC_except_table199
- GCC_except_table217
- GCC_except_table22
- GCC_except_table223
- GCC_except_table224
- GCC_except_table228
- GCC_except_table243
- GCC_except_table244
- GCC_except_table252
- GCC_except_table253
- GCC_except_table259
- GCC_except_table260
- GCC_except_table263
- GCC_except_table264
- GCC_except_table269
- GCC_except_table27
- GCC_except_table270
- GCC_except_table274
- GCC_except_table275
- GCC_except_table276
- GCC_except_table279
- GCC_except_table284
- GCC_except_table295
- GCC_except_table312
- GCC_except_table313
- GCC_except_table316
- GCC_except_table32
- GCC_except_table336
- GCC_except_table339
- GCC_except_table340
- GCC_except_table351
- GCC_except_table362
- GCC_except_table369
- GCC_except_table382
- GCC_except_table383
- GCC_except_table386
- GCC_except_table392
- GCC_except_table396
- GCC_except_table402
- GCC_except_table403
- GCC_except_table410
- GCC_except_table44
- GCC_except_table46
- GCC_except_table498
- GCC_except_table499
- GCC_except_table509
- GCC_except_table520
- GCC_except_table546
- GCC_except_table587
- GCC_except_table60
- GCC_except_table61
- GCC_except_table67
- GCC_except_table676
- GCC_except_table69
- GCC_except_table76
- GCC_except_table84
- GCC_except_table91
- GCC_except_table94
- GCC_except_table981
- GCC_except_table99
- OBJC_IVAR_$_CSFilesSearchQuery._completed
- OBJC_IVAR_$_CSFilesSearchQuery._completions
- OBJC_IVAR_$_CSFilesSearchQuery._mdQuery
- OBJC_IVAR_$_CSFilesSearchQuery._processedItems
- OBJC_IVAR_$_CSFilesSearchQuery._queue
- _MDQueryDisableUpdates
- _MDQueryEnableUpdates
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- __110-[CSSearchableIndex _fetchAttributes:protectionClass:bundleID:items:includeParents:options:completionHandler:]_block_invoke.436
- __115-[CSSearchableIndex fetchLastClientStateWithProtectionClass:forBundleID:clientStateName:options:completionHandler:]_block_invoke.318
- __21-[CSSearchQuery poll]_block_invoke.1113
- __23-[CSSearchQuery cancel]_block_invoke.1122
- __27-[CSFilesSearchQuery start]_block_invoke.31
- __34-[CSSearchConnection cancelQuery:]_block_invoke.1519
- __34-[CSSearchConnection cancelQuery:]_block_invoke.1519.cold.1
- __36-[CSSearchQuery processResultItems:]_block_invoke.1178
- __54-[CSSearchQuery copyResultsFromPlist:protectionClass:]_block_invoke.1146
- __54-[CSSearchQuery copyResultsFromPlist:protectionClass:]_block_invoke.1148
- __55-[CSSuggestion addSuggestionHighlight:withDisplayText:]_block_invoke.1189
- __57-[CSSearchQuery initMDQueryWithQueryString:queryContext:]_block_invoke.1052
- __57-[CSSearchQuery initMDQueryWithQueryString:queryContext:]_block_invoke.1053
- __59-[CSRequestQueue initWithLabel:target:critical:startBlock:]_block_invoke.185
- __60-[CSSearchableItem(Internal) _standardizeExtractedEntities:]_block_invoke.248
- __60-[CSSearchableItem(Internal) _standardizeExtractedEntities:]_block_invoke_2.251
- __63-[CSSearchableIndex _issueDiagnose:logQuery:completionHandler:]_block_invoke.297
- __63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.109
- __63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.110
- __63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.127
- __63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.127.cold.1
- __63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.148
- __63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.152
- __63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.152.cold.1
- __64-[CSUserQuery queryStringWithQueryContext:searchString:options:]_block_invoke.493
- __64-[CSUserQuery queryStringWithQueryContext:searchString:options:]_block_invoke.522
- __64-[CSUserQuery queryStringWithQueryContext:searchString:options:]_block_invoke.738
- __67-[CSSearchableItem(Internal) _standardizeExtractedNumericEntities:]_block_invoke.299
- __67-[CSSearchableItem(Internal) _standardizeExtractedNumericEntities:]_block_invoke.311
- __73-[CSSearchableIndex(SpotlightCache) issueCacheCommand:completionHandler:]_block_invoke.753
- __76-[CSSearchableIndex performIndexJob:protectionClass:acknowledgementHandler:]_block_invoke.368
- __80-[CSSearchQuery filterMegadomePeopleSuggestions:isShortQuery:completionHandler:]_block_invoke.1153
- __80-[CSSearchableItemAttributeSet(CSCoderAdditions) encodeWithCSCoder:includeText:]_block_invoke.1958
- __94-[CSSearchableIndex transferDeletionJournalsForProtectionClass:toDirectory:completionHandler:]_block_invoke.381
- __94-[CSUserQuery filterContactPeopleSuggestions:cachedSuggestionsEmailToScope:completionHandler:]_block_invoke.785
- __99-[CSSearchableIndex _fetchCacheFileDescriptorsForProtectionClass:bundleID:items:completionHandler:]_block_invoke.446
- __99-[CSSearchableIndex _fetchCacheFileDescriptorsForProtectionClass:bundleID:items:completionHandler:]_block_invoke.447
- __MDQueryGetResultCountForAllGroups
- __OBJC_$_PROP_LIST_CSFilesSearchQueryContext
- ___27-[CSFilesSearchQuery start]_block_invoke
- ___50-[CSFilesSearchQuery initWithQueryString:context:]_block_invoke
- ___63+[CSSearchableIndex fetchFile:attributesWithCompletionHandler:]_block_invoke
- ___63+[CSSearchableIndex fetchFile:attributesWithCompletionHandler:]_block_invoke_2
- ___63+[CSSearchableIndex fetchFile:attributesWithCompletionHandler:]_block_invoke_3
- ___block_descriptor_106_e8_32s40s48s56s_e8_v16?0Q8l
- ___block_descriptor_114_e8_32s40s48s56s64r_e13_v24?0^8^B16l
- ___block_descriptor_114_e8_32s40s48s56s64r_e8_v16?0Q8l
- ___block_descriptor_120_e8_32s40s48s56r_e13_v24?0^8^B16l
- ___block_descriptor_33_e5_v8?0l
- ___block_descriptor_44_e8_32w_e24_v16?0"NSNotification"8l
- ___block_descriptor_72_e8_32s40s48s_e8_v16?0Q8l
- __block_literal_global.1017
- __block_literal_global.1058
- __block_literal_global.1062
- __block_literal_global.1116
- __block_literal_global.1125
- __block_literal_global.1373
- __block_literal_global.1405
- __block_literal_global.1431
- __block_literal_global.1478
- __block_literal_global.1480
- __block_literal_global.1482
- __block_literal_global.1486
- __block_literal_global.1488
- __block_literal_global.1490
- __block_literal_global.1492
- __block_literal_global.1494
- __block_literal_global.1497
- __block_literal_global.1500
- __block_literal_global.187
- __block_literal_global.1905
- __block_literal_global.238
- __block_literal_global.240
- __block_literal_global.245
- __block_literal_global.250
- __block_literal_global.255
- __block_literal_global.257
- __block_literal_global.292
- __block_literal_global.301
- __block_literal_global.313
- __block_literal_global.324
- __block_literal_global.325
- __block_literal_global.330
- __block_literal_global.347
- __block_literal_global.387
- __block_literal_global.524
- __block_literal_global.634
- __block_literal_global.646
- __block_literal_global.651
- __block_literal_global.740
- __block_literal_global.744
- __block_literal_global.755
- __block_literal_global.763
- __block_literal_global.798
- __block_literal_global.806
- __block_literal_global.814
- __block_literal_global.94
- _kMDQueryHasUpdateNotification
- _objc_msgSend$completions
- _objc_msgSend$handleNotification:
- _objc_msgSend$initWithLocationID:lat:lng:confidence:
- _objc_msgSend$rankingConfigurationWithMeContact:emailAddresses:phoneFavorites:vipList:clientBundle:isScopedSearch:spotlightQuery:userQuery:tokenString:queryKind:isPeopleSearch:keyboardLanguage:
- _objc_msgSend$throttle
- _objc_msgSend$unthrottle
- _objc_msgSend$updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:
- _pthread_set_qos_class_self_np
- defaultSearchableIndex.onceToken.829
- defaultSearchableIndex.onceToken.836
- defaultSearchableIndex.sDefaultInstance.828
- defaultSearchableIndex.sDefaultInstance.835
- fetchFile:attributesWithCompletionHandler:.onceToken
- fetchFile:attributesWithCompletionHandler:.queue
- fetchFile:attributesWithCompletionHandler:.semaphore
- queryStringWithQueryContext:searchString:options:.isFeatureFlagsEnabled
- queryStringWithQueryContext:searchString:options:.isMailSemanticSearchEnabled
- queryStringWithQueryContext:searchString:options:.onceAttributesToken.737
- queryStringWithQueryContext:searchString:options:.onceToken
CStrings:
+ "\rV"
+ " queryString:%@"
+ " userQuery:%@"
+ "-[CSSearchableIndexRequest initWithSearchableIndex:label:critical:cost:]"
+ "==== CALLBACK data:%p length:%lu crash:%d error:%@ identifier:%@"
+ "@\"CSRankingConfiguration\""
+ "@\"CSSearchableItemAttributeSet\"8@?0"
+ "@\"CSSuggestionsRanker\""
+ "@64@0:8@16@24@32d40d48d56"
+ "@92@0:8^@16Q24^Q32@40@48^s56Q64{CSUnpackInfo=ssssss}72@84"
+ "CSGenerativeModelsAvailabilityManager"
+ "CSQueryAttributeKeyMap_block_invoke"
+ "CSRankingConfiguration"
+ "CSSuggestionsRanker"
+ "Error updating attributes in extension context %@"
+ "Error updating attributes while checking dataless in extension context %@"
+ "Failed to serialize the queryUnderstanding dictionary for MDS query. Error: %@"
+ "MobileMailIndex"
+ "NSCocoaErrorDomain"
+ "Passbook_isPaymentPass"
+ "Passbook_transactionStatus"
+ "Passbook_transactionType"
+ "PreventUnindexOnEviction"
+ "Resumed \"%s\" at %u/%d"
+ "SandboxExtension"
+ "Suspended \"%s\" at %u/%d"
+ "T@\"CSRankingConfiguration\",R,N,V_rankingConfiguration"
+ "T@\"NSArray\",R,N,V_bundleIDs"
+ "T@\"NSDictionary\",&,V_useCaseStatus"
+ "T@\"NSDictionary\",R,N,V_suggestionRankingWeights"
+ "T@\"NSNumber\",R,N,V_country"
+ "T@\"NSNumber\",R,N,V_location"
+ "T@\"NSNumber\",R,N,V_parent"
+ "T@\"NSString\",R,N,V_nlpContextID"
+ "TB,N,V_isTopHit"
+ "TB,R,N,V_enableExtendedEmbeddingTimeout"
+ "TB,R,N,V_enablePommesRanking"
+ "TB,R,N,V_enablePommesSuggestions"
+ "TB,R,N,V_enableSemanticSearch"
+ "TB,R,N,V_enableSuggestions"
+ "TB,R,N,V_enableUniversalSuggestions"
+ "TB,R,N,V_isCJK"
+ "TB,R,N,V_isMail"
+ "TB,R,N,V_isNotes"
+ "TB,R,N,V_isPhotos"
+ "TB,R,N,V_isPommesCtl"
+ "TB,R,N,V_isPommesZKW"
+ "TB,R,N,V_isSafari"
+ "TB,R,N,V_isSearch"
+ "TB,R,N,V_isSettings"
+ "TB,R,N,V_isSpotlight"
+ "TI,R,N"
+ "Tq,R,N,V_maxSuggestionCount"
+ "[GMS] availability notification token %d"
+ "[GMS] error setting up availability notification %u"
+ "[GMS] received gms availability notification"
+ "_bundleIsICloudDriveOrFruitbasket:"
+ "_copyInternalsFrom:"
+ "_cost"
+ "_country"
+ "_enableExtendedEmbeddingTimeout"
+ "_enablePommesRanking"
+ "_enablePommesSuggestions"
+ "_enableSemanticSearch"
+ "_enableSuggestions"
+ "_enableUniversalSuggestions"
+ "_fetchBundleIDsWithCompletionHandler:"
+ "_filterOutHiddenApps"
+ "_gmStatusQueue"
+ "_gmsNotifyToken"
+ "_isAvailableForUseCaseIdentifiers:"
+ "_isMail"
+ "_isNotes"
+ "_isPhotos"
+ "_isPommesCtl"
+ "_isPommesZKW"
+ "_isSafari"
+ "_isSearch"
+ "_isSettings"
+ "_isSpotlight"
+ "_isTopHit"
+ "_kMDItemEvictedDuringImport"
+ "_kMDItemExtractedCurrenciesValues"
+ "_kMDItemExtractedDatesValues"
+ "_kMDItemExtractedLocationsCountry"
+ "_kMDItemExtractedLocationsParent"
+ "_kMDItemExtractedLocationsValues"
+ "_kMDItemTextContentIsTranscribed"
+ "_location"
+ "_lockedLocalPeopleSuggestions"
+ "_lockedPeopleSuggestions"
+ "_lockedTokenSuggestions"
+ "_lockedlocalSuggestions"
+ "_nlpContextID"
+ "_parent"
+ "_rankingConfig"
+ "_rankingConfiguration"
+ "_suggestionRankingWeights"
+ "_suggestionsRanker"
+ "_useCaseStatus"
+ "collectSuggestions:"
+ "com.apple.CloudDocs.iCloudDriveFileProvider"
+ "com.apple.CloudDocs.iCloudDriveFileProviderManaged"
+ "com.apple.CoreSpotlight.ImportExtension"
+ "com.apple.FruitBasket"
+ "com.apple.corespotlight.gmStatusQueue"
+ "com.apple.gms.availability.notification"
+ "com.apple.photos.semanticSearch"
+ "currentLocalSuggestions"
+ "currentPeopleSuggestions"
+ "currentTokenSuggestions"
+ "enableExtendedEmbeddingTimeout"
+ "enablePommesRanking"
+ "enablePommesSuggestions"
+ "enableSemanticSearch"
+ "enableSuggestions"
+ "enableUniversalSuggestions"
+ "encodeURL:withSandboxExtensionData:"
+ "eventIsCancelled"
+ "eventUpdateStatus"
+ "fbi"
+ "fetchAttributesFromImportFileURL:bundleID:fileType:identifier:sandboxExtension:attributesWithCompletionHandler:"
+ "fetchFile:attributesWithSandbox:completionHandler:"
+ "fha"
+ "filterOutHiddenApps"
+ "i == sCSAttrInfoArray[i].attr"
+ "ifURLIsNotDataless:getResultOf:"
+ "initWithLocation:parent:country:lat:lng:confidence:"
+ "initWithPath:bundleId:"
+ "initWithQueryContext:"
+ "initWithRankingConfiguration:"
+ "initWithSearchableIndex:label:critical:cost:"
+ "isPhotosSemanticSearchAvailable"
+ "isPommesZKW"
+ "isPriority"
+ "isSearch"
+ "isSemanticSearchAvailable"
+ "isSpotlight"
+ "isTextPersonExtractionAvailable"
+ "isTopHit"
+ "kMDItemAppEntityTitle"
+ "kMDItemAuthorPhoneNumbers"
+ "kMDItemEventIsCancelled"
+ "kMDItemEventUpdateStatus"
+ "kMDItemIsPriority"
+ "kMDItemPhotosPhotographicStyles"
+ "kMDItemPrimaryRecipientPhoneNumbers"
+ "kMDItemPriorityStatus"
+ "kMDItemRecipientPhoneNumbers"
+ "kMDItemTextContentSummary"
+ "localMaxCount"
+ "location"
+ "moveFrom:"
+ "needsPriority"
+ "needsSummary"
+ "nlpContextID"
+ "other"
+ "parent"
+ "passbookIsPaymentPass"
+ "person"
+ "photosPhotographicStyles"
+ "qid=%ld - Finished (cancelled)"
+ "rankingConfiguration"
+ "rankingConfigurationWithMeContact:emailAddresses:phoneFavorites:vipList:clientBundle:isScopedSearch:isAdvancedSyntax:spotlightQuery:userQuery:tokenString:queryKind:isPeopleSearch:keyboardLanguage:"
+ "searchableItemsForIdentifiers:searchableItemsHandler:"
+ "setEventIsCancelled:"
+ "setEventUpdateStatus:"
+ "setFilterOutHiddenApps:"
+ "setIsTopHit:"
+ "setPassbookIsPaymentPass:"
+ "setPhotosPhotographicStyles:"
+ "setTextContentSummary:"
+ "setTranscribedTextContent:"
+ "setUpdateListenerOptions:"
+ "setUseCaseStatus:"
+ "suggestionRankingWeights"
+ "textContentSummary"
+ "textUnderstanding.TextPersonExtraction"
+ "throttle:"
+ "tokenRewrites"
+ "transcribedTextContent"
+ "unthrottle:"
+ "updateListenerOptions"
+ "updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:"
+ "useCaseStatus"
+ "v24@0:8@\"NSArray\"16"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\">24"
+ "v64@0:8@16@24@32@40@48@?56"
- "\vV"
- " queryString=%@"
- "-->"
- "-[CSFilesSearchQuery handleNotification:]"
- "-[CSSearchableIndexRequest initWithSearchableIndex:label:critical:]"
- "@48@0:8@16d24d32d40"
- "@90@0:8^@16Q24^Q32@40@48^s56Q64{CSUnpackInfo=sssss}72@82"
- "AMP"
- "CSFilesSearchQuery.m"
- "Invalid query string"
- "Resumed \"%s\""
- "Suspended \"%s\""
- "T@\"NSMutableSet\",&,N,V_processedItems"
- "TB,N,V_completed"
- "TB,N,V_completions"
- "T^{__MDQuery=},N,V_mdQuery"
- "_completed"
- "_context.live"
- "_processedItems"
- "amp"
- "com.apple.corespotlight.csfilessearchquery"
- "completed"
- "completions"
- "handleNotification:"
- "initWithLocationID:lat:lng:confidence:"
- "processedItems"
- "rankingConfigurationWithMeContact:emailAddresses:phoneFavorites:vipList:clientBundle:isScopedSearch:spotlightQuery:userQuery:tokenString:queryKind:isPeopleSearch:keyboardLanguage:"
- "setCompleted:"
- "setCompletions:"
- "setProcessedItems:"
- "updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:"

```
