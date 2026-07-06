## tailspind

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.trial.status"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.SystemConfiguration.configd"))
-		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
-		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.powerexperienced.powermitigationsmanager.service"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.logd.admin"))
-		(require-not (global-name "com.apple.geod"))
-		(require-not (global-name "com.apple.coresymbolicationd"))
+		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
-		(require-not (global-name "com.apple.tailspind"))
-		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.biome.access.system"))
-		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.tailspind"))
+		(require-not (global-name "com.apple.powerexperienced.powermitigationsmanager.service"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.coresymbolicationd"))
+		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.geod"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.logd.admin"))
+		(require-not (global-name "com.apple.trial.status"))
 		(require-not (global-name "com.apple.computesafeguards.managing"))
-		(require-not (xpc-service-name "com.apple.swiftuitracingsupport.xpc"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (xpc-service-name "com.apple.tailspin.symbolicationserver"))
+		(require-not (xpc-service-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))

 
 (deny process-exec*
 	(require-all
-		(require-not (literal "/usr/bin/plutil"))
 		(require-not (literal "/usr/bin/tailspin"))
+		(require-not (literal "/usr/bin/plutil"))
 		(require-not (literal "/bin/sh"))
 	)
 )

 (deny sysctl-write
 	(require-all
 		(sysctl-name "vm.debug_range_enabled")
-		(require-not (require-any
-			(sysctl-name "kperf.lazy.cpu_time_threshold")
-			(sysctl-name "ktrace.init_background")
-		))
 		(require-not (require-any
 			(sysctl-name "kperf.action.count")
 			(sysctl-name "kperf.kdebug.action")

 			(sysctl-name "kperf.sampling")
 			(sysctl-name "kperf.timer.count")
 		))
-		(require-not (sysctl-name "kperf.lazy.cpu_action"))
-		(require-not (require-any
-			(sysctl-name "kperf.lightweight_pet")
-			(sysctl-name "kperf.timer.pet_timer")
-		))
-		(require-not (sysctl-name "vm.debug_range_enabled"))
 		(require-not (require-any
 			(sysctl-name "kpc.actionid")
 			(sysctl-name "kpc.config")

 			(sysctl-name "kperf.timer.action")
 			(sysctl-name "kperf.timer.period")
 		))
+		(require-not (sysctl-name "vm.debug_range_enabled"))
+		(require-not (require-any
+			(sysctl-name "kperf.lazy.cpu_time_threshold")
+			(sysctl-name "ktrace.init_background")
+		))
+		(require-not (require-any
+			(sysctl-name "kperf.lightweight_pet")
+			(sysctl-name "kperf.timer.pet_timer")
+		))
+		(require-not (sysctl-name "kperf.lazy.cpu_action"))
 		(require-not (sysctl-name "kern.grade_cputype"))
 		(require-not (sysctl-name "kern.wq_limit_cooperative_threads"))
 		(require-not (system-attribute developer-mode))

 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
+			(require-not (mac-syscall-number 80))
 			(require-not (mac-syscall-number 7))
 			(require-not (mac-syscall-number 67))
 			(require-not (mac-syscall-number 6))
```
