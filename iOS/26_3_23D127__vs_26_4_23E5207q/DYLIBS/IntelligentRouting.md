## IntelligentRouting

> `/System/Library/PrivateFrameworks/IntelligentRouting.framework/IntelligentRouting`

```diff

-97.0.3.0.0
-  __TEXT.__text: 0x9f84
+123.0.2.0.2
+  __TEXT.__text: 0xce04
   __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_methlist: 0x1104
+  __TEXT.__objc_methlist: 0x136c
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0xffb
+  __TEXT.__cstring: 0x13d2
   __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__oslogstring: 0x9a1
-  __TEXT.__unwind_info: 0x338
-  __TEXT.__objc_classname: 0x169
-  __TEXT.__objc_methname: 0x1962
-  __TEXT.__objc_methtype: 0x48c
-  __TEXT.__objc_stubs: 0x10c0
-  __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x240
-  __DATA_CONST.__objc_classlist: 0x88
+  __TEXT.__oslogstring: 0xdbd
+  __TEXT.__unwind_info: 0x430
+  __TEXT.__objc_classname: 0x194
+  __TEXT.__objc_methname: 0x1e84
+  __TEXT.__objc_methtype: 0x5c4
+  __TEXT.__objc_stubs: 0x14c0
+  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__const: 0x3d0
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x658
+  __DATA_CONST.__objc_selrefs: 0x770
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x88
+  __DATA_CONST.__objc_superrefs: 0x98
   __AUTH_CONST.__auth_got: 0x1c0
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x1240
-  __AUTH_CONST.__objc_const: 0x1a00
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xdc
+  __AUTH_CONST.__cfstring: 0x17a0
+  __AUTH_CONST.__objc_const: 0x1db0
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x104
   __DATA.__data: 0x248
-  __DATA_DIRTY.__objc_data: 0x4b0
+  __DATA_DIRTY.__objc_data: 0x5a0
   __DATA_DIRTY.__bss: 0x8
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/IntelligentRoutingServices.framework/IntelligentRoutingServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 21BD5591-F2F4-38CA-9942-E933629E37D6
-  Functions: 324
-  Symbols:   1120
-  CStrings:  756
+  UUID: 88A37890-CE13-3115-8AA5-4F7B26CE7A42
+  Functions: 381
+  Symbols:   1333
+  CStrings:  920
 
Symbols:
+ +[IRHomeSuggestion supportsSecureCoding]
+ +[IRHomeSuggestionTarget supportsSecureCoding]
+ +[IRSession classifyRoomName:accessoryNames:reply:]
+ +[IRSession terminateLLMServiceWithReply:]
+ -[IRContext homeSuggestions]
+ -[IRContext initWithCandidateResults:isBannerClassificationUnavailable:bundleIdentifier:homeSuggestions:]
+ -[IRContext initWithCandidateResults:isBannerClassificationUnavailable:bundleIdentifier:homeSuggestions:metadata:]
+ -[IRContext metadata]
+ -[IRHomeSuggestion .cxx_destruct]
+ -[IRHomeSuggestion accessoryServiceUUID]
+ -[IRHomeSuggestion copyWithZone:]
+ -[IRHomeSuggestion description]
+ -[IRHomeSuggestion encodeWithCoder:]
+ -[IRHomeSuggestion hash]
+ -[IRHomeSuggestion homeUUID]
+ -[IRHomeSuggestion initWithCoder:]
+ -[IRHomeSuggestion initWithType:targetUUID:targetName:accessoryServiceUUID:homeUUID:score:suggestionReason:]
+ -[IRHomeSuggestion initWithType:targetUUID:targetName:accessoryServiceUUID:homeUUID:score:suggestionReason:presentationMode:]
+ -[IRHomeSuggestion isEqual:]
+ -[IRHomeSuggestion presentationMode]
+ -[IRHomeSuggestion score]
+ -[IRHomeSuggestion setAccessoryServiceUUID:]
+ -[IRHomeSuggestion setHomeUUID:]
+ -[IRHomeSuggestion setPresentationMode:]
+ -[IRHomeSuggestion setScore:]
+ -[IRHomeSuggestion setSuggestionReason:]
+ -[IRHomeSuggestion setTargetName:]
+ -[IRHomeSuggestion setTargetUUID:]
+ -[IRHomeSuggestion setType:]
+ -[IRHomeSuggestion suggestionReason]
+ -[IRHomeSuggestion targetName]
+ -[IRHomeSuggestion targetUUID]
+ -[IRHomeSuggestion type]
+ -[IRHomeSuggestionTarget .cxx_destruct]
+ -[IRHomeSuggestionTarget copyWithZone:]
+ -[IRHomeSuggestionTarget description]
+ -[IRHomeSuggestionTarget encodeWithCoder:]
+ -[IRHomeSuggestionTarget hash]
+ -[IRHomeSuggestionTarget initWithCoder:]
+ -[IRHomeSuggestionTarget initWithTargetUUID:type:]
+ -[IRHomeSuggestionTarget isEqual:]
+ -[IRHomeSuggestionTarget setTargetUUID:]
+ -[IRHomeSuggestionTarget setType:]
+ -[IRHomeSuggestionTarget targetUUID]
+ -[IRHomeSuggestionTarget type]
+ -[IRSession _isEventValid:forSuggestionTarget:]
+ -[IRSession donateEvent:forSuggestionTarget:]
+ -[IRSession requestCurrentContextWithTargets:reply:]
+ -[IRSession requestCurrentContextWithTargets:reply:].cold.1
+ -[IRSession runWithConfiguration:].cold.2
+ GCC_except_table43
+ _IRBundleIdentifierAVKitRoutePickerViewService
+ _IRBundleIdentifierBlueAtlas
+ _IRBundleIdentifierControlCenter
+ _IRBundleIdentifierHome
+ _IRBundleIdentifierHomeIntegrationTests
+ _IRBundleIdentifierHomeKit
+ _IRBundleIdentifierHomeTestKitTests
+ _IRBundleIdentifierHomeUtil
+ _IRBundleIdentifierHomeWidgetInteractive
+ _IRBundleIdentifierHomeWidgetTV
+ _IRBundleIdentifierIntelligentRoutingClient
+ _IRBundleIdentifierIntelligentRoutingClientAppleTVControl
+ _IRBundleIdentifierIntelligentRoutingClientHome
+ _IRBundleIdentifierIntelligentRoutingClientMedia
+ _IRBundleIdentifierIntelligentRoutingHostTests
+ _IRBundleIdentifierIntelligentRoutingHostTestsAppleTVControl
+ _IRBundleIdentifierIntelligentRoutingHostTestsHome
+ _IRBundleIdentifierIntelligentRoutingHostTestsMedia
+ _IRBundleIdentifierMediaRemote
+ _IRBundleIdentifierMusic
+ _IRBundleIdentifierMusicUIService
+ _IRBundleIdentifierNanoHome
+ _IRBundleIdentifierNeighborhoodActivityConduitService
+ _IRBundleIdentifierRoverApp
+ _IRBundleIdentifierSiriAssistantService
+ _IRBundleIdentifierSpringboard
+ _IRBundleIdentifierTVRemote
+ _IRBundleIdentifierTVSystemUIService
+ _IRBundleIdentifierTelephonyUtilities
+ _IRContextMetadataIsMicroLocationMapValidKey
+ _IRContextMetadataIsMicroLocationPredictionValidKey
+ _IRContextMetadataIsPeripheralAvailableKey
+ _IRHomeSuggestionPresentationModeAuto
+ _IRHomeSuggestionPresentationModeExplicit
+ _IRHomeSuggestionPresentationModeImplicit
+ _IRHomeSuggestionPresentationModeUnknown
+ _IRHomeSuggestionReQueryNotification
+ _IRHomeSuggestionTypeToString
+ _OBJC_CLASS_$_IRHomeSuggestion
+ _OBJC_CLASS_$_IRHomeSuggestionTarget
+ _OBJC_IVAR_$_IRContext._homeSuggestions
+ _OBJC_IVAR_$_IRContext._metadata
+ _OBJC_IVAR_$_IRHomeSuggestion._accessoryServiceUUID
+ _OBJC_IVAR_$_IRHomeSuggestion._homeUUID
+ _OBJC_IVAR_$_IRHomeSuggestion._presentationMode
+ _OBJC_IVAR_$_IRHomeSuggestion._score
+ _OBJC_IVAR_$_IRHomeSuggestion._suggestionReason
+ _OBJC_IVAR_$_IRHomeSuggestion._targetName
+ _OBJC_IVAR_$_IRHomeSuggestion._targetUUID
+ _OBJC_IVAR_$_IRHomeSuggestion._type
+ _OBJC_IVAR_$_IRHomeSuggestionTarget._targetUUID
+ _OBJC_IVAR_$_IRHomeSuggestionTarget._type
+ _OBJC_METACLASS_$_IRHomeSuggestion
+ _OBJC_METACLASS_$_IRHomeSuggestionTarget
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ __OBJC_$_CLASS_METHODS_IRHomeSuggestion
+ __OBJC_$_CLASS_METHODS_IRHomeSuggestionTarget
+ __OBJC_$_CLASS_PROP_LIST_IRHomeSuggestion
+ __OBJC_$_CLASS_PROP_LIST_IRHomeSuggestionTarget
+ __OBJC_$_INSTANCE_METHODS_IRHomeSuggestion
+ __OBJC_$_INSTANCE_METHODS_IRHomeSuggestionTarget
+ __OBJC_$_INSTANCE_VARIABLES_IRHomeSuggestion
+ __OBJC_$_INSTANCE_VARIABLES_IRHomeSuggestionTarget
+ __OBJC_$_PROP_LIST_IRHomeSuggestion
+ __OBJC_$_PROP_LIST_IRHomeSuggestionTarget
+ __OBJC_CLASS_PROTOCOLS_$_IRHomeSuggestion
+ __OBJC_CLASS_PROTOCOLS_$_IRHomeSuggestionTarget
+ __OBJC_CLASS_RO_$_IRHomeSuggestion
+ __OBJC_CLASS_RO_$_IRHomeSuggestionTarget
+ __OBJC_METACLASS_RO_$_IRHomeSuggestion
+ __OBJC_METACLASS_RO_$_IRHomeSuggestionTarget
+ ___42+[IRSession terminateLLMServiceWithReply:]_block_invoke
+ ___44-[IRSession requestCurrentContextWithReply:]_block_invoke.cold.1
+ ___51+[IRSession classifyRoomName:accessoryNames:reply:]_block_invoke
+ ___52-[IRSession requestCurrentContextWithTargets:reply:]_block_invoke
+ ___52-[IRSession requestCurrentContextWithTargets:reply:]_block_invoke.cold.1
+ ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSString"8"NSError"16ls40l8s32l8
+ _objc_msgSend$_classifyRoomName:accessoryNames:reply:
+ _objc_msgSend$_donateEvent:forSuggestionTarget:
+ _objc_msgSend$_isEventValid:forSuggestionTarget:
+ _objc_msgSend$_requestCurrentContextWithTargets:reply:
+ _objc_msgSend$_terminateLLMServiceWithReply:
+ _objc_msgSend$accessoryServiceUUID
+ _objc_msgSend$array
+ _objc_msgSend$decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:
+ _objc_msgSend$dictionary
+ _objc_msgSend$doubleValue
+ _objc_msgSend$homeSuggestions
+ _objc_msgSend$homeUUID
+ _objc_msgSend$initWithCandidateResults:isBannerClassificationUnavailable:bundleIdentifier:homeSuggestions:
+ _objc_msgSend$initWithCandidateResults:isBannerClassificationUnavailable:bundleIdentifier:homeSuggestions:metadata:
+ _objc_msgSend$initWithTargetUUID:type:
+ _objc_msgSend$initWithType:targetUUID:targetName:accessoryServiceUUID:homeUUID:score:suggestionReason:presentationMode:
+ _objc_msgSend$metadata
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$presentationMode
+ _objc_msgSend$score
+ _objc_msgSend$setAccessoryServiceUUID:
+ _objc_msgSend$setByAddingObject:
+ _objc_msgSend$setHomeUUID:
+ _objc_msgSend$setPresentationMode:
+ _objc_msgSend$setScore:
+ _objc_msgSend$setSuggestionReason:
+ _objc_msgSend$setTargetName:
+ _objc_msgSend$setTargetUUID:
+ _objc_msgSend$setType:
+ _objc_msgSend$suggestionReason
+ _objc_msgSend$targetName
+ _objc_msgSend$targetUUID
+ _objc_msgSend$type
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x24
+ _objc_retain_x25
- -[IRNode HKAccessoryUniqueIdentifier]
- -[IRNode HKRoomUniqueIdentifier]
- -[IRNode setHKAccessoryUniqueIdentifier:]
- -[IRNode setHKRoomUniqueIdentifier:]
- GCC_except_table35
- _OBJC_IVAR_$_IRNode._HKAccessoryUniqueIdentifier
- _OBJC_IVAR_$_IRNode._HKRoomUniqueIdentifier
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$HKAccessoryUniqueIdentifier
- _objc_msgSend$HKRoomUniqueIdentifier
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x26
- _objc_retain_x3
CStrings:
+ ", accessoryServiceUUID: %@"
+ ", homeSuggestions: %@"
+ ", homeUUID: %@"
+ ", metadata: %@"
+ ", presentationMode: %@"
+ ", score: %@"
+ ", suggestionReason: %@"
+ ", targetName: %@"
+ ", targetUUID: %@"
+ ", type: %@"
+ "@\"NSDictionary\""
+ "@44@0:8@16B24@28@36"
+ "@52@0:8@16B24@28@36@44"
+ "@72@0:8q16@24@32@40@48d56@64"
+ "@80@0:8q16@24@32@40@48d56@64@72"
+ "Accessory"
+ "Auto"
+ "Donate event for suggestion target has failed"
+ "Explicit"
+ "Home service package is not allowed to be in OnEvents Mode"
+ "IRContextMetadataIsMicroLocationMapValidKey"
+ "IRContextMetadataIsMicroLocationPredictionValidKey"
+ "IRContextMetadataIsPeripheralAvailableKey"
+ "IRHomeSuggestion"
+ "IRHomeSuggestionReQueryNotification"
+ "IRHomeSuggestionTarget"
+ "Implicit"
+ "LocationAuto"
+ "LocationAutoRejected"
+ "LocationExplicitConfirmationAccepted"
+ "LocationExplicitConfirmationRejected"
+ "LocationRoomUserResolving"
+ "Requesting current context with targets has failed"
+ "Room"
+ "Scene"
+ "T@\"NSArray\",R,C,N,V_homeSuggestions"
+ "T@\"NSDictionary\",R,N,V_metadata"
+ "T@\"NSString\",&,N,V_accessoryServiceUUID"
+ "T@\"NSString\",&,N,V_homeUUID"
+ "T@\"NSString\",&,N,V_presentationMode"
+ "T@\"NSString\",&,N,V_suggestionReason"
+ "T@\"NSString\",&,N,V_targetName"
+ "T@\"NSString\",&,N,V_targetUUID"
+ "Td,N,V_score"
+ "Tq,N,V_type"
+ "[ErrorId - IRSession donateEvent error] [IRSession]: cant donate event: %@ for target: %@, isSessionInvalidated: %@"
+ "[ErrorId - IRSession request current context with targets error] [IRSession]: cant request current context with targets, configuration: %@, targets: %@, isSessionInvalidated: %@"
+ "[ErrorId - IRSession run error] [IRSession]: Home service package is not allowed to be in OnEvents mode"
+ "[ErrorId - Request current context with replay error] requestCurrentContextWithReply failed with error: %@"
+ "[ErrorId - Request current context with targets error] requestCurrentContextWithTargets failed with error: %@"
+ "[IRSession]: LLM service termination completed: %@"
+ "[IRSession]: classifying room name: %@"
+ "[IRSession]: donating event: %@, for suggestion target: %@"
+ "[IRSession]: requestCurrentContextWithReply returned with context: %@"
+ "[IRSession]: requestCurrentContextWithTargets returned with context: %@"
+ "[IRSession]: requestCurrentContextWithTargets with %@ targets"
+ "[IRSession]: room classification completed: %@"
+ "[IRSession]: terminating LLM service"
+ "_accessoryServiceUUID"
+ "_classifyRoomName:accessoryNames:reply:"
+ "_donateEvent:forSuggestionTarget:"
+ "_homeSuggestions"
+ "_homeUUID"
+ "_isEventValid:forSuggestionTarget:"
+ "_metadata"
+ "_presentationMode"
+ "_requestCurrentContextWithTargets:reply:"
+ "_score"
+ "_suggestionReason"
+ "_targetName"
+ "_targetUUID"
+ "_terminateLLMServiceWithReply:"
+ "_type"
+ "accessoryServiceUUID"
+ "array"
+ "classifyRoomName:accessoryNames:reply:"
+ "com.apple.Home"
+ "com.apple.Home.HomeWidget.Interactive"
+ "com.apple.Home.HomeWidgetTV"
+ "com.apple.HomeIntegrationTests.xctrunner"
+ "com.apple.HomeKit"
+ "com.apple.HomeTestKitTests.xctrunner"
+ "com.apple.NanoHome"
+ "com.apple.TVSystemUIService"
+ "com.apple.assistant_service"
+ "com.apple.homeutil"
+ "d"
+ "d16@0:8"
+ "decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:"
+ "dictionary"
+ "donateEvent:forSuggestionTarget:"
+ "doubleValue"
+ "homeSuggestions"
+ "homeUUID"
+ "initWithCandidateResults:isBannerClassificationUnavailable:bundleIdentifier:homeSuggestions:"
+ "initWithCandidateResults:isBannerClassificationUnavailable:bundleIdentifier:homeSuggestions:metadata:"
+ "initWithTargetUUID:type:"
+ "initWithType:targetUUID:targetName:accessoryServiceUUID:homeUUID:score:suggestionReason:"
+ "initWithType:targetUUID:targetName:accessoryServiceUUID:homeUUID:score:suggestionReason:presentationMode:"
+ "metadata"
+ "numberWithDouble:"
+ "numberWithUnsignedInteger:"
+ "presentationMode"
+ "requestCurrentContextWithTargets:reply:"
+ "score"
+ "setAccessoryServiceUUID:"
+ "setByAddingObject:"
+ "setHomeUUID:"
+ "setPresentationMode:"
+ "setScore:"
+ "setSuggestionReason:"
+ "setTargetName:"
+ "setTargetUUID:"
+ "setType:"
+ "suggestionReason"
+ "targetName"
+ "targetUUID"
+ "terminateLLMServiceWithReply:"
+ "type"
+ "v24@0:8d16"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v32@0:8@\"IRHomeEvent\"16@\"IRHomeSuggestionTarget\"24"
+ "v32@0:8@\"NSSet\"16@?<v@?@\"IRContext\"@\"NSError\">24"
+ "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v40@0:8@16@24@?32"
- ", HKAccessoryUniqueIdentifier: %@"
- ", HKRoomUniqueIdentifier: %@"
- "@\"NSUUID\""
- "HKAccessoryUniqueIdentifier"
- "HKRoomUniqueIdentifier"
- "T@\"NSUUID\",&,N,V_HKAccessoryUniqueIdentifier"
- "T@\"NSUUID\",&,N,V_HKRoomUniqueIdentifier"
- "UserInteraction"
- "_HKAccessoryUniqueIdentifier"
- "_HKRoomUniqueIdentifier"
- "setHKAccessoryUniqueIdentifier:"
- "setHKRoomUniqueIdentifier:"

```
