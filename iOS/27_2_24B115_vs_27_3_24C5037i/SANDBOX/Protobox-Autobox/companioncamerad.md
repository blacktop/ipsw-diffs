## companioncamerad

> Group: ⬆️ Updated

```diff

 
 (deny iokit-open-service)
 (allow iokit-open-service
-	(iokit-registry-entry-class "AppleKeyStore")
+	(require-any
+		(iokit-registry-entry-class "AppleJPEGDriver")
+		(iokit-registry-entry-class "AppleKeyStore")
+	)
 )
 
 (deny iokit-set-properties)

 		SYS_psynch_rw_unlock
 		SYS_psynch_rw_unlock2
 		SYS_psynch_cvclrprepost
+		SYS_iopolicysys
 		SYS_issetugid
 		SYS___pthread_kill
 		SYS___pthread_sigmask

 		io_connect_method
 		io_server_version
 		io_service_get_matching_service_bin
+		io_service_get_matching_services_bin
 		io_registry_entry_get_property_bin_buf
 		mach_port_request_notification
 		mach_port_set_attributes

 		task_set_exc_guard_behavior
 		vm_remap_external
 		vm_reallocate
+		mach_vm_copy
 		mach_vm_map_external
 		mach_vm_remap_external
 		mach_vm_region_recurse

 
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
