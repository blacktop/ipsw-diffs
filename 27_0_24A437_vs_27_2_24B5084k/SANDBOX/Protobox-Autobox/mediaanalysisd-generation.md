## mediaanalysisd-generation

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.modelmanager"))
 		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))

 	(fcntl-command
 		F_SETFD
 		F_GETFL
+		F_PREALLOCATE
 		F_NOCACHE
 		F_GETPATH
 		F_GETPROTECTIONCLASS
```
