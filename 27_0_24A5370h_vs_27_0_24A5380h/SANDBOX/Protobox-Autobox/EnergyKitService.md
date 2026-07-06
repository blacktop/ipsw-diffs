## EnergyKitService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.symptom_diagnostics"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
+		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
+		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (global-name "com.apple.homekitevents.xpc"))
 		(require-not (require-any
 			(global-name "com.apple.energykit.localStore")
 			(global-name "com.apple.energykit.privateStore")
 			(global-name "com.apple.energykit.sharedStore")
 		))
-		(require-not (global-name "com.apple.locationd.registration"))
-		(require-not (global-name "com.apple.mobileactivationd"))
-		(require-not (global-name "com.apple.homekitevents.xpc"))
-		(require-not (global-name "com.apple.symptom_diagnostics"))
-		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (system-attribute developer-mode))
 	)
```
