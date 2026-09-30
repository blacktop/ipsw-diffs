## mediasetupd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.assistant.multiuser.service"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.accountsd.accountmanager"))
-		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.debug.telemetry"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.familycircle.agent"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.itunescloud.music-subscription-status-service"))
-		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
-		(require-not (global-name "com.apple.iconservices"))
-		(require-not (global-name "com.apple.locationd.registration"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.mobileactivationd"))
-		(require-not (global-name "com.apple.homehubd.manage"))
-		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
-		(require-not (global-name "com.apple.homed.xpc"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.amsaccountsd.multiuser"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
+		(require-not (global-name "com.apple.itunescloud.music-subscription-status-service"))
+		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.iconservices"))
+		(require-not (global-name "com.apple.accountsd.accountmanager"))
+		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.homehubd.manage"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.amsaccountsd.multiuser"))
+		(require-not (global-name "com.apple.mobileactivationd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.assistant.multiuser.service"))
+		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.erm.logging"))
-		(require-not (global-name "com.apple.duetactivityscheduler"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.datamigrator"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (global-name "com.apple.homed.xpc"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.debug.telemetry"))
+		(require-not (global-name "com.apple.datamigrator"))
+		(require-not (global-name "com.apple.familycircle.agent"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (xpc-service-name "com.apple.itunescloud.music-subscription-status-service"))
+		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))

 		SYS_fsetattrlist
 		SYS_getxattr
 		SYS_setxattr
+		SYS_listxattr
 		SYS_fsctl
 		SYS_shm_open
 		SYS_sysctlbyname
```
