## webprivacyd

> Group: ⬆️ Updated

```diff

 		SYS___sigwait_nocancel
 		SYS___semwait_signal_nocancel
 		SYS_fsgetpath
+		SYS_fileport_makefd
 		SYS_memorystatus_control
 		SYS_guarded_open_np
 		SYS_guarded_close_np

 		mach_exception_raise
 		mach_exception_raise_state
 		mach_exception_raise_state_identity
+		io_iterator_next
+		io_registry_create_iterator
+		io_registry_entry_get_name
 		io_service_open_extended
+		io_service_get_matching_service
+		io_server_version
+		io_service_get_matching_service_bin
+		io_registry_entry_get_properties_bin_buf
+		io_registry_entry_get_property_bin_buf
 		mach_port_request_notification
 		mach_port_set_attributes
 		mach_port_get_context_from_user

 
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
