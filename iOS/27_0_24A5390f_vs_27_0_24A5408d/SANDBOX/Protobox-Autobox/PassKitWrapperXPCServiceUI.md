## PassKitWrapperXPCServiceUI

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
+		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
```
