## IDSRemoteURLConnectionAgent

> Group: ⬆️ Updated

```diff

 			mach_exception_raise_state
 			mach_exception_raise_state_identity
 			io_registry_entry_from_path
+			io_service_close
 			io_service_open_extended
+			io_connect_method
 			io_service_get_matching_service
 			io_server_version
 			mach_port_request_notification

 
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
