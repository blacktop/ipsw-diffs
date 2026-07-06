## ReportSystemMemory

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.osanalytics.report-services"))
-		(require-not (global-name "com.apple.corereporting.report-services"))
-		(require-not (global-name "com.apple.rtcreportingd"))
-		(require-not (global-name "com.apple.debug.telemetry"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.OTATaskingAgent"))
-		(require-not (global-name "com.apple.DeviceRecoveryEnvironmentService"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.coresymbolicationd"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.rtcreportingd"))
+		(require-not (global-name "com.apple.osanalytics.report-services"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.OTATaskingAgent"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.DeviceRecoveryEnvironmentService"))
+		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.corereporting.report-services"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.debug.telemetry"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
