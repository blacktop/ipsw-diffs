## StocksKitService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		MSC_mk_timer_cancel)
 )
 
-(deny syscall-mig
-	(require-all
-		(require-not (kernel-mig-routine
-			host_info
-			host_get_io_master
-			host_get_clock_service
-			host_request_notification
-			host_get_special_port
-			clock_get_time
-			mach_exception_raise
-			mach_exception_raise_state
-			mach_exception_raise_state_identity
-			io_iterator_next
-			io_registry_entry_from_path
-			io_connect_set_notification_port
-			io_service_open_extended
-			io_connect_method
-			io_connect_async_method
-			io_connect_set_notification_port_64
-			io_registry_entry_get_registry_entry_id
-			io_server_version
-			io_service_get_matching_service_bin
-			io_service_get_matching_services_bin
-			io_registry_entry_get_property_bin_buf
-			mach_port_request_notification
-			mach_port_set_attributes
-			mach_port_get_context_from_user
-			mach_port_is_connection_for_service
-			task_info_from_user
-			task_get_special_port_from_user
-			task_set_special_port
-			semaphore_create
-			semaphore_destroy
-			task_set_exc_guard_behavior
-			task_create_identity_token
-			thread_suspend
-			thread_resume
-			thread_info
-			thread_policy
-			vm_copy
-			vm_remap_external
-			mach_make_memory_entry_64
-			vm_reallocate
-			mach_vm_copy
-			mach_vm_map_external
-			mach_vm_remap_external
-			mach_vm_region
-			_mach_make_memory_entry
-			mach_vm_range_create
-			mach_vm_reallocate
-			mach_memory_entry_ownership
-			mach_voucher_attr_command
-			task_restartable_ranges_register
-			task_restartable_ranges_synchronize))
-		(require-any
-			(kernel-mig-routine mach_vm_region_recurse)
-			(require-all
-				(require-not (kernel-mig-routine
-					host_info
-					host_get_clock_service
-					mach_exception_raise
-					mach_exception_raise_state
-					mach_exception_raise_state_identity
-					mach_port_get_context_from_user))
-				(require-not (kernel-mig-routine mach_vm_range_create))
-				(require-not (kernel-mig-routine vm_remap_external))
-				(require-not (kernel-mig-routine task_restartable_ranges_register))
-				(require-not (kernel-mig-routine task_restartable_ranges_synchronize))
-				(require-not (kernel-mig-routine mach_vm_reallocate))
-				(require-not (kernel-mig-routine semaphore_create))
-				(require-not (kernel-mig-routine task_info_from_user))
-				(require-not (kernel-mig-routine io_service_open_extended))
-				(require-not (kernel-mig-routine vm_reallocate))
-			)
-		)
-	)
+(deny syscall-mig)
+(allow syscall-mig
+	(kernel-mig-routine
+		host_info
+		host_get_io_master
+		host_get_clock_service
+		host_request_notification
+		host_get_special_port
+		clock_get_time
+		mach_exception_raise
+		mach_exception_raise_state
+		mach_exception_raise_state_identity
+		io_iterator_next
+		io_registry_entry_from_path
+		io_connect_set_notification_port
+		io_service_open_extended
+		io_connect_method
+		io_connect_async_method
+		io_connect_set_notification_port_64
+		io_registry_entry_get_registry_entry_id
+		io_server_version
+		io_service_get_matching_service_bin
+		io_service_get_matching_services_bin
+		io_registry_entry_get_property_bin_buf
+		mach_port_request_notification
+		mach_port_set_attributes
+		mach_port_get_context_from_user
+		mach_port_is_connection_for_service
+		task_info_from_user
+		task_get_special_port_from_user
+		task_set_special_port
+		semaphore_create
+		semaphore_destroy
+		task_set_exc_guard_behavior
+		task_create_identity_token
+		thread_suspend
+		thread_resume
+		thread_info
+		thread_policy
+		vm_copy
+		vm_remap_external
+		mach_make_memory_entry_64
+		vm_reallocate
+		mach_vm_copy
+		mach_vm_map_external
+		mach_vm_remap_external
+		mach_vm_region_recurse
+		mach_vm_region
+		_mach_make_memory_entry
+		mach_vm_range_create
+		mach_vm_reallocate
+		mach_memory_entry_ownership
+		mach_voucher_attr_command
+		task_restartable_ranges_register
+		task_restartable_ranges_synchronize)
 )
 
 (deny sysctl*

 
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
