## DASDaemon

> `/System/Library/PrivateFrameworks/DASDaemon.framework/DASDaemon`

```diff

-2109.80.9.0.0
-  __TEXT.__text: 0x8a8c
-  __TEXT.__auth_stubs: 0x300
+2109.100.198.0.0
+  __TEXT.__text: 0x94f8
+  __TEXT.__auth_stubs: 0x2e0
   __TEXT.__objc_methlist: 0x470
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0x88
   __TEXT.__cstring: 0xfa7
-  __TEXT.__unwind_info: 0x178
+  __TEXT.__unwind_info: 0x1c8
   __TEXT.__objc_classname: 0x6b
   __TEXT.__objc_methname: 0xf89
   __TEXT.__objc_methtype: 0x19b

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x4c8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x190
+  __AUTH_CONST.__auth_got: 0x180
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x1640
   __AUTH_CONST.__objc_const: 0x5f0

   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9723DE56-89E1-33B0-80C7-0AE76CDCD5DF
+  UUID: 920208B0-E730-3B42-9B84-8405C3A12694
   Functions: 110
-  Symbols:   517
+  Symbols:   515
   CStrings:  586
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
Functions:
~ -[_DASLogValueInterval isEqual:] : 72 -> 76
~ -[_DASLogValueInterval intervalString] : 212 -> 232
~ _defaultFormatter : 68 -> 84
~ -[_DASLogValueInterval description] : 140 -> 152
~ -[_DASLogValueInterval duration] : 136 -> 144
~ -[_DASLogValueInterval durationString] : 192 -> 196
~ -[_DASLogValueInterval setStartDate:] : 12 -> 64
~ -[_DASLogValueInterval setEndDate:] : 12 -> 64
~ -[_DASLogValueInterval setValue:] : 12 -> 64
~ +[_DASLogEntry logEntryForDate:category:message:] : 152 -> 144
~ -[_DASLogEntry description] : 148 -> 160
~ -[_DASLogEntry setDate:] : 12 -> 64
~ -[_DASLogEntry setCategory:] : 12 -> 64
~ -[_DASLogEntry setMessage:] : 12 -> 64
~ -[_DASLogCondition setCondition:] : 12 -> 64
~ -[_DASLogConditionHistory initWithCondition:fromDate:] : 128 -> 136
~ +[_DASLogConditionHistory condition:fromDate:] : 116 -> 112
~ -[_DASLogConditionHistory addCondition:atDate:] : 152 -> 156
~ -[_DASLogConditionHistory idealIntervals] : 392 -> 412
~ -[_DASLogConditionHistory description] : 744 -> 804
~ ___38-[_DASLogConditionHistory description]_block_invoke : 236 -> 244
~ -[_DASLogConditionHistory setConditions:] : 12 -> 64
~ -[_DASLogConditionHistory setIntervals:] : 12 -> 64
~ -[_DASLogExtractor initWithArchive:] : 216 -> 224
~ -[_DASLogExtractor getDefaultFilterPredicate] : 68 -> 84
~ ___45-[_DASLogExtractor getDefaultFilterPredicate]_block_invoke : 136 -> 140
~ -[_DASLogExtractor handleLogEventsLogEvents:sinceDate:withHandler:] : 352 -> 336
~ ___67-[_DASLogExtractor handleLogEventsLogEvents:sinceDate:withHandler:]_block_invoke : 636 -> 644
~ ___67-[_DASLogExtractor handleLogEventsLogEvents:sinceDate:withHandler:]_block_invoke_2 : 124 -> 128
~ -[_DASLogExtractor getScheduledBlocksOfMessages:forActivity:] : 684 -> 700
~ -[_DASLogExtractor getScheduledBlocksOfBARMessages:forApplication:] : 604 -> 616
~ -[_DASLogExtractor getMessagesBeforeRunning:forActivity:] : 692 -> 704
~ -[_DASLogExtractor getAllBARActivityNames:] : 452 -> 472
~ _getSubstring : 216 -> 212
~ -[_DASLogExtractor getAllPushLaunchActivityNames:] : 492 -> 564
~ -[_DASLogExtractor getMessagesWhenAppBackgroundSwitch:forApplication:switchTo:] : 428 -> 432
~ -[_DASLogExtractor getMessagesForAllBARTasks:] : 664 -> 700
~ -[_DASLogExtractor getMessagesForBARLifecycle:forApplication:queryStatus:taskType:] : 628 -> 636
~ -[_DASLogExtractor getActivityStartBeforeDate:forActivity:] : 512 -> 548
~ -[_DASLogExtractor didActivityRun:forActivity:] : 300 -> 308
~ -[_DASLogExtractor getMessagesAfterRunning:forActivity:] : 516 -> 536
~ -[_DASLogExtractor didActivityFinish:forActivity:] : 372 -> 376
~ -[_DASLogExtractor didActivityFinish:forBARActivity:] : 368 -> 380
~ -[_DASLogExtractor didBARFinish:forApplication:] : 300 -> 308
~ -[_DASLogExtractor summarizeRuntimeOverMessages:forActivity:] : 884 -> 952
~ -[_DASLogExtractor getPolicyDenialReasonsFromMessage:] : 488 -> 504
~ -[_DASLogExtractor getpolicyToIntervals:] : 2364 -> 2564
~ -[_DASLogExtractor descriptionOfPolicyToIntervalsMap:] : 1200 -> 1260
~ -[_DASLogExtractor getIncompatibilityReasons:forActivity:] : 1044 -> 1100
~ -[_DASLogExtractor descriptionOfIncompatibilityDenials:] : 532 -> 544
~ -[_DASLogExtractor getInstancesOfHigherThreshold:forActivity:] : 780 -> 836
~ -[_DASLogExtractor descriptionOfHigherThresholds:] : 508 -> 520
~ -[_DASLogExtractor summarizePolicyDenialsOverMessages:maxDuration:] : 1004 -> 1060
~ ___67-[_DASLogExtractor summarizePolicyDenialsOverMessages:maxDuration:]_block_invoke : 236 -> 248
~ -[_DASLogExtractor summarizeAllDenialsOverMessages:forActivity:detail:] : 504 -> 548
~ -[_DASLogExtractor getSummaryFromLogs:forActivity:detail:] : 1728 -> 1928
~ -[_DASLogExtractor getBARSummaryFromLogs:forApplication:detail:] : 4472 -> 4860
~ -[_DASLogExtractor copyActivitySummary:startDate:endDate:detail:error:] : 588 -> 608
~ ___71-[_DASLogExtractor copyActivitySummary:startDate:endDate:detail:error:]_block_invoke : 180 -> 200
~ -[_DASLogExtractor copyApplicationSummary:startDate:endDate:detail:error:] : 540 -> 556
~ ___74-[_DASLogExtractor copyApplicationSummary:startDate:endDate:detail:error:]_block_invoke : 180 -> 200
~ -[_DASLogExtractor objectForTrigger:fromCondition:compactRepresentation:] : 1260 -> 1304
~ -[_DASLogExtractor addConditionToHistory:fromMessage:atTimestamp:compactRepresentation:] : 860 -> 916
~ -[_DASLogExtractor sysConditionsLog:startDate:endDate:] : 1832 -> 1924
~ ___55-[_DASLogExtractor sysConditionsLog:startDate:endDate:]_block_invoke : 128 -> 140
~ ___55-[_DASLogExtractor sysConditionsLog:startDate:endDate:]_block_invoke_2 : 272 -> 292
~ -[_DASLogExtractor setLogStore:] : 12 -> 64
~ -[_DASLogExtractor setDateFormatter:] : 12 -> 64
~ -[_DASLogExtractor setEventStream:] : 12 -> 64
~ -[_DASLogExtractor setSubsystem:] : 12 -> 64
~ -[_DASLogExtractor setCategory:] : 12 -> 64
~ ___defaultFormatter_block_invoke : 144 -> 148
~ ___timeOnlyFormatter_block_invoke : 144 -> 148

```
