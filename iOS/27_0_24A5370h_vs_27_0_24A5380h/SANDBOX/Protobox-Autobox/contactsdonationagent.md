## contactsdonationagent

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.lsd.icons"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.research.adtcd"))
-		(require-not (global-name "com.apple.commcenter.xpc"))
-		(require-not (global-name "com.apple.contactsd"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.pluginkit.pkd"))
-		(require-not (global-name "com.apple.contacts.poster.api"))
-		(require-not (global-name "com.apple.inputservice.keyboardui"))
-		(require-not (global-name "com.apple.debug.telemetry"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.kvsdebug"))
-		(require-not (global-name "com.apple.trustd"))
-		(require-not (global-name "com.apple.kvsd"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.contactsd.contacts-provider"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
-		(require-not (global-name "com.apple.contactsd.support"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (global-name "com.apple.erm.logging"))
-		(require-not (global-name "com.apple.imagent.embedded.auth"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
-		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
-		(require-not (global-name "com.apple.tccd"))
-		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
-		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (global-name "com.apple.aggregated"))
-		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
+		(require-not (global-name "com.apple.kvsd"))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
+		(require-not (global-name "com.apple.inputservice.keyboardui"))
+		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3"))
+		(require-not (global-name "com.apple.commcenter.xpc"))
+		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.pluginkit.pkd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.contacts.poster.api"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.contactsd.contacts-provider"))
+		(require-not (global-name "com.apple.dnssd.service"))
+		(require-not (global-name "com.apple.kvsdebug"))
+		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.contactsd.support"))
+		(require-not (global-name "com.apple.imagent.embedded.auth"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
+		(require-not (global-name "com.apple.debug.telemetry"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.research.adtcd"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.aggregated"))
+		(require-not (global-name "com.apple.contactsd"))
+		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.CARenderServer"))
+		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		SYS_fsync
 		SYS_socket
 		SYS_connect
+		SYS_setsockopt
 		SYS_gettimeofday
+		SYS_getsockopt
 		SYS_writev
 		SYS_fchmod
 		SYS_rename

 		SYS_close_nocancel
 		SYS_fcntl_nocancel
 		SYS_fsync_nocancel
+		SYS_connect_nocancel
 		SYS_sigsuspend_nocancel
 		SYS_writev_nocancel
 		SYS_pread_nocancel

 		SYS_renameatx_np
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
```
