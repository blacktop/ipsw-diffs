## textcontextd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.generativesearch.server.search"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
-		(require-not (global-name "com.apple.locationd.synchronous"))
-		(require-not (global-name "com.apple.contactsd"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.contacts.poster.api"))
-		(require-not (global-name "com.apple.TextInput.accessibility"))
-		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.biome.access.user"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
+		(require-not (global-name "com.apple.TextInput.accessibility"))
+		(require-not (global-name "com.apple.coremedia.mediaplaybackd.sandboxserver.xpc"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.tccd"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
+		(require-not (global-name "com.apple.locationd.synchronous"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.contacts.poster.api"))
+		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (global-name "com.apple.coremedia.mediaplaybackd.remaker.xpc"))
+		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
+		(require-not (global-name "com.apple.generativesearch.server.search"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.coremedia.mediaplaybackd.player.xpc"))
 		(require-not (global-name "com.apple.corerecents.recentsd"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.tccd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.contactsd"))
 		(require-not (local-name "com.apple.iphone.axserver"))
-		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
+		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))

 		task_set_exc_guard_behavior
 		task_create_identity_token
 		thread_policy
+		thread_policy_set
 		vm_remap_external
 		vm_reallocate
 		mach_vm_read
```
