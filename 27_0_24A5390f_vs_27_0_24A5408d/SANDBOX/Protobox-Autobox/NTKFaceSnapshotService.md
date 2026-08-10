## NTKFaceSnapshotService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.TextInput"))
 		(require-not (global-name "com.apple.accessibility.mediaaccessibilityd"))
 		(require-not (global-name "com.apple.ExternalAccessory.distributednotification.server"))
+		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
 		(require-not (global-name "com.apple.MobileTimer.timerserver"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.iap2d.xpc"))

 		SYS_clonefileat
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
