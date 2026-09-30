## UserEventAgent

> Group: ⬆️ Updated

```diff

 
 (deny generic-issue-extension)
 
-(deny iokit-issue-extension)
+(deny iokit-get-properties)
 
-(deny iokit-open-user-client)
-(allow iokit-open-user-client
+(deny iokit-open*)
+(allow iokit-open*
 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")

 	)
 )
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(deny iokit-open-user-client)
+(allow iokit-open-user-client
 	(require-any
 		(iokit-registry-entry-class "AWCAccessoryManager")
 		(iokit-registry-entry-class "AppleAPFSContainer")

 	)
 )
 
-(deny iokit-set-properties
+(deny iokit-open-service
 	(require-all
 		(iokit-property "LinkStatus")
 		(require-not (iokit-registry-entry-class "AppleUSBEthernetDevice"))
 	)
 )
-(deny iokit-set-properties
+(deny iokit-open-service
 	(require-all
 		(require-any
 			(iokit-property "IOAccessoryPortUSBRoleSwitchMaskIndex")

 		(require-not (iokit-registry-entry-class "IOAccessoryPortUSB"))
 	)
 )
-(deny iokit-set-properties
+(deny iokit-open-service
 	(require-all
 		(require-any
 			(iokit-property "ThermalCoolDown")

 		(require-not (iokit-registry-entry-class "AppleHDQGasGaugeControl"))
 	)
 )
-(deny iokit-set-properties
+(deny iokit-open-service
 	(require-any
 		(require-not (iokit-registry-entry-class "AppleDialogPMU"))
 		(require-not (require-any

 	)
 )
 
+(deny iokit-set-properties)
+
 (deny ipc*)
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.*")
 		(ipc-posix-name "apple.cfprefs.daemonv1")

 	)
 )
 
-(deny ipc-posix-shm-write-data)
-(allow ipc-posix-shm-write-data
+(deny ipc-posix-shm-write-create)
+(allow ipc-posix-shm-write-create
 	(ipc-posix-name "apple.cfprefs.user.daemonv1")
 )
 
-(deny job-creation)
+(allow ipc-sysv-shm)
 
-(deny mach-issue-extension)
+(deny isp-command-send)
 
-(deny mach-lookup
+(deny mach-host-special-port-set)
+
+(deny mach-issue-extension
 	(xpc-service-name "com.apple.WebKit*")
 )
-(deny mach-lookup
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))

 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
 		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
+		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.SystemConfiguration.helper"))

 	)
 )
 
+(deny process-codesigning)
+(allow process-codesigning
+	(literal "/usr/bin/plutil")
+)
+
 (deny process-exec*)
 (allow process-exec*
 	(literal "/usr/bin/plutil")

 		SYS_sysctl
 		SYS_getumask
 		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
 		SYS_getattrlist
 		SYS_setattrlist
 		SYS_fgetattrlist
```
