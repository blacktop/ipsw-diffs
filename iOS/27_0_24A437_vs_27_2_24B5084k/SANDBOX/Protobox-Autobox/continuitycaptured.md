## continuitycaptured

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.asset.xpc"))
+		(require-not (global-name "com.apple.xpc.amsengagementd"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.coremedia.admin"))
+		(require-not (global-name "com.apple.CompanionLink"))
 		(require-not (global-name "com.apple.rtcreportingd"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))

 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
 		(require-not (global-name "com.apple.wifi.manager"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
+		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.mediasafetynet.exceptions"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.commcenter.xpc"))

 		(require-not (global-name "com.apple.itunescloudd.xpc"))
 		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
+		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
+		(require-not (global-name "com.apple.SystemConfiguration.DNSConfiguration"))
 		(require-not (global-name "com.apple.systemstatus.activityattribution"))
 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.wifip2pd"))
 		(require-not (global-name "com.apple.timesync.expositor"))
+		(require-not (global-name "com.apple.xpc.amstoold"))
 		(require-not (global-name "com.apple.mediasafetynet.exceptions.cam"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))

 		(require-not (xpc-service-name "com.apple.continuityarkitd"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
-		(require-not (global-name "com.apple.CompanionLink"))
 		(require-not (global-name "com.apple.CARenderServer"))
+		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 (deny socket-ioctl)
 (allow socket-ioctl
 	(ioctl-command
+		CTLIOCGINFO
 		SIOCGCONNINFO
 		SIOCGIFAFLAG_IN6
 		SIOCGIFAGENTDATA

 		SYS_flock
 		SYS_sendto
 		SYS_shutdown
+		SYS_socketpair
 		SYS_mkdir
 		SYS_rmdir
 		SYS_utimes

 		SYS_fgetattrlist
 		SYS_fsetattrlist
 		SYS_getxattr
+		SYS_setxattr
 		SYS_fsetxattr
 		SYS_listxattr
 		SYS_fsctl

 		SYS_fileport_makeport
 		SYS_fileport_makefd
 		SYS_memorystatus_control
+		SYS_guarded_open_np
 		SYS_guarded_close_np
 		SYS_guarded_kqueue_np
 		SYS_change_fdguard_np

 		SYS_connectx
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
+		SYS_unlinkat
 		SYS_mkdirat
 		SYS_bsdthread_ctl
 		SYS_guarded_open_dprotected_np

 		F_SETLKW
 		F_GETPATH
 		F_GETPROTECTIONCLASS
+		F_SETPROTECTIONCLASS
 		F_SETNOSIGPIPE
+		F_OFD_SETLK
+		F_OFD_GETLK
+		F_SETCONFINED
+		F_GETCONFINED
 		F_ADDFILESIGS_RETURN
 		F_CHECK_LV)
 )

 
 (deny system-kas-info)
 
-(with-filter (mac-policy-name "Sandbox")
-	(deny system-mac-syscall
-		(require-all
-			(require-not (mac-syscall-number 7))
-			(require-not (mac-syscall-number 6))
-			(require-not (mac-syscall-number 67))
-			(require-not (mac-syscall-number 5))
-			(require-not (mac-syscall-number 4))
-			(require-not (mac-syscall-number 2))
-		)
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 1)
+		(require-not (mac-policy-name "vnguard"))
 	)
 )
 (deny system-mac-syscall
```
