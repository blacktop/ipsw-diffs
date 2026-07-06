## auearlyboot

> Group: ⬆️ Updated

```diff

 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
 		SYS_guarded_writev_np
+		SYS_persona
 		SYS_getentropy
 		SYS_ulock_wait
 		SYS_ulock_wake

 		MSC_mach_timebase_info_trap)
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
-			io_iterator_reset
-			io_registry_create_iterator
-			io_registry_entry_from_path
-			io_service_close
-			io_registry_entry_in_plane
-			io_service_open_extended
-			io_connect_method
-			io_registry_entry_get_registry_entry_id
-			io_server_version
-			io_service_get_matching_service_bin
-			io_service_get_matching_services_bin
-			io_service_add_notification_bin_64
-			io_registry_entry_get_properties_bin_buf
-			io_registry_entry_get_property_bin_buf
-			mach_port_get_context_from_user
-			task_info_from_user
-			task_get_special_port_from_user
-			task_set_special_port
-			semaphore_create
-			task_set_exc_guard_behavior
-			vm_remap_external
-			vm_reallocate
-			mach_vm_behavior_set
-			mach_vm_map_external
-			_mach_make_memory_entry
-			mach_vm_deferred_reclamation_buffer_flush
-			mach_vm_range_create
-			mach_vm_reallocate
-			UNDNotificationCreated_rpc
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
-				(require-not (kernel-mig-routine task_restartable_ranges_register))
-				(require-not (kernel-mig-routine task_restartable_ranges_synchronize))
-				(require-not (kernel-mig-routine semaphore_create))
-				(require-not (kernel-mig-routine mach_vm_reallocate))
-				(require-not (kernel-mig-routine task_info_from_user))
-				(require-not (kernel-mig-routine vm_remap_external))
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
+		io_iterator_reset
+		io_registry_create_iterator
+		io_registry_entry_from_path
+		io_service_close
+		io_registry_entry_in_plane
+		io_service_open_extended
+		io_connect_method
+		io_registry_entry_get_registry_entry_id
+		io_server_version
+		io_service_get_matching_service_bin
+		io_service_get_matching_services_bin
+		io_service_add_notification_bin_64
+		io_registry_entry_get_properties_bin_buf
+		io_registry_entry_get_property_bin_buf
+		mach_port_get_context_from_user
+		task_info_from_user
+		task_get_special_port_from_user
+		task_set_special_port
+		semaphore_create
+		task_set_exc_guard_behavior
+		vm_remap_external
+		vm_reallocate
+		mach_vm_behavior_set
+		mach_vm_map_external
+		mach_vm_region_recurse
+		_mach_make_memory_entry
+		mach_vm_deferred_reclamation_buffer_flush
+		mach_vm_range_create
+		mach_vm_reallocate
+		UNDNotificationCreated_rpc
+		task_restartable_ranges_register
+		task_restartable_ranges_synchronize)
 )
 
 (deny sysctl*
```
