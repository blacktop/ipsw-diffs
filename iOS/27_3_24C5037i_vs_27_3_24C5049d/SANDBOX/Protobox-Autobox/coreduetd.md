## coreduetd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.contactsd"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.Topic.readOnly"))
 		(require-not (global-name "com.apple.calaccessd"))
+		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (require-any
 			(xpc-service-name "apple.PeopleSuggesterXPCAgent")
 			(xpc-service-name "com.apple.PeopleSuggesterXPCAgent")
```
