## PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

-205.0.1.0.0
-  __TEXT.__text: 0x67e50
-  __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_stubs: 0xaba0
-  __TEXT.__objc_methlist: 0x6a64
+206.0.5.0.0
+  __TEXT.__text: 0x68b70
+  __TEXT.__auth_stubs: 0x8d0
+  __TEXT.__objc_stubs: 0xac00
+  __TEXT.__objc_methlist: 0x6c70
   __TEXT.__objc_classname: 0x825
-  __TEXT.__objc_methtype: 0xfbc
-  __TEXT.__cstring: 0xaf68
-  __TEXT.__objc_methname: 0x118e0
+  __TEXT.__objc_methtype: 0xfd3
+  __TEXT.__cstring: 0xb572
+  __TEXT.__objc_methname: 0x119bb
   __TEXT.__const: 0x498
   __TEXT.__gcc_except_tab: 0xbe0
-  __TEXT.__oslogstring: 0x6d60
+  __TEXT.__oslogstring: 0x6d58
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1168
-  __DATA_CONST.__auth_got: 0x478
-  __DATA_CONST.__got: 0x520
+  __TEXT.__unwind_info: 0x1170
+  __DATA_CONST.__auth_got: 0x480
+  __DATA_CONST.__got: 0x538
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2ea8
-  __DATA_CONST.__cfstring: 0xe5e0
+  __DATA_CONST.__const: 0x2e98
+  __DATA_CONST.__cfstring: 0xe960
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_floatobj: 0x1b0
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xbcd0
-  __DATA.__objc_selrefs: 0x36d0
-  __DATA.__objc_ivar: 0x918
+  __DATA.__objc_const: 0xba60
+  __DATA.__objc_selrefs: 0x3770
+  __DATA.__objc_ivar: 0x924
   __DATA.__objc_data: 0x1c70
   __DATA.__data: 0x4c0
   __DATA.__bss: 0x40

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  Functions: 2477
-  Symbols:   18793
-  CStrings:  5493
+  Functions: 2474
+  Symbols:   18837
+  CStrings:  5532
 
Symbols:
+ +[MOEventBundleRanking defineClassCollections].cold.1
+ +[MOEventPortrait defineClassCollections].cold.1
+ +[MOPlatformInfo isIpad].cold.1
+ -[MOContextMusicMetaData artist]
+ -[MOContextMusicMetaData setArtist:]
+ -[MOContextMusicMetaData setTitle:]
+ -[MOContextMusicMetaData title]
+ -[MOEventBundleRankingInput pCountMaxNormalized]
+ -[MOEventBundleRankingInput pCountWeightedAverageNormalized]
+ -[MOEventBundleRankingInput pCountWeightedSumNormalized]
+ -[MOEventBundleRankingInput setPCountMaxNormalized:]
+ -[MOEventBundleRankingInput setPCountWeightedAverageNormalized:]
+ -[MOEventBundleRankingInput setPCountWeightedSumNormalized:]
+ -[MOEventRoutine fallbackToAddressFormattingWithFormatOption:preferredCategories:poiCategoryBlocklist:mediumConfidenceThreshold:aoiConfidenceThreshold:]
+ -[MOPerson givenName]
+ -[MOPerson setGivenName:]
+ -[MOTemplateBasedContextBuilder musicMetaDataWithArtistSongForBundleContent:]
+ -[MOTemplateBasedContextBuilder musicMetaDataWithMoodForBundleContent:]
+ OBJC_IVAR_$_MOContextMusicMetaData._artist
+ OBJC_IVAR_$_MOContextMusicMetaData._title
+ OBJC_IVAR_$_MOEventBundleRankingInput._pCountMaxNormalized
+ OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedAverageNormalized
+ OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedSumNormalized
+ OBJC_IVAR_$_MOPerson._givenName
+ _OBJC_CLASS_$_NSAssertionHandler
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1180
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1182
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1182.cold.1
+ __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.1388
+ __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.135
+ __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.135.cold.1
+ __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.138
+ __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.138.cold.1
+ __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.141
+ __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.141.cold.1
+ __62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke.943
+ __63-[MOContextManager _generateContextWithOption:request:handler:]_block_invoke.115
+ __67-[MOContextManager _fetchStoredContextsWithOption:request:handler:]_block_invoke.128
+ __67-[MOContextManager _fetchStoredContextsWithOption:request:handler:]_block_invoke.128.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1126
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1132
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1133
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1137
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1168
+ __block_literal_global.134
+ __block_literal_global.137
+ __block_literal_global.140
+ __block_literal_global.143
+ __block_literal_global.146
+ __block_literal_global.1508
+ _kMOKeyPersonGivenName
+ _objc_msgSend$areaOfInterests
+ _objc_msgSend$artist
+ _objc_msgSend$currentHandler
+ _objc_msgSend$givenName
+ _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
+ _objc_msgSend$musicMetaDataWithArtistSongForBundleContent:
+ _objc_msgSend$musicMetaDataWithMoodForBundleContent:
+ _objc_msgSend$pCountMaxNormalized
+ _objc_msgSend$pCountWeightedAverageNormalized
+ _objc_msgSend$pCountWeightedSumNormalized
+ _objc_msgSend$setArtist:
+ _objc_msgSend$setGivenName:
+ _objc_msgSend$setPCountMaxNormalized:
+ _objc_msgSend$setPCountWeightedAverageNormalized:
+ _objc_msgSend$setPCountWeightedSumNormalized:
+ _objc_msgSend$structuredAddress
+ _objc_retainAutoreleasedReturnValue
- -[MOEventBundleRankingInput peopleCountMaxNormalized]
- -[MOEventBundleRankingInput peopleCountWeightedAverageNormalized]
- -[MOEventBundleRankingInput peopleCountWeightedSumNormalized]
- -[MOEventBundleRankingInput setPeopleCountMaxNormalized:]
- -[MOEventBundleRankingInput setPeopleCountWeightedAverageNormalized:]
- -[MOEventBundleRankingInput setPeopleCountWeightedSumNormalized:]
- -[MOEventRoutine formatAddressCurrentFormatWithFallback:]
- -[MOEventRoutine formatAdministrativeAreaWithFormatOption:].cold.1
- -[MOTemplateBasedContextBuilder musicMoodStringsForBundleContent:]
- -[MOTemplateBasedContextBuilder songTitleAndArtistStringsForBundleContent:]
- OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountMaxNormalized
- OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedAverageNormalized
- OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedSumNormalized
- _OUTLINED_FUNCTION_11
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1155
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1157
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1157.cold.1
- __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.1379
- __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.130
- __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.130.cold.1
- __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.133
- __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.133.cold.1
- __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.136
- __50-[MOContextManager _storeNewContexts:withRequest:]_block_invoke.136.cold.1
- __62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke.937
- __63-[MOContextManager _generateContextWithOption:request:handler:]_block_invoke.109
- __67-[MOContextManager _fetchStoredContextsWithOption:request:handler:]_block_invoke.123
- __67-[MOContextManager _fetchStoredContextsWithOption:request:handler:]_block_invoke.123.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1107
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1113
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1114
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1118
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1143
- __block_literal_global.129
- __block_literal_global.132
- __block_literal_global.135
- __block_literal_global.138
- __block_literal_global.141
- __block_literal_global.1499
- _kMOAddressFormatOptionCurrentFormat
- _kMOAddressFormatOptionCurrentFormatCountryCode
- _kMOAddressFormatOptionCurrentFormatDisplayLanguage
- _objc_msgSend$country
- _objc_msgSend$countryCode
- _objc_msgSend$formatAddressCurrentFormatWithFallback:
- _objc_msgSend$getPreferredName
- _objc_msgSend$locality
- _objc_msgSend$musicMoodStringsForBundleContent:
- _objc_msgSend$peopleCountMaxNormalized
- _objc_msgSend$peopleCountWeightedAverageNormalized
- _objc_msgSend$peopleCountWeightedSumNormalized
- _objc_msgSend$setPeopleCountMaxNormalized:
- _objc_msgSend$setPeopleCountWeightedAverageNormalized:
- _objc_msgSend$setPeopleCountWeightedSumNormalized:
- _objc_msgSend$songTitleAndArtistStringsForBundleContent:
CStrings:
+ "\x161"
+ "%@, format option, %@, output string, %@, AOI List, %@"
+ "B56@0:8@16@24@32d40d48"
+ "T@\"NSString\",&,N,V_artist"
+ "T@\"NSString\",&,N,V_givenName"
+ "Tf,N,V_pCountMaxNormalized"
+ "Tf,N,V_pCountWeightedAverageNormalized"
+ "Tf,N,V_pCountWeightedSumNormalized"
+ "_artist"
+ "_givenName"
+ "_pCountMaxNormalized"
+ "_pCountWeightedAverageNormalized"
+ "_pCountWeightedSumNormalized"
+ "add music metadata based on artist and song: %@"
+ "add music metadata based on artist only: %@"
+ "add music metadata based on artist: %@"
+ "add music metadata based on mood: %@"
+ "add music metadata based on song: %@"
+ "areaOfInterests"
+ "artist"
+ "currentHandler"
+ "fallbackToAddressFormattingWithFormatOption:preferredCategories:poiCategoryBlocklist:mediumConfidenceThreshold:aoiConfidenceThreshold:"
+ "givenName"
+ "handleFailureInMethod:object:file:lineNumber:description:"
+ "music string, %@, artist, %@, title, %@"
+ "musicMetaDataWithArtistSongForBundleContent:"
+ "musicMetaDataWithMoodForBundleContent:"
+ "setArtist:"
+ "setGivenName:"
+ "setPCountMaxNormalized:"
+ "setPCountWeightedAverageNormalized:"
+ "setPCountWeightedSumNormalized:"
+ "structuredAddress"
- "\x151"
- "%@, country code, %@, using current format output string, %@"
- "%@, country code, %@, using parking display name output string, %@, fallback, %i"
- "%@, short address format doesn't support the administrative area (state), option, %@, will use default"
- "PlatformInfoOverrideIsSeedBuild"
- "Tf,N,V_peopleCountMaxNormalized"
- "Tf,N,V_peopleCountWeightedAverageNormalized"
- "Tf,N,V_peopleCountWeightedSumNormalized"
- "US"
- "_peopleCountMaxNormalized"
- "_peopleCountWeightedAverageNormalized"
- "_peopleCountWeightedSumNormalized"
- "add music metadata: %@"
- "country"
- "countryCode"
- "currentFormat"
- "formatAddressCurrentFormatWithFallback:"
- "getPreferredName"
- "locality"
- "music string, %@"
- "musicMoodStringsForBundleContent:"
- "peopleCountMaxNormalized"
- "peopleCountWeightedAverageNormalized"
- "peopleCountWeightedSumNormalized"
- "setPeopleCountMaxNormalized:"
- "setPeopleCountWeightedAverageNormalized:"
- "setPeopleCountWeightedSumNormalized:"
- "songTitleAndArtistStringsForBundleContent:"

```
