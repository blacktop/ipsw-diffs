## nexusd

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.coordination.capability"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.wifip2pd"))
-		(require-not (global-name "com.apple.coordination.capability"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.SiriVOXService.client"))
 		(require-not (system-attribute developer-mode))
 	)

 		SYS___sigwait_nocancel
 		SYS___semwait_signal_nocancel
 		SYS_fsgetpath
+		SYS_fileport_makefd
 		SYS_memorystatus_control
 		SYS_guarded_close_np
 		SYS_change_fdguard_np

 		(require-not (kernel-mig-routine
 			host_info
 			host_get_clock_service
+			host_request_notification
 			host_get_special_port
 			clock_get_time
 			mach_exception_raise

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
