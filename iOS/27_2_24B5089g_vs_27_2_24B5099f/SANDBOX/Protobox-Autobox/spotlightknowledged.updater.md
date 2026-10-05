## spotlightknowledged.updater

> Group: ⬆️ Updated

```diff

 			(global-name "com.apple.cascade.donationrequest.SensedUserContext.Place")
 			(global-name "com.apple.cascade.donationrequest.Siri.Transcript.Turn")
 		))
+		(require-not (global-name "com.apple.corepersonalization.server.graphEmbedding"))
 		(require-not (global-name "com.apple.appleneuralengine"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))

 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
+				(require-not (global-name "com.apple.FileCoordination"))
 				(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 				(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 				(require-not (system-attribute developer-mode))

 				(xpc-service-name "*")
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
+				(require-not (global-name "com.apple.FileCoordination"))
 				(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 				(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 				(require-not (system-attribute developer-mode))
```
