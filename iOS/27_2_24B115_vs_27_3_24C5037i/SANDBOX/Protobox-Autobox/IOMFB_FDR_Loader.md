## IOMFB_FDR_Loader

> Group: ⬆️ Updated

```diff

 			mach_vm_behavior_set
 			mach_vm_map_external
 			mach_vm_machine_attribute
+			mach_vm_remap_external
 			mach_vm_region
 			_mach_make_memory_entry
 			mach_vm_purgable_control

 
 (deny system-kas-info)
 
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
```
