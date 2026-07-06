## SyncAgent

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
-		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.safarifetcherd"))
+		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))
-		(require-not (global-name "com.apple.calaccessd"))
-		(require-not (global-name "com.apple.mobile.heartbeat"))
-		(require-not (global-name "com.apple.calaccessd.xpc"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.iokit.powerdxpc"))
+		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
+		(require-not (global-name "com.apple.tccd"))
+		(require-not (global-name "com.apple.accountsd.accountmanager"))
+		(require-not (global-name "com.apple.coremedia.admin"))
+		(require-not (global-name "com.apple.safarifetcherd"))
+		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.spotlight.IndexAgent"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3"))
+		(require-not (global-name "com.apple.linkd.autoShortcut"))
+		(require-not (global-name "com.apple.springboard.services"))
+		(require-not (global-name "com.apple.privacyaccountingd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (require-any
 			(global-name "com.apple.DeviceLink.SyncAgent.${ANY_UUID}.Device.HandlerMessagePort")
 			(global-name "com.apple.DeviceLink.SyncAgent.${ANY_UUID}.Device.MainMessagePort")
 		))
-		(require-not (global-name "com.apple.accountsd.accountmanager"))
-		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
-		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
-		(require-not (global-name "com.apple.trustd"))
-		(require-not (global-name "com.apple.icloudmailagent.secret.xpc"))
-		(require-not (global-name "com.apple.springboard.services"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.remindd"))
-		(require-not (global-name "com.apple.spotlight.IndexAgent"))
-		(require-not (global-name "com.apple.coremedia.admin"))
-		(require-not (global-name "com.apple.iokit.powerdxpc"))
-		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.PowerManagement.control"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.privacyaccountingd"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (global-name "com.apple.chronoservices"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.linkd.autoShortcut"))
-		(require-not (global-name "com.apple.tccd"))
-		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.frontboard.systemappservices"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (global-name "com.apple.aggregated"))
-		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.icloudmailagent.secret.xpc"))
+		(require-not (global-name "com.apple.calaccessd.xpc"))
 		(require-not (xpc-service-name "com.apple.datamigrator"))
+		(require-not (global-name "com.apple.PowerManagement.control"))
+		(require-not (global-name "com.apple.chronoservices"))
+		(require-not (global-name "com.apple.mobile.heartbeat"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.remindd"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.aggregated"))
+		(require-not (global-name "com.apple.calaccessd"))
+		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
+		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.ABDatabaseDoctor"))
 		(require-not (system-attribute developer-mode))
 	)

 		SYS_ioctl
 		SYS_readlink
 		SYS_umask
+		SYS_msync
 		SYS_munmap
 		SYS_mprotect
 		SYS_madvise

 		SYS_getumask
 		SYS_open_dprotected_np
 		SYS_getattrlist
+		SYS_fsetattrlist
 		SYS_getxattr
+		SYS_fsetxattr
 		SYS_fsctl
 		SYS_shm_open
 		SYS_sem_open

 		SYS_write_nocancel
 		SYS_open_nocancel
 		SYS_close_nocancel
+		SYS_msync_nocancel
 		SYS_fcntl_nocancel
 		SYS_fsync_nocancel
 		SYS_sigsuspend_nocancel

 					mach_exception_raise
 					mach_exception_raise_state
 					mach_exception_raise_state_identity))
+				(require-not (kernel-mig-routine vm_remap_external))
 				(require-not (kernel-mig-routine task_restartable_ranges_register))
 				(require-not (kernel-mig-routine task_restartable_ranges_synchronize))
-				(require-not (kernel-mig-routine semaphore_create))
 				(require-not (kernel-mig-routine mach_vm_reallocate))
+				(require-not (kernel-mig-routine semaphore_create))
 				(require-not (kernel-mig-routine task_info_from_user))
-				(require-not (kernel-mig-routine vm_remap_external))
 				(require-not (kernel-mig-routine io_service_open_extended))
 				(require-not (kernel-mig-routine vm_reallocate))
 			)
```
