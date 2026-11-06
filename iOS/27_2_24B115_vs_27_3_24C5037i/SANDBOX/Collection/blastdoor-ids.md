## blastdoor-ids

> Group: ⬆️ Updated

```diff

 
 (deny default)
 
+(deny asr-parser-enter)
+(allow asr-parser-enter
+	(require-not (asr-parser-domain ASR_DOMAIN_IMAGES))
+)
+(deny asr-parser-enter
+	(asr-parser-domain ASR_DOMAIN_IMAGES)
+)
+
 (deny darwin-notification-post)
 
 (deny dynamic-code-generation

 (deny mach-cross-domain-lookup)
 
 (deny mach-derive-port)
+(allow mach-derive-port
+	(global-name "com.apple.analyticsd")
+)
 
+(allow mach-lookup
+	(global-name "com.apple.analyticsd")
+)
 (deny mach-lookup
 	(with no-report)
 	(require-all
```
