## inputanalyticsd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.generativeexperiences.ExternalPartnerCredentialStorage"))
 		(require-not (xpc-service-name "com.apple.siri.context.service"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.apple.ctcategories.service"))
```
