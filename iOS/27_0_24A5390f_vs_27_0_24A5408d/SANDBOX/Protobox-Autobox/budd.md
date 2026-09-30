## budd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.passd.in-app-payment"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
+		(require-not (global-name "com.apple.aa.accountService.xpc"))
 		(require-not (global-name "com.apple.amsprivateidentifiers"))
 		(require-not (global-name "com.apple.PairingManager"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))

 		SYS_clonefileat
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
