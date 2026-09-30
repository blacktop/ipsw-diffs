## remoteappintentsd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
-		(require-not (global-name "com.apple.breadboardservices"))
+		(require-not (global-name "com.apple.linkd.registry"))
+		(require-not (global-name "com.apple.linkd.extension"))
+		(require-not (global-name "com.apple.appprotectiond.guard"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.linkd.transcript"))
-		(require-not (global-name "com.apple.locationd.registration"))
-		(require-not (global-name "com.apple.appprotectiond.guard"))
-		(require-not (global-name "com.apple.appprotectiond.read"))
-		(require-not (global-name "com.apple.pearld"))
-		(require-not (global-name "com.apple.linkd.extension"))
-		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
-		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))
 		(require-not (require-any
 			(global-name "com.apple.findmy.findmylocate.friendshipservice")
 			(global-name "com.apple.findmy.findmylocate.settings")
 		))
-		(require-not (global-name "com.apple.biometrickitd"))
 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.linkd.observationStatusRegistry"))
-		(require-not (global-name "com.apple.findmy.findmylocate.locationservice"))
-		(require-not (global-name "com.apple.ProgressReporting"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
-		(require-not (global-name "com.apple.linkd.registry"))
+		(require-not (global-name "com.apple.findmy.findmylocate.locationservice"))
+		(require-not (global-name "com.apple.biometrickitd"))
 		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
+		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
+		(require-not (global-name "com.apple.pearld"))
+		(require-not (global-name "com.apple.breadboardservices"))
+		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))
+		(require-not (global-name "com.apple.ProgressReporting"))
+		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
+		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (global-name "com.apple.CompanionLink"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))

 			SYS_kdebug_trace
 			SYS_sigreturn
 			SYS_pathconf
+			SYS_fpathconf
 			SYS_lseek
 			SYS_ftruncate
 			SYS_sysctl
```
