## ind

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.apsd"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
+		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.biome.PublicStreamAccessService"))
 		(require-not (global-name "com.apple.networkd_privileged"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.generativeexperiences.availabilityService"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.ak.anisette.xpc"))
+		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.icloudsubscriptionoptimizerd.xpc.client"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.cfnetwork.AuthBrokerAgent"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))

 		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.cache_delete"))
+		(require-not (global-name "com.apple.CoreAuthentication.daemon.libxpc"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.ind.cloudfeatures"))

 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
-				(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
-				(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 				(require-not (global-name "com.apple.CoreAuthentication.daemon"))
 				(require-not (global-name "com.apple.AppSSO.service-xpc"))
 				(require-not (system-attribute developer-mode))

 				(xpc-service-name "*")
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
-				(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
-				(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 				(require-not (global-name "com.apple.CoreAuthentication.daemon"))
 				(require-not (global-name "com.apple.AppSSO.service-xpc"))
 				(require-not (system-attribute developer-mode))
```
