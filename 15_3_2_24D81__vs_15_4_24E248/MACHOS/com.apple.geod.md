## com.apple.geod

> `/System/Library/PrivateFrameworks/GeoServices.framework/Versions/A/XPCServices/com.apple.geod.xpc/Contents/MacOS/com.apple.geod`

```diff

-1986.23.11.14.2
-  __TEXT.__text: 0x41604
-  __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_stubs: 0x7ee0
-  __TEXT.__objc_methlist: 0x20a0
-  __TEXT.__const: 0x260
-  __TEXT.__cstring: 0x442a
-  __TEXT.__objc_classname: 0x88e
-  __TEXT.__objc_methname: 0x77de
-  __TEXT.__objc_methtype: 0x16be
-  __TEXT.__gcc_except_tab: 0xbec
-  __TEXT.__oslogstring: 0x2592
+1986.24.9.12.31
+  __TEXT.__text: 0x3f7e4
+  __TEXT.__auth_stubs: 0xc60
+  __TEXT.__objc_stubs: 0x7be0
+  __TEXT.__objc_methlist: 0x25cc
+  __TEXT.__const: 0x250
+  __TEXT.__cstring: 0x4439
+  __TEXT.__objc_classname: 0x891
+  __TEXT.__objc_methname: 0x75b8
+  __TEXT.__objc_methtype: 0x16b5
+  __TEXT.__gcc_except_tab: 0xab0
+  __TEXT.__oslogstring: 0x220e
   __TEXT.__dlopen_cstrs: 0x54
   __TEXT.__unwind_info: 0xfc8
-  __DATA_CONST.__auth_got: 0x638
-  __DATA_CONST.__got: 0x8f0
-  __DATA_CONST.__const: 0x20c0
-  __DATA_CONST.__cfstring: 0x2f00
+  __DATA_CONST.__auth_got: 0x640
+  __DATA_CONST.__got: 0x8a0
+  __DATA_CONST.__const: 0x2040
+  __DATA_CONST.__cfstring: 0x2e00
   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x110
-  __DATA_CONST.__objc_arraydata: 0x230
-  __DATA_CONST.__objc_arrayobj: 0x480
+  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__objc_arraydata: 0x1f8
+  __DATA_CONST.__objc_arrayobj: 0x408
   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x6c68
-  __DATA.__objc_selrefs: 0x2218
-  __DATA.__objc_ivar: 0x1a8
+  __DATA.__objc_const: 0x62d0
+  __DATA.__objc_selrefs: 0x2220
+  __DATA.__objc_ivar: 0x1ac
   __DATA.__objc_data: 0x1270
   __DATA.__data: 0x780
-  __DATA.__bss: 0x1e0
+  __DATA.__bss: 0x1d0
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 130C2B2D-73FE-326C-B5E4-7DA052FC3CC8
-  Functions: 1096
-  Symbols:   511
-  CStrings:  2691
+  UUID: 1DF2A399-1296-373C-84EB-A5FDA65949C2
+  Functions: 1122
+  Symbols:   502
+  CStrings:  2642
 
Symbols:
+ _GEOCanonicalResourceNameForVersionedName
+ _GEOResourceDevResourcesPath
+ _OBJC_CLASS_$_GEOResourceReportCorrupt
+ _geo_dispatch_timer_create_on_qos
- _GEOBackgroundTaskReportReportTaskInitiated
- _GEOExperimentServerLocalProxyBackgroundTaskIdentifier
- _GEOExperimentServerLocalProxyBackgroundTaskRetryIdentifier
- _GEOMapsAuthBackgroundTaskIdentifier
- _GEOMobileAssetResourceUpdaterTaskIdentifier
- _GEOOnce
- _GEOProactiveTileDownloaderTaskIdentifier
- _GEORequestCounterPowerLoggerBackgroundTaskIdentifier
- _GEOUpdateNetworkDefaultsTaskIdentifier
- _GeoServicesConfig_ExperimentMaxRefreshInterval
- _GeoServicesConfig_ExperimentMinRefreshInterval
- _GeoServicesConfig_ExperimentRunImmediatelyInterval
- _GeoServicesConfig_ExperimentServiceFailureRetryInterval
CStrings:
+ "/System/AppleInternal/Library/Frameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks"
+ "/System/AppleInternal/Library/Frameworks/CoreAnalytics.framework/CoreAnalytics"
+ "/System/AppleInternal/Library/Frameworks/CoreLocation.framework/CoreLocation"
+ "/System/AppleInternal/Library/Frameworks/MobileAsset.framework/MobileAsset"
+ "@16@?0@\"NSString\"8"
+ "BGST unsupported - cannot cancel refresh task"
+ "COMPONENT_TYPE_ACCOLADES"
+ "Peer %{public}@ has made more than %u requests over %f seconds"
+ "_opportunisticResourceLoadingTimer"
+ "_updateTimer"
+ "contentsOfDirectoryAtPath:error:"
+ "corruptedWithRequest:"
+ "fileURL"
+ "fileURLWithPath:isDirectory:"
+ "messageTimestamp"
+ "removeUnpackedResource:at:log:error:"
+ "reportCorruptUnpackedResource:fileURL:"
+ "resource"
+ "setWasThrottled:"
+ "shouldThrottleMessageForServer:"
+ "throttleCount"
+ "throttleInterval"
+ "throttlingEnabled"
+ "v32@0:8@\"GEOResource\"16@\"NSURL\"24"
+ "wasThrottled"
- "@\"BGRepeatingSystemTaskRequest\""
- "Ensuring existence of opportunistic resource loading background task."
- "Error loading experiment configuration from service: %{public}@"
- "Experiment response has refresh interval of %f. Capping at %f."
- "Experiment should have refreshed already or will refresh in the next %f seconds, going to run it now"
- "Failed to submit nonrepeating task with error: %@"
- "Failed to submit repeating task with error: %@"
- "Failed to submit task with error: %@"
- "Failed to update task with error: %@"
- "Finished generating telemetry for type: %llu"
- "Generating telemetry for type: %llu"
- "Loaded new experiment configuration: %{private}@"
- "MobileAsset background task is already scheduled (%{public}@)"
- "NetworkDefaults background task is already scheduled (%{public}@)"
- "New experiment configuration is the same as the previous experiment configuration"
- "OpportunisticResourceLoading background task is already scheduled (%{public}@)"
- "PeriodicTelemetry"
- "Setting experiment refresh interval to %f"
- "Trouble cancelling %@ with error %@"
- "Unknown"
- "Updating experiment refresh interval to %f"
- "_repeatingTask"
- "_submitNonRepeatingRetryTask:"
- "activeTileGroupData"
- "addTileGroupObserver:queue:"
- "cancelTaskRequestWithIdentifier:error:"
- "com.apple.GeoServices.UpdateExperiment"
- "com.apple.GeoServices.UpdateExperiment.Retry"
- "com.apple.geo.ma.resource.server"
- "com.apple.geod.EnvironmentSecurity"
- "com.apple.geod.OpportunisticResourceLoading"
- "com.apple.geod.RequestCountPowerLogger"
- "com.apple.geod.telemetry.daily"
- "com.apple.geod.updateNetworkDefaults"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "dataSet"
- "dictionaryWithObject:forKey:"
- "flushToPowerLog"
- "initWithIdentifier:"
- "initWithObjectsAndKeys:"
- "interval"
- "possibleBackgroundTaskIdentifiers"
- "refreshFromTask:"
- "refreshIntervalSeconds"
- "registerForTaskWithIdentifier:usingQueue:launchHandler:"
- "reportTelemetryForType:completionHandler:"
- "runBackgroundTask:"
- "setExpirationHandler:"
- "setInterval:"
- "setNetworkDownloadSize:"
- "setPreventsDeviceSleep:"
- "setPriority:"
- "setRequiresExternalPower:"
- "setRequiresInexpensiveNetworkConnectivity:"
- "setRequiresNetworkConnectivity:"
- "setScheduleAfter:"
- "setTaskCompleted"
- "setTrySchedulingBefore:"
- "sharedScheduler"
- "submitBGSTQueue"
- "submitBackgroundTasksNeededDuringDaemonStart"
- "submitTaskRequest:error:"
- "taskRequestForIdentifier:"
- "updateTaskRequest:error:"
- "v16@?0@\"BGSystemTask\"8"
- "v24@0:8d16"

```
