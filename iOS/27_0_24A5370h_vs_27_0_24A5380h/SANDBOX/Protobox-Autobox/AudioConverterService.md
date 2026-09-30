## AudioConverterService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.lskdd.xpc"))
 		(require-not (global-name "com.apple.translation.text"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.lskdd.xpc"))
 		(require-not (global-name "com.apple.remindd"))
-		(require-not (xpc-service-name "com.apple.SpatialAudioXPCService"))
-		(require-not (xpc-service-name "com.apple.SpatialAudioProfileXPCService"))
-		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
-		(require-not (xpc-service-name "com.apple.remindd"))
 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
+		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (xpc-service-name "com.apple.SpatialAudioProfileXPCService"))
+		(require-not (xpc-service-name "com.apple.remindd"))
+		(require-not (xpc-service-name "com.apple.SpatialAudioXPCService"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.audioanalyticsd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
-		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.fairplayd.xpc"))
-		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.lskdd"))
 		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.audioanalyticsd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (system-attribute developer-mode))
 	)

 
 (deny system-fcntl)
 (allow system-fcntl
-	(fcntl-command F_SETFD F_GETFL F_GETPATH F_ADDFILESIGS_RETURN F_CHECK_LV)
+	(fcntl-command
+		F_SETFD
+		F_GETFL
+		F_RDADVISE
+		F_GETPATH
+		F_ADDFILESIGS_RETURN
+		F_CHECK_LV)
 )
 
 (deny system-fsctl)
```
