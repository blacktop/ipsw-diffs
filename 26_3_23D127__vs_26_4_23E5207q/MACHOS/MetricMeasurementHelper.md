## MetricMeasurementHelper

> `/System/Library/PrivateFrameworks/MetricMeasurement.framework/XPCServices/MetricMeasurementHelper.xpc/MetricMeasurementHelper`

```diff

-294.80.3.0.0
-  __TEXT.__text: 0x4d1c
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x5cc
+297.100.9.0.0
+  __TEXT.__text: 0x5b58
+  __TEXT.__auth_stubs: 0x630
+  __TEXT.__objc_stubs: 0xe20
+  __TEXT.__objc_methlist: 0x6a4
   __TEXT.__const: 0xb0
-  __TEXT.__objc_classname: 0x1f5
-  __TEXT.__objc_methname: 0xe2b
-  __TEXT.__objc_methtype: 0x42d
-  __TEXT.__cstring: 0x5bd
-  __TEXT.__oslogstring: 0x7fe
-  __TEXT.__gcc_except_tab: 0x134
+  __TEXT.__objc_classname: 0x20e
+  __TEXT.__objc_methname: 0x10aa
+  __TEXT.__objc_methtype: 0x58e
+  __TEXT.__cstring: 0x620
+  __TEXT.__oslogstring: 0xa4e
+  __TEXT.__gcc_except_tab: 0x124
   __TEXT.__ustring: 0x2e
-  __TEXT.__unwind_info: 0x188
-  __DATA_CONST.__auth_got: 0x360
-  __DATA_CONST.__got: 0x118
+  __TEXT.__unwind_info: 0x1c8
+  __DATA_CONST.__auth_got: 0x328
+  __DATA_CONST.__got: 0x128
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x190
-  __DATA_CONST.__cfstring: 0x3e0
+  __DATA_CONST.__cfstring: 0x440
   __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x58
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0xff0
-  __DATA.__objc_selrefs: 0x4c0
-  __DATA.__objc_ivar: 0x58
+  __DATA.__objc_const: 0x1100
+  __DATA.__objc_selrefs: 0x550
+  __DATA.__objc_ivar: 0x60
   __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x420
+  __DATA.__data: 0x480
   __DATA.__bss: 0x28
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/PrivateFrameworks/FunctionCoverage.framework/FunctionCoverage
   - /System/Library/PrivateFrameworks/MetricMeasurement.framework/MetricMeasurement
+  - /System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/PerfPowerMetricMonitor
   - /System/Library/PrivateFrameworks/PerformanceTrace.framework/PerformanceTrace
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpmsample.dylib
   - /usr/lib/libsysmon.dylib
-  UUID: 8DF5BAE9-3FCE-378B-A146-FE8A81EE3652
-  Functions: 101
-  Symbols:   181
-  CStrings:  390
+  UUID: 924E1DE8-8F25-322D-836D-0E538AAAC37E
+  Functions: 110
+  Symbols:   176
+  CStrings:  440
 
Symbols:
+ _OBJC_CLASS_$_PPSMetricMonitor
+ _OBJC_CLASS_$_PPSMetricMonitorConfiguration
- _objc_claimAutoreleasedReturnValue
- _objc_release_x28
- _objc_retain_x1
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x3
- _objc_retain_x8
CStrings:
+ "\t"
+ "  Signaling monitor ready semaphore due to error"
+ "@\"PPSMetricMonitor\""
+ "Failed to collect metrics snapshot: %@"
+ "Failed to initialize PPSMetricMonitor"
+ "Failed to initialize PPSMetricMonitor: %@"
+ "Failed to start monitoring processes: %@"
+ "MetricMeasurement timed out while waiting to start monitoring."
+ "MetricMeasurementHelper: MetricMonitor did become ready"
+ "MetricMeasurementHelper: PPSMetricMonitor ready"
+ "MetricMeasurementHelper: didUpdateWithMetrics"
+ "MetricMonitor ended unexpectedly with error: %@"
+ "MetricMonitor ready timeout"
+ "No PPSMetricMonitor available - setup was not called"
+ "PPSMetricMonitor already torn down"
+ "PPSMetricMonitor not initialized"
+ "PPSMetricMonitorDelegate"
+ "T@\"PPSMetricMonitor\",&,N,V_sharedMonitor"
+ "This build variant is unsupported. Try using an internal build variant."
+ "_monitorReadySemaphore"
+ "_sampleFromMetricMonitorWithProxyMetric:timeout:response:"
+ "_setupMetricMonitorWithProxyMetric:processNames:response:"
+ "_sharedMonitor"
+ "_teardownMetricMonitorWithProxyMetric:response:"
+ "collectMetricsOnSnapshot:"
+ "createMetricMonitorWithDelegate"
+ "defaultConfiguration"
+ "initWithConfiguration:delegate:error:"
+ "metricMonitor:didEndWithError:"
+ "metricMonitor:didUpdateWithMetrics:"
+ "metricMonitorDidBecomeReady:"
+ "metricMonitorInterruptionDidBegin:"
+ "metricMonitorInterruptionDidEnd:"
+ "setMode:"
+ "setSharedMonitor:"
+ "setUpdateDelegate:"
+ "sharedMonitor"
+ "startMonitoringProcessesWithName:error:"
+ "stopMonitoring"
+ "v24@0:8@\"PPSMetricMonitor\"16"
+ "v32@0:8@\"MXMProxyMetric\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"PPSMetricMonitor\"16@\"NSError\"24"
+ "v32@0:8@\"PPSMetricMonitor\"16@\"PPSMetricCollection\"24"
+ "v32@0:8@16@24"
+ "v40@0:8@\"MXMProxyMetric\"16@\"NSArray\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"MXMProxyMetric\"16d24@?<v@?@\"PPSMetricCollection\"Q@\"NSError\">32"
+ "v40@0:8@16@24@?32"

```
