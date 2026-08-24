## SafariShared

> `/System/Library/PrivateFrameworks/SafariShared.framework/Versions/A/SafariShared`

```diff

-625.1.24.11.2
-  __TEXT.__text: 0x2e10ac
-  __TEXT.__objc_methlist: 0x1708c
-  __TEXT.__const: 0x9a884
-  __TEXT.__gcc_except_tab: 0x206b8
-  __TEXT.__cstring: 0x24e97
+625.1.29.11.25
+  __TEXT.__text: 0x2e3d2c
+  __TEXT.__objc_methlist: 0x170fc
+  __TEXT.__const: 0x9aff4
+  __TEXT.__gcc_except_tab: 0x20720
+  __TEXT.__cstring: 0x24f07
   __TEXT.__ustring: 0xcec0
-  __TEXT.__oslogstring: 0x16782
+  __TEXT.__oslogstring: 0x16a62
   __TEXT.__dlopen_cstrs: 0x394
-  __TEXT.__swift5_typeref: 0x338e
-  __TEXT.__swift5_fieldmd: 0x172c
-  __TEXT.__constg_swiftt: 0x2188
+  __TEXT.__swift5_typeref: 0x33a4
+  __TEXT.__swift5_fieldmd: 0x1738
+  __TEXT.__constg_swiftt: 0x21a8
   __TEXT.__swift5_builtin: 0x17c
-  __TEXT.__swift5_reflstr: 0x14b8
+  __TEXT.__swift5_reflstr: 0x14c8
   __TEXT.__swift5_assocty: 0x4b0
   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_proto: 0x448
   __TEXT.__swift5_types: 0x1a8
-  __TEXT.__swift5_capture: 0xc3c
+  __TEXT.__swift5_capture: 0xc1c
   __TEXT.__swift_as_entry: 0x180
   __TEXT.__swift_as_ret: 0x168
   __TEXT.__swift_as_cont: 0x2ec
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0xf930
-  __TEXT.__eh_frame: 0x5480
+  __TEXT.__unwind_info: 0xf968
+  __TEXT.__eh_frame: 0x5508
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xef48
+  __DATA_CONST.__const: 0xef30
   __DATA_CONST.__objc_classlist: 0xd88
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x2e8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc830
+  __DATA_CONST.__objc_selrefs: 0xc838
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x9c8
   __DATA_CONST.__objc_arraydata: 0xb70
-  __DATA_CONST.__got: 0x20b8
-  __AUTH_CONST.__const: 0x13420
+  __DATA_CONST.__got: 0x20c0
+  __AUTH_CONST.__const: 0x13370
   __AUTH_CONST.__cfstring: 0x1bd80
-  __AUTH_CONST.__objc_const: 0x2a120
+  __AUTH_CONST.__objc_const: 0x2a280
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x7c8
   __AUTH_CONST.__objc_arrayobj: 0x3a8
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x2a58
+  __AUTH_CONST.__auth_got: 0x2a68
   __AUTH.__objc_data: 0x3ef0
   __AUTH.__data: 0xf40
-  __DATA.__objc_ivar: 0x1a14
-  __DATA.__data: 0x5528
+  __DATA.__objc_ivar: 0x1a30
+  __DATA.__data: 0x5548
   __DATA.__bss: 0x78f0
   __DATA.__common: 0x70
   __DATA_DIRTY.__objc_data: 0x4938
-  __DATA_DIRTY.__data: 0xb48
+  __DATA_DIRTY.__data: 0xb58
   __DATA_DIRTY.__bss: 0xaf0
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15315
-  Symbols:   25201
-  CStrings:  6357
+  Functions: 15326
+  Symbols:   25225
+  CStrings:  6368
 
Symbols:
+ +[WBSPasswordBreachNotificationManager _passwordManagerURLForSavedAccount:containsHighPriorityAccount:]
+ +[WBSPasswordBreachNotificationManager highLevelDomain:isIncludedInTopFraudTargets:]
+ -[WBSAutoFillValuesResult oneTimeCodeAppearsToHaveBeenFilledInItsEntirety]
+ -[WBSAutoFillValuesResult setOneTimeCodeAppearsToHaveBeenFilledInItsEntirety:]
+ -[WBSBrowserTabCompletionProvider _compareTabMatch:otherTabMatch:usingSelectedTabInfo:]
+ -[WBSBrowserTabCompletionProvider _distanceFromSelectedTabForTabMatch:usingSelectedTabInfo:]
+ -[WBSClusteringCalibration _calibrationDataForLanguage:]
+ -[WBSClusteringCalibration _processCalibrationData:referenceLanguage:]
+ -[WBSClusteringCalibration _registerForOverrideObservation]
+ -[WBSClusteringCalibration _resolveModelVersionForLanguage:]
+ -[WBSClusteringCalibration _version:excludesLanguage:]
+ -[WBSClusteringCalibration defaultMaximumDistanceForLanguage:]
+ -[WBSClusteringCalibration modelVersionForLanguage:]
+ -[WBSDevice(ScreenTime) getIsScreenTimeBlockingURL:completionHandler:]
+ -[WBSEmbeddingStore embedFeatureText:forURL:inProfileIdentifier:language:lastVisitTime:completionHandler:]
+ -[WBSFormMetadata typeConfidence]
+ -[WBSPageContext isCJK]
+ -[WBSSiriIntelligenceDonor _coreSpotlightItemsSubarrays:batchSize:]
+ -[WBSTrialSearchParameters shouldPromoteRecentSearchesStartPageModuleBelowFavorites]
+ GCC_except_table238
+ GCC_except_table239
+ GCC_except_table264
+ GCC_except_table273
+ GCC_except_table279
+ GCC_except_table298
+ GCC_except_table314
+ GCC_except_table334
+ GCC_except_table348
+ GCC_except_table359
+ GCC_except_table360
+ OBJC_IVAR_$_WBSAutoFillValuesResult._oneTimeCodeAppearsToHaveBeenFilledInItsEntirety
+ OBJC_IVAR_$_WBSClusteringCalibration._defaultMaximumDistance
+ OBJC_IVAR_$_WBSClusteringCalibration._overrideObservation
+ OBJC_IVAR_$_WBSClusteringCalibration._referenceLanguage
+ OBJC_IVAR_$_WBSClusteringCalibration._resolvedVersionCache
+ OBJC_IVAR_$_WBSDownloadFileBOMUnarchiver._didCancel
+ OBJC_IVAR_$_WBSFormMetadata._typeConfidence
+ OBJC_IVAR_$_WBSTrialSearchParameters._shouldPromoteRecentSearchesStartPageModuleBelowFavorites
+ _TRIAL_shouldPromoteRecentSearchesStartPageModuleBelowFavorites
+ _WBSDownloadFileUnarchiverErrorDomain
+ _WBSEverLaunchedOnPreRaveOSVersionPreferenceKey
+ _WBSFormMetadataAutoFillFormTypeConfidenceKey
+ _WBSOSLogScreenTime
+ _WBSParsecDomainSafariDouyinCompletion
+ _WBSParsecDomainSafariDouyinSearch
+ _WBSPasswordManagerURLContainsHighPriorityAccountKey
+ _WBSPasswordManagerURLIsForBreachNotificationKey
+ _WBSStartPageSectionTrialRecentSearches
+ _WBSTabClusteringPolicyKey
+ __70-[WBSDevice(ScreenTime) getIsScreenTimeBlockingURL:completionHandler:]_block_invoke
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_WBSDevice_$_ScreenTime
+ __OBJC_$_CATEGORY_WBSDevice_$_ScreenTime
+ ___106-[WBSEmbeddingStore embedFeatureText:forURL:inProfileIdentifier:language:lastVisitTime:completionHandler:]_block_invoke
+ ___106-[WBSEmbeddingStore embedFeatureText:forURL:inProfileIdentifier:language:lastVisitTime:completionHandler:]_block_invoke_2
+ ___106-[WBSEmbeddingStore embedFeatureText:forURL:inProfileIdentifier:language:lastVisitTime:completionHandler:]_block_invoke_3
+ ___106-[WBSEmbeddingStore embedFeatureText:forURL:inProfileIdentifier:language:lastVisitTime:completionHandler:]_block_invoke_4
+ ___59-[WBSClusteringCalibration _registerForOverrideObservation]_block_invoke
+ ___70-[WBSDevice(ScreenTime) getIsScreenTimeBlockingURL:completionHandler:]_block_invoke
+ ___82-[WBSPasswordBreachNotificationManager _contentWithSavedAccounts:topFraudTargets:]_block_invoke
+ ___block_descriptor_40_e8_32s_e25_B16?0"WBSSavedAccount"8l
+ ___block_descriptor_48_ea8_32s40s_e71_q24?0"WBSBrowserTabCompletionMatch"8"WBSBrowserTabCompletionMatch"16l
+ ___block_descriptor_88_ea8_32s40s48s56s64s72bs_e17_v16?0"NSArray"8l
+ ___block_descriptor_88_ea8_32s40s48s56s64s72bs_e22_v16?0"WBSEmbedding"8l
+ __swift_closure_destructor.178Tm
+ _isCJKLanguage
+ _objc_msgSend$_calibrationDataForLanguage:
+ _objc_msgSend$_compareTabMatch:otherTabMatch:usingSelectedTabInfo:
+ _objc_msgSend$_coreSpotlightItemsSubarrays:batchSize:
+ _objc_msgSend$_distanceFromSelectedTabForTabMatch:usingSelectedTabInfo:
+ _objc_msgSend$_passwordManagerURLForSavedAccount:containsHighPriorityAccount:
+ _objc_msgSend$_processCalibrationData:referenceLanguage:
+ _objc_msgSend$_registerForOverrideObservation
+ _objc_msgSend$_resolveModelVersionForLanguage:
+ _objc_msgSend$_version:excludesLanguage:
+ _objc_msgSend$defaultMaximumDistanceForLanguage:
+ _objc_msgSend$embedFeatureText:forURL:inProfileIdentifier:language:lastVisitTime:completionHandler:
+ _objc_msgSend$embedWithItem:language:completion:
+ _objc_msgSend$highLevelDomain:isIncludedInTopFraudTargets:
+ _objc_msgSend$isCJK
+ _objc_msgSend$isUndefined
+ _objc_msgSend$lastSearchEngagementEmission
+ _objc_msgSend$modelVersionForLanguage:
+ _objc_msgSend$passwordManagerSecurityRecommendationsURLForBreachNotificationForHighPriorityAccount:
+ _objc_msgSend$searchEngagementLock
+ _objc_msgSend$setLastSearchEngagementEmission:
+ _objc_msgSend$shouldPromoteRecentSearchesStartPageModuleBelowFavorites
+ _objc_msgSend$textEmbedding
+ _objc_msgSend$typeConfidence
+ _symbolic SDyS2SSgG
+ _symbolic _____Sg_ABt 12SafariShared17WBSBookmarksTopicV
+ _symbolic _____yS2SSgG s18_DictionaryStorageC
+ _symbolic _____ySsG s23_ContiguousArrayStorageC
- +[WBSPasswordBreachNotificationManager _highLevelDomain:isIncludedInTopFraudTargets:]
- -[WBSAnalyticsLogger(WBSAnalyticsLoggerExtras) reportNumberOfFlaggedPasswordsUsingSavedAccountAuditorIfNeeded:]
- -[WBSBrowserTabCompletionProvider _compareTabMatch:otherTabMatch:]
- -[WBSBrowserTabCompletionProvider _distanceFromSelectedTabForTabMatch:]
- -[WBSClusteringCalibration _processCalibrationData:]
- -[WBSClusteringCalibration referenceLanguage]
- -[WBSClusteringCalibration referenceMean]
- -[WBSClusteringCalibration referenceStandardDeviation]
- -[WBSEmbeddingStore embedFeatureText:forURL:inProfileIdentifier:lastVisitTime:completionHandler:]
- -[WBSPageContext setPageLanguage:]
- -[WBSPasswordBreachNotificationManager _passwordManagerURLForSavedAccount:]
- -[WBSStartPageSectionManager _sectionsWithRecentSearchesModule:favoritesIndex:recentSearchesIndex:]
- -[WBSTrialSearchParameters shouldPromoteRecentSearchesStartPageModuleBellowFavorites]
- GCC_except_table222
- GCC_except_table240
- GCC_except_table245
- GCC_except_table268
- GCC_except_table276
- GCC_except_table297
- GCC_except_table300
- GCC_except_table312
- GCC_except_table315
- GCC_except_table316
- GCC_except_table319
- GCC_except_table350
- OBJC_IVAR_$_WBSTrialSearchParameters._shouldPromoteRecentSearchesStartPageModuleBellowFavorites
- _OBJC_CLASS_$_WBSPasswordEvaluator
- _TRIAL_shouldPromoteRecentSearchesStartPageModuleBellowFavorites
- _WBSAutoTabClusteringEnabledKey
- _WBSAutoTabClusteringImmediateModeEnabledKey
- _WBSAutoTabClusteringImmediateModeMigratedKey
- _WBSStartPageSectionRecentSearches
- __OBJC_$_CATEGORY_INSTANCE_METHODS_WBSAnalyticsLogger_$_WBSAnalyticsLoggerExtras
- __OBJC_$_CATEGORY_WBSAnalyticsLogger_$_WBSAnalyticsLoggerExtras
- ___111-[WBSAnalyticsLogger(WBSAnalyticsLoggerExtras) reportNumberOfFlaggedPasswordsUsingSavedAccountAuditorIfNeeded:]_block_invoke
- ___53-[WBSStartPageSectionManager readAndValidateSections]_block_invoke_2
- ___53-[WBSStartPageSectionManager readAndValidateSections]_block_invoke_3
- ___53-[WBSStartPageSectionManager readAndValidateSections]_block_invoke_4
- ___97-[WBSEmbeddingStore embedFeatureText:forURL:inProfileIdentifier:lastVisitTime:completionHandler:]_block_invoke
- ___97-[WBSEmbeddingStore embedFeatureText:forURL:inProfileIdentifier:lastVisitTime:completionHandler:]_block_invoke_2
- ___97-[WBSEmbeddingStore embedFeatureText:forURL:inProfileIdentifier:lastVisitTime:completionHandler:]_block_invoke_3
- ___97-[WBSEmbeddingStore embedFeatureText:forURL:inProfileIdentifier:lastVisitTime:completionHandler:]_block_invoke_4
- ___block_descriptor_32_e46_B32?0"WBSStartPageSectionDescriptor"8Q16^B24l
- ___block_descriptor_40_ea8_32s_e71_q24?0"WBSBrowserTabCompletionMatch"8"WBSBrowserTabCompletionMatch"16l
- ___block_descriptor_80_ea8_32s40s48s56s64bs_e17_v16?0"NSArray"8l
- ___block_descriptor_80_ea8_32s40s48s56s64bs_e22_v16?0"WBSEmbedding"8l
- ___block_descriptor_80_ea8_32s40s48s56s64bs_e5_v8?0l
- __swift_closure_destructor.180Tm
- _objc_msgSend$_compareTabMatch:otherTabMatch:
- _objc_msgSend$_distanceFromSelectedTabForTabMatch:
- _objc_msgSend$_highLevelDomain:isIncludedInTopFraudTargets:
- _objc_msgSend$_passwordManagerURLForSavedAccount:
- _objc_msgSend$_processCalibrationData:
- _objc_msgSend$_sendEvent:usingBlock:
- _objc_msgSend$duplicatePasswordsInPasswords:
- _objc_msgSend$embedFeatureText:forURL:inProfileIdentifier:lastVisitTime:completionHandler:
- _objc_msgSend$embedWithItem:completion:
- _objc_msgSend$evaluatePassword:
- _objc_msgSend$isRecentSearchesInStartPageEnabled
- _objc_msgSend$passwordManagerSecurityRecommendationsURL
- _objc_msgSend$safari_timeIntervalUntilNow
- _objc_msgSend$savedAccountStore
- _objc_msgSend$savedAccountsWithPasswords
- _objc_msgSend$shouldPromoteRecentSearchesStartPageModuleBellowFavorites
- _objc_msgSend$standardPasswordEvaluator
- _objc_msgSend$userIsNeverSaveMarker
- _objc_msgSend$userShouldBeShownPassiveWarning
- _symbolic So12NSDictionaryCSgIeyBy_
CStrings:
+ "22625.1.29.11.25"
+ "Agent (%{public}s) has no instructions available for model %{public}s."
+ "AutoFillFormTypeConfidence"
+ "AutoTabClusteringEnabled"
+ "Coalescing duplicate search-engagement donation: previous donation was %{public}ldms ago, within the %{public}ldms coalescing window."
+ "Ejecting over-merged outlier tab from cluster"
+ "EverLaunchedOnPreRaveOSVersion"
+ "Failed to enable WAL mode for magic extensions database: %s"
+ "Failed to query Screen Time policy; treating URL as allowed: %{public}@"
+ "Ignoring bookmark change caused by our own topic write-back"
+ "Ignoring bookmark metadata change caused by our own topic write-back"
+ "No instructions available for model "
+ "No non-excluding calibrated version found for language %{public}@, falling back to default version %lu despite exclusion"
+ "Skipping %ld of %ld topic writes that wouldn't change anything"
+ "com.apple.SafariShared.DownloadFileUnarchiverError"
+ "douyin_comp"
+ "douyin_search"
+ "excludedLanguages"
+ "trialRecentSearchesIdentifier"
- "22625.1.24.11.2"
- "com.apple.Safari.WeakPasswordReport"
- "numberOfFlaggedPasswords"
- "percentageOfFlaggedPasswords"
- "recentSearchesIdentifier"
- "referenceMean"
- "referenceStandardDeviation"
- "totalNumberOfPasswords"
```
