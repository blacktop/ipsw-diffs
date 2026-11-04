## sucontrollerd

> Group: ⬆️ Updated

```diff

 			_mach_make_memory_entry
 			mach_vm_range_create
 			mach_vm_reallocate
+			mach_voucher_attr_command
 			UNDNotificationCreated_rpc
 			task_restartable_ranges_register
 			task_restartable_ranges_synchronize))

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
 (deny system-mac-syscall
 	(require-all
 		(mac-syscall-number 1)
```
