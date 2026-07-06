## racoon

> Group: ⬆️ Updated

```diff

 				(literal "/private/preboot")
 				(process-attribute is-apple-signed-executable)
 			)
+			(require-all
+				(subpath "/")
+				(process-attribute is-apple-signed-executable)
+			)
 		)
 	)
 )

 				(literal "/private/preboot")
 				(process-attribute is-apple-signed-executable)
 			)
+			(require-all
+				(subpath "/")
+				(process-attribute is-apple-signed-executable)
+			)
 		)
 	)
 )

 )
 
 (allow sysctl*
-	(require-all
-		(require-not (sysctl-name "vm.footprint_suspend"))
-		(require-not (sysctl-name "vm.task_no_footprint_for_debug"))
-		(require-not (sysctl-name "net.inet.ipsec.debug"))
-		(require-any
-			(sysctl-name "kern.ipc.maxsockbuf")
-			(sysctl-name "net.inet.ipsec.esp_port")
-		)
+	(require-any
+		(sysctl-name "kern.ipc.maxsockbuf")
+		(sysctl-name "net.inet.ipsec.esp_port")
 	)
 )
 
```
