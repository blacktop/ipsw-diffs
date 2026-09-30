## fpassetmanagerd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.dnssd.service"))

 		SYS_open_dprotected_np
 		SYS_openat_dprotected_np
 		SYS_getattrlist
+		SYS_fgetattrlist
 		SYS_getxattr
 		SYS_setxattr
 		SYS_listxattr

 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
+		SYS_unlinkat
 		SYS_mkdirat
 		SYS_bsdthread_ctl
 		SYS_guarded_open_dprotected_np
```
