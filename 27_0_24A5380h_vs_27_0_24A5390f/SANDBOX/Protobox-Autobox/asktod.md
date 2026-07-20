## asktod

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
 		(iokit-registry-entry-class "AppleJPEGDriverUserClient")
 		(iokit-registry-entry-class "IOGPUDeviceUserClient")
+		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
 		(iokit-registry-entry-class "IOSurfaceRootUserClient")
 	)
 )
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(deny iokit-open-user-client)
+(allow iokit-open-user-client
 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleJPEGDriver")

 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 	)
 )
 
-(deny job-creation)
+(allow ipc-sysv-shm)
 
-(deny mach-issue-extension)
+(deny isp-command-send)
 
-(deny mach-lookup
+(deny mach-host-special-port-set)
+
+(deny mach-issue-extension
 	(require-all
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.lsd.icons"))

 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.synapse.backlink-service"))
 		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.communication"))
 		(require-not (global-name "com.apple.coreduetd.people"))

 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 (allow socket-ioctl
 	(ioctl-command

 		mach_exception_raise_state_identity
 		io_iterator_next
 		io_registry_entry_from_path
+		io_service_close
 		io_service_open_extended
 		io_connect_method
 		io_connect_async_method
```
