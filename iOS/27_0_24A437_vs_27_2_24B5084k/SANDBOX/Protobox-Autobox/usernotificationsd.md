## usernotificationsd

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.biome.access.user"))
+		(require-not (global-name "com.apple.linkd.registry"))
 		(require-not (global-name "com.apple.replicatorservices"))
 		(require-not (global-name "com.apple.suggestd.contacts"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
```
