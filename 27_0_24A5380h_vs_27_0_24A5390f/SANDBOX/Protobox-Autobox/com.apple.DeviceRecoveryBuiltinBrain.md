## com.apple.DeviceRecoveryBuiltinBrain

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
 	(iokit-registry-entry-class "AppleAPFSContainer")
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(ipc-posix-name "apple.shm.notification_center")
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
 		(require-not (global-name "com.apple.system.notification_center"))

 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 
 (deny syscall-unix)

 		SYS_dup2
 		SYS_fcntl
 		SYS_fsync
+		SYS_socket
 		SYS_sigsuspend
 		SYS_gettimeofday
 		SYS_readv

 			_mach_make_memory_entry
 			mach_vm_range_create
 			mach_vm_reallocate
+			mach_memory_entry_ownership
 			mach_voucher_attr_command
 			task_restartable_ranges_register
 			task_restartable_ranges_synchronize))

 
 (deny system-mac-syscall
 	(require-all
-		(mac-syscall-number 90)
+		(mac-syscall-number 90 96)
 		(require-not (mac-policy-name "AMFI"))
 	)
 )
```
