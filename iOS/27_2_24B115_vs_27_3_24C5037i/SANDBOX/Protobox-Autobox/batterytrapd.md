## batterytrapd

> Group: ⬆️ Updated

```diff

 		vm_reallocate
 		mach_vm_behavior_set
 		mach_vm_map_external
+		mach_vm_remap_external
 		mach_vm_region_recurse
 		mach_vm_region
 		_mach_make_memory_entry

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 90 96)
-		(require-not (mac-policy-name "AMFI"))
+(with-filter (mac-policy-name "AMFI")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 96))
+			(require-not (mac-syscall-number 90))
+		)
 	)
 )
 (deny system-mac-syscall
```
