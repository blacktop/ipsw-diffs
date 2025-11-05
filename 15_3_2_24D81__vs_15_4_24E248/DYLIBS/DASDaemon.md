## DASDaemon

> `/System/Library/PrivateFrameworks/DASDaemon.framework/Versions/A/DASDaemon`

```diff

-1786.80.10.0.0
-  __TEXT.__text: 0x9e78
+1856.101.1.0.0
+  __TEXT.__text: 0x9dd0
   __TEXT.__auth_stubs: 0x190
   __TEXT.__objc_methlist: 0x470
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0x88
   __TEXT.__cstring: 0xfa7
-  __TEXT.__unwind_info: 0x190
+  __TEXT.__unwind_info: 0x198
   __TEXT.__objc_classname: 0x6b
   __TEXT.__objc_methname: 0xf89
   __TEXT.__objc_methtype: 0x19b

   - /System/Library/PrivateFrameworks/LoggingSupport.framework/Versions/A/LoggingSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B774CD03-B951-3CEA-B622-A258A1B0276A
-  Functions: 117
-  Symbols:   391
+  UUID: EFF2A8E5-057B-354B-9B41-77354289C170
+  Functions: 121
+  Symbols:   395
   CStrings:  586
 
Symbols:
+ -[_DASLogConditionHistory description].cold.1
+ -[_DASLogExtractor getDefaultFilterPredicate].cold.1
+ -[_DASLogExtractor sysConditionsLog:startDate:endDate:].cold.1
+ defaultFormatter.cold.1
Functions:
~ _defaultFormatter : 84 -> 68
~ -[_DASLogExtractor getDefaultFilterPredicate] : 84 -> 68
~ -[_DASLogExtractor getScheduledBlocksOfMessages:forActivity:] : 772 -> 768
~ -[_DASLogExtractor getMessagesBeforeRunning:forActivity:] : 804 -> 800
~ -[_DASLogExtractor getAllPushLaunchActivityNames:] : 556 -> 596
~ -[_DASLogExtractor didActivityFinish:forBARActivity:] : 400 -> 392
~ -[_DASLogExtractor getpolicyToIntervals:] : 2740 -> 2736
~ -[_DASLogExtractor getInstancesOfHigherThreshold:forActivity:] : 880 -> 892
~ -[_DASLogExtractor summarizePolicyDenialsOverMessages:maxDuration:] : 1132 -> 1120
~ -[_DASLogExtractor getSummaryFromLogs:forActivity:detail:] : 2020 -> 2000
~ -[_DASLogExtractor getBARSummaryFromLogs:forApplication:detail:] : 5292 -> 5092
~ -[_DASLogExtractor objectForTrigger:fromCondition:compactRepresentation:] : 1344 -> 1324
~ -[_DASLogExtractor sysConditionsLog:startDate:endDate:] : 2124 -> 2108

```
