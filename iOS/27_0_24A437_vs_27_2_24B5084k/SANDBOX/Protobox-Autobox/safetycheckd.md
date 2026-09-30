## safetycheckd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.findmy.findmylocate.locationservice"))
 		(require-not (global-name "com.apple.spotlight.IndexAgent"))
 		(require-not (global-name "com.apple.AuthenticationServices.AutoFill"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (global-name "com.apple.aa.daemon.xpc"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))

 		mach_vm_remap_external
 		mach_vm_region_recurse
 		_mach_make_memory_entry
+		mach_vm_page_range_query
 		mach_vm_range_create
 		mach_vm_reallocate
 		mach_memory_entry_ownership
```
