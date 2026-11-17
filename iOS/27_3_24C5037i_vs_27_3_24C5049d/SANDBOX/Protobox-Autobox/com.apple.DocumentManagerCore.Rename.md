## com.apple.DocumentManagerCore.Rename

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.FileProvider"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.bird.token"))
 		(require-not (global-name "com.apple.system.notification_center"))

 		(require-not (global-name "com.apple.iconservices"))
 		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.coresymbolicationd"))
+		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.bird"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.DesktopServicesHelper"))
+		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.cache_delete.public"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.cache_delete"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.revisiond"))
-		(require-not (global-name "com.apple.FileProvider"))
-		(require-not (global-name "com.apple.DesktopServicesHelper"))
-		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.FileCoordination"))
+		(require-not (global-name "com.apple.cache_delete"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.FSEvents"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.ProgressReporting"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.revisiond"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
