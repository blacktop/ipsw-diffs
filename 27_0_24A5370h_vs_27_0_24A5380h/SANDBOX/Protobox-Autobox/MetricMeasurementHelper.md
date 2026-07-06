## MetricMeasurementHelper

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.functioncoveragehelperd"))
 		(require-not (global-name "com.apple.sysmond"))
+		(require-not (global-name "com.apple.functioncoveragehelperd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (xpc-service-name "com.apple.PerformanceTrace.PerformanceTraceService"))
 		(require-not (global-name "com.apple.PerfPowerMetricMonitor.xpc"))
 		(require-not (system-attribute developer-mode))
```
