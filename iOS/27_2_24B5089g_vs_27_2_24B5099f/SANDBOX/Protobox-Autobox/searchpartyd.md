## searchpartyd

> Group: ⬆️ Updated

```diff

 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.nfcd.hwmanager"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.locationd.routine"))
-		(require-not (global-name "com.apple.contactsd"))
+		(require-not (global-name "com.apple.spotlight.IndexDelegateAgent"))
 		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
 		(require-not (global-name "com.apple.icloud.findmydeviced"))
 		(require-not (global-name "com.apple.diagd"))

 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
 		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.spaceattributiond"))
+		(require-not (global-name "com.apple.contactsd"))
 		(require-not (global-name "com.apple.familycircle.agent"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.routined.registration"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.spotlight.SearchAgent"))
 		(require-not (global-name "com.apple.Carousel.wristmonitor"))
 		(require-not (system-attribute developer-mode))
 	)
```
