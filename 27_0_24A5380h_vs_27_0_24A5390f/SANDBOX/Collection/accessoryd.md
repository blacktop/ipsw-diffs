## accessoryd

> Group: ⬆️ Updated

```diff

 
 (allow fs-snapshot-mount)
 
-(allow iokit-get-properties)
+(allow iokit*)
 
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(system-attribute virtual-device)
 		(require-any

 		)
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-any
 		(extension "com.apple.security.exception.iokit-user-client-class")
 		(iokit-connection "IOGPU")

 	)
 )
 
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-any
 		(%entitlement-is-present "com.apple.security.exception.iokit-user-client-class")
 		(iokit-registry-entry-class "AGXAcceleratorG*")

 	)
 )
 
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-registry-entry-class "IOUSBHostDevice")
 		(require-any

 		)
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-registry-entry-class "IODPController")
 		(require-any

 	)
 )
 
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-all
 		(ipc-posix-name "apple.shm.notification_center")
 		(require-not (%entitlement-is-bool-true "com.apple.security.on-demand-install-capable"))
 	)
 )
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(ipc-posix-name "/com.apple.AppSSO.version")
 )
 
-(deny job-creation)
+(deny isp-command-send)
 
-(deny lsopen
+(deny job-creation
 	(profile-flag "deny-lsopen")
 )
 
-(allow mach-bootstrap)
+(allow mach*)
 
-(allow mach-cross-domain-lookup)
-
-(allow mach-derive-port)
-
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.ak.auth.xpc")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.networkd_privileged")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.ak.anisette.xpc")
 		(process-attribute is-apple-signed-executable)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.system.notification_center")
 		(%entitlement-is-bool-true "com.apple.security.on-demand-install-capable")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-any
 		(extension "com.apple.security.exception.mach-lookup.global-name")
 		(extension "com.apple.security.exception.mach-lookup.local-name")

 		(xpc-service-name "com.apple.externalaccessory.WACEAService")
 	)
 )
-(deny mach-lookup
+(deny mach-issue-extension
 	(require-any
 		(xpc-service-name "com.apple.CoreGraphics.CGPDFService")
 		(xpc-service-name "com.apple.WebKit.*")
 	)
 )
 
-(allow mach-register
+(allow mach-priv-task-port
 	(require-any
 		(extension "com.apple.security.exception.mach-register.global-name")
 		(global-name "com.apple.ExternalAccessory.distributednotification.server")

 	)
 )
 
-(allow mach-task-exception-port-set)
+(allow mach-task-exception-port-set
+	(target self)
+)
 
 (allow mach-task-inspect
 	(target self)

 	(target self)
 )
 
-(allow mach-task-read
-	(target self)
+(allow network*
+	(require-any
+		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
+		(local udp "*:*")
+	)
 )
 
-(allow mach-task-special-port*)
-
-(allow necp-client-open)
-
+(allow network-inbound
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/ExternalAccessory/ea[.0-9]+$")
+		(subpath "${FRONT_USER_HOME}")
+	)
+)
 (allow network-inbound
 	(require-any
 		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")

 )
 
 (allow network-bind
-	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/ExternalAccessory/ea[.0-9]+$")
-		(subpath "${FRONT_USER_HOME}")
-	)
-)
-(allow network-bind
-	(require-any
-		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
-		(local udp "*:*")
-	)
-)
-
-(allow network-outbound
 	(require-all
 		(vnode-type SOCKET)
 		(literal "${FRONT_USER_HOME}/Library/ExternalAccessory/ea*")
 	)
 )
-(allow network-outbound
+(allow network-bind
 	(require-any
 		(control-name "com.apple.flow-divert")
 		(control-name "com.apple.netsrc")

 	)
 )
 
+(allow network-outbound)
+
 (allow nvram*)
 
-(allow process-codesigning)
+(allow process*)
+
+(allow process-codesigning
+	(require-any
+		(literal "/System/Library/PrivateFrameworks/IAP.framework/Support/iap2d")
+		(literal "/System/Library/PrivateFrameworks/IAP.framework/Support/iapd")
+	)
+)
 
 (allow process-exec*
 	(require-any

 	)
 )
 
-(allow process-info*)
-
-(allow process-iopolicy*)
-
 (allow sandbox-check)
 
 (allow signal

 )
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
