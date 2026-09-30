## com.apple.FTLivePhotoService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.facetimemessagestored.service"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.corerecents.recentsd"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.sandboxserver.xpc"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.remaker.xpc"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.player.xpc"))

 		SYS_getattrlistbulk
 		SYS_clonefileat
 		SYS_openat
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64

 		MSC__kernelrpc_mach_port_request_notification_trap
 		MSC_mach_timebase_info_trap
 		MSC_mk_timer_create
-		MSC_mk_timer_destroy)
+		MSC_mk_timer_destroy
+		MSC_mk_timer_arm)
 )
 
 (deny syscall-mig)
```
