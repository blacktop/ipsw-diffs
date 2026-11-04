## donotdisturbd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.kvsd"))
 		(require-not (global-name "com.apple.linkd.transcript"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
-		(require-not (require-any
-			(global-name "com.apple.findmy.findmylocate.friendshipservice")
-			(global-name "com.apple.findmy.findmylocate.settings")
-		))
+		(require-not (global-name "com.apple.findmy.findmylocate.friendshipservice"))
 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))

 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.siri.VoiceShortcuts.xpc"))
-		(require-not (global-name "com.apple.appprotectiond.read"))
+		(require-not (global-name "com.apple.findmy.findmylocate.settings"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.personalization.notificationCategorization"))
+		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.contactsd.support"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.StatusKit.publish"))
+		(require-not (global-name "com.apple.linkd.application-service"))
 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))
 		(require-not (global-name "com.apple.logd.events"))

 		(require-not (global-name "com.apple.misagent"))
 		(require-not (global-name "com.apple.contactsd"))
 		(require-not (global-name "com.apple.calaccessd"))
-		(require-not (global-name "com.apple.PowerManagement.control"))
+		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
+		(require-not (global-name "com.apple.DeviceAccess.xpc"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))

 
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
