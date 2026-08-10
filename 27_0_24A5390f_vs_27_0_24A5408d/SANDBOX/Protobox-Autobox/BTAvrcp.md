## BTAvrcp

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.Music.MPMusicPlayerControllerInternal"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))

 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.itunescloudd.xpc"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
+		(require-not (global-name "com.apple.dnssd.service"))
+		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.medialibraryd.xpc"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.logd.events"))

 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
 		(require-not (xpc-service-name "com.apple.datamigrator"))
+		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		SYS_memorystatus_control
 		SYS_guarded_open_np
 		SYS_guarded_close_np
+		SYS_change_fdguard_np
 		SYS_openat
 		SYS_openat_nocancel
 		SYS_fstatat

 		SYS_guarded_pwrite_np
 		SYS_persona
 		SYS_getentropy
+		SYS_necp_open
+		SYS_necp_client_action
+		SYS___channel_open
+		SYS___channel_get_info
+		SYS___channel_sync
+		SYS___channel_get_opt
+		SYS___channel_set_opt
 		SYS_ulock_wait
 		SYS_ulock_wake
 		SYS_terminate_with_payload

 (deny system-fcntl)
 (allow system-fcntl
 	(fcntl-command
+		F_GETFD
 		F_SETFD
 		F_GETFL
 		F_NOCACHE
```
