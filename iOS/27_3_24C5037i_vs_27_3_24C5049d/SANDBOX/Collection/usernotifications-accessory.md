## usernotifications-accessory

> Group: ⬆️ Updated

```diff

 
 (allow mach-derive-port)
 
+(allow mach-lookup
+	(require-any
+		(global-name "com.apple.coremedia.videocodecd.decompressionsession")
+		(global-name "com.apple.coremedia.videocodecd.decompressionsession.xpc")
+	)
+)
+
 (allow mach-task-exception-port-set)
 
 (allow mach-task-inspect
```
