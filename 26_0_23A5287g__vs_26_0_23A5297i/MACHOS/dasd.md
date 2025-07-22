## dasd

> `/usr/libexec/dasd`

```diff

-2109.0.69.0.1
-  __TEXT.__text: 0x128c2c
+2109.0.84.0.0
+  __TEXT.__text: 0x1290a8
   __TEXT.__auth_stubs: 0x1350
-  __TEXT.__objc_stubs: 0x17d60
-  __TEXT.__objc_methlist: 0x11448
+  __TEXT.__objc_stubs: 0x17d80
+  __TEXT.__objc_methlist: 0x11460
   __TEXT.__const: 0x918
-  __TEXT.__objc_methname: 0x28dbe
-  __TEXT.__cstring: 0xe4b8
-  __TEXT.__oslogstring: 0x115ae
+  __TEXT.__objc_methname: 0x28df6
+  __TEXT.__cstring: 0xe4a8
+  __TEXT.__oslogstring: 0x1161a
   __TEXT.__objc_classname: 0x1908
-  __TEXT.__objc_methtype: 0x3a49
-  __TEXT.__gcc_except_tab: 0x4fb4
+  __TEXT.__objc_methtype: 0x3a8b
+  __TEXT.__gcc_except_tab: 0x4fd8
   __TEXT.__dlopen_cstrs: 0x4e2
-  __TEXT.__unwind_info: 0x4278
+  __TEXT.__unwind_info: 0x4280
   __DATA_CONST.__auth_got: 0x9b8
   __DATA_CONST.__got: 0xa90
-  __DATA_CONST.__const: 0x3da0
-  __DATA_CONST.__cfstring: 0xf200
+  __DATA_CONST.__const: 0x3d60
+  __DATA_CONST.__cfstring: 0xf1e0
   __DATA_CONST.__objc_classlist: 0x620
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1c0

   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA.__objc_const: 0x2eef8
-  __DATA.__objc_selrefs: 0x8ce8
+  __DATA.__objc_selrefs: 0x8d08
   __DATA.__objc_ivar: 0x13ec
   __DATA.__objc_data: 0x3d40
   __DATA.__data: 0x1658
-  __DATA.__bss: 0xc20
+  __DATA.__bss: 0xc28
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 94CE739C-51BC-3DC9-ABCA-3B5E312D0AEB
-  Functions: 7011
+  UUID: 09D43336-36D2-3289-AC61-E98B3C39CAE6
+  Functions: 7013
   Symbols:   663
-  CStrings:  12988
+  CStrings:  12996
 
CStrings:
+ "@128@0:8{?=QQQQQQQQQQQQQQ}16"
+ "Computing Activity Blocking Reasons"
+ "Computing Activity Timelines"
+ "Computing Elapsed Runtimes"
+ "Computing On Battery Runtimes"
+ "Computing Progress Timelines"
+ "Computing Throughput Timelines"
+ "Getting Plugin Prediction Data with metrics: %@ & timeFilter: %@"
+ "Getting Task Runtime Allocations with metrics: %@ & timeFilter: %@"
+ "Getting the Recent Unique Installation Events"
+ "Getting the recent unique progress events"
+ "SELF.RequiresPlugin == YES && SELF.RequiresDeviceInactivity == YES && (SELF.IsCPUIntensive == YES || SELF.IsMemoryIntensive == YES || SELF.IsANEIntensive == YES || SELF.IsGPUIntensive == YES || SELF.IsDiskIntensive == YES)"
+ "Unknown State %@"
+ "addEvent:"
+ "computeActivityBlockingReasons:"
+ "computeActivityTimelines:installationEvents:"
+ "computeEstimatedRunTime:elapsedRunTimes:progressEvents:activity:endDate:"
+ "computeFeatureTimeline:installationEvents:"
+ "computeOnBatteryRunTimes:plugInCheckpoints:"
+ "computeProgressTimelines:"
+ "computeThroughputTimelines:"
+ "convertCountersToNSDictionary:"
+ "decrementCounterForCheckpoint:counters:"
+ "getValue:"
+ "incrementCounterForCheckpoint:counters:"
+ "initializeCheckpointCounters"
+ "isDASTaskCheckpoint:checkpointState:"
+ "loadPluginPrediction:timeFilter:filepath:"
+ "loadTaskRuntimeAllocation:timeFilter:filepath:"
+ "mergeWithTimeSeries:"
+ "onBatteryProcessingStartTime"
+ "startedRunningOnBattery"
+ "usageTimelineForWidgetBudgetID:withEndDate:"
+ "v32@0:8Q16^{?=QQQQQQQQQQQQQQ}24"
+ "valueWithBytes:objCType:"
+ "widgetUsageLikelihoodForBudgetID:endDate:"
+ "{?=QQQQQQQQQQQQQQ}"
+ "{?=QQQQQQQQQQQQQQ}16@0:8"
- "Computing Elapsed Run Time for %@"
- "Finding the last DASTaskCheckpoint event for %@"
- "Finding the last event for checkpoint %lu of %@"
- "Getting the recent unique installation events"
- "Getting the recent unique progress events for %@"
- "Last submission event for %@: %@"
- "LastUpgradeSystemTimestamp >= %lf AND LastUpgradeSystemTimestamp <= %lf"
- "No available task matching name: %@"
- "SELF.RequiresPlugin == YES && SELF.RequiresDeviceInactivity == YES && (SELF.IsCPUIntensive == YES || SELF.IsMemoryIntensive == YES || SELF.IsANEIntensive == YES || SELF.IsGPUIntensive == YES)"
- "TaskName IN %@"
- "Unknown State %@ Count"
- "computeActivityBlockingReason:"
- "computeActivityTimeline:installations:"
- "computeEstimatedRunTime:checkpointTimeSeries:progressTimeSeries:activity:endDate:"
- "computeFeatureTimeline:installations:"
- "computeOnBatteryRunTimeFromCheckpoints:plugInEvents:"
- "computeProgressTimeline:"
- "computeThroughputTimeline:"
- "epochTimestamp < %lf"
- "findLastCheckpointEvent:checkpoint:"
- "findLastDASTaskCheckpointEvent:"
- "findLastTaskSubmissionEvent:"
- "indexOfObject:"
- "populateElapsedRuntimeDictDetails:lastSubmissionEvent:taskCheckpoints:removedSubmissionsCount:"
- "removeImmediatelyPrecedingSubmissions:"
- "removeObjectsInArray:"
- "usageTimelineForWidgetBudgetID:withStartDate:"
- "v48@0:8@16@24@32Q40"
- "widgetUsageLikelihoodForBudgetID:startDate:"

```
