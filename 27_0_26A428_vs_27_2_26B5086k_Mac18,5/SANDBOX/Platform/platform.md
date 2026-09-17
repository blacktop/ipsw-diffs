## platform

> Group: ⬆️ Updated

```diff

 (version 1)
 (allow default)
 
+(allow asr-parser-enter
+	(require-not (asr-parser-domain ASR_DOMAIN_IMAGES))
+)
+
 (deny boot-arg-set
 	(with sip-override)
 	(require-not (require-any
```
