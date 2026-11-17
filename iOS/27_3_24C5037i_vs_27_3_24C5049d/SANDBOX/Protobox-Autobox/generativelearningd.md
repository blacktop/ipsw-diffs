## generativelearningd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.spotlight.IndexAgent"))
 		(require-not (global-name "com.apple.proactive.ActionPrediction.predictions"))
-		(require-not (global-name "com.apple.generativesearch.server.indexing"))
+		(require-not (require-any
+			(global-name "com.apple.generativesearch.server.indexing")
+			(global-name "com.apple.generativesearch.server.salientpostings")
+		))
 		(require-not (global-name "com.apple.symptom_analytics"))
 		(require-not (global-name "com.apple.linkd.autoShortcut"))
-		(require-not (global-name "com.apple.generativesearch.server.salientpostings"))
+		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-not (global-name "com.apple.springboard.backgroundappservices"))
 		(require-not (global-name "com.apple.photos.service"))
 		(require-not (global-name "com.apple.intelligenceplatform.View"))

 		(require-not (global-name "com.apple.contactsd"))
 		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
-		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.ABDatabaseDoctor"))
```
