## platform

> Group: ⬆️ Updated

```diff

 	)
 )
 
+(allow qtn-exec
+	(with authority)
+	(ancestor-signing-identifier "com.apple.WorkflowKit.BackgroundShortcutRunner")
+)
+(allow qtn-exec)
+
 (deny sandbox-check
 	(require-all
 		(filesystem-name "devfs")
```
