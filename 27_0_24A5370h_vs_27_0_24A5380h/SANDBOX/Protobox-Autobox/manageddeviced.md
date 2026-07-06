## manageddeviced

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.mobile.installd"))
-		(require-not (global-name "com.apple.inputservice.keyboardui"))
-		(require-not (global-name "com.apple.itunesstored.xpc"))
-		(require-not (global-name "com.apple.appstored.xpc.jobmanager"))
-		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
-		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.inputservice.keyboardui"))
+		(require-not (global-name "com.apple.appstored.xpc.jobmanager"))
+		(require-not (global-name "com.apple.timed.xpc"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
+		(require-not (global-name "com.apple.itunesstored.xpc"))
 		(require-not (xpc-service-name "com.apple.ctcategories.service"))
 		(require-not (system-attribute developer-mode))
 	)
```
