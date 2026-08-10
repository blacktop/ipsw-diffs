## nfcd

> Group: ⬆️ Updated

```diff

 		(require-not (xpc-service-name "com.apple.SiriTTSService.TrialProxy"))
 		(require-not (xpc-service-name "com.apple.STSXPCHelper"))
 		(require-not (xpc-service-name "com.apple.extensionkitservice"))
+		(require-not (xpc-service-name "com.apple.AppleDeviceQueryService"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.nfc.GenericURLProcessor")
+			(xpc-service-name "com.apple.stockholm.services.NFRadarCommentService")
 			(xpc-service-name "com.apple.stockholm.services.NFRadioPowerSwitch")
 			(xpc-service-name "com.apple.stockholm.services.NFReportingService")
 			(xpc-service-name "com.apple.stockholm.services.NFRestoreService")
 			(xpc-service-name "com.apple.stockholm.services.NFStorageServer")
 			(xpc-service-name "com.apple.stockholm.services.NFUIService")
 		))
-		(require-not (xpc-service-name "com.apple.AppleDeviceQueryService"))
 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")

 		SIOCGIFEXPENSIVE
 		SIOCGIFFLAGS
 		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
 		SIOCGIFULTRACONSTRAINED)
 )
```
