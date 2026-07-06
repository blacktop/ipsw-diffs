## amsondevicestoraged

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.fairplayd.versioned"))
-		(require-not (global-name "com.apple.fairplayd"))
-		(require-not (global-name "com.apple.xpc.amstoold"))
-		(require-not (global-name "com.apple.jetpackassetd.xpc"))
-		(require-not (global-name "com.apple.fairplayd.xpc"))
-		(require-not (global-name "com.apple.symptom_analytics"))
-		(require-not (global-name "com.apple.xpc.amsaccountsd"))
-		(require-not (global-name "com.apple.xpc.amsengagementd"))
-		(require-not (global-name "com.apple.amsservicesanalytics.xpc"))
-		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
-		(require-not (global-name "com.apple.dt.automationmode.reader"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
+		(require-not (global-name "com.apple.iokit.powerdxpc"))
+		(require-not (global-name "com.apple.xpc.amsengagementd"))
+		(require-not (global-name "com.apple.dt.automationmode.reader"))
+		(require-not (global-name "com.apple.fairplayd.versioned"))
+		(require-not (global-name "com.apple.symptom_analytics"))
+		(require-not (global-name "com.apple.amsservicesanalytics.xpc"))
+		(require-not (global-name "com.apple.fairplayd.xpc"))
+		(require-not (global-name "com.apple.jetpackassetd.xpc"))
+		(require-not (global-name "com.apple.fairplayd"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
+		(require-not (global-name "com.apple.xpc.amstoold"))
+		(require-not (global-name "com.apple.xpc.amsaccountsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
```
