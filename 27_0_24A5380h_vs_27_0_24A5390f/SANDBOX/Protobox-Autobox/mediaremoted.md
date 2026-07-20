## mediaremoted

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
 		(iokit-registry-entry-class "AppleJPEGDriver")

 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny ipc-posix-sem-open)
-(allow ipc-posix-sem-open
+(deny ipc-posix-sem-create)
+(allow ipc-posix-sem-create
 	(ipc-posix-name "purplebuddy.sentinel")
 )
 
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
 		(require-not (global-name "com.apple.biome.access.user"))

 		(require-not (global-name "com.apple.breadboardservices"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
 		(require-not (global-name "com.apple.StatusKit.presence"))
+		(require-not (global-name "com.apple.imagent.embedded.auth"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.airplay.receiver.mediaremote.services"))
 		(require-not (global-name "com.apple.gpumemd.source"))

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

 		SYS_getentropy
 		SYS_necp_open
 		SYS_necp_client_action
+		SYS___nexus_set_opt
 		SYS___channel_open
 		SYS___channel_get_info
 		SYS___channel_sync

 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS
 		F_DUPFD_CLOEXEC
+		F_BARRIERFSYNC
 		F_OFD_GETLK
 		F_OFD_SETLKWTIMEOUT
 		F_ADDFILESIGS_RETURN

 
 (deny system-kas-info)
 
-(with-filter (mac-policy-name "Sandbox")
-	(deny system-mac-syscall
-		(require-all
-			(require-not (mac-syscall-number 7))
-			(require-not (mac-syscall-number 6))
-			(require-not (mac-syscall-number 4))
-			(require-not (mac-syscall-number 67))
-			(require-not (mac-syscall-number 2))
-		)
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 1)
+		(require-not (mac-policy-name "vnguard"))
 	)
 )
 (deny system-mac-syscall

 		NECP_CLIENT_ACTION_COPY_RESULT
 		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
 		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
+		NECP_CLIENT_ACTION_MAP_SYSCTLS
 		NECP_CLIENT_ACTION_REMOVE
-		NECP_CLIENT_ACTION_REMOVE_FLOW)
+		NECP_CLIENT_ACTION_REMOVE_FLOW
+		NECP_CLIENT_ACTION_UPDATE_CACHE)
 )
 
 (allow process-exec-update-label)
```
