## watchdogd

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "AppleAPFSUserClient")
 		(iokit-registry-entry-class "AppleCredentialManagerUserClient")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
+		(iokit-registry-entry-class "EndpointSecurityExternalClient")
 		(iokit-registry-entry-class "IOReportUserClient")
 		(iokit-registry-entry-class "IOWatchdogUserClient")
 		(iokit-registry-entry-class "RootDomainUserClient")

 		(iokit-registry-entry-class "AppleT8150PMGR")
 		(iokit-registry-entry-class "AppleT8301PMGR")
 		(iokit-registry-entry-class "AppleT8310PMGR")
+		(iokit-registry-entry-class "EndpointSecurityDriver")
 		(iokit-registry-entry-class "IOPMrootDomain")
 		(iokit-registry-entry-class "IOReportHub")
 	)

 		SYS___pthread_fchdir
 		SYS_bsdthread_create
 		SYS_bsdthread_terminate
+		SYS_kqueue
 		SYS_bsdthread_register
 		SYS_workq_open
 		SYS_workq_kernreturn

 		SYS_fileport_makefd
 		SYS_memorystatus_control
 		SYS_guarded_close_np
+		SYS_guarded_kqueue_np
 		SYS_change_fdguard_np
 		SYS_connectx
 		SYS_getattrlistbulk

 		SYS_terminate_with_payload
 		SYS_abort_with_payload
 		SYS_os_fault_with_payload
+		SYS_kqueue_workloop_ctl
 		SYS_memorystatus_available_memory
 		SYS_objc_bp_assist_cfg_np
 		SYS_shared_region_map_and_slide_2_np

 		io_connect_map_memory_into_task
 		io_connect_unmap_memory_from_task
 		io_connect_method
+		io_connect_set_notification_port_64
 		io_service_add_interest_notification_64
 		io_registry_entry_get_registry_entry_id
 		io_server_version
```
