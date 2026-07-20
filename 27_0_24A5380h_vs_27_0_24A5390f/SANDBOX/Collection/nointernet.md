## nointernet

> Group: ⬆️ Updated

```diff

 
 (deny file-write-setugid)
 
+(deny necp-client-open
+	(with no-report)
+	(local ip "*:*")
+)
+
 (deny network*
 	(with no-report)
 	(local ip "*:*")
 )
 
-(deny network-outbound
+(deny network-bind
 	(local ip "*:*")
 )
-(allow network-outbound
+(allow network-bind
 	(require-all
 		(local ip "*:*")
 		(control-name "com.apple.flow-divert")
 	)
 )
 
+(deny qtn-exec)
+(allow qtn-exec
+	(require-ancestor-with-entitlement "com.apple.security.files.user-selected.executable")
+)
+
 (deny system-kas-info)
```
