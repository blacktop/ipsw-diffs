## ContextKit

> `/System/Library/PrivateFrameworks/ContextKit.framework/ContextKit`

```diff

-302.0.0.0.0
-  __TEXT.__text: 0xfcb4
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_methlist: 0xffc
+305.0.0.0.0
+  __TEXT.__text: 0xf3e8
+  __TEXT.__objc_methlist: 0x104c
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x9ac
-  __TEXT.__gcc_except_tab: 0x308
+  __TEXT.__cstring: 0x9c3
+  __TEXT.__gcc_except_tab: 0x310
   __TEXT.__oslogstring: 0x937
-  __TEXT.__unwind_info: 0x538
-  __TEXT.__objc_classname: 0x17c
-  __TEXT.__objc_methname: 0x2c83
-  __TEXT.__objc_methtype: 0x756
-  __TEXT.__objc_stubs: 0x22c0
-  __DATA_CONST.__got: 0x180
+  __TEXT.__unwind_info: 0x4c0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x628
   __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbb0
+  __DATA_CONST.__objc_selrefs: 0xbe0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__got: 0x180
   __AUTH_CONST.__const: 0x3c0
   __AUTH_CONST.__cfstring: 0x10e0
-  __AUTH_CONST.__objc_const: 0x1d40
-  __AUTH.__objc_data: 0x50
+  __AUTH_CONST.__objc_const: 0x1d80
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x1a8
   __DATA.__data: 0x240
-  __DATA.__bss: 0x60
-  __DATA_DIRTY.__objc_data: 0x320
-  __DATA_DIRTY.__bss: 0x140
+  __DATA.__bss: 0x98
+  __DATA_DIRTY.__objc_data: 0x2d0
+  __DATA_DIRTY.__bss: 0x108
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ContextKitCore.framework/ContextKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 70F31ABA-AA1C-3AFC-B6E8-D65E02993D7B
-  Functions: 470
-  Symbols:   1778
-  CStrings:  1007
+  UUID: 1671606B-B593-39A2-9F44-0671CF4CF2B0
+  Functions: 465
+  Symbols:   1770
+  CStrings:  342
 
Symbols:
+ -[NSCoder(ContextKit_XCoding) decodeUInt32ForKey:]
+ -[NSCoder(ContextKit_XCoding) decodeUInt64ForKey:]
+ -[NSCoder(ContextKit_XCoding) decodeUIntegerForKey:]
+ -[NSCoder(ContextKit_XCoding) encodeUInt32:forKey:]
+ -[NSCoder(ContextKit_XCoding) encodeUInt64:forKey:]
+ -[NSCoder(ContextKit_XCoding) encodeUInteger:forKey:]
+ GCC_except_table62
+ GCC_except_table67
+ GCC_except_table70
+ GCC_except_table88
+ _OBJC_CLASS_$_NSCoder
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSCoder_$_ContextKit_XCoding
+ __OBJC_$_CATEGORY_NSCoder_$_ContextKit_XCoding
+ ___107+[CKContextRequest logTransactionSuccessfulForResponseId:inputLength:completionLength:requestType:logType:]_block_invoke.200
+ ___107+[CKContextRequest logTransactionSuccessfulForResponseId:inputLength:completionLength:requestType:logType:]_block_invoke.200.cold.1
+ ___108+[CKContextRequest logEngagementForResponseId:result:rank:inputLength:completionLength:requestType:logType:]_block_invoke.197
+ ___108+[CKContextRequest logEngagementForResponseId:result:rank:inputLength:completionLength:requestType:logType:]_block_invoke.197.cold.1
+ ___27-[CKContextRequest execute]_block_invoke.180
+ ___27-[CKContextRequest execute]_block_invoke.181
+ ___27-[CKContextRequest execute]_block_invoke.181.cold.1
+ ___27-[CKContextRequest execute]_block_invoke.184
+ ___31+[CKContextRequest pingService]_block_invoke.193
+ ___32+[CKContextXPCClient initialize]_block_invoke.46
+ ___35+[CKContextRequest shutdownService]_block_invoke.194
+ ___38-[CKContextRequest _executeWithReply:]_block_invoke.189
+ ___43+[CKContextRequest requestServiceSemaphore]_block_invoke.208
+ ___43+[CKContextRequest requestServiceSemaphore]_block_invoke.208.cold.1
+ ___49-[CKContextClient retrieveCapabilitiesWithReply:]_block_invoke.108
+ ___49-[CKContextClient retrieveCapabilitiesWithReply:]_block_invoke.108.cold.1
+ ___59-[CKContextRequest _executeCategorizationRequestWithReply:]_block_invoke.192
+ ___59-[CKContextRequest _executeCategorizationRequestWithReply:]_block_invoke.cold.1
+ ___block_descriptor_72_e8_32s40bs48r56r_e34_v24?0"NSDictionary"8"NSError"16lr48l8r56l8s40l8s32l8
+ ___block_literal_global.111
+ ___block_literal_global.118
+ ___block_literal_global.125
+ ___block_literal_global.133
+ ___block_literal_global.149
+ ___block_literal_global.164
+ ___block_literal_global.183
+ ___block_literal_global.196
+ ___block_literal_global.199
+ ___block_literal_global.202
+ ___block_literal_global.206
+ ___block_literal_global.210
+ ___block_literal_global.94
+ ___block_literal_global.96
+ _initWithCoder:.onceToken.109
+ _initWithCoder:.onceToken.116
+ _initWithCoder:.onceToken.123
+ _initWithCoder:.onceToken.131
+ _initWithCoder:.onceToken.139
+ _initWithCoder:.onceToken.147
+ _initWithCoder:.onceToken.155
+ _initWithCoder:.onceToken.162
+ _initWithCoder:.x.108
+ _initWithCoder:.x.115
+ _initWithCoder:.x.122
+ _initWithCoder:.x.130
+ _initWithCoder:.x.138
+ _initWithCoder:.x.146
+ _initWithCoder:.x.154
+ _initWithCoder:.x.161
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$decodeUInt32ForKey:
+ _objc_msgSend$decodeUIntegerForKey:
+ _objc_msgSend$encodeUInt32:forKey:
+ _objc_msgSend$encodeUInteger:forKey:
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_retain_x9
- -[NSCoder decodeUInt32ForKey:]
- -[NSCoder decodeUInt64ForKey:]
- -[NSCoder decodeUIntegerForKey:]
- -[NSCoder encodeUInt32:forKey:]
- -[NSCoder encodeUInt64:forKey:]
- -[NSCoder encodeUInteger:forKey:]
- GCC_except_table66
- GCC_except_table69
- GCC_except_table87
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- ___107+[CKContextRequest logTransactionSuccessfulForResponseId:inputLength:completionLength:requestType:logType:]_block_invoke.155
- ___107+[CKContextRequest logTransactionSuccessfulForResponseId:inputLength:completionLength:requestType:logType:]_block_invoke.155.cold.1
- ___108+[CKContextRequest logEngagementForResponseId:result:rank:inputLength:completionLength:requestType:logType:]_block_invoke.152
- ___108+[CKContextRequest logEngagementForResponseId:result:rank:inputLength:completionLength:requestType:logType:]_block_invoke.152.cold.1
- ___27-[CKContextRequest execute]_block_invoke.138
- ___27-[CKContextRequest execute]_block_invoke.139
- ___27-[CKContextRequest execute]_block_invoke.139.cold.1
- ___27-[CKContextRequest execute]_block_invoke.142
- ___31+[CKContextRequest pingService]_block_invoke.148
- ___32+[CKContextXPCClient initialize]_block_invoke.4
- ___35+[CKContextRequest shutdownService]_block_invoke.149
- ___38-[CKContextRequest _executeWithReply:]_block_invoke.147
- ___43+[CKContextRequest requestServiceSemaphore]_block_invoke.163
- ___43+[CKContextRequest requestServiceSemaphore]_block_invoke.163.cold.1
- ___49-[CKContextClient retrieveCapabilitiesWithReply:]_block_invoke.67
- ___49-[CKContextClient retrieveCapabilitiesWithReply:]_block_invoke.67.cold.1
- ___59-[CKContextRequest _executeCategorizationRequestWithReply:]_block_invoke_2.cold.1
- ___block_descriptor_48_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8
- ___block_literal_global.107
- ___block_literal_global.115
- ___block_literal_global.122
- ___block_literal_global.151
- ___block_literal_global.154
- ___block_literal_global.161
- ___block_literal_global.165
- ___block_literal_global.53
- ___block_literal_global.55
- ___block_literal_global.69
- ___block_literal_global.76
- ___block_literal_global.83
- ___block_literal_global.91
- ___block_literal_global.99
- _initWithCoder:.onceToken.105
- _initWithCoder:.onceToken.113
- _initWithCoder:.onceToken.120
- _initWithCoder:.onceToken.67
- _initWithCoder:.onceToken.74
- _initWithCoder:.onceToken.81
- _initWithCoder:.onceToken.89
- _initWithCoder:.onceToken.97
- _initWithCoder:.x.104
- _initWithCoder:.x.112
- _initWithCoder:.x.119
- _initWithCoder:.x.66
- _initWithCoder:.x.73
- _initWithCoder:.x.80
- _initWithCoder:.x.88
- _initWithCoder:.x.96
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
- _objc_retain_x27
CStrings:
- ".cxx_destruct"
- "@\"CKContextClient\""
- "@\"CKContextFingerprintMinHash\""
- "@\"CKContextRequest\""
- "@\"CKContextResponse\""
- "@\"CKContextSemaphore\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSDateComponents\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSLocale\""
- "@\"NSMutableArray\""
- "@\"NSNumber\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSOrderedSet\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSURL\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@28@0:8^i16I24"
- "@32@0:8@16Q24"
- "@32@0:8B16B20q24"
- "@48@0:8@16@24@32@40"
- "AB"
- "AI"
- "AQ"
- "B"
- "B16@0:8"
- "B20@0:8B16"
- "B24@0:8@16"
- "CKContextClient"
- "CKContextCompleter"
- "CKContextCountedString"
- "CKContextDonationServiceProtocol"
- "CKContextFingerprint"
- "CKContextGlobals"
- "CKContextRequest"
- "CKContextResponse"
- "CKContextResult"
- "CKContextSemaphore"
- "CKContextServiceUpdateNotifications"
- "CKContextXPCClient"
- "CKContextXPCProtocol"
- "ContextKit_XCoding"
- "I"
- "I16@0:8"
- "NSCoding"
- "NSCopying"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T@\"CKContextFingerprintMinHash\",&,N,V_requestFingerprint"
- "T@\"CKContextRequest\",&,N,V_debugRequest"
- "T@\"NSArray\",&,N,V_donorBundleIdentifiers"
- "T@\"NSArray\",&,N,V_level1Topics"
- "T@\"NSArray\",&,N,V_level2Topics"
- "T@\"NSArray\",&,N,V_results"
- "T@\"NSArray\",C,N,V_associatedResults"
- "T@\"NSArray\",C,N,V_donorBundleIdentifiers"
- "T@\"NSArray\",C,N,V_urls"
- "T@\"NSDate\",&,N,V_hideCompletionsAfterDate"
- "T@\"NSDate\",&,N,V_responseDate"
- "T@\"NSDateComponents\",C,N,V_extractedEndDateComponents"
- "T@\"NSDateComponents\",C,N,V_extractedStartDateComponents"
- "T@\"NSDictionary\",&,N,V_itemIds"
- "T@\"NSDictionary\",C,N,V_extractedAddressComponents"
- "T@\"NSDictionary\",C,N,V_partsOfSpeechToTexts"
- "T@\"NSError\",&,N,V_error"
- "T@\"NSError\",R,N"
- "T@\"NSNumber\",&,N,V_overrideBlendAlpha"
- "T@\"NSNumber\",&,N,V_overrideBlendBeta"
- "T@\"NSNumber\",&,N,V_overrideBlendGamma"
- "T@\"NSOrderedSet\",&,N,V_desiredLanguageTags"
- "T@\"NSOrderedSet\",C,N,V_relatedItems"
- "T@\"NSSet\",&,N,V_allowedTopicTypeTags"
- "T@\"NSSet\",C,N,V_preferredSceneIdentifiers"
- "T@\"NSSet\",C,N,V_tags"
- "T@\"NSSet\",R,N"
- "T@\"NSString\",&,N,V_debug"
- "T@\"NSString\",&,N,V_languageTag"
- "T@\"NSString\",&,N,V_string"
- "T@\"NSString\",C,N"
- "T@\"NSString\",C,N,V_category"
- "T@\"NSString\",C,N,V_debug"
- "T@\"NSString\",C,N,V_query"
- "T@\"NSString\",C,N,V_sceneIdentifier"
- "T@\"NSString\",C,N,V_title"
- "T@\"NSString\",C,N,V_topicId"
- "T@\"NSString\",C,N,V_uuid"
- "T@\"NSURL\",C,N,V_url"
- "TB,N,GisExactMatch,V_exactMatch"
- "TB,N,GisOnScreen,V_onScreen"
- "TB,N,V_debug"
- "TB,N,V_dontSkip"
- "TB,N,V_incPending"
- "TB,N,V_includeHigherLevelTopics"
- "TB,N,V_includeLeadImage"
- "TB,N,V_includePartsOfSpeech"
- "TB,N,V_includeRequestInResponse"
- "TB,N,V_includeStructuredExtractionResults"
- "TB,N,V_overrideEnableCoreNLPTagging"
- "TB,N,V_resultsNeedFiltering"
- "TB,N,V_textIsRaw"
- "TB,N,V_timing"
- "TB,R"
- "TB,R,N,GisRequestingContentFromActiveApplications"
- "TI,N,V_topk"
- "TI,R,N,V_numHashes"
- "TQ,N,V_count"
- "TQ,N,V_fingerprintMax"
- "TQ,N,V_mustPrefixMatchLength"
- "TQ,N,V_requestType"
- "TQ,N,V_type"
- "TQ,R,N,V_defaultRequestType"
- "T^i,R,N,V_hashes"
- "Td,N,V_donationTimeout"
- "Ti,N,V_overrideConstellationMinCount"
- "Ti,N,V_overrideConstellationMinWeight"
- "Tq,N,V_maxConstellationTopics"
- "Tq,N,V_minPrefix"
- "Tq,N,V_type"
- "T{CGPoint=dd},N,V_absoluteOriginOnScreen"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_frameInWindow"
- "T{CGSize=dd},N,V_availableLayoutSize"
- "URLWithString:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv24@0:8@\"CKContextDonation\"16"
- "Vv24@0:8@16"
- "^i"
- "^i16@0:8"
- "^{?=AIAIAIAIAiAiAQAIAI}"
- "_absoluteOriginOnScreen"
- "_allowedTopicTypeTags"
- "_associatedResults"
- "_availableLayoutSize"
- "_capabilities"
- "_category"
- "_client"
- "_couldHaveShown"
- "_count"
- "_creationTime"
- "_debug"
- "_debugRequest"
- "_defaultRequestType"
- "_desiredLanguageTags"
- "_discarded"
- "_donationTimeout"
- "_donorBundleIdentifiers"
- "_dontSkip"
- "_engaged"
- "_engagementLogged"
- "_error"
- "_exactMatch"
- "_executeCategorizationRequestWithReply:"
- "_executeWithReply:"
- "_extractedAddressComponents"
- "_extractedEndDateComponents"
- "_extractedStartDateComponents"
- "_fingerprintMax"
- "_frameInWindow"
- "_hashes"
- "_hideCompletions"
- "_hideCompletionsAfterDate"
- "_hideCompletionsTimeLimit"
- "_hideZKW"
- "_ignorePrefix"
- "_incPending"
- "_includeHigherLevelTopics"
- "_includeLeadImage"
- "_includePartsOfSpeech"
- "_includeRequestInResponse"
- "_includeStructuredExtractionResults"
- "_indexVersionId"
- "_input"
- "_inputKeystrokes"
- "_itemIds"
- "_languageTag"
- "_level1Topics"
- "_level2Topics"
- "_likelyUnsolicited"
- "_loggingCouldHaveShown"
- "_loggingCouldHaveShownMax"
- "_loggingInputLengthMax"
- "_loggingServerOverride"
- "_loggingShownMax"
- "_maxConstellationTopics"
- "_minPrefix"
- "_mustPrefixMatchLength"
- "_numHashes"
- "_observeApplicationStateNotifications"
- "_onScreen"
- "_overrideBlendAlpha"
- "_overrideBlendBeta"
- "_overrideBlendGamma"
- "_overrideConstellationMinCount"
- "_overrideConstellationMinWeight"
- "_overrideEnableCoreNLPTagging"
- "_partsOfSpeechToTexts"
- "_postProcessResponse:"
- "_preferredSceneIdentifiers"
- "_query"
- "_relatedItems"
- "_requestFingerprint"
- "_requestType"
- "_response"
- "_responseDate"
- "_results"
- "_resultsMatching:"
- "_resultsNeedFiltering"
- "_sceneIdentifier"
- "_searchLocale"
- "_sema"
- "_semaOwner"
- "_serviceSemaphore"
- "_shm"
- "_shmObject"
- "_shmSize"
- "_shown"
- "_shownLogged"
- "_string"
- "_tags"
- "_textIsRaw"
- "_timing"
- "_title"
- "_topicId"
- "_topk"
- "_transactionLogged"
- "_transactionSuccessful"
- "_type"
- "_updateHandlers"
- "_url"
- "_urls"
- "_uuid"
- "_zkwResults"
- "absoluteOriginOnScreen"
- "absoluteString"
- "activeGauge"
- "addDebug:"
- "addObject:"
- "addObserverForName:object:queue:usingBlock:"
- "allObjects"
- "allocWithZone:"
- "ancestorsForTopics:withReply:"
- "appendFormat:"
- "appendString:"
- "appendToDebug:"
- "array"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "availableLayoutSize"
- "bundleIdentifier"
- "busy"
- "bytes"
- "capabilities"
- "capabilitiesForRequestType:withReply:"
- "capabilitiesWithReply:"
- "characterAtIndex:"
- "clientWithDefaultRequestType:"
- "clientWithPreferredRequestType:"
- "code"
- "compareFingerprintWith:"
- "completer"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "containsObject:"
- "contentAuthor"
- "contentDescription"
- "contentKeywords"
- "copy"
- "copyWithZone:"
- "countByEnumeratingWithState:objects:count:"
- "createRequest"
- "currentLocale"
- "d"
- "d16@0:8"
- "d32@0:8Q16Q24"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "date"
- "dateByAddingTimeInterval:"
- "dealloc"
- "debugDescription"
- "debugText"
- "debugUrlString"
- "decPending"
- "decodeBoolForKey:"
- "decodeDoubleForKey:"
- "decodeFloatForKey:"
- "decodeInt32ForKey:"
- "decodeInt64ForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decodeXPCObjectForKey:"
- "decodeXPCObjectOfType:forKey:"
- "defaultCenter"
- "defaultRequestType"
- "description"
- "dictionaryWithObject:forKey:"
- "didReceiveCKContextServiceUpdateNotification"
- "discard"
- "discardAndLogCompleter:likelyUnsolicited:"
- "domain"
- "donate:"
- "encodeBool:forKey:"
- "encodeDouble:forKey:"
- "encodeFloat:forKey:"
- "encodeInt32:forKey:"
- "encodeInt64:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encodeXPCObject:forKey:"
- "ensureFullyInitialized"
- "errorWithDomain:code:userInfo:"
- "execute"
- "executeCategorizationRequestWithReply:"
- "executeWithReply:"
- "f24@0:8@16"
- "filteredArrayUsingPredicate:"
- "findCategorizationsForRequest:withReply:"
- "findResultsForRequest:withReply:"
- "findResultsForText:languageTag:requestType:withReply:"
- "findResultsForText:languageTag:withReply:"
- "findResultsForText:withReply:"
- "firstObject"
- "frameInWindow"
- "gauge"
- "groupResponses:withReply:"
- "hasPrefix:"
- "hash"
- "hideCompletionsAfterDate"
- "i"
- "i16@0:8"
- "indexVersionId"
- "init"
- "initForClient:"
- "initPlaceholderWithUUID:requestType:"
- "initSemaphoreForXPCService"
- "initWithCapacity:"
- "initWithCharactersNoCopy:length:freeWhenDone:"
- "initWithCoder:"
- "initWithDefaultRequestType:"
- "initWithError:requestType:"
- "initWithFormat:arguments:"
- "initWithHashes:count:"
- "initWithOptions:capacity:"
- "initWithResponse:"
- "initWithResults:requestType:"
- "initWithServiceName:"
- "initWithText:"
- "initWithTimeIntervalSinceNow:"
- "initWithTitle:query:url:category:"
- "initialize"
- "intValue"
- "interfaceWithProtocol:"
- "intersectsSet:"
- "invalidProcessError"
- "invalidate"
- "invalidateAndGetNewXpcConnection"
- "invalidateXpcConnection"
- "invalidationHandler"
- "isEqual:"
- "isEqualToString:"
- "isExactMatch"
- "isLikelyUnsolicitedUserInteraction"
- "isMainThread"
- "isOnScreen"
- "isPlaceholder"
- "isRequestingContentFromActiveApplications"
- "isXPCConnectionError:"
- "leadImage"
- "length"
- "logEngagement:forInput:"
- "logEngagement:forInput:completion:"
- "logEngagement:forInputLength:completion:likelyUnsolicited:"
- "logEngagementForResponseId:result:rank:inputLength:completionLength:requestType:logType:"
- "logResultsShown:serverOverride:"
- "logResultsShown:serverOverride:forInput:"
- "logResultsShownForResponseId:shown:couldHaveShown:topicIds:serverOverride:inputLength:requestType:logType:"
- "logTransactionSuccessfulForInput:"
- "logTransactionSuccessfulForInput:completion:"
- "logTransactionSuccessfulForInputLength:completion:likelyUnsolicited:"
- "logTransactionSuccessfulForResponseId:inputLength:completionLength:requestType:logType:"
- "mainBundle"
- "malformedRequestError"
- "markResultsShown:serverOverride:forInputLength:results:"
- "missingEntitlementError"
- "mutableCopy"
- "new"
- "newRequest"
- "newXpcConnection"
- "notify"
- "notifyAll"
- "numAcquired"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInteger:"
- "objectForKeyedSubscript:"
- "parse:"
- "pending"
- "pendingExceptionsCount"
- "pingService"
- "pingServiceWithReply:"
- "portraitId"
- "predicateWithFormat:"
- "punctuationCharacterSet"
- "q"
- "q16@0:8"
- "q20@0:8B16"
- "q24@0:8d16"
- "queriesMatching:"
- "rangeOfString:"
- "rangeOfString:options:range:locale:"
- "rawHTML"
- "registerConfigurationUpdateHandler:"
- "registerForServiceUpdateNotifications:"
- "remoteObjectProxyWithErrorHandler:"
- "requestServiceSemaphore"
- "requestServiceSemaphoreWithReply:"
- "requestWithText:"
- "requestingContentFromActiveApplications"
- "requestsServed"
- "resetPending"
- "responseDate"
- "responseSummary:showHigherLevelTopics:maxPrefix:"
- "resultByQuery:"
- "resultsMatching:"
- "resultsMatchingTags:"
- "resume"
- "retrieveCapabilites"
- "retrieveCapabilitiesWithReply:"
- "runOffMainThread:"
- "scanHexInt:"
- "scannerWithString:"
- "semaphoreWithReply:"
- "serviceBusyError"
- "serviceDisabledError"
- "set"
- "setAbsoluteOriginOnScreen:"
- "setActiveGauge:"
- "setAllowedTopicTypeTags:"
- "setAssociatedResults:"
- "setAvailableLayoutSize:"
- "setCategory:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setContentAuthor:"
- "setContentDescription:"
- "setContentKeywords:"
- "setCount:"
- "setDebug:"
- "setDebugRequest:"
- "setDebugText:"
- "setDebugUrlString:"
- "setDefaultRequestType:"
- "setDesiredLanguageTags:"
- "setDonationTimeout:"
- "setDonorBundleIdentifiers:"
- "setDontSkip:"
- "setError:"
- "setExactMatch:"
- "setExtractedAddressComponents:"
- "setExtractedEndDateComponents:"
- "setExtractedStartDateComponents:"
- "setFingerprintMax:"
- "setFrameInWindow:"
- "setHideCompletionsAfterDate:"
- "setHideCompletionsTimeLimit:"
- "setIncPending:"
- "setIncludeHigherLevelTopics:"
- "setIncludeLeadImage:"
- "setIncludePartsOfSpeech:"
- "setIncludeRequestInResponse:"
- "setIncludeStructuredExtractionResults:"
- "setInvalidationHandler:"
- "setItemIds:"
- "setLanguageTag:"
- "setLeadImage:"
- "setLevel1Topics:"
- "setLevel2Topics:"
- "setMaxConstellationTopics:"
- "setMinPrefix:"
- "setMustPrefixMatchLength:"
- "setObject:forKeyedSubscript:"
- "setOnScreen:"
- "setOverrideBlendAlpha:"
- "setOverrideBlendBeta:"
- "setOverrideBlendGamma:"
- "setOverrideConstellationMinCount:"
- "setOverrideConstellationMinWeight:"
- "setOverrideEnableCoreNLPTagging:"
- "setPartsOfSpeechToTexts:"
- "setPortraitId:"
- "setPreferredSceneIdentifiers:"
- "setQuery:"
- "setRawHTML:"
- "setRelatedItems:"
- "setRemoteObjectInterface:"
- "setRequestFingerprint:"
- "setRequestType:"
- "setResponseDate:"
- "setResults:"
- "setResultsNeedFiltering:"
- "setSceneIdentifier:"
- "setSnapshot:"
- "setString:"
- "setTags:"
- "setText:"
- "setTextIsRaw:"
- "setTiming:"
- "setTitle:"
- "setTopicId:"
- "setTopk:"
- "setType:"
- "setUiElements:"
- "setUrl:"
- "setUrls:"
- "setUuid:"
- "setWithArray:"
- "setWithCapacity:"
- "setWithObjects:"
- "setWithSet:"
- "sharedMemorySize"
- "shutdownService"
- "shutdownServiceWithReply:"
- "signal"
- "snapshot"
- "statusWithReply:"
- "string:withCount:"
- "stringWithFormat:"
- "subarrayWithRange:"
- "substringFromIndex:"
- "substringToIndex:"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "text"
- "timeIntervalBetweenMachTime:andMachTime:"
- "timeIntervalSinceNow"
- "timeoutError"
- "tryAcquireNeedsIncPending:"
- "tryAcquireServiceSemaphoreNeedsIncPending:"
- "uiElements"
- "updateCachedCapabilitiesWithReply:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8i16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"CKContextSemaphore\">16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@16B24"
- "v28@0:8Q16B24"
- "v32@0:8@\"CKContextRequest\"16@?<v@?@\"CKContextResponse\">24"
- "v32@0:8@\"CKContextRequest\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"CKContextResponse\"@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?@\"NSError\">24"
- "v32@0:8Q16@?<v@?@\"NSSet\"@\"NSString\"@\"NSError\">24"
- "v32@0:8{CGPoint=dd}16"
- "v32@0:8{CGSize=dd}16"
- "v36@0:8Q16@24B32"
- "v36@0:8Q16B24@28"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v44@0:8@16Q24@32B40"
- "v44@0:8Q16B24Q28@36"
- "v48@0:8@16@24Q32@?40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v56@0:8@\"NSString\"16Q24Q32Q40Q48"
- "v56@0:8@16Q24Q32Q40Q48"
- "v72@0:8@\"NSString\"16@\"CKContextResult\"24Q32Q40Q48Q56Q64"
- "v72@0:8@16@24Q32Q40Q48Q56Q64"
- "v76@0:8@\"NSString\"16Q24Q32@\"NSArray\"40B48Q52Q60Q68"
- "v76@0:8@16Q24Q32@40B48Q52Q60Q68"
- "valueForKey:"
- "waitFor:"
- "waitUntilDate:"
- "warmUpForRequestType:withReply:"
- "whitespaceAndNewlineCharacterSet"
- "whitespaceCharacterSet"
- "workWithServiceSemaphore:"
- "xpcConnection"
- "{CGPoint=\"x\"d\"y\"d}"
- "{CGPoint=dd}16@0:8"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}16@0:8"

```
