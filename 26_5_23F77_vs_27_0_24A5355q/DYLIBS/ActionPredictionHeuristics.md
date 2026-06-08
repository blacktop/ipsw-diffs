## ActionPredictionHeuristics

> `/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/ActionPredictionHeuristics`

```diff

-627.13.0.1.0
-  __TEXT.__text: 0x6400
-  __TEXT.__auth_stubs: 0x440
+658.0.9.0.0
+  __TEXT.__text: 0x5d58
   __TEXT.__objc_methlist: 0x32c
-  __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x230
-  __TEXT.__cstring: 0x51c
+  __TEXT.__const: 0x80
+  __TEXT.__gcc_except_tab: 0x224
+  __TEXT.__cstring: 0x524
   __TEXT.__oslogstring: 0x87e
-  __TEXT.__unwind_info: 0x2d8
-  __TEXT.__objc_classname: 0xe4
-  __TEXT.__objc_methname: 0xc85
-  __TEXT.__objc_methtype: 0x3c4
-  __TEXT.__objc_stubs: 0xb40
-  __DATA_CONST.__got: 0x180
+  __TEXT.__unwind_info: 0x158
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x220
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_selrefs: 0x3b8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x230
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x660
   __AUTH_CONST.__cfstring: 0x1a0
   __AUTH_CONST.__objc_const: 0x630
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x38
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x2c0

   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FCCA2794-6B11-32CD-BCD5-8280FB1753B5
-  Functions: 213
-  Symbols:   879
-  CStrings:  311
+  UUID: 8031B817-ECFD-3A8C-AC13-9D3180D12596
+  Functions: 211
+  Symbols:   875
+  CStrings:  128
 
Symbols:
+ ___60+[ATXActionPredictionHeuristics actionsWithLocationManager:]_block_invoke.32
+ ___60+[ATXActionPredictionHeuristics actionsWithLocationManager:]_block_invoke.36
+ ___63-[ATXInformationHeuristics getResultsFromHeuristicInterpreter:]_block_invoke.54
+ ___63-[ATXInformationHeuristics getResultsFromHeuristicInterpreter:]_block_invoke.54.cold.1
+ ___block_literal_global.31
+ ___block_literal_global.39
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- ___60+[ATXActionPredictionHeuristics actionsWithLocationManager:]_block_invoke.38
- ___60+[ATXActionPredictionHeuristics actionsWithLocationManager:]_block_invoke.42
- ___63-[ATXInformationHeuristics getResultsFromHeuristicInterpreter:]_block_invoke.60
- ___63-[ATXInformationHeuristics getResultsFromHeuristicInterpreter:]_block_invoke.60.cold.1
- ___block_literal_global.37
- ___block_literal_global.45
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x25
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<ATXContextHeuristicsDelegate>\""
- "@\"<ATXInformationHeuristicsDelegate>\""
- "@\"ATXContextHeuristicCache\""
- "@\"ATXContextHeuristicResult\"24@0:8@\"<ATXContextHeuristicsEnvironment>\"16"
- "@\"ATXHeuristicDevice\""
- "@\"ATXHeuristicDevice\"16@0:8"
- "@\"ATXInformationHeuristicRefreshTimeTrigger\""
- "@\"ATXLocationManager\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\"16@0:8"
- "@\"NSString\"16@0:8"
- "@\"_PASSimpleCoalescingTimer\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "ATXActionPredictionHeuristics"
- "ATXContextHeuristicProtocol"
- "ATXContextHeuristics"
- "ATXContextHeuristicsEnvironment"
- "ATXInformationHeuristicRefreshTriggerDelegate"
- "ATXInformationHeuristics"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "HeuristicInterpreterProtocol"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<ATXContextHeuristicsDelegate>\",W,N,V_delegate"
- "T@\"<ATXInformationHeuristicsDelegate>\",W,N,V_delegate"
- "T@\"ATXHeuristicDevice\",R,N"
- "T@\"ATXHeuristicDevice\",R,N,V_heuristicDevice"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_coalescedRefreshOperation"
- "_criteriaForRefreshJobOnDate:"
- "_delegate"
- "_earliestCacheRefreshTimeTrigger"
- "_heuristicDevice"
- "_heuristicRefreshTriggers"
- "_heuristicsPendingRefresh"
- "_locationManager"
- "_queue"
- "_queue_cleanupTimeTriggers"
- "_queue_refreshResultsForAllHeuristicsWithCompletionHandler:"
- "_queue_refreshResultsForHeuristics:"
- "_queue_sendRelevantSuggestionsToBlending"
- "_queue_updateHeuristicName:withRefreshTriggers:"
- "_refreshResultsForAllHeuristics:completionHandler:"
- "_refreshResultsForHeuristics:"
- "_removeRefreshCTSJob"
- "_resultsCache"
- "_setRefreshCTSJobForCriteria:fireDate:forHeuristics:"
- "_setRefreshCTSJobForCriteria:forHeuristics:"
- "action"
- "actionMakers"
- "actionsAndExpirersForHeuristicsExcept:bundlePath:now:dataSourcesEndpoint:reply:"
- "actionsWithLocationManager:"
- "addCacheExpirerNotification:"
- "addObject:"
- "addObserverForName:object:queue:usingBlock:"
- "additionalRefreshTriggers"
- "allKeys"
- "allRelevantSuggestionsForDate:"
- "arrayWithObjects:count:"
- "autorelease"
- "class"
- "compare:"
- "conformsToProtocol:"
- "containsObject:"
- "contextHeuristics:didUpdateSuggestions:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "criteria"
- "date"
- "debugDescription"
- "defaultCenter"
- "delegate"
- "description"
- "donateSuggestions:forHeuristic:"
- "earlierDate:"
- "enumerateObjectsUsingBlock:"
- "evictBefore:"
- "expirers"
- "fireDate"
- "firstExpirationDate"
- "getResultsFromHeuristicInterpreter:"
- "hasFailed"
- "hash"
- "heuristicDevice"
- "heuristicName"
- "heuristicResultWithEnvironment:"
- "heuristicsCached"
- "informationHeuristicRefreshTrigger:didTriggerRefreshForHeuristics:"
- "informationHeuristics:didUpdateSuggestions:forHeuristic:"
- "init"
- "initWithArray:"
- "initWithCapacity:"
- "initWithDevice:"
- "initWithFireDate:"
- "initWithFormat:"
- "initWithLocationManager:"
- "initWithObjects:"
- "initWithQueue:operation:"
- "initWithServiceName:"
- "interfaceWithProtocol:"
- "invalidate"
- "isClassCLocked"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRelevant:"
- "listenerEndpoint"
- "mutableCopy"
- "nextCacheExpirationDate"
- "nextChangeAfterDate:"
- "now"
- "objectForKey:found:"
- "objectForKeyedSubscript:"
- "pathForResource:ofType:isDirectory:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "permanentRefreshTriggers"
- "ping:"
- "refreshResultsForAllHeuristicsPendingRefreshWithCompletionHandler:"
- "refreshResultsForAllHeuristicsWithCompletionHandler:"
- "refreshTriggers"
- "registeredHeuristics"
- "release"
- "removeAllObjects"
- "removeObject:"
- "respondsToSelector:"
- "resultsForInformationHeuristics:bundlePath:now:dataSourcesEndpoint:reply:"
- "resume"
- "retain"
- "retainCount"
- "runAfterDelaySeconds:coalescingBehavior:"
- "self"
- "setByAddingObjectsFromSet:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setDelegate:"
- "setObject:expirers:forKey:"
- "setRemoteObjectInterface:"
- "setSuggestions:forKey:"
- "setWithObjects:"
- "sharedInstance"
- "sortWithOptions:usingComparator:"
- "sourceIdentifierForHeuristicWithName:"
- "startTriggeringRefreshForHeuristicIfNotAlready:"
- "stopTriggeringRefreshForAllHeuristics"
- "stopTriggeringRefreshForHeuristicIfAlready:"
- "suggestions"
- "superclass"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "timeIntervalSinceDate:"
- "timeIntervalSinceNow"
- "unionSet:"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v28@0:8B16@?20"
- "v32@0:8@\"ATXInformationHeuristicRefreshTrigger\"16@\"NSSet\"24"
- "v32@0:8@16@24"
- "v40@0:8@16@24@32"
- "v56@0:8@\"NSSet\"16@\"NSString\"24@\"NSDate\"32@\"NSXPCListenerEndpoint\"40@?<v@?@\"NSArray\"@\"NSError\">48"
- "v56@0:8@\"NSSet\"16@\"NSString\"24@\"NSDate\"32@\"NSXPCListenerEndpoint\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"
- "zone"

```
