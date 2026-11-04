## UserEventAgent

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.ExternalAccessory.distributednotification.server"))
+		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.iap2d.xpc"))
 		(require-not (global-name "com.apple.systemstatus"))

 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
+		(require-not (global-name "h.1"))
 		(require-not (global-name "com.apple.coremedia.admin"))
 		(require-not (global-name "com.apple.networkd_privileged"))
 		(require-not (global-name "com.apple.SBUserNotification"))

 		(require-not (global-name "com.apple.server.bluetooth.general.xpc"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.networkscored"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.cfnetwork.AuthBrokerAgent"))
-		(require-not (global-name "com.apple.wifi.manager"))
-		(require-not (global-name "com.apple.accessories.transport-server"))
-		(require-not (global-name "com.apple.networkserviceproxy"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (global-name "com.apple.commcenter.xpc"))
-		(require-not (global-name "com.apple.SystemConfiguration.configd"))
-		(require-not (global-name "com.apple.erm.logging"))
-		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
-		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
-		(require-not (global-name "com.apple.iapd.xpc"))
-		(require-not (global-name "com.apple.audio.AudioSession"))
-		(require-not (global-name "com.apple.nehelper"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (global-name "com.apple.carkit.service"))
 		(require-not (require-any
+			(global-name "8.O")
+			(global-name "8.Z")
+			(global-name "8.e")
+			(global-name "8.p")
 			(global-name "com.apple.CTTelephonyCenter")
 			(global-name "com.apple.ExternalAccessory.matching")
 			(global-name "com.apple.IOUIAngel.LDCM")

 			(global-name "com.apple.systemconfiguration")
 			(global-name "com.apple.xpc.activity")
 		))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.cfnetwork.AuthBrokerAgent"))
+		(require-not (global-name "com.apple.wifi.manager"))
+		(require-not (global-name "com.apple.accessories.transport-server"))
+		(require-not (require-any
+			(global-name "x.I")
+			(global-name "x.b")
+		))
+		(require-not (global-name "com.apple.networkserviceproxy"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3"))
+		(require-not (global-name "com.apple.commcenter.xpc"))
+		(require-not (global-name "com.apple.SystemConfiguration.configd"))
+		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
+		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
+		(require-not (global-name "com.apple.iapd.xpc"))
+		(require-not (global-name "com.apple.audio.AudioSession"))
+		(require-not (global-name "com.apple.nehelper"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.carkit.service"))
 		(require-not (global-name "com.apple.algosd"))
+		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.locationd.registration"))

 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.diagnosticpipeline.service"))
 		(require-not (global-name "com.apple.FSEvents"))
+		(require-not (require-any
+			(global-name "P.-")
+			(global-name "P.S")
+		))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.GSSCred"))
 		(require-not (global-name "com.apple.logd.events"))

 		(require-not (global-name "com.apple.aggregated.addaily"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
+		(require-not (global-name "P.o"))
 		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
 		(require-not (global-name "com.apple.system.logger"))

 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (xpc-service-name "com.apple.audioanalyticsd"))
 		(require-not (xpc-service-name "com.apple.audio.analytics.service"))
-		(require-not (global-name "com.apple.CARenderServer"))
-		(require-not (global-name "com.apple.AppSSO.service-xpc"))
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
