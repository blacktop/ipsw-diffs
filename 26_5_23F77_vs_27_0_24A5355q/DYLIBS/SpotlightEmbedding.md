## SpotlightEmbedding

> `/System/Library/PrivateFrameworks/SpotlightEmbedding.framework/SpotlightEmbedding`

```diff

-2418.5.9.101.0
-  __TEXT.__text: 0x5b74
-  __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_methlist: 0x38c
+2444.104.0.0.0
+  __TEXT.__text: 0x550c
+  __TEXT.__objc_methlist: 0x394
   __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0x22c
-  __TEXT.__cstring: 0x57f
-  __TEXT.__oslogstring: 0x5d0
+  __TEXT.__gcc_except_tab: 0x1e4
+  __TEXT.__cstring: 0x563
+  __TEXT.__oslogstring: 0x5ef
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x1c8
-  __TEXT.__objc_classname: 0x67
-  __TEXT.__objc_methname: 0xcff
-  __TEXT.__objc_methtype: 0x1c9
-  __TEXT.__objc_stubs: 0xf40
-  __DATA_CONST.__got: 0x108
+  __TEXT.__unwind_info: 0x180
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2a8
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x478
-  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_selrefs: 0x4a8
+  __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x330
-  __AUTH_CONST.__auth_got: 0x260
+  __DATA_CONST.__got: 0x100
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x720
-  __AUTH_CONST.__objc_const: 0x660
-  __AUTH_CONST.__objc_doubleobj: 0x180
+  __AUTH_CONST.__cfstring: 0x6a0
+  __AUTH_CONST.__objc_const: 0x4a0
+  __AUTH_CONST.__objc_doubleobj: 0x170
   __AUTH_CONST.__objc_dictobj: 0x2d0
-  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x4c
+  __DATA.__objc_ivar: 0x24
+  __DATA.__data: 0xc0
   __DATA.__bss: 0x8
-  __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__bss: 0x78
+  __DATA_DIRTY.__objc_data: 0xa0
+  __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
-  - /System/Library/PrivateFrameworks/CoreSceneUnderstanding.framework/CoreSceneUnderstanding
+  - /System/Library/PrivateFrameworks/EmbeddingCore.framework/EmbeddingCore
   - /System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/SpotlightEmbeddingCore.framework/SpotlightEmbeddingCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: CDD52197-21AE-3FEB-9EF3-09C8BC299DE0
-  Functions: 104
-  Symbols:   545
-  CStrings:  371
+  UUID: AAF5E851-A119-3E9F-B08F-FC656BF0DCED
+  Functions: 80
+  Symbols:   483
+  CStrings:  155
 
Symbols:
+ +[SPEmbeddingModel initialize]
+ -[SPEmbeddingModel previousVersion]
+ GCC_except_table25
+ GCC_except_table33
+ GCC_except_table7
+ _OBJC_CLASS_$_MADTokenizer
+ _SPEmbeddingProviderRegister
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_CLASS_METHODS_SPEmbeddingProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SPEmbeddingProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SPEmbeddingProvider
+ __OBJC_$_PROTOCOL_REFS_SPEmbeddingProvider
+ __OBJC_CLASS_PROTOCOLS_$_SPEmbeddingModel
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_SPEmbeddingProvider
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_SPEmbeddingProvider
+ ___block_descriptor_165_e8_32s40s48s56s64s72s80s88r96r104r112r_e20_v20?0i8"NSError"12lr88l8s32l8s40l8r96l8s48l8s56l8r104l8s64l8r112l8s72l8s80l8
+ __os_feature_enabled_impl
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$activeTextEmbeddingVersions:
+ _objc_msgSend$previousVersion
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x8
- +[SPEmbeddingResult log]
- -[SPEmbeddingResult .cxx_destruct]
- -[SPEmbeddingResult bias]
- -[SPEmbeddingResult description]
- -[SPEmbeddingResult elementCount]
- -[SPEmbeddingResult elementType]
- -[SPEmbeddingResult embeddingData]
- -[SPEmbeddingResult initWithVersion:data:type:scale:bias:]
- -[SPEmbeddingResult scale]
- -[SPEmbeddingResult version]
- -[SPTextInput .cxx_destruct]
- -[SPTextInput attributedString]
- -[SPTextInput initWithAttributedString:]
- -[SPTextInput initWithText:]
- -[SPTextInput initWithTokenIds:]
- -[SPTextInput inputSource]
- -[SPTextInput setAttributedString:]
- -[SPTextInput setInputSource:]
- -[SPTextInput setText:]
- -[SPTextInput setTokenIDs:]
- -[SPTextInput setType:]
- -[SPTextInput text]
- -[SPTextInput tokenIDs]
- -[SPTextInput tokenLength]
- -[SPTextInput type]
- GCC_except_table23
- GCC_except_table31
- GCC_except_table6
- _OBJC_CLASS_$_CSUTokenizer
- _OBJC_CLASS_$_NSMutableString
- _OBJC_CLASS_$_SPTextInput
- _OBJC_IVAR_$_SPEmbeddingResult._bias
- _OBJC_IVAR_$_SPEmbeddingResult._elementType
- _OBJC_IVAR_$_SPEmbeddingResult._embeddingData
- _OBJC_IVAR_$_SPEmbeddingResult._scale
- _OBJC_IVAR_$_SPEmbeddingResult._version
- _OBJC_IVAR_$_SPTextInput._attributedString
- _OBJC_IVAR_$_SPTextInput._inputSource
- _OBJC_IVAR_$_SPTextInput._text
- _OBJC_IVAR_$_SPTextInput._tokenIDs
- _OBJC_IVAR_$_SPTextInput._type
- _OBJC_METACLASS_$_SPEmbeddingResult
- _OBJC_METACLASS_$_SPTextInput
- __OBJC_$_CLASS_METHODS_SPEmbeddingResult
- __OBJC_$_INSTANCE_METHODS_SPEmbeddingResult
- __OBJC_$_INSTANCE_METHODS_SPTextInput
- __OBJC_$_INSTANCE_VARIABLES_SPEmbeddingResult
- __OBJC_$_INSTANCE_VARIABLES_SPTextInput
- __OBJC_$_PROP_LIST_SPEmbeddingResult
- __OBJC_$_PROP_LIST_SPTextInput
- __OBJC_CLASS_RO_$_SPEmbeddingResult
- __OBJC_CLASS_RO_$_SPTextInput
- __OBJC_METACLASS_RO_$_SPEmbeddingResult
- __OBJC_METACLASS_RO_$_SPTextInput
- ___24+[SPEmbeddingResult log]_block_invoke
- ___block_descriptor_153_e8_32s40s48s56s64s72s80r88r96r104r_e20_v20?0i8"NSError"12lr80l8s32l8s40l8r88l8s48l8s56l8r96l8s64l8r104l8s72l8
- _objc_msgSend$appendFormat:
- _objc_msgSend$copy
- _objc_msgSend$elementCount
- _objc_msgSend$firstObject
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x28
CStrings:
+ "EmbeddingMigration"
+ "MediaAnalysis"
+ "get MAD activeTextEmbeddingVersions failed: %@"
+ "get too many activeTextEmbeddingVersions: %u"
- "!"
- ".cxx_destruct"
- "<%@ %p, "
- "@\"CSUTokenizer\""
- "@\"MADService\""
- "@\"NSArray\""
- "@\"NSAttributedString\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16^@24"
- "@48@0:8Q16@24Q32f40f44"
- "@52@0:8@16B24q28q36^@44"
- "@72@0:8@16B24q28@36q44B52^q56^@64"
- "@76@0:8@16B24@28q36@44q52^q60^@68"
- "@84@0:8@16B24@28q36@44q52B60B64^q68^@76"
- "B"
- "B16@0:8"
- "B20@0:8i16"
- "Embedding has unknown element type (%d); cannot derive count"
- "Q"
- "Q16@0:8"
- "SPEmbeddingModel"
- "SPEmbeddingResult"
- "SPEmbeddingTailspinDumper"
- "SPEmbeddingTokenizer"
- "SPTextInput"
- "T@\"NSArray\",&,N,V_tokenIDs"
- "T@\"NSAttributedString\",&,N,V_attributedString"
- "T@\"NSData\",R,N,V_embeddingData"
- "T@\"NSDate\",&,N,V_latestDumpDate"
- "T@\"NSString\",&,N,V_text"
- "TB,R,N"
- "TQ,N,V_inputSource"
- "TQ,N,V_type"
- "TQ,R,N"
- "TQ,R,N,V_elementType"
- "TQ,R,N,V_version"
- "Tf,R,N,V_bias"
- "Tf,R,N,V_scale"
- "TokenizerForRevision:error:"
- "UTF8String"
- "_attributedString"
- "_bias"
- "_dumpQueue"
- "_elementType"
- "_embeddingData"
- "_initModel"
- "_inputSource"
- "_latestDumpDate"
- "_processAttributedString:"
- "_processText:"
- "_processTextInputs:error:"
- "_processTokenIDs:"
- "_queryIDs"
- "_queue"
- "_requestIDs"
- "_scale"
- "_service"
- "_text"
- "_tokenIDs"
- "_tokenizer"
- "_type"
- "_version"
- "_warmedUp"
- "addEntityUUID:"
- "addObject:"
- "addText:"
- "addTokenIDs:"
- "appendFormat:"
- "array"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "attributedString"
- "attributesOfItemAtPath:error:"
- "bias"
- "boolValue"
- "bundleIdentifier"
- "canDump"
- "cancelAllRequests"
- "cancelQueryID:"
- "cancelRequestID:"
- "cleanupOldDumps"
- "clear"
- "clearQueryID:requestID:"
- "compare:"
- "contentsOfDirectoryAtPath:error:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countryCode"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "csuTokenizerRevision"
- "currentLocale"
- "data"
- "defaultManager"
- "description"
- "deviceCanGenerateEmbeddings"
- "dictionaryWithObjects:forKeys:count:"
- "dump"
- "dumpTailspinSync:"
- "elementCount"
- "elementCount: %d, "
- "elementType"
- "elementType: %d, "
- "embedding"
- "embeddingData"
- "embeddingData: %@>"
- "embeddingResults"
- "enumerateAttributesInRange:options:usingBlock:"
- "enumerateKeysAndObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "f"
- "f16@0:8"
- "fileExistsAtPath:"
- "fileSystemRepresentation"
- "firstObject"
- "floatValue"
- "generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:clientBundleID:timeout:useCLIPSafety:computeThreshold:workCost:error:"
- "generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:clientBundleID:timeout:workCost:error:"
- "generateEmbeddingForTextInputs:extendedContextLength:queryID:clientBundleID:timeout:useCLIPSafety:workCost:error:"
- "generateEmbeddingForTextInputs:extendedContextLength:queryID:timeout:error:"
- "getTokenIDsForText:"
- "getTokensForText:"
- "getUnifiedEmbeddingVersion"
- "hasPrefix:"
- "hasSuffix:"
- "init"
- "initTokenizer"
- "initWithAttributedString:"
- "initWithCapacity:"
- "initWithText:"
- "initWithTokenIds:"
- "initWithUUIDString:"
- "initWithVersion:data:type:scale:bias:"
- "inputSource"
- "intValue"
- "isEqual:"
- "isEqualToNumber:"
- "isEqualToString:"
- "isSafe"
- "isSemanticSearchAvailable"
- "languageCode"
- "lastObject"
- "latestDumpDate"
- "length"
- "lockFilePath"
- "log"
- "logWithBundleID:indexOperation:itemCount:code:"
- "longValue"
- "lowercaseString"
- "mainBundle"
- "maxTokenLength"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInt:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "performRequests:textInputs:completionHandler:"
- "preheatWithCompletionHandler:"
- "prewarmTextRequests:completionHandler:"
- "processInfo"
- "processName"
- "removeAllObjects"
- "removeItemAtPath:error:"
- "removeLastObject"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "safetyScore"
- "scale"
- "service"
- "setAttributedString:"
- "setComputeSafety:"
- "setComputeThreshold:"
- "setDateFormat:"
- "setExtendedContextLength:"
- "setInputSource:"
- "setLatestDumpDate:"
- "setObject:forKey:"
- "setText:"
- "setTokenIDs:"
- "setType:"
- "setVersion:"
- "sharedInstance"
- "sortUsingComparator:"
- "string"
- "stringByAppendingPathComponent:"
- "stringByTrimmingCharactersInSet:"
- "stringFromDate:"
- "stringWithFormat:"
- "substringWithRange:"
- "tailspinDirectory"
- "tailspinPrefix"
- "timeIntervalSinceDate:"
- "tokenIDs"
- "tokenLength"
- "type"
- "v16@0:8"
- "v20@0:8i16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v28@0:8q16i24"
- "version"
- "warmedUp"
- "whitespaceCharacterSet"

```
