## momentsd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.cloudkit.partlycloudd"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.intelligenceplatform.InferenceSupport"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))

 		mach_vm_region_recurse
 		mach_vm_region
 		_mach_make_memory_entry
+		mach_vm_page_range_query
 		mach_vm_deferred_reclamation_buffer_flush
 		mach_vm_range_create
 		mach_vm_reallocate
```
