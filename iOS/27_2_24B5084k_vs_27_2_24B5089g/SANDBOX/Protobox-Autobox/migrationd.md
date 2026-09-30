## migrationd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.appleneuralengine"))
 		(require-not (global-name "com.apple.identityservicesd.idquery.embedded.auth"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
+		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (global-name "com.apple.iap2d.xpc"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))

 		mach_vm_region_recurse
 		mach_vm_region
 		_mach_make_memory_entry
+		mach_vm_page_range_query
 		mach_vm_range_create
 		mach_vm_reallocate
 		mach_memory_entry_ownership
```
