## subridged

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.mobilegestalt.xpc"))
+		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.SBUserNotification"))
+		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.springboard.services"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.FileCoordination"))
-		(require-not (global-name "com.apple.nanoregistry.termsacknowledgementregistry"))
-		(require-not (global-name "com.apple.SBUserNotification"))
-		(require-not (global-name "com.apple.springboard.services"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.sharingd.nsxpc"))
-		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
-		(require-not (global-name "com.apple.mobilegestalt.xpc"))
+		(require-not (global-name "com.apple.nanoregistry.termsacknowledgementregistry"))
+		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent"))
 		(require-not (system-attribute developer-mode))
 	)
```
