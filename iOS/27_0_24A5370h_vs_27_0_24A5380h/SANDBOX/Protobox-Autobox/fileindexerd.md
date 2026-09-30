## fileindexerd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
-		(require-not (global-name "com.apple.bird"))
-		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (global-name "com.apple.mobile.keybagd.xpc"))
-		(require-not (global-name "com.apple.revisiond"))
-		(require-not (global-name "com.apple.FileProvider"))
-		(require-not (global-name "com.apple.spotlight.IndexAgent"))
 		(require-not (global-name "com.apple.biome.access.user"))
-		(require-not (global-name "com.apple.duetactivityscheduler"))
-		(require-not (global-name "com.apple.TapToRadarKit.service"))
 		(require-not (global-name "com.apple.linkd.registry"))
+		(require-not (global-name "com.apple.FileProvider"))
+		(require-not (global-name "com.apple.duetactivityscheduler"))
+		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.TapToRadarKit.service"))
+		(require-not (global-name "com.apple.bird"))
+		(require-not (global-name "com.apple.spotlight.IndexAgent"))
+		(require-not (global-name "com.apple.revisiond"))
+		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.FSEvents"))

 		(require-not (syscall-number
 			SYS_exit
 			SYS_read
+			SYS_write
 			SYS_open
 			SYS_close
 			SYS_getfsstat

 			SYS_kdebug_trace
 			SYS_sigreturn
 			SYS_pathconf
+			SYS_mmap
 			SYS_lseek
 			SYS_ftruncate
 			SYS_sysctl
```
