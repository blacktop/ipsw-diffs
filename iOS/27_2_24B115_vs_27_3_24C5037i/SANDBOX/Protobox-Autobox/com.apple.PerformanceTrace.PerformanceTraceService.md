## com.apple.PerformanceTrace.PerformanceTraceService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (xpc-service-name "com.apple.swiftuitracingsupport.xpc"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))
 	)

 		MSC_mach_timebase_info_trap)
 )
 
-(deny syscall-mig)
-(allow syscall-mig
-	(kernel-mig-routine
-		host_info
-		host_get_io_master
-		host_get_clock_service
-		host_get_special_port
-		kext_request
-		clock_get_time
-		mach_exception_raise
-		mach_exception_raise_state
-		mach_exception_raise_state_identity
-		io_object_get_class
-		io_object_conforms_to
-		io_iterator_next
-		io_registry_entry_from_path
-		io_registry_entry_get_name
-		io_registry_entry_get_child_iterator
-		io_registry_entry_get_parent_iterator
-		io_service_close
-		io_registry_get_root_entry
-		io_registry_entry_create_iterator
-		io_iterator_is_valid
-		io_registry_entry_get_name_in_plane
-		io_registry_entry_get_location_in_plane
-		io_service_open_extended
-		io_connect_map_memory_into_task
-		io_connect_unmap_memory_from_task
-		io_connect_method
-		io_connect_set_notification_port_64
-		io_service_add_interest_notification_64
-		io_registry_entry_get_registry_entry_id
-		io_server_version
-		io_service_get_matching_service_bin
-		io_service_get_matching_services_bin
-		io_registry_entry_get_properties_bin_buf
-		io_registry_entry_get_property_bin_buf
-		mach_port_get_refs
-		mach_port_request_notification
-		mach_port_set_attributes
-		mach_port_get_context_from_user
-		mach_port_set_context
-		mach_port_is_connection_for_service
-		task_threads_from_user
-		task_info_from_user
-		task_suspend
-		task_resume
-		task_get_special_port_from_user
-		task_set_special_port
-		semaphore_create
-		semaphore_destroy
-		task_policy_get
-		task_suspend2
-		task_resume2
-		task_map_corpse_info_64
-		thread_info
-		thread_set_exception_ports
-		vm_copy
-		vm_read_overwrite
-		vm_remap_external
-		vm_reallocate
-		mach_vm_read
-		mach_vm_copy
-		mach_vm_read_overwrite
-		mach_vm_map_external
-		mach_vm_remap_external
-		mach_vm_region_recurse
-		mach_vm_region
-		_mach_make_memory_entry
-		mach_vm_remap_new_external
-		mach_vm_range_create
-		mach_vm_reallocate
-		mach_memory_entry_ownership
-		mach_voucher_attr_command
-		task_restartable_ranges_register
-		task_restartable_ranges_synchronize)
+(deny syscall-mig
+	(require-all
+		(require-not (kernel-mig-routine
+			host_info
+			host_get_io_master
+			host_get_clock_service
+			host_get_special_port
+			kext_request
+			clock_get_time
+			mach_exception_raise
+			mach_exception_raise_state
+			mach_exception_raise_state_identity
+			io_object_get_class
+			io_object_conforms_to
+			io_iterator_next
+			io_registry_entry_from_path
+			io_registry_entry_get_name
+			io_registry_entry_get_child_iterator
+			io_registry_entry_get_parent_iterator
+			io_service_close
+			io_registry_get_root_entry
+			io_registry_entry_create_iterator
+			io_iterator_is_valid
+			io_registry_entry_get_name_in_plane
+			io_registry_entry_get_location_in_plane
+			io_service_open_extended
+			io_connect_map_memory_into_task
+			io_connect_unmap_memory_from_task
+			io_connect_method
+			io_connect_set_notification_port_64
+			io_service_add_interest_notification_64
+			io_registry_entry_get_registry_entry_id
+			io_server_version
+			io_service_get_matching_service_bin
+			io_service_get_matching_services_bin
+			io_registry_entry_get_properties_bin_buf
+			io_registry_entry_get_property_bin_buf
+			mach_port_get_refs
+			mach_port_request_notification
+			mach_port_set_attributes
+			mach_port_get_context_from_user
+			mach_port_set_context
+			mach_port_is_connection_for_service
+			task_threads_from_user
+			task_info_from_user
+			task_suspend
+			task_resume
+			task_get_special_port_from_user
+			task_set_special_port
+			semaphore_create
+			semaphore_destroy
+			task_policy_get
+			task_suspend2
+			task_resume2
+			task_map_corpse_info_64
+			thread_info
+			thread_set_exception_ports
+			vm_copy
+			vm_read_overwrite
+			vm_remap_external
+			vm_reallocate
+			mach_vm_read
+			mach_vm_copy
+			mach_vm_read_overwrite
+			mach_vm_map_external
+			mach_vm_remap_external
+			mach_vm_region_recurse
+			mach_vm_region
+			_mach_make_memory_entry
+			mach_vm_remap_new_external
+			mach_vm_range_create
+			mach_vm_reallocate
+			mach_memory_entry_ownership
+			mach_voucher_attr_command
+			task_restartable_ranges_register
+			task_restartable_ranges_synchronize))
+		(require-any
+			(kernel-mig-routine task_set_exc_guard_behavior)
+			(require-all
+				(require-not (kernel-mig-routine
+					host_info
+					host_get_clock_service
+					mach_exception_raise
+					mach_exception_raise_state
+					mach_exception_raise_state_identity))
+				(require-not (kernel-mig-routine vm_remap_external))
+				(require-not (kernel-mig-routine task_restartable_ranges_register))
+				(require-not (kernel-mig-routine task_restartable_ranges_synchronize))
+				(require-not (kernel-mig-routine mach_vm_reallocate))
+				(require-not (kernel-mig-routine semaphore_create))
+				(require-not (kernel-mig-routine task_info_from_user))
+				(require-not (kernel-mig-routine io_service_open_extended))
+				(require-not (kernel-mig-routine vm_reallocate))
+			)
+		)
+	)
 )
 
 (deny sysctl*

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
 			(require-not (mac-syscall-number 7))
-			(require-not (mac-syscall-number 6))
 			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 6))
 			(require-not (mac-syscall-number 5))
 			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number 2))
```
