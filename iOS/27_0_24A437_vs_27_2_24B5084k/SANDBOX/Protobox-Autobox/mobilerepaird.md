## mobilerepaird

> Group: ⬆️ Updated

```diff

 			(global-name "com.apple.corerepair.diagnostics")
 			(global-name "com.apple.corerepair.intentControl")
 			(global-name "com.apple.corerepair.preflightControl")
+			(global-name "com.apple.mobilerepair.shipmode")
 			(global-name "com.apple.private.corerepair.diagnostics-delegate")
 		))
 		(require-not (global-name "com.apple.lsd.mapdb"))

 		(require-not (global-name "com.apple.nfcd.hwmanager"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.deviceconfigurationd.publisher"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.corefollowup.agent"))
+		(require-not (global-name "com.apple.deviceconfigurationd.consumer"))
 		(require-not (global-name "com.apple.nearbyd.xpc.diagnostics"))
 		(require-not (global-name "com.apple.devicedatareset.DeviceDataResetObservationService.NonLaunching"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.devicedatareset.DeviceDataResetService"))
 		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (xpc-service-name "com.apple.ZhuGeService"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.datamigrator"))

 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))
 	)

 (allow socket-ioctl
 	(ioctl-command
 		CTLIOCGINFO
+		SIOCGCONNINFO
 		SIOCGIFCONSTRAINED
 		SIOCGIFDELEGATE
 		SIOCGIFEXPENSIVE

 		SYS_recvmsg
 		SYS_sendmsg
 		SYS_recvfrom
+		SYS_getsockname
 		SYS_access
 		SYS_crossarch_trap
 		SYS_dup

 		SYS_connectx
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
+		SYS_unlinkat
 		SYS_mkdirat
 		SYS_bsdthread_ctl
 		SYS_guarded_open_dprotected_np
```
