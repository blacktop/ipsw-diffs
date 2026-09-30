## cameraispd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.locationd.synchronous"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.gpumemd.source"))
-		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.backlightd"))
-		(require-not (global-name "com.apple.locationd.registration"))
-		(require-not (global-name "com.apple.systemstatus.publisher"))
-		(require-not (global-name "com.apple.audio.AURemoteIOServer"))
-		(require-not (global-name "com.apple.coremedia.admin"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.tailspind"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.coremedia.admin"))
+		(require-not (global-name "com.apple.backlightd"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.systemstatus.publisher"))
+		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (global-name "com.apple.iohideventsystem"))
+		(require-not (global-name "com.apple.gpumemd.source"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.audio.AURemoteIOServer"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.appleneuralengine"))
 		(require-not (global-name "com.apple.analyticsd"))

 		SYS_open_dprotected_np
 		SYS_openat_dprotected_np
 		SYS_getattrlist
+		SYS_setattrlist
 		SYS_fgetattrlist
 		SYS_fsetattrlist
 		SYS_getxattr

 		SYS_bsdthread_terminate
 		SYS_kqueue
 		SYS_kevent
+		SYS_lchown
 		SYS_bsdthread_register
 		SYS_workq_open
 		SYS_workq_kernreturn
```
