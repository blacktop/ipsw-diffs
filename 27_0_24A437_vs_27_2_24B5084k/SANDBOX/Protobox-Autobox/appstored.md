## appstored

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.appstored.xpc"))
 		(require-not (global-name "com.apple.spotlight.IndexAgent"))
 		(require-not (global-name "com.apple.biometrickitd"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.modelmanager"))
 		(require-not (global-name "com.apple.symptom_analytics"))
 		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.appmanagedfeatures.configuration"))
 		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.AssetCacheLocatorService"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))

 		(require-not (global-name "com.apple.corereporting.report-services"))
 		(require-not (global-name "com.apple.jetpackassetd.xpc"))
 		(require-not (global-name "com.apple.backupd"))
+		(require-not (global-name "com.apple.fairplayd"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
 		(require-not (global-name "com.apple.audio.AudioQueueServer"))

 		SYS_recvmsg
 		SYS_sendmsg
 		SYS_recvfrom
+		SYS_getsockname
 		SYS_access
 		SYS_crossarch_trap
 		SYS_dup
```
