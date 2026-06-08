## IntelligentRouting

> `/System/Library/PrivateFrameworks/IntelligentRouting.framework/IntelligentRouting`

```diff

-124.0.1.0.0
-  __TEXT.__text: 0xce04
-  __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_methlist: 0x136c
+125.0.6.0.0
+  __TEXT.__text: 0xd164
+  __TEXT.__objc_methlist: 0x13ec
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x13d2
-  __TEXT.__gcc_except_tab: 0x80
+  __TEXT.__cstring: 0x147b
+  __TEXT.__gcc_except_tab: 0x6c
   __TEXT.__oslogstring: 0xdbd
-  __TEXT.__unwind_info: 0x430
-  __TEXT.__objc_classname: 0x194
-  __TEXT.__objc_methname: 0x1e84
-  __TEXT.__objc_methtype: 0x5c4
-  __TEXT.__objc_stubs: 0x14c0
-  __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x3d0
+  __TEXT.__unwind_info: 0x420
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x500
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x770
+  __DATA_CONST.__objc_selrefs: 0x788
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x1c0
+  __DATA_CONST.__got: 0xf8
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x17a0
-  __AUTH_CONST.__objc_const: 0x1db0
+  __AUTH_CONST.__cfstring: 0x1800
+  __AUTH_CONST.__objc_const: 0x1e70
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x104
+  __DATA.__objc_ivar: 0x114
   __DATA.__data: 0x248
   __DATA_DIRTY.__objc_data: 0x5a0
   __DATA_DIRTY.__bss: 0x8

   - /System/Library/PrivateFrameworks/IntelligentRoutingServices.framework/IntelligentRoutingServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2DF0F158-EB63-37BF-9A38-AFE45D5A8084
-  Functions: 381
-  Symbols:   1333
-  CStrings:  920
+  UUID: 678BBF79-2F4D-31A5-9ED3-2BAA4A90EEB0
+  Functions: 414
+  Symbols:   1424
+  CStrings:  482
 
Symbols:
+ +[IRSession _isCandidateValid:]
+ +[IRSession _isEventValid:forSuggestionTarget:]
+ -[IRHomeSuggestionTarget accessoryServiceUUID]
+ -[IRHomeSuggestionTarget homeUUID]
+ -[IRHomeSuggestionTarget initWithTargetUUID:type:targetName:accessoryServiceUUID:homeUUID:]
+ -[IRHomeSuggestionTarget setAccessoryServiceUUID:]
+ -[IRHomeSuggestionTarget setHomeUUID:]
+ -[IRHomeSuggestionTarget setTargetName:]
+ -[IRHomeSuggestionTarget targetName]
+ -[IRSession _invalidate]
+ -[IRSession delegateQueue]
+ -[IRSession setDelegateQueue:]
+ GCC_except_table62
+ _IRBundleIdentifierHomed
+ _IRBundleIdentifierIntelligenceFlowd
+ _IRContextMetadataMicroLocationModelCategoryKey
+ _OBJC_IVAR_$_IRHomeSuggestionTarget._accessoryServiceUUID
+ _OBJC_IVAR_$_IRHomeSuggestionTarget._homeUUID
+ _OBJC_IVAR_$_IRHomeSuggestionTarget._targetName
+ _OBJC_IVAR_$_IRSession._delegateQueue
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_9
+ ___23-[IRSession invalidate]_block_invoke
+ ___29-[IRSession deleteCandidate:]_block_invoke
+ ___29-[IRSession deleteCandidate:]_block_invoke.cold.1
+ ___30-[IRSession updateCandidates:]_block_invoke
+ ___30-[IRSession updateCandidates:]_block_invoke.cold.1
+ ___30-[IRSession updateCandidates:]_block_invoke.cold.2
+ ___31-[IRSession _didUpdateContext:]_block_invoke
+ ___34-[IRSession requestCurrentContext]_block_invoke
+ ___34-[IRSession requestCurrentContext]_block_invoke.cold.1
+ ___34-[IRSession runWithConfiguration:]_block_invoke
+ ___34-[IRSession runWithConfiguration:]_block_invoke.cold.1
+ ___34-[IRSession runWithConfiguration:]_block_invoke.cold.2
+ ___35-[IRSession addEvent:forCandidate:]_block_invoke
+ ___35-[IRSession addEvent:forCandidate:]_block_invoke.cold.1
+ ___38-[IRSession _sessionDidFailWithError:]_block_invoke
+ ___40-[IRSession _didSpotOnLocationComplete:]_block_invoke
+ ___44-[IRSession requestCurrentContextWithReply:]_block_invoke.64
+ ___44-[IRSession requestCurrentContextWithReply:]_block_invoke.65
+ ___44-[IRSession requestCurrentContextWithReply:]_block_invoke.65.cold.1
+ ___44-[IRSession requestCurrentContextWithReply:]_block_invoke.66
+ ___45-[IRSession donateEvent:forSuggestionTarget:]_block_invoke
+ ___45-[IRSession donateEvent:forSuggestionTarget:]_block_invoke.cold.1
+ ___45-[IRSession setSpotOnLocationWithParameters:]_block_invoke
+ ___45-[IRSession setSpotOnLocationWithParameters:]_block_invoke.cold.1
+ ___47-[IRSession requestCurrentContextWithBundleID:]_block_invoke
+ ___47-[IRSession requestCurrentContextWithBundleID:]_block_invoke.cold.1
+ ___47-[IRSession requestCurrentContextWithBundleID:]_block_invoke.cold.2
+ ___52-[IRSession requestCurrentContextWithTargets:reply:]_block_invoke.71
+ ___52-[IRSession requestCurrentContextWithTargets:reply:]_block_invoke.73
+ ___52-[IRSession requestCurrentContextWithTargets:reply:]_block_invoke.73.cold.1
+ ___52-[IRSession requestCurrentContextWithTargets:reply:]_block_invoke.74
+ ___64-[IRSession _didUpdateBundlesWithSignificantInteractionPattern:]_block_invoke
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e31_v24?0"IRContext"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ _dispatch_async
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_invalidate
+ _objc_msgSend$delegateQueue
+ _objc_msgSend$initWithTargetUUID:type:targetName:accessoryServiceUUID:homeUUID:
+ _objc_msgSend$setDelegateQueue:
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
- -[IRSession _isCandidateValid:]
- -[IRSession _isEventValid:forSuggestionTarget:]
- -[IRSession deleteCandidate:].cold.1
- -[IRSession requestCurrentContextWithBundleID:].cold.1
- -[IRSession requestCurrentContextWithBundleID:].cold.2
- -[IRSession requestCurrentContextWithReply:].cold.1
- -[IRSession requestCurrentContextWithTargets:reply:].cold.1
- -[IRSession requestCurrentContext].cold.1
- -[IRSession runWithConfiguration:].cold.1
- -[IRSession runWithConfiguration:].cold.2
- -[IRSession setSpotOnLocationWithParameters:].cold.1
- -[IRSession updateCandidates:].cold.1
- -[IRSession updateCandidates:].cold.2
- GCC_except_table43
- ___block_descriptor_40_e8_32bs_e31_v24?0"IRContext"8"NSError"16ls32l8
- _objc_msgSend$initWithTargetUUID:type:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "$"
+ "IRContextMetadataMicroLocationModelCategoryKey"
+ "com.apple.IntelligentRouting.delegate"
+ "com.apple.homed"
+ "com.apple.intelligenceflow.intelligenceflowd"
- "#"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<IRSessionDelegate>\""
- "@\"<IRXPCSessionClient>\""
- "@\"IRCandidate\""
- "@\"IRConfiguration\""
- "@\"IRServiceToken\""
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16q24"
- "@32@0:8q16@24"
- "@32@0:8q16q24"
- "@36@0:8@16B24@28"
- "@40@0:8:16@24@32"
- "@40@0:8@16q24@32"
- "@44@0:8@16B24@28@36"
- "@52@0:8@16B24@28@36@44"
- "@60@0:8@16q24@32@40B48B52B56"
- "@72@0:8q16@24@32@40@48d56@64"
- "@80@0:8q16@24@32@40@48d56@64@72"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8q16"
- "B32@0:8@16@24"
- "IRAppleTVControlEvent"
- "IRBundle"
- "IRCandidate"
- "IRCandidateResult"
- "IRConfiguration"
- "IRContext"
- "IREvent"
- "IRExtensions"
- "IRFrameworkBundle"
- "IRHomeEvent"
- "IRHomeSuggestion"
- "IRHomeSuggestionTarget"
- "IRMediaBundle"
- "IRMediaEvent"
- "IRNode"
- "IRServiceIdentifierMapping"
- "IRServiceParameters"
- "IRServiceToken"
- "IRSession"
- "IRSessionSpotOnLocationParameters"
- "IRXPCSessionClient"
- "IRXPCSessionServer"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "T#,R"
- "T@\"<IRSessionDelegate>\",W,N,V_delegate"
- "T@\"<IRXPCSessionClient>\",W,N,V_delegate"
- "T@\"IRCandidate\",R,N,V_candidate"
- "T@\"IRConfiguration\",C,N,V_configuration"
- "T@\"IRServiceToken\",R,C,N,V_serviceToken"
- "T@\"NSArray\",&,N,V_observerClientIdentifiers"
- "T@\"NSArray\",R,C,N,V_homeSuggestions"
- "T@\"NSDictionary\",R,N,V_metadata"
- "T@\"NSNumber\",&,N,V_sortingHint"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSSet\",R,C,N"
- "T@\"NSSet\",R,N,V_nodes"
- "T@\"NSString\",&,N,V_accessoryServiceUUID"
- "T@\"NSString\",&,N,V_avOutpuDeviceIdentifier"
- "T@\"NSString\",&,N,V_bundleID"
- "T@\"NSString\",&,N,V_contextIdentifier"
- "T@\"NSString\",&,N,V_homeUUID"
- "T@\"NSString\",&,N,V_idsIdentifier"
- "T@\"NSString\",&,N,V_name"
- "T@\"NSString\",&,N,V_presentationMode"
- "T@\"NSString\",&,N,V_rapportIdentifier"
- "T@\"NSString\",&,N,V_suggestionReason"
- "T@\"NSString\",&,N,V_targetName"
- "T@\"NSString\",&,N,V_targetUUID"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_bundleIdentifier"
- "T@\"NSString\",R,N,V_candidateIdentifier"
- "T@\"NSString\",R,N,V_classificationDescription"
- "T@\"NSString\",R,N,V_contextIdentifier"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_name"
- "T@\"NSString\",R,N,V_serviceIdentifier"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "TB,N,V_interrupted"
- "TB,N,V_isCallToAction"
- "TB,N,V_isConservativeFiltered"
- "TB,N,V_isEligibleApp"
- "TB,N,V_isLocal"
- "TB,N,V_isLockScreenControl"
- "TB,N,V_isOutsideApp"
- "TB,N,V_resetAllBrokerDiscoveredCandidates"
- "TB,R"
- "TB,R,N,V_isBannerClassificationUnavailable"
- "TQ,R"
- "Td,N,V_score"
- "Ti,N,V_token"
- "Tq,N,V_mode"
- "Tq,N,V_servicePackage"
- "Tq,N,V_type"
- "Tq,R,N,V_bundleType"
- "Tq,R,N,V_classification"
- "Tq,R,N,V_eventSubType"
- "Tq,R,N,V_eventType"
- "Tq,R,N,V_servicePackage"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_accessoryServiceUUID"
- "_addEvent:forCandidate:"
- "_avOutpuDeviceIdentifier"
- "_bundleID"
- "_bundleIdentifier"
- "_bundleType"
- "_candidate"
- "_candidateIdentifier"
- "_checkAndRecoverIfNeeded"
- "_classification"
- "_classificationDescription"
- "_classifyRoomName:accessoryNames:reply:"
- "_combineServiceIdentifier:withPersonaUniqueIdentifier:"
- "_configuration"
- "_connection"
- "_contextIdentifier"
- "_createNSXPCConnectionWithExportedObject:queue:"
- "_createResumedTemporaryNSXPCConnection"
- "_createServiceWithParameters:reply:"
- "_databaseExportwithReply:"
- "_delegate"
- "_deleteCandidate:"
- "_deleteDatabaseWithReply:"
- "_deleteService:"
- "_didSpotOnLocationComplete:"
- "_didUpdateBundlesWithSignificantInteractionPattern:"
- "_didUpdateContext:"
- "_donateEvent:forSuggestionTarget:"
- "_eventSubType"
- "_eventType"
- "_extractServiceIdentifierFromCombinedString:"
- "_getServiceTokensWithReply:"
- "_homeSuggestions"
- "_homeUUID"
- "_identifier"
- "_idsIdentifier"
- "_internalCandidateResults"
- "_interrupted"
- "_invalidate"
- "_isBannerClassificationUnavailable"
- "_isCallToAction"
- "_isCandidateValid:"
- "_isConservativeFiltered"
- "_isEligibleApp"
- "_isEventSubTypeValid:"
- "_isEventTypeValid:"
- "_isEventValid:forSuggestionTarget:"
- "_isLocal"
- "_isLockScreenControl"
- "_isOutsideApp"
- "_manageSessionAvailableNotificationObservation:"
- "_metadata"
- "_mode"
- "_name"
- "_nodes"
- "_notifySessionHasFailed:desc:"
- "_observerClientIdentifiers"
- "_presentationMode"
- "_queue"
- "_rapportIdentifier"
- "_requestCurrentContextWithBundleID:"
- "_requestCurrentContextWithReply:"
- "_requestCurrentContextWithTargets:reply:"
- "_resetAllBrokerDiscoveredCandidates"
- "_runWithConfiguration:"
- "_score"
- "_serverConnectionInterrupted"
- "_serverConnectionInvalidated"
- "_serviceIdentifier"
- "_serviceIdentifiersMapping"
- "_servicePackage"
- "_serviceToken"
- "_sessionDidFailWithError:"
- "_setQueue:"
- "_setSpotOnLocationWithParameters:"
- "_sortingHint"
- "_suggestionReason"
- "_targetName"
- "_targetUUID"
- "_terminateLLMServiceWithReply:"
- "_token"
- "_type"
- "_updateCandidates:"
- "addEvent:forCandidate:"
- "appendFormat:"
- "appendString:"
- "array"
- "arrayWithObjects:count:"
- "autorelease"
- "boolValue"
- "bundleForClass:"
- "candidateResults"
- "class"
- "classifyRoomName:accessoryNames:reply:"
- "componentsSeparatedByString:"
- "configuration"
- "conformsToProtocol:"
- "connection"
- "containsObject:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createServiceWithParameters:reply:"
- "d"
- "d16@0:8"
- "databaseExportwithReply:"
- "dealloc"
- "debugDescription"
- "decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "delegate"
- "deleteCandidate:"
- "deleteDatabaseWithReply:"
- "deleteService:"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "donateEvent:forSuggestionTarget:"
- "doubleValue"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "firstObject"
- "getServiceTokensWithReply:"
- "hash"
- "i"
- "i16@0:8"
- "init"
- "initWithBundleType:andIdentifier:"
- "initWithCandidate:classification:andClassificationDescription:"
- "initWithCandidate:classification:classificationDescription:sortingHint:isCallToAction:isLockScreenControl:isConservativeFiltered:"
- "initWithCandidateIdentifier:"
- "initWithCandidateResults:isBannerClassificationUnavailable:bundleIdentifier:"
- "initWithCandidateResults:isBannerClassificationUnavailable:bundleIdentifier:homeSuggestions:"
- "initWithCandidateResults:isBannerClassificationUnavailable:bundleIdentifier:homeSuggestions:metadata:"
- "initWithCoder:"
- "initWithDelegate:"
- "initWithEventType:eventSubType:"
- "initWithFormat:"
- "initWithIdentifier:"
- "initWithMachServiceName:options:"
- "initWithName:"
- "initWithObjects:"
- "initWithServiceIdentifier:servicePackage:"
- "initWithServicePackage:"
- "initWithServicePackage:observerClientIdentifiers:"
- "initWithServiceToken:"
- "initWithSet:copyItems:"
- "initWithTargetUUID:type:"
- "initWithType:targetUUID:targetName:accessoryServiceUUID:homeUUID:score:suggestionReason:"
- "initWithType:targetUUID:targetName:accessoryServiceUUID:homeUUID:score:suggestionReason:presentationMode:"
- "intValue"
- "interfaceWithProtocol:"
- "interrupted"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isServicePackageSupported:"
- "isServiceTokenValid:forClientIdentifier:"
- "new"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectForKeyedSubscript:"
- "observerClientIdentifiers"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "q"
- "q16@0:8"
- "queue"
- "release"
- "remoteObjectProxy"
- "requestCurrentContext"
- "requestCurrentContextWithBundleID:"
- "requestCurrentContextWithReply:"
- "requestCurrentContextWithTargets:reply:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "runWithConfiguration:"
- "self"
- "serviceTokenForServiceIdentifier:"
- "serviceTokenForServiceIdentifier:personaUniqueIdentifier:"
- "session:didFailWithError:"
- "session:didSpotOnLocationComplete:"
- "session:didUpdateBundlesWithSignificantInteractionPattern:"
- "session:didUpdateContext:"
- "setAccessoryServiceUUID:"
- "setAvOutpuDeviceIdentifier:"
- "setBundleID:"
- "setByAddingObject:"
- "setClass:forSelector:argumentIndex:ofReply:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setClassification:withDescription:"
- "setConfiguration:"
- "setConnection:"
- "setContextIdentifier:"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setHomeUUID:"
- "setIdsIdentifier:"
- "setInterrupted:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsCallToAction:"
- "setIsConservativeFiltered:"
- "setIsEligibleApp:"
- "setIsLocal:"
- "setIsLockScreenControl:"
- "setIsOutsideApp:"
- "setMode:"
- "setName:"
- "setObserverClientIdentifiers:"
- "setPresentationMode:"
- "setQueue:"
- "setRapportIdentifier:"
- "setRemoteObjectInterface:"
- "setResetAllBrokerDiscoveredCandidates:"
- "setScore:"
- "setServicePackage:"
- "setSortingHint:"
- "setSpotOnLocationWithParameters:"
- "setSuggestionReason:"
- "setTargetName:"
- "setTargetUUID:"
- "setToken:"
- "setType:"
- "setWithArray:"
- "setWithObject:"
- "setWithObjects:"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "terminateLLMServiceWithReply:"
- "token"
- "updateCandidate:"
- "updateCandidates:"
- "updateNodes:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"IRCandidate\"16"
- "v24@0:8@\"IRConfiguration\"16"
- "v24@0:8@\"IRServiceToken\"16"
- "v24@0:8@\"IRSessionSpotOnLocationParameters\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"IRContext\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v32@0:8@\"IREvent\"16@\"IRCandidate\"24"
- "v32@0:8@\"IRHomeEvent\"16@\"IRHomeSuggestionTarget\"24"
- "v32@0:8@\"IRServiceParameters\"16@?<v@?@\"IRServiceToken\"@\"NSError\">24"
- "v32@0:8@\"NSSet\"16@?<v@?@\"IRContext\"@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8q16@24"
- "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"NSString\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "zone"

```
