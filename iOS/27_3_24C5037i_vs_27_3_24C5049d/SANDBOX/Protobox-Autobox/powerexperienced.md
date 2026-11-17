## powerexperienced

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.powerd.extendedbattery"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.powerui.smartChargeManager"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.powerexperienced.resourceusage"))

 		(require-not (global-name "com.apple.OSIntelligence.charging"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.batteryintelligenced.thermalprediction"))
 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.OSIntelligence.battery"))
 		(require-not (global-name "com.apple.iohideventsystem"))

 		task_set_special_port
 		thread_create_from_user
 		semaphore_create
+		semaphore_destroy
 		task_set_exc_guard_behavior
 		thread_policy
 		thread_policy_set
```
