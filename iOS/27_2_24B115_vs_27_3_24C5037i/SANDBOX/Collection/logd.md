## logd

> Group: ⬆️ Updated

```diff

 (delegate default)
 
 (allow asr-parser-enter)
+(deny asr-parser-enter
+	(asr-parser-domain ASR_DOMAIN_IMAGES)
+)
 
 (allow coalition-info)
 
```
