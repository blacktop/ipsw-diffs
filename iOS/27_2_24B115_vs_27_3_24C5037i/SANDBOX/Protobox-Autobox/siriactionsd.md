## siriactionsd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
 		(require-not (global-name "com.apple.linkd.extension"))
 		(require-not (global-name "com.apple.appleneuralengine"))
+		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))

 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.spotlight.IndexAgent"))
 		(require-not (global-name "com.apple.coreservices.lsuseractivitymanager.xpc"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))

 		(require-not (global-name "com.apple.commcenter.xpc"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.springboard.services"))
 		(require-not (global-name "com.apple.backboard.display.services"))
 		(require-not (global-name "com.apple.sessionservices"))
 		(require-not (global-name "com.apple.pasteboard.pasted"))

 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.donotdisturb.service.non-launching"))
 		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.parsecd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))

 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
-				(require-not (global-name "com.apple.CARenderServer"))
 				(require-not (global-name "com.apple.AudioAccessoryServices"))
 				(require-not (system-attribute developer-mode))
 			)

 				(xpc-service-name "*")
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
-				(require-not (global-name "com.apple.CARenderServer"))
 				(require-not (global-name "com.apple.AudioAccessoryServices"))
 				(require-not (system-attribute developer-mode))
 			)

 (allow socket-ioctl
 	(ioctl-command
 		CTLIOCGINFO
+		SIOCGCONNINFO
 		SIOCGIFAGENTDATA
 		SIOCGIFCONSTRAINED
 		SIOCGIFDELEGATE

 
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
