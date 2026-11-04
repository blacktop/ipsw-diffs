## mediaremoted

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (require-any
+			(global-name "com.apple.aeroml.intentrecommend.mediasuggester")
 			(global-name "com.apple.mediaremoteui-pebble.services")
 			(global-name "com.apple.mediaremoteui.services")
 		))

 		(require-not (global-name "com.apple.ProgressReporting"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (xpc-service-name "com.apple.appintents.LiveEntityService"))
 		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))

 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (xpc-service-name "com.apple.NeighborhoodActivityConduitService"))
 		(require-not (xpc-service-name "com.apple.SharePlay.GroupSessionService"))
-		(require-not (xpc-service-name "com.apple.appintents.LiveEntityService"))
 		(require-not (global-name "com.apple.CompanionLink"))
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
