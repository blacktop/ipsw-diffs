## SyncAgent

> Group: ⬆️ Updated

```diff

 	(with no-report)
 	(require-all
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.safarifetcherd"))
+		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))
 		(require-not (global-name "com.apple.calaccessd"))
 		(require-not (global-name "com.apple.mobile.heartbeat"))
 		(require-not (global-name "com.apple.calaccessd.xpc"))

 (deny mach-lookup
 	(require-all
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.safarifetcherd"))
+		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))
 		(require-not (global-name "com.apple.calaccessd"))
 		(require-not (global-name "com.apple.mobile.heartbeat"))
 		(require-not (global-name "com.apple.calaccessd.xpc"))

 		semaphore_create
 		semaphore_destroy
 		task_create_identity_token
+		thread_policy_set
 		vm_remap_external
 		vm_reallocate
 		mach_vm_copy
```
