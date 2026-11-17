## PerfPowerServices

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.biome.access.system"))
 		(require-not (global-name "com.apple.accessories.connection-info-server"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "%"))
 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.ak.auth.xpc"))
 		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))

 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.symptom_analytics"))
 		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
-		(require-not (require-any
-			(global-name "P.-")
-			(global-name "P.S")
-		))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.iapd.xpc"))
 		(require-not (global-name "com.apple.batteryintelligenced.chargetimeestimator"))

 		(require-not (xpc-service-name "com.apple.PPSFeatureFlagReader"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.nfcd.hwmanager"))
 		(require-not (global-name "com.apple.runningboard"))

 		(require-not (global-name "com.apple.ExposureNotification"))
 		(require-not (global-name "com.apple.centaurid.xpc"))
 		(require-not (global-name "com.apple.trial.status"))
-		(require-not (xpc-service-name "com.apple.PerfPowerServicesSignpostReader"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.ind.cloudfeatures"))

 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.wifip2pd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "P.o"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.xpc.amsaccountsd"))

 			(xpc-service-name "com.apple.PPSRelay")
 			(xpc-service-name "com.apple.PerfPowerServicesSignpostService")
 		))
-		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
+		(require-not (xpc-service-name "com.apple.PerfPowerServicesSignpostReader"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
+		(require-not (global-name "com.apple.AppSSO.service-xpc"))
+		(require-not (global-name "com.apple.AccessoryServices"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
 		SYS_guarded_writev_np
+		SYS_renameatx_np
 		SYS_persona
 		SYS_getentropy
 		SYS_necp_open
```
