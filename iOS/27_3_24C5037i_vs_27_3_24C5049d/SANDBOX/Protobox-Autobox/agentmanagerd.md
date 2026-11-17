## agentmanagerd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.biome.PublicStreamAccessService"))
+		(require-not (global-name "com.apple.photos.service"))
+		(require-not (global-name "com.apple.privacyaccountingd"))
 		(require-not (global-name "com.apple.spotlightknowledged"))
+		(require-not (global-name "com.apple.generativesearch.server.search"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (system-attribute developer-mode))
```
