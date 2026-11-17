## diagnosticscheckupd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (global-name "com.apple.HomePodDisplayService.xpc"))
 		(require-not (global-name "com.apple.bluetooth.xpc"))
+		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.corerepair"))
 		(require-not (global-name "com.apple.homed.xpc"))
 		(require-not (global-name "com.apple.backboard.hid.services"))

 			_mach_make_memory_entry
 			mach_vm_range_create
 			mach_vm_reallocate
+			mach_memory_entry_ownership
 			mach_voucher_attr_command
 			task_restartable_ranges_register
 			task_restartable_ranges_synchronize))
```
