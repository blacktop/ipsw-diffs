## agentstored

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
+		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
 	)
 )
 
 (deny iokit-open-service)
 (allow iokit-open-service
-	(iokit-registry-entry-class "AppleKeyStore")
+	(require-any
+		(iokit-registry-entry-class "AppleKeyStore")
+		(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
+	)
 )
 
 (deny iokit-set-properties)

 		(require-not (global-name "com.apple.linkd.autoShortcut"))
 		(require-not (global-name "com.apple.fontservicesd"))
 		(require-not (global-name "com.apple.photos.service"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.generativesearch.server.search"))
+		(require-not (global-name "com.apple.ProgressReporting"))
 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))

 			SYS_getumask
 			SYS_open_dprotected_np
 			SYS_openat_dprotected_np
+			SYS_setattrlist
 			SYS_fgetattrlist
 			SYS_fsetattrlist
 			SYS_fgetxattr
```
