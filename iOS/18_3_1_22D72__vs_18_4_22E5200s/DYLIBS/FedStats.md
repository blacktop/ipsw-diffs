## FedStats

> `/System/Library/PrivateFrameworks/FedStats.framework/FedStats`

```diff

-21.0.0.0.0
-  __TEXT.__text: 0x12cf0
-  __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_methlist: 0xf84
-  __TEXT.__const: 0x2f0
-  __TEXT.__cstring: 0x231c
+27.0.0.0.0
+  __TEXT.__text: 0x13b18
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__objc_methlist: 0x1414
+  __TEXT.__const: 0xc0
+  __TEXT.__cstring: 0x22db
+  __TEXT.__oslogstring: 0x34b
   __TEXT.__ustring: 0x1e
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__oslogstring: 0x211
-  __TEXT.__unwind_info: 0x350
-  __TEXT.__objc_classname: 0x4b0
-  __TEXT.__objc_methname: 0x29e3
-  __TEXT.__objc_methtype: 0x63b
-  __TEXT.__objc_stubs: 0x2440
-  __DATA_CONST.__got: 0x250
-  __DATA_CONST.__const: 0x310
-  __DATA_CONST.__objc_classlist: 0x108
+  __TEXT.__unwind_info: 0x3c8
+  __TEXT.__objc_classname: 0x5ad
+  __TEXT.__objc_methname: 0x2be1
+  __TEXT.__objc_methtype: 0x6b8
+  __TEXT.__objc_stubs: 0x25a0
+  __DATA_CONST.__got: 0x260
+  __DATA_CONST.__const: 0x2f0
+  __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa28
+  __DATA_CONST.__objc_selrefs: 0xb78
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xb8
+  __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x140
-  __AUTH_CONST.__auth_got: 0x260
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x2140
-  __AUTH_CONST.__objc_const: 0x3fd8
-  __AUTH_CONST.__objc_intobj: 0x138
+  __AUTH_CONST.__auth_got: 0x298
+  __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__cfstring: 0x20c0
+  __AUTH_CONST.__objc_const: 0x4518
+  __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0xa50
-  __DATA.__objc_ivar: 0x110
-  __DATA.__data: 0x1f8
-  __DATA.__bss: 0x18
+  __AUTH.__objc_data: 0xbe0
+  __DATA.__objc_ivar: 0x128
+  __DATA.__data: 0x2b8
+  __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 312
-  Symbols:   585
-  CStrings:  888
+  Functions: 365
+  Symbols:   651
+  CStrings:  939
 
Symbols:
+ _NLLanguageEnglish
+ _OBJC_CLASS_$_FedStatsUtilsGammaDistribution
+ _OBJC_CLASS_$_FedStatsUtilsNegativeBinomialDistribution
+ _OBJC_CLASS_$_FedStatsUtilsNormalDistribution
+ _OBJC_CLASS_$_FedStatsUtilsPoissonDistribution
+ _OBJC_CLASS_$_FedStatsUtilsUniformUnitIntervalDistribution
+ _OBJC_METACLASS_$_FedStatsUtilsGammaDistribution
+ _OBJC_METACLASS_$_FedStatsUtilsNegativeBinomialDistribution
+ _OBJC_METACLASS_$_FedStatsUtilsNormalDistribution
+ _OBJC_METACLASS_$_FedStatsUtilsPoissonDistribution
+ _OBJC_METACLASS_$_FedStatsUtilsUniformUnitIntervalDistribution
+ __os_log_error_impl
+ _arc4random_buf
+ _cos
+ _exp
+ _kFedStatsTokenLocationEntity
+ _kFedStatsTokenNumberEntity
+ _kFedStatsTokenPersonEntity
+ _log
+ _objc_setProperty_nonatomic_copy
+ _pow
- _NLTagPunctuation
- _NLTagSentenceTerminator
- _OBJC_CLASS_$_NSMutableCharacterSet
- _kFedStatsCategoricalTypeParameterRemovePunctuation
- _kFedStatsCategoricalTypeParameterTokenizeLocation
- _kFedStatsCategoricalTypeParameterTokenizeNumber
- _kFedStatsCategoricalTypeParameterTokenizePerson
- _kHuffmanLocationEntity
- _kHuffmanNumberEntity
- _kHuffmanPersonEntity
CStrings:
+ "@\"FedStatsUtilsGammaDistribution\""
+ "@24@0:8d16"
+ "@32@0:8d16Q24"
+ "@32@0:8d16d24"
+ "@40@0:8d16d24@32"
+ "@48@0:8@16B24B28B32B36q40"
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
+ "availableTagSchemesForUnit:language:"
+ "cap"
+ "d"
+ "d16@0:8"
+ "d32@0:8d16d24"
+ "defaultDataPointForDataTypeContent:"
+ "distributionWithShape:scale:cap:"
+ "distributionWithSuccessCount:successProbability:"
+ "gamma"
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
+ "sampleLarge"
+ "sampleLargeWithShape:scale:"
+ "sampleSmall"
+ "sampleUncapped"
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
- "formUnionWithCharacterSet:"
- "initWithRemovePunctuation:shuffleMethod:popularWordsDB:tokenizePerson:tokenizeLocation:tokenizeNumber:"
- "punctuationCharacterSet"
- "removePunctuation"
- "tokenizeAndSampleUnigramFromNgram:"
- "tokenizeLocation"
- "tokenizeNumber"
- "tokenizePerson"
- "tokenizeSentence:"
- "whitespaceAndNewlineCharacterSet"

```
