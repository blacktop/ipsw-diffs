## AirPlaySenderService

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
 		(iokit-registry-entry-class "AppleAVE2Driver")

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
 		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))

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
+		CTLIOCGINFO
 		SIOCGIFADDR
 		SIOCGIFCONSTRAINED
 		SIOCGIFDELEGATE

 		SYS_getattrlist
 		SYS_fgetattrlist
 		SYS_fsetattrlist
+		SYS_listxattr
 		SYS_fsctl
 		SYS_shm_open
 		SYS_sysctlbyname

 		SYS_getentropy
 		SYS_necp_open
 		SYS_necp_client_action
+		SYS___nexus_set_opt
 		SYS___channel_get_info
 		SYS___channel_sync
 		SYS_ulock_wait

 		F_GETPATH
 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS
+		F_BARRIERFSYNC
+		F_OFD_GETLK
+		F_OFD_SETLKWTIMEOUT
 		F_ADDFILESIGS_RETURN
 		F_CHECK_LV)
 )

 		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
 		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
 		NECP_CLIENT_ACTION_MAP_SYSCTLS
-		NECP_CLIENT_ACTION_REMOVE_FLOW)
+		NECP_CLIENT_ACTION_REMOVE
+		NECP_CLIENT_ACTION_REMOVE_FLOW
+		NECP_CLIENT_ACTION_UPDATE_CACHE)
 )
 
 (allow process-exec-update-label)
```
