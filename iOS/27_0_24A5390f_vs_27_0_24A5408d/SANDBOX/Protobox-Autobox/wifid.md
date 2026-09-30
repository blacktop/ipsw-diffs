## wifid

> Group: ⬆️ Updated

```diff

 		(require-not (require-any
 			(global-name "com.apple.wapi.client")
 			(global-name "com.apple.wifi.hostapd")
+			(global-name "com.apple.wirelessperception.session")
 		))
 		(require-not (global-name "com.apple.systemstatus"))
 		(require-not (global-name "com.apple.biome.access.system"))

 		(require-not (global-name "com.apple.coreduetd.knowledge"))
 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.geoanalyticsd"))
+		(require-not (xpc-service-name "com.apple.AppleDeviceQueryService"))
 		(require-not (global-name "com.apple.securityd.systemkeychain"))
 		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
 		(require-not (global-name "com.apple.system.notification_center"))

 		(require-not (global-name "com.apple.bluetooth.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.mDNSResponder.control"))
-		(require-not (xpc-service-name "com.apple.AppleDeviceQueryService"))
+		(require-not (xpc-service-name "com.apple.wifi.WiFiCloudAssetsXPCService"))
 		(require-not (global-name "com.apple.symptoms.symptomsd.managed_events"))
 		(require-not (global-name "com.apple.private.corewifi.internal-xpc"))
 		(require-not (global-name "com.apple.SystemConfiguration.IPMonitorControl"))

 		(require-not (global-name "com.apple.fontservicesd"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))
-		(require-not (xpc-service-name "com.apple.audio.analytics.service"))
+		(require-not (xpc-service-name "com.apple.audioanalyticsd"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.carkit.service"))

 		(require-not (global-name "com.apple.algosd"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (xpc-service-name "com.apple.wifi.WiFiCloudAssetsXPCService"))
+		(require-not (xpc-service-name "com.apple.audio.analytics.service"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))

 		(require-not (xpc-service-name "com.apple.wifi.ThreeBarsXPCService"))
 		(require-not (xpc-service-name "com.apple.ZhuGeService"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
-		(require-not (xpc-service-name "com.apple.audioanalyticsd"))
 		(require-not (global-name "com.apple.AccessorySetupUI"))
 		(require-not (system-attribute developer-mode))
 	)
```
