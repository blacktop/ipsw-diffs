## generativesearchd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.generativesearch.server.search"))
-		(require-not (global-name "com.apple.locationd.synchronous"))
-		(require-not (global-name "com.apple.calaccessd"))
-		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.mediaanalysisd.analysis"))
-		(require-not (global-name "com.apple.contacts.poster.api"))
-		(require-not (global-name "com.apple.mediaanalysisd.service.public"))
-		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.generativelearning"))
-		(require-not (global-name "com.apple.photos.service"))
-		(require-not (global-name "com.apple.remindd"))
-		(require-not (global-name "com.apple.coreautomationd.xpc.mobile"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
-		(require-not (global-name "com.apple.privacyaccountingd"))
-		(require-not (global-name "com.apple.contactsd.support"))
-		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
+		(require-not (global-name "com.apple.accountsd.accountmanager"))
+		(require-not (global-name "com.apple.coreautomationd.xpc.mobile"))
+		(require-not (global-name "com.apple.SBUserNotification"))
+		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
+		(require-not (global-name "com.apple.photos.service"))
+		(require-not (global-name "com.apple.privacyaccountingd"))
+		(require-not (global-name "com.apple.locationd.synchronous"))
+		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.generativeexperiences.agentSessionStore"))
+		(require-not (global-name "com.apple.contactsd.support"))
+		(require-not (global-name "com.apple.mediaanalysisd.service.public"))
+		(require-not (global-name "com.apple.generativesearch.server.search"))
+		(require-not (global-name "com.apple.remindd"))
+		(require-not (global-name "com.apple.calaccessd"))
 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (global-name "com.apple.ABDatabaseDoctor"))
 		(require-not (system-attribute developer-mode))
```
