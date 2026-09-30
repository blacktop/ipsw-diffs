## AXMediaUtilitiesService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.coremedia.decompressionsession"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))

 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.spotlight.IndexAgent"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
+		(require-not (global-name "com.apple.modelmanager"))
 		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
 		(require-not (global-name "com.apple.fontservicesd"))

 		SYS___semwait_signal_nocancel
 		SYS_fsgetpath
 		SYS_fileport_makeport
+		SYS_fileport_makefd
 		SYS_memorystatus_control
 		SYS_guarded_open_np
 		SYS_guarded_close_np

 		SYS_getentropy
 		SYS_necp_open
 		SYS_necp_client_action
+		SYS___nexus_set_opt
 		SYS___channel_open
 		SYS___channel_get_info
 		SYS___channel_sync
+		SYS___channel_get_opt
+		SYS___channel_set_opt
 		SYS_ulock_wait
 		SYS_ulock_wake
 		SYS_terminate_with_payload

 		semaphore_destroy
 		task_set_exc_guard_behavior
 		task_create_identity_token
+		thread_policy
 		thread_policy_set
 		vm_remap_external
 		vm_reallocate

 		F_GETPATH
 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS
+		F_DUPFD_CLOEXEC
 		F_SINGLE_WRITER
 		F_BARRIERFSYNC
 		F_OFD_SETLK

 		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT_FINAL
 		NECP_CLIENT_ACTION_MAP_SYSCTLS
 		NECP_CLIENT_ACTION_REMOVE
-		NECP_CLIENT_ACTION_REMOVE_FLOW)
+		NECP_CLIENT_ACTION_REMOVE_FLOW
+		NECP_CLIENT_ACTION_UPDATE_CACHE)
 )
 
 (allow process-exec-update-label)
```
