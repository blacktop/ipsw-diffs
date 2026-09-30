## AirPlaySenderService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.timesync.expositor"))
-		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
-		(require-not (global-name "com.apple.wifip2pd"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))
-		(require-not (global-name "com.apple.mediaremoted.xpc"))
-		(require-not (global-name "com.apple.gpumemd.source"))
-		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
-		(require-not (global-name "com.apple.coremedia.admin"))
+		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.iokit.powerdxpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.coremedia.admin"))
 		(require-not (global-name "com.apple.mediaanalysisd.realtime"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
+		(require-not (global-name "com.apple.mediaremoted.xpc"))
+		(require-not (global-name "com.apple.gpumemd.source"))
+		(require-not (global-name "com.apple.wifip2pd"))
+		(require-not (global-name "com.apple.timesync.expositor"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (xpc-service-name "com.apple.MFAAuthentication.MFAANetwork"))
+		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.CARenderServer"))

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
```
