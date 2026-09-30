## adprivacyd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.amsaccountsd.multiuser"))
 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```
