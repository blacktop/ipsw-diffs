## srp-mdns-proxy

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.mDNSResponder_Helper"))
+		(require-not (global-name "com.apple.mDNSResponder.control"))
 		(require-not (global-name "com.apple.wpantund.xpc"))
 		(require-not (global-name "com.apple.network.IPConfiguration"))
-		(require-not (global-name "com.apple.mDNSResponder.control"))
 		(require-not (global-name "com.apple.pfd"))
 		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
+		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (system-attribute developer-mode))
 	)
```
