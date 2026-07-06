## nutritiond

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.modelmanager"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.arkit.service.NutritionService"))
-		(require-not (global-name "com.apple.perceptiond.context"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.nehelper"))
-		(require-not (global-name "com.apple.coremedia.capturesession"))
-		(require-not (global-name "com.apple.dnssd.service"))
-		(require-not (global-name "com.apple.coremedia.capturesource"))
-		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.trustd"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.visualintelligence.visual-action-prediction"))
-		(require-not (global-name "com.apple.healthd.server"))
-		(require-not (global-name "com.apple.nutritiond.image-analysis"))
 		(require-not (global-name "com.apple.biome.access.user"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (global-name "com.apple.lsd.open"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.biome.access.system"))
-		(require-not (global-name "com.apple.ProgressReporting"))
-		(require-not (global-name "com.apple.modelcatalog.catalog"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.appleneuralengine"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.linkd.registry"))
-		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
+		(require-not (global-name "com.apple.coremedia.capturesource"))
+		(require-not (global-name "com.apple.appleneuralengine"))
+		(require-not (global-name "com.apple.coremedia.capturesession"))
+		(require-not (global-name "com.apple.healthd.server"))
+		(require-not (global-name "com.apple.biome.access.system"))
+		(require-not (global-name "com.apple.perceptiond.context"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3"))
+		(require-not (global-name "com.apple.modelmanager"))
+		(require-not (global-name "com.apple.modelcatalog.catalog"))
+		(require-not (global-name "com.apple.nehelper"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.dnssd.service"))
+		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.nutritiond.image-analysis"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.arkit.service.NutritionService"))
+		(require-not (global-name "com.apple.visualintelligence.visual-action-prediction"))
+		(require-not (global-name "com.apple.ProgressReporting"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
+		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))

 		SYS_getpid
 		SYS_getuid
 		SYS_geteuid
+		SYS_recvmsg
 		SYS_sendmsg
 		SYS_recvfrom
 		SYS_access
+		SYS_chflags
 		SYS_fchflags
 		SYS_crossarch_trap
 		SYS_dup

 		SYS_setsockopt
 		SYS_sigsuspend
 		SYS_gettimeofday
+		SYS_getsockopt
 		SYS_readv
 		SYS_writev
 		SYS_fchown

 		SYS_write_nocancel
 		SYS_open_nocancel
 		SYS_close_nocancel
+		SYS_recvmsg_nocancel
 		SYS_sendmsg_nocancel
 		SYS_recvfrom_nocancel
 		SYS_fcntl_nocancel

 		SYS___channel_open
 		SYS___channel_get_info
 		SYS___channel_sync
+		SYS___channel_get_opt
+		SYS___channel_set_opt
 		SYS_ulock_wait
 		SYS_ulock_wake
 		SYS_terminate_with_payload
```
