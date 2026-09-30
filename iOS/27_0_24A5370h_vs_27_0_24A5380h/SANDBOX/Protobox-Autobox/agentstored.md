## agentstored

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.generativesearch.server.search"))
-		(require-not (global-name "com.apple.accountsd.accountmanager"))
-		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.SBUserNotification"))
-		(require-not (global-name "com.apple.fontservicesd"))
-		(require-not (global-name "com.apple.kvsd"))
-		(require-not (global-name "com.apple.photos.service"))
 		(require-not (global-name "com.apple.biome.access.user"))
-		(require-not (global-name "com.apple.duetactivityscheduler"))
-		(require-not (global-name "com.apple.cloudkit.partlycloudd"))
-		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.linkd.registry"))
-		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
+		(require-not (global-name "com.apple.duetactivityscheduler"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.accountsd.accountmanager"))
+		(require-not (global-name "com.apple.kvsd"))
+		(require-not (global-name "com.apple.SBUserNotification"))
+		(require-not (global-name "com.apple.cloudkit.partlycloudd"))
+		(require-not (global-name "com.apple.fontservicesd"))
+		(require-not (global-name "com.apple.photos.service"))
+		(require-not (global-name "com.apple.generativesearch.server.search"))
 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
+		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))

 		mach_exception_raise
 		mach_exception_raise_state
 		mach_exception_raise_state_identity
+		io_registry_create_iterator
 		io_registry_entry_from_path
 		io_service_open_extended
 		io_connect_method
```
