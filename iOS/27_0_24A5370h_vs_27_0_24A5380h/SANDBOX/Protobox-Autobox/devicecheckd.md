## devicecheckd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.lsd.icons"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.lsd.xpc"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
-		(require-not (global-name "com.apple.mobileassetd.v2"))
-		(require-not (global-name "com.apple.debug.telemetry"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.mobileactivationd"))
-		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
+		(require-not (global-name "com.apple.duetactivityscheduler"))
+		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.lsd.xpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.mobileactivationd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.erm.logging"))
-		(require-not (global-name "com.apple.duetactivityscheduler"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
+		(require-not (global-name "com.apple.securityd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.debug.telemetry"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (xpc-service-name "com.apple.AppleVirtualPlatform.IdentityService"))
+		(require-not (xpc-service-name "com.apple.pvappidentityservice"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon.libxpc"))

 		SYS_munmap
 		SYS_mprotect
 		SYS_madvise
+		SYS_dup2
 		SYS_fcntl
 		SYS_select
 		SYS_fsync
```
