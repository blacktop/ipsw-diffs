## DASDaemon

> `/System/Library/PrivateFrameworks/DASDaemon.framework/DASDaemon`

```diff

-2109.120.16.0.0
-  __TEXT.__text: 0x94f8
-  __TEXT.__auth_stubs: 0x2e0
+2463.0.0.502.1
+  __TEXT.__text: 0x8ce8
   __TEXT.__objc_methlist: 0x470
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__cstring: 0xfa7
-  __TEXT.__unwind_info: 0x1c8
-  __TEXT.__objc_classname: 0x6b
-  __TEXT.__objc_methname: 0xf89
-  __TEXT.__objc_methtype: 0x19b
-  __TEXT.__objc_stubs: 0x10e0
-  __DATA_CONST.__got: 0xd8
+  __TEXT.__cstring: 0x1022
+  __TEXT.__unwind_info: 0x178
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x178
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x4c8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x180
+  __DATA_CONST.__got: 0xd8
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x1640
+  __AUTH_CONST.__cfstring: 0x16e0
   __AUTH_CONST.__objc_const: 0x5f0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x3c
   __DATA.__bss: 0x48

   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 817AF122-C053-3BC9-B2DA-62B27568A704
+  UUID: 48ACAA19-2B6B-3956-AFFC-84656F2EAA45
   Functions: 110
-  Symbols:   515
-  CStrings:  586
+  Symbols:   516
+  CStrings:  381
 
Symbols:
+ ___block_literal_global.145
+ ___block_literal_global.147
+ ___block_literal_global.670
+ ___block_literal_global.763
+ ___block_literal_global.765
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
- ___block_literal_global.146
- ___block_literal_global.148
- ___block_literal_global.656
- ___block_literal_global.749
- ___block_literal_global.751
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x28
Functions:
~ -[_DASLogValueInterval isEqual:] : 76 -> 72
~ -[_DASLogValueInterval intervalString] : 232 -> 212
~ _defaultFormatter : 84 -> 68
~ -[_DASLogValueInterval description] : 152 -> 140
~ -[_DASLogValueInterval duration] : 144 -> 136
~ -[_DASLogValueInterval durationString] : 196 -> 192
~ -[_DASLogValueInterval setStartDate:] : 64 -> 12
~ -[_DASLogValueInterval setEndDate:] : 64 -> 12
~ -[_DASLogValueInterval setValue:] : 64 -> 12
~ +[_DASLogEntry logEntryForDate:category:message:] : 144 -> 152
~ -[_DASLogEntry description] : 160 -> 148
~ -[_DASLogEntry setDate:] : 64 -> 12
~ -[_DASLogEntry setCategory:] : 64 -> 12
~ -[_DASLogEntry setMessage:] : 64 -> 12
~ -[_DASLogCondition setCondition:] : 64 -> 12
~ -[_DASLogConditionHistory initWithCondition:fromDate:] : 136 -> 128
~ +[_DASLogConditionHistory condition:fromDate:] : 112 -> 116
~ -[_DASLogConditionHistory addCondition:atDate:] : 156 -> 152
~ -[_DASLogConditionHistory idealIntervals] : 412 -> 392
~ -[_DASLogConditionHistory description] : 804 -> 744
~ ___38-[_DASLogConditionHistory description]_block_invoke : 244 -> 236
~ -[_DASLogConditionHistory setConditions:] : 64 -> 12
~ -[_DASLogConditionHistory setIntervals:] : 64 -> 12
~ -[_DASLogExtractor initWithArchive:] : 224 -> 216
~ -[_DASLogExtractor getDefaultFilterPredicate] : 84 -> 68
~ ___45-[_DASLogExtractor getDefaultFilterPredicate]_block_invoke : 140 -> 136
~ -[_DASLogExtractor handleLogEventsLogEvents:sinceDate:withHandler:] : 336 -> 352
~ ___67-[_DASLogExtractor handleLogEventsLogEvents:sinceDate:withHandler:]_block_invoke : 644 -> 636
~ ___67-[_DASLogExtractor handleLogEventsLogEvents:sinceDate:withHandler:]_block_invoke_2 : 128 -> 124
~ -[_DASLogExtractor getScheduledBlocksOfMessages:forActivity:] : 700 -> 640
~ -[_DASLogExtractor getScheduledBlocksOfBARMessages:forApplication:] : 616 -> 608
~ -[_DASLogExtractor getMessagesBeforeRunning:forActivity:] : 704 -> 596
~ -[_DASLogExtractor getAllBARActivityNames:] : 472 -> 560
~ _getSubstring : 212 -> 216
~ -[_DASLogExtractor getAllPushLaunchActivityNames:] : 564 -> 696
~ -[_DASLogExtractor getMessagesForAllBARTasks:] : 700 -> 668
~ -[_DASLogExtractor getMessagesForBARLifecycle:forApplication:queryStatus:taskType:] : 636 -> 672
~ -[_DASLogExtractor getActivityStartBeforeDate:forActivity:] : 548 -> 516
~ -[_DASLogExtractor didActivityRun:forActivity:] : 308 -> 304
~ -[_DASLogExtractor getMessagesAfterRunning:forActivity:] : 536 -> 520
~ -[_DASLogExtractor didActivityFinish:forActivity:] : 376 -> 368
~ -[_DASLogExtractor didActivityFinish:forBARActivity:] : 380 -> 372
~ -[_DASLogExtractor getMessagesActivityFinish:forActivity:isCompleted:] : 408 -> 412
~ -[_DASLogExtractor didBARFinish:forApplication:] : 308 -> 304
~ -[_DASLogExtractor summarizeRuntimeOverMessages:forActivity:] : 952 -> 888
~ -[_DASLogExtractor getPolicyDenialReasonsFromMessage:] : 504 -> 696
~ -[_DASLogExtractor getpolicyToIntervals:] : 2564 -> 2380
~ -[_DASLogExtractor descriptionOfPolicyToIntervalsMap:] : 1260 -> 1208
~ -[_DASLogExtractor getIncompatibilityReasons:forActivity:] : 1100 -> 1048
~ -[_DASLogExtractor descriptionOfIncompatibilityDenials:] : 544 -> 536
~ -[_DASLogExtractor getInstancesOfHigherThreshold:forActivity:] : 836 -> 864
~ -[_DASLogExtractor descriptionOfHigherThresholds:] : 520 -> 512
~ -[_DASLogExtractor summarizePolicyDenialsOverMessages:maxDuration:] : 1060 -> 1008
~ ___67-[_DASLogExtractor summarizePolicyDenialsOverMessages:maxDuration:]_block_invoke : 248 -> 236
~ -[_DASLogExtractor summarizeAllDenialsOverMessages:forActivity:detail:] : 548 -> 504
~ -[_DASLogExtractor getSummaryFromLogs:forActivity:detail:] : 1928 -> 1732
~ -[_DASLogExtractor getBARSummaryFromLogs:forApplication:detail:] : 4860 -> 4480
~ -[_DASLogExtractor copyActivitySummary:startDate:endDate:detail:error:] : 608 -> 588
~ ___71-[_DASLogExtractor copyActivitySummary:startDate:endDate:detail:error:]_block_invoke : 200 -> 180
~ -[_DASLogExtractor copyApplicationSummary:startDate:endDate:detail:error:] : 556 -> 540
~ ___74-[_DASLogExtractor copyApplicationSummary:startDate:endDate:detail:error:]_block_invoke : 200 -> 180
~ -[_DASLogExtractor objectForTrigger:fromCondition:compactRepresentation:] : 1304 -> 1260
~ -[_DASLogExtractor addConditionToHistory:fromMessage:atTimestamp:compactRepresentation:] : 916 -> 864
~ -[_DASLogExtractor sysConditionsLog:startDate:endDate:] : 1924 -> 1836
~ ___55-[_DASLogExtractor sysConditionsLog:startDate:endDate:]_block_invoke : 140 -> 128
~ ___55-[_DASLogExtractor sysConditionsLog:startDate:endDate:]_block_invoke_2 : 292 -> 272
~ -[_DASLogExtractor setLogStore:] : 64 -> 12
~ -[_DASLogExtractor setDateFormatter:] : 64 -> 12
~ -[_DASLogExtractor setEventStream:] : 64 -> 12
~ -[_DASLogExtractor setSubsystem:] : 64 -> 12
~ -[_DASLogExtractor setCategory:] : 64 -> 12
~ ___defaultFormatter_block_invoke : 148 -> 144
~ ___timeOnlyFormatter_block_invoke : 148 -> 144
CStrings:
+ "Bailing out."
+ "Decision: AMNP}"
+ "Decision: MNP}"
+ "SUBMITTED"
+ "SUBMITTED <_DASActivity: "
+ "SUBMITTED <_DASActivity: \""
+ "SUBMITTED <_DASActivity: \"bgRefresh-"
+ "Submitted: <_DASActivity: \"bgRefresh-"
+ "response: {100,"
+ "response: {33,"
+ "{name: "
- "\t{name: "
- ".cxx_destruct"
- "@\"NSDate\""
- "@\"NSDateFormatter\""
- "@\"NSMutableArray\""
- "@\"NSObject\""
- "@\"NSString\""
- "@\"OSLogEventStore\""
- "@\"OSLogEventStream\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "@32@0:8@16d24"
- "@36@0:8@16@24B32"
- "@40@0:8@16@24@32"
- "@48@0:8@16@24@32@40"
- "@52@0:8@16@24@32B40^i44"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "Bailing  out."
- "SUBMITTING:"
- "Submitted Activity:"
- "Submitted Activity: <_DASActivity: \"bgRefresh-"
- "Submitted:"
- "T@\"NSDate\",&,N,V_date"
- "T@\"NSDate\",&,N,V_endDate"
- "T@\"NSDate\",&,N,V_startDate"
- "T@\"NSDateFormatter\",&,N,V_dateFormatter"
- "T@\"NSMutableArray\",&,N,V_conditions"
- "T@\"NSMutableArray\",&,N,V_intervals"
- "T@\"NSObject\",&,N,V_condition"
- "T@\"NSObject\",&,N,V_value"
- "T@\"NSString\",&,N,V_category"
- "T@\"NSString\",&,N,V_message"
- "T@\"NSString\",&,N,V_subsystem"
- "T@\"OSLogEventStore\",&,N,V_logStore"
- "T@\"OSLogEventStream\",&,N,V_eventStream"
- "TB,N,V_isIdeal"
- "UTF8String"
- "_DASLogCondition"
- "_DASLogConditionHistory"
- "_DASLogEntry"
- "_DASLogExtractor"
- "_DASLogValueInterval"
- "_category"
- "_condition"
- "_conditions"
- "_date"
- "_dateFormatter"
- "_endDate"
- "_eventStream"
- "_intervals"
- "_isIdeal"
- "_logStore"
- "_message"
- "_startDate"
- "_subsystem"
- "_value"
- "activateStreamFromDate:"
- "addCondition:atDate:"
- "addConditionToHistory:fromMessage:atTimestamp:compactRepresentation:"
- "addObject:"
- "addObjectsFromArray:"
- "allKeys"
- "andPredicateWithSubpredicates:"
- "appendFormat:"
- "appendString:"
- "array"
- "category"
- "characterSetWithCharactersInString:"
- "compare:"
- "components:fromDate:"
- "componentsSeparatedByCharactersInSet:"
- "componentsSeparatedByString:"
- "composedMessage"
- "condition"
- "condition:fromDate:"
- "conditions"
- "containsString:"
- "copy"
- "copyActivitySummary:startDate:endDate:detail:error:"
- "copyApplicationSummary:startDate:endDate:detail:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentCalendar"
- "d16@0:8"
- "date"
- "dateFormatter"
- "dateFromString:"
- "dateWithTimeInterval:sinceDate:"
- "description"
- "descriptionOfHigherThresholds:"
- "descriptionOfIncompatibilityDenials:"
- "descriptionOfPolicyToIntervalsMap:"
- "dictionary"
- "dictionaryWithObjectsAndKeys:"
- "didActivityFinish:forActivity:"
- "didActivityFinish:forBARActivity:"
- "didActivityRun:forActivity:"
- "didBARFinish:forApplication:"
- "distantFuture"
- "distantPast"
- "doubleValue"
- "duration"
- "durationString"
- "endDate"
- "enumerateKeysAndObjectsUsingBlock:"
- "eventStream"
- "extractorForArchive:"
- "filterUsingPredicate:"
- "firstObject"
- "getActivityStartBeforeDate:forActivity:"
- "getAllBARActivityNames:"
- "getAllPushLaunchActivityNames:"
- "getBARSummaryFromLogs:forApplication:detail:"
- "getDefaultFilterPredicate"
- "getIncompatibilityReasons:forActivity:"
- "getInstancesOfHigherThreshold:forActivity:"
- "getMessagesActivityFinish:forActivity:isCompleted:"
- "getMessagesAfterRunning:forActivity:"
- "getMessagesBeforeRunning:forActivity:"
- "getMessagesForAllBARTasks:"
- "getMessagesForBARLifecycle:forApplication:queryStatus:taskType:"
- "getMessagesWhenAppBackgroundSwitch:forApplication:switchTo:"
- "getPolicyDenialReasonsFromMessage:"
- "getScheduledBlocksOfBARMessages:forApplication:"
- "getScheduledBlocksOfMessages:forActivity:"
- "getSummaryFromLogs:forActivity:detail:"
- "getpolicyToIntervals:"
- "handleLogEventsLogEvents:sinceDate:withHandler:"
- "i32@0:8@16@24"
- "i36@0:8B16@20@28"
- "i40@0:8@16@24@?32"
- "i44@0:8@16@24@32B40"
- "idealIntervals"
- "init"
- "initWithArchive:"
- "initWithCondition:fromDate:"
- "initWithSource:"
- "initWithStartDate:endDate:"
- "intValue"
- "intersectionWithDateInterval:"
- "intervalString"
- "intervals"
- "invalidate"
- "isEqual:"
- "isEqualToDate:"
- "isEqualToString:"
- "isIdeal"
- "lastObject"
- "length"
- "localStore"
- "localTimeZone"
- "logEntryForDate:category:message:"
- "logStore"
- "message"
- "minusSet:"
- "mutableCopy"
- "numberWithDouble:"
- "numberWithInt:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "objectForTrigger:fromCondition:compactRepresentation:"
- "predicateWithBlock:"
- "predicateWithFormat:"
- "prepareWithCompletionHandler:"
- "rangeOfString:"
- "rangeOfString:options:"
- "removeObjectAtIndex:"
- "set"
- "setCategory:"
- "setCondition:"
- "setConditions:"
- "setDate:"
- "setDateFormat:"
- "setDateFormatter:"
- "setDateStyle:"
- "setEndDate:"
- "setEventHandler:"
- "setEventStream:"
- "setFilterPredicate:"
- "setFlags:"
- "setIntervals:"
- "setInvalidationHandler:"
- "setIsIdeal:"
- "setLogStore:"
- "setMessage:"
- "setObject:forKeyedSubscript:"
- "setStartDate:"
- "setSubsystem:"
- "setTimeStyle:"
- "setTimeZone:"
- "setUpgradeConfirmationHandler:"
- "setValue:"
- "setWithArray:"
- "sortedArrayUsingComparator:"
- "startDate"
- "storeWithArchiveURL:"
- "string"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringFromDate:"
- "stringWithFormat:"
- "substringWithRange:"
- "subsystem"
- "summarizeActivity:startDate:endDate:detail:"
- "summarizeAllDenialsOverMessages:forActivity:detail:"
- "summarizeApplication:startDate:endDate:detail:"
- "summarizePolicyDenialsOverMessages:maxDuration:"
- "summarizeRuntimeOverMessages:forActivity:"
- "sysConditionsLog:startDate:endDate:"
- "timeIntervalSinceDate:"
- "unionSet:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v32@0:8@16@24"
- "v44@0:8@16@24@32B40"
- "value"
- "withCondition:"

```
