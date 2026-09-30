## jetpackassetd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.xpc.amsengagementd"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.symptom_analytics"))
 		(require-not (global-name "com.apple.amsservicesanalytics.xpc"))

 		semaphore_destroy
 		task_set_exc_guard_behavior
 		thread_terminate
+		thread_get_state_to_user
 		thread_suspend
 		thread_resume
 		thread_info

 		mach_make_memory_entry_64
 		vm_reallocate
 		mach_vm_copy
+		mach_vm_read_overwrite
 		mach_vm_behavior_set
 		mach_vm_map_external
 		mach_vm_remap_external
```
