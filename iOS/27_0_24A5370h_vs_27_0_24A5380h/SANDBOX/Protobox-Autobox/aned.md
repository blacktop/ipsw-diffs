## aned

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.ANECompilerService")

 			(xpc-service-name "com.apple.private.ANEStorageMaintainer")
 		))
 		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))

 	(deny system-mac-syscall
 		(require-all
 			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 80))
 			(require-not (mac-syscall-number 6))
 			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number (_IO "" 8)))
```
