## AUHostingServiceXPC_arrow

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.debug.telemetry"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (xpc-service-name "com.apple.coreaudio.RemoteProcessingBlockRegistrar"))
 		(require-not (xpc-service-name "com.apple.internal.aupbregistrarservice"))
+		(require-not (xpc-service-name "com.apple.coreaudio.RemoteProcessingBlockRegistrar"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (system-attribute developer-mode))
 	)

 		SYS_lseek
 		SYS_ftruncate
 		SYS_sysctl
+		SYS_mlock
+		SYS_munlock
 		SYS_getumask
 		SYS_open_dprotected_np
 		SYS_getattrlist

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
