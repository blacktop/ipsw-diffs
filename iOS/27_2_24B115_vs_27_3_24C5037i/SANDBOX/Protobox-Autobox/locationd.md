## locationd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.carousel.sessionservice"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
 		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
+		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.identityservicesd.idquery.embedded.auth"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.icloud.searchpartyd.beaconmanager"))

 		(require-not (global-name "com.apple.StatusKit.local"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.perceptiond.context"))
+		(require-not (global-name "com.apple.AudioAccessoryServices"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.geoanalyticsd"))
 		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
+		(require-not (require-any
+			(global-name "x.I")
+			(global-name "x.b")
+		))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.navigationListener"))

 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.momentsd"))
 		(require-not (require-any
+			(global-name "com.apple.AccessorySensorManager")
 			(global-name "com.apple.Carousel.statusOverlayServer")
 			(global-name "com.apple.gpsd")
 			(global-name "com.apple.icloud.searchpartyd.advertisementcache")

 		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.sessionservices"))
-		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
+		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
 		(require-not (global-name "com.apple.systemstatus.publisher"))
 		(require-not (global-name "com.apple.modelcatalog.catalog"))
 		(require-not (xpc-service-name "com.apple.MFAAuthentication.MFAANetwork"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (xpc-service-name "com.apple.corelocation.maphelperservice"))
 		(require-not (global-name "com.apple.carkit.service"))
 		(require-not (global-name "com.apple.nearbyd.xpc.nearbyinteraction.observer"))
 		(require-not (global-name "com.apple.wirelessproxd"))

 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.heartratecoordinatord.requestor"))
 		(require-not (global-name "com.apple.countryd.update"))
-		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
+		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
 		(require-not (global-name "com.apple.sos"))
 		(require-not (global-name "com.apple.icloud.searchpartyd.ownersession"))
-		(require-not (xpc-service-name "com.apple.corelocation.maphelperservice"))
+		(require-not (xpc-service-name "com.apple.CoreRepairCoreXPCService"))
 		(require-not (global-name "com.apple.cache_delete"))
 		(require-not (global-name "com.apple.healthlited"))
 		(require-not (global-name "com.apple.PowerManagement.control"))

 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))
+		(require-not (global-name "P.o"))
 		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
 		(require-not (global-name "com.apple.system.logger"))
-		(require-not (xpc-service-name "com.apple.CoreRepairCoreXPCService"))
+		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.familycircle.agent"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.appprotectiond.read"))
+		(require-not (global-name "com.apple.spaceattributiond"))
+		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.routined.registration"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.spaceattributiond"))
-		(require-not (global-name "com.apple.lsd.open"))
-		(require-not (global-name "com.apple.CARenderServer"))
-		(require-not (global-name "com.apple.AudioAccessoryServices"))
-		(require-not (global-name "com.apple.AccessorySensorManager"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
-	)
-)
-(deny system-mac-syscall
-	(require-any
-		(require-not (mac-policy-name "AMFI"))
-		(require-not (mac-syscall-number 90))
-	)
-)
+(deny system-mac-syscall)
 
 (deny system-memorystatus-control)
 (allow system-memorystatus-control
```
