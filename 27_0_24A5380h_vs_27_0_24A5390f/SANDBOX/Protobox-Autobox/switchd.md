## switchd

> Group: ⬆️ Updated

```diff

 
 (deny generic-issue-extension)
 
-(deny iokit-issue-extension)
+(deny iokit-get-properties)
 
-(deny iokit-open-user-client)
-(allow iokit-open-user-client
+(deny iokit-open*)
+(allow iokit-open*
 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")

 	)
 )
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(deny iokit-open-user-client)
+(allow iokit-open-user-client
 	(iokit-registry-entry-class "AppleKeyStore")
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.daemonv1")
 		(ipc-posix-name "apple.cfprefs.system.daemonv1")

 	)
 )
 
-(deny job-creation)
+(allow ipc-sysv-shm)
 
-(deny mach-issue-extension)
+(deny isp-command-send)
 
-(deny mach-lookup
+(deny mach-host-special-port-set)
+
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.lsd.mapdb"))

 	)
 )
 
+(deny process-codesigning)
+(allow process-codesigning
+	(literal "/bin/sh")
+)
+
 (deny process-exec*)
 (allow process-exec*
 	(literal "/bin/sh")

 		MSC_mk_timer_cancel)
 )
 
-(deny syscall-mig
-	(require-all
-		(require-not (kernel-mig-routine
-			host_info
-			host_kernel_version
-			host_page_size
-			host_get_io_master
-			host_get_clock_service
-			host_request_notification
-			host_get_special_port
-			clock_get_time
-			mach_exception_raise
-			mach_exception_raise_state
-			mach_exception_raise_state_identity
-			io_iterator_next
-			io_registry_create_iterator
-			io_registry_entry_from_path
-			io_registry_entry_get_name
-			io_service_open_extended
-			io_connect_method
-			io_server_version
-			io_registry_entry_get_properties_bin_buf
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
-			thread_policy
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
+		host_kernel_version
+		host_page_size
+		host_get_io_master
+		host_get_clock_service
+		host_request_notification
+		host_get_special_port
+		clock_get_time
+		mach_exception_raise
+		mach_exception_raise_state
+		mach_exception_raise_state_identity
+		io_iterator_next
+		io_registry_create_iterator
+		io_registry_entry_from_path
+		io_registry_entry_get_name
+		io_service_open_extended
+		io_connect_method
+		io_server_version
+		io_registry_entry_get_properties_bin_buf
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
+		thread_policy
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
