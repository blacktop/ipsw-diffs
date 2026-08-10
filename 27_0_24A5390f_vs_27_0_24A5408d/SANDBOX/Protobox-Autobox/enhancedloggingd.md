## enhancedloggingd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.ak.anisette.xpc"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.cloudd"))

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
