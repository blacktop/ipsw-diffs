## ManagedAppsSubscriber

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.remotemanagementd.store"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
+		(require-not (global-name "com.apple.lsd.modifydb"))
 		(require-not (global-name "com.apple.dmd"))
 		(require-not (global-name "com.apple.devicemanagementclient.managedappsd"))
 		(require-not (global-name "com.apple.diagd"))
```
