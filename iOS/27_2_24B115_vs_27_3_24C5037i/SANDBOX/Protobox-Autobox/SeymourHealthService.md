## SeymourHealthService

> Group: ⬆️ Updated

```diff

 			SYS_kdebug_trace64
 			SYS_kdebug_trace
 			SYS_sigreturn
+			SYS_pathconf
 			SYS_lseek
 			SYS_sysctl
 			SYS_getumask

 		task_set_exc_guard_behavior
 		vm_remap_external
 		vm_reallocate
+		mach_vm_copy
 		mach_vm_map_external
 		mach_vm_region_recurse
 		_mach_make_memory_entry

 
 (deny system-mac-syscall
 	(require-all
-		(mac-syscall-number 90 96)
+		(mac-syscall-number 96)
 		(require-not (mac-policy-name "AMFI"))
 	)
 )
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
 (deny system-mac-syscall
 	(require-any
-		(require-not (mac-policy-name "Sandbox"))
-		(require-not (mac-syscall-number 2))
+		(require-not (mac-policy-name "AMFI"))
+		(require-not (mac-syscall-number 90))
 	)
 )
 
```
