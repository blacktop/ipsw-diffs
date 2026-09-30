## ServicesAccountLinkingService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.cdp.daemon"))
+		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.fairplaydeviceidentityd"))
 		(require-not (global-name "com.apple.adid"))
 		(require-not (system-attribute developer-mode))

 		MSC__kernelrpc_mach_port_type_trap
 		MSC__kernelrpc_mach_port_request_notification_trap
 		MSC_mach_timebase_info_trap
-		MSC_mk_timer_create)
+		MSC_mk_timer_create
+		MSC_mk_timer_destroy)
 )
 
 (deny syscall-mig

 					mach_exception_raise_state_identity
 					mach_port_get_context_from_user))
 				(require-not (kernel-mig-routine mach_vm_range_create))
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
