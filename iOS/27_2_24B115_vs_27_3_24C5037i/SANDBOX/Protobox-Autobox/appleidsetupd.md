## appleidsetupd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.xpc.amsengagementd"))
 		(require-not (global-name "com.apple.apsd"))
 		(require-not (global-name "com.apple.backboard.hid-services.xpc"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))

 		MSC_semaphore_signal_trap
 		MSC_semaphore_wait_trap
 		MSC_semaphore_timedwait_trap
+		MSC__kernelrpc_mach_port_get_attributes_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_task_name_for_pid

 		io_iterator_next
 		io_registry_entry_from_path
 		io_registry_entry_get_parent_iterator
+		io_service_close
 		io_registry_entry_get_path
 		io_service_open_extended
 		io_connect_method
+		io_service_add_interest_notification_64
 		io_registry_entry_get_registry_entry_id
 		io_server_version
 		io_service_get_matching_service_bin
 		io_service_get_matching_services_bin
 		io_registry_entry_get_property_bin_buf
 		mach_port_deallocate
+		mach_port_get_refs
 		mach_port_request_notification
 		mach_port_set_attributes
 		mach_port_allocate_qos

 
 (deny system-kas-info)
 
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
