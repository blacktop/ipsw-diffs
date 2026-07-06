## networkdiagnosticsd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.logd.admin"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.logd.admin"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (system-attribute developer-mode))
 	)

 (deny sysctl-write
 	(require-all
 		(sysctl-name "vm.debug_range_enabled")
+		(require-not (require-any
+			(sysctl-name "net.inet6.icmp6.nd6_debug")
+			(sysctl-name "net.route.verbose")
+		))
 		(require-not (require-any
 			(sysctl-name "net.diagnose.on")
 			(sysctl-name "net.inet.ip.log.privacy")

 			(sysctl-name "net.inet.udp.log.enable")
 		))
 		(require-not (sysctl-name "vm.debug_range_enabled"))
-		(require-not (require-any
-			(sysctl-name "net.inet6.icmp6.nd6_debug")
-			(sysctl-name "net.route.verbose")
-		))
 		(require-not (sysctl-name "kern.wq_limit_cooperative_threads"))
 		(require-not (system-attribute developer-mode))
 	)
```
