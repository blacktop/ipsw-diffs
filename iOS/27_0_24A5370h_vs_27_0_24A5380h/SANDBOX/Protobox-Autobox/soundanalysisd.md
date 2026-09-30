## soundanalysisd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.timesync.expositor"))
+		(require-not (global-name "com.apple.appleneuralengine"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
+		(require-not (global-name "com.apple.tailspind"))
+		(require-not (global-name "com.apple.alwaysonexclaves"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.audio.AudioQueueServer"))
-		(require-not (global-name "com.apple.audio.AudioSession"))
-		(require-not (global-name "com.apple.HearingModeService"))
-		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
-		(require-not (global-name "com.apple.mediaanalysisd.service.public"))
-		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
+		(require-not (global-name "com.apple.iokit.powerdxpc"))
+		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (require-any
 			(global-name "com.apple.audio.isolated.client.service")
 			(global-name "com.apple.shareddspd")
 		))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.iokit.powerdxpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.audioanalyticsd"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
+		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
+		(require-not (global-name "com.apple.audio.AudioSession"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
-		(require-not (global-name "com.apple.symptom_diagnostics"))
+		(require-not (global-name "com.apple.audio.AudioQueueServer"))
+		(require-not (global-name "com.apple.mediaanalysisd.service.public"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.timesync.expositor"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.HearingModeService"))
+		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
-		(require-not (global-name "com.apple.tailspind"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.audioanalyticsd"))
-		(require-not (global-name "com.apple.alwaysonexclaves"))
 		(require-not (xpc-service-name "com.apple.internal.aupbregistrarservice"))
-		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
-		(require-not (global-name "com.apple.appleneuralengine"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
 		(require-not (global-name "com.apple.BTAudioHALPlugin.xpc"))
 		(require-not (system-attribute developer-mode))
 	)

 		SYS_openat_dprotected_np
 		SYS_getattrlist
 		SYS_fsetattrlist
+		SYS_listxattr
 		SYS_fsctl
 		SYS_shm_open
 		SYS_sysctlbyname

 		SYS_open_nocancel
 		SYS_close_nocancel
 		SYS_sendmsg_nocancel
+		SYS_recvfrom_nocancel
 		SYS_msync_nocancel
 		SYS_fcntl_nocancel
+		SYS_select_nocancel
 		SYS_fsync_nocancel
 		SYS_sigsuspend_nocancel
 		SYS_readv_nocancel

 					mach_exception_raise_state
 					mach_exception_raise_state_identity
 					mach_port_get_context_from_user))
+				(require-not (kernel-mig-routine vm_remap_external))
 				(require-not (kernel-mig-routine task_restartable_ranges_register))
 				(require-not (kernel-mig-routine task_restartable_ranges_synchronize))
-				(require-not (kernel-mig-routine semaphore_create))
 				(require-not (kernel-mig-routine mach_vm_reallocate))
+				(require-not (kernel-mig-routine semaphore_create))
 				(require-not (kernel-mig-routine task_info_from_user))
-				(require-not (kernel-mig-routine vm_remap_external))
 				(require-not (kernel-mig-routine io_service_open_extended))
 				(require-not (kernel-mig-routine vm_reallocate))
 			)

 (deny system-fcntl)
 (allow system-fcntl
 	(fcntl-command
+		F_GETFD
 		F_SETFD
 		F_GETFL
 		F_GETPATH
```
