## wifid

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.coremedia.endpoint.xpc"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
-		(require-not (require-any
-			(global-name "com.apple.findmy.findmylocate.friendshipservice")
-			(global-name "com.apple.findmy.findmylocate.settings")
-		))
+		(require-not (global-name "com.apple.findmy.findmylocate.friendshipservice"))
 		(require-not (global-name "com.apple.WirelessCoexManager"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.uservault"))

 		(require-not (global-name "com.apple.fontservicesd"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))
-		(require-not (xpc-service-name "com.apple.audioanalyticsd"))
+		(require-not (xpc-service-name "com.apple.audio.analytics.service"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.carkit.service"))

 		(require-not (global-name "com.apple.algosd"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (xpc-service-name "com.apple.audio.analytics.service"))
+		(require-not (global-name "com.apple.findmy.findmylocate.settings"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))

 		(require-not (xpc-service-name "com.apple.wifi.ThreeBarsXPCService"))
 		(require-not (xpc-service-name "com.apple.ZhuGeService"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (xpc-service-name "com.apple.audioanalyticsd"))
 		(require-not (global-name "com.apple.AccessorySetupUI"))
 		(require-not (system-attribute developer-mode))
 	)

 		vm_reallocate
 		mach_vm_read
 		mach_vm_copy
+		mach_vm_read_overwrite
 		mach_vm_map_external
 		mach_vm_remap_external
 		mach_vm_region_recurse

 
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
