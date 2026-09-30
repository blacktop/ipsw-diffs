## restoreserviced

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.centaurid.xpc"))
-		(require-not (global-name "com.apple.commcenter.xpc"))
 		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.nearbyd.xpc.diagnostics"))
-		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.commcenter.xpc"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.nfcd.hwmanager"))
+		(require-not (global-name "com.apple.centaurid.xpc"))
+		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.nearbyd.xpc.diagnostics"))
+		(require-not (global-name "com.apple.cameraispd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.cameraispd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
-		(require-not (global-name "com.apple.appleh16camerad"))
 		(require-not (global-name "com.apple.appleh13camerad"))
+		(require-not (global-name "com.apple.appleh16camerad"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
