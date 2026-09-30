## Ciconia

> Group: ⬆️ Updated

```diff

 
 (deny process-exec*
 	(require-all
-		(require-not (literal "/usr/bin/awk"))
 		(require-not (literal "/usr/bin/fileproviderctl"))
 		(require-not (literal "/usr/bin/env"))
+		(require-not (literal "/usr/bin/awk"))
 	)
 )
 (deny process-exec*

 					mach_exception_raise_state
 					mach_exception_raise_state_identity))
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
