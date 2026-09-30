## pcapd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.pcapd-local"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.aggregated"))
 		(require-not (system-attribute developer-mode))
 	)

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
