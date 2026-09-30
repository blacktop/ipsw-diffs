## AudioAccessoryAssetManagementXPCService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.linkd.registry"))
+		(require-not (global-name "com.apple.duetactivityscheduler"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.spotlight.IndexAgent"))
-		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
-		(require-not (global-name "com.apple.frontboard.systemappservices"))
-		(require-not (global-name "com.apple.linkd.registry"))
-		(require-not (xpc-service-name "com.apple.AudioAccessoryAssetManagementXPCService"))
+		(require-not (global-name "com.apple.spotlight.IndexAgent"))
 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
+		(require-not (xpc-service-name "com.apple.AudioAccessoryAssetManagementXPCService"))
 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))
```
