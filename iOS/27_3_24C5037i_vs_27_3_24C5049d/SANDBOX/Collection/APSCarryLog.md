## APSCarryLog

> Group: ⬆️ Updated

```diff

 
 (allow necp-client-open)
 
+(allow nvram-get
+	(nvram-variable "obliteration")
+)
+
 (allow process-codesigning)
 
 (allow process-info-codesignature)
```
