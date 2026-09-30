## PerfPowerServices

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.lsd.xpc"))
+		(require-not (global-name "com.apple.coresymbolicationd"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.backboard.hid-services.xpc"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))

 		(require-not (xpc-service-name "com.apple.PPSFeatureFlagReader"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.nfcd.hwmanager"))
 		(require-not (global-name "com.apple.runningboard"))

 		(require-not (global-name "com.apple.AttentionAwareness"))
 		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
+		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.SystemConfiguration.helper"))
 		(require-not (global-name "com.apple.ExposureNotification"))
 		(require-not (global-name "com.apple.centaurid.xpc"))
 		(require-not (global-name "com.apple.trial.status"))
+		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.ind.cloudfeatures"))
 		(require-not (global-name "com.apple.corereporting.report-services"))

 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.xpc.amsaccountsd"))
 		(require-not (global-name "com.apple.research.adtcd"))
+		(require-not (global-name "com.apple.nesessionmanager"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
+		(require-not (global-name "com.apple.nesessionmanager.flow-divert-token"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.PPSRelay")
 			(xpc-service-name "com.apple.PerfPowerServicesSignpostService")

 		SYS_flock
 		SYS_sendto
 		SYS_shutdown
+		SYS_socketpair
 		SYS_mkdir
 		SYS_rmdir
+		SYS_utimes
+		SYS_gethostuuid
 		SYS_pread
 		SYS_pwrite
 		SYS_statfs

 		SYS___sigwait_nocancel
 		SYS___semwait_signal_nocancel
 		SYS_fsgetpath
+		SYS_audit_session_self
 		SYS_fileport_makeport
 		SYS_fileport_makefd
 		SYS_memorystatus_control

 		SYS_getattrlistbulk
 		SYS_clonefileat
 		SYS_openat
+		SYS_openat_nocancel
 		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat

 		host_request_notification
 		host_statistics64_from_user
 		host_get_special_port
+		kext_request
 		clock_get_time
 		mach_exception_raise
 		mach_exception_raise_state

 		F_GETPATH
 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS
+		F_LOG2PHYS_EXT
 		F_DUPFD_CLOEXEC
 		F_SINGLE_WRITER
 		F_BARRIERFSYNC

 (allow system-necp-client-action
 	(necp-client-action
 		NECP_CLIENT_ACTION_ADD
+		NECP_CLIENT_ACTION_AGENT
 		NECP_CLIENT_ACTION_COPY_AGENT
 		NECP_CLIENT_ACTION_COPY_INTERFACE
 		NECP_CLIENT_ACTION_COPY_RESULT
-		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT)
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
+		NECP_CLIENT_ACTION_REMOVE)
 )
```
