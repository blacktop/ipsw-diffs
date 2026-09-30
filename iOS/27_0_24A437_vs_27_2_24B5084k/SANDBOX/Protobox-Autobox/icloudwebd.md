## icloudwebd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.kvsd"))
 		(require-not (global-name "com.apple.assistant.cdm"))
 		(require-not (global-name "com.apple.bird"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.aa.daemon.xpc"))
 		(require-not (global-name "com.apple.intelligenceplatform.View"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))

 		mach_vm_remap_external
 		mach_vm_region_recurse
 		_mach_make_memory_entry
+		mach_vm_page_range_query
 		mach_vm_range_create
 		mach_vm_reallocate
 		mach_memory_entry_ownership
```
