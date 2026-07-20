## ACCNowPlayingFeature

> Group: ⬆️ Updated

```diff

 	(process-attribute is-autoboxed)
 )
 
-(deny iokit-issue-extension
+(deny iokit-get-properties
 	(with no-report)
 	(process-attribute is-autoboxed)
 )
 
-(deny iokit-open-user-client
+(deny iokit-open*
 	(process-attribute is-autoboxed)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(process-attribute is-autoboxed)
 		(require-any
 			(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 			(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
+			(iokit-registry-entry-class "AppleJPEGDriverUserClient")
+			(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
+			(iokit-registry-entry-class "IOSurfaceRootUserClient")
 		)
 	)
 )
 
+(deny iokit-open-service
+	(with no-report)
+	(process-attribute is-autoboxed)
+)
+
 (deny iokit-set-properties
 	(with no-report)
 	(process-attribute is-autoboxed)

 	(process-attribute is-autoboxed)
 )
 
-(deny ipc-posix-shm-read-data
+(deny ipc-posix-shm*
 	(process-attribute is-autoboxed)
 )
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-all
 		(process-attribute is-autoboxed)
 		(require-any

 	)
 )
 
-(deny job-creation
+(deny isp-command-send
+	(with no-report)
+	(process-attribute is-autoboxed)
+)
+
+(deny mach-host-special-port-set
 	(with no-report)
 	(process-attribute is-autoboxed)
 )
 
 (deny mach-issue-extension
-	(with no-report)
-	(process-attribute is-autoboxed)
-)
-
-(deny mach-lookup
 	(require-all
 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.lsd.xpc"))
+		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
 		(require-not (global-name "com.apple.tccd"))
+		(require-not (global-name "com.apple.coremedia.admin"))
 		(require-not (global-name "com.apple.itunescloudd.tcchelper"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))

 	)
 )
 
+(deny process-codesigning
+	(with no-report)
+	(process-attribute is-autoboxed)
+)
+
 (deny process-exec*
 	(with no-report)
 	(process-attribute is-autoboxed)
```
