## familycircled

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.ExternalAccessory.distributednotification.server"))
 		(require-not (global-name "com.apple.adid.xpc"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (global-name "com.apple.iap2d.xpc"))

 		(require-not (global-name "com.apple.apsd"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
+		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.cksharingmanagementd"))
 		(require-not (global-name "com.apple.networkd_privileged"))
 		(require-not (global-name "com.apple.GameController.gamecontrollerd"))

 			(global-name "com.apple.family.sharing-client.com.apple.ScreenTimeSettings.development")
 			(global-name "com.apple.familycircled.settings")
 		))
+		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (require-any
 			(global-name "com.apple.iap2d.ExternalAccessory.distributednotification.server")
 			(global-name "com.apple.iaptransportd.ExternalAccessory.distributednotification.server")

 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.ak.anisette.xpc"))
+		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.cfnetwork.AuthBrokerAgent"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.identityservicesd.pds"))

 		(require-not (global-name "com.apple.ScreenTimeAgent.setup"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
 		(require-not (global-name "com.apple.coreduetd.people"))
+		(require-not (global-name "com.apple.ScreenTimeSettingsAgent.private"))
 		(require-not (global-name "com.apple.familycircled.sharing"))
 		(require-not (global-name "com.apple.PineBoardRiseServices"))
 		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))

 		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
 		(require-not (xpc-service-name "com.apple.MFAAuthentication.MFAANetwork"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
-		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
-		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
+		(require-not (global-name "com.apple.CoreAuthentication.daemon.libxpc"))
+		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.ABDatabaseDoctor"))
```
