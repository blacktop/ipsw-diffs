## AccessibilityUIServer

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.inputservice.input-ui-host"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.mobilemail.services.xpc"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.iconservices"))

 		(require-not (global-name "com.apple.dt.xctestd.remote.target"))
 		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.lsd.xpc"))
+		(require-not (global-name "com.apple.ManagedSettingsAgent"))
 		(require-not (global-name "com.apple.apsd"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.backboard.hid-services.xpc"))
-		(require-not (global-name "com.apple.Carousel.CSLSDetentService"))
+		(require-not (require-any
+			(global-name "com.apple.Carousel.CSLSDetentService")
+			(global-name "com.apple.uikit.viewservice.com.apple.QuickboardViewService")
+		))
 		(require-not (global-name "com.apple.hangtelemetryd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))

 		(require-not (global-name "com.apple.carousel.connectionstatusservice"))
 		(require-not (global-name "com.apple.systemstatus.publisher"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
+		(require-not (global-name "com.apple.DeviceConfigurationAgent.publisher"))
 		(require-not (global-name "com.apple.photos.service"))
 		(require-not (global-name "com.apple.controlcenter.remoteservice"))
 		(require-not (global-name "com.apple.modelcatalog.catalog"))
 		(require-not (global-name "com.apple.relatived.public"))
 		(require-not (global-name "com.apple.campo"))
+		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.carkit.service"))
 		(require-not (global-name "com.apple.assistivetouchd"))

 		(require-not (global-name "com.apple.audio.AudioUnitServer"))
 		(require-not (global-name "com.apple.TextInput.image-cache-server"))
 		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (global-name "com.apple.appprotectiond.viewsubjectinfo"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.conversationmanager"))
 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.sirittsd"))

 		(require-not (global-name "com.apple.breadboardservices"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
 		(require-not (global-name "com.apple.coreduetd.context"))
-		(require-not (global-name "com.apple.uikit.viewservice.com.apple.QuickboardViewService"))
 		(require-not (global-name "com.apple.rti-stagertool"))
 		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
 		(require-not (global-name "com.apple.carousel.backlightxpc"))
```
