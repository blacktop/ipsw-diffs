## SiriTTSTrainingAgent

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.gpumemd.source"))
-		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
 		(require-not (global-name "com.apple.tailspind"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.audioanalyticsd"))
-		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
 		(require-not (global-name "com.apple.triald.namespace-management"))
+		(require-not (global-name "com.apple.gpumemd.source"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.FileCoordination"))

 		SYS_lseek
 		SYS_ftruncate
 		SYS_sysctl
+		SYS_mlock
+		SYS_munlock
 		SYS_getumask
 		SYS_open_dprotected_np
 		SYS_openat_dprotected_np
```
