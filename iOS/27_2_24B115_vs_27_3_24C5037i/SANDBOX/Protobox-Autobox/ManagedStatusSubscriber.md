## ManagedStatusSubscriber

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.enhancedloggingd.xpc"))
+		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.managedconfiguration.mdmuserdservice"))
+		(require-not (global-name "com.apple.manageddeviced"))
+		(require-not (global-name "com.apple.cache_delete.public"))
 		(require-not (global-name "com.apple.managedconfiguration.mdmdservice"))
 		(require-not (global-name "com.apple.mobilerepaird"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))

 	(machtrap-number
 		MSC__kernelrpc_mach_vm_allocate_trap
 		MSC__kernelrpc_mach_vm_deallocate_trap
+		MSC_task_dyld_process_info_notify_get
 		MSC__kernelrpc_mach_vm_protect_trap
 		MSC__kernelrpc_mach_vm_map_trap
 		MSC__kernelrpc_mach_port_allocate_trap

 		io_connect_method
 		io_server_version
 		io_service_get_matching_service_bin
+		io_service_get_matching_services_bin
 		io_registry_entry_get_property_bin_buf
 		mach_port_request_notification
 		mach_port_set_attributes

 
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
