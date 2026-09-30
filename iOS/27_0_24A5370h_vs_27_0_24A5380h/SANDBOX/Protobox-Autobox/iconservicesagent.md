## iconservicesagent

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
-		(require-not (global-name "com.apple.lsd.icons"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.posterboardservices.services"))
-		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.fontservicesd"))
-		(require-not (global-name "com.apple.iconservices"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.coremedia.admin"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.lsd.icons"))
+		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.gputools.service"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.iconservices"))
+		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
+		(require-not (global-name "com.apple.coremedia.admin"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.fontservicesd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.posterboardservices.services"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.gputools.service"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.FileProvider"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))

 		SYS_crossarch_trap
 		SYS_getppid
 		SYS_dup
+		SYS_pipe
 		SYS_getegid
 		SYS_sigaction
 		SYS_getgid

 		F_GETFD
 		F_SETFD
 		F_GETFL
+		F_SETLKW
 		F_RDADVISE
 		F_NOCACHE
 		F_GETPATH
 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS
+		F_BARRIERFSYNC
 		F_ADDFILESIGS_RETURN
 		F_CHECK_LV
 		F_GETSIGSINFO)
```
