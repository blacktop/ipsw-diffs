## NTKFaceSnapshotService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.photosface"))
 		(require-not (global-name "com.apple.iapd.xpc"))
 		(require-not (global-name "com.apple.pluginkit.pkd"))
+		(require-not (global-name "com.apple.carousel.connectionstatusservice"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
 		(require-not (global-name "com.apple.fontservicesd"))
 		(require-not (require-any

 		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession.xpc"))
+		(require-not (global-name "com.apple.EligibilityQuorum.com.apple.AudioIntelligence"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.chronoservices"))

 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.gputools.service"))
+		(require-not (global-name "com.apple.remindd"))
 		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))
 		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
```
