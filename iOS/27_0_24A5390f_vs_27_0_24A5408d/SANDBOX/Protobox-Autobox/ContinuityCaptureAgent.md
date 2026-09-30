## ContinuityCaptureAgent

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.tailspind"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.nearbyd.xpc.nearbyinteraction"))
 		(require-not (global-name "com.apple.tccd"))

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
