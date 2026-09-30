## finhealth_client

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.passd.payment"))
-		(require-not (global-name "com.apple.passd.library"))
-		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (require-any
 			(global-name "com.apple.finhealthd")
 			(global-name "com.apple.finhealthd.service")
 		))
+		(require-not (global-name "com.apple.passd.payment"))
+		(require-not (global-name "com.apple.passd.library"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (xpc-service-name "com.apple.FinHealth.FinHealthXPCServices"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.finhealthd")
 			(xpc-service-name "com.apple.finhealthd.aggregations")
 			(xpc-service-name "com.apple.finhealthd.service")
 		))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (xpc-service-name "com.apple.FinHealth.FinHealthXPCServices"))
 		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (system-attribute developer-mode))
 	)

 					mach_exception_raise
 					mach_exception_raise_state
 					mach_exception_raise_state_identity))
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
