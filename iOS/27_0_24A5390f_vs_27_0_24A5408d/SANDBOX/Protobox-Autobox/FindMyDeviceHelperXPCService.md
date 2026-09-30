## FindMyDeviceHelperXPCService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc"))
 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (global-name "com.apple.coremedia.mediaparserd.formatreader.xpc"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.sandboxserver.xpc"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.asset.xpc"))

 		SYS_sysctl
 		SYS_getumask
 		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
 		SYS_getattrlist
 		SYS_fgetattrlist
 		SYS_fgetxattr

 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_unlinkat
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_guarded_open_dprotected_np
 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
 		SYS_guarded_writev_np
```
