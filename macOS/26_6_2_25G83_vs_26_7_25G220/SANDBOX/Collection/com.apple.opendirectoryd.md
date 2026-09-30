## com.apple.opendirectoryd

> Group: ⬆️ Updated

```diff

 
 (deny process-legacy-codesigning*)
 
+(deny qtn-exec-no-quarantine)
+(allow qtn-exec-no-quarantine
+	(require-ancestor-with-entitlement "com.apple.security.files.user-selected.executable")
+)
+
 (deny system-kas-info)
```
