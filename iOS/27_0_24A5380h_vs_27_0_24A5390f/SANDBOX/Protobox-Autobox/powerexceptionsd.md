## powerexceptionsd

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
 		(iokit-registry-entry-class "AppleKeyStore")
 		(iokit-registry-entry-class "AppleSMCKeysEndpoint")

 	)
 )
 
-(deny iokit-set-properties
+(deny iokit-open-service
 	(require-any
 		(require-not (iokit-property "#cpu-runaway-sfi-follows-bg"))
 		(require-not (iokit-registry-entry-class "AppleCLPC"))
 	)
 )
 
+(deny iokit-set-properties)
+
 (deny ipc*)
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")

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
 		(require-not (global-name "com.apple.duetactivityscheduler"))

 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 
 (deny syscall-unix)

 		SYS_sendto
 		SYS_mkdir
 		SYS_rmdir
+		SYS_gethostuuid
 		SYS_pread
 		SYS_pwrite
 		SYS_statfs

 		SYS_coalition_info
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_renameat
 		SYS_fstatat
 		SYS_fstatat64
+		SYS_unlinkat
 		SYS_mkdirat
 		SYS_bsdthread_ctl
 		SYS_guarded_open_dprotected_np
 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
 		SYS_guarded_writev_np
+		SYS_stack_snapshot_with_config
 		SYS_persona
 		SYS_getentropy
 		SYS_ulock_wait

 		mach_exception_raise
 		mach_exception_raise_state
 		mach_exception_raise_state_identity
+		io_iterator_next
 		io_registry_entry_from_path
+		io_registry_entry_get_child_iterator
 		io_registry_entry_set_properties
 		io_service_open_extended
 		io_connect_method
 		io_server_version
 		io_service_get_matching_service_bin
+		io_registry_entry_get_properties_bin_buf
 		io_registry_entry_get_property_bin_buf
 		mach_port_deallocate
 		mach_port_request_notification
```
