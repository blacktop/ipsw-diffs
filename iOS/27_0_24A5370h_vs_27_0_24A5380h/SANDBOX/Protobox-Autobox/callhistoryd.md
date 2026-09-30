## callhistoryd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.contacts.poster.api"))
-		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (global-name "com.apple.geod"))
+		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
+		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (global-name "com.apple.CallHistorySyncHelper"))
 		(require-not (system-attribute developer-mode))
 	)
```
