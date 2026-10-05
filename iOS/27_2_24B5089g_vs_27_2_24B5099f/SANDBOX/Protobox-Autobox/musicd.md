## musicd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.kvsd"))
+		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.private.corewifi-xpc"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))

 		(require-not (global-name "com.apple.xpc.amstoold"))
 		(require-not (global-name "com.apple.amsprivateidentifiers"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.xpc.amsaccountsd"))
 		(require-not (global-name "com.apple.nesessionmanager"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.asktod"))
-		(require-not (global-name "com.apple.SBUserNotification"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))
 	)

 		SYS_psynch_rw_unlock
 		SYS_psynch_rw_unlock2
 		SYS_psynch_cvclrprepost
+		SYS_iopolicysys
 		SYS_issetugid
 		SYS___pthread_kill
 		SYS___pthread_sigmask
```
