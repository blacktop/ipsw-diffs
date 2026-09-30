## IDSRemoteURLConnectionAgent

> Group: ⬆️ Updated

```diff

 	(require-all
 		(require-not (kernel-mig-routine
 			host_info
+			host_get_io_master
 			host_get_clock_service
 			host_get_special_port
 			mach_exception_raise
 			mach_exception_raise_state
 			mach_exception_raise_state_identity
+			io_registry_entry_from_path
 			io_service_open_extended
+			io_service_get_matching_service
+			io_server_version
 			mach_port_request_notification
 			mach_port_set_attributes
 			mach_port_get_context_from_user
```
