## localspeechrecognition

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (xpc-service-name "com.apple.speech.localspeechrecognition"))
+		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))
 		(require-not (global-name "com.apple.modelmanager"))
 		(require-not (global-name "com.apple.generativeexperiences.textcomposition"))

 (deny process-exec*)
 
 (deny socket-ioctl)
+(allow socket-ioctl
+	(ioctl-command CTLIOCGINFO SIOCGCONNINFO)
+)
 
 (deny syscall-unix)
 (allow syscall-unix

 		SYS_getpid
 		SYS_getuid
 		SYS_geteuid
+		SYS_recvmsg
 		SYS_sendmsg
+		SYS_recvfrom
 		SYS_access
 		SYS_crossarch_trap
 		SYS_dup

 		SYS_rename
 		SYS_flock
 		SYS_sendto
+		SYS_shutdown
 		SYS_mkdir
 		SYS_rmdir
 		SYS_pread

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64

 		SYS_getentropy
 		SYS_necp_open
 		SYS_necp_client_action
+		SYS___nexus_set_opt
 		SYS___channel_open
 		SYS_ulock_wait
 		SYS_ulock_wake

 		thread_suspend
 		thread_resume
 		thread_info
+		thread_policy
 		thread_policy_set
 		vm_remap_external
 		vm_reallocate

 		F_GETFD
 		F_SETFD
 		F_GETFL
+		F_SETFL
 		F_GETLK
 		F_PREALLOCATE
 		F_RDADVISE

 )
 
 (deny system-necp-client-action)
+(allow system-necp-client-action
+	(necp-client-action
+		NECP_CLIENT_ACTION_ADD
+		NECP_CLIENT_ACTION_ADD_FLOW
+		NECP_CLIENT_ACTION_COPY_AGENT
+		NECP_CLIENT_ACTION_COPY_INTERFACE
+		NECP_CLIENT_ACTION_COPY_RESULT
+		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT_FINAL
+		NECP_CLIENT_ACTION_MAP_SYSCTLS
+		NECP_CLIENT_ACTION_REMOVE
+		NECP_CLIENT_ACTION_REMOVE_FLOW
+		NECP_CLIENT_ACTION_UPDATE_CACHE)
+)
 
 (allow process-exec-update-label)
```
