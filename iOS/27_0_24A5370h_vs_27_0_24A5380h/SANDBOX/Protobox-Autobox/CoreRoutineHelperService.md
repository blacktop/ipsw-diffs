## CoreRoutineHelperService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.gpumemd.source"))
-		(require-not (global-name "com.apple.trustd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.Maps.mapspushd.geoservices"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3"))
+		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.TapToRadarKit.service"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.Maps.mapspushd.geoservices"))
+		(require-not (global-name "com.apple.gpumemd.source"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (system-attribute developer-mode))

 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
+			(require-not (mac-syscall-number 80))
 			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number 67))
 			(require-not (mac-syscall-number 2))
```
