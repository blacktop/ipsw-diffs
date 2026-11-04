## passd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.PassbookUISceneService.remote-ui"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (xpc-service-name "com.apple.PassKitCoreXPCService"))
+		(require-not (xpc-service-name "com.apple.weatherkit.authservice"))
 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.passd.cloud-store"))
 		(require-not (global-name "com.apple.mobileactivationd"))

 		(require-not (global-name "com.apple.installcoordinationd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.private.seserviced.jpki.client"))
-		(require-not (xpc-service-name "com.apple.FinHealth.FinHealthXPCServices"))
+		(require-not (xpc-service-name "com.apple.PassKitCoreXPCService"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (require-any
 			(global-name "com.apple.idcredd.biometrics.xpc")

 		(require-not (global-name "com.apple.nfcd.hwmanager"))
 		(require-not (global-name "com.apple.amsservicesanalytics.xpc"))
 		(require-not (global-name "com.apple.runningboard"))
-		(require-not (xpc-service-name "com.apple.PassKitServicesXPCService"))
+		(require-not (xpc-service-name "com.apple.FinHealth.FinHealthXPCServices"))
 		(require-not (global-name "com.apple.fairplayd.xpc"))
 		(require-not (global-name "com.apple.asd.scoring"))
-		(require-not (xpc-service-name "com.apple.pay.finance.FinanceImageProcessingService"))
+		(require-not (xpc-service-name "com.apple.PassKitServicesXPCService"))
 		(require-not (global-name "com.apple.homed.xpc"))
 		(require-not (global-name "com.apple.pearld"))
 		(require-not (global-name "com.apple.odi.legacySPIService"))
 		(require-not (global-name "com.apple.adid"))
-		(require-not (global-name "com.apple.calaccessd"))
+		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
 		(require-not (global-name "com.apple.coreduetd.context"))
-		(require-not (xpc-service-name "com.apple.FinanceImageProcessingService"))
+		(require-not (xpc-service-name "com.apple.pay.finance.FinanceImageProcessingService"))
 		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
 		(require-not (global-name "com.apple.NPKNanoPassDaemonConnection.XPC"))
 		(require-not (global-name "com.apple.imagent.embedded.auth"))

 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.Contact"))
+		(require-not (global-name "com.apple.weatherkit.authservice"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.servicesanalytics.xpc"))
 		(require-not (global-name "com.apple.seld.tsmmanager"))

 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.xpc.amstoold"))
 		(require-not (global-name "com.apple.parsecd"))
-		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
+		(require-not (xpc-service-name "com.apple.FinanceImageProcessingService"))
 		(require-not (global-name "com.apple.passd.assertions"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.remindd"))

 		(require-not (global-name "com.apple.mobilerepaird"))
 		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.routined.registration"))
-		(require-not (global-name "com.apple.appprotectiond.read"))
+		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.financed.service.bankconnect"))
 		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.spotlight.SearchAgent"))
 		(require-not (global-name "com.apple.siri.vocabularyupdates"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.Topic.readOnly"))
+		(require-not (global-name "com.apple.calaccessd"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon"))

 
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
