## cksharingmanagementd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.cloudkit.audience-provider.com.apple.family"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
+		(require-not (global-name "com.apple.cloudkit.audience-provider.com.apple.family"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (system-attribute developer-mode))
 	)

 			SYS_lseek
 			SYS_sysctl
 			SYS_getumask
+			SYS_fgetattrlist
 			SYS_fsctl
 			SYS_sysctlbyname
 			SYS_gettid

 	(machtrap-number
 		MSC__kernelrpc_mach_vm_allocate_trap
 		MSC__kernelrpc_mach_vm_deallocate_trap
+		MSC_task_dyld_process_info_notify_get
 		MSC__kernelrpc_mach_vm_protect_trap
 		MSC__kernelrpc_mach_vm_map_trap
 		MSC__kernelrpc_mach_port_allocate_trap

 		mach_exception_raise_state
 		mach_exception_raise_state_identity
 		io_registry_entry_from_path
+		io_service_close
 		io_service_open_extended
+		io_connect_method
 		io_service_get_matching_service
 		io_server_version
 		mach_port_request_notification
```
