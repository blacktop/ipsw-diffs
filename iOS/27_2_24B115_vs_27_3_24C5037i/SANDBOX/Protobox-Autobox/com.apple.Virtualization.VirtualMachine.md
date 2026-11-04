## com.apple.Virtualization.VirtualMachine

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.iap2d.distributednotification.server"))
 		(require-not (global-name "com.apple.remoted.virtualization"))
 		(require-not (global-name "com.apple.iohideventsystem"))

 			mach_vm_copy
 			mach_vm_map_external
 			mach_vm_remap_external
+			mach_vm_region_recurse
 			mach_vm_region
 			_mach_make_memory_entry
 			mach_vm_remap_new_external

 			task_restartable_ranges_register
 			task_restartable_ranges_synchronize))
 		(require-any
-			(kernel-mig-routine mach_vm_region_recurse)
 			(kernel-mig-routine task_set_exc_guard_behavior)
 			(require-all
 				(require-not (kernel-mig-routine
```
