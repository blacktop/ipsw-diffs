## SafariShared

> `/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared`

```diff

-625.1.29.10.29
-  __TEXT.__text: 0x297764
-  __TEXT.__objc_methlist: 0x15fe4
-  __TEXT.__const: 0x9afa4
-  __TEXT.__gcc_except_tab: 0x1ea64
-  __TEXT.__cstring: 0x23647
+625.2.4.1.0
+  __TEXT.__text: 0x2a1d3c
+  __TEXT.__objc_methlist: 0x1617c
+  __TEXT.__const: 0xa3734
+  __TEXT.__gcc_except_tab: 0x1ebe0
+  __TEXT.__cstring: 0x23827
   __TEXT.__ustring: 0xcec0
-  __TEXT.__oslogstring: 0x158e2
+  __TEXT.__oslogstring: 0x15ce2
   __TEXT.__dlopen_cstrs: 0x2b7
-  __TEXT.__swift5_typeref: 0x3666
-  __TEXT.__swift5_fieldmd: 0x170c
-  __TEXT.__constg_swiftt: 0x2124
+  __TEXT.__swift5_typeref: 0x368a
+  __TEXT.__swift5_fieldmd: 0x1884
+  __TEXT.__constg_swiftt: 0x2144
   __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_reflstr: 0x14b8
+  __TEXT.__swift5_reflstr: 0x1638
   __TEXT.__swift5_assocty: 0x450
   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_proto: 0x400
-  __TEXT.__swift5_types: 0x198
-  __TEXT.__swift5_capture: 0xc10
+  __TEXT.__swift5_types: 0x194
+  __TEXT.__swift5_capture: 0x1010
   __TEXT.__swift_as_entry: 0x180
   __TEXT.__swift_as_ret: 0x168
   __TEXT.__swift_as_cont: 0x2ec
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x112a0
-  __TEXT.__eh_frame: 0x5438
+  __TEXT.__unwind_info: 0x11420
+  __TEXT.__eh_frame: 0x54e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x16550
+  __DATA_CONST.__const: 0x165a8
   __DATA_CONST.__objc_classlist: 0xcb8
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x2c8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc068
+  __DATA_CONST.__objc_selrefs: 0xc188
   __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x958
+  __DATA_CONST.__objc_superrefs: 0x960
   __DATA_CONST.__objc_arraydata: 0xb00
-  __DATA_CONST.__got: 0x2008
-  __AUTH_CONST.__const: 0xa7b0
-  __AUTH_CONST.__cfstring: 0x1b0a0
-  __AUTH_CONST.__objc_const: 0x285e8
+  __DATA_CONST.__got: 0x2028
+  __AUTH_CONST.__const: 0xb440
+  __AUTH_CONST.__cfstring: 0x1b0c0
+  __AUTH_CONST.__objc_const: 0x285f8
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__objc_intobj: 0x750
+  __AUTH_CONST.__objc_intobj: 0x768
   __AUTH_CONST.__objc_arrayobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_doubleobj: 0xa0
-  __AUTH_CONST.__auth_got: 0x2bd8
-  __AUTH.__objc_data: 0x7c88
-  __AUTH.__data: 0x17c0
-  __DATA.__objc_ivar: 0x1938
-  __DATA.__data: 0x5738
+  __AUTH_CONST.__auth_got: 0x2bd0
+  __AUTH.__objc_data: 0x7c78
+  __AUTH.__data: 0x17a0
+  __DATA.__objc_ivar: 0x1940
+  __DATA.__data: 0x5778
   __DATA.__common: 0xa0
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__bss: 0x9

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14561
-  Symbols:   23756
-  CStrings:  6135
+  Functions: 14807
+  Symbols:   23780
+  CStrings:  6158
 
Symbols:
+ +[NSBundle(SafariSharedExtras) safari_isMainBundleSafariTechnologyPreview]
+ -[WBSAutoFillValuesResult setSuspectedProvenanceOfOneTimeCode:]
+ -[WBSAutoFillValuesResult suspectedProvenanceOfOneTimeCode]
+ -[WBSBiomeDonationManager _searchEngineStream]
+ -[WBSBiomeDonationManager donateSearchEngineWithIdentifier:]
+ -[WBSFormControlMetadata suspectedMaskedEmailAddressForOneTimeCode]
+ -[WBSFormControlMetadata suspectedProvenanceOfOneTimeCode]
+ -[WBSFormDataController _getOneTimeCodeForField:atURL:snapshottedGenerator:oneTimeCodeProvider:receivedAfterDate:staleOneTimeCodeThresholdDate:completionHandler:]
+ -[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:staleOneTimeCodeThresholdDate:completionHandler:]
+ -[WBSFormDataController setLastUsedDate:forIdentifier:withContact:completionHandler:]
+ -[WBSHistory computeSortedRecentWebSearches:completionHandler:]
+ -[WBSHistoryServiceDatabase computeSortedRecentWebSearches:completionHandler:]
+ -[WBSHistoryServiceDatabaseProxy computeSortedRecentWebSearches:completionHandler:]
+ -[WBSHistoryServiceStore computeSortedRecentWebSearches:completionHandler:]
+ -[WBSHistoryServiceURLCompletion _frequencyValueForWebSearchEntry:]
+ -[WBSHistoryServiceURLCompletion computeSortedRecentWebSearches:completionHandler:]
+ -[WBSMutableFormControlMetadata setSuspectedMaskedEmailAddressForOneTimeCode:]
+ -[WBSMutableFormControlMetadata setSuspectedProvenanceOfOneTimeCode:]
+ -[WBSOpenSearchURLTemplate URLWithSearchTerms:previousQuery:]
+ -[WBSOpenSearchURLTemplate _URLStringWithSearchTerms:previousQuery:]
+ -[WBSRecentWebSearchesController mostRecentSearchQueryForSuggestionPersonalization]
+ -[WBSSearchSuggestionsCacheKey .cxx_destruct]
+ -[WBSSearchSuggestionsCacheKey copyWithZone:]
+ -[WBSSearchSuggestionsCacheKey hash]
+ -[WBSSearchSuggestionsCacheKey initWithQueryString:previousCommittedQuery:]
+ -[WBSSearchSuggestionsCacheKey isEqual:]
+ -[WBSTrialManager searchProviderIdentifier]
+ -[WBSTrialSearchParameters _updateWithTrial:forTrial:]
+ -[WBSTrialSearchParameters isPersonalizedGoogleSuggestionsEnabled]
+ GCC_except_table196
+ GCC_except_table197
+ GCC_except_table239
+ GCC_except_table240
+ GCC_except_table255
+ GCC_except_table297
+ GCC_except_table298
+ GCC_except_table299
+ GCC_except_table301
+ GCC_except_table312
+ GCC_except_table324
+ GCC_except_table325
+ _BMSafariSearchEngineIdentifier
+ _OBJC_CLASS_$_BMSafariSearchEngine
+ _OBJC_CLASS_$_WBSSearchSuggestionsCacheKey
+ _OBJC_IVAR_$_WBSAutoFillValuesResult._suspectedProvenanceOfOneTimeCode
+ _OBJC_IVAR_$_WBSBiomeDonationManager._searchEngineStream
+ _OBJC_IVAR_$_WBSFormControlMetadata._suspectedMaskedEmailAddressForOneTimeCode
+ _OBJC_IVAR_$_WBSFormControlMetadata._suspectedProvenanceOfOneTimeCode
+ _OBJC_IVAR_$_WBSSearchSuggestionsCacheKey._previousCommittedQuery
+ _OBJC_IVAR_$_WBSSearchSuggestionsCacheKey._queryString
+ _OBJC_IVAR_$_WBSTrialSearchParameters._isPersonalizedGoogleSuggestionsEnabled
+ _OBJC_METACLASS_$_WBSSearchSuggestionsCacheKey
+ _WBSEnablePersonalizedGoogleSuggestions
+ _WBSEnableRecentSearchesStartPageModuleAtTopOfStartPageKey
+ _WBSFormMetadataControlSuspectedMaskedEmailAddressForOneTimeCodeKey
+ _WBSFormMetadataControlSuspectedProvenanceOfOneTimeCodeKey
+ _WBSOSLogSearchFeatureAvailability
+ _WBSPrefixNavigationalIntentThreshold
+ __OBJC_$_INSTANCE_METHODS_WBSSearchSuggestionsCacheKey
+ __OBJC_$_INSTANCE_VARIABLES_WBSSearchSuggestionsCacheKey
+ __OBJC_CLASS_PROTOCOLS_$_WBSSearchSuggestionsCacheKey
+ __OBJC_CLASS_RO_$_WBSSearchSuggestionsCacheKey
+ __OBJC_METACLASS_RO_$_WBSSearchSuggestionsCacheKey
+ __ZL38oneTimeCodeEmailProvenanceKeywordsData
+ __ZL44controlIsReadOnlyAndAlreadyMatchesCredentialP22WBSFormControlMetadataP8NSStringS2_
+ __ZL44oneTimeCodeTextMessageProvenanceKeywordsData
+ __ZL49oneTimeCodeAuthenticatorAppProvenanceKeywordsData
+ __ZL53cachedRegularExpressionsForOneTimeCodeEmailProvenance
+ __ZL59cachedRegularExpressionsForOneTimeCodeTextMessageProvenance
+ __ZL64cachedRegularExpressionsForOneTimeCodeAuthenticatorAppProvenance
+ __ZN12SafariSharedL43jsOneTimeCodeEmailProvenancePatternMatchersEPK15OpaqueJSContextP13OpaqueJSValueP14OpaqueJSStringPPKS3_
+ __ZN12SafariSharedL49jsOneTimeCodeTextMessageProvenancePatternMatchersEPK15OpaqueJSContextP13OpaqueJSValueP14OpaqueJSStringPPKS3_
+ __ZN12SafariSharedL49jsRegularExpressionsForOneTimeCodeEmailProvenanceEPK15OpaqueJSContextP13OpaqueJSValueP14OpaqueJSStringPPKS3_
+ __ZN12SafariSharedL54jsOneTimeCodeAuthenticatorAppProvenancePatternMatchersEPK15OpaqueJSContextP13OpaqueJSValueP14OpaqueJSStringPPKS3_
+ __ZN12SafariSharedL55jsRegularExpressionsForOneTimeCodeTextMessageProvenanceEPK15OpaqueJSContextP13OpaqueJSValueP14OpaqueJSStringPPKS3_
+ __ZN12SafariSharedL60jsRegularExpressionsForOneTimeCodeAuthenticatorAppProvenanceEPK15OpaqueJSContextP13OpaqueJSValueP14OpaqueJSStringPPKS3_
+ ___162-[WBSFormDataController _getOneTimeCodeForField:atURL:snapshottedGenerator:oneTimeCodeProvider:receivedAfterDate:staleOneTimeCodeThresholdDate:completionHandler:]_block_invoke
+ ___232-[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:staleOneTimeCodeThresholdDate:completionHandler:]_block_invoke
+ ___232-[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:staleOneTimeCodeThresholdDate:completionHandler:]_block_invoke_2
+ ___232-[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:staleOneTimeCodeThresholdDate:completionHandler:]_block_invoke_3
+ ___232-[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:staleOneTimeCodeThresholdDate:completionHandler:]_block_invoke_4
+ ___232-[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:staleOneTimeCodeThresholdDate:completionHandler:]_block_invoke_5
+ ___232-[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:staleOneTimeCodeThresholdDate:completionHandler:]_block_invoke_6
+ ___232-[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:staleOneTimeCodeThresholdDate:completionHandler:]_block_invoke_7
+ ___232-[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:staleOneTimeCodeThresholdDate:completionHandler:]_block_invoke_8
+ ___60-[WBSBiomeDonationManager donateSearchEngineWithIdentifier:]_block_invoke
+ ___60-[WBSBiomeDonationManager donateSearchEngineWithIdentifier:]_block_invoke_2
+ ___74+[NSBundle(SafariSharedExtras) safari_isMainBundleSafariTechnologyPreview]_block_invoke
+ ___75-[WBSHistoryServiceStore computeSortedRecentWebSearches:completionHandler:]_block_invoke
+ ___83-[WBSHistoryServiceURLCompletion computeSortedRecentWebSearches:completionHandler:]_block_invoke
+ ___85-[WBSFormDataController setLastUsedDate:forIdentifier:withContact:completionHandler:]_block_invoke
+ ___85-[WBSFormDataController setLastUsedDate:forIdentifier:withContact:completionHandler:]_block_invoke_2
+ ___block_descriptor_32_e26_B24?0"BMStoreEvent"8^B16l
+ ___block_descriptor_56_ea8_32s40s48bs_e31_v16?0"SFAutoFillOneTimeCode"8ls32l8s40l8s48l8
+ ___unnamed_41
+ ___unnamed_64
+ _objc_msgSend$URLWithSearchTerms:previousQuery:
+ _objc_msgSend$_URLStringWithSearchTerms:previousQuery:
+ _objc_msgSend$_frequencyValueForWebSearchEntry:
+ _objc_msgSend$_getOneTimeCodeForField:atURL:snapshottedGenerator:oneTimeCodeProvider:receivedAfterDate:staleOneTimeCodeThresholdDate:completionHandler:
+ _objc_msgSend$_searchEngineStream
+ _objc_msgSend$_updateWithTrial:forTrial:
+ _objc_msgSend$computeSortedRecentWebSearches:completionHandler:
+ _objc_msgSend$donateAutoFillWithCategory:fieldCount:
+ _objc_msgSend$emailProviderFraudTargets
+ _objc_msgSend$initWithSearchEngineIdentifier:
+ _objc_msgSend$isPersonalizedGoogleSuggestionsEnabled
+ _objc_msgSend$safari_isEarlierThanDate:
+ _objc_msgSend$safari_isMainBundleSafariTechnologyPreview
+ _objc_msgSend$searchProviderIdentifier
+ _objc_msgSend$setLastUsedDate:forIdentifier:withContact:completionHandler:
+ _objc_msgSend$setSuspectedProvenanceOfOneTimeCode:
+ _objc_msgSend$suspectedProvenanceOfOneTimeCode
+ _oneTimeCodeAuthenticatorAppProvenanceKeywords
+ _oneTimeCodeEmailProvenanceKeywords
+ _oneTimeCodeTextMessageProvenanceKeywords
+ _safariTechnologyPreviewApplicationBundleIdentifier
+ _safari_isMainBundleSafariTechnologyPreview.isMainBundleSafariTechnologyPreview
+ _safari_isMainBundleSafariTechnologyPreview.onceToken
+ _symbolic Si13toolCallCount_t
+ _symbolic _____ 12SafariShared24WBSUsageRetentionFeatureO
+ _symbolic _____ 12SafariShared24WBSUsageRetentionTriggerO
+ _symbolic _____ 15TokenGeneration11CachePolicyV
+ _symbolic _____Sg_ABt 12SafariShared17WBSBookmarksTopicV
- +[WBSTrialSearchParameters codePathUUIDForHideIgnoredSiriSuggestedWebsites]
- -[NSExtension(SafariSharedExtras) safari_isUnsignedExtension]
- -[WBSFormDataController _getOneTimeCodeForField:atURL:snapshottedGenerator:oneTimeCodeProvider:receivedAfterDate:completionHandler:]
- -[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:completionHandler:]
- -[WBSHistory computeSortedRecentWebSearches:useExponentialWeighting:completionHandler:]
- -[WBSHistoryServiceDatabase computeSortedRecentWebSearches:useExponentialWeighting:completionHandler:]
- -[WBSHistoryServiceDatabaseProxy computeSortedRecentWebSearches:useExponentialWeighting:completionHandler:]
- -[WBSHistoryServiceStore computeSortedRecentWebSearches:useExponentialWeighting:completionHandler:]
- -[WBSHistoryServiceURLCompletion _frequencyValueForWebSearchEntry:useExponentialWeighting:]
- -[WBSHistoryServiceURLCompletion computeSortedRecentWebSearches:useExponentialWeighting:completionHandler:]
- -[WBSOpenSearchURLTemplate _URLStringWithSearchTerms:]
- -[WBSParsecDFeedbackDispatcher didHideRepeatedlyIgnoredSiriSuggestedSiteWithFeedbackEvent:]
- -[WBSTrialManager isAllowFavoritesInFrequentlyVisitedEnabled]
- -[WBSTrialManager isAllowLogOnURLsInFrequentlyVisitedEnabled]
- -[WBSTrialManager isDropOutliersInFrequentlyVisitedEnabled]
- -[WBSTrialManager performDelayedLaunchOperations]
- -[WBSTrialSearchParameters checkServerCompletionForPrefixNavigationalIntent]
- -[WBSTrialSearchParameters codepathIDs]
- -[WBSTrialSearchParameters enableRecentSearchSortingByVisitCountScore]
- -[WBSTrialSearchParameters enableRecentSearchSortingUsingExponentialWeighting]
- -[WBSTrialSearchParameters prefixNavigationalIntentThreshold]
- -[WBSTrialSearchParameters shouldEmitTriggerLoggingForHidingIgnoredSiriSuggestedWebsite]
- -[WBSTrialSearchParameters shouldHideIgnoredSiriSuggestedSites]
- -[WBSTrialSearchParameters thresholdForHidingIgnoredSiriSuggestedSites]
- -[WBSTrialSearchParameters updateWithTrial:forTrial:]
- GCC_except_table188
- GCC_except_table199
- GCC_except_table207
- GCC_except_table225
- GCC_except_table246
- GCC_except_table259
- GCC_except_table262
- GCC_except_table277
- GCC_except_table280
- GCC_except_table287
- GCC_except_table291
- GCC_except_table294
- GCC_except_table296
- GCC_except_table304
- GCC_except_table305
- GCC_except_table306
- GCC_except_table307
- GCC_except_table308
- GCC_except_table315
- GCC_except_table318
- _OBJC_CLASS_$_WBSDefaultSearchParameters
- _OBJC_IVAR_$_WBSTrialSearchParameters._codepathIDs
- _OBJC_IVAR_$_WBSTrialSearchParameters._enableRecentSearchSortingByVisitCountScore
- _OBJC_IVAR_$_WBSTrialSearchParameters._enableRecentSearchSortingUsingExponentialWeighting
- _OBJC_IVAR_$_WBSTrialSearchParameters._shouldHideIgnoredSiriSuggestedSites
- _OBJC_IVAR_$_WBSTrialSearchParameters._thresholdForHidingIgnoredSiriSuggestedSites
- _OBJC_METACLASS_$_WBSDefaultSearchParameters
- _TRIAL_codepathIDs
- _TRIAL_enableLabelPreviousSearchesInCompletionList
- _TRIAL_enableRecentSearchSortingByVisitCountScore
- _TRIAL_enableRecentSearchSortingUsingExponentialWeighting
- _TRIAL_enableStreamlinedCompletionList
- _TRIAL_shouldHideIgnoredSiriSuggestedSites
- _TRIAL_thresholdForHidingIgnoredSiriSuggestedSites
- __CLASS_METHODS_WBSDefaultSearchParameters
- __CLASS_PROPERTIES_WBSDefaultSearchParameters
- __DATA_WBSDefaultSearchParameters
- __INSTANCE_METHODS_WBSDefaultSearchParameters
- __METACLASS_DATA_WBSDefaultSearchParameters
- __ZZ75+[WBSTrialSearchParameters codePathUUIDForHideIgnoredSiriSuggestedWebsites]E12codePathUUID
- __ZZ75+[WBSTrialSearchParameters codePathUUIDForHideIgnoredSiriSuggestedWebsites]E9onceToken
- ___107-[WBSHistoryServiceURLCompletion computeSortedRecentWebSearches:useExponentialWeighting:completionHandler:]_block_invoke
- ___132-[WBSFormDataController _getOneTimeCodeForField:atURL:snapshottedGenerator:oneTimeCodeProvider:receivedAfterDate:completionHandler:]_block_invoke
- ___202-[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:completionHandler:]_block_invoke
- ___202-[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:completionHandler:]_block_invoke_2
- ___202-[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:completionHandler:]_block_invoke_3
- ___202-[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:completionHandler:]_block_invoke_4
- ___202-[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:completionHandler:]_block_invoke_5
- ___202-[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:completionHandler:]_block_invoke_6
- ___202-[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:completionHandler:]_block_invoke_7
- ___202-[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:completionHandler:]_block_invoke_8
- ___67-[WBSFormDataController setLastUsedDate:forIdentifier:withContact:]_block_invoke_2
- ___75+[WBSTrialSearchParameters codePathUUIDForHideIgnoredSiriSuggestedWebsites]_block_invoke
- ___99-[WBSHistoryServiceStore computeSortedRecentWebSearches:useExponentialWeighting:completionHandler:]_block_invoke
- ___block_descriptor_49_ea8_32s40bs_e45_v16?0"<WBSHistoryServiceDatabaseProtocol>"8ls40l8s32l8
- ___unnamed_39
- ___unnamed_61
- _codePathUUIDStringForHideIgnoredSiriSuggestedWebsites
- _objc_msgSend$_URLStringWithSearchTerms:
- _objc_msgSend$_frequencyValueForWebSearchEntry:useExponentialWeighting:
- _objc_msgSend$_getOneTimeCodeForField:atURL:snapshottedGenerator:oneTimeCodeProvider:receivedAfterDate:completionHandler:
- _objc_msgSend$checkServerCompletionForPrefixNavigationalIntent
- _objc_msgSend$computeSortedRecentWebSearches:useExponentialWeighting:completionHandler:
- _objc_msgSend$decodeObjectForKey:
- _objc_msgSend$enableRecentSearchSortingByVisitCountScore
- _objc_msgSend$isAllowFavoritesInFrequentlyVisitedEnabled
- _objc_msgSend$isAllowLogOnURLsInFrequentlyVisitedEnabled
- _objc_msgSend$isDropOutliersInFrequentlyVisitedEnabled
- _objc_msgSend$prefixNavigationalIntentThreshold
- _objc_msgSend$safari_isUnpackedExtension
- _objc_msgSend$safari_launchServicesDeveloperIdentifier
- _objc_msgSend$shouldPromoteRecentSearchesStartPageModuleBelowFavorites
- _objc_msgSend$shouldPromoteRecentSearchesStartPageModuleToTheTop
- _objc_msgSend$updateWithTrial:forTrial:
- _symbolic _____ 12SafariShared26WBSDefaultSearchParametersC
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/wtf/HashTable.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/wtf/Vector.h"
+ "8625.2.4.1"
+ "Agent (%{public}s) exceeded %ld tool calls; treating as a reasoning failure."
+ "Agent (%{public}s) exceeded the model's context window: %{private}s"
+ "Agent (%{public}s) exceeded the model's context window: %{public}@"
+ "AuthenticatorApp"
+ "E"
+ "Existing one-time code (source: %d) was received %.1f seconds before the last click; waiting longer for a new code"
+ "F"
+ "Factor \"%@\" has a default value of %@"
+ "Factor \"%@\" has value of %@ from the experiment"
+ "Not in an experiment, so we are skipping the step to update Trial factors"
+ "OneTimeCodeAuthenticatorAppProvenanceRegularExpressions"
+ "OneTimeCodeEmailProvenanceRegularExpressions"
+ "OneTimeCodeTextMessageProvenanceRegularExpressions"
+ "Pending feature usage donation: %{public}s/%{public}s%{public}s x%{public}ld"
+ "Pending prune of donated feature events since %{public}s."
+ "Pending settings snapshot donation: nonDefaultProfile=%{bool,public}d iCloudTabs=%{bool,public}d sync=%{bool,public}d extensions=%{bool,public}d"
+ "Skipping %ld of %ld topic writes that wouldn't change anything"
+ "SuspectedMaskedEmailAddressForOneTimeCode"
+ "SuspectedProvenanceOfOneTimeCode"
+ "TextMessage"
+ "Updating Trial parameters based on hardcoded default values"
+ "Updating Trial parameters based on information from the experiment"
+ "WBSEnablePersonalizedGoogleSuggestions"
+ "WBSEnableRecentSearchesStartPageModuleAtTopOfStartPage"
+ "_suspectedMaskedEmailAddressForOneTimeCode"
+ "com.apple.Safari.UsageRetentionFeatureDonation"
+ "distractionControl"
+ "enablePersonalizedGoogleSuggestions"
+ "isPersonalizedGoogleSuggestionsEnabled"
+ "max context length"
+ "maximum allowed is"
+ "oneTimeCodeAuthenticatorAppProvenancePatternMatchers"
+ "oneTimeCodeEmailProvenancePatternMatchers"
+ "oneTimeCodeTextMessageProvenancePatternMatchers"
+ "previousQuery"
+ "regularExpressionsForOneTimeCodeAuthenticatorAppProvenance"
+ "regularExpressionsForOneTimeCodeEmailProvenance"
+ "regularExpressionsForOneTimeCodeTextMessageProvenance"
- "\f"
- "!\xd1"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/wtf/HashTable.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/wtf/Vector.h"
- "0000000000"
- "81C7C46C-0C4F-40C3-9527-EC71B259C813"
- "8625.1.29.10.29"
- "codepathIDs"
- "enableAllowFavoritesInFrequentlyVisited"
- "enableAllowLogOnURLSInFrequentlyVisited"
- "enableDropOutliersInFrequentlyVisited"
- "enableLabelPreviousSearchesInCompletionList"
- "enableRecentSearchSortingByVisitCountScore"
- "enableRecentSearchSortingUsingExponentialWeighting"
- "enableStreamlinedCompletionList"
- "external"
- "shouldHideIgnoredSiriSuggestedSites"
- "thresholdForHidingIgnoredSiriSuggestedSites"
```
