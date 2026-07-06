## visioncompaniond

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.fairplayd.versioned"))
-		(require-not (global-name "com.apple.xpc.amstoold"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.fairplayd.xpc"))
-		(require-not (global-name "com.apple.accountsd.accountmanager"))
-		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.apsd"))
-		(require-not (global-name "com.apple.debug.telemetry"))
-		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.trustd"))
-		(require-not (global-name "com.apple.xpc.amsaccountsd"))
-		(require-not (global-name "com.apple.ak.auth.xpc"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.storekitd"))
-		(require-not (global-name "com.apple.backboard.hid.services"))
-		(require-not (global-name "com.apple.xpc.amsengagementd"))
-		(require-not (global-name "com.apple.cloudd"))
+		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
+		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.ak.auth.xpc"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.xpc.amsengagementd"))
+		(require-not (global-name "com.apple.apsd"))
+		(require-not (global-name "com.apple.tccd"))
+		(require-not (global-name "com.apple.accountsd.accountmanager"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.cloudd"))
+		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.erm.logging"))
-		(require-not (global-name "com.apple.duetactivityscheduler"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.fairplayd.xpc"))
+		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
-		(require-not (global-name "com.apple.tccd"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
+		(require-not (global-name "com.apple.xpc.amstoold"))
+		(require-not (global-name "com.apple.debug.telemetry"))
+		(require-not (global-name "com.apple.backboard.hid.services"))
+		(require-not (global-name "com.apple.xpc.amsaccountsd"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))

 		SYS_sigsuspend
 		SYS_readv
 		SYS_writev
+		SYS_rename
 		SYS_flock
 		SYS_sendto
 		SYS_shutdown

 		SYS_getattrlist
 		SYS_fgetattrlist
 		SYS_setxattr
+		SYS_listxattr
 		SYS_fsctl
 		SYS_shm_open
 		SYS_sysctlbyname
```
