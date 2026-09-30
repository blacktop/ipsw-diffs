## watchdogd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.modelmanager"))
-		(require-not (global-name "com.apple.trial.status"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.translation.text"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.SystemConfiguration.configd"))
-		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.corereporting.report-services"))
-		(require-not (global-name "com.apple.debug.telemetry"))
-		(require-not (global-name "com.apple.SBUserNotification"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.biome.access.user"))
+		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
+		(require-not (global-name "com.apple.biome.access.system"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.translation.text"))
+		(require-not (global-name "com.apple.tailspind"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.coresymbolicationd"))
+		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
-		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.OTATaskingAgent"))
-		(require-not (global-name "com.apple.DeviceRecoveryEnvironmentService"))
-		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
-		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (require-any
 			(global-name "com.apple.runningboard.watchdog")
 			(global-name "com.apple.unblock")
 		))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.OTATaskingAgent"))
+		(require-not (global-name "com.apple.usernotifications.listener"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.DeviceRecoveryEnvironmentService"))
+		(require-not (global-name "com.apple.SystemConfiguration.configd"))
+		(require-not (global-name "com.apple.modelmanager"))
+		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.AppSSO.service-xpc"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.runningboard"))
 		(require-not (require-any
 			(global-name "com.apple.CarPlayApp.oswatchdog")
 			(global-name "com.apple.PreBoard.oswatchdog")

 			(global-name "com.apple.watchdogtestoptin.watchdog")
 			(global-name "com.apple.wifid.watchdog")
 		))
-		(require-not (global-name "com.apple.biome.access.user"))
-		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.erm.logging"))
-		(require-not (global-name "com.apple.coresymbolicationd"))
-		(require-not (global-name "com.apple.diagnosticpipeline.service"))
-		(require-not (global-name "com.apple.tailspind"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.biome.access.system"))
+		(require-not (global-name "com.apple.trial.status"))
+		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.corereporting.report-services"))
 		(require-not (global-name "com.apple.lsd.advertisingidentifiers"))
-		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.usernotifications.listener"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.diagnosticpipeline.service"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.debug.telemetry"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.frontboard.systemappservices"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (system-attribute developer-mode))
 	)

 		task_set_special_port
 		semaphore_create
 		semaphore_destroy
+		task_suspend2
+		task_resume2
 		task_map_corpse_info_64
 		task_set_exc_guard_behavior
 		mach_task_is_self
```
