## skateboardcompaniond

> Group: ⬆️ Updated

```diff

 
 (deny mach-lookup
 	(require-all
-		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
+		(require-not (global-name "com.apple.terminusd"))
+		(require-not (global-name "com.apple.securityd"))
+		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.terminusd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-any
 			(process-attribute is-autoboxed)
 			(require-all
```
