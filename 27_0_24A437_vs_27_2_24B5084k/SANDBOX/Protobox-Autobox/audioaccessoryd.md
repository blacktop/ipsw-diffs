## audioaccessoryd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.CompanionLink"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))

 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
 		(require-not (global-name "com.apple.BTAudioHALPlugin.xpc"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
+		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.erm.logging"))

 (deny socket-ioctl)
 (allow socket-ioctl
 	(ioctl-command
+		SIOCGIFAGENTDATA
 		SIOCGIFCONSTRAINED
 		SIOCGIFDELEGATE
 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )

 		SYS_geteuid
 		SYS_sendmsg
 		SYS_recvfrom
+		SYS_getsockname
 		SYS_access
 		SYS_crossarch_trap
 		SYS_dup

 		SYS_fsync
 		SYS_socket
 		SYS_connect
+		SYS_listen
 		SYS_sigsuspend
 		SYS_gettimeofday
 		SYS_getrusage

 		SYS_rename
 		SYS_flock
 		SYS_sendto
+		SYS_shutdown
 		SYS_mkdir
 		SYS_rmdir
 		SYS_pread

 		SYS_open_nocancel
 		SYS_close_nocancel
 		SYS_sendmsg_nocancel
+		SYS_recvfrom_nocancel
 		SYS_fcntl_nocancel
+		SYS_select_nocancel
 		SYS_fsync_nocancel
 		SYS_connect_nocancel
 		SYS_sigsuspend_nocancel

 (allow system-necp-client-action
 	(necp-client-action
 		NECP_CLIENT_ACTION_ADD
+		NECP_CLIENT_ACTION_ADD_FLOW
+		NECP_CLIENT_ACTION_AGENT
 		NECP_CLIENT_ACTION_COPY_AGENT
 		NECP_CLIENT_ACTION_COPY_INTERFACE
 		NECP_CLIENT_ACTION_COPY_RESULT
-		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT)
+		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
+		NECP_CLIENT_ACTION_MAP_SYSCTLS
+		NECP_CLIENT_ACTION_REMOVE
+		NECP_CLIENT_ACTION_REMOVE_FLOW)
 )
```
