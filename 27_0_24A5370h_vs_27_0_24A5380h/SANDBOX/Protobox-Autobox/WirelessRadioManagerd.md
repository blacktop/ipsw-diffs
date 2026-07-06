## WirelessRadioManagerd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.modelmanager"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.conversationmanager"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.carousel.sessionservice"))
-		(require-not (global-name "com.apple.commcenter.xpc"))
-		(require-not (global-name "com.apple.SystemConfiguration.IPMonitorControl"))
-		(require-not (global-name "com.apple.wifip2pd"))
-		(require-not (global-name "com.apple.SystemConfiguration.configd"))
-		(require-not (global-name "com.apple.routined.registration"))
-		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.wifi.manager"))
-		(require-not (global-name "com.apple.symptom_analytics"))
-		(require-not (global-name "com.apple.gpumemd.source"))
-		(require-not (global-name "com.apple.wpantund.xpc"))
-		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
-		(require-not (global-name "com.apple.SBUserNotification"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
-		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.locationd.registration"))
-		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.wirelessinsightsd"))
-		(require-not (global-name "com.apple.mobileactivationd"))
-		(require-not (global-name "com.apple.FSEvents"))
-		(require-not (global-name "com.apple.commcenter.ari.rt.xpc"))
-		(require-not (global-name "com.apple.commcenter.atcs.xpc"))
-		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.iohideventsystem"))
-		(require-not (global-name "com.apple.symptom_diagnostics"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
-		(require-not (global-name "com.apple.biome.compute.source.user"))
-		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.carousel.sessionservice"))
 		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
 		(require-not (global-name "com.apple.appleneuralengine"))
-		(require-not (global-name "com.apple.frontboard.systemappservices"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (global-name "com.apple.triald.namespace-management"))
-		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.geoanalyticsd"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
+		(require-not (global-name "com.apple.wirelessinsightsd"))
+		(require-not (global-name "com.apple.SBUserNotification"))
+		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.SystemConfiguration.IPMonitorControl"))
+		(require-not (global-name "com.apple.commcenter.atcs.xpc"))
+		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
+		(require-not (global-name "com.apple.mobileactivationd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
+		(require-not (global-name "com.apple.wifi.manager"))
+		(require-not (global-name "com.apple.wpantund.xpc"))
+		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
+		(require-not (global-name "com.apple.biome.compute.source.user"))
+		(require-not (global-name "com.apple.commcenter.xpc"))
+		(require-not (global-name "com.apple.SystemConfiguration.configd"))
+		(require-not (global-name "com.apple.modelmanager"))
+		(require-not (global-name "com.apple.symptom_analytics"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.commcenter.ari.rt.xpc"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.conversationmanager"))
+		(require-not (global-name "com.apple.iohideventsystem"))
+		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
+		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.FSEvents"))
+		(require-not (global-name "com.apple.triald.namespace-management"))
+		(require-not (global-name "com.apple.gpumemd.source"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.wifip2pd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
+		(require-not (global-name "com.apple.routined.registration"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.AudioAccessoryServices"))
 		(require-not (system-attribute developer-mode))

 		io_service_add_notification_bin_64
 		io_registry_entry_get_properties_bin_buf
 		io_registry_entry_get_property_bin_buf
+		mach_port_deallocate
 		mach_port_get_refs
 		mach_port_request_notification
 		mach_port_set_attributes

 		semaphore_destroy
 		task_set_exc_guard_behavior
 		task_create_identity_token
+		thread_terminate
+		thread_suspend
 		thread_info
 		thread_policy
 		vm_copy
```
