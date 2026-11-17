## prototyped

> Group: ⬆️ Updated

```diff

 (allow iokit-open-service
 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
+		(iokit-registry-entry-class "AppleJPEGDriver")
 		(iokit-registry-entry-class "AppleKeyStore")
 		(iokit-registry-entry-class "AppleParavirtGPU")
 		(iokit-registry-entry-class "AppleVirtIONeuralEngineDevice")

 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (global-name "com.apple.hangtracerd"))
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

 		(require-not (global-name "com.apple.biometrickitd"))
 		(require-not (global-name "com.apple.muranod.listener"))
 		(require-not (global-name "com.apple.sharing.sharesheet"))
-		(require-not (require-any
-			(global-name "com.apple.remote-text-editing-legacy")
-			(global-name "com.apple.sharing.remote-text-editing")
-		))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
 		(require-not (global-name "com.apple.UIKit.statusbarserver"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))

 		SYS_bsdthread_create
 		SYS_bsdthread_terminate
 		SYS_kqueue
+		SYS_kevent
 		SYS_lchown
 		SYS_bsdthread_register
 		SYS_workq_open

 		SYS_necp_client_action
 		SYS___channel_open
 		SYS___channel_get_info
+		SYS___channel_sync
 		SYS_ulock_wait
 		SYS_ulock_wake
 		SYS_terminate_with_payload
```
