## linkd

> Group: ⬆️ Updated

```diff

 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleKeyStore")
+		(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
 	)
 )
 

 		(require-not (require-any
 			(global-name "appevent-observer-5555494431be1e7467b03c4ca2ecb2488c22328b.appevent")
 			(global-name "com.apple.corespeech.corespeechd.uaapservice")
+			(global-name "com.apple.linkcli.appevent")
 			(global-name "com.apple.remoteappintentsd..appevent")
 			(global-name "com.apple.remoteappintentsd.appevent")
 			(global-name "com.apple.traj2intent.appeventobserver.appevent")
 		))
 		(require-not (global-name "com.apple.iap2d.xpc"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.appprotectiond.guard"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))

 		(require-not (global-name "com.apple.siri.vocabularyupdates"))
 		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
-		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
-		(require-not (xpc-service-name "com.apple.extensionkitservice"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.BreadBoardIntentsExtension")
 			(xpc-service-name "com.apple.HomeAppIntentsExtension")

 			(xpc-service-name "com.apple.mobilemail.MailShortcutsExtension")
 			(xpc-service-name "com.apple.omniSearch.SearchToolExtension")
 		))
+		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (xpc-service-name "com.apple.extensionkitservice"))
 		(require-not (xpc-service-name "com.apple.appintents.LiveEntityService"))
 		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-any

 
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
