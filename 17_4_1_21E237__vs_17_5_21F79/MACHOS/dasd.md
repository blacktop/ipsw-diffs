## dasd

> `/usr/libexec/dasd`

```diff

-1470.100.56.0.0
-  __TEXT.__text: 0xc8ef0
+1470.120.7.0.0
+  __TEXT.__text: 0xc9c10
   __TEXT.__auth_stubs: 0x12b0
-  __TEXT.__objc_stubs: 0x11b60
-  __TEXT.__objc_methlist: 0xc094
+  __TEXT.__objc_stubs: 0x11c00
+  __TEXT.__objc_methlist: 0xc19c
   __TEXT.__const: 0x770
-  __TEXT.__objc_methname: 0x1e6c9
-  __TEXT.__cstring: 0xa396
-  __TEXT.__oslogstring: 0xb4e2
-  __TEXT.__objc_classname: 0x12fb
+  __TEXT.__objc_methname: 0x1e7c3
+  __TEXT.__cstring: 0xa57f
+  __TEXT.__oslogstring: 0xb5e9
+  __TEXT.__objc_classname: 0x1311
   __TEXT.__objc_methtype: 0x27d4
-  __TEXT.__gcc_except_tab: 0x2688
+  __TEXT.__gcc_except_tab: 0x270c
   __TEXT.__dlopen_cstrs: 0x434
-  __TEXT.__unwind_info: 0x2b94
+  __TEXT.__unwind_info: 0x2c20
   __DATA_CONST.__auth_got: 0x968
   __DATA_CONST.__got: 0x4b0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x2ba8
-  __DATA_CONST.__cfstring: 0xad00
-  __DATA_CONST.__objc_classlist: 0x4b8
+  __DATA_CONST.__cfstring: 0xaee0
+  __DATA_CONST.__objc_classlist: 0x4c0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_classrefs: 0x8a8
-  __DATA_CONST.__objc_superrefs: 0x3e8
-  __DATA_CONST.__objc_arraydata: 0x1d0
+  __DATA_CONST.__objc_classrefs: 0x8b0
+  __DATA_CONST.__objc_superrefs: 0x3f0
+  __DATA_CONST.__objc_arraydata: 0x200
   __DATA_CONST.__objc_arrayobj: 0xd8
-  __DATA_CONST.__objc_intobj: 0x990
+  __DATA_CONST.__objc_intobj: 0x9a8
   __DATA_CONST.__objc_dictobj: 0xc8
-  __DATA.__objc_const: 0x26ee0
-  __DATA.__objc_selrefs: 0x68e8
-  __DATA.__objc_ivar: 0xf6c
-  __DATA.__objc_data: 0x2f30
+  __DATA.__objc_const: 0x27040
+  __DATA.__objc_selrefs: 0x6928
+  __DATA.__objc_ivar: 0xf7c
+  __DATA.__objc_data: 0x2f80
   __DATA.__data: 0x11b0
-  __DATA.__bss: 0x9d8
+  __DATA.__bss: 0x9e8
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  Functions: 5077
+  Functions: 5111
   Symbols:   605
-  CStrings:  8303
+  CStrings:  8335
 
CStrings:
+ "BARMetricDict"
+ "BgRefreshCompletionCount"
+ "BgRefreshSubmissionCount"
+ "Initializing _DASBARMetricRecorder!"
+ "Loaded bar metric dict from defaults %@"
+ "PushLaunchCompletionCount"
+ "PushLaunchSubmissionCount"
+ "Reset _barMetricDict data succesfully %@"
+ "Running telemetry collection using context: %@"
+ "Saved bar metric dict to defaults %@"
+ "T@\"NSDate\",&,V_launchDataCollectionStartDate"
+ "T@\"NSDate\",&,V_prewarmingDataCollectionStartDate"
+ "T@\"NSMutableDictionary\",&,N,V_barMetricDict"
+ "T@\"NSObject<OS_xpc_object>\",&,V_activity"
+ "Wrong argument 'stage': %ld passed to recordBARMetric."
+ "_DASBARMetricRecorder"
+ "_barMetricDict"
+ "addExperimentInformationWithDictionary:"
+ "barMetricDict"
+ "barMetricRecorder"
+ "com.apple.dasd.BackgroundAppRefreshActivityStats"
+ "com.apple.dasd.barMetricRecorder"
+ "com.apple.dasd.dailyPeriodicBackgroundAppRefreshReporting"
+ "com.apple.messages.sync.AttachmentAssetDownload"
+ "com.apple.messages.sync.Backfill"
+ "com.apple.messages.sync.Backup"
+ "com.apple.messages.sync.Initial"
+ "com.apple.messages.sync.Periodic"
+ "com.apple.messages.sync.UserInitiated"
+ "fetchLatestBARMetric"
+ "recordBARMetric:atStage:"
+ "reportBackgroundAppRefreshAnalytics:"
+ "resetBARMetric"
+ "schedule: Running background app refresh analytics background task"
+ "sending BackgroundAppRefreshActivity analytics to CA: %@"
+ "setBarMetricDict:"
+ "shouldRecordBARMetricForActivity:"
+ "updateWithActivity:prewarmingStartDate:launchStartDate:"
- "Running telemetry collection using existing context: %@"
- "Running telemetry collection using newly created context: %@"
- "T@\"NSDate\",&,N,V_launchDataCollectionStartDate"
- "T@\"NSDate\",&,N,V_prewarmingDataCollectionStartDate"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_activity"
- "initWithActivity:prewarmingStartDate:launchStartDate:"

```
