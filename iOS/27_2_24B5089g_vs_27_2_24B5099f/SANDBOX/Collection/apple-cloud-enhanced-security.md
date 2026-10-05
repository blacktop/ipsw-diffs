## apple-cloud-enhanced-security

> Group: ⬆️ Updated

```diff

 	(profile-flag "deny-lsopen")
 )
 
+(allow mach-bootstrap
+	(apply-message-filter
+		(allow mach-message-send)
+	)
+)
+
 (allow mach-derive-port)
 
 (allow mach-lookup
```
