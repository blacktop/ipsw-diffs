## SafariShared

> `/System/Library/PrivateFrameworks/SafariShared.framework/Versions/A/SafariShared`

```diff

-625.1.29.11.27
-  __TEXT.__text: 0x2d1768
-  __TEXT.__objc_methlist: 0x170fc
-  __TEXT.__const: 0x9aff4
-  __TEXT.__gcc_except_tab: 0x20704
-  __TEXT.__cstring: 0x24f17
+625.2.4.1.0
+  __TEXT.__text: 0x2db72c
+  __TEXT.__objc_methlist: 0x1728c
+  __TEXT.__const: 0xa37a4
+  __TEXT.__gcc_except_tab: 0x20884
+  __TEXT.__cstring: 0x250f7
   __TEXT.__ustring: 0xcec0
-  __TEXT.__oslogstring: 0x16a62
+  __TEXT.__oslogstring: 0x16e12
   __TEXT.__dlopen_cstrs: 0x394
-  __TEXT.__swift5_typeref: 0x33a4
-  __TEXT.__swift5_fieldmd: 0x1738
-  __TEXT.__constg_swiftt: 0x21a8
+  __TEXT.__swift5_typeref: 0x33b8
+  __TEXT.__swift5_fieldmd: 0x18b0
+  __TEXT.__constg_swiftt: 0x21c8
   __TEXT.__swift5_builtin: 0x17c
-  __TEXT.__swift5_reflstr: 0x14c8
+  __TEXT.__swift5_reflstr: 0x1648
   __TEXT.__swift5_assocty: 0x4b0
   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_proto: 0x448
-  __TEXT.__swift5_types: 0x1a8
-  __TEXT.__swift5_capture: 0xc1c
+  __TEXT.__swift5_types: 0x1a4
+  __TEXT.__swift5_capture: 0x101c
   __TEXT.__swift_as_entry: 0x180
   __TEXT.__swift_as_ret: 0x168
   __TEXT.__swift_as_cont: 0x2ec
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x12160
-  __TEXT.__eh_frame: 0x5518
+  __TEXT.__unwind_info: 0x122c8
+  __TEXT.__eh_frame: 0x5590
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xef30
+  __DATA_CONST.__const: 0xef88
   __DATA_CONST.__objc_classlist: 0xd88
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x2e8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc838
+  __DATA_CONST.__objc_selrefs: 0xc958
   __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x9c8
+  __DATA_CONST.__objc_superrefs: 0x9d0
   __DATA_CONST.__objc_arraydata: 0xb70
-  __DATA_CONST.__got: 0x20c0
-  __AUTH_CONST.__const: 0x13370
-  __AUTH_CONST.__cfstring: 0x1bda0
-  __AUTH_CONST.__objc_const: 0x2a280
+  __DATA_CONST.__got: 0x20e0
+  __AUTH_CONST.__const: 0x14000
+  __AUTH_CONST.__cfstring: 0x1bdc0
+  __AUTH_CONST.__objc_const: 0x2a290
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__objc_intobj: 0x7c8
+  __AUTH_CONST.__objc_intobj: 0x7e0
   __AUTH_CONST.__objc_arrayobj: 0x3a8
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x2a68
-  __AUTH.__objc_data: 0x3ef0
+  __AUTH_CONST.__auth_got: 0x2a60
+  __AUTH.__objc_data: 0x3f48
   __AUTH.__data: 0xf40
-  __DATA.__objc_ivar: 0x1a30
-  __DATA.__data: 0x5548
+  __DATA.__objc_ivar: 0x1a38
+  __DATA.__data: 0x5598
   __DATA.__common: 0x70
-  __DATA_DIRTY.__objc_data: 0x4938
-  __DATA_DIRTY.__data: 0xb58
+  __DATA_DIRTY.__objc_data: 0x48d0
+  __DATA_DIRTY.__data: 0xb20
   __DATA_DIRTY.__bss: 0xaf0
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15325
-  Symbols:   25223
-  CStrings:  6369
+  Functions: 15568
+  Symbols:   25259
+  CStrings:  6392
 
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
+ GCC_except_table240
+ GCC_except_table241
+ GCC_except_table268
+ GCC_except_table276
+ GCC_except_table279
+ GCC_except_table282
+ GCC_except_table296
+ GCC_except_table300
+ GCC_except_table303
+ GCC_except_table319
+ GCC_except_table334
+ GCC_except_table337
+ GCC_except_table360
+ GCC_except_table362
+ GCC_except_table364
+ GCC_except_table365
+ OBJC_IVAR_$_WBSAutoFillValuesResult._suspectedProvenanceOfOneTimeCode
+ OBJC_IVAR_$_WBSBiomeDonationManager._searchEngineStream
+ OBJC_IVAR_$_WBSFormControlMetadata._suspectedMaskedEmailAddressForOneTimeCode
+ OBJC_IVAR_$_WBSFormControlMetadata._suspectedProvenanceOfOneTimeCode
+ OBJC_IVAR_$_WBSSearchSuggestionsCacheKey._previousCommittedQuery
+ OBJC_IVAR_$_WBSSearchSuggestionsCacheKey._queryString
+ OBJC_IVAR_$_WBSTrialSearchParameters._isPersonalizedGoogleSuggestionsEnabled
+ _BMSafariSearchEngineIdentifier
+ _OBJC_CLASS_$_BMSafariSearchEngine
+ _OBJC_CLASS_$_WBSSearchSuggestionsCacheKey
+ _OBJC_METACLASS_$_WBSSearchSuggestionsCacheKey
+ _WBSEnablePersonalizedGoogleSuggestions
+ _WBSEnableRecentSearchesStartPageModuleAtTopOfStartPageKey
+ _WBSFormMetadataControlSuspectedMaskedEmailAddressForOneTimeCodeKey
+ _WBSFormMetadataControlSuspectedProvenanceOfOneTimeCodeKey
+ _WBSOSLogSearchFeatureAvailability
+ _WBSPrefixNavigationalIntentThreshold
+ __162-[WBSFormDataController _getOneTimeCodeForField:atURL:snapshottedGenerator:oneTimeCodeProvider:receivedAfterDate:staleOneTimeCodeThresholdDate:completionHandler:]_block_invoke
+ __232-[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:staleOneTimeCodeThresholdDate:completionHandler:]_block_invoke
+ __232-[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:staleOneTimeCodeThresholdDate:completionHandler:]_block_invoke_2
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
+ ___60-[WBSBiomeDonationManager donateSearchEngineWithIdentifier:]_block_invoke
+ ___60-[WBSBiomeDonationManager donateSearchEngineWithIdentifier:]_block_invoke_2
+ ___74+[NSBundle(SafariSharedExtras) safari_isMainBundleSafariTechnologyPreview]_block_invoke
+ ___75-[WBSHistoryServiceStore computeSortedRecentWebSearches:completionHandler:]_block_invoke
+ ___83-[WBSHistoryServiceURLCompletion computeSortedRecentWebSearches:completionHandler:]_block_invoke
+ ___85-[WBSFormDataController setLastUsedDate:forIdentifier:withContact:completionHandler:]_block_invoke
+ ___85-[WBSFormDataController setLastUsedDate:forIdentifier:withContact:completionHandler:]_block_invoke_2
+ ___block_descriptor_32_e26_B24?0"BMStoreEvent"8^B16l
+ ___block_descriptor_56_ea8_32s40s48bs_e31_v16?0"SFAutoFillOneTimeCode"8l
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
+ _symbolic Si13toolCallCount_t
+ _symbolic _____ 12SafariShared24WBSUsageRetentionFeatureO
+ _symbolic _____ 12SafariShared24WBSUsageRetentionTriggerO
+ _symbolic _____ 15TokenGeneration11CachePolicyV
+ safari_isMainBundleSafariTechnologyPreview.isMainBundleSafariTechnologyPreview
+ safari_isMainBundleSafariTechnologyPreview.onceToken
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
- GCC_except_table175
- GCC_except_table233
- GCC_except_table253
- GCC_except_table288
- GCC_except_table292
- GCC_except_table293
- GCC_except_table294
- GCC_except_table312
- GCC_except_table331
- GCC_except_table344
- GCC_except_table352
- GCC_except_table355
- OBJC_IVAR_$_WBSTrialSearchParameters._codepathIDs
- OBJC_IVAR_$_WBSTrialSearchParameters._enableRecentSearchSortingByVisitCountScore
- OBJC_IVAR_$_WBSTrialSearchParameters._enableRecentSearchSortingUsingExponentialWeighting
- OBJC_IVAR_$_WBSTrialSearchParameters._shouldHideIgnoredSiriSuggestedSites
- OBJC_IVAR_$_WBSTrialSearchParameters._thresholdForHidingIgnoredSiriSuggestedSites
- _OBJC_CLASS_$_WBSDefaultSearchParameters
- _OBJC_METACLASS_$_WBSDefaultSearchParameters
- _TRIAL_codepathIDs
- _TRIAL_enableLabelPreviousSearchesInCompletionList
- _TRIAL_enableRecentSearchSortingByVisitCountScore
- _TRIAL_enableRecentSearchSortingUsingExponentialWeighting
- _TRIAL_enableStreamlinedCompletionList
- _TRIAL_shouldHideIgnoredSiriSuggestedSites
- _TRIAL_thresholdForHidingIgnoredSiriSuggestedSites
- __202-[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:completionHandler:]_block_invoke
- __202-[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:completionHandler:]_block_invoke_2
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
- ___67-[WBSFormDataController setLastUsedDate:forIdentifier:withContact:]_block_invoke_2
- ___75+[WBSTrialSearchParameters codePathUUIDForHideIgnoredSiriSuggestedWebsites]_block_invoke
- ___99-[WBSHistoryServiceStore computeSortedRecentWebSearches:useExponentialWeighting:completionHandler:]_block_invoke
- ___block_descriptor_49_ea8_32s40bs_e45_v16?0"<WBSHistoryServiceDatabaseProtocol>"8l
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
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/wtf/HashTable.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/wtf/Vector.h"
+ "22625.2.4.1"
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
- "!\xc1"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/wtf/HashTable.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/wtf/Vector.h"
- "0000000000"
- "22625.1.29.11.27"
- "81C7C46C-0C4F-40C3-9527-EC71B259C813"
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
