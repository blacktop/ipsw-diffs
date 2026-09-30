## powerd

> Group: ⬆️ Updated

```diff

 	)
 )
 
-(deny process-exec*)
+(deny process-exec*
+	(require-any
+		(require-not (require-any
+			(literal "/usr/local/bin/ulpm_reload_sb.sh")
+			(literal "/usr/local/bin/ulpm_sfi.sh")
+		))
+		(require-not (system-attribute internal-build))
+	)
+)
+
+(deny process-exec-interpreter
+	(require-all
+		(require-not (literal "/bin/sh"))
+		(require-any
+			(require-not (require-any
+				(literal "/usr/local/bin/ulpm_reload_sb.sh")
+				(literal "/usr/local/bin/ulpm_sfi.sh")
+			))
+			(require-not (system-attribute internal-build))
+		)
+	)
+)
 
 (deny socket-ioctl)
 
```
