## modelmanagerd

> Group: ⬆️ Updated

```diff

 		io_service_get_matching_services_bin
 		io_service_add_notification_bin_64
 		io_registry_entry_get_property_bin_buf
+		mach_port_deallocate
 		mach_port_get_refs
 		mach_port_mod_refs
 		mach_port_request_notification

 		task_set_exc_guard_behavior
 		task_create_identity_token
 		thread_terminate
+		thread_suspend
 		thread_info
 		thread_policy
 		thread_policy_set

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 5))
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
