## DisplayArchiveService

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))

 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))
 	)
```
