## avconferenced

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.spotlight.IndexAgent"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))
 		(require-not (global-name "com.apple.commcenter.xpc"))
 		(require-not (global-name "com.apple.symptom_analytics"))

 		task_set_exc_guard_behavior
 		task_create_identity_token
 		thread_terminate
+		thread_get_state_to_user
 		thread_suspend
 		thread_resume
 		thread_info

 		mach_make_memory_entry_64
 		vm_reallocate
 		mach_vm_copy
+		mach_vm_read_overwrite
 		mach_vm_map_external
 		mach_vm_remap_external
 		mach_vm_region_recurse
```
