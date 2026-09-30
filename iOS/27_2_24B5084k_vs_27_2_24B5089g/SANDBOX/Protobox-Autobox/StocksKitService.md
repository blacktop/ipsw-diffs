## StocksKitService

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
```
