## ASPCarryLog

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.diagnosticpipeline.tasking.service"))
-		(require-not (global-name "com.apple.debug.telemetry"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.familycircle.agent"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.mobile.softwareupdated"))
-		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.mobile.softwareupdated"))
 		(require-not (global-name "com.apple.cache_delete.public"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
+		(require-not (global-name "com.apple.diagnosticpipeline.tasking.service"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.debug.telemetry"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.familycircle.agent"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.cache_delete"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.FileCoordination"))
```
