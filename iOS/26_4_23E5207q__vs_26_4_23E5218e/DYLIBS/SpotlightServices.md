## SpotlightServices

> `/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices`

```diff

-2418.4.8.2.100
-  __TEXT.__text: 0x186764
-  __TEXT.__auth_stubs: 0x1d30
-  __TEXT.__objc_methlist: 0x105e0
-  __TEXT.__const: 0x2dd8
-  __TEXT.__gcc_except_tab: 0x4c20
-  __TEXT.__cstring: 0x3a12a
-  __TEXT.__oslogstring: 0xa6fb
+2418.4.10.1.0
+  __TEXT.__text: 0x18ab00
+  __TEXT.__auth_stubs: 0x1d90
+  __TEXT.__objc_methlist: 0x109e0
+  __TEXT.__const: 0x2de8
+  __TEXT.__gcc_except_tab: 0x4d0c
+  __TEXT.__cstring: 0x3a28a
+  __TEXT.__oslogstring: 0xa79b
   __TEXT.__ustring: 0x8c2
   __TEXT.__dlopen_cstrs: 0xd1
   __TEXT.__swift5_typeref: 0x1e6

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_capture: 0x94
-  __TEXT.__unwind_info: 0x4818
-  __TEXT.__objc_classname: 0x178e
-  __TEXT.__objc_methname: 0x32cb4
-  __TEXT.__objc_methtype: 0x35a1
-  __TEXT.__objc_stubs: 0x1ee80
-  __DATA_CONST.__got: 0x2178
-  __DATA_CONST.__const: 0x10068
-  __DATA_CONST.__objc_classlist: 0x748
+  __TEXT.__unwind_info: 0x4910
+  __TEXT.__objc_classname: 0x17de
+  __TEXT.__objc_methname: 0x33228
+  __TEXT.__objc_methtype: 0x35f1
+  __TEXT.__objc_stubs: 0x1f120
+  __DATA_CONST.__got: 0x21a8
+  __DATA_CONST.__const: 0x100c8
+  __DATA_CONST.__objc_classlist: 0x770
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9a50
+  __DATA_CONST.__objc_selrefs: 0x9b88
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x5a0
+  __DATA_CONST.__objc_superrefs: 0x5c0
   __DATA_CONST.__objc_arraydata: 0x43d8
-  __AUTH_CONST.__auth_got: 0xea8
-  __AUTH_CONST.__const: 0x2c38
-  __AUTH_CONST.__cfstring: 0x35a20
-  __AUTH_CONST.__objc_const: 0x1ac88
+  __AUTH_CONST.__auth_got: 0xed8
+  __AUTH_CONST.__const: 0x2c78
+  __AUTH_CONST.__cfstring: 0x35ba0
+  __AUTH_CONST.__objc_const: 0x1b2d8
   __AUTH_CONST.__objc_intobj: 0x4680
   __AUTH_CONST.__objc_arrayobj: 0xc60
   __AUTH_CONST.__objc_doubleobj: 0x320
   __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH.__objc_data: 0x2728
+  __AUTH.__objc_data: 0x28b8
   __AUTH.__data: 0x118
-  __DATA.__objc_ivar: 0x1780
+  __DATA.__objc_ivar: 0x17b4
   __DATA.__data: 0x12a8
-  __DATA.__bss: 0xe58
+  __DATA.__bss: 0xe68
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x23f0
   __DATA_DIRTY.__data: 0x298

   - /System/Library/PrivateFrameworks/DataDetectorsCore.framework/DataDetectorsCore
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement
+  - /System/Library/PrivateFrameworks/FeatureStore.framework/FeatureStore
   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation

   - /System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities
   - /System/Library/PrivateFrameworks/PersonalizationPortrait.framework/PersonalizationPortrait
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
+  - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/QueryParser.framework/QueryParser
   - /System/Library/PrivateFrameworks/QueryUnderstanding.framework/QueryUnderstanding
   - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1719F16D-3ADC-3EF6-B3AA-42CA39F70A0D
-  Functions: 7008
-  Symbols:   24169
-  CStrings:  22910
+  UUID: 09FB4CB4-4055-3B3B-A35A-0CBC8E258713
+  Functions: 7099
+  Symbols:   24433
+  CStrings:  23012
 
Symbols:
+ +[FeatureStoreLogger insertPQARankerResultWithItem:item:]
+ +[PQAResultList resultsType]
+ +[SSSearchToolRankingSignals keywordMatchScoreFromMatchInfoAttribute:targetQUTokenSet:]
+ -[Bucket initWithItem:isPerfectScoreBucket:queryContext:]
+ -[Bucket isDefaultTemporal]
+ -[Bucket setIsDefaultTemporal:]
+ -[PQARankerResults .cxx_destruct]
+ -[PQARankerResults copyTo:]
+ -[PQARankerResults copyWithZone:]
+ -[PQARankerResults description]
+ -[PQARankerResults dictionaryRepresentation]
+ -[PQARankerResults filteredResults]
+ -[PQARankerResults hasFilteredResults]
+ -[PQARankerResults hasRankedResults]
+ -[PQARankerResults hasRequestIdentifier]
+ -[PQARankerResults hasRetrievedResults]
+ -[PQARankerResults hash]
+ -[PQARankerResults isEqual:]
+ -[PQARankerResults mergeFrom:]
+ -[PQARankerResults rankedResults]
+ -[PQARankerResults readFrom:]
+ -[PQARankerResults requestIdentifier]
+ -[PQARankerResults retrievedResults]
+ -[PQARankerResults setFilteredResults:]
+ -[PQARankerResults setRankedResults:]
+ -[PQARankerResults setRequestIdentifier:]
+ -[PQARankerResults setRetrievedResults:]
+ -[PQARankerResults writeTo:]
+ -[PQARequestIdentifiers .cxx_destruct]
+ -[PQARequestIdentifiers copyTo:]
+ -[PQARequestIdentifiers copyWithZone:]
+ -[PQARequestIdentifiers description]
+ -[PQARequestIdentifiers dictionaryRepresentation]
+ -[PQARequestIdentifiers hasQueryEventId]
+ -[PQARequestIdentifiers hasSessionId]
+ -[PQARequestIdentifiers hasUserTurnId]
+ -[PQARequestIdentifiers hash]
+ -[PQARequestIdentifiers isEqual:]
+ -[PQARequestIdentifiers mergeFrom:]
+ -[PQARequestIdentifiers queryEventId]
+ -[PQARequestIdentifiers readFrom:]
+ -[PQARequestIdentifiers sessionId]
+ -[PQARequestIdentifiers setQueryEventId:]
+ -[PQARequestIdentifiers setSessionId:]
+ -[PQARequestIdentifiers setUserTurnId:]
+ -[PQARequestIdentifiers userTurnId]
+ -[PQARequestIdentifiers writeTo:]
+ -[PQAResult .cxx_destruct]
+ -[PQAResult bundleId]
+ -[PQAResult copyTo:]
+ -[PQAResult copyWithZone:]
+ -[PQAResult description]
+ -[PQAResult dictionaryRepresentation]
+ -[PQAResult hash]
+ -[PQAResult isEqual:]
+ -[PQAResult mergeFrom:]
+ -[PQAResult readFrom:]
+ -[PQAResult resultId]
+ -[PQAResult setBundleId:]
+ -[PQAResult setResultId:]
+ -[PQAResult writeTo:]
+ -[PQAResult writeTo:].cold.1
+ -[PQAResult writeTo:].cold.2
+ -[PQAResultList .cxx_destruct]
+ -[PQAResultList addResults:]
+ -[PQAResultList clearResults]
+ -[PQAResultList copyTo:]
+ -[PQAResultList copyWithZone:]
+ -[PQAResultList description]
+ -[PQAResultList dictionaryRepresentation]
+ -[PQAResultList hash]
+ -[PQAResultList isEqual:]
+ -[PQAResultList mergeFrom:]
+ -[PQAResultList readFrom:]
+ -[PQAResultList resultsAtIndex:]
+ -[PQAResultList resultsCount]
+ -[PQAResultList results]
+ -[PQAResultList setResults:]
+ -[PQAResultList writeTo:]
+ -[SPSearchQueryContext maxSearchToolResultsCountPerBundle]
+ -[SPSearchQueryContext pqaRequestIdentifiers]
+ -[SPSearchQueryContext setMaxSearchToolResultsCountPerBundle:]
+ -[SPSearchQueryContext setPqaRequestIdentifiers:]
+ -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:maxCount:]
+ -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:maxCount:].cold.1
+ -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:maxCount:].cold.2
+ -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:maxCount:].cold.3
+ -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:maxCount:].cold.4
+ -[SSPommesPhotosRanker updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:isDocumentSearch:maxCount:]
+ -[SSPommesRanker updateScoresForItems:withSectionBundle:userQuery:queryID:mailQueryID:mailSessionID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:isDocumentSearch:maxCount:]
+ OBJC_IVAR_$_PQARankerResults._filteredResults
+ OBJC_IVAR_$_PQARankerResults._rankedResults
+ OBJC_IVAR_$_PQARankerResults._requestIdentifier
+ OBJC_IVAR_$_PQARankerResults._retrievedResults
+ OBJC_IVAR_$_PQARequestIdentifiers._queryEventId
+ OBJC_IVAR_$_PQARequestIdentifiers._sessionId
+ OBJC_IVAR_$_PQARequestIdentifiers._userTurnId
+ OBJC_IVAR_$_PQAResult._bundleId
+ OBJC_IVAR_$_PQAResult._resultId
+ OBJC_IVAR_$_PQAResultList._results
+ _OBJC_CLASS_$_FSFFeatureStoreService
+ _OBJC_CLASS_$_FeatureStoreLogger
+ _OBJC_CLASS_$_PBCodable
+ _OBJC_CLASS_$_PQARankerResults
+ _OBJC_CLASS_$_PQARequestIdentifiers
+ _OBJC_CLASS_$_PQAResult
+ _OBJC_CLASS_$_PQAResultList
+ _OBJC_IVAR_$_Bucket._isDefaultTemporal
+ _OBJC_IVAR_$_SPSearchQueryContext._maxSearchToolResultsCountPerBundle
+ _OBJC_IVAR_$_SPSearchQueryContext._pqaRequestIdentifiers
+ _OBJC_METACLASS_$_FeatureStoreLogger
+ _OBJC_METACLASS_$_PBCodable
+ _OBJC_METACLASS_$_PQARankerResults
+ _OBJC_METACLASS_$_PQARequestIdentifiers
+ _OBJC_METACLASS_$_PQAResult
+ _OBJC_METACLASS_$_PQAResultList
+ _PBDataWriterWriteStringField
+ _PBDataWriterWriteSubmessage
+ _PBReaderPlaceMark
+ _PBReaderReadString
+ _PBReaderRecallMark
+ _PBReaderSkipValueWithTag
+ _PQARankerResultsReadFrom
+ _PQARequestIdentifiersReadFrom
+ _PQAResultListReadFrom
+ _PQAResultReadFrom
+ _SSEnableSearchToolPQAPlus
+ _SSEnableSearchToolPQAPlus.cold.1
+ _SSEnableSearchToolPQAPlus.enabled
+ _SSEnableSearchToolPQAPlus.onceToken
+ __OBJC_$_CLASS_METHODS_FeatureStoreLogger
+ __OBJC_$_CLASS_METHODS_PQAResultList
+ __OBJC_$_INSTANCE_METHODS_PQARankerResults
+ __OBJC_$_INSTANCE_METHODS_PQARequestIdentifiers
+ __OBJC_$_INSTANCE_METHODS_PQAResult
+ __OBJC_$_INSTANCE_METHODS_PQAResultList
+ __OBJC_$_INSTANCE_VARIABLES_PQARankerResults
+ __OBJC_$_INSTANCE_VARIABLES_PQARequestIdentifiers
+ __OBJC_$_INSTANCE_VARIABLES_PQAResult
+ __OBJC_$_INSTANCE_VARIABLES_PQAResultList
+ __OBJC_$_PROP_LIST_PQARankerResults
+ __OBJC_$_PROP_LIST_PQARequestIdentifiers
+ __OBJC_$_PROP_LIST_PQAResult
+ __OBJC_$_PROP_LIST_PQAResultList
+ __OBJC_CLASS_PROTOCOLS_$_PQARankerResults
+ __OBJC_CLASS_PROTOCOLS_$_PQARequestIdentifiers
+ __OBJC_CLASS_PROTOCOLS_$_PQAResult
+ __OBJC_CLASS_PROTOCOLS_$_PQAResultList
+ __OBJC_CLASS_RO_$_FeatureStoreLogger
+ __OBJC_CLASS_RO_$_PQARankerResults
+ __OBJC_CLASS_RO_$_PQARequestIdentifiers
+ __OBJC_CLASS_RO_$_PQAResult
+ __OBJC_CLASS_RO_$_PQAResultList
+ __OBJC_METACLASS_RO_$_FeatureStoreLogger
+ __OBJC_METACLASS_RO_$_PQARankerResults
+ __OBJC_METACLASS_RO_$_PQARequestIdentifiers
+ __OBJC_METACLASS_RO_$_PQAResult
+ __OBJC_METACLASS_RO_$_PQAResultList
+ ___131+[SSSearchToolRankingManager calculateLikelihoodForResults:queryContext:isQUInferredIntent:isEventSearchIntent:rankByL2ModelScore:]_block_invoke_2
+ ___195-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:maxCount:]_block_invoke
+ ___195-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:maxCount:]_block_invoke_2
+ ___195-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:maxCount:]_block_invoke_3
+ ___195-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:maxCount:]_block_invoke_4
+ ___195-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:maxCount:]_block_invoke_5
+ ___195-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:maxCount:]_block_invoke_6
+ ___55+[SSSearchToolRankingManager rankSection:queryContext:]_block_invoke.509
+ ___55+[SSSearchToolRankingManager rankSection:queryContext:]_block_invoke.511
+ ___SSEnableSearchToolPQAPlus_block_invoke
+ ___block_descriptor_32_e39_q24?0"NSDictionary"8"NSDictionary"16l
+ ___block_descriptor_41_e8_32s_e41_v32?0"NSNumber"8"NSMutableArray"16^B24ls32l8
+ ___block_literal_global.150
+ ___block_literal_global.154
+ ___block_literal_global.163
+ ___block_literal_global.167
+ ___block_literal_global.168
+ ___block_literal_global.177
+ ___block_literal_global.182
+ ___block_literal_global.187
+ ___block_literal_global.192
+ ___block_literal_global.197
+ ___block_literal_global.214
+ ___block_literal_global.275
+ ___block_literal_global.289
+ ___block_literal_global.292
+ ___block_literal_global.392
+ ___block_literal_global.485
+ ___block_literal_global.576
+ ___block_literal_global.607
+ ___block_literal_global.613
+ ___loadRankingParameters_block_invoke.602
+ ___populateMailRankerBiomeEvent_block_invoke
+ _objc_msgSend$_setError
+ _objc_msgSend$data
+ _objc_msgSend$filteredResults
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$initWithItem:isPerfectScoreBucket:queryContext:
+ _objc_msgSend$insertPBCodableWithInteractionId:item:
+ _objc_msgSend$insertPQARankerResultWithItem:item:
+ _objc_msgSend$keywordMatchScoreFromMatchInfoAttribute:targetQUTokenSet:
+ _objc_msgSend$maxSearchToolResultsCountPerBundle
+ _objc_msgSend$mergeFrom:
+ _objc_msgSend$pqaRequestIdentifiers
+ _objc_msgSend$rankedResults
+ _objc_msgSend$retrievedResults
+ _objc_msgSend$sessionId
+ _objc_msgSend$setFilteredResults:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setQueryEventId:
+ _objc_msgSend$setRankedResults:
+ _objc_msgSend$setResultId:
+ _objc_msgSend$setRetrievedResults:
+ _objc_msgSend$setSessionId:
+ _objc_msgSend$setUserTurnId:
+ _objc_msgSend$updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:maxCount:
+ _objc_msgSend$updateScoresForItems:withSectionBundle:userQuery:queryID:mailQueryID:mailSessionID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:isDocumentSearch:maxCount:
- -[Bucket initWithItem:isPerfectScoreBucket:]
- -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:]
- -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:].cold.1
- -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:].cold.2
- -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:].cold.3
- -[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:].cold.4
- -[SSPommesPhotosRanker updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:isDocumentSearch:]
- -[SSPommesRanker updateScoresForItems:withSectionBundle:userQuery:queryID:mailSessionID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:isDocumentSearch:]
- GCC_except_table12
- GCC_except_table48
- ___186-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:]_block_invoke
- ___186-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:]_block_invoke_2
- ___186-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:]_block_invoke_3
- ___186-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:]_block_invoke_4
- ___186-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:]_block_invoke_5
- ___186-[SSPommesPhotosRanker updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:]_block_invoke_6
- ___55+[SSSearchToolRankingManager rankSection:queryContext:]_block_invoke.497
- ___55+[SSSearchToolRankingManager rankSection:queryContext:]_block_invoke.498
- ___block_literal_global.151
- ___block_literal_global.160
- ___block_literal_global.164
- ___block_literal_global.179
- ___block_literal_global.189
- ___block_literal_global.194
- ___block_literal_global.199
- ___block_literal_global.270
- ___block_literal_global.283
- ___block_literal_global.286
- ___block_literal_global.386
- ___block_literal_global.475
- ___block_literal_global.563
- ___block_literal_global.600
- ___loadRankingParameters_block_invoke.589
- _objc_msgSend$initWithItem:isPerfectScoreBucket:
- _objc_msgSend$isFinished
- _objc_msgSend$updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:
- _objc_msgSend$updateScoresForItems:withSectionBundle:userQuery:queryID:mailSessionID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:isDocumentSearch:
CStrings:
+ "-[PQAResult writeTo:]"
+ "@\"PQARequestIdentifiers\""
+ "@\"PQAResultList\""
+ "@36@0:8@16B24@28"
+ "FeatureStoreLogger"
+ "PQARankerResults"
+ "PQARequestIdentifiers"
+ "PQAResult"
+ "PQAResult.m"
+ "PQAResultList"
+ "Search term and person term match with ID attributes"
+ "Search term and person term match with OCR"
+ "SearchToolPQAPlus"
+ "T@\"NSMutableArray\",&,N,V_results"
+ "T@\"NSString\",&,N,V_queryEventId"
+ "T@\"NSString\",&,N,V_resultId"
+ "T@\"NSString\",&,N,V_sessionId"
+ "T@\"NSString\",&,N,V_userTurnId"
+ "T@\"PQARequestIdentifiers\",&,N,V_requestIdentifier"
+ "T@\"PQARequestIdentifiers\",&,V_pqaRequestIdentifiers"
+ "T@\"PQAResultList\",&,N,V_filteredResults"
+ "T@\"PQAResultList\",&,N,V_rankedResults"
+ "T@\"PQAResultList\",&,N,V_retrievedResults"
+ "TB,N,V_isDefaultTemporal"
+ "Tq,N,V_maxSearchToolResultsCountPerBundle"
+ "[SpotlightRanking] [SearchTool] [Demotion] query=%@ Result=[%@] identifier=[%@] was demoted due to freshness topicalityScore=%f likelihood=%f mostRecentTimeToQueryInMinutesForFreshness=%ld"
+ "[SpotlightRanking] [SearchTool] query=%@ output result: bundleID=%@ identifier=%@ MDItemIdentifier=%@ name=%@ likelihood=%f detectedEventTypes=%@ cardType=%@ linkType=%@ PQA+"
+ "[SpotlightRanking] [SearchTool] query=%@ qid=%llu ranked result %i: bundleId=%@ identifier=%@ MDItemIdentifier=%@ name=%@ score=(likelihood=%f topicality=%f pommesL1Score=%f pommesCalibratedL1Score=%f embeddingSimilarity=%f projectedEmbeddingSimilarity=%f keywordMatchScore=%f freshness=%f engagement=%f pommesL2Score=%f searchToolL2Score=%f) documentSignals=(detectedEventTypes=%@ cardType=%@ link=(type=%@ name=%@ url=%@ isInferred=%i isPromoted=%i) isMailCategoryHighImpact=%i isMailCategoryPromotions=%i startDueDateToNowInSeconds=%ld mostRecentTimeToQueryInDays=%ld) documentEmbeddingAvailable=%d searchTermsMatchTitle=%@, matchInfo=%@"
+ "[biome][mailQid=%lu] Donated BMMailRankerEvent to stream with session=%@, %lu results, semantic_eligible=%d, semantic_triggered=%d, top_hits=%lu/%lu"
+ "_filteredResults"
+ "_isDefaultTemporal"
+ "_maxSearchToolResultsCountPerBundle"
+ "_pqaRequestIdentifiers"
+ "_queryEventId"
+ "_rankedResults"
+ "_resultId"
+ "_results"
+ "_retrievedResults"
+ "_sessionId"
+ "_setError"
+ "_userTurnId"
+ "copyTo:"
+ "filteredResults"
+ "filtered_results"
+ "getBytes:range:"
+ "hasError"
+ "hasFilteredResults"
+ "hasQueryEventId"
+ "hasRankedResults"
+ "hasRequestIdentifier"
+ "hasRetrievedResults"
+ "hasSessionId"
+ "hasUserTurnId"
+ "initWithItem:isPerfectScoreBucket:queryContext:"
+ "insertPBCodableWithInteractionId:item:"
+ "insertPQARankerResultWithItem:item:"
+ "isDefaultTemporal"
+ "item"
+ "keywordMatchScoreFromMatchInfoAttribute:targetQUTokenSet:"
+ "maxSearchToolResultsCountPerBundle"
+ "mergeFrom:"
+ "nil != self->_bundleId"
+ "nil != self->_resultId"
+ "originalIndex"
+ "pqaRequestIdentifiers"
+ "q24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
+ "queryEventId"
+ "query_event_id"
+ "rankedResults"
+ "ranked_results"
+ "readFrom:"
+ "request_identifier"
+ "resultId"
+ "result_id"
+ "resultsType"
+ "retrievedResults"
+ "retrieved_results"
+ "sessionId"
+ "session_id"
+ "setFilteredResults:"
+ "setIsDefaultTemporal:"
+ "setMaxSearchToolResultsCountPerBundle:"
+ "setPqaRequestIdentifiers:"
+ "setQueryEventId:"
+ "setRankedResults:"
+ "setResultId:"
+ "setRetrievedResults:"
+ "setSessionId:"
+ "setUserTurnId:"
+ "updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:maxCount:"
+ "updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:isDocumentSearch:maxCount:"
+ "updateScoresForItems:withSectionBundle:userQuery:queryID:mailQueryID:mailSessionID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:isDocumentSearch:maxCount:"
+ "userTurnId"
+ "user_turn_id"
+ "v104@0:8@16@24@32q40q48@56d64B72@76B84B88B92q96"
+ "v32@?0@\"NSNumber\"8@\"NSMutableArray\"16^B24"
+ "v88@0:8@16@24@32q40d48B56@60B68B72B76q80"
+ "v88@0:8@16@24d32B40@44@52B60@64B72B76q80"
+ "writeTo:"
- "Search term and person term match with ID attributes or OCR text"
- "[SpotlightRanking] [SearchTool] [Boosting] Boosted wallet for matched detectedEvent=%@ item=%@ likelihhod=%0.2f"
- "[SpotlightRanking] [SearchTool] query=%@ qid=%llu ranked result %i: bundleId=%@ identifier=%@ MDItemIdentifier=%@ name=%@ score=(likelihood=%f topicality=%f pommesL1Score=%f pommesCalibratedL1Score=%f embeddingSimilarity=%f projectedEmbeddingSimilarity=%f keywordMatchScore=%f freshness=%f engagement=%f pommesL2Score=%f searchToolL2Score=%f) documentSignals=(detectedEventTypes=%@ cardType=%@ link=(type=%@ name=%@ url=%@ isInferred=%i isPromoted=%i) isMailCategoryHighImpact=%i isMailCategoryPromotions=%i startDueDateToNowInSeconds=%ld isCalendarFlightEventType=%i isCalendarHotelEventType=%i isCalendarRestaurantEventTyp=%i isCalendarOtherReservationEventType=%i mostRecentTimeToQueryInDays=%ld) documentEmbeddingAvailable=%d searchTermsMatchTitle=%@"
- "[biome][qid=%lu] Donated BMMailRankerEvent to stream with session=%@, %lu results, semantic_eligible=%d, semantic_triggered=%d"
- "initWithItem:isPerfectScoreBucket:"
- "updatePhotosRankingItemScore:userQuery:currentTime:collectL2Signals:keyboardLanguage:uniqueSessionID:onlyEmbeddingResults:amlInputs:isCardSearch:isDocumentSearch:"
- "updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:isDocumentSearch:"
- "updateScoresForItems:withSectionBundle:userQuery:queryID:mailSessionID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:isDocumentSearch:"
- "v80@0:8@16@24@32q40d48B56@60B68B72B76"
- "v80@0:8@16@24d32B40@44@52B60@64B72B76"
- "v88@0:8@16@24@32q40@48d56B64@68B76B80B84"

```
