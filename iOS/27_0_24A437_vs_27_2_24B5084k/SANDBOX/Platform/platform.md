## platform

> Group: ⬆️ Updated

```diff

 (version 1)
 (allow default)
 
+(allow asr-parser-enter
+	(require-not (asr-parser-domain ASR_DOMAIN_IMAGES))
+)
+
 (allow dynamic-code-generation
 	(require-all
 		(process-attribute is-sandboxed)
```
