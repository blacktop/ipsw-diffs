## FPCKService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.FileProvider"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
-		(require-not (global-name "com.apple.debug.telemetry"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.revisiond"))
+		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.cache_delete"))
-		(require-not (global-name "com.apple.FileProvider"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.revisiond"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (system-attribute developer-mode))
 	)
```
