## no-write-except-temporary

> Group: ⬆️ Updated

```diff

 
 (deny file-write-setugid)
 
+(deny qtn-exec-no-quarantine)
+(allow qtn-exec-no-quarantine
+	(require-ancestor-with-entitlement "com.apple.security.files.user-selected.executable")
+)
+
 (deny system-kas-info)
```
