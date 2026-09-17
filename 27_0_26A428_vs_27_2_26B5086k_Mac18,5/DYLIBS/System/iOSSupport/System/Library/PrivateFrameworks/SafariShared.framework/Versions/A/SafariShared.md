## SafariShared

> `/System/iOSSupport/System/Library/PrivateFrameworks/SafariShared.framework/Versions/A/SafariShared`

```diff

-625.1.29.11.27
-  __TEXT.__text: 0x1bb918
-  __TEXT.__objc_methlist: 0x12f6c
-  __TEXT.__const: 0x97328
-  __TEXT.__gcc_except_tab: 0x1cc50
-  __TEXT.__cstring: 0x1a887
+625.2.4.1.0
+  __TEXT.__text: 0x1be1e4
+  __TEXT.__objc_methlist: 0x12fd4
+  __TEXT.__const: 0x9fa70
+  __TEXT.__gcc_except_tab: 0x1cdb4
+  __TEXT.__cstring: 0x1abb7
   __TEXT.__ustring: 0xcb78
-  __TEXT.__oslogstring: 0x10df2
+  __TEXT.__oslogstring: 0x10f92
   __TEXT.__dlopen_cstrs: 0xe9
-  __TEXT.__swift5_typeref: 0xc36
-  __TEXT.__swift5_fieldmd: 0x75c
-  __TEXT.__constg_swiftt: 0x7ec
+  __TEXT.__swift5_typeref: 0xc50
+  __TEXT.__swift5_fieldmd: 0x77c
+  __TEXT.__constg_swiftt: 0x7cc
   __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_reflstr: 0x59c
+  __TEXT.__swift5_reflstr: 0x5fc
   __TEXT.__swift5_assocty: 0x198
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_proto: 0x218
-  __TEXT.__swift5_types: 0x98
+  __TEXT.__swift5_types: 0x94
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_capture: 0xe0
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x40
   __TEXT.__swift_as_cont: 0x88
-  __TEXT.__unwind_info: 0xd5b0
-  __TEXT.__eh_frame: 0xf68
+  __TEXT.__unwind_info: 0xd650
+  __TEXT.__eh_frame: 0xfe0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x14c50
+  __DATA_CONST.__const: 0x14ce8
   __DATA_CONST.__objc_classlist: 0xae0
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa468
+  __DATA_CONST.__objc_selrefs: 0xa4c8
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0x850
+  __DATA_CONST.__objc_superrefs: 0x858
   __DATA_CONST.__objc_arraydata: 0x9f0
-  __DATA_CONST.__got: 0x1938
-  __AUTH_CONST.__const: 0x3e70
-  __AUTH_CONST.__cfstring: 0x16de0
-  __AUTH_CONST.__objc_const: 0x224e8
+  __DATA_CONST.__got: 0x1958
+  __AUTH_CONST.__const: 0x3f90
+  __AUTH_CONST.__cfstring: 0x16f80
+  __AUTH_CONST.__objc_const: 0x225d0
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__objc_intobj: 0x5a0
+  __AUTH_CONST.__objc_intobj: 0x5b8
   __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1e88
-  __AUTH.__objc_data: 0x2eb8
+  __AUTH_CONST.__auth_got: 0x1e90
+  __AUTH.__objc_data: 0x2f10
   __AUTH.__data: 0x350
-  __DATA.__objc_ivar: 0x15bc
-  __DATA.__data: 0x3d70
+  __DATA.__objc_ivar: 0x15d0
+  __DATA.__data: 0x3db0
   __DATA.__common: 0x30
-  __DATA_DIRTY.__objc_data: 0x3e70
-  __DATA_DIRTY.__data: 0x160
+  __DATA_DIRTY.__objc_data: 0x3e08
+  __DATA_DIRTY.__data: 0x128
   __DATA_DIRTY.__bss: 0x740
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10534
-  Symbols:   20535
-  CStrings:  4821
+  Functions: 10559
+  Symbols:   20597
+  CStrings:  4849
 
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
+ -[WBSTrialSearchParameters isPersonalizedGoogleSuggestionsEnabled]
+ GCC_except_table219
+ GCC_except_table245
+ GCC_except_table248
+ GCC_except_table263
+ GCC_except_table266
+ GCC_except_table317
+ GCC_except_table318
+ GCC_except_table319
+ GCC_except_table320
+ GCC_except_table321
+ GCC_except_table322
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
+ ___unnamed_37
+ ___unnamed_60
+ _objc_msgSend$URLWithSearchTerms:previousQuery:
+ _objc_msgSend$_URLStringWithSearchTerms:previousQuery:
+ _objc_msgSend$_frequencyValueForWebSearchEntry:
+ _objc_msgSend$_getOneTimeCodeForField:atURL:snapshottedGenerator:oneTimeCodeProvider:receivedAfterDate:staleOneTimeCodeThresholdDate:completionHandler:
+ _objc_msgSend$_searchEngineStream
+ _objc_msgSend$computeSortedRecentWebSearches:completionHandler:
+ _objc_msgSend$emailProviderFraudTargets
+ _objc_msgSend$initWithSearchEngineIdentifier:
+ _objc_msgSend$isPersonalizedGoogleSuggestionsEnabled
+ _objc_msgSend$safari_isEarlierThanDate:
+ _objc_msgSend$safari_isMainBundleSafariTechnologyPreview
+ _objc_msgSend$setLastUsedDate:forIdentifier:withContact:completionHandler:
+ _objc_msgSend$setSuspectedProvenanceOfOneTimeCode:
+ _objc_msgSend$shouldShowInternalUI
+ _objc_msgSend$suspectedProvenanceOfOneTimeCode
+ _oneTimeCodeAuthenticatorAppProvenanceKeywords
+ _oneTimeCodeEmailProvenanceKeywords
+ _oneTimeCodeTextMessageProvenanceKeywords
+ _safariTechnologyPreviewApplicationBundleIdentifier
+ _swift_retain_x25
+ _swift_updateClassMetadata2
+ _symbolic Si13toolCallCount_t
+ _symbolic SiSg
+ _symbolic _____ 15TokenGeneration11CachePolicyV
+ safari_isMainBundleSafariTechnologyPreview.isMainBundleSafariTechnologyPreview
+ safari_isMainBundleSafariTechnologyPreview.onceToken
- -[WBSFormDataController _getOneTimeCodeForField:atURL:snapshottedGenerator:oneTimeCodeProvider:receivedAfterDate:completionHandler:]
- -[WBSFormDataController autoFillValuesForAutomaticPasswordChangeWithAccountInfo:formContexts:savedAccountContext:options:generatedPassword:oneTimeCodeProvider:earliestOneTimeCodeDate:completionHandler:]
- -[WBSHistory computeSortedRecentWebSearches:useExponentialWeighting:completionHandler:]
- -[WBSHistoryServiceDatabase computeSortedRecentWebSearches:useExponentialWeighting:completionHandler:]
- -[WBSHistoryServiceDatabaseProxy computeSortedRecentWebSearches:useExponentialWeighting:completionHandler:]
- -[WBSHistoryServiceStore computeSortedRecentWebSearches:useExponentialWeighting:completionHandler:]
- -[WBSHistoryServiceURLCompletion _frequencyValueForWebSearchEntry:useExponentialWeighting:]
- -[WBSHistoryServiceURLCompletion computeSortedRecentWebSearches:useExponentialWeighting:completionHandler:]
- -[WBSOpenSearchURLTemplate _URLStringWithSearchTerms:]
- -[WBSTrialSearchParameters checkServerCompletionForPrefixNavigationalIntent]
- -[WBSTrialSearchParameters enableRecentSearchSortingByVisitCountScore]
- -[WBSTrialSearchParameters enableRecentSearchSortingUsingExponentialWeighting]
- -[WBSTrialSearchParameters prefixNavigationalIntentThreshold]
- GCC_except_table206
- GCC_except_table207
- GCC_except_table209
- GCC_except_table254
- GCC_except_table258
- GCC_except_table259
- GCC_except_table269
- GCC_except_table281
- GCC_except_table285
- GCC_except_table300
- GCC_except_table312
- OBJC_IVAR_$_WBSTrialSearchParameters._enableRecentSearchSortingByVisitCountScore
- OBJC_IVAR_$_WBSTrialSearchParameters._enableRecentSearchSortingUsingExponentialWeighting
- _OBJC_CLASS_$_WBSDefaultSearchParameters
- _OBJC_METACLASS_$_WBSDefaultSearchParameters
- __CLASS_METHODS_WBSDefaultSearchParameters
- __CLASS_PROPERTIES_WBSDefaultSearchParameters
- __DATA_WBSDefaultSearchParameters
- __INSTANCE_METHODS_WBSDefaultSearchParameters
- __METACLASS_DATA_WBSDefaultSearchParameters
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
- ___99-[WBSHistoryServiceStore computeSortedRecentWebSearches:useExponentialWeighting:completionHandler:]_block_invoke
- ___block_descriptor_49_ea8_32s40bs_e45_v16?0"<WBSHistoryServiceDatabaseProtocol>"8ls40l8s32l8
- ___unnamed_35
- ___unnamed_57
- _objc_msgSend$_URLStringWithSearchTerms:
- _objc_msgSend$_frequencyValueForWebSearchEntry:useExponentialWeighting:
- _objc_msgSend$_getOneTimeCodeForField:atURL:snapshottedGenerator:oneTimeCodeProvider:receivedAfterDate:completionHandler:
- _objc_msgSend$checkServerCompletionForPrefixNavigationalIntent
- _objc_msgSend$computeSortedRecentWebSearches:useExponentialWeighting:completionHandler:
- _objc_msgSend$enableRecentSearchSortingByVisitCountScore
- _objc_msgSend$prefixNavigationalIntentThreshold
- _objc_msgSend$shouldPromoteRecentSearchesStartPageModuleBelowFavorites
- _objc_msgSend$shouldPromoteRecentSearchesStartPageModuleToTheTop
- _symbolic _____ 12SafariShared26WBSDefaultSearchParametersC
CStrings:
+ "\v"
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
+ "OneTimeCodeAuthenticatorAppProvenanceRegularExpressions"
+ "OneTimeCodeEmailProvenanceRegularExpressions"
+ "OneTimeCodeTextMessageProvenanceRegularExpressions"
+ "SuspectedMaskedEmailAddressForOneTimeCode"
+ "SuspectedProvenanceOfOneTimeCode"
+ "TextMessage"
+ "Updating Trial parameters based on hardcoded default values"
+ "WBSEnablePersonalizedGoogleSuggestions"
+ "WBSEnableRecentSearchesStartPageModuleAtTopOfStartPage"
+ "_suspectedMaskedEmailAddressForOneTimeCode"
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
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/wtf/HashTable.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/wtf/Vector.h"
- "22625.1.29.11.27"
```
