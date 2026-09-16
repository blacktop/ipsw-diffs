## SecuritySubscriber

> Group: ⬆️ Updated

```diff

 		SYS_stat
 		SYS_fstat
 		SYS_lstat
+		SYS_pathconf
 		SYS_getrlimit
 		SYS_setrlimit
 		SYS_mmap

 		vm_remap_external
 		mach_make_memory_entry_64
 		vm_reallocate
+		mach_vm_copy
 		mach_vm_behavior_set
 		mach_vm_map_external
 		mach_vm_region_recurse

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 90 96)
-		(require-not (mac-policy-name "AMFI"))
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 2))
+		)
 	)
 )
 (deny system-mac-syscall
 	(require-any
-		(require-not (mac-policy-name "Sandbox"))
-		(require-not (mac-syscall-number 2))
+		(require-not (mac-policy-name "AMFI"))
+		(require-not (mac-syscall-number 90))
 	)
 )
 
```
