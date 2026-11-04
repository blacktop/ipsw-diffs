## searchpartyd

> Group: ⬆️ Updated

```diff

 		))
 		(require-not (global-name "com.apple.apsd"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
+		(require-not (require-any
+			(xpc-service-name "com.apple.findmy.FindMySecureEnvironmentXPCService")
+			(xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceUserNotificationsXPCService")
+		))
 		(require-not (xpc-service-name "com.apple.findmy.locationqualityservice"))
-		(require-not (xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceUserNotificationsXPCService"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
-		(require-not (require-any
-			(global-name "com.apple.findmy.findmylocate.friendshipservice")
-			(global-name "com.apple.findmy.findmylocate.settings")
-		))
+		(require-not (global-name "com.apple.findmy.findmylocate.friendshipservice"))
 		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))

 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.findmy.findmylocate.fencesservice"))
-		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
+		(require-not (global-name "com.apple.spotlight.SearchAgent"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.nfcd.hwmanager"))
-		(require-not (global-name "com.apple.spaceattributiond"))
+		(require-not (global-name "com.apple.findmy.findmylocate.settings"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.locationd.routine"))
-		(require-not (global-name "com.apple.spotlight.IndexDelegateAgent"))
+		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
 		(require-not (global-name "com.apple.icloud.findmydeviced"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
 		(require-not (global-name "com.apple.terminusd"))
+		(require-not (global-name "com.apple.linkd.application-service"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.chronoservices"))
 		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))

 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
 		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.contactsd"))
+		(require-not (global-name "com.apple.spotlight.IndexDelegateAgent"))
 		(require-not (global-name "com.apple.familycircle.agent"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.routined.registration"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.spotlight.SearchAgent"))
+		(require-not (global-name "com.apple.contactsd"))
+		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (global-name "com.apple.Carousel.wristmonitor"))
 		(require-not (system-attribute developer-mode))
 	)

 
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
