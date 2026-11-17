## spotlightknowledged

> Group: ⬆️ Updated

```diff

 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (global-name "com.apple.ciphermld"))
 		(require-not (global-name "com.apple.spotlight.IndexAgent"))
-		(require-not (global-name "com.apple.generativesearch.server.indexing"))
+		(require-not (require-any
+			(global-name "com.apple.generativesearch.server.indexing")
+			(global-name "com.apple.generativesearch.server.salientpostings")
+		))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.corespotlight.powerlog"))
-		(require-not (global-name "com.apple.generativesearch.server.salientpostings"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.spotlight.SearchAgent"))
 		(require-not (global-name "com.apple.cache_delete.public"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))

 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.research.adtcd"))
-		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.ERFoundationExtensionDaemon"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
```
