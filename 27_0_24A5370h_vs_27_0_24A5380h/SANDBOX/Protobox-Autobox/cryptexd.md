## cryptexd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.dnssd.service"))
-		(require-not (global-name "com.apple.nsurlsessiond.NSURLSessionProxyService"))
-		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.trustd"))
-		(require-not (global-name "com.apple.ctkd.token-client"))
-		(require-not (global-name "com.apple.installcoordinationd"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.nsurlsessiond.NSURLSessionProxyService"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.remoted"))
+		(require-not (global-name "com.apple.installcoordinationd"))
+		(require-not (global-name "com.apple.dnssd.service"))
+		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (xpc-service-name "com.apple.diskimagescontroller"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))

 (deny sysctl-write
 	(require-all
 		(sysctl-name "vm.debug_range_enabled")
-		(require-not (sysctl-name "security.mac.image4.nonce.copy_hash"))
 		(require-not (sysctl-name "vm.debug_range_enabled"))
+		(require-not (sysctl-name "security.mac.image4.nonce.copy_hash"))
 		(require-not (sysctl-name "kern.wq_limit_cooperative_threads"))
 		(require-not (system-attribute developer-mode))
 	)
```
