## cksharingmanagementd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (require-any
 			(global-name "com.apple.cloudkit.audience-provider.com.apple.family")
 			(global-name "com.apple.cloudkit.audience-provider.com.apple.people.circles")
 		))
+		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (system-attribute developer-mode))
 	)
```
