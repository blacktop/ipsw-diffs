## schooltimed

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.contactsd"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
```
