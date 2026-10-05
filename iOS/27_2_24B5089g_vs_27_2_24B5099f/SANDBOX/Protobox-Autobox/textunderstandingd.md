## textunderstandingd

> Group: ⬆️ Updated

```diff

 			(xpc-service-name "com.apple.WebKit.WebContent")
 		))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (xpc-service-name "com.apple.Gestures.tracing.service.xpc"))
 		(require-not (xpc-service-name "com.apple.textunderstandingd.uihelper"))
 		(require-not (global-name "com.apple.ExternalAccessory.distributednotification.server"))
 		(require-not (global-name "com.apple.CARenderServer"))
```
