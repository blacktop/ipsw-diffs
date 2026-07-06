## com.apple.dt.instruments.dtsecurity

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.coresymbolicationd"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.coresymbolicationd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (system-attribute developer-mode))
 	)

 (deny sysctl-write
 	(require-all
 		(sysctl-name "vm.debug_range_enabled")
-		(require-not (sysctl-name "vm.debug_range_enabled"))
 		(require-not (require-any
 			(sysctl-name "kpc.period")
 			(sysctl-name "kperf.action.filter_by_pid")

 			(sysctl-name "kperf.timer.action")
 			(sysctl-name "kperf.timer.period")
 		))
+		(require-not (sysctl-name "vm.debug_range_enabled"))
 		(require-not (require-any
 			(sysctl-name "kpc.actionid")
 			(sysctl-name "kpc.config")
```
