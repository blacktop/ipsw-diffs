## installcoordinationd

> Group: ⬆️ Updated

```diff

 		))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
+		(require-not (global-name "com.apple.manageddeviced.managed-apps"))
 		(require-not (global-name "com.apple.healthd.server"))
 		(require-not (global-name "com.apple.mobile.installd"))
 		(require-not (xpc-service-name "com.apple.MobileInstallationHelperService"))

 		mach_vm_region_recurse
 		mach_vm_region
 		_mach_make_memory_entry
+		mach_vm_page_range_query
 		mach_vm_deferred_reclamation_buffer_flush
 		mach_vm_range_create
 		mach_vm_reallocate
```
