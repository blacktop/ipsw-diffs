## ndoagent

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.xpc.amstreatmentstoreservice"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))

 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.xpc.activity.control"))
-		(require-not (global-name "com.apple.AccessoryServices"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.corefollowup.agent"))
 		(require-not (global-name "com.apple.adid"))

 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (global-name "com.apple.AppSSO.service-xpc"))
+		(require-not (global-name "com.apple.AccessoryServices"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		semaphore_create
 		semaphore_destroy
 		task_set_exc_guard_behavior
+		task_create_identity_token
 		thread_terminate
 		thread_info
 		thread_policy
```
