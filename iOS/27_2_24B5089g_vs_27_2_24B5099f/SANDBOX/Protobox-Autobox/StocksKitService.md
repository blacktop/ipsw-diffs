## StocksKitService

> Group: ⬆️ Updated

```diff

 			task_set_special_port
 			semaphore_create
 			semaphore_destroy
+			task_set_exc_guard_behavior
 			task_create_identity_token
 			thread_suspend
 			thread_resume

 			task_restartable_ranges_synchronize))
 		(require-any
 			(kernel-mig-routine mach_vm_region_recurse)
-			(kernel-mig-routine task_set_exc_guard_behavior)
 			(require-all
 				(require-not (kernel-mig-routine
 					host_info
```
