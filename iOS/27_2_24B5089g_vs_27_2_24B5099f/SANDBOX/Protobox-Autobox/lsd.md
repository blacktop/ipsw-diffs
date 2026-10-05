## lsd

> Group: ⬆️ Updated

```diff

 			(global-name "com.apple.CoreServices.fshelper")
 			(global-name "com.apple.mdt")
 			(global-name "com.apple.ondemandd.launchservices")
+			(global-name "com.apple.rtu.urlpolicy")
 		))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.coreservices.lsuseractivitymanager.xpc"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
+				(require-not (global-name "com.apple.coreservices.lsuseractivitymanager.xpc"))
+				(require-not (global-name "com.apple.distributed_notifications@1v3"))
 				(require-not (global-name "com.apple.springboard.services"))
 				(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 				(require-not (global-name "com.apple.lsd.modifydb"))

 					(xpc-service-name "com.apple.AppTrackingTransparency.EnforcementService")
 				))
 				(require-not (xpc-service-name #"^com[.]apple[.].+[.]appremoval$"))
+				(require-not (global-name "com.apple.coreservices.lsuseractivitymanager.xpc"))
+				(require-not (global-name "com.apple.distributed_notifications@1v3"))
 				(require-not (global-name "com.apple.springboard.services"))
 				(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 				(require-not (global-name "com.apple.lsd.modifydb"))
```
