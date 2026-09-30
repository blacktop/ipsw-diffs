## sirittsd

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
 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleKeyStore")

 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
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
 		(require-not (global-name "com.apple.storekitd"))

 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.powerexperienced.resourceusage"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
+		(require-not (global-name "com.apple.biome.compute.source.user"))
 		(require-not (global-name "com.apple.privatecloudcompute"))
 		(require-not (global-name "com.apple.modelmanager"))
 		(require-not (global-name "com.apple.erm.logging"))

 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 (allow socket-ioctl
 	(ioctl-command

 		io_iterator_reset
 		io_registry_create_iterator
 		io_registry_entry_from_path
+		io_registry_entry_get_name
 		io_registry_entry_get_parent_iterator
 		io_service_close
 		io_registry_entry_create_iterator

 		mach_port_set_attributes
 		mach_port_get_context_from_user
 		mach_port_is_connection_for_service
+		task_threads_from_user
 		task_info_from_user
 		task_get_special_port_from_user
 		task_set_special_port

 		semaphore_destroy
 		task_set_exc_guard_behavior
 		task_create_identity_token
+		thread_terminate
 		thread_info
 		thread_policy
 		thread_policy_set

 		mach_vm_region_recurse
 		mach_vm_region
 		_mach_make_memory_entry
+		mach_vm_page_range_query
 		mach_vm_deferred_reclamation_buffer_flush
 		mach_vm_range_create
 		mach_vm_reallocate
```
