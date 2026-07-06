## remotemanagementd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.networkscored"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.accountsd.accountmanager"))
+		(require-not (global-name "com.apple.mobilegestalt.xpc"))
+		(require-not (global-name "com.apple.duetactivityscheduler"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.inputservice.keyboardui"))
 		(require-not (global-name "com.apple.apsd"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.accountsd.accountmanager"))
+		(require-not (global-name "com.apple.inputservice.keyboardui"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.mobileactivationd"))
-		(require-not (global-name "com.apple.managedconfiguration.mdmdservice"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
-		(require-not (global-name "com.apple.managedconfiguration.profiled"))
-		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (global-name "com.apple.duetactivityscheduler"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
-		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (xpc-service-name "com.apple.security.XPCAcmeService"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.managedconfiguration.mdmdservice"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.managedconfiguration.profiled"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.AuthenticationServices.ASConfigurationSubscriber")
 			(xpc-service-name "com.apple.remotemanagement.AccountSubscriber")

 			(xpc-service-name "com.apple.remotemanagement.WatchEnrollmentSubscriber")
 		))
 		(require-not (xpc-service-name "com.apple.SafariShared.SafariConfigurationSubscriber"))
+		(require-not (xpc-service-name "com.apple.security.XPCAcmeService"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon"))

 		io_object_conforms_to
 		io_iterator_next
 		io_iterator_reset
+		io_registry_create_iterator
 		io_registry_entry_from_path
 		io_registry_entry_get_parent_iterator
 		io_registry_entry_create_iterator
```
