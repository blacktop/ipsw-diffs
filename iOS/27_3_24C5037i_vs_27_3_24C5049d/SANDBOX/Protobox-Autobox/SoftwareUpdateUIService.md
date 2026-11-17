## SoftwareUpdateUIService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.hangtracerd"))
 		(require-not (global-name "com.apple.softwareupdateservicesd"))
 		(require-not (global-name "com.apple.iap2d.xpc"))
-		(require-not (global-name "com.apple.rti-screencontinuity"))
+		(require-not (require-any
+			(global-name "com.apple.remote-text-editing-legacy")
+			(global-name "com.apple.rti-screencontinuity")
+			(global-name "com.apple.sharing.remote-text-editing")
+		))
 		(require-not (global-name "com.apple.UIKit.KeyboardManagement.hosted"))
 		(require-not (global-name "com.apple.PrototypeTools.domainserver"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))

 		(require-not (global-name "com.apple.dasd.end-prewarm"))
 		(require-not (global-name "com.apple.biometrickitd"))
 		(require-not (global-name "com.apple.muranod.listener"))
-		(require-not (require-any
-			(global-name "com.apple.remote-text-editing-legacy")
-			(global-name "com.apple.sharing.remote-text-editing")
-		))
 		(require-not (global-name "com.apple.aa.daemon.xpc"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.handwritingd.remoterecognition"))
```
