## nfcd

> Group: ⬆️ Updated

```diff

 ;; (default) inherited from parent profile "baseline"
 (delegate default)
 
-(allow asr-parser-enter)
+(deny asr-parser-enter
+	(asr-parser-domain ASR_DOMAIN_IMAGES)
+)
 
 (allow coalition-info)
 
```
