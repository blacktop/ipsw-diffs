## QueryUnderstanding

> `/System/Library/PrivateFrameworks/QueryUnderstanding.framework/QueryUnderstanding`

```diff

-3525.3.5.0.0
-  __TEXT.__text: 0x6640
-  __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_methlist: 0x724
-  __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0xce9
-  __TEXT.__oslogstring: 0x4be
-  __TEXT.__gcc_except_tab: 0x810
-  __TEXT.__unwind_info: 0x300
-  __TEXT.__objc_classname: 0xad
-  __TEXT.__objc_methname: 0x130c
-  __TEXT.__objc_methtype: 0x401
-  __TEXT.__objc_stubs: 0xe40
-  __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x6c0
+3600.26.10.1.2
+  __TEXT.__text: 0x6aa8
+  __TEXT.__objc_methlist: 0x72c
+  __TEXT.__const: 0xb0
+  __TEXT.__cstring: 0xf2e
+  __TEXT.__oslogstring: 0x4e6
+  __TEXT.__gcc_except_tab: 0x944
+  __TEXT.__unwind_info: 0x2a8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x6d8
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x538
+  __DATA_CONST.__weak_got: 0x8
+  __DATA_CONST.__objc_selrefs: 0x5e8
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x218
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x320
+  __DATA_CONST.__got: 0x140
+  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__cfstring: 0x500
   __AUTH_CONST.__objc_const: 0xe78
+  __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x80
   __DATA.__data: 0x180
-  __DATA.__bss: 0x8
+  __DATA.__bss: 0x9
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__data: 0x1
-  __DATA_DIRTY.__bss: 0x60
+  __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/CoreNLP.framework/CoreNLP
   - /System/Library/PrivateFrameworks/EmbeddingService.framework/EmbeddingService
   - /System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources
+  - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 142973F6-08A0-3E45-93DA-DFC5126E792D
-  Functions: 135
-  Symbols:   664
-  CStrings:  552
+  UUID: D39E427A-E2F9-3F8E-88A7-C53F8A35CEFA
+  Functions: 140
+  Symbols:   717
+  CStrings:  290
 
Symbols:
+ +[U2OwlModel normalizeQueryForInference:]
+ GCC_except_table2
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_UAFAssetSetManager
+ _QUCopyFilePathsForContentTypeAndLocale
+ _QUIsUAFEnabled
+ _QUIsUAFEnabled.cold.1
+ __ZNSt12length_errorC1B9foe220100EPKc
+ __ZNSt3__119__allocate_at_leastB9foe220100INS_9allocatorIfEENS_16allocator_traitsIS2_EEEENS_19__allocation_resultINT0_7pointerENS6_9size_typeEEERT_m
+ __ZNSt3__120__throw_length_errorB9foe220100EPKc
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB9foe220100Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB9foe220100IPfS5_EEvT_T0_m
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B9foe220100Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B9foe220100EmRKf
+ __ZSt28__throw_bad_array_new_lengthB9foe220100v
+ __ZZ14QUIsUAFEnabledE10uafEnabled
+ __ZZ14QUIsUAFEnabledE9onceToken
+ ___NSArray0__struct
+ ___QUIsUAFEnabled_block_invoke
+ ___block_literal_global.174
+ __os_feature_enabled_impl
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$allValues
+ _objc_msgSend$assetNamed:
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$componentsSeparatedByCharactersInSet:
+ _objc_msgSend$contentsOfDirectoryAtPath:error:
+ _objc_msgSend$countryCode
+ _objc_msgSend$defaultManager
+ _objc_msgSend$dictionary
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$location
+ _objc_msgSend$normalizeQueryForInference:
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$retrieveAssetSet:usages:
+ _objc_msgSend$scriptCode
+ _objc_msgSend$sharedManager
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$stringByReplacingMatchesInString:options:range:withTemplate:
+ _objc_msgSend$stringByTrimmingCharactersInSet:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$whitespaceCharacterSet
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x4
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB9nqe210106IPfS5_EEvT_T0_m
- __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B9nqe210106Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B9nqe210106EmRKf
- __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- ___block_literal_global.175
CStrings:
+ " "
+ "$1 $2"
+ "%@-%@"
+ "%@_%@"
+ "([a-zA-Z]):([^ ])"
+ "-_"
+ ".bundle"
+ ".mlmodelc"
+ ".mlpackage"
+ "/AppleInternal/Library/BuildRoots/4~CQ96ugDnvvXc8NpsF4RcdwiCuqZhhpOGMPAhj10/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:413: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "ARG_HOME_LOCATION"
+ "EnableUAFAssetDelivery"
+ "HOME_LOCATION"
+ "INTENT_HOME_SEARCH"
+ "QueryParser"
+ "[QPNLU] Failed to find U2 Model via UAF"
+ "\\s+"
+ "com.apple.search.queryparser"
+ "com.apple.search.queryunderstanding"
+ "sqp.language"
+ "sqp.parser"
+ "sqp.safety"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<QUUnderstandingModel>\""
- "@\"MLFeatureValue\"24@0:8@\"NSString\"16"
- "@\"MLModel\""
- "@\"MLMultiArray\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSCondition\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSError\""
- "@\"NSLocale\""
- "@\"NSLocale\"16@0:8"
- "@\"NSNumber\""
- "@\"NSNumber\"16@0:8"
- "@\"NSObject<OS_os_transaction>\""
- "@\"NSSet\""
- "@\"NSSet\"16@0:8"
- "@\"NSString\"16@0:8"
- "@\"QUEmbeddingService\""
- "@\"U2Head\""
- "@\"U2HeadWrapper\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@28@0:8@16I24"
- "@32@0:8:16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^@32"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24@32^@40"
- "@72@0:8@16@24q32@40@48@56@64"
- "@96@0:8@16@24q32@40@48@56@64@72@80^@88"
- "@?"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "MLFeatureProvider"
- "NSObject"
- "Q"
- "Q16@0:8"
- "QUModelFactory"
- "QUSpans"
- "QUUnderstandingModel"
- "QUUnderstandingOutput"
- "T#,R"
- "T@\"MLModel\",R,N,V_model"
- "T@\"MLMultiArray\",&,N,V_arg_conf_scores"
- "T@\"MLMultiArray\",&,N,V_input_mask"
- "T@\"MLMultiArray\",&,N,V_input_span_features"
- "T@\"MLMultiArray\",&,N,V_intent_scores"
- "T@\"MLMultiArray\",&,N,V_safety_head_scores"
- "T@\"MLMultiArray\",&,N,V_sequence_output"
- "T@\"MLMultiArray\",&,N,V_top_arg_ids"
- "T@\"NSArray\",&,N,V_argIdsForTokens"
- "T@\"NSArray\",&,N,V_argScoresForTokens"
- "T@\"NSArray\",&,N,V_tokenRanges"
- "T@\"NSArray\",&,N,V_tokens"
- "T@\"NSArray\",C,N,V_locationNameRanges"
- "T@\"NSArray\",C,N,V_peopleNameRanges"
- "T@\"NSArray\",R,N"
- "T@\"NSBundle\",&,N"
- "T@\"NSDictionary\",R,N"
- "T@\"NSError\",&,N,V_loadError"
- "T@\"NSLocale\",&,N,V_locale"
- "T@\"NSLocale\",R,N"
- "T@\"NSNumber\",&,N,V_confidenceScore"
- "T@\"NSNumber\",&,N,V_intentId"
- "T@\"NSNumber\",&,N,V_safetyScore"
- "T@\"NSNumber\",R,N"
- "T@\"NSSet\",R,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,N"
- "TQ,N,V_embeddingsTime"
- "TQ,N,V_predictionTime"
- "TQ,R"
- "TQ,R,N"
- "U2HeadBundle"
- "U2HeadInput"
- "U2HeadOutput"
- "U2HeadWrapper"
- "U2Output"
- "U2OwlModel"
- "URLForResource:withExtension:subdirectory:localization:"
- "URLOfModelInThisBundle"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_argIdsForTokens"
- "_argScoresForTokens"
- "_arg_conf_scores"
- "_condition"
- "_confidenceScore"
- "_embeddingService"
- "_embeddingsTime"
- "_input_mask"
- "_input_span_features"
- "_intentId"
- "_intent_scores"
- "_loadError"
- "_loadingLocale"
- "_locale"
- "_locationNameRanges"
- "_model"
- "_peopleNameRanges"
- "_predictionTime"
- "_quModel"
- "_releaseBlock"
- "_safetyScore"
- "_safety_head_scores"
- "_sequence_output"
- "_state"
- "_tokenRanges"
- "_tokens"
- "_top_arg_ids"
- "_transaction"
- "_u2Head"
- "_u2headWrapper"
- "_unsupportedLocaleIdentifiers"
- "addObject:"
- "argIds"
- "argIdsForTokens"
- "argScores"
- "argScoresForTokens"
- "argmaxWithIndex:"
- "array"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "assetURL"
- "autorelease"
- "boolValue"
- "broadcast"
- "bundleForClass:"
- "class"
- "componentsSeparatedByString:"
- "confidenceScore"
- "conformsToProtocol:"
- "containsObject:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dateWithTimeIntervalSinceNow:"
- "debugDescription"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "embedding"
- "embeddingsTime"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "featureNames"
- "featureValueForName:"
- "featureValueWithMultiArray:"
- "featuresAtIndex:"
- "filePathArrayForKey:didFailWithError:"
- "fileURLWithPath:"
- "firstObject"
- "floatValue"
- "getEmbeddingForQuery:completionHandler:"
- "getModelForLocale:withTimeoutMS:"
- "getTokenScoresfromScoreTensor:intentIndex:tokens:subtokenLenForTokens:subtokens:scoreFromSubtokenScores:"
- "getU2PredictionsForEmbedding:queryString:queryID:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:intentHint:error:"
- "getUnderstandingForQueryString:queryID:spans:intentHint:withCompletionHandler:"
- "hash"
- "init"
- "initWithConfiguration:error:"
- "initWithContentsOfURL:configuration:error:"
- "initWithContentsOfURL:error:"
- "initWithFeatureProviderArray:"
- "initWithInput_mask:input_span_features:sequence_output:"
- "initWithLocale:"
- "initWithLocale:version:"
- "initWithMLModel:"
- "initWithShape:dataType:error:"
- "initWithTop_arg_ids:arg_conf_scores:intent_scores:safety_head_scores:"
- "insertObject:atIndex:"
- "intValue"
- "intentId"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "languageCode"
- "length"
- "loadContentsOfURL:configuration:completionHandler:"
- "loadError"
- "loadWithCompletionHandler:"
- "loadWithConfiguration:completionHandler:"
- "locale"
- "localeIdentifier"
- "locationNameRanges"
- "lock"
- "log"
- "mapLogitsToLabels:queryString:queryID:intentHint:tokens:subtokenLenForTokens:subtokens:"
- "metadata"
- "model"
- "modelDescription"
- "modelLoaded"
- "modelMetadata"
- "modelWithContentsOfURL:configuration:error:"
- "modelWithContentsOfURL:error:"
- "multiArrayValue"
- "numberWithBool:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithInteger:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "path"
- "pathForResource:ofType:"
- "peopleNameRanges"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "predictionFromFeatures:completionHandler:"
- "predictionFromFeatures:error:"
- "predictionFromFeatures:options:completionHandler:"
- "predictionFromFeatures:options:error:"
- "predictionFromInput_mask:input_span_features:sequence_output:error:"
- "predictionTime"
- "predictionsFromBatch:options:error:"
- "predictionsFromInputs:options:error:"
- "quModel"
- "rangeValue"
- "release"
- "releaseModel"
- "resourcesForClient:locale:options:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "safetyScore"
- "self"
- "setArgIdsForTokens:"
- "setArgScoresForTokens:"
- "setArg_conf_scores:"
- "setComputeUnits:"
- "setConfidenceScore:"
- "setEmbeddingsTime:"
- "setExperimentalMLE5EngineUsage:"
- "setInput_mask:"
- "setInput_span_features:"
- "setIntentId:"
- "setIntent_scores:"
- "setLoadError:"
- "setLocale:"
- "setLocationNameRanges:"
- "setObject:atIndexedSubscript:"
- "setObject:forKeyedSubscript:"
- "setPeopleNameRanges:"
- "setPredictionTime:"
- "setSafetyScore:"
- "setSafety_head_scores:"
- "setSequence_output:"
- "setTokenRanges:"
- "setTokens:"
- "setTop_arg_ids:"
- "setU2HeadBundle:"
- "setUseSpotlightResources:"
- "setWithArray:"
- "setWithObjects:"
- "shape"
- "sharedInstance"
- "sharedResourcesManager"
- "signpostLog"
- "subtokenLenForTokens"
- "subtokens"
- "superclass"
- "tokenRanges"
- "tokens"
- "unlock"
- "useSpotlightResources"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"<QUUnderstandingModel>\"@\"NSError\">16"
- "v24@0:8Q16"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@?32"
- "v56@0:8@\"NSString\"16q24@\"QUSpans\"32@\"NSNumber\"40@?<v@?@\"<QUUnderstandingOutput>\"@\"NSError\">48"
- "v56@0:8@16q24@32@40@?48"
- "waitUntilDate:"
- "zone"
- "{vector<float, std::allocator<float>>=^f^f{?=^f}}60@0:8@16i24@28@36@44@?52"

```
