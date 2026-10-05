## Photos

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.GameController.gamecontrollerd.app"))
 		(require-not (global-name "com.apple.ind.cloudfeatures"))
 		(require-not (global-name "com.apple.corefollowup.agent"))
+		(require-not (global-name "com.apple.siriactionsd.xpc"))
 		(require-not (global-name "com.apple.generativeexperiences.agentMediaStore"))
 		(require-not (require-any
 			(global-name "com.apple.proximitycamerad")

 			(xpc-service-name "com.sogou.sogouinput.basekeyboard")
 			(xpc-service-name "com.tencent.wetype.keyboard")
 		))
-		(require-not (xpc-service-name "com.navercorp.smartboard.extension"))
 		(require-not (xpc-service-name "com.swiftkey.SwiftKeyApp.Keyboard"))
+		(require-not (xpc-service-name "com.navercorp.smartboard.extension"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
