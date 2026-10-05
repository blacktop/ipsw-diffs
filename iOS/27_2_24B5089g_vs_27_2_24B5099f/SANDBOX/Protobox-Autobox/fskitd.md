## fskitd

> Group: ⬆️ Updated

```diff

 
 (deny mach-lookup
 	(require-all
-		(require-not (global-name "com.apple.FileProvider"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))

 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
+				(require-not (global-name "com.apple.FileProvider"))
+				(require-not (global-name "com.apple.FileCoordination"))
 				(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 				(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 				(require-not (system-attribute developer-mode))

 				))
 				(require-not (xpc-service-name "com.apple.extensionkitservice"))
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
+				(require-not (global-name "com.apple.FileProvider"))
+				(require-not (global-name "com.apple.FileCoordination"))
 				(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 				(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 				(require-not (system-attribute developer-mode))
```
