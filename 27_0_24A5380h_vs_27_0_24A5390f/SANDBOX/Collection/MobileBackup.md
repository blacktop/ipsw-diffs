## MobileBackup

> Group: ⬆️ Updated

```diff

 	)
 )
 
-(deny job-creation)
+(deny isp-command-send)
+
+(deny qtn-exec)
+(allow qtn-exec
+	(require-ancestor-with-entitlement "com.apple.security.files.user-selected.executable")
+)
 
 (deny system-kas-info)
```
