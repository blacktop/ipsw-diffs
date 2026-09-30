## mediaremoted

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.PairingManager"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))

 (allow socket-ioctl
 	(ioctl-command
 		CTLIOCGINFO
+		SIOCGCONNINFO
 		SIOCGIFCONSTRAINED
 		SIOCGIFDELEGATE
 		SIOCGIFEXPENSIVE

 		SYS_rename
 		SYS_flock
 		SYS_sendto
+		SYS_shutdown
 		SYS_socketpair
 		SYS_mkdir
 		SYS_rmdir

 		SYS_fclonefileat
 		SYS_terminate_with_payload
 		SYS_abort_with_payload
+		SYS_necp_session_action
 		SYS_os_fault_with_payload
 		SYS_kqueue_workloop_ctl
 		SYS_memorystatus_available_memory
```
