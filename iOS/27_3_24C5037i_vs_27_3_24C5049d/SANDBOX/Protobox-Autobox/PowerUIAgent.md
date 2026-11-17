## PowerUIAgent

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.powerexperienced.resourceusage"))
 		(require-not (global-name "com.apple.coreservices.lsuseractivitymanager.xpc"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.powerd.lowpowermode"))
 		(require-not (global-name "com.apple.carkit.app.service"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
```
