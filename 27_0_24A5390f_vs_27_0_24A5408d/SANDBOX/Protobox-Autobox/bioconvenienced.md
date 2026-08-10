## bioconvenienced

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.perceptiond.api"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.logd"))
 		(require-any
 			(process-attribute is-autoboxed)
 			(require-all
```
