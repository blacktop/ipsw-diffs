## sirireaderd

> Group: ⬆️ Updated

```diff

 		MSC_iokit_user_client_trap)
 )
 
-(deny syscall-mig
-	(require-all
-		(require-not (kernel-mig-routine
-			host_info
-			host_get_io_master
-			host_get_clock_service
-			host_get_special_port
-			mach_exception_raise
-			mach_exception_raise_state
-			mach_exception_raise_state_identity
-			io_iterator_next
-			io_registry_entry_from_path
-			io_service_close
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
-			task_create_identity_token
-			thread_policy_set
-			vm_remap_external
-			vm_reallocate
-			mach_vm_copy
-			mach_vm_map_external
-			mach_vm_remap_external
-			_mach_make_memory_entry
-			mach_vm_range_create
-			mach_vm_reallocate
-			mach_memory_entry_ownership
-			mach_voucher_attr_command
-			task_restartable_ranges_register
-			task_restartable_ranges_synchronize))
-		(require-any
-			(kernel-mig-routine mach_vm_region_recurse)
-			(kernel-mig-routine task_set_exc_guard_behavior)
-			(require-all
-				(require-not (kernel-mig-routine
-					host_info
-					host_get_clock_service
-					mach_exception_raise
-					mach_exception_raise_state
-					mach_exception_raise_state_identity))
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
+		host_get_special_port
+		mach_exception_raise
+		mach_exception_raise_state
+		mach_exception_raise_state_identity
+		io_iterator_next
+		io_registry_entry_from_path
+		io_service_close
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
+		thread_policy_set
+		vm_remap_external
+		vm_reallocate
+		mach_vm_copy
+		mach_vm_map_external
+		mach_vm_remap_external
+		mach_vm_region_recurse
+		_mach_make_memory_entry
+		mach_vm_range_create
+		mach_vm_reallocate
+		mach_memory_entry_ownership
+		mach_voucher_attr_command
+		task_restartable_ranges_register
+		task_restartable_ranges_synchronize)
 )
 
 (deny sysctl*
```
