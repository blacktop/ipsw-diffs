## UARPAssetManagerServiceMobileAsset

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.mobileassetd.v2"))
-		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		SYS_psynch_rw_wrlock
 		SYS_psynch_rw_unlock
 		SYS_psynch_rw_unlock2
+		SYS_iopolicysys
 		SYS_issetugid
 		SYS___pthread_kill
 		SYS___pthread_sigmask
```
