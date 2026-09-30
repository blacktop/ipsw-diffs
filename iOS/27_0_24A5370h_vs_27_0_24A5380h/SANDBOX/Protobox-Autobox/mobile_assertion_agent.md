## mobile_assertion_agent

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.mobile.heartbeat"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.trustd"))
-		(require-not (global-name "com.apple.iokit.powerdxpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.mobile.heartbeat"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.iokit.powerdxpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.aggregated"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (system-attribute developer-mode))
```
