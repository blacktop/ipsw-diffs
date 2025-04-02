## SpotlightServices

> `/System/Library/PrivateFrameworks/SpotlightServices.framework/Versions/A/SpotlightServices`

```diff

-2333.22.13.7.0
-  __TEXT.__text: 0x145488
-  __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_methlist: 0xcb38
-  __TEXT.__const: 0x26a6
-  __TEXT.__cstring: 0x2f901
-  __TEXT.__oslogstring: 0x799c
-  __TEXT.__gcc_except_tab: 0x4248
+2333.41.1.3.0
+  __TEXT.__text: 0x14906c
+  __TEXT.__auth_stubs: 0x1190
+  __TEXT.__objc_methlist: 0xcc60
+  __TEXT.__const: 0x2686
+  __TEXT.__cstring: 0x2ffb1
+  __TEXT.__oslogstring: 0x7f90
+  __TEXT.__gcc_except_tab: 0x42cc
   __TEXT.__ustring: 0x8c2
   __TEXT.__dlopen_cstrs: 0xd1
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x2b60
-  __TEXT.__objc_classname: 0x1161
-  __TEXT.__objc_methname: 0x2626c
-  __TEXT.__objc_methtype: 0x30e4
-  __TEXT.__objc_stubs: 0x19a00
-  __DATA_CONST.__got: 0x1d38
-  __DATA_CONST.__const: 0xe490
+  __TEXT.__unwind_info: 0x2b80
+  __TEXT.__objc_classname: 0x1162
+  __TEXT.__objc_methname: 0x2696c
+  __TEXT.__objc_methtype: 0x312f
+  __TEXT.__objc_stubs: 0x19dc0
+  __DATA_CONST.__got: 0x1d60
+  __DATA_CONST.__const: 0xe4b0
   __DATA_CONST.__objc_classlist: 0x568
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8088
+  __DATA_CONST.__objc_selrefs: 0x8188
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x478
-  __DATA_CONST.__objc_arraydata: 0xb38
-  __AUTH_CONST.__auth_got: 0x8d0
+  __DATA_CONST.__objc_arraydata: 0xba8
+  __AUTH_CONST.__auth_got: 0x8d8
   __AUTH_CONST.__auth_ptr: 0x38
-  __AUTH_CONST.__const: 0x3900
-  __AUTH_CONST.__cfstring: 0x29440
-  __AUTH_CONST.__objc_const: 0x14ae0
-  __AUTH_CONST.__objc_intobj: 0x2fa0
+  __AUTH_CONST.__const: 0x3930
+  __AUTH_CONST.__cfstring: 0x2a080
+  __AUTH_CONST.__objc_const: 0x14cf0
+  __AUTH_CONST.__objc_intobj: 0x2fd0
   __AUTH_CONST.__objc_doubleobj: 0x290
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__objc_arrayobj: 0x4e0
+  __AUTH_CONST.__objc_arrayobj: 0x528
   __AUTH_CONST.__objc_dictobj: 0x208
   __AUTH.__objc_data: 0x25d0
   __AUTH.__data: 0xe8
-  __DATA.__objc_ivar: 0x128c
-  __DATA.__data: 0x1300
-  __DATA.__bss: 0x1308
+  __DATA.__objc_ivar: 0x12b8
+  __DATA.__data: 0x1310
+  __DATA.__bss: 0x1320
   __DATA.__common: 0x2c
   __DATA_DIRTY.__objc_data: 0xff0
   __DATA_DIRTY.__data: 0xc8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5446
-  Symbols:   14199
-  CStrings:  12860
+  Functions: 5479
+  Symbols:   14281
+  CStrings:  13019
 
Symbols:
+ +[PRSRankingItemRanker initialize].cold.1
+ +[SSRankingManager calculateLikelihoodForSearchTool:queryContext:isQUInferredIntent:isEventSearchIntent:]
+ +[SSRankingManager jsonStringFromDictionary:isSearchToolClient:]
+ +[SSRankingManager logItems:prefix:queryId:query:isSearchToolClient:]
+ +[SSRankingManager logSections:prefix:queryId:query:isSearchToolClient:]
+ +[SSRankingManager logStats:prefix:queryId:query:isSearchToolClient:]
+ +[SSRankingManager searchToolExtractDocTextualFeature:queryContext:title:subject:displayName:searchTermsSet:hasOneOnOneInSearchTerm:]
+ +[SSRankingManager searchToolExtractDocTextualFeature:queryContext:title:subject:displayName:searchTermsSet:hasOneOnOneInSearchTerm:].cold.1
+ +[SSRankingManager searchToolShouldFilterEventBeforeRanking:queryContext:matchQUIntent:searchToolBundles:useLLMQU:hasEventTypeFromQU:].cold.1
+ +[SSRankingManager searchToolShouldFilterResultBeforeRanking:queryContext:matchQUIntent:intentAndResultWithStartDueDate:searchToolBundles:useLLMQU:]
+ -[PRSRankingItem countRecipientByEmails]
+ -[PRSRankingItem creationDate]
+ -[PRSRankingItem isLLMQUPersonMatchedInAuthor]
+ -[PRSRankingItem isLLMQUPersonMatchedInOther]
+ -[PRSRankingItem isLLMQUPersonMatchedInRecipient]
+ -[PRSRankingItem populateOnlyPommesL1RankingFeaturesWithQueryID:bundleID:isSearchToolClient:]
+ -[PRSRankingItem rankedInLowerTier]
+ -[PRSRankingItem searchTermsMatchTitle]
+ -[PRSRankingItem setCountRecipientByEmails:]
+ -[PRSRankingItem setCreationDate:]
+ -[PRSRankingItem setIsLLMQUPersonMatchedInAuthor:]
+ -[PRSRankingItem setIsLLMQUPersonMatchedInOther:]
+ -[PRSRankingItem setIsLLMQUPersonMatchedInRecipient:]
+ -[PRSRankingItem setRankedInLowerTier:]
+ -[PRSRankingItem setSearchTermsMatchTitle:]
+ -[PRSRankingItem setWalletBoardingPassPassengerName:]
+ -[PRSRankingItem walletBoardingPassPassengerName]
+ -[PRSRankingItem(Scoring) calculateFreshnessForSearchTool:userSpecifiedStartTime:userSpecifiedEndTime:]
+ -[PRSRankingItemRanker updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:isDocumentSearch:]
+ -[PRSRankingItemRanker updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:isDocumentSearch:].cold.1
+ -[PRSRankingItemRanker updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:isDocumentSearch:].cold.2
+ -[SPSearchQueryContext normalizedSearchTermsFromQU]
+ -[SPSearchQueryContext parsedArgLocationTermsFromQU]
+ -[SPSearchQueryContext rawSearchTermsFromLLMQU]
+ -[SPSearchQueryContext setNormalizedSearchTermsFromQU:]
+ -[SPSearchQueryContext setParsedArgLocationTermsFromQU:]
+ -[SPSearchQueryContext setRawSearchTermsFromLLMQU:]
+ -[SPSearchQueryContext setUniquePersonsFromLLMQU:]
+ -[SPSearchQueryContext uniquePersonsFromLLMQU]
+ -[SSPommesPhotosRanker isSearchToolClient]
+ -[SSPommesPhotosRanker setIsSearchToolClient:]
+ -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:]
+ -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:].cold.1
+ -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:].cold.2
+ -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:].cold.3
+ -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:].cold.4
+ -[SSPommesPhotosRanker updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:isDocumentSearch:]
+ -[SSPommesRanker isSearchToolClient]
+ -[SSPommesRanker setIsSearchToolClient:]
+ -[SSPommesRanker updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:isDocumentSearch:]
+ -[SSRankingManager logPommesScoringForRankingItem:queryId:query:bundleID:name:topicality:freshness:engagement:likelihood:launchPortion:launchCount:launchPortionOutOfSpotlight:launchCountOutOfSpotlight:engagedInSpotlight:exactMatchedLaunchString:lastUsedDate:recentEngagementDateInSpotlight:recentEngagementDateInApp:recentEngagementDateOutSpotlight:nominateLocalTopHit:isSearchToolClient:]
+ -[SSRankingManager sendTTRLogsWithSections:queryContext:isCommittedSearch:parsecCameLaterThanSRT:]
+ GCC_except_table102
+ GCC_except_table147
+ GCC_except_table166
+ GCC_except_table219
+ GCC_except_table260
+ GCC_except_table332
+ GCC_except_table342
+ GCC_except_table45
+ GCC_except_table51
+ GCC_except_table56
+ GCC_except_table62
+ GCC_except_table64
+ GCC_except_table67
+ GCC_except_table74
+ GCC_except_table77
+ OBJC_IVAR_$_PRSRankingItem._countRecipientByEmails
+ OBJC_IVAR_$_PRSRankingItem._creationDate
+ OBJC_IVAR_$_PRSRankingItem._isLLMQUPersonMatchedInAuthor
+ OBJC_IVAR_$_PRSRankingItem._isLLMQUPersonMatchedInOther
+ OBJC_IVAR_$_PRSRankingItem._isLLMQUPersonMatchedInRecipient
+ OBJC_IVAR_$_PRSRankingItem._rankedInLowerTier
+ OBJC_IVAR_$_PRSRankingItem._searchTermsMatchTitle
+ OBJC_IVAR_$_PRSRankingItem._walletBoardingPassPassengerName
+ OBJC_IVAR_$_SPSearchQueryContext._normalizedSearchTermsFromQU
+ OBJC_IVAR_$_SPSearchQueryContext._parsedArgLocationTermsFromQU
+ OBJC_IVAR_$_SPSearchQueryContext._rawSearchTermsFromLLMQU
+ OBJC_IVAR_$_SPSearchQueryContext._uniquePersonsFromLLMQU
+ OBJC_IVAR_$_SSPommesPhotosRanker._isSearchToolClient
+ OBJC_IVAR_$_SSPommesRanker._isSearchToolClient
+ SSEnableSearchToolDebugMode.cold.1
+ SSEnableSearchToolDebugMode.enabled
+ SSEnableSearchToolDebugMode.onceToken
+ SSRedactStringClient.cold.1
+ SSRedactStringClient.isSearchToolDebugMode
+ SSRedactStringClient.onceToken
+ _MDItemAppEntityTypeDisplayRepresentationName
+ _MDItemIsFromMe
+ _NLTagSchemeTokenType
+ _OBJC_CLASS_$_NLTagger
+ _OBJC_CLASS_$_NSMutableData
+ _SSEnableSearchToolDebugMode
+ _SSRedactStringClient
+ __163+[SSRankingManager searchToolSortResults:isQUIntent:isQUInferredIntent:queryContext:searchToolBundles:eventSearchIntent:maxTopicalityPerBundle:preExtractionBoost:]_block_invoke.1445
+ __186-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:]_block_invoke.334
+ __186-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:]_block_invoke.337
+ __186-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:]_block_invoke.338
+ __186-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:]_block_invoke_2.339
+ __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke.926
+ __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke.930
+ __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke.943
+ __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke.947
+ __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke.962
+ __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke.967
+ __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke_2.934
+ __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke_2.970
+ __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke_2.970.cold.1
+ __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke_3.971
+ __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke_4.974
+ __261-[SSRankingManager nominateLocalTopHitsFromSections:withItemRanker:sectionHeader:maxInitiallyVisibleResults:shortcutResult:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:parsecEnabled:maxNumAppsInTopHitSection:queryId:isSearchToolClient:qu:currentTime:]_block_invoke.561
+ __40-[PRSRankingItemRanker parseLLMQUQuery:]_block_invoke.979
+ __57-[PRSRankingItemRanker prepareItems:inRealSectionBundle:]_block_invoke.1186
+ __65-[SSRankingManager withinSectionTopHitNomination:withItemRanker:]_block_invoke.549
+ __66-[PRSRankingItemRanker computePolicyFeaturesForBundleItems:isCJK:]_block_invoke.1155
+ __66-[PRSRankingItemRanker rerankItemsWithPolicyForBundleItems:isCJK:]_block_invoke.1164
+ __66-[PRSRankingItemRanker rerankItemsWithPolicyForBundleItems:isCJK:]_block_invoke.1168
+ __66-[PRSRankingItemRanker rerankItemsWithPolicyForBundleItems:isCJK:]_block_invoke.1169
+ __66-[PRSRankingItemRanker rerankItemsWithPolicyForBundleItems:isCJK:]_block_invoke.1170
+ __66-[PRSRankingItemRanker rerankItemsWithPolicyForBundleItems:isCJK:]_block_invoke.1171
+ __66-[PRSRankingItemRanker rerankItemsWithPolicyForBundleItems:isCJK:]_block_invoke.1172
+ __66-[PRSRankingItemRanker rerankItemsWithPolicyForBundleItems:isCJK:]_block_invoke.1173
+ __66-[PRSRankingItemRanker rerankItemsWithPolicyForBundleItems:isCJK:]_block_invoke_2.1165
+ __66-[PRSRankingItemRanker rerankItemsWithPolicyForBundleItems:isCJK:]_block_invoke_3.1167
+ __68+[SSRankingManager searchToolRanker:queryContext:searchToolBundles:]_block_invoke.1492
+ __68+[SSRankingManager searchToolRanker:queryContext:searchToolBundles:]_block_invoke.1499
+ __SSQueryParserStripKindFromString_block_invoke.285
+ __SSQueryParserStripKindFromString_block_invoke.292
+ ___105+[SSRankingManager calculateLikelihoodForSearchTool:queryContext:isQUInferredIntent:isEventSearchIntent:]_block_invoke
+ ___133+[SSRankingManager searchToolExtractDocTextualFeature:queryContext:title:subject:displayName:searchTermsSet:hasOneOnOneInSearchTerm:]_block_invoke
+ ___133+[SSRankingManager searchToolExtractDocTextualFeature:queryContext:title:subject:displayName:searchTermsSet:hasOneOnOneInSearchTerm:]_block_invoke_2
+ ___186-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:]_block_invoke
+ ___186-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:]_block_invoke_2
+ ___34+[PRSRankingItemRanker initialize]_block_invoke
+ ___SSEnableSearchToolDebugMode_block_invoke
+ ___SSRedactStringClient_block_invoke
+ ___block_descriptor_41_e8_32s_e34_v32?0"NSString"8"NSArray"16^B24l
+ ___block_descriptor_82_e8_32s40s48s56s64s72s_e75_q24?0"SFSearchResult_SpotlightExtras"8"SFSearchResult_SpotlightExtras"16l
+ ___isOptionalSearchTermForPreExtractionFilter_block_invoke
+ __block_literal_global.1038
+ __block_literal_global.106
+ __block_literal_global.1113
+ __block_literal_global.1128
+ __block_literal_global.1139
+ __block_literal_global.1149
+ __block_literal_global.1184
+ __block_literal_global.1188
+ __block_literal_global.124
+ __block_literal_global.1310
+ __block_literal_global.1312
+ __block_literal_global.1314
+ __block_literal_global.133
+ __block_literal_global.1359
+ __block_literal_global.1379
+ __block_literal_global.1419
+ __block_literal_global.1450
+ __block_literal_global.1472
+ __block_literal_global.1521
+ __block_literal_global.1524
+ __block_literal_global.176
+ __block_literal_global.2098
+ __block_literal_global.2109
+ __block_literal_global.315
+ __block_literal_global.326
+ __block_literal_global.394
+ __block_literal_global.413
+ __block_literal_global.452
+ __block_literal_global.485
+ __block_literal_global.495
+ __block_literal_global.551
+ __block_literal_global.560
+ __block_literal_global.563
+ __block_literal_global.566
+ __block_literal_global.809
+ __block_literal_global.817
+ __block_literal_global.822
+ __block_literal_global.827
+ __block_literal_global.832
+ __block_literal_global.837
+ __block_literal_global.869
+ __block_literal_global.877
+ __block_literal_global.879
+ __block_literal_global.891
+ __block_literal_global.898
+ __block_literal_global.900
+ __block_literal_global.902
+ __block_literal_global.919
+ __block_literal_global.921
+ __block_literal_global.923
+ __block_literal_global.933
+ __block_literal_global.936
+ __block_literal_global.938
+ __block_literal_global.940
+ __block_literal_global.964
+ __block_literal_global.969
+ __block_literal_global.973
+ __block_literal_global.976
+ __block_literal_global.982
+ __getMatchInfoDictionary_block_invoke.481
+ __getMatchInfoDictionary_block_invoke_2.482
+ __loadRankingThresholdingParameters_block_invoke.cold.3
+ _decodeString
+ _emailUpdatesDemotion
+ _emailUpdatesSenderList
+ _encodeString
+ _getEnumValueFromIntentArgString
+ _hasTrailingAsterisk
+ _isSpotlightForSearchToolRegressionTest
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$alphanumericCharacterSet
+ _objc_msgSend$appendBytes:length:
+ _objc_msgSend$calculateFreshnessForSearchTool:userSpecifiedStartTime:userSpecifiedEndTime:
+ _objc_msgSend$calculateLikelihoodForSearchTool:queryContext:isQUInferredIntent:isEventSearchIntent:
+ _objc_msgSend$countRecipientByEmails
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$dataWithCapacity:
+ _objc_msgSend$enumerateTagsInRange:unit:scheme:options:usingBlock:
+ _objc_msgSend$filteredSetUsingPredicate:
+ _objc_msgSend$initWithBase64EncodedString:options:
+ _objc_msgSend$initWithTagSchemes:
+ _objc_msgSend$isEqualToSet:
+ _objc_msgSend$isLLMQUPersonMatchedInAuthor
+ _objc_msgSend$isLLMQUPersonMatchedInRecipient
+ _objc_msgSend$isSubsetOfSet:
+ _objc_msgSend$jsonStringFromDictionary:isSearchToolClient:
+ _objc_msgSend$logPommesScoringForRankingItem:queryId:query:bundleID:name:topicality:freshness:engagement:likelihood:launchPortion:launchCount:launchPortionOutOfSpotlight:launchCountOutOfSpotlight:engagedInSpotlight:exactMatchedLaunchString:lastUsedDate:recentEngagementDateInSpotlight:recentEngagementDateInApp:recentEngagementDateOutSpotlight:nominateLocalTopHit:isSearchToolClient:
+ _objc_msgSend$logSections:prefix:queryId:query:isSearchToolClient:
+ _objc_msgSend$normalizedSearchTermsFromQU
+ _objc_msgSend$parsedArgLocationTermsFromQU
+ _objc_msgSend$populateOnlyPommesL1RankingFeaturesWithQueryID:bundleID:isSearchToolClient:
+ _objc_msgSend$rankedInLowerTier
+ _objc_msgSend$rawSearchTermsFromLLMQU
+ _objc_msgSend$searchTermsMatchTitle
+ _objc_msgSend$searchToolExtractDocTextualFeature:queryContext:title:subject:displayName:searchTermsSet:hasOneOnOneInSearchTerm:
+ _objc_msgSend$searchToolShouldFilterResultBeforeRanking:queryContext:matchQUIntent:intentAndResultWithStartDueDate:searchToolBundles:useLLMQU:
+ _objc_msgSend$setCountRecipientByEmails:
+ _objc_msgSend$setIsLLMQUPersonMatchedInAuthor:
+ _objc_msgSend$setIsLLMQUPersonMatchedInOther:
+ _objc_msgSend$setIsLLMQUPersonMatchedInRecipient:
+ _objc_msgSend$setNormalizedSearchTermsFromQU:
+ _objc_msgSend$setParsedArgLocationTermsFromQU:
+ _objc_msgSend$setRankedInLowerTier:
+ _objc_msgSend$setRawSearchTermsFromLLMQU:
+ _objc_msgSend$setSearchTermsMatchTitle:
+ _objc_msgSend$setUniquePersonsFromLLMQU:
+ _objc_msgSend$tokenLabel
+ _objc_msgSend$updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:
+ _objc_msgSend$updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:isDocumentSearch:
+ _objc_msgSend$updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:isDocumentSearch:
+ _sSetOfOneOnOneMeetingKeywords
+ isOptionalSearchTermForPreExtractionFilter.OptionalSearchTerms
+ isOptionalSearchTermForPreExtractionFilter.onceToken
+ searchToolExtractDocTextualFeature:queryContext:title:subject:displayName:searchTermsSet:hasOneOnOneInSearchTerm:.nlTagger
+ searchToolExtractDocTextualFeature:queryContext:title:subject:displayName:searchTermsSet:hasOneOnOneInSearchTerm:.onceToken
+ serializeToDictForBiomeDonation.dateArrayAttributes
+ serializeToDictForBiomeDonation.extraDataAttributes
- +[SSRankingManager calculateLikelihoodForSearchTool:queryContext:isQUInferredIntent:]
- +[SSRankingManager initialize].cold.1
- +[SSRankingManager logItems:prefix:queryId:query:]
- +[SSRankingManager logStats:prefix:queryId:query:]
- +[SSRankingManager searchToolRanker:queryContext:searchToolBundles:].cold.3
- +[SSRankingManager searchToolShouldFilterResultBeforeRanking:queryContext:matchQUIntent:intentAndResultWithStartDueDate:isCleanSlate:searchToolBundles:useLLMQU:]
- -[PRSRankingItem populateOnlyPommesL1RankingFeaturesWithQueryID:isSearchToolClient:]
- -[PRSRankingItem(Scoring) calculateFreshnessForSearchTool:]
- -[PRSRankingItemRanker updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:]
- -[PRSRankingItemRanker updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:].cold.1
- -[PRSRankingItemRanker updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:].cold.2
- -[PRSRankingItemRanker updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:].cold.3
- -[SPSearchQueryContext entityL1Score]
- -[SPSearchQueryContext initWithSearchString:].cold.1
- -[SPSearchQueryContext initWithSearchString:currentTime:].cold.1
- -[SPSearchQueryContext setEntityL1Score:]
- -[SSPommesPhotosRanker estimatedMaxPommesL1Score]
- -[SSPommesPhotosRanker setEstimatedMaxPommesL1Score:]
- -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:]
- -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:].cold.1
- -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:].cold.2
- -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:].cold.3
- -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:].cold.4
- -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:].cold.5
- -[SSPommesPhotosRanker updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:]
- -[SSPommesRanker estimatedMaxPommesL1Score]
- -[SSPommesRanker setEstimatedMaxPommesL1Score:]
- -[SSPommesRanker updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:]
- -[SSRankingManager logPommesScoringForRankingItem:queryId:query:bundleID:name:topicality:freshness:engagement:likelihood:launchPortion:launchCount:launchPortionOutOfSpotlight:launchCountOutOfSpotlight:engagedInSpotlight:exactMatchedLaunchString:lastUsedDate:recentEngagementDateInSpotlight:recentEngagementDateInApp:recentEngagementDateOutSpotlight:nominateLocalTopHit:isSearchTool:]
- -[SSRankingManager sendTTRLogsWithSections:searchString:queryKind:isCommittedSearch:parsecCameLaterThanSRT:]
- GCC_except_table141
- GCC_except_table157
- GCC_except_table162
- GCC_except_table165
- GCC_except_table179
- GCC_except_table259
- GCC_except_table331
- GCC_except_table341
- GCC_except_table44
- GCC_except_table55
- GCC_except_table61
- GCC_except_table63
- GCC_except_table66
- GCC_except_table70
- GCC_except_table72
- GCC_except_table76
- GCC_except_table99
- OBJC_IVAR_$_SPSearchQueryContext._entityL1Score
- OBJC_IVAR_$_SSPommesPhotosRanker._estimatedMaxPommesL1Score
- OBJC_IVAR_$_SSPommesRanker._estimatedMaxPommesL1Score
- SPQueryIsSearchToolClient.isSearchToolDebugMode
- SPQueryIsSearchToolClient.isSearchToolRanking
- SPQueryIsSearchToolClient.onceToken
- SSEnableSearchToolCleanSlate.cold.1
- SSEnableSearchToolCleanSlate.enabled
- SSEnableSearchToolCleanSlate.onceToken
- SSRedactString.cold.1
- SSRedactString.isSearchToolDebugMode
- SSRedactString.onceToken
- _SSEnableSearchToolCleanSlate
- __169-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:]_block_invoke.334
- __169-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:]_block_invoke.337
- __169-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:]_block_invoke.338
- __169-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:]_block_invoke_2.339
- __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke.726
- __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke.730
- __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke.743
- __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke.745
- __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke.760
- __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke.765
- __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke_2.734
- __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke_2.768
- __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke_2.768.cold.1
- __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke_3.769
- __204-[SSRankingManager rankSectionsUsingBundleIDToSectionMapping:withRanker:preferredBundleIds:isScopedSearch:queryId:isCJK:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:isPeopleSearch:queryContext:]_block_invoke_4.772
- __261-[SSRankingManager nominateLocalTopHitsFromSections:withItemRanker:sectionHeader:maxInitiallyVisibleResults:shortcutResult:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:parsecEnabled:maxNumAppsInTopHitSection:queryId:isSearchToolClient:qu:currentTime:]_block_invoke.551
- __57-[PRSRankingItemRanker prepareItems:inRealSectionBundle:]_block_invoke.1159
- __65-[SSRankingManager withinSectionTopHitNomination:withItemRanker:]_block_invoke.539
- __66-[PRSRankingItemRanker computePolicyFeaturesForBundleItems:isCJK:]_block_invoke.1128
- __66-[PRSRankingItemRanker rerankItemsWithPolicyForBundleItems:isCJK:]_block_invoke.1137
- __66-[PRSRankingItemRanker rerankItemsWithPolicyForBundleItems:isCJK:]_block_invoke.1141
- __66-[PRSRankingItemRanker rerankItemsWithPolicyForBundleItems:isCJK:]_block_invoke.1142
- __66-[PRSRankingItemRanker rerankItemsWithPolicyForBundleItems:isCJK:]_block_invoke.1143
- __66-[PRSRankingItemRanker rerankItemsWithPolicyForBundleItems:isCJK:]_block_invoke.1144
- __66-[PRSRankingItemRanker rerankItemsWithPolicyForBundleItems:isCJK:]_block_invoke.1145
- __66-[PRSRankingItemRanker rerankItemsWithPolicyForBundleItems:isCJK:]_block_invoke.1146
- __66-[PRSRankingItemRanker rerankItemsWithPolicyForBundleItems:isCJK:]_block_invoke_2.1138
- __66-[PRSRankingItemRanker rerankItemsWithPolicyForBundleItems:isCJK:]_block_invoke_3.1140
- __68+[SSRankingManager searchToolRanker:queryContext:searchToolBundles:]_block_invoke.1224
- __68+[SSRankingManager searchToolRanker:queryContext:searchToolBundles:]_block_invoke.1225
- __68+[SSRankingManager searchToolRanker:queryContext:searchToolBundles:]_block_invoke.1234
- __SSQueryParserStripKindFromString_block_invoke.282
- __SSQueryParserStripKindFromString_block_invoke.289
- ___138-[PRSRankingItemRanker updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:]_block_invoke
- ___169-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:]_block_invoke
- ___169-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:]_block_invoke_2
- ___85+[SSRankingManager calculateLikelihoodForSearchTool:queryContext:isQUInferredIntent:]_block_invoke
- ___SPQueryIsSearchToolClient_block_invoke
- ___SSEnableSearchToolCleanSlate_block_invoke
- ___SSRedactString_block_invoke
- ___block_descriptor_74_e8_32s40s48s56s64s_e75_q24?0"SFSearchResult_SpotlightExtras"8"SFSearchResult_SpotlightExtras"16l
- __block_literal_global.1005
- __block_literal_global.1082
- __block_literal_global.1087
- __block_literal_global.1094
- __block_literal_global.1101
- __block_literal_global.1112
- __block_literal_global.1134
- __block_literal_global.1154
- __block_literal_global.1157
- __block_literal_global.1176
- __block_literal_global.118
- __block_literal_global.1216
- __block_literal_global.1219
- __block_literal_global.1227
- __block_literal_global.1270
- __block_literal_global.1272
- __block_literal_global.1274
- __block_literal_global.130
- __block_literal_global.1494
- __block_literal_global.1497
- __block_literal_global.175
- __block_literal_global.1827
- __block_literal_global.312
- __block_literal_global.323
- __block_literal_global.393
- __block_literal_global.412
- __block_literal_global.443
- __block_literal_global.451
- __block_literal_global.484
- __block_literal_global.489
- __block_literal_global.541
- __block_literal_global.550
- __block_literal_global.553
- __block_literal_global.556
- __block_literal_global.605
- __block_literal_global.609
- __block_literal_global.617
- __block_literal_global.622
- __block_literal_global.627
- __block_literal_global.632
- __block_literal_global.637
- __block_literal_global.683
- __block_literal_global.721
- __block_literal_global.723
- __block_literal_global.733
- __block_literal_global.736
- __block_literal_global.738
- __block_literal_global.740
- __block_literal_global.762
- __block_literal_global.767
- __block_literal_global.771
- __block_literal_global.774
- __block_literal_global.871
- __block_literal_global.873
- __block_literal_global.885
- __block_literal_global.888
- __block_literal_global.890
- __block_literal_global.892
- __block_literal_global.911
- __block_literal_global.913
- __block_literal_global.915
- __getMatchInfoDictionary_block_invoke.480
- __getMatchInfoDictionary_block_invoke_2.481
- _objc_msgSend$addResultsFromArray:
- _objc_msgSend$calculateFreshnessForSearchTool:
- _objc_msgSend$calculateLikelihoodForSearchTool:queryContext:isQUInferredIntent:
- _objc_msgSend$entityL1Score
- _objc_msgSend$logPommesScoringForRankingItem:queryId:query:bundleID:name:topicality:freshness:engagement:likelihood:launchPortion:launchCount:launchPortionOutOfSpotlight:launchCountOutOfSpotlight:engagedInSpotlight:exactMatchedLaunchString:lastUsedDate:recentEngagementDateInSpotlight:recentEngagementDateInApp:recentEngagementDateOutSpotlight:nominateLocalTopHit:isSearchTool:
- _objc_msgSend$populateOnlyPommesL1RankingFeaturesWithQueryID:isSearchToolClient:
- _objc_msgSend$searchToolShouldFilterResultBeforeRanking:queryContext:matchQUIntent:intentAndResultWithStartDueDate:isCleanSlate:searchToolBundles:useLLMQU:
- _objc_msgSend$setEntityL1Score:
- _objc_msgSend$updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:
- _objc_msgSend$updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:
- _objc_msgSend$updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:
- processSearchToolFinalResults:queryContext:.isSearchToolAllBundlesEnabled
- searchToolRanker:queryContext:searchToolBundles:.isDebug
- searchToolRanker:queryContext:searchToolBundles:.onceTokenSTDebug
- updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:.isDebug
- updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:.onceToken
CStrings:
+ "\x02Jc\x16-"
+ "\x13\xf0\x11a\x1f\x042\x16A$\xf02"
+ "1 on 1"
+ "1 on 1 appointment"
+ "1 on 1 appointments"
+ "1 on 1 event"
+ "1 on 1 events"
+ "1 on 1 meeting"
+ "1 on 1 meetings"
+ "1 to 1"
+ "1 to 1 appointment"
+ "1 to 1 appointments"
+ "1 to 1 event"
+ "1 to 1 events"
+ "1 to 1 meeting"
+ "1 to 1 meetings"
+ "1-1"
+ "1-1 appointment"
+ "1-1 appointments"
+ "1-1 event"
+ "1-1 events"
+ "1-1 meeting"
+ "1-1 meetings"
+ "1/1"
+ "1/1 appointment"
+ "1/1 appointments"
+ "1/1 event"
+ "1/1 events"
+ "1/1 meeting"
+ "1/1 meetings"
+ "1:1"
+ "1:1 appointment"
+ "1:1 appointments"
+ "1:1 event"
+ "1:1 events"
+ "1:1 meeting"
+ "1:1 meetings"
+ "AllSearchTerm"
+ "AllTokenMatch"
+ "B52@0:8@16@24B32B36@40B48"
+ "Calender/Reminder matched recipient/author"
+ "Calender/Reminder matched title"
+ "Email Label: Promotional"
+ "EmailUpdatesDemotion"
+ "EmailUpdatesSenderList"
+ "EwEaHRxEBhgEPgRACAYD"
+ "EwMbFR8BSRsQfAAeGwULSSYBDg=="
+ "FinalResult"
+ "IRELFR4pBhgEPgRACAYD"
+ "IxkKWQsAEwABMEwABBsLFykXIw4UGQICfRMAGQ=="
+ "JSONObjectWithData:options:error:"
+ "MhQIKw4GEygVIhECDkcNCCg="
+ "NAUOBggABgZZIRUPHxwdJyIcDBoURw8XIxwKWg8GCg=="
+ "NBkbHBkLJw8dJgkbCUceBjcdBgxKCB4XPxVBFwME"
+ "NotMatch"
+ "PR8dERwFHigTOxUGHgtAFCwcCkEFGR4LNl4MGwE="
+ "PerfectMatch"
+ "QU Inferred entity match"
+ "RankedResult"
+ "RetrievalResult"
+ "SELF LIKE[cd] %@"
+ "SpotlightForSearchToolRegressionTest"
+ "SpotlightRankingEncoding"
+ "T@\"NSArray\",&,N,V_normalizedSearchTermsFromQU"
+ "T@\"NSSet\",&,N,V_rawSearchTermsFromLLMQU"
+ "T@\"NSSet\",&,N,V_uniquePersonsFromLLMQU"
+ "T@\"NSString\",&,N,V_parsedArgLocationTermsFromQU"
+ "T@\"NSString\",&,N,V_walletBoardingPassPassengerName"
+ "TB,N,V_isLLMQUPersonMatchedInAuthor"
+ "TB,N,V_isLLMQUPersonMatchedInOther"
+ "TB,N,V_isLLMQUPersonMatchedInRecipient"
+ "TB,N,V_rankedInLowerTier"
+ "Ti,N,V_countRecipientByEmails"
+ "Tq,N,V_searchTermsMatchTitle"
+ "[Demotion]"
+ "[Promotion]"
+ "[Promotion] [Shared Link]"
+ "[SpotlightRanking] [QU] [LLM] query=%@ LLM_QU_Intent=%@ LLM_QU_Inferred_Intent=%@ detected earliest=%i latest=%i parsedQueryFromQU=[%@] parsedPersonFromQU=[%@] hasQueryContextEmbedding=%i queryType=%@ queryTime=%f queryDate=[%@] userSpecififedStartDate=[%@] userSpecifiedEndDate=[%@]"
+ "[SpotlightRanking] [QU] [LLM] query=%@ detected only one of user specified start/end date for user specified time, reset both. queryTime=%f queryDate=[%@] userSpecififedStartDate=[%@] userSpecifiedEndDate=[%@]"
+ "[SpotlightRanking] [QU] [LLM] query=%@ detected user specified end date is earlier than queryTime, reset them. queryTime=%f queryDate=[%@] userSpecififedStartDate=[%@] userSpecifiedEndDate=[%@]"
+ "[SpotlightRanking] [QU] [LLM] query=%@ detected user specified start date is greater than queryTime, reset them. queryTime=%f queryDate=[%@] userSpecififedStartDate=[%@] userSpecifiedEndDate=[%@]"
+ "[SpotlightRanking] [SearchTool] %@ query=%@ identifier=%@ name=[%@] due to %@"
+ "[SpotlightRanking] [SearchTool] [Boosting] Boosted likelihood for inferred app entity match for item=%@ likelihhod=%0.2f"
+ "[SpotlightRanking] [SearchTool] [Calendar] Found one on one search term in the calendar item with id %@."
+ "[SpotlightRanking] [SearchTool] [Calendar] ID:%@, title:%@, Perfect match for one on one meeting queries with single recipient calendar item. Either no person token or person tokens matched in author/recipient."
+ "[SpotlightRanking] [SearchTool] [Calendar] ID:%@, title:%@, calendarEventRecipientsEmailAddresses: %d, personMatchInRecipient:%d, personMatchInAuthor:%d, personMatchOtherThanRecipient:%d."
+ "[SpotlightRanking] [SearchTool] [DefaultDenseScore] query=%@ bundleId=%@ identifier=%@ MDItemIdentifier=%@ searchTermsMatchTitle=%@ assigned default dense score %f"
+ "[SpotlightRanking] [SearchTool] [Demotion] Demoted item=%@ likelihood=0.0 content creation date=%@ is not within user specified time startDate=%@ endDate=%@"
+ "[SpotlightRanking] [SearchTool] [Demotion] Demoted item=%@ likelihood=0.0 pre-extraction startDate=%@ endDate=%@ is not within user specified time startDate=%@ endDate=%@"
+ "[SpotlightRanking] [SearchTool] [Demotion] Demoted likelihood for email update item=%@ subject=[%@] likelihood=%0.2f"
+ "[SpotlightRanking] [SearchTool] [QU] query=%@ useLLMQU=%i QU_Intent=%s LLM_QU_Intent=%@ LLM_QU_Inferred_Intent=%@ earliest=%i latest=%i parsedQueryFromQU=%@ hasQueryContextEmbedding=%i queryType=%@ queryTime=%f queryDate=[%@] userSpecififedStartDate=[%@] userSpecifiedEndDate=[%@]"
+ "[SpotlightRanking] [SearchTool] [Query] Found one on one search term in the query."
+ "[SpotlightRanking] [SearchTool] [personal answers] for query=%@, skipped filtering event due to optional search term =%@"
+ "[SpotlightRanking] [SearchTool] dedupe result %@ with MDItemContentURL"
+ "[SpotlightRanking] [SearchTool] emailUpdatesSenderList loaded: %@"
+ "[SpotlightRanking] [SearchTool] qid=[%llu] query=%@ filter %d-days-old Mail and Messages results %@ bundle=%@ identifier=%@ MDItemIdentifier=%@ for event type and future intent mostRecentTimeToQueryInMinutesForFreshness=%ld"
+ "[SpotlightRanking] [SearchTool] query=%@ bundleId=%@ identifier=%@ MDItemIdentifier=%@ assigned 0 dense score due to location mismatch"
+ "[SpotlightRanking] [SearchTool] query=%@ qid=%llu ranked result %i: bundleId=%@ identifier=%@ MDItemIdentifier=%@ name=%@ score=(likelihood=%f topicality=%f pommesL1Score=%f pommesCalibratedL1Score=%f embeddingSimilarity=%f keywordMatchScore=%f freshness=%f engagement=%f pommesL2Score=%f) documentSignals=(detectedEventTypes=%@ isMailCategoryHighImpact=%i isMailCategoryPromotions=%i startDueDateToNowInSeconds=%ld isCalendarFlightEventType=%i isCalendarHotelEventType=%i isCalendarRestaurantEventTyp=%i isCalendarOtherReservationEventType=%i mostRecentTimeToQueryInDays=%ld) documentEmbeddingAvailable=%d searchTermsMatchTitle=%@"
+ "[SpotlightRanking] [SearchTool] query=%@ ranked result %i: bundleId=%@ identifier=%@ MDItemIdentifier=%@ messageID=%@ messageHeader=%@ contentURL=%@ appEntityInstanceId=%@ name=%@ score=(likelihood=%f topicality=%f pommesL1Score=%f pommesCalibratedL1Score=%f embeddingSimilarity=%f keywordMatchScore=%f freshness=%f engagement=%f pommesL2Score=%f normalizedSparseScore=%f) documentSignals=(detectedEventTypes=%@ isMailCategoryHighImpact=%i isMailCategoryPromotions=%i startDueDateToNowInSeconds=%ld isCalendarFlightEventType=%i isCalendarHotelEventType=%i isCalendarRestaurantEventTyp=%i isCalendarOtherReservationEventType=%i mostRecentTimeToQueryInMinutes=%ld) topicalityAnonFeatDict=(%@) dates=(lastUsedDate=[%@] contentCreationDate=[%@] contentModificationDate=[%@] receivedDate=[%@] sentDate=[%@] startDate=[%@] endDate=[%@]) retrievalType=%i documentEmbeddingAvailable=%d searchTermsMatchTitle=%@"
+ "_countRecipientByEmails"
+ "_isLLMQUPersonMatchedInAuthor"
+ "_isLLMQUPersonMatchedInOther"
+ "_isLLMQUPersonMatchedInRecipient"
+ "_normalizedSearchTermsFromQU"
+ "_parsedArgLocationTermsFromQU"
+ "_rankedInLowerTier"
+ "_rawSearchTermsFromLLMQU"
+ "_searchTermsMatchTitle"
+ "_uniquePersonsFromLLMQU"
+ "_walletBoardingPassPassengerName"
+ "alphanumericCharacterSet"
+ "appendBytes:length:"
+ "appointments"
+ "bookings"
+ "calculateFreshnessForSearchTool:userSpecifiedStartTime:userSpecifiedEndTime:"
+ "calculateLikelihoodForSearchTool:queryContext:isQUInferredIntent:isEventSearchIntent:"
+ "com.apple.ist.customapp.radar"
+ "confirmations"
+ "countRecipientByEmails"
+ "dataUsingEncoding:"
+ "dataWithCapacity:"
+ "enumerateTagsInRange:unit:scheme:options:usingBlock:"
+ "filteredSetUsingPredicate:"
+ "initWithBase64EncodedString:options:"
+ "initWithTagSchemes:"
+ "isEqualToSet:"
+ "isLLMQUPersonMatchedInAuthor"
+ "isLLMQUPersonMatchedInOther"
+ "isLLMQUPersonMatchedInRecipient"
+ "isSubsetOfSet:"
+ "jsonStringFromDictionary:isSearchToolClient:"
+ "kQPQUOutputTokenRawText"
+ "length > 0"
+ "logItems:prefix:queryId:query:isSearchToolClient:"
+ "logPommesScoringForRankingItem:queryId:query:bundleID:name:topicality:freshness:engagement:likelihood:launchPortion:launchCount:launchPortionOutOfSpotlight:launchCountOutOfSpotlight:engagedInSpotlight:exactMatchedLaunchString:lastUsedDate:recentEngagementDateInSpotlight:recentEngagementDateInApp:recentEngagementDateOutSpotlight:nominateLocalTopHit:isSearchToolClient:"
+ "logSections:prefix:queryId:query:isSearchToolClient:"
+ "logStats:prefix:queryId:query:isSearchToolClient:"
+ "meeting"
+ "meetings"
+ "normalizedSearchTermsFromQU"
+ "one on one"
+ "one on one appointment"
+ "one on one appointments"
+ "one on one event"
+ "one on one events"
+ "one on one meeting"
+ "one on one meetings"
+ "one to one"
+ "one to one appointment"
+ "one to one appointments"
+ "one to one event"
+ "one to one events"
+ "one to one meeting"
+ "one to one meetings"
+ "one-on-one"
+ "one-on-one appointment"
+ "one-on-one appointments"
+ "one-on-one event"
+ "one-on-one events"
+ "one-on-one meeting"
+ "one-on-one meetings"
+ "one-to-one"
+ "one-to-one appointment"
+ "one-to-one appointments"
+ "one-to-one event"
+ "one-to-one events"
+ "one-to-one meeting"
+ "one-to-one meetings"
+ "parsedArgLocationTermsFromQU"
+ "populateOnlyPommesL1RankingFeaturesWithQueryID:bundleID:isSearchToolClient:"
+ "rankedInLowerTier"
+ "rawSearchTermsFromLLMQU"
+ "resolveDatesInFuture"
+ "resolveDatesInPast"
+ "searchTermsMatchTitle"
+ "searchToolExtractDocTextualFeature:queryContext:title:subject:displayName:searchTermsSet:hasOneOnOneInSearchTerm:"
+ "searchToolShouldFilterResultBeforeRanking:queryContext:matchQUIntent:intentAndResultWithStartDueDate:searchToolBundles:useLLMQU:"
+ "sendTTRLogsWithSections:queryContext:isCommittedSearch:parsecCameLaterThanSRT:"
+ "setCountRecipientByEmails:"
+ "setIsLLMQUPersonMatchedInAuthor:"
+ "setIsLLMQUPersonMatchedInOther:"
+ "setIsLLMQUPersonMatchedInRecipient:"
+ "setNormalizedSearchTermsFromQU:"
+ "setParsedArgLocationTermsFromQU:"
+ "setRankedInLowerTier:"
+ "setRawSearchTermsFromLLMQU:"
+ "setSearchTermsMatchTitle:"
+ "setUniquePersonsFromLLMQU:"
+ "setWalletBoardingPassPassengerName:"
+ "shared link type and QU Inferred entity match"
+ "uniquePersonsFromLLMQU"
+ "updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:"
+ "updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:isDocumentSearch:"
+ "updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:isDocumentSearch:"
+ "v36@0:8q16@24B32"
+ "v40@0:8@16@24B32B36"
+ "v40@0:8d16d24d32"
+ "v52@0:8@16@24Q32@40B48"
+ "v64@0:8@16B24@28d36@44B52B56B60"
+ "v68@0:8@16@24@32@40@48@56B64"
+ "v80@0:8@16@24@32q40d48B56@60B68B72B76"
+ "v80@0:8@16@24d32B40@44@52B60@64B72B76"
+ "walletBoardingPassPassengerName"
- "\x02Zc\x16)"
- "\x13\xf1a\x1f\x032\x16A\x13\xf02"
- "B56@0:8@16@24B32B36B40@44B52"
- "SearchToolAllBundles"
- "SearchToolCleanSlateDenseRetrieval"
- "SearchToolNoPhoto"
- "SearchToolRanking"
- "Tf,N,V_entityL1Score"
- "Tf,N,V_estimatedMaxPommesL1Score"
- "[SpotlightRanking] [QU] [LLM] query=%@ LLM_QU_Intent=%@ LLM_QU_Inferred_Intent=%@ detected earliest=%i latest=%i parsedQueryFromQU=[%@] parsedPersonFromQU=[%@] entityL1Score=%f hasQueryContextEmbedding=%i queryType=%@ queryTime=%f"
- "[SpotlightRanking] [SearchTool] Boosted likelihood for inferred app entity match for item=%@ %0.2f"
- "[SpotlightRanking] [SearchTool] [Demotion] query=%@ Result=[%@] identifier=[%@] multi-recipient calendar was soft demoted due to person match only in recipient field. LLM QU Intent: %@. calendarEventRecipientsEmailAddresses count=%lu"
- "[SpotlightRanking] [SearchTool] [Doc Classification] Boosted likelihood for calendar item=%@ %0.2f"
- "[SpotlightRanking] [SearchTool] [QU] query=%@ useLLMQU=%i QU_Intent=%s LLM_QU_Intent=%@ LLM_QU_Inferred_Intent=%@ earliest=%i latest=%i parsedQueryFromQU=%@"
- "[SpotlightRanking] [SearchTool] [Shared Link] query=%@ Result: %@ identifier=%@ was promoted due to QU Inferred entity match"
- "[SpotlightRanking] [SearchTool] [Shared Link] query=%@ Result: %@ identifier=%@ was promoted due to shared link type and QU Inferred entity match"
- "[SpotlightRanking] [SearchTool] qid=[%llu] query=%@ filter %d-dayss-old Mail and Messages results %@ bundle=%@ identifier=%@ MDItemIdentifier=%@ for event type and future intent mostRecentTimeToQueryInMinutesForFreshness=%ld"
- "[SpotlightRanking] [SearchTool] qid=[%llu] query=[%@] filter result [%@] bundle=%@ identifier=%@ MDItemIdentifier=%@ for topicalityScore=%f"
- "[SpotlightRanking] [SearchTool] query=%@ Filtering section %@"
- "[SpotlightRanking] [SearchTool] query=%@ Result: %@ identifier=%@ was demoted due to email Label: Promotional"
- "[SpotlightRanking] [SearchTool] query=%@ bundleId=%@ identifier=%@ MDItemIdentifier=%@ assigned default dense score %f"
- "[SpotlightRanking] [SearchTool] query=%@ qid=%llu ranked result %i: bundleId=%@ identifier=%@ MDItemIdentifier=%@ name=%@ score=(likelihood=%f topicality=%f pommesL1Score=%f pommesCalibratedL1Score=%f embeddingSimilarity=%f keywordMatchScore=%f freshness=%f engagement=%f pommesL2Score=%f) documentSignals=(detectedEventTypes=%@ isMailCategoryHighImpact=%i isMailCategoryPromotions=%i startDueDateToNowInSeconds=%ld isCalendarFlightEventType=%i isCalendarHotelEventType=%i isCalendarRestaurantEventTyp=%i isCalendarOtherReservationEventType=%i mostRecentTimeToQueryInDays=%ld) documentEmbeddingAvailable=%d"
- "[SpotlightRanking] [SearchTool] query=%@ ranked result %i: bundleId=%@ identifier=%@ MDItemIdentifier=%@ messageID=%@ messageHeader=%@ contentURL=%@ appEntityInstanceId=%@ name=%@ score=(likelihood=%f topicality=%f pommesL1Score=%f pommesCalibratedL1Score=%f embeddingSimilarity=%f keywordMatchScore=%f freshness=%f engagement=%f pommesL2Score=%f normalizedSparseScore=%f) documentSignals=(detectedEventTypes=%@ isMailCategoryHighImpact=%i isMailCategoryPromotions=%i startDueDateToNowInSeconds=%ld isCalendarFlightEventType=%i isCalendarHotelEventType=%i isCalendarRestaurantEventTyp=%i isCalendarOtherReservationEventType=%i mostRecentTimeToQueryInMinutes=%ld) topicalityAnonFeatDict=(%@) dates=(lastUsedDate=[%@] contentCreationDate=[%@] contentModificationDate=[%@] receivedDate=[%@] sentDate=[%@] startDate=[%@] endDate=[%@]) retrievalType=%i documentEmbeddingAvailable=%d"
- "_entityL1Score"
- "_estimatedMaxPommesL1Score"
- "calculateFreshnessForSearchTool:"
- "calculateLikelihoodForSearchTool:queryContext:isQUInferredIntent:"
- "entityL1Score"
- "estimatedMaxPommesL1Score"
- "logItems:prefix:queryId:query:"
- "logPommesScoringForRankingItem:queryId:query:bundleID:name:topicality:freshness:engagement:likelihood:launchPortion:launchCount:launchPortionOutOfSpotlight:launchCountOutOfSpotlight:engagedInSpotlight:exactMatchedLaunchString:lastUsedDate:recentEngagementDateInSpotlight:recentEngagementDateInApp:recentEngagementDateOutSpotlight:nominateLocalTopHit:isSearchTool:"
- "logStats:prefix:queryId:query:"
- "populateOnlyPommesL1RankingFeaturesWithQueryID:isSearchToolClient:"
- "searchToolShouldFilterResultBeforeRanking:queryContext:matchQUIntent:intentAndResultWithStartDueDate:isCleanSlate:searchToolBundles:useLLMQU:"
- "sendTTRLogsWithSections:searchString:queryKind:isCommittedSearch:parsecCameLaterThanSRT:"
- "setEntityL1Score:"
- "setEstimatedMaxPommesL1Score:"
- "updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:"
- "updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:"
- "updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:"
- "v28@0:8q16B24"
- "v48@0:8@16@24Q32B40B44"
- "v60@0:8@16B24@28d36@44B52B56"
- "v76@0:8@16@24@32q40d48B56@60B68B72"
- "v76@0:8@16@24d32B40@44@52B60@64B72"

```
