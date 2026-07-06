## speechmodeltrainingd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.sirittsd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.privacyaccountingd"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (global-name "com.apple.medialibraryd.xpc"))
 		(require-not (global-name "com.apple.remoted"))
+		(require-not (global-name "com.apple.privacyaccountingd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.itunescloudd.xpc"))
+		(require-not (global-name "com.apple.sirittsd"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.medialibraryd.xpc"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.itunescloudd.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (xpc-service-name "com.apple.siri.embeddedspeech"))
 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
+		(require-not (xpc-service-name "com.apple.siri.embeddedspeech"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (system-attribute developer-mode))
 	)
```
