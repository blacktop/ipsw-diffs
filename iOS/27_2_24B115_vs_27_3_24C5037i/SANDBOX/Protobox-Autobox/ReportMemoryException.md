## ReportMemoryException

> Group: ⬆️ Updated

```diff

 		mach_vm_page_range_query
 		mach_vm_remap_new_external
 		mach_vm_range_create
+		mach_vm_deferred_reclamation_buffer_query
 		mach_vm_reallocate
 		mach_memory_entry_ownership
 		mach_voucher_attr_command

 
 (deny system-kas-info)
 
-(with-filter (mac-policy-name "Sandbox")
-	(deny system-mac-syscall
-		(require-all
-			(require-not (mac-syscall-number 5 6 67))
-			(require-not (mac-syscall-number 4))
-			(require-not (mac-syscall-number 12))
-			(require-not (mac-syscall-number 2))
-		)
-	)
-)
-(deny system-mac-syscall
-	(require-any
-		(require-not (mac-policy-name "AMFI"))
-		(require-not (mac-syscall-number 90))
-	)
-)
+(deny system-mac-syscall)
 
 (deny system-memorystatus-control)
 (allow system-memorystatus-control
```
