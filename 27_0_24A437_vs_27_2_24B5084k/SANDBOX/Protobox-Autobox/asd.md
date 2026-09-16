## asd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.identityservicesd.pds"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.commcenter.xpc"))

 		mach_vm_region_recurse
 		mach_vm_region
 		_mach_make_memory_entry
+		mach_vm_page_range_query
 		mach_vm_range_create
 		mach_vm_reallocate
 		mach_memory_entry_ownership

 		F_SETFD
 		F_GETFL
 		F_SETFL
+		F_SETLKW
 		F_RDADVISE
 		F_NOCACHE
 		F_GETPATH
```
