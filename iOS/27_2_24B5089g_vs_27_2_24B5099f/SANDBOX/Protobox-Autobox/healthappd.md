## healthappd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.iap2d.xpc"))
 		(require-not (global-name "com.apple.healthd.server"))
 		(require-not (global-name "com.apple.systemstatus"))
+		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.nanoprefsync"))

 		(require-not (global-name "com.apple.modelmanager"))
 		(require-not (global-name "com.apple.symptom_analytics"))
 		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (require-any
+			(global-name "com.apple.corepersonalization.server.insights")
+			(global-name "com.apple.corepersonalization.server.memory")
+			(global-name "com.apple.healthcontentd")
+		))
 		(require-not (global-name "com.apple.iapd.xpc"))
 		(require-not (global-name "com.apple.fontservicesd"))
 		(require-not (global-name "com.apple.modelcatalog.catalog"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.healthrecordsd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (global-name "com.apple.healthcontentd"))
+		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
+		(require-not (xpc-service-name "com.apple.MFAAuthentication.MFAANetwork"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))

 		(require-not (global-name "com.apple.xpc.amstoold"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.NPKCompanionAgent.library"))
+		(require-not (global-name "com.apple.seymour"))
 		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
 		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (global-name "com.apple.carkit.navowners.service"))

 		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
 		(require-not (global-name "com.apple.contactsd"))
 		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
-		(require-not (xpc-service-name "com.apple.MFAAuthentication.MFAANetwork"))
-		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
```
