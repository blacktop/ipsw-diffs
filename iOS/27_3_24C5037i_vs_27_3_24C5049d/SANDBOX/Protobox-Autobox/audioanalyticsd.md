## audioanalyticsd

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(iokit-registry-entry-class "AppleProcessorTraceUserClient")
+		(iokit-registry-entry-class "AppleSPUHIDDriverUserClient")
 		(iokit-registry-entry-class "IOHIDLibUserClient")
 		(iokit-registry-entry-class "IOReportUserClient")
 	)

 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.biome.compute.source"))
+		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.biome.access.system"))

 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.Carousel.wristmonitor"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.audio.AudioSession"))

 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
+		(require-not (global-name "com.apple.iohideventsystem"))
+		(require-not (global-name "com.apple.AttentionAwareness"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.FileCoordination"))

 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (xpc-service-name "com.apple.internal.audioanalytics.helper"))
 		(require-not (xpc-service-name "com.apple.ctcategories.service"))
-		(require-not (global-name "com.apple.Carousel.wristmonitor"))
-		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))
 	)
```
