## FedStats

> `/System/Library/PrivateFrameworks/FedStats.framework/Versions/A/FedStats`

```diff

-21.0.0.0.0
-  __TEXT.__text: 0x14f40
-  __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_methlist: 0xf84
-  __TEXT.__const: 0x2f0
-  __TEXT.__cstring: 0x231c
+32.0.0.0.0
+  __TEXT.__text: 0x162f0
+  __TEXT.__auth_stubs: 0x350
+  __TEXT.__objc_methlist: 0x151c
+  __TEXT.__const: 0xd0
+  __TEXT.__cstring: 0x22db
+  __TEXT.__oslogstring: 0x34b
   __TEXT.__ustring: 0x1e
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__oslogstring: 0x211
-  __TEXT.__unwind_info: 0x358
-  __TEXT.__objc_classname: 0x4b0
-  __TEXT.__objc_methname: 0x29e3
-  __TEXT.__objc_methtype: 0x63b
-  __TEXT.__objc_stubs: 0x2440
-  __DATA_CONST.__got: 0x250
-  __DATA_CONST.__const: 0x298
-  __DATA_CONST.__objc_classlist: 0x108
+  __TEXT.__unwind_info: 0x3e8
+  __TEXT.__objc_classname: 0x5cb
+  __TEXT.__objc_methname: 0x2c7e
+  __TEXT.__objc_methtype: 0x735
+  __TEXT.__objc_stubs: 0x25e0
+  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__const: 0x278
+  __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa28
+  __DATA_CONST.__objc_selrefs: 0xb88
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xb8
+  __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x140
-  __AUTH_CONST.__auth_got: 0x180
-  __AUTH_CONST.__const: 0x110
-  __AUTH_CONST.__cfstring: 0x2140
-  __AUTH_CONST.__objc_const: 0x3fd8
-  __AUTH_CONST.__objc_intobj: 0x138
+  __AUTH_CONST.__auth_got: 0x1b8
+  __AUTH_CONST.__const: 0x130
+  __AUTH_CONST.__cfstring: 0x20c0
+  __AUTH_CONST.__objc_const: 0x4568
+  __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0xa50
-  __DATA.__objc_ivar: 0x110
-  __DATA.__data: 0x1f8
-  __DATA.__bss: 0x18
+  __AUTH.__objc_data: 0xbe0
+  __DATA.__objc_ivar: 0x128
+  __DATA.__data: 0x318
+  __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/Frameworks/NaturalLanguage.framework/Versions/A/NaturalLanguage
   - /System/Library/PrivateFrameworks/DifferentialPrivacy.framework/Versions/A/DifferentialPrivacy
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/Versions/A/ProactiveSupport
-  - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/Versions/A/RegulatoryDomain
   - /System/Library/PrivateFrameworks/SafariCore.framework/Versions/A/SafariCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 652CEC5F-0596-36A0-8EFE-FABA6440B0BD
-  Functions: 318
-  Symbols:   1193
-  CStrings:  1145
+  UUID: 9B8D5901-4882-35D0-B246-4BD4BB2179F3
+  Functions: 384
+  Symbols:   1345
+  CStrings:  1199
 
Symbols:
+ +[FedStatsDataEncoder defaultDataPointForDataTypeContent:]
+ +[FedStatsLog logger].cold.1
+ +[FedStatsUtils getDeviceRegion]
+ +[FedStatsUtils getDeviceRegion].cold.1
+ +[FedStatsUtils getDeviceRegion].cold.2
+ +[FedStatsUtils isNaturalLanguageAvailable]
+ +[FedStatsUtils tokenizeSentence:removePunctuation:tokenizePerson:tokenizeLocation:tokenizeNumber:action:]
+ +[FedStatsUtilsGammaDistribution distributionWithShape:scale:cap:]
+ +[FedStatsUtilsGammaDistribution distributionWithShape:scale:cap:].cold.1
+ +[FedStatsUtilsGammaDistribution distributionWithShape:scale:cap:].cold.2
+ +[FedStatsUtilsGammaDistribution sampleLargeWithShape:scale:unitNumberGenerator:]
+ +[FedStatsUtilsGammaDistribution sampleLargeWithShape:scale:unitNumberGenerator:].cold.1
+ +[FedStatsUtilsNegativeBinomialDistribution distributionWithSuccessCount:successProbability:]
+ +[FedStatsUtilsNegativeBinomialDistribution distributionWithSuccessCount:successProbability:].cold.1
+ +[FedStatsUtilsNegativeBinomialDistribution distributionWithSuccessCount:successProbability:].cold.2
+ -[FedStatsCategoricalTypeNgramTokenizer initWithShuffleMethod:popularWordsDB:]
+ -[FedStatsCategoricalTypeNgramTokenizer tokenize:].cold.1
+ -[FedStatsCategoricalTypeSampleTokenizer tokenize:].cold.1
+ -[FedStatsUtilsGammaDistribution .cxx_destruct]
+ -[FedStatsUtilsGammaDistribution cap]
+ -[FedStatsUtilsGammaDistribution initWithShape:scale:cap:]
+ -[FedStatsUtilsGammaDistribution mean]
+ -[FedStatsUtilsGammaDistribution sampleUncappedWithUnitNumberGenerator:]
+ -[FedStatsUtilsGammaDistribution sampleWithUnitNumberGenerator:]
+ -[FedStatsUtilsGammaDistribution sample]
+ -[FedStatsUtilsGammaDistribution scale]
+ -[FedStatsUtilsGammaDistribution setCap:]
+ -[FedStatsUtilsGammaDistribution setScale:]
+ -[FedStatsUtilsGammaDistribution setShape:]
+ -[FedStatsUtilsGammaDistribution shape]
+ -[FedStatsUtilsGammaDistribution varianceOfSecondMoment]
+ -[FedStatsUtilsGammaDistribution variance]
+ -[FedStatsUtilsNegativeBinomialDistribution .cxx_destruct]
+ -[FedStatsUtilsNegativeBinomialDistribution gamma]
+ -[FedStatsUtilsNegativeBinomialDistribution initWithSuccessCount:successProbability:]
+ -[FedStatsUtilsNegativeBinomialDistribution mean]
+ -[FedStatsUtilsNegativeBinomialDistribution sampleWithUnitNumberGenerator:]
+ -[FedStatsUtilsNegativeBinomialDistribution sample]
+ -[FedStatsUtilsNegativeBinomialDistribution setGamma:]
+ -[FedStatsUtilsNegativeBinomialDistribution setSuccessCount:]
+ -[FedStatsUtilsNegativeBinomialDistribution setSuccessProbability:]
+ -[FedStatsUtilsNegativeBinomialDistribution successCount]
+ -[FedStatsUtilsNegativeBinomialDistribution successProbability]
+ -[FedStatsUtilsNegativeBinomialDistribution varianceOfSecondMoment]
+ -[FedStatsUtilsNegativeBinomialDistribution variance]
+ -[FedStatsUtilsNormalDistribution initWithMean:]
+ -[FedStatsUtilsNormalDistribution initWithMean:standardDeviation:]
+ -[FedStatsUtilsNormalDistribution initWithStandardDeviation:]
+ -[FedStatsUtilsNormalDistribution init]
+ -[FedStatsUtilsNormalDistribution mean]
+ -[FedStatsUtilsNormalDistribution sampleWithUnitNumberGenerator:]
+ -[FedStatsUtilsNormalDistribution sample]
+ -[FedStatsUtilsNormalDistribution setMean:]
+ -[FedStatsUtilsNormalDistribution setStandardDeviation:]
+ -[FedStatsUtilsNormalDistribution standardDeviation]
+ -[FedStatsUtilsNormalDistribution varianceOfSecondMoment]
+ -[FedStatsUtilsNormalDistribution variance]
+ -[FedStatsUtilsPoissonDistribution .cxx_destruct]
+ -[FedStatsUtilsPoissonDistribution cap]
+ -[FedStatsUtilsPoissonDistribution initWithMean:]
+ -[FedStatsUtilsPoissonDistribution initWithMean:cap:]
+ -[FedStatsUtilsPoissonDistribution mean]
+ -[FedStatsUtilsPoissonDistribution sampleLargeWithUnitNumberGenerator:]
+ -[FedStatsUtilsPoissonDistribution sampleSmallWithUnitNumberGenerator:]
+ -[FedStatsUtilsPoissonDistribution sampleWithUnitNumberGenerator:]
+ -[FedStatsUtilsPoissonDistribution sample]
+ -[FedStatsUtilsPoissonDistribution setCap:]
+ -[FedStatsUtilsPoissonDistribution setMean:]
+ -[FedStatsUtilsPoissonDistribution varianceOfSecondMoment]
+ -[FedStatsUtilsPoissonDistribution variance]
+ -[FedStatsUtilsUniformUnitIntervalDistribution mean]
+ -[FedStatsUtilsUniformUnitIntervalDistribution sampleWithUnitNumberGenerator:]
+ -[FedStatsUtilsUniformUnitIntervalDistribution sample]
+ -[FedStatsUtilsUniformUnitIntervalDistribution varianceOfSecondMoment]
+ -[FedStatsUtilsUniformUnitIntervalDistribution variance]
+ OBJC_IVAR_$_FedStatsUtilsGammaDistribution._cap
+ OBJC_IVAR_$_FedStatsUtilsGammaDistribution._scale
+ OBJC_IVAR_$_FedStatsUtilsGammaDistribution._shape
+ OBJC_IVAR_$_FedStatsUtilsNegativeBinomialDistribution._gamma
+ OBJC_IVAR_$_FedStatsUtilsNegativeBinomialDistribution._successCount
+ OBJC_IVAR_$_FedStatsUtilsNegativeBinomialDistribution._successProbability
+ OBJC_IVAR_$_FedStatsUtilsNormalDistribution._mean
+ OBJC_IVAR_$_FedStatsUtilsNormalDistribution._standardDeviation
+ OBJC_IVAR_$_FedStatsUtilsPoissonDistribution._cap
+ OBJC_IVAR_$_FedStatsUtilsPoissonDistribution._mean
+ _NLLanguageEnglish
+ _NSLocaleCountryCode
+ _OBJC_CLASS_$_FedStatsUtilsGammaDistribution
+ _OBJC_CLASS_$_FedStatsUtilsNegativeBinomialDistribution
+ _OBJC_CLASS_$_FedStatsUtilsNormalDistribution
+ _OBJC_CLASS_$_FedStatsUtilsPoissonDistribution
+ _OBJC_CLASS_$_FedStatsUtilsUniformUnitIntervalDistribution
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_METACLASS_$_FedStatsUtilsGammaDistribution
+ _OBJC_METACLASS_$_FedStatsUtilsNegativeBinomialDistribution
+ _OBJC_METACLASS_$_FedStatsUtilsNormalDistribution
+ _OBJC_METACLASS_$_FedStatsUtilsPoissonDistribution
+ _OBJC_METACLASS_$_FedStatsUtilsUniformUnitIntervalDistribution
+ __OBJC_$_CLASS_METHODS_FedStatsUtilsGammaDistribution
+ __OBJC_$_CLASS_METHODS_FedStatsUtilsNegativeBinomialDistribution
+ __OBJC_$_INSTANCE_METHODS_FedStatsUtilsGammaDistribution
+ __OBJC_$_INSTANCE_METHODS_FedStatsUtilsNegativeBinomialDistribution
+ __OBJC_$_INSTANCE_METHODS_FedStatsUtilsNormalDistribution
+ __OBJC_$_INSTANCE_METHODS_FedStatsUtilsPoissonDistribution
+ __OBJC_$_INSTANCE_METHODS_FedStatsUtilsUniformUnitIntervalDistribution
+ __OBJC_$_INSTANCE_VARIABLES_FedStatsUtilsGammaDistribution
+ __OBJC_$_INSTANCE_VARIABLES_FedStatsUtilsNegativeBinomialDistribution
+ __OBJC_$_INSTANCE_VARIABLES_FedStatsUtilsNormalDistribution
+ __OBJC_$_INSTANCE_VARIABLES_FedStatsUtilsPoissonDistribution
+ __OBJC_$_PROP_LIST_FedStatsUtilsGammaDistribution
+ __OBJC_$_PROP_LIST_FedStatsUtilsNegativeBinomialDistribution
+ __OBJC_$_PROP_LIST_FedStatsUtilsNormalDistribution
+ __OBJC_$_PROP_LIST_FedStatsUtilsPoissonDistribution
+ __OBJC_$_PROP_LIST_FedStatsUtilsUniformUnitIntervalDistribution
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FedStatsUtilsBaseDistribution
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FedStatsUtilsContinuousDistribution
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FedStatsUtilsDiscreteDistribution
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FedStatsUtilsBaseDistribution
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FedStatsUtilsContinuousDistribution
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FedStatsUtilsDiscreteDistribution
+ __OBJC_$_PROTOCOL_REFS_FedStatsUtilsBaseDistribution
+ __OBJC_$_PROTOCOL_REFS_FedStatsUtilsContinuousDistribution
+ __OBJC_$_PROTOCOL_REFS_FedStatsUtilsDiscreteDistribution
+ __OBJC_CLASS_PROTOCOLS_$_FedStatsUtilsGammaDistribution
+ __OBJC_CLASS_PROTOCOLS_$_FedStatsUtilsNegativeBinomialDistribution
+ __OBJC_CLASS_PROTOCOLS_$_FedStatsUtilsNormalDistribution
+ __OBJC_CLASS_PROTOCOLS_$_FedStatsUtilsPoissonDistribution
+ __OBJC_CLASS_PROTOCOLS_$_FedStatsUtilsUniformUnitIntervalDistribution
+ __OBJC_CLASS_RO_$_FedStatsUtilsGammaDistribution
+ __OBJC_CLASS_RO_$_FedStatsUtilsNegativeBinomialDistribution
+ __OBJC_CLASS_RO_$_FedStatsUtilsNormalDistribution
+ __OBJC_CLASS_RO_$_FedStatsUtilsPoissonDistribution
+ __OBJC_CLASS_RO_$_FedStatsUtilsUniformUnitIntervalDistribution
+ __OBJC_LABEL_PROTOCOL_$_FedStatsUtilsBaseDistribution
+ __OBJC_LABEL_PROTOCOL_$_FedStatsUtilsContinuousDistribution
+ __OBJC_LABEL_PROTOCOL_$_FedStatsUtilsDiscreteDistribution
+ __OBJC_METACLASS_RO_$_FedStatsUtilsGammaDistribution
+ __OBJC_METACLASS_RO_$_FedStatsUtilsNegativeBinomialDistribution
+ __OBJC_METACLASS_RO_$_FedStatsUtilsNormalDistribution
+ __OBJC_METACLASS_RO_$_FedStatsUtilsPoissonDistribution
+ __OBJC_METACLASS_RO_$_FedStatsUtilsUniformUnitIntervalDistribution
+ __OBJC_PROTOCOL_$_FedStatsUtilsBaseDistribution
+ __OBJC_PROTOCOL_$_FedStatsUtilsContinuousDistribution
+ __OBJC_PROTOCOL_$_FedStatsUtilsDiscreteDistribution
+ ___106+[FedStatsUtils tokenizeSentence:removePunctuation:tokenizePerson:tokenizeLocation:tokenizeNumber:action:]_block_invoke
+ ___32+[FedStatsUtils getDeviceRegion]_block_invoke
+ ___81+[FedStatsUtilsGammaDistribution sampleLargeWithShape:scale:unitNumberGenerator:]_block_invoke
+ ___block_descriptor_51_e8_32s40s_e37_v40?0"NSString"8{_NSRange=QQ}16^B32l
+ __os_log_error_impl
+ _arc4random_buf
+ _cos
+ _exp
+ _kFedStatsTokenLocationEntity
+ _kFedStatsTokenNumberEntity
+ _kFedStatsTokenPersonEntity
+ _log
+ _objc_msgSend$autoupdatingCurrentLocale
+ _objc_msgSend$availableTagSchemesForUnit:language:
+ _objc_msgSend$cap
+ _objc_msgSend$distributionWithShape:scale:cap:
+ _objc_msgSend$gamma
+ _objc_msgSend$getDeviceRegion
+ _objc_msgSend$initWithMean:
+ _objc_msgSend$initWithMean:standardDeviation:
+ _objc_msgSend$initWithShape:scale:cap:
+ _objc_msgSend$initWithShuffleMethod:popularWordsDB:
+ _objc_msgSend$initWithSuccessCount:successProbability:
+ _objc_msgSend$isNaturalLanguageAvailable
+ _objc_msgSend$mean
+ _objc_msgSend$sample
+ _objc_msgSend$sampleLargeWithShape:scale:unitNumberGenerator:
+ _objc_msgSend$sampleLargeWithUnitNumberGenerator:
+ _objc_msgSend$sampleSmallWithUnitNumberGenerator:
+ _objc_msgSend$sampleUncappedWithUnitNumberGenerator:
+ _objc_msgSend$sampleWithUnitNumberGenerator:
+ _objc_msgSend$scale
+ _objc_msgSend$shape
+ _objc_msgSend$standardDeviation
+ _objc_msgSend$successCount
+ _objc_msgSend$successProbability
+ _objc_msgSend$variance
+ _objc_setProperty_nonatomic_copy
+ _pow
+ getDeviceRegion.deviceRegionCode
+ getDeviceRegion.onceToken
+ sampleLargeWithShape:scale:unitNumberGenerator:.normal
+ sampleLargeWithShape:scale:unitNumberGenerator:.onceToken
- +[FedStatsUtils checkDeviceRegionCodeRestrictionForAllowedRegions:deniedRegions:].cold.2
- +[FedStatsUtils tokenizeAndSampleUnigramFromNgram:]
- -[FedStatsCategoricalTypeNgramTokenizer initWithRemovePunctuation:shuffleMethod:popularWordsDB:tokenizePerson:tokenizeLocation:tokenizeNumber:]
- -[FedStatsCategoricalTypeNgramTokenizer removePunctuation]
- -[FedStatsCategoricalTypeNgramTokenizer tokenizeLocation]
- -[FedStatsCategoricalTypeNgramTokenizer tokenizeNumber]
- -[FedStatsCategoricalTypeNgramTokenizer tokenizePerson]
- -[FedStatsCategoricalTypeNgramTokenizer tokenizeSentence:]
- OBJC_IVAR_$_FedStatsCategoricalTypeNgramTokenizer._removePunctuation
- OBJC_IVAR_$_FedStatsCategoricalTypeNgramTokenizer._tokenizeLocation
- OBJC_IVAR_$_FedStatsCategoricalTypeNgramTokenizer._tokenizeNumber
- OBJC_IVAR_$_FedStatsCategoricalTypeNgramTokenizer._tokenizePerson
- _NLTagPunctuation
- _NLTagSentenceTerminator
- _OBJC_CLASS_$_NSMutableCharacterSet
- _OBJC_CLASS_$_RDEstimate
- ___58-[FedStatsCategoricalTypeNgramTokenizer tokenizeSentence:]_block_invoke
- ___81+[FedStatsUtils checkDeviceRegionCodeRestrictionForAllowedRegions:deniedRegions:]_block_invoke
- ___block_descriptor_56_e8_32s40s48s_e37_v40?0"NSString"8{_NSRange=QQ}16^B32l
- ___copy_helper_block_e8_32s40s48s
- ___destroy_helper_block_e8_32s40s48s
- _kFedStatsCategoricalTypeParameterRemovePunctuation
- _kFedStatsCategoricalTypeParameterTokenizeLocation
- _kFedStatsCategoricalTypeParameterTokenizeNumber
- _kFedStatsCategoricalTypeParameterTokenizePerson
- _kHuffmanLocationEntity
- _kHuffmanNumberEntity
- _kHuffmanPersonEntity
- _objc_msgSend$componentsSeparatedByCharactersInSet:
- _objc_msgSend$countryCode
- _objc_msgSend$formUnionWithCharacterSet:
- _objc_msgSend$initWithRemovePunctuation:shuffleMethod:popularWordsDB:tokenizePerson:tokenizeLocation:tokenizeNumber:
- _objc_msgSend$lastKnownEstimates
- _objc_msgSend$punctuationCharacterSet
- _objc_msgSend$removePunctuation
- _objc_msgSend$tokenizeLocation
- _objc_msgSend$tokenizeNumber
- _objc_msgSend$tokenizePerson
- _objc_msgSend$tokenizeSentence:
- _objc_msgSend$whitespaceAndNewlineCharacterSet
- checkDeviceRegionCodeRestrictionForAllowedRegions:deniedRegions:.deviceRegionCode
- checkDeviceRegionCodeRestrictionForAllowedRegions:deniedRegions:.onceToken
CStrings:
+ "@\"FedStatsUtilsGammaDistribution\""
+ "@24@0:8d16"
+ "@32@0:8d16Q24"
+ "@32@0:8d16d24"
+ "@40@0:8d16d24@32"
+ "@48@0:8@16B24B28B32B36q40"
+ "FedStatsUtilsBaseDistribution"
+ "FedStatsUtilsContinuousDistribution"
+ "FedStatsUtilsDiscreteDistribution"
+ "FedStatsUtilsGammaDistribution"
+ "FedStatsUtilsGammaDistribution: `scale` must be positive"
+ "FedStatsUtilsGammaDistribution: `shape` must be positive"
+ "FedStatsUtilsNegativeBinomialDistribution"
+ "FedStatsUtilsNegativeBinomialDistribution: `successCount` must be positive"
+ "FedStatsUtilsNegativeBinomialDistribution: `successProbability` must be in (0.0, 1.0)"
+ "FedStatsUtilsNormalDistribution"
+ "FedStatsUtilsPoissonDistribution"
+ "FedStatsUtilsUniformUnitIntervalDistribution"
+ "Ngram words: %@"
+ "Q24@0:8@\"<FedStatsUtilsContinuousDistribution>\"16"
+ "Q24@0:8@16"
+ "Sample random word: %@"
+ "T@\"FedStatsUtilsGammaDistribution\",C,N,V_gamma"
+ "T@\"NSNumber\",&,N,V_cap"
+ "T@\"NSNumber\",C,N,V_cap"
+ "Td,N,V_mean"
+ "Td,N,V_scale"
+ "Td,N,V_shape"
+ "Td,N,V_standardDeviation"
+ "Td,N,V_successCount"
+ "Td,N,V_successProbability"
+ "_cap"
+ "_gamma"
+ "_mean"
+ "_scale"
+ "_shape"
+ "_standardDeviation"
+ "_successCount"
+ "_successProbability"
+ "autoupdatingCurrentLocale"
+ "availableTagSchemesForUnit:language:"
+ "cap"
+ "d"
+ "d16@0:8"
+ "d24@0:8@\"<FedStatsUtilsContinuousDistribution>\"16"
+ "d24@0:8@16"
+ "d40@0:8d16d24@32"
+ "defaultDataPointForDataTypeContent:"
+ "distributionWithShape:scale:cap:"
+ "distributionWithSuccessCount:successProbability:"
+ "gamma"
+ "getDeviceRegion"
+ "initWithMean:"
+ "initWithMean:cap:"
+ "initWithMean:standardDeviation:"
+ "initWithShape:scale:cap:"
+ "initWithShuffleMethod:popularWordsDB:"
+ "initWithStandardDeviation:"
+ "initWithSuccessCount:successProbability:"
+ "isNaturalLanguageAvailable"
+ "mean"
+ "sample"
+ "sampleLargeWithShape:scale:unitNumberGenerator:"
+ "sampleLargeWithUnitNumberGenerator:"
+ "sampleSmallWithUnitNumberGenerator:"
+ "sampleUncappedWithUnitNumberGenerator:"
+ "sampleWithUnitNumberGenerator:"
+ "scale"
+ "setCap:"
+ "setGamma:"
+ "setMean:"
+ "setScale:"
+ "setShape:"
+ "setStandardDeviation:"
+ "setSuccessCount:"
+ "setSuccessProbability:"
+ "shape"
+ "standardDeviation"
+ "successCount"
+ "successProbability"
+ "tokenizeSentence:removePunctuation:tokenizePerson:tokenizeLocation:tokenizeNumber:action:"
+ "v24@0:8d16"
+ "variance"
+ "varianceOfSecondMoment"
- "@48@0:8B16@20@28B36B40B44"
- "TB,R,N,V_removePunctuation"
- "TB,R,N,V_tokenizeLocation"
- "TB,R,N,V_tokenizeNumber"
- "TB,R,N,V_tokenizePerson"
- "_removePunctuation"
- "_tokenizeLocation"
- "_tokenizeNumber"
- "_tokenizePerson"
- "componentsSeparatedByCharactersInSet:"
- "countryCode"
- "formUnionWithCharacterSet:"
- "initWithRemovePunctuation:shuffleMethod:popularWordsDB:tokenizePerson:tokenizeLocation:tokenizeNumber:"
- "lastKnownEstimates"
- "punctuationCharacterSet"
- "removePunctuation"
- "tokenizeAndSampleUnigramFromNgram:"
- "tokenizeLocation"
- "tokenizeNumber"
- "tokenizePerson"
- "tokenizeSentence:"
- "whitespaceAndNewlineCharacterSet"

```
