## featureaccessd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.ind.cloudfeatures"))
-		(require-not (global-name "com.apple.aa.daemon.xpc"))
-		(require-not (global-name "com.apple.mobileactivationd"))
-		(require-not (global-name "com.apple.generativeexperiences.availabilityService"))
-		(require-not (global-name "com.apple.ind.xpc"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.TapToRadarKit.service"))
-		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
+		(require-not (global-name "com.apple.generativeexperiences.availabilityService"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
-		(require-not (global-name "com.apple.modelcatalog.catalog"))
+		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.timed.xpc"))
+		(require-not (global-name "com.apple.aa.daemon.xpc"))
+		(require-not (global-name "com.apple.modelcatalog.catalog"))
+		(require-not (global-name "com.apple.ind.cloudfeatures"))
+		(require-not (global-name "com.apple.ind.xpc"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
+		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (system-attribute developer-mode))
```
