## uarppersonalizationd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.securityd"))
 		(require-not (require-any
 			(global-name "com.apple.uarp.asset.personalization.complete")
 			(global-name "com.apple.uarppersonalization")
 			(global-name "com.apple.uarppersonalization.btleserver")
 		))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
+		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent"))

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
