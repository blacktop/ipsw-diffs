## ospredictiond

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.batteryintelligenced.tallpieestimator"))
+		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.biome.PublicStreamAccessService"))
+		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.backlightd"))
 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))

 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.OSIntelligence.battery"))
+		(require-not (global-name "com.apple.SystemConfiguration.helper"))
 		(require-not (global-name "com.apple.sleepd.sleepserver"))
 		(require-not (global-name "com.apple.donotdisturb.service"))
+		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.batteryintelligenced.batteryanalysis"))
 		(require-not (global-name "com.apple.coreduetd.context"))
 		(require-not (global-name "com.apple.diagd"))

 		SYS___sigwait_nocancel
 		SYS___semwait_signal_nocancel
 		SYS_fsgetpath
+		SYS_fileport_makeport
 		SYS_fileport_makefd
 		SYS_memorystatus_control
 		SYS_guarded_open_np

 		SYS_getattrlistbulk
 		SYS_clonefileat
 		SYS_openat
+		SYS_openat_nocancel
 		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat

 		SYS_getentropy
 		SYS_ulock_wait
 		SYS_ulock_wake
+		SYS_fclonefileat
 		SYS_terminate_with_payload
 		SYS_abort_with_payload
 		SYS_ntp_gettime

 		MSC__kernelrpc_mach_port_mod_refs_trap
 		MSC__kernelrpc_mach_port_insert_right_trap
 		MSC__kernelrpc_mach_port_insert_member_trap
+		MSC__kernelrpc_mach_port_extract_member_trap
 		MSC__kernelrpc_mach_port_construct_trap
 		MSC__kernelrpc_mach_port_destruct_trap
 		MSC_mach_reply_port
```
