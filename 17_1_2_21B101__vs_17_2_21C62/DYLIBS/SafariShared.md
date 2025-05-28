## SafariShared

> `/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared`

```diff

-616.2.9.10.13
-  __TEXT.__text: 0x16157c
-  __TEXT.__auth_stubs: 0x1b20
-  __TEXT.__objc_methlist: 0xee10
-  __TEXT.__gcc_except_tab: 0x19088
-  __TEXT.__cstring: 0x18d7e
-  __TEXT.__const: 0x54cc8
-  __TEXT.__oslogstring: 0xeb21
-  __TEXT.__ustring: 0xd9be
-  __TEXT.__dlopen_cstrs: 0x209
-  __TEXT.__unwind_info: 0xa388
+617.1.17.10.9
+  __TEXT.__text: 0x162eb8
+  __TEXT.__auth_stubs: 0x1af0
+  __TEXT.__objc_methlist: 0xef60
+  __TEXT.__gcc_except_tab: 0x191e0
+  __TEXT.__cstring: 0x18769
+  __TEXT.__const: 0x54dc8
+  __TEXT.__oslogstring: 0xe9a6
+  __TEXT.__ustring: 0xd9b6
+  __TEXT.__dlopen_cstrs: 0x1b3
+  __TEXT.__unwind_info: 0xa404
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x2ccb
-  __TEXT.__objc_methname: 0x2dec8
-  __TEXT.__objc_methtype: 0xb741
-  __TEXT.__objc_stubs: 0x192a0
-  __DATA_CONST.__got: 0x4b0
-  __DATA_CONST.__const: 0x134a8
-  __DATA_CONST.__objc_classlist: 0x9e8
+  __TEXT.__objc_classname: 0x2cee
+  __TEXT.__objc_methname: 0x2e40c
+  __TEXT.__objc_methtype: 0xb7f3
+  __TEXT.__objc_stubs: 0x19500
+  __DATA_CONST.__got: 0x4e0
+  __DATA_CONST.__const: 0x13598
+  __DATA_CONST.__objc_classlist: 0x9f8
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x17b20
-  __DATA_CONST.__objc_selrefs: 0x8978
-  __DATA_CONST.__objc_arraydata: 0x2d20
-  __AUTH_CONST.__const: 0x2860
-  __AUTH_CONST.__objc_const: 0x7b88
-  __AUTH_CONST.__cfstring: 0x1d800
-  __AUTH_CONST.__objc_arrayobj: 0x3c0
+  __DATA_CONST.__objc_const: 0x17d20
+  __DATA_CONST.__objc_selrefs: 0x8a50
+  __DATA_CONST.__objc_arraydata: 0xdd8
+  __AUTH_CONST.__const: 0x28f0
+  __AUTH_CONST.__objc_const: 0x7ca8
+  __AUTH_CONST.__cfstring: 0x16380
+  __AUTH_CONST.__objc_arrayobj: 0x3a8
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__auth_got: 0xda8
-  __AUTH.__objc_data: 0x3200
+  __AUTH_CONST.__auth_got: 0xd90
+  __AUTH.__objc_data: 0x32a0
   __DATA.__objc_protorefs: 0x80
-  __DATA.__objc_classrefs: 0xbd0
-  __DATA.__objc_superrefs: 0x7f0
-  __DATA.__objc_ivar: 0x127c
+  __DATA.__objc_classrefs: 0xc00
+  __DATA.__objc_superrefs: 0x7f8
+  __DATA.__objc_ivar: 0x1294
   __DATA.__data: 0x2c20
-  __DATA.__bss: 0x730
+  __DATA.__bss: 0x710
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3110
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x5e8
+  __DATA_DIRTY.__bss: 0x5b8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/Calculate.framework/Calculate
   - /System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures
   - /System/Library/PrivateFrameworks/ContextKit.framework/ContextKit

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 8435
-  Symbols:   28881
-  CStrings:  12489
+  Functions: 8464
+  Symbols:   28979
+  CStrings:  11598
 
Symbols:
+ +[WBSCGImage imageByAdoptingCGImage:]
+ +[WBSCGImage imageWithCGImage:]
+ +[WBSCyclerRandomnessUtilities _randomStringWithCharactersFromString:withMaximumLength:]
+ +[WBSCyclerRandomnessUtilities randomStringWithMaximumLength:]
+ +[WBSFormAutoFillTestSupport stringRepresentationFromMetadataProvider:]
+ +[WBSFrequentlyVisitedSitesController newRadarProblemURLForHistoryItem:]
+ +[WBSURLCompletionDatabase _topHitFromBaseURLMatchForTopHitFromMatches:shouldReplaceTopHitFromMatches:historyMatches:bookmarkMatches:typedString:searchParameters:timeNow:completionDataSource:].cold.6
+ +[WBSURLCompletionDatabase _topHitFromBaseURLMatchForTopHitFromMatches:shouldReplaceTopHitFromMatches:historyMatches:bookmarkMatches:typedString:searchParameters:timeNow:completionDataSource:].cold.7
+ +[WBSURLCompletionDatabase _topHitFromBaseURLMatchForTopHitFromMatches:shouldReplaceTopHitFromMatches:historyMatches:bookmarkMatches:typedString:searchParameters:timeNow:completionDataSource:].cold.8
+ -[NSString(SafariSharedExtras) safari_ensurePathExtension:]
+ -[NSString(SafariSharedExtras) safari_lastPathComponentWithoutZipExtension]
+ -[NSString(SafariSharedExtras) safari_stringByAddingSoftBreaksBeforePeriods]
+ -[NSString(SafariSharedExtras) safari_stringByReplacingLastOccurrenceOfWhitespaceWithANonBreakingSpace]
+ -[NSString(SafariSharedExtras) safari_stringByReplacingMarkupCharactersWithHTMLEntities]
+ -[NSString(SafariSharedExtras) safari_urlHashesOfComponents]
+ -[NSURL(SafariSharedExtras) safari_hasFeedScheme]
+ -[NSURL(SafariSharedExtras) safari_userVisibleScheme]
+ -[WBSBiomeDonationManager _biomePageLoadDeviceClassForUserAgent:]
+ -[WBSBiomeDonationManager _pageLoadStream]
+ -[WBSBiomeDonationManager donatePageLoadWithUserAgent:wasSearch:wasPrivateBrowsing:wasActualized:provenance:]
+ -[WBSBookmarkAndHistoryCompletionMatch matchesAutocompleteTrigger]
+ -[WBSBookmarkAndHistoryCompletionMatch uuidString]
+ -[WBSCGImage CGImage]
+ -[WBSCGImage dealloc]
+ -[WBSCompletionQuery _bagOfWordsContainsString:]
+ -[WBSEncryptedCloudKeyValueStore _pcsIdentitySet]
+ -[WBSEncryptedCloudKeyValueStore _pcsShareProtection]
+ -[WBSEncryptedCloudKeyValueStore _setPCSIdentitySet:]
+ -[WBSEncryptedCloudKeyValueStore _setPCSShareProtection:]
+ -[WBSFormControlMetadata category]
+ -[WBSFormDataController locale]
+ -[WBSFormDataController setLocale:]
+ -[WBSFormDataController shouldForceUSLocaleForAutoFillFillingTest]
+ -[WBSFormMetadataController finishedAutoFillingOneTimeCode:inFrame:shouldSubmit:]
+ -[WBSMutableFormControlMetadata setCategory:]
+ -[WBSOfflineSearchSuggestionsFetcher currentQuery]
+ -[WBSQuickWebsiteSearchController clearWithCompletionHandler:]
+ -[WBSQuickWebsiteSearchController providersMatchingQueryString:excludingSearchEngineHostSuffixes:]
+ -[WBSQuickWebsiteSearchController providersMatchingString:excludingSearchEngineHostSuffixes:]
+ -[WBSQuickWebsiteSearchController removeProvidersWithHosts:completionHandler:]
+ -[WBSQuickWebsiteSearchController savePendingChangesNowWithCompletionHandler:]
+ -[WBSQuickWebsiteSearchController setSearchURLTemplateFromForm:forSourcePageURLString:completionHandler:]
+ -[WBSReaderAvailabilityCheckResult combinedMetadataForTests]
+ -[WBSReaderFont _createFontDescriptorRefForFontFamilyName:restrictToEnabled:]
+ -[WBSURLCompletionMatch matchesAutocompleteTrigger]
+ -[WBSURLCompletionMatch uuidString]
+ _BMAppWebAppInFocusIdentifier
+ _BMSafariAutoPlayIdentifier
+ _BMSafariNavigationsIdentifier
+ _BMSafariPageLoadIdentifier
+ _BMSafariWebPagePerformanceIdentifier
+ _BiomeLibrary
+ _CGImageRelease
+ _CGImageRetain
+ _OBJC_CLASS_$_BMSafariAutoPlay
+ _OBJC_CLASS_$_BMSafariNavigations
+ _OBJC_CLASS_$_BMSafariPageLoad
+ _OBJC_CLASS_$_BMSafariWebPagePerformance
+ _OBJC_CLASS_$_BMWebAppInFocus
+ _OBJC_CLASS_$_WBSCGImage
+ _OBJC_CLASS_$_WBSFormAutoFillTestSupport
+ _OBJC_IVAR_$_WBSBiomeDonationManager._pageLoadStream
+ _OBJC_IVAR_$_WBSCGImage._CGImage
+ _OBJC_IVAR_$_WBSFormControlMetadata._category
+ _OBJC_IVAR_$_WBSFormDataController._locale
+ _OBJC_IVAR_$_WBSOfflineSearchSuggestionsFetcher._currentQuery
+ _OBJC_IVAR_$_WBSURLCompletionMatch._uuidString
+ _OBJC_METACLASS_$_WBSCGImage
+ _OBJC_METACLASS_$_WBSFormAutoFillTestSupport
+ _WBSDebugAutoFillConsoleLoggingEnabledPreferenceKey
+ _WBSFormMetadataControlCategoryKey
+ _WBSJSTestPathToElementFunctionScript
+ _WBSLastPrivateSearchEngineStringExplicitlyChosenByUserKey
+ _WBSNSBundleLSApplicationCategoryTypeKey
+ _WBSPeriodicSyncSuccessesCount
+ _WBSProfileNameCharacterCountLimit
+ _WBSReaderTestMetadataTextSamplesKey
+ __OBJC_$_CLASS_METHODS_WBSCGImage
+ __OBJC_$_CLASS_METHODS_WBSFormAutoFillTestSupport
+ __OBJC_$_CLASS_METHODS_WBSFrequentlyVisitedSitesController
+ __OBJC_$_INSTANCE_METHODS_WBSCGImage
+ __OBJC_$_INSTANCE_VARIABLES_WBSCGImage
+ __OBJC_$_PROP_LIST_WBSCGImage
+ __OBJC_CLASS_RO_$_WBSCGImage
+ __OBJC_CLASS_RO_$_WBSFormAutoFillTestSupport
+ __OBJC_METACLASS_RO_$_WBSCGImage
+ __OBJC_METACLASS_RO_$_WBSFormAutoFillTestSupport
+ __Z16WTFCrashWithInfoiPKcS0_i
+ __ZL32logCompletionMatchToDebugChannelP8NSStringP21WBSURLCompletionMatch
+ __ZL32logCompletionMatchToDebugChannelP8NSStringP21WBSURLCompletionMatch.cold.1
+ __ZL32logCompletionMatchToDebugChannelP8NSStringP21WBSURLCompletionMatch.cold.2
+ __ZL32logCompletionMatchToDebugChannelP8NSStringPN12SafariShared33BookmarkAndHistoryCompletionMatchE
+ __ZN12SafariShared18ReaderJSController15fullArticleHTMLEv
+ __ZN12SafariShared22ExtensionURLTranslatorC1Ev
+ __ZN12SafariShared22ExtensionURLTranslatorC2Ev
+ __ZN12SafariShared25ArticleFinderJSController17nextPageURLStringEv
+ __ZN12SafariShared25ArticleFinderJSController18articleTitleStringEv
+ __ZN12SafariShared25ArticleFinderJSController20adoptableArticleHTMLEv
+ __ZN12SafariShared25ArticleFinderJSController20pathToArticleElementEv
+ __ZN12SafariShared25ArticleFinderJSController34multiPageContentElementsPathStringEv
+ __ZN12SafariShared25ArticleFinderJSController50evaluateSupportJavaScriptForReaderTestsIfNecessaryEv
+ __ZN12SafariShared33BookmarkAndHistoryCompletionMatch10uuidStringEv
+ __ZN12SafariSharedL30jsIsDebugConsoleLoggingEnabledEPK15OpaqueJSContextP13OpaqueJSValueP14OpaqueJSStringPPKS3_
+ __ZN12SafariSharedL5jsLogEPK15OpaqueJSContextP13OpaqueJSValueS4_mPKPKS3_PS6_.cold.1
+ __ZN3WTF16VectorDestructorILb1ENS_6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS_12RawPtrTraitsIS3_EENS_21DefaultRefDerefTraitsIS3_EEEEE8destructEPS8_SA_
+ __ZN3WTF3RefIN12SafariShared33BookmarkAndHistoryCompletionMatchENS_12RawPtrTraitsIS2_EEED2Ev
+ __ZNKSt3__114default_deleteIN12SafariShared33BookmarkAndHistoryCompletionMatchEEclB7v160006EPS2_
+ __ZNSt3__110__pop_heapB7v160006INS_17_ClassicAlgPolicyEPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_SG_RT0_NS_15iterator_traitsISG_E15difference_typeE.cold.1
+ __ZNSt3__111__sift_downB7v160006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_OT0_NS_15iterator_traitsISH_E15difference_typeESH_.cold.1
+ __ZNSt3__118__insertion_sort_3B7v160006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_SH_T0_.cold.1
+ __ZNSt3__127__insertion_sort_incompleteIRPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEESB_EPS9_EEbT0_SG_T_.cold.1
+ __ZNSt3__19__sift_upB7v160006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_SH_OT0_NS_15iterator_traitsISH_E15difference_typeE.cold.1
+ __ZZ60-[NSString(SafariSharedExtras) safari_urlHashesOfComponents]E4salt
+ __ZZ60-[NSString(SafariSharedExtras) safari_urlHashesOfComponents]E9onceToken
+ ___105-[WBSQuickWebsiteSearchController setSearchURLTemplateFromForm:forSourcePageURLString:completionHandler:]_block_invoke
+ ___105-[WBSQuickWebsiteSearchController setSearchURLTemplateFromForm:forSourcePageURLString:completionHandler:]_block_invoke_2
+ ___105-[WBSQuickWebsiteSearchController setSearchURLTemplateFromForm:forSourcePageURLString:completionHandler:]_block_invoke_3
+ ___109-[WBSBiomeDonationManager donatePageLoadWithUserAgent:wasSearch:wasPrivateBrowsing:wasActualized:provenance:]_block_invoke
+ ___47-[WBSEncryptedCloudKeyValueStore decryptEntry:]_block_invoke
+ ___56-[WBSBiomeDonationManager _clearEventsDonatedSinceDate:]_block_invoke_5
+ ___58-[WBSEncryptedCloudKeyValueStore _currentPCSConfiguration]_block_invoke
+ ___60-[NSString(SafariSharedExtras) safari_urlHashesOfComponents]_block_invoke
+ ___60-[NSString(SafariSharedExtras) safari_urlHashesOfComponents]_block_invoke_2
+ ___62-[WBSQuickWebsiteSearchController clearWithCompletionHandler:]_block_invoke
+ ___71+[WBSFormAutoFillTestSupport stringRepresentationFromMetadataProvider:]_block_invoke
+ ___72+[WBSFrequentlyVisitedSitesController newRadarProblemURLForHistoryItem:]_block_invoke
+ ___72+[WBSFrequentlyVisitedSitesController newRadarProblemURLForHistoryItem:]_block_invoke.25
+ ___78-[WBSQuickWebsiteSearchController removeProvidersWithHosts:completionHandler:]_block_invoke
+ ___78-[WBSQuickWebsiteSearchController removeProvidersWithHosts:completionHandler:]_block_invoke_2
+ ___78-[WBSQuickWebsiteSearchController removeProvidersWithHosts:completionHandler:]_block_invoke_3
+ ___93-[WBSQuickWebsiteSearchController providersMatchingString:excludingSearchEngineHostSuffixes:]_block_invoke
+ ___93-[WBSQuickWebsiteSearchController providersMatchingString:excludingSearchEngineHostSuffixes:]_block_invoke_2
+ ___93-[WBSQuickWebsiteSearchController providersMatchingString:excludingSearchEngineHostSuffixes:]_block_invoke_3
+ ___93-[WBSQuickWebsiteSearchController providersMatchingString:excludingSearchEngineHostSuffixes:]_block_invoke_4
+ ___block_descriptor_32_e30_"NSMutableString"24?0r^i8Q16l
+ ___block_descriptor_32_e43_"NSMutableDictionary"16?0"NSDictionary"8l
+ ___block_descriptor_40_e8_32s_e58_v32?0^{OpaqueFormAutoFillFrame=}8"WBSFormMetadata"16^B24ls32l8
+ ___block_descriptor_48_e8_32s40s_e25_v32?0"NSString"816^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e29_v32?0"NSDictionary"8Q16^B24ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e35_v32?0"NSString"8"NSString"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32r40r48r_e5_v8?0lr32l8r40l8r48l8
+ ___block_descriptor_64_ea8_32s40bs48r56r_e5_v8?0lr48l8s40l8s32l8r56l8
+ ___block_descriptor_64_ea8_32s40s48s56s_e56_v32?0"NSString"8"WBSQuickWebsiteSearchProvider"16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_ea8_32s40s48s56s64s_e24_v32?0{_NSRange=QQ}8^B24ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.419
+ ___block_literal_global.441
+ ___block_literal_global.444
+ ___block_literal_global.446
+ ___block_literal_global.448
+ ___block_literal_global.450
+ ___controlDescription_block_invoke
+ ___sanitizedFormMetadata_block_invoke
+ ___sanitizedFormMetadata_block_invoke_2
+ ___sanitizedMetadata_block_invoke
+ __unnamed_array_storage.236
+ __unnamed_array_storage.248
+ __unnamed_array_storage.577
+ __unnamed_array_storage.604
+ _objc_msgSend$_bagOfWordsContainsString:
+ _objc_msgSend$_biomePageLoadDeviceClassForUserAgent:
+ _objc_msgSend$_createFontDescriptorRefForFontFamilyName:restrictToEnabled:
+ _objc_msgSend$_pageLoadStream
+ _objc_msgSend$_randomStringWithCharactersFromString:withMaximumLength:
+ _objc_msgSend$_setPCSIdentitySet:
+ _objc_msgSend$_setPCSShareProtection:
+ _objc_msgSend$compare:options:
+ _objc_msgSend$containsEmptyComponents
+ _objc_msgSend$dailyVisitCountScoresCountOnSynchronizationQueue
+ _objc_msgSend$dailyVisitCountScoresPtrOnSynchronizationQueue
+ _objc_msgSend$finishedAutoFillingOneTimeCode:inFrame:shouldSubmit:
+ _objc_msgSend$formCount
+ _objc_msgSend$hostname
+ _objc_msgSend$initWithSearch:visited:mode:platform:userAgent:countryCode:entryPoint:actualized:
+ _objc_msgSend$isSearchEvaluationLoggingEnabled
+ _objc_msgSend$isSpeculative
+ _objc_msgSend$kind
+ _objc_msgSend$locale
+ _objc_msgSend$operatingSystemVersionString
+ _objc_msgSend$providersMatchingString:excludingSearchEngineHostSuffixes:
+ _objc_msgSend$randomStringWithMaximumLength:
+ _objc_msgSend$removeProvidersWithHosts:completionHandler:
+ _objc_msgSend$safari_caseAndDiacriticInsensitiveStandardRangeOfString:additionalOptions:
+ _objc_msgSend$safari_hostComponentsEnumerator
+ _objc_msgSend$safari_isLaterThanDate:
+ _objc_msgSend$safari_urlHashesOfComponents
+ _objc_msgSend$setComponentName:
+ _objc_msgSend$setComponentVersion:
+ _objc_msgSend$setDescriptionText:
+ _objc_msgSend$shouldForceUSLocaleForAutoFillFillingTest
+ _objc_msgSend$stringByAppendingPathExtension:
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$weeklyVisitCountScoresCountOnSynchronizationQueue
+ _objc_msgSend$weeklyVisitCountScoresPtrOnSynchronizationQueue
+ _sanitizedMetadata
- +[NSString(SafariSharedExtras) safari_detailStringWithTitleString:prompt:]
- +[WBSCyclerRandomnessUtilities _randomStringWithCharactersFromString:]
- -[NSString(SafariSharedExtras) safari_favoritesTitleWithEmojiForRTL:]
- -[NSString(SafariSharedExtras) safari_isPathExtensionAllowedForAnalytics]
- -[NSString(SafariSharedExtras) safari_stringByRemovingTopLevelDomainFromHost]
- -[NSURL(SafariSharedExtras) safari_URLWithUniqueFilename]
- -[NSURL(SafariSharedExtras) safari_hasScheme:]
- -[WBSBiomeDonationManager _autoPlayStream].cold.1
- -[WBSBiomeDonationManager _navigationsStream].cold.1
- -[WBSBiomeDonationManager _webAppInFocusStream].cold.1
- -[WBSBiomeDonationManager _webPagePerformanceStream].cold.1
- -[WBSCloudTabStore closeTabs:onDevice:]
- -[WBSCloudTabStore closeTabs:onDevice:].cold.1
- -[WBSEncryptedCloudKeyValueStore .cxx_construct]
- -[WBSFormMetadataController finishedAutoFillingOneTimeCodeInFrame:shouldSubmit:]
- -[WBSQuickWebsiteSearchController clear]
- -[WBSQuickWebsiteSearchController providersMatchingQueryString:]
- -[WBSQuickWebsiteSearchController providersMatchingString:]
- -[WBSQuickWebsiteSearchController removeProvidersWithHosts:]
- -[WBSQuickWebsiteSearchController setSearchURLTemplateFromForm:forSourcePageURLString:]
- -[WBSReaderFont _fontDescriptorRefForFontFamilyName:restrictToEnabled:]
- -[WBSRecentWebSearchesController _addLegacySearch:]
- -[WBSRecentWebSearchesController _migrateLegacyData]
- -[WBSRecentWebSearchesController _removeLegacyRecentSearchesData]
- -[_WBSBiomeStream _fetchStream].cold.2
- _BiomeLibraryLibrary
- _BiomeLibraryLibrary.cold.1
- _BiomeLibraryLibraryCore
- _BiomeLibraryLibraryCore.frameworkLibrary
- _CFRunLoopTimerInvalidate
- _CFRunLoopTimerIsValid
- _WBSChromeExtensionURLScheme
- _WBSParsecABGroupIdentifierGenerationDatePreferenceKey
- _WBSParsecABGroupIdentifierPreferenceKey
- __CFHostIsDomainTopLevel
- __ZGVZ73-[NSString(SafariSharedExtras) safari_isPathExtensionAllowedForAnalytics]E16allowedMIMETypes
- __ZL10fileExistsP5NSURL
- __ZL20firstTopHitCandidateRKN3WTF6VectorINS_6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS_12RawPtrTraitsIS3_EENS_21DefaultRefDerefTraitsIS3_EEEELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEEEP31WBSURLCompletionUserTypedStringP19WBSSearchParameters.cold.1
- __ZL32logCompletionMatchToDebugChannelP8NSStringPKN12SafariShared33BookmarkAndHistoryCompletionMatchE
- __ZL36isSchemeThatDoesNotRequireSlashInURLP8NSString
- __ZN12SafariShared12JSControllerC2Ev
- __ZN3WTF17dynamic_objc_castI7JSValueEEPT_P11objc_object
- __ZN3WTF6VectorINS_6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS_12RawPtrTraitsIS3_EENS_21DefaultRefDerefTraitsIS3_EEEELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE6shrinkEm
- __ZN3WTF9RetainPtrIP19_PCSIdentitySetDataEaSERKS3_
- __ZN3WTF9RetainPtrIP25_OpaquePCSShareProtectionEaSERKS3_
- __ZN3WTF9RetainPtrIPK8__CFDataEaSERKS4_
- __ZNK3WTF10RefCountedIN12SafariShared33BookmarkAndHistoryCompletionMatchENSt3__114default_deleteIS2_EEE5derefEv
- __ZZ73-[NSString(SafariSharedExtras) safari_isPathExtensionAllowedForAnalytics]E16allowedMIMETypes
- ___100+[WBSResultRanker filterOutUnlikelyMatchesBeforeTopHitPromotionFromMatches:forQuery:searchProvider:]_block_invoke.cold.1
- ___100+[WBSResultRanker filterOutUnlikelyMatchesBeforeTopHitPromotionFromMatches:forQuery:searchProvider:]_block_invoke.cold.2
- ___40-[WBSQuickWebsiteSearchController clear]_block_invoke
- ___59-[WBSQuickWebsiteSearchController providersMatchingString:]_block_invoke
- ___59-[WBSQuickWebsiteSearchController providersMatchingString:]_block_invoke_2
- ___59-[WBSQuickWebsiteSearchController providersMatchingString:]_block_invoke_3
- ___59-[WBSQuickWebsiteSearchController providersMatchingString:]_block_invoke_4
- ___60-[WBSQuickWebsiteSearchController removeProvidersWithHosts:]_block_invoke
- ___60-[WBSQuickWebsiteSearchController removeProvidersWithHosts:]_block_invoke_2
- ___60-[WBSQuickWebsiteSearchController removeProvidersWithHosts:]_block_invoke_3
- ___67+[WBSResultRanker dedupeSameURLResults:withUniversalSearchResults:]_block_invoke.cold.1
- ___69-[NSString(SafariSharedExtras) safari_favoritesTitleWithEmojiForRTL:]_block_invoke
- ___69-[NSString(SafariSharedExtras) safari_favoritesTitleWithEmojiForRTL:]_block_invoke_2
- ___76+[WBSResultRanker dedupeResults:withSearchSuggestionStrings:searchProvider:]_block_invoke.cold.1
- ___77-[NSString(SafariSharedExtras) safari_stringByRemovingTopLevelDomainFromHost]_block_invoke
- ___79+[WBSResultRanker filterOutUnlikelyMatchesFromTopHits:forQuery:searchProvider:]_block_invoke.cold.1
- ___87-[WBSQuickWebsiteSearchController setSearchURLTemplateFromForm:forSourcePageURLString:]_block_invoke
- ___87-[WBSQuickWebsiteSearchController setSearchURLTemplateFromForm:forSourcePageURLString:]_block_invoke_2
- ___87-[WBSQuickWebsiteSearchController setSearchURLTemplateFromForm:forSourcePageURLString:]_block_invoke_3
- ___BiomeLibraryLibraryCore_block_invoke
- ___block_descriptor_40_ea8_32r_e25_v32?0"NSString"8Q16^B24lr32l8
- ___block_descriptor_56_ea8_32s40s48s_e56_v32?0"NSString"8"WBSQuickWebsiteSearchProvider"16^B24ls32l8s40l8s48l8
- ___block_descriptor_57_ea8_32s40s48r_e8_v12?0B8ls32l8s40l8r48l8
- ___block_descriptor_58_ea8_32s40s48r_e52_v56?0"NSString"8{_NSRange=QQ}16{_NSRange=QQ}32^B48ls32l8s40l8r48l8
- ___block_descriptor_72_ea8_32s40s48s56s_e24_v32?0{_NSRange=QQ}8^B24ls32l8s40l8s48l8s56l8
- ___block_literal_global.410
- ___block_literal_global.431
- ___block_literal_global.434
- ___block_literal_global.436
- ___block_literal_global.438
- ___block_literal_global.440
- ___block_literal_global.98
- ___getBMAppWebAppInFocusIdentifierSymbolLoc_block_invoke
- ___getBMSafariAutoPlayClass_block_invoke
- ___getBMSafariAutoPlayIdentifierSymbolLoc_block_invoke
- ___getBMSafariNavigationsClass_block_invoke
- ___getBMSafariNavigationsIdentifierSymbolLoc_block_invoke
- ___getBMSafariWebPagePerformanceClass_block_invoke
- ___getBMSafariWebPagePerformanceIdentifierSymbolLoc_block_invoke
- ___getBMWebAppInFocusClass_block_invoke
- ___getBiomeLibrarySymbolLoc_block_invoke
- __unnamed_array_storage.233
- __unnamed_array_storage.245
- __unnamed_array_storage.574
- __unnamed_array_storage.598
- _audit_stringBiomeLibrary
- _dlerror
- _dlsym
- _getBMAppWebAppInFocusIdentifierSymbolLoc.ptr
- _getBMSafariAutoPlayClass.softClass
- _getBMSafariAutoPlayIdentifierSymbolLoc.ptr
- _getBMSafariNavigationsClass.softClass
- _getBMSafariNavigationsIdentifierSymbolLoc.ptr
- _getBMSafariWebPagePerformanceClass
- _getBMSafariWebPagePerformanceClass.softClass
- _getBMSafariWebPagePerformanceIdentifierSymbolLoc.ptr
- _getBMWebAppInFocusClass.softClass
- _getBiomeLibrarySymbolLoc.ptr
- _lstat
- _objc_msgSend$URLByAppendingPathExtension:
- _objc_msgSend$URLByDeletingPathExtension
- _objc_msgSend$_fontDescriptorRefForFontFamilyName:restrictToEnabled:
- _objc_msgSend$_isSingleEmoji
- _objc_msgSend$_migrateLegacyData
- _objc_msgSend$_randomStringWithCharactersFromString:
- _objc_msgSend$_removeLegacyRecentSearchesData
- _objc_msgSend$finishedAutoFillingOneTimeCodeInFrame:shouldSubmit:
- _objc_msgSend$initWithArray:
- _objc_msgSend$initWithDomain:visited:platform:performanceEvent:
- _objc_msgSend$initWithDomain:visited:signal:countryCode:
- _objc_msgSend$instancesRespondToSelector:
- _objc_msgSend$providersMatchingString:
- _objc_msgSend$randomString
- _objc_msgSend$removeProvidersWithHosts:
- _objc_msgSend$safari_isRightToLeft
- _objc_msgSend$safari_reverseEnumerateComponents:usingBlock:
CStrings:
+ "\x05\x18"
+ "\x0f\x03"
+ "%.2X"
+ "%@"
+ "%@: \"%{sensitive}@\""
+ "%@: (%{public}8s) %.6f <%{public}@> \"%{public}@\" [%{public}@] (%{public}s) %@"
+ "%@: [%{public}@]"
+ "%d"
+ "&#x27;"
+ "&#x2F;"
+ "&nbsp;"
+ "&quot;"
+ "* DIAGNOSTIC INFORMATION\n"
+ "* SUMMARY\nProvide a detailed explanation of the issue, with steps to reproduce if possible.\n\n"
+ "+[WBSFrequentlyVisitedSitesController newRadarProblemURLForHistoryItem:]"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/__hash_table"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/__utility/exception_guard.h"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/deque"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/vector"
+ "/Library/Caches/com.apple.xbs/Sources/SafariShared/SafariShared/FrequentlyVisitedSites/WBSFrequentlyVisitedSitesController.mm"
+ "00"
+ "<ControlFieldName '%@', ControlCategory '%@', control index %lu>"
+ "<ControlFieldName '%@', control index %lu>"
+ "<Invalid WBSAutoFillFormType %d>"
+ "@\"NSLocale\""
+ "@\"NSMutableDictionary\"16@?0@\"NSDictionary\"8"
+ "@\"NSMutableString\"24@?0r^i8Q16"
+ "@\"WBSCompletionQuery\""
+ "@24@0:8^{CGImage=}16"
+ "AutoFillableLoginForm"
+ "AutoFillableStandardForm"
+ "B24@0:8@\"<WBSCloudTabProvider>\"16"
+ "CGImage"
+ "ChangePasswordForm"
+ "ConfirmPasswordElement"
+ "ControlCategory"
+ "Daily visit count scores: %@\n"
+ "Excluding TopHit that matches www subdomain"
+ "Excluding URL match that is a client or server error"
+ "Excluding URL that matches www subdomain"
+ "Excluding duplicate match with URL"
+ "Excluding duplicate match with search suggestion"
+ "Failed to find ID of visit %{public}@ of item %{sensitive}@: %{public}@"
+ "FirstCreditCardCardholderFieldOrCreditCardNumberField"
+ "Frequently Visited Sites: Issue with %@"
+ "LSApplicationCategoryType"
+ "Last visited: %@ (time interval: %f)\n"
+ "NewAccountForm"
+ "No forms exist on this page.\n"
+ "NonAutoFillableForm"
+ "OldPasswordElement"
+ "Operating system: %@"
+ "PasswordElement"
+ "ReaderJS.sanitizedFullArticle().outerHTML"
+ "Safari Start Page"
+ "Score time interval: %f\n"
+ "T@\"NSLocale\",&,N,V_locale"
+ "T@\"NSString\",R,C,N,V_category"
+ "T@\"NSString\",R,C,N,V_uuidString"
+ "T@\"WBSCompletionQuery\",&,N,V_currentQuery"
+ "T^{CGImage=},R,N,V_CGImage"
+ "T^{_OpaquePCSShareProtection=},N,G_pcsShareProtection,S_setPCSShareProtection:,V_pcsShareProtection"
+ "T^{_PCSIdentitySetData=},N,G_pcsIdentitySet,S_setPCSIdentitySet:,V_pcsIdentitySet"
+ "URL: %@\n"
+ "UndeterminedAutoFillFormType"
+ "UsernameElement"
+ "WBSCGImage"
+ "WBSDebugAutoFillConsoleLoggingEnabled"
+ "WBSFormAutoFillTestSupport"
+ "WBSLastPrivateSearchEngineStringExplicitlyChosenByUserKey"
+ "WBSPeriodicSyncSuccessesCount"
+ "Weekly visit count scores: %@\n"
+ "Will replace topHitFromMatches with redirection baseURL"
+ "^{CGImage=}"
+ "^{CGImage=}16@0:8"
+ "^{_OpaquePCSShareProtection=}"
+ "^{_OpaquePCSShareProtection=}16@0:8"
+ "^{_PCSIdentitySetData=}"
+ "^{_PCSIdentitySetData=}16@0:8"
+ "^{__CTFontDescriptor=}28@0:8@16B24"
+ "_CGImage"
+ "_bagOfWordsContainsString:"
+ "_biomePageLoadDeviceClassForUserAgent:"
+ "_category"
+ "_createFontDescriptorRefForFontFamilyName:restrictToEnabled:"
+ "_locale"
+ "_pageLoadStream"
+ "_randomStringWithCharactersFromString:withMaximumLength:"
+ "_setPCSIdentitySet:"
+ "_setPCSShareProtection:"
+ "_uuidString"
+ "about"
+ "articleTitle"
+ "blank"
+ "blank/"
+ "clearWithCompletionHandler:"
+ "combinedMetadataForTests"
+ "compare:options:"
+ "containsEmptyComponents"
+ "donatePageLoadWithUserAgent:wasSearch:wasPrivateBrowsing:wasActualized:provenance:"
+ "feed"
+ "feeds"
+ "finishedAutoFillingOneTimeCode:inFrame:shouldSubmit:"
+ "formCount"
+ "iOS"
+ "if (typeof pathToElementForTesting === 'undefined') var pathToElementForTesting = function(element) {var path = \"\";for (; element; element = element.parentElement) {var index = 0;for (var sibling = element; sibling; sibling = sibling.previousElementSibling)index++;path = \"/\" + index + path;}return path;};"
+ "imageByAdoptingCGImage:"
+ "imageWithCGImage:"
+ "initWithSearch:visited:mode:platform:userAgent:countryCode:entryPoint:actualized:"
+ "isDebugConsoleLoggingEnabled"
+ "isSearchEvaluationLoggingEnabled"
+ "isSpeculative"
+ "kind"
+ "locale"
+ "matchesAutocompleteTrigger"
+ "newRadarProblemURLForHistoryItem:"
+ "nextPageURL"
+ "operatingSystemVersionString"
+ "pathToElementForTesting(this.articleNode()); "
+ "pcsIdentitySet"
+ "pcsShareProtection"
+ "providersMatchingQueryString:excludingSearchEngineHostSuffixes:"
+ "providersMatchingString:excludingSearchEngineHostSuffixes:"
+ "randomStringWithMaximumLength:"
+ "removeProvidersWithHosts:completionHandler:"
+ "safari_caseAndDiacriticInsensitiveStandardRangeOfString:additionalOptions:"
+ "safari_ensurePathExtension:"
+ "safari_hasFeedScheme"
+ "safari_hostComponentsEnumerator"
+ "safari_isLaterThanDate:"
+ "safari_lastPathComponentWithoutZipExtension"
+ "safari_stringByAddingSoftBreaksBeforePeriods"
+ "safari_stringByReplacingLastOccurrenceOfWhitespaceWithANonBreakingSpace"
+ "safari_stringByReplacingMarkupCharactersWithHTMLEntities"
+ "safari_urlHashesOfComponents"
+ "safari_urlHashesOfComponents_salt"
+ "safari_userVisibleScheme"
+ "savePendingChangesNowWithCompletionHandler:"
+ "setCategory:"
+ "setSearchURLTemplateFromForm:forSourcePageURLString:completionHandler:"
+ "shouldForceUSLocaleForAutoFillFillingTest"
+ "stringByAppendingPathExtension:"
+ "stringByDeletingPathExtension"
+ "stringRepresentationFromMetadataProvider:"
+ "stringWithString:"
+ "this.containerElementsForMultiPageContent().map(pathToElementForTesting).join(' | ');"
+ "token"
+ "v24@0:8^{_OpaquePCSShareProtection=}16"
+ "v24@0:8^{_PCSIdentitySetData=}16"
+ "v44@0:8q16B24B28B32q36"
+ "var adoptableArticle = this.adoptableArticle();var allElements = adoptableArticle.getElementsByTagName('*');var numberOfElements = allElements.length;for (var i = 0; i < numberOfElements; ++i) {var element = allElements[i];element.removeAttribute(this.elementReaderUniqueIDAttributeKey());}adoptableArticle.removeAttribute(this.elementReaderUniqueIDAttributeKey());var articleHTML = adoptableArticle.outerHTML;var subhead = this.articleSubhead();var subheadHTML = '';if (subhead) {var subheadNode = document.createElement('h2');subheadNode.className = 'subhead';subheadNode.textContent = this.articleSubhead();subheadHTML = subheadNode.outerHTML}var metadataElement = this.adoptableMetadataBlock();if (metadataElement) {var allMetadataElements = metadataElement.getElementsByTagName('*');var numberOfMetadataElements = allMetadataElements.length;for (var i = 0; i < numberOfMetadataElements; ++i) {var element = allMetadataElements[i];element.removeAttribute(this.elementReaderUniqueIDAttributeKey());}}var metadataHTML = '';if (metadataElement && metadataElement.innerText) {metadataElement.className = 'metadata';metadataHTML = metadataElement.outerHTML;}articleHTML = subheadHTML + metadataHTML + articleHTML;articleHTML;"
+ "|"
- "\x021"
- "\x05\x17"
- "\x0f\x02"
- "%@ %@"
- "%@-%u"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__hash_table"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__utility/exception_guard.h"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/deque"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/vector"
- "123"
- "3dml"
- "3ds"
- "3g2"
- "3gp"
- "7z"
- "BMAppWebAppInFocusIdentifier"
- "BMSafariAutoPlay"
- "BMSafariAutoPlayIdentifier"
- "BMSafariNavigations"
- "BMSafariNavigationsIdentifier"
- "BMSafariWebPagePerformance"
- "BMSafariWebPagePerformanceIdentifier"
- "BMWebAppInFocus"
- "BiomeLibrary"
- "Closing %lu tabs on device with UUID %{public}@"
- "Closing multiple tabs %{private}@ on \"%{private}@\""
- "Excluding TopHit that matches www subdomain: \"%{sensitive}@\""
- "Excluding URL match that is a client or server error: \"%{sensitive}@\""
- "Excluding URL that matches www subdomain: \"%{sensitive}@\""
- "Excluding duplicate match with URL: \"%{sensitive}@\""
- "Excluding duplicate match with search suggestion: \"%{sensitive}@\""
- "Failed to find ID of visit %{public}@ of item %{private}@: %{public}@"
- "NSString *getBMAppWebAppInFocusIdentifier(void)"
- "NSString *getBMSafariAutoPlayIdentifier(void)"
- "NSString *getBMSafariNavigationsIdentifier(void)"
- "NSString *getBMSafariWebPagePerformanceIdentifier(void)"
- "URLByAppendingPathExtension:"
- "URLByDeletingPathExtension"
- "WBSBiomeDonationManager.m"
- "WBSParsecABGroupIdentifier"
- "WBSParsecABGroupIdentifierGenerationDate"
- "Will replace topHitFromMatches with redirection baseURL."
- "_addLegacySearch:"
- "_fontDescriptorRefForFontFamilyName:restrictToEnabled:"
- "_isSingleEmoji"
- "_migrateLegacyData"
- "_randomStringWithCharactersFromString:"
- "_removeLegacyRecentSearchesData"
- "aab"
- "aac"
- "aam"
- "aas"
- "abw"
- "ac"
- "acc"
- "ace"
- "acu"
- "acutc"
- "adp"
- "aep"
- "afm"
- "afp"
- "ahead"
- "ai"
- "aif"
- "aifc"
- "aiff"
- "air"
- "ait"
- "ami"
- "apk"
- "appcache"
- "application"
- "apr"
- "arc"
- "asc"
- "asf"
- "asm"
- "aso"
- "asx"
- "atc"
- "atom"
- "atomcat"
- "atomsvc"
- "atx"
- "au"
- "avi"
- "aw"
- "azf"
- "azs"
- "azw"
- "bat"
- "bcpio"
- "bdf"
- "bdm"
- "bed"
- "bh2"
- "bin"
- "blb"
- "blorb"
- "bmi"
- "bmp"
- "boz"
- "bpk"
- "btif"
- "bz"
- "bz2"
- "c11amc"
- "c11amz"
- "c4d"
- "c4f"
- "c4g"
- "c4p"
- "c4u"
- "cab"
- "caf"
- "cap"
- "car"
- "cat"
- "cb7"
- "cba"
- "cbr"
- "cbt"
- "cbz"
- "cc"
- "cct"
- "ccxml"
- "cdbcmsg"
- "cdf"
- "cdkey"
- "cdmia"
- "cdmic"
- "cdmid"
- "cdmio"
- "cdmiq"
- "cdx"
- "cdxml"
- "cdy"
- "cer"
- "cfs"
- "cgm"
- "chat"
- "chm"
- "chrome-extension"
- "chrt"
- "cif"
- "cii"
- "cil"
- "cla"
- "clkk"
- "clkp"
- "clkt"
- "clkw"
- "clkx"
- "closeTabs:onDevice:"
- "clp"
- "cmc"
- "cmdf"
- "cml"
- "cmp"
- "cmx"
- "cod"
- "com"
- "conf"
- "cpio"
- "cpp"
- "cpt"
- "crd"
- "crl"
- "crt"
- "cryptonote"
- "csh"
- "csml"
- "csp"
- "css"
- "cst"
- "csv"
- "cu"
- "curl"
- "cww"
- "cxt"
- "cxx"
- "dae"
- "daf"
- "dart"
- "dataless"
- "davmount"
- "dbk"
- "dcr"
- "dcurl"
- "dd2"
- "ddd"
- "deb"
- "def"
- "deploy"
- "der"
- "dfac"
- "dgc"
- "dic"
- "dif"
- "dir"
- "dis"
- "dist"
- "distz"
- "djv"
- "djvu"
- "dll"
- "dmg"
- "dmp"
- "dms"
- "dna"
- "doc"
- "docm"
- "docx"
- "dot"
- "dotm"
- "dotx"
- "dp"
- "dpg"
- "dra"
- "dsc"
- "dssc"
- "dtb"
- "dtd"
- "dts"
- "dtshd"
- "dump"
- "dv"
- "dvb"
- "dvi"
- "dwf"
- "dwg"
- "dxf"
- "dxp"
- "dxr"
- "ecelp4800"
- "ecelp7470"
- "ecelp9600"
- "ecma"
- "edm"
- "edx"
- "efif"
- "ei6"
- "elc"
- "emf"
- "eml"
- "emma"
- "emz"
- "eol"
- "eot"
- "eps"
- "epub"
- "es3"
- "esa"
- "esf"
- "et3"
- "etx"
- "eva"
- "evy"
- "exe"
- "exi"
- "ext"
- "ez"
- "ez2"
- "ez3"
- "f4v"
- "f77"
- "f90"
- "fbs"
- "fcdt"
- "fcs"
- "fdf"
- "fe_launch"
- "fg5"
- "fgd"
- "fh"
- "fh4"
- "fh5"
- "fh7"
- "fhc"
- "fig"
- "finishedAutoFillingOneTimeCodeInFrame:shouldSubmit:"
- "flac"
- "fli"
- "flo"
- "flv"
- "flw"
- "flx"
- "fly"
- "fm"
- "fnc"
- "for"
- "fpx"
- "frame"
- "fsc"
- "fst"
- "ftc"
- "fti"
- "fvt"
- "fxp"
- "fxpl"
- "fzs"
- "g2w"
- "g3"
- "g3w"
- "gac"
- "gam"
- "gbr"
- "gca"
- "gdl"
- "geo"
- "gex"
- "ggb"
- "ggt"
- "ghf"
- "gif"
- "gim"
- "gml"
- "gmx"
- "gnumeric"
- "gph"
- "gpx"
- "gqf"
- "gqs"
- "gram"
- "gramps"
- "gre"
- "grv"
- "grxml"
- "gsf"
- "gtar"
- "gtm"
- "gtw"
- "gv"
- "gxf"
- "gxt"
- "h261"
- "h263"
- "h264"
- "hal"
- "hbci"
- "hdf"
- "hh"
- "hlp"
- "hpgl"
- "hpid"
- "hps"
- "hqx"
- "htke"
- "htm"
- "hvd"
- "hvp"
- "hvs"
- "i2g"
- "icc"
- "ice"
- "icm"
- "ico"
- "ics"
- "id<BMLibraryBase> soft_BiomeLibrary(void)"
- "ief"
- "ifb"
- "ifm"
- "iges"
- "igl"
- "igm"
- "igs"
- "igx"
- "iif"
- "imp"
- "ims"
- "in"
- "initWithArray:"
- "initWithDomain:visited:platform:performanceEvent:"
- "initWithDomain:visited:signal:countryCode:"
- "ink"
- "inkml"
- "install"
- "instancesRespondToSelector:"
- "iota"
- "ipfix"
- "ipk"
- "irm"
- "irp"
- "iso"
- "itp"
- "ivp"
- "ivu"
- "jad"
- "jam"
- "jar"
- "java"
- "jisp"
- "jlt"
- "jnlp"
- "joda"
- "jp2"
- "jpe"
- "jpeg"
- "jpg"
- "jpgm"
- "jpgv"
- "jpm"
- "json"
- "jsonml"
- "kar"
- "karbon"
- "kfo"
- "kia"
- "kml"
- "kmz"
- "kne"
- "knp"
- "kon"
- "kpr"
- "kpt"
- "kpxx"
- "ksp"
- "ktr"
- "ktx"
- "ktz"
- "kwd"
- "kwt"
- "lasxml"
- "latex"
- "lbd"
- "lbe"
- "les"
- "lha"
- "link66"
- "list"
- "list3820"
- "listafp"
- "lnk"
- "lostxml"
- "lrf"
- "lrm"
- "ltf"
- "lvp"
- "lwp"
- "lzh"
- "m13"
- "m14"
- "m1v"
- "m21"
- "m2a"
- "m2v"
- "m3a"
- "m3u"
- "m3u8"
- "m4a"
- "m4p"
- "m4u"
- "m4v"
- "ma"
- "mac"
- "mads"
- "mag"
- "maker"
- "manifest"
- "mar"
- "mathml"
- "mb"
- "mbk"
- "mbox"
- "mc1"
- "mcd"
- "mcurl"
- "mdb"
- "mdi"
- "me"
- "mesh"
- "meta4"
- "metalink"
- "mets"
- "mfm"
- "mft"
- "mgp"
- "mgz"
- "mid"
- "midi"
- "mie"
- "mif"
- "mime"
- "mj2"
- "mjp2"
- "mk3d"
- "mka"
- "mks"
- "mkv"
- "mlp"
- "mmd"
- "mmf"
- "mmr"
- "mng"
- "mny"
- "mobi"
- "mobipocket-ebook"
- "mods"
- "mov"
- "mp2"
- "mp21"
- "mp2a"
- "mp3"
- "mp4"
- "mp4a"
- "mp4s"
- "mp4v"
- "mpc"
- "mpe"
- "mpeg"
- "mpg"
- "mpg4"
- "mpga"
- "mpkg"
- "mpm"
- "mpn"
- "mpp"
- "mpt"
- "mpy"
- "mqy"
- "mrc"
- "mrcx"
- "ms"
- "mscml"
- "mseed"
- "mseq"
- "msf"
- "msh"
- "msi"
- "msl"
- "msty"
- "mts"
- "mus"
- "musicxml"
- "mvb"
- "mwf"
- "mxf"
- "mxl"
- "mxml"
- "mxs"
- "mxu"
- "n-gage"
- "n3"
- "nb"
- "nbp"
- "nc"
- "ncx"
- "nfo"
- "ngdat"
- "nitf"
- "nlu"
- "nml"
- "nnd"
- "nns"
- "nnw"
- "npx"
- "nsc"
- "nsf"
- "ntf"
- "nzb"
- "oa2"
- "oa3"
- "oas"
- "obd"
- "obj"
- "oda"
- "odb"
- "odc"
- "odf"
- "odft"
- "odg"
- "odi"
- "odm"
- "odp"
- "ods"
- "odt"
- "oga"
- "ogg"
- "ogv"
- "ogx"
- "omdoc"
- "onepkg"
- "onetmp"
- "onetoc"
- "onetoc2"
- "opf"
- "opml"
- "oprc"
- "org"
- "osf"
- "osfpvg"
- "otc"
- "otf"
- "otg"
- "oth"
- "oti"
- "ots"
- "ott"
- "oxps"
- "oxt"
- "p10"
- "p12"
- "p7b"
- "p7c"
- "p7m"
- "p7r"
- "p7s"
- "p8"
- "pas"
- "paw"
- "pbd"
- "pbm"
- "pcap"
- "pcf"
- "pcl"
- "pclxl"
- "pct"
- "pcurl"
- "pcx"
- "pdb"
- "pdf"
- "pfa"
- "pfb"
- "pfm"
- "pfr"
- "pfx"
- "pgm"
- "pgn"
- "pgp"
- "pic"
- "pict"
- "pkg"
- "pki"
- "pkipath"
- "plb"
- "plc"
- "plf"
- "pls"
- "pml"
- "png"
- "pnm"
- "pnt"
- "pntg"
- "portpkg"
- "pot"
- "potm"
- "potx"
- "ppam"
- "ppd"
- "ppm"
- "pps"
- "ppsm"
- "ppsx"
- "ppt"
- "pptm"
- "pptx"
- "pqa"
- "prc"
- "pre"
- "prf"
- "providersMatchingQueryString:"
- "providersMatchingString:"
- "ps"
- "psb"
- "psd"
- "psf"
- "pskcxml"
- "ptid"
- "pub"
- "pvb"
- "pwn"
- "pya"
- "pyv"
- "qam"
- "qbo"
- "qfx"
- "qps"
- "qt"
- "qti"
- "qtif"
- "qwd"
- "qwt"
- "qxb"
- "qxd"
- "qxl"
- "qxt"
- "ra"
- "ram"
- "rar"
- "ras"
- "rcprofile"
- "rdf"
- "rdz"
- "removeProvidersWithHosts:"
- "rep"
- "res"
- "rgb"
- "rif"
- "rip"
- "ris"
- "rl"
- "rlc"
- "rld"
- "rm"
- "rmi"
- "rmp"
- "rms"
- "rmvb"
- "rnc"
- "roa"
- "roff"
- "rp9"
- "rpss"
- "rpst"
- "rq"
- "rs"
- "rsd"
- "rss"
- "rtf"
- "rtx"
- "s3m"
- "saf"
- "safari_URLWithUniqueFilename"
- "safari_detailStringWithTitleString:prompt:"
- "safari_favoritesTitleWithEmojiForRTL:"
- "safari_isPathExtensionAllowedForAnalytics"
- "safari_reverseEnumerateComponents:usingBlock:"
- "sbml"
- "sc"
- "scd"
- "scm"
- "scq"
- "scs"
- "scurl"
- "sda"
- "sdc"
- "sdd"
- "sdkd"
- "sdkm"
- "sdp"
- "sdw"
- "see"
- "sema"
- "semd"
- "semf"
- "ser"
- "setSearchURLTemplateFromForm:forSourcePageURLString:"
- "setpay"
- "setreg"
- "sfd-hdstx"
- "sfs"
- "sfv"
- "sgi"
- "sgl"
- "sgm"
- "sgml"
- "sh"
- "shar"
- "shf"
- "sid"
- "sig"
- "sil"
- "silo"
- "sis"
- "sisx"
- "sit"
- "sitx"
- "skd"
- "skm"
- "skp"
- "skt"
- "sldm"
- "sldx"
- "slt"
- "sm"
- "smf"
- "smi"
- "smil"
- "smv"
- "smzip"
- "snd"
- "snf"
- "so"
- "softlink:r:path:/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary"
- "spc"
- "spf"
- "spl"
- "spot"
- "spp"
- "spq"
- "spx"
- "sql"
- "src"
- "srt"
- "sru"
- "srx"
- "ssdl"
- "sse"
- "ssf"
- "ssml"
- "st"
- "stc"
- "std"
- "stf"
- "sti"
- "stk"
- "stl"
- "str"
- "stw"
- "sub"
- "sus"
- "susp"
- "sv4cpio"
- "sv4crc"
- "svc"
- "svd"
- "svg"
- "svgz"
- "swa"
- "swf"
- "swi"
- "sxc"
- "sxd"
- "sxg"
- "sxi"
- "sxm"
- "sxw"
- "t3"
- "taglet"
- "tao"
- "tar"
- "tcap"
- "tcl"
- "teacher"
- "tei"
- "teicorpus"
- "tex"
- "texi"
- "texinfo"
- "text"
- "tfi"
- "tfm"
- "tga"
- "thmx"
- "tif"
- "tiff"
- "tmo"
- "torrent"
- "tpl"
- "tpt"
- "tr"
- "tra"
- "trm"
- "ts"
- "tsd"
- "tsv"
- "ttc"
- "ttf"
- "ttl"
- "twd"
- "twds"
- "txd"
- "txf"
- "txt"
- "u32"
- "udeb"
- "ufd"
- "ufdl"
- "ulx"
- "umj"
- "unityweb"
- "uoml"
- "uri"
- "uris"
- "urls"
- "ustar"
- "utz"
- "uu"
- "uva"
- "uvd"
- "uvf"
- "uvg"
- "uvh"
- "uvi"
- "uvm"
- "uvp"
- "uvs"
- "uvt"
- "uvu"
- "uvv"
- "uvva"
- "uvvd"
- "uvvf"
- "uvvg"
- "uvvh"
- "uvvi"
- "uvvm"
- "uvvp"
- "uvvs"
- "uvvt"
- "uvvu"
- "uvvv"
- "uvvx"
- "uvvz"
- "uvx"
- "uvz"
- "vcard"
- "vcd"
- "vcf"
- "vcg"
- "vcs"
- "vcx"
- "vis"
- "viv"
- "vob"
- "void *BiomeLibraryLibrary(void)"
- "vor"
- "vox"
- "vrml"
- "vsd"
- "vsf"
- "vss"
- "vst"
- "vsw"
- "vtu"
- "vxml"
- "w3d"
- "wad"
- "wav"
- "wax"
- "wbmp"
- "wbs"
- "wbxml"
- "wcm"
- "wdb"
- "wdp"
- "weba"
- "webm"
- "webp"
- "wg"
- "wgt"
- "wks"
- "wm"
- "wma"
- "wmd"
- "wmf"
- "wml"
- "wmlc"
- "wmls"
- "wmlsc"
- "wmv"
- "wmx"
- "wmz"
- "woff"
- "wpd"
- "wpl"
- "wps"
- "wqd"
- "wri"
- "wrl"
- "wsdl"
- "wspolicy"
- "wtb"
- "wvx"
- "x32"
- "x3d"
- "x3db"
- "x3dbz"
- "x3dv"
- "x3dvz"
- "x3dz"
- "xaml"
- "xap"
- "xar"
- "xbap"
- "xbd"
- "xbm"
- "xdf"
- "xdm"
- "xdp"
- "xdssc"
- "xdw"
- "xenc"
- "xer"
- "xfdf"
- "xfdl"
- "xht"
- "xhtml"
- "xhvml"
- "xif"
- "xla"
- "xlam"
- "xlc"
- "xlf"
- "xlm"
- "xls"
- "xlsb"
- "xlsm"
- "xlsx"
- "xlt"
- "xltm"
- "xltx"
- "xlw"
- "xm"
- "xml"
- "xo"
- "xop"
- "xpi"
- "xpl"
- "xpm"
- "xpr"
- "xps"
- "xpw"
- "xpx"
- "xsl"
- "xslt"
- "xsm"
- "xspf"
- "xul"
- "xvm"
- "xvml"
- "xwd"
- "xyz"
- "xz"
- "yang"
- "yin"
- "z1"
- "z2"
- "z3"
- "z4"
- "z5"
- "z6"
- "z7"
- "z8"
- "zaz"
- "zir"
- "zirz"
- "zmm"
- "{RetainPtr<_OpaquePCSShareProtection *>=\"m_ptr\"^v}"
- "{RetainPtr<_PCSIdentitySetData *>=\"m_ptr\"^v}"
- "{RetainPtr<const __CFData *>=\"m_ptr\"^v}"
- "{RetainPtr<const __CTFontDescriptor *>=^v}28@0:8@16B24"

```
