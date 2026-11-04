## tailspind

> Group: ⬆️ Updated

```diff

 		io_service_get_matching_services_bin
 		io_registry_entry_get_properties_bin_buf
 		io_registry_entry_get_property_bin_buf
+		mach_port_deallocate
 		mach_port_get_refs
 		mach_port_request_notification
 		mach_port_set_attributes

 		task_set_exc_guard_behavior
 		mach_task_is_self
 		task_create_identity_token
+		thread_terminate
 		thread_get_state_to_user
 		thread_suspend
 		thread_resume

 		KAS_INFO_TXM_TEXT_SLIDE_SELECTOR)
 )
 
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
