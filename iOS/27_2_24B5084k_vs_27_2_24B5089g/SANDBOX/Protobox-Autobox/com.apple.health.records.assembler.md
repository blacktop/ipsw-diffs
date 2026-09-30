## com.apple.health.records.assembler

> Group: ⬆️ Updated

```diff

 
 (deny mach-issue-extension)
 
-(deny mach-lookup)
+(deny mach-lookup
+	(require-all
+		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.fontservicesd"))
+		(require-not (system-attribute developer-mode))
+	)
+)
 
 (deny process-exec*)
 
```
