## destinationd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
+		(require-not (global-name "com.apple.ExternalAccessory.distributednotification.server"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.Location.readOnly"))
 		(require-not (global-name "com.apple.appleneuralengine"))
+		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.Maps.MapsSync.store"))
 		(require-not (global-name "com.apple.iap2d.xpc"))

 		(require-not (global-name "com.apple.xpc.amsengagementd"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
+		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.kvsd"))
 		(require-not (global-name "com.apple.coremedia.admin"))
 		(require-not (global-name "com.apple.coremedia.endpoint.xpc"))
-		(require-not (require-any
-			(global-name "com.apple.findmy.findmylocate.friendshipservice")
-			(global-name "com.apple.findmy.findmylocate.settings")
-		))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
+		(require-not (global-name "com.apple.findmy.findmylocate.friendshipservice"))
 		(require-not (global-name "com.apple.maps.virtualgarage.server"))
 		(require-not (global-name "com.apple.suggestd.events"))
 		(require-not (require-any

 		(require-not (global-name "com.apple.inputservice.keyboardui"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.findmy.findmylocate.locationservice"))

 		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.passd.payment"))
-		(require-not (xpc-service-name "com.apple.weatherkit.authservice"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.findmy.findmylocate.fencesservice"))
 		(require-not (global-name "com.apple.carkit.service"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
+		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.findmy.findmylocate.settings"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.NamedEntity.readOnly"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.Connections"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))

 		(require-not (global-name "com.apple.imagent.embedded.auth"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.passd.library"))
+		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.financed.service.coredatastore"))
 		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))

 		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (xpc-service-name "com.apple.MFAAuthentication.MFAANetwork"))
 		(require-not (xpc-service-name "com.apple.FinanceImageProcessingService"))
+		(require-not (xpc-service-name "com.apple.weatherkit.authservice"))
 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
-				(require-not (global-name "com.apple.ExternalAccessory.distributednotification.server"))
-				(require-not (global-name "com.apple.FileCoordination"))
-				(require-not (global-name "com.apple.FSEvents"))
-				(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
-				(require-not (global-name "com.apple.CoreServices.coreservicesd"))
-				(require-not (global-name "com.apple.CARenderServer"))
-				(require-not (global-name "com.apple.AppSSO.service-xpc"))
+				(require-not (require-any
+					(global-name "P.-")
+					(global-name "P.S")
+				))
+				(require-not (global-name "P.o"))
 				(require-not (system-attribute developer-mode))
 			)
 			(require-all
 				(xpc-service-name "*")
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
-				(require-not (global-name "com.apple.ExternalAccessory.distributednotification.server"))
-				(require-not (global-name "com.apple.FileCoordination"))
-				(require-not (global-name "com.apple.FSEvents"))
-				(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
-				(require-not (global-name "com.apple.CoreServices.coreservicesd"))
-				(require-not (global-name "com.apple.CARenderServer"))
-				(require-not (global-name "com.apple.AppSSO.service-xpc"))
+				(require-not (require-any
+					(global-name "P.-")
+					(global-name "P.S")
+				))
+				(require-not (global-name "P.o"))
 				(require-not (system-attribute developer-mode))
 			)
 		)

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
 (deny system-mac-syscall
 	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
+(with-filter (mac-policy-name "vnguard")
+	(deny system-mac-syscall
+		(require-not (mac-syscall-number 1))
 	)
 )
 (deny system-mac-syscall
```
