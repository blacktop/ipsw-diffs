## apple-cloud-enhanced-security

> Group: ⬆️ Updated

```diff

 	(profile-flag "deny-lsopen")
 )
 
+(allow mach-bootstrap
+	(apply-message-filter
+		(deny mach-message-send)
+		(allow mach-message-send
+			(require-any
+				(message-number 206 207 711 712 718 800 803 804 805 904)
+				(require-all
+					(message-number 802)
+					(require-not (state-flag "blastdoor-post-launch"))
+				)
+			)
+		)
+	)
+)
+
 (allow mach-derive-port)
 
 (allow mach-lookup
```
