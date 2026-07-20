## blastdoor-ids

> Group: ⬆️ Updated

```diff

 (deny mach-cross-domain-lookup)
 
 (deny mach-derive-port)
-(allow mach-derive-port
-	(global-name "com.apple.analyticsd")
-)
 
 (allow mach-lookup
 	(require-any
-		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.system.notification_center")
 	)
```
