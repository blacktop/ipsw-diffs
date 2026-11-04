## sharereportingd

> Group: ⬆️ Updated

```diff

 			task_get_special_port_from_user
 			task_set_special_port
 			semaphore_create
+			task_set_exc_guard_behavior
 			vm_remap_external
 			vm_reallocate
 			mach_vm_map_external

 			task_restartable_ranges_synchronize))
 		(require-any
 			(kernel-mig-routine mach_vm_region_recurse)
-			(kernel-mig-routine task_set_exc_guard_behavior)
 			(require-all
 				(require-not (kernel-mig-routine
 					host_info

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
 (deny system-mac-syscall
 	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
+(with-filter (mac-policy-name "vnguard")
+	(deny system-mac-syscall
+		(require-not (mac-syscall-number 1))
 	)
 )
 (deny system-mac-syscall
```
