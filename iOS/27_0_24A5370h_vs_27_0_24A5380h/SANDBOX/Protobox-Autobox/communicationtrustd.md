## communicationtrustd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.symptom_diagnostics"))
+		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.accountsd.accountmanager"))
+		(require-not (global-name "com.apple.cmfsyncagent.embedded.auth"))
+		(require-not (global-name "com.apple.privacyaccountingd"))
+		(require-not (global-name "com.apple.contacts.poster.api"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
+		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
+		(require-not (global-name "com.apple.corerecents.recentsd"))
+		(require-not (global-name "com.apple.familycircle.agent"))
 		(require-not (global-name "com.apple.contactsd"))
 		(require-not (global-name "com.apple.sharingd.pairedcontactmanager"))
-		(require-not (global-name "com.apple.accountsd.accountmanager"))
-		(require-not (global-name "com.apple.contacts.poster.api"))
-		(require-not (global-name "com.apple.familycircle.agent"))
-		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.appprotectiond.read"))
-		(require-not (global-name "com.apple.symptom_diagnostics"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
-		(require-not (global-name "com.apple.privacyaccountingd"))
-		(require-not (global-name "com.apple.corerecents.recentsd"))
-		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
-		(require-not (global-name "com.apple.cmfsyncagent.embedded.auth"))
 		(require-not (xpc-service-name "com.apple.CallKit.CallDirectory"))
 		(require-not (global-name "com.apple.ABDatabaseDoctor"))
 		(require-not (system-attribute developer-mode))
```
