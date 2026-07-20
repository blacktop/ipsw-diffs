## symptomsd

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
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
+		(iokit-registry-entry-class "AppleSPUHIDDriverUserClient")
 		(iokit-registry-entry-class "RootDomainUserClient")
 	)
 )
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(deny iokit-open-user-client)
+(allow iokit-open-user-client
 	(require-any
 		(iokit-registry-entry-class "AppleKeyStore")
+		(iokit-registry-entry-class "AppleSPUHIDDriver")
+		(iokit-registry-entry-class "AppleSPUHIDEventDriver")
 		(iokit-registry-entry-class "IOPMrootDomain")
 	)
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
 		(ipc-posix-name "apple.cfprefs.*")
 		(ipc-posix-name "apple.cfprefs.daemonv1")

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
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))

 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
+		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.usymptomsd"))

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

 		SYS_fsgetpath
 		SYS_audit_session_self
 		SYS_audit_session_join
+		SYS_fileport_makeport
 		SYS_fileport_makefd
 		SYS_audit_session_port
 		SYS_memorystatus_control

 		MSC__kernelrpc_mach_port_get_attributes_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
+		MSC_task_name_for_pid
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
 		MSC_swtch_pri

 		io_registry_entry_get_name
 		io_registry_entry_get_parent_iterator
 		io_registry_entry_get_path
+		io_registry_get_root_entry
 		io_registry_entry_create_iterator
 		io_iterator_is_valid
 		io_registry_entry_get_name_in_plane
```
