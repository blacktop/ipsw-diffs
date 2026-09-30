## soundanalysisd

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
 		(iokit-registry-entry-class "AppleExternalSecondaryAudio")

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
 		(require-not (global-name "com.apple.appleneuralengine"))

 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
+(allow socket-ioctl
+	(ioctl-command SIOCGIFEFLAGS SIOCGIFMEDIA SIOCGIFTYPE)
+)
 
 (deny syscall-unix)
 (allow syscall-unix

 		SYS_getuid
 		SYS_geteuid
 		SYS_sendmsg
+		SYS_recvfrom
+		SYS_getpeername
+		SYS_getsockname
 		SYS_access
 		SYS_crossarch_trap
 		SYS_dup

 		SYS_rename
 		SYS_flock
 		SYS_sendto
+		SYS_shutdown
+		SYS_socketpair
 		SYS_mkdir
 		SYS_pread
 		SYS_pwrite

 		SYS_persona
 		SYS_work_interval_ctl
 		SYS_getentropy
+		SYS_necp_open
+		SYS_necp_client_action
 		SYS_ulock_wait
 		SYS_ulock_wake
 		SYS_terminate_with_payload

 		F_GETFD
 		F_SETFD
 		F_GETFL
+		F_SETFL
+		F_RDAHEAD
+		F_NOCACHE
 		F_GETPATH
 		F_GETPROTECTIONCLASS
 		F_BARRIERFSYNC

 )
 
 (deny system-necp-client-action)
+(allow system-necp-client-action
+	(necp-client-action
+		NECP_CLIENT_ACTION_ADD
+		NECP_CLIENT_ACTION_COPY_AGENT
+		NECP_CLIENT_ACTION_COPY_INTERFACE
+		NECP_CLIENT_ACTION_COPY_RESULT
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
+		NECP_CLIENT_ACTION_REMOVE)
+)
 
 (allow process-exec-update-label)
```
