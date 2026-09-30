## sensingpredictd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.wifip2pd"))
 		(require-not (global-name "com.apple.polaris.systemgraph"))
-		(require-not (global-name "com.apple.perceptiond.entitykit"))
 		(require-not (global-name "com.apple.coremedia.capturesource"))
 		(require-not (global-name "com.apple.coremedia.capturesession"))
+		(require-not (global-name "com.apple.perceptiond.entitykit"))
+		(require-not (global-name "com.apple.wifip2pd"))
 		(require-not (global-name "com.apple.AccessorySensorManager"))
 		(require-not (system-attribute developer-mode))
 	)
```
