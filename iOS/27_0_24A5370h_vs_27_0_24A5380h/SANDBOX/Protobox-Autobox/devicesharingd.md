## devicesharingd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.devicesharingd"))
 		(require-not (global-name "com.apple.mobile.keybagd.xpc"))
-		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
-		(require-not (global-name "com.apple.debug.telemetry"))
+		(require-not (global-name "com.apple.devicesharingd.enrollmentassetservice"))
 		(require-not (global-name "com.apple.kvsd"))
+		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
+		(require-not (global-name "com.apple.devicesharingd"))
+		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
 		(require-not (global-name "com.apple.pearld"))
 		(require-not (global-name "com.apple.sharingd.nsxpc"))
-		(require-not (global-name "com.apple.devicesharingd.enrollmentassetservice"))
+		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
-		(require-not (global-name "com.apple.erm.logging"))
-		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (system-attribute developer-mode))
 	)
```
