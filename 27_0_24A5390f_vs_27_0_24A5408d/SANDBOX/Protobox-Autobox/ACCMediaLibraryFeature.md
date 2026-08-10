## ACCMediaLibraryFeature

> Group: ⬆️ Updated

```diff

 (allow default)
 
 (deny file-ioctl
-	(with no-report)
 	(process-attribute is-autoboxed)
 )
+(allow file-ioctl
+	(require-all
+		(process-attribute is-autoboxed)
+		(ioctl-command (_IO "h" 4))
+	)
+)
 
 (deny generic-issue-extension
 	(with no-report)

 
 (deny mach-lookup
 	(require-all
+		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.lsd.xpc"))
+		(require-not (global-name "com.apple.xpc.amsengagementd"))
 		(require-not (global-name "com.apple.tccd"))
+		(require-not (global-name "com.apple.MediaPlayer.MPRadioControllerServer"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.Music.MPMusicPlayerControllerInternal"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))

 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.itunescloudd.xpc"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
+		(require-not (global-name "com.apple.dnssd.service"))
+		(require-not (global-name "com.apple.SystemConfiguration.DNSConfiguration"))
 		(require-not (global-name "com.apple.medialibraryd.xpc"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.xpc.amstoold"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.xpc.amsaccountsd"))
 		(require-not (global-name "com.apple.ProgressReporting"))

 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
-		(require-not (global-name "com.apple.MediaPlayer.MPRadioControllerServer"))
+		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-any
 			(process-attribute is-autoboxed)
 			(require-all
```
