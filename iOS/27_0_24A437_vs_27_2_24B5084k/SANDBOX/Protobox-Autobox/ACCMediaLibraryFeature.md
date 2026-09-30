## ACCMediaLibraryFeature

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.lsd.xpc"))
 		(require-not (global-name "com.apple.xpc.amsengagementd"))
 		(require-not (global-name "com.apple.tccd"))
-		(require-not (global-name "com.apple.MediaPlayer.MPRadioControllerServer"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
-		(require-not (global-name "com.apple.Music.MPMusicPlayerControllerInternal"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
+		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.privacyaccountingd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.mediaremoted.xpc"))

 		(require-not (global-name "com.apple.itunescloudd.xpc"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
 		(require-not (global-name "com.apple.dnssd.service"))
-		(require-not (global-name "com.apple.SystemConfiguration.DNSConfiguration"))
+		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.medialibraryd.xpc"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.xpc.amstoold"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.xpc.amsaccountsd"))
-		(require-not (global-name "com.apple.ProgressReporting"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
+		(require-not (global-name "com.apple.MediaPlayer.MPRadioControllerServer"))
+		(require-not (global-name "com.apple.Music.MPMusicPlayerControllerInternal"))
+		(require-not (global-name "com.apple.SystemConfiguration.DNSConfiguration"))
+		(require-not (global-name "com.apple.ProgressReporting"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-any
 			(process-attribute is-autoboxed)
```
